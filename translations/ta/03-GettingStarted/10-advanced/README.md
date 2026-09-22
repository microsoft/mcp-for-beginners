# மேம்பட்ட சர்வர் பயன்பாடு

MCP SDK இல் இரண்டு விதமான சர்வர்கள் உள்ளன, உங்கள் சாதாரண சர்வர் மற்றும் குறைந்த நிலை சர்வர். பொதுவாக, நீங்கள் அதன் மீது அம்சங்களை சேர்க்க வழக்கமான சர்வரைப் பயன்படுத்துவீர்கள். சில சந்தர்ப்பங்களில், நீங்கள் குறைந்த நிலை சர்வருக்கு சார்ந்திருக்க விரும்பலாம் உதாரணத்திற்கு:

- சிறந்த வரைவுரு. இரண்டு வழக்கமான சர்வர் மற்றும் குறைந்த நிலை சர்வர் இரண்டையும் கொண்டு ஒரு தெளிவான வரைவுருவை உருவாக்க இயலும், ஆனால் குறைந்த நிலை சர்வருடன் இது கொஞ்சம் எளிதாக இருக்கும் என்று வாதிடப்படலாம்.
- அம்ச கிடைக்குமிடம். சில மேம்பட்ட அம்சங்களை மட்டுமே
    குறைந்த நிலை சர்வருடன் மட்டுமே பயன்படுத்த முடியும். பிறகு பகுதிகள் Elicitation மற்றும் பழைய Sampling
    அம்சத்தை கவர்ந்துள்ளோம், இது MCP `2026-07-28` இல் பழமைவாய்ந்தது.

## வழக்கமான சர்வர் மற்றும் குறைந்த நிலை சர்வர்

வழக்கமான சர்வருடன் MCP Server உருவாக்குவது இவ்வாறு இருக்கும்

**Python**

