# جدید سرور کا استعمال

MCP SDK میں دو مختلف قسم کے سرور دستیاب ہیں، آپ کا معمول کا سرور اور نچلے درجے کا سرور۔ عام طور پر، آپ معمول کے سرور کو فیچر شامل کرنے کے لیے استعمال کرتے ہیں۔ کچھ صورتوں میں، تاہم، آپ نچلے درجے کے سرور پر انحصار کرنا چاہتے ہیں جیسے:

- بہتر فن تعمیر۔ صاف فن تعمیر بنانا ممکن ہے دونوں معمول کے سرور اور نچلے درجے کے سرور کے ساتھ لیکن کہا جا سکتا ہے کہ نچلے درجے کے سرور کے ساتھ یہ تھوڑا آسان ہے۔
- فیچر دستیابی۔ کچھ جدید فیچرز صرف نچلے درجے کے سرور کے ساتھ استعمال کیے جا سکتے ہیں۔ آپ بعد کے ابواب میں سیمپلنگ اور ایلیسیٹیشن شامل کرتے ہوئے اسے دیکھیں گے۔

## معمول کا سرور بمقابلہ نچلے درجے کا سرور

یہاں معمول کے سرور کے ساتھ MCP سرور بنانے کا طریقہ دکھایا گیا ہے

**Python**

```python
mcp = FastMCP("Demo")

# ایک جمع کرنے کا آلہ شامل کریں
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

// ایک اضافہ کرنے کا آلہ شامل کریں
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

مطلب یہ ہے کہ آپ واضح طور پر ہر ٹول، ریسورس یا پرامپٹ شامل کرتے ہیں جو آپ چاہتے ہیں کہ سرور کے پاس ہو۔ اس میں کوئی غلطی نہیں ہے۔  

### نچلے درجے کے سرور کا طریقہ

تاہم، جب آپ نچلے درجے کے سرور کا طریقہ استعمال کرتے ہیں تو آپ کو اسے مختلف طریقے سے سوچنا ہوگا۔ ہر ٹول کو رجسٹر کرنے کے بجائے، آپ فیچر کے ہر قسم (ٹولز، ریسورسز یا پرامپٹس) کے لیے دو ہینڈلرز بناتے ہیں۔ مثال کے طور پر ٹولز کے لیے صرف دو فنکشن ہوتے ہیں:

- تمام ٹولز کی فہرست بنانا۔ ایک فنکشن تمام کوششوں کے لیے ذمے دار ہوتا ہے کہ ٹولز کی فہرست بنائے۔
- تمام ٹولز کو کال کرنے کی ہینڈلنگ۔ یہاں بھی، صرف ایک فنکشن ٹول کو کال کرنے کا کام سنبھالتا ہے۔

یہ کم کام لگتا ہے، ہے نا؟ تو ٹول رجسٹر کرنے کے بجائے مجھے بس یہ یقینی بنانا ہے کہ جب میں تمام ٹولز کی فہرست بناؤں تو وہ لسٹ میں ہو اور جب ٹول کال کرنے کی درخواست آئے تو وہ کال ہو جائے۔

آئیے دیکھتے ہیں اب کوڈ کیسا لگتا ہے:

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
  // رجسٹرڈ آلات کی فہرست واپس کریں
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

یہاں ہمارے پاس ایک فنکشن ہے جو فیچرز کی فہرست واپس کرتا ہے۔ ٹولز کی لسٹ میں اب ہر انٹری میں فیلڈز جیسے `name`، `description` اور `inputSchema` ہوتے ہیں تاکہ ریٹرن ٹائپ کے مطابق ہو۔ یہ ہمیں اپنے ٹولز اور فیچر کی تعریف کہیں اور رکھنے کی اجازت دیتا ہے۔ ہم اب اپنے تمام ٹولز کو tools فولڈر میں بنا سکتے ہیں اور اسی طرح آپ کے تمام فیچرز کے لیے بھی، اس طرح آپ کا پروجیکٹ اس طرح منظم ہو سکتا ہے:

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

یہ بہت اچھا ہے، ہماری فن تعمیر کو صاف اور منظم بنایا جا سکتا ہے۔

ٹولز کو کال کرنا کیسا ہے، کیا یہی خیال ہے، ایک ہینڈلر جو کسی بھی ٹول کو کال کرے؟ جی ہاں بالکل، یہ کوڈ ہے:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ایک لغت ہے جس کی چابیاں اوزاروں کے نام ہیں
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
    
    // args: درخواست.params.arguments
    // TODO ٹول کو کال کریں،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

اوپر کے کوڈ سے آپ دیکھ سکتے ہیں، ہمیں یہ پارس کرنا ہے کہ ٹول کون سا کال کرنا ہے اور کن دلائل کے ساتھ، پھر ہمیں ٹول کو کال کرنا ہوتا ہے۔

## ویلیڈیشن کے ساتھ طریقہ کار کو بہتر بنانا

اب تک آپ نے دیکھا کہ ٹولز، ریسورسز اور پرامپٹس شامل کرنے کے لیے آپ کی تمام رجسٹریشن کو ہر فیچر ٹائپ کے لیے دو ہینڈلرز سے تبدیل کیا جا سکتا ہے۔ اور کیا کرنا ہے؟ ہمیں کچھ فارم کی ویلیڈیشن شامل کرنی چاہیے تاکہ یہ یقینی بنایا جا سکے کہ ٹول کو درست دلائل کے ساتھ کال کیا جا رہا ہے۔ ہر رن ٹائم کی اپنی حل ہے، مثلاً Python Pydantic استعمال کرتا ہے اور TypeScript Zod۔ خیال یہ ہے کہ ہم یہ کریں:

- فیچر (ٹول، ریسورس یا پرامپٹ) بنانے کا منطق اس کے مخصوص فولڈر میں منتقل کریں۔
- آنے والی درخواست کی ویلیڈیشن کا طریقہ شامل کریں، مثلاً ٹول کال کرنے کی درخواست۔

### فیچر تخلیق کریں

فیچر بنانے کے لیے ہمیں اس فیچر کے لیے ایک فائل بنانا ہوگی اور یقینی بنانا ہوگا کہ اس میں اس فیچر کے لیے ضروری فیلڈز ہوں۔ یہ فیلڈز ٹولز، ریسورسز اور پرامپٹس میں تھوڑے مختلف ہوتے ہیں۔

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
        # پیرڈانٹک ماڈل کا استعمال کرتے ہوئے ان پٹ کی توثیق کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: پیرڈانٹک شامل کریں، تاکہ ہم ایک AddInputModel بنا سکیں اور آرگز کی توثیق کر سکیں

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

یہاں آپ دیکھ سکتے ہیں کہ ہم یہ کرتے ہیں:

- Pydantic `AddInputModel` اسکیمہ بناتے ہیں جس میں فیلڈز `a` اور `b` ہوتے ہیں، فائل *schema.py* میں۔
- آنے والی درخواست کو `AddInputModel` کی قسم میں پارس کرنے کی کوشش کرتے ہیں، اگر پیرامیٹرز میں کوئی تضاد ہو تو یہ کریش کر جائے گا:

   ```python
   # add.py
    try:
        # Pydantic ماڈل کا استعمال کرتے ہوئے ان پٹ کی تصدیق کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

