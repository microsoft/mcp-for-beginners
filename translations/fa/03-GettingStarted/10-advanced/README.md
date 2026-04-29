# استفاده پیشرفته از سرور

دو نوع مختلف سرور در MCP SDK وجود دارد، سرور معمولی و سرور سطح پایین. معمولاً شما از سرور معمولی برای افزودن ویژگی‌ها استفاده می‌کنید. اما در برخی موارد، می‌خواهید به سرور سطح پایین تکیه کنید مانند:

- معماری بهتر. ممکن است با هر دو سرور معمولی و سطح پایین معماری تمیزی ایجاد کرد، اما می‌توان گفت کمی کار با سرور سطح پایین آسان‌تر است.
- در دسترس بودن ویژگی‌ها. برخی از ویژگی‌های پیشرفته تنها با سرور سطح پایین قابل استفاده هستند. این را در فصل‌های بعدی هنگام افزودن نمونه‌گیری و استخراج خواهید دید.

## سرور معمولی در مقابل سرور سطح پایین

اینجا نحوه ایجاد یک سرور MCP با سرور معمولی را مشاهده می‌کنید

**Python**

```python
mcp = FastMCP("Demo")

# افزودن یک ابزار جمع
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

// افزودن یک ابزار الحاق
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

نکته این است که شما هر ابزار، منبع یا پرسشی را که می‌خواهید سرور داشته باشد به‌صراحت اضافه می‌کنید. مشکلی در این نیست.  

### رویکرد سرور سطح پایین

اما وقتی از رویکرد سرور سطح پایین استفاده می‌کنید، باید به شکل متفاوتی فکر کنید. به جای ثبت هر ابزار، در عوض باید برای هر نوع ویژگی (ابزارها، منابع یا پرسش‌ها) دو هندلر بسازید. برای مثال، ابزارها فقط دو تابع دارند به این شکل:

- فهرست کردن همه ابزارها. یک تابع مسئول همه تلاش‌ها برای فهرست ابزارها است.
- هندل کردن فراخوانی ابزارها. اینجا هم، فقط یک تابع برای هندل کردن فراخوانی یک ابزار وجود دارد.

این احتمالاً کار کمتری به نظر می‌رسد، درست است؟ پس به جای ثبت یک ابزار، فقط باید مطمئن شوم ابزار هنگام فهرست همه ابزارها فهرست شده و هنگام درخواست ورود به فراخوانی ابزار، این اتفاق می‌افتد.

بیایید به کد حالا نگاه کنیم:

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
  // فهرست ابزارهای ثبت شده را بازگردانید
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

اینجا ما اکنون تابعی داریم که لیستی از ویژگی‌ها را برمی‌گرداند. هر ورودی در لیست ابزارها اکنون فیلدهایی مانند `name`، `description` و `inputSchema` دارد تا با نوع بازگشتی مطابقت داشته باشد. این به ما این امکان را می‌دهد که ابزارها و تعریف ویژگی‌هایمان را جای دیگری قرار دهیم. اکنون می‌توانیم همه ابزارهایمان را در یک پوشه tools بسازیم و همین‌طور برای همه ویژگی‌ها این اتفاق می‌افتد تا پروژه شما ناگهان این‌گونه سازماندهی شود:

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

عالی است، معماری ما می‌تواند بسیار تمیز به نظر برسد.

فراخوانی ابزارها چگونه است، آیا همان ایده است، یک هندلر برای فراخوانی هر ابزاری؟ بله، دقیقاً، کد برای این چنین است:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools یک دیکشنری با نام ابزارها به عنوان کلیدها است
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
    
    // آرگ: request.params.arguments
    // انجام شود فراخوانی ابزار،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

همانطور که از کد بالا می‌بینید، باید ابزار برای فراخوانی و آرگومان‌های آن را تحلیل کنیم، و سپس باید به فراخوانی ابزار ادامه دهیم.

## بهبود رویکرد با اعتبارسنجی

تا اینجا، دیدید که چگونه تمام ثبت‌های شما برای افزودن ابزارها، منابع و پرسش‌ها می‌تواند با این دو هندلر به ازای هر نوع ویژگی جایگزین شود. حالا چه چیز بیشتری باید انجام دهیم؟ خب، باید نوعی اعتبارسنجی اضافه کنیم تا مطمئن شویم ابزار با آرگومان‌های درست فراخوانی می‌شود. هر محیط اجرایی راه‌حل خودش را برای این دارد، مثلاً Python از Pydantic و TypeScript از Zod استفاده می‌کند. هدف این است که کارهای زیر را انجام دهیم:

- منطق ساخت یک ویژگی (ابزار، منبع یا پرسش) را به پوشه مختص خودش منتقل کنیم.
- راهی برای اعتبارسنجی یک درخواست ورودی اضافه کنیم که مثلاً درخواست فراخوانی یک ابزار را داشته باشد.

### ایجاد یک ویژگی

برای ایجاد یک ویژگی، باید فایلی برای آن ویژگی ایجاد کنیم و مطمئن شویم فیلدهای اجباری مورد نیاز آن ویژگی وجود دارد. این فیلدها کمی بین ابزارها، منابع و پرسش‌ها متفاوت است.

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
        # ورودی را با استفاده از مدل Pydantic اعتبارسنجی کنید
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # کارهای باقیمانده: اضافه کردن Pydantic، تا بتوانیم یک AddInputModel بسازیم و آرگومان‌ها را اعتبارسنجی کنیم

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

در اینجا می‌بینید که چگونه موارد زیر را انجام می‌دهیم:

- ایجاد یک اسکیما با استفاده از Pydantic به نام `AddInputModel` با فیلدهای `a` و `b` در فایل *schema.py*.
- تلاش برای تجزیه درخواست ورودی به نوع `AddInputModel`، اگر پارامترها مطابقت نداشته باشند این منجر به خطا می‌شود:

   ```python
   # add.py
    try:
        # اعتبارسنجی ورودی با استفاده از مدل پایدنتیک
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

