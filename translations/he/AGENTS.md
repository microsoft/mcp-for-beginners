# AGENTS.md

## סקירת הפרויקט

**MCP למתחילים** הוא תכנית לימודים חינוכית בקוד פתוח ללימוד פרוטוקול הקשר לדגם (MCP) - מסגרת סטנדרטית לאינטראקציות בין מודלי AI ליישומי לקוח. מאגר זה מספק חומרי למידה מקיפים עם דוגמאות קוד מעשיות במגוון שפות תכנות.

### טכנולוגיות מרכזיות

- **שפות תכנות**: C#, Java, JavaScript, TypeScript, Python, Rust
- **מסגרות SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **מסדי נתונים**: PostgreSQL עם תוסף pgvector
- **פלטפורמות ענן**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **כלי בניה**: npm, Maven, pip, Cargo
- **תיעוד**: Markdown עם תרגום אוטומטי רב-שפתי (מעל 48 שפות)

### ארכיטקטורה

- **11 מודולים מרכזיים (00-11)**: מסלול למידה סדיר מעקרונות בסיסיים לנושאים מתקדמים
- **מעבדות מעשיות**: תרגילים מעשיים עם קוד פתרון מלא במגוון שפות
- **פרויקטים לדוגמה**: יישומים עובדים לשרת ותצוגת לקוח MCP
- **מערכת תרגום**: זרימת עבודה אוטומטית ב-GitHub Actions לתמיכה רב-שפתית
- **משאבי תמונה**: תיקיית תמונות מרכזית עם גרסאות מתורגמות

## פקודות התקנה

זהו מאגר המתמקד בתיעוד. רוב ההתקנה מתבצעת בפרויקטים לדוגמה ובמעבדות בודדות.

### התקנת המאגר

```bash
# שכפלו את המאגר
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### עבודה עם פרויקטים לדוגמה

הפרויקטים לדוגמה ממוקמים ב:
- `03-GettingStarted/samples/` - דוגמאות לשפות ספציפיות
- `03-GettingStarted/01-first-server/solution/` - יישומי שרת ראשונים
- `03-GettingStarted/02-client/solution/` - יישומי לקוח
- `11-MCPServerHandsOnLabs/` - מעבדות אינטגרציה מקיפות למסד נתונים

כל פרויקט לדוגמה כולל הוראות התקנה משלו:

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
# או
pip install -e .
python main.py
```

#### פרויקטים ב-Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## זרימת עבודה לפיתוח

### מוכנות MCP 7-28

#### רשימת בדיקה למוכנות המאגר

- [x] **בהירות לתורם חדש**: קובץ זה מגדיר את מטרת המאגר,
  המבנה, כללי תרומה, ונתיבי התקנה לדוגמה.
- [x] **פקודות בניה/בדיקה/בדיקת סגנון עם דגלים מדויקים**:
  - בדיקת סגנון למסמכים במאגר:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - ביקורת תבנית קישורים במסמכי המאגר:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - אימות דוגמאות TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - אימות דוגמאות בפייתון:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - אימות דוגמאות ב-Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **זרימת עבודה ריאליסטית שיכולה להפוך לכלי MCP**:
  `validate_curriculum_change`
- [x] **קלט ופלט ברורים** (ראה מפרט למטה).
- [x] **הרשאות ומצבי כישלון מתועדים** (ראה מפרט למטה).
- [x] **בדיקות CI מפורשות** (פקודות דטרמיניסטיות, קודי יציאה מפורשים,
  ופלט קריא למכונה).

#### זרימת העבודה המוצעת לכלי MCP: `validate_curriculum_change`

##### מטרה

לאמת שינויים בתיעוד תוכנית הלימודים וקוד הדוגמה הייצוגי
לפני מיזוג.

##### קלטים

