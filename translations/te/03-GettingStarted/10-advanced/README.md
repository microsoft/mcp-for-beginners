# అధునాతన సర్వర్ ఉపయోగం

MCP SDKలో రెండు విభిన్న రకాల సర్వర్లు అందుబాటులో ఉన్నాయి, మీ సాధారణ సర్వర్ మరియు లో-లెవల్ సర్వర్. సాధారణంగా, మీరు ఫీచర్స్‌ను జోడించడానికి సాధారణ సర్వర్‌ను ఉపయోగిస్తారు. కానీ కొన్ని సందర్భాలలో, మీరు లో-లెవల్ సర్వర్‌పై ఆధారపడాలనుకుంటారు, ఉదాహరణకి:

- మెరుగైన ఆర్కిటెక్చర్. సాధారణ సర్వర్ మరియు లో-లెవల్ సర్వర్ రెండింటినీ కలిపి క్లియర్ ఆర్కిటెక్చర్ క్రియేట్ చేయవచ్చు, కానీ లో-లెవల్ సర్వర్‌తో ఇది కొంచెం సులభం అని చెప్పవచ్చు.
- ఫీచర్ అందుబాటు. కొన్ని అధునాతన ఫీచర్స్‌ను కేవలం లో-లెవల్ సర్వర్‌తోనే ఉపయోగించవచ్చు. మీరు దీనిని తర్వాత అధ్యాయాలలో సాంప్లింగ్ మరియు elicitation జోడిస్తున్నప్పుడే చూడగలరు.

## సాధారణ సర్వర్ వర్సెస్ లో-లెవల్ సర్వర్

క్రింద సాధారణ సర్వర్‌తో MCP సర్వర్ క్రియేషన్ ఎలా ఉంటుందో ఉంది

**Python**

