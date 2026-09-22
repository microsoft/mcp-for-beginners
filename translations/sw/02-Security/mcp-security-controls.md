# Udhibiti wa Usalama wa MCP - Sasisho la Septemba 2026

> **Kiwango cha sasa:** Hati hii inaakisi
> [Vipimo vya MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> na rasmi
> [MCP Mazoezi Bora ya Usalama](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Itifaki ya Muktadha wa Mfano (MCP) imekua kwa kiasi kikubwa na udhibiti ulioboreshwa wa usalama unaoshughulikia usalama wa kawaida wa programu pamoja na vitisho mahususi vya AI. Hati hii inatoa udhibiti kamili wa usalama kwa utekelezaji salama wa MCP unaoendana na mfumo wa OWASP MCP Top 10.

## 🏔️ Mafunzo ya Vitendo ya Usalama

Kwa uzoefu wa utekelezaji wa usalama wa vitendo, tunapendekeza **[Warsha ya Mkutano wa Usalama wa MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - safari ya kina yenye mwongozo wa kuhakikisha usalama wa seva za MCP katika Azure kwa kutumia mbinu ya "dhaifu → tumiwa → rekebisha → hakiki".

Udhibiti wote wa usalama katika hati hii unalingana na **[Mwongozo wa Usalama wa MCP Azure wa OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, ambao unatoa usanifu wa rejea na miongozo ya utekelezaji maalum ya Azure kwa hatari za OWASP MCP Top 10.

## **Mahitaji ya Usalama YA LAZIMU**

### **Marufuku Muhimu Kutoka kwa Vipimo vya MCP:**

> **MARUFUKU**: Seva za MCP **HAZIWEZI KUPokea** tokeni zozote ambazo hazikutolewa wazi kwa seva ya MCP
>
> **MARUFUKU**: Seva za MCP **HAZITUMII** vikao kwa uthibitishaji  
>
> **YANAHITAJIKA**: Seva za MCP zinazoendesha idhini **ZITAHITAJIKA** kuthibitisha ombi zote zinazoingia
>
> **YA LAZIMU**: Seva za uwakilishi za MCP zinazotumia kitambulisho cha mteja wa mtu wa tatu kisichobadilika
> **ZITAHITAJI** kupata ridhaa kwa kila mteja wa MCP kabla ya kupeleka idhini

---

## 1. **Udhibiti wa Uthibitishaji & Uidhinishaji**

### **Uunganisho wa Mtoaji wa Utambulisho wa Nje**

**Vipimo vya MCP `2026-07-28`** vinaruhusu seva za MCP kuruhusu
uthibitishaji kwa watoa huduma za utambulisho wa nje. Uidhinishaji kwa
usafirishaji wa HTTP unatathminiwa kwa kila ombi; seva za stdio za ndani hupata vyeti
kutoka kwa mazingira yao badala yake.

**Hatari ya OWASP MCP Inayoshughulikiwa**: [MCP07 - Uthibitishaji & Uidhinishaji Usiofaa](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Manufaa ya Usalama:**
1. **Kuondoa Hatari za Uthibitishaji Maalum**: Kupunguza uso wa udhaifu kwa kuepuka utekelezaji wa uthibitishaji maalum
2. **Usalama wa Kiwango cha Shirika**: Kutumia watoa huduma za utambulisho waliothibitishwa kama Microsoft Entra ID wenye vipengele vya usalama vya hali ya juu
3. **Usimamizi wa Utambulisho wa Kitu Kimoja**: Kurahisisha usimamizi wa mzunguko wa mtumiaji, udhibiti wa upatikanaji, na ukaguzi wa uzingatiaji
4. **Uthibitishaji wa Vipengele Mbalimbali**: Kupata uwezo wa MFA kutoka kwa watoa huduma za utambulisho wa shirika
5. **Sera za Upatikanaji Zingine**: Faida kutokana na udhibiti wa upatikanaji unaotegemea hatari na uthibitishaji unaobadilika

**Mahitaji ya Utekelezaji:**
- **Usajili wa Mteja**: Pendekeza Hati za Metadata za Kitambulisho cha Mteja au
  usajili wa awali; tumia Usajili wa Mteja Mzito unaotumika tu kwa
  ulinganifu
- **Uhakikisho wa Malenga wa Tokeni**: Thibitisha tokeni zote zimetolewa wazi kwa seva ya MCP
- **Uthibitishaji wa Mtoaji**: Hakiki kwamba mtoaji wa tokeni anaendana na mtoa utambulisho anayetarajiwa
- **Uthibitishaji wa Saini**: Uhakiki wa siri wa uadilifu wa tokeni
- **Utekelezaji wa Kumalizika kwa Muda**: Utekelezaji mkali wa mipaka ya muda wa tokeni
- **Uhakikisho wa Upana wa Huduma**: Hakikisha tokeni zina ruhusa zinazofaa kwa shughuli zinazohitajika

### **Usalama wa Mantiki ya Uidhinishaji**


**Udhibiti Muhimu:**
- **Ukaguzi Kamili wa Idhini**: Mapitio ya usalama mara kwa mara ya pointi zote za maamuzi ya idhini
- **Chaguo za Usalama za Kuaminika**: Katai ufikiaji wakati mantiki ya idhini haiwezi kufanya uamuzi wa uhakika
- **Mipaka ya Ruhusa**: Tofauti wazi kati ya viwango tofauti vya ruhusa na ufikiaji wa rasilimali
- **Kufuatilia Ukaguzi**: Kurekodi kamili kwa maamuzi yote ya idhini kwa ufuatiliaji wa usalama
- **Mapitio ya Mara kwa Mara ya Ufikiaji**: Uhakiki wa mara kwa mara wa ruhusa za watumiaji na utoaji wa viwango vya ruhusa

## 2. **Usalama wa Tokeni na Udhibiti wa Kuzuia Kupitishwa Kupitia**

**Hatari za OWASP MCP Zilizoshughulikiwa**: [MCP01 - Usimamizi Mbaya wa Tokeni & Kufichuliwa Siri](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Kuzuia Kupitishwa Kwa Tokeni**

**Kupitishwa kwa tokeni kwa uwazi ni marufuku** katika Maelezo ya Idhini ya MCP kutokana na hatari kubwa za usalama:

**Hatari za Usalama Zilizoshughulikiwa:**
- **Kuepuka Udhibiti**: Hupitia udhibiti muhimu wa usalama kama vile ukomo wa kiwango, uhakiki wa maombi, na ufuatiliaji wa trafiki
- **Kuvunjika kwa Uwajibikaji**: Hufanya kutambua mteja kuwa haiwezekani, kuharibu rekodi za ukaguzi na uchunguzi wa matukio
- **Utoaji wa Data Kupitia Wakala**: Huwezesha wahalifu kutumia seva kama wakala wa ufikiaji usioidhinishwa wa data
- **Uvunjaji wa Mipaka ya Uaminifu**: Huvunja dhana za huduma za chini kuhusu asili ya tokeni
- **Kueneza Haraka**: Tokeni zilizoharibika katika huduma nyingi huwezesha kuenea kwa mashambulizi

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

### **Mifumo Salama ya Usimamizi wa Tokeni**

**Mambo Bora:**
- **Tokeni Zenye Muda Mfupi**: Punguza muda wa kufichuliwa kwa mzunguko wa mara kwa mara wa tokeni
- **Kutoa Tokeni Wakati Wa Haja**: Toa tokeni tu wakati zinahitajika kwa shughuli maalum
- **Uhifadhi Salama**: Tumia moduli za usalama wa vifaa (HSMs) au makabati salama ya funguo
- **Kifunga Tokeni**: Thibitisha hadhira ya tokeni na mtengenezaji kwa MCP inayokusudiwa
  rasilimali, mteja, na shughuli
- **Ufuatiliaji na Alerti**: Ugundaji wa wakati halisi wa matumizi mabaya ya tokeni au mifumo ya ufikiaji usioidhinishwa

## 3. **Udhibiti wa Usalama wa Hali ya Programu**

### **Kuzuia Kunyakuliwa kwa Hali ya Programu**

**Njia za Mashambulizi Zilizoshughulikiwa:**
- **Kubahatisha Hali**: Vitambulisho vinavyoweza kutabirika huonesha hali ya mwito mwingine
- **Matumizi Tena ya Watumiaji Wengine**: Hali iliyodukuliwa hutumika na utambulisho tofauti
- **Idhini Isiyoelezwa**: Kumiliki hali hutendewa vibaya kama
  uthibitisho wa ufikiaji

**Udhibiti wa Hali za Programu:**

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

**Usalama wa Usafirishaji:**
- **Utekelezaji wa HTTPS**: Lazimisha HTTPS kwa usafirishaji wa HTTP wa mbali
- **Kushughulikia Cheti**: Tuma na thibitisha idhini kwenye kila ombi la HTTP
- **Kutenganishwa kwa stdio**: Linda seva za stdio za eneo kupitia utengano wa mchakato na
  udhibiti wa cheti wa mazingira

### **Mazingira ya Stateful dhidi ya Stateless**

MCP `2026-07-28` ni isiyo na hali ngazi ya itifaki. Programu bado zinaweza
kuhifadhi hali kwa kurudisha hali wazi kutoka kwa mwito mmoja wa zana na kukubali
kama hoja ya kawaida katika miito inayofuata.

- Hifadhi hali huru kwa mawasiliano yoyote ya usafirishaji.
- Funga hali kwa seva halali iliyo thibitishwa upande wa seva.
- Tendea hali kama jina, si kama cheti cha kubeba.
- Eleza tabia ya kumalizika na urejeshaji kwa hali zilizochakaa.

## 4. **Udhibiti wa Usalama Maalum kwa AI**

**Hatari za OWASP MCP Zilizoshughulikiwa**:

- [MCP06 - Mtiririko wa Makusudio Kupotoshwa](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Uchafuzi wa Vifaa](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Mdinganano wa Amri & Utekelezaji](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Ulinzi wa Kuingiza Maagizo**

**Muungano wa Microsoft Prompt Shields:**
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

**Vidhibiti vya Utekelezaji:**
- **Usafishaji wa Ingizo**: Uhakiki na kuchuja kwa kina kwa viingizo vyote vya mtumiaji
- **Ufafanuzi wa Mipaka ya Yaliyomo**: Tofauti wazi kati ya maagizo ya mfumo na yaliyomo ya mtumiaji
- **Hierakisi ya Maagizo**: Kanuni sahihi za kipaumbele kwa maelekezo yanayokinzana
- **Ufuatiliaji wa Matokeo**: Ugunduzi wa matokeo yenye madhara au yaliyobebwa

### **Kuzuia Uchafuzi wa Vifaa**

**Mfumo wa Usalama wa Vifaa:**
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

**Usimamizi wa Vifaa wa Mabadiliko:**
- **Mchakato wa Idhini**: Ruhusa wazi ya mtumiaji kwa mabadiliko ya kifaa
- **Uwezo wa Rudia Mambo**: Uwezo wa kurudisha toleo la kifaa la awali
- **Ukaguzi wa Mabadiliko**: Historia kamili ya mabadiliko ya ufafanuzi wa kifaa
- **Tathmini ya Hatari**: Tathmini ya moja kwa moja ya hali ya usalama ya kifaa

## 5. **Kuzuia Shambulizi la Msimamizi Mchafu**

### **Usalama wa Wakala wa OAuth**

**Vidhibiti vya Kuzuia Shambulizi:**
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

**Mahitaji ya Utekelezaji:**
- **Usajili wa Mteja**: Inapendekezwa usajili wa awali au Hati za Metadata za Kitambulisho cha Mteja
  Nyaraka; chukulia Usajili wa Mteja Anayetumia Mfumo kama mbadala wa muafaka
- **Uthibitishaji wa Ridhaa ya Mtumiaji**: Wakala wa MCP kutumia Kitambulisho cha Mteja cha mtu wa tatu cha kudumu
  Lazima upate ridhaa kwa kila mteja kabla ya kupeleka ruhusa
- **Uhakiki wa URI ya Kupeleka Mwelekeo**: Uhakiki mkali unaotegemea orodha ya rufaa za kuruhusiwa
- **Ulinzi wa Msimbo wa Ruhusa**: Misimbo yenye muda mfupi na matumizi mara moja
- **Uthibitishaji wa Utambulisho wa Mteja**: Uhakiki thabiti wa vyeti na metadata za mteja

## 6. **Usalama wa Utekelezaji wa Vifaa**

### **Kuweka katika Sanduku na Kutenganisha**

**Kutenganisha Kwenye Kontena:**
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
- **Muktadha wa Mchakato Tofauti**: Kila utekelezaji wa kifaa katika nafasi ya mchakato iliyotenganishwa
- **Mawasiliano ya Mchakato kwa Mchakato**: Mbinu za IPC salama zenye uhakiki
- **Ufuatiliaji wa Mchakato**: Uchambuzi wa tabia wakati wa kukimbia na ugunduzi wa kasoro
- **Utekelezaji wa Rasilimali**: Mipaka madhubuti ya CPU, kumbukumbu, na shughuli za I/O

### **Utekelezaji wa Haki za Chini**

**Usimamizi wa Idhini:**
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

## 7. **Vidhibiti vya Usalama wa Ugavi wa Mnyororo**

**Hatari ya OWASP MCP Iliyoshughulikiwa**: [MCP04 - Mashambulizi ya Ugavi wa Mnyororo wa Programu & Udanganyifu wa Tegemezi](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Uhakiki wa Tegemezi**

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

**Ugunduzi wa Vitisho vya Ugavi wa Mnyororo:**
- **Ufuatiliaji wa Afya ya Tegemezi**: Tathmini endelevu ya tegemezi zote kwa masuala ya usalama
- **Muungano wa Akili za Vitisho**: Sasisho la wakati halisi juu ya vitisho vinavyoibuka vya mnyororo wa ugavi
- **Uchambuzi wa Tabia**: Ugunduzi wa tabia isiyo ya kawaida katika vipengele vya nje
- **Majibu ya Moja kwa Moja**: Kuhifadhi haraka vipengele vilivyoharibika

## 8. **Vidhibiti vya Ufuatiliaji & Ugunduzi**

**Hatari ya OWASP MCP Iliyoshughulikiwa**: [MCP08 - Ukosefu wa Ukaguzi na Telemetri](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Usimamizi wa Taarifa za Usalama na Matukio (SIEM)**

**Mikakati Kamili ya Kurekodi:**
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

**Uchanganuzi wa Tabia:**
- **Uchanganuzi wa Tabia za Mtumiaji (UBA)**: Ugunduzi wa mifumo isiyo ya kawaida ya ufikiaji wa mtumiaji
- **Uchanganuzi wa Tabia za Kiasili (EBA)**: Ufuatiliaji wa tabia ya seva ya MCP na kifaa
- **Ugunduzi wa Kasoro za Mashine ya Kujifunza**: Utambuzi wa vitisho vya usalama kwa msaada wa AI
- **Muungano wa Akili za Vitisho**: Kulinganisha shughuli zilizobainishwa na mifumo ya mashambulizi yanayojulikana

## 9. **Majibu ya Tukio & Urejeshwaji**

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

### **Uwezo wa Forensic**

**Msaada wa Uchunguzi:**
- **Uhifadhi wa Njia ya Ukaguzi**: Kurekodi isiyobadilika yenye uadilifu wa kimfumo cha usimbaji
- **Ukusanyaji wa Ushahidi**: Ukusanyaji wa moja kwa moja wa vitu muhimu vya usalama
- **Urekebishaji wa Mstari wa Wakati**: Mfululizo wa kina wa matukio yaliyopelekea matukio ya usalama
- **Tathmini ya Athari**: Tathmini ya kiwango cha uharibifu na kufichuliwa kwa data

## **Kanuni Muhimu za Usanifu wa Usalama**

### **Ulinzi wa Kina**
- **Tabaka Nyingi za Usalama**: Hakuna sehemu moja pekee inayoweza kuanguka katika usanifu wa usalama
- **Vidhibiti Vinavyojirudia**: Hatua za usalama zinazojirudia kwa kazi muhimu
- **Mifumo ya Usalama Isiyoshindwa**: Mipangilio salama wakati mifumo inakumbana na makosa au mashambulizi

### **Utekelezaji wa Zero Trust**
- **Kamwe Usiamini, Daima Thibitisha**: Uhakiki endelevu wa vyombo vyote na maombi
- **Kanuni ya Haki Ndogo Zaidi**: Haki ndogo kabisa za upatikanaji kwa vipengele vyote
- **Upangaji Mdogo-wa-Micro**: Udhibiti wa mtandao na upatikanaji kwa undani

### **Mabadiliko Endelevu ya Usalama**
- **Urekebishaji wa Mazingira ya Vitisho**: Sasisho za mara kwa mara kukabiliana na vitisho vinavyoibuka
- **Ufanisi wa Udhibiti wa Usalama**: Tathmini na kuboresha vidhibiti kwa kuendelea
- **Uzingatiaji wa Maelezo**: Ulinganifu na viwango vinavyoendelea vya usalama MCP

---

## **Rasilimali za Utekelezaji**

### **Nyaraka Rasmi za MCP**
- [Maelezo ya MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Mazingira Bora ya Usalama ya MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Maelezo ya Idhini ya MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Rasilimali za Usalama za OWASP MCP**
- [Mwongozo wa Usalama wa OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Orodha kamili ya OWASP MCP ya Juu 10 na utekelezaji wa Azure
- [OWASP MCP Juu 10](https://owasp.org/www-project-mcp-top-10/) - Hatari rasmi za usalama za OWASP MCP
- [Warsha ya Mkutano wa Usalama wa MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Mafunzo ya vitendo ya usalama kwa MCP kwenye Azure

### **Suluhisho za Usalama za Microsoft**
- [Kodi za Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Usalama wa Yaliyomo wa Azure](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Usalama wa Juu wa GitHub](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Viwango vya Usalama**
- [Mazingira Bora ya Usalama wa OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 kwa Modeli Kubwa za Lugha](https://genai.owasp.org/)

- [Msingi wa Usalama wa Mtandao wa NIST](https://www.nist.gov/cyberframework)

---

> **Muhimu:** Udhibiti huu wa usalama unaendana na MCP Specification
> `2026-07-28`. Daima hakikisha kupima na
> [nakala rasmi ya sasa](https://modelcontextprotocol.io/specification/2026-07-28/)
> kwani viwango vinaendelea kubadilika.

## Nini Kifuatacho

- Rudi kwa: [Muhtasari wa Kifaa cha Usalama](./README.md)
- Endelea kwa: [Kifaa 3: Kuanzia](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->