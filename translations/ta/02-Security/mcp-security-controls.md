# MCP பாதுகாப்பு கட்டுப்பாடுகள் - செப்டம்பர் 2026 புதுப்பிப்பு

> **தற்போதைய தரநிலை:** இந்த ஆவணம் பிரதிபலிக்கிறது
> [MCP விவரக்குறிப்பு 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> மற்றும் அதிகாரப்பூர்வ
> [MCP பாதுகாப்பு சிறந்த நடைமுறைகள்](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

மாடல் சூழல் அமைப்பு (MCP) பாரம்பரிய மென்பொருள் பாதுகாப்பும் AI-சூழல் அச்சுறுத்தல்களும் உள்ளிட்ட மேம்பட்ட பாதுகாப்பு கட்டுப்பாடுகளுடன் குறிப்பிடத்தக்க அளவில் வளர்ந்துள்ளது. இந்த ஆவணம், OWASP MCP தலைமை 10 மூலம் ஒத்துழைக்கபட்ட பாதுகாப்பான MCP செயல்பாடுகளுக்கான முழுமையான பாதுகாப்பு கட்டுப்பாடுகளை வழங்குகிறது.

## 🏔️ நடைமுறை பாதுகாப்பு பயிற்சி

நடைமுறை, கைமுறை பாதுகாப்பு செயல்பாட்டுத் தகுதிக்கு, நாங்கள் பரிந்துரைக்கிறோம் **[MCP பாதுகாப்பு உச்சி கருத்தரங்கு பயிற்சி (Sherpa)](https://azure-samples.github.io/sherpa/)** - Azure இல் MCP சேவையகங்களை "குறைவு → வழிமுறையினை பயன்படுத்துதல் → திருத்தல் → சரிபார்த்தல்" முறையில் பாதுகாப்பது குறித்த விரிவான வழிகாட்டும் பயணம்.

இந்த ஆவணத்திலுள்ள அனைத்து பாதுகாப்பு கட்டுப்பாடுகளும் **[OWASP MCP Azure பாதுகாப்பு வழிகாட்டி](https://microsoft.github.io/mcp-azure-security-guide/)** உடன் ஒத்துப்போகின்றன, இது OWASP MCP தலைமை 10 அபாயங்களுக்கு Azure-க்கு உட்பட்ட குறிப்பிட்ட செயற்பாட்டு வழிகாட்டுதல்களையும் மேற்கோள் கட்டமைப்புகளையும் வழங்குகிறது.

## **கட்டாயமான பாதுகாப்பு தேவைகள்**

### **MCP விவரக்குறிப்பில் குறிப்பிடப்பட்ட கடுமையான தடைசெய்தல்கள்:**

> **தடைசெய்யப்பட்டுள்ளது**: MCP சேவையகங்கள் **ஒவ்வொருவருக்கும்** MCP சேவையகத்துக்காக தெளிவாக வழங்கப்படாத எந்த டோக்கன்களையும் ஏற்கக் கூடாது
>
> **கட்டாயமாகத் தடையிடப்பட்டுள்ளது**: MCP சேவையகங்கள் **அங்கீகாரத்திற்காக** அமர்வுகளை பயன்படுத்தக் கூடாது  
>
> **தேவைப்படுகின்றது**: அங்கீகாரத்தை செயல்படுத்தும் MCP சேவையகங்கள் அனைத்து உள்நுழைவுகளையும் உறுதி செய்ய **தேவை**
>
> **கட்டாயம்**: நிலையான மூன்றாம் தரப்பு வாடிக்கையாளர் ஐடி பயன்படுத்தும் MCP பிரதிநிதி சேவையகங்கள்
> ஒவ்வொரு MCP வாடிக்கையாளரிடமிருந்தும் அனுமதி எடுத்து அங்கீகாரத்தை இடமாற்றம் செய்ய வேண்டும்

---

## 1. **அங்கீகாரம் மற்றும் அங்கீகார கட்டுப்பாடுகள்**

### **புற அடையாள வழங்குநர் ஒருங்கிணைப்பு**

**MCP விவரக்குறிப்பு `2026-07-28`** MCP சேவையகங்கள் அங்கீகாரத்தை புற அடையாள வழங்குநர்களுக்கு ஒப்படைக்க அனுமதிக்கிறது. HTTP போக்குவரத்துக்கான அங்கீகாரம் ஒவ்வொரு கோரிக்கைக்கும் மதிப்பீடு செய்யப்படுகிறது; உள்ளூர் stdio சேவையகங்கள் பதிலுக்கு தங்கள் சூழலிடமிருந்து ஐடியெஞ்சல்கள் பெறுகின்றன.




**OWASP MCP அபாயம் எதிர்கொள்ளப்பட்டுள்ளது**: [MCP07 - போதுமான அங்கீகாரம் மற்றும் அங்கீகாரமற்றமை](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**பாதுகாப்பு நன்மைகள்:**
1. **தனிப்பயன் அங்கீகார அபாயங்களை நீக்குகிறது**: தனிப்பயன் அங்கீகார செயல்பாடுகளின் பாதிப்பை குறைக்கின்றது
2. **தொழில்முறை தரத்தில் பாதுகாப்பு**: Microsoft Entra ID போன்ற நிரூபிக்கப்பட்ட அடையாள வழங்குநர்களை பயன்படுத்துகிறது
3. **மையமாக்கப்பட்ட அடையாள மேலாண்மை**: பயனர் வரிசை மேலாண்மை, அணுகல் கட்டுப்பாடு மற்றும் இணக்கமான கணக்கெடுப்பை எளிதாக்குகிறது
4. **பன்முறை அங்கீகாரம்**: தொழில்முறை அடையாள வழங்குநர்களிடமிருந்து MFA திறன்களை பெற்றுக்கொள்கிறது
5. **நிபந்தனையுடைய அணுகல் கொள்கைகள்**: அபாய அடிப்படையிலான அணுகல் கட்டுப்பாடுகள் மற்றும் தழுவல் அங்கீகாரத்தைப் பயன்படுத்துகிறது

**செயல் குறிக்கோள்கள்:**
- **வாடிக்கையாளர் பதிவு**: வாடிக்கையாளர் ஐடி ஆவணங்கள் அல்லது முன் பதிவேற்றத்தை முன்னுரிமையுடன் கையாள்க; பொருந்தக்கூடியதால் பழைய Dynamic Client Registration ஐ மட்டுமே பயன்படுத்தவும்
  
  பொருந்துகையில் மட்டுமே
- **டோக்கன் பார்வையாளர் சரிபார்த்தல்**: அனைத்து டோக்கன்களும் தெளிவாக MCP சேவையகத்துக்காக வழங்கப்பட்டதா என்பதை உறுதி செய்யவும்
- **அளிப்பவர் சரிபார்த்தல்**: டோக்கன் வழங்குநர் எதிர்பார்க்கப்படும் அடையாள வழங்குநரை பொருத்துகிறதா என்பதை சரிபார்க்கவும்
- **கையொப்ப சரிபார்த்தல்**: டோக்கன் முழுமையின் கடவுச்சிக்கல் பொருந்துதலை உறுதி செய்க
- **காலாவதியாகும் கட்டுப்பாடு**: டோக்கனின் ஆயுள் வரம்புகளை கடுமையாக பின்பற்றுக
- **குறிமுறை சரிபார்த்தல்**: கோரப்பட்ட செயல்பாடுகளுக்கான உரிய அனுமதிகள் டோக்கன்களில் உள்ளனவா என்பதை உறுதி செய்யவும்

### **அங்கீகார தருக்க பாதுகாப்பு**


**முக்கிய கட்டுப்பாடுகள்:**
- ** விரிவான அனுமதி சோதனைகள்**: அனைத்து அனுமதி முடிவு புள்ளிகளின் முறையான பாதுகாப்பு ஆய்வுகள்
- **தோல்வி-பாதுகாப்பு பொருட்கள்**: அனுமதி நியாயம் கண்டிப்பான முடிவை வழங்காத போது அணுகலை மறுத்தல்
- **அனுமதி வரையறைகள்**: வெவ்வேறு குறிப்பிட்ட உரிமை நிலைகளுக்கும் வள அணுகலுக்கும் தெளிவான பிரிவு
- **ஆடிட் பதிவேட்டிங்**: பாதுகாப்பு கண்காணிப்பிற்கான அனைத்து அனுமதி முடிவுகளும் முழுமையாக பதிவு செய்யப்படுதல்
- **முறையான அணுகல் ஆய்வுகள்**: பயனர் அனுமதிகளின் மற்றும் உரிமைகள் வழங்கல்களின் காலாண்டு சரிபார்ப்பு

## 2. **டோக்கன் பாதுகாப்பு மற்றும் எதிர்ப்பு-பாஸ்த்ரூ கட்டுப்பாடுகள்**

**OWASP MCP ஆபத்து எதிர்ப்பு**: [MCP01 - டோக்கன் தவறான பராமரிப்பு மற்றும் ரகசிய வெளியீடு](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **டோக்கன் பாஸ்த்ரூ தடுப்பு**

MCP அனுமதி விவரக்குறிப்பில் **டோக்கன் பாஸ்த்ரூ தடைசெய்திருக்கிறது** முக்கியமான பாதுகாப்பு ஆபத்துகளுக்காக:

**சோதனை தெரிவித்த பாதுகாப்பு ஆபத்துகள்:**
- **கட்டுப்பாடுகளை மீறல்**: வேகம் கட்டுப்பாடு, கோரிக்கை சரிபார்ப்பு மற்றும் போக்குவரத்து கண்காணிப்பு போன்ற அவசியமான பாதுகாப்பு கட்டுப்பாடுகளை மீறும்
- **பதில் தேர்ச்சி அடையாளம் பாதிப்பு**: கிளையண்ட் அடையாளம் கண்டறிதல் எதுவும் முடியாமல் ஆடிட் தடயங்கள் மற்றும் சம்பவ விசாரணை மங்குதல்
- **பிராக்ஸி அடிப்படையிலான வெளியேற்றல்**: தவறானவர்கள் அனுமதி இல்லாத தரவுகளுக்கான அணுகலுக்கு சர்வர்களை பிராக்ஸிகளாக பயன்படுத்த அனுமதிக்கும்
- **நம்பிக்கை வரம்பு மீறல்**: டோக்கன் தோற்றங்களைப் பற்றி கீழ்மட்ட சேவைகள் கொண்ட நம்பிக்கைக் கருதுகோள்களை உடைக்கும்
- **பக்கவழி நகர்வு**: பல சேவைகளில் பிணைந்த டோக்கன்கள் பெரிய அளவிலான தாக்குதலுக்கு வழிவகுக்கும்

**நிறைவேற்ற கட்டுப்பாடுகள்:**
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

### **பாதுகாப்பான டோக்கன் மேலாண்மை வடிவங்கள்**

**சிறந்த நடைமுறைகள்:**
- **குறைந்த கால வாழ்நாள் டோக்கன்கள்**: அடிக்கடி டோக்கன் மாற்றம் மூலம் வெளிப்பாட்டை குறைக்க
- **தேவைப்பட்டே நேரத்தில் வழங்கல்**: குறிப்பிட்ட செயல்களுக்கே தேவையான நேரத்தில் மட்டும் டோக்கன்களை வழங்கல்
- **பாதுகாப்பான சேமிப்பு**: ஹார்ட்வேர் பாதுகாப்பு மொடியூல்கள் (HSM) அல்லது பாதுகாப்பான முக்கிய குண்டுகளைக் பயன்படுத்துதல்
- **டோக்கன் பிணைப்பு**: குறிக்கோள் MCP வளம், கிளையண்ட் மற்றும் செயல் ஆகியவற்றுக்கான டோக்கன் பார்வையாளரும் வழங்குநரையும் சரிபார்த்தல்
  
- **கண்காணிப்பு மற்றும் அலைபேசுதல்**: டோக்கன் தவறான பயன்படுத்தல் அல்லது அனுமதி இல்லாத அணுகல் முறைகளை நேரடி கண்டறிதல்

## 3. **விண்ணப்பத்தின் நிலை பாதுகாப்பு கட்டுப்பாடுகள்**

### **நிலை ஹேண்டில் கைப்பற்றல் தடுப்பு**

**தாக்குதல் வழிகள் எதிர்த்து:**
- **ஹேண்டில் ஊகிக்கல்**: கணக்கிடத்தக்க அடையாளங்கள் மற்றொரு அழைப்பாளரின் நிலையை வெளிப்படுத்தும்
- **பயனர் இடை மாற்றம்**: திருடப்பட்ட ஹேண்டில் வேறு அடையாளத்துடன் பயன்படுத்தப்படுகிறது
- **மறைமுக அனுமதி**: ஒரு ஹேண்டில் வைத்திருத்தல் தவறுதலாக அணுகல் ஆதாரமாக கருதப்படுதல்
  

**நிலை ஹேண்டில் கட்டுப்பாடுகள்:**

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

**போக்குவரத்து பாதுகாப்பு:**
- **HTTPS கடைபிடிப்பு**: தொலை HTTP போக்குவரத்துக்கு HTTPS தேவையாக்கல்
- **அங்கீகாரம் கையாள்தல்**: ஒவ்வொரு HTTP கோரிக்கையிலும் அனுமதியை அனுப்பி சரிபார்த்தல்
- **stdio தனிமைப்படுத்தல்**: செயற்குழு தனிமைப்பு மற்றும் சுற்றுச் சூழல் அனுமதி கட்டுப்பாடுகள் மூலம் உள்ளூர் stdio சர்வர்களை பாதுகாத்தல்
  

### **நிலையானவை மற்றும் நிலைமையற்றவை தொடர்பான கருதுகோள்கள்**

MCP `2026-07-28` வழங்கல் அடுக்கில் நிலைமையற்றது. விண்ணப்பங்கள் இன்னும்
ஒரே கருவி அழைப்பிலிருந்து ஒரு தெளிவான ஹேண்டிலை மீண்டெடுத்து அதை
பின்னர் செய்யப்பட்ட அழைப்புகளில் சாதாரண கட்டுரையாக ஏற்றுக்கொள்ளலாம்.

- எந்த ஒரு போக்குவரத்து இணைப்பின் சார்பற்றும் நிலையை சேமிக்கவும்.
- சரிபார்க்கப்பட்ட முதன்மை சேவையகத்துடன் நிலை ஹேண்டில்களை பிணைக்கவும்.
- ஒரு ஹேண்டிலை பெயராக, வழிபவர் சான்றாக அல்லாமல் கருதவும்.
- பழைய ஹேண்டில்களுக்கு காலாவதி மற்றும் மீட்புத்தன்மை நடத்தை வரையறுக்கவும்.

## 4. **காணொளி நுண்ணறிவு-குறிப்பிட்ட பாதுகாப்பு கட்டுப்பாடுகள்**

**OWASP MCP ஆபத்துகள் எதிர்ப்பு**:

- [MCP06 - நோக்குத் தொடர்வழி மாறுதல்](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - கருவி விஷம் சேர்க்கை](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - கட்டளை ஊடைத்தல் மற்றும் செயல்](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **குறிப்புச் செய்தி ஊடைதல் எதிர்ப்பு**

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
- **உள்ளீட்டு சுத்திகரிப்பு**: அனைத்து பயனர் உள்ளீடுகளுக்குமான முழுமையான சரிபார்த்தலும் வடிகட்டலும்
- **உள்ளடக்க எல்லை வரையறை**: அமைப்பு அறிவுரைகளும் பயனர் உள்ளடக்கத்திற்கும் இடையே தெளிவான பிரிப்புகள்
- **அறிவுரை வரிசை**: மோதும் அறிவுரைகளுக்கு சரியான முன்னுரிமை விதிகள்
- **வெளியீடு கண்காணிப்பு**: ஆபத்தான அல்லது மாற்றப்பட்ட வெளிகளை கண்டறிதல்

### **கருவி விஷம் சேர்க்கை தடுப்பு**

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
- **ஒப்புதல் பணிகள்**: கருவி மாற்றங்களுக்கு தெளிவான பயனர் சம்மதம்
- **மீளச் செயலாக்க திறன்கள்**: முந்தைய கருவி பதிப்புகளுக்குத் திரும்பும் திறன்
- **மாற்றம் கண்காணிப்பு**: கருவி வரையறை மாற்றங்களின் முழு வரலாறு
- **ஆபத்து மதிப்பீடு**: கருவி பாதுகாப்பு நிலையை தானாக மதிப்பீடு செய்தல்

## 5. **குழப்பமுற்ற துணைநிலை தாக்குதல் தடுப்பு**

### **OAuth பிரதிநிதி பாதுகாப்பு**

**தாக்குதல் தடுப்பு கட்டுப்பாடுகள்:**
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

**செயலாக்க தேவைகள்:**
- **வாடிக்கையாளர் பதிவு**: முன் பதிவு அல்லது வாடிக்கையாளர் ID மெட்டாடேட்டாவை முன்னுரிமை கொள்க
  ஆவணங்கள்; மாற்றக்கூடிய வாடிக்கையாளர் பதிவை பொருந்தும் பின்னடைவு வழியாக கருதுக
- **பயனர் சம்மத சரிபார்த்தல்**: MCP பிரதிநிதிகள் நிலையான மூன்றாம் தரப்பின் வாடிக்கையாளர்
  ID க்கு ஒவ்வொரு வாடிக்கையாளர் சம்மதம் பெறுதல் தேவையானது அங்கீகாரத்துக்குப் முன்னர்
- **திருப்பிச் செல்லுமிட URL சரிபார்த்தல்**: கடுமையான வெள்ளைப் பட்டியல் அடிப்படையிலான செல்லுமிட சரிபார்த்தல்
- **அங்கீகாரக் குறியீடு பாதுகாப்பு**: குறுகிய ஆயுள் குறியீடுகள் மற்றும் ஒருமுறை பயன்பாடு கடைபிடிப்பு
- **வாடிக்கையாளர் அடையாளத் தேர்வு**: வாடிக்கையாளர் அங்கீகாரங்கள் மற்றும் மெட்டாடேட்டாவின் வலுவான சரிபார்த்தல்

## 6. **கருவி செயல்படுத்தல் பாதுகாப்பு**

### **சாந்தாக்கல் மற்றும் தனிமைப்படுத்தல்**

**கக்கூடல் அடிப்படையிலான தனிமைப்படுத்தல்:**
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
- **தனித்த செயல்முறை சூழல்கள்**: ஒவ்வொரு கருவி இயக்கமும் தனிமைப்படுத்தப்பட்ட செயல்முறை இடத்தில்
- **இணை செயல்முறை தொடர்பு**: சரிபார்ப்புடன் பாதுகாப்பான IPC முறைமைகள்
- **செயல்முறை கண்காணிப்பு**: இயக்கநேர நடைமுறைகள் ஆய்வு மற்றும் அசாதாரணங்களை கண்டறிதல்
- **வள கட்டாயம்**: CPU, நினைவகம், மற்றும் I/O செயல்பாடுகளுக்கு கடுமையான வரம்புகள்

### ** குறைந்தபட்ச உரிமைகள் அமலாக்கம்**

**அதிகாரம் மேலாண்மை:**
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

## 7. **விநியோகம் சங்கிலி பாதுகாப்பு கட்டுப்பாடுகள்**

**OWASP MCP ஆபத்து முகாமை**: [MCP04 - மென்பொருள் விநியோகம் சங்கிலி தாக்குதல்கள் & சார்பு திருத்தங்கள்](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **சார்பு சரிபார்த்தல்**

**இடைநிலை கூறுகளின் முழுமையான பாதுகாப்பு:**
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

### **தொடர்ந்த கண்காணிப்பு**

**விநியோகம் சங்கிலி அச்சுறுத்தல் கண்டறிதல்:**
- **சார்பு உடல் நிலை கண்காணிப்பு**: பாதுகாப்பு பிரச்சினைகளுக்கு அனைத்து சார்புகளின் தொடர்ச்சியான மதிப்பீடு
- **அச்சுறுத்தல் நுண்ணறிவு ஒருங்கிணைப்பு**: உருவாய் வரும் விநியோகம் சங்கிலி அச்சுறுத்தல்களின் நேரடி புதுப்பிப்புகள்
- **நடத்தை பகுப்பாய்வு**: வெளிப்புற கூறுகளின் அசாதாரண நடத்தை கண்டறிதல்
- **தானாகச் செயல்**: பாதிக்கப்பட்ட கூறுகளின் உடனடி தடுப்பு

## 8. **கண்காணிப்பு & கண்டறிதல் கட்டுப்பாடுகள்**

**OWASP MCP ஆபத்து முகாமை**: [MCP08 - கணக்கு மற்றும் தொலைவியல் இல்லாதல்](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **பாதுகாப்பு தகவல் மற்றும் நிகழ்வு மேலாண்மை (SIEM)**

**முழுமையான பதிவு முறைகள்:**
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

### **உண்மையானநேர அச்சுறுத்தல் கண்டறிதல்**

**நடத்தை பகுப்பாய்வு:**
- **பயனர் நடத்தை பகுப்பாய்வு (UBA)**: அசாதாரண பயனர் அணுகல் மாதிரிகளை கண்டறிதல்
- **அமைப்பு நடத்தை பகுப்பாய்வு (EBA)**: MCP சேவையகம் மற்றும் கருவி நடத்தை கண்காணிப்பு
- **இயந்திர கற்றல் அசாதாரண கண்டறிதல்**: AI சக்தியுள்ள பாதுகாப்பு அச்சுறுத்தல்களின் அடையாளம்
- **அச்சுறுத்தல் நுண்ணறிவு ஒத்திசைவு**: அறியப்பட்ட தாக்குதல் மாதிரிகளுக்கு எதிரான காணப்பட்ட நடவடிக்கைகளை பொருத்துதல்

## 9. **நிகழ்வு பதில் மற்றும் மீட்பு**

### **தானியக்க பதில் திறன்கள்**

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

### **உடைக்கல் திறன்கள்**

**ஆய்வு உதவி:**
- **கணக்கு பாதை பாதுகாப்பு**: குற்றப்பாட்டுச் சான்றுகள் கையடக்கமில்லாமல் பதிவுசெய்தல்
- **ஆதாரம் சேகரிப்பு**: தொடர்புடைய பாதுகாப்பு ஆவணங்களை தானாகக் கூடுதல்
- **நேர வரிசை மீட்பு**: பாதுகாப்பு சம்பவங்களுக்கு வழிகாட்டும் விரிவான நிகழ்வுகள் வரிசை
- **தீங்கு மதிப்பீடு**: உடைக்கப்பட்ட அளவு மற்றும் தரவு வெளிப்படையின் மதிப்பீடு

## **முக்கிய பாதுகாப்பு கட்டமைப்பு கோட்பாடுகள்**

### **ஆழ அதிர்ச்சி பாதுகாப்பு**
- **பல பாதுகாப்பு அடுக்குகள்**: பாதுகாப்பு கட்டமைப்பில் ஒரே புள்ளி தோல்வி இல்லை
- **மறு நிரலாக்க கட்டுப்பாடுகள்**: முக்கிய செயல்களுக்கு மேம்பட்ட பாதுகாப்பு நடைகள்
- **தோல்வி-பாதுகாப்பு அளவைகள்**: கணினி பிழைகள் அல்லது தாக்குதல்கள் நேர்ந்தால் பாதுகாப்பான இயல்புகள்

### **பூஜ்ஜிய நம்பிக்கை அமலாக்கம்**
- **ஏதுமின்றி நம்பாதே, எப்போதும் சரிபார்க்க**: அனைத்து அலகுகள் மற்றும் கோரிக்கைகளின் தொடர்ந்த சரிபார்ப்பு
- **குறைந்தபட்ச உரிமைக் கொள்கை**: அனைத்து கூறுகளுக்கும் குறைந்த அணுகல் உரிமைகள்
- **சுகுமார் பிரிவாக்கம்**: நுணுக்கமான நெட்வொர்க் மற்றும் அணுகல் கட்டுப்பாடுகள்

### **தொடர்ந்து பாதுகாப்பு மேம்பாடு**
- **அச்சுறுத்தல் காட்சிப்பரப்புக்கு பொருந்துதல்**: உருவாகும் அச்சுறுத்தல்களுக்கு நிதானமான புதுப்பிப்புகள்
- **பாதுகாப்பு கட்டுப்பாடு பயன்திறன்**: கட்டுப்பாடுகளின் தொடர்ந்த மதிப்பீடு மற்றும் மேம்பாடு
- **விபரம் இணக்கம்**: உருவாகும் MCP பாதுகாப்பு தரநிலைகளுடன் ஒத்திசைவு

---

## **செயலாக்க ஆதாரங்கள்**

### **அதிகாரம் பெற்ற MCP ஆவணங்கள்**
- [MCP விவரிப்பு (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP பாதுகாப்பு சிறந்த நடைமுறைகள்](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP அங்கீகார விவரிப்பு](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP பாதுகாப்பு ஆதாரங்கள்**
- [OWASP MCP Azure பாதுகாப்பு வழிகாட்டு](https://microsoft.github.io/mcp-azure-security-guide/) - Azure செயலாக்கத்துடன் முழுமையான OWASP MCP முதல் 10
- [OWASP MCP முதல் 10](https://owasp.org/www-project-mcp-top-10/) - அதிகாரப்பூர்வ OWASP MCP பாதுகாப்பு ஆபத்துக்கள்
- [MCP பாதுகாப்பு மாநாடு வேலையகம் (Sherpa)](https://azure-samples.github.io/sherpa/) - Azure இல் MCP க்கான கைமுறை பாதுகாப்பு பயிற்சி

### **Microsoft பாதுகாப்பு தீர்வுகள்**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure உள்ளடக்க பாதுகாப்பு](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub உயர் பாதுகாப்பு](https://github.com/security/advanced-security)
- [Azure முக்கிய கிடை](https://learn.microsoft.com/azure/key-vault/)

### **பாதுகாப்பு தரநிலைகள்**
- [OAuth 2.0 பாதுகாப்பு சிறந்த நடைமுறைகள் (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [பெரிய மொழி மாதிரிகளுக்கான OWASP சிறந்த 10](https://genai.owasp.org/)

- [NIST சைபர்செர்க்கியூட்டி கட்டமைப்பு](https://www.nist.gov/cyberframework)

---

> **முக்கியம்:** இந்த பாதுகாப்பு கட்டுப்பாடுகள் MCP குறிப்புருவை பிரதிபலிக்கின்றன
> `2026-07-28`. எப்போதும் உறுதிப்படுத்தவும்
> [தற்போதைய அதிகாரப்பூர்வ ஆவணத்துடன்](https://modelcontextprotocol.io/specification/2026-07-28/)
> காரணமாக தரநிலைகள் தொடர்ந்து வளர்கின்றன.

## அடுத்ததாக என்ன

- திரும்ப: [பாதுகாப்பு தொகுதி ஒளிப்படம்](./README.md)
- தொடர: [தொகுதி 3: தொடங்கி வருவது](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->