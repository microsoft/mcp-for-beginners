# استفاده پیشرفته از سرور

دو نوع سرور مختلف در MCP SDK معرفی شده‌اند، سرور معمولی شما و سرور سطح پایین. معمولاً شما از سرور معمولی برای اضافه کردن ویژگی‌ها استفاده می‌کنید. با این حال، در بعضی موارد ممکن است بخواهید به سرور سطح پایین تکیه کنید، مانند:

- معماری بهتر. امکان ایجاد معماری تمیز با هر دو سرور معمولی و سرور سطح پایین وجود دارد اما می‌توان گفت که کمی آسان‌تر با سرور سطح پایین است.
- در دسترس بودن ویژگی‌ها. برخی ویژگی‌های پیشرفته تنها با سرور سطح پایین قابل استفاده‌اند. این موضوع را در فصل‌های بعدی مشاهده خواهید کرد که نمونه‌گیری و استخراج را اضافه می‌کنیم.

## سرور معمولی در مقابل سرور سطح پایین

ایجاد یک سرور MCP با سرور معمولی به شکل زیر است:

**Python**

```python
mcp = FastMCP("Demo")

# اضافه کردن یک ابزار جمع
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

// افزودن یک ابزار جمع
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

موضوع این است که شما به طور صریح هر ابزار، منبع یا پیشنهاد مورد نظر برای سرور را اضافه می‌کنید. مشکلی در این نیست.

### رویکرد سرور سطح پایین

با این حال، وقتی از رویکرد سرور سطح پایین استفاده می‌کنید، باید به شکلی متفاوت فکر کنید. به جای ثبت هر ابزار، در عوض دو هندلر برای هر نوع ویژگی (ابزارها، منابع یا پیشنهادات) ایجاد می‌کنید. برای مثال، ابزارها فقط دو تابع دارند به این شکل:

- فهرست کردن همه ابزارها. یک تابع مسئول تمام تلاش‌ها برای فهرست کردن ابزارها است.
- هندل کردن فراخوانی تمام ابزارها. در اینجا نیز فقط یک تابع برای هندل کردن درخواست به یک ابزار وجود دارد.

این می‌تواند به معنی کاری کمتر باشد، درست است؟ بنابراین به جای ثبت ابزار، تنها باید مطمئن شوم که ابزار موقع فهرست کردن ابزارها نشان داده شود و هنگامی که درخواست فراخوانی ابزار می‌آید، فراخوان شده باشد.

بیایید ببینیم کد چگونه به نظر می‌رسد:

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
  // بازگرداندن فهرست ابزارهای ثبت شده
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

در اینجا تابعی داریم که فهرستی از ویژگی‌ها را بازمی‌گرداند. هر ورودی در لیست ابزارها اکنون دارای فیلدهایی مانند `name`، `description` و `inputSchema` است تا به نوع بازگشتی مطابقت داشته باشد. این امکان را به ما می‌دهد که ابزارها و تعریف ویژگی‌هایمان را در جاهای دیگر قرار دهیم. اکنون می‌توانیم تمام ابزارهای خود را در یک پوشه ابزارها ایجاد کنیم و همینطور برای همه ویژگی‌ها، بنابراین پروژه شما ناگهان می‌تواند به این شکل سازمان‌یافته باشد:

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

فراخوانی ابزارها چطور؟ همان ایده است، یک هندلر برای فراخوانی هر ابزار؟ بله، دقیقاً، کدش این است:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # ابزارها یک دیکشنری با نام ابزارها به عنوان کلیدها هستند
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
    
    // آرگ‌ها: request.params.arguments
    // TODO فراخوانی ابزار،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

همانطور که در کد بالا می‌بینید، باید ابزار را که باید فراخوانی شود و با چه آرگومان‌هایی تجزیه کنیم، سپس ادامه دهیم به فراخوانی ابزار.

## بهبود رویکرد با اعتبارسنجی

تا اینجا، دیدید که چگونه تمامی ثبت‌ها برای اضافه کردن ابزارها، منابع و پیشنهادات می‌تواند با این دو هندلر برای هر نوع ویژگی جایگزین شود. حالا چه باید کرد؟ باید نوعی اعتبارسنجی اضافه کنیم تا اطمینان حاصل کنیم که ابزار با آرگومان‌های درست فراخوانی می‌شود. هر زمان اجرا راه‌حل خودش را دارد، مثلاً پایتون از Pydantic استفاده می‌کند و تایپ‌اسکریپت از Zod. ایده این است که موارد زیر را انجام دهیم:

- منطق ایجاد یک ویژگی (ابزار، منبع یا پیشنهاد) را به پوشه مخصوص به خود منتقل کنیم.
- راهی برای اعتبارسنجی یک درخواست ورودی اضافه کنیم که مثلاً درخواست فراخوانی یک ابزار باشد.

### ایجاد یک ویژگی

برای ایجاد یک ویژگی، باید فایلی برای آن ویژگی بسازیم و مطمئن شویم که فیلدهای اجباری مورد نیاز آن ویژگی را دارد. این فیلدها کمی بین ابزارها، منابع و پیشنهادات متفاوت است.

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
        # اعتبارسنجی ورودی با استفاده از مدل پایدانتیک
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # انجام شود: افزودن پایدانتیک، تا بتوانیم یک AddInputModel بسازیم و پارامترها را اعتبارسنجی کنیم

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

در اینجا می‌بینید که ما موارد زیر را انجام می‌دهیم:

- با استفاده از Pydantic، اسکمای `AddInputModel` را با فیلدهای `a` و `b` در فایل *schema.py* ایجاد می‌کنیم.
- تلاش می‌کنیم که درخواست ورودی را به نوع `AddInputModel` تجزیه کنیم، اگر پارامترها همخوانی نداشته باشند، این باعث کرش می‌شود:

   ```python
   # add.py
    try:
        # اعتبارسنجی ورودی با استفاده از مدل Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

