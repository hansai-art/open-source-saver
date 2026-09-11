# 開源省錢管家 Open Source Saver

![開源省錢管家產品主視覺](assets/hero-geometric.png)

**先看你的電腦裝了什麼，再推薦適合你的開源免費替代工具，附上下載與安裝方式。**

<!-- catalog-summary:start -->
**78 個候選 · 18 大類 · 69 個開源專案 · 8 個非開源免費版／內建候選 · 1 個原始碼可見候選**
<!-- catalog-summary:end -->

**先從一筆錄影訂閱開始：成功替換並停止續訂後，每年可少付 US$108 或 US$179.88。** 這是下方兩個方案的授權費範例，依你原本訂閱哪個方案擇一計算，不是每位使用者的保證節省。

[直接看完整工具清單](docs/CATALOG.zh-TW.md) · [English](README.en.md) · [價格與計算方式](docs/SAVINGS.md) · [國外論壇整理](docs/FORUMS.md) · [提供工具](https://github.com/hansai-art/open-source-saver/issues/new?template=software.md)

這個 Skill 的主要流程是：**盤點電腦已安裝的軟體 → 比對開源免費替代方案 → 列出推薦理由、功能差異與安裝方式。** 安裝到能操作本機的 Claude Code／Codex 等 Agent 後，從你的實際軟體清單開始推薦，不用先自己研究每一款替代品。也能直接瀏覽網頁清單，或只詢問某款軟體。**有現成就拿來用；只有英文，就先整理繁中教學或協助上游翻譯。**

導覽：[能省多少](#先看一筆訂閱能省多少) · [優先需求](#先解決你每天會用的錄影截圖與語音需求) · [全部分類](#目前收錄哪些工具) · [資料來源](#資料從哪裡來) · [提供工具](#歡迎提供你自己開發或你知道的工具) · [新手開始](#新手從這裡開始) · [安裝](#安裝-skill)

## 先看一筆訂閱能省多少

公開個人方案價格，查核日 **2026-09-11**。以美金原價比較，不含地區稅費、促銷或信用卡換匯。

| 原本付費工具／方案 | 官方標示價格 | 免費起手方案與用途 | 成功替換、停止該筆續訂後，每年少付 | 必須先確認的落差 |
|---|---|---|---:|---|
| Camtasia（常被搜尋為 Camtasia Studio）Essentials 年繳 | US$179.88／年 | OBS Studio 錄影 + Kdenlive 基本剪輯 | **US$179.88** | 先測字幕、模板與課程交付；需要整套 Camtasia 流程時，不能只看錄影功能 |
| Screen Studio 年繳 | US$9／月，全年一次繳 US$108 | OBS Studio 錄影 + Kdenlive 後製 | **US$108** | 適合只需錄影與基本剪輯；不是相同的自動縮放、游標美化與分享體驗 |
| Screen Studio 月繳，連續使用 12 個月 | US$29／月 | 同上，先用真實影片試換 | **US$348** | 與年繳是不同情境，兩列不能相加；只用幾個月就按實際月數算 |

價格來源：[TechSmith 官方商店](https://www.techsmith.com/store/camtasia)、[Screen Studio 官方價格](https://screen.studio/)。免費候選來源：[OBS Studio](https://obsproject.com/)、[Kdenlive](https://kdenlive.org/)。

如果你重視 Screen Studio 的一鍵運鏡，請先看 [錄影清單](docs/CATALOG.zh-TW.md#screen-recording) 裡的 Recordly、Capptivo 等候選，再逐項確認免費安裝、字幕、輸出與系統限制。找到名字不表示已經能完成你的工作。

節費公式：**可取消的原訂閱費 − 替代方案新增必要費用**。轉換與學習時間另列。已買斷舊版、原本用免費版、仍需續訂套裝中的其他功能，都不能直接套用上述節省金額。現在還不把全站工具價格加成一個「人人都能省」的總額。[完整計算規則與資料](docs/SAVINGS.md)

## 先解決你每天會用的錄影、截圖與語音需求

| 你想做的事／原工具 | 先看的候選 | 選之前先試什麼 |
|---|---|---|
| 錄課程、螢幕教學／Camtasia | OBS Studio + Kdenlive | 錄一段含麥克風與系統音訊的教學，再完成剪輯輸出 |
| 漂亮的產品示範／Screen Studio | Recordly、Capptivo；基本錄影可看 OBS | 自動縮放、游標、字幕、輸出浮水印及安裝方式 |
| 截圖標註、OCR／Snagit、CleanShot X | Windows：ShareX；Mac：macshot；跨平台：Flameshot、ksnip | 用自己的畫面試長截圖、繁中 OCR、快捷鍵與分享需求 |
| 用說話代替打字／Wispr Flow、Superwhisper | Handy、OpenWhispr、TypeWhisper（Mac） | 一段台灣口音、中英混合與專有名詞；本機模型或雲端費用 |
| 訪談逐字稿／Otter、Descript | noScribe、Vibe、Buzz；會議摘要另看 Meetily Community | 說話者分段、轉錄時間、字幕匯出；不能把轉錄當成文字剪輯 |
| 做字幕、配音與音訊整理 | Subtitle Edit、Audacity；TTS 另看專區 | 字幕時間軸、聲音模型授權；TTS 引擎可能需要設定 |
| 合併、分割 PDF／Acrobat 的部分用途 | PDFsam Basic；Windows 可看 PDF24 Creator | 拆合頁面與正文編輯是兩件事；SumatraPDF 主要是閱讀器 |

以上是**優先查看的候選，不是已由本專案實測的排行榜**。每款的官方入口、平台、免費範圍、用途與限制都在 [完整清單](docs/CATALOG.zh-TW.md)。

## 目前收錄哪些工具

<!-- catalog-categories:start -->
| 分類 | 數量 | 例子 |
|---|---:|---|
| [螢幕錄影](docs/CATALOG.zh-TW.md#screen-recording) | 12 | OBS Studio、Recordly、Capptivo |
| [截圖與 OCR](docs/CATALOG.zh-TW.md#screenshots-ocr) | 8 | ShareX、Flameshot、ksnip |
| [語音輸入／聽寫](docs/CATALOG.zh-TW.md#dictation) | 6 | Handy、OpenWhispr、VoiceInk |
| [逐字稿與會議轉錄](docs/CATALOG.zh-TW.md#transcription) | 10 | Vibe、Buzz、aTrain |
| [字幕與翻譯](docs/CATALOG.zh-TW.md#subtitles) | 3 | Subtitle Edit、pyVideoTrans、VideoLingo |
| [TTS 文字轉語音](docs/CATALOG.zh-TW.md#text-to-speech) | 7 | Readest、Piper（現行維護線）、Qwen3-TTS |
| [影片剪輯、合成與轉檔](docs/CATALOG.zh-TW.md#video-editing) | 9 | Auto-Editor、LosslessCut、Kdenlive |
| [音訊編輯](docs/CATALOG.zh-TW.md#audio-editing) | 2 | Audacity、Ultimate Vocal Remover（UVR） |
| [修圖與繪圖](docs/CATALOG.zh-TW.md#graphics) | 2 | GIMP、Krita |
| [文書與 Office](docs/CATALOG.zh-TW.md#office) | 2 | LibreOffice、ONLYOFFICE Desktop Editors |
| [PDF 閱讀與處理](docs/CATALOG.zh-TW.md#pdf) | 3 | PDF24 Creator、SumatraPDF、PDFsam Basic |
| [傳檔與檔案同步](docs/CATALOG.zh-TW.md#file-transfer) | 2 | LocalSend、Syncthing |
| [視窗、剪貼簿與系統整理](docs/CATALOG.zh-TW.md#productivity) | 3 | Rectangle、Maccy、Pearcleaner |
| [壓縮與解壓縮](docs/CATALOG.zh-TW.md#archives) | 2 | 7-Zip、PeaZip |
| [影音播放](docs/CATALOG.zh-TW.md#media-players) | 3 | VLC media player、IINA、FreeTube |
| [電子郵件](docs/CATALOG.zh-TW.md#email) | 1 | Thunderbird |
| [密碼管理](docs/CATALOG.zh-TW.md#passwords) | 1 | KeePassXC |
| [筆記與電子書](docs/CATALOG.zh-TW.md#notes-reading) | 2 | Joplin、calibre |
<!-- catalog-categories:end -->

**數字怎麼算？** 以 `data/products.json` 的不重複產品 ID 計數，每個產品只列一個主要分類。文章提到的名稱、論壇留言、同一工具的不同平台不重複加總。開源專案包括部分引擎、需設定的工具，以及可能另售官方安裝包的產品；**開源數量不等於免費免設定下載數量**。Pearcleaner 附 Commons Clause 且維護暫停，歸為原始碼可見，不算入開源數。免費非開源也會註明免費版與功能限制。

繁中介面、中文內容、台灣口音準確度分開看；有中文版文件不代表三者都通過。目前第三方工作流與繁中品質仍未完成實測。[統計資料](data/catalog-stats.json) · [驗收狀態](docs/STATUS.md)

## 資料從哪裡來

先讀國外已經做過的整理，再核對官網，最後才讓使用者以自己的任務試用：

1. **既有文章：** [11 篇文章來源](docs/SOURCES.md)，包括 It's FOSS、TechRadar、Lifewire，涵蓋 Adobe、錄影、截圖、聽寫、Office、PDF。另有 53 個文章發現名稱，與正式候選重疊，不能相加。
2. **社群經驗：** [7 筆 Reddit／Hacker News 討論與留言](docs/FORUMS.md)，逐筆區分作者自薦、使用者經驗及回查結果。論壇能找到小專案與實際抱怨，但不把留言當成授權或效能證明。
3. **開源目錄：** [上游清單](docs/SOURCES.md) 提供後續擴充入口；本專案不整包複製未釐清授權的資料庫。
4. **官方證據：** 每個產品保留 [來源與個別查核日](data/products.json)。本次也直接從官方來源補齊傳檔、壓縮、郵件、密碼等缺少的類別；並非所有新增工具都來自論壇。

例如論壇推薦 Longshot 時，留言指出部分免費輸出帶浮水印；Voquill 舊貼文與目前官網定位的關係仍待確認。這些放在待查紀錄，沒有拿來灌大工具數。[查看論壇摘要與收錄決定](docs/FORUMS.md)

## 歡迎提供你自己開發，或你知道的工具

**自己做的專案、每天在用的工具、國外論壇挖到的好東西，都歡迎。** 開源優先，也接受能直接使用的免費非開源軟體與內建功能。只有英文也沒關係，我們可以先補繁中說明，或整理給上游的翻譯提案。

不會寫程式也能參與：按 [提供工具](https://github.com/hansai-art/open-source-saver/issues/new?template=software.md)，填「工具名稱 + 官方連結 + 可以完成什麼工作」。知道的話再補原付費工具、平台、免費限制與中文支援；未知就寫未知。**你是作者或有合作關係也歡迎，請直接註明。**

發現失效連結、價格改了、免費版限制或踩雷經驗？[回報修正](https://github.com/hansai-art/open-source-saver/issues/new?template=correction.md)。想直接改資料可看 [貢獻指南](CONTRIBUTING.md)。

## 新手從這裡開始

1. **安裝 Skill，請 AI 盤點電腦：** 在能操作你電腦的 Agent 中使用下方指令，由 Skill 讀取已安裝軟體清單。Mac／Windows 收集器目前為實驗性，可能漏掉免安裝程式、外掛或特殊安裝位置。
2. **查看對應推薦：** 依清單列出「目前軟體 → 建議替代工具」，說明開源或免費範圍、能取代哪些用途，以及缺少哪些功能；找不到合適替代的也會保留。
3. **取得下載與安裝方式：** 優先推薦符合你系統、可直接使用的開源免費工具，附官方連結與必要步驟。免費非開源工具會另外標明。
4. **挑選工具試用：** 用真實文件或短影片確認功能與輸出；需要 AI 協助安裝時，直接指定工具。推薦本身不會自動安裝、移除原軟體或取消訂閱。

**雲端版 ChatGPT 無法直接掃描你的個人電腦。** 在雲端使用時，Skill 會引導你在目標電腦產生清單，或使用你提供的軟體名稱，再做比對。Linux 與其他裝置先採手動清單或宿主可用的唯讀盤點方式。[盤點操作教學](docs/USAGE.zh-TW.md)

只想找一款軟體的替代品，也可以直接問，不必盤點整台電腦。安裝清單不能證明你正在付費；節費金額需以實際訂閱確認。

## 安裝 Skill

取得整個專案資料夾，包含 SKILL.md、scripts、references、data；不要只複製 SKILL.md。

Claude Code 個人安裝（macOS／Linux，已安裝 Git）：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/hansai-art/open-source-saver.git ~/.claude/skills/open-source-saver
```

在 Claude Code 輸入：

```text
/open-source-saver 先盤點這台電腦已安裝的軟體，推薦適合的開源免費替代工具，列出功能差異、官方下載連結與安裝方式。
```

Codex／其他 Agent：將完整資料夾交給宿主的 Skill 安裝功能，或請 Agent 依該宿主規範安裝此 GitHub 專案；不要假設 Claude 的路徑通用。ChatGPT 雲端安裝 Skill 不等於能掃描你的電腦。[Claude 官方 Skill 說明](https://code.claude.com/docs/en/skills)

沒有 Git：GitHub 頁面 **Code → Download ZIP**，解壓縮後依上述宿主規範放置。目標資料夾已有內容時先檢查，不直接覆寫。

## 不用 AI，也能離線搜尋

需已有 Python 3.10+；在專案資料夾執行：

```bash
python3 scripts/saver.py search "錄影" --platform macos
python3 scripts/saver.py search "Snagit" --platform windows
python3 scripts/saver.py search "dictation" --platform macos --lang en
```

Windows 將 python3 改成 `py -3`。`--include-engines` 可顯示引擎；自然語言需求由 Agent 理解，CLI 請用產品名稱或分類關鍵字。[完整盤點與報告指令](docs/USAGE.zh-TW.md)


## 隱私、授權與目前進度

附帶程式不連網，清單與報告寫到本機；若將內容交給雲端 AI，仍會發生雲端處理。嚴格離線時請直接使用本機 CLI。收集器為實驗性，Windows／Mac 真機驗收仍待完成；可先提供手動工具名稱清單。

本次資料集更新於 **2026-09-11**；各工具保留原查核日，未把未重查的舊項目標成今日查核。不自動安裝、卸載、取消訂閱；不從安裝清單猜帳單。

[Spec](docs/SPEC.zh-TW.md) · [v0.2 優化規劃](docs/OPTIMIZATION.zh-TW.md) · [驗收狀態](docs/STATUS.md)。v0.1.0-alpha 持續擴充中；後續規劃的數量目標不當成已完成。

[MIT License](LICENSE) 適用本專案自製內容；第三方軟體、模型與文章依原條款，見 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。作者：Hans 林思翰。

搜尋關鍵字：開源替代、免費軟體、付費軟體替代、Camtasia Studio 免費替代、Screen Studio 替代、Snagit、CleanShot X、語音輸入、逐字稿、繁體中文、台灣、open source alternatives、free software、Claude Code skill、Codex skill。
