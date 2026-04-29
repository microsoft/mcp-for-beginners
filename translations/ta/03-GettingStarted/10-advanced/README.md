# மேம்பட்ட சர்வர் பயன்பாடு

MCP SDK-வில் இரண்டு விதமான சர்வர்கள் வெளியிடப்பட்டுள்ளன, உங்கள் சாதாரண சர்வர் மற்றும் குறைந்த மட்ட சர்வர். சாதாரணமாக, நீங்கள் அதில் அம்சங்களை சேர்க்க சாதாரண சர்வரைப் பயன்படுத்துவீர்கள். சில சந்தர்ப்பங்களில், கீழ் மட்ட சர்வரை நம்ப விரும்பலாம் பின்வருமாறு:

- சிறந்த கட்டமைப்பு. சாதாரண சர்வர் மற்றும் குறைந்த மட்ட சர்வர் இரண்டையும் கொண்டு ஒரு சுத்தமான கட்டமைப்பை உருவாக்க முடியும் ஆனால் குறைந்த மட்ட சர்வரில் சிறிது எளிதாகும் என்று வாதிடலாம்.
- அம்ச பயன்பாடு. சில மேம்பட்ட அம்சங்களை வெறும் குறைந்த மட்ட சர்வர் மூலம் மட்டுமே பயன்படுத்தலாம். இது பிற அத்தியாயங்களில் ஸாம்பிளிங் மற்றும் எலகிடேஷன் சேர்க்கையில் நீங்கள் காணப்போகிறீர்கள்.

## சாதாரண சர்வர் மற்றும் குறைந்த மட்ட சர்வர்

சாதாரண சர்வர் மூலம் MCP சர்வர் உருவாக்குவது பின்வருமாறு இருக்கும்

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

// ஒரு கூட்டும் கருவியைச் சேர்
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

நீங்கள் சர்வருக்கு வேண்டும் எனும் ஒவ்வொரு கருவி, வளம் அல்லது ப்ராம்ப்டை தெளிவாகச் சேர்க்கின்றீர்கள். இதில் எந்த தவறும் இல்லை.

### குறைந்த மட்ட சர்வர் அணுகுமுறை

ஆனால் குறைந்த மட்ட சர்வர் அணுகுமுறையைப் பயன்படுத்தும் போது, அதை வேறு முறையில் கருதி அவசியம் இரு ஹாண்ட்லர்களை உருவாக்க வேண்டும் (கருவிகள், வளங்கள் அல்லது ப்ராம்ப்ட்கள்) ஒவ்வொரு அம்ச வகைக்கும். உதாரணமாக கருவிகளுக்கு இரண்டு செயல்பாடுகள் உள்ளன:

- அனைத்து கருவிகளை பட்டியலிடுதல். ஒரு செயல்பாடு அனைத்து கருவிகளுக்கான பட்டியலை தயாரிக்கும்.
- அனைத்து கருவிகளுக்கு அழைப்பை கையாளல். இங்கு கூட ஒரு செயல்பாடு மட்டும் கருவி அழைப்புகளை கையாளும்.

இது கடமைகள் குறைவாக இருக்கலாம் அல்லையா? கருவியை பதிவு செய்வதை இடத்தில், நான் எல்லா கருவிகளையும் பட்டியலிடும் போace அது பட்டியலில் இருக்க வேண்டும், மற்றும் கருவியை அழைக்கும் கோரிக்கை வந்தால் அது அழைக்கப்பட வேண்டும் என உறுதி செய்தல் போதுமானது.

இப்போது குறைந்த மட்ட சர்வர் குறியீடு எப்படி இருக்கிறது பார்ப்போம்:

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
  // பதிவு செய்யப்பட்ட கருவிகளின் பட்டியலை வழங்குக
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

