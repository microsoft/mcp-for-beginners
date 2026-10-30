# מחקר מקרה: חשיפת REST API בניהול API כשרת MCP

Azure API Management, היא שירות שמספק שער על גבי נקודות הקצה של ה-API שלך. האופן שבו זה עובד הוא ש-Azure API Management מתפקד כפרוקסי מול ה-APIים שלך ויכול להחליט מה לעשות עם בקשות נכנסות.

באמצעותו, אתה מוסיף מגוון תכונות כמו:

- **אבטחה**, אתה יכול להשתמש בכל דבר ממפתחות API, JWT ועד זהות מנוהלת.
- **הגבלת קצב (Rate limiting)**, תכונה מצוינת היא היכולת להחליט כמה קריאות יעברו בפרק זמן מסוים. זה עוזר להבטיח שכל המשתמשים יקבלו חוויה טובה וגם שהשירות שלך לא יעמוס בבקשות.
- **קנה מידה ואיזון עומסים**. ניתן להגדיר מספר נקודות קצה כדי לאזן את העומס וגם להחליט כיצד "לאזן את העומס".
- **תכונות AI כמו מטמון סמנטי**, הגבלת טוקנים וניטור טוקנים ועוד. אלו תכונות מצוינות שמשפרות את התגובה וגם מסייעות לך לשלוט בהוצאות הטוקנים. [קרא/י עוד כאן](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## למה MCP + Azure API Management?

פרוטוקול הקשר מודל (Model Context Protocol) הופך במהירות לתקן עבור אפליקציות AI סוכניות ואיך לחשוף כלים ונתונים בצורה עקבית. Azure API Management הוא בחירה טבעית כשצריך "לנהל" APIs. שרתי MCP משולבים לעיתים קרובות עם APIs אחרים כדי לפתור בקשות לכלי למשל. לכן שילוב Azure API Management ו-MCP הגיוני מאוד.

## סקירה כללית

במקרה שימוש זה נלמד כיצד לחשוף נקודות קצה של API כשרת MCP. על ידי כך, נוכל לשלב את נקודות הקצה האלה כחלק מאפליקציה סוכנית וגם לנצל את התכונות של Azure API Management.

## תכונות מרכזיות

- אתה בוחר את שיטות נקודת הקצה שאתה רוצה לחשוף ככלים.
- התכונות הנוספות שאתה מקבל תלויות בהגדרות שאתה מגדיר בחלק המדיניות עבור ה-API שלך. אבל כאן נראה לך איך להוסיף הגבלת קצב.

## שלב מקדים: ייבוא API

אם כבר יש לך API ב-Azure API Management, מצוין, תוכל לדלג על שלב זה. אם לא, בדוק קישור זה, [ייבוא API ל-Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## חשיפת API כשרת MCP

כדי לחשוף את נקודות הקצה של ה-API, נעקוב אחר השלבים הבאים:

1. עבור ל-Portal של Azure והכתובת הבאה <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
עבור למופע Azure API Management שלך.

1. בתפריט השמאלי, בחר APIs > MCP Servers > + יצירת שרת MCP חדש.

1. ב-API, בחר REST API לחשוף כשרת MCP.

1. בחר אחת או יותר פעולות API לחשוף ככלים. אפשר לבחור את כל הפעולות או רק פעולות ספציפיות.

    ![בחר שיטות לחשיפה](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. בחר **Create**.

1. עבור לתפריט **APIs** ו-**MCP Servers**, תראה את הבא:

    ![ראה את שרת ה-MCP בפאנל הראשי](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    שרת ה-MCP נוצר ופעולות ה-API נחשפו ככלים. שרת ה-MCP מפורט בפאנל שרתי MCP. עמודת ה-URL מציגה את נקודת הקצה של שרת ה-MCP שאתה יכול לקרוא לה לצורך בדיקות או בתוך אפליקציית לקוח.

## אפשרות: הגדרת מדיניות

ל-Azure API Management יש את הקונספט המרכזי של מדיניות, שבו אתה מגדיר חוקים שונים לנקודות הקצה שלך כמו הגבלת קצב או מטמון סמנטי. המדיניות נכתבת ב-XML.

כך תוכל להגדיר מדיניות להגבלת קצב עבור שרת MCP שלך:

1. בפורטל, תחת APIs, בחר **MCP Servers**.

1. בחר את שרת ה-MCP שיצרת.

1. בתפריט השמאלי, תחת MCP, בחר **Policies**.

1. בעורך המדיניות, הוסף או ערוך את המדיניות שברצונך להחיל על הכלים של שרת ה-MCP. המדיניות מוגדרת בפורמט XML. לדוגמה, תוכל להוסיף מדיניות להגבלת קריאות לכלי שרת ה-MCP (בדוגמה זו, 5 קריאות לכל 30 שניות לפי כתובת IP של הלקוח). הנה XML שיגרום להגבלת קצב:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    הנה תמונה של עורך המדיניות:

    ![עורך מדיניות](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## נסה את זה

בוא נוודא ששרתי MCP שלנו פועל כפי שמתכוונים.

> [!NOTE]
> Azure API Management כיום חושף את השרת הזה דרך נקודת קצה Streamable
> HTTP `/mcp`. שיטת ההעברה HTTP+SSE `/sse` הוותיקה מוצהרת כמיושנת
> ויש להשתמש בה רק עם לקוחות ישנים.

לשם כך, נשתמש ב-Visual Studio Code ו-GitHub Copilot במצב סוכן. נוסיף את שרת ה-MCP לקובץ *mcp.json*. כך, Visual Studio Code ישמש כלקוח עם יכולות סוכניות ומשתמשי קצה יוכלו להקליד פקודות ולתקשר עם השרת.

בוא נראה איך להוסיף את שרת ה-MCP ב-Visual Studio Code:

1. השתמש בפקודת MCP: **Add Server מ-Command Palette**.

1. כשהתבקש, בחר את סוג השרת: **HTTP (HTTP או Server Sent Events)**.

1. הזן את כתובת ה-Streamable HTTP שמוצגת עבור שרת ה-MCP בניהול API.
    לדוגמה:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. הזן מזהה שרת לבחירתך. זו לא ערך חשוב אבל יעזור לך לזכור מהו מופע השרת הזה.

1. בחר האם לשמור את ההגדרה בהגדרות סביבת העבודה או בהגדרות המשתמש.

    - **הגדרות סביבת עבודה** - קונפיגורציית השרת נשמרת בקובץ `.vscode/mcp.json`, הזמין רק בסביבת העבודה הנוכחית.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **הגדרות משתמש** - קונפיגורציית השרת מתווספת לקובץ *settings.json* הגלובלי שלך וזמינה בכל סביבת עבודה. ההגדרה נראית כך:

      ![הגדרות משתמש](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. יש גם להוסיף כותרת קונפיגורציה כדי להבטיח אימות נכון לעבר Azure API Management. משתמשים בכותרת בשם **Ocp-Apim-Subscription-Key**.

    - כך תוכל להוסיף אותה להגדרות:


    ![הוספת כותרת לאימות](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), תגרום להצגת בקשה להזנת ערך מפתח ה-API שניתן למצוא ב-Azure Portal עבור מופע Azure API Management שלך.

   - להוסיפה במקום ל-*mcp.json* אפשר לעשות זאת כך:

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

### השתמש במצב סוכן

עכשיו כשכולנו מוגדרים בהגדרות או ב-*.vscode/mcp.json*, בוא ננסה.

אמור להיות אייקון כלים כך, שם הכלים החשופים מהשרת שלך מופיעים ברשימה:

![כלים מהשרת](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. לחץ על אייקון הכלים ותראה רשימת כלים כך:

    ![כלים](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. הכנס פקודה בצ׳אט כדי להפעיל את הכלי. לדוגמה, אם בחרת כלי לקבל מידע על הזמנה, תוכל לשאול את הסוכן על הזמנה. הנה דוגמה לפקודה:

    ```text
    get information from order 2
    ```

    כעת יוצג לך אייקון כלים שישאל אם להמשיך לקרוא לכלי. בחר להמשיך להפעיל את הכלי, כעת תראה פלט כך:

    ![תוצאה מהפקודה](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **מה שאתה רואה למעלה תלוי בכלים שהגדרת, אבל הרעיון הוא שאתה מקבל תגובה טקסטואלית כמו למעלה**


## הפניות

כך תוכל ללמוד עוד:

- [מדריך על Azure API Management ו-MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [דוגמה בפייתון: אבטחת שרתי MCP מרוחקים באמצעות Azure API Management (נסיוני)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [מעבדת הרשאות לקוח MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [שימוש בתוסף Azure API Management ל-VS Code לייבוא וניהול APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [הרשמה וגילוי שרתי MCP מרוחקים במרכז Azure API](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [שער AI](https://github.com/Azure-Samples/AI-Gateway) ריפוזיטורי מעולה שמראה יכולות AI רבות עם Azure API Management
- [סדנאות שער AI](https://azure-samples.github.io/AI-Gateway/) מכילות סדנאות בשימוש ב-Azure Portal, דרך מצוינת להתחיל להעריך יכולות AI.

## מה הלאה

- חזרה אל: [סקירת מחקרי מקרה](./README.md)
- הבא: [סוכני נסיעות AI ב-Azure](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->