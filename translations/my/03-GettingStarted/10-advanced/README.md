# အဆင့်မြင့်ဆာဗာအသုံးပြုခြင်း

MCP SDK တွင် ဖြန့်ချိထားသော ဆာဗာနှစ်မျိုးရှိပါတယ်၊ သင်၏ ပုံမှန်ဆာဗာနှင့် နိမ့်ဆုံးအဆင့်ဆာဗာ။ ပုံမှန်အားဖြင့် သင်သည် ပုံမှန်ဆာဗာကို အသုံးပြု၍ လုပ်ဆောင်ချက်များ ထည့်သွင်းပါမည်။ သို့သော် တချို့သောအခါများတွင် နိမ့်ဆုံးအဆင့်ဆာဗာကို ဂရုစိုက်ရန်လိုအပ်သည်။ ဥပမာ -

- ပိုမိုကောင်းမွန်သော စီမံခန့်ခွဲမှု။ ပုံမှန်ဆာဗာနှင့် နိမ့်ဆုံးအဆင့်ဆာဗာ နှစ်မျိုးစလုံးဖြင့် သန့်ရှင်းသော စီမံခန့်ခွဲမှု တည်ဆောက်နိုင်ပြီး၊ နိမ့်ဆုံးအဆင့်ဆာဗာဖြင့် ပိုမိုလွယ်ကူသည်ဟု ဆွေးနွေးနိုင်သည်။
- လုပ်ဆောင်ချက်ရရှိနိုင်မှု။ တချို့အဆင့်မြင့်လုပ်ဆောင်ချက်များကို နိမ့်ဆုံးအဆင့်ဆာဗာဖြင့်သာ အသုံးပြုနိုင်သည်။ ပုံမှန်ကျွန်တော်တို့ နောက်ပိုင်းအခန်းများတွင် sampling နှင့် elicitation ထည့်သွင်းသောအခါ တွေ့ရမှာဖြစ်သည်။

## ပုံမှန်ဆာဗာ နှင့် နိမ့်ဆုံးအဆင့်ဆာဗာ

ပုံမှန်ဆာဗာဖြင့် MCP Server တည်ဆောက်ခြင်းသည် ဒီလိုဖြစ်ပါတယ်။

**Python**

