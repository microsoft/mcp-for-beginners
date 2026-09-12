# MCP Beveiliging: Uitgebreide Bescherming voor AI-Systemen

[![MCP Security Best Practices](../../../translated_images/nl/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Beveiliging is fundamenteel voor het ontwerp van AI-systemen, daarom geven we hier prioriteit aan als onze tweede sectie. Dit sluit aan bij Microsoft’s **Secure by Design** principe van de [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Het Model Context Protocol (MCP) brengt krachtige nieuwe mogelijkheden in AI-gestuurde toepassingen, maar introduceert ook unieke beveiligingsuitdagingen die verder gaan dan traditionele softwarerisico’s. MCP-systemen worden geconfronteerd met zowel gevestigde beveiligingskwesties (secure coding, least privilege, supply chain security) als nieuwe AI-specifieke bedreigingen waaronder promptinjectie, toolvergiftiging, sessie-overname, confused deputy-aanvallen, token passthrough-kwetsbaarheden en dynamische wijziging van bevoegdheden.

Deze les onderzoekt de meest kritische veiligheidsrisico’s bij MCP-implementaties—met aandacht voor authenticatie, autorisatie, overmatige permissies, indirecte promptinjectie, sessiebeveiliging, confused deputy-problemen, tokenbeheer en kwetsbaarheden in de supply chain. Je leert praktische controles en best practices om deze risico’s te mitigeren terwijl je gebruikmaakt van Microsoft-oplossingen zoals Prompt Shields, Azure Content Safety en GitHub Advanced Security om je MCP-implementatie te versterken.

## Leerdoelen

Aan het einde van deze les kun je:

- **MCP-specifieke Bedreigingen Identificeren**: Herkennen van unieke beveiligingsrisico’s in MCP-systemen zoals promptinjectie, toolvergiftiging, overmatige permissies, sessie-overname, confused deputy-problemen, token passthrough-kwetsbaarheden en risico’s in de supply chain
- **Beveiligingscontroles Toepassen**: Effectieve mitigaties implementeren inclusief robuuste authenticatie, least privilege-toegang, veilig tokenbeheer, sessiebeveiligingscontroles en verificatie van de supply chain
- **Microsoft Beveiligingsoplossingen Gebruiken**: Microsoft Prompt Shields, Azure Content Safety en GitHub Advanced Security begrijpen en inzetten ter bescherming van MCP workloads
- **Beveiliging van Tools Valideren**: Het belang van toolmetadata-validatie herkennen, monitoring van dynamische wijzigingen uitvoeren en verdedigen tegen indirecte promptinjectieaanvallen
- **Best Practices Integreren**: Gevestigde beveiligingsfundamenten (secure coding, server hardening, zero trust) combineren met MCP-specifieke controles voor uitgebreide bescherming

# MCP Beveiligingsarchitectuur & Controles

Moderne MCP-implementaties vereisen gelaagde beveiligingsbenaderingen die zowel traditionele softwarebeveiliging als AI-specifieke bedreigingen aanpakken. De snel evoluerende MCP-specificatie verfijnt zijn beveiligingscontroles voortdurend, waardoor betere integratie met bedrijfsbeveiligingsarchitecturen en gevestigde best practices mogelijk wordt.

Onderzoek uit het [Microsoft Digital Defense Report](https://aka.ms/mddr) toont aan dat **98% van de gerapporteerde inbreuken voorkomen kunnen worden door robuuze beveiligingshygiëne**. De meest effectieve beschermingsstrategie combineert fundamentele beveiligingspraktijken met MCP-specifieke controles—bewezen baseline beveiligingsmaatregelen blijven het meest impactvol in het verminderen van het totale beveiligingsrisico.

## Huidig Beveiligingslandschap

> **Opmerking:** Dit hoofdstuk combineert gevestigde MCP-beveiligingscontroles met de
> huidige **MCP Specificatie 2026-07-28** autorisatie richtlijnen. Raadpleeg altijd
> de actuele [MCP Specificatie](https://modelcontextprotocol.io/specification/2026-07-28/),
> de [MCP GitHub repository](https://github.com/modelcontextprotocol), en
> [documentatie met beveiligingsbest practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> bij de implementatie van beveiligingsgevoelige code.

> **Autorisatie-update:** MCP `2026-07-28` vereist dat cliënten de
> `iss` parameter in autorisatie-antwoorden valideren (RFC 9207) en geregistreerde
> referenties binden aan de uitgevende autorisatieserver. Dynamische clientregistratie
> wordt uitgefaseerd; nieuwe implementaties dienen Client ID Metadata Documenten te gebruiken.
> Zie [Wat is veranderd in MCP: De 2026-07-28 Specificatie](../01-CoreConcepts/mcp-2026-07-28.md)
> voor de volledige lijst autorisatie-aanpassingen.

## 🏔️ MCP Security Summit Workshop (Sherpa)

Voor **praktische beveiligingstraining** raden we sterk de **MCP Security Summit Workshop** (Sherpa) aan - een uitgebreide begeleide expeditie om MCP-servers in Microsoft Azure te beveiligen.

### Workshop Overzicht

De [MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) biedt praktische en uitvoerbare beveiligingstraining via een bewezen "kwetsbaar → exploit → fix → valideren" methodologie. Je zult:

- **Leren door te breken**: Kwetsbaarheden uit eerste hand ervaren door opzettelijk onveilige servers aan te vallen
- **Gebruikmaken van Azure-native Beveiliging**: Azure Entra ID, Key Vault, API Management en AI Content Safety inzetten
- **Verdedigingsin-diepte volgen**: Vooruitgang boeken via kampen met uitgebreide beveiligingslagen
- **OWASP-standaarden toepassen**: Elke techniek correspondeert met de [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Productiecode ontvangen**: Vertrekken met werkende, geteste implementaties

### De Expeditieroute

| Kamp | Focus | Gedekte OWASP-Risico’s |
|------|-------|---------------------|
| **Basiskamp** | MCP fundamentals & authenticatiekwetsbaarheden | MCP01, MCP07 |
| **Kamp 1: Identiteit** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Kamp 2: Gateway** | API Management, Private Endpoints, governance | MCP02, MCP06, MCP07, MCP09 |
| **Kamp 3: I/O Beveiliging** | Promptinjectie, PII-bescherming, content safety | MCP03, MCP05, MCP06, MCP10 |
| **Kamp 4: Monitoring** | Log Analytics, dashboards, detectie van bedreigingen | MCP04, MCP08 |
| **De Top** | Integratietest Red Team / Blue Team | Alles |

**Begin Vandaag**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 Beveiligingsrisico’s

De [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) beschrijft de tien meest kritische beveiligingsrisico’s voor MCP-implementaties:

| Risico | Beschrijving | Azure Mitigatie |
|------|-------------|------------------|
| **MCP01** | Token Mismanagement & Geheimen Blootstelling | Azure Key Vault, Managed Identity |
| **MCP02** | Privilege Escalatie via Scope Creep | RBAC, Conditional Access |
| **MCP03** | Toolvergiftiging | Toolvalidatie, integriteitsverificatie |
| **MCP04** | Software Supply Chain Aanvallen & Dependency Manipulatie | GitHub Advanced Security, dependency scanning |
| **MCP05** | Command Injection & Uitvoering | Inputvalidatie, sandboxing |
| **MCP06** | Intent Flow Subversion | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Onvoldoende Authenticatie & Autorisatie | Azure Entra ID, OAuth 2.1 met PKCE |
| **MCP08** | Gebrek aan Audit en Telemetrie | Azure Monitor, Application Insights |
| **MCP09** | Shadow MCP Servers | API Center governance, netwerkisolatie |
| **MCP10** | Contextinjectie & Overdreven Delen | Dataclassificatie, minimale blootstelling |

### Evolutie van MCP Authenticatie

De MCP-specificatie is aanzienlijk veranderd in zijn benadering van authenticatie en autorisatie:

- **Oorspronkelijke Aanpak**: Vroege specificaties vereisten dat ontwikkelaars eigen authenticatieservers implementeerden, waarbij MCP-servers fungeerden als OAuth 2.0 autorisatieservers die gebruikersauthenticatie direct beheerden
- **Huidige Standaard (`2026-07-28`)**: MCP-servers kunnen authenticatie delegeren
  aan externe identity providers zoals Microsoft Entra ID. Clients moeten ook
  voldoen aan de huidige eisen voor issuer-validatie en credential-binding.
- **Transport Layer Security**: Verbeterde ondersteuning voor beveiligde transportmechanismen met correcte authenticatiepatronen voor zowel lokale (STDIO) als externe (Streamable HTTP) verbindingen

## Authenticatie & Autorisatiebeveiliging

### Huidige Beveiligingsuitdagingen

Moderne MCP-implementaties ondervinden verschillende uitdagingen op het gebied van authenticatie en autorisatie:

### Risico’s & Bedreigingsvectoren

- **Verkeerd geconfigureerde Autorisatielogica**: Foutieve autorisatie-implementatie in MCP-servers kan gevoelige gegevens blootstellen en toegang verkeerd toepassen
- **OAuth Token Compromittering**: Diefstal van tokens van lokale MCP-servers maakt het voor aanvallers mogelijk zich voor te doen als servers en toegang te krijgen tot downstream diensten
- **Token Passthrough Kwetsbaarheden**: Onjuist tokenbeheer creëert beveiligingscontrole-omzeilingen en gebrek aan verantwoording
- **Overmatige Permissies**: MCP-servers met te veel rechten schenden het least privilege-principe en vergroten het aanvalsoppervlak

#### Token Passthrough: Een Kritiek Anti-Patroon

**Token passthrough is expliciet verboden** in de huidige MCP autorisatiespecificatie vanwege ernstige beveiligingsimplicaties:

##### Omzeiling van Beveiligingscontroles
- MCP-servers en downstream API’s implementeren kritieke beveiligingscontroles (rate limiting, request validatie, verkeersmonitoring) die afhangen van correcte tokenvalidatie
- Direct gebruik van tokens van cliënt naar API omzeilt deze essentiële bescherming en ondermijnt de beveiligingsarchitectuur

##### Verantwoordings- & Audit Uitdagingen  
- MCP-servers kunnen niet onderscheiden welke cliënten upstream-uitgegeven tokens gebruiken, waardoor audit trails worden verbroken
- Downstream resource-server logs tonen misleidende herkomst van aanvragen in plaats van werkelijke MCP-server tussenpersonen
- Incidentonderzoek en compliance-audits worden hierdoor aanzienlijk moeilijker

##### Gevaar voor Gegevensdiefstal
- Ongevalideerde tokenclaims stellen kwaadwillenden met gestolen tokens in staat MCP-servers als proxy’s voor datalekken te gebruiken
- Schendingen van trust boundaries maken ongeautoriseerde toegangs- en beveiligingscontrole-omzeilingen mogelijk

##### Multi-Service Aanvalsvectoren
- Gecompromitteerde tokens die door meerdere diensten worden geaccepteerd, maken laterale bewegingen tussen verbonden systemen mogelijk
- Vertrouwensrelaties tussen diensten kunnen worden geschonden als de herkomst van tokens niet geverifieerd kan worden

### Beveiligingscontroles & Mitigaties

**Kritieke Beveiligingseisen:**

> **VERPLICHT:** MCP-servers **MOETEN GEEN** tokens accepteren die niet expliciet zijn uitgegeven voor die MCP-server

#### Authenticatie & Autorisatiecontroles

- **Strenge Autorisatiecontrole**: Uitgebreide audits uitvoeren van de autorisatielogica van MCP-servers om te garanderen dat alleen bedoelde gebruikers en cliënten toegang hebben tot gevoelige resources
  - **Implementatiehandleiding**: [Azure API Management als authenticatiegateway voor MCP-servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identiteitsintegratie**: [Microsoft Entra ID gebruiken voor MCP-serverauthenticatie](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Veilig Tokenbeheer**: Implementeer [Microsofts tokenvalidatie- en lifecycle best practices](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Valideer dat token audience claims overeenkomen met MCP-serveridentiteit
  - Implementeer correcte tokenrotatie- en vervalbeleid
  - Voorkom token replay-aanvallen en ongeautoriseerd gebruik

- **Beveiligde Tokenopslag**: Beveilig tokenopslag met versleuteling, zowel in rust als in transit
  - **Best Practices**: [Richtlijnen voor veilige tokenopslag en encryptie](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementatie van Toegangscontrole

- **Principe van Least Privilege**: Verleen MCP-servers alleen de minimale rechten die nodig zijn voor de beoogde functionaliteit
  - Regelmatige controle en updates van permissies ter voorkoming van privilege creep
  - **Microsoft Documentatie**: [Veilige least-privileged toegang](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Implementeer fijnmazige roltoewijzingen
  - Beperk rollen nauwkeurig tot specifieke resources en acties
  - Vermijd brede of onnodige permissies die het aanvalsoppervlak vergroten

- **Continue Permissiebewaking**: Voer doorlopende audits en monitoring van toegang uit
  - Monitor gebruikspatronen van permissies voor anomalieën
  - Los excessieve of ongebruikte permissies snel op

## AI-Specifieke Beveiligingsbedreigingen

### Promptinjectie & Toolmanipulatie Aanvallen

Moderne MCP-implementaties worden geconfronteerd met geavanceerde AI-specifieke aanvalsvectoren die traditionele beveiligingsmaatregelen niet volledig kunnen adresseren:

#### **Indirecte Promptinjectie (Cross-Domain Prompt Injection)**

**Indirecte promptinjectie** is een van de meest kritieke kwetsbaarheden in MCP-compatibele AI-systemen. Aanvallers plaatsen kwaadaardige instructies in externe content—documenten, webpagina’s, e-mails of gegevensbronnen—die AI-systemen vervolgens verwerken als legitieme opdrachten.

**Aanvalsscenario’s:**
- **Documentgebaseerde Injectie**: Kwaadaardige instructies verborgen in verwerkte documenten die ongewenste AI-acties triggeren
- **Exploitatie van Webcontent**: Gecompromitteerde webpagina’s met ingebedde prompts die AI-gedrag manipuleren bij scraping
- **E-mailgebaseerde Aanvallen**: Kwaadaardige prompts in e-mails die AI-assistenten informatie laten lekken of ongeautoriseerde acties laten uitvoeren
- **Vervuiling van Gegevensbronnen**: Gecompromitteerde databases of API’s die besmette content aan AI-systemen leveren

**Reële Impact**: Deze aanvallen kunnen leiden tot datalekken, privacyschendingen, productie van schadelijke content en manipulatie van gebruikersinteracties. Voor een gedetailleerde analyse, zie [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/nl/prompt-injection.ed9fbfde297ca877.webp)

#### **Toolvergiftigingsaanvallen**

**Toolvergiftiging** richt zich op de metadata die MCP-tools definiëren en misbruikt hoe LLM’s toolbeschrijvingen en parameters interpreteren bij hun uitvoeringsbeslissingen.

**Aanvalsmethoden:**
- **Metadata-manipulatie**: Aanvallers injecteren kwaadaardige instructies in toolbeschrijvingen, parameterdefinities of gebruiksvoorbeelden
- **Onzichtbare Instructies**: Verborgen prompts in toolmetadata die door AI-modellen verwerkt worden maar onzichtbaar zijn voor menselijke gebruikers
- **Dynamische Toolwijziging ("Rug Pulls")**: Tools die door gebruikers zijn goedgekeurd, worden later gewijzigd om kwaadaardige acties uit te voeren zonder dat de gebruiker het merkt
- **Parameterinjectie**: Kwaadaardige content ingebed in toolparameterschema’s die het gedrag van het model beïnvloeden


**Gehoste Serverrisico's**: Externe MCP-servers brengen verhoogde risico's met zich mee omdat tooldefinities kunnen worden bijgewerkt na de initiële goedkeuring door de gebruiker, waardoor scenario's ontstaan waarin eerder veilige tools kwaadaardig worden. Voor een uitgebreide analyse, zie [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/nl/tool-injection.3b0b4a6b24de6bef.webp)

#### **Aanvullende AI-aanvalsvectoren**

- **Cross-Domain Prompt Injection (XPIA)**: Geavanceerde aanvallen die gebruikmaken van inhoud uit meerdere domeinen om beveiligingscontroles te omzeilen
- **Dynamische Capaciteitswijziging**: Wijzigingen in real-time aan toolcapaciteiten die ontkomen aan initiële beveiligingsbeoordelingen
- **Contextvenstergiftiging**: Aanvallen die grote contextvensters manipuleren om kwaadaardige instructies te verbergen
- **Modelverwarring Aanvallen**: Misbruik van modelbeperkingen om onvoorspelbaar of onveilig gedrag te veroorzaken


### Impact van AI-beveiligingsrisico’s

**Gevolgen met hoge impact:**
- **Data-exfiltratie**: Ongeautoriseerde toegang en diefstal van gevoelige bedrijfs- of persoonlijke gegevens
- **Privacyinbreuken**: Blootstelling van persoonlijk identificeerbare informatie (PII) en vertrouwelijke bedrijfsgegevens  
- **Systeemmanipulatie**: Onbedoelde wijzigingen aan kritieke systemen en workflows
- **Diefstal van Referenties**: Compromittering van authenticatietokens en service-referenties
- **Zijdelingse Beweging**: Gebruik van gecompromitteerde AI-systemen als pivots voor bredere netwerk aanvallen

### Microsoft AI-beveiligingsoplossingen

#### **AI Prompt Shields: Geavanceerde Bescherming tegen Injectie-aanvallen**

Microsoft **AI Prompt Shields** bieden uitgebreide verdediging tegen zowel directe als indirecte promptinjectie-aanvallen via meerdere beveiligingslagen:

##### **Kernbeschermingsmechanismen:**

1. **Geavanceerde Detectie & Filtering**
   - Machine learning-algoritmen en NLP-technieken detecteren kwaadaardige instructies in externe inhoud
   - Realtime analyse van documenten, webpagina's, e-mails en gegevensbronnen op ingesloten bedreigingen
   - Contextueel begrip van legitieme versus kwaadaardige promptpatronen

2. **Spotlighting Technieken**  
   - Onderscheid tussen vertrouwde systeemopdrachten en mogelijk gecompromitteerde externe invoer
   - Teksttransformatie-methoden die modelrelevantie verbeteren terwijl kwaadaardige inhoud wordt geïsoleerd
   - Helpt AI-systemen de juiste instructiehiërarchie te behouden en geïnjecteerde opdrachten te negeren

3. **Scheidingstekens & Data-markering Systemen**
   - Expliciete begrenzing tussen vertrouwde systeemberichten en externe invoertekst
   - Speciale markeringen benadrukken grenzen tussen vertrouwde en onbetrouwbare databronnen
   - Duidelijke scheiding voorkomt verwarring van instructies en ongeautoriseerde opdrachtuitvoering

4. **Continue Threat Intelligence**
   - Microsoft monitort continu opkomende aanvalspatronen en werkt verdedigingsmaatregelen bij
   - Proactief dreigingsjagen op nieuwe injectietechnieken en aanvalsvectoren
   - Regelmatige updates van beveiligingsmodellen om effectiviteit tegen evoluerende bedreigingen te behouden

5. **Azure Content Safety Integratie**
   - Onderdeel van de uitgebreide Azure AI Content Safety suite
   - Extra detectie voor jailbreak-pogingen, schadelijke inhoud en overtredingen van het beveiligingsbeleid
   - Geïntegreerde beveiligingscontroles over AI-applicatiecomponenten heen

**Implementatieresources**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/nl/prompt-shield.ff5b95be76e9c78c.webp)


## Geavanceerde MCP-beveiligingsbedreigingen

### Kwetsbaarheden bij Sessiekaping

**Sessiekaping** vormt een kritisch aanvalsvector in stateful MCP-implementaties waarbij onbevoegde partijen legitieme sessie-identificatoren verkrijgen en misbruiken om zich als cliënten voor te doen en ongeautoriseerde acties uit te voeren.

#### **Aanvalsscenario's & Risico's**

- **Sessiekaping Promptinjectie**: Aanvallers met gestolen sessie-ID's injecteren kwaadaardige gebeurtenissen in servers die sessiestatus delen, wat schadelijke acties kan triggeren of toegang kan geven tot gevoelige gegevens
- **Directe Identiteitsfraude**: Gestolen sessie-ID's maken directe MCP-serveraanroepen mogelijk die authenticatie omzeilen, waarbij aanvallers als legitieme gebruikers worden behandeld
- **Gecompromitteerde Hervatbare Stromen**: Aanvallers kunnen verzoeken voortijdig beëindigen, waardoor legitieme cliënten hervatten met mogelijk kwaadaardige inhoud

#### **Beveiligingsmaatregelen voor Sessiebeheer**

**Kritieke vereisten:**
- **Autorisatieverificatie**: MCP-servers die autorisatie implementeren **MOETEN** ALLE binnenkomende verzoeken verifiëren en **MOGEN NIET** vertrouwen op sessies voor authenticatie
- **Veilige Sessiegeneratie**: Gebruik cryptografisch veilige, niet-deterministische sessie-ID's die zijn gegenereerd met veilige willekeurige nummergeneratoren
- **Gebruikersspecifieke Binding**: Koppel sessie-ID's aan gebruikersspecifieke informatie met formats zoals `<user_id>:<session_id>` om misbruik over gebruikers heen te voorkomen
- **Levenscyclusbeheer van Sessies**: Implementeer correcte vervaldata, rotatie en invalidatie om kwetsbaarheidsvensters te beperken
- **Transportbeveiliging**: Verplichte HTTPS voor alle communicatie om onderschepping van sessie-ID's te voorkomen

### Probleem van de Verwarde Vertegenwoordiger (Confused Deputy)

Het **probleem van de verwarde vertegenwoordiger** ontstaat wanneer MCP-servers optreden als authenticatie-proxy's tussen cliënten en derden, waardoor mogelijkheden voor het omzeilen van autorisatie via misbruik van statische client-ID's ontstaan.

#### **Aanvalsmethoden & Risico’s**

- **Cookie-gebaseerde Toestemmingsomzeiling**: Vorige gebruikersauthenticatie creëert toestemmingscookies die aanvallers misbruiken via kwaadaardige autorisatieverzoeken met gefabriceerde redirect-URI's
- **Diefstal van Autorisatiecodes**: Bestaande toestemmingscookies kunnen autorisatieservers ertoe brengen toestemmingsschermen over te slaan en codes om te leiden naar endpoints die door aanvallers worden beheerd  
- **Ongeautoriseerde API-toegang**: Gestolen autorisatiecodes maken tokenuitwisseling en gebruikersimpostering mogelijk zonder expliciete goedkeuring

#### **Mitigatiestrategieën**

**Verplichte controles:**
- **Explíciete Toestemmingseisen**: MCP-proxyservers die statische client-ID's gebruiken **MOETEN** gebruikers voor elke dynamisch geregistreerde client toestemming vragen
- **OAuth 2.1 Beveiligingsimplementatie**: Volg actuele OAuth-beveiligingsbest practices inclusief PKCE (Proof Key for Code Exchange) voor alle autorisatieverzoeken
- **Strikte Clientvalidatie**: Implementeer rigoureuze validatie van redirect-URI's en clientidentificaties om misbruik te voorkomen

### Zwakke plekken bij Token Passthrough  

**Token passthrough** is een expliciete anti-patroon waarbij MCP-servers clienttokens accepteren zonder juiste validatie en deze doorsturen naar downstream API's, wat in strijd is met MCP-autorisatiespecificaties.

#### **Beveiligingsimplicaties**

- **Omzeiling van Controle**: Direct klant-naar-API tokengebruik omzeilt kritische limieten, validatie en monitoringscontroles
- **Corruptie van Audittrail**: Tokens uitgegeven upstream maken klantidentificatie onmogelijk, wat incidentonderzoek belemmert
- **Proxy-gebaseerde Data-exfiltratie**: Ongevalideerde tokens stellen kwaadwillenden in staat servers als proxy te gebruiken voor ongeautoriseerde data-access
- **Schending van Vertrouwensgrenzen**: Vertrouwensassumpties van downstream services kunnen worden geschonden als tokenherkomst niet geverifieerd kan worden
- **Uitbreiding van Multi-service Aanvallen**: Gecompromitteerde tokens die door meerdere services worden geaccepteerd maken zijdelingse beweging mogelijk

#### **Vereiste Beveiligingsmaatregelen**

**Ononderhandelbare vereisten:**
- **Tokenvalidatie**: MCP-servers **MOETEN NIET** tokens accepteren die niet expliciet voor de MCP-server zijn uitgegeven
- **Ontvangersverificatie**: Valideer altijd dat token audience claims overeenkomen met de identiteit van de MCP-server
- **Juiste Token Levenscyclus**: Implementeer kortdurende toegangstokens met veilige rotatiepraktijken


## Supply Chain Beveiliging voor AI-systemen

Supply chain-beveiliging is geëvolueerd voorbij traditionele softwareafhankelijkheden en omvat nu het hele AI-ecosysteem. Moderne MCP-implementaties moeten rigoureus alle AI-gerelateerde componenten verifiëren en monitoren, aangezien elk potentiële kwetsbaarheden introduceert die de systeeme integriteit kunnen ondermijnen.

### Uitgebreide AI-supply chain componenten

**Traditionele softwareafhankelijkheden:**
- Open-source bibliotheken en frameworks
- Containerafbeeldingen en basis systemen  
- Ontwikkeltools en build pipelines
- Infrastructuurcomponenten en -diensten

**AI-specifieke supply chain elementen:**
- **Foundation Models**: Voorgetrainde modellen van diverse leveranciers die herkomstverificatie vereisen
- **Embedding Services**: Externe vectorisatie- en semantische zoekservices
- **Contextproviders**: Gegevensbronnen, kennisbanken en documentrepositories  
- **API's van derden**: Externe AI-diensten, ML-pijplijnen en dataverwerkende eindpunten
- **Model Artefacten**: Gewichten, configuraties en fijn afgestelde modelvarianten
- **Trainingsdatabronnen**: Databestanden gebruikt voor modeltraining en -fijnstelling

### Omvattende supply chain-beveiligingsstrategie

#### **Componentverificatie & Vertrouwen**
- **Herkomstvalidatie**: Verifieer de oorsprong, licentie en integriteit van alle AI-componenten vóór integratie
- **Beveiligingsbeoordeling**: Voer kwetsbaarheidsscans en beveiligingsreviews uit voor modellen, gegevensbronnen en AI-diensten
- **Reputatie-analyse**: Evalueer de beveiligingshistorie en praktijken van AI-dienstverleners
- **Compliancecontrole**: Zorg dat alle componenten voldoen aan organisatorische beveiligings- en regelgevingsvereisten

#### **Veilige Deploy-pijplijnen**  
- **Geautomatiseerde CI/CD beveiliging**: Integreer beveiligingsscanning in geautomatiseerde deploy-pijplijnen
- **Integriteitscontrole van Artefacten**: Implementeer cryptografische verificatie van alle gedeployde artefacten (code, modellen, configuraties)
- **Gefaseerde Deployments**: Gebruik progressieve implementatiestrategieën met beveiligingsvalidatie in elke fase
- **Vertrouwde Artefactrepositories**: Implementeer alleen vanuit geverifieerde, beveiligde artefactregistraties en -repos

#### **Continue Monitoring & Response**
- **Dependency Scanning**: Voortdurende monitoring op kwetsbaarheden van alle software- en AI-componentafhankelijkheden
- **Modelmonitoring**: Continue beoordeling van modelgedrag, prestatie-afwijking en beveiligingsanomaliën
- **Servicegezondheidstracking**: Monitor externe AI-diensten op beschikbaarheid, beveiligingsincidenten en beleidswijzigingen
- **Integratie van Threat Intelligence**: Verwerk dreigingsfeeds specifiek voor AI- en ML-beveiligingsrisico's

#### **Toegangscontrole & Least Privilege**
- **Rechten op componentniveau**: Beperk toegang tot modellen, gegevens en diensten op basis van zakelijke noodzaak
- **Serviceaccountbeheer**: Implementeer toegewijde serviceaccounts met minimale vereiste rechten
- **Netwerksegmentatie**: Isoleer AI-componenten en beperk netwerktoegang tussen diensten
- **API Gateway Controles**: Gebruik gecentraliseerde API-gateways voor controle en monitoring van toegang tot externe AI-diensten

#### **Incidentrespons & Herstel**
- **Snelle Responsprocedures**: Vastgestelde processen voor patching of vervanging van gecompromitteerde AI-componenten
- **Rotatie van Referenties**: Geautomatiseerde systemen voor het roteren van geheimen, API-sleutels en service-referenties
- **Rollback-mogelijkheden**: Mogelijkheid om snel terug te keren naar eerder bekende goede versies van AI-componenten
- **Herstel na Supply Chain-breuk**: Specifieke procedures voor reageren op compromittering van upstream AI-diensten

### Microsoft-beveiligingstools & Integratie

**GitHub Advanced Security** biedt uitgebreide bescherming van de supply chain inclusief:
- **Geheime Scanning**: Automatische detectie van referenties, API-sleutels en tokens in repositories
- **Dependency Scanning**: Kwetsbaarheidsbeoordeling voor open-source afhankelijkheden en bibliotheken
- **CodeQL Analyse**: Statische code-analyse voor beveiligingskwetsbaarheden en codeerproblemen
- **Supply Chain Inzichten**: Inzicht in gezondheid en beveiligingsstatus van afhankelijkheden

**Integratie Azure DevOps & Azure Repos:**
- Naadloze integratie van beveiligingsscans in Microsoft ontwikkelplatformen
- Geautomatiseerde beveiligingscontroles in Azure Pipelines voor AI-werklasten
- Beleidsafdwinging voor veilige AI-componentdeployments

**Microsoft's interne praktijken:**
Microsoft implementeert uitgebreide supply chain-beveiligingspraktijken voor alle producten. Lees over bewezen benaderingen in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Beste Praktijken voor Foundation Security

MCP-implementaties erven en bouwen voort op de bestaande beveiligingshouding van uw organisatie. Het versterken van fundamentele beveiligingspraktijken verbetert aanzienlijk de algehele beveiliging van AI-systemen en MCP-implementaties.

### Kernfundamenten van beveiliging

#### **Veilige ontwikkelpraktijken**
- **OWASP-compliance**: Bescherming tegen [OWASP Top 10](https://owasp.org/www-project-top-ten/) kwetsbaarheden in webapplicaties
- **AI-specifieke bescherming**: Implementeer controles voor [OWASP Top 10 voor LLM's](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Beheer van veilige geheimen**: Gebruik toegewijde kluizen voor tokens, API-sleutels en gevoelige configuratiegegevens
- **End-to-end encryptie**: Implementeer veilige communicatie over alle applicatiecomponenten en gegevensstromen
- **Invoervalidatie**: Strikte validatie van alle gebruikersinvoer, API-parameters en gegevensbronnen

#### **Verharding van infrastructuur**
- **Multi-Factor Authenticatie**: Verplichte MFA voor alle administratieve en serviceaccounts
- **Patchbeheer**: Geautomatiseerde, tijdige patching voor besturingssystemen, frameworks en afhankelijkheden  
- **Integratie van identiteitsproviders**: Gecentraliseerd identiteitsbeheer via enterprise identity providers (Microsoft Entra ID, Active Directory)
- **Netwerksegmentatie**: Logische isolatie van MCP-componenten om potentiële zijdelingse beweging te beperken
- **Principe van minste privileges**: Minimale vereiste rechten voor alle systeemcomponenten en accounts

#### **Beveiligingsmonitoring & Detectie**
- **Uitgebreide logging**: Gedetailleerde logging van AI-applicatieactiviteiten, inclusief MCP client-server interacties
- **SIEM-integratie**: Gecentraliseerd security informatie en event management voor anomaliedetectie
- **Gedragsanalyse**: AI-gestuurde monitoring voor het detecteren van ongebruikelijke patronen in systeem- en gebruikersgedrag
- **Threat Intelligence**: Integratie van externe dreigingsfeeds en indicatoren van compromittering (IOCs)
- **Incidentrespons**: Goed gedefinieerde procedures voor detectie, respons en herstel van beveiligingsincidenten

#### **Zero Trust Architectuur**
- **Nooit vertrouwen, altijd verifiëren**: Continue verificatie van gebruikers, apparaten en netwerkverbindingen
- **Microsegmentatie**: Gedetailleerde netwerkcontroles die individuele workloads en diensten isoleren
- **Identiteitsgerichte beveiliging**: Beveiligingsbeleid gebaseerd op geverifieerde identiteiten in plaats van netwerk locatie
- **Continue risico-evaluatie**: Dynamische beoordeling van beveiligingshouding op basis van huidige context en gedrag
- **Conditionele toegang**: Toegangscontrole die zich aanpast op basis van risicofactoren, locatie en apparaatvertrouwen

### Patroon voor integratie binnen organisaties

#### **Integratie met het Microsoft beveiligingsecosysteem**
- **Microsoft Defender for Cloud**: Uitgebreid cloudbeveiligingspostuurbeheer
- **Azure Sentinel**: Cloud-native SIEM- en SOAR-mogelijkheden voor bescherming van AI-werklasten
- **Microsoft Entra ID**: Enterprise identiteits- en toegangsbeheer met beleidsregels voor conditionele toegang
- **Azure Key Vault**: Gecentraliseerd geheimenbeheer met hardware security module (HSM) ondersteuning
- **Microsoft Purview**: Gegevensbeheer en naleving voor AI-gegevensbronnen en workflows

#### **Compliance & Governance**
- **Regelgeving Naleving**: Zorg dat MCP-implementaties voldoen aan branchespecifieke compliancevereisten (GDPR, HIPAA, SOC 2)

- **Gegevensclassificatie**: Juiste categorisering en verwerking van gevoelige gegevens behandeld door AI-systemen
- **Audit Trails**: Uitgebreide logboekregistratie voor naleving van regelgeving en forensisch onderzoek
- **Privacy Controles**: Implementatie van privacy-by-design principes in AI-systeemarchitectuur
- **Wijzigingsbeheer**: Formele processen voor beveiligingsbeoordelingen van AI-systeemwijzigingen

Deze fundamentele praktijken creëren een robuuste beveiligingsbasis die de effectiviteit van MCP-specifieke beveiligingscontroles verhoogt en uitgebreide bescherming biedt voor AI-gedreven toepassingen.

## Belangrijke Beveiligingsinzichten

- **Gelaagde Beveiligingsaanpak**: Combineer fundamentele beveiligingspraktijken (veilig coderen, minste privileges, verificatie van toeleveringsketen, continue monitoring) met AI-specifieke controles voor uitgebreide bescherming

- **AI-specifiek Dreigingslandschap**: MCP-systemen worden geconfronteerd met unieke risico's waaronder promptinjectie, vergiftiging van tools, sessiekaping, confused deputy-problemen, kwetsbaarheden bij token-passthrough en buitensporige machtigingen die gespecialiseerde mitigaties vereisen

- **Authenticatie & Autorisatie Uitmuntendheid**: Implementeer robuuste authenticatie met externe identiteitsproviders (Microsoft Entra ID), handhaaf juiste tokenvalidatie en accepteer nooit tokens die niet expliciet zijn uitgegeven voor uw MCP-server

- **AI-aanvalpreventie**: Zet Microsoft Prompt Shields en Azure Content Safety in om te verdedigen tegen indirecte promptinjectie en vergiftiging van tools, terwijl u metadata van tools valideert en monitort op dynamische wijzigingen

- **Sessie- & Transportbeveiliging**: Gebruik cryptografisch veilige, niet-deterministische sessie-ID’s gebonden aan gebruikersidentiteiten, implementeer goed sessiebeheer en gebruik nooit sessies voor authenticatie

- **OAuth Beveiligingsbest Practices**: Voorkom confused deputy-aanvallen via expliciete gebruikersconsent voor dynamisch geregistreerde clients, juiste implementatie van OAuth 2.1 met PKCE, en strikte validatie van redirect-URI’s  

- **Token Beveiligingsprincipes**: Vermijd token-passthrough anti-patronen, valideer token audience claims, implementeer kortdurende tokens met veilige rotatie en onderhoud duidelijke vertrouwensgrenzen

- **Uitgebreide Beveiliging van de Toeleveringsketen**: Behandel alle AI-ecosysteemcomponenten (modellen, embeddings, contextproviders, externe API’s) met dezelfde beveiligingsdiscipline als traditionele softwareafhankelijkheden

- **Continue Evolutie**: Blijf op de hoogte van snel evoluerende MCP-specificaties, draag bij aan beveiligingscommunity-standaarden en handhaaf aanpasbare beveiligingshoudingen naarmate het protocol zich ontwikkelt

- **Microsoft Beveiligingsintegratie**: Maak gebruik van Microsofts uitgebreide beveiligingsecosysteem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) voor verbeterde bescherming bij MCP-implementaties

## Uitgebreide Bronnen

### **Officiële MCP Beveiligingsdocumentatie**
- [MCP Specificatie (Huidig: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Beveiligingsbest Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Autorisatiespecificatie](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **OWASP MCP Beveiligingsbronnen**
- [OWASP MCP Azure Beveiligingsgids](https://microsoft.github.io/mcp-azure-security-guide/) - Uitgebreide OWASP MCP Top 10 met Azure-implementatierichtlijnen
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Officiële OWASP MCP beveiligingsrisico’s
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktische beveiligingstraining voor MCP op Azure

### **Beveiligingsstandaarden & Best Practices**
- [OAuth 2.0 Beveiligingsbest Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Webapplicatiebeveiliging](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 voor Grote Taalmodellen](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **AI Beveiligingsonderzoek & Analyse**
- [Promptinjectie in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Toolvergiftigingsaanvallen (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Beveiligingsonderzoeksbriefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Beveiligingsoplossingen**
- [Microsoft Prompt Shields Documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Beveiliging](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Tokenbeheer Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementatiegidsen & Tutorials**
- [Azure API Management als MCP Authenticatiegateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authenticatie met MCP-servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Veilige Tokenopslag en Encryptie (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Beveiliging van de Toeleveringsketen**
- [Azure DevOps Beveiliging](https://azure.microsoft.com/products/devops)
- [Azure Repos Beveiliging](https://azure.microsoft.com/products/devops/repos/)
- [Journey van Microsoft Supply Chain Security](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Aanvullende Beveiligingsdocumentatie**

Raadpleeg voor uitgebreide beveiligingsrichtlijnen deze gespecialiseerde documenten in deze sectie:

- **[CIMD en DCR Autorisatiesample](./samples/cimd-dcr-auth/README.md)** - Uitvoerbare TypeScript MCP ‘2026-07-28’ resource server die voorkeurs Client ID Metadata Documenten vergelijkt met verouderde Dynamic Client Registration fallback
- **[MCP Beveiligingsbest Practices](./mcp-security-best-practices.md)** - Volledige beveiligingsbest practices voor MCP-implementaties
- **[Azure Content Safety Implementatie](./azure-content-safety-implementation.md)** - Praktische implementatievoorbeelden voor Azure Content Safety-integratie  
- **[MCP Beveiligingscontroles](./mcp-security-controls.md)** - Laatste beveiligingscontroles en technieken voor MCP-implementaties
- **[MCP Best Practices Snelreferentie](./mcp-best-practices.md)** - Snelreferentiegids voor essentiële MCP-beveiligingspraktijken
- **[BlueHat 2026: De toekomst van AI beveiligen: MCP beveiligen met defense in depth-patronen](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Defense-in-depth patronen van het Microsoft Security Response Center (MSRC)

### **Praktijkgerichte Beveiligingstraining**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Uitgebreide praktijkgerichte workshop voor het beveiligen van MCP-servers in Azure met progressieve kampen van Base Camp tot Summit
- **[OWASP MCP Azure Beveiligingsgids](https://microsoft.github.io/mcp-azure-security-guide/)** - Referentiearchitectuur en implementatierichtlijnen voor alle OWASP MCP Top 10-risico’s

---

## Wat Nu

Volgende: [Hoofdstuk 3: Aan de slag](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->