```python
mcp = FastMCP("Demo")

# ఒక జోడింపు సాధనాన్ని చేర్చండి
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

// ఒక జోడింపు సాధనాన్ని జతచేయండి
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

పాయింట్ ఏమిటంటే మీరు స్పష్టంగా సర్వర్‌లో కావలసిన ప్రతి టూల్, రిసోర్స్ లేదా ప్రాంప్ట్‌ను జోడిస్తున్నారు. ఇందులో పొరపాటు లేదు.  

### లో-లెవల్ సర్వర్ పద్ధతి

అయితే, లో-లెవల్ సర్వర్ పద్ధతి ఉపయోగిస్తున్నప్పుడు మీరు వేరుగా ఆలోచించాలి. ప్రతి టూల్‌ను రిజిస్టర్ చేయడం మధ్య, మీరు ప్రతి ఫీచర్ రకం (టూల్స్, రిసోర్సెస్ లేదా ప్రాంప్ట్‌లు) కు రెండు హ్యాండ్లర్స్ సృష్టిస్తారు. ఉదాహరణకి, టూల్స్‌కి కేవలం ఈ రెండు ఫంక్షన్స్ ఉంటాయి:

- అన్ని టూల్స్‌ని జాబితా చేయడం. ఒక ఫంక్షన్ అన్ని టూల్స్ జాబితా చేయడంలో బాధ్యత వహిస్తుంది.
- అన్ని టూల్స్ కాల్స్‌ను హ్యాండిల్ చేయడం. ఇక్కడ కూడా ఒక్క హ్యాండ్లర్ టూల్‌కు కాల్ చేయడాన్ని నిర్వహిస్తుంది.

ఇది తగ్గిన పనిగా అనిపిస్తుందా? కాబట్టి టూల్‌ను రిజిస్టర్ చేయడం బదులు, మీరు అన్ని టూల్స్ జాబితా చేసినప్పుడు టూల్ ఉన్నదని నిర్ధారించాలి, మరియు టూల్ కాల్ రావడాన్ని కూడా చెలామణీ చేయాలి.  

ఇప్పుడు కోడ్ ఎలా ఉందో చూద్దాం:

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
  // నమోదు చేసిన టూల్‌ల జాబితాను ఇవ్వండి
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

ఇక్కడ ఇప్పుడు ఒక ఫంక్షన్ ఫీచర్స్ జాబితాను ఇస్తుంది. టూల్స్ జాబితాలో ప్రతి ఎంట్రీకి `name`, `description` మరియు `inputSchema` వంటి ఫీల్డ్‌లు ఉన్నాయి రాబ్యాక్ టైప్‌ను అనుసరించి. ఇది మన టూల్స్ మరియు ఫీచర్ నిర్వచనాన్ని వేరే చోట ఉంచడానికి సహాయపడుతుంది. ఇప్పుడు మనం టూల్స్ ఫోల్డర్‌లో అన్ని టూల్స్ సృష్టించగలమో అలాగే మీ ప్రాజెక్ట్ లాంటి విధంగా క్రమబద్ధీకరించవచ్చు:

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

అదెంతో బాగుంది, మన ఆర్కిటెక్చర్‌ను చక్కగా చేయవచ్చు.

టూల్స్ కాల్ చేయడం ఎలా ఉంటుంది, అదే ఆలోచనా విధానమా? ఓ టూల్ కాల్ చేయడానికి ఓ హ్యాండ్లర్, ఏ టూల్ అయినా? అవును, ఖచ్చితంగా, దీని కోడ్ ఇక్కడ ఉంది:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools అనేది పరికరాల పేర్లను కీలు గా కలిగి ఉన్న ఒక డిక్షనరీ.
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
    // TODO సాధనాన్ని పిలవండి,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

పైన కోడ్ నుంచి మీరు చూడగలిగితే, మనం కాల్ చేసే టూల్ ఏమిటి మరియు ఏ ఆర్గ్యుమెంట్లతో కలర్ చేయాలో పాయింట్ చేస్తూ, ఆ తర్వాత టూల్‌ను కాల్ చేస్తాం.

## వెరిఫికేషన్‌తో పద్ధతి మెరుగుదల

ఇప్పటి వరకు, మీరు టూల్స్, రిసోర్సెస్ మరియు ప్రాంప్ట్‌లను జోడించేందుకు అన్ని రిజిస్ట్రేషన్లను ఈ రెండు హ్యాండ్లర్స్‌తో ప్రతిస్థాపించగలమని తెలుసుకున్నారు. ఇంకేమి చేయాలి? సరైన ఆర్గ్యుమెంట్లతో టూల్ కాల్ కావడానికి కొంత వెరిఫికేషన్ చేర్చాలి. ప్రతి రన్‌టైమ్ ఈ పని కోసం వారి స్వంత పరిష్కారం ఉంటాయి, ఉదాహరణకి Python Pydantic ఉపయోగిస్తుంది, TypeScript Zod ఉపయోగిస్తుంది. ఆలోచన ఈ విధంగా:

- ఫీచర్ (టూల్, రిసోర్స్ లేదా ప్రాంప్ట్) క్రియేట్ చేసే లాజిక్ దాని ప్రత్యేక ఫోల్డర్‌కు కదిలించాలి.
- టూల్ కాల్ చేసేందుకు వచ్చిన రిక్వెస్ట్‌ని సరైనదిగా వెరిఫై చేయడం అవసరం.

### ఫీచర్ సృష్టించాలి

ఫీచర్ సృష్టించాలంటే, ఆ ఫీచర్ కోసం ఫైల్ సృష్టించాలి మరియు ఆ ఫీచర్‌కు కావలసిన తప్పనిసరి ఫీల్డ్‌లు ఉండాలి. ఈ ఫీల్డ్‌లు టూల్స్, రిసోర్సెస్ మరియు ప్రాంప్ట్‌ల మధ్య కొంచెం భిన్నంగా ఉంటాయి.

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
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను ధృవీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticని జోడించండి, తద్వారా మనం AddInputModel తయారు చేసి ఆర్గ్యూమెంట్లను ధృవీకరించవచ్చు

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ఇక్కడ మీరు ఎలా చేస్తున్నారో చూడండి:

- Pydantic `AddInputModel` ఉపయోగించి schema.py లో `a` మరియు `b` ఫీల్డ్‌లతో స్కీమా సృష్టించడం.
- ఉపయోగించిన రిక్వెస్ట్‌ని `AddInputModel` టైప్‌గా పార్స్ చేయడానికి ప్రయత్నించడం, తప్పు అయితే క్రాష్ అవుతుంది:

   ```python
   # add.py
    try:
        # Pydantic మోడల్ ఉపయోగించి ఇన్పుట్‌ను ధృవీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ఈ పార్సింగ్ లాజిక్‌ను టూల్ కాల్‌లో పెట్టవచ్చు గాని హ్యాండ్లర్ ఫంక్షన్‌లో కూడా పెట్టొచ్చు.

