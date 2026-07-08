---
name: data-backup-guardian
description: 重要檔案備份守護。當使用者要「備份」「怕檔案不見」「重要資料保護」時使用。清點關鍵檔、建立備份清單、驗證備份完整。
---

# data-backup-guardian

## 原則
雲端 session 是暫時容器——唯一可靠持久層是 git。
## 做法
1. 關鍵產出（財報、對帳、記憶）確認已 commit+push
2. 大型二進位檔（非 git 適用）上傳雲端硬碟並記錄位置
3. 定期驗證：git log 確認最新工作已入庫
## 鐵律
沒 commit+push 的工作等於不存在。
