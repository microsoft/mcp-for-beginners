## התחלה  

[![בנה את שרת ה-MCP הראשון שלך](../../../translated_images/he/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(לחץ על התמונה למעלה לצפייה בסרטון של השיעור הזה)_

החלק הזה כולל מספר שיעורים:

- **1 השרת הראשון שלך**, בשיעור הראשון הזה תלמד כיצד ליצור את השרת הראשון שלך ולבדוק אותו באמצעות כלי הבדיקה, דרך חשובה לבדוק ולפתור בעיות בשרת שלך, [לשיעור](01-first-server/README.md)

- **2 לקוח**, בשיעור הזה תלמד כיצד לכתוב לקוח שיכול להתחבר לשרת שלך, [לשיעור](02-client/README.md)

- **3 לקוח עם LLM**, דרך טובה יותר לכתוב לקוח היא להוסיף לו LLM כך שיוכל "לנהל משא ומתן" עם השרת שלך על מה לעשות, [לשיעור](03-llm-client/README.md)

- **4 צריכת שרת במצב סוכן GitHub Copilot ב-Visual Studio Code**. כאן נבחן כיצד להפעיל את שרת ה-MCP שלנו מתוך Visual Studio Code, [לשיעור](04-vscode/README.md)

- **5 שרת stdio Transport**. stdio transport הוא התקן המומלץ לתקשורת בין שרת ללקוח MCP במפרט הנוכחי, המספק תקשורת מאובטחת מבוססת תהליכי משנה, [לשיעור](05-stdio-server/README.md)

- **6 סטרימינג HTTP עם MCP (Streamable HTTP)**. למד על סטרימינג HTTP מודרני, התראות התקדמות, וכיצד ליישם שרתי ולקוחות MCP בזמן אמת ובקנה מידה גדול באמצעות Streamable HTTP, [לשיעור](06-http-streaming/README.md)

- **7 שימוש בערכת כלים AI עבור VSCode** לצרוך ולבדוק את לקוחות ושרתי ה-MCP שלך, [לשיעור](07-aitk/README.md)

- **8 בדיקות**. כאן נתמקד במיוחד כיצד ניתן לבדוק את השרת והלקוח בדרכים שונות, [לשיעור](08-testing/README.md)

- **9 פריסה**. פרק זה יבחן דרכים שונות לפרוס את פתרונות ה-MCP שלך, [לשיעור](09-deployment/README.md)

- **10 שימוש מתקדם בשרת**. פרק זה מכסה שימוש מתקדם בשרת, [לשיעור](./10-advanced/README.md)

- **11 אימות**. פרק זה מכסה כיצד להוסיף אימות פשוט, מאימות בסיסי ועד שימוש ב-JWT ו-RBAC. מומלץ להתחיל כאן ואז לעבור לנושאים מתקדמים בפרק 5 ולבצע חיזוק אבטחה נוסף באמצעות ההמלצות בפרק 2, [לשיעור](./11-simple-auth/README.md)

פרוטוקול מודל הקשר (MCP) הוא פרוטוקול פתוח שמתקנן כיצד יישומים מספקים הקשר ל-LLMs. חשבו על MCP כמו חיבור USB-C ליישומי AI - הוא מספק דרך סטנדרטית לחבר מודלים של AI למקורות נתונים וכלים שונים.

## מטרות למידה

בסיום השיעור הזה, תוכל:

- להגדיר סביבות פיתוח עבור MCP ב-C#, Java, Python, TypeScript ו-JavaScript
- לבנות ולפרוס שרתי MCP בסיסיים עם תכונות מותאמות אישית (משאבים, הנחיות וכלים)
- ליצור יישומי מארח שמתחברים לשרתי MCP
- לבדוק ולפתור בעיות ביישומי MCP
- להבין אתגרים נפוצים בהגדרה ואת הפתרונות שלהם
- לחבר את יישומי MCP שלך לשירותי LLM פופולריים

## הגדרת סביבת MCP שלך

לפני שתתחיל לעבוד עם MCP, חשוב להכין את סביבת הפיתוח שלך ולהבין את זרימת העבודה הבסיסית. חלק זה ידריך אותך בשלבי ההגדרה הראשוניים כדי להבטיח התחלה חלקה עם MCP.

### דרישות מוקדמות

לפני שתצלול לפיתוח MCP, ודא שיש לך:

- **סביבת פיתוח**: עבור השפה שבחרת (C#, Java, Python, TypeScript או JavaScript)
- **IDE/עורך**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm או כל עורך קוד מודרני
- **מנהל חבילות**: NuGet, Maven/Gradle, pip או npm/yarn
- **מפתחות API**: עבור כל שירותי AI שאתה מתכנן להשתמש בהם ביישומי המארח שלך

### SDKs רשמיים

בפרקים הבאים תראה פתרונות שנבנו באמצעות Python, TypeScript, Java ו-.NET. הנה כל ה-SDKs הרשמיים הנתמכים.

MCP מספק SDKs רשמיים למספר שפות:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - מתוחזק בשיתוף פעולה עם Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - מתוחזק בשיתוף פעולה עם Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - המימוש הרשמי של TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - המימוש הרשמי של Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - המימוש הרשמי של Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - מתוחזק בשיתוף פעולה עם Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - המימוש הרשמי של Rust

## נקודות מפתח

- הגדרת סביבת פיתוח MCP היא פשוטה עם SDKs ייעודיים לשפה
- בניית שרתי MCP כוללת יצירה ורישום כלים עם סכמות ברורות
- לקוחות MCP מתחברים לשרתים ולמודלים כדי לנצל יכולות מורחבות
- בדיקות ופתרון בעיות הם חיוניים ליישומי MCP אמינים
- אפשרויות פריסה נעות מפיתוח מקומי ועד פתרונות מבוססי ענן

## תרגול

יש לנו סט דוגמאות שמשלים את התרגילים שתראה בכל הפרקים בחלק הזה. בנוסף, לכל פרק יש גם תרגילים ומשימות משלו.

- [Java Calculator](./samples/java/calculator/README.md)
- [.Net Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## משאבים נוספים

- [בנה סוכנים באמצעות פרוטוקול מודל הקשר על Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP מרוחק עם Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## מה הלאה

הבא: [יצירת שרת MCP הראשון שלך](01-first-server/README.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.