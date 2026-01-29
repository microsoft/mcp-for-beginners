# MCP 計算器伺服器 (Python)

一個簡單的模型上下文協議 (MCP) 伺服器實現，提供基本的計算器功能。

## 安裝

安裝所需的依賴項：

```bash
pip install -r requirements.txt
```

或者直接安裝 MCP Python SDK：

```bash
pip install mcp>=1.18.0
```

## 使用方法

### 啟動伺服器

此伺服器設計用於 MCP 客戶端（例如 Claude Desktop）。啟動伺服器：

```bash
python mcp_calculator_server.py
```

**注意**：直接在終端中運行時，您可能會看到 JSON-RPC 驗證錯誤。這是正常行為——伺服器正在等待格式正確的 MCP 客戶端消息。

### 測試功能

要測試計算器功能是否正常運作：

```bash
python test_calculator.py
```

## 疑難排解

### 匯入錯誤

如果您看到 `ModuleNotFoundError: No module named 'mcp'`，請安裝 MCP Python SDK：

```bash
pip install mcp>=1.18.0
```

### 直接運行時的 JSON-RPC 錯誤

直接運行伺服器時出現 "Invalid JSON: EOF while parsing a value" 等錯誤是預期的。伺服器需要 MCP 客戶端消息，而不是直接的終端輸入。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。