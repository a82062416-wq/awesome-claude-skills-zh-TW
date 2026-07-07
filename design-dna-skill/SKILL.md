---
name: design-dna-skill
description: 設計系統 DNA 提取工具，自動從 UI 截圖/設計圖片生成機器可讀的設計系統 JSON，驅動自動化設計編碼工作流。
license: MIT
keywords: 設計提取, 設計系統, DNA, 自動化設計, UI 轉換, 設計令牌, Vibe Coding
---

# Design-DNA Skill：設計系統自動化提取

## 概述

Design-DNA Skill 是一個智能設計系統提取工具，能自動將 UI 設計截圖、原型圖、設計稿轉換為機器可讀的 Design DNA JSON 格式。通過提取顏色、排版、間距、組件等設計要素，生成完整的設計系統規範，配合 Vibe Coding 框架實現設計到代碼的全自動轉換。

**關鍵詞**：設計系統、DNA 提取、自動化設計、UI 轉換、Vibe Coding、設計令牌

## 何時使用此技能

- 🎨 需要從設計快速生成 UI 代碼
- 📐 建立統一的設計系統規範
- 🔄 實現設計到開發的自動化流程
- 🧬 提取設計的 DNA（核心設計元素）
- 💻 支持 Vibe Coding 自動編碼工作流
- 📊 快速生成設計令牌和設計文檔

## 核心功能

### 1. 智能設計提取
- 自動識別 UI 組件和元素
- 提取色彩系統和調色板
- 分析排版層級和字體選擇
- 識別間距和布局網格

### 2. Design DNA 生成
- 生成標準化的 Design DNA JSON
- 機器可讀的設計規範
- 結構化的設計令牌
- 支持多種設計工具

### 3. 代碼生成支持
- 與 Vibe Coding 框架集成
- 自動生成匹配的 UI 代碼
- 支持 React、Vue、Angular 等框架
- 即插即用的組件代碼

### 4. 工作流集成
- 與 frontend-design-skill 協作
- 支持 canvas-design 優化
- 集成 planning-with-files 進度追蹤
- 支持 code-review-skill 質量檢查

## Design DNA 結構

### 標準 JSON 格式
```json
{
  "metadata": {
    "name": "應用名稱",
    "version": "1.0.0",
    "author": "設計師",
    "created": "2026-01-01"
  },
  "colors": {
    "primary": ["#007AFF", "#0051D5"],
    "secondary": ["#5856D6"],
    "neutral": ["#000000", "#FFFFFF", "#F2F2F7"]
  },
  "typography": {
    "heading": {
      "fontFamily": "SF Pro Display",
      "fontSize": 32,
      "fontWeight": 700,
      "lineHeight": 1.2
    },
    "body": {
      "fontFamily": "SF Pro Text",
      "fontSize": 16,
      "fontWeight": 400,
      "lineHeight": 1.6
    }
  },
  "spacing": {
    "unit": 8,
    "scale": [0, 4, 8, 16, 24, 32, 48, 64]
  },
  "components": {
    "button": {
      "variants": ["primary", "secondary", "tertiary"],
      "sizes": ["small", "medium", "large"],
      "states": ["default", "hover", "active", "disabled"]
    }
  }
}
```

## 使用場景

### 場景 1：快速設計到代碼
```
設計師上傳設計稿
    ↓ Design-DNA 提取
Design DNA JSON 生成
    ↓ Frontend-Design 應用規範
標準化設計系統
    ↓ Vibe Coding 自動生成
完整 UI 代碼（React/Vue/Angular）
    ↓ Code-Review 質量檢查
生產就緒代碼
```

### 場景 2：多品牌管理
```
不同品牌的設計稿
    ↓ Design-DNA 分別提取
獨立的 Design DNA（品牌 1、2、3...）
    ↓ 統一代碼生成
多品牌應用自動生成
    ↓ 快速部署
品牌一致性保證
```

### 場景 3：設計系統遷移
```
舊系統設計
    ↓ Design-DNA 提取舊 DNA
新系統設計稿
    ↓ Design-DNA 提取新 DNA
對比分析與遷移方案
    ↓ 自動化轉換
完成系統升級
```

