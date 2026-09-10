# 🚀 10 שרתי Microsoft MCP שמשנים את הפרודוקטיביות של המפתחים

## 🎯 מה תלמד במדריך זה

מדריך מעשי זה מציג עשרה שרתי Microsoft MCP שמשנים באופן פעיל את האופן שבו מפתחים עובדים עם עוזרים מבוססי AI. במקום רק להסביר מה שרתי MCP *יכולים* לעשות, נראה לך שרתים שכבר עושים שינוי אמיתי בשגרות הפיתוח היומיות במיקרוסופט ומעבר לה.

כל שרת במדריך זה נבחר בהתבסס על שימוש בעולם האמיתי ומשוב מהמפתחים. תגלה לא רק מה כל שרת עושה, אלא גם למה זה חשוב ואיך להפיק ממנו את המרב בפרויקטים שלך. בין אם אתה חדש לחלוטין ל-MCP או מחפש להרחיב את ההתקנה הקיימת שלך, שרתים אלה מייצגים חלק מהכלים הפרקטיים והמשפיעים ביותר הזמינים באקוסיסטם של מיקרוסופט.

> **💡 טיפ התחלה מהירה**
> 
> חדש ל-MCP? אל דאגה! מדריך זה מותאם למתחילים. נסביר מושגים בזמן ההתקדמות, ותמיד תוכל להיעזר במודולים שלנו [הקדמה ל-MCP](../00-Introduction/README.md) ו[מושגי יסוד](../01-CoreConcepts/README.md) לרקע מעמיק יותר.

## סקירה כללית

מדריך מקיף זה חוקר עשרה שרתי Microsoft MCP שמשנים את האופן שבו מפתחים מתקשרים עם עוזרי AI וכלים חיצוניים. מניהול משאבי Azure ועד עיבוד מסמכים, שרתים אלה מדגימים את עוצמת פרוטוקול הקשר לדגם (Model Context Protocol) ביצירת תהליכי פיתוח חלקים ופרודוקטיביים.

## יעדי למידה

עד סוף המדריך תלמד:
- להבין כיצד שרתי MCP משפרים את פרודוקטיביות המפתחים
- ללמוד על יישומי שרותי MCP המשפיעים ביותר של מיקרוסופט
- לגלות מקרים שימוש פרקטיים לכל שרת
- לדעת כיצד להגדיר ולהריץ שרתים אלה ב-VS Code ו-Visual Studio
- לחקור את האקוסיסטם הרחב של MCP וכיווני פיתוח עתידיים

## 🔧 הבנת שרתי MCP: מדריך למתחילים

### מה הם שרתי MCP?

בתור מתחיל בפרוטוקול הקשר לדגם (MCP), ייתכן שתתעניין: "מה בעצם שרת MCP, ולמה זה חשוב?" נתחיל באנלוגיה פשוטה.

תחשוב על שרתי MCP כעוזרים מיוחדים שמסייעים לעוזר הקוד שלך מבוסס AI (כמו GitHub Copilot) להתחבר לכלים ושירותים חיצוניים. בדיוק כמו שאתה משתמש באפליקציות שונות בטלפון שלך למשימות שונות—אחת למזג האוויר, אחת לניווט, אחת לבנקאות—שרתים אלה מעניקים לעוזר ה-AI שלך את היכולת לקשר לכלי פיתוח ושירותים שונים.

### הבעיה ששרתים MCP פותרים

לפני שרתי MCP, אם רצית:
- לבדוק את משאבי Azure שלך
- ליצור נושא ב-GitHub
- לשאול את בסיס הנתונים שלך
- לחפש במסמכים

היית צריך להפסיק לקודד, לפתוח דפדפן, לנווט לאתר המתאים, ולבצע את המשימות ידנית. המעבר המתמיד בין הקשרים שובר את הזרימה שלך ומפחית את הפרודוקטיביות.

### איך שרתי MCP משנים את חוויית הפיתוח שלך

