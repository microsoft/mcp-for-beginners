# Advanced server usage

Dem get two kain servers wey dey inside MCP SDK, your normal server and di low-level server. Normally, you go use di regular server to add features join. But for some cases, you go want use di low-level server like:

- Better architecture. E possible to create clean architecture with both regular server and low-level server but e fit be say e small better with low-level server.
- Feature availability. Some advanced features fit only work with low-level server. You go see dis for later chapters as we add sampling and elicitation.

## Regular server vs low-level server

Dis na how e be to create MCP Server with regular server

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

Di koko be say you need add every tool, resource or prompt wey you want server get explicitly. No wahala with dat.  

### Low-level server approach

But if you use low-level server approach, you for dey think am differently. Instead of you dey register every tool, you go create two handlers per feature type (tools, resources or prompts). So for example tools go get only two functions like dis:

- Listing all tools. One function go dey handle all attempts to list tools.
- handle calling all tools. Here sef, na only one function dey handle calls to tool

E dey sound like less wahala no be? So instead of you dey register tool, na to make sure say tool dey listed anytime I list all tools and make sure say dem dey call am when request come to call tool. 

Make we see how di code now look:

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
  // Return di list of regista tool dem
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

Here now we get one function wey dey return list of features. Each tool wey dey inside tools list now get fields like `name`, `description` and `inputSchema` to follow di return type. Dis one make us fit put our tools and feature definition for anywhere. We fit now create all our tools for tools folder and di same thing go happen for all your features so your project fit sudden be organized like dis:

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

E sweet wella, our architecture fit look very clean.

How e be for calling tools, na the same idea be dat, one handler to call any tool? Yes na, dis na di code for dat:

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
    // TODO make we call the tool,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

As you fit see from di code, we need to parse di tool wey we go call, plus the arguments, then we go dey go call tool.

## Improving the approach with validation

So far, you don see how all your registrations to add tools, resources and prompts fit replace with these two handlers per feature type. Wetin else we gats do? Well, we suppose add some kain validation to make sure say di tool dey called with correct arguments. Each runtime get their own way for dat, for example Python dey use Pydantic and TypeScript dey use Zod. Di idea na say we go do thiings like:

- Move di logic to create a feature (tool, resource or prompt) go inside the folder wey e belong.
- Add way to validate incoming request wey want call tool.

### Create a feature

To create feature, we go create file for dat feature and make sure say e get di fields wey di feature need. Di fields fit differ small between tools, resources and prompts.

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
        # Check and confirm input wit Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, make we fit create AddInputModel and check args well well

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

here you fit see how we do di following:

- Create schema using Pydantic `AddInputModel` with fields `a` and `b` for file *schema.py*.
- Try to parse incoming request make e be type `AddInputModel`, if parameters no match e go crash:

   ```python
   # add.py
    try:
        # Make sure say input correct wit Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

You fit decide to put dis parsing logic for inside tool call or for handler function.

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

- For di handler wey dey deal with all tool calls, we go try parse incoming request into tool's schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    if dis work then we proceed call di actual tool:

    ```typescript
    const result = await tool.callback(input);
    ```

As you fit see, dis approach go create correct architecture as everything go dey where e suppose dey, *server.ts* na small file wey only connect request handlers and every feature dey their own folder like tools/, resources/ or /prompts.

Correct, make we try build dis next.

## Exercise: Creating a low-level server

For dis exercise, we go do:

1. Create low-level server wey go handle listing tools and calling tools.
1. Implement architecture wey you fit build upon.
1. Add validation to sure say your tool calls dey validated well.

### -1- Create an architecture

Di first thing we need na architecture wey go help us scale as we add more features, dis na how e be:

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

Now we don setup architecture wey go make am easy to add new tools inside tools folder. Feel free to follow dis to add subdirectories for resources and prompts.

### -2- Creating a tool

Make we see how e be to create tool next. First, e need to dey inside *tool* subdirectory like dis:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Check input wit Pydantic model
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

Wetin we see here na how we define name, description, and input schema with Pydantic and handler wey go run anytime dis tool call. Finally, we expose `tool_add` wey be dictionary holding all dis properties.

Also we get *schema.py* wey define input schema wey our tool go use:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We also gats update *__init__.py* to make sure tools directory dey serve as module. Plus, we go expose modules inside am like dis:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We fit still dey add more tools to dis file as we dey add more.

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

Here we create dictionary wey get properties:

- name, na name of tool be dat.
- rawSchema, dis na Zod schema, e go check if incoming request for call tool dey valid.
- inputSchema, tool handler go use dis schema.
- callback, dis na function to run tool.

We still get `Tool` wey convert dictionary into type wey mcp server handler fit accept and e be like dis:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

We get *schema.ts* wey hold input schemas for each tool, e be like dis with only one schema so far but as we add tools we fit add more entries:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Correct, make we continue to handle listing of our tools next.

### -3- Handle tool listing

Next, to handle tool listing, we need set request handler for dat. Dis na wetin we add to server file:

**Python**

```python
# kod don comot make e short
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

Here, we add decorator `@server.list_tools` and function `handle_list_tools` to implement am. Dis one need produce list of tools. Make sure each tool get name, description and inputSchema.   

**TypeScript**

To set request handler to list tools, we call `setRequestHandler` on server with schema wey describe wetin we wan do, for dis case `ListToolsRequestSchema`. 

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
// code dem no put for here make e short
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return di list of tools wey dem don register
  return {
    tools: tools
  };
});
```

Good, now we don solve listing tools, make we look how we fit call tools next.

### -4- Handle calling a tool

To call tool, we set another request handler, dis time to handle request wey talk which feature to call and which arguments.

**Python**

Make we use decorator `@server.call_tool` and implement with function like `handle_call_tool`. Inside this function, we go parse tool name, im arguments and make sure say arguments correct for that tool. We fit validate arguments for dis function or inside the real tool.

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
        # make you call the tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Dis na wetin dey happen:

- Our tool name already dey as input parameter `name` wey true for our arguments for `arguments` dictionary.

- Tool go run with `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Di validation dey inside `handler` property wey point to function, if dis one fail e go throw error. 

There, now we understand well how to list and call tools using low-level server.

See di [full example](./code/README.md) here

## Assignment

Add more tools, resources and prompt to di code wey dem give you and observe how you only need add files for tools directory and no other place. 

*No solution given*

## Summary

For dis chapter, we don see how low-level server approach dey work and how e fit help build better architecture we fit continue to add on top. We sef talk about validation and you see how to use validation libraries create schemas for input validation.

## What's Next

- Next: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don be translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am correct, abeg sabi say automated translations fit get some yawa or incorrect tins. The original document wey e dey for im native language na the correct one wey you suppose trust. For important tins, better make person wey sabi translate am do am. We no go responsible for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->