# उन्नत सर्भर प्रयोग

MCP SDK मा दुई फरक प्रकारका सर्भरहरू प्रदर्शित छन्, तपाईंको सामान्य सर्भर र कम-स्तर सर्भर। सामान्यतया, तपाईं सामान्य सर्भरलाई सुविधाहरू थप्न प्रयोग गर्नुहुन्छ। तर, केही अवस्थामा, तपाईंले कम-स्तर सर्भरमा भर पर्न चाहनुहुन्छ जस्तै:

- राम्रो संरचना। दुवै सामान्य सर्भर र कम-स्तर सर्भरसँग सफा संरचना बनाउन सम्भव छ, तर कम-स्तर सर्भरले सजिलो पनी हुन सक्छ भनी बहस गर्न सकिन्छ।
- सुविधा उपलब्धता। केही उन्नत सुविधाहरू केवल कम-स्तर सर्भरसँग मात्र प्रयोग गर्न सकिन्छ। तपाईंले यो पछि अध्यायहरूमा देख्नेछौं जस्तै नमूनाकरण र उत्तेजन थप्दा।

## सामान्य सर्भर र कम-स्तर सर्भर तुलना

यहाँ सामान्य सर्भरसंग MCP सर्भर बनाउने तरिका यस्तै देखिन्छ

**Python**

