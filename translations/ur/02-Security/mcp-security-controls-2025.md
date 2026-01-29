# MCP سیکیورٹی کنٹرولز - دسمبر 2025 اپ ڈیٹ

> **موجودہ معیار**: یہ دستاویز [MCP وضاحت 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) کی سیکیورٹی ضروریات اور سرکاری [MCP سیکیورٹی بہترین طریقہ کار](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) کی عکاسی کرتی ہے۔

ماڈل کانٹیکسٹ پروٹوکول (MCP) نے روایتی سافٹ ویئر سیکیورٹی اور AI مخصوص خطرات دونوں کو حل کرنے والے بہتر سیکیورٹی کنٹرولز کے ساتھ نمایاں ترقی کی ہے۔ یہ دستاویز دسمبر 2025 تک محفوظ MCP نفاذ کے لیے جامع سیکیورٹی کنٹرولز فراہم کرتی ہے۔

## **لازمی سیکیورٹی ضروریات**

### **MCP وضاحت سے اہم ممنوعات:**

> **ممنوع**: MCP سرورز **کسی بھی ایسے ٹوکن کو قبول نہیں کریں گے جو واضح طور پر MCP سرور کے لیے جاری نہ کیے گئے ہوں**  
>
> **ممنوع**: MCP سرورز **تصدیق کے لیے سیشنز استعمال نہیں کریں گے**  
>
> **ضروری**: MCP سرورز جو اجازت نامہ نافذ کرتے ہیں **تمام آنے والی درخواستوں کی تصدیق کریں گے**  
>
> **لازمی**: MCP پراکسی سرورز جو جامد کلائنٹ IDs استعمال کرتے ہیں **ہر متحرک طور پر رجسٹرڈ کلائنٹ کے لیے صارف کی رضامندی حاصل کریں گے**

---

## 1. **تصدیق اور اجازت کنٹرولز**

### **بیرونی شناخت فراہم کنندہ انضمام**

**موجودہ MCP معیار (2025-06-18)** MCP سرورز کو اجازت دیتا ہے کہ وہ تصدیق کو بیرونی شناخت فراہم کنندگان کو تفویض کریں، جو ایک اہم سیکیورٹی بہتری کی نمائندگی کرتا ہے:

### **بیرونی شناخت فراہم کنندہ انضمام**

**موجودہ MCP معیار (2025-11-25)** MCP سرورز کو اجازت دیتا ہے کہ وہ تصدیق کو بیرونی شناخت فراہم کنندگان کو تفویض کریں، جو ایک اہم سیکیورٹی بہتری کی نمائندگی کرتا ہے:

**سیکیورٹی فوائد:**  
1. **کسٹم تصدیق کے خطرات کو ختم کرتا ہے**: کسٹم تصدیق کے نفاذ سے بچ کر کمزوریاں کم کرتا ہے  
2. **انٹرپرائز گریڈ سیکیورٹی**: مائیکروسافٹ اینٹرا ID جیسے مستحکم شناخت فراہم کنندگان کے جدید سیکیورٹی فیچرز کا فائدہ اٹھاتا ہے  
3. **مرکزی شناخت مینجمنٹ**: صارف کے لائف سائیکل مینجمنٹ، رسائی کنٹرول، اور تعمیل آڈٹ کو آسان بناتا ہے  
4. **کثیر عنصر تصدیق**: انٹرپرائز شناخت فراہم کنندگان سے MFA صلاحیتیں حاصل کرتا ہے  
5. **مشروط رسائی پالیسیاں**: خطرے کی بنیاد پر رسائی کنٹرولز اور موافقت پذیر تصدیق سے فائدہ اٹھاتا ہے

**نفاذ کی ضروریات:**  
- **ٹوکن آڈینس کی توثیق**: تمام ٹوکنز کی تصدیق کریں کہ وہ واضح طور پر MCP سرور کے لیے جاری کیے گئے ہیں  
- **جاری کنندہ کی تصدیق**: ٹوکن جاری کنندہ کی توقع شدہ شناخت فراہم کنندہ سے مطابقت کی تصدیق کریں  
- **دستخط کی تصدیق**: ٹوکن کی سالمیت کی کرپٹوگرافک تصدیق  
- **میعاد ختم ہونے کا نفاذ**: ٹوکن کی مدت کی سخت پابندی  
- **اسکوپ کی توثیق**: یقینی بنائیں کہ ٹوکنز میں درخواست کردہ آپریشنز کے لیے مناسب اجازتیں موجود ہیں

### **اجازت منطق کی سیکیورٹی**

