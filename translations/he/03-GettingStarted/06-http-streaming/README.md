# סטרימינג ב-HTTPS עם פרוטוקול הקשר מודל (MCP)

בפרק זה מוצג מדריך מקיף ליישום סטרימינג מאובטח, מדרגי ובזמן אמת עם פרוטוקול הקשר מודל (MCP) באמצעות HTTPS. הוא מכסה את המוטיבציה לסטרימינג, מנגנוני ההעברה הקיימים, כיצד ליישם HTTP סטרימי ב-MCP, שיטות עבודה מומלצות לאבטחה, מעבר מ-SSE, והנחיות מעשיות לבניית יישומי סטרימינג MCP משלך.

> [!WARNING]
> דוגמאות היישום בשיעור זה מכוונות ל**MCP Specification
> `2025-11-25`** ומדגימות את ההלשקה המורשת `initialize`,
> `Mcp-Session-Id`, GET event stream, ודגם ההמשך. MCP `2026-07-28`
> מסיר את התכונות הללו. בקשות HTTP סטרימביליות נוכחיות הן בקשות POST עצמאיות
> עם כותרות `MCP-Protocol-Version` ו-`Mcp-Method`, בנוסף ל-`Mcp-Name`
> במידת הצורך. ראה
> [מה השתנה ב-MCP: המפרט 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> לפני השימוש בדוגמאות אלו ביישום חדש.

## מנגנוני העברה וסטרימינג ב-MCP

קטע זה בוחן את מנגנוני ההעברה השונים הזמינים ב-MCP ואת תפקידם בהפעלת יכולות סטרימינג לתקשורת בזמן אמת בין לקוחות לשרתים.

### מהו מנגנון העברה?

מנגנון העברה מגדיר כיצד הנתונים מוחלפים בין הלקוח לשרת. MCP תומך בסוגי העברה מרובים המתאימים לסביבות שונות ולדרישות מגוונות:

- **stdio**: קלט/פלט סטנדרטי, מתאים לכלים מקומיים ומבוססי שורת פקודה. פשוט אך לא מתאים לרשת או ענן.
- **HTTP+SSE**: אמצעי ההעברה המרוחק הישן, מוטל בספק ב-MCP `2025-03-26`
    ומוחלף על ידי Streamable HTTP. אין להשתמש בו למימושים חדשים.
- **Streamable HTTP**: אמצעי הזרמת נתונים מודרני מבוסס HTTP, התומך בהתראות וסקלאביליות טובה יותר. מומלץ לרוב תרחישי הייצור והענן.

### טבלת השוואה

הסתכלו בטבלת ההשוואה למטה כדי להבין את ההבדלים בין מנגנוני ההעברה הללו:

| העברה | סטטוס | התראות | שימוש טיפוסי |
|---|---|---|---|
| stdio | נוכחי | כן | תהליכים מקומיים |
| HTTP+SSE | מוטל בספק | כן | מימושים מרוחקים ישנים |
| Streamable HTTP | נוכחי | כן | שרתים מרוחקים וענן |

> **טיפ:** הבחירה באמצעי ההעברה הנכון משפיעה על ביצועים, סקלאביליות, וחווית משתמש. **Streamable HTTP** מומלץ ליישומים מודרניים, סקלאביליים ומוכנים לענן.

אמצעי ההעברה הסטנדרטיים הם stdio ו-Streamable HTTP. HTTP+SSE מופיע בדוגמאות ישנות בלבד.


## הזרמה (Streaming): מושגים ומוטיבציה

הבנת המושגים והמוטיבציות הבסיסיים מאחורי הזרמה היא חיונית למימוש מערכות תקשורת בזמן אמת יעילות.

**הזרמה** היא טכניקה בתכנות רשת המאפשרת לשלוח ולקבל נתונים בחתיכות קטנות, ניתנות לניהול, או כרצף של אירועים, במקום להמתין לתגובה מלאה. זה שימושי במיוחד ל:

- קבצים או מערכי נתונים גדולים.
- עדכונים בזמן אמת (כגון צ'אט, פסי התקדמות).
- חישובים ארוכי טווח שבהם רוצים לעדכן את המשתמש.

הנה מה שצריך לדעת על הזרמה ברמה גבוהה:

- הנתונים נשלחים בהדרגה, לא בפעם אחת.
- הלקוח יכול לעבד את הנתונים כשהם מגיעים.
- מפחית את התחושה של עיכוב ומשפר את חווית המשתמש.

### למה להשתמש בהזרמה?

הסיבות לשימוש בהזרמה הן הבאות:

- המשתמשים מקבלים משוב מיד, לא רק בסוף
- מאפשר יישומים בזמן אמת וממשקי משתמש רספונסיביים
- שימוש יעיל יותר במשאבי רשת ומחשוב

### דוגמה פשוטה: שרת ולקוח הזרמת HTTP

הנה דוגמה פשוטה לאופן שבו ניתן לממש הזרמה:

#### Python

**שרת (Python, משתמש ב-FastAPI ו-StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**לקוח (Python, משתמש ב-requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

דוגמה זו מדגימה שרת ששולח סדרת הודעות ללקוח כשהן זמינות, במקום להמתין שכל ההודעות יהיו מוכנות.

**איך זה עובד:**

- השרת משרת כל הודעה כשהיא מוכנה.
- הלקוח מקבל ומדפיס כל חתיכה כשהיא מגיעה.

**דרישות:**

- השרת חייב להשתמש בתגובה זרמתית (למשל `StreamingResponse` ב-FastAPI).
- הלקוח חייב לעבד את התגובה כהזרמה (`stream=True` ב-requests).
- סוג התוכן בדרך כלל `text/event-stream` או `application/octet-stream`.

#### Java

**שרת (Java, משתמש ב-Spring Boot ואירועי Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**לקוח (Java, משתמש ב-Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**הערות למימוש Java:**

- משתמש בערמת Spring Boot ריאקטיבית עם `Flux` להזרמה
- `ServerSentEvent` מספק הזרמת אירועים מובנית עם סוגי אירועים
- `WebClient` עם `bodyToFlux()` מאפשר צריכת הזרמה ריאקטיבית
- `delayElements()` מדמה זמן עיבוד בין אירועים
- אירועים יכולים להכיל סוגים (`info`, `result`) להטיפול טוב יותר בלקוח

### השוואה: הזרמה קלאסית לעומת הזרמה ב-MCP

ההבדלים בין איך שההזרמה עובדת בצורה "קלאסית" לעומת איך שהיא עובדת ב-MCP ניתנים להמחשה כך:

| תכונה                | הזרמת HTTP קלאסית           | הזרמת MCP (התראות)             |
|------------------------|-----------------------------|--------------------------------|
| תגובה ראשית           | מחולקת לקטעים              | יחידה, בסוף                   |
| עדכוני התקדמות        | נשלחים כקטעי נתונים        | נשלחים כהודעות התראה          |
| דרישות מהלקוח          | חייב לעבד זרם               | חייב לממש מטפל בהודעות          |
| מקרה שימוש           | קבצים גדולים, זרמי token AI | התקדמות, לוגים, משוב בזמן אמת |

### הבדלים עיקריים שנצפו

בנוסף, הנה כמה הבדלים עיקריים:

- **תבנית תקשורת:**
  - הזרמת HTTP קלאסית: משתמשת בהעברת נתונים מקוטעת פשוטה לשליחת נתונים בחתיכות
  - הזרמת MCP: משתמשת במערכת התראות מובנית עם פרוטוקול JSON-RPC

- **פורמט הודעה:**
  - HTTP קלאסי: חתיכות טקסט פשוט עם שורות חדשות
  - MCP: אובייקטים מובנים מסוג LoggingMessageNotification עם מטא-נתונים

- **מימוש לקוח:**
  - HTTP קלאסי: לקוח פשוט שעובד עם תגובות הזרמה
  - MCP: לקוח משוכלל יותר עם מטפל בהודעות לעיבוד סוגי הודעות שונים

- **עדכוני התקדמות:**
  - HTTP קלאסי: ההתקדמות היא חלק מזרם התגובה הראשי
  - MCP: ההתקדמות נשלחת באמצעות הודעות התראה נפרדות בעוד שהתגובה הראשית מגיעה בסוף

### המלצות

יש כמה דברים שאנו ממליצים עליהם כשמדובר בבחירה בין מימוש הזרמה קלאסית (כנקודת קצה שהראינו לעיל באמצעות `/stream`) לבין בחירת הזרמה דרך MCP.

- **לצרכים הפשוטים של הזרמה:** הזרמת HTTP קלאסית פשוטה יותר למימוש ומספיקה לצרכי הזרמה בסיסיים.

- **ליישומים מורכבים ואינטראקטיביים:** הזרמת MCP מספקת גישה מובנית יותר עם מטא-נתונים עשירים והפרדה בין התראות לתוצאות סופיות.

- **ליישומי בינה מלאכותית:** מערכת ההתראות של MCP שימושית במיוחד למשימות AI ארוכות טווח שבהן רוצים לעדכן את המשתמשים בהתקדמות.

## הזרמה ב-MCP

טוב, אז ראיתם כמה המלצות והשוואות בנוגע להבדלים בין הזרמה קלאסית להזרמה ב-MCP. בואו ניכנס לפרטים כיצד ניתן לנצל הזרמה ב-MCP.

הבנת אופן פעולת ההזרמה במסגרת MCP חיונית לבניית יישומים רספונסיביים שמספקים משוב בזמן אמת למשתמשים במהלך פעולות ארוכות.

ב-MCP, הזרמה היא לא על שליחת התגובה הראשית בקטעים, אלא על שליחת **התראות** ללקוח בזמן שהכלי מעבד בקשה. התראות אלו יכולות לכלול עדכוני התקדמות, לוגים או אירועים אחרים.

### איך זה עובד

התוצאה הראשית עדיין נשלחת כהודעה יחידה. עם זאת, התראות יכולות להישלח כהודעות נפרדות במהלך העיבוד ועדכונים ללקוח בזמן אמת. הלקוח חייב להיות מסוגל לטפל ולהציג התראות אלו.

### תרגיל אופציונלי: התחבר לשרת MCP מתארח

ניתן גם להשתמש ב-Streamable HTTP מבלי להריץ שרת מקומי. דוגמה זו
מתחברת ל-[Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
מבררת את הכלים שלו, ומחפשת תיעוד MCP ציבורי באמצעות אותה
חבילת SDK של Python כמו [הלקוח המקומי](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

נקודת הקצה האנונימית של Parallel אינה דורשת חשבון או מפתח API. הגישה החינמית מוגבלת בקצב. הרצת סקריפט זה שולחת את שאילתות החיפוש, המטרה, ומזהה סשן אקראי ל-Parallel. השירות מציע גם `web_fetch`,
ששולח את כתובות ה-URL המבוקשות וכל הקשר שנמסר ל-Parallel. השתמש במידע ציבורי לתרגיל זה; עיין ב[תנאים](https://parallel.ai/customer-terms)
ו[מדיניות פרטיות](https://parallel.ai/privacy-policy).

עם Python 3.10 ומעלה וסביבה וירטואלית פעילה, התקן את ה-SDK:


עם Python 3.10 או חדש יותר וסביבת עבודה וירטואלית מופעלת, התקן את ה-SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

שמור את זה כ-`hosted_search.py` והפעל את `python hosted_search.py`:

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

צפה שגילוי יכלול את `web_search` ו-`web_fetch`, ואחריו תגובת חיפוש
המכילה כתובות מקור ומקטעים. התוצאות עשויות להשתנות או להיות ריקות.
הסקריפט בודק את `isError` כי כלי עלול להיכשל גם כשבקשת HTTP
מצליחה. אם הגישה מוגבלת מבחינת קצב, המתן לפני ניסיון נוסף. השתמש שוב באותו
`session_id` אם אתה מרחיב את הסקריפט עם קריאות חיפוש או שליפה קשורות.

HTTP מסוג Streamable מאפשר תגובות JSON ו-SSE; שרת זה יכול להחזיר
תוצאת JSON מלאה ללא התראות התקדמות. ה-SDK מנהל את
ההובלה. המשך עם הדוגמה המקומית מטה כדי ללמוד על התראות.
סקריפט אופציונלי זה מבצע חיפוש מובהק אחד וסוגר את החיבור שלו כאשר
הוא מסתיים. אם בעתיד תחשוף כלים אלה לסוכן, הסוכן עלול להפעיל
אותם במהלך עבודתו; טפל בטקסט מהרשת שנשלף כנתונים בלתי מהימנים.

## מהי התראה?

אמרנו "התראה", מה המשמעות שלה בהקשר של MCP?

התראה היא הודעת JSON-RPC שאין לה `id` ואינה
מקבלת תגובה. MCP משתמש בהתראות להתקדמות, ביטול, ו-
אירועים חד-כיווניים אחרים.

ב-MCP `2025-11-25`, לקוח שולח את `notifications/initialized` לאחר
לחיצת היד הראשונית. ב-MCP `2026-07-28` אין לחיצת יד ראשונית, כך
שהתראה זו היא התנהגות ישנה.

התראה נראית כך כהודעת JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

רישום הוא תכונה המשתמשת בהתראות; בהתראות עצמן הן
סוג כללי של הודעת JSON-RPC.

> **הוסרה ב-MCP `2026-07-28`:** תכונת הרישום נשארת זמינה
> לתאימות אך עשויה להילקח בהסרה בתיקון המפרט הראשון
> שיופץ בתאריך או לאחר 28 ביולי 2027. יישומים חדשים צריכים להשתמש
> ב-`stderr` עם stdio או OpenTelemetry לתצפית מובנית.

עבור יישום ישן של `2025-11-25`, השרת מאפשר את תכונת הרישום
כך:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> בהתאם ל-SDK שבו משתמשים, ייתכן שהרישום יופעל כברירת מחדל, או שתצטרכו להפעילו במפורש בקונפיגורציית השרת שלכם.

ישנם סוגים שונים של התראות:

| Level     | Description                    | Example Use Case                |
|-----------|-------------------------------|---------------------------------|
| debug     | מידע מפורט לניפוי שגיאות      | נקודות כניסה/יציאה מפונקציה    |
| info      | הודעות מידע כלליות            | עדכוני התקדמות תהליך            |
| notice    | אירועים רגילים אך משמעותיים  | שינויים בקונפיגורציה           |
| warning   | תנאי אזהרה                   | שימוש בתכונה מיושנת             |
| error     | תנאי שגיאה                   | כישלונות בתהליך                |
| critical  | תנאים קריטיים                | כשל במרכיב מערכת                |
| alert     | יש לנקוט פעולה מיידית         | זיהוי קורפגע/שחיתות בנתונים   |
| emergency | המערכת אינה תקינה             | כשלון מוחלט של המערכת           |

## יישום התראות ב-MCP

כדי ליישם התראות ב-MCP, יש להגדיר גם את צד השרת וגם את צד הלקוח כדי לטפל בעדכונים בזמן אמת. זה מאפשר לאפליקציה שלך לספק משוב מיידי למשתמשים במהלך פעולות ממושכות.

### צד שרת: שליחת התראות

נתחיל מצד השרת. ב-MCP, מגדירים כלים שיכולים לשלוח התראות בזמן עיבוד בקשות. השרת משתמש באובייקט ההקשר (בדרך כלל `ctx`) כדי לשלוח הודעות ללקוח.

#### פייתון

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

בדוגמה הקודמת, הכלי `process_files` שולח שלוש התראות ללקוח בזמן שהוא מעבד כל קובץ. שיטת `ctx.info()` משמשת לשליחת הודעות מידע.

בנוסף, כדי לאפשר התראות, ודא שהשרת שלך משתמש בטרנספורט של סטרימינג (כמו `streamable-http`) ושהלקוח מיישם מטפל בהודעות לעיבוד ההתראות. כך תוכל להגדיר את השרת להשתמש בטרנספורט `streamable-http`:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

בדוגמת ה-.NET הזו, הכלי `ProcessFiles` מוזהה עם התכונה `Tool` ושולח שלוש התראות ללקוח בזמן שהוא מעבד כל קובץ. שיטת `ctx.Info()` משמשת לשליחת הודעות מידע.

כדי לאפשר התראות בשרת MCP שלך מבוסס .NET, ודא שאתה משתמש בטרנספורט סטרימינג:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### צד לקוח: קבלת התראות

הלקוח חייב ליישם מטפל בהודעות כדי לעבד ולתצוג התראות כשהן מגיעות.

#### פייתון

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

בקוד שלעיל, הפונקציה `message_handler` בודקת אם ההודעה הנכנסת היא הודעת התראה. אם כן, היא מדפיסה את ההתראה; אחרת, היא מעבדת אותה כהודעה רגילה מהשרת. שימו לב גם איך ה-`ClientSession` מאותחל עם ה-`message_handler` לטיפול בהתראות נכנסות.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

בדוגמה זו ב-.NET, הפונקציה `MessageHandler` בודקת אם ההודעה הנכנסת היא הודעת התראה. אם כן, היא מדפיסה את ההתראה; אחרת, היא מעבדת אותה כהודעה רגילה מהשרת. ה-`ClientSession` מאותחל עם המטפל בהודעות דרך ה-`ClientSessionOptions`.

כדי לאפשר התראות, ודא שהשרת שלך משתמש ב-transport סטרימינג (כמו `streamable-http`) ושהלקוח שלך מממש מטפל הודעות לעיבוד ההתראות.

## התראות התקדמות ותסריטים

חלק זה מסביר את המושג של התראות התקדמות ב-MCP, מדוע הן חשובות, ואיך לממש אותן באמצעות HTTP סטרימינג. תמצא גם משימה מעשית להעמקת ההבנה שלך.

התראות התקדמות הן הודעות בזמן אמת שנשלחות מהשרת ללקוח במהלך פעולות ארוכות. במקום להמתין לסיום התהליך כולו, השרת מעדכן את הלקוח על המצב הנוכחי. זה משפר שקיפות, חווית משתמש, ומקל על איתור ותיקון תקלות.

**דוגמה:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### למה להשתמש בהתראות התקדמות?

התראות התקדמות חיוניות מכמה סיבות:

- **חוויית משתמש טובה יותר:** המשתמשים רואים עדכונים כשהעבודה מתקדמת, לא רק בסוף.
- **משוב בזמן אמת:** הלקוחות יכולים להציג פסי התקדמות או יומני פעולות, מה שמעניק תחושה של תגובתיות לאפליקציה.
- **איתור תקלות וניטור קלים יותר:** מפתחים ומשתמשים יכולים לראות איפה תהליך עשוי להאט או להיתקע.

### איך לממש התראות התקדמות

כך ניתן לממש התראות התקדמות ב-MCP:

- **בשרת:** השתמש ב-`ctx.info()` או `ctx.log()` לשלוח התראות בעת עיבוד כל פריט. זה שולח הודעה ללקוח לפני שהתוצאה העיקרית מוכנה.
- **בלקוח:** מימוש מטפל הודעות שמאזין ומציג התראות בזמן שהן מתקבלות. מטפל זה מבדיל בין התראות לתוצאה הסופית.

**דוגמה לשרת:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**דוגמה ללקוח:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## שיקולי אבטחה

אבטחה צריכה להיות בעדיפות עליונה כשמממשים כל שרת, ובפרט כאשר משתמשים ב-HTTP סטרימינג כמו Streamable HTTP ב-MCP.

כאשר מממשים שרתי MCP עם העברות מבוססות HTTP, האבטחה הופכת להיות נושא חשוב ביותר שדורש תשומת לב קפדנית לליקויי אבטחה ומנגנוני הגנה.

### סקירה כללית

אבטחה היא קריטית כאשר חושפים שרתי MCP דרך HTTP. Streamable HTTP מציג משטחי תקיפה חדשים ודורש תצורה זהירה.

הנה כמה שיקולי אבטחה מרכזיים:

- **אימות כותרת Origin**: תמיד לאמת את כותרת ה-`Origin` כדי למנוע התקפות DNS rebinding.
- **הקשירת localhost**: לפיתוח מקומי, קשר את השרתים ל-`localhost` כדי למנוע חשיפה לאינטרנט הציבורי.
- **אימות**: מימוש אימות (למשל, מפתחות API, OAuth) לפריסות בסביבה חיה.
- **CORS**: הגדר מדיניות שיתוף משאבים חוצי מקור (CORS) להגבלת גישה.
- **HTTPS**: השתמש ב-HTTPS בסביבה חיה להצפנת תעבורה.

### שיטות עבודה מומלצות

בנוסף, הנה כמה שיטות עבודה מומלצות ליישום אבטחה בשרת סטרימינג MCP שלך:

- אל תסמוך על בקשות נכנסות ללא אימות.
- נהל ופקח על כל הגישה והשגיאות.
- עדכן תלויות בצורה שוטפת לתיקון פגיעויות אבטחה.

### אתגרים

תתמודד עם אתגרים ביישום אבטחה בשרת סטרימינג MCP:

- איזון בין אבטחה לנוחות פיתוח
- הבטחת תאימות עם סביבות לקוח שונות


## שדרוג מ-SSE ל-Streamable HTTP

לאפליקציות שמשתמשות כעת ב-Server-Sent Events (SSE), מעבר ל-Streamable HTTP מספק יכולות משופרות ותחזוקה טובה יותר בטווח הארוך עבור יישומי MCP שלך.

### למה לשדרג?

יש שתי סיבות משכנעות לשדרג מ-SSE ל-Streamable HTTP:

- Streamable HTTP מציע קנה מידה טוב יותר, תאימות ותמיכה עשירה יותר בהתראות מאשר SSE.
- זהו ה-transport המומלץ לאפליקציות MCP חדשות.

### שלבי המיגרציה

כך ניתן לבצע מיגרציה מ-SSE ל-Streamable HTTP באפליקציות MCP שלך:

- **עדכן קוד שרת** לשימוש ב-`transport="streamable-http"` ב-`mcp.run()`.
- **עדכן קוד לקוח** לשימוש ב-`streamablehttp_client` במקום SSE client.
- **ממש מטפל הודעות** בלקוח לעיבוד התראות.
- **בדוק תאימות** עם כלים וזרימות עבודה קיימות.

### שמירת תאימות

מומלץ לשמור על תאימות עם לקוחות SSE קיימים במהלך תהליך המיגרציה. הנה כמה אסטרטגיות:

- אפשר לתמוך בשני SSE ו-Streamable HTTP על ידי הפעלת שני ה-transports בנקודות קצה שונות.
- העבר לקוחות בהדרגה ל-transport החדש.

### אתגרים

וודא שאתה מתמודד עם האתגרים הבאים במהלך המיגרציה:

- עדכון כל הלקוחות
- טיפול בהבדלים באספקת ההתראות

### משימה: בנה אפליקציית סטרימינג MCP משלך

**תסריט:**
בנה שרת ולקוח MCP שבו השרת מעבד רשימת פריטים (למשל, קבצים או מסמכים) ושולח התראה על כל פריט שעובד. הלקוח יציג כל התראה כשהיא מתקבלת.

**שלבים:**

1. מימוש כלי שרת שמעבד רשימה ושולח התראות על כל פריט.
2. מימוש לקוח עם מטפל הודעות להצגת ההתראות בזמן אמת.
3. בדוק את היישום שלך על ידי הרצת השרת והלקוח וצפה בהתראות.

[פתרון](./solution/README.md)

## קריאה נוספת ומה הלאה?

כדי להמשיך במסע שלך עם סטרימינג MCP ולהרחיב את הידע שלך, חלק זה מספק משאבים נוספים ושלבי המשך מומלצים לבניית אפליקציות מתקדמות יותר.

### קריאה נוספת

- [Microsoft: מבוא ל-HTTP סטרימינג](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ב-ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: בקשות סטרימינג](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### מה הלאה?

- נסה לבנות כלים מתקדמים יותר ל-MCP שמשתמשים בסטרימינג לאנליטיקה בזמן אמת, צ'אט או עריכה שיתופית.
- חקור אינטגרציה של סטרימינג MCP עם מסגרות frontend (React, Vue וכו') לעדכוני UI חיים.
- הבא: [שימוש ב-Microsoft Foundry Toolkit עבור Visual Studio Code](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->