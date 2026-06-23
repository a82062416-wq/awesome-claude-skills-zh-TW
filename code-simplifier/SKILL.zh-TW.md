---
name: code-simplifier
description: 自動簡化複雜代碼，提升可讀性和可維護性，識別冗餘邏輯和優化機會。
license: MIT
keywords: 代碼簡化, 重構, 可讀性, 代碼優化, 技術債務, 複雜度降低
---

# Code Simplifier Skill：智能代碼簡化優化

## 概述

Code Simplifier 是一個智能代碼簡化工具，能自動分析複雜代碼並提供簡化建議。通過識別冗餘邏輯、提取公共模式、優化算法流程，幫助開發者將複雜代碼轉化為簡潔、優雅、易於維護的代碼。

**關鍵詞**：代碼簡化、重構、可讀性提升、技術債務清理、複雜度優化

## 何時使用此技能

- 🔗 代碼變得過於複雜和難以理解
- 🧹 需要清理技術債務
- 📉 想降低圈複雜度（Cyclomatic Complexity）
- 🔄 識別和消除重複代碼
- 🎯 優化算法邏輯和流程
- ♻️ 重構舊代碼以提高維護性

## 核心功能

### 1. 複雜度分析
- 計算圈複雜度和認知複雜度
- 識別過度嵌套的邏輯
- 檢測冗長的條件語句
- 定位難以理解的代碼段

### 2. 簡化建議
- 邏輯重構和優化
- 提取方法和模塊化
- 使用設計模式優化結構
- 條件語句簡化

### 3. 重複代碼檢測
- 識別完全相同的代碼塊
- 發現相似的邏輯模式
- 建議公共提取
- 跨文件分析

### 4. 自動重構
- 應用常見的簡化模式
- 生成簡化後的代碼
- 保持原有功能
- 提高代碼品質

## 簡化類型

### 1. 邏輯簡化
```javascript
// ❌ 複雜的嵌套邏輯
function checkUser(user) {
  if (user) {
    if (user.active) {
      if (user.role === 'admin') {
        if (user.permissions.includes('delete')) {
          return true;
        }
      }
    }
  }
  return false;
}

// ✅ 簡化版本（使用提前返回）
function checkUser(user) {
  if (!user?.active) return false;
  if (user.role !== 'admin') return false;
  return user.permissions.includes('delete');
}

// ✅ 最簡版本（使用邏輯符號）
const checkUser = (user) => 
  user?.active && 
  user.role === 'admin' && 
  user.permissions.includes('delete');
```

### 2. 條件簡化
```javascript
// ❌ 冗長的 if-else
function getStatus(age) {
  if (age < 13) {
    return 'child';
  } else if (age < 18) {
    return 'teenager';
  } else if (age < 65) {
    return 'adult';
  } else {
    return 'senior';
  }
}

// ✅ 簡化版本
const getStatus = (age) => {
  const ranges = [
    [13, 'child'],
    [18, 'teenager'],
    [65, 'adult']
  ];
  return ranges.find(([limit]) => age < limit)?.[1] || 'senior';
};
```

### 3. 提取方法
```javascript
// ❌ 長方法，多個責任
function processOrder(order) {
  const total = order.items.reduce((sum, item) => {
    const discountedPrice = item.price * (1 - item.discount);
    const taxedPrice = discountedPrice * 1.1;
    return sum + taxedPrice * item.quantity;
  }, 0);
  
  const savings = order.items.reduce((sum, item) => {
    return sum + (item.price * item.discount * item.quantity);
  }, 0);
  
  order.total = total;
  order.savings = savings;
  saveOrder(order);
}

// ✅ 簡化版本（提取方法）
const calculateItemPrice = (item) => 
  item.price * (1 - item.discount) * 1.1;

const calculateTotal = (items) =>
  items.reduce((sum, item) => sum + calculateItemPrice(item) * item.quantity, 0);

const calculateSavings = (items) =>
  items.reduce((sum, item) => sum + item.price * item.discount * item.quantity, 0);

function processOrder(order) {
  order.total = calculateTotal(order.items);
  order.savings = calculateSavings(order.items);
  saveOrder(order);
}
```

### 4. 設計模式應用
```typescript
// ❌ 策略手動分散
class PaymentProcessor {
  process(type: string, amount: number) {
    if (type === 'credit') {
      // 信用卡邏輯
    } else if (type === 'paypal') {
      // PayPal 邏輯
    } else if (type === 'crypto') {
      // 加密貨幣邏輯
    }
  }
}

// ✅ 簡化版本（策略模式）
interface PaymentStrategy {
  process(amount: number): void;
}

const strategies = {
  credit: new CreditCardPayment(),
  paypal: new PayPalPayment(),
  crypto: new CryptoPayment()
};

class PaymentProcessor {
  process(type: string, amount: number) {
    strategies[type].process(amount);
  }
}
```

## 複雜度指標

