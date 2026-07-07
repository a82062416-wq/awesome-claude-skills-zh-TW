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

### 原則 2️⃣：保持 Context 乾淨（內建方法，免安裝）
**為什麼？** MCP 工具回傳一萬個 tokens 的 JSON，會灌爆你的 context window

**真正有效的做法（Claude Code 內建）：**
- 換新任務就開新對話或用 `/clear` — 最有效的清理方式
- 對話太長時用 `/compact` 壓縮歷史，只留重點
- 用 `/context` 檢查目前 context 用量，看誰在吃 tokens
- 大範圍搜尋交給 **subagent**（Explore agent）跑，只回傳結論，不佔主對話
- 用不到的連接器在對話設定裡關掉（Ahrefs、Figma 平常保持關閉）
- Claude 回覆要求精簡：先講結論，細節放檔案裡而不是貼在對話中

---

### 原則 3️⃣：長期記憶（每個 session 必做）
**為什麼？** 雲端 session 是暫時容器，不記下來下次就全忘了

**記憶協定：**
- 🔴 **Session 開始：先讀 `memory/MEMORY.md`**（使用者輪廓、偏好、專案進度都在裡面）
- 學到新事實/偏好/教訓 → 立即更新 `memory/MEMORY.md` 並 commit（hooks 會自動推送）
- 使用者說「記住…」→ 寫入記憶；說「你記得嗎」→ 查記憶
- 詳細協定見 `long-term-memory-skill/SKILL.md`

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
- 設計：frontend-design、canvas-design、theme-factory、design-dna
- 開發：code-review、code-simplifier、webapp-testing、mcp-builder
- 影片：remotion-video（程式化影片）、ffmpeg-video（後製）、video-downloader
- 記憶：**long-term-memory（memory/MEMORY.md，本倉庫內建）**、supermemory
- 辦公：xlsx / docx / pdf / pptx + 自訂稽核/對帳/出勤技能

### MCP 層（最後手段）
- Google Drive、Calendar、Notion、Gmail、Canva、Gamma、Zoom、GitHub

---

## 📝 每次開始前的 Checklist

- [ ] **先讀 `memory/MEMORY.md`（長期記憶）**
- [ ] 優先用 CLI
- [ ] 其次用 Skills
- [ ] 實在不行才用 MCP
- [ ] 對話太長就 `/compact`，換任務就 `/clear`
- [ ] 學到新東西記得寫回 memory/MEMORY.md

---

**記住：省 tokens = 省錢 = 更多資源用在重要的事！** 💰✨
