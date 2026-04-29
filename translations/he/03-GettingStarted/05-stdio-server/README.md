# שרת MCP עם תחבורה stdio

> **⚠️ עדכון חשוב**: החל מגרסת מפרט MCP 2025-06-18, ממשק SSE עצמאי (Server-Sent Events) הוסר והוחלף בתחבורה "HTTP סטרימבילי". מפרט MCP הנוכחי מגדיר שני מנגנוני תחבורה עיקריים:
> 1. **stdio** - קלט/פלט סטנדרטי (מומלץ לשרתי מקומיים)
> 2. **HTTP סטרימבילי** - לשרתים מרוחקים שיכולים להשתמש ב-SSE פנימית
>
> השיעור עודכן כדי להתמקד בתחבורה של **stdio**, שהיא הגישה המומלצת לרוב המימושים של שרתי MCP.

תחבורה stdio מאפשרת לשרתי MCP לתקשר עם לקוחות דרך ערוצי הקלט והפלט הסטנדרטיים. זוהי מנגנון התחבורה הנפוץ והמומלץ במפרט MCP הנוכחי, שמספק דרך פשוטה ויעילה לבניית שרתי MCP שניתן לשלבם בקלות עם יישומי לקוח שונים.

## סקירה כללית

שיעור זה עוסק באופן בנייה ושימוש בשרתי MCP באמצעות תחבורה stdio.

## מטרות הלמידה

בסוף שיעור זה תוכל:

- לבנות שרת MCP עם תחבורה stdio.
- לנפות תקלות בשרת MCP באמצעות Inspector.
- לצרוך שרת MCP באמצעות Visual Studio Code.
- להבין את מנגנוני התחבורה הנוכחיים של MCP ולמה stdio מומלץ.

## תחבורה stdio - איך זה עובד

תחבורה stdio היא אחת משתי סוגי התחבורה הנתמכים במפרט MCP הנוכחי (2025-06-18). כך זה עובד:

- **תקשורת פשוטה**: השרת קורא הודעות JSON-RPC מקלט סטנדרטי (`stdin`) ושולח הודעות לפלט סטנדרטי (`stdout`).
- **מתבסס על תהליך**: הלקוח משיק את שרת ה-MCP כתת-תהליך.
- **פורמט הודעה**: הודעות הן בקשות, התראות או תגובות JSON-RPC נפרדות, המופרדות על ידי שורות חדשות.
- **יומנים**: השרת יִכָּתֵב מחרוזות UTF-8 לסטנדרט ההפלט השגיאות (`stderr`) לצורך רישום יומנים.

### דרישות מרכזיות:
- ההודעות **חייבות** להיות מופרדות על ידי שורות חדשות ואסור שיכילו שורות חדשות מקוננות.
- השרת **אסור** שיכתוב לפלט סטנדרטי (`stdout`) משהו שאינו הודעת MCP תקינה.
- הלקוח **אסור** שיכתוב לסטנדרט הקלט (`stdin`) של השרת משהו שאינו הודעת MCP תקינה.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```
  
בקוד למעלה:

- אנחנו מייבאים את המחלקה `Server` ואת `StdioServerTransport` מ-MCP SDK
- יוצרים מופע שרת עם קונפיגורציה בסיסית ויכולות
- יוצרים מופע `StdioServerTransport` ומחברים אליו את השרת, מאפשרים תקשורת דרך stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# צור מופע שרת
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```
  
בקוד למעלה:

- יוצרים מופע שרת באמצעות MCP SDK
- מגדירים כלים באמצעות דקורטורים
- משתמשים במנהל ההקשר stdio_server לטיפול בתחבורה

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```
  
ההבדל המרכזי מ-SSE הוא ששרתי stdio:

- אינם דורשים הקמת שרת אינטרנט או נקודות קצה HTTP
- משיקים כתת-תהליכים על ידי הלקוח
- מתקשרים דרך ערוצי stdin/stdout
- פשוטים יותר ליישום ולניפוי שגיאות

## תרגיל: יצירת שרת stdio

כדי ליצור את השרת שלנו, עלינו לזכור שני דברים:

- נצטרך להשתמש בשרת אינטרנט כדי לחשוף נקודות קצה לחיבור והודעות.

## מעבדה: יצירת שרת MCP stdio פשוט

במעבדה זו ניצור שרת MCP פשוט באמצעות תחבורה stdio המומלצת. שרת זה יחשוף כלים שהלקוחות יוכלו לקרוא בעזרת הפרוטוקול Model Context Protocol הסטנדרטי.

### דרישות מקדימות

- Python 3.8 ומעלה
- MCP Python SDK: `pip install mcp`
- הבנה בסיסית בתכנות אסינכרוני

נתחיל ביצירת שרת MCP stdio הראשון שלנו:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# להגדיר רישום
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# צור את השרת
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # השתמש בהובלת stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```
  
## הבדלים מרכזיים מהגישה SSE שהוסרה

