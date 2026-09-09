# לקוח מחשבון LLM

אפליקציית Java המדגימה כיצד להשתמש ב-LangChain4j כדי להתחבר לשירות מחשבון MCP (פרוטוקול הקשר מודל) דרך ה-API התואם ל-MiniMax OpenAI.

## דרישות מוקדמות

- Java 21 ומעלה
- Maven 3.6+ (או שימוש ב-Maven wrapper המצורף)
- מפתח API ל-MiniMax
- שירות מחשבון MCP הפועל בכתובת `http://localhost:8080`

## קבלת מפתח ה-API

אפליקציה זו משתמשת ב-API התואם ל-MiniMax OpenAI. בצע את השלבים הבאים כדי לקבל את המפתח והנקודת קצה:

### 1. בחר נקודת קצה
1. השתמש ב-`https://api.minimax.io/v1` לנקודת הקצה הגלובלית
2. השתמש ב-`https://api.minimaxi.com/v1` לנקודת הקצה בסין

### 2. צור מפתח API
1. צור מפתח API ל-MiniMax מחשבון מחשבונך ב-MiniMax
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

## הגדרה והתקנה

1. **שכפל או עבור לספריית הפרויקט**

2. **התקן תלותיות**:
   ```cmd
   mvnw clean install
   ```
   או אם יש לך Maven מותקן גלובלית:
   ```cmd
   mvn clean install
   ```

3. **הגדר את משתני הסביבה** (ראה את סעיף "קבלת מפתח ה-API" למעלה)

4. **הפעל את שירות מחשבון MCP**:
   וודא ששירות מחשבון MCP מהפרק 1 פועל בכתובת `http://localhost:8080/sse`. יש להפעילו לפני תחילת הלקוח.

## הפעלת האפליקציה

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## מה עושה האפליקציה

האפליקציה מדגימה שלוש אינטראקציות עיקריות עם שירות המחשבון:

1. **חיבור**: מחשבת את סכום 24.5 ו-17.3
2. **שורש ריבועי**: מחשבת את השורש הריבועי של 144
3. **עזרה**: מציגה פונקציות מחשבון זמינות

## תוצאה צפויה

בעת ריצה מוצלחת, אמורה להיראות תוצאה דומה ל:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## פתרון בעיות

### בעיות נפוצות

1. **"משתנה הסביבה OPENAI_API_KEY לא מוגדר"**
   - ודא שהגדרת את משתנה הסביבה `OPENAI_API_KEY`
   - הפעל מחדש את הטרמינל/שורת הפקודה לאחר ההגדרה

2. **"החיבור נדחה ל-localhost:8080"**
   - ודא ששירות מחשבון MCP פועל על פורט 8080
   - בדוק אם שירות אחר משתמש בפורט 8080

3. **"אימות נכשל"**
   - אמת שמפתח ה-API שלך תקין
   - בדוק ש-`OPENAI_BASE_URL` תואם לנקודת הקצה שבחרת

4. **שגיאות בניית Maven**
   - ודא שאתה משתמש ב-Java 21 ומעלה: `java -version`
   - נסה לנקות את הבנייה: `mvnw clean`

### ניפוי שגיאות

כדי לאפשר יומן ניפוי שגיאות, הוסף את הפרמטר JVM הבא בעת הריצה:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## תצורה

האפליקציה מוגדרת ל:
- להשתמש ב-MiniMax-M3 כברירת מחדל, או ב-MiniMax-M2.7 כאשר `MINIMAX_MODEL_ID` מוגדר
- להתחבר ל-`OPENAI_BASE_URL` אם מוגדר; אחרת להשתמש ב-`https://api.minimaxi.com/v1` כאשר `MINIMAX_REGION=cn_zh`, או ב-`https://api.minimax.io/v1` כברירת מחדל
- להתחבר לשירות MCP בכתובת `http://localhost:8080/sse`
- להשתמש בזמן המתנה של 60 שניות לבקשות

## תלותיות

תלותיות מרכזיות בפרויקט זה:
- **LangChain4j**: לאינטגרציה עם AI וניהול כלים
- **LangChain4j MCP**: לתמיכה בפרוטוקול הקשר מודל
- **LangChain4j OpenAI official**: לאינטגרציה עם MiniMax OpenAI-compatible API
- **Spring Boot**: למערכת האפליקציה ולהזרקת תלויות

## רישיון

פרויקט זה מורשה תחת רישיון Apache 2.0 - ראו את הקובץ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) לפרטים.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->