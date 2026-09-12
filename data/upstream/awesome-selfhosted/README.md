# Awesome Selfhosted 上游探索索引

這份索引把 [awesome-selfhosted-data](https://github.com/awesome-selfhosted/awesome-selfhosted-data) 的 **1,346 筆來源紀錄**整理為 **1,346 個去重專案、84 個上游分類**，用來擴大搜尋與建立待研究清單。

**這些專案尚未經 Open Source Saver 逐項官方查核，也不計入精選推薦數量。** 上游包含 92 個帶有非自由授權的去重專案；`upstream_nonfree: true` 原樣保留該資訊，不能把整份索引宣稱為可免費商用的開源軟體。自架也可能需要主機、網域、維護、API 或商業功能費用。

| 項目 | 本次快照 |
| --- | --- |
| 資料檔 | [index.json](index.json) |
| 上游版本 | [`851f84709d5ac80deb2933d3a81dc48d89818be7`](https://github.com/awesome-selfhosted/awesome-selfhosted-data/tree/851f84709d5ac80deb2933d3a81dc48d89818be7) |
| 上游提交時間 | 2026-09-11T06:07:43-04:00 |
| 擷取日期 | 2026-09-12 |
| 合併的重複來源紀錄 | 0 |
| 資料授權 | [CC BY-SA 3.0](LICENSE) |
| 原作者 | [完整上游 AUTHORS](AUTHORS) |

## 收錄欄位與界線

每筆保留名稱、別名、官方網址、原始碼網址、授權代碼、上游分類、語言／部署技術，以及指向固定 commit 的原始 YAML 檔案連結。沒有複製上游的產品介紹文章、比較結論或功能描述。

- `id`：由正規化來源網址產生的穩定 ID；同一 repo 的重複紀錄會合併，名稱差異存入 `aliases`。
- `canonical_url`：優先使用原始碼網址，合併 GitHub repo 的大小寫、`.git`、分支與檔案網址差異。未知主機保留可能表示專案身分的 URL 查詢參數。
- `upstream_files`：每筆資料可追溯的固定版本來源。合併專案保留所有來源連結。
- `licenses`：上游回報的授權代碼，尚未逐項比對各專案當下的 LICENSE。
- `upstream_nonfree`：任一授權代碼出現在上游非自由授權清單就標記為 `true`，合併後也保留此提醒。`false` 也不代表已完成本專案的授權審查。
- `platforms`：上游的程式語言或部署技術，**不代表** Windows、macOS、iOS 等終端裝置相容性。
- `review_status`：固定為 `upstream-discovery-unreviewed`；進入正式推薦前須另外查核安裝方式、授權、維護狀態、付費限制及取代範圍。

網址已檢查 HTTP(S) 格式，並禁止含有帳密的 URL；匯入時沒有逐站測試是否仍可連線。這是自架軟體領域的一份上游快照，不代表涵蓋全世界所有軟體。精選推薦與本索引可能重疊，兩者數量不可直接相加當成唯一工具總數。

## 重建與更新

一般使用者讀取 JSON 不需要額外套件。只有維護者匯入 YAML 時需要 Python、Git 和 PyYAML。匯入程式不連網、不安裝套件、不執行上游專案程式；只讀取已取得的本機 Git 快照。它以 `git archive` 讀取固定 commit，因此工作目錄未提交的內容不會混入索引。

先自行取得或更新 `awesome-selfhosted-data` 的本機 checkout，再執行：

```bash
python scripts/import_upstream.py --source ../awesome-selfhosted-data --commit 851f84709d5ac80deb2933d3a81dc48d89818be7 --retrieved-at 2026-09-12
```

相同 Git commit 與 `--retrieved-at` 會產生完全一致的 `index.json`、README、LICENSE 和 AUTHORS。更新時換成實際取得的新 commit 與擷取日期；`--check` 可核對目前輸出是否與來源一致而不寫檔。若上游資料授權不再是 CC BY-SA 3.0，程式會停止，要求先確認新的再利用條件。

## 授權與改作聲明

原始清單由 awesome-selfhosted contributors 維護，作者名單完整保留於 [AUTHORS](AUTHORS)。上游資料依 [Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) 發布；這份衍生索引同樣採用 **CC BY-SA 3.0**。本目錄中的衍生資料不改採專案根目錄的 MIT 授權。

Open Source Saver 的改作包括：篩選為事實欄位、移除原文描述、統一 JSON 格式、正規化網址、合併同 repo 紀錄、加入穩定 ID、來源版本與未查核標記。軟體本身各有自己的授權，清單資料授權不會取代軟體授權；本索引也不代表上游作者為 Open Source Saver 背書。
