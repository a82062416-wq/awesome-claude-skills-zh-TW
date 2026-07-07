---
name: code-review-skill
description: 全面的代碼審查技能，涵蓋 20+ 種語言和框架，提供生產級別的審查指南和最佳實踐。
license: MIT
keywords: 代碼審查, 代碼品質, 最佳實踐, 架構審查, 性能優化, 安全審查
---

# Code Review Skill：全面的代碼審查框架

## 概述

Code Review Skill 是一個全面的代碼審查框架，包含超過 16,000 行精心策劃的審查指南，涵蓋 React 19、Vue 3、Rust、TypeScript、TanStack Query v5 等 20+ 種語言和框架。為 Claude Code 和 AI 開發者提供生產級別的代碼品質保證。

**關鍵詞**：代碼審查、代碼品質、最佳實踐、架構優化、性能審查、安全檢查

## 何時使用此技能

- 👀 需要進行全面的代碼審查
- ✅ 確保代碼符合最佳實踐
- 🏗️ 審查軟件架構和設計決策
- 🚀 優化代碼性能和可維護性
- 🔒 檢查安全漏洞和風險
- 📚 學習各語言框架的最佳實踐

## 核心功能

### 1. 多語言審查支持
- React 19、Vue 3、Angular
- TypeScript、JavaScript
- Python、Java、C#、Go、Rust
- SQL、GraphQL 等數據層
- 前端、後端、全棧審查

### 2. 維度覆蓋
- **代碼風格**：一致性、可讀性、命名規範
- **架構設計**：模式選擇、層級結構、耦合度
- **性能**：算法效率、渲染優化、內存管理
- **安全性**：漏洞檢測、權限控制、數據保護
- **可維護性**：複雜度、文檔、測試覆蓋

### 3. 框架特定指南
- React：Hooks、性能優化、狀態管理
- Vue：組件設計、響應式系統、生命週期
- TypeScript：類型安全、泛型、高級特性
- Rust：所有權系統、借用、內存安全

### 4. 實踐引導
- 問題識別和建議
- 代碼示例和改進方案
- 詳細的解釋和推理
- 優先級和嚴重程度分類

## 審查框架

### 審查層級

```
Level 1：基礎檢查
├─ 語法和風格
├─ 命名規範
└─ 基本邏輯

Level 2：架構審查
├─ 設計模式
├─ 類/模塊設計
└─ 依賴關係

Level 3：高級優化
├─ 性能和效率
├─ 安全性和風險
└─ 可維護性和擴展性
```

## 審查流程

### 1. 代碼理解階段
```
讀取代碼
    ↓
理解目的和邏輯
    ↓
識別技術棧和框架
```

### 2. 逐維度審查
```
代碼風格 → 架構 → 性能 → 安全 → 可維護性
```

### 3. 匯總和建議
```
列出所有問題
    ↓
按優先級排序
    ↓
提供改進建議
    ↓
生成審查報告
```

## 審查維度詳解

### 代碼風格和可讀性
```javascript
// ❌ 不推薦
const x = arr.map(a => a * 2).filter(b => b > 5);

// ✅ 推薦
const doubled = numbers.map(num => num * 2);
const filtered = doubled.filter(num => num > 5);
```

### 架構設計
```typescript
// ❌ 違反單一責任原則
class User {
  name: string;
  saveToDb() { }
  sendEmail() { }
  generateReport() { }
}

// ✅ 遵循 SOLID 原則
class User {
  name: string;
}
class UserRepository {
  save(user: User) { }
}
class EmailService {
  send(user: User) { }
}
```

### 性能優化
```react
// ❌ 不必要的重新渲染
function List({ items }) {
  return items.map(item => <Item item={item} />);
}

// ✅ 使用 memo 優化
const Item = React.memo(({ item }) => <div>{item}</div>);
```

## 使用場景

### 場景 1：Pull Request 審查
```
開發者提交 PR
    ↓
Code Review Skill 分析代碼
    ↓
生成詳細的審查報告
    ↓
提供改進建議
    ↓
幫助開發者優化代碼
```

