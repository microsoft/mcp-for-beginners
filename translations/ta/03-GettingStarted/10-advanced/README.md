# மேம்பட்ட சர்வர் பயன்பாடு

MCP SDK இல் இரண்டு விதமான சர்வர்கள் வெளிப்படுத்தப்பட்டுள்ளன, உங்கள் சாதாரண சர்வர் மற்றும் குறைந்த நிலை சர்வர். சாதாரணமாக, அதில் அம்சங்களைச் சேர்க்க에는 சாதாரண சர்வரைப் பயன்படுத்துவீர்கள். சில சமயங்களில், நீங்கள் குறைந்த நிலை சர்வரை நம்ப விரும்புவீர்கள், உதாரணமாக:

- சிறந்த கட்டமைப்பு. சாதாரண சர்வர் மற்றும் குறைந்த நிலை சர்வர் இரண்டையும் அடிப்படையாக கொண்டு ஒரு சுத்தமான கட்டமைப்பை உருவாக்க முடியும், ஆனால் குறைந்த நிலை சர்வருடன் அதை சிறிது எளிதாக செய்ய முடியும் என்று கூறப்படலாம்.
- அம்சங்கள் கிடைக்கும் அளவு. சில மேம்பட்ட அம்சங்களை குறைந்த நிலை சர்வர் மட்டுமே பயன்படுத்த முடியும். எடுக்கும் மாதிரிகள் மற்றும் கேள்வித்தாள் சேர்க்கையில் இதை அடுத்த அத்தியாயங்களில் காண்பீர்கள்.

## சாதாரண சர்வர் மற்றும் குறைந்த நிலை சர்வர்

இதோ ஒரு MCP சர்வர் உருவாக்கும் போது சாதாரண சர்வருடன் எப்படி இருக்கும் என்பதின் உதாரணம்

**Python**