**TypeScript**

```typescript
// సర్వర్.ts
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

       // @ts-గమనించవద్దు
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

// స్కీమా.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// జోడించు.ts
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

- అన్ని టూల్ కాల్స్ హ్యాండిల్ చేసే హ్యాండ్లర్‌లో, రిక్వెస్ట్‌ను టూల్ నిర్వచించిన స్కీమాలో పార్స్ చేయడానికి ప్రయత్నిస్తారు:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ఇది పనిచేస్తే మనం టూల్ను వాస్తవంగా కాల్ చేస్తాము:

    ```typescript
    const result = await tool.callback(input);
    ```

ఈ విధానం చక్కని ఆర్కిటెక్చర్‌ను సృష్టిస్తుంది ఎందుకంటే *server.ts* అనేది చాలా చిన్న ఫైల్, ఇది రిక్వెస్ట్ హ్యాండ్లర్స్ మాత్రమే కలిపి ఉంచుతుంది, మరియు ప్రతి ఫీచర్ సంబంధిత ఫోల్డర్‌లో ఉంటుంది, ఉదా: tools/, resources/, లేదా prompts/.

అద్భుతం, దీన్ని తదుపరి నిర్మించడానికి ప్రయత్నిద్దాం.

## వ్యాయామం: లో-లెవల్ సర్వర్ సృష్టించడం

ఈ వ్యాయామంలో, మనం:

1. టూల్స్ జాబితా చేయడం మరియు కాల్ చేయడం హ్యాండిల్ చేసే లో-లెవల్ సర్వర్ సృష్టించాలి.
2. మీరు పునఃనిర్మించదగిన ఆర్కిటెక్చర్ ను అమలు చేయాలి.
3. టూల్ కాల్స్ సరైనంగా వెరిఫై చేయబడటానికి వెరిఫికేషన్ జోడించాలి.

### -1- ఆర్కిటెక్చర్ సృష్టించండి

మొదటి చర్య మా అంశాల్లో దీని వెడల్పును పెంచే ఆర్కిటెక్చర్ సృష్టించడం, ఇది ఇలా ఉంటుంది:

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

ఇప్పుడికి, టూల్స్ ఫోల్డర్‌లో కొత్త టూల్స్ సులభంగా జోడించేందుకు ఆర్కిటెక్చర్ సెట్ చేయబడింది. రిసోర్సెస్ మరియు ప్రాంప్ట్‌లకు సబ్‌డైరెక్టరీలు జోడించడంలో ఈ విధానాన్ని అనుసరించండి.

### -2- టూల్ సృష్టించండి

తర్వాత, టూల్ సృష్టించడం ఎలా ఉంటుందో చూద్దాం. ముందుగా, ఇది టూల్ సబ్‌డైరెక్టరీలో క్రింద విధంగా ఉండాలి:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ని ధృవీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ని జోడించాలి, తద్వారా మేము AddInputModel సృష్టించి args ని ధృవీకరించగలుగుతాము

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ఇక్కడ మీరు చూస్తున్నది పేరును, వివరణను, Pydantic ఉపయోగించి ఇన్‌పుట్ స్కీమాను నిర్వచించడం మరియు టూల్ కాల్ అయినప్పుడు పిలవబడే హ్యాండ్లర్. చివరగా, `tool_add` అనే డిక్షనరీ ద్వారా ఈ లక్షణాలు బహిర్భావం అవుతున్నాయి.

ఇంకా *schema.py* ఉంది, ఇది మన టూల్‌లో ఉపయోగించే ఇన్‌పుట్ స్కీమాను నిర్వచిస్తుంది:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

మరియు *__init__.py* ఫైల్‌ని నింపాలి, తద్వారా tools డైరెక్టరీ మాడ్యూల్‌గా భావించబడుతుంది. అదనంగా, అందులోని మాడ్యూల్స్‌ను ఇలా ఎక్స్‌పోజ్ చేయాలి:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

మనం ఈ ఫైల్‌కు కొత్త టూల్స్ జతచేస్తున్నప్పుడు ఈ క్ర‌మాన్ని కొనసాగించవచ్చు.

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

ఇక్కడ ప్రాపర్టీస్ కలిగిన డిక్షనరీ సృష్టിക്കുന്നു:

- name: టూల్ పేరు.
- rawSchema: ఇది Zod స్కీమా, ఈ టూల్‌ను కాల్ చేసే రిక్వెస్ట్‌లను వెరిఫై చేయడానికి ఉపయోగిస్తారు.
- inputSchema: హ్యాండ్లర్ కోసం ఉపయోగించే స్కీమా.
- callback: ఈ టూల్‌ను పిలవడానికి ఉపయోగించే ఫంక్షన్.

`Tool` ఉంది, ఇది ఈ డిక్షనరీని mcp సర్వర్ హ్యాండ్లర్ అంగీకరిస్తున్న టైప్‌గా మార్చుతుంది, ఇది ఇలా ఉంటుంది:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

మరియు *schema.ts* ఉంది, అందులో ప్రస్తుతం ఒక్క స్కీమా ఉన్నా, మనం టూల్స్ పెంచేము కాబట్టి ఇంకొన్ని ఎంట్రీలు జోడించవచ్చు:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

గుడ్, ఇప్పుడు మన టూల్స్ జాబితా నిర్వహణను చేద్దాం.

### -3- టూల్స్ జాబితా నిర్వహణ

ఇప్పుడు టూల్స్ జాబితాను నిర్వహించడానికి రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయాలి. మన సర్వర్ ఫైల్లో క్రింద యాడ్ చేయాలి:

**Python**

```python
# సంక్షిప్తత కోసం కోడ్ వదిలివేయబడింది
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

