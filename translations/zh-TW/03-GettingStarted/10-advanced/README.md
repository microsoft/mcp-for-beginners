# 高級伺服器使用

在 MCP SDK 中，有兩種不同類型的伺服器：普通伺服器和低階伺服器。通常，您會使用普通伺服器來添加功能。然而，在某些情況下，您可能需要依賴低階伺服器，例如：

- 更好的架構。雖然使用普通伺服器和低階伺服器都可以創建乾淨的架構，但可以說使用低階伺服器會稍微容易一些。
- 功能可用性。一些高級功能只能在低階伺服器中使用。在後續章節中，您將看到如何添加取樣和引導功能。

## 普通伺服器 vs 低階伺服器

以下是使用普通伺服器創建 MCP 伺服器的樣子：

**Python**

```python
mcp = FastMCP("Demo")

# Add an addition tool
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

// Add an addition tool
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

重點在於，您需要明確地添加每個工具、資源或提示到伺服器中。這種方式並沒有問題。

### 低階伺服器方法

然而，使用低階伺服器方法時，您需要以不同的方式思考。與其註冊每個工具，您需要為每種功能類型（工具、資源或提示）創建兩個處理器。例如，對於工具，僅需要兩個函數，如下所示：

- 列出所有工具。一個函數負責所有列出工具的請求。
- 處理所有工具的調用。這裡也僅有一個函數負責處理工具的調用。

這聽起來像是更少的工作量，對吧？因此，與其註冊每個工具，我只需要確保工具在列出所有工具時被列出，並且在有請求調用工具時被正確調用。

讓我們看看代碼的樣子：

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
                    "a": {"type": "number", "description": "nubmer to add"}, 
                    "b": {"type": "number", "description": "nubmer to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "nubmer to add"}, 
                "b": {"type": "number", "description": "nubmer to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

在這裡，我們有一個函數返回功能列表。工具列表中的每個條目現在都有 `name`、`description` 和 `inputSchema` 等字段，以符合返回類型。這使我們可以將工具和功能定義放在其他地方。我們現在可以在工具文件夾中創建所有工具，資源和提示也可以如此，從而使項目架構看起來像這樣：

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

這很棒，我們的架構可以變得非常乾淨。

那麼調用工具呢？是否也是同樣的思路，一個處理器負責調用任何工具？是的，完全正確，以下是相關代碼：

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
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
    // TODO call the tool, 

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

如上代碼所示，我們需要解析出要調用的工具及其參數，然後進一步調用該工具。

## 改進方法：添加驗證

到目前為止，您已看到如何用每種功能類型的兩個處理器替代所有工具、資源和提示的註冊。接下來需要做什麼？我們應該添加某種形式的驗證，以確保工具被正確的參數調用。每種運行時都有自己的解決方案，例如 Python 使用 Pydantic，TypeScript 使用 Zod。基本思路如下：

- 將創建功能（工具、資源或提示）的邏輯移到專用文件夾。
- 添加一種方法來驗證傳入的請求，例如調用工具的請求。

### 創建功能

要創建功能，我們需要為該功能創建一個文件，並確保它具有該功能所需的必填字段。不同功能（工具、資源和提示）的字段略有不同。

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
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

在這裡，您可以看到以下操作：

- 在文件 *schema.py* 中使用 Pydantic 創建一個名為 `AddInputModel` 的模式，包含字段 `a` 和 `b`。
- 嘗試將傳入的請求解析為 `AddInputModel` 類型，如果參數不匹配，則會報錯：

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

您可以選擇將此解析邏輯放在工具調用本身或處理器函數中。

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

- 在處理所有工具調用的處理器中，我們嘗試將傳入的請求解析為工具定義的模式：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果解析成功，我們就可以繼續調用實際的工具：

    ```typescript
    const result = await tool.callback(input);
    ```

如您所見，這種方法創建了一個良好的架構，每個部分都有其位置，*server.ts* 文件非常小，只負責連接請求處理器，而每個功能都在其各自的文件夾中，例如 tools/、resources/ 或 prompts/。

很好，接下來我們嘗試構建這個架構。

## 練習：創建低階伺服器

在這個練習中，我們將完成以下任務：

1. 創建一個低階伺服器，處理工具的列出和調用。
1. 實現一個可擴展的架構。
1. 添加驗證，確保工具調用得到正確的驗證。

### -1- 創建架構

首先，我們需要設計一個架構，幫助我們在添加更多功能時進行擴展，架構如下：

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

現在，我們已設置了一個架構，確保可以輕鬆地在工具文件夾中添加新工具。您可以按照此方式為資源和提示添加子目錄。

### -2- 創建工具

接下來，我們看看如何創建工具。首先，需要在其 *tool* 子目錄中創建工具，如下所示：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

我們看到這裡定義了工具的名稱、描述、使用 Pydantic 定義的輸入模式，以及工具被調用時的處理器。最後，我們暴露了 `tool_add`，它是一個包含所有這些屬性的字典。

此外，還有 *schema.py* 文件，用於定義工具使用的輸入模式：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們還需要填充 *__init__.py* 文件，以確保工具目錄被視為模組。此外，我們需要暴露其中的模組，如下所示：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

隨著添加更多工具，我們可以繼續向此文件添加內容。

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

在這裡，我們創建了一個包含以下屬性的字典：

- name：工具的名稱。
- rawSchema：Zod 模式，用於驗證調用工具的請求。
- inputSchema：此模式將由處理器使用。
- callback：用於調用工具。

此外，還有 `Tool`，用於將此字典轉換為 MCP 伺服器處理器可以接受的類型，代碼如下：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

還有 *schema.ts* 文件，我們在其中存儲每個工具的輸入模式，目前只有一個模式，但隨著工具的增加，我們可以添加更多條目：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，接下來我們處理工具的列出功能。

### -3- 處理工具列出

接下來，要處理工具的列出，我們需要在伺服器文件中設置一個請求處理器。以下是需要添加的內容：

**Python**

```python
# code omitted for brevity
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

