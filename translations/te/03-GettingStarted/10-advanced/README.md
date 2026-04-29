# అధునాతన సర్వర్ వినియోగం

MCP SDKలో రెండు రకాల సర్వర్లు అందుబాటులో ఉంటాయి, మీ సాధారణ సర్వర్ మరియు లో-లెవెల్ సర్వర్. సాధారణంగా, మీరు సర్వర్‌కు ఫీచర్లను జోడించడానికి సాధారణ సర్వర్‌ను ఉపయోగిస్తారు. కానీ కొన్ని సందర్భాల్లో, మీరు కింది వాటి వంటి కారణాల వల్ల లో-లెవెల్ సర్వర్‌పై ఆధారపడి ఉండాలనుకుంటారు:

- మంచి ఆర్కిటెక్చర్. సాధారణ సర్వర్ మరియు లో-లెవెల్ సర్వర్ రెండన్నింటితో కలిసి ఒక శుభ్రమైన ఆర్కిటెక్చర్ సృష్టించడం సాధ్యమైంది కానీ లో-లెవెల్ సర్వర్‌తో కొంచెం సులభంగా అని చెప్పవచ్చు.
- ఫీచర్ అందుబాటులో ఉండడం. కొన్ని అధునాతన ఫీచర్లను కేవలం లో-లెవెల్ సర్వర్‌తోనే ఉపయోగించవచ్చు. సాంప్లింగ్ మరియు ఎలిసిటేషన్‌ను జోడించిన తర్వాత మీరు దీన్ని తరువాత అధ్యాయాలలో చూడవచ్చు.

## సాధారణ సర్వర్ VS లో-లెవెల్ సర్వర్

ఇది సాధారణ సర్వర్‌తో MCP సర్వర్ సృష్టించడం ఎలా ఉంటుందో ఉంది

**Python**

