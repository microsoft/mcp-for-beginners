# کنترل‌های امنیتی MCP - به‌روزرسانی دسامبر ۲۰۲۵

> **استاندارد فعلی**: این سند نیازمندی‌های امنیتی [مشخصات MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) و بهترین شیوه‌های رسمی امنیتی [MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) را منعکس می‌کند.

پروتکل مدل کانتکست (MCP) به طور قابل توجهی با کنترل‌های امنیتی پیشرفته که تهدیدات سنتی نرم‌افزاری و تهدیدات خاص هوش مصنوعی را پوشش می‌دهد، بالغ شده است. این سند کنترل‌های امنیتی جامعی برای پیاده‌سازی‌های امن MCP تا دسامبر ۲۰۲۵ ارائه می‌دهد.

## **نیازمندی‌های امنیتی اجباری**

### **ممنوعیت‌های حیاتی از مشخصات MCP:**

> **ممنوع**: سرورهای MCP **نباید** هیچ توکنی را که به طور صریح برای سرور MCP صادر نشده است، قبول کنند  
>
> **ممنوع**: سرورهای MCP **نباید** از نشست‌ها برای احراز هویت استفاده کنند  
>
> **الزامی**: سرورهای MCP که مجوزدهی را پیاده‌سازی می‌کنند **باید** تمام درخواست‌های ورودی را تأیید کنند  
>
> **اجباری**: سرورهای پراکسی MCP که از شناسه‌های کلاینت استاتیک استفاده می‌کنند **باید** برای هر کلاینت ثبت‌شده پویا رضایت کاربر را دریافت کنند

---

## ۱. **کنترل‌های احراز هویت و مجوزدهی**

### **ادغام ارائه‌دهنده هویت خارجی**

**استاندارد فعلی MCP (۲۰۲۵-۰۶-۱۸)** اجازه می‌دهد سرورهای MCP احراز هویت را به ارائه‌دهندگان هویت خارجی واگذار کنند که یک بهبود امنیتی قابل توجه است:

### **ادغام ارائه‌دهنده هویت خارجی**

**استاندارد فعلی MCP (۲۰۲۵-۱۱-۲۵)** اجازه می‌دهد سرورهای MCP احراز هویت را به ارائه‌دهندگان هویت خارجی واگذار کنند که یک بهبود امنیتی قابل توجه است:

**مزایای امنیتی:**
۱. **حذف ریسک‌های احراز هویت سفارشی**: کاهش سطح آسیب‌پذیری با اجتناب از پیاده‌سازی‌های سفارشی احراز هویت  
۲. **امنیت سطح سازمانی**: بهره‌گیری از ارائه‌دهندگان هویت معتبر مانند Microsoft Entra ID با ویژگی‌های امنیتی پیشرفته  
۳. **مدیریت متمرکز هویت**: ساده‌سازی مدیریت چرخه عمر کاربر، کنترل دسترسی و ممیزی انطباق  
۴. **احراز هویت چندعاملی**: به ارث بردن قابلیت‌های MFA از ارائه‌دهندگان هویت سازمانی  
۵. **سیاست‌های دسترسی شرطی**: بهره‌مندی از کنترل‌های دسترسی مبتنی بر ریسک و احراز هویت تطبیقی

**نیازمندی‌های پیاده‌سازی:**
- **اعتبارسنجی مخاطب توکن**: تأیید اینکه تمام توکن‌ها به طور صریح برای سرور MCP صادر شده‌اند  
- **تأیید صادرکننده**: اعتبارسنجی اینکه صادرکننده توکن با ارائه‌دهنده هویت مورد انتظار مطابقت دارد  
- **تأیید امضا**: اعتبارسنجی رمزنگاری یکپارچگی توکن  
- **اجرای انقضا**: اجرای سختگیرانه محدودیت‌های عمر توکن  
- **اعتبارسنجی دامنه**: اطمینان از اینکه توکن‌ها مجوزهای مناسب برای عملیات درخواست شده را دارند

