# MCP Bezpečnostní Kontroly - Aktualizace prosinec 2025

> **Aktuální standard**: Tento dokument odráží bezpečnostní požadavky [MCP specifikace 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) a oficiální [MCP bezpečnostní osvědčené postupy](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) výrazně dozrál s vylepšenými bezpečnostními kontrolami, které řeší jak tradiční softwarovou bezpečnost, tak specifické hrozby AI. Tento dokument poskytuje komplexní bezpečnostní kontroly pro bezpečné implementace MCP k prosinci 2025.

## **POVINNÉ bezpečnostní požadavky**

### **Kritické zákazy z MCP specifikace:**

> **ZAKÁZÁNO**: MCP servery **NESMÍ** přijímat žádné tokeny, které nebyly explicitně vydány pro MCP server  
>
> **ZAKÁZÁNO**: MCP servery **NESMÍ** používat relace pro autentizaci  
>
> **POŽADOVÁNO**: MCP servery implementující autorizaci **MUSÍ** ověřovat VŠECHNY příchozí požadavky  
>
> **POVINNÉ**: MCP proxy servery používající statické ID klientů **MUSÍ** získat souhlas uživatele pro každého dynamicky registrovaného klienta

---

## 1. **Kontroly autentizace a autorizace**

### **Integrace externího poskytovatele identity**

**Aktuální MCP standard (2025-06-18)** umožňuje MCP serverům delegovat autentizaci na externí poskytovatele identity, což představuje významné bezpečnostní zlepšení:

### **Integrace externího poskytovatele identity**

**Aktuální MCP standard (2025-11-25)** umožňuje MCP serverům delegovat autentizaci na externí poskytovatele identity, což představuje významné bezpečnostní zlepšení:

**Bezpečnostní přínosy:**
1. **Eliminace rizik vlastních autentizací**: Snižuje zranitelnost vyhýbáním se vlastním implementacím autentizace  
2. **Podniková bezpečnost**: Využívá zavedené poskytovatele identity jako Microsoft Entra ID s pokročilými bezpečnostními funkcemi  
3. **Centralizovaná správa identity**: Zjednodušuje správu životního cyklu uživatelů, řízení přístupu a audit souladu  
4. **Vícefaktorová autentizace**: Dědí schopnosti MFA od podnikových poskytovatelů identity  
5. **Podmíněné přístupové politiky**: Využívá řízení přístupu založené na riziku a adaptivní autentizaci

**Požadavky na implementaci:**
- **Validace publika tokenu**: Ověřit, že všechny tokeny jsou explicitně vydány pro MCP server  
- **Ověření vydavatele**: Validovat, že vydavatel tokenu odpovídá očekávanému poskytovateli identity  
- **Ověření podpisu**: Kryptografická validace integrity tokenu  
- **Vynucení expirace**: Přísné dodržování limitů životnosti tokenu  
- **Validace rozsahu**: Zajistit, že tokeny obsahují odpovídající oprávnění pro požadované operace

### **Bezpečnost logiky autorizace**

**Kritické kontroly:**
- **Komplexní audity autorizace**: Pravidelné bezpečnostní revize všech rozhodovacích bodů autorizace  
- **Výchozí bezpečné nastavení**: Zamítnout přístup, pokud logika autorizace nemůže učinit jednoznačné rozhodnutí  
- **Hranice oprávnění**: Jasné oddělení mezi různými úrovněmi oprávnění a přístupem k prostředkům  
- **Auditní záznamy**: Kompletní logování všech rozhodnutí autorizace pro bezpečnostní monitoring  
- **Pravidelné revize přístupu**: Periodická validace uživatelských oprávnění a přiřazení privilegií

## 2. **Bezpečnost tokenů a kontroly proti průchodu tokenů**

### **Prevence průchodu tokenů**

**Průchod tokenů je explicitně zakázán** v MCP specifikaci autorizace kvůli kritickým bezpečnostním rizikům:

