# అధునాతన సర్వర్ వాడకం

MCP SDKలో రెండు రకాల సర్వర్లు ఉన్నాయి, మీ సాధారణ సర్వర్ మరియు తక్కువ స్థాయి సర్వర్. సాధారణంగా, మీరు సాధారణ సర్వర్‌ను ఉపయోగించి ఫీచర్లను జోడిస్తారు. కానీ కొన్ని సందర్భాల్లో, తక్కువ స్థాయి సర్వర్‌పై ఆధారపడాలనుకుంటారు:

- మెరుగైన సాంకేతిక నిర్మాణం. సాధారణ సర్వర్ మరియు తక్కువ స్థాయి సర్వర్ రెండింటితో కూడిన స్వచ్ఛమైన నిర్మాణాన్ని సృష్టించడం సాధ్యం కానీ, తక్కువ స్థాయి సర్వర్‌తో కొంచెం సులభంగా ఉండొచ్చు.
- ఫీచర్ అందుబాటు. కొన్ని అధునాతన ఫీచర్లు కేవలం
    తక్కువ స్థాయి సర్వర్‌తో మాత్రమే ఉపయోగించవచ్చు. తర్వాత అధ్యायాలు Elicitation మరియు legacy Sampling ఫీచర్‌ను వివరించాయి,
    ఇది MCP `2026-07-28` లో డిప్రికేటెడ్ అయింది.

## సాధారణ సర్వర్ మరియు తక్కువ స్థాయి సర్వర్ మధ్య తేడా

సాధారణ సర్వర్‌తో MCP సర్వర్ ఎలా సృష్టిస్తారో చూడండి:

**Python**

