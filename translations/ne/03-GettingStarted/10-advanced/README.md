# उन्नत सर्भर प्रयोग

MCP SDK मा दुई विभिन्न प्रकारका सर्भरहरू प्रकट छन्, तपाईंको सामान्य सर्भर र लो-लेवल सर्भर। सामान्यतया, तपाईं यसको लागि नियमित सर्भर प्रयोग गर्नुहुन्छ। तर केही केसहरूमा, तपाईं लो-लेवल सर्भरमा निर्भर रहन चाहनुहुन्छ, जस्तै:

- राम्रो वास्तुकला। दुवै नियमित र लो-लेवल सर्भरका साथ एक सफा वास्तुकला बनाउन सकिन्छ तर भनिन्छ कि यो अलि सजिलो हुन्छ लो-लेवल सर्भरसँग।
- फिचर उपलब्धता। केही उन्नत सुविधाहरू केवल
    लो-लेवल सर्भरमा मात्र प्रयोग गर्न सकिन्छ। पछि अध्यायहरूले Elicitation र legacy Sampling फ्रिचर समेट्छन्,
    जुन MCP `2026-07-28` मा अप्रचलित छ।

## नियमित सर्भर बनाम लो-लेवल सर्भर

यहाँ नियमित सर्भरसँग MCP सर्भर सिर्जना गर्दा कस्तो देखिन्छ:

**Python**

