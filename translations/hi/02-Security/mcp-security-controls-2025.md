# MCP सुरक्षा नियंत्रण - दिसंबर 2025 अपडेट

> **वर्तमान मानक**: यह दस्तावेज़ [MCP विनिर्देशन 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) सुरक्षा आवश्यकताओं और आधिकारिक [MCP सुरक्षा सर्वोत्तम प्रथाओं](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) को दर्शाता है।

मॉडल कॉन्टेक्स्ट प्रोटोकॉल (MCP) ने पारंपरिक सॉफ़्टवेयर सुरक्षा और AI-विशिष्ट खतरों दोनों को संबोधित करते हुए उन्नत सुरक्षा नियंत्रणों के साथ महत्वपूर्ण प्रगति की है। यह दस्तावेज़ दिसंबर 2025 तक सुरक्षित MCP कार्यान्वयन के लिए व्यापक सुरक्षा नियंत्रण प्रदान करता है।

## **अनिवार्य सुरक्षा आवश्यकताएँ**

### **MCP विनिर्देशन से महत्वपूर्ण निषेध:**

> **प्रतिबंधित**: MCP सर्वर **कभी भी स्वीकार नहीं कर सकते** ऐसे टोकन जो स्पष्ट रूप से MCP सर्वर के लिए जारी नहीं किए गए हों  
>
> **प्रतिबंधित**: MCP सर्वर प्रमाणीकरण के लिए सत्रों का उपयोग **नहीं कर सकते**  
>
> **आवश्यक**: MCP सर्वर जो प्राधिकरण लागू करते हैं, **सभी इनबाउंड अनुरोधों का सत्यापन करना चाहिए**  
>
> **अनिवार्य**: स्थिर क्लाइंट आईडी का उपयोग करने वाले MCP प्रॉक्सी सर्वर को प्रत्येक गतिशील रूप से पंजीकृत क्लाइंट के लिए उपयोगकर्ता की सहमति प्राप्त करनी चाहिए

---

## 1. **प्रमाणीकरण और प्राधिकरण नियंत्रण**

### **बाहरी पहचान प्रदाता एकीकरण**

**वर्तमान MCP मानक (2025-06-18)** MCP सर्वरों को प्रमाणीकरण को बाहरी पहचान प्रदाताओं को सौंपने की अनुमति देता है, जो एक महत्वपूर्ण सुरक्षा सुधार है:

### **बाहरी पहचान प्रदाता एकीकरण**

**वर्तमान MCP मानक (2025-11-25)** MCP सर्वरों को प्रमाणीकरण को बाहरी पहचान प्रदाताओं को सौंपने की अनुमति देता है, जो एक महत्वपूर्ण सुरक्षा सुधार है:

**सुरक्षा लाभ:**
1. **कस्टम प्रमाणीकरण जोखिम समाप्त करता है**: कस्टम प्रमाणीकरण कार्यान्वयन से बचकर जोखिम सतह को कम करता है  
2. **एंटरप्राइज़-ग्रेड सुरक्षा**: Microsoft Entra ID जैसे स्थापित पहचान प्रदाताओं का उपयोग करता है जिनमें उन्नत सुरक्षा विशेषताएं हैं  
3. **केंद्रीकृत पहचान प्रबंधन**: उपयोगकर्ता जीवनचक्र प्रबंधन, पहुंच नियंत्रण, और अनुपालन ऑडिटिंग को सरल बनाता है  
4. **मल्टी-फैक्टर प्रमाणीकरण**: एंटरप्राइज़ पहचान प्रदाताओं से MFA क्षमताएं प्राप्त करता है  
5. **सशर्त पहुंच नीतियां**: जोखिम-आधारित पहुंच नियंत्रण और अनुकूली प्रमाणीकरण से लाभान्वित होता है

**कार्यान्वयन आवश्यकताएँ:**
- **टोकन ऑडियंस सत्यापन**: सभी टोकन स्पष्ट रूप से MCP सर्वर के लिए जारी किए गए हैं यह सत्यापित करें  
- **जारीकर्ता सत्यापन**: टोकन जारीकर्ता अपेक्षित पहचान प्रदाता से मेल खाता है यह सत्यापित करें  
- **हस्ताक्षर सत्यापन**: टोकन की अखंडता का क्रिप्टोग्राफिक सत्यापन  
- **समाप्ति प्रवर्तन**: टोकन जीवनकाल सीमाओं का कड़ाई से पालन  
- **स्कोप सत्यापन**: सुनिश्चित करें कि टोकन में अनुरोधित संचालन के लिए उपयुक्त अनुमतियाँ हैं

