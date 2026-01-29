# שרת MCP עם stdio Transport

> **⚠️ עדכון חשוב**: החל ממפרט MCP 2025-06-18, ה-SSE (Server-Sent Events) העצמאי **הוצא משימוש** והוחלף ב-"Streamable HTTP" transport. מפרט MCP הנוכחי מגדיר שני מנגנוני תעבורה עיקריים:
> 1. **stdio** - קלט/פלט סטנדרטי (מומלץ לשרתים מקומיים)
> 2. **Streamable HTTP** - לשרתים מרוחקים שעשויים להשתמש ב-SSE באופן פנימי
>
> שיעור זה עודכן להתמקד ב-**stdio transport**, שהוא הגישה המומלצת לרוב מימושי שרתי MCP.

ה-stdio transport מאפשר לשרתי MCP לתקשר עם לקוחות דרך זרמי קלט ופלט סטנדרטיים. זהו מנגנון התעבורה הנפוץ והמומלץ ביותר במפרט MCP הנוכחי, המספק דרך פשוטה ויעילה לבנות שרתי MCP שניתן לשלב בקלות עם יישומי לקוח שונים.

## סקירה כללית

שיעור זה מכסה כיצד לבנות ולצרוך שרתי MCP באמצעות stdio transport.

## מטרות למידה

בסיום השיעור, תוכלו:

- לבנות שרת MCP באמצעות stdio transport.
- לנטר ולתקן באגים בשרת MCP באמצעות ה-Inspector.
- לצרוך שרת MCP באמצעות Visual Studio Code.
- להבין את מנגנוני התעבורה הנוכחיים של MCP ולמה stdio מומלץ.

## stdio Transport - איך זה עובד

ה-stdio transport הוא אחד משני סוגי התעבורה הנתמכים במפרט MCP הנוכחי (2025-06-18). כך זה עובד:

- **תקשורת פשוטה**: השרת קורא הודעות JSON-RPC מקלט סטנדרטי (`stdin`) ושולח הודעות לפלט סטנדרטי (`stdout`).
- **מבוסס תהליך**: הלקוח מפעיל את שרת ה-MCP כתהליך משנה.
- **פורמט הודעות**: ההודעות הן בקשות, התראות או תגובות JSON-RPC בודדות, המופרדות על ידי שורות חדשות.
- **לוגים**: השרת **עשוי** לכתוב מחרוזות UTF-8 לשגיאה סטנדרטית (`stderr`) לצורכי לוגים.

### דרישות עיקריות:
- ההודעות **חייבות** להיות מופרדות על ידי שורות חדשות ו**אסור** להכיל שורות חדשות משובצות.
- השרת **אסור** שיכתוב ל-`stdout` משהו שאינו הודעת MCP תקינה.
- הלקוח **אסור** שיכתוב ל-`stdin` של השרת משהו שאינו הודעת MCP תקינה.

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

- אנו מייבאים את המחלקה `Server` ואת `StdioServerTransport` מ-SDK של MCP.
- אנו יוצרים מופע של שרת עם תצורה ויכולות בסיסיות.

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

בקוד הקודם אנו:

- יוצרים מופע של שרת באמצעות SDK של MCP.
- מגדירים כלים באמצעות דקורטורים.
- משתמשים ב-context manager של stdio_server לניהול התעבורה.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

ההבדל המרכזי מ-SSE הוא ששרתי stdio:

- אינם דורשים הגדרת שרת אינטרנט או נקודות קצה HTTP.
- מופעלים כתהליכי משנה על ידי הלקוח.
- מתקשרים דרך זרמי stdin/stdout.
- פשוטים יותר ליישום ולניטור.

## תרגיל: יצירת שרת stdio

כדי ליצור את השרת שלנו, עלינו לזכור שני דברים:

- עלינו להשתמש בשרת אינטרנט כדי לחשוף נקודות קצה לחיבור ולהודעות.

## מעבדה: יצירת שרת MCP stdio פשוט

במעבדה זו, ניצור שרת MCP פשוט באמצעות stdio transport המומלץ. שרת זה יחשוף כלים שלקוחות יוכלו לקרוא באמצעות פרוטוקול Model Context.

### דרישות מוקדמות

- Python 3.8 או גרסה מאוחרת יותר.
- SDK של MCP לפייתון: `pip install mcp`.
- הבנה בסיסית של תכנות אסינכרוני.

בואו נתחיל ביצירת שרת MCP stdio הראשון שלנו:

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

## הבדלים מרכזיים מגישת SSE שהוצאה משימוש

**Stdio Transport (הסטנדרט הנוכחי):**
- מודל פשוט של תהליך משנה - הלקוח מפעיל את השרת כתהליך משנה.
- תקשורת דרך stdin/stdout באמצעות הודעות JSON-RPC.
- אין צורך בהגדרת שרת HTTP.
- ביצועים ואבטחה טובים יותר.
- קל יותר לניטור ופיתוח.

