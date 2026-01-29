# מדריך לימוד - פרוטוקול הקשר מודל (MCP) למתחילים

מדריך זה מספק סקירה כללית של מבנה המאגר והתוכן עבור תכנית הלימודים "פרוטוקול הקשר מודל (MCP) למתחילים". השתמשו במדריך זה כדי לנווט במאגר בצורה יעילה ולהפיק את המרב מהמשאבים הזמינים.

## סקירה כללית של המאגר

פרוטוקול הקשר מודל (MCP) הוא מסגרת סטנדרטית לאינטראקציות בין מודלים של AI לבין יישומי לקוח. MCP נוצר במקור על ידי Anthropic וכיום מתוחזק על ידי קהילת MCP הרחבה דרך הארגון הרשמי ב-GitHub. מאגר זה מספק תכנית לימודים מקיפה עם דוגמאות קוד מעשיות ב-C#, Java, JavaScript, Python ו-TypeScript, המיועדות למפתחי AI, אדריכלי מערכות ומהנדסי תוכנה.

## מפת תכנית לימודים חזותית

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```

## מבנה המאגר

המאגר מאורגן ל-11 חלקים עיקריים, כל אחד מתמקד בהיבט שונה של MCP:

1. **מבוא (00-Introduction/)**
   - סקירה כללית של פרוטוקול הקשר מודל
   - מדוע סטנדרטיזציה חשובה בצינורות AI
   - מקרי שימוש מעשיים ויתרונות

2. **מושגים מרכזיים (01-CoreConcepts/)**
   - ארכיטקטורת לקוח-שרת
   - רכיבי פרוטוקול מרכזיים
   - דפוסי מסרים ב-MCP

3. **אבטחה (02-Security/)**
   - איומי אבטחה במערכות מבוססות MCP
   - שיטות מומלצות לאבטחת יישומים
   - אסטרטגיות אימות והרשאה
   - **תיעוד אבטחה מקיף**:
     - שיטות אבטחה מומלצות ל-MCP 2025
     - מדריך יישום אבטחת תוכן של Azure
     - בקרות וטכניקות אבטחה של MCP
     - מדריך מהיר לשיטות אבטחה מומלצות
   - **נושאי אבטחה מרכזיים**:
     - התקפות הזרקת הנחיות והרעלת כלים
     - חטיפת סשן ובעיות "סגן מבולבל"
     - חולשות העברת אסימונים
     - הרשאות יתר ובקרת גישה
     - אבטחת שרשרת אספקה עבור רכיבי AI
     - שילוב Microsoft Prompt Shields

4. **התחלה (03-GettingStarted/)**
   - הגדרת סביבה וקונפיגורציה
   - יצירת שרתי ולקוחות MCP בסיסיים
   - שילוב עם יישומים קיימים
   - כולל חלקים עבור:
     - יישום שרת ראשון
     - פיתוח לקוח
     - שילוב לקוח LLM
     - שילוב VS Code
     - שרת Server-Sent Events (SSE)
     - שימוש מתקדם בשרת
     - סטרימינג HTTP
     - שילוב AI Toolkit
     - אסטרטגיות בדיקה
     - הנחיות לפריסה

5. **יישום מעשי (04-PracticalImplementation/)**
   - שימוש ב-SDKs בשפות תכנות שונות
   - טכניקות דיבוג, בדיקה ואימות
   - יצירת תבניות הנחיה ותהליכי עבודה לשימוש חוזר
   - פרויקטים לדוגמה עם דוגמאות יישום

6. **נושאים מתקדמים (05-AdvancedTopics/)**
   - טכניקות הנדסת הקשר
   - שילוב סוכני Foundry
   - תהליכי עבודה AI רב-מודליים
   - הדגמות אימות OAuth2
   - יכולות חיפוש בזמן אמת
   - סטרימינג בזמן אמת
   - יישום הקשרים שורשיים
   - אסטרטגיות ניתוב
   - טכניקות דגימה
   - גישות סקיילינג
   - שיקולי אבטחה
   - שילוב אבטחת Entra ID
   - שילוב חיפוש באינטרנט

7. **תרומות קהילה (06-CommunityContributions/)**
   - כיצד לתרום קוד ותיעוד
   - שיתוף פעולה דרך GitHub
   - שיפורים ומשוב מונעי קהילה
   - שימוש בלקוחות MCP שונים (Claude Desktop, Cline, VSCode)
   - עבודה עם שרתי MCP פופולריים כולל יצירת תמונות

8. **לקחים מאימוץ מוקדם (07-LessonsfromEarlyAdoption/)**
   - יישומים בעולם האמיתי וסיפורי הצלחה
   - בנייה ופריסה של פתרונות מבוססי MCP
   - מגמות ומפת דרכים עתידית
   - **מדריך שרתי MCP של Microsoft**: מדריך מקיף ל-10 שרתי MCP מוכנים לייצור של Microsoft כולל:
     - שרת MCP של Microsoft Learn Docs
     - שרת MCP של Azure (15+ מחברים מתמחים)
     - שרת MCP של GitHub
     - שרת MCP של Azure DevOps
     - שרת MCP של MarkItDown
     - שרת MCP של SQL Server
     - שרת MCP של Playwright
     - שרת MCP של Dev Box
     - שרת MCP של Azure AI Foundry
     - שרת MCP של Microsoft 365 Agents Toolkit

9. **שיטות מומלצות (08-BestPractices/)**
   - כוונון ביצועים ואופטימיזציה
   - תכנון מערכות MCP עמידות לתקלות
   - אסטרטגיות בדיקה ועמידות

10. **מחקרי מקרה (09-CaseStudy/)**
    - **שבעה מחקרי מקרה מקיפים** המדגימים את גמישות MCP בתרחישים מגוונים:
    - **סוכני נסיעות AI של Azure**: תזמור רב-סוכנים עם Azure OpenAI וחיפוש AI
    - **שילוב Azure DevOps**: אוטומציה של תהליכי עבודה עם עדכוני נתוני YouTube
    - **שליפת תיעוד בזמן אמת**: לקוח קונסול Python עם סטרימינג HTTP
    - **מחולל תכנית לימוד אינטראקטיבי**: אפליקציית Chainlit עם AI שיחתי
    - **תיעוד בתוך העורך**: שילוב VS Code עם תהליכי עבודה של GitHub Copilot
    - **ניהול API של Azure**: שילוב API ארגוני עם יצירת שרת MCP
    - **רישום MCP של GitHub**: פיתוח אקוסיסטם ופלטפורמת שילוב סוכנים
    - דוגמאות יישום הכוללות שילוב ארגוני, פרודוקטיביות מפתחים ופיתוח אקוסיסטם

11. **סדנה מעשית (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - סדנה מעשית מקיפה המשלבת MCP עם AI Toolkit
    - בניית יישומים חכמים המגשרים בין מודלי AI לכלים בעולם האמיתי
    - מודולים מעשיים המכסים יסודות, פיתוח שרת מותאם אישית ואסטרטגיות פריסה לייצור
    - **מבנה מעבדה**:
      - מעבדה 1: יסודות שרת MCP
      - מעבדה 2: פיתוח שרת MCP מתקדם
      - מעבדה 3: שילוב AI Toolkit
      - מעבדה 4: פריסה לייצור וסקיילינג
    - גישת לימוד מבוססת מעבדה עם הוראות שלב-אחר-שלב

12. **מעבדות שילוב מסדי נתונים של שרת MCP (11-MCPServerHandsOnLabs/)**
    - **מסלול לימוד מקיף של 13 מעבדות** לבניית שרתי MCP מוכנים לייצור עם שילוב PostgreSQL
    - **יישום ניתוח קמעונאות בעולם האמיתי** באמצעות מקרה השימוש של Zava Retail
    - **דפוסים ברמת ארגון** כולל אבטחת רמות שורה (RLS), חיפוש סמנטי וגישה לנתונים רב-דיירים
    - **מבנה מעבדה מלא**:
      - **מעבדות 00-03: יסודות** - מבוא, ארכיטקטורה, אבטחה, הגדרת סביבה
      - **מעבדות 04-06: בניית שרת MCP** - עיצוב מסד נתונים, יישום שרת MCP, פיתוח כלים
      - **מעבדות 07-09: תכונות מתקדמות** - חיפוש סמנטי, בדיקה ודיבוג, שילוב VS Code
      - **מעבדות 10-12: ייצור ושיטות מומלצות** - פריסה, ניטור, אופטימיזציה
    - **טכנולוגיות מכוסות**: מסגרת FastMCP, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **תוצאות לימוד**: שרתי MCP מוכנים לייצור, דפוסי שילוב מסדי נתונים, ניתוחים מבוססי AI, אבטחה ארגונית

## משאבים נוספים

המאגר כולל משאבים תומכים:

- **תיקיית תמונות**: מכילה דיאגרמות ואיורים המשמשים לאורך תכנית הלימודים
- **תרגומים**: תמיכה רב-שפתית עם תרגומים אוטומטיים של תיעוד
- **משאבים רשמיים של MCP**:
  - [תיעוד MCP](https://modelcontextprotocol.io/)
  - [מפרט MCP](https://spec.modelcontextprotocol.io/)
  - [מאגר GitHub של MCP](https://github.com/modelcontextprotocol)

## כיצד להשתמש במאגר זה

1. **לימוד רציף**: עקבו אחר הפרקים לפי הסדר (00 עד 11) לחוויית לימוד מובנית.
2. **מיקוד לפי שפה**: אם אתם מעוניינים בשפת תכנות מסוימת, חקרו את תיקיות הדוגמאות עבור יישומים בשפה המועדפת עליכם.
3. **יישום מעשי**: התחילו עם החלק "התחלה" כדי להגדיר את הסביבה שלכם וליצור את שרת ולקוח MCP הראשונים שלכם.
4. **חקירה מתקדמת**: לאחר שתהיו נוחים עם היסודות, צללו לנושאים המתקדמים להרחבת הידע שלכם.
5. **מעורבות קהילתית**: הצטרפו לקהילת MCP דרך דיונים ב-GitHub וערוצי Discord כדי להתחבר למומחים ולמפתחים אחרים.

## לקוחות וכלי MCP

תכנית הלימודים מכסה מגוון לקוחות וכלי MCP:

1. **לקוחות רשמיים**:
   - Visual Studio Code 
   - MCP ב-Visual Studio Code
   - Claude Desktop
   - Claude ב-VSCode 
   - Claude API

2. **לקוחות קהילתיים**:
   - Cline (מבוסס טרמינל)
   - Cursor (עורך קוד)
   - ChatMCP
   - Windsurf

3. **כלי ניהול MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## שרתי MCP פופולריים

המאגר מציג מגוון שרתי MCP, כולל:

1. **שרתי MCP רשמיים של Microsoft**:
   - שרת MCP של Microsoft Learn Docs
   - שרת MCP של Azure (15+ מחברים מתמחים)
   - שרת MCP של GitHub
   - שרת MCP של Azure DevOps
   - שרת MCP של MarkItDown
   - שרת MCP של SQL Server
   - שרת MCP של Playwright
   - שרת MCP של Dev Box
   - שרת MCP של Azure AI Foundry
   - שרת MCP של Microsoft 365 Agents Toolkit

2. **שרתי ייחוס רשמיים**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **יצירת תמונות**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **כלי פיתוח**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **שרתי מתמחים**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## תרומה

מאגר זה מקבל בברכה תרומות מהקהילה. ראו את החלק תרומות קהילה להנחיות כיצד לתרום בצורה יעילה לאקוסיסטם MCP.

----

*מדריך לימוד זה עודכן ב-6 באוקטובר 2025 ומספק סקירה כללית של המאגר נכון לתאריך זה. תוכן המאגר עשוי להתעדכן לאחר תאריך זה.*

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.