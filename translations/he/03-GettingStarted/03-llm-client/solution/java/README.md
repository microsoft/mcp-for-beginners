# לקוח מחשבון LLM

יישום Java המדגים כיצד להשתמש ב-LangChain4j כדי להתחבר לשירות מחשבון MCP (Model Context Protocol) עם אינטגרציה של GitHub Models.

## דרישות מוקדמות

- Java 21 ומעלה  
- Maven 3.6+ (או שימוש ב-Maven wrapper המצורף)  
- חשבון GitHub עם גישה ל-GitHub Models  
- שירות מחשבון MCP פועל ב-`http://localhost:8080`  

## קבלת טוקן GitHub

יישום זה משתמש ב-GitHub Models שדורש טוקן גישה אישי של GitHub. בצע את השלבים הבאים כדי לקבל את הטוקן שלך:

### 1. גישה ל-GitHub Models  
1. עבור אל [GitHub Models](https://github.com/marketplace/models)  
2. התחבר עם חשבון ה-GitHub שלך  
3. בקש גישה ל-GitHub Models אם עדיין לא עשית זאת  

### 2. יצירת טוקן גישה אישי  
1. עבור אל [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)  
2. לחץ על "Generate new token" → "Generate new token (classic)"  
3. תן לטוקן שם תיאורי (למשל, "MCP Calculator Client")  
4. הגדר תוקף לפי הצורך  
5. בחר את ההרשאות הבאות:  
   - `repo` (אם ניגשים לרפוזיטוריות פרטיות)  
   - `user:email`  
6. לחץ על "Generate token"  
7. **חשוב**: העתק את הטוקן מיד - לא תוכל לראות אותו שוב!  

### 3. הגדרת משתנה סביבה

#### ב-Windows (Command Prompt):  
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### ב-Windows (PowerShell):  
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### ב-macOS/Linux:  
```bash
export GITHUB_TOKEN=your_github_token_here
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

3. **הגדר את משתנה הסביבה** (ראה סעיף "קבלת טוקן GitHub" למעלה)

4. **הפעל את שירות מחשבון MCP**:  
   ודא ששירות MCP מהפרק הראשון פועל ב-`http://localhost:8080/sse`. השירות צריך לפעול לפני הפעלת הלקוח.

## הפעלת היישום

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## מה היישום עושה

היישום מדגים שלוש אינטראקציות עיקריות עם שירות המחשבון:

1. **חיבור**: מחשב את הסכום של 24.5 ו-17.3  
2. **שורש ריבועי**: מחשב את השורש הריבועי של 144  
3. **עזרה**: מציג את הפונקציות הזמינות במחשבון  

## פלט צפוי

כאשר היישום רץ בהצלחה, תראה פלט דומה ל:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## פתרון בעיות

### בעיות נפוצות

1. **"GITHUB_TOKEN environment variable not set"**  
   - ודא שהגדרת את משתנה הסביבה `GITHUB_TOKEN`  
   - הפעל מחדש את הטרמינל/שורת הפקודה לאחר ההגדרה  

2. **"Connection refused to localhost:8080"**  
   - ודא ששירות MCP פועל על פורט 8080  
   - בדוק אם שירות אחר תופס את פורט 8080  

3. **"Authentication failed"**  
   - וודא שהטוקן שלך תקין ויש לו הרשאות מתאימות  
   - בדוק שיש לך גישה ל-GitHub Models  

4. **שגיאות בניית Maven**  
   - ודא שאתה משתמש ב-Java 21 ומעלה: `java -version`  
   - נסה לנקות את הבנייה: `mvnw clean`  

### איתור באגים

כדי להפעיל רישום דיבוג, הוסף את הפרמטר הבא ל-JVM בעת ההרצה:  
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## קונפיגורציה

היישום מוגדר ל:  
- שימוש ב-GitHub Models עם המודל `gpt-4.1-nano`  
- התחברות לשירות MCP ב-`http://localhost:8080/sse`  
- הגדרת timeout של 60 שניות לבקשות  
- הפעלת רישום בקשות/תגובות לצורך דיבוג  

## תלויות

תלויות מרכזיות בפרויקט זה:  
- **LangChain4j**: לאינטגרציה עם AI וניהול כלים  
- **LangChain4j MCP**: לתמיכה ב-Model Context Protocol  
- **LangChain4j GitHub Models**: לאינטגרציה עם GitHub Models  
- **Spring Boot**: למסגרת היישום והזרקת תלויות  

## רישיון

הפרויקט מורשה תחת רישיון Apache 2.0 - ראה את קובץ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) לפרטים.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.