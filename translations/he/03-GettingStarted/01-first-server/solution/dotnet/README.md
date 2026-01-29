# הפעלת הדוגמה הזו

## -1- התקנת התלויות

```bash
dotnet restore
```

## -3- הפעלת הדוגמה

```bash
dotnet run
```

## -4- בדיקת הדוגמה

עם השרת פועל בטרמינל אחד, פתחו טרמינל נוסף והריצו את הפקודה הבאה:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

זה אמור להפעיל שרת אינטרנט עם ממשק חזותי שמאפשר לכם לבדוק את הדוגמה.

לאחר שהשרת מחובר:

- נסו לרשום כלים ולהפעיל `add`, עם ארגומנטים 2 ו-4, אתם אמורים לראות 6 בתוצאה.
- עברו למשאבים ותבנית משאבים וקראו ל-"greeting", הקלידו שם ואתם אמורים לראות ברכה עם השם שסיפקתם.

### בדיקה במצב CLI

ניתן להפעיל את הדוגמה ישירות במצב CLI על ידי הרצת הפקודה הבאה:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

זה ירשום את כל הכלים הזמינים בשרת. אתם אמורים לראות את הפלט הבא:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

כדי להפעיל כלי, הקלידו:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

אתם אמורים לראות את הפלט הבא:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> בדרך כלל הרבה יותר מהיר להפעיל את המפקח במצב CLI מאשר בדפדפן.
> קראו עוד על המפקח [כאן](https://github.com/modelcontextprotocol/inspector).

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.  