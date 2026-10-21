# AGENTS.md

## סקירת הפרויקט

**MCP למתחילים** הוא תכנית לימודים חינוכית בקוד פתוח ללימוד פרוטוקול הקשר מודל (MCP) - מסגרת סטנדרטית לאינטראקציות בין מודלים של בינה מלאכותית ליישומי לקוח. מאגר זה מספק חומרי למידה מקיפים עם דוגמאות קוד מעשיות במגוון שפות תכנות.

### טכנולוגיות מפתח

- **שפות תכנות**: C#, Java, JavaScript, TypeScript, Python, Rust
- **מסגרות ו-SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **מאגרי נתונים**: PostgreSQL עם תוסף pgvector
- **פלטפורמות ענן**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **כלי בנייה**: npm, Maven, pip, Cargo
- **תיעוד**: Markdown עם תרגום אוטומטי רב-שפות (48+ שפות)

### ארכיטקטורה

- **11 מודולים מרכזיים (00-11)**: מסלול למידה רציף מהיסודות לנושאים מתקדמים
- **מעבדות מעשיות**: תרגילים מעשיים עם קוד פתרון מלא במגוון שפות
- **פרויקטי דוגמה**: מימושי שרת ולקוח של MCP עובדי
- **מערכת תרגום**: תהליך עבודה אוטומטי ב-GitHub Actions לתמיכה ברב-שפות
- **נכסי תמונה**: תיקיית תמונות מרכזית עם גרסאות מתורגמות

## פקודות התקנה

זהו מאגר ממוקד תיעוד. רוב ההתקנה מתבצעת בתוך פרויקטים לדוגמה ומעבדות פרטניות.

### התקנת המאגר

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### עבודה עם פרויקטי דוגמה

פרויקטי הדוגמה נמצאים ב:
- `03-GettingStarted/samples/` - דוגמאות ספציפיות לשפה
- `03-GettingStarted/01-first-server/solution/` - מימושי שרת ראשוניים
- `03-GettingStarted/02-client/solution/` - מימושי לקוח
- `11-MCPServerHandsOnLabs/` - מעבדות אינטגרציה מקיפות למאגרי נתונים

כל פרויקט דוגמה כולל הוראות התקנה משלו:

#### פרויקטים ב-TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### פרויקטים בפייתון
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### פרויקטים ב-Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## תהליך פיתוח

### מוכנות MCP 7-28

#### רשימת בדיקת מוכנות המאגר

- [x] **בהירות לתורם חדש**: קובץ זה מגדיר את מטרת המאגר, 
  מבנה, כללי תרומה, ונתיבי התקנה לדוגמא.
- [x] **פקודות בנייה/בדיקה/לינט עם דגלים מדויקים**:
  - לינט לתיעוד המאגר:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - ביקורת תבניות קישורים לתיעוד המאגר:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - אימות דוגמאות TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - אימות דוגמאות Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - אימות דוגמאות Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **תהליך עבודה ריאליסטי אחד שיכול להפוך לכלי MCP**:
  `validate_curriculum_change`
- [x] **קלט/פלט מפורשים** (ראה מפרט למטה).
- [x] **הרשאות ומצבי כשל מתועדים** (ראה מפרט למטה).
- [x] **יכולת בדיקת CI מפורשת** (פקודות דטרמיניסטיות,
  קודי יציאה מפורשים, ופלט קריא למכונה).

#### תהליך עבודה מועמד לכלי MCP: `validate_curriculum_change`

##### מטרה

לאמת את שינויי התיעוד בתכנית הלימודים ואת בריאות קוד הדוגמה המייצגת לפני המיזוג.


##### קלטים

- `changed_paths: string[]` (נדרש) - שינו נתיבים יחסיים ב-PR.
- `run_docs_lint: boolean` (ברירת מחדל `true`)
- `run_links_audit: boolean` (ברירת מחדל `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (ברירת מחדל כל `false`)

##### פלטים

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### הרשאות

- קריאת קבצי סביבת עבודה וכתיבת ארטיפקטים שנוצרו על ידי הכלי (למשל, דוחות לינט,
  יומני בדיקות) בלבד; ללא כתיבות ל-`translations/` או
  `translated_images/`.
- הרצת פקודות shell מקומיות.
- גישה רשת אופציונלית רק להשבתת חבילות (`npm ci`,
  `python -m pip install`, פתרון תלות של `mvn`).
- אין הרשאה לדחיפה, מיזוג או שינוי `translations/` או
  `translated_images/`.

##### מצבי כשל

- `E_NO_INPUT_PATHS`: `changed_paths` ריק.
- `E_INVALID_PATH`: נתיב הקלט יוצא משורש המאגר.
- `E_LINT_FAILED`: לינט Markdown יוצא עם קוד שגיאה.
- `E_LINK_AUDIT_FAILED`: פקודת ביקורת קישורים יוצאת עם קוד שגיאה.
- `E_SAMPLE_TEST_FAILED`: דוגמת בדיקה/בנייה יוצאת עם קוד שגיאה.
- `E_TIMEOUT`: הפקודה חרגה ממועד ההמתנה המוגדר.

##### חוזה CI מומלץ

לאוטומציה של האימות, קבע משימת CI ש:

- מפעילה על בקשות משיכה שנוגעות ל-`*.md`, קוד דוגמה או קובץ זה.
- מריצה את הפקודות המדויקות שמפורטות למעלה.
- שומרת יומנים כארטיפקטים.
- מכשלת את המשימה על כל קוד יציאה שאינו אפס.

#### אם אתם משדרים שרת MCP מהמאגר הזה

- [ ] קריאת יומן השינויים הסופי של MCP `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] אימות שגרסת SDK שנבחרה תומכת ב-MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] הסרת הנחות על מושב והידוק יד; לטפל בכל בקשה כ
  עצמאית:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] שליחת כותרות `Mcp-Method` ו-`Mcp-Name` עבור בקשות HTTP גולמיות:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] ביקורת על קודי שגיאה מוצפנים (`missing resource` הועבר מ-`-32002` ל-`-32602`).
