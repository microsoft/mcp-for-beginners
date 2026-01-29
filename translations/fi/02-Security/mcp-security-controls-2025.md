# MCP:n tietoturvakontrollit – joulukuu 2025 päivitys

> **Nykyinen standardi**: Tämä asiakirja heijastaa [MCP-spesifikaation 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) tietoturvavaatimuksia ja virallisia [MCP:n tietoturvan parhaat käytännöt](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) on kehittynyt merkittävästi parannettujen tietoturvakontrollien myötä, jotka käsittelevät sekä perinteistä ohjelmistoturvaa että tekoälyyn liittyviä uhkia. Tämä asiakirja tarjoaa kattavat tietoturvakontrollit turvallisille MCP-toteutuksille joulukuusta 2025 alkaen.

## **VELVOITTAVAT tietoturvavaatimukset**

### **Kriittiset kieltoja MCP-spesifikaatiosta:**

> **KIELLETTY**: MCP-palvelimet **EIVÄT SAA** hyväksyä mitään tunnuksia, joita ei ole nimenomaisesti myönnetty MCP-palvelimelle  
>
> **KIELLETTY**: MCP-palvelimet **EIVÄT SAA** käyttää istuntoja todennukseen  
>
> **VAADITTU**: MCP-palvelimet, jotka toteuttavat valtuutuksen, **MUSTA** tarkistaa KAIKKI saapuvat pyynnöt  
>
> **VELVOITTAVA**: MCP-välityspalvelimet, jotka käyttävät staattisia asiakastunnuksia, **MUSTA** hankkia käyttäjän suostumus jokaiselle dynaamisesti rekisteröidylle asiakkaalle

---

## 1. **Todennus- ja valtuutuskontrollit**

### **Ulkoinen identiteetin tarjoajan integrointi**

**Nykyinen MCP-standardi (2025-06-18)** sallii MCP-palvelimien delegoida todennuksen ulkoisille identiteetin tarjoajille, mikä on merkittävä tietoturvaparannus:

### **Ulkoinen identiteetin tarjoajan integrointi**

**Nykyinen MCP-standardi (2025-11-25)** sallii MCP-palvelimien delegoida todennuksen ulkoisille identiteetin tarjoajille, mikä on merkittävä tietoturvaparannus:

**Tietoturvaedut:**
1. **Poistaa räätälöidyn todennuksen riskit**: Vähentää haavoittuvuuspintaa välttämällä räätälöityjä todennuksen toteutuksia  
2. **Yritystason tietoturva**: Hyödyntää vakiintuneita identiteetin tarjoajia kuten Microsoft Entra ID, joissa on kehittyneet tietoturvaominaisuudet  
3. **Keskitetty identiteetin hallinta**: Yksinkertaistaa käyttäjän elinkaaren hallintaa, pääsynvalvontaa ja vaatimustenmukaisuuden tarkastuksia  
4. **Monivaiheinen todennus**: Perii MFA-ominaisuudet yrityksen identiteetin tarjoajilta  
5. **Ehdolliset pääsypolitiikat**: Hyödyntää riskipohjaisia pääsynvalvontoja ja adaptiivista todennusta

**Toteutusvaatimukset:**
- **Tunnuksen kohdeyleisön validointi**: Varmista, että kaikki tunnukset on nimenomaisesti myönnetty MCP-palvelimelle  
- **Myöntäjän varmennus**: Vahvista, että tunnuksen myöntäjä vastaa odotettua identiteetin tarjoajaa  
- **Allekirjoituksen tarkistus**: Kryptografinen validointi tunnuksen eheydestä  
- **Vanhentumisen valvonta**: Tiukka tunnuksen voimassaoloajan noudattaminen  
- **Laajuuden validointi**: Varmista, että tunnuksissa on asianmukaiset oikeudet pyydettyihin toimiin

### **Valtuutuslogiikan tietoturva**

**Kriittiset kontrollit:**
- **Kattavat valtuutustarkastukset**: Säännölliset tietoturvakatselmukset kaikista valtuutuspäätöspisteistä  
- **Vikasietoisuus oletuksena**: Estä pääsy, jos valtuutuslogiikka ei pysty tekemään selkeää päätöstä  
- **Oikeuksien rajat**: Selkeä erottelu eri käyttöoikeustasojen ja resurssien pääsyn välillä  
- **Auditointilokit**: Kaikkien valtuutuspäätösten täydellinen lokitus tietoturvaseurantaa varten  
- **Säännölliset pääsyn tarkastukset**: Käyttäjäoikeuksien ja valtuuksien ajantasainen validointi

## 2. **Tunnusten tietoturva ja anti-passthrough-kontrollit**

### **Tunnusten läpiviennin estäminen**

**Tunnusten läpivienti on nimenomaisesti kielletty** MCP:n valtuutusspesifikaatiossa kriittisten tietoturvariskien vuoksi:

**Käsitellyt tietoturvariskit:**
- **Kontrollien kiertäminen**: Ohittaa olennaiset tietoturvakontrollit kuten nopeusrajoitukset, pyyntöjen validoinnin ja liikenteen seurannan  
- **Vastuullisuuden katoaminen**: Estää asiakkaan tunnistamisen, mikä turmelee auditointijäljet ja tapaustutkinnan  
- **Välityspalvelinperusteinen tiedon kalastelu**: Mahdollistaa haitallisten toimijoiden käyttää palvelimia välityspalvelimina luvattomaan tiedon saantiin  
- **Luottamusrajojen rikkominen**: Rikkoo jälkijohteisten palveluiden oletuksia tunnusten alkuperästä  
- **Sivuttaisliike**: Kompromettoitujen tunnusten käyttö useissa palveluissa laajentaa hyökkäystä

**Toteutuskontrollit:**
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

### **Turvalliset tunnusten hallintamallit**

**Parhaat käytännöt:**
- **Lyhytkestoiset tunnukset**: Minimoi altistusaika tiheällä tunnusten kierrätyksellä  
- **Tarpeen mukaan myöntäminen**: Myönnä tunnukset vain tarvittaessa tiettyihin toimiin  
- **Turvallinen tallennus**: Käytä laitteistoturvamoduuleja (HSM) tai turvallisia avainholveja  
- **Tunnusten sitominen**: Sido tunnukset tiettyihin asiakkaisiin, istuntoihin tai toimiin mahdollisuuksien mukaan  
- **Seuranta ja hälytykset**: Reaaliaikainen tunnusten väärinkäytön tai luvattoman käytön havaitseminen

## 3. **Istuntojen tietoturvakontrollit**

### **Istunnon kaappauksen estäminen**

**Käsitellyt hyökkäysvektorit:**
- **Istunnon kaappauksen kehotteen injektio**: Haitallisten tapahtumien injektointi jaettuun istuntotilaan  
- **Istunnon väärentäminen**: Luvaton varastettujen istunto-ID:iden käyttö todennuksen ohittamiseksi  
- **Jatkuvien virtojen hyökkäykset**: Palvelimen lähettämien tapahtumien jatkamisen hyväksikäyttö haitallisen sisällön injektointiin

**Pakolliset istuntokontrollit:**
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

**Siirtoturva:**
- **HTTPS:n pakollisuus**: Kaikki istuntoviestintä TLS 1.3 -yhteydellä  
- **Turvalliset evästeominaisuudet**: HttpOnly, Secure, SameSite=Strict  
- **Sertifikaattien pinnaus**: Kriittisissä yhteyksissä MITM-hyökkäysten estämiseksi

### **Tilalliset vs tilattomat näkökohdat**

**Tilallisille toteutuksille:**
- Jaettu istuntotila vaatii lisäsuojaa injektiohyökkäyksiä vastaan  
- Jonopohjainen istuntohallinta tarvitsee eheyden varmistuksen  
- Useat palvelininstanssit vaativat turvallisen istuntotilan synkronoinnin

**Tilattomille toteutuksille:**
- JWT- tai vastaava tunnuspohjainen istuntohallinta  
- Kryptografinen istuntotilan eheyden tarkistus  
- Pienempi hyökkäyspinta, mutta vaatii vahvan tunnusten validoinnin

## 4. **Tekoälyyn liittyvät tietoturvakontrollit**

### **Kehotteen injektion puolustus**

**Microsoft Prompt Shields -integraatio:**
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

**Toteutuskontrollit:**
- **Syötteen puhdistus**: Kaikkien käyttäjäsisältöjen kattava validointi ja suodatus  
- **Sisällön rajaus**: Selkeä erottelu järjestelmäohjeiden ja käyttäjäsisällön välillä  
- **Ohjeiden hierarkia**: Oikea etusijajärjestys ristiriitaisille ohjeille  
- **Tulosten seuranta**: Haitallisten tai manipuloitujen tulosten havaitseminen

### **Työkalujen myrkytyksen estäminen**

**Työkalujen tietoturvakehys:**
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

**Dynaaminen työkalujen hallinta:**
- **Hyväksyntätyönkulut**: Käyttäjän nimenomainen suostumus työkalumuutoksille  
- **Palautusmahdollisuudet**: Mahdollisuus palauttaa aiempiin työkaluversion tiloihin  
- **Muutosten auditointi**: Täydellinen historia työkalumäärittelyjen muutoksista  
- **Riskinarviointi**: Automaattinen työkalujen tietoturvan tilan arviointi

## 5. **Confused Deputy -hyökkäyksen estäminen**

### **OAuth-välityspalvelimen tietoturva**

**Hyökkäyksen estokontrollit:**
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

**Toteutusvaatimukset:**
- **Käyttäjän suostumuksen varmistus**: Älä koskaan ohita suostumusnäyttöjä dynaamisessa asiakasrekisteröinnissä  
- **Redirect URI:n validointi**: Tiukka valkoinen lista uudelleenohjauskohteiden tarkistukseen  
- **Valtuutuskoodin suojaus**: Lyhytkestoiset koodit, jotka ovat kertakäyttöisiä  
- **Asiakkaan identiteetin varmennus**: Vahva asiakastunnusten ja metatietojen validointi

