# MCP Bezpečnostné Kontroly - Aktualizácia December 2025

> **Aktuálny Štandard**: Tento dokument odráža bezpečnostné požiadavky [MCP Špecifikácie 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) a oficiálne [MCP Bezpečnostné Najlepšie Praktiky](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) výrazne dozrel s vylepšenými bezpečnostnými kontrolami, ktoré riešia tradičné softvérové bezpečnostné hrozby aj špecifické hrozby AI. Tento dokument poskytuje komplexné bezpečnostné kontroly pre bezpečné implementácie MCP k decembru 2025.

## **POVINNÉ Bezpečnostné Požiadavky**

### **Kritické Zákazy zo Špecifikácie MCP:**

> **ZAKÁZANÉ**: MCP servery **NESMÚ** akceptovať žiadne tokeny, ktoré neboli explicitne vydané pre MCP server  
>
> **ZAKÁZANÉ**: MCP servery **NESMÚ** používať relácie na autentifikáciu  
>
> **POVINNÉ**: MCP servery implementujúce autorizáciu **MUSIA** overiť VŠETKY prichádzajúce požiadavky  
>
> **POVINNÉ**: MCP proxy servery používajúce statické ID klientov **MUSIA** získať súhlas používateľa pre každého dynamicky registrovaného klienta

---

## 1. **Kontroly Autentifikácie a Autorizácie**

### **Integrácia Externého Poskytovateľa Identity**

**Aktuálny MCP Štandard (2025-06-18)** umožňuje MCP serverom delegovať autentifikáciu na externých poskytovateľov identity, čo predstavuje významné bezpečnostné zlepšenie:

### **Integrácia Externého Poskytovateľa Identity**

**Aktuálny MCP Štandard (2025-11-25)** umožňuje MCP serverom delegovať autentifikáciu na externých poskytovateľov identity, čo predstavuje významné bezpečnostné zlepšenie:

**Bezpečnostné Výhody:**
1. **Eliminuje Riziká Vlastnej Autentifikácie**: Znižuje zraniteľnosť vyhýbaním sa vlastným implementáciám autentifikácie  
2. **Podniková Bezpečnosť**: Využíva etablovaných poskytovateľov identity ako Microsoft Entra ID s pokročilými bezpečnostnými funkciami  
3. **Centralizovaná Správa Identity**: Zjednodušuje správu životného cyklu používateľa, kontrolu prístupu a audit súladu  
4. **Viacfaktorová Autentifikácia**: Dedičnosť MFA schopností od podnikových poskytovateľov identity  
5. **Podmienené Prístupové Politiky**: Využíva kontrolu prístupu založenú na riziku a adaptívnu autentifikáciu

**Požiadavky na Implementáciu:**
- **Validácia Publikum Tokenu**: Overiť, že všetky tokeny sú explicitne vydané pre MCP server  
- **Overenie Vydavateľa**: Validovať, že vydavateľ tokenu zodpovedá očakávanému poskytovateľovi identity  
- **Overenie Podpisu**: Kryptografická validácia integrity tokenu  
- **Vynucovanie Platnosti**: Prísne dodržiavanie limitov životnosti tokenu  
- **Validácia Rozsahu**: Zabezpečiť, že tokeny obsahujú vhodné oprávnenia pre požadované operácie

### **Bezpečnosť Autorizácie**

**Kritické Kontroly:**
- **Komplexné Audity Autorizácie**: Pravidelné bezpečnostné revízie všetkých rozhodovacích bodov autorizácie  
- **Predvolené Bezpečné Nastavenia**: Zamietnuť prístup, ak autorizácia nemôže urobiť jednoznačné rozhodnutie  
- **Hranice Oprávnení**: Jasné oddelenie medzi rôznymi úrovňami privilégií a prístupom k zdrojom  
- **Auditné Záznamy**: Kompletné zaznamenávanie všetkých rozhodnutí autorizácie pre bezpečnostné monitorovanie  
- **Pravidelné Kontroly Prístupu**: Periodická validácia používateľských oprávnení a prideľovania privilégií

## 2. **Bezpečnosť Tokenu a Kontroly Proti Passthrough**

### **Prevencia Passthrough Tokenu**

**Passthrough tokenu je výslovne zakázaný** v MCP Špecifikácii Autorizácie kvôli kritickým bezpečnostným rizikám:

**Riešené Bezpečnostné Riziká:**
- **Obchádzanie Kontroly**: Obchádza základné bezpečnostné kontroly ako obmedzenie rýchlosti, validáciu požiadaviek a monitorovanie prevádzky  
- **Zlyhanie Zodpovednosti**: Zneidentifikovateľnosť klienta, čo poškodzuje auditné stopy a vyšetrovanie incidentov  
- **Proxy Exfiltrácia**: Umožňuje škodlivým aktérom používať servery ako proxy pre neautorizovaný prístup k dátam  
- **Porušenie Dôvery**: Porušuje predpoklady dôvery downstream služieb o pôvode tokenov  
- **Laterálny Pohyb**: Kompromitované tokeny naprieč viacerými službami umožňujú širšie rozšírenie útoku

