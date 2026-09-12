# בקרות אבטחה של MCP - עדכון ספטמבר 2026

> **התקן הנוכחי:** מסמך זה משקף
> [מפרט MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> ואת 
> [הנחיות האבטחה הטובות ביותר של MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

פרוטוקול הקשר של המודל (MCP) התפתח משמעותית עם בקרות אבטחה משופרות המטפלות באבטחת תוכנה מסורתית ואיומים ספציפיים ל-AI. מסמך זה מספק בקרות אבטחה מקיפות ליישומי MCP מאובטחים התואמים למסגרת OWASP MCP Top 10.

## 🏔️ הדרכת אבטחה מעשית

לניסיון מעשי בביצוע אבטחה, אנו ממליצים על **[סדנת הפסגה לאבטחת MCP (שרפה)](https://azure-samples.github.io/sherpa/)** - מסע הדרכה מקיף לאבטחת שרתי MCP ב-Azure בשיטת "פגיע → ניצול → תיקון → אימות".

כל בקרות האבטחה במסמך זה תואמות את **[מדריך האבטחה של OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)**, המספק ארכיטקטורות התייחסות והנחיות יישום ספציפיות ל-Azure לסיכוני OWASP MCP Top 10.

## **דרישות אבטחה מחייבות**

### **איסורים קריטיים ממפרט MCP:**

> **אסור**: שרתי MCP **אסור שיקבלו** כל אסימוני גישה שלא הונפקו במפורש עבור שרת ה-MCP
>
> **אסור**: שרתי MCP **אסור שישתמשו** במושבים לאימות  
>
> **נדרש**: שרתי MCP שמיישמים הרשאה **חייבים** לאמת את כל הבקשות הנכנסות
>
> **מחייב**: שרתי פרוקסי של MCP המשתמשים במזהה לקוח צד שלישי סטטי
> **חייבים** לקבל הסכמה מכל לקוח MCP לפני העברת ההרשאה

---

## 1. **בקרות אימות והרשאה**

### **אינטגרציה עם ספק זהות חיצוני**

**מפרט MCP `2026-07-28`** מאפשר לשרתי MCP להסמיך
אימות לספקי זהות חיצוניים. ההרשאה עבור תחבורה ב-HTTP
מוערכת לכל בקשה; שרתי stdio מקומיים מקבלים אישורי גישה
מהסביבה שלהם במקום זאת.

**סיכון MCP מטופל ב-OWASP**: [MCP07 - אימות והרשאה לא מספקים](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**יתרונות אבטחה:**
1. **מבטל סיכוני אימות מותאמים אישית**: מצמצם את משטח הפגיעות על ידי הימנעות מיישומי אימות מותאמים
2. **אבטחת ארגונית ברמה גבוהה**: מנצל ספקי זהות מבוססים כמו Microsoft Entra ID עם תכונות אבטחה מתקדמות
3. **ניהול זהויות מרכזי**: מפשט ניהול מחזור חיי משתמש, בקרת גישה וביקורת תאימות
4. **אימות רב-שלבי (MFA)**: יורש יכולות MFA מספקי זהות ארגוניים
5. **מדיניות גישה מותנית**: נהנה מבקרות גישה מבוססות סיכון ואימות אדפטיבי

**דרישות יישום:**
- **רישום לקוח**: העדפה למסמכי מטא-נתוני מזהה לקוח או
  רישום מוקדם; שימוש ברישום דינמי מיושן של לקוח רק עבור
  תאימות
- **אימות קהל יעד של אסימון**: אימות שכל האסימונים הונפקו במפורש עבור שרת MCP
- **אימות מוּנפק**: אימות שהמונפק של האסימון תואם לספק הזהות הצפוי
- **אימות חתימה**: אימות קריפטוגרפי של תקינות האסימון
- **אכיפת תוקף**: אכיפה מחמירה של מגבלות חיי האסימון
- **אימות תחום**: ודא שהאסימונים כוללים הרשאות מתאימות לפעולות המבוקשות

### **אבטחת לוגיקת הרשאה**


**בקרות קריטיות:**
- **ביקורות הרשאה מקיפות**: סקירות אבטחה שוטפות של כל נקודות קבלת ההחלטות בהרשאה
- **ברירות מחדל בטוחות**: דחיית גישה כאשר לוגיקת ההרשאה לא יכולה לקבל החלטה חד־משמעית
- **גבולות הרשאה**: הפרדה ברורה בין רמות הרשאה שונות וגישה למשאבים
- **רישום ביקורת**: תיעוד מלא של כל החלטות ההרשאה למטרות ניטור אבטחה
- **סקירות גישה סדירות**: אימות תקופתי של הרשאות משתמש והקצאות הרשאה

## 2. **אבטחת אסימונים ובקרות נגד העברה בלתי מורשית**

**סיכוני OWASP MCP מטופלים**: [MCP01 - ניהול אסימונים שגוי וחשיפת סודות](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **מניעת העברת אסימונים**

**העברת אסימונים אסורה במפורש** בהספקת הרשאת MCP עקב סיכוני אבטחה קריטיים:

**סיכוני אבטחה מטופלים:**
- **עקיפת בקרות**: מדלג על בקרות אבטחה חיוניות כמו הגבלת תדירות, אימות בקשות וניטור תעבורה
- **שבירת אחריות**: הופך את זיהוי הלקוח לבלתי אפשרי, תוך פגיעה בשבילים ובחקירת אירועים
- **גניבת מידע באמצעות פרוקסי**: מאפשר לכוחות זדוניים להשתמש בשרתים כפרוקסי לגישה בלתי מורשית לנתונים
- **הפרת גבולות אמון**: שוברת הנחות אמון של שירותי היעד לגבי מקור האסימון
- **תנועה רוחבית**: אסימונים מופרים במספר שירותים מאפשרים הרחבת התקפה רחבה יותר

**בקרות יישום:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **דפוסי ניהול אסימונים בטוחים**

**שיטות עבודה מומלצות:**
- **אסימונים קצרים-טווח**: צמצום חלון החשיפה עם סיבוב אסימונים תכוף
- **הנפקה במועד הצורך**: הנפקת אסימונים רק כאשר דרושים לפעולות ספציפיות
- **אחסון מאובטח**: שימוש במודולי אבטחה חומרתיים (HSM) או מטריות מפתחות מאובטחות
- **קשירת אסימונים**: אימות קהל ומנפיק האסימון למשאב MCP הייעודי
  לקוח ופעולה
- **ניטור והתראות**: זיהוי בזמן אמת של שימוש לרעה באסימון או דפוסי גישה בלתי מורשים

## 3. **בקרות אבטחת מצב היישום**

### **מניעת חטיפת מזהי מצב**

**וקטורי התקפה מטופלים:**
- **ניחוש מזהים**: מזהים ניתנים לניבוי שמחשפים מצב של קורא אחר
- **שימוש חוזר בין משתמשים**: מזהה גנוב שנעשה בו שימוש עם זהות שונה
- **הרשאה משתמעת**: החזקת מזהה נתפסת בטעות כהוכחה לגישה


**בקרות על מזהי מצב:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**אבטחת תעבורה:**
- **אכיפת HTTPS**: דרוש HTTPS לתעבורת HTTP מרחוק
- **טיפול באישורים**: שליחה ואימות הרשאה בכל בקשה של HTTP
- **בידוד stdio**: הגנת שרתי stdio מקומיים באמצעות בידוד תהליכים ובקרות אישורים סביבתיות


### **שיקולי מצב מול חסרי מצב**

MCP `2026-07-28` חסר מצב ברמת הפרוטוקול. יישומים עדיין יכולים
לשמור מצב בעזרת החזרת מזהה מפורש משיחה אחת למכונה וקבלה
שלו כארגומנט רגיל בשיחות מאוחרות יותר.

- אחסן מצב בנפרד מכל חיבור תעבורה יחיד.
- קשר מזהי מצב לשרת הראשי המאומת בצד השרת.
- התייחס למזהה כשם, לא כאישור נושא.
- הגדר התנהגות של תפוגה והתאוששות עבור מזהים ישנים.

## 4. **בקרות אבטחה ספציפיות ל-AI**

**סיכוני OWASP MCP מטופלים**:

- [MCP06 - תת-ווריאציה של זרימת הכוונה](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - הרעלת כלי](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - הזרקת פקודות וביצוע](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **הגנה מפני הזרקת פקודות**

**אינטגרציה עם Microsoft Prompt Shields:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**בקרות יישום:**
- **ניקוי קלט**: אימות וסינון מקיף של כל קלטי המשתמש
- **הגדרת גבולות תוכן**: הפרדה ברורה בין הוראות מערכת לתוכן המשתמש
- **ירושה של הוראות**: כללי עדיפות נכונים להוראות מתנגשות
- **ניטור פלט**: זיהוי פלטים פוטנציאלית מזיקים או מנוהלים באופן לא תקין

### **מניעת הרעלת כלים**

**מסגרת ביטחון לכלים:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**ניהול דינמי של כלים:**
- **זרימות עבודה לאישור**: הסכמה מפורשת של המשתמש לשינויים בכלים
- **אפשרויות חזרה לגרסה קודמת**: יכולת לחזור לגרסאות קודמות של כלי
- **ביקורת שינויים**: היסטוריה מלאה של שינויים בהגדרות הכלים
- **הערכת סיכונים**: הערכה אוטומטית של מצב האבטחה של הכלים

## 5. **מניעת התקפת סגן מבולבל**

### **אבטחת Proxy OAuth**

**בקרות מניעת התקפה:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**דרישות יישום:**
- **רישום לקוח**: עדיפות לרישום מוקדם או מסמכי מטא-דאטה של מזהה לקוח
  ; לנהוג ברישום דינמי של לקוח כפיתרון גיבוי תואם
- **אימות הסכמת משתמש**: פרוקסי MCP המשתמשים במזהה לקוח צד שלישי סטטי
  חייבים לקבל הסכמה לכל לקוח לפני העברת ההרשאה
- **אימות URI להפנייה מחדש**: אימות קפדני מבוסס רשימת לבנה של יעדי ההפניה
- **הגנה על קוד ההרשאה**: קודים קצרים עם אכיפת שימוש יחיד
- **אימות זהות לקוח**: אימות תקיף של אישורי לקוח ומטא-דאטה

## 6. **אבטחת ביצוע כלים**

### **סאנדבוקס והפרדה*

**הפרדה מבוססת מכולות:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**הפרדת תהליכים:**
- **הקשרים נפרדים לתהליכים**: כל ביצוע כלי במרחב תהליכים מבודד
- **תקשורת בין-תהליכים**: מנגנוני IPC מאובטחים עם אימות
- **ניטור תהליכים**: ניתוח התנהגות בזמן ריצה וזיהוי חריגות
- **אכיפת משאבים**: הגבלות מחמירות על CPU, זיכרון ופעולות I/O

### **יישום של הרשאות מינימום**

**ניהול הרשאות:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **בקרות אבטחת שרשרת אספקה**

**סיכון OWASP MCP מטופל**: [MCP04 - התקפות על שרשרת אספקה ותמרון תלות](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **אימות תלות**

**אבטחה מקיפה של רכיבים:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **ניטור רציף**

**זיהוי איומים בשרשרת אספקה:**
- **ניטור בריאות התלותים**: הערכה מתמדת של כל התלותים בנושאי אבטחה
- **אינטגרציה של מודיעין איומים**: עדכונים בזמן אמת על איומי שרשרת אספקה מתפתחים
- **ניתוח התנהגות**: זיהוי התנהגות חריגה ברכיבים חיצוניים
- **תגובה אוטומטית**: בידוד מיידי של רכיבים שנפגעו

## 8. **בקרות ניטור וזיהוי**

**סיכון OWASP MCP מטופל**: [MCP08 - חוסר בביקורת וטלאומטריה](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **ניהול מידע ואירועי אבטחה (SIEM)**

**אסטרטגיית רישום מקיפה:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **זיהוי איומים בזמן אמת**

**אנליטיקה התנהגותית:**
- **אנליטיקת התנהגות משתמשים (UBA)**: זיהוי דפוסי גישה חריגים של משתמשים
- **אנליטיקת התנהגות ישויות (EBA)**: ניטור התנהגות שרתי וכלי MCP
- **זיהוי חריגות בלמידת מכונה**: זיהוי איומים מבוסס AI
- **קורלציה של מודיעין איומים**: השוואת פעילויות נצפות נגד דפוסי התקפה ידועים

## 9. **תגובה לאירועים והתאוששות**

### **יכולות תגובה אוטומטית**

**פעולות תגובה מיידיות:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **יכולות פורנזיות**

**תמיכה בחקירה:**
- **שימור רישום ביקורת**: רישום בלתי ניתן לשינוי עם שלמות קריפטוגרפית
- **איסוף ראיות**: איסוף אוטומטי של ארטיפקטים רלוונטיים לאבטחה
- **שחזור רצף אירועים**: רצף מפורט של אירועים שהובילו לאירועי אבטחה
- **הערכת השפעה**: הערכת היקף הפגיעה וחשיפת המידע

## **עקרונות מפתח בארכיטקטורת אבטחה**

### **הגנה בשכבות**
- **מספר שכבות אבטחה**: אין נקודת כשל יחידה בארכיטקטורת האבטחה
- **בקרות כפולות**: אמצעי אבטחה חופפים לתפקודים קריטיים
- **מנגנוני בטיחות בכשל**: ברירות מחדל מאובטחות במפגש עם שגיאות או התקפות

### **יישום אפס אמון**
- **לעולם אל תאמין, תמיד אמת**: אימות מתמשך של כל היישויות והבקשות
- **עיקרון הרשאת מינימום**: זכויות גישה מינימליות לכל הרכיבים
- **מיקרו-סגמנטציה**: בקרות רשת וגישה מדויקות ומפורטות

### **התפתחות אבטחה מתמשכת**
- **התאמת נוף האיומים**: עדכונים שוטפים לטיפול באיומים מתפתחים
- **יעילות בקרות אבטחה**: הערכה ושיפור מתמיד של הבקרות
- **ציות למפרט**: התאמה לסטנדרטים אבטחתיים מתפתחים של MCP

---

## **משאבי יישום**

### **תיעוד רשמי של MCP**
- [מפרט MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [הנחיות אבטחה טובות של MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [מפרט הרשאות MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **משאבי אבטחת OWASP MCP**
- [מדריך אבטחת Azure של OWASP MCP](https://microsoft.github.io/mcp-azure-security-guide/) - רשימת OWASP MCP עשר הגדולות במימוש Azure
- [עשרת הגדולים של OWASP MCP](https://owasp.org/www-project-mcp-top-10/) - סכנות אבטחה רשמיות של OWASP MCP
- [סדנת שיא אבטחת MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - הדרכת אבטחה מעשית ל-MCP ב-Azure

### **פתרונות אבטחה של מייקרוסופט**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **תקני אבטחה**
- [הנחיות אבטחת OAuth 2.0 הטובות ביותר (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [עשרת הגדולים של OWASP לדגמי שפה גדולים](https://genai.owasp.org/)

- [מסגרת אבטחת סייבר של NIST](https://www.nist.gov/cyberframework)

---

> **חשוב:** בקרות האבטחה הללו משקפות את מפרט MCP
> `2026-07-28`. יש תמיד לוודא מול
> [התיעוד הרשמי הנוכחי](https://modelcontextprotocol.io/specification/2026-07-28/)
> ככל שהסטנדרטים ממשיכים להתפתח.

## מה הלאה

- חזור ל: [סקירת מודול האבטחה](./README.md)
- המשך ל: [מודול 3: להתחלה](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->