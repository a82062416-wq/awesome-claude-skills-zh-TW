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
- ⚠️ 未完成：每週巡檢 Routine 被平台 MCP 核准層擋住，待使用者在 claude.ai/code 介面手動建立
  或之後 session 重試 create_trigger

## 📚 專案進行中

- `awesome-claude-skills-zh-TW`：繁中技能收藏庫 + plugin marketplace（41 個可載入技能）
- PR #3（2026-07-07 完成合併）：整合報告 + 影片/記憶技能 + 技能樹儀表板 + Harness Phase 1-3
- 完整環境盤點見 `CLAUDE-CODE-整合分析報告.md`；技能總覽見 `skill-tree.html`

## 💡 已學到的教訓

- 2026-07-07 決策：34 個 SKILL.zh-TW.md 技能因檔名不符從未被載入 → 複製為 SKILL.md 雙檔並存
  （不改名，保留中文版可讀性）；驗證腳本永久防止此類問題復發
- 2026-07-07 決策：自動 push 條件改為「有未推送 commit 且工作區乾淨」，原 hooks 的
  "if" 欄位不是官方 schema、從未生效；marketplace 幽靈條目 algorithmic-art 已移除

- 使用者的組織插件目錄（knowledge-work-plugins）沒有 claude-mem/Remotion/Superpowers，
  帳號層級裝不了 → 改用倉庫內建技能 + 檔案式記憶（本系統）
- 雲端 session 是暫時容器，任何要保存的東西都必須 commit 進 git

---
*最後更新：2026-07-07（session：cloud-cold-integration）*
