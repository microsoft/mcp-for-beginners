# प्रगत सर्व्हर वापर

MCP SDK मध्ये दोन वेगळ्या प्रकारचे सर्व्हर उघडलेले आहेत, तुमचा सामान्य सर्व्हर आणि लो-लेव्हल सर्व्हर. सामान्यतः, तुम्ही त्यात वैशिष्ट्ये जोडण्यासाठी नियमित सर्व्हर वापराल. मात्र काही बाबतीत, तुम्हाला लो-लेव्हल सर्व्हर वापरण्याचा आधार घ्यावा लागतो, जसे:

- चांगली आर्किटेक्चर. नियमित सर्व्हर आणि लो-लेव्हल सर्व्हर दोन्ही वापरून स्वच्छ आर्किटेक्चर तयार करणे शक्य आहे परंतु लो-लेव्हल सर्व्हर वापरून ते थोडे सोपे सांगितले जाऊ शकते.
- वैशिष्ट्य उपलब्धता. काही प्रगत वैशिष्ट्ये फक्त लो-लेव्हल सर्व्हरसह वापरता येतात. तुम्हाला हे पुढील प्रकरणांमध्ये दिसेल जसे आपण सॅम्पलिंग आणि एलिसिटेशन जोडतो.

## नियमित सर्व्हर विरुद्ध लो-लेव्हल सर्व्हर

येथे नियमित सर्व्हरसह MCP सर्व्हर तयार करण्याचे कसे दिसते:

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

हा मुद्दा असा आहे की तुम्ही स्पष्टपणे प्रत्येक साधन, संसाधन किंवा प्रॉम्प्ट जो सर्व्हरमध्ये हवा आहे तो जोडता. यात काही गैर नाही.

### लो-लेव्हल सर्व्हर दृष्टिकोन

तथापि, जेव्हा तुम्ही लो-लेव्हल सर्व्हर दृष्टिकोन वापरता तेव्हा तुम्हाला वेगळ्या प्रकारे विचार करावा लागतो. प्रत्येक साधन नोंदवण्याऐवजी, तुम्ही प्रत्येक वैशिष्ट्य प्रकारासाठी (साधने, संसाधने किंवा प्रॉम्प्ट) दोन हँडलर तयार करता. उदाहरणार्थ साधनांसाठी केवळ दोन फंक्शन्स असतात:

- सर्व साधने सूचीबद्ध करणे. एक फंक्शन सर्व साधनांच्या सूचीकरणासाठी जबाबदार असते.
- सर्व साधने कॉल करणे. येथेही, केवळ एक फंक्शन आहे जे साधन कॉलिंग हँडल करते.

हे कमी काम वाटते नाही का? त्यामुळे साधन नोंदवण्याऐवजी, जेव्हा सर्व साधने सूचीबद्ध करतो तेव्हा ते साधन यादीत आहे याची खात्री करण्याची गरज आहे आणि जेव्हा कॉलसाठी विनंती येते तेव्हा ते कॉल केले जाते.

आता बघूया कोड कसा दिसतो:

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
  // नोंदणीकृत साधनांची यादी परत करा
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

येथे आता आपल्याला वैशिष्ट्यांची यादी परत करणारे एक फंक्शन आहे. साधनांच्या यादीतील प्रत्येक नोंदीमध्ये `name`, `description` आणि `inputSchema` सारखे फील्ड्स असतात जे परतावा प्रकाराचे पालन करतात. त्यामुळे आपण आपली साधने आणि वैशिष्ट्य व्याख्या दुसऱ्या ठिकाणी ठेवू शकतो. आता आपण सर्व साधने tools फोल्डरमध्ये तयार करू शकतो आणि तसचं तुमच्या सर्व वैशिष्ट्यांसाठी देखील, ज्यामुळे तुमचा प्रोजेक्ट अशाप्रकारे संघटित होऊ शकतो:

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

हे छान आहे, आपली आर्किटेक्चर व्यवस्थित दिसू शकते.

