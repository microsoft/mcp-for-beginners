# Udhibiti wa Usalama wa MCP - Sasisho la Desemba 2025

> **Kiwango cha Sasa**: Hati hii inaonyesha mahitaji ya usalama ya [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) na [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) rasmi.

Itifaki ya Muktadha wa Mfano (MCP) imekua kwa kiasi kikubwa na udhibiti wa usalama ulioboreshwa unaoshughulikia usalama wa programu za jadi na vitisho maalum vya AI. Hati hii inatoa udhibiti kamili wa usalama kwa utekelezaji salama wa MCP kuanzia Desemba 2025.

## **Mahitaji ya Usalama YA LAZIMA**

### **Marufuku Muhimu kutoka MCP Specification:**

> **MARUFUKU**: Seva za MCP **HAZIRUHUSIWI** kukubali tokeni zozote ambazo hazikutolewa wazi kwa seva ya MCP  
>
> **MARUFUKU**: Seva za MCP **HAZIRUHUSIWI** kutumia vikao kwa uthibitishaji  
>
> **INAHITAJIKA**: Seva za MCP zinazotekeleza idhini **ZINAHITAJIKA** kuthibitisha MAOMBI YOTE yanayoingia  
>
> **LAZIMA**: Seva za wakala wa MCP zinazotumia vitambulisho vya mteja vya kudumu **ZINAHITAJIKA** kupata idhini ya mtumiaji kwa kila mteja aliyejiandikisha kwa nguvu

---

## 1. **Udhibiti wa Uthibitishaji & Idhini**

### **Uunganisho wa Mtoa Utambulisho wa Nje**

**Kiwango cha MCP cha Sasa (2025-06-18)** kinaruhusu seva za MCP kuhamisha uthibitishaji kwa watoa utambulisho wa nje, kinachoonyesha uboreshaji mkubwa wa usalama:

### **Uunganisho wa Mtoa Utambulisho wa Nje**

**Kiwango cha MCP cha Sasa (2025-11-25)** kinaruhusu seva za MCP kuhamisha uthibitishaji kwa watoa utambulisho wa nje, kinachoonyesha uboreshaji mkubwa wa usalama:

**Manufaa ya Usalama:**
1. **Hutoa Hatari za Uthibitishaji wa Kipekee**: Kupunguza eneo la hatari kwa kuepuka utekelezaji wa uthibitishaji wa kipekee
2. **Usalama wa Kiwango cha Biashara**: Kutumia watoa utambulisho waliothibitishwa kama Microsoft Entra ID wenye vipengele vya usalama vya hali ya juu
3. **Usimamizi wa Utambulisho wa Kituo Kimoja**: Kurahisisha usimamizi wa mzunguko wa mtumiaji, udhibiti wa upatikanaji, na ukaguzi wa ufuataji
4. **Uthibitishaji wa Vipengele Vingi (MFA)**: Kupata uwezo wa MFA kutoka kwa watoa utambulisho wa biashara
5. **Sera za Upatikanaji wa Masharti**: Manufaa kutoka kwa udhibiti wa upatikanaji unaotegemea hatari na uthibitishaji unaobadilika

**Mahitaji ya Utekelezaji:**
- **Uthibitishaji wa Hadhira ya Tokeni**: Thibitisha tokeni zote zimetolewa wazi kwa seva ya MCP
- **Uthibitishaji wa Mtengenezaji**: Thibitisha mtengenezaji wa tokeni analingana na mtoa utambulisho anayetegemewa
- **Uthibitishaji wa Saini**: Uthibitishaji wa kijasusi wa uadilifu wa tokeni
- **Utekelezaji wa Muda wa Kumalizika**: Utekelezaji mkali wa mipaka ya muda wa tokeni
- **Uthibitishaji wa Eneo**: Hakikisha tokeni zina ruhusa zinazofaa kwa shughuli zinazohitajika

### **Usalama wa Mantiki ya Idhini**