می‌توانید انتخاب کنید که این منطق تجزیه را در داخل خود فراخوانی ابزار قرار دهید یا در تابع هندلر.

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

// طرح‌واره.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// افزودن.ts
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

- در هندلری که به همه فراخوانی‌های ابزار رسیدگی می‌کند، حالا تلاش می‌کنیم درخواست ورودی را به اسکمای تعریف شده ابزار تبدیل کنیم:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    اگر موفق شود، ادامه می‌دهیم به فراخوانی خود ابزار:

    ```typescript
    const result = await tool.callback(input);
    ```

همانطور که می‌بینید، این رویکرد معماری عالی ایجاد می‌کند چون هر چیزی جای خودش را دارد، فایل *server.ts* خیلی کوچک است و فقط هندلرهای درخواست را تنظیم می‌کند و هر ویژگی در پوشه مربوط به خود یعنی tools/، resources/ یا /prompts قرار دارد.

عالی، بیایید این را بسازیم.

## تمرین: ایجاد یک سرور سطح پایین

در این تمرین، موارد زیر را انجام می‌دهیم:

1. ایجاد سرور سطح پایین که فهرست کردن ابزارها و فراخوانی ابزارها را هندل کند.
1. پیاده‌سازی معماری‌ای که بتوانید روی آن ساخت.
1. اضافه کردن اعتبارسنجی برای اطمینان از اینکه فراخوانی‌های ابزار به درستی اعتبارسنجی می‌شوند.

### -1- ایجاد معماری

اولین چیزی که باید حل کنیم معماری‌ای است که به ما کمک کند وقتی ویژگی‌های بیشتری اضافه می‌کنیم، مقیاس‌پذیر بماند، به این شکل است:

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

اکنون معماری‌ای داریم که تضمین می‌کند به راحتی می‌توانیم ابزارهای جدید در پوشه ابزارها اضافه کنیم. آزادید زیرپوشه‌هایی برای منابع و پیشنهادات نیز اضافه کنید.

### -2- ایجاد یک ابزار

ببینیم ایجاد یک ابزار به چه صورت است. ابتدا باید در زیرپوشه *tool* ایجاد شود به این شکل:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # اعتبارسنجی ورودی با استفاده از مدل Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: اضافه کردن Pydantic، تا بتوانیم یک AddInputModel بسازیم و آرگومان‌ها را اعتبارسنجی کنیم

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

اینجا می‌بینیم که نام، توضیح و اسکمای ورودی با Pydantic تعریف شده‌اند و یک هندلر وجود دارد که وقتی این ابزار فراخوانی شد، اجرا می‌شود. در نهایت `tool_add` را قرار می‌دهیم که یک دیکشنری شامل این ویژگی‌ها است.

همچنین *schema.py* وجود دارد که اسکمای ورودی مورد استفاده توسط ابزار ما را تعریف می‌کند:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

همچنین باید *__init__.py* را پر کنیم تا پوشه ابزارها به عنوان یک ماژول شناخته شود. علاوه بر این، باید ماژول‌های داخل آن را به این صورت منتشر کنیم:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

