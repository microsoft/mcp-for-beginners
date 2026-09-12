# اعلیٰ سرور کا استعمال  

MCP SDK میں دو مختلف قسم کے سرورز موجود ہیں، آپ کا معمول کا سرور اور نِچلے سطح کا سرور۔ عام طور پر، آپ معمول کے سرور کو فیچر شامل کرنے کے لیے استعمال کریں گے۔ تاہم کچھ حالات میں آپ نِچلے سطح کے سرور پر انحصار کرنا چاہیں گے جیسا کہ:  

- بہتر معمارتی ڈھانچہ۔ دونوں، معمول کا سرور اور نِچلے سطح کا سرور استعمال کرکے صاف ستھرا معمارتی ڈھانچہ بنانا ممکن ہے مگر کہا جا سکتا ہے کہ نِچلے سطح کے سرور کے ساتھ یہ تھوڑا آسان ہوتا ہے۔  
- فیچر کی دستیابی۔ کچھ جدید فیچرز صرف نِچلے سطح کے سرور کے ساتھ استعمال کیے جا سکتے ہیں۔  
    بعد کے ابواب میں Elicitation اور legacy Sampling فیچر شامل ہیں، جو MCP `2026-07-28` میں منسوخ کر دیا گیا ہے۔  
 

## معمول کا سرور بمقابلہ نچلے سطح کا سرور  

معمول کے سرور کے ساتھ MCP سرور بنانے کا طریقہ کچھ یوں دکھائی دیتا ہے:  

**Python**  

```python
mcp = FastMCP("Demo")

# ایک اضافی آلہ شامل کریں
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

// ایک اضافہ کرنے والا آلہ شامل کریں
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
  
مطلب یہ ہے کہ آپ واضح طور پر ہر ٹول، ریسورس یا پرامپٹ کو شامل کرتے ہیں جو آپ سرور میں چاہتے ہیں۔ اس میں کوئی مسئلہ نہیں ہے۔  

### نچلے سطح کے سرور کا طریقہ  

لیکن جب آپ نچلے سطح کے سرور کا طریقہ استعمال کرتے ہیں تو آپ کو اس بارے میں مختلف سوچنا ہوتا ہے۔ ہر ٹول کو رجسٹر کرنے کے بجائے، آپ ہر فیچر کی قسم (ٹولز، ریسورسز یا پرامپٹس) کے لیے دو ہینڈلرز بناتے ہیں۔ مثلاً ٹولز کی دو فنکشنز کچھ یوں ہیں:  

- تمام ٹولز کی فہرست دینا۔ ایک فنکشن تمام فہرست کے لیے ذمہ دار ہوتا ہے۔  
- کالز کو ہینڈل کرنا۔ یہاں بھی، صرف ایک فنکشن ٹول کی کالز کو ہینڈل کرتا ہے۔  

یہ کم کام لگتا ہے، ہے نا؟ تو اب ٹول کو رجسٹر کرنے کی بجائے مجھے صرف اتنا یقینی بنانا ہے کہ جب میں ٹولز کی فہرست نکالوں تو وہ شامل ہو اور جب کوئی ٹول کال کرنے کی درخواست آئے تو وہ کال ہو جائے۔  

آئیے دیکھتے ہیں اب کوڈ کیسا دکھائی دیتا ہے:  

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
  
یہاں ہمارے پاس اب ایک فنکشن ہے جو فیچرز کی فہرست واپس کرتا ہے۔ ٹولز کی ہر انٹری میں اب `name`, `description` اور `inputSchema` جیسے فیلڈز شامل ہیں تاکہ ریٹرن ٹائپ کی پابندی کی جا سکے۔ اس سے ہمیں اپنے ٹولز اور فیچر کی تعریف کہیں اور رکھنے کی اجازت ملتی ہے۔ اب ہم تمام ٹولز کو tools فولڈر میں بنا سکتے ہیں اور آپ کے تمام فیچرز کے لیے بھی یہی ترتیب ہو سکتی ہے، یوں آپ کا پروجیکٹ یوں منظم ہو سکتا ہے:  

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
  
یہ بہت اچھا ہے، ہمارا معمارتی ڈھانچہ کافی صاف ستھرا ہو سکتا ہے۔  

اب ٹولز کو کال کرنے کا کیا؟ کیا یہ بھی یہی خیال ہے؟ ایک ہینڈلر جو ہر ٹول کو کال کرے، کوئی بھی ٹول؟ جی ہاں، بالکل، کوڈ کچھ یوں ہے:  

**Python**  

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ایک لغت ہے جس میں ٹول کے نام بطور کلید ہیں
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
    
    // دلائل: request.params.arguments
    // کرنے کے لئے: آلہ کو کال کریں،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```
  
