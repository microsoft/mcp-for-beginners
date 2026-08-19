# צריכת שרת מהתוסף AI Toolkit עבור Visual Studio Code

כאשר אתם מפתחים סוכן בינה מלאכותית, זה לא רק על יצירת תגובות חכמות; זה גם על מתן היכולת לסוכן שלכם לפעול. כאן נכנס לפרוטוקול הקשר המודל (MCP). MCP מקל על סוכנים לגשת לכלים ושירותים חיצוניים בצורה עקבית. חשבו על זה כמו לחבר את הסוכן שלכם אל ארגז כלים שהוא יכול *באמת* להשתמש בו.

נגיד שאתם מחברים סוכן לשרת MCP למחשבון. פתאום, הסוכן שלכם יכול לבצע פעולות מתמטיות רק על ידי קבלת פקודה כמו "כמה זה 47 כפול 89?"—בלי צורך לכתוב לוגיקה קשה או לבנות APIs מותאמים.

## סקירה כללית

השיעור הזה מכסה כיצד לחבר שרת MCP למחשבון לסוכן באמצעות התוסף [AI Toolkit](https://aka.ms/AIToolkit) ב-Visual Studio Code, מה שמאפשר לסוכן לבצע פעולות מתמטיות כגון חיבור, חיסור, כפל וחילוק בשפה טבעית.

AI Toolkit הוא תוסף חזק עבור Visual Studio Code המייעל את פיתוח הסוכנים. מהנדסי AI יכולים בקלות לבנות יישומי בינה מלאכותית על ידי פיתוח ובדיקה של מודלים מבוססי יצירה—מקומית או בענן. התוסף תומך ברוב המודלים הגדולים הקיימים כיום.

*הערה*: AI Toolkit תומך כרגע בפייתון ו-TypeScript.

## מטרות למידה

בסוף השיעור תהיה לכם היכולת:

- לצרוך שרת MCP דרך AI Toolkit.
- להגדיר תצורת סוכן כדי לאפשר לו לגלות ולנצל כלים המסופקים על ידי שרת MCP.
- להשתמש בכלי MCP באמצעות שפה טבעית.

## גישה

כך ניגש לזה ברמה גבוהה:

- ליצור סוכן ולהגדיר את ההנחיה המערכתית שלו.
- ליצור שרת MCP עם כלי מחשבון.
- לחבר את Agent Builder לשרת MCP.
- לבדוק את קריאת הכלים של הסוכן בשפה טבעית.

מצוין, עכשיו כשאנחנו מבינים את הזרימה, בואו נגדיר סוכן AI שישתמש בכלים חיצוניים דרך MCP, ויגדיל את היכולות שלו!

## דרישות מוקדמות

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit עבור Visual Studio Code](https://aka.ms/AIToolkit)

## תרגיל: צריכת שרת

> [!WARNING]
> הערה למשתמשי macOS. אנחנו בודקים כרגע בעיה המשפיעה על התקנת תלויות ב-macOS. כתוצאה מכך, משתמשי macOS לא יוכלו להשלים את המדריך הזה כרגע. נעדכן את ההוראות ברגע שתיקון יהיה זמין. תודה על הסבלנות וההבנה!

בתרגיל הזה תבנו, תריצו, ותשפרו סוכן AI עם כלים משרת MCP בתוך Visual Studio Code באמצעות AI Toolkit.

### -0- שלב הכנה, הוספת דגם GPT-4o ל-My Models

התרגיל משתמש בדגם **GPT-4o**. יש להוסיף את הדגם ל-**My Models** לפני יצירת הסוכן.

![צילום מסך של ממשק בחירת דגם בתוסף AI Toolkit של Visual Studio Code. הכותרת אומרת "מצאו את הדגם המתאים לפתרון הבינה המלאכותית שלכם" עם כותרת משנה המעודדת גילוי, בדיקה, ופריסה של דגמי AI. למטה, תחת "דגמים פופולריים," מוצגות שש כרטיסיות של דגמים: DeepSeek-R1 (מתארח ב-GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - קטן, מהיר), ו-DeepSeek-R1 (מתארח ב-Ollama). לכל כרטיס כפתורים להוספה או ניסיון בשדה Playground](../../../../translated_images/he/aitk-model-catalog.2acd38953bb9c119.webp)

1. פתחו את התוסף **AI Toolkit** משורת הפעילות (Activity Bar).
1. בסקשן **Catalog** בחרו **Models** כדי לפתוח את **קטלוג הדגמים**. בחירת **Models** תפתח את **קטלוג הדגמים** בכרטיס עורך חדש.
1. בשורת החיפוש של **קטלוג הדגמים** הזינו **OpenAI GPT-4o**.
1. לחצו על **+ הוסף** כדי להוסיף את הדגם לרשימת **My Models** שלכם. ודאו שבחרתם בדגם המתארח ב-GitHub.
1. ב-**Activity Bar**, ודאו שהדגם **OpenAI GPT-4o** מופיע ברשימה.

### -1- יצירת סוכן

ה-**Agent (Prompt) Builder** מאפשר לכם ליצור ולערוך סוכני AI משלכם. בחלק זה, תיצרו סוכן חדש ותצמידו לו דגם שמפעיל את השיחה.

![צילום מסך של ממשק "Calculator Agent" ב-AI Toolkit ל-Visual Studio Code. בפאנל השמאלי, הדגם שנבחר הוא "OpenAI GPT-4o (דרך GitHub)." ההנחיה המערכתית היא "אתה פרופסור באוניברסיטה שלמד מתמטיקה," וההנחיה למשתמש היא "הסבר לי את המשוואה של פורייה במונחים פשוטים." אפשרויות נוספות כוללות כפתורים להוספת כלים, הפעלת MCP Server, ובחירת פלט מובנה. כפתור "הרצה" כחול בחלק התחתון. בפאנל הימני, תחת "התחל עם דוגמאות," שלושה סוכנים לדוגמא: מפתח אתרים (עם MCP Server, מפשט כיתה ב', ומפרש חלומות, כל אחד עם תיאור קצר של תפקידו).](../../../../translated_images/he/aitk-agent-builder.901e3a2960c3e477.webp)

1. פתחו את התוסף **AI Toolkit** משורת הפעילות.
1. בסקשן **Tools**, בחרו **Agent (Prompt) Builder**. בחירת **Agent (Prompt) Builder** תפתח את הפונקציה בכרטיס עורך חדש.
1. לחצו על כפתור **+ סוכן חדש**. התוסף יפעיל אשף דרך **Command Palette**.
1. הזינו את השם **Calculator Agent** ולחצו **Enter**.
1. ב-**Agent (Prompt) Builder**, בשדה **Model**, בחרו את הדגם **OpenAI GPT-4o (דרך GitHub)**.

### -2- יצירת הנחיה מערכתית לסוכן

עם יצירת הסוכן, הגיע הזמן להגדיר את האישיות והמטרה שלו. בחלק זה, תשתמשו בתכונת **Generate system prompt** כדי לתאר את ההתנהגות המתוכננת של הסוכן—למשל, סוכן מחשבון—ותהיו שהדגם יכתוב עבורכם את ההנחיה המערכתית.

![צילום מסך של ממשק "Calculator Agent" ב-AI Toolkit ל-Visual Studio Code עם חלון מודאלי פתוח שכותרתו "Generate a prompt." החלון מסביר שניתן ליצור תבנית הנחיה על ידי שיתוף פרטים בסיסיים וכולל תיבת טקסט עם דוגמת הנחיה מערכתית: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." מתחת לתיבת הטקסט יש כפתורים "Close" ו-"Generate." ברקע, חלק מהגדרת הסוכן נראה, כולל הדגם שנבחר "OpenAI GPT-4o (via GitHub)" ושדות להנחיות מערכת ומשתמש.](../../../../translated_images/he/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. בסקשן **Prompts**, לחצו על הכפתור **Generate system prompt**. כפתור זה פותח את הבונה הנחיות שמשתמש ב-AI כדי ליצור הנחיה מערכתית לסוכן.
1. בחלון **Generate a prompt**, הזינו את הטקסט הבא: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. לחצו על כפתור **Generate**. יופיע התראה בפינה התחתונה-ימנית המאשרת שההנחיה המערכתית נוצרת. לאחר השלמת יצירת ההנחיה, היא תופיע בשדה **System prompt** ב-**Agent (Prompt) Builder**.
1. עברו על ה-**System prompt** ושנו במידת הצורך.

### -3- יצירת שרת MCP

עכשיו כשקבעתם את ההנחיה המערכתית לסוכן—המנחה את התנהגותו ותגובותיו—הגיע הזמן לצייד את הסוכן ביכולות מעשיות. בחלק זה, תיצרו שרת MCP למחשבון עם כלים לביצוע פעולות חיבור, חיסור, כפל וחילוק. שרת זה יאפשר לסוכן לבצע חישובים בזמן אמת בתגובה להנחיות בשפה טבעית.

![צילום מסך של החלק התחתון בממשק Calculator Agent בתוסף AI Toolkit של Visual Studio Code. מוצגים תפריטים נפתחים לכלי עבודה ולפלט מובנה, כולל תפריט נפתח לסוג הפלט שנבחר להצגה כטקסט. מימין יש כפתור "+ MCP Server" להוספת שרת Model Context Protocol. מעל לסקשן הכלים יש אזור תמונה ריק.](../../../../translated_images/he/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit מצויד בתבניות להקלת יצירת שרת MCP משלכם. נשתמש בתבנית פייתון ליצירת שרת MCP למחשבון.

*הערה*: AI Toolkit תומך כרגע בפייתון ו-TypeScript.

1. בסקשן **Tools** של **Agent (Prompt) Builder**, לחצו על כפתור **+ MCP Server**. התוסף יפעל אשף דרך **Command Palette**.
1. בחרו **+ הוסף שרת**.
1. בחרו **צור שרת MCP חדש**.
1. בחרו בתבנית **python-weather**.
1. בחרו **תיקיית ברירת מחדל** לשמירת תבנית שרת MCP.
1. הזינו את השם הבא לשרת: **Calculator**
1. חלון Visual Studio Code חדש ייפתח. בחרו **כן, אני סומך על המחברים**.
1. באמצעות הטרמינל (**Terminal** > **טרמינל חדש**), צרו סביבה וירטואלית: `python -m venv .venv`
1. באמצעות הטרמינל, הפעלו את הסביבה הווירטואלית:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. באמצעות הטרמינל, התקינו את התלויות: `pip install -e .[dev]`
1. בתצוגת **Explorer** בשורת הפעילות, הרחיבו את התיקיה **src** ובחרו ב-**server.py** לפתיחתו בעורך.
1. החליפו את הקוד בקובץ **server.py** עם הקוד הבא ושמרו:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- הרצת הסוכן עם שרת MCP למחשבון

עכשיו כשלסוכן שלכם יש כלים, הגיע הזמן להשתמש בהם! בחלק זה תגישו הנחיות לסוכן כדי לבדוק ולוודא האם הסוכן משתמש בכלי המתאים משרת MCP למחשבון.

![צילום מסך של ממשק Calculator Agent בתוסף AI Toolkit ל-Visual Studio Code. בפאנל השמאלי, תחת "Tools," נוסף שרת MCP בשם local-server-calculator_server, המראה ארבעה כלים זמינים: חיבור, חיסור, כפל וחילוק. תווית מראה שארבעה כלים פעילים. מתחת יש סקשן "Structure output" מכווץ וכפתור הרצה כחול. בפאנל הימני, תחת "Model Response," הסוכן מפעיל את כלים הכפל והחיסור עם קלטים {"a": 3, "b": 25} ו-{"a": 75, "b": 20} בהתאמה. התגובה הסופית של הכלי מוצגת כ-75.0. כפתור "View Code" מופיע בתחתית.](../../../../translated_images/he/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

תפעילו את שרת MCP למחשבון במכונת הפיתוח המקומית שלכם דרך **Agent Builder** כלקוח MCP.

1. לחצו על `F5` כדי להתחיל לנפות את שרת MCP. **Agent (Prompt) Builder** יפתח בכרטיס עורך חדש. מצב השרת ייראה בטרמינל.
1. בשדה **User prompt** של **Agent (Prompt) Builder**, הזינו את הפקודה הבאה: `קניתי 3 פריטים במחיר 25$ כל אחד, ואז השתמשתי בהנחה של 20$. כמה שילמתי?`
1. לחצו על כפתור **Run** כדי לייצר את תגובת הסוכן.
1. עברו על פלט הסוכן. המודל אמור להסיק ששילמתם **55$**.
1. הנה פירוט מה אמור לקרות:
    - הסוכן בוחר בכלי **כפל** ו**חיסור** כדי לסייע בחישוב.
    - ערכי `a` ו-`b` מוקצים לכלי **כפל**.
    - ערכי `a` ו-`b` מוקצים לכלי **חיסור**.
    - התגובה מכל כלי מוצגת ב-**Tool Response** המתאים.
    - הפלט הסופי מהמודל מופיע ב-**Model Response**.
1. הגישו הנחיות נוספות כדי לבדוק את הסוכן לעומק. אפשר לשנות את ההנחיה הקיימת בשדה **User prompt** על ידי לחיצה ושינוי הטקסט.
1. כשתסיימו לבדוק את הסוכן, תוכלו לעצור את השרת דרך **טרמינל** על ידי הקשת **CTRL/CMD+C** כדי לצאת.

## מטלה

נסו להוסיף כלי נוסף לקובץ **server.py** שלכם (למשל: החזרת שורש ריבועי של מספר). הגישו הנחיות נוספות שידרשו מהסוכן להשתמש בכלי החדש שלכם (או בכלים קיימים). וודאו לאתחל את השרת לטעון את הכלים החדשים.

## פתרון

[פתרון](./solution/README.md)

## נקודות מרכזיות

הנקודות המרכזיות בפרק זה הן:

- תוסף AI Toolkit הוא לקוח מצוין המאפשר לכם לצרוך שרתי MCP וכלים שלהם.
- תוכלו להוסיף כלים חדשים לשרתי MCP, ולהרחיב את יכולות הסוכן כדי לעמוד בדרישות בהתפתחות.
- AI Toolkit כולל תבניות (למשל, תבניות שרת MCP בפייתון) להקל על יצירת כלים מותאמים.

## משאבים נוספים

- [תיעוד AI Toolkit](https://aka.ms/AIToolkit/doc)

## מה הלאה
- הבא: [בדיקה וניפוי שגיאות](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->