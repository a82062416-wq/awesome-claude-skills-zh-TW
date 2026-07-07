# 🧠 Claude Code 完整整合分析報告

> 產出日期：2026-07-07
> 目的：完整盤點你目前 Claude Code（雲端環境）的技能、工具、連接器與設定狀態，
> 並針對「網頁開發」「影片製作」「記憶功能」三大領域提出強化建議。
> 以後不確定 Claude Code 能做什麼，看這一份就夠了。

---

## 📊 一、總覽（你現在擁有什麼）

| 類別 | 數量 | 狀態 |
|------|------|------|
| 個人自訂 Skills（claude.ai 已啟用） | 6 個 | ✅ 全部啟用 |
| 官方/社群 Skills（claude.ai 已啟用） | 14 個 | ✅ 全部啟用 |
| 本倉庫收藏的 Skills（awesome-claude-skills-zh-TW） | 40 個資料夾 | 📚 收藏庫 |
| MCP 連接器（Connectors） | 9 個已安裝 | 7 個已連線可用 |
| Claude Code 內建工作流技能 | 15+ 個 | ✅ 隨時可用 |
| 自動化 Hooks | 2 組 | ✅ 已設定（自動暫存 + 自動推送） |

---

## 🎯 二、個人自訂 Skills（你自己做的，共 6 個）

這些是你為自己的工作流量身打造的技能，全部已啟用：

| Skill 名稱 | 功能 | 觸發情境 |
|-----------|------|---------|
| `changhe-audit` | 長谷蓮清大樓月份財務月報表 Excel 全面稽核（收支驗算、跨表勾稽、代收明細比對、零用金核對） | 提到「長谷蓮清財報」「稽核月報表」「勾稽代收明細」 |
| `labor-insurance-reply` | 勞保局來函查核處理：撰寫回函、製作薪資明細 xlsx、出勤紀錄 xlsx（含勞健保費率、破月折算、國定假日） | 提到「勞保局來函」「查核投保薪資」「薪資清冊」 |
| `community-fee-reconciliation` | 悅讀ABC社區管理費月度收繳明細表填寫（H~M欄），基礎版 | 社區管理費對帳 |
| `community-fee-reconciliation-v2` | 同上完整版：補繳仍未繳/預繳(月)/攜帶前月欠繳/長期欠款範圍 | 社區管理費對帳（複雜案例） |
| `community-fee-reconciliation-v3` | 同上最新版：含分頁已填/清冊月份核對等前置確認 + 六種繳款情境 | 社區管理費對帳（建議用這版） |
| `attendance-sheet-builder` | 依班表建立多人出勤時數分頁：多班別、寬限期、遲到早退、國定假日 | 建立出勤表 |

> 💡 建議：`community-fee-reconciliation` 有三個版本，v3 最完整。建議停用 v1、v2 避免觸發混亂，只留 v3。

---

## 🛠️ 三、官方/社群 Skills（claude.ai 已啟用，共 14 個）

### 文件處理（4 個）— 你的辦公主力
- `xlsx` — Excel 建立/編輯/公式/圖表（你的財報稽核技能都靠它）
- `docx` — Word 文件建立與編輯（追蹤修訂、目錄、頁碼）
- `pptx` — 簡報建立與編輯
- `pdf` — PDF 提取/合併/分割/表單

### 設計與創作（6 個）
- `canvas-design` — 海報、視覺設計（PNG/PDF）
- `algorithmic-art` — p5.js 生成藝術
- `slack-gif-creator` — Slack 動畫 GIF
- `theme-factory` — 為 artifacts 套用主題（10 種預設主題）
- `brand-guidelines` — Anthropic 品牌色彩與字體
- `web-artifacts-builder` — 複雜多組件網頁 artifacts（React、Tailwind、shadcn/ui）

### 開發與寫作（4 個）
- `skill-creator` — 建立/優化/測試新技能（你擴充技能庫的核心工具）
- `mcp-builder` — 建立 MCP 伺服器
- `doc-coauthoring` — 結構化文件共同撰寫
- `internal-comms` — 內部溝通文件（狀態報告、FAQ、專案更新）

### Claude Code 內建工作流技能（本環境隨時可用）
`code-review`（代碼審查）、`simplify`（代碼簡化）、`verify`（變更驗證）、`security-review`（安全審查）、`dataviz`（數據視覺化）、`init`（建立 CLAUDE.md）、`loop`（定時循環任務）、`update-config`（設定管理）、`claude-api`（API 參考）、`run`（啟動專案）等。

---

## 🔌 四、MCP 連接器狀態（9 個）

