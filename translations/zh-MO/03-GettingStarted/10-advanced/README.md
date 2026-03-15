# 進階伺服器使用

MCP SDK 中有兩種不同類型的伺服器，一個是一般伺服器，另一個是低階伺服器。通常你會使用一般伺服器來新增功能。不過在某些情況下，你可能會依賴低階伺服器，例如：

- 更好的架構設計。雖然可以用一般伺服器和低階伺服器創建乾淨的架構，但可以說用低階伺服器會略為容易些。
- 功能可用性。有些進階功能只能用低階伺服器來實作。你會在後面的章節看到我們新增取樣和引導的時候。

## 一般伺服器 vs 低階伺服器

以下是使用一般伺服器創建 MCP 伺服器的範例

**Python**

```python
mcp = FastMCP("Demo")

# 新增一個加法工具
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**TypeScript**

```typescript
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// 添加一個加法工具
server.registerTool("add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);
```

重點是你會明確地新增每個你想讓伺服器擁有的工具、資源或提示。這樣做沒有錯。

### 低階伺服器方法

不過，使用低階伺服器時，思考方式會不一樣。你不再註冊每個工具，而是會為每種功能類型（工具、資源或提示）創建兩個函數處理器。譬如說，針對工具只有兩個功能：

- 列出所有工具。一個函數負責所有列出工具的嘗試。
- 處理呼叫所有工具。在這裡，也是只有一個函數負責處理各工具的呼叫。

聽起來似乎工作量比較少，對吧？所以不需要註冊工具，只要確保工具列表在列出時出現，接著在收到呼叫工具的請求時正確呼叫它就好。

我們來看現在程式碼長什麼樣：

**Python**

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="add",
            description="Add two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "number to add"}, 
                    "b": {"type": "number", "description": "number to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 返回已註冊工具的清單
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "number to add"}, 
                "b": {"type": "number", "description": "number to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

這裡我們有一個回傳功能列表的函式。工具列表中，每個項目都有像 `name`、`description` 和 `inputSchema` 等欄位，以符合回傳型別。我們可以把工具和功能定義放在別處，現在我們可以在 tools 資料夾建立所有工具，功能同樣如此，專案就能突然這樣組織：

```text
app
--| tools
----| add
----| substract
--| resources
----| products
----| schemas
--| prompts
----| product-description
```

非常好，我們的架構看起來相當乾淨。

那呼叫工具是否也是這個概念，一個處理器呼叫任意工具？是的，完全正確，程式碼如下：

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools 是一個以工具名稱為鍵的字典
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

**TypeScript**

```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if(!tool) {
        return {
            error: {
                code: "tool_not_found",
                message: `Tool ${name} not found.`
            }
       };
    }
    
    // 參數：request.params.arguments
    // 待辦事項 呼叫工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

從上面的程式碼你可以看出，我們需要解析要呼叫哪個工具，並帶入何種參數，接著才能真正呼叫該工具。

## 用驗證改進方法

到現在為止，你已經看到用兩個處理器代替註冊所有工具、資源和提示的作法。我們還需要做什麼？我們應該加上某種驗證，確保工具被呼叫時帶的參數正確。每種執行環境都有自己的解決方案，例如 Python 使用 Pydantic，TypeScript 使用 Zod。做法是：

- 把建立一個功能（工具、資源或提示）的邏輯移到其專屬資料夾。
- 增加一種方式來驗證進來的請求，例如確認呼叫某工具時參數正確。

### 建立一個功能

要建立功能，我們需要建立該功能的檔案並確保其具備此功能所必需的欄位。不同類型（工具、資源、提示）欄位會略有不同。

**Python**

```python
# schema.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# add.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待辦事項：加入 Pydantic，以便我們可以創建 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

可看到我們如何：

- 使用 Pydantic 在 *schema.py* 檔透過 `AddInputModel` 建立結構，欄位有 `a`, `b`。
- 嘗試將進來的請求解析為 `AddInputModel` 型別，參數不符合時會出錯：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以選擇把此解析邏輯寫在工具的呼叫裡或在處理器函式中。

**TypeScript**

```typescript
// 伺服器.ts
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if (!tool) {
       return {
        error: {
            code: "tool_not_found",
            message: `Tool ${name} not found.`
        }
       };
    }
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);

       // @ts-ignore
       const result = await tool.callback(input);

       return {
          content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
      };
    } catch (error) {
       return {
          error: {
             code: "invalid_arguments",
             message: `Invalid arguments for tool ${name}: ${error instanceof Error ? error.message : String(error)}`
          }
    };
   }

});

// 架構.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// 新增.ts
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