```python
mcp = FastMCP("Demo")

# ஒரு கூட்டல் கருவியைச் சேர்க்கவும்
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

// ஒரு கூட்டல் கருவியைச் சேர்
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

முக்கியமாக நீங்கள் சர்வரில் சேர்க்க விரும்பும் அனைத்து கருவிகள், ஆதாரங்கள் அல்லது ஊக்கங்களை தெளிவாக சேர்க்கிறீர்கள். அதில் பிரச்சனை ஏதும் இல்லை.  

### குறைந்த நிலை சர்வர் அணுகுமுறை

ஆனால், குறைந்த நிலை சர்வர் அணுகுமுறையைப் பயன்படுத்தும்போது அதை வேறுபடியாக யோசிக்க வேண்டும். ஒவ்வொரு அம்ச வகைக்கும் (கருவிகள், ஆதாரங்கள் அல்லது ஊக்கங்கள்) இரண்டு ஹேன்ட்லர்களை உருவாக்குகிறீர்கள். உதாரணமாக கருவிகளுக்கு இரண்டு செயல்பாடுகள் உள்ளன:

- அனைத்து கருவிகளையும் பட்டியல்செய்தல். ஒன்று அனைத்து கருவிகளையும் பட்டியல்செய்ய பொறுப்பாக இருக்கும்.
- அனைத்து கருவி அழைப்புகளையும் கையாளுதல். இங்கு ஒரே செயல்பாடு ஒரு கருவிக்கு அழைப்புகளை கையாளும்.

இது குறைவான வேலை போல தான் தோன்றுகிறதா? எனவே ஒரு கருவியை பதிவு செய்வதற்குப் பதிலாக, எனக்கு தேவையானது அனைத்து கருவிகளையும் பட்டியல்செய்து உடனே கருவிக்கு அழைப்பை கையாள்வதே தான். 

இப்போது கோடு எப்படி இருக்கும் என்று பார்ப்போம்:

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
  // பதிவு செய்யப்பட்ட கருவிகளின் பட்டியலை திருப்பி வழங்கவும்
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

இப்போது ஒரு செயல்பாடு அம்சங்களின் பட்டியலை திருப்பி தருகிறது. அறிமுகப்பட்ட கருவிகளின் ஒவ்வொரு நுழைவிலும் `name`, `description` மற்றும் `inputSchema` போன்ற புலங்கள் உள்ளன, இது திருப்புகை வகையை பின்பற்றுகிறது. இதனால் நமது கருவிகள் மற்றும் அம்ச வரைவுகளை வேறு இடங்களில் வைக்கலாம். நமது அனைத்து கருவிகளை ஒரு tools கோப்புறையில் உருவாக்கலாம் மற்றும் உங்கள் அனைத்து அம்சங்களுக்கும் அதே விதமாக உங்கள் திட்டம் இந்த மாதிரி அமைக்கலாம்:

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

இது சிறந்தது, நமது வரைவாறு நன்றாக சுத்தமாக தெரியும்.

கருவிகளை அழைப்பது எப்படி, அதே யோசனை தானா, எது மாதிரியான கருவி என்றாலும் ஒரு ஹேன்ட்லர் கருவியை அழைக்கும், ஆம் அதுவே, இதோ அதன் கோடு:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools என்பது கருவி பெயர்களைக் கழுதைகளாக கொண்ட ஒரு அகராதி ஆகும்
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
    // செய்ய வேண்டியது கருவியை அழைக்கவும்,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

மேலே உள்ள கோட்டில், எது கருவி என்பதையும் எந்த புணர்ச்சிகளுடன் அழைக்கப்பட வேண்டும் என்பதையும் நாம் பிரித்து பார்ப்போம், பின்னர் கருவியை அழைப்பதில் முன்னேற வேண்டும்.

## பரிசுத்தப்படுத்தல் மூலம் அணுகுமுறையை மேம்படுத்துதல்

இப்போது வரை, கருவிகள், ஆதாரங்கள் மற்றும் ஊக்கங்களை சேர்க்க உங்கள் எல்லா பதிவுகளையும் இந்த இரண்டு ஹேன்ட்லர்களால் மாற்றலாம். இன்னும் என்ன செய்வது? நிச்சயமாகக் கருவி சரியான புணர்ச்சிகளுடன் அழைக்கப்படுவதை உறுதி செய்ய ஒரு வகையான பரிசுத்தப்படுத்தலைச் சேர்க்க வேண்டும். ஒவ்வொரு ரன்டைமும் இதற்கான தன்னுடைய தீர்வை கொண்டுள்ளது, உதாரணத்திற்கு Python பைடான்டிக் மற்றும் TypeScript Zod ஐப் பயன்படுத்துகிறது. நோக்கம் இதுதான்:

- ஒரு அம்சத்தை (கருவி, ஆதாரம் அல்லது ஊக்கம்) உருவாக்குவதற்கான தர்க்கத்தை அதன் சொந்த கோப்புறைக்கு நகர்த்துதல்.
- ஒரு வருகையை பரிசுத்தப்படுத்த வழி சேர்க்க, உதாரணத்திற்கு கருவி அழைப்பை பரிசுத்தப்படுத்த முடியுமென்பதை உறுதி செய்ய.

### ஒரு அம்சம் உருவாக்கு

ஒரு அம்சத்தை உருவாக்க, அந்த அம்சத்திற்கு ஒரு கோப்பை உருவாக்கி அதில் அவசியமான புலங்கள் இருக்க வேண்டும். கருவிகள், ஆதாரங்கள் மற்றும் ஊக்கங்களில் புலங்கள் கொஞ்சம் വ്യത്യस्थമായി இருக்கும்.

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
        # Pydantic மாதிரியை பயன்படுத்தி உள்ளீட்டை சரிபார்க்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # செய்ய: Pydantic ஐச் சேர்க்கவும், ஆகையால் நாம் AddInputModel ஐ உருவாக்கி args ஐ சரிபார்க்கலாம்

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

இங்கு நாம் கீழ்க்காணும் செயல்களை செய்ய்கிறோம்:

- Pydantic `AddInputModel` ஐ schema.py கோப்பில் `a` மற்றும் `b` என்ற புலங்களுடன் உருவாக்கு.
- வருகையை `AddInputModel` வகையாக பிரிக்க முயற்சி செய், அளவுகோல்களில் முரண்பாடு இருந்தால் இது தகரும்:

   ```python
   # add.py
    try:
        # Pydantic மாடலை பயன்படுத்தி உள்ளீட்டை சரிபார்க்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

இந்த பிரிக்கைகலை கருவி அழைப்பில் அல்லது ஹேன்ட்லர் செயல்பாட்டில் வைக்கலாம்.

**TypeScript**

