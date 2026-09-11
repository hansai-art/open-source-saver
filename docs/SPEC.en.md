# Open Source Saver — v0.1.0-alpha specification

[繁體中文](SPEC.zh-TW.md) · [Home](../README.en.md)

## Goal and scope

Find existing open-source and free alternatives from a named paid app, a task, or an installed-app inventory. Traditional Chinese is primary; English is supported. Prefer existing/built-in capabilities, ready-to-use free products, open source when equally suitable, existing localization/tutorials, upstream translations, integration, then development as a last resort.

Deliver an Agent Skill and small local adapters, not a desktop application, cloud database, account system, background service or replacement media/office engine. Research works by reading Markdown without Python. Optional CLI and Mac collector require Python 3.10+ with only the standard library. Windows collection uses Windows PowerShell 5.1+.

## Inputs and responsibilities

| Entry | Input | Output |
|---|---|---|
| Named app | Screen Studio, Snagit, Word | Conditional candidates checked against actual requirements |
| Work task | Recording, dictation, PDF merging | Existing tool or built-in feature; no unnecessary inventory |
| Inventory | Collector JSON or manual names | Known source-product groups, candidates and unmatched items |

The agent interprets language and evaluates requirements. The CLI performs explicit aliases, keywords and static reports; it is not semantic search or a final recommendation engine. A cloud/container host is not the user's PC. Without access to the actual device, use manual import or provide local commands.

## Components

SKILL.md routes research and decisions. scripts/saver.py implements validation, search and private reports. collect_macos.py reads Info.plist metadata in known application folders. collect-windows.ps1 reads HKLM/HKCU uninstall records in both registry views and current-user Appx packages.

products.json has 58 bilingual candidate products; alternatives.json has 14 conditional source groups; article-sources.json has 11 references; discovery.json has 53 article-discovered names with optional catalog IDs. Those counts overlap and must not be added. CATALOG files expose the same data in Chinese and English; SOURCES preserves attribution. Tests cover data, matching, output privacy and fixture collection.

All initial product runtime_tested fields are false. Documentation review is distinct from product workflow testing. Counts are snapshots, not a maximum catalog size.

## Collection and minimization

Inventory envelope: schema_version, platform, collector, collected_at, coverage, warnings, applications. Allowed application metadata: name, version, and available publisher, bundle_id, package_id, collector. Do not collect serials, account names, install paths, uninstall commands, payment data or browsing history.

Mac reads /Applications, ~/Applications and /System/Applications, through at most two subdirectory levels. On an app bundle, read metadata without descending inside. Skip symlinks. Deduplicate by bundle ID/name and version. Failed reads produce generic warnings without paths. This limited implementation supersedes the earlier system_profiler-first proposal.

Windows uses no elevation, HKLM/HKCU Registry32/Registry64 and current-user Appx, excluding framework/resource packages. Never invoke Win32_Product, uninstall commands, other users' Appx enumeration or WinGet source updates. Preserve partial results and coverage warnings.

Neither collector promises portable apps, every user, extensions or all system components. Empty results do not prove an empty computer. Homebrew, WinGet and osquery may be manually used when already available and useful; their raw exports are not supported import formats in this release.

## CLI contract

| Command | Arguments | Result |
|---|---|---|
| validate | none | Check product IDs, fields, relationships, URLs, dates and alias conflicts |
| search QUERY | optional --platform, --lang, --json, --include-engines | Candidate list, explicit empty result |
| report | required --input, --output, --platform; optional --lang | Local Markdown; no raw inventory printed |
| collect_macos.py | --output | Local JSON, Mac only |
| collect-windows.ps1 | -OutputPath | Local JSON, Windows only |

Search platform values: macos/windows/linux/web/android/ios. Report supports the three desktop platforms. Unknown platforms cannot pass a requested platform filter. Engines are hidden unless explicitly included in search. Sort order is explicit relationship, exact name/category/keyword, then substring, not a quality score.