اوپر کے کوڈ سے دیکھا جا سکتا ہے کہ ہمیں یہ معلوم کرنا ہوتا ہے کہ کون سا ٹول کال کرنا ہے، اور کس دلیل کے ساتھ، پھر ہمیں ٹول کو کال کرنا ہوتا ہے۔  

## قابلِ اعتبار بنانے کے لئے طریقہ کار کی بہتری  

اب تک، آپ نے دیکھا کہ ٹولز، ریسورسز اور پرامپٹس کو شامل کرنے کے تمام رجسٹریشنز کو فیچر قسم کے حساب سے صرف دو ہینڈلرز سے تبدیل کیا جا سکتا ہے۔ اب ہمیں اور کیا کرنا چاہیے؟ ہم کچھ قسم کی ویلیڈیشن شامل کریں تاکہ یقین ہو کہ ٹول صحیح دلائل کے ساتھ کال ہو رہا ہے۔ ہر رن ٹائم کے پاس اس کے لیے اپنا حل ہوتا ہے، مثلاً Python Pydantic استعمال کرتا ہے اور TypeScript Zod استعمال کرتا ہے۔ خیال یہ ہے کہ ہم مندرجہ ذیل کریں:  

- فیچر (ٹول، ریسورس یا پرامپٹ) بنانے کی منطق کو اس کے مخصوص فولڈر میں منتقل کریں۔  
- آنے والی درخواست کو ویلیڈیٹ کرنے کا طریقہ شامل کریں، مثلاً ٹول کال کرنے کی درخواست۔  

### فیچر بنائیں  

فیچر بنانے کے لیے، ہمیں اس فیچر کے لیے ایک فائل بنانی ہوگی اور یہ یقینی بنانا ہوگا کہ اس میں لازمی فیلڈز موجود ہوں جو مختلف ہو سکتے ہیں ٹولز، ریسورسز اور پرامپٹس کے لیے۔  

**Python**  

```python
# سکیما.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# ایڈ.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ان پٹ کی تصدیق کے لیے Pydantic ماڈل استعمال کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic شامل کریں، تاکہ ہم ایک AddInputModel بنا سکیں اور دلائل کی تصدیق کر سکیں

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

- Pydantic `AddInputModel` اسکیمہ بنائیں جس میں فیلڈز `a` اور `b` ہیں، فائل *schema.py* میں۔  
- آنے والی درخواست کو `AddInputModel` کی طرح پارس کرنے کی کوشش کریں، اگر پیرامیٹرز میں میل نہ ہو تو یہ کریش کر جائے گا:  

   ```python
   # add.py
    try:
        # Pydantic ماڈل استعمال کرتے ہوئے ان پٹ کی توثیق کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```
  
آپ یہ پارسنگ لاجک خود ٹول کال میں بھی رکھ سکتے ہیں یا ہینڈلر فنکشن میں۔  

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

// اسکیمہ.ts
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
  
