# לקוח מחשבון LLM

יישום ב-Java המדגים כיצד להשתמש ב-LangChain4j כדי להתחבר לשירות מחשבון MCP (Model Context Protocol) דרך ממשק API תואם MiniMax OpenAI.

## דרישות מוקדמות

- Java 21 או גבוה יותר
- Maven 3.6+ (או שימוש במעטפת Maven הכלולה)
- מפתח API של MiniMax
- שירות מחשבון MCP פועל בכתובת `http://localhost:8080`

## קבלת מפתח ה-API

יישום זה משתמש בממשק API תואם MiniMax OpenAI. בצע את השלבים הבאים לקבלת המפתח והנקודה הקצה שלך:

### 1. בחר נקודת קצה
1. השתמש ב-`https://api.minimax.io/v1` עבור נקודת הקצה העולמית
2. השתמש ב-`https://api.minimaxi.com/v1` עבור נקודת הקצה בסין

### 2. צור מפתח API
1. צור מפתח API של MiniMax מחשבון MiniMax שלך
2. שמור את המפתח במקום בטוח

### 3. הגדר את משתני הסביבה

#### ב-Windows (שורת הפקודה):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### ב-Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### ב-macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## התקנה והגדרה

1. **שכפל או עבור לתיקיית הפרויקט**

2. **התקן את התלויות**:
   ```cmd
   mvnw clean install
   ```
   או אם יש לך Maven מותקן באופן גלובלי:
   ```cmd
   mvn clean install
   ```

3. **הגדר את משתני הסביבה** (ראה את הקטע "קבלת מפתח ה-API" למעלה)

4. **הפעל את שירות מחשבון MCP**:
   וודא ששירות מחשבון MCP משלב 1 פועל בכתובת `http://localhost:8080/sse`. זה צריך לפעול לפני הפעלת הלקוח.

## הפעלת היישום

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## מה היישום עושה

היישום מדגים שלושה אינטראקציות עיקריות עם שירות המחשבון:

1. **חיבור**: מחשב את הסכום של 24.5 ו-17.3
2. **שורש ריבועי**: מחשב את השורש הריבועי של 144
3. **עזרה**: מציג פונקציות מחשבון זמינות

## פלט צפוי

בעת ריצה מוצלחת, אמור להיראות פלט דומה ל:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## פתרון תקלות

### בעיות נפוצות

1. **"משתנה הסביבה OPENAI_API_KEY לא מוגדר"**
   - ודא שהגדרת את משתנה הסביבה `OPENAI_API_KEY`
   - אתחל מחדש את המסוף/שורת הפקודה אחרי שהגדרת את המשתנה

2. **"החיבור נדחה ל-localhost:8080"**
   - ודא ששירות מחשבון MCP פועל על פורט 8080
   - בדוק אם שירות אחר משתמש בפורט 8080

3. **"אימות נכשל"**
   - אמת שהמפתח API שלך תקין
   - בדוק ש-`OPENAI_BASE_URL` תואם לנקודת הקצה שבכוונתך להשתמש בה

4. **שגיאות בניית Maven**
   - ודא שאתה משתמש ב-Java 21 או גבוה יותר: `java -version`
   - נסה לנקות את הבנייה: `mvnw clean`

### איתור באגים

כדי לאפשר רישום איתור באגים, הוסף את הפרמטר JVM הבא בעת הריצה:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## תצורה

היישום מוגדר ל:
- להשתמש ב-MiniMax-M3 כברירת מחדל; הגדר `MINIMAX_MODEL_ID` כדי לבחור בין `MiniMax-M3` או `MiniMax-M2.7`
- להתחבר ל-`OPENAI_BASE_URL` כשהוא מוגדר; אחרת להשתמש ב-`https://api.minimaxi.com/v1` כאשר `MINIMAX_REGION=cn_zh`, או ב-`https://api.minimax.io/v1` כברירת מחדל
- להתחבר לשירות MCP בכתובת `http://localhost:8080/sse`
- להשתמש בזמני המתנה של 60 שניות לבקשות

## תלויות

תלויות עיקריות בפרויקט זה:
- **LangChain4j**: לאינטגרציה עם בינה מלאכותית וניהול כלים
- **LangChain4j MCP**: לתמיכת פרוטוקול Model Context
- **LangChain4j OpenAI רשמי**: לאינטגרציה עם ממשק API תואם MiniMax OpenAI
- **Spring Boot**: למסגרת יישום והזרקת תלות

## רישיון

פרויקט זה מורשה על פי רישיון Apache 2.0 - עיין בקובץ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) לפרטים.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->