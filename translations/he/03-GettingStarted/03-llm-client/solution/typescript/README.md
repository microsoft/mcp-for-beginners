# הרצת הדוגמה הזו

בדוגמה הזו יש להשתמש ב-LLM בצד הלקוח. ה-LLM דורש שתפעילו את זה ב-Codespaces או שתגדירו טוקן גישה אישי ב-GitHub כדי שזה יעבוד.

## -1- התקנת התלויות

```bash
npm install
```

## -3- הפעלת השרת

```bash
npm run build
```

## -4- הפעלת הלקוח

```sh
npm run client
```

אתם אמורים לראות תוצאה דומה ל:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.