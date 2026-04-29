# အဆင့်မြင့်ဆာဗာအသုံးပြုမှု

MCP SDK တွင် ထွက်ရှိထားသော ဆာဗာနှစ်မျိုးရှိသည်၊ သင်၏ပုံမှန်ဆာဗာနှင့် အနိမ့်အဆင့်ဆာဗာ ဖြစ်သည်။ ပုံမှန်အားဖြင့် သင်သည် ပုံမှန်ဆာဗာကို အသုံးပြု၍ လက္ခဏာများ ထည့်သွင်းပါမည်။ သို့သော် အချို့သောအခြေအနေများတွင် အနိမ့်အဆင့်ဆာဗာကို အခြေခံလိုသည့်အခါများရှိပါသည်၊ ဥပမာ -

- ပိုမိုကောင်းမွန်သော वास्तुकला။ ပုံမှန်ဆာဗာနှင့်အတူ အနိမ့်အဆင့်ဆာဗာကို တွဲဖက်၍ သန့်ရှင်းသော वास्तुकला တည်ဆောက်နိုင်သော်လည်း အနိမ့်အဆင့်ဆာဗာဖြင့် ပိုမိုလွယ်ကူကြောင်း ဆိုနိုင်ပါသည်။
- လက္ခဏာရရှိနိုင်မှု။ အဆင့်မြင့်လက္ခဏာတချို့မှာ အနိမ့်အဆင့် ဆာဗာကိုသာ အသုံးပြုနိုင်သည်။ သင်သည် နောက်ထပ်အခန်းများတွင် sampling နှင့် elicitation ထည့်သွင်းသည့်အခါ၌ ဤကိစ္စကို မြင်ရလိမ့်မည်။

## ပုံမှန်ဆာဗာ နှင့် အနိမ့်အဆင့်ဆာဗာ ဆန့်ကျင်ဘက်

ပုံမှန်ဆာဗာဖြင့် MCP ဆာဗာ တည်ဆောက်ခြင်းသည် ဤလိုပုံစံဖြစ်သည်

**Python**

