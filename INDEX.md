# 🗺️ 倉庫導覽地圖（INDEX）

> 覺得亂？看這裡就好。所有東西分成 **技能 / 制度 / 記憶 / 工具 / 產出 / 文件** 六層。
> 63 個技能平鋪在根目錄難以一眼看懂，本地圖按用途分類，找技能從這裡開始。
> 最後更新：2026-07-08

---

## 🗂️ 第一層：技能（63 個，按用途分類）

### 💰 你的本業 · 財務會計（8）
| 技能 | 做什麼 |
|------|--------|
| bank-reconciliation-skill | 銀行對帳單勾稽、存款調節表 |
| payroll-calculator-skill | 台灣薪資（勞健保、加班費、代扣） |
| tax-filing-helper-skill | 營業稅／扣繳申報 |
| budget-variance-skill | 預算vs實際差異、超支分析 |
| depreciation-skill | 固定資產折舊表 |
| utility-splitter-skill | 水電公共費用分攤 |
| excel-formula-auditor-skill | Excel 公式錯誤稽核 |
| invoice-organizer | 發票收據自動歸檔 |

### 🏢 你的本業 · 物業社區（4）
| 技能 | 做什麼 |
|------|--------|
| mgmt-committee-report-skill | 管委會月度報告 |
| meeting-minutes-skill | 會議記錄格式化 |
| vendor-contract-tracker-skill | 廠商合約到期追蹤 |
| arrears-chaser-skill | 分級欠費催繳信 |

### ⚖️ 你的本業 · 法規（1）
labor-law-advisor-skill（勞基法：特休、資遣費、工時）

> 💡 上面 13 個 + claude.ai 上的 6 個自訂技能（財報稽核、勞保回函、社區對帳v3、出勤表），
> 合起來就是你的「台灣物業會計技能包」——這是別人抄不走的核心資產。

### 📄 文件處理（3）
document-skills（docx/pdf/pptx/xlsx）、markitdown-skill（多格式轉MD）、paddleocr-skill（OCR）

### 🎨 設計創作（10）
canvas-design、frontend-design、theme-factory、brand-guidelines、design-dna-skill、
taste-skill、stop-slop、image-enhancer、slack-gif-creator、artifacts-builder

### 🎬 影片媒體（3）
remotion-video-skill（程式化影片）、ffmpeg-video-skill（後製）、video-downloader

### 💻 開發工具（14）
code-review-skill、code-simplifier、mcp-builder、webapp-testing、skill-creator、
template-skill、changelog-generator、planning-with-files、headroom-skill、ralph-loom、
harness-skill、skill-share、developer-growth-analysis、bpm-framework-skill、experience-lab-skill

### 📣 商業行銷（7）
competitive-ads-extractor、lead-research-assistant、domain-name-brainstormer、
content-research-writer、internal-comms、meeting-insights-analyzer、raffle-winner-picker

### 🔒 安全（3）
secret-scanner-skill（機密掃描）、injection-defense-skill（提示注入防禦）、
supply-chain-vetting-skill（供應鏈審查）

### 🧠 記憶（2）
long-term-memory-skill（Git 版記憶）、supermemory-skill（雲端記憶）

### ⚙️ 工作流元技能（5）
skill-consistency-checker-skill（技能一致性）、token-optimizer-skill（省 token）、
backup-guardian-skill（備份守護）、file-organizer（檔案整理）、n8n-workflows（自動化流）

---

## 🏛️ 第二層：制度（讓弱模型穩定工作的框架）
| 位置 | 內容 |
|------|------|
| `CLAUDE.md` | 五大核心原則（CLI優先、context乾淨、記憶、任務協定、協作制度） |
| `harness/` | 弱模型協作制度 10 檔（診斷、派工、升降級、判斷矩陣、模板、反思、交接、審計藍圖） |
| `fable-harness/` | FABLE-PROTOCOL 行為協議 + Stop 驗證閘 |

## 🧠 第三層：記憶
| 位置 | 內容 |
|------|------|
| `memory/MEMORY.md` | 長期記憶（每次開機自動載入） |
| `memory/plans/` | 任務計畫檔 |
| `memory/archive/` | 歷史歸檔 |

## 🛠️ 第四層：工具
| 位置 | 內容 |
|------|------|
| `scripts/validate_repo.py` | 健康檢查（技能↔marketplace↔README↔git 四方一致） |
| `.claude/commands/` | 自訂指令：/plan /monthly-audit /fee-check /retro |
| `.claude/agents/` | 子代理：researcher、skeptic、red-team、simplifier |
| `.github/workflows/` | CI 自動驗證 |

## 📦 第五層：產出物
| 檔案 | 內容 |
|------|------|
| `skill-tree.html` | 技能樹視覺化儀表板 |
| `CLAUDE-CODE-整合分析報告.md` | 環境完整盤點 |
| `harness/07-audit-blueprint.md` | 八大面向診斷藍圖 |

## 📄 第六層：專案文件
`README.md`（繁中）、`README.en.md`（英文）、`CONTRIBUTING.md`、本 `INDEX.md`

---

## ❓ 為什麼不把技能實體搬進子資料夾？

技能的資料夾路徑被 `marketplace.json`、`README`、Claude Code 載入器三處引用。
實體搬移 63 個資料夾會同時打斷這三處，修復半徑巨大、風險高於收益
（判斷矩陣停損信號1）。**分類用這份地圖解決「找不到」，不動實體結構**——
這是「單一真實來源 + 索引」而非「大搬遷」的正解。

未來若技能成長到難以管理，再評估 Claude Code 支援的巢狀技能結構後審慎遷移。