இங்கு ஒரு செயல்பாடு அம்சங்களின் பட்டியலை வழங்குகிறது. கருவி பட்டியலில் ஒவ்வொரு உள்ளீட்டிலும் `name`, `description` மற்றும் `inputSchema` போன்ற புலங்கள் உள்ளன, இது திரும்பும் வகையை பின்பற்றும். இதனால் கருவிகள் மற்றும் அம்ச வரையறைகளை வேறு இடத்தில் வைக்கக்கூடும். இப்போது நாம் அனைத்து கருவிகளையும் tools கோப்பகத்தில் உருவாக்கலாம், அதேபோல் உங்கள் அனைத்து அம்சங்களும் அமைந்துகொள்ளலாம் இதுதான் உங்கள் திட்டம் அப்படியே ஒழுங்கமைக்கப்படுமாறு ஒரு மாதிரியாக இருக்கலாம்:

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

சூப்பர், நமது கட்டமைப்பு மிகவும் சுத்தமாக தோன்றும்.

கருவிகளை அழைப்பது பற்றி என்ன? அதே யோசனைதான் அல்லவா, எந்த கருவியை வேண்டுமானாலும் ஒன்று ஹாண்ட்லர் தான் அழைக்கும்? ஆம், சரி, இதோ அதற்கான குறியீடு:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools என்பது கருவி பெயர்களைக் கீகளாக கொண்ட ஒரு அகராதி தான்
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

மேலுள்ள குறியீட்டை பார்த்தால், நாம் அழைக்க வேண்டிய கருவி மற்றும் அதற்கான_ARGUMENTS-ஐ பர்ஸிங் செய்ய வேண்டும், பிறகு கருவியை அழைக்க வேண்டும்.

## சரிபார்ப்புடன் அணுகுமுறை மேம்படுத்தல்

இதுவரை, கருவிகள், வளங்கள் மற்றும் ப்ராம்ப்ட்களை சேர்க்க உங்கள் பதிவு முறையை இரண்டு ஹாண்ட்லர்களால் மாற்ற முடியும் என்பதை பார்த்தீர்கள். இனிமேலும் என்ன செய்ய வேண்டும்? நிச்சயமாக, கருவி சரியாக அழைக்கப்படுவதை உறுதி செய்ய ஒரு வகை சரிபார்ப்பு சேர்க்க வேண்டும். ஒவ்வொரு ரன்டைமுக்கும் இதற்கு இயல்பான தீர்வு இருக்கிறது, எடுத்துக்காட்டாக Python Pydantic-ஐ பயன்படுத்துகிறது, TypeScript Zod-ஐப் பயன்படுத்துகிறது. யோசனை பின்வருமாறு:

- ஒரு அம்சத்தை (கருவி, வளம் அல்லது ப்ராம்ப்ட்) உருவாக்கும் தார்மீகமினலகத்தை அதன் குறிப்பிட்ட கோப்பகத்திற்கு மாற்ற. 
- ஒரு கோரிக்கையை பரிசோதிக்கும் வழியைச் சேர்க்கவும், உதாரணமாக ஒரு கருவியை அழைக்க விரும்புகிற கோரிக்கையை சரிபார்க்கவும்.

### ஒரு அம்சம் உருவாக்குதல்

ஒரு அம்சத்தை உருவாக்க, அந்த அம்சத்திற்கு ஒரு கோப்பை உருவாக்கி அவசியமான புலங்கள் உள்ளதா என உறுதி செய்ய வேண்டும். அந்த புலங்கள் கருவி, வளம் மற்றும் ப்ராம்ப்ட்களுக்கு சிறிது வேறுபடும்.

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
        # Pydantic மாதிரியுடன் உள்ளீட்டை பரிசோதிக்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # செய்வது: Pydantic ஐச் சேர்க்கவும், அதனால் நாம் AddInputModel ஐ உருவாக்கி args ஐ சரிபார்க்கலாம்

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

இதில் நாம் பின்வருமாறு செய்கிறோம்:

