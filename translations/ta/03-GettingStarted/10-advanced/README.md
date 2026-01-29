# மேம்பட்ட சர்வர் பயன்பாடு

MCP SDK-யில் இரண்டு விதமான சர்வர்கள் உள்ளன: உங்கள் சாதாரண சர்வர் மற்றும் குறைந்த நிலை சர்வர். பொதுவாக, நீங்கள் சாதாரண சர்வரை பயன்படுத்தி அதில் அம்சங்களைச் சேர்ப்பீர்கள். ஆனால் சில சந்தர்ப்பங்களில், நீங்கள் குறைந்த நிலை சர்வரை பயன்படுத்த விரும்புவீர்கள், உதாரணமாக:

- சிறந்த கட்டமைப்பு. சாதாரண சர்வர் மற்றும் குறைந்த நிலை சர்வர் இரண்டையும் பயன்படுத்தி சுத்தமான கட்டமைப்பை உருவாக்க முடியும், ஆனால் குறைந்த நிலை சர்வருடன் இது சற்று எளிதாக இருக்கலாம்.
- அம்சங்களின் கிடைக்குமிடம். சில மேம்பட்ட அம்சங்கள் குறைந்த நிலை சர்வருடன் மட்டுமே பயன்படுத்த முடியும். இது பின்னர் அத்தியாயங்களில் நீங்கள் vz;பார்ப்பீர்கள், எSamples மற்றும் elicitation சேர்க்கும்போது.

## சாதாரண சர்வர் vs குறைந்த நிலை சர்வர்

இங்கே MCP Server-ஐ சாதாரண சர்வர் மூலம் உருவாக்குவது எப்படி இருக்கும் என்பதைப் பாருங்கள்:

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

இங்கே முக்கியமானது, நீங்கள் சர்வருக்கு தேவையான ஒவ்வொரு கருவி, வளம் அல்லது prompt-ஐ தெளிவாகச் சேர்க்க வேண்டும். இதில் எந்த தவறும் இல்லை.

### குறைந்த நிலை சர்வர் அணுகுமுறை

ஆனால், நீங்கள் குறைந்த நிலை சர்வர் அணுகுமுறையைப் பயன்படுத்தும்போது, நீங்கள் வேறுபட்ட முறையில் யோசிக்க வேண்டும். அதாவது ஒவ்வொரு அம்ச வகைக்கும் (கருவிகள், வளங்கள் அல்லது prompts) இரண்டு ஹேண்ட்லர்களை உருவாக்க வேண்டும். உதாரணமாக கருவிகள், அப்போது இரண்டு செயல்பாடுகள் மட்டுமே இருக்கும்:

- அனைத்து கருவிகளையும் பட்டியலிடுதல். ஒரு செயல்பாடு அனைத்து கருவிகளை பட்டியலிட முயற்சிக்க பொறுப்பாக இருக்கும்.
- அனைத்து கருவிகளையும் அழைப்பதற்கான செயல்பாடு. இங்கே, ஒரு கருவியை அழைப்பதற்கான அனைத்து கோரிக்கைகளையும் ஒரே செயல்பாடு கையாளும்.

இது சற்றே குறைவான வேலைபாடாக இருக்கிறதா? அதாவது, ஒரு கருவியை பதிவு செய்வதற்குப் பதிலாக, நான் அனைத்து கருவிகளையும் பட்டியலிடும்போது அந்த கருவி பட்டியலில் இருக்க வேண்டும் என்பதையும், ஒரு கருவியை அழைக்க கோரிக்கை வந்தால் அது அழைக்கப்பட வேண்டும் என்பதையும் உறுதிப்படுத்த வேண்டும்.

இப்போது குறியீடு எப்படி இருக்கும் என்பதைப் பார்ப்போம்:

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

இங்கே, ஒரு செயல்பாடு அம்சங்களின் பட்டியலைத் திருப்புகிறது. கருவிகளின் பட்டியலில் உள்ள ஒவ்வொரு நுழைவும் `name`, `description` மற்றும் `inputSchema` போன்ற புலங்களை கொண்டிருக்க வேண்டும். இது நமது கருவிகள் மற்றும் அம்ச வரையறையை வேறு இடத்தில் வைக்க அனுமதிக்கிறது. இப்போது உங்கள் கருவிகளை ஒரு *tools* கோப்பகத்தில் உருவாக்கலாம், அதேபோல் உங்கள் அனைத்து அம்சங்களையும், எனவே உங்கள் திட்டம் இப்படி அமைக்கப்படலாம்:

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