وقتی ابزارهای بیشتری اضافه کنیم، می‌توانیم به همین فایل اضافه کنیم.

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

در اینجا دیکشنری‌ای می‌سازیم که شامل ویژگی‌های زیر است:

- name، نام ابزار است.
- rawSchema، این اسکمای Zod است که برای اعتبارسنجی درخواست‌های ورودی به منظور فراخوانی این ابزار به کار می‌رود.
- inputSchema، این اسکما توسط هندلر استفاده می‌شود.
- callback، این برای فراخوانی ابزار استفاده می‌شود.

همچنین `Tool` استفاده می‌شود تا این دیکشنری به نوعی تبدیل شود که هندلر سرور MCP می‌تواند قبول کند، که به شکل زیر است:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

و *schema.ts* که اسکماهای ورودی هر ابزار را ذخیره می‌کند و به این صورت است، فعلاً فقط یک اسکما دارد اما با افزودن ابزارها ورودی‌های بیشتری اضافه می‌کنیم:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

عالی، اکنون به هندل کردن فهرست کردن ابزارها می‌پردازیم.

### -3- هندل کردن فهرست ابزارها

برای هندل کردن فهرست ابزارها، باید هندلر درخواست مناسب تعریف کنیم. این چیزی است که باید به فایل سرور اضافه کنیم:

**Python**

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

در اینجا دکوراتور `@server.list_tools` را اضافه و تابع پیاده‌سازی `handle_list_tools` را می‌سازیم. در آن باید فهرستی از ابزارها تولید کنیم. توجه داشته باشید که هر ابزار باید نام، توضیح و inputSchema داشته باشد.

**TypeScript**

برای تنظیم هندلر درخواست فهرست ابزارها، باید `setRequestHandler` را روی سرور با اسکمایی متناسب با عملکردمان یعنی `ListToolsRequestSchema` صدا بزنیم.

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
  // بازگشت فهرست ابزارهای ثبت شده
  return {
    tools: tools
  };
});
```

خوب، حالا بخش فهرست کردن ابزارها حل شد، بیایید به فراخوانی ابزارها نگاه کنیم.

### -4- هندل کردن فراخوانی ابزار

برای فراخوانی یک ابزار، باید هندلر درخواست دیگری تعریف کنیم که روی رسیدگی به درخواستی تمرکز دارد که مشخص می‌کند کدام ویژگی باید فراخوانی شود و با چه آرگومان‌هایی.

**Python**

از دکوراتور `@server.call_tool` استفاده کنیم و آن را با تابعی مانند `handle_call_tool` پیاده‌سازی کنیم. در این تابع باید نام ابزار، آرگومان‌های آن را استخراج کنیم و مطمئن شویم که آرگومان‌ها برای ابزار مورد نظر معتبرند. می‌توانیم اعتبارسنجی آرگومان‌ها را در این تابع انجام دهیم یا در خود ابزار.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools یک دیکشنری است که نام ابزارها را به عنوان کلیدها دارد
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # فراخوانی ابزار
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

شرح موارد:

- نام ابزار به عنوان پارامتر ورودی `name` حاضر است که برای آرگومان‌ها به صورت دیکشنری `arguments` است.

- ابزار با `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` فراخوانی می‌شود. اعتبارسنجی آرگومان‌ها در خاصیت `handler` انجام می‌شود که به تابعی اشاره دارد، اگر ناموفق بود استثنا پرتاب می‌شود.

اکنون فهم کاملی از فهرست کردن و فراخوانی ابزارها با استفاده از سرور سطح پایین داریم.

[مثال کامل](./code/README.md) را اینجا ببینید

## تمرین

کدی که داده شده را با چندین ابزار، منابع و پیشنهاد گسترش دهید و مشاهده کنید که تنها نیاز دارید فایل‌ها را در پوشه tools اضافه کنید و جای دیگری نیازی به تغییر نیست.

*راه حل ارائه نشده*

## خلاصه

در این فصل دیدیم که چگونه رویکرد سرور سطح پایین کار می‌کند و چگونه می‌تواند به ما کمک کند معماری زیبایی ایجاد کنیم که بتوانیم روی آن بسازیم. همچنین درباره اعتبارسنجی صحبت کردیم و نحوه کار با کتابخانه‌های اعتبارسنجی برای ایجاد اسکماهای اعتبارسنجی ورودی آموزش داده شد.

## بخش بعدی

- بعدی: [احراز هویت ساده](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئول هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->