# प्रगत सर्व्हर वापर

MCP SDK मध्ये दोन वेगवेगळ्या प्रकारचे सर्व्हर उपलब्ध आहेत, तुमचा सामान्य सर्व्हर आणि लो-लेव्हल सर्व्हर. सामान्यतः, तुम्ही नियमित सर्व्हर वापरता तेथे फीचर्स जोडण्यासाठी. काही प्रकरणांमध्ये, तुम्हाला लो-लेव्हल सर्व्हरवर अवलंबून रहायचे असते जसे की:

- चांगली आर्किटेक्चर. नियमित सर्व्हर आणि लो-लेव्हल सर्व्हर यांच्या दोघांसह स्वच्छ आर्किटेक्चर तयार करणे शक्य आहे पण असे म्हणता येईल की लो-लेव्हल सर्व्हर वापरणे थोडे सोपे आहे.
- फीचर उपलब्धता. काही प्रगत फीचर्स फक्त लो-लेव्हल सर्व्हरसह वापरू शकतात.
    नंतरच्या अध्यायांमध्ये Elicitation आणि वारसा Sampling
    वैशिष्ट्य आहे, जे MCP `2026-07-28` मध्ये depreciate केले गेले आहे.

## नियमित सर्व्हर विरुद्ध लो-लेव्हल सर्व्हर

नियमित सर्व्हर वापरल्यास MCP सर्व्हर तयार करणे कसे दिसते ते येथे आहे

**Python**

```python
mcp = FastMCP("Demo")

# एक बेरीज साधन जोडा
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

// एक बेरीज साधन जोडा
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

मुद्दा असा आहे की तुम्ही प्रत्येक टूल, संसाधन किंवा प्रॉम्प्ट स्पष्टपणे सर्व्हरमध्ये जोडता जे तुम्हाला आवश्यक आहे. यात काही चुकीचे नाही.

### लो-लेव्हल सर्व्हर पद्धत

परंतु, जेव्हा तुम्ही लो-लेव्हल सर्व्हर पद्धत वापरता तेव्हा तुम्हाला वेगळ्या प्रकारे विचार करावा लागतो. प्रत्येक टूल नोंदवण्याऐवजी, तुम्ही प्रत्येक फीचर प्रकारासाठी दोन हँडलर्स तयार करता (टूल्स, संसाधने किंवा प्रॉम्प्टसाठी). उदाहरणार्थ टूल्ससाठी फक्त दोन फंक्शन्स असतात:

- सर्व टूल्सची यादी बनवणे. एक फंक्शन सर्व टूल्सची यादी करण्याचा प्रयत्न करेल.
- सर्व टूल्सना कॉल हाताळणे. येथेही, टूलला कॉल करण्यासाठी फक्त एकच फंक्शन आहे.

हे ऐकताच कमी मेहनत वाटते ना? म्हणून, टूल नोंदवण्याऐवजी मला फक्त हे सुनिश्चित करायचं आहे की जेव्हा मी सर्व टूल्सची यादी करतो तेव्हा टूल यादीत असावा आणि जेव्हा टूलला कॉल करण्यासाठी विनंती येते तेव्हा त्याला कॉल केले जावे.

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
  // नोंदणीकृत साधनेची यादी परत करा
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

येथे आता आमच्याकडे ऐसे फंक्शन आहे जे फीचर्सची यादी परत करतो. टूल्सच्या यादीतील प्रत्येक एन्ट्रीमध्ये `name`, `description` आणि `inputSchema` सारखी फील्ड्स आहेत जी रिटर्न टाईपशी सुसंगत आहेत. यामुळे आपण आपल्या टूल्स आणि फीचर डिफिनिशन दुसरीकडे ठेवू शकतो. आता आपण आपल्या सर्व टूल्स एक tools फोल्डरमध्ये तयार करू शकतो आणि तेच तुमच्या सर्व फीचर्ससाठी लागू आहे त्यामुळे तुमचा प्रोजेक्ट अचानक असे संघटित होऊ शकतो:

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

छान आहे, आपली आर्किटेक्चर खूप स्वच्छ दिसू शकते.

टूल कॉल करण्याबद्दल काय, तेच कल्पना का, टूलला कॉल करण्यासाठी एक हँडलर, कोणतेही टूल? होय, अगदी तसेच, त्यासाठीचा कोड असा आहे:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools हे साधनांची नावे की म्हणून असलेले एक शब्दकोश आहे
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
    // TODO टूल कॉल करा,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

वरच्या कोडमधून दिसतंय की, आपल्याला कॉल करायचा टूल आणि कोणते arguments असतील ते पार्स करावे लागतात, आणि नंतर टूल कॉल करावे लागते.

## पडताळणीसह पद्धत सुधारित करणे

आतापर्यंत, तुम्ही पाहिलं की टूल्स, संसाधने आणि प्रॉम्प्ट जोडण्यासाठी सर्व नोंदणी या दोन हँडलर्सने पर्यायी बनू शकतात. अजून काय करायचं आहे? आपल्याला काही प्रकारची पडताळणी जोडावी लागेल, जेणेकरून टूल योग्य arguments सह कॉल होत आहे याची खात्री होईल. प्रत्येक रनटाईमची स्वतःची यासाठी उपाययोजना आहे, उदा. Python मध्ये Pydantic वापरतात आणि TypeScript मध्ये Zod वापरतात. कल्पना अशी की आपण हे पुढीलप्रमाणे करतो:

- फीचर तयार करण्याचा लॉजिक (टूल, संसाधन किंवा प्रॉम्प्ट) त्यांच्या समर्पक फोल्डरमध्ये हलवा.
- उदाहरणार्थ, टूलला कॉल करण्याच्या येणाऱ्या विनंतीची पडताळणी करण्याचा मार्ग जोडा.

### फीचर तयार करा

फीचर तयार करण्यासाठी, आपण त्या फीचरसाठी फाईल तयार करावी लागेल आणि त्याचे आवश्यक फील्डस असावेत. जे फील्ड्स टूल्स, संसाधने आणि प्रॉम्प्ट्समध्ये थोडा फरक असू शकतो.

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
        # Pydantic मॉडेल वापरून इनपुट सत्यापित करा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोडा, जेणेकरून आपण AddInputModel तयार करू शकू आणि args चे सत्यापन करू शकू

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

येथे तुम्ही पाहतो की आपण काय करत आहोत:

- Pydantic `AddInputModel` वापरून स्कीमा तयार करा ज्यात `a` आणि `b` फील्ड्स असतील, फाईल *schema.py* मध्ये.
- येणारी विनंती `AddInputModel` प्रकारात पार्स करण्याचा प्रयत्न करा, जर पॅरामिटर्समध्ये विसंगती असेल तर ही क्रॅश होईल:

   ```python
   # add.py
    try:
        # Pydantic मॉडेल वापरून इनपुट सत्यापित करा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