**Udhibiti Muhimu:**
- **Ukaguzi Kamili wa Idhini**: Mapitio ya usalama ya mara kwa mara ya pointi zote za maamuzi ya idhini
- **Mazingira Salama ya Kutoeleweka**: Kukanusha upatikanaji wakati mantiki ya idhini haiwezi kufanya uamuzi thabiti
- **Mipaka ya Ruhusa**: Tofauti wazi kati ya viwango tofauti vya mamlaka na upatikanaji wa rasilimali
- **Kufuatilia Ukaguzi**: Kurekodi kamili kwa maamuzi yote ya idhini kwa ufuatiliaji wa usalama
- **Mapitio ya Mara kwa Mara ya Upatikanaji**: Uthibitishaji wa mara kwa mara wa ruhusa za watumiaji na mgawanyo wa mamlaka

## 2. **Usalama wa Tokeni & Udhibiti wa Kuzuia Kupitisha Tokeni**

### **Kuzuia Kupitisha Tokeni**

**Kupitisha tokeni kinarufukwa wazi** katika MCP Authorization Specification kutokana na hatari kubwa za usalama:

**Hatari za Usalama Zinazoshughulikiwa:**
- **Kuepuka Udhibiti**: Kupita udhibiti muhimu wa usalama kama ukomo wa kiwango, uthibitishaji wa maombi, na ufuatiliaji wa trafiki
- **Kukosekana kwa Uwajibikaji**: Kufanya utambuzi wa mteja usiwezekane, kuharibu rekodi za ukaguzi na uchunguzi wa matukio
- **Utoaji wa Data Kupitia Wakala**: Kuruhusu wahalifu kutumia seva kama mawakala kwa upatikanaji usioidhinishwa wa data
- **Uvunjaji wa Mipaka ya Uaminifu**: Kuvunja dhana za huduma za chini kuhusu asili ya tokeni
- **Harakati za Pembeni**: Tokeni zilizoathirika katika huduma nyingi kuruhusu upanuzi mkubwa wa mashambulizi

**Udhibiti wa Utekelezaji:**
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

### **Mifumo ya Usimamizi wa Tokeni Salama**

**Mbinu Bora:**
- **Tokeni za Muda Mfupi**: Punguza dirisha la kufichuliwa kwa mzunguko wa mara kwa mara wa tokeni
- **Utoaji wa Wakati Sahihi**: Toa tokeni tu wakati zinahitajika kwa shughuli maalum
- **Uhifadhi Salama**: Tumia moduli za usalama wa vifaa (HSMs) au hazina salama za funguo
- **Ufungaji wa Tokeni**: Funga tokeni kwa wateja, vikao, au shughuli maalum inapowezekana
- **Ufuatiliaji & Tahadhari**: Ugunduzi wa wakati halisi wa matumizi mabaya ya tokeni au mifumo isiyoidhinishwa ya upatikanaji

## 3. **Udhibiti wa Usalama wa Vikao**

### **Kuzuia Uvunjaji wa Kikao**

**Njia za Kushambulia Zinazoshughulikiwa:**
- **Kuingizwa kwa Amri za Kikao**: Matukio mabaya yaliyoingizwa katika hali ya kikao kilichoshirikiwa
- **Kuiga Kikao**: Matumizi yasiyoidhinishwa ya vitambulisho vya kikao vilivyoibiwa kupita uthibitishaji
- **Mashambulizi ya Kuendelea kwa Mtiririko**: Matumizi mabaya ya kuendelea kwa matukio ya seva kwa kuingiza maudhui mabaya

**Udhibiti wa Lazima wa Kikao:**
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

**Usalama wa Usafirishaji:**
- **Utekelezaji wa HTTPS**: Mawasiliano yote ya kikao kupitia TLS 1.3
- **Sifa Salama za Vidakuzi**: HttpOnly, Secure, SameSite=Strict
- **Kuweka Pini Cheti**: Kwa muunganisho muhimu kuzuia mashambulizi ya MITM

### **Mazingira ya Stateful dhidi ya Stateless**