```python
mcp = FastMCP("Demo")

# ပေါင်းထည့်ရန်ကိရိယာတစ်ခု ထည့်ပါ
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

// ပေါင်းထည့်သည့်ကိရိယာတစ်ခု ထည့်ပါ
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

အဓိကအချက်မှာ သင်သည် ဆာဗာတွင် ပါဝင်စေရန် လိုသော tool, resource သို့မဟုတ် prompt တစ်ခုချင်းစီကို လက်တွေ့ထည့်သွင်းရပါသည်။ ၎င်းအပေါ် မလိုလားဘဲ ရှိသည်။

### အနိမ့်အဆင့်ဆာဗာနည်းဗျူဟာ

သို့သော် အနိမ့်အဆင့်ဆာဗာနည်းလမ်းကို အသုံးပြုသောအခါ သင့်တွင် ထူးခြားသောအတွေးအခေါ်ရှိရမည်။ တစ်ခုချင်း tool ကို မှတ်ပုံတင်ခြင်းမပြုဘဲ တစ်မျိုးတည်း feature အမျိုးအစားစီ (tools, resources သို့မဟုတ် prompts) အတွက် handler နှစ်ခုကို ဖန်တီးရမည်ဖြစ်သည်။ ဥပမာ tools အတွက် အောက်ပါ function နှစ်ခုသာ ရှိငြိမ်မည် –

- tools အားလုံး စာရင်းပြုစုခြင်း။ tools စာရင်းအား ပြုစုဖော်ပြရန် တာဝန်ယူသော function တစ်ခုရှိမည်။
- tools ကို ခေါ်ဆိုခြင်းကို ကောင်းမွန်စွာ ကိုင်တွယ်ခြင်း။ ဤနေရာတွင်လည်း tool စစ်ဆေးမှုများကို ကောင်းမွန်စွာ ကိုင်တွယ်အပ်သော function တစ်ခုသာရှိမည်။

ဤကိစ္စသည် ပိုမိုလျော့နည်းသော အလုပ်ဖြစ်နိုင်သည်ဟု ထင်ကျွံပါသလား? ထို့ကြောင့် tool တစ်ခုစီကို မှတ်ပုံတင်ခြင်းမပြုဘဲ tool အားလုံး စာရင်းထဲ ပါဝင်စေရန် အာမျိုးသေချာစေရန်နှင့် call လုပ်ရန် လာသော တောင်းဆိုမှုပေါ် မူတည်၍ tool ကို ခေါ်ဆိုခြင်းကိုသာ သေချာစွာ ဆောင်ရွက်ရမည်။

အခု ဤကုဒ် ပုံစံကို ကြည့်ကြရအောင် -

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
  // မှတ်ပုံတင်ထားသောကိရိယာများစာရင်းတင်ပြပါ။
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

ယခု ကျွန်ုပ်တို့တွင် function တစ်ခုရှိပြီး feature များစာရင်းကို return ပြန်ပါသည်။ tools စာရင်းရှိ entry တစ်ခုချင်းစီတွင် `name`, `description` နှင့် `inputSchema` ကဲ့သို့သော field များ ပါဝင်ပြီး return အမျိုးအစားကို လိုက်နာသည်။ ဤနည်း ကြောင့် ကျွန်ုပ်တို့၏ tools နှင့် feature သတ်မှတ်ချက်များကို အခြား နေရာတွင် သတ်မှတ်နိုင်ပြီး tools ဖိုလ်ဒါတွင် tools များအားလုံးကို ဖန်တီးနိုင်ပါသည်။ features အားလုံးအတွက်လည်း သက်ဆိုင်ရာ directory များဖြင့် ခွဲဝေထားနိုင်ပြီး project သည် ဤလို ပြုစုနိုင်ပါသည်။

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

သင့်၏ वास्तुकला သန့်ရှင်းစေသည့် နေရာမှအထူးအဆင်ပြေသည်။

tools ခေါ်ဆိုခြင်းသည် လည်း တူညီသဘောရော? tool တစ်ခုကို ခေါ်ဆိုရန် handler တစ်ခုသာရှိပြီး၊ tools ဘယ်ဟာမဆို ခေါ်နိုင်မလား? ဟုတ်ကဲ့၊ code ကို အောက်တွင်ရနိုင်ပါသည် -

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools သည် ကိရိယာအမည်များကို key အဖြစ်အသုံးပြုထားသည့် dictionary ဖြစ်သည်
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
    // TODO ကိရိယာကိုခေါ်ပါ၊

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

အထက်ပါကုဒ်တွင် ကြည့်ရှုနိုင်သည့်အတိုင်း tool ကို ခေါ်ရန် ဘယ် tool အားခေါ်သာ မည်သည့် argument များနှင့် အတူ call လုပ်မည်ဆိုတာကို parse out ပြုလုပ်ရသည်။ ထို့နောက် tool ကို ခေါ်ဆိုရမည်။

## ဤနည်းပညာအား validation ဖြင့် တိုးတက်စေခြင်း

ယခုအထိ tools, resources နှင့် prompts ထည့်ရန် register လုပ်နေသည့် function များအား အထက်ဖော်ပြသော handler နှစ်ခုဖြင့် အစားထိုးနိုင်ကြောင်း မြင်ရပြီးဖြစ်သည်။ နောက်ထပ် ဆောင်ရွက်ရမည့် အရာမှာ မည်သည်နည်း? tool ကို မှန်ကန်သော argument များဖြင့် ခေါ်ဆိုချက်ဖြစ်စေရန် validation အစိတ်အပိုင်း တစ်ခု ထည့်သွင်းရမည်ဖြစ်သည်။ runtime တစ်ခုခြင်းစီတွင် မတူညီသော နည်းလမ်းများ ရှိသည်၊ ဥပမာ Python တွင် Pydantic ကို အသုံးပြုသည်၊ TypeScript တွင် Zod ကို အသုံးပြုသည်။ အကြောင်းအရာမှာ အောက်ပါအတိုင်းဖြစ်သည် –

- feature (tool, resource သို့မဟုတ် prompt) ဖန်တီးမှုအတွင်း logic ကို သီးသန့် ဖိုလ်ဒါထားခြင်း။
- tool တစ်ခု ခေါ်ဆိုရန်တောင်းဆိုမှုရှိလာသည်ကို စစ်ဆေးရန် validation method ဖြည့်စွက်ခြင်း။

### feature တစ်ခု ဖန်တီးခြင်း

feature တစ်ခု ဖန်တီးရန် feature ကို သီးသန့် ဖိုင်တစ်ခု ဖန်တီးပြီး feature အတွက် လိုအပ်သော အဓိက field များပါဝင်ရန် သေချာရမည်။ tools, resources နှင့် prompts မှာ field မတူသည့် အပိုင်းအား ရှင်းလင်းပါသည်။

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
        # Pydantic မော်ဒယ်ကို အသုံးပြုပြီး အချက်အလက်အကဲဖြတ်ခြင်း
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ကို ထည့်သွင်းပါ၊ ဒါမှ addInputModel တစ်ခု ဖန်တီးပြီး args များကို အတည်ပြုနိုင်ပါလိမ့်မယ်။

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

အောက်ပါအတိုင်း ဆောင်ရွက်သည်ကို သင်မြင်နိုင်သည် -

- Pydantic ကို အသုံးပြု၍ `AddInputModel` schema ကို *schema.py* ဖိုင်တွင် ဖန်တီးပြီး field `a` နှင့် `b` ပါဝင်သည်။
- လာရောက်သော call ကို `AddInputModel` အမျိုးအစားဖြစ်ရမည်ဟု parse လုပ်ရန် ကြိုးစား၊ argument မညီလျှင် crash ဖြစ်ပေါ်ပါမည်။

   ```python
   # add.py
    try:
        # Pydantic မော်ဒယ်ကို အသုံးပြု၍ အတွင်းထည့်မှုကို အတည်ပြုပါ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ဤ parsing logic ကို tool call အတွင်း သို့မဟုတ် handler function ထဲတွင်ထားရမည်ကို ရွေးချယ်နိုင်သည်။

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

