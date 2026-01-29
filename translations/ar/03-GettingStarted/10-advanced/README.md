# استخدام الخادم المتقدم

هناك نوعان مختلفان من الخوادم التي يتم توفيرها في MCP SDK، الخادم العادي والخادم منخفض المستوى. عادةً، ستستخدم الخادم العادي لإضافة ميزات إليه. ومع ذلك، في بعض الحالات، قد تحتاج إلى الاعتماد على الخادم منخفض المستوى مثل:

- هيكلية أفضل. من الممكن إنشاء هيكلية نظيفة باستخدام كل من الخادم العادي والخادم منخفض المستوى، ولكن يمكن القول إنه أسهل قليلاً مع الخادم منخفض المستوى.
- توفر الميزات. بعض الميزات المتقدمة يمكن استخدامها فقط مع الخادم منخفض المستوى. سترى ذلك في الفصول القادمة عندما نضيف أخذ العينات والاستنباط.

## الخادم العادي مقابل الخادم منخفض المستوى

هكذا يبدو إنشاء خادم MCP باستخدام الخادم العادي:

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

الفكرة هنا أنك تضيف بشكل صريح كل أداة أو مورد أو مطالبة تريد أن يحتوي عليها الخادم. لا مشكلة في ذلك.

### نهج الخادم منخفض المستوى

ومع ذلك، عند استخدام نهج الخادم منخفض المستوى، تحتاج إلى التفكير بطريقة مختلفة، حيث بدلاً من تسجيل كل أداة، تقوم بإنشاء معالجين لكل نوع من الميزات (الأدوات، الموارد أو المطالبات). على سبيل المثال، بالنسبة للأدوات، سيكون هناك وظيفتان فقط مثل:

- سرد جميع الأدوات. وظيفة واحدة ستكون مسؤولة عن جميع محاولات سرد الأدوات.
- معالجة استدعاء جميع الأدوات. هنا أيضًا، هناك وظيفة واحدة فقط لمعالجة استدعاء أداة.

يبدو ذلك وكأنه عمل أقل، أليس كذلك؟ بدلاً من تسجيل أداة، فقط تحتاج إلى التأكد من أن الأداة مدرجة عند سرد جميع الأدوات وأنه يتم استدعاؤها عند وجود طلب وارد لاستدعاء أداة.

لنلقِ نظرة على كيف يبدو الكود الآن:

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

هنا لدينا الآن وظيفة تُرجع قائمة بالميزات. كل إدخال في قائمة الأدوات يحتوي الآن على حقول مثل `name`، `description` و `inputSchema` لتتوافق مع نوع الإرجاع. هذا يمكننا من وضع تعريف الأدوات والميزات في مكان آخر. يمكننا الآن إنشاء جميع أدواتنا في مجلد الأدوات، وينطبق نفس الشيء على جميع ميزاتك، بحيث يمكن تنظيم مشروعك فجأة كما يلي:

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

هذا رائع، يمكننا جعل الهيكلية تبدو نظيفة جدًا.

ماذا عن استدعاء الأدوات، هل هي نفس الفكرة، معالج واحد لاستدعاء أداة، أي أداة؟ نعم، بالضبط، إليك الكود لذلك:

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

كما ترى من الكود أعلاه، نحتاج إلى تحليل الأداة التي سيتم استدعاؤها، ومع أي معطيات، ثم نحتاج إلى المتابعة لاستدعاء الأداة.

## تحسين النهج باستخدام التحقق

حتى الآن، رأيت كيف يمكن استبدال جميع تسجيلاتك لإضافة الأدوات، الموارد والمطالبات بهذه المعالجات لكل نوع من الميزات. ماذا أيضًا نحتاج إلى القيام به؟ حسنًا، يجب أن نضيف نوعًا من التحقق للتأكد من أن الأداة يتم استدعاؤها بالمعطيات الصحيحة. كل وقت تشغيل لديه حله الخاص لهذا، على سبيل المثال Python يستخدم Pydantic و TypeScript يستخدم Zod. الفكرة هي أننا نقوم بما يلي:

- نقل المنطق لإنشاء ميزة (أداة، مورد أو مطالبة) إلى مجلدها المخصص.
- إضافة طريقة للتحقق من الطلب الوارد الذي يطلب على سبيل المثال استدعاء أداة.

### إنشاء ميزة

لإنشاء ميزة، سنحتاج إلى إنشاء ملف لتلك الميزة والتأكد من أنه يحتوي على الحقول الإلزامية المطلوبة لتلك الميزة. تختلف الحقول قليلاً بين الأدوات، الموارد والمطالبات.

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

هنا يمكنك أن ترى كيف نقوم بما يلي:

- إنشاء مخطط باستخدام Pydantic `AddInputModel` مع الحقول `a` و `b` في ملف *schema.py*.
- محاولة تحليل الطلب الوارد ليكون من نوع `AddInputModel`، إذا كان هناك عدم تطابق في المعطيات، فسيحدث خطأ:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

يمكنك اختيار وضع منطق التحليل هذا في استدعاء الأداة نفسه أو في وظيفة المعالج.

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

- في المعالج الذي يتعامل مع جميع استدعاءات الأدوات، نحاول الآن تحليل الطلب الوارد إلى المخطط المحدد للأداة:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    إذا نجح ذلك، نتابع لاستدعاء الأداة الفعلية:

    ```typescript
    const result = await tool.callback(input);
    ```

كما ترى، هذا النهج يخلق هيكلية رائعة حيث كل شيء له مكانه، ملف *server.ts* هو ملف صغير جدًا فقط يقوم بتوصيل معالجات الطلبات وكل ميزة موجودة في مجلدها الخاص مثل tools/، resources/ أو /prompts.

