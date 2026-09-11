# שרת MCP עם טרנספורט stdio

> **⚠️ עדכון חשוב**: מאז מפרט MCP מ-2025-06-18, הטרנספורט העצמאי SSE (Server-Sent Events) הוכרז כלא מומלץ והוחלף על ידי טרנספורט "HTTP סטרימבילי". מפרט MCP הנוכחי מגדיר שני מנגנוני טרנספורט עיקריים:
> 1. **stdio** - קלט/פלט סטנדרטי (מומלץ לשרתים מקומיים)
> 2. **HTTP סטרימבילי** - לשרתים מרוחקים שעשויים להשתמש ב-SSE פנימית
>
> שיעור זה עודכן כדי להתמקד ב**טרנספורט stdio**, שהוא הגישה המומלצת לרוב יישומי שרת MCP.

טרנספורט stdio מאפשר לשרתי MCP לתקשר עם לקוחות דרך זרמי הקלט והפלט הסטנדרטיים. זהו המנגנון הנפוץ והמומלץ במפרט MCP הנוכחי, ומספק דרך פשוטה ויעילה לבניית שרתי MCP שניתן לשלב בקלות עם יישומי לקוח מגוונים.

## סקירה כללית

שיעור זה מכסה כיצד לבנות ולצרוך שרתי MCP באמצעות טרנספורט stdio.

## מטרות הלמידה

בסיום שיעור זה תוכל/י:

- לבנות שרת MCP תוך שימוש בטרנספורט stdio.
- לבצע איתור באגים בשרת MCP באמצעות ה-Inspector.
- לצרוך שרת MCP באמצעות Visual Studio Code.
- להבין את מנגנוני הטרנספורט של MCP הנוכחיים ולמה stdio הוא המומלץ.


## טרנספורט stdio - איך זה עובד

טרנספורט stdio הוא אחד משני הטרנספורטים הסטנדרטיים במפרט MCP
`2026-07-28`. כך זה עובד:

- **תקשורת פשוטה**: השרת קורא הודעות JSON-RPC מקלט סטנדרטי (`stdin`) ושולח הודעות לפלט סטנדרטי (`stdout`).
- **מבוסס תהליך**: הלקוח מפעיל את שרת MCP כתהליך משנה.
- **פורמט הודעה**: ההודעות הן בקשות JSON-RPC בודדות, התראות או תגובות, מופרדות על ידי שורות חדשות.
- **רישום לוגים**: השרת רשאי לכתוב מחרוזות UTF-8 לזרם השגיאות הסטנדרטי (`stderr`) למטרות רישום.

### דרישות מרכזיות:
- ההודעות חייבות להיות מופרדות על ידי שורות חדשות וחייבות לא להכיל שורות חדשות מוטמעות
- השרת אסור שיכתוב ל-`stdout` משהו שאינו הודעת MCP חוקית
- הלקוח אסור שיכתוב ל-`stdin` של השרת משהו שאינו הודעת MCP חוקית

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

בקוד הבא:

- מייבאים את המחלקה `Server` ואת `StdioServerTransport` מ-SDK של MCP
- יוצרים מופע שרת עם קונפיגורציה וכישורים בסיסיים
- יוצרים מופע `StdioServerTransport` ומחברים את השרת אליו, מאפשרים תקשורת על פני stdin/stdout

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

בקוד הבא:

- יוצרים מופע שרת באמצעות MCP SDK
- מגדירים כלים באמצעות קישוטים (decorators)
- משתמשים במנהל ההקשר stdio_server כדי לטפל בטרנספורט

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

- אינם דורשים התקנת שרת רשת או נקודות קצה HTTP
- מופעלים כתהליכים משנה על ידי הלקוח
- מתקשרים דרך זרמי stdin/stdout
- פשוטים יותר ליישום ואיתור באגים

## תרגיל: יצירת שרת stdio

כדי ליצור את השרת שלנו, עלינו לזכור שתי נקודות:

- אנחנו צריכים להשתמש בשרת רשת כדי לחשוף נקודות קצה לחיבור ולהודעות.
## מעבדה: יצירת שרת MCP פשוט ב_stdio_

במעבדה זו ניצור שרת MCP פשוט באמצעות טרנספורט stdio המומלץ. שרת זה יחשוף כלים שיכולים לקוחות לקרוא באמצעות פרוטוקול Model Context Protocol הסטנדרטי.

### דרישות מוקדמות

- Python 3.8 או גרסה חדשה יותר
- MCP Python SDK: `pip install mcp`
- הבנה בסיסית של תכנות אסינכרוני