- Pydantic `AddInputModel` பயன்படுத்தி `a` மற்றும் `b` புலங்களுடன் ஒரு நிரலாக்க கோப்பை *schema.py*-ல் உருவாக்குதல்.
- வந்த கோரிக்கை `AddInputModel`வின் வகை என்று பர்ஸிங் செய்ய முயற்சிக்கும், புலங்கள் பொருந்தாவிட்டால் இது கோளாறு உண்டாக்கும்:

   ```python
   # add.py
    try:
        # Pydantic மாதிரியைப் பயன்படுத்தி உள்ளீட்டை சரிபார்க்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

நீங்கள் இந்த பர்ஸிங் வழிமுறையை கருவி அழைப்பில் அல்லது ஹாண்ட்லர் செயல்பாட்டில் வைக்க முடியும்.

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

- அனைத்து கருவி அழைப்புகளையும் கையாளும் ஹாண்ட்லரில், வந்த கோரிக்கை கருவியின் வரையறுக்கப்பட்ட கோவையில் பர்ஸிங் செய்ய முயற்சிக்கிறது:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    இது வெற்றிகரமாக இருந்தால், நாம் உண்மையான கருவியை அழைக்க proceed செய்கிறோம்:

    ```typescript
    const result = await tool.callback(input);
    ```

இந்த அணுகுமுறை ஒரு சிறந்த கட்டமைப்பை உருவாக்குகிறது, ஏனெனில் எல்லாவற்றுக்கும் தங்களுக்கான இடம் உள்ளது. *server.ts* என்பது மிகவும் சிறிய கோப்பு, இது மட்டும் கோரிக்கை ஹாண்ட்லர்களை இணைப்பதற்காகவே உள்ளது, மற்றும் ஒவ்வொரு அம்சமும் தங்கள் சொந்த கோப்பகத்தில் உள்ளது, அதாவது tools/, resources/ அல்லது /prompts/.

சரி, இதை அடுத்து உருவாக்க முயற்சிக்கலாம்.

## பயிற்சி: குறைந்த மட்ட சர்வர் உருவாக்கல்

இந்த பயிற்சியில், நாம் பின்வருமாறு செய்வோம்:

1. கருவிகளை பட்டியலிடுதல் மற்றும் அழைப்பை கையாளும் குறைந்த மட்ட சர்வர் உருவாக்குதல்.
1. மேம்படுத்தக்கூடிய கட்டமைப்பை நடைமுறைப்படுத்துதல்.
1. உங்கள் கருவி அழைப்புகள் சரியாக சரிபார்ப்படுவதை உறுதி செய்ய சரிபார்ப்பைச் சேர்க்கவும்.

### -1- கட்டமைப்பை உருவாக்குதல்

நாம் முதலில் கவனிக்க வேண்டியது கட்டமைப்பு, இது கூடுதலாக அம்சங்களைச் சேர்க்க உதவும், இது இதுபோல இருக்கும்:

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

இப்போது நாங்கள் tools கோப்பகத்தில் புதிய கருவிகளை எளிதில் சேர்க்கக்கூடிய கட்டமைப்பை அமைத்துவிட்டோம். resources மற்றும் prompts க்கான துணை கோப்பகங்களையும் இதில் சேர்க்கலாம்.

### -2- கருவி உருவாக்குதல்

இப்போது அடுத்ததாக ஒரு கருவியை உருவாக்குவது எப்படி என்பதை பார்க்கலாம். முதலில் அது *tool* துணை கோப்பகத்தில் உருவாக வேண்டும் பின்வருமாறு:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic மொடல் பயன்படுத்தி உள்ளீட்டை சரிபார்க்கவும்
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ஐச் சேர்க்கவும், ஆகவே நாம் AddInputModel ஐ உருவாக்கி args ஐ சரிபார்க்க முடியும்

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

இதில் நாம் பெயர், விளக்கம் மற்றும் Pydantic மூலம் உள்ளீட்டு கோவையை வரையறுக்கும் விதத்தை காண்கிறோம் மற்றும் இந்த கருவி அழைக்கப்படும் போது இயக்கப்படும் ஹாண்ட்லர் உள்ளது. இறுதியில், அனைத்து பண்புகளையும் கொண்ட `tool_add` என்ற அகராதியை வெளிப்படுத்துகிறோம்.

மேலும் *schema.py* உள்ளது, இது கருவியின் உள்ளீட்டு கோவையை வரையறுக்க பயன்படுத்தப்படுகிறது:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

மேலும் *__init__.py* கோப்பை நிரப்ப அவரிக் கருவிகள் கோப்பகம் தொகுப்பாக கருதப்படுவதை உறுதி செய்ய வேண்டும். கூடுதலாக, உள்ளமைப்புகளை பின்வருமாறு வெளிப்படுத்த வேண்டும்:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

நாம் கருவிகள் கூடியபோது இந்த கோப்பில் தொடர்ச்சியாக சேர்க்கலாம்.

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

இங்க 우리는 பண்புகளால் ஆன அகராதி ஒன்றை உருவாக்குகிறோம்:

- name, இது கருவியின் பெயர்.
- rawSchema, இது Zod கோவில், இது கருவியை அழைக்கும் வருகைகளை சரிபார்க்க பயன்படுத்தப்படும்.
- inputSchema, இந்த கோவை ஹாண்ட்லரால் பயன்படுத்தப்படும்.
- callback, இது கருவியை இயக்க பயன்படுத்தப்படும்.

மேலும், `Tool` உள்ளது, இது இந்த அகராதியை mcp சர்வர் ஹாண்ட்லர் ஏற்றுக்கொள்ளக்கூடிய வகையாக மாற்றுகிறது:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

மேலும் *schema.ts* உள்ளது, இங்கு ஒவ்வொரு கருவிக்கும் உள்ளீட்டு கோவைகள் சேமிக்கப்படுகின்றன. தற்போது ஒரு கோவை மட்டும் உள்ளது, ஆனால் கருவிகள் சேர்க்கப்பட்டால் மேலும் உள்ளீடுகள் சேர்க்கலாம்:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

சிறந்தது, இப்போது கருவிகளை பட்டியலிடுவதை கையாளுவோம்.

### -3- கருவி பட்டியலை கையாளுதல்

அடுத்து, கருவிகளை பட்டியலிடுவதற்கான கோரிக்கை ஹாண்ட்லரை அமைக்க வேண்டும். இதோ சர்வர் கோப்பில் சேர்க்க வேண்டியது:

**Python**

```python
# சுருக்கத்துக்காக குறியீடு நீக்கப்பட்டுள்ளது
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

