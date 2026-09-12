#!/usr/bin/env python3
"""Import an attributed discovery snapshot from a local awesome-selfhosted-data clone.

Maintainer-only dependency: PyYAML. Normal saver.py usage remains dependency-free.
No network requests, application installations, or upstream code execution occur.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile
from urllib.parse import quote, urlsplit, urlunsplit

SOURCE_URL = "https://github.com/awesome-selfhosted/awesome-selfhosted-data"
REVIEW_STATUS = "upstream-discovery-unreviewed"
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "data/upstream/awesome-selfhosted"


def git(source: Path, *arguments: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(source), *arguments], check=True, capture_output=True
    ).stdout


def validate_url(value: object) -> str:
    if not isinstance(value, str) or not value or any(c.isspace() for c in value):
        raise ValueError(f"Expected an HTTP(S) URL, got {value!r}")
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError(f"Unsupported URL: {value!r}")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("Credentials must not appear in discovery URLs")
    # Accessing port also rejects malformed port values.
    _ = parsed.port
    return value


def canonical_url(value: str) -> str:
    """Normalize repository identity without discarding unknown-host project IDs."""
    parsed = urlsplit(validate_url(value))
    host = parsed.hostname.lower()
    scheme = parsed.scheme.lower()
    port = parsed.port
    if port is None or (scheme, port) in {("http", 80), ("https", 443)}:
        netloc = f"[{host}]" if ":" in host else host
    else:
        netloc = f"[{host}]:{port}" if ":" in host else f"{host}:{port}"
    path = re.sub(r"/+", "/", parsed.path).rstrip("/")
    query = parsed.query
    # These hosts identify a repository by owner/repo; branch/file views are aliases.
    if host in {"github.com", "www.github.com", "bitbucket.org", "codeberg.org"}:
        host = "github.com" if host == "www.github.com" else host
        netloc = host if port in {None, 80, 443} else f"{host}:{port}"
        segments = path.strip("/").split("/")
        if len(segments) >= 2:
            path = "/" + "/".join(segments[:2])
        path = path.removesuffix(".git")
        if host == "github.com":
            path = path.lower()
        scheme, query = "https", ""
    elif host == "gitlab.com":
        path = path.split("/-/", 1)[0].removesuffix(".git")
        scheme, query = "https", ""
    else:
        path = path.removesuffix(".git")
        # Gitweb/CVS URLs can identify the actual project in ?p= or ?repname=.
        # Keep their query rather than silently merging unrelated repositories.
    return urlunsplit((scheme, netloc, path, query, ""))


def strings(value: object, field: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{field} must be a nonempty string list")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"Invalid {field}: {value!r}")
    return sorted(set(value), key=lambda item: (item.casefold(), item))


def normalize_entries(records: list[tuple[str, dict]], commit: str,
                      nonfree: set[str], known_licenses: set[str]) -> list[dict]:
    grouped: dict[str, dict] = {}
    for filename, record in records:
        name = record.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"Missing project name in {filename}")
        website = validate_url(record.get("website_url"))
        source_code = validate_url(record.get("source_code_url"))
        identity = canonical_url(source_code)
        licenses = strings(record.get("licenses"), "licenses")
        tags = strings(record.get("tags"), "tags")
        platforms = strings(record.get("platforms"), "platforms")
        unknown = set(licenses) - known_licenses
        if unknown:
            raise ValueError(f"Unknown upstream license IDs in {filename}: {sorted(unknown)}")
        source_file = f"{SOURCE_URL}/blob/{commit}/{quote(filename, safe='/')}"
        item = grouped.get(identity)
        if item is None:
            item = {
                "id": "ash-" + hashlib.sha256(identity.encode("utf-8")).hexdigest()[:20],
                "name": name,
                "aliases": [],
                "website_url": website,
                "source_code_url": source_code,
                "canonical_url": identity,
                "licenses": licenses,
                "tags": tags,
                "platforms": platforms,
                "upstream_nonfree": bool(set(licenses) & nonfree),
                "upstream_files": [source_file],
                "review_status": REVIEW_STATUS,
            }
            grouped[identity] = item
        else:
            names = {item["name"], name, *item["aliases"]}
            ordered_names = sorted(names, key=lambda value: (value.casefold(), value))
            item["name"], item["aliases"] = ordered_names[0], ordered_names[1:]
            for key, incoming in [("licenses", licenses), ("tags", tags),
                                  ("platforms", platforms), ("upstream_files", [source_file])]:
                item[key] = sorted(set(item[key]) | set(incoming))
            item["upstream_nonfree"] = bool(set(item["licenses"]) & nonfree)
    entries = sorted(grouped.values(), key=lambda item: (item["name"].casefold(), item["id"]))
    if len({item["id"] for item in entries}) != len(entries):
        raise ValueError("Stable ID hash collision; increase ID hash length before importing")
    return entries


def read_snapshot(source: Path, revision: str) -> tuple[str, str, dict[str, bytes]]:
    commit = git(source, "rev-parse", "--verify", f"{revision}^{{commit}}").decode().strip()
    if not re.fullmatch(r"[0-9a-f]{40,64}", commit):
        raise ValueError("Could not resolve a full snapshot commit")
    committed_at = git(source, "show", "-s", "--format=%cI", commit).decode().strip()
    archive = git(source, "archive", "--format=tar", commit, "--", "software", "LICENSE",
                  "AUTHORS", "licenses.yml", "licenses-nonfree.yml")
    contents = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as tar:
        for member in tar.getmembers():
            if member.isfile():
                stream = tar.extractfile(member)
                if stream is not None:
                    contents[member.name] = stream.read()
    for required in ("LICENSE", "AUTHORS", "licenses.yml", "licenses-nonfree.yml"):
        if required not in contents:
            raise ValueError(f"Snapshot lacks required upstream attribution/schema file {required}")
    if not contents["LICENSE"].decode().startswith(
        "Creative Commons Attribution-ShareAlike 3.0 Unported"
    ):
        raise ValueError("Upstream data license changed; review redistribution terms before import")
    return commit, committed_at, contents


def build_index(source: Path, revision: str, retrieved_at: str) -> tuple[dict, dict[str, bytes]]:
    try:
        import yaml
    except ImportError as error:
        raise ValueError("Maintainer import requires PyYAML: python -m pip install PyYAML") from error
    dt.date.fromisoformat(retrieved_at)
    commit, committed_at, files = read_snapshot(source, revision)
    nonfree = {item["identifier"] for item in yaml.safe_load(files["licenses-nonfree.yml"])}
    known = nonfree | {item["identifier"] for item in yaml.safe_load(files["licenses.yml"])}
    records = [(name, yaml.safe_load(content)) for name, content in sorted(files.items())
               if name.startswith("software/") and name.endswith(".yml")]
    if not records:
        raise ValueError("No upstream software records found")
    entries = normalize_entries(records, commit, nonfree, known)
    index = {
        "schema_version": 1,
        "source": {
            "name": "awesome-selfhosted-data",
            "repository_url": SOURCE_URL,
            "commit": commit,
            "commit_date": committed_at,
            "retrieved_at": retrieved_at,
            "license": "CC-BY-SA-3.0",
            "license_url": "https://creativecommons.org/licenses/by-sa/3.0/",
            "authors_url": f"{SOURCE_URL}/blob/{commit}/AUTHORS",
            "nonfree_license_ids": sorted(nonfree),
        },
        "status": REVIEW_STATUS,
        "stats": {
            "source_records": len(records),
            "unique_records": len(entries),
            "duplicate_records": len(records) - len(entries),
            "nonfree_records": sum(item["upstream_nonfree"] for item in entries),
            "tags": len({tag for item in entries for tag in item["tags"]}),
        },
        "entries": entries,
    }
    return index, {"LICENSE": files["LICENSE"], "AUTHORS": files["AUTHORS"]}


def render_readme(index: dict) -> str:
    source, stats = index["source"], index["stats"]
    return f"""# Awesome Selfhosted 上游探索索引

