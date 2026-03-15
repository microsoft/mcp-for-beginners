## 測試與除錯

在開始測試您的 MCP 伺服器之前，瞭解可用的工具和除錯最佳實務非常重要。有效的測試確保您的伺服器表現符合預期，並幫助您快速識別與解決問題。以下章節概述了驗證您的 MCP 實作所推薦的方法。

## 概覽

本課程涵蓋如何選擇正確的測試方法及最有效的測試工具。

## 學習目標

課程結束時，您將能夠：

- 描述各種測試方法。
- 使用不同工具有效地測試您的程式碼。

## 測試 MCP 伺服器

MCP 提供工具來協助您測試與除錯伺服器：

- **MCP Inspector**：一個可作為 CLI 工具及視覺化工具執行的指令行工具。
- **手動測試**：您可以使用像 curl 這類工具來執行 Web 請求，任何能執行 HTTP 的工具皆可。
- **單元測試**：您可以使用偏好的測試框架來測試伺服器與客戶端的功能。

### 使用 MCP Inspector

我們在先前課程已介紹此工具的使用，這裡稍作宏觀說明。此工具是基於 Node.js 架構，您可以透過呼叫 `npx` 執行檔使用，該指令會暫時下載並安裝該工具，完成請求後將自行清理。

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) 能幫助您：

- **探索伺服器能力**：自動偵測可用資源、工具和提示
- **測試工具執行**：嘗試不同參數並即時查看回應
- **檢視伺服器元資料**：檢查伺服器資訊、架構及設定

工具的典型執行如以下顯示：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

上述指令啟動 MCP 及其視覺化介面，並在瀏覽器中啟動本地網頁介面。您可以看到一個儀表板，顯示您已註冊的 MCP 伺服器、其可用工具、資源和提示。此介面允許您互動測試工具執行，檢視伺服器元資料及實時回應，使驗證和除錯 MCP 伺服器實作更加方便。

介面示意圖如下： ![Inspector](../../../../translated_images/zh-TW/connect.141db0b2bd05f096.webp)

您也可以以 CLI 模式執行此工具，只需加入 `--cli` 屬性。以下範例示範以「CLI」模式執行工具，列出伺服器上的所有工具：

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 手動測試

除了使用 inspector 工具測試伺服器能力外，另一相似方法是執行支援 HTTP 的用戶端工具，例如 curl。

使用 curl，您可以直接利用 HTTP 請求測試 MCP 伺服器：

```bash
# 範例：測試伺服器元資料
curl http://localhost:3000/v1/metadata

# 範例：執行工具
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

從上述 curl 的用法可見，您使用 POST 請求來呼叫工具，負載(payload)包含工具名稱及其參數。請使用最符合您需求的方法。一般而言，CLI 工具速度較快且容易腳本化，這對於 CI/CD 環境十分有用。

### 單元測試

為您的工具和資源建立單元測試，以確保它們按預期運作。以下為範例測試程式碼：

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

    # 創建幾個測試工具
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

前述程式碼完成以下工作：

- 利用 pytest 框架，讓您以函式方式創建測試並使用 assert 陳述式。
- 建立具兩個不同工具的 MCP 伺服器。
- 使用 `assert` 陳述句檢查特定條件是否符合。

可參考[完整檔案](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

基於上述檔案，您可以測試自家伺服器，以確保功能正確建立。

所有主要 SDK 都有類似測試章節，您可以根據選用的執行環境加以調整。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)

## 額外資源

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 下一步

- 下一節：[部署](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言版本文件應被視為權威資料來源。對於重要資訊，建議聘請專業人工翻譯。我們不對因使用本翻譯內容所產生之任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->