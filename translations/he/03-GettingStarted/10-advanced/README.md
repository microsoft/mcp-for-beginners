# שימוש מתקדם בשרת

יש שני סוגים שונים של שרתים המוצגים ב-MCP SDK, השרת הרגיל שלך והשרת ברמה נמוכה. בדרך כלל, תשתמש בשרת הרגיל כדי להוסיף לו תכונות. עם זאת, במקרים מסוימים תרצה להסתמך על השרת ברמה נמוכה כמו:

- ארכיטקטורה טובה יותר. ניתן ליצור ארכיטקטורה נקייה עם השרת הרגיל והשרת ברמה נמוכה אבל ניתן לטעון שזה מעט קל יותר עם שרת ברמה נמוכה.
- זמינות תכונות. חלק מהתכונות המתקדמות ניתן להשתמש רק עם שרת ברמה נמוכה. תראה את זה בפרקים הבאים כשנוסיף דגימה ואילוץ.

## שרת רגיל מול שרת ברמה נמוכה

כך נראה יצירת שרת MCP עם השרת הרגיל

**Python**

```python
mcp = FastMCP("Demo")

# הוסף כלי חיבור
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

// הוסף כלי חיבור
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

העניין הוא שאתה מוסיף במפורש כל כלי, משאב או הנחיה שברצונך שהשרת יכלול. אין בזה שום דבר לא נכון.

### גישת שרת ברמה נמוכה

עם זאת, כשאתה משתמש בגישת השרת ברמה נמוכה, צריך לחשוב אחרת. במקום לרשום כל כלי, אתה יוצר שני מטפלים לכל סוג תכונה (כלים, משאבים או הנחיות). למשל, לכלים יש רק שתי פונקציות כך:

- הצגת כל הכלים. פונקציה אחת תהיה אחראית על כל הניסיונות להציג כלים.
- טיפול בקריאה לכל הכלים. גם כאן, יש פונקציה אחת שמטפלת בקריאות לכלי.

נשמע כמו פחות עבודה אולי? אז במקום לרשום כלי, רק צריך לוודא שהכלי מופיע ברשימת הכלים ושהוא מזומן כשיש בקשה לקרוא לכלי.

בוא נראה איך הקוד נראה עכשיו:

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
  // החזר את רשימת הכלים הרשומים
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

כעת יש לנו פונקציה שמחזירה רשימת תכונות. כל רשומה ברשימת הכלים כוללת שדות כמו `name`, `description` ו-`inputSchema` כדי להתאים לסוג החזרה. זה מאפשר לנו למקם את הכלים וההגדרות שלהם במקום אחר. ניתן כעת ליצור את כל הכלים בתיקיית כלים וכך גם לגבי כל התכונות, כך שהפרויקט שלך יכול להיות מאורגן כך:

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

זה מצוין, הארכיטקטורה שלנו יכולה להיות נקייה ומסודרת.

ומה לגבי קריאות לכלים, האם זה הרעיון האחד אז, מטפל אחד לקרוא לכלי, לא משנה איזה? כן, בדיוק, זה הקוד לכך:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools הוא מילון עם שמות כלים כמפתחות
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
    
    // ארגומנטים: request.params.arguments
    // יש לקרוא לכלי,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

כפי שניתן לראות מהקוד למעלה, אנחנו צריכים לנתח את הכלי שצריך להזמן, ואיזה ארגומנטים, ואז להמשיך לקרוא לכלי.

## שיפור הגישה עם ולידציה

עד עכשיו, ראית כיצד כל ההרשמות שלך להוספת כלים, משאבים והנחיות יכולות להיות מוחלפות בשני מטפלים לכל סוג תכונה. מה עוד צריך לעשות? יש להוסיף סוג של ולידציה כדי לוודא שהכלי נקרא עם ארגומנטים נכונים. לכל סביבת ריצה יש פתרון שונה, למשל ב-Python משתמשים ב-Pydantic וב-TypeScript ב-Zod. הרעיון הוא לבצע את הפעולות הבאות:

- להעביר את הלוגיקה ליצירת תכונה (כלי, משאב או הנחיה) לתיקייה ייעודית.
- להוסיף דרך לאמת בקשה נכנסת, למשל לקרוא כלי.

### צור תכונה

ליצירת תכונה, צריך ליצור קובץ עבורה ולוודא שיש בו את השדות הנדרשים לאותה תכונה. השדות משתנים במקצת בין כלים, משאבים והנחיות.

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
        # אמת קלט באמצעות מודל Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: להוסיף Pydantic, כדי שנוכל ליצור AddInputModel ולאמת את הפרמטרים

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

כאן רואים איך עושים את הפעולות הבאות:

- יצירת סכמה בעזרת Pydantic בשם `AddInputModel` עם שדות `a` ו-`b` בקובץ *schema.py*.
- ניסיון לנתח את הבקשה שנכנסת כדי שתתאים לסוג `AddInputModel`, אם יש חוסר התאמה בפרמטרים זה יגרום לקריסה:

   ```python
   # add.py
    try:
        # אמת קלט באמצעות מודל Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ניתן לבחור אם לשים את לוגיקת הניתוח בתוך קריאת הכלי עצמה או בתוך פונקציית המטפל.

