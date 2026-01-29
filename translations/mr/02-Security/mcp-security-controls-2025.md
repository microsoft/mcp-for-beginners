# MCP सुरक्षा नियंत्रण - डिसेंबर 2025 अपडेट

> **सध्याचा मानक**: हा दस्तऐवज [MCP स्पेसिफिकेशन 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) सुरक्षा आवश्यकता आणि अधिकृत [MCP सुरक्षा सर्वोत्तम पद्धती](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) प्रतिबिंबित करतो.

मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) पारंपरिक सॉफ्टवेअर सुरक्षा आणि AI-विशिष्ट धोके यांना संबोधित करणाऱ्या सुधारित सुरक्षा नियंत्रणांसह लक्षणीय प्रगती केली आहे. हा दस्तऐवज डिसेंबर 2025 पर्यंत सुरक्षित MCP अंमलबजावणीसाठी सर्वसमावेशक सुरक्षा नियंत्रण प्रदान करतो.

## **अनिवार्य सुरक्षा आवश्यकता**

### **MCP स्पेसिफिकेशनमधील महत्त्वाच्या बंदी:**

> **प्रतिबंधित**: MCP सर्व्हर **कधीही स्वीकारू नयेत** असे टोकन जे स्पष्टपणे MCP सर्व्हरसाठी जारी केलेले नाहीत  
>
> **प्रतिबंधित**: MCP सर्व्हर प्रमाणीकरणासाठी सत्रे वापरू नयेत  
>
> **आवश्यक**: अधिकृतता अंमलबजावणाऱ्या MCP सर्व्हरने सर्व इनबाउंड विनंत्या तपासल्या पाहिजेत  
>
> **अनिवार्य**: स्थिर क्लायंट आयडी वापरणाऱ्या MCP प्रॉक्सी सर्व्हरने प्रत्येक गतिशील नोंदणीकृत क्लायंटसाठी वापरकर्त्याची संमती मिळवली पाहिजे

---

## 1. **प्रमाणीकरण आणि अधिकृतता नियंत्रण**

### **बाह्य ओळख प्रदाता एकत्रीकरण**

**सध्याचा MCP मानक (2025-06-18)** MCP सर्व्हरना बाह्य ओळख प्रदात्यांकडे प्रमाणीकरण सोपवण्याची परवानगी देतो, जे एक महत्त्वपूर्ण सुरक्षा सुधारणा आहे:

### **बाह्य ओळख प्रदाता एकत्रीकरण**

**सध्याचा MCP मानक (2025-11-25)** MCP सर्व्हरना बाह्य ओळख प्रदात्यांकडे प्रमाणीकरण सोपवण्याची परवानगी देतो, जे एक महत्त्वपूर्ण सुरक्षा सुधारणा आहे:

**सुरक्षा फायदे:**
1. **सानुकूल प्रमाणीकरण धोके कमी करतो**: सानुकूल प्रमाणीकरण अंमलबजावणी टाळून धोका कमी करतो  
2. **एंटरप्राइझ-ग्रेड सुरक्षा**: Microsoft Entra ID सारख्या स्थापित ओळख प्रदात्यांचा वापर करतो ज्यात प्रगत सुरक्षा वैशिष्ट्ये आहेत  
3. **केंद्रीकृत ओळख व्यवस्थापन**: वापरकर्ता जीवनचक्र व्यवस्थापन, प्रवेश नियंत्रण आणि अनुपालन ऑडिटिंग सुलभ करते  
4. **मल्टी-फॅक्टर प्रमाणीकरण**: एंटरप्राइझ ओळख प्रदात्यांकडून MFA क्षमता प्राप्त होते  
5. **सशर्त प्रवेश धोरणे**: धोका-आधारित प्रवेश नियंत्रण आणि अनुकूली प्रमाणीकरणाचा लाभ

**अंमलबजावणी आवश्यकता:**
- **टोकन प्रेक्षक पडताळणी**: सर्व टोकन स्पष्टपणे MCP सर्व्हरसाठी जारी केलेले आहेत का ते तपासा  
- **जारीकर्त्याची पडताळणी**: टोकन जारी करणारा अपेक्षित ओळख प्रदात्याशी जुळतो का ते सत्यापित करा  
- **स्वाक्षरी पडताळणी**: टोकन अखंडतेची क्रिप्टोग्राफिक पडताळणी  
- **कालबाह्यता अंमलबजावणी**: टोकनच्या आयुष्याच्या मर्यादांचे कडक पालन  
- **परिसर पडताळणी**: टोकनमध्ये विनंती केलेल्या ऑपरेशन्ससाठी योग्य परवानग्या आहेत का ते सुनिश्चित करा

### **अधिकृतता लॉजिक सुरक्षा**

