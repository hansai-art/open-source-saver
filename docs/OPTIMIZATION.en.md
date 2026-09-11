# Open Source Saver v0.2 optimization specification

Date: 2026-09-11 · Status: specification decided; implementation follows the milestones below.

[繁體中文](OPTIMIZATION.zh-TW.md) · [Current specification](SPEC.en.md) · [Verification status](STATUS.md)

## Product decisions

Reuse existing software before proposing development. Serve Taiwan general users and audiovisual creators; free proprietary products are eligible. Improve evidence and coverage before building more software. Reuse GitHub, Markdown, JSON and existing scripts. Do not build recording, transcription or subtitle engines, a cloud account system, database or desktop application.

The first public release remains v0.1.0-alpha. This document does not claim that v0.2 is implemented. The baseline is 58 products, 14 conditional mappings and 11 articles. The 53 discovery names overlap with products and must not be added to the total.

## Priorities and acceptance

| Priority | Gap | Decision | Acceptance |
|---|---|---|---|
| P0 | Few source-product mappings | Expand by task, then add names | 20 representative needs each have qualifying candidates or an explicit gap |
| P0 | Open source does not prove a free installer | Separate binary, hosting, compilation and model/API costs | No source-only candidate passes a no-compilation requirement |
| P0 | Coarse evidence labels | Attach sources and dates to required features | Unknown cannot pass mandatory requirements |
| P0 | One localization field | Separate documentation, UI, Chinese content and Taiwan speech | Evidence cannot be transferred between these dimensions |
| P1 | Keyword search misses task synonyms | Add task aliases and empty-result guidance | Dictation synonyms resolve to the same task |
| P1 | Mixed-language catalogs | Generate complete translations from shared JSON | Same IDs, counts, ordering and links in both languages |
| P1 | Collectors lack native validation | Test ordinary-permission Mac and Windows | Record omissions and coverage instead of claiming full-device scanning |

## Scale and entry gates

Targets: at least 200 deduplicated discovery candidates, 80 products with minimum official verification, and 40 source-app or task mappings. These are future targets, not current results. Do not lower quality to meet them.

Discovery requires a name, originating source, task and discovery date. Minimum official verification requires the official site, acquisition page, platforms, free acquisition conditions, license or terms source, and one core use plus limitations. Incomplete products remain discovery leads. Reading documentation is not a workflow test.

Do not count aliases, versions, OS variants or web/desktop editions as separate products. Keep edition records. Renames, forks and discontinued products use canonical_id, previous_names and related_project; similar names alone cannot justify merging.

The 20 task fixtures are: long course recording, tutorial auto-zoom, short recording sharing, screenshot annotation, scrolling screenshots, OCR, dictation, long-audio transcription, multi-speaker transcripts, subtitle correction, Traditional Chinese subtitle export, TTS, silence cutting, lossless trimming, transcoding/compression, audio denoising, photo editing, vector drawing, Office documents and PDF editing. Each fixture names at least one of Mac or Windows and records known gaps on the other platform.

## Reuse strategy

Use the existing 11 articles for names, task context and paid-app relationships. Retain links, bibliographic metadata and original summaries; do not redistribute full articles. Evaluate opensource.builders, RunaCapital/awesome-oss-alternatives and other awesome lists for reusable mappings only after checking their current format, scope, data license and maintenance.

Official downloads, terms and documentation establish product facts. Article popularity and GitHub stars do not prove quality. Community submissions enter the catalog only after review. Prefer direct references or a small format conversion when legal reusable data exists. Add an adapter only for demonstrated repeated work; do not start with a universal scraper. If lawful batch access is unavailable, keep manual submissions and source indexes.

## Schema v2 contract and migration

Keep schema v1 working until a reproducible migration is ready. Preserve product IDs.

Required fields: id, canonical_name, aliases, category, platforms, official_url, acquisition_url, delivery, cost_type, source_license, commercial_terms, localization, claims, sources and status.