**TypeScript**

```typescript
// שרת.ts
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

       // @ts-התעלם
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

// סכימה.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// הוסף.ts
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

- במטפל המטפל בכל קריאות הכלים, עכשיו מנסים לנתח את הבקשה הנכנסת לפי הסכמה שהוגדרה לכלי:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    אם זה עובד, ממשיכים לקרוא לכלי בפועל:

    ```typescript
    const result = await tool.callback(input);
    ```

כפי שניתן לראות, גישה זו יוצרת ארכיטקטורה טובה שבה לכל דבר יש את מקומו, הקובץ *server.ts* הוא קטן מאוד ומחבר רק את המטפלים והכל תכונה נמצאת בתיקייה הייעודית שלה, כלומר tools/, resources/ או /prompts.

מצוין, בוא ננסה לבנות את זה עכשיו.

## תרגיל: יצירת שרת ברמה נמוכה

בתרגיל זה נעשה את הפעולות הבאות:

1. ליצור שרת ברמה נמוכה שמטפל ברישום כלים והפעלת כלים.
2. ליישם ארכיטקטורה שניתן להרחיב עליה.
3. להוסיף ולידציה כדי לוודא שקריאות הכלים שלך מאומתות כראוי.

### -1- יצירת ארכיטקטורה

הדבר הראשון שצריך לטפל בו הוא ארכיטקטורה שעוזרת לנו להתרחב עם הוספת תכונות, כך זה נראה:

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

כעת הגדרנו ארכיטקטורה שמאפשרת בקלות להוסיף כלים חדשים בתיקיית כלים. ניתן להוסיף תתי תיקיות למשאבים והנחיות.

### -2- יצירת כלי

נראה איך נראה יצירת כלי. קודם כל, הוא צריך להיווצר בתת-תיקיית *tool* כך:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # אמת קלט באמצעות מודל Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: הוסף Pydantic, כדי שנוכל ליצור AddInputModel ולאמת את הפרמטרים

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

מה שרואים כאן זה כיצד מגדירים שם, תיאור, וסכמת קלט באמצעות Pydantic ומטפל שייקרא כאשר הכלי מופעל. לבסוף, חושפים את `tool_add` שהיא מילון שמכיל את כל התכונות האלה.

יש גם את *schema.py* שמשמש להגדרת סכמת הקלט של הכלי שלנו:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

בנוסף, צריך למלא את *__init__.py* כדי להבטיח שהתיקייה כלים תתייחס כמודול. בנוסף, יש לחשוף את המודולים שבתוכה כך:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

אפשר להמשיך להוסיף לקובץ זה ככל שמוסיפים כלים.

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

כאן אנו יוצרים מילון המורכב מתכונות:

- name, זה שם הכלי.
- rawSchema, זו הסכמה של Zod, שישמש לאימות בקשות נכנסות לקריאה לכלי.
- inputSchema, סכמה זו תשמש במטפל.
- callback, משמש לקריאת הכלי.

יש גם את `Tool` שמשמש להמרת המילון לסוג שמתאים למטפל השרתים של mcp ונראה כך:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ויש את *schema.ts* שבו מאוחסנות סכמות הקלט לכל כלי, ונראה כך כרגע עם סכמה אחת בלבד, אבל כשנוסיף כלים נוסיף שם רשומות נוספות:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

מצוין, בוא נמשיך לטפל ברישום הכלים הלאה.

### -3- טיפול ברישום כלים

כדי לטפל ברישום הכלים, צריכים להגדיר מטפל בקשות לכך. כך יש להוסיף לקובץ השרת:

**Python**

```python
# הקוד הושמט לצורך תמצות
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

