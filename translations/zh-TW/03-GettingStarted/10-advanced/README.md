# 進階伺服器使用方式

MCP SDK 中提供了兩種不同類型的伺服器：一般伺服器與低階伺服器。通常你會使用一般伺服器來新增功能，但在某些情況下你可能想要依賴低階伺服器，例如：

- 更佳的架構。雖然可以用一般伺服器搭配低階伺服器來建立乾淨的架構，但可以說使用低階伺服器會稍微容易一些。
- 功能可用性。有些進階功能只能用低階伺服器來使用。在後續章節中我們將加入抽樣與引導時會看到這點。

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

重點是你必須明確地加上你希望伺服器擁有的每個工具、資源或提示。這樣做沒有錯。

### 低階伺服器做法

然而，當你使用低階伺服器方式時，你需要用不同的思維來看待它。不是註冊每個工具，而是每個功能類型（工具、資源或提示）建立兩個處理程序。例如工具就只有兩個函式：

- 列出所有工具。一個函式會負責處理所有列出工具的嘗試。
- 處理調用所有工具。此處也只有一個函式處理工具調用請求。

聽起來工作量可能比較少對吧？所以我不必註冊工具，只要確保列出所有工具時該工具會被列出，且當有工具調用請求時會被呼叫即可。

我們來看看現在程式碼長什麼樣子：

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
  // 返回註冊工具的列表
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

這裡我們有一個回傳功能列表的函式。工具列表中的每筆都包含 `name`、`description` 和 `inputSchema` 等欄位以符合回傳類型。這使我們能將工具與功能定義放置在其他地方。我們現在可以在 tools 資料夾創建所有工具，其他功能也同理，你的專案就能組織成這樣：

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

很棒，我們架構可以做到相當乾淨。

呼叫工具呢？也是同樣想法，一個處理程序呼叫任一工具？沒錯，以下為程式碼：

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
    // 待辦事項 呼叫該工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

如上面程式碼所示，我們需要解析出要呼叫的工具以及參數，接著才進行調用。

## 以驗證改進此做法

目前為止，你已看到如何替代註冊所有工具、資源與提示的方式以兩個處理程序處理每種類型功能。接著還需要做什麼？我們應該加上一種驗證機制確保工具被呼叫時使用正確參數。每個執行環境都有自己的解決方案，例如 Python 使用 Pydantic，TypeScript 使用 Zod。想法是：

- 把建立功能（工具、資源或提示）的邏輯移到專屬資料夾。
- 增加方式驗證如呼叫工具時的請求。

### 創建功能

要創建功能，我們需要為它建立檔案，並確保擁有該功能必須的欄位。工具、資源、提示的欄位略有差異。

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

    # 待辦事項：新增 Pydantic，這樣我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

你可以看到我們做了以下幾件事：

- 使用 Pydantic 在 *schema.py* 中建立名為 `AddInputModel` 的 schema，包含欄位 `a` 與 `b`。
- 嘗試解析進來的請求為 `AddInputModel` 類型，若參數不符合會導致程式崩潰：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以自行決定是把解析邏輯放在工具調用本身或處理程序函式。

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

       // 忽略 TypeScript 錯誤
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

- 在處理所有工具調用的 handler 裡，我們嘗試將來的請求解析為工具所定義的 schema：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    若成功再繼續呼叫實際工具：

    ```typescript
    const result = await tool.callback(input);
    ```

如你所見，這種做法產生出很棒的架構，所有東西都各司其職，*server.ts* 是個很小的檔案只負責設定請求處理程序，每個功能放在其對應的資料夾，例如 tools/、resources/ 或 prompts/。

很好，讓我們接著嘗試建立這個。

## 練習：建立低階伺服器

在此練習中，我們會做：

1. 建立低階伺服器，處理工具列表與工具調用。
1. 實作一個可以持續擴充的架構。
1. 加入驗證確保工具調用被適當驗證。

### -1- 建立架構

首先要先建立方便隨著功能成長擴充的架構，長這樣：

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

現在我們設立一個架構，確保能輕鬆在 tools 資料夾中新增工具。也可以依照這邏輯新增資源與提示的子目錄。

### -2- 建立工具

接著看看建立工具的樣子。首先，工具須建立於其 *tool* 子目錄：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型驗證輸入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待辦事項：新增 Pydantic，以便我們可以建立 AddInputModel 並驗證參數

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

這裡示範如何用 Pydantic 定義名稱、描述、輸入 schema，還有一個在工具被呼叫時會執行的處理程序。最後我們將這些屬性打包成字典 `tool_add`。

另有 *schema.py* 定義工具使用的輸入 schema：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

同時我們須填入 *__init__.py* 以確保 tools 資料夾成為模組，並將裡面模組公開出來：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

隨著工具越來越多，我們可以不斷擴增此檔案。

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

這裡創建一個字典包含屬性：

- name: 工具名稱
- rawSchema: Zod schema，用來驗證呼叫此工具的請求
- inputSchema: handler 使用的 schema
- callback: 呼叫此工具的函式

還有 `Tool` 用來將此字典轉成 mcp server handler 可接受的型別，看起來像這樣：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

在 *schema.ts* 中存放各工具的輸入 schemas，目前只一個但未來會持續新增：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，接著處理工具列表。

### -3- 處理工具列表

要處理列出工具，我們需要在伺服器檔中設定一個請求處理程序：

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

這裡我們新增裝飾器 `@server.list_tools` 並實作函式 `handle_list_tools`，裡面要回傳工具列表。要注意每個工具都須有 name、description 和 inputSchema。

**TypeScript**

要設定列出工具的請求處理程序，我們在伺服器上呼叫 `setRequestHandler` 並帶入我們想執行的 schema，這裡是 `ListToolsRequestSchema`。

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
  // 回傳已註冊工具的清單
  return {
    tools: tools
  };
});
```

很好，工具列表搞定後，接著看看如何呼叫工具。

### -4- 處理呼叫工具

呼叫工具需要設定另一個請求處理程序，專門處理指定呼叫哪個功能及帶入參數的請求。

**Python**

使用裝飾器 `@server.call_tool` 並實作函式 `handle_call_tool`。此函式將解析工具名稱、參數並確保符合該工具所需參數。參數驗證可在此函式驗證，或此後實際工具中驗證。

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

- 工具名稱已存在於輸入參數 `name`，真正參數則在 `arguments` 字典中。
- 工具透過 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 被呼叫，參數的驗證發生在 `handler` 指向的函式中，若有錯誤會拋出異常。

現在你已完整了解如何用低階伺服器列出與呼叫工具。

完整範例請見 [full example](./code/README.md)

## 作業

擴充給你的程式碼，新增多個工具、資源和提示，並體會你只需要在 tools 目錄新增檔案，其他地方不必修改。

<em>沒有提供解答</em>

## 總結

本章節介紹低階伺服器的運作方式以及如何用它建立良好的架構。我們也討論了驗證並示範如何用驗證函式庫建立輸入驗證規則。

## 下一步

- 下一章：[簡易認證](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的本地語言版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或曲解負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->