#!/usr/bin/env python3
"""Regenerate both public catalogs from the same product data."""
import json
from pathlib import Path
from saver import render, validate

ROOT = Path(__file__).resolve().parents[1]


def main():
    catalog = json.loads((ROOT / 'data/products.json').read_text(encoding='utf-8'))
    mappings = json.loads((ROOT / 'data/alternatives.json').read_text(encoding='utf-8'))['mappings']
    validate(catalog, mappings)
    products = catalog['products']
    for lang in ['zh-TW', 'en']:
        title = '開源與免費軟體清單' if lang == 'zh-TW' else 'Open-source and free software catalog'
        lines = ['# ' + title, '', '[繁體中文](CATALOG.zh-TW.md) · [English](CATALOG.en.md)', '',
                 f"{len(products)} candidate products. Snapshot: {catalog['checked_on']}. No product workflow or Chinese-quality tests claimed.",
                 '候選清單，非完整替代保證；與文章發現名單有重疊，不能相加。', '',
                 '[Sources](SOURCES.md) · [JSON](../data/products.json) · [Contribute](../CONTRIBUTING.md)', '']
        for category in dict.fromkeys(p['category'] for p in products):
            lines += ['## ' + category, '', render([p for p in products if p['category'] == category], lang), '']
        (ROOT / f'docs/CATALOG.{lang}.md').write_text('\n'.join(lines), encoding='utf-8')
    print('Both catalogs generated.')


if __name__ == '__main__':
    main()
