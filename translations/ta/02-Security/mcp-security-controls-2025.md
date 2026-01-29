# MCP பாதுகாப்பு கட்டுப்பாடுகள் - டிசம்பர் 2025 புதுப்பிப்பு

> **தற்போதைய தரநிலை**: இந்த ஆவணம் [MCP விவரக்குறிப்பு 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) பாதுகாப்பு தேவைகள் மற்றும் அதிகாரப்பூர்வ [MCP பாதுகாப்பு சிறந்த நடைமுறைகள்](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) ஆகியவற்றை பிரதிபலிக்கிறது.

Model Context Protocol (MCP) பாரம்பரிய மென்பொருள் பாதுகாப்பும் AI-க்கு தனித்துவமான அச்சுறுத்தல்களும் ஆகியவற்றை கையாளும் மேம்பட்ட பாதுகாப்பு கட்டுப்பாடுகளுடன் முக்கியமாக வளர்ந்துள்ளது. இந்த ஆவணம் டிசம்பர் 2025 நிலவரப்படி பாதுகாப்பான MCP செயலாக்கங்களுக்கு விரிவான பாதுகாப்பு கட்டுப்பாடுகளை வழங்குகிறது.

## **கட்டாயமான பாதுகாப்பு தேவைகள்**

### **MCP விவரக்குறிப்பில் இருந்து முக்கியத் தடைசெய்யப்பட்டவை:**

> **தடைசெய்யப்பட்டது**: MCP சேவையகங்கள் MCP சேவையகத்திற்காக தெளிவாக வழங்கப்படாத எந்த டோக்கன்களையும் ஏற்கக் கூடாது  
>
> **தடைசெய்யப்பட்டது**: MCP சேவையகங்கள் அங்கீகாரத்திற்கு அமர்வுகளை பயன்படுத்தக் கூடாது  
>
> **தேவை**: அங்கீகாரம் செயல்படுத்தும் MCP சேவையகங்கள் அனைத்து உள்ளீட்டு கோரிக்கைகளையும் சரிபார்க்க வேண்டும்  
>
> **கட்டாயம்**: நிலையான கிளையண்ட் ஐடிகளைக் கொண்ட MCP பிரதிநிதி சேவையகங்கள் ஒவ்வொரு இயக்கத்தில் பதிவு செய்யப்பட்ட கிளையண்ட் ஒவ்வொன்றுக்கும் பயனர் ஒப்புதலை பெற வேண்டும்

---

## 1. **அங்கீகாரம் மற்றும் அங்கீகார கட்டுப்பாடுகள்**

### **வெளிப்புற அடையாள வழங்குநர் ஒருங்கிணைப்பு**

**தற்போதைய MCP தரநிலை (2025-06-18)** MCP சேவையகங்களுக்கு அங்கீகாரத்தை வெளிப்புற அடையாள வழங்குநர்களுக்கு ஒப்படைக்க அனுமதிக்கிறது, இது முக்கியமான பாதுகாப்பு மேம்பாடு ஆகும்:

### **வெளிப்புற அடையாள வழங்குநர் ஒருங்கிணைப்பு**

**தற்போதைய MCP தரநிலை (2025-11-25)** MCP சேவையகங்களுக்கு அங்கீகாரத்தை வெளிப்புற அடையாள வழங்குநர்களுக்கு ஒப்படைக்க அனுமதிக்கிறது, இது முக்கியமான பாதுகாப்பு மேம்பாடு ஆகும்:

