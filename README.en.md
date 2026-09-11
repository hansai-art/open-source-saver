# Open Source Saver / 開源省錢管家

**Find existing open-source and free alternatives to paid software. Traditional Chinese first, English second.**

[繁體中文](README.md) · [Catalog](docs/CATALOG.en.md) · [Usage](docs/USAGE.en.md) · [Specification](docs/SPEC.en.md) · [Sources](docs/SOURCES.md)

An Agent Skill for recording, screenshots/OCR, dictation, transcription, subtitles, TTS, video/audio editing, graphics, Office and PDF research. Designed around standard SKILL.md packaging for hosts such as Claude Code and Codex; host-specific installation and permissions are not universally tested.

## What it does

- Named app: “Find a free Screen Studio alternative with automatic zoom and captions.”
- Work need: “I need free Mac dictation with Traditional Chinese support.”
- Inventory: “Use these installed-app names to find candidates worth trying.”
- Reuse built-in features and existing products, distinguish open source, freeware, free tiers, paid features and setup requirements.
- Supply official links, limitations and review dates without inventing subscription savings.

**v0.1.0-alpha: 58 candidate products, 14 conditional source groups, 11 articles.** The 53 article-discovery names overlap the catalog and are not an additional verified recommendation count. Local helpers require no paid API, account or cloud backend. Your agent/model costs and data processing are separate.

## Browse without installing

[Screen recording](docs/CATALOG.en.md#screen-recording) · [Screenshots/OCR](docs/CATALOG.en.md#screenshots-ocr) · [Dictation](docs/CATALOG.en.md#dictation) · [Transcription](docs/CATALOG.en.md#transcription) · [Subtitles](docs/CATALOG.en.md#subtitles) · [TTS](docs/CATALOG.en.md#text-to-speech) · [Video](docs/CATALOG.en.md#video-editing) · [Graphics](docs/CATALOG.en.md#graphics) · [Office](docs/CATALOG.en.md#office) · [PDF](docs/CATALOG.en.md#pdf)

Read each limitation before choosing. PDF24 Creator desktop is Windows-only; open-source VoiceInk does not imply free official binaries; Resolve Studio features are distinct from the free edition.

## Install the skill

Keep the complete folder including SKILL.md, scripts, references and data.

Claude Code personal installation on macOS/Linux with Git:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/hansai-art/open-source-saver.git ~/.claude/skills/open-source-saver
```

Then invoke:

```text
/open-source-saver Find free Mac alternatives to Screen Studio. I need automatic zoom and captions. Answer in English.
```

For Codex or another host, give its skill installer this repository or ask the agent to install the complete folder using its documented skill mechanism. Do not assume Claude's path applies everywhere. Installing in a cloud host does not grant access to your device. [Claude official instructions](https://code.claude.com/docs/en/skills)

Without Git, choose **Code → Download ZIP**, extract and install the complete folder through your host. Inspect an existing destination instead of overwriting it.

## Optional offline CLI

With Python 3.10+ already installed, from the project folder:

```bash
python3 scripts/saver.py search "screen recording" --platform macos --lang en
python3 scripts/saver.py search "Snagit" --platform windows --lang en
python3 scripts/saver.py search "transcription" --include-engines --lang en
```

On Windows replace python3 with `py -3`. CLI search uses names/keywords; the agent handles conversational requirements. [Inventory and reports](docs/USAGE.en.md)

## Privacy and alpha limits

Bundled helpers do not make network requests and write private inventories/reports locally without printing contents. For strict offline work, do not paste those files into cloud AI. Collectors remain experimental pending real Mac/Windows validation; manual import is available now. No third-party product workflow or Chinese-quality tests are claimed. Snapshot date: 2026-09-10; check current downloads and free-tier terms.

No automatic installs, uninstalls or subscription changes. Installed does not mean paid. No promise of complete Adobe or Office replacement.

[Contribute](CONTRIBUTING.md) with original app, actual task, candidate, official source, platform, free limits and localization evidence. Reuse existing articles, then verify finalists. [MIT](LICENSE) covers our original work; third-party terms remain separate: [notices](THIRD_PARTY_NOTICES.md). Created by Hans Lin / 林思翰.

[Implementation and verification status](docs/STATUS.md)

[v0.2 optimization specification](docs/OPTIMIZATION.en.md)
