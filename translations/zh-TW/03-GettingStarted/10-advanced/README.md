# 進階伺服器使用方式

MCP SDK 中暴露兩種不同類型的伺服器，分別是一般伺服器及低階伺服器。通常，你會使用一般伺服器來新增功能。不過，某些情況下，你會想仰賴低階伺服器，例如：

- 更佳架構。雖然可同時使用一般伺服器和低階伺服器來建立乾淨的架構，但可以說用低階伺服器會稍微容易些。
- 功能支援。有些進階功能只能使用低階伺服器。後面章節中我們加入取樣與誘導時會看到這點。

## 一般伺服器 與 低階伺服器

以下是建立 MCP Server 使用一般伺服器的範例：

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

// 新增一個加法工具
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

重點是你必須明確新增你想讓伺服器擁有的各項工具、資源或提示詞。這沒什麼不對。

### 低階伺服器方式

然而，使用低階伺服器方式時，需要用不同思維。你不是註冊每個工具，而是針對每種類型的功能（工具、資源或提示詞）建立兩個處理器。例如，工具只要兩個函式：

- 列出所有工具。一個函式負責所有列出工具的嘗試。
- 處理呼叫所有工具。此處同樣只有一個函式負責呼叫工具。

聽起來像是工作量變少了對吧？所以不用註冊工具，只要確保這工具會被列在所有工具列表中，且在接收到呼叫工具的請求時會被呼叫就好。

以下是程式碼範例：

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
  // 返回已註冊工具的列表
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

這裡我們有一個函式會回傳功能列表。工具清單中每個項目都有 `name`、`description` 和 `inputSchema` 等欄位，以符合回傳型別。這讓我們可以將工具與功能定義放在其他地方。我們現在可以在 tools 資料夾中建立所有工具，其他功能也是，同理如此，因此專案案結構看起來會像這樣：

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

非常好，我們的架構可以建立得相當乾淨。

呼叫工具呢？也是同樣概念，一個處理器負責呼叫任一工具？沒錯，程式碼如下：

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
    // 待辦 呼叫工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

從上方程式碼可見，我們需要解析要呼叫的工具與參數，接著進行呼叫。

## 用驗證改善此做法

到目前為止，你看到所有註冊新增工具、資源和提示詞的作法，都可用每種類型兩個處理器取代。還有什麼是必要的呢？我們應增加某種形式的驗證，確保工具呼叫時使用正確參數。各執行環境有不同解決方案，例如 Python 使用 Pydantic，TypeScript 使用 Zod。理念如下：

- 把建立功能（工具、資源或提示詞）的邏輯移到專屬資料夾。
- 增加驗證來核對傳入請求，例如呼叫工具時。

### 建立功能

建立功能時，我們會為該功能建立檔案，並確保該功能具有必要欄位。工具、資源和提示詞需要的欄位略有差異。

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

    # TODO: 加入 Pydantic，以便我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

此處示範了：

- 用 Pydantic 在 *schema.py* 建立 `AddInputModel` 架構，並有欄位 `a` 和 `b`。
- 嘗試將傳入請求解析為 `AddInputModel`，如果參數不符會噴錯：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可決定要把此解析邏輯放在工具呼叫本體還是處理器函式。

**TypeScript**

```typescript
// server.ts
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

// schema.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// add.ts
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

- 在處理所有工具呼叫的處理器中，我們嘗試將傳入請求解析成工具定義的架構：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    若成功接著呼叫實際工具：

    ```typescript
    const result = await tool.callback(input);
    ```

可見此方式打造良好架構，所有東西都有位置，*server.ts* 僅負責連線請求處理器，各功能則位於各自資料夾（tools/、resources/ 或 /prompts）。

很好，接著實作此架構。

## 練習：建立低階伺服器

本練習會做以下事情：

1. 建立低階伺服器，處理工具列舉與工具呼叫。
1. 實作可擴充的架構。
1. 加入驗證以確保工具呼叫時參數正確。

### -1- 建立架構

首先要處理的是能隨著功能增加擴充的架構，如下所示：

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

我們已建立能輕鬆新增工具的 tools 資料夾架構。歡迎照此架構再新增 resources 與 prompts 子目錄。

### -2- 建立工具

接著來看看建立工具長什麼樣。首先，要在其 *tool* 子目錄建立：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: 加入 Pydantic，以便我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

我們看到如何定義名稱、描述與使用 Pydantic 建立輸入架構，以及工具被呼叫時會被調用的處理函式。最後我們公開 `tool_add`，該字典包含所有這些屬性。

還有 *schema.py* 定義我們工具使用的輸入架構：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們也需要填寫 *__init__.py* 以確保 tools 資料夾被視為模組，並且像這樣公開模組：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

新增工具時可以持續擴充此檔案。

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

我們建立一個字典，包含以下屬性：

- name，工具名稱。
- rawSchema，Zod 架構，用來驗證呼叫此工具的傳入請求。
- inputSchema，處理函式會使用的架構。
- callback，用於執行此工具。

還有 `Tool` 供將此字典轉換成 mcp 伺服器處理器可接受的型別：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

此處我們存放各工具輸入架構的 *schema.ts* 也長這樣，現階段只有一個架構，後續新增工具會增加更多項目：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，接著處理工具列舉。

### -3- 處理工具列舉

我們需要建立列舉工具的請求處理器，於是如下新增到伺服器檔案：

**Python**

```python
# 為簡潔起見省略程式碼
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

此處我們使用裝飾器 `@server.list_tools` 與對應實作函式 `handle_list_tools`。該函式要產生工具列表，請注意每工具均需有名稱、描述與 inputSchema。

**TypeScript**

要建立工具列舉處理器，我們呼叫伺服器的 `setRequestHandler`，並使用符合需求的架構此例為 `ListToolsRequestSchema`。

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
// 代碼略去以節省篇幅
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 回傳已註冊工具的列表
  return {
    tools: tools
  };
});
```

很好，工具列舉已處理完成，接著看如何呼叫工具。

### -4- 處理呼叫工具

建立新請求處理器，專攻接收欲呼叫功能及參數的請求。

**Python**

用裝飾器 `@server.call_tool` 實作如同函式 `handle_call_tool`。函式內需解析工具名稱、參數，並確定參數符合該工具要求。驗證可在此函式或工具本身進行。

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

說明如下：

- 輸入參數已有工具名稱 `name`，與包含參數的 `arguments` 字典。
- 以 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 呼叫工具。參數驗證在 `handler` 指向的函式內進行，若失敗將拋出錯誤。

如此，我們便完整理解如何用低階伺服器列舉及呼叫工具。

看此處 [完整範例](./code/README.md)

## 作業

擴充你手邊的程式碼，新增多個工具、資源與提示詞，體會你只需要在 tools 目錄新增檔案，無須更動其他地方。

*無解答提供*

## 總結

本章探討低階伺服器使用方式及它如何協助打造良好可擴充架構，也談及驗證，示範如何使用驗證函式庫來建立輸入驗證架構。

## 接下來

- 下一章：[簡單身份驗證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言文件應被視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->