**اہم کنٹرولز:**  
- **جامع اجازت آڈٹس**: تمام اجازت کے فیصلوں کے پوائنٹس کا باقاعدہ سیکیورٹی جائزہ  
- **فیل سیف ڈیفالٹس**: جب اجازت منطق واضح فیصلہ نہ کر سکے تو رسائی مسترد کریں  
- **اجازت کی حد بندی**: مختلف مراعات کی سطحوں اور وسائل کی رسائی کے درمیان واضح تفریق  
- **آڈٹ لاگنگ**: سیکیورٹی مانیٹرنگ کے لیے تمام اجازت کے فیصلوں کا مکمل لاگ  
- **باقاعدہ رسائی جائزے**: صارف کی اجازتوں اور مراعات کی باقاعدہ تصدیق

## 2. **ٹوکن سیکیورٹی اور اینٹی پاس تھرو کنٹرولز**

### **ٹوکن پاس تھرو کی روک تھام**

**MCP اجازت نامہ وضاحت میں ٹوکن پاس تھرو واضح طور پر ممنوع ہے** کیونکہ یہ سنگین سیکیورٹی خطرات کا باعث بنتا ہے:

**حل شدہ سیکیورٹی خطرات:**  
- **کنٹرول کی بائی پاسنگ**: ریٹ لمیٹنگ، درخواست کی توثیق، اور ٹریفک مانیٹرنگ جیسے اہم سیکیورٹی کنٹرولز کو بائی پاس کرتا ہے  
- **جوابدہی کا خاتمہ**: کلائنٹ کی شناخت ناممکن بناتا ہے، آڈٹ ٹریلز اور واقعہ کی تحقیقات کو خراب کرتا ہے  
- **پراکسی پر مبنی ڈیٹا چوری**: بدنیت افراد کو غیر مجاز ڈیٹا تک رسائی کے لیے سرورز کو پراکسی کے طور پر استعمال کرنے کی اجازت دیتا ہے  
- **اعتماد کی حد کی خلاف ورزیاں**: نیچے کی سروسز کے ٹوکن کے ماخذ کے بارے میں اعتماد کے مفروضات کو توڑتا ہے  
- **افقی حرکت**: متعدد سروسز میں متاثرہ ٹوکنز وسیع حملے کی توسیع کی اجازت دیتے ہیں

**نفاذ کنٹرولز:**  
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

### **محفوظ ٹوکن مینجمنٹ کے نمونے**

**بہترین طریقہ کار:**  
- **مختصر مدت کے ٹوکنز**: بار بار ٹوکن کی تبدیلی کے ساتھ نمائش کا وقت کم کریں  
- **ضرورت کے وقت جاری کرنا**: مخصوص آپریشنز کے لیے صرف ضرورت پڑنے پر ٹوکن جاری کریں  
- **محفوظ ذخیرہ**: ہارڈویئر سیکیورٹی ماڈیولز (HSMs) یا محفوظ کی والٹس کا استعمال  
- **ٹوکن بائنڈنگ**: جہاں ممکن ہو، ٹوکنز کو مخصوص کلائنٹس، سیشنز، یا آپریشنز سے منسلک کریں  
- **مانیٹرنگ اور الرٹنگ**: ٹوکن کے غلط استعمال یا غیر مجاز رسائی کے نمونوں کا حقیقی وقت میں پتہ لگانا

## 3. **سیشن سیکیورٹی کنٹرولز**

### **سیشن ہائی جیکنگ کی روک تھام**

**حملے کے راستے:**  
- **سیشن ہائی جیک پرامپٹ انجیکشن**: مشترکہ سیشن اسٹیٹ میں بدنیت واقعات کا انجیکشن  
- **سیشن امپرسونیشن**: چوری شدہ سیشن IDs کا غیر مجاز استعمال کر کے تصدیق کو بائی پاس کرنا  
- **ریزیوم ایبل اسٹریم حملے**: سرور سے بھیجے گئے ایونٹ کی بحالی کا بدنیت مواد انجیکشن کے لیے استحصال

**لازمی سیشن کنٹرولز:**  
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
  
**ٹرانسپورٹ سیکیورٹی:**  
- **HTTPS کا نفاذ**: تمام سیشن مواصلات TLS 1.3 پر  
- **محفوظ کوکی خصوصیات**: HttpOnly، Secure، SameSite=Strict  
- **سرٹیفکیٹ پننگ**: MITM حملوں کو روکنے کے لیے اہم کنکشنز کے لیے

### **اسٹیٹ فل بمقابلہ اسٹیٹ لیس غور و فکر**

