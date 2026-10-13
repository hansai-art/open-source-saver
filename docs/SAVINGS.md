# 節費範例怎麼算 / Savings methodology

[繁中首頁](../README.md) · [English home](../README.en.md) · [價格 JSON / Price data](../data/price-benchmarks.json)

查核日 / Checked: **2026-10-13**. Currency: **USD**.

首頁現在採用「每個常見領域只挑一個代表性付費工具」的十筆桌面軟體示例，Adobe 家族只計 Photoshop 一筆，排除 Slack、Dropbox、Figma、Otter 這類以網路服務為主的工具，合計 **US$989.13**，首頁四捨五入顯示約 **US$989／年**。這不是市場占有率排名、個人帳單或本專案已實現的節省成果；只有使用者真的有該筆支出、替代品完成工作並成功停止續費或不再購買，才算實際節省。

The homepage now uses ten desktop-software examples, with one representative paid tool per common category. Adobe is counted once, represented by Photoshop. Slack, Dropbox, Figma and Otter are excluded as primarily network services. The illustrative total is **US$989.13**, rounded on the homepage to about **US$989/year**. This is not a market-share ranking, the user's invoice or measured savings achieved by this project. It becomes real savings only when the user has the expense, the replacement completes the work and the user stops renewing or buying the original tool.

## 首頁十筆基準 / Homepage basket

| 領域 / Category | 代表性付費工具 / Paid tool | 年度基準 / Annualized benchmark | 首頁首選候選 / First candidate | 官方價格 / Official price |
|---|---|---:|---|---|
| 螢幕錄影 / Screen recording | [Screen Studio](https://screen.studio/) | US$108.00 | [OpenScreen](https://github.com/getopenscreen/openscreen) | [Screen Studio](https://screen.studio/) |
| 截圖標註 / Screenshots and markup | [Snagit](https://www.techsmith.com/store/snagit) | US$39.00 | [macshot](https://github.com/sw33tLie/macshot) | [TechSmith](https://www.techsmith.com/store/snagit) |
| 文書試算表 / Documents and spreadsheets | [Microsoft 365 Personal](https://www.microsoft.com/en-us/microsoft-365/p/microsoft-365-personal/cfq7ttc0k5bf) | US$99.99 | [ONLYOFFICE](https://www.onlyoffice.com/) | [Microsoft](https://www.microsoft.com/en-us/microsoft-365/p/microsoft-365-personal/cfq7ttc0k5bf) |
| 個人筆記 / Personal notes | [Notion Plus](https://www.notion.com/pricing) | US$120.00 | [Obsidian](https://obsidian.md/) | [Notion](https://www.notion.com/pricing) |
| 修圖 / Image editing | [Adobe Photoshop](https://www.adobe.com/products/photoshop/plans.html) | US$263.88 | [GIMP](https://www.gimp.org/) | [Adobe](https://www.adobe.com/products/photoshop/plans.html) |
| PDF 編輯 / PDF editing | [PDF Expert Pro](https://pdfexpert.com/pricing) | US$79.99 | [PDFsam Basic](https://pdfsam.org/pdfsam-basic/) | [PDF Expert](https://pdfexpert.com/pricing) |
| 密碼 / Passwords | [1Password Individual](https://1password.com/pricing/personal) | US$47.88 | [Proton Pass](https://proton.me/pass) | [1Password](https://1password.com/pricing/personal) |
| Mac 維護 / Mac maintenance | [CleanMyMac](https://macpaw.com/store/cleanmymac) | US$119.40 | [Pearcleaner](https://github.com/Alienator88/Pearcleaner) | [CleanMyMac](https://macpaw.com/store/cleanmymac) |
| 程式編輯 / Code editing | [Sublime Text Personal](https://www.sublimehq.com/store/text) | US$33.00 annualized | [VSCodium](https://vscodium.com/) | [Sublime Text](https://www.sublimehq.com/store/text) |
| 防毒 / Antivirus | [Avast Premium Security](https://www.avast.com/premium-security) | US$77.99 renewal benchmark | [ClamAV](https://www.clamav.net/) | [Avast](https://www.avast.com/premium-security) |
| **合計 / Total** |  | **US$989.13** |  |  |

Notion、1Password 與 CleanMyMac 的月繳價格以 12 個月年化；Sublime Text 的個人 US$99／3 年授權年化為 US$33，授權本身不會在 3 年後失效；Avast 使用官方頁面顯示的 US$77.99／年續訂基準，首年優惠不列入。Adobe 家族只計 Photoshop，避免同一家族重複計算。免費／開源候選只代表第一個值得試的方向，不代表完整功能等效，仍要用自己的檔案、帳號與交付流程驗證。

Notion, 1Password and CleanMyMac are annualized from monthly prices. Sublime Text's US$99 personal license covers 3 years of updates and is annualized to US$33; the license does not expire after that update period. Avast uses the official US$77.99/year renewal benchmark, excluding first-year promotions. Adobe is represented once by Photoshop to avoid double-counting the family. The free/open-source candidate is only the first direction to test, not a full-equivalence claim; validate it with your files, accounts and delivery workflow.

## 個人計算 / Personal calculation

**一年可省現金 = 一年內確實可避免的原支出 − 替代方案新增必要支出。**

**Annual cash savings = expenses actually avoidable within the year − necessary new costs of the alternative.**

- 先確認使用者真的有這筆支出，以及取消何時生效。已繳不可退的期間不能立刻算成退費。 / Establish the real expense and cancellation date; prepaid nonrefundable periods do not become an immediate refund.
- 以帳單與所在地結帳價格為準，標明折扣、稅費、幣別及期間；本次範例不換算新台幣。 / Use the invoice and regional checkout terms, including currency, discounts, taxes and term. These examples do not convert to TWD.
- 替代品有必要的 API、模型、硬體、主機或儲存費用就扣除；學習及遷移工時另外估。 / Subtract necessary API, model, hardware, hosting and storage costs; estimate transition time separately.
- 套裝只算一次；仍需使用其中功能而繼續付費，該筆節省就是零。 / Count a suite once; continuing the same subscription means no savings on that expense.
- 舊買斷授權、免費閱讀器及原本就用免費版的情境，不套用年度訂閱節費數字。 / Perpetual licenses and already-free tools do not inherit annual subscription savings.
- 螢幕錄影、截圖、Office、筆記、修圖、PDF、密碼、防毒、Mac 維護與程式編輯各只取一筆代表性方案；Adobe 家族只計一筆，不能把首頁十筆當成完整市場排名。 / Keep one representative plan per category; Adobe is counted once, and the ten homepage rows are not a complete market ranking.

## 維護 / Maintenance

修改價格時，同步更新 `data/price-benchmarks.json`、兩份 README 的十筆表格與標題總額、查核日。保留確切方案與付費週期；不要只寫品牌最低價，或用試用價代替正常價格。

When refreshing prices, update the JSON, the ten-row tables and displayed totals in both READMEs, and the review date together. Preserve the exact plan and billing period; do not substitute a trial price or an unrelated entry plan.