```typescript
// சர்வர்.ts
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

       // @ts-புறக்கணி
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

// திட்டம்.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// சேர்க்க.ts
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

- அனைத்து கருவி அழைப்புக்களையும் கையாளும் ஹேன்ட்லரில், வருகையை கருவியின் வரையறுக்கப்பட்ட schema-படி பிரிக்க முயல்கிறோம்:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    அது நேர்ந்தால், உண்மையான கருவியை அழைக்க முன்னேறுவோம்:

    ```typescript
    const result = await tool.callback(input);
    ```

இப்போது இந்த அணுகுமுறை நன்றாக ஒருங்கிணைந்த வரைவாக்கத்தை உருவாக்குகிறது, *server.ts* என்பது கோரிக்கை கையாளிகளைக் இணைக்கும் மிகச் சிறிய கோப்பு மட்டுமே, மேலும் ஒவ்வொரு அம்சமும் அவருடைய சொந்த கோப்புறைகளில் இயங்குகிறது உதாரணத்திற்கு tools/, resources/ அல்லது /prompts.

சிறப்பாக, அடுத்ததாக இதை கட்டமைக்க முயலுவோம்.

## பயிற்சி: குறைந்த நிலை சர்வர் உருவாக்குதல்

இந்த பயிற்சியில் நாம் பின்வருமாறு செய்கிறோம்:

1. கருவிகள் பட்டியலிடும் மற்றும் கருவிகளை அழைக்கும் குறைந்த நிலை சர்வரை உருவாக்கு.
1. நீங்கள் கட்டமைக்கக்கூடிய வரைவுருவை செயலாக்கு.
1. உங்கள் கருவி அழைப்புகள் சரியான பரிசுத்தப்படுத்தப்பட்டுள்ளன என்பதை உறுதி செய்ய பரிசுத்தப்படுத்தலைச் சேர்க்கவும்.

### -1- ஒரு வரைவுரு உருவாக்கு

முதலில், நாம் அதிகமான அம்சங்களைச் சேர்ப்பதற்கு உதவும் வரைவுருவை கவனிக்க வேண்டும், இது இவ்வாறு இருக்கும்:

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

இப்போது நாமெளிமையுடன் tools கோப்புறையில் புதிய கருவிகளைச் சேர்க்கும் கட்டமைப்பு அமைத்துள்ளோம். resources மற்றும் prompts க்கும் துணை கோப்புறைகள் சேர்க்க விரும்பினால் இதைக் கடைபிடிக்கலாம்.

### -2- ஒரு கருவி உருவாக்குதல்

அடுத்து ஒரு கருவி உருவாக்குதல் எப்படி என பார்ப்போம். முதலில் அதனை *tool* துணை கோப்புறையில் உருவாக்க வேண்டும் இவ்வாறாக:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic மாதிரியைப் பயன்படுத்தி உள்ளீட்டை சரிபார்க்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # செய்யவேண்டியது: Pydantic ஐச் சேர்க்கவும், அதனால் நாம் AddInputModel உருவாக்கி args ஐ சரிபார்க்க முடியும்

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

இங்கு நாம் பெயர், விளக்கம் மற்றும் உள்ளீட்டு சரிபார்ப்பை Pydantic கொண்டு வரையறுக்கும் விதத்தை பார்க்கின்றோம் மற்றும் இந்த கருவி அழைக்கப்படும் போது அழைக்கப்படும் ஹேன்ட்லர் உண்மை ஆகும். இறுதியில் `tool_add` என்ற அகராதி அனைத்தும் உள்ளதாக்கப்படுகிறது.

கூடவே, *schema.py* என்பது கருவி உள்ளீட்டு சரிபார்ப்பை வரையறுக்கும் கோப்பாகும்:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

மேலும் *__init__.py* ஐ நிரப்பி tools கோப்புறை ஒரு மாட்யூல் ஆக நடத்தப்படுவதை உறுதி செய்ய வேண்டும். கூடுதலாக, அதில் உள்ள உறுப்புகள் வெளியிடப்பட வேண்டும் இவ்வாறு:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

நாம் அதிக கருவிகள் சேர்க்கும்போது இந்த கோப்பில் தொடர்ந்தும் சேர்க்கலாம்.

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

இங்கு சொத்துக்களை உடைய அகராதி ஒன்றை உருவாக்குகிறோம்:

- name, இது கருவியின் பெயர்.
- rawSchema, இது Zod schema ஆகும், இது கருவி அழைப்புகளின் வருகைகளை பரிசுத்தப்படுத்த பயன்படுத்தப்படும்.
- inputSchema, இவ்வளவு schema ஹேன்ட்லரால் பயன்படுத்தப்படும்.
- callback, இது கருவியை அழைக்கப்பயன்படும்.

மேலும் `Tool` உள்ளது, இது இந்த அகராதியை mcp சர்வர் ஹேன்ட்லர் ஏற்றுக்கொள்ளும் வகையாக மாற்ற கையாளப்படுகிறது மற்றும் இதோவையாக தெரிகிறது:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

மேலும் *schema.ts* உள்ளது, இது ஒவ்வொரு கருவிக்கும் உள்ளீட்டு schemas சேமிக்கும் இடமாகும், இங்கு தற்போது ஒரே schema உள்ளது, ஆனால் கருவிகள் அதிகரிக்கும் போது நாங்கள் கூடுதலாக நுழைவுகளைச் சேர்க்கலாம்:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

சிறப்பாக, அடுத்து நமது கருவிகளின் பட்டியலை கையாள்வோம்.

### -3- கருவி பட்டியலை கையாளு

அடுத்து நமது கருவிகளின் பட்டியலை கையாள, ஒரு கோரிக்கை ஹேன்ட்லரை அமைக்க வேண்டும். சர்வர் கோப்பில் இதைப் பின்வருமாறு சேர்க்க வேண்டும்:

**Python**

```python
# குறுகியதற்காக குறியீடு省略ப்பட்டது
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

