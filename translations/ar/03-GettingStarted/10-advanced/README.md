# الاستخدام المتقدم للخادم

هناك نوعان مختلفان من الخوادم المعروضة في MCP SDK، الخادم العادي والخادم منخفض المستوى. عادةً، ستستخدم الخادم العادي لإضافة الميزات إليه. ولكن في بعض الحالات، تريد الاعتماد على الخادم منخفض المستوى مثل:

- هندسة أفضل. من الممكن إنشاء هندسة نظيفة باستخدام كل من الخادم العادي والخادم منخفض المستوى، ولكن يمكن الجدال بأنها أسهل قليلاً مع خادم منخفض المستوى.
- توافر الميزات. بعض الميزات المتقدمة يمكن استخدامها فقط مع خادم منخفض المستوى. ستشاهد هذا في الفصول اللاحقة مع إضافة التعيين والاستنباط.

## الخادم العادي مقابل الخادم منخفض المستوى

إليك كيف يبدو إنشاء خادم MCP باستخدام الخادم العادي

**Python**

```python
mcp = FastMCP("Demo")

# أضف أداة جمع
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

النقطة هي أنك تضيف صراحة كل أداة، أو مورد أو طلب تريد أن يمتلكه الخادم. لا شيء خاطئ في ذلك.  

### نهج الخادم منخفض المستوى

ومع ذلك، عند استخدام نهج الخادم منخفض المستوى تحتاج إلى التفكير بطريقة مختلفة. بدلاً من تسجيل كل أداة، تقوم بدلاً من ذلك بإنشاء معالجين لكل نوع ميزة (أدوات، موارد أو طلبات). لذلك على سبيل المثال، الأدوات تحتوي فقط على وظيفتين كما يلي:

- سرد جميع الأدوات. وظيفة واحدة ستكون مسؤولة عن جميع محاولات سرد الأدوات.
- التعامل مع استدعاء جميع الأدوات. هنا أيضا، هناك وظيفة واحدة فقط تتعامل مع استدعاءات الأدوات

هل يبدو هذا عملًا أقل محتملًا؟ لذا بدلاً من تسجيل أداة، فقط أحتاج إلى التأكد من أن الأداة مدرجة عندما أسرد كل الأدوات وأنه يتم استدعاؤها عندما يأتي طلب لاستدعاء أداة. 

لنلقي نظرة على كيف يبدو الكود الآن:

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

لدينا الآن وظيفة تُرجع قائمة بالميزات. كل إدخال في قائمة الأدوات يحتوي الآن على حقول مثل `name` و `description` و `inputSchema` للالتزام بنوع القيمة المرجعة. هذا يمكننا من وضع أدواتنا وتعريف الميزات في مكان آخر. يمكننا الآن إنشاء كل أدواتنا في مجلد أدوات وينطبق الشيء نفسه على جميع الميزات بحيث يمكن تنظيم مشروعك فجأة كما يلي:

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

هذا رائع، يمكن جعل هيكليتنا تبدو نظيفة جدًا.

ماذا عن استدعاء الأدوات، هل هي نفس الفكرة إذن، معالج واحد لاستدعاء أداة، أي أداة كانت؟ نعم، بالضبط، إليك الكود لذلك:

**Python**

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
    
    // الوسيطات: request.params.arguments
    // TODO الاتصال بالأداة،

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

كما ترى من الكود أعلاه، نحتاج إلى تحليل الأداة لاستدعائها وبأي وسائط، ثم نحتاج إلى المتابعة لاستدعاء الأداة.

## تحسين النهج بالتحقق

حتى الآن، رأيت كيف يمكن استبدال كل تسجيلاتك لإضافة الأدوات والموارد والطلبات بهذين المعالجين لكل نوع ميزة. ماذا نحتاج أن نفعل أيضًا؟ حسناً، يجب أن نضيف شكلًا من أشكال التحقق لضمان أن الأداة تُستدعى بالوسائط الصحيحة. لكل وقت تشغيل حله الخاص، على سبيل المثال تستخدم Python مكتبة Pydantic وتستخدم TypeScript مكتبة Zod. الفكرة هي أننا نقوم بما يلي:

- نقل منطق إنشاء ميزة (أداة، مورد أو طلب) إلى مجلدها المخصص.
- إضافة طريقة للتحقق من طلب وارد يطلب على سبيل المثال استدعاء أداة.

### إنشاء ميزة

لإنشاء ميزة، نحتاج إلى إنشاء ملف لتلك الميزة والتأكد من وجود الحقول الإلزامية المطلوبة لتلك الميزة. تختلف الحقول قليلاً بين الأدوات والموارد والطلبات.

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
        # التحقق من صحة الإدخال باستخدام نموذج Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # للقيام به: إضافة Pydantic، حتى نتمكن من إنشاء نموذج AddInputModel والتحقق من الوسائط input

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

هنا يمكنك رؤية كيف نقوم بما يلي:

- إنشاء مخطط باستخدام Pydantic `AddInputModel` مع حقول `a` و `b` في ملف *schema.py*.
- محاولة تحليل الطلب الوارد ليكون من نوع `AddInputModel`، إذا كان هناك عدم تطابق في المعلمات فسيتعطل:

   ```python
   # add.py
    try:
        # التحقق من صحة الإدخال باستخدام نموذج Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

