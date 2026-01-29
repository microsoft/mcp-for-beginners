# MCP stdio Server - פתרון .NET

> **⚠️ חשוב**: הפתרון הזה עודכן לשימוש ב**stdio transport** כפי שמומלץ במפרט MCP 2025-06-18. השימוש ב-SSE transport המקורי הופסק.

## סקירה כללית

פתרון .NET זה מדגים כיצד לבנות שרת MCP באמצעות stdio transport הנוכחי. ה-stdio transport פשוט יותר, מאובטח יותר ומספק ביצועים טובים יותר בהשוואה לגישה המיושנת של SSE.

## דרישות מקדימות

- .NET 9.0 SDK או גרסה מאוחרת יותר
- הבנה בסיסית של הזרקת תלות ב-.NET

## הוראות התקנה

### שלב 1: שחזור תלות

```bash
dotnet restore
```

### שלב 2: בניית הפרויקט

```bash
dotnet build
```

## הפעלת השרת

שרת ה-stdio פועל בצורה שונה משרת HTTP הישן. במקום להפעיל שרת אינטרנט, הוא מתקשר דרך stdin/stdout:

```bash
dotnet run
```

**חשוב**: השרת ייראה כאילו הוא "נתקע" - זה נורמלי! הוא ממתין להודעות JSON-RPC מ-stdin.

## בדיקת השרת

### שיטה 1: שימוש ב-MCP Inspector (מומלץ)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

זה יבצע:
1. הפעלת השרת כתהליך משנה
2. פתיחת ממשק אינטרנט לבדיקות
3. אפשרות לבדוק את כל כלי השרת בצורה אינטראקטיבית

### שיטה 2: בדיקה ישירה משורת הפקודה

ניתן גם לבדוק על ידי הפעלת ה-Inspector ישירות:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### כלים זמינים

השרת מספק את הכלים הבאים:

- **AddNumbers(a, b)**: חיבור שני מספרים
- **MultiplyNumbers(a, b)**: כפל שני מספרים  
- **GetGreeting(name)**: יצירת ברכה מותאמת אישית
- **GetServerInfo()**: קבלת מידע על השרת

### בדיקה עם Claude Desktop

כדי להשתמש בשרת הזה עם Claude Desktop, הוסף את התצורה הזו ל-`claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## מבנה הפרויקט

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## הבדלים מרכזיים מ-HTTP/SSE

**stdio transport (נוכחי):**
- ✅ התקנה פשוטה - אין צורך בשרת אינטרנט
- ✅ אבטחה טובה יותר - אין נקודות קצה HTTP
- ✅ שימוש ב-`Host.CreateApplicationBuilder()` במקום `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` במקום `WithHttpTransport()`
- ✅ יישום קונסול במקום יישום אינטרנט
- ✅ ביצועים טובים יותר

**HTTP/SSE transport (מיושן):**
- ❌ דרש שרת אינטרנט ASP.NET Core
- ❌ היה צורך בהגדרת ניתוב `app.MapMcp()`
- ❌ תצורה ותלות מורכבות יותר
- ❌ שיקולי אבטחה נוספים
- ❌ הופסק במפרט MCP 2025-06-18

## תכונות פיתוח

- **הזרקת תלות**: תמיכה מלאה ב-DI עבור שירותים ולוגים
- **לוגים מובנים**: לוגים נכונים ל-stderr באמצעות `ILogger<T>`
- **מאפייני כלים**: הגדרת כלים נקייה באמצעות `[McpServerTool]`
- **תמיכה ב-Async**: כל הכלים תומכים בפעולות אסינכרוניות
- **טיפול בשגיאות**: טיפול בשגיאות בצורה אלגנטית ולוגים

## טיפים לפיתוח

- השתמש ב-`ILogger` ללוגים (לעולם אל תכתוב ישירות ל-stdout)
- בנה עם `dotnet build` לפני בדיקות
- בדוק עם ה-Inspector לצורך ניפוי חזותי
- כל הלוגים נכתבים אוטומטית ל-stderr
- השרת מטפל באותות כיבוי בצורה אלגנטית

פתרון זה עוקב אחר מפרט MCP הנוכחי ומדגים את שיטות העבודה המומלצות ליישום stdio transport באמצעות .NET.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.