**Kwa Utekelezaji wa Stateful:**
- Hali ya kikao kilichoshirikiwa inahitaji ulinzi zaidi dhidi ya mashambulizi ya kuingizwa
- Usimamizi wa kikao unaotegemea foleni unahitaji uthibitishaji wa uadilifu
- Mifumo mingi ya seva inahitaji usawazishaji salama wa hali ya kikao

**Kwa Utekelezaji wa Stateless:**
- Usimamizi wa kikao unaotegemea JWT au tokeni zinazofanana
- Uthibitishaji wa kijasusi wa uadilifu wa hali ya kikao
- Kupunguza eneo la mashambulizi lakini kunahitaji uthibitishaji thabiti wa tokeni

## 4. **Udhibiti wa Usalama Maalum kwa AI**

### **Ulinzi wa Kuingizwa kwa Amri**

**Uunganisho wa Microsoft Prompt Shields:**
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

**Udhibiti wa Utekelezaji:**
- **Usafishaji wa Ingizo**: Uthibitishaji na uchujaji kamili wa ingizo zote za mtumiaji
- **Ufafanuzi wa Mipaka ya Maudhui**: Tofauti wazi kati ya maagizo ya mfumo na maudhui ya mtumiaji
- **Mlinganyo wa Maagizo**: Sheria sahihi za kipaumbele kwa maagizo yanayopingana
- **Ufuatiliaji wa Matokeo**: Ugunduzi wa matokeo yanayoweza kuwa hatari au yaliyobadilishwa

### **Kuzuia Uharibifu wa Zana**

**Mfumo wa Usalama wa Zana:**
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

**Usimamizi wa Zana unaobadilika:**
- **Mchakato wa Idhini**: Idhini wazi ya mtumiaji kwa mabadiliko ya zana
- **Uwezo wa Kurudisha Mabadiliko**: Uwezo wa kurudisha matoleo ya awali ya zana
- **Ukaguzi wa Mabadiliko**: Historia kamili ya mabadiliko ya ufafanuzi wa zana
- **Tathmini ya Hatari**: Tathmini ya moja kwa moja ya hali ya usalama ya zana

## 5. **Kuzuia Mashambulizi ya Mwakilishi Mchanganyiko**

### **Usalama wa Wakala wa OAuth**

**Udhibiti wa Kuzuia Mashambulizi:**
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

**Mahitaji ya Utekelezaji:**
- **Uthibitishaji wa Idhini ya Mtumiaji**: Kamwe usiruke skrini za idhini kwa usajili wa mteja wa nguvu
- **Uthibitishaji wa URI ya Kuongoza**: Uthibitishaji mkali wa orodha ya maeneo ya kuongoza
- **Ulinzi wa Msimbo wa Idhini**: Msimbo wa muda mfupi na utekelezaji wa matumizi mara moja
- **Uthibitishaji wa Utambulisho wa Mteja**: Uthibitishaji thabiti wa sifa na metadata za mteja

## 6. **Usalama wa Utekelezaji wa Zana**

### **Kuweka Kizuizi na Kutenganisha**

**Kutenganisha kwa Mifuko:**
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

**Kutenganisha Mchakato:**
- **Muktadha wa Mchakato Tofauti**: Kila utekelezaji wa zana katika nafasi ya mchakato iliyotengwa
- **Mawasiliano ya Mchakato kwa Mchakato**: Mbinu salama za IPC zenye uthibitishaji
- **Ufuatiliaji wa Mchakato**: Uchambuzi wa tabia ya wakati wa utekelezaji na ugunduzi wa kasoro
- **Utekelezaji wa Rasilimali**: Mipaka thabiti ya CPU, kumbukumbu, na shughuli za I/O

### **Utekelezaji wa Mamlaka ya Chini Zaidi**

**Usimamizi wa Ruhusa:**
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

## 7. **Udhibiti wa Usalama wa Mnyororo wa Ugavi**

### **Uthibitishaji wa Mtegemezi**

**Usalama Kamili wa Vipengele:**
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

### **Ufuatiliaji Endelevu**

