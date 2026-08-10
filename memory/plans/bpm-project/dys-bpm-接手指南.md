# 🚀 dys-bpm 接手指南（開新對話用）

> 決策（2026-07-10）：BPM 主線 = 使用者自建的 `a82062416-wq/dys-bpm`（Vue 3 + Vite, v0.5）。
> **接續深做、不重做。** awesome repo 裡我做的 HTML 原型（v1/v2）退休，僅留參考。

## 📦 專案現況（我看過的評估）
- 技術棧：Vue 3 `<script setup>` + Vite 8 + vue-router + vuedraggable，共 2938 行
- 已完成（核心骨架齊全）：
  - `engine.js` 簽核引擎：串簽/會簽/或簽、退回、知會、條件分流（不用 eval，安全）、發布快照版本
  - `DesignerPage`(573行) 流程設計器、`FormRenderer`(245) 動態表單
  - `OrgPage` 組織+主管解析、`LoginPage`+表單三權限、`MonitorPage` 作業監控
  - 待辦/我的申請/我處理的/副本 各頁面齊全
- 推測待補（未細看）：資料持久化（前端 store 重整可能掉資料）、真多人帳號、部署上線、Nueip 紫色 UI 風格

## 🗂️ 新對話怎麼選倉庫
在 Claude Code（claude.ai/code 或 app）**新建 session** 時：
- **來源倉庫（source / repository）選 `a82062416-wq/dys-bpm`**（不是 awesome-claude-skills）
- dys-bpm 已在 session 範圍內，選它，新對話就直接在這個專案裡工作

## 📋 起手指令（複製貼上到新對話）

```
這是我的 BPM 專案 dys-bpm（Vue 3 + Vite），已到 v0.5。
請做一次完整的代碼檢測與修正，照以下步驟，不要重做整個專案：

1. 先讀 README、package.json、src/ 全部，用 3-5 句複述你對架構的理解讓我確認
2. 環境驗證：npm install 後 npm run build，確認能否成功建置，貼出結果
3. 代碼檢測（逐檔），用表格列出「檔案:行號｜問題｜嚴重度｜建議修法」，重點查：
   - engine.js 簽核引擎邏輯漏洞（串簽/會簽/或簽/退回/條件分流有沒有算錯）
   - 資料持久化：store 重整會不會掉資料
   - 會當掉的 bug、null/邊界沒處理
   - 安全問題
   - 可簡化的重複代碼
4. 給我一份修正計畫（按嚴重度排序），等我同意再動手
5. 修正時逐項改，每處說明「改前什麼問題、改後怎麼驗證」，不要一次全改
6. 全部改完跑一次 build 確認沒壞，並開發伺服器實際點一遍關鍵流程
```

## 💡 給新對話 AI 的提醒
- 使用者非工程師：結論先行、繁中、少黑話、幫他判斷值不值得
- 遵守 dys-bpm 自己的 CLAUDE.md（若有）＞本指南
- 改功能必附 fail-then-pass 證據（見 fable-harness 協議）
