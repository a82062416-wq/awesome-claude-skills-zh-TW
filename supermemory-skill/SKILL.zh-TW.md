---
name: supermemory-skill
description: 使用 supermemory 為 AI 提供強大的長期記憶能力，跨 session 保留和檢索上下文信息。
license: MIT
keywords: 長期記憶, 上下文管理, 會話持久化, 信息檢索, 記憶管理, 知識積累
---

# Supermemory Skill：AI 長期記憶系統

## 概述

Supermemory 是一個高效的 AI 記憶系統，為 Claude 和其他 AI 模型提供跨 session 的長期記憶能力。支持自動記憶提取、智能檢索、記憶壓縮等功能，幫助 AI 在多個對話中積累和利用知識。

**關鍵詞**：長期記憶、上下文管理、知識積累、會話持久化、信息檢索

## 何時使用此技能

- 💾 需要跨多個 session 保留信息
- 🧠 構建 AI 的長期知識庫
- 🔍 快速檢索相關歷史信息
- 📚 累積用户偏好和上下文
- 🎯 改進個性化 AI 響應
- 🔄 實現記憶的演化和學習

## 核心功能

### 1. 自動記憶提取
- 從對話自動識別重要信息
- 智能摘要生成
- 記憶分類和標籤

### 2. 高效檢索
- 快速相似度搜索
- 語義理解檢索
- 上下文相關信息推薦

### 3. 記憶管理
- 記憶版本控制
- 過期信息清理
- 優先級管理

### 4. 多層記憶
- 短期記憶（當前 session）
- 中期記憶（最近對話）
- 長期記憶（所有歷史）

## 記憶架構

### 記憶層級結構
```
┌─ 工作記憶 ─────┐
│   （當前 session）
│   - 實時信息
│   - 臨時上下文
└──────────────┬┘
              ↓
┌─ 短期記憶 ────┐
│   （最近對話）
│   - 最後 10 個 session
│   - 關鍵決策點
└──────────────┬┘
              ↓
┌─ 長期記憶 ────┐
│   （歷史知識）
│   - 用户偏好
│   - 已學知識
│   - 建立的關係
└──────────────┘
```

## 使用場景

### 場景 1：持續個人助手
```
Session 1：用户告訴你偏好和目標
    ↓
Supermemory 保存用户信息
    ↓
Session 2-N：自動使用保存的信息
    ↓
AI 在所有對話中保持個性化
```

### 場景 2：項目開發協作
```
Session 1：討論項目架構
    ↓
保存架構決策和上下文
    ↓
Session 2：繼續編碼
    ↓
自動恢復架構上下文
    ↓
編碼風格和選擇保持一致
```

### 場景 3：知識積累系統
```
多個研究 session
    ↓
自動記錄發現和見解
    ↓
建立知識圖譜
    ↓
快速檢索相關信息
    ↓
生成綜合報告
```

## 實施步驟

### 1. 初始化 Supermemory
```python
from supermemory import Memory

# 創建記憶系統
memory = Memory(
    name="個人助手記憶",
    model="claude-opus",
    storage="persistent"  # 持久化存儲
)
```

### 2. 保存記憶
```python
# 自動保存重要信息
memory.save({
    "type": "user_preference",
    "content": "用户喜歡簡潔清晰的解釋",
    "tags": ["偏好", "溝通"],
    "priority": "high"
})

# 對話結束時自動提取記憶
memory.extract_from_conversation(conversation_history)
```

### 3. 檢索記憶
```python
# 基於查詢檢索相關記憶
relevant_memories = memory.search(
    query="用户的編程偏好",
    limit=5,
    relevance_threshold=0.7
)

# 在 AI 提示中注入記憶
context = memory.get_context()
ai_prompt = f"{context}\n\n新提問..."
```

### 4. 管理和優化
```python
# 查看記憶統計
stats = memory.get_stats()
print(f"記憶數: {stats['total_memories']}")
print(f"檢索効率: {stats['avg_retrieval_time']}ms")

# 清理過期記憶
memory.cleanup(days=30)

# 記憶壓縮
memory.compress()
```

## 記憶類型

### 1. 事實記憶
```python
memory.save_fact(
    "Python 首先應該使用列表推導式而不是 for 循環",
    tags=["Python", "最佳實踐"]
)
```

### 2. 偏好記憶
```python
memory.save_preference(
    "用户喜歡代碼首先使用類型提示",
    tags=["編碼風格", "用户偏好"]
)
```

### 3. 關係記憶
```python
memory.save_relation(
    "Alice 是項目的首席架構師",
    tags=["團隊", "角色"]
)
```

### 4. 決策記憶
```python
memory.save_decision(
    "選擇 PostgreSQL 而非 MongoDB 是因為需要 ACID 事務",
    tags=["技術決策", "理由"]
)
```

## 性能特性

### 檢索效率
```
記憶數 | 檢索時間
─────────────
100   | 10ms
1000  | 50ms
10000 | 200ms
100000| 800ms
（使用向量索引優化）
```

### 存儲成本
```
1000 條記憶 ≈ 1-2MB
10000 條記憶 ≈ 10-20MB
100000 條記憶 ≈ 100-200MB
（取決於記憶複雜度和壓縮設置）
```

## 最佳實踐

### ✅ 推薦做法
- 定期自動提取重要信息
- 為記憶添加清晰的標籤
- 定期審查和更新舊記憶
- 設置合理的記憶保留策略
- 監控記憶系統的性能
- 備份重要的記憶

### ⚠️ 注意事項
- 避免存儲過多低質量信息
- 定期清理重複的記憶
- 保護敏感信息的隱私
- 不要無限增長記憶大小
- 監控記憶檢索的準確性

## 與其他技能的協作

此技能可與以下技能組合使用：

| 協作技能 | 用途 |
|---------|------|
| **claude-mem** | 多層記憶系統互補 |
| **mem0** | 通用記憶層集成 |
| **ECC** | 為 Agent 提供記憶能力 |
| **headroom** | 壓縮記憶存儲空間 |

## 記憶演化

### 記憶學習週期
```
1. 提取：自動識別重要信息
    ↓
2. 存儲：保存到長期記憶
    ↓
3. 檢索：在需要時快速調用
    ↓
4. 反饋：評估檢索相關性
    ↓
5. 優化：根據使用調整存儲策略
```

## 常見問題

### Q: 記憶會佔用很多存儲空間嗎？
**A**: Supermemory 使用智能壓縮，1000 條記憶通常只需 1-2MB。可配置清理策略控制大小。

### Q: 檢索的記憶準確度如何？
**A**: 使用向量相似度搜索，準確度通常在 85-95% 之間。可通過調整閾值平衡召回率和精確度。

### Q: 可以跨多個 AI 模型使用記憶嗎？
**A**: 是的，Supermemory 提供標準化格式，可被不同 AI 模型訪問。

### Q: 舊記憶會自動過期嗎？
**A**: 可以配置過期策略。默認情況下，閒置 90 天的記憶會被標記為過期。

## 資源

- [Supermemory GitHub](https://github.com/supermemoryai/supermemory) - 官方倉庫
- [文檔](https://github.com/supermemoryai/supermemory) - 完整使用指南
- [API 參考](https://github.com/supermemoryai/supermemory/wiki/API) - 開發者文檔

## 總結

Supermemory 是實現 AI 長期學習的關鍵系統：
- ✅ 跨 session 保留上下文
- ✅ 高效的語義檢索
- ✅ 自動記憶提取
- ✅ 優化的存儲和檢索
- ✅ 可擴展的架構

特別適合需要持續學習、個性化適應、知識積累的長期 AI 應用。
