# ضوابط أمان MCP - تحديث ديسمبر 2025

> **المعيار الحالي**: يعكس هذا المستند متطلبات الأمان في [مواصفة MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) وأفضل الممارسات الأمنية الرسمية لـ [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

لقد نضج بروتوكول سياق النموذج (MCP) بشكل كبير مع ضوابط أمان محسنة تعالج كل من أمان البرمجيات التقليدية والتهديدات الخاصة بالذكاء الاصطناعي. يوفر هذا المستند ضوابط أمان شاملة لتنفيذات MCP الآمنة اعتبارًا من ديسمبر 2025.

## **متطلبات الأمان الإلزامية**

### **القيود الحرجة من مواصفة MCP:**

> **ممنوع**: يجب على خوادم MCP **عدم قبول** أي رموز لم تصدر صراحة لخادم MCP  
>
> **محظور**: يجب على خوادم MCP **عدم استخدام** الجلسات للمصادقة  
>
> **مطلوب**: يجب على خوادم MCP التي تنفذ التفويض **التحقق من جميع الطلبات الواردة**  
>
> **إلزامي**: يجب على خوادم وكيل MCP التي تستخدم معرفات عملاء ثابتة **الحصول على موافقة المستخدم لكل عميل مسجل ديناميكيًا**

---

## 1. **ضوابط المصادقة والتفويض**

### **تكامل مزود الهوية الخارجي**

يسمح **المعيار الحالي لـ MCP (2025-06-18)** لخوادم MCP بتفويض المصادقة إلى مزودي هوية خارجيين، مما يمثل تحسنًا أمنيًا كبيرًا:

### **تكامل مزود الهوية الخارجي**

يسمح **المعيار الحالي لـ MCP (2025-11-25)** لخوادم MCP بتفويض المصادقة إلى مزودي هوية خارجيين، مما يمثل تحسنًا أمنيًا كبيرًا:

**فوائد الأمان:**
1. **إزالة مخاطر المصادقة المخصصة**: يقلل من سطح الهجوم بتجنب تنفيذات المصادقة المخصصة  
2. **أمان بمستوى المؤسسات**: يستفيد من مزودي الهوية المعتمدين مثل Microsoft Entra ID مع ميزات أمان متقدمة  
3. **إدارة هوية مركزية**: يبسط إدارة دورة حياة المستخدم، التحكم في الوصول، وتدقيق الامتثال  
4. **المصادقة متعددة العوامل**: يرث قدرات المصادقة متعددة العوامل من مزودي الهوية المؤسسية  
5. **سياسات الوصول الشرطية**: يستفيد من ضوابط الوصول القائمة على المخاطر والمصادقة التكيفية  

**متطلبات التنفيذ:**
- **التحقق من جمهور الرمز**: التحقق من أن جميع الرموز صادرة صراحة لخادم MCP  
- **التحقق من المصدر**: التحقق من أن مصدر الرمز يطابق مزود الهوية المتوقع  
- **التحقق من التوقيع**: التحقق التشفيري من سلامة الرمز  
- **فرض انتهاء الصلاحية**: تطبيق صارم لحدود عمر الرمز  
- **التحقق من النطاق**: التأكد من أن الرموز تحتوي على الأذونات المناسبة للعمليات المطلوبة  

### **أمان منطق التفويض**

**الضوابط الحرجة:**
- **تدقيقات تفويض شاملة**: مراجعات أمنية منتظمة لجميع نقاط اتخاذ قرارات التفويض  
- **الإفتراضات الآمنة**: رفض الوصول عندما لا يمكن لمنطق التفويض اتخاذ قرار حاسم  
- **حدود الأذونات**: فصل واضح بين مستويات الامتياز المختلفة والوصول إلى الموارد  
- **تسجيل التدقيق**: تسجيل كامل لجميع قرارات التفويض لمراقبة الأمان  
- **مراجعات وصول دورية**: التحقق الدوري من أذونات المستخدم وتعيينات الامتياز  

## 2. **أمان الرموز وضوابط منع التمرير**

### **منع تمرير الرموز**

**تم حظر تمرير الرموز صراحة** في مواصفة تفويض MCP بسبب مخاطر أمنية حرجة:

**المخاطر الأمنية المعالجة:**
- **التحايل على الضوابط**: تجاوز ضوابط الأمان الأساسية مثل تحديد المعدل، التحقق من الطلب، ومراقبة الحركة  
- **انهيار المساءلة**: يجعل تحديد هوية العميل مستحيلاً، مما يفسد سجلات التدقيق والتحقيق في الحوادث  
- **التسريب عبر الوكيل**: يمكّن الجهات الخبيثة من استخدام الخوادم كوسطاء للوصول غير المصرح به إلى البيانات  
- **انتهاكات حدود الثقة**: يكسر افتراضات الثقة في الخدمات اللاحقة حول أصول الرموز  
- **الحركة الجانبية**: تمكن الرموز المخترقة عبر خدمات متعددة من توسيع نطاق الهجوم  

**ضوابط التنفيذ:**
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

### **أنماط إدارة الرموز الآمنة**

**أفضل الممارسات:**
- **رموز قصيرة العمر**: تقليل نافذة التعرض بتدوير الرموز بشكل متكرر  
- **الإصدار عند الحاجة**: إصدار الرموز فقط عند الحاجة لعمليات محددة  
- **التخزين الآمن**: استخدام وحدات الأمان المادية (HSM) أو خزائن المفاتيح الآمنة  
- **ربط الرموز**: ربط الرموز بعملاء أو جلسات أو عمليات محددة حيثما أمكن  
- **المراقبة والتنبيه**: الكشف في الوقت الحقيقي عن سوء استخدام الرموز أو أنماط الوصول غير المصرح بها  

## 3. **ضوابط أمان الجلسة**

### **منع اختطاف الجلسة**

**مسارات الهجوم المعالجة:**
- **حقن مطالبات اختطاف الجلسة**: حقن أحداث خبيثة في حالة الجلسة المشتركة  
- **انتحال الجلسة**: استخدام غير مصرح به لمعرفات الجلسة المسروقة لتجاوز المصادقة  
- **هجمات استئناف تدفق الأحداث**: استغلال استئناف أحداث الخادم لإدخال محتوى خبيث  

**ضوابط الجلسة الإلزامية:**
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

**أمان النقل:**
- **فرض HTTPS**: جميع اتصالات الجلسة عبر TLS 1.3  
- **سمات الكوكيز الآمنة**: HttpOnly، Secure، SameSite=Strict  
- **تثبيت الشهادة**: للاتصالات الحرجة لمنع هجمات MITM  

### **الاعتبارات بين الحالة والحالة بدون حالة**

**للتنفيذات ذات الحالة:**
- تتطلب حالة الجلسة المشتركة حماية إضافية ضد هجمات الحقن  
- إدارة الجلسة القائمة على الطوابير تحتاج إلى التحقق من السلامة  
- تتطلب مثيلات الخادم المتعددة مزامنة آمنة لحالة الجلسة  

**للتنفيذات بدون حالة:**
- إدارة الجلسة باستخدام JWT أو رموز مماثلة  
- التحقق التشفيري من سلامة حالة الجلسة  
- تقليل سطح الهجوم ولكن يتطلب تحققًا قويًا من الرموز  

## 4. **ضوابط أمان خاصة بالذكاء الاصطناعي**

### **الدفاع ضد حقن المطالبات**

**تكامل Microsoft Prompt Shields:**
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

**ضوابط التنفيذ:**
- **تنقية المدخلات**: التحقق الشامل وتصفيه جميع مدخلات المستخدم  
- **تعريف حدود المحتوى**: فصل واضح بين تعليمات النظام ومحتوى المستخدم  
- **تسلسل التعليمات**: قواعد أسبقية صحيحة للتعليمات المتضاربة  
- **مراقبة المخرجات**: الكشف عن المخرجات الضارة أو المعدلة  

### **منع تسميم الأدوات**

**إطار أمان الأدوات:**
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

**إدارة الأدوات الديناميكية:**
- **سير عمل الموافقة**: موافقة صريحة من المستخدم على تعديلات الأدوات  
- **قدرات التراجع**: إمكانية العودة إلى إصدارات الأدوات السابقة  
- **تدقيق التغييرات**: سجل كامل لتعديلات تعريف الأدوات  
- **تقييم المخاطر**: تقييم آلي لوضع أمان الأدوات  

## 5. **منع هجوم الوكيل المشوش**

### **أمان وكيل OAuth**

**ضوابط منع الهجوم:**
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

**متطلبات التنفيذ:**
- **التحقق من موافقة المستخدم**: عدم تخطي شاشات الموافقة لتسجيل العملاء الديناميكي  
- **التحقق من URI إعادة التوجيه**: تحقق صارم قائم على القائمة البيضاء لوجهات إعادة التوجيه  
- **حماية رمز التفويض**: رموز قصيرة العمر مع فرض الاستخدام لمرة واحدة  
- **التحقق من هوية العميل**: تحقق قوي من بيانات اعتماد العميل والبيانات الوصفية  

## 6. **أمان تنفيذ الأدوات**

### **العزل والتقسيم**

**العزل القائم على الحاويات:**
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

**عزل العمليات:**
- **سياقات عمليات منفصلة**: تنفيذ كل أداة في مساحة عملية معزولة  
- **الاتصال بين العمليات**: آليات IPC آمنة مع التحقق  
- **مراقبة العمليات**: تحليل سلوك وقت التشغيل واكتشاف الشذوذ  
- **فرض الموارد**: حدود صارمة على CPU، الذاكرة، وعمليات الإدخال/الإخراج  

### **تنفيذ مبدأ أقل امتياز**

**إدارة الأذونات:**
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

## 7. **ضوابط أمان سلسلة التوريد**

### **التحقق من التبعيات**

**أمان مكونات شامل:**
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

### **المراقبة المستمرة**

**كشف تهديدات سلسلة التوريد:**
- **مراقبة صحة التبعيات**: تقييم مستمر لجميع التبعيات لمشاكل الأمان  
- **تكامل استخبارات التهديدات**: تحديثات في الوقت الحقيقي حول تهديدات سلسلة التوريد الناشئة  
- **التحليل السلوكي**: الكشف عن السلوك غير المعتاد في المكونات الخارجية  
- **الاستجابة الآلية**: احتواء فوري للمكونات المخترقة  

## 8. **ضوابط المراقبة والكشف**

### **إدارة معلومات الأمان والأحداث (SIEM)**

**استراتيجية تسجيل شاملة:**
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

### **الكشف عن التهديدات في الوقت الحقيقي**

**تحليلات السلوك:**
- **تحليلات سلوك المستخدم (UBA)**: الكشف عن أنماط وصول المستخدم غير المعتادة  
- **تحليلات سلوك الكيان (EBA)**: مراقبة سلوك خادم MCP والأدوات  
- **كشف الشذوذ باستخدام التعلم الآلي**: تحديد التهديدات الأمنية مدعوم بالذكاء الاصطناعي  
- **ترابط استخبارات التهديدات**: مطابقة الأنشطة المرصودة مع أنماط الهجوم المعروفة  

## 9. **الاستجابة للحوادث والتعافي**

### **قدرات الاستجابة الآلية**

**إجراءات الاستجابة الفورية:**
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

### **قدرات التحليل الجنائي**

**دعم التحقيق:**
- **حفظ سجل التدقيق**: تسجيل غير قابل للتغيير مع سلامة تشفيرية  
- **جمع الأدلة**: جمع آلي للقطع الأمنية ذات الصلة  
- **إعادة بناء الجدول الزمني**: تسلسل مفصل للأحداث التي أدت إلى الحوادث الأمنية  
- **تقييم التأثير**: تقييم نطاق الاختراق وكشف البيانات  

## **مبادئ أساسية لهندسة الأمان**

### **الدفاع في العمق**
- **طبقات أمان متعددة**: لا نقطة فشل واحدة في هندسة الأمان  
- **ضوابط زائدة**: تدابير أمان متداخلة للوظائف الحرجة  
- **آليات آمنة افتراضية**: إعدادات آمنة عند مواجهة الأخطاء أو الهجمات  

### **تنفيذ الثقة الصفرية**
- **عدم الثقة مطلقًا، والتحقق دائمًا**: التحقق المستمر من جميع الكيانات والطلبات  
- **مبدأ أقل امتياز**: أقل حقوق وصول لجميع المكونات  
- **التقسيم الدقيق**: ضوابط دقيقة للشبكة والوصول  

### **تطور أمان مستمر**
- **التكيف مع مشهد التهديدات**: تحديثات منتظمة لمعالجة التهديدات الناشئة  
- **فعالية ضوابط الأمان**: تقييم وتحسين مستمر للضوابط  
- **الامتثال للمواصفات**: التوافق مع معايير أمان MCP المتطورة  

---

## **موارد التنفيذ**

### **التوثيق الرسمي لـ MCP**
- [مواصفة MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [أفضل ممارسات أمان MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [مواصفة تفويض MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **حلول أمان Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **معايير الأمان**
- [أفضل ممارسات أمان OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP أفضل 10 لنماذج اللغة الكبيرة](https://genai.owasp.org/)
- [إطار عمل الأمن السيبراني NIST](https://www.nist.gov/cyberframework)

---

> **مهم**: تعكس ضوابط الأمان هذه مواصفة MCP الحالية (2025-06-18). تحقق دائمًا من [التوثيق الرسمي](https://spec.modelcontextprotocol.io/) الأحدث حيث تستمر المعايير في التطور بسرعة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->