```python
mcp = FastMCP("Demo")

# ఒక జతచేసే సాధనాన్ని జోడించండి
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

మీరు సర్వర్‌కి కావలసిన ప్రతి టూల్, రిసోర్స్ లేదా ప్రాంప్ట్‌ని స్పష్టంగా యాడ్ చేస్తారని ముఖ్యాంశం. ఇది తప్పేమీ కాదు.

### లో-లెవెల్ సర్వర్ విధానం

కానీ, మీరు లో-లెవెల్ సర్వర్ విధానం ఉపయోగిస్తే, మీరు దీన్ని వేరే విధంగా ఆలోచించాలి. ప్రతి ఫీచర్ టైపు (టూల్స్, రిసోర్సెస్ లేదా ప్రాంప్ట్‌ల కోసం)కి రెండు హ్యాండ్లర్లు సృష్టించాలి. ఉదాహరణకు టూల్స్ కోసం రెండు ఫంక్షన్లు ఉంటాయి ఈ విధంగా:

- అన్ని టూల్స్‌ను లిస్ట్ చేయడం. ఒక ఫంక్షన్ అన్ని టూల్స్ లిస్టింగ్ ప్రయత్నాలను నిర్వహిస్తుంది.
- అన్ని టూల్స్ కాల్‌ను హ్యాండిల్ చేయడం. ఇక్కడ కూడా ఒకే ఒక ఫంక్షన్ అన్ని టూల్ కాల్‌లను హ్యాండిల్ చేస్తుంది.

ఇది కొంత పని తక్కువగా ఉంటుంది కదా? కాబట్టి టూల్ నందించడానికి బాధపడవద్దు, నేనెప్పుడూ అన్ని టూల్స్ లిస్ట్ చేసినపుడు టూల్ లిస్ట్‌లో ఉన్నదా మరియు టూల్ కాల్ చేయాల్సిన అభ్యర్థన వస్తే ఈ టూల్ పిలవబడుతుందా అని చూసుకుంటే సరిపోతుంది.

ఇప్పుడు కోడ్ ఎలా కనిపెడుతుందో చూద్దాం:

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
  // నమోదు చేసిన సాధనాల జాబితాను తిరిగి ఇవ్వండి
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

ఇక్కడ ఇప్పుడు ఒక ఫంక్షన్ ఉంది ఇది ఫీచర్ల జాబితా ఇస్తుంది. టూల్స్ జాబితాలో ప్రతి ఎంట్రీకు `name`, `description` మరియు `inputSchema` వంటి ఫీల్డులు ఉంటాయి, అవి రిటర్న్ టైప్కి అనుగుణంగా ఉన్నాయి. ఇది మన టూల్స్ మరియు ఫీచర్ నిర్వచనాన్ని ఎక్కడైనా ఉంచడానికి అనుమతిస్తుంది. ఇప్పుడు మనం టూల్స్ అందించిన `tools` ఫోల్డర్‌లో అన్ని టూల్స్ సృష్టించవచ్చు మరియు అదే విధంగా మీ అన్ని ఫీచర్ల కోసం ఇది వర్తిస్తుంది కాబట్టి మీ ప్రాజెక్ట్ ఇలా ఏర్పాటు అయి ఉంటుంది:

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

దారుణం కాదు, మన ఆర్కిటెక్చర్ చాలా శుభ్రంగా కనిపించేలా చేయవచ్చు.

టూల్స్ కాల్ చేయడమేమిటి, ఇదే ఐడియా కదా, ఒక హ్యాండలర్ ఏ టూల్ అయినా కాల్ చేస్తుందా? అవును, ఇదిగో కోడ్:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools అనేది సాధనాల పేర్లను కీలు గా ఉంచుకునే డిక్షనరీ.
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

పైన ఉన్న కోడ్ నుండి మీరు చూస్తున్నట్లే, మాకు కాల్ చేయవలసిన టూల్ పేరు మరియు దానికి అవసరమైన ఆర్గ్యుమెంట్స్ పార్స్ చేయాలి, అనంతరం ఆ టూల్‌ను కాల్ చేయాలి.

## ధ్రువీకరణతో ఈ విధానాన్ని మెరుగుపరచడం

ఇప్పటివరకు, మీరు సాధారణంగా టూల్స్, రిసోర్సెస్ మరియు ప్రాంప్ట్‌లను జోడించే అన్ని రిజిస్ట్రేషన్లు ఈ రెండు హ్యాండ్లర్లతో పోటీ చేయవచ్చు అని చూశారు. మరేమి చేయాలి? సరైన ఆర్గ్యుమెంట్స్‌తో టూల్ పిలవబడుతున్నదన్న భరోసా కోసం కొంత ధ్రువీకరణ (validation) జోడించాలి. ప్రతి రన్‌టైమ్ దీనికి తగిన పరిష్కారం కలిగి ఉంటుంది, ఉదాహరణకు Pythonలో Pydantic ఉపయోగిస్తారు మరియు TypeScriptలో Zod. లక్ష్యం ఇలా ఉంటుంది:

- ఫీచర్ (టూల్, రిసోర్స్ లేదా ప్రాంప్ట్) సృష్టించే లాజిక్‌ను ప్రత్యేక ఫోల్డర్‌లోకి మార్చటం.
- ఉదాహరణగా టూల్ కాల్ చేయమని వచ్చిన రిక్వెస్ట్‌ను ధృవీకరించడానికి ఒక మార్గాన్ని జోడించడం.

### ఫీచర్ సృష్టించటం

ఒక ఫీచర్ సృష్టించడానికి, ఆ ఫీచర్ కోసం ఒక ఫైల్ సృష్టించి, ఆ ఫీచర్‌కు అవసరమైన తప్పనిసరి ఫీల్డ్స్ ఉన్నాయో లేదో చూసుకోవాలి. అవి టూల్స్, రిసోర్సెస్, మరియు ప్రాంప్ట్‌లలో కొంచెం వేరు ఉంటాయి.

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
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను ధ్రువీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticను జోడించండి, తద్వారా మేము AddInputModelని సృష్టించి ఆర్గ్స్‌ని ధ్రువీకరించవచ్చు

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ఇక్కడ మేము ఈ క్రింద చూపిన విధంగా చేస్తాము:

- *schema.py* ఫైల్‌లో `AddInputModel` అనే Pydantic స్కీమాను `a` మరియు `b` ఫీల్డులతో సృష్టించడం.
- వచ్చిన రిక్వెస్ట్‌ను `AddInputModel` టైపుగా పార్స్ చేయడానికి ప్రయత్నించడం, పారామీటర్ల మధ్య ఏ తారాజు ఉంటే అది క్రాష్ అవుతుంది:

   ```python
   # add.py
    try:
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను ధృవీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

