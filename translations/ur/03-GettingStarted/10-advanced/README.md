# اعلی درجے کے سرور کا استعمال

MCP SDK میں دو مختلف قسم کے سرورز دستیاب ہیں، آپ کا معمول کا سرور اور کم سطح کا سرور۔ عموماً، آپ اضافی خصوصیات شامل کرنے کے لیے معمول کا سرور استعمال کریں گے۔ بعض صورتوں میں، آپ کم سطح کے سرور پر انحصار کرنا چاہتے ہیں جیسے:

- بہتر معماری۔ صاف ستھری معماری بنانے کے لئے دونوں معمول کے سرور اور کم سطح کے سرور کا استعمال ممکن ہے لیکن کہا جا سکتا ہے کہ کم سطح کے سرور کے ساتھ یہ کچھ آسان ہوتا ہے۔
- خصوصیات کی دستیابی۔ کچھ اعلی خصوصیات صرف کم سطح کے سرور کے ساتھ استعمال کی جا سکتی ہیں۔ آپ اسے آگے کے ابواب میں دیکھیں گے جب ہم سیمپلنگ اور ایلیسیٹیشن شامل کریں گے۔

## معمول کا سرور بمقابلہ کم سطح کا سرور

یہاں MCP سرور کی تخلیق معمول کے سرور کے ساتھ کیسی لگتی ہے:

**Python**