**Implementačné Kontroly:**
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

### **Vzory Bezpečného Manažmentu Tokenu**

**Najlepšie Praktiky:**
- **Krátkodobé Tokeny**: Minimalizovať expozičné okno častou rotáciou tokenov  
- **Vydávanie Na Požiadanie**: Vydávať tokeny len keď sú potrebné pre konkrétne operácie  
- **Bezpečné Ukladanie**: Používať hardvérové bezpečnostné moduly (HSM) alebo bezpečné úložiská kľúčov  
- **Viazanie Tokenu**: Viazať tokeny na konkrétnych klientov, relácie alebo operácie, kde je to možné  
- **Monitorovanie a Upozorňovanie**: Detekcia zneužitia tokenov alebo neautorizovaných prístupov v reálnom čase

## 3. **Kontroly Bezpečnosti Relácií**

### **Prevencia Únosu Relácie**

**Riešené Útoky:**
- **Vkladanie škodlivých udalostí do relácie**: Vkladanie škodlivých udalostí do zdieľaného stavu relácie  
- **Impersonácia Relácie**: Neoprávnené použitie ukradnutých ID relácie na obídenie autentifikácie  
- **Útoky na Obnovenie Streamu**: Zneužitie obnovenia serverom posielaných udalostí na vkladanie škodlivého obsahu

**Povinné Kontroly Relácie:**
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

**Bezpečnosť Prenosu:**
- **Vynucovanie HTTPS**: Všetka komunikácia relácie cez TLS 1.3  
- **Bezpečné Atribúty Cookies**: HttpOnly, Secure, SameSite=Strict  
- **Pripnutie Certifikátu**: Pre kritické spojenia na prevenciu MITM útokov

### **Úvahy o Stavových vs Bezstavových Implementáciách**

**Pre Stavové Implementácie:**
- Zdieľaný stav relácie vyžaduje dodatočnú ochranu proti injekčným útokom  
- Správa relácií založená na frontách potrebuje overenie integrity  
- Viacnásobné inštancie servera vyžadujú bezpečnú synchronizáciu stavu relácie

**Pre Bezstavové Implementácie:**
- Správa relácií založená na JWT alebo podobných tokenoch  
- Kryptografická validácia integrity stavu relácie  
- Znížená plocha útoku, ale vyžaduje robustnú validáciu tokenov

## 4. **AI-Špecifické Bezpečnostné Kontroly**

### **Ochrana proti Vkladaniu Promptov**

**Integrácia Microsoft Prompt Shields:**
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

**Implementačné Kontroly:**
- **Sanitácia Vstupov**: Komplexná validácia a filtrovanie všetkých používateľských vstupov  
- **Definícia Obsahových Hraníc**: Jasné oddelenie systémových inštrukcií a používateľského obsahu  
- **Hierarchia Inštrukcií**: Správne pravidlá prednosti pre konfliktné inštrukcie  
- **Monitorovanie Výstupu**: Detekcia potenciálne škodlivých alebo manipulovaných výstupov

### **Prevencia Otravy Nástrojov**

**Rámec Bezpečnosti Nástrojov:**
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

**Dynamická Správa Nástrojov:**
- **Schvaľovacie Procesy**: Explicitný súhlas používateľa pre modifikácie nástrojov  
- **Možnosti Návratu**: Schopnosť vrátiť sa k predchádzajúcim verziám nástrojov  
- **Audit Zmien**: Kompletná história zmien definície nástrojov  
- **Hodnotenie Rizík**: Automatizované hodnotenie bezpečnostného stavu nástrojov

## 5. **Prevencia Útoku „Confused Deputy“**

### **Bezpečnosť OAuth Proxy**

**Kontroly Prevencie Útoku:**
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

**Požiadavky na Implementáciu:**
- **Overenie Súhlasu Používateľa**: Nikdy nevynechávať obrazovky súhlasu pri dynamickej registrácii klienta  
- **Validácia Redirect URI**: Prísna validácia cieľov presmerovania na základe whitelistu  
- **Ochrana Autorizačných Kódov**: Krátkodobé kódy s vynútením jednorazového použitia  
- **Overenie Identity Klienta**: Robustná validácia poverení a metadát klienta

## 6. **Bezpečnosť Spúšťania Nástrojov**

### **Sandboxing a Izolácia**

**Izolácia založená na Kontajneroch:**
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

