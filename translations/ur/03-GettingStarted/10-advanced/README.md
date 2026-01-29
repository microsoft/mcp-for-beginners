# اعلی درجے کے سرور کا استعمال

MCP SDK میں دو مختلف قسم کے سرورز موجود ہیں: عام سرور اور لو لیول سرور۔ عام طور پر، آپ عام سرور کو استعمال کرتے ہیں تاکہ اس میں خصوصیات شامل کی جا سکیں۔ لیکن کچھ حالات میں، آپ کو لو لیول سرور پر انحصار کرنا پڑتا ہے، جیسے:

- بہتر آرکیٹیکچر۔ عام سرور اور لو لیول سرور دونوں کے ساتھ صاف ستھرا آرکیٹیکچر بنانا ممکن ہے، لیکن یہ کہا جا سکتا ہے کہ لو لیول سرور کے ساتھ یہ قدرے آسان ہے۔
- خصوصیات کی دستیابی۔ کچھ اعلی درجے کی خصوصیات صرف لو لیول سرور کے ساتھ استعمال کی جا سکتی ہیں۔ آپ بعد کے ابواب میں دیکھیں گے جب ہم سیمپلنگ اور ایلیسیٹیشن شامل کریں گے۔

## عام سرور بمقابلہ لو لیول سرور

یہاں یہ دکھایا گیا ہے کہ MCP سرور کو عام سرور کے ساتھ کیسے بنایا جاتا ہے:

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

بات یہ ہے کہ آپ واضح طور پر ہر وہ ٹول، ریسورس یا پرامپٹ شامل کرتے ہیں جو آپ چاہتے ہیں کہ سرور میں موجود ہو۔ اس میں کوئی مسئلہ نہیں۔

### لو لیول سرور کا طریقہ

تاہم، جب آپ لو لیول سرور کا طریقہ استعمال کرتے ہیں تو آپ کو مختلف انداز میں سوچنا پڑتا ہے۔ یعنی، ہر ٹول کو رجسٹر کرنے کے بجائے، آپ فیچر کی قسم (ٹولز، ریسورسز یا پرامپٹس) کے لیے دو ہینڈلرز بناتے ہیں۔ مثال کے طور پر، ٹولز کے لیے صرف دو فنکشنز ہوتے ہیں، جیسے:

- تمام ٹولز کی فہرست بنانا۔ ایک فنکشن تمام کوششوں کے لیے ذمہ دار ہوگا جو ٹولز کی فہرست بنانے کے لیے کی جاتی ہیں۔
- تمام ٹولز کو کال کرنے کا ہینڈل۔ یہاں بھی، صرف ایک فنکشن ٹول کو کال کرنے کی درخواستوں کو ہینڈل کرتا ہے۔

یہ کم کام لگتا ہے، ٹھیک ہے؟ تو، ٹول کو رجسٹر کرنے کے بجائے، مجھے صرف یہ یقینی بنانا ہوگا کہ ٹول اس وقت فہرست میں شامل ہو جب میں تمام ٹولز کی فہرست بناتا ہوں اور یہ کہ اسے کال کیا جائے جب کوئی درخواست آتی ہے۔

آئیے دیکھتے ہیں کہ کوڈ اب کیسا لگتا ہے:

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

یہاں ہمارے پاس ایک فنکشن ہے جو فیچرز کی فہرست واپس کرتا ہے۔ ٹولز کی فہرست میں ہر اندراج میں اب `name`، `description` اور `inputSchema` جیسے فیلڈز ہیں تاکہ ریٹرن ٹائپ کے مطابق ہو۔ اس سے ہمیں اپنے ٹولز اور فیچر ڈیفینیشن کو کہیں اور رکھنے کی سہولت ملتی ہے۔ ہم اب اپنے تمام ٹولز کو ایک ٹولز فولڈر میں بنا سکتے ہیں اور یہی بات آپ کے تمام فیچرز کے لیے بھی لاگو ہوتی ہے، تاکہ آپ کا پروجیکٹ اچانک اس طرح منظم ہو سکے:

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

یہ زبردست ہے، ہمارا آرکیٹیکچر کافی صاف ستھرا نظر آ سکتا ہے۔