```python
mcp = FastMCP("Demo")

# ఒక జోడింపు పరికరాన్ని జోడించండి
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

// ఒక అదనపు సాధనాన్ని జోడించండి
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

ముఖ్య విషయం ఏమిటంటే, మీరు సర్వரில் అవసరమైన ప్రతీ టూల్, వనరు లేదా ప్రాంప్ట్‌ను స్పష్టంగా జోడించాలి. దీన్లో తప్పేమీ లేదు.  

### తక్కువ స్థాయి సర్వర్ పద్ధతి

అయితే, తక్కువ స్థాయి సర్వర్ పద్ధతిని ఉపయోగించినప్పుడు మీరు వేరు ఆలోచించాల్సి ఉంటుంది. ప్రతి ఫీచర్ రకానికి (టూల్స్, వనరులు లేదా ప్రాంప్ట్‌లు) రెండు హాండ్లర్లను సృష్టించాలి. ఉదాహరణకి టూల్స్‌కు రెండు ఫంక్షన్లు మాదిరిగా ఉంటాయి:

- అన్ని టూల్స్‌ని జాబితా చేయడం. ఒక ఫంక్షన్ అన్ని టూల్స్ జాబితా చేయడానికి బాధ్యత వహిస్తుంది.
- టూల్ కాల్ నిర్వహణ. ఇక్కడ కూడా, ఒక్క ఫంక్షన్ టూల్ కాల్‌లను నిర్వహిస్తుంది.

ఇది కొంత పని తగ్గిందా అనిపిస్తోందా? కాబట్టి టూల్ രജిస్ట్రేషన్ చేయకుండానే, నా జాబితాలో టూల్ ఉన్నదని నిర్ధారించడం మరియు కాలింగ్ అభ్యర్థన వచ్చినప్పుడు టూల్‌ను పిలవడం సరిపోతుంది.

ఇప్పుడు కింది కోడ్ ఎలా ఉంటుందో చూద్దాం:

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
  // నమోదు చేసిన పరికరాల జాబితాను తిరిగి ఇవ్వండి
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

ఇప్పుడు మాకు ఒక ఫంక్షన్ ఉంది, ఇది ఫీచర్ల జాబితాను ఇస్తుంది. టూల్స్ జాబితాలో ప్రతి ఎంట్రీ కి `name`, `description` మరియు `inputSchema` వంటి ఫీల్డ్స్ ఉన్నాయి, ఇది రిటర్న్ రకం కొరకు అవసరం. ఇది మా టూల్స్ మరియు ఫీచర్ నిర్వచనాన్ని వేరే చోట ఉంచగలిగేలా చేస్తుంది. ఇప్పుడు అన్ని టూల్స్‌ను tools ఫోల్డర్‌లో సృష్టించవచ్చు, అలాగే మీ అన్ని ఫీచర్‌లను కూడా ఇలా పెట్టవచ్చు, అందువల్ల మీ ప్రాజెక్ట్ ఈ విధంగా సులభంగా క్రమబద్ధీకరించబడుతుంది:

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

ఇది గొప్పది, మా సాంకేతిక నిర్మాణం చాలా శుభ్రంగా కనిపించేది.

టూల్స్ కాల్ చేయడం ఎలా ఉంటుంది, అదే ఆలోచన కాకపోతే, ప్రతి టూల్‌ను పిలవడానికి ఒక్క హాండ్లర్ ఉంటాడా? అవును, అర్ధం చేసుకున్నట్లే, ఇక్కడ దానికి సంబంధించిన కోడ్:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools అనేది టూల్ పేర్లను కీలు తో కలిగిన ఒక నిఘంటువు.
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
    
    // ఆర్గ్స్: request.params.arguments
    // TODO టూల్‌ను పిలవండి,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

పై కోడ్ ను చూడండి, మేము పిలిచే టూల్ మరియు దానికి ఇచ్చే ఆర్గ్యుమెంట్లను పార్స్ చేయాలి, ఆపై టూల్‌ను పిలవాలి.

## ధ్రువపరిచే విధానంతో పద్ధతి మెరుగుపరచడం

ఇప్పటివరకు, మీరు టూల్స్, వనరులు మరియు ప్రాంప్ట్‌లను జోడించడానికి అన్ని రిజిస్ట్రేషన్‌లను ప్రతి ఫీచర్ రకానికి రెండు హాండ్లర్లతో భర్తీ చేయగలిగినట్లు చూశారు. మాకు ఇంకేమి చేయాలి? బాగుంది, టూల్ సరైన దారితీస్తున్నో లేదో నిర్ధారించడానికి ధ్రువపరిచే రూపాన్ని జోడించాలి. ప్రతి రన్‌టైమ్ కి సాధనాలు ఉంటాయి, ఉదాహరణకి Python ప్యాడాంటిక్ (Pydantic) ఉపయోగిస్తుంది, TypeScript జాడ్ (Zod) ఉపయోగిస్తుంది. భావన ఏమిటంటే మేము ఇలా చేస్తాము:

- ఫీచర్ సృష్టించే లాజిక్‌ను (టూల్, వనరు లేదా ప్రాంప్ట్) దాని ప్రత్యేక ఫోల్డర్‌కు కదిలించడం.
- ఉదాహరణకు టూల్ పిలవమని వచ్చిన అభ్యర్థనను ధ్రువీకరించే మార్గాన్ని జోడించడం.

### ఫీచర్ సృష్టించండి

ఫీచర్ సృష్టించడానికి, ఆ ఫీచర్ కోసం ఒక ఫైల్ సృష్టించి, ఆ ఫీచర్ కోసం తప్పనిసరి ఫీల్డ్‌లు ఉన్నాయని నిర్ధారించాలి. ఆ ఫీల్డ్‌లు టూల్స్, వనరులు మరియు ప్రాంప్ట్‌లలో కొంత భిన్నంగా ఉంటాయి.

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
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను సరి చూసుకోండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticను జోడించండి, దీని ద్వారా మనం AddInputModel సృష్టించి ఆర్గ్యుమెంట్లను సరి చూసుకోగలము

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ఇక్కడ మేము ఇలా చేస్తాము:

- ప్యాడాంటిక్ `AddInputModel` ఉపయోగించి *schema.py* ఫైల్లో `a` మరియు `b` అనే ఫీల్డ్‌లతో స్కీమాను సృష్టించడం.
- వచ్చే అభ్యర్థనను `AddInputModel` టైప్‌గా పார் చేసి చూడటం, ప్యారామీటర్లు సరిపోలనప్పుడు క్రాష్ అవుతుంది:

   ```python
   # add.py
    try:
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను ధృవీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ఈ పాస్ లాజిక్‌ను మీరు టూల్ కాల్ లో పెట్టవచ్చు లేదా హాండ్లర్ ఫంక్షన్‌లో పెట్టవచ్చు.

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

// స్కీమా.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// జత చేయండి.ts
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

- అన్ని టూల్ కాల్‌లను నిర్వహించే హాండ్లర్‌లో, వచ్చే అభ్యర్థనను టూల్ నిర్వచించిన స్కీమాకు అనుగుణంగా పార్ చేయడానికి ప్రయత్నిస్తాము:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    అది సరి అయితే అసలు టూల్‌ను పిలవడానికి కొనసాగుతాము:

    ```typescript
    const result = await tool.callback(input);
    ```

మీరు చూస్తున్నట్లయితే, ఈ పద్ధతి ఒక అద్భుతమైన నిర్మాణం సృష్టిస్తుంది, ఎందుకంటే *server.ts* అనేది చాలా చిన్న ఫైల్ మాత్రమే, ఇది అభ్యర్థన హాండ్లర్లను కలపటం మాత్రమే చేస్తుంది, మరియు ప్రతి ఫీచర్ తన ప్రత్యేక ఫోల్డర్‌లో ఉంటుంది అంటే tools/, resources/ లేదా prompts/.

