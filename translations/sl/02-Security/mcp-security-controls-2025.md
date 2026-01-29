# MCP Varnostni Ukrepi - Posodobitev december 2025

> **Trenutni standard**: Ta dokument odraža varnostne zahteve [MCP specifikacije 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) in uradne [MCP varnostne najboljše prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) je zrel z izboljšanimi varnostnimi ukrepi, ki naslavljajo tako tradicionalno varnost programske opreme kot tudi specifične grožnje AI. Ta dokument zagotavlja celovite varnostne ukrepe za varne implementacije MCP od decembra 2025.

## **OBVEZNE varnostne zahteve**

### **Kritične prepovedi iz MCP specifikacije:**

> **ZAPOVEDANO**: MCP strežniki **NE SMEJO** sprejemati nobenih žetonov, ki niso izrecno izdani za MCP strežnik  
>
> **PREPOVEDANO**: MCP strežniki **NE SMEJO** uporabljati sej za avtentikacijo  
>
> **ZAHETNO**: MCP strežniki, ki izvajajo avtorizacijo, **MORAJO** preveriti VSE dohodne zahteve  
>
> **OBVEZNO**: MCP proxy strežniki, ki uporabljajo statične ID-je odjemalcev, **MORAJO** pridobiti soglasje uporabnika za vsakega dinamično registriranega odjemalca

---

## 1. **Ukrepi za avtentikacijo in avtorizacijo**

### **Integracija zunanjega ponudnika identitete**

**Trenutni MCP standard (2025-06-18)** omogoča MCP strežnikom delegiranje avtentikacije zunanjim ponudnikom identitete, kar predstavlja pomembno varnostno izboljšavo:

### **Integracija zunanjega ponudnika identitete**

**Trenutni MCP standard (2025-11-25)** omogoča MCP strežnikom delegiranje avtentikacije zunanjim ponudnikom identitete, kar predstavlja pomembno varnostno izboljšavo:

**Varnostne koristi:**
1. **Odpravlja tveganja lastne avtentikacije**: Zmanjšuje ranljivost z izogibanjem lastnim implementacijam avtentikacije  
2. **Varnost na ravni podjetja**: Izrablja uveljavljene ponudnike identitete, kot je Microsoft Entra ID, z naprednimi varnostnimi funkcijami  
3. **Centralizirano upravljanje identitet**: Poenostavlja upravljanje življenjskega cikla uporabnikov, nadzor dostopa in revizijo skladnosti  
4. **Večfaktorska avtentikacija**: Deduje MFA zmogljivosti od podjetniških ponudnikov identitete  
5. **Politike pogojnega dostopa**: Izkoristi nadzor dostopa na podlagi tveganja in prilagodljivo avtentikacijo

**Zahteve za implementacijo:**
- **Preverjanje občinstva žetona**: Preverite, da so vsi žetoni izrecno izdani za MCP strežnik  
- **Preverjanje izdajatelja**: Validirajte, da izdajatelj žetona ustreza pričakovanemu ponudniku identitete  
- **Preverjanje podpisa**: Kriptografska validacija integritete žetona  
- **Uveljavljanje poteka**: Strogo spoštovanje omejitev življenjske dobe žetona  
- **Preverjanje obsega**: Zagotovite, da žetoni vsebujejo ustrezna dovoljenja za zahtevane operacije

### **Varnost avtorizacijske logike**

**Kritični ukrepi:**
- **Celovite revizije avtorizacije**: Redni varnostni pregledi vseh točk odločanja o avtorizaciji  
- **Privzete varne nastavitve**: Zavrni dostop, kadar avtorizacijska logika ne more sprejeti dokončne odločitve  
- **Meje dovoljenj**: Jasna ločitev med različnimi ravnmi privilegijev in dostopom do virov  
- **Revizijsko beleženje**: Popolno beleženje vseh odločitev o avtorizaciji za varnostni nadzor  
- **Redni pregledi dostopa**: Periodično preverjanje uporabniških dovoljenj in dodelitev privilegijev

## 2. **Varnost žetonov in ukrepi proti posredovanju**

### **Preprečevanje posredovanja žetonov**

**Posredovanje žetonov je izrecno prepovedano** v MCP specifikaciji avtorizacije zaradi kritičnih varnostnih tveganj:

**Naslavljana varnostna tveganja:**
- **Obhod nadzora**: Zaobide bistvene varnostne ukrepe, kot so omejevanje hitrosti, validacija zahtev in nadzor prometa  
- **Razpad odgovornosti**: Onemogoča identifikacijo odjemalca, kar pokvari revizijske sledi in preiskave incidentov  
- **Izsiljevanje prek proxyja**: Omogoča zlonam uporabo strežnikov kot proxyjev za nepooblaščen dostop do podatkov  
- **Kršitve zaupanja**: Prekine predpostavke zaupanja v izvor žetonov v nadaljnjih storitvah  
- **Lateralno gibanje**: Kompromitirani žetoni na več storitvah omogočajo širitev napada

**Ukrepi za implementacijo:**
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

### **Varnostni vzorci upravljanja žetonov**

**Najboljše prakse:**
- **Kratkotrajni žetoni**: Zmanjšajte izpostavljenost z pogosto rotacijo žetonov  
- **Izdaja po potrebi**: Izdajajte žetone samo, ko so potrebni za specifične operacije  
- **Varnostno shranjevanje**: Uporabljajte strojne varnostne module (HSM) ali varne ključne skrinjice  
- **Povezava žetonov**: Povežite žetone s specifičnimi odjemalci, sejami ali operacijami, kjer je mogoče  
- **Nadzor in opozarjanje**: Zaznavanje zlorabe žetonov ali nepooblaščenih vzorcev dostopa v realnem času

## 3. **Ukrepi za varnost sej**

### **Preprečevanje prevzema sej**

**Naslavljeni napadi:**
- **Vbrizgavanje zlonamernih dogodkov v sejo**: Vbrizgavanje zlonamernih dogodkov v deljeno stanje seje  
- **Prevzem identitete seje**: Nepooblaščena uporaba ukradenih ID-jev sej za obhod avtentikacije  
- **Napadi z nadaljevanjem toka**: Izraba nadaljevanja strežniško poslanih dogodkov za vbrizgavanje zlonamerne vsebine

**Obvezni ukrepi za seje:**
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

**Varnost prenosa:**
- **Uveljavljanje HTTPS**: Vsa komunikacija sej preko TLS 1.3  
- **Varnostne atribute piškotkov**: HttpOnly, Secure, SameSite=Strict  
- **Pripenjanje certifikatov**: Za kritične povezave, da preprečite MITM napade

### **Razmisleki o stanju seje (stateful) in brez stanja (stateless)**

**Za implementacije s stanjem:**
- Deljeno stanje seje zahteva dodatno zaščito pred vbrizgavanjem  
- Upravljanje sej na osnovi čakalnih vrst potrebuje preverjanje integritete  
- Več strežniških instanc zahteva varno sinhronizacijo stanja sej

**Za implementacije brez stanja:**
- Upravljanje sej na osnovi JWT ali podobnih žetonov  
- Kriptografska validacija integritete stanja seje  
- Zmanjšana površina napada, vendar zahteva robustno validacijo žetonov

## 4. **Specifični varnostni ukrepi za AI**

### **Obramba pred vbrizgavanjem ukazov**

**Integracija Microsoft Prompt Shields:**
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

**Ukrepi za implementacijo:**
- **Sanitizacija vhodov**: Celovita validacija in filtriranje vseh uporabniških vhodov  
- **Določitev mej vsebine**: Jasna ločitev med sistemskimi navodili in uporabniško vsebino  
- **Hierarhija navodil**: Pravilna pravila prednosti za nasprotujoča si navodila  
- **Nadzor izhodov**: Zaznavanje potencialno škodljivih ali manipuliranih izhodov

### **Preprečevanje zastrupitve orodij**

**Okvir za varnost orodij:**
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

**Dinamično upravljanje orodij:**
- **Delovni tokovi odobritve**: Izrecno soglasje uporabnika za spremembe orodij  
- **Možnosti povrnitve**: Sposobnost vrnitve na prejšnje različice orodij  
- **Revizija sprememb**: Popolna zgodovina sprememb definicij orodij  
- **Ocena tveganja**: Avtomatizirana ocena varnostnega stanja orodij

## 5. **Preprečevanje napada z zmedenim posrednikom**

### **Varnost OAuth proxyja**

**Ukrepi za preprečevanje napadov:**
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

**Zahteve za implementacijo:**
- **Preverjanje uporabniškega soglasja**: Nikoli ne preskočite zaslonov za soglasje pri dinamični registraciji odjemalcev  
- **Validacija URI za preusmeritev**: Stroga validacija dovoljenih destinacij na osnovi bele liste  
- **Zaščita avtorizacijskih kod**: Kratkotrajne kode z enkratno uporabo  
- **Preverjanje identitete odjemalca**: Robustna validacija poverilnic in metapodatkov odjemalca

## 6. **Varnost izvajanja orodij**

