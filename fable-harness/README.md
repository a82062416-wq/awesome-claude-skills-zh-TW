# 🧭 Fable Harness（本倉庫原生實作版）

改編自 [Miguok/fable-harness](https://github.com/Miguok/fable-harness)（MIT License）。

因雲端環境無法直接 clone 外部倉庫，2026-07-07 依原專案 INSTALL.md 規格
**原生重新實作**：三個 hook 腳本經逐檔安全審查後等價重寫（繁中化），
`verify_gate.py` 為全新實作並附自測（`python3 verify_gate.py --test`）。

## 組件

| 組件 | 位置 | 觸發 |
|------|------|------|
| 行為協議注入 | `hooks/inject_protocol.sh` + `fable_protocol.md` | SessionStart |
| 每輪微提醒 | `hooks/prompt_nudge.sh` | UserPromptSubmit |
| 驗證閘（fail-open） | `hooks/verify_gate.py` | Stop |
| 多方抗辯技能 | `.claude/skills/adversarial-review/` | 重大結論時 |
| 三反方 subagent | `.claude/agents/{skeptic,red-team,simplifier}.md` | 由抗辯技能派出 |

## 驗證安裝

新 session 問：「你的協議代號是什麼？」→ 應回答 `FABLE-PROTOCOL-V1-CANARY`。

## 與原版差異

- 安裝位置：專案 `.claude/`（非全域 `~/.claude/`）——雲端容器是暫時的，
  只有進 git 的設定才能跨 session 存活
- 全部繁中化；驗證閘的測試指令清單加入本倉庫的 `scripts/validate_repo.py`
- 協議文與 CLAUDE.md 四原則整合（記憶、CLI 優先、context 乾淨、任務協定）