तुम्ही हे पार्सिंग लॉजिक टूल कॉलमध्येच ठेवू शकता किंवा हँडलर फंक्शनमध्ये.

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

- सर्व टूल कॉल समोरासमोर करणाऱ्या हँडलरमध्ये, आम्ही आता येणारी विनंती टूलच्या डिफाइंड स्कीमामध्ये पार्स करण्याचा प्रयत्न करू:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    जर ते यशस्वी झाले, तर आपण वास्तविक टूल कॉल करण्याकडे पुढे जातो:

    ```typescript
    const result = await tool.callback(input);
    ```

तर तुम्हाला दिसतंय की, ही पद्धत खूप चांगली आर्किटेक्चर तयार करते कारण प्रत्येक गोष्टीस त्याचा ठिकाण असतो, *server.ts* ही एक अतिशय लहान फाईल आहे जी फक्त विनंती हँडलर्सना जोडी लावते आणि प्रत्येक फीचर त्यांच्या संबंधित फोल्डरमध्ये असतो उदा tools/, resources/ किंवा /prompts.

छान आहे, चला पुढे हे पुढील पाऊल उचलूया.

## व्यायाम: लो-लेव्हल सर्व्हर तयार करणे

या व्यायामात, आपण पुढील कार्ये करूया:

1. टूल्सची यादी करणे आणि टूल कॉलिंग हाताळणारा लो-लेव्हल सर्व्हर तयार करणे.
1. एक अशी आर्किटेक्चर राबविणे ज्यावर तुम्ही पुढे बांधकाम करू शकता.
1. तुमच्या टूल कॉलसाठी योग्य पडताळणी याची खात्री करण्यासाठी पडताळणी जोडा.

### -1- आर्किटेक्चर तयार करा

सुरुवातीला आपल्याला अशी आर्किटेक्चर पाहिजे जी जशी आपण अधिक फीचर्स जोडतो तशी स्केल करू शकते, येथे ती कशी दिसते:

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

आता आपण अशी आर्किटेक्चर सेट केली आहे ज्यामुळे आपण सहजपणे tools फोल्डरमध्ये नवीन टूल्स जोडू शकतो. संसाधने आणि प्रॉम्प्टसाठीही सबडिरेक्टरीज जोडण्यासाठी तुम्ही सहज अनुसरू शकता.

### -2- टूल तयार करणे

पुढे आपल्याला टूल तयार करण्याचे काय दिसते ते पाहू. प्रथम, ते त्याच्या *tool* उपडिरेक्टरी मध्ये तयार करावे लागेल असे:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मॉडेल वापरून इनपुटची पडताळणी करा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोडा, जेणेकरून आपण AddInputModel तयार करू शकू आणि args ची पडताळणी करू शकू

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

आपण येथे पाहतो की आपण नाव, वर्णन, आणि इनपुट स्कीमा Pydantic वापरून परिभाषित करत आहोत आणि एक हँडलरही आहे जो टूल कॉल केल्यावर कॉल केला जाईल. शेवटी, आपण `tool_add` एक्सपोज करतो जे सर्व या गुणधर्मांशी संबंधित dictionary आहे.

तसेच *schema.py* ही फाईल आहे जी आपल्या टूलसाठी वापरल्या जाणार्‍या इनपुट स्कीमाला परिभाषित करते:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

