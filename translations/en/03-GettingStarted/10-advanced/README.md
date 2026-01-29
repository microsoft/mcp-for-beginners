# Advanced server usage

The MCP SDK provides two types of servers: the regular server and the low-level server. Typically, you would use the regular server to add features. However, there are cases where the low-level server is preferable, such as:

- **Improved architecture**: While both server types can support clean architecture, the low-level server may make it slightly easier to achieve.
- **Feature availability**: Some advanced features, like sampling and elicitation (covered in later chapters), are only accessible via the low-level server.

## Regular server vs low-level server

Here’s an example of how an MCP Server is created using the regular server:

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

With the regular server, you explicitly add each tool, resource, or prompt that you want the server to include. This approach works well.

### Low-level server approach

Using the low-level server requires a different mindset. Instead of registering each tool individually, you create two handlers for each feature type (tools, resources, or prompts). For example, tools would have:

- **Listing all tools**: A single function responsible for listing all tools.
- **Handling tool calls**: A single function responsible for handling calls to any tool.

This approach might seem like less work. Instead of registering each tool, you ensure the tool is listed when tools are requested and that it is called when an incoming request specifies it.

Here’s how the code looks:

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

In this example, a function returns a list of features. Each entry in the tools list includes fields like `name`, `description`, and `inputSchema` to match the expected return type. This allows you to organize your tools and feature definitions in separate folders, resulting in a project structure like this:

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

This organization helps create a clean architecture.

What about calling tools? Is it the same idea—one handler for calling any tool? Yes, exactly. Here’s the code for that:

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

As shown, the handler parses the tool to be called, along with its arguments, and then proceeds to invoke the tool.

## Improving the approach with validation

So far, we’ve replaced individual registrations for tools, resources, and prompts with two handlers per feature type. What’s next? Adding validation to ensure tools are called with the correct arguments. Each runtime has its own solution for this—for example, Python uses Pydantic, and TypeScript uses Zod. The process involves:

- Moving the logic for creating a feature (tool, resource, or prompt) to its dedicated folder.
- Adding validation for incoming requests, such as calls to tools.

### Creating a feature

To create a feature, you need to create a file for it and ensure it includes the mandatory fields required for that feature. The required fields vary slightly between tools, resources, and prompts.

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

Here’s what happens:

- A schema is created using Pydantic (`AddInputModel`) with fields `a` and `b` in the file *schema.py*.
- The incoming request is parsed to match the `AddInputModel` type. If the parameters don’t match, the process will fail:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

You can decide whether to include this parsing logic in the tool call itself or in the handler function.

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

In the handler for all tool calls, the incoming request is parsed into the tool’s defined schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

If the parsing succeeds, the tool is invoked:

    ```typescript
    const result = await tool.callback(input);
    ```

This approach results in a well-organized architecture. The *server.ts* file remains small, handling only request wiring, while each feature resides in its respective folder (e.g., tools/, resources/, or prompts/).

Great! Let’s build this next.

## Exercise: Creating a low-level server

In this exercise, we will:

1. Create a low-level server to handle tool listing and tool calls.
2. Implement a scalable architecture.
3. Add validation to ensure tool calls are properly validated.

### -1- Create an architecture

First, we need an architecture that supports scalability as we add more features. Here’s an example:

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

This setup ensures that new tools can be added easily in the tools folder. You can follow the same structure to add subdirectories for resources and prompts.

### -2- Creating a tool

Next, let’s create a tool. It should be placed in the *tools* subdirectory like this:

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

Here’s what happens:

- The tool’s name, description, and input schema (defined using Pydantic) are specified.
- A handler is defined to be invoked when the tool is called.
- The `tool_add` dictionary is exposed, containing all these properties.

The *schema.py* file defines the input schema for the tool:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Additionally, *__init__.py* must be populated to treat the tools directory as a module. It should expose the modules within it:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

You can update this file as you add more tools.

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

Here, a dictionary is created with the following properties:

- **name**: The tool’s name.
- **rawSchema**: A Zod schema for validating incoming requests.
- **inputSchema**: A schema used by the handler.
- **callback**: A function to invoke the tool.

The `Tool` type converts this dictionary into a format the MCP server handler can accept:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

The *schema.ts* file stores input schemas for tools. Currently, it contains one schema, but more can be added as needed:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Great! Let’s move on to handling tool listing.

### -3- Handle tool listing

To handle tool listing, we need to set up a request handler. Here’s what to add to the server file:

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

The `@server.list_tools` decorator is used, along with the `handle_list_tools` function. This function generates a list of tools, each with a name, description, and inputSchema.

**TypeScript**

To set up the request handler for listing tools, use `setRequestHandler` on the server with a schema like `ListToolsRequestSchema`:

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

Now that tool listing is handled, let’s look at calling tools.

### -4- Handle calling a tool

To call a tool, set up another request handler to process requests specifying the feature to call and its arguments.

**Python**

Use the `@server.call_tool` decorator and implement it with a function like `handle_call_tool`. This function parses the tool name and arguments, ensuring the arguments are valid for the specified tool. Validation can occur here or downstream in the tool itself.

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

Here’s what happens:

- The tool name is extracted from the `name` parameter, and arguments are extracted from the `arguments` dictionary.
- The tool is invoked using `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argument validation occurs in the `handler` function, raising an exception if validation fails.

Now you have a complete understanding of listing and calling tools using a low-level server.

See the [full example](./code/README.md) here.

## Assignment

Extend the provided code by adding tools, resources, and prompts. Reflect on how this approach allows you to add files only in the tools directory without modifying other parts of the project.

*No solution provided*

## Summary

In this chapter, we explored the low-level server approach and how it helps create a scalable architecture. We also discussed validation and demonstrated how to use validation libraries to create schemas for input validation.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.