# שרת MCP עם תחבורת stdio  

> **⚠️ עדכון חשוב**: מאז מפרט MCP מתאריך 2025-06-18, תחבורת SSE העצמאית (Server-Sent Events) הוגדרה כ**מאולצת** והוחלפה בתחבורת "Streamable HTTP". מפרט ה-MCP הנוכחי מגדיר שני מנגנוני תחבורה עיקריים:  
> 1. **stdio** - קלט/פלט סטנדרטי (מומלץ לשרתי מקומיים)  
> 2. **Streamable HTTP** - לשרתי מרוחקים שעשויים להשתמש ב-SSE פנימית  
>  
> שיעור זה עודכן כדי להתמקד בתחבורת **stdio**, שהיא הגישה המומלצת לרוב יישומי שרת MCP.  

תחבורת stdio מאפשרת לשרתי MCP לתקשר עם לקוחות דרך זרמי קלט ופלט סטנדרטיים. זוהי שיטת התחבורה הנפוצה והמומלצת במפרט MCP הנוכחי, המספקת דרך פשוטה ויעילה לבניית שרתי MCP שניתן לשלבם בקלות עם יישומי לקוח שונים.  

## סקירה כללית  

שיעור זה סוקר כיצד לבנות ולצרוך שרתי MCP המשתמשים בתחבורת stdio.  

## מטרות למידה  

בסיום שיעור זה תוכל:  

- לבנות שרת MCP המשתמש בתחבורת stdio.  
- לנפות שגיאות בשרת MCP באמצעות Inspector.  
- לצרוך שרת MCP באמצעות Visual Studio Code.  
- להבין את מנגנוני התחבורה הנוכחיים ב-MCP ולמה stdio מומלץ.  


## תחבורת stdio - כיצד זה עובד  

תחבורת stdio היא אחת משתי תחבורות הסטנדרט במפרט MCP  
`2026-07-28`. כך זה עובד:  

- **תקשורת פשוטה**: השרת קורא הודעות JSON-RPC מקלט סטנדרטי (`stdin`) ושולח הודעות לפלט סטנדרטי (`stdout`).  
- **מבוסס תהליך**: הלקוח מפעיל את שרת ה-MCP כתת-תהליך.  
- **פורמט הודעות**: ההודעות הן בקשות JSON-RPC, הודעות או תגובות נפרדות, המופרדות על ידי שורות חדשות.  
- **רישום לוגים**: השרת רשאי לכתוב מחרוזות UTF-8 לסטנדרט ארור (`stderr`) לצרכי רישום.  

### דרישות מרכזיות:  
- ההודעות חייבות להיות מופרדות בשורות חדשות ואסור שתכילו שורות חדשות משובצות  
- השרת אסור שיכתוב דבר ל-`stdout` שאינו הודעת MCP תקינה  
- הלקוח אסור שיכתוב דבר ל-`stdin` של השרת שאינו הודעת MCP תקינה  

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
  
בקוד שלמעלה:  

- אנחנו מייבאים את המחלקה `Server` ואת `StdioServerTransport` מתוך ערכת הפיתוח MCP  
- יוצרים מופע שרת עם קונפיגורציה ויכולות בסיסיות  
- יוצרים מופע `StdioServerTransport` ומחברים אליו את השרת, המאפשר תקשורת דרך stdin/stdout  

### Python  

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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
  
בקוד שלמעלה אנחנו:  

- יוצרים מופע שרת באמצעות ערכת הפיתוח MCP  
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
  
ההבדל המרכזי לעומת SSE הוא ששרתי stdio:  

- אינם דורשים הקמת שרת אינטרנט או נקודות קצה HTTP  
- מופעלים כתת-תהליכים על ידי הלקוח  
- מתקשרים דרך זרמי stdin/stdout  
- פשוטים יותר ליישום וניפוי שגיאות  

## תרגיל: יצירת שרת stdio  

כדי ליצור את השרת שלנו, עלינו לזכור שני דברים:  

- אנו זקוקים לשרת אינטרנט כדי לחשוף נקודות קצה לחיבור ולהודעות.  
## מעבדה: יצירת שרת MCP stdio פשוט  

במעבדה זו, ניצור שרת MCP פשוט המשתמש בתחבורת stdio המומלצת. שרת זה יחשוף כלים שניתן לקרוא להם דרך פרוטוקול Model Context הסטנדרטי.  

### דרישות מוקדמות  

- Python 3.8 או מאוחר יותר  
- ערכת הפיתוח MCP Python: `pip install mcp`  
- הבנה בסיסית של תכנות אסינכרוני  

