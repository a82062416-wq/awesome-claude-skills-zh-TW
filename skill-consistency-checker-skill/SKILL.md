---
name: skill-consistency-checker
description: 技能註冊一致性檢查。當使用者要「檢查技能」「技能有沒有漏註冊」「一致性檢查」時使用。比對技能資料夾↔marketplace↔README 三方是否一致。
---

# skill-consistency-checker

## 檢查（單一真實來源原則）
1. 有 SKILL.md 但未在 marketplace.json 註冊 → 對外隱形
2. marketplace 註冊但資料夾不存在 → 幽靈條目
3. 有技能但 README 未列
## 落地
已整合進 scripts/validate_repo.py，CI 強制。這是防『寫入/讀出不一致』的控制單元。