```python
mcp = FastMCP("Demo")

# थप्ने उपकरण थप्नुहोस्
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

// एक थप उपकरण थप्नुहोस्
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

मुख्य कुरा यो हो कि तपाईं स्पष्ट रूपमा प्रत्येक उपकरण, स्रोत वा प्रम्प्ट थप्नुहुन्छ जुन तपाईंको सर्भरमा चाहिन्छ। यसमा केही समस्या छैन।  

### लो-लेवल सर्भर तरिका

तथापि, जब तपाईं लो-लेवल सर्भर विधि प्रयोग गर्नुहुन्छ, तपाईंले यसलाई फरक तरिकाले सोच्न आवश्यक हुन्छ। प्रत्येक उपकरण दर्ता गर्ने सट्टा, तपाईंले प्रत्येक फिचर प्रकार (उपकरण, स्रोत वा प्रम्प्ट) का लागि दुई ह्यान्डलरहरू सिर्जना गर्नुहुन्छ। उदाहरणका लागि उपकरणहरूका लागि यसरी केवल दुई फंक्शन हुन्छन्:

- सबै उपकरणहरूको सूची बनाउने। एउटा फंक्शन सबै सूची बनाउनका लागि जिम्मेवार हुन्छ।
- सबै उपकरण कॉलहरू सामाँने गर्ने। यहाँ पनि, एउटा मात्र फंक्शन उपकरणलाई कल गर्न ह्यान्डल गर्छ।

यसले सम्भावित रूपमा कम काम जस्तो लाग्छ, हो? त्यसैले उपकरण दर्ता गर्ने सट्टा, मैले केवल पक्का गर्नुपर्छ कि उपकरण सूचीमा छ भने सबै उपकरणहरूको जब म सूची बनाउँछु र जब उपकरणलाई कल गर्ने अनुरोध आउँछ त्यस बेला यसलाई कल गरिन्छ।

अब हामी हेरौं कि कोड अब कस्तो देखिन्छ:

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
  // दर्ता गरिएका उपकरणहरूको सूची फर्काउनुहोस्
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

यहाँ हामीसँग फिचरहरूको सूची फर्काउने एउटा फंक्शन छ। उपकरणहरूको सूचीमा हरेक प्रविष्टिमा `name`, `description` र `inputSchema` जस्ता फिल्डहरू छन् जुन रिटर्न प्रकार अनुसार हुन्छन्। यसले हामीलाई उपकरण र फिचर परिभाषा अरू ठाउँमा राख्न सक्षम बनाउँछ। अब हामी सबै उपकरणहरू `tools` फोल्डरमा बनाउन सक्छौं र त्यस्तै तपाईंका सबै फिचरहरूका लागि पनि, त्यसैले तपाईंको प्रोजेक्ट यसरी व्यवस्थित हुन सक्छ:

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

त्यो राम्रो छ, हाम्रो वास्तुकला अलि सफा देखाउन सकिन्छ।

उपकरणहरू कल गर्ने कुरा के हो, त्यो पनि त्यस्तै हो, एउटा ह्यान्डलर सबै उपकरणलाई कल गर्ने? हो, बिल्कुल, यहाँ कोड छ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools लाई कुंजीको रूपमा उपकरण नामहरू रहेको शब्दकोश हो
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
    // TODO उपकरणलाई कल गर्नुहोस्,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

माथि कोडबाट देखिन्छ, हामीले उपकरण कल गर्न कुन उपकरण हो र कुन तर्कहरूसँग कल गर्नेछौं भनेर पार्स गर्नुपर्छ र त्यसपछि उपकरण कलमा अगाडि बढ्नुपर्छ।

## मान्यताको साथ प्रक्रिया सुधार गर्दै

अहिलेसम्म, तपाईंले देख्नुभएको छ कि कसरी उपकरण, स्रोत र प्रम्प्ट थप्नका लागि तपाईंले प्रत्येक फिचर प्रकारका लागि दुई ह्यान्डलरहरूले सबै दर्ताहरू प्रतिस्थापन गर्न सक्छ। अब हामीले के गर्नुपर्छ? हामीले उपकरणलाई सही तर्कहरूसँग कल गरिएको छ भन्ने सुनिश्चित गर्न केही प्रकारको मान्यता थप्नुपर्छ। हरेक रनटाइमको आफ्नै समाधान हुन्छ, उदाहरणका लागि Python ले Pydantic प्रयोग गर्छ र TypeScript ले Zod। विचार यस्तो छ:

- फिचर (उपकरण, स्रोत वा प्रम्प्ट) बनाउनको लागि यसको समर्पित फोल्डरमा तर्क सिर्जना गर्ने तर्क सार्नुहोस्।
- आउँदो अनुरोधलाई मान्य गर्नका लागि एउटा तरिका थप्नुहोस्, उदाहरणका लागि उपकरण कल गर्न।

### फिचर सिर्जना गर्नुहोस्

फिचर सिर्जना गर्न, हामीले त्यो फिचरको फाइल बनाउनुपर्छ र सुनिश्चित गर्नुपर्छ कि त्यहाँ आवश्यक फिल्डहरू छन्। यी फिल्डहरू उपकरण, स्रोत र प्रम्प्टहरू बीच अलि फरक हुन्छन्।

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
        # Pydantic मोडल प्रयोग गरेर इनपुट मान्य गर्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic थप्नुहोस्, ताकि हामी AddInputModel बनाउन सकौं र args मान्य गर्न सकौं

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ तपाईं देख्नुहुन्छ हामीले निम्न गर्छौं:

- Pydantic `AddInputModel` प्रयोग गरी स्किमा बनाउने जसमा फिल्डहरू `a` र `b` छन् फाइल *schema.py* मा।
- आउँदो अनुरोधलाई `AddInputModel` प्रकारको पार्स गर्ने प्रयास गर्ने, यदि प्यारामिटरहरू असम्बन्धित छन् भने क्र्यास हुनेछ:

   ```python
   # add.py
    try:
        # Pydantic मोडेल प्रयोग गरेर इनपुट प्रमाणित गर्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

तपाईं यो पार्सिङ तर्कलाई उपकरण कालमै वा ह्यान्डलर फंक्शनमै राख्न चयन गर्न सक्नुहुन्छ।

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

- सबै उपकरण कालहरूमा ह्यान्डलर भित्र, हामीले आउँदो अनुरोधलाई उपकरणले परिभाषित गरेको स्किमा अनुसार पार्स गर्न प्रयास गर्छौं:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    यदि त्यो सफल भयो भने हामी वास्तवमा उपकरण कल गर्न अगाडि बढ्छौं:

    ```typescript
    const result = await tool.callback(input);
    ```

देखाउन सकिन्छ, यस तरिकाले महान वास्तुकला सिर्जना हुन्छ किनभने सबै कुरा आफ्नो ठाउँमा हुन्छ, *server.ts* एउटा सानो फाइल हो जसले अनुरोध ह्यान्डलरहरूलाई मात्र जोड्छ र प्रत्येक फिचर तिनीहरूका सम्बन्धित फोल्डरहरूमा छन् जस्तै tools/, resources/ वा /prompts।

