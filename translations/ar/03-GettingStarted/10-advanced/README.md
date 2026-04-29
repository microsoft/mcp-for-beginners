# الاستخدام المتقدم للخادم

هناك نوعان مختلفان من الخوادم المعروضة في MCP SDK، خادمك العادي والخادم منخفض المستوى. عادة، ستستخدم الخادم العادي لإضافة ميزات إليه. ولكن في بعض الحالات، تريد الاعتماد على الخادم منخفض المستوى مثل:

- هندسة أفضل. من الممكن إنشاء هندسة نظيفة باستخدام كل من الخادم العادي والخادم منخفض المستوى، لكن يمكن القول إن الأمر أسهل قليلاً مع الخادم منخفض المستوى.
- توفر الميزات. بعض الميزات المتقدمة لا يمكن استخدامها إلا مع خادم منخفض المستوى. سترى هذا في الفصول التالية مع إضافة السحب والاستنباط.

## الخادم العادي مقابل الخادم منخفض المستوى

هذا هو شكل إنشاء خادم MCP باستخدام الخادم العادي

**Python**

```python
mcp = FastMCP("Demo")

# أضف أداة الجمع
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

النقطة هي أنك تضيف صراحةً كل أداة أو مورد أو موجه تريد أن يحتوي عليه الخادم. لا عيب في ذلك.

### نهج الخادم منخفض المستوى

ومع ذلك، عند استخدام نهج الخادم منخفض المستوى، عليك التفكير فيه بشكل مختلف. بدلاً من تسجيل كل أداة، تقوم بدلاً من ذلك بإنشاء معالجين لكل نوع ميزة (أدوات، موارد أو موجهات). على سبيل المثال، الأدوات لديها وظيفتان فقط كما يلي:

- سرد كل الأدوات. وظيفة واحدة مسؤولة عن كل المحاولات لسرد الأدوات.
- التعامل مع استدعاء كل الأدوات. هنا أيضًا، هناك وظيفة واحدة فقط تتعامل مع استدعاء أداة.

يبدو هذا كما لو كان أقل عملاً، أليس كذلك؟ لذا بدلاً من تسجيل أداة، فقط يجب أن أتأكد من أن الأداة مدرجة عندما أسرد كل الأدوات وأنها تُستدعى عند وجود طلب وارد لاستدعاء أداة.

لنلق نظرة على شكل الكود الآن:

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

هنا لدينا الآن دالة تُرجع قائمة بالميزات. كل إدخال في قائمة الأدوات يحتوي الآن على حقول مثل `name`، `description` و `inputSchema` للامتثال لنوع الإرجاع. هذا يمكننا من وضع أدواتنا وتعريف الميزات في مكان آخر. يمكننا الآن إنشاء كل أدواتنا في مجلد الأدوات وينطبق الشيء نفسه على كل ميزاتك بحيث يمكن تنظيم مشروعك فجأة كما يلي:

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

هذا رائع، يمكن أن تبدو هندستنا نظيفة جدًا.

ماذا عن استدعاء الأدوات، هل هي نفس الفكرة إذًا، معالج واحد لاستدعاء أداة، أياً كانت؟ نعم بالضبط، هذا هو الكود لذلك:

**Python**

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
    
    // الوسائط: request.params.arguments
    // مهمة: استدعاء الأداة،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

كما ترى من الكود أعلاه، نحتاج إلى تحليل الأداة التي ستُستدعى، وبأي معطيات، ثم نحتاج إلى المتابعة في استدعاء الأداة.

## تحسين النهج مع التحقق

حتى الآن، رأيت كيف يمكن استبدال كل التسجيلات لإضافة أدوات، موارد وموجهات بهذين المعالجين لكل نوع ميزة. ماذا نحتاج إلى فعله أيضًا؟ حسنًا، يجب أن نضيف نوعًا من التحقق لضمان أن الأداة تُستدعى بالمعطيات الصحيحة. لكل بيئة تشغيل حلها الخاص لهذا، على سبيل المثال تستخدم Python Pydantic و TypeScript تستخدم Zod. الفكرة هي أننا نقوم بما يلي:

- نقل المنطق لإنشاء ميزة (أداة، مورد أو موجه) إلى مجلدها المخصص.
- إضافة طريقة للتحقق من صحة طلب وارد يطلب مثلاً استدعاء أداة.

### إنشاء ميزة

لإنشاء ميزة، سنحتاج إلى إنشاء ملف لتلك الميزة والتأكد من أنه يحتوي على الحقول الإلزامية المطلوبة لتلك الميزة. تختلف الحقول قليلاً بين الأدوات، الموارد والموجهات.

**Python**

```python
# سكيمة.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# إضافة.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # تحقق من صحة الإدخال باستخدام نموذج Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: أضف Pydantic، حتى نتمكن من إنشاء AddInputModel والتحقق من صحة الوسائط

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