**महत्त्वाचे नियंत्रण:**
- **सर्वसमावेशक अधिकृतता ऑडिट**: सर्व अधिकृतता निर्णय बिंदूंचे नियमित सुरक्षा पुनरावलोकन  
- **फेल-सेफ डीफॉल्ट्स**: अधिकृतता लॉजिक निश्चित निर्णय घेऊ शकत नसल्यास प्रवेश नाकारणे  
- **परवानगी सीमा**: वेगवेगळ्या विशेषाधिकार स्तरांमध्ये आणि संसाधन प्रवेशात स्पष्ट विभाजन  
- **ऑडिट लॉगिंग**: सुरक्षा देखरेखीकरिता सर्व अधिकृतता निर्णयांचे पूर्ण लॉगिंग  
- **नियमित प्रवेश पुनरावलोकने**: वापरकर्ता परवानग्या आणि विशेषाधिकार नियुक्तींचे कालावधीने सत्यापन

## 2. **टोकन सुरक्षा आणि अँटी-पासथ्रू नियंत्रण**

### **टोकन पासथ्रू प्रतिबंध**

**MCP अधिकृतता स्पेसिफिकेशनमध्ये टोकन पासथ्रू स्पष्टपणे प्रतिबंधित आहे** कारण त्यात गंभीर सुरक्षा धोके आहेत:

**सुरक्षा धोके:**
- **नियंत्रण टाळणे**: दर मर्यादित करणे, विनंती पडताळणी, आणि ट्रॅफिक मॉनिटरिंग सारख्या आवश्यक सुरक्षा नियंत्रणांना वगळणे  
- **जबाबदारी मोडणे**: क्लायंट ओळख शक्य नसल्यामुळे ऑडिट ट्रेल्स आणि घटनेच्या तपासणीचे भ्रष्टिकरण  
- **प्रॉक्सी-आधारित डेटा चोरी**: अनधिकृत डेटा प्रवेशासाठी सर्व्हरचा प्रॉक्सी म्हणून वापर करणे  
- **विश्वास सीमा उल्लंघन**: टोकनच्या उत्पत्तीबाबत डाउनस्ट्रीम सेवा विश्वास गहाळ करणे  
- **पार्श्वभूमी हालचाल**: अनेक सेवा ओलांडून तुटलेले टोकन वापरून मोठ्या प्रमाणावर हल्ला वाढवणे

**अंमलबजावणी नियंत्रण:**
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

### **सुरक्षित टोकन व्यवस्थापन नमुने**

**सर्वोत्तम पद्धती:**
- **लघु आयुष्याचे टोकन**: वारंवार टोकन फेरफटका करून उघडकीचा वेळ कमी करा  
- **जस्ट-इन-टाइम जारीकरण**: विशिष्ट ऑपरेशन्ससाठी आवश्यक तेव्हाच टोकन जारी करा  
- **सुरक्षित संचयन**: हार्डवेअर सुरक्षा मॉड्यूल (HSMs) किंवा सुरक्षित की वॉल्ट वापरा  
- **टोकन बाइंडिंग**: शक्य असल्यास टोकन विशिष्ट क्लायंट, सत्र किंवा ऑपरेशन्सशी बांधा  
- **मॉनिटरिंग आणि अलर्टिंग**: टोकन गैरवापर किंवा अनधिकृत प्रवेश नमुन्यांचे रिअल-टाइम शोध

## 3. **सत्र सुरक्षा नियंत्रण**

### **सत्र हायजॅकिंग प्रतिबंध**

**हल्ल्याचे मार्ग:**
- **सत्र हायजॅक प्रॉम्प्ट इंजेक्शन**: सामायिक सत्र स्थितीत दुर्भावनायुक्त घटना इंजेक्ट करणे  
- **सत्र छद्मवेश**: चोरी केलेल्या सत्र आयडीचा अनधिकृत वापर करून प्रमाणीकरण टाळणे  
- **रिसुमेबल स्ट्रीम हल्ले**: सर्व्हर-सेंड इव्हेंट पुनरारंभाचा गैरवापर करून दुर्भावनायुक्त सामग्री इंजेक्शन

**अनिवार्य सत्र नियंत्रण:**
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

**ट्रान्सपोर्ट सुरक्षा:**
- **HTTPS अंमलबजावणी**: सर्व सत्र संवाद TLS 1.3 वर  
- **सुरक्षित कुकी वैशिष्ट्ये**: HttpOnly, Secure, SameSite=Strict  
- **प्रमाणपत्र पिनिंग**: MITM हल्ल्यांपासून संरक्षणासाठी महत्त्वाच्या कनेक्शन्ससाठी