رائع، دعونا نحاول بناء هذا الآن.

## تمرين: إنشاء خادم منخفض المستوى

في هذا التمرين، سنقوم بما يلي:

1. إنشاء خادم منخفض المستوى يتعامل مع سرد الأدوات واستدعاء الأدوات.
1. تنفيذ هيكلية يمكنك البناء عليها.
1. إضافة التحقق للتأكد من أن استدعاءات الأدوات يتم التحقق منها بشكل صحيح.

### -1- إنشاء هيكلية

أول شيء نحتاج إلى معالجته هو هيكلية تساعدنا على التوسع مع إضافة المزيد من الميزات، هكذا تبدو:

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

الآن قمنا بإعداد هيكلية تضمن أنه يمكننا بسهولة إضافة أدوات جديدة في مجلد الأدوات. لا تتردد في اتباع هذا لإضافة مجلدات فرعية للموارد والمطالبات.

### -2- إنشاء أداة

لنرى كيف يبدو إنشاء أداة بعد ذلك. أولاً، يجب أن يتم إنشاؤها في مجلدها الفرعي *tool* كما يلي:

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

ما نراه هنا هو كيف نحدد الاسم، الوصف، مخطط الإدخال باستخدام Pydantic ومعالج سيتم استدعاؤه بمجرد استدعاء هذه الأداة. أخيرًا، نقوم بتعريض `tool_add` وهو قاموس يحتوي على جميع هذه الخصائص.

هناك أيضًا *schema.py* الذي يُستخدم لتحديد مخطط الإدخال المستخدم بواسطة أداتنا:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

نحتاج أيضًا إلى ملء *__init__.py* لضمان التعامل مع مجلد الأدوات كأنه وحدة. بالإضافة إلى ذلك، نحتاج إلى تعريض الوحدات داخله كما يلي:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

يمكننا الاستمرار في إضافة إلى هذا الملف مع إضافة المزيد من الأدوات.

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

هنا نقوم بإنشاء قاموس يتكون من الخصائص:

- name، هذا هو اسم الأداة.
- rawSchema، هذا هو مخطط Zod، سيتم استخدامه للتحقق من الطلبات الواردة لاستدعاء هذه الأداة.
- inputSchema، هذا المخطط سيتم استخدامه بواسطة المعالج.
- callback، يتم استخدامه لاستدعاء الأداة.

هناك أيضًا `Tool` الذي يُستخدم لتحويل هذا القاموس إلى نوع يمكن أن يقبله معالج خادم MCP، ويبدو كما يلي:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

وهناك *schema.ts* حيث نخزن مخططات الإدخال لكل أداة، ويبدو كما يلي مع مخطط واحد فقط في الوقت الحالي، ولكن مع إضافة أدوات يمكننا إضافة المزيد من الإدخالات:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

رائع، دعونا نتابع التعامل مع سرد أدواتنا بعد ذلك.

### -3- التعامل مع سرد الأدوات

بعد ذلك، للتعامل مع سرد الأدوات، نحتاج إلى إعداد معالج طلب لذلك. إليك ما نحتاج إلى إضافته إلى ملف الخادم الخاص بنا:

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

هنا نضيف الزخرفة `@server.list_tools` والوظيفة المنفذة `handle_list_tools`. في الأخيرة، نحتاج إلى إنتاج قائمة بالأدوات. لاحظ كيف يجب أن تحتوي كل أداة على اسم، وصف ومخطط إدخال.

**TypeScript**

لإعداد معالج الطلب لسرد الأدوات، نحتاج إلى استدعاء `setRequestHandler` على الخادم مع مخطط يناسب ما نحاول القيام به، في هذه الحالة `ListToolsRequestSchema`.

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

رائع، الآن قمنا بحل جزء سرد الأدوات، دعونا نلقي نظرة على كيفية استدعاء الأدوات بعد ذلك.

### -4- التعامل مع استدعاء أداة

لاستدعاء أداة، نحتاج إلى إعداد معالج طلب آخر، هذه المرة يركز على التعامل مع طلب يحدد أي ميزة يتم استدعاؤها ومع أي معطيات.

**Python**

دعونا نستخدم الزخرفة `@server.call_tool` وننفذها بوظيفة مثل `handle_call_tool`. داخل تلك الوظيفة، نحتاج إلى تحليل اسم الأداة، معطياتها والتأكد من أن المعطيات صالحة للأداة المعنية. يمكننا التحقق من المعطيات في هذه الوظيفة أو في الأداة نفسها.

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

هنا ما يحدث:

- اسم أداتنا موجود بالفعل كمعطى إدخال `name`، وهو صحيح بالنسبة لمعطياتنا في شكل قاموس `arguments`.

- يتم استدعاء الأداة باستخدام `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. يتم التحقق من المعطيات في خاصية `handler` التي تشير إلى وظيفة، إذا فشل ذلك، سيتم رفع استثناء.

هناك، الآن لدينا فهم كامل لسرد واستدعاء الأدوات باستخدام خادم منخفض المستوى.

راجع [المثال الكامل](./code/README.md) هنا

## المهمة

قم بتوسيع الكود الذي تم إعطاؤه لك مع عدد من الأدوات، الموارد والمطالبات، وفكر في كيف تلاحظ أنك تحتاج فقط إلى إضافة ملفات في مجلد الأدوات وليس في أي مكان آخر.

*لا توجد حل مقدم*

## الملخص

في هذا الفصل، رأينا كيف يعمل نهج الخادم منخفض المستوى وكيف يمكن أن يساعدنا في إنشاء هيكلية جيدة يمكننا الاستمرار في البناء عليها. كما ناقشنا التحقق وتم عرض كيفية العمل مع مكتبات التحقق لإنشاء مخططات للتحقق من الإدخال.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.