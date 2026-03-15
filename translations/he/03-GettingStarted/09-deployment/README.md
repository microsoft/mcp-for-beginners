# פריסת שרתי MCP

פריסת שרת MCP שלך מאפשרת לאחרים לגשת לכלים ולמשאבים שלו מעבר לסביבה המקומית שלך. ישנן מספר אסטרטגיות פריסה שכדאי לקחת בחשבון, בהתאם לדרישותיך בקנה מידה, אמינות ונוחות ניהול. למטה תמצא הנחיות לפריסת שרתי MCP מקומית, במכולות, ובענן.

## מבוא

שיעור זה מכסה כיצד לפרוס את יישום שרת MCP שלך.

## יעדי הלמידה

בסוף שיעור זה, תהיה מסוגל/ת:

- להעריך גישות פריסה שונות.
- לפרוס את היישום שלך.

## פיתוח ופריסה מקומית

אם השרת שלך מיועד להיות בשימוש על ידי הרצתו במחשב המשתמש, תוכל לעקוב אחר השלבים הבאים:

1. **הורד את השרת**. אם לא כתבת את השרת, הורד אותו תחילה למחשב שלך.  
1. **הפעל את תהליך השרת**: הרץ את אפליקציית שרת MCP שלך

עבור SSE (לא דרוש לשרת מסוג stdio)

1. **הגדר את הרשת**: ודא שהשרת נגיש בנמל הצפוי  
1. **חבר לקוחות**: השתמש בכתובות חיבור מקומיות כמו `http://localhost:3000`

## פריסה בענן

ניתן לפרוס שרתי MCP בפלטפורמות ענן שונות:

- **פונקציות ללא שרת**: פרוס שרתי MCP קלים ופונקציונליים כפונקציות ללא שרת  
- **שירותי מכולות**: השתמש בשירותים כגון Azure Container Apps, AWS ECS, או Google Cloud Run  
- **קוברנטיס**: פרוס ונהל שרתי MCP באשכולות Kubernetes לזמינות גבוהה  

### דוגמה: Azure Container Apps

שירות Azure Container Apps תומך בפריסת שרתי MCP. השירות עדיין בתהליכי פיתוח והוא תומך כרגע בשרתי SSE.

הנה כיצד ניתן לעשות זאת:

1. שכפל ריפו:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. הרץ אותו מקומית כדי לבדוק:

  ```sh
  uv venv
  uv sync

  # לינוקס/מק או אס
  export API_KEYS=<AN_API_KEY>
  # ווינדוס
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. כדי לנסות אותו מקומית, צור קובץ *mcp.json* בתיקיית *.vscode* והוסף את התוכן הבא:

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

  לאחר שהשרת SSE הופעל, תוכל ללחוץ על סמל ההפעלה בקובץ ה-JSON, כעת אמורות להופיע כלים על השרת שמזוהים על ידי GitHub Copilot, ראה את סמל הכלי.

1. לפרוס, הרץ את הפקודה הבאה:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

וזהו, פרוס את השרת מקומית, ופרוס אותו ל-Azure באמצעות השלבים הללו.

## משאבים נוספים

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [מאמר על Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [ריפו של Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## מה הלאה

- הבא: [נושאים מתקדמים בשרת](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתירגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי של מתרגם אנושי. אנו לא נושאים באחריות לנזקים או אי-הבנות הנובעים משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->