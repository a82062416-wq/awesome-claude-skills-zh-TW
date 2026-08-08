# 交接文件：給 CODEX（或任何接手的 AI 工具）

> 這份文件整理「awesome-claude-skills-zh-TW」倉庫目前的完整狀態，讓 CODEX 接手時
> 不用重新問一輪就能理解上下文。內容來源：`memory/MEMORY.md`（長期記憶）、
> `memory/plans/`（任務計畫檔）、git 提交紀錄、`INDEX.md`（倉庫導覽）。
> 產生時間：2026-08-06。

---

## 1. 這是誰、這個倉庫是做什麼的

**使用者輪廓：**
- 繁體中文（台灣）使用者，Email：a82062416@gmail.com
- 工作領域：物業管理 / 會計行政（大樓財報稽核、社區管理費對帳、勞健保事務、出勤管理）
- 服務的物件：長谷蓮清大樓（財報稽核）、悅讀ABC社區（管理費收繳）
- **非工程師背景**，靠 AI CLI 工具自動化日常工作流程；喜歡把重複性工作做成「技能」
  （Claude Skills 概念：一個資料夾 + SKILL.md，定義一套可重複觸發的工作流程）

**倉庫定位：**
`a82062416-wq/awesome-claude-skills-zh-TW` 是一個繁體中文的 Claude Skills 收藏庫，
同時也是一個 plugin marketplace（`.claude-plugin/marketplace.json`），目前收錄
**68 個技能**，分兩大類：
1. 台灣物業會計專用技能包（約 20 個）——這是使用者最核心、別人抄不走的資產
2. 通用工作流技能（設計、開發、文件處理、資料分析等）——多數翻譯/改編自社群其他倉庫

---

## 2. 使用者偏好（溝通風格，務必遵守）

- **回報結論先行**，繁體中文，少用術語黑話
- 喜歡表格 + emoji 的輕快格式，但**誠實 > 討喜**——壞消息、失敗、不確定要直說，不要粉飾
- 重視成本效益：CLI 指令優先 > Skills > MCP 工具（MCP 的 schema 很吃 token）
- 希望對話/頁面保持精簡，不要冗長輸出
- 曾表達對 Claude Code 介面「複雜、沒中文版」的不滿，考慮過改用 CODEX——
  最後決定「保留這個倉庫（繁中專化資產不宜捨棄）+ 補齊技能空缺」，
  但顯然仍在評估要不要把日常操作介面換成 CODEX，這份文件就是為此準備的

---

## 3. 目前的技術狀態

### 3.1 倉庫結構（六層）
| 層 | 內容 |
|---|---|
| 技能 | 68 個技能資料夾平鋪在根目錄，靠 `INDEX.md` 分類導覽（不做實體搬移，避免打斷路徑引用） |
| 制度 | `CLAUDE.md`（核心原則）、`harness/`（弱模型協作制度：派工、升降級、判斷矩陣、交接信） |
| 記憶 | `memory/MEMORY.md`（長期記憶主檔）、`memory/plans/`（任務計畫檔）|
| 工具 | `scripts/validate_repo.py`（健康檢查）、`.github/workflows/`（CI）|
| 產出物 | `skill-tree.html`、`CLAUDE-CODE-整合分析報告.md` |
| 文件 | `README.md` / `README.en.md` / `CONTRIBUTING.md` / 本檔 |

### 3.2 驗證機制
每次改動後必跑：
```bash
python3 scripts/validate_repo.py
```
檢查項目：marketplace.json 有效性、每個 plugin 的 source 目錄與 SKILL.md 存在且被 git 追蹤、
SKILL.md frontmatter 完整性、記憶檔大小上限。CI（GitHub Actions）在每次 push/PR 時強制跑同一支腳本。

### 3.3 使用者本機環境（Windows）
使用者已在自己的 Windows 電腦上，透過 Claude Code CLI 完成本倉庫**全部 68 個技能**的安裝：
```bash
claude plugin marketplace add https://github.com/a82062416-wq/awesome-claude-skills-zh-TW
claude plugin install <技能名稱>   # 逐一裝過 68 個
```
全部顯示 `enabled`。**這件事跟本倉庫的 git 內容無關**——是使用者電腦上 Claude Code 的全域插件設定，
CODEX 若要提供對等能力，需要另外設計自己的技能載入機制（CODEX 不吃 `.claude-plugin/marketplace.json` 格式）。

---

## 4. 最近完成的工作（時間序）