బాగుంది, ఇప్పుడు దీన్ని నిర్మించడానికి ప్రయత్నిద్దాం.

## వ్యాయామం: తక్కువ స్థాయి సర్వర్ సృష్టించడం

ఈ వ్యాయామంలో, మేము కింది పనులు చేయబోతున్నాం:

1. టూల్స్ జాబితా చేయడం మరియు టూల్స్ పిలవడం నిర్వహించే ఒక తక్కువ స్థాయి సర్వర్ సృష్టించడం.
1. మీరు నిర్మించగలిగే ఒక నిర్మాణాన్ని అమలు చేయడం.
1. మీ టూల్ పిలింపులు సరిగ్గా ధృవీకరించబడినట్లు నిర్ధారించడానికి ధ్రువీకరణ జోడించడం.

### -1- నిర్మాణం సృష్టించండి

మేము మొదట పరిష్కరించుకునేది, కొత్త ఫీచర్‌లను జోడించినప్పుడు మనకు సహాయపడే ఒక నిర్మాణం. ఇది ఈ విధంగా ఉంటుంది:

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

ఇప్పుడు మేము ఒక నిర్మాణాన్ని సెట్ చేసుకున్నాం, ఇది tools ఫోల్డర్‌లో కొత్త టూల్స్‌ను సులభంగా జోడించేందుకు సహాయపడుతుంది. మీరు ఇచ్ఛించినట్లుగా resources మరియు prompts కోసం సబ్డైరెక్టరీలు కూడా జోడించవచ్చు.

### -2- ఒక టూల్ సృష్టించడం

తర్వాత, టూల్ సృష్టించడం ఎలా ఉంటుందో చూద్దాం. ముందుగా, అది *tool* అనే ఉప డైరెక్టరీలో సృష్టించాలి:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను ధృవీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticని చేర్చండి, కాబట్టి మేము AddInputModelను క్రియేట్ చేసి argsని ధృవీకరించగలము

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ఇక్కడ మనం పేరు, వివరణ మరియు ఇన్‌పుట్ స్కీమాను ప్యాడాంటిక్ ఉపయోగించి నిర్వచిస్తున్నాము మరియు టూల్ పిలవబడినప్పుడు కాల్ అయ్యే హాండ్లర్ ఉంది. చివరకు, `tool_add` అనే డిక్షనరీ ద్వారా ఈ అన్ని లక్షణాలు ఎక్స్‌పోజ్ చేస్తున్నాము.

అలాగే *schema.py* ఉంటుంది, ఇది మా టూల్ ఉపయోగించే ఇన్‌పుట్ స్కీమాను నిర్వచించే ఫైలు:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

మేము *__init__.py* ఫైల్‌ను కూడా పూర్వగతం చేయాలి, tools డైరెక్టరీని మాడ్యూల్‌గా గుర్తించేలా. అదనంగా, అందులోని మాడ్యూల్‌లను ఇలా ఎక్స్‌పోజ్ చేయాలి:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

మరిన్ని టూల్స్ జోడించినప్పుడు ఈ ఫైల్‌కు జోడించడాన్ని కొనసాగించవచ్చు.

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

ఇక్కడ, లక్షణాల డిక్షనరీ సృష్టిస్తున్నారు:

- name: టూల్ పేరు.
- rawSchema: జాడ్ స్కీమా, ఈ స్కీమా టూల్ పిలుపు కోసం వచ్చే అభ్యర్థనలను ధృవీకరిస్తుంది.
- inputSchema: హాండ్లర్ ఉపయోగించే స్కీమా.
- callback: టూల్‌ను పిలవడానికి ఉపయోగించబడుతుంది.

`Tool` ని ఉపయోగించి ఈ డిక్షనరీని mcp సర్వర్ హాండ్లర్ అంగీకరించే టైప్‌గా మార్చటం జరుగుతోంది, ఇది ఇలా ఉంటది:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ఇంకా *schema.ts* ఉంటుంది, ఇందులో ప్రతి టూల్ కొరకు ఇన్‌పుట్ స్కీమాలు నిల్వ చేస్తారు, ప్రస్తుతానికి ఒక్కటే ఇందులో ఉన్నా, కొత్త టూల్స్ జోడించినప్పుడు మరిన్ని ఎంట్రీలు జోడిస్తారు:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

బాగుంది, ఇప్పుడు టూల్స్ జాబితాను నిర్వహించే దిశగా కొనసాగుదాం.

### -3- టూల్స్ జాబితా నిర్వహణ