```python
mcp = FastMCP("Demo")

# ပေါင်းခြင်းကိရိယာတစ်ခုထည့်ပါ
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

// ပေါင်းထည့်ခြင်းကိရိယာတစ်ခုကို ထည့်ပါ
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

အဓိကမှာ သင်သည် ဆာဗာတွင် ပါဝင်စေလိုသော ကိရိယာ၊ ရင်းမြစ် သို့မဟုတ် prompt တစ်ခုချင်းစီကို သက်သေပြ စာရင်းသွင်းရသည်။ အဲဒါမှာ ပြဿနာမရှိပါဘူး။

### နိမ့်ဆုံးအဆင့်ဆာဗာနည်းလမ်း

သို့သော် နိမ့်ဆုံးအဆင့်ဆာဗာနည်းလမ်းကို အသုံးပြုသောအခါ သင်သည် ကွဲပြားစွာ စဉ်းစားရပါမည်။ ကိရိယာတိုင်းကို မှတ်ပုံတင်ခြင်းမပြုဘဲ အစား feature အမျိုးအစား (ကိရိယာများ, ရင်းမြစ်များ သို့မဟုတ် prompt များ) အတွက် handler နှစ်ခု ဖန်တီးရမည်။ ဥပမာ - ကိရိယာများအတွက် functions နှစ်ခုသာရှိသည် -

- ကိရိယာအားလုံးကို စာရင်းပြုစုခြင်း။ ကိရိယာအားလုံးကို စာရင်းတွင်သွင်းရန် လုပ်ဆောင်မှု တစ်ခု။
- ကိရိယာခေါ်ယူမှုကို ကိုင်တွယ်ခြင်း။ ကိရိယာတစ်ခုခုကို ခေါ်သည့် function တစ်ခုသာ ရှိသည်။

ဒါက လုပ်ငန်းပမာဏနည်းသလို ထင်ပါတယ်။ ကိရိယာတစ်ခု register ပြုလုပ်ရန် အစား ကိရိယာအားလုံးစဉ်းစားပြီး လိုအပ်သည့်အခါ ခေါ်သင့်သည်။

ယခု code မည်သို့ ခေတ်မှီပြောင်းလဲသည်ကို ကြည့်ကြရအောင်။

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
  // မှတ်ပုံတင်ထားသော ကိရိယာများ၏ စာရင်းကို ပြန်တမ်းပေးပါ။
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

ယခု features စာရင်း အား return ပြန်ပေးသည့် function တစ်ခုရှိသည်။ tools စာရင်းထဲမှာ `name`, `description`, `inputSchema` ကဲ့သို့သော fields ပါဝင်ပြီး return အမျိုးအစားနှင့် ဆက်စပ်သည်။ ဒီဟာကြောင့် tools များနှင့် feature အကြောင်းအရာကို အခြားနေရာများမှာ သိမ်းဆည်းနိုင်သည်။ သင် tools များအား tools ဖိုလ်ဒါထဲတွင် ချထားနိုင်ပြီး feature များအားလုံးကိုလည်း အဲဒီလိုစီစဉ်နိုင်သည်။ သင့်ပရောဂျက်သည် သိသိသာသာ စီမံခန့်ခွဲမှုရှိမည်။

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

အဲဒါကောင်းပါတယ်၊ ကျွန်တော်တို့စီမံခန့်ခွဲမှုကို သန့်ရှင်းစေပါတယ်။

ကိရိရ်းဖုန့်ခေါ်ပုံကတော့ အဲဒီလိုပြန်ပါသလား၊ တစ်ခုတည်းသော handler ကိရိယာတစ်ခုကို ခေါ်ဖို့ဆိုတာနဲ့ ညီတယ်လား? ဟုတ်ပါတယ်၊ code ကို အောက်ပါအတိုင်းဖြစ်ပါသည် -

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools သည် ကိရိယာနာမည်များကို key အဖြစ် အသုံးပြုသော dictionary ဖြစ်သည်။
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
    // TODO ကိရိယာကိုခေါ်ရန်,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

အထက်တွင် မြင်သာသလို ကိရိယာတစ်ခုကို ခေါ်ဖို့ အမည်နှင့် အချက်အလက်များကို တိကျစွာ ဖော်ထုတ်ပြီး ကိရိယာကို ခေါ်ယူရမည်။

## အတည်ပြုမှုဖြင့် နည်းလမ်းတိုးတက်စေခြင်း

အခုထိ သင်သည် tools, resources နှင့် prompts များ အသစ်ထည့်သွင်းရန် မှတ်ပုံတင်ခြင်းများကို feature အမျိုးအစားတိုင်းအတွက် handler နှစ်ခုဖြင့် အစားထိုးနိုင်တာကို မြင်ရပါပြီ။ နောက်ဘာလုပ်ရမလဲ? ကိရိယာကို မှန်ကန်သော arguments ဖြင့် ခေါ်ယူမည်ဆိုတာ အတည်ပြုသော validation လုပ်ငန်းစဉ် ထည့်သွင်းရပါမည်။ အချို့ runtime များတွင် Python မှ Pydantic ကို၊ TypeScript မှ Zod ကို အသုံးပြုသည်။ အဓိကအရေးအသားမှာ -

- feature တစ်ခု (ကိရိယာ, ရင်းမြစ် သို့မဟုတ် prompt) ဖန်တီးရန် ဇယားကို ထားရှိသော ဖိုလ်ဒါက သို့ရွှေ့ပါ။
- ဥပမာ ကိရိယာခေါ်ဖို့ ရုတ်တရက် စီစဉ်ထားသော request တစ်ခုကို သွင်းယူပြီး အတည်ပြုပါ။

### feature ဖန်တီးခြင်း

feature တစ်ခုဖန်တီးရန်အတွက်၊ 해당 feature အတွက် ဖိုင်တစ်ခုသည် ဖန်တီးထားရမည်နှင့် ၎င်း feature အတွက် လိုအပ်သော မပါမဖြစ် fields ပါဝင်ရမည်။ tools, resources နှင့် prompts အတွင်း fields အနည်းငယ် ကွာခြားသည်။

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
        # Pydantic မော်ဒယ် အသုံးပြု၍ input ကို စစ်ဆေးပါ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ထည့်ပါ၊ ထိုကြောင့် AddInputModel ဖန်တီးနိုင်ပြီး args များကို စစ်ဆေးနိုင်ပါသည်။

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ဒီမှာ ကျွန်တော်တို့ အောက်ပါအတိုင်း ဆောင်ရွက်သည် -

- Pydantic `AddInputModel` ကို အသုံးပြု၍ `a` နှင့် `b` field များပါရှိသော schema ဖန်တီးခြင်း (*schema.py* ဖိုင်တွင်)။
- ကုဒ်တွင် အသွင်းလာသော request ကို `AddInputModel` အမျိုးအစားဖြင့် စစ်ဆေးရာမမှန်ကန်မှုရှိပါက 崩潰 ဖြစ်နိုင်သည်။

   ```python
   # add.py
    try:
        # Pydantic မော်ဒယ် အသုံးပြု၍ ထည့်သွင်းရမည့်ဒေတာကို အတည်ပြုပါ။
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ဒီ parsing နည်းလမ်းကို ကိရိယာခေါ် function ထဲမှာထားစရာမလိုပဲ handler function ထဲမှာထားနိုင်သည်။

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

