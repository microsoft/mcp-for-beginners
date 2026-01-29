# उन्नत सर्भर प्रयोग

MCP SDK मा दुई प्रकारका सर्भरहरू उपलब्ध छन्: सामान्य सर्भर र लो-लेभल सर्भर। सामान्यतया, तपाईंले सामान्य सर्भर प्रयोग गरेर सुविधाहरू थप्नुहुन्छ। तर केही अवस्थामा, तपाईंले लो-लेभल सर्भरमा निर्भर गर्न चाहनुहुन्छ, जस्तै:

- राम्रो आर्किटेक्चर। सामान्य सर्भर र लो-लेभल सर्भर दुवै प्रयोग गरेर सफा आर्किटेक्चर बनाउन सकिन्छ, तर लो-लेभल सर्भर प्रयोग गर्दा यो अलि सजिलो हुन सक्छ।
- सुविधाको उपलब्धता। केही उन्नत सुविधाहरू केवल लो-लेभल सर्भरमा मात्र प्रयोग गर्न सकिन्छ। तपाईंले यो पछि अध्यायहरूमा देख्नुहुनेछ जब हामी स्याम्पलिङ र एलिसिटेसन थप्छौं।

## सामान्य सर्भर बनाम लो-लेभल सर्भर

सामान्य सर्भर प्रयोग गरेर MCP सर्भर कसरी बनाइन्छ भन्ने यहाँ देख्न सकिन्छ:

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

यहाँ मुख्य कुरा यो हो कि तपाईंले सर्भरमा चाहिने प्रत्येक टूल, स्रोत वा प्रम्प्ट स्पष्ट रूपमा थप्नुहुन्छ। यसमा कुनै समस्या छैन।  

### लो-लेभल सर्भरको दृष्टिकोण

तर, जब तपाईं लो-लेभल सर्भरको दृष्टिकोण अपनाउनुहुन्छ, तपाईंले फरक तरिकाले सोच्नुपर्छ। यहाँ प्रत्येक टूल, स्रोत वा प्रम्प्टको लागि दुई ह्यान्डलरहरू बनाइन्छ। उदाहरणका लागि, टूलहरूको लागि:

- सबै टूलहरूको सूची बनाउने। एउटा फङ्सनले टूलहरूको सूची बनाउने प्रयासहरूलाई जिम्मा लिन्छ।
- सबै टूलहरू कल गर्ने। यहाँ पनि, एउटा मात्र फङ्सनले टूलहरू कल गर्ने अनुरोधहरूलाई जिम्मा लिन्छ।

यो कम काम जस्तो लाग्छ, हैन? त्यसैले टूल दर्ता गर्ने सट्टा, म केवल यो सुनिश्चित गर्नुपर्छ कि टूल सूचीमा छ जब म सबै टूलहरूको सूची बनाउँछु र यो कल गरिन्छ जब टूल कल गर्न अनुरोध आउँछ।

अब कोड कस्तो देखिन्छ हेर्नुहोस्:

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

यहाँ हामीसँग अब एउटा फङ्सन छ जसले सुविधाहरूको सूची फर्काउँछ। टूलहरूको सूचीमा प्रत्येक प्रविष्टिमा `name`, `description` र `inputSchema` जस्ता फिल्डहरू छन् ताकि यो रिटर्न टाइपसँग मेल खान सकोस्। यसले हामीलाई हाम्रो टूलहरू र सुविधाहरूको परिभाषा अन्यत्र राख्न सक्षम बनाउँछ। अब हामी सबै टूलहरूलाई टूल्स फोल्डरमा राख्न सक्छौं र त्यस्तै सबै सुविधाहरूलाई पनि राख्न सक्छौं ताकि हाम्रो प्रोजेक्ट यसरी व्यवस्थित गर्न सकिन्छ:

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

यो राम्रो छ, हाम्रो आर्किटेक्चर सफा देखिन सक्छ।

