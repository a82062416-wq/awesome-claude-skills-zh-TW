#!/usr/bin/env python3
"""倉庫健康檢查：驗證 JSON 設定與技能結構。

用法:
  python3 scripts/validate_repo.py          # 嚴格模式（CI 用）：有錯誤 exit 1
  python3 scripts/validate_repo.py --hook   # hook 模式：只印警告，永遠 exit 0
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOK_MODE = "--hook" in sys.argv
errors: list[str] = []
warns: list[str] = []


def check_json(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
        if "�" in text:
            errors.append(f"{path.name}: 內含損壞字元（U+FFFD）")
        return json.loads(text)
    except FileNotFoundError:
        errors.append(f"{path} 不存在")
    except json.JSONDecodeError as e:
        errors.append(f"{path.name}: JSON 解析失敗 — {e}")
    return None


def check_frontmatter(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        warns.append(f"{skill_md.relative_to(ROOT)}: 缺少 YAML frontmatter")
        return
    fm = m.group(1)
    for field in ("name:", "description:"):
        if field not in fm:
            warns.append(f"{skill_md.relative_to(ROOT)}: frontmatter 缺 {field[:-1]}")


# 1. 設定檔 JSON 必須有效
mp = check_json(ROOT / ".claude-plugin" / "marketplace.json")
check_json(ROOT / ".claude" / "settings.json")

# 2. marketplace 每個 plugin 的 source 必須存在且含 SKILL.md
if mp:
    for p in mp.get("plugins", []):
        src = ROOT / p.get("source", "").lstrip("./")
        if not src.is_dir():
            errors.append(f"marketplace: {p['name']} 的 source 目錄不存在（{p['source']}）")
        elif not (src / "SKILL.md").is_file():
            errors.append(f"marketplace: {p['name']} 缺 SKILL.md（{p['source']}）")

# 3. 所有 SKILL.md 的 frontmatter 完整性
for skill_md in sorted(ROOT.glob("*/SKILL.md")) + sorted(ROOT.glob("*/*/SKILL.md")):
    check_frontmatter(skill_md)

# 4. 只有 zh-TW 版而沒有 SKILL.md 的資料夾（載入器不認得，形同死資產）
for zh in sorted(ROOT.glob("*/SKILL.zh-TW.md")) + sorted(ROOT.glob("*/*/SKILL.zh-TW.md")):
    if not (zh.parent / "SKILL.md").is_file():
        errors.append(f"{zh.parent.relative_to(ROOT)}: 只有 SKILL.zh-TW.md，Claude Code 不會載入")

# 5. 記憶檔大小控制（協定上限 150 行，寬限到 200）
mem = ROOT / "memory" / "MEMORY.md"
if mem.is_file():
    lines = len(mem.read_text(encoding="utf-8").splitlines())
    if lines > 200:
        warns.append(f"memory/MEMORY.md 已 {lines} 行（協定上限 150）— 該歸檔瘦身了")

for w in warns:
    print(f"⚠️  {w}")
for e in errors:
    print(f"❌ {e}")

if not errors and not warns:
    print("✅ 倉庫健康檢查全數通過")
elif not errors:
    print(f"✅ 無錯誤（{len(warns)} 個警告）")

sys.exit(0 if (HOOK_MODE or not errors) else 1)