இங்கு, `@server.list_tools` அலங்காரக் குறியீட்டு மற்றும் அதை செயல்படுத்தும் `handle_list_tools` செயல்பாடு சேர்க்கப்பட்டுள்ளன. இந்த செயல்பாட்டில், கருவிகளின் பட்டியலை உருவாக்க வேண்டும். எவ்வொரு கருவிக்கும் பெயர், விளக்கம் மற்றும் inputSchema வேண்டும் என்பதை கவனியுங்கள்.

**TypeScript**

கருவிகள் பட்டியலிடும் கோரிக்கைக்கு ஹாண்ட்லரை அமைக்க, சர்வரில் `setRequestHandler` ஐ அழைக்கும் போது இயங்கும் கோவை `ListToolsRequestSchema` என்று வரையறுக்க வேண்டும்:

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
// குறும்படத்துக்காக குறியீடு ஒதுக்கப்பட்டது
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // பதிவு செய்யப்பட்ட கருவிகளின் பட்டியலைத் திருப்பி வழங்கவும்
  return {
    tools: tools
  };
});
```

சரி, இப்போது கருவிகள் பட்டியலிடல் முடிந்துவிட்டது. அடுத்ததாக கருவிகளை அழைக்கும் முறையை பார்ப்போம்.

### -4- கருவியை அழைப்பதை கையாளுதல்

கருவியை அழைக்க, வேறு ஒரு கோரிக்கை ஹாண்ட்லரை அமைக்க வேண்டும். இப்போது எந்த அம்சத்தை எந்த arguments-உடன் அழைக்க வேண்டும் என்பதை கவனம் செலுத்தும்.

**Python**

`@server.call_tool` அலங்கார குறியீட்டை பயன்படுத்தி `handle_call_tool` என்ற செயல்பாட்டை நடைமுறைப்படுத்துவோம். இந்த செயல்பாட்டில், கருவியின் பெயர், அதன் argument ஆகியவற்றை வேறு எடுத்து அந்த argument-கள் சரியானவை என்பது உறுதி செய்ய வேண்டும். இந்த சரிபார்ப்பை இந்த செயல்பாட்டிலோ அல்லது உண்மையான கருவியில் பின் கட்டத்தில் செய்யலாம்.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # கருவி பெயர்கள் விசைகளாக உள்ள ஒரு அகராதி ஆகும்
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

இதோ என்ன நடக்கிறது:

- நமது கருவி பெயர் உள்ளது உள்ளீட்டு அளவுரு `name` எனும் புலத்தில், மற்றும் வாதங்கள் `arguments` அகராதியில் உள்ளன.

- கருவி கொடுக்கப்பட்ட `handler` புலத்தை await செய்து அழைக்கப்படுகிறது: `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. arguments சரிபார்ப்பு `handler` ஆகும் செயல்பாட்டில் நடக்கிறது, அது தோல்வியுற்றால் விபத்து எழும்.

