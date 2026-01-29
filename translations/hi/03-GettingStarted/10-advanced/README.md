# उन्नत सर्वर उपयोग

MCP SDK में दो प्रकार के सर्वर उपलब्ध हैं: सामान्य सर्वर और लो-लेवल सर्वर। आमतौर पर, आप सामान्य सर्वर का उपयोग करके उसमें फीचर्स जोड़ते हैं। लेकिन कुछ मामलों में, आपको लो-लेवल सर्वर पर निर्भर रहना पड़ता है, जैसे:

- बेहतर आर्किटेक्चर। सामान्य सर्वर और लो-लेवल सर्वर दोनों के साथ एक साफ-सुथरा आर्किटेक्चर बनाना संभव है, लेकिन यह तर्क दिया जा सकता है कि लो-लेवल सर्वर के साथ यह थोड़ा आसान है।
- फीचर उपलब्धता। कुछ उन्नत फीचर्स केवल लो-लेवल सर्वर के साथ उपयोग किए जा सकते हैं। आप इसे बाद के अध्यायों में देखेंगे जब हम सैंपलिंग और एलिसिटेशन जोड़ेंगे।

## सामान्य सर्वर बनाम लो-लेवल सर्वर

यहां बताया गया है कि MCP सर्वर को सामान्य सर्वर के साथ कैसे बनाया जाता है:

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

इसमें मुख्य बात यह है कि आप स्पष्ट रूप से प्रत्येक टूल, संसाधन या प्रॉम्प्ट जोड़ते हैं जिसे आप सर्वर में शामिल करना चाहते हैं। इसमें कोई समस्या नहीं है।  

### लो-लेवल सर्वर दृष्टिकोण

हालांकि, जब आप लो-लेवल सर्वर दृष्टिकोण का उपयोग करते हैं, तो आपको अलग तरीके से सोचना पड़ता है। यहां, प्रत्येक फीचर प्रकार (टूल्स, संसाधन या प्रॉम्प्ट्स) के लिए दो हैंडलर बनाने की आवश्यकता होती है। उदाहरण के लिए, टूल्स के लिए केवल दो फंक्शन होते हैं, जैसे:

- सभी टूल्स की सूची बनाना। एक फंक्शन सभी टूल्स को सूचीबद्ध करने के प्रयासों के लिए जिम्मेदार होगा।
- सभी टूल्स को कॉल करना। यहां भी, केवल एक फंक्शन टूल को कॉल करने के अनुरोधों को संभालता है।

यह कम काम जैसा लगता है, है ना? तो, टूल को रजिस्टर करने के बजाय, मुझे केवल यह सुनिश्चित करना होगा कि टूल सूची में शामिल हो और जब टूल को कॉल करने का अनुरोध आए तो उसे कॉल किया जाए।

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

यहां हमारे पास एक फंक्शन है जो फीचर्स की सूची लौटाता है। टूल्स सूची में प्रत्येक प्रविष्टि में अब `name`, `description` और `inputSchema` जैसे फील्ड होते हैं ताकि रिटर्न टाइप का पालन किया जा सके। यह हमें हमारे टूल्स और फीचर डिफिनिशन को कहीं और रखने की अनुमति देता है। अब हम अपने सभी टूल्स को एक टूल्स फोल्डर में और सभी फीचर्स को उनके संबंधित फोल्डर में व्यवस्थित कर सकते हैं, जिससे हमारा प्रोजेक्ट इस प्रकार दिख सकता है:

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

यह शानदार है, हमारा आर्किटेक्चर काफी साफ-सुथरा बनाया जा सकता है।

टूल्स को कॉल करने के बारे में क्या, क्या यह भी वही विचार है, एक हैंडलर जो किसी भी टूल को कॉल करता है? हां, बिल्कुल, इसका कोड इस प्रकार है:

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

जैसा कि आप ऊपर दिए गए कोड से देख सकते हैं, हमें कॉल करने के लिए टूल और उसके तर्कों को पार्स करना होगा, और फिर हमें टूल को कॉल करने की प्रक्रिया करनी होगी।

## दृष्टिकोण में सुधार: वैलिडेशन के साथ

अब तक, आपने देखा कि टूल्स, संसाधन और प्रॉम्प्ट्स जोड़ने के लिए आपके सभी रजिस्ट्रेशन को प्रत्येक फीचर प्रकार के लिए इन दो हैंडलर्स से बदला जा सकता है। अब हमें और क्या करना चाहिए? खैर, हमें यह सुनिश्चित करने के लिए कुछ प्रकार का वैलिडेशन जोड़ना चाहिए कि टूल को सही तर्कों के साथ कॉल किया गया है। प्रत्येक रनटाइम का अपना समाधान होता है, उदाहरण के लिए Python में Pydantic और TypeScript में Zod का उपयोग होता है। विचार यह है कि हम निम्नलिखित करें:

- फीचर (टूल, संसाधन या प्रॉम्प्ट) बनाने के लिए लॉजिक को उसके समर्पित फोल्डर में ले जाएं।
- एक तरीका जोड़ें जो आने वाले अनुरोध को मान्य करे, जैसे कि टूल को कॉल करने का अनुरोध।

### फीचर बनाना

फीचर बनाने के लिए, हमें उस फीचर के लिए एक फाइल बनानी होगी और यह सुनिश्चित करना होगा कि उसमें उस फीचर के लिए आवश्यक अनिवार्य फील्ड हों। ये फील्ड टूल्स, संसाधन और प्रॉम्प्ट्स के बीच थोड़े अलग होते हैं।

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

यहां आप देख सकते हैं कि हम निम्नलिखित करते हैं:

- *schema.py* फाइल में Pydantic `AddInputModel` का उपयोग करके `a` और `b` फील्ड के साथ एक स्कीमा बनाते हैं।
- आने वाले अनुरोध को `AddInputModel` प्रकार में पार्स करने का प्रयास करते हैं। यदि पैरामीटर में कोई असमानता है, तो यह क्रैश हो जाएगा:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

आप चुन सकते हैं कि इस पार्सिंग लॉजिक को टूल कॉल में ही रखें या हैंडलर फंक्शन में।

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

- सभी टूल कॉल्स को संभालने वाले हैंडलर में, हम अब आने वाले अनुरोध को टूल के परिभाषित स्कीमा में पार्स करने का प्रयास करते हैं:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    यदि यह काम करता है, तो हम वास्तविक टूल को कॉल करने की प्रक्रिया करते हैं:

    ```typescript
    const result = await tool.callback(input);
    ```

जैसा कि आप देख सकते हैं, यह दृष्टिकोण एक शानदार आर्किटेक्चर बनाता है क्योंकि हर चीज़ का अपना स्थान होता है। *server.ts* एक बहुत छोटी फाइल होती है जो केवल अनुरोध हैंडलर्स को वायर करती है और प्रत्येक फीचर अपने संबंधित फोल्डर में होता है, जैसे tools/, resources/ या /prompts।

शानदार, चलिए इसे बनाने की कोशिश करते हैं।

## अभ्यास: लो-लेवल सर्वर बनाना

इस अभ्यास में, हम निम्नलिखित करेंगे:

1. टूल्स की सूची बनाने और उन्हें कॉल करने के लिए एक लो-लेवल सर्वर बनाएं।
1. एक ऐसा आर्किटेक्चर लागू करें जिसे आप आगे बढ़ा सकें।
1. वैलिडेशन जोड़ें ताकि आपके टूल कॉल्स सही तरीके से मान्य हों।

### -1- एक आर्किटेक्चर बनाएं

पहली चीज़ जो हमें संबोधित करनी है वह एक ऐसा आर्किटेक्चर है जो हमें अधिक फीचर्स जोड़ने के साथ स्केल करने में मदद करता है। यह इस प्रकार दिखता है:

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

अब हमने ऐसा आर्किटेक्चर सेटअप कर लिया है जो सुनिश्चित करता है कि हम आसानी से टूल्स फोल्डर में नए टूल्स जोड़ सकते हैं। संसाधन और प्रॉम्प्ट्स के लिए सबडायरेक्टरी जोड़ने के लिए स्वतंत्र महसूस करें।

### -2- एक टूल बनाना

आइए देखें कि टूल बनाना कैसा दिखता है। सबसे पहले, इसे इसके *tool* सबडायरेक्टरी में बनाया जाना चाहिए, जैसे:

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

यहां हम देखते हैं कि हम नाम, विवरण, Pydantic का उपयोग करके एक इनपुट स्कीमा और एक हैंडलर परिभाषित करते हैं जिसे इस टूल को कॉल करने पर सक्रिय किया जाएगा। अंत में, हम `tool_add` को एक्सपोज़ करते हैं, जो इन सभी गुणों को रखने वाला एक डिक्शनरी है।

इसके अलावा, *schema.py* का उपयोग हमारे टूल द्वारा उपयोग किए जाने वाले इनपुट स्कीमा को परिभाषित करने के लिए किया जाता है:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

हमें *__init__.py* को भी पॉप्युलेट करना होगा ताकि टूल्स डायरेक्टरी को एक मॉड्यूल के रूप में माना जाए। इसके अतिरिक्त, हमें इसके भीतर मॉड्यूल्स को एक्सपोज़ करना होगा, जैसे:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

