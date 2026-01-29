# הדגמת סטרימינג HTTP של מחשבון

הפרויקט הזה מדגים סטרימינג HTTP באמצעות Server-Sent Events (SSE) עם Spring Boot WebFlux. הוא מורכב משתי אפליקציות:

- **Calculator Server**: שירות ווב ריאקטיבי שמבצע חישובים ומשדר תוצאות באמצעות SSE  
- **Calculator Client**: אפליקציית לקוח שצורכת את נקודת הקצה של הסטרימינג

## דרישות מוקדמות

- Java 17 ומעלה  
- Maven 3.6 ומעלה  

## מבנה הפרויקט

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## איך זה עובד

1. ה-**Calculator Server** חושף נקודת קצה `/calculate` שמבצעת:  
   - מקבלת פרמטרים בשאילתה: `a` (מספר), `b` (מספר), `op` (פעולה)  
   - פעולות נתמכות: `add`, `sub`, `mul`, `div`  
   - מחזירה Server-Sent Events עם התקדמות החישוב והתוצאה  

2. ה-**Calculator Client** מתחבר לשרת ומבצע:  
   - שולח בקשה לחישוב `7 * 5`  
   - צורך את תגובת הסטרימינג  
   - מדפיס כל אירוע למסוף  

## הפעלת האפליקציות

### אפשרות 1: שימוש ב-Maven (מומלץ)

#### 1. הפעלת ה-Calculator Server

פתח טרמינל ונווט לתיקיית השרת:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

השרת יפעל בכתובת `http://localhost:8080`

תראה פלט דומה ל:  
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. הפעלת ה-Calculator Client

פתח **טרמינל חדש** ונווט לתיקיית הלקוח:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

הלקוח יתחבר לשרת, יבצע את החישוב ויציג את תוצאות הסטרימינג.

### אפשרות 2: שימוש ב-Java ישירות

#### 1. קומפילציה והפעלה של השרת:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. קומפילציה והפעלה של הלקוח:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## בדיקת השרת ידנית

ניתן גם לבדוק את השרת באמצעות דפדפן או curl:

### שימוש בדפדפן:  
גש לכתובת: `http://localhost:8080/calculate?a=10&b=5&op=add`

### שימוש ב-curl:  
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## פלט צפוי

בעת הרצת הלקוח, תראה פלט סטרימינג דומה ל:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## פעולות נתמכות

- `add` - חיבור (a + b)  
- `sub` - חיסור (a - b)  
- `mul` - כפל (a * b)  
- `div` - חילוק (a / b, מחזיר NaN אם b = 0)  

## תיעוד API

### GET /calculate

**פרמטרים:**  
- `a` (נדרש): מספר ראשון (double)  
- `b` (נדרש): מספר שני (double)  
- `op` (נדרש): פעולה (`add`, `sub`, `mul`, `div`)  

**תגובה:**  
- Content-Type: `text/event-stream`  
- מחזיר Server-Sent Events עם התקדמות החישוב והתוצאה  

**בקשת דוגמה:**  
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**תגובה לדוגמה:**  
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## פתרון תקלות

### בעיות נפוצות

1. **פורט 8080 כבר בשימוש**  
   - עצור כל אפליקציה אחרת שמשתמשת בפורט 8080  
   - או שנה את פורט השרת בקובץ `calculator-server/src/main/resources/application.yml`  

2. **חיבור נדחה**  
   - ודא שהשרת רץ לפני הפעלת הלקוח  
   - בדוק שהשרת התחיל בהצלחה על פורט 8080  

3. **בעיות בשמות פרמטרים**  
   - הפרויקט כולל קונפיגורציית קומפילציה של Maven עם הדגל `-parameters`  
   - אם נתקלת בבעיות בקישור פרמטרים, ודא שהפרויקט נבנה עם הקונפיגורציה הזו  

### עצירת האפליקציות

- לחץ `Ctrl+C` בטרמינל שבו רצה כל אפליקציה  
- או השתמש בפקודה `mvn spring-boot:stop` אם רצה כרקע  

## טכנולוגיות בשימוש

- **Spring Boot 3.3.1** - מסגרת אפליקציה  
- **Spring WebFlux** - מסגרת ווב ריאקטיבית  
- **Project Reactor** - ספריית סטרימינג ריאקטיבית  
- **Netty** - שרת I/O לא חוסם  
- **Maven** - כלי בנייה  
- **Java 17+** - שפת תכנות  

## צעדים הבאים

נסה לשנות את הקוד כדי:  
- להוסיף פעולות מתמטיות נוספות  
- לכלול טיפול בשגיאות עבור פעולות לא חוקיות  
- להוסיף רישום בקשות/תגובות  
- לממש אימות  
- להוסיף בדיקות יחידה

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.