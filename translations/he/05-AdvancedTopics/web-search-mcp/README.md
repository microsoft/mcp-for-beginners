# שיעור: בניית שרת MCP לחיפוש באינטרנט

פרק זה מדגים כיצד לבנות סוכן AI אמיתי שמשתלב עם APIs חיצוניים, מטפל בסוגי נתונים מגוונים, מנהל שגיאות ומאחד כלים מרובים — הכל בפורמט מוכן לפרודקשן. תראו:

- **שילוב עם APIs חיצוניים שדורשים אימות**
- **טיפול בסוגי נתונים מגוונים ממספר נקודות קצה**
- **אסטרטגיות טיפול בשגיאות ורישום יציבות**
- **אורקסטרציה של כלים מרובים בשרת יחיד**

בסוף, תרכשו ניסיון מעשי עם דפוסים ופרקטיקות מומלצות החיוניות ליישומים מתקדמים מבוססי AI ו-LLM.

## מבוא

בשיעור זה תלמדו כיצד לבנות שרת MCP ולקוח מתקדמים שמרחיבים את יכולות ה-LLM עם נתוני רשת בזמן אמת באמצעות SerpAPI. זוהי מיומנות קריטית לפיתוח סוכני AI דינמיים שיכולים לגשת למידע עדכני מהאינטרנט.

## מטרות הלמידה

בסיום השיעור תוכלו:

- לשלב APIs חיצוניים (כמו SerpAPI) בצורה מאובטחת בשרת MCP
- לממש כלים מרובים לחיפוש באינטרנט, חדשות, מוצרים ושאלות ותשובות
- לפרסר ולעצב נתונים מובנים לצריכת LLM
- לטפל בשגיאות ולנהל מגבלות קצב API ביעילות
- לבנות ולבדוק לקוחות MCP אוטומטיים ואינטראקטיביים

## שרת MCP לחיפוש באינטרנט

חלק זה מציג את הארכיטקטורה והתכונות של שרת MCP לחיפוש באינטרנט. תראו כיצד FastMCP ו-SerpAPI משולבים יחד להרחבת יכולות ה-LLM עם נתוני רשת בזמן אמת.

### סקירה כללית

מימוש זה כולל ארבעה כלים המדגימים את יכולת ה-MCP לטפל במשימות מגוונות המונעות על ידי API חיצוני בצורה מאובטחת ויעילה:

- **general_search**: לתוצאות חיפוש רחבות באינטרנט
- **news_search**: לכותרות חדשות עדכניות
- **product_search**: לנתוני מסחר אלקטרוני
- **qna**: לקטעי שאלות ותשובות

### תכונות
- **דוגמאות קוד**: כוללות קטעי קוד ספציפיים לשפה בפייתון (וקלים להרחבה לשפות נוספות) עם נקודות קוד להבהרה

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

לפני הרצת הלקוח, כדאי להבין מה השרת עושה. קובץ [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) מממש את שרת ה-MCP, חושף כלים לחיפוש באינטרנט, חדשות, מוצרים ושאלות ותשובות באמצעות שילוב עם SerpAPI. הוא מטפל בבקשות נכנסות, מנהל קריאות API, מפרש תגובות ומחזיר תוצאות מובנות ללקוח.

