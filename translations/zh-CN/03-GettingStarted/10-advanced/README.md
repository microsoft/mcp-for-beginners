# 高级服务器使用

MCP SDK 中暴露了两种不同类型的服务器，普通服务器和低级服务器。通常情况下，你会使用普通服务器来添加功能。但在某些情况下，你可能希望依赖低级服务器，例如：

- 更好的架构。使用普通服务器和低级服务器都可以创建干净的架构，但可以说低级服务器稍微更容易一些。
- 功能可用性。一些高级功能只能与低级服务器一起使用。后续章节中我们会展示采样和引导技术。

## 普通服务器 vs 低级服务器

使用普通服务器创建 MCP 服务器的示例如下：

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

关键点是你显式地添加想要服务器拥有的每个工具、资源或提示。这没有错。

### 低级服务器方法

然而，使用低级服务器方法时，你需要以不同方式思考。不是注册每个工具，而是为每种特性类型（工具、资源或提示）创建两个处理器。例如，工具只有两个函数：

- 列出所有工具。一个函数负责所有尝试列出工具的操作。
- 处理调用所有工具。在这里，也只有一个函数处理对工具的调用。

听起来可能工作量更少，对吧？因此，不是注册一个工具，而是确保它在列出所有工具时被列出，并在有调用工具的请求时被调用。

让我们看看现在的代码长什么样：

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

这里我们有一个返回功能列表的函数。工具列表中的每一项现在包含字段如 `name`、`description` 和 `inputSchema` 以符合返回类型。这允许我们将工具和功能定义放在其他地方。我们现在可以将所有工具放在 tools 文件夹中，项目也可以按以下方式组织：

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

这很好，我们的架构看起来可以相当整洁。

调用工具呢？也是同样的思路，一个处理器调用任何工具？没错，代码如下：

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
    // 待办事项 调用工具，

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

从上面的代码可以看到，我们需要解析要调用的工具及其参数，然后继续执行调用。

## 使用验证改进方式

到目前为止，你已经看到如何用每种特性类型的两个处理器替代所有的注册操作。那我们还需要做什么？我们应该添加一些验证以确保工具调用参数正确。每种运行环境有自己的解决方案，比如 Python 使用 Pydantic，TypeScript 使用 Zod。思路是：

- 将创建特性（工具、资源或提示）的逻辑移动到其专属文件夹。
- 添加验证传入请求的方法，例如调用工具请求的验证。

### 创建特性

创建特性时，我们需要为该特性创建一个文件，并确保它具有该特性必需的字段。不同类型工具、资源和提示字段略有不同。

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

这里你可以看到如何做以下事情：

- 使用 Pydantic `AddInputModel` 创建一个 schema，字段是 `a` 和 `b`，位于 *schema.py* 文件中。
- 尝试将传入请求解析为 `AddInputModel` 类型，如果参数不匹配会崩溃：

   ```python
   # add.py
    try:
        # 使用Pydantic模型验证输入
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以选择将解析逻辑放在工具调用本身或处理函数中。

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

- 在处理所有工具调用的处理器中，尝试将传入请求解析到工具定义的 schema 中：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果成功，则继续调用实际工具：

    ```typescript
    const result = await tool.callback(input);
    ```

如你所见，这种方法建立了良好的架构，所有东西各归其位，*server.ts* 是一个非常小的文件，只负责连接请求处理器，每个特性放在对应文件夹下：tools/、resources/ 或 prompts/。

很好，让我们接下来尝试构建它。

## 练习：创建低级服务器

本练习中，我们将执行：

1. 创建低级服务器，处理工具列表和工具调用。
2. 实现一个可扩展的架构。
3. 添加验证以确保工具调用得到正确验证。

### -1- 创建架构

首先需要搭建一个帮助扩展的架构，形如下所示：

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

现在我们建立的架构确保可以轻松在 tools 文件夹添加新工具。你也可以按照此方法为资源和提示添加子目录。

### -2- 创建工具

接下来看看如何创建工具。首先必须在 *tool* 子目录中创建，例如：

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

这里定义了 name、description 和输入 schema（用 Pydantic 定义），以及调用该工具时将执行的处理器。最后，暴露 `tool_add` 字典，包含所有属性。

还有 *schema.py* 用于定义工具的输入 schema：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

还需要填充 *__init__.py* 以确保 tools 目录被视为模块，并导出模块，如下所示：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

随着工具添加，我们可以继续往这里添加。

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

这里创建了一个字典，包含属性：

- name，工具名称。
- rawSchema，这是 Zod schema，用于验证调用工具的请求。
- inputSchema，该 schema 由处理器使用。
- callback，用于调用工具。

还有 `Tool` 用于将该字典转换为 mcp 服务器处理器可接受的类型，代码如下：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

 *schema.ts* 存储每个工具的输入 schema，目前只有一个，后续添加工具时可以加更多：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，接下来处理工具列表的实现。

### -3- 处理工具列表

接下来处理请求处理器，负责列出工具。服务器文件中添加如下内容：

**Python**

```python
# 为简洁起见，省略代码
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

这里使用修饰器 `@server.list_tools` 和实现函数 `handle_list_tools`，它需要返回工具列表。注意每个工具需有 name、description 和 inputSchema。

**TypeScript**

设置处理器时调用 `setRequestHandler`，传入符合请求的 schema，比如 `ListToolsRequestSchema`：

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
// 代码简略
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 返回已注册工具列表
  return {
    tools: tools
  };
});
```

很好，现在我们解决了工具列表部分，接下来看看如何调用工具。

### -4- 处理调用工具

调用工具时，需要另一个请求处理器，处理指定调用哪个功能及传入哪些参数的请求。

**Python**

使用修饰器 `@server.call_tool`，实现函数 `handle_call_tool`。函数内部解析工具名和参数，并验证参数是否符合该工具要求。参数验证可以在此处或实际工具内部执行。

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

发生了什么：

- 工具名通过输入参数 `name` 获取；参数在 `arguments` 字典中。

- 通过 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 调用工具。参数验证在 `handler` 属性指向的函数中执行，如果失败会抛出异常。

好了，现在我们已经完整了解了如何使用低级服务器列出和调用工具。

完整示例见 [full example](./code/README.md)

## 作业

请用多个工具、资源和提示扩展已有代码，并体会你只需要在 tools 目录添加文件，无需其他地方改动。

*未提供答案*

## 总结

本章介绍了低级服务器方法及其如何帮助我们构建可扩展的良好架构。还讲了验证的概念，并展示如何使用验证库创建输入验证 schema。

## 接下来

- 下一章：[简单认证](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由人工智能翻译服务【Co-op Translator】（https://github.com/Azure/co-op-translator）进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。请以原始语言的文档为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译可能引起的任何误解或错误解释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->