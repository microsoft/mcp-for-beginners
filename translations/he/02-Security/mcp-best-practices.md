# MCP Security Best Practices 2025

מדריך מקיף זה מפרט את שיטות העבודה המומלצות החיוניות לאבטחה ליישום מערכות פרוטוקול הקשר למודל (MCP) בהתבסס על מפרט **MCP Specification 2025-11-25** העדכני ביותר ותקני התעשייה הנוכחיים. שיטות אלו מתייחסות הן לחששות אבטחה מסורתיים והן לאיומים ספציפיים לבינה מלאכותית הייחודיים לפריסות MCP.

## דרישות אבטחה קריטיות

### בקרות אבטחה חובה (דרישות MUST)

1. **אימות אסימון**: שרתי MCP **אסור שיקבלו** אסימונים שלא הונפקו במפורש עבור שרת ה-MCP עצמו  
2. **אימות הרשאה**: שרתי MCP המיישמים הרשאה **חייבים** לאמת את כל הבקשות הנכנסות ו**אסור להשתמש** במפגשים לאימות  
3. **הסכמת משתמש**: שרתי פרוקסי MCP המשתמשים במזהי לקוח סטטיים **חייבים** לקבל הסכמה מפורשת מהמשתמש עבור כל לקוח שנרשם דינמית  
4. **מזהי מפגש מאובטחים**: שרתי MCP **חייבים** להשתמש במזהי מפגש קריפטוגרפיים מאובטחים, לא דטרמיניסטיים, שנוצרו באמצעות מחוללי מספרים אקראיים מאובטחים

## שיטות אבטחה מרכזיות

### 1. אימות וקיזוז קלט  
- **אימות קלט מקיף**: אמת וקזז את כל הקלטים כדי למנוע התקפות הזרקה, בעיות confused deputy ופגיעויות הזרקת פרומפט  
- **אכיפת סכמת פרמטרים**: יישם אימות סכמת JSON מחמיר לכל פרמטרי הכלים וקלטי ה-API  
- **סינון תוכן**: השתמש ב-Microsoft Prompt Shields וב-Azure Content Safety לסינון תוכן זדוני בפרומפטים ובתגובות  
- **קיזוז פלט**: אמת וקזז את כל הפלטים של המודל לפני הצגתם למשתמשים או למערכות משניות

### 2. מצוינות באימות והרשאה  
- **ספקי זהות חיצוניים**: הפקד את האימות על ספקי זהות מבוססים (Microsoft Entra ID, ספקי OAuth 2.1) במקום ליישם אימות מותאם אישית  
- **הרשאות מדויקות**: יישם הרשאות גרנולריות ספציפיות לכלי בהתאם לעקרון ההרשאה המינימלית  
- **ניהול מחזור חיים של אסימונים**: השתמש באסימוני גישה קצרים עם סיבוב מאובטח ואימות קהל נכון  
- **אימות רב-שלבי**: דרוש אימות MFA לכל גישה מנהלית ולפעולות רגישות

### 3. פרוטוקולי תקשורת מאובטחים  
- **אבטחת שכבת תחבורה**: השתמש ב-HTTPS/TLS 1.3 לכל התקשורת של MCP עם אימות תעודה תקין  
- **הצפנה מקצה לקצה**: יישם שכבות הצפנה נוספות לנתונים רגישים מאוד במעבר ובמנוחה  
- **ניהול תעודות**: שמור על ניהול מחזור חיים תקין של תעודות עם תהליכי חידוש אוטומטיים  
- **אכיפת גרסת פרוטוקול**: השתמש בגרסת פרוטוקול MCP הנוכחית (2025-11-25) עם ניהול גרסאות תקין

### 4. הגבלת קצב מתקדמת והגנת משאבים  
- **הגבלת קצב רב-שכבתית**: יישם הגבלת קצב ברמת משתמש, מפגש, כלי ומשאב כדי למנוע שימוש לרעה  
- **הגבלת קצב אדפטיבית**: השתמש בהגבלת קצב מבוססת למידת מכונה המסתגלת לדפוסי שימוש ואינדיקטורים של איומים  
- **ניהול מכסת משאבים**: קבע מגבלות מתאימות למשאבי חישוב, שימוש בזיכרון וזמן ביצוע  
- **הגנת DDoS**: פרוס מערכות הגנת DDoS וניתוח תעבורה מקיפים

### 5. רישום ומעקב מקיפים  
- **רישום ביקורת מובנה**: יישם לוגים מפורטים, ניתנים לחיפוש לכל פעולות MCP, ביצועי כלים ואירועי אבטחה  
- **מעקב אבטחה בזמן אמת**: פרוס מערכות SIEM עם זיהוי חריגות מבוסס בינה מלאכותית לעומסי עבודה של MCP  
- **רישום תואם פרטיות**: רישום אירועי אבטחה תוך שמירה על דרישות ותקנות פרטיות  
- **אינטגרציה לתגובה לאירועים**: חבר מערכות רישום לזרימות עבודה אוטומטיות של תגובה לאירועים

