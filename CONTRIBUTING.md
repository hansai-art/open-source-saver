# 參與整理 / Contributing

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
