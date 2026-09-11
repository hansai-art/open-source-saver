#!/usr/bin/env python3
"""Read app bundle metadata in known directories; never scan the whole disk."""
import argparse
import datetime as dt
import json
import os
import plistlib
import sys
from pathlib import Path
from saver import write_output


def collect(roots):
    applications, warnings, seen = [], [], set()
    for root in roots:
        if not root.is_dir():
            continue
        def denied(_error):
            warnings.append('A directory could not be read')
        for parent, dirs, _files in os.walk(root, followlinks=False, onerror=denied):
            depth = len(Path(parent).relative_to(root).parts)
            for name in list(dirs):
                if not name.endswith('.app'):
                    continue
                dirs.remove(name)
                bundle = Path(parent) / name
                if bundle.is_symlink():
                    warnings.append('Symlinked app skipped')
                    continue
                try:
                    with (bundle / 'Contents/Info.plist').open('rb') as stream:
                        info = plistlib.load(stream)
                    if not isinstance(info, dict):
                        raise ValueError('App metadata must be a dictionary')
                    app_name = info.get('CFBundleDisplayName') or info.get('CFBundleName') or name[:-4]
                    version = str(info.get('CFBundleShortVersionString', ''))
                    bundle_id = str(info.get('CFBundleIdentifier', ''))
                    key = (bundle_id or str(app_name), version)
                    if key not in seen:
                        seen.add(key)
                        applications.append({'name': str(app_name), 'version': version, 'bundle_id': bundle_id})
                except (OSError, ValueError, TypeError, plistlib.InvalidFileException):
                    warnings.append('An app metadata file could not be read')
            if depth >= 2:
                dirs[:] = []
    return {'schema_version': 1, 'platform': 'macos', 'collector': 'known-app-directories',
            'collected_at': dt.datetime.now(dt.timezone.utc).isoformat(),
            'coverage': 'Application folders, at most two levels of subfolders; no full-disk, Homebrew formula or browser-extension inventory',
            'warnings': sorted(set(warnings)), 'applications': applications}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if sys.platform != 'darwin':
        print('This collector requires the target Mac. Use a manual inventory here.', file=sys.stderr)
        return 2
    try:
        data = collect([Path('/Applications'), Path.home() / 'Applications', Path('/System/Applications')])
        write_output(args.output, json.dumps(data, ensure_ascii=False, indent=2))
        print('Inventory saved locally; contents were not printed.')
    except OSError:
        print('Cannot save inventory. Check output existence and permissions.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