ٹولز کو کال کرنے کے بارے میں کیا خیال ہے؟ کیا یہ بھی وہی آئیڈیا ہے، ایک ہینڈلر جو کسی بھی ٹول کو کال کرے؟ جی ہاں، بالکل، اس کے لیے کوڈ یہ ہے:

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

جیسا کہ آپ اوپر کے کوڈ سے دیکھ سکتے ہیں، ہمیں یہ معلوم کرنا ہوگا کہ کون سا ٹول کال کرنا ہے، کس آرگومنٹس کے ساتھ، اور پھر ہمیں ٹول کو کال کرنے کے لیے آگے بڑھنا ہوگا۔

## طریقہ کار کو ویلیڈیشن کے ساتھ بہتر بنانا

اب تک، آپ نے دیکھا کہ ٹولز، ریسورسز اور پرامپٹس شامل کرنے کے لیے آپ کی تمام رجسٹریشنز کو فیچر کی قسم کے لیے ان دو ہینڈلرز کے ساتھ تبدیل کیا جا سکتا ہے۔ ہمیں اور کیا کرنا چاہیے؟ ٹھیک ہے، ہمیں کسی قسم کی ویلیڈیشن شامل کرنی چاہیے تاکہ یہ یقینی بنایا جا سکے کہ ٹول کو صحیح آرگومنٹس کے ساتھ کال کیا جا رہا ہے۔ ہر رن ٹائم کے پاس اس کے لیے اپنا حل ہوتا ہے، مثال کے طور پر Python میں Pydantic استعمال ہوتا ہے اور TypeScript میں Zod۔ آئیڈیا یہ ہے کہ ہم درج ذیل کریں:

- فیچر (ٹول، ریسورس یا پرامپٹ) بنانے کی منطق کو اس کے مخصوص فولڈر میں منتقل کریں۔
- آنے والی درخواست کو ویلیڈیٹ کرنے کا طریقہ شامل کریں، جیسے کہ ٹول کو کال کرنے کی درخواست۔

### فیچر بنانا

فیچر بنانے کے لیے، ہمیں اس فیچر کے لیے ایک فائل بنانی ہوگی اور یہ یقینی بنانا ہوگا کہ اس میں اس فیچر کے لیے مطلوبہ فیلڈز موجود ہوں۔ یہ فیلڈز ٹولز، ریسورسز اور پرامپٹس کے درمیان تھوڑا مختلف ہوتے ہیں۔

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

یہاں آپ دیکھ سکتے ہیں کہ ہم درج ذیل کرتے ہیں:

- Pydantic `AddInputModel` کا استعمال کرتے ہوئے ایک اسکیمہ بناتے ہیں جس میں فیلڈز `a` اور `b` ہیں، فائل *schema.py* میں۔
- آنے والی درخواست کو `AddInputModel` کی قسم میں تبدیل کرنے کی کوشش کرتے ہیں، اگر پیرامیٹرز میں کوئی عدم مطابقت ہو تو یہ کریش ہو جائے گا:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

آپ یہ انتخاب کر سکتے ہیں کہ آیا اس پارسنگ منطق کو خود ٹول کال میں رکھیں یا ہینڈلر فنکشن میں۔

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

- ہینڈلر میں جو تمام ٹول کالز کو ہینڈل کرتا ہے، ہم اب آنے والی درخواست کو ٹول کے ڈیفائن کردہ اسکیمہ میں تبدیل کرنے کی کوشش کرتے ہیں:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    اگر یہ کام کرتا ہے تو ہم اصل ٹول کو کال کرنے کے لیے آگے بڑھتے ہیں:

    ```typescript
    const result = await tool.callback(input);
    ```

جیسا کہ آپ دیکھ سکتے ہیں، یہ طریقہ کار ایک بہترین آرکیٹیکچر بناتا ہے کیونکہ ہر چیز اپنی جگہ پر ہوتی ہے، *server.ts* ایک بہت چھوٹی فائل ہے جو صرف درخواست ہینڈلرز کو وائر اپ کرتی ہے اور ہر فیچر اپنے متعلقہ فولڈر میں ہوتا ہے، جیسے tools/, resources/ یا /prompts۔

زبردست، آئیے اسے بنانے کی کوشش کرتے ہیں۔