```python
mcp = FastMCP("Demo")

# ஒரு கூட்டுதல் கருவியைச் சேர்க்கவும்
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

// ஒரு கூட்டல் கருவியைச் சேர்க்கவும்
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

புள்ளி என்னவென்றால், நீங்கள் சர்வருக்கு வேண்டும் எனும் ஒவ்வொரு கருவி, வளம் அல்லது கேள்வித்தாளையும் தெளிவாகச் சேர்க்கிறீர்கள். இதில் தவறு எதுவும் இல்லை.  

### குறைந்த நிலை சர்வர் முறையைப் பயன்படுத்துதல்

ஆனால் குறைந்த நிலை சர்வர் முறையைப் பயன்படுத்தும்போது, வேறுபடமாக யோசிய வேண்டும். ஒவ்வொரு கருவி, வளம் அல்லது கேள்வித்தாள் வகைக்கும் இரண்டு கையாளுனர்களையே உருவாக்க வேண்டும். உதாரணமாக, கருவிகளுக்கு இரண்டு செயலிகளே இருப்பதுதான்:

- அனைத்து கருவிகளையும் பட்டியலிடுதல். அனைத்து கருவிகளை பட்டியலிடும் முயற்சிகளுக்குமான ஒரு செயலி.
- அனைத்து கருவிகளுக்கும் அழைப்பை கையாளுதல். இங்கே, ஒரு செயலி மட்டும் கருவி அழைப்புகளை கையாளும்.

அது குறைவான பணியாக இருக்குமே? ஆகவே கருவியை பதிவு செய்யாமல், அனைத்து கருவிகளையும் பட்டியலிடும்போது கருவி பட்டியலில் உள்ளது மற்றும் கருவி அழைக்கும்போது அது அழைக்கப்படுகிறது என்பதையே உறுதிப்படுத்தவேண்டும். 

இப்போது குறைந்த நிலை முறையால் குறியீடு எப்படி இருக்கிறது பார்ப்போம்:

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
  // பதிவு செய்யப்பட்ட கருவிகளின் பட்டியலை 반환ி்்்்்்்்்்
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

இங்கு ஒரு செயலி அம்சப் பட்டியலைத் தருகிறது. கருவிகளின் பட்டியலில் ஒவ்வொரு நுழைவிலும் `name`, `description` மற்றும் `inputSchema` போன்ற புலங்கள் உள்ளன, இது திரும்பும் வகைக்கு ஒத்திருக்க வேண்டும். இதனால், கருவிகள் மற்றும் அம்ச வரையறைகளை வேறு இடத்திலும் வைக்க முடியும். இப்போது அனைத்து கருவிகளையும் tools என்ற கோப்பகத்தில் உருவாக்கலாம் மற்றும் உங்கள் அனைத்து அம்சங்களும் பொருத்தமான இடத்தில் இருக்கும், எனவே உங்கள் திட்டம் இவ்வாறு ஒழுங்கமைக்கப்படலாம்:

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

சருமா, எங்கள் கட்டமைப்பு சுத்தமாகத் தோற்றமளிக்க முடியும்.

கருவிகளை அழைக்குவது எப்படி? அதுவே ஐடியா தானே? ஒரு கையாளுனர் ஒரு கருவியை அழைக்கும், எந்த கருவி எடுத்தாலும்? ஆம், அதுதான், இதோ அதற்கான குறியீடு:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools என்பது கருவி имен்கள் முக்கியங்களாக கொண்ட ஒரு அகராதி ஆகும்
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
    // TODO கருவியை அழைக்கவும்,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

மேலே கொடுக்கப்பட்ட குறியீடு போல, நாம் எது அழைக்கப்படும் கருவி மற்றும் அதன் கட்டளைகளை பிரிக்கவேண்டும், பின்னர் அந்த கருவியை அழைக்கவேண்டும்.

## சரிபார்ப்புடன் முறையை மேம்படுத்துதல்

இப்பொழுது வரை, கருவி, வளம் மற்றும் கேள்வித்தாள்களைச் சேர்க்கும் உங்கள் பதிவு முறையை இவ்வாறு இரண்டு கையாளுனர்களால் மாற்றலாம் என்பதைப் பார்த்தோம். மேலதிகம் என்ன செய்ய வேண்டும்? கருவி சரியான கட்டளைகளுடன் அழைக்கப்படுவதாக உறுதிப்படுத்த சரிபார்ப்பு ஒரு வடிவத்தைச் சேர்க்க வேண்டும். ஒவ்வொரு ரன்டைமுக்கும் இதற்கான தனி தீர்வு உள்ளது; உதாரணமாக Python Pydantic-ஐ பயன்படுத்துகிறது மற்றும் TypeScript Zod-ஐ பயன்படுத்துகிறது. கருத்து என்னவென்றால்:

- அம்சத்தை (கருவி, வளம் அல்லது கேள்வித்தாள்) உருவாக்கும் லாஜிக் அதற்கான அடைவு கோப்பகத்தில் மாற்றுவது.
- வருகை கோரிக்கையை சரிபார்க்கும் வழியைக் சேர்ப்பது, உதாரணமாக கருவி அழைக்கும்போது.

### ஒரு அம்சத்தை உருவாக்குதல்

ஒரு அம்சத்தை உருவாக்க, அதற்கான கோப்பை உருவாக்கி அதில் அவசியமான புலங்கள் உள்ளன என்பதை உறுதிப்படுத்தவேண்டும். இந்த புலங்கள் கருவிகள், வளங்கள் மற்றும் கேள்வித்தாள்களுக்கு சில வேறுபாடுகளை கொண்டிருக்கலாம்.

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
        # Pydantic மாடலை பயன்படுத்தி உள்ளீட்டை சரிபார்க்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # செய்யவேண்டும்: Pydantic ஐ சேர்க்கவும், இதனால் நாம் ஒரு AddInputModel உருவாக்கவும் மற்றும் args ஐ சரிபார்க்கவும் முடியும்

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

இங்கே நாம் பின்வரும் பணிகளை செய்கிறோம்:

- Pydantic இல் `AddInputModel` என்ற ஸ்கீமாவை `a` மற்றும் `b` புலங்களுடன் `schema.py` கோப்பில் உருவாக்குதல்.
- வருகை கோரிக்கையைக் `AddInputModel` வகைபோல் பகுப்பாய்வு செய்ய முயற்சி செய்தல்; புலங்கள் பொருந்தவில்லை என்றால் இது தோல்வி அடையும்:

   ```python
   # add.py
    try:
        # Pydantic மாதிரியை பயன்படுத்தி உள்ளீட்டை சரிபார்க்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

இந்த பகுப்பாய்வு லாஜிகைப் பணையை கருவி அழைப்பில் நேரடியாக அல்லது கையாளுனர் செயலியில் வைக்கலாம்.

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

- அனைத்து கருவி அழைப்புகளுக்கு பதிலளிக்கும் கையாளுனரில், வருகை கோரிக்கையை கருவியின் வரையறுக்கப்பட்ட ஸ்கீமாவாக பகுப்பாய்வு செய்ய முயற்சி செய்கிறது:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    அது வெற்றியடைந்தால், நாம் கருவியை அழைக்க முன்னேறும்:

    ```typescript
    const result = await tool.callback(input);
    ```

எப்படி என்றால், இந்த முறை ஒரு சிறந்த கட்டமைப்பை உருவாக்குகிறது, என்று *server.ts* என்பது மிகச் சிறிய கோப்பாகும், இது கோரிக்கை கையாளுனர்களை மட்டும் இணைக்கிறது மற்றும் ஒவ்வொரு அம்சமும் அதனுடைய கோப்பகத்தில் இருந்துள்ளதாலும் tools/, resources/ அல்லது /prompts/.