شما می‌توانید انتخاب کنید که این منطق تجزیه را در خود فراخوانی ابزار یا در تابع هندلر قرار دهید.

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

// شِما.ts
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

- در هندلری که با همه فراخوانی‌های ابزار سر و کار دارد، اکنون تلاش می‌کنیم درخواست ورودی را به اسکیما تعریف شده ابزار تبدیل کنیم:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    اگر این موفق بود، سپس به فراخوانی ابزار واقعی ادامه می‌دهیم:

    ```typescript
    const result = await tool.callback(input);
    ```

همانطور که می‌بینید، این رویکرد معماری خوبی ایجاد می‌کند چون همه چیز جای خود را دارد، فایل *server.ts* بسیار کوچک است که فقط هندلرهای درخواست را وصل می‌کند و هر ویژگی در پوشه مخصوص خودش (tools/، resources/ یا /prompts) است.

عالی است، بیایید بعدی را بسازیم.

## تمرین: ساختن یک سرور سطح پایین

در این تمرین، کارهای زیر را انجام می‌دهیم:

1. ساختن یک سرور سطح پایین که فهرست کردن ابزارها و فراخوانی ابزارها را هندل می‌کند.
1. پیاده‌سازی معماری‌ای که بتوان بر آن ساخت.
1. افزودن اعتبارسنجی برای اطمینان از صحت فراخوانی ابزارها.

### -1- ایجاد معماری

اولین چیزی که باید به آن بپردازیم، معماری‌ای است که به ما کمک می‌کند هنگام افزودن ویژگی‌های بیشتر، مقیاس‌پذیر باشیم، این‌گونه است:

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

حالا معماری‌ای تنظیم کرده‌ایم که تضمین می‌کند می‌توانیم به راحتی ابزارهای جدید را در پوشه tools اضافه کنیم. احساس آزادی کنید که برای منابع و پرسش‌ها پوشه‌های فرعی اضافه کنید.

### -2- ساختن یک ابزار

بیایید ببینیم ساختن یک ابزار چگونه است. اول، باید در زیرپوشه *tool* خودش ساخته شود به این شکل:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # اعتبارسنجی ورودی با استفاده از مدل پایدانتیک
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # نکته: افزودن پایدانتیک تا بتوانیم یک AddInputModel ایجاد کرده و پارامترها را اعتبارسنجی کنیم

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

این‌جا می‌بینیم که چگونه با استفاده از Pydantic نام، توضیح و اسکیما ورودی تعریف می‌شود و یک هندلر که هنگام فراخوانی این ابزار اجرا می‌شود. در نهایت، `tool_add` را که یک دیکشنری شامل این ویژگی‌ها است، صادر می‌کنیم.

همچنین *schema.py* وجود دارد که اسکیما ورودی استفاده شده توسط ابزار ما را تعریف می‌کند:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ما همچنین باید *__init__.py* را پر کنیم تا مطمئن شویم پوشه tools به‌عنوان یک ماژول در نظر گرفته شود. علاوه بر این، باید ماژول‌های درون آن را به این شکل صادر کنیم:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

می‌توانیم هرچه ابزار بیشتر می‌سازیم به این فایل اضافه کنیم.

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

