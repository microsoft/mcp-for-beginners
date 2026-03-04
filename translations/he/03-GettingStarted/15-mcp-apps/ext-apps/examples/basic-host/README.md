# דוגמה: מארח בסיסי

מימוש מתייחס שמראה כיצד לבנות יישום מארח MCP שמתחבר לשרתי MCP ומציג ממשקי כלי בתוך סנדבוקס מאובטח.

המארח הבסיסי הזה יכול לשמש גם לבדוק אפליקציות MCP במהלך פיתוח מקומי.

## קבצים עיקריים

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - מארח React UI עם בחירת כלי, קלט פרמטרים וניהול iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - פרוקסי iframe חיצוני עם אימות אבטחה והעברת הודעות דו-כיוונית
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - לוגיקה מרכזית: חיבור לשרת, קריאת כלים, והגדרת AppBridge

## התחלה

```bash
npm install
npm run start
# פתח http://localhost:8080
```
  
ברירת המחדל היא שיישום המארח ינסה להתחבר לשרת MCP בכתובת `http://localhost:3001/mcp`. ניתן להגדיר התנהגות זו על ידי קביעה של משתנה הסביבה `SERVERS` במערך JSON של כתובות שרת:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```
  
## ארכיטקטורה

דוגמה זו משתמשת בתבנית סנדבוקס עם שני iframes לבידוד ממשק משתמש מאובטח:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```
  
**מדוע שני iframes?**

- ה-iframe החיצוני פועל במקור נפרד (פורט 8081) ומונע גישה ישירה למארח  
- ה-iframe הפנימי מקבל HTML דרך `srcdoc` ומוגבל על ידי מאפייני הסנדבוקס  
- ההודעות עוברות דרך ה-iframe החיצוני שמאמת ומעביר אותן דו-כיוונית  

ארכיטקטורה זו מבטיחה שגם אם קוד ממשק המשתמש של הכלי זדוני, הוא לא יוכל לגשת ל-DOM, לקוקיז או להקשר ה-JavaScript של יישום המארח.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור:**
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי־דיוקים. יש להתייחס למסמך המקורי בשפת המקור כמקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו אינם אחראים לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->