சரி, இதை அடுத்து உருவாக்க முயல்போம்.

## பயிற்சி: குறைந்த நிலை சர்வர் உருவாக்குதல்

இந்த பயிற்சியில், நாம் பின்வருவன செய்வோம்:

1. கருவிகள் பட்டியலிடுதல் மற்றும் அழைப்பின் கையாளும் குறைந்த நிலை சர்வரை உருவாக்குதல்.
1. மேம்படுத்தக்கூடிய கட்டமைப்புடன் செயல்படுத்துதல்.
1. கருவி அழைப்புகள் சரியாகச் சரிபார்க்கப்படுவதை உறுதிப்படுத்தும் சரிபார்ப்பைச் சேர்த்தல்.

### -1- கட்டமைப்பை உருவாக்குதல்

முதலில் நாம் கவனிக்க வேண்டியது, அதிக அம்சங்கள் சேர்க்கப்படும் போது அளவிட உதவும் கட்டமைப்பு. இதோ அது எப்படி இருக்கும்:

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

இதனால், tools என்ற கோப்பகத்தில் நமது கருவிகளை எளிதில் சேர்க்கலாம். resources மற்றும் prompts க்கும் துணைக்கோப்பகங்களைச் சேர்க்க இதை பின்பற்றலாம்.

### -2- ஒரு கருவி உருவாக்குதல்

அடுத்து ஒரு கருவி உருவாக்குவது எப்படி என்று பார்க்கலாம். முதலில் அது *tool* துணைக்கோப்பகத்தில் இருக்க வேண்டும்:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic மாதிரியை பயன்படுத்தி உள்ளீட்டை சரிபார்க்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # செயலாக்க வேண்டியது: Pydantic ஐச் சேர்க்கவும், இதனால் நாம் AddInputModel ஐ உருவாக்கி args ஐ சரிபார்க்கலாம்

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

இங்கு நாம் பெயர், விளக்கம் மற்றும் உள்ளீடு ஸ்கீமாவைப் Pydantic கொண்டு வரையறுக்கிறோம்; 그리고 கருவி அழைக்கப்படும் போது செயல்படும் கையாளுனரை வரையறுக்கிறோம். இறுதியாக `tool_add` என்னும் அகராதி அனைத்து பண்புகளையும் கொண்டுள்ளது.

மேலும், கருவி பயன்படுத்தும் உள்ளீடு ஸ்கீமாவை வரையறுக்கும் *schema.py* உள்ளது:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

மேலும் *__init__.py* ஐ நிரப்பி tools கோப்பகம் ஒரு மொட்யூலாக கருதப்படுவதை உறுதிசெய்வதும், அதில் உள்ள மொட்யூல்களை வெளியிடுவதும் சொல்லப்பட்டுள்ளன:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

இங்கே நாம் கருவிகளை கூட்டி சேர்க்கலாம்.

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

இங்கு நாம் பண்புகளைக் கொண்ட ஒரு அகராதி உருவாக்குகிறோம்:

- name, கருவியின் பெயர்.
- rawSchema, Zod ஸ்கீமா, கருவி அழைக்கும் வருகை கோரிக்கைகளைச் சரிபார்க்க பயன்படுத்தப்படும்.
- inputSchema, கையாளுனரால் பயன்படுத்தப்படும் ஸ்கீமா.
- callback, கருவியை அழைக்கும் 함수.

மேலும் `Tool` உள்ளது, இது இந்த அகராதியைக் `mcp server handler` ஏற்றுக்கொள்ளும் வகையாக மாற்றுகிறது, இதோ அது:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

மற்றும் உள்ளீடு ஸ்கீமாத் தொகுப்புகளை எங்கு வைத்துள்ளோம் என்றால் *schema.ts*, இங்கு தற்போது ஒரு ஸ்கீமா மட்டுமே இருக்கிறது, ஆனால் கருவிகள் அதிகரிக்கையில் மேலும் நுழைவுகள் சேர்க்கலாம்:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

சரி, அடுத்து கருவிகள் பட்டியலிடுவதை கையாளுவோம்.

### -3- கருவிகளை பட்டியலிட கையாளுதல்

அடுத்து, கருவி பட்டியலிடுவதற்கான கோரிக்கை கையாளுனரை அமைக்கவேண்டும். அதற்கு எங்கள் சர்வர் கோப்பில் வேணாம் இடுகை இதோ:

**Python**

