# 節費範例怎麼算 / Savings methodology

[繁中首頁](../README.md) · [English home](../README.en.md) · [價格 JSON / Price data](../data/price-benchmarks.json)

查核日 / Checked: **2026-09-11**. Currency: **USD**.

首頁使用 [TechSmith 官方商店](https://www.techsmith.com/store/camtasia) 與 [Screen Studio 官方頁面](https://screen.studio/) 的個人方案公開價格。數字是費用比較基準，不是使用者帳單，也不是本專案的歷史節省成果。Screen Studio 月繳按 12 個月換算；官網年繳方案的每月等值需乘 12。兩種付款方案互斥。

The homepage uses public individual-plan prices from those official pages. They are benchmarks, not the user's invoice or measured savings achieved by this project. Monthly Screen Studio assumes 12 payments; the annual plan's displayed monthly equivalent is multiplied by 12. Never combine those billing alternatives.

## 個人計算 / Personal calculation

**一年可省現金 = 一年內確實可避免的原支出 − 替代方案新增必要支出。**

**Annual cash savings = expenses actually avoidable within the year − necessary new costs of the alternative.**

- 先確認使用者真的有這筆支出，以及取消何時生效。已繳不可退的期間不能立刻算成退費。 / Establish the real expense and cancellation date; prepaid nonrefundable periods do not become an immediate refund.
- 以帳單與所在地結帳價格為準，標明折扣、稅費、幣別及期間；本次範例不換算新台幣。 / Use the invoice and regional checkout terms, including currency, discounts, taxes and term. These examples do not convert to TWD.
- 替代品有必要的 API、模型、硬體、主機或儲存費用就扣除；學習及遷移工時另外估。 / Subtract necessary API, model, hardware, hosting and storage costs; estimate transition time separately.
- 套裝只算一次；仍需使用其中功能而繼續付費，該筆節省就是零。 / Count a suite once; continuing the same subscription means no savings on that expense.
- 舊買斷授權、免費閱讀器及原本就用免費版的情境，不套用年度訂閱節費數字。 / Perpetual licenses and already-free tools do not inherit annual subscription savings.
- 基本錄影與剪輯能否滿足需求要先測；不得把 OBS 的錄影能力寫成 Screen Studio 完整自動運鏡，也不得假設已換掉 Camtasia 全套功能。 / Trial the workflow first; basic recording/editing does not establish equivalence to automatic camera movement or a complete suite.

## 維護 / Maintenance

修改價格時，同步更新 `data/price-benchmarks.json`、兩份 README 的表格與開頭範例、查核日。保留確切方案與付費週期；不要只寫品牌最低價，或用試用價代替正常價格。

When refreshing prices, update the JSON, both README tables and opening examples, and the review date together. Preserve exact plan and billing period; do not substitute a trial price or an unrelated entry plan.