**תחבורה stdio (תקן נוכחי):**  
- מודל תת-תהליך פשוט – הלקוח משיק את השרת כתהליך בן  
- תקשורת דרך stdin/stdout באמצעות הודעות JSON-RPC  
- לא נדרש הקמת שרת HTTP  
- ביצועים ואבטחה טובים יותר  
- קל יותר לניפוי שגיאות ולפיתוח  

**תחבורה SSE (הוסרה מגרסת MCP 2025-06-18):**  
- דרש שרת HTTP עם נקודות קצה SSE  
- הגדרת תשתית השרת מורכבת יותר  
- שיקולי אבטחה נוספים בנקודות קצה HTTP  
- הוחלף כיום על ידי HTTP סטרימבילי לתרחישים מבוססי ווב  

### יצירת שרת עם תחבורה stdio

כדי ליצור את השרת שלנו עם stdio, יש לבצע:

1. **ייבוא הספריות הדרושות** - נדרשים רכיבי שרת MCP ותחבורה stdio  
2. **יצירת מופע שרת** - הגדרת השרת עם היכולות שלו  
3. **הגדרת כלים** - הוספת הפונקציונליות אותה רוצים לחשוף  
4. **הגדרת התחבורה** - הקונפיגורציה של תקשורת stdio  
5. **הרצת השרת** - הפעלת השרת וטיפול בהודעות  

בואו נבנה זאת שלב אחר שלב:

### שלב 1: יצירת שרת stdio בסיסי

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# הגדר רישום יומן
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# צור את השרת
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```
  
### שלב 2: הוספת כלים נוספים

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```
  
### שלב 3: הפעלת השרת

שמור את הקוד כקובץ `server.py` והרץ אותו משורת הפקודה:

```bash
python server.py
```
  
השרת יתחיל ויחכה לקלט מ-stdin. הוא מתקשר באמצעות הודעות JSON-RPC על גבי תחבורה stdio.

### שלב 4: בדיקה עם Inspector

ניתן לבדוק את השרת באמצעות MCP Inspector:

1. התקן את Inspector: `npx @modelcontextprotocol/inspector`  
2. הרץ את Inspector וכוון אותו אל השרת שלך  
3. בדוק את הכלים שיצרת  

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
  
## ניפוי שגיאות לשרת stdio שלך

### שימוש ב-MCP Inspector

MCP Inspector הוא כלי חשוב לניפוי שגיאות ובדיקת שרתי MCP. כך משתמשים בו עם שרת stdio שלך:

1. **התקן את Inspector**:  
   ```bash
   npx @modelcontextprotocol/inspector
   ```
  
2. **הרץ את Inspector**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
3. **בדוק את השרת שלך**: Inspector מספק ממשק רשת שבו אפשר:
   - לראות את יכולות השרת
   - לבדוק כלים עם פרמטרים שונים
   - לעקוב אחרי הודעות JSON-RPC
   - לנפות תקלות בחיבור  

### שימוש ב-VS Code

ניתן גם לנפות שגיאות בשרת MCP ישירות ב-VS Code:

1. צור קובץ קונפיגורציית הפעלה ב- `.vscode/launch.json`:  
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```
  
2. הגדר נקודות עצירה בקוד השרת שלך  
3. הפעל את המדבג ובדוק באמצעות Inspector  

### טיפים נפוצים לניפוי שגיאות

- השתמש ב-`stderr` לרישום יומנים - לעולם אל תכתוב ל-`stdout` כיוון שזה שמור להודעות MCP  
- ודא שכל הודעות JSON-RPC מופרדות בשורות חדשות  
- בדוק תחילה עם כלים פשוטים לפני הוספת פונקציונליות מורכבת  
- השתמש ב-Inspector כדי לוודא את פורמט ההודעות

## צריכת שרת stdio ב-VS Code

כשתבנה את שרת ה-MCP stdio שלך, תוכל לשלב אותו עם VS Code לשימוש עם Claude או לקוחות אחרים התומכים ב-MCP.

### קונפיגורציה

1. **צור קובץ קונפיגורציית MCP** בנתיב `%APPDATA%\Claude\claude_desktop_config.json` (Windows) או `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```
  
2. **אתחל את Claude מחדש**: סגור ופתח מחדש את Claude כדי שיטען את הקונפיגורציה החדשה.

3. **בדוק את החיבור**: התחל שיחה עם Claude ונסה להשתמש בכלי השרת שלך:  
   - "אתה יכול לברך אותי באמצעות כלי הברכה?"  
   - "חשב את הסכום של 15 ו-27"  
   - "מה המידע על השרת?"

### דוגמת שרת stdio ב-TypeScript

הנה דוגמה מלאה ב-TypeScript לעיון:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// הוסף כלים
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```
  
### דוגמת שרת stdio ב-.NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```
  
## סיכום

בשיעור המעודכן למדת כיצד:

- לבנות שרתי MCP באמצעות **תחבורה stdio** הנוכחית (הגישה המומלצת)  
- להבין מדוע תחבורה SSE הוסרה לטובת stdio ו-HTTP סטרימבילי  
- ליצור כלים הניתנים לקריאה על ידי לקוחות MCP  
- לנפות תקלות בשרת באמצעות MCP Inspector  
- לשלב את שרת stdio שלך ב-VS Code ו-Claude  

