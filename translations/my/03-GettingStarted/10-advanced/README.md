# အဆင့်မြင့် server အသုံးပြုမှု

MCP SDK မှာ server နှစ်မျိုးရှိပါတယ်၊ သင့်ရိုးရိုး server နဲ့ low-level server ပါ။ သာမန်အားဖြင့် သင့်ရိုးရိုး server ကို အသုံးပြုပြီး feature တွေထည့်သွင်းနိုင်ပါတယ်။ သို့သော် အချို့သောအခြေအနေများတွင် low-level server ကို အောက်ပါအတိုင်း အသုံးပြုလိုတတ်ပါတယ်-

- Architecture ပိုမိုကောင်းမွန်မှု။ Regular server နဲ့ low-level server နှစ်ခုလုံးကို အသုံးပြုပြီး သန့်ရှင်းသော architecture တည်ဆောက်နိုင်ပေမယ့် low-level server နဲ့ ပိုမိုလွယ်ကူတတ်ပါတယ်။
- Feature ရရှိနိုင်မှု။ အချို့သော အဆင့်မြင့် feature တွေကို low-level server နဲ့သာ အသုံးပြုနိုင်ပါတယ်။ နောက်ပိုင်း chapter တွေမှာ sampling နဲ့ elicitation တွေထည့်သွင်းတဲ့အခါမှာ ဒီအကြောင်းကို တွေ့ရပါမယ်။

## Regular server နဲ့ low-level server

MCP Server ကို regular server နဲ့ ဖန်တီးတဲ့နည်းလမ်းက ဒီလိုပုံစံရှိပါတယ်-

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

ဒီမှာ အဓိကက server ရဲ့ tool, resource, prompt တစ်ခုချင်းစီကို ထည့်သွင်းဖို့ explicitly လုပ်ရပါတယ်။ ဒီနည်းလမ်းမှာ ဘာမှမမှားပါဘူး။

### Low-level server နည်းလမ်း

သို့သော် low-level server နည်းလမ်းကို အသုံးပြုတဲ့အခါ feature type (tools, resources, prompts) တစ်ခုချင်းစီအတွက် handler နှစ်ခုဖန်တီးရမယ်ဆိုတာကို အဓိကထားပြီး အခြားနည်းလမ်းနဲ့ ဆင်တူမဟုတ်ပါဘူး။ Tools ကို ဥပမာပြရမယ်ဆိုရင် handler နှစ်ခုသာလိုအပ်ပါတယ်-

- Tools အားလုံးကို စာရင်းပြုစုခြင်း။ Tools စာရင်းပြုစုဖို့ function တစ်ခုသာလိုအပ်ပါတယ်။
- Tools အားလုံးကို ခေါ်ယူခြင်း။ Tools ကို ခေါ်ယူဖို့ function တစ်ခုသာလိုအပ်ပါတယ်။

ဒီနည်းလမ်းက အလုပ်ပိုမိုလျော့နည်းတတ်ပါတယ်လို့ ထင်ရပါတယ်။ Tool တစ်ခုချင်းစီကို register လုပ်ရမယ့်အစား tool ကို စာရင်းထဲမှာ ထည့်သွင်းပြီး request ရောက်လာတဲ့အခါ tool ကို ခေါ်ယူနိုင်ဖို့ သေချာစေဖို့သာ လိုအပ်ပါတယ်။

အခု code ပုံစံကို ကြည့်လိုက်ရအောင်-

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

ဒီမှာ feature တွေကို စာရင်းပြုစုတဲ့ function တစ်ခုရှိပါတယ်။ Tools စာရင်းထဲက entry တစ်ခုချင်းစီမှာ `name`, `description`, `inputSchema` field တွေပါဝင်ဖို့လိုအပ်ပါတယ်။ ဒီနည်းလမ်းက tools နဲ့ feature တွေကို project ရဲ့ tools folder မှာ သီးသန့်ထားနိုင်စေပြီး project ကို အလှပဆုံး organization လုပ်နိုင်ပါတယ်။

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

