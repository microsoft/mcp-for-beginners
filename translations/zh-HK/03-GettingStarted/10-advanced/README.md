# 進階伺服器使用

MCP SDK 中公開了兩種類型的伺服器，分別是你一般使用的伺服器和低階伺服器。通常，你會使用一般伺服器來為其添加功能，但在某些情況下，你會想要依賴低階伺服器，例如：

- 更佳架構。雖然可以同時搭配一般伺服器和低階伺服器來建立較乾淨的架構，但有人會認為以低階伺服器實現會稍微容易一些。
- 功能可用性。有些進階功能只能使用低階伺服器。稍後章節中我們新增抽樣與引導時會看到這點。

## 一般伺服器 vs 低階伺服器

以下是用一般伺服器建立 MCP Server 的樣貌

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

// 加入一個加法工具
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

重點是你需要明確地加入你想要伺服器擁有的每個工具、資源或提示。這種方式沒有問題。

### 低階伺服器方法

然而，採用低階伺服器方法時，你需要用不同思維。你不需註冊每個工具，而是為每種類型的功能（工具、資源或提示）建立兩個處理器。舉例來說，工具會有兩個函式：

- 列出所有工具。一個函式負責所有列出工具的請求。
- 處理呼叫所有工具。這裡也只有一個函式負責工具呼叫。

聽起來似乎工作量比較小對吧？因此不需註冊工具，我只需確保當列出所有工具時，它會被列出，且當收到呼叫工具的請求時能夠被呼叫。

我們來看看現在程式碼長什麼樣：

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

這邊我們有一個函式回傳功能清單。工具列表的每個項目都有 `name`、`description` 和 `inputSchema` 等欄位，符合回傳型別。這使我們可以把工具和功能定義放到其他地方。我們現在可以把所有工具放在 tools 資料夾，其他功能也是如此，因此你的專案可以變得像這樣組織：

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

這很棒，我們的架構可以做得相當乾淨。

呼叫工具呢，是不是同樣的想法，只有一個處理器處理所有工具呼叫？沒錯，以下是相關程式碼：

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools 是以工具名稱為鍵的字典
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
    
    // args: request.params.arguments
    // TODO 調用該工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

從上面程式碼可以看到，我們需要解析要呼叫的工具名稱及其參數，接著執行呼叫。

## 以驗證改進這思路

至此，你已看到原先註冊所有工具、資源和提示的過程被改寫成每種類型只需兩個處理器。我們還需要做什麼呢？應該加入某種驗證，確保呼叫工具時帶入正確的參數。每種執行環境都有自己的解決方案，例如 Python 用 Pydantic，TypeScript 用 Zod。我們的思路是：

- 將建立功能（工具、資源或提示）的邏輯搬到其專屬資料夾。
- 增加方式驗證發來的請求（例如呼叫工具的）是否有效。

### 建立功能

要建立功能，我們需要建立一個檔案，並確保該檔案有每個該功能必備的欄位。各功能的欄位會稍微不同。

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

這裡示範如何：

- 使用 Pydantic 在 *schema.py* 裡建立一個名為 `AddInputModel` 的 schema，欄位為 `a` 和 `b`。
- 嘗試解析傳入的請求為 `AddInputModel` 型別，如果參數不符將會報錯：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以選擇把這段解析邏輯放在工具呼叫的函式裡，或是放在處理器函式中。

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

- 在處理所有工具呼叫的處理器中，我們會嘗試將傳入請求解析為該工具定義的 schema：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    成功後再繼續執行實際工具呼叫：

    ```typescript
    const result = await tool.callback(input);
    ```

如你所見，這種方法讓架構很好地井然有序，*server.ts* 是極小的檔案，只負責連接請求處理器，每個功能都在自己的資料夾，如 tools/、resources/ 或 prompts/。

太好了，接下來我們試著建立它。

## 練習：建立低階伺服器

在這個練習中，我們將完成：

1. 建立一個低階伺服器，處理列出工具和工具呼叫。
2. 實作可擴充的架構。
3. 新增驗證確保呼叫工具時參數有效。

### -1- 建立架構

我們首先要建立的，是方便隨著功能增加而擴充的架構，如下所示：

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

現在我們建立了這樣架構，確保可以輕鬆在 tools 資料夾新增工具。你也可以照此再為 resources 和 prompts 建立子目錄。

### -2- 建立工具

接著來看看建立工具的樣貌。首先要在其 *tool* 子目錄裡建立工具，如下：

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

這裡展示如何用 Pydantic 定義名稱、描述和輸入 schema，還有處理器 handler，會在該工具被呼叫時執行。最後公開 `tool_add` 字典，包含了這些屬性。

此外還有 *schema.py*，用來定義工具所使用的輸入 schema：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們還需要填充 *__init__.py*，確保 tools 目錄被視為模組，並公開其中的模組，如下：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

隨著加入更多工具你可以持續在這檔案新增對應項目。

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

這裡我們建立一個字典包含屬性：

- name，工具名稱。
- rawSchema，Zod schema，用以驗證呼叫此工具時的請求。
- inputSchema，處理器會使用的 schema。
- callback，用來呼叫工具。

還有 `Tool` 型別用於把這字典轉成 mcp 伺服器處理器能接受的型別，樣子如下：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

此外，*schema.ts* 用來存放每個工具的輸入 schema，目前只有一個，但可隨工具增加而加入更多：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，我們接著處理列出工具的功能。

### -3- 處理列出工具

要處理列出工具，我們必須設置一個對應的請求處理器。要加到伺服器檔案的程式碼如下：

**Python**

```python
# 程式碼為簡潔起見已被省略
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

這裡我們加上裝飾器 `@server.list_tools` 和實作函式 `handle_list_tools`。在該函式中需要回傳工具清單，注意每個工具需要有 name、description 與 inputSchema。

**TypeScript**

要為列出工具設定請求處理器，我們會在伺服器上呼叫 `setRequestHandler`，並帶入相符的 schema，這裡是 `ListToolsRequestSchema`。

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
// 為簡潔省略代碼
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 返回已註冊工具的列表
  return {
    tools: tools
  };
});
```

太好了，工具列出部分搞定，接下來看怎麼呼叫工具。

### -4- 處理呼叫工具

要呼叫工具，我們需要設置另一個請求處理器，專門針對請求中指定要呼叫哪個功能和帶入哪些參數進行處理。

**Python**

我們使用裝飾器 `@server.call_tool`，並以 `handle_call_tool` 函式實作。在該函式中，要拆解工具名稱、其參數，並確保參數對該工具有效。我們可以選擇在此函式驗證參數，或在工具實作端驗證。

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

執行流程說明：

- 工具名稱已經由輸入參數 `name` 傳入，呼叫的參數則是 `arguments` 字典。

- 工具透過 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 呼叫。參數驗證是在 `handler` 函式中進行，驗證失敗會丟例外。

如此，我們對用低階伺服器列出與呼叫工具有完整理解。

完整範例請見 [full example](./code/README.md)

## 作業

擴展你手上已有代碼，新增多個工具、資源和提示，並觀察你只需在 tools 目錄中新增檔案，其他地方幾乎無需改動的狀況。

*無提供解答*

## 總結

本章介紹低階伺服器的運作方式，以及如何藉此建立可維護擴充的架構。同時說明驗證的重要性，並展示如何運用驗證庫來為輸入建立 schema。

## 下一步

- 下一章：[簡易身份驗證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用人工智能翻譯服務 [Co-op 翻譯器](https://github.com/Azure/co-op-translator) 所翻譯。儘管我們致力於準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->