### **स्टेटफुल विरुद्ध स्टेटलेस विचार**

**स्टेटफुल अंमलबजावणीसाठी:**
- सामायिक सत्र स्थितीसाठी इंजेक्शन हल्ल्यांपासून अतिरिक्त संरक्षण आवश्यक  
- क्यू-आधारित सत्र व्यवस्थापनासाठी अखंडता पडताळणी आवश्यक  
- अनेक सर्व्हर उदाहरणांसाठी सुरक्षित सत्र स्थिती समक्रमण आवश्यक

**स्टेटलेस अंमलबजावणीसाठी:**
- JWT किंवा तत्सम टोकन-आधारित सत्र व्यवस्थापन  
- सत्र स्थिती अखंडतेची क्रिप्टोग्राफिक पडताळणी  
- कमी हल्ला पृष्ठभाग परंतु मजबूत टोकन पडताळणी आवश्यक

## 4. **AI-विशिष्ट सुरक्षा नियंत्रण**

### **प्रॉम्प्ट इंजेक्शन संरक्षण**

**Microsoft Prompt Shields एकत्रीकरण:**
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

**अंमलबजावणी नियंत्रण:**
- **इनपुट स्वच्छता**: सर्व वापरकर्ता इनपुटची सर्वसमावेशक पडताळणी आणि फिल्टरिंग  
- **सामग्री सीमा व्याख्या**: प्रणाली सूचना आणि वापरकर्ता सामग्री यामध्ये स्पष्ट विभाजन  
- **सूचना श्रेणीक्रम**: विरोधाभासी सूचनांसाठी योग्य प्राधान्य नियम  
- **आउटपुट मॉनिटरिंग**: संभाव्य हानिकारक किंवा बदललेल्या आउटपुटची शोध

### **टूल विषबाधा प्रतिबंध**

**टूल सुरक्षा फ्रेमवर्क:**
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

**डायनॅमिक टूल व्यवस्थापन:**
- **मंजुरी कार्यप्रवाह**: टूल बदलांसाठी स्पष्ट वापरकर्ता संमती  
- **रोलबॅक क्षमता**: मागील टूल आवृत्त्यांकडे परत जाण्याची क्षमता  
- **बदल ऑडिटिंग**: टूल व्याख्या बदलांचा पूर्ण इतिहास  
- **धोका मूल्यांकन**: टूल सुरक्षा स्थितीचे स्वयंचलित मूल्यांकन

## 5. **कन्फ्यूज्ड डेप्युटी हल्ला प्रतिबंध**

### **OAuth प्रॉक्सी सुरक्षा**

**हल्ला प्रतिबंध नियंत्रण:**
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

**अंमलबजावणी आवश्यकता:**
- **वापरकर्ता संमती पडताळणी**: गतिशील क्लायंट नोंदणीसाठी कधीही संमती स्क्रीन वगळू नका  
- **रिडायरेक्ट URI पडताळणी**: रिडायरेक्ट गंतव्यांची कडक व्हाइटलिस्ट-आधारित पडताळणी  
- **अधिकृतता कोड संरक्षण**: लघु आयुष्याचे कोड आणि एकदाच वापर अंमलबजावणी  
- **क्लायंट ओळख पडताळणी**: क्लायंट क्रेडेन्शियल्स आणि मेटाडेटाची मजबूत पडताळणी

## 6. **टूल अंमलबजावणी सुरक्षा**

### **सँडबॉक्सिंग आणि पृथक्करण**

**कंटेनर-आधारित पृथक्करण:**
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

**प्रक्रिया पृथक्करण:**
- **वेगळे प्रक्रिया संदर्भ**: प्रत्येक टूल अंमलबजावणी स्वतंत्र प्रक्रिया जागेत  
- **इंटर-प्रोसेस कम्युनिकेशन**: पडताळणीसह सुरक्षित IPC यंत्रणा  
- **प्रक्रिया मॉनिटरिंग**: रनटाइम वर्तन विश्लेषण आणि अपवाद शोध  
- **संसाधन अंमलबजावणी**: CPU, मेमरी, आणि I/O ऑपरेशन्सवर कडक मर्यादा

### **कमी विशेषाधिकार अंमलबजावणी**

**परवानगी व्यवस्थापन:**
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

## 7. **पुरवठा साखळी सुरक्षा नियंत्रण**

### **आश्रितता पडताळणी**

**सर्वसमावेशक घटक सुरक्षा:**
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

### **सतत मॉनिटरिंग**