टूलहरू कल गर्ने बारेमा के? के यो पनि एउटै विचार हो, एउटा ह्यान्डलर जसले कुनै पनि टूल कल गर्छ? हो, ठीक त्यस्तै। यहाँ त्यसको कोड छ:

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

माथिको कोडबाट देख्न सकिन्छ कि हामीले कल गर्नुपर्ने टूल र त्यसका लागि आवश्यक आर्गुमेन्टहरू छुट्याउनुपर्छ, त्यसपछि टूल कल गर्न अगाडि बढ्नुपर्छ।

## दृष्टिकोण सुधार गर्दै: मान्यता जाँच

अहिलेसम्म, तपाईंले देख्नुभएको छ कि टूल, स्रोत र प्रम्प्ट थप्नका लागि सबै दर्ताहरूलाई प्रत्येक सुविधाको प्रकारका लागि यी दुई ह्यान्डलरहरूद्वारा प्रतिस्थापन गर्न सकिन्छ। अब के गर्नुपर्छ? खैर, हामीले केही प्रकारको मान्यता थप्नुपर्छ ताकि टूल सही आर्गुमेन्टहरूसँग कल गरिएको होस्। प्रत्येक रनटाइमको आफ्नै समाधान छ, उदाहरणका लागि Python ले Pydantic प्रयोग गर्छ र TypeScript ले Zod प्रयोग गर्छ। विचार यो हो कि हामी निम्न कार्यहरू गर्छौं:

- सुविधाहरू (टूल, स्रोत वा प्रम्प्ट) सिर्जना गर्ने तर्कलाई यसको समर्पित फोल्डरमा सार्नुहोस्।
- टूल कल गर्न अनुरोध जाँच्नको लागि मान्यता थप्नुहोस्।

### सुविधा सिर्जना गर्नुहोस्

फिचर सिर्जना गर्न, हामीले त्यस फिचरको लागि फाइल सिर्जना गर्नुपर्छ र सुनिश्चित गर्नुपर्छ कि त्यसमा आवश्यक फिल्डहरू छन्। टूल, स्रोत र प्रम्प्टका लागि आवश्यक फिल्डहरू अलि फरक हुन्छन्।

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

यहाँ तपाईंले देख्न सक्नुहुन्छ कि हामी निम्न कार्यहरू गर्छौं:

- *schema.py* फाइलमा Pydantic `AddInputModel` प्रयोग गरेर `a` र `b` फिल्डहरू सहित स्किमा सिर्जना गर्नुहोस्।
- आउने अनुरोधलाई `AddInputModel` प्रकारको बनाउन प्रयास गर्नुहोस्। यदि प्यारामिटरहरूमा मेल छैन भने यो क्र्यास हुनेछ:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

तपाईंले यो पार्सिङ तर्क टूल कलमा राख्ने वा ह्यान्डलर फङ्सनमा राख्ने निर्णय गर्न सक्नुहुन्छ।

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

- सबै टूल कलहरूलाई ह्यान्डल गर्ने ह्यान्डलरमा, हामी आउने अनुरोधलाई टूलको परिभाषित स्किमामा पार्स गर्न प्रयास गर्छौं:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    यदि यो सफल भयो भने हामी वास्तविक टूल कल गर्न अगाडि बढ्छौं:

    ```typescript
    const result = await tool.callback(input);
    ```

जस्तो देखिन्छ, यो दृष्टिकोणले राम्रो आर्किटेक्चर सिर्जना गर्छ किनकि सबै कुराको आफ्नै स्थान हुन्छ। *server.ts* एउटा सानो फाइल हुन्छ जसले केवल अनुरोध ह्यान्डलरहरूलाई तारजोड गर्छ र प्रत्येक फिचरहरू आफ्ना फोल्डरहरूमा हुन्छन्, जस्तै tools/, resources/ वा /prompts।

राम्रो, अब यसलाई निर्माण गर्न प्रयास गरौं।

## अभ्यास: लो-लेभल सर्भर सिर्जना गर्नुहोस्