ఇక్కడ, మేము `@server.list_tools` డెకరేటర్ మరియు `handle_list_tools` అనే అమలు ఫంక్షన్ జోడించాము. ఇందులో టూల్స్ జాబితాను తయారు చేయాలి. ప్రతి టూల్‌కు పేరూ, వివరణతో పాటు ఇన్‌పుట్ స్కీమా ఉండాలని గమనించండి.  

**TypeScript**

tools జాబితా కోసం రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయడానికి, సర్వర్‌పై `setRequestHandler`ని కాల్ చేసి, మనం చేస్తున్న పనికి సరిపోయే స్కీమా ఇస్తాం, అంటే `ListToolsRequestSchema`.

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
// సంక్షిప్తత కోసం కోడ్ మినహాయించబడింది
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // నమోదు చేయబడిన సాధనాల జాబితాను తిరిగి ఇవ్వండి
  return {
    tools: tools
  };
});
```

బాగుంది, ఇప్పుడు టూల్స్ జాబితా సమస్య పరిష్కరించుకున్నాం, ఇప్పుడు టూల్స్ కాల్ ఎలా జరుగుతుందో చూద్దాం.

### -4- టూల్ కాల్ నిర్వహణ

టూల్‌ను కాల్ చేయడానికి మరో రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయాలి, ఇది పిలవవలసిన ఫీచర్ ఏదో మరియు ఆర్గ్యుమెంట్లు ఏమిటో స్పష్టం చేసే రిక్వెస్ట్‌ను హ్యాండిల్ చేస్తుంది.

**Python**

`@server.call_tool` డెకరేటర్ ఉపయోగించి `handle_call_tool` అనే ఫంక్షన్ అమలు చేద్దాం. ఆ ఫంక్షన్‌లో, టూల్ పేరు, ఆర్గ్యుమెంట్లు పార్స్ చేసి, ఆ ఆర్గ్యుమెంట్లు సరైనదిగా ఉన్నాయని నిర్ధారించాలి. మీరు దీన్ని ఈ ఫంక్షన్‌లో లేదా తర్వాత టూల్‌లో వెరిఫై చేయవచ్చు.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools అనేది టూల్ పేర్లను కీలు గా కలిగి ఉన్న డిక్షనరీ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # టూల్‌ను పిలవండి
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

నివేదిక ఉంది:

- మన టూల్ పేరు ఇన్‌పుట్ పారామిటర్ `name`గా అందుబాటులో ఉంది, ఆర్గ్యుమెంట్లు `arguments` డిక్షనరీగా ఉన్నాయి.

- టూల్ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` తో కాల్ అవుతుంది. ఆర్గ్యుమెంట్ల వెరిఫికేషన్ `handler` ఫంక్షన్ లో జరుగుతుంది, అది ఫెయిలైతే ఎక్స్‌సెప్షన్ రైజ్ అవుతుంది.

