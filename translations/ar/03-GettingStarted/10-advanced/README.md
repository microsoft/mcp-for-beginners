# استخدام الخادم المتقدم

هناك نوعان مختلفان من الخوادم المعروضة في MCP SDK، خادمك العادي وخادم منخفض المستوى. عادةً، ستستخدم الخادم العادي لإضافة ميزات إليه. ولكن في بعض الحالات، قد تريد الاعتماد على الخادم المنخفض المستوى مثل:

- هندسة أفضل. من الممكن إنشاء هندسة نظيفة مع كل من الخادم العادي والخادم منخفض المستوى، لكن يمكن القول إن الأمر أسهل قليلاً مع خادم منخفض المستوى.
- توافر الميزات. بعض الميزات المتقدمة يمكن استخدامها فقط مع
    خادم منخفض المستوى. تغطي الفصول اللاحقة ميزة الاستنباط والميزة القديمة للعينة
    التي تم إهمالها في MCP `2026-07-28`.

## الخادم العادي مقابل الخادم منخفض المستوى

هذا ما يبدو عليه إنشاء خادم MCP بالخادم العادي

**بايثون**

```python
mcp = FastMCP("Demo")

# أضف أداة الجمع
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**تايب سكريبت**

```typescript
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// أضف أداة جمع
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

النقطة هي أنك تضيف صراحة كل أداة أو مورد أو موجه تريد أن يمتلكه الخادم. لا يوجد خطأ في ذلك.  

### نهج الخادم منخفض المستوى

ومع ذلك، عندما تستخدم نهج الخادم منخفض المستوى، تحتاج إلى التفكير فيه بشكل مختلف. بدلاً من تسجيل كل أداة، تقوم بإنشاء معالجين لكل نوع ميزة (الأدوات، الموارد أو الموجهات). لذا، على سبيل المثال، تحتوي الأدوات على وظيفتين فقط كما يلي:

- سرد جميع الأدوات. وظيفة واحدة تكون مسؤولة عن جميع المحاولات لسرد الأدوات.
- التعامل مع استدعاء كل الأدوات. هنا أيضاً، هناك وظيفة واحدة فقط تتعامل مع استدعاءات أداة

هذا يبدو كأنه عمل أقل محتمل، أليس كذلك؟ لذا بدلاً من تسجيل أداة، فقط أحتاج إلى التأكد من أن الأداة مدرجة عندما أقوم بسرد جميع الأدوات وأنه يتم استدعاؤها عندما يكون هناك طلب وارد لاستدعاء أداة. 

لنلق نظرة على كيف يبدو الكود الآن:

**بايثون**

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

**تايب سكريبت**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // إرجاع قائمة الأدوات المسجلة
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

هنا لدينا وظيفة تُرجع قائمة بالميزات. كل مدخل في قائمة الأدوات الآن يحتوي على حقول مثل `name` و `description` و `inputSchema` لتتوافق مع نوع الإرجاع. هذا يمكننا من وضع أدواتنا وتعريف الميزات في مكان آخر. يمكننا الآن إنشاء جميع أدواتنا في مجلد أدوات ونفس الشيء لجميع ميزاتك بحيث يمكن تنظيم مشروعك فجأة كما يلي:

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

هذا رائع، يمكننا جعل هندستنا تبدو نظيفة إلى حد كبير.

ماذا عن استدعاء الأدوات، هل هي نفس الفكرة إذن، معالج واحد لاستدعاء أداة، أياً كانت؟ نعم، بالضبط، هذا هو الكود لذلك:

**بايثون**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # الأدوات هي قاموس يحتوي على أسماء الأدوات كمفاتيح
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

**تايب سكريبت**

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
    
    // الوسيطات: request.params.arguments
    // TODO استدعاء الأداة،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

كما ترى من الكود أعلاه، نحتاج إلى تحليل الأداة التي ستستدعى، ومع أي معاملات، ثم ننتقل لاستدعاء الأداة.

## تحسين النهج بالتحقق

حتى الآن، رأيت كيف يمكن استبدال جميع تسجيلاتك لإضافة الأدوات والموارد والموجهات بهذين المعالجين لكل نوع ميزة. ما الذي نحتاج لفعله أكثر؟ حسنًا، يجب علينا إضافة شكل من أشكال التحقق لضمان استدعاء الأداة بالمعاملات الصحيحة. لكل بيئة تشغيل حل خاص بها، على سبيل المثال تستخدم بايثون Pydantic وتستخدم تايب سكريبت Zod. الفكرة هي أننا نقوم بما يلي:

- نقل منطق إنشاء ميزة (أداة، مورد أو موجه) إلى مجلدها المخصص.
- إضافة طريقة للتحقق من طلب وارد يطلب مثلاً استدعاء أداة.

### إنشاء ميزة

لإنشاء ميزة، نحتاج إلى إنشاء ملف لتلك الميزة والتأكد من أن لديها الحقول الإلزامية المطلوبة لتلك الميزة. تختلف الحقول قليلاً بين الأدوات، الموارد والموجهات.

**بايثون**

```python
# سكيما.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# أضف.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # تحقق من صحة الإدخال باستخدام نموذج Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # يجب التنفيذ: أضف Pydantic، حتى نتمكن من إنشاء AddInputModel والتحقق من صحة الوسائط

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

هنا ترى كيف نفعل ما يلي:

- إنشاء مخطط باستخدام Pydantic `AddInputModel` يحتوي على حقول `a` و `b` في ملف *schema.py*.
- محاولة تحليل الطلب الوارد ليكون من نوع `AddInputModel`، إذا كان هناك عدم تطابق في المعلمات سينهي ذلك التنفيذ:

   ```python
   # add.py
    try:
        # التحقق من صحة الإدخال باستخدام نموذج Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

يمكنك اختيار ما إذا كنت تضع هذا المنطق التحليلي في استدعاء الأداة نفسها أو في وظيفة المعالج.

**تايب سكريبت**

```typescript
// الخادم.ts
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

       // @تجاهل-ts
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

// مخطط.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// إضافة.ts
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

- في المعالج الذي يتعامل مع جميع استدعاءات الأدوات، نحاول الآن تحليل الطلب الوارد إلى مخطط الأداة المعرفة:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    إذا نجح ذلك، بعد ذلك ننتقل لاستدعاء الأداة الفعلية:

    ```typescript
    const result = await tool.callback(input);
    ```

كما ترى، يخلق هذا النهج هندسة رائعة حيث يكون لكل شيء مكانه، الملف *server.ts* هو ملف صغير جدًا يربط فقط معالجات الطلبات، وكل ميزة في مجلدها الخاص مثل tools/، resources/ أو /prompts.

عظيم، دعنا نحاول بناء هذا الآن. 

## تمرين: إنشاء خادم منخفض المستوى

في هذا التمرين، سنقوم بالتالي:

1. إنشاء خادم منخفض المستوى يتعامل مع سرد الأدوات واستدعاء الأدوات.
1. تنفيذ هندسة يمكنك البناء عليها.
1. إضافة تحقق للتأكد من أن استدعاءات أدواتك يتم التحقق منها بشكل صحيح.

### -1- إنشاء هندسة

أول شيء نحتاج لمعرفته هو إنشاء هندسة تساعدنا في التوسع مع إضافة المزيد من الميزات، هكذا تبدو:

**بايثون**

```text
server.py
--| tools
----| __init__.py
----| add.py
----| schema.py
client.py
```

**تايب سكريبت**

```text
server.ts
--| tools
----| add.ts
----| schema.ts
client.ts
```

لقد قمنا الآن بإعداد هندسة تضمن أننا نستطيع إضافة أدوات جديدة بسهولة في مجلد الأدوات. لا تتردد في اتباع هذا لإنشاء مجلدات فرعية للموارد والموجهات.

### -2- إنشاء أداة

دعنا نرى ما هو شكل إنشاء أداة بعد ذلك. أولاً، يجب أن تُنشأ في دليله الفرعي *tool* كما يلي:

**بايثون**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # التحقق من صحة الإدخال باستخدام نموذج Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: إضافة Pydantic، حتى نتمكن من إنشاء AddInputModel والتحقق من صحة الوسائط

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ما نراه هنا هو كيف نعرّف الاسم، الوصف، ومخطط الإدخال باستخدام Pydantic ومعالج سيتم استدعاؤه بمجرد استدعاء هذه الأداة. وأخيراً، نعرض `tool_add` وهي قاموس يحتوي على كل هذه الخصائص.

هناك أيضًا *schema.py* يُستخدم لتعريف مخطط الإدخال الذي يستخدمه أداتنا:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

نحتاج أيضًا إلى تعبئة ملف *__init__.py* لضمان اعتبار دليل الأدوات كوحدة (module). بالإضافة، نحتاج إلى عرض الوحدات بداخله على النحو التالي:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

يمكننا الاستمرار في الإضافة إلى هذا الملف مع إضافة المزيد من الأدوات.

**تايب سكريبت**

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

هنا ننشئ قاموسًا مكونًا من الخصائص:

- name، هذا هو اسم الأداة.
- rawSchema، هذا هو مخطط Zod، سيتم استخدامه للتحقق من صحة الطلبات الواردة لاستدعاء هذه الأداة.
- inputSchema، سيتم استخدام هذا المخطط من قبل المعالج.
- callback، هذا يستخدم لاستدعاء الأداة.

هناك أيضًا `Tool` التي تُستخدم لتحويل هذا القاموس إلى نوع يمكن لمعالج خادم mcp قبوله ويبدو كالتالي:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

وهناك *schema.ts* حيث نخزن مخططات الإدخال لكل أداة التي تبدو كما يلي مع وجود مخطط واحد فقط في الوقت الحالي ولكن مع إضافة أدوات يمكننا إضافة المزيد من المدخلات:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

عظيم، لننتقل الآن لمعالجة سرد أدواتنا.

### -3- معالجة سرد الأدوات

بعد ذلك، لمعالجة سرد أدواتنا، نحتاج إلى إعداد معالج طلب لذلك. هذا ما نحتاج لإضافته إلى ملف الخادم:

**بايثون**

```python
# تم اختصار الكود للضرورة
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