**Řešené bezpečnostní rizika:**
- **Obcházení kontrol**: Obchází zásadní bezpečnostní kontroly jako omezení rychlosti, validaci požadavků a monitorování provozu  
- **Ztráta odpovědnosti**: Ztěžuje identifikaci klienta, poškozuje auditní stopy a vyšetřování incidentů  
- **Proxy exfiltrace**: Umožňuje škodlivým aktérům používat servery jako proxy pro neoprávněný přístup k datům  
- **Porušení hranic důvěry**: Narušuje předpoklady downstream služeb o původu tokenů  
- **Laterální pohyb**: Kompromitované tokeny napříč službami umožňují širší expanzi útoku

**Kontroly implementace:**
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

### **Vzorové bezpečné řízení tokenů**

**Osvědčené postupy:**
- **Krátkodobé tokeny**: Minimalizovat dobu expozice častou rotací tokenů  
- **Vydávání na požádání**: Vydávat tokeny pouze, když jsou potřeba pro konkrétní operace  
- **Bezpečné uložení**: Používat hardwarové bezpečnostní moduly (HSM) nebo zabezpečené úložiště klíčů  
- **Vazba tokenů**: Vázat tokeny na konkrétní klienty, relace nebo operace, pokud je to možné  
- **Monitorování a upozornění**: Detekce zneužití tokenů nebo neoprávněných přístupů v reálném čase

## 3. **Kontroly bezpečnosti relací**

### **Prevence únosu relace**

**Řešené vektory útoku:**
- **Vstřikování škodlivých promptů do relace**: Škodlivé události vkládané do sdíleného stavu relace  
- **Impersonace relace**: Neoprávněné použití ukradených ID relace k obejití autentizace  
- **Útoky na obnovu streamu**: Zneužití obnovení serverem odesílaných událostí pro škodlivé vkládání obsahu

**Povinné kontroly relace:**
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

**Bezpečnost přenosu:**
- **Vynucení HTTPS**: Veškerá komunikace relace přes TLS 1.3  
- **Atributy zabezpečených cookies**: HttpOnly, Secure, SameSite=Strict  
- **Připnutí certifikátu**: Pro kritická spojení k prevenci MITM útoků

### **Stavové vs bezstavové úvahy**

**Pro stavové implementace:**
- Sdílený stav relace vyžaduje dodatečnou ochranu proti injekčním útokům  
- Správa relace založená na frontách vyžaduje ověření integrity  
- Více instancí serveru vyžaduje bezpečnou synchronizaci stavu relace

**Pro bezstavové implementace:**
- Správa relace založená na JWT nebo podobných tokenech  
- Kryptografická validace integrity stavu relace  
- Snížená plocha útoku, ale vyžaduje robustní validaci tokenů

## 4. **Specifické bezpečnostní kontroly pro AI**

### **Ochrana proti prompt injection**

**Integrace Microsoft Prompt Shields:**
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

**Kontroly implementace:**
- **Sanitace vstupů**: Komplexní validace a filtrování všech uživatelských vstupů  
- **Definice hranic obsahu**: Jasné oddělení systémových instrukcí a uživatelského obsahu  
- **Hierarchie instrukcí**: Správná pravidla precedence pro konfliktní instrukce  
- **Monitorování výstupu**: Detekce potenciálně škodlivých nebo manipulovaných výstupů

### **Prevence otravy nástrojů**

**Rámec bezpečnosti nástrojů:**
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

**Dynamická správa nástrojů:**
- **Schvalovací workflow**: Explicitní souhlas uživatele pro změny nástrojů  
- **Možnosti návratu**: Schopnost vrátit se k předchozím verzím nástrojů  
- **Audit změn**: Kompletní historie modifikací definic nástrojů  
- **Hodnocení rizik**: Automatizované vyhodnocení bezpečnostního stavu nástrojů

## 5. **Prevence útoku zmateného zástupce**

### **Bezpečnost OAuth proxy**

**Kontroly prevence útoků:**
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

**Požadavky na implementaci:**
- **Ověření souhlasu uživatele**: Nikdy nevynechávat obrazovky souhlasu pro dynamickou registraci klienta  
- **Validace URI přesměrování**: Přísná validace cílových adres na základě whitelistu  
- **Ochrana autorizačního kódu**: Krátkodobé kódy s vynucením jednorázového použití  
- **Ověření identity klienta**: Robustní validace přihlašovacích údajů a metadat klienta

## 6. **Bezpečnost provádění nástrojů**

### **Sandboxing a izolace**

**Izolace založená na kontejnerech:**
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

