# 企業與自架 SaaS 擴充研究紀錄

查核日期：2026-09-12。

本批新增 **35 個獨立產品、13 個主分類、37 組付費產品用途對照**。與原有 78 款清單按產品名稱及來源比對，無重複；正式合併仍需與其他研究批次交叉去重。products 是同一 schema 的增量；business-mappings.json 另外提供 category_labels 給 build_catalog.py，mappings 欄位可直接合併。

## 查核範圍

- 每個產品均實際讀取官方 GitHub README；對授權不明確或 open-core 者另讀官方 LICENSE、版本授權文件。
- Wiki.js 與 DokuWiki 的文字只描述文件 Wiki，用途對應不推定 Notion 資料庫或 Confluence 巨集可原樣搬移。
- 全部設 runtime_tested=false、zh_tw=unknown。已讀文件不能充當安裝測試、繁體中文驗收或資料遷移驗收。
- platforms:[web] 代表瀏覽器端，不代表已驗證任何使用者電腦可直接執行伺服器。delivery:self-hosted 表示需要部署及持續維護。
- 不提供虛構節省金額。總成本仍包含主機、資料庫、備份、寄信、金流、外部 API、導入及維護；如原有付費方案的必要功能仍須付費擴充，不能把全部訂閱列成可省。
- 各品牌對照只表示值得測試的相同用途候選，relationship_status 全是 conditional-candidates-not-workflow-tested。
- 授權屬版本／檔案層級觀察；不把倉庫含有商業目錄推定整個免費核心都非開源，也不把核心授權套到 Enterprise 程式。

## 本次發現舊文章容易寫錯的地方

