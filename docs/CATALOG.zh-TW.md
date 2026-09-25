# 開源與免費軟體清單

[繁體中文](CATALOG.zh-TW.md) · [English](CATALOG.en.md)

**190 個候選 · 53 大類 · 180 個開源專案 · 8 個非開源免費版／內建候選 · 2 個原始碼可見候選**

資料集更新：2026-09-25；個別查核日見各列。包含引擎與需設定項目，不代表全部可免費一鍵安裝；工作流與繁中品質未實測。

[Alternatives](ALTERNATIVES.zh-TW.md) · [Research](RESEARCH.md) · [Sources](SOURCES.md) · [Forums](FORUMS.md) · [JSON](../data/products.json) · [Contribute](../CONTRIBUTING.md)

## screen-recording

**螢幕錄影**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [OBS Studio](https://github.com/obsproject/obs-studio) | 課程長錄影、直播、多場景與多音訊來源 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0-or-later | 不把錄影能力等同 Screen Studio 式自動運鏡；目前官方 Mac 版本要求 macOS 13+。 | [official-docs-reviewed](https://github.com/obsproject/obs-studio/blob/master/README.rst) / 2026-09-11 |
| [Recordly](https://github.com/webadderallorg/Recordly) | 教學示範、產品 demo、自動縮放與游標動畫 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0；另見 LICENSE.md | Mac 14+；Linux 游標隱藏有限制。README 標 AGPL-3.0，LICENSE.md 另有品牌及署名文字，改版前要核對全文。 | [official-docs-reviewed](https://github.com/webadderallorg/Recordly/blob/main/README.md) / 2026-09-10 |
| [Capptivo](https://github.com/SECHAK-AG/capptivo) | 跟隨游標縮放、點擊縮放、錄影標記及本機字幕 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | Mac 建置未簽署；字幕需另備 whisper-cli，首次下載模型；Mac 13+。附帶元件各有授權。 | [official-docs-reviewed](https://github.com/SECHAK-AG/capptivo/blob/main/README.md) / 2026-09-10 |
| [Cap](https://github.com/CapSoftware/Cap) | Loom 式錄影分享與 Studio 模式的縮放、字幕、裁切 | macos, windows · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0 為主；指定 crates 為 MIT | 本機、雲端、自架及官方方案費用分開核對；不能把開源當成所有託管服務免費。 | [official-docs-reviewed](https://github.com/CapSoftware/Cap/blob/main/README.md) / 2026-09-10 |
| [Screenity](https://github.com/alyssaxuu/screenity) | 瀏覽器示範錄影、畫面註記、點擊與游標強調 | macos, windows, linux · 瀏覽器外掛 | 開源；安裝包、模型與服務費用另查 · GPL-3.0（MV3 版本） | 瀏覽器錄影與原生桌面錄影有差異；免費外掛與 Screenity Pro 功能不可混用。 | [official-docs-reviewed](https://github.com/alyssaxuu/screenity/blob/master/README.md) / 2026-09-10 |
| [OpenScreenStudio](https://github.com/Glyph-Software/OpenScreenStudio) | Mac 專用自動點擊縮放、游標覆蓋、攝影機泡泡與 MP4／GIF | macos · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0 | README 說基礎需求 Mac 13+，但實際 ScreenCaptureKit 錄影路徑需 Mac 15+；未公證，先小範圍試錄。 | [official-docs-reviewed](https://github.com/Glyph-Software/OpenScreenStudio/blob/main/README.md) / 2026-09-10 |
| [Kap](https://github.com/wulkano/Kap) | 簡單區域錄影、快速製作短示範 | macos · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | 主 repo 最後推送時間為 2024-11，較久；新系統相容性待測，不列長課程主錄影首選。 | [official-docs-reviewed](https://github.com/wulkano/Kap/blob/main/README.md) / 2026-09-10 |
| [ScreenToGif](https://github.com/NickeManarin/ScreenToGif) | 短錄影與 GIF 編輯，適合教學步驟 | windows · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MS-PL | 僅 Windows；不適合拿來代表 Mac 替代方案，也不是長課程剪輯系統。 | [official-docs-reviewed](https://github.com/NickeManarin/ScreenToGif/blob/master/README.md) / 2026-09-10 |
| [ScreenPal](https://screenpal.com/plans) | 短教學錄影 | macos, windows · 桌面軟體 | 有功能限制的免費版；非開源 · see-upstream | 官網免費方案每段 15 分鐘，長課程優先選其他工具；不將所有行銷頁功能都當免費。 | [official-docs-partial](https://screenpal.com/plans) / 2026-09-10 |
| [FlashBack Express](https://www.flashbackrecorder.com/express) | 錄影候選 | windows · 桌面軟體 | 免費與付費功能界線待查 · see-upstream | 官網確認 Windows 與本機儲存；文章對水印描述不一致，編輯與 AI 功能免費範圍尚待版本／方案表確認。 | [official-docs-partial](https://www.flashbackrecorder.com/express) / 2026-09-10 |
| [macOS Screenshot / QuickTime](https://support.apple.com/en-us/102618) | 基本螢幕錄影 | macos · 系統內建 | macOS 內建；非開源 · see-upstream | 不需另購錄影軟體；官方操作支援畫面與麥克風，不據此保證所有系統音訊需求。 | [official-docs-partial](https://support.apple.com/en-us/102618) / 2026-09-10 |
| [Screenify](https://www.imobie.com/screenify/) | 錄教學、螢幕加鏡頭、錄音後簡單修剪 | macos, windows · 桌面軟體 | 免費軟體；非開源 · see-upstream | 官網稱免費、無錄影時間限制，支援本機輸出；FocuSee 的自動運鏡是另一產品。繁中與新款 Mac 尚未實測。 | [official-docs-partial](https://www.imobie.com/screenify/) / 2026-09-10 |

## screenshots-ocr

**截圖與 OCR**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [ShareX](https://github.com/ShareX/ShareX) | 截圖、滾動擷取、箭頭文字、遮蔽、OCR 與後續自動化 | windows · 桌面軟體 | 免費開源 · GPL-3.0 | 僅 Windows；自動上傳是可選工作流程，私密截圖應只選本機輸出。 | [official-docs-reviewed](https://github.com/ShareX/ShareX/blob/develop/README.md) / 2026-09-11 |
| [Flameshot](https://github.com/flameshot-org/flameshot) | 快速截圖並加箭頭、文字、框線等教學標記 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | Mac 上的快捷鍵與螢幕權限需實測；不是完整長截圖／素材管理工作台。 | [official-docs-reviewed](https://github.com/flameshot-org/flameshot/blob/master/README.md) / 2026-09-10 |
| [ksnip](https://github.com/ksnip/ksnip) | 截圖編號、註解、釘選等說明圖用途 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | 官方功能表顯示各平台不同；全域快捷鍵主要限 Windows／X11，OCR 外掛不是全平台相同。作者正在找共同維護者。 | [official-docs-reviewed](https://github.com/ksnip/ksnip/blob/master/README.md) / 2026-09-10 |
| [Greenshot](https://github.com/greenshot/greenshot) | 輕量截圖、標示、局部遮蔽與輸出 | windows · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | 此 repo 是 Windows 版；不把同名 Mac 產品算進這個開源項目。 | [official-docs-reviewed](https://github.com/greenshot/greenshot/blob/main/README.md) / 2026-09-10 |
| [NormCap](https://github.com/dynobo/normcap) | 從畫面擷取文字，減少手動抄寫 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0-or-later | OCR 工具而非註解編輯器；中文辨識取決於 Tesseract 語言資料，繁中語料效果待測。 | [official-docs-reviewed](https://github.com/dynobo/normcap/blob/main/README.md) / 2026-09-10 |
| [Text Grab](https://github.com/TheJoeFin/Text-Grab) | 快速框選畫面轉成可複製文字 | windows · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | Windows 專用；OS OCR 語言及字型影響結果。 | [official-docs-reviewed](https://github.com/TheJoeFin/Text-Grab/blob/main/README.md) / 2026-09-10 |
| [Lightshot](https://app.prntscr.com/en/index.html) | 快速區域截圖與標註 | macos, windows · 桌面軟體 | 免費軟體；非開源 · see-upstream | 有官方免費下載；網路分享會上傳截圖，不等於所有截圖都只留在本機。 | [official-docs-partial](https://app.prntscr.com/en/index.html) / 2026-09-10 |
| [macshot](https://github.com/sw33tLie/macshot) | Mac 截圖、16:9／固定像素尺寸選取、標註、OCR、翻譯、滾動擷取與錄影 | macos · 桌面軟體 | 免費開源 · GPL-3.0 | 要求 macOS 12.3+；官方 README 列 40 種語言，但繁中介面與台灣情境未實測；雲端上傳需自行設定服務，完整 CleanShot X 等效仍需逐項比對。 | [official-docs-reviewed](https://github.com/sw33tLie/macshot) / 2026-09-25 |
| [Capso](https://github.com/lzhgus/Capso) | Mac 原生截圖、螢幕錄影、16:9／固定像素尺寸選取、OCR 與標註 | macos · 桌面軟體 | 免費使用；原始碼可見，非 OSI 開源 · Business Source License 1.1，依專案條款三年後轉 Apache-2.0 | 要求 macOS 15+；BSL 1.1 禁止 fork 後販售競爭產品；Cloud Share 需自備 Cloudflare R2，錄影、相機與麥克風需授權。 | [official-docs-reviewed](https://github.com/lzhgus/Capso/blob/main/README.md) / 2026-09-25 |

## dictation

**語音輸入／聽寫**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Handy](https://github.com/cjpais/Handy) | 按快捷鍵說話，把文字輸入目前游標位置 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | 先下載模型；不同模型支援語言不同，繁中情境應選支援中文的多語模型；藍牙麥克風可能影響播放音質。 | [official-docs-reviewed](https://github.com/cjpais/Handy/blob/main/README.md) / 2026-09-10 |
| [OpenWhispr](https://github.com/OpenWhispr/openwhispr) | 語音輸入、整理口述文字、會議與筆記 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | 本機與雲端模式分開；選雲端模型可能有 API 費用；Intel Mac 部分說話者功能受限。 | [official-docs-reviewed](https://github.com/OpenWhispr/openwhispr/blob/main/README.md) / 2026-09-10 |
| [VoiceInk](https://github.com/Beingpax/VoiceInk) | Mac 原生語音輸入，評估 Superwhisper／Wispr Flow 類用途 | macos · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | 原始碼開放但官方成品有試用及付費方案；自行建置需開發環境。文件 Mac 最低版本敘述有 14.0／14.4 差異，依成品要求核對。 | [official-docs-reviewed](https://github.com/Beingpax/VoiceInk/blob/main/README.md) / 2026-09-10 |
| [Whispering／Epicenter](https://github.com/EpicenterHQ/epicenter) | 錄音後轉文字、選擇轉錄供應商與可選潤飾 | macos, windows, linux, web · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0-or-later（目前 apps） | 舊 braden-w repo 已封存並搬移；桌面由 Epicenter 宿主提供，Web 與桌面能力不同；不能引用舊版 MIT 作新版授權。 | [official-docs-reviewed](https://github.com/EpicenterHQ/epicenter/blob/main/apps/whispering/README.md) / 2026-09-10 |
| [Apple Dictation](https://support.apple.com/guide/mac-help/use-dictation-mh40584/mac) | 將說話輸入文字欄位 | macos · 系統內建 | macOS 內建；非開源 · see-upstream | 不是長音檔逐字稿工具；是否在裝置處理需查看鍵盤設定，語言與功能依系統而異。 | [official-docs-partial](https://support.apple.com/guide/mac-help/use-dictation-mh40584/mac) / 2026-09-10 |
| [TypeWhisper](https://github.com/TypeWhisper/typewhisper-mac) | 跨應用程式聽寫，可選本機或雲端引擎 | macos · 桌面軟體 | 免費開源 · GPL-3.0 | 本機模型需下載；雲端 API 可能收費，繁中介面未確認。 | [official-docs-reviewed](https://github.com/TypeWhisper/typewhisper-mac) / 2026-09-11 |

## transcription

**逐字稿與會議轉錄**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Vibe](https://github.com/thewh1teagle/vibe) | 現成的音訊／影片本機轉錄，具說話者分離與時間戳相關功能 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | 適合和你的 MOSS-ASR 比較現成工作流程；多人效果與專有名詞需同語料測試。 | [official-docs-reviewed](https://github.com/thewh1teagle/vibe/blob/main/README.md) / 2026-09-10 |
| [Buzz](https://github.com/chidiwilliams/buzz) | 音訊影片或麥克風轉錄，輸出 TXT／SRT／VTT | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | 選本機 backend 才符合離線要求；README 的安裝包入口指向 SourceForge。 | [official-docs-reviewed](https://github.com/chidiwilliams/buzz/blob/main/README.md) / 2026-09-10 |
| [aTrain](https://github.com/aTrainTranscription/aTrain) | 研究訪談、離線逐字稿與說話者分離 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0 | 主要現成發布通路是 Windows／Linux；Mac 不以一般一鍵安裝推薦；GPU 配置另計。 | [official-docs-reviewed](https://github.com/aTrainTranscription/aTrain/blob/develop/README.md) / 2026-09-10 |
| [WhisperX](https://github.com/m-bain/whisperX) | 字級時間戳對齊、多人逐字稿與字幕底層 | windows, linux · 開發引擎 | 開源；安裝包、模型與服務費用另查 · BSD-2-Clause（程式） | 不是現成桌面 App；說話者模組有模型下載與條款要求，重疊語音及中文對齊效果需驗證。 | [official-docs-reviewed](https://github.com/m-bain/whisperX/blob/main/README.md) / 2026-09-10 |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | 本機 Whisper 推論，適合 Mac 端或現成工具串接 | macos, windows, linux · 開發引擎 | 開源；安裝包、模型與服務費用另查 · MIT | 模型需要另備；引擎本身不是完整編輯、校對或多人標記工作台。 | [official-docs-reviewed](https://github.com/ggml-org/whisper.cpp/blob/master/README.md) / 2026-09-10 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | 以 CTranslate2 執行 Whisper，適合大量轉錄 | macos, windows, linux · 開發引擎 | 開源；安裝包、模型與服務費用另查 · MIT | NVIDIA GPU 加速與 Mac Metal 不是同一條路線；不是可直接取代逐字稿網站的 UI。 | [official-docs-reviewed](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md) / 2026-09-10 |
| [FunASR](https://github.com/modelscope/FunASR) | ASR、VAD、標點與說話者流程，補中文語音處理選擇 | 待確認 · 需要設定 | 開源；安裝包、模型與服務費用另查 · MIT（程式）；模型另核對 | 程式 MIT 不等於所有模型相同授權；需指定 checkpoint、硬體與模型條款。 | [official-docs-reviewed](https://github.com/modelscope/FunASR/blob/main/README.md) / 2026-09-10 |
| [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | 離線 ASR／TTS／VAD／說話者與語音處理共用引擎 | macos, windows, linux, android, ios · 開發引擎 | 開源；安裝包、模型與服務費用另查 · Apache-2.0（程式） | 是整合底層，不算另一個現成 dictation App；不同模型能力及授權各自核對。 | [official-docs-reviewed](https://github.com/k2-fsa/sherpa-onnx/blob/master/README.md) / 2026-09-10 |
| [noScribe](https://github.com/kaixxx/noScribe) | 本機訪談逐字稿與說話者分段 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 需要模型、儲存空間及運算時間；台灣口音辨識未實測。 | [official-docs-reviewed](https://github.com/kaixxx/noScribe) / 2026-09-11 |
| [Meetily Community](https://github.com/Zackriya-Solutions/meetily) | 本機會議轉錄與摘要的社群版 | macos, windows · 桌面軟體 | 免費開源 · MIT | 摘要需設定模型；Pro 的進階功能不能算入免費社群版。 | [official-docs-reviewed](https://github.com/Zackriya-Solutions/meetily) / 2026-09-11 |

## subtitles

**字幕與翻譯**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit) | 字幕校對、時間軸、轉格式與可選語音／翻譯服務 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | 現行 repo 已有跨平台建置；Mac 推薦 14+，文件稱最低 12；下載時辨別 RC 與穩定版。線上服務可能付費。 | [official-docs-reviewed](https://github.com/SubtitleEdit/subtitleedit/blob/main/README.md) / 2026-09-10 |
| [pyVideoTrans](https://github.com/jianchang512/pyvideotrans) | 轉錄、字幕翻譯、多角色配音、音畫對齊與影片合成 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | Windows 有預打包版；Mac／Linux 安裝較多設定。是否離線與費用依 ASR／LLM／TTS 選擇。 | [official-docs-reviewed](https://github.com/jianchang512/pyvideotrans/blob/main/README.md) / 2026-09-10 |
| [VideoLingo](https://github.com/Huanshere/VideoLingo) | 影片翻譯、字幕分段對齊與配音 | 待確認 · 需要設定 | 開源；安裝包、模型與服務費用另查 · Apache-2.0 | 已有完整流程，值得先用；需配置環境與模型／API，不把作者的 Netflix 品質宣稱當作驗證結果。 | [official-docs-reviewed](https://github.com/Huanshere/VideoLingo/blob/main/README.md) / 2026-09-10 |

## text-to-speech

**TTS 文字轉語音**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Readest](https://github.com/readest/readest) | 閱讀文件／電子書時使用 TTS 朗讀 | macos, windows, linux, android, ios, web · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0 | 是現成閱讀入口，不是 Obsidian 外掛或配音錄音室；音色、離線程度及費用依所用 TTS 服務。 | [official-docs-reviewed](https://github.com/readest/readest/blob/main/README.md) / 2026-09-10 |
| [Piper（現行維護線）](https://github.com/OHF-Voice/piper1-gpl) | 低延遲本機文字朗讀，供既有閱讀工具接入 | 待確認 · 開發引擎 | 開源；安裝包、模型與服務費用另查 · GPL-3.0（程式） | 不是廣告表演級音色保證；聲音模型有各自授權，繁中發音與台灣口音待測。 | [official-docs-reviewed](https://github.com/OHF-Voice/piper1-gpl/blob/main/README.md) / 2026-09-10 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | 中文與多語配音、聲音設計、聲音複製 | 待確認 · 需要設定 | 開源；安裝包、模型與服務費用另查 · Apache-2.0（repo）；指定權重另核對 | 適合本機或自架評估，不是 Mac 一鍵 App；長文穩定度、停頓與台灣口音要試聽。 | [official-docs-reviewed](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md) / 2026-09-10 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 少量語音素材建立聲音模型、中文與跨語言配音 | macos, windows, linux · 需要設定 | 開源；安裝包、模型與服務費用另查 · MIT（程式）；權重另核對 | 需要設定與素材；整合包、預訓練權重及附帶模型分開核對，不等於全程零設定。 | [official-docs-reviewed](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md) / 2026-09-10 |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) | 多語聲音生成、聲音複製、中文發音控制 | 待確認 · 需要設定 | 開源；安裝包、模型與服務費用另查 · Apache-2.0（程式）；權重另核對 | 目前 repo 位於 QwenAudio；適合比較配音後端，Mac 部署與效能不作已支援承諾。 | [official-docs-reviewed](https://github.com/QwenAudio/CosyVoice/blob/main/README.md) / 2026-09-10 |
| [Kokoro](https://github.com/hexgrad/kokoro) | 輕量本機 TTS，普通話與英文等語言朗讀 | macos, windows, linux · 開發引擎 | 開源；安裝包、模型與服務費用另查 · Apache-2.0；README 稱權重亦 Apache | README 支援 Mandarin，不能推導為台灣口音；中文額外依賴與長文品質需測。 | [official-docs-reviewed](https://github.com/hexgrad/kokoro/blob/main/README.md) / 2026-09-10 |
| [eSpeak NG](https://github.com/espeak-ng/espeak-ng) | 低資源朗讀、輔助功能與發音處理 | windows, linux · 開發引擎 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | 聲音較機械，適合功能性朗讀，不列商業形象片配音首選；Mac 整合另核對。 | [official-docs-reviewed](https://github.com/espeak-ng/espeak-ng/blob/master/README.md) / 2026-09-10 |

## video-editing

**影片剪輯、合成與轉檔**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Auto-Editor](https://github.com/WyattBlue/auto-editor) | 先剪掉靜音或低活動片段，再匯出到既有剪輯軟體 | macos, windows, linux · 需要設定 | 開源；安裝包、模型與服務費用另查 · Unlicense（repo） | 官方 README 已有 Skill 安裝入口；音量偵測不理解內容，會誤刪閱讀／操作停頓。商業 GUI 與此開源 CLI 不同。 | [official-docs-reviewed](https://github.com/WyattBlue/auto-editor/blob/master/README.md) / 2026-09-10 |
| [LosslessCut](https://github.com/mifi/lossless-cut) | 快速裁切長錄影、抽音軌與無重編碼處理 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-2.0 | 關鍵影格與格式限制會影響切點；不是完整 NLE，也不能靠 stream copy 燒字幕。 | [official-docs-reviewed](https://github.com/mifi/lossless-cut/blob/master/README.md) / 2026-09-10 |
| [Kdenlive](https://github.com/KDE/kdenlive) | 一般剪輯、多軌影片與字幕工作 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 適合新專案評估，不能保證 Premiere 專案／外掛完整遷移。現行下載頁 Mac 13+。 | [official-docs-reviewed](https://github.com/KDE/kdenlive/blob/master/README.md) / 2026-09-11 |
| [Shotcut](https://github.com/mltframework/shotcut) | 一般剪接與多格式影片處理 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | 客戶指定專案格式要另評估；現行 Mac 版為 12+，較舊 OS 有舊版下載。 | [official-docs-reviewed](https://github.com/mltframework/shotcut/blob/master/README.md) / 2026-09-10 |
| [HandBrake](https://github.com/HandBrake/HandBrake) | 課程影片壓縮、轉 MP4／MKV／WebM 與裝置用格式 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-2.0 | 是轉碼器，不是時間軸剪輯器；不以多次轉碼替代保留高品質母檔。 | [official-docs-reviewed](https://github.com/HandBrake/HandBrake/blob/master/README.markdown) / 2026-09-10 |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 批次轉檔、抽音訊、字幕燒錄與影音流程串接 | macos, windows, linux · 開發引擎 | 開源；安裝包、模型與服務費用另查 · LGPL 為主／可選 GPL 元件 | 使用現成命令即可；LGPL／GPL 取決於建置元件，不能用單一授權涵蓋所有 binary。 | [official-docs-reviewed](https://github.com/FFmpeg/FFmpeg/blob/master/README.md) / 2026-09-10 |
| [Natron](https://github.com/NatronGitHub/Natron) | 節點式合成、摳像與 OpenFX 流程 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-2.0 | 不能打包宣稱完整替代 After Effects；Mac CPU 架構與版本相容性需核對下載包。 | [official-docs-reviewed](https://github.com/NatronGitHub/Natron/blob/RB-2.6/README.md) / 2026-09-10 |
| [Blender](https://github.com/blender/blender) | 沿用你既有 3D 能力，承接 3D、合成與部分影片工作 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0（整體） | 不是新發現的工具；保留作已安裝可重用選項，不把轉換現有商業專案的成本當零。 | [official-docs-reviewed](https://github.com/blender/blender/blob/main/README.md) / 2026-09-10 |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | 剪輯、調色、音訊後製 | macos, windows, linux · 桌面軟體 | 有免費版；非開源 · see-upstream | 有免費桌面版；Studio 的 AI、降噪等不算免費能力，格式支援需按素材核對。 | [official-docs-partial](https://www.blackmagicdesign.com/products/davinciresolve) / 2026-09-10 |

## audio-editing

**音訊編輯**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Audacity](https://github.com/audacity/audacity) | 口播剪輯、多軌錄音與基本音訊整理 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0（整體）；部分檔案另有授權 | 不等於完整取代 Audition 的所有專業工作流；本次 master 涉及新版開發，使用者應選穩定版。 | [official-docs-reviewed](https://github.com/audacity/audacity/blob/master/README.md) / 2026-09-10 |
| [Ultimate Vocal Remover（UVR）](https://github.com/Anjok07/ultimatevocalremovergui) | 將人聲與伴奏分離，整理影片配音素材 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT（GUI）；模型另核對 | 分離結果可能有殘留與音質損失；模型與 GUI 授權分開，不能承諾錄音修復百分百成功。 | [official-docs-reviewed](https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md) / 2026-09-10 |

## graphics

**修圖與繪圖**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [GIMP](https://www.gimp.org/) | 照片修整與點陣圖編輯 | macos, windows, linux · 桌面軟體 | 免費開源 · see-upstream | 官網確認免費開源；能否替代特定 Photoshop 專案需用實際檔案確認。 | [official-docs-partial](https://www.gimp.org/) / 2026-09-10 |
| [Krita](https://krita.org/en/) | 繪畫、筆刷與插畫 | macos, windows, linux · 桌面軟體 | 免費開源 · see-upstream | 官網提供免費版本與繁中網站；不把網站翻譯當成已實測完整繁中 UI。 | [official-docs-partial](https://krita.org/en/) / 2026-09-10 |

## office

**文書與 Office**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [LibreOffice](https://www.libreoffice.org/) | 文件、試算表、簡報與 Draw | macos, windows, linux · 桌面軟體 | 免費開源 · see-upstream | 官網確認免費開源；不沿用文章『完全相容』說法，正式交付檔案需驗證。 | [official-docs-partial](https://www.libreoffice.org/) / 2026-09-10 |
| [ONLYOFFICE Desktop Editors](https://www.onlyoffice.com/desktop) | 文件、試算表、簡報與 PDF | macos, windows, linux · 桌面軟體 | 免費開源桌面版 · see-upstream | 確認免費桌面產品；雲端協作方案、AI 提供者與付費服務另外核對。 | [official-docs-partial](https://www.onlyoffice.com/desktop) / 2026-09-10 |

## pdf

**PDF 閱讀與處理**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [PDF24 Creator](https://tools.pdf24.org/en/creator) | PDF 合併、拆分、轉檔與 OCR | windows · 桌面軟體 | 個人與商用免費 · see-upstream | 官網明列私人與商業使用免費，離線處理；桌面版沒有 macOS。 | [official-docs-partial](https://tools.pdf24.org/en/creator) / 2026-09-10 |
| [SumatraPDF](https://www.sumatrapdfreader.org/free-pdf-reader) | 輕量 PDF 與電子書閱讀 | windows · 桌面軟體 | 免費開源 · see-upstream | 僅 Windows；閱讀器不能當成 Acrobat Pro 正文編輯替代品。 | [official-docs-reviewed](https://www.sumatrapdfreader.org/free-pdf-reader) / 2026-09-11 |
| [PDFsam Basic](https://pdfsam.org/pdfsam-basic/) | PDF 合併、分割、旋轉與擷取頁面 | macos, windows, linux · 桌面軟體 | 免費開源 · AGPL-3.0 | Basic 不等於另售 Visual／Enhanced；不能據此承諾正文編輯。 | [official-docs-reviewed](https://pdfsam.org/pdfsam-basic/) / 2026-09-11 |

## file-transfer

**傳檔與檔案同步**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [LocalSend](https://localsend.org/) | 同一區域網路跨裝置傳檔 | macos, windows, linux, android, ios · 桌面軟體 | 免費開源 · see-upstream | 雙方裝置需可互通；不是附贈雲端空間或遠端分享服務。 | [official-docs-reviewed](https://localsend.org/) / 2026-09-11 |
| [Syncthing](https://syncthing.net/) | 裝置間同步檔案 | macos, windows, linux · 桌面軟體 | 免費開源 · see-upstream | 需要自己的裝置與儲存空間，不附贈雲端容量。 | [official-docs-reviewed](https://syncthing.net/) / 2026-09-11 |
| [rclone](https://github.com/rclone/rclone) | 在不同雲端空間與本機間搬移、複製及同步檔案 | macos, windows, linux · 命令列 | 開源；安裝包、模型與服務費用另查 · MIT | 命令列工具；同步可傳播刪除，不能視為版本備份。雲端容量、API 配額與流量費依供應商。 | [official-docs-reviewed](https://github.com/rclone/rclone) / 2026-09-12 |

## productivity

**視窗、剪貼簿與系統整理**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Rectangle](https://rectangleapp.com/) | 快捷鍵與拖曳排列視窗 | macos · 桌面軟體 | 免費開源 · see-upstream | 本條目是免費 Rectangle，另售 Rectangle Pro；僅 Mac。 | [official-docs-reviewed](https://rectangleapp.com/) / 2026-09-11 |
| [Maccy](https://github.com/p0deje/Maccy) | 以快捷鍵搜尋剪貼簿歷史 | macos · 桌面軟體 | 免費開源 · MIT | GitHub Releases 可取得免費版本；目前需 macOS 14+，先設定敏感內容排除。 | [official-docs-reviewed](https://github.com/p0deje/Maccy) / 2026-09-11 |
| [Pearcleaner](https://github.com/alienator88/Pearcleaner) | Mac 應用程式移除與相關檔案整理 | macos · 桌面軟體 | 免費；原始碼可見，非開源 · Apache-2.0 with Commons Clause; source-available | Commons Clause 限制，不能標為 OSI 開源；上游維護暫停，不列優先推薦。 | [official-docs-reviewed](https://github.com/alienator88/Pearcleaner) / 2026-09-11 |
| [BleachBit](https://github.com/bleachbit/bleachbit) | 清理快取、暫存檔與應用程式痕跡 | windows, linux · 桌面軟體 | 免費開源 · GPL-3.0-or-later | 刪除前先用預覽檢查範圍；清理不等於修復硬碟或保證加速，正式成品以 Windows／Linux 為主。 | [official-docs-reviewed](https://github.com/bleachbit/bleachbit) / 2026-09-12 |

## archives

**壓縮與解壓縮**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [7-Zip](https://www.7-zip.org/) | Windows 圖形介面壓縮與解壓縮 | windows · 桌面軟體 | 免費開源 · LGPL/BSD components; unRAR restrictions | 可解開 RAR，不可建立 RAR；其他平台的命令列版本另查。 | [official-docs-reviewed](https://www.7-zip.org/) / 2026-09-11 |
| [PeaZip](https://peazip.github.io/) | 跨平台壓縮與解壓縮介面 | macos, windows, linux · 桌面軟體 | 免費開源 · see-upstream | 先確認使用格式的建立或解壓支援，以及系統對應安裝包。 | [official-docs-reviewed](https://peazip.github.io/) / 2026-09-11 |

## media-players

**影音播放**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [VLC media player](https://github.com/videolan/vlc) | 本機影片與音訊播放 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0-or-later; components vary | 播放器用途；不等於影片剪輯器，也不包含付費影音內容。 | [official-docs-reviewed](https://github.com/videolan/vlc) / 2026-09-11 |
| [IINA](https://iina.io/) | Mac 原生風格影音播放器 | macos · 桌面軟體 | 免費開源 · GPL-3.0 | 僅 Mac；不同處理器與版本的最低系統需求須依官網。 | [official-docs-reviewed](https://iina.io/) / 2026-09-11 |
| [FreeTube](https://freetubeapp.io/) | 桌面 YouTube 觀看與本機觀看紀錄 | macos, windows, linux · 桌面軟體 | 免費開源 · AGPL-3.0 | 觀看仍需連網；不是付費內容通行證，也非 YouTube Premium 完整替代。 | [official-docs-reviewed](https://freetubeapp.io/) / 2026-09-11 |

## email

**電子郵件**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Thunderbird](https://www.thunderbird.net/en-US/) | 桌面郵件管理 | macos, windows, linux · 桌面軟體 | 免費開源 · see-upstream | 免費郵件客戶端不包含付費信箱、雲端容量或企業服務。 | [official-docs-reviewed](https://www.thunderbird.net/en-US/) / 2026-09-11 |

## passwords

**密碼管理**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [KeePassXC](https://keepassxc.org/) | 本機加密密碼資料庫 | macos, windows, linux · 桌面軟體 | 免費開源 · see-upstream | 同步與備份需自行規劃；先確認團隊分享、復原及管理需求。 | [official-docs-reviewed](https://keepassxc.org/) / 2026-09-11 |

## notes-reading

**筆記與電子書**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Joplin](https://joplinapp.org/) | 本機筆記與待辦整理 | macos, windows, linux, android, ios · 桌面軟體 | 免費開源 · see-upstream | Joplin Cloud 另外收費；同步服務、匯入品質及團隊功能需確認。 | [official-docs-reviewed](https://joplinapp.org/) / 2026-09-11 |
| [calibre](https://calibre-ebook.com/about) | 電子書管理、閱讀與格式轉換 | macos, windows, linux · 桌面軟體 | 免費開源 · see-upstream | 不保證所有書籍格式與排版都能無損轉換。 | [official-docs-reviewed](https://calibre-ebook.com/about) / 2026-09-11 |

## vector-design

**向量設計與 UI 原型**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Inkscape](https://inkscape.org/) | 製作 Logo、圖示、向量插畫與 SVG 網頁素材 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0-or-later | 以 SVG 為核心；AI 檔、外掛與印刷交付需用實際檔案測試，不能保證 Illustrator 專案無損往返。 | [official-docs-reviewed](https://gitlab.com/inkscape/inkscape/-/raw/master/README.md) / 2026-09-12 |
| [Penpot](https://github.com/penpot/penpot) | 瀏覽器 UI 設計、互動原型、設計元件與多人協作，可自行部署 | web · 需自架 | 開源核心；代管與企業服務可能另計 · MPL-2.0 | 自架需主機維護；企業 SSO、權限與管理功能有付費方案，Figma 元件與外掛需另測遷移。 | [official-docs-reviewed](https://raw.githubusercontent.com/penpot/penpot/develop/README.md) / 2026-09-12 |

## desktop-publishing

**桌面出版與字型製作**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Scribus](https://www.scribus.net/) | 雜誌、型錄、宣傳單與印刷 PDF 排版，支援 CMYK、特別色與 ICC 色彩管理 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 / GPL-3.0; see component notices | 繁中字型、長文溢出及印廠規格需校樣；GitHub 為社群鏡像，下載與問題回報依官方入口。 | [official-docs-reviewed](https://sourceforge.net/projects/scribus/) / 2026-09-12 |
| [FontForge](https://github.com/fontforge/fontforge) | 製作、修改及轉換 OpenType、TrueType、UFO 等字型 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0-or-later as a whole; many parts BSD-3-Clause | 字距、提示資訊及不同系統的顯示需驗證；工具免費不代表取得原字型的修改或再散布權。 | [official-docs-reviewed](https://github.com/fontforge/fontforge) / 2026-09-12 |

## photo-workflow

**RAW 顯影、照片管理與全景**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [darktable](https://github.com/darktable-org/darktable) | 非破壞式 RAW 顯影、照片資料庫、批次調整與輸出 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 官方明言不是 Lightroom 複製品；目前 README 的 Mac 支援為 Apple Silicon／macOS 14+，相機與編輯資料遷移需另測。 | [official-docs-reviewed](https://github.com/darktable-org/darktable) / 2026-09-12 |
| [RawTherapee](https://github.com/RawTherapee/RawTherapee) | RAW 顯影、去馬賽克、色彩調整與高品質照片輸出 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 官方定位聚焦影像顯影，完整素材管理、列印與上傳需搭配其他工具；先確認相機格式。 | [official-docs-reviewed](https://github.com/RawTherapee/RawTherapee) / 2026-09-12 |
| [digiKam](https://www.digikam.org/) | 大量相片與影片匯入、標籤、評分、搜尋、RAW 管理及批次處理 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0-or-later | 本機照片庫需自行備份；遠端服務外掛另有資料傳輸與服務條件，不能當成已包含雲端儲存。 | [official-docs-reviewed](https://www.digikam.org/about/) / 2026-09-12 |
| [Hugin](https://hugin.sourceforge.io/) | 把重疊照片接成全景或大型拼接影像 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 視差、移動物體與曝光差異仍需人工檢查；各平台安裝包來源與版本需按下載頁確認，官方列有繁中但未實測。 | [official-docs-reviewed](https://hugin.sourceforge.io/) / 2026-09-12 |

## cad-modeling

**CAD 製圖與參數建模**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [FreeCAD](https://github.com/FreeCAD/FreeCAD) | 參數式零件建模、約束草圖、尺寸修改與工程圖 | macos, windows, linux · 桌面軟體 | 免費開源 · LGPL-2.1 | 工作台與外掛功能需分開確認；大型組立、CAM 後處理及商用 CAD 檔案往返要用實際專案測試。 | [official-docs-reviewed](https://github.com/FreeCAD/FreeCAD) / 2026-09-12 |
| [LibreCAD](https://github.com/LibreCAD/LibreCAD) | 2D 工程製圖與 DXF 圖面編輯、轉 PDF／SVG | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 主力是 2D；DWG 版本、字型、標註與圖層輸出需實檔核對，Mac 建置未公證。 | [official-docs-reviewed](https://github.com/LibreCAD/LibreCAD) / 2026-09-12 |
| [OpenSCAD](https://github.com/openscad/openscad) | 以程式定義可重複修改尺寸的零件、治具與 3D 列印模型 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 with CGAL linking exception | 需寫腳本；不以自由雕塑或角色動畫為定位，布林運算與輸出模型仍要驗證。 | [official-docs-reviewed](https://github.com/openscad/openscad) / 2026-09-12 |
| [SolveSpace](https://github.com/solvespace/solvespace) | 輕量 2D／3D 參數建模與約束式零件設計 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 選穩定版；官方提醒 edge 建置可能有嚴重錯誤，6DOF 控制器支援也有平台差異。 | [official-docs-reviewed](https://github.com/solvespace/solvespace) / 2026-09-12 |

## electronics-design

**電子電路與電氣設計**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [KiCad](https://www.kicad.org/) | 電路圖、PCB 佈線與 Gerber／IPC-2581 製造輸出 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 元件庫、封裝、電氣規則及板廠製程限制須自行驗證；不保證 Altium 專案完整轉換。 | [official-docs-reviewed](https://www.kicad.org/about/kicad/) / 2026-09-12 |
| [QElectroTech](https://qelectrotech.org/) | 工業電氣、配線、液壓與氣壓系統圖面繪製 | macos, windows, linux · 桌面軟體 | 免費開源 · GNU GPL; see project license | 圖面工具不等同電氣模擬或完整 EPLAN 工程資料管理；元件符號與交付規範需核對。 | [official-docs-reviewed](https://qelectrotech.org/) / 2026-09-12 |

## animation-2d

**2D 動畫與向量動態**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [OpenToonz](https://github.com/opentoonz/opentoonz) | 傳統 2D 動畫製作與繪製，源於 Toonz 的動畫工作流程 | macos, windows, linux · 桌面軟體 | 免費開源 · BSD-3-Clause core; bundled components have separate licenses | 學習成本與專案交換需評估；官方只承認 opentoonz.github.io 與 GitHub 為官方來源，第三方筆刷與元件授權分開。 | [official-docs-reviewed](https://github.com/opentoonz/opentoonz) / 2026-09-12 |
| [Synfig Studio](https://github.com/synfig/synfig) | 向量與點陣素材的 2D 補間動畫 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 先以角色與鏡頭樣本測試，不能把自動補間當成完成表演動畫，也不保證 Moho 或 Animate 專案相容。 | [official-docs-reviewed](https://github.com/synfig/synfig) / 2026-09-12 |
| [Pencil2D](https://github.com/pencil2d/pencil) | 入門手繪逐格動畫，可搭配點陣與向量素材 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 複雜長片、團隊協作和商用動畫檔案交換需另評估；nightly 版本穩定度較低。 | [official-docs-reviewed](https://github.com/pencil2d/pencil) / 2026-09-12 |
| [Glaxnimate](https://glaxnimate.org/) | 向量補間動畫、Lottie、動態 SVG、GIF 與 WebP 素材 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0-or-later | Lottie 播放器支援度各異；先在目標 App 或網頁試播，不等同完整 After Effects 合成。 | [official-docs-reviewed](https://glaxnimate.org/) / 2026-09-12 |

## game-development

**遊戲與互動開發**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Godot Engine](https://github.com/godotengine/godot) | 2D／3D 遊戲、互動展示與跨平台應用開發 | macos, windows, linux · 桌面軟體 | 免費開源 · MIT | 引擎免權利金不代表主機移植、商店帳號與素材免費；Unity 專案仍需重新整合與測效能。 | [official-docs-reviewed](https://raw.githubusercontent.com/godotengine/godot/master/README.md) / 2026-09-12 |
| [GDevelop](https://github.com/4ian/GDevelop) | 以事件與模組化行為製作 2D／3D 遊戲和互動原型 | macos, windows, linux · 桌面軟體 | 開源編輯器／引擎；線上服務與素材可能另計 · MIT core/editor/engine | 編輯器與引擎開源；線上服務、商業支援、素材與託管功能另外計價或限額。 | [official-docs-reviewed](https://github.com/4ian/GDevelop) / 2026-09-12 |
| [LÖVE](https://love2d.org/) | 以 Lua 撰寫 2D 遊戲、互動原型與遊戲教學 | macos, windows, linux · 開發引擎 | 免費開源 · Zlib | 這是程式框架，需要自己寫遊戲邏輯與整合工具；行動平台封裝流程需另做。 | [official-docs-reviewed](https://love2d.org/) / 2026-09-12 |
| [libGDX](https://libgdx.com/) | 使用 Java 開發可跨桌面、手機與網頁的 2D／3D 遊戲 | macos, windows, linux · 開發引擎 | 免費開源 · Apache-2.0 | 需 Java 與建置工具能力；框架不等同完整可視化編輯器，各平台 SDK 與上架條件另計。 | [official-docs-reviewed](https://libgdx.com/) / 2026-09-12 |

## music-production

**音樂製作、樂譜與 DJ**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Ardour](https://ardour.org/) | 多軌音訊與 MIDI 錄製、剪輯、混音及影片配樂同步 | macos, windows, linux · 桌面軟體 | 開源；官方預編譯版收費，可自行從原始碼建置 · GPL-2.0 | 官方預編譯版本付費；原始碼可自行建置但 Mac／Windows 建置較複雜，音效外掛相容性需測。 | [official-docs-reviewed](https://ardour.org/) / 2026-09-12 |
| [LMMS](https://github.com/LMMS/lmms) | 鋼琴捲軸編曲、節拍樣式、合成器與混音製作 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 以編曲與音源製作為主；錄音、外掛格式與跨平台相容性需另外確認，不能套用完整 FL Studio 工作流。 | [official-docs-reviewed](https://github.com/LMMS/lmms) / 2026-09-12 |
| [MuseScore Studio](https://github.com/musescore/MuseScore) | 樂譜編輯、MIDI 輸入、MusicXML 交換與列印 PDF | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 免費桌面編譜器與 MuseScore.com 訂閱、樂譜取得及額外音源分開看；匯入後仍需校對排版。 | [official-docs-reviewed](https://github.com/musescore/MuseScore) / 2026-09-12 |
| [Hydrogen](https://github.com/hydrogen-music/hydrogen) | 鼓組樣式編排、鼓機、MIDI／OSC 控制與現場節奏循環 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0-or-later | 聚焦打擊節奏；需另外確認鼓組取樣授權與 DAW 同步，不能代替完整錄音工作站。 | [official-docs-reviewed](https://github.com/hydrogen-music/hydrogen) / 2026-09-12 |
| [Mixxx](https://mixxx.org/) | 多唱盤 DJ 混音、節拍同步、控制器映射、錄音與直播 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 需核對控制器型號與映射，既有曲庫能讀取不代表所有 cue 點與資料可完整遷移；音樂來源授權另計。 | [official-docs-reviewed](https://mixxx.org/features/) / 2026-09-12 |
| [Qtractor](https://qtractor.org/) | Linux 家庭錄音室的多軌音訊／MIDI 編排、錄音與混音 | linux · 桌面軟體 | 免費開源 · GPL-2.0-or-later | 目標平台為 Linux，依賴 JACK 與 ALSA；不能列為 Mac 或 Windows 原生替代品。 | [official-docs-reviewed](https://qtractor.org/) / 2026-09-12 |
| [Sonic Visualiser](https://www.sonicvisualiser.org/) | 音樂錄音的波形、特徵視覺化與研究註記 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0-or-later | Vamp 分析外掛需另裝；官方說不支援 VST、AudioUnit、LV2，定位是分析而非完整 DAW。 | [official-docs-reviewed](https://www.sonicvisualiser.org/) / 2026-09-12 |
| [Sonic Pi](https://sonic-pi.net/) | 用程式碼即時創作音樂、合成音色與教學示範 | macos, windows, linux · 桌面軟體 | 免費開源 · MIT main code; GPL-3.0 obligations for bundled GUI binaries | 需學習即時編碼；不能當成傳統時間軸 DAW，主程式、GUI 相依元件與教材各有授權。 | [official-docs-reviewed](https://github.com/sonic-pi-net/sonic-pi) / 2026-09-12 |

## scientific-computing

**統計分析與科學計算**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [GNU Octave](https://octave.org/) | 矩陣運算、數值分析、2D／3D 繪圖與相容部分 MATLAB 腳本 | macos, windows, linux · 桌面軟體 | 免費開源 · GNU GPL | 只保證部分語法相近；MATLAB Toolbox、Simulink 與專有函式不能假定可直接執行，Mac 安裝依官方 wiki。 | [official-docs-reviewed](https://octave.org/) / 2026-09-12 |
| [Scilab](https://www.scilab.org/) | 科學數值計算、訊號處理、控制系統與 Xcos 動態系統建模 | macos, windows, linux · 桌面軟體 | 免費開源 · GNU GPL | 語言、外掛與模擬器需重新驗證；既有 MATLAB／Simulink 檔案不能當成即開即用。 | [official-docs-reviewed](https://www.scilab.org/about) / 2026-09-12 |
| [JASP](https://github.com/jasp-stats/jasp-desktop) | 圖形介面的傳統與貝氏統計分析、研究表格與報告 | macos, windows, linux · 桌面軟體 | 免費開源 · AGPL-3.0 | 統計方法與模組覆蓋需逐項比對，資料編碼、遺漏值及模型假設仍由研究者判斷。 | [official-docs-reviewed](https://jasp-stats.org/) / 2026-09-12 |
| [jamovi](https://github.com/jamovi/jamovi) | 以試算表介面執行統計分析，產生 R 語法並擴充分析模組 | macos, windows, linux · 桌面軟體 | 免費開源 · AGPL-3.0; engine/common components GPL-2.0-or-later | 僅代表方法候選；SPSS syntax、附加模組與研究結果需逐項重現，雲端服務與桌面版分開核對。 | [official-docs-reviewed](https://www.jamovi.org/about.html) / 2026-09-12 |

## gis-mapping

**GIS 與地圖製作**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [QGIS](https://qgis.org/) | 地理資料編修、空間分析、地圖製作與可重現的處理流程 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 座標系統、資料來源授權與外掛需核對；ArcGIS 專有地理資料庫、企業權限與雲端服務另評估。 | [official-docs-reviewed](https://qgis.org/project/overview/) / 2026-09-12 |

## science-education

**科學影像、化學與天文教育**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Stellarium](https://stellarium.org/) | 桌面星空模擬、觀星規劃、時間變化與天文教學 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 望遠鏡控制與外掛依硬體確認；此列為桌面開源專案，不混入同名手機 App 的付費功能。 | [official-docs-reviewed](https://stellarium.org/) / 2026-09-12 |
| [Avogadro 2](https://www.openchemistry.org/projects/avogadro2/) | 分子結構編輯、3D 化學視覺化與計算化學前處理 | macos, windows, linux · 桌面軟體 | 免費開源 · BSD-3-Clause | 視覺化軟體不等同所有量子化學計算引擎；外部程式、資料格式與力場結果需另外驗證。 | [official-docs-reviewed](https://www.openchemistry.org/projects/avogadro2/) / 2026-09-12 |
| [ImageJ](https://imagej.net/ij/) | 科學影像量測、區域統計、堆疊影像處理與外掛擴充 | macos, windows, linux · 桌面軟體 | 免費開源 · Public domain core; plugins have separate licenses | 量測需校正與驗證；核心公有領域不代表所有外掛同授權，Fiji 發行套件不另外重複計數。 | [official-docs-reviewed](https://imagej.net/ij/docs/intro.html) / 2026-09-12 |

## project-management

**專案管理與看板**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [OpenProject Community](https://github.com/opf/openproject) | 甘特圖、專案排程、任務與工時預算管理 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-3.0 | Enterprise 附加功能與官方代管另計；需自管伺服器、資料庫及備份。 | [official-docs-reviewed](https://github.com/opf/openproject/blob/dev/README.md) / 2026-09-12 |
| [Taiga](https://github.com/taigaio/taiga-back) | 敏捷團隊的 Scrum 衝刺、Kanban 看板與問題追蹤 | web · 需自架 | 開源；自架、維護與選購服務另計 · MPL-2.0 | 需部署前後端與相依服務；Jira 自訂流程及整合要逐項重建，代管另計。 | [official-docs-reviewed](https://github.com/taigaio/taiga-back/blob/main/README.md) / 2026-09-12 |
| [Kanboard](https://github.com/kanboard/kanboard) | 輕量看板與工作進度管理 | web · 需自架 | 開源；自架、維護與選購服務另計 · MIT | 官方明列 maintenance mode，主要接受小修與社群貢獻；需自架 PHP 環境，不宜期待大量新功能。 | [official-docs-reviewed](https://github.com/kanboard/kanboard/blob/main/README.md) / 2026-09-12 |
| [WeKan](https://github.com/wekan/wekan) | 以共享卡片和清單管理團隊工作 | web · 需自架 | 開源；自架、維護與選購服務另計 · MIT | 需管理 MongoDB、更新及備份；官方建議正式伺服器至少 4 GB RAM，不能只算零授權費。 | [official-docs-reviewed](https://github.com/wekan/wekan/blob/main/README.md) / 2026-09-12 |
| [Plane Community](https://github.com/makeplane/plane) | 議題、週期、模組與產品路線圖管理 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 | 需部署 Docker／Kubernetes 與相依服務；遷移前驗證所需功能是否在 Community 版本，不能用雲端展示推定全部免費。 | [official-docs-reviewed](https://github.com/makeplane/plane/blob/preview/README.md) / 2026-09-12 |

## crm

**客戶關係與銷售管理**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [SuiteCRM](https://github.com/SuiteCRM/SuiteCRM) | 管理客戶關係、銷售資料與 CRM 工作流程 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 | 7 與 8 的功能與遷移路徑不同；需 PHP／資料庫管理，官方代管及支援另計。 | [official-docs-reviewed](https://github.com/SuiteCRM/SuiteCRM/blob/hotfix/README.md) / 2026-09-12 |
| [EspoCRM](https://github.com/espocrm/espocrm) | 潛在客戶、商機、聯絡人與客服案件管理 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 | 核心開源；報表、BPM 等擴充屬額外套件，需核對方案；自架主機與維護另計。 | [official-docs-reviewed](https://github.com/espocrm/espocrm/blob/master/README.md) / 2026-09-12 |
| [Frappe CRM](https://github.com/frappe/crm) | 用商機看板、活動紀錄與自訂檢視管理銷售 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 | 需要 Frappe 環境與資料庫；雲端代管另計，不能視為完整行銷自動化或 ERP。 | [official-docs-reviewed](https://github.com/frappe/crm/blob/develop/README.md) / 2026-09-12 |

## erp

**ERP 與進銷存**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [ERPNext](https://github.com/frappe/erpnext) | 整合採購、庫存、製造、會計與專案資料 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-3.0 | 需要導入、清理資料及自架維護；台灣稅務、電子發票與薪資適用性未驗證，不能直接替換本地財會系統。 | [official-docs-reviewed](https://github.com/frappe/erpnext/blob/develop/README.md) / 2026-09-12 |
| [Dolibarr](https://github.com/Dolibarr/dolibarr) | 中小企業報價、訂單、發票與庫存管理 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-3.0-or-later | 代管與部分模組可能付費；需部署 PHP／資料庫，台灣電子發票及在地財會流程尚未驗證。 | [official-docs-reviewed](https://github.com/Dolibarr/dolibarr/blob/develop/README.md) / 2026-09-12 |
| [Odoo Community](https://github.com/odoo/odoo) | 以社群版模組整合 CRM、庫存及企業作業 | web · 需自架 | 開源；自架、維護與選購服務另計 · LGPL-3.0 (Community); Enterprise/apps have separate licenses | 只計 Community；Enterprise 與部分 Apps 是其他授權且可能付費，需逐模組核對；導入、主機、在地化另計。 | [official-docs-reviewed](https://github.com/odoo/odoo/blob/19.0/README.md) / 2026-09-12 |

## web-analytics

**網站分析**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Matomo On-Premise Community](https://github.com/matomo-org/matomo) | 網站流量、事件、活動來源與電子商務追蹤 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-3.0-or-later | 自架需 PHP／MySQL；熱圖、錄影、漏斗等屬 Premium 功能，授權免費不代表整套功能免費。 | [official-docs-reviewed](https://github.com/matomo-org/matomo/blob/6.x-dev/README.md) / 2026-09-12 |
| [Umami](https://github.com/umami-software/umami) | 以簡潔儀表板查看流量、活動來源與轉換 | web · 需自架 | 開源；自架、維護與選購服務另計 · MIT | 需 Node.js／PostgreSQL 與追蹤碼；分析模型及匯入能力須自行驗證，不能假設可無損搬入 GA 歷史報表。 | [official-docs-reviewed](https://github.com/umami-software/umami/blob/master/README.md) / 2026-09-12 |
| [Plausible Community Edition](https://github.com/plausible/analytics) | 自架輕量網站流量與目標轉換統計 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0-or-later; tracker MIT | CE 缺雲端的行銷漏斗、營收目標、SSO 與 Sites API；需維護 PostgreSQL／ClickHouse，且新功能更新較慢。 | [official-docs-reviewed](https://github.com/plausible/analytics/blob/master/README.md) / 2026-09-12 |

## business-intelligence

**商業智慧與儀表板**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Metabase Open Source](https://github.com/metabase/metabase) | 讓團隊以視覺查詢或 SQL 建立資料儀表板 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL (OSS edition); enterprise directory commercial | 只計 OSS 版本；enterprise 目錄及企業映像受商業授權，資料連接、權限與維護需自行設定。 | [official-docs-reviewed](https://github.com/metabase/metabase/blob/master/README.md) / 2026-09-12 |
| [Apache Superset](https://github.com/apache/superset) | 連接資料庫，製作圖表、SQL 分析與互動儀表板 | web · 需自架 | 開源；自架、維護與選購服務另計 · Apache-2.0 | 需建立資料來源連線並維護伺服器；不含現成企業資料倉儲，也未驗證 Power BI／Tableau 報表匯入。 | [official-docs-reviewed](https://github.com/apache/superset/blob/master/README.md) / 2026-09-12 |

## forms-surveys

**表單與問卷**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [LimeSurvey Community](https://github.com/LimeSurvey/LimeSurvey) | 分支邏輯、多語問卷與研究調查 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-2.0-or-later | 自架需 PHP／資料庫與寄信服務；複雜問卷要測試跳題，Cloud 方案及維運成本另計。 | [official-docs-reviewed](https://github.com/LimeSurvey/LimeSurvey/blob/master/README.md) / 2026-09-12 |
| [OpnForm Community](https://github.com/OpnForm/OpnForm) | 建立表單、條件邏輯、嵌入及提交通知 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 (core); enterprise directory proprietary | api/app/Enterprise 使用專有授權，不能把全部功能算進免費核心；需維護 Laravel／Nuxt、資料庫及郵件。 | [official-docs-reviewed](https://github.com/OpnForm/OpnForm/blob/main/README.md) / 2026-09-12 |

## ecommerce

**電商與購物車**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [WooCommerce](https://github.com/woocommerce/woocommerce) | 在 WordPress 上銷售實體商品與數位產品 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-3.0 | 需要 WordPress 主機；訂閱、預約及會員等可能靠付費擴充，金流手續費與台灣物流／電子發票串接另計。 | [official-docs-reviewed](https://github.com/woocommerce/woocommerce/blob/trunk/README.md) / 2026-09-12 |
| [PrestaShop](https://github.com/PrestaShop/PrestaShop) | 自架商店、商品目錄與購物車 | web · 需自架 | 開源；自架、維護與選購服務另計 · OSL-3.0 core; AFL-3.0 modules | 需要 PHP／MySQL 主機；主題、模組及金物流服務另核價，正式環境應用穩定版，非 develop 分支。 | [official-docs-reviewed](https://github.com/PrestaShop/PrestaShop/blob/develop/README.md) / 2026-09-12 |
| [Medusa Core](https://github.com/medusajs/medusa) | 以可客製的電商模組建立商店與 B2B 交易流程 | web · 需自架 | 開源；自架、維護與選購服務另計 · MIT core; designated Enterprise materials commercial | 需工程師組裝前台及整合金物流；核心 MIT，RBAC Enterprise 材料另有商業授權，雲端主機另計。 | [official-docs-reviewed](https://github.com/medusajs/medusa/blob/develop/README.md) / 2026-09-12 |
| [Saleor](https://github.com/saleor/saleor) | GraphQL 電商後端及多通路商品、價格與庫存 | web · 需自架 | 開源；自架、維護與選購服務另計 · BSD-3-Clause | API 為主，需另部署或開發前台／Dashboard 並串接金流；雲端代管與維護成本另計。 | [official-docs-reviewed](https://github.com/saleor/saleor/blob/main/README.md) / 2026-09-12 |

## helpdesk

**客服與工單**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Zammad](https://github.com/zammad/zammad) | 彙整 Email、聊天與其他管道的客服案件 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 | 需部署及維護客服伺服器、郵件和整合；官方雲端及支援另計，先驗證既有工單匯入。 | [official-docs-reviewed](https://github.com/zammad/zammad/blob/develop/README.md) / 2026-09-12 |
| [osTicket](https://github.com/osTicket/osTicket) | 將郵件、電話及網頁需求整理成可分派工單 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-2.0 | 需 PHP／MySQL 和郵件設定；重點是工單管理，不能推定具備完整即時聊天、AI 或全通路行銷。 | [official-docs-reviewed](https://github.com/osTicket/osTicket/blob/develop/README.md) / 2026-09-12 |
| [FreeScout](https://github.com/freescout-help-desk/freescout) | 用共享信箱分派客服、內部備註與追蹤對話 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 | 核心與外加模組須分開估價；多種整合／進階功能透過模組提供，主機、郵件與維護仍有成本。 | [official-docs-reviewed](https://github.com/freescout-help-desk/freescout/blob/dist/README.md) / 2026-09-12 |
| [Chatwoot Community](https://github.com/chatwoot/chatwoot) | 整合網站即時聊天與多管道客服收件匣 | web · 需自架 | 開源；自架、維護與選購服務另計 · MIT core; enterprise directory separate commercial terms | enterprise 目錄不屬 MIT 核心；AI、社群管道與外部服務要核對版本及用量費，需自架維護。 | [official-docs-reviewed](https://github.com/chatwoot/chatwoot/blob/develop/README.md) / 2026-09-12 |

## booking-scheduling

**預約與排程**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Easy!Appointments](https://github.com/alextselegidis/easyappointments) | 服務人員可預約時段、客戶管理與 Google 日曆同步 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-3.0 code; CC-BY-3.0 content | 需 PHP／MySQL、郵件及日曆設定；Premium 功能與專業服務另計，跨時區及預約規則要實測。 | [official-docs-reviewed](https://github.com/alextselegidis/easyappointments/blob/main/README.md) / 2026-09-12 |

## team-chat

**團隊通訊**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Zulip](https://github.com/zulip/zulip) | 以主題串整理同步及非同步團隊聊天 | web · 需自架 | 開源；自架、維護與選購服務另計 · Apache-2.0 | 自架需 Linux 伺服器與維護；與 Slack 討論習慣不同，匯入、整合及通知服務方案要另確認。 | [official-docs-reviewed](https://github.com/zulip/zulip/blob/main/README.md) / 2026-09-12 |

## wiki-knowledge

**團隊 Wiki 與知識庫**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [BookStack](https://www.bookstackapp.com/) | 以書籍、章節與頁面整理公司手冊及知識文件 | web · 需自架 | 開源；自架、維護與選購服務另計 · MIT | 需 PHP／資料庫主機；固定文件結構，不能直接取代 Notion 資料庫；官方主程式來源已指向 Codeberg。 | [official-docs-reviewed](https://github.com/BookStackApp/BookStack/blob/development/readme.md) / 2026-09-12 |
| [Wiki.js](https://github.com/requarks/wiki) | 架設團隊 Wiki、操作文件及知識頁面 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 | 需 Node.js、相容資料庫與權限設定；升級前核對支援版本，不能推定能原樣匯入所有 Confluence 巨集。 | [official-docs-reviewed](https://github.com/requarks/wiki/blob/main/README.md) / 2026-09-12 |
| [DokuWiki](https://github.com/dokuwiki/dokuwiki) | 不需資料庫的輕量文件 Wiki | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-2.0 | 仍需 PHP 網頁主機、備份及權限設定；外掛相容性與既有文件轉換要另外驗證。 | [official-docs-reviewed](https://github.com/dokuwiki/dokuwiki/blob/master/README) / 2026-09-12 |

## workflow-automation

**工作流程自動化**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Activepieces Community](https://github.com/activepieces/activepieces) | 以視覺流程串接 SaaS、Webhook 與 AI 服務 | web · 需自架 | 開源；自架、維護與選購服務另計 · MIT Community; enterprise features commercial | packages/ee 及 packages/server/api/src/app/ee 採商業授權；自架不免除第三方 API／模型費用，Zapier 流程需重建並檢查連接器覆蓋。 | [official-docs-reviewed](https://github.com/activepieces/activepieces/blob/main/README.md) / 2026-09-12 |
| [Node-RED](https://github.com/node-red/node-red) | 用流程節點連接 API、事件與裝置 | web · 需自架 | 開源；自架、維護與選購服務另計 · Apache-2.0 | 需 Node.js 執行環境；第三方節點維護品質不同，伺服器及 API 用量另計，流程需自行設計。 | [official-docs-reviewed](https://github.com/node-red/node-red/blob/main/README.md) / 2026-09-12 |

## email-marketing

**電子報與行銷自動化**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [listmonk](https://github.com/knadh/listmonk) | 自架電子報、訂閱名單與批次寄送管理 | web · 需自架 | 開源；自架、維護與選購服務另計 · AGPL-3.0 | 需 PostgreSQL 與郵件發送服務；SMTP 用量、退信處理與寄件網域聲譽另計，不能把大量寄信視為免費。 | [official-docs-reviewed](https://github.com/knadh/listmonk/blob/master/README.md) / 2026-09-12 |
| [Mautic](https://github.com/mautic/mautic) | 客戶分群、跨管道行銷活動與自動化流程 | web · 需自架 | 開源；自架、維護與選購服務另計 · GPL-3.0-or-later | 需要主機、排程、資料庫與郵件服務；正式使用穩定發行版，Git 開發分支不建議直接上線，遷移名單與流程須驗證。 | [official-docs-reviewed](https://github.com/mautic/mautic/blob/7.x/README.md) / 2026-09-12 |

## backup-recovery

**備份與還原**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [restic](https://github.com/restic/restic) | 加密增量備份到本機、SFTP 或物件儲存 | macos, windows, linux · 命令列 | 開源；安裝包、模型與服務費用另查 · BSD-2-Clause | 命令列工具；需自行安排排程、保管密碼及測試還原，雲端儲存與流量另計。 | [official-docs-reviewed](https://github.com/restic/restic) / 2026-09-12 |
| [BorgBackup（1.4 穩定系列）](https://github.com/borgbackup/borg) | 具壓縮、加密、去重的檔案歷史備份 | macos, linux · 命令列 | 開源；安裝包、模型與服務費用另查 · BSD-3-Clause | 正式資料選 1.4 穩定系列；主線 Borg 2 仍為測試版，不應用於正式備份。遠端主機與空間需自備。 | [official-docs-reviewed](https://github.com/borgbackup/borg) / 2026-09-12 |
| [Kopia](https://github.com/kopia/kopia) | 以圖形介面或 CLI 建立加密、去重的檔案快照 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · Apache-2.0 | 備份檔案與資料夾，不是整機磁碟映像；儲存空間另計，透過 rclone 的部分整合仍屬實驗。 | [official-docs-reviewed](https://github.com/kopia/kopia) / 2026-09-12 |
| [Duplicati（開源備份用戶端）](https://github.com/duplicati/duplicati) | 排程壓縮與加密備份，存往雲端或遠端檔案伺服器 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT（排除 proprietary/ 與另有授權元件） | 開源用戶端不含雲端空間；需驗證還原。MIT 範圍排除 proprietary 目錄與另有授權的元件。 | [official-docs-reviewed](https://github.com/duplicati/duplicati) / 2026-09-12 |

## database-clients

**資料庫查詢與管理**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [DBeaver Community](https://github.com/dbeaver/dbeaver) | 以 SQL 編輯器管理多種關聯資料庫、匯入匯出資料 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · Apache-2.0 | 本項僅計 Community；特定非 JDBC 資料源與進階功能屬商業版，AI 供應商、資料庫及雲端費用另計。 | [official-docs-reviewed](https://github.com/dbeaver/dbeaver) / 2026-09-12 |
| [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) | 以表格介面建立、查詢及修改 SQLite 檔案 | macos, windows, linux · 桌面軟體 | 免費開源 · MPL-2.0 或 GPL-3.0-or-later；附帶元件另列 | 主要處理 SQLite；不是通用遠端資料庫管理器，也不等同 Excel 公式與試算表功能。 | [official-docs-reviewed](https://github.com/sqlitebrowser/sqlitebrowser) / 2026-09-12 |
| [Beekeeper Studio Community](https://github.com/beekeeper-studio/beekeeper-studio) | 以 SQL 編輯器管理 PostgreSQL、MySQL、SQLite 等資料庫 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0-or-later（Community；不含 src-commercial） | 只收錄 GPL 社群版；src-commercial 為商業原始碼可見授權，Oracle、DuckDB 等支援需核對付費方案。 | [official-docs-reviewed](https://github.com/beekeeper-studio/beekeeper-studio) / 2026-09-12 |

## developer-tools

**程式編輯與 API 開發**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [VSCodium](https://github.com/VSCodium/vscodium) | 使用去除微軟品牌與預設遙測設定的 VS Code 社群成品 | macos, windows, linux · 桌面軟體 | 免費開源 · MIT | 預設使用 Open VSX；部分微軟外掛僅授權官方 VS Code，不保證除錯器與全部外掛可移轉。 | [official-docs-reviewed](https://github.com/VSCodium/vscodium) / 2026-09-12 |
| [Zed](https://github.com/zed-industries/zed) | 程式編輯、協作與外部 AI 模型／代理整合 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0-or-later（標示元件為 Apache-2.0） | 編輯器免費；託管 AI、Pro 與團隊管理分別有費用，自備 API 金鑰仍需付模型費。 | [official-docs-reviewed](https://github.com/zed-industries/zed) / 2026-09-12 |
| [Neovim](https://github.com/neovim/neovim) | 可用 Lua／外掛擴充的鍵盤導向程式編輯器 | macos, windows, linux · 命令列 | 免費開源 · Apache-2.0 與 Vim license | 需要學習模態編輯；語言伺服器、除錯器與 AI 外掛需另行設定，不能直接視為完整商業 IDE。 | [official-docs-reviewed](https://github.com/neovim/neovim) / 2026-09-12 |
| [Geany](https://github.com/geany/geany) | 輕量 IDE，提供語法標色、程式補全及建置操作 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 適合一般程式編輯；特定語言工具鏈與外掛需自備，進階重構及框架支援要以專案試用確認。 | [official-docs-reviewed](https://github.com/geany/geany) / 2026-09-12 |
| [Bruno（開源版）](https://github.com/usebruno/bruno) | API 請求與測試保存在本機檔案，可用 Git 協作 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | 無內建雲端同步；官方商業版有額外功能，不能把付費版功能一併算入開源版。 | [official-docs-reviewed](https://github.com/usebruno/bruno) / 2026-09-12 |
| [Hoppscotch Community](https://github.com/hoppscotch/hoppscotch) | 使用網頁或桌面介面測試 REST、GraphQL 與 WebSocket API | macos, windows, linux, web · 網頁服務 | 開源；安裝包、模型與服務費用另查 · MIT | 瀏覽器跨來源連線可能需要代理或外掛；自架、託管及 Enterprise 功能與費用需分開確認。 | [official-docs-reviewed](https://github.com/hoppscotch/hoppscotch) / 2026-09-12 |

## device-integration

**手機與裝置整合**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [scrcpy](https://github.com/Genymobile/scrcpy) | 把 Android 畫面與聲音鏡像到電腦並以鍵鼠控制 | macos, windows, linux · 桌面軟體 | 免費開源 · Apache-2.0 | 目標需 Android 5+，音訊轉送需 Android 11+；通常需 USB 偵錯，不支援 iPhone 鏡像。 | [official-docs-reviewed](https://github.com/Genymobile/scrcpy) / 2026-09-12 |
| [KDE Connect](https://github.com/KDE/kdeconnect-kde) | 讓手機與電腦共享檔案、剪貼簿及通知，提供遙控功能 | macos, windows, linux, android, ios · 桌面軟體 | 免費開源 · GPL-2.0 與 GPL-3.0（依元件） | 裝置需配對；不同系統的通知、背景執行與控制能力不一致，iOS 不能假設具備 Android 全部功能。 | [official-docs-reviewed](https://github.com/KDE/kdeconnect-kde) / 2026-09-12 |
| [App Manager](https://github.com/MuntashirAkon/AppManager) | 查看 Android 應用程式權限、追蹤元件、APK 與使用資訊 | android · 行動 App | 免費開源 · GPL-3.0-or-later | 完整應用資料備份與元件封鎖需 root；部分權限及凍結操作需 root／ADB，無 root 不代表可用全部功能。 | [official-docs-reviewed](https://github.com/MuntashirAkon/AppManager) / 2026-09-12 |

## file-management

**檔案管理與去重**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Double Commander](https://github.com/doublecmd/doublecmd) | 雙窗格檔案管理，整理大量目錄與檔案 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 受到 Total Commander 啟發，但外掛、快捷鍵與平台行為不能直接視為完全相容。 | [official-docs-reviewed](https://github.com/doublecmd/doublecmd) / 2026-09-12 |
| [Krokiet（Czkawka 專案）](https://github.com/qarmin/czkawka) | 找重複檔、相似圖片、空資料夾與大型檔案 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0-only（Krokiet；其他元件另見各目錄） | 舊 Czkawka GTK 前端停止新增發行，改用 Krokiet；相似影片需 FFmpeg，RAW／HEIF 支援依建置而異，刪除前人工確認。 | [official-docs-reviewed](https://github.com/qarmin/czkawka) / 2026-09-12 |

## local-ai

**本機 AI 與模型工具**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Jan](https://github.com/janhq/jan) | 下載本機模型對話，或連接雲端 API 與自訂助手 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · Apache-2.0 | 離線僅適用本機模型路徑；模型需另下載並核對授權，RAM／GPU 影響速度，雲端 API 另收費。 | [official-docs-reviewed](https://github.com/janhq/jan) / 2026-09-12 |
| [GPT4All](https://github.com/nomic-ai/gpt4all) | 在桌機執行本機 LLM，透過 LocalDocs 查詢文件 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT（模型授權另外核對） | 模型檔需另下載並核對授權；Linux 官方成品為 x86-64，CPU 可跑不代表大型模型速度足夠。 | [official-docs-reviewed](https://github.com/nomic-ai/gpt4all) / 2026-09-12 |
| [Ollama](https://github.com/ollama/ollama) | 下載及執行模型，透過 CLI／API 串接其他 AI 工具 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT（模型授權另外核對） | 本機與雲端模式不同；要全本機需停用雲端功能，模型授權、記憶體／GPU 與雲端額度另外核對。 | [official-docs-reviewed](https://github.com/ollama/ollama) / 2026-09-12 |

## network-monitoring

**DNS 與網路監控**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) | 自架 DNS 過濾器，在網路層阻擋廣告與追蹤網域 | linux, windows, macos, web · 需自架 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | 要有常駐主機並設定 DNS；無法阻擋與內容共用網域的 YouTube／Twitch 廣告，不能等同完整網頁內容攔截。 | [official-docs-reviewed](https://github.com/AdguardTeam/AdGuardHome) / 2026-09-12 |
| [Pi-hole](https://github.com/pi-hole/pi-hole) | 以自有 Linux 主機集中管理網域封鎖與 DNS 查詢統計 | linux, web · 需自架 | 開源；安裝包、模型與服務費用另查 · EUPL-1.2（Core；其他元件依各授權） | 需常駐 Linux 或容器環境並調整網路 DNS；網域過濾不能取代所有瀏覽器內容攔截，硬體及維護另計。 | [official-docs-reviewed](https://github.com/pi-hole/pi-hole) / 2026-09-12 |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | 監看網站、TCP、DNS 與服務可用性，提供告警及狀態頁 | web, linux, windows · 需自架 | 開源；安裝包、模型與服務費用另查 · MIT | 需自架並維護監控主機；資料目錄不支援 NFS。與被監控服務放同台，當機時可能一起失去告警能力。 | [official-docs-reviewed](https://github.com/louislam/uptime-kuma) / 2026-09-12 |

## personal-finance

**個人財務與記帳**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [GnuCash](https://github.com/Gnucash/gnucash) | 個人與小型企業的複式記帳，整理帳戶及收支 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 或 GPL-3.0；部分檔案有 OpenSSL 例外 | 需學習會計科目與複式記帳；台灣銀行匯入、稅務報表與電子發票流程尚未驗證，不能當作已在地化會計套裝。 | [official-docs-reviewed](https://github.com/Gnucash/gnucash) / 2026-09-12 |
| [Actual Budget](https://github.com/actualbudget/actual) | 本機優先的預算與個人收支管理，可加裝同步伺服器 | macos, windows, linux, web · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · MIT | 銀行串接需 actual-server 與第三方服務；官方列出的銀行區域不含台灣，不能保證自動抓取本地銀行。 | [official-docs-reviewed](https://github.com/actualbudget/actual) / 2026-09-12 |
| [Money Manager Ex](https://github.com/moneymanagerex/moneymanagerex) | 整理家庭收支、信用卡、資產及多帳戶現金流 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-2.0 | 本項核對桌面版；行動版相容性與同步方式另查，沒有驗證台灣網銀自動連線或公司稅務申報。 | [official-docs-reviewed](https://github.com/moneymanagerex/moneymanagerex) / 2026-09-12 |

## privacy-security

**隱私與安全防護**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [Cryptomator（桌面版）](https://github.com/cryptomator/cryptomator) | 先在本機加密檔案及檔名，再交給既有雲端同步 | macos, windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0（另提供商業授權） | 不提供雲端容量；手機免費版為唯讀，寫入需各平台授權，不能把桌面免費套用到手機完整功能。 | [official-docs-reviewed](https://github.com/cryptomator/cryptomator) / 2026-09-12 |
| [Portmaster](https://github.com/safing/portmaster) | 監看與阻擋個別程式連線，管理 DNS 及追蹤封鎖 | windows, linux · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · GPL-3.0 | 免費防火牆不含所有付費功能；連線歷史、頻寬統計及 SPN 隱私網路需另外核對方案，不支援 macOS。 | [official-docs-reviewed](https://github.com/safing/portmaster) / 2026-09-12 |

## remote-access

**遠端桌面與設備管理**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [RustDesk](https://github.com/rustdesk/rustdesk) | 跨平台遠端桌面，可自行架設中繼伺服器 | macos, windows, linux, android · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0 | 免費 OSS 伺服器與 Server Pro 不同；SSO、集中管理等方案功能需核對，伺服器與維護另計。 | [official-docs-reviewed](https://github.com/rustdesk/rustdesk) / 2026-09-12 |
| [Apache Guacamole](https://github.com/apache/guacamole-client) | 在瀏覽器集中連線 RDP、VNC 與 SSH 工作環境 | web · 需自架 | 開源；安裝包、模型與服務費用另查 · Apache-2.0 | 瀏覽器端免裝客戶端，但仍須部署閘道伺服器及目的端協定服務；主機與管理成本另計。 | [official-docs-reviewed](https://github.com/apache/guacamole-client) / 2026-09-12 |
| [MeshCentral](https://github.com/Ylianst/MeshCentral) | 自架電腦管理後台，提供遠端桌面、終端機及檔案操作 | web, windows, macos, linux · 需自架 | 開源；安裝包、模型與服務費用另查 · Apache-2.0 | 需架設伺服器並在受管電腦安裝 agent；TLS、帳號權限、更新與備份由管理者維護。 | [official-docs-reviewed](https://github.com/Ylianst/MeshCentral) / 2026-09-12 |

## rss-reference

**資訊訂閱與文獻管理**

| 工具 | 用途 | 平台／部署 | 費用／授權 | 限制 | 證據 |
|---|---|---|---|---|---|
| [FreshRSS](https://github.com/FreshRSS/FreshRSS) | 自架 RSS／Atom 訂閱中心，跨裝置閱讀與整理文章 | web · 需自架 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0 | 需部署 PHP／Web 伺服器及排程抓取；API 相容不等於所有付費閱讀器功能，主機與備份由自己負責。 | [official-docs-reviewed](https://github.com/FreshRSS/FreshRSS) / 2026-09-12 |
| [RSS Guard](https://github.com/martinrotter/rssguard) | 桌面 RSS／Atom／JSON Feed 閱讀，也可連接 FreshRSS 等服務 | macos, windows, linux · 桌面軟體 | 免費開源 · GPL-3.0 | 本機閱讀可直接使用；連接外部閱讀服務仍受該服務方案與 API 限制，跨裝置同步需額外後端。 | [official-docs-reviewed](https://github.com/martinrotter/rssguard) / 2026-09-12 |
| [Zotero](https://github.com/zotero/zotero) | 收集、整理、註記及引用研究文獻，管理 PDF 與書目 | macos, windows, linux, android, ios · 桌面軟體 | 開源；安裝包、模型與服務費用另查 · AGPL-3.0 | 書目資料同步免費不限量；附件雲端空間免費 300 MB，擴充需付費或另配 WebDAV，群組附件不能用 WebDAV。 | [official-docs-reviewed](https://github.com/zotero/zotero) / 2026-09-12 |
| [JabRef](https://github.com/JabRef/jabref) | 管理 BibTeX／BibLaTeX 書目，搜尋資料及插入引用 | macos, windows, linux · 桌面軟體 | 免費開源 · MIT | 以 .bib 文獻庫工作流為主；Word／LibreOffice 整合與既有書目欄位需試匯入，不能把文章取得當作全文授權。 | [official-docs-reviewed](https://github.com/JabRef/jabref) / 2026-09-12 |
