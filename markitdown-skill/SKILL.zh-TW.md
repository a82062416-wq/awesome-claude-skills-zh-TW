---
name: markitdown-skill
description: 使用 Microsoft 開源的 markitdown 工具將多種文檔格式（PDF、Word、PPT、Excel、圖片、音頻等）轉換為 Markdown，便於 Claude 處理和分析。
license: MIT
keywords: 文檔轉換, Markdown, PDF, Word, PowerPoint, Excel, 格式轉換, 文檔處理
---

# Markitdown Skill：多格式文檔轉換為 Markdown

## 概述

Markitdown 是 Microsoft 開源的強大文檔轉換工具，可將多種常見文檔格式轉換為 Markdown。透過這個技能，Claude 能夠直接處理和分析各種格式的文檔，提升文檔工作流程的效率。

**關鍵詞**：文檔轉換、格式轉換、Markdown、PDF、Word、PowerPoint、Excel、圖片、音頻

## 何時使用此技能

- 📄 需要將 PDF、Word 文檔轉換為 Markdown 進行編輯或分析
- 📊 從 Excel 表格提取數據並轉換為 Markdown 格式
- 🎯 將 PowerPoint 演示文稿轉換為文本/Markdown 大綱
- 🖼️ 提取圖片中的文字（OCR）並轉換為 Markdown
- 🔊 從音頻文件轉錄並轉換為 Markdown
- 🗂️ 批量轉換多個文檔以統一處理
- 📚 將現有文檔庫轉換為 Markdown 格式進行知識管理

## 支持的文檔格式

### 輸入格式
| 格式 | 說明 |
|------|------|
| **PDF** | 便攜式文檔格式，支持文字和圖表提取 |
| **DOCX** | Microsoft Word 文檔，保留格式和結構 |
| **PPTX** | Microsoft PowerPoint 演示文稿，提取幻燈片內容 |
| **XLSX** | Microsoft Excel 電子表格，轉換為表格 Markdown |
| **HTML** | 網頁文件，轉換為結構化 Markdown |
| **JPG/PNG** | 圖片文件，支持 OCR 文字識別 |
| **MP3/WAV** | 音頻文件，進行語音轉錄（需配置） |
| **JSON/XML** | 數據格式文件 |
| **TXT** | 純文本文件 |

### 輸出格式
- **Markdown** - 統一的 Markdown 格式
- **完整的元數據** - 文檔元信息、創建時間、作者等
- **結構化內容** - 保留原文檔的結構層級

## 核心功能

### 1. 文本提取
- 從 PDF 提取全文
- 從 Word 文檔保留格式提取
- 從 PowerPoint 幻燈片提取文字

### 2. 表格處理
- Excel 表格轉換為 Markdown 表格
- 保留單元格格式和計算結果
- 支持多個工作表轉換

### 3. 圖片處理
- OCR 文字識別
- 圖片描述提取
- 嵌入式圖片轉換

### 4. 元數據保留
- 文檔標題、作者、創建時間
- 修訂歷史
- 文檔屬性

### 5. 結構保留
- 標題層級轉換為 Markdown 標題
- 列表結構保留
- 超鏈接保留

## 使用場景

### 場景 1：知識管理系統
```
原始：多個 Word 文檔、PDF 報告
轉換：統一的 Markdown 格式
用途：建立可搜索的知識庫，便於版本控制
```

### 場景 2：文檔內容分析
```
原始：客戶提供的 PDF 合同、提案
轉換：結構化的 Markdown
用途：Claude 快速分析內容、提取關鍵信息
```

### 場景 3：數據整理
```
原始：Excel 數據表、PowerPoint 報告
轉換：Markdown 表格和文本
用途：統一格式，便於進一步處理
```

### 場景 4：文檔協作
```
原始：各種格式的團隊文檔
轉換：Markdown（支持 Git 版本控制）
用途：提升團隊協作效率，便於追蹤變更
```

## 實施步驟

### 1. 安裝 Markitdown
```bash
pip install markitdown
```

### 2. 基本使用
```python
import markitdown

# 轉換 PDF
md_content = markitdown.markitdown(file_path="document.pdf")

# 轉換 Word
md_content = markitdown.markitdown(file_path="report.docx")

# 轉換 Excel
md_content = markitdown.markitdown(file_path="data.xlsx")
```

### 3. 處理輸出
- 保存為 `.md` 文件
- 進一步編輯或分析
- 集成到知識管理系統

## 工作流程

### 轉換流程
1. **上傳文檔** → Claude 接收各種格式文檔
2. **格式識別** → Markitdown 自動識別文檔類型
3. **內容提取** → 提取文本、表格、圖片、元數據
4. **Markdown 生成** → 轉換為結構化 Markdown
5. **內容處理** → Claude 分析、總結或編輯內容

### 批量轉換
```
輸入資料夾（多種格式文檔）
         ↓
   Markitdown 處理
         ↓
輸出資料夾（統一 Markdown）
```

## 最佳實踐

### ✅ 推薦做法
- 保存原始文檔的備份
- 檢查轉換結果的準確性，尤其是複雜表格
- 為複雜文檔（如掃描 PDF）提供 OCR 支持
- 使用元數據追蹤文檔來源
- 對大量文檔進行批量轉換時分批處理

### ⚠️ 注意事項
- 掃描 PDF（圖片型）需要額外的 OCR 支持
- 複雜的圖表可能需要手動調整
- 某些特殊格式或加密文檔可能無法轉換
- 大文檔轉換可能耗時，建議分割處理

## 與其他技能的協作

此技能可與以下技能組合使用以獲得最佳效果：

| 協作技能 | 用途 |
|---------|------|
| **content-research-writer** | 轉換後進行內容研究和寫作增強 |
| **file-organizer** | 轉換後自動整理和分類文檔 |
| **meeting-insights-analyzer** | 轉換會議記錄進行分析 |
| **document-skills (docx/pdf)** | 需要編輯時進一步處理 Markdown |
| **stop-slop** | 優化轉換後的文檔品質 |

## 常見問題

### Q: 是否支持掃描 PDF？
**A**: Markitdown 基礎版本可能對掃描 PDF 的支持有限。建議使用支持 OCR 的版本或搭配 OCR 工具。

### Q: 轉換後的 Markdown 可以轉回原格式嗎？
**A**: Markdown 是單向轉換終點。若需要編輯，建議使用 Markdown 編輯器，然後使用其他工具（如 Pandoc）轉換回原格式。

### Q: 大文檔如何處理？
**A**: 建議分割為較小的部分，逐個轉換，最後合併結果。

### Q: 如何保留文檔的視覺格式（顏色、字體等）？
**A**: Markdown 本身不支持顏色和複雜排版。若需保留，建議同時保存 HTML 版本。

## 資源

- [Markitdown GitHub](https://github.com/microsoft/markitdown) - 官方倉庫
- [Microsoft 文檔](https://github.com/microsoft/markitdown/blob/main/README.md) - 完整使用指南
- [Pandoc](https://pandoc.org/) - 替代方案，支持更多格式

## 總結

Markitdown 是一個強大的文檔轉換工具，能夠：
- ✅ 支持多種常見文檔格式
- ✅ 轉換為結構化的 Markdown
- ✅ 保留文檔結構和元數據
- ✅ 便於知識管理和版本控制
- ✅ 與 Claude 無縫協作

特別適合需要批量處理異構文檔、建立知識庫或進行文檔分析的場景。
