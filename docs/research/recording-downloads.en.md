# Recording Post-production and Download Research Guide

Evidence date: 2026-10-10. This page records reviews of official documentation, releases, and source code; no acceptance test has run on the user's Windows, Mac, or Linux device.
Versions and features are snapshots. Recheck downloads, licenses, platforms, and extension compatibility before recommending.

## Contents

- [Selection rules](#selection-rules)
- [Recording requirements](#recording-requirements)
- [Recording boundaries](#recording-boundaries)
- [Download tools](#download-tools)
- [Varia Traditional Chinese review](#varia-traditional-chinese-review)
- [Five-minute acceptance check](#five-minute-acceptance-check)
- [Official sources and exclusions](#official-sources-and-exclusions)

## Selection rules

- For post-recording automatic zoom, captions, and further customization, try the maintained OpenScreen continuation first.
- For entirely local silence cuts, use Auto-Editor as a workflow component alongside a recorder, not as a complete screencast editor.
- For consistent Traditional Chinese captions, check recognition, character conversion, and subtitle output separately; a Traditional Chinese UI does not prove Traditional Chinese recognition output.
- Prefer Varia's existing download features. On Mac, compare Gopeed when a usable native release matters, and check the video extension version separately.
- When one small feature is missing, patch upstream or add a processing step before creating another equivalent product.

## Recording requirements

| Tool | License / recent release | Remove unwanted content | Automatic zoom | Chinese captions / main gap |
| --- | --- | --- | --- | --- |
| [Maintained OpenScreen](https://github.com/getopenscreen/openscreen) | MIT, v2.0.0, 2026-10-03 | Smart cuts requires an LLM; transcript deletion is interactive editing | Click data captured by its own recorder | Local Whisper Chinese; no fixed Traditional Chinese setting found; no SRT / VTT |
| [Recordly](https://github.com/webadderallorg/Recordly) | AGPL-3.0 plus branding terms, v1.4.0, 2026-09-08 | Manual timeline editing verified; semantic automatic cuts unverified | Zoom suggestions from cursor activity | Local captions and SRT / VTT output; fixed Traditional Chinese conversion unverified |
| [Auto-Editor](https://github.com/WyattBlue/auto-editor) | Unlicense, 31.7.2, 2026-10-03 | CLI silence cuts based on audio thresholds | Not cursor-tracking zoom | Do not present as a ready-made Traditional Chinese caption tool |
| [Flowtake](https://github.com/JNX03/Flowtake) | MIT, v1.7.2, 2026-09-12 | Trim / split verified | Cursor-driven zoom / pan | Reviewed language dropdown lacks Chinese; do not claim ready-made Traditional Chinese captions |
| [OpenCC](https://github.com/BYVoid/OpenCC) | Apache-2.0, Chinese conversion engine | No video editing | None | Offline Simplified-to-Traditional and Taiwan wording conversion; cannot fix ASR errors |

## Recording boundaries

Use `getopenscreen/openscreen` for OpenScreen. The original `siddharthvaddem/openscreen` repository is archived; do not present it as the maintained line.
Automatic zoom reads the recording's `.cursor.json`. Imported MP4s can be edited and captioned, but without equivalent cursor data they lack the same automatic zoom capability.
Holding the pointer still over something without clicking also does not create an automatic zoom for that moment.

Local Whisper transcription, burned-in captions, and transcript deletion are free. Deleting selected words or silences cuts the video, but still requires user action.
Smart cuts lets an external LLM decide edits and requires a chosen provider; its API may cost money. Do not label it entirely offline, free automatic editing.
Local MCP lets an existing AI agent operate the editor; the CLI records, captions, and exports. Both shipped in v2 and avoid GUI automation; the CLI still needs a desktop/display session, and a Linux capture portal may require user selection. Do not describe capture as fully unattended.
Silero VAD skipping silence during recognition does not mean the exported video automatically removes every silence.

For consistent Traditional Chinese output, add OpenCC after transcription, preserve caption timestamps, then burn in or export the result.
OpenCC converts characters and regional wording; proper nouns, Taiwan-accent recognition errors, and caption segmentation need separate review.
When a course platform requires SRT / VTT, OpenScreen needs an output addition; Recordly already provides subtitle sidecar output.
Old Recordly forks may still say MIT. Review the current upstream AGPL and branding terms rather than mixing license descriptions.

## Download tools

| Tool | Free scope and license | Verified uses / platforms | Updates and selection conditions |
| --- | --- | --- | --- |
| [Varia](https://github.com/giantpinkrobots/varia) | Free, MPL-2.0 | aria2 + yt-dlp for files, torrents, and media; Windows / Linux; experimental Mac Intel / ARM builds | v2026.8.5-1, 2026-08-23; `next` received code updates on 2026-10-03 |
| [Gopeed](https://github.com/GopeedLab/gopeed) | Free, GPL-3.0 | Multi-connection downloads on Mac / Windows / Linux; video extensions available | Stable v1.9.3, 2026-03-18; current YouTube extension requires 2.0 |

Gopeed 2.0.0-beta.3 was published on 2026-09-18 UTC, which is 09-19 in Taiwan. List beta and stable releases separately.
The current [monkeyWie YouTube extension](https://github.com/monkeyWie/gopeed-extension-youtube) requires Gopeed 2.0; old store summaries do not establish 1.9.3 compatibility.
The extension's `package.json` declares ISC; record it separately from Gopeed's GPL-3.0. Test an actual video download to verify extension compatibility.

## Varia Traditional Chinese review

Varia already includes Traditional Chinese; do not build a duplicate localized product. `po/zh_TW.po` has the same file SHA in `next` and the stable release.
This review counted 194 catalog messages: 125 translated and non-fuzzy, 26 fuzzy, and 43 empty.
125 / 194 = 64.4% is the translated, compilable share of that catalog, not completeness of the entire current interface.
The POT lags behind code; new or changed strings may be absent. Existing PO statistics cannot establish whole-product coverage.
`zh_TW` appears in `po/LINGUAS`, and the build's `msgfmt` does not include fuzzy translations.

On Windows / Mac, try setting the system preferred language to Traditional Chinese and restarting Varia, then check the display. A specific in-app language switch and each package's locale behavior have not been verified; do not invent a settings path.
On Linux, try `LANGUAGE=zh_TW varia`; results across packages and desktop environments remain untested.
Translation entry point: [Varia Traditional Chinese Weblate](https://hosted.weblate.org/projects/varia/varia/zh_Hant/).
Upstream [CONTRIBUTING.md](https://github.com/giantpinkrobots/varia/blob/next/CONTRIBUTING.md) rejects AI-generated translations, PR descriptions, and comments.
This work records gaps only; it creates no translations or upstream PR. Later, a human should refresh the POT, resolve fuzzy and empty entries, and verify the actual interface.

## Five-minute acceptance check

1. Record a one-minute demo with the candidate: three clicks, a two-second pause, Chinese narration, and one proper noun.
2. Check that automatic zoom follows clicks, then import an ordinary MP4 to compare behavior without cursor data.
3. Identify whether pause removal is manual, audio-threshold based, or LLM driven; ensure useful silent actions survive the export.
4. Generate Chinese captions; check Traditional characters, proper nouns, segmentation, and synchronization after cuts; export ten seconds to verify burn-in or SRT / VTT.
5. For a downloader, test pause / resume on an available test file, then video downloading and the Traditional Chinese UI; record OS, CPU architecture, package, and extension versions.

This is initial screening. Separately test long recordings, varying audio levels, batch exports, and platform-specific problems. Report source review as reviewed, not runtime-tested.

## Official sources and exclusions

- OpenScreen: [v2.0.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.0.0), [downloads](https://github.com/getopenscreen/openscreen/releases), [automatic zoom](https://getopenscreen.com/features/auto-zoom/), [captions](https://getopenscreen.com/docs/captions/), [AI / MCP](https://getopenscreen.com/docs/ai-editing/), [CLI](https://getopenscreen.com/docs/cli/).
- OpenScreen Chinese captions: [v2 language codes](https://github.com/getopenscreen/openscreen/blob/v2.0.0/src/lib/ai-edition/transcription/languageLabels.ts), [Whisper calls](https://github.com/getopenscreen/openscreen/blob/v2.0.0/electron/stt/whisperServer.ts).
- Recordly: [downloads](https://github.com/webadderallorg/Recordly/releases), [license and branding terms](https://github.com/webadderallorg/Recordly/blob/main/LICENSE.md), [subtitle output source](https://github.com/webadderallorg/Recordly/blob/v1.4.0/electron/ipc/register/exportCaptionSidecars.ts).
- Auto-Editor: [31.7.2](https://github.com/WyattBlue/auto-editor/releases/tag/31.7.2), [documentation](https://auto-editor.com/docs/), [license](https://github.com/WyattBlue/auto-editor/blob/master/LICENSE).
- Flowtake: [v1.7.2 / downloads](https://github.com/JNX03/Flowtake/releases/tag/v1.7.2). OpenCC: [official documentation](https://github.com/BYVoid/OpenCC), [license](https://github.com/BYVoid/OpenCC/blob/master/LICENSE).
- Varia: [official downloads](https://giantpinkrobots.github.io/varia/), [release](https://github.com/giantpinkrobots/varia/releases/tag/v2026.8.5-1), [Traditional Chinese catalog](https://github.com/giantpinkrobots/varia/blob/next/po/zh_TW.po), [language list](https://github.com/giantpinkrobots/varia/blob/next/po/LINGUAS), [build](https://github.com/giantpinkrobots/varia/blob/next/po/meson.build).
- Gopeed: [downloads](https://gopeed.com/download), [v1.9.3](https://github.com/GopeedLab/gopeed/releases/tag/v1.9.3), [2.0.0-beta.3](https://github.com/GopeedLab/gopeed/releases/tag/v2.0.0-beta.3), [extension requirement](https://github.com/monkeyWie/gopeed-extension-youtube/blob/main/README.md), [extension license field](https://github.com/monkeyWie/gopeed-extension-youtube/blob/main/package.json).

Excluded from first choices: XDM 8 is still a 2023 release and 9 is unreleased; Persepolis has 2025 releases but this review found no verified 2026 maintenance evidence.
Coherence has insufficient recent core progress. Cursor inactivity is not audio silence and cannot establish automatic removal of narration pauses.
