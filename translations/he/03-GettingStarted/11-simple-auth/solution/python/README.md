# הפעלת דוגמה

## יצירת סביבה

```sh
python -m venv venv
source ./venv/bin/activate
```

## התקנת תלותים

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## יצירת אסימון

תצטרכו ליצור אסימון שהלקוח ישתמש בו כדי לתקשר עם השרת.

הפעילו:

```sh
python util.py
```

## הפעלת קוד

הפעילו את הקוד עם:

```sh
python server.py
```

בטרמינל נפרד, הקלידו:

```sh
python client.py
```

בטרמינל של השרת, אתם אמורים לראות משהו כמו:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

בחלון של הלקוח, אתם אמורים לראות טקסט דומה ל:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

זה אומר שהכול עובד.

### שינוי המידע כדי לראות כישלון

אתרו את הקוד הזה ב-*server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

שנו אותו כך שיאמר "User.Write". לאסימון הנוכחי שלכם אין רמת הרשאה זו, ולכן אם תפעילו מחדש את השרת ותנסו להפעיל את הלקוח שוב, אתם אמורים לראות שגיאה דומה לשגיאה הבאה בטרמינל של השרת:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

אתם יכולים או להחזיר את הקוד של השרת למצבו הקודם או ליצור אסימון חדש שכולל את ההרשאה הנוספת הזו, הבחירה בידיכם.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.