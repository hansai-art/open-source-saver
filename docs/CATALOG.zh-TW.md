# 開源與免費軟體清單

[繁體中文](CATALOG.zh-TW.md) · [English](CATALOG.en.md)

58 candidate products. Snapshot: 2026-09-10. No product workflow or Chinese-quality tests claimed.
候選清單，非完整替代保證；與文章發現名單有重疊，不能相加。

[Sources](SOURCES.md) · [JSON](../data/products.json) · [Contribute](../CONTRIBUTING.md)

## screen-recording

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [OBS Studio](https://github.com/obsproject/obs-studio) | 課程長錄影、直播、多場景與多音訊來源 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 不把錄影能力等同 Screen Studio 式自動運鏡；目前官方 Mac 版本要求 macOS 13+。 | official-docs-reviewed / 2026-09-10 |
| [Recordly](https://github.com/webadderallorg/Recordly) | 教學示範、產品 demo、自動縮放與游標動畫 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | Mac 14+；Linux 游標隱藏有限制。README 標 AGPL-3.0，LICENSE.md 另有品牌及署名文字，改版前要核對全文。 | official-docs-reviewed / 2026-09-10 |
| [Capptivo](https://github.com/SECHAK-AG/capptivo) | 跟隨游標縮放、點擊縮放、錄影標記及本機字幕 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | Mac 建置未簽署；字幕需另備 whisper-cli，首次下載模型；Mac 13+。附帶元件各有授權。 | official-docs-reviewed / 2026-09-10 |
| [Cap](https://github.com/CapSoftware/Cap) | Loom 式錄影分享與 Studio 模式的縮放、字幕、裁切 | macos, windows | 開源；安裝包、模型與服務費用另查 | 本機、雲端、自架及官方方案費用分開核對；不能把開源當成所有託管服務免費。 | official-docs-reviewed / 2026-09-10 |
| [Screenity](https://github.com/alyssaxuu/screenity) | 瀏覽器示範錄影、畫面註記、點擊與游標強調 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 瀏覽器錄影與原生桌面錄影有差異；免費外掛與 Screenity Pro 功能不可混用。 | official-docs-reviewed / 2026-09-10 |
| [OpenScreenStudio](https://github.com/Glyph-Software/OpenScreenStudio) | Mac 專用自動點擊縮放、游標覆蓋、攝影機泡泡與 MP4／GIF | macos | 開源；安裝包、模型與服務費用另查 | README 說基礎需求 Mac 13+，但實際 ScreenCaptureKit 錄影路徑需 Mac 15+；未公證，先小範圍試錄。 | official-docs-reviewed / 2026-09-10 |
| [Kap](https://github.com/wulkano/Kap) | 簡單區域錄影、快速製作短示範 | macos | 開源；安裝包、模型與服務費用另查 | 主 repo 最後推送時間為 2024-11，較久；新系統相容性待測，不列長課程主錄影首選。 | official-docs-reviewed / 2026-09-10 |
| [ScreenToGif](https://github.com/NickeManarin/ScreenToGif) | 短錄影與 GIF 編輯，適合教學步驟 | windows | 開源；安裝包、模型與服務費用另查 | 僅 Windows；不適合拿來代表 Mac 替代方案，也不是長課程剪輯系統。 | official-docs-reviewed / 2026-09-10 |
| [ScreenPal](https://screenpal.com/plans) | 短教學錄影 | macos, windows | 有功能限制的免費版；非開源 | 官網免費方案每段 15 分鐘，長課程優先選其他工具；不將所有行銷頁功能都當免費。 | official-docs-partial / 2026-09-10 |
| [FlashBack Express](https://www.flashbackrecorder.com/express) | 錄影候選 | windows | 免費與付費功能界線待查 | 官網確認 Windows 與本機儲存；文章對水印描述不一致，編輯與 AI 功能免費範圍尚待版本／方案表確認。 | official-docs-partial / 2026-09-10 |
| [macOS Screenshot / QuickTime](https://support.apple.com/en-us/102618) | 基本螢幕錄影 | macos | macOS 內建；非開源 | 不需另購錄影軟體；官方操作支援畫面與麥克風，不據此保證所有系統音訊需求。 | official-docs-partial / 2026-09-10 |
| [Screenify](https://www.imobie.com/screenify/) | 錄教學、螢幕加鏡頭、錄音後簡單修剪 | macos, windows | 免費軟體；非開源 | 官網稱免費、無錄影時間限制，支援本機輸出；FocuSee 的自動運鏡是另一產品。繁中與新款 Mac 尚未實測。 | official-docs-partial / 2026-09-10 |

## screenshots-ocr

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [ShareX](https://github.com/ShareX/ShareX) | 截圖、滾動擷取、箭頭文字、遮蔽、OCR 與後續自動化 | windows | 開源；安裝包、模型與服務費用另查 | 僅 Windows；自動上傳是可選工作流程，私密截圖應只選本機輸出。 | official-docs-reviewed / 2026-09-10 |
| [Flameshot](https://github.com/flameshot-org/flameshot) | 快速截圖並加箭頭、文字、框線等教學標記 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | Mac 上的快捷鍵與螢幕權限需實測；不是完整長截圖／素材管理工作台。 | official-docs-reviewed / 2026-09-10 |
| [ksnip](https://github.com/ksnip/ksnip) | 截圖編號、註解、釘選等說明圖用途 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 官方功能表顯示各平台不同；全域快捷鍵主要限 Windows／X11，OCR 外掛不是全平台相同。作者正在找共同維護者。 | official-docs-reviewed / 2026-09-10 |
| [Greenshot](https://github.com/greenshot/greenshot) | 輕量截圖、標示、局部遮蔽與輸出 | windows | 開源；安裝包、模型與服務費用另查 | 此 repo 是 Windows 版；不把同名 Mac 產品算進這個開源項目。 | official-docs-reviewed / 2026-09-10 |
| [NormCap](https://github.com/dynobo/normcap) | 從畫面擷取文字，減少手動抄寫 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | OCR 工具而非註解編輯器；中文辨識取決於 Tesseract 語言資料，繁中語料效果待測。 | official-docs-reviewed / 2026-09-10 |
| [Text Grab](https://github.com/TheJoeFin/Text-Grab) | 快速框選畫面轉成可複製文字 | windows | 開源；安裝包、模型與服務費用另查 | Windows 專用；OS OCR 語言及字型影響結果。 | official-docs-reviewed / 2026-09-10 |
| [Lightshot](https://app.prntscr.com/en/index.html) | 快速區域截圖與標註 | macos, windows | 免費軟體；非開源 | 有官方免費下載；網路分享會上傳截圖，不等於所有截圖都只留在本機。 | official-docs-partial / 2026-09-10 |

## dictation

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [Handy](https://github.com/cjpais/Handy) | 按快捷鍵說話，把文字輸入目前游標位置 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 先下載模型；不同模型支援語言不同，繁中情境應選支援中文的多語模型；藍牙麥克風可能影響播放音質。 | official-docs-reviewed / 2026-09-10 |
| [OpenWhispr](https://github.com/OpenWhispr/openwhispr) | 語音輸入、整理口述文字、會議與筆記 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 本機與雲端模式分開；選雲端模型可能有 API 費用；Intel Mac 部分說話者功能受限。 | official-docs-reviewed / 2026-09-10 |
| [VoiceInk](https://github.com/Beingpax/VoiceInk) | Mac 原生語音輸入，評估 Superwhisper／Wispr Flow 類用途 | macos | 開源；安裝包、模型與服務費用另查 | 原始碼開放但官方成品有試用及付費方案；自行建置需開發環境。文件 Mac 最低版本敘述有 14.0／14.4 差異，依成品要求核對。 | official-docs-reviewed / 2026-09-10 |
| [Whispering／Epicenter](https://github.com/EpicenterHQ/epicenter) | 錄音後轉文字、選擇轉錄供應商與可選潤飾 | macos, windows, linux, web | 開源；安裝包、模型與服務費用另查 | 舊 braden-w repo 已封存並搬移；桌面由 Epicenter 宿主提供，Web 與桌面能力不同；不能引用舊版 MIT 作新版授權。 | official-docs-reviewed / 2026-09-10 |
| [Apple Dictation](https://support.apple.com/guide/mac-help/use-dictation-mh40584/mac) | 將說話輸入文字欄位 | macos | macOS 內建；非開源 | 不是長音檔逐字稿工具；是否在裝置處理需查看鍵盤設定，語言與功能依系統而異。 | official-docs-partial / 2026-09-10 |

## transcription

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [Vibe](https://github.com/thewh1teagle/vibe) | 現成的音訊／影片本機轉錄，具說話者分離與時間戳相關功能 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 適合和你的 MOSS-ASR 比較現成工作流程；多人效果與專有名詞需同語料測試。 | official-docs-reviewed / 2026-09-10 |
| [Buzz](https://github.com/chidiwilliams/buzz) | 音訊影片或麥克風轉錄，輸出 TXT／SRT／VTT | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 選本機 backend 才符合離線要求；README 的安裝包入口指向 SourceForge。 | official-docs-reviewed / 2026-09-10 |
| [aTrain](https://github.com/aTrainTranscription/aTrain) | 研究訪談、離線逐字稿與說話者分離 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 主要現成發布通路是 Windows／Linux；Mac 不以一般一鍵安裝推薦；GPU 配置另計。 | official-docs-reviewed / 2026-09-10 |
| [WhisperX](https://github.com/m-bain/whisperX) | 字級時間戳對齊、多人逐字稿與字幕底層 | windows, linux | 開源；安裝包、模型與服務費用另查 | 不是現成桌面 App；說話者模組有模型下載與條款要求，重疊語音及中文對齊效果需驗證。 | official-docs-reviewed / 2026-09-10 |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | 本機 Whisper 推論，適合 Mac 端或現成工具串接 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 模型需要另備；引擎本身不是完整編輯、校對或多人標記工作台。 | official-docs-reviewed / 2026-09-10 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | 以 CTranslate2 執行 Whisper，適合大量轉錄 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | NVIDIA GPU 加速與 Mac Metal 不是同一條路線；不是可直接取代逐字稿網站的 UI。 | official-docs-reviewed / 2026-09-10 |
| [FunASR](https://github.com/modelscope/FunASR) | ASR、VAD、標點與說話者流程，補中文語音處理選擇 | 待確認 | 開源；安裝包、模型與服務費用另查 | 程式 MIT 不等於所有模型相同授權；需指定 checkpoint、硬體與模型條款。 | official-docs-reviewed / 2026-09-10 |
| [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | 離線 ASR／TTS／VAD／說話者與語音處理共用引擎 | macos, windows, linux, android, ios | 開源；安裝包、模型與服務費用另查 | 是整合底層，不算另一個現成 dictation App；不同模型能力及授權各自核對。 | official-docs-reviewed / 2026-09-10 |

## subtitles

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit) | 字幕校對、時間軸、轉格式與可選語音／翻譯服務 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 現行 repo 已有跨平台建置；Mac 推薦 14+，文件稱最低 12；下載時辨別 RC 與穩定版。線上服務可能付費。 | official-docs-reviewed / 2026-09-10 |
| [pyVideoTrans](https://github.com/jianchang512/pyvideotrans) | 轉錄、字幕翻譯、多角色配音、音畫對齊與影片合成 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | Windows 有預打包版；Mac／Linux 安裝較多設定。是否離線與費用依 ASR／LLM／TTS 選擇。 | official-docs-reviewed / 2026-09-10 |
| [VideoLingo](https://github.com/Huanshere/VideoLingo) | 影片翻譯、字幕分段對齊與配音 | 待確認 | 開源；安裝包、模型與服務費用另查 | 已有完整流程，值得先用；需配置環境與模型／API，不把作者的 Netflix 品質宣稱當作驗證結果。 | official-docs-reviewed / 2026-09-10 |

## text-to-speech

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [Readest](https://github.com/readest/readest) | 閱讀文件／電子書時使用 TTS 朗讀 | macos, windows, linux, android, ios, web | 開源；安裝包、模型與服務費用另查 | 是現成閱讀入口，不是 Obsidian 外掛或配音錄音室；音色、離線程度及費用依所用 TTS 服務。 | official-docs-reviewed / 2026-09-10 |
| [Piper（現行維護線）](https://github.com/OHF-Voice/piper1-gpl) | 低延遲本機文字朗讀，供既有閱讀工具接入 | 待確認 | 開源；安裝包、模型與服務費用另查 | 不是廣告表演級音色保證；聲音模型有各自授權，繁中發音與台灣口音待測。 | official-docs-reviewed / 2026-09-10 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | 中文與多語配音、聲音設計、聲音複製 | 待確認 | 開源；安裝包、模型與服務費用另查 | 適合本機或自架評估，不是 Mac 一鍵 App；長文穩定度、停頓與台灣口音要試聽。 | official-docs-reviewed / 2026-09-10 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 少量語音素材建立聲音模型、中文與跨語言配音 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 需要設定與素材；整合包、預訓練權重及附帶模型分開核對，不等於全程零設定。 | official-docs-reviewed / 2026-09-10 |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) | 多語聲音生成、聲音複製、中文發音控制 | 待確認 | 開源；安裝包、模型與服務費用另查 | 目前 repo 位於 QwenAudio；適合比較配音後端，Mac 部署與效能不作已支援承諾。 | official-docs-reviewed / 2026-09-10 |
| [Kokoro](https://github.com/hexgrad/kokoro) | 輕量本機 TTS，普通話與英文等語言朗讀 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | README 支援 Mandarin，不能推導為台灣口音；中文額外依賴與長文品質需測。 | official-docs-reviewed / 2026-09-10 |
| [eSpeak NG](https://github.com/espeak-ng/espeak-ng) | 低資源朗讀、輔助功能與發音處理 | windows, linux | 開源；安裝包、模型與服務費用另查 | 聲音較機械，適合功能性朗讀，不列商業形象片配音首選；Mac 整合另核對。 | official-docs-reviewed / 2026-09-10 |

## video-editing

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [Auto-Editor](https://github.com/WyattBlue/auto-editor) | 先剪掉靜音或低活動片段，再匯出到既有剪輯軟體 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 官方 README 已有 Skill 安裝入口；音量偵測不理解內容，會誤刪閱讀／操作停頓。商業 GUI 與此開源 CLI 不同。 | official-docs-reviewed / 2026-09-10 |
| [LosslessCut](https://github.com/mifi/lossless-cut) | 快速裁切長錄影、抽音軌與無重編碼處理 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 關鍵影格與格式限制會影響切點；不是完整 NLE，也不能靠 stream copy 燒字幕。 | official-docs-reviewed / 2026-09-10 |
| [Kdenlive](https://github.com/KDE/kdenlive) | 一般剪輯、多軌影片與字幕工作 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 適合新專案評估，不能保證 Premiere 專案／外掛完整遷移。現行下載頁 Mac 13+。 | official-docs-reviewed / 2026-09-10 |
| [Shotcut](https://github.com/mltframework/shotcut) | 一般剪接與多格式影片處理 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 客戶指定專案格式要另評估；現行 Mac 版為 12+，較舊 OS 有舊版下載。 | official-docs-reviewed / 2026-09-10 |
| [HandBrake](https://github.com/HandBrake/HandBrake) | 課程影片壓縮、轉 MP4／MKV／WebM 與裝置用格式 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 是轉碼器，不是時間軸剪輯器；不以多次轉碼替代保留高品質母檔。 | official-docs-reviewed / 2026-09-10 |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 批次轉檔、抽音訊、字幕燒錄與影音流程串接 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 使用現成命令即可；LGPL／GPL 取決於建置元件，不能用單一授權涵蓋所有 binary。 | official-docs-reviewed / 2026-09-10 |
| [Natron](https://github.com/NatronGitHub/Natron) | 節點式合成、摳像與 OpenFX 流程 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 不能打包宣稱完整替代 After Effects；Mac CPU 架構與版本相容性需核對下載包。 | official-docs-reviewed / 2026-09-10 |
| [Blender](https://github.com/blender/blender) | 沿用你既有 3D 能力，承接 3D、合成與部分影片工作 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 不是新發現的工具；保留作已安裝可重用選項，不把轉換現有商業專案的成本當零。 | official-docs-reviewed / 2026-09-10 |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | 剪輯、調色、音訊後製 | macos, windows, linux | 有免費版；非開源 | 有免費桌面版；Studio 的 AI、降噪等不算免費能力，格式支援需按素材核對。 | official-docs-partial / 2026-09-10 |

## audio-editing

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [Audacity](https://github.com/audacity/audacity) | 口播剪輯、多軌錄音與基本音訊整理 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 不等於完整取代 Audition 的所有專業工作流；本次 master 涉及新版開發，使用者應選穩定版。 | official-docs-reviewed / 2026-09-10 |
| [Ultimate Vocal Remover（UVR）](https://github.com/Anjok07/ultimatevocalremovergui) | 將人聲與伴奏分離，整理影片配音素材 | macos, windows, linux | 開源；安裝包、模型與服務費用另查 | 分離結果可能有殘留與音質損失；模型與 GUI 授權分開，不能承諾錄音修復百分百成功。 | official-docs-reviewed / 2026-09-10 |

## graphics

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [GIMP](https://www.gimp.org/) | 照片修整與點陣圖編輯 | macos, windows, linux | 免費開源 | 官網確認免費開源；能否替代特定 Photoshop 專案需用實際檔案確認。 | official-docs-partial / 2026-09-10 |
| [Krita](https://krita.org/en/) | 繪畫、筆刷與插畫 | macos, windows, linux | 免費開源 | 官網提供免費版本與繁中網站；不把網站翻譯當成已實測完整繁中 UI。 | official-docs-partial / 2026-09-10 |

## office

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [LibreOffice](https://www.libreoffice.org/) | 文件、試算表、簡報與 Draw | macos, windows, linux | 免費開源 | 官網確認免費開源；不沿用文章『完全相容』說法，正式交付檔案需驗證。 | official-docs-partial / 2026-09-10 |
| [ONLYOFFICE Desktop Editors](https://www.onlyoffice.com/desktop) | 文件、試算表、簡報與 PDF | macos, windows, linux | 免費開源桌面版 | 確認免費桌面產品；雲端協作方案、AI 提供者與付費服務另外核對。 | official-docs-partial / 2026-09-10 |

## pdf

| 工具 / Tool | 用途 / Use | 平台 / OS | 費用 / Cost | 限制 / Limits | 證據 / Evidence |
|---|---|---|---|---|---|
| [PDF24 Creator](https://tools.pdf24.org/en/creator) | PDF 合併、拆分、轉檔與 OCR | windows | 個人與商用免費 | 官網明列私人與商業使用免費，離線處理；桌面版沒有 macOS。 | official-docs-partial / 2026-09-10 |
