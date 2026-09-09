# MCP 計算機伺服器 (Python)



一個簡單的 Model Context Protocol (MCP) 伺服器實作，使用 Python 提供基本的計算機功能。


## 安裝

安裝所需的依賴：

```bash
pip install -r requirements.txt
```

或是直接安裝 MCP Python SDK：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## 使用方法

### 啟動伺服器

該伺服器設計供 MCP 用戶端使用（比如 Claude Desktop）。啟動伺服器：

```bash
python mcp_calculator_server.py
```

<strong>注意</strong>：直接在終端機執行時，您會看到 JSON-RPC 驗證錯誤。這是正常行為——伺服器正在等待格式正確的 MCP 用戶端訊息。

### 測試功能

確認計算機功能正常運作：

```bash
python test_calculator.py
```

## 疑難排解

### 匯入錯誤

如果看到 `ModuleNotFoundError: No module named 'mcp'`，請安裝 MCP Python SDK：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### 直接執行時的 JSON-RPC 錯誤

直接執行伺服器時出現 “Invalid JSON: EOF while parsing a value” 類似錯誤是預期現象。伺服器需要 MCP 用戶端的訊息，而非直接終端機輸入。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->