# Usage

[繁體中文](USAGE.zh-TW.md) · [Home](../README.en.md)

## Choose the smallest entry

For a named replacement, ask the skill or browse the catalog; do not scan unnecessarily. Run collectors on the actual target computer. Cloud chat cannot scan your personal Mac/Windows through these commands.

Run commands from the repository root with Python 3.10+; Windows can use py -3. Without Python, browse Markdown or use a host that already has a runtime for manual data. Strict offline use must not upload an inventory.

## Manual inventory

Create a private folder outside the repository, for example ~/Documents/open-source-saver-private. Save apps.txt, one application per line. This example is synthetic:

```text
Adobe Premiere Pro 2024
Microsoft Word
Screen Studio
Unknown Example App
```

Or JSON (raw WinGet/system_profiler exports are not supported):

```json
{"applications": [{"name": "Microsoft Word", "version": "example"}, {"display_name": "Snagit"}]}
```

```bash
python3 scripts/saver.py report --input ~/Documents/open-source-saver-private/apps.txt --platform macos --output ~/Documents/open-source-saver-private/report.md --lang en
```

Open report.md locally. It lists candidates and unmatched items, not actual subscriptions or savings. Existing outputs are never overwritten; choose a new filename.

## Mac collection (experimental)

```bash
python3 scripts/collect_macos.py --output ~/Documents/open-source-saver-private/inventory.json
python3 scripts/saver.py report --input ~/Documents/open-source-saver-private/inventory.json --platform macos --output ~/Documents/open-source-saver-private/scan-report.md --lang en
```

Three known App folders, at most two subdirectory levels. Homebrew formulae, symlinked apps, other folders/users and browser extensions may be absent. Metadata failures create warnings. This is not full-device coverage.

## Windows collection (experimental)

Use Windows PowerShell without administrator elevation:

```powershell
$SaverPrivateDir = Join-Path $env:USERPROFILE 'Documents\open-source-saver-private'
powershell -NoProfile -File .\scripts\collect-windows.ps1 -OutputPath "$SaverPrivateDir\inventory.json"
py -3 .\scripts\saver.py report --input "$SaverPrivateDir\inventory.json" --platform windows --output "$SaverPrivateDir\report.md" --lang en
```

If organization policy blocks scripts, use manual input rather than changing machine-wide policy. Covers readable HKLM/HKCU uninstall records and current-user Appx, not every portable app. Technical Appx names may remain unmatched.

## Search

```bash
python3 scripts/saver.py search "screen recording" --platform macos --lang en
python3 scripts/saver.py search "dictation" --platform windows --lang en
python3 scripts/saver.py search "PDF" --platform windows --lang en
python3 scripts/saver.py search "transcription" --include-engines --json
python3 scripts/saver.py validate
```

Categories: screen-recording, screenshots-ocr, dictation, transcription, subtitles, text-to-speech, video-editing, audio-editing, graphics, office, pdf. Engines are hidden by default, but setup-heavy tools can still appear; read delivery and limitations.

No results? Reuse [sources](SOURCES.md) and data/discovery.json. A missing local match is not proof that no alternative exists.

## Privacy and failures

Helpers make no network requests and do not print inventory contents. Keep private outputs outside public repositories. Strict offline means running locally without asking a cloud agent to read the output. Live official-source research is separate.

FileExistsError: choose a new output name. Invalid data: check the documented JSON/text schema. Wrong platform: run on the target device or import manually. Missing Python: use the Markdown catalog first. Empty results/warnings: inspect coverage and supplement manually, rather than inferring no installed software.
