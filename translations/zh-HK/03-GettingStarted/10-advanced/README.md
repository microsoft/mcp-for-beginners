# 進階伺服器使用

在 MCP SDK 中有兩種不同類型的伺服器，分別是一般伺服器和低階伺服器。通常，您會使用一般伺服器來新增功能。但在某些情況下，您會想要依賴低階伺服器，例如：

- 更好的架構。可以用一般伺服器和低階伺服器都可以創建乾淨的架構，但可以說使用低階伺服器會稍微簡單一點。
- 功能可用性。一些進階功能只能與
    低階伺服器一起使用。後面的章節會介紹 Elicitation 和舊版 Sampling
    功能，該功能在 MCP `2026-07-28` 中已棄用。

## 一般伺服器與低階伺服器

這是使用一般伺服器創建 MCP 伺服器的方式

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

這裡的重點是您需要明確加入每個想要伺服器擁有的工具、資源或提示。這沒有錯誤。  

### 低階伺服器方法

不過，使用低階伺服器方法時，您需要以不同角度思考。您不會註冊每個工具，而是針對每種類型的功能（工具、資源或提示）建立兩個處理器。舉例來說，工具只會有兩個函式，像這樣：

- 列出所有工具。一個函式負責所有工具列舉的嘗試。
- 處理呼叫所有工具。這裡也是，一個函式負責處理對工具的呼叫

這聽起來好像工作量比較少，是不是？所以不需要註冊工具，只需確保在列出所有工具時列出該工具，並在收到呼叫工具的請求時呼叫它。

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

這裡我們有一個回傳功能清單的函式。工具清單中的每個項目現在都有 `name`、`description` 和 `inputSchema` 等欄位，以符合回傳類型。這讓我們能將工具和功能定義放到其他地方。我們現在可以在 tools 資料夾裡建立所有工具，其他功能也是同理，讓您的專案突然變得這麼有組織：

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

這很棒，我們的架構可以看起來非常乾淨。

那呼叫工具呢？也是同樣概念嗎？只有一個處理器去呼叫工具，不論是哪個工具？對，完全正確，這是代碼：

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
    // 待辦 呼叫工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

從上述程式碼可見，我們需要解析出要呼叫的工具及其參數，接著進行工具的呼叫。

## 用驗證改進方法

到目前為止，您已看到如何用每種類型兩個處理器取代註冊所有工具、資源和提示。我們還需要做什麼？我們應該加上某種驗證機制，確保工具的呼叫附帶正確的參數。各環境有自己的解決方案，例如 Python 使用 Pydantic，TypeScript 使用 Zod。概念是：

- 將建立功能（工具、資源或提示）的邏輯移到專屬資料夾。
- 加入驗證進入請求的機制，確保工具呼叫的正確性。

### 建立功能

建立功能時，需要為該功能建立檔案，確保包含該功能所需的欄位。這些欄位在工具、資源和提示之間略有不同。

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

    # TODO: 加入 Pydantic，讓我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

您可以看到以下作法：

- 在 *schema.py* 中用 Pydantic 建立 `AddInputModel` 架構，含欄位 `a` 和 `b`。
- 試圖將進入請求解析為 `AddInputModel` 類型，如果參數不符合將產生錯誤：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

您可選擇將此解析邏輯放在工具呼叫本身或是處理函式中。

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

// 結構.ts
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

- 在負責所有工具呼叫的處理器中，嘗試將進入請求解析成工具定義的 schema：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果解析成功，就進一步呼叫實際的工具：

    ```typescript
    const result = await tool.callback(input);
    ```

如您所見，這種方法創造了很棒的架構，一切都有其位置，*server.ts* 是個非常小的檔案，僅負責串接請求處理器，每項功能則在各自資料夾中：tools/、resources/ 或 /prompts。

很好，接著讓我們來建立這個。

## 練習：建立低階伺服器

在這項練習中，我們將做以下幾件事：

1. 建立一個低階伺服器，處理工具清單及工具呼叫。
1. 實作可延展的架構。
1. 加入驗證以確保工具呼叫能被正確驗證。

### -1- 建立架構

我們首先要建立的是一個能隨著功能增加而擴展的架構，看起來像這樣：

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

現在我們設置了一個架構，確保可以輕鬆地在 tools 資料夾新增新工具。資源和提示也可用子目錄分類。

### -2- 建立工具

接著我們看看建立工具長什麼樣子。首先，工具必須在 *tool* 子目錄建立，像這樣：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待辦事項：新增 Pydantic，以便我們能建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

可見我們如何用 Pydantic 定義 name、description 和輸入 schema，還有一個在呼叫工具時會被呼叫的處理函式。最後，我們公開 `tool_add`，這是一個包含所有屬性的字典。

此外還有 *schema.py* 用來定義工具所用的輸入 schema：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我們也需要填寫 *__init__.py*，確保 tools 目錄被視為模組，還要像這樣公開模組裡的內容：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

我們可以隨著工具增加繼續加內容到這個檔案。

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

這裡創建了一個屬性字典：

- name，工具名稱。
- rawSchema，Zod schema 用來驗證呼叫工具的進入請求。
- inputSchema，這個 schema 由處理器使用。
- callback，用來呼叫工具的函式。

還有一個 `Tool` 用來將這字典轉成 mcp 伺服器處理器可以接受的型別，看起來像這樣：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* 是用來存放每個工具輸入 schema 的，目前只有一個 schema，但未來可加入更多：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

好的，接著來處理工具清單的部分。

### -3- 處理工具清單

接著，要處理工具清單，我們要設置一個相應的請求處理器。這是我們要加在伺服器檔案的程式：

**Python**

```python
# 為簡潔起見，省略代碼
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

在此，我們加上 `@server.list_tools` 裝飾器及實作函式 `handle_list_tools`。在此函式中，要產生工具清單。注意每個工具都必須擁有 name、description 和 inputSchema。   

**TypeScript**

要設置列舉工具的請求處理器，需要在伺服器上呼叫 `setRequestHandler`，並用符合我們需求的 schema，例如 `ListToolsRequestSchema`。

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
// 代碼省略以簡潔表示
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 回傳已註冊工具的列表
  return {
    tools: tools
  };
});
```

很好，現已解決工具列舉部分，接下來看看呼叫工具如何實作。

### -4- 處理呼叫工具

呼叫工具時，我們要設置另一個請求處理器，專責處理指定呼叫哪個功能及帶什麼參數的請求。

**Python**

使用裝飾器 `@server.call_tool`，用函式 `handle_call_tool` 實作。在該函式中，我們需解析工具名稱、參數，並確保參數對該工具有效。參數驗證可在此函式中或後續工具本身中完成。

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
        # 調用工具
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

運作流程如下：

- 工具名稱已存在於輸入參數 `name`，而我們的參數在 `arguments` 字典中。

- 工具被呼叫形式為 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`。參數驗證發生在 `handler` 屬性指向的函式中，若失敗將拋出例外。

現在，我們完整理解了使用低階伺服器列舉和呼叫工具的流程。

參見此處的 [完整示範](./code/README.md)

## 指派作業

擴充您所獲得的程式碼，新增多個工具、資源和提示，並觀察您會發現只需在 tools 目錄新增檔案，其他地方不需更動。

<em>未提供解答</em>

## 總結

本章介紹了低階伺服器方法的運作方式，以及如何幫助我們建立可繼續擴充的良好架構。我們也討論了驗證，示範如何使用驗證函式庫創建輸入的驗證 schema。

## 接下來

- 下一課： [簡易認證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->