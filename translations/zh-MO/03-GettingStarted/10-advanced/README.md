# 進階伺服器使用

MCP SDK 中公開了兩種不同類型的伺服器，分別是一般伺服器和低階伺服器。通常，你會使用一般伺服器來為其添加功能。但有些情況下，你可能想依賴低階伺服器，例如：

- 更好的架構。使用一般伺服器和低階伺服器都能建立乾淨的架構，但可以說低階伺服器稍微容易一些。
- 功能可用性。某些進階功能只能用低階伺服器使用。你會在後面的章節看到，我們如何加入取樣和誘導。

## 一般伺服器 vs 低階伺服器

以下是用一般伺服器建立 MCP Server 的樣子

**Python**

```python
mcp = FastMCP("Demo")

# 添加一個加法工具
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

重點是你必須明確添加你想讓伺服器擁有的每個工具、資源或提示。這沒什麼問題。

### 低階伺服器方法

但是，使用低階伺服器時需要用不同思維來考慮。你不是註冊每個工具，而是針對每種功能類型（工具、資源或提示）建立兩個處理函式。比如說工具只有兩個函式：

- 列出所有工具。一個函式負責所有列出工具的請求。
- 處理呼叫所有工具。這裡也只有一個函式處理呼叫工具。

聽起來好像工作量較少對吧？因此，你不用註冊工具，只需確保當列出所有工具時該工具出現，且當有呼叫工具的請求時該工具會被呼叫。

我們來看看現在的程式碼長什麼樣：

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
        name: "add",
        description: "Add two numbers",
        inputSchema: {
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

這裡我們有一個函式回傳功能列表。工具清單中的每個項目都具有 `name`、`description` 和 `inputSchema` 等欄位以符合回傳類型。這讓我們能把工具和功能定義放在其他地方。我們現在可以把所有工具放在 tools 資料夾，其他功能也是如此，專案就能突然變得像這樣組織：

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

太好了，我們的架構可以變得非常乾淨。

那呼叫工具呢？是不是也是一個處理函式呼叫任意工具？沒錯，這是程式碼：

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools 是一個以工具名稱作為鍵的字典
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
    // 待辦 呼叫該工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

如上程式碼，我們要解析要呼叫的工具是什麼、帶什麼參數，然後進行工具呼叫。

## 用驗證來改進方法

目前為止你已看到如何用這兩個處理函式替代添加工具、資源和提示的所有註冊。我們還需要做什麼？我們應該加個驗證機制來確保工具被呼叫時帶上正確參數。每種執行環境都有自己的方案，例如 Python 用 Pydantic，TypeScript 用 Zod。想法如下：

- 將建立功能（工具、資源或提示）的邏輯移至專屬資料夾。
- 新增機制驗證傳入的請求，例如呼叫工具。

### 建立功能

建立功能時，我們必須為該功能建立檔案，並確保具有必要欄位，各欄位在工具、資源、提示中略有不同。

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

    # TODO: 加入 Pydantic，咁我哋可以創建一个 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

你可以看到我們做了以下事：

- 使用 Pydantic 在 *schema.py* 中建立具有欄位 `a` 和 `b` 的 `AddInputModel` schema。
- 嘗試把傳入請求解析成 `AddInputModel`，參數不符合會導致崩潰：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以選擇把解析邏輯放在工具呼叫裡或放在處理函式中。

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

       // @ts-忽略
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

- 在處理所有工具呼叫的 handler 中，嘗試把傳入請求解析為該工具定義的 schema：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果解析成功，我們就繼續呼叫工具：

    ```typescript
    const result = await tool.callback(input);
    ```

可見這種方法創建很好的架構，每件事都有自己的位置，*server.ts* 是非常小的檔案，僅用於接線請求處理，且每個功能都在相應的資料夾裡，例如 tools/、resources/ 或 prompts/。

很好，我們接著試著構建這些。

## 練習：建立低階伺服器

本練習我們將做：

1. 建立一個低階伺服器，處理工具列表和工具呼叫。
2. 實現一個可供繼續擴展的架構。
3. 新增驗證確保工具呼叫帶正確參數。

### -1- 建立架構

首先要處理一個能隨功能增長而擴展的架構，如下：

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

我們已建好架構，能輕易在 tools 資料夾中加入新工具。也可以依此增設 resources 和 prompts 子目錄。

### -2- 建立工具

接著看看建立工具長什麼樣。首先，工具得放在 tools 子目錄，像是：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待辦事項：添加 Pydantic，這樣我們可以創建一個 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

我們在此定義名稱、描述和使用 Pydantic 描述輸入的 schema，還有被呼叫時會執行的 handler。最後透過 `tool_add` 將這些屬性以字典形式暴露出來。

還有 *schema.py*，用來定義工具使用的輸入 schema：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們也需將 *__init__.py* 填充，確保 tools 資料夾被視為模組。還要暴露裡面的模組，像這樣：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

隨著加入更多工具，我們會不斷擴充此檔案。

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

我們建立包含多個屬性的字典：

- name：工具名稱。
- rawSchema：Zod schema，用來驗證傳入呼叫該工具的請求。
- inputSchema：handler 使用的 schema。
- callback：執行工具的函式。

還有一個 `Tool` 用來把字典轉成 mcp server handler 可接受的類型，如下：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

還有 *schema.ts*，我們會把各工具的輸入 schemas 放在這，目前只有一個 schema，但未來可新增多筆：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，我們接著處理如何列出工具。

### -3- 處理工具列表

要處理工具列表，需在伺服器檔案新增請求處理函式：

**Python**

```python
# 為簡潔起見已省略程式碼
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

這裡加上裝飾器 `@server.list_tools` 和實作函式 `handle_list_tools`。在該函式中，回傳工具清單。注意每個工具要有 name、description 和 inputSchema。

**TypeScript**

要設定列出工具的請求處理，需要對伺服器呼叫 `setRequestHandler`，並傳入符合功能的 schema，這裡是 `ListToolsRequestSchema`。

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
// 為簡潔起見省略了程式碼
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 返回已註冊工具的清單
  return {
    tools: tools
  };
});
```

很好，工具列表已完成。我們接著看怎麼呼叫工具。

### -4- 處理呼叫工具

呼叫工具需要再設一個請求處理器，專門處理指定要呼叫何種功能與帶何參數的請求。

**Python**

我們用裝飾器 `@server.call_tool`，實作函式 `handle_call_tool`。該函式中需解析工具名稱及參數，並確保參數對應工具有效。參數驗證可在此函式中做，也可在工具本體做。

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools 是一個以工具名稱作為鍵的字典
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

- 工具名稱已存在於輸入參數 `name`，參數則位於 `arguments` 字典。
- 透過 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 呼叫工具。參數合法與否會在 `handler` 指向的函式中驗證，出錯會拋例外。

好了，我們現在完整了解如何用低階伺服器列出與呼叫工具。

請見完整範例於此 [full example](./code/README.md)

## 作業

擴充你手上的程式碼，加入多個工具、資源及提示，並反思你只需在 tools 資料夾新增檔案，其他地方完全不須變動。

<em>無解答提供</em>

## 總結

本章我們介紹低階伺服器方法及如何用它打造可繼續擴充的良好架構。也講述驗證，並示範如何使用驗證函式庫建立輸入驗證的 schema。

## 接下來

- 下一章：[簡單認證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。文件之原始語言版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引致之任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->