இதனால், குறைந்த மட்ட சர்வர் மூலம் கருவிகளை பட்டியலிடுதல் மற்றும் அழைக்கும் முறையை நாங்கள் முழுமையாக புரிந்துகொண்டோம்.

[முழு எடுத்துக்காட்டை](./code/README.md) இங்கே பாருங்கள்

## பணிமுறை

உங்களுக்கு கொடுக்கப்பட்ட குறியீட்டை பல கருவிகள், வளங்கள் மற்றும் ப்ராம்ப்ட்களுடன் விரிவுபடுத்தி, நீங்கள் தவிர வேறு எங்கேயும் கோப்புகளைச் சேர்க்க வேண்டியதில்லை என்பதை கவனியுங்கள்.

*பதிலளிப்பு இல்லை*

## சுருக்கம்

இந்த அத்தியாயத்தில், குறைந்த மட்ட சர்வர் அணுகுமுறை எப்படி வேலை செய்கிறது மற்றும் அது எவ்வாறு நன்மையான கட்டமைப்பை உருவாக்க உதவுகிறது என்பதைக் கண்டோம். மேலும், சரிபார்ப்பு பற்றி விவாதித்தோம் மற்றும் உள்ளீட்டு சரிபார்ப்பு கோவைகளை உருவாக்க_validation நூலகங்கள் பயன்படுத்துவதைக் கற்றோம்.

## அடுத்தது

- அடுத்து: [எளிய பற்றாக்குறை](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**எச்சரிக்கை**:
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற செயற்கை நுண்ணறிவு மொழிமாற்ற சேவையை பயன்படுத்தி மொழிமாற்றம் செய்யப்பட்டுள்ளது. நம்முடைய முயற்சி நெறிப்படுத்துதலுக்காக இருந்தாலும், தானாகும் மொழிமாற்றங்களில் பிழைகள் அல்லது தவறுகள் இருக்க வாய்ப்பு உள்ளது என்பதைக் கவனத்தில் கொள்ளவும். ஒригинல் ஆவணம் அதன் மொழியில் அதிகாரப்பூர்வ மூலமாகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு தொழில்முறை மனித மொழிமாற்றம் பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதனால் ஏற்படும் எந்தவொரு தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பு ஏற்கவில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->