**اسٹیٹ فل نفاذ کے لیے:**  
- مشترکہ سیشن اسٹیٹ کو انجیکشن حملوں سے اضافی تحفظ کی ضرورت  
- قطار پر مبنی سیشن مینجمنٹ کو سالمیت کی تصدیق کی ضرورت  
- متعدد سرور انسٹینسز کو محفوظ سیشن اسٹیٹ ہم آہنگی کی ضرورت

**اسٹیٹ لیس نفاذ کے لیے:**  
- JWT یا اسی طرح کے ٹوکن پر مبنی سیشن مینجمنٹ  
- سیشن اسٹیٹ کی سالمیت کی کرپٹوگرافک تصدیق  
- کم حملے کا دائرہ لیکن مضبوط ٹوکن کی توثیق کی ضرورت

## 4. **AI مخصوص سیکیورٹی کنٹرولز**

### **پرامپٹ انجیکشن دفاع**

**مائیکروسافٹ پرامپٹ شیلڈز انضمام:**  
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
  
**نفاذ کنٹرولز:**  
- **ان پٹ صفائی**: تمام صارف ان پٹس کی جامع توثیق اور فلٹرنگ  
- **مواد کی حد بندی کی تعریف**: نظام کی ہدایات اور صارف کے مواد کے درمیان واضح تفریق  
- **ہدایات کی درجہ بندی**: متصادم ہدایات کے لیے مناسب ترجیحی قواعد  
- **آؤٹ پٹ مانیٹرنگ**: ممکنہ نقصان دہ یا تبدیل شدہ آؤٹ پٹس کا پتہ لگانا

### **ٹول زہر آلودگی کی روک تھام**

**ٹول سیکیورٹی فریم ورک:**  
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
  
**متحرک ٹول مینجمنٹ:**  
- **منظوری کے ورک فلو**: ٹول میں تبدیلیوں کے لیے واضح صارف کی رضامندی  
- **واپس پلٹنے کی صلاحیتیں**: پچھلے ٹول ورژنز پر واپس جانے کی صلاحیت  
- **تبدیلی کی آڈٹنگ**: ٹول کی تعریف میں تبدیلیوں کی مکمل تاریخ  
- **خطرے کا جائزہ**: ٹول کی سیکیورٹی کی حالت کا خودکار جائزہ

## 5. **کنفیوژڈ ڈیپٹی حملے کی روک تھام**

### **OAuth پراکسی سیکیورٹی**

**حملے کی روک تھام کنٹرولز:**  
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
  
**نفاذ کی ضروریات:**  
- **صارف کی رضامندی کی تصدیق**: متحرک کلائنٹ رجسٹریشن کے لیے رضامندی کے اسکرینز کو کبھی نہ چھوڑیں  
- **ری ڈائریکٹ URI کی توثیق**: ری ڈائریکٹ مقامات کی سخت وائٹ لسٹ پر مبنی توثیق  
- **اجازت نامہ کوڈ کی حفاظت**: مختصر مدت کے کوڈز جن کا واحد استعمال لازمی ہو  
- **کلائنٹ شناخت کی تصدیق**: کلائنٹ اسناد اور میٹا ڈیٹا کی مضبوط توثیق

## 6. **ٹول ایگزیکیوشن سیکیورٹی**

### **سینڈ باکسنگ اور علیحدگی**

**کنٹینر پر مبنی علیحدگی:**  
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
  
**پروسیس علیحدگی:**  
- **الگ الگ پروسیس کانٹیکسٹس**: ہر ٹول ایگزیکیوشن کو علیحدہ پروسیس اسپیس میں  
- **انٹر پروسیس کمیونیکیشن**: توثیق کے ساتھ محفوظ IPC میکانزم  
- **پروسیس مانیٹرنگ**: رن ٹائم رویے کا تجزیہ اور انوملی کی شناخت  
- **وسائل کا نفاذ**: CPU، میموری، اور I/O آپریشنز پر سخت حدود

### **کم سے کم مراعات کا نفاذ**

**اجازت مینجمنٹ:**  
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
  
## 7. **سپلائی چین سیکیورٹی کنٹرولز**

### **انحصار کی توثیق**

**جامع جزو سیکیورٹی:**  
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
  
### **مسلسل مانیٹرنگ**

**سپلائی چین خطرے کی شناخت:**  
- **انحصار کی صحت کی نگرانی**: تمام انحصار کی سیکیورٹی مسائل کے لیے مسلسل جائزہ  
- **خطرے کی انٹیلی جنس انضمام**: ابھرتے ہوئے سپلائی چین خطرات پر حقیقی وقت کی اپ ڈیٹس  
- **رویے کا تجزیہ**: بیرونی اجزاء میں غیر معمولی رویے کی شناخت  
- **خودکار ردعمل**: متاثرہ اجزاء کی فوری روک تھام

