# 🤖 AGENTS.md — 給 Codex（或其他 agent CLI）的專案指南

> 本檔案是從 `CLAUDE.md` + `memory/MEMORY.md` 轉譯過來的版本，
> 目的是讓 Codex CLI（讀取 AGENTS.md 慣例）或其他 agent 工具能理解這個倉庫的規則與現況。
> 完整原版仍是 `CLAUDE.md`（Claude Code 專用）+ `memory/MEMORY.md`（長期記憶），
> 兩邊內容打架時，**先讀那兩份，本檔案只是搬運/摘要**。

---

## 👤 使用者背景

- 語言：繁體中文（台灣），非工程師背景
- 工作領域：物業管理 / 會計行政（大樓財報稽核、社區管理費對帳、勞保勞健保）
- 溝通偏好：**結論先行 + 明確建議**（值不值得做、該不該做），不要丟一堆資訊讓他自己判斷
- 格式偏好：表格 + emoji 的繁中報告

## 🎯 核心工作原則（從 CLAUDE.md 翻譯）

1. **能用 CLI 就不要用 MCP／重工具**：查文件用 `cat`/`grep`，提交代碼用 `git`，
   不要為小事動用需要大量 token 的外部整合工具
2. **保持 context 乾淨**：長任務拆小、結論寫進檔案而非全部塞對話裡
3. **長期記憶**：這個倉庫用 `memory/MEMORY.md` 記錄使用者輪廓/偏好/專案進度。
   **任何 agent 接手這個倉庫，第一件事都應該先讀這個檔案。**
   學到新事實/決策 → 更新並記錄
4. **任務分級協定**：
   - 小任務（單檔修改、查詢）→ 直接做
   - 中大型任務（多檔案、新系統）→ 先寫計畫到 `memory/plans/<日期>-<任務名>.md`，
     使用者確認後才動手，做完寫結果回記憶檔
5. **改功能邏輯要有 fail-then-pass 證據**：先證明問題存在，改完再證明修好了，
   不能只憑「看起來對」

## 📂 倉庫結構速覽

```
awesome-claude-skills-zh-TW/
├─ CLAUDE.md              ← Claude Code 專用指南（本檔案的原始版本）
├─ AGENTS.md              ← 本檔案，給 Codex/其他 agent 看
├─ memory/
│  ├─ MEMORY.md           ← 🔴 長期記憶，每次接手必讀
│  └─ plans/              ← 任務計畫檔（含 bpm-project/ 等子專案紀錄）
├─ scripts/validate_repo.py  ← 倉庫一致性驗證（技能↔marketplace↔README）
├─ harness/                ← Claude 專屬協作制度（見下方「不會搬過去的東西」）
├─ *-skill/ 或各技能資料夾/  ← 60+ 個技能，格式為 SKILL.md（部分含 SKILL.zh-TW.md）
└─ .claude/                ← Claude Code 專屬設定（hooks、subagent、settings.json）
```

## ✅ Codex 可以直接沿用的部分

- **`memory/MEMORY.md`**：純 Markdown，Codex 讀了就懂使用者是誰、專案進度、過去決策
- **`memory/plans/`**：計畫檔與紀錄，純文字，直接讀
- **技能內容本身**：`*/SKILL.md` 裡的邏輯、腳本（如 xlsx 稽核腳本、財報對帳邏輯）是
  Python/純邏輯，Codex 可以直接執行或參考，不依賴 Claude 專屬機制
- **`scripts/validate_repo.py`**：一般 Python script，任何 agent 都能跑
  ```bash
  python3 scripts/validate_repo.py
  ```
- **Git 操作、任務協定、溝通風格**：這些是「怎麼做事」的原則，跟工具無關，照抄就對

## ⚠️ 不會直接搬過去的東西（Claude Code 專屬機制）

| Claude 專屬功能 | 做什麼用 | Codex 沒有對應物時怎麼辦 |
|---|---|---|
| **Skill 工具**（`Skill(...)` 呼叫） | 把技能包裝成可一鍵呼叫的指令 | Codex 沒有同名機制；把技能內容當「參考文件」讀，照著邏輯手動做，或請 Codex 直接讀 SKILL.md 內文當 prompt |
| **Subagent**（Agent 工具、researcher/skeptic/red-team 等） | 分工、平行研究、對抗性審查 | Codex 若支援 sub-session/parallel task 可近似；否則單一 session 循序做，品質会打折但功能不缺 |
| **Hooks**（`.claude/settings.json` 的 SessionStart/Stop/PostToolUse） | 自動載入記憶、自動驗證、自動 push | **這是最大的落差**。Codex 沒有這套 hook 系統，等於「自動提醒/自動擋錯」機制消失，
  要嘛找 Codex 自己的 hook/plugin 機制做等效設定，要嘛改成**每次手動要求**：「先讀 memory/MEMORY.md」「改完跑 validate_repo.py」「跑完記得 commit + push」 |
| **fable-harness/**（OODA 協議、驗證閘） | 強制走「蒐證→假設→抗辯→行動」流程，改壞東西會被攔下 | 沒有自動攔截機制；改為在 prompt 裡明確要求 Codex 遵守同樣紀律（本檔案已把核心原則翻譯過來） |
| **MCP 連接器**（Gmail、Drive、Notion、Canva、Gamma、Zoom、GitHub MCP） | claude.ai 帳號層級的整合 | 這些是 claude.ai 平台功能，跟 Codex 無關，Codex 若要連同樣服務要另外設定（多半用官方 CLI 或 API） |

## 🚀 給 Codex 的建議起手式

如果要用 Codex 接手這個倉庫，第一則訊息可以這樣寫：

```
這是我原本用 Claude Code 維護的倉庫。請先讀這幾個檔案了解狀況：
1. memory/MEMORY.md（我是誰、專案進度、過去決策）
2. AGENTS.md（工作原則，取代 Claude Code 的 CLAUDE.md）
3. memory/plans/（進行中任務的計畫紀錄）

讀完用 3-5 句話跟我確認你的理解，再開始做事。
之後每次改動：改完先驗證（python3 scripts/validate_repo.py），
有結論就更新 memory/MEMORY.md 並 commit。
```

## 🔀 雙邊並用注意事項（如果 Claude Code 和 Codex 都在用）

- **`memory/MEMORY.md` 是共用真相來源**：不管哪個 agent 工作，都要讀這份、
  改完都要寫回這份 —— 這樣兩邊才不會各自為政、互相蓋掉對方的紀錄
- 建議在 `memory/MEMORY.md` 每次更新時**標註是哪個 agent 做的**
  （例如「2026-07-28（Codex）：...」），方便回頭追溯是誰改的
- Git commit 訊息維持一致風格（繁中、結論先行），不管哪個工具生成的
- **不要同時開兩個 agent 改同一個檔案**——沒有鎖機制，會衝突

---
*建立日期：2026-07-28（由 Claude 建立，供 Codex 交接使用）*
