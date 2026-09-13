# उन्नत सर्वर उपयोग

MCP SDK में दो अलग प्रकार के सर्वर उपलब्ध हैं, आपका सामान्य सर्वर और लो-लेवल सर्वर। सामान्यतः, आप इसके लिए नियमित सर्वर का उपयोग करते हैं ताकि इसमें फीचर्स जोड़े जा सकें। लेकिन कुछ मामलों में, आप लो-लेवल सर्वर पर निर्भर रहना चाहते हैं जैसे कि:

- बेहतर वास्तुकला। एक साफ-सुथरी वास्तुकला बनाना संभव है जिसमें दोनों नियमित सर्वर और लो-लेवल सर्वर होते हैं, लेकिन यह कहा जा सकता है कि लो-लेवल सर्वर के साथ यह थोड़ा आसान होता है।
- फीचर उपलब्धता। कुछ उन्नत फीचर केवल
    लो-लेवल सर्वर के साथ ही उपयोग किए जा सकते हैं। बाद के अध्यायों में Elicitation और legacy Sampling
    फीचर को कवर किया गया है, जो MCP `2026-07-28` में अप्रचलित हो चुका है।

## नियमित सर्वर बनाम लो-लेवल सर्वर

नियमित सर्वर के साथ MCP Server बनाने का यह तरीका है

**Python**

```python
mcp = FastMCP("Demo")

# एक जोड़ने का उपकरण जोड़ें
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

// एक जोड़ उपकरण जोड़ें
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

मुख्य बात यह है कि आप स्पष्ट रूप से प्रत्येक टूल, संसाधन या प्रॉम्प्ट जो आप सर्वर में चाहते हैं उसे जोड़ते हैं। इसमें कोई गलती नहीं है।  

### लो-लेवल सर्वर दृष्टिकोण

हालांकि, जब आप लो-लेवल सर्वर दृष्टिकोण का उपयोग करते हैं तो आपको उसे अलग तरह से सोचना होगा। प्रत्येक टूल को रजिस्टर करने के बजाय, आप प्रत्येक फीचर प्रकार (टूल, संसाधन या प्रॉम्प्ट) के लिए दो हैंडलर बनाते हैं। उदाहरण के लिए, टूल्स के लिए केवल दो फंक्शंस होते हैं जैसे:

- सभी टूल्स की सूची बनाना। एक फ़ंक्शन सभी टूल्स की सूची बनाने के प्रयासों के लिए जिम्मेदार होगा।
- टूल कॉल का हैंडल करना। यहाँ भी केवल एक फ़ंक्शन टूल कॉल्स को संभालता है।

यह संभावित रूप से कम काम जैसा लगता है, है ना? तो टूल को रजिस्टर करने के बजाय, मुझे बस यह सुनिश्चित करना है कि जब मैं सभी टूल्स की सूची बनाऊं तब वह टूल सूचीबद्ध हो और जब टूल कॉल करने के लिए रिक्वेस्ट आए तो वह कॉल हो जाए। 

अब कोड कैसा दिखता है, आइए देखते हैं:

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
  // पंजीकृत उपकरणों की सूची वापस करें
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

अब हमारे पास एक फ़ंक्शन है जो फीचर्स की सूची लौटाता है। टूल्स सूची में प्रत्येक प्रविष्टि में `name`, `description` और `inputSchema` जैसे फ़ील्ड होते हैं ताकि रिटर्न प्रकार का अनुपालन हो सके। इससे हम अपने टूल्स और फीचर परिभाषा को कहीं और रख सकते हैं। अब हम अपने सभी टूल्स को एक tools फ़ोल्डर में बना सकते हैं और आपके सभी फीचर्स के लिए भी यही, ताकि आपका प्रोजेक्ट इस प्रकार व्यवस्थित हो सके:

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

यह बढ़िया है, हमारी वास्तुकला काफी साफ-सुथरी लग सकती है।

टूल कॉल करने के बारे में क्या, क्या यह वही विचार है, एक हैंडलर किस्म के हर टूल को कॉल करने का? बिल्कुल, यहां उसका कोड है:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools एक शब्दकोश है जिसमें टूल के नाम कुंजी के रूप में हैं
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
    // TODO टूल को कॉल करें,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ऊपर दिए गए कोड से आप देख सकते हैं कि हमें कॉल करने के लिए टूल और उसके तर्कों को पार्स करना होगा, फिर टूल को कॉल करना होगा।

## सत्यापन के साथ दृष्टिकोण में सुधार

अब तक, आपने देखा कि टूल्स, संसाधनों और प्रॉम्प्ट्स को जोड़ने के लिए आपकी सभी रजिस्ट्रेशन को प्रति फीचर प्रकार दो हैंडलर से बदला जा सकता है। अब हमें और क्या करना है? खैर, हमें कुछ प्रकार का सत्यापन जोड़ना चाहिए ताकि यह सुनिश्चित हो सके कि टूल सही तर्कों के साथ कॉल किया गया है। प्रत्येक रनटाइम इसका अपना समाधान रखता है, उदाहरण के लिए Python में Pydantic और TypeScript में Zod होता है। विचार यह है कि हम निम्न करें:

- एक फीचर (टूल, संसाधन या प्रॉम्प्ट) बनाने की लॉजिक को उसके समर्पित फ़ोल्डर में स्थानांतरित करें।
- एक तरीका जोड़ें जिससे आने वाले अनुरोध, जैसे कि टूल कॉल करने का अनुरोध, को सत्यापित किया जा सके।

### एक फीचर बनाएँ

एक फीचर बनाने के लिए, हमें उस फीचर के लिए एक फ़ाइल बनानी होगी और सुनिश्चित करना होगा कि उसमें उस फीचर के आवश्यक अनिवार्य फ़ील्ड मौजूद हों। ये फ़ील्ड टूल्स, संसाधन और प्रॉम्प्ट्स के अनुसार थोड़ा अलग होते हैं।

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
        # Pydantic मॉडल का उपयोग करके इनपुट को मान्य करें
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोड़ें, ताकि हम एक AddInputModel बना सकें और आर्ग्यूमेंट्स को मान्य कर सकें

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ आप देख सकते हैं कि हम निम्न काम करते हैं:

- Pydantic `AddInputModel` का उपयोग करके schema बनाते हैं जिसमें फ़ील्ड `a` और `b` फ़ाइल *schema.py* में होते हैं।
- आने वाले अनुरोध को `AddInputModel` प्रकार में पार्स करने का प्रयास करते हैं, यदि पैरामीटर में मेल नहीं बैठता तो क्रैश होगा:

   ```python
   # add.py
    try:
        # Pydantic मॉडल का उपयोग करके इनपुट को मान्य करें
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