Accept UTF-8 with optional BOM: string arrays, objects with name/display_name, applications envelopes, or text files with one name per line. Maximum 10 MB input and 300 characters per name. Invalid schemas fail rather than silently becoming empty. Normalize Unicode NFKC, case and whitespace. Only explicitly permitted Adobe aliases accept year suffixes; never strip arbitrary digits. Preserve unknowns. Group known source versions in reports without inferring subscription count.

Refuse existing output files; create missing parent directories. POSIX outputs use 0600; Windows inherits folder ACLs. Print status only. Errors do not echo private names, paths or raw input. Python exits 0 on success and 2 on input/environment failures; PowerShell throws terminating errors. Bundled scripts make no network requests.

## Data and evidence

Product fields: id, name, category, keywords, platforms, delivery, url, sources, cost, license, evidence, checked_on, runtime_tested, zh_tw, zh/en.use, zh/en.limits. Delivery: desktop/builtin/extension/setup/engine. Categories cover recording, screenshots/OCR, dictation, transcription, subtitles, TTS, video, audio, graphics, office and PDF.

Upstream license summaries do not license this project or prove free models, official binaries or hosting. official-docs-reviewed denotes the previous official-documentation review; official-docs-partial covers selected positioning/free-tier facts only. Discovery means article leads. Unknown localization, commercial-use terms, platform support or functionality stays unknown.

MIT covers this project's original code, documentation and compilation. Link to articles with original short summaries; do not redistribute full articles or unlicensed datasets. Third-party software, models, assets, marks and services retain their terms.

## Recommendations, localization and costs

Mandatory platform, features, delivery formats and setup burden come before cost or popularity. Free proprietary products may rank first. Trials and commercial-use paid editions are not permanently free. Prefer finished apps for nondevelopers; show self-hosting/models when setup is acceptable.

Distinguish Traditional Chinese documentation, UI, content/font compatibility and Taiwan speech quality. Reuse upstream translation infrastructure and tutorials. A suggested translation does not authorize sending an issue, PR or message.

The agent labels Try, Conditional replacement, or Keep current tool, and states unknowns. CLI output is a candidate list only. Do not promise complete After Effects, Office macro or client project compatibility from name mappings.

Savings require actual avoidable future spending: next-12-month avoidable original cost minus replacement recurring and one-time cash costs. Count bundles once, do not treat nonrefundable prepaid charges as recoverable, and show time costs separately. CLI does not read bills or calculate savings.

## Privacy and publication

Cloud agent use can transmit supplied content. Strict offline use requires running collectors and reports directly on the target device without loading the private results into cloud conversations. Live research is separate. No automatic installs, removals, subscription changes, default-app changes or project migrations.

Do not publish real inventories, private reports, credentials, account paths or confidential work. Examples are explicitly synthetic. Ignore rules supplement, not replace, review of staged files.

## Acceptance and release gates

Verify known version aliases, negative near-name matches, platform filtering, hidden engines, Unicode/BOM import, duplicates, invalid schemas, unknown retention, status-only stdout/stderr, no overwrite and wrong-platform failure. Mac fixtures must cover metadata, versions, depth, warnings and symlinks. Windows still needs native syntax and HKLM/HKCU/Appx/Unicode device tests. Bilingual instructions must match executable commands.

An alpha may publish research/search/manual-import features with experimental collectors. Stable requires real Mac and Windows tests with ordinary permissions, offline network observation, an end-to-end report and host installation checks. Publishing alpha does not satisfy stable gates.

## Execution and maintenance

1. Implement specification, Skill, local scripts, data and bilingual docs.
2. Run data/behavior/scenario checks and fix demonstrated issues.
3. Publish an open alpha with reproducible limits.
4. Expand by actual needs and community reports; complete device tests before stable.

Reuse articles and catalogs first, compare a few plausible candidates, then do one focused expansion for a mandatory gap. Verify free tiers/downloads at recommendation time; revisit platform/license evidence after 30 days or a relevant release. No scheduled updater exists. If sources are unavailable, label snapshot dates and unknowns.

Success means users know what to try, which task it addresses, the gaps and official acquisition path. Download, trial, migration and cancelled renewal are distinct outcomes. A website, browser extension and upstream translations are outside this alpha's required implementation.
