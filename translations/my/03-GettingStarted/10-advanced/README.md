# အဆင့်မြင့်ဆာဗာ အသုံးပြုခြင်း

MCP SDK တွင် ပြသထားသော ဆာဗာအမျိုးအစားနှစ်မျိုးရှိပြီး၊ သင့်ရဲ့ ပုံမှန်ဆာဗာနှင့် အနိမ့်အဆင့် ဆာဗာဖြစ်သည်။ ပုံမှန်အားဖြင့် သင်သည် ပုံမှန်ဆာဗာကို အသုံးပြု၍ အင်္ဂါရပ်များ ထည့်သွင်းပါမည်။ သို့သော်လည်း တချို့အခြေအနေများတွင် အနိမ့်အဆင့်ဆာဗာအပေါ် မူတည်ချင်သော အကြောင်းအရင်းများ ရှိနိုင်ပါသည်။

- ပိုမိုကောင်းမွန်သော ဖွဲ့စည်းတည်ဆောက်ပုံ။ ပုံမှန်ဆာဗာနှင့် အနိမ့်အဆင့် ဆာဗာ နှစ်မျိုးကိုပေါင်းစပ်ပြီး သန့်ရှင်းသောဖွဲ့စည်းတည်ဆောက်ပုံကို ဖန်တီးနိုင်သော်လည်း အနိမ့်အဆင့် ဆာဗာဖြင့် ပိုမိုလွယ်ကူတယ်လို့ ဆိုနိုင်ပါသည်။
- အင်္ဂါရပ် ရရှိနိုင်မှု။ အဆင့်မြင့် အင်္ဂါရပ်တချို့ကို အနိမ့်အဆင့် ဆာဗာဖြင့်သာ အသုံးပြုနိုင်ပါသည်။
    ပြန်ကြားပိုင်းနောက်ပိုင်းတွင် Elicitation နှင့် legacy Sampling အင်္ဂါရပ်များကို ဖေါ်ပြမည်ဖြစ်ပြီး၊ MCP `2026-07-28` တွင် မသုံးရတော့သော အင်္ဂါရပ်များ ဖြစ်သည်။


## ပုံမှန်ဆာဗာနှင့် အနိမ့်အဆင့်ဆာဗာ

ပုံမှန်ဆာဗာဖြင့် MCP ဆာဗာ တည်ဆောက်မှုကဲ့သို့ ရှိပါသည်။

**Python**