נתחיל ביצירת שרת stdio ראשון:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# תכנת רישום
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
    # השתמש בהעברת stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## הבדלים מרכזיים מהגישה המיושנת SSE

**טרנספורט stdio (תקן נוכחי):**
- מודל תהליך משנה פשוט - הלקוח מפעיל את השרת כתהליך ילד
- תקשורת דרך stdin/stdout באמצעות הודעות JSON-RPC
- ללא צורך בהתקנת שרת HTTP
- ביצועים ואבטחה טובים יותר
- איתור באגים ופיתוח קלים יותר

**טרנספורט SSE (מיושן מאז MCP 2025-06-18):**
- דרוש שרת HTTP עם נקודות SSE
- התקנה מורכבת יותר עם תשתית שרת אינטרנט
- שיקולי אבטחה נוספים עבור נקודות קצה HTTP
- כעת מוחלף ב-Streamable HTTP לתרחישי רשת

### יצירת שרת עם טרנספורט stdio

כדי ליצור את שרת stdio שלנו, עלינו:

1. **ייבא את הספריות הדרושות** - אנו זקוקים לרכיבי שרת MCP וטרנספורט stdio
2. **צור מופע שרת** - הגדר את השרת עם הכישורים שלו
3. **הגדר כלים** - הוסף את הפונקציונליות שברצונך לחשוף
4. **הגדר את הטרנספורט** - קונפיגורציית תקשורת stdio
5. **הפעל את השרת** - התחל את השרת וטפל בהודעות

נבנה זאת שלב אחרי שלב:

### שלב 1: צור שרת stdio בסיסי

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# הגדר תיעוד
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

### שלב 2: הוסף כלים נוספים

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

שמור את הקוד כ`server.py` והפעל אותו משורת הפקודה:

```bash
python server.py
```

השרת יתחיל ויחכה לקלט מ-stdin. הוא מתקשר באמצעות הודעות JSON-RPC על גבי טרנספורט stdio.

### שלב 4: בדיקה עם ה-Inspector

ניתן לבדוק את השרת באמצעות MCP Inspector:

1. התקן את ה-Inspector: `npx @modelcontextprotocol/inspector`
2. הפעל את ה-Inspector והצביע אליו על השרת שלך
3. בדוק את הכלים שיצרת

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## איתור באגים בשרת stdio שלך

### שימוש ב-MCP Inspector

MCP Inspector הוא כלי חשוב לאיתור באגים ובדיקת שרתי MCP. כך משתמשים בו עם שרת stdio שלך:

1. **התקנת ה-Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **הפעלת ה-Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **בדוק את השרת שלך**: ה-Inspector מספק ממשק רשת שבו תוכל:
   - לצפות בכישורי השרת
   - לבדוק כלים עם פרמטרים שונים
   - לעקוב אחרי הודעות JSON-RPC
   - לאתר בעיות חיבור

### שימוש ב-VS Code

ניתן גם לבצע איתור באגים ישירות ב-VS Code:

1. צור קובץ קונפיגורציה ב`.vscode/launch.json`:
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
3. הפעל את הדיבאגר ובדוק עם ה-Inspector

### טיפים נפוצים לאיתור באגים

- השתמש ב-`stderr` לרישום לוגים - לעולם אל תכתוב ל-`stdout` שכן הוא שמור להודעות MCP
- ודא שכל הודעות JSON-RPC מופרדות בשורות חדשות
- נסה כלים פשוטים תחילה לפני הוספת פונקציונליות מורכבת
- השתמש ב-Inspector כדי לוודא את פורמטי ההודעות

## צריכת שרת stdio שלך ב-VS Code

ברגע שבנית את שרת stdio שלך, תוכל לשלב אותו עם VS Code לשימוש עם Claude או לקוחות אחרים התומכים ב-MCP.

### קונפיגורציה

1. **צור קובץ קונפיגורציה MCP** ב`%APPDATA%\Claude\claude_desktop_config.json` (ווינדוס) או `~/Library/Application Support/Claude/claude_desktop_config.json` (מק):

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

2. **אתחל מחדש את Claude**: סגור ופתח מחדש את Claude לטעינת קונפיגורציית השרת החדשה.

3. **בדוק את החיבור**: התחל שיחה עם Claude ונסה להשתמש בכלי השרת שלך:
   - "האם תוכל לברך אותי באמצעות כלי הברכה?"
   - "חשב את הסכום של 15 ו-27"
   - "מהו מידע השרת?"

### דוגמת שרת stdio ב-TypeScript

הנה דוגמה מלאה ב-TypeScript כהפניה:

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

בשיעור המעודכן הזה למדת כיצד:

- לבנות שרתי MCP באמצעות **טרנספורט stdio** הנוכחי (הגישה המומלצת)
- להבין מדוע טרנספורט SSE הפך ללא מומלץ לטובת stdio ו-Streamable HTTP
- ליצור כלים שניתן לקרוא להם על ידי לקוחות MCP
- לבצע איתור באגים בשרת שלך באמצעות MCP Inspector
- לשלב את שרת stdio שלך עם VS Code ו-Claude

טרנספורט stdio מספק דרך פשוטה, בטוחה ובעלת ביצועים טובים יותר לבניית שרתי MCP לעומת גישת SSE המיושנת. זוהי הדרך המומלצת לרוב יישומי שרת MCP מאז המפרט מ-2025-06-18.


### .NET

1. נתחיל ביצירת כלים, לשם כך ניצור קובץ *Tools.cs* עם התוכן הבא:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## תרגיל: בדיקת שרת stdio שלך

כעת שכבר בנית את שרת stdio שלך, בוא נבדוק שהוא פועל כראוי.

### דרישות מוקדמות

1. ודא שהתקנת את MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. קוד השרת שלך צריך להיות שמור (למשל כ-`server.py`)

### בדיקה עם ה-Inspector

1. **הפעל את ה-Inspector יחד עם השרת**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **פתח את ממשק הרשת**: Inspector יפתח דפדפן המציג את יכולות השרת.

3. **בדוק את הכלים**: 
   - נסה את כלי `get_greeting` עם שמות שונים
   - בדוק את כלי `calculate_sum` עם מספרים מגוונים
   - קרא לכלי `get_server_info` כדי לראות מטא-נתוני שרת

4. **עקוב אחרי התקשורת**: ה-Inspector מראה את הודעות ה-JSON-RPC המוחלפות בין הלקוח לשרת.

### מה תראה

כאשר השרת שלך יתחיל כהלכה, תראה:
- יכולות שרת המופיעות ב-Inspector
- כלים זמינים לבדיקה
- חילופי הודעות JSON-RPC מוצלחים
- תגובות הכלים מוצגות בממשק

### בעיות נפוצות ופתרונות

**השרת לא מתחיל:**
- בדוק שכל התלויות מותקנות: `pip install mcp`
- אמת תחביר והיסטים של Python
- חפש הודעות שגיאה בקונסולה

**כלים לא מופיעים:**
- ודא שקישוטי `@server.tool()` קיימים
- בדוק שהפונקציות לכלים מוגדרות לפני `main()`
- אמת שהשרת מוגדר כראוי

**בעיות חיבור:**
- ודא שהשרת משתמש בטרנספורט stdio כראוי
- בדוק שאין תהליכים אחרים שמפריעים
- אמת את תחביר הפקודה ל-Inspector

## משימה

נסה להרחיב את השרת עם יכולות נוספות. ראה [אתר זה](https://api.chucknorris.io/) כדי למשל להוסיף כלי שקורא ל-API. תחליט בעצמך איך השרת ייראה. שיהיה כיף :)
## פתרון

[פתרון](./solution/README.md) הנה פתרון אפשרי עם קוד עובד.

## נקודות עיקריות לזכור

נקודות העיקריות מפרק זה הן:

- טרנספורט stdio הוא המנגנון המומלץ לשרתים מקומיים ב-MCP.
- טרנספורט stdio מאפשר תקשורת חלקה בין שרתי MCP ללקוחות באמצעות זרמי הקלט והפלט הסטנדרטיים.
- אפשר להשתמש גם ב-Inspector וגם ב-Visual Studio Code כדי לצרוך שרתי stdio ישירות, מה שהופך את איתור הבאגים והאינטגרציה לפשוטים.

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

אחרי שלמדת כיצד לבנות שרתי MCP עם טרנספורט stdio, תוכל לחקור נושאים מתקדמים יותר:

- **הבא**: [HTTP סטרימינג עם MCP (Streamable HTTP)](../06-http-streaming/README.md) - ללמוד על מנגנון הטרנספורט הנתמך השני לשרתים מרוחקים
- **מתקדם**: [הנחיות אבטחה ב-MCP](../../02-Security/README.md) - ליישם אבטחה בשרתי MCP שלך
- **ייצור**: [אסטרטגיות פריסה](../09-deployment/README.md) - לפרוס את השרתים לשימוש ייצור

## משאבים נוספים

- [מפרט MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - מפרט נוכחי
- [תיעוד MCP SDK](https://github.com/modelcontextprotocol/sdk) - הפניות ל-SDK בכל השפות
- [דוגמאות קהילתיות](../../06-CommunityContributions/README.md) - דוגמאות שרת נוספות מהקהילה

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->