### **امنیت منطق مجوزدهی**

**کنترل‌های حیاتی:**
- **ممیزی جامع مجوزدهی**: بازبینی‌های امنیتی منظم تمام نقاط تصمیم‌گیری مجوزدهی  
- **پیش‌فرض‌های ایمن**: رد دسترسی زمانی که منطق مجوزدهی نتواند تصمیم قطعی بگیرد  
- **مرزهای مجوز**: تفکیک واضح بین سطوح امتیاز و دسترسی به منابع  
- **ثبت لاگ ممیزی**: ثبت کامل تمام تصمیمات مجوزدهی برای نظارت امنیتی  
- **بازبینی‌های منظم دسترسی**: اعتبارسنجی دوره‌ای مجوزها و تخصیص امتیازات کاربران

## ۲. **امنیت توکن و کنترل‌های ضد عبور توکن**

### **جلوگیری از عبور توکن**

**عبور توکن به صراحت در مشخصات مجوزدهی MCP ممنوع است** به دلیل ریسک‌های امنیتی حیاتی:

**ریسک‌های امنیتی پوشش داده شده:**
- **دور زدن کنترل‌ها**: عبور از کنترل‌های امنیتی ضروری مانند محدودیت نرخ، اعتبارسنجی درخواست و نظارت بر ترافیک  
- **شکست مسئولیت‌پذیری**: غیرممکن کردن شناسایی کلاینت و خراب کردن مسیرهای ممیزی و بررسی حوادث  
- **خروج داده از طریق پراکسی**: اجازه به بازیگران مخرب برای استفاده از سرورها به عنوان پراکسی برای دسترسی غیرمجاز به داده‌ها  
- **نقض مرز اعتماد**: شکستن فرضیات اعتماد سرویس‌های پایین‌دستی درباره منشاء توکن‌ها  
- **حرکت جانبی**: توکن‌های به خطر افتاده در چندین سرویس امکان گسترش حمله را فراهم می‌کنند

**کنترل‌های پیاده‌سازی:**
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

### **الگوهای مدیریت امن توکن**

**بهترین شیوه‌ها:**
- **توکن‌های کوتاه‌مدت**: کاهش پنجره در معرض خطر با چرخش مکرر توکن‌ها  
- **صدور به موقع**: صدور توکن‌ها فقط زمانی که برای عملیات خاص لازم است  
- **ذخیره‌سازی امن**: استفاده از ماژول‌های امنیتی سخت‌افزاری (HSM) یا خزانه‌های کلید امن  
- **بستن توکن**: اتصال توکن‌ها به کلاینت‌ها، نشست‌ها یا عملیات خاص در صورت امکان  
- **نظارت و هشداردهی**: شناسایی بلادرنگ سوءاستفاده از توکن یا الگوهای دسترسی غیرمجاز

## ۳. **کنترل‌های امنیت نشست**

### **جلوگیری از ربودن نشست**

**بردارهای حمله پوشش داده شده:**
- **تزریق درخواست ربودن نشست**: رویدادهای مخرب تزریق شده به وضعیت نشست مشترک  
- **تقلید نشست**: استفاده غیرمجاز از شناسه‌های نشست سرقت شده برای دور زدن احراز هویت  
- **حملات جریان قابل ادامه**: سوءاستفاده از ادامه رویدادهای ارسال شده توسط سرور برای تزریق محتوای مخرب

**کنترل‌های اجباری نشست:**
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

**امنیت انتقال:**
- **اجرای HTTPS**: تمام ارتباطات نشست بر بستر TLS 1.3  
- **ویژگی‌های امن کوکی**: HttpOnly، Secure، SameSite=Strict  
- **پین کردن گواهی**: برای ارتباطات حیاتی جهت جلوگیری از حملات MITM

### **ملاحظات حالت‌دار در مقابل بدون حالت**