هنا، نضيف الزينة `@server.list_tools` والوظيفة المنفذة `handle_list_tools`. في الوظيفة الأخيرة، نحتاج إلى إنتاج قائمة من الأدوات. لاحظ كيف أن كل أداة تحتاج إلى اسم، وصف و inputSchema.   

**تايب سكريبت**

لإعداد معالج الطلب لسرد الأدوات، نحتاج إلى استدعاء `setRequestHandler` على الخادم مع مخطط يتناسب مع ما نحاول القيام به، في هذه الحالة `ListToolsRequestSchema`. 

```typescript
// فهرس.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// خادم.ts
// تم حذف الكود للاختصار
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // إرجاع قائمة الأدوات المسجلة
  return {
    tools: tools
  };
});
```

عظيم، الآن حللنا جزء سرد الأدوات، دعنا نرى كيف يمكن استدعاء الأدوات بعد ذلك.

### -4- معالجة استدعاء أداة

لاستدعاء أداة، نحتاج إلى إعداد معالج طلب آخر، هذه المرة يركز على التعامل مع طلب يحدد أي ميزة سيتم استدعاؤها وبأي معاملات.

**بايثون**

لنستخدم الزينة `@server.call_tool` وننفذها بوظيفة مثل `handle_call_tool`. داخل تلك الوظيفة، نحتاج إلى استخراج اسم الأداة، معاملاتها والتأكد من صحة المعاملات الخاصة بالأداة المعنية. يمكننا التحقق من المعاملات في هذه الوظيفة أو لاحقاً في الأداة الفعلية.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # الأدوات هي قاموس بأسماء الأدوات كمفاتيح
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # استدعاء الأداة
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

هذا ما يحدث:

- اسم أداتنا موجود بالفعل كمعامل إدخال `name` وهذا صحيح بالنسبة لمعطياتنا في شكل قاموس `arguments`.

- يتم استدعاء الأداة بـ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. يحدث التحقق من المعاملات في خاصية `handler` التي تشير إلى وظيفة، إذا فشل ذلك سيتم رفع استثناء. 

الآن، لدينا فهم كامل لسرد واستدعاء الأدوات باستخدام خادم منخفض المستوى.

انظر [المثال الكامل](./code/README.md) هنا

## المهمة

قم بتوسيع الشيفرة التي حصلت عليها بعدد من الأدوات والموارد والموجهات وراجع كيف تلاحظ أنك تحتاج فقط إلى إضافة ملفات في دليل الأدوات وليس في أي مكان آخر. 

*لا توجد حل مقترح*

## الملخص

في هذا الفصل، شاهدنا كيف يعمل نهج الخادم منخفض المستوى وكيف يمكن أن يساعدنا في إنشاء هندسة جميلة يمكننا الاستمرار في البناء عليها. كما ناقشنا التحقق وتم عرض كيف تعمل مع مكتبات التحقق لإنشاء مخططات للتحقق من الإدخال.

## التالي

- التالي: [المصادقة البسيطة](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->