आता साधने कॉल करण्याबाबत काय, तोही एकच कल्पना, प्रत्येक साधन कॉलसाठी एक हँडलर? होय, अगदी तसे, त्यासाठीचा कोड:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools हा शब्दकोश आहे ज्यामध्ये टूलची नावे की म्हणून असतात
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

वरील कोडमधून दिसते की, आपल्याला कोणती साधन कॉल करायची आहे आणि कोणते आर्ग्युमेंट्स आहेत ते पार्स करावे लागेल आणि नंतर साधन कॉल करण्याची प्रक्रिया पुढे करावी लागेल.

## व्हॅलिडेशनसह दृष्टीकोन सुधारणा

आत्तापर्यंत तुम्ही पाहिले की कसे अनिवार्यरित्या प्रत्येक साधन, संसाधन आणि प्रॉम्प्ट नोंदणी करण्याऐवजी फिचर प्रकारासाठी हे दोन हँडलर वापरले जाऊ शकतात. अजून काय करावे? आपल्याला साधन योग्य आर्ग्युमेंट्ससह कॉल होत आहे याची खात्री करण्यासाठी प्रकारांची काही प्रमाणात पडताळणी जोडावी लागेल. प्रत्येक रनटाइमला यासाठी स्वतःचे साधन आहे, उदा. Python मध्ये Pydantic वापरतो आणि TypeScript मध्ये Zod वापरतो. कल्पना अशी आहे की आपण पुढील गोष्टी करू:

- वैशिष्ट्य (साधन, संसाधन किंवा प्रॉम्प्ट) तयार करण्याची लॉजिक त्याच्या समर्पित फोल्डरमध्ये हलवावी.
- येणाऱ्या विनंतीचे पडताळणी करण्याचा मार्ग तयार करावा, उदा. साधन कॉल करायची आहे का नाही.

### वैशिष्ट्य तयार करा

वैशिष्ट्य तयार करण्यासाठी, आपण त्या वैशिष्ट्यासाठी एक फाइल तयार करावी लागेल आणि तिच्यात त्या वैशिष्ट्यासाठी आवश्यक अनिवार्य फील्ड्स आहेत याची खात्री करावी लागेल. कृती साधने, संसाधने आणि प्रॉम्प्ट यामध्ये थोडी वेगळी आहे.

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
        # Pydantic मॉडेल वापरून इनपुट तपासा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोडा, जेणेकरून आपण AddInputModel तयार करू शकाल आणि args वैध करू शकू

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

इथे आपण कसे करतो ते पाहूया:

- Pydantic वापरून `AddInputModel` नावाचा स्कीमा तयार करतो ज्यात `a` आणि `b` फील्ड्स असतात, फाइल *schema.py* मध्ये.
- येणाऱ्या विनंतीला `AddInputModel` प्रकारात पार्स करण्याचा प्रयत्न करतो, जर तिथे तपशील किंवा प्रकार जुळले नाही तर अपयश येईल:

   ```python
   # add.py
    try:
        # Pydantic मॉडेल वापरून इनपुट वैधता तपासा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

हा पार्सिंग लॉजिक तुम्ही साधन कॉल फंक्शनमध्ये ठेवू शकता किंवा हँडलर फंक्शनमध्ये.

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

- सर्व साधने कॉल हँडल करणाऱ्या हँडलरमध्ये, आपण येणारी विनंती साधनाच्या स्कीमामध्ये पार्स करण्याचा प्रयत्न करतो:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    जर ते यशस्वी झाले, तर आपण खरे साधन कॉल करतो:

    ```typescript
    const result = await tool.callback(input);
    ```

जसे तुम्ही पाहता, ही पद्धत छान आर्किटेक्चर तयार करते कारण प्रत्येक गोष्ट तिच्या ठिकाणी आहे, *server.ts* ही एक फार छोटी फाइल आहे जी फक्त विनंती हँडलर जोडते आणि प्रत्येक वैशिष्ट्य त्याच्या स्वतंत्र फोल्डरमध्ये आहे उदा. tools/, resources/ किंवा prompts/.

चांगले, आता आपण हे तयार करूया.

## व्यायाम: लो-लेव्हल सर्व्हर तयार करणे

या व्यायामात, आपण पुढील गोष्टी करू:

1. एक लो-लेव्हल सर्व्हर तयार करणे जो साधने सूचीबद्ध करेल आणि साधने कॉल करेल.
2. अशी आर्किटेक्चर राबविणे ज्यावर तुम्ही वाढ करू शकता.
3. पडताळणी जोडणे जेणेकरून तुमचे साधन कॉल योग्य प्रकारे पडताळले जातील.

### -1- आर्किटेक्चर तयार करा

सर्वात आधी आपल्याला अशी आर्किटेक्चर आवश्यक आहे जी नवीन वैशिष्ट्ये जोडल्यास आपण सहजपणे वाढ करू शकू. असे कसे दिसते ते पाहूया:

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

आता आपण अशी आर्किटेक्चर तयार केली आहे जी आपल्याला नवीन साधने tools फोल्डरमध्ये सहजपणे जोडण्याची परवानगी देते. संसाधने आणि प्रॉम्प्टसाठी उपनिर्देशिका तयार करण्यासाठी तुम्ही पुढे जाऊ शकता.

### -2- साधन तयार करणे

चला पाहूया साधन तयार करणे कसे असते. प्रथम ते त्याच्या *tool* उपनिर्देशिकेत तयार करावे लागेल असे:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मॉडेल वापरून इनपुट सत्यापित करा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोडा, जेणेकरून आपण AddInputModel तयार करू शकू आणि args सत्यापित करू शकू

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

येथे आपण कसे नाव, वर्णन आणि इनपुट स्कीमा Pydantic वापरून परिभाषित करतो आणि एक हँडलर जो या साधनाला कॉल केल्यावर कार्यान्वित होतो. शेवटी आपण `tool_add` हे डिक्शनरी म्हणून या सर्व गुणधर्मांसह एक्सपोज करतो.

तसेच *schema.py* आहे जे आमच्या साधनासाठी इनपुट स्कीमा परिभाषित करतो:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

साधन निर्देशिका मॉड्यूल म्हणून वापरली जावी यासाठी *__init__.py* प्रविष्ट करणे आवश्यक आहे. तसेच आतली मॉड्यूल्स ही प्रकट करणे आवश्यक आहे:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

आम्ही हळूहळू या फाइलमध्ये अधिक साधने जोडू शकतो.

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

इथे आपण एक डिक्शनरी तयार करतो ज्यामध्ये पुढील गुणधर्म आहेत:

- name, साधनाचे नाव.
- rawSchema, हे Zod स्कीमा आहे, येणाऱ्या विनंतीसाठी पडताळणी करण्यासाठी वापरले जाईल.
- inputSchema, हा स्कीमा हँडलर वापरतो.
- callback, हे साधनाला invoke करण्यासाठी वापरले जाते.

तसेच `Tool` आहे जे या डिक्शनरीला त्याठिकाणी जे mcp सर्व्हर हँडलर स्वीकारू शकतो तितक्या प्रकारात रूपांतरित करते आणि ते असे दिसते:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

आणि *schema.ts* आहे जिथे आपण प्रत्येक साधनासाठी इनपुट स्कीमा साठवतो. सध्या एकच स्कीमा आहे पण साधने वाढविल्यानंतर जास्त नोंदी जोडू शकतो:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

चांगले, आता आपले साधने सूचीबद्ध करणे कसे हाताळायचे ते पाहू.

### -3- साधने सूचीबद्ध करणे हाताळा

साधने सूचीबद्ध करण्यासाठी, आम्हाला एक विनंती हँडलर तयार करावा लागेल. हे आपल्याला आपल्या सर्व्हर फाइलमध्ये जोडावे लागेल:

**Python**

```python
# संक्षिप्ततेसाठी कोड वगळण्यात आला आहे
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

