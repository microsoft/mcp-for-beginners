# הרצת הדוגמה הזו

מומלץ להתקין את `uv` אבל זה לא חובה, ראה [הוראות](https://docs.astral.sh/uv/#highlights)

## -1- התקן את התלויות

```bash
npm install
```

## -3- הפעל את השרת

```bash
npm run build
```

## -4- הפעל את הלקוח

```sh
npm run client
```

אתה אמור לראות תוצאה דומה ל:

```text
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.