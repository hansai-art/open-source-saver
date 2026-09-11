# 使用方式

[English](USAGE.en.md) · [首頁](../README.md)

## 1. 先決定是否需要掃描

只找某款軟體替代品，直接問 Skill 或查清單即可。需要盤點才在真正目標電腦執行以下命令。雲端聊天環境無法藉此掃描你的 Mac／Windows。

以下命令均在專案根目錄執行。Python 需 3.10+；Windows 可用 py -3。沒有 Python 可先使用雙語清單，或交由已具備 runtime 的 Agent 處理手動資料；嚴格離線則不能上傳清單。

## 2. 最簡單：手動清單

在專案外建立私人資料夾，例如 Mac 的 ~/Documents/open-source-saver-private。建立 apps.txt，一行一個名稱。以下是虛構範例，不是實際掃描：

```text
Adobe Premiere Pro 2024
Microsoft Word
Screen Studio
Unknown Example App
```

也可使用 JSON（不要直接輸入 WinGet／system_profiler 原始格式）：

```json
{
  "applications": [
    {"name": "Microsoft Word", "version": "example"},
    {"display_name": "Snagit"}
  ]
}
```

```bash
python3 scripts/saver.py report --input ~/Documents/open-source-saver-private/apps.txt --platform macos --output ~/Documents/open-source-saver-private/report.md
```

打開本機 report.md 檢查候選與未配對項。它不會算費用、不會判定你正在訂閱。輸出檔存在會拒絕覆寫，請換名稱。

## 3. Mac 盤點（實驗性）

```bash
python3 scripts/collect_macos.py --output ~/Documents/open-source-saver-private/inventory.json
python3 scripts/saver.py report --input ~/Documents/open-source-saver-private/inventory.json --platform macos --output ~/Documents/open-source-saver-private/scan-report.md
```

只讀三個已知 App 目錄、最多兩層子資料夾。Homebrew formula、symlink App、其他資料夾、其他使用者與瀏覽器外掛可能漏掉。讀 metadata 的失敗會留下警告。不是全機覆蓋保證。

## 4. Windows 盤點（實驗性）

在 Windows PowerShell 執行，不需要系統管理員：

```powershell
$SaverPrivateDir = Join-Path $env:USERPROFILE 'Documents\open-source-saver-private'
powershell -NoProfile -File .\scripts\collect-windows.ps1 -OutputPath "$SaverPrivateDir\inventory.json"
py -3 .\scripts\saver.py report --input "$SaverPrivateDir\inventory.json" --platform windows --output "$SaverPrivateDir\report.md"
```

組織執行原則若禁止腳本，改用手動清單；不要為這個工具修改全機執行原則。收集範圍為可讀取的 HKLM／HKCU 安裝紀錄及目前使用者 Appx，免安裝程式可能漏掉。Appx 名稱可能是技術識別字，未配對時保留，不亂猜。

## 5. 搜尋與更多候選

```bash
python3 scripts/saver.py search "錄影" --platform macos
python3 scripts/saver.py search "語音輸入" --platform windows
python3 scripts/saver.py search "PDF" --platform windows
python3 scripts/saver.py search "transcription" --include-engines --json
python3 scripts/saver.py validate
```

可用分類：screen-recording、screenshots-ocr、dictation、transcription、subtitles、text-to-speech、video-editing、audio-editing、graphics、office、pdf。用 --lang en 切英文說明。引擎預設不列，但需配置的工具仍可能出現，請讀 delivery 與限制。

找不到時先參考 [文章來源](SOURCES.md) 和 data/discovery.json；不要把空結果當成市場上不存在替代品。發現新的工具不需要立即開發新的軟體。

## 6. 隱私與錯誤

本機腳本不發網路請求、不印原始清單。私人報告也可能揭露工作內容，請留在私人資料夾，避免提交到 GitHub。嚴格離線模式在本機終端機操作，不請雲端 AI 開啟結果。一般聊天查證官方網站則是連線模式。

錯誤處理：FileExistsError → 換輸出檔名；資料錯誤 → 檢查上述 JSON 或一行一個名稱；平台錯誤 → 到目標系統或改匯入；Python 找不到 → 先直接查清單。盤點零項目或有 warnings → 檢查覆蓋範圍與手動補充，不解讀成全機無軟體。