**Ugunduzi wa Vitisho vya Mnyororo wa Ugavi:**
- **Ufuatiliaji wa Afya ya Mtegemezi**: Tathmini endelevu ya vyanzo vyote kwa masuala ya usalama
- **Uunganisho wa Ujasusi wa Vitisho**: Sasisho za wakati halisi juu ya vitisho vinavyoibuka vya mnyororo wa ugavi
- **Uchambuzi wa Tabia**: Ugunduzi wa tabia zisizo za kawaida katika vipengele vya nje
- **Majibu ya Moja kwa Moja**: Kuzuia mara moja kwa vipengele vilivyoathirika

## 8. **Udhibiti wa Ufuatiliaji & Ugunduzi**

### **Usimamizi wa Taarifa za Usalama na Matukio (SIEM)**

**Mkakati Kamili wa Kurekodi:**
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

### **Ugunduzi wa Vitisho kwa Wakati Halisi**

**Uchambuzi wa Tabia:**
- **Uchambuzi wa Tabia za Mtumiaji (UBA)**: Ugunduzi wa mifumo isiyo ya kawaida ya upatikanaji wa mtumiaji
- **Uchambuzi wa Tabia za Kitu (EBA)**: Ufuatiliaji wa tabia ya seva ya MCP na zana
- **Ugunduzi wa Kasoro kwa Kujifunza Mashine**: Utambuzi wa vitisho vya usalama kwa msaada wa AI
- **Ulinganifu wa Ujasusi wa Vitisho**: Kulinganisha shughuli zilizoonekana na mifumo ya mashambulizi inayojulikana

## 9. **Majibu ya Tukio & Urejeshaji**

### **Uwezo wa Majibu ya Moja kwa Moja**

**Hatua za Majibu ya Haraka:**
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

### **Uwezo wa Uchunguzi wa Kisheria**

**Msaada wa Uchunguzi:**
- **Uhifadhi wa Rekodi za Ukaguzi**: Kurekodi isiyobadilika yenye uadilifu wa kijasusi
- **Ukusanyaji wa Ushahidi**: Ukusanyaji wa moja kwa moja wa nyaraka muhimu za usalama
- **Urekebishaji wa Mfululizo wa Matukio**: Mfuatano wa kina wa matukio yaliyopelekea matukio ya usalama
- **Tathmini ya Athari**: Tathmini ya kiwango cha uharibifu na kufichuliwa kwa data

## **Misingi Muhimu ya Usanifu wa Usalama**

### **Ulinzi kwa Kina**
- **Tabaka Nyingi za Usalama**: Hakuna sehemu moja inayoweza kushindwa katika usanifu wa usalama
- **Udhibiti wa Kurudia**: Hatua za usalama zinazojirudia kwa kazi muhimu
- **Mifumo Salama ya Kutoeleweka**: Chaguo salama wakati mifumo inakutana na makosa au mashambulizi

### **Utekelezaji wa Kuamini Sifuri**
- **Kamwe Usiamini, Daima Thibitisha**: Uthibitishaji endelevu wa vyombo vyote na maombi
- **Kanuni ya Mamlaka ya Chini Zaidi**: Haki za upatikanaji za chini kabisa kwa vipengele vyote
- **Ugawaji Mdogo wa Mtandao**: Udhibiti wa mtandao na upatikanaji kwa undani

### **Mabadiliko Endelevu ya Usalama**
- **Urekebishaji wa Mazingira ya Vitisho**: Sasisho za mara kwa mara kushughulikia vitisho vinavyoibuka
- **Ufanisi wa Udhibiti wa Usalama**: Tathmini na kuboresha udhibiti kwa kuendelea
- **Uzingatiaji wa Maelezo**: Ulinganifu na viwango vinavyobadilika vya usalama vya MCP

---

## **Rasilimali za Utekelezaji**

### **Nyaraka Rasmi za MCP**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Suluhisho za Usalama za Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Viwango vya Usalama**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Muhimu**: Udhibiti huu wa usalama unaonyesha maelezo ya sasa ya MCP (2025-06-18). Daima thibitisha dhidi ya [nyaraka rasmi](https://spec.modelcontextprotocol.io/) za hivi karibuni kwani viwango vinaendelea kubadilika kwa kasi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifu cha Kutotegemea**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->