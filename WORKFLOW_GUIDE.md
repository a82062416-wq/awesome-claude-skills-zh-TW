# 🎯 三層指令澄清工作流

> 為容易「指令不夠明確」的開發者設計的自動化工作流

---

## 工作流程圖

```
你的指令
  ↓
1️⃣ Prompt Improver (自動檢查)
   ├─ 清楚？直接執行 ✅
   └─ 模糊？提問澄清 🤔
  ↓
2️⃣ Brainstorming (強制思考)
   ├─ 理解需求
   ├─ 提問細節
   ├─ 設計方案
   └─ 你批准後才編碼 ✓
  ↓
3️⃣ Karpathy Skills (編碼規範)
   └─ 確保代碼品質 ⭐
```

---

## 每層的作用

### 第一層：Prompt Improver 🛡️
**自動檢查提示詞清晰度**

| 情況 | 動作 |
|------|------|
| 指令清楚 | ✅ 直接執行，無延遲 |
| 指令模糊 | 🤔 提 1-6 個澄清問題 |
| 需要跳過 | ⚡ 用 `*` 或 `/` 前綴繞過 |

**何時啟動：** 你按 Enter 提交指令時

**例子：**
```
❌ 你寫：「幫我改代碼」
→ Prompt Improver 攔截：
   「具體改什麼部分？目標是什麼？」

✅ 你寫：「把 auth.ts 的 JWT 驗證從 HS256 改成 RS256」
→ 直接執行，不問
```

---

### 第二層：Brainstorming 🧠
**強制先思考，後編碼**

來自 [Superpowers](https://github.com/obra/superpowers) 框架，執行流程：

1. **上下文探索** - 理解你的需求背景
2. **澄清問題** - 提出關鍵細節
3. **方案選項** - 提供 2-3 種實現方案
4. **你的批准** - 你同意後才開始編碼

**何時啟動：** 在複雜功能開發前

**例子：**
```
你寫：「加一個用戶認證系統」

Brainstorming 強制執行：
1. 現在有認證系統嗎？
2. 需要什麼級別的安全性？
3. JWT vs Session？OAuth？
4. 預期有多少用戶？
5. 需要 2FA 嗎？

→ 設計方案：
   方案 A: JWT + Refresh Token (推薦)
   方案 B: Session + Redis (適合大用戶量)
   方案 C: OAuth 整合 (第三方)

→ 你選擇並批准
→ 才開始編碼
```

---

### 第三層：Karpathy Skills 📋
**編碼規範與最佳實踐**

確保代碼符合：
- ✅ 簡潔清晰
- ✅ 有適當註釋
- ✅ 包含測試
- ✅ 無過度設計

---

## 如何使用

### 安裝工具

```bash
# 1. 在 Claude Code 中安裝 Prompt Improver
/skill add severity1/claude-code-prompt-improver

# 2. 安裝 Superpowers (包含 Brainstorming)
/skill add obra/superpowers

# 3. 安裝 Karpathy Skills
# 下載到 ~/.config/claude-code/skills/
```

### 典型工作流

**情況 1：簡單任務（自動跳過第二層）**
```
你：「幫我修正拼寫錯誤」
  ↓ Prompt Improver: 清楚 ✅
  ↓ 直接執行
  ✓ 完成
```

**情況 2：複雜功能（完整三層流程）**
```
你：「加一個支付系統」
  ↓ Prompt Improver: 模糊 🤔 提問
  ↓ 你詳細說明
  ↓ Brainstorming: 討論設計
  ↓ 你批准方案
  ↓ Karpathy Skills: 編碼時應用規範
  ✓ 完成
```

---

## 快速提示

| 場景 | 做什麼 |
|------|--------|
| 指令很清楚 | 正常提交，Improver 會放行 |
| 不想被問 | 用 `*` 或 `/` 前綴（如 `* 改這個`） |
| 想跳過 Brainstorming | 說「快速實現」而不是「設計方案」 |
| 需要高品質代碼 | 提及「生產環境」或「測試必須通過」 |

---

## 配置到 Claude Code

在 `~/.claude/settings.json` 或 `.claude/settings.json` 中：

```json
{
  "permissions": {
    "allow": [
      "Read", "Edit", "Write", "Bash",
      "mcp__github__*",
      "Skill(session-start-hook)"
    ]
  },
  "hooks": {
    "UserPromptSubmit": "prompt-improver-hook",
    "PreToolUse": "brainstorming-check"
  }
}
```

---

## 何時使用這個工作流

✅ **推薦用於：**
- 你經常指令不夠清楚
- 複雜項目開發
- 需要高代碼品質
- 想要「第一次就對」

❌ **不推薦用於：**
- 簡單、緊急的任務
- 你已經很清楚需求時
- 需要快速原型

---

## 常見問題

**Q: 會不會太慢？**  
A: 第一層（Prompt Improver）對清晰指令零開銷。第二層只在需要時啟動。

**Q: 可以個別關閉某一層嗎？**  
A: 可以，用前綴跳過（`*`）或在指令中說「快速實現」。

**Q: 這個工作流對所有項目都適用嗎？**  
A: 最適合複雜項目。簡單任務可跳過第二層。

---

## 下一步

1. 安裝三個工具
2. 試試簡單任務（自動跳過第二層）
3. 試試複雜功能（完整三層流程）
4. 根據習慣微調配置

**開始變得聰明吧！** 🚀