- `changed_paths: string[]` (נדרש) - הנתיבים היחסיים ששונו ב-PR.
- `run_docs_lint: boolean` (ברירת מחדל `true`)
- `run_links_audit: boolean` (ברירת מחדל `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (ברירת מחדל כולם `false`)

##### פלטים

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### הרשאות

- קריאת קבצי סביבת עבודה וכתיבת פריטי ארטיפקט שנוצרו על ידי הכלי (למשל, דוחות בדיקת סגנון,
  יומני בדיקות) בלבד; ללא כתיבה בתיקיות `translations/` או
  `translated_images/`.
- הרצת פקודות shell מקומיות.
- גישה רשתית אופציונלית רק לשחזור חבילות (`npm ci`,
  `python -m pip install`, פתרון תלות ב-`mvn`).
- אין הרשאה לדחיפה, מיזוג או שינוי בתיקיות `translations/` או
  `translated_images/`.

##### מצבי כישלון

- `E_NO_INPUT_PATHS`: `changed_paths` ריקה.
- `E_INVALID_PATH`: נתיב הקלט זורם מחוץ לשורש המאגר.
- `E_LINT_FAILED`: בדיקת סגנון markdown יצאה עם קוד שגיאה.
- `E_LINK_AUDIT_FAILED`: פקודת ביקורת הקישורים יצאה עם שגיאה.
- `E_SAMPLE_TEST_FAILED`: בדיקת/בנית הדוגמה יצאה בשגיאה.
- `E_TIMEOUT`: הפקודה חרגה ממגבלת זמן מוגדרת.

##### חוזה מומלץ ל-CI

לאוטומציה של האימות, יש להגדיר משימת CI ש:

- מופעלת בעת בקשות משיכה שכוללות `*.md`, קודי דוגמה, או קובץ זה.
- מריצה את הפקודות המדויקות המצוינות למעלה.
- שומרת יומנים כפריטי ארטיפקט.
- מבטלת את המשימה על כל קוד יציאה לא אפס.

#### אם אתם משחררים שרת MCP מהמאגר הזה

- [ ] קראו את טיוטת יומן השינויים עבור MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] הריצו את השרת שלכם נגד גרסאות בטא של SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] הסירו הנחות על סשן ו-handshake; טפלו בכל בקשה כמחסנית עצמאית:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] שלחו כותרות `Mcp-Method` ו-`Mcp-Name` עבור בקשות HTTP גולמיות:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] בדקו קודי שגיאה מוקשחים (`missing resource` הועבר מ-`-32002` ל-`-32602`).
- [ ] סמנו ותכננו הגירה לשורשים מיושנים, דגימה, ו
  רישום:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] עברו מה-API הניסיוני `2025-11-25` של משימות:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] בדקו הרשאה להקשחת OAuth ו-OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>




- **translations/**: גרסאות ספציפיות שפה (נוצר אוטומטית, לא לעריכה ישירה)
- **translated_images/**: גרסאות תמונה מותאמות לשפה (נוצר אוטומטית)
- **images/**: תמונות ותרשימים מקוריים




2. עדכנו תמונות בתיקיית `images/` אם נדרש
3. הפעולה co-op-translator ב-GitHub תייצר תרגומים אוטומטית
4. התרגומים מתעדכנים בלחיצה לסניף הראשי




- **אסור לערוך ידנית** קבצים בתיקיית `translations/`
- מטא-נתוני תרגום מוטמעים בכל קובץ מתורגם
- שפות נתמכות: מעל 48 שפות כולל ערבית, סינית, צרפתית, גרמנית, הינדי, יפנית, קוריאנית,
פורטוגזית, רוסית, ספרדית, ועוד רבות

## הוראות בדיקה

### אימות התיעוד

מאחר שמדובר בעיקר במאגר תיעוד, הבדיקות מתמקדות ב:

1. **ביקורת תבנית קישורים**: רשימת קישורי Markdown לבדיקה

   ```bash
   # רשימת קישורי Markdown (בדיקת תבנית)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **אימות דוגמאות קוד**: בדיקה שהדוגמאות מקומפילות/רץ

   ```bash
   # נווט לדוגמה ספציפית והרץ את הבדיקות שלה
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **בדיקת סגנון Markdown**: בדיקת עקביות הפורמט

   ```bash
   # השתמש ב-markdownlint אם צריך
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### בדיקת פרויקטים לדוגמה

כל דוגמה לשפה כוללת שיטת בדיקה משלה:

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

## הנחיות לסגנון קוד

### סגנון התיעוד

- השתמשו בשפה ברורה, ידידותית למתחילים
- כללו דוגמאות קוד במגוון שפות כשמתאים
- עקבו אחרי שיטות Markdown מיטביות:
  - השתמשו בכותרות סגנון ATX (`#`)
  - השתמשו בבלוקים סגורים עם זיהוי שפה
  - כללו טקסט חלופי לתמונות
  - שמרו על אורך שורות סביר (לא חובה קפדנית, אך הגיונית)

### סגנון דוגמאות קוד

#### TypeScript/JavaScript
- השתמשו במודולים ES (`import`/`export`)
- עקבו אחרי קונבנציות מצב קשוח של TypeScript
- כללו הערות טיפוס
- תגיעו ל-ES2022

#### Python
- עקבו אחרי הנחיות סגנון PEP 8
- השתמשו ברמזי טיפוס כשמתאים
- כללו docstrings לפונקציות ומחלקות
- השתמשו בתכונות Python מודרניות (3.8+)

#### Java
- עקבו אחרי קונבנציות Spring Boot
- השתמשו בתכונות Java 21
- עקבו אחרי מבנה פרויקט סטנדרטי ב-Maven
- כללו הערות Javadoc

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

## בניה ופריסה

### פריסת תיעוד

המאגר משתמש ב-GitHub Pages או דומה לאחסון תיעוד (אם רלוונטי). שינויים בסניף הראשי מפעילים:

1. זרימת עבודה לתרגום (`.github/workflows/co-op-translator.yml`)
2. תרגום אוטומטי של כל קבצי Markdown באנגלית
3. לוקליזציה של תמונות לפי הצורך

### אין צורך בתהליך בניה

מאגר זה מכיל בעיקר תיעוד Markdown. אין צורך בקומפילציה או תהליך בניה לתוכן הליבה של התכנית.

### פריסת פרויקטים לדוגמה

לפרויקטים לדוגמה בודדים עשויות להיות הוראות פריסה:
- ראו `03-GettingStarted/09-deployment/` להנחיות פריסת שרת MCP
- דוגמאות לפריסת Azure Container Apps ב-`11-MCPServerHandsOnLabs/`

## הנחיות לתרומה

### תהליך בקשת משיכה

1. **פיצול ושכפול**: פצלו את המאגר ושכפלו את הפיצול מקומית
2. **יצירת ענף**: השתמשו בשמות ענפים תיאוריים (למשל, `fix/typo-module-3`, `add/python-example`)
3. **ביצוע שינויים**: ערכו רק את קבצי markdown באנגלית (לא את התרגומים)
4. **בדיקה מקומית**: ודאו ש-Markdown מוצג נכון
5. **שליחת PR**: השתמשו בכותרות ותיאורים ברורים לבקשות המשיכה
6. **חתימה על הסכם CLA**: חתמו על הסכם הרישיון לתורמים של Microsoft עם הבקשה

### פורמט כותרת בקשה למשיכה

השתמשו בכותרות ברורות ותיאוריות:
- `[Module XX] תיאור קצר` לשינויים ספציפיים למודול
- `[Samples] תיאור` לשינויים בדוגמאות קוד
- `[Docs] תיאור` לעדכוני תיעוד כלליים

### מה לתרום

- תיקוני באגים בתיעוד או בדוגמאות קוד
- דוגמאות קוד חדשות בשפות נוספות
- הבהרות ושיפורים לתוכן קיים
- מקרי מבחן חדשים או דוגמאות מעשיות
- דיווחי בעיות לתוכן לא ברור או שגוי

### מה לא לעשות

- אל תערכו ישירות קבצים בתיקיית `translations/`
- אל תערכו את תיקיית `translated_images/`
- אל תוסיפו קבצים בינאריים גדולים ללא שיח
- אל תשנו קבצי זרימת עבודה לתרגום ללא תיאום

## הערות נוספות

### תחזוקת המאגר

- **יומן שינויים**: כל השינויים המשמעותיים מתועדים ב-`changelog.md`
- **מדריך לימודים**: השתמשו ב-`study_guide.md` לסקירת ניווט בתכנית הלימודים
- **תבניות דיווח**: השתמשו בתבניות דיווח ב-GitHub לדיווח באגים ובקשות תכונות
- **קוד התנהגות**: כל התורמים חייבים לעקוב אחרי קוד ההתנהגות של Microsoft Open Source

### מסלול למידה

עקבו אחרי מודולים בסדר סידורי (00-11) ללמידה מיטבית:
1. **00-02**: יסודות (הקדמה, קונספטים מרכזיים, אבטחה)
2. **03**: התחלה עם יישום מעשי
3. **04-05**: יישום מעשי ונושאים מתקדמים
4. **06-10**: קהילה, שיטות מיטביות, ויישומים מעשיים
5. **11**: מעבדות אינטגרציה מקיפות למסדי נתונים (13 מעבדות עוקבות)

### משאבי תמיכה

- **תיעוד**: https://modelcontextprotocol.io/
- **מפרט**: https://spec.modelcontextprotocol.io/
- **קהילה**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: שרת Discord של Microsoft Foundry
- **קורסים קשורים**: ראו README.md לנתיבי למידה נוספים של Microsoft

### פתרון תקלות נפוץ

**ש: בקשת המשיכה שלי נכשלת בבדיקת התרגום**
ת: וודאו שערכתם רק את קבצי ה-Markdown באנגלית בתיקיות המודולים הראשיים, לא את הגרסאות המתורגמות.

**ש: איך מוסיפים שפה חדשה?**
ת: תמיכת השפות מנוהלת דרך זרימת העבודה co-op-translator. פתחו נושא לדיון בהוספת שפות חדשות.

**ש: דוגמאות הקוד לא עובדות**

תשובה: ודא שעקבת אחרי הוראות ההתקנה בקובץ ה-README של הדוגמה הספציפית. בדוק שיש לך את הגרסאות הנכונות של התלויות מותקנות.

**שאלה: התמונות לא מוצגות**
תשובה: אמת כי הנתיבים לתמונות יחסיים ומשתמשים בשרטוטים קדמיים. התמונות צריכות להיות בתיקיית `images/` או `translated_images/` עבור גרסאות מתורגמות.

### שיקולי ביצועים

- תהליך התרגום עשוי לקחת מספר דקות להשלמה
- יש לייעל תמונות גדולות לפני המחויבות
- שמור על קבצי markdown אינדיבידואליים ממוקדים ובעלי גודל סביר
- השתמש בקישורים יחסיים לניידות טובה יותר

### ממשל הפרויקט

הפרויקט הזה עוקב אחר נהלי קוד פתוח של מיקרוסופט:
- רישיון MIT לקוד ותיעוד
- קוד התנהגות לקוד פתוח של מיקרוסופט
- דרוש CLA לתרומות
- נושאי אבטחה: עקוב אחר הנחיות SECURITY.md
- תמיכה: ראה SUPPORT.md עבור משאבי סיוע

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->