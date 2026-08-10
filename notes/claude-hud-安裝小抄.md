# 📟 Claude HUD 安裝小抄

> Claude Code 狀態列插件：把 context 余量做成輸入框下的進度條，全程可見。
> 資料來自 Claude Code 官方 statusline API（真實值，非估算）。
> 來源：[jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)

## ✅ 安全審查（2026-07-08，用 supply-chain-vetting 技能跑過）
- ⭐ 26.2k star、1.2k fork、v0.3.0（活躍維護）
- 🔒 純本機：無外部網路請求、無憑證存取，只讀 stdin JSON／transcript／git
- 官方插件架構，需 Claude Code v1.0.80+、Node 18+
- **結論：可安心安裝**

## 🚀 安裝三步（在「你自己電腦的 Claude Code 輸入框」依序輸入）
```
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/claude-hud:setup
```
輸入完**重啟 Claude Code**，狀態列進度條就會出現。

## ⚙️ 平台注意（官方 README，影片沒提）
- **Linux**：需設定 `TMPDIR` 環境變數，否則狀態列可能不出現
- **Windows**：需先裝 Node.js 18+

## 📊 裝好長這樣
```
[Opus | Max] │ my-project git:(main*)
Context █████░░░░░ 45%  │  Usage ██░░ 25%
```
顯示：模型名稱、Git 分支、Context 進度條（綠→黃→紅）、訂閱用量。
可切換百分比／token 數／剩餘量；1M context 長會話自動放大刻度。

## ⚠️ 為什麼不能請雲端的 Claude 代裝
`/plugin` 系列是 Claude Code 輸入框的**互動指令**，不是 shell 指令，雲端 agent 無法觸發；
且狀態列只在本機終端顯示、雲端暫時容器裝了也看不到。**這個插件的價值在你自己的電腦上。**

## 💡 和本倉庫的關係
它跟倉庫裡的 `token-optimizer-skill` 是互補的——HUD 給你「看得見的油表」，
token-optimizer 給你「省油的開法」。兩個一起用最省 token。