در اینجا یک دیکشنری از ویژگی‌ها ایجاد می‌کنیم:

- name، نام ابزار است.
- rawSchema، این اسکیمای Zod است، برای اعتبارسنجی درخواست‌های ورودی برای فراخوانی این ابزار استفاده می‌شود.
- inputSchema، این اسکیما توسط هندلر استفاده می‌شود.
- callback، این برای اجرای ابزار استفاده می‌شود.

همچنین `Tool` وجود دارد که این دیکشنری را به نوعی تبدیل می‌کند که هندلر سرور mcp بتواند آن را بپذیرد و به این شکل است:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

و *schema.ts* جایی است که اسکیماهای ورودی برای هر ابزار ذخیره شده‌اند که تنها یک اسکیما فعلاً دارد اما با افزودن ابزارها می‌توانیم ورودی بیشتری اضافه کنیم:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

عالی است، بیایید بعدی را برای هندل کردن فهرست ابزارها جلو ببریم.

### -3- هندل کردن فهرست ابزارها

حالا برای هندل کردن فهرست ابزارها، باید یک هندلر درخواست تنظیم کنیم. این چیزی است که باید به فایل سرور اضافه کنیم:

**Python**

```python
# کد برای اختصار حذف شده است
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

در اینجا دکوراتور `@server.list_tools` و تابع پیاده‌سازی `handle_list_tools` را اضافه می‌کنیم. در دومی، باید لیستی از ابزارها تولید کنیم. توجه کنید که هر ابزار باید نام، توضیح و inputSchema داشته باشد.   

**TypeScript**

برای تنظیم هندلر درخواست فهرست ابزارها، باید `setRequestHandler` را روی سرور با یک اسکیما متناسب با کاری که می‌خواهیم انجام دهیم فراخوانی کنیم، در این مورد `ListToolsRequestSchema`.

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
  // بازگرداندن فهرست ابزارهای ثبت شده
  return {
    tools: tools
  };
});
```

عالی، حالا ما بخش فهرست ابزارها را حل کرده‌ایم، بیایید ببینیم بعداً چطور می‌توانیم ابزارها را فراخوانی کنیم.

### -4- هندل کردن فراخوانی یک ابزار

برای فراخوانی یک ابزار، باید هندلر درخواست دیگری تنظیم کنیم، این بار تمرکز روی یک درخواست است که مشخص می‌کند کدام ویژگی باید فراخوانی شود و با چه آرگومان‌هایی.

**Python**

از دکوراتور `@server.call_tool` استفاده کنیم و با تابعی مانند `handle_call_tool` آن را پیاده‌سازی کنیم. در این تابع باید نام ابزار، آرگومان‌های آن را تجزیه کنیم و اطمینان حاصل کنیم که آرگومان‌ها برای ابزار مربوطه معتبر هستند. می‌توانیم اعتبارسنجی آرگومان‌ها را در همین تابع انجام دهیم یا در داخل خود ابزار.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # ابزارها یک دیکشنری هستند که نام ابزارها به عنوان کلید استفاده می‌شود
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

- نام ابزار ما به عنوان پارامتر ورودی `name` حاضر است که برای آرگومان‌ها در قالب دیکشنری `arguments` درست است.

- ابزار با `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` فراخوانی می‌شود. اعتبارسنجی آرگومان‌ها در پراپرتی `handler` که به یک تابع اشاره می‌کند انجام می‌شود، اگر ناموفق باشد یک استثنا می‌افکند.

حالا ما درک کامل از فهرست کردن و فراخوانی ابزارها با استفاده از سرور سطح پایین داریم.

مثال کامل را اینجا ببینید [full example](./code/README.md)

## تکلیف

کدی که به شما داده شده را با تعداد بیشتری ابزار، منابع و پرسش‌ها در پوشه tools توسعه دهید و بررسی کنید که فقط کافی است فایل جدیدی در پوشه tools اضافه کنید و در هیچ جای دیگری نیازی به اضافه کردن فایل نیست.

*هیچ راه‌حلی ارائه نشده است*

## خلاصه

در این فصل دیدیم چگونه رویکرد سرور سطح پایین کار می‌کند و چگونه می‌تواند به ما کمک کند معماری خوبی داشته باشیم که بتوانیم روی آن بسازیم. همچنین درباره اعتبارسنجی صحبت کردیم و به شما نشان داده شد چگونه با کتابخانه‌های اعتبارسنجی برای ساختن اسکیماهای اعتبارسنجی ورودی کار کنید.

## مرحله بعد

- بعدی: [احراز هویت ساده](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است دارای اشتباهات یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->