```python
mcp = FastMCP("Demo")

# ایک اضافہ کا آلہ شامل کریں
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

// ایک اضافی آلہ شامل کریں
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

مدعا یہ ہے کہ آپ وضاحت کے ساتھ ہر ٹول، ریسورس یا پرامپٹ شامل کرتے ہیں جسے آپ سرور میں شامل کرنا چاہتے ہیں۔ اس میں کوئی مسئلہ نہیں ہے۔

### کم سطح کے سرور کا طریقہ کار

تاہم، جب آپ کم سطح کے سرور کا طریقہ استعمال کرتے ہیں تو آپ کو مختلف سوچنا پڑتا ہے۔ ہر ٹول کو رجسٹر کرنے کے بجائے، آپ فیچر کی قسم (ٹولز، ریسورسز یا پرامپٹس) کے لیے دو ہینڈلرز بناتے ہیں۔ تو مثلاً ٹولز کے لیے صرف دو فنکشن ہوتے ہیں، جیسے:

- تمام ٹولز کی فہرست بنانا۔ ایک فنکشن تمام کوششوں کے لیے ذمہ دار ہوتا ہے کہ ٹولز کی فہرست بنائے۔
- تمام ٹولز کو کال کرنے کا ہینڈل۔ یہاں بھی صرف ایک فنکشن ہے جو کسی ٹول کو کال کرنے کو ہینڈل کرتا ہے۔

یہ ممکنہ طور پر کم کام لگتا ہے، درست؟ تو ایک ٹول رجسٹر کرنے کے بجائے مجھے صرف یہ یقینی بنانا ہے کہ ٹولز کی فہرست میں وہ شامل ہو اور جب کسی درخواست میں ٹول کال کرنے کو کہا جائے تو اسے کال کیا جائے۔

اب دیکھتے ہیں کوڈ کیسا لگتا ہے:

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
  // رجسٹرڈ ٹولز کی فہرست واپس کریں
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

یہاں ہمارے پاس ایک فنکشن ہے جو فیچرز کی فہرست لوٹاتا ہے۔ ٹولز کی فہرست میں ہر اندراج میں اب `name`, `description` اور `inputSchema` جیسے فیلڈز ہوتے ہیں تاکہ ریٹرن ٹائپ کی پابندی ہو۔ اس طرح ہم اپنی ٹولز اور فیچر کی تعریف کہیں اور رکھ سکتے ہیں۔ اب ہم تمام ٹولز کو tools فولڈر میں بنا سکتے ہیں اور یہی بات آپ کے تمام فیچرز پر لاگو ہوتی ہے تاکہ آپ کا پروجیکٹ اچانک اس طرح منظم ہو جائے:

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

یہ بہت اچھا ہے، ہماری معماری کافی صاف ستھری بن سکتی ہے۔

اب ٹولز کال کرنے کی کیا حالت ہے؟ کیا اب بھی ایک ہی ہینڈلر ہوتا ہے جو کسی بھی ٹول کو کال کرتا ہے؟ جی ہاں، بالکل، یہ کوڈ ہے:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ایک لغت ہے جس میں ٹول کے نام کلیدوں کے طور پر ہیں
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
    
    // ارگس: request.params.arguments
    // کرنے کے لیے آلے کو کال کریں،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

جیسا کہ آپ اوپر والے کوڈ سے دیکھ سکتے ہیں، ہمیں یہ پارس کرنا ہے کہ کون سا ٹول کال کرنا ہے، کون سے دلائل کے ساتھ، اور پھر ہمیں ٹول کال کرنے کے عمل کو آگے بڑھانا ہے۔

## توثیق کے ساتھ طریقہ کار کو بہتر بنانا

اب تک آپ نے دیکھا کہ آپ کی تمام رجسٹریشنیں ٹولز، ریسورسز اور پرامپٹس شامل کرنے کے لیے فیچر کی قسم کے لیے دو ہینڈلرز میں تبدیل کی جا سکتی ہیں۔ اب اور کیا کرنا چاہیے؟ ہمیں ٹول کو درست دلائل کے ساتھ کال کرنے کے لیے کچھ قسم کی توثیق شامل کرنی چاہیے۔ ہر رن ٹائم کا اپنا حل ہوتا ہے، مثلاً Python میں Pydantic اور TypeScript میں Zod استعمال ہوتا ہے۔ خیال یہ ہے کہ ہم درج ذیل کریں:

- کسی فیچر (ٹول، ریسورس یا پرامپٹ) بنانے کی منطق کو اس کے مخصوص فولڈر میں منتقل کریں۔
- کسی درخواست کی درستگی کو چیک کرنے کا طریقہ شامل کریں جو مثال کے طور پر ٹول کال کرنے کی درخواست کرتی ہے۔

### فیچر بنائیں

فیچر بنانے کے لیے، ہمیں اس فیچر کے لیے ایک فائل بنانی ہوگی اور یقینی بنانا ہوگا کہ اس میں لازمی فیلڈز موجود ہوں جو اس فیچر کے لیے درکار ہیں۔ جو فیلڈز مختلف ہو سکتے ہیں وہ ٹولز، ریسورسز اور پرامپٹس میں فرق کر سکتے ہیں۔

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
        # ان پٹ کی تصدیق کرنے کے لیے Pydantic ماڈل استعمال کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # کرنے کے لئے: Pydantic شامل کریں، تاکہ ہم AddInputModel بنا سکیں اور دلائل کی تصدیق کر سکیں

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

یہاں آپ دیکھ سکتے ہیں کہ ہم:

- Pydantic `AddInputModel` کا استعمال کرتے ہوئے schema بناتے ہیں جس میں فیلڈز `a` اور `b` ہیں، فائل *schema.py* میں۔
- آنے والی درخواست کو `AddInputModel` کی قسم میں پارس کرنے کی کوشش کرتے ہیں، اگر پیرامیٹرز میں کوئی مطابقت نہ ہو تو یہ کریش کر جائے گا:

   ```python
   # add.py
    try:
        # پائیڈینٹک ماڈل کا استعمال کرتے ہوئے ان پٹ کی تصدیق کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

آپ یہ پارس کرنے کی منطق ٹول کال میں بذات خود یا ہینڈلر فنکشن میں رکھ سکتے ہیں۔

**TypeScript**

