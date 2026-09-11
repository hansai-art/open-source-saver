# Open Source Saver / 開源省錢管家

**See what is installed on your computer, then get suitable free and open-source alternatives with download and installation guidance.**

<!-- catalog-summary:start -->
**78 candidates · 18 categories · 69 open-source projects · 8 proprietary free-tier/built-in candidates · 1 source-available candidate**
<!-- catalog-summary:end -->

**Start with one recording subscription: a successful switch and cancellation could avoid US$108 or US$179.88 a year.** These are the two annual-plan examples below, selected according to your existing plan—not guaranteed savings for every reader.

[Browse the catalog](docs/CATALOG.en.md) · [繁體中文](README.md) · [Savings methodology](docs/SAVINGS.md) · [Forum research](docs/FORUMS.md) · [Suggest a tool](https://github.com/hansai-art/open-source-saver/issues/new?template=software.md)

The Skill's primary workflow is **inventory installed apps → match free/open-source alternatives → explain recommendations, feature gaps and installation steps**. Use a compatible agent with access to your computer, such as a local Claude Code or Codex host, to start from the software you actually have. You can also browse the catalog or ask about a single app. Reuse working products first. For English-only tools, improve Traditional Chinese guidance or contribute translations upstream before proposing a new product.

Navigation: [Savings](#what-could-one-subscription-save) · [Priority tasks](#start-with-your-everyday-tasks) · [Categories](#whats-in-the-catalog) · [Research](#where-the-recommendations-come-from) · [Contribute](#share-a-tool-including-your-own) · [Get started](#new-here) · [Installation](#install-the-skill)

## What could one subscription save?

Public individual-plan benchmarks checked **2026-09-11**, in USD. Taxes, regional checkout differences, promotions and FX fees are excluded.

| Paid product / plan | Official price | Free starting point | Annual license expense avoided after successful replacement and cancellation | Check before switching |
|---|---|---|---:|---|
| Camtasia Essentials annual (also searched as Camtasia Studio) | US$179.88/year | OBS Studio recording + Kdenlive editing | **US$179.88** | Trial captions, templates and course delivery; basic recording alone does not replace the whole suite |
| Screen Studio annual | US$9/month equivalent, US$108 billed annually | OBS Studio + Kdenlive for basic recording/editing | **US$108** | Automatic zoom, cursor styling and sharing are not equivalent |
| Screen Studio monthly, used for all 12 months | US$29/month | Same basic workflow, subject to a real trial | **US$348** | An alternative billing scenario; never add it to the annual-plan row |

Official prices: [TechSmith](https://www.techsmith.com/store/camtasia), [Screen Studio](https://screen.studio/). Free tools: [OBS Studio](https://obsproject.com/), [Kdenlive](https://kdenlive.org/).

Need Screen Studio-style automatic camera movement? Explore Recordly and Capptivo in the [recording section](docs/CATALOG.en.md#screen-recording), then verify free acquisition, features and export limits. A catalog entry is not proof that your workflow can migrate.

**Avoidable recurring expense − necessary new costs = potential cash savings.** Track migration time separately. An old perpetual license, an already-free edition or a suite you still need does not automatically produce annual savings. [Methodology and machine-readable prices](docs/SAVINGS.md)

## Start with your everyday tasks

| Task / original tool | Candidates to explore | A useful trial |
|---|---|---|
| Record a course / Camtasia | OBS Studio + Kdenlive | Record microphone and system audio, edit a short lesson and export it |
| Polished product demos / Screen Studio | Recordly, Capptivo; OBS for basic recording | Check automatic zoom, cursor effects, captions, watermarks and installation |
| Screenshots / Snagit, CleanShot X | ShareX on Windows; macshot on Mac; Flameshot or ksnip across platforms | Test scrolling capture, Chinese OCR, shortcuts and sharing |
| Voice typing / Wispr Flow, Superwhisper | Handy, OpenWhispr, TypeWhisper on Mac | Test mixed Chinese/English terminology and local versus cloud costs |
| Transcripts / Otter, Descript | noScribe, Vibe, Buzz; Meetily Community for meeting summaries | Check speakers, processing time and exports; transcription is not text-based video editing |
| Subtitles and audio | Subtitle Edit, Audacity; see the TTS section for speech synthesis | Check timing and model terms; engines may require setup |
| PDF page operations / parts of Acrobat | PDFsam Basic; PDF24 Creator on Windows | Test splitting/merging separately from text editing; SumatraPDF is primarily a reader |

These are starting candidates, not a runtime-tested ranking. [Each catalog row](docs/CATALOG.en.md) includes official links, platform, cost scope and limitations.

## What's in the catalog?

<!-- catalog-categories:start -->
| Category | Count | Examples |
|---|---:|---|
| [Screen recording](docs/CATALOG.en.md#screen-recording) | 12 | OBS Studio, Recordly, Capptivo |
| [Screenshots and OCR](docs/CATALOG.en.md#screenshots-ocr) | 8 | ShareX, Flameshot, ksnip |
| [Voice typing / dictation](docs/CATALOG.en.md#dictation) | 6 | Handy, OpenWhispr, VoiceInk |
| [Transcription and meetings](docs/CATALOG.en.md#transcription) | 10 | Vibe, Buzz, aTrain |
| [Subtitles and translation](docs/CATALOG.en.md#subtitles) | 3 | Subtitle Edit, pyVideoTrans, VideoLingo |
| [Text to speech](docs/CATALOG.en.md#text-to-speech) | 7 | Readest, Piper（現行維護線）, Qwen3-TTS |
| [Video editing, compositing and conversion](docs/CATALOG.en.md#video-editing) | 9 | Auto-Editor, LosslessCut, Kdenlive |
| [Audio editing](docs/CATALOG.en.md#audio-editing) | 2 | Audacity, Ultimate Vocal Remover（UVR） |
| [Graphics](docs/CATALOG.en.md#graphics) | 2 | GIMP, Krita |
| [Office documents](docs/CATALOG.en.md#office) | 2 | LibreOffice, ONLYOFFICE Desktop Editors |
| [PDF reading and processing](docs/CATALOG.en.md#pdf) | 3 | PDF24 Creator, SumatraPDF, PDFsam Basic |
| [File transfer and synchronization](docs/CATALOG.en.md#file-transfer) | 2 | LocalSend, Syncthing |
| [Windows, clipboard and system utilities](docs/CATALOG.en.md#productivity) | 3 | Rectangle, Maccy, Pearcleaner |
| [Archives](docs/CATALOG.en.md#archives) | 2 | 7-Zip, PeaZip |
| [Media players](docs/CATALOG.en.md#media-players) | 3 | VLC media player, IINA, FreeTube |
| [Email](docs/CATALOG.en.md#email) | 1 | Thunderbird |
| [Password management](docs/CATALOG.en.md#passwords) | 1 | KeePassXC |
| [Notes and ebooks](docs/CATALOG.en.md#notes-reading) | 2 | Joplin, calibre |
<!-- catalog-categories:end -->

Counts use unique product IDs and one primary category per entry. Platforms, article mentions and forum comments are not extra products. The open-source count includes engines, setup-heavy projects and products that may charge for official binaries; it is **not a count of free one-click downloads**. Pearcleaner has a Commons Clause restriction and paused maintenance, so it is counted as source-available, not open source. Proprietary free tiers retain their limits.

Traditional Chinese UI, Chinese content and Taiwan-accent speech quality are separate questions. No third-party workflow or Chinese-quality testing is claimed. [Generated statistics](data/catalog-stats.json) · [Verification status](docs/STATUS.md)

## Where the recommendations come from

1. [11 existing articles](docs/SOURCES.md) from It's FOSS, TechRadar and Lifewire. The 53 discovery names overlap the product catalog and must not be added to it.
2. [7 Reddit / Hacker News discussions and comments](docs/FORUMS.md), distinguishing developer promotion, user experiences and subsequent official verification.
3. [Upstream directories](docs/SOURCES.md) for continued discovery, without copying databases whose reuse terms are unresolved.
4. [Official documentation and per-product dates](data/products.json). Additional official research fills gaps such as archives, mail, passwords and file transfer; not every new entry came from a forum.

Forum leads also expose limits: Longshot comments mention watermarked free outputs; the relationship between an older Voquill launch and its current website remains unresolved. These stay in the research notes rather than inflating product counts.

## Share a tool—including your own

**Your own project, a tool you use every day, or a discovery from another community is welcome.** We prioritize open source and also accept usable freeware, free tiers and built-in features. English-only tools are welcome; help us add Traditional Chinese guidance or prepare an upstream translation proposal.

No coding needed: [suggest software](https://github.com/hansai-art/open-source-saver/issues/new?template=software.md) with its name, official link and the task it solves. Add platform, original paid tool, free limits and language evidence if known. State unknowns honestly. If you are the developer or have a commercial relationship, say so.

[Report corrections](https://github.com/hansai-art/open-source-saver/issues/new?template=correction.md) for broken links, changed prices, restrictions or reproducible problems. For data changes, see [Contributing](CONTRIBUTING.md).

## New here?

1. Install the Skill in an agent that can access your computer, then ask it to inventory installed apps. Mac/Windows collectors are experimental and may miss portable apps, extensions or unusual locations.
2. Review the installed-app-to-alternative table, including free/open-source terms, supported tasks, feature gaps and unmatched apps.
3. Follow the official download links and installation guidance. Ready-to-use free open-source tools are prioritized; proprietary free options are labeled separately.
4. Choose a tool and trial a real document or recording. If you want the agent to install it, name that tool. Recommendations alone do not install software, remove existing apps or cancel subscriptions.

**Cloud ChatGPT cannot directly scan your personal computer.** In a cloud host, the Skill guides local collection or accepts an app-name list. Linux and other devices use a manual list or an available read-only host method. [Inventory instructions](docs/USAGE.en.md)

A request about one specific app does not require a full inventory. Installed apps are not evidence of paid subscriptions; savings require actual billing information.

## Install the skill

Keep the complete folder including SKILL.md, scripts, references and data.

Claude Code personal installation on macOS/Linux with Git:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/hansai-art/open-source-saver.git ~/.claude/skills/open-source-saver
```

Then invoke:

```text
/open-source-saver Inventory the apps installed on this computer, recommend suitable free open-source alternatives, and include feature gaps, official downloads and installation steps. Answer in English.
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


## Privacy, licensing and progress

Bundled helpers make no network requests and save inventories/reports locally. Sending those files to cloud AI still involves cloud processing; use the local CLI for strict offline work. Collectors are experimental pending native Mac/Windows validation; manual app names work now.

Dataset updated **2026-09-11**. Each product retains its actual evidence date; existing rows were not all rechecked today. No automatic installation, removal or subscription changes, and no billing guesses from installed-app names.

[Specification](docs/SPEC.en.md) · [v0.2 plan](docs/OPTIMIZATION.en.md) · [Status](docs/STATUS.md). The growing v0.1.0-alpha catalog does not mean all future v0.2 gates are complete.

[MIT](LICENSE) covers original project content. Third-party software, models and articles retain their own terms: [notices](THIRD_PARTY_NOTICES.md). Created by Hans Lin / 林思翰.

Search terms: open source alternatives, free software, Camtasia Studio alternative, Screen Studio alternative, screenshots, voice typing, dictation, Traditional Chinese, Taiwan, Claude Code skill, Codex skill.
