# סטרימינג דרך HTTPS עם פרוטוקול הקשר דגם (MCP)

פרק זה מספק מדריך מקיף ליישום סטרימינג מאובטח, ניתן להרחבה ובזמן אמת באמצעות פרוטוקול הקשר דגם (MCP) באמצעות HTTPS. הוא מכסה את המוטיבציה לסטרימינג, מנגנוני ההעברה הזמינים, איך ליישם HTTP סטרימינג ב-MCP, פרקטיקות אבטחה, מעבר מ-SSE והנחיות מעשיות לבניית אפליקציות סטרימינג MCP משלך.

> **מבט קדימה:** שיעור זה מתאר את Streamable HTTP תחת **מפרט MCP 2025-11-25**, שבו מושב מוקם במהלך ה־`initialize` ומקובע עם כותרת `Mcp-Session-Id`. מועמד השחרור '2026-07-28' מסיר לחלוטין את יצירת החיבור וזיהוי המושב, מה שהופך כל בקשה לעצמאית וניתנת לכיוון לכל מופע שרת ללא מושבים מלוכדים. עיין ב-[מה משתנה ב-MCP: מועמד השחרור 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) לפרטים.

## מנגנוני העברה וסטרימינג ב-MCP

חלק זה בוחן את מנגנוני ההעברה השונים הזמינים ב-MCP ואת תפקידם בהפעלת יכולות סטרימינג לתקשורת בזמן אמת בין לקוחות לשרתים.

### מהו מנגנון העברה?

מנגנון העברה מגדיר כיצד הנתונים מוחלפים בין הלקוח לשרת. MCP תומך בסוגי העברה רבים להתאים לסביבות וצרכים שונים:

- **stdio**: קלט/פלט סטנדרטי, מתאים לכלים מקומיים ומבוססי פקודה. פשוט אך לא מתאים לאינטרנט או ענן.
- **SSE (Server-Sent Events)**: מאפשר לשרתים לדחוף עדכוני זמן אמת ללקוחות דרך HTTP. טוב לממשקי ווב, אך מוגבל בסקלביליות ובגמישות. בהתאם למפרט MCP 2025-06-18, מנגנון SSE הייעודי הוחלף ב-"Streamable HTTP".
- **Streamable HTTP**: מנגנון סטרימינג מודרני מבוסס HTTP, תומך בהתראות וסקלביליות טובה יותר. מומלץ לרוב תרחישי ייצור וענן.

### טבלת השוואה

עיין בטבלת ההשוואה למטה להבנת ההבדלים בין מנגנוני ההעברה הללו:

| העברה           | עדכוני זמן אמת  | סטרימינג | סקלביליות | מקרה שימוש             |
|-----------------|-----------------|-----------|------------|-------------------------|
| stdio           | לא              | לא        | נמוכה     | כלים מקומיים ב-CLI     |
| SSE             | כן              | כן        | בינונית  | ווב, עדכונים בזמן אמת |
| Streamable HTTP | כן              | כן        | גבוהה     | ענן, ריבוי לקוחות      |

> **טיפ:** הבחירה במנגנון ההעברה הנכון משפיעה על ביצועים, סקלביליות וחוויית משתמש. **Streamable HTTP** מומלץ לאפליקציות מודרניות, להרחבה ולענן.

שים לב לסטדיואו ול-SSE שהוצגו בפרקים הקודמים ואיך Streamable HTTP הוא המנגנון שמטופל בפרק זה.

## סטרימינג: מושגים ומוטיבציה

הבנת מושגי היסוד והמניעים מאחורי סטרימינג חיונית ליישום מערכות תקשורת בזמן אמת יעילות.

**סטרימינג** היא טכניקה בתכנות רשת שמאפשרת לשלוח ולקבל נתונים בחתיכות קטנות, ניתנות לניהולה, או כרצף אירועים, במקום להמתין לתגובה מלאה לפני שמתחילים לעבד. זה שימושי במיוחד ב:

- קבצים או מערכי נתונים גדולים.
- עדכוני זמן אמת (למשל, צ'אט, פסי התקדמות).
- חישובים ארוכי טווח שבהם רוצים ליידע את המשתמש.

הנה מה שצריך לדעת על סטרימינג ברמה גבוהה:

- הנתונים מועברים בהדרגה, לא בבת אחת.
- הלקוח יכול לעבד נתונים כשהם מגיעים.
- מפחית תחושת עיכוב ומשפר חוויית משתמש.

### למה להשתמש בסטרימינג?

הסיבות לשימוש בסטרימינג הן:

- המשתמשים מקבלים משוב מידי, לא רק בסוף
- מאפשר אפליקציות בזמן אמת וממשקים תגובתיים
- שימוש יעיל יותר במשאבי רשת ומחשוב

### דוגמה פשוטה: שרת ולקוח סטרימינג HTTP

הנה דוגמה פשוטה לאופן בו ניתן ליישם סטרימינג:

#### פייתון

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

**איך זה פועל:**

- השרת מייצר כל הודעה כשהיא מוכנה.
- הלקוח מקבל ומדפיס כל חלק כשהוא מגיע.

**דרישות:**

- השרת חייב להשתמש בתגובה סטרימינג (למשל `StreamingResponse` ב-FastAPI).
- הלקוח חייב לעבד את התגובה כסטרימינג (`stream=True` ב-requests).
- סוג התוכן בדרך כלל `text/event-stream` או `application/octet-stream`.

#### ג'אווה

**שרת (Java, משתמש ב-Spring Boot וב-Server-Sent Events):**

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

**הערות לביצוע בג'אווה:**

- משתמש בסטאק ריאקטיבי של Spring Boot עם `Flux` לסטרימינג
- `ServerSentEvent` מספק סטרימינג מבני עם סוגי אירועים
- `WebClient` עם `bodyToFlux()` מאפשר צריכת סטרימינג ריאקטיבית
- `delayElements()` מדמה זמן עיבוד בין אירועים
- לאירועים יש סוגים (`info`, `result`) לטיפול טוב יותר בלקוח

### השוואה: סטרימינג קלאסי מול סטרימינג ב-MCP

ההבדלים בין האופן בו סטרימינג עובד ב"אופן קלאסי" לבין ב-MCP ניתנים להצגה כך:

| תכונה                   | סטרימינג HTTP קלאסי          | סטרימינג MCP (התראות)           |
|-------------------------|------------------------------|----------------------------------|
| תגובה ראשית             | מפוצלת לחלקים               | בודדת, בסוף                    |
| עדכוני התקדמות          | נשלחים כחלקי נתונים          | נשלחים כהודעות התראה           |
| דרישות לקוח             | חייב לעבד סטרימינג          | חייב לממש מנהל הודעות           |
| מקרה שימוש              | קבצים גדולים, סטרימי טוקנים | התקדמות, לוגים, משוב בזמן אמת |

### הבדלים מרכזיים שנתגלו

בנוסף, הנה כמה הבדלים מרכזיים:

- **תבנית תקשורת:**
  - סטרימינג HTTP קלאסי: משתמש בקידוד משלוח בחתיכות פשוט לשליחת נתונים בחלקים
  - סטרימינג MCP: משתמש במערכת התראות מובנית עם פרוטוקול JSON-RPC

- **פורמט ההודעה:**
  - HTTP קלאסי: חתיכות טקסט פשוט עם שורות חדשות
  - MCP: אובייקטים Structured LoggingMessageNotification עם מטה-דאטה

- **מימוש לקוח:**
  - HTTP קלאסי: לקוח פשוט שמעבד תגובות סטרימינג
  - MCP: לקוח מתוחכם יותר עם מנהל הודעות לעיבוד סוגי הודעות שונים

- **עדכוני התקדמות:**
  - HTTP קלאסי: ההתקדמות היא חלק מזרם התגובה הראשי
  - MCP: ההתקדמות נשלחת כהודעות התראה נפרדות בזמן שהתגובה הראשית מגיעה בסוף

### המלצות

ישנם דברים שאנו ממליצים כשמדובר בבחירה בין יישום סטרימינג קלאסי (כפי שהראינו למעלה עם /stream) לבין סטרימינג דרך MCP.

- **לצרכי סטרימינג פשוטים:** סטרימינג HTTP קלאסי פשוט יותר ליישום ומספיק לצרכים בסיסיים.

- **לאפליקציות מורכבות ואינטראקטיביות:** סטרימינג MCP מספק גישה מובנית יותר עם מטא-דאטה עשיר והפרדה בין התראות לתוצאות סופיות.

- **לאפליקציות בינה מלאכותית:** מערכת ההתראות של MCP שימושית במיוחד למשימות בינה מלאכותית ארוכות טווח שבהן רוצים ליידע את המשתמשים על ההתקדמות.

## סטרימינג ב-MCP

טוב, ראיתם כבר כמה המלצות והשוואות עד כה על ההבדל בין סטרימינג קלאסי לסטרימינג ב-MCP. בואו נבחן בפירוט איך אפשר למנף סטרימינג ב-MCP.

הבנת אופן פעולת הסטרימינג במסגרת MCP הכרחית לבניית אפליקציות תגובתיות שמספקות משוב בזמן אמת למשתמשים בעת פעולות ארוכות טווח.

ב-MCP, סטרימינג איננו לשלוח את התגובה הראשית בחלקים, אלא לשלוח **התראות** ללקוח בזמן שהכלי מעבד בקשה. התראות אלו יכולות לכלול עדכוני התקדמות, לוגים או אירועים אחרים.

### איך זה עובד

התוצאה הראשית עדיין נשלחת כתשובה בודדת. עם זאת, התראות יכולות להישלח כהודעות נפרדות במהלך העיבוד וכך לעדכן את הלקוח בזמן אמת. הלקוח חייב להיות מסוגל לטפל ולהציג התראות אלו.

## מהי התראה?

אמרנו "התראה", מה זה אומר בהקשר של MCP?

התראה היא הודעה שנשלחת מהשרת ללקוח כדי ליידע על התקדמות, מצב או אירועים אחרים במהלך פעולה ארוכת טווח. התראות משפרות שקיפות וחוויית משתמש.

למשל, הלקוח אמור לשלוח התראה כאשר ההאב הראשוני עם השרת הושלם.

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

התראות משתייכות לנושא ב-MCP הנקרא ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **הודעת הפסקת שימוש:** מועמד השחרור למפרט MCP `2026-07-28` מסמן את אובייקט ה-Logging כמיושן לטובת `stderr` עבור העברות stdio ו-OpenTelemetry לצפיית מבנה. Logging ממשיך לפעול ב-`2025-11-25` ולפחות שנה אחרי כל הפסקה רשמית. ראו [מה משתנה ב-MCP: מועמד השחרור 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

כדי לגרום ללוגינג לפעול, השרת צריך לאפשר אותו כתכונה/יכולת כך:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> בהתאם ל-SDK שבה משתמשים, ייתכן שהלוגינג מופעל כברירת מחדל, או שתצטרך להפעילו במפורש בקונפיגורציית השרת שלך.

ישנם סוגי התראות שונים:

| רמה       | תיאור                        | דוגמת שימוש                   |
|-----------|------------------------------|-------------------------------|
| debug     | מידע מפורט לבדיקת שגיאות   | נקודות כניסה/יציאה מפונקציה  |
| info      | הודעות כלליות לעדכון       | עדכוני התקדמות בפעולה        |
| notice    | אירועים רגילים אך חשובים    | שינויים בקונפיגורציה          |
| warning   | תנאי אזהרה                  | שימוש בתכונות מיושנות         |
| error     | תנאי שגיאה                 | כישלונות בפעולה              |
| critical  | תנאי קריטי                 | כשל במרכיבי מערכת             |
| alert     | דרושה פעולה מיידית         | זיהוי שיבוש נתונים           |
| emergency | מערכת לא שמישה           | כשל מערכת מלא                |

## יישום התראות ב-MCP

כדי ליישם התראות ב-MCP, יש להגדיר את שני הצדדים — השרת והלקוח — לטפל בעדכונים בזמן אמת. זה מאפשר לאפליקציה שלך לספק משוב מיידי למשתמשים במהלך פעולות ארוכות טווח.

### צד שרת: שליחת התראות

נתחיל מצד השרת. ב-MCP, מגדירים כלים שיכולים לשלוח התראות בעת עיבוד בקשות. השרת משתמש באובייקט ההקשר (בדרך כלל `ctx`) כדי לשלוח הודעות ללקוח.

#### פייתון

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

בדוגמה הקודמת, הכלי `process_files` שולח שלוש התראות ללקוח כאשר הוא מעבד כל קובץ. השיטה `ctx.info()` משמשת לשליחת הודעות מידע.

בנוסף, כדי לאפשר התראות, וודא שהשרת שלך משתמש בהעברה סטרימינג (כמו `streamable-http`) ושהלקוח מממש מנהל הודעות לעיבוד התראות. הנה איך להגדיר את השרת להשתמש בהעברה `streamable-http`:

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

בדוגמת .NET זו, הכלי `ProcessFiles` מסומן עם התכונה `Tool` ושולח שלוש התראות ללקוח בעת עיבוד כל קובץ. השיטה `ctx.Info()` משמשת לשליחת הודעות מידע.

כדי לאפשר התראות בשרת MCP שלך ב-.NET, ודא שאתה משתמש בהעברה סטרימינג:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### צד לקוח: קבלת התראות

הלקוח חייב לממש מנהל הודעות לעיבוד והצגת התראות כשהן מגיעות.

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

בקוד הקודם, הפונקציה `message_handler` בודקת אם ההודעה הנכנסת היא התראה. אם כן, היא מדפיסה את ההתראה; אחרת, היא מעבדת אותה כהודעת שרת רגילה. שים לב כיצד `ClientSession` מאותחל עם `message_handler` לטיפול בהתראות נכנסות.

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

בדוגמת .NET זו, הפונקציה `MessageHandler` בודקת אם ההודעה הנכנסת היא התראה. אם כן, היא מדפיסה את ההתראה; אחרת, היא מעבדת אותה כהודעת שרת רגילה. `ClientSession` מאותחל עם מנהל ההודעות דרך `ClientSessionOptions`.

כדי לאפשר התראות, ודא שהשרת שלך משתמש בהעברה סטרימינג (כמו `streamable-http`) ושהלקוח מממש מנהל הודעות לעיבוד התראות.

## התראות התקדמות & תרחישים

חלק זה מסביר את מושג התראות ההתקדמות ב-MCP, מדוע הן חשובות, ואיך ליישמן באמצעות Streamable HTTP. תמצא גם תרגיל מעשי לחיזוק ההבנה.

התראות התקדמות הן הודעות בזמן אמת שנשלחות מהשרת ללקוח במהלך פעולות ארוכות טווח. במקום להמתין לסיום כל התהליך, השרת מעדכן את הלקוח על המצב הנוכחי. זה משפר שקיפות, חוויית משתמש והופך את התהליך לנוח יותר לניפוי באגים.

**דוגמה:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### למה להשתמש בהתראות התקדמות?

התראות התקדמות חיוניות ממספר סיבות:

- **חוויית משתמש טובה יותר:** המשתמשים רואים עדכונים כשהעבודה מתקדמת, לא רק בסיום.
- **משוב בזמן אמת:** הלקוחות יכולים להראות פסי התקדמות או לוגים, מה שהופך את האפליקציה לתגובתית.
- **קל לניפוי באגים ולניטור:** מפתחים ומשתמשים יכולים לראות איפה התהליך איטי או תקוע.

### איך ליישם התראות התקדמות

הנה איך ניתן ליישם התראות התקדמות ב-MCP:

- **בשרת:** השתמש ב-`ctx.info()` או `ctx.log()` לשליחת התראות בזמן עיבוד כל פריט. זה שולח הודעה ללקוח לפני שהתוצאה הראשית מוכנה.
- **בלקוח:** מימוש מנהל הודעות שמאזין ומציג התראות כשהן מגיעות. המנהל מבדיל בין התראות לתוצאה הסופית.

**דוגמת שרת:**


#### פייתון

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**דוגמה ללקוח:**

#### פייתון

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## שיקולי אבטחה

אבטחה צריכה להיות בעדיפות עליונה בעת יישום כל שרת, במיוחד בעת שימוש בהעברות מבוססות HTTP כמו Streamable HTTP ב-MCP.

כאשר מיישמים שרתי MCP עם העברות מבוססות HTTP, האבטחה הופכת לדאגה מרכזית שדורשת תשומת לב קפדנית לווקטורי התקפה שונים ומנגנוני הגנה.

### סקירה כללית

אבטחה היא קריטית כאשר חושפים שרתי MCP באמצעות HTTP. Streamable HTTP מציג משטחי תקיפה חדשים ודורש תצורה זהירה.

הנה כמה שיקולי אבטחה מרכזיים:

- **אימות כותרת מקור (Origin)**: תמיד לאמת את כותרת ה-Origin כדי למנוע התקפות של DNS Rebiding.
- **קשירת localhost**: לפיתוח מקומי, לקשר שרתים ל-localhost כדי למנוע חשיפה לאינטרנט הציבורי.
- **אימות**: ליישם אימות (כמו מפתחות API, OAuth) במערכות פרודקשן.
- **CORS**: להגדיר מדיניות שיתוף משאבים בין מקורות (CORS) להגבלת גישה.
- **HTTPS**: להשתמש ב-HTTPS בפרודקשן להצפנת התעבורה.

### שיטות מומלצות

בנוסף, הנה כמה שיטות מיטביות שיש לעקוב אחריהן בעת יישום אבטחה בשרת סטרימינג MCP:

- לעולם לא לסמוך לבקשות נכנסות ללא אימות.
- לתעד ולנטר את כל הגישות והטעויות.
- לעדכן באופן קבוע תלויות כדי לתקן פרצות אבטחה.

### אתגרים

תשיגו מספר אתגרים ביישום אבטחה בשרתי סטרימינג MCP:

- איזון בין אבטחה לנוחות הפיתוח
- הבטחת תאימות עם סביבות לקוח שונות


## שדרוג מ-SSE ל-Streamable HTTP

עבור אפליקציות המשתמשות כעת ב-Server-Sent Events (SSE), המעבר ל-Streamable HTTP מספק יכולות משופרות וקיימות טובה יותר לטווח הארוך ביישומי MCP.

### למה לשדרג?

ישנם שני סיבות משכנעות לשדרוג מ-SSE ל-Streamable HTTP:

- Streamable HTTP מציע סקלביליות טובה יותר, תאימות, ותמיכה עשירה יותר בהתראות מאשר SSE.
- זוהי העברה מומלצת לאפליקציות MCP חדשות.

### שלבי ההגירה

כך תוכלו להגר מ-SSE ל-Streamable HTTP באפליקציות MCP שלכם:

- **עדכון קוד השרת** לשימוש ב-`transport="streamable-http"` ב-`mcp.run()`.
- **עדכון קוד הלקוח** לשימוש ב-`streamablehttp_client` במקום לקוח SSE.
- **יישום מנהל הודעות** בלקוח לעיבוד התראות.
- **בדיקה לתאימות** עם כלים וזרימות עבודה קיימות.

### שמירת תאימות

מומלץ לשמור על תאימות עם לקוחות SSE קיימים במהלך תהליך ההגירה. הנה כמה אסטרטגיות:

- ניתן לתמוך בשני SSE ו-Streamable HTTP על ידי הפעלת שתי ההעברות בנקודות קצה שונות.
- להגר בהדרגה את הלקוחות להמרה החדשה.

### אתגרים

יש לטפל באתגרים הבאים במהלך ההגירה:

- הבטחת עדכון כל הלקוחות
- טיפול בהבדלים בהעברת ההודעות

### משימה: צרו אפליקציית סטרימינג MCP משלכם

**תרחיש:**
צרו שרת ולקוח MCP כאשר השרת מעבד רשימת פריטים (למשל, קבצים או מסמכים) ושולח התראה על כל פריט המעובד. הלקוח יציג כל התראה בעת הגעתה.

**שלבים:**

1. יש ליישם כלי שרת שמעבד רשימה ושולח התראות עבור כל פריט.
2. יש ליישם לקוח עם מנהל הודעות להצגת התראות בזמן אמת.
3. לבדוק את היישום על ידי הרצת השרת והלקוח, ולצפות בהתראות.

[פתרון](./solution/README.md)

## קריאה נוספת ומה הלאה?

כדי להמשיך את דרככם עם סטרימינג MCP ולהרחיב את הידע שלכם, חלק זה מספק משאבים נוספים והצעות לשלבים הבאים בבניית יישומים מתקדמים יותר.

### קריאה נוספת

- [Microsoft: מבוא לסטרימינג HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ב-ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: בקשות סטרימינג](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### מה הלאה?

- נסו לבנות כלים מתקדמים יותר ל-MCP המשתמשים בסטרימינג לאנליטיקה בזמן אמת, צ'אט, או עריכה שיתופית.
- חקרו אינטגרציה של סטרימינג MCP עם מסגרות frontend (React, Vue וכו') לעדכוני ממשק משתמש חיים.
- הבא: [שימוש ב-AI Toolkit ל-VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->