- tool calls အားလုံးကို ကတ်ပါသော handler ထဲတွင် လာရောက်သော call ကို tool ၏ သတ်မှတ်ထားသော schema တွင် parse လုပ်ရန် ကြိုးစားသည် -

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    သည်အကောင့်ဖွင့်ရင် သတ္တိပြု၍ တကယ် tool ကို ခေါ်ဆိုပါမည် -

    ```typescript
    const result = await tool.callback(input);
    ```

ဤနည်းလမ်းကြောင့် *server.ts* သည် တောင်းဆိုမှုပေးပို့သူများကို ချိတ်ဆက်ရာမှာသာ တိုစိတ်ဖွင့်ဖိုင်ဖြစ်ပြီး feature တစ်ခုချင်းစီသည် သီးသန့်ဖိုလ်ဒါ (tools/, resources/ သို့မဟုတ် /prompts) တွင်ရှိသည့် architecture ကောင်းမွန်စေရန် အထောက်အကူပြုသည်။

ကောင်းပါပြီ၊ နောက်တွင် ပိုမိုတည်ဆောက်ကြရအောင်။

## လေ့ကျင့်ခန်း - အနိမ့်အဆင့်ဆာဗာ တည်ဆောက်ခြင်း

ဤလေ့ကျင့်ခန်းတွင် ကျွန်ုပ်တို့ ဆောင်ရွက်မည့်အရာများမှာ -

1. tools စာရင်းပြုစုခြင်းနှင့် tool call များကို ကိုင်တွယ်သော အနိမ့်အဆင့် ဆာဗာတစ်ခု ဖန်တီးမည်။
2. တည်ဆောက်နိုင်စေသော architecture တစ်ခု ဖန်တီးမည်။
3. tool call များမှန်ကန်စေရန် validation ထည့်သွင်းမည်။

### -1- Architecture တည်ဆောက်ခြင်း

ပထမဆုံး ဆွေးနွေးရန်မှာ ထပ်မံဖြည့်ဆည်းသည့် feature များအတွက် ရှုပ်ထွေးစရာမရှိစွာ ထောက်ပံ့ပေးမည့် architecture ဖြစ်သည်၊ ဤမှာ ပုံစံ -

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