**برای پیاده‌سازی‌های حالت‌دار:**
- وضعیت نشست مشترک نیازمند حفاظت اضافی در برابر حملات تزریق  
- مدیریت نشست مبتنی بر صف نیازمند اعتبارسنجی یکپارچگی  
- چندین نمونه سرور نیازمند همگام‌سازی امن وضعیت نشست

**برای پیاده‌سازی‌های بدون حالت:**
- مدیریت نشست مبتنی بر JWT یا توکن مشابه  
- اعتبارسنجی رمزنگاری یکپارچگی وضعیت نشست  
- کاهش سطح حمله اما نیازمند اعتبارسنجی قوی توکن

## ۴. **کنترل‌های امنیتی خاص هوش مصنوعی**

### **دفاع در برابر تزریق درخواست**

**ادغام Microsoft Prompt Shields:**
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

**کنترل‌های پیاده‌سازی:**
- **پاک‌سازی ورودی**: اعتبارسنجی و فیلتر جامع تمام ورودی‌های کاربر  
- **تعریف مرز محتوا**: تفکیک واضح بین دستورالعمل‌های سیستم و محتوای کاربر  
- **سلسله مراتب دستورالعمل**: قواعد تقدم مناسب برای دستورالعمل‌های متضاد  
- **نظارت خروجی**: شناسایی خروجی‌های بالقوه مضر یا دستکاری شده

### **جلوگیری از مسمومیت ابزار**

**چارچوب امنیت ابزار:**
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

**مدیریت پویا ابزار:**
- **گردش کارهای تأیید**: رضایت صریح کاربر برای تغییرات ابزار  
- **قابلیت بازگشت**: امکان بازگرداندن به نسخه‌های قبلی ابزار  
- **ممیزی تغییرات**: تاریخچه کامل تغییرات تعریف ابزار  
- **ارزیابی ریسک**: ارزیابی خودکار وضعیت امنیتی ابزار

## ۵. **جلوگیری از حمله معاون گیج‌شده**

### **امنیت پراکسی OAuth**

**کنترل‌های پیشگیری از حمله:**
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

**نیازمندی‌های پیاده‌سازی:**
- **تأیید رضایت کاربر**: هرگز صفحه‌های رضایت برای ثبت کلاینت پویا را رد نکنید  
- **اعتبارسنجی URI بازگشت**: اعتبارسنجی سختگیرانه مبتنی بر فهرست سفید مقصدهای بازگشت  
- **حفاظت کد مجوز**: کدهای کوتاه‌مدت با اجرای استفاده یک‌باره  
- **اعتبارسنجی هویت کلاینت**: اعتبارسنجی قوی مدارک و متادیتای کلاینت

## ۶. **امنیت اجرای ابزار**

### **ایزولاسیون و سندباکس**

**ایزولاسیون مبتنی بر کانتینر:**
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

**ایزولاسیون فرآیند:**
- **زمینه‌های فرآیند جداگانه**: اجرای هر ابزار در فضای فرآیند ایزوله  
- **ارتباط بین فرآیندی**: مکانیزم‌های IPC امن با اعتبارسنجی  
- **نظارت فرآیند**: تحلیل رفتار زمان اجرا و شناسایی ناهنجاری  
- **اجرای محدودیت منابع**: محدودیت سخت بر CPU، حافظه و عملیات I/O

### **پیاده‌سازی حداقل امتیاز**

**مدیریت مجوز:**
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

## ۷. **کنترل‌های امنیت زنجیره تأمین**

### **اعتبارسنجی وابستگی‌ها**

**امنیت جامع مؤلفه‌ها:**
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

### **نظارت مستمر**

**شناسایی تهدیدات زنجیره تأمین:**
- **نظارت سلامت وابستگی‌ها**: ارزیابی مستمر تمام وابستگی‌ها برای مسائل امنیتی  
- **ادغام اطلاعات تهدید**: به‌روزرسانی‌های بلادرنگ درباره تهدیدات نوظهور زنجیره تأمین  
- **تحلیل رفتاری**: شناسایی رفتار غیرمعمول در مؤلفه‌های خارجی  
- **پاسخ خودکار**: مهار فوری مؤلفه‌های به خطر افتاده