ဒီလိုနည်းလမ်းက architecture ကို သန့်ရှင်းစေပါတယ်။

Tools ကို ခေါ်ယူတဲ့အခါမှာလည်း handler တစ်ခုသာလိုအပ်ပါတယ်။ Tools တစ်ခုချင်းစီကို handler တစ်ခုတည်းနဲ့ ခေါ်ယူနိုင်ပါတယ်။ အောက်မှာ code ကို ကြည့်လိုက်ရအောင်-

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

အထက်က code မှာ tool ကို ခေါ်ယူဖို့ tool နဲ့ arguments ကို parse လုပ်ပြီး tool ကို ခေါ်ယူရပါတယ်။

## Validation ဖြင့် နည်းလမ်းတိုးတက်စေခြင်း

Tools, resources, prompts တွေကို register လုပ်တဲ့အစား feature type တစ်ခုချင်းစီအတွက် handler နှစ်ခုသာ အသုံးပြုနိုင်တဲ့နည်းလမ်းကို သင်တွေ့မြင်ခဲ့ပါပြီ။ အခုတော့ tool ကို မှန်ကန်သော arguments နဲ့ ခေါ်ယူဖို့ validation တစ်ခုထည့်သွင်းဖို့လိုအပ်ပါတယ်။ Runtime တစ်ခုချင်းစီမှာ validation solution ကို အသုံးပြုနိုင်ပါတယ်၊ ဥပမာ Python မှာ Pydantic ကို အသုံးပြုပြီး TypeScript မှာ Zod ကို အသုံးပြုပါတယ်။ အဓိကမှာ အောက်ပါအတိုင်းလုပ်ရပါမယ်-

- Feature (tool, resource, prompt) တစ်ခုဖန်တီးဖို့ သီးသန့် folder တစ်ခုမှာ logic ကို ရွှေ့ထားပါ။
- Request ရောက်လာတဲ့အခါ validation logic ကို ထည့်သွင်းပါ။

### Feature တစ်ခုဖန်တီးခြင်း

Feature တစ်ခုဖန်တီးဖို့ feature ရဲ့ mandatory fields တွေပါဝင်တဲ့ file တစ်ခုဖန်တီးရပါမယ်။ Tools, resources, prompts တစ်ခုချင်းစီမှာ fields မတူညီနိုင်ပါတယ်။

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

ဒီမှာ အောက်ပါအတိုင်းလုပ်ဆောင်ထားပါတယ်-

- *schema.py* file မှာ Pydantic `AddInputModel` ကို အသုံးပြုပြီး `a` နဲ့ `b` field တွေပါဝင်တဲ့ schema တစ်ခုဖန်တီးထားပါတယ်။
- Incoming request ကို `AddInputModel` type ဖြစ်ဖို့ parse လုပ်ဖို့ ကြိုးစားထားပါတယ်၊ parameter မကိုက်ညီရင် crash ဖြစ်နိုင်ပါတယ်။

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Parsing logic ကို tool call ထဲမှာပဲ ထည့်သွင်းနိုင်သလို handler function ထဲမှာလည်း ထည့်သွင်းနိုင်ပါတယ်။

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

- Tool call တွေကို handle လုပ်တဲ့ handler မှာ incoming request ကို tool ရဲ့ schema နဲ့ parse လုပ်ဖို့ ကြိုးစားထားပါတယ်။

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    အဲဒါအောင်မြင်ရင် tool ကို ခေါ်ယူဖို့ ဆက်လုပ်ပါ။

    ```typescript
    const result = await tool.callback(input);
    ```

ဒီနည်းလမ်းက architecture ကို အလှပဆုံးဖန်တီးနိုင်ပါတယ်၊ *server.ts* file က request handler တွေကို wire up လုပ်ဖို့သာ အသုံးပြုပြီး feature တစ်ခုချင်းစီကို tools/, resources/, prompts/ folder တွေမှာ သီးသန့်ထားနိုင်ပါတယ်။

