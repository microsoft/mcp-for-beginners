# פריסת שרתי MCP

פריסת שרת ה-MCP שלך מאפשרת לאחרים לגשת לכלים ולמשאבים שלו מעבר לסביבה המקומית שלך. קיימות מספר אסטרטגיות פריסה שכדאי לשקול, בהתאם לדרישות שלך בנוגע להרחבה, אמינות ונוחות ניהול. להלן הנחיות לפריסת שרתי MCP באופן מקומי, במכולות ובענן.

## סקירה כללית

השיעור הזה עוסק באיך לפרוס את אפליקציית שרת ה-MCP שלך.

## מטרות הלמידה

בסיום השיעור תוכל:

- להעריך גישות פריסה שונות.
- לפרוס את האפליקציה שלך.

## פיתוח ופריסה מקומית

אם השרת שלך מיועד לשימוש על ידי הרצה במחשב המשתמש, תוכל לבצע את השלבים הבאים:

1. **הורד את השרת**. אם לא כתבת את השרת, הורד אותו תחילה למחשב שלך.  
1. **הפעל את תהליך השרת**: הרץ את אפליקציית שרת ה-MCP שלך.

עבור SSE (לא נדרש לשרת מסוג stdio)

1. **הגדר את הרשת**: ודא שהשרת נגיש בפורט הצפוי.  
1. **חבר לקוחות**: השתמש בכתובות חיבור מקומיות כמו `http://localhost:3000`.

## פריסה בענן

ניתן לפרוס שרתי MCP בפלטפורמות ענן שונות:

- **פונקציות ללא שרת (Serverless Functions)**: פרוס שרתי MCP קלים כפונקציות ללא שרת.  
- **שירותי מכולות**: השתמש בשירותים כמו Azure Container Apps, AWS ECS או Google Cloud Run.  
- **Kubernetes**: פרוס ונהל שרתי MCP באשכולות Kubernetes לזמינות גבוהה.

### דוגמה: Azure Container Apps

Azure Container Apps תומך בפריסת שרתי MCP. זה עדיין בתהליך פיתוח וכרגע תומך בשרתי SSE.

כך תוכל לעשות זאת:

1. שכפל מאגר:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. הרץ אותו מקומית כדי לבדוק:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. כדי לנסות מקומית, צור קובץ *mcp.json* בתיקיית *.vscode* והוסף את התוכן הבא:

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

  לאחר שהשרת SSE יופעל, תוכל ללחוץ על סמל ההפעלה בקובץ ה-JSON, כעת תראה שכלים בשרת מזוהים על ידי GitHub Copilot, ראה את סמל הכלי.

1. לפריסה, הרץ את הפקודה הבאה:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

זהו, פרוס מקומית או פרוס ל-Azure באמצעות השלבים האלה.

## משאבים נוספים

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [מאמר על Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [מאגר Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## מה הלאה

- הבא: [יישום מעשי](../../04-PracticalImplementation/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.