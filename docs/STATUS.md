# 實作與驗收狀態 / Implementation status

Version: v0.1.0-alpha · Status checked: 2026-09-12 · Dataset updated: 2026-09-12; individual product evidence dates retained

| 項目 / Item | 狀態 / Status |
|---|---|
| Spec、Skill、繁中／英文說明 / Specification, Skill and bilingual docs | 完成 / Complete |
| 產品資料 / Product snapshot | 189 個候選、53 大類、99 組條件對照 / 189 candidates, 53 categories, 99 conditional mappings |
| 文章、目錄與社群 / Research sources | 新增 38 筆、7 語系；保留舊 11 篇文章及 7 筆社群紀錄 / 38 new sources across 7 language labels; legacy research retained |
| 廣域索引 / Broad discovery | 1,346 個去重上游項目、84 個上游分類；全部未逐項查核 / 1,346 unique upstream leads, 84 tags; individually unreviewed |
| 離線搜尋、手動匯入與報告 / Offline search, manual import and reports | 已實作並以虛構資料驗證 / Implemented, tested with synthetic data |
| 自動測試 / Automated tests | Linux / Python：16 項通過 / 16 passed |
| Skill 結構驗證 / Skill structure validation | 通過 / Passed |
| Agent 情境 / Agent scenario | Mac 錄影、自動縮放、繁中字幕、免編譯：正確保留未知，不承諾完整替換 / Preserved unknowns instead of promising an unverified replacement |
| macOS 收集器 / macOS collector | metadata 測資通過；真機未測 / Synthetic metadata tests passed; device testing pending |
| Windows 收集器 / Windows collector | 已實作；原生 PowerShell 語法與真機未測 / Implemented; native PowerShell parsing and device tests pending |
| 第三方工具工作流 / Third-party workflows | 全部尚未實測 / None runtime-tested |
| GitHub 公開發布 / Public GitHub publication | v0.1.0-alpha 原始碼公開 / v0.1.0-alpha source published |

## 重現 / Reproduce

From the project folder / 在專案資料夾執行：

```bash
python3 scripts/saver.py validate
python3 -m unittest discover -s tests -v
python3 scripts/build_catalog.py
python3 scripts/build_research.py
```

Tests use temporary synthetic inputs, never real installed-app lists. The passing Mac fixture test does not prove that permissions, native app enumeration or all bundle layouts work on a real Mac. The network guard covers the fixture invocation only; full device-level offline observation remains pending.

測試僅用暫存虛構資料。Mac metadata 測試不代表真機權限、應用程式覆蓋率已通過；測試中的網路防護只涵蓋該次呼叫，尚未完成目標電腦全流程網路觀察。

## 下一階段 / Next steps

1. 公開 alpha：[GitHub 專案](https://github.com/hansai-art/open-source-saver)。後續依下列項目驗收。 / Public alpha available; continue the verification work below.
2. 在一般權限 Windows 與 Mac 驗收收集器；紀錄系統版本、已知漏項、Unicode 和報告結果。 / Test collectors on ordinary-permission Windows and Mac devices.
3. 依真實需求先試錄影、截圖、聽寫與字幕；分開記錄免費安裝、繁中 UI、台灣口音、交付格式。 / Trial priority workflows and record separate free-installation, localization, speech and format evidence.
4. 以既有文章與上游目錄持續補缺；更新相同 JSON，再重建雙語清單。 / Expand from existing articles and upstream catalogs, then regenerate both catalogs from shared JSON.

## 發布設定 / Publication settings

- Repository: `open-source-saver`
- Visibility: Public
- Description: `開源省錢管家｜繁中優先的開源與免費軟體替代指南、盤點工具及 Agent Skill。Open-source and free software alternatives, inventory tools and Agent Skill.`
- Suggested topics: `open-source-alternatives`, `free-software`, `agent-skills`, `claude-code`, `codex`, `traditional-chinese`, `taiwan`, `software-inventory`
- License: MIT for original project content; see THIRD_PARTY_NOTICES.md.

後續更新只提交專案內容；不要提交真實 inventory、私人報告或憑證。GitHub 公開原始碼不代表真機與第三方工作流已通過驗收。

Publish project content only, excluding private inventories, reports and credentials. Public source availability does not imply native-device or third-party workflow validation.

## 先前 v0.2 規劃紀錄 / Earlier planning record

[繁中優化規格](OPTIMIZATION.zh-TW.md) · [English optimization specification](OPTIMIZATION.en.md)

已完成 O01：雙語規格、首頁入口與兩款 GitHub 提報模板。O02–O05 尚待實作；O06 已完成 alpha 原始碼公開，v0.2 發布仍待驗收。200／80／40 是下一版目標；本次首頁與社群研究更新已將候選擴為 78 個、對照擴為 20 組，並非 v0.2 完整驗收。

O01 is complete: bilingual specification, README links and two GitHub issue templates. O02–O05 remain pending; O06 has published the alpha source, while the v0.2 release still requires its acceptance gates. The 200/80/40 counts are future targets; this homepage/community update expanded the dataset to 78 candidates and 20 mappings without claiming full v0.2 acceptance. The alpha source is public on GitHub.

## 首頁與來源擴充 / Homepage and source expansion · 2026-09-11

- 中英文首頁先呈現收錄數、節費範例、18 類索引與優先任務，再介紹安裝。 / Both homepages lead with counts, savings examples, categories and tasks before installation.
- 新增 20 個候選；合計 69 個開源、8 個非開源免費版／內建候選、1 個原始碼可見候選。此分法不代表每個開源專案都附免費安裝包。 / Added 20 candidates; source classification is not a free-binary count.
- 新增 7 筆論壇討論／留言的原創摘要，未確認的線索不計入工具數。 / Added 7 forum source summaries, excluding unresolved leads from product totals.
- 官網價格基準與假設見 [SAVINGS.md](SAVINGS.md)；未測量使用者實際節省。 / Official benchmarks are illustrative, not measured user savings.
- 分類數、來源分類與雙語首頁統計由同一 JSON 自動產生。 / Product JSON generates statistics and both README category tables.

## 2026-09-12 全球領域擴充

- 基準 commit：`e0e4f2162176fcec3a7c1d6100b458baa697d8c1`。工具 78 → 189（2.42 倍）、領域 18 → 53（2.94 倍）、條件對照 20 → 99。
- 新增工具 111 個均閱讀官方資料；舊資料日期不覆蓋。獨立複查 15 個新增產品的官方資料，修正平台與版別授權。
- 新增 38 筆國內外來源：22 正文、9 目錄段落、6 目錄入口、1 僅發現線索。
- 匯入 1,346 筆上游發現項，92 筆保留非自由授權標記，固定來源 commit，CC BY-SA 3.0 單獨保留。固定來源重建檢查通過。
- 離線 `discover` 支援名稱、分類及中英關鍵字；與整理候選搜尋分開。新增資料重複、雙語欄位、平台及搜尋測試，全部 16 項通過。
- 實際第三方安裝、完整遷移、效能、繁中介面與使用者節省仍未實測；Windows／Mac 真機收集器驗收仍待完成。

[研究方法](RESEARCH.md) · [國內外來源](RESEARCH-SOURCES.md) · [機器可讀統計](../data/research-stats.json)
