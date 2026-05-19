# Skill 4: API Documentation Generator

## 說明
API文檔生成器，讓文檔不再滯後。

## 功能
- 從代碼註釋和Controller定義中自動生成結構化的API文檔
- 支持OpenAPI格式
- 自動生成文檔

## 使用方式
```bash
claude "掃描src/main/java/com/example/controller下的所有Controller，生成OpenAPI 3.0格式的API文檔，保存為api-docs.yaml"
```

## 優點
- 文檔與代碼同步
- 減少手工維護工作量
- 支持多種輸出格式

## 缺點
- 需要代碼註釋規範才能生成高質量文檔
- 複雜應結構可能需要手動調整

## 適用場景
- RESTful API開發
- 前後端協作
- 微服務文檔管理