עם שרתי MCP, תוכל להישאר בסביבת הפיתוח שלך (VS Code, Visual Studio וכו') ולפשט לבקש מהעוזר AI שלך לטפל במשימות אלה. למשל:

**במקום תהליך עבודה מסורתי זה:**
1. להפסיק לקודד
2. לפתוח דפדפן
3. לנווט לפורטל Azure
4. לבדוק פרטי חשבון אחסון
5. לחזור ל-VS Code
6. להמשיך בקידוד

**כעת ניתן לעשות כך:**
1. לשאול את ה-AI: "מה מצב חשבונות האחסון שלי ב-Azure?"
2. להמשיך לקודד עם המידע שסופק

### יתרונות מרכזיים למתחילים

#### 1. 🔄 **שמור על מצב הזרימה שלך**
- לא צריך להחליף בין אפליקציות שונות
- שמור על ההתמקדות בקוד שאתה כותב
- הפחת את העומס המנטלי בניהול כלים שונים

#### 2. 🤖 **השתמש בשפה טבעית במקום פקודות מורכבות**
- במקום לזכור תחביר SQL, תאר מה הנתונים שאתה צריך
- במקום לזכור פקודות Azure CLI, הסבר מה אתה רוצה להשיג
- תן ל-AI לטפל בפרטים הטכניים בזמן שאתה מתמקד בלוגיקה

#### 3. 🔗 **חבר כלים מרובים יחד**
- צור תהליכים חזקים על ידי שילוב שירותים שונים
- דוגמה: "קבל את כל נושאי GitHub האחרונים וצור פריטי עבודה מתאימים ב-Azure DevOps"
- בניית אוטומציה ללא כתיבת סקריפטים מורכבים

#### 4. 🌐 **גש לאקוסיסטמה גדלה**
- נצל שרתים שבנו מיקרוסופט, GitHub וחברות נוספות
- ערבב והתאם בין כלים של ספקים שונים בקלות
- הצטרף לאקוסיסטמה סטנדרטית שפועלת בין עוזרי AI שונים

#### 5. 🛠️ **למד באמצעות עשייה**
- התחל עם שרתים מוכנים להבנה ראשונית של המושגים
- בנה בהדרגה שרתים משלך ככל שתתמקצע יותר
- השתמש ב-SDKים ובתיעוד הקיים להנחיית למידתך

### דוגמה מהחיים האמיתיים למתחילים

נניח שאתה חדש לפיתוח אתרים ועובד על הפרויקט הראשון שלך. כך שרתי MCP יכולים לעזור:

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

### יתרון התקן הארגוני

MCP הופך לתקן תעשייתי רחב, מה שאומר:
- **עקביות**: חווית שימוש דומה בין כלים וחברות שונות
- **אינטרופרביליות**: שרתים מספקים שונים משתפים פעולה
- **הגנה לעתיד**: מיומנויות והגדרות עוברים בין עוזרי AI שונים
- **קהילה**: אקוסיסטמה גדולה של ידע משותף ומשאבים

### התחלה: מה תלמד

במדריך זה, נסקור 10 שרתי Microsoft MCP שחשובים במיוחד למפתחים בכל הרמות. כל שרת מתוכנן:
- לפתור אתגרים נפוצים בפיתוח 
- להפחית משימות חוזרות
- לשפר את איכות הקוד
- להרחיב הזדמנויות למידה

> **💡 טיפ למידה**
> 
> אם אתה חדש לגמרי ל-MCP, התחל ממודולי ה[הקדמה ל-MCP](../00-Introduction/README.md) ו[מושגי יסוד](../01-CoreConcepts/README.md). ואז חזור לכאן לראות את המושגים בפעולה עם כלים אמיתיים של מיקרוסופט.
>
> לקונטקסט נוסף על חשיבות MCP, עיין בפוסט של מריה נאגגה: [התחבר פעם אחת, שלב בכל מקום עם MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## התחלה עם MCP ב-VS Code ו-Visual Studio 🚀

הקמת שרתי MCP אלה פשוטה אם אתה משתמש ב-Visual Studio Code או Visual Studio 2022 יחד עם GitHub Copilot.

### הגדרת VS Code

כך נראה התהליך הבסיסי ב-VS Code:

1. **הפעל מצב סוכן**: ב-VS Code, עבור למצב סוכן בחלון Copilot Chat
2. **הגדר שרתי MCP**: הוסף הגדרות שרתים לקובץ settings.json ב-VS Code שלך
3. **הפעל שרתים**: לחץ על הכפתור "התחל" עבור כל שרת שברצונך להשתמש בו
4. **בחר כלים**: בחר אילו שרתי MCP להפעיל במפגש הנוכחי

להוראות מפורטות, עיין ב[תיעוד MCP של VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 טיפ מקצועי: נהל שרתי MCP כמו מקצוען!**
> 
> תצוגת ההרחבות ב-VS Code כוללת עכשיו [ממשק נוח לניהול שרתי MCP מותקנים](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! יש לך גישה מהירה להתחלה, עצירה וניהול שרתי MCP מותקנים בממשק ברור ופשוט. נסה!

### הגדרת Visual Studio 2022

עבור Visual Studio 2022 (גרסה 17.14 ומעלה):

1. **הפעל מצב סוכן**: לחץ על התפריט הנפתח "שאל" בחלון GitHub Copilot Chat ובחר "סוכן"
2. **צור קובץ הגדרות**: צור קובץ `.mcp.json` בתיקיית הפתרון שלך (מיקום מומלץ: `<SOLUTIONDIR>\.mcp.json`)
3. **הגדר שרתים**: הוסף את הגדרות שרתי MCP שלך באמצעות פורמט MCP סטנדרטי
4. **אישור כלים**: כאשר תתבקש, אשר את הכלים שברצונך להשתמש בהם עם הרשאות טווח מתאימות

לעיון בהוראות מפורטות להקמת Visual Studio, עיין ב[תיעוד MCP של Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

לכל שרת MCP דרישות קונפיגורציה משלו (מחרוזות חיבור, אימות וכו'), אך דפוס ההגדרה אחיד בשני ה-IDEים.

## לקח שלמדנו משרתי Microsoft MCP 🛠️

### 1. 📚 שרת Microsoft Learn Docs MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**מה הוא עושה**: שרת Microsoft Learn Docs MCP הוא שירות מאוכלס בענן המספק לעוזרי AI גישה בזמן אמת לתיעוד הרשמי של מיקרוסופט דרך פרוטוקול הקשר לדגם. הוא מתחבר ל`https://learn.microsoft.com/api/mcp` ומאפשר חיפוש סמנטי ברחבי Microsoft Learn, תיעוד Azure, תיעוד Microsoft 365, ומקורות רשמיים נוספים של מיקרוסופט.

**למה זה מועיל**: למרות שזה נראה כמו "רק תיעוד," שרת זה חיוני לכל מפתח המשתמש בטכנולוגיות מיקרוסופט. אחת התלונות הגדולות של מפתחי .NET על עוזרי קוד מבוססי AI היא שהם לא מעודכנים בגרסאות האחרונות של .NET ו-C#. שרת Microsoft Learn Docs MCP פותר זאת על ידי אספקת גישה בזמן אמת לתיעוד העדכני ביותר, הפניות API, והנחיות הטובות ביותר. בין אם אתה עובד עם ה-SDKs העדכניים ביותר של Azure, מגלם תכונות חדשות של C# 13, או מיישם תבניות Aspire מתקדמות, שרת זה מבטיח שלעוזר ה-AI שלך תהיה גישה למידע סמכותי ומעודכן ליצירת קוד מדויק ומודרני.

**שימוש בעולם האמיתי**: "מהן הפקודות az cli ליצירת אפליקציה במכולה ב-Azure לפי תיעוד הרשמי של Microsoft Learn?" או "כיצד להגדיר Entity Framework עם הזרקת תלות ב-ASP.NET Core?" או "סקור את הקוד הזה כדי לוודא שהוא תואם להמלצות ביצועים בתיעוד Microsoft Learn." השרת מספק כיסוי מקיף ברחבי Microsoft Learn, תיעוד Azure ותיעוד Microsoft 365 באמצעות חיפוש סמנטי מתקדם למציאת המידע ההקשרי הרלוונטי ביותר. הוא מחזיר עד 10 קטעי תוכן איכותיים עם כותרות מאמרים וקישורים, תוך גישה תמידית לתיעוד העדכני ביותר של מיקרוסופט כאשר הוא מתפרסם.

**דוגמה בולטת**: השרת מציע את כלי `microsoft_docs_search` שמבצע חיפוש סמנטי בתיעוד הטכני הרשמי של מיקרוסופט. לאחר ההגדרה, ניתן לשאול שאלות כמו "כיצד לממש אימות JWT ב-ASP.NET Core?" ולקבל תגובות מפורטות ורשמיות עם קישורי מקור. איכות החיפוש יוצאת דופן כי הוא מבין הקשר – שאילתא על "containers" בהקשר Azure תחזיר תיעוד של Azure Container Instances, בעוד שאותו מונח בהקשר .NET יחזיר מידע רלוונטי של אוספי C#.

זה מועיל במיוחד לספריות ומקרים המשתנים במהירות או עודכנו לאחרונה. למשל, בפרויקטי קוד אחרונים רציתי לנצל תכונות בגרסאות האחרונות של Aspire ו-Microsoft.Extensions.AI. על ידי הכללת שרת Microsoft Learn Docs MCP, יכולתי להיעזר לא רק בתיעוד API, אלא גם במדריכים והנחיות שפורסמו ממש לאחרונה.

> **💡 טיפ מקצועי**
> 
> אפילו למודלים ידידותיים לכלים נדרש עידוד להשתמש בכלי MCP! שקול להוסיף הנחיה מערכתית או [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) כגון: "יש לך גישה ל-`microsoft.docs.mcp` – השתמש בכלי זה לחיפוש בתיעוד הרשמי העדכני של מיקרוסופט בעת טיפול בשאלות על טכנולוגיות Microsoft כמו C#, Azure, ASP.NET Core, או Entity Framework."
>
> לדוגמה מצוינת לשימוש זה, עיין במצב הצ'אט [C# .NET Janitor](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) ממאגר Awesome GitHub Copilot. מצב זה מנצל במיוחד את שרת Microsoft Learn Docs MCP לסייע בניקוי ומודרניזציה של קוד C# באמצעות דפוסים והמלצות עדכניות.
### 2. ☁️ שרת Azure MCP


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**מה זה עושה**: שרת Azure MCP הוא חבילת כלים מקיפה הכוללת יותר מ-15 מחברים ייעודיים לשירותי Azure, שמביאים את כל מערכת האקולוגית של Azure אל זרימת העבודה של ה-AI שלך. זה לא רק שרת יחיד – זו אוסף רב עוצמה הכולל ניהול משאבים, חיבוריות למסדי נתונים (PostgreSQL, SQL Server), ניתוח יומני Azure Monitor עם KQL, אינטגרציה עם Cosmos DB, ועוד הרבה יותר.

**למה זה שימושי**: מעבר לניהול משאבי Azure בלבד, השרת הזה משפר באופן דרמטי את איכות הקוד כשעובדים עם Azure SDKs. כשאתה משתמש ב-Azure MCP במצב Agent, הוא לא רק עוזר לך לכתוב קוד – הוא עוזר לך לכתוב *קוד Azure טוב יותר*, שעוקב אחרי דפוסי אימות עדכניים, שיטות טיפול בשגיאות מיטביות, ומנצל את התכונות האחרונות של ה-SDK. במקום לקבל קוד כללי שעשוי לעבוד, תקבל קוד שעוקב אחרי הדפוסים המומלצים של Azure לעומסי עבודה בפרודקשן.

**מודולים עיקריים כוללים**:
- **🗄️ מחברי מסדי נתונים**: גישה ישירה בשפה טבעית ל-Azure Database עבור PostgreSQL ו-SQL Server
- **📊 Azure Monitor**: ניתוח יומנים מונמך KQL ותובנות תפעוליות
- **🌐 ניהול משאבים**: ניהול מחזור חיים מלא של משאבי Azure
- **🔐 אימות**: דפוסי DefaultAzureCredential וזהות מנוהלת
- **📦 שירותי אחסון**: פעולות Blob Storage, Queue Storage ו-Table Storage
- **🚀 שירותי מכולות**: ניהול Azure Container Apps, Container Instances ו-AKS
- **ועוד מחברים ייעודיים רבים**

**שימוש במציאות**: "רשום לי את חשבונות האחסון שלי ב-Azure", "שאול חלל עבודה של Log Analytics עבור שגיאות בשעה האחרונה", או "עזור לי לבנות אפליקציית Azure בשימוש Node.js עם אימות נכון"

**תרחיש הדגמה מלא**: להלן תהליך מלא שמדגים את העוצמה של השילוב בין Azure MCP להרחבת GitHub Copilot for Azure ב-VS Code. כשיש לך את שניהם מותקנים ותיתן פקודה:

> "צור סקריפט Python שמעלה קובץ ל-Azure Blob Storage באמצעות אימות DefaultAzureCredential. הסקריפט צריך להתחבר לחשבון האחסון שלי בשם 'mycompanystorage', להעלות למכולה בשם 'documents', ליצור קובץ בדיקה עם חותמת זמן נוכחית להעלאה, לטפל בשגיאות בחן ולספק פלט אינפורמטיבי, לעקוב אחרי שיטות האימות וטיפול בשגיאות המומלצות של Azure, לכלול הערות שמסבירות איך אימות DefaultAzureCredential עובד, ולהפוך את הסקריפט למבנה טוב עם פונקציות ותיעוד נאותים."

שרת Azure MCP ייצור סקריפט Python מלא ומוכן פרודקשן שמ:
- משתמש ב-SDK האחרון של Azure Blob Storage עם דפוסי אסינכרוניות נכונים
- מיישם את DefaultAzureCredential עם הסבר מקיף של שרשרת הנפילה
- כולל טיפול בשגיאות מקיף עם סוגי החריגות הספציפיות של Azure
- עוקב אחרי שיטות העבודה הטובות ביותר של Azure SDK לניהול משאבים וטיפול בחיבורים
- מספק רישום מפורט ופלט קונסולה אינפורמטיבי
- יוצר סקריפט ממוסד היטב עם פונקציות, תיעוד ורמזי טיפוס

מה שמדהים בזה הוא שבלעדיו, ייתכן ותקבל קוד אחסון blob גנרי שעובד אך אינו עוקב אחרי דפוסי Azure הנוכחיים. עם Azure MCP, תקבל קוד שמשתמש בשיטות האימות האחרונות, מטפל בתרחישי שגיאה ספציפיים ל-Azure, ועוקב אחרי שיטות מומלצות של מיקרוסופט ליישומים בפרודקשן.

**דוגמה מובלטת**: התקשיתי לזכור את הפקודות הספציפיות של ממשקי השורת פקודה `az` ו-`azd` לשימוש חד-פעמי. תמיד זו תהליך דו-שלבי עבורי: תחילה חיפוש התחביר, ואז הרצת הפקודה. לעיתים קרובות פשוט נכנס לפורטל ומנווט כדי לסיים עבודה כי אני לא רוצה להודות שאני לא זוכר את התחביר ב-CLI. היכולת פשוט לתאר את מה שאני רוצה מדהימה, ואף יותר טוב כשאפשר לעשות זאת בלי לעזוב את סביבת הפיתוח שלי!

יש רשימה מצוינת של מקרים שימוש ב-[מאגר Azure MCP](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) שיעזרו לך להתחיל. להדרכות הקמה מקיפות ואפשרויות תצורה מתקדמות, עיין ב-[התיעוד הרשמי של Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 שרת GitHub MCP

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**מה זה עושה**: שרת GitHub MCP הרשמי מספק אינטגרציה חלקה עם כל מערכת האקולוגית של GitHub, ומציע גם גישה מרוחקת מאוחסנת וגם אפשרויות פריסה מקומית באמצעות Docker. זה לא רק על פעולות בסיסיות במאגר – זו ערכת כלים מקיפה הכוללת ניהול GitHub Actions, זרימות עבודות בקשות שיבה (pull request), מעקב אחרי בעיות, סריקות אבטחה, התראות, ויכולות אוטומציה מתקדמות.

**למה זה שימושי**: השרת הזה משנה את האופן שבו אתה מתקשר עם GitHub על ידי הבאת חוויית הפלטפורמה המלאה ישירות לסביבת הפיתוח שלך. במקום לעבור כל הזמן בין VS Code ו-GitHub.com לניהול פרויקטים, סקירת קוד ומעקב CI/CD, אתה יכול לנהל הכל באמצעות פקודות בשפה טבעית תוך כדי שמירה על מיקוד בקוד שלך.

> **ℹ️ הערה: סוגים שונים של 'סוכנים'**
> 
> אל תבלבל בין שרת GitHub MCP לבין סוכן הקידוד של GitHub (הסוכן AI שאפשר להקצות לו משימות קידוד אוטומטיות). שרת GitHub MCP פועל במצב Agent של VS Code כדי לספק אינטגרציה עם API של GitHub, בעוד שסוכן הקידוד של GitHub הוא תכונה נפרדת שיוצרת בקשות שיבה כאשר הוא מוקצה לבעיות ב-GitHub.

**יכולות עיקריות כוללות**:
- **⚙️ GitHub Actions**: ניהול צנרת CI/CD מלאה, מעקב אחרי זרימות עבודה וטיפול בארטיפקטים
- **🔀 בקשות שיבה (Pull Requests)**: יצירה, סקירה, מיזוג וניהול PRs עם מעקב סטטוס מקיף
- **🐛 בעיות (Issues)**: ניהול מחזור חיים מלא של בעיות, תגובות, תיוגים והקצאה
- **🔒 אבטחה**: התראות סריקת קוד, גילוי סודות, ואינטגרציה עם Dependabot
- **🔔 התראות**: ניהול חכם של התראות ושליטה במנויים למאגר
- **📁 ניהול מאגר**: פעולות קבצים, ניהול סניפים, וארגון המאגר
- **👥 שיתוף פעולה**: חיפוש משתמשים וארגונים, ניהול צוותים, ושליטה בגישה

**שימוש במציאות**: "צור בקשת שיבה מתוך הסניף המאפיין שלי", "הראה לי את כל ריצות ה-CI שנכשלו השבוע", "רשום התראות אבטחה פתוחות עבור מאגרי הקוד שלי", או "מצא את כל הבעיות שהוקצו אליי בארגונים שלי"

**תרחיש הדגמה מלא**: הנה זרימת עבודה חזקה שמדגימה את יכולות שרת GitHub MCP:

> "אני צריך להתכונן לסקירת הספרינט שלנו. הראה לי את כל בקשות השיבה שיצרתי השבוע, בדוק את סטטוס צנרת ה-CI/CD שלנו, צור סיכום של התראות אבטחה שיש לטפל בהן, ועזור לי לנסח הערות שחרור המבוססות על PRs ממוזגים עם תווית 'feature'."

שרת GitHub MCP יבצע:
- שאילתא אחר בקשות השיבה האחרונות שלך עם מידע מפורט על הסטטוס
- ניתוח ריצות זרימות עבודה והדגשת כישלונות או בעיות ביצועים
- איסוף תוצאות סריקת אבטחה ודירוג התראות קריטיות
- יצירת הערות שחרור מקיפות מתוך מידע שנשלף מ-PRs ממוזגים
- מתן צעדים הבאים לשלב תכנון הספרינט והכנת השחרור

**דוגמה מובלטת**: אני אוהב להשתמש בזה לזרימות עבודה של סקירת קוד. במקום לקפוץ בין VS Code, התראות GitHub ודפי בקשות שיבה, אני יכול להגיד "הראה לי את כל ה-PRs שממתינים לסקירה שלי" ואז "הוסף תגובה ל-PR #123 ששואלת על טיפול השגיאות בשיטת האימות." השרת מטפל בקריאות API של GitHub, שומר על הקשר השיחה, ואפילו עוזר לי לנסח תגובות סקירה יותר בונות.

**אפשרויות אימות**: השרת תומך גם ב-OAuth (שקוף ב-VS Code) וגם ב- Personal Access Tokens, עם כלי קונפיגורציה שמאפשרים להפעיל רק את הפונקציונליות של GitHub שאתה צריך. ניתן להפעיל אותו כשרת מרוחק לאינטגרציה מיידית או מקומית באמצעות Docker לשליטה מלאה.

> **💡 טיפ מקצועי**
> 
> הפעל רק את קבוצות הכלים שאתה צריך על ידי קביעת הפרמטר `--toolsets` בהגדרות שרת ה-MCP שלך כדי להקטין את גודל ההקשר ולשפר את בחירת כלי ה-AI. לדוגמה, הוסף `"--toolsets", "repos,issues,pull_requests,actions"` לארגומנטים של הקונפיגורציה של MCP עבורך זרימות עבודה פיתוחיות מרכזיות, או השתמש ב- `"--toolsets", "notifications, security"` אם אתה מעוניין בעיקר ביכולות ניטור GitHub.
### 4. 🔄 שרת Azure DevOps MCP

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**מה זה עושה**: מתחבר לשירותי Azure DevOps לניהול פרויקט כולל, מעקב אחרי Work Items, ניהול צנרת בנייה, ופעולות על מאגרים.

**למה זה שימושי**: עבור צוותים שמשתמשים ב-Azure DevOps כפלטפורמת DevOps הראשית שלהם, שרת MCP זה מפסיק את הצורך לעבור בין סביבת הפיתוח שלך וממשק הווב של Azure DevOps. ניתן לנהל Work Items, לבדוק סטטוס בנייה, לשאול מאגרים, ולטפל במשימות ניהול פרויקט ישירות מהעוזר AI שלך.

**שימוש במציאות**: "הראה לי את כל ה-Work Items הפעילים בספרינט הנוכחי עבור פרויקט WebApp", "צור דיווח באג עבור בעית ההתחברות שמצאתי עכשיו", או "בדוק את סטטוס צנרות הבנייה שלנו והראה לי כל כישלון אחרון"

**דוגמה מובלטת**: ניתן בקלות לבדוק את סטטוס הספרינט הנוכחי של הצוות שלך עם שאילתה פשוטה כמו "הראה לי את כל ה-Work Items הפעילים בספרינט הנוכחי עבור פרויקט WebApp" או "צור דיווח באג עבור בעית ההתחברות שמצאתי עכשיו" מבלי לעזוב את סביבת הפיתוח.

### 5. 📝 שרת MarkItDown MCP


[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**מה זה עושה**: MarkItDown הוא שרת המרה מקיף של מסמכים הממיר פורמטים שונים של קבצים למארקדאון איכותי, מותאם לצריכת LLM ולזרימות עבודה של ניתוח טקסט.

**למה זה שימושי**: חיוני עבור זרימות עבודה מודרניות של תיעוד! MarkItDown מטפל במגוון מרשים של פורמטים, תוך שמירה על מבנה קריטי במסמך כמו כותרות, רשימות, טבלאות וקישורים. בניגוד לכלי חילוץ טקסט פשוטים, הוא מתמקד בשמירת המשמעות הסמנטית והעיצוב שהם בעלי ערך הן לעיבוד בינה מלאכותית והן לקריאות אנושית.

**פורמטים של קבצים נתמכים**:
- **מסמכי משרד**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **קבצי מדיה**: תמונות (עם מטא-נתוני EXIF ו-OCR), אודיו (עם מטא-נתוני EXIF וטרנסקריפציה של דיבור)
- **תוכן רשת**: HTML, פידים של RSS, כתובות יוטיוב, דפי ויקיפדיה
- **פורמטי נתונים**: CSV, JSON, XML, קבצי ZIP (מעבד את התוכן בצורה רקורסיבית)
- **פורמטי פרסום**: EPub, מחברות Jupyter (.ipynb)
- **דואר אלקטרוני**: הודעות Outlook (.msg)
- **מתקדם**: אינטגרציה עם Azure Document Intelligence לעיבוד PDF משופר

**יכולות מתקדמות**: MarkItDown תומך בתיאורי תמונות מונעי LLM (כאשר מסופק לקוח OpenAI), Azure Document Intelligence לעיבוד PDF משופר, טרנסקריפציה של אודיו לתוכן דיבור, ומערכת תוספים להרחבה לפורמטי קבצים נוספים.

**שימוש בעולם האמיתי**: "המר מצגת PowerPoint זו למארקדאון עבור אתר התיעוד שלנו", "חלץ טקסט מה-PDF הזה עם מבנה כותרות תקין", או "המר גיליון Excel זה לפורמט טבלה קריא"

**דוגמה מובלטת**: לציטוט מ-[תיעוד MarkItDown](https://github.com/microsoft/markitdown#why-markdown):

> מארקדאון קרוב מאוד לטקסט רגיל, עם מינימום סימון או עיצוב, אך עדיין מספק דרך לייצוג מבנה מסמך חשוב. LLMs מרכזיים, כמו GPT-4o של OpenAI, "מדברים" מארקדאון באופן טבעי, ולעיתים קרובות משלבים מארקדאון בתשובותיהם ללא בקשה. זה מרמז כי הם אומנו על כמויות עצומות של טקסטים במבנה מארקדאון, ומבינים את זה היטב. כתוצאה צדדית, הקונבנציות של מארקדאון גם יעילות מאוד מבחינת אסימון.

MarkItDown ממש טוב בשמירת מבנה המסמך, מה שחשוב לזרימות עבודה של בינה מלאכותית. לדוגמה, בעת המרת מצגת PowerPoint, הוא שומר על ארגון השקופיות עם הכותרות הנכונות, מחלץ טבלאות כטבלאות מארקדאון, כולל טקסט אלטרנטיבי לתמונות, ואפילו מעבד את הערות הדובר. תרשימים מומרצים לטבלאות נתונים קריאות, והמארקדאון המתקבל שומר על הרצף הלוגי של המצגת המקורית. זה הופך אותו למושלם להזנת תוכן מצגות למערכות AI או ליצירת תיעוד משקופיות קיימות.
### 6. 🗃️ שרת SQL Server MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**מה זה עושה**: מספק גישה שיחתית למסדי נתונים של SQL Server (מקום, Azure SQL, או Fabric)

**למה זה שימושי**: דומה לשרת PostgreSQL אבל לאקוסיסטם Microsoft SQL. התחבר בקלות עם מחרוזת חיבור פשוטה והתחל לשאול בשפה טבעית – ללא צורך במעבר הקשר!

**שימוש בעולם האמיתי**: "מצא את כל ההזמנות שלא מומשו ב-30 הימים האחרונים" מתורגם לשאילתות SQL מתאימות ומחזיר תוצאות מעוצבות

**דוגמה מובלטת**: ברגע שמגדירים את חיבור מסד הנתונים, ניתן להתחיל לנהל שיחות עם הנתונים מיד. פוסט הבלוג מציג זאת באמצעות שאלה פשוטה: "לאיזה מסד נתונים אתה מחובר?" שרת ה-MCP מגיב בקריאה לכלי מסד נתונים מתאים, מתחבר למופע SQL Server ומחזיר פרטים אודות חיבור המסד הנוכחי – הכל ללא כתיבת שורת SQL אחת. השרת תומך בפעולות מסד נתונים מקיפות, מניהול סכמות ועד מניפולציית נתונים, הכל דרך הנחיות בשפה טבעית. לקבלת הוראות התקנה ודוגמאות תצורה עם VS Code ו-Claude Desktop, ראו: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 שרת Playwright MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**מה זה עושה**: מאפשר לסוכני AI לקיים אינטראקציה עם דפי אינטרנט לצורך בדיקות ואוטומציה

> **ℹ️ נושא כוח עבור GitHub Copilot**
> 
> שרת Playwright MCP מפעיל את סוכן הקידוד של GitHub Copilot, ומעניק לו יכולות גלישה ברשת! [למידע נוסף על תכונה זו](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**למה זה שימושי**: מושלם לבדיקות אוטומטיות המונעות מתיאורים בשפה טבעית. AI יכול לנווט באתרי אינטרנט, למלא טפסים, ולחלץ נתונים דרך צילומי מצב נגישות מובנים – זהו כלי חזק ביותר!

**שימוש בעולם האמיתי**: "בדוק את תהליך ההתחברות ואמת שהלוח טעון כראוי" או "צור בדיקה שמחפשת מוצרים ומאמתת את דף התוצאות" – הכל ללא צורך בקוד המקור של האפליקציה

**דוגמה מובלטת**: חברת הצוות שלי דבי אובריין עושה עבודה מדהימה לאחרונה עם שרת Playwright MCP! למשל, היא הראתה לאחרונה כיצד ניתן ליצור בדיקות Playwright שלמות מבלי אפילו לגשת לקוד המקור של האפליקציה. בתרחיש שלה, היא ביקשה מקופילוט ליצור בדיקה לאפליקציית חיפוש סרטים: עבור לאתר, חפש את "גרפילד", ואמת שהסרט מופיע בתוצאות. ה-MCP פתחה סשן דפדפן, חקרה את מבנה הדף בעזרת צילומי מצב DOM, מצאה את הסלקטורים הנכונים, ויצרה בדיקת TypeScript עובדת במלואה שעברה בהצלחה בריצה הראשונה.

מה שהופך זאת לעוצמתי באמת הוא שמדובר בגישור על הפער בין הנחיות בשפה טבעית לבין קוד בדיקה בר ביצוע. גישות מסורתיות דורשות כתיבת בדיקות ידנית או גישה לקוד להקשר. אך עם Playwright MCP, ניתן לבדוק אתרים חיצוניים, אפליקציות לקוח, או לעבוד בסצנריואים של בדיקות תיבת שחור שבהן אין גישה לקוד.


### 8. 💻 שרת Dev Box MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**מה זה עושה**: מנהל סביבות Microsoft Dev Box באמצעות שפה טבעית

**למה זה שימושי**: מפשט מאוד את ניהול סביבות הפיתוח! יצירה, תצורה וניהול של סביבות פיתוח ללא הצורך לזכור פקודות ספציפיות.

**שימוש בעולם האמיתי**: "הקם Dev Box חדש עם ה-SDK האחרון של .NET וקבע אותו עבור הפרויקט שלנו", "בדוק את מצב כל סביבות הפיתוח שלי", או "צור סביבה דמו סטנדרטית למצגות הצוות שלנו"

**דוגמה מובלטת**: אני מעריץ גדול של השימוש ב-Dev Box לפיתוח אישי. הרגע בו התבהר לי זה היה כשג'יימס מונטמניו הסביר כמה Dev Box טוב לדמוים בכנסים, כי יש לו חיבור אתרנט מהיר במיוחד ללא קשר לאינטרנט בבית המלון / בטיסה בו אני נמצא. למעשה, תרגלתי לאחרונה דמו של כנס בזמן שהמחשב הנייד שלי היה מחובר לאינטרנט דרך חם-נקודת הטלפון שלי במהלך נסיעה באוטובוס מברוז' לאנטוורפן! אבל הצעד הבא שלי כאן הוא להתמקד בניהול צוות של סביבות פיתוח מרובות וסביבות דמו סטנדרטיות. שימוש נוסף גדול שאני שומע מלקוחות וקולגות כמובן, הוא שימוש ב-Dev Box לסביבות פיתוח מראש מוגדרות. בשני המקרים, השימוש ב-MCP לתצורה וניהול Dev Boxes מאפשר אינטראקציה בשפה טבעית, הכל תוך כדי הישארות בסביבת הפיתוח שלך.

### 9. 🤖 שרת Microsoft Foundry MCP


[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**מה זה עושה**: שרת Microsoft Foundry MCP מספק למפתחים גישה מקיפה לאקוסיסטם ה-AI של Azure, כולל קטלוגי מודלים, ניהול פריסות, אינדוקס מידע עם Azure AI Search וכלי הערכה. שרת ניסיוני זה מחבר את הפער בין פיתוח AI לבין תשתית ה-AI החזקה של Azure, ומאפשר בנייה, פריסה והערכה נוחים של יישומי AI.

**למה זה שימושי**: שרת זה משנה את אופן העבודה עם שירותי Azure AI על ידי כך שהוא מביא יכולות AI ברמת ארגון ישירות לזרימת הפיתוח שלך. במקום לעבור בין פורטל Azure, תיעוד וסביבת הפיתוח שלך, ניתן לגלות מודלים, לפרוס שירותים, לנהל בסיסי ידע ולהעריך ביצועי AI באמצעות פקודות בשפה טבעית. זה רלוונטי במיוחד למפתחים שבונים יישומי RAG (הפקה מואצת באמצעות אחזור מידע), מנחים פריסות מרובות מודלים או מיישמים קווי הערכה מקיפים ל-AI.

**יכולות מפתח למפתחים**:
- **🔍 גילוי ופריסת מודלים**: חקור את קטלוג המודלים של Microsoft Foundry, קבל מידע מפורט עם דוגמאות קוד, ופרוס מודלים לשירותי Azure AI
- **📚 ניהול ידע**: צור ונהל אינדקסים ב-Azure AI Search, הוסף מסמכים, קבע מגדירים (indexers) ובנה מערכות RAG מתקדמות
- **⚡ אינטגרציית סוכנים של AI**: התחבר לסוכני Azure AI, שאול סוכנים קיימים, והערך ביצועים של סוכנים בתרחישי הפעלה
- **📊 מסגרת הערכה**: הפעל הערכות טקסט וסוכנים מקיפות, הפק דוחות ב-Markdown, ויישם בקרת איכות ליישומי AI
- **🚀 כלי אב טיפוס**: קבל הוראות התקנה עבור אב טיפוס מבוסס GitHub וגישה ל-Microsoft Foundry Labs למחקר ופיתוח מודלים מתקדמים

**שימוש מעשי בעולם האמיתי**: "פרוס מודל Phi-4 לשירותי Azure AI עבור היישום שלי", "צור אינדקס חיפוש חדש למערכת RAG לתיעוד שלי", "הערך את התגובות של הסוכן שלי על פי מדדי איכות", או "מצא את מודל ההסקה הטוב ביותר למשימות הניתוח המורכבות שלי"

**תסריט מדגים מלא**: זוהי זרימת עבודה עוצמתית לפיתוח AI:

> "אני בונה סוכן תמיכה ללקוחות. תעזור לי למצוא מודל הסקה טוב מתוך הקטלוג, לפרוס אותו לשירותי Azure AI, ליצור בסיס ידע מהתיעוד שלנו, להקים מסגרת הערכה לבדיקת איכות התגובות, ואחר כך לעזור לי לאב-טיפוס אינטגרציה עם טוקן GitHub למבחן."

שרת Microsoft Foundry MCP יבצע:
- שאילתות בקטלוג המודלים כדי להמליץ על מודלי הסקה אופטימליים בהתאם לדרישותיך
- יספק פקודות פריסה ומידע על מכסות לאזור Azure המועדף עליך
- יקים אינדקסי Azure AI Search עם סכימה מתאימה לתיעוד שלך
- יגדיר קווי הערכה עם מדדי איכות ובדיקות בטיחות
- יפיק קוד אב-טיפוס עם אימות GitHub למבחן מיידי
- יספק מדריכי התקנה מפורטים מותאמים לערמת הטכנולוגיה הספציפית שלך

**דוגמה מובלטת**: בתור מפתח, התקשיתי לעקוב אחרי הדגמים השונים של LLM הזמינים. אני מכיר כמה עיקריים, אבל הרגשתי שאני מפספס שיפורי פרודוקטיביות ויעילות. וכרטיסים ומכסות גורמים ללחץ וקושי בניהול – אף פעם לא בטוח אם אני בוחר את המודל הנכון למשימה הנכונה או מבזבז את התקציב בצורה לא יעילה. שמעתי על שרת MCP הזה מג׳יימס מונטמאגנו כשבדקתי המלצות עם שותפים, ואני נרגש לנסות אותו! יכולות גילוי המודלים נראות מרשימות במיוחד עבור מי כמוני שמחפש לחקור מעבר למודלים הרגילים ולמצוא מודלים מותאמים למשימות ספציפיות. מסגרת ההערכה אמורה לעזור לי לוודא שאני באמת מקבל תוצאות טובות יותר, ולא רק מנסה משהו חדש לשם הדוגמה.

> **ℹ️ סטטוס ניסיוני**
> 
> שרת MCP זה הוא ניסיוני ומתפתח באופן פעיל. תכונות ו-APIs עלולים להשתנות. מושלם לחקירת יכולות Azure AI ולבניית אב-טיפוס, אך יש לבדוק דרישות יציבות לשימוש בסביבה פרודקשן.
### 10. 🏢 שרת Microsoft 365 Agents Toolkit MCP

[![התקן ב-VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![התקן ב-VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**מה זה עושה**: מספק למפתחים כלים חיוניים לבניית סוכני AI ויישומים שמשולבים עם Microsoft 365 ו-Microsoft 365 Copilot, כולל אימות סכימות, קבלת קוד לדוגמה וסיוע בתיקון תקלות.

**למה זה שימושי**: פיתוח עבור Microsoft 365 ו-Copilot כולל סכימות מניפסט מורכבות ודפוסי פיתוח ספציפיים. שרת MCP זה מביא משאבי פיתוח חיוניים ישירות לסביבת העריכה שלך, מסייע לך לאמת סכימות, למצוא קוד לדוגמה ולפתור בעיות נפוצות ללא צורך בהתייחסות תכופה לתיעוד.

**שימוש מעשי**: "אמת את מניפסט הסוכן ההצהרתי שלי ותקן שגיאות סכימה שיש", "הראה לי דוגמאות קוד ליישום תוסף Microsoft Graph API", או "עזור לי לפתור בעיות אימות באפליקציית Teams שלי"

**דוגמה מובלטת**: פניתי לחברי ג׳ון מילר אחרי שדיברתי איתו בבילד על סוכני M365, והוא המליץ על שרת MCP זה. זה יכול להיות מעולה למפתחים חדשים לסוכני M365 כי הוא מספק תבניות, קוד לדוגמה ושלד לפיתוח מהיר בלי לשקוע בתיעוד. יכולות אימות הסכימה נראות שימושיות במיוחד למניעת שגיאות מבנה מניפסט שיכולות לגרום לשעות של תיקוני באגים.

> **💡 טיפ מקצועי**
> 
> השתמש בשרת זה לצד שרת Microsoft Learn Docs MCP לתמיכה מקיפה בפיתוח M365 – אחד מספק את התיעוד הרשמי והשני כלי פיתוח מעשיים וסיוע בתיקון בעיות.


## מה הלאה? 🔮

## 📋 סיכום

פרוטוקול Model Context (MCP) משנה את האופן שבו מפתחים מתקשרים עם עוזרי AI וכלים חיצוניים. 10 שרתי Microsoft MCP אלה מדגימים את עוצמת האינטגרציה הסטנדרטית של AI, ומאפשרים זרימות עבודה חלקות ששומרות על רצף הפיתוח תוך גישה ליכולות חזקות חיצוניות.

החל משילוב אקוסיסטם Azure כולל וכלה בכלים מתמחים כמו Playwright לאוטומציה דפדפן ו-MarkItDown לעיבוד מסמכים – שרתים אלה מציגים כיצד MCP יכול לשפר פרודוקטיביות בסביבות פיתוח מגוונות. הפרוטוקול הסטנדרטי מבטיח שכלים אלה עובדים יחד בהרמוניה, ויוצרים חווית פיתוח מגובשת.

ככל שהאקוסיסטם של MCP ממשיך להתפתח, שמירה על מעורבות בקהילה, חקירת שרתים חדשים ובניית פתרונות מותאמים אישית יהיו מפתח למקסם את הפרודוקטיביות בפיתוח שלך. אופיו הפתוח של MCP מאפשר לך לשלב כלים מספקים שונים ליצירת זרימת עבודה מושלמת לצרכים הספציפיים שלך.

## 🔗 משאבים נוספים

- [מאגר רשמי של Microsoft MCP](https://github.com/microsoft/mcp)
- [קהילה ותיעוד MCP](https://modelcontextprotocol.io/introduction)
- [תיעוד MCP ל-VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [תיעוד MCP ל-Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [תיעוד MCP ל-Azure](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [בואו נלמד – אירועי MCP](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [קוסטומיזציות מדהימות ל-GitHub Copilot](https://github.com/awesome-copilot)
- [MCP SDK בשפת C#](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [ימי פיתוח MCP בשידור חי 29-30 ביולי או צפייה על פי דרישה](https://aka.ms/mcpdevdays)

## 🎯 תרגילים

1. **התקנה וקונפיגורציה**: התקן אחד משרתי MCP בסביבת VS Code שלך ובדוק פונקציונליות בסיסית.
2. **שילוב זרימת עבודה**: עצב זרימת עבודה שמשלבת לפחות שלושה שרתי MCP שונים.
3. **תכנון שרת מותאם**: זהה משימה בשגרת הפיתוח היומית שלך שיכולה להרוויח משרת MCP מותאם וצרף מפרט עבורו.
4. **ניתוח ביצועים**: השווה בין היעילות של שימוש בשרתי MCP לבין גישות מסורתיות למשימות פיתוח נפוצות.
5. **הערכת אבטחה**: הערך את השלכות האבטחה של שימוש בשרתי MCP בסביבת הפיתוח שלך והצע פרקטיקות מיטביות.


הבא: [Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->