# 🧠 長期記憶（每次 session 開始必讀）

> 規則：Claude 在這個倉庫工作時，session 開始先讀這份檔案；
> 學到關於使用者的新事實、偏好、專案狀態時，立即更新本檔並 commit（hooks 會自動推送）。
> 保持精簡：只記「下次 session 還需要知道」的事，過時內容直接刪除。

## 👤 使用者輪廓

- 主要語言：繁體中文（台灣）
- Email：a82062416@gmail.com
- 工作領域：物業管理 / 會計行政（大樓財報稽核、社區管理費對帳、勞保勞健保事務、出勤管理）
- 服務的物件：長谷蓮清大樓（財報稽核）、悅讀ABC社區（管理費收繳）
- 技術程度：非工程師背景，靠 Claude Code 自動化工作流；喜歡把重複工作做成 Skill

## ⚙️ 使用偏好

- 稱 Claude Code 為「cloud code / cloud cold」（口語）
- 重視 token 成本：CLI 優先 > Skills > MCP（見 CLAUDE.md）
- 希望 context/頁面保持乾淨，不喜歡冗長輸出
- 希望 Claude 有長期記憶、越用越聰明
- 喜歡表格 + emoji 的繁中報告格式
- 🌟 最重視「結論式總結 + 幫他判斷」：非工程師，要的是「值不值得／該不該做」的明確建議
  與對比，不是一堆資訊讓他自己消化。評估外部工具/插件時先下判斷再給理由（他明確說「這樣比較清楚」）

## 📌 環境狀態（2026-07-07 Phase 1-3 強化後）

- claude.ai 已啟用 20 個技能：6 個自訂 + 14 個官方
- ⚠️ 待辦：community-fee-reconciliation 應只留 v3，v1/v2 待使用者在 claude.ai 停用
- MCP 連接器：Gmail、Calendar、Drive、Notion、Canva、Gamma、Zoom 已連線；Ahrefs、Figma 未啟用
- 倉庫 hooks（已重寫）：SessionStart 自動載入本記憶檔；Write/Edit 後先驗證再暫存；
  Bash 後有未推送 commit 且工作區乾淨才 push
- 自訂指令：/plan（規劃模式）、/monthly-audit（財報稽核）、/fee-check（管理費對帳）、/retro（回顧寫記憶）
- Subagent：researcher（.claude/agents/，研究只回結論保持 context 乾淨）
- 閉環驗證：scripts/validate_repo.py（hook 寬鬆模式 + CI 嚴格模式）+ GitHub Actions
- 任務協定：CLAUDE.md 原則 4——中大型任務必走「理解→計畫（memory/plans/）→執行→驗證→交付紀錄」
- Fable Harness（2026-07-07 安裝，改編自 Miguok/fable-harness）：SessionStart 注入
  FABLE-PROTOCOL（代號 FABLE-PROTOCOL-V1-CANARY）、每輪 OODA 微提醒、Stop 驗證閘
  （改程式沒驗證會被擋）、adversarial-review 技能 + skeptic/red-team/simplifier 三反方 agent
- 🏛️ 協作制度（2026-07-07，Fable 5 唯一 session 的交接產物）：`harness/` 目錄——
  派工三件套、升降級路徑、判斷力矩陣、派工模板、反思協議、交接信。
  弱模型接手第一件事：讀 harness/00-diagnosis.md 與 06-handoff-letter.md
- ⚠️ 未完成：每週巡檢 Routine 被平台 MCP 核准層擋住（永久阻斷，勿重試——
  見 harness/00-diagnosis.md），待使用者在 claude.ai/code 介面手動建立

## 📚 專案進行中

### 🎯 BPM 項目（主線：dys-bpm Vue 項目）
- **決策**（2026-07-10）：放棄新工具探詢，全力做 BPM
- **決策**（2026-07-15）：此倉庫內的 nuBPM HTML 原型**不繼續迭代**
  - 原因：真正工程已在 `a82062416-wq/dys-bpm`（Vue 3 + Vite）進行
  - 此倉庫的 v2 原型已驗證 UX 想法，存檔參考即可
  - 分支 claude/cloud-cold-integration-nq01ha：已修復 git 簽署，待關閉

- 2026-07-08 八大強化（分支 claude/cloud-cold-integration-nq01ha，三批已推送）：
  harness/07-audit-blueprint.md（8面向診斷藍圖）、16個台灣物業會計新技能、
  validate 第6檢查（技能↔marketplace↔README 一致性控制單元）、SKILL 模板、
  gitignore 安全強化。marketplace 從 29→61 註冊全一致


- `awesome-claude-skills-zh-TW`：繁中技能收藏庫 + plugin marketplace（41 個可載入技能）
- PR #3（2026-07-07 完成合併）：整合報告 + 影片/記憶技能 + 技能樹儀表板 + Harness Phase 1-3
- 完整環境盤點見 `CLAUDE-CODE-整合分析報告.md`；技能總覽見 `skill-tree.html`
- 🗺️ 倉庫導覽分類看 `INDEX.md`（63 技能按用途分 11 類 + 六層結構）；
  技能實體平鋪根目錄未搬移（動路徑風險高），靠 INDEX 索引導覽

## 💡 已學到的教訓

- 2026-07-15 決策：此倉庫的 nuBPM HTML 原型（v2）已存檔，不繼續做。真正 BPM 工程轉向 dys-bpm Vue 項目。
  此倉庫改為「技能倉庫 + 記憶庫」，不再做項目型原型。
  
- 2026-07-15 決策：工具探詢迴圈浪費 tokens（裝了 OpenJarvis 但無 API key）。應及時轉向項目交付。
  用戶判斷力清晰，能快速決策「哪邊已經有了」，應尊重並立即轉向。
  
- 2026-07-07 決策：34 個 SKILL.zh-TW.md 技能因檔名不符從未被載入 → 複製為 SKILL.md 雙檔並存
  （不改名，保留中文版可讀性）；驗證腳本永久防止此類問題復發
- 2026-07-07 決策：自動 push 條件改為「有未推送 commit 且工作區乾淨」，原 hooks 的
  "if" 欄位不是官方 schema、從未生效；marketplace 幽靈條目 algorithmic-art 已移除

- 使用者的組織插件目錄（knowledge-work-plugins）沒有 claude-mem/Remotion/Superpowers，
  帳號層級裝不了 → 改用倉庫內建技能 + 檔案式記憶（本系統）
- 雲端 session 是暫時容器，任何要保存的東西都必須 commit 進 git

---
*最後更新：2026-07-15（session：cloud-cold-integration-收工）*
