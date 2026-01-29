# שירות מחשבון בסיסי MCP

שירות זה מספק פעולות מחשבון בסיסיות דרך פרוטוקול Model Context (MCP). הוא מעוצב כדוגמה פשוטה למתחילים הלומדים על יישומי MCP.

למידע נוסף, ראה [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## תכונות

שירות המחשבון הזה מציע את היכולות הבאות:

1. **פעולות אריתמטיות בסיסיות**:
   - חיבור של שני מספרים
   - חיסור של מספר אחד מאחר
   - כפל של שני מספרים
   - חילוק של מספר אחד באחר (עם בדיקת חילוק באפס)

## שימוש בסוג `stdio`
  
## תצורה

1. **הגדרת שרתי MCP**:
   - פתח את סביבת העבודה שלך ב-VS Code.
   - צור קובץ `.vscode/mcp.json` בתיקיית סביבת העבודה שלך להגדרת שרתי MCP. דוגמת תצורה:

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

   - תתבקש להזין את שורש מאגר ה-GitHub, שניתן לקבל באמצעות הפקודה `git rev-parse --show-toplevel`.

## שימוש בשירות

השירות חושף את נקודות הקצה הבאות דרך פרוטוקול MCP:

- `add(a, b)`: מחבר שני מספרים יחד
- `subtract(a, b)`: מחסר את המספר השני מהראשון
- `multiply(a, b)`: מכפיל שני מספרים
- `divide(a, b)`: מחלק את המספר הראשון בשני (עם בדיקת אפס)
- isPrime(n): בודק אם מספר הוא ראשוני

## בדיקה עם Github Copilot Chat ב-VS Code

1. נסה לבצע בקשה לשירות באמצעות פרוטוקול MCP. לדוגמה, תוכל לשאול:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. כדי לוודא שהכלים בשימוש, הוסף #MyCalculator להודעה. לדוגמה:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## גרסה מכולתית

הפתרון הקודם מצוין כאשר מותקן .NET SDK וכל התלויות במקום. עם זאת, אם תרצה לשתף את הפתרון או להריץ אותו בסביבה שונה, תוכל להשתמש בגרסה המכולתית.

1. הפעל את Docker וודא שהוא פועל.
1. מהטרמינל, נווט לתיקייה `03-GettingStarted\samples\csharp\src`
1. לבניית תמונת Docker עבור שירות המחשבון, הרץ את הפקודה הבאה (החלף את `<YOUR-DOCKER-USERNAME>` בשם המשתמש שלך ב-Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. לאחר שהתמונה נבנתה, נעלה אותה ל-Docker Hub. הרץ את הפקודה הבאה:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## שימוש בגרסה המכולתית

1. בקובץ `.vscode/mcp.json`, החלף את תצורת השרת בפקודה הבאה:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   בהתבוננות בתצורה, ניתן לראות שהפקודה היא `docker` והארגומנטים הם `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. הדגל `--rm` מבטיח שהמכולה תוסר לאחר עצירתה, והדגל `-i` מאפשר אינטראקציה עם קלט הסטנדרטי של המכולה. הארגומנט האחרון הוא שם התמונה שבנינו ופרסמנו ל-Docker Hub.

## בדיקת הגרסה המכולתית

הפעל את שרת MCP על ידי לחיצה על כפתור ההפעלה הקטן מעל `"mcp-calc": {`, וכמו קודם תוכל לבקש משירות המחשבון לבצע עבורך חישובים.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.