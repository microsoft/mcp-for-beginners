# שימוש מתקדם בשרת

ב-MCP SDK ישנם שני סוגי שרתים: השרת הרגיל והשרת ברמה נמוכה. בדרך כלל, תשתמשו בשרת הרגיל כדי להוסיף לו תכונות. עם זאת, במקרים מסוימים, כדאי להסתמך על השרת ברמה נמוכה, למשל:

- ארכיטקטורה טובה יותר. ניתן ליצור ארכיטקטורה נקייה גם עם השרת הרגיל וגם עם השרת ברמה נמוכה, אך ניתן לטעון שזה מעט קל יותר עם השרת ברמה נמוכה.
- זמינות תכונות. ישנן תכונות מתקדמות שניתן להשתמש בהן רק עם שרת ברמה נמוכה. תראו זאת בפרקים הבאים כשנוסיף דגימה והפקה.

## שרת רגיל מול שרת ברמה נמוכה

כך נראה יצירת שרת MCP עם השרת הרגיל:

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

הרעיון הוא שאתה מוסיף באופן מפורש כל כלי, משאב או הנחיה שתרצה שהשרת יכיל. אין בזה שום דבר רע.

### גישה של שרת ברמה נמוכה

עם זאת, כשאתה משתמש בגישה של שרת ברמה נמוכה, עליך לחשוב בצורה שונה. במקום לרשום כל כלי, אתה יוצר שני מטפלים לכל סוג תכונה (כלים, משאבים או הנחיות). לדוגמה, עבור כלים יש רק שתי פונקציות כמו כך:

- רשימת כל הכלים. פונקציה אחת תהיה אחראית לכל הניסיונות לרשום כלים.
- טיפול בקריאה לכל הכלים. גם כאן, יש רק פונקציה אחת שמטפלת בקריאות לכלי.

זה נשמע כמו פחות עבודה, נכון? במקום לרשום כלי, אני רק צריך לוודא שהכלי מופיע ברשימה כשאני רושם את כל הכלים ושניתן לקרוא לו כשיש בקשה נכנסת לקרוא לכלי.

בואו נסתכל על איך הקוד נראה עכשיו:

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

כאן יש לנו פונקציה שמחזירה רשימת תכונות. כל ערך ברשימת הכלים מכיל שדות כמו `name`, `description` ו-`inputSchema` כדי להתאים לסוג ההחזרה. זה מאפשר לנו לשים את ההגדרות של הכלים והתכונות במקום אחר. עכשיו אנחנו יכולים ליצור את כל הכלים שלנו בתיקיית כלים, וכך גם עבור כל התכונות, כך שהפרויקט שלנו יכול להיות מאורגן כך:

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

זה נהדר, הארכיטקטורה שלנו יכולה להיראות די נקייה.

מה לגבי קריאה לכלים? האם זה אותו רעיון, מטפל אחד לקריאה לכלי, לא משנה איזה כלי? כן, בדיוק, הנה הקוד לכך:

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

כפי שניתן לראות מהקוד לעיל, אנחנו צריכים לנתח את הכלי לקריאה, עם אילו ארגומנטים, ואז להמשיך לקרוא לכלי.

## שיפור הגישה עם ולידציה

עד כה, ראיתם איך כל הרישומים להוספת כלים, משאבים והנחיות יכולים להיות מוחלפים בשני מטפלים לכל סוג תכונה. מה עוד אנחנו צריכים לעשות? ובכן, כדאי להוסיף צורה כלשהי של ולידציה כדי להבטיח שהכלי נקרא עם הארגומנטים הנכונים. לכל סביבת ריצה יש פתרון משלה לכך, לדוגמה Python משתמשת ב-Pydantic ו-TypeScript משתמשת ב-Zod. הרעיון הוא שאנחנו עושים את הדברים הבאים:

- מעבירים את הלוגיקה ליצירת תכונה (כלי, משאב או הנחיה) לתיקייה ייעודית.
- מוסיפים דרך לוודא בקשה נכנסת שמבקשת, לדוגמה, לקרוא לכלי.

### יצירת תכונה

כדי ליצור תכונה, נצטרך ליצור קובץ עבור אותה תכונה ולוודא שיש לה את השדות החיוניים הנדרשים עבור אותה תכונה. אילו שדות משתנים מעט בין כלים, משאבים והנחיות.

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

כאן ניתן לראות איך אנחנו עושים את הדברים הבאים:

- יוצרים סכימה באמצעות Pydantic `AddInputModel` עם שדות `a` ו-`b` בקובץ *schema.py*.
- מנסים לנתח את הבקשה הנכנסת להיות מסוג `AddInputModel`, אם יש אי התאמה בפרמטרים זה יגרום לקריסה:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

אתם יכולים לבחור אם לשים את לוגיקת הניתוח הזו בקריאה לכלי עצמו או בפונקציית המטפל.

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

- במטפל שמתמודד עם כל קריאות הכלים, אנחנו מנסים לנתח את הבקשה הנכנסת לתוך הסכימה שהוגדרה עבור הכלי:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    אם זה עובד, אנחנו ממשיכים לקרוא לכלי עצמו:

    ```typescript
    const result = await tool.callback(input);
    ```

כפי שניתן לראות, הגישה הזו יוצרת ארכיטקטורה נהדרת שבה לכל דבר יש מקום משלו, הקובץ *server.ts* הוא קובץ קטן מאוד שמחבר את מטפלי הבקשות וכל תכונה נמצאת בתיקייה שלה, כלומר tools/, resources/ או /prompts.

נהדר, בואו ננסה לבנות את זה עכשיו.