這份索引把 [awesome-selfhosted-data]({SOURCE_URL}) 的 **{stats['source_records']:,} 筆來源紀錄**整理為 **{stats['unique_records']:,} 個去重專案、{stats['tags']} 個上游分類**，用來擴大搜尋與建立待研究清單。

**這些專案尚未經 Open Source Saver 逐項官方查核，也不計入精選推薦數量。** 上游包含 {stats['nonfree_records']} 個帶有非自由授權的去重專案；`upstream_nonfree: true` 原樣保留該資訊，不能把整份索引宣稱為可免費商用的開源軟體。自架也可能需要主機、網域、維護、API 或商業功能費用。

| 項目 | 本次快照 |
| --- | --- |
| 資料檔 | [index.json](index.json) |
| 上游版本 | [`{source['commit']}`]({SOURCE_URL}/tree/{source['commit']}) |
| 上游提交時間 | {source['commit_date']} |
| 擷取日期 | {source['retrieved_at']} |
| 合併的重複來源紀錄 | {stats['duplicate_records']} |
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
python scripts/import_upstream.py --source ../awesome-selfhosted-data --commit {source['commit']} --retrieved-at {source['retrieved_at']}
```

相同 Git commit 與 `--retrieved-at` 會產生完全一致的 `index.json`、README、LICENSE 和 AUTHORS。更新時換成實際取得的新 commit 與擷取日期；`--check` 可核對目前輸出是否與來源一致而不寫檔。若上游資料授權不再是 CC BY-SA 3.0，程式會停止，要求先確認新的再利用條件。

## 授權與改作聲明

原始清單由 awesome-selfhosted contributors 維護，作者名單完整保留於 [AUTHORS](AUTHORS)。上游資料依 [Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) 發布；這份衍生索引同樣採用 **CC BY-SA 3.0**。本目錄中的衍生資料不改採專案根目錄的 MIT 授權。

Open Source Saver 的改作包括：篩選為事實欄位、移除原文描述、統一 JSON 格式、正規化網址、合併同 repo 紀錄、加入穩定 ID、來源版本與未查核標記。軟體本身各有自己的授權，清單資料授權不會取代軟體授權；本索引也不代表上游作者為 Open Source Saver 背書。
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path, help="Local upstream Git checkout")
    parser.add_argument("--commit", default="HEAD", help="Local upstream revision; resolved to full SHA")
    parser.add_argument("--retrieved-at", required=True, help="Actual retrieval date, YYYY-MM-DD")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Compare expected files; do not write")
    args = parser.parse_args()
    try:
        index, outputs = build_index(args.source, args.commit, args.retrieved_at)
        outputs["index.json"] = (json.dumps(index, ensure_ascii=False, indent=2) + "\n").encode()
        outputs["README.md"] = render_readme(index).encode()
        if args.check:
            mismatches = [name for name, content in outputs.items()
                          if not (args.output / name).is_file()
                          or (args.output / name).read_bytes() != content]
            if mismatches:
                raise ValueError("Missing or out-of-date generated files: " + ", ".join(mismatches))
        else:
            args.output.mkdir(parents=True, exist_ok=True)
            for name, content in outputs.items():
                (args.output / name).write_bytes(content)
        print(json.dumps({"mode": "check" if args.check else "write", **index["stats"]}))
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"Import failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
