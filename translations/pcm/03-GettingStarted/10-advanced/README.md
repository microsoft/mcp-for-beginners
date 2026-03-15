# Advanced server usage

Dem get two kain server weh dem show for MCP SDK, na your normal server and the low-level server. Normally, you go use the regular server to add features to am. But for some cases, you fit want rely on the low-level server like:

- Better architecture. E possible to create one clean architecture with both the regular server and low-level server but e fit be sey e better small with low-level server.
- Feature availability. Some advanced features fit only work with low-level server. You go see dis one for later chapters as we dey add sampling and elicitation.

## Regular server vs low-level server

Dis na how e be wen you dey create MCP Server with regular server

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

The koko be sey you go add each tool, resource or prompt wey you want the server get clearly. No wahala with dat.  

### Low-level server approach

But wen you use the low-level server method, you go need think am different. Instead make you register each tool, you go create two handlers per feature type (tools, resources or prompts). So for example tools get only two functions like this:

- Listing all tools. One function go handle all tries to list tools.
- handle calling all tools. Here too, na one function dey handle calls to any tool.

E sound like say e go reduce work abi? So instead make you register tool every time, you just go make sure say tool dey for list wen you dey list all tools and e dey called wen request don come to call tool.

Make we look how the code look now:

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
  // Return di list of registered tools
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

Now we get one function wey dey return list of features. Every tool wey dey the tools list get fields like `name`, `description` and `inputSchema` to follow the return type. Dis one make we fit put our tools and feature definition anywhere. We fit create all tools for tools folder and the same tin go for all your features so your project fit arrange like this suddenly:

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

E good well well, our architecture fit look clean nicely.

How about to call tools, na the same thing abi, one handler to call tool, any tool? Yes na, dis be the code for am:

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
    // TODO make call to di tool,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

As you see for top code, we need parse the tool to call, and the arguments to use, then we go call the tool.

## Improving the approach with validation

Up till now, you don see how to replace all your registrations for adding tools, resources and prompts with these two handlers per feature type. Wetin else we need do? We for add some kind validation to make sure tool dey called with correct arguments. Each runtime get their own way to do am, for example Python dey use Pydantic and TypeScript dey use Zod. The idea be say we go do dis:

- Move the logic to create feature (tool, resource or prompt) go their own folder.
- Add way to validate incoming request wey want for example call tool.

### Create a feature

To create feature, we go create file for that feature and make sure sey e get the important fields wey the feature need. The fields dey different small between tools, resources and prompts.

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
        # Check say input correct wit Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we fit create AddInputModel and check args well well

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Here you fit see how we dey do dis tin:

- Create schema using Pydantic `AddInputModel` with fields `a` and `b` for file *schema.py*.
- Try parse the incoming request make e be of type `AddInputModel`, if parameters no match e go crash:

   ```python
   # add.py
    try:
        # Check di input wit Pydantic model make e correct
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

You fit decide whether to put this parsing logic inside the tool call itself or inside the handler function.

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

- Inside handler wey dey handle all tool calls, we dey now try parse the incoming request enter the tool defined schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    if e correct then we proceed call the real tool:

    ```typescript
    const result = await tool.callback(input);
    ```

As you see, this method create better architecture because everything get its own place, the *server.ts* na small small file only to wire up the request handlers and each feature dey their own folder i.e tools/, resources/ or /prompts.

Beta, make we try build this next. 

## Exercise: Creating a low-level server

For this exercise, we go do this things:

1. Create low-level server to handle listing of tools and calling tools.
1. Implement architecture wey you go fit build more on top.
1. Add validation to make sure say your tool calls dey valid.

### -1- Create an architecture

The first thing we need na create architecture wey go help us scale as we add more features, this na how e go be:

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

Now we don set architecture make e easy to add new tools for tools folder. You fit still add subdirectories for resources and prompts.

### -2- Creating a tool

Make we see how to create tool. First, you need create am for *tool* subdirectory like this:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Check di input wit Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we fit create AddInputModel and check di args well well

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Wetin you dey see here na how we define name, description, and input schema with Pydantic and handler wey go run wen dem call the tool. We go expose `tool_add` as dictionary wey hold all these properties.

Also dem get *schema.py* wey dem use to define input schema wey our tool go use:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We need still fill *__init__.py* so tools directory go be treated as module. Plus, we need expose the modules inside am like this:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We fit continue add more tools files here as we add more tools.

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

For here, we dey create dictionary wey get these properties:

- name, na the name of tool.
- rawSchema, na the Zod schema wey dem go use validate incoming requests for this tool.
- inputSchema, this one handler go take use.
- callback, na dis one dey invoke the tool.

Dem also get `Tool` wey go convert this dictionary to type wey the mcp server handler fit accept and e look like this:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

And dem get *schema.ts* wey hold input schemas for every tool like dis one with one schema for now but as we add more tools, we fit add more entries:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Beta, make we handle listing of our tools next.

### -3- Handle tool listing

To handle listing our tools, we need setup request handler for dat. This na wetin we go add for our server file:

**Python**

```python
# code no too long so e no include
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

Here, we add decorator `@server.list_tools` plus implement function `handle_list_tools`. For the function, we need produce list of tools. Make sure say each tool get name, description and inputSchema.   

**TypeScript**

To set up request handler for listing tools, we need call `setRequestHandler` for server with schema wey fit wetin we wan do, for here na `ListToolsRequestSchema`. 

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
// Code don cut short for make am brief
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return di list of tools wey dem don register
  return {
    tools: tools
  };
});
```

Cool, now we don solve how to list tools, make we see how we fit dey call tools next.

### -4- Handle calling a tool

To call tool, we need setup another request handler, this time e go handle request wey specify which feature to call and with which arguments.

**Python**

Make we use decorator `@server.call_tool` and implement am with function like `handle_call_tool`. Inside the function, we go parse out the tool name, arguments and make sure the arguments valid for the tool. You fit validate arguments inside this function or later inside the tool.

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

Dis na wetin dey happen:

- Our tool name dey as input parameter `name` and arguments dey the form of `arguments` dictionary.

- The tool dey called with `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. The validation for arguments dey inside `handler` property wey point to function, if e no correct e go throw exception. 

So now we get full understanding of how to list and call tools using low-level server.

See the [full example](./code/README.md) here

## Assignment

Add more tools, resources and prompt for the code we give you and notice sey you only need add files inside tools directory no other place. 

*No solution given*

## Summary

For this chapter, we don see how low-level server approach work and how e fit help create beta architecture we fit continue build on top. We still talk about validation and you don see how to work with validation libraries to create schemas for input validation.

## What's Next

- Next: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na im wey AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) translate am. Even though we dey try make am correct, abeg sabi say automatic translation fit get mistakes or wahala. Di original document wey dey im own language na di real correct one. If na serious matter, e better make pesin wey sabi translate am humanly do am. We no go carry any matter wey fit show because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->