```typescript
// سرور۔ٹی ایس
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

// سکیمہ۔ٹی ایس
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// شامل کریں۔ٹی ایس
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

- تمام ٹول کالز کو ہینڈل کرنے والے ہینڈلر میں ہم اب کوشش کرتے ہیں کہ آنے والی درخواست کو ٹول کی تعریف شدہ schema میں پارس کریں:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    اگر وہ کامیاب ہو جائے تو ہم اصل ٹول کو کال کرتے ہیں:

    ```typescript
    const result = await tool.callback(input);
    ```

جیسا کہ آپ دیکھ سکتے ہیں، یہ طریقہ کار ایک اچھی معماری بناتا ہے کیونکہ ہر چیز کی اپنی جگہ ہے، *server.ts* بہت چھوٹی فائل ہے جو صرف درخواستوں کے ہینڈلرز کو مربوط کرتی ہے اور ہر فیچر اپنے فولڈر میں ہوتا ہے یعنی tools/, resources/ یا /prompts۔

شاباش، اب اگلا مرحلہ بناتے ہیں۔

## مشق: کم سطح کا سرور بنانا

اس مشق میں، ہم درج ذیل کریں گے:

1. ایک کم سطح کا سرور بنائیں جو ٹولز کی فہرست اور کال کو ہینڈل کرے۔
2. ایک ایسی معماری نافذ کریں جس پر آپ مزید تعمیر کر سکیں۔
3. توثیق شامل کریں تاکہ یہ یقینی ہو کہ آپ کی ٹول کالز درست طریقے سے توثیق شدہ ہوں۔

### -1- ایک معماری بنائیں

سب سے پہلے ہمیں ایک ایسی معماری ترتیب دینی ہے جو ہمیں مزید فیچرز شامل کرنے میں مدد دے۔ یہ کچھ اس طرح ہوگا:

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

اب ہم نے ایک ایسی معماری قائم کی ہے جو یقینی بناتی ہے کہ ہم آسانی سے tools فولڈر میں نئے ٹولز شامل کر سکیں۔ آپ فیل کریں کہ resources اور prompts کے لیے سب ڈائریکٹریز بھی بنا لیں۔

### -2- ایک ٹول بنائیں

اب دیکھتے ہیں کہ ٹول بنانے کا کیا طریقہ ہے۔ سب سے پہلے اسے اپنے *tool* ذیلی ڈائریکٹری میں بنانا ہوگا جیسا کہ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # پائیڈانٹک ماڈل کا استعمال کرتے ہوئے ان پٹ کی تصدیق کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # کرنے کے لئے: پائیڈانٹک شامل کریں، تاکہ ہم AddInputModel بنا سکیں اور دلائل کی تصدیق کر سکیں

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

یہاں ہم دیکھتے ہیں کہ ہم کس طرح نام، وضاحت، اور ان پٹ اسکیمہ Pydantic کے ذریعے تعریف کرتے ہیں اور ایک ہینڈلر جو اس ٹول کے کال ہونے پر چلایا جائے گا۔ آخر میں، ہم `tool_add` ایک ڈکشنری کو ظاہر کرتے ہیں جو تمام پراپرٹیز رکھتی ہے۔

اسی طرح *schema.py* بھی ہے جو ان پٹ اسکیمہ کی تعریف کے لیے استعمال ہوتا ہے جو ہمارے ٹول کے لیے ہوتا ہے:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ہمیں *__init__.py* بھی بھرنا پڑتا ہے تاکہ tools ڈائریکٹری کو ماڈیول کے طور پر تسلیم کیا جائے۔ اس کے علاوہ، ہمیں ماڈیولز کو اس طرح ظاہر کرنا ہوتا ہے:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ہم اس فائل میں مزید ٹولز شامل کرنے کے ساتھ اضافہ جاری رکھ سکتے ہیں۔

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

یہاں ہم ایک ڈکشنری بناتے ہیں جس میں پراپرٹیز شامل ہیں:

- name، یہ ٹول کا نام ہے۔
- rawSchema، یہ Zod اسکیمہ ہے جو آنے والی درخواستوں کی توثیق کے لیے استعمال ہوتا ہے جو اس ٹول کو کال کرتی ہیں۔
- inputSchema، یہ اسکیمہ ہینڈلر کے لیے استعمال ہوتا ہے۔
- callback، یہ ٹول کو چلانے کے لیے استعمال ہوتا ہے۔

اس کے علاوہ `Tool` ہے جو اس ڈکشنری کو ایک ٹائپ میں تبدیل کرتا ہے جو mcp سرور ہینڈلر قبول کر سکتا ہے اور یہ کچھ اس طرح دکھائی دیتا ہے:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

اور *schema.ts* بھی ہے جہاں ہم ہر ٹول کے ان پٹ اسکیمہ رکھتے ہیں، فی الحال صرف ایک اسکیمہ کے ساتھ لیکن جب ہم مزید ٹولز شامل کریں گے تو مزید اندراجات بھی کر سکتے ہیں:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

زبردست، اب بڑھتے ہیں ٹولز کی فہرست بنانے کی طرف۔

### -3- ٹول کی فہرست سنبھالیں

اب، اپنی ٹولز کی فہرست سنبھالنے کے لیے، ہمیں ایک درخواست ہینڈلر ترتیب دینا ہوگا۔ یہاں ہم اپنے سرور فائل میں جو شامل کریں گے وہ ہے:

**Python**

```python
# کوڈ کو مختصر کرنے کے لیے حذف کر دیا گیا ہے
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