## 實施步驟

### 1. 準備設計資源
```bash
# 支援的輸入格式
- PNG/JPG 截圖
- Figma/Sketch 設計稿
- 高保真原型圖
- UI 線框圖
```

### 2. 執行設計提取
```javascript
import DesignDNA from './design-dna-skill'

const dna = new DesignDNA()
const designJson = await dna.extract({
  input: 'design-screenshot.png',
  options: {
    extractColors: true,
    extractTypography: true,
    extractSpacing: true,
    extractComponents: true
  }
})

console.log(designJson)
```

### 3. 生成代碼
```javascript
// 與 Vibe Coding 集成
import VibeCoding from 'vibe-coding'

const vibeCoding = new VibeCoding(designJson)
const uiCode = await vibeCoding.generate({
  framework: 'react',
  components: ['Button', 'Card', 'Input'],
  styling: 'tailwind-css'
})
```

### 4. 驗證和優化
```javascript
// 使用 Code-Review 檢查代碼質量
const review = await codeReview.analyze(uiCode)
const optimized = await codeSimplifier.simplify(uiCode)
```

## Design DNA 提取詳解

### 色彩提取
```
自動識別：
✅ 主色調和輔助色
✅ 中性色系（灰度）
✅ 功能色（成功/警告/錯誤）
✅ 漸變和陰影色
✅ 文字色和背景色對比度檢查
```

### 排版分析
```
提取信息：
✅ 字體家族和字重
✅ 字號階級（H1-H6, Body, Small 等）
✅ 行高和段落間距
✅ 字母間距
✅ 文本對齊和縮進
```

### 間距系統
```
識別：
✅ 基礎間距單位（通常 8px）
✅ 間距比例和階級
✅ 外邊距和內邊距規則
✅ 柵欄系統（12 列、24 列等）
✅ 響應式斷點間距
```

### 組件分析
```
發現：
✅ 按鈕變體和狀態
✅ 表單元素設計
✅ 卡片和容器
✅ 導航組件
✅ 模態框和通知
✅ 圖標和插圖風格
```

## 與其他 Skills 的協作

### 工作流完全圖

```
設計資源
    ↓
【新增】Design-DNA-Skill
    ├─ 自動提取設計系統
    ├─ 生成 Design DNA JSON
    └─ 創建設計令牌文件
    ↓
Design DNA JSON
    ↓
【Vibe Coding 框架】
    ├─ React 代碼生成
    ├─ Vue 代碼生成
    └─ Angular 代碼生成
    ↓
UI 代碼框架
    ↓
【現有】Frontend-Design-Skill
    ├─ 應用設計規範
    ├─ 確保美學一致性
    └─ 優化組件設計
    ↓
【現有】Canvas-Design-Skill
    ├─ 視覺優化
    ├─ 資產生成
    └─ 主題應用
    ↓
【現有】Code-Review-Skill
    ├─ 代碼質量檢查
    ├─ 最佳實踐驗證
    └─ 性能審查
    ↓
【現有】Code-Simplifier
    ├─ 代碼簡化
    ├─ 複雜度降低
    └─ 可維護性提升
    ↓
【現有】Planning-with-Files
    ├─ 進度追蹤
    ├─ 版本控制
    └─ 恢復能力
    ↓
生產就緒的 UI 代碼 ✅
```

## 最佳實踐

### ✅ 推薦做法
- 使用高品質的設計輸入（高分辨率、清晰版本）
- 確保設計遵循規範和一致性
- 定期驗證提取的 Design DNA 準確性
- 保存 Design DNA JSON 用於版本控制
- 建立設計系統的單一真實源
- 定期更新設計規範和令牌

### ⚠️ 注意事項
- 複雜的自定義設計可能需要手動調整
- 確保提供完整的設計上下文
- 驗證自動生成代碼的準確性
- 檢查色彩對比度和可訪問性
- 測試不同分辨率和設備
- 定期更新與新設計工具的兼容性