- إنشاء مخطط باستخدام Pydantic `AddInputModel` بالحقول `a` و `b` في الملف *schema.py*.
- محاولة تحليل الطلب الوارد ليكون من نوع `AddInputModel`، إذا حدث عدم تطابق في المعلمات سيؤدي ذلك إلى تعطل:

   ```python
   # add.py
    try:
        # التحقق من صحة الإدخال باستخدام نموذج Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

يمكنك اختيار ما إذا كنت تضع منطق التحليل هذا في استدعاء الأداة نفسه أو في دالة المعالج.

**TypeScript**

```typescript
// سيرفر.ts
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

- في المعالج الذي يتعامل مع كل استدعاءات الأدوات، نحاول الآن تحليل الطلب الوارد إلى مخطط محدد للأداة:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    إذا نجح ذلك فنستمر في استدعاء الأداة الفعلية:

    ```typescript
    const result = await tool.callback(input);
    ```

كما ترى، هذا النهج يخلق هندسة رائعة حيث لكل شيء مكانه، *server.ts* هو ملف صغير جدًا يربط فقط معالجات الطلبات ولكل ميزة مجلدها الخاص مثل tools/، resources/ أو /prompts.

رائع، لنحاول بناء هذا بعد ذلك.

## التمرين: إنشاء خادم منخفض المستوى

في هذا التمرين، سنقوم بالتالي:

1. إنشاء خادم منخفض المستوى يتعامل مع سرد الأدوات واستدعاء الأدوات.
2. تنفيذ هندسة يمكنك البناء عليها.
3. إضافة التحقق لضمان أن استدعاءات أدواتك مُحققة بشكل صحيح.

### -1- إنشاء هندسة

أول شيء نحتاج لمناقشته هو هندسة تساعدنا على التوسيع مع إضافة مزيد من الميزات، هكذا تبدو:

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

الآن قمنا بإعداد هندسة تضمن أننا يمكننا بسهولة إضافة أدوات جديدة في مجلد الأدوات. لا تتردد في اتباع هذا لإضافة مجلدات فرعية للموارد والموجهات.

### -2- إنشاء أداة

لنرَ كيف يبدو إنشاء أداة بعد ذلك. أولاً، يجب إنشاؤها في المجلد الفرعي *tool* هكذا:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # التحقق من صحة الإدخال باستخدام نموذج Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # مهمة: أضف Pydantic، حتى نتمكن من إنشاء نموذج AddInputModel والتحقق من صحة الوسيطات

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ما نراه هنا هو كيف نحدد الاسم، الوصف ومخطط الإدخال باستخدام Pydantic ومعالج سيتم استدعاؤه عند استدعاء هذه الأداة. وأخيرًا، نعرض `tool_add` وهو قاموس يحتوي على كل هذه الخصائص.

يوجد أيضاً *schema.py* يُستخدم لتعريف مخطط الإدخال المستخدم من قبل أداتنا:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

نحن بحاجة أيضاً لملء *__init__.py* لضمان التعامل مع مجلد الأدوات كوحدة. بالإضافة إلى ذلك، نحتاج إلى عرض الوحدات بداخله هكذا:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

