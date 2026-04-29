# प्रगत सर्व्हर वापर

MCP SDK मध्ये दोन वेगवेगळ्या प्रकारचे सर्व्हर एक्सपोज केलेले असतात, तुमचा सामान्य सर्व्हर आणि लो-लेव्हल सर्व्हर. सामान्यतः, तुम्ही साधारण सर्व्हर वापरून त्यात फीचर्स जोडता. परंतु काहीप्रकारच्या बाबतीत, तुम्हाला लो-लेव्हल सर्व्हरवर अवलंबून राहायचे असते जसे की:

- चांगली आर्किटेक्चर. नियमित सर्व्हर आणि लो-लेव्हल सर्व्हर दोघांनाही वापरून स्वच्छ आर्किटेक्चर तयार करणे शक्य आहे परंतु असे म्हणता येईल की लो-लेव्हल सर्व्हर वापरणे थोडे सोपे आहे.
- फीचर उपलब्धता. काही प्रगत फीचर्स फक्त लो-लेव्हल सर्व्हरसह वापरता येतात. नंतरच्या अध्यायांमध्ये तुम्हाला हे दिसेल जेव्हा आपण सॅम्पलिंग आणि एलिसिटेशन जोडतो.

## नियमित सर्व्हर विरुद्ध लो-लेव्हल सर्व्हर

साधारण सर्व्हर वापरून MCP सर्व्हर तयार करण्याचा प्रकार असा दिसतो:

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

इथे मुद्दा असा आहे की तुम्ही स्पष्टपणे प्रत्येक टूल, रिसोर्स किंवा प्रॉम्प्ट यांना सर्व्हरमध्ये समाविष्ट करता जे तुम्हाला हवे आहे. यात काही हरकत नाही.  

### लो-लेव्हल सर्व्हर पध्दत

परंतु जेव्हा तुम्ही लो-लेव्हल सर्व्हर पध्दत वापरता तेव्हा तुम्हाला वेगळ्या प्रकारे विचार करावा लागतो. प्रत्येक टूल नोंदणी करण्याऐवजी तुम्ही प्रत्येक फीचर प्रकारासाठी दोन हॅण्डलर्स तयार करता (टूल्स, रिसोर्सेस किंवा प्रॉम्प्ट्स). उदाहरणादाखल टूल्ससाठी फक्त दोन फंक्शन्स असतात:

- सर्व टूल्सची यादी देणे. एक फंक्शन सर्व टूल्सची यादी निर्मितीसाठी जबाबदार असते.
- सर्व टूल्सना कॉल करणे. येथेही फक्त एक फंक्शन टूल कॉल्सला हेंडल करते.

हे कमी काम वाटते नाही का? म्हणून टूल नोंदणी करण्याऐवजी मला फक्त खात्री करायची की जेव्हा सर्व टूल्सची यादी बनवते तेव्हा टूल त्यात आहे आणि जेव्हा टूल कॉल करण्याची विनंती येते तेव्हा तो कॉल होतो. 

आता या कोडचा एक दृष्टिक्षेप पाहूया:

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

इथे आपल्याकडे आता एक फंक्शन आहे जे फीचर्सची यादी परत करते. टूल्स यादीतील प्रत्येक एंट्री मध्ये `name`, `description`, आणि `inputSchema` ही फील्ड्स असतात ज्यामुळे परतावा प्रकारास अनुरूप होते. यामुळे आपल्याला टूल्स आणि फीचर डिफिनेशन दुसर्‍या ठिकाणी ठेवता येतात. आता आपण आपले सर्व टूल्स टूल्स फोल्डरमध्ये तयार करू शकतो आणि तसेच सर्व तुमचे फीचर्स सुध्दा त्यामुळे तुमचा प्रोजेक्ट अचानक असे संघटित होऊ शकतो:

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

मस्त आहे, आपली आर्किटेक्चर अपेक्षेप्रमाणे स्वच्छ बनू शकते.