పార్సింగ్ లాజిక్‌ను టూల్ కాల్‌లో పెట్టాలి లేదా హ్యాండ్లర్ ఫంక్షన్‌లో పెట్టాలి అనేది మీరు ఎంచుకోవచ్చు.

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

// సృష్టించు.ts
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

- అన్ని టూల్ కాల్‌లను హ్యాండిల్ చేసే హ్యాండ్లర్లో, మనం ఇప్పుడు వచ్చిన రిక్వెస్ట్‌ను ఆ టూల్ నిర్వచించిన స్కీమాలోకి పార్స్ చేయడానికి ప్రయత్నిస్తాము:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ఇది సక్సెస్ అయితే, నిజమైన టూల్‌ను కాల్ చేయమని ముందుకు పోతాము:

    ```typescript
    const result = await tool.callback(input);
    ```

మీరు చూసిన ప్రకారం, ఈ విధానం గొప్ప ఆర్కిటెక్చర్ సృష్టిస్తుంది ఎందుకంటే ప్రతిదీ తన సొంత ప్రదేశంలో ఉంటుంది, *server.ts* చాలా చిన్న ఫైల్ గా ఉంటుంది, ఇది కేవలం రిక్వెస్ట్ హ్యాండ్లర్లను వైర్ చేస్తుంది మరియు ప్రతి ఫీచర్ తన తగిన ఫోల్డర్‌లో ఉంటుంది అంటే tools/, resources/ లేదా prompts/.

మంచిది, ఇక దీన్ని నిర్మించడానికి ప్రయత్నిద్దాం.

## వ్యాయామం: లో-లెవెల్ సర్వర్ సృష్టించడం

ఈ వ్యాయామంలో, మేము ఈ క్రింది వాటిని చేస్తాము:

1. టూల్స్ లిస్టింగ్ మరియు కాలింగ్‌ను హ్యాండిల్ చేసే లో-లెవెల్ సర్వర్ సృష్టించడం.
1. మీరు అభివృద్ధి చేయగల ఆర్కిటెక్చర్‌ను అమలు చేయడం.
1. మీ టూల్ కాల్స్ సక్రమంగా ధృవీకరించబడతాయని నిర్ధారించేందుకు ధ్రువీకరణ జోడించడం.

### -1- ఆర్కిటెక్చర్ సృష్టించడం

మా ముందుగా పరిష్కరించవలసినది, ఇంకా ఫీచర్లను జోడించడాన్ని సులభతరం చేయగల ఆర్కిటెక్చర్. ఇది ఇలా ఉంటుంది:

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

ఇప్పుడు మన దగ్గర ఆర్కిటెక్చర్ ఏర్పడింది, ఇది మనం tools ఫోల్డర్లో కొత్త టూల్స్ సులభంగా జోడించగలుగుతామని. మీరు resources మరియు prompts కోసం సబ్‌డైరెక్టరీస్ కూడా జోడించవచ్చు.

### -2- టూల్ సృష్టించడం

ఇప్పుడు టూల్ సృష్టించడం ఎలా ఉంటుందో చూద్దాం. మొదట, అది తన *tool* సబ్‌డైరెక్టరీలో సృష్టించాలి:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic మోడల్ ఉపయోగించి ఇన్‌పుట్‌ను ధ్రువీకరించండి
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ను జోడించండి, దాంతో మనం AddInputModel సృష్టించి ఆర్గ్స్ ని ధ్రువీకరించగలము

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ఇక్కడ మనం పేరును, వివరణను మరియు ఇన్‌పుట్ స్కీమాను Pydantic ఉపయోగించి నిర్వచిస్తున్నాం మరియు టూల్ పిలవబడినప్పుడు అమలు అయ్యే హ్యాండ్లర్ కూడా ఉంది. చివరగా, `tool_add` ను ఎగ్జిపోజ్ చేస్తున్నాం, ఇది ఈ అన్ని ప్రాపర్టీలతో కూడిన డిక్షనరీ.