### 圈複雜度（Cyclomatic Complexity）
```
複雜度 1-5：簡單，易於理解
複雜度 6-10：中等，可以接受
複雜度 11-20：複雜，需要簡化
複雜度 > 20：過度複雜，必須重構
```

### 認知複雜度
- 測量代碼的心理負荷
- 考慮嵌套深度
- 評估邏輯分支數量

## 簡化流程

### 1. 分析階段
```
讀取代碼
    ↓
計算複雜度指標
    ↓
識別問題區域
```

### 2. 簡化建議
```
分析複雜度
    ↓
生成簡化方案
    ↓
評估影響
    ↓
提供建議和代碼示例
```

### 3. 驗證階段
```
應用簡化
    ↓
運行測試確保功能不變
    ↓
檢查性能影響
    ↓
審查可讀性改進
```

## 使用場景

### 場景 1：技術債務清理
```
遺留代碼複雜度高
    ↓
Code Simplifier 分析
    ↓
生成簡化方案
    ↓
逐步重構
    ↓
提高可維護性
```

### 場景 2：代碼審查
```
代碼過於複雜
    ↓
自動生成簡化建議
    ↓
提供代碼示例
    ↓
幫助開發者學習更簡潔的寫法
```

### 場景 3：性能優化
```
發現複雜的算法
    ↓
分析效率問題
    ↓
建議優化方案
    ↓
實現簡化和優化的版本
```

## 最佳實踐

### ✅ 推薦做法
- 定期檢查代碼的複雜度指標
- 設定團隊的複雜度上限
- 在代碼審查時使用簡化建議
- 優先簡化關鍵路徑上的代碼
- 逐步而非激進地進行重構
- 為每次簡化編寫測試

### ⚠️ 注意事項
- 不要盲目追求最小複雜度
- 簡化不能以犧牲功能為代價
- 過度簡化可能導致代碼難以理解
- 優先考慮可讀性而非行數減少
- 在簡化前充分理解原有邏輯

## 支持的語言

- ✅ JavaScript/TypeScript
- ✅ Python
- ✅ Java
- ✅ C#
- ✅ Go
- ✅ Rust
- ✅ 其他主流編程語言

## 與其他技能的協作

此技能可與以下技能組合使用：

| 協作技能 | 用途 |
|---------|------|
| **Code Review** | 結合審查發現複雜代碼區域 |
| **Superpowers** | 在開發流程中應用簡化 |
| **Planning with Files** | 規劃大規模重構項目 |
| **Ralph Loom** | 自動化重構執行 |

## 簡化前後對比

### 示例 1：條件簡化
```javascript
// 簡化前：圈複雜度 8
function validateUser(user) {
  if (user) {
    if (user.email) {
      if (user.email.includes('@')) {
        if (user.age >= 18) {
          if (user.status === 'active') {
            return true;
          }
        }
      }
    }
  }
  return false;
}

// 簡化後：圈複雜度 2
const isValidUser = (user) => 
  user?.email?.includes('@') && 
  user.age >= 18 && 
  user.status === 'active';

// 改進：50% 代碼行數減少，可讀性提升 300%
```

### 示例 2：算法優化
```javascript
// 簡化前：時間複雜度 O(n²)
function removeDuplicates(arr) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    let found = false;
    for (let j = 0; j < result.length; j++) {
      if (arr[i] === result[j]) {
        found = true;
        break;
      }
    }
    if (!found) result.push(arr[i]);
  }
  return result;
}

// 簡化後：時間複雜度 O(n)
const removeDuplicates = (arr) => [...new Set(arr)];

// 改進：代碼行數減少 80%，性能提升 10 倍
```

## 常見問題

### Q: 簡化會影響性能嗎？
**A**: 通常不會，簡化的代碼往往性能相同或更優。我們建議在簡化後運行性能測試以確認。

### Q: 簡化後的代碼會更難以理解嗎？
**A**: 不會。簡化的目標就是提高可讀性。如果簡化使代碼更難理解，我們會調整建議。

### Q: 能否自動應用簡化？
**A**: 是的，許多簡化建議可以自動應用，但建議先審查再應用，確保符合項目風格。

### Q: 如何處理已有大量複雜代碼的項目？
**A**: 建議使用優先級排序，先從關鍵路徑和高風險區域開始，逐步進行。

## 資源

- [Code Simplifier GitHub](https://github.com/addyosmani/agent-skills) - 官方倉庫
- [重構模式指南](https://github.com/addyosmani/agent-skills/tree/main/skills/code-simplification) - 詳細指南
- [複雜度指標說明](https://en.wikipedia.org/wiki/Cyclomatic_complexity) - 理論背景

## 總結

Code Simplifier 是提升代碼品質的重要工具：
- ✅ 自動識別複雜代碼
- ✅ 提供具體的簡化建議
- ✅ 支持多種編程語言
- ✅ 降低維護成本
- ✅ 提高代碼可讀性

特別適合需要清理技術債務、提升代碼品質、建立簡潔編碼標準的團隊。