ניתן לעיין במימוש המלא ב-[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

הנה דוגמה קצרה לאופן שבו השרת מגדיר ומרשם כלי:

### שרת Python

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **שילוב API חיצוני**: מדגים טיפול מאובטח במפתחות API ובבקשות חיצוניות
- **פרסור נתונים מובנים**: מראה כיצד להמיר תגובות API לפורמטים ידידותיים ל-LLM
- **טיפול בשגיאות**: טיפול יציב בשגיאות עם רישום מתאים
- **לקוח אינטראקטיבי**: כולל גם בדיקות אוטומטיות וגם מצב אינטראקטיבי לבדיקות
- **ניהול הקשר**: מנצל את MCP Context לרישום ומעקב אחר בקשות

## דרישות מוקדמות

לפני שתתחילו, ודאו שהסביבה שלכם מוגדרת כראוי על ידי ביצוע השלבים הבאים. זה יבטיח שכל התלויות מותקנות ומפתחות ה-API מוגדרים נכון לפיתוח ובדיקות חלקות.

- Python 3.8 ומעלה
- מפתח SerpAPI (הרשמו ב-[SerpAPI](https://serpapi.com/) - יש שכבת חינם)

## התקנה

כדי להתחיל, בצעו את השלבים הבאים להגדרת הסביבה:

1. התקינו את התלויות באמצעות uv (מומלץ) או pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. צרו קובץ `.env` בשורש הפרויקט עם מפתח SerpAPI שלכם:

```
SERPAPI_KEY=your_serpapi_key_here
```

## שימוש

שרת MCP לחיפוש באינטרנט הוא הרכיב המרכזי החושף כלים לחיפוש באינטרנט, חדשות, מוצרים ושאלות ותשובות באמצעות שילוב עם SerpAPI. הוא מטפל בבקשות נכנסות, מנהל קריאות API, מפרש תגובות ומחזיר תוצאות מובנות ללקוח.

ניתן לעיין במימוש המלא ב-[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### הפעלת השרת

להפעלת שרת ה-MCP, השתמשו בפקודה הבאה:

```bash
python server.py
```

השרת ירוץ כשרת MCP מבוסס stdio שאליו הלקוח יכול להתחבר ישירות.

### מצבי לקוח

הלקוח (`client.py`) תומך בשני מצבים לאינטראקציה עם שרת ה-MCP:

- **מצב רגיל**: מריץ בדיקות אוטומטיות שבודקות את כל הכלים ומוודאות את תגובותיהם. זה שימושי לבדיקות מהירות שהשרת והכלים פועלים כמצופה.
- **מצב אינטראקטיבי**: מפעיל ממשק מבוסס תפריט שבו ניתן לבחור ולהפעיל כלים ידנית, להזין שאילתות מותאמות ולראות תוצאות בזמן אמת. אידיאלי לחקירת יכולות השרת וניסויים עם קלטים שונים.

ניתן לעיין במימוש המלא ב-[`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### הפעלת הלקוח

להרצת הבדיקות האוטומטיות (השרת יופעל אוטומטית):

```bash
python client.py
```

או להרצה במצב אינטראקטיבי:

```bash
python client.py --interactive
```

### בדיקות בשיטות שונות

ישנן דרכים שונות לבדוק ולהתממשק עם הכלים שהשרת מספק, בהתאם לצרכים ולזרימת העבודה שלכם.

#### כתיבת סקריפטים מותאמים לבדיקה עם MCP Python SDK
ניתן גם לבנות סקריפטים מותאמים לבדיקה באמצעות MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

בהקשר זה, "סקריפט בדיקה" הוא תוכנית פייתון מותאמת שאתם כותבים כדי לפעול כלקוח לשרת MCP. במקום להיות בדיקת יחידה פורמלית, סקריפט זה מאפשר להתחבר לשרת באופן תכנותי, לקרוא לכל אחד מהכלים עם פרמטרים שתבחרו, ולבדוק את התוצאות. גישה זו שימושית ל:

- פרוטוטייפינג וניסויים עם קריאות לכלים
- אימות תגובות השרת לקלטים שונים
- אוטומציה של קריאות חוזרות לכלים
- בניית זרימות עבודה או אינטגרציות משלכם מעל שרת ה-MCP

ניתן להשתמש בסקריפטים כדי לנסות שאילתות חדשות במהירות, לאבחן התנהגות כלים, או אפילו כנקודת התחלה לאוטומציה מתקדמת יותר. להלן דוגמה לשימוש ב-MCP Python SDK ליצירת סקריפט כזה:

## תיאורי כלים

ניתן להשתמש בכלים הבאים שמספק השרת לביצוע סוגי חיפושים ושאילתות שונים. כל כלי מתואר להלן עם הפרמטרים שלו ודוגמת שימוש.

חלק זה מספק פרטים על כל כלי זמין ופרמטריו.

### general_search

מבצע חיפוש כללי באינטרנט ומחזיר תוצאות מעוצבות.

**כיצד לקרוא לכלי זה:**

ניתן לקרוא ל-`general_search` מתוך הסקריפט שלכם באמצעות MCP Python SDK, או אינטראקטיבית דרך Inspector או מצב הלקוח האינטראקטיבי. הנה דוגמת קוד עם ה-SDK:

# [דוגמת Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

כחלופה, במצב אינטראקטיבי, בחרו `general_search` מהתפריט והזינו את השאילתה כשמתבקש.

**פרמטרים:**
- `query` (מחרוזת): שאילתת החיפוש

**דוגמת בקשה:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

מחפש מאמרי חדשות עדכניים הקשורים לשאילתה.

**כיצד לקרוא לכלי זה:**

ניתן לקרוא ל-`news_search` מתוך הסקריפט שלכם באמצעות MCP Python SDK, או אינטראקטיבית דרך Inspector או מצב הלקוח האינטראקטיבי. הנה דוגמת קוד עם ה-SDK:

# [דוגמת Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

כחלופה, במצב אינטראקטיבי, בחרו `news_search` מהתפריט והזינו את השאילתה כשמתבקש.

**פרמטרים:**
- `query` (מחרוזת): שאילתת החיפוש

**דוגמת בקשה:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

מחפש מוצרים התואמים לשאילתה.

**כיצד לקרוא לכלי זה:**

ניתן לקרוא ל-`product_search` מתוך הסקריפט שלכם באמצעות MCP Python SDK, או אינטראקטיבית דרך Inspector או מצב הלקוח האינטראקטיבי. הנה דוגמת קוד עם ה-SDK:

# [דוגמת Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

כחלופה, במצב אינטראקטיבי, בחרו `product_search` מהתפריט והזינו את השאילתה כשמתבקש.

**פרמטרים:**
- `query` (מחרוזת): שאילתת חיפוש המוצר

**דוגמת בקשה:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

מקבל תשובות ישירות לשאלות ממנועי חיפוש.

**כיצד לקרוא לכלי זה:**

ניתן לקרוא ל-`qna` מתוך הסקריפט שלכם באמצעות MCP Python SDK, או אינטראקטיבית דרך Inspector או מצב הלקוח האינטראקטיבי. הנה דוגמת קוד עם ה-SDK:

# [דוגמת Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

כחלופה, במצב אינטראקטיבי, בחרו `qna` מהתפריט והזינו את השאלה כשמתבקש.

**פרמטרים:**
- `question` (מחרוזת): השאלה למציאת תשובה

**דוגמת בקשה:**

```json
{
  "question": "what is artificial intelligence"
}
```

## פרטי קוד

חלק זה מספק קטעי קוד והפניות למימושי השרת והלקוח.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

ראו את [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) ו-[`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) לפרטי מימוש מלאים.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## מושגים מתקדמים בשיעור זה

לפני שתתחילו לבנות, הנה כמה מושגים מתקדמים חשובים שיופיעו לאורך הפרק. הבנתם תעזור לכם לעקוב, גם אם אתם חדשים בהם:

- **אורקסטרציה של כלים מרובים**: משמעות הדבר הפעלת מספר כלים שונים (כמו חיפוש באינטרנט, חדשות, מוצרים ושאלות ותשובות) בתוך שרת MCP יחיד. זה מאפשר לשרת שלכם לטפל במגוון משימות, לא רק באחת.
- **ניהול מגבלות קצב API**: APIs רבים (כמו SerpAPI) מגבילים כמה בקשות אפשר לבצע בפרק זמן מסוים. קוד טוב בודק מגבלות אלו ומטפל בהן בצורה חלקה, כדי שהאפליקציה לא תקרוס אם תגיע למגבלה.
- **פרסור נתונים מובנים**: תגובות API לעיתים מורכבות ומקוננות. המושג מתייחס להפיכת תגובות אלו לפורמטים נקיים וקלים לשימוש, ידידותיים ל-LLM או תוכניות אחרות.
- **התאוששות משגיאות**: לפעמים דברים משתבשים — אולי הרשת נופלת, או ה-API לא מחזיר את מה שציפיתם. התאוששות משגיאות פירושה שהקוד שלכם יכול להתמודד עם הבעיות האלו ולספק משוב שימושי, במקום לקרוס.
- **אימות פרמטרים**: זהו תהליך בדיקת כל הקלטים לכלים שלכם כדי לוודא שהם נכונים ובטוחים לשימוש. כולל הגדרת ערכי ברירת מחדל ווידוא סוגי הנתונים, מה שעוזר למנוע באגים ובלבול.

חלק זה יעזור לכם לאבחן ולפתור בעיות נפוצות שעשויות להתרחש בעבודה עם שרת MCP לחיפוש באינטרנט. אם תיתקלו בשגיאות או בהתנהגות לא צפויה, חלק פתרון הבעיות הזה מספק פתרונות לבעיות הנפוצות ביותר. עברו על הטיפים לפני שתפנו לעזרה נוספת — הם לרוב פותרים בעיות במהירות.

## פתרון בעיות

בעת עבודה עם שרת MCP לחיפוש באינטרנט, ייתכן שתיתקלו מדי פעם בבעיות — זה נורמלי בפיתוח עם APIs חיצוניים וכלים חדשים. חלק זה מספק פתרונות מעשיים לבעיות הנפוצות ביותר, כדי שתוכלו לחזור לעבודה במהירות. אם נתקלתם בשגיאה, התחילו כאן: הטיפים הבאים מתייחסים לבעיות שהמשתמשים נתקלים בהן לעיתים קרובות ויכולים לעזור לפתור את הבעיה ללא צורך בעזרה נוספת.

### בעיות נפוצות

להלן כמה מהבעיות השכיחות ביותר, יחד עם הסברים ברורים ושלבים לפתרונן:

1. **חסר SERPAPI_KEY בקובץ .env**
   - אם אתם רואים את השגיאה `SERPAPI_KEY environment variable not found`, זה אומר שהאפליקציה שלכם לא מוצאת את מפתח ה-API הדרוש לגישה ל-SerpAPI. כדי לתקן זאת, צרו קובץ בשם `.env` בשורש הפרויקט (אם הוא לא קיים) והוסיפו שורה כמו `SERPAPI_KEY=your_serpapi_key_here`. החליפו את `your_serpapi_key_here` במפתח האמיתי שלכם מאתר SerpAPI.

2. **שגיאות מודול לא נמצא**
   - שגיאות כמו `ModuleNotFoundError: No module named 'httpx'` מצביעות על כך שחבילה דרושה בפייתון חסרה. זה קורה בדרך כלל אם לא התקנתם את כל התלויות. כדי לפתור זאת, הריצו `pip install -r requirements.txt` בטרמינל שלכם להתקנת כל מה שהפרויקט צריך.

3. **בעיות חיבור**
   - אם אתם מקבלים שגיאה כמו `Error during client execution`, זה לרוב אומר שהלקוח לא מצליח להתחבר לשרת, או שהשרת לא רץ כמצופה. בדקו ששני הלקוח והשרת הם בגרסאות תואמות, ושהקובץ `server.py` קיים ורץ בתיקייה הנכונה. הפעלה מחדש של השרת והלקוח יכולה לעזור גם כן.

4. **שגיאות SerpAPI**
   - אם מופיעה השגיאה `Search API returned error status: 401`, זה אומר שמפתח ה-SerpAPI שלכם חסר, שגוי או פג תוקף. עברו ללוח הבקרה של SerpAPI, וודאו את המפתח שלכם, ועדכנו את קובץ `.env` במידת הצורך. אם המפתח נכון ועדיין מופיעה השגיאה, בדקו אם שכבת החינם שלכם נגמרה.

### מצב דיבוג

ברירת המחדל, האפליקציה רושמת רק מידע חשוב. אם תרצו לראות פרטים נוספים על מה שקורה (למשל לאבחון בעיות מורכבות), תוכלו להפעיל את מצב DEBUG. זה יציג הרבה יותר מידע על כל שלב שהאפליקציה מבצעת.

**דוגמה: פלט רגיל**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**דוגמה: פלט DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

שימו לב שמצב DEBUG כולל שורות נוספות על בקשות HTTP, תגובות ופרטים פנימיים אחרים. זה יכול להיות מאוד מועיל לפתרון בעיות.
כדי להפעיל את מצב DEBUG, הגדר את רמת הלוג ל-DEBUG בראש הקובץ `client.py` או `server.py` שלך:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## מה הלאה

- [5.10 שידור בזמן אמת](../mcp-realtimestreaming/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.