यस अभ्यासमा, हामी निम्न कार्यहरू गर्नेछौं:

1. टूलहरूको सूची बनाउने र टूलहरू कल गर्ने लो-लेभल सर्भर सिर्जना गर्नुहोस्।
1. निर्माण गर्न सकिने आर्किटेक्चर कार्यान्वयन गर्नुहोस्।
1. सुनिश्चित गर्नुहोस् कि तपाईंको टूल कलहरू सही रूपमा मान्यता प्राप्त छन्।

### -1- आर्किटेक्चर सिर्जना गर्नुहोस्

पहिलो कुरा हामीले सम्बोधन गर्नुपर्छ भनेको आर्किटेक्चर हो जसले हामीलाई थप सुविधाहरू थप्दै जाँदा स्केल गर्न मद्दत गर्छ। यहाँ यो कस्तो देखिन्छ:

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

अब हामीले यस्तो आर्किटेक्चर सेटअप गरेका छौं जसले सुनिश्चित गर्छ कि हामी सजिलैसँग टूल्स फोल्डरमा नयाँ टूलहरू थप्न सक्छौं। स्रोतहरू र प्रम्प्टहरूको लागि सबडाइरेक्टरीहरू थप्न स्वतन्त्र महसुस गर्नुहोस्।

### -2- टूल सिर्जना गर्नुहोस्

अब टूल सिर्जना गर्ने प्रक्रिया हेर्नुहोस्। पहिलो, यसलाई यसको *tool* सबडाइरेक्टरीमा यसरी सिर्जना गर्नुपर्छ:

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

यहाँ हामीले देख्छौं कि कसरी नाम, विवरण, Pydantic प्रयोग गरेर इनपुट स्किमा परिभाषित गरिन्छ र ह्यान्डलर बनाइन्छ जुन टूल कल हुँदा सक्रिय हुन्छ। अन्तमा, हामी `tool_add` लाई एक्सपोज गर्छौं जुन यी सबै गुणहरू समावेश गर्ने डिक्सनरी हो।

त्यहाँ *schema.py* पनि छ जुन हाम्रो टूलले प्रयोग गर्ने इनपुट स्किमा परिभाषित गर्न प्रयोग गरिन्छ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

हामीले *__init__.py* पनि भरपर्दो बनाउनुपर्छ ताकि टूल्स डाइरेक्टरीलाई मोड्युलको रूपमा व्यवहार गरियोस्। साथै, हामीले यसमा मोड्युलहरू एक्सपोज गर्नुपर्छ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

हामीले थप टूलहरू थप्दै जाँदा यस फाइलमा थप्न जारी राख्न सक्छौं।

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

यहाँ हामी गुणहरूको डिक्सनरी सिर्जना गर्छौं:

- name, यो टूलको नाम हो।
- rawSchema, यो Zod स्किमा हो, यो आउने अनुरोधहरूलाई मान्यता दिन प्रयोग गरिन्छ।
- inputSchema, यो स्किमा ह्यान्डलरले प्रयोग गर्नेछ।
- callback, यो टूललाई सक्रिय गर्न प्रयोग गरिन्छ।

त्यहाँ `Tool` पनि छ जसले यस डिक्सनरीलाई प्रकारमा रूपान्तरण गर्छ जुन MCP सर्भर ह्यान्डलरले स्वीकार गर्न सक्छ। यो यसरी देखिन्छ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

त्यहाँ *schema.ts* पनि छ जहाँ हामी प्रत्येक टूलको इनपुट स्किमाहरू राख्छौं। हालको अवस्थामा केवल एउटा स्किमा छ, तर हामी टूलहरू थप्दै जाँदा थप प्रविष्टिहरू थप्न सक्छौं:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

राम्रो, अब हामी हाम्रो टूलहरूको सूची ह्यान्डल गर्न अगाडि बढ्छौं।

### -3- टूल सूची ह्यान्डल गर्नुहोस्