အခုတော့ ဒီနည်းလမ်းကို လက်တွေ့လုပ်ဆောင်ကြည့်ရအောင်။

## လေ့ကျင့်ခန်း: Low-level server တစ်ခုဖန်တီးခြင်း

ဒီလေ့ကျင့်ခန်းမှာ အောက်ပါအတိုင်းလုပ်ဆောင်ပါမယ်-

1. Tools စာရင်းပြုစုခြင်းနဲ့ tools ခေါ်ယူခြင်းကို handle လုပ်တဲ့ low-level server တစ်ခုဖန်တီးပါ။
1. Architecture တစ်ခုတည်ဆောက်ပြီး feature တွေထည့်သွင်းနိုင်အောင်လုပ်ပါ။
1. Tool call တွေကို မှန်ကန်စွာ validate လုပ်နိုင်ဖို့ validation ထည့်သွင်းပါ။

### -1- Architecture တစ်ခုဖန်တီးခြင်း

Feature တွေကို ပိုမိုထည့်သွင်းနိုင်အောင် architecture တစ်ခုဖန်တီးရမယ်၊ ဒီလိုပုံစံရှိပါတယ်-

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

အခုတော့ tools folder ထဲမှာ tools အသစ်တွေကို အလွယ်တကူထည့်သွင်းနိုင်တဲ့ architecture တစ်ခုဖန်တီးထားပါပြီ။ Resources နဲ့ prompts အတွက် subdirectories တွေထည့်သွင်းနိုင်ပါတယ်။

### -2- Tool တစ်ခုဖန်တီးခြင်း

Tool တစ်ခုဖန်တီးတဲ့နည်းလမ်းကို ကြည့်လိုက်ရအောင်။ Tool ကို *tool* subdirectory ထဲမှာ ဖန်တီးရပါမယ်-

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

ဒီမှာ tool ရဲ့ name, description, input schema ကို Pydantic နဲ့ define လုပ်ထားပြီး tool ကို ခေါ်ယူတဲ့ handler ကို ဖန်တီးထားပါတယ်။ နောက်ဆုံးမှာ `tool_add` dictionary ကို expose လုပ်ထားပါတယ်။

*schema.py* file မှာ tool ရဲ့ input schema ကို define လုပ်ထားပါတယ်-

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Tools directory ကို module အဖြစ်သတ်မှတ်ဖို့ *__init__.py* ကို populate လုပ်ရပါမယ်။ Tools အသစ်တွေထည့်သွင်းတဲ့အခါ ဒီ file ကို update လုပ်နိုင်ပါတယ်-

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

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

ဒီမှာ dictionary တစ်ခုဖန်တီးထားပြီး properties တွေပါဝင်ပါတယ်-

- name, tool ရဲ့ name ဖြစ်ပါတယ်။
- rawSchema, Zod schema ဖြစ်ပြီး incoming request တွေကို validate လုပ်ဖို့ အသုံးပြုပါတယ်။
- inputSchema, handler မှာ အသုံးပြုမယ့် schema ဖြစ်ပါတယ်။
- callback, tool ကို invoke လုပ်ဖို့ အသုံးပြုပါတယ်။

`Tool` ကို MCP server handler က accept လုပ်နိုင်တဲ့ type အဖြစ် convert လုပ်ဖို့ အသုံးပြုပါတယ်-

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* file မှာ tool ရဲ့ input schemas တွေကို သိမ်းထားပါတယ်၊ tool တစ်ခုသာရှိပေမယ့် tools အသစ်တွေထည့်သွင်းတဲ့အခါ entry တွေကို ထပ်ထည့်နိုင်ပါတယ်-

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

အခုတော့ tools စာရင်းပြုစုခြင်းကို handle လုပ်ဖို့ ဆက်လုပ်ဆောင်ရအောင်။

