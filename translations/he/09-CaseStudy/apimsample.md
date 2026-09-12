# מחקר מקרה: חשיפת REST API בניהול API כשרת MCP

Azure API Management, היא שירות המספק שער על גבי נקודות הקצה של ה-API שלך. הדרך שבה זה עובד היא ש-Azure API Management פועל כמו פרוקסי מול ה-APIs שלך ויכול להחליט מה לעשות עם הבקשות הנכנסות.

באמצעותו, אתה מוסיף מגוון רחב של תכונות כגון:

- **אבטחה**, ניתן להשתמש בכל דבר ממפתחות API, JWT ועד לזהות מנוהלת.
- **הגבלת קצב**, תכונה נהדרת היא היכולת להחליט כמה קריאות יעברו במשך יחידת זמן מסוימת. זה עוזר להבטיח שלכל המשתמשים תהיה חווית שימוש טובה וגם שהשירות שלך לא יעמוס עם בקשות.
- **קנה מידה ואיזון עומסים**. ניתן להגדיר מספר נקודות קצה כדי לאזן את העומס וגם להחליט כיצד "לאזן את העומס".
- **תכונות בינה מלאכותית כמו מטמון סמנטי**, הגבלת טוקנים ומעקב אחר טוקנים ועוד. אלו תכונות מצוינות המשפרות את המהירות וגם עוזרות לך לעקוב אחרי ההוצאה על טוקנים. [קרא עוד כאן](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## למה MCP + Azure API Management?

פרוטוקול Model Context Protocol הופך במהירות לסטנדרט לאפליקציות AI סוכניות ואופן החשיפה של כלים ונתונים בצורה עקבית. Azure API Management הוא בחירה טבעית כאשר צריך "לנהל" APIs. שרתי MCP לעיתים משתלבים עם APIs אחרים כדי לפתור בקשות לכלי, למשל. לכן שילוב של Azure API Management ו-MCP הגיוני מאוד.

## מבט כללי

במקרה שימוש ספציפי זה נלמד כיצד לחשוף נקודות קצה של API כשרת MCP. על ידי כך, נוכל להפוך נקודות קצה אלו לחלק מאפליקציה סוכנית תוך ניצול התכונות של Azure API Management.

## תכונות מפתח

- אתה בוחר את פעולות הנקודות קצה שברצונך לחשוף ככלים.
- התכונות הנוספות שתקבלות תלויות במה שאתה מגדיר במדור המדיניות של ה-API שלך. כאן נראה איך ניתן להוסיף הגבלת קצב.

## שלב מקדים: ייבוא API

אם כבר יש לך API ב-Azure API Management, מצוין, אז תוכל לדלג על שלב זה. אם לא, בדוק קישור זה, [ייבוא API ל-Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## חשיפת API כשרת MCP

כדי לחשוף את נקודות הקצה של ה-API, נעקוב אחר השלבים הבאים:

1. נווט לפורטל Azure לכתובת <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
נווט למופע ניהול ה-API שלך.

1. בתפריט השמאלי, בחר APIs > MCP Servers > + יצירת שרת MCP חדש.

1. ב-API, בחר REST API שברצונך לחשוף כשרת MCP.

1. בחר פעולה אחת או יותר של ה-API לחשיפה ככלים. תוכל לבחור בכל הפעולות או רק פעולות ספציפיות.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. בחר **צור**.

1. נווט לאפשרות בתפריט **APIs** ו-**MCP Servers**, אמור להופיע כפי שמוצג:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    שרת MCP נוצר והפעולות של ה-API נחשפו ככלים. שרת MCP מופיע בלשונית שרתי MCP. עמודת ה-URL מציגה את כתובת נקודת הקצה של שרת MCP שניתן לקרוא לה לבדיקה או מתוך אפליקציית לקוח.

## אופציונלי: הגדרת מדיניות

ל-Azure API Management יש את המושג המרכזי של מדיניות שבה מגדירים חוקים שונים לנקודות הקצה שלך כמו לדוגמה הגבלת קצב או מטמון סמנטי. מדיניות זו מוגדרת ב-XML.

כך תוכל להגדיר מדיניות להגבלת קצב בשרת MCP שלך:

1. בפורטל, תחת APIs, בחר **MCP Servers**.

1. בחר את שרת ה-MCP שיצרת.

1. בתפריט השמאלי, תחת MCP, בחר **Policies**.

1. בעורך המדיניות, הוסף או ערוך את המדיניות שברצונך להחיל על כלים של שרת MCP. המדיניות מוגדרת בפורמט XML. לדוגמה, ניתן להוסיף מדיניות להגבלת קריאות לכלי השרת (בדוגמה זו, 5 קריאות ל-30 שניות לכל כתובת IP של לקוח). הנה XML שיגרום להגבלת קצב:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    הנה תמונה של עורך המדיניות:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## נסה זאת

נוודא ששרת ה-MCP שלנו פועל כפי שנדרש.

> [!NOTE]
> Azure API Management חושף כעת שרת זה דרך נקודת הקצה Streamable
> HTTP `/mcp`. הבניין הישן HTTP+SSE `/sse` מוצהב
> ויש להשתמש בו רק עם לקוחות ישנים.

לשם כך, נשתמש ב-Visual Studio Code וב-GitHub Copilot במצב סוכן. נוסיף את שרת MCP לקובץ *mcp.json*. כך Visual Studio Code יפעל כלקוח עם יכולות סוכניות ומשתמשי הקצה יוכלו להקליד פקודה ולתקשר עם השרת.

נראה כיצד, להוסיף את שרת ה-MCP ב-Visual Studio Code:

1. השתמש בפקודת MCP: **Add Server מתוך פלטת הפקודות**.

1. כאשר תתבקש, בחר את סוג השרת: **HTTP (HTTP או Server Sent Events)**.

1. הזן את כתובת ה-URL של ה-HTTP Streamable שמוצגת לשרת MCP בניהול API.
    למשל:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. הזן מזהה שרת לבחירתך. זהו ערך לא חשוב אך יעזור לך לזכור מהו מופע השרת הזה.

1. בחר האם לשמור את ההגדרות בהגדרות סביבת העבודה שלך או בהגדרות המשתמש.

  - **הגדרות סביבת עבודה** - הגדרות השרת נשמרות בקובץ .vscode/mcp.json הזמין רק בסביבת העבודה הנוכחית.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **הגדרות משתמש** - הגדרות השרת מתווספות לקובץ הגלובלי *settings.json* וזמינות בכל סביבת עבודה. ההגדרות נראות כך:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. יש להוסיף גם הגדרה, כותרת כדי לוודא שהאימות מתבצע כראוי כלפי Azure API Management. משתמשים בכותרת בשם **Ocp-Apim-Subscription-Key**.

    - הנה איך להוסיף זאת להגדרות:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), זה יגרום להצגת פקודה לשאלה על ערך מפתח ה-API שניתן למצוא בפורטל Azure עבור מופע Azure API Management שלך.

   - כדי להוסיף זאת ל-*mcp.json* במקום, אפשר להוסיף כך:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### שימוש במצב סוכן

עכשיו כל ההגדרות בוצעו, בין אם בהגדרות או בקובץ *.vscode/mcp.json*. בוא ננסה.

אמור להופיע סמל כלים כפי שמוצג, שבו הכלים החשופים מהשרת שלך מופיעים ברשימה:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. לחץ על סמל הכלים ותראה רשימת כלים כמו כך:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. הזן פקודה בשיחה כדי להפעיל את הכלי. לדוגמה, אם בחרת כלי לקבלת מידע על הזמנה, אתה יכול לשאול את הסוכן על הזמנה. הנה דוגמת פקודה:

    ```text
    get information from order 2
    ```

    כעת יוצג סמל כלים שיבקש ממך להמשיך ולהפעיל את הכלי. בחר להמשיך בפעולה, ותראה פלט כזה:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **מה שתראה למעלה תלוי בכלים שהגדרת, אבל הרעיון הוא שתקבל תגובה טקסטואלית כפי שמוצג**


## הפניות

הנה דרכים ללמוד עוד:

- [מדריך על Azure API Management ו-MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [דוגמת Python: אבטחת שרתי MCP מרוחקים עם Azure API Management (במצב ניסיוני)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [מעבדת הרשאת לקוח MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [שימוש בתוסף Azure API Management ל-VS Code ליבוא וניהול APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [רישום וגילוי שרתי MCP מרוחקים במרכז Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) מאגר נפלא שמראה יכולות רבות של AI עם Azure API Management
- [סדנאות AI Gateway](https://azure-samples.github.io/AI-Gateway/) מכילות סדנאות באמצעות פורטל Azure, דרך נהדרת להתחיל להעריך יכולות AI.

## מה הלאה

- חזרה אל: [סקירת מחקרי מקרה](./README.md)
- הבא: [סוכני נסיעות בינה מלאכותית ב-Azure](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->