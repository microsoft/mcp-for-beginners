# 進階伺服器使用

MCP SDK 中有兩種不同類型的伺服器，分別是一般伺服器和低階伺服器。通常，你會使用一般伺服器來新增功能，但在某些場合，你可能會想依賴低階伺服器，例如：

- 更好的架構。使用一般伺服器和低階伺服器都能建立乾淨的架構，但可以說使用低階伺服器會稍微更簡單。
- 功能可用性。某些進階功能只能在低階伺服器中使用。
    後面章節會介紹 Elicitation 以及已在 MCP `2026-07-28` 中棄用的舊版 Sampling 功能。


## 一般伺服器 vs 低階伺服器

以下是用一般伺服器建立 MCP 伺服器的範例

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

重點是你需要明確地加入伺服器要擁有的每個工具、資源或提示。這樣做沒有問題。  

### 低階伺服器方法

不過，使用低階伺服器時需要以不同的方式思考。你不是註冊每個工具，而是為每種類型的功能（工具、資源或提示）建立兩個處理器。舉例來說，工具只有兩個函數如下：

- 列出所有工具。這個函數負責所有嘗試列出工具的呼叫。
- 處理所有呼叫工具的行為。這裡也只有一個函數負責處理呼叫工具。

這聽起來可能工作量比較少，對吧？所以不用註冊每個工具，只要確保工具在列出所有工具時被列出，並在收到呼叫該工具請求時被呼叫即可。

讓我們看看現在的程式碼長什麼樣：

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

這裡我們有一個返回功能清單的函數。tools 清單中的每個條目現在都有 `name`、`description` 和 `inputSchema` 等欄位，符合回傳類型。這讓我們可以將工具和功能定義放在別處。我們現在可以將所有工具放在 tools 資料夾裡，其他功能亦同，讓專案結構變成：

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

這很棒，我們的架構可以變得相當乾淨。

那呼叫工具呢，是不是也是一個處理器呼叫任意工具？是的，完全正確，這是相應的程式碼：

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

從上方程式碼可見，我們需要解析要呼叫的工具以及帶入的參數，再進行呼叫。

## 用驗證提升方案

到目前為止，你已看到用兩個處理器替代所有註冊工具、資源與提示的方式。接著我們還需要做什麼？我們應該加上驗證機制來確保工具呼叫時帶入正確參數。不同語言也有各自解決方案，例如 Python 用 Pydantic，TypeScript 用 Zod。想法如下：

- 將建立功能（工具、資源或提示）的邏輯移至其專屬資料夾。
- 新增驗證進來的請求（例如呼叫工具）的機制。

### 建立功能

建立功能時，我們要為該功能建立一個檔案，並確保該功能必填欄位存在。不同類型（工具、資源、提示）在欄位上會稍有差異。

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

這裡你可以看到我們如何做到：

- 在 *schema.py* 中用 Pydantic 建立帶有欄位 `a` 和 `b` 的 `AddInputModel` schema。
- 嘗試將進來的請求解析為 `AddInputModel` 型別，參數不符時將會崩潰：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以選擇把解析邏輯放在工具呼叫中或處理器函數中。

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

- 在處理所有工具呼叫的處理器中嘗試將請求解析為工具定義的 schema：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果成功則繼續呼叫真正的工具：

    ```typescript
    const result = await tool.callback(input);
    ```

如你所見，這方法創造了一個很好的架構，`server.ts` 是一個很小的檔案，負責串接請求處理器，而每個功能均在各自資料夾中，如 tools/、resources/ 或 prompts/。

很棒，讓我們繼續來實作。

## 練習：建立低階伺服器

在這個練習中，我們會進行以下操作：

1. 建立一個低階伺服器，處理列出工具與呼叫工具。
1. 實作一個易於擴充的架構。
1. 加入驗證以確保工具呼叫的正確性。

### -1- 建立架構

首先我們要處理的是一個讓新增功能時能輕鬆擴展的架構，如下：

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

現在我們已設定能輕鬆在 tools 資料夾新增工具的架構。你也可以依此為 resources 和 prompts 建立子目錄。

### -2- 建立工具

接下來看看建立工具的方式。工具需要建立在自己的 *tool* 子目錄中，如下：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待辦事項：加入 Pydantic，以便我們可以建立 AddInputModel 並驗證引數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

我們看到如何用 Pydantic 定義名稱、描述、輸入模式，還有當工具被呼叫時會被觸發的處理器。最後，我們公開 `tool_add`，它是包含這些屬性的字典。

同時還有 *schema.py*，用來定義工具的輸入模式：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們還要填寫 *__init__.py*，確保 tools 目錄被視為模組，並且匯出裡面的模組，如下：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

我們可隨著新增更多工具持續擴充此檔案。

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

這裡我們建立一個字典，內容包含：

- name，工具名稱。
- rawSchema，Zod schema，用以驗證呼叫此工具的請求。
- inputSchema，處理器用的 schema。
- callback，用來呼叫工具。

還有 `Tool` 用來將此字典轉成 MCP 伺服器處理器可以接受的類型，如下：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

另外，有 *schema.ts* 放置所有工具的輸入 schema，目前只含一個，但隨著工具增加可擴充更多：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

好的，接著處理列出工具的部分。

### -3- 處理工具列出

接著，為了列出工具，我們需要設置一個請求處理器。以下是要加入伺服器檔案的程式：

**Python**

```python
# 代碼為簡潔起見已省略
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

這裡，我們加上 `@server.list_tools` 裝飾器和實作函數 `handle_list_tools`。在函數中要產生工具清單。每個工具需含名稱、描述及 inputSchema。   

**TypeScript**

設置列出工具的請求處理器，我們在伺服器上呼叫 `setRequestHandler`，並使用符合此用途的 schema，例如 `ListToolsRequestSchema`。

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
// 代碼省略以節省篇幅
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 返回已註冊工具的列表
  return {
    tools: tools
  };
});
```

好了，現在我們解決了列出工具的問題，接著看如何呼叫工具。

### -4- 處理呼叫工具

為了呼叫工具，我們需要建立另一個請求處理器，這次專注於處理指定呼叫哪個功能與傳入哪些參數的請求。

**Python**

我們使用 `@server.call_tool` 裝飾器實作一個函數，如 `handle_call_tool`。在此函數中，我們要解析工具名稱、參數，並確保參數有效。驗證可在此函數或實際工具中進行。

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

- 工具名稱已經作為輸入參數 `name`，參數則以 `arguments` 字典形式提供。

- 呼叫工具使用 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`。參數驗證在 `handler` 函數中進行，如有錯誤會引發例外。

這樣，我們就完整理解了如何用低階伺服器列出與呼叫工具。

請參考 [完整範例](./code/README.md)

## 作業

請用你手上的程式碼添加一些工具、資源和提示，並思考你會發現只需在 tools 目錄裡增加檔案，而不需在其他地方添加。

<em>本章無提供解答</em>

## 總結

本章介紹了低階伺服器方法如何運作，以及如何幫助我們建立乾淨且可擴充的架構。我們也討論了驗證，並示範如何使用驗證庫來建立輸入的 schema。

## 下一步

- 下一章：[簡單驗證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->