### -3- Tools စာရင်းပြုစုခြင်းကို handle လုပ်ခြင်း

Tools စာရင်းပြုစုဖို့ request handler တစ်ခုကို server file မှာ ထည့်သွင်းရပါမယ်-

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

ဒီမှာ `@server.list_tools` decorator နဲ့ `handle_list_tools` function ကို အသုံးပြုထားပါတယ်။ Tools စာရင်းကို ထုတ်ပေးဖို့ function ထဲမှာ logic ထည့်သွင်းထားပါတယ်။ Tool တစ်ခုချင်းစီမှာ name, description, inputSchema ပါဝင်ဖို့လိုအပ်ပါတယ်။

**TypeScript**

Tools စာရင်းပြုစုဖို့ request handler ကို setRequestHandler function ကို server မှာ call လုပ်ရပါမယ်၊ ဒီမှာ `ListToolsRequestSchema` ကို အသုံးပြုထားပါတယ်-

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

အခုတော့ tools စာရင်းပြုစုခြင်းကို ပြီးမြောက်ပါပြီ၊ tools ကို ခေါ်ယူဖို့ နည်းလမ်းကို ဆက်လက်ကြည့်လိုက်ရအောင်။

### -4- Tool တစ်ခုခေါ်ယူခြင်းကို handle လုပ်ခြင်း

Tool တစ်ခုခေါ်ယူဖို့ request handler တစ်ခုကို ထည့်သွင်းရပါမယ်၊ feature ကို ခေါ်ယူဖို့ request နဲ့ arguments ကို handle လုပ်ရပါမယ်။

**Python**

`@server.call_tool` decorator ကို အသုံးပြုပြီး `handle_call_tool` function ကို implement လုပ်ရပါမယ်။ Function ထဲမှာ tool name, arguments ကို parse လုပ်ပြီး arguments တွေကို validate လုပ်ရပါမယ်။ Validation ကို function ထဲမှာပဲ လုပ်နိုင်သလို tool ထဲမှာလည်း လုပ်နိုင်ပါတယ်။

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

ဒီမှာ အောက်ပါအတိုင်းလုပ်ဆောင်ထားပါတယ်-

- Tool name ကို input parameter `name` အနေနဲ့ ရရှိထားပြီး arguments ကို dictionary အနေနဲ့ ရရှိထားပါတယ်။
- Tool ကို `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` နဲ့ ခေါ်ယူထားပါတယ်။ Arguments validation ကို `handler` property ထဲမှာ လုပ်ထားပါတယ်၊ မအောင်မြင်ရင် exception ဖြစ်နိုင်ပါတယ်။

ဒီနည်းလမ်းနဲ့ low-level server ကို အသုံးပြုပြီး tools စာရင်းပြုစုခြင်းနဲ့ tools ခေါ်ယူခြင်းကို အပြည့်အစုံနားလည်နိုင်ပါပြီ။

[full example](./code/README.md) ကို ဒီမှာကြည့်ပါ။

## အလုပ်ပေးစာ

Tools, resources, prompts အများအပြားကို code ထဲမှာ ထည့်သွင်းပြီး tools directory ထဲမှာသာ file တွေထည့်သွင်းရတဲ့အကြောင်းကို သုံးသပ်ပါ။

*ဖြေရှင်းချက်မပေးထားပါ*

## အကျဉ်းချုပ်

ဒီ chapter မှာ low-level server နည်းလမ်းက ဘယ်လိုအလုပ်လုပ်သလဲဆိုတာနဲ့ သန့်ရှင်းသော architecture တစ်ခုကို တည်ဆောက်နိုင်တဲ့နည်းလမ်းကို လေ့လာခဲ့ပါတယ်။ Validation ကိုလည်း ဆွေးနွေးပြီး input validation အတွက် schema တွေဖန်တီးဖို့ validation libraries တွေကို အသုံးပြုနည်းကို ပြသခဲ့ပါတယ်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။