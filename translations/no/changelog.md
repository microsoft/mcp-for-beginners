# Endringslogg: MCP for Beginners Curriculum

Dette dokumentet fungerer som en oversikt over alle betydelige endringer gjort i Model Context Protocol (MCP) for Beginners curriculum. Endringer dokumenteres i omvendt kronologisk rekkefølge (nyeste endringer først).

## 11. april 2026

### Ny leksjon, dokumentasjonsfikser og avhengighetsoppdateringer

#### Nytt læreinnhold lagt til

**Modul 05 - Avanserte emner**
- **Leksjon 5.17: Adversarial Multi-Agent Reasoning med MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattende guide som dekker det adversarielle debattmønsteret for multi-agent systemer
  - Mermaid arkitekturdiagram: to agenter → delt MCP-server → debatttranskripsjon → dommer → avgjørelse
  - Delt MCP verktøysserver (`web_search` + `run_python`) implementert i Python og TypeScript
  - Motstridende systemprompt (FOR / MOT / Dommer) med eksplisitte krav til verktøybruk
  - Debattorchestrator i Python, TypeScript og C# som styrer runder og ruting av argumenter
  - MCP `ClientSession`-kobling for orchestrator til ekte verktøysanrop
  - Brukstilfeldtabell (hallusinasjonsdeteksjon, trusselmodellering, API-designgjennomgang, faktasjekk, teknologivalg)
  - Sikkerhetshensyn: sandkasseutførelse, verktøysanropsvalidering, hastighetsbegrensning, revisjonslogging
  - Strukturert øvelse med tre praktiske scenarier (kodegjennomgang, arkitekturavgjørelse, innholdsmoderering)

#### Dokumentasjonsfikser