### **प्राधिकरण तर्क सुरक्षा**

**महत्वपूर्ण नियंत्रण:**
- **व्यापक प्राधिकरण ऑडिट**: सभी प्राधिकरण निर्णय बिंदुओं की नियमित सुरक्षा समीक्षा  
- **फेल-सेफ डिफ़ॉल्ट**: जब प्राधिकरण तर्क स्पष्ट निर्णय नहीं कर पाता तो पहुंच अस्वीकृत करें  
- **अनुमति सीमाएं**: विभिन्न विशेषाधिकार स्तरों और संसाधन पहुंच के बीच स्पष्ट विभाजन  
- **ऑडिट लॉगिंग**: सुरक्षा निगरानी के लिए सभी प्राधिकरण निर्णयों का पूर्ण लॉगिंग  
- **नियमित पहुंच समीक्षा**: उपयोगकर्ता अनुमतियों और विशेषाधिकार असाइनमेंट का आवधिक सत्यापन

## 2. **टोकन सुरक्षा और एंटी-पासथ्रू नियंत्रण**

### **टोकन पासथ्रू रोकथाम**

**MCP प्राधिकरण विनिर्देशन में टोकन पासथ्रू स्पष्ट रूप से निषिद्ध है** क्योंकि यह गंभीर सुरक्षा जोखिम उत्पन्न करता है:

**सुरक्षा जोखिम जो संबोधित किए गए हैं:**
- **नियंत्रण परिहार**: आवश्यक सुरक्षा नियंत्रण जैसे दर सीमा, अनुरोध सत्यापन, और ट्रैफ़िक निगरानी को बायपास करता है  
- **जवाबदेही टूटना**: क्लाइंट पहचान असंभव बनाता है, ऑडिट ट्रेल और घटना जांच को भ्रष्ट करता है  
- **प्रॉक्सी-आधारित डेटा चोरी**: दुर्भावनापूर्ण अभिनेताओं को सर्वरों का उपयोग अनधिकृत डेटा पहुंच के लिए प्रॉक्सी के रूप में करने की अनुमति देता है  
- **ट्रस्ट सीमा उल्लंघन**: डाउनस्ट्रीम सेवा के टोकन मूल के ट्रस्ट अनुमानों को तोड़ता है  
- **पार्श्व आंदोलन**: कई सेवाओं में समझौता किए गए टोकन व्यापक हमले का विस्तार सक्षम करते हैं

**कार्यान्वयन नियंत्रण:**
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

### **सुरक्षित टोकन प्रबंधन पैटर्न**

**सर्वोत्तम प्रथाएं:**
- **अल्पकालिक टोकन**: बार-बार टोकन रोटेशन के साथ जोखिम विंडो को न्यूनतम करें  
- **जरूरत के समय जारी करना**: केवल विशिष्ट संचालन के लिए आवश्यक होने पर टोकन जारी करें  
- **सुरक्षित भंडारण**: हार्डवेयर सुरक्षा मॉड्यूल (HSM) या सुरक्षित कुंजी वॉल्ट का उपयोग करें  
- **टोकन बाइंडिंग**: जहां संभव हो, टोकन को विशिष्ट क्लाइंट, सत्र, या संचालन से बांधें  
- **निगरानी और अलर्टिंग**: टोकन दुरुपयोग या अनधिकृत पहुंच पैटर्न का वास्तविक समय पता लगाना

## 3. **सत्र सुरक्षा नियंत्रण**

### **सत्र अपहरण रोकथाम**

**संबोधित हमले के वेक्टर:**
- **सत्र अपहरण प्रॉम्प्ट इंजेक्शन**: साझा सत्र स्थिति में दुर्भावनापूर्ण घटनाओं का इंजेक्शन  
- **सत्र छद्मवेश**: चोरी हुए सत्र आईडी का अनधिकृत उपयोग प्रमाणीकरण को बायपास करने के लिए  
- **पुनः आरंभ योग्य स्ट्रीम हमले**: सर्वर-संप्रेषित घटना पुनः आरंभ का दुरुपयोग दुर्भावनापूर्ण सामग्री इंजेक्शन के लिए

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

**ट्रांसपोर्ट सुरक्षा:**
- **HTTPS प्रवर्तन**: सभी सत्र संचार TLS 1.3 पर  
- **सुरक्षित कुकी विशेषताएं**: HttpOnly, Secure, SameSite=Strict  
- **प्रमाणपत्र पिनिंग**: MITM हमलों को रोकने के लिए महत्वपूर्ण कनेक्शनों के लिए

### **राज्यपूर्ण बनाम राज्यहीन विचार**