ယခု tools ဖိုလ်ဒါအတွင်း သာ tool အသစ်များ သပ်ရပ်စွာ ပြုလုပ်နိုင်မည့် architecture တည်ဆောက်ထားပါသည်။ resources နှင့် prompts အတွက်လည်း အထက်ပါနည်းစနစ်ကို အသုံးပြုနိုင်ပါသည်။

### -2- Tool တစ်ခု ဖန်တီးခြင်း

tool ထုတ်လုပ်မှု ပုံစံကို ခြုံငုံကြည့်ပါ။ ပထမဆုံး၊ tool ကို *tool* ဖိုလ်ဒါအတွင်း ဖန်တီးရမည်၊ ဤလို -

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic မော်ဒယ်ကို အသုံးပြု၍ အင်ပွတ်ကို သေချာစစ်ဆေးပါ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ထည့်သွင်းပါ၊ ထို့ကြောင့် AddInputModel တစ်ခု ဖန်တီးပြီး args များအား စစ်ဆေးနိုင်မည်ဖြစ်သည်။

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ဤနေရာတွင် Pydantic ဖြင့် name, description နှင့် input schema ကို သတ်မှတ်၍ tool ဖန်တီးခြင်းကို မြင်ရသည်။ handler နှင့် tool အသုံးပြုမည့် callback ရှိပြီး၊ `tool_add` dictionary မှာ အဆိုပါ properties များတိုက်ရိုက် ထည့်သွင်းထားသည်။

ထက်ပါ *schema.py* ကျရောက်ပါသည်၊ ကျွန်ုပ်တို့၏ tool အသုံးပြု input schema ဖြင့် သတ်မှတ်ထားသည်။

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

tools directory ကို module အဖြစ် သိမှတ်ရန် *__init__.py* ထည့်သွင်းရန် လိုအပ်ပါသည်။ ထို့အပြင် module များကို ပြသရန် -

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

tool များ ပေါင်းထည့်သည့်အခါ အမှတ်အသား ပြုစုရန်သုံးနိုင်ပါသည်။

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

tools များ၏ attribute များပါဝင်သော dictionary ဖန်တီးသည် -

- name - tool အမည်
- rawSchema - Zod schema, အဆိုပါ tool ကို call မှုများကို validate ဘို့ အသုံးပြုသည်။
- inputSchema - handler မှ အထောက်အကူပြုရန် schema
- callback - tool ကို ခေါ်ဖို့ အသုံးပြုသည်။

`Tool` ဖြစ်သော type ကို MCP server handler မှ လက်ခံနိုင်ရန် dictionary မှ ပြောင်းရွှေ့သည် - 

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* သည် tool များ၏ input schema များကို သိမ်းဆည်းထားပြီး၊ ယခုတွင် schema တစ်ခုသာရှိသော်လည်း tool များပေါင်းထည့်သည့်အခါ၌ ထပ်ဖြည့်နိုင်ပါသည် -

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ကောင်းပါပြီ၊ tools စာရင်းပြုစုခြင်းကို နောက်ထပ်ဆောင်ရွက်ကြရအောင်။

### -3- Tool စာရင်း ပြုစုခြင်းကို ကိုင်တွယ်ခြင်း

tools စာရင်းကို ကိုင်တွယ်ရန် request handler များကို server ဖိုင်တွင် ထည့်သွင်းရမည်ဖြစ်သည် -

**Python**

```python
# အတိုချုံးဖော်ပြရန် ကိုဒ်ကို ဖြုတ်ထားသည်
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

ဤတွင် `@server.list_tools` decorator ဖြင့် `handle_list_tools` function ကို တည်ဆောက်ပြီး၊ tool များ စာရင်းပြုစုထားရပါသည်။ နာမည်, ဖော်ပြချက်နှင့် inputSchema ဟူသော field များ မရှိမဖြစ် လိုအပ်သည်။

**TypeScript**

tools စာရင်းကို request handler ဖြင့် စီမံရန် `setRequestHandler` ကို server တွင် ခေါ်၍ `ListToolsRequestSchema` သတ်မှတ်ချက်နှင့် အသုံးပြုသည် -

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
// အတိုချုံးဖော်ပြရန် ကုဒ်ကို ဖယ်ရှားထားသည်
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // မှတ်ပုံတင်ထားသည့် ကိရိယာများစာရင်းကိုပြန်လည်ပေးပို့ပါ။
  return {
    tools: tools
  };
});
```

