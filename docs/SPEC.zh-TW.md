# 開源省錢管家 — v0.1.0-alpha Spec

[English](SPEC.en.md) · [首頁](../README.md)

## 1. 產品目標

從指定軟體、工作需求或安裝清單找到現成的開源與免費替代方案。繁中優先、英文第二。排序原則：現有／內建功能 → 免費成品 → 條件相近時優先開源 → 中文設定與教學 → 翻譯貢獻 → 整合 → 最後才開發。

第一版是 Agent Skill 加少量本機轉接程式，不建桌面 App、帳號、雲端資料庫或背景服務，不重寫錄影、OCR、語音或文書引擎。無 Python 仍可讀 Markdown 清單並使用 Skill 研究。附帶 CLI 與 Mac 收集器需要 Python 3.10+，不需要 pip 套件；Windows 收集器使用 Windows PowerShell 5.1+。

## 2. 入口與責任

| 入口 | 輸入 | 輸出 |
|---|---|---|
| 指定軟體 | Screen Studio、Snagit、Word 等 | 按必要功能核對的條件式候選 |
| 工作需求 | 螢幕錄影、語音輸入、合併 PDF | 現成工具或內建功能；不先盤點 |
| 安裝盤點 | 收集器 JSON 或手動名稱清單 | 已知產品群組、候選及未配對項 |

Skill 理解自然語言並核對工作需求；CLI 只做明確別名、關鍵字搜尋與靜態候選報告，不是語意搜尋或最終推薦引擎。雲端 Agent 無本機能力時改用手動匯入，不把容器當成使用者電腦。

## 3. 交付架構

| 路徑 | 責任 |
|---|---|
| SKILL.md | 入口、查證、工具路由、判斷與輸出 |
| scripts/saver.py | 離線資料驗證、搜尋、匯入、候選報告 |
| scripts/collect_macos.py | 已知 App 目錄的 Info.plist 最小欄位盤點 |
| scripts/collect-windows.ps1 | HKLM/HKCU 32/64 位元 Uninstall 與目前使用者 Appx |
| data/products.json | 58 個中英文產品候選 |
| data/alternatives.json | 14 組原工具／用途的條件式關係與別名 |
| data/article-sources.json | 11 篇文章書目、日期、摘要與候選名稱 |
| data/discovery.json | 53 個文章發現名稱及其來源／catalog ID |
| docs/CATALOG.*.md | 可搜尋與分享的雙語清單 |
| docs/SOURCES.md | 文章與上游出處 |
| tests/ | 資料、配對、隱私輸出與固定測資驗證 |

58 與 53 有重疊，不能相加。文章發現、官方初篩與工作流實測分開；初版所有產品 runtime_tested=false。名單數是快照，不是擴充上限。

## 4. 收集器與資料最小化

Envelope 欄位：schema_version、platform、collector、collected_at、coverage、warnings、applications。App 欄位：name、version，以及來源可提供的 publisher、bundle_id、package_id、collector。禁止加入序號、使用者名稱、安裝路徑、卸載命令、付款與瀏覽紀錄。

Mac 僅檢查 /Applications、~/Applications、/System/Applications，最多兩層子目錄；遇 .app 只讀 Info.plist，不進包內遞迴，不追蹤 symlink。依 bundle ID（或名稱）與版本去重，失敗留下不含路徑的警告。本版採已知目錄取代先前 system_profiler 全盤點草案，以縮小範圍與資訊量。

Windows 無管理員提升，只讀 HKLM/HKCU 的 Registry32/Registry64，再讀目前使用者 Appx、略過 framework/resource package。不呼叫 Win32_Product、不跑卸載、不列其他使用者 Appx、不觸發 WinGet 來源更新。部分來源失敗時仍保存可讀項與警告。

兩者都不保證涵蓋免安裝程式、全部使用者、瀏覽器外掛及所有系統元件。零項目不代表未安裝軟體。Homebrew、WinGet、osquery 僅作已有環境的人工補充；不強制安裝，也不宣稱 CLI 支援其原始匯出格式。

## 5. CLI 合約

| 命令 | 參數 | 結果 |
|---|---|---|
| validate | 無 | 驗證 ID、欄位、關係、來源 URL、日期與別名衝突 |
| search QUERY | --platform、--lang、--json、--include-engines 可選 | 候選列表，無匹配時明示 |
| report | --input、--output、--platform 必填；--lang 可選 | 本機 Markdown 報告，不印原始名稱 |
| collect_macos.py | --output 必填 | 本機 macOS JSON |
| collect-windows.ps1 | -OutputPath 必填 | 本機 Windows JSON |

search 平台為 macos/windows/linux/web/android/ios；report 僅三種桌面系統。未知平台者不通過指定平台篩選。引擎預設排除，明確 include-engines 才列入搜尋。排序依已知關係、精確名稱／分類關鍵字、子字串，不代表品質分數。

