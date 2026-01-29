# प्रगत सर्व्हर वापर

MCP SDK मध्ये दोन प्रकारचे सर्व्हर उपलब्ध आहेत: सामान्य सर्व्हर आणि लो-लेव्हल सर्व्हर. सामान्यतः, तुम्ही नियमित सर्व्हर वापरून त्यामध्ये वैशिष्ट्ये जोडता. परंतु काही विशिष्ट परिस्थितीत तुम्हाला लो-लेव्हल सर्व्हरवर अवलंबून राहावे लागते, जसे की:

- चांगली आर्किटेक्चर. नियमित सर्व्हर आणि लो-लेव्हल सर्व्हर दोन्ही वापरून स्वच्छ आर्किटेक्चर तयार करणे शक्य आहे, परंतु लो-लेव्हल सर्व्हरसह हे थोडे सोपे वाटू शकते.
- वैशिष्ट्य उपलब्धता. काही प्रगत वैशिष्ट्ये फक्त लो-लेव्हल सर्व्हरवर वापरता येतात. पुढील प्रकरणांमध्ये तुम्ही हे पाहाल, जसे की सॅम्पलिंग आणि एलिसिटेशन जोडताना.

## नियमित सर्व्हर विरुद्ध लो-लेव्हल सर्व्हर

नियमित सर्व्हर वापरून MCP सर्व्हर तयार करणे कसे दिसते ते येथे आहे:

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

येथे तुम्ही स्पष्टपणे प्रत्येक टूल, संसाधन किंवा प्रॉम्प्ट जोडता जे तुम्हाला सर्व्हरमध्ये हवे आहे. यात काहीच चुकीचे नाही.

### लो-लेव्हल सर्व्हर दृष्टिकोन

तथापि, लो-लेव्हल सर्व्हर दृष्टिकोन वापरताना तुम्हाला वेगळ्या प्रकारे विचार करावा लागतो. प्रत्येक टूल नोंदवण्याऐवजी, तुम्ही प्रत्येक वैशिष्ट्य प्रकारासाठी (टूल्स, संसाधने किंवा प्रॉम्प्ट्स) दोन हँडलर्स तयार करता. उदाहरणार्थ, टूल्ससाठी फक्त दोन फंक्शन्स असतात:

- सर्व टूल्सची यादी करणे. एक फंक्शन सर्व टूल्स यादी करण्याच्या प्रयत्नांसाठी जबाबदार असेल.
- सर्व टूल्स कॉल करणे. येथे देखील, टूल कॉल करण्यासाठी फक्त एक फंक्शन जबाबदार असेल.

हे कमी काम वाटते ना? त्यामुळे टूल नोंदवण्याऐवजी, मला फक्त हे सुनिश्चित करावे लागेल की टूल सर्व टूल्स यादी करताना दिसते आणि टूल कॉल करण्यासाठी विनंती आल्यावर ते कॉल केले जाते.

आता कोड कसा दिसतो ते पाहूया:

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

येथे आम्ही आता एक फंक्शन तयार करतो जे वैशिष्ट्यांची यादी परत करते. टूल्स यादीतील प्रत्येक एंट्रीमध्ये `name`, `description` आणि `inputSchema` सारखी फील्ड्स असतात जे परत प्रकाराशी जुळतात. यामुळे आम्ही आमची टूल्स आणि वैशिष्ट्ये इतरत्र ठेवू शकतो. आता आम्ही आमची सर्व टूल्स एका टूल्स फोल्डरमध्ये तयार करू शकतो आणि तुमच्या प्रकल्पाचे आयोजन असे करता येते:

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

छान, आमचे आर्किटेक्चर स्वच्छ दिसू शकते.

टूल्स कॉल करणे कसे आहे, तर एक हँडलर टूल कॉल करण्यासाठी, कोणतेही टूल? होय, अगदी तसेच, त्यासाठी कोड येथे आहे:

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

वरील कोडमध्ये तुम्ही पाहू शकता की, आम्हाला कॉल करण्यासाठी टूल आणि त्यासाठी कोणते आर्ग्युमेंट्स वापरायचे आहेत ते पार्स करावे लागते आणि नंतर टूल कॉल करावे लागते.

## दृष्टिकोन सुधारण्यासाठी व्हॅलिडेशन

आतापर्यंत, तुम्ही पाहिले की टूल्स, संसाधने आणि प्रॉम्प्ट्स जोडण्यासाठी तुमच्या सर्व नोंदणींना प्रत्येक वैशिष्ट्य प्रकारासाठी दोन हँडलर्सने कसे बदलता येते. आणखी काय करावे लागेल? आम्ही काही प्रकारचे व्हॅलिडेशन जोडले पाहिजे जेणेकरून टूल योग्य आर्ग्युमेंट्ससह कॉल केले जाईल. प्रत्येक रनटाइमसाठी यासाठी स्वतःचे उपाय आहेत, उदाहरणार्थ Python मध्ये Pydantic वापरले जाते आणि TypeScript मध्ये Zod वापरले जाते. कल्पना अशी आहे की आम्ही खालीलप्रमाणे करतो:

