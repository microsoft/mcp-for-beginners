<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1de8367745088b9fcd4746ea4cc5a161",
  "translation_date": "2025-11-18T19:17:39+00:00",
  "source_file": "03-GettingStarted/10-advanced/README.md",
  "language_code": "pcm"
}
-->
# Advanced server usage

For MCP SDK, e get two kain server wey e dey expose: di normal server and di low-level server. Normally, you go use di regular server to add features join am. But for some cases, you fit wan use di low-level server like:

- Better architecture. You fit create clean architecture with both di regular server and di low-level server, but e fit dey small-small easier with di low-level server.
- Feature availability. Some advanced features fit only work with di low-level server. You go see dis one for later chapters as we dey add sampling and elicitation.

## Regular server vs low-level server

Dis na how di creation of MCP Server go look like with di regular server:

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

Di koko be say you go explicitly add each tool, resource or prompt wey you wan make di server get. Nothing dey wrong with dat one.

### Low-level server approach

But if you wan use di low-level server approach, you go need think am differently. Instead of registering each tool, you go create two handlers per feature type (tools, resources or prompts). For example, for tools, you go only get two functions like dis:

- List all tools. One function go dey responsible for all attempts to list tools.
- Handle calling all tools. Here too, na only one function go dey handle calls to any tool.

E be like say dis one go reduce work small, abi? So instead of registering tool, I just need make sure say di tool dey listed when I list all tools and say e dey called when request come to call di tool.

Make we see how di code go look now:

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

Now, we get function wey dey return list of features. Each entry for di tools list now get fields like `name`, `description` and `inputSchema` to match di return type. Dis one go allow us put our tools and feature definition for another place. We fit now create all our tools for tools folder and di same thing go for all your features so your project fit dey organized like dis:

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

E make sense, our architecture fit dey clean like dat.

Wetin about calling tools? E be di same idea, one handler to call any tool? Yes, na exactly so. See di code for dat one:

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

As you see for di code above, we need to parse di tool wey we wan call, and wetin arguments we go use, then we go proceed to call di tool.

## Improving the approach with validation

So far, you don see how all your registrations to add tools, resources and prompts fit dey replaced with dis two handlers per feature type. Wetin else we need do? Well, we suppose add validation to make sure say di tool dey called with correct arguments. Each runtime get their own way to do dis, for example Python dey use Pydantic and TypeScript dey use Zod. Di idea be say we go do di following:

- Move di logic for creating feature (tool, resource or prompt) go di folder wey e dey.
- Add way to validate incoming request wey dey ask to call tool, for example.

### Create a feature

To create feature, we go need create file for dat feature and make sure say e get di mandatory fields wey di feature need. Di fields go dey different small between tools, resources and prompts.

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

Here you fit see how we dey do di following:

- Create schema using Pydantic `AddInputModel` with fields `a` and `b` for file *schema.py*.
- Try parse di incoming request to be of type `AddInputModel`. If di parameters no match, e go crash:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

You fit decide whether to put dis parsing logic for di tool call itself or for di handler function.

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

- For di handler wey dey deal with all tool calls, we go try parse di incoming request into di tool's defined schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    if e work, then we go proceed to call di actual tool:

    ```typescript
    const result = await tool.callback(input);
    ```

As you see, dis approach dey create better architecture as everything get di place wey e suppose dey. Di *server.ts* go be very small file wey just dey wire up di request handlers and each feature go dey their own folder like tools/, resources/ or prompts/.

Nice one, make we try build dis next.

## Exercise: Creating a low-level server

For dis exercise, we go do di following:

1. Create low-level server wey go handle listing of tools and calling of tools.
1. Implement architecture wey you fit build on top.
1. Add validation to make sure say your tool calls dey properly validated.

### -1- Create an architecture

Di first thing we need address na architecture wey go help us scale as we dey add more features. Dis na how e go look:

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

Now we don set up architecture wey go make sure say we fit easily add new tools for tools folder. Feel free to follow dis to add subdirectories for resources and prompts.

### -2- Creating a tool

Make we see how to create tool next. First, e need dey created for di *tool* subdirectory like dis:

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

Wetin we see here na how we dey define name, description, input schema using Pydantic and handler wey go dey invoked once dis tool dey called. Lastly, we dey expose `tool_add` wey be dictionary wey hold all dis properties.

E still get *schema.py* wey we dey use to define di input schema wey our tool go use:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We go also need populate *__init__.py* to make sure say di tools directory dey treated as module. Plus, we go expose di modules inside am like dis:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We fit dey add to dis file as we dey add more tools.

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

Here we dey create dictionary wey get properties:

- name, na di name of di tool.
- rawSchema, na di Zod schema, e go validate incoming requests to call dis tool.
- inputSchema, dis schema go dey used by di handler.
- callback, dis one dey used to invoke di tool.

E still get `Tool` wey dey convert dis dictionary into type wey di MCP server handler fit accept and e go look like dis:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

And e get *schema.ts* where we dey store di input schemas for each tool. E go look like dis with only one schema for now, but as we dey add tools, we go dey add more entries:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Nice one, make we proceed to handle di listing of our tools next.

### -3- Handle tool listing

Next, to handle di listing of tools, we need set up request handler for dat. Dis na wetin we need add to our server file:

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

Here, we dey add decorator `@server.list_tools` and di implementing function `handle_list_tools`. For di function, we need produce list of tools. Note say each tool need get name, description and inputSchema.

**TypeScript**

To set up request handler for listing tools, we need call `setRequestHandler` for di server with schema wey fit wetin we dey try do, for dis case `ListToolsRequestSchema`.

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

Nice one, now we don solve di part of listing tools. Make we look how we fit dey call tools next.

### -4- Handle calling a tool

To call tool, we need set up another request handler, dis time to deal with request wey dey specify which feature to call and with wetin arguments.

**Python**

Make we use di decorator `@server.call_tool` and implement am with function like `handle_call_tool`. Inside di function, we need parse di tool name, di argument and make sure say di arguments dey valid for di tool wey dem wan call. We fit validate di arguments for dis function or downstream for di actual tool.

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

Dis na wetin dey happen:

- Di tool name don already dey as input parameter `name`, di same thing for di arguments wey dey as `arguments` dictionary.

- Di tool dey called with `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Di validation of di arguments dey happen for di `handler` property wey dey point to function. If e fail, e go raise exception.

Now, we don get full understanding of how to list and call tools using low-level server.

See di [full example](./code/README.md) here.

## Assignment

Add more tools, resources and prompts to di code wey dem give you and reflect on how you notice say you only need add files for tools directory and nowhere else.

*No solution given*

## Summary

For dis chapter, we see how di low-level server approach dey work and how e fit help us create better architecture wey we fit dey build on top. We also discuss validation and dem show you how to use validation libraries to create schemas for input validation.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg sabi say transle-shon wey machine do fit get mistake or no dey accurate well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e better make professional human transle-shon dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->