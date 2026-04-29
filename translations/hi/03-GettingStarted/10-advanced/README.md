# उन्नत सर्वर उपयोग

MCP SDK में दो अलग-अलग प्रकार के सर्वर उपलब्ध हैं, आपका सामान्य सर्वर और निम्न-स्तरीय सर्वर। सामान्यतः, आप इसमें फीचर्स जोड़ने के लिए नियमित सर्वर का उपयोग करेंगे। कुछ मामलों में, आप निम्न-स्तरीय सर्वर पर निर्भर करना चाहते हैं जैसे:

- बेहतर वास्तुकला। दोनों नियमित सर्वर और निम्न-स्तरीय सर्वर के साथ एक साफ-सुथरी वास्तुकला बनाना संभव है, लेकिन कहा जा सकता है कि निम्न-स्तरीय सर्वर के साथ यह थोड़ा आसान होता है।
- फीचर उपलब्धता। कुछ उन्नत फीचर्स केवल निम्न-स्तरीय सर्वर के साथ ही उपयोग किए जा सकते हैं। आप इसे बाद के अध्यायों में देखेंगे जैसे हम सैम्पलिंग और एलीसिटेशन जोड़ते हैं।

## नियमित सर्वर बनाम निम्न-स्तरीय सर्वर

यहाँ नियमित सर्वर के साथ MCP सर्वर बनाने का तरीका है

**Python**

```python
mcp = FastMCP("Demo")

# एक जोड़ उपकरण जोड़ें
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

बात यह है कि आप स्पष्ट रूप से प्रत्येक टूल, संसाधन या प्रॉम्प्ट जोड़ते हैं जिसे आप चाहते हैं कि सर्वर के पास हो। इसमें कोई गलती नहीं है।

### निम्न-स्तरीय सर्वर दृष्टिकोण

हालांकि, जब आप निम्न-स्तरीय सर्वर दृष्टिकोण का उपयोग करते हैं तो आपको इसे अलग तरीके से सोचना होगा। प्रत्येक टूल को रजिस्टर करने के बजाय, आप फीचर प्रकार (टूल, संसाधन या प्रॉम्प्ट) के लिए दो हैंडलर बनाते हैं। उदाहरण के लिए टूल्स के लिए केवल दो फ़ंक्शन होंगे:

- सभी टूल्स की सूची बनाना। एक फ़ंक्शन सभी टूल्स की सूचि दिखाने की कोशिशों के लिए जिम्मेदार होगा।
- सभी टूल्स को कॉल करना। यहाँ भी, केवल एक फ़ंक्शन टूल कॉल्स को संभालेगा।

यह सुनने में कम काम की तरह लगता है न? इसलिए टूल को रजिस्टर करने के बजाय, मुझे केवल यह सुनिश्चित करना है कि जब मैं सभी टूल्स की सूची बनाऊँ, तब ये सूचीबद्ध हो, और जब टूल कॉल करने का अनुरोध आए तो यह कॉल हो।

आइए देखें कि कोड अब कैसा दिखता है:

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
  // पंजीकृत उपकरणों की सूची लौटाएं
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

अब हमारे पास एक फ़ंक्शन है जो फीचर्स की सूची लौटाता है। टूल्स सूची के प्रत्येक प्रविष्टि में अब `name`, `description` और `inputSchema` जैसे फ़ील्ड्स होते हैं जो रिटर्न टाइप का पालन करते हैं। इससे हमें टूल्स और फीचर परिभाषा कहीं और रखने की अनुमति मिलती है। हम अब अपने सभी टूल्स को एक टूल्स फ़ोल्डर में बना सकते हैं और यही आपके सभी फीचर्स के लिए भी संभव है, ताकि आपका प्रोजेक्ट इस तरह व्यवस्थित हो सके:

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

यह शानदार है, हमारी वास्तुकला साफ-सुथरी दिखाई दे सकती है।

टूल कॉल करने का क्या? क्या यह भी वही विचार है, एक हैंडलर जो किसी भी टूल को कॉल करे? हाँ, बिल्कुल, यहाँ इसका कोड है:

**Python**

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
    
    // तर्क: request.params.arguments
    // TODO उपकरण को कॉल करें,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ऊपर के कोड से आप देख सकते हैं, हमें टूल को कॉल करना है और कौन-से आर्गुमेंट्स के साथ, यह पार्स करना होगा, फिर टूल को कॉल करना होगा।

## वेरीफ़िकेशन के साथ दृष्टिकोण में सुधार

अब तक, आपने देखा कि टूल्स, संसाधन और प्रॉम्प्ट जोड़ने के लिए आपकी सभी रजिस्ट्रेशन को प्रत्येक फीचर प्रकार के लिए केवल दो हैंडलरों से कैसे बदला जा सकता है। हमें और क्या करना है? हमें कुछ प्रकार के वेरीफ़िकेशन जोड़ने चाहिए यह सुनिश्चित करने के लिए कि टूल सही आर्गुमेंट्स के साथ कॉल किया गया है। प्रत्येक रनटाइम का अपना समाधान होता है, उदाहरण के लिए Python Pydantic का उपयोग करता है और TypeScript Zod का। विचार यह है कि हम निम्न करें:

- फीचर (टूल, संसाधन या प्रॉम्प्ट) बनाने की लॉजिक को इसके समर्पित फ़ोल्डर में ले जाएं।
- किसी अनुरोध को Validate करने का तरीका जोड़ें, जैसे कि टूल कॉल करने के लिए अनुरोध।

### एक फीचर बनाएं

फीचर बनाने के लिए, हमें उस फीचर के लिए एक फ़ाइल बनानी होगी और यह सुनिश्चित करना होगा कि इसमें उस फीचर के लिए आवश्यक अनिवार्य फ़ील्ड्स हों। टूल्स, संसाधन और प्रॉम्प्ट में फ़ील्ड्स थोड़े अलग होते हैं।

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
        # Pydantic मॉडल का उपयोग करके इनपुट मान्य करें
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोड़ें, ताकि हम एक AddInputModel बना सकें और args को मान्य कर सकें

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ आप देख सकते हैं हम निम्न कार्य करते हैं:

- `schema.py` फ़ाइल में Pydantic `AddInputModel` का उपयोग करते हुए एक स्कीमा बनाना जिसमें `a` और `b` फ़ील्ड्स हैं।
- आने वाले अनुरोध को `AddInputModel` के प्रकार में पार्स करने का प्रयास करना, अगर पैरामीटर मेल नहीं खाते तो यह क्रैश करेगा:

   ```python
   # add.py
    try:
        # इनपुट को Pydantic मॉडल का उपयोग करके मान्य करें
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