आपण *__init__.py* मध्ये देखील भर घालावी लागेल जेणेकरून tools डायरेक्टरीला मॉड्यूल म्हणून गणले जाईल. याशिवाय, त्यातील मॉड्यूल्स आपल्याला बाहेर दाखवावे लागतील असे:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

आपण असे करून अधिक टूल्स जोडत राहू शकतो.

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

येथे आपण गुणधर्मांची dictionary तयार करतो:

- name, टूलचे नाव.
- rawSchema, ही Zod स्कीमा आहे, जी टूल कॉलसंबंधी येणाऱ्या विनंत्यांची पडताळणी करण्यासाठी वापरली जाईल.
- inputSchema, ही स्कीमा हँडलर वापरेल.
- callback, टूलला invoke करण्यासाठी वापरली जाते.

`Tool` नावाचा प्रकारदेखील आहे जो ही dictionary mcp सर्व्हर हँडलर स्वीकारू शकणाऱ्या टाईप मध्ये कन्व्हर्ट करतो, जो असा दिसतो:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

आणि *schema.ts* आहे जिथे आपण प्रत्येक टूलसाठी इनपुट स्कीमा ठेवतो, सध्या फक्त एकच स्कीमा आहे पण टूल्स वाढवले तर अधिक एन्ट्रीज वाढवू शकतो:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

छान आहे, पुढे टूल्सची यादी हाताळूया.

### -3- टूल्सची यादी हाताळा

पुढे, टूल्सची यादी हाताळण्यासाठी, आपल्याला त्यासाठी विनंती हँडलर तयार करायचा आहे. आपल्या सर्व्हर फाइलमध्ये हे जोडा:

**Python**

```python
# संक्षिप्ततेसाठी कोड वगळलेला आहे
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

येथे, आपण `@server.list_tools` डेकोरेटर वापरून `handle_list_tools` नावाने एक फंक्शन तयार करतो. त्यात आपल्याला टूल्सची यादी तयार करावी लागते. प्रत्येक टूलला नाव, वर्णन आणि inputSchema असणे आवश्यक आहे.

**TypeScript**

टूल्सची यादी करावयाची असल्यास, आपण सर्व्हरवर `setRequestHandler` कॉल करतो ज्यात स्कीमा `ListToolsRequestSchema` वापरली जाते.

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
// संक्षिप्ततेसाठी कोड वगळला
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // नोंदणीकृत उपकरणांची यादी परत करा
  return {
    tools: tools
  };
});
```

छान, आता आपण टूल्सची यादीचा भाग सोडवला, पुढे पाहूया टूल कॉल कसं करता येईल.

### -4- टूल कॉल हाताळा

टूल कॉल करण्यासाठी, आपल्याला आणखी एक विनंती हँडलर सेट करायचा आहे, जो कुठला फीचर कॉल करायचा आहे आणि कोणते arguments आहेत याशी संबंधित आहे.

**Python**

आपण `@server.call_tool` डेकोरेटर वापरू आणि `handle_call_tool` नावाने फंक्शन तयार करू. त्या फंक्शनमध्ये, आपण टूल नाव, त्याचा arguments पार्स करतो आणि खात्री करतो की arguments टूलसाठी वैध आहेत. अपघातांपासून argumentsची पडताळणी आपण ह्या फंक्शनमध्ये किंवा टूलमध्ये नंतर करू शकता.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ही साधन नावे की म्हणून वापरून असलेली शब्दकोश आहे
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # साधन कॉल करा
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

येथे जे होते ते:

- आपला टूल नाव इनपुट पॅरामीटर `name` मध्ये आहे आणि arguments `arguments` dictionary मध्ये आहेत.

- टूल कॉल `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ने केला जातो. arguments ची पडताळणी `handler` प्रॉपर्टीत असलेल्या फंक्शनमध्ये होते, जर पडताळणी अयशस्वी झाली तर अपवाद उडतो.

आत्ता आपल्याला लो-लेव्हल सर्व्हर वापरून टूल्सची यादी आणि कॉलिंग यांचा पूर्ण आकलन आहे.

येथे [पूर्ण उदाहरण](./code/README.md) पहा

## असाइनमेंट

दिलेल्या कोडमध्ये अनेक टूल्स, संसाधने आणि प्रॉम्प्ट्स जोडा आणि लक्षात घ्या की तुम्हाला फक्त tools डिरेक्टरीत फाईल्स जोडायच्या आहेत आणि दुसरीत्र कुठेही नाही.

*कोणताही उपाय दिला नाही*

## सारांश

या अध्यायात, आपण पाहिले की लो-लेव्हल सर्व्हर पद्धत कशी काम करते आणि ती आपल्याला एक छान आर्किटेक्चर तयार करण्यात कशी मदत करू शकते ज्यावर आपण पुढे बांधणी करू शकतो. आम्ही पडताळणीबद्दलही चर्चा केली आणि तुम्हाला इनपुट पडताळणीसाठी स्कीमा तयार करण्यासाठी पडताळणी लायब्ररींसह कसे काम करायचे ते दाखवले.

## पुढचे काय

- पुढे: [साधे प्रमाणीकरण](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->