**SSE Transport (הוצא משימוש החל מ-MCP 2025-06-18):**
- דרש שרת HTTP עם נקודות קצה של SSE.
- הגדרה מורכבת יותר עם תשתית שרת אינטרנט.
- שיקולי אבטחה נוספים לנקודות קצה HTTP.
- הוחלף כעת ב-Streamable HTTP לתרחישים מבוססי אינטרנט.

### יצירת שרת עם stdio transport

כדי ליצור שרת stdio, עלינו:

1. **לייבא את הספריות הנדרשות** - נזדקק לרכיבי שרת MCP ול-stdio transport.
2. **ליצור מופע של שרת** - להגדיר את השרת עם יכולותיו.
3. **להגדיר כלים** - להוסיף את הפונקציונליות שברצוננו לחשוף.
4. **להגדיר את התעבורה** - להגדיר תקשורת stdio.
5. **להפעיל את השרת** - להפעיל את השרת ולטפל בהודעות.

בואו נבנה זאת שלב אחר שלב:

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

שמרו את הקוד כ-`server.py` והפעילו אותו משורת הפקודה:

```bash
python server.py
```

השרת יתחיל וימתין לקלט מ-stdin. הוא מתקשר באמצעות הודעות JSON-RPC על גבי stdio transport.

### שלב 4: בדיקה עם ה-Inspector

ניתן לבדוק את השרת שלכם באמצעות MCP Inspector:

1. התקינו את ה-Inspector: `npx @modelcontextprotocol/inspector`.
2. הפעילו את ה-Inspector והפנו אותו לשרת שלכם.
3. בדקו את הכלים שיצרתם.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## ניטור שרת stdio שלכם

### שימוש ב-MCP Inspector

ה-MCP Inspector הוא כלי חשוב לניטור ובדיקת שרתי MCP. כך תשתמשו בו עם שרת stdio שלכם:

1. **התקינו את ה-Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **הפעילו את ה-Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **בדקו את השרת שלכם**: ה-Inspector מספק ממשק אינטרנט שבו תוכלו:
   - לצפות ביכולות השרת.
   - לבדוק כלים עם פרמטרים שונים.
   - לעקוב אחר הודעות JSON-RPC.
   - לנטר בעיות חיבור.

### שימוש ב-VS Code

ניתן גם לנטר את שרת MCP שלכם ישירות ב-VS Code:

1. צרו קובץ תצורה ב-`.vscode/launch.json`:
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

2. הגדירו נקודות עצירה בקוד השרת שלכם.
3. הפעילו את מנטר הבאגים ובדקו עם ה-Inspector.

### טיפים נפוצים לניטור

- השתמשו ב-`stderr` ללוגים - לעולם אל תכתבו ל-`stdout`, שמיועד להודעות MCP בלבד.
- ודאו שכל הודעות JSON-RPC מופרדות בשורות חדשות.
- התחילו עם כלים פשוטים לפני הוספת פונקציונליות מורכבת.
- השתמשו ב-Inspector כדי לוודא את פורמט ההודעות.

## צריכת שרת stdio שלכם ב-VS Code

לאחר שבניתם את שרת MCP stdio שלכם, תוכלו לשלב אותו עם VS Code כדי להשתמש בו עם Claude או לקוחות תואמי MCP אחרים.

### תצורה

1. **צרו קובץ תצורה של MCP** ב-`%APPDATA%\Claude\claude_desktop_config.json` (Windows) או `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **אתחלו את Claude**: סגרו ופתחו מחדש את Claude כדי לטעון את תצורת השרת החדשה.

3. **בדקו את החיבור**: התחילו שיחה עם Claude ונסו להשתמש בכלים של השרת שלכם:
   - "תוכל לברך אותי באמצעות כלי הברכה?"
   - "חשב את הסכום של 15 ו-27."
   - "מהו מידע השרת?"

### דוגמה לשרת stdio ב-TypeScript

להלן דוגמה מלאה ב-TypeScript לעיונכם:

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
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## סיכום

בשיעור זה למדתם כיצד:

- לבנות שרתי MCP באמצעות **stdio transport** (הגישה המומלצת).
- להבין מדוע תעבורת SSE הוצאה משימוש לטובת stdio ו-Streamable HTTP.
- ליצור כלים שניתן לקרוא על ידי לקוחות MCP.
- לנטר את השרת שלכם באמצעות MCP Inspector.
- לשלב את שרת stdio שלכם עם VS Code ו-Claude.

ה-stdio transport מספק דרך פשוטה, מאובטחת ובעלת ביצועים טובים יותר לבנות שרתי MCP בהשוואה לגישת SSE שהוצאה משימוש. זהו מנגנון התעבורה המומלץ לרוב מימושי שרתי MCP החל ממפרט 2025-06-18.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.