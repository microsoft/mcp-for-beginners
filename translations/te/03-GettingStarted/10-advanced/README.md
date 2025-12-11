<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1de8367745088b9fcd4746ea4cc5a161",
  "translation_date": "2025-12-11T12:42:53+00:00",
  "source_file": "03-GettingStarted/10-advanced/README.md",
  "language_code": "te"
}
-->
# అధునాతన సర్వర్ వినియోగం

MCP SDKలో రెండు రకాల సర్వర్లు అందుబాటులో ఉన్నాయి, మీ సాధారణ సర్వర్ మరియు లో-లెవల్ సర్వర్. సాధారణంగా, మీరు సాధారణ సర్వర్‌ను ఉపయోగించి దానికి ఫీచర్లను జోడిస్తారు. కొన్ని సందర్భాల్లో, మీరు లో-లెవల్ సర్వర్‌పై ఆధారపడాలనుకుంటారు, ఉదాహరణకు:

- మెరుగైన ఆర్కిటెక్చర్. సాధారణ సర్వర్ మరియు లో-లెవల్ సర్వర్ రెండింటితో కూడిన శుభ్రమైన ఆర్కిటెక్చర్ సృష్టించడం సాధ్యమే కానీ లో-లెవల్ సర్వర్‌తో ఇది కొంచెం సులభమని వాదించవచ్చు.
- ఫీచర్ అందుబాటు. కొన్ని అధునాతన ఫీచర్లు కేవలం లో-లెవల్ సర్వర్‌తో మాత్రమే ఉపయోగించవచ్చు. మీరు తర్వాతి అధ్యాయాల్లో సాంప్లింగ్ మరియు ఎలిసిటేషన్ జోడించినప్పుడు దీన్ని చూడగలరు.

## సాధారణ సర్వర్ vs లో-లెవల్ సర్వర్

ఇది సాధారణ సర్వర్‌తో MCP సర్వర్ సృష్టించడం ఎలా ఉంటుందో చూపిస్తుంది

**Python**

