# חקר מקרה: חשיפת REST API ב-API Management כשרת MCP

Azure API Management הוא שירות שמספק שער (Gateway) מעל נקודות הקצה של ה-API שלך. השירות פועל כפרוקסי מול ה-APIs שלך ויכול להחליט מה לעשות עם בקשות נכנסות.

באמצעותו, ניתן להוסיף מגוון רחב של תכונות כמו:

- **אבטחה** - ניתן להשתמש בכלים כמו מפתחות API, JWT ועד זהות מנוהלת.
- **הגבלת קצב** - תכונה נהדרת שמאפשרת להחליט כמה קריאות עוברות בפרק זמן מסוים. זה עוזר להבטיח חוויית משתמש טובה ולמנוע עומס יתר על השירות.
- **סקיילינג ואיזון עומסים** - ניתן להגדיר מספר נקודות קצה לאיזון עומסים ולהחליט כיצד לבצע את האיזון.
- **תכונות AI כמו קאשינג סמנטי**, הגבלת טוקנים, ניטור טוקנים ועוד. תכונות אלו משפרות את התגובה ועוזרות לנהל את השימוש בטוקנים. [קרא עוד כאן](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## למה MCP + Azure API Management?

Model Context Protocol הופך במהירות לסטנדרט עבור אפליקציות AI סוכניות ולחשיפת כלים ונתונים בצורה עקבית. Azure API Management הוא בחירה טבעית כשצריך "לנהל" APIs. שרתי MCP משתלבים לעיתים קרובות עם APIs אחרים כדי לפתור בקשות לכלים, ולכן השילוב בין Azure API Management ו-MCP הוא הגיוני.

## סקירה כללית

במקרה שימוש זה נלמד כיצד לחשוף נקודות קצה של API כשרת MCP. על ידי כך, ניתן לשלב בקלות את הנקודות הללו כחלק מאפליקציה סוכנית תוך ניצול התכונות של Azure API Management.

## תכונות עיקריות

- ניתן לבחור את שיטות הנקודות שברצונך לחשוף ככלים.
- התכונות הנוספות שתוכל לקבל תלויות במה שתגדיר בסעיף המדיניות של ה-API. כאן נראה כיצד להוסיף הגבלת קצב.

## שלב מקדים: ייבוא API

אם כבר יש לך API ב-Azure API Management, מצוין, תוכל לדלג על שלב זה. אם לא, עיין בקישור הבא: [ייבוא API ל-Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## חשיפת API כשרת MCP

כדי לחשוף את נקודות הקצה של ה-API, בצע את השלבים הבאים:

1. היכנס ל-Azure Portal בכתובת הבאה: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   נווט למופע ה-API Management שלך.

1. בתפריט השמאלי, בחר **APIs > MCP Servers > + Create new MCP Server**.

1. בחר REST API שברצונך לחשוף כשרת MCP.

1. בחר פעולה אחת או יותר של ה-API שברצונך לחשוף ככלים. ניתן לבחור את כל הפעולות או פעולות ספציפיות בלבד.

    ![בחירת שיטות לחשיפה](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. בחר **Create**.

1. נווט לאפשרות התפריט **APIs** ו-**MCP Servers**, ותראה את המסך הבא:

    ![צפייה בשרת MCP בחלון הראשי](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    שרת ה-MCP נוצר ופעולות ה-API נחשפו ככלים. שרת ה-MCP מופיע בחלונית MCP Servers. עמודת ה-URL מציגה את נקודת הקצה של שרת ה-MCP שניתן לקרוא לה לצורך בדיקה או שימוש באפליקציית לקוח.

## אופציונלי: הגדרת מדיניות

ל-Azure API Management יש את הקונספט המרכזי של מדיניות, שבו ניתן להגדיר חוקים שונים עבור נקודות הקצה, כמו הגבלת קצב או קאשינג סמנטי. המדיניות נכתבת בפורמט XML.

כך ניתן להגדיר מדיניות להגבלת קצב עבור שרת ה-MCP:

1. בפורטל, תחת APIs, בחר **MCP Servers**.

1. בחר את שרת ה-MCP שיצרת.

1. בתפריט השמאלי, תחת MCP, בחר **Policies**.

1. בעורך המדיניות, הוסף או ערוך את המדיניות שברצונך להחיל על הכלים של שרת ה-MCP. המדיניות מוגדרת בפורמט XML. לדוגמה, ניתן להוסיף מדיניות להגבלת קריאות לכלים של שרת ה-MCP (בדוגמה זו, 5 קריאות לכל 30 שניות לכל כתובת IP של לקוח). להלן דוגמת XML שתגרום להגבלת קצב:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    להלן תמונה של עורך המדיניות:

    ![עורך מדיניות](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## בדיקה

בואו נוודא ששרת ה-MCP שלנו פועל כראוי.

לצורך כך, נשתמש ב-Visual Studio Code וב-GitHub Copilot במצב Agent. נוסיף את שרת ה-MCP לקובץ *mcp.json*. על ידי כך, Visual Studio Code יפעל כלקוח עם יכולות סוכניות, ומשתמשי הקצה יוכלו להקליד פקודות ולתקשר עם השרת.

כך ניתן להוסיף את שרת ה-MCP ב-Visual Studio Code:

1. השתמש בפקודה **MCP: Add Server** מתוך ה-Command Palette.

1. כאשר תתבקש, בחר את סוג השרת: **HTTP (HTTP or Server Sent Events)**.

1. הזן את כתובת ה-URL של שרת ה-MCP ב-API Management. לדוגמה: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (לנקודת קצה SSE) או **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (לנקודת קצה MCP). שים לב להבדל בין הפרוטוקולים `/sse` או `/mcp`.

1. הזן מזהה שרת לבחירתך. ערך זה אינו חשוב במיוחד, אך הוא יעזור לך לזכור מהו מופע השרת.

1. בחר אם לשמור את ההגדרה בהגדרות סביבת העבודה או בהגדרות המשתמש.

  - **הגדרות סביבת עבודה** - ההגדרה נשמרת בקובץ .vscode/mcp.json הזמין רק בסביבת העבודה הנוכחית.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    או אם תבחר ב-HTTP כפרוטוקול, זה ייראה מעט שונה:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **הגדרות משתמש** - ההגדרה מתווספת לקובץ *settings.json* הגלובלי שלך וזמינה בכל סביבות העבודה. ההגדרה נראית כך:

    ![הגדרת משתמש](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. יש להוסיף גם כותרת (header) כדי לוודא שהאימות מול Azure API Management מתבצע כראוי. נעשה שימוש בכותרת בשם **Ocp-Apim-Subscription-Key**.

    - כך ניתן להוסיף אותה להגדרות:

    ![הוספת כותרת לאימות](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). פעולה זו תגרום להצגת בקשה להזנת ערך מפתח ה-API, שניתן למצוא ב-Azure Portal עבור מופע ה-Azure API Management שלך.

   - כדי להוסיף אותה ל-*mcp.json*, ניתן לעשות זאת כך:

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

### שימוש במצב Agent

כעת הכל מוגדר, בין אם בהגדרות או בקובץ *.vscode/mcp.json*. בואו ננסה זאת.

אמור להופיע סמל כלים שבו רשומים הכלים שנחשפו מהשרת שלך:

![כלים מהשרת](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. לחץ על סמל הכלים ותראה רשימת כלים כמו זו:

    ![כלים](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. הזן פקודה בצ'אט כדי להפעיל את הכלי. לדוגמה, אם בחרת בכלי לקבלת מידע על הזמנה, תוכל לשאול את הסוכן על הזמנה. להלן דוגמת פקודה:

    ```text
    get information from order 2
    ```

    כעת תוצג לך אפשרות להפעיל את הכלי. בחר להמשיך, ותראה פלט כמו זה:

    ![תוצאה מהפקודה](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **מה שתראה תלוי בכלים שהגדרת, אך הרעיון הוא שתקבל תגובה טקסטואלית כמו זו.**

## מקורות

כך תוכל ללמוד עוד:

- [מדריך על Azure API Management ו-MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [דוגמת Python: אבטחת שרתי MCP מרוחקים באמצעות Azure API Management (ניסיוני)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [מעבדה לאישור לקוח MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [שימוש בתוסף Azure API Management עבור VS Code לייבוא וניהול APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [רישום וגילוי שרתי MCP מרוחקים ב-Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) מאגר נהדר שמציג יכולות AI רבות עם Azure API Management
- [סדנאות AI Gateway](https://azure-samples.github.io/AI-Gateway/) מכיל סדנאות באמצעות Azure Portal, דרך מצוינת להתחיל להעריך יכולות AI.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.