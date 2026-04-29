# उन्नत सर्भर प्रयोग

MCP SDK मा दुई विभिन्न प्रकारका सर्भरहरू खुला छन्, तपाईंको सामान्य सर्भर र लो-लेवल सर्भर। सामान्यतया, तपाईंले यसमा सुविधाहरू थप्न सामान्य सर्भर प्रयोग गर्नुहुन्छ। तर केही अवस्थामा, तपाईं लो-लेवल सर्भरमा निर्भर हुनुहुन्छ जुन जस्तै:

- राम्रो वास्तुकला। सामान्य सर्भर र लो-लेवल दुवै सर्भरसँग सफा वास्तुकला बनाउन सकिन्छ तर त्यो केही हदसम्म लो-लेवल सर्भरसँग सजिलो हुन सक्छ भनी बहस गर्न सकिन्छ।
- सुविधा उपलब्धता। केही उन्नत सुविधाहरू केवल लो-लेवल सर्भरसँग मात्र प्रयोग गर्न सकिन्छ। तपाईंले यो पछि अध्यायहरूमा देख्नु हुनेछ जब हामी नमूना र elicitation थप्छौं।

## सामान्य सर्भर vs लो-लेवल सर्भर

यहाँ एक MCP सर्भरको सिर्जना सामान्य सर्भरसँग कस्तो देखिन्छ:

**Python**

