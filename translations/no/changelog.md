# Endringslogg: MCP for Beginners Pensum

Dette dokumentet fungerer som en oversikt over alle betydelige endringer gjort i Model Context Protocol (MCP) for Beginners pensum. Endringer dokumenteres i omvendt kronologisk rekkefølge (nyeste endringer først).

## 18. desember 2025

### Oppdatering av sikkerhetsdokumentasjon - MCP-spesifikasjon 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Oppdatering av spesifikasjonsversjon
- **Oppdatering av protokollversjon**: Oppdatert til å referere til siste MCP-spesifikasjon 2025-11-25 (utgitt 25. november 2025)
  - Oppdatert alle referanser til spesifikasjonsversjon fra 2025-06-18 til 2025-11-25
  - Oppdatert dokumentdatoer fra 18. august 2025 til 18. desember 2025
  - Verifisert at alle spesifikasjons-URLer peker til gjeldende dokumentasjon
- **Innholdsvalidering**: Omfattende validering av sikkerhetsbeste praksis mot siste standarder
  - **Microsoft Security Solutions**: Verifisert gjeldende terminologi og lenker for Prompt Shields (tidligere "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID og Azure Key Vault
  - **OAuth 2.1 Security**: Bekreftet samsvar med siste OAuth sikkerhetsbeste praksis
  - **OWASP-standarder**: Validert at OWASP Top 10 for LLMs-referanser fortsatt er oppdaterte
  - **Azure-tjenester**: Verifisert alle Microsoft Azure dokumentasjonslenker og beste praksis
- **Standardtilpasning**: Alle refererte sikkerhetsstandarder bekreftet oppdaterte
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure sikkerhets- og samsvarsrammeverk
- **Implementeringsressurser**: Verifisert alle lenker til implementeringsguider og ressurser
  - Azure API Management autentiseringsmønstre
  - Microsoft Entra ID integrasjonsguider
  - Azure Key Vault hemmelighetshåndtering
  - DevSecOps pipelines og overvåkningsløsninger

### Kvalitetssikring av dokumentasjon
- **Spesifikasjonssamsvar**: Sikret at alle obligatoriske MCP sikkerhetskrav (MÅ/MÅ IKKE) samsvarer med siste spesifikasjon
- **Ressursaktualitet**: Verifisert alle eksterne lenker til Microsoft-dokumentasjon, sikkerhetsstandarder og implementeringsguider
- **Dekning av beste praksis**: Bekreftet omfattende dekning av autentisering, autorisasjon, AI-spesifikke trusler, leverandørkjedesikkerhet og bedriftsmønstre

## 6. oktober 2025

### Utvidelse av Komme i gang-seksjon – Avansert serverbruk & Enkel autentisering

#### Avansert serverbruk (03-GettingStarted/10-advanced)
- **Nytt kapittel lagt til**: Introdusert en omfattende guide til avansert MCP-serverbruk, som dekker både vanlige og lavnivå serverarkitekturer.
  - **Vanlig vs. lavnivå server**: Detaljert sammenligning og kodeeksempler i Python og TypeScript for begge tilnærminger.
  - **Handler-basert design**: Forklaring av handler-basert verktøy-/ressurs-/prompt-administrasjon for skalerbare, fleksible serverimplementasjoner.
  - **Praktiske mønstre**: Virkelige scenarier hvor lavnivå servermønstre er fordelaktige for avanserte funksjoner og arkitektur.

#### Enkel autentisering (03-GettingStarted/11-simple-auth)
- **Nytt kapittel lagt til**: Trinnvis guide for å implementere enkel autentisering i MCP-servere.
  - **Autentiseringskonsepter**: Klar forklaring av autentisering vs. autorisasjon, og håndtering av legitimasjon.
  - **Grunnleggende autentiseringsimplementasjon**: Middleware-baserte autentiseringsmønstre i Python (Starlette) og TypeScript (Express), med kodeeksempler.
  - **Overgang til avansert sikkerhet**: Veiledning for å starte med enkel autentisering og gå videre til OAuth 2.1 og RBAC, med referanser til avanserte sikkerhetsmoduler.

Disse tilleggene gir praktisk, hands-on veiledning for å bygge mer robuste, sikre og fleksible MCP-serverimplementasjoner, som bygger bro mellom grunnleggende konsepter og avanserte produksjonsmønstre.

## 29. september 2025

### MCP Server Database Integrasjon Labs - Omfattende praktisk læringssti

#### 11-MCPServerHandsOnLabs - Ny komplett databaseintegrasjons-pensum
- **Fullstendig 13-lab læringssti**: Lagt til omfattende praktisk pensum for å bygge produksjonsklare MCP-servere med PostgreSQL databaseintegrasjon
  - **Virkelighetsnær implementering**: Zava Retail analysebrukstilfelle som demonstrerer bedriftsnivåmønstre
  - **Strukturert læringsprogresjon**:
    - **Labs 00-03: Grunnlag** - Introduksjon, kjernearkitektur, sikkerhet & multi-tenancy, miljøoppsett
    - **Labs 04-06: Bygging av MCP-server** - Databasedesign & skjema, MCP-serverimplementasjon, verktøyutvikling  
    - **Labs 07-09: Avanserte funksjoner** - Semantisk søkeintegrasjon, testing & feilsøking, VS Code-integrasjon
    - **Labs 10-12: Produksjon & beste praksis** - Distribusjonsstrategier, overvåking & observabilitet, beste praksis & optimalisering
  - **Bedriftsteknologier**: FastMCP-rammeverk, PostgreSQL med pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Avanserte funksjoner**: Row Level Security (RLS), semantisk søk, multi-tenant data-tilgang, vektor-embeddings, sanntidsovervåking

#### Terminologistandardisering - Modul til Lab-konvertering
- **Omfattende dokumentasjonsoppdatering**: Systematisk oppdatert alle README-filer i 11-MCPServerHandsOnLabs til å bruke "Lab"-terminologi i stedet for "Modul"
  - **Seksjonsoverskrifter**: Oppdatert "What This Module Covers" til "What This Lab Covers" i alle 13 labs
  - **Innholdsbeskrivelse**: Endret "This module provides..." til "This lab provides..." gjennom hele dokumentasjonen
  - **Læringsmål**: Oppdatert "By the end of this module..." til "By the end of this lab..."
  - **Navigasjonslenker**: Konvertert alle "Module XX:"-referanser til "Lab XX:" i kryssreferanser og navigasjon
  - **Fullføringssporing**: Oppdatert "After completing this module..." til "After completing this lab..."
  - **Bevarte tekniske referanser**: Opprettholdt Python-modulreferanser i konfigurasjonsfiler (f.eks. `"module": "mcp_server.main"`)

#### Forbedring av studieveiledning (study_guide.md)
- **Visuelt pensumkart**: Lagt til ny seksjon "11. Database Integration Labs" med omfattende visualisering av lab-struktur
- **Repository-struktur**: Oppdatert fra ti til elleve hovedseksjoner med detaljert beskrivelse av 11-MCPServerHandsOnLabs
- **Læringsstiveiledning**: Forbedret navigasjonsinstruksjoner for seksjoner 00-11
- **Teknologidekning**: Lagt til detaljer om FastMCP, PostgreSQL, Azure-tjenesteintegrasjoner
- **Læringsutbytte**: Vektlagt produksjonsklar serverutvikling, databaseintegrasjonsmønstre og bedriftsikkerhet

#### Forbedring av hoved-README-struktur
- **Lab-basert terminologi**: Oppdatert hoved README.md i 11-MCPServerHandsOnLabs til konsekvent bruk av "Lab"-struktur
- **Læringssti-organisering**: Klar progresjon fra grunnleggende konsepter gjennom avansert implementering til produksjonsdistribusjon
- **Virkelighetsfokus**: Vekt på praktisk, hands-on læring med bedriftsnivåmønstre og teknologier

### Forbedringer i dokumentasjonskvalitet og konsistens
- **Hands-on læringsfokus**: Forsterket praktisk, lab-basert tilnærming gjennom hele dokumentasjonen
- **Bedriftsmønsterfokus**: Fremhevet produksjonsklare implementasjoner og bedriftsikkerhetshensyn
- **Teknologiintegrasjon**: Omfattende dekning av moderne Azure-tjenester og AI-integrasjonsmønstre
- **Læringsprogresjon**: Klar, strukturert sti fra grunnleggende konsepter til produksjonsdistribusjon

## 26. september 2025

### Forbedring av casestudier - GitHub MCP Registry-integrasjon

#### Casestudier (09-CaseStudy/) - Fokus på økosystemutvikling
- **README.md**: Stor utvidelse med omfattende GitHub MCP Registry casestudie
  - **GitHub MCP Registry casestudie**: Ny omfattende casestudie som undersøker GitHubs MCP Registry-lansering i september 2025
    - **Problemanalyse**: Detaljert gjennomgang av fragmentert MCP-serveroppdagelse og distribusjonsutfordringer
    - **Løsningsarkitektur**: GitHubs sentraliserte registertilnærming med ett-klikk VS Code-installasjon
    - **Forretningspåvirkning**: Målbare forbedringer i utvikleronboarding og produktivitet
    - **Strategisk verdi**: Fokus på modulær agentdistribusjon og tverrverktøy interoperabilitet
    - **Økosystemutvikling**: Posisjonering som grunnleggende plattform for agentisk integrasjon
  - **Forbedret casestudie-struktur**: Oppdatert alle syv casestudier med konsistent formatering og omfattende beskrivelser
    - Azure AI Travel Agents: Vekt på multi-agent orkestrering
    - Azure DevOps-integrasjon: Fokus på arbeidsflytautomatisering
    - Sanntids dokumenthenting: Python konsollklientimplementasjon
    - Interaktiv studieplan-generator: Chainlit samtalewebapp
    - In-Editor dokumentasjon: VS Code og GitHub Copilot-integrasjon
    - Azure API Management: Bedrifts-API-integrasjonsmønstre
    - GitHub MCP Registry: Økosystemutvikling og fellesskapsplattform
  - **Omfattende konklusjon**: Omskrevet konklusjonsseksjon som fremhever syv casestudier som dekker flere MCP-implementeringsdimensjoner
    - Bedriftsintegrasjon, multi-agent orkestrering, utviklerproduktivitet
    - Økosystemutvikling, utdanningsapplikasjoner kategorisering
    - Forbedrede innsikter i arkitekturmønstre, implementeringsstrategier og beste praksis
    - Vekt på MCP som moden, produksjonsklar protokoll

#### Oppdateringer i studieveiledning (study_guide.md)
- **Visuelt pensumkart**: Oppdatert tankekart for å inkludere GitHub MCP Registry i Casestudier-seksjonen
- **Beskrivelse av casestudier**: Forbedret fra generiske beskrivelser til detaljert gjennomgang av syv omfattende casestudier
- **Repository-struktur**: Oppdatert seksjon 10 for å reflektere omfattende casestudiedekning med spesifikke implementeringsdetaljer
- **Endringslogg-integrasjon**: Lagt til oppføring 26. september 2025 som dokumenterer GitHub MCP Registry-tillegg og casestudieforbedringer
- **Datooppdateringer**: Oppdatert bunntekst-tidsstempel for å reflektere siste revisjon (26. september 2025)

### Forbedringer i dokumentasjonskvalitet
- **Konsistensforbedring**: Standardisert casestudieformatering og struktur på tvers av alle syv eksempler
- **Omfattende dekning**: Casestudier dekker nå bedrifts-, utviklerproduktivitet- og økosystemutviklingsscenarier
- **Strategisk posisjonering**: Forsterket fokus på MCP som grunnleggende plattform for agentisk systemdistribusjon
- **Ressursintegrasjon**: Oppdaterte tilleggsmaterialer for å inkludere GitHub MCP Registry-lenke

## 15. september 2025

### Utvidelse av avanserte emner - Egendefinerte transportmekanismer & kontekstengineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Ny avansert implementeringsguide
- **README.md**: Komplett implementeringsguide for egendefinerte MCP transportmekanismer
  - **Azure Event Grid Transport**: Omfattende serverløs hendelsesdrevet transportimplementasjon
    - C#, TypeScript og Python-eksempler med Azure Functions-integrasjon
    - Hendelsesdrevne arkitekturmønstre for skalerbare MCP-løsninger
    - Webhook-mottakere og push-basert meldingshåndtering
  - **Azure Event Hubs Transport**: Høy gjennomstrømming streaming-transportimplementasjon
    - Sanntids streamingmuligheter for lav-latens scenarier
    - Partisjonering og checkpoint-administrasjon
    - Meldingsbatching og ytelsesoptimalisering
  - **Bedriftsintegrasjonsmønstre**: Produksjonsklare arkitektur-eksempler
    - Distribuert MCP-prosessering på tvers av flere Azure Functions
    - Hybrid transportarkitektur som kombinerer flere transporttyper
    - Meldingsholdbarhet, pålitelighet og feilhåndteringsstrategier
  - **Sikkerhet & overvåking**: Azure Key Vault-integrasjon og observabilitetsmønstre
    - Administrert identitetsautentisering og minste privilegium-tilgang
    - Application Insights telemetri og ytelsesovervåking
    - Kretsbrytere og feiltoleransemønstre
  - **Testingsrammeverk**: Omfattende teststrategier for egendefinerte transporter
    - Enhetstesting med testdoubler og mocking-rammeverk
    - Integrasjonstesting med Azure Test Containers
    - Ytelses- og belastningstesting hensyn

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Fremvoksende AI-disiplin
- **README.md**: Omfattende utforskning av kontekstengineering som et fremvoksende felt
  - **Kjerneprinsipper**: Fullstendig kontekstdeling, handlingsbeslutningsbevissthet og kontekstvindu-administrasjon
  - **MCP-protokollsamsvar**: Hvordan MCP-design adresserer kontekstengineering-utfordringer
    - Begrensninger i kontekstvindu og progressive lastestrategier
    - Relevansbestemmelse og dynamisk kontekstinnhenting
    - Multimodal kontekstbehandling og sikkerhetshensyn
  - **Implementeringstilnærminger**: Enkelttrådet vs. multi-agent arkitekturer
    - Kontekstchunking og prioriteringsteknikker
    - Progressiv kontekstlasting og komprimeringsstrategier
    - Lagdelt konteksttilnærming og innhentingsoptimalisering
  - **Målerammeverk**: Fremvoksende metrikker for evaluering av konteksteffektivitet
    - Inndataseffektivitet, ytelse, kvalitet og brukeropplevelsesvurderinger
    - Eksperimentelle tilnærminger til kontekstoptimalisering
    - Feilanalyse og forbedringsmetodikker

#### Oppdateringer i pensumnavigasjon (README.md)
- **Forbedret modulstruktur**: Oppdatert pensumtabell for å inkludere nye avanserte emner
  - Lagt til Context Engineering (5.14) og Custom Transport (5.15) oppføringer
  - Konsistent formatering og navigasjonslenker på tvers av alle moduler
  - Oppdaterte beskrivelser for å reflektere nåværende innholdsomfang

### Forbedringer i katalogstruktur
- **Navnestandardisering**: Omdøpt "mcp transport" til "mcp-transport" for konsistens med andre avanserte emnekataloger
- **Innholdsorganisering**: Alle 05-AdvancedTopics-mapper følger nå konsistent navnemønster (mcp-[topic])

### Forbedringer i dokumentasjonskvalitet
- **MCP-spesifikasjonssamsvar**: Alt nytt innhold refererer til gjeldende MCP-spesifikasjon 2025-06-18
- **Flerspråklige eksempler**: Omfattende kodeeksempler i C#, TypeScript og Python
- **Bedriftsfokus**: Produksjonsklare mønstre og Azure skyintegrasjon gjennomgående
- **Visuell dokumentasjon**: Mermaid-diagrammer for arkitektur- og flytvisualisering

## 18. august 2025

### Omfattende dokumentasjonsoppdatering - MCP 2025-06-18 standarder

#### MCP Security Best Practices (02-Security/) - Fullstendig modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fullstendig omskriving i samsvar med MCP-spesifikasjon 2025-06-18
  - **Obligatoriske krav**: Lagt til eksplisitte MÅ/MÅ IKKE-krav fra offisiell spesifikasjon med klare visuelle indikatorer
  - **12 kjerne sikkerhetspraksiser**: Omstrukturert fra 15-punkts liste til omfattende sikkerhetsdomener
    - Token-sikkerhet og autentisering med integrasjon av ekstern identitetsleverandør
    - Sesjonshåndtering og transport-sikkerhet med kryptografiske krav
    - AI-spesifikk trusselbeskyttelse med integrasjon av Microsoft Prompt Shields
    - Tilgangskontroll og tillatelser med prinsippet om minste privilegium
    - Innholdssikkerhet og overvåking med integrasjon av Azure Content Safety
    - Leverandørkjede-sikkerhet med omfattende komponentverifisering
    - OAuth-sikkerhet og forebygging av forvirret stedfortreder med PKCE-implementering
    - Hendelseshåndtering og gjenoppretting med automatiserte funksjoner
    - Overholdelse og styring med regulatorisk tilpasning
    - Avanserte sikkerhetskontroller med nulltillit-arkitektur
    - Integrasjon av Microsoft sikkerhetsekosystem med omfattende løsninger
    - Kontinuerlig sikkerhetsevolusjon med adaptive praksiser
  - **Microsoft sikkerhetsløsninger**: Forbedret integrasjonsveiledning for Prompt Shields, Azure Content Safety, Entra ID og GitHub Advanced Security
  - **Implementeringsressurser**: Kategoriserte omfattende ressurslenker etter Offisiell MCP-dokumentasjon, Microsoft sikkerhetsløsninger, sikkerhetsstandarder og implementeringsguider

#### Avanserte sikkerhetskontroller (02-Security/) - Enterprise-implementering
- **MCP-SECURITY-CONTROLS-2025.md**: Fullstendig revisjon med sikkerhetsrammeverk på bedriftsnivå
  - **9 omfattende sikkerhetsdomener**: Utvidet fra grunnleggende kontroller til detaljert bedriftsrammeverk
    - Avansert autentisering og autorisasjon med Microsoft Entra ID-integrasjon
    - Token-sikkerhet og anti-passthrough-kontroller med omfattende validering
    - Sesjonssikkerhetskontroller med forebygging av kapring
    - AI-spesifikke sikkerhetskontroller med forebygging av prompt-injeksjon og verktøyforgiftning
    - Forebygging av forvirret stedfortreder-angrep med OAuth-proxy-sikkerhet
    - Verktøykjøringssikkerhet med sandkasse og isolasjon
    - Leverandørkjede-sikkerhetskontroller med avhengighetsverifisering
    - Overvåkings- og deteksjonskontroller med SIEM-integrasjon
    - Hendelseshåndtering og gjenoppretting med automatiserte funksjoner
  - **Implementeringseksempler**: Lagt til detaljerte YAML-konfigurasjonsblokker og kodeeksempler
  - **Microsoft-løsningsintegrasjon**: Omfattende dekning av Azure sikkerhetstjenester, GitHub Advanced Security og bedriftsidentitetsadministrasjon

#### Avanserte emner sikkerhet (05-AdvancedTopics/mcp-security/) - Produksjonsklar implementering
- **README.md**: Fullstendig omskriving for bedriftsimplementering av sikkerhet
  - **Nåværende spesifikasjonstilpasning**: Oppdatert til MCP-spesifikasjon 2025-06-18 med obligatoriske sikkerhetskrav
  - **Forbedret autentisering**: Microsoft Entra ID-integrasjon med omfattende .NET- og Java Spring Security-eksempler
  - **AI-sikkerhetsintegrasjon**: Microsoft Prompt Shields og Azure Content Safety-implementering med detaljerte Python-eksempler
  - **Avansert trusselmitigering**: Omfattende implementeringseksempler for
    - Forebygging av forvirret stedfortreder-angrep med PKCE og validering av bruker samtykke
    - Forebygging av token-passthrough med målgruppevalidering og sikker tokenhåndtering
    - Forebygging av sesjonskapring med kryptografisk binding og atferdsanalyse
  - **Bedriftsintegrasjon av sikkerhet**: Azure Application Insights-overvåking, trusseldeteksjonspipelines og leverandørkjede-sikkerhet
  - **Implementeringssjekkliste**: Klare obligatoriske vs. anbefalte sikkerhetskontroller med fordeler fra Microsoft sikkerhetsekosystem

### Dokumentasjonskvalitet og standardtilpasning
- **Spesifikasjonsreferanser**: Oppdatert alle referanser til nåværende MCP-spesifikasjon 2025-06-18
- **Microsoft sikkerhetsekosystem**: Forbedret integrasjonsveiledning gjennom all sikkerhetsdokumentasjon
- **Praktisk implementering**: Lagt til detaljerte kodeeksempler i .NET, Java og Python med bedriftsmønstre
- **Ressursorganisering**: Omfattende kategorisering av offisiell dokumentasjon, sikkerhetsstandarder og implementeringsguider
- **Visuelle indikatorer**: Klar merking av obligatoriske krav vs. anbefalte praksiser


#### Kjernebegreper (01-CoreConcepts/) - Fullstendig modernisering
- **Protokollversjonsoppdatering**: Oppdatert til å referere nåværende MCP-spesifikasjon 2025-06-18 med datobasert versjonering (ÅÅÅÅ-MM-DD-format)
- **Arkitekturforbedring**: Forbedrede beskrivelser av Hosts, Clients og Servers for å reflektere nåværende MCP-arkitektur mønstre
  - Hosts nå tydelig definert som AI-applikasjoner som koordinerer flere MCP-klienttilkoblinger
  - Clients beskrevet som protokollkoblinger som opprettholder én-til-én serverrelasjoner
  - Servers forbedret med lokale vs. eksterne distribusjonsscenarier
- **Primitive omstrukturering**: Fullstendig revisjon av server- og klientprimitiver
  - Serverprimitiver: Ressurser (datakilder), Prompter (maler), Verktøy (kjørbare funksjoner) med detaljerte forklaringer og eksempler
  - Klientprimitiver: Sampling (LLM fullføringer), Elicitation (brukerinput), Logging (feilsøking/overvåking)
  - Oppdatert med nåværende oppdagelses- (`*/list`), hentings- (`*/get`) og utførelses- (`*/call`) metode-mønstre
- **Protokollarkitektur**: Innført to-lags arkitekturmodell
  - Datalag: JSON-RPC 2.0-grunnlag med livssyklusadministrasjon og primitiver
  - Transportlag: STDIO (lokal) og Streamable HTTP med SSE (ekstern) transportmekanismer
- **Sikkerhetsrammeverk**: Omfattende sikkerhetsprinsipper inkludert eksplisitt brukersamtykke, datavern, sikker kjøring av verktøy og transportlagsikkerhet
- **Kommunikasjonsmønstre**: Oppdaterte protokollmeldinger for å vise initialisering, oppdagelse, utførelse og varslingsflyter
- **Kodeeksempler**: Oppfriskede flerspråklige eksempler (.NET, Java, Python, JavaScript) for å reflektere nåværende MCP SDK-mønstre

#### Sikkerhet (02-Security/) - Omfattende sikkerhetsrevisjon  
- **Standardtilpasning**: Full tilpasning til MCP-spesifikasjon 2025-06-18 sikkerhetskrav
- **Autentiseringsevolusjon**: Dokumentert utvikling fra egendefinerte OAuth-servere til ekstern identitetsleverandør-delegering (Microsoft Entra ID)
- **AI-spesifikk trusselanalyse**: Forbedret dekning av moderne AI-angrepsvektorer
  - Detaljerte scenarier for prompt-injeksjonsangrep med virkelighetseksempler
  - Mekanismer for verktøyforgiftning og "rug pull"-angrepsmønstre
  - Forgiftning av kontekstvindu og modellforvirringsangrep
- **Microsoft AI-sikkerhetsløsninger**: Omfattende dekning av Microsoft sikkerhetsekosystem
  - AI Prompt Shields med avansert deteksjon, spotlighting og skilleteknikker
  - Azure Content Safety-integrasjonsmønstre
  - GitHub Advanced Security for leverandørkjede-beskyttelse
- **Avansert trusselmitigering**: Detaljerte sikkerhetskontroller for
  - Sesjonskapring med MCP-spesifikke angrepsscenarier og kryptografiske sesjons-ID-krav
  - Forvirret stedfortreder-problemer i MCP-proxy-scenarier med eksplisitte samtykkekrav
  - Token-passthrough-sårbarheter med obligatoriske valideringskontroller
- **Leverandørkjede-sikkerhet**: Utvidet AI-leverandørkjede-dekning inkludert grunnmodeller, embedding-tjenester, kontekstleverandører og tredjeparts-APIer
- **Grunnleggende sikkerhet**: Forbedret integrasjon med bedrifts sikkerhetsmønstre inkludert nulltillit-arkitektur og Microsoft sikkerhetsekosystem
- **Ressursorganisering**: Kategoriserte omfattende ressurslenker etter type (offisielle dokumenter, standarder, forskning, Microsoft-løsninger, implementeringsguider)

### Forbedringer i dokumentasjonskvalitet
- **Strukturerte læringsmål**: Forbedrede læringsmål med spesifikke, handlingsrettede resultater
- **Kryssreferanser**: Lagt til lenker mellom relaterte sikkerhets- og kjernebegrepsemner
- **Oppdatert informasjon**: Oppdatert alle datoreferanser og spesifikasjonslenker til gjeldende standarder
- **Implementeringsveiledning**: Lagt til spesifikke, handlingsrettede implementeringsretningslinjer gjennom begge seksjoner

## 16. juli 2025

### README og navigasjonsforbedringer
- Fullstendig redesignet pensum-navigasjon i README.md
- Erstattet `<details>`-tagger med mer tilgjengelig tabellbasert format
- Opprettet alternative layoutvalg i ny mappe "alternative_layouts"
- Lagt til kortbaserte, fanebaserte og akkordeonstil navigasjonseksempler
- Oppdatert repositoriumstrukturseksjon for å inkludere alle nyeste filer
- Forbedret "Hvordan bruke dette pensumet"-seksjonen med klare anbefalinger
- Oppdatert MCP-spesifikasjonslenker til å peke til korrekte URLer
- Lagt til seksjon for Context Engineering (5.14) i pensumstrukturen

### Oppdateringer i studieveiledning
- Fullstendig revidert studieveiledning for å samsvare med nåværende repositoriumstruktur
- Lagt til nye seksjoner for MCP-klienter og verktøy, og populære MCP-servere
- Oppdatert visuell pensumkart for å nøyaktig reflektere alle emner
- Forbedret beskrivelser av avanserte emner for å dekke alle spesialiserte områder
- Oppdatert casestudier-seksjon for å reflektere faktiske eksempler
- Lagt til denne omfattende endringsloggen

### Fellesskapsbidrag (06-CommunityContributions/)
- Lagt til detaljert informasjon om MCP-servere for bildegenerering
- Lagt til omfattende seksjon om bruk av Claude i VSCode
- Lagt til Cline terminalklient-oppsett og bruksanvisning
- Oppdatert MCP-klientseksjon for å inkludere alle populære klientvalg
- Forbedret bidragseksempler med mer nøyaktige kodeeksempler

### Avanserte emner (05-AdvancedTopics/)
- Organisert alle spesialiserte emnemapper med konsistent navngivning
- Lagt til materialer og eksempler for kontekstengineering
- Lagt til dokumentasjon for Foundry-agentintegrasjon
- Forbedret dokumentasjon for Entra ID sikkerhetsintegrasjon

## 11. juni 2025

### Første opprettelse
- Utgitt første versjon av MCP for Beginners-pensum
- Opprettet grunnstruktur for alle 10 hovedseksjoner
- Implementert visuelt pensumkart for navigasjon
- Lagt til innledende prøveprosjekter i flere programmeringsspråk

### Komme i gang (03-GettingStarted/)
- Opprettet første serverimplementeringseksempler
- Lagt til veiledning for klientutvikling
- Inkludert instruksjoner for LLM-klientintegrasjon
- Lagt til dokumentasjon for VS Code-integrasjon
- Implementert Server-Sent Events (SSE) servereksempler

### Kjernebegreper (01-CoreConcepts/)
- Lagt til detaljert forklaring av klient-server-arkitektur
- Opprettet dokumentasjon om nøkkelprotokollkomponenter
- Dokumentert meldingsmønstre i MCP

## 23. mai 2025

### Repositoriumstruktur
- Initialisert repositorium med grunnleggende mappestruktur
- Opprettet README-filer for hver hovedseksjon
- Satt opp oversettelsesinfrastruktur
- Lagt til bilde-ressurser og diagrammer

### Dokumentasjon
- Opprettet innledende README.md med oversikt over pensum
- Lagt til CODE_OF_CONDUCT.md og SECURITY.md
- Satt opp SUPPORT.md med veiledning for å få hjelp
- Opprettet foreløpig studieveiledningsstruktur

## 15. april 2025

### Planlegging og rammeverk
- Innledende planlegging for MCP for Beginners-pensum
- Definerte læringsmål og målgruppe
- Skisserte 10-seksjons struktur for pensum
- Utviklet konseptuelt rammeverk for eksempler og casestudier
- Opprettet innledende prototypeeksempler for nøkkelbegreper

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->