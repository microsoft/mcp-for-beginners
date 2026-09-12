# 進階伺服器使用

MCP SDK 中暴露了兩種不同類型的伺服器，你的一般伺服器和低階伺服器。通常，你會使用一般伺服器來新增功能。然而，在某些情況下，你可能會依賴低階伺服器，例如：

- 更好的架構。使用一般伺服器和低階伺服器都可以建立乾淨的架構，但可以說使用低階伺服器稍微比較容易。
- 功能可用性。有些進階功能只能用低階
    伺服器使用。後續章節涵蓋了 Elicitation 和被棄用的 Sampling
    功能，在 MCP `2026-07-28` 中已經不建議使用。

## 一般伺服器與低階伺服器

下面是建立 MCP 伺服器時使用一般伺服器的範例：

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

重點是你明確地加上每一個你希望伺服器具備的工具、資源或提示。這樣做沒有錯。  

### 低階伺服器方法

但當你使用低階伺服器方法時，需要用不同的角度思考。你不是註冊每個工具，而是為每種功能類型（工具、資源或提示）建立兩個處理器。舉例來說，工具只會有兩個函數如下：

- 列出所有工具。一個函數負責所有列出工具的嘗試。
- 處理呼叫所有工具。在這裡也只有一個函數處理工具的呼叫。

聽起來像是較少工作量對吧？所以我不需要註冊工具，只需要確保當我列出所有工具時它會出現在列表中，且當有呼叫工具的請求時它會被呼叫。

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
  // 返回註冊的工具清單
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

這裡我們有一個函數會回傳功能列表。工具清單中的每個項目都有像 `name`、`description` 和 `inputSchema` 這些欄位以符合回傳類型。這允許我們把工具和功能定義放在其他地方。我們可以將所有工具放到 tools 資料夾，功能也是如此，讓你的專案架構看起來像這樣：

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

非常好，我們的架構可以變得相當整潔。

那麼呼叫工具呢？是不是也是同樣的概念，一個處理器負責呼叫任一工具？是的，正是如此，以下是該程式碼：

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
    
    // args: request.params.arguments
    // TODO 呼叫工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

從上面的程式碼可以看到，我們需要解析出要呼叫的工具以及帶入的參數，然後進行工具呼叫。

## 使用驗證改進這種方法

到目前為止，你已經看到如何用這兩個處理器替代所有註冊工具、資源和提示的方式。我們還需要做什麼？我們應該新增某種形式的驗證，以確保工具被正確的參數呼叫。每個執行環境都有自己的方案，例如 Python 使用 Pydantic，TypeScript 使用 Zod。總結想法如下：

- 把建立功能（工具、資源或提示）的邏輯移到專屬資料夾。
- 加入一種方式驗證針對特定呼叫（例如呼叫工具）的請求。

### 創建功能

要創建功能，我們需要建立該功能的檔案，並確保它具有該功能所需的欄位。不同工具、資源和提示的欄位略有不同。

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

    # TODO：新增 Pydantic，以便我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

你可以看到我們做了以下事情：

- 在 *schema.py* 檔案中使用 Pydantic 建立名為 `AddInputModel` 的 schema，帶有欄位 `a` 和 `b`。
- 嘗試將請求解析為 `AddInputModel` 類型，若參數不符則會崩潰：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以選擇將此解析邏輯放在工具呼叫本身或處理器函數中。

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

- 在處理所有工具呼叫的處理器中，我們嘗試將傳入的請求解析成工具定義的 schema：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果解析成功，就繼續呼叫實際工具：

    ```typescript
    const result = await tool.callback(input);
    ```

如你所見，這種方法形成了優良的架構，因為所有東西都有它的位子，*server.ts* 是個非常小的檔案，只負責連接請求處理器，每個功能分別放在自己的資料夾中，例如 tools/、resources/ 或 prompts/。

很好，我們接著嘗試建立這個架構。 

## 練習：建立低階伺服器

在這個練習中，我們將：

1. 建立一個低階伺服器來處理列出工具和呼叫工具。
1. 實作一個你可以持續擴充的架構。
1. 增加驗證以確保工具呼叫被妥善驗證。

### -1- 建立架構

首先我們需要解決的是一個架構，能幫助我們隨著功能增加而擴展，架構如下所示：

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

現在我們已設定好一個架構，確保我們能輕鬆在 tools 資料夾中新增工具。隨意依照此架構新增 resources 和 prompts 子目錄。

### -2- 創建工具

讓我們看看創建工具的作法。首先，它需要建立在其 *tool* 子目錄內，像這樣：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待辦事項：加入 Pydantic，以便我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

這裡展示如何用 Pydantic 定義名稱、描述和輸入 schema，以及一個當此工具被呼叫時會觸發的處理器。最後，我們公開 `tool_add`，它是包含這些屬性的字典。

還有 *schema.py* 用來定義工具使用的輸入 schema：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們還需要填充 *__init__.py* 以確保 tools 目錄被視為模組。此外，我們需要將其中的模組公開，如下所示：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

隨著工具增加，我們可以繼續新增至這個檔案。

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

這裡我們建立一個包含屬性的字典：

- name，工具的名稱。
- rawSchema，Zod schema，用來驗證呼叫此工具的請求。
- inputSchema，此 schema 會由處理器使用。
- callback，用來執行該工具。

還有 `Tool` 用來將此字典轉成 mcp server 處理器可接受的類型，長這樣：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

另外有 *schema.ts*，我們把每個工具的輸入 schema 存放在這裡，當前只有一個 schema，但隨著工具增加，我們還能新增更多條目：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，接下來我們處理工具列表的功能。

### -3- 處理工具列表

接著，要處理列出工具，我們需要為這設定一個請求處理器。以下是在我們的伺服器檔案中需加入的內容：

**Python**

```python
# 代碼已為簡潔而省略
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

這裡，我們新增了裝飾器 `@server.list_tools` 和實現函數 `handle_list_tools`。後者需要產生一個工具清單。注意每個工具需有名稱、描述與 inputSchema。   

**TypeScript**

要設定列出工具的請求處理器，需在伺服器呼叫 `setRequestHandler`，並傳入符合我們需求的 schema，此例是 `ListToolsRequestSchema`。 

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
// 程式碼為簡潔起見而省略
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 返回已註冊工具的列表
  return {
    tools: tools
  };
});
```

很好，現在我們已解決工具列表的部份，接著看看如何呼叫工具。

### -4- 處理呼叫工具

要呼叫工具，我們需要設定另一個請求處理器，這次是處理指定呼叫哪個功能以及帶哪些參數的請求。

**Python**

使用裝飾器 `@server.call_tool`，並用 `handle_call_tool` 函數實作。在該函數裡，我們需解析工具名稱、參數並確保參數對應的工具有效。我們可以在此函數內或實際工具內驗證參數。

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

以下為流程：

- 我們的工具名稱已經存在於輸入參數 `name` 中，參數則在 `arguments` 字典中。

- 工具被呼叫時：`result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`。參數驗證發生於 `handler` 屬性指向的函數中，若失敗會引發異常。

就這樣，我們對使用低階伺服器列出和呼叫工具有完整的了解。

請看 [完整範例](./code/README.md)

## 作業

在你準備的範例中新增多個工具、資源和提示，並思考你會發現你只需在 tools 資料夾添加檔案，其他地方都不用更動。 

<em>未提供解答</em>

## 總結

本章節說明了低階伺服器方法的運作原理，以及如何幫助我們建立一個持續可擴充的漂亮架構。我們也討論了驗證並示範如何使用驗證函式庫建立輸入驗證 schema。

## 接下來

- 下一章：[簡易身份驗證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->