```python
mcp = FastMCP("Demo")

# ఒక జోడింపు సాధనాన్ని జోడించండి
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

// ఒక జోడింపు సాధనాన్ని జోడించండి
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

ముఖ్య విషయం ఏమిటంటే మీరు సర్వర్‌కు కావలసిన ప్రతి టూల్, వనరు లేదా ప్రాంప్ట్‌ను స్పష్టంగా జోడిస్తారు. ఇందులో ఏ తప్పు లేదు.

### లో-లెవల్ సర్వర్ విధానం

కానీ, మీరు లో-లెవల్ సర్వర్ విధానాన్ని ఉపయోగించినప్పుడు మీరు వేరుగా ఆలోచించాలి, అంటే ప్రతి ఫీచర్ రకం (టూల్స్, వనరులు లేదా ప్రాంప్ట్స్) కోసం రెండు హ్యాండ్లర్లను సృష్టించాలి. ఉదాహరణకు టూల్స్‌కు కేవలం రెండు ఫంక్షన్లు ఉంటాయి:

- అన్ని టూల్స్‌ను జాబితా చేయడం. ఒక ఫంక్షన్ అన్ని టూల్స్ జాబితా చేయడానికి బాధ్యత వహిస్తుంది.
- అన్ని టూల్స్‌ను పిలవడం. ఇక్కడ కూడా, ఒకే ఒక ఫంక్షన్ టూల్‌కు కాల్‌లను నిర్వహిస్తుంది.

ఇది తక్కువ పని అనిపిస్తుందా? కాబట్టి టూల్‌ను రిజిస్టర్ చేయడం కాకుండా, నేను టూల్స్ జాబితా చేసినప్పుడు టూల్ జాబితాలో ఉండాలని మరియు టూల్ పిలవడానికి రిక్వెస్ట్ వచ్చినప్పుడు అది పిలవబడాలని చూసుకోవాలి.

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
  // నమోదు చేసిన సాధనాల జాబితాను తిరిగి ఇవ్వండి
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

ఇక్కడ ఇప్పుడు ఫీచర్ల జాబితాను తిరిగి ఇచ్చే ఒక ఫంక్షన్ ఉంది. టూల్స్ జాబితాలో ప్రతి ఎంట్రీకి `name`, `description` మరియు `inputSchema` వంటి ఫీల్డ్స్ ఉన్నాయి, ఇవి రిటర్న్ టైప్‌కు అనుగుణంగా ఉంటాయి. ఇది మన టూల్స్ మరియు ఫీచర్ నిర్వచనాన్ని వేరే చోట ఉంచడానికి వీలు కల్పిస్తుంది. ఇప్పుడు మనం tools ఫోల్డర్‌లో అన్ని టూల్స్‌ను సృష్టించవచ్చు మరియు అదే విధంగా మీ ప్రాజెక్ట్ ఇలా సక్రమంగా ఏర్పడుతుంది:

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

అది గొప్పది, మన ఆర్కిటెక్చర్ చాలా శుభ్రమైనదిగా కనిపించవచ్చు.

టూల్స్ పిలవడం ఎలా ఉంటుంది, అదే ఆలోచన కదా, ఒక హ్యాండ్లర్ ఏ టూల్ అయినా పిలవడానికి? అవును, ఖచ్చితంగా, దీని కోడ్ ఇక్కడ ఉంది:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools అనేది టూల్ పేర్లను కీలు గా కలిగిన డిక్షనరీ.
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
    // TODO టూల్‌ను పిలవండి,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

పై కోడ్ నుండి మీరు చూడగలిగినట్లుగా, మనం పిలవాల్సిన టూల్‌ను, దానికి ఏ ఆర్గ్యుమెంట్లు ఉన్నాయో పార్స్ చేయాలి, ఆ తర్వాత టూల్‌ను పిలవాలి.

## ధృవీకరణతో విధానాన్ని మెరుగుపరచడం

ఇప్పటివరకు, మీరు టూల్స్, వనరులు మరియు ప్రాంప్ట్‌లను జోడించడానికి చేసిన అన్ని రిజిస్ట్రేషన్లు ఈ రెండు హ్యాండ్లర్లతో ఎలా మార్చవచ్చో చూశారు. మరేమి చేయాలి? మనం టూల్ సరైన ఆర్గ్యుమెంట్లతో పిలవబడుతున్నదని నిర్ధారించడానికి ధృవీకరణను జోడించాలి. ప్రతి రన్‌టైమ్ దీనికి తమ స్వంత పరిష్కారం కలిగి ఉంటాయి, ఉదాహరణకు Python Pydantic ఉపయోగిస్తుంది, TypeScript Zod ఉపయోగిస్తుంది. ఆలోచన ఏమిటంటే:

- ఫీచర్ (టూల్, వనరు లేదా ప్రాంప్ట్) సృష్టించే లాజిక్‌ను దాని ప్రత్యేక ఫోల్డర్‌కు తరలించడం.
- ఉదాహరణకు టూల్ పిలవమని రిక్వెస్ట్ వచ్చినప్పుడు దాన్ని ధృవీకరించడానికి ఒక విధానం జోడించడం.

### ఫీచర్ సృష్టించడం

ఫీచర్ సృష్టించడానికి, ఆ ఫీచర్ కోసం ఒక ఫైల్ సృష్టించి, ఆ ఫీచర్‌కు అవసరమైన తప్పనిసరి ఫీల్డ్స్ ఉన్నాయో లేదో చూసుకోవాలి. టూల్స్, వనరులు మరియు ప్రాంప్ట్‌ల మధ్య ఫీల్డ్స్ కొంత భిన్నంగా ఉంటాయి.

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

    # TODO: Pydanticని జోడించండి, తద్వారా మేము AddInputModelని సృష్టించి ఆర్గ్స్‌ను ధృవీకరించగలము

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ఇక్కడ మీరు ఇలా చేస్తారు:

- Pydantic `AddInputModel` ఉపయోగించి *schema.py* ఫైల్‌లో `a` మరియు `b` ఫీల్డ్స్‌తో స్కీమాను సృష్టించడం.
- రిక్వెస్ట్‌ను `AddInputModel` టైప్‌గా పార్స్ చేయడానికి ప్రయత్నించడం, పారామీటర్లలో ఏదైనా తేడా ఉంటే ఇది క్రాష్ అవుతుంది:

   ```python
   # add.py
    try:
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను ధృవీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ఈ పార్సింగ్ లాజిక్‌ను మీరు టూల్ కాల్‌లోనే ఉంచవచ్చు లేదా హ్యాండ్లర్ ఫంక్షన్‌లో ఉంచవచ్చు.

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

       // @ts-గమనించకండి
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

- అన్ని టూల్ కాల్స్‌ను నిర్వహించే హ్యాండ్లర్‌లో, రిక్వెస్ట్‌ను టూల్ నిర్వచించిన స్కీమాకు పార్స్ చేయడానికి ప్రయత్నిస్తాము:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ఇది సఫలమైతే, అసలు టూల్‌ను పిలవడానికి ముందుకు వెళ్తాము:

    ```typescript
    const result = await tool.callback(input);
    ```

ఈ విధానం గొప్ప ఆర్కిటెక్చర్‌ను సృష్టిస్తుంది, ఎందుకంటే ప్రతీది తన స్థానంలో ఉంటుంది, *server.ts* చాలా చిన్న ఫైల్, ఇది కేవలం రిక్వెస్ట్ హ్యాండ్లర్లను వైర్ చేస్తుంది మరియు ప్రతి ఫీచర్ తమ సంబంధిత ఫోల్డర్‌లలో ఉంటుంది, అంటే tools/, resources/ లేదా prompts/.

