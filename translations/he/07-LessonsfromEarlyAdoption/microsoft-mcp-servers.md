# 🚀 10 שרתי Microsoft MCP שמשנים את פרודוקטיביות המפתחים

## 🎯 מה תלמדו במדריך הזה

מדריך מעשי זה מציג עשרה שרתי Microsoft MCP שמשנים באופן פעיל את אופן העבודה של מפתחים עם עוזרי AI. במקום רק להסביר מה שרתי MCP *יכולים* לעשות, נראה לכם שרתים שכבר עושים הבדל אמיתי בזרימות העבודה היומיות של הפיתוח במיקרוסופט ומעבר לה.

כל שרת במדריך זה נבחר בהתבסס על שימוש בעולם האמיתי ומשוב מפתחים. תגלה לא רק מה כל שרת עושה, אלא למה זה חשוב ואיך להפיק את המירב ממנו בפרויקטים שלך. בין אם אתה חדש לחלוטין ל-MCP או מחפש להרחיב את ההתקנה הקיימת שלך, שרתים אלה מייצגים כמה מהכלים הפרקטיים והמשפיעים ביותר הזמינים באקוסיסטם של מיקרוסופט.

> **💡 טיפ התחלה מהירה**
>
> חדש ב-MCP? אל תדאג! מדריך זה מיועד להיות ידידותי למתחילים. נסביר מושגים תוך כדי, ותוכל תמיד להפנות חזרה למודולים שלנו [מבוא ל-MCP](../00-Introduction/README.md) ו-[מושגי בסיס](../01-CoreConcepts/README.md) לרקע עמוק יותר.

## סקירה כללית

מדריך מקיף זה חוקר עשרה שרתי Microsoft MCP שמהפכנים את אופן האינטראקציה של מפתחים עם עוזרי AI וכלים חיצוניים. מניהול משאבים ב-Azure ועד עיבוד מסמכים, שרתים אלה מדגימים את כוח פרוטוקול הקשר הדגם ביצירת זרימות עבודה חלקות ופרודוקטיביות בפיתוח.

## מטרות הלמידה

בסוף מדריך זה, תלמדו:
- להבין איך שרתי MCP משפרים את פרודוקטיביות המפתחים
- ללמוד על המימושים המשפיעים ביותר של שרתי MCP של מיקרוסופט
- לגלות מקרי שימוש פרקטיים לכל שרת
- לדעת איך להגדיר ולהתאים שרתים אלה ב-VS Code ו-Visual Studio
- לחקור את האקוסיסטם הרחב יותר של MCP וכיוונים לעתיד

## 🔧 הבנת שרתי MCP: מדריך למתחילים

### מה הם שרתי MCP?

בתור מתחיל ל-Model Context Protocol (MCP), אולי תשאל: "מה בדיוק שרת MCP, ולמה זה חשוב לי?" נתחיל באנלוגיה פשוטה.

תחשוב על שרתי MCP כעוזרים מיוחדים שעוזרים לעוזר הקוד שלך מבוסס AI (כמו GitHub Copilot) להתחבר לכלים ושירותים חיצוניים. כמו שאתה משתמש באפליקציות שונות בטלפון שלך למשימות שונות – אחת למזג אוויר, אחרת לניווט, אחת לבנקאות – שרתי MCP נותנים לעוזר ה-AI שלך את היכולת לתקשר עם כלים ושירותים שונים לפיתוח.

### הבעיה ששרתי MCP פותרים

לפני שרתי MCP, אם רצית:
- לבדוק את משאבי Azure שלך
- ליצור issue ב-GitHub
- לשאול את מסד הנתונים שלך
- לחפש בתיעוד

היית צריך להפסיק לקודד, לפתוח דפדפן, לנווט לאתר המתאים, ולבצע ידנית את המשימות. החלפת הקשר מתמדת זו שוברת את הזרימה שלך ומפחיתה את הפרודוקטיביות.

### איך שרתי MCP משנים את חווית הפיתוח שלך

