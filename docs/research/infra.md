# 開源省錢管家：開發、隱私與基礎工具研究筆記

研究日期：2026-09-12

本批 38 個新產品、21 組用途條件式配對、11 個新增類別標籤。沿用既有 file-transfer 與 productivity 類別，未把平台版本、Krokiet/Czkawka 前端或商業版拆成多個產品。資料欄位遵守現有 products.json／alternatives.json；infra-mappings.json 的 category_labels 是另外提供給產生器的中英標籤。

## 研究範圍與查核方式

逐項透過 GitHub 連接器取得官方儲存庫 metadata 與 README，確認產品用途、平台、授權與非封存狀態。GitHub 無法辨識混合授權時，再讀 LICENSE／COPYING／Cargo.toml。官方產品網站用於核對版本、下載、託管與付費功能。全部 runtime_tested=false；尚未做安裝、遷移、效能、繁中介面或商業工作流實測。

paid-to-OSS mappings 是本研究根據文件功能的條件式判斷，不是作者背書或完整替代認證。來源中有付費版、原始碼可見模組、第三方模型、服務費用時，僅收錄明示的開源範圍。清理、備份和自架失效情境屬一般部署建議；不假裝已跑過破壞或還原測試。

## 影響推薦的具體發現

- **BorgBackup**：官網列 Borg 1.4 為正式穩定系列，Borg 2 為測試版本並禁止作正式備份使用。Windows 不列入本批穩定候選平台。[版本界線](https://www.borgbackup.org/)
- **Krokiet／Czkawka**：官方主 README 寫明 Czkawka GTK 12 為最後發行，新使用者應選 Krokiet；Krokiet Cargo.toml 為 GPL-3.0-only。不同前端不重複計數，RAW／HEIF 與相似影片有依賴限制。[README](https://github.com/qarmin/czkawka/blob/master/README.md) · [Krokiet](https://github.com/qarmin/czkawka/blob/master/krokiet/README.md)
- **Duplicati**：現行 LICENSE 為 MIT，但排除 proprietary/ 與其他另有授權元件，不沿用舊文章的 LGPL 授權。[授權](https://github.com/duplicati/duplicati/blob/master/LICENSE)
- **Beekeeper Studio**：Community 為 GPL-3.0-or-later；src-commercial 是商業授權，本批未將其功能算入 GPL 版。Oracle、DuckDB 等資料庫欄位需看官方版別表。[授權](https://github.com/beekeeper-studio/beekeeper-studio/blob/master/LICENSE.md)
- **Zed**：編輯器免費，但 AI、Pro、Business 與使用者自己的模型 API 費用需要分開算。[方案](https://zed.dev/pricing)
- **RustDesk**：OSS 伺服器與 Server Pro 功能不同；Pro 是自架方案授權，不是包含主機的 SaaS。[方案](https://rustdesk.com/pricing/)
- **Cryptomator**：桌面加密功能免費；Android/iOS 免費為唯讀，寫入需各平台授權。[下載與平台條件](https://cryptomator.org/downloads/)
- **KDE Connect**：repo README 有「Mac／Windows 尚未正式支援」的舊段落，但官方下載頁目前有 Windows 與 macOS 穩定下載。因此平台以官方下載頁為準，不沿用該舊段落。[官方下載](https://kdeconnect.kde.org/download.html)
- **Actual Budget**：官方列的銀行區域為紐西蘭、歐洲、北美、巴西，未建立台灣銀行支援；bank-sync 需要 server，金鑰不受預算資料端對端加密保護。[銀行文件](https://actualbudget.org/docs/advanced/bank-sync/)
- **Zotero**：現行 COPYING 是 AGPLv3；書目同步免費不限量，附件空間免費 300 MB；WebDAV 僅能處理個人庫附件。[同步](https://www.zotero.org/support/sync) · [授權](https://github.com/zotero/zotero/blob/main/COPYING)
- **Pi-hole**：Core 現行 LICENSE 為 EUPL-1.2，不把早期 GPL 記憶套用至所有元件。[授權](https://github.com/pi-hole/pi-hole/blob/master/LICENSE)
- **Ollama／Jan／GPT4All**：程式碼開源不等於所有模型授權相同或無硬體成本；Ollama 另有雲端路徑，需明確選本機模式。[Ollama FAQ](https://docs.ollama.com/faq)
- **AdGuard Home**：官方明列 DNS 無法擋與內容共用網域的 YouTube／Twitch 廣告，不以「全面去廣告」包裝。[限制](https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md)
- **Uptime Kuma**：官方不支援 NFS 作資料目錄；自架也不自動提供外部監控節點，服務與監控同台的失效風險需由部署設計處理。[README](https://github.com/louislam/uptime-kuma/blob/master/README.md)

## 本批不採用或不延伸的項目

Remmina 官網確認為自由軟體且有 Linux 安裝說明，但本次 GitLab LICENSE 存取失敗；為維持完整可讀的授權證據，本批以 Apache Guacamole 補足遠端入口情境，沒有把 Remmina 列入 38 項。未抓取論壇整篇文章；各項使用原創中英摘要與官方連結，不將文章來源數量算成產品數。金融產品只做軟體功能整理，沒有給投資、稅務或會計法規判斷。

## 逐項來源與查核快照

所有列均為文件查核，不是執行測試。以下 default branch 及 last push 是本次 GitHub API 快照，不能單憑最近推送時間推定品質或安全。

| ID | 產品 | 官方文件 | 分支 | 最近推送 | 封存 |
|---|---|---|---|---|---|
| infra-restic | restic | [README](https://github.com/restic/restic/blob/master/README.md) | master | 2026-09-01T01:43:58Z | no |
| infra-borg | BorgBackup（1.4 穩定系列） | [README](https://github.com/borgbackup/borg/blob/master/README.rst) | master | 2026-09-11T17:42:58Z | no |
| infra-kopia | Kopia | [README](https://github.com/kopia/kopia/blob/master/README.md) | master | 2026-09-10T22:47:07Z | no |
| infra-duplicati | Duplicati（開源備份用戶端） | [README](https://github.com/duplicati/duplicati/blob/master/README.md) | master | 2026-09-11T17:18:57Z | no |
| infra-rustdesk | RustDesk | [README](https://github.com/rustdesk/rustdesk/blob/master/README.md) | master | 2026-09-12T06:31:17Z | no |
| infra-guacamole | Apache Guacamole | [README](https://github.com/apache/guacamole-client/blob/main/README) | main | 2026-08-29T18:23:02Z | no |
| infra-meshcentral | MeshCentral | [README](https://github.com/Ylianst/MeshCentral/blob/master/readme.md) | master | 2026-09-05T08:27:07Z | no |
| infra-double-commander | Double Commander | [README](https://github.com/doublecmd/doublecmd/blob/master/README.md) | master | 2026-09-11T15:52:49Z | no |
| infra-krokiet | Krokiet（Czkawka 專案） | [README](https://github.com/qarmin/czkawka/blob/master/krokiet/README.md) | master | 2026-09-09T19:48:14Z | no |
| infra-rclone | rclone | [README](https://github.com/rclone/rclone/blob/master/README.md) | master | 2026-09-11T04:16:22Z | no |
| infra-cryptomator | Cryptomator（桌面版） | [README](https://github.com/cryptomator/cryptomator/blob/develop/README.md) | develop | 2026-09-11T19:13:05Z | no |
| infra-bleachbit | BleachBit | [README](https://github.com/bleachbit/bleachbit/blob/master/README.md) | master | 2026-09-12T05:41:07Z | no |
| infra-portmaster | Portmaster | [README](https://github.com/safing/portmaster/blob/development/README.md) | development | 2026-09-10T08:44:59Z | no |
| infra-vscodium | VSCodium | [README](https://github.com/VSCodium/vscodium/blob/master/README.md) | master | 2026-09-09T12:44:56Z | no |
| infra-zed | Zed | [README](https://github.com/zed-industries/zed/blob/main/README.md) | main | 2026-09-12T06:26:23Z | no |
| infra-neovim | Neovim | [README](https://github.com/neovim/neovim/blob/master/README.md) | master | 2026-09-12T03:23:41Z | no |
| infra-geany | Geany | [README](https://github.com/geany/geany/blob/master/README.rst) | master | 2026-08-03T21:34:14Z | no |
| infra-bruno | Bruno（開源版） | [README](https://github.com/usebruno/bruno/blob/main/readme.md) | main | 2026-09-11T09:04:13Z | no |
| infra-hoppscotch | Hoppscotch Community | [README](https://github.com/hoppscotch/hoppscotch/blob/main/README.md) | main | 2026-09-10T22:31:29Z | no |
| infra-dbeaver | DBeaver Community | [README](https://github.com/dbeaver/dbeaver/blob/devel/README.md) | devel | 2026-09-12T06:38:16Z | no |
| infra-sqlite-browser | DB Browser for SQLite | [README](https://github.com/sqlitebrowser/sqlitebrowser/blob/master/README.md) | master | 2026-09-09T00:32:41Z | no |
| infra-beekeeper | Beekeeper Studio Community | [README](https://github.com/beekeeper-studio/beekeeper-studio/blob/master/README.md) | master | 2026-09-12T02:06:11Z | no |
| infra-jan | Jan | [README](https://github.com/janhq/jan/blob/main/README.md) | main | 2026-09-11T06:02:04Z | no |
| infra-gpt4all | GPT4All | [README](https://github.com/nomic-ai/gpt4all/blob/main/README.md) | main | 2025-05-27T20:05:19Z | no |
| infra-ollama | Ollama | [README](https://github.com/ollama/ollama/blob/main/README.md) | main | 2026-09-11T21:44:45Z | no |
| infra-gnucash | GnuCash | [README](https://github.com/Gnucash/gnucash/blob/stable/README) | stable | 2026-09-11T23:22:22Z | no |
| infra-actual | Actual Budget | [README](https://github.com/actualbudget/actual/blob/master/README.md) | master | 2026-09-11T21:55:42Z | no |
| infra-money-manager-ex | Money Manager Ex | [README](https://github.com/moneymanagerex/moneymanagerex/blob/master/README.md) | master | 2026-09-11T10:21:35Z | no |
| infra-freshrss | FreshRSS | [README](https://github.com/FreshRSS/FreshRSS/blob/edge/README.md) | edge | 2026-09-11T06:18:09Z | no |
| infra-rss-guard | RSS Guard | [README](https://github.com/martinrotter/rssguard/blob/master/README.md) | master | 2026-09-11T01:41:18Z | no |
| infra-zotero | Zotero | [README](https://github.com/zotero/zotero/blob/main/README.md) | main | 2026-09-11T18:47:32Z | no |
| infra-jabref | JabRef | [README](https://github.com/JabRef/jabref/blob/main/README.md) | main | 2026-09-11T22:57:29Z | no |
| infra-scrcpy | scrcpy | [README](https://github.com/Genymobile/scrcpy/blob/master/README.md) | master | 2026-09-11T16:58:44Z | no |
| infra-kde-connect | KDE Connect | [README](https://github.com/KDE/kdeconnect-kde/blob/master/README.md) | master | 2026-09-11T01:51:15Z | no |
| infra-app-manager | App Manager | [README](https://github.com/MuntashirAkon/AppManager/blob/master/README.md) | master | 2026-09-12T06:17:07Z | no |
| infra-adguard-home | AdGuard Home | [README](https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md) | master | 2026-09-11T14:57:43Z | no |
| infra-pi-hole | Pi-hole | [README](https://github.com/pi-hole/pi-hole/blob/master/README.md) | master | 2026-09-06T19:06:42Z | no |
| infra-uptime-kuma | Uptime Kuma | [README](https://github.com/louislam/uptime-kuma/blob/master/README.md) | master | 2026-09-12T05:01:49Z | no |

