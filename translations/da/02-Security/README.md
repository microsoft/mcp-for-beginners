# MCP-sikkerhed: Omfattende beskyttelse af AI-systemer

[![MCP Security Best Practices](../../../translated_images/da/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Klik på billedet ovenfor for at se videoen til denne lektion)_

Sikkerhed er grundlæggende for design af AI-systemer, og derfor prioriterer vi det som vores anden sektion. Dette stemmer overens med Microsofts **Secure by Design**-princip fra [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) bringer kraftfulde nye muligheder til AI-drevne applikationer, samtidig med at det introducerer unikke sikkerhedsudfordringer, der rækker ud over traditionelle software-risici. MCP-systemer står over for både etablerede sikkerhedsbekymringer (sikker kodning, mindst privilegium, forsyningskædesikkerhed) og nye AI-specifikke trusler, herunder promptinjektion, værktøjsforgiftning, sessionkapring, confused deputy-angreb, token-passthrough-sårbarheder og dynamisk kapacitetsmodifikation.

Denne lektion udforsker de mest kritiske sikkerhedsrisici i MCP-implementeringer—dækker autentificering, autorisation, overdrevne tilladelser, indirekte promptinjektion, sessionssikkerhed, confused deputy-problemer, tokenhåndtering og forsyningskædesårbarheder. Du vil lære handlingsorienterede kontroller og bedste praksis til at afbøde disse risici, samtidig med at du udnytter Microsoft-løsninger som Prompt Shields, Azure Content Safety og GitHub Advanced Security til at styrke din MCP-udrulning.

## Læringsmål

Ved slutningen af denne lektion vil du kunne:

- **Identificere MCP-specifikke trusler**: Genkende unikke sikkerhedsrisici i MCP-systemer, herunder promptinjektion, værktøjsforgiftning, overdrevne tilladelser, sessionkapring, confused deputy-problemer, token-passthrough-sårbarheder og forsyningskæderisici
- **Anvende sikkerhedskontroller**: Implementere effektive afbødninger, herunder robust autentificering, mindst privilegium-adgang, sikker tokenhåndtering, sessionssikkerhedskontroller og forsyningskædeverifikation
- **Udnytte Microsoft-sikkerhedsløsninger**: Forstå og implementere Microsoft Prompt Shields, Azure Content Safety og GitHub Advanced Security til beskyttelse af MCP-arbejdsbelastninger
- **Validere værktøjssikkerhed**: Genkende vigtigheden af validering af værktøjsmetadata, overvågning af dynamiske ændringer og forsvar mod indirekte promptinjektionsangreb
- **Integrere bedste praksis**: Kombinere etablerede sikkerhedsprincipper (sikker kodning, serverhærde, zero trust) med MCP-specifikke kontroller for omfattende beskyttelse

# MCP-sikkerhedsarkitektur & kontroller

Moderne MCP-implementeringer kræver lagdelte sikkerhedstilgange, der adresserer både traditionel softwaresikkerhed og AI-specifikke trusler. Den hurtigt udviklende MCP-specifikation modnes fortsat med sine sikkerhedskontroller, hvilket muliggør bedre integration med virksomheders sikkerhedsarkitekturer og etablerede bedste praksisser.

Forskning fra [Microsoft Digital Defense Report](https://aka.ms/mddr) viser, at **98 % af rapporterede brud ville blive forhindret ved robust sikkerhedshygiejne**. Den mest effektive beskyttelsesstrategi kombinerer grundlæggende sikkerhedspraksis med MCP-specifikke kontroller—beviste baseline-sikkerhedsforanstaltninger forbliver de mest indflydelsesrige til at reducere den samlede sikkerhedsrisiko.

## Nuværende sikkerhedssituation

> **Bemærk:** Disse oplysninger afspejler MCP-sikkerhedsstandarder pr. **18. december 2025**. MCP-protokollen udvikler sig hurtigt, og fremtidige implementeringer kan introducere nye autentificeringsmønstre og forbedrede kontroller. Henvis altid til den aktuelle [MCP-specifikation](https://spec.modelcontextprotocol.io/), [MCP GitHub-repository](https://github.com/modelcontextprotocol) og [dokumentation om bedste sikkerhedspraksis](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) for den nyeste vejledning.

### Udvikling af MCP-autentificering

MCP-specifikationen har udviklet sig betydeligt i sin tilgang til autentificering og autorisation:

- **Oprindelig tilgang**: Tidlige specifikationer krævede, at udviklere implementerede brugerdefinerede autentificeringsservere, hvor MCP-servere fungerede som OAuth 2.0-autoriseringsservere, der håndterede brugerautentificering direkte
- **Nuværende standard (2025-11-25)**: Opdateret specifikation tillader, at MCP-servere delegerer autentificering til eksterne identitetsudbydere (såsom Microsoft Entra ID), hvilket forbedrer sikkerhedsholdningen og reducerer implementeringskompleksiteten
- **Transport Layer Security**: Forbedret understøttelse af sikre transportmekanismer med korrekte autentificeringsmønstre for både lokale (STDIO) og fjernforbindelser (Streamable HTTP)

## Autentificering & autorisationssikkerhed

### Nuværende sikkerhedsudfordringer

Moderne MCP-implementeringer står over for flere autentificerings- og autorisationsudfordringer:

### Risici & trusselsvektorer

- **Fejlkonfigureret autorisationslogik**: Fejl i autorisationsimplementering i MCP-servere kan eksponere følsomme data og anvende adgangskontroller forkert
- **OAuth-tokenkompromittering**: Tyveri af lokale MCP-servertokens gør det muligt for angribere at udgive sig for at være servere og få adgang til nedstrøms tjenester
- **Token-passthrough-sårbarheder**: Forkert tokenhåndtering skaber omgåelser af sikkerhedskontroller og ansvarlighedsgab
- **Overdrevne tilladelser**: Overprivilegerede MCP-servere overtræder mindst privilegium-princippet og udvider angrebsoverflader

#### Token-passthrough: Et kritisk anti-mønster

**Token-passthrough er udtrykkeligt forbudt** i den nuværende MCP-autorisation-specifikation på grund af alvorlige sikkerhedsmæssige konsekvenser:

##### Omgåelse af sikkerhedskontroller
- MCP-servere og nedstrøms API’er implementerer kritiske sikkerhedskontroller (ratebegrænsning, anmodningsvalidering, trafikovervågning), der afhænger af korrekt tokenvalidering
- Direkte klient-til-API-tokenbrug omgår disse væsentlige beskyttelser og underminerer sikkerhedsarkitekturen

##### Ansvarlighed & revisionsudfordringer  
- MCP-servere kan ikke skelne mellem klienter, der bruger upstream-udstedte tokens, hvilket bryder revisionsspor
- Nedstrøms ressourcelogfiler viser vildledende anmodningskilder i stedet for faktiske MCP-servermellemled
- Hændelsesundersøgelser og overholdelsesrevisioner bliver betydeligt vanskeligere

##### Risiko for dataudtræk
- Uvaliderede tokenpåstande gør det muligt for ondsindede aktører med stjålne tokens at bruge MCP-servere som proxyer til dataudtræk
- Brud på tillidsgrænser tillader uautoriserede adgangsmønstre, der omgår tilsigtede sikkerhedskontroller

##### Angrebsvinkler med flere tjenester
- Kompromitterede tokens, der accepteres af flere tjenester, muliggør lateral bevægelse på tværs af tilknyttede systemer
- Tillidsantagelser mellem tjenester kan blive brudt, når tokenoprindelser ikke kan verificeres

### Sikkerhedskontroller & afbødninger

**Kritiske sikkerhedskrav:**

> **OBLIGATORISK**: MCP-servere **MÅ IKKE** acceptere nogen tokens, der ikke eksplicit er udstedt til MCP-serveren

#### Autentificerings- & autorisationskontroller

- **Grundig autorisationsgennemgang**: Udfør omfattende revisioner af MCP-serveres autorisationslogik for at sikre, at kun tilsigtede brugere og klienter kan få adgang til følsomme ressourcer
  - **Implementeringsvejledning**: [Azure API Management som autentificeringsgateway for MCP-servere](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitetsintegration**: [Brug af Microsoft Entra ID til MCP-serverautentificering](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Sikker tokenhåndtering**: Implementer [Microsofts bedste praksis for tokenvalidering og livscyklus](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Valider, at tokenaudience-påstande matcher MCP-serveridentiteten
  - Implementer korrekt tokenrotation og udløbspolitikker
  - Forhindre token-replay-angreb og uautoriseret brug

- **Beskyttet tokenlagring**: Sikr tokenlagring med kryptering både i hvile og under overførsel
  - **Bedste praksis**: [Retningslinjer for sikker tokenlagring og kryptering](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementering af adgangskontrol

- **Princippet om mindst privilegium**: Giv MCP-servere kun de minimale tilladelser, der kræves for den tilsigtede funktionalitet
  - Regelmæssige tilladelsesgennemgange og opdateringer for at forhindre privilegieudvidelse
  - **Microsoft-dokumentation**: [Sikker mindst-privilegeret adgang](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollebaseret adgangskontrol (RBAC)**: Implementer finmaskede rollefordelinger
  - Afgræns roller stramt til specifikke ressourcer og handlinger
  - Undgå brede eller unødvendige tilladelser, der udvider angrebsoverflader

- **Kontinuerlig tilladelsesovervågning**: Implementer løbende adgangsrevision og overvågning
  - Overvåg tilladelsesbrugsmønstre for anomalier
  - Afhjælp hurtigt overdrevne eller ubrugte privilegier

## AI-specifikke sikkerhedstrusler

### Promptinjektion & værktøjsmanipulationsangreb

Moderne MCP-implementeringer står over for sofistikerede AI-specifikke angreb, som traditionelle sikkerhedsforanstaltninger ikke fuldt ud kan imødegå:

#### **Indirekte promptinjektion (Cross-Domain Prompt Injection)**

**Indirekte promptinjektion** repræsenterer en af de mest kritiske sårbarheder i MCP-aktiverede AI-systemer. Angribere indlejrer ondsindede instruktioner i eksternt indhold—dokumenter, websider, e-mails eller datakilder—som AI-systemer efterfølgende behandler som legitime kommandoer.

**Angrebsscenarier:**
- **Dokumentbaseret injektion**: Ondsindede instruktioner skjult i behandlede dokumenter, der udløser utilsigtede AI-handlinger
- **Udnyttelse af webindhold**: Kompromitterede websider med indlejrede prompts, der manipulerer AI-adfærd ved scraping
- **E-mail-baserede angreb**: Ondsindede prompts i e-mails, der får AI-assistenter til at lække information eller udføre uautoriserede handlinger
- **Forurenede datakilder**: Kompromitterede databaser eller API’er, der leverer forurenet indhold til AI-systemer

**Virkelige konsekvenser**: Disse angreb kan resultere i dataudtræk, brud på privatlivets fred, generering af skadeligt indhold og manipulation af brugerinteraktioner. For detaljeret analyse, se [Prompt Injection i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/da/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Værktøjsforgiftning-angreb**

**Værktøjsforgiftning** retter sig mod metadata, der definerer MCP-værktøjer, og udnytter, hvordan LLM’er fortolker værktøjsbeskrivelser og parametre til at træffe eksekveringsbeslutninger.

**Angrebsmekanismer:**
- **Manipulation af metadata**: Angribere injicerer ondsindede instruktioner i værktøjsbeskrivelser, parameterdefinitioner eller brugseksempler
- **Usynlige instruktioner**: Skjulte prompts i værktøjsmetadata, der behandles af AI-modeller, men er usynlige for menneskelige brugere
- **Dynamisk værktøjsmodifikation ("Rug Pulls")**: Værktøjer, der er godkendt af brugere, ændres senere til at udføre ondsindede handlinger uden brugerens viden
- **Parameterinjektion**: Ondsindet indhold indlejret i værktøjsparameterskemaer, der påvirker modeladfærd

**Risici ved hostede servere**: Fjern-MCP-servere udgør forhøjede risici, da værktøjsdefinitioner kan opdateres efter initial brugeraccept, hvilket skaber scenarier, hvor tidligere sikre værktøjer bliver ondsindede. For omfattende analyse, se [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/da/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Yderligere AI-angrebsvinkler**

- **Cross-Domain Prompt Injection (XPIA)**: Sofistikerede angreb, der udnytter indhold fra flere domæner til at omgå sikkerhedskontroller
- **Dynamisk kapacitetsmodifikation**: Ændringer i realtid af værktøjskapaciteter, der undslipper indledende sikkerhedsvurderinger
- **Context Window Poisoning**: Angreb, der manipulerer store kontekstvinduer for at skjule ondsindede instruktioner
- **Model Confusion Angreb**: Udnyttelse af modellens begrænsninger til at skabe uforudsigelig eller usikker adfærd

### AI-sikkerhedsrisikos påvirkning

**Konsekvenser med høj påvirkning:**
- **Dataudtræk**: Uautoriseret adgang til og tyveri af følsomme virksomheds- eller persondata
- **Privatlivsbrud**: Eksponering af personligt identificerbare oplysninger (PII) og fortrolige forretningsdata  
- **Systemmanipulation**: Utilsigtede ændringer i kritiske systemer og arbejdsgange
- **Credential-tyveri**: Kompromittering af autentificeringstokens og servicelegitimationsoplysninger
- **Lateral bevægelse**: Brug af kompromitterede AI-systemer som springbræt til bredere netværksangreb

### Microsoft AI-sikkerhedsløsninger

#### **AI Prompt Shields: Avanceret beskyttelse mod injektionsangreb**

Microsoft **AI Prompt Shields** leverer omfattende forsvar mod både direkte og indirekte promptinjektionsangreb gennem flere sikkerhedslag:

##### **Kernebeskyttelsesmekanismer:**

1. **Avanceret detektion & filtrering**
   - Maskinlæringsalgoritmer og NLP-teknikker opdager ondsindede instruktioner i eksternt indhold
   - Realtidsanalyse af dokumenter, websider, e-mails og datakilder for indlejrede trusler
   - Kontekstuel forståelse af legitime vs. ondsindede promptmønstre

2. **Spotlighting-teknikker**  
   - Skelner mellem betroede systeminstruktioner og potentielt kompromitterede eksterne input
   - Teksttransformationsmetoder, der forbedrer modelrelevans samtidig med at ondsindet indhold isoleres
   - Hjælper AI-systemer med at opretholde korrekt instruktionshierarki og ignorere injicerede kommandoer

3. **Delimiter- & datamarkeringssystemer**
   - Eksplicit afgrænsning mellem betroede systembeskeder og ekstern inputtekst
   - Specielle markører fremhæver grænser mellem betroede og utroværdige datakilder
   - Klar adskillelse forhindrer instruktionsforvirring og uautoriseret kommandoeksekvering

4. **Kontinuerlig trusselsintelligens**
   - Microsoft overvåger løbende nye angrebsmønstre og opdaterer forsvar
   - Proaktiv trusselsjagt efter nye injektionsteknikker og angrebsvinkler
   - Regelmæssige opdateringer af sikkerhedsmodeller for at opretholde effektivitet mod udviklende trusler

5. **Integration med Azure Content Safety**
   - En del af den omfattende Azure AI Content Safety-suite
   - Yderligere detektion af jailbreak-forsøg, skadeligt indhold og overtrædelser af sikkerhedspolitikker
   - Enhedlige sikkerhedskontroller på tværs af AI-applikationskomponenter

**Implementeringsressourcer**: [Microsoft Prompt Shields Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/da/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Avancerede MCP-sikkerhedstrusler

### Sessionkapringssårbarheder

**Sessionkapring** repræsenterer en kritisk angrebsvinkel i stateful MCP-implementeringer, hvor uautoriserede parter opnår og misbruger legitime sessions-id’er for at udgive sig for at være klienter og udføre uautoriserede handlinger.

#### **Angrebsscenarier & risici**

- **Sessionkaprings-promptinjektion**: Angribere med stjålne session-id’er injicerer ondsindede hændelser i servere, der deler sessionstilstand, hvilket potentielt udløser skadelige handlinger eller adgang til følsomme data
- **Direkte udgivelse**: Stjålne session-id’er muliggør direkte MCP-serverkald, der omgår autentificering og behandler angribere som legitime brugere
- **Kompromitterede genoptagelige streams**: Angribere kan afbryde anmodninger for tidligt, hvilket får legitime klienter til at genoptage med potentielt ondsindet indhold

#### **Sikkerhedskontroller for sessionstyring**

**Kritiske krav:**
- **Autorisation Verifikation**: MCP-servere, der implementerer autorisation, **SKAL** verificere ALLE indgående forespørgsler og **MÅ IKKE** stole på sessioner til autentificering  
- **Sikker Session Generering**: Brug kryptografisk sikre, ikke-deterministiske session-ID'er genereret med sikre tilfældige talgeneratorer  
- **Bruger-specifik Binding**: Bind session-ID'er til bruger-specifik information ved brug af formater som `<user_id>:<session_id>` for at forhindre misbrug af sessioner på tværs af brugere  
- **Session Livscyklusstyring**: Implementer korrekt udløb, rotation og ugyldiggørelse for at begrænse sårbarhedsvinduer  
- **Transport Sikkerhed**: Obligatorisk HTTPS for al kommunikation for at forhindre opsnapning af session-ID'er  

### Forvirret Stedfortræder Problem

Det **forvirrede stedfortræder problem** opstår, når MCP-servere fungerer som autentificeringsproxyer mellem klienter og tredjepartstjenester, hvilket skaber muligheder for autorisationsomgåelse gennem udnyttelse af statiske klient-ID'er.

#### **Angrebsmetoder & Risici**

- **Cookie-baseret Samtykke Omgåelse**: Tidligere brugerautentificering skaber samtykkecookies, som angribere udnytter gennem ondsindede autorisationsanmodninger med manipulerede redirect-URI'er  
- **Tyveri af Autorisationskode**: Eksisterende samtykkecookies kan få autorisationsservere til at springe samtykkeskærme over og omdirigere koder til angriber-kontrollerede endepunkter  
- **Uautoriseret API Adgang**: Stjålne autorisationskoder muliggør token-udveksling og brugerudgivelse uden eksplicit godkendelse  

#### **Afhjælpningsstrategier**

**Obligatoriske Kontroller:**  
- **Eksplícit Samtykkekrav**: MCP-proxyservere, der bruger statiske klient-ID'er, **SKAL** indhente brugersamtykke for hver dynamisk registreret klient  
- **OAuth 2.1 Sikkerhedsimplementering**: Følg gældende OAuth-sikkerhedspraksis inklusive PKCE (Proof Key for Code Exchange) for alle autorisationsanmodninger  
- **Streng Klientvalidering**: Implementer grundig validering af redirect-URI'er og klientidentifikatorer for at forhindre udnyttelse  

### Token Passthrough Sårbarheder  

**Token passthrough** repræsenterer et eksplicit anti-mønster, hvor MCP-servere accepterer klienttokens uden korrekt validering og videresender dem til nedstrøms API'er, hvilket overtræder MCP-autorisation specifikationerne.

#### **Sikkerhedsmæssige Konsekvenser**

- **Omgåelse af Kontrol**: Direkte klient-til-API tokenbrug omgår kritiske begrænsninger, validering og overvågningskontroller  
- **Korrumpering af Revisionsspor**: Tokens udstedt opstrøms gør klientidentifikation umulig og bryder hændelsesundersøgelsesmuligheder  
- **Proxy-baseret Dataudtræk**: Uvaliderede tokens muliggør, at ondsindede aktører bruger servere som proxyer til uautoriseret dataadgang  
- **Brud på Tillidsgrænser**: Nedstrøms tjenesters tillidsantagelser kan blive brudt, når tokenoprindelse ikke kan verificeres  
- **Udvidelse af Multi-tjeneste Angreb**: Kompromitterede tokens accepteret på tværs af flere tjenester muliggør lateral bevægelse  

#### **Påkrævede Sikkerhedskontroller**

**Ikke-forhandlingsbare Krav:**  
- **Tokenvalidering**: MCP-servere **MÅ IKKE** acceptere tokens, der ikke eksplicit er udstedt til MCP-serveren  
- **Audience Verifikation**: Altid validér token-audience claims, så de matcher MCP-serverens identitet  
- **Korrekt Token Livscyklus**: Implementer kortlivede adgangstokens med sikre rotationspraksisser  

## Supply Chain Sikkerhed for AI-Systemer

Supply chain sikkerhed har udviklet sig ud over traditionelle softwareafhængigheder til at omfatte hele AI-økosystemet. Moderne MCP-implementeringer skal grundigt verificere og overvåge alle AI-relaterede komponenter, da hver enkelt introducerer potentielle sårbarheder, der kan kompromittere systemets integritet.

### Udvidede AI Supply Chain Komponenter

**Traditionelle Softwareafhængigheder:**  
- Open source biblioteker og frameworks  
- Containerbilleder og basesystemer  
- Udviklingsværktøjer og build pipelines  
- Infrastrukturkomponenter og tjenester  

**AI-specifikke Supply Chain Elementer:**  
- **Foundation Models**: Fortrænede modeller fra forskellige leverandører, der kræver proveniensverifikation  
- **Embedding Services**: Eksterne vektorisering- og semantiske søgetjenester  
- **Context Providers**: Datakilder, vidensbaser og dokumentarkiver  
- **Tredjeparts API'er**: Eksterne AI-tjenester, ML-pipelines og dataproceseendepunkter  
- **Model Artefakter**: Vægte, konfigurationer og finjusterede modelvarianter  
- **Træningsdatasæt**: Datasæt brugt til modeltræning og finjustering  

### Omfattende Supply Chain Sikkerhedsstrategi

#### **Komponentverifikation & Tillid**  
- **Proveniensvalidering**: Verificer oprindelse, licensering og integritet af alle AI-komponenter før integration  
- **Sikkerhedsvurdering**: Udfør sårbarhedsscanninger og sikkerhedsgennemgange af modeller, datakilder og AI-tjenester  
- **Omdømmeanalyse**: Evaluer sikkerhedshistorik og praksis hos AI-tjenesteudbydere  
- **Overholdelsesverifikation**: Sikr at alle komponenter opfylder organisatoriske sikkerheds- og regulatoriske krav  

#### **Sikre Deployments Pipelines**  
- **Automatiseret CI/CD Sikkerhed**: Integrer sikkerhedsscanning i automatiserede deployments pipelines  
- **Artefaktintegritet**: Implementer kryptografisk verifikation for alle deployerede artefakter (kode, modeller, konfigurationer)  
- **Faset Udrulning**: Brug progressive udrulningsstrategier med sikkerhedsvalidering i hver fase  
- **Betroede Artefaktarkiver**: Deploy kun fra verificerede, sikre artefaktregistre og arkiver  

#### **Kontinuerlig Overvågning & Respons**  
- **Afhængighedsscanning**: Løbende sårbarhedsovervågning for alle software- og AI-komponentafhængigheder  
- **Modelovervågning**: Kontinuerlig vurdering af modeladfærd, performance-drift og sikkerhedsanomalier  
- **Servicehelbredsopfølgning**: Overvåg eksterne AI-tjenester for tilgængelighed, sikkerhedshændelser og politikændringer  
- **Trusselsintelligens Integration**: Indarbejd trusselsfeeds specifikt for AI- og ML-sikkerhedsrisici  

#### **Adgangskontrol & Mindste Privilegium**  
- **Komponentniveau Tilladelser**: Begræns adgang til modeller, data og tjenester baseret på forretningsbehov  
- **Servicekonto Administration**: Implementer dedikerede servicekonti med minimale nødvendige tilladelser  
- **Netværkssegmentering**: Isoler AI-komponenter og begræns netværksadgang mellem tjenester  
- **API Gateway Kontroller**: Brug centraliserede API-gateways til at kontrollere og overvåge adgang til eksterne AI-tjenester  

#### **Hændelsesrespons & Genopretning**  
- **Hurtige Responsprocedurer**: Etablerede processer for patching eller udskiftning af kompromitterede AI-komponenter  
- **Credential Rotation**: Automatiserede systemer til rotation af hemmeligheder, API-nøgler og servicelegitimationsoplysninger  
- **Rollback Muligheder**: Evne til hurtigt at rulle tilbage til tidligere kendte gode versioner af AI-komponenter  
- **Supply Chain Brud Genopretning**: Specifikke procedurer for respons på kompromittering af opstrøms AI-tjenester  

### Microsoft Sikkerhedsværktøjer & Integration

**GitHub Advanced Security** tilbyder omfattende supply chain beskyttelse inklusive:  
- **Secret Scanning**: Automatisk detektion af legitimationsoplysninger, API-nøgler og tokens i repositories  
- **Afhængighedsscanning**: Sårbarhedsvurdering for open source afhængigheder og biblioteker  
- **CodeQL Analyse**: Statisk kodeanalyse for sikkerhedssårbarheder og kodningsproblemer  
- **Supply Chain Indsigter**: Synlighed i afhængigheders sundhed og sikkerhedsstatus  

**Azure DevOps & Azure Repos Integration:**  
- Sømløs sikkerhedsscanning på tværs af Microsofts udviklingsplatforme  
- Automatiske sikkerhedstjek i Azure Pipelines for AI-arbejdsbelastninger  
- Politikhåndhævelse for sikker AI-komponentudrulning  

**Microsoft Interne Praksisser:**  
Microsoft implementerer omfattende supply chain sikkerhedspraksisser på tværs af alle produkter. Læs om dokumenterede tilgange i [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Foundation Security Best Practices

MCP-implementeringer arver og bygger videre på din organisations eksisterende sikkerhedsholdning. Styrkelse af grundlæggende sikkerhedspraksisser forbedrer markant den samlede sikkerhed for AI-systemer og MCP-udrulninger.

### Kerne Sikkerhedsprincipper

#### **Sikre Udviklingspraksisser**  
- **OWASP Overholdelse**: Beskyt mod [OWASP Top 10](https://owasp.org/www-project-top-ten/) webapplikationssårbarheder  
- **AI-specifikke Beskyttelser**: Implementer kontroller for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Sikker Secrets Management**: Brug dedikerede vaults til tokens, API-nøgler og følsomme konfigurationsdata  
- **End-to-End Kryptering**: Implementer sikre kommunikationskanaler på tværs af alle applikationskomponenter og dataflows  
- **Inputvalidering**: Grundig validering af alle brugerinput, API-parametre og datakilder  

#### **Infrastruktur Hærdning**  
- **Multi-Faktor Autentificering**: Obligatorisk MFA for alle administrative og servicekonti  
- **Patch Management**: Automatiseret, rettidig patching af operativsystemer, frameworks og afhængigheder  
- **Identitetsudbyder Integration**: Centraliseret identitetsstyring via enterprise identitetsudbydere (Microsoft Entra ID, Active Directory)  
- **Netværkssegmentering**: Logisk isolering af MCP-komponenter for at begrænse lateral bevægelse  
- **Mindste Privilegium Princip**: Minimale nødvendige tilladelser for alle systemkomponenter og konti  

#### **Sikkerhedsovervågning & Detektion**  
- **Omfattende Logging**: Detaljeret logning af AI-applikationsaktiviteter, inklusive MCP klient-server interaktioner  
- **SIEM Integration**: Centraliseret sikkerhedsinformations- og hændelsesstyring til anomalidetektion  
- **Adfærdsanalyse**: AI-drevet overvågning for at opdage usædvanlige mønstre i system- og brugeradfærd  
- **Trusselsintelligens**: Integration af eksterne trusselsfeeds og kompromitteringsindikatorer (IOCs)  
- **Hændelsesrespons**: Veldefinerede procedurer for detektion, respons og genopretning ved sikkerhedshændelser  

#### **Zero Trust Arkitektur**  
- **Aldrig Stol, Altid Verificer**: Kontinuerlig verifikation af brugere, enheder og netværksforbindelser  
- **Mikrosegmentering**: Granulære netværkskontroller, der isolerer individuelle workloads og tjenester  
- **Identitetscentreret Sikkerhed**: Sikkerhedspolitikker baseret på verificerede identiteter frem for netværksplacering  
- **Kontinuerlig Risikovurdering**: Dynamisk evaluering af sikkerhedsholdning baseret på aktuel kontekst og adfærd  
- **Betinget Adgang**: Adgangskontroller, der tilpasses baseret på risikofaktorer, placering og enhedstillid  

### Enterprise Integrationsmønstre

#### **Microsoft Sikkerhedsøkosystem Integration**  
- **Microsoft Defender for Cloud**: Omfattende cloud sikkerhedsholdningsstyring  
- **Azure Sentinel**: Cloud-native SIEM og SOAR kapaciteter til beskyttelse af AI-arbejdsbelastninger  
- **Microsoft Entra ID**: Enterprise identitets- og adgangsstyring med betingede adgangspolitikker  
- **Azure Key Vault**: Centraliseret secrets management med hardware security module (HSM) backing  
- **Microsoft Purview**: Datastyring og compliance for AI-datakilder og workflows  

#### **Compliance & Governance**  
- **Regulatorisk Overensstemmelse**: Sikr at MCP-implementeringer opfylder branchespecifikke compliance-krav (GDPR, HIPAA, SOC 2)  
- **Dataklassificering**: Korrekt kategorisering og håndtering af følsomme data behandlet af AI-systemer  
- **Revisionsspor**: Omfattende logning til regulatorisk overholdelse og retsmedicinsk undersøgelse  
- **Privatlivskontroller**: Implementering af privacy-by-design principper i AI-systemarkitektur  
- **Change Management**: Formelle processer for sikkerhedsgennemgang af AI-systemændringer  

Disse grundlæggende praksisser skaber en robust sikkerhedsbase, der forbedrer effektiviteten af MCP-specifikke sikkerhedskontroller og giver omfattende beskyttelse for AI-drevne applikationer.

## Vigtige Sikkerhedsindsigter

- **Lagdelt Sikkerhedstilgang**: Kombiner grundlæggende sikkerhedspraksisser (sikker kodning, mindste privilegium, supply chain verifikation, kontinuerlig overvågning) med AI-specifikke kontroller for omfattende beskyttelse  

- **AI-specifik Trusselslandskab**: MCP-systemer står over for unikke risici, herunder prompt injection, tool poisoning, session hijacking, confused deputy problemer, token passthrough sårbarheder og overdrevne tilladelser, som kræver specialiserede afhjælpninger  

- **Autentificering & Autorisation Excellence**: Implementer robust autentificering ved brug af eksterne identitetsudbydere (Microsoft Entra ID), håndhæv korrekt tokenvalidering, og accepter aldrig tokens, der ikke eksplicit er udstedt til din MCP-server  

- **AI Angrebsforebyggelse**: Deploy Microsoft Prompt Shields og Azure Content Safety for at forsvare mod indirekte prompt injection og tool poisoning angreb, samtidig med at værktøjsmetadata valideres og dynamiske ændringer overvåges  

- **Session & Transport Sikkerhed**: Brug kryptografisk sikre, ikke-deterministiske session-ID'er bundet til brugeridentiteter, implementer korrekt session livscyklusstyring, og brug aldrig sessioner til autentificering  

- **OAuth Sikkerhedsbest Practices**: Forebyg confused deputy angreb gennem eksplicit brugersamtykke for dynamisk registrerede klienter, korrekt OAuth 2.1 implementering med PKCE, og streng redirect URI validering  

- **Token Sikkerhedsprincipper**: Undgå token passthrough anti-mønstre, validér token audience claims, implementer kortlivede tokens med sikker rotation, og oprethold klare tillidsgrænser  

- **Omfattende Supply Chain Sikkerhed**: Behandl alle AI-økosystemets komponenter (modeller, embeddings, context providers, eksterne API'er) med samme sikkerhedsniveau som traditionelle softwareafhængigheder  

- **Kontinuerlig Udvikling**: Hold dig opdateret med hurtigt udviklende MCP-specifikationer, bidrag til sikkerhedsfællesskabets standarder, og oprethold adaptive sikkerhedsholdninger efterhånden som protokollen modnes  

- **Microsoft Sikkerhedsintegration**: Udnyt Microsofts omfattende sikkerhedsøkosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) for forbedret MCP-udrulningsbeskyttelse  

## Omfattende Ressourcer

### **Officiel MCP Sikkerhedsdokumentation**  
- [MCP Specification (Current: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)  

### **Sikkerhedsstandarder & Best Practices**  
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft Digital Defense Report](https://aka.ms/mddr)  

### **AI Sikkerhedsforskning & Analyse**  
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Sikkerhedsforskningsbriefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Sikkerhedsløsninger**
- [Microsoft Prompt Shields Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Sikkerhed](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Bedste Praksis](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Avanceret Sikkerhed](https://github.com/security/advanced-security)

### **Implementeringsvejledninger & Tutorials**
- [Azure API Management som MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentication med MCP Servere](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Sikker Token Opbevaring og Kryptering (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Supply Chain Sikkerhed**
- [Azure DevOps Sikkerhed](https://azure.microsoft.com/products/devops)
- [Azure Repos Sikkerhed](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Sikkerhedsrejse](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Yderligere Sikkerhedsdokumentation**

For omfattende sikkerhedsguidance, se disse specialiserede dokumenter i denne sektion:

- **[MCP Sikkerheds Bedste Praksis 2025](./mcp-security-best-practices-2025.md)** - Fuldstændige sikkerhedsbedste praksisser for MCP-implementeringer
- **[Azure Content Safety Implementering](./azure-content-safety-implementation.md)** - Praktiske implementeringseksempler for Azure Content Safety integration  
- **[MCP Sikkerhedskontroller 2025](./mcp-security-controls-2025.md)** - Seneste sikkerhedskontroller og teknikker for MCP-udrulninger
- **[MCP Bedste Praksis Hurtig Reference](./mcp-best-practices.md)** - Hurtig referenceguide for essentielle MCP sikkerhedspraksisser

---

## Hvad er Næste

Næste: [Kapitel 3: Kom godt i gang](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->