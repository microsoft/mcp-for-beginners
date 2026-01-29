# שיטות אבטחה מומלצות ל-MCP - עדכון דצמבר 2025

> **חשוב**: מסמך זה משקף את דרישות האבטחה העדכניות ביותר של [מפרט MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) ואת [שיטות האבטחה המומלצות הרשמיות של MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). יש תמיד להתייחס למפרט הנוכחי לקבלת ההנחיות המעודכנות ביותר.

## שיטות אבטחה חיוניות ליישומי MCP

פרוטוקול הקשר למודל מציג אתגרים ייחודיים באבטחה החורגים מאבטחת תוכנה מסורתית. שיטות אלו מתייחסות הן לדרישות אבטחה בסיסיות והן לאיומים ספציפיים ל-MCP כולל הזרקת פקודות, הרעלת כלים, חטיפת מושבים, בעיות של סגן מבלבל ופגיעויות בהעברת אסימונים.

### **דרישות אבטחה מחייבות**

**דרישות קריטיות ממפרט MCP:**

### **דרישות אבטחה מחייבות**

**דרישות קריטיות ממפרט MCP:**

> **אסור**: שרתי MCP **אסור** לקבל כל אסימון שלא הונפק במפורש עבור שרת ה-MCP  
>  
> **חובה**: שרתי MCP המיישמים הרשאה **חובה** לאמת את כל הבקשות הנכנסות  
>  
> **אסור**: שרתי MCP **אסור** להשתמש במושבים לאימות  
>  
> **חובה**: שרתי פרוקסי MCP המשתמשים במזהי לקוח סטטיים **חובה** לקבל הסכמת משתמש עבור כל לקוח שנרשם דינמית

---

## 1. **אבטחת אסימון ואימות**

**בקרות אימות והרשאה:**  
   - **סקירת הרשאות קפדנית**: עריכת ביקורות מקיפות על לוגיקת ההרשאה של שרת MCP כדי להבטיח שרק משתמשים ולקוחות מיועדים יוכלו לגשת למשאבים  
   - **שילוב ספקי זהות חיצוניים**: שימוש בספקי זהות מבוססים כמו Microsoft Entra ID במקום יישום אימות מותאם אישית  
   - **אימות קהל היעד של האסימון**: תמיד לאמת שהאסימונים הונפקו במפורש עבור שרת ה-MCP שלך - לעולם לא לקבל אסימונים ממקורות עליונים  
   - **מחזור חיים תקין של אסימון**: יישום סיבוב אסימונים מאובטח, מדיניות תפוגה ומניעת התקפות השמעת אסימונים

**אחסון אסימונים מוגן:**  
   - שימוש ב-Azure Key Vault או מאגרי אישורים מאובטחים דומים לכל הסודות  
   - יישום הצפנה לאסימונים במנוחה ובמעבר  
   - סיבוב סדיר של אישורים ומעקב אחר גישה לא מורשית

## 2. **ניהול מושבים ואבטחת תעבורה**

**שיטות מושב מאובטחות:**  
   - **מזהי מושב קריפטוגרפיים מאובטחים**: שימוש במזהי מושב מאובטחים, לא דטרמיניסטיים, שנוצרו עם מחוללי מספרים אקראיים מאובטחים  
   - **קישור ספציפי למשתמש**: קישור מזהי מושב לזהויות משתמש באמצעות פורמטים כמו `<user_id>:<session_id>` למניעת שימוש לרעה במושבים בין משתמשים  
   - **ניהול מחזור חיים של מושב**: יישום תפוגה, סיבוב וביטול תקינים להגבלת חלונות פגיעות  
   - **אכיפת HTTPS/TLS**: HTTPS חובה לכל התקשורת למניעת יירוט מזהי מושב

**אבטחת שכבת תעבורה:**  
   - קונפיגורציית TLS 1.3 היכן שניתן עם ניהול תעודות תקין  
   - יישום נעילת תעודה לחיבורים קריטיים  
   - סיבוב תעודות סדיר ואימות תוקף

## 3. **הגנה מפני איומי AI ספציפיים** 🤖

**הגנה מפני הזרקת פקודות:**  
   - **Microsoft Prompt Shields**: פריסת מגן פקודות AI לזיהוי וסינון מתקדם של הוראות זדוניות  
   - **ניקוי קלט**: אימות וניקוי כל הקלטים למניעת התקפות הזרקה ובעיות סגן מבלבל  
   - **גבולות תוכן**: שימוש במערכות מפרידות וסימון נתונים להבחנה בין הוראות מהימנות לתוכן חיצוני

