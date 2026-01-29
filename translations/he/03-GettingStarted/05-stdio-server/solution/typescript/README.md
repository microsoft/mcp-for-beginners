# MCP stdio Server - פתרון ב-TypeScript

> **⚠️ חשוב**: הפתרון הזה עודכן לשימוש ב-**stdio transport** כפי שמומלץ במפרט MCP 2025-06-18. התמיכה ב-SSE transport המקורי הופסקה.

## סקירה כללית

הפתרון הזה ב-TypeScript מדגים כיצד לבנות שרת MCP באמצעות stdio transport הנוכחי. ה-stdio transport פשוט יותר, מאובטח יותר ומספק ביצועים טובים יותר בהשוואה לגישת ה-SSE שהופסקה.

## דרישות מקדימות

- Node.js גרסה 18 ומעלה
- מנהל חבילות npm או yarn

## הוראות התקנה

### שלב 1: התקנת התלויות

```bash
npm install
```

### שלב 2: בניית הפרויקט

```bash
npm run build
```

## הפעלת השרת

שרת ה-stdio פועל בצורה שונה משרת ה-SSE הישן. במקום להפעיל שרת אינטרנט, הוא מתקשר דרך stdin/stdout:

```bash
npm start
```

**חשוב**: השרת ייראה כאילו הוא "נתקע" - זה נורמלי! הוא ממתין להודעות JSON-RPC מ-stdin.

## בדיקת השרת

### שיטה 1: שימוש ב-MCP Inspector (מומלץ)

```bash
npm run inspector
```

זה יבצע:
1. הפעלת השרת כתהליך משנה
2. פתיחת ממשק אינטרנטי לבדיקה
3. אפשרות לבדוק את כל הכלים של השרת בצורה אינטראקטיבית

### שיטה 2: בדיקה ישירה משורת הפקודה

ניתן גם לבדוק על ידי הפעלת ה-Inspector ישירות:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### כלים זמינים

השרת מספק את הכלים הבאים:

- **add(a, b)**: חיבור שני מספרים
- **multiply(a, b)**: כפל שני מספרים  
- **get_greeting(name)**: יצירת ברכה מותאמת אישית
- **get_server_info()**: קבלת מידע על השרת

### בדיקה עם Claude Desktop

כדי להשתמש בשרת הזה עם Claude Desktop, הוסף את ההגדרה הבאה לקובץ `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## מבנה הפרויקט

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## הבדלים מרכזיים מ-SSE

**stdio transport (נוכחי):**
- ✅ התקנה פשוטה - אין צורך בשרת HTTP
- ✅ אבטחה משופרת - אין נקודות קצה HTTP
- ✅ תקשורת מבוססת תהליכי משנה
- ✅ JSON-RPC דרך stdin/stdout
- ✅ ביצועים טובים יותר

**SSE transport (הופסק):**
- ❌ דרש התקנת שרת Express
- ❌ נדרש ניהול ניתוב ומושבים מורכב
- ❌ יותר תלויות (Express, טיפול ב-HTTP)
- ❌ שיקולי אבטחה נוספים
- ❌ הופסק במפרט MCP 2025-06-18

## טיפים לפיתוח

- השתמש ב-`console.error()` לרישום לוגים (לעולם לא ב-`console.log()` כיוון שהוא כותב ל-stdout)
- בצע בנייה עם `npm run build` לפני בדיקות
- בדוק עם ה-Inspector לצורך ניפוי שגיאות חזותי
- ודא שכל הודעות ה-JSON מעוצבות כראוי
- השרת מטפל באופן אוטומטי בכיבוי מסודר בעת SIGINT/SIGTERM

הפתרון הזה עוקב אחר מפרט MCP הנוכחי ומדגים שיטות עבודה מומלצות ליישום stdio transport באמצעות TypeScript.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.