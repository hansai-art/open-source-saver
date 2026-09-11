#!/usr/bin/env python3
"""Offline software discovery and conservative inventory matching; stdlib only."""
import argparse
import datetime as dt
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COST_ZH = {
    'free and open-source': '免費開源',
    'freeware; source-available, not open-source': '免費；原始碼可見，非開源',
    'free open-source desktop edition': '免費開源桌面版',
    'free tier; proprietary': '有免費版；非開源',
    'free/paid feature boundaries need review': '免費與付費功能界線待查',
    'freeware; not open-source': '免費軟體；非開源',
    'freeware; personal and commercial use': '個人與商用免費',
    'included with macOS; proprietary': 'macOS 內建；非開源',
    'limited free tier; proprietary': '有功能限制的免費版；非開源',
    'open-source; binary/model/service costs may differ': '開源；安裝包、模型與服務費用另查',
}


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def normalize(value):
    return ' '.join(unicodedata.normalize('NFKC', value).casefold().split())


def source_match(name, mappings):
    normalized = normalize(name)
    for mapping in mappings:
        for alias in mapping['aliases']:
            alias = normalize(alias)
            if normalized == alias:
                return mapping
            # Only explicitly permitted, product-specific version suffixes.
            if mapping.get('year_suffix') and re.fullmatch(re.escape(alias) + r' 20\d{2}(?:\.\d+)*', normalized):
                return mapping
    return None


def inventory(path):
    path = Path(path)
    if path.stat().st_size > 10_000_000:
        raise ValueError('Inventory exceeds 10 MB')
    warnings = []
    if path.suffix.lower() == '.json':
        raw = read_json(path)
        if isinstance(raw, dict):
            warnings = raw.get('warnings', [])
            raw = raw.get('applications')
        if not isinstance(raw, list):
            raise ValueError('JSON must be an array or an object with applications array')
    else:
        raw = path.read_text(encoding='utf-8-sig').splitlines()
    clean, seen = [], set()
    for row in raw:
        if isinstance(row, str):
            name = row.strip()
        elif isinstance(row, dict):
            name = row.get('name', row.get('display_name'))
        else:
            raise ValueError('Each item must be a string or a name object')
        if not isinstance(name, str):
            raise ValueError('Each application needs a string name')
        if not name.strip():
            continue
        if len(name) > 300:
            raise ValueError('Application name exceeds 300 characters')
        key = normalize(name)
        if key not in seen:
            seen.add(key)
            clean.append(name.strip())
    # Preserve coverage signal without copying potentially sensitive error contents.
    return clean, bool(warnings)


def eligible(product, platform, include_engines=False):
    if not include_engines and product['delivery'] == 'engine':
        return False
    if platform and platform not in product['platforms']:
        return False
    return True


def search(products, mappings, query, platform=None, include_engines=False):
    mapping = source_match(query, mappings)
    target_ids = mapping['targets'] if mapping else []
    query = normalize(query)
    scored = []
    for p in products:
        if not eligible(p, platform, include_engines):
            continue
        score = 0
        if p['id'] in target_ids:
            score = 100 - target_ids.index(p['id'])
        terms = [p['name'], p['category'], *p['keywords'], *p.get('aliases', [])]
        if query and any(query == normalize(t) for t in terms):
            score = max(score, 90)
        elif query and any(query in normalize(t) for t in terms):
            score = max(score, 30)
        if not query:
            score = 1
        if score:
            scored.append((score, p))
    return [p for _, p in sorted(scored, key=lambda item: (-item[0], item[1]['id']))]


def escape(value):
    # Application names and upstream strings are data, never Markdown instructions.
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '\\|').replace('\n', ' ').replace('\r', ' ').replace('`', "'").replace('[', '\\[').replace(']', '\\]')


def render(products, lang):
    zh = lang == 'zh-TW'
    header = '| 工具 | 用途 | 平台 | 費用 | 限制 | 證據 |' if zh else '| Tool | Use | OS | Cost | Limits | Evidence |'
    rows = [header, '|---|---|---|---|---|---|']
    for p in products:
        text = p['zh'] if zh else p['en']
        rows.append('| ' + ' | '.join([f"[{escape(p['name'])}]({p['url']})", escape(text['use']), ', '.join(p['platforms']) or ('待確認' if zh else 'Unknown'), escape(COST_ZH.get(p['cost'], p['cost']) if zh else p['cost']), escape(text['limits']), escape(p['evidence'] + ' / ' + p['checked_on'])]) + ' |')
    return '\n'.join(rows)


