# Open Source Saver / 開源省錢管家

![Open Source Saver product artwork](assets/hero-open-source-saver.png)

**Replace the tools you pay for with suitable free/open-source options, test them on your real work, then decide whether to cancel.**

<!-- catalog-summary:start -->
**213 candidates · 54 categories · 200 open-source projects · 11 proprietary free-tier/built-in candidates · 2 source-available candidates**
<!-- catalog-summary:end -->

**Also included: 1,346 searchable upstream leads across 84 upstream tags and 48 international research sources.** Upstream leads are unreviewed, may overlap curated products, and are counted separately.

Current catalog: **78 → 204 products (2.62×), 18 → 54 categories (3×), 20 → 102 conditional mappings**. [Method and evidence](docs/RESEARCH.md)

**You do not need to replace everything at once.** Open Source Saver puts common paid tools, free/open-source candidates, Chinese-language status, platform limits and download links together so you can find the one worth testing first.

[Browse the catalog](docs/CATALOG.en.md) · [Original-product mappings](docs/ALTERNATIVES.en.md) · [International research](docs/RESEARCH-SOURCES.md) · [Upstream index](data/upstream/awesome-selfhosted/README.md) · [繁體中文](README.md) · [Savings methodology](docs/SAVINGS.md) · [Forum research](docs/FORUMS.md) · [Suggest a tool](https://github.com/hansai-art/open-source-saver/issues/new?template=software.md)

The Skill's primary workflow is **inventory installed apps → match free/open-source alternatives → explain recommendations, feature gaps and installation steps**. Use a compatible agent with access to your computer, such as a local Claude Code or Codex host, to start from the software you actually have. You can also browse the catalog or ask about a single app. Reuse working products first. For English-only tools, improve Traditional Chinese guidance or contribute translations upstream before proposing a new product.

Navigation: [Savings](#what-could-you-save) · [Recent work](#what-we-recently-did) · [Priority tasks](#start-with-your-everyday-tasks) · [Categories](#whats-in-the-catalog) · [Research](#where-the-recommendations-come-from) · [Contribute](#share-a-tool-including-your-own) · [Get started](#new-here) · [Installation](#install-the-skill)

## What we recently did

We recently reorganized the catalog around real tasks: stronger conditions for Office, notes, screenshots, recording, captions, downloads and creative tools; refreshed Traditional Chinese status, platforms, licenses, prices and official download evidence; and started using traceable community evaluations and reproducible issues to adjust recommendation priority.

The homepage keeps only the decision points. Full changes and evidence limits remain in the [update log](docs/STATUS.md), [research and evidence](docs/RESEARCH-SOURCES.md) and [full catalog](docs/CATALOG.en.md).

Share better open-source tools, Chinese translations, real compatibility notes and reproducible issues. We will adjust recommendation priority based on traceable community feedback.

The detailed ArtCraft and recording/download reviews remain available in the research files and update log; they are not repeated on the homepage.

## What could you save?

### Ten free alternatives: about US$1,006 in first-year costs

If you pay for recording, screenshots, Office, notes, image editing, PDF editing, passwords, antivirus, Mac maintenance and video compression software, these costs can become a large invisible fixed cost. Each category below keeps one representative paid tool, using **US public prices checked on 2026-10-13**. Nine priced examples total **US$956.13/year**. Apple Compressor adds a US$49.99 one-time purchase, bringing first-year costs to US$1,006.12. Adobe is counted once, represented by Photoshop; Slack, Dropbox, Figma and Otter are excluded because they are primarily network services rather than desktop-software examples.

This is not a market-share ranking or a promise that every reader can save this amount. It counts only when you actually pay the expense, the replacement completes your work, and you stop renewing or buying the original tool.

**Ten representative examples:**

1. **Screen recording**: [Screen Studio](https://screen.studio/) US$108/year → **[OpenScreen](https://github.com/getopenscreen/openscreen)**
2. **Screenshots and markup**: [Snagit](https://www.techsmith.com/store/snagit) US$39/year → **[macshot](https://github.com/sw33tLie/macshot)**
3. **Documents and spreadsheets**: [Microsoft 365 Personal](https://www.microsoft.com/en-us/microsoft-365/p/microsoft-365-personal/cfq7ttc0k5bf) US$99.99/year → **[ONLYOFFICE](https://www.onlyoffice.com/)**
4. **Personal notes**: [Notion Plus](https://www.notion.com/pricing) US$120 annualized → **[Obsidian](https://obsidian.md/)**
5. **Adobe family (image-editing representative)**: [Adobe Photoshop](https://www.adobe.com/products/photoshop/plans.html) US$263.88/year → **[GIMP](https://www.gimp.org/)**
6. **PDF editing**: [PDF Expert Pro](https://pdfexpert.com/pricing) US$79.99/year → **[PDFsam Basic](https://pdfsam.org/pdfsam-basic/)**
7. **Passwords**: [1Password Individual](https://1password.com/pricing/personal) US$47.88 annualized → **[Proton Pass](https://proton.me/pass)**
8. **Mac maintenance**: [CleanMyMac](https://macpaw.com/store/cleanmymac) US$9.95/month, US$119.40/year → **[Pearcleaner](https://github.com/Alienator88/Pearcleaner)**
9. **Video compression and conversion**: [Apple Compressor](https://apps.apple.com/us/app/compressor/id424390742?mt=12) US$49.99 one-time → **[CompressO](https://github.com/codeforreal1/compressO)** for ordinary offline batch compression/conversion, excluding Final Cut/Motion integration and professional HDR/delivery workflows.
10. **Antivirus**: [Avast Premium Security](https://www.avast.com/premium-security) US$77.99/year (renewal benchmark) → **[ClamAV](https://www.clamav.net/)**

**First-year total: US$1,006.12 = US$956.13 recurring annual benchmarks + US$49.99 one-time. Do not repeat the purchase in later years. Apple price reviewed 2026-10-15.**

CompressO was recommended by Hans; official docs reviewed 2026-10-15, not runtime-tested here. Stable 3.0.0 was released 2026-04-06. Traditional Chinese UI unverified. macOS is not notarized; official Homebrew cask removes quarantine. Upstream lists Debian 13/Ubuntu 24 compatibility issues. [Official downloads](https://github.com/codeforreal1/compressO/releases/tag/3.0.0).

You do not need to replace ten tools at once. Start with the subscription you use most and can cancel most easily, download the candidate, run one complete workflow with your own files, then decide. The catalog explains platforms, Chinese-language status, licensing, free limits and official entry points instead of giving you a bare list of names.

[See the full calculation, sources and limits](docs/SAVINGS.md) · [Browse all candidates](docs/CATALOG.en.md)

## Start with your everyday tasks

| Task / original tool | Candidates to explore | A useful trial |
|---|---|---|
| Word, Excel, PowerPoint | **ONLYOFFICE first**; Collabora Office and LibreOffice | Test Traditional Chinese coverage, DOCX/XLSX/PPTX layout, macros and fonts with real files; community evaluations can change the order |
| Notion (personal notes / knowledge management) | **Obsidian first for free use (not open source)**; Joplin when open-source licensing is required | Obsidian itself is free; Sync and Publish are paid add-ons. Local Markdown vaults are not equivalent to Notion databases, collaboration or automation, so test imports and sync |
| Record a course / Camtasia | OBS Studio + Kdenlive | Record microphone and system audio, edit a short lesson and export it |
| Polished product demos / Screen Studio | OpenScreen, Recordly; OBS for basic recording | Check automatic zoom, cursor effects, captions, watermarks and installation |
| Screenshots / Snagit, CleanShot X | **macshot first on Mac**; ShareX first on Windows; Capso, Flameshot or ksnip as alternatives | Test scrolling capture, 16:9/fixed-size selection, Chinese OCR, shortcuts and sharing |
| Voice typing / Wispr Flow, Superwhisper | Handy, OpenWhispr, TypeWhisper on Mac | Test mixed Chinese/English terminology and local versus cloud costs |
| Transcripts / Otter, Descript | noScribe, Vibe, Buzz; Meetily Community for meeting summaries | Check speakers, processing time and exports; transcription is not text-based video editing |
| Subtitles and audio | Subtitle Edit, Audacity; see the TTS section for speech synthesis | Check timing and model terms; engines may require setup |
| PDF page operations / parts of Acrobat | PDFsam Basic; PDF24 Creator on Windows | Test splitting/merging separately from text editing; SumatraPDF is primarily a reader |

These are starting candidates, not a runtime-tested ranking. [Each catalog row](docs/CATALOG.en.md) includes official links, platform, cost scope and limitations.

## What's in the catalog?

<!-- catalog-categories:start -->
| Category | Count | Examples |
|---|---:|---|
| [Screen recording](docs/CATALOG.en.md#screen-recording) | 14 | OBS Studio, Recordly, Capptivo |
| [Screenshots and OCR](docs/CATALOG.en.md#screenshots-ocr) | 10 | ShareX, Flameshot, ksnip |
| [Voice typing / dictation](docs/CATALOG.en.md#dictation) | 6 | Handy, OpenWhispr, VoiceInk |
| [Transcription and meetings](docs/CATALOG.en.md#transcription) | 10 | Vibe, Buzz, aTrain |
| [Subtitles and translation](docs/CATALOG.en.md#subtitles) | 4 | Subtitle Edit, pyVideoTrans, VideoLingo |
| [Text to speech](docs/CATALOG.en.md#text-to-speech) | 7 | Readest, Piper（現行維護線）, Qwen3-TTS |
| [Video editing, compositing and conversion](docs/CATALOG.en.md#video-editing) | 12 | Auto-Editor, LosslessCut, Kdenlive |
| [Audio editing](docs/CATALOG.en.md#audio-editing) | 2 | Audacity, Ultimate Vocal Remover（UVR） |
| [Graphics](docs/CATALOG.en.md#graphics) | 3 | GIMP, Krita, PhotoCraft |
| [Office documents](docs/CATALOG.en.md#office) | 3 | LibreOffice, ONLYOFFICE Desktop Editors, Collabora Office |
| [PDF reading and processing](docs/CATALOG.en.md#pdf) | 4 | PDF24 Creator, SumatraPDF, PDFsam Basic |
| [File transfer and synchronization](docs/CATALOG.en.md#file-transfer) | 3 | LocalSend, Syncthing, rclone |
| [Windows, clipboard and system utilities](docs/CATALOG.en.md#productivity) | 9 | Rectangle, Maccy, Pearcleaner |
| [Archives](docs/CATALOG.en.md#archives) | 2 | 7-Zip, PeaZip |
| [Media players](docs/CATALOG.en.md#media-players) | 3 | VLC media player, IINA, FreeTube |
| [Email](docs/CATALOG.en.md#email) | 1 | Thunderbird |
| [Password management](docs/CATALOG.en.md#passwords) | 2 | KeePassXC, Proton Pass |
| [Notes and ebooks](docs/CATALOG.en.md#notes-reading) | 3 | Joplin, Obsidian, calibre |
| [Vector design and UI prototyping](docs/CATALOG.en.md#vector-design) | 3 | Inkscape, Penpot, VectorCraft |
| [Desktop publishing and font creation](docs/CATALOG.en.md#desktop-publishing) | 3 | Scribus, FontForge, DesignCraft |
| [RAW development, photo management and panoramas](docs/CATALOG.en.md#photo-workflow) | 5 | darktable, RawTherapee, digiKam |
| [CAD drafting and parametric modeling](docs/CATALOG.en.md#cad-modeling) | 4 | FreeCAD, LibreCAD, OpenSCAD |
| [Electronics and electrical design](docs/CATALOG.en.md#electronics-design) | 2 | KiCad, QElectroTech |
| [2D animation and vector motion](docs/CATALOG.en.md#animation-2d) | 4 | OpenToonz, Synfig Studio, Pencil2D |
| [Game and interactive development](docs/CATALOG.en.md#game-development) | 4 | Godot Engine, GDevelop, LÖVE |
| [Music production, notation and DJ](docs/CATALOG.en.md#music-production) | 8 | Ardour, LMMS, MuseScore Studio |
| [Statistics and scientific computing](docs/CATALOG.en.md#scientific-computing) | 4 | GNU Octave, Scilab, JASP |
| [GIS and cartography](docs/CATALOG.en.md#gis-mapping) | 1 | QGIS |
| [Scientific imaging, chemistry and astronomy education](docs/CATALOG.en.md#science-education) | 3 | Stellarium, Avogadro 2, ImageJ |
| [Project management and Kanban](docs/CATALOG.en.md#project-management) | 5 | OpenProject Community, Taiga, Kanboard |
| [CRM and sales](docs/CATALOG.en.md#crm) | 3 | SuiteCRM, EspoCRM, Frappe CRM |
| [ERP and inventory](docs/CATALOG.en.md#erp) | 3 | ERPNext, Dolibarr, Odoo Community |
| [Web analytics](docs/CATALOG.en.md#web-analytics) | 3 | Matomo On-Premise Community, Umami, Plausible Community Edition |
| [Business intelligence and dashboards](docs/CATALOG.en.md#business-intelligence) | 2 | Metabase Open Source, Apache Superset |
| [Forms and surveys](docs/CATALOG.en.md#forms-surveys) | 2 | LimeSurvey Community, OpnForm Community |
| [Ecommerce and storefronts](docs/CATALOG.en.md#ecommerce) | 4 | WooCommerce, PrestaShop, Medusa Core |
| [Helpdesk and customer support](docs/CATALOG.en.md#helpdesk) | 4 | Zammad, osTicket, FreeScout |
| [Booking and scheduling](docs/CATALOG.en.md#booking-scheduling) | 1 | Easy!Appointments |
| [Team chat](docs/CATALOG.en.md#team-chat) | 1 | Zulip |
| [Team wikis and knowledge bases](docs/CATALOG.en.md#wiki-knowledge) | 3 | BookStack, Wiki.js, DokuWiki |
| [Workflow automation](docs/CATALOG.en.md#workflow-automation) | 2 | Activepieces Community, Node-RED |
| [Email marketing and automation](docs/CATALOG.en.md#email-marketing) | 2 | listmonk, Mautic |
| [Backup and recovery](docs/CATALOG.en.md#backup-recovery) | 4 | restic, BorgBackup（1.4 穩定系列）, Kopia |
| [Database clients](docs/CATALOG.en.md#database-clients) | 3 | DBeaver Community, DB Browser for SQLite, Beekeeper Studio Community |
| [Code editing and API development](docs/CATALOG.en.md#developer-tools) | 6 | VSCodium, Zed, Neovim |
| [Phone and device integration](docs/CATALOG.en.md#device-integration) | 3 | scrcpy, KDE Connect, App Manager |
| [File management and duplicate cleanup](docs/CATALOG.en.md#file-management) | 2 | Double Commander, Krokiet（Czkawka 專案） |
| [Local AI and model tools](docs/CATALOG.en.md#local-ai) | 3 | Jan, GPT4All, Ollama |
| [DNS and network monitoring](docs/CATALOG.en.md#network-monitoring) | 3 | AdGuard Home, Pi-hole, Uptime Kuma |
| [Personal finance and accounting](docs/CATALOG.en.md#personal-finance) | 3 | GnuCash, Actual Budget, Money Manager Ex |
| [Privacy and security](docs/CATALOG.en.md#privacy-security) | 3 | Cryptomator（桌面版）, ClamAV, Portmaster |
| [Remote access and device management](docs/CATALOG.en.md#remote-access) | 3 | RustDesk, Apache Guacamole, MeshCentral |
| [Feeds and reference management](docs/CATALOG.en.md#rss-reference) | 4 | FreshRSS, RSS Guard, Zotero |
| [Download managers, acceleration and video downloads](docs/CATALOG.en.md#download-managers) | 2 | Varia, Gopeed |
<!-- catalog-categories:end -->

Counts use unique product IDs and one primary category per entry. Platforms, article mentions and forum comments are not extra products. The open-source count includes engines, setup-heavy projects and products that may charge for official binaries; it is **not a count of free one-click downloads**. Pearcleaner has a Commons Clause restriction and paused maintenance, so it is counted as source-available, not open source. Proprietary free tiers retain their limits.

Traditional Chinese UI, Chinese content and Taiwan-accent speech quality are separate questions. No third-party workflow or Chinese-quality testing is claimed. [Generated statistics](data/catalog-stats.json) · [Verification status](docs/STATUS.md)

## Where the recommendations come from

1. **45 international sources:** [Attributed summaries and candidate links](docs/RESEARCH-SOURCES.md), covering English, French, German, Traditional Chinese, Hong Kong Chinese, Simplified Chinese and Japanese. We reviewed 22 bodies of content, 9 relevant directory sections and 6 directory indexes; 1 source remains discovery-only. This update adds 7 ArtCraft official version reviews. Scope is recorded per source.
2. **1,346 upstream discovery leads:** [Awesome Selfhosted snapshot](data/upstream/awesome-selfhosted/README.md), pinned to an immutable commit and searchable offline. All are unreviewed here, including 92 marked nonfree upstream. The derived index keeps CC BY-SA 3.0, AUTHORS and LICENSE; it is not a promise of free commercial use.
3. **Existing research retained:** [11 articles](docs/SOURCES.md) and [7 Reddit/Hacker News discussions](docs/FORUMS.md). Overlapping candidate mentions do not increase curated totals.
4. **111 previously reviewed products:** [Creative and engineering: 38](docs/research/creative.md), [business: 35](docs/research/business.md), [developer and personal tools: 38](docs/research/infra.md). Each has official documentation, bilingual scope and limitations, costs and license information. Existing products retain their earlier evidence dates; third-party workflows remain untested.

Our aim is broad, useful global coverage; no like-for-like benchmark establishes this as the world's most complete directory. Research records disagreements and outdated claims, including Zotero storage, Kanboard maintenance, Cal.diy scope and stable vs beta Borg versions. [Method, evidence levels and remaining gaps](docs/RESEARCH.md)

## Share a tool—including your own

**Your own project, a tool you use every day, or a discovery from another community is welcome.** We prioritize open source and also accept usable freeware, free tiers and built-in features. English-only tools are welcome; help us add Traditional Chinese guidance or prepare an upstream translation proposal.

Alongside better open-source or free tools, please share real-world evaluations, compatibility notes and reproducible problems. We will adjust recommendation priority based on traceable community feedback while retaining evidence dates and unverified limitations.

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

Dataset updated **2026-10-13**. Obsidian was added as the free first choice for Notion personal notes and knowledge management, and ClamAV was added as an antivirus-engine candidate, with proprietary, command-line and extra-configuration limits clearly marked. Each product retains its actual evidence date; existing rows were not all rechecked today. No automatic installation, removal or subscription changes, and no billing guesses from installed-app names.

[Specification](docs/SPEC.en.md) · [v0.2 plan](docs/OPTIMIZATION.en.md) · [Status](docs/STATUS.md). The growing v0.1.0-alpha catalog does not mean all future v0.2 gates are complete.

[MIT](LICENSE) covers original project content. Third-party software, models and articles retain their own terms: [notices](THIRD_PARTY_NOTICES.md). Created by Hans Lin / 林思翰.

Search terms: open source alternatives, free software, Camtasia Studio alternative, Screen Studio alternative, screenshots, voice typing, dictation, Traditional Chinese, Taiwan, Claude Code skill, Codex skill.