### 場景 2：代碼庫遷移
```
舊代碼庫
    ↓
審查現有代碼品質
    ↓
識別風險和問題
    ↓
規劃遷移策略
    ↓
確保新代碼符合標準
```

### 場景 3：技術債務清理
```
掃描整個項目
    ↓
識別技術債務
    ↓
優先級排序
    ↓
逐步重構
    ↓
提升代碼品質
```

## 最佳實踐

### ✅ 推薦做法
- 為每個 PR 進行系統的代碼審查
- 關注架構和設計決策，不只是風格問題
- 提供建設性的反饋和改進建議
- 重視審查的教育意義
- 定期審查代碼庫的整體健康度
- 維護團隊的代碼標準文檔

### ⚠️ 注意事項
- 避免過度關注瑣碎的風格問題
- 審查應該是討論而不是指責
- 考慮語境和權衡，而不是絕對規則
- 避免「自動化」的、沒有思考的審查
- 定期更新審查標準以適應新的語言特性

## 支持的語言和框架

### 前端
- ✅ React 19（Hooks、Server Components）
- ✅ Vue 3（Composition API、Script Setup）
- ✅ Angular（RxJS、依賴注入）
- ✅ Svelte（響應式、存儲）
- ✅ TypeScript（高級特性）

### 後端
- ✅ Node.js/Express
- ✅ Python（Django、FastAPI）
- ✅ Java（Spring Boot）
- ✅ Go
- ✅ Rust（async、所有權）
- ✅ C#（.NET Core）

### 數據和查詢
- ✅ SQL（性能、索引）
- ✅ GraphQL（結構、效率）
- ✅ TanStack Query v5（緩存策略）
- ✅ 數據庫設計

## 與其他技能的協作

此技能可與以下技能組合使用：

| 協作技能 | 用途 |
|---------|------|
| **Code Simplifier** | 自動簡化審查中發現的複雜代碼 |
| **Planning with Files** | 為審查流程保存計劃和檢查清單 |
| **Superpowers** | 在開發工作流中集成代碼審查 |
| **MCP Builder** | 構建自定義審查規則 |

## 審查清單範例

```markdown
## React 組件審查清單
- [ ] 組件是否遵循單一責任原則
- [ ] 是否正確使用了 Hooks
- [ ] 是否有不必要的重新渲染
- [ ] Props 是否有默認值和類型
- [ ] 是否有適當的錯誤處理
- [ ] 是否有性能問題
- [ ] 代碼是否易於測試
- [ ] 文檔是否完整

## TypeScript 審查清單
- [ ] 類型是否完整，避免 any
- [ ] 是否使用適當的泛型
- [ ] 接口設計是否合理
- [ ] 是否有未使用的類型定義
- [ ] 類型推斷是否正確
```

## 常見問題

### Q: 審查過程需要多長時間？
**A**: 取決於代碼規模。小型改動（< 500 行）通常需要 10-30 分鐘，大型代碼庫掃描可能需要更長時間。建議進行增量審查。

### Q: 能否自定義審查規則？
**A**: 是的，你可以創建項目特定的審查標準和檢查清單，以符合你的團隊的特定需求。

### Q: 如何處理團隊成員之間的審查風格差異？
**A**: 建立統一的代碼標準文檔，使用此技能作為標準的執行工具，確保所有審查的一致性。

### Q: 能否與 CI/CD 集成？
**A**: 可以，許多團隊將代碼審查集成到 CI 管道中，在合併前自動檢查。

## 資源

- [Code Review Skill GitHub](https://github.com/awesome-skills/code-review-skill) - 官方倉庫
- [審查指南](https://github.com/awesome-skills/code-review-skill) - 16,000+ 行詳細指南
- [框架特定指南](https://github.com/awesome-skills/code-review-skill/tree/main/frameworks) - 各框架審查標準

## 總結

Code Review Skill 是確保代碼品質的關鍵工具：
- ✅ 20+ 語言和框架支持
- ✅ 16,000+ 行專業審查指南
- ✅ 多維度完整審查
- ✅ 架構和性能優化
- ✅ 安全性檢查

特別適合需要維護高代碼品質、遵循最佳實踐、建立團隊編碼標準的開發團隊。