**राज्यपूर्ण कार्यान्वयन के लिए:**
- साझा सत्र स्थिति को इंजेक्शन हमलों से अतिरिक्त सुरक्षा की आवश्यकता होती है  
- कतार-आधारित सत्र प्रबंधन को अखंडता सत्यापन की आवश्यकता होती है  
- कई सर्वर उदाहरणों को सुरक्षित सत्र स्थिति समन्वयन की आवश्यकता होती है

**राज्यहीन कार्यान्वयन के लिए:**
- JWT या समान टोकन-आधारित सत्र प्रबंधन  
- सत्र स्थिति अखंडता का क्रिप्टोग्राफिक सत्यापन  
- कम हमला सतह लेकिन मजबूत टोकन सत्यापन आवश्यक

## 4. **AI-विशिष्ट सुरक्षा नियंत्रण**

### **प्रॉम्प्ट इंजेक्शन रक्षा**

**Microsoft प्रॉम्प्ट शील्ड्स एकीकरण:**
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

**कार्यान्वयन नियंत्रण:**
- **इनपुट सैनिटाइजेशन**: सभी उपयोगकर्ता इनपुट का व्यापक सत्यापन और फ़िल्टरिंग  
- **सामग्री सीमा परिभाषा**: सिस्टम निर्देशों और उपयोगकर्ता सामग्री के बीच स्पष्ट विभाजन  
- **निर्देश पदानुक्रम**: विरोधाभासी निर्देशों के लिए उचित प्राथमिकता नियम  
- **आउटपुट निगरानी**: संभावित हानिकारक या हेरफेर किए गए आउटपुट का पता लगाना

### **टूल विषाक्तता रोकथाम**

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

**गतिशील टूल प्रबंधन:**
- **स्वीकृति कार्यप्रवाह**: टूल संशोधनों के लिए स्पष्ट उपयोगकर्ता सहमति  
- **रोलबैक क्षमताएं**: पिछले टूल संस्करणों पर वापस जाने की क्षमता  
- **परिवर्तन ऑडिटिंग**: टूल परिभाषा संशोधनों का पूर्ण इतिहास  
- **जोखिम मूल्यांकन**: टूल सुरक्षा स्थिति का स्वचालित मूल्यांकन

## 5. **कन्फ्यूज्ड डिप्टी हमला रोकथाम**

### **OAuth प्रॉक्सी सुरक्षा**

**हमला रोकथाम नियंत्रण:**
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

**कार्यान्वयन आवश्यकताएँ:**
- **उपयोगकर्ता सहमति सत्यापन**: गतिशील क्लाइंट पंजीकरण के लिए सहमति स्क्रीन कभी न छोड़ें  
- **रिडायरेक्ट URI सत्यापन**: रिडायरेक्ट गंतव्यों का कड़ाई से श्वेतसूची-आधारित सत्यापन  
- **प्राधिकरण कोड सुरक्षा**: अल्पकालिक कोड जिनका एकल उपयोग प्रवर्तन हो  
- **क्लाइंट पहचान सत्यापन**: क्लाइंट क्रेडेंशियल और मेटाडेटा का मजबूत सत्यापन

## 6. **टूल निष्पादन सुरक्षा**

### **सैंडबॉक्सिंग और पृथक्करण**

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
- **अलग प्रक्रिया संदर्भ**: प्रत्येक टूल निष्पादन अलग प्रक्रिया स्थान में  
- **इंटर-प्रोसेस संचार**: सत्यापन के साथ सुरक्षित IPC तंत्र  
- **प्रक्रिया निगरानी**: रनटाइम व्यवहार विश्लेषण और असामान्यता पता लगाना  
- **संसाधन प्रवर्तन**: CPU, मेमोरी, और I/O संचालन पर कड़े सीमाएं

### **न्यूनतम विशेषाधिकार कार्यान्वयन**

**अनुमति प्रबंधन:**
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

## 7. **सप्लाई चेन सुरक्षा नियंत्रण**

### **निर्भरता सत्यापन**

**व्यापक घटक सुरक्षा:**
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

### **निरंतर निगरानी**

**सप्लाई चेन खतरा पता लगाना:**
- **निर्भरता स्वास्थ्य निगरानी**: सभी निर्भरताओं का सुरक्षा मुद्दों के लिए निरंतर मूल्यांकन  
- **खतरा खुफिया एकीकरण**: उभरते सप्लाई चेन खतरों पर वास्तविक समय अपडेट  
- **व्यवहार विश्लेषण**: बाहरी घटकों में असामान्य व्यवहार का पता लगाना  
- **स्वचालित प्रतिक्रिया**: समझौता किए गए घटकों का त्वरित नियंत्रण

