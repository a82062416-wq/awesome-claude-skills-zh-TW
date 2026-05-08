# 🧠 Claude Code 核心原則與最佳實踐

## 📌 必讀原則（每次開 Code 前記住）

### 原則 1️⃣：能用 CLI 就不要用 MCP
**為什麼？** MCP 工具會把完整的 schema 塞進你的 context window，輸入輸出都算錢 🔥

**實踐方式：**
- ✅ 優先用 CLI 命令（bash、git 等）
- ✅ 其次用 Skills（設計、開發工具）
- ❌ 最後才用 MCP（作為後備方案）

**例子：**
- 查文件 → 用 `cat` 或 `grep`，不要用 Google Drive MCP
- 提交代碼 → 用 `git` 命令，不要用 GitHub MCP
- 發郵件 → 用 CLI 工具，不要用 Gmail MCP

---

### 原則 2️⃣：安裝 Context-Mode 攔截多餘輸出
**為什麼？** MCP 工具回傳一萬個 tokens 的 JSON，會灌爆你的 context window

**解決方案：**
- 安裝開源插件 **Context-Mode**
- 它會在背景索引 MCP 原始輸出
- 只摘要關鍵信息給你
- **讓你的 context 保持乾淨！**

安裝命令：
```bash
npm install @context-mode/plugin
```

---

## 🎯 使用優先級（CP 值最高 → 最低）

| 優先級 | 工具類型 | 例子 | 說明 |
|--------|---------|------|------|
| 🥇 最高 | **CLI** | bash、git、npm | 零開銷，直接執行 |
| 🥈 次高 | **Skills** | 設計、開發、記憶 | 輕量、針對性強 |
| 🥉 備選 | **MCP** | Google Drive、Notion | 重量級、消耗 tokens |

---

## 💡 實際案例

### ❌ 錯誤用法
```
Claude: "我用 GitHub MCP 查看倉庫文件"
成本: 5000+ tokens（schema + 輸出）
```

### ✅ 正確用法
```
Claude: "我用 git log 和 cat 查看文件"
成本: 100 tokens
效率: 5倍提升 🚀
```

---

## 🛠️ 你現在擁有的完整工具鏈

### CLI 層（最優先）
- `git` - 版本控制
- `bash` - 命令執行
- `npm/node` - 開發

### Skills 層（次優先）
- 設計：Impeccable、frontend-design、ui-ux-pro-max 等（6 個）
- 開發：Web Access、PUA
- 記憶：claude-mem、mem0
- 工作流：superpowers（7 階段）

### MCP 層（最後手段）
- Google Drive、Calendar、Notion、Gmail、GitHub

---

## 📝 每次開始前的 Checklist

- [ ] 優先用 CLI
- [ ] 其次用 Skills
- [ ] 實在不行才用 MCP
- [ ] 用 MCP 時記得啟用 Context-Mode
- [ ] 檢查 claude-mem 有無相關記憶

---

**記住：省 tokens = 省錢 = 更多資源用在重要的事！** 💰✨