آپ یہ منتخب کر سکتے ہیں کہ یہ پارسنگ لاجک ٹول کال میں رکھیں یا ہینڈلر فنکشن میں۔

**TypeScript**

```typescript
// سرور.ts
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

       // @ts-نظر انداز کریں
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

// سکیمہ.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// شامل کریں.ts
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

- تمام ٹول کالز سے نمٹنے والے ہینڈلر میں ہم آنے والی درخواست کو ٹول کے متعین کردہ اسکیمہ میں پارس کرنے کی کوشش کرتے ہیں:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    اگر یہ کامیاب ہو جائے تو ہم اصل ٹول کو کال کرتے ہیں:

    ```typescript
    const result = await tool.callback(input);
    ```

جیسا کہ آپ دیکھ سکتے ہیں، یہ طریقہ کار ایک خوبصورت فن تعمیر بناتا ہے کیونکہ ہر چیز اپنی جگہ ہوتی ہے، *server.ts* ایک بہت چھوٹی فائل ہے جو صرف ریکویسٹ ہینڈلرز کو جوڑتی ہے اور ہر فیچر اپنے متعلقہ فولڈر میں ہوتا ہے یعنی tools/، resources/ یا prompts/۔

اچھا ہے، اب اگلی چیز بنانے کی کوشش کرتے ہیں۔ 

## مشق: نچلے درجے کا سرور بنانا

اس مشق میں ہم یہ کریں گے:

1. ایک نچلے درجے کا سرور بنائیں جو ٹولز کی فہرست بنانا اور ٹولز کو کال کرنا سنبھالے۔
2. ایک ایسی فن تعمیر نافذ کریں جس پر آپ آگے تعمیر کر سکیں۔
3. ویلیڈیشن شامل کریں تاکہ یہ یقینی بنایا جا سکے کہ آپ کی ٹول کالز مناسب طریقے سے ویلیڈیٹ ہوں۔

### -1- فن تعمیر بنائیں

پہلی چیز یہ ہے کہ ایک ایسی فن تعمیر بنائیں جو ہمیں آسانی سے نئی خصوصیات شامل کرنے میں مدد دے، یہ اس طرح دکھائی دیتی ہے:

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

اب ہم نے ایسی فن تعمیر ترتیب دی ہے جو ہمیں آسانی سے tools فولڈر میں نئے ٹول شامل کرنے کی اجازت دیتی ہے۔ آپ آزاد ہیں کہ resources اور prompts کے لیے سب فولڈرز بھی بنائیں۔

### -2- ایک ٹول بنائیں

آئیے دیکھتے ہیں کہ ایک ٹول بنانا کیسا ہے۔ سب سے پہلے، یہ اپنے *tool* سب ڈائریکٹری میں ہونا چاہیے اس طرح:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ان پٹ کی تصدیق Pydantic ماڈل کا استعمال کرتے ہوئے کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic شامل کریں، تاکہ ہم AddInputModel بنا سکیں اور دلائل کی تصدیق کر سکیں

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

یہاں ہم دیکھتے ہیں کہ کیسے ہم Pydantic کا استعمال کرتے ہوئے نام، وضاحت اور ان پٹ اسکیمہ کی تعریف کرتے ہیں اور ایک ہینڈلر جو کال کرنے پر چلے گا۔ آخر میں، ہم `tool_add` کو ایک ڈکشنری کے طور پر ظاہر کرتے ہیں جو یہ تمام خصوصیات رکھتی ہے۔

اس کے ساتھ *schema.py* بھی ہے جہاں ہم ان پٹ اسکیمہ کی تعریف کرتے ہیں جو ہمارے ٹول کے لیے استعمال ہوتا ہے:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ہمیں *__init__.py* کو بھی بھرنا ہے تاکہ tools ڈائریکٹری کو ماڈیول کے طور پر تسلیم کیا جا سکے۔ علاوہ ازیں، ہمیں اس کے اندر ماڈیولز کو اس طرح ظاہر کرنا ہوگا:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

جیسے جیسے ہم مزید ٹولز شامل کریں گے ہم اس فائل میں بھی اضافہ کرتے رہ سکتے ہیں۔

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

یہاں ہم خصوصیات پر مشتمل ایک ڈکشنری بناتے ہیں:

- name، یہ ٹول کا نام ہے۔
- rawSchema، یہ Zod اسکیمہ ہے، جو آنے والی درخواستوں کو اس ٹول کو کال کرنے کے لیے ویلیڈیٹ کرے گا۔
- inputSchema، یہ اسکیمہ ہینڈلر کے لیے استعمال ہوگا۔
- callback، یہ ٹول کو چلانے کے لیے استعمال ہوتا ہے۔

اس کے ساتھ `Tool` بھی ہے جو یہ ڈکشنری MCP سرور ہینڈلر کے قابل قبول ٹائپ میں تبدیل کرتا ہے اور یہ اس طرح دکھائی دیتا ہے:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

اور *schema.ts* بھی ہے جہاں ہم ہر ٹول کے ان پٹ اسکیمہ رکھ سکتے ہیں، فی الحال صرف ایک اسکیمہ ہے لیکن جیسے جیسے ہم اور ٹولز شامل کریں گے مزید انٹریز بھی شامل کر سکیں گے:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

اچھا، اب ہم ٹولز کی فہرست سنبھالنے کے لیے آگے بڑھتے ہیں۔

### -3- ٹول کی فہرست کو سنبھالنا

اگلے مرحلے میں، ٹولز کی فہرست بنانے کے لیے ہمیں ایک ریکویسٹ ہینڈلر بنانا ہوگا۔ یہ وہ چیز ہے جو ہمیں اپنی سرور فائل میں شامل کرنی ہے:

**Python**

```python
# کوڈ مختصر کرنے کے لیے حذف کر دیا گیا ہے
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