அதிகப்பட்சம், நமது கட்டமைப்பு மிகவும் சுத்தமாக இருக்கலாம்.

கருவிகளை அழைப்பது எப்படி? அதே யோசனைதானா, ஒரு ஹேண்ட்லர் ஒரு கருவியை அழைக்க, எந்த கருவி என்றாலும்? ஆம், சரியாக, இதற்கான குறியீடு இங்கே:

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

மேலே உள்ள குறியீட்டில் நீங்கள் காணலாம், நாம் அழைக்க வேண்டிய கருவியை, எந்த வாதங்களுடன் அழைக்க வேண்டும் என்பதைப் பிரித்தெடுக்க வேண்டும், பின்னர் அந்த கருவியை அழைக்க தொடர வேண்டும்.

## அணுகுமுறையை சரிபார்ப்புடன் மேம்படுத்துதல்

இப்போது வரை, நீங்கள் கருவிகள், வளங்கள் மற்றும் prompts சேர்க்கும் உங்கள் அனைத்து பதிவுகளையும் ஒவ்வொரு அம்ச வகைக்கும் இந்த இரண்டு ஹேண்ட்லர்களால் மாற்ற முடியும் என்பதைப் பார்த்தீர்கள். இன்னும் என்ன செய்ய வேண்டும்? நன்றாக, ஒரு கருவி சரியான வாதங்களுடன் அழைக்கப்படுகிறதா என்பதை உறுதிப்படுத்த ஒரு வகையான சரிபார்ப்பைச் சேர்க்க வேண்டும். ஒவ்வொரு runtime-க்கும் இதற்கான தங்கள் சொந்த தீர்வு உள்ளது, உதாரணமாக Python Pydantic-ஐ பயன்படுத்துகிறது, TypeScript Zod-ஐ பயன்படுத்துகிறது. யோசனை என்னவென்றால், நாம் இதைச் செய்வோம்:

- ஒரு அம்சத்தை (கருவி, வளம் அல்லது prompt) உருவாக்கும் தார்மீகத்தை அதன் தனிப்பட்ட கோப்பகத்திற்கு நகர்த்தவும்.
- ஒரு கருவியை அழைக்க கோரிக்கை வரும்போது அதை சரிபார்க்க ஒரு வழியைச் சேர்க்கவும்.

### ஒரு அம்சத்தை உருவாக்குதல்

ஒரு அம்சத்தை உருவாக்க, அந்த அம்சத்திற்கான ஒரு கோப்பை உருவாக்கி, அந்த அம்சத்திற்குத் தேவையான கட்டாய புலங்கள் உள்ளதா என்பதை உறுதிப்படுத்த வேண்டும். எந்த புலங்கள் கருவிகள், வளங்கள் மற்றும் prompts இடையே சற்று மாறுபடும்.

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

இங்கே நீங்கள் பின்வருவதைப் பார்க்கலாம்:

- *schema.py* கோப்பில் `AddInputModel` என்ற Pydantic-ஐப் பயன்படுத்தி `a` மற்றும் `b` புலங்களுடன் ஒரு schema உருவாக்குதல்.
- வரவிருக்கும் கோரிக்கையை `AddInputModel` வகையாக parse செய்ய முயற்சிக்கிறது, பராமETERS-ல் பிழை இருந்தால் இது crash ஆகும்:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

இந்த parsing logic-ஐ கருவி அழைப்பில் அல்லது ஹேண்ட்லர் செயல்பாட்டில் வைக்க நீங்கள் தேர்வு செய்யலாம்.

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

- அனைத்து கருவி அழைப்புகளை கையாளும் ஹேண்ட்லரில், நாம் வரவிருக்கும் கோரிக்கையை கருவியின் வரையறுக்கப்பட்ட schema-க்கு parse செய்ய முயற்சிக்கிறோம்:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    அது வேலை செய்தால், பின்னர் நாங்கள் உண்மையான கருவியை அழைக்க தொடருகிறோம்:

    ```typescript
    const result = await tool.callback(input);
    ```

நீங்கள் காணலாம், இந்த அணுகுமுறை ஒரு சிறந்த கட்டமைப்பை உருவாக்குகிறது, ஏனெனில் ஒவ்வொன்றும் அதன் இடத்தில் உள்ளது, *server.ts* ஒரு மிகச் சிறிய கோப்பு மட்டுமே, இது கோரிக்கை ஹேண்ட்லர்களை இணைக்கிறது, ஒவ்வொரு அம்சமும் அதன் தனிப்பட்ட கோப்பகத்தில் உள்ளது, அதாவது tools/, resources/ அல்லது /prompts.