```python
# சுருக்கத்துக்காக குறியீடு விலக்கப்பட்டது
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

இங்கு `@server.list_tools` என்ற அலங்காரி மற்றும் `handle_list_tools` என்ற செயலியை சேர்க்கின்றோம். இரண்டாம் செயலியில், கருவிகளின் பட்டியலை உருவாக்க வேண்டும். ஒவ்வொரு கருவிக்கும் பெயர், விளக்கம் மற்றும் inputSchema இருக்க வேண்டும் என்பதை கவனியுங்கள்.

**TypeScript**

கருவிகளை பட்டியலிடுவதற்கான கோரிக்கை கையாளுனரை அமைக்க, `setRequestHandler` ஐ சர்வერში அழைத்து, நாம் செய்யும் செயலுக்கு உட்பட்டு இருக்கும் ஸ்கீமாவை (இங்கே `ListToolsRequestSchema`) வழங்க வேண்டும்.

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
// சுருக்கமாகக் குறியீடு நீக்கப்பட்டது
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // பதிவு செய்யப்பட்ட கருவிகளின் பட்டியலைத் திருப்பி விடு
  return {
    tools: tools
  };
});
```

சரி, இப்போது கருவிகளை பட்டியலிடுவது முடிந்தது, அடுத்து கருவிகளை அழைப்பது எப்படி என்றே பார்ப்போம்.

### -4- கருவியை அழைக்க கையாளுதல்

கருவியை அழைப்பதற்கு, வேறு ஒரு கோரிக்கை கையாளுனரை அமைக்க வேண்டும், இது எந்த அம்சத்தை எந்த கட்டளைகளுடன் அழைக்க வேண்டும் என்பதைக் கவனிக்கும்.

**Python**

`@server.call_tool` என்ற அலங்காரியைப் பயன்படுத்தி `handle_call_tool` என்ற செயலியை உருவாக்குவோம். அதில் கருவி பெயர், அதன் கட்டளைகளைக் பிரித்து, அந்த கருவிக்கு கட்டளைகள் சரியானவையாக உள்ளதா என்று உறுதிசெய்யவேண்டும். கட்டளைகளை இங்கு அல்லது கருவி உள்ளே சரிபார்க்கலாம்.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # கருவிகள் என்பது கருவி பெயர்களை விசைகளாகக் கொண்ட அகராதி ஆகும்
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

இதில் என்ன நடக்கிறது:

- கருவி பெயர் `name` என்ற உள்ளீடு அளவுருவாக ஏற்கப்பட்டு உள்ளது; கட்டளைகள் `arguments` என்ற அகராதியாக உள்ளன.
- கருவி `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` என்று அழைக்கப்படுகிறது. கட்டளைகள் சரிபார்ப்பு `handler` பண்பில் செய்கிறது, இது ஒரு செயலியை குறிக்கிறது; தோல்வியடைந்தால் தவறு எழுப்பும்.

இப்போ நமக்கு குறைந்த நிலை சர்வர் வழியாக கருவிகளை பட்டியலிடுதல் மற்றும் அழைக்குதல் எப்படி என்பதை முழுமையாக புரிந்துகொண்டோம்.

[அனைத்து உதாரணம்](./code/README.md) இங்கே பார்க்கவும்.

## பணிக்கூறுகள்

உங்களுக்கு கொடுக்கப்பட்ட குறியீட்டினை பல கருவிகள், வளங்கள் மற்றும் கேள்வித்தாள்களுடன் விரிவாக்கி, கருவிகள் கோப்பகத்தில் மட்டும் கோப்புகளைச் சேர்ப்பதுதான் தேவையானது என்பதை கவனியுங்கள்.

*எந்த தீர்வும் கொடுக்கவில்லை*

## சுருக்கம்

இந்த அத்தியாயத்தில், குறைந்த நிலை சர்வர் முறையைப் பயன்படுத்துவது எப்படி என்று பார்த்தோம் மற்றும் இது எளிதான கட்டமைப்பை உருவாக்க உதவுகிறது என்பதையும் அறிந்தோம். சரிபார்ப்பு முக்கியத்துவம் மற்றும் உள்ளீடு சரிபார்ப்புக்கான ஸ்கீமாக்கலை உருவாக்கும் நூலகங்களுடன் எப்படி வேலை செய்ய வேண்டும் என்று கண்டோம்.

## அடுத்து என்ன

- அடுத்து: [எளிய அங்கீகாரம்](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**விரிவுரை**:  
இச் சான்றிதழ் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற செயற்கை அறிவு மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், இயந்திர மொழிபெயர்ப்பில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதில் கவனம் செலுத்தவும். தாய்மை மொழியில் இருக்கும் அசல் ஆவணத்தையே அதிகாரப்பூர்வமான மூலமாகப் கருத வேண்டும். முக்கிய தகவல்களுக்கு, நிபுணர் மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பு இல்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->