## ۸. **کنترل‌های نظارت و شناسایی**

### **مدیریت اطلاعات و رویدادهای امنیتی (SIEM)**

**استراتژی جامع ثبت لاگ:**
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

### **شناسایی تهدید بلادرنگ**

**تحلیل رفتاری:**
- **تحلیل رفتار کاربر (UBA)**: شناسایی الگوهای دسترسی غیرمعمول کاربران  
- **تحلیل رفتار موجودیت (EBA)**: نظارت بر رفتار سرور MCP و ابزارها  
- **شناسایی ناهنجاری با یادگیری ماشین**: شناسایی تهدیدات امنیتی با هوش مصنوعی  
- **همبستگی اطلاعات تهدید**: تطبیق فعالیت‌های مشاهده شده با الگوهای حمله شناخته شده

## ۹. **پاسخ به حادثه و بازیابی**

### **قابلیت‌های پاسخ خودکار**

**اقدامات پاسخ فوری:**
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

### **قابلیت‌های جرم‌شناسی**

**پشتیبانی از تحقیقات:**
- **حفظ مسیر ممیزی**: ثبت لاگ غیرقابل تغییر با یکپارچگی رمزنگاری  
- **جمع‌آوری شواهد**: جمع‌آوری خودکار آثار امنیتی مرتبط  
- **بازسازی خط زمانی**: توالی دقیق رویدادهای منجر به حوادث امنیتی  
- **ارزیابی تأثیر**: ارزیابی دامنه نفوذ و افشای داده‌ها

## **اصول کلیدی معماری امنیتی**

### **دفاع در عمق**
- **چندین لایه امنیتی**: عدم وجود نقطه شکست واحد در معماری امنیتی  
- **کنترل‌های افزونه**: اقدامات امنیتی همپوشان برای عملکردهای حیاتی  
- **مکانیزم‌های ایمن پیش‌فرض**: تنظیمات امن هنگام مواجهه با خطاها یا حملات

### **پیاده‌سازی اعتماد صفر**
- **هرگز اعتماد نکن، همیشه تأیید کن**: اعتبارسنجی مداوم تمام موجودیت‌ها و درخواست‌ها  
- **اصل حداقل امتیاز**: حداقل حقوق دسترسی برای تمام مؤلفه‌ها  
- **ریز‌بخشی**: کنترل‌های شبکه و دسترسی دقیق

### **تکامل مستمر امنیت**
- **انطباق با چشم‌انداز تهدید**: به‌روزرسانی‌های منظم برای مقابله با تهدیدات نوظهور  
- **اثربخشی کنترل‌های امنیتی**: ارزیابی و بهبود مستمر کنترل‌ها  
- **انطباق با مشخصات**: همسویی با استانداردهای امنیتی در حال تکامل MCP

---

## **منابع پیاده‌سازی**

### **مستندات رسمی MCP**
- [مشخصات MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [بهترین شیوه‌های امنیتی MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [مشخصات مجوزدهی MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **راهکارهای امنیتی مایکروسافت**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **استانداردهای امنیتی**
- [بهترین شیوه‌های امنیت OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [ده تهدید برتر OWASP برای مدل‌های زبان بزرگ](https://genai.owasp.org/)
- [چارچوب امنیت سایبری NIST](https://www.nist.gov/cyberframework)

---

> **مهم**: این کنترل‌های امنیتی منعکس‌کننده مشخصات فعلی MCP (۲۰۲۵-۰۶-۱۸) هستند. همواره با آخرین [مستندات رسمی](https://spec.modelcontextprotocol.io/) بررسی کنید زیرا استانداردها به سرعت در حال تکامل هستند.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->