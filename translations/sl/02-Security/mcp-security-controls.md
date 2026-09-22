# Varnostni nadzor MCP - Posodobitev september 2026

> **Trenutni standard:** Ta dokument odraža
> [Specifikacijo MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> in uradne
> [Najboljše varnostne prakse MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Protokol Model Context (MCP) je močno dozorel z izboljšanimi nadzori varnosti, ki obravnavajo tako tradicionalno varnost programske opreme kot tudi grožnje, specifične za umetno inteligenco. Ta dokument zagotavlja celovite varnostne nadzore za varne implementacije MCP v skladu z okvirjem OWASP MCP Top 10.

## 🏔️ Praktična varnostna usposabljanja

Za praktične izkušnje z varnostno implementacijo priporočamo **[Delavnico MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** – celovito vodeno odpravo za varovanje MCP strežnikov v Azure z metodologijo »ranljiv → izkoriščen → popravljen → potrjen«.

Vsi varnostni nadzori v tem dokumentu so usklajeni z **[Vodnikom za varnost MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, ki nudi referenčne arhitekture in specifike za implementacijo v Azure za tveganja OWASP MCP Top 10.

## **OBVEZNE varnostne zahteve**

### **Kritične prepovedi iz specifikacije MCP:**

> **ZAPOVEDANO:** MCP strežniki **NE SMEJO** sprejemati tokenov, ki niso izrecno izdani za MCP strežnik
>
> **PREPOVEDANO:** MCP strežniki **NE SMEJO** uporabljati sej za avtentikacijo  
>
> **ZAHTEVANO:** MCP strežniki, ki izvajajo pooblastila, **MORAJO** preveriti VSE dohodne zahteve
>
> **OBVEZNO:** MCP proxy strežniki, ki uporabljajo statični ID odjemalca tretje osebe,
> **MORAJO** pridobiti soglasje za vsakega MCP odjemalca pred posredovanjem pooblastila

---

## 1. **Nadzor avtentikacije in pooblastila**

### **Integracija zunanjega ponudnika identitet**

**Specifikacija MCP `2026-07-28`** dovoljuje MCP strežnikom delegiranje
avtentikacije zunanjim ponudnikom identitet. Pooblastila za HTTP
prenose se ocenjujejo za posamezno zahtevo; lokalni stdio strežniki dobijo poverilnice
iz svojega okolja.

**Naslovljeno tveganje OWASP MCP**: [MCP07 - nezadostna avtentikacija in pooblastila](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Varnostne koristi:**
1. **Odpravlja tveganja lastnih avtentikacij**: Zmanjšuje površino ranljivosti z izogibanjem lastnim implementacijam avtentikacije
2. **Varnost podjetniške ravni**: Izkorišča uveljavljene ponudnike identitet, kot je Microsoft Entra ID, z naprednimi varnostnimi funkcijami
3. **Centralizirano upravljanje identitet**: Poenostavlja upravljanje življenjskega cikla uporabnikov, nadzor dostopa in revizijo skladnosti
4. **Večfaktorska avtentikacija**: Deduje zmogljivosti MFA od podjetniških ponudnikov identitet
5. **Pogojevanje politik dostopa**: Izkorišča nadzore dostopa na podlagi tveganja in prilagodljivo avtentikacijo

**Zahteve za implementacijo:**
- **Registracija odjemalca**: Prednost naj imajo dokumenti z metapodatki ID odjemalca ali
  predregistracija; zastarelo dinamično registracijo odjemalcev uporabite samo za
  združljivost
- **Preverjanje občinstva tokena**: Preverite, da so vsi tokeni izrecno izdani za MCP strežnik
- **Preverjanje izdajatelja**: Potrdite, da izdajatelj tokena ustreza pričakovanemu ponudniku identitet
- **Preverjanje podpisa**: Kriptografsko preverjanje celovitosti tokena
- **Uveljavljanje poteka**: Strogo uveljavljanje omejitev življenjske dobe tokena
- **Preverjanje obsega**: Zagotovite, da tokeni vsebujejo primerna dovoljenja za zahtevane operacije

### **Varnost logike pooblastil**


**Kritični nadzorni ukrepi:**
- **Celovite revizije pooblastil**: Redni varnostni pregledi vseh točk odločanja o pooblastilih
- **Privzete nastavitve za zaščito**: Zavrni dostop, kadar logika pooblastil ne more podati dokončne odločitve
- **Meje dovoljenj**: Jasna ločitev med različnimi ravnmi privilegijev in dostopom do virov
- **Revizijsko beleženje**: Popolno beleženje vseh odločitev o pooblastilih za varnostno spremljanje
- **Redni pregledi dostopa**: Občasna potrjevanja uporabniških dovoljenj in dodelitev privilegijev

## 2. **Varnost žetonov in nadzor proti posredovanju**

**Naslavljano tveganje OWASP MCP**: [MCP01 - Nepravilno upravljanje žetonov in razkritje skrivnosti](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Preprečevanje posredovanja žetonov**

**Posredovanje žetonov je izrecno prepovedano** v specifikaciji dovoljenj MCP zaradi kritičnih varnostnih tveganj:

**Naslavljena varnostna tveganja:**
- **Zaobidenje nadzora**: Zaobide bistvene varnostne kontrole, kot so omejevanje hitrosti, preverjanje zahtevkov in spremljanje prometa
- **Razočaranje odgovornosti**: Onemogoči identifikacijo odjemalca, pokvari revizijske sledi in preiskave incidentov
- **Izvoz preko proxyja**: Omogoča zlonamernim akterjem uporabo strežnikov kot proxyjev za nepooblaščen dostop do podatkov
- **Kršitve zaupanja**: Podira predpostavke o izvoru žetona v zaupanih storitvah nižjega sloja
- **Lateralno premikanje**: Kompromitirani žetoni med več storitvami omogočajo širitev napada

**Kontrole za izvedbo:**
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
- **Izdaja natanko pravočasno**: Izdajajte žetone le, ko so potrebni za specifične operacije
- **Varnostno shranjevanje**: Uporaba strojnih varnostnih modulov (HSM) ali varnih ključnih zakladnic
- **Povezava žetona**: Preverite občinstvo in izdajatelja žetona za namenjeni MCP
  vir, odjemalca in operacijo
- **Spremljanje in opozarjanje**: Zaznavanje zlorab žetonov ali nepooblaščenih vzorcev dostopa v realnem času

## 3. **Nadzor varnosti stanja aplikacije**

### **Preprečevanje prevzema upravljanja stanja**

**Naslavljeni vektorji napadov:**
- **Ugibanje upravljanja**: Napovedljivi identifikatorji razkrijejo stanje drugega klicatelja
- **Ponovna uporaba med uporabniki**: Ukradeno upravljanje se uporabi z drugo identiteto
- **Implicitna pooblastila**: Lastništvo upravljanja se nepravilno obravnava kot
  dokaz dostopa

**Kontrole upravljanja stanja:**

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

**Varnost prenosa:**
- **Zahteva HTTPS**: Zahtevajte HTTPS za oddaljene HTTP prenose
- **Ravnanje z poverilnicami**: Pošiljajte in preverjajte pooblastila ob vsakem HTTP zahtevku
- **Izolacija stdio**: Zaščitite lokalne stdio strežnike s procesno izolacijo in
  nadzorom poverilnic okolja

### **Razmisleki o stanju z ali brez stanja**

MCP `2026-07-28` je brezstaničen na protokolarni ravni. Aplikacije lahko
vseeno ohranjajo stanje z vračanjem eksplicitnega upravljanja iz enega klica orodja in njegovo sprejemanje
kot običajen argument pri kasnejših klicih.

- Shranjujte stanje neodvisno od katerega koli posameznega prenosnega povezave.
- Povežite upravljanje stanj s preverjenim glavnim strežnikom.
- Obdelujte upravljanje kot ime, ne kot poverilnico nosilca.
- Določite potečevalne in obnovitvene obnašanje za zastarela upravljanja.

## 4. **Nadzor varnosti specifičen za AI**

**Naslavljena tveganja OWASP MCP**:

- [MCP06 - Subverzija poteka namere](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Zastrupljanje orodij](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Vbrizgavanje ukazov in izvajanje](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Obramba pred vbrizgavanjem pozivov**

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

**Kontrole izvajanja:**
- **Čiščenje vhodov**: Celovita validacija in filtriranje vseh uporabniških vhodov
- **Določitev mej vsebine**: Jasna ločitev med sistemskimi navodili in uporabniško vsebino
- **Hierarhija navodil**: Pravilna pravila prednosti za nasprotujoča si navodila
- **Nadzor izhoda**: Zaznavanje potencialno škodljivih ali manipuliranih izhodov

### **Preprečevanje zastrupljanja orodij**

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
- **Procesi odobritve**: Izrecno soglasje uporabnika za spremembe orodij
- **Možnosti razveljavitve**: Možnost povrnitve na prejšnje različice orodij
- **Revizija sprememb**: Popolna zgodovina sprememb definicij orodij
- **Ocenjevanje tveganj**: Avtomatizirana ocena varnostnega stanja orodij

## 5. **Preprečevanje napada z zmedeno pooblastitvijo »

### **Varnost proxy OAuth**

**Kontrole za preprečevanje napadov:**
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

**Zahteve za izvedbo:**
- **Registracija klienta**: Prednost predregistracije ali metapodatkov ID klienta
  Dokumenti; dinamična registracija klienta kot združljivostna rezerva
- **Preverjanje uporabniškega soglasja**: MCP proxyji z uporabo statičnega ID tretje osebe
  morajo pridobiti soglasje za posamezen klient pred posredovanjem avtorizacije
- **Validacija URI za preusmeritev**: Stroga validacija destinacij preusmeritve na podlagi bele liste
- **Zaščita avtorizacijskih kod**: Kodice z omejeno življenjsko dobo in uveljavitvijo enkratne uporabe
- **Preverjanje identitete klienta**: Močna validacija poverilnic in metapodatkov klienta

## 6. **Varnost izvajanja orodij**

### **Peskovnik in izolacija**

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
- **Ločeni konteksti procesov**: Vsako izvajanje orodja v izoliranem prostoru procesa
- **Medprocesna komunikacija**: Varni mehanizmi IPC z validacijo
- **Nadzor procesov**: Analiza vedenja med izvajanjem in zaznavanje anomalij
- **Uveljavljanje virov**: Strogi limiti za CPU, pomnilnik in I/O operacije

### **Izvedba najmanjših privilegijev**

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

## 7. **Kontrole varnosti dobavne verige**

**Naslovljeno tveganje OWASP MCP**: [MCP04 - Napadi fotografskih verig in manipulacija odvisnosti](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

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

### **Neprekinjeno spremljanje**

**Zaznavanje groženj v dobavni verigi:**
- **Spremljanje stanja odvisnosti**: Neprestana ocena vseh odvisnosti glede varnostnih težav
- **Integracija obveščevalnih podatkov o grožnjah**: Posodobitve v realnem času o nastajajočih grožnjah v dobavni verigi
- **Vedenjska analiza**: Zaznavanje nenavadnega vedenja v zunanjih komponentah
- **Samodejni odziv**: Takojšnja zajezitev kompromitiranih komponent

## 8. **Kontrole nadzora in zaznavanja**

**Naslovljeno tveganje OWASP MCP**: [MCP08 - Pomanjkanje revizije in telemetrije](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Upravljanje varnostnih informacij in dogodkov (SIEM)**

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
- **Analitika vedenja uporabnikov (UBA)**: Zaznavanje nenavadnih vzorcev uporabniškega dostopa
- **Analitika vedenja entitet (EBA)**: Spremljanje vedenja MCP strežnika in orodij
- **Zaznavanje anomalij z učenjem stroja**: Identifikacija varnostnih groženj z umetno inteligenco
- **Korelacija obveščevalnih podatkov o grožnjah**: Ujemanje opaženih dejavnosti z znanimi vzorci napadov

## 9. **Odziv na incidente in okrevanje**

### **Samodejne odzivne sposobnosti**

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

### **Forenzične sposobnosti**

**Podpora preiskavi:**
- **Ohranjanje revizijske sledi**: Neprekinjeno beleženje z uporabo kriptografske integritete
- **Zbiranje dokazov**: Samodejno zbiranje relevantnih varnostnih artefaktov
- **Rekonstrukcija časovnice**: Podroben zaporedje dogodkov, ki vodijo do varnostnih incidentov
- **Ocenjevanje vpliva**: Ocena obsega kompromisa in izpostavljenosti podatkov

## **Ključna načela varnostne arhitekture**

### **Obramba v globino**
- **Več plasti varnosti**: Brez enotne točke okvare v varnostni arhitekturi
- **Podvojene kontrole**: Prekrivajoči varnostni ukrepi za kritične funkcije
- **Mehanizmi za varno delovanje**: Varnostne privzete vrednosti pri napakah ali napadih

### **Izvedba ničelnega zaupanja (Zero Trust)**
- **Nikoli ne zaupi, vedno preveri**: Neprestano preverjanje vseh entitet in zahtevkov
- **Načelo najmanjših privilegijev**: Minimalne pravice dostopa za vse komponente
- **Mikrosegmentacija**: Granularna omrežna in dostopna kontrola

### **Neprestana varnostna evolucija**
- **Prilagoditev pokrajini groženj**: Redne posodobitve za obravnavo nastajajočih groženj
- **Učinkovitost varnostnih kontrol**: Nenehno ocenjevanje in izboljševanje kontrol
- **Skladnost s specifikacijami**: Usmerjenost na razvijajoče se MCP varnostne standarde

---

## **Viri za izvedbo**

### **Uradna MCP dokumentacija**
- [MCP Specifikacija (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Najboljše varnostne prakse MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specifikacija avtorizacije MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP varnostni viri**
- [OWASP MCP Azure varnostni vodič](https://microsoft.github.io/mcp-azure-security-guide/) - Celovit OWASP MPC Top 10 z implementacijo v Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Uradne varnostne nevarnosti OWASP MCP
- [Delavnica MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktično varnostno usposabljanje za MCP na Azure

### **Microsoftove varnostne rešitve**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Varnostni standardi**
- [OAuth 2.0 Najboljše varnostne prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 za velike jezikovne modele](https://genai.owasp.org/)

- [Okvir NIST za kibernetsko varnost](https://www.nist.gov/cyberframework)

---

> **Pomembno:** Ti varnostni nadzori odražajo specifikacijo MCP
> `2026-07-28`. Vedno preverite glede na
> [trenutno uradno dokumentacijo](https://modelcontextprotocol.io/specification/2026-07-28/)
> saj se standardi še naprej razvijajo.

## Kaj sledi

- Vrni se na: [Pregled varnostnega modula](./README.md)
- Nadaljuj na: [Modul 3: Začetek](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->