राम्रो, अब हामी यसलाई निर्माण गर्न प्रयास गरौं।

## अभ्यास: लो-लेवल सर्भर सिर्जना

यस अभ्यासमा, हामीले निम्न गर्नेछौं:

1. उपकरणहरूको सूची र उपकरण कल ह्यान्डल गर्ने लो-लेवल सर्भर सिर्जना गर्ने।
1. तपाईंले विस्तार गर्न सक्ने वास्तुकला कार्यान्वयन गर्ने।
1. उपकरण कलहरू ठीकसँग मान्य भए भन्ने सुनिश्चित गर्न मान्यता थप्ने।

### -1- वास्तुकला सिर्जना

पहिलो कुरा हामीले समाधान गर्नुपर्ने कुरा यस्तो वास्तुकला हो जसले हामीलाई फिचरहरू थप्दै विस्तार गर्न मद्दत गर्छ, यसले यसरी देखिन्छ:

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

अब हामीले एउटा वास्तुकला सेट गरेका छौं जसले हामी सजिलै उपकरणहरू tools फोल्डरमा थप्न सक्छौं। स्रोत र प्रम्प्टहरूका लागि उप-डिरेक्टोरीहरू थप्न यसलाई पालना गर्न स्वतन्त्र हुनुहोस्।

### -2- उपकरण सिर्जना

अर्को, उपकरण सिर्जना कस्तो देखिन्छ हेर्नुहोस्। सुरुमा, यसलाई यसको *tool* उप-डिरेक्टरीमा यसरी बनाउनुपर्छ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मोडेल प्रयोग गरी इनपुट प्रमाणित गर्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic थप्ने, ताकि हामी AddInputModel सिर्जना गरी args प्रमाणित गर्न सकौं

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ देख्न सकिन्छ कि कसरी नाम, विवरण, र इनपुट स्किमा Pydantic प्रयोग गरी परिभाषित गरिन्छ र एउटा ह्यान्डलर हुन्छ जुन यो उपकरण कल हुँदा कार्यान्वयन हुन्छ। अन्ततः, `tool_add` एक्स्पोज गरिएको छ जुन यी सबै सम्पत्तिहरू समेटिएको डिक्शनरी हो।

*schema.py* पनि छ जसले हाम्रो उपकरणले प्रयोग गर्ने इनपुट स्किमा परिभाषित गर्नका लागि प्रयोग हुन्छ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

हामीले *__init__.py* पनि भर्नु पर्छ ताकि tools डिरेक्टरीलाई एउटा मोड्युलको रुपमा व्यवहार गरियोस्। साथै, यसअन्तर्गतका मोड्युलहरूलाई यसरी एक्स्पोज गर्नुपर्छ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

नयाँ उपकरण थप्दा हामीले यस फाइलमा थप्न सक्छौं।

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

यहाँ हामी एउटा डिक्शनरी बनाउँछौं जसमा सम्पत्तिहरू समावेश छन्:

- name, यो उपकरणको नाम हो।
- rawSchema, यो Zod स्किमा हो, जसले यो उपकरण कल गर्ने अनुरोधहरूको मान्यता गर्नेछ।
- inputSchema, यो स्किमा ह्यान्डलरले प्रयोग गर्नेछ।
- callback, यो उपकरणलाई invoke गर्न प्रयोग हुन्छ।

`Tool` पनि छ जुन यो डिक्शनरीलाई एक प्रकारमा रूपान्तरण गर्छ जुन mcp सर्भर ह्यान्डलरले स्वीकार गर्न सक्छ र यसो देखिन्छ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

अनि *schema.ts* छ जहाँ हामी प्रत्येक उपकरणका लागि इनपुट स्किमाहरू राख्छौं जुन हाल केवल एउटा स्किमा मात्र छ तर उपकरण थप्दै जाँदा थप प्रविष्टिहरू थप्न सक्छौं:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

राम्ररी, अब हामी उपकरणहरूको सूची ह्यान्डल गर्न अघि बढौं।

### -3- उपकरण सूची ह्यान्डल गर्नुहोस्

अर्को, उपकरण सूची ह्यान्डल गर्न हामीलाई अनुरोध ह्यान्डलर सेटअप गर्नुपर्छ। हाम्रो सर्भर फाइलमा निम्न थप्नु आवश्यक छ:

**Python**

```python
# संक्षिप्तताको लागि कोड हटाइएको छ
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

यहाँ, हामी `@server.list_tools` डेकोरेटर थप्छौं र कार्यान्वयन गर्ने फंक्शन `handle_list_tools`। यसमा हामीले उपकरणहरूको सूची उत्पादन गर्नुपर्छ। हरेक उपकरणसँग नाम, विवरण र inputSchema हुनु आवश्यक छ भन्नाले ध्यान दिनुहोस्।   

**TypeScript**

सूची बनाउनका लागि अनुरोध ह्यान्डलर सेटअप गर्न, हामीले सर्भरमा `setRequestHandler` कल गर्नु पर्छ र स्किमालाई मिलाउनु पर्छ जुन हामी गर्न खोजिरहेका छौं, यस अवस्थामा `ListToolsRequestSchema`। 

```typescript
// इंडेक्स.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// सर्भर.ts
// brevity का लागि कोड हटाइएको
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // दर्ता गरिएका टूलहरूको सूची फर्काउनुहोस्
  return {
    tools: tools
  };
});
```

राम्ररी, अब हामीले उपकरण सूचीको टुक्रा समाधान गर्यौं, अब हेरौं कि कसरी उपकरणहरू कल गर्न सक्छौं।

### -4- उपकरण कल ह्यान्डल गर्नुहोस्

उपकरण कल गर्न, अर्को अनुरोध ह्यान्डलर सेटअप गर्नुपर्छ, यो पटक कुन फिचर कल गर्ने र कुन तर्कहरूसँग भन्ने निर्दिष्टीकरणको सामाना गर्न।

**Python**

हामी डेकोरेटर `@server.call_tool` प्रयोग गर्छौं र यसलाई `handle_call_tool` जस्तो फंक्शनमार्फत कार्यान्वयन गर्छौं। त्यो फंक्शनभित्र, हामी उपकरणको नाम, यसको तर्कहरू पार्स गर्नुपर्छ र उपकरणका लागि तर्कहरू मान्य छन् वा छैनन् भन्ने सुनिश्चित गर्नुपर्छ। हामी यस फंक्शनमा वा वास्तविक उपकरणमा पनि तर्कहरू मान्य गर्न सक्छौं।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools एउटा शब्दकोश हो जसका कुञ्जीहरू उपकरण नामहरू हुन्
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # उपकरण चलाउनुहोस्
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

यहाँ के हुन्छ:

- हाम्रो उपकरण नाम इनपुट प्यारामिटर `name` रूपमा पहिलेबाट छ जुन `arguments` डिक्शनरीका हाम्रो तर्कहरू हुन्।

- `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ले उपकरणलाई कल गर्छ। तर्कहरूको मान्यता `handler` सम्पत्तिमा हुन्छ जुन एउटा फंक्शन हो, यदि यो असफल भयो भने अपवाद उठ्छ। 

यति, अब हामीसँग लो-लेवल सर्भर प्रयोग गरेर उपकरण सूची बनाउने र कल गर्ने पूर्ण बुझाइ छ।

यहाँ [पूर्ण उदाहरण](./code/README.md) हेर्नुहोस्

## कार्य

तपाईंले पाएको कोडलाई धेरै उपकरण, स्रोत र प्रम्प्टसँग विस्तार गर्नुहोस् र कसरी तपाईंले केवल tools डिरेक्टरीमा फाइलहरू मात्र थप्नुपर्ने देख्नुहुन्छ।

*कुनै समाधान दिइएको छैन*

## सारांश

यस अध्यायमा, हामीले देख्यौं कि लो-लेवल सर्भर विधि कसरी काम गर्छ र यो कसरी राम्रो वास्तुकला सिर्जना गर्न मद्दत गर्छ जुन हामी निरन्तर निर्माण गर्न सक्छौं। हामीले मान्यताको विषयमा पनि छलफल गर्यौं र तपाईंलाई इनपुट मान्यताको लागि स्किमाहरू सिर्जना गर्न मान्यता पुस्तकालयहरू प्रयोग गर्ने तरिका देखाइयो।

## अर्को के छ

- अर्को: [सरल प्रमाणीकरण](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->