# הפעלת הדוגמה הזו

## -1- התקנת התלויות

```bash
dotnet restore
```

## -2- הפעלת הדוגמה

```bash
dotnet run
```

## -3- בדיקת הדוגמה

פתחו טרמינל נפרד לפני שאתם מריצים את הפקודה הבאה (ודאו שהשרת עדיין פועל).

כאשר השרת פועל באחד הטרמינלים, פתחו טרמינל נוסף והריצו את הפקודה הבאה:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

זה אמור להפעיל שרת אינטרנט עם ממשק חזותי שיאפשר לכם לבדוק את הדוגמה.

> ודאו ש-**Streamable HTTP** נבחר כסוג התעבורה, וכתובת ה-URL היא `http://localhost:3001/mcp`.

לאחר שהשרת מחובר:

- נסו לרשום כלים ולהפעיל `add`, עם ארגומנטים 2 ו-4, אתם אמורים לראות 6 בתוצאה.
- עברו למשאבים ולתבנית משאבים וקראו ל-"greeting", הקלידו שם ואתם אמורים לראות ברכה עם השם שסיפקתם.

### בדיקה במצב CLI

ניתן להפעיל את הדוגמה ישירות במצב CLI על ידי הרצת הפקודה הבאה:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

זה ירשום את כל הכלים הזמינים בשרת. אתם אמורים לראות את הפלט הבא:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
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
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

אתם אמורים לראות את הפלט הבא:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
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
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.