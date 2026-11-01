# שירות מחשבון בסיסי MCP

שירות זה מספק פעולות מחשבון בסיסיות דרך פרוטוקול הקשר המודלי (MCP). הוא מתוכנן כדוגמה פשוטה למתחילים הלומדים על מימושי MCP.

למידע נוסף, עיין ב-[C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## תכונות

שירות המחשבון הזה מציע את היכולות הבאות:

1. **פעולות אריתמטיות בסיסיות**:
   - חיבור של שני מספרים
   - חיסור של מספר אחד מאחר
   - כפל של שני מספרים
   - חילוק של מספר אחד בשני (עם בדיקת חילוק באפס)

## שימוש בסוג `stdio`
  
## קונפיגורציה

1. **הגדרת שרתי MCP**:
   - פתח את סביבת העבודה שלך ב-VS Code.
   - צור קובץ `.vscode/mcp.json` בתיקיית סביבת העבודה שלך להגדיר את שרתי MCP. דוגמת קונפיגורציה:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - תתבקש להזין את שורש מאגר GitHub, שניתן לקבל אתו באמצעות הפקודה `git rev-parse --show-toplevel`.

## שימוש בשירות

השירות חושף את נקודות הקצה הבאות דרך פרוטוקול MCP:

- `add(a, b)`: הוסף שני מספרים
- `subtract(a, b)`: החסר את המספר השני מהראשון
- `multiply(a, b)`: כפל שני מספרים
- `divide(a, b)`: חלק את המספר הראשון בשני (עם בדיקה לאפס)
- isPrime(n): בדוק אם מספר הוא ראשוני

## בדיקה עם Github Copilot Chat ב-VS Code

1. נסה לבצע בקשה לשירות באמצעות פרוטוקול MCP. לדוגמה, תוכל לשאול:
   - "הוסף 5 ו-3"
   - "החסר 10 מ-4"
   - "כפל 6 ו-7"
   - "חלק 8 ב-2"
   - "האם 37854 ראשוני?"
   - "מהם 3 המספרים הראשוניים לפני אחרי 4242?"
2. כדי לוודא שהכלי בשימוש הוסף #MyCalculator להודעה. לדוגמה:
   - "הוסף 5 ו-3 #MyCalculator"
   - "החסר 10 מ-4 #MyCalculator


## גרסה בקונטיינר

הפתרון הקודם מצוין כאשר מותקן SDK של .NET וכל התלויות במקומן. עם זאת, אם תרצה לשתף את הפתרון או להריץ אותו בסביבה שונה, תוכל להשתמש בגרסה בקונטיינר.

1. הפעל את Docker וודא שהוא פועל.
1. מהטרמינל, נווט בתיקייה `03-GettingStarted\samples\csharp\src` 
1. לבניית תמונת Docker לשירות המחשבון, הרץ את הפקודה הבאה (החליף את `<YOUR-DOCKER-USERNAME>` בשם המשתמש שלך ב-Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. לאחר שהתמונה בנויה, נעלה אותה ל-Docker Hub. הרץ את הפקודה הבאה:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## שימוש בגרסה בדוקר

1. בקובץ `.vscode/mcp.json`, החלף את הגדרת השרת עם הבאה:
   ```json
    "mcp-calculator": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calculator"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   בהתבוננות בקונפיגורציה, ניתן לראות שהפקודה היא `docker` והארגומנטים הם `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. הדגל `--rm` מבטיח שהקונטיינר יוסר לאחר שהוא נעצר, והדגל `-i` מאפשרת אינטראקציה עם קלט סטנדרטי של הקונטיינר. הארגומנט האחרון הוא שם התמונה שיצרנו ושהעברנו ל-Docker Hub.

## בדוק את גרסת הדוקר

הפעל את שרת MCP על ידי לחיצה על כפתור ההפעלה הקטן מעל `"mcp-calculator": {`, וכמו קודם תוכל לבקש משירות המחשבון לעשות עבורך חישובים.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->