आप इस पार्सिंग लॉजिक को टूल कॉल के अंदर या हैंडलर फ़ंक्शन में डाल सकते हैं।

**TypeScript**

```typescript
// सर्वर.ts
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

       // @ts-नज़रअंदाज़
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

// जोड़ें.ts
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

- सभी टूल कॉल्स को संभालने वाले हैंडलर में, हम अब इनकमिंग अनुरोध को टूल के परिभाषित स्कीमा में पार्स करने की कोशिश करते हैं:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    अगर यह काम करता है तो हम असली टूल को कॉल करने बढ़ते हैं:

    ```typescript
    const result = await tool.callback(input);
    ```

जैसा कि आप देख सकते हैं, यह दृष्टिकोण एक बेहतरीन वास्तुकला बनाता है क्योंकि हर चीज़ का अपना स्थान होता है, *server.ts* एक बहुत छोटी फ़ाइल है जो केवल रिक्वेस्ट हैंडलर सेट करती है और प्रत्येक फीचर अपने-अपने फ़ोल्डर में होता है जैसे tools/, resources/ या prompts/।

बहुत अच्छा, आइए इसे बनाने की कोशिश करें।

## अभ्यास: एक निम्न-स्तरीय सर्वर बनाना

इस अभ्यास में, हम निम्न करेंगे:

1. टूल्स की लिस्टिंग और कॉलिंग को संभालने वाला निम्न-स्तरीय सर्वर बनाएंगे।
2. एक ऐसी वास्तुकला लागू करेंगे जिस पर आप आगे निर्माण कर सकें।
3. यह सुनिश्चित करने के लिए वैलिडेशन जोड़ेंगे कि आपके टूल कॉल सही ढंग से वैलिडेट होते हैं।

### -1- एक वास्तुकला बनाएं

सबसे पहले हमें ऐसी वास्तुकला बनानी है जो अधिक फीचर्स जोड़ने पर स्केल में मदद करे, यह कुछ ऐसा दिखता है:

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

अब हमने एक ऐसी वास्तुकला सेट की है जो सुनिश्चित करती है कि हम टूल्स को टूल्स फ़ोल्डर में आसानी से जोड़ सकते हैं। संसाधन और प्रॉम्प्ट के लिए सबडायरेक्टरीज़ जोड़ने के लिए इसे फॉलो करें।

### -2- एक टूल बनाना

आइए देखें कि टूल बनाने का अगला कदम क्या है। सबसे पहले, इसे अपने *tool* सबडायरेक्टरी में बनाना होता है, इस तरह:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मॉडल का उपयोग करके इनपुट मान्य करें
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोड़ें, ताकि हम एक AddInputModel बना सकें और आर्ग्स को मान्य कर सकें

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ आप देख सकते हैं कि हम नाम, विवरण और इनपुट स्कीमा को Pydantic के साथ कैसे परिभाषित करते हैं और एक हैंडलर जो तब कॉल किया जाएगा जब यह टूल कॉल होगा। अंत में, हम `tool_add` एक्सपोज़ करते हैं जो इन सभी प्रॉपर्टीज़ को होल्ड करता है।

इसके साथ एक *schema.py* फ़ाइल है जो टूल के इनपुट स्कीमा को परिभाषित करती है:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

हमें *__init__.py* भी भरना होगा ताकि tools डायरेक्टरी को एक मॉड्यूल माना जाए। साथ ही, मॉड्यूल्स को इस तरह से एक्सपोज़ करें:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

जैसे-जैसे आप और टूल्स जोड़ेंगे, आप इस फाइल को अपडेट कर सकते हैं।

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

यहाँ हम एक dictionary बनाते हैं जिसमें प्रॉपर्टीज़ होती हैं:

- name, यह टूल का नाम है।
- rawSchema, यह Zod स्कीमा है, जो इस टूल को कॉल करने वाले आने वाले अनुरोधों को वैलिडेट करने के लिए उपयोग होगा।
- inputSchema, यह स्कीमा हैंडलर द्वारा उपयोग होगा।
- callback, यह टूल को invoke करने के लिए प्रयोग होता है।

साथ में `Tool` भी है जो इस dictionary को एक प्रकार में कन्वर्ट करता है जिसे mcp सर्वर हैंडलर स्वीकार कर सकता है, यह कुछ इस तरह दिखता है:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

और एक *schema.ts* है जहां हम हर टूल के लिए इनपुट स्कीमा रखते हैं, फिलहाल इसमें केवल एक स्कीमा है, लेकिन जैसे-जैसे आपके टूल्स बढ़ेंगे, और एंट्रीज़ जोड़ सकते हैं:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

बहुत अच्छा, अब आइए अपने टूल्स की लिस्टिंग को संभालते हैं।

### -3- टूल लिस्टिंग को संभालना

अब, टूल्स की लिस्टिंग को संभालने के लिए, हमें इसके लिए एक रिक्वेस्ट हैंडलर सेट करना होगा। इसे अपने सर्वर फाइल में इस तरह जोड़ना होगा:

**Python**

```python
# संक्षिप्तता के लिए कोड छोड़ा गया है
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