在這裡，我們添加了裝飾器 `@server.list_tools` 和實現函數 `handle_list_tools`。在後者中，我們需要生成工具列表。注意，每個工具需要有名稱、描述和輸入模式。

**TypeScript**

要設置列出工具的請求處理器，我們需要在伺服器上調用 `setRequestHandler`，並使用適合我們需求的模式，在此例中為 `ListToolsRequestSchema`。

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
// code omitted for brevity
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: tools
  };
});
```

很好，現在我們已解決列出工具的部分，接下來看看如何調用工具。

### -4- 處理工具調用

要調用工具，我們需要設置另一個請求處理器，專注於處理指定要調用的功能及其參數的請求。

**Python**

我們使用裝飾器 `@server.call_tool` 並用函數 `handle_call_tool` 實現它。在該函數中，我們需要解析工具名稱及其參數，並確保參數對應工具是有效的。我們可以選擇在此函數中或工具的下游進行參數驗證。

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invoke the tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

以下是發生的事情：

- 工具名稱已作為輸入參數 `name` 提供，參數則以 `arguments` 字典的形式提供。

- 工具通過 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 調用。參數的驗證發生在 `handler` 屬性指向的函數中，如果失敗，將拋出異常。

至此，我們已全面了解如何使用低階伺服器列出和調用工具。

查看[完整示例](./code/README.md)。

## 作業

擴展您已獲得的代碼，添加多個工具、資源和提示，並反思您是否注意到只需要在工具目錄中添加文件，而不需要修改其他地方。

*未提供解答*

## 總結

在本章中，我們了解了低階伺服器方法的工作原理，以及如何幫助我們創建一個可持續擴展的良好架構。我們還討論了驗證，並展示了如何使用驗證庫創建輸入驗證模式。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。