| 連接器 | 狀態 | 功能 |
|--------|------|------|
| ✅ Gmail | 已連線、本對話可用 | 搜尋信件、草稿回覆、摘要討論串 |
| ✅ Google Calendar | 已連線、本對話可用 | 行程管理、會議協調 |
| ✅ Google Drive | 已連線、本對話可用 | 搜尋/讀取/上傳檔案 |
| ✅ Notion | 已連線、本對話可用 | 搜尋、更新工作區 |
| ✅ Canva | 已連線、本對話可用 | 搜尋/建立/匯出設計 |
| ✅ Gamma | 已連線、本對話可用 | AI 生成簡報、文件、網頁 |
| ✅ Zoom | 已連線、本對話可用 | 搜尋會議、錄影摘要 |
| ⚠️ Ahrefs | 未啟用 | SEO 分析（需要時再開） |
| ⚠️ Figma | 未啟用 | 設計稿轉代碼（需要時再開） |

> ⚠️ 依照你 CLAUDE.md 的原則：**能用 CLI 就不用 MCP**。這些連接器是「最後手段」，
> 但 Gmail/Calendar/Drive/Notion 這類雲端服務沒有 CLI 可替代時，用 MCP 是正確的。

---

## 📚 五、本倉庫（awesome-claude-skills-zh-TW）收藏狀態

倉庫目前收藏 **40 個技能資料夾**，已設定為 Claude Code plugin marketplace（`.claude-plugin/marketplace.json`）。分類如下：

- **文件處理**：document-skills（docx/pdf/pptx/xlsx）、markitdown-skill、paddleocr-skill
- **開發工具**：mcp-builder、code-review-skill、code-simplifier、changelog-generator、webapp-testing、planning-with-files、headroom-skill、harness-skill、ralph-loom
- **設計 UI**：frontend-design、canvas-design、theme-factory、brand-guidelines、design-dna-skill、taste-skill、stop-slop、artifacts-builder
- **商業行銷**：competitive-ads-extractor、lead-research-assistant、domain-name-brainstormer、invoice-organizer、experience-lab-skill、bpm-framework-skill
- **內容媒體**：content-research-writer、image-enhancer、slack-gif-creator、video-downloader
- **生產力**：file-organizer、meeting-insights-analyzer、internal-comms、developer-growth-analysis、raffle-winner-picker
- **記憶**：supermemory-skill
- **自動化**：n8n-workflows
- **工具**：skill-creator、skill-share、template-skill

### 自動化 Hooks（.claude/settings.json）
1. **PostToolUse (Write|Edit)**：自動 `git add -A` 暫存所有變更
2. **PostToolUse (Bash git commit)**：commit 後自動推送到遠端分支

---

## ⚡ 六、你的 Claude Code 現在可以執行什麼任務？

綜合以上，直接列出你隨時可以下的指令類型：

### 🏢 物業/會計工作（你的強項區）
- 「稽核長谷蓮清 X 月財報」→ 自動驗算、勾稽、比對
- 「填悅讀ABC X 月管理費明細」→ 自動分類入帳/預繳/缺繳
- 「回覆勞保局來函 + 做薪資清冊和出勤紀錄」
- 「依班表做出勤時數表」
- 任何 Excel / Word / PDF / PPT 的建立、分析、轉換

### 💻 開發任務
- 建立網頁、React 應用、HTML artifacts（web-artifacts-builder + frontend-design）
- 代碼審查、簡化、安全審查（/code-review、/simplify、/security-review）
- 建立自己的 MCP 伺服器（mcp-builder）
- 建立新技能（skill-creator）—— 把任何重複工作流變成技能
- 用 Playwright 測試網頁（webapp-testing）

### 🎨 設計與內容
- 海報、視覺設計、生成藝術、GIF
- Canva 設計搜尋與建立、Gamma 一鍵生成簡報/網頁
- 品牌一致的文件與簡報

### 📧 日常整合
- 搜尋/摘要 Gmail、管理 Google 日曆、讀寫 Google Drive/Notion
- Zoom 會議摘要
- 定時任務（/loop、Routines 排程）

---

## 🚀 七、三大領域強化建議（2026 網路搜尋結果）

### 1️⃣ 網頁開發強化

| 推薦技能 | 說明 | 安裝優先度 |
|---------|------|-----------|
| **frontend-design**（官方） | 2026 最熱門設計技能（27 萬+ 安裝），避免「AI 罐頭風」介面，產出有個性的生產級 UI。**倉庫已收藏，確保在 Code 中啟用** | 🥇 必裝 |
| **Superpowers**（obra） | 最完整的多代理開發工作流（40.9k stars）：腦力激盪 → 規劃 → TDD → 審查，全流程串接 | 🥇 必裝 |
| **web-design-guidelines** | 網頁設計規範審查（無障礙、排版、間距） | 🥈 建議 |
| **mattpocock/skills** | TypeScript 日常開發最佳實踐 | 🥈 建議 |

