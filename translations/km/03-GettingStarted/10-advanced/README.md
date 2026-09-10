# ការប្រើប្រាស់ម៉ាស៊ីនមេជំនាញ

មានម៉ាស៊ីនមេពីរ​ប្រភេទខុសគ្នាត្រូវបានបង្ហាញក្នុង MCP SDK គឺម៉ាស៊ីនមេធម្មតារបស់អ្នក និងម៉ាស៊ីនមេកម្រិតទាប។ ជាទូទៅ អ្នកនឹងប្រើម៉ាស៊ីនមេធម្មតាដើម្បីបន្ថែមមុខងារ។ ប៉ុន្តែក្នុងករណីខ្លះ អ្នកចង់ពឹងផ្អែកលើម៉ាស៊ីនមេកម្រិតទាប ដូចជា៖

- សំណង់រចនាសម្ព័ន្ធល្អប្រសើរ។ អាចបង្កើតសំណង់រចនាសម្ព័ន្ធបានស្អាតទាំងម៉ាស៊ីនមេធម្មតា និងម៉ាស៊ីនមេកម្រិតទាប ប៉ុន្តារឿងនេះអាចអះអាងថាវាងាយស្រួលជាមួយម៉ាស៊ីនមេកម្រិតទាបបន្តិច។
- ការត្រូវការមុខងារ។ មុខងារដែលជំនាញខ្ពស់ខ្លះផ្តល់បានតែជាមួយ
    ម៉ាស៊ីនមេកម្រិតទាបប៉ុណ្ណោះ។ ជំពូកក្រោយនិយាយពី Elicitation និងមុខងារ Sampling សម្រាប់តំបន់ចាស់
    ដែលត្រូវបានឈប់បច្ចុប្បន្នភាពនៅ MCP `2026-07-28`។

## ម៉ាស៊ីនមេធម្មតាប្រឆាំងម៉ាស៊ីនមេកម្រិតទាប

នេះគឺជាដំណើរការបង្កើតម៉ាស៊ីនមេ MCP ជាមួយម៉ាស៊ីនមេធម្មតា

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

ចំណុចគឺ អ្នកប្រុងបញ្ចូលឧបករណ៍ ស្រោមប្រើ ឬការបញ្ជូនដែលអ្នកចង់ឲ្យម៉ាស៊ីនមេមាន។ មិនមានអ្វីខុសទេ។

### វិធីសាស្រ្តម៉ាស៊ីនមេកម្រិតទាប

ទោះយ៉ាងណា នៅពេលប្រើវិធីសាស្រ្តម៉ាស៊ីនមេកម្រិតទាប អ្នកត្រូវគិតផ្សេង។ ជំនួសការចុះបញ្ជីឧបករណ៍ ពួកអ្នកបង្កើតកម្មវិធីរៀបចំក្រុមហ៊ុនពីរតាមប្រភេទមុខងារ (ឧបករណ៍ ស្រោមប្រើ ឬការបញ្ជូនំ)។ ក្នុងឧទាហរណ៍ឧបករណ៍មានមុខងារពីរតៃ:

- រាយបញ្ជីឧបករណ៍ទាំងអស់។ មុខងារមួយត្រូវទទួលខុសត្រូវក្នុងការរាយបញ្ជីឧបករណ៍ទាំងអស់។
- គ្រប់គ្រងការហៅឧបករណ៍ទាំងអស់។ នៅទីនេះ ក៏មានមុខងារមួយសម្រាប់គ្រប់គ្រងហៅឧបករណ៍ផងដែរ។

វាមើលទៅមើលច្រើនការងារតិចមែនទេ? ដូច្នេះជំនួសការចុះបញ្ជីឧបករណ៍ ខ្ញុំត្រូវប្រាកដថាឧបករណ៍ត្រូវបានរាយបញ្ជីពេលខ្ញុំរាយបញ្ជីឧបករណ៍ទាំងអស់ ហើយត្រូវបានហៅពេលមានការស្នើសុំសម្រាប់ហៅឧបករណ៍។