```python
mcp = FastMCP("Demo")

# ပေါင်းထည့်သည့်ကိရိယာတစ်ခုထည့်ပါ
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

// ထည့်သွင်းမှုကိရိယာတစ်ခုကို ပေါင်းထည့်ပါ
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

အဓိက အဓိပ္ပါယ်က သင် ဆာဗာတွင်ရှိသင့်သော tool, resource သို့မဟုတ် prompt တိုင်းကို တိတိကျကျ ထည့်သွင်းသည်။ ဒီမှာ ဒို့အမှားမရှိပါ။

### အနိမ့်အဆင့် ဆာဗာ နည်းလမ်း

သို့သော် အနိမ့်အဆင့် ဆာဗာကို အသုံးပြုသောအခါ သင်သည် ကွဲပြားသောတွေးခေါ်မှုများ လိုတယ်။ တစ်ခုချင်းစီ tool တစ်ခုအားလုံးကို မှတ်ပုံတင်ရန်မလိုဘဲ feature အမျိုးအစား (tools, resources, prompts) တစ်ခုချင်းစီအတွက် handler နှစ်ခု ဖန်တီးရမည်ဖြစ်သည်။ ဥပမာအားဖြင့် tool များသည် အောက်ပါအတိုင်း function နှစ်ခုသာ ရှိသည်။

- tool များ စာရင်းပြုစုခြင်း။ တစ်ခုသော function တစ်ခုက သင့်အား tool များအားလုံးကို စာရင်းပြုစုခွင့် ရရှိစေသည်။
- tool များအား ခေါ်ရန် ထိန်းချုပ်ခြင်း။ ဒီမှာလည်း function တစ်ခု သာ တာဝန်ယူသည်။

ဒီဟာတွေမှာ ကန့်သတ်တာ ပိုနည်းတာမျိုးတော့ ရှိမလား။ tool တစ်ခုကို မှတ်ပုံတင်ခြင်းမလုပ်ပဲ၊ tool များကို စာရင်းပြုစုတဲ့အခါ tool ရှိဖို့ သေချာစေပြီး tool ခေါ်တဲ့ နေ့တစ်နေ့ တောင်းဆိုမှု ရလာတဲ့အခါ ခေါ်နိုင်စေရမယ်။

အခု အောက်က code ကို ကြည့်ကြရအောင်။

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
  // မှတ်ပုံတင်ထားသောကိရိယာများစာရင်းကိုပြန်ပေးပါ
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

ဒီမှာတော့ feature များစာရင်း ပြန်ပေးသူ function ရှိသည်။ tools စာရင်း တစ်ခုချင်းစီတွင် `name`, `description` နှင့် `inputSchema` စတဲ့ အချက်အလက်များ ပါဝင်သည်။ ဒါက့ဲ့ ကျွန်ုပ်တို့၏ tools နှင့် feature ဖော်ပြချက်ကို ဒေသအသီးသီးမှာ ထားနိုင်စေသည်။ သင်တို့ tools ကို tools ဖိုလ်ဒါအတွင်းတွင် ပြုစုနိုင်ပြီး feature များလည်း ဒီလိုပဲ project ရှိ စီမံခန့်ခွဲမှု ပိုကောင်းစေမည်။

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

ဒီဟာကောင်းတယ်၊ ဖွဲ့စည်းတည်ဆောက်ပုံကို သန့်ရှင်းစေနိုင်ပြီ။

Tool များကို ခေါ်ရန် ပြောရင်လည်း ညီမျှတာပါလား၊ tool တစ်ခုကို ခေါ်တဲ့ handler တစ်ခု ရှိရုံဖြစ်တာလား? ဟုတ်တယ်၊ ဒီတော့ အောက်က code ကိုကြည့်ရအောင်:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools သည် ကိရိယာအမည်များကို key အဖြစ်သုံးသည့် dictionary တစ်ခုဖြစ်သည်။
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
    // လုပ်ရန် - ကိရိယာကိုခေါ်ပါ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

အပေါ်က code မှာကြည့်လိုက်ရင် tool ကို ဘယ် tool ကို ဘယ် argument တွေနဲ့ ခေါ်မယ်ဆိုတာ ပြန်ဖြေရှင်းနေပြီး tool ကို ခေါ်သွားရင် ထပ်ဆင့်လုပ်ဆောင်နေပါသည်။

## စနစ်တိုးတက်မှုကို သေချာစေရန် စစ်ဆေးခြင်းဖြင့် မြှင့်တင်ခြင်း

ဒီအထိပဲပြောရင် tool, resource နှင့် prompt တွေ စာရင်းထဲမှာ အဲဒီ handler နှစ်ခုနဲ့ အစားထိုးနိုင်ပြီ။ တခြား ဘာလုပ်ရန်လိုသလဲ? အဲဒါကတော့ tool ကို ဖုန်းခေါ်တဲ့ argument တွေ မှန်ကန်ကြောင်း သေချာစေရန် စစ်ဆေးမှု(Validation) လုပ်သင့်ပါတယ်။ runtime တစ်ခုချင်းစီမှာ ပုံမှန်နည်းလမ်းရှိပြီး၊ ဥပမာ Python မှာ Pydantic ကို သုံးပြီး TypeScript မှာ Zod ကို သုံးသည်။ အဓိကမှာ အောက်ပါအတိုင်းလုပ်သည်။

- feature (tool, resource, prompt) ဖန်တီးရာ logic ကို ဒေသခံဖိုလ်ဒါတစ်ခုထဲသို့ ရွှေ့မည်။
- tool ကို ဖုန်းခေါ်တဲ့ requesting စစ်ဆေးမှုတစ်ခု ရှိရမည်။

### feature တစ်ခု ဖန်တီးခြင်း

feature ဖန်တီးရန် ဟာ feature အတွက် လိုအပ်သော အချက်အလက်များပါဝင်သင့်သည်။ tool, resource, prompt များအတွက် လိုအပ်ချက်က တခါတရံကွဲလွဲနိုင်သည်။

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
        # Pydantic မော်ဒယ်ကို အသုံးပြု၍ အထောက်အထား စစ်ဆေးပါ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ကို ထည့်သွင်းပြီး AddInputModel ကို ဖန်တီးနိုင်ရန်နှင့် args များကို စစ်ဆေးနိုင်ရန်လုပ်ဆောင်ရန်

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ဒီမှာ မည်သို့လုပ်ထားသည်ကို ကြည့်ပါ။

- Pydantic `AddInputModel` ကို အသုံးပြုပြီး schema ကို *schema.py* ဖိုင်ထဲတွင် ဖန်တီးသည်၊ field တွေမှာ `a` နှင့် `b` ပါဝင်သည်။
- အဝင်တောင်းဆိုမှုကို `AddInputModel` အမျိုးအစားအဖြစ်  ကြိုးစား parse လုပ်သည်၊ parameter မကိုက်ညီလျှင် crash ဖြစ်မည်။

   ```python
   # add.py
    try:
        # Pydantic မော်ဒယ်ကို အသုံးပြု၍ အင်ပုတ်ကို စစ်ဆေးပါ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Parsing logic ကို tool ခေါ်မှုတွင်းတွင် ထည့်နိုင်သည်၊ သို့မဟုတ် handler function အတွင်း ထည့်နိုင်သည်။

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