## مشق: لو لیول سرور بنانا

اس مشق میں، ہم درج ذیل کریں گے:

1. ایک لو لیول سرور بنائیں جو ٹولز کی فہرست بنانے اور ٹولز کو کال کرنے کو ہینڈل کرے۔
1. ایک آرکیٹیکچر نافذ کریں جس پر آپ کام کر سکیں۔
1. ویلیڈیشن شامل کریں تاکہ یہ یقینی بنایا جا سکے کہ آپ کے ٹول کالز مناسب طریقے سے ویلیڈیٹ کیے گئے ہیں۔

### -1- ایک آرکیٹیکچر بنائیں

سب سے پہلے ہمیں ایک آرکیٹیکچر کو حل کرنا ہوگا جو ہمیں مزید فیچرز شامل کرنے کے ساتھ اسکیل کرنے میں مدد دے، یہ اس طرح نظر آتا ہے:

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

اب ہم نے ایک آرکیٹیکچر سیٹ اپ کر لیا ہے جو یہ یقینی بناتا ہے کہ ہم آسانی سے ٹولز فولڈر میں نئے ٹولز شامل کر سکتے ہیں۔ آپ ریسورسز اور پرامپٹس کے لیے سب ڈائریکٹریز شامل کرنے کے لیے آزاد ہیں۔

### -2- ایک ٹول بنانا

آئیے دیکھتے ہیں کہ اگلا ٹول بنانا کیسا لگتا ہے۔ سب سے پہلے، اسے اپنے *tool* سب ڈائریکٹری میں اس طرح بنایا جانا چاہیے:

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

یہاں ہم دیکھتے ہیں کہ ہم نام، تفصیل، Pydantic کا استعمال کرتے ہوئے ایک ان پٹ اسکیمہ اور ایک ہینڈلر ڈیفائن کرتے ہیں جو اس وقت کال کیا جائے گا جب یہ ٹول کال کیا جا رہا ہو۔ آخر میں، ہم `tool_add` کو ایک ڈکشنری کے طور پر ظاہر کرتے ہیں جس میں یہ تمام پراپرٹیز موجود ہیں۔

اس کے علاوہ *schema.py* بھی ہے جو ہمارے ٹول کے لیے استعمال ہونے والے ان پٹ اسکیمہ کو ڈیفائن کرتا ہے:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ہمیں *__init__.py* کو بھی پاپولیٹ کرنے کی ضرورت ہے تاکہ ٹولز ڈائریکٹری کو ایک ماڈیول کے طور پر ٹریٹ کیا جا سکے۔ اضافی طور پر، ہمیں اس میں موجود ماڈیولز کو اس طرح ظاہر کرنے کی ضرورت ہے:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ہم اس فائل میں مزید ٹولز شامل کرتے ہوئے اضافہ کر سکتے ہیں۔

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

یہاں ہم پراپرٹیز پر مشتمل ایک ڈکشنری بناتے ہیں:

- name، یہ ٹول کا نام ہے۔
- rawSchema، یہ Zod اسکیمہ ہے، یہ آنے والی درخواستوں کو ویلیڈیٹ کرنے کے لیے استعمال ہوگا۔
- inputSchema، یہ اسکیمہ ہینڈلر کے ذریعے استعمال ہوگا۔
- callback، یہ ٹول کو کال کرنے کے لیے استعمال ہوتا ہے۔

یہاں `Tool` بھی ہے جو اس ڈکشنری کو ایک قسم میں تبدیل کرتا ہے جسے mcp سرور ہینڈلر قبول کر سکتا ہے اور یہ اس طرح نظر آتا ہے:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

اور *schema.ts* ہے جہاں ہم ہر ٹول کے لیے ان پٹ اسکیمہ اسٹور کرتے ہیں، جو اس وقت صرف ایک اسکیمہ پر مشتمل ہے لیکن جیسے جیسے ہم ٹولز شامل کرتے ہیں، ہم مزید اندراجات شامل کر سکتے ہیں:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

زبردست، آئیے اگلے مرحلے میں اپنے ٹولز کی فہرست بنانے کو ہینڈل کریں۔

### -3- ٹولز کی فہرست بنانا

