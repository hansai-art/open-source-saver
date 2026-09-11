# 實作與驗收狀態 / Implementation status

Version: v0.1.0-alpha · Status checked: 2026-09-11 · Product snapshot: 2026-09-10

| 項目 / Item | 狀態 / Status |
|---|---|
| Spec、Skill、繁中／英文說明 / Specification, Skill and bilingual docs | 完成 / Complete |
| 產品資料 / Product snapshot | 58 個候選，14 組條件對照 / 58 candidates, 14 conditional mappings |
| 既有文章 / Existing articles | 11 篇來源，53 個發現名稱，與候選重疊 / 11 sources, 53 overlapping discovery names |
| 離線搜尋、手動匯入與報告 / Offline search, manual import and reports | 已實作並以虛構資料驗證 / Implemented, tested with synthetic data |
| 自動測試 / Automated tests | Linux / Python：12 項通過 / 12 passed |
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

## v0.2 規劃更新 / Planning update

[繁中優化規格](OPTIMIZATION.zh-TW.md) · [English optimization specification](OPTIMIZATION.en.md)

已完成 O01：雙語規格、首頁入口與兩款 GitHub 提報模板。O02–O05 尚待實作；O06 已完成 alpha 原始碼公開，v0.2 發布仍待驗收。200／80／40 是下一版目標；現有產品與對照數量沒有增加。

O01 is complete: bilingual specification, README links and two GitHub issue templates. O02–O05 remain pending; O06 has published the alpha source, while the v0.2 release still requires its acceptance gates. The 200/80/40 counts are future targets; the current dataset has not expanded. The alpha source is public on GitHub.