មកមើលពីរបៀបកូដឥឡូវនេះឆ្លងកាត់:

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
  // បង្វិលបញ្ជីឧបករណ៍ដែលបានចុះបញ្ជី
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

នៅទីនេះ យើងមានមុខងារមួយដែលត្រឡប់បញ្ជីមុខងារ។ រាល់ធាតុក្នុងបញ្ជីឧបករណ៍ឥឡូវមានវាលដូចជា `name`, `description` និង `inputSchema` ដើម្បីសម្រួលប្រភេទត្រឡប់។ វាអាចផ្តល់ឱ្យយើងដាក់ឧបករណ៍ និងការពិពណ៌នាមុខងាររបស់យើងនៅកន្លែងផ្សេងទៀត។ យើងអាចបង្កើតឧបករណ៍ទាំងអស់នៅក្នុងថត tools ហើយសម្រាប់មុខងារទាំងអស់ឲ្យគម្រោងរបស់អ្នករួចរាល់ដូច្នេះ ៖

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

នេះពិតជាល្អ សំណង់រចនាសម្ព័ន្ធរបស់យើងអាចធ្វើឲ្យមើលទៅស្អាតណាស់។

ក្នុងការហៅឧបករណ៍ តើវាគឺជាគំនិតដូចគ្នាទេ មុខងារមួយហៅឧបករណ៍ណាមួយ? បាទត្រឹមត្រូវនេះជាកូដសម្រាប់វា៖

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools គឺជា dictionary ដែលមានឈ្មោះឧបករណ៍ជា key
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

ដូចដែលអ្នកឃើញពីកូដខាងលើ យើងត្រូវបំលែងឧបករណ៍ដើម្បីហៅ និងជាមួយនឹងអាគុយម៉ង់ ហើយបន្ទាប់មកត្រូវបន្តទៅការហៅឧបករណ៍។

## កែលម្អវិធីសាស្រ្តជាមួយការផ្ទៀងផ្ទាត់

រហូតដល់ពេលនេះ អ្នកបានឃើញវិធីសាស្រ្តចុះបញ្ជីឧបករណ៍ ស្រោមប្រើ និងការបញ្ជូន ត្រូវបានជំនួសដោយមុខងារចំនួនពីរប្រភេទមុខងារតែម្តង។ តើយើងត្រូវធ្វើអ្វីបន្ថែមទៀត? យើងគួរតែបន្ថែមការផ្ទៀងផ្ទាត់ ដើម្បីធានាថាឧបករណ៍ត្រូវបានហៅជាមួយនឹងអាគុយម៉ង់ត្រឹមត្រូវ។ រាល់ runtime មានដំណោះស្រាយផ្ទាល់ខ្លួន សម្រាប់ Python ប្រើ Pydantic ហើយសម្រាប់ TypeScript ប្រើ Zod។ គំនិតគឺយើងធ្វើដូចខាងក្រោម៖

- ផ្លាស់ប្តូរតុល្យភាពសម្រាប់បង្កើតមុខងារ (ឧបករណ៍ ស្រោមប្រើ ឬការបញ្ជូន) ទៅថតជាក់លាក់របស់វា។
- បន្ថែមវិធីសាស្រ្តត្រួតពិនិត្យសំណើដែលមកដល់ ដើម្បីឧទាហរណ៍ហៅឧបករណ៍។

### បង្កើតមុខងារ

ដើម្បីបង្កើតមុខងារ យើងត្រូវបង្កើតឯកសារសម្រាប់មុខងារនោះ និងប្រាកដថាវាមានវាលបាច់ដែលត្រូវការសម្រាប់មុខងារនោះ។ វាលខុសគ្នាមួយចំនួនរវាងឧបករណ៍ ស្រោមប្រើ និងការបញ្ជូន។

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
        # ផ្ទៀងផ្ទាត់ការបញ្ចូលដោយប្រើគំរូ Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: បន្ថែម Pydantic ដូច្នេះយើងអាចបង្កើត AddInputModel និងផ្ទៀងផ្ទាត់ args បាន

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

