# ការប្រើប្រាស់ម៉ាស៊ីន​បម្រើ​ជ្រើសរើស

មានម៉ាស៊ីន​បម្រើពីរប្រភេទផ្ទាល់ក្នុង MCP SDK ដែលមានម៉ាស៊ីន​បម្រើធម្មតារបស់អ្នក និងម៉ាស៊ីន​បម្រើកម្រិតទាប។ ជាទូទៅ អ្នកនឹងប្រើម៉ាស៊ីន​បម្រើធម្មតាសម្រាប់បន្ថែមមុខងារ។ ទោះយ៉ាងណា សម្រាប់ករណីខ្លះ អ្នកចង់ពឹងពាក់លើម៉ាស៊ីន​បម្រើកម្រិតទាប ដូចជាៈ

- ស្ថាបត្យកម្មល្អជាង។ អាចបង្កើតស្ថាបត្យកម្មបានស្អាតជាមួយម៉ាស៊ីន​បម្រើធម្មតា និងម៉ាស៊ីន​បម្រើកម្រិតទាបទាំងពីរ ប៉ុន្តែអាចអះអាងថាបានល្អជាងពីម៉ាស៊ីន​បម្រើកម្រិតទាប។
- ការរក្សាទុកមុខងារ។ មុខងាររបស់កម្រិតខ្ពស់ខ្លះអាចប្រើបានតែជាមួយម៉ាស៊ីន​បម្រើកម្រិតទាប។ អ្នកនឹងឃើញច្បាប់នេះនៅក្នុងជំពូកក្រោយនៅពេលយើងបន្ថែមការសំណាក់ទិន្នន័យ និងការលូតលាស់។

## ម៉ាស៊ីន​បម្រើធម្មតា ប្រៀបធៀបជាមួយម៉ាស៊ីន​បម្រើកម្រិតទាប

នេះគឺជាការបង្កើត MCP Server ដូចជា​ជាមួយម៉ាស៊ីន​បម្រើធម្មតា

**Python**