כאן, מוסיפים דקורטור `@server.list_tools` ואת הפונקציה המיישמת `handle_list_tools`. בפונקציה זו, צריכים ליצור רשימת כלים. שים לב שכל כלי צריך לכלול שם, תיאור ו-inputSchema.

**TypeScript**

כדי להגדיר מטפל בקשות לרישום כלים, צריך לקרוא ל-`setRequestHandler` על השרת עם סכמת בקשה מתאימה, כאן זו `ListToolsRequestSchema`.

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
// קוד הושמט לקיצור
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // החזר את רשימת הכלים הרשומים
  return {
    tools: tools
  };
});
```

מעולה, פתרנו חלק את רישום הכלים, בוא נראה כיצד נקרא כלים בהמשך.

### -4- טיפול בקריאה לכלי

כדי לקרוא כלי, צריכים להגדיר מטפל בקשה נוסף, הפעם שמתמקד בטיפול בבקשה שמציינת איזו תכונה לקרוא ואיזו קלט להעביר.

**Python**

נשתמש בדקורטור `@server.call_tool` ונממש פונקציה בשם `handle_call_tool`. בתוך פונקציה זו, צריכים לנתח את שם הכלי, הארגומנטים שלו, ולהבטיח שהארגומנטים תקינים לכלי הרלוונטי. אפשר לאמת את הארגומנטים כאן או בתוך הכלי בפועל.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools הוא מילון שבו שמות הכלים הם המפתחות
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # הפעל את הכלי
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

כך זה מתבצע:

- שם הכלי שלנו כבר קיים כפרמטר קלט בשם `name` וארגומנטים כ"מילון" בשם `arguments`.

- הכלי נקרא עם `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. אימות הארגומנטים מתבצע במאפיין `handler` שמצביע על פונקציה, ואם זה נכשל תתעורר חריגה.

עכשיו יש לנו הבנה מלאה של רישום וקריאה לכלים באמצעות שרת ברמה נמוכה.

ראה את [הדוגמה המלאה](./code/README.md) כאן

## מטלה

הרחב את הקוד שקיבלת עם מספר כלים, משאבים והנחיות והבחן כיצד אתה מבחין בכך שרק צריך להוסיף קבצים בתיקיית הכלים ולא במקום אחר.

*אין פתרון מוצע*

## סיכום

בפרק זה ראינו איך עובדת גישת שרת ברמה נמוכה ואיך היא עוזרת לנו ליצור ארכיטקטורה נקייה שניתן לבנות עליה. גם דיברנו על אימות והוצגו לך דרכי עבודה עם ספריות אימות ליצירת סכמות לאימות קלט.

## מה הלאה

- הבא: [אימות פשוט](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). על אף שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים ממוחשבים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו יש להיחשב כמקור הסמכותי. למידע קריטי מומלץ לבצע תרגום מקצועי על ידי מתרגם אנושי. אנו לא נישא באחריות לכל אי הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->