נתחיל ביצירת שרת stdio ראשון שלנו:  

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```
  
## הבדלים מרכזיים לעומת גישת SSE המיושנת  

**תחבורת stdio (תקן נוכחי):**  
- מודל תת-תהליך פשוט - הלקוח מפעיל את השרת כתהליך ילד  
- תקשורת דרך stdin/stdout באמצעות הודעות JSON-RPC  
- אין צורך בהקמת שרת HTTP  
- ביצועים וביטחון טובים יותר  
- ניפוי שגיאות ופיתוח קלים יותר  

**תחבורת SSE (מאולצת מאז MCP 2025-06-18):**  
- דרוש שרת HTTP עם נקודות קצה SSE  
- התקנה מורכבת יותר עם תשתית שרת אינטרנט  
- שיקולי ביטחון נוספים עבור נקודות קצה HTTP  
- הוחלפה ב-Streamable HTTP לסצנאריוני רשת  

### יצירת שרת עם תחבורת stdio  

כדי ליצור את שרת ה-stdio שלנו, עלינו:  

1. **לייבא את הספריות הנדרשות** - נדרשים רכיבי שרת MCP ותחבורת stdio  
2. **ליצור מופע שרת** - להגדיר את השרת עם היכולות שלו  
3. **להגדיר כלים** - להוסיף את הפונקציונליות שברצוננו לחשוף  
4. **להגדיר את התחבורה** - להגדיר את תקשורת stdio  
5. **להפעיל את השרת** - להתחיל את השרת ולטפל בהודעות  

בואו נבנה את זה שלב אחר שלב:  

### שלב 1: יצירת שרת stdio בסיסי  

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
  
השרת יתחיל ויחכה לקלט מ-stdin. הוא מתקשר באמצעות הודעות JSON-RPC דרך תחבורת stdio.  

### שלב 4: בדיקה עם Inspector  

ניתן לבדוק את השרת באמצעות ה-MCP Inspector:  

1. התקן את ה-Inspector: `npx @modelcontextprotocol/inspector`  
2. הפעל את ה-Inspector וכוון אותו לשרת שלך  
3. בדוק את הכלים שיצרת  

### .NET  

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## ניפוי שגיאות בשרת stdio שלך  

### שימוש ב-MCP Inspector  

MCP Inspector הוא כלי חשוב לניפוי שגיאות ובדיקת שרתי MCP. כך משתמשים בו עם שרת stdio שלך:  

1. **התקן את ה-Inspector**:  
   ```bash
   npx @modelcontextprotocol/inspector
   ```
  
2. **הפעל את ה-Inspector**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
3. **בדוק את השרת שלך**: ה-Inspector מספק ממשק רשת בו ניתן:  
   - לצפות ביכולות השרת  
   - לבדוק כלים עם פרמטרים שונים  
   - לנטר הודעות JSON-RPC  
   - לנפות בעיות חיבור  

### שימוש ב-VS Code  

ניתן גם לנפות שגיאות בשרת MCP ישירות ב-VS Code:  

1. צור תצורת הפעלה ב-`.vscode/launch.json`:  
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
3. הפעל את מנפה השגיאות ובדוק עם ה-Inspector  

### טיפים נפוצים לניפוי שגיאות  

- השתמש ב-`stderr` לרישום לוגים - לעולם לא כתוב ל-`stdout` שמור להודעות MCP  
- ודא שכל הודעות JSON-RPC מופרדות בשורות חדשות  
- בדוק כלים פשוטים תחילה לפני הוספת פונקציונליות מורכבת  
- השתמש ב-Inspector לווידוא פורמטים של הודעות  

## צריכת שרת stdio שלך ב-VS Code  

לאחר שבנית את שרת MCP stdio שלך, ניתן לשלבו ב-VS Code לשימוש עם Claude או לקוחות MCP אחרים.  

### קונפיגורציה  

1. **צור קובץ קונפיגורציית MCP** ב-`%APPDATA%\Claude\claude_desktop_config.json` (Windows) או ב-`~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):  

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
  
2. **הפעל מחדש את Claude**: סגור ופתח מחדש את Claude לטעינת קונפיגורציית השרת החדשה.  

3. **בדוק את החיבור**: התחיל שיחה עם Claude ונסה להשתמש בכלי השרת:  
   - "האם תוכל לברך אותי באמצעות כלי הברכה?"  
   - "חשב את הסכום של 15 ו-27"  
   - "מהן פרטי השרת?"  

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

// Add tools
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

בשיעור המעודכן נלמד:  

- לבנות שרתי MCP באמצעות **תחבורת stdio** הנוכחית (הגישה המומלצת)  
- להבין מדוע תחבורת SSE בוטלה לטובת stdio ו-Streamable HTTP  
- ליצור כלים שניתן לקרוא להם מלקוחות MCP  
- לנפות שגיאות בשרת שלך באמצעות MCP Inspector  
- לשלב שרת stdio שלך עם VS Code ו-Claude  

