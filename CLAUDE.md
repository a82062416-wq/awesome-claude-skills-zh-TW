# ⚙️ Claude Code 設定與最佳實踐

本文檔記錄技能百寶袋項目的開發設定和編碼規範。

---

## 📋 通用原則

### 優先編輯，非重寫
- 優先選擇編輯（Edit），而非重寫整個文件
- 除非文件被編輯過，否則不要重複閱讀已閱讀的文件
- 保持改動最小化

### 輸出追求簡潔
- 輸出簡潔明快
- 推理過程必須詳盡（內部思考過程清晰）
- 避免廢話，直接說重點

---

## 💻 代碼規範

### 檔案大小限制
- **單一檔案不超過 400 行**
- 超過 400 行時必須拆分
- 理由：可維護性、可測試性、單一職責

### 嵌套深度限制
- **嵌套不超過 4 層**
- 理由：可讀性、複雜度控制
- 超過時考慮提取為函數/組件

---

## 💰 Token 成本意識

### 2026 年 Token 成本警告
- **Token 真的會越來越貴**
- 優先使用 MarkitDown 轉換文檔（無 token 成本）
- 減少不必要的文件重讀
- 評估 API 調用的必要性

### Token 優化策略
1. **複用已閱讀的信息** - 不重複讀文件
2. **批量操作** - 並行執行獨立任務
3. **精確搜索** - 用 grep/find，避免讀整個文件
4. **提示詞優化** - 表達清晰，減少澄清回合

---

## 🎯 項目特定設定

### 專案名稱
🎒 **技能百寶袋**

### 開發分支
```
claude/check-mcp-skills-QMYVV
```

### 已安裝 Skills
- ✅ Prompt Improver
- ✅ Karpathy Skills
- ✅ Gstack（23 個專家角色）
- ✅ UI UX Pro Max（161 個設計規則）
- ✅ Matt 的 Skills（/grill-me）

### 核心工具
- 🛠️ Hermes Agent（已安裝，待 Ollama 配置）
- 📄 MarkitDown（已安裝）
- 🔍 Prompt Improver（自動檢查指令）

---

## 📖 使用指南

### Claude Code 啟動
```bash
# 自動加載所有已安裝 Skills
claude
```

### Gstack 指令
```bash
/office-hours          # 激進式產品質問
/plan-ceo-review       # 策略範圍挑戰
/plan-eng-review       # 架構審查
```

### Matt 的 Skills
```bash
/grill-me              # 編碼前激進式提問
```

---

## 🚀 未來計畫

- [ ] 完成網頁項目（待網站介紹）
- [ ] 配置 Hermes + Ollama（本地免費方案）
- [ ] 添加更多設計 Skills（shadcn-ui、web-accessibility）
- [ ] 定期更新技能百寶袋推薦清單

---

**最後更新：2026-05-13**
