# איתור באגים עם MCP Inspector

> [!NOTE]
> פקודות המשתמשות ב-`--sse` וקישורים שמסתיימים ב-`/sse` בודקות את ממשק ההובלה הישן HTTP+SSE.
> עבור שרת MCP חדש `2026-07-28`, השתמש בגרסת Inspector התומכת ב-Streamable HTTP ובחר בהובלה זו.


**MCP Inspector** הוא כלי איתור באגים חיוני המאפשר לך לבדוק ולטפל בנושאים בשרתי MCP שלך באופן אינטראקטיבי ללא צורך באפליקציית אירוח AI מלאה. חשוב עליו כ"Postman ל-MCP" - הוא מספק ממשק ויזואלי לשליחת בקשות, צפייה בתגובות והבנת התנהגות השרת שלך.

## למה להשתמש ב-MCP Inspector?

בעת בניית שרתי MCP, תיתקל לעיתים קרובות באתגרים הבאים:

- **"האם השרת שלי בכלל רץ?"** - Inspector מציג את מצב החיבור
- **"האם הכלים שלי רשומים נכון?"** - Inspector מציג את כל הכלים הזמינים
- **"מה פורמט התגובה?"** - Inspector מציג תגובות JSON מלאות
- **"למה הכלי הזה לא עובד?"** - Inspector מציג הודעות שגיאה מפורטות

## דרישות מוקדמות

- התקנת Node.js 18+
- npm (מגיע עם Node.js)
- שרת MCP לבדיקה (ראה [Module 3.1 - First Server](../01-first-server/README.md))

## התקנה

### אפשרות 1: הפעלה עם npx (מומלץ לבדיקות מהירות)

```bash
npx @modelcontextprotocol/inspector
```

### אפשרות 2: התקנה גלובלית

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### אפשרות 3: הוספה לפרויקט שלך

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

הוסף ל-`package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## חיבור לשרת שלך

### שרתי stdio (תהליך מקומי)

עבור שרתים שמתקשרים דרך קלט/פלט סטנדרטי:

```bash
# Python server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js server
npx @modelcontextprotocol/inspector node ./build/index.js

# With environment variables
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### שרתי SSE/HTTP (רשת)

עבור שרתים שרצים כשירותי HTTP:

1. הפעל את השרת תחילה:
   ```bash
   python server.py  # Server running on http://localhost:8080
   ```

2. הפעל את Inspector והתחבר:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## סקירת ממשק Inspector

