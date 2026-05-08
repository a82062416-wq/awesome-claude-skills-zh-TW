# 🚀 n8n 工作流集合

本資料夾儲存所有自動化工作流，使用 [n8n](https://n8n.io/) 無代碼平台建立。

> **提示：** 開始前請先閱讀 [CLAUDE.md](./CLAUDE.md) 了解最佳實踐！

## 📋 工作流清單

### 已建立的工作流

| 工作流名稱 | 目的 | 頻率 | 狀態 | 文檔 |
|-----------|------|------|------|------|
| （待添加） | （待添加） | （待添加） | 🔄 | [README](./workflows/) |

### 規劃中的工作流

- [ ] 郵件自動化
- [ ] 資料整理和清理
- [ ] 報告生成
- [ ] 資料備份
- [ ] Slack 通知

---

## 🏗️ 資料夾結構

```
n8n-workflows/
├─ CLAUDE.md                  # 最佳實踐指南（必讀！）
├─ README.md                  # 本文件
├─ workflows/
│  ├─ workflow-1/
│  │  ├─ workflow.json        # n8n 工作流文件
│  │  └─ README.md            # 工作流文檔
│  ├─ workflow-2/
│  │  ├─ workflow.json
│  │  └─ README.md
│  └─ ...
└─ docs/
   ├─ setup.md                # 安裝和配置指南
   └─ troubleshooting.md      # 故障排除
```

---

## 🔧 快速開始

### 1. 安裝 n8n

```bash
# 用 Docker（推薦）
docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n

# 或用 npm
npm install -g n8n
n8n start
```

### 2. 打開 n8n
訪問 http://localhost:5678

### 3. 導入工作流
- 在 n8n 中點「Import」
- 選擇 `workflow.json` 文件
- 配置應用憑證
- 啟用工作流

---

## 📝 建立新工作流

1. **計劃** - 在 CLAUDE.md 中查看最佳實踐
2. **建立** - 在 n8n 中設計工作流
3. **測試** - 用測試數據驗證
4. **導出** - 在 n8n 中導出為 JSON
5. **文檔** - 創建工作流 README.md
6. **提交** - 提交到 Git

**工作流命名規則：**
```
workflows/功能名稱/
  ├─ workflow.json
  └─ README.md
```

---

## 🆘 故障排除

### 工作流無法啟動？
- 檢查應用憑證是否正確
- 查看執行日誌找出問題步驟
- 參考 CLAUDE.md 中的錯誤處理指南

### 數據未正確傳遞？
- 驗證數據映射是否正確
- 使用「Test」按鈕逐步測試
- 檢查應用 API 文檔

### 性能問題？
- 減少工作流中的步驟數
- 使用子工作流模組化
- 優化 API 調用

---

## 📚 相關資源

- [n8n 官方文檔](https://docs.n8n.io/)
- [本項目的最佳實踐](./CLAUDE.md)
- [n8n 社區論壇](https://community.n8n.io/)

---

## 📊 統計

- **總工作流數：** 0（待添加）
- **最後更新：** 2026-05-08
- **維護者：** @your-name

---

**開始建立你的第一個工作流吧！** 🎉
