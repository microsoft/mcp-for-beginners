# הגדרת לקוחות מארחים פופולריים של MCP

> [!NOTE]
> תצורות מארחים המצביעות על `/sse` הן דוגמות ישנות של HTTP+SSE עבור
> MCP `2025-11-25`. עבור MCP `2026-07-28`, יש לבחור ב-Streamable HTTP במארחים
> שתומכים בכך ולהשתמש בנקודת הקצה שהוגדרה על ידי השרת.

מדריך זה מסביר כיצד להגדיר ולשימוש שרתי MCP עם יישומי מארחים פופולריים של AI. לכל מארח יש גישה משלו לתצורה, אבל לאחר ההגדרה, כולם מתקשרים עם שרתי MCP באמצעות הפרוטוקול המ стандарטי.

## מהו מארח MCP?

**מארח MCP** הוא יישום AI שיכול להתחבר לשרתי MCP כדי להרחיב את היכולות שלו. חשבו עליו כ"חזית" שהמשתמשים מתקשרים איתה, בעוד ששרתי MCP מספקים את הכלים והנתונים ב"גב".

```mermaid
flowchart LR
    User[👤 משתמש] --> Host[🖥️ מארח MCP]
    Host --> S1[שרת MCP א]
    Host --> S2[שרת MCP ב]
    Host --> S3[שרת MCP ג]
    
    subgraph "מרצים פופולריים"
        H1[שולחן עבודה של קלוד]
        H2[VS קוד]
        H3[סורסור]
        H4[קליין]
        H5[ווינדסרף]
    end
```

## דרישות מוקדמות

- שרת MCP להתחבר אליו (ראה [Module 3.1 - שרת ראשון](../01-first-server/README.md))
- יישום המארח מותקן במערכת שלך
- היכרות בסיסית עם קבצי תצורה בפורמט JSON

---

## 1. Claude Desktop

**Claude Desktop** הוא יישום שולחני רשמי של Anthropic התומך בנגן ב-MCP באופן מובנה.

### התקנה