כש-Inspector מופעל, תראה ממשק אינטרנט (בדרך כלל ב-`http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## בדיקת כלים

### רשימת כלים זמינים

1. לחץ על לשונית **כלים**
2. Inspector קורא אוטומטית ל-`tools/list`
3. תראה את כל הכלים הרשומים עם:
   - שם הכלי
   - תיאור
   - סכמת קלט (פרמטרים)

### קריאת כלי

1. בחר כלי מהרשימה
2. מלא את הפרמטרים הדרושים בטופס
3. לחץ על **הרץ כלי**
4. צפה בתגובה בלוח התוצאות

**דוגמה: בדיקת כלי מחשבון**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### איתור שגיאות בכלים

כשכלי נכשל, Inspector מציג:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

קודי שגיאה נפוצים:
| קוד | משמעות |
|------|---------|
| -32700 | שגיאת פרסור (JSON לא תקין) |
| -32600 | בקשה לא חוקית |
| -32601 | שיטה לא נמצאה |
| -32602 | פרמטרים לא חוקיים |
| -32603 | שגיאה פנימית |

---

## בדיקת משאבים

### רשימת משאבים

1. לחץ על לשונית **משאבים**
2. Inspector קורא ל-`resources/list`
3. תראה:
   - כתובות URI של המשאבים
   - שמות ותיאורים
   - סוגי MIME

### קריאת משאב

1. בחר משאב
2. לחץ על **קרא משאב**
3. צפה בתוכן שהוחזר

**דוגמת פלט:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## בדיקת פרומפטים

### רשימת פרומפטים

1. לחץ על לשונית **פרומפטים**
2. Inspector קורא ל-`prompts/list`
3. צפה בתבניות הפרומפט הזמינות

### קבלת פרומפט

1. בחר פרומפט
2. מלא ארגומנטים נדרשים אם יש
3. לחץ על **קבל פרומפט**
4. ראה את הודעות הפרומפט שהוצגו

---

## ניתוח יומן הודעות

יומן ההודעות מציג את כל הודעות פרוטוקול MCP. התמלול מטה הוא משרת
`2025-11-25` ישן וכולל את לחיצת הידיים שהוסרה `initialize`. שרת
`2026-07-28` משתמש במטה-נתוני בקשה עצמי ו-`server/discover` במקום זאת.


```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### מה לחפש

- **זוגות בקשה/תגובה**: כל `→` צריך להתאים ל-`←`
- **הודעות שגיאה**: חפש `"error"` בתגובות
- **תזמון**: רווחים גדולים עשויים להעיד על בעיות ביצועים
- **גרסת פרוטוקול**: ודא שהשרת והלקוח מסכימים על הגרסה

---

## אינטגרציה עם VS Code

ניתן להפעיל את Inspector ישירות מתוך VS Code:

### שימוש ב-launch.json

הוסף ל-`.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### שימוש ב-Tasks

הוסף ל-`.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## תרחישי איתור באגים נפוצים

### תרחיש 1: השרת לא מתחבר

**תסמינים:** Inspector מציג "מנותק" או תקוע על "מתחבר..."

**רשימת בדיקה:**
1. ✅ האם פקודת השרת נכונה?
2. ✅ האם כל התלויות מותקנות?
3. ✅ האם הנתיב לשרת מוחלט או יחסי לתיקיית העבודה הנוכחית?
4. ✅ האם משתני סביבה הנדרשים מוגדרים?

**שלבי איתור באגים:**
```bash
# Test server manually first
python -c "import your_server_module; print('OK')"

# Check for import errors
python -m your_server_module 2>&1 | head -20

# Verify MCP SDK is installed
pip show mcp
```

### תרחיש 2: כלים אינם מופיעים

**תסמינים:** לשונית הכלים מציגה רשימה ריקה

**סיבות אפשריות:**
1. כלים לא נרשמו במהלך אתחול השרת
2. השרת התרסק לאחר ההפעלה
3. מטפל `tools/list` מחזיר מערך ריק

**שלבי איתור באגים:**
1. בדוק את יומן ההודעות עבור תגובת `tools/list`
2. הוסף רישום לקוד רישום הכלים שלך
3. וודא שמקשטי `@mcp.tool()` קיימים (פייתון)

### תרחיש 3: הכלי מחזיר שגיאה

**תסמינים:** קריאת כלי מחזירה תגובת שגיאה

**גישה לאיתור באגים:**
1. קרא את הודעת השגיאה בקפידה
2. בדוק שסוגי הפרמטרים תואמים את הסכימה
3. הוסף ניהול try/catch עם הודעות שגיאה מפורטות
4. בדוק יומני שרת עבור עקבות מחסנית

**דוגמה לניהול שגיאה משופר:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Tool logic here
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### תרחיש 4: תוכן המשאב ריק

**תסמינים:** המשאב מחזיר אך התוכן ריק או null

**רשימת בדיקה:**
1. ✅ הנתיב או ה-URI של הקובץ נכונים
2. ✅ לשרת יש הרשאה לקרוא את המשאב
3. ✅ תוכן המשאב מוחזר כראוי

---

## תכונות מתקדמות של Inspector

### כותרות מותאמות אישית (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### רישום מפורט

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### הקלטת מפגשים

Inspector יכול לייצא יומני הודעות לניתוח מאוחר יותר:
1. לחץ על **ייצוא יומן** בלוח ההודעות
2. שמור את קובץ ה-JSON
3. שתף עם חברי הצוות לצורך איתור באגים

---

## שיטות עבודה מומלצות

1. **בדוק מוקדם ולעיתים קרובות** - השתמש ב-Inspector בזמן הפיתוח, לא רק כשדברים נשברים
2. **התחל מהפשוט** - בדוק חיבוריות בסיסית לפני קריאות כלי מורכבות
3. **בדוק את הסכמה** - הרבה שגיאות נובעות מאי התאמת סוגי פרמטרים
4. **קרא הודעות שגיאה** - שגיאות MCP בדרך כלל תיאוריות
5. **השאר את ה-Inspector פתוח** - זה עוזר לתפוס בעיות תוך כדי פיתוח

---

## מה הלאה

השלמת את מודול 3: התחלת העבודה! המשך ללמוד:

- [מודול 4: יישום מעשי](../../04-PracticalImplementation/README.md)

---

## משאבים נוספים

- [מאגר GitHub של MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [מפרט MCP - הודעות פרוטוקול](https://modelcontextprotocol.io/specification/2026-07-28/)
- [מפרט JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->