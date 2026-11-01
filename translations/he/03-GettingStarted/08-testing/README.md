## בדיקות ואיתור באגים

לפני שתתחילו לבדוק את שרת MCP שלכם, חשוב להבין את הכלים הזמינים ואת שיטות העבודה הטובות לאיתור באגים. בדיקות יעילות מבטיחות שהשרת שלכם מתנהג כמצופה ומסייעות לכם לזהות ולפתור בעיות במהירות. החלק הבא מפרט שיטות מומלצות לאימות יישום MCP שלכם.

## סקירה כללית

שיעור זה מסביר כיצד לבחור את גישת הבדיקה הנכונה ואת כלי הבדיקה היעיל ביותר.

## מטרות הלמידה

בסוף השיעור תוכלו:

- לתאר גישות שונות לבדיקה.
- להשתמש בכלים שונים כדי לבדוק את הקוד שלכם בצורה יעילה.


## בדיקות שרתי MCP

MCP מספק כלים שיעזרו לכם לבדוק ולתקן באגים בשרתים שלכם:

- **MCP Inspector**: כלי שורת פקודה שניתן להריץ גם ככלי CLI וגם ככלי חזותי.
- **בדיקה ידנית**: תוכלו להשתמש בכלי כמו curl להפעיל בקשות רשת, אבל כל כלי שמסוגל להריץ HTTP יעבוד.
- **בדיקות יחידה**: ניתן להשתמש במסגרת בדיקות מועדפת כדי לבדוק את התכונות של השרת והלקוח.

### שימוש ב-MCP Inspector

תיארנו את השימוש בכלי זה בשיעורים קודמים אך נדבר עליו בקצרה ברמה גבוהה. זהו כלי מבוסס Node.js ואתם יכולים להשתמש בו על ידי קריאה לקובץ ההרצה `npx` אשר יוריד ויתקין את הכלי זמנית וינקה את עצמו לאחר סיום הרצת הבקשה שלכם.

ה-[MCP Inspector](https://github.com/modelcontextprotocol/inspector) עוזר לכם:

- **לגלות יכולות שרת**: לאתר אוטומטית משאבים, כלים, והנחיות זמינות
- **לבדוק הרצת כלים**: לנסות פרמטרים שונים ולראות תגובות בזמן אמת
- **להציג מטה-נתוני שרת**: לבדוק מידע על השרת, סכימות וקונפיגורציות

דוגמה להרצה טיפוסית של הכלי נראית כך:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

הפקודה שלמעלה מפעילה MCP ואת הממשק החזותי שלו ופותרת ממשק רשת מקומי בדפדפן שלכם. תוכלו לצפות בלוח בקרה המציג את שרתי MCP הרשומים שלכם, הכלים הזמינים, המשאבים וההנחיות שלהם. הממשק מאפשר בדיקה אינטראקטיבית של הרצת כלים, בחינה של מטה-נתוני השרת, וצפייה בתגובות בזמן אמת, מה שמקל על אימות ותיקון יישומי שרת MCP שלכם.

כך זה יכול להיראות: ![Inspector](../../../../translated_images/he/connect.141db0b2bd05f096.webp)

ניתן גם להריץ את הכלי במצב CLI שבו מוסיפים את התכונה `--cli`. הנה דוגמה להרצת הכלי במצב "CLI" שמציגה את כל הכלים בשרת:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### בדיקה ידנית

מעבר להרצת כלי ה-inspector כדי לבדוק את יכולות השרת, גישה דומה היא להריץ לקוח שיכול להשתמש ב-HTTP כמו curl למשל.

עם curl, תוכלו לבדוק את שרתי MCP ישירות באמצעות בקשות HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

כפי שניתן לראות משימוש curl לעיל, אתם משתמשים בבקשת POST כדי להפעיל כלי באמצעות מטען המכיל את שמו של הכלי ואת הפרמטרים שלו. השתמשו בגישה שנוחה לכם ביותר. כלים מבוססי CLI בדרך כלל מהירים יותר לשימוש ומתאימים לסקריפטים, מה שיכול להיות שימושי בסביבת CI/CD.

### בדיקות יחידה

צרו בדיקות יחידה לכלים ולמשאבים שלכם כדי לוודא שהם עובדים כמצופה. הנה דוגמת קוד לבדיקות.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

הקוד שלעיל עושה את הדברים הבאים:

- מנצל את מסגרת pytest שמאפשרת ליצור בדיקות כפונקציות ולהשתמש בפקודות assert.
- יוצר שרת MCP עם שני כלים שונים.
- משתמש בפקודת `assert` כדי לבדוק שמתקיימים תנאים מסוימים.

עיינו בקובץ המלא [כאן](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

בהתבסס על הקובץ לעיל, תוכלו לבדוק את השרת שלכם כדי לוודא שהיכולות נוצרו כראוי.

לכל סביבות הפיתוח המרכזיות יש קטעי בדיקות דומים כך שתוכלו להתאים לסביבת הריצה שבחרתם.

## דוגמאות 

- [מחשבון Java](../samples/java/calculator/README.md)
- [מחשבון .NET](../../../../03-GettingStarted/samples/csharp)
- [מחשבון JavaScript](../samples/javascript/README.md)
- [מחשבון TypeScript](../samples/typescript/README.md)
- [מחשבון Python](../../../../03-GettingStarted/samples/python) 

## משאבים נוספים

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## מה הלאה

- הבא: [פריסה](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->