## 測試與除錯

在開始測試您的 MCP 伺服器之前，了解可用的工具和除錯最佳實務非常重要。有效的測試能確保您的伺服器表現如預期，並幫助您快速識別和解決問題。以下章節概述驗證您的 MCP 實作的建議方法。

## 概述

本課程涵蓋如何選擇正確的測試方法及最有效的測試工具。

## 學習目標

完成本課程後，您將能夠：

- 描述各種測試方法。
- 使用不同工具有效測試您的程式碼。

## 測試 MCP 伺服器

MCP 提供工具幫助您測試及除錯伺服器：

- **MCP Inspector**：命令行工具，可作為 CLI 工具和視覺化工具執行。
- **手動測試**：您可以使用像 curl 這樣的工具執行網路請求，任何可使用 HTTP 的工具都可以。
- **單元測試**：可以使用您偏好的測試框架測試伺服器及用戶端的功能。

### 使用 MCP Inspector

我們在之前的課程中已描述此工具的用法，這裡來簡單介紹一下。這是一個基於 Node.js 的工具，您可以透過呼叫 `npx` 執行檔使用它，`npx` 會暫時下載並安裝該工具，執行完請求後會自行清理。

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) 幫助您：

- **發現伺服器功能**：自動偵測可用的資源、工具和提示
- **測試工具執行**：嘗試不同參數並即時查看回應
- **檢視伺服器元資料**：檢查伺服器資訊、結構與配置

工具的典型執行範例如下：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

上述指令啟動 MCP 及其視覺化介面，並在您的瀏覽器中啟動本地網頁介面。您會看到一個儀表板，顯示您註冊的 MCP 伺服器、其可用工具、資源及提示。此介面允許您互動式測試工具執行、檢查伺服器元資料並觀看即時回應，使驗證和除錯 MCP 伺服器實作更為方便。

它大致會長這樣：![Inspector](../../../../translated_images/zh-HK/connect.141db0b2bd05f096.webp)

您也可以在 CLI 模式下執行此工具，這時加上 `--cli` 參數。以下是在「CLI」模式下列出伺服器所有工具的範例：

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 手動測試

除了使用 inspector 工具測試伺服器功能外，另一類似方法是使用能發送 HTTP 請求的客戶端工具，例如 curl。

使用 curl，您可以直接用 HTTP 請求測試 MCP 伺服器：

```bash
# 範例: 測試伺服器元資料
curl http://localhost:3000/v1/metadata

# 範例: 執行工具
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

從上述 curl 用法可見，您使用 POST 請求呼叫工具，並傳送含工具名稱及其參數的 payload。請選擇最適合您的方法。一般而言 CLI 工具使用較快速，且易於編寫腳本，在 CI/CD 環境中特別實用。

### 單元測試

為您的工具和資源建立單元測試，確保其如預期運作。以下是一些示範測試程式碼。

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
        # 測試無游標參數（省略）
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # 使用 cursor=None 測試
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # 使用字串作為游標測試
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # 使用空字串游標測試
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

上述程式碼做了以下事情：

- 採用 pytest 框架，讓您可以用函式建立測試，並使用 assert 陳述式。
- 建立一個有兩個不同工具的 MCP 伺服器。
- 使用 `assert` 陳述式檢查特定條件是否符合。

您可以參考[完整檔案](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

參考此檔，您可以測試自己的伺服器確保功能正常建立。

所有主要 SDK 都有類似的測試章節，可依您選擇的執行環境調整。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)

## 其他資源

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 下一步

- 下一課： [部署](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文的母語版本應被視為權威來源。若涉及重要資訊，建議尋求專業人工翻譯。我們不對因使用此翻譯而引致的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->