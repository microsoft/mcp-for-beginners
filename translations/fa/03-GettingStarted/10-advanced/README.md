# استفاده پیشرفته از سرور

در SDK MCP دو نوع مختلف سرور در دسترس است، سرور معمولی و سرور سطح پایین. معمولاً شما از سرور معمولی برای افزودن ویژگی‌ها استفاده می‌کنید. اما در برخی موارد، می‌خواهید به سرور سطح پایین متکی باشید، مانند:

- معماری بهتر. امکان ایجاد معماری تمیز با هر دو سرور معمولی و سرور سطح پایین وجود دارد، اما می‌توان گفت با سرور سطح پایین کمی راحت‌تر است.
- در دسترس بودن ویژگی. برخی ویژگی‌های پیشرفته فقط با
    سرور سطح پایین قابل استفاده هستند. فصل‌های بعدی به ویژگی اِلِسیِشن و نمونه‌برداری قدیمی
    می‌پردازند که در MCP `2026-07-28` منسوخ شده است.

## مقایسه سرور معمولی و سرور سطح پایین

در اینجا نحوه ایجاد یک سرور MCP با سرور معمولی را می‌بینید

**پایتون**

```python
mcp = FastMCP("Demo")

# افزودن ابزار جمع کردن
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**تایپ‌اسکریپت**

```typescript
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// افزودن یک ابزار افزودنی
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

نکته این است که شما به طور صریح هر ابزار، منبع یا پرسش را که می‌خواهید سرور داشته باشد اضافه می‌کنید. مشکلی در این نیست.  

### روش سرور سطح پایین

با این حال، وقتی از روش سرور سطح پایین استفاده می‌کنید باید به شکل متفاوتی به آن فکر کنید. به جای ثبت هر ابزار، در هر نوع ویژگی (ابزار، منابع یا پرسش‌ها) دو هندلر ایجاد می‌کنید. برای مثال، ابزارها فقط دو تابع دارند به این صورت:

- فهرست کردن همه ابزارها. یک تابع مسئول همه تلاش‌ها برای فهرست کردن ابزارهاست.
- هندل کردن فراخوانی همه ابزارها. همچنین فقط یک تابع مسئول اداره فراخوانی به ابزار است

این به نظر می‌رسد کار کمتری باشد، درست است؟ بنابراین به جای ثبت یک ابزار، فقط کافی است مطمئن شوم که وقتی همه ابزارها را فهرست می‌کنم آن ابزار هم باشد و هنگام رسیدن درخواست برای فراخوانی ابزار، آن ابزار فراخوانی شود.

بیایید ببینیم کد چگونه حالا به نظر می‌رسد:

**پایتون**

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

**تایپ‌اسکریپت**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // بازگرداندن فهرست ابزارهای ثبت‌شده
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

اینجا ما تابعی داریم که لیست ویژگی‌ها را برمی‌گرداند. هر ورودی در لیست ابزارها اکنون فیلدهایی مانند `name`، `description` و `inputSchema` دارد تا به نوع بازگشتی تطابق داشته باشد. این به ما اجازه می‌دهد ابزارها و تعریف ویژگی‌های‌مان را جای دیگری قرار دهیم. اکنون می‌توانیم همه ابزارهای‌مان را در پوشه tools ایجاد کنیم و همین‌طور برای همه ویژگی‌ها، بنابراین پروژه شما ناگهان می‌تواند مانند این سازماندهی شود:

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

این عالی است، معماری ما می‌تواند خیلی تمیز به نظر برسد.

چه طور ابزارها فراخوانی می‌شوند، آیا ایده مشابه است، یک هندلر برای فراخوانی هر ابزار؟ بله دقیقاً، این هم کد آن:

**پایتون**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools یک دیکشنری است که نام ابزارها به عنوان کلیدها هستند
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

**تایپ‌اسکریپت**

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
    
    // آرگ‌ها: request.params.arguments
    // انجام شود فراخوانی ابزار،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

همانطور که در کد بالا می‌بینید، باید ابزاری که باید فراخوانی شود و با چه آرگومان‌هایی را تجزیه کنیم و سپس باید به فراخوانی ابزار برویم.

## بهبود رویکرد با اعتبارسنجی

تاکنون دیده‌اید که چگونه تمام ثبت‌هایتان برای افزودن ابزارها، منابع و پرسش‌ها می‌تواند با این دو هندلر در هر نوع ویژگی جایگزین شود. حالا باید چه کار کنیم؟ باید نوعی اعتبارسنجی اضافه کنیم تا اطمینان حاصل شود ابزار با آرگومان‌های درست فراخوانی می‌شود. هر محیط اجرایی راه‌حل خود را برای این دارد، مثلاً پایتون از Pydantic و تایپ‌اسکریپت از Zod استفاده می‌کند. ایده این است که کارهای زیر را انجام دهیم:

- منطق ایجاد یک ویژگی (ابزار، منبع یا پرسش) را به پوشه اختصاصی آن منتقل کنیم.
- راهی برای اعتبارسنجی درخواست‌های ورودی برای مثال هنگام درخواست فراخوانی یک ابزار اضافه کنیم.

### ایجاد یک ویژگی

برای ایجاد یک ویژگی، باید فایلی برای آن ویژگی ایجاد کنیم و مطمئن شویم که فیلدهای اجباری مورد نیاز آن ویژگی را دارد. فیلدها کمی بین ابزارها، منابع و پرسش‌ها متفاوت است.

**پایتون**

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
        # ورودی را با استفاده از مدل Pydantic اعتبارسنجی می‌کند
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # انجام شد: Pydantic را اضافه کنید تا بتوانیم یک AddInputModel ایجاد کنیم و آرگومان‌ها را اعتبارسنجی کنیم

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

اینجا می‌بینید که چگونه انجام می‌دهیم:

- ایجاد یک اسکیمای با استفاده از Pydantic به نام `AddInputModel` با فیلدهای `a` و `b` در فایل *schema.py*.
- تلاش برای تجزیه درخواست ورودی به نوع `AddInputModel`، اگر پارامترها ناسازگار باشند این منجر به خطا خواهد شد:

   ```python
   # add.py
    try:
        # ورودی را با استفاده از مدل Pydantic اعتبارسنجی کنید
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

می‌توانید انتخاب کنید این منطق تجزیه را در خود فراخوانی ابزار قرار دهید یا در تابع هندلر.

**تایپ‌اسکریپت**

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

// طرح.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// اضافه کن.ts
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

- در هندلری که با همه فراخوانی‌های ابزار سروکار دارد، اکنون سعی می‌کنیم درخواست ورودی را به اسکیمای تعریف‌شده ابزار تجزیه کنیم:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    اگر این موفق بود، سپس به فراخوانی ابزار واقعی ادامه می‌دهیم:

    ```typescript
    const result = await tool.callback(input);
    ```

همانطور که می‌بینید این رویکرد معماری عالی ایجاد می‌کند چون هر چیزی جای خود را دارد، *server.ts* فایلی بسیار کوچک است که فقط هندلرهای درخواست را متصل می‌کند و هر ویژگی در پوشه مربوط خودش است مثل tools/، resources/ یا /prompts.

عالی، بیایید حالا تلاش کنیم این را بسازیم.

## تمرین: ساخت سرور سطح پایین

در این تمرین، کارهای زیر را انجام می‌دهیم:

1. ساخت یک سرور سطح پایین برای رسیدگی به فهرست ابزارها و فراخوانی ابزارها.
1. پیاده‌سازی معماری که بتوانید روی آن بسازید.
1. افزودن اعتبارسنجی برای اطمینان از اینکه فراخوانی‌های ابزار به درستی اعتبارسنجی می‌شوند.

### -1- ایجاد یک معماری

اولین موضوعی که باید به آن بپردازیم معماری است که کمک کند وقتی ویژگی‌های بیشتری اضافه می‌کنیم مقیاس‌پذیر باشد، این به این صورت است:

**پایتون**

```text
server.py
--| tools
----| __init__.py
----| add.py
----| schema.py
client.py
```

**تایپ‌اسکریپت**

```text
server.ts
--| tools
----| add.ts
----| schema.ts
client.ts
```

حالا معماری تنظیم شده‌ایم که تضمین می‌کند به راحتی می‌توانیم ابزارهای جدید را در پوشه tools اضافه کنیم. حس راحتی داشته باشید که برای منابع و پرسش‌ها هم زیرپوشه اضافه کنید.

### -2- ایجاد یک ابزار

ببینیم ایجاد یک ابزار بعداً چگونه است. اول باید در زیرپوشه *tool* خودش ایجاد شود به این صورت:

**پایتون**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # اعتبارسنجی ورودی با استفاده از مدل پایدانتیک
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: افزودن پایدانتیک تا بتوانیم یک AddInputModel ایجاد کنیم و آرگومان‌ها را اعتبارسنجی کنیم

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

آنچه اینجا می‌بینیم نحوه تعریف نام، توضیح و اسکیمای ورودی با استفاده از Pydantic و یک هندلری است که هنگام فراخوانی این ابزار اجرا می‌شود. در نهایت `tool_add` را به عنوان دیکشنری با این خصوصیات منتشر می‌کنیم.

همچنین *schema.py* وجود دارد که برای تعریف اسکیمای ورودی مورد استفاده ابزار ماست:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

همچنین باید *__init__.py* را پر کنیم تا اطمینان حاصل شود پوشه tools به عنوان یک ماژول در نظر گرفته شود. افزون بر این، باید ماژول‌های درون آن را اینگونه منتشر کنیم:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

می‌توانیم به این فایل ادامه دهیم همانطور که ابزارهای بیشتری اضافه می‌کنیم.

**تایپ‌اسکریپت**

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

در اینجا دیکشنری‌ای ایجاد می‌کنیم متشکل از ویژگی‌ها:

- name، نام ابزار است.
- rawSchema، اسکیمای Zod است که برای اعتبارسنجی درخواست‌های ورودی برای فراخوانی این ابزار استفاده می‌شود.
- inputSchema، این اسکیمایی است که توسط هندلر استفاده می‌شود.
- callback، این برای اجرای ابزار استفاده می‌شود.

همچنین `Tool` وجود دارد که برای تبدیل این دیکشنری به نوعی است که هندلر سرور MCP می‌تواند آن را قبول کند و به این صورت است:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

و همچنین *schema.ts* جایی که اسکیمای ورودی هر ابزار را ذخیره می‌کنیم که به شکل زیر است فقط با یک اسکیمای فعلی اما هرچه ابزار اضافه کنیم می‌توانیم موارد بیشتری اضافه کنیم:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

عالی، حالا ادامه می‌دهیم به هندل کردن فهرست ابزارها.

### -3- مدیریت فهرست ابزار

برای مدیریت فهرست ابزارها، باید یک هندلر درخواست برای این تنظیم کنیم. این چیزی است که باید به فایل سرور اضافه کنیم:

**پایتون**

```python
# کد برای اختصار حذف شد
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