- 在處理所有工具呼叫的處理器中，我們會嘗試將進入請求解析成該工具定義的結構：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    若成功就繼續呼叫實際工具：

    ```typescript
    const result = await tool.callback(input);
    ```

正如你所見，這種作法建立了良好架構，一切都有其位置，*server.ts* 是一個很小的檔案，僅連接請求處理器，每個功能放在其對應資料夾，即 tools/、resources/ 或 prompts/。

很好，我們接著練習實作。

## 練習：建立低階伺服器

此練習我們將進行以下事項：

1. 建立一個低階伺服器，負責列出工具及呼叫工具。
1. 實作一個可繼續擴充的架構。
1. 加入驗證，確保工具呼叫正確驗證。

### -1- 建立架構

首先我們要建立的架構幫助日後擴展功能，長這樣：

**Python**

```text
server.py
--| tools
----| __init__.py
----| add.py
----| schema.py
client.py
```

**TypeScript**

```text
server.ts
--| tools
----| add.ts
----| schema.ts
client.ts
```

現在我們已設計一個架構，可輕鬆在 tools 資料夾中新增新工具。你也可依此為資源和提示建立子資料夾。

### -2- 建立工具

我們來看建立工具的步驟。首先，要在其 *tool* 子資料夾建立：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待辦事項：添加 Pydantic，以便我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

這裡展示如何定義名稱、說明和 Pydantic 的輸入結構，以及會被呼叫的處理函式。最後，我們公開 `tool_add` 字典，包含所有這些屬性。

還有 *schema.py* 定義工具的輸入結構如下：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們還需要填寫 *__init__.py*，確保 tools 目錄被視為模組，並且公開模組內的內容，如下：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

隨著新增工具，我們會繼續擴充此檔案。

**TypeScript**

```typescript
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

這裡建立一個字典，包含屬性：

- name，工具名稱。
- rawSchema，Zod 結構，用來驗證呼叫工具的請求。
- inputSchema，供處理器使用的結構。
- callback，負責執行該工具。

還有 `Tool`，用來將此字典轉換成 MCP 伺服器處理器可接受的型別，內容大概長這樣：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

另外有 *schema.ts* 儲存每個工具的輸入結構，目前只有一個結構，但隨著新增工具會越來越多：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，我們接著處理工具列表的部分。

### -3- 處理列出工具

接著要處理列出工具的請求，需要為此建立一個請求處理器。以下是要加到伺服器檔案的內容：

**Python**

```python
# 為簡潔起見，已省略代碼
from tools import tools

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    tool_list = []
    print(tools)

    for tool in tools.values():
        tool_list.append(
            types.Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=pydantic_to_json(tool["input_schema"]),
            )
        )
    return tool_list
```

這裡加上裝飾器 `@server.list_tools` 和實作函式 `handle_list_tools`。裡面要產生工具列表。注意每個工具需要有名稱、說明和輸入結構。

**TypeScript**

要建立列出工具的請求處理器，需要對伺服器呼叫 `setRequestHandler`，並帶入符合操作的結構，此處為 `ListToolsRequestSchema`。

```typescript
// index.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// server.ts
// 為簡潔起見省略代碼
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 返回已註冊工具的列表
  return {
    tools: tools
  };
});
```

太好了，我們解決了列出工具部分，接著看看呼叫工具的實作。

### -4- 處理呼叫工具

呼叫工具時，我們要設置另一個請求處理器，專注處理接收哪個功能與參數的請求。

**Python**

使用裝飾器 `@server.call_tool`，並用函式 `handle_call_tool` 來實作。該函式中，我們要解析工具名稱和其參數，並確保參數對該工具有效。我們可以選擇在這裡驗證參數，或在實際工具中下游驗證。

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools 是一個以工具名稱為鍵的字典
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # 調用該工具
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

流程說明：

- 工具名稱已在輸入參數 `name` 中，參數是 `arguments` 字典。
- 用 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 呼叫工具，在 handler 屬性指向的函式中驗證參數，若失敗將會拋錯。

這樣，我們就完整理解了如何用低階伺服器列出和呼叫工具。

在此查看[完整範例](./code/README.md)

## 作業

在給你的程式碼中新增多個工具、資源和提示，並注意發現只需在 tools 目錄新增檔案，不用改其他地方。

*不提供解答*

## 總結

本章我們了解低階伺服器的運作，及其如何幫助創建易擴充且乾淨的架構。我們也討論了驗證，並展示如何使用驗證函式庫建立輸入結構以進行驗證。

## 接下來

- 下一章: [簡單認證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由人工智能翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。文件的原始語言版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而引起的任何誤解或誤釋，我們不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->