**Modul 03 - Komme i gang**
- **05-stdio-server/README.md**: Fikset ufullstendig TypeScript stdio-server eksempel — la til manglende transport-instansiering (`new StdioServerTransport()`) og `server.connect(transport)` kall for å samsvare med Python- og .NET-eksemplene i samme seksjon
- **14-sampling/README.md**: Fikset skrivefeil — rettet `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Oppdateringer i curriculum

**Hoved README.md**
- La til oppføring 5.17 (Adversarial Multi-Agent Reasoning med MCP) i curriculum-tabellen med direkte lenke til ny leksjon

**05-AdvancedTopics/README.md**
- La til rad for Leksjon 5.17 i leksjonstabellen

**study_guide.md**
- La til temaet Adversarial Multi-Agent Reasoning i tankekartet og prosabeskrivelsen for Avanserte Emner

#### Kode- og sikkerhetsfikser

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Sikkerhetsfikser — kommandoinjeksjon**: Erstattet `execSync` shell-interpolasjon med `execFile` + `promisify` i TypeScript `run_python` verktøyet, slik at kommandoinjeksjonsflaten elimineres (LLM-styrt kode sendes nå som et bokstavelig argv-element uten shell involvering)
- **MCP verktøysløyfe-kobling**: Oppdaterte Python debattorchestrator til å bruke `AsyncAnthropic` klient (erstatter blokkering av sync `Anthropic`), sende live `ClientSession` direkte til hver agenttur, hente verktøydefinisjoner via `session.list_tools()` hver tur, og sende `tool_use` blokker via `session.call_tool()` i en loop til modellen gir en endelig tekstrespons

#### Avhengighetsoppdateringer

- Oppgradert `hono` til 4.12.12 i flere pakker (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Oppgradert `@hono/node-server` fra 1.19.11 til 1.19.13 i TypeScript-pakker
- Oppgradert `cryptography` fra 46.0.5 til 46.0.7 i Python-pakker (10-StreamliningAIWorkflows lab 3 og 4)
- Oppgradert `lodash` fra 4.17.23 til 4.18.1 i 10-StreamliningAIWorkflows inspector

#### Oversettelser

- Synkroniserte oversettelser for 48+ språk med de siste kildeendringene (i18n oppdatering)

---

## 5. februar 2026

### Validering på tvers av depotet og navigasjonsforbedringer

#### Nytt læreinnhold lagt til

**Modul 03 - Komme i gang**
- **12-mcp-hosts/README.md**: Ny omfattende guide for oppsett av MCP-verter
  - Konfigurasjonseksempler for Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON konfigurasjonsmaler for alle viktige verter
  - Transporttypers sammenligningstabell (stdio, SSE/HTTP, WebSocket)
  - Feilsøking av vanlige tilkoblingsproblemer
  - Sikkerhetsanbefalinger for vertskonfigurasjon

- **13-mcp-inspector/README.md**: Ny feilsøkingsguide for MCP Inspector
  - Installasjonsmetoder (npx, global npm, fra kilde)
  - Tilkobling til servere via stdio og HTTP/SSE
  - Testverktøy, ressurser og prompt-arbeidsflyter
  - VS Code integrasjon med MCP Inspector
  - Vanlige feilsøkingsscenarier med løsninger

**Modul 04 - Praktisk implementering**
- **pagination/README.md**: Ny guidet innføring i implementering av paginering
  - Cursor-basert pagineringsmønstre i Python, TypeScript, Java
  - Håndtering av paginering på klientsiden
  - Strategier for cursor-design (ugjennomskinnelig vs strukturert)
  - Anbefalinger for ytelsesoptimalisering

**Modul 05 - Avanserte emner**
- **mcp-protocol-features/README.md**: Dypdykk i nye protokollfunksjoner
  - Fremdriftsvarsler implementering
  - Avbestillingsmønstre for forespørsler
  - Ressursmaler med URI-mønstre
  - Serverlivssyklusadministrasjon
  - Loggnivåkontroll
  - Feilhåndteringsmønstre med JSON-RPC-koder

#### Navigasjonsfikser (24+ filer oppdatert)

**Modulens hoved-READMEer**
 Nå linker de til både første leksjon OG neste modul

**02-Sikkerhets underfiler**
- Alle 5 supplerende sikkerhetsdokumenter har nå "Hva er neste"-navigasjon:

**09-CaseStudy filer**
- Alle kasusstudiefiler har nå sekvensiell navigasjon:

**10-StreamliningAI Labs**
La til "Hva er neste"-seksjon i Modul 10 oversikten og Modul 11

#### Kode- og innholdsrettelser

**SDK og avhengighetsoppdateringer**
Fikset tom åpenai versjon til `^4.95.0`
Oppgradert SDK fra `^1.8.0` til `>=1.26.0`
Oppdatert mcp versjonspinner til `>=1.26.0`

**Kodefikser**
Fikset ugyldig modell `gpt-4o-mini` til `gpt-4.1-mini`

**Innholdsrettelser**
Fikset ødelagt lenke `READMEmd` → `README.md`, fikset curriculum-tittel `Module 1-3` → `Module 0-3`, rettet sakssensitiv sti
Fjernet korrumpert duplikat Case Study 5-innhold

**Forbedringer i nybegynnerveiledning**
La til riktig introduksjon, læringsmål og forutsetninger for nybegynnere

#### Oppdateringer i curriculum

**Hoved README.md**
- La til oppføringer 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) i curriculum-tabellen

**Modul-READMEer**
La til leksjoner 12 og 13 i leksjonslisten
La til Praktiske guider-seksjon med pagineringslenke
La til leksjoner 5.15 (Custom Transport) og 5.16 (Protocol Features)

**study_guide.md**
- Oppdatert tankekart med alle nye temaer: MCP Hosts Oppsett, MCP Inspector, Paginatoringsstrategier, Dypdykk i Protokollfunksjoner

## 28. jan. 2026

### MCP-spesifikasjon 2025-11-25 samsvarsrevisjon

#### Forbedring av kjernekonsepter (01-CoreConcepts/)
- **Ny klient-primitive - Roots**: La til omfattende dokumentasjon om Roots klientprimitive som gjør at servere kan forstå filsystemgrenser og tilgangstillatelser
- **Verktøyanmerkninger**: La til dokumentasjon om verktøyadferdsanmerkninger (`readOnlyHint`, `destructiveHint`) for bedre verktøykjøringsbeslutninger
- **Verktøysanrop i Sampling**: Oppdatert Sampling-dokumentasjon til å inkludere `tools` og `toolChoice` parametere for modellstyrt verktøy-tilkalling under sampling-forespørsler
- **URL-modus elicitering**: La til dokumentasjon om URL-basert elicitering for serverinitiert ekstern webinteraksjon
- **Tasks (Eksperimentell)**: La til ny seksjon som dokumenterer eksperimentell Tasks-funksjon for holdbare kjøringswrappere og utsatt resultatinnhenting
- **Ikonsupport**: Notert at verktøy, ressurser, ressursmaler og prompt nå kan inkludere ikoner som tilleggsmeldedata

#### Dokumentasjonsoppdateringer
- **README.md**: La til MCP-spesifikasjon 2025-11-25 versjonsreferanse og forklaring på datobasert versjonering
- **study_guide.md**: Oppdatert curriculum-kart for å inkludere Tasks og Tool Annotations i seksjonen Core Concepts; oppdatert dokumentets tidsstempel

#### Samsvarsverifisering av spesifikasjoner
- **Protokollversjon**: Verifisert at all dokumentasjon refererer til gjeldende MCP-spesifikasjon 2025-11-25
- **Arkitekturalignering**: Bekreftet nøyaktighet i dokumentasjonen av tolagsarkitektur (Datalag + Transportlag)
- **Primitivdokumentasjon**: Validert serverprimitiver (Ressurser, Prompter, Verktøy) og klientprimitiver (Sampling, Elicitation, Logging, Roots)
- **Transportmekanismer**: Verifisert STLIO og Streamable HTTP-transportdokumentasjon
- **Sikkerhetsveiledning**: Bekreftet samsvar med gjeldende MCP sikkerhetsbeste praksis-dokumentasjon

#### Viktige MCP 2025-11-25 funksjoner dokumentert
- **OpenID Connect Discovery**: Auth-serveroppdagelse via OIDC
- **OAuth Client ID metadata-dokumenter**: Anbefalt klientregistreringsmekanisme
- **JSON Schema 2020-12**: Standard dialekt for MCP skjema-definisjoner
- **SDK Tiering System**: Formaliserte krav for SDK-funksjonsstøtte og vedlikehold
- **Styringsstruktur**: Formaliserte arbeidsgrupper og interessegrupper i MCP-styring

### Stor oppdatering av sikkerhetsdokumentasjon (02-Security/)

#### Integrasjon av MCP Security Summit Workshop (Sherpa)
- **Nytt praktisk treningsressurs**: La til omfattende integrasjon med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i all sikkerhetsdokumentasjon
- **Dekning av ekspedisjonsrute**: Dokumenterte full progresjon fra Base Camp til Summit
- **OWASP-alignering**: All sikkerhetsveiledning mapes nå til OWASP MCP Azure Security Guide-risikoer

#### OWASP MCP Top 10-integrasjon
- **Ny seksjon**: La til tabell over OWASP MCP Top 10 sikkerhetsrisikoer med Azure-mitigasjoner i hovedsikkerhets-README
- **Risiko-basert dokumentasjon**: Oppdatert mcp-security-controls-2025.md med OWASP MCP risiko-referanser for hvert sikkerhetsdomene
- **Referansearkitektur**: Lenket til OWASP MCP Azure Security Guide referansearkitektur og implementeringsmønstre

#### Oppdaterte sikkerhetsfiler
- **README.md**: La til Sherpa Workshop oversikt, ekspedisjonsrute-tabell, OWASP MCP Top 10 risikosammendrag og seksjon for praktisk trening
- **mcp-security-controls-2025.md**: Oppdatert header til februar 2026, lagt til OWASP risikoreferanser (MCP01-MCP08), fikset versjonsinkonsistens i spesifikasjonen
- **mcp-security-best-practices-2025.md**: La til Sherpa og OWASP ressursseksjon, oppdatert tidsstempel
- **mcp-best-practices.md**: La til praktisk treningsseksjon med Sherpa og OWASP-lenker
- **azure-content-safety-implementation.md**: La til OWASP MCP06 referanse, Sherpa Camp 3 alignement, og tilleggsressursseksjon

#### Nye ressurslenker lagt til
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuelle OWASP MCP risikosider (MCP01-MCP10)

### Curriculum-omfattende MCP-spesifikasjon 2025-11-25 justering

#### Modul 03 - Komme i gang
- **SDK-dokumentasjon**: La til Go SDK i offisiell SDK-liste; oppdaterte alle SDK-referanser for samsvar med MCP-spesifikasjon 2025-11-25
- **Transportavklaring**: Oppdaterte STDIO og HTTP Streaming transportbeskrivelser med eksplisitte spesifikasjonsreferanser

#### Modul 04 - Praktisk implementering
- **SDK-oppdateringer**: La til Go SDK; oppdaterte SDK-liste med spesifikasjonsversjonsreferanse
- **Autorisasjonsspesifikasjon**: Oppdaterte MCP Authorization spesifikasjonslink til gjeldende 2025-11-25 versjon

#### Modul 05 - Avanserte emner
- **Nye funksjoner**: Lagt til notat om nye MCP-spesifikasjon 2025-11-25 funksjoner (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Sikkerhetsressurser**: La til OWASP MCP Top 10 og Sherpa workshop-lenker i tillegg til referanser

#### Modul 06 - Fellesskapsbidrag
- **SDK-liste**: La til Swift og Rust SDK-er; oppdaterte spesifikasjonslink til 2025-11-25
- **Spesifikasjonsreferanse**: Oppdatert MCP-spesifikasjonslink til direkte spesifikasjons-URL

#### Modul 07 - Lærdom fra tidlig adopsjon
- **Ressursoppdateringer**: La til MCP-spesifikasjon 2025-11-25 lenke og OWASP MCP Top 10 i tillegg til ressurser

#### Modul 08 - Beste praksis
- **Spesifikasjonsversjon**: Oppdatert MCP-spesifikasjonsreferanse til 2025-11-25
- **Sikkerhetsressurser**: La til OWASP MCP Top 10 og Sherpa workshop i tillegg til referanser

#### Modul 10 - Strømlinjeforming av AI-arbeidsflyt
- **Merkeoppdatering**: Endret MCP-versjonsmerke fra SDK-versjon (1.9.3) til spesifikasjonsversjon (2025-11-25)
- **Ressurslenker**: Oppdatert MCP-spesifikasjonslink; la til OWASP MCP Top 10

#### Modul 11 - MCP Server praktiske labber
- **Spesifikasjonsreferanse**: Oppdatert MCP-spesifikasjonslink til 2025-11-25 versjon
- **Sikkerhetsressurser**: La til OWASP MCP Top 10 i offisielle ressurser

## 18. desember 2025
### Oppdatering av sikkerhetsdokumentasjon - MCP-spesifikasjon 2025-11-25

#### MCP Sikkerhetsanbefalinger (02-Security/mcp-best-practices.md) - Oppdatering av spesifikasjonsversjon
- **Oppdatering av protokollversjon**: Oppdatert for å referere til siste MCP-spesifikasjon 2025-11-25 (utgitt 25. november 2025)
  - Oppdaterte alle referanser til spesifikasjonsversjoner fra 2025-06-18 til 2025-11-25
  - Oppdaterte dokumentdatoer fra 18. august 2025 til 18. desember 2025
  - Verifiserte at alle spesifikasjons-URL-er peker til aktuell dokumentasjon
- **Innholdsvalidering**: Omfattende validering av sikkerhetsanbefalinger mot nyeste standarder
  - **Microsoft sikkerhetsløsninger**: Verifisert gjeldende terminologi og lenker for Prompt Shields (tidligere "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID og Azure Key Vault
  - **OAuth 2.1 sikkerhet**: Bekreftet samsvar med siste OAuth-sikkerhetsanbefalinger
  - **OWASP-standarder**: Validert at OWASP Top 10 for LLM-referanser fortsatt er oppdaterte
  - **Azure-tjenester**: Verifiserte alle Microsoft Azure dokumentasjonslenker og beste praksis
- **Standardjustering**: Alle refererte sikkerhetsstandarder bekreftet oppdaterte
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 beste praksis for sikkerhet
  - Azure sikkerhets- og samsvarsrammeverk
- **Implementeringsressurser**: Verifiserte alle implementeringsveiledninger og ressurser
  - Azure API Management autentiseringsmønstre
  - Microsoft Entra ID integrasjonsveiledninger
  - Azure Key Vault secrets management
  - DevSecOps pipelines og overvåkingsløsninger

### Dokumentasjonskvalitetssikring
- **Spesifikasjonsoverholdelse**: Sikret at alle obligatoriske MCP-sikkerhetskrav (MÅ/MÅ IKKE) stemmer med siste spesifikasjon
- **Ressursaktualitet**: Verifisert alle eksterne lenker til Microsoft-dokumentasjon, sikkerhetsstandarder og implementeringsveiledninger
- **Dekning av beste praksis**: Bekreftet omfattende dekning av autentisering, autorisasjon, AI-spesifikke trusler, leverandørkjedesikkerhet og bedriftsmønstre

## 6. oktober 2025

### Utvidelse av Komme i gang-seksjon – Avansert serverbruk og enkel autentisering

#### Avansert serverbruk (03-GettingStarted/10-advanced)
- **Nytt kapittel lagt til**: Introdusert en omfattende guide for avansert MCP serverbruk, som dekker både vanlige og lavnivå serverarkitekturer.
  - **Vanlig vs. lavnivå server**: Detaljert sammenligning og kodeeksempler i Python og TypeScript for begge tilnærminger.
  - **Handler-basert design**: Forklaring av handler-basert verktøy-/ressurs-/prompt-administrasjon for skalerbare, fleksible serverimplementeringer.
  - **Praktiske mønstre**: Virkelighetsnære scenarier hvor lavnivå servermønstre er fordelaktige for avanserte funksjoner og arkitektur.

#### Enkel autentisering (03-GettingStarted/11-simple-auth)
- **Nytt kapittel lagt til**: Steg-for-steg veiledning for å implementere enkel autentisering i MCP-servere.
  - **Autentiseringskonsepter**: Klar forklaring av autentisering vs. autorisasjon, og håndtering av legitimasjon.
  - **Grunnleggende autentiseringsimplementasjon**: Middleware-baserte autentiseringsmønstre i Python (Starlette) og TypeScript (Express), med kodeeksempler.
  - **Videreutvikling til avansert sikkerhet**: Veiledning for å starte med enkel autentisering og videre til OAuth 2.1 og RBAC, med referanser til avanserte sikkerhetsmoduler.

Disse tilleggene gir praktisk, hands-on veiledning for å bygge mer robuste, sikre og fleksible MCP-serverimplementeringer, som bygger bro mellom grunnleggende konsepter og avanserte produksjonsmønstre.

## 29. september 2025

### MCP Server Database Integrasjonslaboratorier - Omfattende praktisk læringsløype

#### 11-MCPServerHandsOnLabs - komplett kurs i databaseintegrasjon
- **Fullstendig 13-lab læringsløype**: Lagt til omfattende praktisk kurs for å bygge produksjonsklare MCP-servere med PostgreSQL-databaseintegrasjon
  - **Virkelige implementeringer**: Zava Retail analytics brukstilfelle som demonstrerer bedriftsmønstre
  - **Strukturert progresjon**:
    - **Lab 00-03: Grunnlag** - Introduksjon, kjernearkitektur, sikkerhet & multi-tenant, miljøoppsett
    - **Lab 04-06: Bygging av MCP-server** - Databasedesign & skjema, MCP-serverimplementasjon, verktøyutvikling  
    - **Lab 07-09: Avanserte funksjoner** - Semantisk søk-integrasjon, testing & feilsøking, VS Code-integrasjon
    - **Lab 10-12: Produksjon & beste praksis** - Distribusjonsstrategier, overvåking & observabilitet, beste praksis & optimalisering
  - **Bedriftsteknologier**: FastMCP-rammeverk, PostgreSQL med pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Avanserte funksjoner**: Row Level Security (RLS), semantisk søk, multi-tenant datatilgang, vektorinnbeddinger, sanntidsovervåking

#### Terminologistandardisering - Modul til Lab-konvertering
- **Omfattende dokumentasjonsoppdatering**: Systematisk oppdatert alle README-filer i 11-MCPServerHandsOnLabs til å bruke "Lab"-terminologi i stedet for "Modul"
  - **Seksjonsoverskrifter**: Oppdatert "What This Module Covers" til "What This Lab Covers" i alle 13 labber
  - **Innholdsbeskrivelser**: Endret "This module provides..." til "This lab provides..." i dokumentasjonen
  - **Læringsmål**: Oppdatert "By the end of this module..." til "By the end of this lab..."
  - **Navigasjonslenker**: Konverterte alle "Module XX:" referanser til "Lab XX:" i kryssreferanser og navigasjon
  - **Fullføringssporing**: Oppdatert "After completing this module..." til "After completing this lab..."
  - **Tekniske referanser bevart**: Opprettholdt Python-modulreferanser i konfigurasjonsfiler (f.eks. `"module": "mcp_server.main"`)

#### Forbedring av studieguide (study_guide.md)
- **Visuelt kurskart**: Lagt til ny seksjon "11. Database Integration Labs" med komplett visualisering av labstruktur
- **Repositorystruktur**: Oppdatert fra ti til elleve hovedseksjoner med detaljert beskrivelse av 11-MCPServerHandsOnLabs
- **Læringsstiveiledning**: Forbedret navigasjonsinstruksjoner for seksjoner 00-11
- **Teknologidekning**: Lagt til FastMCP, PostgreSQL, Azure-tjenesteintegrasjoner
- **Læringsresultater**: Fremhevet produksjonsklare serverutvikling, databaseintegrasjonsmønstre og bedriftsikkerhet

#### Hoved-README strukturforbedring
- **Lab-baserte begreper**: Oppdatert hoved-README.md i 11-MCPServerHandsOnLabs til konsekvent "Lab"-struktur
- **Læringsløypeorganisering**: Klar progresjon fra grunnleggende konsepter til avansert implementering og produksjonsdistribusjon
- **Virkelighetsfokus**: Vekt på praktisk, hands-on læring med bedriftsmønstre og teknologier

### Forbedringer i dokumentasjonskvalitet og konsistens
- **Hands-on fokus**: Forsterket praktisk, lab-basert tilnærming i all dokumentasjon
- **Bedriftsmønstre**: Fremhevet produksjonsklare implementeringer og bedriftsikkerhetshensyn
- **Teknologiintegrasjon**: Omfattende dekning av moderne Azure-tjenester og AI-integrasjonsmønstre
- **Læringsprogresjon**: Klar, strukturert vei fra grunnleggende konsepter til produksjonsdistribusjon

## 26. september 2025

### Case-studier forbedring - GitHub MCP Registry-integrasjon

#### Case-studier (09-CaseStudy/) - Fokus på økosystemutvikling
- **README.md**: Stor utvidelse med omfattende GitHub MCP Registry case-studie
  - **GitHub MCP Registry case-studie**: Ny omfattende gjennomgang av GitHubs MCP Registry-lansering i september 2025
    - **Problem-analyse**: Detaljert gjennomgang av fragmentert MCP server-oppdagelse og distribusjonsutfordringer
    - **Løsningsarkitektur**: GitHubs sentraliserte registry-tilnærming med ett-klikk VS Code installasjon
    - **Forretningspåvirkning**: Målbare forbedringer i utvikleropplæring og produktivitet
    - **Strategisk verdi**: Fokus på modulær agent-distribusjon og verktøysinteroperabilitet
    - **Økosystemutvikling**: Posisjonering som grunnleggende plattform for agentintegrasjon
  - **Forbedret case-studie struktur**: Oppdaterte alle syv case-studier med konsekvent format og komplett beskrivelse
    - Azure AI Travel Agents: Vekt på multi-agent orkestrering
    - Azure DevOps-integrasjon: Fokus på arbeidsflytautomatisering
    - Sanntidsdokumentasjonsoppslag: Python konsollklientimplementasjon
    - Interaktiv studieplan-generator: Chainlit samtalewebapp
    - In-Editor dokumentasjon: VS Code og GitHub Copilot integrasjon
    - Azure API Management: Bedrifts-API-integrasjonsmønstre
    - GitHub MCP Registry: Økosystemutvikling og fellesskapsplattform
  - **Omfattende konklusjon**: Omskrevet avslutningsseksjon som fremhever syv case-studier på tvers av MCP-implementeringsdimensjoner
    - Bedriftsintegrasjon, multi-agent orkestrering, utviklerproduktivitet
    - Økosystemutvikling, utdanningsapplikasjoner kategorisering
    - Forbedret innsikt i arkitekturmønstre, implementeringsstrategier og beste praksis
    - Vekt på MCP som moden, produksjonsklar protokoll

#### Oppdateringer i studieguide (study_guide.md)
- **Visuelt kurskart**: Oppdatert tankekart for å inkludere GitHub MCP Registry i Case Studies-seksjonen
- **Case-studiebeskrivelse**: Utvidet fra generelle beskrivelser til detaljert gjennomgang av syv omfattende case-studier
- **Repositorystruktur**: Oppdatert seksjon 10 for å reflektere komplett case-studie dekning med spesifikke implementasjonsdetaljer
- **Endringsloggintegrasjon**: Lagt til 26. september 2025-oppføring som dokumenterer GitHub MCP Registry tillegg og case-studieforbedringer
- **Datooppdateringer**: Oppdatert tidsstempel i bunnteksten til nyeste revisjon (26. september 2025)

### Forbedringer i dokumentasjonskvalitet
- **Konsistensforbedring**: Standardisert case-studieformat og struktur på tvers av alle syv eksempler
- **Omfattende dekning**: Case-studier dekker nå bedrifts-, utviklerproduktivitet- og økosystemutviklingsscenarier
- **Strategisk posisjonering**: Forsterket fokus på MCP som grunnplattform for agentbasert systemdistribusjon
- **Ressursintegrasjon**: Oppdaterte tilleggsmateriale med lenke til GitHub MCP Registry

## 15. september 2025

### Utvidelse av avanserte emner - Egendefinerte transporterer og kontekstengineering

#### MCP egendefinerte transportører (05-AdvancedTopics/mcp-transport/) - Ny avansert implementasjonsveiledning
- **README.md**: Komplett implementasjonsveiledning for egendefinerte MCP transportmekanismer
  - **Azure Event Grid Transport**: Omfattende serverløs hendelsesdrevet transportimplementasjon
    - C#, TypeScript og Python-eksempler med Azure Functions-integrasjon
    - Hendelsesdrevne arkitekturmønstre for skalerbare MCP-løsninger
    - Webhook-mottakere og push-basert meldinghåndtering
  - **Azure Event Hubs Transport**: Høyytelses streamingtransportimplementasjon
    - Sanntidstrømming for lav-latens scenarier
    - Partisjonering og checkpoint-styring
    - Meldingsbatching og ytelsesoptimalisering
  - **Bedriftsintegrasjonsmønstre**: Produksjonsklare arkitektur-eksempler
    - Distribuert MCP-prosessering på tvers av flere Azure Functions
    - Hybrid transportarkitektur som kombinerer flere transporttyper
    - Meldingsholdbarhet, pålitelighet og feilhåndtering
  - **Sikkerhet & overvåking**: Azure Key Vault integrasjon og observabilitetsmønstre
    - Managed identity autentisering og minste privilegiumsaksess
    - Application Insights telemetri og ytelsesovervåking
    - Circuit breakers og feilgjengivelsesmønstre
  - **Testrammeverk**: Omfattende teststrategier for egendefinerte transportører
    - Enhetstester med testdoubler og mocking-rammeverk
    - Integrasjonstester med Azure Test Containers
    - Ytelses- og belastningstesting hensyn

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Fremvoksende AI-disiplin
- **README.md**: Omfattende utforskning av kontekstengineering som et nytt felt
  - **Kjerneprinsipper**: Komplett deling av kontekst, beslutningsbevissthet, og håndtering av kontekstvindu
  - **MCP-protokolltilpasning**: Hvordan MCP-design adresserer utfordringer med kontekstengineering
    - Begrensninger av kontekstvindu og progresjonell lasting
    - Relevansbestemmelse og dynamisk kontekstinnhenting
    - Multimodal konsteksthåndtering og sikkerhetshensyn
  - **Implementeringstilnærminger**: Enkelttrådet vs. multi-agent arkitekturer
    - Kontekstdeling og prioriteringsteknikker
    - Progresjonell kontekstlasting og komprimeringsstrategier
    - Lagvis konteksttilnærming og hentingsoptimalisering
  - **Målerammeverk**: Fremvoksende metrikker for evaluering av konteksteffektivitet
    - Input-effektivitet, ytelse, kvalitet og brukeropplevelse
    - Eksperimentelle tilnærminger for kontekstoptimalisering
    - Feilanalyse og forbedringsmetoder

#### Oppdateringer i kursnavigasjon (README.md)
- **Forbedret modulstruktur**: Oppdatert kurs-tabell til å inkludere nye avanserte emner
  - Lagt til Context Engineering (5.14) og Custom Transport (5.15)
  - Konsistent formatering og navigasjonslenker på tvers av moduler
  - Oppdaterte beskrivelser for å reflektere gjeldende innholdsomfang

### Forbedringer i katalogstruktur
- **Navnestandardisering**: Omdøpt "mcp transport" til "mcp-transport" for samsvar med andre avanserte temakataloger
- **Innholdsorganisering**: Alle 05-AdvancedTopics-mapper følger nå konsistent navngivningsmønster (mcp-[topic])

### Forbedringer i dokumentasjonskvalitet
- **MCP-spesifikasjonsjustering**: Alt nytt innhold refererer MCP-spesifikasjon 2025-06-18
- **Flerspråklige eksempler**: Omfattende kodeeksempler i C#, TypeScript og Python
- **Bedriftsfokus**: Produksjonsklare mønstre og Azure skyintegrasjon gjennomgående
- **Visuell dokumentasjon**: Mermaid-diagrammer for arkitektur og flytdiagrammer

## 18. august 2025

### Omfattende dokumentasjonsoppdatering - MCP 2025-06-18 standarder

#### MCP sikkerhetsanbefalinger (02-Security/) - Fullstendig modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fullstendig omskriving i tråd med MCP-spesifikasjon 2025-06-18  
  - **Obligatoriske krav**: Lagt til eksplisitte MÅ/MÅ IKKE-krav fra offisiell spesifikasjon med tydelige visuelle indikatorer  
  - **12 Kjernepraksiser for sikkerhet**: Omstrukturert fra 15-punktsliste til omfattende sikkerhetsdomener  
    - Token-sikkerhet og autentisering med ekstern identitetstilbyderintegrasjon  
    - Sesjonshåndtering og transport-sikkerhet med kryptografiske krav  
    - AI-spesifikk trusselbeskyttelse med Microsoft Prompt Shields-integrasjon  
    - Tilgangskontroll og tillatelser med prinsippet om minste privilegium  
    - Innholdssikkerhet og overvåkning med Azure Content Safety-integrasjon  
    - Leverandørkjede-sikkerhet med omfattende komponentverifisering  
    - OAuth-sikkerhet og prevensjon av forvirret stedfortreder med PKCE-implementering  
    - Hendelseshåndtering og gjenoppretting med automatiserte kapasiteter  
    - Overholdelse og styring med regulatorisk samsvar  
    - Avanserte sikkerhetskontroller med nulltillit-arkitektur  
    - Microsoft sikkerhetsøkosystemintegrasjon med omfattende løsninger  
    - Kontinuerlig sikkerhetsevolusjon med adaptive praksiser  
  - **Microsoft sikkerhetsløsninger**: Forbedret integrasjonsveiledning for Prompt Shields, Azure Content Safety, Entra ID, og GitHub Advanced Security  
  - **Implementeringsressurser**: Kategorisert omfattende ressurslenker etter Offisiell MCP-dokumentasjon, Microsoft sikkerhetsløsninger, sikkerhetsstandarder og implementeringsguider  

#### Avanserte sikkerhetskontroller (02-Security/) - Enterprise-implementering  
- **MCP-SECURITY-CONTROLS-2025.md**: Fullstendig revisjon med sikkerhetsrammeverk for bedriftsnivå  
  - **9 omfattende sikkerhetsdomener**: Utvidet fra grunnleggende kontroller til detaljerte bedriftsrammer  
    - Avansert autentisering og autorisasjon med Microsoft Entra ID-integrasjon  
    - Token-sikkerhet og anti-passthrough-kontroller med omfattende validering  
    - Sesjonssikkerhetskontroller med kapringsforebygging  
    - AI-spesifikke sikkerhetskontroller med forebygging av prompt-injeksjon og verktøytoksinering  
    - Forvirret stedfortreder-angrepforebygging med OAuth-proxy-sikkerhet  
    - Sikkerhet ved kjøring av verktøy med sandkasse og isolasjon  
    - Leverandørkjede-sikkerhetskontroller med avhengighetsverifisering  
    - Overvåking og detekteringskontroller med SIEM-integrasjon  
    - Hendelseshåndtering og gjenoppretting med automatiserte kapasiteter  
  - **Implementeringseksempler**: Lagt til detaljerte YAML-konfigurasjonsblokker og kodeeksempler  
  - **Microsoft-løsningsintegrasjon**: Omfattende dekning av Azure-sikkerhetstjenester, GitHub Advanced Security og bedriftsidentitetsforvaltning  

#### Avanserte emner sikkerhet (05-AdvancedTopics/mcp-security/) - Produksjonsklar implementering  
- **README.md**: Fullstendig omskrevet for implementering av bedriftsikkerhet  
  - **Nåværende spesifikasjonsjustering**: Oppdatert til MCP-spesifikasjon 2025-06-18 med obligatoriske sikkerhetskrav  
  - **Forbedret autentisering**: Microsoft Entra ID-integrasjon med omfattende .NET- og Java Spring Security-eksempler  
  - **AI-sikkerhetsintegrasjon**: Microsoft Prompt Shields og Azure Content Safety-implementering med detaljerte Python-eksempler  
  - **Avansert trusselmitigering**: Omfattende implementeringseksempler for  
    - Forvirret stedfortreder-angrepforebygging med PKCE og validering av bruker-samtykke  
    - Token Passthrough-forebygging med målgruppevalidering og sikker token-håndtering  
    - Sesjonskapringsforebygging med kryptografisk binding og adferdsanalyse  
  - **Bedriftsikkerhetsintegrasjon**: Azure Application Insights-overvåking, trusseldeteksjonspipelines og leverandørkjede-sikkerhet  
  - **Implementeringssjekkliste**: Klare obligatoriske vs. anbefalte sikkerhetskontroller med Microsoft sikkerhetsøkosystemfordeler  

### Dokumentasjonskvalitet & standardjustering  
- **Spesifikasjonsreferanser**: Oppdatert alle referanser til gjeldende MCP-spesifikasjon 2025-06-18  
- **Microsoft sikkerhetsøkosystem**: Forbedret integrasjonsveiledning gjennom all sikkerhetsdokumentasjon  
- **Praktisk implementering**: Lagt til detaljerte kodeeksempler i .NET, Java og Python med bedriftsmønstre  
- **Ressursorganisering**: Omfattende kategorisering av offisiell dokumentasjon, sikkerhetsstandarder og implementeringsguider  
- **Visuelle indikatorer**: Klare markeringer av obligatoriske krav vs. anbefalte praksiser  

#### Kjernebegreper (01-CoreConcepts/) - Fullstendig modernisering  
- **Protokollversjonsoppdatering**: Oppdatert til å referere til gjeldende MCP-spesifikasjon 2025-06-18 med datobasert versjonering (YYYY-MM-DD-format)  
- **Arkitekturfinepussing**: Forbedrede beskrivelser av verter, klienter og servere for å reflektere gjeldende MCP-arkitektur  
  - Verter definert som AI-applikasjoner som koordinerer flere MCP-klienttilkoblinger  
  - Klienter beskrevet som protokoll-konnektorer som opprettholder én-til-én server-relasjoner  
  - Servere utvidet med lokale vs. eksterne distribusjonsscenarier  
- **Primitivrestrukturering**: Fullstendig overhaling av server- og klientprimitiver  
  - Serverprimitiver: Ressurser (datakilder), Prompter (maler), Verktøy (eksekverbare funksjoner) med detaljerte forklaringer og eksempler  
  - Klientprimitiver: Sampling (LLM fullføringer), Elicitation (brukerinndata), Logging (feilsøking/overvåkning)  
  - Oppdatert med nåværende oppdagelses- (`*/list`), hentedata- (`*/get`) og eksekverings- (`*/call`) metode-mønstre  
- **Protokollarkitektur**: Innført to-lags arkitekturmodell  
  - Datalag: JSON-RPC 2.0 fundament med livssyklusforvaltning og primitiver  
  - Transportlag: STDIO (lokal) og Streamable HTTP med SSE (fjern) transportmekanismer  
- **Sikkerhetsrammeverk**: Omfattende sikkerhetsprinsipper inkludert eksplisitt brukersamtykke, datavern, sikker kjøring av verktøy og transportsikkerhet  
- **Kommunikasjonsmønstre**: Oppdaterte protokollmeldinger for initialisering, oppdagelse, utførelse, og varsling  
- **Kodeeksempler**: Oppfriskede fler-språklige eksempler (.NET, Java, Python, JavaScript) for å reflektere nåværende MCP SDK-mønstre  

#### Sikkerhet (02-Security/) - Omfattende sikkerhetsoverhaling  
- **Standardtilpasning**: Full samsvar med MCP-spesifikasjon 2025-06-18 sikkerhetskrav  
- **Autentiseringsevolusjon**: Dokumentert utvikling fra egendefinerte OAuth-servere til ekstern identitetstilbyder-delegasjon (Microsoft Entra ID)  
- **AI-spesifikk trusselanalyse**: Forbedret dekning av moderne AI-angrepsvektorer  
  - Detaljerte scenarier for prompt-injeksjonsangrep med virkelige eksempler  
  - Mekanismer for verktøytoksinering og ”rug pull”-angrepsmønstre  
  - Kontekstvindu-toksinering og modellforvirringsangrep  
- **Microsoft AI-sikkerhetsløsninger**: Omfattende dekning av Microsoft sikkerhetsøkosystem  
  - AI Prompt Shields med avansert deteksjon, spotlighting og avgrensningsteknikker  
  - Azure Content Safety-integrasjonsmønstre  
  - GitHub Advanced Security for leverandørkjede-beskyttelse  
- **Avansert trusselmitigering**: Detaljerte sikkerhetskontroller for  
  - Sesjonskapring med MCP-spesifikke angrepsscenarier og kryptografiske sesjons-ID-krav  
  - Forvirret stedfortreder-problemer i MCP proxy-scenarier med eksplisitte samtykkekrav  
  - Token passthrough-sårbarheter med obligatoriske valideringskontroller  
- **Leverandørkjede-sikkerhet**: Utvidet AI-leverandørkjede-dekning inkludert fundamentmodeller, embeddings-tjenester, kontekstleverandører og tredjeparts-APIer  
- **Fundamentalsikkerhet**: Forbedret integrasjon med bedrifts-sikkerhetsmønstre inkludert nulltillit-arkitektur og Microsoft sikkerhetsøkosystem  
- **Ressursorganisering**: Kategorisert omfattende ressurslenker etter type (Offisiell dokumentasjon, Standarder, Forskning, Microsoft-løsninger, Implementeringsguider)  

### Forbedringer i dokumentasjonskvalitet  
- **Strukturerte læringsmål**: Forbedrede læringsmål med spesifikke, handlingsorienterte resultater  
- **Kryssreferanser**: Lagt til lenker mellom relaterte sikkerhets- og kjernebegreps-emner  
- **Oppdatert informasjon**: Oppdatert alle datoreferanser og spesifikasjonslenker til gjeldende standarder  
- **Implementeringsveiledning**: Lagt til spesifikke, handlingsorienterte implementeringsretningslinjer gjennom begge seksjoner  

## 16. juli 2025  

### README- og navigasjonsforbedringer  
- Fullstendig redesignet pensum-navigasjon i README.md  
- Erstattet `<details>`-tagger med mer tilgjengelig tabellformat  
- Opprettet alternative layoutvalg i ny "alternative_layouts"-mappe  
- Lagt til kortbaserte, fanebaserte og akkordeon-stil navigasjonseksempler  
- Oppdatert avsnittet om depotstruktur for å inkludere alle siste filer  
- Forbedret "Hvordan bruke dette pensumet"-seksjonen med klare anbefalinger  
- Oppdatert MCP-spesifikasjonslenker til å peke til korrekte URL-er  
- Lagt til seksjon for kontekstteknikk (5.14) i pensumstrukturen  

### Oppdateringer i studieguide  
- Fullstendig revidert studieguide for å samsvare med nåværende depotstruktur  
- Lagt til nye seksjoner for MCP-klienter og verktøy, og populære MCP-servere  
- Oppdatert visuell pensumkart for å nøyaktig reflektere alle emner  
- Forbedret beskrivelser av avanserte emner for å dekke alle spesialiserte områder  
- Oppdatert kasusstudieseksjon for å reflektere faktiske eksempler  
- Lagt til denne omfattende endringsloggen  

### Fellesskapsbidrag (06-CommunityContributions/)  
- Lagt til detaljert informasjon om MCP-servere for bilde-generering  
- Lagt til omfattende seksjon for bruk av Claude i VSCode  
- Lagt til Cline terminalklient-oppsett og bruksinstruksjoner  
- Oppdatert MCP-klientseksjon for å inkludere alle populære klientalternativer  
- Forbedret bidrags-eksempler med mer presise kodeprøver  

### Avanserte emner (05-AdvancedTopics/)  
- Organisert alle spesialiserte emnemapper med konsistent navngivning  
- Lagt til materiale og eksempler for kontekstteknikk  
- Lagt til dokumentasjon for Foundry-agentintegrasjon  
- Forbedret integrasjon med Entra ID sikkerhet  

## 11. juni 2025  

### Første opprettelse  
- Utgitt første versjon av MCP for Beginners-pensum  
- Opprettet grunnleggende struktur for alle 10 hovedseksjoner  
- Implementert visuell pensumkart for navigasjon  
- Lagt til innledende eksempelsprosjekter i flere programmeringsspråk  

### Komme i gang (03-GettingStarted/)  
- Opprettet første serverimplementeringseksempler  
- Lagt til veiledning for klientutvikling  
- Inkludert instruksjoner for LLM-klientintegrasjon  
- Lagt til dokumentasjon for VS Code-integrasjon  
- Implementert Server-Sent Events (SSE) server-eksempler  

### Kjernebegreper (01-CoreConcepts/)  
- Lagt til detaljert forklaring av klient-server-arkitektur  
- Opprettet dokumentasjon om nøkkelkomponenter i protokollen  
- Dokumenterte meldingsmønstre i MCP  

## 23. mai 2025  

### Depotstruktur  
- Initialisert depot med grunnleggende mappestruktur  
- Opprettet README-filer for hver hovedseksjon  
- Satt opp oversettelsesinfrastruktur  
- Lagt til bilde-ressurser og diagrammer  

### Dokumentasjon  
- Opprettet initial README.md med oversikt over pensum  
- Lagt til CODE_OF_CONDUCT.md og SECURITY.md  
- Satt opp SUPPORT.md med veiledning for å få hjelp  
- Opprettet foreløpig struktur for studieguide  

## 15. april 2025  

### Planlegging og rammeverk  
- Innledende planlegging for MCP for Beginners-pensum  
- Definerte læringsmål og målgruppe  
- Skisset opp 10-seksjons struktur for pensum  
- Utviklet konseptuelt rammeverk for eksempler og kasusstudier  
- Opprettet første prototyp-eksempler for nøkkelkonsepter  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->