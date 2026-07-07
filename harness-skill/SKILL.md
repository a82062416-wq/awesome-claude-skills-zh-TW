---
name: harness-skill
description: 使用 harness 框架自動設計和編排 AI Agent 團隊，實現複雜的多 Agent 協作工作流。
license: MIT
keywords: Agent 編排, 團隊協作, 工作流自動化, 多 Agent, AI 編排, 複雜任務
---

# Harness Skill：AI Agent 團隊編排框架

## 概述

Harness 是一個強大的 AI Agent 編排框架，能自動設計和協調多個 AI Agent 團隊完成複雜任務。支持動態 Agent 生成、任務分配、結果聚合等功能，適合需要多 Agent 協作的複雜場景。

**關鍵詞**：Agent 編排、團隊協作、工作流自動化、多 Agent 系統、複雜任務

## 何時使用此技能

- 🤖 需要多個 AI Agent 協作完成任務
- 📊 複雜項目需要分工協作
- 🎯 動態生成和分配 Agent 角色
- 🔄 需要 Agent 間的通訊和協調
- 📈 大規模並行處理任務
- 🏗️ 構建多層級 Agent 架構

## 核心功能

### 1. Agent 編排
- 動態 Agent 生成
- 角色定義和分配
- 能力配置

### 2. 任務分配
- 智能任務分解
- 優先級管理
- 負載均衡

### 3. 協作機制
- Agent 間通訊
- 結果聚合
- 衝突解決

### 4. 監控和管理
- 任務進度追蹤
- Agent 狀態監控
- 性能優化

## Agent 架構類型

### 1. 線性流程
```
Agent A → Agent B → Agent C → 結果
（順序執行，前一個的輸出是下一個的輸入）
```

### 2. 並行流程
```
Agent A ┐
Agent B ├→ 聚合層 → 結果
Agent C ┘
（同時執行，最後聚合結果）
```

### 3. 層級結構
```
管理 Agent
    ├─ 分析 Agent 團隊
    ├─ 設計 Agent 團隊
    └─ 實施 Agent 團隊
```

### 4. 動態網絡
```
Agent 根據需要動態通訊和協作
（複雜的相互依賴關係）
```

## 使用場景

### 場景 1：軟件開發項目
```
需求分析 Agent
    ↓
架構設計 Agent（並行：數據層、業務層、UI層）
    ↓
代碼生成 Agent
    ↓
測試 Agent
    ↓
文檔生成 Agent
    ↓
集成和交付
```

### 場景 2：內容創作
```
內容規劃 Agent
    ├─ 文案撰寫 Agent
    ├─ 圖片生成 Agent
    ├─ 視頻編輯 Agent
    └─ SEO 優化 Agent
        ↓
內容發布 Agent
```

### 場景 3：研究和分析
```
研究方向確定
    ↓
文獻搜索 Agent（並行）
    ↓
內容分析 Agent（並行）
    ↓
結果統合 Agent
    ↓
報告生成 Agent
```

## 實施步驟

### 1. 定義 Agent 角色
```python
from harness import Agent, Team

# 定義 Agent
analyst = Agent(
    name="數據分析師",
    role="分析數據並生成見解",
    capabilities=["data_analysis", "visualization"]
)

writer = Agent(
    name="報告撰寫師",
    role="將分析結果轉換為報告",
    capabilities=["writing", "formatting"]
)
```

### 2. 組織 Agent 團隊
```python
# 創建團隊
team = Team(
    name="分析團隊",
    agents=[analyst, writer],
    workflow="linear"  # 或 parallel, hierarchical
)
```

### 3. 定義任務流程
```python
# 定義任務
task = {
    "goal": "分析銷售數據並生成報告",
    "data": sales_data,
    "constraints": {
        "deadline": "2 小時",
        "budget": 100  # token 預算
    }
}

# 執行
result = team.execute(task)
```

### 4. 監控和優化
```python
# 監控進度
status = team.get_status()
print(f"完成度: {status['progress']}%")
print(f"耗時: {status['elapsed_time']}s")
print(f"Token 使用: {status['token_usage']}")

# 獲取詳細日誌
logs = team.get_logs()
```

## Agent 設計最佳實踐

### ✅ 推薦做法
- 明確定義每個 Agent 的角色和責任
- 設置合理的 Agent 數量（不要過多）
- 實現清晰的 Agent 間通訊協議
- 定期監控 Agent 性能
- 保存執行日誌用於調試
- 設置合理的超時和重試機制

### ⚠️ 注意事項
- 避免 Agent 間的無限循環通訊
- 監控 token 成本，設置上限
- 確保 Agent 間的數據一致性
- 測試 Agent 故障時的恢復機制
- 不要創建過多相同功能的 Agent

## 與其他技能的協作

此技能可與以下技能組合使用：

| 協作技能 | 用途 |
|---------|------|
| **superpowers** | 確保 Agent 遵循開發流程 |
| **ECC** | 為 Agent 提供技能和安全 |
| **headroom** | 壓縮 Agent 間的通訊成本 |
| **mcp-builder** | 構建 Agent 可用的 MCP 工具 |

## 性能優化

### Token 成本優化
```
原始方案：每個 Agent 獨立處理
    ↓
優化：Agent 間共享上下文
    ↓
節省 40-60% token 成本
```

### 並行度設置
```
Agent 數量 vs 完成時間：
- 1 Agent：100 時間單位
- 3 Agent（並行）：35 時間單位
- 5 Agent（並行）：25 時間單位
（收益遞減）
```

## 常見問題

### Q: 應該創建多少個 Agent？
**A**: 根據任務複雜度，通常 2-5 個 Agent 最有效。過多 Agent 會增加協調成本。

### Q: Agent 間如何通訊？
**A**: Harness 提供標準化的消息隊列和通訊協議，支持同步和非同步通訊。

### Q: 如何處理 Agent 故障？
**A**: 實現重試機制、故障轉移和結果驗證，確保系統韌性。

### Q: 可以動態生成 Agent 嗎？
**A**: 是的，Harness 支持根據任務動態生成和回收 Agent。

## 資源

- [Harness GitHub](https://github.com/revfactory/harness) - 官方倉庫
- [文檔](https://github.com/revfactory/harness) - 完整使用指南
- [範例](https://github.com/revfactory/harness/tree/main/examples) - 實際應用示例

## 總結

Harness 是構建複雜 AI 系統的關鍵框架：
- ✅ 自動編排多個 Agent
- ✅ 支持多種協作模式
- ✅ 動態適應任務需求
- ✅ 內置監控和優化
- ✅ 可擴展的架構

特別適合需要多 Agent 協作、高複雜度任務的 AI 應用。
