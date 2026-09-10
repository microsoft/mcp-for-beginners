# MCP 計算器伺服器 (Python)



一個用 Python 實作的簡易模型上下文協議 (MCP) 伺服器，提供基本計算器功能。


## 安裝

安裝所需依賴：

```bash
pip install -r requirements.txt
```

或直接安裝 MCP Python SDK：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## 使用方法

### 啟動伺服器

此伺服器設計供 MCP 用戶端使用（例如 Claude Desktop）。啟動伺服器：

```bash
python mcp_calculator_server.py
```

<strong>注意</strong>：直接在終端機執行時，會看到 JSON-RPC 驗證錯誤。這是正常現象——伺服器正在等待格式正確的 MCP 用戶端訊息。

### 測試功能

測試計算器功能是否正常：

```bash
python test_calculator.py
```

## 疑難排解

### 匯入錯誤

如果出現 `ModuleNotFoundError: No module named 'mcp'` 錯誤，請安裝 MCP Python SDK：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### 直接執行時的 JSON-RPC 錯誤

直接執行伺服器時出現類似「Invalid JSON: EOF while parsing a value」錯誤是預期行為。伺服器需要 MCP 用戶端訊息，非直接的終端機輸入。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->