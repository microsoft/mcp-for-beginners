# MCP bezpečnostné kontroly - aktualizácia september 2026

> **Súčasný štandard:** Tento dokument odráža
> [MCP špecifikáciu 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> a oficiálne
> [Najlepšie bezpečnostné praktiky MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Protokol Model Context (MCP) výrazne dozrel s vylepšenými bezpečnostnými kontrolami, ktoré riešia tradičné bezpečnostné aspekty softvéru aj špecifické hrozby AI. Tento dokument poskytuje komplexné bezpečnostné kontroly pre bezpečné implementácie MCP zosúladené s rámcom OWASP MCP Top 10.

## 🏔️ Praktický bezpečnostný tréning

Pre praktickú, reálnu skúsenosť s implementáciou bezpečnosti odporúčame **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** – komplexnú riadenú expedíciu na zabezpečenie MCP serverov v Azure pomocou metodológie „zraniteľný → exploit → oprava → overenie“.

Všetky bezpečnostné kontroly v tomto dokumente sú zosúladené s **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, ktorý poskytuje referenčné architektúry a odporúčania pre implementáciu špecifickú pre Azure pre riziká OWASP MCP Top 10.

## **POVINNÉ bezpečnostné požiadavky**

### **Kritické zákazy podľa MCP špecifikácie:**

> **ZAKÁZANÉ**: MCP servery **NESMÚ** akceptovať žiadne tokeny, ktoré neboli výslovne vydané pre MCP server
>
> **ZAKÁZANÉ**: MCP servery **NESMÚ** používať relácie na autentifikáciu  
>
> **POVINNÉ**: MCP servery implementujúce autorizáciu **MUSIA** overiť VŠETKY prichádzajúce požiadavky
>
> **POVINNÉ**: MCP proxy servery používajúce statické klientské ID tretích strán
> **MUSIA** získať súhlas pre každého MCP klienta pred odoslaním autorizácie

---

## 1. **Kontroly autentifikácie a autorizácie**

### **Integrácia externých poskytovateľov identity**

**MCP špecifikácia `2026-07-28`** umožňuje MCP serverom delegovať
autentifikáciu na externých poskytovateľov identity. Autorizácia pre HTTP
prenosy sa hodnotí pre každú požiadavku; lokálne stdio servery získavajú poverenia
miesto toho z prostredia.

**Riziko OWASP MCP riešené**: [MCP07 - Nedostatočná autentifikácia a autorizácia](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Bezpečnostné výhody:**
1. **Eliminuje riziká vlastnej autentifikácie**: Znižuje zraniteľnosť vyhýbaním sa vlastným implementáciám autentifikácie
2. **Podnikového štandardu bezpečnosť**: Využíva overených poskytovateľov identity ako Microsoft Entra ID s pokročilými bezpečnostnými funkciami
3. **Centralizované riadenie identity**: Zjednodušuje správu životného cyklu používateľa, kontrolu prístupu a audity zhody
4. **Viacfaktorová autentifikácia**: Dedia schopnosti MFA od podnikového poskytovateľa identity
5. **Podmienkové prístupové politiky**: Využíva kontroly prístupu na základe rizika a adaptívnu autentifikáciu

**Požiadavky na implementáciu:**
- **Registrácia klienta**: Uprednostniť metadata dokumenty klienta alebo
  predregistráciu; použitie zastaralého Dynamic Client Registration len pre
  kompatibilitu
- **Overenie publika tokenu**: Overiť, že všetky tokeny sú výslovne vydané pre MCP server
- **Overenie vydavateľa**: Overiť, že vydavateľ tokenu zodpovedá očakávanému poskytovateľovi identity
- **Overenie podpisu**: Kryptografické overenie integrity tokenu
- **Presadzovanie expirácie**: Prísne dodržiavanie limitov životnosti tokenu
- **Overovanie oprávnení**: Zabezpečiť, že tokeny obsahujú príslušné povolenia pre požadované operácie

### **Bezpečnosť logiky autorizácie**

**Kritické kontroly:**
- **Komplexné audity autorizácie**: Pravidelné bezpečnostné kontroly všetkých bodov rozhodovania o autorizácii
- **Fail-Safe predvolené nastavenia**: Odmietnuť prístup, keď logika autorizácie nemôže prijať definitívne rozhodnutie
- **Hraničné povolenia**: Jasné oddelenie medzi rôznymi úrovňami privilégií a prístupu k zdrojom
- **Auditné protokolovanie**: Kompletné logovanie všetkých rozhodnutí o autorizácii na monitorovanie bezpečnosti
- **Pravidelné revízie prístupu**: Periodická validácia používateľských oprávnení a pridelení privilégií

## 2. **Bezpečnosť tokenov a kontroly zabraňujúce ich prenosu**

**Riziko OWASP MCP riešené**: [MCP01 - Nesprávne nakladanie s tokenmi a expozícia tajomstiev](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Prevencia prenosu tokenov**

**Prenos tokenov je v MCP autorizácii výslovne zakázaný** kvôli kritickým bezpečnostným rizikám:

**Riešené bezpečnostné riziká:**
- **Obídenie kontrol**: Obchádza základné bezpečnostné kontroly ako obmedzovanie rýchlosti, validáciu požiadaviek a monitorovanie prevádzky
- **Narušenie zodpovednosti**: Zneprístupňuje identifikáciu klienta, čím poškodzuje audity a vyšetrovanie incidentov
- **Exfiltrácia cez proxy**: Umožňuje útočníkom využiť servery ako proxy pre neautorizovaný prístup k údajom
- **Porušenie hraníc dôvery**: Porušuje predpoklady downstream služieb o pôvode tokenu
- **Postupný pohyb**: Kompromitované tokeny naprieč službami umožňujú rozsiahlejšie útoky

**Implementačné kontroly:**
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

### **Vzory bezpečného spravovania tokenov**

**Najlepšie praktiky:**
- **Krátkodobé tokeny**: Minimalizovať obdobie expozície častou rotáciou tokenov
- **Vydávanie na požiadanie**: Vydávať tokeny len keď sú potrebné pre konkrétne operácie
- **Bezpečné uloženie**: Používať hardwarové bezpečnostné moduly (HSM) alebo bezpečné kľúčové úložiská
- **Viazanie tokenu**: Overiť publikum a vydavateľa tokenu pre určený MCP
  zdroj, klienta a operáciu
- **Monitorovanie a upozorňovanie**: Detekcia prípadného zneužitia tokenov alebo neautorizovaných vzorov prístupu v reálnom čase

## 3. **Kontroly bezpečnosti stavu aplikácie**

### **Prevencia krádeže state handle**

**Rizikové útoky riešené:**
- **Hádané handlovanie**: Predvídateľné identifikátory vystavujú stav iného volajúceho
- **Medziužívateľské znovupoužitie**: Ukradnutý handle sa používa s inou identitou
- **Implicitná autorizácia**: Vlastnenie handlu je nesprávne považované za
  dôkaz prístupu

**Kontroly state handle:**

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

**Bezpečnosť prenosu:**
- **Presadzovanie HTTPS**: Vyžadovať HTTPS pre vzdialené HTTP prenosy
- **Zaobchádzanie s povereniami**: Odosielať a validovať autorizáciu pri každom HTTP požiadavku
- **Izolácia stdio**: Chrániť lokálne stdio servery procesovou izoláciou a
  kontrolou poverení prostredia

### **Úvahy o stavovosti vs. bezstavovosti**

MCP `2026-07-28` je na protokolovej vrstve bezstavový. Aplikácie môžu stále
udržiavať stav tým, že vrátia explicitný handle z jedného volania nástroja a akceptujú
ho ako bežný argument pri neskorších volaniach.

- Ukladať stav nezávisle od akejkoľvek jednej transportnej spojenia.
- Viazať state handly na autentifikovaného princípa na strane servera.
- Zaobchádzať s handle ako s menom, nie ako s nositeľským poverením.
- Definovať správanie expirácie a obnovy pre zastarané handly.

## 4. **Špecifické bezpečnostné kontroly pre AI**

**Riziká OWASP MCP riešené**:

- [MCP06 - Podvrhnutie toku úmyslov](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Otrávenie nástroja](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Vstrekovanie a vykonávanie príkazov](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Ochrana proti podvrhnutiu promptu**

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

**Implementačné kontroly:**
- **Sanitácia vstupu**: Komplexná validácia a filtrovanie všetkých používateľských vstupov
- **Definícia hranice obsahu**: Jasné oddelenie systémových inštrukcií a používateľského obsahu
- **Hierarchia inštrukcií**: Správne pravidlá prednosti pre konfliktné inštrukcie
- **Monitorovanie výstupu**: Detekcia potenciálne škodlivých alebo zmanipulovaných výstupov

### **Prevencia otrávenia nástroja**

**Rámec bezpečnosti nástrojov:**
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

**Dynamické riadenie nástrojov:**
- **Schvaľovacie workflowy**: Explicitný súhlas používateľa pre zmeny nástroja
- **Možnosti obnovy**: Schopnosť vrátiť sa k predchádzajúcim verziám nástroja
- **Audit zmien**: Kompletná história úprav definícií nástroja
- **Hodnotenie rizík**: Automatizované vyhodnocovanie bezpečnostného stavu nástrojov

## 5. **Prevencia útoku zmätkujúceho zástupcu**

### **Bezpečnosť OAuth proxy**

**Kontroly prevencie útokov:**
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

**Implementačné požiadavky:**
- **Registrácia klienta**: Uprednostniť predregistrovanie alebo klientské ID metadáta
  dokumenty; dynamická registrácia klienta ako kompatibilný záložný plán
- **Overenie súhlasu používateľa**: MCP proxy s pevným klientským ID tretej strany
  musia získať súhlas pre každý klient pred preposlaním autorizácie
- **Validácia URI presmerovania**: Prísna validácia príjemcov presmerovania na základe whitelistu
- **Ochrana autorizačného kódu**: Krátkodobé kódy s vynúteným jednorazovým použitím
- **Overenie totožnosti klienta**: Robustná validácia klientskych poverení a metadát

## 6. **Bezpečnosť vykonávania nástrojov**

### **Sandboxing a izolácia**

**Izolácia založená na kontajneroch:**
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

**Izolácia procesov:**
- **Oddelené kontexty procesov**: Každé vykonanie nástroja v izolovanom procesnom priestore
- **Medzi-procesová komunikácia**: Bezpečné IPC mechanizmy s validáciou
- **Monitorovanie procesov**: Analýza správania za behu a detekcia anomálií
- **Vynucovanie zdrojov**: Prísne limity CPU, pamäte a I/O operácií

### **Implementácia princípu najmenších práv**

**Správa oprávnení:**
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

## 7. **Kontroly bezpečnosti dodávateľského reťazca**

**OWASP MCP riziko riešené**: [MCP04 - Útoky na softvérový dodávateľský reťazec a manipulácia so závislosťami](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Verifikácia závislostí**

**Komplexná bezpečnosť komponentov:**
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

### **Kontinuálne monitorovanie**

**Detekcia hrozieb v dodávateľskom reťazci:**
- **Monitorovanie zdravotného stavu závislostí**: Neustále hodnotenie všetkých závislostí z hľadiska bezpečnostných problémov
- **Integrácia hrozbovej inteligencie**: Aktualizácie v reálnom čase o nových hrozbách v dodávateľskom reťazci
- **Behaviorálna analýza**: Detekcia nezvyčajného správania v externých komponentoch
- **Automatizovaná reakcia**: Okamžité zadržanie kompromitovaných komponentov

## 8. **Kontroly monitorovania a detekcie**

**OWASP MCP riziko riešené**: [MCP08 - Nedostatok auditu a telemetrie](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Manažment bezpečnostných informácií a udalostí (SIEM)**

**Komplexná stratégia zaznamenávania:**
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

### **Detekcia hrozieb v reálnom čase**

**Behaviorálna analytika:**
- **Analytika správania používateľov (UBA)**: Detekcia nezvyčajných vzorcov prístupu používateľov
- **Analytika správania entít (EBA)**: Monitorovanie správania MCP servera a nástrojov
- **Detekcia anomálií pomocou strojového učenia**: AI-poháňaná identifikácia bezpečnostných hrozieb
- **Korelovanie hrozbovej inteligencie**: Porovnávanie pozorovaných aktivít so známymi vzormi útokov

## 9. **Reakcia na incidenty a obnova**

### **Automatizované reakčné schopnosti**

**Okamžité opatrenia reakcie:**
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

### **Forenzné schopnosti**

**Podpora vyšetrovania:**
- **Zachovanie auditnej stopy**: Nemenné zaznamenávanie s kryptografickou integritou
- **Zber dôkazov**: Automatizované zhromažďovanie relevantných bezpečnostných artefaktov
- **Rekonštrukcia časovej osi**: Detailná sekvencia udalostí vedúcich k bezpečnostným incidentom
- **Hodnotenie dopadu**: Vyhodnotenie rozsahu kompromitácie a expozície dát

## **Kľúčové princípy bezpečnostnej architektúry**

### **Obrana v hĺbke**
- **Viaceré bezpečnostné vrstvy**: Žiadny jediný bod zlyhania v bezpečnostnej architektúre
- **Redundantné kontroly**: Prekrývajúce sa bezpečnostné opatrenia pre kritické funkcie
- **Mechanizmy fail-safe**: Bezpečné predvolené nastavenia pri chybách alebo útokoch

### **Implementácia Zero Trust**
- **Nikdy neveriť, vždy overovať**: Neustála validácia všetkých entít a požiadaviek
- **Princíp najmenších práv**: Minimálne prístupové práva pre všetky komponenty
- **Mikrosegmentácia**: Granulárna sieťová a prístupová kontrola

### **Kontinuálny bezpečnostný vývoj**
- **Adaptácia na hrozby v prostredí**: Pravidelné aktualizácie reagujúce na vznikajúce hrozby
- **Efektivita bezpečnostných kontrol**: Neustále hodnotenie a zlepšovanie kontrol
- **Súlad so špecifikáciou**: Zladenie s vyvíjajúcimi sa bezpečnostnými štandardmi MCP

---

## **Implementačné zdroje**

### **Oficiálna dokumentácia MCP**
- [Špecifikácia MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Najlepšie bezpečnostné praktiky MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Špecifikácia autorizácie MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Bezpečnostné zdroje OWASP MCP**
- [Sprievodca bezpečnosťou OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Komplexné OWASP MCP Top 10 s implementáciou v Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Oficiálne bezpečnostné riziká OWASP MCP
- [MCP Security Summit workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktický bezpečnostný tréning MCP na Azure

### **Bezpečnostné riešenia Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Bezpečnostné štandardy**
- [Najlepšie bezpečnostné praktiky OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 pre veľké jazykové modely](https://genai.owasp.org/)

- [NIST kybernetický rámec](https://www.nist.gov/cyberframework)

---

> **Dôležité:** Tieto bezpečnostné kontroly odrážajú špecifikáciu MCP
> `2026-07-28`. Vždy si overte podľa
> [aktuálnej oficiálnej dokumentácie](https://modelcontextprotocol.io/specification/2026-07-28/)
>, keďže štandardy sa neustále menia.

## Čo ďalej

- Návrat na: [Prehľad bezpečnostného modulu](./README.md)
- Pokračovať na: [Modul 3: Začíname](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->