சிறந்தது, இதை அடுத்ததாக உருவாக்க முயற்சிப்போம்.

## பயிற்சி: குறைந்த நிலை சர்வரை உருவாக்குதல்

இந்த பயிற்சியில், நாம் பின்வருவதைச் செய்வோம்:

1. கருவிகளை பட்டியலிடுவதையும், கருவிகளை அழைப்பதையும் கையாளும் ஒரு குறைந்த நிலை சர்வரை உருவாக்குங்கள்.
1. நீங்கள் கட்டமைக்கக்கூடிய ஒரு கட்டமைப்பை செயல்படுத்துங்கள்.
1. உங்கள் கருவி அழைப்புகள் சரியாக சரிபார்க்கப்படுவதை உறுதிப்படுத்த validation சேர்க்கவும்.

### -1- ஒரு கட்டமைப்பை உருவாக்குதல்

முதலில், நாம் அதிக அம்சங்களைச் சேர்க்கும்போது எங்களுக்கு அளவீட்டில் உதவும் ஒரு கட்டமைப்பை உருவாக்க address செய்ய வேண்டும், இதோ அது எப்படி இருக்கும்:

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

இப்போது, நாம் ஒரு tools கோப்பகத்தில் புதிய கருவிகளை எளிதாகச் சேர்க்க முடியும் என்பதை உறுதிப்படுத்தும் ஒரு கட்டமைப்பை அமைத்துள்ளோம். resources மற்றும் prompts-க்கு துணை கோப்பகங்களைச் சேர்க்க இந்த வழிமுறையை பின்பற்றலாம்.

### -2- ஒரு கருவியை உருவாக்குதல்

அடுத்ததாக, ஒரு கருவியை உருவாக்குவது எப்படி இருக்கும் என்பதைப் பார்ப்போம். முதலில், அது அதன் *tool* துணை கோப்பகத்தில் உருவாக்கப்பட வேண்டும், இப்படி:

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

இங்கே நாம் காண்பது, name, description, Pydantic-ஐப் பயன்படுத்தி ஒரு input schema மற்றும் இந்த கருவி அழைக்கப்படும் போது invoke செய்யப்படும் ஒரு ஹேண்ட்லரை வரையறுக்கிறோம். இறுதியாக, `tool_add`-ஐ dictionary ஆக வெளிப்படுத்துகிறோம், இது இந்த அனைத்து பண்புகளையும் கொண்டுள்ளது.

மேலும், *schema.py* உள்ளது, இது நமது கருவி பயன்படுத்தும் input schema-ஐ வரையறுக்க பயன்படுத்தப்படுகிறது:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

நாம் *__init__.py*-ஐ populate செய்ய வேண்டும், tools கோப்பகம் ஒரு module ஆக கருதப்படுவதை உறுதிப்படுத்த. கூடுதலாக, நாம் அதன் modules-ஐ இப்படி வெளிப்படுத்த வேண்டும்:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

நாம் மேலும் கருவிகளைச் சேர்க்கும்போது இந்த கோப்பில் சேர்க்கலாம்.

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

இங்கே நாம் பண்புகளின் dictionary-ஐ உருவாக்குகிறோம்:

- name, இது கருவியின் பெயர்.
- rawSchema, இது Zod schema, இது இந்த கருவியை அழைக்க வரவிருக்கும் கோரிக்கைகளை validate செய்ய பயன்படுத்தப்படும்.
- inputSchema, இந்த schema ஹேண்ட்லரால் பயன்படுத்தப்படும்.
- callback, இது கருவியை invoke செய்ய பயன்படுத்தப்படும்.

`Tool` உள்ளது, இது dictionary-ஐ MCP server ஹேண்ட்லர் ஏற்கக்கூடிய வகையாக மாற்ற பயன்படுத்தப்படுகிறது, இது இப்படி இருக்கும்:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

மேலும், *schema.ts* உள்ளது, இது ஒவ்வொரு கருவிக்கான input schemas-ஐ சேமிக்க பயன்படுத்தப்படுகிறது, இது தற்போது ஒரு schema மட்டுமே கொண்டுள்ளது, ஆனால் நாம் மேலும் கருவிகளைச் சேர்க்கும்போது மேலும் entries சேர்க்கலாம்:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

சிறந்தது, அடுத்ததாக நமது கருவிகளை பட்டியலிட கையாள்வதைத் தொடங்குவோம்.

### -3- கருவி பட்டியலிட கையாளுதல்

