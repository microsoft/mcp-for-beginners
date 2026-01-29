# בקרות אבטחה של MCP - עדכון דצמבר 2025

> **תקן נוכחי**: מסמך זה משקף את דרישות האבטחה של [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) ואת [הנחיות אבטחה הטובות ביותר של MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

פרוטוקול הקשר של המודל (MCP) התפתח משמעותית עם בקרות אבטחה משופרות המתייחסות הן לאבטחת תוכנה מסורתית והן לאיומים ספציפיים לבינה מלאכותית. מסמך זה מספק בקרות אבטחה מקיפות ליישומי MCP מאובטחים נכון לדצמבר 2025.

## **דרישות אבטחה מחייבות**

### **איסורים קריטיים מפרוטוקול MCP:**

> **אסור**: שרתי MCP **אסור שיקבלו** כל אסימונים שלא הונפקו במפורש עבור שרת MCP  
>
> **אסור**: שרתי MCP **אסור שישתמשו** במפגשים לאימות  
>
> **נדרש**: שרתי MCP המיישמים הרשאה **חייבים** לאמת את כל הבקשות הנכנסות  
>
> **מחייב**: שרתי פרוקסי MCP המשתמשים במזהי לקוח סטטיים **חייבים** לקבל הסכמת משתמש עבור כל לקוח שנרשם דינמית

---

## 1. **בקרות אימות והרשאה**

### **שילוב ספק זהות חיצוני**

**תקן MCP נוכחי (2025-06-18)** מאפשר לשרתי MCP להאציל אימות לספקי זהות חיצוניים, מה שמייצג שיפור אבטחה משמעותי:

### **שילוב ספק זהות חיצוני**

**תקן MCP נוכחי (2025-11-25)** מאפשר לשרתי MCP להאציל אימות לספקי זהות חיצוניים, מה שמייצג שיפור אבטחה משמעותי:

**יתרונות אבטחה:**
1. **מונע סיכוני אימות מותאם אישית**: מצמצם את שטח הפגיעות על ידי הימנעות מיישומי אימות מותאמים אישית  
2. **אבטחה ברמת ארגון**: מנצל ספקי זהות מבוססים כמו Microsoft Entra ID עם תכונות אבטחה מתקדמות  
3. **ניהול זהות מרכזי**: מפשט ניהול מחזור חיי משתמש, בקרת גישה וביקורת תאימות  
4. **אימות רב-שלבי**: יורש יכולות MFA מספקי זהות ארגוניים  
5. **מדיניות גישה מותנית**: נהנה מבקרות גישה מבוססות סיכון ואימות אדפטיבי

**דרישות יישום:**
- **אימות קהל אסימון**: לאמת שכל האסימונים הונפקו במפורש עבור שרת MCP  
- **אימות מנפיק**: לאמת שמנפיק האסימון תואם לספק הזהות הצפוי  
- **אימות חתימה**: אימות קריפטוגרפי של שלמות האסימון  
- **אכיפת תוקף**: אכיפה מחמירה של מגבלות חיי האסימון  
- **אימות תחום**: לוודא שהאסימונים מכילים הרשאות מתאימות לפעולות המבוקשות

### **אבטחת לוגיקת הרשאה**

**בקרות קריטיות:**
- **ביקורות הרשאה מקיפות**: סקירות אבטחה סדירות של כל נקודות קבלת ההחלטות בהרשאה  
- **ברירות מחדל בטוחות**: סירוב גישה כאשר לוגיקת ההרשאה אינה יכולה לקבל החלטה חד-משמעית  
- **גבולות הרשאה**: הפרדה ברורה בין רמות הרשאה שונות וגישה למשאבים  
- **רישום ביקורת**: תיעוד מלא של כל החלטות ההרשאה למעקב אבטחה  
- **סקירות גישה סדירות**: אימות תקופתי של הרשאות משתמשים והקצאות הרשאה

## 2. **אבטחת אסימון ובקרות מניעת העברה ישירה**

### **מניעת העברה ישירה של אסימון**

**העברה ישירה של אסימון אסורה במפורש** בפרוטוקול ההרשאה של MCP עקב סיכוני אבטחה קריטיים:

**סיכוני אבטחה מטופלים:**
- **עקיפת בקרות**: עוקף בקרות אבטחה חיוניות כמו הגבלת קצב, אימות בקשות ומעקב תעבורה  
- **שבירת אחריות**: מונע זיהוי לקוח, פוגע בשרשראות ביקורת ובחקירת תקריות  
- **הוצאה לא חוקית דרך פרוקסי**: מאפשר לשחקנים זדוניים להשתמש בשרתים כפרוקסי לגישה לא מורשית לנתונים  
- **הפרת גבולות אמון**: שוברת הנחות אמון של שירותים במקור האסימונים  
- **תנועה רוחבית**: אסימונים שנפרצו בין שירותים מאפשרים הרחבת התקפות

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

### **תבניות ניהול אסימונים מאובטחות**

**הנחיות טובות:**
- **אסימונים קצרים חיים**: צמצום חלון החשיפה עם סיבוב אסימונים תכוף  
- **הנפקה בזמן אמת**: הנפקת אסימונים רק בעת הצורך לפעולות ספציפיות  
- **אחסון מאובטח**: שימוש במודולי אבטחה חומרתיים (HSM) או כספות מפתחות מאובטחות  
- **קישור אסימונים**: קישור אסימונים ללקוחות, מפגשים או פעולות ספציפיות ככל האפשר  
- **מעקב והתראות**: זיהוי בזמן אמת של שימוש לרעה באסימונים או דפוסי גישה לא מורשים

## 3. **בקרות אבטחת מפגשים**

### **מניעת חטיפת מפגשים**

**וקטורי התקפה מטופלים:**
- **הזרקת פקודות חטיפת מפגש**: אירועים זדוניים מוזרקים למצב מפגש משותף  
- **זיוף מפגש**: שימוש לא מורשה במזהי מפגש גנובים לעקיפת אימות  
- **התקפות המשך זרם**: ניצול חידוש אירועי שרת להזרקת תוכן זדוני

**בקרות מפגש מחייבות:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**אבטחת תעבורה:**
- **אכיפת HTTPS**: כל תקשורת המפגש על TLS 1.3  
- **מאפייני עוגיות מאובטחות**: HttpOnly, Secure, SameSite=Strict  
- **נעילת תעודה**: לחיבורים קריטיים למניעת התקפות MITM

### **שיקולים בין מצב מדינתי ללא מדינתי**

**ליישומים מדינתיים:**
- מצב מפגש משותף דורש הגנה נוספת מפני התקפות הזרקה  
- ניהול מפגש מבוסס תור דורש אימות שלמות  
- מופעי שרת מרובים דורשים סינכרון מאובטח של מצב המפגש

**ליישומים ללא מדינה:**
- ניהול מפגש מבוסס JWT או אסימונים דומים  
- אימות קריפטוגרפי של שלמות מצב המפגש  
- שטח התקפה מצומצם אך דורש אימות אסימונים חזק

## 4. **בקרות אבטחה ספציפיות לבינה מלאכותית**

### **הגנה מפני הזרקת פקודות**

**שילוב Microsoft Prompt Shields:**
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
- **סינון קלט**: אימות וסינון מקיף של כל קלטי המשתמש  
- **הגדרת גבולות תוכן**: הפרדה ברורה בין הוראות מערכת לתוכן משתמש  
- **היררכיית הוראות**: כללי קדימות נכונים להוראות סותרות  
- **מעקב פלט**: זיהוי פלטים פוטנציאלית מזיקים או מנוהלים

### **מניעת הרעלת כלים**

**מסגרת אבטחת כלים:**
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

**ניהול כלים דינמי:**
- **זרימות עבודה לאישור**: הסכמת משתמש מפורשת לשינויים בכלים  
- **יכולת חזרה לאחור**: אפשרות לשחזור גרסאות קודמות של כלים  
- **ביקורת שינויים**: היסטוריה מלאה של שינויים בהגדרת כלים  
- **הערכת סיכונים**: הערכה אוטומטית של מצב האבטחה של הכלים

## 5. **מניעת התקפת סגן מבלבל**

### **אבטחת פרוקסי OAuth**

**בקרות מניעת התקפה:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
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
- **אימות הסכמת משתמש**: לעולם לא לדלג על מסכי הסכמה לרישום לקוח דינמי  
- **אימות URI הפניה מחדש**: אימות מחמיר מבוסס רשימת לבנה של יעדי הפניה  
- **הגנת קוד הרשאה**: קודים קצרים חיים עם אכיפת שימוש חד-פעמי  
- **אימות זהות לקוח**: אימות חזק של אישורי לקוח ומטא-נתונים

## 6. **אבטחת ביצוע כלים**

### **סנדבוקס ובידוד**

**בידוד מבוסס מכולות:**
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

**בידוד תהליכים:**
- **הקשרי תהליך נפרדים**: כל ביצוע כלי במרחב תהליך מבודד  
- **תקשורת בין תהליכים**: מנגנוני IPC מאובטחים עם אימות  
- **מעקב תהליכים**: ניתוח התנהגות בזמן ריצה וזיהוי חריגות  
- **אכיפת משאבים**: הגבלות מחמירות על CPU, זיכרון ופעולות I/O

### **יישום עיקרון ההרשאה המינימלית**

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

### **אימות תלותיות**

**אבטחת רכיבים מקיפה:**
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

### **מעקב רציף**

**זיהוי איומי שרשרת אספקה:**
- **מעקב בריאות תלותיות**: הערכה רציפה של כל התלותיות לאיומי אבטחה  
- **שילוב מודיעין איומים**: עדכונים בזמן אמת על איומי שרשרת אספקה מתפתחים  
- **ניתוח התנהגותי**: זיהוי התנהגות חריגה ברכיבים חיצוניים  
- **תגובה אוטומטית**: בידוד מיידי של רכיבים שנפרצו

## 8. **בקרות ניטור וזיהוי**

### **ניהול מידע ואירועים אבטחתיים (SIEM)**

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
- **אנליטיקת התנהגות משתמש (UBA)**: זיהוי דפוסי גישה חריגים של משתמשים  
- **אנליטיקת התנהגות ישות (EBA)**: מעקב אחר התנהגות שרתי MCP וכלים  
- **זיהוי חריגות בלמידת מכונה**: זיהוי איומי אבטחה מונחה בינה מלאכותית  
- **קורלציה עם מודיעין איומים**: התאמת פעילויות נצפות לתבניות התקפה ידועות

## 9. **תגובה ותיקון תקריות**

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
- **שימור שרשרת ביקורת**: רישום בלתי ניתן לשינוי עם שלמות קריפטוגרפית  
- **איסוף ראיות**: איסוף אוטומטי של ארטיפקטים רלוונטיים לאבטחה  
- **שחזור ציר זמן**: רצף מפורט של אירועים שהובילו לתקריות אבטחה  
- **הערכת השפעה**: הערכת היקף הפגיעה וחשיפת נתונים

## **עקרונות מפתח בארכיטקטורת אבטחה**

### **הגנה בעומק**
- **שכבות אבטחה מרובות**: אין נקודת כשל יחידה בארכיטקטורת האבטחה  
- **בקרות מיותרות**: אמצעי אבטחה חופפים לתפקודים קריטיים  
- **מנגנוני כשל בטוח**: ברירות מחדל מאובטחות כאשר מערכות נתקעות בשגיאות או התקפות

### **יישום אפס אמון**
- **לעולם לא לסמוך, תמיד לאמת**: אימות רציף של כל ישויות ובקשות  
- **עיקרון ההרשאה המינימלית**: זכויות גישה מינימליות לכל הרכיבים  
- **מיקרו-סגמנטציה**: בקרות רשת וגישה גרנולריות

### **התפתחות אבטחה מתמשכת**
- **התאמת נוף איומים**: עדכונים סדירים לטיפול באיומים מתפתחים  
- **יעילות בקרות אבטחה**: הערכה ושיפור מתמיד של הבקרות  
- **עמידה בתקנים**: התאמה לסטנדרטים מתפתחים של אבטחת MCP

---

## **משאבי יישום**

### **תיעוד רשמי של MCP**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **פתרונות אבטחה של מיקרוסופט**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **תקני אבטחה**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **חשוב**: בקרות אבטחה אלו משקפות את מפרט MCP הנוכחי (2025-06-18). יש תמיד לאמת מול [התיעוד הרשמי](https://spec.modelcontextprotocol.io/) העדכני ביותר שכן התקנים ממשיכים להתפתח במהירות.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->