یہاں ہم `@server.list_tools` ڈیکوریٹر اور اس کے نفاذ کے لیے `handle_list_tools` فنکشن شامل کرتے ہیں۔ اس میں ہمیں ٹولز کی فہرست بنانی ہوتی ہے۔ نوٹ کریں کہ ہر ٹول کا نام، وضاحت اور inputSchema ہونا چاہیے۔   

**TypeScript**

ٹولز کی فہرست بنانے کے لیے ریکویسٹ ہینڈلر سیٹ کرنے کے لیے، ہمیں سرور پر `setRequestHandler` کال کرنی ہے جس کی اسکیمہ اس مقصد کے مطابق ہو، اس معاملے میں `ListToolsRequestSchema`۔

```typescript
// انڈیکس.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// سرور.ts
// کوڈ کو مختصر کرنے کے لیے چھوڑ دیا گیا
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // رجسٹرڈ ٹولز کی فہرست واپس کریں
  return {
    tools: tools
  };
});
```

عظیم، اب ہم نے ٹولز کی فہرست بنانے کا حصہ حل کر لیا، آئیے دیکھتے ہیں کہ ٹولز کو کال کیسے کیا جا سکتا ہے۔

### -4- ٹول کال کو سنبھالنا

ایک ٹول کو کال کرنے کے لیے، ہمیں ایک اور ریکویسٹ ہینڈلر قائم کرنا ہوگا جو یہ دیکھے کہ کون سا فیچر کال کرنا ہے اور کس دلائل کے ساتھ۔

