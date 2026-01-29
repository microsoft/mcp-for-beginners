# הפעלת דוגמה

הדוגמה הזו מפעילה שרת MCP עם תוכנת ביניים שבודקת אם יש כותרת Authorization תקינה.

## התקנת תלותים

```bash
pip install "mcp[cli]" 
```

## הפעלת השרת

```bash
python server.py
```

הפעל את הלקוח בחלון טרמינל אחר

```bash
python client.py
```

אתה אמור לראות תוצאה דומה ל:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

זה אומר שהאישור שנשלח מתקבל.

נסה לשנות את האישור ב-`client.py` ל-"secret-token2", ואז אתה אמור לראות את הטקסט הזה כחלק מהתגובה:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

זה אומר שהיית מאומת (היה לך אישור), אבל הוא היה לא תקין.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.