ကောင်းပါပြီ၊ tools စာရင်းပြုစုခြင်း ပိုင်းကို ဖြေရှင်းလိုက်ပါပြီ၊ tool call များကို နောက်တွင် ကြည့်ကြရအောင်။

### -4- Tool ခေါ်ဆိုခြင်း ကိုင်တွယ်ခြင်း

Tool တစ်ခု ခေါ်ဆိုရန် request handler တစ်ခု သတ်မှတ်ရမည်၊ calls လုပ်ရန် လိုသည့် feature နှင့် argument များ ပါဝင်သည့် request များကို ကိုင်တွယ်ရန်။

**Python**

`@server.call_tool` decorator ကို အသုံးပြု၍ `handle_call_tool` function သို့ ထည့်သွင်းပါ။ function အတွင်း tool name, argument များကို parse လုပ်ပြီး tool ဆက်အသုံးပြုမှု မြားကို သတ်မှတ်ထားသည်။ argument များကို function တွင် သို့မဟုတ် tool 内部ထား validate ပေးနိုင်သည်။

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools သည် ကိရိယာနာမည်များကို key များအဖြစ်ပါဝင်သည့် သင်္ကေတအဖြစ်ရှိသော dictionary ဖြစ်သည်
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ကိရိယာကို အသုံးပြုပါ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

ဖြစ်ပေါ်မည့်အလုပ်များမှာ -

- tool name ကို input parameter `name` နှင့် `arguments` dictionary အားဖြင့် ရှိသော arguments ကောင်တာများဖြင့် ယှဉ်ကြည့်သည်။
- tool ကို `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ဖြင့် ကောလ်လုပ်သည်။ argument validation ကို handler function တွင် ကျင်းပပြီး မအောင်မြင်လျှင် exception ဖြစ်ပေါ်မည်။

ဤနေရာတွင် အနိမ့်အဆင့် server မှ tools စာရင်းပြုစုခြင်းနှင့် call လုပ်ခြင်းကို လုံးဝနားလည်လို့ရပြီ ဖြစ်သည်။

[full example](./code/README.md) ကို ကြည့်ရှုနိုင်ပါသည်။

## အလုပ်အပ်

သင့်အား ရရှိထားသောကုဒ်များကို နောက်ထပ် tools, resources နှင့် prompt များဖြည့်စွက်ပြီး tools ဖိုလ်ဒါတွင် မူလအတိုင်းဖိုင်ထည့်ရန်သာ လိုအပ်ကြောင်း သတိပြုကြည့်ပါ။

*ဖြေရှင်းချက် မပါရှိပါ*

## အနှစ်ချုပ်

ဤအခန်းတွင် အနိမ့်အဆင့်ဆာဗာနည်းလမ်းကို ကြည့်ရှုပြီး အဘယ်သို့ architecture တည်ဆောက်မှုကို ကူညီပေးနိုင်ကြောင်း၊ validation ကို ဘယ်လိုတိုးတက်စေသလဲဆိုတာကို လေ့လာသည်။ validation library များဖြင့် input validation schema များကို တည်ဆောက်ပုံကို မြင်ရသည်။

## နောက်တစ်ဆင့်

- နောက်တစ်ခု - [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**တစ်ကြိမ်ပြောချက်**:  
ဤစာရွက်သည် AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်၍ရရှိပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးပမ်းသည်ဖြစ်သော်လည်း အလိုအလျောက်ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ရှိနိုင်သည်ကို သတိပြုပါရန်။ မူရင်းစာရွက်ကို ဇာတိဘာသာဖြင့် သေချာသောအချက်အလက်ရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လူကြီးမင်းတို့သည် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်၏အသုံးပြုမှုပေးသော နားလည်မှုများ သို့မဟုတ် မှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->