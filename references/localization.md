# 台灣使用情境 / Taiwan localization

Record four different facts: Traditional Chinese documentation, UI, content/format compatibility, and Taiwan speech quality. `zh-CN` alone is not `zh-TW` or `zh-Hant`.

先找上游語系與中文教學。缺翻譯依上游 Weblate、Crowdin、issue 或 PR 規則處理；只在使用者要求實際聯絡／貢獻時送出。不為翻譯先 fork 整個產品。

Use Taiwan terms: 軟體、檔案、資料夾、儲存、匯入、匯出、外掛程式. Preserve placeholders, shortcuts, brand names and markup. Simplified-to-Traditional conversion is a draft, not QA.

Check locale presence and completeness separately. For gettext, inspect `LINGUAS`, PO/POT and current source extraction: count nonempty non-fuzzy entries, fuzzy entries and untranslated entries, and check whether the template lags source. Fuzzy translations are not normally compiled unless the build opts in; do not describe their text as a confirmed runtime UI defect. A catalog percentage is not whole-interface coverage. Record the reviewed release/ref and keep runtime quality unknown until tested.

For speech-generated captions, distinguish UI localization, Chinese ASR and output script. A `zh` recognition setting is not a verified `zh-TW` subtitle setting. OpenCC can normalize script and Taiwan vocabulary but cannot correct recognition or timing errors. Preserve timestamps and placeholders when integrating conversion.

Varia already includes `zh_TW`; the 2026-10-10 review found incomplete translations and a stale POT, not a missing locale. Follow [Varia's current contribution guide](https://github.com/giantpinkrobots/varia/blob/next/CONTRIBUTING.md): ordinary translations go through Weblate, and AI-generated translations/PR descriptions/comments are not accepted. Do not submit an AI-produced translation on the user's behalf or conceal its origin. Offer an evidence-backed human review checklist and retain the existing language instead of making a duplicate product. See the recording/download research guide for the dated counts and sources.

For speech, test a consented sample with Mandarin, English names and relevant terminology; record model, hardware and settings. For documents, test real fonts, tracked changes, layout and export. Do not infer quality from a language-support label.
