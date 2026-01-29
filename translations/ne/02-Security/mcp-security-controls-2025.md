# MCP सुरक्षा नियन्त्रणहरू - डिसेम्बर २०२५ अपडेट

> **हालको मापदण्ड**: यो दस्तावेजले [MCP विनिर्देशन २०२५-११-२५](https://spec.modelcontextprotocol.io/specification/2025-11-25/) सुरक्षा आवश्यकताहरू र आधिकारिक [MCP सुरक्षा उत्तम अभ्यासहरू](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) प्रतिबिम्बित गर्दछ।

मोडेल कन्टेक्स्ट प्रोटोकल (MCP) ले परम्परागत सफ्टवेयर सुरक्षा र AI-विशिष्ट खतराहरूलाई सम्बोधन गर्ने उन्नत सुरक्षा नियन्त्रणहरूसँग महत्वपूर्ण प्रगति गरेको छ। यो दस्तावेजले डिसेम्बर २०२५ सम्म सुरक्षित MCP कार्यान्वयनहरूको लागि व्यापक सुरक्षा नियन्त्रणहरू प्रदान गर्दछ।

## **अनिवार्य सुरक्षा आवश्यकताहरू**

### **MCP विनिर्देशनबाट महत्वपूर्ण निषेधहरू:**

> **निषेधित**: MCP सर्भरहरूले **कुनै पनि टोकनहरू स्वीकार गर्नु हुँदैन जुन स्पष्ट रूपमा MCP सर्भरका लागि जारी गरिएको छैनन्**  
>
> **प्रतिबन्धित**: MCP सर्भरहरूले प्रमाणीकरणका लागि सत्रहरू प्रयोग गर्नु हुँदैन  
>
> **आवश्यक**: MCP सर्भरहरूले प्राधिकरण कार्यान्वयन गर्दा **सबै इनबाउन्ड अनुरोधहरू जाँच गर्नैपर्छ**  
>
> **अनिवार्य**: स्थिर क्लाइन्ट ID प्रयोग गर्ने MCP प्रोक्सी सर्भरहरूले प्रत्येक गतिशील रूपमा दर्ता गरिएको क्लाइन्टको लागि प्रयोगकर्ता सहमति प्राप्त गर्नैपर्छ

---

## १. **प्रमाणीकरण र प्राधिकरण नियन्त्रणहरू**

### **बाह्य पहिचान प्रदायक एकीकरण**

**हालको MCP मापदण्ड (२०२५-०६-१८)** ले MCP सर्भरहरूलाई प्रमाणीकरण बाह्य पहिचान प्रदायकहरूलाई सुम्पन अनुमति दिन्छ, जुन महत्वपूर्ण सुरक्षा सुधार हो:

### **बाह्य पहिचान प्रदायक एकीकरण**

**हालको MCP मापदण्ड (२०२५-११-२५)** ले MCP सर्भरहरूलाई प्रमाणीकरण बाह्य पहिचान प्रदायकहरूलाई सुम्पन अनुमति दिन्छ, जुन महत्वपूर्ण सुरक्षा सुधार हो:

**सुरक्षा लाभहरू:**
१. **अनुकूलित प्रमाणीकरण जोखिमहरू हटाउँछ**: अनुकूलित प्रमाणीकरण कार्यान्वयनहरूबाट जोखिम सतह घटाउँछ  
२. **उद्यम-स्तर सुरक्षा**: Microsoft Entra ID जस्ता स्थापित पहिचान प्रदायकहरूको उन्नत सुरक्षा सुविधाहरू प्रयोग गर्दछ  
३. **केन्द्रित पहिचान व्यवस्थापन**: प्रयोगकर्ता जीवनचक्र व्यवस्थापन, पहुँच नियन्त्रण, र अनुपालन अडिटिङ सरल बनाउँछ  
४. **बहु-कारक प्रमाणीकरण**: उद्यम पहिचान प्रदायकहरूबाट MFA क्षमता प्राप्त गर्दछ  
५. **सशर्त पहुँच नीतिहरू**: जोखिम-आधारित पहुँच नियन्त्रण र अनुकूली प्रमाणीकरणबाट लाभ उठाउँछ

**कार्यान्वयन आवश्यकताहरू:**
- **टोकन दर्शक प्रमाणीकरण**: सबै टोकनहरू स्पष्ट रूपमा MCP सर्भरका लागि जारी गरिएको छ कि छैन जाँच गर्नुहोस्  
- **जारीकर्ता प्रमाणीकरण**: टोकन जारीकर्ताले अपेक्षित पहिचान प्रदायकसँग मेल खान्छ कि छैन प्रमाणित गर्नुहोस्  
- **हस्ताक्षर प्रमाणीकरण**: टोकन अखण्डताको क्रिप्टोग्राफिक प्रमाणीकरण  
- **समाप्ति लागू गर्नुहोस्**: टोकनको जीवनकाल सीमा कडाइका साथ लागू गर्नुहोस्  
- **स्कोप प्रमाणीकरण**: टोकनहरूले अनुरोध गरिएका अपरेसनहरूको लागि उपयुक्त अनुमति समावेश गरेको सुनिश्चित गर्नुहोस्

### **प्राधिकरण तर्क सुरक्षा**

**महत्वपूर्ण नियन्त्रणहरू:**
- **व्यापक प्राधिकरण अडिटहरू**: सबै प्राधिकरण निर्णय बिन्दुहरूको नियमित सुरक्षा समीक्षा  
- **फेल-सेफ पूर्वनिर्धारित मानहरू**: प्राधिकरण तर्कले निश्चित निर्णय गर्न नसक्दा पहुँच अस्वीकृत गर्नुहोस्  
- **अनुमति सीमाहरू**: विभिन्न विशेषाधिकार स्तर र स्रोत पहुँच बीच स्पष्ट विभाजन  
- **अडिट लगिङ**: सुरक्षा अनुगमनका लागि सबै प्राधिकरण निर्णयहरूको पूर्ण लगिङ  
- **नियमित पहुँच समीक्षा**: प्रयोगकर्ता अनुमतिहरू र विशेषाधिकार असाइनमेन्टहरूको आवधिक प्रमाणीकरण

## २. **टोकन सुरक्षा र एन्टी-पासथ्रू नियन्त्रणहरू**

### **टोकन पासथ्रू रोकथाम**

**MCP प्राधिकरण विनिर्देशनमा टोकन पासथ्रू स्पष्ट रूपमा निषेध गरिएको छ** किनभने यसले महत्वपूर्ण सुरक्षा जोखिमहरू निम्त्याउँछ:

**समाधान गरिएका सुरक्षा जोखिमहरू:**
- **नियन्त्रण बाइपास**: दर सीमांकन, अनुरोध प्रमाणीकरण, र ट्राफिक अनुगमन जस्ता आवश्यक सुरक्षा नियन्त्रणहरू बाइपास गर्दछ  
- **जवाफदेहिता विफलता**: क्लाइन्ट पहिचान असम्भव बनाउँछ, जसले अडिट ट्रेल र घटना अनुसन्धानलाई भ्रष्ट पार्छ  
- **प्रोक्सी-आधारित डाटा चोरी**: दुष्ट व्यक्तिहरूलाई सर्भरहरूलाई अनधिकृत डाटा पहुँचका लागि प्रोक्सीको रूपमा प्रयोग गर्न सक्षम बनाउँछ  
- **विश्वास सीमा उल्लंघन**: टोकन उत्पत्तिको बारेमा डाउनस्ट्रीम सेवाहरूको विश्वास मान्यताहरू तोड्छ  
- **पार्श्वगत आन्दोलन**: धेरै सेवाहरूमा सम्झौता गरिएको टोकनहरूले व्यापक आक्रमण विस्तार सक्षम पार्छ

**कार्यान्वयन नियन्त्रणहरू:**
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

### **सुरक्षित टोकन व्यवस्थापन ढाँचाहरू**

**उत्तम अभ्यासहरू:**
- **छोटो अवधिका टोकनहरू**: बारम्बार टोकन रोटेसनले जोखिम खुल्ने समय कम गर्नुहोस्  
- **ठिक समयमा जारी गर्नुहोस्**: विशेष अपरेसनहरूको लागि मात्र आवश्यक पर्दा टोकन जारी गर्नुहोस्  
- **सुरक्षित भण्डारण**: हार्डवेयर सुरक्षा मोड्युल (HSM) वा सुरक्षित कुञ्जी भण्डारहरू प्रयोग गर्नुहोस्  
- **टोकन बाइन्डिङ**: सम्भव भएमा टोकनहरूलाई विशिष्ट क्लाइन्ट, सत्र, वा अपरेसनसँग बाँध्नुहोस्  
- **अनुगमन र सचेतना**: टोकन दुरुपयोग वा अनधिकृत पहुँच ढाँचाहरूको वास्तविक-समय पत्ता लगाउने

## ३. **सत्र सुरक्षा नियन्त्रणहरू**

### **सत्र अपहरण रोकथाम**

**समाधान गरिएका आक्रमण मार्गहरू:**
- **सत्र अपहरण प्रॉम्प्ट इन्जेक्शन**: साझा सत्र अवस्थामाथि दुष्ट घटनाहरू इन्जेक्ट गरिन्छ  
- **सत्र नक्कलीकरण**: चोरी गरिएको सत्र ID को अनधिकृत प्रयोगले प्रमाणीकरण बाइपास गर्दछ  
- **पुनः सुरु गर्न मिल्ने स्ट्रिम आक्रमणहरू**: सर्भर-प्रेषित घटना पुनः सुरु गरेर दुष्ट सामग्री इन्जेक्शन

**अनिवार्य सत्र नियन्त्रणहरू:**
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
- **HTTPS लागू गर्नुहोस्**: सबै सत्र सञ्चार TLS 1.3 मार्फत  
- **सुरक्षित कुकी विशेषताहरू**: HttpOnly, Secure, SameSite=Strict  
- **प्रमाणपत्र पिनिङ**: MITM आक्रमण रोक्न महत्वपूर्ण जडानहरूको लागि

### **राज्यपूर्ण बनाम राज्यरहित विचारहरू**

**राज्यपूर्ण कार्यान्वयनहरूको लागि:**
- साझा सत्र अवस्थाले इन्जेक्शन आक्रमणहरू विरुद्ध थप सुरक्षा आवश्यक छ  
- क्यू-आधारित सत्र व्यवस्थापनले अखण्डता प्रमाणीकरण आवश्यक छ  
- धेरै सर्भर उदाहरणहरूले सुरक्षित सत्र अवस्था समक्रमण आवश्यक छ

**राज्यरहित कार्यान्वयनहरूको लागि:**
- JWT वा समान टोकन-आधारित सत्र व्यवस्थापन  
- सत्र अवस्थाको क्रिप्टोग्राफिक प्रमाणीकरण  
- आक्रमण सतह कम हुन्छ तर बलियो टोकन प्रमाणीकरण आवश्यक छ

## ४. **AI-विशिष्ट सुरक्षा नियन्त्रणहरू**

### **प्रॉम्प्ट इन्जेक्शन रक्षा**

**Microsoft प्रॉम्प्ट शिल्ड्स एकीकरण:**
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

**कार्यान्वयन नियन्त्रणहरू:**
- **इनपुट सफाई**: सबै प्रयोगकर्ता इनपुटहरूको व्यापक प्रमाणीकरण र फिल्टरिङ  
- **सामग्री सीमा परिभाषा**: प्रणाली निर्देशन र प्रयोगकर्ता सामग्री बीच स्पष्ट विभाजन  
- **निर्देशन पदानुक्रम**: विरोधाभासी निर्देशनहरूको लागि उचित प्राथमिकता नियमहरू  
- **आउटपुट अनुगमन**: सम्भावित हानिकारक वा परिमार्जित आउटपुटहरूको पत्ता लगाउने

### **उपकरण विषाक्तता रोकथाम**

**उपकरण सुरक्षा फ्रेमवर्क:**
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

**गतिशील उपकरण व्यवस्थापन:**
- **स्वीकृति कार्यप्रवाहहरू**: उपकरण संशोधनहरूको लागि स्पष्ट प्रयोगकर्ता सहमति  
- **रोलब्याक क्षमता**: अघिल्लो उपकरण संस्करणमा फर्कन सक्ने क्षमता  
- **परिवर्तन अडिटिङ**: उपकरण परिभाषा संशोधनहरूको पूर्ण इतिहास  
- **जोखिम मूल्याङ्कन**: उपकरण सुरक्षा अवस्थाको स्वचालित मूल्याङ्कन

## ५. **कन्फ्युज्ड डेप्युटी आक्रमण रोकथाम**

### **OAuth प्रोक्सी सुरक्षा**

**आक्रमण रोकथाम नियन्त्रणहरू:**
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

**कार्यान्वयन आवश्यकताहरू:**
- **प्रयोगकर्ता सहमति प्रमाणीकरण**: गतिशील क्लाइन्ट दर्ताका लागि कहिल्यै सहमति स्क्रिनहरू छोड्नु हुँदैन  
- **रिडिरेक्ट URI प्रमाणीकरण**: रिडिरेक्ट गन्तव्यहरूको कडा श्वेतसूची आधारित प्रमाणीकरण  
- **प्राधिकरण कोड सुरक्षा**: छोटो अवधिका कोडहरू र एक पटक प्रयोग लागू गर्नुहोस्  
- **क्लाइन्ट पहिचान प्रमाणीकरण**: क्लाइन्ट प्रमाणपत्र र मेटाडाटा कडा प्रमाणीकरण

## ६. **उपकरण कार्यान्वयन सुरक्षा**

### **स्यान्डबक्सिङ र पृथक्करण**

**कन्टेनर-आधारित पृथक्करण:**
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
- **अलग प्रक्रिया सन्दर्भहरू**: प्रत्येक उपकरण कार्यान्वयन अलग प्रक्रिया स्थानमा  
- **अन्तर-प्रक्रिया सञ्चार**: प्रमाणीकरणसहित सुरक्षित IPC संयन्त्रहरू  
- **प्रक्रिया अनुगमन**: रनटाइम व्यवहार विश्लेषण र असामान्यता पत्ता लगाउने  
- **स्रोत लागू गर्नुहोस्**: CPU, मेमोरी, र I/O अपरेसनहरूमा कडा सीमा

### **न्यूनतम विशेषाधिकार कार्यान्वयन**

**अनुमति व्यवस्थापन:**
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

## ७. **आपूर्ति श्रृंखला सुरक्षा नियन्त्रणहरू**

### **निर्भरता प्रमाणीकरण**

**व्यापक कम्पोनेन्ट सुरक्षा:**
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

### **लगातार अनुगमन**

**आपूर्ति श्रृंखला खतरा पत्ता लगाउने:**
- **निर्भरता स्वास्थ्य अनुगमन**: सबै निर्भरता सुरक्षा समस्याहरूको निरन्तर मूल्याङ्कन  
- **खतरा खुफिया एकीकरण**: उदाउँदो आपूर्ति श्रृंखला खतराहरूमा वास्तविक-समय अपडेटहरू  
- **व्यवहार विश्लेषण**: बाह्य कम्पोनेन्टहरूमा असामान्य व्यवहार पत्ता लगाउने  
- **स्वचालित प्रतिक्रिया**: सम्झौता गरिएको कम्पोनेन्टहरूको तत्काल नियन्त्रण

## ८. **अनुगमन र पत्ता लगाउने नियन्त्रणहरू**

### **सुरक्षा सूचना र घटना व्यवस्थापन (SIEM)**

**व्यापक लगिङ रणनीति:**
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

### **वास्तविक-समय खतरा पत्ता लगाउने**

**व्यवहार विश्लेषण:**
- **प्रयोगकर्ता व्यवहार विश्लेषण (UBA)**: असामान्य प्रयोगकर्ता पहुँच ढाँचाहरूको पत्ता लगाउने  
- **इकाई व्यवहार विश्लेषण (EBA)**: MCP सर्भर र उपकरण व्यवहारको अनुगमन  
- **मेसिन लर्निङ असामान्यता पत्ता लगाउने**: AI-संचालित सुरक्षा खतरा पहिचान  
- **खतरा खुफिया सहसंबन्ध**: ज्ञात आक्रमण ढाँचाहरू विरुद्ध अवलोकित गतिविधिहरू मिलाउने

## ९. **घटना प्रतिक्रिया र पुन: प्राप्ति**

### **स्वचालित प्रतिक्रिया क्षमता**

**तत्काल प्रतिक्रिया कार्यहरू:**
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

### **फरेन्सिक क्षमता**

**अनुसन्धान समर्थन:**
- **अडिट ट्रेल संरक्षण**: क्रिप्टोग्राफिक अखण्डतासहित अपरिवर्तनीय लगिङ  
- **साक्ष्य सङ्कलन**: सम्बन्धित सुरक्षा सामग्रीहरूको स्वचालित सङ्कलन  
- **समयरेखा पुनर्निर्माण**: सुरक्षा घटनाहरूमा पुर्‍याउने घटनाहरूको विस्तृत अनुक्रम  
- **प्रभाव मूल्याङ्कन**: सम्झौता दायरा र डाटा खुलासाको मूल्याङ्कन

## **प्रमुख सुरक्षा वास्तुकला सिद्धान्तहरू**

### **गहिराइमा रक्षा**
- **धेरै सुरक्षा तहहरू**: सुरक्षा वास्तुकलामा कुनै एकल विफलता बिन्दु छैन  
- **अतिरिक्त नियन्त्रणहरू**: महत्वपूर्ण कार्यहरूको लागि ओभरलैपिङ सुरक्षा उपायहरू  
- **फेल-सेफ संयन्त्रहरू**: प्रणालीहरूले त्रुटि वा आक्रमणहरू सामना गर्दा सुरक्षित पूर्वनिर्धारित मानहरू

### **शून्य विश्वास कार्यान्वयन**
- **कहिल्यै विश्वास नगर्नुहोस्, सधैं प्रमाणीकरण गर्नुहोस्**: सबै इकाइहरू र अनुरोधहरूको निरन्तर प्रमाणीकरण  
- **न्यूनतम विशेषाधिकार सिद्धान्त**: सबै कम्पोनेन्टहरूको लागि न्यूनतम पहुँच अधिकार  
- **सूक्ष्म-विभाजन**: सूक्ष्म नेटवर्क र पहुँच नियन्त्रणहरू

### **निरन्तर सुरक्षा विकास**
- **खतरा परिदृश्य अनुकूलन**: उदाउँदो खतराहरूलाई सम्बोधन गर्न नियमित अपडेटहरू  
- **सुरक्षा नियन्त्रण प्रभावकारिता**: नियन्त्रणहरूको निरन्तर मूल्याङ्कन र सुधार  
- **विनिर्देशन अनुपालन**: विकासशील MCP सुरक्षा मापदण्डहरूसँग मेल

---

## **कार्यान्वयन स्रोतहरू**

### **आधिकारिक MCP दस्तावेजहरू**
- [MCP विनिर्देशन (२०२५-११-२५)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP सुरक्षा उत्तम अभ्यासहरू](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP प्राधिकरण विनिर्देशन](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft सुरक्षा समाधानहरू**
- [Microsoft प्रॉम्प्ट शिल्ड्स](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure सामग्री सुरक्षा](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub उन्नत सुरक्षा](https://github.com/security/advanced-security)
- [Azure कुञ्जी भण्डार](https://learn.microsoft.com/azure/key-vault/)

### **सुरक्षा मापदण्डहरू**
- [OAuth 2.0 सुरक्षा उत्तम अभ्यासहरू (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [ठूला भाषा मोडेलहरूको लागि OWASP शीर्ष १०](https://genai.owasp.org/)
- [NIST साइबरसुरक्षा फ्रेमवर्क](https://www.nist.gov/cyberframework)

---

> **महत्वपूर्ण**: यी सुरक्षा नियन्त्रणहरूले हालको MCP विनिर्देशन (२०२५-०६-१८) प्रतिबिम्बित गर्दछन्। मापदण्डहरू तीव्र गतिमा विकास भइरहेका कारण सधैं नवीनतम [आधिकारिक दस्तावेज](https://spec.modelcontextprotocol.io/) सँग प्रमाणीकरण गर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->