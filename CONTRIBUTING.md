# 參與整理 / Contributing

**歡迎提供你自己開發，或你知道的工具。免費非開源與內建功能也可以，請標明條件。**

不會寫程式也可 [開 Issue 提供工具](https://github.com/hansai-art/open-source-saver/issues/new?template=software.md)：先填名稱、官方連結與用途；其餘未知可明寫。作者自薦、合作或利益關係請註明，不影響提報資格。只有英文也歡迎；可先補繁中教學，再提出上游翻譯建議。

**Your own projects and tools you know are welcome, including usable proprietary freeware and built-in features.** No coding required: suggest a name, official URL and use case in an Issue. Disclose authorship or commercial relationships; unknown fields may remain unknown. English-only projects are welcome.

先找現有文章與工具，確認清單缺口，再提 PR。不要因為英文介面就重寫產品。

新增候選請提供：原工具／需求、候選名稱、官方網址與下載入口、平台、免費範圍、商用限制、部署方式、繁中文件／UI 證據、已知缺口、查核日期。只在你實測且附版本、平台與步驟時標示工作流實測；初版 validator 刻意禁止未經升級流程的 runtime_tested=true。

產品在 data/products.json；替代關係在 data/alternatives.json；只在文章看到而未核對的放 data/discovery.json。兩種語言的用途與限制都要更新，使用 scripts/build_catalog.py 重建雙語清單。新增來源只放原創短摘要和連結，不貼完整文章、不直接搬未釐清授權的 JSON。

```bash
python3 scripts/saver.py validate
python3 scripts/build_catalog.py
python3 -m unittest discover -s tests -v
```

不提交真實安裝清單、私人報告、API key 或帳單。請用虛構測資。文件修正不需要安裝所有候選工具。Windows／Mac 收集器改動需要對應平台驗證；沒有環境就明寫未測。

English: reuse existing tools and article research. Propose candidates with official sources, platform, actual use case, free/commercial limits, delivery mode, localization evidence, gaps and date. Update both language summaries. Distinguish article discovery from official review and reproducible workflow testing. Run the commands above; regenerate catalogs with build_catalog.py. Never commit private inventories, reports, credentials or bills. Use synthetic fixtures. State missing native-platform validation honestly.

## 統計與來源維護 / Counts and evidence

每個產品只給一個主要分類，新增 `source_type`：`open-source`、`proprietary` 或 `source-available`。原始碼公開但附 Commons Clause 等限制的，不標為開源。`see-upstream` 表示未整理完整授權組合，請循官方來源確認條款；不是商用授權已審核的標記。

`build_catalog.py` 會更新兩份首頁的收錄數、分類表、雙語清單和 `data/catalog-stats.json`。價格不由分類腳本重新查網路，請依 [節費維護規則](docs/SAVINGS.md) 另行更新。論壇只收短摘要與原文連結到 `data/community-sources.json`，待查線索不灌進產品數。

Assign one primary category and a source classification per product. Source-available restrictions are not OSI open source. `see-upstream` means the full license mix is not normalized here, not that commercial terms were cleared. Regenerate counts and both catalogs with the existing script. Refresh prices separately; forum-only leads do not increase catalog totals.

## 大量研究與上游索引 / Bulk research and upstream discovery

先讀 [研究規範](docs/RESEARCH.md)，再選缺少的工作領域。新增國內外文章或目錄到 `data/research-sources.json`，寫實際閱讀範圍、原創摘要、候選名稱、語言與限制；有官方反證時附 `verification_sources`。不把目錄總數當逐項查核數。

上游索引只是待研究資料，不直接匯入 `products.json`。先核對正式專案的當前文件、授權、安裝與費用，才升級為整理候選。自架服務以 `platforms: ["web"]` 表達瀏覽器使用端，`delivery: "self-hosted"` 表達部署；不要把 Linux 伺服器需求當成 Mac 安裝包。

完成後執行 `python3 scripts/build_research.py` 同步來源去向與研究統計；維護上游索引時依其 [重建說明](data/upstream/awesome-selfhosted/README.md)，保留 CC BY-SA 3.0 與作者署名。原創程式與研究摘要維持專案 MIT，不能把上游衍生索引改標 MIT。
