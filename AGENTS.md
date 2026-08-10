# 🤖 AGENTS.md — 給 Codex（或其他 agent CLI）的入口指南

> Codex 依業界慣例會自動找這個檔名。**這份檔案本身不重複規則內容**，只做三件事：
> 指路、翻譯 Claude Code 專屬機制、標註「哪些狀態查不到、要問使用者」。
> 這樣設計是為了避免跟 `CLAUDE.md` / `memory/MEMORY.md` 內容分裂（發生過一次教訓，見底部）。

---

## 第一步：讀這兩份，不要讀這份文件的舊版摘要

1. **`memory/MEMORY.md`** — 使用者是誰、目前進度、過去決策，**永遠是最新狀態**
2. **`CLAUDE.md`** — 核心工作原則（CLI 優先、context 管理、記憶協定、任務分級、協作制度）

讀完用 3-5 句話跟使用者確認理解，再開始做事。

---

## Claude Code 專屬機制 → Codex 該怎麼做（這段是穩定的，不太會過期）

這個倉庫是用 Claude Code 建的，有幾個機制**沒有 Codex 對應物**，只能靠人工補：

| Claude 專屬 | 做什麼用 | Codex 沒有時怎麼辦 |
|---|---|---|
| **Hooks**（`.claude/settings.json`：SessionStart/Stop/PostToolUse） | 自動載入記憶、自動驗證、自動 push | 沒有自動觸發機制。**每次要主動**：開始先讀 MEMORY.md、改完跑 `python3 scripts/validate_repo.py`、有結論記得叫使用者確認後自己 commit+push |
| **Skill 工具**（`Skill(...)` 呼叫、`.claude-plugin/marketplace.json`） | 一鍵觸發技能 | 沒有這層。技能本體（各資料夾的 `SKILL.md`）是純文字，**直接當參考文件讀**，照裡面的邏輯手動做即可，內容本身沒有遺失 |
| **Subagent**（`.claude/agents/`：red-team/researcher/simplifier/skeptic） | 分工、對抗性審查 | 沒有對應物。重大結論改成自己用「先支持、再反駁自己」的方式過一輪，或誠實跟使用者說「這個沒有第二人審查」 |
| **自訂斜線指令**（`.claude/commands/`） | `/plan`、`/fee-check` 等快捷流程 | 讀對應的 `.md` 內容當一次性指令執行 |
| **fable-harness/**（OODA 協議、驗證閘） | 強制蒐證→假設→行動的紀律，改壞會被攔 | 沒有自動攔截；**自己要求自己**遵守同樣紀律：先蒐證、假設要明講、改動邏輯要有 fail-then-pass 證據 |

## 查不到的狀態（別假設，要問使用者）

以下這些**不在這個倉庫的任何檔案裡**，是 claude.ai 平台或使用者本機的帳號層級設定，Codex 讀不到、也無法代為操作：

- claude.ai 網頁版目前啟用哪些技能（曾記錄過一個時間點的快照，見 `memory/MEMORY.md`，但可能已過期）
- 使用者 Windows 電腦上 Claude Code CLI 裝了哪些 plugin（同上，snapshot 不等於即時狀態）

**遇到需要這些狀態的任務，先問使用者現況，不要憑舊記錄推測。**

## 起手式（複製貼給 Codex 開場用）

```
這是我原本用 Claude Code 維護的倉庫。請先讀：
1. memory/MEMORY.md（我是誰、專案進度、過去決策——這份是最新狀態）
2. CLAUDE.md（核心工作原則）
3. AGENTS.md（Claude Code 專屬機制要怎麼在你這邊代替執行）

讀完用 3-5 句話跟我確認你的理解，再開始做事。
```

## 雙邊並用注意事項

- `memory/MEMORY.md` 是共用真相來源，不管哪個 agent 工作都要讀寫這份，
  更新時標註是哪個 agent 做的（例如「2026-08-10（Codex）：...」）
- **不要同時開兩個 agent 改同一個檔案**——沒有鎖機制，會衝突
- 改動內容盡量用 commit 說明清楚，繁中、結論先行，跟 Claude Code 那邊風格一致

---

## 📌 一次踩過的坑（別重蹈覆轍）

**這份 AGENTS.md 曾經消失過一次**：早期建過一版，因為分支被合併 PR 後又 reset 回 main，
未合併的 commit 直接遺失，沒人發現。後來另一個 session 做了功能重複但**檔名不同**的
`CODEX-HANDOFF.md`，兩份文件並存、內容各自過期。

**現在的作法**：只留這一份 `AGENTS.md` 當入口，`CODEX-HANDOFF.md` 已改成指向這裡的
指標檔（不重複內容）。**以後任何 session 要更新交接資訊，只改這份 + `memory/MEMORY.md`，
不要再開第三份文件。**

---
*建立：2026-07-28｜重建＋改版：2026-08-10（修復分支重置遺失問題，改為指路型設計）*
