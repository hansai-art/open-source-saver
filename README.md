# 開源省錢管家 Open Source Saver

**找現成的開源與免費軟體，幫你評估付費工具能不能換。繁體中文優先，英文第二。**

[English](README.en.md) · [完整清單](docs/CATALOG.zh-TW.md) · [使用方式](docs/USAGE.zh-TW.md) · [Spec](docs/SPEC.zh-TW.md) · [文章來源](docs/SOURCES.md)

適合找螢幕錄影、截圖、OCR、語音輸入、逐字稿、字幕、TTS 配音、剪輯、修圖、Office、PDF 的替代方案。可作 Claude Code / Codex 等支援 Agent Skills 的工具參考；各宿主實際安裝與權限依其規範，並未全面實測。

## 它會做什麼

- **指定軟體**：「找 Screen Studio 的免費替代品，我要自動縮放和字幕。」
- **描述需求**：「我用 Mac，要免費的語音輸入工具，繁中優先。」
- **提供清單**：「依這份安裝清單，找可試用的替代品。」
- 先找內建功能和現成產品，區分開源、免費非開源、免費版、付費功能及部署負擔。
- 附官方入口、用途、限制與查核日期；不把找到替代品當成已經省錢。

**v0.1.0-alpha：58 個候選產品、14 組條件式對照、11 篇文章。** 另保留 53 個文章發現名稱，與產品清單重疊。無付費 API、無帳號、無雲端後端是本機工具的設計；使用雲端 AI 的費用與資料傳輸另計。

## 直接看清單，不安裝也能用

| 需求 | 清單入口／例子 |
|---|---|
| 螢幕錄影 | [錄影清單](docs/CATALOG.zh-TW.md#screen-recording)：OBS、Recordly、Capptivo、Screenify |
| 截圖／OCR | [截圖清單](docs/CATALOG.zh-TW.md#screenshots-ocr)：ShareX、Flameshot、NormCap、Lightshot |
| 語音輸入 | [聽寫清單](docs/CATALOG.zh-TW.md#dictation)：Handy、OpenWhispr、Apple Dictation |
| 逐字稿 | [轉錄清單](docs/CATALOG.zh-TW.md#transcription)：Vibe、Buzz、aTrain |
| 字幕／配音 | [字幕](docs/CATALOG.zh-TW.md#subtitles)、[TTS](docs/CATALOG.zh-TW.md#text-to-speech) |
| 剪輯／修圖／文書 | [影片](docs/CATALOG.zh-TW.md#video-editing)、[圖像](docs/CATALOG.zh-TW.md#graphics)、[Office](docs/CATALOG.zh-TW.md#office)、[PDF](docs/CATALOG.zh-TW.md#pdf) |

每款都有適用範圍。例：PDF24 Creator 桌面版僅 Windows；VoiceInk 開源不代表官方成品免費；DaVinci Resolve 免費版不含全部 Studio 功能。先看限制再下載。

## 安裝 Skill

取得整個專案資料夾，包含 SKILL.md、scripts、references、data；不要只複製 SKILL.md。

Claude Code 個人安裝（macOS／Linux，已安裝 Git）：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/hansai-art/open-source-saver.git ~/.claude/skills/open-source-saver
```

在 Claude Code 輸入：

```text
/open-source-saver 我用 Mac，找 Screen Studio 的免費替代品，需要自動縮放與字幕。
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

## 隱私與目前限制

- 附帶程式不連網，清單與報告直接寫本機，不自動印出內容。
- **嚴格離線時，不要把私人清單或報告貼進雲端 AI。** 本機掃描與雲端分析不是同一件事。
- 收集器為實驗性：未宣稱已完成 Mac／Windows 真機與完整平台驗收；可先用手動清單。
- 工具授權、免費限制與下載可能改變；快照查核日為 2026-09-10。所列第三方軟體均未由本專案完成工作流實測，繁中準確率也未測。
- 不自動安裝、卸載、取消訂閱；不從安裝清單猜費用。不宣稱百分百替代 Adobe／Office。

## 參與整理

[貢獻方式](CONTRIBUTING.md)：提供原付費工具、真正用途、候選、官方連結、平台、免費限制及繁中狀態。先用國外既有文章與目錄找候選，再核對官網；不要整包複製文章。

[MIT License](LICENSE) 適用本專案自製內容；第三方產品與文章保留原條款，見 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。作者：Hans 林思翰。

搜尋關鍵字：開源替代、免費軟體、付費軟體替代、螢幕錄影、截圖、語音轉文字、繁體中文、台灣、open source alternatives、free software、software inventory、Claude Code skill、Codex skill。

[實作與驗收狀態](docs/STATUS.md)

[v0.2 優化規格](docs/OPTIMIZATION.zh-TW.md)
