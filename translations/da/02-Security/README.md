# MCP-sikkerhed: Omfattende beskyttelse af AI-systemer

[![MCP Security Best Practices](../../../translated_images/da/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klik på billedet ovenfor for at se videoen af denne lektion)_

Sikkerhed er grundlæggende i designet af AI-systemer, og derfor prioriterer vi det som vores anden sektion. Dette er i overensstemmelse med Microsofts **Secure by Design**-princip fra [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) bringer kraftfulde nye muligheder til AI-drevne applikationer, samtidig med at det introducerer unikke sikkerhedsudfordringer, der rækker ud over traditionelle software-risici. MCP-systemer står over for både etablerede sikkerhedsbekymringer (sikker kodning, mindst privilegium, forsyningskædesikkerhed) og nye AI-specifikke trusler inklusive prompt-injektion, tool-forgiftning, sessionkapring, confused deputy-angreb, token-gennemgangssårbarheder og dynamisk kapacitetsmodifikation.

Denne lektion undersøger de mest kritiske sikkerhedsrisici i MCP-implementeringer—dækkende autentifikation, autorisation, overdrevne tilladelser, indirekte prompt-injektion, sessionsikkerhed, confused deputy-problemer, tokenstyring og forsyningskæde-sårbarheder. Du lærer handlingsrettede kontrolforanstaltninger og bedste praksisser til at afbøde disse risici, samtidig med at du udnytter Microsoft-løsninger som Prompt Shields, Azure Content Safety og GitHub Advanced Security til at styrke din MCP-udrulning.

## Læringsmål

Ved slutningen af denne lektion vil du kunne:

- **Identificere MCP-specifikke trusler**: Genkende unikke sikkerhedsrisici i MCP-systemer inklusive prompt-injektion, tool-forgiftning, overdrevne tilladelser, sessionkapring, confused deputy-problemer, token-gennemgangssårbarheder og forsyningskæderisici
- **Anvende sikkerhedskontroller**: Implementere effektive afbødningsmetoder herunder robust autentifikation, mindst privilegeret adgang, sikker tokenstyring, sessionssikkerhedskontroller og verifikation af forsyningskæde
- **Udnytte Microsofts sikkerhedsløsninger**: Forstå og implementere Microsoft Prompt Shields, Azure Content Safety og GitHub Advanced Security til beskyttelse af MCP-arbejdsbelastninger
- **Validere tool-sikkerhed**: Forstå vigtigheden af validering af tool-metadata, overvågning af dynamiske ændringer og forsvar mod indirekte prompt-injektionsangreb
- **Integrere bedste praksisser**: Kombinere etablerede sikkerhedsgrundlag (sikker kodning, serverhærde, zero trust) med MCP-specifikke kontroller for omfattende beskyttelse

# MCP-sikkerhedsarkitektur og kontroller

Moderne MCP-implementeringer kræver lagdelte sikkerhedstilgange, der adresserer både traditionel softwaresikkerhed og AI-specifikke trusler. Den hurtigt udviklende MCP-specifikation fortsætter med at modne sine sikkerhedskontroller, hvilket muliggør bedre integration med virksomheders sikkerhedsarkitekturer og etablerede bedste praksisser.

Forskning fra [Microsoft Digital Defense Report](https://aka.ms/mddr) viser, at **98 % af rapporterede overtrædelser ville blive forhindret ved robust sikkerhedshygiejne**. Den mest effektive beskyttelsesstrategi kombinerer grundlæggende sikkerhedspraksisser med MCP-specifikke kontroller—dokumenterede baselinesikkerhedsforanstaltninger forbliver de mest indflydelsesrige til at reducere den samlede sikkerhedsrisiko.

## Aktuelt sikkerhedsmiljø

> **Bemærk:** Dette kapitel kombinerer etablerede MCP-sikkerhedskontroller med den
> nuværende **MCP Specification 2026-07-28**-autoriseringsvejledning. Henvis altid
> til den aktuelle [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub-repositorium](https://github.com/modelcontextprotocol) og
> [sikkerhedsbedste praksisdokumentationen](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> ved implementering af sikkerhedsfølsom kode.

> **Autorisationsopdatering:** MCP `2026-07-28` kræver, at klienter validerer
> `iss`-parameteren i autorisationssvar (RFC 9207) og binder registrerede
> legitimationsoplysninger til den udstedende autorisationsserver. Dynamisk klientregistrering
> er forældet; nye implementeringer bør anvende Client ID Metadata Documents.
> Se [Hvad er ændret i MCP: Specifikation 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> for den komplette liste over autorisationsændringer.

## 🏔️ MCP Security Summit Workshop (Sherpa)

For **praktisk sikkerhedstræning** anbefaler vi stærkt **MCP Security Summit Workshop** (Sherpa) - en omfattende guidet ekspedition til sikring af MCP-servere i Microsoft Azure.

### Workshop Oversigt

[MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) giver praktisk, handlingsrettet sikkerhedstræning gennem en dokumenteret "sårbar → udnyttelse → løsning → validering" metode. Du vil:

- **Lære ved at bryde ting**: Oplev sårbarheder direkte ved at udnytte bevidst usikre servere
- **Bruge Azure-native sikkerhed**: Udnyt Azure Entra ID, Key Vault, API Management og AI Content Safety
- **Følge forsvar i dybden**: Gå igennem lejr, der opbygger omfattende sikkerhedslag
- **Anvende OWASP-standarder**: Hver teknik svarer til [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Få produktionsklar kode**: Afslut med fungerende, testede implementeringer

### Ekspeditionsruten

| Lejr | Fokus | OWASP-risici dækket |
|------|-------|---------------------|
| **Base Camp** | MCP-grundlæggende & autentifikationssårbarheder | MCP01, MCP07 |
| **Lejr 1: Identitet** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Lejr 2: Gateway** | API Management, Private Endpoints, styring | MCP02, MCP06, MCP07, MCP09 |
| **Lejr 3: I/O Sikkerhed** | Prompt-injektion, PII-beskyttelse, indholdssikkerhed | MCP03, MCP05, MCP06, MCP10 |
| **Lejr 4: Overvågning** | Log Analytics, dashboards, trusselsdetektion | MCP04, MCP08 |
| **Toppen** | Red Team / Blue Team integrations-test | Alle |

**Kom i gang**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 sikkerhedsrisici

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) beskriver de ti mest kritiske sikkerhedsrisici for MCP-implementeringer:

| Risiko | Beskrivelse | Azure Afbødning |
|------|-------------|------------------|
| **MCP01** | Forkert håndtering af tokens & eksponering af hemmeligheder | Azure Key Vault, Managed Identity |
| **MCP02** | Privilegie-eskalering via scope creep | RBAC, betinget adgang |
| **MCP03** | Tool-forgiftning | Tool-validering, integritetsverifikation |
| **MCP04** | Softwareforsyningskædeangreb & afhængighedsmanipulation | GitHub Advanced Security, afhængighedsscanning |
| **MCP05** | Kommando-injektion & eksekvering | Inputvalidering, sandboxing |
| **MCP06** | Underminering af intention flow | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Utilstrækkelig autentifikation & autorisation | Azure Entra ID, OAuth 2.1 med PKCE |
| **MCP08** | Manglende revision og telemetri | Azure Monitor, Application Insights |
| **MCP09** | Skygge-MCP-servere | API Center-styring, netværksisolation |
| **MCP10** | Kontekst-injektion & overdeling | Dataklassificering, minimal eksponering |

### Udvikling af MCP autentifikation

MCP-specifikationen har udviklet sig betydeligt i sin tilgang til autentifikation og autorisation:

- **Oprindelig tilgang**: Tidlige specifikationer krævede, at udviklere implementerede særskilte autentifikationsservere, hvor MCP-servere fungerede som OAuth 2.0 autorisationsservere, der styrede brugerautentifikation direkte
- **Nuværende standard (`2026-07-28`)**: MCP-servere kan delegere autentifikation
  til eksterne identitetsudbydere som Microsoft Entra ID. Klienter skal også
  anvende gældende krav til udsteder-validering og legitimation-binding.
- **Sikkerhed for transportlag**: Forbedret understøttelse af sikre transportmekanismer med passende autentifikationsmønstre for både lokale (STDIO) og fjernforbindelser (Streamable HTTP)

## Autentifikation & autorisationssikkerhed

### Nuværende sikkerhedsudfordringer

Moderne MCP-implementeringer står over for flere udfordringer inden for autentifikation og autorisation:

### Risici & trusselvektorer

- **Forkert konfigureret autorisationslogik**: Fejlbehæftet autorisationsimplementering i MCP-servere kan eksponere følsomme data og forkert anvende adgangskontroller
- **OAuth-token kompromittering**: Lokalt MCP-server token-tyveri tillader angribere at udgive sig for servere og få adgang til nedstrøms tjenester
- **Token-gennemgangssårbarheder**: Forkert token-håndtering skaber omgåelser af sikkerhedskontroller og ansvarlighedshuller
- **Overdrevne tilladelser**: MCP-servere med for mange privilegier overtræder princippet om mindst privilegium og udvider angrebsoverflader

#### Token-gennemgang: Et kritisk anti-mønster

**Token-gennemgang er udtrykkeligt forbudt** i den aktuelle MCP-autoritetspecifikation på grund af alvorlige sikkerhedsmæssige konsekvenser:

##### Omgåelse af sikkerhedskontrol
- MCP-servere og nedstrøms API'er implementerer kritiske sikkerhedskontroller (ratebegrænsning, anmodningsvalidering, trafikmonitorering), som afhænger af korrekt tokenvalidering
- Direkte klient-til-API-token brug omgår disse væsentlige beskyttelser og underminerer sikkerhedsarkitekturen

##### Ansvarlighed og revisionsudfordringer  
- MCP-servere kan ikke skelne mellem klienter, der bruger opstrøms udstedte tokens, hvilket bryder revisionsspor
- Logfiler på nedstrøms ressource-servere viser vildledende anmodningskilder i stedet for faktiske MCP-server mellemmænd
- Incidentundersøgelse og regelefterlevelsesrevisioner bliver betydeligt vanskeligere

##### Risiko for dataudslip
- Uvaliderede token-påstande gør det muligt for ondsindede aktører med stjålne tokens at bruge MCP-servere som proxier til dataudslip
- Tillidsgrænseovertrædelser tillader uautoriserede adgangsmønstre, der omgår tilsigtede sikkerhedskontroller

##### Angrebsvektorer på tværs af flere tjenester
- Kompromitterede tokens accepteret af flere tjenester muliggør lateral bevægelse på tværs af tilknyttede systemer
- Tillidsantagelser mellem tjenester kan blive brudt, når token-oprindelser ikke kan verificeres

### Sikkerhedskontroller & afbødninger

**Kritiske sikkerhedskrav:**

> **OBLIGATORISK**: MCP-servere **MÅ IKKE** acceptere tokens, der ikke eksplicit er udstedt til MCP-serveren

#### Autentifikations- og autorisationskontroller

- **Grundig autorisationsgennemgang**: Udfør omfattende revisioner af MCP-serveres autorisationslogik for at sikre, at kun tilsigtede brugere og klienter kan få adgang til følsomme ressourcer
  - **Implementeringsvejledning**: [Azure API Management som autentifikationsgateway for MCP-servere](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitetsintegration**: [Brug af Microsoft Entra ID til MCP-serverautentifikation](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Sikker tokenstyring**: Implementer [Microsofts bedste praksis for tokenvalidering og livscyklus](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validér, at tokenets audience-påstand matcher MCP-serveridentitet
  - Implementer passende tokenrotation og udløbspolitikker
  - Forhindre token replay-angreb og uautoriseret brug

- **Sikret tokenlagring**: Sørg for krypteret tokenlagring både i hvilende tilstand og under overførsel
  - **Bedste praksis**: [Retningslinjer for sikker tokenlagring og kryptering](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementering af adgangskontrol

- **Princippet om mindst privilegium**: Tildel MCP-servere kun de mindste nødvendige tilladelser til tilsigtet funktionalitet
  - Regelmæssige gennemgange og opdateringer af tilladelser for at forhindre privilegieudvidelse
  - **Microsoft-dokumentation**: [Sikker mindst-privilegeret adgang](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollestyring (RBAC)**: Implementer finmasket rollefordeling
  - Afgræns roller snævert til specifikke ressourcer og handlinger
  - Undgå brede eller unødvendige tilladelser, der udvider angrebsoverfladen

- **Kontinuerlig permission-overvågning**: Implementer løbende adgangsrevision og overvågning
  - Overvåg mønstre for brug af tilladelser efter unormaliteter
  - Afhjælp hurtigst muligt overdrevne eller ubrugte privilegier

## AI-specifikke sikkerhedstrusler

### Prompt-injektion & manipulation af tools-angreb

Moderne MCP-implementeringer står over for sofistikerede AI-specifikke angrebsvektorer, som traditionelle sikkerhedstiltag ikke fuldt ud kan adressere:

#### **Indirekte prompt-injektion (Cross-Domain Prompt Injection)**

**Indirekte prompt-injektion** udgør en af de mest kritiske sårbarheder i MCP-aktiverede AI-systemer. Angribere indlejrer ondsindede instruktioner i eksternt indhold—dokumenter, websider, emails eller datakilder—som AI-systemerne efterfølgende behandler som legitime kommandoer.

**Angrebsscenarier:**
- **Dokumentbaseret injektion**: Ondsindede instruktioner skjult i behandlede dokumenter, der udløser utilsigtede AI-handlinger
- **Udnyttelse af webindhold**: Kompromitterede websider indeholdende indlejrede prompts, der manipulerer AI-adfærd ved scraping
- **Email-baserede angreb**: Ondsindede prompts i emails, som får AI-assistenter til at lække informationer eller udføre uautoriserede handlinger
- **Forurening af datakilde**: Kompromitterede databaser eller API'er, der leverer forgiftet indhold til AI-systemer

**Reel world-impact**: Disse angreb kan resultere i dataudslip, privatlivsbrud, generering af skadeligt indhold og manipulation af brugerinteraktioner. For detaljeret analyse se [Prompt Injection i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/da/prompt-injection.ed9fbfde297ca877.webp)

#### **Tool-forgiftning-angreb**

**Tool-forgiftning** retter sig mod metadata, der definerer MCP-tools, ved at udnytte hvordan LLM'er fortolker tool-beskrivelser og parametre til at træffe eksekveringsbeslutninger.

**Angrebsmekanismer:**
- **Manipulation af metadata**: Angribere injicerer ondsindede instruktioner i tool-beskrivelser, parameterdefinitioner eller brugseksempler
- **Usynlige instruktioner**: Skjulte prompts i tool-metadata, som behandles af AI-modeller men er usynlige for menneskelige brugere
- **Dynamisk tool-modifikation ("Rug Pulls")**: Tools godkendt af brugere ændres senere til at udføre ondsindede handlinger uden brugerens viden
- **Parameter-injektion**: Ondsindet indhold indlejret i tool-parametriske skemaer, som påvirker modellens adfærd


**Risici ved Hosted Servere**: Fjernservere for MCP udgør forhøjede risici, da tool-definitioner kan opdateres efter brugerens oprindelige godkendelse, hvilket skaber scenarier, hvor tidligere sikre værktøjer bliver ondsindede. For en omfattende analyse, se [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/da/tool-injection.3b0b4a6b24de6bef.webp)

#### **Yderligere AI Angrebsvinkler**

- **Cross-Domain Prompt Injection (XPIA)**: Sofistikerede angreb, der udnytter indhold fra flere domæner for at omgå sikkerhedskontroller
- **Dynamisk Kapabilitetsændring**: Ændringer i realtid af tool kapabiliteter, som slipper uden om initiale sikkerhedsvurderinger
- **Context Window Poisoning**: Angreb, der manipulerer store kontekstvinduer for at skjule ondsindede instruktioner
- **Model Confusion Angreb**: Udnyttelse af modellimitations for at skabe uforudsigelig eller usikker adfærd


### AI Sikkerhedsrisiko Konsekvenser

**Højt Impact Konsekvenser:**
- **Dataudtrækning**: Uautoriseret adgang til og tyveri af følsomme virksomheds- eller personlige data
- **Privatlivsbrud**: Eksponering af personligt identificerbare oplysninger (PII) og fortrolige forretningsdata
- **Systemmanipulation**: Utilsigtede ændringer i kritiske systemer og arbejdsgange
- **Tyveri af legitimationsoplysninger**: Kompromittering af autentifikationstokens og servicelegitimationsoplysninger
- **Lateral Bevægelse**: Brug af kompromitterede AI-systemer som pivotpunkter for bredere netværksangreb

### Microsoft AI Sikkerhedsløsninger

#### **AI Prompt Shields: Avanceret Beskyttelse mod Injection Angreb**

Microsoft **AI Prompt Shields** leverer omfattende forsvar mod både direkte og indirekte prompt injection-angreb gennem flere sikkerhedslag:

##### **Kernebeskyttelsesmekanismer:**

1. **Avanceret Detektion & Filtrering**
   - Maskinlæringsalgoritmer og NLP-teknikker registrerer ondsindede instruktioner i eksternt indhold
   - Realtidsanalyse af dokumenter, websider, e-mails og datakilder for indlejrede trusler
   - Kontekstuel forståelse af legitime vs. ondsindede promptmønstre

2. **Spotlighting Metoder**  
   - Skelner mellem betroede systeminstruktioner og potentielt kompromitterede eksterne input
   - Teksttransformationsmetoder, der forbedrer modellens relevans samtidig med isolering af ondsindet indhold
   - Hjælper AI-systemer med at opretholde korrekt instruktionshierarki og ignorere injicerede kommandoer

3. **Delimiter & Datamarking Systemer**
   - Eksplicit grænse-definition mellem betroede systembeskeder og ekstern inputtekst
   - Specielle markører fremhæver grænser mellem betroede og utroværdige datakilder
   - Klar adskillelse forhindrer instruktionsforvirring og uautoriseret kommandoeksekvering

4. **Kontinuerlig Trusselintelligens**
   - Microsoft overvåger løbende nye angrebsmønstre og opdaterer forsvar
   - Proaktiv trusselsjagt efter nye injection-teknikker og angrebsvinkler
   - Regelmæssige opdateringer af sikkerhedsmodeller for at opretholde effektivitet mod udviklende trusler

5. **Azure Content Safety Integration**
   - En del af det omfattende Azure AI Content Safety suite
   - Yderligere detektion af jailbreak-forsøg, skadeligt indhold og overtrædelser af sikkerhedspolitikker
   - Forenede sikkerhedskontroller på tværs af AI applikationskomponenter

**Implementeringsressourcer**: [Microsoft Prompt Shields Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/da/prompt-shield.ff5b95be76e9c78c.webp)


## Avancerede MCP Sikkerhedstrusler

### Session Hijacking Sårbarheder

**Session hijacking** repræsenterer en kritisk angrebsvinkel i stateful MCP-implementeringer, hvor uautoriserede parter får og misbruger legitime sessions-id'er for at efterligne klienter og udføre uautoriserede handlinger.

#### **Angrebsscenarier & Risici**

- **Session Hijack Prompt Injection**: Angribere med stjålne sessions-id'er injicerer ondsindede hændelser i servere, der deler sessionstilstand, hvilket potentielt udløser skadelige handlinger eller adgang til følsomme data
- **Direkte Efterligning**: Stjålne sessions-id'er muliggør direkte MCP serveropkald, der omgår autentifikation, og behandler angribere som legitime brugere
- **Kompromitterede Genoptagelige Strømme**: Angribere kan afbryde forespørgsler for tidligt, hvilket får legitime klienter til at genoptage med potentielt ondsindet indhold

#### **Sikkerhedskontroller for Session Management**

**Kritiske krav:**
- **Autorisation Bekræftelse**: MCP-servere, der implementerer autorisation, **SKAL** verificere ALLE indgående forespørgsler og **MÅ IKKE** stole på sessions for autentifikation
- **Sikker Session Generering**: Brug kryptografisk sikre, ikke-deterministiske sessions-id'er, der genereres med sikre tilfældige talgeneratorer
- **Brugerspecifik Binding**: Bind sessions-id'er til brugerspecifik information ved brug af formater som `<user_id>:<session_id>` for at forhindre sessionmisbrug på tværs af brugere
- **Session Livscyklus Management**: Implementer korrekt udløb, rotation og ugyldiggørelse for at begrænse sårbarhedsvinduer
- **Transport Sikkerhed**: Obligatorisk HTTPS for al kommunikation for at forhindre opsnuseri af sessions-id'er

### Confused Deputy Problem

Den **forvirrede stedfortræder-problem** opstår, når MCP-servere agerer som autentifikationsproxyer mellem klienter og tredjepartstjenester, hvilket skaber muligheder for autorisationsomgåelse gennem udnyttelse af statiske klient-id'er.

#### **Angribsmetoder & Risici**

- **Cookie-baseret Samtykke Omgåelse**: Tidligere brugergodkendelse skaber samtykkecookies som angribere udnytter via ondsindede autorisationsanmodninger med manipulerede redirect-URI'er
- **Tyveri af Autorisationskode**: Eksisterende samtykkecookies kan få autorisationsservere til at springe samtykkeskærme over og dirigere koder til angriberstyrede endepunkter
- **Uautoriseret API Adgang**: Stjålne autorisationskoder muliggør token-udveksling og brugerefterligning uden eksplicit godkendelse

#### **Afværgestrategier**

**Obligatoriske kontroller:**
- **Eksplicitte Samtykkekrav**: MCP proxy-servere med statiske klient-id'er **SKAL** opnå brugersamtykke for hver dynamisk registreret klient
- **OAuth 2.1 Sikkerhedsimplementering**: Følg aktuelle OAuth bedste praksis, herunder PKCE (Proof Key for Code Exchange) for alle autorisationsanmodninger
- **Streng Klientvalidering**: Implementer streng validering af redirect-URI'er og klientidentifikatorer for at forhindre misbrug

### Token Passthrough Sårbarheder  

**Token passthrough** repræsenterer et eksplicit anti-mønster, hvor MCP-servere accepterer klienttokens uden korrekt validering og videresender dem til downstream-API'er, hvilket overtræder MCP autorisationsspecifikationer.

#### **Sikkerhedsmæssige konsekvenser**

- **Kontrolomgåelse**: Direkte klient-til-API token-brug omgår vigtige rate-begrænsninger, valideringer og overvågningskontroller
- **Forringelse af revisionsspor**: Upstream-udstedte tokens gør klientidentifikation umulig og bryder hændelsesundersøgelsesmuligheder
- **Proxy-baseret dataudtræk**: Uvaliderede tokens giver ondsindede aktører mulighed for at bruge servere som proxyer for uautoriseret dataadgang
- **Overtrædelser af tillidsgrænser**: Downstream-tjenesters tillidsantagelser kan brydes, når tokenoprindelse ikke kan verificeres
- **Udvidelse af multi-service angreb**: Kompromitterede tokens accepteret på tværs af flere tjenester muliggør lateral bevægelse

#### **Påkrævede sikkerhedskontroller**

**Ufravigelige krav:**
- **Tokenvalidering**: MCP-servere **MÅ IKKE** acceptere tokens, der ikke eksplicit er udstedt til MCP-serveren
- **Audience-verifikation**: Altid validér at tokenaudience matcher MCP-serverens identitet
- **Korrekt token livscyklus**: Implementer kortlivede adgangstokens med sikre rotationsprocedurer


## Supply Chain Sikkerhed for AI Systemer

Supply chain-sikkerhed har udviklet sig ud over traditionelle softwareafhængigheder til at omfatte hele AI-økosystemet. Moderne MCP-implementeringer skal omhyggeligt verificere og overvåge alle AI-relaterede komponenter, da hver enkelt introducerer potentielle sårbarheder, som kan kompromittere systemintegriteten.

### Udvidede AI Supply Chain Komponenter

**Traditionelle softwareafhængigheder:**
- Open source biblioteker og frameworks
- Containerbilleder og basesystemer  
- Udviklingsværktøjer og byggepipeliner
- Infrastrukturkomponenter og -services

**AI-specifikke supply chain elementer:**
- **Foundation Models**: Fortrænede modeller fra forskellige leverandører, der kræver proveniensverifikation
- **Embedding Services**: Eksterne vektorisering og semantiske søgetjenester
- **Context Providers**: Datakilder, vidensbaser og dokumentsamlinger  
- **Tredjeparts API'er**: Eksterne AI-tjenester, ML pipelines og databehandlingsendepunkter
- **Modelartifakter**: Vægte, konfigurationer og finjusterede modelvarianter
- **Træningsdatasæt**: Datasæt brugt til modeltræning og finjustering

### Omfattende Supply Chain Sikkerhedsstrategi

#### **Komponentverifikation & Tillid**
- **Proveniensvalidering**: Verificér oprindelse, licensering og integritet af alle AI-komponenter før integration
- **Sikkerhedsvurdering**: Udfør sårbarhedsscanninger og sikkerhedsgennemgange af modeller, datakilder og AI-tjenester
- **Omdømmeanalyse**: Evaluer leverandørers sikkerhedshistorik og praksis
- **Overholdelsesverifikation**: Sikr at alle komponenter opfylder organisatoriske sikkerheds- og lovgivningskrav

#### **Sikre Deploy Pipelines**  
- **Automatiseret CI/CD Sikkerhed**: Integrér sikkerhedsscanning gennem automatiserede deploy-pipelines
- **Artifaktintegritet**: Implementer kryptografisk verifikation af alle deployerede artefakter (kode, modeller, konfigurationer)
- **Faset deployment**: Brug progressive deploymentsstrategier med sikkerhedsvalidering på hvert trin
- **Betroede Artefakt Repositorier**: Deploy kun fra verificerede, sikre artefaktregistre og repositorier

#### **Kontinuerlig Overvågning & Respons**
- **Afhængighedsscanning**: Løbende sårbarhedsovervågning af alle software- og AI-komponentafhængigheder
- **Modelovervågning**: Kontinuerlig vurdering af modeladfærd, performance-drift og sikkerhedsafvigelser
- **Service Sundhedsovervågning**: Overvåg eksterne AI-tjenester for tilgængelighed, sikkerhedshændelser og politikændringer
- **Trusselintelligensintegration**: Inkorporer trusselsfeeds specifikke for AI og ML sikkerhedsrisici

#### **Adgangskontrol & Mindst Privilegium**
- **Komponentniveau tilladelser**: Begræns adgang til modeller, data og services baseret på forretningsbehov
- **Servicekontoadministration**: Implementer dedikerede servicekonti med minimale nødvendige tilladelser
- **Netværkssegmentering**: Isolér AI-komponenter og begræns netværksadgang mellem services
- **API Gateway Kontroller**: Brug centraliserede API gateways til at kontrollere og overvåge adgang til eksterne AI-tjenester

#### **Hændelsesrespons & Genopretning**
- **Hurtige Responsprocedurer**: Etablerede processer for patching eller udskiftning af kompromitterede AI-komponenter
- **Roterning af Legitimationer**: Automatiserede systemer til at rotere hemmeligheder, API-nøgler og servicelegitimationsoplysninger
- **Rollback Capability**: Mulighed for hurtigt at vende tilbage til tidligere kendte gode versioner af AI-komponenter
- **Supply Chain Brud Genopretning**: Specifikke procedurer for reaktion på kompromittering af opstrøms AI-tjenester

### Microsoft Sikkerhedsværktøjer & Integration

**GitHub Advanced Security** tilbyder omfattende supply chain beskyttelse inklusive:
- **Secret Scanning**: Automatiseret detektion af legitimationer, API-nøgler og tokens i repositorier
- **Afhængighedsscanning**: Sårbarhedsvurdering af open source afhængigheder og biblioteker
- **CodeQL Analyse**: Statisk kodeanalyse for sikkerhedssårbarheder og kodningsproblemer
- **Supply Chain Indsigter**: Synlighed i afhængighedsstatus og sikkerhedssituation

**Azure DevOps & Azure Repos Integration:**
- Sømløs sikkerhedsscanning på tværs af Microsoft udviklingsplatforme
- Automatiserede sikkerhedstjek i Azure Pipelines for AI arbejdsbelastninger
- Politikegennemførelse for sikker AI-komponentdeployering

**Microsoft Interne Praksisser:**
Microsoft implementerer omfattende supply chain sikkerhedspraksisser på tværs af alle produkter. Lær om velafprøvede tilgange i [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Foundation Security Bedste Praksis

MCP-implementeringer arver og bygger videre på organisationens eksisterende sikkerhedsposition. Styrkelse af grundlæggende sikkerhedspraksis forbedrer betydeligt den samlede sikkerhed i AI-systemer og MCP-implementeringer.

### Kerne Sikkerhedsprincipper

#### **Sikre Udviklingspraksisser**
- **OWASP Overholdelse**: Beskyt mod [OWASP Top 10](https://owasp.org/www-project-top-ten/) webapplikationssårbarheder
- **AI-specifikke Beskyttelser**: Implementer kontroller for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Sikker Secrets Management**: Brug dedikerede vaults til tokens, API-nøgler og følsomme konfigurationsdata
- **End-to-End Kryptering**: Implementer sikre kommunikationsveje mellem alle applikationskomponenter og dataflows
- **Inputvalidering**: Grundig validering af alle brugerinput, API-parametre og datakilder

#### **Infrastrukturforstærkning**
- **Multi-Faktor Autentifikation**: Obligatorisk MFA for alle administrative og servicekonti
- **Patch Management**: Automatiseret, rettidig patchning af operativsystemer, frameworks og afhængigheder  
- **Identity Provider Integration**: Centraliseret identitetsstyring gennem virksomhedens identitetsudbydere (Microsoft Entra ID, Active Directory)
- **Netværkssegmentering**: Logisk isolering af MCP-komponenter for at begrænse lateral bevægelsespotentiale
- **Mindste Privilegium Princip**: Minimale nødvendige tilladelser for alle systemkomponenter og konti

#### **Sikkerhedsovervågning & Detektion**
- **Omfattende Logging**: Detaljeret logging af AI-applikationsaktiviteter, inklusive MCP klient-server-interaktioner
- **SIEM Integration**: Centraliseret sikkerhedsinformations- og hændelsesstyring til anomali-detektion
- **Adfærdsanalyse**: AI-drevet overvågning til at opdage usædvanlige mønstre i system- og brugeradfærd
- **Trusselsintelligens**: Integration af eksterne trusselsfeeds og indikatorer på kompromis (IOCs)
- **Hændelsesrespons**: Veldefinerede procedurer for detektion, respons og genopretning ved sikkerhedshændelser

#### **Zero Trust Arkitektur**
- **Aldrig Stol, Bekræft Altid**: Kontinuerlig verifikation af brugere, enheder og netværksforbindelser
- **Micro-segmentering**: Granulære netværkskontroller, der isolerer individuelle workloads og services
- **Identitetscentreret Sikkerhed**: Sikkerhedspolitikker baseret på verificerede identiteter frem for netværksplacering
- **Kontinuerlig Risikoanalyse**: Dynamisk evaluering af sikkerhedsposition baseret på aktuel kontekst og adfærd
- **Betinget Adgang**: Adgangskontroller, der tilpasser sig baseret på risikofaktorer, placering og enhedstillid

### Enterprise Integrationsmønstre

#### **Microsoft Sikkerhedsøkosystem Integration**
- **Microsoft Defender for Cloud**: Omfattende cloud sikkerhedsstyringspostur
- **Azure Sentinel**: Cloud-native SIEM og SOAR kapaciteter til AI arbejdsbelastningsbeskyttelse
- **Microsoft Entra ID**: Enterprise identitets- og adgangsstyring med betingede adgangspolitikker
- **Azure Key Vault**: Centraliseret secrets management med hardware-sikkerhedsmodul (HSM) backup
- **Microsoft Purview**: Datastyring og compliance for AI datakilder og arbejdsgange

#### **Compliance & Governance**
- **Regulatorisk Overensstemmelse**: Sikr at MCP-implementeringer opfylder branchespecifikke compliance-krav (GDPR, HIPAA, SOC 2)

- **Dataklassifikation**: Korrekt kategorisering og håndtering af følsomme data behandlet af AI-systemer
- **Revisionsspor**: Omfattende logføring for overholdelse af regler og retsmedicinsk undersøgelse
- **Privatlivskontroller**: Implementering af privatlivs-by-design principper i AI-systemarkitektur
- **Ændringsstyring**: Formelle processer til sikkerhedsgennemgang af ændringer i AI-systemer

Disse grundlæggende praksisser skaber en robust sikkerhedsbase, som øger effektiviteten af MCP-specifikke sikkerhedskontroller og giver omfattende beskyttelse af AI-drevne applikationer.

## Vigtige Sikkerhedsindsigter

- **Lagvis Sikkerhedstilgang**: Kombiner grundlæggende sikkerhedspraksis (sikker kodning, mindst privilegium, forsyningskædeverifikation, kontinuerlig overvågning) med AI-specifikke kontroller for omfattende beskyttelse

- **AI-Specifik Trusselslandskab**: MCP-systemer står over for unikke risici, herunder prompt-injektion, værktøjsforgiftning, session-kapring, forvirrede stedfortræder-problemer, token-gennemgangssårbarheder og overdrevne tilladelser, som kræver specialiserede afbødninger

- **Ekspertise i Autentificering & Autorisation**: Implementer robust autentificering ved brug af eksterne identitetsudbydere (Microsoft Entra ID), håndhæv korrekt tokenvalidering, og accepter aldrig tokens, der ikke eksplicit er udstedt til din MCP-server

- **Forebyggelse af AI-angreb**: Udrul Microsoft Prompt Shields og Azure Content Safety for at beskytte mod indirekte prompt-injektion og værktøjsforgiftning, samtidig med at værktøjsmetadata valideres og overvåges for dynamiske ændringer

- **Session- & Transport Sikkerhed**: Brug kryptografisk sikre, ikke-deterministiske sessions-ID'er knyttet til brugeridentiteter, implementer korrekt session livscyklusstyring, og brug aldrig sessions til autentificering

- **OAuth Sikkerhedspraksis**: Forebyg forvirrede stedfortræder-angreb gennem eksplicit brugeraccept for dynamisk registrerede klienter, korrekt OAuth 2.1-implementering med PKCE og streng validering af redirect URI  

- **Token Sikkerhedsprincipper**: Undgå anti-patterns med token-gennemgang, valider tokenets audience-claims, implementer kortlevet tokens med sikker rotation, og oprethold klare tillidsgrænser

- **Omfattende Forsyningskæde Sikkerhed**: Behandl alle AI-økosystemkomponenter (modeller, embeddings, kontekstudbydere, eksterne API'er) med samme sikkerhedsniveau som traditionelle softwareafhængigheder

- **Kontinuerlig Udvikling**: Hold dig opdateret med hurtigt udviklende MCP-specifikationer, bidrag til sikkerhedsstandarder i fællesskabet, og oprethold adaptive sikkerhedsstrategier efterhånden som protokollen modnes

- **Microsoft Sikkerhedsintegration**: Udnyt Microsofts omfattende sikkerhedsøkosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) for forbedret MCP-implementeringsbeskyttelse

## Omfattende Ressourcer

### **Officiel MCP Sikkerhedsdokumentation**
- [MCP Specifikation (Aktuel: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Sikkerhedsbedste Praksis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Autorisationsspecifikation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **OWASP MCP Sikkerhedsressourcer**
- [OWASP MCP Azure Sikkerhedsguide](https://microsoft.github.io/mcp-azure-security-guide/) - Omfattende OWASP MCP Top 10 med Azure-implementeringsvejledning
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Officielle OWASP MCP sikkerhedsrisici
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on sikkerhedstræning for MCP på Azure

### **Sikkerhedsstandarder & Bedste Praksis**
- [OAuth 2.0 Sikkerhedsbedste Praksis (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Webapplikationssikkerhed](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for Store Sprogmodeller](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **AI Sikkerhedsforskning & Analyse**
- [Prompt Injection i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Værktøjsforgiftning Angreb (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Sikkerhedsforskningsbriefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Sikkerhedsløsninger**
- [Microsoft Prompt Shields Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Sikkerhed](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Bedste Praksis](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementeringsvejledninger & Tutorials**
- [Azure API Management som MCP Autentificeringsgateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Autentificering med MCP Servere](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Sikker Tokenopbevaring og Kryptering (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Forsyningskæde Sikkerhed**
- [Azure DevOps Sikkerhed](https://azure.microsoft.com/products/devops)
- [Azure Repos Sikkerhed](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Forsyningskæde Sikkerhedsrejse](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Yderligere Sikkerhedsdokumentation**

For omfattende sikkerhedsanvisninger, henvis til disse specialiserede dokumenter i denne sektion:

- **[CIMD og DCR Autorisationsprøve](./samples/cimd-dcr-auth/README.md)** - Kørbar TypeScript MCP `2026-07-28` ressource-server, der sammenligner foretrukne Client ID Metadata-dokumenter med forældet Dynamisk Klientregistreringsfallback
- **[MCP Sikkerhedsbedste Praksis](./mcp-security-best-practices.md)** - Fuldstændig sikkerhedsbedste praksis for MCP-implementeringer
- **[Azure Content Safety Implementering](./azure-content-safety-implementation.md)** - Praktiske implementeringseksempler på Azure Content Safety integration  
- **[MCP Sikkerhedskontroller](./mcp-security-controls.md)** - Seneste sikkerhedskontroller og teknikker for MCP-udrulninger
- **[MCP Bedste Praksis Hurtig Reference](./mcp-best-practices.md)** - Hurtig referenceguide til essentielle MCP sikkerhedspraksisser
- **[BlueHat 2026: Sikring af AI's fremtid: Sikring af MCP med forsvar-i-dybden mønstre](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Forsvar-i-dybden mønstre fra Microsoft Security Response Center (MSRC)

### **Hands-On Sikkerhedstræning**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Omfattende hands-on workshop til sikring af MCP-servere i Azure med progressive lejre fra Base Camp til Summit
- **[OWASP MCP Azure Sikkerhedsguide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referencearkitektur og implementeringsvejledning for alle OWASP MCP Top 10 risici

---

## Hvad er næste

Næste: [Kapitel 3: Kom godt i gang](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->