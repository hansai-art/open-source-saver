# 實作與驗收狀態 / Implementation status

Version: v0.1.0-alpha · Status checked: 2026-10-13 · Dataset updated: 2026-10-13; individual product evidence dates retained

| 項目 / Item | 狀態 / Status |
|---|---|
| Spec、Skill、繁中／英文說明 / Specification, Skill and bilingual docs | 完成 / Complete |
| 產品資料 / Product snapshot | 204 個候選、54 大類、102 組條件對照 / 204 candidates, 54 categories, 102 conditional mappings |
| 文章、目錄與社群 / Research sources | 48 筆、7 語系，含錄影／下載與先前 ArtCraft 官方文件；保留舊 11 篇文章及 7 筆社群紀錄 / 48 sources across 7 language labels, including recording/download and earlier ArtCraft official documents; legacy research retained |
| 廣域索引 / Broad discovery | 1,346 個去重上游項目、84 個上游分類；全部未逐項查核 / 1,346 unique upstream leads, 84 tags; individually unreviewed |
| 離線搜尋、手動匯入與報告 / Offline search, manual import and reports | 已實作並以虛構資料驗證 / Implemented, tested with synthetic data |
| 自動測試 / Automated tests | Linux / Python：22 項通過 / 22 passed |
| Skill 結構驗證 / Skill structure validation | 通過 / Passed |
| Agent 情境 / Agent scenario | Mac 錄影後製與 IDM 替代：獨立 Agent 使用離線快照，保留費用、繁中、beta 與待開發整合條件 / Independent offline scenario retained cost, locale, beta and proposed-integration conditions |
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

## 2026-10-09 ArtCraft 收錄與採用建議

- 新增七款獨立開源工具、100 組原軟體對照中的 Creative Cloud／ArtCraft 分流。各款保留版本、安裝資產列表、繁中 UI 來源與 CLI／MCP 文件證據。
- 四款版本含繁中 UI，三款未提供繁中。LightCraft 字形限制、FilmCraft HEVC 文件差異與 DesignCraft PDF 文件差異逐款列明。
- 搜尋和報告顯示採用建議與下載入口；`--exclude-experimental` 可隱藏早期開發項。EffectCraft 為研究用途，不能開啟 AEP／AEPX 或使用 AE 外掛。
- 資料與 21 項離線測試通過。第三方安裝包、GUI、檔案遷移、中文品質及 CLI／MCP 工作流未實測。

[繁中查核](research/artcraft.md) · [English review](research/artcraft.en.md)

## 2026-10-10 錄影自動化、繁中與下載器研究 / Recording and download research

- 新增 OpenScreen、Flowtake、OpenCC、Varia、Gopeed，更新 Recordly 與 Auto-Editor；工具合計 202 個、54 大類、101 組條件對照。 / Added five tools and refreshed two; 202 products, 54 categories, 101 conditional mappings.
- 區分點擊縮放、文字剪輯、靜音規則、語意剪輯及 API 費用；記錄匯入 MP4 的游標資料缺口與 proposed integration，未宣稱已實作。 / Separate zoom, transcript cuts, silence rules, semantic editing and API costs; proposed integrations are not existing features.
- 下載器保留正式／beta、平台成熟度及外掛相容版本；不套用作者宣稱的加速倍數。修正 IDM 精確對照混入 IDML 排版工具的搜尋問題。 / Retain stable/beta and plugin/platform conditions; no unmeasured speed claims.
- Varia 已有繁中，194 條目為 125 已譯、26 fuzzy、43 未譯；POT 落後源碼，未測全介面。遵守上游規則，未送出 AI 翻譯或 PR。 / Varia has an incomplete existing locale and a stale POT; no AI translation or upstream PR was submitted.
- 22 項既有／回歸測試及獨立 Agent 離線情境通過。官方文件、源碼與版本資產列表已查核；所有第三方安裝、字幕品質與實際下載速度仍未實測。 / Docs, source and relevant asset lists reviewed; third-party installs, caption quality and speed remain untested.

[繁中研究與驗收](research/recording-downloads.md) · [English review](research/recording-downloads.en.md)

## 2026-10-13 Office、截圖與社群評價更新 / Office, screenshots and community feedback