```python
mcp = FastMCP("Demo")

# एक थप उपकरण थप्नुहोस्
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

विषय हो कि तपाईंले स्पष्ट रूपमा प्रत्येक उपकरण, स्रोत वा प्रांप्ट जुन सर्भरमा आवश्यक छ त्यसलाई थप्नुहुन्छ। यसमा कुनै समस्या छैन।

### कम-स्तर सर्भर दृष्टिकोण

तर जब तपाईं कम-स्तर सर्भर दृष्टिकोण प्रयोग गर्नुहुन्छ तब तपाईंले फरक तरिकाले सोच्नुपर्छ। प्रत्येक उपकरण दर्ता गर्ने सट्टा, तपाईंले प्रत्येक सुविधा प्रकार (उपकरणहरू, स्रोतहरू वा प्रांप्टहरू) को लागि दुई ह्यान्डलरहरू सिर्जना गर्नुहुन्छ। उदाहरणको लागि, उपकरणहरूको लागि केवल दुई फंक्शन हुन्छन्:

- सबै उपकरणहरूको सूची बनाउने। एउटा फंक्शनले सबै उपकरणहरूको सूची बनाउने सबै प्रयासहरू संभाल्नेछ।
- सबै उपकरणहरूलाई कल गर्ने संभाल गर्ने। यहाँ पनि, केवल एउटा फंक्शनले उपकरणलाई कल गर्ने अनुरोधहरू संभाल्नेछ।

यो काम कम लाग्दोजस्तो सुनिन्छ है? त्यसैले उपकरण दर्ता गर्ने सट्टा, मलाई केवल सूची बनाउँदा यो उपकरण सूचीमा छ भनी सुनिश्चित गर्नुपर्छ र उपकरण कॉल गर्न आउने अनुरोधमा यो कल हुन्छ।

अब कोड कस्तो देखिन्छ हेरौं:

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

यहाँ अब हामीसँग एउटा फंक्शन छ जसले सुविधाहरूको सूची फर्काउँछ। उपकरण सूचीका प्रत्येक प्रविष्टिमा `name`, `description` र `inputSchema` जस्ता क्षेत्रहरू छन् जुन फर्काउने प्रकारमा मिल्छ। यसले हामीलाई उपकरणहरू र सुविधा परिभाषा अन्यत्र राख्न सक्षम बनाउँछ। हामी अब हाम्रो सबै उपकरणहरू tools फोल्डरमा राख्न सक्छौं र सबै सुविधाहरूका लागि पनि यस्तै गर्ने सकिन्छ, ताकि तपाईंको प्रोजेक्ट यसरी व्यवस्थित हुन सक्छ:

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

यो राम्रो हो, हाम्रो संरचना निकै सफा देखिने बनाउन सकिन्छ।

उपकरणहरू कल गर्ने कुरा के हो, के त्यो पनि त्यस्तै हो, कुनै पनि उपकरण कल गर्न एक ह्यान्डलर? हो, बिल्कुल सही, यहाँ त्यो कोड छ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools एउटा शब्दकोश हो जसमा उपकरण नामहरू कुञ्जीहरूका रूपमा हुन्छन्
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

माथिको कोडबाट देख्न सकिन्छ, हामीले उपकरण कल गर्नुपर्ने र कुन आर्गुमेन्टसहित कल गर्ने भन्ने पार्स गर्नुपर्छ, अनि उपकरणलाई कल गर्न अघि बढ्नुपर्छ।

## प्रमाणीकरणसँग यो दृष्टिकोण सुधार्नु

अहिलेसम्म, तपाईंले सबै दर्ता प्रक्रियाहरू कसरी दुई ह्यान्डलरहरू मार्फत प्रतिस्थापन गर्ने देख्नुभयो। अब के गर्नुपर्छ? हामीले उपकरण सही आर्गुमेन्टसहित कल भइरहेको छ भनी सुनिश्चित गर्न कुनै प्रमाणीकरण थप्नुपर्छ। प्रत्येक रनटाइमसँग यसको आफ्नै समाधान छ, जस्तै Python मा Pydantic र TypeScript मा Zod प्रयोग हुन्छ। विचार यस्तो छ:

- सुविधा (उपकरण, स्रोत वा प्रांप्ट) बनाउनको लागि तिनीको समर्पित फोल्डरमा तर्क सार्नुहोस्।
- उपकरण कॉल गर्न अनुरोध आएको प्रमाणीकरण गर्न उपयुक्त तरिका थप्नुहोस्।

### सुविधा सिर्जना गर्नुहोस्

सुविधा सिर्जना गर्न, हामीले त्यो सुविधाको लागि एउटा फाइल बनाउनुपर्छ र त्यो सुविधा आवश्यक पर्ने अनिवार्य क्षेत्रहरू सुनिश्चित गर्नुपर्छ। विभिन्न सुविधामा क्षेत्रहरू केही फरक हुन्छन्।

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
        # Pydantic मोडेल प्रयोग गरी इनपुट प्रमाणित गर्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic थप्नुहोस्, ताकि हामी AddInputModel बनाउन र args प्रमाणित गर्न सक्छौं

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ हामीले यो गर्छौं:

- Pydantic `AddInputModel` स्कीमा बनाएर `a` र `b` क्षेत्रहरू समावेश गर्ने, फाइल *schema.py* मा।
- आउने अनुरोधलाई `AddInputModel` प्रकारको पार्स गर्ने प्रयास गर्ने, यदि मापदण्डमा मेल नखाएमा प्रोग्राम क्र्यास हुन्छ:

   ```python
   # add.py
    try:
        # Pydantic मोडल प्रयोग गरेर इनपुट मान्य पार्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

यो पार्स गर्ने तर्क तपाईं उपकरण कलमा गर्ने वा ह्यान्डलर फंक्शनमा गर्ने रोज्न सक्नुहुन्छ।

**TypeScript**