```python
mcp = FastMCP("Demo")

# បន្ថែមឧបករណ៍បូក
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

// បន្ថែមឧបករណ៍បូក
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

គោលបំណងគឺអ្នកត្រូវបន្ថែមឧបករណ៍ រដ្ឋធនធាន ឬការជំរុញ នីមួយៗទៅម៉ាស៊ីន​បម្រើ។ មិនមានអ្វីខុសទេ។  

### វិធីសាស្រ្តម៉ាស៊ីន​បម្រើកម្រិតទាប

ទោះបីជាយ៉ាងណា កាលណាអ្នកប្រើវិធីសាស្រ្តម៉ាស៊ីន​បម្រើកម្រិតទាប អ្នកត្រូវគិតឲ្យល្អ។ មិនប៊ុន្រក់ឧបករណ៍នីមួយៗទេ តែអ្នកបង្កើតអ្នកដោះស្រាយពីរ រយៈមុខងារមួយ (ឧបករណ៍, រដ្ឋធនធាន ឬការជំរុញ)។ ឧទាហរណ៍ ឧបករណ៍ត្រូវមានមុខងារចំនួនពីរដូចខាងក្រោម៖

- បញ្ជីឧបករណ៍ទាំងអស់។ មុខងារមួយមានកាតព្វកិច្ចគ្រប់គ្រងការបង្ហាញបញ្ជីឧបករណ៍ទាំងអស់។
- គ្រប់គ្រងការហៅឧបករណ៍ទាំងអស់។ នៅទីនេះ មានតែមុខងារតែមួយគ្រប់គ្រងការហៅឧបករណ៍។

នេះស្តាប់ហួសពីការងារ តើយ៉ាងណា? ដូច្នេះផ្ទុយពីការចុះបញ្ជីឧបករណ៍ ខ្ញុំគ្រាន់តែត្រូវធ្វើឲ្យវាត្រូវបង្ហាញនៅពេលបញ្ជីឧបករណ៍ និងត្រូវហៅវា នៅពេលមានការស្នើសុំហៅឧបករណ៍។

មកមើលរបៀបដែលកូដបង្ហាញឥឡូវនេះ៖

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
  // ត្រឡប់បញ្ជីឧបករណ៍ដែលបានចុះបញ្ជី
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

នៅទីនេះ ឥឡូវនេះមានមុខងារមួយដែលត្រឡប់បញ្ជីមុខងារ។ ចំណូលមួយក្នុងបញ្ជីឧបករណ៍មានវាលដូចជា `name`, `description` និង `inputSchema` ដែលអនុវត្តទៅតាមប្រភេទត្រឡប់។ វាផ្ដល់ឱ្យយើងអាចដាក់ឧបករណ៍ និងកំណត់មុខងារនៅកន្លែងផ្សេង។ ឥឡូវនេះ អាចបង្កើតឧបករណ៍ទាំងអស់នៅក្នុងថត tools ហើយដូចគ្នាទៅនឹងមុខងារទាំងអស់ ដូច្នេះគម្រោងរបស់អ្នកអាចរៀបចំបានដូច្នេះ៖

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

ល្អណាស់ ស្ថាបត្យកម្មរបស់យើងអាចធ្វើឲ្យស្អាតបាន។

តើការហៅឧបករណ៍ល្អដូចម្តេច? តើវាជាគំនិតដូចគ្នា? មុខងារដើម្បីហៅឧបករណ៍ មួយនេះហើយ? បាទ ច្បាស់ហើយ នេះគឺជា​កូដសម្រាប់វា៖

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools គឺជាដិក్షាណារីដែលមានឈ្មោះឧបករណ៍ជា key
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
    // TODO ហៅឧបករណ៍,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ដូចដែលអ្នកឃើញពីកូដខាងលើ យើងត្រូវបំបែកឧបករណ៍ដែលត្រូវហៅ និងអាជ្ញាបណ្ណដែលត្រូវប្រើ ហើយបន្ទាប់មកយើងត្រូវបន្តហៅឧបករណ៍នោះ។

## កែលម្អវិធីសាស្រ្តជាមួយការផ្ទៀងផ្ទាត់

មកដល់ពេលនេះ អ្នកបានឃើញថាការចុះបញ្ជីមុខងារ ដើម្បីបន្ថែមឧបករណ៍ រដ្ឋធនធាន និងជំរុញអាចជំនួសដោយអ្នកដោះស្រាយពីរនៅក្នុងមុខងារ។ តើមានអ្វីផ្សេងទៀតដើម្បីធ្វើ? យើងគួរបន្ថែមការផ្ទៀងផ្ទាត់ឲ្យទៅតាមសមាសភាពសម្រាប់ធានាថាឧបករណ៍ត្រូវបានហៅជាសុចរិត។ រuntime ទាំងអស់មានដំណោះស្រាយផ្ទាល់ខ្លួន សម្រាប់ឧទាហរណ៍ Python ប្រើ Pydantic និង TypeScript ប្រើ Zod។ គំនិតគឺដូចខាងក្រោម៖

- ផ្លាស់ប្តូរតុល្យភាពបង្កើតមុខងារ (ឧបករណ៍, រដ្ឋធនធាន ឬជំរុញ) ទៅថតរបស់ខ្លួន។
- បន្ថែមវិធីសាស្រ្តផ្ទៀងផ្ទាត់សំណើសុំចូល មួយដែលស្នើសុំហៅឧបករណ៍ជាដើម។

### បង្កើតមុខងារ

ដើម្បីបង្កើតមុខងារ អ្នកត្រូវបង្កើតឯកសារសម្រាប់មុខងារនោះហើយធ្វើឲ្យវាមានវាលបង្ហាញពេញលេញដែលត្រូវការ។ វាលនីមួយៗខុសគ្នារវាងឧបករណ៍ រដ្ឋធនធាន និងជំរុញ។

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
        # បញ្ជាក់តម្លៃបញ្ចូលដោយប្រើម៉ូដែល Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: បន្ថែម Pydantic ដើម្បីយើងអាចបង្កើត AddInputModel និងបញ្ជាក់ args បាន

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

នៅទីនេះ អ្នកអាចឃើញថាយើងធ្វើការដូចខាងក្រោម៖

- បង្កើតស្គីម៉ាទីដោយប្រើ Pydantic `AddInputModel` មានវាល `a` និង `b` ក្នុងឯកសារ *schema.py*។
- ព្យាយាមបំបែកសំណើចូលឲ្យក្លាយជា `AddInputModel` ប្រសិនបើ parameters មិនត្រូវផ្ទុយ នេះនឹងបណ្តាលឲ្យមានកំហុស៖

   ```python
   # add.py
    try:
        # ត្រួតពិនិត្យការបញ្ចូលដោយប្រើម៉ូឌែល Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

