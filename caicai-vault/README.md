# 菜菜 Vault

這是菜菜的個人知識庫，供 AI Agent（JACK）讀取使用。

---

## 資料夾結構與檔案索引

```
/
  README.md              ← 你正在讀的這份
  agent-persona.md       ← JACK 的人格設定：三層（Identity/Soul/Persona）、反駁與服從時機、溝通風格
  memory-summary.md      ← 長期記憶摘要：Sticky 提醒、重要決策表、菜菜的模式、當前焦點

  /identity              ← 菜菜是誰
    decision-style.md    ← 決策風格：數據驅動為主；品質標準與卡關模式待補
  /context               ← 公司背景
    company-overview.md  ← 公司基本盤（公開佔位版；完整數據在私有 Vault）
  /memory                ← 重要決策紀錄、會議結論 → 讀 INDEX.md
  /sop                   ← 操作流程
    after-action.md      ← 收官三步：寫 memory → 更新相關文件 → 更新 memory-summary
    git-workflow.md      ← Day-2 Git 操作：同步、第二台機器、衝突處理、救援
    vault-changelog.md   ← 核心檔案更新 log 的歷史存放處（結構性事件）
    vault-audit.md       ← Vault 索引健檢 SOP：抓漏 index 的檔案與過時條目，每月跑一次
  /operations            ← 公司營運資料（規章制度、勞保勞動法規、系統開發）— 尚無檔案
  /projects              ← 各項目的狀態 → 讀 INDEX.md（收官的搬 archive/）
  /people                ← 重要聯絡人背景 — 尚無檔案
  /skills                ← JACK 的技能檔案（可迭代重複運用的工作流程）
    document-intake.md   ← 文件收件流程：丟檔案 → 判斷所屬專案 → 修正/完成/歸檔 → 收官
```

變動慢的資料夾（identity/、context/、sop/、operations/）在這裡逐檔詳列；會堆疊的資料夾（memory/、projects/）各自維護 `INDEX.md`，這裡只留一行入口。進資料夾前先讀它的 `INDEX.md`。

## Agent 閱讀順序

1. 讀這份 README（了解整體結構）
2. 讀 `agent-persona.md`（了解自己的角色與協作方式）
3. 讀 `memory-summary.md`（掌握近期重要事項）
4. 依任務需要，讀對應資料夾的內容

## 命名規則

- 檔名即索引：用描述性檔名，避免泛稱（`hr-hiring-strategy.md`，不要 `notes.md`）
- 同分類用 `主題-子項` 格式，主題在前（`client-highend-strategy.md`、`client-highend-pipeline.md`）
- memory/ 檔名：`YYYY-MM-DD_主題.md` · projects/ 資料夾：`YYYY-MM-主題/`

## 🚨 強制規則（不是建議）

### #1 — 索引同步
- **新增 / 刪除檔案** → 當次 response 內改對應資料夾的 `INDEX.md`（有 INDEX 的資料夾）
- **新增 / 刪除「資料夾」或其他結構性變動** → 改這份 README（資料夾描述 + 底部更新 log）

### #2 — 對外文稿規則
只要這段文字**會被菜菜以外的人看到**（客戶提案、公司公告、對外文件、公開貼文等），撰寫前必須讀 `identity/voice-and-tone.md`。不確定時視為對外。

兩條都是完成任務的必要條件。第二道安全網：收官檢查（after-action）時再確認一次。

## 維護原則

- 一個事實只寫在一個地方（Single Source of Truth）
- 建新檔案前先搜尋有沒有現有的
- 每份文件開頭標注最後更新日期
- 敏感資訊（API key、密碼、員工個資）不進這個 repo

---

*最後更新：2026/07/06（persona 定稿：中文強制、表格偏好、爭論界線 + 第一個技能 skills/document-intake.md）*
*前次更新：2026/07/06（檢索優化：README 索引細化到檔案層級 + sop/ 補 frontmatter）*

*📏 更新 log 規則：只留最近兩條。新增一條時，把被擠掉的那條搬進 `sop/vault-changelog.md`。*