## 6. **Työkalujen suoritusturva**

### **Säilötys ja eristäminen**

**Konttipohjainen eristäminen:**
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

**Prosessieristys:**
- **Eri prosessikontekstit**: Jokainen työkalun suoritus eristetyssä prosessitilassa  
- **Prosessien välinen viestintä**: Turvalliset IPC-mekanismit validoinnilla  
- **Prosessien valvonta**: Suorituksen käyttäytymisen analysointi ja poikkeamien havaitseminen  
- **Resurssien valvonta**: Tiukat rajat CPU:lle, muistille ja I/O-toiminnoille

### **Vähimmän oikeuden periaatteen toteutus**

**Oikeuksien hallinta:**
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

## 7. **Toimitusketjun tietoturvakontrollit**

### **Riippuvuuksien varmennus**

**Kattava komponenttien tietoturva:**
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

### **Jatkuva seuranta**

**Toimitusketjun uhkien havaitseminen:**
- **Riippuvuuksien terveystilan seuranta**: Kaikkien riippuvuuksien jatkuva arviointi tietoturvaongelmien varalta  
- **Uhkatiedon integrointi**: Reaaliaikaiset päivitykset nousevista toimitusketjuuhkista  
- **Käyttäytymisanalyysi**: Epätavallisen käyttäytymisen havaitseminen ulkoisissa komponenteissa  
- **Automaattinen reagointi**: Välitön kompromettoitujen komponenttien eristäminen

## 8. **Seuranta- ja havaitsemiskontrollit**

### **Tietoturvatiedon ja tapahtumien hallinta (SIEM)**

**Kattava lokitusstrategia:**
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

### **Reaaliaikainen uhkien havaitseminen**

**Käyttäytymisanalytiikka:**
- **Käyttäjäkäyttäytymisen analytiikka (UBA)**: Epätavallisten käyttäjäpääsykuvioiden havaitseminen  
- **Entiteettikäyttäytymisen analytiikka (EBA)**: MCP-palvelimen ja työkalujen käyttäytymisen seuranta  
- **Koneoppimiseen perustuva poikkeamien havaitseminen**: Tekoälypohjainen tietoturvauhkaiden tunnistus  
- **Uhkatiedon korrelaatio**: Havainnoitujen toimintojen vertailu tunnettuun hyökkäysmalliin

## 9. **Häiriötilanteiden hallinta ja palautuminen**

### **Automaattiset reagointikyvyt**

**Välittömät reagointitoimet:**
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

### **Forensiikkakyvyt**

**Tutkinnan tuki:**
- **Auditointijälkien säilytys**: Muuttumaton lokitus kryptografisella eheydellä  
- **Todisteiden keruu**: Automaattinen olennaisten tietoturva-artefaktien keruu  
- **Aikajanan rekonstruointi**: Yksityiskohtainen tapahtumaketju tietoturvaloukkauksiin johtaneista tapahtumista  
- **Vaikutusarviointi**: Kompromissin laajuuden ja tietovuodon arviointi

## **Keskeiset tietoturva-arkkitehtuurin periaatteet**

### **Syvyyteen puolustautuminen**
- **Useita tietoturvakerroksia**: Ei yksittäistä vikaantumispistettä tietoturva-arkkitehtuurissa  
- **Redundantit kontrollit**: Päällekkäiset tietoturvatoimenpiteet kriittisissä toiminnoissa  
- **Vikasietoisuusmekanismit**: Turvalliset oletukset virhe- tai hyökkäystilanteissa

### **Zero Trust -toteutus**
- **Älä koskaan luota, varmista aina**: Jatkuva kaikkien toimijoiden ja pyyntöjen validointi  
- **Vähimmän oikeuden periaate**: Minimoi kaikkien komponenttien käyttöoikeudet  
- **Mikrosegmentointi**: Tarkat verkko- ja pääsynvalvonnat

### **Jatkuva tietoturvan kehitys**
- **Uhkakentän mukautuminen**: Säännölliset päivitykset nousevien uhkien käsittelemiseksi  
- **Tietoturvakontrollien tehokkuus**: Kontrollien jatkuva arviointi ja parantaminen  
- **Spesifikaation noudattaminen**: Yhdenmukaisuus kehittyvien MCP-tietoturvastandardien kanssa

---

## **Toteutusresurssit**

### **Virallinen MCP-dokumentaatio**
- [MCP-spesifikaatio (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP:n tietoturvan parhaat käytännöt](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP:n valtuutusspesifikaatio](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoftin tietoturvaratkaisut**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Tietoturvastandardit**
- [OAuth 2.0:n tietoturvan parhaat käytännöt (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 suurille kielimalleille](https://genai.owasp.org/)
- [NIST:n kyberturvallisuuskehys](https://www.nist.gov/cyberframework)

---

> **Tärkeää**: Nämä tietoturvakontrollit heijastavat nykyistä MCP-spesifikaatiota (2025-06-18). Tarkista aina viimeisimmät [viralliset dokumentit](https://spec.modelcontextprotocol.io/), sillä standardit kehittyvät nopeasti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->