1. **2026-07-07**：Harness Phase 1-3——弱模型協作制度（`harness/` 十份文件）、
   Fable Harness（FABLE-PROTOCOL 行為協議、OODA 提醒、Stop 驗證閘）、
   長期記憶系統上線、SKILL.zh-TW.md 雙檔並存修復（34 個技能因檔名不符從未被載入）
2. **2026-07-08**：八大面向強化——`harness/07-audit-blueprint.md`（診斷藍圖）、
   新增 16 個台灣物業會計技能、marketplace 一致性檢查（第 6 檢查項）、SKILL 模板、
   gitignore 安全強化。技能數 29→61。之後又加 INDEX.md 導覽地圖，技能數到 63
3. **2026-07-31**：研究 ComposioHQ/awesome-claude-skills（71k star 的英文通用倉庫）後，
   確認本倉庫「資料與分析」分類原本全是台灣物業會計專用技能，通用資料分析/根因追蹤/
   履歷客製化/TDD/測試修復是真空缺 → 新增 5 個繁中原創技能：
   `csv-data-analyzer`、`root-cause-tracing`、`resume-tailor`、`tdd-workflow`、`test-fixing`。
   技能數 63→68。計畫檔：`memory/plans/2026-07-31-補齊通用技能空缺.md`（PR #9，已合併）
4. **2026-08-03**：記錄使用者本機已完成全部 68 個技能安裝（PR #10，已合併）

---

## 5. 已學到的教訓（避免重蹈覆轍）

- **34 個 SKILL.zh-TW.md 技能因檔名不符從未被載入**——Claude Code 只認 `SKILL.md`，
  中文版檔名要雙檔並存（不是改名，是複製一份 `SKILL.md`）
- **GitHub MCP 在此環境僅允許操作本倉庫本身**，查其他倉庫（如 ComposioHQ）一律要改用
  網頁抓取，不要嘗試對外部倉庫呼叫 `get_file_contents` 之類的 API（會被拒絕）
- **Squash merge 之後同一分支不能直接繼續加新 commit 再開 PR**——squash 後 master 上的
  提交雜湊跟原分支不同，會導致下一個 PR 誤判成衝突（因為 diff 被要求重複套用）。
  正確做法：merge 完成後，把分支 reset 到最新 master，再 cherry-pick 真正新增的 commit
- **雲端 session 是暫時容器**，任何要保存的東西都必須 commit + push 進 git，
  不存在「之後再存」這回事——容器隨時可能被回收
- 使用者的組織插件目錄（knowledge-work-plugins）沒有 claude-mem/Remotion/Superpowers，
  帳號層級裝不了 → 改用倉庫內建技能 + 檔案式記憶（本系統）

---

## 6. 待辦 / 未完成事項

- ⚠️ claude.ai 網頁版上有 `community-fee-reconciliation` v1/v2/v3 三個版本同時啟用，
  應該只留 v3，v1/v2 待使用者自己在 claude.ai 介面手動停用（AI 端無法代為操作帳號設定）
- ⚠️ 每週巡檢 Routine 曾被平台 MCP 核准層永久阻斷，不要重試，待使用者在 claude.ai/code
  介面手動建立（細節見 `harness/00-diagnosis.md`）
- Firecrawl（網頁抓取/爬蟲工具，`firecrawl/firecrawl`，146.7k star）——使用者曾表達興趣，
  尚未決定要用託管 API 還是自架，這件事**還沒開始做**
- Token Monitor（`Javis603/token-monitor`，桌面用量監控小工具）——已提供下載連結給使用者，
  是否已安裝完成未知，跟本倉庫技術無關

---

## 7. 給 CODEX 的具體建議

1. **先讀 `memory/MEMORY.md`**（比這份文件更即時，本文件是某個時間點的快照）
2. 改動技能/marketplace 後**務必跑 `python3 scripts/validate_repo.py`**，這是本倉庫唯一的
   閉環驗證方式，CI 也靠它把關
3. 開發規範按 `CLAUDE.md` 五大原則（CLI 優先、context 乾淨、長期記憶、任務協定、
   `harness/` 協作制度）——即使 CODEX 不是 Claude Code，這些原則（尤其「改動前先讀記憶、
   中大型任務先寫計畫檔再執行」）依然適用，是這個使用者長期形成的工作習慣，照著做溝通成本最低
4. 使用者是非工程師，**任何會影響對外可見狀態的操作**（push、開 PR、合併、刪除）
   先確認再做——這不是本倉庫的規則，是這位使用者一貫的期待
5. 有問題時用**這份文件 + `memory/MEMORY.md` + `harness/06-handoff-letter.md`**
   三份拼起來，基本上能重建完整脈絡，不需要使用者從頭解釋一遍
