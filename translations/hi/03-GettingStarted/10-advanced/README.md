# उन्नत सर्वर उपयोग

MCP SDK में दो अलग-अलग प्रकार के सर्वर उपलब्ध हैं, आपका सामान्य सर्वर और कम-स्तरीय सर्वर। आम तौर पर, आप इसमें सुविधाएँ जोड़ने के लिए नियमित सर्वर का उपयोग करेंगे। हालांकि कुछ मामलों में, आप कम-स्तरीय सर्वर पर निर्भर रहना चाहते हैं जैसे कि:

- बेहतर वास्तुकला। यह संभव है कि दोनों सामान्य सर्वर और कम-स्तरीय सर्वर के साथ एक साफ़ वास्तुकला बनाई जाए, लेकिन कहा जा सकता है कि यह कम-स्तरीय सर्वर के साथ थोड़ा आसान है।
- सुविधा उपलब्धता। कुछ उन्नत सुविधाएँ केवल कम-स्तरीय सर्वर के साथ ही उपयोग की जा सकती हैं। आप इसे बाद के अध्यायों में देखेंगे जब हम सैंपलिंग और एलिसिटेशन जोड़ेंगे।

## नियमित सर्वर बनाम कम-स्तरीय सर्वर

यहाँ MCP सर्वर बनाने का उदाहरण है सामान्य सर्वर के साथ

**Python**

```python
mcp = FastMCP("Demo")

# एक जोड़ने वाला उपकरण जोड़ें
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

// एक योग टूल जोड़ें
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

मूल बात यह है कि आप स्पष्ट रूप से प्रत्येक टूल, संसाधन या प्रॉम्प्ट जोड़ते हैं जिसे आप सर्वर में रखना चाहते हैं। इसमें कोई दिक्कत नहीं है।  

### कम-स्तरीय सर्वर दृष्टिकोण

हालांकि, जब आप कम-स्तरीय सर्वर दृष्टिकोण का उपयोग करते हैं तो आपको इसे अलग तरह से सोचना होगा। प्रत्येक टूल को पंजीकृत करने के बजाय, आप प्रत्येक फीचर प्रकार (टूल, संसाधन या प्रॉम्प्ट) के लिए दो हैंडलर बनाते हैं। उदाहरण के लिए, टूल के लिए केवल दो फ़ंक्शन होते हैं:

- सभी टूल को सूचीबद्ध करना। एक फ़ंक्शन सभी टूल की सूची बनाने के प्रयासों के लिए जिम्मेदार होगा।
- सभी टूल को कॉल करना। यहाँ भी, केवल एक फ़ंक्शन टूल को कॉल करने के लिए अनुरोधों को संभालता है।

यह संभावित रूप से कम काम लग रहा है, है ना? इसलिए टूल पंजीकृत करने के बजाय, मुझे बस यह सुनिश्चित करना है कि टूल सभी टूल सूची में सूचीबद्ध हो और जब टूल को कॉल करने का अनुरोध आए तो वह बुलाया जाए। 

आईए देखें कि अब कोड कैसा दिखता है:

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

यहाँ हमारे पास एक फ़ंक्शन है जो फीचर्स की सूची लौटाता है। टूल्स सूची के प्रत्येक प्रविष्टि में अब `name`, `description` और `inputSchema` जैसे फ़ील्ड होते हैं ताकि रिटर्न टाइप का पालन हो। यह हमें हमारे टूल्स और फीचर परिभाषा को कहीं और रखने में सक्षम बनाता है। अब हम अपने सभी टूल्स को एक tools फोल्डर में बना सकते हैं और यही बात आपके सभी फीचर्स के लिए लागू होती है, ताकि आपका प्रोजेक्ट इस तरह व्यवस्थित हो सके:

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

यह बढ़िया है, हमारी वास्तुकला काफी साफ़-सुथरी दिखाई दे सकती है।

टूल्स को कॉल करने का क्या, क्या यही विचार है, एक हैंडलर किसी भी टूल को कॉल करने के लिए? हाँ, बिल्कुल, यहाँ इसका कोड है:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # टूल्स एक शब्दकोश है जिसमें टूल नाम कुंजी के रूप में होते हैं
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
    // TODO उपकरण को कॉल करें,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

जैसा कि आप ऊपर के कोड से देख सकते हैं, हमें कॉल किए जाने वाले टूल और उसपर दिए गए तर्कों को पार्स करना होता है, उसके बाद टूल को कॉल करना होता है।

## मान्यता (वैलिडेशन) के साथ दृष्टिकोण में सुधार

अब तक, आपने देखा कि टूल्स, संसाधन और प्रॉम्प्ट जोड़ने के लिए आपकी सभी पंजीकरण इस तरह प्रत्येक फीचर प्रकार के दो हैंडलर से बदली जा सकती हैं। अब हमें और क्या करने की जरूरत है? खैर, हमें कुछ प्रकार की वैलिडेशन जोड़नी चाहिए ताकि यह सुनिश्चित हो सके कि टूल सही तर्कों के साथ कॉल किया गया है। प्रत्येक रनटाइम के पास इसके लिए अपने समाधान होते हैं, उदाहरण के लिए Python में Pydantic और TypeScript में Zod का उपयोग होता है। विचार यह है कि हम निम्न करें:

- एक फीचर (टूल, संसाधन या प्रॉम्प्ट) बनाने के लॉजिक को उसके समर्पित फ़ोल्डर में ले जाएं।
- आने वाले अनुरोध को वैलिडेट करने का तरीका जोड़ें जो उदाहरण के लिए टूल कॉल करने के लिए हो।

### एक फीचर बनाएं

फीचर बनाने के लिए, हमें उस फीचर के लिए एक फ़ाइल बनानी होगी और यह सुनिश्चित करना होगा कि उसमें उस फीचर के लिए आवश्यक अनिवार्य फ़ील्ड हों। टूल, संसाधन और प्रॉम्प्ट में ये फ़ील्ड थोड़े भिन्न होते हैं।

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
        # Pydantic मॉडल का उपयोग करके इनपुट सत्यापित करें
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोड़ें, ताकि हम AddInputModel बना सकें और args को सत्यापित कर सकें

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

यहाँ आप देख सकते हैं कि हम निम्न करते हैं:

- Pydantic `AddInputModel` का उपयोग करके एक स्कीमा बनाना जिसमें फ़ील्ड `a` और `b` हैं फ़ाइल *schema.py* में।
- आने वाले अनुरोध को `AddInputModel` प्रकार में पार्स करने का प्रयास करते हैं, यदि पैरामीटर में मेल नहीं है तो यह क्रैश हो जाएगा:

   ```python
   # add.py
    try:
        # Pydantic मॉडल का उपयोग करके इनपुट मान्य करें
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

