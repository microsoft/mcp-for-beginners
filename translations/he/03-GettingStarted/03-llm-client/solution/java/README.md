# לקוח LLM למחשבון  

> [!NOTE]  
> הפתרון הזה מתחבר לשירות המחשבון הישן של הקורס של HTTP+SSE ו  
> מיועד ל-MCP `2025-11-25` SDK APIs. זה אינו דוגמת `2026-07-28` Streamable HTTP.  
 

יישום Java המדגים כיצד להשתמש ב-LangChain4j כדי להתחבר לשירות מחשבון MCP (Model Context Protocol) דרך ממשק ה-API התואם MiniMax OpenAI.  

## דרישות מקדימות  

- Java 21 או גרסה חדשה יותר  
- Maven 3.6+ (או שימוש ב-wrapper של Maven הכלול)  
- מפתח API של MiniMax  
- שירות מחשבון MCP הפועל על `http://localhost:8080`  

## קבלת מפתח ה-API  

יישום זה משתמש בממשק ה-API התואם MiniMax OpenAI. עקוב אחר השלבים הבאים כדי לקבל את המפתח והנקודה הסופית:  

### 1. בחר נקודת קצה  
1. השתמש ב-`https://api.minimax.io/v1` לנקודת הקצה הגלובלית  
2. השתמש ב-`https://api.minimaxi.com/v1` לנקודת הקצה בסין  

### 2. צור מפתח API  
1. צור מפתח API של MiniMax מחשבון MiniMax שלך  
2. שמור את המפתח במקום מאובטח  

### 3. הגדר את משתני הסביבה  

#### ב-Windows (Command Prompt):  
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

1. **שכפל או נווט לספריית הפרויקט**  

2. **התקן את התלויות**:  
   ```cmd
   mvnw clean install
   ```
   או אם יש לך Maven מותקן באופן גלובלי:  
   ```cmd
   mvn clean install
   ```
  
3. **הגדר את משתני הסביבה** (ראו סעיף "קבלת מפתח API" למעלה)  

4. **הפעל את שירות המחשבון MCP**:  
   ודא שיש לך את שירות המחשבון MCP של פרק 1 פועל על `http://localhost:8080/sse`. יש להפעילו לפני הפעלת הלקוח.  

## הפעלת היישום  

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```
  
## מה היישום עושה  

היישום מדגים שלוש אינטראקציות עיקריות עם שירות המחשבון:  

1. **חיבור**: מחשב את הסכום של 24.5 ו-17.3  
2. **שורש ריבועי**: מחשב את השורש הריבועי של 144  
3. **עזרה**: מציג פונקציות מחשבון זמינות  

## תוצאה צפויה  

בעת הפעלה מוצלחת, עליך לראות פלט דומה ל:  

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```
  
## פתרון תקלות  

### בעיות נפוצות  

1. **"משתנה הסביבה OPENAI_API_KEY לא מוגדר"**  
   - ודא שהגדרת את משתנה הסביבה `OPENAI_API_KEY`  
   - הפעל מחדש את הטרמינל / שורת הפקודה לאחר ההגדרה  

2. **"החיבור נדחה אל localhost:8080"**  
   - ודא ששירות המחשבון MCP פועל על הפורט 8080  
   - בדוק אם שירות אחר משתמש בפורט 8080  

3. **"האימות נכשל"**  
   - ודא שמפתח ה-API שלך תקין  
   - בדוק ש-`OPENAI_BASE_URL` מתאים לנקודת הקצה שבחרת להשתמש בה  

4. **שגיאות בניית Maven**  
   - ודא שאתה משתמש ב-Java 21 או גרסה גבוהה יותר: `java -version`  
   - נסה לנקות את הבנייה: `mvnw clean`  

### איתור באגים  

להפעלת רישום debug, הוסף את הפרמטר הבא ל-JVM בעת ההפעלה:  
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```
  
## תצורה  

היישום מוגדר כך:  
- להשתמש ב-MiniMax-M3 כברירת מחדל; הגדר את `MINIMAX_MODEL_ID` לבחירת `MiniMax-M3` או `MiniMax-M2.7`  
- להתחבר ל-`OPENAI_BASE_URL` כאשר הוא מוגדר; אחרת השתמש ב-`https://api.minimaxi.com/v1` כאשר `MINIMAX_REGION=cn_zh`, או ב-`https://api.minimax.io/v1` כברירת מחדל  
- להתחבר לשירות MCP ב-`http://localhost:8080/sse`  
- להשתמש בפסק זמן של 60 שניות לבקשות  

## תלויות  

תלויות עיקריות בפרויקט זה:  
- **LangChain4j**: לשילוב AI וניהול כלים  
- **LangChain4j MCP**: לתמיכה בפרוטוקול הקשר למודל  
- **LangChain4j OpenAI רשמי**: לשילוב ממשק API תואם MiniMax OpenAI  
- **Spring Boot**: למסגרת יישום והזרקת תלויות  

## רישיון  

פרויקט זה מורשה תחת רישיון Apache 2.0 - ראה את הקובץ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) לפרטים.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->