參考來源：[Firecrawl 2026 最佳技能榜](https://www.firecrawl.dev/blog/best-claude-code-skills)、[Composio Top 10](https://composio.dev/content/top-claude-skills)、[UX Planet 百技能實測](https://uxplanet.org/ive-tried-100-claude-code-skills-these-are-the-best-97f19ee05bda)

### 2️⃣ 影片製作強化

| 推薦技能 | 說明 | 安裝優先度 |
|---------|------|-----------|
| **Remotion 官方技能** | 2026 年 1 月爆紅（首週 25k+ 安裝，全球第 4 熱門技能）。用 React/TypeScript 寫影片，Claude 寫組件 → Remotion 渲染成 MP4 | 🥇 必裝 |
| **Claude-Code-Video-Toolkit**（wilwaldon） | 完整影片生產工具鏈：Remotion、Manim 數學動畫、螢幕錄影、YouTube 剪輯、FFmpeg 後製 | 🥇 必裝 |
| **claude-code-video-toolkit**（digitalsamba） | AI 原生影片製作工具組 | 🥈 建議 |
| **FFmpeg 後製模式** | GIF 轉 MP4、壓縮、平台編碼預設、音軌提取、批次處理 | 🥈 建議 |

參考來源：[Remotion Agent Skills Guide 2026](https://aividpipeline.com/blog/remotion-agent-skills-guide-2026)、[wilwaldon/Claude-Code-Video-Toolkit](https://github.com/wilwaldon/Claude-Code-Video-Toolkit)、[XDA：用 Claude Code 剪影片](https://www.xda-developers.com/forget-vibe-coding-apps-people-are-now-vibe-editing-videos-with-claude-code/)

> 💡 你倉庫裡已有 `video-downloader` 和 `slack-gif-creator`，加上 Remotion 技能後就是完整鏈：下載 → 剪輯 → 生成 → 後製。

### 3️⃣ 記憶功能強化

| 推薦方案 | 說明 | 適合誰 |
|---------|------|--------|
| **claude-mem** | 46.1k stars 最熱門記憶插件。原生 Claude Code plugin，5 個 hooks 自動記錄，SQLite + 全文搜尋，跨 session 記憶。⚠️ 注意：2026/2 社群審計指出 37777 埠 API 無認證，本機其他程式可讀取記憶，個人機器可用但注意隱私 | 單機個人使用 🥇 |
| **Mem0** | 2026/4 新算法達 LoCoMo 基準 91.6% 準確率，token 消耗少 3-4 倍。MCP + hooks + SDK 三合一 | 想要雲端記憶層 🥈 |
| **Supermemory** | 跨機器同步 + 團隊共享記憶（**倉庫已收藏 supermemory-skill**），需付費訂閱 | 多裝置/團隊 🥈 |

參考來源：[claude-mem GitHub](https://github.com/thedotmack/claude-mem)、[DataCamp claude-mem 指南](https://www.datacamp.com/tutorial/claude-mem-guide)、[Mem0 官方整合文件](https://docs.mem0.ai/integrations/claude-code)、[claude-supermemory](https://github.com/supermemoryai/claude-supermemory)

> 💡 建議路線：先裝 **claude-mem**（免費、本機、最成熟），如果之後需要跨裝置再上 Supermemory。

---

## ✅ 八、行動清單（照這個順序做）

1. **清理重複技能**：停用 `community-fee-reconciliation` v1 和 v2，只留 v3
2. **裝記憶**：`claude plugin install claude-mem` — 解決「每次開新對話都失憶」的問題
3. **裝影片鏈**：安裝 Remotion 官方技能 + Video Toolkit
4. **啟用網頁鏈**：確認 frontend-design 在 Claude Code 已啟用，考慮加裝 Superpowers
5. **視需求開啟** Figma 連接器（設計稿轉代碼時很有用）
6. **持續收藏**：發現好技能就加進本倉庫，用 `skill-creator` 把自己的重複工作流做成技能

---

## 📌 附：使用優先級提醒（來自你的 CLAUDE.md）

1. 🥇 **CLI 優先**（git、bash、npm）— 零開銷
2. 🥈 **Skills 次之** — 輕量、針對性強
3. 🥉 **MCP 最後** — 消耗 tokens，雲端服務（Gmail/Notion 等）才用

**省 tokens = 省錢 = 更多資源用在重要的事！** 💰✨