- تمام ٹول کالز کو ہینڈل کرنے والے ہینڈلر میں ہم اب کوشش کرتے ہیں کہ آنے والی درخواست کو ٹول کے متعین اسکیمہ میں پارس کریں:  

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```
  
    اگر یہ کامیاب ہو جائے تو پھر ہم اصل ٹول کو کال کرتے ہیں:  

    ```typescript
    const result = await tool.callback(input);
    ```
  
جیسا کہ آپ دیکھ سکتے ہیں، یہ طریقہ ایک بہترین معمارتی ڈھانچہ بناتا ہے کیونکہ ہر چیز اپنی جگہ ہوتی ہے۔ *server.ts* بہت چھوٹی فائل ہے جو صرف درخواست ہینڈلرز کو ترتیب دیتی ہے اور ہر فیچر اپنے فولڈر میں ہوتا ہے مثلاً tools/, resources/ یا /prompts۔  

اچھا، آئیے اگلی مرتبہ اسے بناتے ہیں۔  

## مشق: نچلے سطح کا سرور بنانا  

اس مشق میں ہم یہ کریں گے:  

1. ایک نچلے سطح کا سرور بنائیں جو ٹولز کی فہرست اور ٹولز کی کال کو ہینڈل کرے۔  
1. ایک معمارتی ڈھانچہ نافذ کریں جس پر آپ تعمیر کر سکیں۔  
1. ویلیڈیشن شامل کریں تاکہ آپ کی ٹول کالز صحیح طور پر تصدیق شدہ ہوں۔  

### -1- معمارتی ڈھانچہ بنانا  

سب سے پہلے ہمیں ایک ایسا ڈھانچہ بنانا ہے جو بڑھتی ہوئی خصوصیات کے ساتھ آسان Expansion کی اجازت دے، یوں دکھائی دیتا ہے:  

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
  
اب ہم نے ایک ایسا معمارتی ڈھانچہ ترتیب دیا ہے جو آسانی سے ٹولز فولڈر میں نئے ٹولز شامل کرنے کی اجازت دیتا ہے۔ ریسورسز اور پرامپٹس کے لئے ذیلی ڈائریکٹری بنانے کے لئے آپ اسے فالو کر سکتے ہیں۔  

### -2- ٹول بنائیں  

آئیں دیکھیں کہ ٹول بنانے کا طریقہ کیا ہے۔ سب سے پہلے، اسے اپنے ٹول سب ڈائریکٹری میں بنائیں، کچھ یوں:  

**Python**  

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # پائیڈانٹک ماڈل کا استعمال کرتے ہوئے ان پٹ کی تصدیق کریں
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # کرنے کے لیے: پائیڈانٹک شامل کریں، تاکہ ہم AddInputModel بنا سکیں اور آرگس کی تصدیق کر سکیں

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```
  
یہاں ہم نام، تفصیل، اور ان پٹ اسکیمہ Pydantic کے ساتھ متعین کرتے ہیں، اور ایک ہینڈلر جو ٹول کال پر فعال ہوگا۔ آخر میں ہم `tool_add` ظاہر کرتے ہیں جو یہ خصوصیات رکھتا ہے۔  

یہاں *schema.py* بھی ہے جو ہمارے ٹول کے ان پٹ اسکیمہ کو متعین کرتا ہے:  

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```
  
ہمیں *__init__.py* کو بھی بھرنا ہوگا تاکہ tools ڈائریکٹری کو ایک ماڈیول سمجھا جائے۔ اس کے علاوہ ہمیں ماڈیولز کو یوں دکھانا ہوگا:  

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```
  
جیسے جیسے ہم نئے ٹولز شامل کریں گے ہم اس فائل میں اضافہ کر سکتے ہیں۔  

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
  
یہاں ہم ایک ڈکشنری بناتے ہیں جس میں یہ خصوصیات شامل ہیں:  

- name، یعنی ٹول کا نام۔  
- rawSchema، یہ Zod اسکیمہ ہے جو آنے والی درخواستوں کی تصدیق کے لیے استعمال ہوگا۔  
- inputSchema، یہ اسکیمہ ہینڈلر کی طرف سے استعمال ہوتا ہے۔  
- callback، یہ ٹول کو کال کرنے کے لیے استعمال ہوتا ہے۔  

`Tool` بھی ہے جو اس ڈکشنری کو ایسے ٹائپ میں تبدیل کرتا ہے جسے mcp سرور ہینڈلر قبول کر سکے، یہ کچھ یوں دکھائی دیتا ہے:  

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```
  
یہاں *schema.ts* ہے جہاں ہم ہر ٹول کے ان پٹ اسکیمہ کو اسٹور کرتے ہیں، فی الحال صرف ایک اسکیمہ ہے مگر جیسے جیسے ہم ٹولز بڑھائیں گے ہم مزید انٹریز شامل کریں گے:  

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```
  
اچھا، اب ہم اپنے ٹولز کی فہرست کو ہینڈل کریں گے۔  

### -3- ٹولز کی فہرست ہینڈل کریں  

اگلا قدم ٹولز کی فہرست دھکیلنے کے لیے درخواست ہینڈلر ترتیب دینا ہے۔ یہ وہ چیز ہے جو ہمیں اپنے سرور فائل میں شامل کرنا ہو گا:  