அடுத்ததாக, நமது கருவிகளை பட்டியலிட கையாள, அதற்கான ஒரு கோரிக்கை ஹேண்ட்லரை அமைக்க வேண்டும். இதோ நமது சர்வர் கோப்பில் சேர்க்க வேண்டியது:

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

இங்கே, நாம் `@server.list_tools` என்ற decorator-ஐ சேர்க்கிறோம் மற்றும் `handle_list_tools` என்ற செயல்பாட்டை செயல்படுத்துகிறோம். பின்னர், நாம் கருவிகளின் பட்டியலை உருவாக்க வேண்டும். ஒவ்வொரு கருவியும் name, description மற்றும் inputSchema கொண்டிருக்க வேண்டும் என்பதை கவனிக்கவும்.

**TypeScript**

கருவிகளை பட்டியலிட கோரிக்கை ஹேண்ட்லரை அமைக்க, நாம் `setRequestHandler`-ஐ சர்வரில் அழைக்க வேண்டும், இது நாம் செய்ய முயற்சிக்கும் செயல்பாட்டிற்கு பொருந்தும் schema-ஐ கொண்டிருக்க வேண்டும், இந்தச் சந்தர்ப்பத்தில் `ListToolsRequestSchema`.

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

சிறந்தது, இப்போது நமது கருவிகளை பட்டியலிடும் பகுதியை தீர்வு செய்துள்ளோம், அடுத்ததாக கருவிகளை அழைப்பது எப்படி இருக்கும் என்பதைப் பார்ப்போம்.

### -4- ஒரு கருவியை அழைக்க கையாளுதல்

ஒரு கருவியை அழைக்க, ஒரு request handler-ஐ அமைக்க வேண்டும், இது எந்த அம்சத்தை அழைக்க வேண்டும் மற்றும் எந்த வாதங்களுடன் என்பதை கையாளும்.

**Python**

நாம் `@server.call_tool` என்ற decorator-ஐ பயன்படுத்துவோம் மற்றும் `handle_call_tool` என்ற செயல்பாட்டுடன் அதை செயல்படுத்துவோம். அந்த செயல்பாட்டில், நாம் கருவியின் பெயர், அதன் வாதங்கள் மற்றும் அந்த கருவிக்கு பொருந்தும் வாதங்கள் சரிபார்க்கப்படுகிறதா என்பதை parse செய்ய வேண்டும். இந்த செயல்பாட்டில் அல்லது கீழே உள்ள கருவியில் validation செய்யலாம்.

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

இங்கே என்ன நடக்கிறது:

- நமது கருவியின் பெயர் `name` என்ற input parameter ஆகவே உள்ளது, இது `arguments` dictionary வடிவில் உள்ள வாதங்களுக்கும் பொருந்தும்.

- கருவி `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` மூலம் அழைக்கப்படுகிறது. வாதங்களின் validation `handler` property-யில் நடக்கிறது, இது ஒரு செயல்பாட்டைச் சுட்டுகிறது, அது தோல்வியடையுமானால் exception throw செய்யும்.

இங்கே, கருவிகளை பட்டியலிடுவதையும், குறைந்த நிலை சர்வரைப் பயன்படுத்தி கருவிகளை அழைப்பதையும் முழுமையாக புரிந்துகொண்டுள்ளோம்.

[முழு உதாரணத்தை](./code/README.md) இங்கே பாருங்கள்

## பணிக்கூற்று

உங்களுக்கு வழங்கப்பட்ட குறியீட்டுடன் பல கருவிகள், வளங்கள் மற்றும் prompts சேர்க்கவும், மேலும் நீங்கள் tools கோப்பகத்தில் மட்டுமே கோப்புகளைச் சேர்க்க வேண்டும் என்பதை கவனிக்கவும்.

*தீர்வு வழங்கப்படவில்லை*

## சுருக்கம்

இந்த அத்தியாயத்தில், குறைந்த நிலை சர்வர் அணுகுமுறை எப்படி வேலை செய்கிறது என்பதைப் பார்த்தோம், மேலும் அதை நாம் கட்டமைக்கக்கூடிய ஒரு நல்ல கட்டமைப்பை உருவாக்க உதவுகிறது. validation பற்றியும் விவாதித்தோம், மேலும் input validation க்கான schemas உருவாக்க validation libraries-ஐ எப்படி வேலை செய்ய வேண்டும் என்பதை உங்களுக்கு காட்டப்பட்டது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்செயல்முறையை உறுதிப்படுத்த முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.