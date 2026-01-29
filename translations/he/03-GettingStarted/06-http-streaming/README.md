# סטרימינג HTTPS עם פרוטוקול Model Context Protocol (MCP)

פרק זה מספק מדריך מקיף ליישום סטרימינג מאובטח, ניתן להרחבה ובזמן אמת עם פרוטוקול Model Context Protocol (MCP) באמצעות HTTPS. הוא מכסה את המוטיבציה לסטרימינג, מנגנוני התעבורה הזמינים, כיצד ליישם HTTP ניתן לסטרימינג ב-MCP, שיטות עבודה מומלצות לאבטחה, מעבר מ-SSE והנחיות מעשיות לבניית יישומי MCP סטרימינג משלכם.

## מנגנוני תעבורה וסטרימינג ב-MCP

סעיף זה בוחן את מנגנוני התעבורה השונים הזמינים ב-MCP ואת תפקידם באפשרות יכולות סטרימינג לתקשורת בזמן אמת בין לקוחות לשרתים.

### מהו מנגנון תעבורה?

מנגנון תעבורה מגדיר כיצד נתונים מוחלפים בין הלקוח לשרת. MCP תומך במספר סוגי תעבורה כדי להתאים לסביבות ודרישות שונות:

- **stdio**: קלט/פלט סטנדרטי, מתאים לכלים מקומיים ובסיסיים מבוססי CLI. פשוט אך לא מתאים לאינטרנט או לענן.
- **SSE (Server-Sent Events)**: מאפשר לשרתים לדחוף עדכונים בזמן אמת ללקוחות דרך HTTP. טוב לממשקי משתמש באינטרנט, אך מוגבל בהרחבה ובגמישות.
- **Streamable HTTP**: תעבורת סטרימינג מודרנית מבוססת HTTP, תומכת בהתראות ובהרחבה טובה יותר. מומלץ לרוב התרחישים בייצור ובענן.

### טבלת השוואה

עיינו בטבלת ההשוואה הבאה כדי להבין את ההבדלים בין מנגנוני התעבורה הללו:

| תעבורה            | עדכונים בזמן אמת | סטרימינג | הרחבה    | מקרה שימוש               |
|-------------------|------------------|-----------|----------|--------------------------|
| stdio             | לא               | לא        | נמוכה    | כלים מקומיים מבוססי CLI |
| SSE               | כן               | כן        | בינונית | אינטרנט, עדכונים בזמן אמת |
| Streamable HTTP   | כן               | כן        | גבוהה    | ענן, ריבוי לקוחות        |

> **טיפ:** בחירת התעבורה הנכונה משפיעה על הביצועים, ההרחבה וחוויית המשתמש. **Streamable HTTP** מומלץ ליישומים מודרניים, ניתנים להרחבה ומוכנים לענן.

שימו לב לתעבורות stdio ו-SSE שהוצגו בפרקים הקודמים וכיצד Streamable HTTP הוא התעבורה המכוסה בפרק זה.

## סטרימינג: מושגים ומוטיבציה

הבנת המושגים והמוטיבציה הבסיסיים מאחורי סטרימינג חיונית ליישום מערכות תקשורת בזמן אמת יעילות.

**סטרימינג** הוא טכניקה בתכנות רשת המאפשרת שליחת וקבלת נתונים במקטעים קטנים ונוחים או כרצף של אירועים, במקום להמתין לתגובה שלמה. זה שימושי במיוחד עבור:

- קבצים או מערכי נתונים גדולים.
- עדכונים בזמן אמת (לדוגמה, צ'אט, סרגלי התקדמות).
- חישובים ארוכי טווח שבהם רוצים לעדכן את המשתמש.

הנה מה שצריך לדעת על סטרימינג ברמה גבוהה:

- הנתונים נמסרים בהדרגה, לא בבת אחת.
- הלקוח יכול לעבד נתונים כשהם מגיעים.
- מפחית את זמן ההמתנה הנתפס ומשפר את חוויית המשתמש.

### למה להשתמש בסטרימינג?

הסיבות לשימוש בסטרימינג הן:

- המשתמשים מקבלים משוב מיידי, לא רק בסיום.
- מאפשר יישומים בזמן אמת וממשקי משתמש מגיבים.
- שימוש יעיל יותר במשאבי רשת וחישוב.

### דוגמה פשוטה: שרת ולקוח סטרימינג HTTP

הנה דוגמה פשוטה כיצד ניתן ליישם סטרימינג:

#### Python

**שרת (Python, באמצעות FastAPI ו-StreamingResponse):**

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

**לקוח (Python, באמצעות requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

דוגמה זו מדגימה שרת ששולח סדרת הודעות ללקוח כשהן זמינות, במקום להמתין שכל ההודעות יהיו מוכנות.

**כיצד זה עובד:**

- השרת מניב כל הודעה כשהיא מוכנה.
- הלקוח מקבל ומדפיס כל מקטע כשהוא מגיע.

**דרישות:**

- השרת חייב להשתמש בתגובה סטרימינג (לדוגמה, `StreamingResponse` ב-FastAPI).
- הלקוח חייב לעבד את התגובה כזרם (`stream=True` ב-requests).
- Content-Type הוא בדרך כלל `text/event-stream` או `application/octet-stream`.

#### Java

**שרת (Java, באמצעות Spring Boot ו-Server-Sent Events):**

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

**לקוח (Java, באמצעות Spring WebFlux WebClient):**

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

**הערות יישום ב-Java:**

- משתמש בסטאק הריאקטיבי של Spring Boot עם `Flux` לסטרימינג.
- `ServerSentEvent` מספק סטרימינג מובנה עם סוגי אירועים.
- `WebClient` עם `bodyToFlux()` מאפשר צריכת סטרימינג ריאקטיבית.
- `delayElements()` מדמה זמן עיבוד בין אירועים.
- אירועים יכולים לכלול סוגים (`info`, `result`) לניהול טוב יותר בצד הלקוח.

### השוואה: סטרימינג קלאסי מול סטרימינג ב-MCP

ההבדלים בין אופן הפעולה של סטרימינג "קלאסי" לבין MCP מוצגים כך:

| תכונה                | סטרימינג HTTP קלאסי         | סטרימינג MCP (התראות)         |
|----------------------|----------------------------|--------------------------------|
| תגובה עיקרית         | מחולקת למקטעים             | יחידה, בסיום                  |
| עדכוני התקדמות       | נשלחים כמקטעי נתונים       | נשלחים כהתראות                |
| דרישות לקוח          | חייב לעבד זרם              | חייב ליישם מנהל הודעות         |
| מקרה שימוש           | קבצים גדולים, זרמי AI      | התקדמות, לוגים, משוב בזמן אמת |

### הבדלים מרכזיים שנצפו

בנוסף, הנה כמה הבדלים מרכזיים:

- **תבנית תקשורת:**
  - סטרימינג HTTP קלאסי: משתמש בקידוד העברה מחולק פשוט לשליחת נתונים במקטעים.
  - סטרימינג MCP: משתמש במערכת התראות מובנית עם פרוטוקול JSON-RPC.

- **פורמט הודעה:**
  - HTTP קלאסי: מקטעי טקסט פשוטים עם שורות חדשות.
  - MCP: אובייקטים מובנים מסוג LoggingMessageNotification עם מטא-נתונים.

- **יישום לקוח:**
  - HTTP קלאסי: לקוח פשוט שמעבד תגובות סטרימינג.
  - MCP: לקוח מתוחכם יותר עם מנהל הודעות לעיבוד סוגי הודעות שונים.

- **עדכוני התקדמות:**
  - HTTP קלאסי: ההתקדמות היא חלק מזרם התגובה הראשי.
  - MCP: ההתקדמות נשלחת כהודעות התראה נפרדות בעוד התגובה הראשית מגיעה בסיום.

### המלצות

ישנם דברים שאנו ממליצים עליהם בבחירה בין יישום סטרימינג קלאסי (כמו נקודת הקצה שהראינו לכם לעיל באמצעות `/stream`) לבין בחירה בסטרימינג דרך MCP.

- **לצרכים פשוטים של סטרימינג:** סטרימינג HTTP קלאסי פשוט יותר ליישום ומספיק לצרכים בסיסיים.
- **ליישומים מורכבים ואינטראקטיביים:** סטרימינג MCP מספק גישה מובנית יותר עם מטא-נתונים עשירים והפרדה בין התראות לתוצאות סופיות.
- **ליישומי AI:** מערכת ההתראות של MCP שימושית במיוחד למשימות AI ארוכות טווח שבהן רוצים לעדכן משתמשים על התקדמות.

## סטרימינג ב-MCP

אוקיי, ראיתם כמה המלצות והשוואות עד כה על ההבדל בין סטרימינג קלאסי לסטרימינג ב-MCP. בואו ניכנס לפרטים כיצד תוכלו לנצל סטרימינג ב-MCP.

הבנת אופן הפעולה של סטרימינג במסגרת MCP חיונית לבניית יישומים מגיבים המספקים משוב בזמן אמת למשתמשים במהלך פעולות ארוכות טווח.

ב-MCP, סטרימינג אינו עוסק בשליחת התגובה הראשית במקטעים, אלא בשליחת **התראות** ללקוח בזמן שכלי מעבד בקשה. התראות אלו יכולות לכלול עדכוני התקדמות, לוגים או אירועים אחרים.

### כיצד זה עובד

התוצאה העיקרית עדיין נשלחת כתגובה יחידה. עם זאת, התראות יכולות להישלח כהודעות נפרדות במהלך העיבוד ובכך לעדכן את הלקוח בזמן אמת. הלקוח חייב להיות מסוגל לטפל ולהציג את ההתראות הללו.

## מהי התראה?

אמרנו "התראה", מה זה אומר בהקשר של MCP?

התראה היא הודעה שנשלחת מהשרת ללקוח כדי ליידע על התקדמות, סטטוס או אירועים אחרים במהלך פעולה ארוכת טווח. התראות משפרות שקיפות וחוויית משתמש.

לדוגמה, לקוח אמור לשלוח התראה לאחר ביצוע לחיצת יד ראשונית עם השרת.

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

התראות שייכות לנושא ב-MCP המכונה ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

כדי לגרום ללוגים לעבוד, השרת צריך להפעיל זאת כתכונה/יכולת כך:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> בהתאם ל-SDK שבו משתמשים, ייתכן שלוגים יופעלו כברירת מחדל, או שתצטרכו להפעילם במפורש בתצורת השרת.

ישנם סוגים שונים של התראות:

| רמה       | תיאור                      | מקרה שימוש לדוגמה              |
|-----------|----------------------------|---------------------------------|
| debug     | מידע מפורט לדיבוג          | נקודות כניסה/יציאה לפונקציות   |
| info      | הודעות מידע כלליות         | עדכוני התקדמות של פעולה        |
| notice    | אירועים רגילים אך משמעותיים | שינויים בתצורה                 |
| warning   | תנאי אזהרה                 | שימוש בתכונה מיושנת            |
| error     | תנאי שגיאה                 | כשלי פעולה                     |
| critical  | תנאים קריטיים              | כשלי רכיבי מערכת               |
| alert     | פעולה נדרשת מיידית         | זיהוי פגיעה בנתונים            |
| emergency | המערכת אינה שמישה          | כשל מוחלט של המערכת            |

## יישום התראות ב-MCP

כדי ליישם התראות ב-MCP, עליכם להגדיר את צד השרת וצד הלקוח לטיפול בעדכונים בזמן אמת. כך תוכלו לספק משוב מיידי למשתמשים במהלך פעולות ארוכות טווח.

### צד השרת: שליחת התראות

נתחיל בצד השרת. ב-MCP, מגדירים כלים שיכולים לשלוח התראות בזמן עיבוד בקשות. השרת משתמש באובייקט הקשר (בדרך כלל `ctx`) כדי לשלוח הודעות ללקוח.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

בדוגמה הקודמת, הכלי `process_files` שולח שלוש התראות ללקוח בזמן שהוא מעבד כל קובץ. השיטה `ctx.info()` משמשת לשליחת הודעות מידע.

בנוסף, כדי להפעיל התראות, ודאו שהשרת שלכם משתמש בתעבורת סטרימינג (כמו `streamable-http`) והלקוח שלכם מיישם מנהל הודעות לעיבוד התראות. כך ניתן להגדיר את השרת לשימוש בתעבורת `streamable-http`:

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

בדוגמה זו ב-.NET, הכלי `ProcessFiles` מעוטר בתכונת `Tool` ושולח שלוש התראות ללקוח בזמן שהוא מעבד כל קובץ. השיטה `ctx.Info()` משמשת לשליחת הודעות מידע.

כדי להפעיל התראות בשרת MCP שלכם ב-.NET, ודאו שאתם משתמשים בתעבורת סטרימינג:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### צד הלקוח: קבלת התראות

הלקוח חייב ליישם מנהל הודעות לעיבוד והצגת התראות כשהן מגיעות.

#### Python

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

בקוד הקודם, הפונקציה `message_handler` בודקת אם ההודעה הנכנסת היא התראה. אם כן, היא מדפיסה את ההתראה; אחרת, היא מעבדת אותה כהודעת שרת רגילה. שימו לב גם כיצד `ClientSession` מאותחל עם `message_handler` לטיפול בהתראות נכנסות.

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

בדוגמה זו ב-.NET, הפונקציה `MessageHandler` בודקת אם ההודעה הנכנסת היא התראה. אם כן, היא מדפיסה את ההתראה; אחרת, היא מעבדת אותה כהודעת שרת רגילה. ה-`ClientSession` מאותחל עם מנהל ההודעות דרך `ClientSessionOptions`.

כדי להפעיל התראות, ודאו שהשרת שלכם משתמש בתעבורת סטרימינג (כמו `streamable-http`) והלקוח שלכם מיישם מנהל הודעות לעיבוד התראות.

## התראות התקדמות ותסריטים

סעיף זה מסביר את מושג התראות ההתקדמות ב-MCP, מדוע הן חשובות וכיצד ליישמן באמצעות Streamable HTTP. תמצאו גם משימה מעשית לחיזוק ההבנה שלכם.

התראות התקדמות הן הודעות בזמן אמת שנשלחות מהשרת ללקוח במהלך פעולות ארוכות טווח. במקום להמתין לסיום התהליך כולו, השרת מעדכן את הלקוח על הסטטוס הנוכחי. זה משפר שקיפות, חוויית משתמש ומקל על דיבוג.

**דוגמה:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### למה להשתמש בהתראות התקדמות?

התראות התקדמות חיוניות מכמה סיבות:

- **חוויית משתמש טובה יותר:** משתמשים רואים עדכונים כשהעבודה מתקדמת, לא רק בסיום.
- **משוב בזמן אמת:** לקוחות יכולים להציג סרגלי התקדמות או לוגים, מה שהופך את האפליקציה למגיבה.
- **דיבוג וניטור קלים יותר:** מפתחים ומשתמשים יכולים לראות היכן תהליך עשוי להיות איטי או תקוע.

### כיצד ליישם התראות התקדמות

כך ניתן ליישם התראות התקדמות ב-MCP:

- **בשרת:** השתמשו ב-`ctx.info()` או `ctx.log()` כדי לשלוח התראות כשהפריטים מעובדים. זה שולח הודעה ללקוח לפני שהתוצאה הראשית מוכנה.
- **בלקוח:** יישמו מנהל הודעות שמאזין להתראות ומציג אותן כשהן מגיעות. מנהל זה מבדיל בין התראות לתוצאה הסופית.

**דוגמת שרת:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**דוגמת לקוח:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## שיקולי אבטחה

בעת יישום שרתי MCP עם תעבורות מבוססות HTTP, האבטחה הופכת לדאגה מרכזית שדורשת תשומת לב קפדנית למספר וקטורי תקיפה ומנגנוני הגנה.

### סקירה כללית

האבטחה קריטית כאשר חושפים שרתי MCP דרך HTTP. Streamable HTTP מציג משטחי תקיפה חדשים ודורש תצורה זהירה.

### נקודות מפתח

- **אימות כותרת Origin**: תמיד אימתו את כותרת ה-`Origin` כדי למנוע מתקפות DNS rebinding.
- **קשירה ל-localhost**: לפיתוח מקומי, קשרו שרתים ל-`localhost` כדי להימנע מחשיפתם לאינטרנט הציבורי.
- **אימות**: יישמו אימות (לדוגמה, מפתחות API, OAuth) לפריסות בייצור.
- **CORS**: הגדירו מדיניות Cross-Origin Resource Sharing (CORS) כדי להגביל גישה.
- **HTTPS**: השתמשו ב-HTTPS בייצור כדי להצפין תעבורה.

### שיטות עבודה מומלצות

- לעולם אל תסמכו על בקשות נכנסות ללא אימות.
- רשמו ונתחו את כל הגישות והשגיאות.
- עדכנו באופן קבוע תלותים כדי לתקן פגיעויות אבטחה.

### אתגרים

- איזון בין אבטחה לקלות פיתוח.
- הבטחת תאימות עם סביבות לקוח שונות.

## שדרוג מ-SSE ל-Streamable HTTP

ליישומים שמשתמשים כיום ב-Server-Sent Events (SSE), מעבר ל-Streamable HTTP מספק יכולות משופרות וקיימות טובה יותר לטווח הארוך עבור יישומי MCP שלכם.

### למה לשדרג?
ישנם שני יתרונות מרכזיים לשדרוג מ-SSE ל-Streamable HTTP:

- Streamable HTTP מציע יכולת הרחבה טובה יותר, תאימות רחבה יותר ותמיכה עשירה יותר בהתראות בהשוואה ל-SSE.
- זהו אמצעי התקשורת המומלץ עבור יישומי MCP חדשים.

### שלבי מעבר

כך ניתן לעבור מ-SSE ל-Streamable HTTP ביישומי MCP שלכם:

- **עדכנו את קוד השרת** לשימוש ב-`transport="streamable-http"` בתוך `mcp.run()`.
- **עדכנו את קוד הלקוח** לשימוש ב-`streamablehttp_client` במקום לקוח SSE.
- **ממשו מנהל הודעות** בצד הלקוח לעיבוד התראות.
- **בדקו תאימות** עם כלים ותהליכי עבודה קיימים.

### שמירה על תאימות

מומלץ לשמור על תאימות עם לקוחות SSE קיימים במהלך תהליך המעבר. הנה כמה אסטרטגיות:

- ניתן לתמוך גם ב-SSE וגם ב-Streamable HTTP על ידי הפעלת שני אמצעי התקשורת בנקודות קצה שונות.
- העבירו לקוחות בהדרגה לאמצעי התקשורת החדש.

### אתגרים

יש לטפל באתגרים הבאים במהלך המעבר:

- לוודא שכל הלקוחות מעודכנים
- להתמודד עם הבדלים במשלוח ההתראות

## שיקולי אבטחה

אבטחה צריכה להיות בראש סדר העדיפויות בעת יישום שרתים, במיוחד כאשר משתמשים באמצעי תקשורת מבוססי HTTP כמו Streamable HTTP ב-MCP.

בעת יישום שרתי MCP עם אמצעי תקשורת מבוססי HTTP, האבטחה הופכת לנושא קריטי הדורש תשומת לב קפדנית למגוון וקטורי תקיפה ומנגנוני הגנה.

### סקירה כללית

אבטחה היא קריטית כאשר חושפים שרתי MCP דרך HTTP. Streamable HTTP מציג משטחי תקיפה חדשים ודורש תצורה זהירה.

הנה כמה שיקולי אבטחה מרכזיים:

- **אימות כותרת Origin**: תמיד אימתו את כותרת ה-`Origin` כדי למנוע תקיפות DNS rebinding.
- **קשירה ל-localhost**: לפיתוח מקומי, קשרו את השרתים ל-`localhost` כדי למנוע חשיפה לאינטרנט הציבורי.
- **אימות**: יישמו מנגנוני אימות (כגון מפתחות API, OAuth) עבור פריסות ייצור.
- **CORS**: הגדירו מדיניות Cross-Origin Resource Sharing (CORS) כדי להגביל גישה.
- **HTTPS**: השתמשו ב-HTTPS בסביבת ייצור כדי להצפין את התעבורה.

### שיטות עבודה מומלצות

בנוסף, הנה כמה שיטות עבודה מומלצות ליישום אבטחה בשרת MCP מבוסס סטרימינג:

- לעולם אל תסמכו על בקשות נכנסות ללא אימות.
- תעדו ונטרו את כל הגישות והשגיאות.
- עדכנו באופן קבוע את התלויות כדי לתקן פגיעויות אבטחה.

### אתגרים

תיתקלו בכמה אתגרים בעת יישום אבטחה בשרתי MCP מבוססי סטרימינג:

- איזון בין אבטחה לנוחות פיתוח
- הבטחת תאימות עם סביבות לקוח שונות

### משימה: בנו אפליקציית MCP סטרימינג משלכם

**תרחיש:**
בנו שרת ולקוח MCP שבהם השרת מעבד רשימת פריטים (לדוגמה, קבצים או מסמכים) ושולח התראה עבור כל פריט שעובד. הלקוח צריך להציג כל התראה בזמן אמת.

**שלבים:**

1. מימוש כלי שרת שמעבד רשימה ושולח התראות עבור כל פריט.
2. מימוש לקוח עם מנהל הודעות שמציג התראות בזמן אמת.
3. בדקו את המימוש על ידי הפעלת השרת והלקוח, וצפו בהתראות.

[פתרון](./solution/README.md)

## קריאה נוספת ומה הלאה?

כדי להמשיך את המסע שלכם עם סטרימינג ב-MCP ולהרחיב את הידע, חלק זה מספק משאבים נוספים והצעות לצעדים הבאים לבניית יישומים מתקדמים יותר.

### קריאה נוספת

- [Microsoft: מבוא לסטרימינג ב-HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ב-ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: בקשות סטרימינג](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### מה הלאה?

- נסו לבנות כלים מתקדמים יותר ב-MCP המשתמשים בסטרימינג לניתוח בזמן אמת, צ'אט או עריכה שיתופית.
- חקרו שילוב סטרימינג ב-MCP עם מסגרות פרונטאנד (React, Vue וכו') לעדכוני UI חיים.
- הבא: [שימוש בערכת כלים AI עבור VSCode](../07-aitk/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.