# 🏛️ Harness 制度總覽（弱模型長期運作框架）

> 本目錄由 Fable 5 於 2026-07-07 建立（該模型在本環境的唯一一次 session）。
> 目的：把高階判斷力外化為制度，讓 Sonnet / Opus / Haiku 在此框架下穩定自主產出。
> **這些檔案是憲法層級**——修改權限見 `05-reflection.md`。

## 📂 檔案地圖與載入時機

| 檔案 | 內容 | 什麼時候讀 |
|------|------|-----------|
| `00-diagnosis.md` | 環境診斷書 + 本制度的能力極限（誠實條款） | 接手環境的第一個 session |
| `01-delegation.md` | 派工三件套 + 隔離驗證制度 | **每次要派 subagent 之前** |
| `02-escalation.md` | 模型升降級路徑、重試上限、熔斷 | 任何工具錯誤/失敗發生時 |
| `03-judgment-matrix.md` | 判斷力檢核表（停損/完成/提問） | 卡住時、想收工時、想問使用者時 |
| `04-templates.md` | 四種任務的派工 prompt 模板 | 派工時直接複製填空 |
| `05-reflection.md` | 自我更新協議：什麼能自己改、什麼要問 | 想修改任何制度/設定檔案之前 |
| `06-handoff-letter.md` | Fable 5 的交接信：三件關鍵事 + 腐化預防 | 接手環境的第一個 session |
| `lessons.md` | 踩坑紀錄（append-only） | 犯錯後寫入；開工前掃一眼 |

## 🚀 啟動方式（每個新 session）

1. SessionStart hooks 已自動注入 memory/MEMORY.md 與 FABLE-PROTOCOL——不用手動做
2. 第一次接手本環境：先讀 `00-diagnosis.md` 與 `06-handoff-letter.md`
3. 日常任務：照 CLAUDE.md 全部原則執行（含原則 4 任務協定）
4. 要派 subagent：先讀 `01-delegation.md`，用 `04-templates.md` 的模板
5. 出錯：查 `02-escalation.md` 決定重試/升級/熔斷
6. 不確定要不要停/收工/提問：查 `03-judgment-matrix.md`

## ⛓️ 制度間的優先序（衝突時）

使用者當下指示 > CLAUDE.md > 本目錄制度檔 > memory/MEMORY.md 偏好 > 模型自身判斷

- 使用者指示與 CLAUDE.md/制度檔衝突時的程序：**先指出矛盾一次**（一句話即可），
  使用者確認後其指示勝出，照做並把該例外記入 memory/MEMORY.md
