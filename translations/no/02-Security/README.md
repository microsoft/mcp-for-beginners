# MCP Security: Omfattende beskyttelse for AI-systemer

[![MCP Security Best Practices](../../../translated_images/no/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Klikk på bildet over for å se video av denne leksjonen)_

Sikkerhet er grunnleggende for design av AI-systemer, og derfor prioriterer vi det som vår andre seksjon. Dette samsvarer med Microsofts **Secure by Design**-prinsipp fra [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) bringer kraftige nye muligheter til AI-drevne applikasjoner samtidig som det introduserer unike sikkerhetsutfordringer som går utover tradisjonelle programvarerisikoer. MCP-systemer står overfor både etablerte sikkerhetsbekymringer (sikker koding, minste privilegium, leverandørkjede-sikkerhet) og nye AI-spesifikke trusler inkludert prompt-injeksjon, verktøyforgiftning, sesjonskapring, confused deputy-angrep, token-passthrough-sårbarheter og dynamisk modifisering av kapasiteter.

Denne leksjonen utforsker de mest kritiske sikkerhetsrisikoene i MCP-implementasjoner—dekker autentisering, autorisasjon, overdrevne tillatelser, indirekte prompt-injeksjon, sesjonssikkerhet, confused deputy-problemer, tokenhåndtering og leverandørkjede-sårbarheter. Du vil lære handlingsrettede kontroller og beste praksis for å redusere disse risikoene samtidig som du utnytter Microsoft-løsninger som Prompt Shields, Azure Content Safety og GitHub Advanced Security for å styrke din MCP-distribusjon.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- **Identifisere MCP-spesifikke trusler**: Gjenkjenne unike sikkerhetsrisikoer i MCP-systemer inkludert prompt-injeksjon, verktøyforgiftning, overdrevne tillatelser, sesjonskapring, confused deputy-problemer, token-passthrough-sårbarheter og leverandørkjede-risikoer
- **Anvende sikkerhetskontroller**: Implementere effektive tiltak inkludert robust autentisering, minste privilegium-tilgang, sikker tokenhåndtering, sesjonssikkerhetskontroller og leverandørkjedeverifisering
- **Utnytte Microsoft sikkerhetsløsninger**: Forstå og distribuere Microsoft Prompt Shields, Azure Content Safety og GitHub Advanced Security for beskyttelse av MCP-arbeidsbelastninger
- **Validere verktøysikkerhet**: Gjenkjenne viktigheten av validering av verktøymetadata, overvåking av dynamiske endringer og forsvar mot indirekte prompt-injeksjonsangrep
- **Integrere beste praksis**: Kombinere etablerte sikkerhetsfundamenter (sikker koding, serverherding, zero trust) med MCP-spesifikke kontroller for omfattende beskyttelse

# MCP sikkerhetsarkitektur og kontroller

Moderne MCP-implementasjoner krever lagdelte sikkerhetstilnærminger som adresserer både tradisjonell programvaresikkerhet og AI-spesifikke trusler. Den raskt utviklende MCP-spesifikasjonen modnes kontinuerlig sine sikkerhetskontroller, noe som muliggjør bedre integrasjon med bedriftsikkerhetsarkitekturer og etablerte beste praksiser.

Forskning fra [Microsoft Digital Defense Report](https://aka.ms/mddr) viser at **98 % av rapporterte brudd ville vært forhindret med robust sikkerhetshygiene**. Den mest effektive beskyttelsesstrategien kombinerer grunnleggende sikkerhetspraksis med MCP-spesifikke kontroller—beviste baselinesikkerhetstiltak forblir de mest innflytelsesrike for å redusere samlet sikkerhetsrisiko.

## Nåværende sikkerhetslandskap

> **Merk:** Denne informasjonen reflekterer MCP-sikkerhetsstandarder per **18. desember 2025**. MCP-protokollen utvikler seg raskt, og fremtidige implementasjoner kan introdusere nye autentiseringsmønstre og forbedrede kontroller. Henvis alltid til gjeldende [MCP Specification](https://spec.modelcontextprotocol.io/), [MCP GitHub repository](https://github.com/modelcontextprotocol) og [sikkerhetsbeste praksis-dokumentasjon](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) for siste veiledning.

### Utvikling av MCP-autentisering

MCP-spesifikasjonen har utviklet seg betydelig i sin tilnærming til autentisering og autorisasjon:

- **Opprinnelig tilnærming**: Tidlige spesifikasjoner krevde at utviklere implementerte egne autentiseringsservere, med MCP-servere som OAuth 2.0 autorisasjonsservere som håndterte brukerautentisering direkte
- **Nåværende standard (2025-11-25)**: Oppdatert spesifikasjon tillater MCP-servere å delegere autentisering til eksterne identitetsleverandører (som Microsoft Entra ID), noe som forbedrer sikkerhetsposisjonen og reduserer implementeringskompleksitet
- **Transport Layer Security**: Forbedret støtte for sikre transportmekanismer med riktige autentiseringsmønstre for både lokale (STDIO) og eksterne (Streamable HTTP) tilkoblinger

## Autentisering og autorisasjonssikkerhet

### Nåværende sikkerhetsutfordringer

Moderne MCP-implementasjoner møter flere autentiserings- og autorisasjonsutfordringer:

### Risikoer og trusselvektorer

- **Feilkonfigurert autorisasjonslogikk**: Feil i autorisasjonsimplementasjon i MCP-servere kan eksponere sensitiv data og feilaktig anvende tilgangskontroller
- **OAuth-token kompromittering**: Tyveri av lokale MCP-servertokens gjør at angripere kan utgi seg for servere og få tilgang til nedstrøms tjenester
- **Token-passthrough-sårbarheter**: Feil håndtering av tokens skaper omgåelser av sikkerhetskontroller og ansvarsgap
- **Overdrevne tillatelser**: MCP-servere med for høye privilegier bryter minste privilegium-prinsippet og utvider angrepsflaten

#### Token Passthrough: Et kritisk anti-mønster

**Token passthrough er eksplisitt forbudt** i gjeldende MCP-autorisasjonsspesifikasjon på grunn av alvorlige sikkerhetsimplikasjoner:

##### Omgåelse av sikkerhetskontroller
- MCP-servere og nedstrøms API-er implementerer kritiske sikkerhetskontroller (ratebegrensning, forespørselsvalidering, trafikkovervåking) som avhenger av korrekt tokenvalidering
- Direkte klient-til-API tokenbruk omgår disse essensielle beskyttelsene og undergraver sikkerhetsarkitekturen

##### Ansvarlighet og revisjonsutfordringer  
- MCP-servere kan ikke skille mellom klienter som bruker tokens utstedt oppstrøms, noe som bryter revisjonsspor
- Nedstrøms ressursserverlogger viser misvisende forespørselsopprinnelse i stedet for faktiske MCP-servermellomledd
- Hendelsesundersøkelser og samsvarsrevisjoner blir betydelig vanskeligere

##### Risiko for dataeksfiltrasjon
- Uvaliderte tokenpåstander gjør det mulig for ondsinnede aktører med stjålne tokens å bruke MCP-servere som proxyer for dataeksfiltrasjon
- Brudd på tillitsgrenser tillater uautorisert tilgang som omgår tiltenkte sikkerhetskontroller

##### Angrepsvektorer med flere tjenester
- Kompromitterte tokens akseptert av flere tjenester muliggjør lateral bevegelse på tvers av tilkoblede systemer
- Tillitsantakelser mellom tjenester kan brytes når tokenopprinnelse ikke kan verifiseres

### Sikkerhetskontroller og tiltak

**Kritiske sikkerhetskrav:**

> **OBLIGATORISK**: MCP-servere **MÅ IKKE** akseptere noen tokens som ikke eksplisitt er utstedt for MCP-serveren

#### Autentiserings- og autorisasjonskontroller

- **Grundig autorisasjonsgjennomgang**: Utfør omfattende revisjoner av MCP-serveres autorisasjonslogikk for å sikre at kun tiltenkte brukere og klienter får tilgang til sensitive ressurser
  - **Implementeringsveiledning**: [Azure API Management som autentiseringsgateway for MCP-servere](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitetsintegrasjon**: [Bruke Microsoft Entra ID for MCP-serverautentisering](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Sikker tokenhåndtering**: Implementer [Microsofts beste praksis for tokenvalidering og livssyklus](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Valider at token audience-påstander samsvarer med MCP-serveridentitet
  - Implementer riktig tokenrotasjon og utløpspolicyer
  - Forhindre token replay-angrep og uautorisert bruk

- **Beskyttet tokenlagring**: Sikre tokenlagring med kryptering både i ro og under overføring
  - **Beste praksis**: [Retningslinjer for sikker tokenlagring og kryptering](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementering av tilgangskontroll

- **Prinsippet om minste privilegium**: Gi MCP-servere kun minimumstillatelser som kreves for tiltenkt funksjonalitet
  - Regelmessige tillatelsesgjennomganger og oppdateringer for å forhindre privilegiekryp
  - **Microsoft-dokumentasjon**: [Sikker minsteprivilegium-tilgang](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollebasert tilgangskontroll (RBAC)**: Implementer finmasket rollefordeling
  - Avgrens roller stramt til spesifikke ressurser og handlinger
  - Unngå brede eller unødvendige tillatelser som utvider angrepsflaten

- **Kontinuerlig tillatelsesovervåking**: Implementer løpende tilgangsrevisjon og overvåking
  - Overvåk mønstre for tillatelsesbruk for anomalier
  - Raskt utbedre overdrevne eller ubrukte privilegier

## AI-spesifikke sikkerhetstrusler

### Prompt-injeksjon og verktøymanipuleringsangrep

Moderne MCP-implementasjoner møter sofistikerte AI-spesifikke angrepsvektorer som tradisjonelle sikkerhetstiltak ikke fullt ut kan adressere:

#### **Indirekte prompt-injeksjon (Cross-Domain Prompt Injection)**

**Indirekte prompt-injeksjon** representerer en av de mest kritiske sårbarhetene i MCP-aktiverte AI-systemer. Angripere legger inn ondsinnede instruksjoner i eksternt innhold—dokumenter, nettsider, e-poster eller datakilder—som AI-systemer deretter behandler som legitime kommandoer.

**Angrepsscenarier:**
- **Dokumentbasert injeksjon**: Ondsinnede instruksjoner skjult i behandlede dokumenter som utløser utilsiktede AI-handlinger
- **Utnyttelse av webinnhold**: Kompromitterte nettsider med innebygde prompts som manipulerer AI-atferd ved innhenting
- **E-postbaserte angrep**: Ondsinnede prompts i e-poster som får AI-assistenter til å lekke informasjon eller utføre uautoriserte handlinger
- **Forurensning av datakilder**: Kompromitterte databaser eller API-er som leverer forurenset innhold til AI-systemer

**Virkelige konsekvenser**: Disse angrepene kan føre til dataeksfiltrasjon, personvernbrudd, generering av skadelig innhold og manipulering av brukerinteraksjoner. For detaljert analyse, se [Prompt Injection i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/no/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Verktøyforgiftning-angrep**

**Verktøyforgiftning** retter seg mot metadata som definerer MCP-verktøy, og utnytter hvordan LLM-er tolker verktøybeskrivelser og parametere for å ta beslutninger om utførelse.

**Angrepsmekanismer:**
- **Manipulering av metadata**: Angripere injiserer ondsinnede instruksjoner i verktøybeskrivelser, parameterdefinisjoner eller bruks-eksempler
- **Usynlige instruksjoner**: Skjulte prompts i verktøymetadata som behandles av AI-modeller, men er usynlige for menneskelige brukere
- **Dynamisk verktøymodifisering ("Rug Pulls")**: Verktøy godkjent av brukere endres senere for å utføre ondsinnede handlinger uten brukerens viten
- **Parameterinjeksjon**: Ondsinnet innhold innebygd i verktøyparametreskjemaer som påvirker modellens atferd

**Risiko ved hostede servere**: Eksterne MCP-servere utgjør forhøyet risiko da verktøydefinisjoner kan oppdateres etter initial brukeraksept, noe som skaper scenarioer hvor tidligere trygge verktøy blir ondsinnede. For omfattende analyse, se [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/no/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Ytterligere AI-angrepsvektorer**

- **Cross-Domain Prompt Injection (XPIA)**: Sofistikerte angrep som utnytter innhold fra flere domener for å omgå sikkerhetskontroller
- **Dynamisk kapasitetsmodifisering**: Sanntidsendringer i verktøykapasiteter som unngår initial sikkerhetsvurdering
- **Context Window Poisoning**: Angrep som manipulerer store kontekstvinduer for å skjule ondsinnede instruksjoner
- **Model Confusion Angrep**: Utnyttelse av modellbegrensninger for å skape uforutsigbar eller usikker atferd

### AI-sikkerhetsrisikoens konsekvenser

**Høyt påvirkningsnivå:**
- **Dataeksfiltrasjon**: Uautorisert tilgang og tyveri av sensitiv bedrifts- eller persondata
- **Personvernbrudd**: Eksponering av personlig identifiserbar informasjon (PII) og konfidensielle forretningsdata  
- **Systemmanipulering**: Utilsiktede endringer i kritiske systemer og arbeidsflyter
- **Tyveri av legitimasjon**: Kompromittering av autentiseringstokener og tjenestekredentialer
- **Lateral bevegelse**: Bruk av kompromitterte AI-systemer som pivot for bredere nettverksangrep

### Microsoft AI-sikkerhetsløsninger

#### **AI Prompt Shields: Avansert beskyttelse mot injeksjonsangrep**

Microsoft **AI Prompt Shields** gir omfattende forsvar mot både direkte og indirekte prompt-injeksjonsangrep gjennom flere sikkerhetslag:

##### **Kjernebeskyttelsesmekanismer:**

1. **Avansert deteksjon og filtrering**
   - Maskinlæringsalgoritmer og NLP-teknikker oppdager ondsinnede instruksjoner i eksternt innhold
   - Sanntidsanalyse av dokumenter, nettsider, e-poster og datakilder for innebygde trusler
   - Kontekstuell forståelse av legitime vs. ondsinnede promptmønstre

2. **Spotlighting-teknikker**  
   - Skiller mellom betrodde systeminstruksjoner og potensielt kompromitterte eksterne input
   - Teksttransformasjonsmetoder som forbedrer modellrelevans samtidig som ondsinnet innhold isoleres
   - Hjelper AI-systemer med å opprettholde riktig instruksjonshierarki og ignorere injiserte kommandoer

3. **Delimiter- og datamerkingssystemer**
   - Eksplisitt grense-definisjon mellom betrodde systemmeldinger og ekstern inputtekst
   - Spesielle markører som fremhever grenser mellom betrodde og ubetrodd datakilder
   - Klar separasjon forhindrer instruksjonsforvirring og uautorisert kommandoeksekvering

4. **Kontinuerlig trusselintelligens**
   - Microsoft overvåker kontinuerlig nye angrepsmønstre og oppdaterer forsvar
   - Proaktiv trusseljakt etter nye injeksjonsteknikker og angrepsvektorer
   - Regelmessige sikkerhetsmodelloppdateringer for å opprettholde effektivitet mot utviklende trusler

5. **Integrasjon med Azure Content Safety**
   - Del av omfattende Azure AI Content Safety-pakke
   - Ytterligere deteksjon for jailbreak-forsøk, skadelig innhold og sikkerhetspolicybrudd
   - Enhetlige sikkerhetskontroller på tvers av AI-applikasjonskomponenter

**Implementeringsressurser**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/no/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Avanserte MCP-sikkerhetstrusler

### Sesjonskapringssårbarheter

**Sesjonskapring** representerer en kritisk angrepsvektor i stateful MCP-implementasjoner hvor uautoriserte parter oppnår og misbruker legitime sesjonsidentifikatorer for å utgi seg for klienter og utføre uautoriserte handlinger.

#### **Angrepsscenarier og risikoer**

- **Sesjonskaprings-prompt-injeksjon**: Angripere med stjålne sesjons-ID-er injiserer ondsinnede hendelser i servere som deler sesjonstilstand, noe som potensielt utløser skadelige handlinger eller tilgang til sensitiv data
- **Direkte utgi seg for**: Stjålne sesjons-ID-er muliggjør direkte MCP-serverkall som omgår autentisering, og behandler angripere som legitime brukere
- **Kompromitterte gjenopptakbare strømmer**: Angripere kan avslutte forespørsler for tidlig, noe som får legitime klienter til å gjenoppta med potensielt ondsinnet innhold

#### **Sikkerhetskontroller for sesjonshåndtering**

**Kritiske krav:**
- **Autorisasjonsverifisering**: MCP-servere som implementerer autorisasjon **MÅ** verifisere ALLE innkommende forespørsler og **MÅ IKKE** stole på økter for autentisering  
- **Sikker øktgenerering**: Bruk kryptografisk sikre, ikke-deterministiske økt-IDer generert med sikre tilfeldige tallgeneratorer  
- **Brukerspesifikk binding**: Bind økt-IDer til brukerspesifikk informasjon ved bruk av formater som `<user_id>:<session_id>` for å forhindre misbruk av økter på tvers av brukere  
- **Håndtering av øktens livssyklus**: Implementer riktig utløp, rotasjon og ugyldiggjøring for å begrense sårbarhetsvinduer  
- **Transport-sikkerhet**: Obligatorisk HTTPS for all kommunikasjon for å forhindre avlytting av økt-IDer  

### Problemet med forvirret stedfortreder

**Problemet med forvirret stedfortreder** oppstår når MCP-servere fungerer som autentiseringsproxyer mellom klienter og tredjepartstjenester, noe som skaper muligheter for autorisasjonsomgåelse gjennom utnyttelse av statiske klient-IDer.

#### **Angrepsmekanismer og risikoer**

- **Omgåelse av samtykke basert på informasjonskapsler**: Tidligere brukerautentisering skaper samtykke-informasjonskapsler som angripere utnytter gjennom ondsinnede autorisasjonsforespørsler med manipulerte redirect-URIer  
- **Tyveri av autorisasjonskode**: Eksisterende samtykke-informasjonskapsler kan føre til at autorisasjonsservere hopper over samtykkeskjermer og videresender koder til angriperkontrollerte endepunkter  
- **Uautorisert API-tilgang**: Stjålne autorisasjonskoder muliggjør tokenutveksling og brukerutgivelse uten eksplisitt godkjenning  

#### **Avbøtende strategier**

**Obligatoriske kontroller:**  
- **Eksplisitte samtykkekrav**: MCP-proxyservere som bruker statiske klient-IDer **MÅ** innhente brukersamtykke for hver dynamisk registrerte klient  
- **OAuth 2.1 sikkerhetsimplementering**: Følg gjeldende OAuth-sikkerhetspraksis inkludert PKCE (Proof Key for Code Exchange) for alle autorisasjonsforespørsler  
- **Streng klientvalidering**: Implementer grundig validering av redirect-URIer og klientidentifikatorer for å forhindre utnyttelse  

### Sårbarheter ved token-gjennomgang  

**Token-gjennomgang** representerer et eksplisitt anti-mønster hvor MCP-servere aksepterer klienttoken uten riktig validering og videresender dem til nedstrøms APIer, noe som bryter med MCPs autorisasjonsspesifikasjoner.

#### **Sikkerhetsimplikasjoner**

- **Omgåelse av kontroll**: Direkte klient-til-API tokenbruk omgår kritiske begrensninger på hastighet, validering og overvåking  
- **Korrupsjon av revisjonsspor**: Token utstedt oppstrøms gjør klientidentifikasjon umulig, noe som bryter etterforskningsevner ved hendelser  
- **Proxy-basert dataeksfiltrasjon**: Uvaliderte token gjør det mulig for ondsinnede aktører å bruke servere som proxyer for uautorisert dataadgang  
- **Brudd på tillitsgrenser**: Nedstrøms tjenester kan få brutt sine tillitsantakelser når token-opprinnelse ikke kan verifiseres  
- **Utvidelse av angrep på tvers av tjenester**: Kompromitterte token akseptert på flere tjenester muliggjør lateral bevegelse  

#### **Påkrevde sikkerhetskontroller**

**Ikke-forhandlingsbare krav:**  
- **Tokenvalidering**: MCP-servere **MÅ IKKE** akseptere token som ikke eksplisitt er utstedt for MCP-serveren  
- **Publikumsverifisering**: Alltid valider at tokenets audience-krav samsvarer med MCP-serverens identitet  
- **Riktig tokenlivssyklus**: Implementer kortlivede tilgangstoken med sikre rotasjonsrutiner  

## Leverandørkjede-sikkerhet for AI-systemer

Leverandørkjede-sikkerhet har utviklet seg utover tradisjonelle programvareavhengigheter til å omfatte hele AI-økosystemet. Moderne MCP-implementasjoner må grundig verifisere og overvåke alle AI-relaterte komponenter, da hver enkelt introduserer potensielle sårbarheter som kan kompromittere systemintegriteten.

### Utvidede AI-leverandørkjede-komponenter

**Tradisjonelle programvareavhengigheter:**  
- Open source-biblioteker og rammeverk  
- Containerbilder og basisystemer  
- Utviklingsverktøy og bygg-pipelines  
- Infrastrukturkomponenter og tjenester  

**AI-spesifikke leverandørkjedeelementer:**  
- **Grunnmodeller**: Fortrente modeller fra ulike leverandører som krever proveniensverifisering  
- **Embedding-tjenester**: Eksterne vektorisering- og semantiske søketjenester  
- **Kontekstleverandører**: Datakilder, kunnskapsbaser og dokumentarkiver  
- **Tredjeparts-APIer**: Eksterne AI-tjenester, ML-pipelines og dataprosesseringsendepunkter  
- **Modellartefakter**: Vekter, konfigurasjoner og finjusterte modellvarianter  
- **Treningsdatasett**: Datasett brukt til modelltrening og finjustering  

### Omfattende leverandørkjede-sikkerhetsstrategi

#### **Komponentverifisering og tillit**  
- **Proveniensvalidering**: Verifiser opprinnelse, lisensiering og integritet for alle AI-komponenter før integrasjon  
- **Sikkerhetsvurdering**: Utfør sårbarhetsskanninger og sikkerhetsgjennomganger for modeller, datakilder og AI-tjenester  
- **Omdømmeanalyse**: Evaluer sikkerhetshistorikk og praksis hos AI-tjenesteleverandører  
- **Samsvarsverifisering**: Sørg for at alle komponenter oppfyller organisatoriske sikkerhets- og regulatoriske krav  

#### **Sikre distribusjonspipelines**  
- **Automatisert CI/CD-sikkerhet**: Integrer sikkerhetsskanning gjennom automatiserte distribusjonspipelines  
- **Artefaktintegritet**: Implementer kryptografisk verifisering for alle distribuerte artefakter (kode, modeller, konfigurasjoner)  
- **Trinnvis distribusjon**: Bruk progressive distribusjonsstrategier med sikkerhetsvalidering i hvert trinn  
- **Pålitelige artefakt-repositorier**: Distribuer kun fra verifiserte, sikre artefaktregistre og repositorier  

#### **Kontinuerlig overvåking og respons**  
- **Avhengighetsskanning**: Løpende sårbarhetsovervåking for alle programvare- og AI-komponentavhengigheter  
- **Modellovervåking**: Kontinuerlig vurdering av modellatferd, ytelsesavvik og sikkerhetsanomalier  
- **Tjenestehelseovervåking**: Overvåk eksterne AI-tjenester for tilgjengelighet, sikkerhetshendelser og policyendringer  
- **Trusselintelligensintegrasjon**: Inkluder trusseldata spesifikke for AI- og ML-sikkerhetsrisikoer  

#### **Tilgangskontroll og minste privilegium**  
- **Komponentnivå-tillatelser**: Begrens tilgang til modeller, data og tjenester basert på forretningsbehov  
- **Tjenestekontoadministrasjon**: Implementer dedikerte tjenestekontoer med minimale nødvendige tillatelser  
- **Nettverkssegmentering**: Isoler AI-komponenter og begrens nettverkstilgang mellom tjenester  
- **API-gateway-kontroller**: Bruk sentraliserte API-gatewayer for å kontrollere og overvåke tilgang til eksterne AI-tjenester  

#### **Hendelsesrespons og gjenoppretting**  
- **Raske responsprosedyrer**: Etablerte prosesser for patching eller utskifting av kompromitterte AI-komponenter  
- **Legitimasjonsrotasjon**: Automatiserte systemer for rotasjon av hemmeligheter, API-nøkler og tjenestekredentialer  
- **Rollback-muligheter**: Evne til raskt å rulle tilbake til tidligere kjente gode versjoner av AI-komponenter  
- **Gjenoppretting ved leverandørkjedebrudd**: Spesifikke prosedyrer for respons ved kompromittering av oppstrøms AI-tjenester  

### Microsoft sikkerhetsverktøy og integrasjon

**GitHub Advanced Security** tilbyr omfattende leverandørkjede-beskyttelse inkludert:  
- **Hemmelighetsskanning**: Automatisk deteksjon av legitimasjon, API-nøkler og token i repositorier  
- **Avhengighetsskanning**: Sårbarhetsvurdering for open source-avhengigheter og biblioteker  
- **CodeQL-analyse**: Statisk kodeanalyse for sikkerhetssårbarheter og kodeproblemer  
- **Leverandørkjedeinnsikt**: Synlighet i avhengighetshelse og sikkerhetsstatus  

**Azure DevOps & Azure Repos-integrasjon:**  
- Sømløs sikkerhetsskanning på tvers av Microsofts utviklingsplattformer  
- Automatiserte sikkerhetssjekker i Azure Pipelines for AI-arbeidsbelastninger  
- Policyhåndhevelse for sikker distribusjon av AI-komponenter  

**Microsofts interne praksis:**  
Microsoft implementerer omfattende leverandørkjede-sikkerhetspraksis på tvers av alle produkter. Les om velprøvde tilnærminger i [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Grunnleggende sikkerhetspraksis

MCP-implementasjoner arver og bygger videre på organisasjonens eksisterende sikkerhetsposisjon. Å styrke grunnleggende sikkerhetspraksis forbedrer betydelig den totale sikkerheten for AI-systemer og MCP-distribusjoner.

### Kjerneprinsipper for sikkerhet

#### **Sikre utviklingspraksiser**  
- **OWASP-overholdelse**: Beskytt mot [OWASP Top 10](https://owasp.org/www-project-top-ten/) sårbarheter i webapplikasjoner  
- **AI-spesifikke beskyttelser**: Implementer kontroller for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Sikker hemmelighetshåndtering**: Bruk dedikerte hvelv for token, API-nøkler og sensitiv konfigurasjonsdata  
- **Ende-til-ende-kryptering**: Implementer sikre kommunikasjoner på tvers av alle applikasjonskomponenter og dataflyter  
- **Inputvalidering**: Grundig validering av alle brukerinput, API-parametere og datakilder  

#### **Infrastrukturherding**  
- **Multifaktorautentisering**: Obligatorisk MFA for alle administrative og tjenestekontoer  
- **Patchhåndtering**: Automatisert, tidsriktig patching for operativsystemer, rammeverk og avhengigheter  
- **Identitetsleverandørintegrasjon**: Sentralisert identitetshåndtering gjennom bedriftsidentitetsleverandører (Microsoft Entra ID, Active Directory)  
- **Nettverkssegmentering**: Logisk isolasjon av MCP-komponenter for å begrense lateral bevegelse  
- **Prinsippet om minste privilegium**: Minimale nødvendige tillatelser for alle systemkomponenter og kontoer  

#### **Sikkerhetsovervåking og deteksjon**  
- **Omfattende logging**: Detaljert logging av AI-applikasjonsaktiviteter, inkludert MCP klient-server-interaksjoner  
- **SIEM-integrasjon**: Sentralisert sikkerhetsinformasjons- og hendelseshåndtering for anomali-deteksjon  
- **Atferdsanalyse**: AI-drevet overvåking for å oppdage uvanlige mønstre i system- og brukeradferd  
- **Trusselintelligens**: Integrasjon av eksterne trusseldata og kompromissindikatorer (IOC)  
- **Hendelsesrespons**: Veldefinerte prosedyrer for deteksjon, respons og gjenoppretting ved sikkerhetshendelser  

#### **Zero Trust-arkitektur**  
- **Aldri stol på, alltid verifiser**: Kontinuerlig verifisering av brukere, enheter og nettverkstilkoblinger  
- **Mikrosegmentering**: Granulære nettverkskontroller som isolerer individuelle arbeidsbelastninger og tjenester  
- **Identitetssentrert sikkerhet**: Sikkerhetspolicyer basert på verifiserte identiteter fremfor nettverksplassering  
- **Kontinuerlig risikovurdering**: Dynamisk evaluering av sikkerhetsposisjon basert på nåværende kontekst og adferd  
- **Betinget tilgang**: Tilgangskontroller som tilpasses basert på risikofaktorer, lokasjon og enhetstillit  

### Mønstre for bedriftsintegrasjon

#### **Integrasjon i Microsofts sikkerhetsekosystem**  
- **Microsoft Defender for Cloud**: Omfattende sky-sikkerhetsstyring  
- **Azure Sentinel**: Sky-native SIEM og SOAR-funksjoner for beskyttelse av AI-arbeidsbelastninger  
- **Microsoft Entra ID**: Bedriftsidentitets- og tilgangsstyring med betingede tilgangspolicyer  
- **Azure Key Vault**: Sentralisert hemmelighetshåndtering med hardware security module (HSM) støtte  
- **Microsoft Purview**: Datastyring og samsvar for AI-datakilder og arbeidsflyter  

#### **Samsvar og styring**  
- **Regulatorisk tilpasning**: Sørg for at MCP-implementasjoner oppfyller bransjespesifikke samsvarskrav (GDPR, HIPAA, SOC 2)  
- **Dataklassifisering**: Korrekt kategorisering og håndtering av sensitiv data behandlet av AI-systemer  
- **Revisjonsspor**: Omfattende logging for regulatorisk samsvar og rettsmedisinsk etterforskning  
- **Personvernkontroller**: Implementering av personvern-ved-design-prinsipper i AI-systemarkitektur  
- **Endringshåndtering**: Formelle prosesser for sikkerhetsgjennomgang av AI-systemendringer  

Disse grunnleggende praksisene skaper et robust sikkerhetsgrunnlag som forbedrer effektiviteten til MCP-spesifikke sikkerhetskontroller og gir omfattende beskyttelse for AI-drevne applikasjoner.  

## Viktige sikkerhetskonklusjoner

- **Lagvis sikkerhetstilnærming**: Kombiner grunnleggende sikkerhetspraksiser (sikker koding, minste privilegium, leverandørkjedeverifisering, kontinuerlig overvåking) med AI-spesifikke kontroller for omfattende beskyttelse  

- **AI-spesifikt trussellandskap**: MCP-systemer står overfor unike risikoer inkludert prompt-injeksjon, verktøyforgiftning, øktkapring, forvirret stedfortreder-problemer, token-gjennomgangssårbarheter og overdrevne tillatelser som krever spesialiserte avbøtninger  

- **Autentisering og autorisasjon i verdensklasse**: Implementer robust autentisering med eksterne identitetsleverandører (Microsoft Entra ID), håndhev riktig tokenvalidering, og aksepter aldri token som ikke eksplisitt er utstedt for din MCP-server  

- **Forebygging av AI-angrep**: Distribuer Microsoft Prompt Shields og Azure Content Safety for å forsvare mot indirekte prompt-injeksjon og verktøyforgiftning, samtidig som du validerer verktøymetadata og overvåker dynamiske endringer  

- **Økt- og transportsikkerhet**: Bruk kryptografisk sikre, ikke-deterministiske økt-IDer bundet til brukeridentiteter, implementer riktig håndtering av øktens livssyklus, og bruk aldri økter for autentisering  

- **OAuth-sikkerhetsbeste praksis**: Forhindre forvirret stedfortreder-angrep gjennom eksplisitt brukersamtykke for dynamisk registrerte klienter, korrekt OAuth 2.1-implementering med PKCE, og streng validering av redirect-URIer  

- **Token-sikkerhetsprinsipper**: Unngå token-gjennomgangs-anti-mønstre, valider tokenets audience-krav, implementer kortlivede token med sikker rotasjon, og oppretthold klare tillitsgrenser  

- **Omfattende leverandørkjede-sikkerhet**: Behandle alle AI-økosystemkomponenter (modeller, embeddings, kontekstleverandører, eksterne APIer) med samme sikkerhetsnivå som tradisjonelle programvareavhengigheter  

- **Kontinuerlig utvikling**: Hold deg oppdatert med raskt utviklende MCP-spesifikasjoner, bidra til sikkerhetsfellesskapets standarder, og oppretthold adaptive sikkerhetsposisjoner etter hvert som protokollen modnes  

- **Microsoft sikkerhetsintegrasjon**: Utnytt Microsofts omfattende sikkerhetsekosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) for forbedret beskyttelse ved MCP-distribusjon  

## Omfattende ressurser

### **Offisiell MCP-sikkerhetsdokumentasjon**  
- [MCP-spesifikasjon (Gjeldende: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP sikkerhetsbeste praksis](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP autorisasjonsspesifikasjon](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [MCP GitHub-repositorium](https://github.com/modelcontextprotocol)  

### **Sikkerhetsstandarder og beste praksis**  
- [OAuth 2.0 sikkerhetsbeste praksis (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 webapplikasjonssikkerhet](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 for store språkmodeller](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft Digital Defense Report](https://aka.ms/mddr)  

### **AI-sikkerhetsforskning og analyse**  
- [Prompt-injeksjon i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Verktøyforgiftning-angrep (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Sikkerhetsforskningsbriefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Sikkerhetsløsninger**
- [Microsoft Prompt Shields Dokumentasjon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Sikkerhet](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Beste Praksis](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Avansert Sikkerhet](https://github.com/security/advanced-security)

### **Implementeringsguider & Veiledninger**
- [Azure API Management som MCP Autentiseringsgateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Autentisering med MCP Servere](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Sikker Tokenlagring og Kryptering (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Leverandørkjede Sikkerhet**
- [Azure DevOps Sikkerhet](https://azure.microsoft.com/products/devops)
- [Azure Repos Sikkerhet](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Leverandørkjede Sikkerhetsreise](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Ytterligere Sikkerhetsdokumentasjon**

For omfattende sikkerhetsveiledning, se disse spesialiserte dokumentene i denne seksjonen:

- **[MCP Sikkerhets Beste Praksis 2025](./mcp-security-best-practices-2025.md)** - Fullstendige sikkerhets beste praksiser for MCP-implementeringer
- **[Azure Content Safety Implementering](./azure-content-safety-implementation.md)** - Praktiske implementeringseksempler for Azure Content Safety-integrasjon  
- **[MCP Sikkerhetskontroller 2025](./mcp-security-controls-2025.md)** - Nyeste sikkerhetskontroller og teknikker for MCP-distribusjoner
- **[MCP Beste Praksis Hurtigreferanse](./mcp-best-practices.md)** - Hurtigreferanseguide for essensielle MCP sikkerhetspraksiser

---

## Hva er Neste

Neste: [Kapittel 3: Komme i Gang](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->