### **Sandboxing in izolacija**

**Izolacija na osnovi kontejnerjev:**
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

**Izolacija procesov:**
- **Ločeni procesni konteksti**: Vsako izvajanje orodja v izoliranem procesnem prostoru  
- **Medprocesna komunikacija**: Varnostni IPC mehanizmi z validacijo  
- **Nadzor procesov**: Analiza vedenja med izvajanjem in zaznavanje anomalij  
- **Uveljavljanje virov**: Stroge omejitve CPU, pomnilnika in I/O operacij

### **Implementacija najmanjših privilegijev**

**Upravljanje dovoljenj:**
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

## 7. **Varnost dobavne verige**

### **Preverjanje odvisnosti**

**Celovita varnost komponent:**
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

### **Neprekinjen nadzor**

**Zaznavanje groženj v dobavni verigi:**
- **Nadzor zdravja odvisnosti**: Neprekinjena ocena vseh odvisnosti glede varnostnih težav  
- **Integracija obveščevalnih podatkov o grožnjah**: Posodobitve v realnem času o novih grožnjah v dobavni verigi  
- **Vedenjska analiza**: Zaznavanje nenavadnega vedenja v zunanjih komponentah  
- **Avtomatiziran odziv**: Takojšnja zajezitev kompromitiranih komponent

## 8. **Ukrepi za nadzor in zaznavanje**

### **Sistem za upravljanje varnostnih informacij in dogodkov (SIEM)**

**Celovita strategija beleženja:**
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

### **Zaznavanje groženj v realnem času**

**Vedenjska analitika:**
- **Analitika vedenja uporabnikov (UBA)**: Zaznavanje nenavadnih vzorcev dostopa uporabnikov  
- **Analitika vedenja entitet (EBA)**: Nadzor vedenja MCP strežnikov in orodij  
- **Zaznavanje anomalij z uporabo strojnega učenja**: AI-podprta identifikacija varnostnih groženj  
- **Korelacija obveščevalnih podatkov o grožnjah**: Ujemanje opaženih aktivnosti z znanimi vzorci napadov

## 9. **Odziv na incidente in okrevanje**

### **Avtomatizirane odzivne zmogljivosti**

**Takojšnji odzivni ukrepi:**
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

### **Forenzične zmogljivosti**

**Podpora preiskavam:**
- **Ohranjanje revizijskih sledi**: Neizbrisno beleženje s kriptografsko integriteto  
- **Zbiranje dokazov**: Avtomatizirano zbiranje relevantnih varnostnih artefaktov  
- **Rekonstrukcija časovnice**: Podroben zaporedni pregled dogodkov, ki so vodili do varnostnih incidentov  
- **Ocena vpliva**: Presoja obsega kompromisa in izpostavljenosti podatkov

## **Ključna načela varnostne arhitekture**

### **Obramba v globino**
- **Več plasti varnosti**: Brez enotne točke odpovedi v varnostni arhitekturi  
- **Podvojeni ukrepi**: Prekrivajoči se varnostni ukrepi za kritične funkcije  
- **Mehanizmi varnega odpovedovanja**: Varnostne privzete nastavitve ob napakah ali napadih

### **Implementacija ničelnega zaupanja**
- **Nikoli ne zaupaj, vedno preverjaj**: Neprestano preverjanje vseh entitet in zahtev  
- **Načelo najmanjših privilegijev**: Minimalne pravice dostopa za vse komponente  
- **Mikrosegmentacija**: Granularni nadzor omrežja in dostopa

### **Neprestana varnostna evolucija**
- **Prilagajanje groženjskemu okolju**: Redne posodobitve za naslavljanje novih groženj  
- **Učinkovitost varnostnih ukrepov**: Stalna ocena in izboljševanje ukrepov  
- **Skladnost s specifikacijami**: Usmerjenost k razvijajočim se MCP varnostnim standardom

---

## **Viri za implementacijo**

### **Uradna MCP dokumentacija**
- [MCP specifikacija (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP varnostne najboljše prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP specifikacija avtorizacije](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft varnostne rešitve**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Varnostni standardi**
- [OAuth 2.0 varnostne najboljše prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 za velike jezikovne modele](https://genai.owasp.org/)
- [NIST okvir za kibernetsko varnost](https://www.nist.gov/cyberframework)

---

> **Pomembno**: Ti varnostni ukrepi odražajo trenutno MCP specifikacijo (2025-06-18). Vedno preverite najnovejšo [uradno dokumentacijo](https://spec.modelcontextprotocol.io/), saj se standardi hitro razvijajo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->