**Izolace procesů:**
- **Oddělené kontexty procesů**: Každé spuštění nástroje v izolovaném procesním prostoru  
- **Meziprocesová komunikace**: Bezpečné IPC mechanismy s validací  
- **Monitorování procesů**: Analýza chování za běhu a detekce anomálií  
- **Vynucení zdrojů**: Přísné limity na CPU, paměť a I/O operace

### **Implementace principu nejmenších privilegií**

**Správa oprávnění:**
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

## 7. **Kontroly bezpečnosti dodavatelského řetězce**

### **Ověření závislostí**

**Komplexní bezpečnost komponent:**
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

### **Kontinuální monitorování**

**Detekce hrozeb v dodavatelském řetězci:**
- **Monitorování stavu závislostí**: Průběžné hodnocení všech závislostí na bezpečnostní problémy  
- **Integrace zpravodajství o hrozbách**: Aktualizace v reálném čase o nově vznikajících hrozbách v dodavatelském řetězci  
- **Behaviorální analýza**: Detekce neobvyklého chování v externích komponentách  
- **Automatická reakce**: Okamžité zadržení kompromitovaných komponent

## 8. **Kontroly monitorování a detekce**

### **Správa bezpečnostních informací a událostí (SIEM)**

**Komplexní strategie logování:**
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

### **Detekce hrozeb v reálném čase**

**Behaviorální analýza:**
- **Analýza chování uživatelů (UBA)**: Detekce neobvyklých vzorců přístupu uživatelů  
- **Analýza chování entit (EBA)**: Monitorování chování MCP serveru a nástrojů  
- **Detekce anomálií pomocí strojového učení**: AI-poháněná identifikace bezpečnostních hrozeb  
- **Korelace zpravodajství o hrozbách**: Porovnání pozorovaných aktivit s známými vzory útoků

## 9. **Reakce na incidenty a obnova**

### **Automatizované reakční schopnosti**

**Okamžité reakční akce:**
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

### **Forenzní schopnosti**

**Podpora vyšetřování:**
- **Zachování auditní stopy**: Neměnné logování s kryptografickou integritou  
- **Sbírání důkazů**: Automatizované shromažďování relevantních bezpečnostních artefaktů  
- **Rekonstrukce časové osy**: Detailní sled událostí vedoucích k bezpečnostním incidentům  
- **Hodnocení dopadu**: Vyhodnocení rozsahu kompromitace a expozice dat

## **Klíčové principy bezpečnostní architektury**

### **Obrana v hloubce**
- **Více bezpečnostních vrstev**: Žádný jediný bod selhání v bezpečnostní architektuře  
- **Redundantní kontroly**: Překrývající se bezpečnostní opatření pro kritické funkce  
- **Bezpečné výchozí nastavení**: Bezpečné výchozí hodnoty při chybách nebo útocích

### **Implementace Zero Trust**
- **Nikdy nedůvěřuj, vždy ověřuj**: Neustálá validace všech entit a požadavků  
- **Princip nejmenších privilegií**: Minimální přístupová práva pro všechny komponenty  
- **Mikrosegmentace**: Granulární síťové a přístupové kontroly

### **Kontinuální vývoj bezpečnosti**
- **Adaptace na hrozby**: Pravidelné aktualizace pro řešení nově vznikajících hrozeb  
- **Efektivita bezpečnostních kontrol**: Průběžné hodnocení a zlepšování kontrol  
- **Soulad se specifikací**: Soulad s vyvíjejícími se MCP bezpečnostními standardy

---

## **Zdroje pro implementaci**

### **Oficiální dokumentace MCP**
- [MCP specifikace (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP bezpečnostní osvědčené postupy](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP specifikace autorizace](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft bezpečnostní řešení**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Bezpečnostní standardy**
- [OAuth 2.0 bezpečnostní osvědčené postupy (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 pro velké jazykové modely](https://genai.owasp.org/)
- [NIST kybernetický bezpečnostní rámec](https://www.nist.gov/cyberframework)

---

> **Důležité**: Tyto bezpečnostní kontroly odrážejí aktuální MCP specifikaci (2025-06-18). Vždy ověřujte podle nejnovější [oficiální dokumentace](https://spec.modelcontextprotocol.io/), protože standardy se rychle vyvíjejí.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->