- वैशिष्ट्य (टूल, संसाधन किंवा प्रॉम्प्ट) तयार करण्याचे लॉजिक त्याच्या समर्पित फोल्डरमध्ये हलवा.
- येणाऱ्या विनंतीसाठी व्हॅलिडेशन जोडा, उदाहरणार्थ टूल कॉल करण्यासाठी.

### वैशिष्ट्य तयार करा

वैशिष्ट्य तयार करण्यासाठी, आम्हाला त्या वैशिष्ट्यासाठी एक फाइल तयार करावी लागेल आणि त्या वैशिष्ट्यासाठी आवश्यक फील्ड्स असणे सुनिश्चित करावे लागेल. टूल्स, संसाधने आणि प्रॉम्प्ट्ससाठी फील्ड्स थोडे वेगळे असतात.

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

येथे तुम्ही पाहू शकता की आम्ही खालील गोष्टी कशा करतो:

- *schema.py* फाइलमध्ये Pydantic वापरून `AddInputModel` स्कीमा तयार करतो ज्यामध्ये `a` आणि `b` फील्ड्स असतात.
- येणाऱ्या विनंतीला `AddInputModel` प्रकारात पार्स करण्याचा प्रयत्न करतो, जर पॅरामीटर्समध्ये विसंगती असेल तर हे क्रॅश होईल:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

तुम्ही हे पार्सिंग लॉजिक टूल कॉलमध्ये किंवा हँडलर फंक्शनमध्ये ठेवायचे का ते निवडू शकता.

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

- सर्व टूल कॉल्ससाठी हँडलरमध्ये, आम्ही येणाऱ्या विनंतीला टूलच्या परिभाषित स्कीमामध्ये पार्स करण्याचा प्रयत्न करतो:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    जर ते यशस्वी झाले तर आम्ही प्रत्यक्ष टूल कॉल करण्यास पुढे जातो:

    ```typescript
    const result = await tool.callback(input);
    ```

जसे तुम्ही पाहू शकता, या दृष्टिकोनामुळे एक उत्कृष्ट आर्किटेक्चर तयार होते कारण प्रत्येक गोष्टीचे स्थान निश्चित असते, *server.ts* ही एक अतिशय छोटी फाइल असते जी फक्त विनंती हँडलर्स वायर करते आणि प्रत्येक वैशिष्ट्य त्याच्या संबंधित फोल्डरमध्ये असते म्हणजे टूल्स/, संसाधने/ किंवा /प्रॉम्प्ट्स.

छान, चला पुढे जाऊया आणि हे तयार करण्याचा प्रयत्न करूया.

## व्यायाम: लो-लेव्हल सर्व्हर तयार करणे

या व्यायामात, आम्ही खालील गोष्टी करू:

1. टूल्सची यादी हाताळण्यासाठी आणि टूल्स कॉल करण्यासाठी लो-लेव्हल सर्व्हर तयार करा.
1. तुम्ही तयार करू शकता अशी आर्किटेक्चर अंमलात आणा.
1. तुमचे टूल कॉल योग्य प्रकारे व्हॅलिडेट केले जात आहेत याची खात्री करण्यासाठी व्हॅलिडेशन जोडा.

### -1- आर्किटेक्चर तयार करा

सर्वप्रथम, आम्हाला अशा आर्किटेक्चरला संबोधित करावे लागेल जे आम्ही अधिक वैशिष्ट्ये जोडत असताना स्केल करण्यात मदत करते, ते असे दिसते:

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

आता आम्ही अशा आर्किटेक्चरमध्ये सेट अप केले आहे जे सुनिश्चित करते की आम्ही टूल्स फोल्डरमध्ये सहज नवीन टूल्स जोडू शकतो. संसाधने आणि प्रॉम्प्ट्ससाठी उपडायरेक्टरी जोडण्यासाठी तुम्ही हे अनुसरण करू शकता.

### -2- टूल तयार करणे

पुढे, टूल तयार करणे कसे दिसते ते पाहूया. प्रथम, ते त्याच्या *tool* उपडायरेक्टरीमध्ये तयार केले पाहिजे, असे:

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

येथे आपण पाहतो की आम्ही नाव, वर्णन, Pydantic वापरून इनपुट स्कीमा आणि एक हँडलर परिभाषित करतो जो हे टूल कॉल केल्यावर चालवला जाईल. शेवटी, आम्ही `tool_add` उघड करतो जो या सर्व गुणधर्मांचा समावेश असलेला डिक्शनरी आहे.

तसेच *schema.py* आहे जे आमच्या टूलद्वारे वापरले जाणारे इनपुट स्कीमा परिभाषित करण्यासाठी वापरले जाते:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

आम्हाला *__init__.py* देखील भरावे लागेल जेणेकरून टूल्स डिरेक्टरीला मॉड्यूल म्हणून मानले जाईल. याशिवाय, आम्हाला त्यामधील मॉड्यूल्स उघड करावे लागतील, असे:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

आम्ही अधिक टूल्स जोडत असताना या फाइलमध्ये भर घालू शकतो.

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

