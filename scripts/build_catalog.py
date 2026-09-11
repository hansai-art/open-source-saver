#!/usr/bin/env python3
"""Regenerate catalogs and README counts from one product dataset; no network."""
import json
import re
from collections import Counter
from pathlib import Path
from saver import render, validate

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_NAMES = {
    'screen-recording': ('螢幕錄影', 'Screen recording'),
    'screenshots-ocr': ('截圖與 OCR', 'Screenshots and OCR'),
    'dictation': ('語音輸入／聽寫', 'Voice typing / dictation'),
    'transcription': ('逐字稿與會議轉錄', 'Transcription and meetings'),
    'subtitles': ('字幕與翻譯', 'Subtitles and translation'),
    'text-to-speech': ('TTS 文字轉語音', 'Text to speech'),
    'video-editing': ('影片剪輯、合成與轉檔', 'Video editing, compositing and conversion'),
    'audio-editing': ('音訊編輯', 'Audio editing'),
    'graphics': ('修圖與繪圖', 'Graphics'),
    'office': ('文書與 Office', 'Office documents'),
    'pdf': ('PDF 閱讀與處理', 'PDF reading and processing'),
    'file-transfer': ('傳檔與檔案同步', 'File transfer and synchronization'),
    'productivity': ('視窗、剪貼簿與系統整理', 'Windows, clipboard and system utilities'),
    'archives': ('壓縮與解壓縮', 'Archives'),
    'media-players': ('影音播放', 'Media players'),
    'email': ('電子郵件', 'Email'),
    'passwords': ('密碼管理', 'Password management'),
    'notes-reading': ('筆記與電子書', 'Notes and ebooks'),
}


def replace_block(text, name, body):
    pattern = rf'<!-- {name}:start -->.*?<!-- {name}:end -->'
    result, count = re.subn(pattern, lambda _: f'<!-- {name}:start -->\n{body}\n<!-- {name}:end -->', text, flags=re.S)
    if count != 1:
        raise ValueError(f'Expected exactly one {name} block')
    return result


def main():
    catalog = json.loads((ROOT / 'data/products.json').read_text(encoding='utf-8'))
    mappings = json.loads((ROOT / 'data/alternatives.json').read_text(encoding='utf-8'))['mappings']
    validate(catalog, mappings)
    products = catalog['products']
    categories = Counter(p['category'] for p in products)
    kinds = Counter(p['source_type'] for p in products)
    if set(categories) - CATEGORY_NAMES.keys():
        raise ValueError('Add bilingual category labels before publishing a new category')
    if set(kinds) - {'open-source', 'proprietary', 'source-available'}:
        raise ValueError('Unknown source classification')
    stats = dict(updated_on=catalog['checked_on'], product_count=len(products), category_count=len(categories),
                 source_type_counts=dict(kinds), category_counts=dict(categories), mapping_count=len(mappings),
                 counting_rule='Unique product IDs; one primary category per product; sources and platform variants are not extra products.')
    (ROOT / 'data/catalog-stats.json').write_text(json.dumps(stats, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    ordered = [k for k in CATEGORY_NAMES if k in categories]
    for lang in ['zh-TW', 'en']:
        zh = lang == 'zh-TW'
        title = '開源與免費軟體清單' if zh else 'Open-source and free software catalog'
        summary = (f"**{len(products)} 個候選 · {len(categories)} 大類 · {kinds['open-source']} 個開源專案 · {kinds['proprietary']} 個非開源免費版／內建候選 · {kinds['source-available']} 個原始碼可見候選**" if zh else
                   f"**{len(products)} candidates · {len(categories)} categories · {kinds['open-source']} open-source projects · {kinds['proprietary']} proprietary free-tier/built-in candidates · {kinds['source-available']} source-available candidate**")
        note = (f"資料集更新：{catalog['checked_on']}；個別查核日見各列。包含引擎與需設定項目，不代表全部可免費一鍵安裝；工作流與繁中品質未實測。" if zh else
                f"Dataset updated: {catalog['checked_on']}; individual review dates remain in each row. Includes engines and setup-heavy projects, not all free one-click downloads. Workflows and Chinese quality untested.")
        lines = ['# ' + title, '', '[繁體中文](CATALOG.zh-TW.md) · [English](CATALOG.en.md)', '', summary, '', note, '',
                 '[Sources](SOURCES.md) · [Forums](FORUMS.md) · [JSON](../data/products.json) · [Contribute](../CONTRIBUTING.md)', '']
        table = ['| 分類 | 數量 | 例子 |' if zh else '| Category | Count | Examples |', '|---|---:|---|']
        for category in ordered:
            label = CATEGORY_NAMES[category][0 if zh else 1]
            entries = [p for p in products if p['category'] == category]
            # Stable raw category headings preserve existing catalog fragment links.
            lines += ['## ' + category, '', '**' + label + '**', '', render(entries, lang), '']
            examples = '、'.join(p['name'] for p in entries[:3]) if zh else ', '.join(p['name'] for p in entries[:3])
            table.append(f"| [{label}](docs/CATALOG.{lang}.md#{category}) | {len(entries)} | {examples} |")
        (ROOT / f'docs/CATALOG.{lang}.md').write_text('\n'.join(lines), encoding='utf-8')
        readme = ROOT / ('README.md' if zh else 'README.en.md')
        text = replace_block(readme.read_text(encoding='utf-8'), 'catalog-summary', summary)
        text = replace_block(text, 'catalog-categories', '\n'.join(table))
        readme.write_text(text, encoding='utf-8')
    print(f'Generated both catalogs, README statistics and {len(categories)} category rows from {len(products)} products.')


if __name__ == '__main__':
    main()