**מניעת הרעלת כלים:**  
   - **אימות מטא-נתוני כלים**: יישום בדיקות שלמות להגדרות כלים ומעקב אחר שינויים בלתי צפויים  
   - **מעקב דינמי אחר כלים**: ניטור התנהגות בזמן ריצה והקמת התראות על דפוסי ביצוע בלתי צפויים  
   - **זרימות עבודה לאישור**: דרישת אישור מפורש של משתמש לשינויים בכלים ולשינויים ביכולות

## 4. **בקרת גישה והרשאות**

**עקרון ההרשאה המינימלית:**  
   - הענקת שרתי MCP רק את ההרשאות המינימליות הנדרשות לתפקוד המיועד  
   - יישום בקרת גישה מבוססת תפקידים (RBAC) עם הרשאות מדויקות  
   - סקירות הרשאות סדירות ומעקב רציף אחר הסלמת הרשאות

**בקרות הרשאה בזמן ריצה:**  
   - הטלת מגבלות משאבים למניעת התקפות התשה  
   - שימוש בבידוד מכולות לסביבות ביצוע כלים  
   - יישום גישה בזמן אמת לפונקציות ניהוליות

## 5. **בטיחות תוכן ומעקב**

**יישום בטיחות תוכן:**  
   - **שילוב Azure Content Safety**: שימוש ב-Azure Content Safety לזיהוי תוכן מזיק, ניסיונות פריצה והפרות מדיניות  
   - **ניתוח התנהגותי**: יישום ניטור התנהגות בזמן ריצה לזיהוי חריגות בשרת MCP ובביצוע כלים  
   - **רישום מקיף**: רישום כל ניסיונות האימות, קריאות כלים ואירועי אבטחה עם אחסון מאובטח ועמיד לזיופים

**מעקב רציף:**  
   - התראות בזמן אמת על דפוסים חשודים וניסיונות גישה לא מורשים  
   - שילוב עם מערכות SIEM לניהול מרכזי של אירועי אבטחה  
   - ביקורות אבטחה סדירות ובדיקות חדירה של יישומי MCP

## 6. **אבטחת שרשרת אספקה**

**אימות רכיבים:**  
   - **סריקת תלותיות**: שימוש בסריקות פגיעות אוטומטיות לכל התלויות בתוכנה וברכיבי AI  
   - **אימות מקור**: אימות מקור, רישוי ושלמות של מודלים, מקורות נתונים ושירותים חיצוניים  
   - **חבילות חתומות**: שימוש בחבילות חתומות קריפטוגרפית ואימות חתימות לפני פריסה

**צינור פיתוח מאובטח:**  
   - **GitHub Advanced Security**: יישום סריקת סודות, ניתוח תלותיות וניתוח סטטי CodeQL  
   - **אבטחת CI/CD**: שילוב אימות אבטחה לאורך כל צינורות הפריסה האוטומטיים  
   - **שלמות ארטיפקטים**: יישום אימות קריפטוגרפי לארטיפקטים וקונפיגורציות בפריסה

## 7. **אבטחת OAuth ומניעת סגן מבלבל**

**יישום OAuth 2.1:**  
   - **יישום PKCE**: שימוש ב-Proof Key for Code Exchange (PKCE) לכל בקשות ההרשאה  
   - **הסכמה מפורשת**: קבלת הסכמת משתמש עבור כל לקוח שנרשם דינמית למניעת התקפות סגן מבלבל  
   - **אימות URI הפניה מחדש**: יישום אימות מחמיר של URI הפניה מחדש ומזהי לקוח

**אבטחת פרוקסי:**  
   - מניעת עקיפת הרשאה באמצעות ניצול מזהי לקוח סטטיים  
   - יישום זרימות עבודה לאישור גישה ל-API של צד שלישי  
   - מעקב אחר גניבת קוד הרשאה וניסיונות גישה לא מורשים ל-API

## 8. **תגובה לאירועים ושחזור**

**יכולות תגובה מהירה:**  
   - **תגובה אוטומטית**: יישום מערכות אוטומטיות לסיבוב אישורים ולכידת איומים  
   - **נהלי שחזור**: יכולת להחזיר במהירות קונפיגורציות ורכיבים ידועים וטובים  
   - **יכולות פורנזיות**: מסלולי ביקורת מפורטים ורישום לחקירת אירועים

**תקשורת ותיאום:**  
   - נהלי הסלמה ברורים לאירועי אבטחה  
   - שילוב עם צוותי תגובה לאירועים בארגון  
   - סימולציות אירועי אבטחה ותרגילי שולחן סדירים

