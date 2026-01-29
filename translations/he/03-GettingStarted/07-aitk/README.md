# צריכת שרת מהרחבת AI Toolkit עבור Visual Studio Code

כשאתם בונים סוכן AI, זה לא רק על יצירת תגובות חכמות; זה גם על לתת לסוכן שלכם את היכולת לבצע פעולות. כאן נכנס לתמונה פרוטוקול Model Context Protocol (MCP). MCP מאפשר לסוכנים גישה לכלים ושירותים חיצוניים בצורה עקבית. תחשבו על זה כמו לחבר את הסוכן שלכם לארגז כלים שהוא *באמת* יכול להשתמש בו.

נניח שאתם מחברים סוכן לשרת MCP של מחשבון. פתאום, הסוכן שלכם יכול לבצע פעולות מתמטיות רק על ידי קבלת שאלה כמו "מה זה 47 כפול 89?"—בלי צורך לקודד לוגיקה או לבנות APIs מותאמים אישית.

## סקירה כללית

השיעור הזה מכסה איך לחבר שרת MCP של מחשבון לסוכן באמצעות הרחבת [AI Toolkit](https://aka.ms/AIToolkit) ב-Visual Studio Code, ולאפשר לסוכן שלכם לבצע פעולות מתמטיות כמו חיבור, חיסור, כפל וחילוק באמצעות שפה טבעית.

AI Toolkit היא הרחבה עוצמתית ל-Visual Studio Code שמייעלת את פיתוח הסוכנים. מהנדסי AI יכולים בקלות לבנות יישומי AI על ידי פיתוח ובדיקת מודלים גנרטיביים—מקומית או בענן. ההרחבה תומכת ברוב המודלים הגנרטיביים המרכזיים הזמינים כיום.

*הערה*: AI Toolkit תומכת כרגע ב-Python ו-TypeScript.

## מטרות למידה

בסוף השיעור הזה, תוכלו:

- לצרוך שרת MCP באמצעות AI Toolkit.
- להגדיר תצורת סוכן שתאפשר לו לגלות ולהשתמש בכלים המסופקים על ידי שרת MCP.
- להשתמש בכלי MCP באמצעות שפה טבעית.

## גישה

כך ניגש לנושא ברמה גבוהה:

- יצירת סוכן והגדרת ההנחיה המערכתית שלו.
- יצירת שרת MCP עם כלים של מחשבון.
- חיבור Agent Builder לשרת MCP.
- בדיקת הפעלת הכלים של הסוכן באמצעות שפה טבעית.

מעולה, עכשיו כשאנחנו מבינים את הזרימה, בואו נגדיר סוכן AI שינצל כלים חיצוניים דרך MCP, ויעצים את היכולות שלו!

## דרישות מוקדמות

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit עבור Visual Studio Code](https://aka.ms/AIToolkit)

## תרגיל: צריכת שרת

> [!WARNING]
> הערה למשתמשי macOS. אנחנו כרגע חוקרים בעיה שמשפיעה על התקנת תלותים ב-macOS. כתוצאה מכך, משתמשי macOS לא יוכלו להשלים את המדריך הזה בשלב זה. נעדכן את ההוראות ברגע שתהיה תיקון זמין. תודה על הסבלנות וההבנה!

בתרגיל הזה, תבנו, תפעילו ותשפרו סוכן AI עם כלים משרת MCP בתוך Visual Studio Code באמצעות AI Toolkit.

### -0- שלב מקדים, הוסיפו את מודל OpenAI GPT-4o ל-My Models

התרגיל משתמש במודל **GPT-4o**. יש להוסיף את המודל ל-**My Models** לפני יצירת הסוכן.

![צילום מסך של ממשק בחירת מודלים בהרחבת AI Toolkit של Visual Studio Code. הכותרת היא "Find the right model for your AI Solution" עם כותרת משנה המעודדת משתמשים לגלות, לבדוק ולפרוס מודלים של AI. מתחת, תחת "Popular Models," מוצגים שישה כרטיסי מודלים: DeepSeek-R1 (מתארח ב-GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - קטן, מהיר), ו-DeepSeek-R1 (מתארח ב-Ollama). כל כרטיס כולל אפשרויות "Add" להוספת המודל או "Try in Playground](../../../../translated_images/he/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.png)

1. פתחו את ההרחבה **AI Toolkit** מ-**Activity Bar**.
1. בקטע **Catalog**, בחרו **Models** כדי לפתוח את **Model Catalog**. בחירת **Models** פותחת את **Model Catalog** בלשונית עורך חדשה.
1. בשורת החיפוש של **Model Catalog**, הזינו **OpenAI GPT-4o**.
1. לחצו על **+ Add** כדי להוסיף את המודל לרשימת **My Models**. ודאו שבחרתם במודל שמתארח ב-**GitHub**.
1. ב-**Activity Bar**, ודאו שהמודל **OpenAI GPT-4o** מופיע ברשימה.

### -1- יצירת סוכן

**Agent (Prompt) Builder** מאפשר לכם ליצור ולהתאים אישית סוכנים מבוססי AI. בחלק הזה, תיצרו סוכן חדש ותשייכו לו מודל שיניע את השיחה.

![צילום מסך של ממשק "Calculator Agent" ב-AI Toolkit עבור Visual Studio Code. בלוח השמאלי, המודל שנבחר הוא "OpenAI GPT-4o (via GitHub)." הנחיית המערכת היא "You are a professor in university teaching math," והנחיית המשתמש היא "Explain to me the Fourier equation in simple terms." אפשרויות נוספות כוללות כפתורים להוספת כלים, הפעלת MCP Server, ובחירת פלט מובנה. כפתור כחול "Run" נמצא בתחתית. בלוח הימני, תחת "Get Started with Examples," מופיעים שלושה סוכנים לדוגמה: Web Developer (עם MCP Server, Second-Grade Simplifier, ו-Dream Interpreter, כל אחד עם תיאור קצר של תפקידו.](../../../../translated_images/he/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.png)

1. פתחו את ההרחבה **AI Toolkit** מ-**Activity Bar**.
1. בקטע **Tools**, בחרו **Agent (Prompt) Builder**. בחירת **Agent (Prompt) Builder** פותחת את **Agent (Prompt) Builder** בלשונית עורך חדשה.
1. לחצו על כפתור **+ New Agent**. ההרחבה תפעיל אשף הגדרה דרך **Command Palette**.
1. הזינו את השם **Calculator Agent** ולחצו **Enter**.
1. ב-**Agent (Prompt) Builder**, בשדה **Model**, בחרו במודל **OpenAI GPT-4o (via GitHub)**.

### -2- יצירת הנחיית מערכת לסוכן

לאחר שהסוכן נבנה, הגיע הזמן להגדיר את האישיות והמטרה שלו. בחלק הזה, תשתמשו בתכונת **Generate system prompt** כדי לתאר את ההתנהגות המיועדת של הסוכן—במקרה הזה, סוכן מחשבון—ותתנו למודל לכתוב את הנחיית המערכת עבורכם.

![צילום מסך של ממשק "Calculator Agent" ב-AI Toolkit עבור Visual Studio Code עם חלון מודאלי פתוח שכותרתו "Generate a prompt." המודאל מסביר שניתן ליצור תבנית הנחיה על ידי שיתוף פרטים בסיסיים וכולל תיבת טקסט עם הנחיית מערכת לדוגמה: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." מתחת לתיבת הטקסט יש כפתורים "Close" ו-"Generate". ברקע, חלק מהגדרת הסוכן גלויה, כולל המודל שנבחר "OpenAI GPT-4o (via GitHub)" ושדות להנחיות מערכת ומשתמש.](../../../../translated_images/he/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.png)

1. בקטע **Prompts**, לחצו על כפתור **Generate system prompt**. כפתור זה פותח את בונה ההנחיות שמנצל AI ליצירת הנחיית מערכת עבור הסוכן.
1. בחלון **Generate a prompt**, הזינו את הטקסט הבא: `אתה עוזר מתמטי יעיל ומועיל. כשנותנים לך בעיה הכוללת אריתמטיקה בסיסית, אתה מגיב עם התוצאה הנכונה.`
1. לחצו על כפתור **Generate**. תופיע התראה בפינה הימנית-תחתונה המאשרת שהנחיית המערכת נוצרת. לאחר שהיצירה תושלם, ההנחיה תופיע בשדה **System prompt** של **Agent (Prompt) Builder**.
1. סקרו את **System prompt** וערכו במידת הצורך.

### -3- יצירת שרת MCP

עכשיו, לאחר שהגדרתם את הנחיית המערכת של הסוכן—המנחה את התנהגותו ותגובותיו—הגיע הזמן לצייד את הסוכן ביכולות מעשיות. בחלק הזה, תיצרו שרת MCP של מחשבון עם כלים לביצוע חיבור, חיסור, כפל וחילוק. שרת זה יאפשר לסוכן שלכם לבצע פעולות מתמטיות בזמן אמת בתגובה להנחיות בשפה טבעית.

!["צילום מסך של החלק התחתון של ממשק Calculator Agent ב-AI Toolkit עבור Visual Studio Code. הוא מציג תפריטים נפתחים עבור “Tools” ו-“Structure output,” יחד עם תפריט נפתח שכותרתו “Choose output format” שמוגדר ל-“text.” מימין, יש כפתור שכותרתו “+ MCP Server” להוספת שרת Model Context Protocol. אייקון מציין מקום לתמונה מוצג מעל קטע Tools.](../../../../translated_images/he/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.png)

AI Toolkit מצוידת בתבניות להקלת יצירת שרת MCP משלכם. נשתמש בתבנית Python ליצירת שרת MCP של מחשבון.

*הערה*: AI Toolkit תומכת כרגע ב-Python ו-TypeScript.

1. בקטע **Tools** של **Agent (Prompt) Builder**, לחצו על כפתור **+ MCP Server**. ההרחבה תפעיל אשף הגדרה דרך **Command Palette**.
1. בחרו **+ Add Server**.
1. בחרו **Create a New MCP Server**.
1. בחרו **python-weather** כתבנית.
1. בחרו **Default folder** לשמירת תבנית שרת MCP.
1. הזינו את השם הבא לשרת: **Calculator**
1. חלון חדש של Visual Studio Code ייפתח. בחרו **Yes, I trust the authors**.
1. באמצעות הטרמינל (**Terminal** > **New Terminal**), צרו סביבה וירטואלית: `python -m venv .venv`
1. באמצעות הטרמינל, הפעילו את הסביבה הווירטואלית:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. באמצעות הטרמינל, התקינו את התלויות: `pip install -e .[dev]`
1. בתצוגת **Explorer** של **Activity Bar**, הרחיבו את התיקייה **src** ובחרו **server.py** כדי לפתוח את הקובץ בעורך.
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

### -4- הפעלת הסוכן עם שרת MCP של מחשבון

עכשיו, כשהסוכן שלכם מצויד בכלים, הגיע הזמן להשתמש בהם! בחלק הזה, תגישו הנחיות לסוכן כדי לבדוק ולאמת אם הסוכן מנצל את הכלי המתאים משרת MCP של מחשבון.

![צילום מסך של ממשק Calculator Agent ב-AI Toolkit עבור Visual Studio Code. בלוח השמאלי, תחת “Tools,” נוסף שרת MCP בשם local-server-calculator_server, שמציג ארבעה כלים זמינים: add, subtract, multiply, ו-divide. תג מציין שארבעה כלים פעילים. מתחת יש קטע “Structure output” מכווץ וכפתור כחול “Run.” בלוח הימני, תחת “Model Response,” הסוכן מפעיל את הכלים multiply ו-subtract עם קלטים {"a": 3, "b": 25} ו-{"a": 75, "b": 20} בהתאמה. ה-“Tool Response” הסופי מוצג כ-75.0. כפתור “View Code” מופיע בתחתית.](../../../../translated_images/he/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.png)

תפעילו את שרת MCP של מחשבון במכונת הפיתוח המקומית שלכם דרך **Agent Builder** כלקוח MCP.

1. לחצו `F5` כדי להתחיל לנפות שגיאות בשרת MCP. **Agent (Prompt) Builder** ייפתח בלשונית עורך חדשה. סטטוס השרת גלוי בטרמינל.
1. בשדה **User prompt** של **Agent (Prompt) Builder**, הזינו את ההנחיה הבאה: `קניתי 3 פריטים במחיר של $25 כל אחד, ואז השתמשתי בהנחה של $20. כמה שילמתי?`
1. לחצו על כפתור **Run** כדי ליצור את תגובת הסוכן.
1. סקרו את הפלט של הסוכן. המודל אמור להסיק ששילמתם **$55**.
1. הנה פירוט של מה שצריך לקרות:
    - הסוכן בוחר בכלים **multiply** ו-**subtract** כדי לעזור בחישוב.
    - הערכים `a` ו-`b` המתאימים מוקצים לכלי **multiply**.
    - הערכים `a` ו-`b` המתאימים מוקצים לכלי **subtract**.
    - התגובה מכל כלי מסופקת ב-**Tool Response** המתאים.
    - הפלט הסופי מהמודל מסופק ב-**Model Response** הסופי.
1. הגישו הנחיות נוספות כדי לבדוק את הסוכן. תוכלו לשנות את ההנחיה הקיימת בשדה **User prompt** על ידי לחיצה לתוך השדה והחלפת ההנחיה הקיימת.
1. לאחר שתסיימו לבדוק את הסוכן, תוכלו לעצור את השרת דרך **הטרמינל** על ידי הזנת **CTRL/CMD+C** כדי לצאת.

## משימה

נסו להוסיף כלי נוסף לקובץ **server.py** שלכם (לדוגמה: להחזיר את השורש הריבועי של מספר). הגישו הנחיות נוספות שידרשו מהסוכן לנצל את הכלי החדש שלכם (או כלים קיימים). ודאו שאתם מפעילים מחדש את השרת כדי לטעון כלים שנוספו.

## פתרון

[פתרון](./solution/README.md)

## נקודות מפתח

הנקודות המרכזיות מהפרק הזה הן:

- הרחבת AI Toolkit היא לקוח מצוין שמאפשר לצרוך שרתי MCP והכלים שלהם.
- תוכלו להוסיף כלים חדשים לשרתי MCP, להרחיב את יכולות הסוכן כדי לעמוד בדרישות משתנות.
- AI Toolkit כוללת תבניות (לדוגמה, תבניות שרת MCP ב-Python) כדי לפשט את יצירת הכלים המותאמים אישית.

## משאבים נוספים

- [מסמכי AI Toolkit](https://aka.ms/AIToolkit/doc)

## מה הלאה
- הבא: [בדיקות וניפוי שגיאות](../08-testing/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.