- [ ] מיגרציה של Roots, Sampling, Logging, והירשם דינמי ללקוח:

  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] מיגרציה מ-API הניסיוני של `2025-11-25` Tasks:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] סקירת אישור עבור OAuth והקשחת OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### מבנה התיעוד

- **מודולים 00-11**: תוכן הליבה בקורס בסדר הכרונולוגי
- **translations/**: גרסאות בשפות ספציפיות (נוצר אוטומטית, אין לערוך ישירות)
- **translated_images/**: גרסאות תמונה מתורגמות (נוצר אוטומטית)
- **images/**: תמונות ומדגמים מקוריים

### ביצוע שינויים בתיעוד

1. עריכת קבצי markdown באנגלית בלבד בתיקיות מודולים השורשיות (00-11)
2. עדכון תמונות בתיקיית `images/` במידת הצורך
3. פעולת GitHub co-op-translator תיצור אוטומטית תרגומים
4. תרגומים מיוצרים מחדש על כל דחיפה לענף הראשי

### עבודה עם תרגומים

- **תרגום אוטומטי**: זרימת העבודה GitHub Actions מטפלת בכל התרגומים
- **אין לערוך ידנית** קבצים בתיקיית `translations/`
- מטאדאטה של התרגום מוטמעת בכל קובץ מתורגם
- שפות נתמכות: 48+ שפות כולל ערבית, סינית, צרפתית, גרמנית, הינדית, יפנית, קוריאנית, פורטוגזית, רוסית, ספרדית ועוד רבות

## הוראות בדיקה

### אימות תיעוד

מאחר ומדובר בעיקר במאגר תיעוד, הבדיקות מתמקדות ב:

1. **בדיקת תבנית קישורים**: רשימת קישורי Markdown לסקירה

   ```bash
   # List Markdown links (pattern audit)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **אימות דוגמת קוד**: בדוק שדוגמאות הקוד מתרגמות/מפעלות

   ```bash
   # Navigate to specific sample and run its tests
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **בדיקת Markdown (Linting)**: בדוק עקביות עיצוב

   ```bash
   # Use markdownlint if needed
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### בדיקת פרויקט לדוגמה

לכל דוגמה ספציפית לשפה יש גישת בדיקה משלה:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## הנחיות סגנון קוד

### סגנון תיעוד

- השתמש בשפה ברורה וידידותית למתחילים
- כלול דוגמאות קוד בשפות שונות כשמתאים
- עקוב אחר שיטות העבודה הטובות של markdown:
  - השתמש בכותרות בסגנון ATX (`#` תחביר)
  - השתמש בבלוקים של קוד עם מזהי שפה
  - כלול טקסט אלטרנטיבי תיאורי לתמונות
  - שמור על אורך שורות סביר (ללא הגבלה נוקשה, אך הייה הגיוני)

### סגנון דוגמת קוד

#### TypeScript/JavaScript
- השתמש במודולי ES (`import`/`export`)
- עקוב אחר קונבנציות מצב מחמיר של TypeScript
- כלול אנוטציות טיפוס
- מטרה ES2022

#### Python
- עקוב אחר הנחיות סגנון PEP 8
- השתמש ברמזי טיפוס כשמתאים
- כלול docstrings לפונקציות ומחלקות
- השתמש בתכונות Python מודרניות (3.8+)

#### Java
- עקוב אחר קונבנציות Spring Boot
- השתמש בתכונות Java 21
- עקוב אחר מבנה פרויקט Maven סטנדרטי
- כלול הערות Javadoc

### ארגון קבצים

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## בנייה ופריסה

### פריסת תיעוד

המאגר משתמש ב-GitHub Pages או דומה לאירוח תיעוד (אם רלוונטי). שינויים בענף הראשי מפעילים:

1. תהליך תרגום (`.github/workflows/co-op-translator.yml`)
2. תרגום אוטומטי של כל קבצי markdown באנגלית
3. מיקום תמונות לפי הצורך

### אין צורך בתהליך בנייה

מאגר זה מכיל בעיקר תיעוד markdown. אין צורך בצעד הרכבה או בנייה לתוכן הליבת קורס.

### פריסת פרויקט לדוגמה

לפרויקטים לדוגמה בודדים עשויות להיות הוראות פריסה:
- ראה `03-GettingStarted/09-deployment/` להנחיות פריסת שרת MCP
- דוגמאות לפריסת Azure Container Apps ב`11-MCPServerHandsOnLabs/`

## הנחיות לתרומה

### תהליך בקשת משיכה (Pull Request)

1. **תפוס ושכפל**: תפוס את המאגר ושכפל את התפיסה מקומית
2. **צור ענף**: השתמש בשמות ענף תיאוריים (למשל `fix/typo-module-3`, `add/python-example`)
3. **בצע שינויים**: ערוך רק קבצי markdown באנגלית (לא תרגומים)
4. **בדוק מקומית**: וודא שה-markdown מוצג כראוי
5. **הגש PR**: השתמש בכותרות ותיאורים ברורים ל-PR
6. **CLA**: חתום על הסכם תרומת מיקרוסופט כשמתבקש

### פורמט כותרת PR

השתמש בכותרות ברורות ותיאוריות:
- `[Module XX] Brief description` לשינויים ספציפיים למודול
- `[Samples] Description` לשינויים בדוגמאות קוד
- `[Docs] Description` לעדכוני תיעוד כלליים

### מה לתרום

- תיקוני שגיאות בתיעוד או דוגמאות קוד
- דוגמאות קוד חדשות בשפות נוספות
- הבהרות ושיפורים לתוכן קיים
- מחקרים מקרה חדשים או דוגמאות מעשיות
- דיווחי בעיות על תוכן לא ברור או שגוי

### מה לא לעשות

- אל תערוך קבצים ישירות בתיקיית `translations/`
- אל תערוך את תיקיית `translated_images/`
- אל תוסיף קבצי בינאר גדולים ללא דיון
- אל תשנה קבצי תהליך תרגום ללא תיאום

## הערות נוספות

### תחזוקת מאגר

- **יומן שינויים**: כל השינויים המשמעותיים מתועד ב`changelog.md`
- **מדריך לימוד**: השתמש ב`study_guide.md` לתצוגת ניווט תוכנית הלימודים
- **תבניות בעיה**: השתמש בתבניות בעיות של GitHub לדיווח באגים ובקשות תכונות
- **קוד התנהגות**: כל התורמים חייבים לעקוב אחר קוד ההתנהגות של מיקרוסופט בקוד פתוח

### מסלול למידה

עקוב אחר המודולים בסדר רציף (00-11) ללמידה מיטבית:
1. **00-02**: יסודות (הקדמה, מושגי יסוד, אבטחה)
2. **03**: התחלה עם יישום מעשי
3. **04-05**: יישום מעשי ונושאים מתקדמים
4. **06-10**: קהילה, שיטות עבודה מיטביות ויישומים בעולם האמיתי
5. **11**: מעבדות אינטגרציה מקיפות למסדי נתונים (13 מעבדות רצופות)

### משאבי תמיכה

- **תיעוד**: https://modelcontextprotocol.io/
- **מפרט**: https://modelcontextprotocol.io/specification/2026-07-28/
- **קהילה**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: שרת Discord של Microsoft Foundry
- **קורסים קשורים**: ראה README.md בשביל מסלולי הלימוד האחרים של מיקרוסופט

### פתרון בעיות נפוצות

**ש: ה-PR שלי נכשל בבדיקת תרגום**
תשובה: ודא שערכת רק קבצי markdown באנגלית בתיקיות המודולים הראשיות, לא גרסאות מתורגמות.

**ש: איך אני מוסיף שפה חדשה?**
תשובה: תמיכת השפה מנוהלת באמצעות תהליך co-op-translator. פתח נושא לדיון על הוספת שפות חדשות.

**ש: דוגמאות הקוד לא עובדות**
תשובה: ודא שנקטת את הוראות ההגדרה בקובץ README של הדוגמה הספציפית. בדוק שיש לך את הגרסאות הנכונות של התלויות מותקנות.

**ש: התמונות לא מוצגות**
תשובה: אמת את נתיבי התמונות הם יחסיים ומשתמשים בסלאשים קדימה. התמונות צריכות להיות בתיקיית `images/` או `translated_images/` עבור גרסאות מתורגמות.

### שיקולי ביצועים

- תהליך התרגום עלול לקחת כמה דקות להשלמה
- תמונות גדולות יש לאופטימיזציה לפני ההתחייבות
- שמור על קבצי markdown ממוקדים ובגודל סביר
- השתמש בקישורים יחסיים לניידות טובה יותר

### ממשל פרויקט

פרויקט זה עוקב אחרי שיטות קוד פתוח של מיקרוסופט:
- רישיון MIT לקוד ותיעוד
- קוד התנהגות קוד פתוח של מיקרוסופט
- דרוש CLA לתרומות
- נושאי אבטחה: עקוב אחר הנחיות SECURITY.md
- תמיכה: ראה את SUPPORT.md עבור משאבי עזרה

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->