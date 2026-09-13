# הפעלת הדוגמה הזו

מומלץ להתקין את `uv` אך זה לא חובה, עיין ב[הוראות](https://docs.astral.sh/uv/#highlights)

## -0- צור סביבת עבודה וירטואלית

```bash
python -m venv venv
```

## -1- הפעל את סביבת העבודה הווירטואלית

```bash
venv\Scripts\activate
```

## -2- התקן את התלויות

```bash
pip install "mcp[cli]"
```

## -3- הפעל את הדוגמה

```bash
python client.py
```

אתה אמור לראות פלט דומה ל:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->