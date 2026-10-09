# Review of seven ArtCraft Adobe alternatives

[繁體中文](artcraft.md) · [English](artcraft.en.md)

Reviewed 2026-10-09. Begin with small PhotoCraft, VectorCraft and PdfCraft trials; keep EffectCraft for research.

ArtCraft Crafting Apps are seven independent third-party applications with MIT OR Apache-2.0 code. Adobe source, other Creative Cloud products and ArtCraft's AI image/video service are outside this seven-app catalog addition. Count savings by the cancellable bill.

## Versions, downloads and localization

All seven release listings contain universal macOS DMGs, Windows installers, Linux packages and separate WebAssembly archives. Web archives require hosting; fixed-version downloads are linked below.

| Original | Tool / version | Adoption | Traditional Chinese UI |
|---|---|---|---|
| Photoshop | [PhotoCraft v0.5.0](https://github.com/storytold/photocraft/releases/tag/v0.5.0) | Early trial | Present; quality untested |
| Illustrator | [VectorCraft v0.7.0](https://github.com/storytold/vectorcraft/releases/tag/v0.7.0) | Early trial | Present; quality untested |
| Premiere Pro | [FilmCraft v0.4.0](https://github.com/storytold/filmcraft/releases/tag/v0.4.0) | Early trial | Absent in reviewed version |
| Lightroom | [LightCraft v0.4.0](https://github.com/storytold/lightcraft/releases/tag/v0.4.0) | Early trial | Present; quality untested |
| Acrobat | [PdfCraft v0.4.0](https://github.com/storytold/pdfcraft/releases/tag/v0.4.0) | Early trial | Present; quality untested |
| After Effects | [EffectCraft v0.6.0](https://github.com/storytold/effectcraft/releases/tag/v0.6.0) | Research only | Absent in reviewed version |
| InDesign | [DesignCraft v0.4.0](https://github.com/storytold/designcraft/releases/tag/v0.4.0) | Early trial | Absent in reviewed version |

UI language status comes from each reviewed version's registry/catalog. Text display, UI translation, OCR, editing and Taiwan glyph forms are separate capabilities. LightCraft documents Simplified-first desktop fonts and unverified web glyph coverage.

## Gaps and useful trial tasks

### PhotoCraft

Early alpha. Professional typography, generative features and Photoshop plugins have gaps. Upstream PSD corpus scores are author tests; check client PSDs, fonts and smart objects. Traditional Chinese UI is present; translation and glyph quality are untested.

Trial: Round-trip a copied PSD with Chinese type, masks and smart objects, then compare it in Photoshop.

Sources: [README](https://github.com/storytold/photocraft/blob/v0.5.0/README.md) · [Cargo / license](https://github.com/storytold/photocraft/blob/v0.5.0/Cargo.toml) · [Release](https://github.com/storytold/photocraft/releases/tag/v0.5.0) · [UI language](https://github.com/storytold/photocraft/blob/v0.5.0/crates/ui-egui/src/i18n/mod.rs)

### VectorCraft

Actively developed. AI import covers PDF-compatible files; 3D/materials, CJK vertical composition and some effects remain incomplete. Start with new vector work. Traditional Chinese UI is present; translation and glyph quality are untested.

Trial: Trial an SVG and a PDF-compatible AI sample, checking layers, gradients, Chinese fonts and PDF export.

Sources: [README](https://github.com/storytold/vectorcraft/blob/v0.7.0/README.md) · [Cargo / license](https://github.com/storytold/vectorcraft/blob/v0.7.0/Cargo.toml) · [Release](https://github.com/storytold/vectorcraft/releases/tag/v0.7.0) · [UI language](https://github.com/storytold/vectorcraft/blob/v0.7.0/crates/ui-egui/src/i18n/mod.rs)

### FilmCraft

Early development. Large-media performance, camera/phone files and cross-platform coverage need work; no VST3, Audio Units or OpenFX hosting. Premiere migration is untested. Official HEVC export descriptions conflict; verify the OS/GPU path. This version has no Traditional Chinese UI in its language registry.

Trial: Edit 30 seconds of phone footage with Chinese captions and music; check picture, audio and sync.

Sources: [README](https://github.com/storytold/filmcraft/blob/v0.4.0/README.md) · [Cargo / license](https://github.com/storytold/filmcraft/blob/v0.4.0/Cargo.toml) · [Release](https://github.com/storytold/filmcraft/releases/tag/v0.4.0) · [UI language](https://github.com/storytold/filmcraft/blob/v0.4.0/crates/ui-egui/src/i18n.rs)

### LightCraft

Early development. Measured camera calibration and some RAW paths have gaps; Lightroom edit-history migration is untested. Trial your camera files. Traditional Chinese UI is documented; desktop fonts prefer Simplified Chinese glyph forms, and web glyph coverage is unverified.

Trial: Import three RAWs from your camera and check white balance, skin tones, highlights and batch JPEG export.

Sources: [README](https://github.com/storytold/lightcraft/blob/v0.4.0/README.md) · [Cargo / license](https://github.com/storytold/lightcraft/blob/v0.4.0/Cargo.toml) · [Release](https://github.com/storytold/lightcraft/releases/tag/v0.4.0) · [UI language](https://github.com/storytold/lightcraft/blob/v0.4.0/docs/localization-zh-hant.md)

### PdfCraft

Early development; formerly PrintCraft. Existing-text editing, especially CJK, non-Latin OCR, Office conversion and long-term signature validation have gaps. Start with page operations. Traditional Chinese UI is present; Chinese text editing and OCR require separate validation.

Trial: Merge, split, annotate and print a non-confidential Chinese PDF; evaluate text editing and OCR separately.

Sources: [README](https://github.com/storytold/pdfcraft/blob/v0.4.0/README.md) · [Cargo / license](https://github.com/storytold/pdfcraft/blob/v0.4.0/Cargo.toml) · [Release](https://github.com/storytold/pdfcraft/releases/tag/v0.4.0) · [UI language](https://github.com/storytold/pdfcraft/blob/v0.4.0/crates/ui-egui/src/i18n/mod.rs)

### EffectCraft

Upstream describes an early tool; retain After Effects for client work. Cannot open .aep/.aepx or host After Effects plugins. An effect's presence does not establish matching behavior. No Traditional Chinese UI in this version; CLI/MCP are documentation-reviewed only.

Trial: Create a new five-second title and trial CLI rendering, alpha and audio; retain client AE projects in After Effects.

Sources: [README](https://github.com/storytold/effectcraft/blob/v0.6.0/README.md) · [Cargo / license](https://github.com/storytold/effectcraft/blob/v0.6.0/Cargo.toml) · [Release](https://github.com/storytold/effectcraft/releases/tag/v0.6.0) · [UI language](https://github.com/storytold/effectcraft/blob/v0.6.0/crates/ui-egui/src/i18n.rs)

### DesignCraft

Actively developed. INDD is unreadable; full InDesign CJK composition, frame grids and detailed ruby remain incomplete. Proof Chinese IDML, PDFs and print specifications. This version has Simplified but no Traditional Chinese UI. The README's PDF roadmap wording is stale; roadmap and release notes list PDF functionality.

Trial: Lay out a two-page Chinese brochure with images and paragraph styles; proof IDML/PDF, line breaks, bleed and fonts.

Sources: [README](https://github.com/storytold/designcraft/blob/v0.4.0/README.md) · [Cargo / license](https://github.com/storytold/designcraft/blob/v0.4.0/Cargo.toml) · [Release](https://github.com/storytold/designcraft/releases/tag/v0.4.0) · [UI language](https://github.com/storytold/designcraft/blob/v0.4.0/crates/ui-egui/src/i18n.rs) · [Roadmap](https://github.com/storytold/designcraft/blob/v0.4.0/ROADMAP.md)

## Automation and evidence scope

All seven document CLI, MCP and JSON control interfaces. Start background-processing experiments with small test files; metadata retains `automation.runtime_tested: false`.

This review covers version docs, licenses, asset listings and locale definitions, plus this repository's search/report behavior. Third-party installation, GUI, performance, migration and MCP workflows are untested; upstream compatibility scores remain author tests.

[Product data](../../data/products.json) · [Usage and adoption](../USAGE.en.md)