ఇలా, మనకు లో-లెవల్ సర్వర్ ఉపయోగించి టూల్స్ జాబితా చేయడం మరియు కాల్ చేయడంపై పూవులైన అవగాహన వచ్చింది.

పూర్తి ఉదాహరణ కోసం చూడండి [full example](./code/README.md)

## అసైన్‌మెంట్

మీకు ఇచ్చిన కోడ్‌ను విస్తరించి టూల్స్, రిసోర్సెస్ మరియు ప్రాంప్ట్‌లను జోడించండి మరియు మీరు గమనించే విషయం ఏమిటంటే టూల్స్ డైరెక్టరీలో ఫైల్‌లు మాత్రమే జోడించాల్సి ఉంటుందని గుర్తించండి.

*ఏ వేళా పరిష్కారం లేదు*

## సారాంశం

ఈ అధ్యాయంలో, లో-లెవల్ సర్వర్ పద్ధతి ఎలా పనిచేస్తుందో చూశాం మరియు మనం నిర్మించుకునే చక్కని ఆర్కిటెక్చర్ సృష్టించవచ్చని తెలుసుకున్నాం. వెరిఫికేషన్ గురించి చర్చించాం మరియు ఇన్‌పుట్ వెరిఫికేషన్ కోసం స్కీమాలు క్రియేట్ చేయడంలో వెరిఫికేషన్ లైబ్రరీలతో ఎలా పని చేయాలో చూపించారు.

## ముందస్తు

- తరువాతి: [సులభమైన ఆథెంటికేషన్](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**స్పష్టీకరణ**:  
ఈ పత్రాన్ని AI అనువాద సేవ అయిన [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువాదం చేయబడింది. మేము సవ్యమైన అనువాదానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమెటిక్ అనువాదాలలో లోపాలు లేదా తప్పులున్నుండే అవకాశం ఉంది. మూల పత్రం స్థానిక భాషలోనే అధికారిక సూత్రంగా పరిగణించాలి. ముఖ్య సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫార్సు చేసుకుంటాము. ఈ అనువాదం వలన కలిగిన ఏవైనా అపార్థాలు లేదా తప్పు అర్థం చేసుకోవడాలకు మేము బాధ్యులం కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->