```python
mcp = FastMCP("Demo")

# थप उपकरण थप्नुहोस्
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

// थप उपकरण थप्नुहोस्
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

मूल कुरा यो हो कि तपाईं स्पष्ट रूपमा प्रत्येक उपकरण, स्रोत वा संकेत (prompt) जुन तपाईं सर्भरमा चाहनुहुन्छ त्यसलाई थप्नुहुन्छ। यसमा केही पनि गलत छैन।

### लो-लेवल सर्भर दृष्टिकोण

तर, जब तपाईं लो-लेवल सर्भर दृष्टिकोण प्रयोग गर्नुहुन्छ, तपाईंले यसलाई फरक तरिकाले सोचना आवश्यक छ। प्रत्येक उपकरण दर्ता गर्नको सट्टा, तपाईं प्रत्येक सुविधाका लागि दुई ह्याण्डलरहरू सिर्जना गर्नुहुन्छ (उपकरणहरू, स्रोतहरू वा संकेतहरू)। उदाहरणका लागि उपकरणहरूका लागि केवल दुईवटा फंक्सनहरू हुन्छन्:

- सबै उपकरणहरूको सूचीकरण। एउटै फङ्सन सबै उपकरणहरू सूचीबद्ध गर्ने प्रयासहरूको जिम्मेवार हुन्छ।
- सबै उपकरणहरूलाई कल गर्ने कार्य। यहाँ पनि, एउटा मात्र फङ्सन उपकरणलाई कल गर्नको लागि जिम्मेवार हुन्छ।

यो सम्भावित कम काम जस्तो सुनिन्छ होइन र? त्यसैले उपकरण दर्ता गर्नुको सट्टा, म केवल यो सुनिश्चित गर्नु पर्छ कि उपकरणहरू सूचीमा सूचीबद्ध छन् र उपकरण कलको लागि अनुरोध आइपर्दा उक्त उपकरण कल हुन्छ।

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
  // दर्ता गरिएको उपकरणहरूको सूची फिर्ता गर्नुहोस्
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

यहाँ हामीसँग एक फङ्सन छ जसले सुविधाहरूको सूची फर्काउँछ। उपकरणहरूको प्रत्येक प्रवेशमा अब `name`, `description` र `inputSchema` जस्ता फिल्डहरू छन् जसले फर्काइएको प्रकारलाई पालना गर्छ। यसले हामीलाई हाम्रो उपकरण र सुविधा परिभाषालाई जहाँसुकै राख्न सक्ने बनाउँछ। हामी अब सबै उपकरणहरूलाई tools फोल्डरमा बनाउन सक्छौं र सबै सुविधा पनि त्यसैगरी राख्न सकिन्छ, यसले तपाईंको परियोजना यसरी व्यवस्थित हुन सक्छ:

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

यो राम्रो छ, हाम्रो वास्तुकला निकै सफा देखिने बनाउन सकिन्छ।

उपकरणहरू कॉल गर्ने कुरा के हो, के त्यो पनि त्यस्तै सोच हो, एउटा ह्याण्डलरले कुनै पनि उपकरणलाई कल गर्ने? हो, बिल्कुल, यसका लागि कोड यस्तो देखिन्छ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools एउटा शब्दकोश हो जहाँ टूल नामहरू कुञ्जीको रूपमा छन्
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

माथिको कोडबाट देख्न सकिन्छ, हामीले कल गर्ने उपकरण र यसको आर्गुमेन्टहरू पार्स गर्नुपर्छ, अनि उपकरणलाई कल गर्न जानुपर्छ।

## मान्यता (Validation) संग दृष्टिकोण सुधार

अझसम्म, तपाईंले देख्नु भयो कि कसरी उपकरणहरू, स्रोतहरू र संकेतहरू थप्नका लागि सबै दर्ता यी दुई ह्याण्डलरहरूबाट प्रतिस्थापन गर्न सकिन्छ। अब अरू के गर्नु आवश्यक छ? हामीले कुनै न कुनै प्रकारको मान्यता थप्नुपर्छ जसले सुनिश्चित गर्छ कि उपकरणलाई सही आर्गुमेन्टसँग कल गरिएको छ। प्रत्येक रनटाइमसँग यसको आफ्नै समाधान छ, उदाहरणका लागि Python ले Pydantic प्रयोग गर्छ र TypeScript ले Zod प्रयोग गर्छ। विचार यस्तो छ:

- सुविधा (उपकरण, स्रोत वा संकेत) सिर्जना गर्ने तर्कलाई यसको समर्पित फोल्डरमा सार्ने।
- उपकरण कल गर्न अनुरोध गर्दा त्यसको मान्यता गर्ने तरिका थप्ने।

### सुविधा सिर्जना गर्नुहोस्

सुविधा सिर्जना गर्न, हामीलाई त्यो सुविधाको लागि एउटा फाइल बनाउनुपर्छ र त्यसमा आवश्यक अनिवार्य फिल्डहरू हुनु जरुरी छ। कुन फिल्डहरू फरक-फरक हुन्छन् उपकरण, स्रोत र संकेतहरूमा।

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
        # Pydantic मोडल प्रयोग गरी इनपुट प्रमाणीकरण गर्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic थप्नुहोस्, ताकि हामी AddInputModel बनाउन र args प्रमाणीकरण गर्न सकौं

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ हेर्नुहोस् हामीले के गरेका छौं:

- Pydantic ‘AddInputModel’ प्रयोग गरेर स्कीमा बनाएर *schema.py* फाइलमा `a` र `b` फिल्डहरू राखेका छौं।
- आउने अनुरोधलाई `AddInputModel` प्रकारमा पार्स गर्ने प्रयास गर्छौं, यदि प्यारामीटरमा विसङ्गति छ भने यो क्र्यास हुनेछ:

   ```python
   # add.py
    try:
        # Pydantic मोडल प्रयोग गरी इनपुट प्रमाणित गर्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

तपाईं यो पार्सिङ तर्कलाई उपकरण कलमा राख्न सक्छ वा ह्याण्डलर फंक्शनमा राख्न सक्छ।

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

// स्किम.ts
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

- सबै उपकरण कलहरूलाई ह्याण्डल गर्ने ह्याण्डलरमा, हामी अहिले आउने अनुरोधलाई उपकरणले परिभाषित स्कीमामा पार्स गर्ने प्रयास गर्छौं:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    यदि यो सफल भयो भने हामी वास्तविक उपकरणलाई कल गर्न अघि बढ्छौं:

    ```typescript
    const result = await tool.callback(input);
    ```

जस्तै देख्नुभयो, यस दृष्टिकोणले राम्रो वास्तुकला सिर्जना गर्छ किनकि प्रत्येक कुरा यसको स्थानमा हुन्छ, *server.ts* एउटा सानो फाइल हो जसले केवल अनुरोध ह्याण्डलरहरूलाई जोड्छ र प्रत्येक सुविधा आफ्नो सम्बन्धित फोल्डरमा हुन्छ जस्तै tools/, resources/ वा prompts/.

शानदार, अब यसलाई निर्माण गर्ने प्रयास गरौं।

## अभ्यास: लो-लेवल सर्भर सिर्जना

