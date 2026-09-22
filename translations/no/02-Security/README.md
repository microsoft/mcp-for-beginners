# MCP-sikkerhet: Omfattende beskyttelse for AI-systemer

[![MCP Security Best Practices](../../../translated_images/no/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klikk på bildet ovenfor for å se video av denne leksjonen)_

Sikkerhet er grunnleggende for design av AI-systemer, og derfor prioriterer vi det som vår andre seksjon. Dette samsvarer med Microsofts prinsipp **Secure by Design** fra [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) gir kraftige nye muligheter for AI-drevne applikasjoner samtidig som det introduserer unike sikkerhetsutfordringer som går utover tradisjonelle programvarerisikoer. MCP-systemer står overfor både etablerte sikkerhetsbekymringer (sikker koding, minste privilegium, leverandørkjede-sikkerhet) og nye AI-spesifikke trusler inkludert prompt-injeksjon, verktøyforgiftning, sesjonskapring, confused deputy-angrep, token forwarding-sårbarheter og dynamisk endring av kapasiteter.

Denne leksjonen utforsker de mest kritiske sikkerhetsrisikoene i MCP-implementasjoner—inkludert autentisering, autorisasjon, overdrevne tillatelser, indirekte prompt-injeksjon, sesjonssikkerhet, confused deputy-problemer, token-administrasjon og leverandørkjede-sårbarheter. Du vil lære om konkrete kontroller og beste praksis for å redusere disse risikoene samtidig som du bruker Microsoft-løsninger som Prompt Shields, Azure Content Safety og GitHub Advanced Security for å styrke din MCP-distribusjon.

## Læringsmål

Etter denne leksjonen skal du kunne:

- **Identifisere MCP-spesifikke trusler**: Gjenkjenne unike sikkerhetsrisikoer i MCP-systemer inkludert prompt-injeksjon, verktøyforgiftning, overdrevne tillatelser, sesjonskapring, confused deputy-problemer, token forwarding-sårbarheter og leverandørkjedetrusler
- **Anvende sikkerhetskontroller**: Implementere effektive tiltak inkludert robust autentisering, minste privilegium-tilgang, sikker token-administrasjon, sesjonssikkerhetskontroller og verifisering av leverandørkjeden
- **Utnytte Microsoft-sikkerhetsløsninger**: Forstå og implementere Microsoft Prompt Shields, Azure Content Safety og GitHub Advanced Security for beskyttelse av MCP-arbeidsbelastninger
- **Validere verktøysikkerhet**: Forstå viktigheten av validering av verktøymetadata, overvåking av dynamiske endringer og forsvar mot indirekte prompt-injeksjonsangrep
- **Integrere beste praksis**: Kombinere etablerte sikkerhetsfundamenter (sikker koding, serverherding, zero trust) med MCP-spesifikke kontroller for omfattende beskyttelse

# MCP-sikkerhetsarkitektur og kontroller

Moderne MCP-implementasjoner krever lagdelte sikkerhetstilnærminger som adresserer både tradisjonell programvaresikkerhet og AI-spesifikke trusler. Den raskt utviklende MCP-spesifikasjonen modnes kontinuerlig med sine sikkerhetskontroller, noe som muliggjør bedre integrasjon med virksomhetens sikkerhetsarkitektur og etablerte beste praksiser.

Forskning fra [Microsoft Digital Defense Report](https://aka.ms/mddr) viser at **98 % av rapporterte brudd kunne vært forhindret med robust sikkerhetshygiene**. Den mest effektive beskyttelsesstrategien kombinerer grunnleggende sikkerhetsrutiner med MCP-spesifikke kontroller—dokumenterte basis sikkerhetstiltak er fortsatt mest effektive for å redusere samlet sikkerhetsrisiko.

## Nåværende sikkerhetslandskap

> **Merk:** Dette kapittelet kombinerer etablerte MCP-sikkerhetskontroller med den
> nåværende **MCP Specification 2026-07-28** autorisasjonsveiledningen. Referer alltid
> til den gjeldende [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub-repositoriet](https://github.com/modelcontextprotocol), og
> [dokumentasjonen for sikkerhetsbeste praksiser](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> når du implementerer sikkerhetskritisk kode.

> **Oppdatering i autorisasjon:** MCP `2026-07-28` krever at klienter validerer
> `iss`-parameteren i autorisasjonssvar (RFC 9207) og binder registrerte
> legitimasjoner til utstedende autorisasjonsserver. Dynamisk klientregistrering
> er utfaset; nye implementasjoner bør bruke Client ID Metadata Documents.
> Se [Hva som er endret i MCP: Spesifikasjonen 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> for fullstendig liste over autorisasjonsendringer.

## 🏔️ MCP Security Summit Workshop (Sherpa)

For **praktisk sikkerhetstrening** anbefaler vi sterkt **MCP Security Summit Workshop** (Sherpa) – en omfattende guidet ekspedisjon for å sikre MCP-servere i Microsoft Azure.

### Workshop-oversikt

[MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) tilbyr praktisk, håndgripelig sikkerhetstrening gjennom en dokumentert "sårbar → utnytt → fiks → valider"-metodikk. Du vil:

- **Lære ved å bryte ting**: Opplev sårbarheter på egen hånd ved å utnytte tilsiktet usikre servere
- **Bruke Azure-innfødte sikkerhetsløsninger**: Utnytte Azure Entra ID, Key Vault, API Management og AI Content Safety
- **Følge forsvar-i-dybden-prinsippet**: Bygge opp omfattende sikkerhetslag gjennom leire
- **Anvende OWASP-standarder**: Hver teknikk knyttes til [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Få produksjonsklar kode**: Gå bort med fungerende, testede implementasjoner

### Ekspedisjonsruten

| Leir | Fokus | Dekkede OWASP-risikoer |
|------|-------|---------------------|
| **Basecamp** | MCP-grunnleggende & autentiseringssårbarheter | MCP01, MCP07 |
| **Leir 1: Identitet** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Leir 2: Gateway** | API Management, private endepunkter, styring | MCP02, MCP06, MCP07, MCP09 |
| **Leir 3: I/O-sikkerhet** | Prompt-injeksjon, beskyttelse av PII, innholdssikkerhet | MCP03, MCP05, MCP06, MCP10 |
| **Leir 4: Overvåking** | Logganalyse, dashboards, trusseldeteksjon | MCP04, MCP08 |
| **Toppen** | Red Team / Blue Team integrasjonstest | Alle |

**Kom i gang**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Topp 10 sikkerhetsrisikoer

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) beskriver de ti mest kritiske sikkerhetsrisikoene for MCP-implementasjoner:

| Risiko | Beskrivelse | Azure-mitigasjon |
|------|-------------|------------------|
| **MCP01** | Feil i tokenhåndtering og lekkasje av hemmeligheter | Azure Key Vault, Managed Identity |
| **MCP02** | Eskalering av privilegier via Scope Creep | RBAC, betinget tilgang |
| **MCP03** | Verktøyforgiftning | Validering av verktøy, integritetskontroll |
| **MCP04** | Angrep på programvareleverandørkjede og manipulering av avhengigheter | GitHub Advanced Security, avhengighetsskanning |
| **MCP05** | Kommando-injeksjon og utførelse | Input-validering, sandboxing |
| **MCP06** | Underminering av intensjonsflyt | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Utilstrekkelig autentisering og autorisasjon | Azure Entra ID, OAuth 2.1 med PKCE |
| **MCP08** | Manglende revisjon og telemetri | Azure Monitor, Application Insights |
| **MCP09** | Skygge-MCP-servere | API-senterstyring, nettverksisolasjon |
| **MCP10** | Context Injection & Over-Sharing | Dataklassifisering, minimal eksponering |

### Utvikling av MCP-autentisering

MCP-spesifikasjonen har utviklet seg betydelig i sin tilnærming til autentisering og autorisasjon:

- **Opprinnelig tilnærming**: Tidlige spesifikasjoner krevde at utviklere implementerte egendefinerte autentiseringsservere, hvor MCP-servere fungerte som OAuth 2.0-autoriseringservere som håndterte brukerautentisering direkte
- **Nåværende standard (`2026-07-28`)**: MCP-servere kan delegere autentisering
  til eksterne identitetsleverandører som Microsoft Entra ID. Klienter må også
  anvende gjeldende krav til validering av utsteder og binding av legitimasjon.
- **Transportlagsikkerhet**: Forbedret støtte for sikre transportmekanismer med riktige autentiseringsmønstre for både lokale (STDIO) og eksterne (streamable HTTP) tilkoblinger

## Autentiserings- og autorisasjonssikkerhet

### Nåværende sikkerhetsutfordringer

Moderne MCP-implementasjoner står overfor flere utfordringer innen autentisering og autorisasjon:

### Risikoer og trusselvektorer

- **Feilkonfigurert autorisasjonslogikk**: Feil i autorisasjonsimplementering i MCP-servere kan eksponere sensitive data og feilaktig anvende tilgangskontroller
- **Kompromittering av OAuth-token**: Tyveri av lokale MCP-token gjør at angripere kan utgi seg for å være servere og få tilgang til nedstrøms tjenester
- **Token forwarding-sårbarheter**: Feil håndtering av tokens åpner for omgåelse av sikkerhetskontroller og manglende ansvarsfraskrivelse
- **Overdrevne tillatelser**: MCP-servere med for høye privilegier bryter prinsippet om minste privilegium og utvider angrepsflater

#### Token forwarding: Et kritisk anti-mønster

**Token forwarding er uttrykkelig forbudt** i gjeldende MCP-autorisasjonsspesifikasjon på grunn av alvorlige sikkerhetsimplikasjoner:

##### Omgåelse av sikkerhetskontroller
- MCP-servere og nedstrøms-APIer implementerer kritiske sikkerhetskontroller (rate limiting, forespørselsvalidering, trafikkovervåking) som er avhengige av korrekt tokenvalidering
- Direkte klient-til-API token-bruk omgår disse essensielle beskyttelsene og undergraver sikkerhetsarkitekturen

##### Ansvars- og revisjonsutfordringer  
- MCP-servere klarer ikke å skille mellom klienter som bruker tokens utstedt oppstrøms, noe som ødelegger revisjonsspor
- Nedstrøms ressursserver-logger viser misvisende forespørselsopprinnelser i stedet for faktiske MCP-server-mellomledd
- Hendelsesundersøkelser og samsvarsgjennomganger blir betydelig vanskeligere

##### Risiko for datautvinning
- Uvaliderte tokenpåstander gjør at ondsinnede aktører med stjålne tokens kan bruke MCP-servere som proxyer for datautvinning
- Tillitsbrudd i sikkerhetsgrensene tillater uautorisert tilgang som omgår tiltenkte sikkerhetskontroller

##### Multi-tjeneste angrepsvektorer
- Kompromitterte tokens akseptert av flere tjenester muliggjør lateral bevegelse på tvers av tilkoblede systemer
- Tillitsantagelser mellom tjenester kan brytes når tokenopprinnelse ikke kan verifiseres

### Sikkerhetskontroller og mitigeringer

**Kritiske sikkerhetskrav:**

> **OBLIGATORISK**: MCP-servere **MÅ IKKE** akseptere tokens som ikke eksplisitt er utstedt for MCP-serveren

#### Autentiserings- og autorisasjonskontroller

- **Nøye autorisasjonsgjennomgang**: Utfør omfattende revisjoner av MCP-serverens autorisasjonslogikk for å sikre at bare tilsiktede brukere og klienter får tilgang til sensitive ressurser
  - **Implementasjonsveiledning**: [Azure API Management som autentiseringsgateway for MCP-servere](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitetsintegrasjon**: [Bruke Microsoft Entra ID for MCP-serverautentisering](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Sikker token-administrasjon**: Implementer [Microsofts beste praksis for tokenvalidering og livssyklus](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Valider at tokenets målgruppe stemmer overens med MCP-serverens identitet
  - Implementer korrekt tokenrotasjon og utløpspolicy
  - Forhindre token-gjenspill og uautorisert bruk

- **Beskyttet token-lagring**: Sikre tokenlagring med kryptering både i ro og under overføring
  - **Beste praksis**: [Retningslinjer for sikker tokenlagring og kryptering](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Tilgangskontrollimplementasjon

- **Prinsippet om minste privilegium**: Gi MCP-servere kun nødvendige tillatelser som trengs for tilsiktet funksjonalitet
  - Regelmessige gjennomganger og oppdateringer av tillatelser for å hindre privilegie-eskalering
  - **Microsoft-dokumentasjon**: [Sikker tilgang med minste privilegium](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollestyrt tilgangskontroll (RBAC)**: Implementer finmaskede rolleoppgaver
  - Avgrens roller til spesifikke ressurser og handlinger
  - Unngå brede eller unødvendige tillatelser som utvider angrepsflater

- **Kontinuerlig overvåking av tillatelser**: Implementer løpende revisjon og overvåking av tilgang
  - Overvåk mønstre i tillatelsesbruk for anomalier
  - Raskt korriger overdrevne eller ubrukte privilegier

## AI-spesifikke sikkerhetstrusler

### Prompt-injeksjon og angrep på verktøymanipulering

Moderne MCP-implementasjoner møter sofistikerte AI-spesifikke angrepsvektorer som tradisjonelle sikkerhetstiltak ikke fullt ut kan adressere:

#### **Indirekte prompt-injeksjon (tverrdomenes prompt-injeksjon)**

**Indirekte prompt-injeksjon** utgjør en av de mest kritiske sårbarhetene i AI-systemer med MCP. Angripere skjuler ondsinnede instruksjoner i eksternt innhold—dokumenter, nettsider, e-poster eller datakilder—som AI-systemene deretter behandler som legitime kommandoer.

**Angrepsscenarioer:**
- **Dokumentbasert injeksjon**: Ondsinnede instruksjoner skjult i prosesserte dokumenter som utløser utilsiktede AI-handlinger
- **Utnyttelse av webinnhold**: Kompromitterte nettsider med innebygde prompt som manipulerer AI-adferd ved innhenting
- **E-postbaserte angrep**: Ondsinnede prompt i e-poster som får AI-assistenter til å lekke informasjon eller utføre uautoriserte handlinger
- **Forurensning av datakilder**: Kompromitterte databaser eller APIer som tjener forurenset innhold til AI-systemer

**Reell påvirkning**: Disse angrepene kan føre til datautvinning, personvernbrudd, generering av skadelig innhold og manipulering av brukerinteraksjoner. For detaljert analyse, se [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/no/prompt-injection.ed9fbfde297ca877.webp)

#### **Verktøyforgiftning-angrep**

**Verktøyforgiftning** retter seg mot metadata som definerer MCP-verktøy, og utnytter hvordan LLM-er tolker verktøybeskrivelser og parametere for å ta beslutninger om utførelse.

**Angrepsmekanismer:**
- **Manipulering av metadata**: Angripere injiserer ondsinnede instruksjoner i verktøybeskrivelser, parameterdefinisjoner eller brukseksempler
- **Usynlige instruksjoner**: Skjulte prompt i verktøymetadata som behandles av AI-modeller men er usynlige for menneskelige brukere
- **Dynamiske verktøyendringer ("Rug Pulls")**: Verktøy godkjent av brukere blir senere endret for å utføre skadelige handlinger uten brukerens viten
- **Parameterinjeksjon**: Ondsinnet innhold innebygd i verktøyparameter-skjemaer som påvirker modellens oppførsel


**Risiko ved hostede servere**: Fjernstyrte MCP-servere utgjør forhøyede risikoer ettersom verktøydefinisjoner kan oppdateres etter første godkjenning av brukeren, noe som kan skape situasjoner hvor tidligere sikre verktøy blir ondsinnede. For en omfattende analyse, se [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Verktøyinnsprøytingsangrep Diagram](../../../translated_images/no/tool-injection.3b0b4a6b24de6bef.webp)

#### **Ytterligere AI-angrepsvektorer**

- **Tverrdomenepromptinnsprøyting (XPIA)**: Sofistikerte angrep som utnytter innhold fra flere domener for å omgå sikkerhetskontroller
- **Dynamisk endring av kapasiteter**: Sanntidsendringer i verktøysfunksjoner som unngår innledende sikkerhetsvurderinger
- **Konstekstvindu-forgiftning**: Angrep som manipulerer store kontekstvinduer for å skjule ondsinnede instruksjoner
- **Modellforvirringsangrep**: Utnyttelse av modellbegrensninger for å skape uforutsigbare eller usikre atferder


### Påvirkning av AI-sikkerhetsrisiko

**Konsekvenser med høy påvirkning:**
- **Dataeksfiltrasjon**: Uautorisert tilgang og tyveri av sensitiv bedrifts- eller persondata
- **Personvernbrudd**: Eksponering av personlig identifiserbar informasjon (PII) og konfidensielle forretningsdata  
- **Systemmanipulasjon**: Utilsiktede endringer i kritiske systemer og arbeidsflyter
- **Tyveri av legitimasjon**: Kompromittering av autentiseringstokener og tjenestekredentialer
- **Laterale bevegelser**: Bruk av kompromitterte AI-systemer som pivotpunkter for bredere nettverksangrep

### Microsoft AI-sikkerhetsløsninger

#### **AI Prompt Shields: Avansert beskyttelse mot innsprøytingsangrep**

Microsoft **AI Prompt Shields** gir omfattende forsvar mot både direkte og indirekte promptinnsprøytingsangrep gjennom flere sikkerhetslag:

##### **Kjernebeskyttelsesmekanismer:**

1. **Avansert deteksjon og filtrering**
   - Maskinlæringsalgoritmer og NLP-teknikker oppdager ondsinnede instruksjoner i ekstern innhold
   - Sanntidsanalyse av dokumenter, nettsider, e-poster og datakilder for innebygde trusler
   - Kontekstuell forståelse av legitime vs. ondsinnede promptmønstre

2. **Spotlighting-teknikker**  
   - Skiller mellom pålitelige systeminstruksjoner og potensielt kompromitterte eksterne input
   - Teksttransformasjonsmetoder som øker modellrelevans samtidig som ondsinnet innhold isoleres
   - Hjelper AI-systemer med å opprettholde riktig instruksjonshierarki og ignorere innsatte kommandoer

3. **Avgrensnings- og datamerkesystemer**
   - Eksplisitt grensedefinisjon mellom pålitelige systemmeldinger og ekstern inputtekst
   - Spesielle markører fremhever grenser mellom pålitelige og upålitelige datakilder
   - Klart skille hindrer instruksjonsforvirring og uautorisert kommandoeksekvering

4. **Kontinuerlig trusselintelligens**
   - Microsoft overvåker kontinuerlig nye angrepsmønstre og oppdaterer forsvaret
   - Proaktiv trusseljakt for nye innsprøytingsteknikker og angrepsvektorer
   - Regelmessige oppdateringer av sikkerhetsmodeller for å opprettholde effektivitet mot utviklende trusler

5. **Integrasjon med Azure Content Safety**
   - Del av den omfattende Azure AI Content Safety-pakken
   - Ytterligere deteksjon for jailbreak-forsøk, skadelig innhold og sikkerhetspolicybrudd
   - Enhetlige sikkerhetskontroller på tvers av AI-applikasjonskomponenter

**Implementeringsressurser**: [Microsoft Prompt Shields Dokumentasjon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Beskyttelse](../../../translated_images/no/prompt-shield.ff5b95be76e9c78c.webp)


## Avanserte MCP-sikkerhetstrusler

### Sårbarheter for overtakelse av sesjoner

**Sesjonshijacking** representerer en kritisk angrepsvektor i tilstandsfulle MCP-implementeringer hvor uautoriserte parter skaffer og misbruker legitime sesjonsidentifikatorer for å utgi seg for klienter og utføre uautoriserte handlinger.

#### **Angrepsscenarioer og risikoer**

- **Sesjonshijack promptinnsprøyting**: Angripere med stjålne sesjons-IDer sprøyter inn ondsinnede hendelser i servere som deler sesjonsstatus, noe som potensielt utløser skadelige handlinger eller gir tilgang til sensitiv data
- **Direkte utgi seg for andre**: Stjålne sesjons-IDer muliggjør direkte MCP-serverkall som omgår autentisering og behandler angripere som legitime brukere
- **Kompromitterte gjenopptakbare strømmer**: Angripere kan avslutte forespørsler for tidlig, noe som får legitime klienter til å gjenoppta med potensielt ondsinnelig innhold

#### **Sikkerhetskontroller for sesjonshåndtering**

**Kritiske krav:**
- **Autorisasjonsverifisering**: MCP-servere som implementerer autorisasjon **MÅ** verifisere ALLE innkommende forespørsler og **MÅ IKKE** stole på sesjoner for autentisering
- **Sikker sesjonsgenerering**: Bruk kryptografisk sikre, ikke-deterministiske sesjons-IDer generert med sikre tilfeldige tallgeneratorer
- **Brukerspesifikk binding**: Bind sesjons-IDer til brukerspesifikk informasjon ved bruk av formater som `<user_id>:<session_id>` for å forhindre misbruk på tvers av brukere
- **Livssyklushåndtering for sesjoner**: Implementer korrekt utløp, rotasjon og ugyldiggjøring for å begrense sårbarhetsvinduene
- **Transport-sikkerhet**: Obligatorisk HTTPS for all kommunikasjon for å forhindre avlytting av sesjons-ID

### Problemet med forvirret fullmektig

**Problemet med forvirret fullmektig** oppstår når MCP-servere fungerer som autentiseringsmeglere mellom klienter og tredjepartstjenester, noe som skaper muligheter for autorisasjonsomgåelse gjennom utnyttelse av statiske klient-IDer.

#### **Angrepsmekanikk og risikoer**

- **Omgåelse av samtykke basert på informasjonskapsler**: Tidligere brukergodkjenning skaper samtykkekaker som angripere utnytter gjennom ondsinnede autorisasjonsforespørsler med spesiallagde videresendings-URIer
- **Tyveri av autorisasjonskode**: Eksisterende samtykkekaker kan føre til at autorisasjonsservere hopper over samtykkeskjermer og videresender koder til angriperkontrollerte endepunkter  
- **Uautorisert API-tilgang**: Stjålne autorisasjonskoder muliggjør tokenutveksling og utgi seg for bruker uten eksplisitt godkjenning

#### **Avbøtende strategier**

**Obligatoriske kontroller:**
- **Eksplisitte samtykkekrav**: MCP-proxyservere som bruker statiske klient-IDer **MÅ** innhente brukersamtykke for hver dynamisk registrert klient
- **OAuth 2.1 sikkerhetsimplementering**: Følg gjeldende beste praksis for OAuth-sikkerhet, inkludert PKCE (Proof Key for Code Exchange) for alle autorisasjonsforespørsler
- **Streng klientvalidering**: Implementer streng validering av videresendings-URIer og klientidentifikatorer for å forhindre utnyttelse

### Sårbarheter ved token-gjennomføring  

**Token-gjennomføring** representerer et eksplisitt anti-mønster der MCP-servere aksepterer klienttoken uten skikkelig validering og videresender dem til nedstrøms APIer, noe som bryter med MCPs autorisasjonsspesifikasjoner.

#### **Sikkerhetsimplikasjoner**

- **Omgåelse av kontroll**: Direkte tokenbruk klient-til-API omgår kritiske begrensninger, validering og overvåkingskontroller
- **Korrupsjon av revisjonsspor**: Opprinnelig utstedte token gjør klientidentifisering umulig og bryter etterforskningsmuligheter ved hendelser
- **Proxy-basert dataeksfiltrasjon**: Uvaliderte token gir ondsinnede aktører mulighet til å bruke servere som proxy for uautorisert dataadgang
- **Brudd på tillitsgrenser**: Nedstrøms tjenesters tillitsantagelser kan brytes når token-opprinnelse ikke kan bekreftes
- **Utvidelse av angrep på tvers av tjenester**: Kompromitterte token akseptert i flere tjenester muliggjør laterale bevegelser

#### **Påkrevde sikkerhetskontroller**

**Ikke-forhandlingsbare krav:**
- **Token-validering**: MCP-servere **MÅ IKKE** akseptere token som ikke er eksplisitt utstedt for MCP-serveren
- **Publikumsverifisering**: Alltid valider at token-publikumsclaims samsvarer med MCP-serverens identitet
- **Korrekt token-livssyklus**: Implementer kortvarige tilgangstoken med sikre rotasjonsrutiner


## Sikkerhet i leverandørkjeden for AI-systemer

Sikkerhet i leverandørkjeden har utviklet seg utover tradisjonelle programvaredelag avhengigheter for å omfatte hele AI-økosystemet. Moderne MCP-implementeringer må grundig verifisere og overvåke alle AI-relaterte komponenter, da hver av dem introduserer potensielle sårbarheter som kan kompromittere systemets integritet.

### Utvidede AI-leverandørkjede-komponenter

**Tradisjonelle programvareavhengigheter:**
- Åpen kildekode-biblioteker og rammeverk
- Containerbilder og grunnleggende systemer  
- Utviklingsverktøy og byggeprosesser
- Infrastrukturkomponenter og tjenester

**AI-spesifikke leverandørkjedeelementer:**
- **Fundamentmodeller**: Fortrente modeller fra ulike leverandører som krever proveniensverifisering
- **Embedding-tjenester**: Eksterne vektorisering- og semantiske søketjenester
- **Kontekstleverandører**: Datakilder, kunnskapsbaser og dokumentsamlinger  
- **Tredjeparts-APIer**: Eksterne AI-tjenester, maskinlæringspipelines og dataprosesseringsendepunkter
- **Modellartefakter**: Vekter, konfigurasjoner og finjusterte modellvarianter
- **Treningsdatasett**: Datasett brukt til modelltrening og finjustering

### Omfattende leverandørkjedesikkerhetsstrategi

#### **Komponentverifisering og tillit**
- **Proveniensvalidering**: Verifiser opprinnelse, lisensiering og integritet for alle AI-komponenter før integrasjon
- **Sikkerhetsvurdering**: Gjennomfør sårbarhetsskanninger og sikkerhetsgjennomganger for modeller, datakilder og AI-tjenester
- **Omdømmeanalyse**: Evaluer sikkerhetshistorikk og praksis til AI-tjenesteleverandører
- **Overholdelsesverifisering**: Sikre at alle komponenter oppfyller organisasjonens sikkerhets- og regulatoriske krav

#### **Sikre distribusjonspipelines**  
- **Automatisert CI/CD-sikkerhet**: Integrer sikkerhetsskanning gjennom automatiserte distribusjonspipelines
- **Integritetsverifisering av artefakter**: Implementer kryptografisk verifisering for alle distribuerte artefakter (kode, modeller, konfigurasjoner)
- **Trinnvis distribusjon**: Bruk progressive distribusjonsstrategier med sikkerhetsvalidering på hvert trinn
- **Pålitelige artefaktregistere**: Distribuer kun fra verifiserte, sikre artefaktregistre og depoter

#### **Kontinuerlig overvåking og respons**
- **Avhengighetsskanning**: Pågående sårbarhetsovervåking for all programvare- og AI-komponentavhengighet
- **Modellovervåking**: Kontinuerlig vurdering av modellatferd, ytelsesavvik og sikkerhetsanomalier
- **Tjenestehelseovervåking**: Overvåk eksterne AI-tjenester for tilgjengelighet, sikkerhetshendelser og policyendringer
- **Integrasjon av trusselintelligens**: Inkluder trusselfeeder spesifikt rettet mot AI- og ML-sikkerhetsrisikoer

#### **Tilgangskontroll og minste privilegier**
- **Komponentnivåtillatelser**: Begrens tilgang til modeller, data og tjenester basert på forretningsbehov
- **Håndtering av tjenestekontoer**: Implementer dedikerte tjenestekontoer med minimale nødvendige tillatelser
- **Nettverkssegmentering**: Isoler AI-komponenter og begrens nettverkstilgang mellom tjenester
- **API-gateway-kontroller**: Bruk sentraliserte API-gatewayer for å kontrollere og overvåke tilgang til eksterne AI-tjenester

#### **Hendelseshåndtering og gjenoppretting**
- **Raske responsprosedyrer**: Etablerte prosesser for patching eller erstatning av kompromitterte AI-komponenter
- **Rotasjon av legitimasjon**: Automatiserte systemer for rotasjon av hemmeligheter, API-nøkler og tjenestekredentialer
- **Rull tilbake-muligheter**: Evne til raskt å gå tilbake til tidligere kjente gode versjoner av AI-komponenter
- **Gjenoppretting ved leverandørkjede-brudd**: Spesifikke prosedyrer for å håndtere kompromittering av oppstrøms AI-tjenester

### Microsoft sikkerhetsverktøy og integrasjon

**GitHub Advanced Security** gir omfattende leverandørkjede-beskyttelse inkludert:
- **Hemmelighetsskanning**: Automatisert oppdagelse av legitimasjon, API-nøkler og token i depoter
- **Avhengighetsskanning**: Sårbarhetsvurdering for åpen kildekode-avhengigheter og biblioteker
- **CodeQL-analyse**: Statisk kodeanalyse for sikkerhetssårbarheter og kodeproblemer
- **Leverandørkjedeinnsikt**: Innsikt i avhengighetshelse og sikkerhetstatus

**Integrasjon med Azure DevOps & Azure Repos:**
- Sømløs sikkerhetsskanning på tvers av Microsofts utviklingsplattformer
- Automatiserte sikkerhetssjekker i Azure Pipelines for AI-arbeidsmengder
- Policyhåndheving for sikker distribusjon av AI-komponenter

**Microsofts interne praksiser:**
Microsoft implementerer omfattende sikkerhetsrutiner i leverandørkjeden på tvers av alle produkter. Les mer om beprøvde tilnærminger i [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Beste praksis for grunnleggende sikkerhet

MCP-implementeringer arver og bygger videre på organisasjonens eksisterende sikkerhetsnivå. Styrking av grunnleggende sikkerhetsrutiner forbedrer betydelig den samlede sikkerheten til AI-systemer og MCP-distribusjoner.

### Kjerneprinsipper for sikkerhet

#### **Sikre utviklingsrutiner**
- **OWASP-samsvar**: Beskytt mot [OWASP Top 10](https://owasp.org/www-project-top-ten/) nettapplikasjonssårbarheter
- **AI-spesifikke beskyttelser**: Implementer kontroller for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Sikker hemmelighetshåndtering**: Bruk dedikerte hvulster for token, API-nøkler og sensitiv konfigurasjonsdata
- **Ende-til-ende-kryptering**: Implementer sikret kommunikasjon gjennom alle applikasjonskomponenter og datastrømmer
- **Inputvalidering**: Grundig validering av alle brukerinput, API-parametere og datakilder

#### **Infrastrukturherding**
- **Flerfaktorautentisering**: Obligatorisk MFA for alle administrative og tjenestekontoer
- **Patchhåndtering**: Automatisert, tidsriktig patching for operativsystemer, rammeverk og avhengigheter  
- **Integrasjon med identitetsleverandør**: Sentralisert identitetshåndtering via bedriftsidentitetsleverandører (Microsoft Entra ID, Active Directory)
- **Nettverkssegmentering**: Logisk isolasjon av MCP-komponenter for å begrense laterale bevegelser
- **Prinsippet om minste privilegium**: Minimalt nødvendige tillatelser for alle systemkomponenter og kontoer

#### **Sikkerhetsovervåking og deteksjon**
- **Omfattende logging**: Detaljert logging av AI-applikasjonsaktiviteter, inkludert MCP klient-server-interaksjoner
- **SIEM-integrasjon**: Sentralisert sikkerhetsinformasjon og hendelseshåndtering for anomali-deteksjon
- **Atferdsanalyse**: AI-drevet overvåking for å oppdage uvanlige mønstre i system- og brukeratferd
- **Trusselintelligens**: Integrasjon av eksterne trusselfeedere og kompromissindikatorer (IOC-er)
- **Hendelseshåndtering**: Veldefinerte prosedyrer for påvisning, respons og gjenoppretting ved sikkerhetshendelser

#### **Zero Trust-arkitektur**
- **Aldri stol, verifiser alltid**: Kontinuerlig verifisering av brukere, enheter og nettverkstilkoblinger
- **Mikrosegmentering**: Granulære nettverkskontroller som isolerer individuelle arbeidsbelastninger og tjenester
- **Identitetssentrert sikkerhet**: Sikkerhetspolicyer basert på verifiserte identiteter i stedet for nettverkslokasjon
- **Kontinuerlig risikovurdering**: Dynamisk vurdering av sikkerhetsnivå basert på nåværende kontekst og atferd
- **Betinget tilgang**: Tilgangskontroller som tilpasses basert på risikofaktorer, lokasjon og enhetstillit

### Enterprise integrasjonsmønstre

#### **Integrasjon i Microsofts sikkerhetsekosystem**
- **Microsoft Defender for Cloud**: Omfattende skybasert sikkerhetsnivåhåndtering
- **Azure Sentinel**: Skybasert SIEM- og SOAR-funksjonalitet for beskyttelse av AI-arbeidsmengder
- **Microsoft Entra ID**: Bedriftsidentitets- og tilgangsstyring med betingede tilgangspolicyer
- **Azure Key Vault**: Sentralisert hemmelighetshåndtering med maskinvarenær sikkerhetsmodul (HSM)
- **Microsoft Purview**: Datastyring og samsvar for AI-datakilder og arbeidsflyter

#### **Samsvar og styring**
- **Regulatorisk tilpasning**: Sørg for at MCP-implementeringer oppfyller bransjespesifikke samsvarskrav (GDPR, HIPAA, SOC 2)

- **Dataklassifisering**: Korrekt kategorisering og håndtering av sensitiv data behandlet av AI-systemer
- **Revisjonsspor**: Omfattende logging for regulatorisk etterlevelse og rettsmedisinsk undersøkelse
- **Personvernkontroller**: Implementering av personvern som en del av designprinsipper i AI-systemarkitektur
- **Endringshåndtering**: Formelle prosesser for sikkerhetsgjennomganger av AI-systemendringer

Disse grunnleggende praksisene skaper en robust sikkerhetsstandard som forbedrer effektiviteten til MCP-spesifikke sikkerhetskontroller og gir omfattende beskyttelse for AI-drevne applikasjoner.

## Viktige sikkerhetsfunn

- **Lagvis sikkerhetstilnærming**: Kombiner grunnleggende sikkerhetspraksis (sikker koding, minste privilegium, forsyningskjedeverifisering, kontinuerlig overvåkning) med AI-spesifikke kontroller for omfattende beskyttelse

- **AI-spesifikt trussellandskap**: MCP-systemer står overfor unike risikoer inkludert promptinjektasjon, verktøyforgiftning, sesjonkapring, forvirret stedfortreder-problemer, token-gjennomgangssårbarheter og overdrevne tillatelser som krever spesialiserte tiltak

- **Autentisering og autorisasjonsdyktighet**: Implementer robust autentisering ved bruk av eksterne identitetsleverandører (Microsoft Entra ID), håndhev korrekt token-validering, og godtatt aldri tokens som ikke er eksplisitt utstedt for din MCP-server

- **Forebygging av AI-angrep**: Distribuer Microsoft Prompt Shields og Azure Content Safety for å forsvare mot indirekte promptinjektasjon og verktøyforgiftning, samtidig som du validerer verktøymetadata og overvåker dynamiske endringer

- **Sesjons- og transportssikkerhet**: Bruk kryptografisk sikre, ikke-deterministiske sesjons-IDer bundet til brukeridentiteter, implementer korrekt sesjonslivssyklusadministrasjon, og bruk aldri sesjoner til autentisering

- **Best practices for OAuth-sikkerhet**: Forhindre angrep via forvirret stedfortreder gjennom eksplisitt brukersamtykke for dynamisk registrerte klienter, korrekt implementering av OAuth 2.1 med PKCE, og streng validering av redirect URI  

- **Token-sikkerhetsprinsipper**: Unngå anti-mønstre som token-gjennomgang, valider token-audience-påstander, implementer kortlivede tokens med sikker rotasjon, og oppretthold klare tillitsgrenser

- **Omfattende sikkerhet i forsyningskjeden**: Behandle alle AI-økosystemkomponenter (modeller, embeddings, kontekstleverandører, eksterne API-er) med samme sikkerhetsskjerp som tradisjonelle programvareavhengigheter

- **Kontinuerlig utvikling**: Hold deg oppdatert med raskt utviklende MCP-spesifikasjoner, bidra til sikkerhetsfellesskapets standarder, og oppretthold adaptive sikkerhetsposisjoner etter hvert som protokollen modnes

- **Microsoft-sikkerhetsintegrasjon**: Utnytt Microsofts omfattende sikkerhetsekosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) for forbedret beskyttelse ved MCP-distribusjon

## Omfattende ressurser

### **Offisiell MCP-sikkerhetsdokumentasjon**
- [MCP-spesifikasjon (Nåværende: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP sikkerhets beste praksis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Autorisasjonsspesifikasjon](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **OWASP MCP sikkerhetsressurser**
- [OWASP MCP Azure sikkerhetsguide](https://microsoft.github.io/mcp-azure-security-guide/) - Omfattende OWASP MCP Top 10 med Azure implementeringsveiledning
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Offisielle OWASP MCP sikkerhetsrisikoer
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk sikkerhetstrening for MCP på Azure

### **Sikkerhetsstandarder og beste praksis**
- [OAuth 2.0 sikkerhets beste praksis (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 webapplikasjonssikkerhet](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for store språkmodeller](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **AI-sikkerhetsforskning og analyse**
- [Promptinjeksjon i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Verktøyforgiftningangrep (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP sikkerhetsforskningsbriefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft sikkerhetsløsninger**
- [Microsoft Prompt Shields dokumentasjon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety-tjeneste](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID sikkerhet](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Beste praksis for Azure tokenhåndtering](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementeringsguider og opplæringer**
- [Azure API Management som MCP-autentiseringsgateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentisering med MCP-servere](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Sikker tokenlagring og kryptering (video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps og sikkerhet i forsyningskjeden**
- [Azure DevOps sikkerhet](https://azure.microsoft.com/products/devops)
- [Azure Repos sikkerhet](https://azure.microsoft.com/products/devops/repos/)
- [Microsofts reise mot sikker programvareleverandørkjede](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Ytterligere sikkerhetsdokumentasjon**

For omfattende sikkerhetsveiledning, se disse spesialiserte dokumentene i denne seksjonen:

- **[CIMD og DCR Autorisasjonseksempel](./samples/cimd-dcr-auth/README.md)** - Kjørbar TypeScript MCP `2026-07-28` ressursserver som sammenligner foretrukne Client ID Metadata Documents med nedtrappet Dynamic Client Registration fallback
- **[MCP beste praksis for sikkerhet](./mcp-security-best-practices.md)** - Fullstendige sikkerhets beste praksiser for MCP-implementasjoner
- **[Implementering av Azure Content Safety](./azure-content-safety-implementation.md)** - Praktiske implementeringseksempler for integrering av Azure Content Safety  
- **[MCP sikkerhetskontroller](./mcp-security-controls.md)** - Nyeste sikkerhetskontroller og teknikker for MCP-distribusjoner
- **[MCP beste praksis referanse](./mcp-best-practices.md)** - Hurtigreferanse guide for essensielle MCP-sikkerhetspraksiser
- **[BlueHat 2026: Sikring av AI-ens fremtid: Sikring av MCP med dybdeforsvarsmønstre](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Dybdeforsvarsmønstre fra Microsoft Security Response Center (MSRC)

### **Praktisk sikkerhetstrening**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Omfattende praktisk workshop for sikring av MCP-servere i Azure med progressive leirer fra Base Camp til Summit
- **[OWASP MCP Azure sikkerhetsguide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referansearkitektur og implementeringsveiledning for alle OWASP MCP Top 10 risikoer

---

## Hva er neste

Neste: [Kapittel 3: Komme i gang](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->