కూడా *schema.py* ఉంది, ఇది మన టూల్ ఇన్‌పుట్ స్కీమాను నిర్వచించడానికి ఉపయోగిస్తారు:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

మనం *__init__.py* ని కూడా నింపాలి, తద్వారా tools డైరెక్టరీ మాడ్యూల్‌గా పరిగణించబడుతుంది. అదనంగా, అందులోని మాడ్యూల్స్‌ను కూడా ఇలా ఎగ్జిపోజ్ చేయాలి:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

మనం ఈ ఫైల్‌ను మరిన్ని టూల్స్ జోడించుకునేప్పుడు కొనసాగించవచ్చు.

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

ఇక్కడ మనం ఒక డిక్షనరీ సృష్టిస్తున్నాం, అందులో ప్రాపర్టీలుగా ఉన్నాయి:

- name, ఇది టూల్ పేరు.
- rawSchema, ఇది Zod స్కీమా, ఇది టూల్ కాల్ కోసం వచ్చిన రిక్వెస్టును ధృవీకరించడానికి ఉపయోగపడుతుంది.
- inputSchema, ఈ స్కీమా హ్యాండ్లర్ ద్వారా ఉపయోగించబడుతుంది.
- callback, దీని ద్వారా టూల్‌ను పిలుస్తారు.

మరియు `Tool` ఉంది, ఇది ఈ డిక్షనరీని mcp సర్వర్ హ్యాండ్లర్ అంగీకరించే టైప్‌గా మార్చుతుంది:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

మరియు *schema.ts* ఉంది, ఇందులో ప్రస్తుతం ఒక్క స్కీమా ఉన్నా అడిగినంతగా కొత్త టూల్స్ జోడిస్తాం:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

మంచిది, ఇక మన టూల్స్ లిస్టింగ్ హ్యాండిల్ చేయడానికి ప్రయత్నిద్దాం.

### -3- టూల్స్ లిస్టింగ్ హ్యాండిల్ చేయటం

ఇప్పుడు మనం టూల్స్ ని లిస్ట్ చేయడానికి ఒక రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయాలి. ఇది మన సర్వర్ ఫైల్‌కు ఇలా జోడించాలి:

**Python**

```python
# సారాంశం కోసం కోడ్ తీసివేయబడింది
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

ఇక్కడ, మేము `@server.list_tools` డెకరేటర్‌ను జోడించి, `handle_list_tools` అనే ఫంక్షన్‌ను అమలు చేస్తున్నాం. ఇందులో, మనం టూల్స్ జాబితాను ఉత్పత్తి చేయాలి. ప్రతి టూల్‌కు పేరు, వివరణ మరియు inputSchema ఉండాలి.

**TypeScript**

టూల్స్ లిస్ట్ చేయటానికి రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయడానికి, సర్వర్‌పై `setRequestHandler` కలెక్టర్‌ను పిలువాలి, ఇక్కడ మనం చేయదలచిన పని ప్రకారంగా స్కీమా ఇవ్వాలి, ఈ సందర్భంలో `ListToolsRequestSchema`.

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
// సారాంశానికి కోడ్ తొలగించబడింది
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // నమోదు చేయబడిన సాధనాల జాబితాను తిరిగి ఇవ్వండి
  return {
    tools: tools
  };
});
```

మంచిది, ఇప్పుడు టూల్స్ లిస్ట్ చేసే పని పరిష్కరించగా, తదుపరి టూల్స్ ని ఎలా కాల్ చేయాలో చూద్దాం.

### -4- టూల్ కాల్ హ్యాండిల్ చేయటం