នៅទីនេះ អ្នកអាចឃើញពីវិធីសាស្រ្តដូចខាងក្រោម៖

- បង្កើត schema ដោយប្រើ Pydantic `AddInputModel` មានវាល `a` និង `b` ក្នុងឯកសារ *schema.py*។
- ព្យាយាមបំលែងសំណើដែលមកដល់ឲ្យស្របជាប្រភេទ `AddInputModel` បើមានការខុសគ្នានៅពាក្យបញ្ជា នេះនឹងធ្វើឲ្យកើតកំហុស៖

   ```python
   # add.py
    try:
        # ពិនិត្យការបញ្ចូលដោយប្រើម៉ូឌែល Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

អ្នកអាចជ្រើសរើសដាក់បង្កើតវិធីសាស្រ្តនេះក្នុងការហៅឧបករណ៍ផ្ទាល់ ឬក្នុងមុខងារគ្រប់គ្រង។

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

- ក្នុងមុខងារគ្រប់គ្រងការហៅឧបករណ៍ទាំងអស់ ឥឡូវនេះយើងព្យាយាមបំលែងសំណើដែលមកដល់ទៅ schema ដដែលនៃឧបករណ៍៖

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    បើវាជោគជ័យវានឹងបន្តហៅឧបករណ៍ពិតប្រាកដ៖

    ```typescript
    const result = await tool.callback(input);
    ```

ដូចដែលអ្នកឃើញ វិធីសាស្រ្តនេះបង្កើតសំណង់រចនាសម្ព័ន្ធល្អ ពីព្រោះរាល់វត្ថុមានទីតាំងមួយ ផ្ទុកក្នុងថតខ្លួនឯង គឺ tools/, resources/ ឬ prompts ។

ល្អណាស់ យើងសាកល្បងកសាងវាបន្ទាប់។

## អនុវត្តន៍៖ បង្កើតម៉ាស៊ីនមេកម្រិតទាប

ក្នុងសកម្មភាពនេះ យើងនឹងធ្វើដូចខាងក្រោម៖

1. បង្កើតម៉ាស៊ីនមេកម្រិតទាប គ្រប់គ្រងការរាយបញ្ជីឧបករណ៍ និងការហៅឧបករណ៍។
1. អនុវត្តសំណង់រចនាសម្ព័ន្ធដែលអ្នកអាចសាងសង់លើវា។
1. បន្ថែមការផ្ទៀងផ្ទាត់ដើម្បីធានាថាការហៅឧបករណ៍ត្រូវបានផ្ទៀងផ្ទាត់យ៉ាងត្រឹមត្រូវ។

### -1- បង្កើតសំណង់រចនាសម្ព័ន្ធ

អ្វីដែលយើងត្រូវដោះស្រាយជំពូកដំបូងគឺសំណង់រចនាសម្ព័ន្ធដែលជួយឲ្យយើងអាចពង្រីកបាន ខាងក្រោមនេះជារូបមន្ត៖

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

ឥឡូវនេះយើងបានរៀបចំសំណង់រចនាសម្ព័ន្ធដែលធានាថា អ្នកអាចបន្ថែមឧបករណ៍ថ្មីៗនៅក្នុងថត tools បានយ៉ាងងាយស្រួល។ អ្នកអាចបន្ថែមថតរងសម្រាប់ resources និង prompts ថែមទៀត។

### -2- បង្កើតឧបករណ៍

មកមើលពីរបៀបបង្កើតឧបករណ៍បន្ទាប់។ ជាដំបូង វាត្រូវបានបង្កើតក្នុងថត *tool* របស់វា ដូចខាងក្រោម៖

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ផ្ទៀងផ្ទាត់ការបញ្ចូលដោយប្រើម៉ូឌែល Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: បន្ថែម Pydantic ដើម្បីដែលយើងអាចបង្កើត AddInputModel និងផ្ទៀងផ្ទាត់ args បាន

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

អ្វីដែលយើងឃើញនៅទីនេះគឺរបៀបកំណត់ឈ្មោះ ការពិពណ៌នា និង schema នាំចូលប្រើ Pydantic ហើយមានមុខងារគ្រប់គ្រងដែលត្រូវបានហៅពេលឧបករណ៍នេះត្រូវបានហៅ។ ចុងក្រោយ យើងបង្ហាញ `tool_add` ដែលជាផ្ទាំងតំណរទាំងអស់នៃលក្ខណៈទាំងនេះ។

នៅមាន *schema.py* ដែលប្រើសម្រាប់កំណត់ schema នាំចូលសម្រាប់ឧបករណ៍របស់យើង៖

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

យើងត្រូវបំពេញ *__init__.py* ដើម្បីធានាថាតម្លៃថត tools ត្រូវបានប្រើជាម៉ូឌុល។ លើសពីនេះ យើងត្រូវបង្ហាញម៉ូឌុលនៅក្នុង វាថ្មីៗដូចខាងក្រោម៖

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

យើងអាចបន្ថែមទៅឯកសារនេះបើបន្ថែមឧបករណ៍ថ្មី។

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

នៅទីនេះ យើងបង្កើតផ្ទាំងដែលមានលក្ខណៈ៖

- name, រូបមន្តឈ្មោះឧបករណ៍។
- rawSchema, នេះគឺ schema Zod ដែលប្រើសម្រាប់ផ្ទៀងផ្ទាត់សំណើដែលមកដល់ក្នុងការហៅឧបករណ៍នេះ។
- inputSchema, schema នេះប្រើដោយមុខងារគ្រប់គ្រង។
- callback, ប្រើសម្រាប់ហៅឧបករណ៍។

មាន `Tool` ដែលប្រើបម្លែងផ្ទាំងនេះទៅប្រភេទដែល mcp server handler ទទួលបាន ហើយវាមើលទៅដូចខាងក្រោម៖

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ហើយមាន *schema.ts* ដែលយើងរក្សាទុក schema នាំចូល សម្រាប់ឧបករណ៍មួយៗ ដូចខាងក្រោមដែលមាន schema មួយនៅបច្ចុប្បន្ន ប៉ុន្តែបើបន្ថែមឧបករណ៍ អាចបន្ថែមធាតុជាច្រើន៖

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ល្អណាស់ យើងបន្តដំណើរការគ្រប់គ្រងការរាយបញ្ជីឧបករណ៍បន្ទាប់។

### -3- គ្រប់គ្រងការរាយបញ្ជីឧបករណ៍

បន្ទាប់មក ដើម្បីគ្រប់គ្រងការរាយបញ្ជីឧបករណ៍ យើងត្រូវបង្កើតមុខងារគ្រប់គ្រងសំណើសម្រាប់វា។ នេះគឺអ្វីដែលយើងត្រូវបន្ថែមទៅក្នុងឯកសារម៉ាស៊ីនមេ៖

**Python**

```python
# កូដបានលុបទុកសម្រាប់រំលេចខ្លី
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