```typescript
// सर्भर.ts
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

// स्कीमा.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// थप्नुहोस्.ts
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

- सबै उपकरण कल ह्यान्डलरमा, हामी अहिले आउने अनुरोधलाई उपकरणको परिभाषित स्कीमामा पार्स गर्न कोशिस गर्छौं:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    यदि सफल भयो भने वास्तविक उपकरणलाई कल गर्छौं:

    ```typescript
    const result = await tool.callback(input);
    ```

जसरी देख्न सकिन्छ, यसले राम्रो संरचना बनाउँछ किनभने सबै विषयहरूको निश्चित स्थान छ, *server.ts* एक सानो फाइल हो जुन केवल अनुरोध ह्यान्डलरहरू जोड्छ र प्रत्येक सुविधा आफ्नो फोल्डरमा जस्तै tools/, resources/ वा /prompts मा हुन्छ।

शानदार, अब यसलाई निर्माण गरौं।

## अभ्यास: कम-स्तर सर्भर सिर्जना

यस अभ्यासमा, हामी निम्न गर्नेछौं:

1. उपकरणहरूको सूची र उपकरण कलहरू ह्यान्डल गर्ने कम-स्तर सर्भर सिर्जना गर्ने।
2. तपाईँले विस्तार गर्न सक्ने संरचना कार्यान्वयन गर्ने।
3. तपाईंको उपकरण कल सही प्रमाणीकरण भएको सुनिश्चित गर्न प्रमाणीकरण थप्ने।

### -1- संरचना सिर्जना गर्नुहोस्

पहिलो कुरा भनेको एक यस्ता संरचना सिर्जना गर्ने हो जुन हामीलाई नयाँ सुविधाहरू थप्दा सजिलै विस्तार गर्न सघाउँछ, यसले यस्तै देखिन्छ:

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

अब हामीसँग यस्तो संरचना छ जसले सजिलै नयाँ उपकरणहरू tools फोल्डरमा थप्न सकिन्छ सुनिश्चित गर्छ। स्रोत र प्रांप्टहरूका लागि उप-डिरेक्टरीहरू थप्न स्वतन्त्र महसुस गर्नुहोस्।

### -2- उपकरण बनाउनुहोस्

अब उपकरण बनाउन कस्तो देखिन्छ हेरौं। पहिले यो आफ्नो *tool* उपडिरेक्टरीमा हुनुपर्छ जस्तै:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मोडल प्रयोग गरेर इनपुट प्रमाणित गर्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic थप्नुहोस्, ताकि हामी AddInputModel बनाउन र args प्रमाणित गर्न सकौं

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ हामीले नाम, विवरण र इनपुट स्कीमा Pydantic प्रयोग गरेर परिभाषित गर्ने र एउटा ह्यान्डलर बनाउने देखिन्छ जुन उपकरण कल हुँदा चलाइनेछ। अन्तमा, हामी `tool_add` लाई एक्सपोथ गर्छौं जुन यी सम्पत्तिहरू समावेश गर्दछ।

त्यहाँ *schema.py* पनि छ जुन उपकरणले प्रयोग गर्ने इनपुट स्कीमा परिभाषित गर्दछ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

हामीले *__init__.py* पनि भर्नुपर्ने हुन्छ जसले tools डिरेक्टरीलाई मोड्युलको रूपमा मानिन सुनिश्चित गर्छ। साथै, यसमा रहेका मोड्युलहरूलाई यसरी एक्सपोथ गर्नु पर्छ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

हामी यस फाइलमा थप उपकरणहरू थप्दै जान सक्छौं।

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

यहाँ हामी एक dictionary सिर्जना गर्छौं जसमा समावेश छन्:

- name, उपकरणको नाम।
- rawSchema, Zod स्कीमा हो, यसले उपकरण कॉल गर्न आउने अनुरोध प्रमाणीकरण गर्न प्रयोग हुन्छ।
- inputSchema, यो स्कीमा ह्यान्डलरले प्रयोग गर्छ।
- callback, उपकरणलाई कल गर्न प्रयोग हुन्छ।

त्यसका साथै `Tool` छ जसले यो dictionary लाई mcp सर्भर ह्यान्डलरले स्वीकार गर्न सक्ने प्रकारमा रुपान्तरण गर्छ र यसो देखिन्छ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

र *schema.ts* जहाँ हामी प्रत्येक उपकरणको इनपुट स्कीमा राख्छौं, अहिले एउटा मात्र छ तर जति उपकरणहरू थपिन्छ त्यति थप हुनेछ:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

शानदार, अब हामीले उपकरणहरूको सूची ह्यान्डल गर्ने काम गर्नुपर्नेछ।

### -3- उपकरण सूची ह्यान्डल गर्नुहोस्

अब उपकरणहरूको सूची ह्यान्डल गर्न, हामीले त्यो अनुरोध ह्यान्डलर सेटअप गर्नुपर्छ। हाम्रो सर्भर फाइलमा थप्नुपर्ने कुरा:

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

यहाँ, हामी `@server.list_tools` डेकोरेटर र `handle_list_tools` कार्यान्वयन गर्छौं। यसले उपकरणहरूको सूची उत्पादन गर्नुपर्छ। हरेक उपकरणमा नाम, विवरण र inputSchema चाहिन्छ।

**TypeScript**

उपकरणहरूको सूची बनाउन अनुरोध ह्यान्डलर सेटअप गर्न, हामीले सर्भरमा `setRequestHandler` कल गरेर `ListToolsRequestSchema` संग मिल्दोजुल्दो स्कीमा दिनु पर्छ।

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
// छोटकरीका लागि कोड हटाइयो
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // दर्ता गरिएका उपकरणहरूको सूची फर्काउनुहोस्
  return {
    tools: tools
  };
});
```

