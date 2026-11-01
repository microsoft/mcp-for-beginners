# MCP-turvavalvonta - Päivitys syyskuu 2026

> **Voimassa oleva standardi:** Tämä dokumentti noudattaa
> [MCP-määrittelyä 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> ja virallista
> [MCP-turvakäytäntöjä](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Model Context Protocol (MCP) on kehittynyt merkittävästi sisältäen parannettuja turvavalvontoja, jotka käsittelevät sekä perinteistä ohjelmistoturvallisuutta että AI-kohtaisia uhkia. Tämä dokumentti tarjoaa kattavat turvavalvonnat turvallisiin MCP-toteutuksiin, jotka ovat linjassa OWASP MCP Top 10 -kehikon kanssa.

## 🏔️ Käytännön turvakoulutus

Käytännön ja konkreettisen turvakäyttöönoton kokemuksen saamiseksi suosittelemme **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - kattava opastettu matka MCP-palvelimien turvaamiseen Azure-ympäristössä käyttäen "haavoittuvainen → hyökkäys → korjaus → validointi" -menetelmää.

Kaikki tässä dokumentissa esitetyt turvavalvonnat ovat yhdenmukaisia **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** -oppaan kanssa, joka tarjoaa referenssiarkkitehtuurit ja Azure-spesifiset toteutusohjeet OWASP MCP Top 10 -riskeille.

## **PAKOLLISET turvavaatimukset**

### **Kriittiset kiellot MCP-määrittelystä:**

> **KIELLETTY:** MCP-palvelimet **EIVÄT SAA** hyväksyä minkäänlaisia tunnuksia, joita ei nimenomaisesti ole annettu kyseiselle MCP-palvelimelle
>
> **KIELLETTY:** MCP-palvelimet **EIVÄT SAA** käyttää sessioita todennukseen
>
> **VAATIMUS:** MCP-palvelimet, jotka toteuttavat valtuutuksen, **MUSTAVAT** tarkistaa KAIKKI saapuvat pyynnöt
>
> **PAKOLLINEN:** MCP-välityspalvelimet, jotka käyttävät staattista kolmannen osapuolen asiakastunnusta,
> **ON saatava** suostumus jokaiselta MCP-asiakkaalta ennen valtuutuksen välittämistä

---

## 1. **Todennus- ja valtuutusvalvonnat**

### **Ulkoinen tunnistuspalveluntarjoaja-integraatio**

**MCP-määrittely `2026-07-28`** sallii MCP-palvelinten delegoida
todennus ulkoisille tunnistuspalveluntarjoajille. HTTP:n valtuutus
transports arvioidaan pyynnön mukaan; paikalliset stdio-palvelimet saavat tunnistetietonsa
sen sijaan ympäristöstään.

**OWASP MCP -riski, johon paneudutaan**: [MCP07 - Riittämätön todennus ja valtuutus](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Turvallisuushyödyt:**
1. **Poistaa mukautetun todennuksen riskit**: Vähentää haavoittuvuuspintaa välttämällä mukautettuja todennusratkaisuja
2. **Yritystason turvallisuus**: Hyödyntää vakiintuneita identiteetin tarjoajia, kuten Microsoft Entra ID:tä, edistyneillä turvallisuusominaisuuksilla
3. **Keskitetty identiteetin hallinta**: Yksinkertaistaa käyttäjän elinkaaren hallintaa, käyttöoikeuksien valvontaa ja vaatimustenmukaisuuden auditoimista
4. **Monivaiheinen tunnistautuminen**: Perii MFA-ominaisuudet yrityksen identiteetin tarjoajilta
5. **Ehdolliset käyttöoikeuskäytännöt**: Hyötyy riskipohjaisista käyttövalvontamekanismeista ja adaptiivisesta todennuksesta

**Toteutusvaatimukset:**
- **Asiakasrekisteröinti**: Suosi Client ID Metadata -dokumentteja tai
  ennakkorekisteröintiä; käytä vanhentunutta Dynamic Client Registration -menetelmää vain
  yhteensopivuuden vuoksi
- **Tokenin vastaanottajavalidointi**: Varmista, että kaikki tokenit on nimenomaisesti myönnetty MCP-palvelimelle
- **Myöntäjän vahvistus**: Vahvista, että tokenin myöntäjä vastaa odotettua identiteetin tarjoajaa
- **Allekirjoituksen tarkistus**: Kryptografinen validointi tokenin eheydestä
- **Vanhenemisen valvonta**: Tiukka tokenin eliniän rajoitusten valvonta
- **Laajuuden validointi**: Varmista, että tokenit sisältävät asianmukaiset oikeudet pyydettyihin operaatioihin

### **Valtuutuslogiikan turvallisuus**

**Keskeiset valvontatoimet:**
- **Laajat valtuutusauditoinnit**: Säännölliset turvallisuustarkastukset kaikilla valtuutuspäätösten kohdilla
- **Varmuuskytketyydet oletusarvoina**: Estä pääsy, jos valtuutuslogiikka ei pysty tekemään lopullista päätöstä
- **Oikeusrajojen selkeys**: Selkeä jako eri valtuustasojen ja resurssien käytön välillä
- **Auditointilokit**: Kaikkien valtuutuspäätösten täydellinen kirjaaminen turvallisuuden seurantaa varten
- **Säännölliset käyttöoikeustarkastukset**: Käyttäjän oikeuksien ja oikeustasojen määräaikainen vahvistus

## 2. **Tokenien turvallisuus ja Anti-Passthrough -valvontamekanismit**

**OWASP MCP -riski, johon paneudutaan**: [MCP01 - Tokenien huono hallinta & salaisuuksien paljastuminen](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Tokenien suoran läpipääsyn estäminen**

**Tokenien suora läpipääsy (passthrough) on nimenomaisesti kielletty** MCP:n valtuutusmäärityksessä kriittisten turvallisuusriskien vuoksi:

**Ongelmat, joihin puututaan:**
- **Toimintavalvonnan kiertäminen**: Ohittaa oleelliset turvamekanismit, kuten nopeusrajoitukset, pyyntöjen validoinnin ja liikenteen seurannan
- **Vastuullisuuden katoaminen**: Estää asiakkaan tunnistamisen, turmellen auditointilokit ja tapaustutkimukset
- **Välityspalvelimen väärinkäyttö**: Mahdollistaa hyökkääjien käyttää palvelimia proxyina luvattomaan datoihin pääsyyn
- **Luottamusrakenteiden rikkominen**: Rikkoo jälkipalveluiden luottamusolettamia tokenin alkuperästä
- **Sivuttaissuuntaiset liikkeet**: Kompromettoidut tokenit useissa palveluissa laajentavat hyökkäysmahdollisuuksia

**Toteutuksen valvontakeinot:**
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

### **Turvalliset tokenien hallintamallit**

**Parhaat käytännöt:**
- **Lyhytikäiset tokenit**: Minimoi altistumisaika tiheällä tokenien kierrätyksellä
- **Tarvittaessa myöntäminen**: Myönnä tokenit vain silloin, kun niitä tarvitaan tiettyihin toimiin
- **Turvallinen säilytys**: Käytä laitteistoturvakomponentteja (HSM) tai turvallisia avainholveja
- **Tokenin sidonta**: Vahvista tokenin vastaanottaja ja myöntäjä tarkoitetulle MCP
  resurssille, asiakkaalle ja operaatiolle
- **Valvonta ja hälytykset**: Reaaliaikainen tokenien väärinkäytön tai luvattoman pääsyn havaitseminen

## 3. **Sovellustilan turvallisuusvalvontamekanismit**

### **Tilan hallintatunnisteen (state handle) kaappauksen esto**

**Hyökkäysvektorit, joihin puututaan:**
- **Tunnisteen arvauksen estäminen**: Ennustettavat tunnisteet paljastavat toisen käyttäjän tilan
- **Ristiin käytön estäminen**: Varastettua tunnistetta käytetään eri identiteetillä
- **Epäsuora valtuutus**: Tunnisteen hallussapitoa käsitellään virheellisesti pääsyn todistuksena




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

**Siirron turvallisuus:**
- **HTTPS:n pakottaminen**: Edellytä HTTPS etä-HTTP-siirroille
- **Todennustietojen käsittely**: Lähetä ja varmista valtuutus jokaisessa HTTP-pyynnössä
- **stdio-eristys**: Suojaa paikalliset stdio-palvelimet prosessieristyksen ja
  ympäristömuuttujien valtuutushallinnan avulla

### **Tilallinen vs tilaton näkökulma**

MCP `2026-07-28` on protokollakerroksella tilaton. Sovellukset voivat silti
ylläpitää tilaa palauttamalla eksplisiittisen kahvan yhdestä työkalukutsusta ja hyväksymällä
sen tavallisena argumenttina myöhemmissä kutsuissa.

- Säilytä tila itsenäisesti riippumatta yksittäisestä siirtoliitännästä.
- Sitota tila-kahvat todennettuun pääkäyttäjään palvelimen puolella.
- Käsittele kahvaa nimenä, ei haltijan valtuutena.
- Määrittele vanhentuneiden kahvojen vanhentumisen ja palautumisen käyttäytyminen.

## 4. **Tekoälyyn liittyvät turvakontrollit**

**OWASP MCP -riskit, joita käsitellään**:
- [MCP06 - Tarkoitusvirheen hyväksikäyttö](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Työkalumyrkytys](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Komentojen injektointi ja suoritus](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Kehoituksen injektoinnin torjunta**

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

**Toteutuksen kontrollit:**
- **Syötteen puhdistus**: Kaikkien käyttäjätulosten kattava validointi ja suodatus
- **Sisällön rajojen määrittely**: Selkeä ero järjestelmäohjeiden ja käyttäjän sisällön välillä
- **Ohjehierarkia**: Oikeat etuoikeussäännöt ristiriitaisille ohjeille
- **Tulosteseuranta**: Haitallisten tai manipuloitujen tulosteiden havaitseminen

### **Työkalumyrkytyksen estäminen**

**Työkaluturvakehys:**
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
- **Hyväksyntätyönkulut**: Selkeä käyttäjän suostumus työkalumuutoksiin
- **Palautusmahdollisuudet**: Mahdollisuus palauttaa edelliseen työkaluversion
- **Muutosvalvonta**: Kattava historia työkalumääritelmien muutoksista
- **Riskinarviointi**: Automatisoitu arvio työkalun turvatasosta

## 5. **Confused Deputy -hyökkäyksen estäminen**

### **OAuth-välityspalvelimen turvallisuus**

**Hyökkäyksen estokontrollit:**
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

**Toteutusvaatimukset:**
- **Asiakasrekisteröinti**: Suosi ennakko-rekisteröintiä tai Client ID -metadata
  -tiedostoja; käsittele dynaamista asiakasrekisteröintiä yhteensopivuuden varmistamiseksi
- **Käyttäjän suostumuksen varmennus**: MCP-välityspalvelimien, jotka käyttävät staattista kolmannen osapuolen asiakastunnusta,
  on saatava asiakkaan suostumus ennen valtuutuksen välittämistä
- **Uudelleenohjauksen URI:n validointi**: Tiukasti valkoinen-listapohjainen validointi uudelleenohjauskohteille
- **Valtuutuskoodin suojaus**: Lyhytikäiset koodit, jotka ovat kertakäyttöisiä
- **Asiakkaan tunnistuksen varmennus**: Vahva validoitu tunnistus asiakastunnisteille ja metadatalle

## 6. **Työkalun suoritusvarmuus**

### **Säilötys ja eristäminen**

**Konttipohjainen eristys:**
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

**Prosessien eristys:**
- **Eri prosessikontekstit**: Jokainen työkalun suoritus eristetyssä prosessitilassa
- **Prosessien välinen viestintä**: Turvalliset IPC-mekanismit validoinnilla
- **Prosessien valvonta**: Suoritusaikainen käyttäytymisanalyysi ja poikkeavuuksien havaitseminen
- **Resurssien valvonta**: Tiukat rajat CPU:n, muistin ja I/O-toimintojen käytölle

### **Vähimmän edun periaatteen toteutus**

**Oikeushallinta:**
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

## 7. **Toimitusketjun turvallisuusvalvonta**

**OWASP MCP -riski kohdattu**: [MCP04 - Ohjelmistotoimitusketjun hyökkäykset ja riippuvuuksien manipulointi](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Riippuvuuksien varmennus**

**Kattava komponenttien turvallisuus:**
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

### **Jatkuva valvonta**

**Toimitusketjun uhkien havaitseminen:**
- **Riippuvuuksien terveyden seuranta**: Kaikkien riippuvuuksien jatkuva arviointi turvallisuusongelmien varalta
- **Uhkatiedon integrointi**: Reaaliaikaiset päivitykset nousevista toimitusketjun uhista
- **Käyttäytymisanalyysi**: Epätavallisen käyttäytymisen tunnistus ulkoisissa komponenteissa
- **Automaattinen reagointi**: Välitön kompromettoituneiden komponenttien eristäminen

## 8. **Valvonta- ja havaitsemisvalvonnat**

**OWASP MCP -riski kohdattu**: [MCP08 - Auditoinnin ja telemetrian puute](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Turvallisuustiedon ja tapahtumien hallinta (SIEM)**

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
- **Käyttäjän käyttäytymisen analyysi (UBA)**: Epätavallisten käyttäjän käyttökuvioiden tunnistus
- **Entiteetin käyttäytymisen analyysi (EBA)**: MCP-palvelimen ja työkalujen käyttäytymisen seuranta
- **Koneoppimisen poikkeavuuksien havaitseminen**: AI-avusteinen turvallisuusuhkien tunnistus
- **Uhkatiedon korrelaatio**: Havainnoitujen toimintojen vertaaminen tunnettuun hyökkäysmalliin

## 9. **Häiriötilanteisiin reagointi ja palautuminen**

### **Automaattisen reagoinnin valmiudet**

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

**Tutkimuksen tuki:**
- **Auditointilokin säilytys**: Muuttumaton lokitus kryptografisella eheyden varmistuksella
- **Todisteiden keruu**: Automaattinen olennaisten turvallisuusartefaktien kokoaminen
- **Aikajanan rekonstruointi**: Yksityiskohtainen tapahtumasarja, joka johtaa turvallisuuspoikkeamiin
- **Vaikutuksen arviointi**: Arvio kompromissin laajuudesta ja tietovuodoista

## **Keskeiset turvallisuusarkkitehtuurin periaatteet**

### **Syvyyspuolustus**
- **Useita turvallisuuskerroksia**: Ei yksittäisiä yksittäispisteen vikoja turvallisuusarkkitehtuurissa
- **Redundantit valvontatoimet**: Päällekkäiset turvatoimet kriittisiin toimintoihin
- **Vikasietomekanismit**: Turvalliset oletusasetukset virhetilanteissa tai hyökkäystilanteissa

### **Nollaluottamusperiaatteen toteutus**
- **Älä koskaan luota, tarkista aina**: Jatkuva kaikkien toimijoiden ja pyyntöjen validointi
- **Vähimmän etuoikeuden periaate**: Kaikille komponenteille minimaalinen käyttöoikeus
- **Mikrosegmentointi**: Tarkat verkko- ja pääsynvalvontamekanismit

### **Jatkuva turvallisuuden kehitys**
- **Uhka-alueen mukautuminen**: Säännölliset päivitykset nousevien uhkien hallitsemiseksi
- **Turvallisuusvalvonnan tehokkuus**: Valvontatoimien jatkuva arviointi ja parantaminen
- **Määritysten noudattaminen**: Yhdenmukaisuus kehittyvien MCP-turvastandardien kanssa

---

## **Toteutusresurssit**

### **Viralliset MCP-dokumentit**
- [MCP-määritys (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP-turvallisuuden parhaat käytännöt](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP-valtuutusmäärittely](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP -turvallisuusresurssit**
- [OWASP MCP Azure -turvaopas](https://microsoft.github.io/mcp-azure-security-guide/) - Kattava OWASP MCP Top 10 Azure-toteutuksineen
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Viralliset OWASP MCP -turvauhat
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Käytännön turvallisuuskoulutus MCP:lle Azurella

### **Microsoftin turvallisuusratkaisut**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Turvastandardit**
- [OAuth 2.0 turvallisuuden parhaat käytännöt (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 suurten kielimallien turvallisuudessa](https://genai.owasp.org/)
- [NISTin kyberturvallisuuskehys](https://www.nist.gov/cyberframework)

---

> **Tärkeää:** Nämä turvatoimet heijastavat MCP-määritystä
> `2026-07-28`. Tarkista aina
> [ajantasainen virallinen dokumentaatio](https://modelcontextprotocol.io/specification/2026-07-28/)
> kun standardit kehittyvät.

## Mitä seuraavaksi

- Palaa kohtaan: [Turvallisuusmoduulin yleiskatsaus](./README.md)
- Jatka kohtaan: [Moduuli 3: Aloittaminen](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->