اینجا دکوراتور `@server.list_tools` را اضافه می‌کنیم و تابع پیاده‌سازی `handle_list_tools`. در دومی، باید لیستی از ابزارها تولید کنیم. دقت کنید هر ابزار باید نام، توضیح و inputSchema داشته باشد.   

**تایپ‌اسکریپت**

برای تنظیم هندلر درخواست فهرست ابزارها، باید `setRequestHandler` را روی سرور با اسکیمایی متناسب با کاری که می‌خواهیم انجام دهیم فراخوانی کنیم، در این مورد `ListToolsRequestSchema`.

```typescript
// ایندکس.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// سرور.ts
// کد برای اختصار حذف شد
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // بازگرداندن لیست ابزارهای ثبت شده
  return {
    tools: tools
  };
});
```

عالی، حالا که بخش فهرست کردن ابزارها را حل کردیم، بیایید ببینیم چگونه می‌توانیم ابزارها را فراخوانی کنیم.

### -4- مدیریت فراخوانی ابزار

برای فراخوانی ابزار، باید هندلر درخواست دیگری تنظیم کنیم که این بار روی درخواست‌هایی تمرکز دارد که مشخص می‌کنند کدام ویژگی باید فراخوانی شود و با چه آرگومان‌هایی.

**پایتون**

از دکوراتور `@server.call_tool` استفاده کنیم و آن را با تابعی مانند `handle_call_tool` پیاده‌سازی کنیم. در این تابع باید نام ابزار، آرگومان‌های آن را استخراج کنیم و اطمینان حاصل کنیم آرگومان‌ها برای آن ابزار معتبر هستند. می‌توانیم اعتبارسنجی را در این تابع یا در خود ابزار انجام دهیم.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools یک دیکشنری با نام ابزارها به‌عنوان کلید است
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ابزار را فراخوانی کن
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

اینجا چه اتفاقی می‌افتد:

- نام ابزار به عنوان پارامتر ورودی `name` موجود است که برای آرگومان‌ها به شکل دیکشنری `arguments` درست است.

- ابزار با `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` فراخوانی می‌شود. اعتبارسنجی آرگومان‌ها در خاصیت `handler` که به یک تابع اشاره می‌کند انجام می‌شود، اگر این ناموفق باشد استثنایی ایجاد خواهد شد.

حالا ما درک کامل از فهرست کردن و فراخوانی ابزارها با استفاده از سرور سطح پایین داریم.

نمونه کامل را در این [لینک](./code/README.md) ببینید

## تمرین

کدی که داده‌شده را با تعداد بیشتری ابزار، منابع و پرسش گسترش دهید و بررسی کنید که چگونه تنها کافی است فایل‌ها را در دایرکتوری tools اضافه کنید و جای دیگر نیازی به تغییر نیست.

*هیچ راه‌حلی داده نشده است*

## خلاصه

در این فصل دیدیم که روش سرور سطح پایین چگونه کار می‌کند و چگونه می‌تواند به ما کمک کند تا معماری خوبی بسازیم که بتوانیم روی آن ادامه دهیم. همچنین درباره اعتبارسنجی بحث کردیم و چگونگی کار با کتابخانه‌های اعتبارسنجی برای ایجاد اسکیمای ورودی نشان داده شد.

## مرحله بعد

- مرحله بعد: [تصدیق ساده](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->