शानदार, अब हामीले उपकरणहरूको सूची बनाउने भाग समाधान गर्यौं, अब हामी कसरि उपकरणहरू कल गर्ने हेरौं।

### -4- उपकरण कल ह्यान्डल गर्नुहोस्

उपकरण कल गर्न अर्को अनुरोध ह्यान्डलर सेटअप गर्नुपर्छ, जुन कुन सुविधा कल गर्नुपर्ने र कुन आर्गुमेन्टसहित हो भनी अनुरोध ह्यान्डल गर्ने हुन्छ।

**Python**

`@server.call_tool` डेकोरेटर प्रयोग गरेर `handle_call_tool` नामक फंक्शन कार्यान्वयन गरौं। सो फंक्शनमा, उपकरणको नाम, आर्गुमेन्ट पार्स गर्नुपर्छ र उपकरणका लागि तर्कहरू मान्य छन् कि छैनन् सुनिश्चित गर्नुपर्छ। यस प्रमाणीकरण प्रक्रिया यो फंक्शन वा उपकरणमा हुन सक्छ।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # उपकरणहरू एउटा शब्दकोश हो जसमा उपकरणको नाम कुञ्जीका रूपमा हुन्छन्
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # उपकरणलाई कल गर्नुहोस्
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

यहाँ के हुन्छ:

- उपकरण नाम पहिले नै `name` इनपुट प्यारामिटरमा छ जुन `arguments` डिक्शनरीमा आर्गुमेन्टहरू नै हुन्।

- उपकरण यसरी कल हुन्छ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`। आर्गुमेन्ट प्रमाणीकरण `handler` नामक फंक्शनमा हुन्छ, यदि असफल भयो भने अपवाद आउनेछ।

अब हामीसँग कम-स्तर सर्भर प्रयोग गरी उपकरणहरूको सूची र कल गर्ने पूर्ण बुझाइ छ।

यहाँ [पूर्ण उदाहरण](./code/README.md) हेर्नुहोस्

## कार्य

तपाईंले पाएको कोडमा थुप्रै उपकरणहरू, स्रोतहरू र प्रांप्टहरू थप्नुहोस् र हेर्नुहोस् कि तपाईंलाई केवल tools डिरेक्टरीमा फाइलहरू मात्र थप्नुपर्छ, अरू कतै होइन।

*कुनै समाधान दिइएको छैन*

## सारांश

यस अध्यायमा, हामीले कसरी कम-स्तर सर्भर दृष्टिकोणले काम गर्छ र सहजै निर्माण गर्न मिल्ने राम्रो संरचना कसरी बनाउन सकिन्छ हेऱ्यौं। हामीले प्रमाणीकरणको कुरा पनि गर्‍यौं र तपाईँलाई प्रमाणीकरण पुस्तकालयहरू प्रयोग गरी इनपुट प्रमाणीकरणका लागि स्कीमा कसरी बनाउने देखाइयो।

## के आउँछ

- अर्को: [सरल प्रमाणीकरण](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ कृत्रिम बुद्धिमत्ता अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी सहीपनको प्रयास गर्दछौं, तर कृपया जान्नुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धि हुन सक्छ। मूल दस्तावेज आफ्नो मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि भ्रम वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->