గొప్పది, దీన్ని తర్వాత నిర్మిద్దాం.

## వ్యాయామం: లో-లెవల్ సర్వర్ సృష్టించడం

ఈ వ్యాయామంలో, మనం ఈ క్రింది పనులు చేస్తాము:

1. టూల్స్ జాబితా చేయడం మరియు టూల్స్ పిలవడం నిర్వహించే లో-లెవల్ సర్వర్ సృష్టించడం.
2. మీరు నిర్మించగల ఆర్కిటెక్చర్‌ను అమలు చేయడం.
3. మీ టూల్ కాల్స్ సరైన ధృవీకరణతో ఉన్నాయని నిర్ధారించడానికి ధృవీకరణ జోడించడం.

### -1- ఆర్కిటెక్చర్ సృష్టించడం

మొదట మనం పరిష్కరించాల్సినది ఒక ఆర్కిటెక్చర్, ఇది మనకు ఫీచర్లు పెరిగినప్పుడు స్కేల్ అవ్వడానికి సహాయపడుతుంది, ఇది ఇలా ఉంటుంది:

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

ఇప్పుడు మనం tools ఫోల్డర్‌లో కొత్త టూల్స్ సులభంగా జోడించగలిగే ఆర్కిటెక్చర్ సెట్ చేసుకున్నాము. వనరులు మరియు ప్రాంప్ట్‌ల కోసం సబ్‌డైరెక్టరీలను జోడించడానికి ఈ విధానాన్ని అనుసరించండి.

### -2- టూల్ సృష్టించడం

తర్వాత టూల్ సృష్టించడం ఎలా ఉంటుందో చూద్దాం. మొదట, అది *tool* సబ్‌డైరెక్టరీలో సృష్టించాలి, ఇలా:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను ధృవీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic జోడించండి, తద్వారా మేము AddInputModel సృష్టించి ఆర్గ్స్‌ను ధృవీకరించవచ్చు

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ఇక్కడ మనం పేరు, వివరణ, Pydantic ఉపయోగించి ఇన్‌పుట్ స్కీమా మరియు ఈ టూల్ పిలవబడినప్పుడు అమలు అయ్యే హ్యాండ్లర్‌ను నిర్వచిస్తాము. చివరగా, `tool_add` అనే డిక్షనరీని ఎక్స్‌పోజ్ చేస్తాము, ఇది ఈ అన్ని ప్రాపర్టీలను కలిగి ఉంటుంది.

ఇంకా *schema.py* ఉంది, ఇది మన టూల్ ఉపయోగించే ఇన్‌పుట్ స్కీమాను నిర్వచించడానికి ఉపయోగిస్తారు:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

మనం *__init__.py* ను కూడా పూరించాలి, తద్వారా tools డైరెక్టరీ మాడ్యూల్‌గా పరిగణించబడుతుంది. అదనంగా, అందులోని మాడ్యూల్స్‌ను ఇలా ఎక్స్‌పోజ్ చేయాలి:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

మనం కొత్త టూల్స్ జోడించినప్పుడు ఈ ఫైల్‌ను కొనసాగించవచ్చు.

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

ఇక్కడ మనం ప్రాపర్టీలతో కూడిన డిక్షనరీని సృష్టిస్తాము:

- name, ఇది టూల్ పేరు.
- rawSchema, ఇది Zod స్కీమా, ఇది టూల్ పిలవడానికి రిక్వెస్ట్‌లను ధృవీకరించడానికి ఉపయోగిస్తారు.
- inputSchema, ఈ స్కీమాను హ్యాండ్లర్ ఉపయోగిస్తుంది.
- callback, ఇది టూల్‌ను పిలవడానికి ఉపయోగిస్తారు.

`Tool` కూడా ఉంది, ఇది ఈ డిక్షనరీని mcp సర్వర్ హ్యాండ్లర్ అంగీకరించే టైప్‌గా మార్చడానికి ఉపయోగిస్తారు, ఇది ఇలా ఉంటుంది:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

మరియు *schema.ts* ఉంది, ఇందులో ప్రతి టూల్ కోసం ఇన్‌పుట్ స్కీమాలు నిల్వ ఉంటాయి, ప్రస్తుతం ఒక్క స్కీమా మాత్రమే ఉంది కానీ టూల్స్ పెరిగినప్పుడు మరిన్ని ఎంట్రీలు జోడించవచ్చు:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

గొప్పది, ఇప్పుడు మనం టూల్స్ జాబితా నిర్వహణకు ముందుకు పోదాం.

