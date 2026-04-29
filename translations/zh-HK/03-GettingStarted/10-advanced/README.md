# 進階伺服器使用

MCP SDK 中有兩種不同類型的伺服器可供使用，分別是普通伺服器與低階伺服器。通常你會使用普通伺服器來新增功能，但有些情況下，你會想依賴低階伺服器，例如：

- 更好的架構。利用普通伺服器與低階伺服器都可以建立乾淨的架構，但可以說使用低階伺服器會稍微簡單一點。
- 功能可用性。某些進階功能只能在低階伺服器中使用。後面章節中會看到這點，當我們加入抽樣（sampling）和引導（elicitation）時。

## 普通伺服器 vs 低階伺服器

以下是用普通伺服器建立 MCP 伺服器的範例：

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

重點是你需要明確新增你希望伺服器擁有的每個工具、資源或提示。這樣做沒有錯。

### 低階伺服器方法

不過使用低階伺服器方法時，你需要用不同的思維方式。你不需要註冊每個工具，而是針對每種功能類型（工具、資源或提示）建立兩個處理器。例如對於工具，只有兩個函式：

- 列出所有工具。用一個函式負責處理所有列出工具的嘗試。
- 處理工具呼叫。這裡也是，只用一個函式處理所有對工具的呼叫。

聽起來工作量可能比較少，對吧？所以不用註冊工具，只要確保工具會出現在列出工具的清單中，並且在有呼叫該工具的請求時會被呼叫即可。

讓我們來看看現在程式碼長什麼樣：

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

這裡我們有一個函式回傳功能清單，工具清單中的每一項都有 `name`、`description` 和 `inputSchema` 等欄位以符合回傳類型。這讓我們可以將工具跟功能定義放在其他地方。我們現在可以於 tools 資料夾建立所有工具，其他功能也是如此，讓專案組織突然變成這樣：

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

這太棒了，我們的架構能看起來非常乾淨。

那麼呼叫工具呢？也是同樣的概念嗎？用一個處理器呼叫任一工具？是的，沒錯，以下是程式碼：

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

從上述程式碼可以看出來，我們需要解析出要呼叫的工具以及帶入的參數，接著才進行工具呼叫。

## 用驗證改進做法

到目前為止，你看到你要新增工具、資源、提示的註冊都可以用每個功能類型兩個處理器取代。我們還要做什麼？我們應該加上某種驗證以確保呼叫工具時帶入的參數是正確的。每個執行時環境有各自解決方案，例如 Python 用 Pydantic，TypeScript 用 Zod。想法是這樣：

- 把建立功能（工具、資源或提示）的邏輯搬到它專屬的資料夾。
- 新增驗證方法用來驗證例如呼叫工具的請求。

### 建立功能

建立功能時，我們需要為該功能建立檔案，並確保它有該功能所要求的必要欄位。這些欄位在工具、資源和提示間會略有不同。

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

    # TODO: 加入 Pydantic，咁我哋可以建立 AddInputModel 同驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

這裡你可以看到我們做了以下動作：

- 使用 Pydantic 在 *schema.py* 中建立 `AddInputModel` 架構，欄位有 `a` 和 `b`。
- 嘗試將進來的請求解析成 `AddInputModel` 類型，若參數不符會造成程式崩潰：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以選擇將解析邏輯放在工具本身的呼叫中或放在處理器函式中。

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

       // 忽略 TypeScript 檢查
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

- 在處理所有工具呼叫的函式中，我們嘗試把進來的請求解析成該工具定義的架構：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    若成功解析，我們就進行真正的工具呼叫：

    ```typescript
    const result = await tool.callback(input);
    ```

你可以看到這種方式打造出很棒的架構，所有東西都有自己的位置，*server.ts* 是個很小的檔案，只負責串接請求處理器，而每個功能則放在各自資料夾，例如 tools/、resources/ 或 prompts/。

太好了，我們接下來嘗試打造這個。

## 練習：建立低階伺服器

在這個練習中，我們會做到：

1. 建立能處理工具清單與工具呼叫的低階伺服器。
2. 實現一個可擴展的架構。
3. 加入驗證以確保工具呼叫被正確驗證。

### -1- 建立架構

我們首要解決的是建立可隨著功能增加而輕鬆擴展的架構，長得像這樣：

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

現在我們建立了能輕鬆在 tools 資料夾加入新工具的架構。你也可以按這原則為 resources 和 prompts 分別建立子目錄。

### -2- 建立工具

接著看看建立工具長怎樣。首先，它必須建立在 *tool* 子目錄裡，如下：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待辦：加入 Pydantic，以便我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

這裡展示我們如何定義 name、description 和使用 Pydantic 的輸入架構，以及一個會在呼叫此工具時執行的處理器。最後，我們暴露 `tool_add`，它是一個字典，包含這些屬性。

還有 *schema.py* 用來定義工具的輸入架構：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們也要填寫 *__init__.py* 來將 tools 目錄視為模組，並且將模組內部內容暴露出來，如下：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

隨著加入更多工具，我們可以持續向此檔案添加。

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

這裡我們建立一個字典，包含如下屬性：

- name，代表工具的名稱。
- rawSchema，Zod 架構，用以驗證呼叫該工具的請求是否正確。
- inputSchema，處理器將會使用這個架構。
- callback，用來呼叫該工具。

還有 `Tool` 用來將字典轉成 mcp 伺服器處理器可以接受的類型，如下：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

而 *schema.ts* 則用以存放每個工具的輸入架構，目前只有一個架構，隨著加入工具會新增更多：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

太棒了，接下來處理工具列出功能。

### -3- 處理工具列表

接著要處理列出所有工具，為此我們要為伺服器設定請求處理器，這是要對伺服器檔案加入的內容：

**Python**

```python
# 為簡潔起見省略了代碼
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

這裡加上 `@server.list_tools` 裝飾器，並實作函式 `handle_list_tools`。裡面需產生工具列表。注意每個工具都需有 name、description 和 inputSchema。

**TypeScript**

建立工具列表請求處理器時，我們對伺服器呼叫 `setRequestHandler` 並指定適合的架構，這裡是 `ListToolsRequestSchema`。

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

太好了，現在我們完成了列出工具，接著看看如何呼叫工具。

### -4- 處理呼叫工具

要呼叫工具，我們必須建立另一個請求處理器，這回是處理指明要呼叫哪個功能以及帶哪些參數的請求。

**Python**

使用 `@server.call_tool` 裝飾器並實作像 `handle_call_tool` 的函式。該函式裡我們解析工具名稱、參數，並確保傳入的參數符合工具需求。可在此函式或實際工具內驗證參數。

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

- 工具名稱已作為輸入參數 `name`，而參數在 `arguments` 字典中。
- 使用 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 來呼叫工具。引數驗證在指向函式的 `handler` 屬性中進行，若違反則會拋例外。

以上，我們完整理解透過低階伺服器列出與呼叫工具的流程。

參考[完整範例](./code/README.md)

## 作業

將你拿到的程式碼擴充，加入多個工具、資源以及提示，並觀察你只需在 tools 資料夾中加入檔案，而不必更動其他地方。

<em>無解答提供</em>

## 小結

本章節介紹低階伺服器作法，解說其如何幫助建立良好架構並持續可擴充。另外討論了驗證，並示範如何用驗證函式庫建立輸入驗證的架構。

## 接下來

- 下一章節：[簡易認證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人類翻譯。對於因使用本翻譯而引起的任何誤解或錯誤詮釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->