- tool ခေါ်မှုအားလုံးကို ကိုင်တွယ်သော handler မှာ လာသောတောင်းဆိုမှုကို tool ၏ schema ဖြင့် ပြန် parse လုပ်ရန် ကြိုးစားနေသည်။

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    အကယ်၍ အလုပ်လုပ်တယ်ဆိုရင် tool ကို တကယ်ခေါ်ရန် ဆက်လက်တည်ဆောက်မည့်အခြေအနေဖြစ်သည်။

    ```typescript
    const result = await tool.callback(input);
    ```

ဒီနည်းလမ်းက ဖွဲ့စည်းတည်ဆောက်ပုံကို ကောင်းမွန်စေရန် အထောက်အကူ ဖြစ်ပြီး `server.ts` ကတော့ အလွန်သေးသော ဖိုင်တစ်ခုဖြစ်ပြီး တောင်းဆိုမှု handler ကိုပဲ ကွန်ယက်ဆက်ထားသည်။ feature အားလုံးကို သူ့ရဲ့ ဒေသခံ ဖိုလ်ဒါတွင် ထားသည်။ tools/, resources/ သို့မဟုတ် prompts/ များစွာလည်း ထောက်ပံ့သည်။

အဆင်ပြေပြီ၊ ဒါကို လုပ်ဆောင်ကြည့်ရအောင်။

## လေ့ကျင့်မှု: အနိမ့် အဆင့် ဆာဗာ ဖန်တီးခြင်း

ဒီလုပ်ငန်းမှာ အောက်ပါအရာများ ပြုလုပ်ပါမည်။

1. tool များ စာရင်းပြုစုခြင်းနှင့် tool ခေါ်ခြင်း ကို ကိုင်တွယ်သည့် အနိမ့် အဆင့် ဆာဗာ တစ်ခု ဖန်တီးပါ။
1. တီထွင်နိုင်သော ဖွဲ့စည်းတည်ဆောက်ပုံ တစ်ခု ကို အကောင်အထည်ဖော်ပါ။
1. tool ခေါ်မှုများ မှန်ကန်စွာ စစ်ဆေးမှု ပေါင်းထည့်ပါ။

### -1- ဖွဲ့စည်းတည်ဆောက်ပုံ ဖန်တီးခြင်း