### 6. שיטות אחסון מאובטחות משופרות  
- **מודולי אבטחת חומרה**: השתמש באחסון מפתחות מגובה HSM (Azure Key Vault, AWS CloudHSM) לפעולות קריפטוגרפיות קריטיות  
- **ניהול מפתחות הצפנה**: יישם סיבוב מפתחות, הפרדה ובקרות גישה מתאימות למפתחות הצפנה  
- **ניהול סודות**: אחסן את כל מפתחות ה-API, האסימונים והאישורים במערכות ניהול סודות ייעודיות  
- **סיווג נתונים**: סווג נתונים על פי רמות רגישות ויישם אמצעי הגנה מתאימים

### 7. ניהול אסימונים מתקדם  
- **מניעת העברת אסימונים**: אסור במפורש דפוסי העברת אסימונים העוברים על בקרות אבטחה  
- **אימות קהל**: אמת תמיד שטענות הקהל של האסימון תואמות לזהות שרת ה-MCP המיועד  
- **הרשאה מבוססת טענות**: יישם הרשאה גרנולרית מבוססת טענות אסימון ותכונות משתמש  
- **קישור אסימונים**: קשר אסימונים למפגשים, משתמשים או מכשירים ספציפיים במידת הצורך

### 8. ניהול מפגשים מאובטח  
- **מזהי מפגש קריפטוגרפיים**: צור מזהי מפגש באמצעות מחוללי מספרים אקראיים קריפטוגרפיים (לא רצפים ניתנים לחיזוי)  
- **קישור למשתמש ספציפי**: קשר מזהי מפגש למידע ספציפי למשתמש באמצעות פורמטים מאובטחים כמו `<user_id>:<session_id>`  
- **בקרות מחזור חיים של מפגש**: יישם תהליכי תפוגה, סיבוב וביטול מפגשים תקינים  
- **כותרות אבטחה למפגש**: השתמש בכותרות אבטחה HTTP מתאימות להגנת מפגש

### 9. בקרות אבטחה ספציפיות לבינה מלאכותית  
- **הגנה מפני הזרקת פרומפט**: פרוס Microsoft Prompt Shields עם הדגשה, מפרידים וטכניקות סימון נתונים  
- **מניעת הרעלת כלים**: אמת מטא-נתוני כלים, פקח על שינויים דינמיים ואמת שלמות הכלי  
- **אימות פלט מודל**: סרוק פלטי מודל לזיהוי דליפת נתונים, תוכן מזיק או הפרות מדיניות אבטחה  
- **הגנת חלון הקשר**: יישם בקרות למניעת הרעלת חלון הקשר והתקפות מניפולציה

### 10. אבטחת ביצוע כלים  
- **הרצת כלים בסביבה מבודדת**: הרץ ביצועי כלים בסביבות מכולה מבודדות עם מגבלות משאבים  
- **הפרדת הרשאות**: הפעל כלים עם ההרשאות המינימליות הנדרשות וחשבונות שירות נפרדים  
- **בידוד רשת**: יישם סגמנטציה של רשת לסביבות ביצוע כלים  
- **מעקב ביצוע**: פקח על ביצוע כלים לזיהוי התנהגות חריגה, שימוש במשאבים והפרות אבטחה

### 11. אימות אבטחה מתמשך  
- **בדיקות אבטחה אוטומטיות**: שלב בדיקות אבטחה בצינורות CI/CD עם כלים כמו GitHub Advanced Security  
- **ניהול פגיעויות**: סרוק באופן קבוע את כל התלויות, כולל מודלים חכמים ושירותים חיצוניים  
- **בדיקות חדירה**: ערוך הערכות אבטחה סדירות הממוקדות במיוחד ביישומי MCP  
- **סקירות קוד אבטחה**: יישם סקירות אבטחה חובה לכל שינויים בקוד הקשורים ל-MCP

### 12. אבטחת שרשרת אספקה לבינה מלאכותית  
- **אימות רכיבים**: אמת מקור, שלמות ואבטחה של כל רכיבי הבינה המלאכותית (מודלים, אמבדינגים, APIs)  
- **ניהול תלות**: שמור מלאי עדכני של כל התוכנות והתלויות בבינה מלאכותית עם מעקב אחר פגיעויות  
- **מאגרי אמון**: השתמש במקורות מאומתים ואמינים לכל המודלים, הספריות והכלים  
- **מעקב שרשרת אספקה**: פקח באופן רציף על פגיעות בספקי שירותי בינה מלאכותית ובמאגרי מודלים

## דפוסי אבטחה מתקדמים

### ארכיטקטורת Zero Trust ל-MCP  
- **לעולם אל תסמוך, תמיד אמת**: יישם אימות מתמשך לכל משתתפי MCP  
- **מיקרו-סגמנטציה**: בידוד רכיבי MCP עם בקרות רשת וזהות גרנולריות  
- **גישה מותנית**: יישם בקרות גישה מבוססות סיכון המסתגלות להקשר ולהתנהגות  
- **הערכת סיכון מתמשכת**: הערך דינמית את מצב האבטחה בהתבסס על אינדיקטורים של איומים נוכחיים

