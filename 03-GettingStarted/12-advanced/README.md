# Advanced server usage

There are two different types of servers exposes in the MCP SDK, your normal server and the low-level server. Normally, you would use the regular server to add features to it. For some cases though, you want to rely on the low-level server such as:

- Better architecture. It's possible to create a clean architecture with both the regular server and a low-level server but it can be argued that it's slightly easier with a low-level server.
- Feature avavailability. Some advanced features can only be used with a low-level server. Youiwill see this in later chapters as we add sampling and elicitation.

## Regular server vs low-level server

Here's what the creation of an MCP Server looks like with the regular server

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

The point being is that you explicitly add each tool, resource or prompt that you want the server to have. Nothing wrong with that.  

### Low-level server approach

However, when you use the low-level server approach you need to think about differently namely that instead of registering each tool you instead create two handlers per feature type (tools, resources or prompts). So for example tools then only have two functions like so:

- Listing all tools. One function would be responsible for all attempts to list tools.
- handle calling all tools. Here also, there's only one function handling calls to a tool

That sounds like potentially less work right? So instead of registering a tool, I just need to make sure the tool is listed when I list all tools and that's it's called when there's an incoming request to call a tool. 

Let's have a look at how the code now looks:

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

Here we now have a function that returns a list of features. Each entry in the tools list now have fields like `name`, `description` and `inputSchema` to adhere to the return type. This enables us to put our tools and feature definition elsewhere. We can now create all our tools in a tools folder and the same goes for all your features so your project can suddenly be organized like so:

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

That's great, our architecture can be made to look quite clean.

What about calling tools, is it the same idea then, one handler to call a tool, whichever tool? Yes, exactly, here's the code for that:

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
        result = await tool["handler"](arguments)
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

As you can see from above code, we need to parse out the tool to call, and with what arguments, and then we need to proceed to calling the tool.

## Improving the approach with validation

So far, you've seen how all your registrations to add tools, resources and prompts can be replaced with these two handlers per feature type. What else do we need to do? Well, we should add some form of validation to ensure that the tool is called with right arguments. Each runtime have their own solution for this, for example Python uses Pydantic and TypeScript uses Zod. The idea is that we do the following:

- Move the logic for creating a feature (tool, resource or prompt) to its dedicated folder.
- Add a way to validate an incoming request asking to for example call a tool.

### Create a feature

To create a feature, we will need to create a file for that feature and make sure it has the mandatory fields requred of that feature. Which fields differ a bit between tools, resources and prompts.

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

here you can see how we do the following:

- Create a schema using Pydantic `AddInputModel` with fields `a` and `b` in file *schema.py*.
- Attempt to parse the incoming request to be of type `AddInputModel`, if there's a mismatch in parameters this will crash:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

You can choose whether to put this parsing logic in the tool call itself or in the handler function.

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

- In the handler dealing with all tool calls, we now try to parse the incoming request into the tool's defined schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    if that works then we proceed to call the actual tool:

    ```typescript
    const result = await tool.callback(input);
    ```

As you can see, this approach creates a great architecture as everything has it's place, the *server.ts* is a very small file that only wires up th request handlers and each features is in their respective folder i.e tools/, resources/ or /prompts.

Great, let's try to build this next. 

## Exercise: Creating a low-level server

In this exercise, we will do the following:

1. Create a low-level server handling listing of tools and calling of tools.
1. Implement an architecture you can build upon.
1. Add validation to ensure your tool calls are properly validated.

### -1- Create an architecture

The first thing we need to address is an architecture that helps us scale as we add more features, here's what it looks like:

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

Now we have set up in architecture that ensures we can easily add new tools in a tools folder. Feel free to follow this to add subdirectories for resources and prompts.

### -2- Creating a tool

Let's see what creating a tool looks like next. First, it needs to be created in its *tool* subdirectory like so:

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

What we se here is how we define name, description, an input schema using Pydantic and a handler that will be invoked once this tool is being called. Lastly, we expose `tool_add` which is a dictionary holding all these properties.

There's also *schema.py* that's used to define the input schema used by our tool:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We also need to populate *__init__.py* to ensure the tools directory is treated as a module. Additionally, we need to expose the modules within it like so:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We can keep adding to this file as we add more tools.

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

Here we create a dictionary consisting of properties:

- name, this is the name of the tool.
- rawSchema, this is the Zod schema, it will be used to validate incoming requests to call this tool.
- inputSchema, this schema will be used by the handler.
- callback, this is used to invoke the tool.

There' also `Tool` that's used to convert this dictionary into a type the mcp server handler can accept and it looks like so:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

And there's *schema.ts* where we store the input schemas for each tool that looks like so with only one schema at present but as we add tools we can add more entries:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Great, let's procced to handle the listing of our tools next.

### -3- Handle tool listing

Next, to handle listing our tools, we need to set up a request handler for that. Here's what we need to add to our server file:

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

Here' we add the decorator `@server.list_tools` and the implementing function `handle_list_tools`. In the latter, we need to produce a list of tools. Note how each tool needs to have a name, description and inputSchema.   

**TypeScript**

To set up the request handler for listing tools, we need to call `setRequestHandler` on the server with a schema fitting what we're trying to do, in this case `ListToolsRequestSchema`. 

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

Great, now we have solved the piece of listing tools, let's look at how we could be calling tools next.

### -4- Handle calling a tool

To call a tool, we need set up another request handler, this time focused on dealing with a request specifying which feature to call and with what arguments.

**Python**

Let's use the decorator `@server.call_tool` and implement it with a function like `handle_call_tool`. Within that function, we need to parse out the tool name, its argument and ensure the arguments are valid for the tool in question. We can either validate the arguments in this function or downstream in the actual tool.

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
        result = await tool["handler"](arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Here's what goes on:

- Our tool name is already present as the input parameter `name` which is true for our arguments in the form of the `arguments` dictionary.

- The tool is called with `result = await tool["handler"](arguments)`. The validation of the arguments happens in the `handler` property which points to a function, if that fails it will raise an exception. 

There, now we have a full understanding of listing and calling tools using a low-level server.

See the [full example](./code/README.md) here

## Assignment

Extend the code you've been given with a number of tools, resources and prompt and reflect over how you notice that you only need to add files in tools directory and nowhere else. 

*No solution given*

## Summary

In this chapter, we saw how low-level server approach worked and how that can help us create a nice architecture we can keep building on. We also discussed validation and you were shown how to work with validation libraries to create schemas for input validation.