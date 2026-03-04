# שרת MCP עם תחבורת stdio

> **⚠️ עדכון חשוב**: החל מ-MCP Specification 2025-06-18, תחבורת SSE עצמאית (Server-Sent Events) הוכרזה כ**מיושנת** והוחלפה בתחבורת "Streamable HTTP". המפרט הנוכחי של MCP מגדיר שני מנגנוני תחבורה עיקריים:
> 1. **stdio** - קלט/פלט סטנדרטי (מומלץ לשרתים מקומיים)
> 2. **Streamable HTTP** - עבור שרתים מרוחקים שעשויים להשתמש ב-SSE פנימית
>
> שיעור זה עודכן כדי להתמקד ב**תחבורת stdio**, שהיא הגישה המומלצת לרוב מימושי שרת MCP.

תחבורת ה-stdio מאפשרת לשרתי MCP לתקשר עם לקוחות דרך זרמי קלט ופלט סטנדרטיים. זוהי שיטת התחבורה הנפוצה והמומלצת במפרט MCP הנוכחי, המספקת דרך פשוטה ויעילה לבנות שרתי MCP שניתן לשלב בקלות עם יישומי לקוח שונים.

## סקירה כללית

שיעור זה דן כיצד לבנות ולצרוך שרתי MCP באמצעות תחבורת stdio.

## מטרות למידה

בסיום שיעור זה תוכל:

- לבנות שרת MCP באמצעות תחבורת stdio.
- לבצע איתור שגיאות בשרתי MCP באמצעות Inspector.
- לצרוך שרת MCP באמצעות Visual Studio Code.
- להבין את מנגנוני התחבורה הנוכחיים של MCP ולמה stdio מומלץ.

## תחבורת stdio - איך זה עובד

תחבורת ה-stdio היא אחד משני סוגי התחבורה הנתמכים במפרט MCP הנוכחי (2025-06-18). כך זה עובד:

- **תקשורת פשוטה**: השרת קורא הודעות JSON-RPC מ-standard input (`stdin`) ושולח הודעות ל-standard output (`stdout`).
- **מבוסס תהליך**: הלקוח מפעיל את שרת MCP כתהליך משני.
- **פורמט הודעות**: ההודעות הן בקשות JSON-RPC בודדות, התראות או תגובות, המופרדות בשורות חדשות.
- **רישום**: השרת יכול לכתוב מחרוזות UTF-8 ל-standard error (`stderr`) לצורך רישום.