- ကိရိယာခေါ်ရာတွင် handler တွင် လာတဲ့ request ကို ကိရိယာ၏ schema အတိုင်း ပစက်ခ်ဖတ်ကြည့်ကြသည်။

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    တကယ်လက်တွေ့တောင် ကျော်သွားရင် tool ကို ခေါ်သွားတယ် -

    ```typescript
    const result = await tool.callback(input);
    ```

ဒီနည်းလမ်းဟာ ဆာဗာ.ts ဖိုင်မှာ requests handler တွေ link လုပ်သည့် နေရာအစိတ်အပိုင်းသေးငယ်ပြီး ထိုင်ခုံစဥ် feature များကို သက်ဆိုင်ရာ folder များမှာ သိမ်းဆည်းတာဖြစ်ပြီး အသေးစိတ် architecture ကောင်းတယ်။

ထိုအတိုင်း ဆက်လက်လုပ်ကြည့်မယ်။

## လေ့ကျင့်ခန်း - နိမ့်ဆုံးအဆင့် ဆာဗာဖန်တီးခြင်း

ဒီလေ့ကျင့်ခန်းမှာ -

1. ကိရိယာများ စာရင်းပြုပြင်ခြင်းနှင့် ကိရိယာခေါ်ဆိုမှုကို ကိုင်တွယ်နိုင်သော နိမ့်ဆုံးလွတ်လပ်တဲ့ ဆာဗာတစ်ခု ဖန်တီးမည်။
2. ဆောက်လုပ်နိုင်စွမ်းရှိသော architecture တစ်ခု တည်ဆောက်မည်။
3. ကိရိယာခေါ်ဆိုမှုများကို မှန်ကန်စွာ အတည်ပြုရန် validation ထည့်သွင်းမည်။

### -1- Architecture တည်ဆောက်ခြင်း

ပထမ ဦးစွာ လိုအပ်တာမှာ feature များ တိုးချဲ့သွားရာ မှ ဘာသာရပ်သွားတည်ဆောက်ပုံပါ။ ဒီလို ဖြစ်ပါတယ်။

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

ယခု tools ဖိုလ်ဒါတွင် tools အသစ်ထည့်ရန် လွယ်ကူသည့် architecture ကို စတင်ထည့်သွင်းပြီးဖြစ်သည်။ resources နှင့် prompts အတွက် subdirectory များ ထည့်သွင်းစေလိုပါက အဆင်ပြေပါသည်။

### -2- tool တစ်ခု ဖန်တီးခြင်း

