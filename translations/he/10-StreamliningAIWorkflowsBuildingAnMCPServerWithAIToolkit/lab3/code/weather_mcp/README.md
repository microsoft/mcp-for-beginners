# שרת MCP למזג אוויר

זהו דוגמה של שרת MCP בפייתון המממש כלים למזג אוויר עם תגובות מדומות. ניתן להשתמש בו כתשתית לשרת MCP משלך. הוא כולל את התכונות הבאות:

- **כלי מזג אוויר**: כלי שמספק מידע מזג אוויר מדומה על בסיס המיקום הנתון.
- **חיבור ל-Agent Builder**: תכונה המאפשרת חיבור של שרת MCP ל-Agent Builder לבדיקות ודיבוג.
- **דיבוג ב-[MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: תכונה המאפשרת דיבוג של שרת MCP באמצעות MCP Inspector.

## התחל עם התבנית של שרת MCP למזג אוויר

> **דרישות מוקדמות**
>
> להפעלת שרת MCP במחשב הפיתוח המקומי שלך, תזדקק ל:
>
> - [Python](https://www.python.org/)
> - (*אופציונלי - אם אתה מעדיף uv*) [uv](https://github.com/astral-sh/uv)
> - [הרחבת דיבוג לפייתון](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## הכנת הסביבה

יש שתי גישות להקמת הסביבה לפרויקט זה. תוכל לבחור אחת מהן לפי העדפתך.

> הערה: טען מחדש את VSCode או את הטרמינל כדי לוודא שמשתמשים בפייתון של הסביבה הווירטואלית לאחר יצירת הסביבה הווירטואלית.

| גישה | צעדים |
| -------- | ----- |
| שימוש ב-`uv` | 1. צור סביבה וירטואלית: `uv venv` <br>2. הפעל את פקודת VSCode "***Python: Select Interpreter***" ובחר את הפייתון מהסביבה הווירטואלית שיצרת <br>3. התקן תלותים (כולל תלותים לפיתוח): `uv pip install -r pyproject.toml --extra dev` |
| שימוש ב-`pip` | 1. צור סביבה וירטואלית: `python -m venv .venv` <br>2. הפעל את פקודת VSCode "***Python: Select Interpreter***" ובחר את הפייתון מהסביבה הווירטואלית שיצרת<br>3. התקן תלותים (כולל תלותים לפיתוח): `pip install -e .[dev]` | 

לאחר הקמת הסביבה, תוכל להפעיל את השרת במחשב הפיתוח המקומי שלך דרך Agent Builder כלקוח MCP כדי להתחיל:
1. פתח את לוח הדיבוג ב-VS Code. בחר `Debug in Agent Builder` או לחץ על `F5` כדי להתחיל בדיבוג של שרת MCP.
2. ב-Microsoft Foundry Toolkit Agent Builder, בחר הפצת Foundry פעילה כגון `gpt-5.1`, ואז הכנס: `What is the weather in Shanghai?` השרת יתחבר אוטומטית.
3. לחץ על `Run` כדי לבדוק את השרת עם ההנחיה.

**מזל טוב**! הפעלת בהצלחה את שרת MCP למזג אוויר במחשב הפיתוח המקומי שלך דרך Agent Builder כלקוח MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## מה כלול בתבנית

| תיקיה / קובץ | תוכן                                      |
| ------------ | -------------------------------------------- |
| `.vscode`    | קבצי VSCode לדיבוג                         |
| `.aitk`      | תצורות ל-Microsoft Foundry Toolkit                     |
| `src`        | קוד המקור של שרת MCP למזג אוויר            |

## כיצד לדבג את שרת MCP למזג אוויר

> הערות:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) הוא כלי חזותי למפתח לבדיקות ודיבוג שרתי MCP.
> - כל מצבי הדיבוג תומכים בנקודות עצירה, כך שניתן להוסיף נקודות עצירה לקוד מימוש הכלים.

| מצב דיבוג | תיאור | שלבים לדיבוג |
| ---------- | ----------- | --------------- |
| Agent Builder | דבג את שרת MCP ב-Agent Builder דרך Microsoft Foundry Toolkit. | 1. פתח את לוח הדיבוג ב-VS Code. בחר `Debug in Agent Builder` ולחץ על `F5` כדי להתחיל בדיבוג של שרת MCP.<br>2. בחר הפצת Foundry פעילה כגון `gpt-5.1`, ואז הכנס `What is the weather in Shanghai?`. השרת יתחבר אוטומטית.<br>3. לחץ על `Run` כדי לבדוק את השרת עם ההנחיה. |
| MCP Inspector | דבג את שרת MCP באמצעות MCP Inspector. | 1. התקן [Node.js](https://nodejs.org/)<br> 2. הגדר את Inspector: `cd inspector` && `npm install` <br> 3. פתח את לוח הדיבוג ב-VS Code. בחר `Debug SSE in Inspector (Edge)` או `Debug SSE in Inspector (Chrome)`. לחץ F5 כדי להתחיל בדיבוג.<br> 4. כשה-MCP Inspector עולה בדפדפן, לחץ על כפתור `Connect` כדי להתחבר לשרת MCP זה.<br> 5. אז תוכל `List Tools`, לבחור כלי, להזין פרמטרים, ו-`Run Tool` כדי לדבג את קוד השרת שלך.<br> |

## פורטים ברירת מחדל והתאמות

| מצב דיבוג | פורטים | הגדרות | התאמות | הערה |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | ערוך את [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) כדי לשנות את הפורטים הנ"ל. | אין |
| MCP Inspector | 3001 (שרת); 5173 ו-3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | ערוך את [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) כדי לשנות את הפורטים הנ"ל.| אין |

## משוב

אם יש לך משוב או הצעות לתבנית זו, אנא פתח נושא ב-[מאגר Microsoft Foundry Toolkit בגיטהאב](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->