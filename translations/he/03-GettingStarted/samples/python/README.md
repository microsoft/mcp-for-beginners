# שרת מחשבון MCP (פייתון)



מימוש פשוט של שרת Model Context Protocol (MCP) בפייתון המספק פונקציונליות בסיסית של מחשבון.


## התקנה

התקן את התלויות הדרושות:

```bash
pip install -r requirements.txt
```

או התקן את MCP Python SDK ישירות:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## שימוש

### הפעלת השרת

השרת מיועד לשימוש על ידי לקוחות MCP (כמו Claude Desktop). כדי להפעיל את השרת:

```bash
python mcp_calculator_server.py
```

**הערה**: בעת הפעלה ישירה בטרמינל, תראה שגיאות אימות JSON-RPC. זהו התנהגות נורמלית - השרת מחכה להודעות לקוח MCP בפורמט תקין.

### בדיקת הפונקציות

כדי לבדוק שהפונקציות במחשבון פועלות כראוי:

```bash
python test_calculator.py
```

## פתרון בעיות

### שגיאות ייבוא

אם אתה רואה `ModuleNotFoundError: No module named 'mcp'`, התקן את MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### שגיאות JSON-RPC בעת הרצה ישירה

שגיאות כמו "Invalid JSON: EOF while parsing a value" בעת הרצת השרת ישירות הן צפויות. השרת זקוק להודעות של לקוח MCP, לא לקלט ישיר מהטרמינל.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->