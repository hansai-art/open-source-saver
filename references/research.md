# Expand coverage without weakening recommendations

Use this reference for catalog expansion and research tasks. A user's bulk research request is not subject to the normal three-candidate shortlist limit.

## Research ladder

1. Search the reviewed catalog by task and original paid software; inspect the actual gaps.
2. Search `python3 scripts/saver.py discover "QUERY" --limit 30` for upstream discovery leads. Chinese terms have explicit translations in `data/discovery-keywords.json`; this is not semantic search. The upstream index is separately licensed and unreviewed. Do not load the whole index into model context.
3. Reuse `data/research-sources.json`, `data/article-sources.json`, `data/community-sources.json` and `docs/RESEARCH.md` to find existing comparisons and regional experience. Record exactly what was read; a search snippet is not a full article review.
4. For selected candidates, read current official product/repository docs and license. Confirm actual edition, platform and delivery, free distribution vs source, hosted/AI/API costs, essential feature gaps and maintenance warnings. Name the replacement use case rather than promising complete equivalence.
5. Add only reviewed entries to `data/products.json`, with bilingual use/limits, individual dates and sources. Preserve unknown localization and untested runtime. Add specific, conditional mappings in `data/alternatives.json`; deduplicate software, aliases and repository URLs.
6. Regenerate with `scripts/build_catalog.py` and `scripts/build_research.py`, validate, then update the repo. Imported upstream facts keep their attribution and license; original summaries link to articles rather than reproduce them.

## Depth for consequential migrations

Pick a real acceptance task: open/edit/export a representative file, migrate a small workspace, restore a backup, or reproduce the core workflow. Record version, OS, architecture, free edition, result and unsupported feature. Reading docs only qualifies for documentation review. A project license never proves the official binary, cloud plan, model weights or integrations are all free.

Measure unique products, useful categories, named-product mappings, research provenance and unresolved gaps separately. Do not sum overlapping indexes or turn an ambition such as “world's most complete” into an established ranking. Stop a research pass when its agreed breadth is met and remaining items are explicitly queued; prioritize new domains and contradictory evidence over repeated broad searches.
