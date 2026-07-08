---
name: secret-scanner
description: 機密洩漏掃描。當使用者要「檢查有沒有洩漏密碼」「commit 前掃描」「機密掃描」時使用，或在 push 含個資/財務的 repo 前主動跑。偵測 API key、密碼、個資、金鑰。
---

# secret-scanner

## 掃描目標
API key/token、password=、私鑰(-----BEGIN)、身分證字號、信用卡號、帳號密碼
## 用法
git diff 掃描待提交內容；發現→擋下並列出檔案:行號
## 對本環境特別重要
自動 git add -A + 自動 push 的組合下，機密一旦寫入就會被推上 GitHub。這是第一道防線。