येथे आपण डेकोरेटर `@server.list_tools` वापरतो आणि फंक्शन `handle_list_tools` अमलात आणतो. यात आपल्याला साधनांची यादी तयार करावी लागते. लक्षात ठेवा की प्रत्येक साधनाचे नाव, वर्णन आणि inputSchema असणे आवश्यक आहे.

**TypeScript**

साधने सूचीबद्ध करण्यासाठी विनंती हँडलर सेटअप करण्यासाठी, सर्व्हरवर `setRequestHandler` कॉल करतो आणि त्याला योग्य स्कीमा देतो, या बाबतीत `ListToolsRequestSchema`.

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
// संक्षिप्ततेसाठी कोड वगळले
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // नोंदणीकृत साधनांची यादी परत करा
  return {
    tools: tools
  };
});
```

छान, आता आपण साधने सूचीबद्ध करण्याचा भाग पूर्ण केला. पाहूया साधने कॉल कशी करू शकतो.

### -4- साधन कॉल हाताळा

साधन कॉल करण्यासाठी, आम्हाला दुसरा विनंती हँडलर सेट करावा लागेल, जो कोणते वैशिष्ट्य कॉल करायचे आहे आणि कोणते आर्ग्युमेंटसह हे हाताळेल.

**Python**

चलो डेकोरेटर `@server.call_tool` वापरून `handle_call_tool` नावाच्या फंक्शनसह अमलात आणूया. या फंक्शनमध्ये आपल्याला साधनाचे नाव, त्याचे आर्ग्युमेंट पार्स करावे लागेल आणि खात्री करावी लागेल की आर्ग्युमेंट्स त्या साधनासाठी योग्य आहेत. आपण हे पडताळणी या फंक्शनमध्ये करू शकतो किंवा नंतर खऱ्या साधनात करू शकतो.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools हे उपकरणांच्या नावांनी केलेले एक शब्दकोश आहे
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # उपकरणाला कॉल करा
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

येथे काय होते ते पाहू:

- आपले साधन नाव `name` या इनपुट पॅरामीटरमध्ये आधीच आहे आणि `arguments` डिक्शनरी मध्ये आपल्या आर्ग्युमेंट्स आहेत.

- साधन `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` वापरून कॉल केले जाते. आर्ग्युमेंट्सची पडताळणी `handler` प्रॉपर्टीमध्ये होईल जी फंक्शनकडे निर्देश करते, जर ते अयशस्वी झाले तर अपवाद उडेल.

अशा प्रकारे, आपल्याकडे एक संपूर्ण समजूत झाली की लो-लेव्हल सर्व्हर वापरून साधने सूचीबद्ध करणे आणि कॉल करणे कसे करावे.

पूर्ण उदाहरण येथे पाहा: [full example](./code/README.md)

## असाइनमेंट

तुम्हाला दिलेला कोड अनेक साधने, संसाधने आणि प्रॉम्प्टसह वाढवा आणि पहा की तुम्हाला फक्त tools निर्देशिकेत फाइल्स जोडण्याची गरज आहे, इतर कुठेही नाही.

*कोणताही समाधान दिलेले नाही*

## सारांश

या प्रकरणात आपण पाहिले की कसा लो-लेव्हल सर्व्हर दृष्टिकोन कार्य करतो आणि कसा आपल्या आर्किटेक्चरला स्वच्छ ठेवण्यास मदत करतो. आपण पडताळणीवर चर्चा केली आणि कसे पडताळणी लायब्ररीज वापरून इनपुट पडताळणीसाठी स्कीमा तयार करायचे हे देखील पाहिले.

## पुढे काय

- पुढे: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज एआय अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला गेला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा असत्यता असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत सर्वोत्तम आणि अधिकृत स्रोत मानले पाहिजे. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थनिर्णयांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->