**Izolácia Procesov:**
- **Oddelené Kontexty Procesov**: Každé spustenie nástroja v izolovanom procesnom priestore  
- **Medziprocesová Komunikácia**: Bezpečné IPC mechanizmy s validáciou  
- **Monitorovanie Procesov**: Analýza správania za behu a detekcia anomálií  
- **Vynucovanie Zdroja**: Prísne limity na CPU, pamäť a I/O operácie

### **Implementácia Najmenších Právomocí**

**Správa Oprávnení:**
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

## 7. **Kontroly Bezpečnosti Dodávateľského Reťazca**

### **Overovanie Závislostí**

**Komplexná Bezpečnosť Komponentov:**
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

### **Kontinuálne Monitorovanie**

**Detekcia Hrozieb v Dodávateľskom Reťazci:**
- **Monitorovanie Zdravia Závislostí**: Neustále hodnotenie všetkých závislostí na bezpečnostné problémy  
- **Integrácia Hrozbovej Inteligencie**: Aktualizácie v reálnom čase o nových hrozbách v dodávateľskom reťazci  
- **Behaviorálna Analýza**: Detekcia nezvyčajného správania v externých komponentoch  
- **Automatická Reakcia**: Okamžité zadržanie kompromitovaných komponentov

## 8. **Kontroly Monitorovania a Detekcie**

### **Správa Bezpečnostných Informácií a Udalostí (SIEM)**

**Komplexná Stratégia Logovania:**
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

### **Detekcia Hrozieb v Reálnom Čase**

**Behaviorálna Analytika:**
- **Analytika Správania Používateľov (UBA)**: Detekcia nezvyčajných vzorcov prístupu používateľov  
- **Analytika Správania Entít (EBA)**: Monitorovanie správania MCP servera a nástrojov  
- **Detekcia Anomálií Pomocou Strojového Učenia**: AI-poháňaná identifikácia bezpečnostných hrozieb  
- **Korelácia Hrozbovej Inteligencie**: Porovnávanie pozorovaných aktivít s známymi vzormi útokov

## 9. **Reakcia na Incidenty a Obnova**

### **Automatizované Reakčné Schopnosti**

**Okamžité Reakčné Akcie:**
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

### **Forenzné Schopnosti**

**Podpora Vyšetrovania:**
- **Zachovanie Auditnej Stopy**: Nemenné logovanie s kryptografickou integritou  
- **Zber Dôkazov**: Automatizované zhromažďovanie relevantných bezpečnostných artefaktov  
- **Rekonštrukcia Časovej Os**: Detailné sledovanie udalostí vedúcich k bezpečnostným incidentom  
- **Hodnotenie Dopadu**: Vyhodnotenie rozsahu kompromitácie a expozície dát

## **Kľúčové Bezpečnostné Architektonické Princípy**

### **Obrana v Hĺbke**
- **Viacvrstvové Bezpečnostné Opatrenia**: Žiadny jediný bod zlyhania v bezpečnostnej architektúre  
- **Redundantné Kontroly**: Prekrývajúce sa bezpečnostné opatrenia pre kritické funkcie  
- **Bezpečné Predvolené Nastavenia**: Bezpečné nastavenia pri chybách alebo útokoch

### **Implementácia Zero Trust**
- **Nikdy Neveriť, Vždy Overovať**: Neustála validácia všetkých entít a požiadaviek  
- **Princíp Najmenších Právomocí**: Minimálne prístupové práva pre všetky komponenty  
- **Mikrosegmentácia**: Granulárne sieťové a prístupové kontroly

### **Kontinuálny Vývoj Bezpečnosti**
- **Adaptácia na Hrozby**: Pravidelné aktualizácie na riešenie nových hrozieb  
- **Efektivita Bezpečnostných Kontrol**: Neustále hodnotenie a zlepšovanie kontrol  
- **Súlad so Špecifikáciou**: Zladenie s vyvíjajúcimi sa MCP bezpečnostnými štandardmi

---

## **Implementačné Zdroje**

### **Oficiálna MCP Dokumentácia**
- [MCP Špecifikácia (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Bezpečnostné Najlepšie Praktiky](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Špecifikácia Autorizácie](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Bezpečnostné Riešenia**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Bezpečnostné Štandardy**
- [OAuth 2.0 Bezpečnostné Najlepšie Praktiky (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 pre Veľké Jazykové Modely](https://genai.owasp.org/)
- [NIST Kybernetický Bezpečnostný Rámec](https://www.nist.gov/cyberframework)

---

> **Dôležité**: Tieto bezpečnostné kontroly odrážajú aktuálnu MCP špecifikáciu (2025-06-18). Vždy overujte podľa najnovšej [oficiálnej dokumentácie](https://spec.modelcontextprotocol.io/), pretože štandardy sa rýchlo vyvíjajú.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->