tool တစ်ခုဖန်တီးမှုသည် အောက်ပါအတိုင်း ဖြစ်သည်။ ပထမဆုံး၊ အဲဒီ tool ကို tools subdirectory ထဲတွင် ဖန်တီးရမည်။

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic မော်ဒယ်ကို အသုံးပြု၍ အချက်အလက်များကို စစ်ဆေးပါ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ကို ထည့်သွင်းပါ၊ ဒါမှသာ AddInputModel ကို ဖန်တီးပြီး args များကို စစ်ဆေးနိုင်မှာ ဖြစ်ပါတယ်

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ဒီမှာ ကျွန်တော်တို့ မြင်ရတာက name, description နှင့် input schema ကို Pydantic ဖြင့် ဖော်ပြထားပြီး tool ခေါ်သည့်အခါ လက်ခံဆောင်ရွက်မည့် handler ပါရှိသည်။ နောက်ဆုံးတွင် `tool_add` ဆိုတဲ့ properties စုစည်းထားသော dictionary အဖြစ် ထုတ်ဖော်ထားသည်။

*schema.py* ကို tool ၏ input schema အတွက် သတ်မှတ်ထားသည် -

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

tools directory ကို module အဖြစ် သတ်မှတ်ရန် *__init__.py* ဖိုင်ထဲကို အသစ်ဖြည့်စွက်ရမည်။ ထို့နောက် ထို module တွေကို ထွက်ပေါ်အောင်ပြုလုပ်ရန် -

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

tools များ တိုးတက်လာတာနဲ့အမျှ ထပ်ဖြည့်နိုင်ပါတယ်။

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

property များပါဝင်သော dictionary ဖန်တီးထားသည် -

- name - tool အမည်။
- rawSchema - Zod schema သည် tool ခေါ်ဆိုမည့် request များကို အတည်ပြုရန် အသုံးပြုသည်။
- inputSchema - handler မှအသုံးပြုမည့် schema။
- callback - tool ကို ခေါ်ရန် သုံးသည်။

`Tool` သည် mcp server handler အတွက် အသုံးပြုနိုင်သော type သို့ ဤ dictionary ကို ပြောင်းလဲရန် အသုံးပြုသည် -

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* တွင် tools အတွက် input schemas သိမ်းဆည်းထားပြီး ယနေ့တွင် schema တစ်ခုသာရှိပေမယ့် tools များ တိုးလာလျှင် အချက်အလက် သစ်များ ထည့်ရန် ဖြစ်သည် -

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ကောင်းပြီ။ tools များစာရင်း သုံးသပ်ကို ဆက်လုပ်ကြည့်မယ်။

### -3- tool စာရင်းကို ကိုင်တွယ်ခြင်း

tools များစာရင်းကို စီမံရန် request handler တစ်ခု ဖန်တီးရမည်။ ဆာဗာ ဖိုင်တွင် ထည့်သွင်းရန် -

**Python**

```python
# ကိုဒ်တိုု၌ချုပ်ထားသည်
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

ဤနေရာတွင် `@server.list_tools` decorator နှင့် `handle_list_tools` function ကို အသုံးပြုသည်။ ၎င်းတွင် tools စာရင်း တင်ပေးရမည်။ ကိရိယာတစ်ခုချင်း စာရင်းတွင် name, description နှင့် inputSchema ရှိရမည်။

**TypeScript**

tools များ စာရင်းကျင်းပရန် request handler တစ်ခု ဖန်တီးရန် `setRequestHandler` ကို ဆာဗာပေါ်တွင်သုံးပြီး အတည်မပြုမှု schema ကို `ListToolsRequestSchema` အတိုင်း ဖြည့်သွင်းရမည်။

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
// အတိုချုပ်အတွက် ကုဒ်ကိုဖျောက်ထားသည်
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // စာရင်းသွင်းထားသော ကိရိယာများစာရင်းကို ပြန်ပေးသည်
  return {
    tools: tools
  };
});
```

ကောင်းပြီ၊ tools စာရင်းကို ဖြေရှင်းလိုက်ပါပြီ။ tools ခေါ်ဆိုမှုကို ဘယ်လို 처리 နိုင်မယ်ဆိုတာ ကြည့်ကြရအောင်။