ပထမဦးဆုံး ဖြေရှင်းရန်လိုအပ်တာကတော့ feature ပိုများလာသည့်အခါ အဆင်ပြေစေရန် architecture ဖြစ်သည်။ အောက်မှာ ပုံစံရိုက်ပြထားသည်။

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

ယခုမှာ tools ဖိုလ်ဒါအတွင်း tool အသစ်များ ထည့်သွင်းလွယ်ကူသည့် architecture တည်ဆောက်ပြီး ဖြစ်သည်။ resources နှင့် prompts အတွက် subdirectories ဖန်တီးရန် လိုလျှင် လိုက်နာနိုင်ပါသည်။

### -2- tool တစ်ခု ဖန်တီးခြင်း

tool ဖန်တီးရာတွင် အရင်ဆုံး *tool* subdirectory ထဲတွင် ဖန်တီးရမည်၊ အောက်ပါအတိုင်းဖြစ်သည်။

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic မော်ဒယ်ကို အသုံးပြုပြီး အကဲဖြတ်ပါ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ထည့်ပါ၊ ထိုနောက် AddInputModel တစ်ခု ဖန်တီးပြီး args များကို အကဲဖြတ်နိုင်ပါစေ

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ဒီမှာ name, description နှင့် input schema ကို Pydantic ဖြင့် သတ်မှတ်ထားပြီး tool တစ်ခုခေါ်သောအခါ ခေါ်ဆောင်မည့် handler ကိုလည်း ထည့်ထားပါသည်။ နောက်ဆုံးရလဒ်အနေဖြင့် `tool_add` ဆိုသော dictionary ကို ပြသထားသည်။

*schema.py* ကိုလည်း tools အတွက် input schema သတ်မှတ်ရာတွင် အသုံးပြုသည်။

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

tools directory ကို module အဖြစ် သတ်မှတ်ရန် *__init__.py* ထည့်သွင်းပြီး modules များကို ပြသရန် လိုအပ်သည်။

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

tools များ ထပ်မံဖန်တီးတိုင်း ဒီဖိုင်ကို ဆက်လက်တိုးချဲ့နိုင်ပါသည်။

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

ဒီမှာ properties ပါရှိတဲ့ dictionary တစ်ခု ဖန်တီးထားသည်။

- name၊ tool အမည်ဖြစ်သည်။
- rawSchema၊ tool ခေါ်သည့်တောင်းဆိုမှုများကို စစ်ဆေးရန် သုံးသော Zod schema ဖြစ်သည်။
- inputSchema၊ handler မှ အသုံးပြုခြင်းခံ schema ဖြစ်သည်။
- callback၊ tool ကို ခေါ်ရန် သုံးသည်။

mcp server handler မှ လက်ခံနိုင်စေရန် ဒီ dictionary ကို type တွေသို့ ပြောင်းရန် `Tool` ကိုလည်း ရေးထားသည်။

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* တွင် tools များအတွက် input schema များ ထားရှိပြီး၊ လက်ရှိမှာ schema တစ်ခုသာ ရှိသော်လည်း tools များထပ်မံဖြည့်စွက်နိုင်သည်။

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ကောင်းပါပြီ၊ tools စာရင်းဆွဲခြင်းကို အောက်တွင် ဆက်လက်ဆောင်ရွက်ကြမည်။

### -3- tools စာရင်း ကိုင်တွယ်

tools များစာရင်းကိုင်တွယ်ရန် server ဖိုင်တွင် တောင်းဆိုမှု handler တစ်ခု သတ်မှတ်ရမည်။ အောက်က code ကို server ဖိုင်ထဲ သွင်းပါ။

**Python**