עם שרתי MCP, אתה יכול להישאר בסביבת הפיתוח שלך (VS Code, Visual Studio וכו') ופשוט לבקש מהעוזר AI שלך לטפל במשימות אלה. לדוגמה:

**במקום זרימת עבודה מסורתית זו:**
1. להפסיק לקודד
2. לפתוח דפדפן
3. לנווט לפורטל Azure
4. לחפש פרטים של חשבון אחסון
5. לחזור ל-VS Code
6. להמשיך לקודד

**אתה יכול עכשיו לעשות זאת:**
1. לשאול את ה-AI: "מה מצב חשבונות האחסון שלי ב-Azure?"
2. להמשיך לקודד עם המידע שסופק

### יתרונות עיקריים למתחילים

#### 1. 🔄 **להישאר במצב זרימה**
- לא להחליף בין אפליקציות מרובות יותר
- לשמור על המיקוד בקוד שאתה כותב
- להפחית עומס מנטלי של ניהול כלים שונים

#### 2. 🤖 **להשתמש בשפה טבעית במקום פקודות מורכבות**
- במקום לזכור תחביר SQL, לתאר איזה מידע אתה צריך
- במקום לזכור פקודות Azure CLI, להסביר מה אתה רוצה להשיג
- לתת ל-AI לטפל בפרטים הטכניים בעוד אתה מתמקד בלוגיקה

#### 3. 🔗 **לחבר בין כלים מרובים**
- ליצור זרימות עבודה עוצמתיות על ידי שילוב שירותים שונים
- דוגמה: "קבל את כל ה-issues האחרונים מ-GitHub ויצר פריטים מתאימים ב-Azure DevOps"
- לבנות אוטומציות ללא כתיבת סקריפטים מורכבים

#### 4. 🌐 **גישה לאקוסיסטם הולך וגדל**
- להנות משרתים שנבנו על ידי מיקרוסופט, GitHub וחברות נוספות
- לשלב כלים של ספקים שונים בצורה חלקה
- להצטרף לאקוסיסטם סטנדרטי העובד עם עוזרי AI שונים

#### 5. 🛠️ **ללמוד דרך עשייה**
- להתחיל עם שרתים מוכנים להבנה של המושגים
- לבנות שרתים משלך בהדרגה ככל שאתה מתרגל יותר
- להשתמש ב-SDKים והדוקומנטציה הזמינים להנחיית הלמידה

### דוגמה מהעולם האמיתי למתחילים

נניח שאתה חדש בפיתוח ווב ועובד על הפרויקט הראשון שלך. כך שרתי MCP יכולים לעזור:

**גישה מסורתית:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**עם שרתי MCP:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### היתרון בסטנדרט הארגוני

MCP הופך לסטנדרט רחב בתעשייה, כלומר:
- **עקביות**: חוויה דומה בכלים ובחברות שונות
- **אינטרופרביליות**: שרתים מספקים שונים פועלים יחד
- **הבטחת עתיד**: מיומנויות והתקנות עוברות בין עוזרי AI שונים
- **קהילה**: אקוסיסטם גדול של ידע משותף ומשאבים

### התחלת העבודה: מה תלמדו

במדריך זה נחקור 10 שרתי Microsoft MCP השימושיים במיוחד למפתחים בכל הרמות. כל שרת מיועד ל:
- לפתור אתגרים נפוצים בפיתוח
- להפחית משימות חוזרות
- לשפר את איכות הקוד
- להעצים הזדמנויות למידה

> **💡 טיפ למידה**
>
> אם אתה חדש לחלוטין ל-MCP, התחל במודולים שלנו [מבוא ל-MCP](../00-Introduction/README.md) ו-[מושגי בסיס](../01-CoreConcepts/README.md). לאחר מכן חזור לכאן לראות את המושגים האלה בעשייה עם כלים אמיתיים של מיקרוסופט.
>
> להקשר נוסף על החשיבות של MCP, עיין בפוסט של מריה נאגגה: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## התחלת העבודה עם MCP ב-VS Code ו-Visual Studio 🚀

ההגדרה של שרתי MCP אלה פשוטה אם אתה משתמש ב-Visual Studio Code או Visual Studio 2022 עם GitHub Copilot.

### הגדרת VS Code

הנה התהליך הבסיסי ל-VS Code:

1. **הפעל מצב סוכן**: ב-VS Code, החלף למצב סוכן בחלון שיחת Copilot
2. **הגדר שרתי MCP**: הוסף הגדרות שרת לקובץ settings.json של VS Code
3. **הפעל שרתים**: לחץ על כפתור "הפעל" לכל שרת שברצונך להשתמש בו
4. **בחר כלים**: בחר אילו שרתי MCP לאפשר במפגש הנוכחי שלך

להוראות הגדרה מפורטות, עיין ב-[תיעוד MCP של VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 טיפ מקצועי: נהל שרתי MCP כמו מקצוען!**
>
> תצוגת ההרחבות ב-VS Code כוללת כעת [ממשק משתמש נוח לניהול שרתי MCP מותקנים](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! יש לך גישה מהירה להתחלה, עצירה וניהול כל שרתי MCP המותקנים עם ממשק ברור ופשוט. נסה זאת!

### הגדרת Visual Studio 2022

עבור Visual Studio 2022 (גרסה 17.14 ומעלה):

1. **הפעל מצב סוכן**: לחץ על תפריט הנפתח "שאל" בחלון שיחת GitHub Copilot ובחר "סוכן"
2. **צור קובץ הגדרות**: צור קובץ `.mcp.json` בספריית הפתרון שלך (המיקום המומלץ: `<SOLUTIONDIR>\.mcp.json`)
3. **הגדר שרתים**: הוסף את הגדרות שרת MCP שלך באמצעות הפורמט הסטנדרטי של MCP
4. **אישור כלים**: כאשר תתבקש, אשר את הכלים שברצונך להשתמש בהם עם הרשאות מתאימות להיקף

להוראות הגדרה מפורטות ל-Visual Studio, עיין ב-[תיעוד MCP של Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

לכל שרת MCP יש דרישות הגדרה משלו (מחרוזות חיבור, אימות וכו') אך דפוס ההגדרה אחיד בשני סביבות הפיתוח.

## לקח משרתי Microsoft MCP 🛠️

### 1. 📚 שרת Microsoft Learn Docs MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**מה הוא עושה**: שרת Microsoft Learn Docs MCP הוא שירות ענן שמספק לעוזרי AI גישה בזמן אמת לתיעוד הרשמי של מיקרוסופט דרך Model Context Protocol. הוא מתחבר ל-`https://learn.microsoft.com/api/mcp` ומאפשר חיפוש סמנטי ברחבי Microsoft Learn, תיעוד Azure, תיעוד Microsoft 365 ומקורות רשמיים אחרים של מיקרוסופט.

**למה זה שימושי**: למרות שזה נראה כמו "סתם תיעוד", שרת זה חיוני לכל מפתח המשתמש בטכנולוגיות מיקרוסופט. אחת התלונות הגדולות ביותר של מפתחים ב-.NET לגבי עוזרי קידוד מבוססי AI היא שהם לא מעודכנים עם הגרסאות האחרונות של .NET ו-C#. שרת Microsoft Learn Docs MCP פותר זאת על ידי מתן גישה בזמן אמת לתיעוד הכי עדכני, הפניות API, ופרקטיקות מומלצות. בין אם אתה עובד עם ה-SDKים החדשים ביותר של Azure, בודק תכונות חדשות ב-C# 13, או מיישם תבניות Aspire מתקדמות, שרת זה מבטיח שלעוזר ה-AI שלך יש גישה למידע מוסמך ועדכני כדי לייצר קוד מדויק ומודרני.

**שימוש מעשי**: "מהן פקודות az cli ליצירת אפליקציית מכולה ב-Azure לפי התיעוד הרשמי של Microsoft Learn?" או "איך להגדיר Entity Framework עם הזרקת תלות ב-ASP.NET Core?" או אולי "עיין בקוד זה כדי לוודא שהוא תואם להמלצות הביצועים בתיעוד Microsoft Learn." השרת מספק תמיכה מקיפה בכל Microsoft Learn, תיעוד Azure, ותיעוד Microsoft 365 באמצעות חיפוש סמנטי מתקדם למציאת המידע הרלוונטי ביותר להקשר. הוא מחזיר עד 10 חתיכות תוכן איכותיות עם כותרות מאמרים וקישורים, תמיד ניגש לתיעוד העדכני ביותר של מיקרוסופט כפי שמתפרסם.

**דוגמה בולטת**: השרת חושף את הכלי `microsoft_docs_search` שמבצע חיפוש סמנטי נגד התיעוד הטכני הרשמי של מיקרוסופט. לאחר ההגדרה, אפשר לשאול שאלות כמו "איך מיישמים אימות JWT ב-ASP.NET Core?" ולקבל תגובות מפורטות, רשמיות עם קישורי מקור. איכות החיפוש מצוינת כי הוא מבין את ההקשר – שאלות על "containers" בהקשר של Azure יחזירו תיעוד של Azure Container Instances, בעוד אותו מונח בהקשר של .NET יחזיר מידע רלוונטי על איסוף ב-C#.

זה שימושי במיוחד עבור ספריות ומקרי שימוש שמשתנים במהירות או התעדכנו לאחרונה. לדוגמה, בפרויקטים קוד לאחרונה רציתי לנצל תכונות בגרסאות החדשות של Aspire ו-Microsoft.Extensions.AI. על ידי הכללת שרת Microsoft Learn Docs MCP, הצלחתי לנצל לא רק תיעוד API, אלא גם מדריכים והסברים שפורסמו זה עתה.

> **💡 טיפ מקצועי**
>
> אפילו דגמים ידידותיים לכלים זקוקים לעידוד להשתמש בכלי MCP! שקול להוסיף פרומפט מערכת או [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) כמו: "יש לך גישה ל-`microsoft.docs.mcp` – השתמש בכלי זה לחיפוש בתיעוד הרשמי העדכני ביותר של מיקרוסופט כשאתה מטפל בשאלות על טכנולוגיות מיקרוסופט כמו C#, Azure, ASP.NET Core או Entity Framework."
>
> לדוגמה מצוין לכך בפועל, עיין ב-[מצב הצ'אט של מנקה קוד C# .NET](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) ממאגר Awesome GitHub Copilot. מצב זה מנצל במיוחד את שרת Microsoft Learn Docs MCP כדי לסייע בניקוי וחדשנות קוד C# תוך שימוש בתבניות ופרקטיקות מומלצות עדכניות.
### 2. ☁️ שרת Azure MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**מה הוא עושה**: שרת Azure MCP הוא חבילה מקיפה של יותר מ-15 מחברים לשירותי Azure מיוחדים שמביאים את כל אקוסיסטם Azure לזרימת העבודה של ה-AI שלך. זה לא רק שרת אחד – זוהי אוסף עוצמתי שכולל ניהול משאבים, חיבור למסדי נתונים (PostgreSQL, SQL Server), ניתוח יומני Azure Monitor עם KQL, אינטגרציה ל-Cosmos DB, והרבה יותר.

**למה זה שימושי**: מעבר לניהול משאבי Azure, שרת זה משפר באופן דרמטי את איכות הקוד כשהוא עובד עם SDK של Azure. כאשר משתמשים ב-Azure MCP במצב סוכן, הוא לא רק עוזר לכתוב קוד – הוא עוזר לכתוב קוד Azure *טוב יותר* שעוקב אחרי דפוסי אימות עדכניים, שיטות טיפול בשגיאות מומלצות וניצול תכונות ה-SDK האחרונות. במקום לקבל קוד גנרי שעשוי לעבוד, תקבל קוד העוקב אחרי דפוסי ההמלצה של Azure לעומסי ייצור.

**מודולים מרכזיים כוללים**:
- **🗄️ מחברי מסד נתונים**: גישה ישירה בשפה טבעית ל-Azure Database עבור PostgreSQL ו-SQL Server
- **📊 Azure Monitor**: ניתוח יומני מבוסס KQL ותובנות תפעוליות
- **🌐 ניהול משאבים**: ניהול מלא של מחזור חיים של משאבי Azure
- **🔐 אימות**: דפוסי DefaultAzureCredential וזהות מנוהלת
- **📦 שירותי אחסון**: פעולות ב-Blob Storage, Queue Storage ו-Table Storage
- **🚀 שירותי מכולות**: אפליקציות מכולות Azure, מופעי מכולות וניהול AKS
- **ועוד מחברים מיוחדים רבים**

**שימוש מעשי**: "רשום את חשבונות האחסון שלי ב-Azure", "שאול את סביבת Log Analytics שלי עבור שגיאות בשעה האחרונה", או "עזור לי לבנות אפליקציית Azure עם Node.js עם אימות נכון"

**סצנה דמו מלאה**: הנה הליכה מלאה שמראה את הכוח בשילוב Azure MCP עם הרחבת GitHub Copilot עבור Azure ב-VS Code. כאשר יש לך את שניהם מותקנים ומזין בקשה:

> "צור סקריפט פייתון שמעלה קובץ ל-Azure Blob Storage באמצעות אימות DefaultAzureCredential. הסקריפט צריך להתחבר לחשבון האחסון שלי בשם 'mycompanystorage', להעלות למיכל בשם 'documents', ליצור קובץ בדיקה עם החותמת הזמנים הנוכחית להעלאה, לטפל בשגיאות בצורה אלגנטית ולספק פלט מידע, לעקוב אחר שיטות עבודה מומלצות של Azure לאימות ולטיפול בשגיאות, לכלול הערות המסבירות כיצד עובד אימות DefaultAzureCredential, ולעשות שהסקריפט יהיה מובנה היטב עם פונקציות ותיעוד נאותים."

שרת Azure MCP יפיק סקריפט פייתון מלא ומוכן לייצור ש:
- משתמש ב-SDK האחרון של Azure Blob Storage עם דפוסי async נכונים
- מיישם את DefaultAzureCredential עם הסבר מקיף על שרשרת הנפילה בחזרה
- כולל טיפול שגיאות איתן עם סוגי חריגות ספציפיים של Azure
- עוקב אחר השיטות הטובות ביותר של Azure SDK לניהול משאבים וטיפול בחיבור
- מספק רישום מפורט ופלט מידע לקונסול
- יוצר סקריפט מובנה היטב עם פונקציות, תיעוד ורמזי טיפוס

מה שהופך זאת למרשים הוא שבלעדי Azure MCP, יתכן ותקבל קוד אחסון blob גנרי שעובד אבל לא עוקב אחר דפוסי Azure העכשוויים. עם Azure MCP, אתה מקבל קוד שמנצל את שיטות האימות החדישות ביותר, מטפל בתרחישי שגיאות ספציפיים ל-Azure, ועוקב אחר השיטות המומלצות של Microsoft ליישומים בפרודקשן.

**דוגמה מוקדמת**: התקשיתי לזכור את הפקודות הספציפיות של הכלים `az` ו-`azd` לשימוש חד-פעמי. תמיד זה תהליך דו-שלבי בשבילי: קודם מחפש את התחביר, ואז מריץ את הפקודה. לעתים פשוט נכנס לפורטל ומקליק כדי לסיים את העבודה כי אני לא רוצה להודות שאני לא זוכר את תחביר ה-CLI. היכולת פשוט לתאר מה אני רוצה מדהימה, ויותר טוב לעשות זאת בלי לעזוב את ה-IDE שלי!

יש רשימה מצוינת של מקרי שימוש ב-[מאגר Azure MCP](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) להתחלה. למדריכים מקיפים לאתחול ואפשרויות תצורה מתקדמות, בדוק את [התיעוד הרשמי של Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 שרת GitHub MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**מה הוא עושה**: שרת GitHub MCP הרשמי מספק אינטגרציה חלקה עם כל האקוסיסטם של GitHub, כולל גישה מרוחקת מתארחת ואפשרויות פריסה מקומית באמצעות Docker. זה לא רק פעולות בסיסיות על המאגר – זו ערכת כלים מקיפה שכוללת ניהול GitHub Actions, זרימות עבודה של בקשות משיכה, מעקב אחר סוגיות, סריקת אבטחה, התראות ויכולות אוטומציה מתקדמות.

**למה זה שימושי**: השרת משנה את האופן שבו אתה מתקשר עם GitHub על ידי הבאת חוויית הפלטפורמה המלאה לסביבת הפיתוח שלך. במקום לעבור כל הזמן בין VS Code ל-GitHub.com כדי לנהל פרויקטים, לסקור קוד ולעקוב אחרי CI/CD, אתה יכול לבצע הכל באמצעות פקודות בשפה טבעית תוך שמירה על ריכוז בקוד שלך.

> **ℹ️ הערה: סוגים שונים של 'סוכנים'**
> 
> אל תבלבל את שרת GitHub MCP עם סוכן הקידוד של GitHub (הסוכן המבוסס בינה מלאכותית שניתן להקצות לו סוגיות למשימות קידוד אוטומטיות). שרת GitHub MCP פועל במצב סוכן של VS Code כדי לספק אינטגרציית API של GitHub, בעוד ש-Agent הקידוד של GitHub הוא תכונה נפרדת שיוצרת pull request כאשר הוא מוקצה לסוגיות ב-GitHub.

**יכולות מרכזיות כוללות**:
- **⚙️ GitHub Actions**: ניהול מלא של צינור CI/CD, מעקב זרימות עבודה וטיפול בארטיפקטים
- **🔀 Pull Requests**: יצירה, סקירה, מיזוג וניהול PRs עם מעקב מצב מקיף
- **🐛 סוגיות**: ניהול מחזור חיים מלא של סוגיות, הערות, סימונים והקצאות
- **🔒 אבטחה**: התראות סריקת קוד, גילוי סודות ואינטגרציית Dependabot
- **🔔 התראות**: ניהול התראות חכם ושליטה במנוי המאגר
- **📁 ניהול מאגר**: פעולות קבצים, ניהול סניפים ומינהל המאגר
- **👥 שיתוף פעולה**: חיפוש משתמשים וארגונים, ניהול צוותים ושליטת גישה

**שימוש בעולם האמיתי**: "צור pull request מהסניף הפונקציונלי שלי", "הראה לי את כל ריצות ה-CI הכושלות השבוע", "רשום את כל התראות האבטחה הפתוחות עבור המאגר שלי", או "מצא את כל הבעיות המוקצות לי בארגונים שלי"

**תסריט הדגמה מלא**: הנה זרימת עבודה עוצמתית המדגימה את יכולות שרת GitHub MCP:

> "אני צריך להתכונן לסקירת הספרינט שלנו. הראה לי את כל ה-pull requests שיצרתי השבוע, בדוק את מצב צינורות ה-CI/CD שלנו, צור סיכום של כל התראות האבטחה שצריך לטפל בהן, ועזור לי לערוך ניסוח של רשומות השחרור בהתבסס על PRs מיטוגים עם התג 'feature'."

שרת GitHub MCP:
- ישאיל שאילתות עבור ה-pull requests האחרונים שלך עם מידע מצב מפורט
- ינתח ריצות זרימת עבודה ויאיר כל כשל או בעיית ביצועים
- יקבץ תוצאות סריקת אבטחה ויתעדף התראות קריטיות
- יפיק רשומות שחרור מקיפות על ידי חילוץ מידע מ-PRs מיטוגים
- יספק שלבים הבאים לפעולה לתכנון ספרינט והכנת שחרור

**דוגמה מוקדמת**: אני אוהב להשתמש בזה לזרימות עבודה של סקירת קוד. במקום לקפוץ בין VS Code, התראות GitHub ודפי pull requests, אני יכול לומר "הראה לי את כל ה-PRs שמחכים לסקירה שלי" ואז "תוסיף תגובה ל-PR #123 לגבי טיפול בשגיאות בשיטת האימות." השרת מטפל בקריאות API של GitHub, שומר על הקשר בשיחה ואפילו עוזר לי ליצור תגובות סקירה בונות יותר.

**אפשרויות אימות**: השרת תומך גם ב-OAuth (חלק ב-VS Code) וגם ב- Personal Access Tokens, עם ערכות כלים ניתנות להגדרה שיאפשרו רק את הפונקציונליות של GitHub שאתה צריך. ניתן להריץ אותו כשירות מתארח מרחוק להתקנה מיידית או מקומית דרך Docker לקבלת שליטה מלאה.

> **💡 טיפ מקצועי**
> 
> אפשר רק את ערכות הכלים שאתה צריך על ידי קונפיגורציה של הפרמטר `--toolsets` בהגדרות שרת ה-MCP שלך כדי להפחית גודל הקונטקסט ולשפר את בחירת כלי ה-AI. לדוגמה, הוסף `"--toolsets", "repos,issues,pull_requests,actions"` לארגומנטים בקונפיגורציית ה-MCP שלך עבור זרימות עבודה לפיתוח ליבה, או השתמש ב-`"--toolsets", "notifications, security"` אם אתה מתמקד בעיקר ביכולות ניטור GitHub.
### 4. 🔄 שרת Azure DevOps MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**מה הוא עושה**: מתחבר לשירותי Azure DevOps לניהול פרויקטים מקיף, מעקב אחרי פריטי עבודה, ניהול צינורות בנייה ופעלים על מאגרים.

**למה זה שימושי**: עבור צוותים שמשתמשים ב-Azure DevOps כפלטפורמת DevOps הראשית שלהם, שרת ה-MCP הזה מבטל את הצורך להחליף טאבים בין סביבת הפיתוח לממשק האינטרנט של Azure DevOps. ניתן לנהל פריטי עבודה, לבדוק סטטוסי בנייה, לבצע שאילתות על מאגרים ולטפל במשימות ניהול פרויקטים ישירות מהעוזר הממוחשב שלך.

**שימוש בעולם האמיתי**: "הראה לי את כל פריטי העבודה הפעילים בספרינט הנוכחי עבור פרויקט WebApp", "צור דו"ח באג עבור בעיית ההתחברות שמצאתי זה עתה", או "בדוק את מצב צינורות הבנייה שלנו והראה לי כל כישלונות לאחרונה"

**דוגמה מוקדמת**: אפשר בקלות לבדוק את מצב הספרינט הנוכחי של הצוות עם שאלה פשוטה כמו "הראה לי את כל פריטי העבודה הפעילים בספרינט הנוכחי עבור פרויקט WebApp" או "צור דו"ח באג עבור בעיית ההתחברות שמצאתי זה עתה" מבלי לעזוב את סביבת הפיתוח.

### 5. 📝 שרת MarkItDown MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**מה הוא עושה**: MarkItDown הוא שרת המרה מקיף שממיר פורמטים שונים של קבצים ל-Markdown איכותי, מותאם לצריכת המודלים הגדולים (LLM) וזרימות עבודה לניתוח טקסט.

**למה זה שימושי**: חיוני עבור זרימות עבודה מודרניות של תיעוד! MarkItDown מטפל במגוון מרשים של פורמטי קבצים תוך שמירה על מבנה הקריטי של המסמך כמו כותרות, רשימות, טבלאות וקישורים. בניגוד לכלי חילוץ טקסט פשוטים, הוא מתמקד בשמירת המשמעות הסמנטית והעיצוב שבעלי ערך הן לעיבוד בינה מלאכותית והן לקריאות אנושית.

**פורמטים נתמכים**:
- **מסמכי משרד**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **קבצי מדיה**: תמונות (עם מטה-דאטה EXIF ו-OCR), אודיו (עם מטה-דאטה EXIF ותמלול דיבור)
- **תוכן אינטרנטי**: HTML, פידים של RSS, URLs של YouTube, דפי ויקיפדיה
- **פורמטי נתונים**: CSV, JSON, XML, קבצי ZIP (מעבד תוכן באופן רקורסיבי)
- **פורמטי פרסום**: EPub, מחברות Jupyter (.ipynb)
- **מיילים**: הודעות Outlook (.msg)
- **מתקדם**: אינטגרציה עם Azure Document Intelligence לעיבוד PDF משופר

**יכולות מתקדמות**: MarkItDown תומך בתיאורי תמונות מונעי LLM (כאשר מסופק לקוח OpenAI), אינטגרציה עם Azure Document Intelligence לעיבוד PDF משופר, תמלול אודיו לתוכן דיבור, ומערכת פלאגינים להרחבה לפורמטי קבצים נוספים.

**שימוש בעולם האמיתי**: "המר את המצגת PowerPoint הזו ל-Markdown עבור אתר התיעוד שלנו", "חלץ טקסט מתוך PDF זה עם מבנה כותרות נכון", או "המר את גיליון האקסל הזה לטבלת Markdown קריאה"

**דוגמה מוקדמת (מעוברת)**: 
[תיעוד MarkItDown](https://github.com/microsoft/markitdown#why-markdown) מסביר
ש-Markdown שומר על מבנה המסמך עם עומס מינימלי של עיצוב.
מודלים לשוניים בדרך כלל מייצרים Markdown, מה שהופך אותו לפורמט יעיל החלפת תגים
לזרימות עבודה לעיבוד מסמכים.

MarkItDown מצוין בשמירת מבנה המסמך, מה שחשוב לזרימות עבודה של בינה מלאכותית. לדוגמה, בהמרת מצגת PowerPoint, הוא שומר על ארגון השקופיות עם הכותרות הנכונות, מחלץ טבלאות כטבלאות Markdown, כולל טקסט חלופי לתמונות, ואפילו מעבד את הערות הדובר. תרשימים מומרות לטבלאות נתונים קריאות, ו-Markdown הנוצר שומר על זרימה לוגית של המצגת המקורית. זה מושלם להזנת תוכן מצגות למערכות AI או ליצירת תיעוד משקופיות קיימות.
### 6. 🗃️ שרת SQL Server MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**מה הוא עושה**: מספק גישה שיחית למסדי נתונים של SQL Server (במקום, Azure SQL, או Fabric)

**למה זה שימושי**: דומה לשרת PostgreSQL אבל עבור האקו-סיסטם של Microsoft SQL. התחבר עם מחרוזת חיבור פשוטה והתחל לשאול בשפה טבעית – אין עוד החלפת הקשרים!

**שימוש בעולם האמיתי**: "מצא את כל ההזמנות שלא בוצעו ב-30 הימים האחרונים" מתורגם לשאילתות SQL מתאימות ומחזיר תוצאות מעוצבות

**דוגמה מוקדמת**: לאחר שהגדרת את חיבור מסד הנתונים שלך, תוכל להתחיל לשוחח עם הנתונים מיד. הפוסט בבלוג מציג זאת עם שאלה פשוטה: "לאיזה מסד נתונים אתה מחובר?" שרת ה-MCP מגיב על ידי הפעלת כלי מסד נתונים מתאים, מתחבר למופע SQL Server שלך, ומחזיר פרטים על החיבור הנוכחי – הכל בלי לכתוב שורת SQL אחת. השרת תומך בפעולות מקיפות על מסדי נתונים, מניהול סכמות עד למניפולציה של נתונים, כולם דרך פקודות בשפה טבעית. לקבלת הוראות הגדרה ודוגמאות קונפיגורציה עם VS Code ו-Claude Desktop, ראה: [הכר את שרת MSSQL MCP (בטא)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 שרת Playwright MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**מה הוא עושה**: מאפשר לסוכני AI לאינטראקציה עם דפי אינטרנט לצורך בדיקות ואוטומציה

> **ℹ️ מפעיל את GitHub Copilot**
> 
> שרת Playwright MCP מספק את סוכן הקידוד של GitHub Copilot, ומעניק לו יכולות גלישה באינטרנט! [למידע נוסף על תכונה זו](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**למה זה שימושי**: מושלם לבדיקות אוטומטיות שמונעות מתיאורים בשפה טבעית. AI יכול לנווט באתרים, למלא טפסים ולחלץ נתונים דרך טביעות נגישות מובנות – זה מאוד עוצמתי!

**שימוש בעולם האמיתי**: "בדוק את תהליך ההתחברות ואמת שהלוח מחוונים נטען כראוי" או "צור מבחן שמחפש מוצרים ומאמת את דף התוצאות" – וכל זאת בלי הצורך בקוד המקור של האפליקציה

**דוגמה מוקדמת**: עמיתתי Debbie O'Brien עושה עבודה מדהימה עם שרת Playwright MCP לאחרונה! למשל, היא הראתה איך ניתן לייצר מבחני Playwright מלאים בלי אפילו לקבל גישה לקוד המקור של האפליקציה. בתרחיש שלה, היא ביקשה מקופילוט ליצור מבחן לאפליקציית חיפוש סרטים: לנווט לאתר, לחפש "Garfield", ולאמת שהסרט מופיע בתוצאות. השרת פתח סשן דפדפן, חקר את מבנה הדף עם טביעות DOM, מצא את הסלקטורים המתאימים ויצר מבחן TypeScript עובד במלואו שעבר בריצה הראשונה.

מה שהופך את זה לעוצמתי באמת הוא שזה מחבר את הפער בין הוראות בשפה טבעית לבין קוד בדיקה ניתן לביצוע. גישות מסורתיות דורשות או כתיבת בדיקות ידנית או גישה לקוד לצורך הקשר. אבל עם Playwright MCP, אפשר לבדוק אתרים חיצוניים, יישומים עבור לקוח, או לעבוד בתרחישי בדיקת קופסה שחורה שבהם אין גישה לקוד.


### 8. 💻 שרת Dev Box MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**מה הוא עושה**: מנהל סביבות Microsoft Dev Box דרך שפה טבעית

**מדוע זה שימושי**: מפשט מאוד את ניהול סביבות הפיתוח! צור, הגדר ונהל סביבות פיתוח מבלי לזכור פקודות ספציפיות.

**שימוש בעולם האמיתי**: "הגדר Dev Box חדש עם ה-SDK האחרון של .NET וקונפג אותו לפרויקט שלנו", "בדוק את הסטטוס של כל סביבות הפיתוח שלי", או "צור סביבת הדגמה סטנדרטית עבור מצגות הצוות שלנו"

**דוגמה מובלטת**: אני מעריץ גדול של השימוש ב-Dev Box לפיתוח אישי. רגע האור שלי כאן היה כשהג'יימס מונטמאגנו הסביר כמה Dev Box מצוין להדגמות בכנסים, כי יש לו חיבור אתרנט מהיר במיוחד בלי תלות בווייפיי הכנס/מלון/מטוס שאני עשוי להשתמש בו באותו הרגע. למעשה, לאחרונה עשיתי תרגול להדגמת כנס כשהמחשב הנייד שלי מחובר לנקודת החמה בפלאפון בזמן נסיעה באוטובוס מברוז׳ לאנטוורפן! אבל הצעד הבא שלי כאן הוא לחקור יותר את הניהול הצוותי של מספר סביבות פיתוח וסביבות הדגמה סטנדרטיות. ומקרה שימוש גדול נוסף ששמעתי מלקוחות ועמיתים הוא כמובן שימוש ב-Dev Box לסביבות פיתוח מוגדרות מראש. בשני המקרים, שימוש ב-MCP להגדרה ולניהול Dev Boxes מאפשר אינטראקציה בשפה טבעית, כל זאת תוך כדי שמירה בסביבת הפיתוח שלך.

### 9. 🤖 שרת Microsoft Foundry MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**מה הוא עושה**: שרת Microsoft Foundry MCP מספק למפתחים גישה מקיפה לאקו-סיסטם של AI של Azure, כולל קטלוגי מודלים, ניהול פריסה, אינדקס ידע עם Azure AI Search וכלי הערכה. שרת ניסיוני זה מחבר את הפער בין פיתוח AI לתשתית AI העוצמתית של Azure, ומאפשר בנייה, פריסה והערכת יישומי AI בקלות.

**מדוע זה שימושי**: שרת זה משנה את האופן בו עובדים עם שירותי Azure AI על ידי הבאת יכולות AI ברמת ארגון ישירות לזרימת העבודה שלך. במקום לעבור בין פורטל Azure, תיעוד וסביבת הפיתוח שלך, ניתן לגלות מודלים, לפרוס שירותים, לנהל בסיסי ידע ולהעריך ביצועי AI דרך פקודות בשפה טבעית. זה עוצמתי במיוחד למפתחים הבונים יישומי RAG (Retrieval-Augmented Generation), מנהלים פריסות מרובות מודלים, או מיישמים צנרת הערכה מקיפה ל-AI.

**יכולות מפתח למפתחים**:
- **🔍 גילוי מודלים & פריסה**: חקור את קטלוג המודלים של Microsoft Foundry, קבל מידע מפורט עם דוגמאות קוד, ופרוס מודלים לשירותי Azure AI
- **📚 ניהול ידע**: צור ונהל אינדקסים ב-Azure AI Search, הוסף מסמכים, קונפג אינדקסרים, ובנה מערכות RAG מתקדמות
- **⚡ אינטגרציה עם סוכני AI**: התחבר עם סוכני Azure AI, שאול סוכנים קיימים, והערך ביצועי סוכן בתרחישי הפקה
- **📊 מסגרת הערכה**: הרץ הערכות טקסט וסוכנים מקיפות, הפק דוחות Markdown, ויישם בקרת איכות עבור יישומי AI
- **🚀 כלים לפרוטוטייפינג**: קבל הנחיות הגדרה לפרוטוטייפינג מבוסס GitHub וגש ל-Microsoft Foundry Labs למחקר מודלים מתקדמים

**שימוש אמיתי של מפתח**: "פרוס מודל Phi-4 לשירותי Azure AI עבור היישום שלי", "צור אינדקס חיפוש חדש למערכת RAG של התיעוד שלי", "הערך את תגובות הסוכן שלי מול מדדי איכות", או "מצא את מודל ההיגיון הטוב ביותר למשימות האנליזה המורכבות שלי"

**תרחיש הדגמה מלא**: הנה זרימת פיתוח AI עוצמתית:

> "אני בונה סוכן תמיכה ללקוח. עזור לי למצוא מודל היגיון טוב מהקטלוג, לפרוס אותו לשירותי Azure AI, ליצור בסיס ידע מתיעוד שלנו, להקים מסגרת הערכה לבדיקת איכות התגובה, ואז לעזור לי לפרוטוטייפ את האינטגרציה עם טוקן GitHub לבדיקות."

שרת Microsoft Foundry MCP י:
- ישאל את קטלוג המודלים כדי להמליץ על מודלי היגיון אופטימליים בהתאם לדרישותיך
- יספק פקודות פריסה ומידע על מכסות לאזור Azure המועדף עליך
- יגדיר אינדקסים ב-Azure AI Search עם סכימה מתאימה לתיעוד שלך
- יקונפג צנרת הערכה עם מדדי איכות ובדיקות בטיחות
- יפיק קוד פרוטוטייפינג עם אימות GitHub לבדיקות מיידיות
- יספק מדריכי הגדרה מקיפים המותאמים לערכת הטכנולוגיה שלך

**דוגמה מובלטת**: כמתכנת, נאבקתי לעמוד בקצב דגמי ה-LLM השונים הזמינים. אני מכיר כמה עיקריים, אבל מרגיש שאני מפספס שיפורים בפרודוקטיביות ויעילות. והטוקנים והמכסות הם מלחיצים וקשים לניהול – אני אף פעם לא יודע אם אני בוחר נכון את המודל למשימה או מבזבז תקציב בלא יעילות. שמעתי רק לאחרונה על שרת MCP זה מג'יימס מונטמאגנו כשבדקתי המלצות מפתחים אחרים לשרת MCP לפוסט הזה, ואני נרגש להשתמש בו! יכולות הגילוי של המודל נראות מרשימות במיוחד למי כמוני שרוצה לחקור מעבר למודלים הרגילים ולמצוא מודלים מותאמים למשימות ספציפיות. מסגרת ההערכה תעזור לי לוודא שאני באמת משיג תוצאות טובות יותר, ולא סתם מנסה משהו חדש לשם שינוי.

> **ℹ️ סטטוס ניסיוני**
> 
> שרת MCP זה הוא ניסיוני ומתפתח באופן פעיל. תכונות ו-API עשויים להשתנות. מושלם לחקירת יכולות Azure AI ולבניית פרוטוטיפים, אך יש לאמת דרישות יציבות לשימוש בפרודקשן.
### 10. 🏢 שרת Microsoft 365 Agents Toolkit MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**מה הוא עושה**: מספק למפתחים כלי מפתח לבניית סוכני AI ויישומים שמשתלבים עם Microsoft 365 ו-Microsoft 365 Copilot, כולל אימות סכימה, קבלת דוגמאות קוד, וסיוע בתיקון תקלות.

**מדוע זה שימושי**: פיתוח ל-Microsoft 365 ו-Copilot כולל סכימות מאניווס מורכבות ודפוסי פיתוח ספציפיים. שרת MCP זה מביא מקורות פיתוח חיוניים ישירות לסביבת הקידוד שלך, ועוזר לאמת סכימות, למצוא דוגמאות קוד ולטפל בבעיות נפוצות מבלי להישען ללא הפסק על תיעוד.

**שימוש בעולם האמיתי**: "אמת את מאניווס הסוכן הדקלרטיבי ותיקן שגיאות סכימה", "הראה לי דוגמאות קוד ליישום תוסף Microsoft Graph API", או "עזור לי לתקן בעיות אימות באפליקציית Teams שלי"

**דוגמה מובלטת**: פניתי לחבר שלי ג'ון מילר אחרי שדיברנו בבילד על סוכני M365, והוא המליץ על MCP הזה. זה יכול להיות מעולה למפתחים חדשים ל-M365 Agents כי הוא מספק תבניות, דוגמאות קוד, ומבנים להתחלה ללא הצפה בתיעוד. תכונות אימות הסכימה נראות שימושיות במיוחד למניעת שגיאות במבנה המאניווס שיכולות לגרום לשעות של דיבוג.

> **💡 טיפ מומחה**
> 
> השתמש בשרת זה לצד שרת Microsoft Learn Docs MCP לתמיכה מקיפה בפיתוח M365 – אחד מספק את התיעוד הרשמי והאחר כלי פיתוח מעשיים וסיוע בתיקון תקלות.


## מה הלאה? 🔮

## 📋 סיכום

פרוטוקול הקשר למודל (MCP) משנה את האופן בו מפתחים מתקשרים עם עוזרי AI וכלים חיצוניים. עשרת שרתי ה-MCP של Microsoft הללו מדגימים את עוצמת האינטגרציה הסטנדרטית של AI, ומאפשרים זרימות עבודה חלקות ששומרות על מפתחים במצב זרימה תוך גישה לכישורים חיצוניים עוצמתיים.

מהאינטגרציה המקיפה של אקו-סיסטם Azure ועד כלים מיוחדים כמו Playwright לאוטומציה בדפדפן ו-MarkItDown לעיבוד מסמכים, שרתים אלו ממחישים כיצד MCP יכול לשפר פרודוקטיביות במגוון תרחישי פיתוח. הפרוטוקול הסטנדרטי מוודא שכלים אלו עובדים יחד בצורה חלקה, ויוצרים חוויית פיתוח מלוכדת.

ככל שאקו-סיסטם ה-MCP ממשיך להתפתח, שמירה על מעורבות בקהילה, חקר שרתים חדשים ובניית פתרונות מותאמים יהיה המפתח למיצוי הפרודוקטיביות בפיתוח שלך. טיב הפרוטוקול הפתוח של MCP מאפשר לך לשלב כלי ספקים שונים ליצירת זרימת עבודה מושלמת לצרכים הספציפיים שלך.

## 🔗 משאבים נוספים

- [מאגר MCP הרשמי של מיקרוסופט](https://github.com/microsoft/mcp)
- [קהילת MCP ותיעוד](https://modelcontextprotocol.io/introduction)
- [תיעוד MCP ל-VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [תיעוד MCP ל-Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [תיעוד MCP ל-Azure](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [בואו ללמוד – אירועי MCP](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [התאמות GitHub Copilot מדהימות](https://github.com/awesome-copilot)
- [ערכת פיתוח MCP ל-C#](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [ימי פיתוח MCP בשידור חי 29/30 ביולי או צפייה לפי דרישה](https://aka.ms/mcpdevdays)

## 🎯 תרגילים

1. **התקן והגדר**: התקן אחד משרתי MCP בסביבת VS Code שלך ובדוק פונקציונליות בסיסית.
2. **אינטגרציית זרימת עבודה**: עצב זרימת פיתוח שמשלבת לפחות שלושה שרתי MCP שונים.
3. **תכנון שרת מותאם אישית**: זהה משימה בשגרת הפיתוח היומית שלך שיכולה להרוויח משרת MCP מותאם וכתוב מפרט שלה.
4. **ניתוח ביצועים**: השווה את היעילות של שימוש בשרתי MCP מול גישות מסורתיות למשימות פיתוח נפוצות.
5. **הערכת אבטחה**: הערך את ההשלכות האבטחתיות של שימוש בשרתי MCP בסביבת הפיתוח שלך והצע שיטות עבודה מומלצות.


הבא: [שיטות עבודה מומלצות](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->