### דרישות מפתח:
- ההודעות חייבות להיות מופרדות בשורות חדשות ואסור שיכילו שורות חדשות בתוך ההודעה
- השרת חייב לא לכתוב ל-`stdout` כל דבר שאינו הודעת MCP תקפה
- הלקוח חייב לא לכתוב ל-`stdin` של השרת כל דבר שאינו הודעת MCP תקפה

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
```
  
בקוד הקודם:

- מייבאים את מחלקת `Server` ואת `StdioServerTransport` מ-SDK של MCP
- יוצרים מופע שרת עם תצורה ויכולות בסיסיות

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
  
בקוד הקודם:

- יוצרים מופע שרת באמצעות SDK של MCP
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

- לא דורשים הקמת שרת ווב או נקודות קצה HTTP
- מופעלים כתהליכים משניים על ידי הלקוח
- מתקשרים דרך זרמי stdin/stdout
- פשוטים יותר ליישום ולאיתור שגיאות

## תרגיל: יצירת שרת stdio

כדי ליצור את השרת שלנו, עלינו לזכור שני דברים:

- עלינו להשתמש בשרת ווב כדי לחשוף נקודות קצה לחיבור ולהודעות.

## מעבדה: יצירת שרת MCP stdio פשוט

במעבדה זו ניצור שרת MCP פשוט באמצעות תחבורת stdio המומלצת. שרת זה יספק כלים שהלקוחות יוכלו לקרוא באמצעות פרוטוקול Model Context Protocol הסטנדרטי.

### דרישות מקדימות

- Python 3.8 ומעלה
- MCP Python SDK: `pip install mcp`
- הבנה בסיסית בתכנות אסינכרוני

נתחיל ביצירת שרת MCP stdio ראשון שלנו:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# הגדר יומן רישום
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
  

## הבדלים עיקריים מהגישה הישן של SSE

**תחבורת stdio (תקן נוכחי):**
- מודל תהליך משני פשוט - הלקוח מפעיל את השרת כתהליך ילד
- תקשורת דרך stdin/stdout באמצעות הודעות JSON-RPC
- אין צורך בהקמת שרת HTTP
- ביצועים ובטיחות טובים יותר
- איתור שגיאות ופיתוח קלים יותר

**תחבורת SSE (מיושנת החל מ-MCP 2025-06-18):**
- דרש שרת HTTP עם נקודות SSE
- הקמה מורכבת יותר עם תשתית שרת ווב
- שיקולי אבטחה נוספים לנקודות HTTP
- הוחלף כעת ב-Streamable HTTP לתרחישי ווב

### יצירת שרת עם תחבורת stdio

כדי ליצור את שרת ה-stdio שלנו, עלינו:

1. **ייבוא הספריות הדרושות** - צריכים את רכיבי השרת ותחבורת stdio
2. **יצירת מופע שרת** - להגדיר את השרת עם יכולותיו
3. **הגדרת כלים** - להוסיף את הפונקציונליות שאנו רוצים לחשוף
4. **הגדרת התחבורה** - לכוון את תקשורת ה-stdio
5. **הפעלת השרת** - להתחיל את השרת ולטפל בהודעות

נתחיל לבנות זאת שלב אחר שלב:

### שלב 1: יצירת שרת stdio בסיסי

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# הגדר יומן רישום
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

שמור את הקוד כ-`server.py` והפעל אותו משורת הפקודה:

```bash
python server.py
```
  
השרת יתחיל ויחכה לקלט מ-stdin. הוא מתקשר באמצעות הודעות JSON-RPC מעל תחבורת stdio.

### שלב 4: בדיקה עם Inspector

אתה יכול לבדוק את השרת שלך באמצעות MCP Inspector:

1. התקן את Inspector: `npx @modelcontextprotocol/inspector`
2. הפעל את Inspector ופנה לשרת שלך
3. בדוק את הכלים שיצרת

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
  
## איתור שגיאות לשרת stdio שלך

### שימוש ב-MCP Inspector

MCP Inspector הוא כלי חשוב לאיתור שגיאות ובדיקות בשרתי MCP. כך תשתמש בו עם שרת stdio שלך:

1. **התקן את Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```
  
2. **הפעל את Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
3. **בדוק את השרת שלך**: ה-Inspector מספק ממשק ווב שבו ניתן:
   - לצפות ביכולות השרת
   - לבדוק כלים עם פרמטרים שונים
   - לעקוב אחרי הודעות JSON-RPC
   - לאתר בעיות חיבור

### שימוש ב-VS Code

אתה יכול גם לבצע איתור שגיאות ישירות ב-VS Code:

1. צור תצורת הפעלה בקובץ `.vscode/launch.json`:
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
3. הפעל את הדיבאגר ובדוק עם Inspector  

### טיפים נפוצים לאיתור שגיאות

- השתמש ב-`stderr` לרישום - אל תכתוב ל-`stdout` כי הוא שמור להודעות MCP
- ודא שכל הודעות JSON-RPC מופרדות בשורה חדשה
- בדוק כלים פשוטים תחילה לפני הוספת פונקציונליות מורכבת
- השתמש ב-Inspector כדי לוודא פורמט ההודעות

## צריכת שרת stdio שלך ב-VS Code

לאחר שבנית את שרת ה-stdio שלך, תוכל לשלב אותו עם VS Code כדי להשתמש בו עם Claude או לקוחות תואמים אחרים של MCP.

### תצורה

1. **צור קובץ תצורה של MCP ב- `%APPDATA%\Claude\claude_desktop_config.json` (Windows) או `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):**

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
  
2. **הפעל מחדש את Claude**: סגור ופתח מחדש את Claude כדי לטעון את התצורה החדשה של השרת.

3. **בדוק את החיבור**: התחל שיחה עם Claude ונסה להשתמש בכלי השרת:
   - "האם תוכל לברך אותי באמצעות כלי הברכות?"
   - "חשב את סכום 15 ו-27"
   - "מה המידע על השרת?"

### דוגמה לשרת stdio ב-TypeScript

להלן דוגמה מלאה ב-TypeScript לעיון:

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
  
### דוגמה לשרת stdio ב-.NET

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

בשיעור זה למדת כיצד:

- לבנות שרתי MCP באמצעות **תחבורת stdio** הנוכחית (הגישה המומלצת)
- להבין מדוע תחבורת SSE הוכרזה כמיושנת לטובת stdio ו-Streamable HTTP
- ליצור כלים שניתן לקרוא להם על ידי לקוחות MCP
- לאתר שגיאות בשרת שלך באמצעות MCP Inspector
- לשלב את שרת stdio שלך עם VS Code ו-Claude

תחבורת stdio מספקת דרך פשוטה, בטוחה וביצועית יותר לבניית שרתי MCP בהשוואה לגישת SSE המיושנת. היא התחבורה המומלצת לרוב מימושי שרת MCP החל מהמפרט מ-18/06/2025.

### .NET

1. נתחיל ביצירת כלים, לשם כך ניצור קובץ *Tools.cs* עם התוכן הבא:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```
  