def report(names, products, mappings, platform, lang, has_warnings=False):
    zh = lang == 'zh-TW'
    lines = ['# 開源與免費軟體候選報告' if zh else '# Open-source and free software candidates', '', '本機快照配對；未驗證遷移可行性，不代表已付費或已省錢。' if zh else 'Local snapshot matching. Migration suitability, paid subscriptions and savings are not established.', '']
    if has_warnings:
        lines += ['收集器回報覆蓋限制；原始警告留在本機輸入檔。' if zh else 'Collector reported coverage limitations; original warnings remain in the local input.', '']
    grouped, unknown = {}, []
    for name in names:
        match = source_match(name, mappings)
        if match:
            grouped.setdefault(match['id'], match)
        else:
            unknown.append(name)
    for mapping in grouped.values():
        targets = [p for tid in mapping['targets'] for p in products if p['id'] == tid and eligible(p, platform)]
        lines += ['## ' + escape(mapping['name']), '', escape(mapping['zh_note'] if zh else mapping['en_note']), '']
        if targets:
            lines += [render(targets, lang), '']
        else:
            lines += ['指定平台沒有已知符合候選，需另查。' if zh else 'No known candidates for this platform; research required.', '']
    lines += ['## 未配對／需另查' if zh else '## Unmatched / research needed', '']
    lines += ['- ' + escape(n) for n in unknown] or ['無' if zh else 'None']
    lines += ['', f"Input names: {len(names)}; mapped product groups: {len(grouped)}; unmatched: {len(unknown)}.", 'Counts describe this input, not full-device coverage.', '']
    return '\n'.join(lines)


def write_output(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Refuse clobbering: inventory/report files may contain the user's own work.
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, 'w', encoding='utf-8') as stream:
        stream.write(content)


def validate(catalog, mappings):
    products = catalog['products']
    ids = {p['id'] for p in products}
    if len(ids) != len(products):
        raise ValueError('Duplicate product ID')
    aliases = set()
    for p in products:
        for field in ('name', 'category', 'delivery', 'platforms', 'cost', 'evidence', 'checked_on', 'zh', 'en', 'sources', 'keywords'):
            if field not in p:
                raise ValueError('Missing product field: ' + field)
        for url in [p['url'], *p['sources']]:
            if not re.match(r'^https://[^\s<>\[\]()]+$', url):
                raise ValueError('Invalid HTTPS source URL')
        dt.date.fromisoformat(p['checked_on'])
        if p['runtime_tested'] is not False:
            raise ValueError('Initial catalog must not claim runtime testing')
    for m in mappings:
        if not set(m['targets']) <= ids:
            raise ValueError('Unknown mapping target')
        for alias in m['aliases']:
            key = normalize(alias)
            if key in aliases:
                raise ValueError('Conflicting source aliases')
            aliases.add(key)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('validate', help='Check bundled data consistency')
    s = sub.add_parser('search', help='Search candidates, not verified replacements')
    s.add_argument('query')
    s.add_argument('--platform', choices=['macos', 'windows', 'linux', 'web', 'android', 'ios'])
    s.add_argument('--include-engines', action='store_true')
    s.add_argument('--json', action='store_true')
    s.add_argument('--lang', choices=['zh-TW', 'en'], default='zh-TW')
    r = sub.add_parser('report', help='Write private report; do not print inventory')
    r.add_argument('--input', required=True)
    r.add_argument('--output', required=True)
    r.add_argument('--platform', required=True, choices=['macos', 'windows', 'linux'])
    r.add_argument('--lang', choices=['zh-TW', 'en'], default='zh-TW')
    args = parser.parse_args(argv)
    try:
        catalog = read_json(ROOT / 'data/products.json')
        mappings = read_json(ROOT / 'data/alternatives.json')['mappings']
        validate(catalog, mappings)
        if args.command == 'validate':
            print(f"Valid: {len(catalog['products'])} products, {len(mappings)} source mappings")
        elif args.command == 'search':
            results = search(catalog['products'], mappings, args.query, args.platform, args.include_engines)
            print(json.dumps(results, ensure_ascii=False, indent=2) if args.json else render(results, args.lang))
            if not results and not args.json:
                print('沒有符合候選 / No matches. Search the linked articles; do not infer full replacement.')
        else:
            names, warnings = inventory(args.input)
            write_output(args.output, report(names, catalog['products'], mappings, args.platform, args.lang, warnings))
            print('Report saved locally. Inventory contents were not printed.')
    except (OSError, ValueError, KeyError, TypeError) as error:
        # Avoid leaking names, paths, raw JSON or registry values through exception text.
        print('Operation failed (' + type(error).__name__ + '). Check input schema, output existence and permissions.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
