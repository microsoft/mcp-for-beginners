# استفاده پیشرفته از سرور

در MCP SDK دو نوع سرور مختلف وجود دارد: سرور معمولی و سرور سطح پایین. معمولاً از سرور معمولی برای افزودن ویژگی‌ها استفاده می‌کنید. اما در برخی موارد، ممکن است بخواهید به سرور سطح پایین تکیه کنید، مانند:

- معماری بهتر. امکان ایجاد یک معماری تمیز با هر دو نوع سرور وجود دارد، اما می‌توان گفت که با سرور سطح پایین کمی آسان‌تر است.
- دسترسی به ویژگی‌ها. برخی از ویژگی‌های پیشرفته فقط با سرور سطح پایین قابل استفاده هستند. در فصل‌های بعدی خواهید دید که چگونه این ویژگی‌ها مانند نمونه‌گیری و استخراج اطلاعات اضافه می‌شوند.

## سرور معمولی در مقابل سرور سطح پایین

اینجا نحوه ایجاد یک MCP Server با استفاده از سرور معمولی آورده شده است:

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

نکته این است که شما به‌طور صریح هر ابزار، منبع یا درخواست مورد نظر خود را به سرور اضافه می‌کنید. این روش مشکلی ندارد.

### رویکرد سرور سطح پایین

با این حال، زمانی که از رویکرد سرور سطح پایین استفاده می‌کنید، باید به شکل متفاوتی فکر کنید. به جای ثبت هر ابزار، شما دو هندلر برای هر نوع ویژگی (ابزارها، منابع یا درخواست‌ها) ایجاد می‌کنید. برای مثال، ابزارها فقط دو تابع دارند، مانند:

- لیست کردن تمام ابزارها. یک تابع مسئول تمام تلاش‌ها برای لیست کردن ابزارها خواهد بود.
- مدیریت فراخوانی تمام ابزارها. در اینجا نیز فقط یک تابع برای مدیریت فراخوانی ابزارها وجود دارد.

این روش به نظر می‌رسد که کار کمتری نیاز دارد، درست است؟ بنابراین به جای ثبت یک ابزار، فقط باید مطمئن شوید که ابزار هنگام لیست کردن ابزارها نمایش داده می‌شود و هنگام دریافت درخواست برای فراخوانی ابزار، فراخوانی می‌شود.

بیایید نگاهی به کد بیندازیم:

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

در اینجا ما یک تابع داریم که لیستی از ویژگی‌ها را برمی‌گرداند. هر ورودی در لیست ابزارها اکنون دارای فیلدهایی مانند `name`، `description` و `inputSchema` است تا با نوع بازگشتی مطابقت داشته باشد. این امکان را به ما می‌دهد که ابزارها و تعریف ویژگی‌ها را در جای دیگری قرار دهیم. اکنون می‌توانیم تمام ابزارها را در یک پوشه ابزارها ایجاد کنیم و همین کار را برای تمام ویژگی‌ها انجام دهیم، بنابراین پروژه شما می‌تواند به این شکل سازماندهی شود:

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

این عالی است، معماری ما می‌تواند بسیار تمیز به نظر برسد.

در مورد فراخوانی ابزارها، آیا همان ایده است، یک هندلر برای فراخوانی ابزار، هر ابزاری؟ بله، دقیقاً، اینجا کد مربوط به آن آورده شده است:

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

همان‌طور که در کد بالا مشاهده می‌کنید، باید ابزار مورد نظر برای فراخوانی و آرگومان‌های مربوطه را تجزیه کنیم و سپس به فراخوانی ابزار ادامه دهیم.

## بهبود رویکرد با اعتبارسنجی

تا اینجا، دیدید که چگونه تمام ثبت‌ها برای افزودن ابزارها، منابع و درخواست‌ها می‌توانند با این دو هندلر برای هر نوع ویژگی جایگزین شوند. چه کار دیگری باید انجام دهیم؟ خوب، باید نوعی اعتبارسنجی اضافه کنیم تا مطمئن شویم ابزار با آرگومان‌های صحیح فراخوانی می‌شود. هر زمان اجرا راه‌حل خاص خود را برای این کار دارد، برای مثال Python از Pydantic و TypeScript از Zod استفاده می‌کند. ایده این است که موارد زیر را انجام دهیم:

