#!/usr/bin/env python3
"""檢查 repo 內所有 Markdown 檔案的相對連結是否指向存在的檔案/資料夾。

用法：python3 scripts/check-links.py
回傳：0 = 全部有效；1 = 有破連結（逐條列出）
CI 與本機共用同一份，確保「驗證」步驟前後一致。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", ".obsidian", "node_modules"}
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "tel:")


def md_files():
    for p in ROOT.rglob("*.md"):
        if not any(part in SKIP_DIRS for part in p.parts):
            yield p


FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
CODESPAN_RE = re.compile(r"`[^`\n]*`")


def main() -> int:
    broken = []
    for md in md_files():
        text = md.read_text(encoding="utf-8", errors="replace")
        text = FENCE_RE.sub("", text)
        text = CODESPAN_RE.sub("", text)
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            if target.startswith(SKIP_PREFIXES):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                broken.append(f"{md.relative_to(ROOT)} → {target}")
    if broken:
        print(f"❌ 發現 {len(broken)} 條破損的相對連結：")
        for b in broken:
            print(f"  {b}")
        return 1
    print("✅ 所有相對連結有效")
    return 0


if __name__ == "__main__":
    sys.exit(main())
