---
name: 技能英文名（kebab-case，與資料夾名一致）
description: 一句話說明「做什麼 + 何時觸發」。務必含觸發詞（使用者會說的話），否則不會被啟動。範例：「當使用者要『X』『Y』時使用。」
---

# 技能名

## 何時用 / 不用
- ✅ 適用情境
- ❌ 不適用（交給哪個技能）

## 流程
1. 步驟（先蒐證/讀input）
2. 步驟（處理）
3. 步驟（產出）

## 鐵律 / 誠實條款
- 涉及金額/法規/日期：先查當年度數值並附來源，不確定就標註，不可用舊記憶
- 完成定義：驗收條件逐條有證據

## 落檔檢查（提交前，機器會擋）
- [ ] 資料夾名（慣例帶 -skill 後綴）與 frontmatter name、marketplace source 對應一致
- [ ] 已註冊 .claude-plugin/marketplace.json（**未註冊會被 CI 擋下**）
- [ ] 已列 README.md
- [ ] python3 scripts/validate_repo.py 通過（未通過 = 進不了 master）