## תרגיל: יצירת שרת ברמה נמוכה

בתרגיל הזה, נעשה את הדברים הבאים:

1. ניצור שרת ברמה נמוכה שמטפל ברישום כלים ובקריאה לכלים.
1. נממש ארכיטקטורה שניתן לבנות עליה.
1. נוסיף ולידציה כדי להבטיח שהקריאות לכלים מאומתות כראוי.

### -1- יצירת ארכיטקטורה

הדבר הראשון שאנחנו צריכים לטפל בו הוא ארכיטקטורה שעוזרת לנו להתרחב ככל שנוסיף עוד תכונות. הנה איך זה נראה:

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

עכשיו יש לנו ארכיטקטורה שמבטיחה שנוכל להוסיף בקלות כלים חדשים בתיקיית הכלים. אתם מוזמנים לעקוב אחרי זה כדי להוסיף תתי-תיקיות עבור משאבים והנחיות.

### -2- יצירת כלי

בואו נראה איך יצירת כלי נראית. קודם כל, הוא צריך להיווצר בתת-תיקיית *tool* כך:

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

מה שאנחנו רואים כאן זה איך אנחנו מגדירים שם, תיאור, סכימת קלט באמצעות Pydantic ומטפל שיקרא ברגע שהכלי מופעל. לבסוף, אנחנו חושפים את `tool_add` שהוא מילון שמחזיק את כל התכונות הללו.

יש גם *schema.py* שמשמש להגדרת סכימת הקלט שמשמשת את הכלי:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

אנחנו גם צריכים לאכלס את *__init__.py* כדי להבטיח שהתיקייה של הכלים תטופל כמודול. בנוסף, אנחנו צריכים לחשוף את המודולים שבתוכה כך:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

אנחנו יכולים להמשיך להוסיף לקובץ הזה ככל שנוסיף עוד כלים.

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

כאן אנחנו יוצרים מילון שמורכב מתכונות:

- name, זהו שם הכלי.
- rawSchema, זו סכימת Zod, היא תשמש לאימות בקשות נכנסות לקרוא לכלי הזה.
- inputSchema, סכימה זו תשמש את המטפל.
- callback, זה משמש להפעלת הכלי.

יש גם `Tool` שמשמש להמיר את המילון הזה לסוג שהמטפל של שרת MCP יכול לקבל, וזה נראה כך:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ויש *schema.ts* שבו אנחנו מאחסנים את סכימות הקלט עבור כל כלי, וזה נראה כך עם סכימה אחת בלבד כרגע, אבל ככל שנוסיף כלים נוכל להוסיף עוד ערכים:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

נהדר, בואו נמשיך לטפל ברישום הכלים הבא.

### -3- טיפול ברישום כלים

כדי לטפל ברישום הכלים, אנחנו צריכים להגדיר מטפל בקשות לכך. הנה מה שאנחנו צריכים להוסיף לקובץ השרת שלנו:

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

כאן אנחנו מוסיפים את הדקורטור `@server.list_tools` ואת הפונקציה המממשת `handle_list_tools`. בפונקציה הזו, אנחנו צריכים לייצר רשימת כלים. שימו לב שכל כלי צריך לכלול שם, תיאור ו-inputSchema.

**TypeScript**

כדי להגדיר את מטפל הבקשות לרישום כלים, אנחנו צריכים לקרוא ל-`setRequestHandler` על השרת עם סכימה שמתאימה למה שאנחנו מנסים לעשות, במקרה הזה `ListToolsRequestSchema`.

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

נהדר, עכשיו פתרנו את החלק של רישום כלים, בואו נסתכל על איך נוכל לקרוא לכלים הבא.

### -4- טיפול בקריאה לכלי

כדי לקרוא לכלי, אנחנו צריכים להגדיר מטפל בקשות נוסף, הפעם ממוקד בטיפול בבקשה שמפרטת איזו תכונה לקרוא ועם אילו ארגומנטים.

**Python**

בואו נשתמש בדקורטור `@server.call_tool` ונממש אותו עם פונקציה כמו `handle_call_tool`. בתוך הפונקציה הזו, אנחנו צריכים לנתח את שם הכלי, את הארגומנטים שלו ולהבטיח שהארגומנטים תקפים עבור הכלי המדובר. אנחנו יכולים לאמת את הארגומנטים בפונקציה הזו או בהמשך בכלי עצמו.

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

הנה מה שקורה:

- שם הכלי שלנו כבר קיים כפרמטר קלט `name`, וזה נכון גם עבור הארגומנטים בצורה של מילון `arguments`.

- הכלי נקרא עם `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. האימות של הארגומנטים מתרחש בתכונת `handler` שמצביעה על פונקציה, אם זה נכשל זה יגרום לחריגה.

זהו, עכשיו יש לנו הבנה מלאה של רישום וקריאה לכלים באמצעות שרת ברמה נמוכה.

ראו את [הדוגמה המלאה](./code/README.md) כאן.

## משימה

הרחיבו את הקוד שקיבלתם עם מספר כלים, משאבים והנחיות ושקלו איך אתם שמים לב שאתם רק צריכים להוסיף קבצים בתיקיית הכלים ולא בשום מקום אחר.

*אין פתרון נתון*

## סיכום

בפרק הזה, ראינו איך גישת שרת ברמה נמוכה עובדת ואיך היא יכולה לעזור לנו ליצור ארכיטקטורה יפה שניתן להמשיך לבנות עליה. דנו גם באימות והוצגו לכם דרכים לעבוד עם ספריות אימות כדי ליצור סכימות לאימות קלט.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.