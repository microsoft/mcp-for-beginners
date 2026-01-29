# MCP Java Client - הדגמת מחשבון

הפרויקט הזה מדגים כיצד ליצור לקוח Java שמתחבר ומתקשר עם שרת MCP (Model Context Protocol). בדוגמה זו, נתחבר לשרת המחשבון מהפרק הראשון ונבצע פעולות מתמטיות שונות.

## דרישות מוקדמות

לפני הרצת הלקוח, יש לבצע את הפעולות הבאות:

1. **הפעלת שרת המחשבון** מהפרק הראשון:
   - נווט לתיקיית שרת המחשבון: `03-GettingStarted/01-first-server/solution/java/`
   - בנייה והרצת שרת המחשבון:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - השרת אמור לפעול בכתובת `http://localhost:8080`

2. **Java 21 או גרסה גבוהה יותר** מותקנת במערכת שלך  
3. **Maven** (כלול דרך Maven Wrapper)

## מהו SDKClient?

`SDKClient` הוא יישום Java שמדגים כיצד:
- להתחבר לשרת MCP באמצעות Server-Sent Events (SSE)  
- לרשום את הכלים הזמינים מהשרת  
- לקרוא לפונקציות מחשבון שונות מרחוק  
- לטפל בתגובות ולהציג תוצאות

## איך זה עובד

הלקוח משתמש במסגרת Spring AI MCP כדי:

1. **להקים חיבור**: יוצר WebFlux SSE לקוח תחבורה להתחברות לשרת המחשבון  
2. **אתחול הלקוח**: מגדיר את לקוח MCP ומקים את החיבור  
3. **גילוי כלים**: מציג את כל פעולות המחשבון הזמינות  
4. **ביצוע פעולות**: קורא לפונקציות מתמטיות שונות עם נתוני דוגמה  
5. **הצגת תוצאות**: מציג את תוצאות כל חישוב

## מבנה הפרויקט

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## תלות מרכזית

הפרויקט משתמש בתלויות המרכזיות הבאות:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

תלות זו מספקת:
- `McpClient` - ממשק הלקוח הראשי  
- `WebFluxSseClientTransport` - תחבורה SSE לתקשורת מבוססת רשת  
- סכמות פרוטוקול MCP וסוגי בקשות/תגובות

## בניית הפרויקט

בנה את הפרויקט באמצעות Maven wrapper:

```cmd
.\mvnw clean install
```

## הרצת הלקוח

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**[!NOTE]**: ודא ששרת המחשבון פועל בכתובת `http://localhost:8080` לפני ביצוע הפקודות.

## מה הלקוח עושה

בעת הרצת הלקוח, הוא יבצע:

1. **חיבור** לשרת המחשבון בכתובת `http://localhost:8080`  
2. **רשימת כלים** - מציג את כל פעולות המחשבון הזמינות  
3. **ביצוע חישובים**:  
   - חיבור: 5 + 3 = 8  
   - חיסור: 10 - 4 = 6  
   - כפל: 6 × 7 = 42  
   - חילוק: 20 ÷ 4 = 5  
   - חזקה: 2^8 = 256  
   - שורש ריבועי: √16 = 4  
   - ערך מוחלט: |-5.5| = 5.5  
   - עזרה: מציג פעולות זמינות

## פלט צפוי

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**[!NOTE]**: ייתכן שתראה אזהרות Maven לגבי תהליכים תלויים בסיום - זה נורמלי באפליקציות ריאקטיביות ואינו מצביע על שגיאה.

## הבנת הקוד

### 1. הגדרת תחבורה  
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```  
יוצר תחבורה מסוג SSE (Server-Sent Events) שמתחברת לשרת המחשבון.

### 2. יצירת הלקוח  
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```  
יוצר לקוח MCP סינכרוני ומאתחל את החיבור.

### 3. קריאת כלים  
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```  
קורא לכלי "add" עם הפרמטרים a=5.0 ו-b=3.0.

## פתרון תקלות

### השרת לא פועל  
אם מתקבלות שגיאות חיבור, ודא ששרת המחשבון מהפרק הראשון פועל:  
```
Error: Connection refused
```  
**פתרון**: הפעל את שרת המחשבון תחילה.

### הפורט כבר בשימוש  
אם הפורט 8080 תפוס:  
```
Error: Address already in use
```  
**פתרון**: עצור יישומים אחרים שמשתמשים בפורט 8080 או שנה את הפורט בשרת.

### שגיאות בנייה  
אם נתקלת בשגיאות בנייה:  
```cmd
.\mvnw clean install -DskipTests
```

## למידה נוספת

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)  
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)  
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.