អ្នកអាចជ្រើសរើសដាក់វិធីសាស្រ្តនេះក្នុងការហៅឧបករណ៍គ្រប់គ្រង ឬនៅក្នុងមុខងារអ្នកដោះស្រាយ។

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

- នៅក្នុងអ្នកដោះស្រាយដែលគ្រប់គ្រងការហៅឧបករណ៍ទាំងអស់ ឥឡូវនេះយើងព្យាយាមបំបែកសំណើចូលទៅតាមស្គីម៉ារបស់ឧបករណ៍៖

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ប្រសិនបើវាដំណើរការត្រឹមត្រូវ យើងបន្តហៅឧបករណ៍ពិតប្រាកដ៖

    ```typescript
    const result = await tool.callback(input);
    ```

ដូចដែលអ្នកឃើញ វិធីសាស្រ្តនេះបង្កើតស្ថាបត្យកម្មល្អ ព្រោះគ្រប់អ្វីមានទីតាំងរបស់ខ្លួន *server.ts* គឺឯកសារតូចតែកាន់តែភ្ជាប់អ្នកដោះស្រាយសំណើ និងមុខងារនីមួយៗនៅក្នុងថតរបស់ខ្លួន tools/, resources/ ឬ /prompts។

ល្អណាស់ យើងសាកល្បងបង្កើតវាបន្តទីនេះ។

## លំហាត់: បង្កើតម៉ាស៊ីន​បម្រើកម្រិតទាប

ក្នុងលំហាត់នេះ យើងនឹងបង្កើត៖

1. បង្កើតម៉ាស៊ីន​បម្រើកម្រិតទាបគ្រប់គ្រងបញ្ជីឧបករណ៍ និងហៅឧបករណ៍។
2. អនុវត្តស្ថាបត្យកម្មដែលអ្នកអាចបន្តសាងសង់បាន។
3. បន្ថែមការផ្ទៀងផ្ទាត់ឲ្យធានាថាការហៅឧបករណ៍របស់អ្នកត្រូវបានផ្ទៀងផ្ទាត់ត្រឹមត្រូវ។

### -1- បង្កើតស្ថាបត្យកម្ម

អ្វីដែលយើងត្រូវរៀបចំបំបំរុងគឺស្ថាបត្យកម្មដែលជួយអោយយើងសំរួលពេលបន្ថែមមុខងារ ថ្មីៗនេះរូបភាពដូចខាងក្រោម៖

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

ឥឡូវនេះយើងបានរៀបចំស្ថាបត្យកម្មដែលធានាថាអាចបន្ថែមឧបករណ៍ថ្មីៗនៅក្នុងថត tools បានយ៉ាងងាយស្រួល។ អ្នកអាចបន្ថែមថតរងសម្រាប់ resources និង prompts នេះផងដែរ។

### -2- បង្កើតឧបករណ៍

មកមើលរបៀបបង្កើតឧបករណ៍បន្ទាប់។ ជាដំបូង វាត្រូវបង្កើតនៅក្នុងថតរង *tool* ដូចខាងក្រោម៖

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ថតសំគាល់ការបញ្ចូលដោយប្រើម៉ូឌែល Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: បញ្ចូល Pydantic ដើម្បីឲ្យយើងអាចបង្កើត AddInputModel និងធ្វើតេស្ត args បាន

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