**பாதுகாப்பு நன்மைகள்:**
1. **தனிப்பயன் அங்கீகார ஆபத்துகளை நீக்குகிறது**: தனிப்பயன் அங்கீகார செயலாக்கங்களை தவிர்த்து பாதிப்பு பரப்பை குறைக்கிறது  
2. **தொழில்துறை தரமான பாதுகாப்பு**: Microsoft Entra ID போன்ற நிறுவனம் அடையாள வழங்குநர்களின் மேம்பட்ட பாதுகாப்பு அம்சங்களை பயன்படுத்துகிறது  
3. **மையமாக்கப்பட்ட அடையாள மேலாண்மை**: பயனர் வாழ்க்கைசுழற்சி மேலாண்மை, அணுகல் கட்டுப்பாடு மற்றும் ஒத்திசைவு கண்காணிப்பை எளிமைப்படுத்துகிறது  
4. **பல-காரண அங்கீகாரம்**: தொழில்துறை அடையாள வழங்குநர்களிடமிருந்து MFA திறன்களை பெறுகிறது  
5. **நிபந்தனை அடிப்படையிலான அணுகல் கொள்கைகள்**: ஆபத்துக்களுக்கான அடிப்படையில் அணுகல் கட்டுப்பாடுகள் மற்றும் தழுவல் அங்கீகாரம்

**செயலாக்க தேவைகள்:**
- **டோக்கன் பார்வையாளர் சரிபார்ப்பு**: அனைத்து டோக்கன்களும் தெளிவாக MCP சேவையகத்திற்காக வழங்கப்பட்டுள்ளதா என்பதை சரிபார்க்கவும்  
- **வழங்குநர் சரிபார்ப்பு**: டோக்கன் வழங்குநர் எதிர்பார்க்கப்படும் அடையாள வழங்குநருடன் பொருந்துகிறதா என்பதை சரிபார்க்கவும்  
- **கையொப்ப சரிபார்ப்பு**: டோக்கன் ஒருமைத்தன்மையை குறியாக்க முறையில் சரிபார்க்கவும்  
- **காலாவதி அமலாக்கம்**: டோக்கன் ஆயுள் வரம்புகளை கடுமையாக அமல்படுத்தவும்  
- **வட்டார சரிபார்ப்பு**: கோரப்பட்ட செயல்பாடுகளுக்கான உரிய அனுமதிகள் டோக்கன்களில் உள்ளதா என்பதை உறுதிப்படுத்தவும்

### **அங்கீகார தர்க்க பாதுகாப்பு**

**முக்கிய கட்டுப்பாடுகள்:**
- **விரிவான அங்கீகார கணக்காய்வுகள்**: அனைத்து அங்கீகார முடிவு புள்ளிகளின் பாதுகாப்பு மதிப்பாய்வுகள்  
- **தோல்வி-பாதுகாப்பு இயல்புகள்**: அங்கீகார தர்க்கம் தெளிவான முடிவை எடுக்க முடியாதபோது அணுகலை மறுக்கவும்  
- **அனுமதி எல்லைகள்**: வெவ்வேறு привிலேஜ் நிலைகள் மற்றும் வள அணுகலுக்கு தெளிவான பிரிவுகள்  
- **கணக்காய்வு பதிவு**: பாதுகாப்பு கண்காணிப்புக்கான அனைத்து அங்கீகார முடிவுகளின் முழுமையான பதிவு  
- **பிரதான அணுகல் மதிப்பாய்வுகள்**: பயனர் அனுமதிகள் மற்றும் привилேஜ் ஒதுக்கீடுகளின் காலாண்டு சரிபார்ப்பு

## 2. **டோக்கன் பாதுகாப்பு மற்றும் எதிர்-பாஸ்த்ரூ கட்டுப்பாடுகள்**

### **டோக்கன் பாஸ்த்ரூ தடுப்பு**

**MCP அங்கீகார விவரக்குறிப்பில் டோக்கன் பாஸ்த்ரூ தெளிவாக தடைசெய்யப்பட்டுள்ளது** முக்கிய பாதுகாப்பு ஆபத்துகளுக்காக:

**கையாளப்பட்ட பாதுகாப்பு ஆபத்துகள்:**
- **கட்டுப்பாடு தவிர்ப்பு**: விகித வரம்பு, கோரிக்கை சரிபார்ப்பு மற்றும் போக்குவரத்து கண்காணிப்பு போன்ற முக்கிய பாதுகாப்பு கட்டுப்பாடுகளை தவிர்க்கிறது  
- **பொறுப்புத்தன்மை முறிவு**: கிளையண்ட் அடையாளம் காண முடியாமல் ஆக்கி கணக்காய்வு பாதைகளை மற்றும் சம்பவ விசாரணையை கெடுக்கும்  
- **பிரதிநிதி அடிப்படையிலான வெளியேற்றம்**: அனுமதியற்ற தரவு அணுகலுக்காக சேவையகங்களை பிரதிநிதிகளாக பயன்படுத்த தீய நோக்கமுள்ளவர்கள்  
- **நம்பிக்கை எல்லை மீறல்கள்**: டோக்கன் தோற்றம் குறித்த கீழ்தர சேவை நம்பிக்கை கருதுகோள்களை உடைக்கும்  
- **பக்கவழி நகர்வு**: பல சேவைகளுக்கு பரவியுள்ள கெடுபிடிக்கப்பட்ட டோக்கன்கள் விரிவான தாக்குதலை அனுமதிக்கும்

**செயலாக்க கட்டுப்பாடுகள்:**
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

### **பாதுகாப்பான டோக்கன் மேலாண்மை மாதிரிகள்**

**சிறந்த நடைமுறைகள்:**
- **குறுகிய ஆயுள் டோக்கன்கள்**: அடிக்கடி டோக்கன் மாற்றத்துடன் வெளிப்பாடு நேரத்தை குறைக்கவும்  
- **தேவையான நேரத்தில் வழங்கல்**: குறிப்பிட்ட செயல்பாடுகளுக்காக மட்டுமே டோக்கன்களை வழங்கவும்  
- **பாதுகாப்பான சேமிப்பு**: ஹார்ட்வேர் பாதுகாப்பு மாட்யூல்கள் (HSM) அல்லது பாதுகாப்பான விசை குவால்ட்களை பயன்படுத்தவும்  
- **டோக்கன் பிணைப்பு**: டோக்கன்களை குறிப்பிட்ட கிளையண்டுகள், அமர்வுகள் அல்லது செயல்பாடுகளுடன் பிணைக்கவும்  
- **கண்காணிப்பு மற்றும் எச்சரிக்கை**: டோக்கன் தவறான பயன்பாடு அல்லது அனுமதியற்ற அணுகல் மாதிரிகளை நேரடி கண்டறிதல்

## 3. **அமர்வு பாதுகாப்பு கட்டுப்பாடுகள்**

### **அமர்வு கைப்பற்றல் தடுப்பு**

**தாக்குதல் வழிகள்:**
- **அமர்வு கைப்பற்றல் தூண்டுதல் ஊட்டுதல்**: பகிரப்பட்ட அமர்வு நிலைக்கு தீய நிகழ்வுகள் ஊட்டுதல்  
- **அமர்வு போலி உருவாக்கல்**: திருடப்பட்ட அமர்வு ஐடிகளை அனுமதியின்றி பயன்படுத்தி அங்கீகாரத்தை தவிர்க்கும்  
- **மீண்டும் தொடங்கக்கூடிய ஸ்ட்ரீம் தாக்குதல்கள்**: சேவையக அனுப்பும் நிகழ்வு மீட்பு மூலம் தீய உள்ளடக்கம் ஊட்டுதல்

**கட்டாய அமர்வு கட்டுப்பாடுகள்:**
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

**போக்குவரத்து பாதுகாப்பு:**
- **HTTPS அமல்படுத்தல்**: அனைத்து அமர்வு தொடர்புகளும் TLS 1.3 மூலம்  
- **பாதுகாப்பான குக்கி பண்புகள்**: HttpOnly, Secure, SameSite=Strict  
- **சான்றிதழ் பிணைப்பு**: MITM தாக்குதல்களைத் தடுக்கும் முக்கிய இணைப்புகளுக்கு

### **நிலையான மற்றும் நிலையற்ற அமலாக்கக் கருத்துக்கள்**