टूलहरूको सूची ह्यान्डल गर्न, हामीले त्यसका लागि अनुरोध ह्यान्डलर सेटअप गर्नुपर्छ। यहाँ हामीले हाम्रो सर्भर फाइलमा थप्नुपर्ने कुरा छ:

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

यहाँ हामीले `@server.list_tools` डेकोरेटर र `handle_list_tools` कार्यान्वयन गर्ने फङ्सन थप्छौं। पछिल्लोमा, हामीले टूलहरूको सूची उत्पादन गर्नुपर्छ। प्रत्येक टूलमा नाम, विवरण र inputSchema हुनुपर्छ।

**TypeScript**

टूलहरूको सूची बनाउने अनुरोध ह्यान्डलर सेटअप गर्न, हामीले सर्भरमा `setRequestHandler` कल गर्नुपर्छ। यसमा `ListToolsRequestSchema` स्किमा चाहिन्छ।

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

राम्रो, अब हामीले टूलहरूको सूची बनाउने टुक्रा समाधान गरेका छौं। अब टूलहरू कल गर्ने प्रक्रिया हेर्न अगाडि बढौं।

### -4- टूल कल ह्यान्डल गर्नुहोस्

टूल कल गर्न, हामीले अर्को अनुरोध ह्यान्डलर सेटअप गर्नुपर्छ। यसले कुन फिचर कल गर्ने र कुन आर्गुमेन्टहरूसँग कल गर्ने अनुरोधलाई सम्बोधन गर्छ।

**Python**

हामी `@server.call_tool` डेकोरेटर प्रयोग गर्छौं र `handle_call_tool` जस्तो फङ्सन कार्यान्वयन गर्छौं। त्यस फङ्सनभित्र, हामीले टूलको नाम, यसको आर्गुमेन्ट छुट्याउनुपर्छ र सुनिश्चित गर्नुपर्छ कि आर्गुमेन्टहरू टूलको लागि मान्य छन्। हामीले यो मान्यता यस फङ्सनमा वा टूलमा राख्न सक्छौं।

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

यहाँ के हुन्छ:

- हाम्रो टूलको नाम पहिले नै इनपुट प्यारामिटर `name` को रूपमा उपलब्ध छ। आर्गुमेन्टहरू `arguments` डिक्सनरीको रूपमा उपलब्ध छन्।

- टूल `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` प्रयोग गरेर कल गरिन्छ। आर्गुमेन्टहरूको मान्यता `handler` गुणमा हुन्छ जुन फङ्सनमा पोइन्ट गर्छ। यदि यो असफल भयो भने यो अपवाद फ्याँक्छ।

अब हामीले लो-लेभल सर्भर प्रयोग गरेर टूलहरूको सूची बनाउने र टूलहरू कल गर्ने प्रक्रिया पूर्ण रूपमा बुझ्यौं।

पूरा उदाहरण [यहाँ](./code/README.md) हेर्नुहोस्।

## असाइनमेन्ट

तपाईंलाई दिइएको कोडलाई टूलहरू, स्रोतहरू र प्रम्प्टहरूको संख्या थपेर विस्तार गर्नुहोस्। ध्यान दिनुहोस् कि तपाईंले केवल टूल्स डाइरेक्टरीमा फाइलहरू थप्नुपर्छ र अन्यत्र केही गर्नुपर्दैन।

*कुनै समाधान दिइएको छैन*

## सारांश

यस अध्यायमा, हामीले लो-लेभल सर्भर दृष्टिकोण कसरी काम गर्छ र यसले राम्रो आर्किटेक्चर सिर्जना गर्न कसरी मद्दत गर्छ भन्ने कुरा देख्यौं। हामीले मान्यता जाँचको चर्चा गर्यौं र तपाईंलाई इनपुट मान्यता गर्न स्किमा सिर्जना गर्न मान्यता पुस्तकालयहरूसँग काम गर्ने तरिका देखाइयो।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।