आप चुन सकते हैं कि इस पार्सिंग लॉजिक को टूल कॉल में ही रखें या हैंडलर फ़ंक्शन में।

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

- सभी टूल कॉल संभालने वाले हैंडलर में, हम अब आने वाले अनुरोध को टूल के परिभाषित स्कीमा में पार्स करने का प्रयास करते हैं:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    यदि यह काम करता है तो हम वास्तविक टूल को कॉल करते हैं:

    ```typescript
    const result = await tool.callback(input);
    ```

जैसा कि आप देख सकते हैं, यह दृष्टिकोण एक अच्छी वास्तुकला बनाता है क्योंकि हर चीज़ का अपना स्थान होता है, *server.ts* एक बहुत छोटी फ़ाइल है जो केवल अनुरोध हैंडलरों को जोड़ती है और प्रत्येक फीचर अपने-अपने फ़ोल्डर में होता है यानी tools/, resources/ या /prompts।

बहुत अच्छा, चलिए इसे अगले चरण में बनाते हैं।

## अभ्यास: एक कम-स्तरीय सर्वर बनाना

इस अभ्यास में, हम निम्न करेंगे:

1. टूल्स की सूची बनाने और टूल्स को कॉल करने वाले कम-स्तरीय सर्वर को संभालना।
1. ऐसी वास्तुकला लागू करना जिस पर आप निर्माण कर सकें।
1. यह सुनिश्चित करने के लिए मान्यता जोड़ना कि आपके टूल कॉल सही ढंग से वैलिडेटेड हों।

### -1- एक वास्तुकला बनाएं

पहली बात जो हमें संबोधित करनी है वह ऐसी वास्तुकला है जो हमें अधिक फीचर्स जोड़ते समय मापनीयता (स्केल) में मदद करे, यह इस प्रकार दिखती है:

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

अब हमने एक ऐसी वास्तुकला सेटअप की है जो सुनिश्चित करती है कि हम आसानी से tools फोल्डर में नए टूल जोड़ सकें। संसाधन (resources) और प्रॉम्प्ट (prompts) के लिए सबडायरेक्टरी जोड़ने के लिए स्वतंत्र महसूस करें।

### -2- एक टूल बनाना

आइए देखें कि टूल बनाना कैसा दिखता है। सबसे पहले, इसे *tool* उपनिर्देशिका में इस तरह बनाया जाना चाहिए:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मॉडल का उपयोग करके इनपुट को मान्य करें
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

यहाँ हम देखते हैं कि कैसे हम नाम, विवरण और इनपुट स्कीमा को Pydantic का उपयोग करते हुए परिभाषित करते हैं और एक हैंडलर जो तब बुलाया जाएगा जब यह टूल कॉल किया जाएगा। अंत में, हम `tool_add` को एक्सपोज़ करते हैं जो इन सभी गुणों को रखता है।

साथ ही *schema.py* भी है जिसका उपयोग हमारे टूल के इनपुट स्कीमा को परिभाषित करने के लिए किया जाता है:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

हमें *__init__.py* फ़ाइल को भी भरना होगा ताकि tools निर्देशिका को एक मॉड्यूल माना जाए। इसके अलावा, हमें उसके भीतर के मॉड्यूल्स को इस तरह से एक्सपोज़ करना होगा:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

जैसे-जैसे हम अधिक टूल जोड़ते जाएंगे, हम इस फ़ाइल में अधिक जोड़ सकते हैं।

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