जैसे-जैसे हम अधिक टूल्स जोड़ते हैं, हम इस फाइल में जोड़ सकते हैं।

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
- rawSchema, यह Zod स्कीमा है, इसका उपयोग आने वाले अनुरोधों को मान्य करने के लिए किया जाएगा।
- inputSchema, इस स्कीमा का उपयोग हैंडलर द्वारा किया जाएगा।
- callback, इसका उपयोग टूल को सक्रिय करने के लिए किया जाएगा।

इसके अलावा `Tool` का उपयोग इस डिक्शनरी को एक प्रकार में बदलने के लिए किया जाता है जिसे MCP सर्वर हैंडलर स्वीकार कर सकता है। यह इस प्रकार दिखता है:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

और *schema.ts* है जहां हम प्रत्येक टूल के लिए इनपुट स्कीमा स्टोर करते हैं। यह वर्तमान में केवल एक स्कीमा के साथ दिखता है, लेकिन जैसे-जैसे हम टूल्स जोड़ते हैं, हम अधिक प्रविष्टियां जोड़ सकते हैं:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

शानदार, चलिए अपने टूल्स की सूची को संभालने के लिए आगे बढ़ते हैं।

### -3- टूल सूची को संभालना

अगला, टूल्स की सूची को संभालने के लिए, हमें इसके लिए एक अनुरोध हैंडलर सेटअप करना होगा। यहां हमें अपने सर्वर फाइल में जोड़ने की आवश्यकता है:

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

यहां हम `@server.list_tools` डेकोरेटर और `handle_list_tools` कार्यान्वयन फंक्शन जोड़ते हैं। बाद वाले में, हमें टूल्स की एक सूची तैयार करनी होती है। ध्यान दें कि प्रत्येक टूल में नाम, विवरण और इनपुट स्कीमा होना चाहिए।   

**TypeScript**

टूल्स की सूची बनाने के लिए अनुरोध हैंडलर सेटअप करने के लिए, हमें `ListToolsRequestSchema` के साथ सर्वर पर `setRequestHandler` कॉल करना होगा।

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

शानदार, अब हमने टूल्स की सूची बनाने का टुकड़ा हल कर लिया है। चलिए देखते हैं कि टूल्स को कॉल करना कैसा दिखता है।

### -4- टूल को कॉल करना संभालना

टूल को कॉल करने के लिए, हमें एक और अनुरोध हैंडलर सेटअप करना होगा, इस बार एक अनुरोध को संभालने पर ध्यान केंद्रित करना होगा जो यह निर्दिष्ट करता है कि किस फीचर को कॉल करना है और किन तर्कों के साथ।

**Python**

आइए `@server.call_tool` डेकोरेटर का उपयोग करें और इसे `handle_call_tool` जैसे फंक्शन के साथ लागू करें। उस फंक्शन के भीतर, हमें टूल का नाम, उसके तर्कों को पार्स करना होगा और यह सुनिश्चित करना होगा कि तर्क उस टूल के लिए मान्य हैं। हम इन तर्कों को इस फंक्शन में या डाउनस्ट्रीम वास्तविक टूल में मान्य कर सकते हैं।

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

यहां क्या होता है:

- हमारे टूल का नाम पहले से ही इनपुट पैरामीटर `name` के रूप में मौजूद है, जो हमारे तर्कों के लिए भी सही है, जो `arguments` डिक्शनरी के रूप में आते हैं।

- टूल को `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` के साथ कॉल किया जाता है। तर्कों का वैलिडेशन `handler` प्रॉपर्टी में होता है जो एक फंक्शन की ओर इशारा करता है। यदि यह विफल होता है, तो यह एक अपवाद उठाएगा। 

अब हमारे पास लो-लेवल सर्वर का उपयोग करके टूल्स की सूची बनाने और उन्हें कॉल करने की पूरी समझ है।

पूरा उदाहरण [यहां देखें](./code/README.md)

## असाइनमेंट

आपको दिए गए कोड को कई टूल्स, संसाधन और प्रॉम्प्ट्स के साथ विस्तारित करें और इस पर विचार करें कि आपने देखा कि आपको केवल टूल्स डायरेक्टरी में फाइलें जोड़ने की आवश्यकता है और कहीं और नहीं। 

*कोई समाधान नहीं दिया गया*

## सारांश

इस अध्याय में, हमने देखा कि लो-लेवल सर्वर दृष्टिकोण कैसे काम करता है और यह हमें एक अच्छा आर्किटेक्चर बनाने में कैसे मदद कर सकता है जिसे हम आगे बढ़ा सकते हैं। हमने वैलिडेशन पर चर्चा की और आपको दिखाया कि इनपुट वैलिडेशन के लिए स्कीमा बनाने के लिए वैलिडेशन लाइब्रेरी के साथ कैसे काम करें।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।