**நிலையான செயலாக்கங்களுக்கு:**
- பகிரப்பட்ட அமர்வு நிலைக்கு ஊட்டுதல் தாக்குதல்களுக்கு கூடுதல் பாதுகாப்பு தேவை  
- வரிசை அடிப்படையிலான அமர்வு மேலாண்மைக்கு ஒருமைத்தன்மை சரிபார்ப்பு  
- பல சேவையக உதவிகள் பாதுகாப்பான அமர்வு நிலை ஒத்திசைவு தேவை

**நிலையற்ற செயலாக்கங்களுக்கு:**
- JWT அல்லது அதே போன்ற டோக்கன் அடிப்படையிலான அமர்வு மேலாண்மை  
- அமர்வு நிலை ஒருமைத்தன்மை குறியாக்க சரிபார்ப்பு  
- குறைந்த தாக்குதல் பரப்பை கொண்டது ஆனால் வலுவான டோக்கன் சரிபார்ப்பை தேவைப்படுத்துகிறது

## 4. **AI-க்கு தனித்துவமான பாதுகாப்பு கட்டுப்பாடுகள்**

### **தூண்டுதல் ஊட்டுதல் பாதுகாப்பு**

**Microsoft Prompt Shields ஒருங்கிணைப்பு:**
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

**செயலாக்க கட்டுப்பாடுகள்:**
- **உள்ளீடு சுத்திகரிப்பு**: அனைத்து பயனர் உள்ளீடுகளின் விரிவான சரிபார்ப்பு மற்றும் வடிகட்டி  
- **உள்ளடக்க எல்லை வரையறை**: அமைப்பு அறிவுரைகள் மற்றும் பயனர் உள்ளடக்கத்துக்கு தெளிவான பிரிவு  
- **அறிவுரை வரிசை**: முரண்பட்ட அறிவுரைகளுக்கு சரியான முன்னுரிமை விதிகள்  
- **வெளியீடு கண்காணிப்பு**: தீங்கு விளைவிக்கும் அல்லது மாற்றப்பட்ட வெளியீடுகளை கண்டறிதல்

### **கருவி விஷப்பொருள் தடுப்பு**

**கருவி பாதுகாப்பு கட்டமைப்பு:**
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

**இயங்கும் கருவி மேலாண்மை:**
- **அங்கீகாரம் பணிகள்**: கருவி மாற்றங்களுக்கு தெளிவான பயனர் ஒப்புதல்  
- **மீள்பதிவு திறன்கள்**: முந்தைய கருவி பதிப்புகளுக்கு திரும்பும் திறன்  
- **மாற்ற கணக்காய்வு**: கருவி வரையறை மாற்றங்களின் முழுமையான வரலாறு  
- **ஆபத்து மதிப்பீடு**: கருவி பாதுகாப்பு நிலையை தானாக மதிப்பீடு செய்தல்

## 5. **குழப்பப்பட்ட பிரதிநிதி தாக்குதல் தடுப்பு**

### **OAuth பிரதிநிதி பாதுகாப்பு**

**தாக்குதல் தடுப்பு கட்டுப்பாடுகள்:**
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

**செயலாக்க தேவைகள்:**
- **பயனர் ஒப்புதல் சரிபார்ப்பு**: இயக்கத்தில் பதிவு செய்யப்பட்ட கிளையண்ட் ஒவ்வொன்றுக்கும் ஒப்புதல் திரைகளை தவிர்க்க வேண்டாம்  
- **மீண்டும் வழிமாற்று URI சரிபார்ப்பு**: மீண்டும் வழிமாற்று இலக்குகளுக்கான கடுமையான வெள்ளியியல் பட்டியல் அடிப்படையிலான சரிபார்ப்பு  
- **அங்கீகார குறியீடு பாதுகாப்பு**: குறுகிய ஆயுள் கொண்ட ஒருமுறை பயன்பாட்டு குறியீடுகள்  
- **கிளையண்ட் அடையாள சரிபார்ப்பு**: கிளையண்ட் அங்கீகாரங்கள் மற்றும் மெட்டாடேட்டாவின் வலுவான சரிபார்ப்பு

## 6. **கருவி செயலாக்க பாதுகாப்பு**

