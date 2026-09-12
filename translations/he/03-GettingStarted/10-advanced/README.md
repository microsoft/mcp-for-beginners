# שימוש מתקדם בשרת

ישנם שני סוגים שונים של שרתים ב-MCP SDK, השרת הרגיל שלך והשרת ברמת נמוכה. בדרך כלל, תשתמש בשרת הרגיל כדי להוסיף לו תכונות. עם זאת, במקרים מסוימים תרצה להסתמך על השרת ברמת נמוכה, כמו למשל:

- ארכיטקטורה טובה יותר. אפשר ליצור ארכיטקטורה נקייה עם שני השרתים הרגיל והנמוך, אבל ניתן לטעון שזה קל יותר עם שרת ברמת נמוכה.
- זמינות תכונות. כמה תכונות מתקדמות ניתן להשתמש רק עם
    שרת ברמת נמוכה. בפרקים מאוחרים יותר נדון ב-Elicitation ובתכונת Sampling המיושנת,
    שנפסלה ב-MCP `2026-07-28`.

## שרת רגיל נגד שרת ברמת נמוכה

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

העיקרון הוא שאתה מוסיף באופן מפורש כל כלי, משאב או פרומפט שברצונך שיהיה לשרת. אין בכך בעיה.  

### גישת שרת ברמת נמוכה

לעומת זאת, כשאתה משתמש בגישת שרת ברמת נמוכה אתה צריך לחשוב על זה אחרת. במקום לרשום כל כלי, אתה יוצר שני מטפלים עבור כל סוג תכונה (כלים, משאבים או פרומפטים). לדוגמה, לכלים יש שתי פונקציות בלבד כך:

- הצגת כל הכלים. פונקציה אחת אחראית על כל הניסיונות לרשום כלים.
- טיפול בקריאות לכלים. גם כאן, יש רק פונקציה אחת שטיפלה בקריאות לכלי.

זה נשמע כמו פחות עבודה, לא? במקום לרשום כלי, אני רק צריך לוודא שהכלי מופיע כאשר אני מציג את כל הכלים ושהוא נקרא כשיש בקשה לקרוא לכלי. 

בוא נסתכל איך הקוד נראה עכשיו:

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

כאן יש לנו פונקציה שמחזירה רשימה של תכונות. כל רשומה ברשימת הכלים כוללת שדות כמו `name`, `description` ו-`inputSchema` כדי לעמוד בסוג ההחזרה. זה מאפשר לנו למקם את הכלים והגדרת התכונות במקום אחר. אנחנו יכולים עכשיו ליצור את כל הכלים שלנו בתיקיה tools והדבר נכון גם לכל התכונות כך שהפרויקט שלך יכול להיות מאורגן כך:

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

זה נהדר, הארכיטקטורה שלנו יכולה להראות נקייה למדי.

מה לגבי קריאות לכלים, האם זה אותו רעיון, מטפל אחד שקורא לכל כלי, איזה כלי שזה יהיה? כן, בדיוק, הנה הקוד לכך:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools הוא מילון עם שמות של כלים כמפתחות
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

כפי שניתן לראות מהקוד למעלה, אנחנו צריכים לנתח איזה כלי לקרוא, עם אילו פרמטרים, ואז להמשיך לקרוא לכלי.

## שיפור הגישה עם אימות

עד כה ראית איך כל ההרשמות להוספת כלים, משאבים ופרומפטים יכולים להיות מוחלפים בשני מטפלים אלה עבור כל סוג תכונה. מה עוד צריך לעשות? אנחנו צריכים להוסיף איזושהי אימות כדי לוודא שהכלי נקרא עם הפרמטרים הנכונים. לכל runtime יש פתרון משלו לכך, לדוגמה Python משתמש ב-Pydantic ו-TypeScript משתמש ב-Zod. הרעיון הוא שנעשה את הדברים הבאים:

- להעביר את הלוגיקה של יצירת תכונה (כלי, משאב או פרומפט) לתיקיה ייעודית.
- להוסיף דרך לאמת בקשה נכנסת שכאשר מנסים לקרוא לכלי לדוגמה.

### יצירת תכונה