1. **Cal.com 已轉向 Cal.diy 社群倉庫，不能沿用舊替代推薦。** 官方 README 顯示 Cal.diy 是 MIT，已拿掉 Teams、Organizations、Insights、Workflows、SSO／SAML 等 Enterprise 功能，並只建議 personal, non-production。這批企業候選不納入，預約先收錄 Easy!Appointments。來源：[Cal.diy README](https://github.com/calcom/cal.diy/blob/main/README.md)、[官方自架說明](https://www.cal.diy/)。
2. **Medusa 現為 open-core。** MIT 只涵蓋核心；指定 RBAC Enterprise 材料需商業協議，不能說整個倉庫全 MIT。[README](https://github.com/medusajs/medusa/blob/develop/README.md)、[LICENSE](https://github.com/medusajs/medusa/blob/develop/LICENSE)。
3. **Taiga 目前 backend README 使用 MPL-2.0。** 不能直接抄舊表格上的 AGPL。[README](https://github.com/taigaio/taiga-back/blob/main/README.md)。
4. **BookStack 官方文件指向 Codeberg。** GitHub README 仍可讀取，但官網明示主要 source 位於 Codeberg；不是看到來源移動就判定停止維護。[官網](https://www.bookstackapp.com/)、[README](https://github.com/BookStackApp/BookStack/blob/development/readme.md)。
5. **Kanboard 正在 maintenance mode。** 仍可用作簡單看板候選，但不推薦期待大量新功能的團隊。[README](https://github.com/kanboard/kanboard/blob/main/README.md)。
6. **Plausible CE 有明確功能缺口。** 官方對照表說明 CE 沒有 marketing funnels、ecommerce revenue goals、SSO、Sites API，不能用 Cloud 功能清單充當 CE。[README](https://github.com/plausible/analytics/blob/master/README.md)。
7. **同個倉庫不代表同種授權。** Metabase enterprise、Chatwoot enterprise、OpnForm api/app/Enterprise、Activepieces 的兩處 ee 目錄都必須排除在 OSS 核心之外。
8. **WooCommerce 依現在官方插件 readme 標 GPLv3。** 不沿用印象中的舊授權值。[插件 readme](https://github.com/woocommerce/woocommerce/blob/trunk/plugins/woocommerce/readme.txt)。
9. **ERP 在台灣能不能用是另一個驗收問題。** 本次只確認官方功能與自架性質，未驗證台灣電子發票、薪資、稅務及會計作業。ERPNext、Dolibarr、Odoo Community 的候選文字保留這個界線。

## 覆蓋數量

| 分類 | 本批數量 |
| --- | ---: |
| 預約與排程 | 1 |
| 商業智慧與儀表板 | 2 |
| 客戶關係與銷售管理 | 3 |
| 電商與購物車 | 4 |
| 電子報與行銷自動化 | 2 |
| ERP 與進銷存 | 3 |
| 表單與問卷 | 2 |
| 客服與工單 | 4 |
| 專案管理與看板 | 5 |
| 團隊通訊 | 1 |
| 網站分析 | 3 |
| 團隊 Wiki 與知識庫 | 3 |
| 工作流程自動化 | 2 |

## 每個產品的主要查核記錄

下列 SHA 是讀取檔案時由 GitHub API 回傳的 **blob SHA**，不是程式版本、release 或 runtime 測試結果。原始文章內容不整篇搬運，資料集用摘要、功能界線與來源連結保留可追溯性。

| 產品 | 已讀官方主要資料 | blob SHA |
| --- | --- | --- |
| OpenProject Community | [官方 README](https://github.com/opf/openproject/blob/dev/README.md) | `f077258f783efe3cb64272eb3bb526f240a49f15` |
| Taiga | [官方 README](https://github.com/taigaio/taiga-back/blob/main/README.md) | `2937275d9aa2d700f1b931b9d630caebdfd508c2` |
| Kanboard | [官方 README](https://github.com/kanboard/kanboard/blob/main/README.md) | `6795b0ddc9a277d1cedd7b75f0c5cd0a4199122b` |
| WeKan | [官方 README](https://github.com/wekan/wekan/blob/main/README.md) | `27cd30d2357dcf23a384f5eb6b9572c456685a51` |
| Plane Community | [官方 README](https://github.com/makeplane/plane/blob/preview/README.md) | `74688cd92c4b14a9e34ad26075fa752a755b21c2` |
| SuiteCRM | [官方 README](https://github.com/SuiteCRM/SuiteCRM/blob/hotfix/README.md) | `6492df4ff987ea0801427dfcce00e787f8031483` |
| EspoCRM | [官方 README](https://github.com/espocrm/espocrm/blob/master/README.md) | `8db5d5758ae6255544833f3fd9354522cf318a5a` |
| Frappe CRM | [官方 README](https://github.com/frappe/crm/blob/develop/README.md) | `6e66305bd7ad38510d6544ccb9699f079441c077` |
| ERPNext | [官方 README](https://github.com/frappe/erpnext/blob/develop/README.md) | `bb7a8bc2c33033e506dc5c15469aaacfe31ceee5` |
| Dolibarr | [官方 README](https://github.com/Dolibarr/dolibarr/blob/develop/README.md) | `464e051e5423c52189fae72ebb86cae23bb5df8c` |
| Odoo Community | [官方 README](https://github.com/odoo/odoo/blob/19.0/README.md) | `ac3c04c8f4c53e75a25ec330143f870d2af9ae8b` |
| Matomo On-Premise Community | [官方 README](https://github.com/matomo-org/matomo/blob/6.x-dev/README.md) | `8dcee2296ffdb70465732af782a2869592b1a5ca` |
| Umami | [官方 README](https://github.com/umami-software/umami/blob/master/README.md) | `e0ebef01bb8593670e2b1d42d17f947207984805` |
| Plausible Community Edition | [官方 README](https://github.com/plausible/analytics/blob/master/README.md) | `6320d91e4b69b40da0c6a5433a258bf23e0f51ce` |
| Metabase Open Source | [官方 README](https://github.com/metabase/metabase/blob/master/README.md) | `0724c61a87c07294fdd3788d4ab4a14218fc9f50` |
| Apache Superset | [官方 README](https://github.com/apache/superset/blob/master/README.md) | `961886df64d20b96bc6d3632d29e68dffc074872` |
| LimeSurvey Community | [官方 README](https://github.com/LimeSurvey/LimeSurvey/blob/master/README.md) | `c3d3869a1986432b8929699f46afa50f1ce6a8ae` |
| OpnForm Community | [官方 README](https://github.com/OpnForm/OpnForm/blob/main/README.md) | `4faec7600913a79dcc10ae7029b0d7a55e73df44` |
| WooCommerce | [官方 README](https://github.com/woocommerce/woocommerce/blob/trunk/README.md) | `ea9f6c1bd1f8c278d2d0ea28ece42e33149a564f` |
| PrestaShop | [官方 README](https://github.com/PrestaShop/PrestaShop/blob/develop/README.md) | `dc9da0328582549d48ae22bf7f84cbd225c99724` |
| Medusa Core | [官方 README](https://github.com/medusajs/medusa/blob/develop/README.md) | `555892311daf5f44023620a3b2daa16729f01075` |
| Saleor | [官方 README](https://github.com/saleor/saleor/blob/main/README.md) | `c713c69282671a8cd254fe3607e647e7a1b9a463` |
| Zammad | [官方 README](https://github.com/zammad/zammad/blob/develop/README.md) | `a14ceb2e9dc8a5f65b08ae6ef698db307e03ecba` |
| osTicket | [官方 README](https://github.com/osTicket/osTicket/blob/develop/README.md) | `7ddad4a7471aaffee50cbb456be85d1194e8da65` |
| FreeScout | [官方 README](https://github.com/freescout-help-desk/freescout/blob/dist/README.md) | `1a7ff4643ade7d137bf571c930947e0b4f8cee35` |
| Chatwoot Community | [官方 README](https://github.com/chatwoot/chatwoot/blob/develop/README.md) | `d8b8ae7a2331ba9eb4002ea7d2911a4ae36bf297` |
| Easy!Appointments | [官方 README](https://github.com/alextselegidis/easyappointments/blob/main/README.md) | `cefbb18b1d997e9cedccd89bc90731b95fa7900f` |
| Zulip | [官方 README](https://github.com/zulip/zulip/blob/main/README.md) | `062e7788bfa050ccfc43727a68a29025a0a61127` |
| BookStack | [官方 README](https://github.com/BookStackApp/BookStack/blob/development/readme.md) | `e9e5d197b4365fe68e275101dedbd83d8e98f61d` |
| Wiki.js | [官方 README](https://github.com/requarks/wiki/blob/main/README.md) | `12b88069035f73f2733e62eaf7bf2a9678d65d0f` |
| DokuWiki | [官方 README](https://github.com/dokuwiki/dokuwiki/blob/master/README) | `d016e558296622fc141f48263f396ea17eb3bba8` |
| Activepieces Community | [官方 README](https://github.com/activepieces/activepieces/blob/main/README.md) | `83e16d857968de7c88600a6536d32042202b2348` |
| Node-RED | [官方 README](https://github.com/node-red/node-red/blob/main/README.md) | `1293e94d8503d6734c251cc2962524ffb4b291fd` |
| listmonk | [官方 README](https://github.com/knadh/listmonk/blob/master/README.md) | `0be3f3ef7ede5c229b6c1668e2c6639394335265` |
| Mautic | [官方 README](https://github.com/mautic/mautic/blob/7.x/README.md) | `27c7e65fb8ecf4d5fe44efa97f8f1f3221b959ea` |

## 官方補充資料

- [Odoo Community／Enterprise 授權文件](https://github.com/odoo/documentation/blob/19.0/content/legal/licenses.rst)：分清 LGPL 社群版、Enterprise 與部分 Apps 的專有條款。
- [EspoCRM 擴充目錄](https://www.espocrm.com/extensions/)：報表、BPM、工作流、Sales Pack 等有獨立套件邊界。
- [Matomo 定價與功能對照](https://matomo.org/pricing/)：Community 核心與付費 Premium 外掛不同；本批未採其浮動價格作節省估算。
- [FreeScout 模組目錄](https://freescout.net/modules/)：核心共享信箱與外加功能分開估價。
- [Metabase LICENSE](https://github.com/metabase/metabase/blob/master/LICENSE.txt)：OSS 與 Enterprise 程式和映像有明確路徑區別。
- [Chatwoot LICENSE](https://github.com/chatwoot/chatwoot/blob/develop/LICENSE)：MIT 不涵蓋 enterprise/。
- [OpnForm LICENSE](https://github.com/OpnForm/OpnForm/blob/main/LICENSE)：AGPL core 與 api/app/Enterprise 分開；採保守 AGPL-3.0 標示。
- [Activepieces LICENSE](https://github.com/activepieces/activepieces/blob/main/LICENSE)：packages/ee/ 及 packages/server/api/src/app/ee 都是商業條款範圍。
- [PrestaShop LICENSE](https://github.com/PrestaShop/PrestaShop/blob/develop/LICENSE.md)：core 為 OSL-3.0、modules 為 AFL-3.0。
- [Saleor LICENSE](https://github.com/saleor/saleor/blob/main/LICENSE)：BSD-3-Clause。
- [Frappe CRM LICENSE](https://github.com/frappe/crm/blob/develop/LICENSE)、[ERPNext license](https://github.com/frappe/erpnext/blob/develop/license.txt)：分別為 AGPL-3.0 與 GPL-3.0，不能因同一組織就套同一授權。
- [Mautic LICENSE](https://github.com/mautic/mautic/blob/7.x/LICENSE.txt)：GPL-3.0-or-later；README 另明示正式環境應用 release／production package。
- [DokuWiki 官網](https://www.dokuwiki.org/)與 [COPYING](https://github.com/dokuwiki/dokuwiki/blob/master/COPYING)：不需資料庫的 Wiki、GPL-2.0；部分官網頁面此次直接擷取失敗，功能描述有官方搜尋摘要及倉庫資料交叉支持。

## 下一輪值得深挖的缺口

- 台灣 ERP／電子發票／金物流：找有實際導入教程、外掛維護紀錄與台灣測試環境的案例，先核對版本，避免把全球支援誤寫成台灣支援。
- 各核心任務的遷移實測：從真實匯出檔驗證 Jira／Trello、Salesforce、Shopify、Zendesk、Confluence，保留欄位、附件、權限及失敗項目清單。
- 部署成本：固定小團隊人數、資料量、郵件量與流量，用可重算的 TCO 表比較授權差額，不只標「免費」。
- 商業邊界追蹤：定期重看 LICENSE、Enterprise 目錄及 CE 功能對照，尤其是新創 open-core 專案；用來源變更觸發重新研究。
- 企業管理延伸：人資、招募、工時、資產、文件簽署、學習平台與預算核銷還有獨立生態，不能因 ERP 收錄就視為全部覆蓋。

