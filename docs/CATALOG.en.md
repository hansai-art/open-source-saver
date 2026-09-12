# Open-source and free software catalog

[繁體中文](CATALOG.zh-TW.md) · [English](CATALOG.en.md)

**189 candidates · 53 categories · 180 open-source projects · 8 proprietary free-tier/built-in candidates · 1 source-available candidate**

Dataset updated: 2026-09-12; individual review dates remain in each row. Includes engines and setup-heavy projects, not all free one-click downloads. Workflows and Chinese quality untested.

[Alternatives](ALTERNATIVES.en.md) · [Research](RESEARCH.md) · [Sources](SOURCES.md) · [Forums](FORUMS.md) · [JSON](../data/products.json) · [Contribute](../CONTRIBUTING.md)

## screen-recording

**Screen recording**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [OBS Studio](https://github.com/obsproject/obs-studio) | Screen recording, livestreaming and scenes | macos, windows, linux · desktop | free and open-source · GPL-2.0-or-later | Not automatic cinematic cursor zoom; check OS requirements. | [official-docs-reviewed](https://github.com/obsproject/obs-studio/blob/master/README.rst) / 2026-09-11 |
| [Recordly](https://github.com/webadderallorg/Recordly) | Polished recordings with cursor effects and zoom | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · AGPL-3.0；另見 LICENSE.md | Check platform-specific cursor/audio support and AGPL distribution terms. | [official-docs-reviewed](https://github.com/webadderallorg/Recordly/blob/main/README.md) / 2026-09-10 |
| [Capptivo](https://github.com/SECHAK-AG/capptivo) | Tutorial recording, cursor zoom and captions | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT | Captioning needs whisper-cli and a model; unsigned Mac builds may need extra steps. | [official-docs-reviewed](https://github.com/SECHAK-AG/capptivo/blob/main/README.md) / 2026-09-10 |
| [Cap](https://github.com/CapSoftware/Cap) | Recording and video sharing | macos, windows · desktop | open-source; binary/model/service costs may differ · AGPL-3.0 為主；指定 crates 為 MIT | Local recording, hosted sharing and paid services have different costs. | [official-docs-reviewed](https://github.com/CapSoftware/Cap/blob/main/README.md) / 2026-09-10 |
| [Screenity](https://github.com/alyssaxuu/screenity) | Browser-based screen recording and annotation | macos, windows, linux · extension | open-source; binary/model/service costs may differ · GPL-3.0（MV3 版本） | Chrome extension; do not include paid Screenity Pro features. | [official-docs-reviewed](https://github.com/alyssaxuu/screenity/blob/master/README.md) / 2026-09-10 |
| [OpenScreenStudio](https://github.com/Glyph-Software/OpenScreenStudio) | Native Mac screen and webcam recording | macos · desktop | open-source; binary/model/service costs may differ · AGPL-3.0 | Capture path may require a newer macOS than the base app; early candidate. | [official-docs-reviewed](https://github.com/Glyph-Software/OpenScreenStudio/blob/main/README.md) / 2026-09-10 |
| [Kap](https://github.com/wulkano/Kap) | Short Mac recordings | macos · desktop | open-source; binary/model/service costs may differ · MIT | Recent macOS compatibility has not been tested; lower-priority candidate. | [official-docs-reviewed](https://github.com/wulkano/Kap/blob/main/README.md) / 2026-09-10 |
| [ScreenToGif](https://github.com/NickeManarin/ScreenToGif) | GIF capture and editing | windows · desktop | open-source; binary/model/service costs may differ · MS-PL | Windows only; check required .NET runtime. | [official-docs-reviewed](https://github.com/NickeManarin/ScreenToGif/blob/master/README.md) / 2026-09-10 |
| [ScreenPal](https://screenpal.com/plans) | Short screen recordings | macos, windows · desktop | limited free tier; proprietary · see-upstream | Official free plan has a 15-minute recording limit; verify other feature tiers. | [official-docs-partial](https://screenpal.com/plans) / 2026-09-10 |
| [FlashBack Express](https://www.flashbackrecorder.com/express) | Screen recording with local saving | windows · desktop | free/paid feature boundaries need review · see-upstream | Articles disagree about watermarks; confirm exact build and free editing/AI limits. | [official-docs-partial](https://www.flashbackrecorder.com/express) / 2026-09-10 |
| [macOS Screenshot / QuickTime](https://support.apple.com/en-us/102618) | Basic screen and microphone recording | macos · builtin | included with macOS; proprietary · see-upstream | System audio and advanced editing requirements need separate verification. | [official-docs-partial](https://support.apple.com/en-us/102618) / 2026-09-10 |
| [Screenify](https://www.imobie.com/screenify/) | Screen/webcam/audio recording and trimming | macos, windows · desktop | freeware; not open-source · see-upstream | Auto zoom belongs to the separate FocuSee product; Mac features differ. | [official-docs-partial](https://www.imobie.com/screenify/) / 2026-09-10 |

## screenshots-ocr

**Screenshots and OCR**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [ShareX](https://github.com/ShareX/ShareX) | Screenshots and capture workflows | windows · desktop | free and open-source · GPL-3.0 | Windows only; configure uploads intentionally. | [official-docs-reviewed](https://github.com/ShareX/ShareX/blob/develop/README.md) / 2026-09-11 |
| [Flameshot](https://github.com/flameshot-org/flameshot) | Screenshot annotation | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0 | OS permissions and global shortcuts need checking. | [official-docs-reviewed](https://github.com/flameshot-org/flameshot/blob/master/README.md) / 2026-09-10 |
| [ksnip](https://github.com/ksnip/ksnip) | Screenshots, annotation and pinned images | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0 | OCR and hotkey support differ by platform; maintenance status needs review. | [official-docs-reviewed](https://github.com/ksnip/ksnip/blob/master/README.md) / 2026-09-10 |
| [Greenshot](https://github.com/greenshot/greenshot) | Basic screenshot capture and annotation | windows · desktop | open-source; binary/model/service costs may differ · GPL-3.0 | This entry covers open-source Windows software, not the separate Mac product. | [official-docs-reviewed](https://github.com/greenshot/greenshot/blob/main/README.md) / 2026-09-10 |
| [NormCap](https://github.com/dynobo/normcap) | Screen-area OCR to text | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0-or-later | Chinese recognition depends on installed Tesseract language packs. | [official-docs-reviewed](https://github.com/dynobo/normcap/blob/main/README.md) / 2026-09-10 |
| [Text Grab](https://github.com/TheJoeFin/Text-Grab) | Screen OCR on Windows | windows · desktop | open-source; binary/model/service costs may differ · MIT | Not a complete screenshot-editing replacement. | [official-docs-reviewed](https://github.com/TheJoeFin/Text-Grab/blob/main/README.md) / 2026-09-10 |
| [Lightshot](https://app.prntscr.com/en/index.html) | Quick screenshot capture and annotation | macos, windows · desktop | freeware; not open-source · see-upstream | Online sharing uploads screenshots; no tested OCR or scrolling capture. | [official-docs-partial](https://app.prntscr.com/en/index.html) / 2026-09-10 |
| [macshot](https://github.com/sw33tLie/macshot) | Mac screenshots, annotations, OCR and scrolling capture | macos · desktop | free and open-source · GPL-3.0 | Compare individual CleanShot X sharing and editing tasks; Chinese quality untested. | [official-docs-reviewed](https://github.com/sw33tLie/macshot) / 2026-09-11 |

## dictation

**Voice typing / dictation**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Handy](https://github.com/cjpais/Handy) | Local hotkey voice typing | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT | Choose a model that supports Chinese; accuracy and microphones need testing. | [official-docs-reviewed](https://github.com/cjpais/Handy/blob/main/README.md) / 2026-09-10 |
| [OpenWhispr](https://github.com/OpenWhispr/openwhispr) | Hotkey dictation with local or cloud backends | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT | Cloud features may cost money; some Intel Mac features differ. | [official-docs-reviewed](https://github.com/OpenWhispr/openwhispr/blob/main/README.md) / 2026-09-10 |
| [VoiceInk](https://github.com/Beingpax/VoiceInk) | Native Mac dictation | macos · desktop | open-source; binary/model/service costs may differ · GPL-3.0 | Source is available under GPL; official distributed builds/updates may be paid. | [official-docs-reviewed](https://github.com/Beingpax/VoiceInk/blob/main/README.md) / 2026-09-10 |
| [Whispering／Epicenter](https://github.com/EpicenterHQ/epicenter) | Dictation through Whispering and Epicenter | macos, windows, linux, web · desktop | open-source; binary/model/service costs may differ · AGPL-3.0-or-later（目前 apps） | App, host and inference backend have distinct requirements; current licensing differs from old releases. | [official-docs-reviewed](https://github.com/EpicenterHQ/epicenter/blob/main/apps/whispering/README.md) / 2026-09-10 |
| [Apple Dictation](https://support.apple.com/guide/mac-help/use-dictation-mh40584/mac) | Voice typing into text fields | macos · builtin | included with macOS; proprietary · see-upstream | Check settings for on-device processing; language support varies; not a file-transcription tool. | [official-docs-partial](https://support.apple.com/guide/mac-help/use-dictation-mh40584/mac) / 2026-09-10 |
| [TypeWhisper](https://github.com/TypeWhisper/typewhisper-mac) | Local or cloud dictation across apps | macos · desktop | free and open-source · GPL-3.0 | Local models require downloads; cloud APIs may cost extra. Traditional Chinese UI unconfirmed. | [official-docs-reviewed](https://github.com/TypeWhisper/typewhisper-mac) / 2026-09-11 |

## transcription

**Transcription and meetings**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Vibe](https://github.com/thewh1teagle/vibe) | Local audio/video transcription | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT | Chinese accuracy, speaker labels and timing need testing. | [official-docs-reviewed](https://github.com/thewh1teagle/vibe/blob/main/README.md) / 2026-09-10 |
| [Buzz](https://github.com/chidiwilliams/buzz) | Local microphone and file transcription | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT | No promise of accurate speaker separation or proper-noun recognition. | [official-docs-reviewed](https://github.com/chidiwilliams/buzz/blob/main/README.md) / 2026-09-10 |
| [aTrain](https://github.com/aTrainTranscription/aTrain) | Interview transcription and diarization | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · AGPL-3.0 | Windows/Linux packages; Mac route requires Python and CPU setup. | [official-docs-reviewed](https://github.com/aTrainTranscription/aTrain/blob/develop/README.md) / 2026-09-10 |
| [WhisperX](https://github.com/m-bain/whisperX) | Word-aligned transcription and speaker diarization | windows, linux · engine | open-source; binary/model/service costs may differ · BSD-2-Clause（程式） | Python setup and separate model access/terms; overlapping speech is difficult. | [official-docs-reviewed](https://github.com/m-bain/whisperX/blob/main/README.md) / 2026-09-10 |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Local Whisper inference | macos, windows, linux · engine | open-source; binary/model/service costs may differ · MIT | An engine/CLI, not a finished transcription UI; model license is separate. | [official-docs-reviewed](https://github.com/ggml-org/whisper.cpp/blob/master/README.md) / 2026-09-10 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Efficient Whisper inference in Python | macos, windows, linux · engine | open-source; binary/model/service costs may differ · MIT | NVIDIA CUDA acceleration is distinct from Mac CPU execution. | [official-docs-reviewed](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md) / 2026-09-10 |
| [FunASR](https://github.com/modelscope/FunASR) | ASR, punctuation and voice activity pipelines | Unknown · setup | open-source; binary/model/service costs may differ · MIT（程式）；模型另核對 | Developer toolkit; licenses and requirements vary by model. | [official-docs-reviewed](https://github.com/modelscope/FunASR/blob/main/README.md) / 2026-09-10 |
| [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | Cross-platform ASR/TTS inference | macos, windows, linux, android, ios · engine | open-source; binary/model/service costs may differ · Apache-2.0（程式） | Developer engine; inspect each model's terms and platform support. | [official-docs-reviewed](https://github.com/k2-fsa/sherpa-onnx/blob/master/README.md) / 2026-09-10 |
| [noScribe](https://github.com/kaixxx/noScribe) | Local interview transcription and speaker segmentation | macos, windows, linux · desktop | free and open-source · GPL-3.0 | Requires models, storage and compute time; Taiwan-accent accuracy untested. | [official-docs-reviewed](https://github.com/kaixxx/noScribe) / 2026-09-11 |
| [Meetily Community](https://github.com/Zackriya-Solutions/meetily) | Community edition for local meeting transcription and summaries | macos, windows · desktop | free and open-source · MIT | Model setup is needed for summaries; Pro-only features are outside the free community edition. | [official-docs-reviewed](https://github.com/Zackriya-Solutions/meetily) / 2026-09-11 |

## subtitles

**Subtitles and translation**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit) | Subtitle editing and synchronization | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT | Download stable releases; optional online services have separate costs. | [official-docs-reviewed](https://github.com/SubtitleEdit/subtitleedit/blob/main/README.md) / 2026-09-10 |
| [pyVideoTrans](https://github.com/jianchang512/pyvideotrans) | Transcription, translation, dubbing and subtitles | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0 | Windows package; Mac/Linux setup and API costs vary. | [official-docs-reviewed](https://github.com/jianchang512/pyvideotrans/blob/main/README.md) / 2026-09-10 |
| [VideoLingo](https://github.com/Huanshere/VideoLingo) | Video translation and dubbing pipeline | Unknown · setup | open-source; binary/model/service costs may differ · Apache-2.0 | Needs model/API configuration; Traditional Chinese documentation is not UI validation. | [official-docs-reviewed](https://github.com/Huanshere/VideoLingo/blob/main/README.md) / 2026-09-10 |

## text-to-speech

**Text to speech**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Readest](https://github.com/readest/readest) | Reading ebooks aloud | macos, windows, linux, android, ios, web · desktop | open-source; binary/model/service costs may differ · AGPL-3.0 | Reader app, not a voice production studio; voice backends vary. | [official-docs-reviewed](https://github.com/readest/readest/blob/main/README.md) / 2026-09-10 |
| [Piper（現行維護線）](https://github.com/OHF-Voice/piper1-gpl) | Local text-to-speech | Unknown · engine | open-source; binary/model/service costs may differ · GPL-3.0（程式） | GPL engine; voice models have separate licenses. | [official-docs-reviewed](https://github.com/OHF-Voice/piper1-gpl/blob/main/README.md) / 2026-09-10 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | Multilingual voice generation | Unknown · setup | open-source; binary/model/service costs may differ · Apache-2.0（repo）；指定權重另核對 | Python/model setup; no turnkey Mac or Taiwan-accent guarantee. | [official-docs-reviewed](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md) / 2026-09-10 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | Voice cloning and multilingual dubbing | macos, windows, linux · setup | open-source; binary/model/service costs may differ · MIT（程式）；權重另核對 | GUI/model setup; code and model terms differ. | [official-docs-reviewed](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md) / 2026-09-10 |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) | Multilingual speech generation | Unknown · setup | open-source; binary/model/service costs may differ · Apache-2.0（程式）；權重另核對 | Model and GPU setup required; no tested Mac workflow. | [official-docs-reviewed](https://github.com/QwenAudio/CosyVoice/blob/main/README.md) / 2026-09-10 |
| [Kokoro](https://github.com/hexgrad/kokoro) | Compact multilingual speech generation | macos, windows, linux · engine | open-source; binary/model/service costs may differ · Apache-2.0；README 稱權重亦 Apache | Mandarin needs the corresponding language components; accent not tested. | [official-docs-reviewed](https://github.com/hexgrad/kokoro/blob/main/README.md) / 2026-09-10 |
| [eSpeak NG](https://github.com/espeak-ng/espeak-ng) | Lightweight synthetic speech | windows, linux · engine | open-source; binary/model/service costs may differ · GPL-3.0 | Mechanical voice quality; not the first choice for polished narration. | [official-docs-reviewed](https://github.com/espeak-ng/espeak-ng/blob/master/README.md) / 2026-09-10 |

## video-editing

**Video editing, compositing and conversion**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Auto-Editor](https://github.com/WyattBlue/auto-editor) | Automatic silence/activity-based cutting | macos, windows, linux · setup | open-source; binary/model/service costs may differ · Unlicense（repo） | CLI with an upstream skill; meaningful pauses and project exports need review. | [official-docs-reviewed](https://github.com/WyattBlue/auto-editor/blob/master/README.md) / 2026-09-10 |
| [LosslessCut](https://github.com/mifi/lossless-cut) | Fast trimming without re-encoding | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-2.0 | Keyframe constraints; stream copy cannot burn captions. | [official-docs-reviewed](https://github.com/mifi/lossless-cut/blob/master/README.md) / 2026-09-10 |
| [Kdenlive](https://github.com/KDE/kdenlive) | Nonlinear video editing | macos, windows, linux · desktop | free and open-source · GPL-3.0 | Project exchange and delivery formats require testing. | [official-docs-reviewed](https://github.com/KDE/kdenlive/blob/master/README.md) / 2026-09-11 |
| [Shotcut](https://github.com/mltframework/shotcut) | General video editing | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0 | Check current OS requirements; no Premiere project compatibility guarantee. | [official-docs-reviewed](https://github.com/mltframework/shotcut/blob/master/README.md) / 2026-09-10 |
| [HandBrake](https://github.com/HandBrake/HandBrake) | Video transcoding | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-2.0 | Not a nonlinear editor. | [official-docs-reviewed](https://github.com/HandBrake/HandBrake/blob/master/README.markdown) / 2026-09-10 |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Media processing and encoding | macos, windows, linux · engine | open-source; binary/model/service costs may differ · LGPL 為主／可選 GPL 元件 | CLI/library; binary build options affect licensing. | [official-docs-reviewed](https://github.com/FFmpeg/FFmpeg/blob/master/README.md) / 2026-09-10 |
| [Natron](https://github.com/NatronGitHub/Natron) | Node-based compositing | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-2.0 | Not a complete After Effects replacement; verify platform packages. | [official-docs-reviewed](https://github.com/NatronGitHub/Natron/blob/RB-2.6/README.md) / 2026-09-10 |
| [Blender](https://github.com/blender/blender) | 3D, animation, compositing and video editing | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0（整體） | Existing project formats, plugins and team workflows may not transfer. | [official-docs-reviewed](https://github.com/blender/blender/blob/main/README.md) / 2026-09-10 |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | Editing, grading and audio post-production | macos, windows, linux · desktop | free tier; proprietary · see-upstream | Studio AI and advanced effects are paid; test actual codecs and hardware. | [official-docs-partial](https://www.blackmagicdesign.com/products/davinciresolve) / 2026-09-10 |

## audio-editing

**Audio editing**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Audacity](https://github.com/audacity/audacity) | Audio editing and cleanup | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0（整體）；部分檔案另有授權 | Check stable release and plugin compatibility. | [official-docs-reviewed](https://github.com/audacity/audacity/blob/master/README.md) / 2026-09-10 |
| [Ultimate Vocal Remover（UVR）](https://github.com/Anjok07/ultimatevocalremovergui) | Separating vocals and music | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT（GUI）；模型另核對 | Models have separate terms; separation can introduce artifacts. | [official-docs-reviewed](https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md) / 2026-09-10 |

## graphics

**Graphics**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [GIMP](https://www.gimp.org/) | Photo retouching and raster editing | macos, windows, linux · desktop | free and open-source · see-upstream | Test PSD/project round trips, fonts, color and plugins. | [official-docs-partial](https://www.gimp.org/) / 2026-09-10 |
| [Krita](https://krita.org/en/) | Digital painting and illustration | macos, windows, linux · desktop | free and open-source · see-upstream | Not a complete Photoshop replacement; UI localization not tested. | [official-docs-partial](https://krita.org/en/) / 2026-09-10 |

## office

**Office documents**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [LibreOffice](https://www.libreoffice.org/) | Documents, spreadsheets, presentations and Draw | macos, windows, linux · desktop | free and open-source · see-upstream | Test actual files, macros, fonts and collaboration requirements. | [official-docs-partial](https://www.libreoffice.org/) / 2026-09-10 |
| [ONLYOFFICE Desktop Editors](https://www.onlyoffice.com/desktop) | Office documents, spreadsheets, presentations and PDFs | macos, windows, linux · desktop | free open-source desktop edition · see-upstream | Hosted services and optional AI providers may be paid; test document fidelity. | [official-docs-partial](https://www.onlyoffice.com/desktop) / 2026-09-10 |

## pdf

**PDF reading and processing**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [PDF24 Creator](https://tools.pdf24.org/en/creator) | Offline PDF merging, splitting, conversion and OCR | windows · desktop | freeware; personal and commercial use · see-upstream | Desktop version is Windows only; not a full Acrobat workflow guarantee. | [official-docs-partial](https://tools.pdf24.org/en/creator) / 2026-09-10 |
| [SumatraPDF](https://www.sumatrapdfreader.org/free-pdf-reader) | Lightweight PDF and ebook reading | windows · desktop | free and open-source · see-upstream | Windows only; reading is not a substitute for Acrobat Pro text editing. | [official-docs-reviewed](https://www.sumatrapdfreader.org/free-pdf-reader) / 2026-09-11 |
| [PDFsam Basic](https://pdfsam.org/pdfsam-basic/) | Merge, split, rotate and extract PDF pages | macos, windows, linux · desktop | free and open-source · AGPL-3.0 | Basic differs from paid Visual/Enhanced; do not infer full text-editing capabilities. | [official-docs-reviewed](https://pdfsam.org/pdfsam-basic/) / 2026-09-11 |

## file-transfer

**File transfer and synchronization**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [LocalSend](https://localsend.org/) | Transfer files between devices on a local network | macos, windows, linux, android, ios · desktop | free and open-source · see-upstream | Devices must reach each other; no bundled cloud storage or remote-sharing service. | [official-docs-reviewed](https://localsend.org/) / 2026-09-11 |
| [Syncthing](https://syncthing.net/) | Synchronize files between your devices | macos, windows, linux · desktop | free and open-source · see-upstream | Requires your own devices and storage; no bundled cloud quota. | [official-docs-reviewed](https://syncthing.net/) / 2026-09-11 |
| [rclone](https://github.com/rclone/rclone) | Copy, move and synchronize files between local and cloud storage | macos, windows, linux · cli | open-source; binary/model/service costs may differ · MIT | CLI tool; sync may propagate deletions and is not versioned backup. Provider quotas and storage/traffic fees apply. | [official-docs-reviewed](https://github.com/rclone/rclone) / 2026-09-12 |

## productivity

**Windows, clipboard and system utilities**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Rectangle](https://rectangleapp.com/) | Arrange windows with shortcuts and snapping | macos · desktop | free and open-source · see-upstream | This entry covers free Rectangle, not the separate paid Rectangle Pro; Mac only. | [official-docs-reviewed](https://rectangleapp.com/) / 2026-09-11 |
| [Maccy](https://github.com/p0deje/Maccy) | Search clipboard history with keyboard shortcuts | macos · desktop | free and open-source · MIT | Free downloads are in GitHub Releases; current versions need macOS 14+. Configure exclusions for sensitive copies. | [official-docs-reviewed](https://github.com/p0deje/Maccy) / 2026-09-11 |
| [Pearcleaner](https://github.com/alienator88/Pearcleaner) | Mac app removal and associated-file cleanup | macos · desktop | freeware; source-available, not open-source · Apache-2.0 with Commons Clause; source-available | Commons Clause restriction: not OSI open source. Upstream maintenance is on hold; not a first-choice recommendation. | [official-docs-reviewed](https://github.com/alienator88/Pearcleaner) / 2026-09-11 |
| [BleachBit](https://github.com/bleachbit/bleachbit) | Clean caches, temporary files and application traces | windows, linux · desktop | free and open-source · GPL-3.0-or-later | Preview selected files before deleting. Cleaning is not disk repair or guaranteed acceleration; use supported Windows/Linux builds. | [official-docs-reviewed](https://github.com/bleachbit/bleachbit) / 2026-09-12 |

## archives

**Archives**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [7-Zip](https://www.7-zip.org/) | Windows graphical archive creation and extraction | windows · desktop | free and open-source · LGPL/BSD components; unRAR restrictions | Extracts but does not create RAR archives; other-platform CLI editions need separate review. | [official-docs-reviewed](https://www.7-zip.org/) / 2026-09-11 |
| [PeaZip](https://peazip.github.io/) | Cross-platform graphical archive management | macos, windows, linux · desktop | free and open-source · see-upstream | Check creation versus extraction support for your formats and choose the correct platform package. | [official-docs-reviewed](https://peazip.github.io/) / 2026-09-11 |

## media-players

**Media players**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [VLC media player](https://github.com/videolan/vlc) | Local video and audio playback | macos, windows, linux · desktop | free and open-source · GPL-2.0-or-later; components vary | A player, not a full video editor or a paid-content subscription. | [official-docs-reviewed](https://github.com/videolan/vlc) / 2026-09-11 |
| [IINA](https://iina.io/) | A Mac-focused media player | macos · desktop | free and open-source · GPL-3.0 | Mac only; check OS requirements for your processor and release. | [official-docs-reviewed](https://iina.io/) / 2026-09-11 |
| [FreeTube](https://freetubeapp.io/) | Desktop YouTube viewing with local history | macos, windows, linux · desktop | free and open-source · AGPL-3.0 | Viewing still needs a network connection; not access to paid content or a complete Premium replacement. | [official-docs-reviewed](https://freetubeapp.io/) / 2026-09-11 |

## email

**Email**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Thunderbird](https://www.thunderbird.net/en-US/) | Desktop email management | macos, windows, linux · desktop | free and open-source · see-upstream | A free mail client does not include paid mail hosting, cloud storage or enterprise services. | [official-docs-reviewed](https://www.thunderbird.net/en-US/) / 2026-09-11 |

## passwords

**Password management**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [KeePassXC](https://keepassxc.org/) | Local encrypted password databases | macos, windows, linux · desktop | free and open-source · see-upstream | Plan synchronization and backups separately; check team sharing, recovery and administration needs. | [official-docs-reviewed](https://keepassxc.org/) / 2026-09-11 |

## notes-reading

**Notes and ebooks**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Joplin](https://joplinapp.org/) | Local notes and to-do organization | macos, windows, linux, android, ios · desktop | free and open-source · see-upstream | Joplin Cloud is separately paid; verify sync setup, import fidelity and team features. | [official-docs-reviewed](https://joplinapp.org/) / 2026-09-11 |
| [calibre](https://calibre-ebook.com/about) | Ebook library management, reading and conversion | macos, windows, linux · desktop | free and open-source · see-upstream | Conversion fidelity depends on the book and formats; not all layouts transfer unchanged. | [official-docs-reviewed](https://calibre-ebook.com/about) / 2026-09-11 |

## vector-design

**Vector design and UI prototyping**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Inkscape](https://inkscape.org/) | Vector illustration, icons, logos and SVG assets | macos, windows, linux · desktop | free and open-source · GPL-2.0-or-later | SVG-first workflow; validate Illustrator file round trips, plugins and print delivery with real projects. | [official-docs-reviewed](https://gitlab.com/inkscape/inkscape/-/raw/master/README.md) / 2026-09-12 |
| [Penpot](https://github.com/penpot/penpot) | Browser-based UI design, prototypes, design systems and collaborative self-hosting | web · self-hosted | open-source core; hosting and enterprise services may cost extra · MPL-2.0 | Hosting requires operations; enterprise governance and SSO can be paid. Validate Figma component and plugin migration. | [official-docs-reviewed](https://raw.githubusercontent.com/penpot/penpot/develop/README.md) / 2026-09-12 |

## desktop-publishing

**Desktop publishing and font creation**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Scribus](https://www.scribus.net/) | Page layout for brochures, magazines and print PDFs with CMYK, spot colors and ICC support | macos, windows, linux · desktop | free and open-source · GPL-2.0 / GPL-3.0; see component notices | Proof Chinese typography, text overflow and printer specifications; GitHub is a community mirror, not the authoritative development channel. | [official-docs-reviewed](https://sourceforge.net/projects/scribus/) / 2026-09-12 |
| [FontForge](https://github.com/fontforge/fontforge) | Create, edit and convert OpenType, TrueType, UFO and other fonts | macos, windows, linux · desktop | free and open-source · GPL-3.0-or-later as a whole; many parts BSD-3-Clause | Validate kerning, hinting and rendering; the editor license does not grant modification or redistribution rights to input fonts. | [official-docs-reviewed](https://github.com/fontforge/fontforge) / 2026-09-12 |

## photo-workflow

**RAW development, photo management and panoramas**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [darktable](https://github.com/darktable-org/darktable) | Non-destructive RAW processing, photo cataloging and export | macos, windows, linux · desktop | free and open-source · GPL-3.0 | A distinct workflow, not a Lightroom clone. Current README lists Apple Silicon Macs with macOS 14+; verify cameras and editing-history migration. | [official-docs-reviewed](https://github.com/darktable-org/darktable) / 2026-09-12 |
| [RawTherapee](https://github.com/RawTherapee/RawTherapee) | RAW development, demosaicing, color control and photo export | macos, windows, linux · desktop | free and open-source · GPL-3.0 | Not an all-in-one asset manager; printing, catalog management and uploading may require other tools. Check camera support. | [official-docs-reviewed](https://github.com/RawTherapee/RawTherapee) / 2026-09-12 |
| [digiKam](https://www.digikam.org/) | Import, tag, rate, search and manage large photo/video collections | macos, windows, linux · desktop | free and open-source · GPL-2.0-or-later | Back up the local library; optional remote-service plugins have separate privacy and service terms. Cloud storage is not included. | [official-docs-reviewed](https://www.digikam.org/about/) / 2026-09-12 |
| [Hugin](https://hugin.sourceforge.io/) | Stitch overlapping photographs into panoramas or image mosaics | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Inspect parallax, moving subjects and exposure mismatches; check platform-specific packages. Traditional Chinese is officially listed, not runtime tested. | [official-docs-reviewed](https://hugin.sourceforge.io/) / 2026-09-12 |

## cad-modeling

**CAD drafting and parametric modeling**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [FreeCAD](https://github.com/FreeCAD/FreeCAD) | Parametric part modeling, constrained sketches and technical drawings | macos, windows, linux · desktop | free and open-source · LGPL-2.1 | Evaluate workbenches separately; test large assemblies, CAM post-processors and proprietary CAD file exchange before migration. | [official-docs-reviewed](https://github.com/FreeCAD/FreeCAD) / 2026-09-12 |
| [LibreCAD](https://github.com/LibreCAD/LibreCAD) | 2D technical drafting, DXF editing and PDF/SVG conversion | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Primarily 2D; validate DWG versions, fonts, dimensions and layers. Current macOS builds are not notarized. | [official-docs-reviewed](https://github.com/LibreCAD/LibreCAD) / 2026-09-12 |
| [OpenSCAD](https://github.com/openscad/openscad) | Script-defined parametric parts, fixtures and 3D-printable solids | macos, windows, linux · desktop | free and open-source · GPL-2.0 with CGAL linking exception | Requires scripting; not an organic sculpting or character-animation tool. Validate boolean geometry and exported meshes. | [official-docs-reviewed](https://github.com/openscad/openscad) / 2026-09-12 |
| [SolveSpace](https://github.com/solvespace/solvespace) | Lightweight constrained 2D/3D parametric modeling | macos, windows, linux · desktop | free and open-source · GPL-3.0 | Prefer stable releases; edge builds may be unstable and 6DOF controller support differs by platform. | [official-docs-reviewed](https://github.com/solvespace/solvespace) / 2026-09-12 |

## electronics-design

**Electronics and electrical design**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [KiCad](https://www.kicad.org/) | Schematic capture, PCB layout and Gerber/IPC-2581 manufacturing output | macos, windows, linux · desktop | free and open-source · GPL-3.0 | Validate symbols, footprints, electrical rules and fabrication constraints; complete Altium project conversion is not established. | [official-docs-reviewed](https://www.kicad.org/about/kicad/) / 2026-09-12 |
| [QElectroTech](https://qelectrotech.org/) | Industrial electrical, wiring, hydraulic and pneumatic diagrams | macos, windows, linux · desktop | free and open-source · GNU GPL; see project license | Diagram authoring does not establish circuit simulation or complete EPLAN engineering-data management; validate symbols and delivery rules. | [official-docs-reviewed](https://qelectrotech.org/) / 2026-09-12 |

## animation-2d

**2D animation and vector motion**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [OpenToonz](https://github.com/opentoonz/opentoonz) | Traditional 2D animation production based on the Toonz workflow | macos, windows, linux · desktop | free and open-source · BSD-3-Clause core; bundled components have separate licenses | Assess training and project interchange. Only opentoonz.github.io and the repository are official sources; brushes and dependencies have separate licenses. | [official-docs-reviewed](https://github.com/opentoonz/opentoonz) / 2026-09-12 |
| [Synfig Studio](https://github.com/synfig/synfig) | Tweened 2D animation from vector and bitmap artwork | macos, windows, linux · desktop | free and open-source · GPL-3.0 | Test representative characters and shots; interpolation does not automate performance animation or ensure proprietary project compatibility. | [official-docs-reviewed](https://github.com/synfig/synfig) / 2026-09-12 |
| [Pencil2D](https://github.com/pencil2d/pencil) | Traditional hand-drawn 2D animation with bitmap and vector graphics | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Evaluate long-form productions, collaboration and commercial animation-file interchange separately; nightly builds are less stable. | [official-docs-reviewed](https://github.com/pencil2d/pencil) / 2026-09-12 |
| [Glaxnimate](https://glaxnimate.org/) | Vector tween animation and Lottie, animated SVG, GIF or WebP assets | macos, windows, linux · desktop | free and open-source · GPL-3.0-or-later | Lottie player compatibility varies; preview on the target app or site. This is not a complete After Effects compositor. | [official-docs-reviewed](https://glaxnimate.org/) / 2026-09-12 |

## game-development

**Game and interactive development**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Godot Engine](https://github.com/godotengine/godot) | 2D/3D games, interactive experiences and cross-platform development | macos, windows, linux · desktop | free and open-source · MIT | No engine royalties does not mean free console ports, store accounts or assets. Unity projects require migration and performance testing. | [official-docs-reviewed](https://raw.githubusercontent.com/godotengine/godot/master/README.md) / 2026-09-12 |
| [GDevelop](https://github.com/4ian/GDevelop) | Event-based 2D/3D games and interactive prototypes without conventional coding | macos, windows, linux · desktop | open-source editor/engine; online services and assets may cost extra · MIT core/editor/engine | The editor and engine are open source; online services, commercial support, assets and hosted features have separate costs or limits. | [official-docs-reviewed](https://github.com/4ian/GDevelop) / 2026-09-12 |
| [LÖVE](https://love2d.org/) | Lua-based 2D games, prototypes and game-programming education | macos, windows, linux · engine | free and open-source · Zlib | A code framework requiring game logic and tooling, not a visual no-code editor; mobile packaging needs additional work. | [official-docs-reviewed](https://love2d.org/) / 2026-09-12 |
| [libGDX](https://libgdx.com/) | Java framework for 2D/3D games across desktop, mobile and web | macos, windows, linux · engine | free and open-source · Apache-2.0 | Requires Java and build-system skills; not a complete visual editor. Platform SDKs and distribution requirements remain separate. | [official-docs-reviewed](https://libgdx.com/) / 2026-09-12 |

## music-production

**Music production, notation and DJ**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Ardour](https://ardour.org/) | Multitrack audio/MIDI recording, editing, mixing and soundtrack synchronization | macos, windows, linux · desktop | open-source; official prebuilt versions are paid; source builds are available · GPL-2.0 | Official prebuilt versions are paid; free source builds can be complex on macOS/Windows. Test audio hardware and plugin compatibility. | [official-docs-reviewed](https://ardour.org/) / 2026-09-12 |
| [LMMS](https://github.com/LMMS/lmms) | Piano-roll composition, beat patterns, synthesis and mixing | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Evaluate recording needs and platform-specific plugins separately; full FL Studio project migration is not established. | [official-docs-reviewed](https://github.com/LMMS/lmms) / 2026-09-12 |
| [MuseScore Studio](https://github.com/musescore/MuseScore) | Music notation, MIDI input, MusicXML interchange and PDF score printing | macos, windows, linux · desktop | free and open-source · GPL-3.0 | Distinguish the free desktop editor from MuseScore.com subscriptions, score access and extra sounds; proof imported score layout. | [official-docs-reviewed](https://github.com/musescore/MuseScore) / 2026-09-12 |
| [Hydrogen](https://github.com/hydrogen-music/hydrogen) | Pattern-based drum programming, MIDI/OSC control and live drum loops | macos, windows, linux · desktop | free and open-source · GPL-2.0-or-later | Focused on percussion; check drum-sample licenses and DAW synchronization. Not a complete recording workstation. | [official-docs-reviewed](https://github.com/hydrogen-music/hydrogen) / 2026-09-12 |
| [Mixxx](https://mixxx.org/) | DJ deck mixing, beat synchronization, controller mapping, recording and broadcasting | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Verify controller mappings; readable external libraries do not guarantee full cue/metadata migration. Music rights remain separate. | [official-docs-reviewed](https://mixxx.org/features/) / 2026-09-12 |
| [Qtractor](https://qtractor.org/) | Linux multitrack audio/MIDI sequencing, recording and mixing | linux · desktop | free and open-source · GPL-2.0-or-later | Targets Linux and depends on JACK/ALSA; do not present it as a native Windows or macOS replacement. | [official-docs-reviewed](https://qtractor.org/) / 2026-09-12 |
| [Sonic Visualiser](https://www.sonicvisualiser.org/) | Detailed visualization, analysis and annotation of music recordings | macos, windows, linux · desktop | free and open-source · GPL-2.0-or-later | Install Vamp analysis plugins separately; VST, AudioUnit and LV2 are unsupported. An analysis tool rather than a complete DAW. | [official-docs-reviewed](https://www.sonicvisualiser.org/) / 2026-09-12 |
| [Sonic Pi](https://sonic-pi.net/) | Live-coded music, synthesis and programming education | macos, windows, linux · desktop | free and open-source · MIT main code; GPL-3.0 obligations for bundled GUI binaries | Requires live-coding skills and is not a conventional timeline DAW; main code, GUI dependencies and learning materials have different licenses. | [official-docs-reviewed](https://github.com/sonic-pi-net/sonic-pi) / 2026-09-12 |

## scientific-computing

**Statistics and scientific computing**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [GNU Octave](https://octave.org/) | Numerical computing, matrix operations, plotting and many MATLAB-style scripts | macos, windows, linux · desktop | free and open-source · GNU GPL | MATLAB toolboxes, Simulink and proprietary functions are not automatically compatible; macOS installation follows the project wiki. | [official-docs-reviewed](https://octave.org/) / 2026-09-12 |
| [Scilab](https://www.scilab.org/) | Numerical analysis, signal processing, control systems and Xcos dynamic modeling | macos, windows, linux · desktop | free and open-source · GNU GPL | Revalidate scripts, modules and simulation behavior; existing MATLAB/Simulink files are not established as drop-in compatible. | [official-docs-reviewed](https://www.scilab.org/about) / 2026-09-12 |
| [JASP](https://github.com/jasp-stats/jasp-desktop) | GUI-based frequentist and Bayesian analyses with research-oriented tables | macos, windows, linux · desktop | free and open-source · AGPL-3.0 | Compare required analyses module by module; researchers must validate coding, missing-data handling and model assumptions. | [official-docs-reviewed](https://jasp-stats.org/) / 2026-09-12 |
| [jamovi](https://github.com/jamovi/jamovi) | Spreadsheet-style statistics, R syntax output and extensible analysis modules | macos, windows, linux · desktop | free and open-source · AGPL-3.0; engine/common components GPL-2.0-or-later | Reproduce SPSS syntax, required modules and results case by case; evaluate cloud-service terms separately from desktop use. | [official-docs-reviewed](https://www.jamovi.org/about.html) / 2026-09-12 |

## gis-mapping

**GIS and cartography**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [QGIS](https://qgis.org/) | Geospatial editing, analysis, cartography and reproducible processing workflows | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Validate coordinate systems, data licenses and plugins; proprietary geodatabases, enterprise permissions and cloud services need separate evaluation. | [official-docs-reviewed](https://qgis.org/project/overview/) / 2026-09-12 |

## science-education

**Scientific imaging, chemistry and astronomy education**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Stellarium](https://stellarium.org/) | Desktop planetarium, sky planning, time simulation and astronomy teaching | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Check telescope hardware and plugins; this entry covers the open-source desktop project, not paid features of similarly named mobile apps. | [official-docs-reviewed](https://stellarium.org/) / 2026-09-12 |
| [Avogadro 2](https://www.openchemistry.org/projects/avogadro2/) | Molecular editing, 3D chemical visualization and simulation preparation | macos, windows, linux · desktop | free and open-source · BSD-3-Clause | Not a replacement for every quantum-chemistry engine; verify external programs, formats and force-field results separately. | [official-docs-reviewed](https://www.openchemistry.org/projects/avogadro2/) / 2026-09-12 |
| [ImageJ](https://imagej.net/ij/) | Scientific image measurement, region statistics, stack processing and plugins | macos, windows, linux · desktop | free and open-source · Public domain core; plugins have separate licenses | Calibrate and validate measurements; plugin licenses differ from the public-domain core. Fiji is not counted again as a separate duplicate here. | [official-docs-reviewed](https://imagej.net/ij/docs/intro.html) / 2026-09-12 |

## project-management

**Project management and Kanban**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [OpenProject Community](https://github.com/opf/openproject) | Gantt planning, project tasks, time and budget tracking | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-3.0 | Enterprise add-ons and managed hosting are separate; operate the server, database and backups. | [official-docs-reviewed](https://github.com/opf/openproject/blob/dev/README.md) / 2026-09-12 |
| [Taiga](https://github.com/taigaio/taiga-back) | Scrum sprints, Kanban boards and issue tracking | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · MPL-2.0 | Requires frontend/backend deployment and dependencies; rebuild Jira workflows and integrations individually; hosting costs apply. | [official-docs-reviewed](https://github.com/taigaio/taiga-back/blob/main/README.md) / 2026-09-12 |
| [Kanboard](https://github.com/kanboard/kanboard) | Lightweight Kanban task and workflow management | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · MIT | Officially in maintenance mode with small fixes and community contributions; requires PHP hosting and is unsuitable if rapid feature growth is essential. | [official-docs-reviewed](https://github.com/kanboard/kanboard/blob/main/README.md) / 2026-09-12 |
| [WeKan](https://github.com/wekan/wekan) | Collaborative card-based team task boards | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · MIT | Operate MongoDB, updates and backups; README recommends at least 4 GB total RAM for a production server, so free licensing is not zero operating cost. | [official-docs-reviewed](https://github.com/wekan/wekan/blob/main/README.md) / 2026-09-12 |
| [Plane Community](https://github.com/makeplane/plane) | Issues, cycles, modules and product roadmaps | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 | Requires Docker/Kubernetes and dependent services; verify required features in Community before migration rather than assuming all cloud features are free. | [official-docs-reviewed](https://github.com/makeplane/plane/blob/preview/README.md) / 2026-09-12 |

## crm

**CRM and sales**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [SuiteCRM](https://github.com/SuiteCRM/SuiteCRM) | Customer relationships, sales data and CRM workflows | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 | Version 7 and 8 have different feature and migration paths; PHP/database operations, managed hosting and support require separate planning. | [official-docs-reviewed](https://github.com/SuiteCRM/SuiteCRM/blob/hotfix/README.md) / 2026-09-12 |
| [EspoCRM](https://github.com/espocrm/espocrm) | Leads, opportunities, contacts and customer support cases | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 | Core is open source; reporting and BPM extensions are separate packages with their own terms; hosting and maintenance are additional. | [official-docs-reviewed](https://github.com/espocrm/espocrm/blob/master/README.md) / 2026-09-12 |
| [Frappe CRM](https://github.com/frappe/crm) | Sales pipelines, activity history and custom lead/deal views | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 | Requires Frappe and database operations; managed cloud is separate and the app is not a complete marketing automation suite or ERP. | [official-docs-reviewed](https://github.com/frappe/crm/blob/develop/README.md) / 2026-09-12 |

## erp

**ERP and inventory**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [ERPNext](https://github.com/frappe/erpnext) | Integrated purchasing, inventory, manufacturing, accounting and projects | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-3.0 | Implementation, data cleanup and hosting are required; Taiwan tax, e-invoice and payroll suitability has not been validated. | [official-docs-reviewed](https://github.com/frappe/erpnext/blob/develop/README.md) / 2026-09-12 |
| [Dolibarr](https://github.com/Dolibarr/dolibarr) | Quotes, orders, invoices and inventory for smaller organizations | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-3.0-or-later | Hosting and some modules may cost extra; requires PHP/database operations, and Taiwan e-invoice/accounting workflows are unvalidated. | [official-docs-reviewed](https://github.com/Dolibarr/dolibarr/blob/develop/README.md) / 2026-09-12 |
| [Odoo Community](https://github.com/odoo/odoo) | Community modules for CRM, inventory and business operations | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · LGPL-3.0 (Community); Enterprise/apps have separate licenses | Only Community is counted; Enterprise and some Apps use separate potentially paid licenses; check each module and budget hosting, implementation and localization. | [official-docs-reviewed](https://github.com/odoo/odoo/blob/19.0/README.md) / 2026-09-12 |

## web-analytics

**Web analytics**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Matomo On-Premise Community](https://github.com/matomo-org/matomo) | Website traffic, events, campaign and ecommerce tracking | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-3.0-or-later | Requires PHP/MySQL hosting; heatmaps, session recordings and funnels are Premium features rather than all being included in the free core. | [official-docs-reviewed](https://github.com/matomo-org/matomo/blob/6.x-dev/README.md) / 2026-09-12 |
| [Umami](https://github.com/umami-software/umami) | Traffic, campaigns and conversions in a compact analytics dashboard | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · MIT | Requires Node.js/PostgreSQL and a tracking script; verify reporting models and imports rather than assuming lossless migration of GA history. | [official-docs-reviewed](https://github.com/umami-software/umami/blob/master/README.md) / 2026-09-12 |
| [Plausible Community Edition](https://github.com/plausible/analytics) | Self-hosted lightweight traffic and goal-conversion analytics | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0-or-later; tracker MIT | CE omits cloud marketing funnels, revenue goals, SSO and Sites API; operates PostgreSQL/ClickHouse and receives features more slowly. | [official-docs-reviewed](https://github.com/plausible/analytics/blob/master/README.md) / 2026-09-12 |

## business-intelligence

**Business intelligence and dashboards**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Metabase Open Source](https://github.com/metabase/metabase) | Visual questions, SQL queries and shared data dashboards | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL (OSS edition); enterprise directory commercial | Count the OSS edition only; enterprise code/images use commercial terms, and database connections, permissions and operations need configuration. | [official-docs-reviewed](https://github.com/metabase/metabase/blob/master/README.md) / 2026-09-12 |
| [Apache Superset](https://github.com/apache/superset) | Database exploration, SQL analysis and interactive dashboards | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · Apache-2.0 | Configure data connections and operate servers; no bundled enterprise data warehouse or validated Power BI/Tableau report import. | [official-docs-reviewed](https://github.com/apache/superset/blob/master/README.md) / 2026-09-12 |

## forms-surveys

**Forms and surveys**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [LimeSurvey Community](https://github.com/LimeSurvey/LimeSurvey) | Branching multilingual questionnaires and research surveys | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-2.0-or-later | Requires PHP/database hosting and email delivery; test branching logic carefully; cloud plans and operations cost separately. | [official-docs-reviewed](https://github.com/LimeSurvey/LimeSurvey/blob/master/README.md) / 2026-09-12 |
| [OpnForm Community](https://github.com/OpnForm/OpnForm) | Form building, conditional logic, embedding and submission notifications | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 (core); enterprise directory proprietary | api/app/Enterprise uses proprietary terms; verify free-core coverage and operate Laravel/Nuxt, database and email delivery. | [official-docs-reviewed](https://github.com/OpnForm/OpnForm/blob/main/README.md) / 2026-09-12 |

## ecommerce

**Ecommerce and storefronts**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [WooCommerce](https://github.com/woocommerce/woocommerce) | Physical and digital product stores on WordPress | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-3.0 | Requires WordPress hosting; subscriptions, bookings and memberships may use paid extensions; payment fees and local shipping/e-invoice integrations remain. | [official-docs-reviewed](https://github.com/woocommerce/woocommerce/blob/trunk/README.md) / 2026-09-12 |
| [PrestaShop](https://github.com/PrestaShop/PrestaShop) | Self-hosted stores, product catalogs and shopping carts | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · OSL-3.0 core; AFL-3.0 modules | Requires PHP/MySQL hosting; price themes, modules and payment/shipping services separately; deploy stable releases rather than develop. | [official-docs-reviewed](https://github.com/PrestaShop/PrestaShop/blob/develop/README.md) / 2026-09-12 |
| [Medusa Core](https://github.com/medusajs/medusa) | Composable commerce modules for custom storefronts and B2B workflows | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · MIT core; designated Enterprise materials commercial | Needs storefront engineering and payment/shipping integrations; MIT core excludes designated commercial RBAC Enterprise materials and cloud costs. | [official-docs-reviewed](https://github.com/medusajs/medusa/blob/develop/README.md) / 2026-09-12 |
| [Saleor](https://github.com/saleor/saleor) | GraphQL commerce backend with channel-specific products, prices and inventory | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · BSD-3-Clause | API-first; deploy/build a storefront and dashboard and integrate payments; cloud hosting and operations cost separately. | [official-docs-reviewed](https://github.com/saleor/saleor/blob/main/README.md) / 2026-09-12 |

## helpdesk

**Helpdesk and customer support**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Zammad](https://github.com/zammad/zammad) | Customer support tickets across email, chat and other channels | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 | Requires server, email and integration operations; cloud/support are separate and existing ticket imports should be validated. | [official-docs-reviewed](https://github.com/zammad/zammad/blob/develop/README.md) / 2026-09-12 |
| [osTicket](https://github.com/osTicket/osTicket) | Assignable support tickets from email, phone and web requests | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-2.0 | Requires PHP/MySQL and email configuration; ticketing does not imply full live chat, AI or omnichannel marketing functionality. | [official-docs-reviewed](https://github.com/osTicket/osTicket/blob/develop/README.md) / 2026-09-12 |
| [FreeScout](https://github.com/freescout-help-desk/freescout) | Shared support inboxes, assignment, internal notes and conversation tracking | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 | Price core and add-on modules separately; many integrations/advanced features are modules, and hosting, email and maintenance remain costs. | [official-docs-reviewed](https://github.com/freescout-help-desk/freescout/blob/dist/README.md) / 2026-09-12 |
| [Chatwoot Community](https://github.com/chatwoot/chatwoot) | Website live chat and multichannel customer support inboxes | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · MIT core; enterprise directory separate commercial terms | enterprise directory is outside the MIT core; verify AI/channel edition coverage and external-service charges; self-hosting requires operations. | [official-docs-reviewed](https://github.com/chatwoot/chatwoot/blob/develop/README.md) / 2026-09-12 |

## booking-scheduling

**Booking and scheduling**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Easy!Appointments](https://github.com/alextselegidis/easyappointments) | Provider availability, customer appointments and Google Calendar sync | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-3.0 code; CC-BY-3.0 content | Requires PHP/MySQL, email and calendar configuration; Premium features/services cost separately; test time zones and booking rules. | [official-docs-reviewed](https://github.com/alextselegidis/easyappointments/blob/main/README.md) / 2026-09-12 |

## team-chat

**Team chat**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Zulip](https://github.com/zulip/zulip) | Topic-threaded live and asynchronous team conversations | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · Apache-2.0 | Self-hosting needs Linux server operations; workflow differs from Slack, and imports, integrations and notification-service plans need checking. | [official-docs-reviewed](https://github.com/zulip/zulip/blob/main/README.md) / 2026-09-12 |

## wiki-knowledge

**Team wikis and knowledge bases**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [BookStack](https://www.bookstackapp.com/) | Company handbooks and knowledge organized as books, chapters and pages | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · MIT | Needs PHP/database hosting; its document hierarchy is not a Notion database replacement; official development source now points to Codeberg. | [official-docs-reviewed](https://github.com/BookStackApp/BookStack/blob/development/readme.md) / 2026-09-12 |
| [Wiki.js](https://github.com/requarks/wiki) | Team wikis, operating documentation and knowledge pages | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 | Requires Node.js, a supported database and permissions configuration; verify versions and migration of Confluence macros before adoption. | [official-docs-reviewed](https://github.com/requarks/wiki/blob/main/README.md) / 2026-09-12 |
| [DokuWiki](https://github.com/dokuwiki/dokuwiki) | Lightweight documentation wiki without a database | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-2.0 | Still needs PHP web hosting, backups and access controls; validate plugins and conversion of existing documentation. | [official-docs-reviewed](https://github.com/dokuwiki/dokuwiki/blob/master/README) / 2026-09-12 |

## workflow-automation

**Workflow automation**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Activepieces Community](https://github.com/activepieces/activepieces) | Visual automations across SaaS, webhooks and AI services | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · MIT Community; enterprise features commercial | packages/ee and packages/server/api/src/app/ee use commercial terms; self-hosting does not remove API/model charges; rebuild flows and check connectors. | [official-docs-reviewed](https://github.com/activepieces/activepieces/blob/main/README.md) / 2026-09-12 |
| [Node-RED](https://github.com/node-red/node-red) | Flow-based connections between APIs, events and devices | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · Apache-2.0 | Requires a Node.js runtime; third-party nodes vary in maintenance; servers/API usage cost separately and flows need authoring. | [official-docs-reviewed](https://github.com/node-red/node-red/blob/main/README.md) / 2026-09-12 |

## email-marketing

**Email marketing and automation**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [listmonk](https://github.com/knadh/listmonk) | Self-hosted newsletters, mailing lists and campaign delivery | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · AGPL-3.0 | Needs PostgreSQL and a mail delivery service; SMTP usage, bounces and sender reputation remain operational costs. | [official-docs-reviewed](https://github.com/knadh/listmonk/blob/master/README.md) / 2026-09-12 |
| [Mautic](https://github.com/mautic/mautic) | Contact segmentation, multichannel campaigns and marketing automation | web · self-hosted | open-source; self-hosting, maintenance and optional services cost extra · GPL-3.0-or-later | Needs hosting, scheduled jobs, database and email services; use stable production packages, not development branches, and validate contact/workflow migration. | [official-docs-reviewed](https://github.com/mautic/mautic/blob/7.x/README.md) / 2026-09-12 |

## backup-recovery

**Backup and recovery**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [restic](https://github.com/restic/restic) | Encrypted incremental backups to local, SFTP or object storage | macos, windows, linux · cli | open-source; binary/model/service costs may differ · BSD-2-Clause | CLI setup and restore drills required; storage and transfer fees are separate. | [official-docs-reviewed](https://github.com/restic/restic) / 2026-09-12 |
| [BorgBackup（1.4 穩定系列）](https://github.com/borgbackup/borg) | Deduplicated, compressed and encrypted file-history backups | macos, linux · cli | open-source; binary/model/service costs may differ · BSD-3-Clause | Choose stable Borg 1.4 for production; Borg 2 is testing. Supply remote storage and maintain restores. | [official-docs-reviewed](https://github.com/borgbackup/borg) / 2026-09-12 |
| [Kopia](https://github.com/kopia/kopia) | GUI or CLI encrypted file snapshots with deduplication | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · Apache-2.0 | File/folder backup rather than whole-disk imaging; storage costs extra and some rclone backends are experimental. | [official-docs-reviewed](https://github.com/kopia/kopia) / 2026-09-12 |
| [Duplicati（開源備份用戶端）](https://github.com/duplicati/duplicati) | Scheduled encrypted backups to cloud or remote file storage | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT（排除 proprietary/ 與另有授權元件） | Storage is not included; validate restores. MIT excludes the proprietary directory and separately licensed components. | [official-docs-reviewed](https://github.com/duplicati/duplicati) / 2026-09-12 |

## database-clients

**Database clients**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [DBeaver Community](https://github.com/dbeaver/dbeaver) | Multi-database SQL editing, browsing, import and export | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · Apache-2.0 | Community scope only; some non-JDBC sources and advanced features require commercial editions. Database/cloud/AI charges remain separate. | [official-docs-reviewed](https://github.com/dbeaver/dbeaver) / 2026-09-12 |
| [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) | Create, query and edit SQLite files with a spreadsheet-like interface | macos, windows, linux · desktop | free and open-source · MPL-2.0 或 GPL-3.0-or-later；附帶元件另列 | Targets SQLite, not general remote database administration or spreadsheet formulas. | [official-docs-reviewed](https://github.com/sqlitebrowser/sqlitebrowser) / 2026-09-12 |
| [Beekeeper Studio Community](https://github.com/beekeeper-studio/beekeeper-studio) | SQL editing and management for PostgreSQL, MySQL, SQLite and others | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0-or-later（Community；不含 src-commercial） | GPL Community edition only. src-commercial has a commercial source-available license; check paid support for Oracle, DuckDB and others. | [official-docs-reviewed](https://github.com/beekeeper-studio/beekeeper-studio) / 2026-09-12 |

## developer-tools

**Code editing and API development**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [VSCodium](https://github.com/VSCodium/vscodium) | Community VS Code binaries with Microsoft branding and default telemetry removed | macos, windows, linux · desktop | free and open-source · MIT | Uses Open VSX. Some Microsoft extensions are restricted to official VS Code; check debugger and extension compatibility. | [official-docs-reviewed](https://github.com/VSCodium/vscodium) / 2026-09-12 |
| [Zed](https://github.com/zed-industries/zed) | Code editing, collaboration and external AI/model integration | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0-or-later（標示元件為 Apache-2.0） | The editor is free; hosted AI, Pro and team administration have separate costs. Bring-your-own API keys still incur provider charges. | [official-docs-reviewed](https://github.com/zed-industries/zed) / 2026-09-12 |
| [Neovim](https://github.com/neovim/neovim) | Extensible modal code editor with scripting and plugin support | macos, windows, linux · cli | free and open-source · Apache-2.0 與 Vim license | Requires modal-editing skills; language servers, debuggers and AI integrations need separate configuration. | [official-docs-reviewed](https://github.com/neovim/neovim) / 2026-09-12 |
| [Geany](https://github.com/geany/geany) | Lightweight IDE with syntax highlighting, completion and build commands | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Provide language toolchains/plugins separately; validate advanced refactoring and framework support on a real project. | [official-docs-reviewed](https://github.com/geany/geany) / 2026-09-12 |
| [Bruno（開源版）](https://github.com/usebruno/bruno) | Local-file API requests and testing with Git collaboration | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT | No built-in cloud sync; commercial editions add features that must not be assumed in the open-source edition. | [official-docs-reviewed](https://github.com/usebruno/bruno) / 2026-09-12 |
| [Hoppscotch Community](https://github.com/hoppscotch/hoppscotch) | Web or desktop API testing for REST, GraphQL and WebSocket | macos, windows, linux, web · web | open-source; binary/model/service costs may differ · MIT | Browser cross-origin requests may need an interceptor or proxy. Distinguish self-hosted, hosted and Enterprise features/costs. | [official-docs-reviewed](https://github.com/hoppscotch/hoppscotch) / 2026-09-12 |

## device-integration

**Phone and device integration**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [scrcpy](https://github.com/Genymobile/scrcpy) | Mirror and control Android video/audio from a computer | macos, windows, linux · desktop | free and open-source · Apache-2.0 | Requires Android 5+ and usually USB debugging; audio forwarding needs Android 11+. Does not mirror iPhones. | [official-docs-reviewed](https://github.com/Genymobile/scrcpy) / 2026-09-12 |
| [KDE Connect](https://github.com/KDE/kdeconnect-kde) | Pair phones and computers for files, clipboard, notifications and remote input | macos, windows, linux, android, ios · desktop | free and open-source · GPL-2.0 與 GPL-3.0（依元件） | Pair devices first. Notifications, background behavior and controls vary by OS; iOS is not feature-identical to Android. | [official-docs-reviewed](https://github.com/KDE/kdeconnect-kde) / 2026-09-12 |
| [App Manager](https://github.com/MuntashirAkon/AppManager) | Inspect Android app permissions, trackers, APKs and usage information | android · mobile | free and open-source · GPL-3.0-or-later | Full app-data backups and component blocking require root; other controls need root/ADB. Unrooted use has narrower capabilities. | [official-docs-reviewed](https://github.com/MuntashirAkon/AppManager) / 2026-09-12 |

## file-management

**File management and duplicate cleanup**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Double Commander](https://github.com/doublecmd/doublecmd) | Dual-pane file management for directory and file operations | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Do not assume complete Total Commander plugin, shortcut or platform compatibility. | [official-docs-reviewed](https://github.com/doublecmd/doublecmd) / 2026-09-12 |
| [Krokiet（Czkawka 專案）](https://github.com/qarmin/czkawka) | Find duplicate files, similar images, empty directories and large files | macos, windows, linux · desktop | free and open-source · GPL-3.0-only（Krokiet；其他元件另見各目錄） | Krokiet succeeds the retired GTK frontend. Similar videos need FFmpeg; optional image formats vary. Review matches before deleting. | [official-docs-reviewed](https://github.com/qarmin/czkawka) / 2026-09-12 |

## local-ai

**Local AI and model tools**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Jan](https://github.com/janhq/jan) | Chat with downloaded local models or connect cloud APIs and assistants | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · Apache-2.0 | Offline behavior applies to local models only. Model licenses, RAM/GPU requirements and cloud API costs are separate. | [official-docs-reviewed](https://github.com/janhq/jan) / 2026-09-12 |
| [GPT4All](https://github.com/nomic-ai/gpt4all) | Run local LLM chats and query documents through LocalDocs | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT（模型授權另外核對） | Download and license models separately. Official Linux builds are x86-64; CPU support does not guarantee acceptable large-model speed. | [official-docs-reviewed](https://github.com/nomic-ai/gpt4all) / 2026-09-12 |
| [Ollama](https://github.com/ollama/ollama) | Run and manage models through CLI/API integrations | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · MIT（模型授權另外核對） | Local and cloud modes differ; disable cloud features for local-only use. Check model licenses, hardware and cloud quotas separately. | [official-docs-reviewed](https://github.com/ollama/ollama) / 2026-09-12 |

## network-monitoring

**DNS and network monitoring**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) | Self-hosted DNS filtering for network-wide ad and tracker domains | linux, windows, macos, web · self-hosted | open-source; binary/model/service costs may differ · GPL-3.0 | Requires a running host and DNS configuration; cannot block same-domain YouTube/Twitch ads or replace full content filtering. | [official-docs-reviewed](https://github.com/AdguardTeam/AdGuardHome) / 2026-09-12 |
| [Pi-hole](https://github.com/pi-hole/pi-hole) | Centralized DNS blocking and query statistics on your own Linux host | linux, web · self-hosted | open-source; binary/model/service costs may differ · EUPL-1.2（Core；其他元件依各授權） | Needs a running Linux/container host and DNS setup. Domain filtering does not replace all browser content blocking; hardware/maintenance cost extra. | [official-docs-reviewed](https://github.com/pi-hole/pi-hole) / 2026-09-12 |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | Monitor website and service uptime with alerts and status pages | web, linux, windows · self-hosted | open-source; binary/model/service costs may differ · MIT | Requires maintained hosting; data directories cannot use NFS. A shared host failure may take down both the target and its monitor. | [official-docs-reviewed](https://github.com/louislam/uptime-kuma) / 2026-09-12 |

## personal-finance

**Personal finance and accounting**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [GnuCash](https://github.com/Gnucash/gnucash) | Double-entry personal and small-business accounting | macos, windows, linux · desktop | free and open-source · GPL-2.0 或 GPL-3.0；部分檔案有 OpenSSL 例外 | Requires accounting setup; Taiwanese bank imports, tax reports and e-invoice workflows are unverified, not a localized accounting-suite claim. | [official-docs-reviewed](https://github.com/Gnucash/gnucash) / 2026-09-12 |
| [Actual Budget](https://github.com/actualbudget/actual) | Local-first budgeting and personal finance with optional sync server | macos, windows, linux, web · desktop | open-source; binary/model/service costs may differ · MIT | Bank integrations require actual-server and third-party providers; listed coverage does not establish Taiwanese bank support. | [official-docs-reviewed](https://github.com/actualbudget/actual) / 2026-09-12 |
| [Money Manager Ex](https://github.com/moneymanagerex/moneymanagerex) | Track household spending, cards, assets and multi-account cash flow | macos, windows, linux · desktop | free and open-source · GPL-2.0 | Desktop edition reviewed; mobile compatibility and synchronization need separate checks. Taiwanese bank automation and business tax filing are unverified. | [official-docs-reviewed](https://github.com/moneymanagerex/moneymanagerex) / 2026-09-12 |

## privacy-security

**Privacy and security**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [Cryptomator（桌面版）](https://github.com/cryptomator/cryptomator) | Encrypt files and filenames before existing cloud synchronization | macos, windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0（另提供商業授權） | Does not supply cloud storage. Mobile free editions are read-only; write access requires separate platform licenses. | [official-docs-reviewed](https://github.com/cryptomator/cryptomator) / 2026-09-12 |
| [Portmaster](https://github.com/safing/portmaster) | Application firewall with connection control, DNS and tracker blocking | windows, linux · desktop | open-source; binary/model/service costs may differ · GPL-3.0 | Network history, bandwidth reporting and SPN have paid boundaries. Desktop support is Windows/Linux, not macOS. | [official-docs-reviewed](https://github.com/safing/portmaster) / 2026-09-12 |

## remote-access

**Remote access and device management**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [RustDesk](https://github.com/rustdesk/rustdesk) | Cross-platform remote desktop with optional self-hosted relay | macos, windows, linux, android · desktop | open-source; binary/model/service costs may differ · AGPL-3.0 | OSS server differs from Server Pro; verify centralized administration and SSO requirements, plus hosting costs. | [official-docs-reviewed](https://github.com/rustdesk/rustdesk) / 2026-09-12 |
| [Apache Guacamole](https://github.com/apache/guacamole-client) | Browser gateway for RDP, VNC and SSH sessions | web · self-hosted | open-source; binary/model/service costs may differ · Apache-2.0 | Browser clients need no plugin, but the gateway and destination protocol services still need deployment and maintenance. | [official-docs-reviewed](https://github.com/apache/guacamole-client) / 2026-09-12 |
| [MeshCentral](https://github.com/Ylianst/MeshCentral) | Self-hosted device management with remote desktop, terminal and files | web, windows, macos, linux · self-hosted | open-source; binary/model/service costs may differ · Apache-2.0 | Requires a server and managed-device agents; administrators maintain TLS, accounts, updates and backups. | [official-docs-reviewed](https://github.com/Ylianst/MeshCentral) / 2026-09-12 |

## rss-reference

**Feeds and reference management**

| Tool | Use | Platform / delivery | Cost / license | Limits | Evidence |
|---|---|---|---|---|---|
| [FreshRSS](https://github.com/FreshRSS/FreshRSS) | Self-hosted RSS/Atom aggregation for cross-device article reading | web · self-hosted | open-source; binary/model/service costs may differ · AGPL-3.0 | Requires server deployment and feed refresh scheduling. API compatibility does not reproduce every paid-reader feature; hosting and backups remain yours. | [official-docs-reviewed](https://github.com/FreshRSS/FreshRSS) / 2026-09-12 |
| [RSS Guard](https://github.com/martinrotter/rssguard) | Desktop RSS/Atom/JSON reading with optional feed-service integrations | macos, windows, linux · desktop | free and open-source · GPL-3.0 | Local reading works independently; external service plans/API limits still apply and cross-device sync needs a backend. | [official-docs-reviewed](https://github.com/martinrotter/rssguard) / 2026-09-12 |
| [Zotero](https://github.com/zotero/zotero) | Collect, organize, annotate and cite research sources and PDFs | macos, windows, linux, android, ios · desktop | open-source; binary/model/service costs may differ · AGPL-3.0 | Metadata sync is free and unlimited; file storage has 300 MB free. More storage costs extra; WebDAV supports personal, not group libraries. | [official-docs-reviewed](https://github.com/zotero/zotero) / 2026-09-12 |
| [JabRef](https://github.com/JabRef/jabref) | Manage BibTeX/BibLaTeX libraries, research metadata and citations | macos, windows, linux · desktop | free and open-source · MIT | Primarily a .bib workflow; test word-processor integration and imported fields. Metadata retrieval does not grant full-text access. | [official-docs-reviewed](https://github.com/JabRef/jabref) / 2026-09-12 |
