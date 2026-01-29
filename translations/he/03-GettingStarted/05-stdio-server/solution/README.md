# פתרונות שרת MCP stdio

> **⚠️ חשוב**: פתרונות אלו עודכנו לשימוש ב-**stdio transport** כפי שמומלץ במפרט MCP 2025-06-18. אמצעי התקשורת המקורי SSE (Server-Sent Events) הוצא משימוש.

להלן הפתרונות המלאים לבניית שרתי MCP באמצעות stdio transport בכל סביבת ריצה:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - יישום מלא של שרת stdio
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - שרת stdio ב-Python עם asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - שרת stdio ב-.NET עם הזרקת תלות

כל פתרון מדגים:
- הגדרת stdio transport
- הגדרת כלי שרת
- טיפול נכון בהודעות JSON-RPC
- אינטגרציה עם לקוחות MCP כמו Claude

כל הפתרונות עומדים במפרט MCP הנוכחי ומשתמשים ב-stdio transport המומלץ לביצועים ואבטחה מיטביים.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.