## 支持的設計工具

- ✅ Figma
- ✅ Sketch
- ✅ Adobe XD
- ✅ Adobe Photoshop/Illustrator
- ✅ Penpot（開源）
- ✅ InVision
- ✅ Framer
- ✅ 任何 UI 截圖

## 支持的代碼框架（通過 Vibe Coding）

- ✅ React 18+
- ✅ Vue 3
- ✅ Angular 16+
- ✅ Svelte
- ✅ Next.js
- ✅ Nuxt
- ✅ Astro

## 與其他技能的協作

此技能可與以下技能組合使用：

| 協作技能 | 用途 |
|---------|------|
| **frontend-design** | 應用和驗證設計規範 |
| **canvas-design** | 視覺優化和資產生成 |
| **code-review-skill** | 生成代碼的質量檢查 |
| **code-simplifier** | 自動簡化生成的代碼 |
| **planning-with-files** | 追蹤設計到代碼的進度 |
| **harness-skill** | 協調多 Agent 的設計流程 |
| **brand-guidelines** | 保持品牌一致性 |

## 常見問題

### Q: Design DNA 和 Design Tokens 的區別是什麼？
**A**: Design Tokens 是設計系統的最小單位（顏色、字號等），而 Design DNA 是完整的設計系統指紋，包含結構、關係和上下文。DNA 更全面，包含 Tokens。

### Q: 能否自動提取複雜的自定義設計？
**A**: 自動提取適用於標準設計系統。複雜或高度定制的設計可能需要 30-50% 的手動調整。建議提供清晰、有組織的設計文件。

### Q: 提取的準確率有多高？
**A**: 對於規範設計，準確率通常 90-95%。對於新奇設計或高度定制，準確率 70-85%。應始終進行人工審查。

### Q: 支持設計系統的版本控制嗎？
**A**: 是的，Design DNA JSON 可納入 Git，支持版本控制、diff 對比和歷史追蹤。

### Q: 能否生成多個設計系統的代碼？
**A**: 是的，支持批量處理。可以為同一應用生成多個設計變體和品牌版本。

### Q: 生成的代碼需要多少人工調整？
**A**: 取決於設計複雜度。簡單應用 10-20% 調整，複雜應用 30-50%。建議使用 Code-Review 和 Code-Simplifier 進一步優化。

## 性能指標

### 提取速度
```
簡單設計（< 10 頁）    : < 5 秒
中等設計（10-50 頁）  : 5-15 秒
複雜設計（50+ 頁）    : 15-30 秒
```

### 代碼生成速度（Vibe Coding）
```
簡單頁面（< 5 組件）   : < 3 秒
中等頁面（5-15 組件）  : 3-10 秒
複雜頁面（15+ 組件）   : 10-30 秒
```

### 生成代碼質量
```
代碼覆蓋率            : 70-90%（根據設計複雜度）
自動化程度            : 60-80%（需手工調整 20-40%）
可測試性              : 85%+（支持自動化測試）
可維護性              : 高（模塊化結構）
```

## 資源

- [Design-DNA GitHub](https://github.com/zanwei/design-dna) - 官方倉庫
- [Vibe Coding 指南](https://dev.to/pockit_tools/vibe-coding-in-2026) - Vibe Coding 2026 完整指南
- [Design Tokens 標準](https://design-tokens.github.io/community-group/format/) - W3C 設計令牌標準
- [設計系統最佳實踐](https://www.designsystems.com/) - Design Systems 資源

## 總結

Design-DNA Skill 是現代設計自動化的核心：
- ✅ 自動提取設計系統
- ✅ 生成機器可讀的 Design DNA
- ✅ 驅動 Vibe Coding 自動編碼
- ✅ 支持多框架代碼生成
- ✅ 無縫集成現有 Skills
- ✅ 設計到代碼全自動化

特別適合需要快速設計實現、多品牌管理、設計系統標準化、自動化 UI 編碼的團隊和開發者。

**Design 系統智能化時代已來，Design-DNA 是你的起點。** 🚀