1. הורד את Claude Desktop מ-[claude.ai/download](https://claude.ai/download)
2. התקן והיכנס עם חשבון Anthropic שלך

### תצורה

Claude Desktop משתמש בקובץ תצורה בפורמט JSON להגדרת שרתי MCP.

**מיקום קובץ התצורה:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**דוגמת תצורה:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### אפשרויות תצורה

| שדה | תיאור | דוגמה |
|-------|-------------|---------|
| `command` | הקובץ להוצאה לפועל | `"python"`, `"node"`, `"npx"` |
| `args` | ארגומנטים בשורת הפקודה | `["-m", "my_server"]` |
| `env` | משתני סביבה | `{"API_KEY": "xxx"}` |
| `cwd` | תיקיית עבודה | `"/path/to/server"` |

### בדיקת ההגדרה

1. שמור את קובץ התצורה
2. הפעל מחדש את Claude Desktop לגמרי (סגור ופתח מחדש)
3. פתח שיחה חדשה
4. חפש את סמל 🔌 שמצביע על שרתים מחוברים
5. נסה לבקש מ-Claude להשתמש באחד הכלים שלך

### פתרון בעיות ב-Claude Desktop

**השרת לא מופיע:**
- בדוק את תחביר קובץ התצורה בעזרת מאמת JSON
- ודא שהנתיב לפקודה נכון
- בדוק את יומני Claude Desktop: עזרה → הצג יומנים

**השרת קורץ בהפעלה:**
- בדוק ידנית את השרת במסוף קודם
- ודא שמשתני הסביבה מוגדרים נכון
- ודא שכל התלויות מותקנות

---

## 2. VS Code עם GitHub Copilot

VS Code תומך ב-MCP דרך תוספי GitHub Copilot Chat.

### דרישות מוקדמות

1. VS Code גרסה 1.99+ מותקן
2. תוסף GitHub Copilot מותקן
3. תוסף GitHub Copilot Chat מותקן

### תצורה

VS Code משתמש ב-`.vscode/mcp.json` בהגדרות סביבת העבודה או המשתמש.

**תצורת סביבת עבודה** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**הגדרות משתמש** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### שימוש ב-MCP ב-VS Code

1. פתח את לוח הפקד של Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. הקלד `@` כדי לראות את כלי ה-MCP הזמינים
3. השתמש בשפה טבעית להפעלת כלים: "חשב 25 * 48 באמצעות המחשבון"

### פתרון בעיות ב-VS Code

**שרתות MCP לא נטענים:**
- בדוק את לוח הפלט → "MCP" עבור יומני שגיאות
- טען מחדש את החלון: Ctrl+Shift+P → "Developer: Reload Window"
- ודא שהשרת רץ בצורה עצמאית קודם

---

## 3. Cursor

**Cursor** הוא עורך קוד המונחה AI עם תמיכה מובנית ב-MCP.

### התקנה

1. הורד את Cursor מ-[cursor.sh](https://cursor.sh)
2. התקן והיכנס

### תצורה

Cursor משתמש בפורמט תצורה דומה לזה של Claude Desktop.

**מיקום קובץ התצורה:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**דוגמת תצורה:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### שימוש ב-MCP ב-Cursor

1. פתח את הצ'אט של AI ב-Cursor (Ctrl+L / Cmd+L)
2. כלי MCP מופיעים אוטומטית בהצעות
3. בקש מה-AI לבצע משימות באמצעות השרתים המחוברים

---

## 4. Cline (מבוסס טרמינל)

**Cline** הוא לקוח MCP מבוסס טרמינל, אידיאלי לזרימות עבודה של שורת פקודה.

### התקנה

```bash
npm install -g @anthropic/cline
```

### תצורה

Cline משתמש במשתני סביבה וארגומנטים בשורת הפקודה.

**שימוש במשתני סביבה:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**שימוש בארגומנטים בשורת הפקודה:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**קובץ תצורה** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### שימוש ב-Cline

```bash
# התחל מפגש אינטראקטיבי
cline

# שאילתה אחת עם MCP
cline "Calculate the square root of 144 using the calculator"

# רשום כלים זמינים
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** הוא עורך קוד נוסף המונחה AI עם תמיכה ב-MCP.

### התקנה

1. הורד את Windsurf מ-[codeium.com/windsurf](https://codeium.com/windsurf)
2. התקן ופתח חשבון

### תצורה

תצורת Windsurf מנוהלת דרך ממשק ההגדרות:

1. פתח הגדרות (Ctrl+, / Cmd+,)
2. חפש "MCP"
3. לחץ "ערוך ב-settings.json"

**דוגמת תצורה:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## השוואת סוגי תחבורה

מארחים שונים תומכים במנגנוני תחבורה שונים:

| מארח | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (קלט/פלט סטנדרטי): הטוב ביותר עבור שרתים מקומיים שמופעלים על ידי המארח
**SSE/HTTP**: הטוב ביותר עבור שרתים מרוחקים או שרתים שמשותפים בין מספר לקוחות

---

## פתרון בעיות נפוצות

### השרת לא מתחיל

1. **בדוק את השרת ידנית קודם:**
   ```bash
   # לפייתון
   python -m your_server_module
   
   # עבור Node.js
   node /path/to/server/index.js
   ```

2. **בדוק את נתיב הפקודה:**
   - השתמש בנתיבים מוחלטים כאשר זה אפשרי
   - ודא שהקובץ ההרצה נמצא ב-PATH שלך

3. **וודא תלותיות:**
   ```bash
   # פייתון
   pip list | grep mcp
   
   # נוד.ג'ס
   npm list @modelcontextprotocol/sdk
   ```

### השרת מתחבר אך הכלים לא עובדים

1. **בדוק יומני שרת** - לרוב המארחים יש אפשרויות רישום
2. **ודא רישום כלי** - השתמש ב-MCP Inspector לבדיקה
3. **בדוק הרשאות** - חלק מהכלים צריכים גישה לקבצים/רשת

### משתני סביבה לא מועברים

- חלק מהמארחים מנקים משתני סביבה
- השתמש בשדה התצורה `env` במפורש
- הימנע מנתונים רגישים בקבצי תצורה (השתמש בניהול סודות)

---

## שיטות טובות לאבטחה

1. **אל תתחייב למפתחות API** בקבצי תצורה
2. **השתמש במשתני סביבה** עבור נתונים רגישים
3. **הגביל הרשאות שרת** רק למה שנדרש
4. **סקור את קוד השרת** לפני מתן גישה למערכת שלך
5. **השתמש ברשימות מורשות** לגישה למערכת הקבצים ולרשת

---

## מה הלאה

- [3.13 - איתור תקלות עם MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - צור את שרת MCP הראשון שלך](../01-first-server/README.md)
- [מודול 5 - נושאים מתקדמים](../../05-AdvancedTopics/README.md)

---

## משאבים נוספים

- [תיעוד MCP של Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [תוסף MCP لـ VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [מפרט MCP - תחבורה](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [רישום שרתי MCP רשמי](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->