**पुरवठा साखळी धोका शोध:**
- **आश्रितता आरोग्य मॉनिटरिंग**: सर्व आश्रिततांवर सुरक्षा समस्या यासाठी सतत मूल्यांकन  
- **धोका बुद्धिमत्ता एकत्रीकरण**: उदयोन्मुख पुरवठा साखळी धोके यावर रिअल-टाइम अपडेट्स  
- **वर्तन विश्लेषण**: बाह्य घटकांमधील असामान्य वर्तन शोध  
- **स्वयंचलित प्रतिसाद**: तुटलेल्या घटकांचे त्वरित प्रतिबंध

## 8. **मॉनिटरिंग आणि शोध नियंत्रण**

### **सुरक्षा माहिती आणि घटना व्यवस्थापन (SIEM)**

**सर्वसमावेशक लॉगिंग धोरण:**
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

### **रिअल-टाइम धोका शोध**

**वर्तन विश्लेषण:**
- **वापरकर्ता वर्तन विश्लेषण (UBA)**: असामान्य वापरकर्ता प्रवेश नमुने शोधणे  
- **घटक वर्तन विश्लेषण (EBA)**: MCP सर्व्हर आणि टूल वर्तनाचे निरीक्षण  
- **मशीन लर्निंग अपवाद शोध**: AI-चालित सुरक्षा धोके ओळखणे  
- **धोका बुद्धिमत्ता सुसंगती**: ज्ञात हल्ला नमुन्यांशी निरीक्षित क्रियाकलापांची जुळणी

## 9. **घटना प्रतिसाद आणि पुनर्प्राप्ती**

### **स्वयंचलित प्रतिसाद क्षमता**

**तत्काळ प्रतिसाद क्रिया:**
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

### **फॉरेन्सिक क्षमता**

**तपास समर्थन:**
- **ऑडिट ट्रेल संरक्षण**: क्रिप्टोग्राफिक अखंडतेसह अपरिवर्तनीय लॉगिंग  
- **पुरावे संकलन**: संबंधित सुरक्षा पुरावे स्वयंचलित संकलन  
- **कालरेषा पुनर्निर्मिती**: सुरक्षा घटनांकडे नेणाऱ्या घटनांची सविस्तर अनुक्रमणिका  
- **प्रभाव मूल्यांकन**: तुटलेले प्रमाण आणि डेटा उघडकीचे मूल्यमापन

## **महत्त्वाचे सुरक्षा आर्किटेक्चर तत्त्वे**

### **गहन संरक्षण**
- **अनेक सुरक्षा स्तर**: सुरक्षा आर्किटेक्चरमध्ये एकही एकल बिंदू अपयशासाठी नाही  
- **अतिरिक्त नियंत्रण**: महत्त्वाच्या कार्यांसाठी ओव्हरलॅपिंग सुरक्षा उपाय  
- **फेल-सेफ यंत्रणा**: प्रणाली त्रुटी किंवा हल्ल्यांमध्ये सुरक्षित डीफॉल्ट्स

### **झिरो ट्रस्ट अंमलबजावणी**
- **कधीही विश्वास ठेवू नका, नेहमी पडताळणी करा**: सर्व घटक आणि विनंत्यांची सतत पडताळणी  
- **कमी विशेषाधिकार तत्त्व**: सर्व घटकांसाठी किमान प्रवेश अधिकार  
- **मायक्रो-सेगमेंटेशन**: सूक्ष्म नेटवर्क आणि प्रवेश नियंत्रण

### **सतत सुरक्षा विकास**
- **धोका परिदृश्य अनुकूलन**: उदयोन्मुख धोके हाताळण्यासाठी नियमित अद्यतने  
- **सुरक्षा नियंत्रण प्रभावीपणा**: नियंत्रणांचे सतत मूल्यांकन आणि सुधारणा  
- **स्पेसिफिकेशन अनुपालन**: विकसित होणाऱ्या MCP सुरक्षा मानकांशी सुसंगतता

---

## **अंमलबजावणी संसाधने**

### **अधिकृत MCP दस्तऐवज**
- [MCP स्पेसिफिकेशन (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP सुरक्षा सर्वोत्तम पद्धती](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP अधिकृतता स्पेसिफिकेशन](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft सुरक्षा उपाय**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **सुरक्षा मानके**
- [OAuth 2.0 सुरक्षा सर्वोत्तम पद्धती (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP टॉप 10 फॉर लार्ज लँग्वेज मॉडेल्स](https://genai.owasp.org/)
- [NIST सायबरसुरक्षा फ्रेमवर्क](https://www.nist.gov/cyberframework)

---

> **महत्त्वाचे**: हे सुरक्षा नियंत्रण सध्याच्या MCP स्पेसिफिकेशन (2025-06-18) प्रतिबिंबित करतात. मानके जलद विकसित होत असल्याने नेहमी [अधिकृत दस्तऐवज](https://spec.modelcontextprotocol.io/) तपासा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->