यस अभ्यासमा, हामी यस्ता चरणहरू गर्नेछौं:

1. उपकरणहरूको सूची र उपकरणको कल गर्ने लो-लेवल सर्भर सिर्जना गर्ने।
2. तपाईंले निर्माण गर्न सक्ने वास्तुकला कार्यान्वयन गर्ने।
3. तपाईंका उपकरण कलहरू उचित रूपमा मान्य छन् भनी सुनिश्चित गर्न मान्यता थप्ने।

### -1- वास्तुकला सिर्जना गर्नुहोस्

सर्वप्रथम हामीले अड्रेस गर्नुपर्ने कुरा यस्तो वास्तुकला हो जसले सुविधाहरू थप गर्दै जाँदा स्केलिङ मद्दत गर्दछ, यसरी देखिन्छ:

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

अब हामीले यस्तो वास्तुकला सेट गर्यौं जसले हामीलाई सजिलै नयाँ उपकरणहरू tools फोल्डरमा थप्न अनुमति दिन्छ। स्रोत र संकेतहरूको लागि उप-डिरेक्टरी थप्न यो पालना गर्न सक्नुहुन्छ।

### -2- उपकरण सिर्जना गर्ने

अब, उपकरण सिर्जना कस्तो देखिन्छ हेर्नुहोस्। पहिले यो *tool* उप-डिरेक्टरीमा सिर्जना हुनुपर्छ, यसरी:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मोडल प्रयोग गरेर इनपुट मान्यता गर्नुहोस्
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic थप्नुहोस्, ताकि हामी AddInputModel बनाउन र आर्गुमेन्टहरू मान्यता गर्न सकौं

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ हामीले उपकरणको नाम, वर्णन, र इनपुट स्कीमा पायडेन्टिक प्रयोग गरेर परिभाषित गरेका छौं र एक ह्याण्डलर पनि छ जुन उपकरण कल गर्दा ब्यवस्थित हुन्छ। अन्तमा, हामीले `tool_add` एक्स्पोज गरेका छौं जुन यी सम्पूर्ण विवरणहरू समेटेका एउटा डिक्शनरी हो।

त्यसैगरी *schema.py* छ जहाँ हामीले हाम्रो उपकरणको इनपुट स्कीमा परिभाषित गरेका छौं:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

हामीले *__init__.py* फाइल पनि भर्नुपर्छ जसले उपकरण डायरेक्टरीलाई एक मोड्युल जस्तो व्यवहार गर्न सहयोग पुर्याउँछ। साथै, हामीलाई यसमा रहेका मोड्युलहरूलाई यसरी एक्स्पोज गर्नुपर्छ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

हामी प्रत्येक नयाँ उपकरण थप्दा यस फाइलमा थप गर्न सकिन्छ।

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

यहाँ हामी गुणहरू समेटिएको डिक्शनरी बनाउँछौं:

- name, उपकरणको नाम हो।
- rawSchema, यो Zod स्कीमा हो, यसको प्रयोग उपकरण कल गर्न आउने अनुरोधहरू प्रमाणित गर्न हुनेछ।
- inputSchema, यो स्कीमालाई ह्याण्डलरले प्रयोग गर्नेछ।
- callback, यो उपकरण कल गर्न प्रयोग हुन्छ।

त्यहाँ `Tool` छ जसले यस डिक्शनरीलाई mcp सर्भर ह्याण्डलरले स्वीकार गर्ने प्रकारमा रूपान्तरण गर्छ जसो देखिन्छ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

र *schema.ts* छ जहाँ हामी प्रत्येक उपकरणको इनपुट स्कीमा भण्डारण गर्छौं जुन हाल एकै स्कीमा मात्र भएको भएता पनि उपकरणहरू थप्दा थप विवरण थप्न सकिन्छ:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

शानदार, अब हामीले उपकरणहरूको सूचीकरण ह्यान्डल गर्ने क्रममा अघि बढौं।

### -3- उपकरण सूचीकरण ह्यान्डल गर्ने

अब, उपकरणहरूको सूची ह्यान्डल गर्न हामीलाई अनुरोध ह्याण्डलर सेटअप गर्नुपर्छ, हाम्रो सर्भर फाइलमा यसो थप्नुपर्छ:

**Python**

