#!/usr/bin/env python3
"""FABLE-PROTOCOL 驗證閘（Stop hook）。

偵測：最後一個真實使用者訊息之後，若有 Edit/Write/NotebookEdit 修改程式檔
但沒有任何自動化驗證（測試指令或 scripts/validate_repo.py），就擋下 Stop
並提醒補驗證。

設計原則：fail-open —— 任何異常一律靜默放行（exit 0、無輸出），
閘門絕不可弄壞 session。

自測：python3 verify_gate.py --test
"""
import json
import re
import sys

CODE_EXT = re.compile(
    r"\.(py|js|jsx|ts|tsx|sh|bash|go|rs|java|rb|php|c|cc|cpp|h|hpp|css|scss|vue|svelte)$",
    re.I,
)
EDIT_TOOLS = {"Edit", "Write", "NotebookEdit"}
TEST_CMD = re.compile(
    r"(pytest|python3?\s+-m\s+(pytest|unittest)|npm\s+(test|run\s+test)|npx\s+(jest|vitest|playwright)"
    r"|yarn\s+test|cargo\s+test|go\s+test|rspec|phpunit|validate_repo\.py|bash\s+\S*test\S*\.sh)",
    re.I,
)
SELF_TEST = re.compile(r"--test\b")


def analyze(entries: list[dict]) -> tuple[bool, bool]:
    """回傳 (改了程式檔, 跑了驗證)——只看最後一個真實使用者訊息之後。"""
    last_user = -1
    for i, e in enumerate(entries):
        if e.get("type") != "user":
            continue
        content = (e.get("message") or {}).get("content")
        if isinstance(content, str) or (
            isinstance(content, list)
            and any(b.get("type") == "text" for b in content if isinstance(b, dict))
        ):
            last_user = i
    code_edited = ran_check = False
    for e in entries[last_user + 1 :] if last_user >= 0 else entries:
        content = (e.get("message") or {}).get("content")
        if not isinstance(content, list):
            continue
        for b in content:
            if not (isinstance(b, dict) and b.get("type") == "tool_use"):
                continue
            name, inp = b.get("name", ""), b.get("input") or {}
            if name in EDIT_TOOLS and CODE_EXT.search(str(inp.get("file_path", ""))):
                code_edited = True
            elif name == "Bash":
                cmd = str(inp.get("command", ""))
                if TEST_CMD.search(cmd) and not SELF_TEST.search(cmd):
                    ran_check = True
    return code_edited, ran_check


def self_test() -> int:
    mk_user = lambda t: {"type": "user", "message": {"content": t}}
    mk_tool = lambda n, i: {
        "type": "assistant",
        "message": {"content": [{"type": "tool_use", "name": n, "input": i}]},
    }
    cases = [
        # (entries, 預期 code_edited, 預期 ran_check)
        ([mk_user("改一下"), mk_tool("Edit", {"file_path": "a.py"})], True, False),
        ([mk_user("改"), mk_tool("Edit", {"file_path": "a.py"}),
          mk_tool("Bash", {"command": "python3 scripts/validate_repo.py"})], True, True),
        ([mk_user("寫文件"), mk_tool("Write", {"file_path": "README.md"})], False, False),
        ([mk_tool("Edit", {"file_path": "old.py"}), mk_user("問個問題")], False, False),
        ([mk_user("測"), mk_tool("Bash", {"command": "python3 verify_gate.py --test"})], False, False),
    ]
    for n, (entries, want_edit, want_check) in enumerate(cases, 1):
        got = analyze(entries)
        assert got == (want_edit, want_check), f"case {n}: got {got}"
    print("✅ verify_gate 自測 5/5 通過")
    return 0


def main() -> int:
    if "--test" in sys.argv:
        return self_test()
    try:
        payload = json.load(sys.stdin)
        if payload.get("stop_hook_active"):  # 已經被本閘擋過一次，放行避免迴圈
            return 0
        path = payload.get("transcript_path")
        if not path:
            return 0
        entries = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
        code_edited, ran_check = analyze(entries)
        if code_edited and not ran_check:
            print(json.dumps({
                "decision": "block",
                "reason": "🧪 FABLE 驗證閘：本輪修改了程式檔但未見自動化驗證。"
                          "請跑對應測試或 python3 scripts/validate_repo.py 附上結果；"
                          "若確實不需驗證，向使用者說明原因後再結束。",
            }, ensure_ascii=False))
    except Exception:
        pass  # fail-open：閘門絕不可弄壞 session
    return 0


if __name__ == "__main__":
    sys.exit(main())