នៅទីនេះ យើងបន្ថែម decorator `@server.list_tools` និងមុខងារអនុវត្ត `handle_list_tools`។ នៅក្នុងមុខងារនេះ យើងត្រូវបង្កើតបញ្ជីឧបករណ៍។ ចំណាំថារាល់ឧបករណ៍ត្រូវមានឈ្មោះ ការពិពណ៌នា និង inputSchema។

**TypeScript**

ដើម្បីដាក់តំណាងសំណើរ​សម្រាប់រាយបញ្ជីឧបករណ៍ ត្រូវហៅ `setRequestHandler` លើម៉ាស៊ីនមេជាមួយ schema សមរម្យ `ListToolsRequestSchema`។

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
// កូដបានលុបចេញសម្រាប់ការសង្ខេប
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ត្រឡប់មកនូវបញ្ជីឧបករណ៍ដែលបានចុះបញ្ជីរួចហើយ
  return {
    tools: tools
  };
});
```

ល្អ ឥឡូវ យើងបានដោះស្រាយផ្នែករាយបញ្ជីឧបករណ៍ មកមើលពីរបៀបហៅឧបករណ៍បន្ទាប់។

### -4- គ្រប់គ្រងការហៅឧបករណ៍

ដើម្បីហៅឧបករណ៍ យើងត្រូវបង្កើតមុខងារគ្រប់គ្រងសំណើមួយទៀត ដែលផ្ដោតលើការដាក់បញ្ជាក់មុខងារដែលត្រូវហៅ និងអាគុយម៉ង់ដែលត្រូវប្រើ។

**Python**

ដើម្បីប្រើ decorator `@server.call_tool` និងអនុវត្តវាដោយមុខងារ `handle_call_tool`។ ក្នុងមុខងារនេះ យើងត្រូវបំលែងឈ្មោះឧបករណ៍ អាគុយម៉ង់ និងធានាថាអាគុយម៉ង់ត្រូវត្រូវសម្រាប់ឧបករណ៍។ អ្នកអាចផ្ទៀងផ្ទាត់អាគុយម៉ង់ក្នុងមុខងារនេះ ឬក្នុងឧបករណ៍ផ្ទាល់។

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools គឺជាឌិចស្យូណារីដែលមានឈ្មោះឧបករណ៍ជាគូនខ្នង
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

នេះគឺជា​អ្វី​ដែលកើតឡើង៖

- ឈ្មោះឧបករណ៍មានស្រាប់ជាប៉ារ៉ាម៉ែត្រ `name` ដែលមានរូបមន្តក្នុង អាគុយម៉ង់ជា `arguments`។

- ឧបករណ៍ត្រូវបានហៅជាមួយ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`។ ការផ្ទៀងផ្ទាត់អាគុយម៉ង់ប្រព្រឹត្តនៅក្នុងគុណលក្ខណៈ `handler` ដែលបង្ហាញមុខងារ ប្រសិនបើខ្វះវានឹងបញ្ចេញករណីកំហុស។