आप चुन सकते हैं कि यह पार्सिंग लॉजिक टूल कॉल में रखें या हैंडलर फ़ंक्शन में।

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

- सभी टूल कॉल्स को संभालने वाले हैंडलर में, हम अब आने वाले अनुरोध को टूल की परिभाषित स्कीमा में पार्स करने की कोशिश करते हैं:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    यदि वह सही होता है तो हम असली टूल को कॉल करने के लिए आगे बढ़ते हैं:

    ```typescript
    const result = await tool.callback(input);
    ```

जैसा आप देख सकते हैं, यह दृष्टिकोण एक शानदार वास्तुकला बनाता है क्योंकि सबकुछ अपनी जगह पर होता है, *server.ts* एक बहुत छोटी फ़ाइल होती है जो केवल अनुरोध हैंडलर्स को वायर करता है और प्रत्येक फीचर अपने संबंधित फ़ोल्डर में होता है जैसे tools/, resources/ या /prompts।

बढ़िया, अब इसे बनाना शुरू करते हैं।

## अभ्यास: एक लो-लेवल सर्वर बनाना

इस अभ्यास में, हम निम्न करेंगे:

1. एक लो-लेवल सर्वर बनाएंगे जो टूल्स की सूची बनाना और उन्हें कॉल करना संभाले।
1. एक ऐसी वास्तुकला लागू करेंगे जिस पर आप आगे निर्माण कर सकते हैं।
1. सत्यापन जोड़ेंगे ताकि आपके टूल कॉल सही ढंग से सत्यापित हों।

### -1- एक वास्तुकला बनाएँ

पहली बात जो हमें संबोधित करनी है वह है एक ऐसी वास्तुकला जो अधिक फीचर्स जोड़ने पर आसानी से बढ़ाई जा सके, यह इस प्रकार है:

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

अब हमने एक ऐसी वास्तुकला सेट कर ली है जो सुनिश्चित करती है कि हम आसानी से tools फ़ोल्डर में नए टूल जोड़ सकें। संसाधनों और प्रॉम्प्ट्स के लिए उपनिर्देशिकाएं जोड़ने के लिए स्वतंत्र महसूस करें।

### -2- टूल बनाना

अगला देखते हैं कि टूल बनाना कैसा दिखता है। पहले, इसे उसके *tool* उपनिर्देशिका में बनाया जाना चाहिए जैसे:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मॉडल का उपयोग करके इनपुट मान्य करें
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोड़ें, ताकि हम एक AddInputModel बना सकें और आर्ग्यूमेंट्स को मान्य कर सकें

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहां हम देखते हैं कि कैसे हम नाम, विवरण और इनपुट स्कीमा Pydantic का उपयोग करके परिभाषित करते हैं और एक हैंडलर जिसे टूल कॉल होने पर बुलाया जाएगा। अंत में, हम `tool_add` को एक्सपोज़ करते हैं जो इन सभी गुणों को रखने वाला एक डिक्शनरी है।

इसके अलावा *schema.py* है जिसका उपयोग हमारे टूल के लिए इनपुट स्कीमा परिभाषित करने में किया जाता है:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

हमें *__init__.py* को भी भरना होगा ताकि tools निर्देशिका को एक मॉड्यूल माना जाए। इसके भीतर की मॉड्यूल को भी इस प्रकार एक्सपोज़ करना होगा:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

जैसे-जैसे हम अधिक टूल जोड़ेंगे हम इस फ़ाइल में जोड़ते रह सकते हैं।

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