اگلا، ٹولز کی فہرست بنانے کو ہینڈل کرنے کے لیے، ہمیں اپنے سرور فائل میں ایک درخواست ہینڈلر سیٹ اپ کرنے کی ضرورت ہے:

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

یہاں ہم `@server.list_tools` ڈیکوریٹر اور `handle_list_tools` فنکشن شامل کرتے ہیں۔ مؤخر الذکر میں، ہمیں ٹولز کی ایک فہرست تیار کرنی ہوگی۔ نوٹ کریں کہ ہر ٹول میں نام، تفصیل اور inputSchema ہونا ضروری ہے۔

**TypeScript**

ٹولز کی فہرست بنانے کے لیے درخواست ہینڈلر سیٹ اپ کرنے کے لیے، ہمیں `setRequestHandler` کو سرور پر کال کرنے کی ضرورت ہے، جس میں ایک اسکیمہ ہو جو ہم کرنے کی کوشش کر رہے ہیں، اس معاملے میں `ListToolsRequestSchema`۔

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

زبردست، اب ہم نے ٹولز کی فہرست بنانے کا مسئلہ حل کر لیا ہے، آئیے دیکھتے ہیں کہ اگلے مرحلے میں ٹولز کو کال کرنا کیسا لگتا ہے۔

### -4- ٹول کو کال کرنا

ٹول کو کال کرنے کے لیے، ہمیں ایک اور درخواست ہینڈلر سیٹ اپ کرنے کی ضرورت ہے، اس بار ایک درخواست کو ہینڈل کرنے پر توجہ مرکوز کرتے ہوئے جو یہ بتاتی ہے کہ کون سا فیچر کال کرنا ہے اور کس آرگومنٹس کے ساتھ۔

**Python**

آئیے `@server.call_tool` ڈیکوریٹر استعمال کریں اور اسے `handle_call_tool` فنکشن کے ساتھ نافذ کریں۔ اس فنکشن کے اندر، ہمیں ٹول کا نام، اس کے آرگومنٹس کو معلوم کرنا ہوگا اور یہ یقینی بنانا ہوگا کہ آرگومنٹس متعلقہ ٹول کے لیے درست ہیں۔ ہم آرگومنٹس کو اس فنکشن میں یا نیچے کی سطح پر اصل ٹول میں ویلیڈیٹ کر سکتے ہیں۔

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

یہاں کیا ہوتا ہے:

- ہمارا ٹول نام پہلے ہی ان پٹ پیرامیٹر `name` کے طور پر موجود ہے، جو ہمارے آرگومنٹس کے لیے بھی درست ہے، جو `arguments` ڈکشنری کی شکل میں ہیں۔

- ٹول کو `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` کے ساتھ کال کیا جاتا ہے۔ آرگومنٹس کی ویلیڈیشن `handler` پراپرٹی میں ہوتی ہے جو ایک فنکشن کی طرف اشارہ کرتی ہے، اگر یہ ناکام ہو جائے تو یہ ایک استثنا پیدا کرے گا۔

یہاں، اب ہمیں لو لیول سرور کا استعمال کرتے ہوئے ٹولز کی فہرست بنانے اور کال کرنے کی مکمل سمجھ ہے۔

[مکمل مثال](./code/README.md) یہاں دیکھیں

## اسائنمنٹ

آپ کو دیے گئے کوڈ کو متعدد ٹولز، ریسورسز اور پرامپٹس کے ساتھ بڑھائیں اور غور کریں کہ آپ کو صرف ٹولز ڈائریکٹری میں فائلز شامل کرنے کی ضرورت ہے اور کہیں اور نہیں۔

*کوئی حل فراہم نہیں کیا گیا*

## خلاصہ

اس باب میں، ہم نے دیکھا کہ لو لیول سرور کا طریقہ کیسے کام کرتا ہے اور یہ کیسے ہمیں ایک اچھا آرکیٹیکچر بنانے میں مدد دے سکتا ہے جس پر ہم کام کرتے رہ سکتے ہیں۔ ہم نے ویلیڈیشن پر بھی بات کی اور آپ کو دکھایا کہ ان پٹ ویلیڈیشن کے لیے اسکیمہ بنانے کے لیے ویلیڈیشن لائبریریوں کے ساتھ کیسے کام کیا جائے۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