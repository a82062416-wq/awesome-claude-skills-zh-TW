---
description: 索引健檢：比對 repo 實際技能資料夾與兩份 README 的索引是否一致
---

對本 repo 執行索引完整性檢查（移植自 Vault for Founders 的 vault-audit SOP）：

1. **列實際**：列出 repo 根目錄所有技能資料夾（排除 `.git`、`.github`、`.claude`、`scripts`、`caicai-vault`）
2. **列索引**：從 `README.md` 與 `README.en.md` 抽出所有指向本地資料夾的條目
3. **比對差異**：
   - 🔴 有資料夾但沒索引（兩份 README 分開檢查）
   - 🟡 有索引但資料夾不存在
   - 🟠 中文有、英文沒有（或反過來）—— 同步破口
4. **報告**：固定格式輸出（摘要數字 + 三類問題清單 + 建議），**只回報不自動修改**，使用者決定後才動手

建議頻率：每月一次，或大量新增技能後。
