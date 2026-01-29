# שרת MCP למזג אוויר

זהו שרת MCP לדוגמה שנכתב ב-Python ומיישם כלים למזג אוויר עם תגובות מדומות. ניתן להשתמש בו כבסיס ליצירת שרת MCP משלכם. הוא כולל את התכונות הבאות:

- **כלי מזג אוויר**: כלי המספק מידע מדומה על מזג האוויר בהתבסס על מיקום נתון.
- **כלי שיבוט Git**: כלי המשכפל מאגר Git לתיקייה מסוימת.
- **כלי פתיחה ב-VS Code**: כלי שפותח תיקייה ב-VS Code או ב-VS Code Insiders.
- **חיבור ל-Agent Builder**: תכונה שמאפשרת לחבר את שרת MCP ל-Agent Builder לצורך בדיקות וניפוי שגיאות.
- **ניפוי שגיאות ב-[MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: תכונה שמאפשרת לנפות שגיאות בשרת MCP באמצעות MCP Inspector.

## התחלה עם תבנית שרת MCP למזג אוויר

> **דרישות מקדימות**
>
> כדי להפעיל את שרת MCP במחשב הפיתוח המקומי שלכם, תצטרכו:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (נדרש עבור כלי git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) או [VS Code Insiders](https://code.visualstudio.com/insiders/) (נדרש עבור כלי open_in_vscode)
> - (*אופציונלי - אם אתם מעדיפים uv*) [uv](https://github.com/astral-sh/uv)
> - [תוסף ניפוי שגיאות ל-Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## הכנת הסביבה

ישנן שתי גישות להגדרת הסביבה עבור הפרויקט הזה. תוכלו לבחור אחת מהן בהתאם להעדפתכם.

> הערה: יש לטעון מחדש את VSCode או את הטרמינל כדי לוודא שה-Python של הסביבה הווירטואלית בשימוש לאחר יצירת הסביבה הווירטואלית.

| גישה | שלבים |
| -------- | ----- |
| שימוש ב-`uv` | 1. יצירת סביבה וירטואלית: `uv venv` <br>2. הפעלת פקודת VSCode "***Python: Select Interpreter***" ובחירת ה-Python מהסביבה הווירטואלית שנוצרה <br>3. התקנת תלותים (כולל תלותים לפיתוח): `uv pip install -r pyproject.toml --extra dev` |
| שימוש ב-`pip` | 1. יצירת סביבה וירטואלית: `python -m venv .venv` <br>2. הפעלת פקודת VSCode "***Python: Select Interpreter***" ובחירת ה-Python מהסביבה הווירטואלית שנוצרה<br>3. התקנת תלותים (כולל תלותים לפיתוח): `pip install -e .[dev]` | 

לאחר הגדרת הסביבה, תוכלו להפעיל את השרת במחשב הפיתוח המקומי שלכם דרך Agent Builder בתור MCP Client כדי להתחיל:
1. פתחו את לוח ניפוי השגיאות ב-VS Code. בחרו `Debug in Agent Builder` או לחצו `F5` כדי להתחיל לנפות שגיאות בשרת MCP.
2. השתמשו ב-AI Toolkit Agent Builder כדי לבדוק את השרת עם [הבקשה הזו](../../../../../../../../../../../open_prompt_builder). השרת יתחבר אוטומטית ל-Agent Builder.
3. לחצו `Run` כדי לבדוק את השרת עם הבקשה.

**מזל טוב**! הפעלתם בהצלחה את שרת MCP למזג אוויר במחשב הפיתוח המקומי שלכם דרך Agent Builder בתור MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## מה כלול בתבנית

| תיקייה / קובץ | תכולה                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | קבצי VSCode לניפוי שגיאות                   |
| `.aitk`      | הגדרות עבור AI Toolkit                      |
| `src`        | קוד המקור של שרת MCP למזג אוויר             |

## איך לנפות שגיאות בשרת MCP למזג אוויר

> הערות:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) הוא כלי פיתוח חזותי לבדיקות וניפוי שגיאות בשרתי MCP.
> - כל מצבי ניפוי השגיאות תומכים בנקודות עצירה, כך שתוכלו להוסיף נקודות עצירה לקוד מימוש הכלים.

## כלים זמינים

### כלי מזג אוויר
הכלי `get_weather` מספק מידע מדומה על מזג האוויר עבור מיקום מסוים.

| פרמטר | סוג | תיאור |
| --------- | ---- | ----------- |
| `location` | מחרוזת | מיקום לקבלת מידע על מזג האוויר (לדוגמה, שם עיר, מדינה או קואורדינטות) |

### כלי שיבוט Git
הכלי `git_clone_repo` משכפל מאגר Git לתיקייה מסוימת.

| פרמטר | סוג | תיאור |
| --------- | ---- | ----------- |
| `repo_url` | מחרוזת | כתובת URL של מאגר ה-Git לשיבוט |
| `target_folder` | מחרוזת | נתיב לתיקייה שבה המאגר ישוכפל |

הכלי מחזיר אובייקט JSON עם:
- `success`: ערך בוליאני שמציין אם הפעולה הצליחה
- `target_folder` או `error`: נתיב המאגר המשוכפל או הודעת שגיאה

### כלי פתיחה ב-VS Code
הכלי `open_in_vscode` פותח תיקייה ב-VS Code או ב-VS Code Insiders.

| פרמטר | סוג | תיאור |
| --------- | ---- | ----------- |
| `folder_path` | מחרוזת | נתיב לתיקייה לפתיחה |
| `use_insiders` | בוליאני (אופציונלי) | האם להשתמש ב-VS Code Insiders במקום ב-VS Code הרגיל |

הכלי מחזיר אובייקט JSON עם:
- `success`: ערך בוליאני שמציין אם הפעולה הצליחה
- `message` או `error`: הודעת אישור או הודעת שגיאה

| מצב ניפוי שגיאות | תיאור | שלבים לניפוי שגיאות |
| ---------- | ----------- | --------------- |
| Agent Builder | ניפוי שגיאות בשרת MCP דרך Agent Builder באמצעות AI Toolkit. | 1. פתחו את לוח ניפוי השגיאות ב-VS Code. בחרו `Debug in Agent Builder` ולחצו `F5` כדי להתחיל לנפות שגיאות בשרת MCP.<br>2. השתמשו ב-AI Toolkit Agent Builder כדי לבדוק את השרת עם [הבקשה הזו](../../../../../../../../../../../open_prompt_builder). השרת יתחבר אוטומטית ל-Agent Builder.<br>3. לחצו `Run` כדי לבדוק את השרת עם הבקשה. |
| MCP Inspector | ניפוי שגיאות בשרת MCP באמצעות MCP Inspector. | 1. התקינו [Node.js](https://nodejs.org/)<br> 2. הגדירו את Inspector: `cd inspector` && `npm install` <br> 3. פתחו את לוח ניפוי השגיאות ב-VS Code. בחרו `Debug SSE in Inspector (Edge)` או `Debug SSE in Inspector (Chrome)`. לחצו F5 כדי להתחיל לנפות שגיאות.<br> 4. כאשר MCP Inspector ייפתח בדפדפן, לחצו על כפתור `Connect` כדי לחבר את שרת MCP הזה.<br> 5. לאחר מכן תוכלו `List Tools`, לבחור כלי, להזין פרמטרים, וללחוץ `Run Tool` כדי לנפות שגיאות בקוד השרת שלכם.<br> |

## פורטים ברירת מחדל והתאמות אישיות

| מצב ניפוי שגיאות | פורטים | הגדרות | התאמות אישיות | הערה |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | ערכו את [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) כדי לשנות את הפורטים הנ"ל. | N/A |
| MCP Inspector | 3001 (שרת); 5173 ו-3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | ערכו את [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) כדי לשנות את הפורטים הנ"ל.| N/A |

## משוב

אם יש לכם משוב או הצעות עבור התבנית הזו, אנא פתחו בעיה ב-[מאגר GitHub של AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.