यहां हम गुणों का एक डिक्शनरी बनाते हैं:

- name, यह टूल का नाम है।
- rawSchema, यह Zod स्कीमा है, इसका उपयोग आने वाले टूल कॉल अनुरोधों को सत्यापित करने के लिए किया जाएगा।
- inputSchema, इस स्कीमा का उपयोग हैंडलर करेगा।
- callback, इसका उपयोग टूल को invoke करने के लिए किया जाता है।

इसके अलावा `Tool` है जो इस डिक्शनरी को एक प्रकार में परिवर्तित करता है जिसे mcp सर्वर हैंडलर स्वीकार करता है और यह इस प्रकार दिखता है:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

और *schema.ts* है जहां हम प्रत्येक टूल के लिए इनपुट स्कीमा रखते हैं, जो वर्तमान में केवल एक स्कीमा है लेकिन जैसे ही हम टूल जोड़ेंगे अधिक प्रविष्टियां जोड़ सकते हैं:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

बढ़िया, अब हम अपने टूल लिस्टिंग को संभालने के लिए आगे बढ़ते हैं।

### -3- टूल लिस्टिंग संभालना

अब, अपने टूल्स की लिस्टिंग संभालने के लिए, हमें इसके लिए एक अनुरोध हैंडलर सेट करना होगा। इसे अपनी सर्वर फ़ाइल में इस प्रकार जोड़ें:

**Python**

```python
# संक्षिप्तता के लिए कोड को हटा दिया गया है
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

यहाँ, हम डेकोरेटर `@server.list_tools` और कार्यान्वयन फ़ंक्शन `handle_list_tools` जोड़ते हैं। उसमें, हमें टूल्स की एक सूची बनानी होगी। ध्यान दें कि प्रत्येक टूल में नाम, विवरण और inputSchema होना चाहिए।   

**TypeScript**

टूल्स लिस्ट करने के लिए अनुरोध हैंडलर सेट अप करने के लिए, हमें सर्वर पर `setRequestHandler` कॉल करना होगा उस स्कीमा के साथ जो हम करना चाहते हैं, इस मामले में `ListToolsRequestSchema`।

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
// संक्षिप्तता के लिए कोड छोड़ा गया
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // पंजीकृत टूल्स की सूची लौटाएं
  return {
    tools: tools
  };
});
```

बढ़िया, अब हमने टूल्स की लिस्टिंग का काम सुलझा लिया है, आइए देखें कि हम टूल कॉल कैसे कर सकते हैं।

### -4- टूल कॉल संभालना

टूल कॉल करने के लिए, हमें एक और अनुरोध हैंडलर सेट अप करना होगा, जो यह बताता हो कि कौन सा फीचर कॉल करना है और किस तर्क के साथ।

**Python**

चलिए डेकोरेटर `@server.call_tool` का उपयोग करें और इसे `handle_call_tool` जैसी फ़ंक्शन से कार्यान्वित करें। उस फ़ंक्शन में, हमें टूल का नाम, उसके तर्क पार्स करना होगा और यह सुनिश्चित करना होगा कि तर्क टूल के लिए मान्य हैं। हम इस फ़ंक्शन में तर्कों को सत्यापित कर सकते हैं या वास्तविक टूल के भीतर नीचे(validate करवा सकते हैं)।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools एक शब्दकोश है जिसमें टूल नाम कुंजियों के रूप में हैं
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # टूल को चलाएं
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

यहाँ क्या होता है:

- हमारा टूल नाम पहले से इनपुट पैरामीटर `name` के रूप में मौजूद है जो कि `arguments` डिक्शनरी के फ़ॉर्म में हमारे तर्क हैं।

- टूल को `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` के साथ कॉल किया जाता है। तर्कों का सत्यापन `handler` प्रॉपर्टी में होता है जो एक फ़ंक्शन को इंगित करता है, यदि वह असफल होता है तो यह एक अपवाद उठाएगा। 

बस, अब हमारे पास लो-लेवल सर्वर का उपयोग करके टूल लिस्टिंग और कॉल की पूरी समझ है।

पूरा उदाहरण यहाँ देखें: [full example](./code/README.md)

## असाइनमेंट

आपने जो कोड दिया गया है उसे कुछ टूल्स, संसाधन और प्रॉम्प्ट्स के साथ बढ़ाएं और देखें कि आपको केवल tools निर्देशिका में ही फाइलें जोड़नी हैं और कहीं और नहीं।

*कोई समाधान नहीं दिया गया*

## सारांश

इस अध्याय में, हमने देखा कि लो-लेवल सर्वर दृष्टिकोण कैसे काम करता है और यह हमारी वास्तुकला को कितना साफ और संगठित बना सकता है जिसपर हम आगे निर्माण कर सकते हैं। हमने सत्यापन पर भी चर्चा की और आपको दिखाया गया कि कैसे सत्यापन लाइब्रेरीज के साथ स्कीमा बनाकर इनपुट वेलिडेशन काम करता है।

## आगे क्या है

- अगला: [साधारण प्रमाणीकरण](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->