இங்கு, `@server.list_tools` என்ற டெக்கரேட்டரும், அதனை நடைமுறைப்படுத்தும் `handle_list_tools` செயல்பாடும் சேர்க்கப்பட்டுள்ளன. கடைசியில், ஒரு கருவிகளின் பட்டியலை உருவாக்க வேண்டும். ஒவ்வொரு கருவியும் பெயர், விளக்கம் மற்றும் inputSchema வைத்திருக்க வேண்டும்.   

**TypeScript**

கருவிகள் பட்டியலைக் கையாள கோரிக்கை ஹேன்ட்லரை அமைக்க, சர்வர் மீது `setRequestHandler` க்கு பாஸ்பாடாக இது போன்ற schema வழங்க வேண்டும், இந்நிலையில் `ListToolsRequestSchema`. 

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
// சுருக்கத்தில் குறியீடு விலக்கப்பட்டது
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // பதிவு செய்யப்பட்ட கருவிகளின் பட்டியலை திருப்பி கொடு
  return {
    tools: tools
  };
});
```

சிறப்பாக, இப்போது கருவிகளை பட்டியலிடும் பிரச்சனையை தீர்த்தோம், அடுத்து கருவிகளை அழைக்கும் விதமாக பார்ப்போம்.

### -4- கருவி அழைப்பை கையாளு

கருவியை அழைக்கும் ஹேன்ட்லரை இன்னொரு முறையாக அமைக்க வேண்டும், இதில் எந்த அம்சத்தை எவ்வாறு அழைக்க வேண்டும் என்பது கோரிக்கையில் குறிப்பிடப்படும்.

**Python**

`@server.call_tool` என்ற டெக்கரேட்டரை பயன்படுத்தி `handle_call_tool` என்ற செயல்பாட்டை நடைமுறைப்படுத்துவோம். இதில் கருவி பெயர், அதன் புணர்ச்சிகள் பிரிக்கப்பட்டு சரிபார்க்கப்பட வேண்டும். இந்த புணர்ச்சிகள் இந்த இடத்தில் அல்லது கருவியில் நேரடியாக பரிசுத்தப்படுத்தப்படலாம்.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools என்பது கருவி பெயர்களை விசைகளாக கொண்டு உள்ள ஒரு அகராதி
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # கருவியை அழைக்கவும்
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

இதோ நடந்துகொள்ளும் செயல்முறை:

- நமது கருவி பெயர் ஏற்கனவே உள்ளீட்டை வழங்கும் `name` என்ற இடத்தில் உள்ளது, புணர்ச்சிகள் `arguments` அகராதியில் உள்ளன.

- கருவி அழைக்கப்படுகிறது `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` என்பதை பயன்படுத்தி. புணர்ச்சிகளின் பரிசுத்தப்படுத்தல் `handler` சொத்தில் நடக்கும், அது செயல்பாடாக இருக்கிறது, தோல்வியுற்றால் தவறுஉருப்பை எழுப்பும். 

இதோ, இப்போது குறைந்த நிலை சர்வரைப் பயன்படுத்தி கருவிகளை பட்டியலிடுவதும் அழைப்பதின் முழுமையான புரிதல் உள்ளது.

முழு உதாரணம் இதோ காண்க: [full example](./code/README.md)

## பணிகள்

இனி நீங்கள் பெற்றுள்ள கோட்டை சிறிது கருவிகள், ஆதாரங்கள் மற்றும் ஊக்கங்களுடன் விரிவுபடுத்தி, tools கோப்புறையில் மட்டும் கோப்புகளை சேர்த்தால் போதும் என்பதைக் கவனியுங்கள்.

*ஏதாவது தீர்வு இல்லை*

## சாராம்சம்

இந்த அத்தியாயத்தில் குறைந்த நிலை சர்வர் அணுகுமுறை எப்படி வேலை செய்கிறது, அதை வைத்து எளிமையான வரைவுருவை எவ்வாறு உருவாக்க முடியும் என்பதைப் பார்த்தோம். பரிசுத்தப்படுத்தலை பற்றியும் விவாதித்து, உள்ளீட்டு பார்வையீட்டிற்கு schema உருவாக்கும் validation நூலகங்களைப் பயன்படுத்துவது எப்படி என்பதைக் கற்றுக்கொண்டீர்கள்.

## அடுத்தது என்ன

- அடுத்து: [எளிய அங்கீகாரம்](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->