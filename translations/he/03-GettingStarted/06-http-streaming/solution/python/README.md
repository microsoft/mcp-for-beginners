# הפעלת הדוגמה הזו

כך ניתן להפעיל את שרת ולקוח הזרמת HTTP הקלאסי, כמו גם את שרת ולקוח הזרמת MCP באמצעות Python.

### סקירה כללית

- תגדיר שרת MCP שמזרים התראות התקדמות ללקוח בזמן שהוא מעבד פריטים.
- הלקוח יציג כל התראה בזמן אמת.
- מדריך זה מכסה דרישות מקדימות, הגדרה, הפעלה ופתרון בעיות.

### דרישות מקדימות

- Python 3.9 או גרסה חדשה יותר
- חבילת Python בשם `mcp` (ניתן להתקין באמצעות `pip install mcp`)

### התקנה והגדרה

1. שיבט את המאגר או הורד את קבצי הפתרון.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **צור והפעל סביבה וירטואלית (מומלץ):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **התקן את התלויות הנדרשות:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### קבצים

- **שרת:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **לקוח:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### הפעלת שרת הזרמת HTTP הקלאסי

1. נווט לתיקיית הפתרון:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. הפעל את שרת הזרמת HTTP הקלאסי:

   ```pwsh
   python server.py
   ```

3. השרת יתחיל ויציג:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### הפעלת לקוח הזרמת HTTP הקלאסי

1. פתח מסוף חדש (הפעל את אותה סביבה וירטואלית ותיקייה):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. תראה הודעות מוזרמות מודפסות ברצף:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### הפעלת שרת הזרמת MCP

1. נווט לתיקיית הפתרון:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. הפעל את שרת MCP עם פרוטוקול streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. השרת יתחיל ויציג:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### הפעלת לקוח הזרמת MCP

1. פתח מסוף חדש (הפעל את אותה סביבה וירטואלית ותיקייה):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. תראה התראות מודפסות בזמן אמת כשהשרת מעבד כל פריט:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### שלבים מרכזיים ביישום

1. **צור את שרת MCP באמצעות FastMCP.**
2. **הגדר כלי שמעבד רשימה ושולח התראות באמצעות `ctx.info()` או `ctx.log()`.**
3. **הפעל את השרת עם `transport="streamable-http"`.**
4. **ממש לקוח עם מנהל הודעות שמציג התראות כשהן מגיעות.**

### סקירת קוד
- השרת משתמש בפונקציות אסינכרוניות ובהקשר MCP כדי לשלוח עדכוני התקדמות.
- הלקוח מממש מנהל הודעות אסינכרוני שמדפיס התראות ותוצאה סופית.

### טיפים ופתרון בעיות

- השתמש ב-`async/await` לפעולות שאינן חוסמות.
- תמיד טפל בחריגות הן בשרת והן בלקוח כדי להבטיח יציבות.
- בדוק עם מספר לקוחות כדי לצפות בעדכונים בזמן אמת.
- אם נתקלת בשגיאות, בדוק את גרסת Python שלך וודא שכל התלויות מותקנות.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.