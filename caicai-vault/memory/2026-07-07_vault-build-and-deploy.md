---
updated: 2026-07-07
tags: [memory, vault, milestone]
summary: Vault 初始建置與部署收官：JACK 上線、公開安全版進 PR #4、私有 repo 待建
---

# Vault 初始建置與部署

日期：2026/07/06 – 07/07

## 做了什麼

- 依 [Vault for Founders](https://github.com/cwlin0131/Vault-for-Founders) 框架從零建置菜菜的 Vault
- JACK 🛡️ persona 三層（Identity / Soul / Persona）以討論式建立，非模板填空
- 檢索優化：檔案級索引、YAML frontmatter、更新 log 兩條規則、vault-audit SOP
- 建立第一個技能 `skills/document-intake.md`（丟檔案 → 判斷專案 → 修正/完成）
- 部署：完整版 zip 交付菜菜；公開安全版推上 skills 倉庫 PR #4

## 決策 / 結論

| 決策 | 理由 |
|------|------|
| AI 搭檔命名 JACK，軍師定位 | 敢反駁、結論先行、表格優先、一律繁中 —— 菜菜親自定調 |
| 高端客戶 = 高利潤案場 | 判斷軸：利潤率 > 規模 > 品牌 |
| 主力業務與高利潤方向重疊 → 加碼強項 | 市場策略不是轉型，是放大既有優勢 |
| 敏感資訊只進私有 Vault | 公開倉庫一律佔位版（涉及第三方的內部評估尤其不可公開） |

## 教訓

- **雲端 session 是暫時的**：Vault 檔案必須即時交付（zip）或推上 repo，不能留在容器裡
- **公開 repo 的紅線**：涉及可識別第三方的內部評估，即使趕時間也要抽換後再上

## 未完成（交接給下一個 session 的 JACK）

- [ ] 菜菜建立私有 repo：https://github.com/new?name=caicai-vault&visibility=private → 把完整版 zip 內容推上去
- [ ] PR #4（skills 倉庫公開安全版）待菜菜 review 後 merge
- [ ] voice-and-tone.md 建檔（第一次寫對外文稿前）
- [ ] decision-style 品質標準與卡關模式、流失率口徑、市場開發卡點
