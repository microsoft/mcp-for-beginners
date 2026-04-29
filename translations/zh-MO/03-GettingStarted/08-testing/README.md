## 測試與除錯

在開始測試您的 MCP 伺服器之前，了解可用的工具及除錯的最佳實踐非常重要。有效的測試能確保您的伺服器行為符合預期，並幫助您快速識別與解決問題。以下章節概述了驗證 MCP 實作的推薦方法。

## 概述

本課程涵蓋如何選擇合適的測試方法及最有效的測試工具。

## 學習目標

完成本課程後，您將能夠：

- 描述各種測試方法。
- 使用不同工具有效地測試您的程式碼。

## 測試 MCP 伺服器

MCP 提供工具幫助您測試與除錯您的伺服器：

- **MCP Inspector**：一個可以同時當作 CLI 工具與視覺化工具執行的指令列工具。
- <strong>手動測試</strong>：您可以使用像 curl 這樣的工具執行網路請求，但任何能執行 HTTP 的工具皆適用。
- <strong>單元測試</strong>：您可以使用喜歡的測試框架來測試伺服器與用戶端的功能。

### 使用 MCP Inspector

我們先前課程已描述此工具的使用方法，這裡略述其概況。它是使用 Node.js 建置的工具，您可以透過執行 `npx` 指令使用它，該指令會暫時下載並安裝此工具，執行您的請求後會自行清理。

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) 幫助您：

- <strong>偵測伺服器功能</strong>：自動發現可用的資源、工具和提示
- <strong>測試工具執行</strong>：嘗試不同參數並即時查看回應
- <strong>檢視伺服器元資料</strong>：審視伺服器資訊、架構及設定

工具的典型執行示例如下：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

上述指令會啟動 MCP 及其視覺介面，並在瀏覽器中開啟本機網頁介面。您會看到一個儀表板，顯示您註冊的 MCP 伺服器、其可用的工具、資源及提示。介面允許您互動式地測試工具執行、檢查伺服器元資料及即時查看回應，使驗證與除錯 MCP 伺服器實作更為方便。

畫面看起來像這樣：![Inspector](../../../../translated_images/zh-MO/connect.141db0b2bd05f096.webp)

您也可以以 CLI 模式執行此工具，方法是在指令中加入 `--cli` 屬性。以下是以「CLI」模式執行工具列出伺服器上所有工具的範例：

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 手動測試

除了執行 Inspector 測試伺服器功能外，另一種類似方法是運行能使用 HTTP 的客戶端工具，例如 curl。

利用 curl，您可以直接使用 HTTP 請求測試 MCP 伺服器：

```bash
# 例子：測試伺服器元數據
curl http://localhost:3000/v1/metadata

# 例子：執行工具
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

從上述 curl 使用方式可以看出，您使用 POST 請求透過包含工具名稱及參數的有效負載呼叫工具。請選擇最適合您的方式。一般來說，CLI 工具使用起來較快速且易於編寫腳本，於 CI/CD 環境中尤為實用。

### 單元測試

為您的工具和資源建立單元測試，以確保它們如預期運作。以下是一些範例測試程式碼。

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

    # 創建一些測試工具
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

前述程式碼說明：

- 利用 pytest 框架，可以將測試寫成函式並使用 assert 陳述式。
- 建立一個包含兩個不同工具的 MCP 伺服器。
- 使用 `assert` 陳述式檢查特定條件是否成立。

請參考[完整檔案](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

有了上述檔案，您可以測試自己的伺服器以確保所建立的功能皆正常。

所有主流 SDK 都有相似的測試章節，您可依選擇的執行環境進行調整。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)

## 其他資源

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 下一步

- 下一步：[部署](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件以其母語版本為權威來源。對於重要資訊，建議採用專業人工翻譯。本公司不對因使用本翻譯所產生之任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->