כדי ליצור תכונה, נצטרך ליצור קובץ לתכונה זו ולוודא שיש בו את השדות החובה הדרושים לתכונה. אילו שדות יש משתנים בין כלים, משאבים ופרומפטים.

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

    # TODO: הוסף Pydantic, כדי שנוכל ליצור AddInputModel ולאמת ארגומנטים

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
- מנסים לנתח את הבקשה הנכנסת להיות מסוג `AddInputModel`, אם יש חוסר התאמה בפרמטרים זה יתפרק:

   ```python
   # add.py
    try:
        # אמת קלט באמצעות מודל Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

אפשר לבחור אם לשים את לוגיקת הפירוק בתוך קריאת הכלי עצמו או בתוך פונקציית המטפל.

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

- במטפל שעוסק בכל הקריאות לכלים, אנחנו עכשיו מנסים לנתח את הבקשה הנכנסת לסכימת הכלי שהוגדרה:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    אם זה עובד אז ממשיכים לקרוא לכלי בפועל:

    ```typescript
    const result = await tool.callback(input);
    ```

כפי שאתה רואה, הגישה הזו יוצרת ארכיטקטורה טובה כי לכל דבר יש את מקומו, הקובץ *server.ts* הוא קטן מאוד ורק מחבר את מטפלי הבקשות וכל תכונה ממוקמת בתיקיה המתאימה לה לדוגמה tools/, resources/ או /prompts.

מצוין, בוא ננסה לבנות זאת בהמשך. 

## תרגיל: יצירת שרת ברמת נמוכה

בתרגיל זה נבצע את הדברים הבאים:

1. ליצור שרת ברמת נמוכה שמטפל ברשימת כלים ובקריאות לכלים.
1. ליישם ארכיטקטורה שניתן להמשיך לבנות עליה.
1. להוסיף אימות כדי לוודא שקריאות הכלי שלך מאומתות כראוי.

### -1- יצירת ארכיטקטורה

הדבר הראשון שצריך לטפל בו הוא ארכיטקטורה שעוזרת לנו להגדיל ולהוסיף תכונות בקלות, כך זה נראה:

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

עכשיו הקמנו ארכיטקטורה שמבטיחה שנוכל להוסיף בקלות כלים חדשים בתיקייה tools. אפשר להוסיף תיקיות משנה למשאבים ופרומפטים על פי הצורך.

### -2- יצירת כלי

נראה איך ליצור כלי. קודם כל צריך ליצור אותו בתיקיית *tool* ככה:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # אמת קלט באמצעות מודל Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: הוסף Pydantic, כדי שנוכל ליצור AddInputModel ולאמת ארגומנטים

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

מה שנראה כאן זה איך מגדירים שם, תיאור וסכימת קלט באמצעות Pydantic ומטפל שיופעל כאשר קוראים לכלי. לבסוף, אנחנו חושפים את `tool_add` שהוא מילון המכיל את כל התכונות האלה.

יש גם את *schema.py* המשמש להגדרת סכימת הקלט שמשמשת את הכלי:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

בנוסף, צריכים למלא את *__init__.py* כדי לוודא שתיקיית tools מטופלת כמודול. בנוסף, צריך לחשוף את המודולים שבתוכה כך:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

אפשר להמשיך להוסיף לקובץ הזה ככל שמוסיפים כלים נוספים.

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

כאן אנו יוצרים מילון שמכיל תכונות:

- name, זהו שם הכלי.
- rawSchema, זוהי סכימת Zod, שתשמש לאימות בקשות נכנסות לקריאת הכלי.
- inputSchema, סכימה זו תשמש על ידי המטפל.
- callback, זה משמש לקריאת הכלי.

יש גם את `Tool` שמשמש להמרת המילון הזה לסוג שמטפל שרת MCP יכול לקבל והוא נראה כך:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ויש את *schema.ts* שבו מאחסנים את סכימות הקלט לכל כלי, נראה כך עם סכימה אחת בהווה אבל ככל שנוסיף כלים נוסיף עוד רשומות:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

מצוין, נמשיך לטפל ברשימת הכלים שלנו בהמשך.

### -3- טיפול ברשימת כלים

הבא לטפל ברשימת הכלים שלנו, צריך להגדיר מטפל בקשות לכך. הנה מה שצריך להוסיף לקובץ השרת:

**Python**

```python
# הקוד הושמט כדי לקצר
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

כאן אנחנו מוסיפים את הדקורטור `@server.list_tools` ואת הפונקציה המממשת `handle_list_tools`. בפונקציה זו צריך להחזיר רשימת כלים. שים לב שכל כלי צריך להכיל שם, תיאור ו-inputSchema.   

**TypeScript**

כדי להגדיר את מטפל הבקשות לרישום הכלים, צריך לקרוא ל-`setRequestHandler` על השרת עם סכימה שמתאימה למה שאנחנו מנסים לעשות, במקרה זה `ListToolsRequestSchema`. 

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
// הקוד הושמט לקיצור
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // החזר את רשימת הכלים הרשומים
  return {
    tools: tools
  };
});
```

מצוין, פתרנו את החלק של רישום הכלים, נבחן כיצד ניתן לקרוא לכלים בהמשך.

### -4- טיפול בקריאת כלי

כדי לקרוא לכלי, צריך להגדיר מטפל בקשת נוסף, הפעם ממוקד בטיפול בבקשה שמציינת איזו תכונה לקרוא ואיזה פרמטרים.

**Python**

נשתמש בדקורטור `@server.call_tool` ונממש פונקציה בשם `handle_call_tool`. בתוך פונקציה זו צריך לנתח את שם הכלי, הפרמטרים ולהבטיח שהפרמטרים תקינים לכלי הנזקק. אפשר לאמת את הפרמטרים כאן או בפונקציה עצמה של הכלי.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # כלים הוא מילון שבו שמות הכלים הם המפתחות
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

הנה מה שקורה:

- שם הכלי כבר קיים כפרמטר קלט `name` וזה נכון גם לפרמטרים במילון `arguments`.

- הכלי נקרא עם `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. האימות של הפרמטרים מתבצע במאפיין `handler` שמצביע לפונקציה, אם זה נכשל ייזרק חריג.

לכן, עכשיו יש לנו הבנה מלאה של רשימה וקריאת כלים באמצעות שרת ברמת נמוכה.

לראות את [הדוגמה המלאה](./code/README.md) כאן

## משימה

הרחב את הקוד שקיבלת עם מספר כלים, משאבים ופרומפטים והרהר כיצד אתה מבחין שאתה רק צריך להוסיף קבצים בתיקיית tools ולא בשום מקום אחר. 

*לא ניתנה פתרון*

## סיכום

בפרק זה ראינו איך גישת שרת ברמת נמוכה עובדת ואיך זה יכול לעזור לנו ליצור ארכיטקטורה יפה שאפשר להמשיך לבנות עליה. דנו גם באימות והודגם לך איך לעבוד עם ספריות אימות ליצירת סכימות לאימות קלט.

## מה הלאה

- הלאה: [אימות פשוט](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->