### **சேண்ட்பாக்சிங் மற்றும் தனிமைப்படுத்தல்**

**கண்டெய்னர் அடிப்படையிலான தனிமைப்படுத்தல்:**
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

**செயல்முறை தனிமைப்படுத்தல்:**
- **தனித்த செயல்முறை சூழல்கள்**: ஒவ்வொரு கருவி செயல்பாடும் தனித்த செயல்முறை இடத்தில்  
- **இணைய செயல்முறை தொடர்பு**: சரிபார்ப்புடன் பாதுகாப்பான IPC முறைகள்  
- **செயல்முறை கண்காணிப்பு**: ஓட்டுநிலை நடத்தை பகுப்பாய்வு மற்றும் அசாதாரணம் கண்டறிதல்  
- **வள கட்டுப்பாடு**: CPU, நினைவகம் மற்றும் I/O செயல்பாடுகளுக்கு கடுமையான வரம்புகள்

### **குறைந்த привилேஜ் செயலாக்கம்**

**அனுமதி மேலாண்மை:**
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

## 7. **விநியோக சங்கிலி பாதுகாப்பு கட்டுப்பாடுகள்**

### **இணைப்பு சரிபார்ப்பு**

**விரிவான கூறு பாதுகாப்பு:**
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

### **தொடர்ச்சியான கண்காணிப்பு**

**விநியோக சங்கிலி அச்சுறுத்தல் கண்டறிதல்:**
- **இணைப்பு ஆரோக்கிய கண்காணிப்பு**: அனைத்து இணைப்புகளின் பாதுகாப்பு பிரச்சனைகளுக்கான தொடர்ச்சியான மதிப்பீடு  
- **அச்சுறுத்தல் நுண்ணறிவு ஒருங்கிணைப்பு**: உருவாகும் விநியோக சங்கிலி அச்சுறுத்தல்களுக்கு நேரடி புதுப்பிப்புகள்  
- **நடத்தை பகுப்பாய்வு**: வெளிப்புற கூறுகளில் அசாதாரண நடத்தை கண்டறிதல்  
- **தானியங்கி பதில்**: கெடுபிடிக்கப்பட்ட கூறுகளை உடனடி கட்டுப்பாடு

## 8. **கண்காணிப்பு மற்றும் கண்டறிதல் கட்டுப்பாடுகள்**

### **பாதுகாப்பு தகவல் மற்றும் நிகழ்வு மேலாண்மை (SIEM)**

**விரிவான பதிவு திட்டம்:**
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

### **நேரடி அச்சுறுத்தல் கண்டறிதல்**

**நடத்தை பகுப்பாய்வு:**
- **பயனர் நடத்தை பகுப்பாய்வு (UBA)**: அசாதாரண பயனர் அணுகல் மாதிரிகளை கண்டறிதல்  
- **அமைப்பு நடத்தை பகுப்பாய்வு (EBA)**: MCP சேவையக மற்றும் கருவி நடத்தை கண்காணிப்பு  
- **இயந்திர கற்றல் அசாதாரணம் கண்டறிதல்**: AI-ஆல் இயக்கப்படும் பாதுகாப்பு அச்சுறுத்தல்களின் அடையாளம்  
- **அச்சுறுத்தல் நுண்ணறிவு ஒத்திசைவு**: அறியப்பட்ட தாக்குதல் மாதிரிகளுடன் கவனிக்கப்பட்ட செயல்பாடுகளை பொருத்துதல்

## 9. **சம்பவ பதில் மற்றும் மீட்பு**

### **தானியங்கி பதில் திறன்கள்**

**உடனடி பதில் நடவடிக்கைகள்:**
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

### **விவேசன திறன்கள்**