यहाँ, हम डेकोरेटर `@server.list_tools` और फ़ंक्शन `handle_list_tools` जोड़ते हैं। इस फ़ंक्शन में हम टूल्स की सूची बनानी होती है। ध्यान दें कि प्रत्येक टूल का नाम, विवरण और inputSchema होना चाहिए। 

**TypeScript**

टूल्स की लिस्टिंग के लिए रिक्वेस्ट हैंडलर सेट करने के लिए, हमें `setRequestHandler` को सर्वर पर कॉल करना है और एक स्कीमा प्रदान करना है जो हमारे काम के अनुकूल हो, इस मामले में `ListToolsRequestSchema`।

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

बहुत अच्छा, अब हमने टूल्स की लिस्टिंग का हिस्सा हल कर लिया है, चलिए देखते हैं कि टूल कॉलिंग कैसे हो सकती है।

### -4- टूल कॉल को संभालना

टूल कॉल करने के लिए, हमें एक और रिक्वेस्ट हैंडलर सेट करना होगा, जो किसी रिक्वेस्ट को संभालता है जिसमें बताया जाता है कि किस फीचर को कॉल करना है और किस आर्गुमेंट्स के साथ।

**Python**

आइए डेकोरेटर `@server.call_tool` का उपयोग करें और उसे `handle_call_tool` नामक फ़ंक्शन से लागू करें। इस फ़ंक्शन के अंदर, हमें टूल का नाम, इसके आर्गुमेंट्स पार्स करने होंगे और सुनिश्चित करना होगा कि आर्गुमेंट्स उस टूल के लिए वैध हैं। हम आर्गुमेंट्स को इस फ़ंक्शन में या टूल के अंदर वैलिडेट कर सकते हैं।

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
        # टूल को कॉल करें
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

यहाँ क्या होता है:

- हमारा टूल नाम इनपुट पैरामीटर `name` के रूप में पहले से मौजूद होता है और आर्गुमेंट्स `arguments` डिक्शनरी के रूप में हैं।

- टूल को `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` के साथ कॉल किया जाता है। आर्गुमेंट्स की वैलिडेशन `handler` प्रॉपर्टी में होती है जो एक फ़ंक्शन पॉइंटर है, अगर यह विफल होता है, तो यह अपवाद उठाएगा।

बिल्कुल, अब हमारे पास निम्न-स्तरीय सर्वर का उपयोग करके टूल्स लिस्टिंग और कॉलिंग को पूरी तरह समझने का अवसर है।

पूरा उदाहरण यहां देखें: [full example](./code/README.md)

## असाइनमेंट

जो कोड आपको दिया गया है उसमें कई टूल्स, संसाधन और प्रॉम्प्ट जोड़ें और देखें कि आपको केवल tools डायरेक्टरी में फाइलें जोड़नी होती हैं और कहीं और नहीं।

*कोई समाधान नहीं दिया गया*

## सारांश

इस अध्याय में, हमने देखा कि निम्न-स्तरीय सर्वर दृष्टिकोण कैसे काम करता है और यह हमें एक अच्छी वास्तुकला बनाने में कैसे मदद करता है जिस पर हम आगे निर्माण कर सकते हैं। हमने वैलिडेशन पर भी चर्चा की और आपको दिखाया गया कि वैलिडेशन लाइब्रेरीज के साथ इनपुट स्कीमा कैसे बनाया जाता है।

## आगे क्या है

- अगला: [सरल प्रमाणीकरण](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, उसे प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->