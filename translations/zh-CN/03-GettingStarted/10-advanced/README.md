# 高级服务器使用

MCP SDK 中暴露了两种不同类型的服务器，普通服务器和低级服务器。通常，你会使用普通服务器来添加功能。但是在某些情况下，你会依赖低级服务器，比如：

- 更好的架构。通过普通服务器和低级服务器都可以创建干净的架构，但可以说使用低级服务器稍微更容易一些。
- 功能可用性。某些高级功能只能与
    低级服务器一起使用。后面的章节涵盖了引导和已在 MCP `2026-07-28` 中弃用的 legacy Sampling 功能。


## 普通服务器与低级服务器

下面是使用普通服务器创建 MCP 服务器时的样子

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

重点是你需要显式地添加你想让服务器拥有的每个工具、资源或提示。这没有问题。  

### 低级服务器方案

但是，当你使用低级服务器方案时，你需要以不同的方式思考。不是注册每个工具，而是为每种功能类型（工具、资源或提示）创建两个处理器。所以例如工具只有两个函数，如下：

- 列出所有工具。一个函数负责所有列出工具的尝试。
- 处理调用所有工具。在这里，也只有一个函数负责处理对工具的调用。

这听起来似乎工作更少，对吧？所以不再注册工具，我只需确保在列出所有工具时工具被列出，在有调用工具的请求时它被调用。

让我们看看代码现在是什么样子：

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

这里我们有一个返回功能列表的函数。工具列表中的每个条目现在都有像 `name`, `description` 和 `inputSchema` 这样的字段，以符合返回类型。这使得我们可以将工具和功能定义放在别处。现在我们可以在 tools 文件夹中创建所有工具，对所有功能都一样，这样你的项目突然间可以组织成这样：

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

这很好，我们的架构可以变得相当干净。

那调用工具呢？也是同样的思路吗？一个处理器调用任意工具？是的，完全正确，代码如下：

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
    // 待办 调用该工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

正如你从上面的代码看到的，我们需要解析出调用的工具以及参数，然后继续调用这个工具。

## 使用校验改进方法

到目前为止，你已经看到了如何用每种功能类型的两个处理器替代所有添加工具、资源和提示的注册。那我们还需要做什么？我们应该添加某种形式的校验，确保工具调用的参数是正确的。每种运行时都有自己的解决方案，比如 Python 使用 Pydantic，TypeScript 使用 Zod。思路是我们做以下事情：

- 将创建功能（工具、资源或提示）的逻辑移动到专用文件夹中。
- 添加一种方法验证传入请求，比如调用工具的请求。

### 创建一个功能

创建功能时，我们需要为该功能创建一个文件，并确保它具备该功能所需的必填字段。工具、资源和提示所需字段略有不同。

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

这里你可以看到我们如何：

- 在 *schema.py* 文件中使用 Pydantic 创建 `AddInputModel` 模式，带字段 `a` 和 `b`。
- 尝试将传入请求解析为 `AddInputModel` 类型，如果参数不匹配将抛出异常：

   ```python
   # add.py
    try:
        # 使用 Pydantic 模型验证输入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以选择将此解析逻辑放在工具调用中或处理器函数中。

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

- 在处理所有工具调用的处理器中，我们尝试将传入请求解析为工具定义的模式：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果成功，我们继续调用实际的工具：

    ```typescript
    const result = await tool.callback(input);
    ```

如你所见，该方法创建了一个很棒的架构，因为一切都有自己的位置，*server.ts* 只是一个非常小的文件，只负责连接请求处理器，每个功能都在各自的文件夹中，即 tools/、resources/ 或 /prompts。

太好了，让我们接着构建它。

## 练习：创建低级服务器

在本练习中，我们将完成以下任务：

1. 创建一个低级服务器，处理工具的列出和调用。
1. 实现一个可扩展的架构。
1. 添加校验，确保工具调用得到了正确验证。

### -1- 创建架构

首先我们需要解决的架构问题是帮助我们随功能增加而扩展，如下所示：

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

现在我们设置了一个架构，确保我们可以很方便地在 tools 文件夹中添加新工具。你也可以用相同方法给 resources 和 prompts 添加子目录。

### -2- 创建工具

接下来看看创建工具的过程。首先，它需要在它的 *tool* 子目录中创建，像这样：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # 使用 Pydantic 模型验证输入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # 待办：添加 Pydantic，这样我们可以创建一个 AddInputModel 并验证参数

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

我们可以看到这里如何定义 name、description 和使用 Pydantic 的输入模式，以及当工具被调用时会执行的处理函数。最终暴露的 `tool_add` 是一个字典，包含所有这些属性。

还有 *schema.py* 用来定义工具使用的输入模式：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我们还需要填充 *__init__.py* 文件，确保 tools 目录被识别为模块。此外，我们还需要像下面这样暴露其中的模块：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

随着工具增多，我们可以继续在此文件添加更多。

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

这里我们构建了一个包含以下属性的字典：

- name，工具的名称。
- rawSchema，Zod 模式，用于验证调用该工具的传入请求。
- inputSchema，此模式将被处理器使用。
- callback，用于调用该工具。

还有 `Tool`，用于将这个字典转换成 mcp 服务器处理器可以接受的类型，长这样：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* 用来存储每个工具的输入模式，当前只有一个模式，但随着工具增多，可以添加更多条目：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，让我们继续处理工具列表的功能。

### -3- 处理工具列表

接下来，为了处理列出工具，我们需要设置一个请求处理器。需要在服务器文件中添加如下内容：

**Python**

```python
# 为简洁起见省略代码
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

这里，我们添加了装饰器 `@server.list_tools` 和其实现函数 `handle_list_tools`。在后者中，需要生成工具列表。注意每个工具必须包含 name、description 和 inputSchema。   

**TypeScript**

为了设置请求处理器列出工具，我们需要对服务器调用 `setRequestHandler`，传入适合我们意图的模式，这里是 `ListToolsRequestSchema`。

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

太好了，现在我们解决了工具列表问题，接下来看看如何调用工具。

### -4- 处理工具调用

要调用工具，我们需要设置另一个请求处理器，这次是处理请求中指定调用哪个功能及其参数的。

**Python**

我们使用装饰器 `@server.call_tool`，并用函数 `handle_call_tool` 实现它。在该函数中，我们需要解析工具名称、参数，并确保参数对指定工具有效。可以在此函数中或实际工具中验证参数。

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

过程如下：

- 工具名已作为输入参数 `name` 提供，参数则在 `arguments` 字典中。

- 调用工具使用 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`。参数验证由指向函数的 `handler` 属性完成，如果失败将抛出异常。

到此为止，我们已经全面理解了如何使用低级服务器列出和调用工具。

请查看[完整示例](./code/README.md)

## 任务

扩展给定代码，添加多个工具、资源和提示，并思考你会发现只需要在 tools 目录添加文件，其他地方无需更改。

<em>未给出解答</em>

## 总结

本章介绍了低级服务器方案的工作原理，以及它如何帮助我们创建可持续构建的良好架构。我们还讨论了验证，并展示了如何使用验证库来创建输入验证模式。

## 接下来

- 下一个：[简单认证](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->