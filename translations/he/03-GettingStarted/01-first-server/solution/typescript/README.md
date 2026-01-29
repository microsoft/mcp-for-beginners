# הפעלת הדוגמה הזו

מומלץ להתקין את `uv`, אבל זה לא חובה. ראו [הוראות](https://docs.astral.sh/uv/#highlights)

## -1- התקנת התלויות

```bash
npm install
```

## -3- הפעלת הדוגמה

```bash
npm run build
```

## -4- בדיקת הדוגמה

עם השרת פועל בטרמינל אחד, פתחו טרמינל נוסף והריצו את הפקודה הבאה:

```bash
npm run inspector
```

זה אמור להפעיל שרת אינטרנט עם ממשק חזותי שיאפשר לכם לבדוק את הדוגמה.

לאחר שהשרת מחובר:

- נסו לרשום כלים ולהפעיל את `add`, עם ארגומנטים 2 ו-4. אתם אמורים לראות 6 בתוצאה.
- עברו למשאבים ולתבנית משאבים וקראו ל-"greeting". הקלידו שם, ואתם אמורים לראות ברכה עם השם שסיפקתם.

### בדיקה במצב CLI

הבודק שהפעלתם הוא למעשה אפליקציית Node.js, ו-`mcp dev` הוא מעטפת סביבה עבורה.

ניתן להפעיל אותו ישירות במצב CLI על ידי הרצת הפקודה הבאה:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

זה יפרט את כל הכלים הזמינים בשרת. אתם אמורים לראות את הפלט הבא:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

כדי להפעיל כלי, הקלידו:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> בדרך כלל הרבה יותר מהיר להפעיל את הבודק במצב CLI מאשר בדפדפן.
> קראו עוד על הבודק [כאן](https://github.com/modelcontextprotocol/inspector).

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.