```python
# संक्षिप्तताका लागि कोड छाडिएको छ
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

यहाँ, हामीले `@server.list_tools` डेकोरेटर थपेका छौं र कार्यान्वयन गर्ने फंक्शन `handle_list_tools` राखेका छौं। यस फंक्शनमा हामी उपकरणहरूको सूची प्रदान गर्नुपर्छ। हरेक उपकरणसँग नाम, विवरण र inputSchema हुनुपर्छ।

**TypeScript**

उपकरण सूचीकरण गर्न अनुरोध ह्याण्डलर सेटअप गर्न हामीले सर्भरमा `setRequestHandler` कल गरिन्छ जुन स्कीमा अनुरूप हुन्छ, यो अवस्थामा `ListToolsRequestSchema`।

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
// संक्षिप्तताका लागि कोड छोडिएको
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // दर्ता गरिएका उपकरणहरूको सूची फर्काउनुहोस्
  return {
    tools: tools
  };
});
```

शानदार, अब हामीले उपकरणहरूको सूचीकरणको भाग समाधान गर्यौं, अर्को उपकरणहरू कसरी कल गर्नेछौं हेर्नुहोस्।

### -4- उपकरण कल ह्यान्डल गर्ने

उपकरण कल गर्न अर्को अनुरोध ह्याण्डलर सेटअप गर्नुपर्छ, यस पटक त्यो अनुरोधमा कुन सुविधा कल गर्ने र के आर्गुमेन्टहरू हुने भनेर फोकस गरिन्छ।

**Python**

`@server.call_tool` डेकोरेटर प्रयोग गरी `handle_call_tool` फंक्शन कार्यान्वयन गरौं। यस फंक्शनमा हामीले उपकरणको नाम, यसको आर्गुमेन्ट पार्स गर्नुपर्छ र ती आर्गुमेन्टहरू उपकरण अनुरूप सही छन् कि छैनन् भनी सुनिश्चित गर्नुपर्छ। हामी यी आर्गुमेन्टहरूलाई उक्त फंक्सनमा वा उपकरणको वास्तविक ह्यान्डलरमा सत्यापन गर्न सकिन्छ।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools एक शब्दकोश हो जसमा उपकरण नामहरू कुञ्जीहरूका रूपमा हुन्छन्
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

यस्तो हुन्छ:

- हाम्रो उपकरण नाम पहिले नै इनपुट प्यारामीटर `name` मा छ, जुन `arguments` डिक्शनरीको रूपमा हामीले लिएको आर्गुमेन्टसँग मिल्छ।

- उपकरण `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ले कल हुन्छ। आर्गुमेन्टको मान्यता `handler` प्रोपर्टीमा हुन्छ जुन फङ्सनमा इशारा गर्छ, यदि त्यो असफल भयो भने अपवाद आइपर्दछ।

यति, अब हामीसँग लो-लेवल सर्भर प्रयोग गरी उपकरणहरू सूचीकरण र कल गर्नु कस्तो हुन्छ भन्ने पूर्ण बुझाइ छ।

पूरा उदाहरण यहाँ हेर्नुहोस्: [full example](./code/README.md)

## असाइनमेन्ट

तपाईंले दिएको कोडलाई थप उपकरणहरू, स्रोतहरू र संकेतहरू सहित विस्तार गर्नुहोस् र कस्तो महसुस हुन्छ त्यो प्रतिबिम्बित गर्नुहोस् कि तपाईंलाई केवल tools डाइरेक्टरीमा फाइलहरू मात्र थप्न आवश्यक पर्छ र अरु ठाउँमा होइन।

*कुनै समाधान दिइएको छैन*

## सारांश

यस अध्यायमा, हामीले लो-लेवल सर्भर दृष्टिकोण कसरी काम गर्छ र यसले कस्तो राम्रो वास्तुकला सिर्जना गर्न मद्दत गर्छ भनेर देख्यौं। हामीले मान्यता (validation) पनि छलफल गर्यौं र कसरी मान्यता लाइब्रेरीहरू (जस्तै Pydantic र Zod) प्रयोग गरेर इनपुटको स्कीमा बनाउने देख्यौं।

## के छ अर्को

- अर्को: [सरल प्रमाणिकरण](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यस दस्तावेजलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुनसक्छन्। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुँदैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->