## 8. **निगरानी और पता लगाने के नियंत्रण**

### **सुरक्षा सूचना और घटना प्रबंधन (SIEM)**

**व्यापक लॉगिंग रणनीति:**
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

### **रियल-टाइम खतरा पता लगाना**

**व्यवहार विश्लेषिकी:**
- **उपयोगकर्ता व्यवहार विश्लेषिकी (UBA)**: असामान्य उपयोगकर्ता पहुंच पैटर्न का पता लगाना  
- **इकाई व्यवहार विश्लेषिकी (EBA)**: MCP सर्वर और टूल व्यवहार की निगरानी  
- **मशीन लर्निंग असामान्यता पता लगाना**: AI-संचालित सुरक्षा खतरों की पहचान  
- **खतरा खुफिया सहसंबंध**: ज्ञात हमले पैटर्न के खिलाफ देखी गई गतिविधियों का मिलान

## 9. **घटना प्रतिक्रिया और पुनर्प्राप्ति**

### **स्वचालित प्रतिक्रिया क्षमताएं**

**तत्काल प्रतिक्रिया क्रियाएं:**
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

### **फोरेंसिक क्षमताएं**

**जांच समर्थन:**
- **ऑडिट ट्रेल संरक्षण**: अपरिवर्तनीय लॉगिंग क्रिप्टोग्राफिक अखंडता के साथ  
- **साक्ष्य संग्रह**: संबंधित सुरक्षा अभिलेखों का स्वचालित संग्रह  
- **समयरेखा पुनर्निर्माण**: सुरक्षा घटनाओं की विस्तृत घटनाक्रम  
- **प्रभाव मूल्यांकन**: समझौते के दायरे और डेटा प्रकटीकरण का मूल्यांकन

## **प्रमुख सुरक्षा वास्तुकला सिद्धांत**

### **गहराई में रक्षा**
- **कई सुरक्षा परतें**: सुरक्षा वास्तुकला में कोई एकल विफलता बिंदु नहीं  
- **अतिरिक्त नियंत्रण**: महत्वपूर्ण कार्यों के लिए ओवरलैपिंग सुरक्षा उपाय  
- **फेल-सेफ तंत्र**: जब सिस्टम त्रुटियों या हमलों का सामना करते हैं तो सुरक्षित डिफ़ॉल्ट

### **शून्य ट्रस्ट कार्यान्वयन**
- **कभी भरोसा न करें, हमेशा सत्यापित करें**: सभी इकाइयों और अनुरोधों का निरंतर सत्यापन  
- **न्यूनतम विशेषाधिकार सिद्धांत**: सभी घटकों के लिए न्यूनतम पहुंच अधिकार  
- **माइक्रो-सेगमेंटेशन**: सूक्ष्म नेटवर्क और पहुंच नियंत्रण

### **निरंतर सुरक्षा विकास**
- **खतरा परिदृश्य अनुकूलन**: उभरते खतरों को संबोधित करने के लिए नियमित अपडेट  
- **सुरक्षा नियंत्रण प्रभावशीलता**: नियंत्रणों का निरंतर मूल्यांकन और सुधार  
- **विनिर्देशन अनुपालन**: विकसित हो रहे MCP सुरक्षा मानकों के साथ संरेखण

---

## **कार्यान्वयन संसाधन**

### **आधिकारिक MCP दस्तावेज़ीकरण**
- [MCP विनिर्देशन (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP सुरक्षा सर्वोत्तम प्रथाएं](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP प्राधिकरण विनिर्देशन](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft सुरक्षा समाधान**
- [Microsoft प्रॉम्प्ट शील्ड्स](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure कंटेंट सेफ्टी](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub उन्नत सुरक्षा](https://github.com/security/advanced-security)
- [Azure की वॉल्ट](https://learn.microsoft.com/azure/key-vault/)

### **सुरक्षा मानक**
- [OAuth 2.0 सुरक्षा सर्वोत्तम प्रथाएं (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [बड़े भाषा मॉडल के लिए OWASP टॉप 10](https://genai.owasp.org/)
- [NIST साइबरसुरक्षा फ्रेमवर्क](https://www.nist.gov/cyberframework)

---

> **महत्वपूर्ण**: ये सुरक्षा नियंत्रण वर्तमान MCP विनिर्देशन (2025-06-18) को दर्शाते हैं। नवीनतम [आधिकारिक दस्तावेज़ीकरण](https://spec.modelcontextprotocol.io/) के खिलाफ हमेशा सत्यापित करें क्योंकि मानक तेजी से विकसित हो रहे हैं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->