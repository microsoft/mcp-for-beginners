# 高级服务器使用

MCP SDK 中提供了两种不同类型的服务器：普通服务器和低级服务器。通常情况下，你会使用普通服务器来添加功能。然而，在某些情况下，你可能需要依赖低级服务器，例如：

- 更好的架构。虽然使用普通服务器和低级服务器都可以创建一个干净的架构，但可以说使用低级服务器稍微容易一些。
- 功能可用性。一些高级功能只能通过低级服务器使用。在后续章节中，你会看到我们如何添加采样和引导功能。

## 普通服务器 vs 低级服务器

以下是使用普通服务器创建 MCP 服务器的示例：

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

重点在于你需要显式地添加每个工具、资源或提示到服务器中。这种方式没有问题。

### 低级服务器方法

然而，当你使用低级服务器方法时，需要采用不同的思路。与其注册每个工具，不如为每种功能类型（工具、资源或提示）创建两个处理程序。例如，对于工具，只需要两个函数：

- 列出所有工具。一个函数负责所有列出工具的尝试。
- 处理调用所有工具。另一个函数负责处理对工具的调用。

听起来工作量可能更少，对吧？因此，与其注册一个工具，我只需要确保工具在列出所有工具时被列出，并且在收到调用工具的请求时被调用。

让我们看看代码是如何实现的：

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

在这里，我们有一个返回功能列表的函数。工具列表中的每个条目现在都有 `name`、`description` 和 `inputSchema` 等字段，以符合返回类型。这使我们可以将工具和功能定义放在其他地方。我们现在可以在一个工具文件夹中创建所有工具，其他功能也可以这样组织，因此项目可以像这样组织：

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

这很好，我们的架构可以变得非常干净。

那么调用工具呢？是否也是同样的思路，一个处理程序处理所有工具的调用？是的，完全正确，以下是相关代码：

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

从上面的代码可以看出，我们需要解析出要调用的工具及其参数，然后继续调用该工具。

## 使用验证改进方法

到目前为止，你已经看到如何通过每种功能类型的两个处理程序替换所有工具、资源和提示的注册。那么接下来我们需要做什么呢？我们应该添加某种形式的验证，以确保工具被正确的参数调用。每种运行时都有自己的解决方案，例如 Python 使用 Pydantic，TypeScript 使用 Zod。我们的目标是：

- 将创建功能（工具、资源或提示）的逻辑移到专用文件夹。
- 添加一种验证传入请求的方法，例如调用工具的请求。

### 创建功能

要创建一个功能，我们需要为该功能创建一个文件，并确保它具有该功能所需的必填字段。这些字段在工具、资源和提示之间略有不同。

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

在这里你可以看到我们做了以下事情：

- 在文件 *schema.py* 中使用 Pydantic 创建了一个名为 `AddInputModel` 的模式，包含字段 `a` 和 `b`。
- 尝试将传入请求解析为 `AddInputModel` 类型，如果参数不匹配，将会报错：

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

你可以选择将此解析逻辑放在工具调用本身或处理程序函数中。

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

- 在处理所有工具调用的处理程序中，我们尝试将传入请求解析为工具定义的模式：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    如果解析成功，我们继续调用实际工具：

    ```typescript
    const result = await tool.callback(input);
    ```

如你所见，这种方法创建了一个很好的架构，每个部分都有其位置，*server.ts* 文件非常小，仅用于连接请求处理程序，而每个功能都在其各自的文件夹中，例如 tools/、resources/ 或 prompts/。

很好，让我们尝试构建这个架构。

## 练习：创建低级服务器

在这个练习中，我们将完成以下任务：

1. 创建一个低级服务器，处理工具的列出和调用。
1. 实现一个可扩展的架构。
1. 添加验证以确保工具调用得到正确验证。

### -1- 创建架构

首先，我们需要解决一个问题：如何设计一个架构以便随着功能的增加能够轻松扩展。以下是架构示例：

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

现在我们已经设置了一个架构，确保我们可以轻松地在工具文件夹中添加新工具。你可以按照这个架构为资源和提示添加子目录。

### -2- 创建工具

接下来，我们看看创建工具的过程。首先，它需要在其 *tool* 子目录中创建，如下所示：

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

我们看到这里定义了工具的名称、描述、使用 Pydantic 定义的输入模式，以及一个处理程序，当工具被调用时会执行。最后，我们暴露了 `tool_add`，它是一个包含所有这些属性的字典。

还有一个 *schema.py* 文件，用于定义工具使用的输入模式：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

我们还需要填充 *__init__.py* 文件，以确保工具目录被视为一个模块。此外，我们需要暴露其中的模块，如下所示：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

随着工具的增加，我们可以继续向这个文件添加内容。

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

在这里，我们创建了一个包含以下属性的字典：

- name：工具的名称。
- rawSchema：这是 Zod 模式，用于验证调用该工具的传入请求。
- inputSchema：此模式将由处理程序使用。
- callback：用于调用工具。

还有 `Tool`，它用于将这个字典转换为 MCP 服务器处理程序可以接受的类型，如下所示：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

此外，还有 *schema.ts* 文件，我们在其中存储每个工具的输入模式，目前只有一个模式，但随着工具的增加，我们可以添加更多条目：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

很好，接下来我们处理工具的列出功能。

### -3- 处理工具列出

接下来，为了处理工具的列出，我们需要在服务器文件中设置一个请求处理程序。以下是需要添加的内容：

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

在这里，我们添加了装饰器 `@server.list_tools` 和实现函数 `handle_list_tools`。在后者中，我们需要生成一个工具列表。注意每个工具需要有名称、描述和输入模式。

**TypeScript**

为了设置列出工具的请求处理程序，我们需要在服务器上调用 `setRequestHandler`，并使用一个适合我们目标的模式，在这种情况下是 `ListToolsRequestSchema`。

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

很好，现在我们已经解决了列出工具的部分，接下来看看如何调用工具。

### -4- 处理工具调用

为了调用工具，我们需要设置另一个请求处理程序，这次专注于处理指定要调用的功能及其参数的请求。

**Python**

我们使用装饰器 `@server.call_tool` 并通过函数 `handle_call_tool` 实现。在该函数中，我们需要解析工具名称及其参数，并确保参数对该工具有效。我们可以选择在此函数中或工具的下游验证参数。

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

以下是发生的事情：

- 工具名称已经作为输入参数 `name` 提供，参数以 `arguments` 字典的形式存在。

- 工具通过 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` 调用。参数的验证发生在 `handler` 属性指向的函数中，如果验证失败，将抛出异常。

现在我们已经全面了解了如何使用低级服务器列出和调用工具。

查看[完整示例](./code/README.md)

## 作业

使用给定的代码扩展工具、资源和提示的数量，并思考你是否注意到只需要在工具目录中添加文件，而无需修改其他地方。

*不提供解决方案*

## 总结

在本章中，我们了解了低级服务器方法的工作原理，以及如何利用它创建一个可以持续扩展的良好架构。我们还讨论了验证，并展示了如何使用验证库创建输入验证模式。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。