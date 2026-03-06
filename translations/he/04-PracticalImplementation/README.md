# מימוש מעשי

[![כיצד לבנות, לבדוק ולפרוס אפליקציות MCP עם כלים וזרימות עבודה אמיתיות](../../../translated_images/he/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(לחצו על התמונה למעלה לצפייה בסרטון של השיעור)_

המימוש המעשי הוא המקום שבו כוחו של פרוטוקול הקשר למודל (MCP) הופך למוחשי. בעוד שהבנת התיאוריה והארכיטקטורה שמאחורי MCP חשובה, הערך האמיתי מתגלה כאשר אתם מיישמים את המושגים הללו כדי לבנות, לבדוק ולפרוס פתרונות הפותרים בעיות מהעולם האמיתי. פרק זה גשר על הפער בין ידע קונספטואלי לפיתוח מעשי, ומכוון אתכם בתהליך הבאת אפליקציות מבוססות MCP לחיים.

בין אם אתם מפתחים עוזרים חכמים, משבצים AI בזמני עבודה עסקיים, או בונים כלים מותאמים לעיבוד נתונים, MCP מספק בסיס גמיש. העיצוב הלא תלוי בשפה וה-SDKs הרשמיים לשפות תכנות פופולריות מהווים נגישות למגוון רחב של מפתחים. באמצעות ניצול SDKs אלו, תוכלו ליצור אבטיפוס במהירות, לחזור על הפיתוח ולהגדיל את הפתרונות שלכם בפלטפורמות וסביבות שונות.

בקטעים הבאים, תמצאו דוגמאות מעשיות, קוד לדוגמה ואסטרטגיות פריסה המבקשות להדגים כיצד ליישם MCP ב-C#, Java עם Spring, TypeScript, JavaScript, ו-Python. תלמדו גם כיצד לאבחן ולבדוק את שרתי MCP שלכם, לנהל APIs ולפרוס פתרונות לענן באמצעות Azure. משאבי התרגול האלו נועדו להאיץ את הלמידה ולעזור לכם לבנות בביטחון אפליקציות MCP עמידות ומוכנות לפרודקשן.

## סקירה כללית

שיעור זה מתמקד בהיבטים מעשיים של יישום MCP בכמה שפות תכנות. נחקור כיצד להשתמש ב-SDKs של MCP ב-C#, Java עם Spring, TypeScript, JavaScript, ו-Python כדי לבנות אפליקציות חזקות, לאבחן ולבדוק שרתי MCP, וליצור משאבים, הנחיות, וכלים לשימוש חוזר.

## מטרות הלמידה

בסיום השיעור תגיעו ליכולות:

- ליישם פתרונות MCP באמצעות SDKs רשמיים בשפות תכנות שונות
- לאבחן ולבדוק שרתי MCP בצורה שיטתית
- ליצור ולהשתמש בתכונות שרת (משאבים, הנחיות, וכלים)
- לעצב זרימות עבודה יעילות ל-MCP למשימות מורכבות
- לייעל מימושי MCP עבור ביצועים ואמינות

## משאבים רשמיים של SDK

פרוטוקול הקשר למודל מציע SDKs רשמיים לשפות רבות (בהתאם ל-[מפרט MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java עם Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **הערה:** דורש תלות ב-[Project Reactor](https://projectreactor.io). (ראו [דיון מס' 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## עבודה עם SDKs של MCP

קטע זה מספק דוגמאות מעשיות ליישום MCP בכמה שפות תכנות. תוכלו למצוא קודי דוגמה בתיקיית `samples` הממוינת לפי שפה.

### דוגמאות זמינות

המאגר כולל [מימושי דוגמה](../../../04-PracticalImplementation/samples) בשפות הבאות:

- [C#](./samples/csharp/README.md)
- [Java עם Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

כל דוגמה מדגימה מושגי מפתח ודפוסי מימוש ל-MCP בשפה ובמערכת האקולוגית הספציפית.

### מדריכים מעשיים

מדריכים נוספים למימוש מעשי של MCP:

- [פגינציה וקבוצות תוצאות גדולות](./pagination/README.md) - טיפול בפגינציה מבוססת מצביעים לכלים, משאבים ומאגרי נתונים גדולים

## תכונות שרת מרכזיות

שרתי MCP יכולים לממש כל צירוף מהתכונות הבאות:

### משאבים

משאבים מספקים הקשר ונתונים למשתמש או למודל AI לשימוש:

- מאגרי מסמכים
- בסיסי ידע
- מקורות נתונים מובנים
- מערכות קבצים

### הנחיות

הנחיות הן הודעות וזרימות עבודה בתבנית עבור משתמשים:

- תבניות שיחה מוגדרות מראש
- דפוסי אינטראקציה מונחים
- מבני דיאלוג מיוחדים

### כלים

כלים הם פונקציות שהמודל AI מבצע:

- כלי עיבוד נתונים
- אינטגרציות API חיצוניות
- יכולות חישוביות
- פונקציונליות חיפוש

## דוגמאות מימוש: מימוש C#

מאגר ה-SDK הרשמי של C# כולל מספר דוגמאות מימוש המדגימות היבטים שונים של MCP:

- **לקוח MCP בסיסי**: דוגמה פשוטה המראה כיצד ליצור לקוח MCP ולקרוא לכלים
- **שרת MCP בסיסי**: מימוש שרת מינימלי עם רישום כלי בסיסי
- **שרת MCP מתקדם**: שרת מלא תכונות עם רישום כלים, אימות וניהול שגיאות
- **אינטגרציה עם ASP.NET**: דוגמאות המדגימות אינטגרציה עם ASP.NET Core
- **דפוסי מימוש כלים**: דפוסים שונים למימוש כלים עם רמות מורכבות שונות

ממשק ה-MCP ל-C# נמצא בבחינה וה-API עלול להשתנות. נשדרג את הבלוג הזה בהתפתחות ה-SDK.

### תכונות מרכזיות

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- בניית [שרת MCP ראשון](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

לדוגמאות מימוש מלאות של C#, בקרו ב-[מאגר דוגמאות SDK רשמי ל-C#](https://github.com/modelcontextprotocol/csharp-sdk)

## דוגמא למימוש: מימוש Java עם Spring

ל-SDK של Java עם Spring יש אפשרויות מימוש MCP חזקות עם תכונות ברמת ארגון.

### תכונות מרכזיות

- אינטגרציה עם Spring Framework
- בטיחות טיפוסים חזקה
- תמיכה בתכנות תגובתי
- ניהול שגיאות מקיף

לדוגמת מימוש מלאה של Java עם Spring, ראו [דוגמת Java עם Spring](samples/java/containerapp/README.md) בתיקיית הדוגמאות.

## דוגמא למימוש: מימוש JavaScript

ה-SDK של JavaScript מספק גישה קלה וגמישה למימוש MCP.

### תכונות מרכזיות

- תמיכה ב-Node.js וראש דפדפן
- API מבוסס הבטחות (promises)
- אינטגרציה פשוטה עם Express ומסגרות נוספות
- תמיכה ב-WebSocket לבידור זרם

לדוגמת מימוש מלאה של JavaScript, ראו [דוגמת JavaScript](samples/javascript/README.md) בתיקיית הדוגמאות.

## דוגמא למימוש: מימוש Python

ה-SDK של Python מציע גישה פייתונית למימוש MCP עם אינטגרציות מצוינות למסגרות ML.

### תכונות מרכזיות

- תמיכה ב-Async/await עם asyncio
- אינטגרציה עם FastAPI
- רישום כלים פשוט
- אינטגרציה טבעית עם ספריות ML פופולריות

לדוגמת מימוש מלאה של Python, ראו [דוגמת Python](samples/python/README.md) בתיקיית הדוגמאות.

## ניהול API

ניהול API של Azure הוא תשובה מצוינת לשאלה כיצד להגן על שרתי MCP. הרעיון הוא לשים מופע של ניהול API של Azure מול שרת ה-MCP שלך ולתת לו לטפל בתכונות שאתם צפויים לרצות, כגון:

- הגבלת קצב
- ניהול אסימונים
- ניטור
- איזון עומסים
- אבטחה

### דוגמת Azure

הנה דוגמת Azure שעושה בדיוק את זה, כלומר [יצירת שרת MCP ואבטחתו עם ניהול API של Azure](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

ראו כיצד מתבצע תהליך האישור בתמונה למטה:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

בתמונה שלמעלה, מתרחשים הדברים הבאים:

- מתבצעת אימות/הרשאה באמצעות Microsoft Entra.
- ניהול API של Azure משמש כשער ומשתמש במדיניות כדי לכוון ולנהל תנועה.
- Azure Monitor רושם את כל הבקשות לניתוח נוסף.

#### תהליך הרשאה

נבחן את תהליך ההרשאה ביתר פירוט:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### מפרט הרשאת MCP

למידע נוסף על [מפרט הרשאת MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## פריסת שרת MCP מרוחק ב-Azure

בואו נראה אם נוכל לפרוס את הדוגמה שהזכרנו קודם:

1. שכפול המאגר

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. רישום ספק השירות `Microsoft.App`.

   - אם אתם משתמשים ב-Azure CLI, הריצו `az provider register --namespace Microsoft.App --wait`.
   - אם אתם משתמשים ב-Azure PowerShell, הריצו `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. לאחר מכן הריצו `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` לאחר זמן מה כדי לבדוק האם הרישום הושלם.

1. הריצו את הפקודה [azd](https://aka.ms/azd) הבאה כדי לספק את שירות ניהול ה-API, אפליקציית הפונקציה (עם קוד) ואת כל משאבי Azure הנדרשים האחרים

    ```shell
    azd up
    ```

    פקודה זו אמורה לפרוס את כל משאבי הענן ב-Azure

### בדיקת השרת שלכם עם MCP Inspector

1. בחלון טרמינל חדש, התקינו והריצו את MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    תראו ממשק דומה ל:

    ![Connect to Node inspector](../../../translated_images/he/connect.141db0b2bd05f096.webp)

1. לחצו CTRL כדי לטעון את אפליקציית הרשת MCP Inspector מה-URL שמוצג על ידי האפליקציה (לדוגמה [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. הגדרו את סוג ההעברה ל-`SSE`
1. הגדרו את ה-URL לנקודת הקצה SSE של ניהול ה-API שלכם שמופיע לאחר `azd up` ולחצו **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **רשימת כלים**. לחצו על כלי ו**הריצו את הכלי**.

אם כל השלבים הצליחו, אתם אמורים להיות מחוברים עכשיו לשרת MCP והצלחתם לקרוא לכלי.

## שרתי MCP ל-Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): סט מאגרים זה מהווה תבנית התחלה מהירה לבניית ופריסת שרתי MCP מרוחקים מותאמים אישית באמצעות Azure Functions עם Python, C# .NET או Node/TypeScript.

הדוגמאות מספקות פתרון מלא המאפשר למפתחים:

- בנייה והרצה מקומית: פיתוח ואבחון שרת MCP במכונה מקומית
- פריסה ל-Azure: פריסה קלה לענן באמצעות פקודת azd up פשוטה
- חיבור מלקוחות: חיבור לשרת MCP מלקוחות שונים כולל מצב סוכן Copilot של VS Code וכלי MCP Inspector

### תכונות מרכזיות

- אבטחה כברירת מחדל: שרת MCP מוגן באמצעות מפתחות ו-HTTPS
- אפשרויות אימות: תמיכה ב-OAuth באמצעות אימות מובנה ו/או ניהול API
- בידוד רשת: מאפשר בידוד רשת באמצעות רשתות וירטואליות של Azure (VNET)
- ארכיטקטורה ללא שרת: משתמש ב-Azure Functions לביצוע סקלבילי ומונחה אירועים
- פיתוח מקומי: תמיכה מקיפה בפיתוח ואבחון מקומי
- פריסה פשוטה: תהליך פריסה חלק ל-Azure

המאגר כולל את כל קבצי התצורה, קוד המקור והגדרות התשתית הנדרשים להתחלה מהירה עם מימוש שרת MCP מוכן לפרודקשן.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) – מימוש דוגמה של MCP באמצעות Azure Functions עם Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – מימוש דוגמה של MCP באמצעות Azure Functions עם C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – מימוש דוגמה של MCP באמצעות Azure Functions עם Node/TypeScript.

## נקודות מרכזיות להסכמה

- SDKs של MCP מספקים כלים ספציפיים לשפות למימוש פתרונות MCP חזקים
- תהליך האבחון והבדיקה קריטי ליישומים אמינים של MCP
- תבניות הנחייה לשימוש חוזר מאפשרות אינטראקציות אחידות עם AI
- זרימות עבודה מתוכננות היטב יכולות לתזמר משימות מורכבות באמצעות כלים רבים
- יישום פתרונות MCP דורש התייחסות לאבטחה, ביצועים וניהול שגיאות

## תרגיל

עצבו זרימת עבודה מעשית ל-MCP שמתמודדת עם בעיה אמיתית בתחום שלכם:

1. זיהוי 3-4 כלים שיהיו שימושיים לפתרון הבעיה הזו
2. יצירת דיאגרם זרימת עבודה המציג כיצד כלים אלו מתקשרים זה עם זה
3. מימוש גרסה בסיסית של אחד הכלים בשפת התכנות המועדפת עליכם
4. יצירת תבנית הנחייה שתעזור למודל להשתמש בכלי שלכם באופן אפקטיבי

## משאבים נוספים

---

## מה הלאה

הבא: [נושאים מתקדמים](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדייק, יש לקחת בחשבון שתירגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->