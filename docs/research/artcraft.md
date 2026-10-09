# ArtCraft 七款 Adobe 開源替代工具查核

[繁體中文](artcraft.md) · [English](artcraft.en.md)

查核日期：2026-10-09。建議先試 PhotoCraft、VectorCraft、PdfCraft 的小型檔案操作，EffectCraft 先保留研究用途。

ArtCraft Crafting Apps 是七款第三方獨立軟體，程式碼採 MIT 或 Apache-2.0。Adobe 官方原始碼、其他 Creative Cloud 產品，以及 ArtCraft AI 影像／影片服務不在這七款的收錄範圍。套裝費用依可取消的那筆帳單計算。

## 版本、下載與中文介面

七款 release 資產列表均有 Mac universal DMG、Windows 安裝包、Linux 套件與另外提供的 WebAssembly 壓縮檔。網頁壓縮檔需自行部署，下載位置依下表固定版本。

| 原軟體 | 工具／版本 | 建議 | 繁中 UI |
|---|---|---|---|
| Photoshop | [PhotoCraft v0.5.0](https://github.com/storytold/photocraft/releases/tag/v0.5.0) | 早期試用 | 版本含繁中，品質未實測 |
| Illustrator | [VectorCraft v0.7.0](https://github.com/storytold/vectorcraft/releases/tag/v0.7.0) | 早期試用 | 版本含繁中，品質未實測 |
| Premiere Pro | [FilmCraft v0.4.0](https://github.com/storytold/filmcraft/releases/tag/v0.4.0) | 早期試用 | 此版本未提供 |
| Lightroom | [LightCraft v0.4.0](https://github.com/storytold/lightcraft/releases/tag/v0.4.0) | 早期試用 | 版本含繁中，品質未實測 |
| Acrobat | [PdfCraft v0.4.0](https://github.com/storytold/pdfcraft/releases/tag/v0.4.0) | 早期試用 | 版本含繁中，品質未實測 |
| After Effects | [EffectCraft v0.6.0](https://github.com/storytold/effectcraft/releases/tag/v0.6.0) | 研究用途 | 此版本未提供 |
| InDesign | [DesignCraft v0.4.0](https://github.com/storytold/designcraft/releases/tag/v0.4.0) | 早期試用 | 此版本未提供 |

語言狀態以查核版本的 UI 語言定義／翻譯檔為依據。中文可顯示、繁中選單、OCR、正文編輯與台灣字形是不同能力。LightCraft 官方文件特別記錄簡中字形優先與網頁版字形缺口。

## 功能差異與試用任務

### PhotoCraft

早期 alpha。專業字排、生成式功能與 Photoshop 外掛有缺口；官方 PSD 測試集成績是作者自測，客戶 PSD、字型與智慧物件需另驗。已確認版本含繁中 UI，翻譯與字形未實測。

試用任務：開啟含繁中文字、遮色片與智慧物件的 PSD 副本，改字後存回，再用 Photoshop 比對。

來源：[README](https://github.com/storytold/photocraft/blob/v0.5.0/README.md) · [Cargo / license](https://github.com/storytold/photocraft/blob/v0.5.0/Cargo.toml) · [Release](https://github.com/storytold/photocraft/releases/tag/v0.5.0) · [UI language](https://github.com/storytold/photocraft/blob/v0.5.0/crates/ui-egui/src/i18n/mod.rs)

### VectorCraft

持續開發中。AI 匯入限 PDF 相容檔案，3D／材質、CJK 直排組版與部分效果仍有缺口；先試向量新稿。已確認版本含繁中 UI，翻譯與字形未實測。

試用任務：用一份 SVG 與一份 PDF 相容 AI 樣稿測圖層、漸層、中文字型及 PDF 輸出。

來源：[README](https://github.com/storytold/vectorcraft/blob/v0.7.0/README.md) · [Cargo / license](https://github.com/storytold/vectorcraft/blob/v0.7.0/Cargo.toml) · [Release](https://github.com/storytold/vectorcraft/releases/tag/v0.7.0) · [UI language](https://github.com/storytold/vectorcraft/blob/v0.7.0/crates/ui-egui/src/i18n/mod.rs)

### FilmCraft

早期開發。大型素材效能、相機／手機檔案與跨平台測試仍待補足，不支援 VST3／Audio Units／OpenFX 外掛；Premiere 專案遷移未驗證。官方文件對 HEVC 匯出描述有出入，需依作業系統與 GPU 實測。此版本 UI 語言清單沒有繁中。

試用任務：剪一支 30 秒手機素材，加繁中字幕與配樂，確認輸出畫面、音訊與同步。

來源：[README](https://github.com/storytold/filmcraft/blob/v0.4.0/README.md) · [Cargo / license](https://github.com/storytold/filmcraft/blob/v0.4.0/Cargo.toml) · [Release](https://github.com/storytold/filmcraft/releases/tag/v0.4.0) · [UI language](https://github.com/storytold/filmcraft/blob/v0.4.0/crates/ui-egui/src/i18n.rs)

### LightCraft

早期開發。相機色彩校正資料與特定 RAW 格式仍有缺口，既有 Lightroom 編輯歷史遷移未驗證；先測自己的相機檔。已確認繁中 UI，官方註明桌面字型優先採簡中字形，網頁版繁中字形覆蓋未驗。

試用任務：匯入同一台相機的三張 RAW，測白平衡、膚色、亮部與批次 JPEG。

來源：[README](https://github.com/storytold/lightcraft/blob/v0.4.0/README.md) · [Cargo / license](https://github.com/storytold/lightcraft/blob/v0.4.0/Cargo.toml) · [Release](https://github.com/storytold/lightcraft/releases/tag/v0.4.0) · [UI language](https://github.com/storytold/lightcraft/blob/v0.4.0/docs/localization-zh-hant.md)

### PdfCraft

早期開發，原名 PrintCraft。正文編輯尤其 CJK、非拉丁 OCR、Office 轉檔與長期簽章驗證仍有缺口；先測拆合頁面。已確認版本含繁中 UI，中文正文編輯與 OCR 是另外的驗收項。

試用任務：用非機密的繁中 PDF 測合併、分割、註解與列印，正文編輯及 OCR 分開測。

來源：[README](https://github.com/storytold/pdfcraft/blob/v0.4.0/README.md) · [Cargo / license](https://github.com/storytold/pdfcraft/blob/v0.4.0/Cargo.toml) · [Release](https://github.com/storytold/pdfcraft/releases/tag/v0.4.0) · [UI language](https://github.com/storytold/pdfcraft/blob/v0.4.0/crates/ui-egui/src/i18n/mod.rs)

### EffectCraft

官方列為早期工具，暫不建議取代客戶 AE 工作。無法開啟 .aep／.aepx，也不能使用 After Effects 外掛；大量效果存在不等於與 AE 行為一致。此版本 UI 未提供繁中，CLI／MCP 僅核對文件。

試用任務：從零做一段 5 秒標題動畫，測 CLI 渲染、透明背景與音訊，不拿客戶 AE 原檔遷移。

來源：[README](https://github.com/storytold/effectcraft/blob/v0.6.0/README.md) · [Cargo / license](https://github.com/storytold/effectcraft/blob/v0.6.0/Cargo.toml) · [Release](https://github.com/storytold/effectcraft/releases/tag/v0.6.0) · [UI language](https://github.com/storytold/effectcraft/blob/v0.6.0/crates/ui-egui/src/i18n.rs)

### DesignCraft

持續開發中。無法讀取 INDD，完整 InDesign CJK 組版、框格與細部注音仍未完成；需用繁中樣稿校對 IDML、PDF 與印刷規格。此版本有簡中 UI，未提供繁中。README 的 PDF 規劃文字較舊，Roadmap 與 release 已列 PDF 功能。

試用任務：以繁中、圖片與段落樣式排兩頁型錄，測 IDML 與 PDF，再核對斷行、出血及字型。

來源：[README](https://github.com/storytold/designcraft/blob/v0.4.0/README.md) · [Cargo / license](https://github.com/storytold/designcraft/blob/v0.4.0/Cargo.toml) · [Release](https://github.com/storytold/designcraft/releases/tag/v0.4.0) · [UI language](https://github.com/storytold/designcraft/blob/v0.4.0/crates/ui-egui/src/i18n.rs) · [Roadmap](https://github.com/storytold/designcraft/blob/v0.4.0/ROADMAP.md)

## 自動化與查核範圍

七款官方文件均描述 CLI、MCP 與 JSON 控制通道。適合從小檔案建立背景處理測試，資料保留 `automation.runtime_tested: false`。

本次已讀版本文件、授權、下載資產列表與語言定義，並驗證開源省錢管家的搜尋及報告。第三方軟體安裝、GUI、效能、遷移及 MCP 流程尚未實測，作者的相容率與測試數字保留作者自測身分。

[工具資料](../../data/products.json) · [採用建議與操作](../USAGE.zh-TW.md)