## 9. **ציות וממשל**

**ציות לרגולציה:**  
   - הבטחת יישומי MCP עומדים בדרישות ספציפיות לתעשייה (GDPR, HIPAA, SOC 2)  
   - יישום סיווג נתונים ובקרות פרטיות לעיבוד נתוני AI  
   - שמירת תיעוד מקיף לביקורת ציות

**ניהול שינויים:**  
   - תהליכי סקירת אבטחה פורמליים לכל שינויים במערכת MCP  
   - בקרת גרסאות וזרימות עבודה לאישור שינויים בקונפיגורציה  
   - הערכות ציות סדירות וניתוח פערים

## 10. **בקרות אבטחה מתקדמות**

**ארכיטקטורת Zero Trust:**  
   - **לעולם לא לסמוך, תמיד לאמת**: אימות רציף של משתמשים, מכשירים וחיבורים  
   - **מיקרו-סגמנטציה**: בקרות רשת מדויקות המבודדות רכיבי MCP בודדים  
   - **גישה מותנית**: בקרות גישה מבוססות סיכון המותאמות להקשר ולהתנהגות נוכחית

**הגנה בזמן ריצה על יישומים:**  
   - **הגנה עצמית על יישומים בזמן ריצה (RASP)**: פריסת טכניקות RASP לזיהוי איומים בזמן אמת  
   - **ניטור ביצועי יישומים**: מעקב אחר חריגות ביצועים שעשויות להעיד על התקפות  
   - **מדיניות אבטחה דינמית**: יישום מדיניות אבטחה המתאימה עצמה בהתאם לנוף האיומים הנוכחי

## 11. **שילוב אקוסיסטם האבטחה של מיקרוסופט**

**אבטחה מקיפה של מיקרוסופט:**  
   - **Microsoft Defender for Cloud**: ניהול מצב אבטחה בענן לעומסי עבודה של MCP  
   - **Azure Sentinel**: יכולות SIEM ו-SOAR ילידיות לענן לזיהוי איומים מתקדם  
   - **Microsoft Purview**: ממשל וציות לנתונים עבור זרימות עבודה ונתוני AI

**ניהול זהות וגישה:**  
   - **Microsoft Entra ID**: ניהול זהויות ארגוני עם מדיניות גישה מותנית  
   - **Privileged Identity Management (PIM)**: גישה בזמן אמת וזרימות עבודה לאישור פונקציות ניהוליות  
   - **הגנת זהות**: גישה מותנית מבוססת סיכון ותגובה אוטומטית לאיומים

## 12. **התפתחות אבטחה מתמשכת**

**שמירה על עדכניות:**  
   - **מעקב מפרט**: סקירה סדירה של עדכוני מפרט MCP ושינויים בהנחיות אבטחה  
   - **מודיעין איומים**: שילוב פידים ספציפיים ל-AI וסימני פגיעה  
   - **מעורבות קהילתית באבטחה**: השתתפות פעילה בקהילת אבטחת MCP ותוכניות גילוי פגיעויות

**אבטחה אדפטיבית:**  
   - **אבטחת למידת מכונה**: שימוש בגילוי חריגות מבוסס ML לזיהוי דפוסי התקפה חדשים  
   - **אנליטיקה חיזויית לאבטחה**: יישום מודלים חיזוייתיים לזיהוי איומים פרואקטיבי  
   - **אוטומציה באבטחה**: עדכוני מדיניות אבטחה אוטומטיים המבוססים על מודיעין איומים ושינויים במפרט

---

## **משאבי אבטחה קריטיים**

### **תיעוד רשמי של MCP**
- [מפרט MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [שיטות אבטחה מומלצות ל-MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [מפרט הרשאות MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **פתרונות אבטחה של מיקרוסופט**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [אבטחת Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **תקני אבטחה**
- [שיטות אבטחה מומלצות ל-OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP עשרת הגדולים למודלים שפתיים גדולים](https://genai.owasp.org/)
- [מסגרת ניהול סיכוני AI של NIST](https://www.nist.gov/itl/ai-risk-management-framework)

### **מדריכי יישום**
- [שער אימות MCP לניהול API של Azure](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID עם שרתי MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **הודעת אבטחה**: שיטות האבטחה של MCP מתפתחות במהירות. יש תמיד לאמת מול [מפרט MCP הנוכחי](https://spec.modelcontextprotocol.io/) ו[תיעוד האבטחה הרשמי](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) לפני היישום.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->