## תרגיל: בדיקת שרת stdio שלך

כעת, לאחר שבנית את שרת stdio שלך, נבדוק שהוא פועל כראוי.

### דרישות מקדימות

1. ודא שהתקנת את MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```
  
2. הקוד של השרת שלך נשמר (למשל כ-`server.py`)

### בדיקה עם Inspector

1. **הפעל את Inspector עם השרת שלך**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
2. **פתח את ממשק הווב**: ה-Inspector יפתח דפדפן המציג את יכולות השרת שלך.

3. **בדוק את הכלים**: 
   - נסה את הכלי `get_greeting` עם שמות שונים  
   - בדוק את כלי `calculate_sum` עם מספרים שונים  
   - קרא לכלי `get_server_info` כדי לצפות במטא-דטה של השרת  

4. **עקוב אחרי התקשורת**: ה-Inspector מציג את הודעות JSON-RPC שמתחלפות בין הלקוח לשרת.

### מה תראה

כאשר השרת שלך עולה בהצלחה, תראה:
- יכולות השרת ברשימה ב-Inspector
- כלי בדיקה זמינים
- החלפות הודעות JSON-RPC מוצלחות
- תגובות לכלים מוצגות בממשק

### בעיות נפוצות ופתרונות

**השרת לא מתחיל:**
- בדוק שכל התלויות מותקנות: `pip install mcp`
- ודא תחביר ופיסוק פייתון תקינים
- חפש הודעות שגיאה בקונסול

**כלים לא מופיעים:**
- ודא שקיימים דקורטורים `@server.tool()`
- בדוק שהפונקציות של הכלים מוגדרות לפני `main()`
- וודא שהשרת מוגדר נכון

**בעיות חיבור:**
- ודא שהשרת משתמש בstdio כראוי
- וודא שלא קיימים תהליכים אחרים שמפריעים
- בדוק את תחביר הפקודות של Inspector

## מטלה

נסה לבנות את השרת שלך עם יכולות נוספות. עיין בעמוד [זה](https://api.chucknorris.io/) כדי, למשל, להוסיף כלי שמבצע קריאת API. אתה מחליט איך השרת צריך להיראות. בהצלחה :)

## פתרון

[פתרון](./solution/README.md) להלן פתרון אפשרי עם קוד עובד.

## נקודות מפתח

הנקודות המרכזיות מהפרק הן:

- תחבורת stdio היא המנגנון המומלץ לשרתי MCP מקומיים.
- תחבורת stdio מאפשרת תקשורת חלקה בין שרתי MCP לבין לקוחות באמצעות זרמי קלט ופלט סטנדרטיים.
- ניתן להשתמש ב-Inspector וב-Visual Studio Code לצריכת שרתי stdio ישירות, מה שמקל על איתור בעיות ושילוב.

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

כעת שלמדת כיצד לבנות שרתי MCP עם תחבורת stdio, תוכל לחקור נושאים מתקדמים יותר:

- **הבא**: [הזרמת HTTP עם MCP (Streamable HTTP)](../06-http-streaming/README.md) - למידה על מנגנון תחבורה נוסף הנתמך לשרתים מרוחקים  
- **מתקדם**: [הנחיות אבטחת MCP](../../02-Security/README.md) - יישום אבטחה בשרתי MCP שלך  
- **לפרודקשן**: [אסטרטגיות הפצה](../09-deployment/README.md) - פרוס את השרתים שלך לשימוש בפרודקשן  

## משאבים נוספים

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - המפרט הרשמי  
- [תיעוד SDK של MCP](https://github.com/modelcontextprotocol/sdk) - הפניות SDK לכל השפות  
- [דוגמאות מהקהילה](../../06-CommunityContributions/README.md) - דוגמאות שרת נוספות מהקהילה

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום אוטומטי AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדייק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפת המקור מהווה את המקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי באנוש. אנו אינם אחראים לכל אי-הבנות או פרשנויות שגוֹת הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->