### -3- టూల్స్ జాబితా నిర్వహణ

తర్వాత, మనం టూల్స్ జాబితా నిర్వహించడానికి రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయాలి. మన సర్వర్ ఫైల్‌లో ఈ క్రింది కోడ్ జోడించాలి:

**Python**

```python
# సంక్షిప్తత కోసం కోడ్ తొలగించబడింది
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

ఇక్కడ `@server.list_tools` డెకరేటర్ మరియు `handle_list_tools` ఫంక్షన్‌ను జోడిస్తాము. ఈ ఫంక్షన్‌లో మనం టూల్స్ జాబితాను ఉత్పత్తి చేయాలి. ప్రతి టూల్‌కు పేరు, వివరణ మరియు inputSchema ఉండాలి.

**TypeScript**

టూల్స్ జాబితా కోసం రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయడానికి, మనం సర్వర్‌పై `setRequestHandler` పిలవాలి, ఇది మనం చేయదలచిన పనికి సరిపోయే స్కీమాతో, ఈ సందర్భంలో `ListToolsRequestSchema` తో.

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
// సంక్షిప్తత కోసం కోడ్ తొలగించబడింది
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // నమోదు చేసిన పరికరాల జాబితాను తిరిగి ఇవ్వండి
  return {
    tools: tools
  };
});
```

గొప్పది, ఇప్పుడు మనం టూల్స్ జాబితా చేయడం పరిష్కరించాము, ఇప్పుడు టూల్స్ పిలవడం ఎలా ఉంటుందో చూద్దాం.

### -4- టూల్ పిలవడం నిర్వహణ

టూల్ పిలవడానికి, మరో రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయాలి, ఇది ఏ ఫీచర్ పిలవాలో మరియు ఏ ఆర్గ్యుమెంట్లతో పిలవాలో స్పష్టంగా చెప్పే రిక్వెస్ట్‌ను నిర్వహిస్తుంది.

**Python**

`@server.call_tool` డెకరేటర్ ఉపయోగించి `handle_call_tool` అనే ఫంక్షన్‌ను అమలు చేద్దాం. ఆ ఫంక్షన్‌లో టూల్ పేరు, దాని ఆర్గ్యుమెంట్లు పార్స్ చేసి, ఆ ఆర్గ్యుమెంట్లు టూల్‌కు సరైనవో లేదో ధృవీకరించాలి. ఆర్గ్యుమెంట్ల ధృవీకరణను ఈ ఫంక్షన్‌లో లేదా అసలు టూల్‌లో చేయవచ్చు.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools అనేది టూల్ పేర్లను కీలు గా కలిగిన డిక్షనరీ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # టూల్ ను పిలవండి
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

ఇది ఏమి జరుగుతుందంటే:

- మన టూల్ పేరు ఇప్పటికే ఇన్‌పుట్ పారామీటర్ `name`గా ఉంది, అలాగే `arguments` డిక్షనరీలో మన ఆర్గ్యుమెంట్లు ఉన్నాయి.

- టూల్ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ద్వారా పిలవబడుతుంది. ఆర్గ్యుమెంట్ల ధృవీకరణ `handler` ప్రాపర్టీలో జరుగుతుంది, ఇది ఒక ఫంక్షన్‌ను సూచిస్తుంది, అది విఫలమైతే ఎక్సెప్షన్ వస్తుంది.

ఇలా, మనకు లో-లెవల్ సర్వర్ ఉపయోగించి టూల్స్ జాబితా చేయడం మరియు పిలవడం పూర్తిగా అర్థమైంది.

[పూర్తి ఉదాహరణ](./code/README.md) ఇక్కడ చూడండి

## అసైన్‌మెంట్

మీకు ఇచ్చిన కోడ్‌ను అనేక టూల్స్, వనరులు మరియు ప్రాంప్ట్‌లతో విస్తరించండి మరియు మీరు గమనించే విధంగా మీరు కేవలం tools డైరెక్టరీలో ఫైళ్లను మాత్రమే జోడించాల్సి ఉంటుంది, మరెక్కడా కాదు.

*ఏ పరిష్కారం ఇవ్వబడలేదు*

## సారాంశం

ఈ అధ్యాయంలో, లో-లెవల్ సర్వర్ విధానం ఎలా పనిచేస్తుందో మరియు అది మనకు ఎలా మంచి ఆర్కిటెక్చర్ సృష్టించడంలో సహాయపడుతుందో చూశాం. ధృవీకరణ గురించి కూడా చర్చించాము మరియు ఇన్‌పుట్ ధృవీకరణ కోసం స్కీమాలు సృష్టించడానికి ధృవీకరణ లైబ్రరీలతో ఎలా పని చేయాలో చూపించాము.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->