### -4- tool ခေါ်ယူမှု ကိုင်တွယ်ခြင်း

tool ကို ခေါ်ရန် request handler တစ်ခု ပိုမို စီမံရမည်။ ဤ handler သည် ဖွင့်ဆိုမှု feature နာမည် နှင့် argument များ ကို လက်ခံရမည်။

**Python**

`@server.call_tool` decorator အား အသုံးပြုပြီး `handle_call_tool` function ဖြင့် အကောင်အထည်ဖော်လိုက်မည်။ function မှာ tool နာမည်၊ argument များကို ခွဲထုတ်ပြီး argument များသည် မှန်ကန်ကြောင်း အတည်ပြုပြီး ၎င်းတို့ကို တက်ကြွစွာ ခေါ်ယူရမည်။ arguments validation ကို ဒီ function မှာ သို့မဟုတ် အဲဒီ tool handler ထဲမှာ ပြုလုပ်နိုင်သည်။

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools သည် tool နာမည်များကို key အနေနှင့် သုံးထားသော dictionary ဖြစ်သည်
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # tool ကို ဖော်ဆောင်ပါ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

အောက်ပါအတိုင်းလုပ်ဆောင်သည်-

- tool နာမည်သည် input parameter `name` အဖြစ် ရှိပြီး `arguments` dictionary မှ argument များဖြစ်သည်။
- call ကို `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ဖြင့် ဆောင်ရွက်ပြီး arguments validation သည် handler function ထဲတွင် ဂရုပြုသည်။ မအောင်မြင်ပါက exception ထွက်မည်။

အခုကျွန်ုပ်တို့ ကျွန်တော်တို့ နိမ့်ဆုံးအဆင့်ဆာဗာဖြင့် tools များ စာရင်းထုတ်ခြင်းနှင့် ခေါ်ဆိုမှုများ လုံးဝနားလည်ပြီးဖြစ်သည်။

[full example](./code/README.md) ကို ဒီမှာကြည့်ပါ။

## တာဝန်ပေးမှု

သင့်လက်ခံထား သည့် ကုဒ်ထဲသို့ tools, resources နှင့် prompts များ အများအပြား ထည့်သွင်းပါ။ tools directory တွင် ဖိုင်များ တင်သွင်းရုံဖြင့်သာ လုပ်ဆောင်ရာ အခြားနေရာမလိုအပ်ကြောင်း တွေ့မြင်ပါလိမ့်မည်။

*ဖြေရှင်းချက် မပေးပါ*

## အနှစ်ချုပ်

ဒီအခန်းတွင် နိမ့်ဆုံးအဆင့်ဆာဗာနည်းလမ်း အလုပ်လုပ်ပုံနှင့် ဘယ်လို architecture ကောင်းတည်ဆောက်နိုင်သည်ကို ကြည့်ရှုခဲ့သည်။ validation အရေးပါမှုအကြောင်း နှင့် validation library များ အသုံးပြုပြီး input schema များ ဖန်တီးနည်းကို ပြသခဲ့သည်။

## နောက်တစ်ခန်း

- နောက်တစ်ခန်း - [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အချက်မပြုတ်ချက်**  
ဤစာရွက်ကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်က ကြားခံဘာသာပြန်ခြင်းကြောင့် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ဖြစ်ပေါ်နိုင်သောကြောင်း သတိပြုရန်လိုအပ်ပါသည်။ မူရင်းစာရွက်ကို လက်ရှိနိုင်ငံဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အရင်းအမြစ်အဖြစ် တွင်ကျယ်စွာ အသုံးပြုရမည်ဖြစ်သည်။ အရေးကြီးသောအချက်အလက်များအတွက် ကျွမ်းကျင်သော လူသားဘာသာပြန်ကူညီမှုကိုအကြံပြုပါသည်။ ဤဘာသာပြန်ဝန်ဆောင်မှု အသုံးပြုမှုကြောင့်ဖြစ်ပေါ်လာနိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းချက်များအတွက် ကျွန်ုပ်တို့၏ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->