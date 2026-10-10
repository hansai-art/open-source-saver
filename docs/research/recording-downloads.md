# 錄影後製與下載工具研究指南

查核日期：2026-10-10。此頁是官方文件、版本與原始碼審閱紀錄，尚未在使用者的 Windows、Mac 或 Linux 實機執行驗收。
版本與功能是當日快照。推薦前重新核對下載頁、授權、平台與外掛相容版本。

## 目錄

- [選擇原則](#選擇原則)
- [錄影後製需求對照](#錄影後製需求對照)
- [錄影工具的關鍵界線](#錄影工具的關鍵界線)
- [下載工具](#下載工具)
- [Varia 繁中查核與改善](#varia-繁中查核與改善)
- [五分鐘驗收](#五分鐘驗收)
- [官方來源與排除項目](#官方來源與排除項目)

## 選擇原則

- 需要錄完自動縮放、字幕與後續自行擴充：先試 OpenScreen 現維護線。
- 需要完全本機刪靜音：Auto-Editor 是流程元件，可搭配錄影工具，不當成完整螢幕錄影編輯器。
- 需要穩定繁體字幕：確認辨識、簡繁轉換與字幕輸出三個環節，繁中介面不等於繁體辨識結果。
- 下載工具優先 Varia 的現成功能。Mac 重視原生可用版本時可比較 Gopeed，另核對影片外掛版本。
- 現有產品少一個小功能時先修上游或加處理步驟，避免重新建立同類產品。

## 錄影後製需求對照

| 工具 | 授權／近期版本 | 剪掉多餘內容 | 自動縮放 | 中文字幕／主要缺口 |
| --- | --- | --- | --- | --- |
| [OpenScreen 現維護線](https://github.com/getopenscreen/openscreen) | MIT，v2.0.0，2026-10-03 | Smart cuts 需 LLM，刪逐字稿是互動剪輯 | 依自行錄影取得的游標點擊資料 | 本機 Whisper 中文，未找到固定繁體設定，無 SRT／VTT |
| [Recordly](https://github.com/webadderallorg/Recordly) | AGPL-3.0，另有品牌條款，v1.4.0，2026-09-08 | 已確認手動 timeline 剪輯，未證實語意自動剪輯 | 游標活動建議縮放 | 本機字幕，可輸出 SRT／VTT，固定繁體轉換未確認 |
| [Auto-Editor](https://github.com/WyattBlue/auto-editor) | Unlicense，31.7.2，2026-10-03 | CLI 依音訊門檻刪靜音 | 不是游標追蹤縮放 | 不當成現成繁中字幕工具 |
| [Flowtake](https://github.com/JNX03/Flowtake) | MIT，v1.7.2，2026-09-12 | 已確認 trim／split | 游標驅動 zoom／pan | 已查語言下拉選單無中文，不宣稱現成繁中字幕 |
| [OpenCC](https://github.com/BYVoid/OpenCC) | Apache-2.0，中文轉換引擎 | 無影片剪輯 | 無 | 離線簡轉繁與台灣詞彙轉換，不能修正語音辨識誤字 |

## 錄影工具的關鍵界線

OpenScreen 使用 `getopenscreen/openscreen`，原作者的 `siddharthvaddem/openscreen` 已封存，勿把舊庫當現維護線。
它的自動縮放讀取錄影旁的 `.cursor.json`。可匯入 MP4 剪輯與產字幕，但沒有同樣的游標資料就沒有相同的自動縮放能力。
游標只是停著指向某處而沒有點擊，也不會自然產生該次自動縮放。

本機 Whisper 轉錄、字幕燒錄與逐字稿刪除可免費使用。刪除選取文字或靜音會剪影片，仍是使用者操作。
Smart cuts 會讓外部 LLM 決定裁切，需自選供應者，API 可能收費。不要將它寫成完全離線免費的自動剪輯。
本機 MCP 可供既有 AI agent 操作，CLI 可錄影、字幕與匯出。兩者已在 v2 公開，不需要 GUI 自動化；CLI 仍需桌面／display session，Linux 錄影選擇器也可能要求操作，不能當成完全無人值守。
Silero VAD 在辨識流程跳過靜音，不等於輸出影片已自動刪除所有靜音。

固定繁體輸出的建議補法是轉錄後接 OpenCC，保留字幕時間碼，再燒錄或匯出。
OpenCC 可轉換字形與地區詞彙，專有名詞、台灣口音誤辨與字幕斷句仍需另外校對。
需交課程平台的 SRT／VTT 時，OpenScreen 尚須補輸出功能，Recordly 已有字幕 sidecar 路徑。
Recordly 的舊 fork 可能仍標 MIT，查現在 upstream 的 AGPL 與品牌條款，勿混用授權描述。

## 下載工具

| 工具 | 免費與授權 | 已確認用途／平台 | 更新與選擇條件 |
| --- | --- | --- | --- |
| [Varia](https://github.com/giantpinkrobots/varia) | 免費，MPL-2.0 | aria2＋yt-dlp，檔案、種子與影音下載，Windows／Linux；Mac Intel／ARM 為實驗版 | v2026.8.5-1，2026-08-23；`next` 於 2026-10-03 有程式更新 |
| [Gopeed](https://github.com/GopeedLab/gopeed) | 免費，GPL-3.0 | Mac／Windows／Linux 多連線下載，可裝影片外掛 | 穩定版 v1.9.3，2026-03-18；新 YouTube 外掛要求 2.0 |

Gopeed 2.0.0-beta.3 發布於 2026-09-18 UTC，台灣日期為 09-19。把測試版與穩定版分開列。
[monkeyWie 的 YouTube 外掛](https://github.com/monkeyWie/gopeed-extension-youtube) 現版本要求 Gopeed 2.0，勿用舊商店摘要推論 1.9.3 相容。
外掛 `package.json` 標示 ISC，與 Gopeed 本體 GPL-3.0 分開記錄。外掛相容性仍須實際下載影片驗收。

## Varia 繁中查核與改善

Varia 已有繁體中文，不要建立重複的繁中產品。`po/zh_TW.po` 在 `next` 與穩定版的檔案 SHA 相同。
本次統計目錄共 194 個訊息：125 個非 fuzzy 已翻譯、26 個 fuzzy、43 個空白。
125／194＝64.4% 是這份目錄可編譯的已譯比例，不是整個目前介面的完整度。
POT 落後程式，新增或變動字串可能未被目錄涵蓋，不能把既有 PO 統計當成全產品 coverage。
`zh_TW` 已列入 `po/LINGUAS`，建置的 `msgfmt` 不使用 fuzzy 翻譯。

Windows／Mac 可先將系統偏好語言設為繁體中文並重新啟動 Varia，檢查實際顯示。未驗證特定的應用程式語言切換選項或各安裝包語系行為，不自行杜撰設定路徑。
Linux 可嘗試 `LANGUAGE=zh_TW varia`，不同套件與桌面環境的結果尚未實測。
翻譯入口：[Varia 繁中 Weblate](https://hosted.weblate.org/projects/varia/varia/zh_Hant/)。
上游 [CONTRIBUTING.md](https://github.com/giantpinkrobots/varia/blob/next/CONTRIBUTING.md) 不接受 AI 生成翻譯、PR 描述與留言。
此次只記錄缺口，沒有翻譯或送 PR。後續由人工更新 POT、處理 fuzzy 與空白，再驗證實際介面。

## 五分鐘驗收

1. 用候選工具錄製一分鐘示範：三次點擊、兩秒停頓、中文解說與一個專有名詞。
2. 錄完檢查自動縮放是否跟到點擊，並匯入一個普通 MP4 比較是否缺游標資料。
3. 檢查停頓被刪除的操作是手動、音量規則還是 LLM，確認輸出保留有用的無聲操作。
4. 生成中文字幕，檢查繁體、專有名詞、斷句與裁切後的同步，輸出十秒確認燒錄或 SRT／VTT。
5. 下載工具用可下載的測試檔檢查暫停續傳，再測影片與繁中畫面，記錄 OS、CPU 架構、包版本與外掛版本。

這是初步篩選，長錄影、不同音量、批次匯出與平台特殊問題另做驗收。只完成源碼審閱時寫「已查核」，不寫「已實測」。

## 官方來源與排除項目

- OpenScreen：[v2.0.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.0.0)、[下載](https://github.com/getopenscreen/openscreen/releases)、[自動縮放](https://getopenscreen.com/features/auto-zoom/)、[字幕](https://getopenscreen.com/docs/captions/)、[AI／MCP](https://getopenscreen.com/docs/ai-editing/)、[CLI](https://getopenscreen.com/docs/cli/)。
- OpenScreen 中文字幕：[v2 語言代碼](https://github.com/getopenscreen/openscreen/blob/v2.0.0/src/lib/ai-edition/transcription/languageLabels.ts)、[Whisper 呼叫](https://github.com/getopenscreen/openscreen/blob/v2.0.0/electron/stt/whisperServer.ts)。
- Recordly：[下載](https://github.com/webadderallorg/Recordly/releases)、[授權與品牌條款](https://github.com/webadderallorg/Recordly/blob/main/LICENSE.md)、[字幕輸出原始碼](https://github.com/webadderallorg/Recordly/blob/v1.4.0/electron/ipc/register/exportCaptionSidecars.ts)。
- Auto-Editor：[31.7.2](https://github.com/WyattBlue/auto-editor/releases/tag/31.7.2)、[使用文件](https://auto-editor.com/docs/)、[授權](https://github.com/WyattBlue/auto-editor/blob/master/LICENSE)。
- Flowtake：[v1.7.2／下載](https://github.com/JNX03/Flowtake/releases/tag/v1.7.2)。OpenCC：[官方文件](https://github.com/BYVoid/OpenCC)、[授權](https://github.com/BYVoid/OpenCC/blob/master/LICENSE)。
- Varia：[官方下載](https://giantpinkrobots.github.io/varia/)、[版本](https://github.com/giantpinkrobots/varia/releases/tag/v2026.8.5-1)、[繁中目錄](https://github.com/giantpinkrobots/varia/blob/next/po/zh_TW.po)、[語言清單](https://github.com/giantpinkrobots/varia/blob/next/po/LINGUAS)、[建置](https://github.com/giantpinkrobots/varia/blob/next/po/meson.build)。
- Gopeed：[下載](https://gopeed.com/download)、[v1.9.3](https://github.com/GopeedLab/gopeed/releases/tag/v1.9.3)、[2.0.0-beta.3](https://github.com/GopeedLab/gopeed/releases/tag/v2.0.0-beta.3)、[外掛需求](https://github.com/monkeyWie/gopeed-extension-youtube/blob/main/README.md)、[外掛授權欄位](https://github.com/monkeyWie/gopeed-extension-youtube/blob/main/package.json)。

不列首選：XDM 8 版仍是 2023 release，9 尚未發布；Persepolis 有 2025 版本但本次未確認 2026 維護證據。
Coherence 近期核心進度不足，游標 inactive 不是音訊 silence，不能拿來聲稱自動刪解說停頓。
