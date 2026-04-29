## 測試與除錯

在開始測試您的 MCP 伺服器之前，了解可用的工具和最佳除錯實踐非常重要。有效的測試確保您的伺服器按預期運作，並幫助您快速識別和解決問題。以下章節概述了驗證 MCP 實作的建議方法。

## 概述

本課程涵蓋如何選擇合適的測試方法以及最有效的測試工具。

## 學習目標

完成本課程後，您將能夠：

- 描述各種測試方法。
- 使用不同工具有效地測試您的程式碼。

## 測試 MCP 伺服器

MCP 提供工具幫助您測試和除錯伺服器：

- **MCP Inspector**：一個命令列工具，可作為 CLI 工具和視覺化工具執行。
- <strong>手動測試</strong>：您可以使用像 curl 這樣的工具執行網路請求，但任何能執行 HTTP 的工具皆可。
- <strong>單元測試</strong>：您可以使用喜愛的測試框架測試伺服器和用戶端的功能。

### 使用 MCP Inspector

我們在之前的課程中描述過此工具的使用方式，但這裡先簡單介紹。它是用 Node.js 建立的工具，您可透過呼叫 `npx` 執行檔來使用，`npx` 會臨時下載並安裝該工具，完成後會自動清除。

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) 能幫助您：

- <strong>發現伺服器功能</strong>：自動偵測可用資源、工具及提示
- <strong>測試工具執行</strong>：嘗試不同參數並即時查看回應
- <strong>檢視伺服器資訊</strong>：查閱伺服器訊息、結構及設定

典型的工具執行指令如下：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

上述指令會啟動一個 MCP 及其視覺界面，並在瀏覽器中啟動本地端網頁介面。您會看到一個儀表板，顯示已註冊的 MCP 伺服器、其可用工具、資源及提示。介面允許您互動式測試工具執行、檢視伺服器資訊，並查看即時回應，使驗證與除錯 MCP 伺服器實作更簡便。

大致畫面如下：![Inspector](../../../../translated_images/zh-TW/connect.141db0b2bd05f096.webp)

您也可以使用 CLI 模式執行此工具，方法是在指令加上 `--cli` 參數。以下是用 CLI 模式執行並列出伺服器所有工具的範例：

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 手動測試

除了使用 inspector 工具測試伺服器功能，另一類似方法是使用能執行 HTTP 的用戶端，例如 curl。

使用 curl，您可直接透過 HTTP 請求測試 MCP 伺服器：

```bash
# 範例：測試伺服器的元資料
curl http://localhost:3000/v1/metadata

# 範例：執行工具
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

從上述 curl 用法可見，您使用 POST 請求呼叫工具，並帶入包含工具名稱及參數的載荷。選擇最適合您的方式。CLI 工具一般使用速度較快，且適合寫成腳本，對 CI/CD 環境特別有用。

### 單元測試

為您的工具與資源撰寫單元測試以確保功能如期運作。以下為範例測試程式碼。

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# 標記整個模組為非同步測試
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # 建立幾個測試工具
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # 測試不帶游標參數（省略）
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # 測試游標為 None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # 測試游標為字串
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # 測試游標為空字串
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

以上程式碼執行以下操作：

- 採用 pytest 框架，讓您能以函式形式建立測試，並使用 assert 陳述式。
- 建立一個包含兩種工具的 MCP 伺服器。
- 使用 `assert` 陳述式檢查特定條件是否成立。

請參考完整檔案於 [這裡](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)。

根據該檔案，您可以測試自己的伺服器，確保功能如預期被建立。

各主要 SDK 都有類似的測試章節，您可依選擇的運行時調整。

## 範例

- [Java 計算器](../samples/java/calculator/README.md)
- [.Net 計算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算器](../samples/javascript/README.md)
- [TypeScript 計算器](../samples/typescript/README.md)
- [Python 計算器](../../../../03-GettingStarted/samples/python)

## 其他資源

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 下一步

- 下一課: [部署](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或錯誤解讀負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->