- ONLYOFFICE 列為 Word、Excel、PowerPoint 首選；新增 Collabora Office 作為 LibreOffice 技術線的另一個候選。ONLYOFFICE 官方語言表列出 zh-TW，但 Editors 翻譯仍不完整，未宣稱實檔相容性已通過。 / ONLYOFFICE is now first for Word, Excel and PowerPoint; Collabora Office was added as another LibreOffice-based candidate. ONLYOFFICE officially lists zh-TW, but Editors translation coverage remains incomplete and real-file compatibility is untested.
- macshot 列為 Mac 截圖首選，依使用者回饋記錄，未在本專案重現測試；Windows 截圖首選仍為 ShareX。 / macshot is now the Mac screenshot first choice based on user feedback, not reproduced runtime testing in this project; ShareX remains first for Windows screenshots.
- 除了新增工具，也接受實際使用評價、相容性紀錄與可重現問題；推薦優先順序會依可追溯社群意見調整，並保留證據日期與未驗證限制。 / Real-world evaluations, compatibility notes and reproducible problems are welcome; recommendation priority may change based on traceable community feedback while evidence dates and unverified limitations remain visible.
- 本次資料重建：203 個工具、54 大類、101 組條件對照；未執行第三方 Office 檔案遷移或 macshot 真機測試。 / Rebuilt snapshot: 203 products, 54 categories and 101 conditional mappings; no third-party Office migration or macshot device test was run.

## 2026-10-13 Obsidian 與 Notion 對照更新 / Obsidian and Notion mapping

- 新增 Obsidian，列為 Notion 個人筆記／知識管理的免費首選；因 Obsidian 本體不是開源，資料分類為非開源免費候選，開源授權需求則保留 Joplin。 / Added Obsidian as the free first choice for Notion personal notes and knowledge management; Obsidian is proprietary, so it is classified as a free non-open-source candidate, while Joplin remains the open-source option.
- 官方定價頁列出本體免費使用，Sync／Publish 等為選購服務；官方提供中文說明與翻譯貢獻入口，但繁體中文介面完整度尚未確認。 / The official pricing page says the app is free to use, with Sync/Publish as optional services; official Chinese help and translation contribution paths exist, but Traditional Chinese UI coverage is unconfirmed.
- 本次資料重建：204 個工具、54 大類、102 組條件對照；未執行 Obsidian 匯入、外掛、同步或 Notion 資料遷移實測。 / Rebuilt snapshot: 204 products, 54 categories and 102 conditional mappings; Obsidian import, plugin, sync and Notion migration were not runtime-tested.

## 2026-10-13 Proton Pass 密碼管理推薦 / Proton Pass password-manager recommendation

- 依使用者推薦新增 Proton Pass，列為 1Password／LastPass 對照的第一候選；KeePassXC 保留為另一個本機開源方向。 / Added Proton Pass from user recommendation as the first candidate for 1Password/LastPass mappings; KeePassXC remains as another local open-source direction.
- 官方資料確認 Proton Pass 有可用免費方案、跨裝置應用與開源資訊；帳號匯入、同步、復原與繁中介面仍未實測。 / Official sources document a usable free plan, cross-device apps and open-source information; account import, sync, recovery and Traditional Chinese UI remain untested.
- 本次資料重建：206 個工具、54 大類、102 組條件對照。 / Rebuilt snapshot: 206 products, 54 categories and 102 conditional mappings.

## 2026-10-13 首頁節費案例改為桌面軟體 / Homepage savings basket focused on desktop software

- Adobe 家族在首頁節費案例只保留 Photoshop 一筆，並移除 Acrobat 的重複計算；依使用者意見，Slack、Dropbox、Figma、Otter 等以網路服務為主的工具也不放入這組桌面軟體案例。 / The homepage savings basket now counts the Adobe family once through Photoshop and removes Acrobat from the duplicate calculation; following user feedback, primarily network-based tools such as Slack, Dropbox, Figma and Otter are also excluded from this desktop-software basket.
- 以 PDF Expert、CleanMyMac、Sublime Text 與 Avast Premium Security 對 ClamAV 補回不同桌面工具類別，十筆示例改為 US$989.13，首頁四捨五入顯示約 US$989／年；這仍是公開價格基準，不是個人實際帳單或保證節省。 / PDF Expert, CleanMyMac, Sublime Text and Avast Premium Security versus ClamAV restore distinct desktop-software categories; the ten-example total is now US$989.13, rounded on the homepage to about US$989/year. This remains an illustrative public-price benchmark, not a personal invoice or guaranteed savings.