អ្វីដែលយើងឃើញនៅទីនេះគឺរបៀបកំណត់ឈ្មោះ, ពណ៌នា និង schema ចូលដោយប្រើ Pydantic ហើយអ្នកដោះស្រាយដែលនឹងត្រូវហៅនៅពេលឧបករណ៍នេះត្រូវហៅ។ ជាការបញ្ចប់ យើងបង្ហាញ `tool_add` ដែលជាថតភាពDICT ឯកត្តដែលមានគុណលក្ខណៈទាំងនេះ។

មាន *schema.py* ដែលប្រើសម្រាប់កំណត់ស្គីម៉ា​ចូលដែលប្រើដោយឧបករណ៍:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

យើងត្រូវបំពេញ *__init__.py* ដើម្បីធ្វើឲ្យថតឧបករណ៍ត្រូវបានប្រើជាមូឌុល។ ក៏ដូចជាត្រូវបង្ហាញមូឌុលនៅក្នុងថតនោះដែរ ដូចខាងក្រោម៖

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

យើងអាចបន្ថែមទៀតទៅឯកសារនេះពេលបន្ថែមឧបករណ៍ថ្មីៗ។

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

នៅទីនេះ យើងបង្កើត dict ដែលមានគុណលក្ខណៈៈ

- name, ឈ្មោះឧបករណ៍។
- rawSchema, ស្គីម៉ា Zod នេះប្រើដើម្បីផ្ទៀងផ្ទាត់សំណើចូលហៅឧបករណ៍។
- inputSchema, ស្គីម៉ានេះប្រើដោយអ្នកដោះស្រាយ។
- callback, ប្រើហៅឧបករណ៍។

មាន `Tool` ដែលប្រើបម្លែង dict នេះទៅជាប្រភេទដែលអ្នកដោះស្រាយម៉ាស៊ីន​បម្រើ mcp អាចទទួលបាន ហើយវាមើលទៅដូចខាងក្រោម៖

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ហើយមាន *schema.ts* ដែលផ្ទុកស្គីម៉ាចូលសម្រាប់ឧបករណ៍នីមួយៗ ដែលដូចរូបខាងក្រោម មានស្គីម៉ា​មួយគត់ក្នុងពេលបច្ចុប្បន្ន ប៉ុន្តែម្តងទៀត អ្នកអាចបន្ថែមចំណូលថ្មីៗបាន៖

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ល្អណាស់ បន្ទាប់មកយើងនឹងគ្រប់គ្រងបញ្ជីឧបករណ៍។

### -3- គ្រប់គ្រងបញ្ជីឧបករណ៍

បន្ទាប់មក ដើម្បីគ្រប់គ្រងបញ្ជីឧបករណ៍ យើងត្រូវរៀបចំអ្នកដោះស្រាយសំណើសុំសម្រាប់វា។ អ្វីដែលយើងត្រូវបន្ថែមក្នុងឯកសារម៉ាស៊ីន​បម្រើ៖

**Python**

```python
# កូដបានលុបចេញសម្រាប់ការសង្ខេបខ្លី
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

នៅទីនេះ យើងបន្ថែម decorator `@server.list_tools` ហើយអនុវត្តមុខងារ `handle_list_tools`។ ក្នុងមុខងារនេះ យើងត្រូវបង្កើតបញ្ជីឧបករណ៍។ សម្គាល់ថាក្នុងឧបករណ៍នីមួយៗ ត្រូវមាន name, description និង inputSchema។   

**TypeScript**

ដើម្បីរៀបចំអ្នកដោះស្រាយសំណើសុំសម្រាប់បញ្ជីឧបករណ៍ យើងត្រូវហៅ setRequestHandler លើម៉ាស៊ីន​បម្រើជាមួយស្គីម៉ាដែលសមស្របនឹងបំណងយើង នៅនៅរឿងនេះគឺជា `ListToolsRequestSchema`។

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
// កូដបានលុបចេញសម្រាប់ការប្រមូលផ្តុំ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ត្រឡប់មកវិញនូវបញ្ជីឧបករណ៍ដែលបានចុះបញ្ជី
  return {
    tools: tools
  };
});
```

ល្អហើយ ឥឡូវនេះយើងបានដោះស្រាយផ្នែកបញ្ជីឧបករណ៍ ដូច្នេះមកមើលរបៀបហៅឧបករណ៍បន្ទាប់។