**விசாரணை ஆதரவு:**
- **கணக்காய்வு பாதை பாதுகாப்பு**: குறியாக்க ஒருமைத்தன்மையுடன் மாற்றமுடியாத பதிவு  
- **சான்று சேகரிப்பு**: தொடர்புடைய பாதுகாப்பு ஆவணங்களை தானாக சேகரித்தல்  
- **நிகழ்வு வரிசை மீட்டமைப்பு**: பாதுகாப்பு சம்பவங்களுக்கு வழிவகுக்கும் நிகழ்வுகளின் விரிவான வரிசை  
- **பாதிப்பு மதிப்பீடு**: கெடுபிடிப்பு பரப்பளவு மற்றும் தரவு வெளிப்பாட்டின் மதிப்பீடு

## **முக்கிய பாதுகாப்பு கட்டமைப்பு 원칙ங்கள்**

### **ஆழமான பாதுகாப்பு**
- **பல பாதுகாப்பு அடுக்குகள்**: பாதுகாப்பு கட்டமைப்பில் ஒரே புள்ளி தோல்வி இல்லை  
- **மீண்டும் மீண்டும் கட்டுப்பாடுகள்**: முக்கிய செயல்பாடுகளுக்கான ஒட்டுமொத்த பாதுகாப்பு நடவடிக்கைகள்  
- **தோல்வி-பாதுகாப்பு இயந்திரங்கள்**: அமைப்புகள் பிழைகள் அல்லது தாக்குதல்களை சந்திக்கும் போது பாதுகாப்பான இயல்புகள்

### **பூஜ்ய நம்பிக்கை செயலாக்கம்**
- **நம்பாதே, எப்போதும் சரிபார்க்க**: அனைத்து அங்கங்களும் மற்றும் கோரிக்கைகளும் தொடர்ச்சியான சரிபார்ப்பு  
- **குறைந்த привилேஜ் 원칙ம்**: அனைத்து கூறுகளுக்கும் குறைந்தபட்ச அணுகல் உரிமைகள்  
- **சிறிய பிரிவாக்கம்**: நெட்வொர்க் மற்றும் அணுகல் கட்டுப்பாடுகளின் நுணுக்கமான பிரிவாக்கம்

### **தொடர்ச்சியான பாதுகாப்பு முன்னேற்றம்**
- **அச்சுறுத்தல் சூழல் தழுவல்**: உருவாகும் அச்சுறுத்தல்களை கையாளும் காலாண்டு புதுப்பிப்புகள்  
- **பாதுகாப்பு கட்டுப்பாடு செயல்திறன்**: கட்டுப்பாடுகளின் தொடர்ச்சியான மதிப்பீடு மற்றும் மேம்பாடு  
- **விவரக்குறிப்பு ஒத்திசைவு**: வளர்ந்து வரும் MCP பாதுகாப்பு தரநிலைகளுடன் ஒத்திசைவு

---

## **செயலாக்க வளங்கள்**

### **அதிகாரப்பூர்வ MCP ஆவணங்கள்**
- [MCP விவரக்குறிப்பு (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP பாதுகாப்பு சிறந்த நடைமுறைகள்](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP அங்கீகார விவரக்குறிப்பு](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft பாதுகாப்பு தீர்வுகள்**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub மேம்பட்ட பாதுகாப்பு](https://github.com/security/advanced-security)
- [Azure விசை குவால்](https://learn.microsoft.com/azure/key-vault/)

### **பாதுகாப்பு தரநிலைகள்**
- [OAuth 2.0 பாதுகாப்பு சிறந்த நடைமுறைகள் (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [பெரிய மொழி மாதிரிகளுக்கான OWASP Top 10](https://genai.owasp.org/)
- [NIST சைபர் பாதுகாப்பு கட்டமைப்பு](https://www.nist.gov/cyberframework)

---

> **முக்கியம்**: இந்த பாதுகாப்பு கட்டுப்பாடுகள் தற்போதைய MCP விவரக்குறிப்பை (2025-06-18) பிரதிபலிக்கின்றன. தரநிலைகள் விரைவாக வளர்ந்து கொண்டிருப்பதால் எப்போதும் [அதிகாரப்பூர்வ ஆவணங்களை](https://spec.modelcontextprotocol.io/) சரிபார்க்கவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனிக்கவும். அசல் ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பேற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->