यहाँ हम एक डिक्शनरी बनाते हैं जिसमें गुण होते हैं:

- name, यह टूल का नाम है।
- rawSchema, यह Zod स्कीमा है, इसका उपयोग इस टूल को कॉल करने वाले आने वाले अनुरोधों को वैलिडेट करने के लिए किया जाएगा।
- inputSchema, यह स्कीमा हैंडलर द्वारा उपयोग किया जाएगा।
- callback, इसका उपयोग टूल को invoke करने के लिए किया जाता है।

साथ ही `Tool` भी है जो इस डिक्शनरी को उस प्रकार में बदलने के लिए उपयोग होता है जिसे mcp सर्वर हैंडलर स्वीकार कर सकता है और इसका स्वरूप इस प्रकार है:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

और *schema.ts* भी है जहाँ हम प्रत्येक टूल के लिए इनपुट स्कीमाइन रखते हैं, अभी एक ही स्कीमा है लेकिन जैसे-जैसे टूल बढ़ेंगे हम इसमें अधिक प्रविष्टियां जोड़ सकते हैं:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

बहुत बढ़िया, अब टूल की सूची संभालने के लिए आगे बढ़ते हैं।

### -3- टूल की सूची संभालना

अगला, टूल की सूची संभालने के लिए, हमें इसके लिए एक अनुरोध हैंडलर सेटअप करना होगा। इसे सर्वर फ़ाइल में जोड़ना होगा:

**Python**

```python
# संक्षिप्तता के लिए कोड छांटा गया है
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

यहाँ, हम डेकोरेटर `@server.list_tools` जोड़ते हैं और कार्यान्वयन फ़ंक्शन `handle_list_tools` बनाते हैं। बाद वाले में, हमें टूल्स की एक सूची बनानी होती है। ध्यान दें कि प्रत्येक टूल के पास नाम, विवरण और inputSchema होना चाहिए।   

**TypeScript**

टूल सूची बनाने के लिए अनुरोध हैंडलर सेटअप करने के लिए, हमें सर्वर पर `setRequestHandler` कॉल करना होता है जो उस स्कीमा के अनुकूल हो जो हम करना चाहते हैं, इस मामले में `ListToolsRequestSchema`।

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
// संक्षिप्तता के लिए कोड छोड़ दिया गया है
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // पंजीकृत उपकरणों की सूची लौटाएं
  return {
    tools: tools
  };
});
```

अच्छा, अब हमने टूल की सूची बनाने का हिस्सा हल कर लिया है, आइए देखें कि टूल्स कॉल करना कैसे किया जा सकता है।

### -4- टूल कॉल को संभालना

टूल को कॉल करने के लिए, हमें एक और अनुरोध हैंडलर सेटअप करना होगा, इस बार एक ऐसे अनुरोध को संभालने के लिए जो बताता है कि कौन सा फीचर कॉल करना है और किन तर्कों के साथ।

**Python**

आइए डेकोरेटर `@server.call_tool` का उपयोग करें और इसे `handle_call_tool` जैसा फ़ंक्शन बनाएं। उस फ़ंक्शन के भीतर, हमें टूल नाम, इसके आर्गुमेंट को पार्स करना होता है और सुनिश्चित करना होता है कि तर्क उस टूल के लिए वैध हैं। हम या तो तर्कों को इस फ़ंक्शन में वैलिडेट कर सकते हैं या वास्तविक टूल में नीचे।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools एक शब्दकोश है जिसमें टूल नाम कुंजियाँ हैं
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

- हमारा टूल नाम पहले से ही इनपुट पैरामीटर `name` के रूप में मौजूद है जो `arguments` डिक्शनरी के रूप में हमारे आर्गुमेंट हैं।

- टूल को `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` के साथ कॉल किया जाता है। तर्कों की वैधता `handler` प्रॉपर्टी में होती है जो एक फ़ंक्शन की ओर इशारा करती है, यदि वह विफल होती है तो यह अपवाद फेंकेगा। 

तो, अब हमें कम-स्तरीय सर्वर का उपयोग करके टूल की सूची बनाने और कॉल करने की पूरी समझ हो गई है।

पूर्ण उदाहरण देखें: [full example](./code/README.md)

## असाइनमेंट

आपको दिया गया कोड बढ़ाएँ जिसमें कई टूल, संसाधन और प्रॉम्प्ट हों और यह समझें कि आपको केवल tools निर्देशिका में फाइलें जोड़नी होती हैं और कहीं और नहीं।

*कोई समाधान नहीं दिया गया*

## सारांश

इस अध्याय में, हमने देखा कि कम-स्तरीय सर्वर दृष्टिकोण कैसे काम करता है और यह हमें एक अच्छी वास्तुकला बनाने में कैसे मदद कर सकता है जिस पर हम लगातार निर्माण कर सकते हैं। हमने मान्यता पर भी चर्चा की और आपको दिखाया गया कि इनपुट मान्यता के लिए स्कीमाएँ बनाने के लिए मान्यता लाइब्रेरियों के साथ कैसे काम करें।

## अगले कदम

- अगला: [सरल प्रमाणीकरण](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या गलतियां हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्याओं के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->