## בדיקות וניפוי שגיאות

לפני שתתחילו לבדוק את שרת ה-MCP שלכם, חשוב להבין את הכלים הזמינים ואת שיטות העבודה המומלצות לניפוי שגיאות. בדיקות יעילות מבטיחות שהשרת שלכם מתנהג כפי שציפיתם ועוזרות לכם לזהות ולפתור בעיות במהירות. הסעיף הבא מפרט גישות מומלצות לאימות יישום ה-MCP שלכם.

## סקירה כללית

השיעור הזה עוסק בבחירת הגישה הנכונה לבדיקות ובכלי הבדיקה היעיל ביותר.

## מטרות הלמידה

בסיום השיעור תוכלו:

- לתאר גישות שונות לבדיקות.
- להשתמש בכלים שונים כדי לבדוק את הקוד שלכם בצורה יעילה.

## בדיקות שרתי MCP

MCP מספק כלים שיעזרו לכם לבדוק ולפתור בעיות בשרתים שלכם:

- **MCP Inspector**: כלי שורת פקודה שניתן להפעיל גם כ-CLI וגם ככלי ויזואלי.
- **בדיקות ידניות**: ניתן להשתמש בכלי כמו curl להרצת בקשות רשת, אך כל כלי התומך ב-HTTP יתאים.
- **בדיקות יחידה**: אפשר להשתמש במסגרת הבדיקות המועדפת עליכם כדי לבדוק את הפונקציות של השרת והלקוח.

### שימוש ב-MCP Inspector

תיארנו את השימוש בכלי זה בשיעורים קודמים, אבל נסקור אותו בקצרה. זהו כלי שנבנה ב-Node.js וניתן להפעילו באמצעות הפקודה `npx` שמורידה ומתקינה את הכלי זמנית ומנקה את עצמה לאחר סיום הריצה.

ה-[MCP Inspector](https://github.com/modelcontextprotocol/inspector) עוזר לכם:

- **לגלות יכולות שרת**: מזהה אוטומטית משאבים, כלים והנחיות זמינות
- **לבחון הפעלת כלים**: לנסות פרמטרים שונים ולראות תגובות בזמן אמת
- **לצפות במטא-דאטה של השרת**: לבדוק מידע על השרת, סכימות והגדרות

הרצה טיפוסית של הכלי נראית כך:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

הפקודה שלמעלה מפעילה MCP וממשק ויזואלי שמעלה ממשק רשת מקומי בדפדפן שלכם. תוכלו לראות לוח בקרה המציג את שרתי ה-MCP הרשומים שלכם, הכלים, המשאבים וההנחיות הזמינים. הממשק מאפשר לכם לבדוק אינטראקטיבית הפעלת כלים, לבדוק מטא-דאטה של השרת ולראות תגובות בזמן אמת, מה שמקל על אימות וניפוי שגיאות ביישומי ה-MCP שלכם.

כך זה יכול להיראות: ![Inspector](../../../../translated_images/he/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

ניתן גם להפעיל את הכלי במצב CLI על ידי הוספת הפרמטר `--cli`. הנה דוגמה להפעלת הכלי במצב "CLI" שמציג את כל הכלים בשרת:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### בדיקות ידניות

מלבד הפעלת כלי ה-inspector לבדיקת יכולות השרת, גישה דומה היא להפעיל לקוח התומך ב-HTTP, כמו curl לדוגמה.

עם curl, ניתן לבדוק שרתי MCP ישירות באמצעות בקשות HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

כפי שניתן לראות בדוגמה שלמעלה, משתמשים בבקשת POST כדי להפעיל כלי עם מטען הכולל את שם הכלי והפרמטרים שלו. השתמשו בגישה שהכי מתאימה לכם. כלים מבוססי CLI בדרך כלל מהירים יותר לשימוש ומתאימים לאוטומציה, דבר שיכול להיות שימושי בסביבת CI/CD.

### בדיקות יחידה

צרו בדיקות יחידה לכלים ולמשאבים שלכם כדי לוודא שהם פועלים כמצופה. הנה דוגמת קוד לבדיקות.

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

הקוד שלמעלה עושה את הדברים הבאים:

- משתמש במסגרת pytest שמאפשרת ליצור בדיקות כפונקציות ולהשתמש בפקודות assert.
- יוצר שרת MCP עם שני כלים שונים.
- משתמש בפקודת `assert` כדי לוודא שתקיימו תנאים מסוימים.

עיינו ב-[הקובץ המלא כאן](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

בהתבסס על הקובץ הזה, תוכלו לבדוק את השרת שלכם כדי לוודא שהיכולות נוצרות כראוי.

כל ערכות הפיתוח הגדולות כוללות סעיפי בדיקה דומים, כך שתוכלו להתאים לסביבת הריצה שבחרתם.

## דוגמאות

- [מחשבון Java](../samples/java/calculator/README.md)
- [מחשבון .Net](../../../../03-GettingStarted/samples/csharp)
- [מחשבון JavaScript](../samples/javascript/README.md)
- [מחשבון TypeScript](../samples/typescript/README.md)
- [מחשבון Python](../../../../03-GettingStarted/samples/python)

## משאבים נוספים

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## מה הלאה

- הבא: [פריסה](../09-deployment/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.