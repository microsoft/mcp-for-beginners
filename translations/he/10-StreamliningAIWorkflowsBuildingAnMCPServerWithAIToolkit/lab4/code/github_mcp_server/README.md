# שרת MCP למזג אוויר

זהו דוגמה של שרת MCP בפייתון המממש כלים למזג אוויר עם תגובות מדומות. ניתן להשתמש בו כמבנה לשרת MCP משלך. הוא כולל את התכונות הבאות: 

- **כלי מזג אוויר**: כלי המספק מידע מזג אוויר מדומה בהתאם למיקום הנתון.
- **כלי שיבוט Git**: כלי המשכפל מאגר git לתיקייה מסוימת.
- **כלי פתיחת VS Code**: כלי הפותח תיקייה ב-VS Code או ב-VS Code Insiders.
- **חיבור ל-Agent Builder**: תכונה המאפשרת חיבור של שרת ה-MCP ל-Agent Builder לצורך בדיקות וניפוי שגיאות.
- **ניפוי באג ב-[MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: תכונה המאפשרת ניפוי באגים בשרת MCP באמצעות MCP Inspector.

## התחלה עם תבנית שרת MCP למזג אוויר

> **דרישות מקדימות**
>
> כדי להריץ את שרת ה-MCP במכונת הפיתוח המקומית שלך, תזדקק ל:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (נדרש לכלי git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) או [VS Code Insiders](https://code.visualstudio.com/insiders/) (נדרש לכלי open_in_vscode)
> - (*אופציונלי - אם אתה מעדיף uv*) [uv](https://github.com/astral-sh/uv)
> - [תוסף ניפוי שגיאות של פייתון](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## הכנת הסביבה

קיימות שתי דרכים להגדיר את הסביבה עבור הפרויקט הזה. ניתן לבחור אחת מהן לפי ההעדפה שלך.

> הערה: טען מחדש את VSCode או את הטרמינל כדי לוודא שהפייתון של הסביבה הווירטואלית משמש לאחר יצירת הסביבה הווירטואלית.

| גישה | שלבים |
| -------- | ----- |
| שימוש ב-`uv` | 1. צור סביבה וירטואלית: `uv venv` <br>2. הפעל את הפקודה ב-VSCode "***Python: Select Interpreter***" ובחר את הפייתון מהסביבה הווירטואלית שנוצרה <br>3. התקן תלותיות (כולל תלותיות פיתוח): `uv pip install -r pyproject.toml --extra dev` |
| שימוש ב-`pip` | 1. צור סביבה וירטואלית: `python -m venv .venv` <br>2. הפעל את הפקודה ב-VSCode "***Python: Select Interpreter***" ובחר את הפייתון מהסביבה הווירטואלית שנוצרה<br>3. התקן תלותיות (כולל תלותיות פיתוח): `pip install -e .[dev]` | 

לאחר שהגדרת את הסביבה, תוכל להפעיל את השרת במכונת הפיתוח המקומית שלך באמצעות Agent Builder כלקוח MCP כדי להתחיל:
1. פתח את לוח הניפוי ב-VS Code. בחר `Debug in Agent Builder` או לחץ על `F5` כדי להתחיל לנפות את באגים של שרת ה-MCP.
2. ב-Microsoft Foundry Toolkit עבור Visual Studio Code Agent Builder, בחר פריסה פעילה של Foundry כמו `gpt-5.1`, ואז הזן: `What is the weather in Shanghai?` השרת יתחבר אוטומטית.
3. לחץ על `Run` כדי לבדוק את השרת עם השאילתה.

**ברכות**! הצלחת להפעיל את שרת MCP למזג אוויר במכונת הפיתוח המקומית שלך באמצעות Agent Builder כלקוח MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## מה כלול בתבנית

| תיקייה / קובץ| תוכן                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | קבצי VSCode לניפוי שגיאות                   |
| `.aitk`      | קונפיגורציית Microsoft Foundry Toolkit      |
| `src`        | קוד המקור של שרת ה-MCP למזג אוויר   |

## איך לנפות באגים בשרת MCP למזג אוויר

> הערות:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) הוא כלי פיתוח ויזואלי לבדיקה וניפוי שגיאות של שרתי MCP.
> - כל מצבי הניפוי תומכים בנקודות עצירה, כך אפשר להוסיף נקודות עצירה בקוד מימוש הכלי.

## כלים זמינים

### כלי מזג אוויר
הכלי `get_weather` מספק מידע מזג אוויר מדומה למיקום מסוים.

| פרמטר | סוג | תיאור |
| --------- | ---- | ----------- |
| `location` | מחרוזת | מיקום לקבלת מזג האוויר (למשל, שם עיר, מדינה, או קואורדינטות) |

### כלי שיבוט Git
הכלי `git_clone_repo` משכפל מאגר git לתיקייה מסוימת.

| פרמטר | סוג | תיאור |
| --------- | ---- | ----------- |
| `repo_url` | מחרוזת | כתובת URL של מאגר ה-git לשכפול |
| `target_folder` | מחרוזת | נתיב לתיקייה שאליה יש לשכפל את המאגר |

הכלי מחזיר אובייקט JSON עם:
- `success`: בוליאני המציין אם הפעולה הצליחה
- `target_folder` או `error`: הנתיב של המאגר המשוכפל או הודעת שגיאה

### כלי פתיחת VS Code
הכלי `open_in_vscode` פותח תיקייה ביישום VS Code או VS Code Insiders.

| פרמטר | סוג | תיאור |
| --------- | ---- | ----------- |
| `folder_path` | מחרוזת | נתיב לתיקייה לפתיחה |
| `use_insiders` | בוליאני (אופציונלי) | האם להשתמש ב-VS Code Insiders במקום VS Code רגיל |

הכלי מחזיר אובייקט JSON עם:
- `success`: בוליאני המציין אם הפעולה הצליחה
- `message` או `error`: הודעת אישור או הודעת שגיאה

| מצב ניפוי | תיאור | שלבים לניפוי |
| ---------- | ----------- | --------------- |
| Agent Builder | ניפוי שגיאות בשרת MCP ב-Agent Builder דרך Microsoft Foundry Toolkit עבור Visual Studio Code. | 1. פתח את לוח הניפוי ב-VS Code. בחר `Debug in Agent Builder` ולחץ על `F5` כדי להתחיל לנפות את באגים של שרת ה-MCP.<br>2. בחר פריסה פעילה של Foundry כגון `gpt-5.1` ואז הזן `What is the weather in Shanghai?`. השרת יתחבר אוטומטית.<br>3. לחץ על `Run` כדי לבדוק את השרת עם השאילתה. |
| MCP Inspector | ניפוי שגיאות בשרת MCP באמצעות MCP Inspector. | 1. התקן את [Node.js](https://nodejs.org/)<br> 2. הגדר את Inspector: `cd inspector` && `npm install` <br> 3. פתח את לוח הניפוי ב-VS Code. בחר `Debug SSE in Inspector (Edge)` או `Debug SSE in Inspector (Chrome)`. לחץ F5 כדי להתחיל לנפות. <br> 4. כאשר MCP Inspector מופעל בדפדפן, לחץ על כפתור `Connect` כדי להתחבר לשרת MCP זה.<br> 5. אז תוכל `List Tools`, לבחור כלי, להזין פרמטרים, ו-`Run Tool` כדי לנפות שגיאות בקוד השרת שלך.<br> |

## פורטים ברירת מחדל והתאמות אישיות

| מצב ניפוי | פורטים | הגדרות | התאמות אישיות | הערה |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | ערוך את [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) כדי לשנות את הפורטים הנ"ל. | לא זמין |
| MCP Inspector | 3001 (שרת); 5173 ו-3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | ערוך את [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) כדי לשנות את הפורטים הנ"ל.| לא זמין |

## משוב

אם יש לך משוב או הצעות לתבנית זו, אנא פתח issue ב-[מאגר GitHub של Microsoft Foundry Toolkit עבור Visual Studio Code](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->