తరువాత, టూల్స్ జాబితాను నిర్వహించేందుకు అభ్యర్థన హాండ్లర్ సెట్ చేయాలి. సర్వర్ ఫైల్‌లో ఈ కింద ఇచ్చిన విధంగా జోడించండి:

**Python**

```python
# సంక్షిప్తంగా కోడ్ తడవబడింది
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

ఇక్కడ, `@server.list_tools` డెకొరేటర్ జోడించి, `handle_list_tools` అనే అమలు ఫంక్షన్ ఉంది. దీని ద్వారా టూల్స్ జాబితా ఉత్పత్తి చేయాలి. ప్రతి టూల్ కు పేరు, వివరణ మరియు inputSchema ఉండాలని గమనించండి.   

**TypeScript**

టూల్స్ జాబితా కోసం అభ్యర్థన హాండ్లర్‌ని సెట్ చేయడానికి, సర్వర్‌పై `setRequestHandler` పిలువాలి, అందులో స్కీం `ListToolsRequestSchema`కి సరిపోలేలా ఇవ్వాలి.

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
// సంక్షిప్తంగా కోడ్ తొలగించబడింది
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // నమోదు చేసిన పరికరాల జాబితాను తిరిగి ఇవ్వండి
  return {
    tools: tools
  };
});
```

బాగుంది, ఇప్పుడు టూల్స్ జాబితా చేయడం పరిష్కరించాం, ఇప్పుడు టూల్స్ పిలవడం ఎలా ఉంటుందో చూద్దాం.

### -4- టూల్ పిలవడం నిర్వహణ

టూల్ పిలవడానికి, మరో అభ్యర్థన హాండ్లర్ సెట్ చేయాలి, ఇది పిలవవలసిన ఫీచర్ మరియు దానికి ఇచ్చే ఆర్గ్యుమెంట్లను గుర్తిస్తుంది.

**Python**

`@server.call_tool` డెకొరేటర్ ఉపయోగించి `handle_call_tool` వంటి ఫంక్షన్‌ను అమలు చేయండి. ఆ ఫంక్షన్‌లో టూల్ పేరు మరియు దానికి వచ్చే ఆర్గ్యుమెంట్లను పార్ చేసి, అవి టూల్‌కు సరిపెడుతున్నాయా లేదా అని ధ్రువీకరించాలి. ఇది ఆర్గ్యుమెంట్లను ఈ ఫంక్షన్‌లోనో లేదా అసలు టూల్‌లోనో చెయ్యవచ్చు.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools అనేది సాధన పేర్లను కీలు గా ఉన్న ఒక డిక్షనరీ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # సాధనాన్ని ఆహ్వానించండి
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

జరుగుతున్నది ఇది:

- టూల్ పేరు `name` అనే ఇన్‌పుట్ ప్యారామీటర్‌గా ముందే ఉంది, అలాగే `arguments` డిక్షనరీ రూపంలో మా ఆర్గ్యుమెంట్లు కూడా.

- టూల్ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` తో పిలవబడుతుంది. ఆర్గ్యుమెంట్ల ధృవీకరణ `handler` ప్రాపర్టీ కనెక్టైన ఫంక్షన్‌లో జరుగుతుంది, ఇది విఫలం అయితే ఎక్సెప్షన్ ఇస్తుంది.

ఇప్పుడు తక్కువ స్థాయి సర్వర్ ఉపయోగించి టూల్స్ జాబితా చేయడం మరియు పిలవడంపై పూర్తి అవగాహన కలిగి ఉన్నాం.

పూర్తి ఉదాహరణకు [ఇక్కడ](./code/README.md) చూడండి

## అసైన్మెంట్

ఇచ్చిన కోడ్‌ను అనేక టూల్స్, వనరులు మరియు ప్రాంప్ట్‌లతో విస్తరించి, మీరు గమనించే విధంగా tools డైరెక్టరీలోనే ఫైల్‌లు జోడించాల్సి ఉండటం మాత్రమే ఉందని పరిగణించండి.

*ఏదైనా పరిష్కారం ఇవ్వలేదు*

## సారాంశం

ఈ అధ్యాయంలో, తక్కువ స్థాయి సర్వర్ పద్ధతి ఎలా పని చేస్తుందో, దీని ద్వారా అందమైన నిర్మాణం ఎలా ఏర్పడుతుందో చూశాము, దీన్ని ఆధారంగా మరింత అభివృద్ధి చేయవచ్చో కూడా తెలుసుకున్నాము. అలాగే ధృవీకరణ గురించి చర్చించాము మరియు ఇన్‌పుట్ ధృవీకరణ కోసం స్కీమాలు సృష్టించడానికి ధృవీకరణ లైబ్రరీలను ఉపయోగించడం ఎలా అనేది చూశాము.

## తదుపరి

- తదుపరి: [సాధారణ ధృవీకరణ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->