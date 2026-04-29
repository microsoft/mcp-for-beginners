# שימוש מתקדם בשרת

קיימים שני סוגים שונים של שרתים המחוברים ב-MCP SDK, השרת הרגיל שלך והשרת ברמה נמוכה. בדרך כלל, תשתמש בשרת הרגיל כדי להוסיף לו תכונות. במקרים מסוימים עם זאת, תרצה להסתמך על השרת ברמה נמוכה כמו:

- ארכיטקטורה טובה יותר. אפשר ליצור ארכיטקטורה נקייה עם השרת הרגיל ועם השרת ברמה נמוכה, אבל ניתן לטעון שזה מעט קל יותר עם שרת ברמה נמוכה.  
- זמינות תכונות. חלק מהתכונות המתקדמות ניתן להשתמש בהן רק עם שרת ברמה נמוכה. תראה זאת בפרקים הבאים כשנוסיף דגימה ואילוציות.

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

הנקודה היא שאתה מוסיף במפורש כל כלי, משאב או הנחיה שברצונך שהשרת יכיל. אין בכך כל בעיה.

### גישת שרת ברמה נמוכה

עם זאת, כשאתה משתמש בגישה של שרת ברמה נמוכה אתה צריך לחשוב על זה אחרת. במקום לרשום כל כלי, אתה יוצר שני מטפלים לכל סוג תכונה (כלים, משאבים או הנחיות). למשל, כלי אז יש רק שתי פונקציות כך:

- רשימת כל הכלים. פונקציה אחת אחראית על כל הניסיונות לרשום כלים.
- טיפול בקריאה לכל הכלים. כאן גם, יש רק פונקציה אחת שמטפלת בקריאות לכלי

נשמע כמו עבודה פחותה, נכון? אז במקום לרשום כלי, אני רק צריך לוודא שהכלי מופיע כשאני מציג את רשימת הכלים ושקוראים לו כשיש בקשת קריאה לכלי.

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
  // החזר את רשימת הכלים שנרשמו
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

כאן יש לנו עכשיו פונקציה שמחזירה רשימת תכונות. כל ערך ברשימת הכלים כולל עכשיו שדות כגון `name`, `description` ו-`inputSchema` כדי לעמוד בסוג ההחזרה. זה מאפשר לנו למקם את הכלים והגדרת התכונות שלנו במקום אחר. כעת נוכל ליצור את כל הכלים שלנו בתיקיית כלים וכך גם לגבי כל התכונות שלך כך שהפרויקט שלך יכול להיות מאורגן כך:

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

זה מצוין, הארכיטקטורה שלנו יכולה להיראות די נקייה.

מה בנוגע לקריאה לכלים, האם זה הרעיון? כן, בדיוק, הנה הקוד לכך:

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
    // TODO לקרוא לכלי,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

כפי שניתן לראות מהקוד למעלה, אנו צריכים לפרש איזה כלי לקרוא ועם אילו ארגומנטים, ואז עלינו להמשיך לקרוא לכלי.

## שיפור הגישה עם אימות

עד כה, ראית כיצד כל הרישומים שלך להוספת כלים, משאבים והנחיות ניתן להחליף בשני מטפלים אלה לכל סוג תכונה. מה עוד צריך לעשות? נרצה להוסיף איזושהי בדיקת תקינות כדי לוודא שהכלי נקרא עם הארגומנטים הנכונים. לכל סביבה יש פתרון משלה לכך, למשל Python משתמשת ב-Pydantic ו-TypeScript משתמשת ב-Zod. הרעיון הוא כך:

- להעביר את הלוגיקה ליצירת תכונה (כלי, משאב או הנחיה) לתיקייה הייעודית שלה.
- להוסיף דרך לאמת בקשה נכנסת המבקשת למשל לקרוא לכלי.

### יצירת תכונה

כדי ליצור תכונה, נצטרך ליצור קובץ עבור אותה תכונה ולוודא שיש לה את השדות החובה הנדרשים לסוג התכונה. אילו שדות שונים במעט בין כלים, משאבים והנחיות.

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

    # TODO: להוסיף Pydantic, כדי שנוכל ליצור AddInputModel ולאמת ארגומנטים

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

כאן ניתן לראות כיצד אנו מבצעים את הדברים הבאים:

- ליצור סכימה באמצעות Pydantic `AddInputModel` הכוללת שדות `a` ו-`b` בקובץ *schema.py*.
- לנסות לפרש את הבקשה הנכנסת להיות מסוג `AddInputModel`, אם יש חוסר התאמה בפרמטרים זה יגרום לשגיאה:

   ```python
   # add.py
    try:
        # אמת את הקלט באמצעות מודל Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

אתה יכול לבחור אם למקם את לוגיקת הפרשנות בתוך קריאת הכלי עצמה או בפונקציית המטפל.

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

- במטפל המטפל בכל הקריאות לכלים, אנו מנסים כעת לפרש את הבקשה הנכנסת לסכימת הכלי שהוגדרה:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    אם זה עובד אז נמשיך לקרוא לכלי בפועל:

    ```typescript
    const result = await tool.callback(input);
    ```

כפי שניתן לראות, גישה זו יוצרת ארכיטקטורה טובה כי לכל דבר יש מקום, קובץ *server.ts* הוא קטן מאוד ורק מחבר בין המטפלים, וכל תכונה נמצאת בתיקייה הייעודית שלה כגון tools/, resources/ או /prompts.

מעולה, בוא ננסה לבנות את זה עכשיו.

## תרגיל: יצירת שרת ברמה נמוכה

בתרגיל זה נעשה את הדברים הבאים:

1. ניצור שרת ברמה נמוכה שמטפל ברשימת כלים ובקריאות לכלים.
1. נממש ארכיטקטורה שניתן להמשיך לבנות עליה.
1. נוסיף אימות לוודא שהקריאות לכלי מאומתות כראוי.

### -1- יצירת ארכיטקטורה

הדבר הראשון שעלינו לטפל בו הוא ארכיטקטורה שמסייעת לנו להתרחב כשנוסיף תכונות נוספות, כך זה נראה:

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

כעת הגדרנו ארכיטקטורה שמבטיחה שנוכל להוסיף כלים חדשים בקלות בתיקיית tools. ניתן להוסיף תת-תיקיות עבור resources ו-prompts בהתאם.

### -2- יצירת כלי

נראה כיצד נראה יצירת כלי. תחילה, הוא צריך להיווצר בתת-תיקיית *tool* כך:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # לאמת קלט באמצעות מודל Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: להוסיף Pydantic, כדי שנוכל ליצור AddInputModel ולאמת ארגומנטים

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

כאן אנו רואים כיצד מגדירים שם, תיאור וסכימת קלט באמצעות Pydantic ומטפל שייקרא כשכלי זה יופעל. לבסוף, אנו חושפים את `tool_add` שהוא מילון המכיל את כל התכונות הללו.

יש גם את *schema.py* שבו מוגדרת סכימת הקלט של הכלי:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

בנוסף יש למלא את *__init__.py* כדי להבטיח שהתיקייה tools תטופל כמודול. בנוסף יש לחשוף את המודולים שבתוכה כך:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ניתן להמשיך להוסיף לקובץ זה ככל שנוסיף כלים נוספים.

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

כאן אנו יוצרים מילון הכולל תכונות:

- name, שם הכלי.
- rawSchema, סכימת Zod שתשמש לאימות בקשות קריאה לכלי.
- inputSchema, סכימה שתשמש על ידי המטפל.
- callback, פונקציה שמפעילה את הכלי.

יש גם את `Tool` שמשמש להמרת מילון זה לסוג שהמטפל של שרת mcp יכול לקבל והוא נראה כך:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

וקיים קובץ *schema.ts* שבו נשמרות סכימות הקלט של כל כלי, שנראות כך עם סכימה אחת בלבד כרגע אך עם הוספת כלים נוספים נוסיף עוד רשומות:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

מצוין, נמשיך כעת לטפל ברשימת הכלים.

### -3- טיפול ברשימת כלים

כדי לטפל ברשימת הכלים, עלינו להגדיר מטפל לבקשה זו. הנה מה שיש להוסיף לקובץ השרת שלנו:

**Python**

```python
# הקוד הושמט לקיצור
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

כאן אנו מוסיפים את הדקורטור `@server.list_tools` ואת פונקציית היישום `handle_list_tools`. בפונקציה זו, נדרש להחזיר רשימת כלים. שים לב שכל כלי חייב להכיל name, description ו-inputSchema.

**TypeScript**

כדי להגדיר מטפל לבקשת רשימת כלים, יש לקרוא ל-`setRequestHandler` על השרת עם סכימה המתאימה לנושא, במקרה זה `ListToolsRequestSchema`.

```typescript
// אינדקס.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// שרת.ts
// הקוד הושמט לשם תמצות
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // החזר את רשימת הכלים הרשומים
  return {
    tools: tools
  };
});
```

מעולה, כעת פתרנו את נושא רשימת הכלים, נבחן עכשיו כיצד ניתן לקרוא לכלים.

### -4- טיפול בקריאת כלי

כדי לקרוא לכלי, יש להגדיר מטפל נוסף בבקשה, הפעם שמטפל בבקשה שמציינת איזו תכונה לקרוא ואילו ארגומנטים יש להעביר.

**Python**

נשתמש בדקורטור `@server.call_tool` ונממש אותו באמצעות פונקציה כמו `handle_call_tool`. בתוך פונקציה זו, עלינו לפרש את שם הכלי, את הארגומנטים ולוודא שהארגומנטים תקינים עבור הכלי המדובר. ניתן לאמת את הפרמטרים כאן או בהמשך בתוך הכלי עצמו.

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
        # הפעל את הכלי
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

כך זה מתבצע:

- שם הכלי שלנו כבר מופיע כפרמטר קלט `name` שהוא גם שם המפתח במילון `arguments`.

- הכלי נקרא באמצעות `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. האימות של הארגומנטים מתבצע בתוך `handler` שמצביע על פונקציה, ואם זה נכשל תתעורר חריגה.

ולכן, כעת יש לנו הבנה מלאה של רישום קריאה לכלים באמצעות שרת ברמה נמוכה.

ראה את [הדוגמה המלאה](./code/README.md) כאן

## משימה

הרחב את הקוד שניתן לך עם מספר כלים, משאבים והנחיות והרהר כיצד אתה מבחין בכך שאתה רק צריך להוסיף קבצים בתיקיית tools ולשום מקום אחר.

*אין פתרון שניתן*

## סיכום

בפרק זה ראינו כיצד גישת השרת ברמה נמוכה עובדת ואיך זה מסייע לנו ליצור ארכיטקטורה נקייה שנוכל להמשיך לבנות עליה. גם דיברנו על אימות וראית איך לעבוד עם ספריות אימות כדי ליצור סכימות לאימות קלט.

## מה הלאה

- הבא: [אימות פשוט](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכות. עבור מידע קריטי, מומלץ להיעזר בתרגום מקצועי אנושי. אנו לא נישא באחריות לכל אי-הבנה או פרשנות מוטעית הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->