## 8. **مانیٹرنگ اور شناخت کنٹرولز**

### **سیکیورٹی معلومات اور ایونٹ مینجمنٹ (SIEM)**

**جامع لاگنگ حکمت عملی:**  
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
  
### **حقیقی وقت خطرے کی شناخت**

**رویے کا تجزیہ:**  
- **صارف رویے کا تجزیہ (UBA)**: غیر معمولی صارف رسائی کے نمونوں کی شناخت  
- **ادارہ جاتی رویے کا تجزیہ (EBA)**: MCP سرور اور ٹول کے رویے کی نگرانی  
- **مشین لرننگ انوملی کی شناخت**: AI سے چلنے والی سیکیورٹی خطرات کی شناخت  
- **خطرے کی انٹیلی جنس ہم آہنگی**: مشاہدہ شدہ سرگرمیوں کا معروف حملے کے نمونوں سے میل

## 9. **واقعہ کا ردعمل اور بحالی**

### **خودکار ردعمل کی صلاحیتیں**

**فوری ردعمل کے اقدامات:**  
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
  
### **فورینزک صلاحیتیں**

**تحقیقی معاونت:**  
- **آڈٹ ٹریل کی حفاظت**: ناقابل تبدیلی لاگنگ کرپٹوگرافک سالمیت کے ساتھ  
- **ثبوت کی جمع آوری**: متعلقہ سیکیورٹی دستاویزات کا خودکار جمع کرنا  
- **ٹائم لائن کی تعمیر نو**: سیکیورٹی واقعات کی تفصیلی ترتیب  
- **اثرات کا جائزہ**: سمجھوتے کی حد اور ڈیٹا کے انکشاف کا اندازہ

## **اہم سیکیورٹی آرکیٹیکچر اصول**

### **گہرائی میں دفاع**  
- **متعدد سیکیورٹی پرتیں**: سیکیورٹی آرکیٹیکچر میں کوئی واحد ناکامی نقطہ نہیں  
- **متعدد کنٹرولز**: اہم افعال کے لیے اوورلیپنگ سیکیورٹی اقدامات  
- **فیل سیف میکانزم**: جب نظام غلطیوں یا حملوں کا سامنا کرے تو محفوظ ڈیفالٹس

### **زیرو ٹرسٹ نفاذ**  
- **کبھی اعتماد نہ کریں، ہمیشہ تصدیق کریں**: تمام اداروں اور درخواستوں کی مسلسل توثیق  
- **کم سے کم مراعات کا اصول**: تمام اجزاء کے لیے کم از کم رسائی حقوق  
- **مائیکرو سیگمنٹیشن**: باریک نیٹ ورک اور رسائی کنٹرولز

### **مسلسل سیکیورٹی ارتقاء**  
- **خطرے کے منظرنامے کی مطابقت**: ابھرتے ہوئے خطرات کو حل کرنے کے لیے باقاعدہ اپ ڈیٹس  
- **سیکیورٹی کنٹرول کی تاثیر**: کنٹرولز کی جاری جانچ اور بہتری  
- **وضاحت کی تعمیل**: MCP سیکیورٹی معیارات کے ارتقاء کے ساتھ ہم آہنگی

---

## **نفاذ کے وسائل**

### **سرکاری MCP دستاویزات**  
- [MCP وضاحت (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP سیکیورٹی بہترین طریقہ کار](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP اجازت نامہ وضاحت](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **مائیکروسافٹ سیکیورٹی حل**  
- [مائیکروسافٹ پرامپٹ شیلڈز](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [ایزور کانٹینٹ سیفٹی](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [گیٹ ہب ایڈوانسڈ سیکیورٹی](https://github.com/security/advanced-security)  
- [ایزور کی والٹ](https://learn.microsoft.com/azure/key-vault/)

### **سیکیورٹی معیارات**  
- [OAuth 2.0 سیکیورٹی بہترین طریقہ کار (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP ٹاپ 10 برائے بڑے زبان کے ماڈلز](https://genai.owasp.org/)  
- [NIST سائبر سیکیورٹی فریم ورک](https://www.nist.gov/cyberframework)

---

> **اہم**: یہ سیکیورٹی کنٹرولز موجودہ MCP وضاحت (2025-06-18) کی عکاسی کرتے ہیں۔ ہمیشہ تازہ ترین [سرکاری دستاویزات](https://spec.modelcontextprotocol.io/) کے خلاف تصدیق کریں کیونکہ معیارات تیزی سے ارتقاء پذیر ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->