**Python**  

```python
# کوڈ کی مختصراً نظر انداز کیا گیا ہے
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
  
یہاں ہم ڈیکوریٹر `@server.list_tools` اور اس کی فنکشن `handle_list_tools` شامل کرتے ہیں۔ اس میں ہمیں ٹولز کی ایک فہرست دینی ہوتی ہے۔ نوٹ کریں کہ ہر ٹول کے پاس نام، تفصیل اور inputSchema ہونا ضروری ہے۔  

**TypeScript**  

ٹولز کی فہرست کے لیے درخواست ہینڈلر ترتیب دینے کے لیے ہمیں سرور پر `setRequestHandler` کال کرنا ہوتا ہے اور اسکیمہ پاس کرنا ہوتا ہے جو اس کام کے لیے ہے، یہاں `ListToolsRequestSchema` ہے۔  

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
// کوڈ اختصار کے لیے حذف کیا گیا
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // رجسٹرڈ آلات کی فہرست لوٹائیں
  return {
    tools: tools
  };
});
```
  
اچھا، اب ہم نے ٹولز کی فہرست نکالنے کا مسئلہ حل کر لیا ہے، آئیے دیکھتے ہیں کہ ہم ٹولز کو کیسے کال کر سکتے ہیں۔  

### -4- ٹول کال ہینڈل کریں  

ٹول کال کرنے کے لیے، ہمیں ایک اور درخواست ہینڈلر ترتیب دینا ہوتا ہے جو اس خصوصیت (فیچر) اور اس کے دلائل کو سنبھالے۔  

**Python**  

آئیں ڈیکوریٹر `@server.call_tool` استعمال کریں اور اسے `handle_call_tool` فنکشن کے ساتھ نافذ کریں۔ اس فنکشن میں ہمیں ٹول کا نام، اس کی دلیل کو پارس کرنا ہوگا اور تصدیق کرنی ہوگی کہ دلائل ٹول کے لیے درست ہیں۔ ہم دلائل کی ویلیڈیشن یہاں بھی کر سکتے ہیں یا ٹول میں آگے۔  

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ایک لغت ہے جس میں اوزار کے نام چابیاں ہیں
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # اوزار کو طلب کریں
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```
  
یہاں کیا ہوتا ہے:  

- ہمارا ٹول نام گزشتہ سے بطور ان پٹ پیرامیٹر `name` موجود ہے جو کہ ہمارے دلائل `arguments` ڈکشنری کی صورت میں ہیں۔  

- ٹول کو `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` کے ساتھ کال کیا جاتا ہے۔ دلائل کی تصدیق `handler` پراپرٹی میں ہوتی ہے جو ایک فنکشن کی طرف اشارہ کرتی ہے، اگر یہ ناکام ہو تو ایک استثناء (exception) پھینکے گا۔  

اب ہمیں نچلے سطح کے سرور کے ذریعہ ٹولز کی فہرست نکالنے اور کال کرنے کا مکمل فہم حاصل ہو گیا ہے۔  

مکمل مثال یہاں دیکھیں: [full example](./code/README.md)  

## اسائنمنٹ  

آپ کو دیا گیا کوڈ مزید ٹولز، ریسورسز اور پرامپٹس کے ساتھ توسیع کریں اور غور کریں کہ آپ کو صرف tools ڈائریکٹری میں فائلیں شامل کرنا پڑتی ہیں اور کہیں اور نہیں۔  

*کوئی حل فراہم نہیں کیا گیا*  

## خلاصہ  

اس باب میں، ہم نے دیکھا کہ نچلے سطح کا سرور کیسے کام کرتا ہے اور وہ ہمیں کیسی عمدہ معمارتی ڈھانچہ بنانے میں مدد دے سکتا ہے جس پر ہم مزید تعمیر کر سکتے ہیں۔ ہم نے ویلیڈیشن پر بھی تبادلہ خیال کیا اور آپ کو دکھایا گیا کہ ان پٹ ویلیڈیشن کے لیے اسکیمہ بنانے کے لیے ویلیڈیشن لائبریریز کے ساتھ کیسے کام کرنا ہے۔  

## اگلا کیا ہے  

- اگلا: [سادہ تصدیق](../11-simple-auth/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->