### יישום בינה מלאכותית השומר על פרטיות  
- **מזעור נתונים**: חשוף רק את הנתונים המינימליים הנדרשים לכל פעולה ב-MCP  
- **פרטיות דיפרנציאלית**: יישם טכניקות שמירת פרטיות לעיבוד נתונים רגישים  
- **הצפנה הומומורפית**: השתמש בטכניקות הצפנה מתקדמות לחישוב מאובטח על נתונים מוצפנים  
- **למידה פדרטיבית**: יישם גישות למידה מבוזרת השומרות על מקומיות ופרטיות הנתונים

### תגובה לאירועים במערכות בינה מלאכותית  
- **נהלי תגובה ספציפיים לבינה מלאכותית**: פתח נהלי תגובה לאירועים המותאמים לאיומים ספציפיים ל-AI ו-MCP  
- **תגובה אוטומטית**: יישם כליאה ותיקון אוטומטיים לאירועי אבטחה נפוצים בבינה מלאכותית  
- **יכולות פורנזיות**: שמור על מוכנות פורנזית לפגיעות במערכות AI ודליפות נתונים  
- **נהלי שיקום**: הקם נהלים לשיקום מהרעלת מודלים, התקפות הזרקת פרומפט ופגיעות בשירותים

## משאבים ותקנים ליישום

### תיעוד רשמי של MCP  
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - מפרט פרוטוקול MCP נוכחי  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - הנחיות אבטחה רשמיות  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - דפוסי אימות והרשאה  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - דרישות אבטחת שכבת תחבורה

### פתרונות אבטחה של מיקרוסופט  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - הגנה מתקדמת מפני הזרקת פרומפט  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - סינון תוכן AI מקיף  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - ניהול זהות וגישה ארגוני  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - ניהול סודות ואישורים מאובטח  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - סריקת אבטחה לשרשרת אספקה וקוד

### תקני אבטחה ומסגרות עבודה  
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - הנחיות אבטחה עדכניות ל-OAuth  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - סיכוני אבטחה באפליקציות ווב  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - סיכוני אבטחה ספציפיים ל-AI  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - ניהול סיכוני AI מקיף  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - מערכות ניהול אבטחת מידע

### מדריכים והדרכות ליישום  
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - דפוסי אימות ארגוניים  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - אינטגרציית ספק זהות  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - שיטות ניהול אסימונים מומלצות  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - דפוסי הצפנה מתקדמים

### משאבי אבטחה מתקדמים  
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - שיטות פיתוח מאובטחות  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - בדיקות אבטחה ספציפיות ל-AI  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - מתודולוגיית מודל איומים ל-AI  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - טכניקות שמירת פרטיות ב-AI

### תאימות וממשל  
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - תאימות פרטיות במערכות AI  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - יישום AI אחראי  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - בקרות אבטחה לספקי שירותי AI  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - דרישות תאימות AI בתחום הבריאות

### DevSecOps ואוטומציה  
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - צינורות פיתוח AI מאובטחים  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - אימות אבטחה מתמשך  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - פריסת תשתיות מאובטחת  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - אבטחת מכולות לעומסי עבודה של AI

### ניטור ותגובה לאירועים  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - פתרונות ניטור מקיפים  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - נהלי תגובה לאירועים ספציפיים ל-AI  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - ניהול מידע ואירועים אבטחתיים  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - מקורות מודיעין איומים ל-AI

## 🔄 שיפור מתמשך

### הישאר מעודכן עם תקנים מתפתחים  
- **עדכוני מפרט MCP**: פקח על שינויים רשמיים במפרט MCP והודעות אבטחה  
- **מודיעין איומים**: הירשם להזנות איומי אבטחה לבינה מלאכותית ומאגרי פגיעויות  
- **מעורבות קהילתית**: השתתף בדיונים וקבוצות עבודה בקהילת אבטחת MCP  
- **הערכה סדירה**: ערוך הערכות רבעוניות של מצב האבטחה ועדכן שיטות בהתאם

### תרומה לאבטחת MCP  
- **מחקר אבטחה**: תרום למחקר אבטחת MCP ולתוכניות גילוי פגיעויות  
- **שיתוף שיטות עבודה מומלצות**: שתף יישומי אבטחה ולימודים עם הקהילה
- **פיתוח סטנדרטי**: השתתפות בפיתוח מפרט MCP ויצירת תקני אבטחה  
- **פיתוח כלים**: פיתוח ושיתוף כלים וספריות אבטחה לאקוסיסטם של MCP  

---

*מסמך זה משקף את שיטות העבודה הטובות ביותר לאבטחת MCP נכון ל-18 בדצמבר 2025, בהתבסס על מפרט MCP מ-25 בנובמבר 2025. יש לסקור ולעדכן את שיטות האבטחה באופן קבוע ככל שהפרוטוקול ונוף האיומים מתפתחים.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->