**Python**

آئیے `@server.call_tool` ڈیکوریٹر استعمال کریں اور `handle_call_tool` کے فنکشن سے اسے نافذ کریں۔ اس فنکشن میں، ہمیں ٹول کا نام، اس کا ارگیومنٹ پارس کرنا ہوگا اور یہ یقینی بنانا ہوگا کہ ارگیومنٹس اس ٹول کے لیے درست ہیں۔ ہم ارگیومنٹس کی ویلیڈیشن یا تو اس فنکشن میں کر سکتے ہیں یا اصل ٹول کے اندر۔

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ایک لغت ہے جس میں ٹول کے نام چابیاں ہیں
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ٹول کو چلائیں
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

یہاں کیا ہوتا ہے:

- ہمارا ٹول نام ان پٹ پیرامیٹر `name` کے طور پر موجود ہے جو ہمارے ارگیومنٹس `arguments` ڈکشنری کی صورت میں بھی ہے۔

- ٹول `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` کے ساتھ کال کیا جاتا ہے۔ ارگیومنٹس کی ویلیڈیشن `handler` پراپرٹی میں ہوتی ہے جو ایک فنکشن کی طرف اشارہ کرتی ہے، اگر یہ ناکام رہتا ہے تو ایک استثناء پھینکے گا۔

تو اب ہمارے پاس نچلے درجے کے سرور کا استعمال کرتے ہوئے ٹولز کی فہرست بنانے اور کال کرنے کا مکمل فہم ہے۔

مکمل مثال دیکھیں: [full example](./code/README.md)

## اسائنمنٹ

آپ کو دیا گیا کوڈ کئی ٹولز، ریسورسز اور پرامپٹس کے ساتھ توسیع دیں اور غور کریں کہ آپ کو صرف tools ڈائریکٹری میں فائلز شامل کرنی پڑتی ہیں اور کہیں اور نہیں۔

*کوئی حل مہیا نہیں کیا گیا*

## خلاصہ

اس باب میں، ہم نے دیکھا کہ نچلے درجے کے سرور کا طریقہ کیسے کام کرتا ہے اور کیسے یہ ہمیں ایک اچھی فن تعمیر بنانے میں مدد دیتا ہے جس پر ہم مسلسل بنا سکتے ہیں۔ ہم نے ویلیڈیشن پر بھی بات کی اور آپ کو دکھایا گیا کہ آپ کس طرح ویلیڈیشن لائبریریاں استعمال کر کے ان پٹ ویلیڈیشن کے لیے اسکیمہ بنا سکتے ہیں۔

## آگے کیا ہے

- اگلا: [سادہ توثیق](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لئے کام کرتے ہیں، براہ کرم اس بات کا خیال رکھیں کہ خودکار ترجمے میں غلطیاں یا بے ضابطگیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->