یہاں ہم `@server.list_tools` سجاوٹ (decorator) شامل کرتے ہیں اور فنکشن `handle_list_tools` لکھتے ہیں۔ اس کے اندر ہمیں ٹولز کی فہرست نکالنی ہوتی ہے۔ دھیان دیں کہ ہر ٹول میں نام، وضاحت اور inputSchema ہونا ضروری ہے۔

**TypeScript**

ٹولز کی فہرست کے لیے درخواست ہینڈلر ترتیب دینے کے لیے، ہمیں سرور پر `setRequestHandler` کال کرنی ہوگی جس میں وہ اسکیمہ ہو جو ہم لاگو کر رہے ہوں، اس کیس میں `ListToolsRequestSchema`۔

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
// کوڈ مختصر کرنے کے لیے حذف کر دیا گیا
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // رجسٹرڈ ٹولز کی فہرست واپس کریں
  return {
    tools: tools
  };
});
```

زبردست، اب ہم نے ٹولز کی فہرست بنانا حل کر لیا ہے، اب دیکھتے ہیں کہ ہم ٹولز کو کیسے کال کر سکتے ہیں۔

### -4- ٹول کال سنبھالیں

ٹول کال کرنے کے لیے، ہمیں ایک اور درخواست ہینڈلر ترتیب دینا ہوگا، جو یہ دیکھے کہ کون سا فیچر کال کرنا ہے اور کس دلائل کے ساتھ۔

**Python**

آئیں `@server.call_tool` سجاوٹ استعمال کریں اور اسے فنکشن `handle_call_tool` کے ساتھ نافذ کریں۔ اس فنکشن میں ہمیں ٹول کا نام، اس کا دلیل (argument) نکالنا ہے اور یقین دہانی کرنا ہے کہ دلائل اس ٹول کے لیے درست ہیں۔ ہم دلائل کی توثیق اس فنکشن میں کر سکتے ہیں یا اصل ٹول میں۔

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ایک لغت ہے جس میں اوزار کے نام کلید کے طور پر ہوتے ہیں
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # اوزار کو چلائیں
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

یہاں کیا ہو رہا ہے:

- ہمارا ٹول نام پہلے سے ان پٹ پیرامیٹر `name` میں موجود ہے جو کہ ہمارے دلائل `arguments` ڈکشنری کی شکل میں ہیں۔

- ٹول کو کال کیا جاتا ہے `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` سے۔ دلائل کی توثیق `handler` پراپرٹی میں ہوتی ہے جو ایک فنکشن کی طرف اشارہ کرتی ہے، اگر یہ ناکام ہو تو استثناء (exception) پھینکے گی۔

بس، اب ہمیں ٹولز کی فہرست بنانا اور کال کرنے کا مکمل اندازہ ہو گیا ہے کم سطح کے سرور کے استعمال سے۔

مکمل مثال دیکھیں [یہاں](./code/README.md)

## اسائنمنٹ

جو کوڈ آپ کو دیا گیا ہے اس میں متعدد ٹولز، ریسورسز اور پرامپٹس شامل کریں اور غور کریں کہ آپ کو صرف tools ڈائریکٹری میں فائلیں شامل کرنے کی ضرورت ہے اور کہیں اور نہیں۔

*کوئی حل فراہم نہیں کیا گیا*

## خلاصہ

اس باب میں، ہم نے دیکھا کہ کم سطح کا سرور طریقہ کار کیسے کام کرتا ہے اور یہ ہمیں ایک اچھی معماری بنانے میں کس طرح مدد دیتا ہے جس پر ہم مستقبل میں تعمیر کر سکتے ہیں۔ ہم نے توثیق پر بھی بات کی اور آپ کو دکھایا گیا کہ کس طرح توثیقی لائبریریوں کے ساتھ اسکیمیاز بنا کر ان پٹ ویلیڈیشن کی جا سکتی ہے۔

## آگے کیا ہے

- اگلا: [سادہ تصدیق](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی وضاحت**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کی مدد سے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہِ کرم اس بات سے آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا بے ضابطگیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہئے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تعبیر کے لیے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->