# 🩺 環境診斷書（2026-07-07，Fable 5 出具）

## 環境現況（接手時的狀態）

| 層 | 狀態 | 證據 |
|----|------|------|
| 記憶 | ✅ memory/MEMORY.md + SessionStart 自動注入 | .claude/settings.json hooks |
| 任務協定 | ✅ CLAUDE.md 原則 4（理解→計畫→執行→驗證→交付） | CLAUDE.md |
| 行為協議 | ✅ FABLE-PROTOCOL（OODA、fail-then-pass、誠實回報） | fable-harness/ |
| 驗證閉環 | ✅ validate_repo.py（hook 寬鬆 + CI 嚴格）+ Stop 驗證閘 | scripts/、.github/workflows/ |
| 例行指令 | ✅ /plan /monthly-audit /fee-check /retro | .claude/commands/ |
| Subagents | ✅ researcher + skeptic/red-team/simplifier | .claude/agents/ |
| 協作制度 | ✅ 本目錄（派工、升降級、判斷矩陣、模板、反思、交接） | harness/ |

## 已知平台限制（不要浪費時間重試）

1. **claude-code-remote MCP 的寫入工具被核准層擋死**：create_trigger、send_later、
   add_repo 全部回「requires approval」且核准流程斷裂。試過 5+ 次。
   → 排程改用使用者手動建 Routine；外部倉庫改用 WebFetch 讀公開內容後原生實作
2. **WebFetch 用小模型摘要頁面**：拿不到長檔案的逐字內容，只能拿摘要。
   要逐字內容時分段要求、或對短檔案效果較好
3. **雲端容器是暫時的**：沒 commit + push 的東西 = 不存在。~/.claude/ 全域設定會蒸發，
   一切持久化都走專案內檔案 + git

## ⚖️ 誠實條款：本制度的能力極限

這套 harness 能讓弱模型逼近高階品質的部分：**流程紀律、錯誤攔截、驗證完整性、
記憶延續**。以下是它「注定做不到」的，弱模型遇到時的標準應對：

### 極限 1：模糊的商業美感與品味決策
設計方向、文案語感、「哪個看起來比較高級」——檢核表無法量化品味。
**應對標準**：
- 禁止自由發揮。優先沿用既有範本（theme-factory 主題、frontend-design 錨點、
  過往已被使用者接受的產出——去 memory/archive/ 和 git 歷史找）
- 產出 2-3 個變體 + 各自一句話理由，讓使用者選，不要自己定案
- 使用者說「你決定就好」時，選最保守、最像既有作品的那個

### 極限 2：全新架構決策（無前例可循的技術選型）
**應對標準**：跑 adversarial-review 三鏡頭抗辯，裁決照該技能的過半存活制
（存活 2 票或 3 票 → 採信，2 票時附風險清單；存活 ≤1 票 → 擋回）。
被擋回且修正後仍 ≤1 票存活時，帶著選項與利弊向使用者提問
（見 03-judgment-matrix.md 熔斷段）。不要假裝有把握。

### 極限 3：跨領域的隱含業務知識
勞健保費率變動、社區管理慣例、法規更新——模型記憶會過時。
**應對標準**：涉及金額/法規/日期的計算，先 WebSearch 確認當年度數值並附來源；
查不到就明確標註「以 X 年資料計算，請確認現行值」。**不確定的事就查，
查不到就標註，絕不編造。**

### 極限 4：長鏈推理的靜默錯誤
弱模型在 10+ 步的推理鏈中會不自覺出錯且不自知。
**應對標準**：把長鏈拆成可獨立驗證的短段（01-delegation.md）；每段用工具實證
（跑指令、讀檔案），不用「我認為」串接兩個事實。
