# MCP 計算機伺服器 (Python)



一個簡單的 Model Context Protocol (MCP) 伺服器 Python 實作，提供基本的計算機功能。


## 安裝

安裝所需的依賴：

```bash
pip install -r requirements.txt
```

或直接安裝 MCP Python SDK：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## 使用方法

### 啟動伺服器

該伺服器設計給 MCP 客戶端（如 Claude Desktop）使用。啟動伺服器：

```bash
python mcp_calculator_server.py
```

<strong>注意</strong>：直接在終端機中執行時，你會看到 JSON-RPC 驗證錯誤。這是正常行為——伺服器正在等待格式正確的 MCP 客戶端訊息。

### 測試功能

測試計算機功能是否正常：

```bash
python test_calculator.py
```

## 疑難排解

### 匯入錯誤

如果出現 `ModuleNotFoundError: No module named 'mcp'`，請安裝 MCP Python SDK：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### 直接執行時的 JSON-RPC 錯誤

直接執行伺服器時出現像是 “Invalid JSON: EOF while parsing a value” 這類錯誤是預期中的。伺服器需要 MCP 客戶端訊息，而非直接的終端機輸入。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->