टूल्स कॉल करण्याबद्दल काय, त्याच कल्पनेप्रमाणे का, एक हॅण्डलर टूल कॉल करण्यासाठी, कोणताही टूल? हो, अगदी बरोबर, हा त्यासाठीचा कोड आहे:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools हे साधन नावे की म्हणून वापरले जाणारे एक शब्दकोश आहे
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
    // TODO टूलला कॉल करा,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

वरील कोडमधून, आपल्याला कॉल करण्यासाठी कोणता टूल आहे आणि कोणते arguments दिले आहेत हे पार्स करावे लागते, आणि नंतर टूल कॉल करावे लागते.

## व्हॅलिडेशन वापरून पध्दत सुधारणा

आत्तापर्यंत, तुम्ही पाहिले की टूल्स, रिसोर्सेस आणि प्रॉम्प्ट्स जोडण्यासाठी सर्व नोंदी या दोन हँडलर्सनी कशा बदलल्या जातात. आणखी काय करायचं? हो, आपण टूल योग्य आर्ग्युमेंट्ससह कॉल होतोय याची खात्री करण्यासाठी एखादे प्रकारचे व्हॅलिडेशन जोडले पाहिजे. प्रत्येक रनटाईमवर यासाठी वेगवेगळे उपाय असतात, उदाहरणार्थ Python मध्ये Pydantic वापरले जाते आणि TypeScript मध्ये Zod वापरले जाते. कल्पना अशी की आपण पुढील गोष्टी करतो:

- एखाद्या फीचर (टूल, रिसोर्स किंवा प्रॉम्प्ट) तयार करण्यासाठी त्या फीचरच्या समर्पित फोल्डरमध्ये लॉजिक हलवणे.
- येणारी विनंती योग्य आहे का याची तपासणी करण्याचा मार्ग जोडणे जसे की एखाद्या टूलला कॉल करताना.

### फीचर तयार करा

एखादे फीचर तयार करण्यासाठी, आपण त्या फीचरसाठी फाईल तयार करावी लागेल आणि आवश्यक फील्ड्स त्या फाईलमध्ये असाव्यात. टूल्स, रिसोर्सेस आणि प्रॉम्प्ट्समधील फील्ड्स थोडे वेगळे असू शकतात.

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
        # Pydantic मॉडेल वापरून इनपुटचे प्रमाणीकरण करा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोडा, जेणेकरून आपण एक AddInputModel तयार करू शकू आणि args चे प्रमाणीकरण करू शकू

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

येथे आपण कसे करतो ते पाहा:

- Pydantic वापरून `AddInputModel` हा स्कीमा तयार करतो ज्यामध्ये `a` आणि `b` हे फील्ड्स असतात, आणि तो *schema.py* फाईलमध्ये असतो.
- येणारी विनंती `AddInputModel` प्रकारात पार्स करण्याचा प्रयत्न करतो, जर पॅरामीटर्समध्ये मिसमॅच असेल तर क्रॅश होईल:

   ```python
   # add.py
    try:
        # Pydantic मॉडेल वापरून इनपुटची पडताळणी करा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

हे पार्सिंग लॉजिक टूल कॉलमध्ये ठेवायचे की हॅण्डलर फंक्शनमध्ये हे तुम्हाला ठरवायचे आहे.

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

- सर्व टूल कॉल्स हाताळणाऱ्या हॅण्डलरमध्ये, येणाऱ्या विनंतीला टूलच्या परिभाषित स्कीमामध्ये पार्स करण्याचा प्रयत्न करतो:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    जर ते यशस्वी झाले तर मूळ टूल कॉल करतो:

    ```typescript
    const result = await tool.callback(input);
    ```

ही पध्दत एक छान आर्किटेक्चर तयार करते कारण प्रत्येक गोष्टीची ठिकाणे ठरलेली असते, *server.ts* एक खूपच लहान फाईल आहे जी फक्त रिक्वेस्ट हँडलर जोडते आणि प्रत्येक फीचर त्याच्या संबंधित फोल्डरमध्ये असतो उदा. tools/, resources/ किंवा /prompts.

छान, पुढे या गोष्टी बांधण्याचा प्रयत्न करूया.

## सराव: लो-लेव्हल सर्व्हर तयार करणे

या सरावात आपण हे करणार आहोत:

1. टूल्सची यादी तयार करणे आणि टूल कॉलिंग हाताळणारा लो-लेव्हल सर्व्हर तयार करणे.
2. आपण बांधू शकणारी आर्किटेक्चर इम्प्लिमेंट करणे.
3. तुमच्या टूल कॉल्स योग्य प्रकारे व्हॅलिडेट होत आहेत याची खात्री करण्यासाठी व्हॅलिडेशन जोडणे.

### -1- आर्किटेक्चर तयार करा

आपण प्रथम तयार करायची गोष्ट म्हणजे अशी आर्किटेक्चर जी आपल्याला अधिक फीचर्स जोडताना स्केल करता येईल, त्याचा आराखडा असा आहे:

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

आता आपण अशी आर्किटेक्चर तयार केली आहे जी आपल्याला tools फोल्डरमध्ये सहज नवीन टूल्स जोडण्याची संधी देते. आपले resources आणि prompts साठी ही सबडिरेक्टरी तयार करण्यासाठी मनमोकळेपणाने या पद्धतीचे अनुसरण करा.

### -2- टूल तयार करणे

आता टूल तयार करणे कसे दिसते ते पाहूया. प्रथम, ते आपल्या *tool* सबडिरेक्टरीमध्ये तयार करावे लागेल जे असे दिसते:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic मॉडेल वापरून इनपुटचे प्रमाणीकरण करा
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic जोडा, जेणेकरून आपण AddInputModel तयार करू शकू आणि args चे प्रमाणीकरण करू शकू

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

आपण इथे पाहतो की कसे नाव, वर्णन आणि इनपुट स्कीमा Pydantic वापरून परिभाषित केले आहे आणि एक हँडलर आहे जो टूल कॉल केल्यावर invoke होतो. शेवटी, आपण `tool_add` नावाचा डिक्शनरी एक्सपोज करतो ज्यात हे सर्व गुणधर्म असतात.

तसेच *schema.py* आहे जे इनपुट स्कीमा डिफाइन करण्यासाठी वापरले जाते:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

आपल्याला *__init__.py* मध्येही भर घालणे आवश्यक आहे जेणेकरून tools डिरेक्टरी मॉड्यूल म्हणून वागेल. शिवाय, त्यातील मॉड्यूल्स एक्सपोज करणे आवश्यक आहे असे:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

टूल्स वाढवत राहिल्यावर आपण या फाईलमध्ये अधिक जोडू शकतो.

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

इथे आपण प्रॉपर्टीजचे एक डिक्शनरी तयार करतो:

- name, टूलचे नाव.
- rawSchema, ही Zod स्कीमा आहे जी येणाऱ्या टूल कॉल्सची विनंती व्हॅलिडेट करेल.
- inputSchema, ही स्कीमा हँडलर वापरेल.
- callback, हा टूल invoke करण्यासाठी वापरला जातो.

`Tool` देखील आहे जो या डिक्शनरीला एक प्रकारात रूपांतरित करतो ज्याला mcp सर्व्हर हँडलर स्वीकारू शकतो, आणि तो असा दिसतो:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

आणि *schema.ts* आहे जिथे आपण प्रत्येक टूलसाठी इनपुट स्कीमा साठवितो, सध्या केवळ एक स्कीमा आहे पण टूल्स वाढवल्यावर यामध्ये अधिक एन्ट्रीज जोडू शकतो:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

चांगलं, आता टूल्सची यादी हाताळणं कसं करायचं ते पुढे पाहूया.

### -3- टूल यादी हाताळा

आता टूल्सची यादी हाताळण्यासाठी, आपल्याला यासाठी रिक्वेस्ट हँडलर सेट करावा लागतो. खालीलप्रमाणे आपल्या सर्व्हर फाइलमध्ये ह्या गोष्टी जोडाव्या लागतील:

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

इथे आपण `@server.list_tools` डेकोरेटर आणि त्याशी निगडित फंक्शन `handle_list_tools` जोडतो. या फंक्शनमध्ये आपण टूल्सची यादी तयार करतो. लक्षात घ्या की प्रत्येक टूलमध्ये नाव, वर्णन आणि inputSchema असावे लागते.

**TypeScript**

टूल्सची यादी देण्यासाठी रिक्वेस्ट हँडलर सेट करताना, server वर `setRequestHandler` कॉल करतो ज्यामध्ये आपण करायच्या क्रियेच्या अनुरूप स्कीमा दिली जाते, इथे `ListToolsRequestSchema`.

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

छान, आता आपल्याला टूल्सची यादी तयार करण्याचा बाजू मिळाला, पुढे पाहूया आपण टूल्स कॉल कसे करू शकतो.

### -4- टूल कॉलिंग हाताळा

टूल कॉल करण्यासाठी, आपल्याला आणखी एक रिक्वेस्ट हँडलर सेट करावा लागतो, ज्यात कोणता फीचर कॉल करायचा आहे आणि कोणते arguments द्यायचे आहेत हे सांगेले.

**Python**

`@server.call_tool` डेकोरेटर वापरून `handle_call_tool` नावाचं फंक्शन इम्प्लिमेंट करूया. या फंक्शनमध्ये आपण टूलचे नाव वाचतो, त्याचे arguments पार्स करतो आणि खात्री करतो की arguments त्या टूलसाठी योग्य आहेत. आपण arguments हे फंक्शनमध्येच व्हॅलिडेट करू शकतो किंवा नंतर मूळ टूलमध्ये करू शकतो.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools हा टूल नावांसह कीजसह एक शब्दकोश आहे
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # टूलला कॉल करा
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

यामध्ये काय होते:

- टूलचे नाव input parameter `name` मध्ये असते आणि arguments `arguments` डिक्शनरी मध्ये असतात.

- टूल कॉल केला जातो `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` या प्रमाणे. arguments चे व्हॅलिडेशन `handler` प्रॉपर्टीमध्ये होते ज्यातील फंक्शनला कॉल होते, अयशस्वी झाल्यास एक्सेप्शन येते.

मग, आपल्याला लो-लेव्हल सर्व्हर वापरून टूल्सची यादी आणि कॉलिंग पूर्ण समजली.

[पूर्ण उदाहरण](./code/README.md) येथे पाहा

## असाइनमेंट

तुम्हाला दिलेला कोड वाढवा अनेक टूल्स, रिसोर्सेस आणि प्रॉम्प्ट्ससह आणि लक्षात घ्या की तुम्हाला फक्त tools डिरेक्टरीमध्ये फाइल्स जोडायच्या आहेत आणि कुठेही इतर ठिकाणी नाहीत.

*कोणतीही सोल्यूशन दिलेली नाही*

## सारांश

या अध्यायात, आपण पाहिले की लो-लेव्हल सर्व्हर पध्दत कशी काम करते आणि ती आपल्याला कशी एक चांगली आर्किटेक्चर तयार करण्यास मदत करते जिच्यावर आपण पुढे काम करू शकतो. आपण व्हॅलिडेशनबद्दलही चर्चा केली आणि व्हॅलिडेशन लायब्ररी वापरून इनपुट व्हॅलिडेशनसाठी स्कीमा कसे तयार करायचे हे शिकले.

## पुढे काय

- पुढे: [सामान्य प्रमाणीकरण](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केलेला आहे. आम्ही अचूकतेसाठी प्रयत्न करत असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अशुद्धता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वपूर्ण माहितीसाठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या समजुतीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->