# פריסת שרתי MCP

> [!NOTE]
> דוגמאות הגדרה המשתמשות ב-`/sse` נקודת קצה מפנות לטרנספורט הישן HTTP+SSE.
> שרתי MCP `2026-07-28` מרוחקים משתמשים ב-Streamable HTTP, בדרך כלל בנקודת קצה שהוגדרה על ידי השרת כמו `/mcp`.


פריסת שרת ה-MCP שלך מאפשרת לאחרים לגשת לכלים ולמשאבים שלו מעבר לסביבה המקומית שלך. ישנן כמה אסטרטגיות פריסה שיש לקחת בחשבון, בהתאם לדרישות שלך לגבי סקלאביליות, מהימנות ונוחות ניהול. למטה תמצא הדרכה לפריסת שרתי MCP מקומית, במיכלים ובענן.

## מבוא

שיעור זה מכסה כיצד לפרוס את אפליקציית שרת ה-MCP שלך.

## מטרות הלמידה

בסיום שיעור זה תוכל:

- להעריך גישות פריסה שונות.
- לפרוס את האפליקציה שלך.

## פיתוח ופריסה מקומית

אם השרת שלך מיועד לשימוש על מחשב של המשתמשים, תוכל לעקוב אחרי השלבים הבאים:

1. **הורד את השרת**. אם לא כתבת את השרת, הורד אותו קודם כל למחשב שלך.
1. **הפעל את תהליך השרת**: הרץ את אפליקציית שרת ה-MCP שלך

עבור SSE (לא נדרש לשרת מסוג stdio)

1. **הגדר רשת**: ודא שהשרת נגיש בנמל הצפוי
1. **חבר לקוחות**: השתמש בכתובות חיבור מקומיות כמו `http://localhost:3000`

## פריסת ענן

ניתן לפרוס שרתי MCP בפלטפורמות ענן שונות:

- **פונקציות ללא שרת (Serverless Functions)**: פרוס שרתי MCP קלים כסטודנט פונקציות חסרות שרת
- **שירותי מכולות**: השתמש בשירותים כמו Azure Container Apps, AWS ECS, או Google Cloud Run
- **קוברנטיס**: פרוס ונהל שרתי MCP באשכולות Kubernetes לזמינות גבוהה

### דוגמה: Azure Container Apps

Azure Container Apps תומך בפריסת שרתי MCP. זה עדיין בעבודה וטרם תומך אלא שרתי SSE.

הנה איך תוכל לעשות זאת:

1. שכפל מאגר:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. הרץ את זה באופן מקומי לבדיקה:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. כדי לנסות את זה מקומית, צור קובץ *mcp.json* בתיקיית *.vscode* והוסף את התוכן הבא:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  לאחר שהשרת SSE הופעל, תוכל ללחוץ על סמל ההפעלה בקובץ ה-JSON, וכעת תראה שכלים בשרת נבחרים על ידי GitHub Copilot, ראה את סמל הכלי.

1. לפריסה, הרץ את הפקודה הבאה:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

הנה לך, פרוס מקומית, פרוס ל-Azure דרך השלבים האלו.

## משאבים נוספים

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## מה הלאה

- הבא: [Advanced Server Topics](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->