येथे आम्ही गुणधर्मांचा समावेश असलेला डिक्शनरी तयार करतो:

- name, हे टूलचे नाव आहे.
- rawSchema, हे Zod स्कीमा आहे, ते येणाऱ्या विनंतीला व्हॅलिडेट करण्यासाठी वापरले जाईल.
- inputSchema, हे स्कीमा हँडलरद्वारे वापरले जाईल.
- callback, हे टूल चालवण्यासाठी वापरले जाते.

तसेच `Tool` आहे जे या डिक्शनरीला प्रकारात रूपांतरित करण्यासाठी वापरले जाते जे MCP सर्व्हर हँडलर स्वीकारू शकतो आणि ते असे दिसते:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

आणि *schema.ts* आहे जिथे आम्ही प्रत्येक टूलसाठी इनपुट स्कीमा संग्रहित करतो, सध्या फक्त एक स्कीमा आहे परंतु आम्ही टूल्स जोडत असताना अधिक एंट्रीज जोडू शकतो:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

छान, पुढे आमच्या टूल्सची यादी हाताळण्याकडे जाऊया.

### -3- टूल्सची यादी हाताळा

पुढे, टूल्सची यादी हाताळण्यासाठी, आम्हाला त्यासाठी विनंती हँडलर सेट अप करावा लागेल. येथे आम्हाला आमच्या सर्व्हर फाइलमध्ये काय जोडावे लागेल:

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

येथे आम्ही `@server.list_tools` डेकोरेटर आणि `handle_list_tools` अंमलात आणणारे फंक्शन जोडतो. नंतरच्या फंक्शनमध्ये, आम्हाला टूल्सची यादी तयार करावी लागते. लक्षात घ्या की प्रत्येक टूलमध्ये नाव, वर्णन आणि inputSchema असणे आवश्यक आहे.

**TypeScript**

टूल्सची यादी सेट करण्यासाठी विनंती हँडलर सेट करण्यासाठी, आम्हाला `ListToolsRequestSchema` शी जुळणाऱ्या स्कीमासह सर्व्हरवर `setRequestHandler` कॉल करावा लागेल.

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

छान, आता आम्ही टूल्सची यादी हाताळण्याचा भाग सोडवला आहे, पुढे टूल्स कॉल कसे करायचे ते पाहूया.

### -4- टूल कॉल करणे हाताळा

टूल कॉल करण्यासाठी, आम्हाला आणखी एक विनंती हँडलर सेट करावा लागेल, यावेळी कोणते वैशिष्ट्य कॉल करायचे आणि कोणत्या आर्ग्युमेंट्ससह हे हाताळण्यासाठी.

**Python**

चला `@server.call_tool` डेकोरेटर वापरूया आणि `handle_call_tool` सारख्या फंक्शनसह अंमलात आणूया. त्या फंक्शनमध्ये, आम्हाला टूलचे नाव, त्याचे आर्ग्युमेंट्स पार्स करावे लागतील आणि त्या टूलसाठी आर्ग्युमेंट्स वैध आहेत याची खात्री करावी लागेल. आम्ही आर्ग्युमेंट्सचे व्हॅलिडेशन या फंक्शनमध्ये किंवा डाउनस्ट्रीम प्रत्यक्ष टूलमध्ये करू शकतो.

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

येथे काय चालते:

- आमचे टूल नाव आधीच इनपुट पॅरामीटर `name` म्हणून उपलब्ध आहे, जे आमच्या आर्ग्युमेंट्ससाठी देखील खरे आहे, `arguments` डिक्शनरीच्या स्वरूपात.

- टूल `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ने कॉल केले जाते. आर्ग्युमेंट्सचे व्हॅलिडेशन `handler` प्रॉपर्टीमध्ये होते जे एका फंक्शनकडे निर्देश करते, जर ते अयशस्वी झाले तर ते अपवाद उभा करेल.

आता आम्हाला लो-लेव्हल सर्व्हर वापरून टूल्सची यादी आणि कॉल करण्याची संपूर्ण समज आहे.

पूर्ण उदाहरण येथे पहा [full example](./code/README.md)

## असाइनमेंट

तुम्हाला दिलेल्या कोडमध्ये अनेक टूल्स, संसाधने आणि प्रॉम्प्ट्स जोडून विस्तारित करा आणि तुम्हाला हे लक्षात येते की तुम्हाला फक्त टूल्स डिरेक्टरीमध्ये फाइल्स जोडाव्या लागतात आणि इतरत्र नाही यावर विचार करा.

*कोणतेही उत्तर दिलेले नाही*

## सारांश

या प्रकरणात, आम्ही लो-लेव्हल सर्व्हर दृष्टिकोन कसा कार्य करतो आणि ते आम्हाला तयार करण्यायोग्य चांगले आर्किटेक्चर तयार करण्यात कसे मदत करू शकते हे पाहिले. आम्ही व्हॅलिडेशनवर चर्चा केली आणि तुम्हाला इनपुट व्हॅलिडेशनसाठी स्कीमा तयार करण्यासाठी व्हॅलिडेशन लायब्ररीसह कसे कार्य करावे हे दाखवले.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.