يمكنك اختيار وضع هذا المنطق التحليلي داخل استدعاء الأداة نفسه أو في وظيفة المعالج.

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

- في المعالج الذي يتعامل مع جميع استدعاءات الأدوات، نحاول الآن تحليل الطلب الوارد إلى المخطط المحدد للأداة:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    إذا نجح هذا، نتابع لاستدعاء الأداة الفعلية:

    ```typescript
    const result = await tool.callback(input);
    ```

كما ترى، هذا النهج يخلق هندسة رائعة حيث لكل شيء مكانه، *server.ts* هو ملف صغير جدًا يربط فقط معالجات الطلبات وكل ميزة في مجلدها الخاص مثل tools/, resources/ أو /prompts.

رائع، لنحاول بناء هذا بعد ذلك. 

## التمرين: إنشاء خادم منخفض المستوى

في هذا التمرين، سنقوم بما يلي:

1. إنشاء خادم منخفض المستوى يتعامل مع سرد الأدوات واستدعاء الأدوات.
1. تنفيذ هندسة يمكنك البناء عليها.
1. إضافة التحقق لضمان أن استدعاءات أدواتك تم التحقق منها بشكل صحيح.

### -1- إنشاء هندسة

أول شيء نحتاج إلى معالجته هو هندسة تساعدنا على التوسع مع إضافة المزيد من الميزات، وهنا كيف تبدو:

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

الآن أعددنا هندسة تضمن أنه يمكننا بسهولة إضافة أدوات جديدة في مجلد الأدوات. لا تتردد في اتباع هذا لإضافة مجلدات فرعية للموارد والطلبات.

### -2- إنشاء أداة

لنرى كيف يبدو إنشاء أداة بعد ذلك. أولاً، يجب إنشاؤها في مجلد *tool* الفرعي كما يلي:

**Python**