```python
# အတိုချုံးရေးရန် ကုဒ်ကို ဖယ်ရှားထားသည်။
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

decorator `@server.list_tools` နှင့် function `handle_list_tools` ကို ထည့်ထားသည်။ အဆိုပါ function တွင် tools စာရင်း ထုတ်ပေးရမည် ဖြစ်ပြီး tool တစ်ခုချင်းစီတွင် name, description နှင့် inputSchema ရှိရမည်။

**TypeScript**

tools များ စာရင်းတောင်းခံရန် request handler တည်ဆောက်ရာ server တွင် `setRequestHandler` ကို သုံးပြီး schema အနေဖြင့် `ListToolsRequestSchema` သတ်မှတ်ပါ။

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
// ပြောဆိုရန် က short-cut code ကို ဖျောက်ထားသည်
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // မှတ်ပုံတင်ထားသော ကိရိယာများစာရင်းကို ရှာဖွေ ပြန်ပေးရန်
  return {
    tools: tools
  };
});
```

ကောင်းပြီး tools စာရင်း ဆွဲခြင်းအပိုင်း ဖြေရှင်းပြီးနောက်၊ tool များကို ခေါ်ချင်သည်ကို ကြည့်ရအောင်။

### -4- tool ခေါ်မှု ကိုင်တွယ်

tool ခေါ်ရန် request handler နှင့် သက်ဆိုင်သော feature ကို တင်ပြပြီး argument များ ဖြင့် ဆောင်ရွက်မည့် handler တစ်ခု စီစဉ်ရမည်။

**Python**

decorator `@server.call_tool` ကို အသုံးပြုပြီး function `handle_call_tool` မှာ tool အမည်၊ argument ကို parse လုပ်ရန် နှင့် argument များ မှန်ကန်မှန်းစစ်ဆေးရန် လိုအပ်သည်။ argument များကို ဒီ function ထဲမှာ သို့မဟုတ် အသုံးပြု tool ထဲမှာ စစ်ဆေးနိုင်သည်။

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools သည် ကိရိယာအမည်များကို key များအဖြစ် သုံးထားသော dictionary ဖြစ်သည်
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ကိရိယာကို ခေါ်ယူပါ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

ကျွန်ုပ်တို့တွင် ဖြစ်ပေါ်နေသည့် အချက်အလက်များမှာ -

- tool အမည် `name` parameter အဖြစ် ပေးထားပြီး၊ argument များက `arguments` dictionary အဖြစ် ရှိသည်။

- tool ကို `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ဖြင့်ခေါ်ခြင်း၊ argument များစစ်ဆေးမှုကို handler function တွင် ပြုလုပ်ပြီး မအောင်မြင်လျှင် error ပြလိမ့်မည်။

ဒါဆိုတော့ အနိမ့်အဆင့် ဆာဗာကို အဓိကအသုံးပြု၍ tools စာရင်းဆွဲခြင်းနှင့် tool ခေါ်ခြင်း ကျွမ်းကျင်စွာ သိရှိသွားပါပြီ။

ဒီမှာ [Full example](./code/README.md) ကို ကြည့်ရှုနိုင်ပါသည်။

## တာဝန်

ပေးထားသော code ကို ဖြည့်စွက်ကာ tools, resources နှင့် prompt များ တိုးမြှင့်ပြီး tools directory ထဲတွင်ဖိုင်ဖြစ်ရုံပဲ တခြားအနေဖြင့် ဖိုင်များ မလိုအပ်ကြောင်း တွေ့ရှိအပေါ် မှတ်ယူပါ။

*ဖြေရှင်းချက် မပေးပါ*

## အကျဉ်းချုပ်

ဒီအခန်းတွင် အနိမ့်အဆင့် ဆာဗာနည်းလမ်းနှင့် မည်သို့ အဆင့်မြင့် ဖွဲ့စည်းတည်ဆောက်ပုံကို ဖန်တီးနိုင်သလဲဟု မြင်တွေ့ခဲ့ပြီး၊ validation ပြုလုပ်ခြင်းနှင့် validation လိုက်ဘ်ရေရီများကို အသုံးပြု၍ input စစ်ဆေးအချက်အလက်များ ဖန်တီးခြင်းကို ရှင်းပြခဲ့သည်။

## နောက်တစ်ခုမှာ ဘာလဲ

- နောက်ထပ်: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->