תחבורה stdio מספקת דרך פשוטה, בטוחה ויעילה יותר לבניית שרתי MCP לעומת גישת SSE שהוסרה. היא תחבורת ברירת המחדל לרוב מימושי שרתי MCP החל מגרסת 2025-06-18.

### .NET

1. בוא ניצור תחילה כמה כלים, לשם כך ניצור קובץ *Tools.cs* עם התוכן הבא:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```
  
## תרגיל: בדיקת שרת stdio שלך

כעת כשבנית את שרת stdio שלך, בוא נבדוק שהוא פועל כראוי.

### דרישות מקדימות

1. ודא שהתקנת את MCP Inspector:  
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```
  
2. הקוד שלך צריך להיות שמור (למשל כ-`server.py`)

### בדיקה עם Inspector

1. **הפעל את Inspector עם השרת שלך**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
2. **פתח את ממשק הרשת**: Inspector יפתח דפדפן המציג את יכולות השרת שלך.

3. **בדוק את הכלים**:
   - נסה את הכלי `get_greeting` עם שמות שונים  
   - בדוק את הכלי `calculate_sum` עם מספרים שונים  
   - קרא לכלי `get_server_info` כדי לראות מטא-דאטה של השרת  

4. **עקוב אחרי התקשורת**: Inspector מציג את הודעות JSON-RPC המנותחות בין הלקוח לשרת.

### מה תראה

כששרתך מתחיל כראוי, תראה:  
- רשימת יכולות שרת ב-Inspector  
- כלים זמינים לבדיקה  
- החלפות הודעות JSON-RPC מוצלחות  
- תגובות כלים מוצגות בממשק  

### תקלות נפוצות ופתרונות

**השרת לא מתחיל:**  
- בדוק שכל התלויות מותקנות: `pip install mcp`  
- ודא שאין שגיאות תחביר ושההזחות נכונות בפייתון  
- חפש הודעות שגיאה בקונסול  

**כלים לא מופיעים:**  
- ודא שקיימים דקורטורי `@server.tool()`  
- בדוק שהפונקציות מוגדרות לפני `main()`  
- ודא שהשרת מוגדר כראוי  

**בעיות חיבור:**  
- ודא שהשרת משתמש בתחבורה stdio כראוי  
- בדוק שאף תהליך אחר לא מפריע  
- וודא את תחביר הפקודה של Inspector  

## מטלה

נסה להרחיב את השרת שלך עם יכולות נוספות. ראה [עמוד זה](https://api.chucknorris.io/) כדי להוסיף, למשל, כלי שקורא ל-API. אתה מחליט איך יראה השרת. בהצלחה :)

## פתרון

[פתרון](./solution/README.md) הנה פתרון אפשרי עם קוד עובד.

## נקודות מפתח

נקודות עיקריות בפרק זה הן:

- תחבורה stdio היא המנגנון המומלץ לשרתי MCP מקומיים.  
- תחבורה stdio מאפשרת תקשורת חלקה בין שרתי MCP ללקוחות דרך ערוצי קלט ופלט סטנדרטיים.  
- ניתן להשתמש הן ב-Inspector והן ב-Visual Studio Code לצריכת שרתי stdio ישירות, מה שמקל על ניפוי שגיאות ושילוב.  

## דוגמאות

- [מחשבון Java](../samples/java/calculator/README.md)  
- [מחשבון .Net](../../../../03-GettingStarted/samples/csharp)  
- [מחשבון JavaScript](../samples/javascript/README.md)  
- [מחשבון TypeScript](../samples/typescript/README.md)  
- [מחשבון Python](../../../../03-GettingStarted/samples/python)  

## משאבים נוספים

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)  

## מה הלאה

## צעדים הבאים

כעת שהבנת כיצד לבנות שרתי MCP עם תחבורה stdio, תוכל לחקור נושאים מתקדמים יותר:

- **הבא**: [HTTP Streaming עם MCP (HTTP סטרימבילי)](../06-http-streaming/README.md) - למד על מנגנון התחבורה השני הנתמך לשרתים מרוחקים  
- **מתקדם**: [פרקטיקות אבטחה טובות ל-MCP](../../02-Security/README.md) - יישם אבטחה בשרתי MCP שלך  
- **פרודקשן**: [אסטרטגיות פריסה](../09-deployment/README.md) - העלה את השרתים לשימוש בזמן אמת  

## משאבים נוספים

- [מפרט MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - מפרט רשמי  
- [תיעוד MCP SDK](https://github.com/modelcontextprotocol/sdk) - הפניות SDK לכל השפות  
- [דוגמאות מהקהילה](../../06-CommunityContributions/README.md) - דוגמאות שרת נוספות מהקהילה  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל טעויות או אי דיוקים. יש להתייחס למסמך המקורי בשפת המקור כמקור הסמכותי. עבור מידע קריטי, מומלץ תרגום מקצועי על ידי אדם. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->