- منطق ایجاد یک ویژگی (ابزار، منبع یا درخواست) را به پوشه اختصاصی آن منتقل کنیم.
- راهی برای اعتبارسنجی درخواست ورودی اضافه کنیم که مثلاً درخواست فراخوانی یک ابزار را بررسی کند.

### ایجاد یک ویژگی

برای ایجاد یک ویژگی، باید یک فایل برای آن ویژگی ایجاد کنیم و مطمئن شویم که دارای فیلدهای الزامی مورد نیاز آن ویژگی است. این فیلدها بسته به ابزارها، منابع و درخواست‌ها کمی متفاوت هستند.

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

در اینجا می‌توانید ببینید که چگونه موارد زیر را انجام می‌دهیم:

- ایجاد یک اسکیمای با استفاده از Pydantic `AddInputModel` با فیلدهای `a` و `b` در فایل *schema.py*.
- تلاش برای تجزیه درخواست ورودی به نوع `AddInputModel`. اگر پارامترها مطابقت نداشته باشند، این کار شکست خواهد خورد:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

می‌توانید انتخاب کنید که این منطق تجزیه را در خود فراخوانی ابزار یا در تابع هندلر قرار دهید.

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

- در هندلری که با تمام فراخوانی‌های ابزار سروکار دارد، اکنون تلاش می‌کنیم درخواست ورودی را به اسکیمای تعریف‌شده ابزار تجزیه کنیم:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    اگر این کار موفقیت‌آمیز باشد، سپس به فراخوانی ابزار واقعی ادامه می‌دهیم:

    ```typescript
    const result = await tool.callback(input);
    ```

همان‌طور که می‌بینید، این رویکرد یک معماری عالی ایجاد می‌کند، زیرا همه چیز جایگاه خود را دارد. فایل *server.ts* یک فایل بسیار کوچک است که فقط هندلرهای درخواست را تنظیم می‌کند و هر ویژگی در پوشه‌های مربوطه خود قرار دارد، یعنی tools/، resources/ یا /prompts.

عالی، بیایید سعی کنیم این را بسازیم.

## تمرین: ایجاد یک سرور سطح پایین

در این تمرین، موارد زیر را انجام خواهیم داد:

1. ایجاد یک سرور سطح پایین که لیست کردن ابزارها و فراخوانی ابزارها را مدیریت کند.
1. پیاده‌سازی یک معماری که بتوانید بر اساس آن بسازید.
1. افزودن اعتبارسنجی برای اطمینان از اینکه فراخوانی ابزارها به‌درستی اعتبارسنجی شده‌اند.

### -1- ایجاد معماری

اولین چیزی که باید به آن بپردازیم، معماری است که به ما کمک می‌کند با افزودن ویژگی‌های بیشتر مقیاس‌پذیر باشیم. اینجا نحوه انجام آن آورده شده است:

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

اکنون معماری‌ای تنظیم کرده‌ایم که تضمین می‌کند می‌توانیم به‌راحتی ابزارهای جدیدی را در یک پوشه ابزارها اضافه کنیم. می‌توانید از این روش برای افزودن زیرپوشه‌ها برای منابع و درخواست‌ها نیز استفاده کنید.

### -2- ایجاد یک ابزار

بیایید ببینیم ایجاد یک ابزار چگونه است. ابتدا باید در زیرپوشه *tool* ایجاد شود، مانند:

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

در اینجا می‌بینیم که چگونه نام، توضیحات، یک اسکیمای ورودی با استفاده از Pydantic و یک هندلر که هنگام فراخوانی این ابزار اجرا می‌شود را تعریف می‌کنیم. در نهایت، `tool_add` را که یک دیکشنری حاوی تمام این ویژگی‌ها است، ارائه می‌دهیم.

همچنین فایل *schema.py* وجود دارد که برای تعریف اسکیمای ورودی مورد استفاده ابزار ما استفاده می‌شود:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ما همچنین باید *__init__.py* را پر کنیم تا اطمینان حاصل کنیم که پوشه ابزارها به‌عنوان یک ماژول در نظر گرفته می‌شود. علاوه بر این، باید ماژول‌های داخل آن را به این شکل ارائه دهیم:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

می‌توانیم با افزودن ابزارهای بیشتر به این فایل ادامه دهیم.

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

در اینجا یک دیکشنری شامل ویژگی‌های زیر ایجاد می‌کنیم:

- name، این نام ابزار است.
- rawSchema، این اسکیمای Zod است که برای اعتبارسنجی درخواست‌های ورودی برای فراخوانی این ابزار استفاده می‌شود.
- inputSchema، این اسکیمای توسط هندلر استفاده خواهد شد.
- callback، این برای فراخوانی ابزار استفاده می‌شود.

همچنین `Tool` وجود دارد که برای تبدیل این دیکشنری به نوعی که هندلر سرور MCP بتواند بپذیرد استفاده می‌شود و به این شکل است:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

و فایل *schema.ts* وجود دارد که اسکیمای ورودی برای هر ابزار را ذخیره می‌کند و در حال حاضر فقط یک اسکیمای دارد، اما با افزودن ابزارهای بیشتر می‌توانیم ورودی‌های بیشتری اضافه کنیم:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

عالی، بیایید به مدیریت لیست کردن ابزارها ادامه دهیم.

### -3- مدیریت لیست ابزارها

برای مدیریت لیست کردن ابزارها، باید یک هندلر درخواست برای آن تنظیم کنیم. اینجا چیزی است که باید به فایل سرور خود اضافه کنیم:

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

در اینجا ما دکوریتور `@server.list_tools` و تابع پیاده‌سازی `handle_list_tools` را اضافه می‌کنیم. در دومی، باید لیستی از ابزارها تولید کنیم. توجه کنید که هر ابزار باید دارای نام، توضیحات و inputSchema باشد.

**TypeScript**

برای تنظیم هندلر درخواست برای لیست کردن ابزارها، باید `setRequestHandler` را روی سرور با اسکیمایی که با کاری که می‌خواهیم انجام دهیم مطابقت دارد، فراخوانی کنیم، در این مورد `ListToolsRequestSchema`.

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

عالی، اکنون بخش لیست کردن ابزارها را حل کرده‌ایم، بیایید به نحوه فراخوانی ابزارها نگاه کنیم.

### -4- مدیریت فراخوانی ابزار

برای فراخوانی ابزار، باید یک هندلر درخواست دیگر تنظیم کنیم، این بار متمرکز بر مدیریت یک درخواست که مشخص می‌کند کدام ویژگی فراخوانی شود و با چه آرگومان‌هایی.

**Python**

بیایید از دکوریتور `@server.call_tool` استفاده کنیم و آن را با تابعی مانند `handle_call_tool` پیاده‌سازی کنیم. در داخل این تابع، باید نام ابزار، آرگومان‌های آن را تجزیه کنیم و مطمئن شویم که آرگومان‌ها برای ابزار مورد نظر معتبر هستند. می‌توانیم آرگومان‌ها را در این تابع یا در پایین‌دست در ابزار واقعی اعتبارسنجی کنیم.

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

در اینجا چه اتفاقی می‌افتد:

- نام ابزار ما به‌عنوان پارامتر ورودی `name` موجود است، که برای آرگومان‌های ما به شکل دیکشنری `arguments` نیز صادق است.

- ابزار با `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` فراخوانی می‌شود. اعتبارسنجی آرگومان‌ها در ویژگی `handler` اتفاق می‌افتد که به یک تابع اشاره می‌کند، اگر این کار شکست بخورد، یک استثنا ایجاد خواهد کرد.

اکنون ما درک کاملی از لیست کردن و فراخوانی ابزارها با استفاده از یک سرور سطح پایین داریم.

مثال کامل را [اینجا](./code/README.md) ببینید.

## تکلیف

کدی که به شما داده شده است را با تعدادی ابزار، منابع و درخواست گسترش دهید و تأمل کنید که چگونه متوجه می‌شوید فقط نیاز دارید فایل‌ها را در پوشه ابزارها اضافه کنید و نه جای دیگر.

*هیچ راه‌حلی ارائه نشده است*

## خلاصه

در این فصل، دیدیم که رویکرد سرور سطح پایین چگونه کار می‌کند و چگونه می‌تواند به ما کمک کند یک معماری خوب ایجاد کنیم که بتوانیم بر اساس آن ادامه دهیم. همچنین در مورد اعتبارسنجی بحث کردیم و به شما نشان داده شد که چگونه با استفاده از کتابخانه‌های اعتبارسنجی اسکیمای‌هایی برای اعتبارسنجی ورودی ایجاد کنید.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.