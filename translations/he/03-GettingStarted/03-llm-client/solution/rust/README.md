# הפעלת הדוגמה הזו

זוהי הפתרון ב-Rust לדוגמת ה-LLM client. יש צורך בכלי עבודה של Rust מותקן; ראה את [המדריך הרשמי להתקנה](https://www.rust-lang.org/tools/install).

הלקוח קורא למודל Microsoft Foundry לפריסה דרך נקודת הקצה Azure OpenAI
v1.

> [!NOTE]
> הערך המועבר כ-`model` הוא שם הפריסה שלך ב-Foundry, ולא בהכרח
> שם המודל הבסיסי.

## -0- קונפיגורציה של Microsoft Foundry

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
$env:AZURE_OPENAI_API_KEY = "<api-key>"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
```

## -1- בניית הדוגמה

```bash
cargo build
```

## -2- הפעלת הדוגמה

```bash
cargo run
```

הלקוח מפעיל את שרת MCP של המחשבון, מושך את רשימת הכלים שלו, ומשתמש
במודל שפרסת כדי לקרוא לכלי `add`. אמור להופיע פלט המציג
את קריאת הכלי (למשל, "Calling tool: add") ואת תוצאת הקריאה.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->