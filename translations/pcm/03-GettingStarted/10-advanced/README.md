# Advanced server usage

Dem get two kain servers wey dem dey show for MCP SDK, your normal server and the low-level server. Normally, you go dey use the regular server to add features. But for some cases, you go wan rely on the low-level server like:

- Better architecture. E fit possible to create clean architecture with both regular server and low-level server but e fit talk say e easy small for low-level server.
- Feature availability. Some advanced features fit only work with
    low-level server. Later chapters go talk about Elicitation and the legacy Sampling
    feature, wey MCP don stop use for `2026-07-28`.

## Regular server vs low-level server

Dis na how dem dey create MCP Server with the regular server

**Python**

```python
mcp = FastMCP("Demo")

# Add one addition tool
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

// Add one addition tool
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

The gist be say you dey add each tool, resource or prompt wey you want the server get by yourself. Nothing wrong there.

### Low-level server approach

But if you dey use the low-level server approach, you need to think am different. Instead of registering each tool, you go create two handlers for each feature type (tools, resources or prompts). So for example, tools go only get two functions like dis:

- Listing all tools. One function dey responsible for all attempts wey dey list tools.
- handle calling all tools. Also, only one function dey handle calls to tool

E come be like say na less work be dis right? Instead of registering tool, I just need make sure say tool dey listed when I list all tools and say e go get called when request come to call tool.

Make we look how the code dey now:

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
  // Return di list of tools wey don register
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

Now we get function wey dey return list of features. Each entry for tools list get fields like `name`, `description` and `inputSchema` wey dey follow the return type. Dis one make we fit put our tools and feature definition for other place. Now, we fit create all tools for tools folder and everything go dey organized like dis:

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

E sweet, our architecture fit dey clean well well.

How about to call tools, na the same thing, one handler to call any tool? Yes, na so e be, see the code:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools na dictionary wey get tool names as keys
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
    // TODO call di tool,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

As you fit see for di code, we need to parse the tool to call, with which arguments, then we go call the tool.

## Improving the approach with validation

So far, you don see how all your registrations to add tools, resources and prompts fit change to these two handlers per feature type. Wetin else we need do? We go add validation to make sure say tool dey call with correct arguments. Each runtime get dia own way for dis, for example Python dey use Pydantic and TypeScript dey use Zod. The plan be say we go do dis:

- Move the logic wey dey create feature (tool, resource or prompt) to im own folder.
- Add way to validate incoming request wey wan for example call tool.

### Create a feature

To create feature, we go create file for the feature and make sure it get mandatory fields wey the feature need. The fields fit dey different small between tools, resources and prompts.

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
        # Check if input correct wit Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, mek we fit create AddInputModel and check args well well

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Here you fit see how we do dis:

- Create schema using Pydantic `AddInputModel` with fields `a` and `b` inside file *schema.py*.
- Try parse the incoming request as type `AddInputModel`, if parameters no match e go crash:

   ```python
   # add.py
    try:
        # Chek di input wit Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

You fit choose put dis parsing logic inside the tool call or inside handler function.

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

- Inside handler wey dey handle all tool calls, now we try parse the incoming request with tool schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    if e work, then we go call the tool:

    ```typescript
    const result = await tool.callback(input);
    ```

As you fit see, dis approach fit build nice architecture since everything get im place, the *server.ts* na small file wey just wire up request handlers and every feature dey im own folder like tools/, resources/ or /prompts.

Correct, make we try build dis next.

## Exercise: Creating a low-level server

For this exercise, we go do dis things:

1. Create low-level server wey handle listing tools and calling tools.
1. Build architecture wey you fit add more on top.
1. Add validation to make sure tool calls dey properly validated.

### -1- Create architecture

The first thing we need na architecture wey go help us scale as we add features, e look like dis:

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

Now we don set architecture wey make am easy to add new tools for tools folder. Feel free to add subdirectories for resources and prompts.

### -2- Creating tool

Make we see how to create tool. First, e go dey inside *tool* subdirectory like dis:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Check the input with Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, make we fit create AddInputModel and check args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

What we see here be how we define name, description, and input schema using Pydantic and handler wey go run when tool get call. Last last, we expose `tool_add` wey be dictionary wey hold all these properties.

We get *schema.py* too wey dey define input schema for our tool:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We need also make *__init__.py* make tools directory fit dey treated as module. Plus, we expose the modules inside like dis:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We fit still add to this file as we add more tools.

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

Here we create dictionary with properties:

- name, na di name of the tool.
- rawSchema, na the Zod schema, e go validate incoming requests wey wan call tool.
- inputSchema, this schema go dey used by the handler.
- callback, this one na to invoke the tool.

We get `Tool` wey convert dictionary to type wey mcp server handler fit accept, e look like dis:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

And schema.ts na where we dey put input schemas for each tool, now e get only one schema but as we add tools, we fit add more:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Correct, make we move to handle tool listing.

### -3- Handle tool listing

Next to handle tool listing, we go setup request handler for am. Na wetin we go add for server file:

**Python**

```python
# code no too long, e chop shorten
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

We add decorator `@server.list_tools` and the function `handle_list_tools`. For the function, we need make list of tools. Every tool must get name, description and inputSchema.

**TypeScript**

To setup request handler for tool listing, we call `setRequestHandler` on server with schema wey go fit `ListToolsRequestSchema`.

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
// code comot make e short
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Make e return di list of registered tools
  return {
    tools: tools
  };
});
```

Correct now, we don solve tool listing, make we see how to call tools.

### -4- Handle call tool

To call tool, we setup new request handler wey go handle which feature to call and arguments.

**Python**

We use decorator `@server.call_tool` and function `handle_call_tool`. Inside the function, we parse tool name, arguments, and check say arguments valid. We fit validate in this function or inside the tool itself.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools na dictionary wey get tool names as keys
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # make you use the tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Here be wetin dey happen:

- Tool name dey as input parameter `name`. Arguments dey as `arguments` dictionary.

- Tool dey called with `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validation dey happen for `handler`, if validation fail e go raise exception.

Now, we get full idea of how to list and call tools with low-level server.

Check [full example](./code/README.md)

## Assignment

Add tools, resources and prompts for the code wey dem give you and notice say you go only add files for tools directory and nowhere else.

*No solution given*

## Summary

For this chapter, we see how low-level server approach work and how e fit help create better architecture wey we fit build on top. We also talk validation and you see how to use validation libraries to create schemas for input validation.

## What’s Next

- Next: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->