### -4- គ្រប់គ្រងការហៅឧបករណ៍

ដើម្បីហៅឧបករណ៍ យើងត្រូវរៀបចំអ្នកដោះស្រាយសំណើសុំមួយទៀត ដែលផ្តោតលើធ្វើការបញ្ជាក់មុខងារដែលត្រូវហៅ និងអាជ្ញាបណ្ណដែលត្រូវប្រើ។

**Python**

យើងប្រើ decorator `@server.call_tool` ហើយអនុវត្តវា ជាមួយមុខងារ `handle_call_tool`។ ក្នុងមុខងារនេះ បំបែកឈ្មោះឧបករណ៍ និងអាជ្ញាបណ្ណហើយធានាថាអាជ្ញាបណ្ណត្រឹមត្រូវសម្រាប់ឧបករណ៍។ អ្នកអាចផ្ទៀងផ្ទាត់អាជ្ញាបណ្ណនៅក្នុងមុខងារនេះ ឬនៅក្នុងឧបករណ៍ពិតប្រាកដ។

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools គឺជាថតទិន្នន័យដែលមានឈ្មោះឧបករណ៍ជាគ្រាប់សោ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ហៅឧបករណ៍
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

នេះជាអ្វីដែលកំពុងបើកចំហ៖

- ឈ្មោះឧបករណ៍របស់យើងមានជាអាជ្ញាស្នូល `name` ដែលជាការបញ្ចូលក្នុង `arguments` ដែលជាដិចស្ដ dictionary។

- ឧបករណ៍ត្រូវបានហៅជាមួយ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`។ ការផ្ទៀងផ្ទាត់ argument ធ្វើឡើងនៅក្នុង property `handler` ដែលពួកវាជាមុខងារ បើបរាជ័យវានឹងបង្កើតកំហុស។

ហើយឥឡូវនេះ យើងបានយល់ដឹងពេញលេញអំពីការបង្ហាញនិងហៅឧបករណ៍ដោយប្រើម៉ាស៊ីន​បម្រើកម្រិតទាប។

មើល [ឧទាហរណ៍ពេញលេញ](./code/README.md) នៅទីនេះ

## កិច្ចការ

ពង្រីកកូដដែលបានផ្តល់ជូនដោយបន្ថែមឧបករណ៍ ចំណេញ និងការជំរុញជាច្រើន ហើយសម្គាល់ថាអ្នកត្រូវបន្ថែមឯកសារផ្តល់នៅក្នុងថត tools ប៉ុណ្ណោះ ហើយគ្មានទីផ្សេងទៀតទេ។

*មិនមានដំណោះស្រាយផ្តល់*

## សង្ខេប

ក្នុងជំពូកនេះ អ្នកបានឃើញវិធីសាស្រ្តម៉ាស៊ីន​បម្រើកម្រិតទាបរបស់ MCP SDK និងរបៀបដែលវាអាចជួយបង្កើតស្ថាបត្យកម្មល្អដែលអាចបន្តសាងសង់បាន។ យើងបានផ្លាស់ប្តូរពិចារណាអំពីការផ្ទៀងផ្ទាត់ និងបានបង្ហាញអ្នកពីរបៀបប្រើបណ្ណាល័យ validation ដើម្បីបង្កើតស្គីម៉ាសម្រាប់ការផ្ទៀងផ្ទាត់ការបញ្ចូល។

## ជំហានបន្ទាប់

- បន្ទាប់: [ការផ្ទៀងផ្ទាត់ដោយសាមញ្ញ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការសម្រេចចិត្ត**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ បើទោះយើងខំប្រឹងប្រែងដើម្បីមានភាពត្រឹមត្រូវ ល្វើយករណីបកប្រែដោយស្វ័យប្រវត្តិក្នុងឯកសារនេះអាចមានកំហុស ឬមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកជាឯកសារដំបូងដើម្បីយោង។ សម្រាប់ព័ត៌មានសំខាន់ណាស់ ការបកប្រែដោយមនុស្សជំនាញគឺត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសប្លែកណាមួយដែលកើតចេញពីការប្រើប្រាស់ការបកប្រែនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->