- delivery: builtin, desktop-binary, browser-extension, web-service, self-hosted, source-only or engine. A product may have multiple editions.
- cost_type: free, freemium, paid, trial or unknown. Record free limits and chargeable components separately. Unknown is not free.
- localization: docs_zh_tw, ui_zh_tw, chinese_content and taiwan_speech; each has yes/no/partial/unknown and supporting evidence. Speech tests include their method.
- claims: feature, value (yes/no/partial/unknown), edition, platform, source_url, checked_on, optional tested_on and test_notes.
- sources: url, kind (article/official/runtime), checked_on and reuse_notes. An article establishes what it recommended, not necessarily current free terms.
- status: discovered, documented, workflow-tested, stale or archived. Workflow testing requires OS, version, task and result, not a bare boolean.

Store relationships separately: source_name/task_id, aliases, target_id, replaces, does_not_replace, required_setup and evidence. Recording capability does not prove replacement of recording, zoom, subtitles and sharing together.

Do not infer cost_type from a license string or upgrade unknown localization. Retain unknown when migration cannot establish a field. Validate v2 in a separate file before switching and preserve rollback to v1.

## Recommendation behavior

1. Collect only decision-changing details: OS, source app/task, mandatory features and acceptable setup. Search immediately when sufficient context exists.
2. Check built-in capabilities and the snapshot, then reuse articles, directories and official evidence for gaps. Strict offline use must not connect or load private inventories into cloud context.
3. Filter mandatory requirements first. Unsupported and unknown features cannot enter the confirmed-fit result set.
4. Rank eligible tools by installation burden, clear free scope, localization, delivery compatibility and maintenance evidence. Do not invent numerical confidence or rank by stars.
5. Compare up to three tools with replacement scope, gaps, acquisition and a trial task. Expand once for a specific unmet requirement.
6. Retain a paid tool or propose a clearly unverified multi-tool workflow when no candidate qualifies. Do not install tools or cancel subscriptions automatically.

Output: recommendation level, tool, task, OS, cost type, localization, official acquisition, limits, evidence date and trial task. Savings require actual avoidable spending and must not double-count bundles.

## Maintenance and verification

Start with demand-driven updates; no scheduled updater. Recheck free terms, downloads and mandatory features when recommending; evidence older than 30 days needs review. Preserve link-failure status and history instead of deleting a product immediately. Discontinued maintenance is a sourced risk, not automatic proof of unusability.

Validate ID uniqueness, alias conflicts, URLs, dates, references, translations and agreement between data and generated catalogs. Treat search results and submissions as data, never instructions to execute commands. Never use private inventories as fixtures or issue attachments.

## GitHub and user access

Destination: hansai-art/open-source-saver, Public, MIT for original project content. Chinese README first, English switch at the top. Offer three paths: browse categories without installation, install the Skill, or run local commands.

Include product aliases, common paid apps, Chinese task terms, official links and platforms for GitHub text search. Use Markdown category anchors and GitHub search before building a search website. Provide tool-submission and correction templates covering tasks, platforms, costs, sources, localization and test status without asking for complete installed-app lists.

## Milestones

| ID | Work | Dependency | Completion |
|---|---|---|---|
| O01 | Bilingual optimization spec, README entries, submission templates | None | Delivered in this update; local document links resolve |
| O02 | Schema v2, migration and validator | O01 | Preserve all 58 IDs and unknowns; rollback works |
| O03 | Source review, deduplication and mappings | O02 | Reach 200/80/40 or explicitly block release; no padding |
| O04 | Mandatory-feature/setup filtering and explanations | O02 | 20 task fixtures pass; unknown never passes a hard requirement |
| O05 | Native inventory and installation walkthroughs | O04 | One ordinary-permission record per OS, including omissions and Unicode |
| O06 | Public alpha, then v0.2 | Alpha may follow O01; v0.2 requires O02–O05 | Remote completeness, tested acquisition and explicit completion status |

Full-device coverage and replacing every paid product are not release requirements. These observable gates define completion. Missing source rights, mandatory evidence or target-device access keeps the release at alpha with explicit blockers.