輸入接受 UTF-8 或 UTF-8 BOM：字串陣列、含 name/display_name 的物件陣列、applications envelope，或文字檔一行一個名稱。上限 10 MB、單一名稱 300 字元。無效 schema 回報錯誤，不假裝空清單。名稱用 Unicode NFKC、大小寫、空白正規化；僅明確允許的 Adobe 名稱接受年份尾碼，不任意刪除所有數字。未知保留；多版本只合併報告產品群，不推斷訂閱份數。

輸出檔存在則拒絕覆寫；需要時建立父資料夾；POSIX 設 0600，Windows 沿用目標目錄 ACL。成功只印狀態，錯誤不印私人名稱、路徑或原始輸入。Python exit 0 成功、2 輸入／環境錯誤；PowerShell 使用終止錯誤。所有附帶程式不發網路請求。

## 6. 產品資料合約

每產品：id、name、category、keywords、platforms、delivery、url、sources、cost、license、evidence、checked_on、runtime_tested、zh_tw、zh/en.use、zh/en.limits。交付型態 desktop/builtin/extension/setup/engine。分類涵蓋錄影、截圖 OCR、聽寫、轉錄、字幕、朗讀配音、剪輯、音訊、圖像、Office、PDF。

license 是上游摘要，不能當成本專案授權，也不能推導模型、官方成品或服務免費。official-docs-reviewed 表示已讀官方文件；official-docs-partial 只代表部分產品定位／免費範圍核對；discovery 只是文章線索。未知的繁中、商用、費用、平台與功能不可自行補成已驗證。

MIT 只涵蓋本專案自製程式、文件及整理內容。第三方文章只保留連結、書目、名稱及自寫短摘要，不複製全文或未釐清授權的資料包。第三方產品、模型、圖像、商標與服務仍適用各自條款。

## 7. 推薦與台灣情境

先篩平台、必要功能、交付格式與部署負擔，再比較免費範圍、中文、學習與維護成本。免費非開源可以成為首選；試用版或商業用途需付費的版本不能當永久免費。無工程背景者優先成品，願意配置時才提模型／自架。

分開記錄繁中文件、繁中 UI、中文字型／格式與台灣語音品質；缺翻譯先找上游資源和教學。提出翻譯建議不等於自動發送 issue、PR 或訊息。

Agent 標示建議試用／有條件替換／暫不建議及未知項。CLI 只輸出候選，不能自動判定遷移成功。完整 After Effects、Office 巨集、客戶指定專案格式不能靠名稱對映承諾。

## 8. 費用與隱私

使用者提供實付費用後，才計算未來 12 個月可避免支出 − 新方案持續費 − 一次性現金轉換費。套裝只算一次；已預繳不退款不能算可收回；時間成本另外列。CLI 不讀帳單也不計算節省。

一般 Agent 可能把輸入送至雲端。嚴格離線要求直接在目標電腦執行收集與報告，不將私人檔案讀入雲端對話。網路查證與離線模式分開。Skill 不自動安裝、卸載、取消訂閱、改預設程式或移轉專案。

公開 GitHub 禁止包含真實 inventory、私人報告、憑證、個人路徑或未公開工作內容。範例使用明示的虛構資料。gitignore 不能取代提交內容檢查。

## 9. 驗收與發布門檻

| 驗收 | 可觀察結果 |
|---|---|
| 版本與別名 | 已知 Adobe 年份可配對，相似陌生產品不合併 |
| 平台與部署 | Windows-only 不進 Mac；引擎預設隱藏 |
| 匯入 | 中文、BOM、重複、錯誤 schema、空清單正確處理 |
| 未知 | 保留未配對，不推論付費／開源 |
| 私人輸出 | 報告寫檔，stdout/stderr 不含原始名稱與路徑 |
| 非破壞 | 不覆寫舊檔，錯平台不掃描 |
| Mac 測資 | metadata、版本、深度、警告與 symlink 正確 |
| Windows | 另需目標系統語法與 HKLM/HKCU/Appx/Unicode 實測 |
| 文件 | 中英文命令、安裝與限制一致 |

v0.1.0-alpha 可公開分享研究、查詢與手動匯入；收集器明標實驗性。stable 需要 Mac／Windows 真機、一般權限、離線網路觀察、端到端報告及 Agent 宿主安裝驗收。公開 alpha 不等於達成 stable 門檻。

## 10. 執行順序與完成定義

1. 完成 Spec、Skill、本機工具、資料與雙語說明。
2. 執行資料、行為與情境測試，修正可重現問題。
3. 發布公開 alpha 與可下載內容，保留未實測限制。
4. 依社群回報與需求補缺，完成兩平台實測後才提升穩定版。

候選更新先利用文章及既有目錄，先比較少數合適工具，再為必要缺口做一次定向搜尋，不無限擴張。推薦當下核對免費限制與下載；平台／授權超過 30 天或版本變動時複查。沒有自動排程。來源不可讀時標快照日期及未知。

成功指標是使用者知道可試哪款、可承接哪個用途、缺口與下載入口；下載、試用、遷移、停止續費分開記錄。另做網站、瀏覽器外掛及工具翻譯不屬於這次 alpha 的必要交付。