תחבורת stdio מספקת דרך פשוטה, מאובטחת ויעילה יותר לבניית שרתי MCP בהשוואה לשיטת SSE המיושנת. היא התחבורה המומלצת לרוב יישומי שרת MCP בהתאם למפרט 2025-06-18.  


### .NET  

1. נתחיל ביצירת כלים, לשם כך ניצור קובץ *Tools.cs* עם התוכן הבא:  

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```
  
## תרגיל: בדיקת שרת stdio שלך  

עכשיו כשבנינו את שרת ה-stdio שלך, בוא נבדוק שהוא פועל כראוי.  

### דרישות מוקדמות  

1. ודא כי התקנת את MCP Inspector:  
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```
  
2. קוד השרת שלך צריך להיות שמור (למשל כ-`server.py`)  

### בדיקה עם ה-Inspector  

1. **הפעל את ה-Inspector עם השרת שלך**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
2. **פתח את ממשק הרשת**: ה-Inspector יפתח חלון דפדפן המציג את יכולות השרת שלך.  

3. **בדוק את הכלים**:  
   - נסה את הכלי `get_greeting` עם שמות שונים  
   - בדוק את הכלי `calculate_sum` עם מספרים שונים  
   - קרא לכלי `get_server_info` כדי לראות מטה-דאטה של השרת  

4. **נטר את התקשורת**: ה-Inspector מציג את הודעות JSON-RPC המחליפות בין הלקוח לשרת.  

### מה תראה  

כאשר השרת שלך יתחיל כראוי, תראה:  
- יכולות השרת ברשימה ב-Inspector  
- כלים זמינים לבדיקות  
- החלפות הודעות JSON-RPC מוצלחות  
- תגובות כלים מוצגות בממשק  

### בעיות נפוצות ופתרונות  

**השרת לא מתחיל:**  
- ודא שכל התלויות מותקנות: `pip install mcp`  
- בדוק תחביר והזחות בפייתון  
- חפש הודעות שגיאה במסוף  

**כלים לא מופיעים:**  
- ודא שקיימים דקורטורי `@server.tool()`  
- בדוק שהפונקציות של הכלים מוגדרות לפני `main()`  
- ודא שהשרת מקונפג כראוי  

**בעיות חיבור:**  
- ודא שהשרת משתמש בתחבורת stdio נכון  
- בדוק שאף תהליך אחר לא מפריע  
- ודא תחביר הפקודה של ה-Inspector  

## מטלה  

נסה להרחיב את השרת שלך עם יותר יכולות. ראה [דף זה](https://api.chucknorris.io/) כדי, למשל, להוסיף כלי שקורא ל-API. אתה קובע איך השרת צריך להיראות. תהנה :)  
## פתרון  

[פתרון](./solution/README.md) הנה פתרון אפשרי עם קוד עובד.  

## נקודות מרכזיות  

הנקודות המרכזיות מפרק זה הן:  

- תחבורת stdio היא מנגנון התחבורה המומלץ לשרתי MCP מקומיים.  
- תחבורת stdio מאפשרת תקשורת חלקה בין שרתי MCP ללקוחות דרך זרמי קלט ופלט סטנדרטיים.  
- ניתן להשתמש גם ב-Inspector וגם ב-Visual Studio Code לצריכת שרתי stdio ישירות, מה שהפך את ניפוי השגיאות והאינטגרציה לפשוטים.  

## דוגמאות  

- [מחשבון Java](../samples/java/calculator/README.md)  
- [מחשבון .NET](../../../../03-GettingStarted/samples/csharp)  
- [מחשבון JavaScript](../samples/javascript/README.md)  
- [מחשבון TypeScript](../samples/typescript/README.md)  
- [מחשבון Python](../../../../03-GettingStarted/samples/python)  

## משאבים נוספים  

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)  

## מה הלאה  

## צעדים הבאים  

כעת כשמדעת כיצד לבנות שרתי MCP עם תחבורת stdio, תוכל לחקור נושאים מתקדמים יותר:  

- **הבא**: [HTTP Streaming עם MCP (Streamable HTTP)](../06-http-streaming/README.md) - למידה על מנגנון תחבורה נוסף הנתמך לשרתי מרוחקים  
- **מתקדם**: [שיטות בטיחות מקובלות ב-MCP](../../02-Security/README.md) - יישום אבטחה בשרתי MCP שלך  
- **פרודקשן**: [אסטרטגיות פריסה](../09-deployment/README.md) - פריסת השרתים לשימוש בייצור  

## משאבים נוספים  

- [מפרט MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - מפרט נוכחי  
- [מסמכי ערכת פיתוח MCP](https://github.com/modelcontextprotocol/sdk) - הפניות SDK לכל השפות  
- [דוגמאות מהקהילה](../../06-CommunityContributions/README.md) - דוגמאות נוספות מיישומי שרת של הקהילה  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->