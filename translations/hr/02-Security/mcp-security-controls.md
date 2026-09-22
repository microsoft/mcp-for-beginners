# MCP Sigurnosne Kontrole - Ažuriranje za rujan 2026.

> **Trenutni standard:** Ovaj dokument odražava
> [MCP Specifikaciju 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> i službene
> [MCP Sigurnosne Najbolje Prakse](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Protokol Model Konteksta (MCP) značajno je napredovao s poboljšanim sigurnosnim kontrolama koje pokrivaju kako tradicionalne sigurnosne probleme softvera tako i specifične prijetnje umjetnoj inteligenciji. Ovaj dokument pruža sveobuhvatne sigurnosne kontrole za sigurne implementacije MCP usklađene s OWASP MCP Top 10 okvirom.

## 🏔️ Praktična Sigurnosna Obuka

Za praktično iskustvo implementacije sigurnosti, preporučamo **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - sveobuhvatnu vođenu ekspediciju za osiguranje MCP servera u Azureu koristeći metodologiju "ranjivost → eksploatacija → popravak → validacija".

Sve sigurnosne kontrole u ovom dokumentu usklađene su s **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, koja nudi referentne arhitekture i specifične smjernice za implementaciju u Azureu za OWASP MCP Top 10 rizike.

## **OBAVEZNI Sigurnosni Zahtjevi**

### **Kritične zabrane iz MCP Specifikacije:**

> **ZABRANJENO**: MCP serveri **NE SMEJU** prihvatiti bilo kakve tokene koji nisu izričito izdani za MCP server
>
> **ZABRANJENO**: MCP serveri **NE SMEJU** koristiti sesije za autentifikaciju  
>
> **OBAVEZNO**: MCP serveri koji provode autorizaciju **MORAJU** verificirati SVE dolazne zahtjeve
>
> **NEOPHODNO**: MCP proxy serveri koji koriste statični ID klijenta treće strane
> **MORAJU** dobiti suglasnost za svakog MCP klijenta prije prosljeđivanja autorizacije

---

## 1. **Kontrole Autentifikacije i Autorizacije**

### **Integracija vanjskih pružatelja identiteta**

**MCP Specifikacija `2026-07-28`** dopušta MCP serverima delegiranje
autentifikacije vanjskim pružateljima identiteta. Autorizacija za HTTP
transportere procjenjuje se po zahtjevu; lokalni stdio serveri umjesto toga dobivaju vjerodajnice
iz svoje okoline.

**OWASP MCP Rizik riješen**: [MCP07 - Nedostatna autentikacija i autorizacija](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Sigurnosne prednosti:**
1. **Eliminira rizike prilagođene autentifikacije**: Smanjuje ranjivost izbjegavanjem prilagođenih implementacija autentifikacije
2. **Sigurnost na razini poduzeća**: Koristi etablirane pružatelje identiteta poput Microsoft Entra ID s naprednim sigurnosnim značajkama
3. **Centralizirano upravljanje identitetom**: Pojednostavljuje upravljanje životnim ciklusom korisnika, kontrolu pristupa i reviziju usklađenosti
4. **Višefaktorska autentifikacija**: Nasljeđuje MFA mogućnosti od pružatelja identiteta poduzeća
5. **Uvjetne politike pristupa**: Koristi kontrole pristupa temeljene na riziku i adaptivnu autentifikaciju

**Zahtjevi za implementaciju:**
- **Registracija klijenta**: Preferirati dokumente o metapodacima ID klijenta ili
  predregistraciju; koristiti zastarjelu dinamičku registraciju klijenata samo za
  kompatibilnost
- **Validacija publike tokena**: Provjeriti da su svi tokeni izričito izdani za MCP server
- **Verifikacija izdavača**: Potvrditi da izdavač tokena odgovara očekivanom pružatelju identiteta
- **Provjera potpisa**: Kriptografska provjera integriteta tokena
- **Provedba isteka**: Strogo poštivanje rokova trajanja tokena
- **Validacija opsega**: Osigurati da tokeni sadrže odgovarajuće dozvole za tražene operacije

### **Sigurnost logike autorizacije**


**Kritične kontrole:**
- **Sveobuhvatni auditi autorizacije**: Redoviti sigurnosni pregledi svih točaka donošenja odluka o autorizaciji
- **Zadane postavke sigurne pri neuspjehu**: Odbij pristup kada logika autorizacije ne može donijeti konačnu odluku
- **Granice dopuštenja**: Jasna razgraničenja između različitih razina privilegija i pristupa resursima
- **Evidencija audita**: Potpuno bilježenje svih odluka autorizacije za sigurnosni nadzor
- **Redoviti pregledi pristupa**: Periodična validacija korisničkih dozvola i dodjela privilegija

## 2. **Sigurnost tokena i kontrole protiv prosljeđivanja**

**OWASP MCP rizik koji se rješava**: [MCP01 - Pogrešno upravljanje tokenima i izlaganje tajni](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Prevencija prosljeđivanja tokena**

**Prosljeđivanje tokena je izričito zabranjeno** u MCP specifikaciji autorizacije zbog kritičnih sigurnosnih rizika:

**Sigurnosni rizici koji se rješavaju:**
- **Zaobilaženje kontrola**: Zaobilazi ključne sigurnosne kontrole poput ograničenja brzine, validacije zahtjeva i nadzora prometa
- **Raspad odgovornosti**: Onemogućuje identifikaciju klijenta, kvareći audite i istrage incidenata
- **Eksfiltracija putem proxyja**: Omogućuje zlonamjernim akterima korištenje poslužitelja kao proxyja za neovlašteni pristup podacima
- **Povrede granica povjerenja**: Krši pretpostavke usluga niže razine o podrijetlu tokena
- **Lateralno kretanje**: Kompromitirani tokeni na više usluga omogućuju širenje napada

**Kontrole implementacije:**
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

### **Sigurni obrasci upravljanja tokenima**

**Najbolje prakse:**
- **Kratkotrajni tokeni**: Minimizirajte izloženi vremenski prozor čestom rotacijom tokena
- **Izdavanje "točno u vrijeme"**: Izdajte tokene samo kada su potrebni za specifične operacije
- **Sigurna pohrana**: Koristite hardverske sigurnosne module (HSM) ili sigurne upravitelje ključeva
- **Povezivanje tokena**: Provjeravajte publiku i izdavatelja tokena za namjenski MCP
  resurs, klijenta i operaciju
- **Nadzor i alarmiranje**: Detekcija u stvarnom vremenu zloupotrebe tokena ili neovlaštenih obrazaca pristupa

## 3. **Sigurnosne kontrole stanja aplikacije**

### **Prevencija otmice upravljačkog identifikatora**

**Adresirani vektori napada:**
- **Pogađanje identifikatora**: Predvidljivi identifikatori otkrivaju stanje drugog pozivatelja
- **Ponovna upotreba među korisnicima**: Ukradeni identifikator se koristi s drugačijim identitetom
- **Implicitna autorizacija**: Posjedovanje identifikatora se pogrešno smatra
  dokazom pristupa

**Kontrole upravljačkih identifikatora:**

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

**Sigurnost prijenosa:**
- **Obavezni HTTPS**: Za udaljene HTTP prijenose zahtijevajte HTTPS
- **Rukovanje vjerodajnicama**: Šaljite i validirajte autorizaciju na svakom HTTP zahtjevu
- **Izolacija stdio-a**: Zaštitite lokalne stdio poslužitelje kroz izolaciju procesa i
  kontrole vjerodajnica okoline

### **Razmatranja između stanja s i bez stanja**

MCP `2026-07-28` je bezstanje na razini protokola. Aplikacije ipak mogu
održavati stanje vraćanjem eksplicitnog identifikatora iz jednog poziva alata i prihvaćanjem
kao običnog argumenta u kasnijim pozivima.

- Pohranite stanje neovisno o bilo kojoj pojedinačnoj transportnoj vezi.
- Vežite identifikatore stanja za autentificiranog klijenta na poslužiteljskoj strani.
- Tretirajte identifikator kao ime, a ne kao vjerodajnicu nositelja.
- Definirajte ponašanje isteka i oporavka za zastarjele identifikatore.

## 4. **Sigurnosne kontrole specifične za AI**

**Rizici OWASP MCP adresirani:** 

- [MCP06 - Subverzija toka namjere](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Trovanje alata](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Umetanje i izvršavanje naredbi](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Obrana od unosa naredbi**

**Integracija Microsoft Prompt Shields-a:**
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

**Kontrole implementacije:**
- **Sanitacija unosa**: Sveobuhvatna validacija i filtriranje svih korisničkih unosa
- **Definicija granica sadržaja**: Jasna odvojenost između sistemskih uputa i korisničkog sadržaja
- **Hijerarhija uputa**: Ispravna pravila prioriteta za sukobljene upute
- **Nadzor izlaza**: Otkrivanje potencijalno štetnih ili manipuliranih izlaza

### **Prevencija trovanja alata**

**Sigurnosni okvir za alate:**
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

**Dinamičko upravljanje alatima:**
- **Radni tokovi odobrenja**: Izričiti korisnički pristanak za izmjene alata
- **Mogućnost vraćanja unazad**: Mogućnost povratka na prethodne verzije alata
- **Revizija promjena**: Potpuna povijest izmjena definicija alata
- **Procjena rizika**: Automatizirana evaluacija sigurnosnog stanja alata

## 5. **Prevencija napada zbrkanog zamjenika**

### **Sigurnost OAuth proxy-ja**

**Kontrole za prevenciju napada:**
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

**Zahtjevi implementacije:**
- **Registracija klijenta**: Prednost pri pre-registraciji ili dokumentima Client ID metapodataka
  ; tretirati dinamičku registraciju klijenta kao kompatibilni fallback
- **Verifikacija korisničkog pristanka**: MCP proxy-ji koji koriste statični treći klijentski ID
  moraju dobiti pristanak po klijentu prije prosljeđivanja autorizacije
- **Validacija URI preusmjeravanja**: Stroga validacija ciljeva preusmjeravanja na temelju bijele liste
- **Zaštita autorizacijskog koda**: Kratkotrajni kodovi s provedbom jednokratne upotrebe
- **Verifikacija identiteta klijenta**: Robusna validacija vjerodajnica i metapodataka klijenta

## 6. **Sigurnost izvršavanja alata**

### **Sandboxing i izolacija**

**Izolacija zasnovana na kontejnerima:**
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

**Izolacija procesa:**
- **Odvojeni konteksti procesa**: Svako izvršavanje alata u izoliranom prostoru procesa
- **Međuprocesna komunikacija**: Sigurni IPC mehanizmi s validacijom
- **Nadzor procesa**: Analiza ponašanja u runtime-u i otkrivanje anomalija
- **Provođenje ograničenja resursa**: Stroga ograničenja na CPU, memoriju i I/O operacije

### **Implementacija načela najmanjih privilegija**

**Upravljanje dopuštenjima:**
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

## 7. **Kontrole sigurnosti lanca opskrbe**

**Rizik OWASP MCP adresiran**: [MCP04 - Napadi na lanac opskrbe softverom i manipulacija ovisnostima](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Provjera ovisnosti**

**Sveobuhvatna sigurnost komponenti:**
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

### **Kontinuirani nadzor**

**Otkrivanje prijetnji u lancu opskrbe:**
- **Praćenje zdravlja ovisnosti**: Kontinuirana procjena svih ovisnosti u smislu sigurnosnih problema
- **Integracija obavještajnih podataka o prijetnjama**: Ažuriranja u stvarnom vremenu o novim prijetnjama u lancu opskrbe
- **Analiza ponašanja**: Otkrivanje neuobičajenog ponašanja u vanjskim komponentama
- **Automatski odgovor**: Trenutno suzbijanje kompromitiranih komponenti

## 8. **Kontrole nadzora i otkrivanja**

**Rizik OWASP MCP adresiran**: [MCP08 - Nedostatak revizije i telemetrije](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Upravljanje sigurnosnim informacijama i događajima (SIEM)**

**Sveobuhvatna strategija zapisivanja:**
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

### **Otkrivanje prijetnji u stvarnom vremenu**

**Analitika ponašanja:**
- **Analiza ponašanja korisnika (UBA)**: Otkrivanje neuobičajenih obrazaca pristupa korisnika
- **Analiza ponašanja entiteta (EBA)**: Nadzor ponašanja MCP servera i alata
- **Otkrivanje anomalija pomoću strojnog učenja**: Prepoznavanje sigurnosnih prijetnji vođeno umjetnom inteligencijom
- **Korelacija obavještajnih podataka o prijetnjama**: Usporedba zapaženih aktivnosti s poznatim obrascima napada

## 9. **Odgovor na incidente i oporavak**

### **Automatizirane sposobnosti odgovora**

**Radnje trenutnog odgovora:**
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

### **Forenzičke sposobnosti**

**Podrška za istrage:**
- **Čuvanje zapisa audit staze**: Nepromjenjivo zapisivanje s kriptografskim integritetom
- **Prikupljanje dokaza**: Automatizirano sakupljanje relevantnih sigurnosnih artefakata
- **Rekonstrukcija vremenske linije**: Detaljan slijed događaja koji su doveli do sigurnosnih incidenata
- **Procjena utjecaja**: Evaluacija obuhvata kompromisa i izloženosti podataka

## **Ključna načela sigurnosne arhitekture**

### **Obrana u dubini**
- **Višestruki sigurnosni slojevi**: Nema jedne točke kvara u sigurnosnoj arhitekturi
- **Redundantne kontrole**: Preklapajući sigurnosni mehanizmi za kritične funkcije
- **Mehanizmi za siguran pad**: Sigurne zadane postavke kada sustavi naiđu na pogreške ili napade

### **Implementacija Zero Trust načela**
- **Nikad ne vjeruj, uvijek provjeri**: Kontinuirana validacija svih entiteta i zahtjeva
- **Načelo najmanjih privilegija**: Minimalna prava pristupa za sve komponente
- **Mikrosegmentacija**: Granularne kontrole mreže i pristupa

### **Kontinuirana evolucija sigurnosti**
- **Prilagodba krajoliku prijetnji**: Redovita ažuriranja za adresiranje novih prijetnji
- **Učinkovitost sigurnosnih kontrola**: Stalna evaluacija i poboljšanje kontrola
- **Usuglašenost sa specifikacijama**: Prilagodba rastućim MCP sigurnosnim standardima

---

## **Resursi za implementaciju**

### **Službena MCP dokumentacija**
- [MCP specifikacija (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Najbolje sigurnosne prakse MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specifikacija autorizacije MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP sigurnosni resursi**
- [OWASP MCP Azure sigurnosni vodič](https://microsoft.github.io/mcp-azure-security-guide/) - Sveobuhvatni OWASP MCP Top 10 s Azure implementacijom
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Službeni OWASP MCP sigurnosni rizici
- [MCP Security Summit radionica (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktična sigurnosna obuka za MCP na Azureu

### **Microsoft sigurnosna rješenja**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Sigurnosni standardi**
- [Najbolje prakse sigurnosti OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 za velike jezične modele](https://genai.owasp.org/)

- [NIST Okvir za kibernetičku sigurnost](https://www.nist.gov/cyberframework)

---

> **Važno:** Ove sigurnosne kontrole odražavaju MCP specifikaciju
> `2026-07-28`. Uvijek provjerite protiv
> [trenutne službene dokumentacije](https://modelcontextprotocol.io/specification/2026-07-28/)
> jer se standardi kontinuirano razvijaju.

## Što slijedi

- Povratak na: [Pregled sigurnosnog modula](./README.md)
- Nastavi na: [Modul 3: Početak rada](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->