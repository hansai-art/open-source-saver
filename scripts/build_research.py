#!/usr/bin/env python3
"""Build international bibliography and expansion measurements, offline."""
import json
from collections import Counter
from pathlib import Path
from saver import escape, normalize, read_json

ROOT = Path(__file__).resolve().parents[1]


def main():
    research = read_json(ROOT / 'data/research-sources.json')
    sources = research['sources']
    products = read_json(ROOT / 'data/products.json')['products']
    stats = read_json(ROOT / 'data/catalog-stats.json')
    baseline = read_json(ROOT / 'data/expansion-baseline.json')
    upstream = read_json(ROOT / 'data/upstream/awesome-selfhosted/index.json')
    if len({s['id'] for s in sources}) != len(sources) or len({s['url'] for s in sources}) != len(sources):
        raise ValueError('Duplicate research source ID or URL')
    names = {normalize(n): p for p in products for n in [p['name'], *p.get('aliases', [])]}
    lines = ['# 國內外研究來源與收錄去向', '',
             '每筆保留實際閱讀範圍、候選名稱與原創摘要。目錄局部讀取不代表逐項核對，文章觀點也不等於官方功能或授權證據。', '',
             '[研究方法與缺口](RESEARCH.md) · [工具目錄](CATALOG.zh-TW.md) · [結構化資料](../data/research-sources.json)', '']
    for s in sources:
        linked = []
        for name in s['selected_candidates']:
            product = names.get(normalize(name))
            linked.append((f"[{escape(name)}](CATALOG.zh-TW.md#{product['category']})" if product else escape(name)))
        lines += [f"## {s['id']} · {s['title']}", '',
                  f"[{s['publisher']}]({s['url']}) · {s['language']} · {s['region']} · {s['checked_on']}", '',
                  f"- 閱讀狀態：{s['read_status']}；{s['review_scope']}",
                  f"- 提取重點：{s['zh_summary']}",
                  f"- 工具線索：{'、'.join(linked) or '此來源提供研究方法或分類入口'}", 
                  f"- 採用限制：{s['caveat']}", '']
        for evidence in s.get('verification_sources', []):
            lines += [f"官方回查：[來源]({evidence['url']}) — {evidence['note']}", '']
    (ROOT / 'docs/RESEARCH-SOURCES.md').write_text('\n'.join(lines), encoding='utf-8')
    # Link older article discoveries to reviewed additions, preserving original article evidence.
    discovery_path = ROOT / 'data/discovery.json'
    discovery = read_json(discovery_path)
    for item in discovery['candidates']:
        if not item.get('catalog_id'):
            product = names.get(normalize(item['name']))
            if product:
                item['catalog_id'] = product['id']
    discovery_path.write_text(json.dumps(discovery, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    metrics = {
        'updated_on': research['checked_on'], 'baseline_commit': baseline['commit'],
        'baseline_products': baseline['products'], 'curated_products': len(products),
        'product_growth_factor': round(len(products)/baseline['products'], 2),
        'baseline_categories': baseline['categories'], 'curated_categories': stats['category_count'],
        'category_growth_factor': round(stats['category_count']/baseline['categories'], 2),
        'conditional_mappings': stats['mapping_count'],
        'new_research_sources': len(sources),
        'source_languages': dict(Counter(s['language'] for s in sources)),
        'source_read_statuses': dict(Counter(s['read_status'] for s in sources)),
        'legacy_article_sources': len(read_json(ROOT/'data/article-sources.json')['articles']),
        'upstream_unique_records': len(upstream['entries']),
        'upstream_commit': upstream['source']['commit'],
        'runtime_tested_products': sum(p['runtime_tested'] for p in products),
        'acceptance': {'products_at_least_double': len(products) >= baseline['minimum_products'],
                       'categories_at_least_double': stats['category_count'] >= baseline['minimum_categories']},
        'counting_rule': baseline['counting_rule']}
    (ROOT/'data/research-stats.json').write_text(json.dumps(metrics, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