```python
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

ما نراه هنا هو كيفية تعريف الاسم والوصف ومخطط الإدخال باستخدام Pydantic ومعالج سينادى عند استدعاء هذه الأداة. وأخيراً، نعرض `tool_add` وهو قاموس يحوي جميع هذه الخصائص.

هناك أيضًا *schema.py* يُستخدم لتعريف مخطط الإدخال المستخدم في أداتنا:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

نحتاج أيضًا إلى تعبئة *__init__.py* لضمان اعتبار مجلد الأدوات كوحدة. بالإضافة لذلك، نحتاج إلى تعريض الوحدات داخله كما يلي:

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

هنا ننشئ قاموسًا يتكون من الخصائص:

- name، هذا هو اسم الأداة.
- rawSchema، هذا هو مخطط Zod، سيستخدم للتحقق من صحة الطلبات الواردة لاستدعاء هذه الأداة.
- inputSchema، هذا المخطط سيستخدمه المعالج.
- callback، هذا يُستخدم لاستدعاء الأداة.

هناك أيضًا `Tool` التي تُستخدم لتحويل هذا القاموس إلى نوع يمكن لمعالج خادم mcp قبوله ويبدو كما يلي:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

وهناك *schema.ts* حيث نخزن مخططات الإدخال لكل أداة التي تبدو كما يلي مع مخطط واحد فقط حاليًا ولكن مع إضافة أدوات يمكننا إضافة المزيد من الإدخالات:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

رائع، لننتقل الآن للتعامل مع سرد أدواتنا.

### -3- التعامل مع سرد الأدوات

التالي، لمعالجة سرد الأدوات، نحتاج إلى إعداد معالج طلب لذلك. إليك ما نحتاج إلى إضافته لملف الخادم:

**Python**

```python
# تم حذف الكود للاختصار
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

هنا، نضيف المزين `@server.list_tools` والوظيفة المنفذة `handle_list_tools`. في الأخيرة، نحتاج إلى إنتاج قائمة بالأدوات. لاحظ كيف يجب أن تحتوي كل أداة على اسم، وصف و inputSchema.   

**TypeScript**

لإعداد معالج الطلب لسرد الأدوات، نحتاج إلى استدعاء `setRequestHandler` على الخادم مع مخطط يتناسب مع ما نحاول القيام به، في هذه الحالة `ListToolsRequestSchema`. 

```typescript
// الفهرس.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// الخادم.ts
// تم حذف الكود للاختصار
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // إرجاع قائمة الأدوات المسجلة
  return {
    tools: tools
  };
});
```

رائع، الآن حللنا جزء سرد الأدوات، لننظر كيف يمكننا استدعاء الأدوات بعد ذلك.

### -4- التعامل مع استدعاء أداة

لاستدعاء أداة، نحتاج إلى إعداد معالج طلب آخر، هذه المرة يركز على التعامل مع طلب يحدد أي ميزة يتم استدعاؤها وبأي وسيطات.

**Python**

لنستخدم المزين `@server.call_tool` وننفذه بوظيفة مثل `handle_call_tool`. داخل تلك الوظيفة، نحتاج إلى استخراج اسم الأداة، وسيطها والتأكد من أن الوسائط صالحة للأداة المعنية. يمكننا التحقق من الوسائط في هذه الوظيفة أو في الأداة نفسها.

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
        # استدعِ الأداة
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

إليك ما يحدث:

- اسم أداتنا موجود بالفعل كمعامل إدخال `name` وكذلك وسائطنا في شكل القاموس `arguments`.

- يتم استدعاء الأداة باستخدام `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. التحقق من صحة الوسائط يتم في خاصية `handler` التي تشير إلى وظيفة، إذا فشل هذا سيتم رفع استثناء.

الآن، لدينا فهم كامل لسرد واستدعاء الأدوات باستخدام خادم منخفض المستوى.

انظر [المثال الكامل](./code/README.md) هنا

## التعيين

قم بتمديد الكود الذي استلمته مع عدد من الأدوات والموارد والطلبات وانعكس على كيف تلاحظ أنك تحتاج فقط إلى إضافة ملفات في مجلد الأدوات ولا في أي مكان آخر.

*لا توجد حلول متوفرة*

## الملخص

في هذا الفصل، رأينا كيف يعمل نهج الخادم منخفض المستوى وكيف يمكن أن يساعدنا في إنشاء هندسة جيدة يمكننا الاستمرار في البناء عليها. ناقشنا أيضًا التحقق وتم عرض كيفية العمل مع مكتبات التحقق لإنشاء مخططات للتحقق من الإدخال.

## ماذا بعد

- التالي: [المصادقة البسيطة](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->