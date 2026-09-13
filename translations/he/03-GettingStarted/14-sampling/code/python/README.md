# הרץ את הדוגמה

> [!WARNING]
> הדוגמה הזו משתמשת בדגימה מיושנת ובנקודת קצה HTTP+SSE ישנה. היא
> נשמרת לצורך תאימות עם MCP `2025-11-25`. מימושים חדשים צריכים לקרוא
> ישירות לספק LLM ולהשתמש ב-HTTP סטרימי לתעבורת MCP מרוחקת.

## צור סביבה וירטואלית

```sh
python -m venv venv
source ./venv/bin/activate
```

## התקן תלותיות

```sh
pip install "mcp[cli]"
```

## הרץ את השרת

```sh
uvicorn server:app --port 8000
```

## בדוק את השרת עם GitHub Copilot ו-VS Code

הוסף את הערך ל-mcp.json כך:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

וודא שאתה לוחץ על "start" על השרת.

ב-GitHub Copilot הדבק את ההנחיה הבאה:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

בפעם הראשונה תתבקש האם לאשר את פעולת Sampling, ואז תתבקש לאשר לכלי להריץ "create_blog". תראה תגובה דומה ל:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->