يمكننا الاستمرار في الإضافة إلى هذا الملف مع إضافة المزيد من الأدوات.

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

هنا ننشئ قاموس يتكون من الخصائص التالية:

- name، هذا هو اسم الأداة.
- rawSchema، هذا هو مخطط Zod، سيستخدم للتحقق من صحة الطلبات الواردة لاستدعاء هذه الأداة.
- inputSchema، هذا المخطط سيستخدمه المعالج.
- callback، هذا يُستخدم لاستدعاء الأداة.

يوجد أيضًا `Tool` الذي يُستخدم لتحويل هذا القاموس إلى نوع يمكن لمعالج خادم mcp قبوله ويبدو هكذا:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

وهناك *schema.ts* حيث نخزن مخططات الإدخال لكل أداة ويبدو هكذا مع مخطط واحد فقط حاليا، لكن مع إضافة أدوات يمكن إضافة المزيد:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

رائع، لننتقل لمعالجة سرد أدواتنا بعد ذلك.

### -3- معالجة سرد الأدوات

التالي، لمعالجة سرد أدواتنا، نحتاج إلى إعداد معالج للطلبات لذلك. هذا ما نحتاج إضافته لملف الخادم الخاص بنا:

**Python**

```python
# تم حذف الشيفرة للاختصار
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

هنا نضيف المزخرف `@server.list_tools` والدالة المنفذة `handle_list_tools`. في الأخيرة، نحتاج إلى إنشاء قائمة بالأدوات. لاحظ كيف كل أداة تحتاج إلى أن تحتوي على اسم، وصف وinputSchema.

**TypeScript**

لإعداد معالج الطلب لسرد الأدوات، نحتاج لاستدعاء `setRequestHandler` على الخادم مع مخطط يناسب ما نحاول القيام به، في هذه الحالة `ListToolsRequestSchema`.

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

رائع، الآن حللنا جزء سرد الأدوات، لنتطلع كيف يمكننا استدعاء الأدوات بعد ذلك.

### -4- معالجة استدعاء أداة

لاستدعاء أداة، نحتاج إلى إعداد معالج طلب آخر، هذه المرة يركز على التعامل مع طلب يحدد أي ميزة ستُستدعى وبأي معطيات.

**Python**

لنستخدم المزخرف `@server.call_tool` وننفذه بدالة مثل `handle_call_tool`. داخل تلك الدالة، نحتاج لتحليل اسم الأداة، المعطيات والتأكد من صحة المعطيات الخاصة بالأداة المعنية. يمكننا التحقق من المعطيات في هذه الدالة أو لاحقًا في الأداة الفعلية.

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

- اسم أداتنا موجود بالفعل كمعامل إدخال `name` وهو صحيح بالنسبة لمعطياتنا في شكل قاموس `arguments`.

- يتم استدعاء الأداة بـ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. يتحقق المعالج من المعطيات في خاصية `handler` التي تشير إلى دالة، إذا فشل ذلك سيثير استثناء.

هكذا، لدينا فهم كامل لسرد واستدعاء الأدوات باستخدام خادم منخفض المستوى.

شاهد [المثال الكامل](./code/README.md) هنا

## المهمة

وسّع الكود الذي استلمته بعدد من الأدوات، الموارد والموجهات وانعكس على كيف تلاحظ أنك تحتاج فقط لإضافة ملفات في مجلد الأدوات ولا في أي مكان آخر.

*لا توجد حلول مقدمة*

## الملخص

في هذا الفصل، رأينا كيف يعمل نهج الخادم منخفض المستوى وكيف يمكن أن يساعدنا على إنشاء هندسة لطيفة نستمر في البناء عليها. ناقشنا أيضًا التحقق وتم شرح كيفية العمل مع مكتبات التحقق لإنشاء مخططات للتحقق من الإدخال.

## القادم

- التالي: [المصادقة البسيطة](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للمعلومات الحساسة أو الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أية سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->