ឥឡូវនេះ យើងបានយល់ព្រមច្បាស់ពីការរាយបញ្ជី និងហៅឧបករណ៍ដោយប្រើម៉ាស៊ីនមេកម្រិតទាប។

មើល [ឧទាហរណ៍ពេញលេញ](./code/README.md) នៅទីនេះ

## ការចាត់តាំង

ពង្រីកកូដដែលអ្នកទទួលបានជាមួយឧបករណ៍ ស្រោមប្រើ និងការបញ្ជូន ជាច្រើន ហើយទស្សនាថា អ្នកត្រូវបញ្ចូលឯកសារតែក្នុងថត tools ប៉ុណ្ណោះ។

*មិនមានដំណោះស្រាយបង្ហាញ*

## សេចក្ដីសរុប

នៅក្នុងជំពូកនេះ យើងបានឃើញរបៀបម៉ាស៊ីនមេកម្រិតទាបដំណើរការ ហើយវាអាចជួយបង្កើតសំណង់រចនាសម្ព័ន្ធល្អដែលអាចអភិវឌ្ឍបាន។ យើងក៏បានពិភាក្សាអំពីការផ្ទៀងផ្ទាត់ និងបង្ហាញពីវិធីនៃការប្រើបណ្ណាល័យផ្ទៀងផ្ទាត់ដើម្បីបង្កើត schema សម្រាប់ការផ្ទៀងផ្ទាត់នាំចូល។

## តើអ្វីទៅបន្ទាប់

- បន្ទាប់៖ [ការផ្ទៀងផ្ទាត់ជា​សាមញ្ញ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->