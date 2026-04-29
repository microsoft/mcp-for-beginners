# 高级服务器使用

MCP SDK 中暴露了两种不同类型的服务器，分别是普通服务器和低级服务器。通常情况下，你会使用普通服务器来添加功能。不过在某些情况下，你可能想依赖低级服务器，比如：

- 更好的架构。虽然用普通服务器和低级服务器都可以创建清晰的架构，但有人认为低级服务器会稍微容易一些。
- 功能可用性。有些高级功能只能通过低级服务器来使用。你将在后面的章节中看到，比如添加采样和引导。

## 普通服务器与低级服务器

下面是用普通服务器创建 MCP 服务器的示例

**Python**

```python
mcp = FastMCP("Demo")

# 添加一个加法工具
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

// 添加一个加法工具
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

重点是你明确添加了每个工具、资源或提示，告诉服务器它应该具备哪些功能。这种做法没有问题。

### 低级服务器方法

然而，当你使用低级服务器方法时，需要用不同的思路来看待。不是注册每一个工具，而是针对每种功能类型（工具、资源或提示）创建两个处理函数。例如工具只有两个函数：

- 列出所有工具。一个函数负责所有列出工具的请求。
- 处理调用所有工具。这也是一个函数，负责所有对工具的调用。

听上去工作量可能更少吧？所以不需要注册工具，只需保证列表函数能正确列出该工具，同时调用函数能处理请求调用此工具。

来看下代码现在的样子：

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
  // 返回已注册工具的列表
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

这里我们有一个函数返回特征列表。工具列表中的每一项都有如 `name`、`description` 和 `inputSchema` 等字段，以符合返回类型。这使我们可以把工具和特征定义放在别处。我们可以把所有工具放到 tools 文件夹，同理为其他特征建立对应文件夹，你的项目架构可以变成这样：

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

这很好，我们的架构可以非常清晰。

那调用工具也是类似思路吗？一个处理函数来调用任何工具？是的，示例如下：

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools 是一个以工具名称为键的字典
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
    
    // 参数：request.params.arguments
    // 待办 调用工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

如上代码，我们需要解析调用的是哪个工具，用什么参数，然后进行调用。

## 通过验证改进方案

到目前为止，已经看到所有添加工具、资源、提示的注册可以被每种功能类型的两个处理函数替代。还需要做什么？我们应当添加某种验证来确保调用工具时参数正确。每种运行时有自己的方式，比如 Python 用 Pydantic，TypeScript 用 Zod。做法是：

- 把创建特征（工具、资源或提示）的逻辑放到其专属文件夹。
- 添加验证来确认传入请求调用工具时参数格式正确。

### 创建特征

创建特征时，需要为该特征创建一个文件，并确保具备该特征必须的字段。不同类型的工具、资源和提示需要的字段有所不同。

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
        # 使用 Pydantic 模型验证输入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待办：添加 Pydantic，以便我们可以创建 AddInputModel 并验证参数

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

这里可以看到我们做了以下事情：

- 用 Pydantic 在 *schema.py* 中创建名为 `AddInputModel` 的模式，包含字段 `a` 和 `b`。
- 尝试把传入请求解析成 `AddInputModel` 类型，如果参数不匹配，将会抛出异常：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型验证输入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以选择把解析逻辑放在工具调用本身，或者放在处理函数中。

**TypeScript**

```typescript
// 服务器.ts
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

// 模式.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// 添加.ts
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

- 在处理所有工具调用的处理函数中，试图将传入请求解析为工具定义的模式：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果成功解析，则调用对应工具：

    ```typescript
    const result = await tool.callback(input);
    ```

正如你所见，这种方式架构优良，每样东西有它的位置，*server.ts* 非常简洁，仅负责连接请求处理器，而每个特征都放在它们各自的文件夹 tools/、resources/ 或 prompts/ 中。

很好，我们继续动手试试。

## 练习：创建低级服务器

本练习中，我们将完成：

1. 创建低级服务器，处理工具列表与工具调用。
1. 实现一个可扩展的架构。
1. 添加验证以确保工具调用参数正确。

### -1- 创建架构

首先搭建一个有利于扩展的新架构，如下所示：

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

现在我们搭建了一个架构，轻松添加新工具到 tools 文件夹。你也可以类似方式为 resources 和 prompts 建立子目录。

### -2- 创建工具

来看下创建工具的示例。先在 *tool* 子目录下创建：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型验证输入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待办事项：添加 Pydantic，以便我们可以创建 AddInputModel 并验证参数

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

这里展示了如何定义名字、描述和输入模式（使用 Pydantic），以及一个当该工具被调用时执行的处理函数。最后导出 `tool_add` 字典，它包含所有这些属性。

还有 *schema.py*，定义工具输入模式：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

还要填充 *__init__.py*，确保 tools 目录被视为模块。同时导出该目录内的模块，如下：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

随着工具增多，可以不断向此文件添加。

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

这里我们创建了一个字典，包含属性：

- name，工具名称。
- rawSchema，Zod 模式，用于验证调用请求。
- inputSchema，处理函数使用的模式。
- callback，调用工具的函数。

还有 `Tool`，将该字典转换为 MCP 服务器处理器可接受的类型，如下：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

另外有 *schema.ts*，存储各工具的输入模式，目前只有一个模式，后续添加工具时可增加更多条目：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，接下来处理工具列表请求。

### -3- 处理工具列表

要处理列出工具请求，需要在服务器文件中设置请求处理函数：

**Python**

```python
# 代码省略以简洁表示
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

为此添加装饰器 `@server.list_tools` 以及处理函数 `handle_list_tools`。该函数返回工具列表。注意每个工具都必须有 name、description 和 inputSchema。

**TypeScript**

要设置工具列表请求处理，用 `setRequestHandler`，传入满足需求的模式，这里是 `ListToolsRequestSchema`。

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
// 代码省略以简洁起见
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 返回已注册工具的列表
  return {
    tools: tools
  };
});
```

很好，工具列表部分已经解决，接下来看看如何调用工具。

### -4- 处理调用工具

调用工具时，设置另一个请求处理函数，接收请求，说明调用哪个功能以及参数。

**Python**

这次使用装饰器 `@server.call_tool`，用函数 `handle_call_tool` 实现。该函数解析工具名和参数，确认参数有效。参数校验可以在函数中做，也可以放在实际工具里做。

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools 是一个以工具名称为键的字典
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # 调用该工具
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

要点如下：

- 工具名来自输入参数 `name`，参数来自 `arguments` 字典。
- 调用工具：`result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`。参数校验在 `handler` 函数里，失败会抛异常。

到这，你已经全面了解了如何使用低级服务器实现工具列表和调用。

完整示例见[此处](./code/README.md)

## 练习任务

为已有代码添加多个工具、资源、提示，然后体会你只需在 tools 目录添加文件，而无需其他地方改动。

<em>无提供答案</em>

## 总结

本章展示了低级服务器的工作原理以及如何构建良好的架构。还讨论了验证机制，并演示了如何使用验证库创建输入验证模式。

## 接下来

- 下章： [简单认证](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力保证准确性，但请注意自动翻译可能包含错误或不准确之处。原始文档的本地语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对于因使用此翻译而产生的任何误解或曲解概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->