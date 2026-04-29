## 測試與除錯

在開始測試您的 MCP 伺服器之前，了解可用的工具和最佳除錯實務非常重要。有效的測試能確保您的伺服器按預期運作，並幫助您快速識別和解決問題。以下章節概述了驗證 MCP 實作的建議方法。

## 概觀

本課程涵蓋如何選擇合適的測試方法以及最有效的測試工具。

## 學習目標

完成本課程後，您將能夠：

- 描述各種測試方法。
- 使用不同工具有效測試您的程式碼。

## 測試 MCP 伺服器

MCP 提供工具協助您測試和除錯伺服器：

- **MCP Inspector**：一個可作為 CLI 工具或視覺化工具使用的命令列工具。
- <strong>手動測試</strong>：您可以使用像 curl 這類工具執行 Web 請求，但任何能執行 HTTP 的工具皆可使用。
- <strong>單元測試</strong>：您可以使用偏好的測試框架測試伺服器和客戶端的功能。

### 使用 MCP Inspector

我們在之前的課程中介紹過此工具的用法，但這裡稍作說明。它是一個用 Node.js 建立的工具，您可以透過呼叫 `npx` 執行檔使用，該指令會暫時下載並安裝此工具，執行完您的請求後即自動清理。

[<a href="https://github.com/modelcontextprotocol/inspector" target="_blank" rel="noopener">MCP Inspector</a>] 幫助您：

- <strong>偵測伺服器功能</strong>：自動辨識可用的資源、工具與提示
- <strong>測試工具執行</strong>：嘗試不同參數並即時看見回應
- <strong>檢視伺服器資訊</strong>：檢查伺服器資訊、架構及設定

工具的典型執行範例如下：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

上述命令啟動 MCP 及其視覺化介面，並在瀏覽器中開啟本地 Web 介面。您將看到一個儀表板，顯示註冊的 MCP 伺服器、其可用工具、資源及提示。介面讓您能互動式測試工具執行、檢查伺服器元資料及觀看即時回應，更輕鬆驗證和除錯 MCP 伺服器實作。

介面範例如下： ![Inspector](../../../../translated_images/zh-HK/connect.141db0b2bd05f096.webp)

您也可以以 CLI 模式執行此工具，方法是在命令中加上 `--cli` 參數。這是以「CLI」模式執行工具並列出伺服器上所有工具的範例：

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 手動測試

除了執行 Inspector 工具測試伺服器功能外，另一相似方法是執行可用 HTTP 的客戶端，如 curl。

利用 curl，您可以透過 HTTP 請求直接測試 MCP 伺服器：

```bash
# 範例：測試伺服器元資料
curl http://localhost:3000/v1/metadata

# 範例：執行工具
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

如上所示，使用 curl 發送 POST 請求，以工具名稱及參數組成的有效負載來呼叫工具。請選擇最適合您的方法。CLI 工具通常較快且易於編寫指令碼，適用於 CI/CD 環境。

### 單元測試

為您的工具和資源建立單元測試，以確保其正常運作。以下是示範測試程式碼。

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

        # 測試 cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # 測試 cursor 為字串
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # 測試空字串游標
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

上述程式碼做了以下幾件事：

- 利用 pytest 框架，讓您能以函式形式建立測試並使用 assert 陳述式。
- 建立一個包含兩個不同工具的 MCP 伺服器。
- 使用 `assert` 陳述式檢查特定條件是否成立。

請參考[此完整檔案](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

根據上述檔案，您可以測試自己的伺服器，確保功能如預期被建立。

所有主要 SDK 都有類似的測試章節，您可以視所選運行環境調整。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)

## 附加資源

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 下一步

- 下一課： [部署](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->