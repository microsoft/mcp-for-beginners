## בדיקות וניפוי שגיאות

לפני שתתחיל לבדוק את שרת MCP שלך, חשוב להבין את הכלים הזמינים ואת שיטות העבודה המומלצות לניפוי שגיאות. בדיקה יעילה מבטיחה שהשרת שלך מתנהג כמצופה ועוזרת לך לזהות ולפתור בעיות במהירות. הקטע הבא מפרט גישות מומלצות לאימות יישום MCP שלך.

## סקירה כללית

הלקח הזה מכסה כיצד לבחור את גישת הבדיקה הנכונה ואת כלי הבדיקה היעיל ביותר.

## מטרות הלמידה

עם סיום שיעור זה תוכל:

- לתאר גישות שונות לבדיקות.
- להשתמש בכלים שונים כדי לבדוק את הקוד שלך באופן יעיל.

## בדיקות שרתי MCP

MCP מספק כלים שיעזרו לך לבדוק ולנפות שגיאות בשרתים שלך:

- **MCP Inspector**: כלי שורת פקודה שניתן להריץ גם ככלי CLI וגם ככלי חזותי.
- **בדיקה ידנית**: ניתן להשתמש בכלי כמו curl כדי לבצע בקשות רשת, אבל כל כלי שמסוגל להריץ HTTP יעשה.
- **בדיקות יחידה**: אפשר להשתמש במסגרת הבדיקות המועדפת עליך כדי לבדוק את הפיצ'רים של השרת והלקוח.

### שימוש ב-MCP Inspector

תיארנו את השימוש בכלי זה בשיעורים קודמים, אך נדבר עליו בקצרה ברמה גבוהה. זהו כלי שבנוי ב-Node.js ואתה יכול להשתמש בו על ידי קריאת ההרצה `npx` שתוריד ותתקין את הכלי זמנית ותנקה את עצמך לאחר סיום הרצת הבקשה.

ה-[MCP Inspector](https://github.com/modelcontextprotocol/inspector) עוזר לך:

- **לגלות יכולות שרת**: זיהוי אוטומטי של משאבים, כלים, והנחיות זמינים
- **בדיקת הרצת כלים**: נסה פרמטרים שונים וצפה בתגובות בזמן אמת
- **צפייה במטא-נתוני שרת**: בדוק מידע על השרת, סכימות ותצורות

הרצת הכלי טיפוסית נראית כך:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

הפקודה הנ"ל מפעילה שרת MCP וממשק ויזואלי שלו ומשיקה ממשק רשת מקומי בדפדפן שלך. תוכל לראות לוח המחוונים המציג את שרתי MCP הרשומים שלך, הכלים, המשאבים וההנחיות שלהם. הממשק מאפשר לבדוק אינטראקטיבית הרצת כלים, לבדוק מטא-נתוני שרת, ולראות תגובות בזמן אמת, מה שמקל על אימות וניפוי שגיאות ביישום MCP שלך.

כך זה יכול להיראות: ![Inspector](../../../../translated_images/he/connect.141db0b2bd05f096.webp)

אתה יכול גם להריץ כלי זה במצב CLI שבו מוסיפים את הפרמטר `--cli`. להלן דוגמה להרצת הכלי במצב "CLI" שמפרט את כל הכלים על השרת:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### בדיקה ידנית

מלבד הרצת כלי המפקח לבדוק יכולות שרת, גישה דומה היא להריץ לקוח שמסוגל להשתמש ב-HTTP כמו למשל curl.

עם curl, תוכל לבדוק ישירות שרתי MCP באמצעות בקשות HTTP:

```bash
# דוגמה: מטא-נתוני שרת בדיקה
curl http://localhost:3000/v1/metadata

# דוגמה: הפעלת כלי
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

כפי שניתן לראות מהשימוש הנ"ל ב-curl, אתה משתמש בבקשת POST כדי להפעיל כלי באמצעות מטען הכולל את שם הכלי ופרמטרים שלו. השתמש בגישה שהכי מתאימה לך. כלים של CLI בדרך כלל מהירים יותר לשימוש ונוחים לאוטומציה, מה שיכול להיות שימושי בסביבת CI/CD.

### בדיקות יחידה

צור בדיקות יחידה לכלים ולמשאבים שלך כדי לוודא שהם פועלים כמצופה. הנה דוגמת קוד לבדיקות.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# סמן את כל המודול לבדיקות אסינכרוניות
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # צור כמה כלי בדיקה
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # בדיקה ללא פרמטר סמן (הושמט)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # בדיקה עם סמן=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # בדיקה עם סמן כמחרוזת
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # בדיקה עם מחרוזת סמן ריקה
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

הקוד הקודם עושה את הדברים הבאים:

- משתמש במסגרת pytest שמאפשרת ליצור בדיקות כמשימות ולהשתמש בהצהרות assert.
- יוצר שרת MCP עם שני כלים שונים.
- משתמש ב-`assert` כדי לבדוק שתנאים מסוימים מתקיימים.

עיין בקובץ המלא ב-[קישור כאן](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

בהתבסס על הקובץ למעלה, תוכל לבדוק את השרת שלך כדי לוודא שהיכולות נוצרות כפי שצריך.

כל ערכות הפיתוח הגדולות מכילות חלקי בדיקה דומים, כך שתוכל להתאים לסביבת הריצה שבחרת.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. יש להתייחס למסמך המקורי בשפת המקור כמקור הסמכותי. למידע קריטי מומלץ תרגום מקצועי על ידי אדם. אנו אינם אחראים לכל אי הבנות או פרשנויות שגויות הנובעות מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->