టూల్‌ను కాల్ చేయడానికి, మరో రిక్వెస్ట్ హ్యాండ్లర్ సెట్ చేయాలి, ఇది ఏ ఫీచర్ పిలవాలనుకుంటున్నాం మరియు దానికి ఏ ఆర్గ్యుమెంట్స్ ఇవ్వాలనో అన్నదానిపై కేంద్రీకృతమవుతుంది.

**Python**

`@server.call_tool` డెకరేటర్‌ను ఉపయోగించి, `handle_call_tool` అనే ఫంక్షన్‌ను అమలు చేద్దాం. ఆ ఫంక్షన్‌లో టూల్ పేరు, దాని ఆర్గ్యుమెంట్స్‌ను పార్స్ చేసి, ఆ ఆర్గ్యుమెంట్స్ సరైనవా కాదా చెక్ చేయాలి. ఇది మీరు ఈ ఫంక్షన్‌లో ధృవీకరించవచ్చు లేదా అసలు టూల్‌లోనే చెక్ చేయవచ్చు.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools అనేది టూల్ పేర్లను కీలు గా గల డిక్షనరీ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # టూల్ ను ఆహ్వానించండి
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

ఇక్కడ ఏమి జరుగుతుంది:

- మన టూల్ పేరు ఇన్‌పుట్ పరామీటర్ `name` రూపంలో ఇప్పటికే ఉంది, మరియు ఆర్గ్యుమెంట్స్ `arguments` డిక్షనరీ ఆకారంలో ఉన్నాయి.

- టూల్ పిలవబడుతుంది `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ద్వారా. ఆర్గ్యుమెంట్స్ ధృవీకరణ హ్యాండ్లర్ ప్రాపర్టీ ద్వారా జరుగుతుంది, అది ఫంక్షన్‌కు సూచిస్తుంది, అది విఫలమైతే ఒక ఎక్సెప్షన్ తొలగుతుంది.

ఇలా మనకు లో-లెవెల్ సర్వర్ ఉపయోగించి టూల్స్ లిస్ట్ మరియు కాల్ గురించి పూర్తి అవగాహన వచ్చింది.

పూర్తి ఉదాహరణ ఇది చూడండి: [full example](./code/README.md)

## అసైన్మెంట్

మీకు ఇచ్చిన కోడ్‌ని కొంతమంది టూల్స్, రిసోర్సెస్ మరియు ప్రాంప్ట్‌లతో విస్తరించండి మరియు టూల్స్ డైరెక్టరీలో మాత్రమే ఫైళ్లను జోడించాల్సి వస్తుందన్న విషయం ఎలా గమనించారో ఆలోచించండి.

*పరిష్కారం ఇవ్వలేదు*

## సారాంశం

ఈ అధ్యాయంలో, లో-లెవెల్ సర్వర్ విధానం ఎలా పనిచేస్తుందో మరియు అది మనకు ఎలా ఒక మంచి ఆర్కిటెక్చర్ సృష్టించడంలో సహాయపడుతుందో చూశాం. అలాగే ధృవీకరణ గురించి చర్చించాము మరియు ఇన్‌పుట్ ధృవీకరణకు స్కీమాలు సృష్టించడానికి ధృవీకరణ లైబ్రరీలతో ఎలా పని చేయాలో మీకు చూపించబడింది.

## తరువాత ఏం చేయాలి

- తర్వాతి: [సాధారణ గుర్తింపు](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్‌ను AI భాషా అనువాద సేవ అయిన [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము సరిగ్గా ఉండేందుకు ప్రయత్నించినప్పటికీ, స్వయంచాలక అనువాదాలలో తప్పులు లేదా అసున్నతులు ఉండవచ్చు అని గమనించాలి. అసలు డాక్యుమెంట్ తన స్వదేశ భాషలో ప్రామాణిక మూలంగా పరిగణించబడాలి. కీలక సమాచారం కోసం, వృత్తిపరమైన మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడుకతో సంభవించే ఏవైనా అవగాహనలో పొరపాట్లు లేదా తప్పుబాట్లకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->