# MCP-beveiliging: Uitgebreide bescherming voor AI-systemen

[![MCP Security Best Practices](../../../translated_images/nl/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Beveiliging is fundamenteel voor het ontwerp van AI-systemen, daarom geven we er prioriteit aan als onze tweede sectie. Dit sluit aan bij Microsofts **Secure by Design**-principe uit de [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Het Model Context Protocol (MCP) brengt krachtige nieuwe mogelijkheden naar AI-gedreven applicaties, terwijl het unieke beveiligingsuitdagingen introduceert die verder gaan dan traditionele softwarerisico’s. MCP-systemen worden geconfronteerd met zowel gevestigde beveiligingsproblemen (veilig coderen, minste privilege, beveiliging van de toeleveringsketen) als nieuwe AI-specifieke bedreigingen, waaronder promptinjectie, toolvergiftiging, sessiekaping, confused deputy-aanvallen, kwetsbaarheden bij token-passthrough en dynamische wijziging van mogelijkheden.

Deze les behandelt de meest kritieke beveiligingsrisico’s in MCP-implementaties—met aandacht voor authenticatie, autorisatie, overmatige permissies, indirecte promptinjectie, sessiebeveiliging, confused deputy-problemen, tokenbeheer en kwetsbaarheden in de toeleveringsketen. Je leert toepasbare controles en best practices om deze risico’s te beperken, terwijl je Microsoft-oplossingen zoals Prompt Shields, Azure Content Safety en GitHub Advanced Security inzet om je MCP-implementatie te versterken.

## Leerdoelen

Aan het einde van deze les kun je:

- **MCP-specifieke bedreigingen identificeren**: Unieke beveiligingsrisico’s in MCP-systemen herkennen, waaronder promptinjectie, toolvergiftiging, overmatige permissies, sessiekaping, confused deputy-problemen, token-passthrough kwetsbaarheden en risico’s in de toeleveringsketen
- **Beveiligingscontroles toepassen**: Effectieve mitigaties implementeren, waaronder robuuste authenticatie, toegang op basis van minste privilege, veilig tokenbeheer, sessiebeveiligingscontroles en verificatie van de toeleveringsketen
- **Microsoft-beveiligingsoplossingen benutten**: Microsoft Prompt Shields, Azure Content Safety en GitHub Advanced Security begrijpen en inzetten voor bescherming van MCP-workloads
- **Toolbeveiliging valideren**: Het belang van validatie van toolmetadata, monitoring van dynamische wijzigingen en verdediging tegen indirecte promptinjectie-aanvallen herkennen
- **Best practices integreren**: Gevestigde beveiligingsfundamenten (veilig coderen, serverhardening, zero trust) combineren met MCP-specifieke controles voor uitgebreide bescherming

# MCP-beveiligingsarchitectuur & -controles

Moderne MCP-implementaties vereisen gelaagde beveiligingsbenaderingen die zowel traditionele softwarebeveiliging als AI-specifieke bedreigingen aanpakken. De snel evoluerende MCP-specificatie blijft zijn beveiligingscontroles verfijnen, waardoor betere integratie met enterprise-beveiligingsarchitecturen en gevestigde best practices mogelijk wordt.

Onderzoek uit het [Microsoft Digital Defense Report](https://aka.ms/mddr) toont aan dat **98% van de gerapporteerde inbreuken voorkomen zou kunnen worden door robuuste beveiligingshygiëne**. De meest effectieve beschermingsstrategie combineert fundamentele beveiligingspraktijken met MCP-specifieke controles—bewezen basisbeveiligingsmaatregelen blijven het meest impactvol in het verminderen van het algehele beveiligingsrisico.

## Huidig beveiligingslandschap

> **Opmerking:** Deze informatie weerspiegelt MCP-beveiligingsnormen per **18 december 2025**. Het MCP-protocol blijft zich snel ontwikkelen en toekomstige implementaties kunnen nieuwe authenticatiepatronen en verbeterde controles introduceren. Raadpleeg altijd de actuele [MCP-specificatie](https://spec.modelcontextprotocol.io/), [MCP GitHub-repository](https://github.com/modelcontextprotocol) en [documentatie over beveiligingsbest practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) voor de laatste richtlijnen.

### Evolutie van MCP-authenticatie

De MCP-specificatie is aanzienlijk geëvolueerd in zijn aanpak van authenticatie en autorisatie:

- **Oorspronkelijke aanpak**: Vroege specificaties vereisten dat ontwikkelaars eigen authenticatieservers implementeerden, waarbij MCP-servers fungeerden als OAuth 2.0 Authorization Servers die gebruikersauthenticatie direct beheerden
- **Huidige standaard (2025-11-25)**: Bijgewerkte specificatie staat toe dat MCP-servers authenticatie delegeren aan externe identiteitsproviders (zoals Microsoft Entra ID), wat de beveiligingshouding verbetert en de implementatiecomplexiteit vermindert
- **Transportlaagbeveiliging**: Verbeterde ondersteuning voor veilige transportmechanismen met juiste authenticatiepatronen voor zowel lokale (STDIO) als externe (Streamable HTTP) verbindingen

## Authenticatie- & autorisatiebeveiliging

### Huidige beveiligingsuitdagingen

Moderne MCP-implementaties worden geconfronteerd met diverse uitdagingen op het gebied van authenticatie en autorisatie:

### Risico’s & bedreigingsvectoren

- **Foutief geconfigureerde autorisatielogica**: Onjuiste autorisatie-implementatie in MCP-servers kan gevoelige gegevens blootstellen en toegang verkeerd toepassen
- **OAuth-tokencompromis**: Diefstal van tokens van lokale MCP-servers stelt aanvallers in staat zich voor te doen als servers en toegang te krijgen tot downstream-services
- **Token-passthrough kwetsbaarheden**: Onjuist tokenbeheer creëert beveiligingscontrole-omzeilingen en verantwoordingslacunes
- **Overmatige permissies**: Overbevoegde MCP-servers schenden het principe van minste privilege en vergroten het aanvalsoppervlak

#### Token-passthrough: een kritisch anti-patroon

**Token-passthrough is expliciet verboden** in de huidige MCP-autorisatiespecificatie vanwege ernstige beveiligingsimplicaties:

##### Omzeiling van beveiligingscontroles
- MCP-servers en downstream-API’s implementeren kritieke beveiligingscontroles (rate limiting, verzoekvalidatie, verkeersmonitoring) die afhankelijk zijn van correcte tokenvalidatie
- Direct gebruik van tokens van client naar API omzeilt deze essentiële beschermingen en ondermijnt de beveiligingsarchitectuur

##### Verantwoordings- & audituitdagingen  
- MCP-servers kunnen niet onderscheiden welke clients tokens gebruiken die upstream zijn uitgegeven, waardoor auditsporen verbroken worden
- Logs van downstream resource-servers tonen misleidende verzoekherkomst in plaats van de daadwerkelijke MCP-server als tussenpersoon
- Incidentonderzoek en compliance-audits worden aanzienlijk moeilijker

##### Risico’s op datalekken
- Ongeldige tokenclaims stellen kwaadwillenden met gestolen tokens in staat MCP-servers als proxy’s voor datalekken te gebruiken
- Vertrouwensgrensschendingen maken ongeautoriseerde toegangspatronen mogelijk die bedoelde beveiligingscontroles omzeilen

##### Multi-service aanvalsvectoren
- Gecompromitteerde tokens die door meerdere services worden geaccepteerd, maken laterale bewegingen over verbonden systemen mogelijk
- Vertrouwensveronderstellingen tussen services kunnen worden geschonden wanneer tokenherkomst niet kan worden geverifieerd

### Beveiligingscontroles & mitigaties

**Kritieke beveiligingseisen:**

> **VERPLICHT**: MCP-servers **MOGEN GEEN** tokens accepteren die niet expliciet voor de MCP-server zijn uitgegeven

#### Authenticatie- & autorisatiecontroles

- **Grondige autorisatiebeoordeling**: Voer uitgebreide audits uit van de autorisatielogica van MCP-servers om te waarborgen dat alleen bedoelde gebruikers en clients toegang hebben tot gevoelige bronnen
  - **Implementatiehandleiding**: [Azure API Management als authenticatiegateway voor MCP-servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identiteitsintegratie**: [Gebruik van Microsoft Entra ID voor MCP-serverauthenticatie](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Veilig tokenbeheer**: Implementeer [Microsofts beste praktijken voor tokenvalidatie en levenscyclus](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Valideer dat token audience claims overeenkomen met de identiteit van de MCP-server
  - Implementeer correcte tokenrotatie- en vervalbeleid
  - Voorkom token replay-aanvallen en ongeautoriseerd gebruik

- **Beschermde tokenopslag**: Beveilig tokenopslag met encryptie in rust en tijdens transport
  - **Best practices**: [Richtlijnen voor veilige tokenopslag en encryptie](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementatie van toegangscontrole

- **Principe van minste privilege**: Verleen MCP-servers alleen de minimale permissies die nodig zijn voor de beoogde functionaliteit
  - Regelmatige herziening en bijwerking van permissies om privilege creep te voorkomen
  - **Microsoft-documentatie**: [Veilige toegang met minste privilege](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Implementeer fijnmazige roltoewijzingen
  - Beperk rollen strikt tot specifieke bronnen en acties
  - Vermijd brede of onnodige permissies die het aanvalsoppervlak vergroten

- **Continue permissiemonitoring**: Voer doorlopende toegangsaudits en monitoring uit
  - Monitor gebruikspatronen van permissies op anomalieën
  - Los overmatige of ongebruikte privileges snel op

## AI-specifieke beveiligingsbedreigingen

### Promptinjectie- & toolmanipulatie-aanvallen

Moderne MCP-implementaties worden geconfronteerd met geavanceerde AI-specifieke aanvalsvectoren die traditionele beveiligingsmaatregelen niet volledig kunnen adresseren:

#### **Indirecte promptinjectie (Cross-Domain Prompt Injection)**

**Indirecte promptinjectie** is een van de meest kritieke kwetsbaarheden in MCP-compatibele AI-systemen. Aanvallers verbergen kwaadaardige instructies in externe content—documenten, webpagina’s, e-mails of databronnen—die AI-systemen vervolgens verwerken als legitieme opdrachten.

**Aanvalsscenario’s:**
- **Documentgebaseerde injectie**: Kwaadaardige instructies verborgen in verwerkte documenten die onbedoelde AI-acties triggeren
- **Misbruik van webinhoud**: Gecompromitteerde webpagina’s met ingebedde prompts die AI-gedrag manipuleren bij scraping
- **E-mailgebaseerde aanvallen**: Kwaadaardige prompts in e-mails die AI-assistenten doen lekken of ongeautoriseerde acties laten uitvoeren
- **Verontreiniging van databronnen**: Gecompromitteerde databases of API’s die besmette content aan AI-systemen leveren

**Reële impact**: Deze aanvallen kunnen leiden tot datalekken, privacyschendingen, generatie van schadelijke content en manipulatie van gebruikersinteracties. Voor gedetailleerde analyse, zie [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/nl/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Toolvergiftiging-aanvallen**

**Toolvergiftiging** richt zich op de metadata die MCP-tools definieert, waarbij wordt misbruikt hoe LLM’s toolbeschrijvingen en parameters interpreteren om uitvoeringsbeslissingen te nemen.

**Aanvalsmethoden:**
- **Manipulatie van metadata**: Aanvallers injecteren kwaadaardige instructies in toolbeschrijvingen, parameterdefinities of gebruiksvoorbeelden
- **Onzichtbare instructies**: Verborgen prompts in toolmetadata die door AI-modellen worden verwerkt maar onzichtbaar zijn voor menselijke gebruikers
- **Dynamische toolwijziging ("Rug Pulls")**: Tools die door gebruikers zijn goedgekeurd worden later aangepast om kwaadaardige acties uit te voeren zonder dat gebruikers dit merken
- **Parameterinjectie**: Kwaadaardige inhoud ingebed in toolparameterschema’s die het modelgedrag beïnvloeden

**Risico’s bij gehoste servers**: Externe MCP-servers brengen verhoogde risico’s met zich mee omdat tooldefinities na initiële gebruikersgoedkeuring kunnen worden bijgewerkt, waardoor scenario’s ontstaan waarin eerder veilige tools kwaadaardig worden. Voor uitgebreide analyse, zie [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/nl/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Aanvullende AI-aanvalsvectoren**

- **Cross-Domain Prompt Injection (XPIA)**: Geavanceerde aanvallen die content uit meerdere domeinen gebruiken om beveiligingscontroles te omzeilen
- **Dynamische wijziging van mogelijkheden**: Real-time aanpassingen van toolmogelijkheden die initiële beveiligingsbeoordelingen ontlopen
- **Context window poisoning**: Aanvallen die grote contextvensters manipuleren om kwaadaardige instructies te verbergen
- **Modelverwarring-aanvallen**: Misbruik van modelbeperkingen om onvoorspelbaar of onveilig gedrag te creëren

### Impact van AI-beveiligingsrisico’s

**Gevolgen met hoge impact:**
- **Datalekken**: Ongeautoriseerde toegang en diefstal van gevoelige bedrijfs- of persoonlijke gegevens
- **Privacyschendingen**: Blootstelling van persoonlijk identificeerbare informatie (PII) en vertrouwelijke bedrijfsdata  
- **Systeemmanipulatie**: Onbedoelde wijzigingen aan kritieke systemen en workflows
- **Diefstal van referenties**: Compromittering van authenticatietokens en service-referenties
- **Laterale beweging**: Gebruik van gecompromitteerde AI-systemen als pivot voor bredere netwerk-aanvallen

### Microsoft AI-beveiligingsoplossingen

#### **AI Prompt Shields: Geavanceerde bescherming tegen injectie-aanvallen**

Microsoft **AI Prompt Shields** bieden uitgebreide verdediging tegen zowel directe als indirecte promptinjectie-aanvallen via meerdere beveiligingslagen:

##### **Kernbeschermingsmechanismen:**

1. **Geavanceerde detectie & filtering**
   - Machine learning-algoritmen en NLP-technieken detecteren kwaadaardige instructies in externe content
   - Real-time analyse van documenten, webpagina’s, e-mails en databronnen op ingebedde bedreigingen
   - Contextueel begrip van legitieme versus kwaadaardige promptpatronen

2. **Spotlighting-technieken**  
   - Onderscheidt vertrouwde systeeminstructies van mogelijk gecompromitteerde externe input
   - Teksttransformatietechnieken die modelrelevantie verbeteren en kwaadaardige content isoleren
   - Helpt AI-systemen de juiste instructiehiërarchie te behouden en geïnjecteerde commando’s te negeren

3. **Delimiter- & datamarkering-systemen**
   - Expliciete grensdefinitie tussen vertrouwde systeemberichten en externe invoertekst
   - Speciale markeringen benadrukken grenzen tussen vertrouwde en onbetrouwbare databronnen
   - Duidelijke scheiding voorkomt instructieverwarring en ongeautoriseerde uitvoering van commando’s

4. **Continue dreigingsinformatie**
   - Microsoft monitort continu opkomende aanvalspatronen en werkt verdedigingen bij
   - Proactief dreigingsonderzoek naar nieuwe injectietechnieken en aanvalsvectoren
   - Regelmatige updates van beveiligingsmodellen om effectiviteit tegen evoluerende bedreigingen te behouden

5. **Integratie met Azure Content Safety**
   - Onderdeel van de uitgebreide Azure AI Content Safety-suite
   - Extra detectie voor jailbreakpogingen, schadelijke content en overtredingen van beveiligingsbeleid
   - Geünificeerde beveiligingscontroles over AI-applicatiecomponenten

**Implementatieresources**: [Microsoft Prompt Shields Documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/nl/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Geavanceerde MCP-beveiligingsbedreigingen

### Kwetsbaarheden voor sessiekaping

**Sessiekaping** is een kritieke aanvalsvector in stateful MCP-implementaties waarbij onbevoegden legitieme sessie-identificaties verkrijgen en misbruiken om zich voor te doen als clients en ongeautoriseerde acties uit te voeren.

#### **Aanvalsscenario’s & risico’s**

- **Sessiekaping promptinjectie**: Aanvallers met gestolen sessie-ID’s injecteren kwaadaardige gebeurtenissen in servers die sessiestatus delen, wat schadelijke acties kan triggeren of toegang tot gevoelige data kan geven
- **Directe imitatie**: Gestolen sessie-ID’s maken directe MCP-serveraanroepen mogelijk die authenticatie omzeilen en aanvallers als legitieme gebruikers behandelen
- **Gecompromitteerde hervatbare streams**: Aanvallers kunnen verzoeken voortijdig beëindigen, waardoor legitieme clients mogelijk met kwaadaardige content hervatten

#### **Beveiligingscontroles voor sessiebeheer**

**Kritieke vereisten:**
- **Autorisatieverificatie**: MCP-servers die autorisatie implementeren **MOETEN** ALLE inkomende verzoeken verifiëren en **MOGEN NIET** vertrouwen op sessies voor authenticatie  
- **Veilige sessiegeneratie**: Gebruik cryptografisch veilige, niet-deterministische sessie-ID's die worden gegenereerd met veilige willekeurige nummergeneratoren  
- **Gebruikersspecifieke binding**: Koppel sessie-ID's aan gebruikersspecifieke informatie met formaten zoals `<user_id>:<session_id>` om misbruik van sessies tussen gebruikers te voorkomen  
- **Beheer van sessielevenscyclus**: Implementeer correcte vervaldata, rotatie en ongeldigmaking om kwetsbaarheidsvensters te beperken  
- **Transportbeveiliging**: Verplichte HTTPS voor alle communicatie om onderschepping van sessie-ID's te voorkomen  

### Confused Deputy Probleem

Het **confused deputy probleem** doet zich voor wanneer MCP-servers optreden als authenticatieproxy's tussen clients en derden, waardoor mogelijkheden ontstaan voor autorisatie-omzeiling via exploitatie van statische client-ID's.

#### **Aanvalmechanismen & Risico's**

- **Cookie-gebaseerde toestemmingsomzeiling**: Eerdere gebruikersauthenticatie creëert toestemmingscookies die aanvallers misbruiken via kwaadaardige autorisatieverzoeken met speciaal samengestelde redirect-URI's  
- **Diefstal van autorisatiecodes**: Bestaande toestemmingscookies kunnen ervoor zorgen dat autorisatieservers toestemmingsschermen overslaan en codes doorsturen naar door aanvallers gecontroleerde eindpunten  
- **Ongeautoriseerde API-toegang**: Gestolen autorisatiecodes maken tokenuitwisseling en gebruikersimitatie mogelijk zonder expliciete goedkeuring  

#### **Mitigatiestrategieën**

**Verplichte controles:**  
- **Expliciete toestemmingsvereisten**: MCP-proxyservers die statische client-ID's gebruiken **MOETEN** gebruikersconsent verkrijgen voor elke dynamisch geregistreerde client  
- **OAuth 2.1 beveiligingsimplementatie**: Volg de huidige OAuth-beveiligingsbest practices inclusief PKCE (Proof Key for Code Exchange) voor alle autorisatieverzoeken  
- **Strikte clientvalidatie**: Implementeer rigoureuze validatie van redirect-URI's en clientidentificaties om exploitatie te voorkomen  

### Token Passthrough Kwetsbaarheden  

**Token passthrough** is een expliciete anti-patroon waarbij MCP-servers clienttokens accepteren zonder juiste validatie en deze doorsturen naar downstream API's, wat in strijd is met MCP-autorisatiespecificaties.

#### **Beveiligingsimplicaties**

- **Omzeiling van controles**: Direct gebruik van client-naar-API tokens omzeilt kritieke limieten, validatie en monitoring  
- **Corruptie van audittrail**: Tokens uitgegeven door upstream maken clientidentificatie onmogelijk, wat incidentonderzoek belemmert  
- **Proxy-gebaseerde data-exfiltratie**: Ongevalideerde tokens stellen kwaadwillenden in staat servers als proxy te gebruiken voor ongeautoriseerde data toegang  
- **Schending van vertrouwensgrenzen**: Vertrouwensveronderstellingen van downstream services kunnen worden geschonden wanneer tokenherkomst niet kan worden geverifieerd  
- **Uitbreiding van multi-service aanvallen**: Gecompromitteerde tokens die door meerdere services worden geaccepteerd maken laterale beweging mogelijk  

#### **Vereiste beveiligingscontroles**

**Niet-onderhandelbare vereisten:**  
- **Tokenvalidatie**: MCP-servers **MOGEN NIET** tokens accepteren die niet expliciet voor de MCP-server zijn uitgegeven  
- **Audience-verificatie**: Valideer altijd dat de audience claims van tokens overeenkomen met de identiteit van de MCP-server  
- **Juiste tokenlevenscyclus**: Implementeer kortdurende toegangstokens met veilige rotatiepraktijken  

## Supply Chain Beveiliging voor AI-systemen

Supply chain beveiliging is geëvolueerd voorbij traditionele softwareafhankelijkheden en omvat het gehele AI-ecosysteem. Moderne MCP-implementaties moeten alle AI-gerelateerde componenten rigoureus verifiëren en monitoren, aangezien elk potentiële kwetsbaarheden introduceert die de systeemintegriteit kunnen compromitteren.

### Uitgebreide AI Supply Chain Componenten

**Traditionele softwareafhankelijkheden:**  
- Open-source bibliotheken en frameworks  
- Containerimages en basissystemen  
- Ontwikkeltools en build pipelines  
- Infrastructuurcomponenten en -diensten  

**AI-specifieke supply chain elementen:**  
- **Foundation Models**: Voorgetrainde modellen van diverse aanbieders die herkomstverificatie vereisen  
- **Embedding Services**: Externe vectorisatie- en semantische zoekdiensten  
- **Contextproviders**: Databronnen, kennisbanken en documentrepositories  
- **Derdepartij-API's**: Externe AI-diensten, ML-pijplijnen en dataverwerkingseindpunten  
- **Modelartefacten**: Gewichten, configuraties en fijn-afgestelde modelvarianten  
- **Trainingsdatabronnen**: Datasets gebruikt voor modeltraining en fine-tuning  

### Uitgebreide Supply Chain Beveiligingsstrategie

#### **Componentverificatie & Vertrouwen**  
- **Herkomstvalidatie**: Verifieer oorsprong, licenties en integriteit van alle AI-componenten vóór integratie  
- **Beveiligingsbeoordeling**: Voer kwetsbaarheidsscans en beveiligingsreviews uit voor modellen, databronnen en AI-diensten  
- **Reputatieanalyse**: Evalueer de beveiligingshistorie en praktijken van AI-dienstverleners  
- **Compliance-verificatie**: Zorg dat alle componenten voldoen aan organisatorische beveiligings- en regelgevingseisen  

#### **Veilige Deployment Pipelines**  
- **Geautomatiseerde CI/CD-beveiliging**: Integreer beveiligingsscans in geautomatiseerde deployment pipelines  
- **Integriteit van artefacten**: Implementeer cryptografische verificatie voor alle gedeployde artefacten (code, modellen, configuraties)  
- **Gefaseerde deployment**: Gebruik progressieve deploymentstrategieën met beveiligingsvalidatie in elke fase  
- **Vertrouwde artefactrepositories**: Deploy alleen vanuit geverifieerde, veilige artefactregistries en repositories  

#### **Continue Monitoring & Respons**  
- **Afhankelijkheidsscanning**: Voortdurende kwetsbaarheidsmonitoring voor alle software- en AI-componentafhankelijkheden  
- **Modelmonitoring**: Continue beoordeling van modelgedrag, prestatieafwijkingen en beveiligingsanomalieën  
- **Servicegezondheidstracking**: Monitor externe AI-diensten op beschikbaarheid, beveiligingsincidenten en beleidswijzigingen  
- **Integratie van dreigingsinformatie**: Verwerk dreigingsfeeds specifiek voor AI- en ML-beveiligingsrisico's  

#### **Toegangscontrole & Least Privilege**  
- **Componentniveau-permissies**: Beperk toegang tot modellen, data en diensten op basis van zakelijke noodzaak  
- **Serviceaccountbeheer**: Implementeer toegewijde serviceaccounts met minimale vereiste permissies  
- **Netwerksegmentatie**: Isoleer AI-componenten en beperk netwerktoegang tussen diensten  
- **API Gateway-controles**: Gebruik gecentraliseerde API-gateways om toegang tot externe AI-diensten te controleren en monitoren  

#### **Incidentrespons & Herstel**  
- **Snelle responsprocedures**: Vastgestelde processen voor patchen of vervangen van gecompromitteerde AI-componenten  
- **Rotatie van referenties**: Geautomatiseerde systemen voor het roteren van geheimen, API-sleutels en service-referenties  
- **Rollback-mogelijkheden**: Mogelijkheid om snel terug te keren naar eerder bekende goede versies van AI-componenten  
- **Herstel bij supply chain-inbreuken**: Specifieke procedures voor het reageren op compromittering van upstream AI-diensten  

### Microsoft Beveiligingstools & Integratie

**GitHub Advanced Security** biedt uitgebreide bescherming van de supply chain, waaronder:  
- **Secret Scanning**: Geautomatiseerde detectie van referenties, API-sleutels en tokens in repositories  
- **Dependency Scanning**: Kwetsbaarheidsbeoordeling voor open-source afhankelijkheden en bibliotheken  
- **CodeQL Analyse**: Statische code-analyse voor beveiligingskwetsbaarheden en codeerproblemen  
- **Supply Chain Insights**: Inzicht in afhankelijkheidsgezondheid en beveiligingsstatus  

**Azure DevOps & Azure Repos Integratie:**  
- Naadloze integratie van beveiligingsscans over Microsoft ontwikkelplatforms  
- Geautomatiseerde beveiligingscontroles in Azure Pipelines voor AI-workloads  
- Beleidsafdwinging voor veilige AI-componentdeployments  

**Microsoft Interne Praktijken:**  
Microsoft implementeert uitgebreide supply chain beveiligingspraktijken in alle producten. Lees over bewezen benaderingen in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Foundation Security Best Practices

MCP-implementaties erven en bouwen voort op de bestaande beveiligingshouding van uw organisatie. Het versterken van fundamentele beveiligingspraktijken verbetert aanzienlijk de algehele beveiliging van AI-systemen en MCP-deployments.

### Kernfundamenten van Beveiliging

#### **Veilige ontwikkelpraktijken**  
- **OWASP-compliance**: Bescherming tegen [OWASP Top 10](https://owasp.org/www-project-top-ten/) webapplicatiekwetsbaarheden  
- **AI-specifieke bescherming**: Implementeer controles voor [OWASP Top 10 voor LLM's](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Veilig geheimbeheer**: Gebruik toegewijde kluizen voor tokens, API-sleutels en gevoelige configuratiegegevens  
- **End-to-end encryptie**: Implementeer veilige communicatie over alle applicatiecomponenten en datastromen  
- **Inputvalidatie**: Strenge validatie van alle gebruikersinvoer, API-parameters en databronnen  

#### **Infrastructuurverharding**  
- **Multi-factor authenticatie**: Verplichte MFA voor alle administratieve en serviceaccounts  
- **Patchbeheer**: Geautomatiseerd, tijdig patchen van besturingssystemen, frameworks en afhankelijkheden  
- **Integratie van identiteitsproviders**: Gecentraliseerd identiteitsbeheer via enterprise identiteitsproviders (Microsoft Entra ID, Active Directory)  
- **Netwerksegmentatie**: Logische isolatie van MCP-componenten om laterale beweging te beperken  
- **Principe van minste privilege**: Minimale vereiste permissies voor alle systeemcomponenten en accounts  

#### **Beveiligingsmonitoring & Detectie**  
- **Uitgebreide logging**: Gedetailleerde logging van AI-applicatieactiviteiten, inclusief MCP client-server interacties  
- **SIEM-integratie**: Gecentraliseerd security information and event management voor anomaliedetectie  
- **Gedragsanalyse**: AI-gestuurde monitoring om ongebruikelijke patronen in systeem- en gebruikersgedrag te detecteren  
- **Dreigingsinformatie**: Integratie van externe dreigingsfeeds en indicators of compromise (IOCs)  
- **Incidentrespons**: Goed gedefinieerde procedures voor detectie, respons en herstel van beveiligingsincidenten  

#### **Zero Trust Architectuur**  
- **Nooit vertrouwen, altijd verifiëren**: Continue verificatie van gebruikers, apparaten en netwerkverbindingen  
- **Micro-segmentatie**: Gedetailleerde netwerkcontroles die individuele workloads en diensten isoleren  
- **Identiteitsgerichte beveiliging**: Beveiligingsbeleid gebaseerd op geverifieerde identiteiten in plaats van netwerklocatie  
- **Continue risicobeoordeling**: Dynamische evaluatie van beveiligingshouding op basis van huidige context en gedrag  
- **Conditionele toegang**: Toegangscontroles die zich aanpassen op basis van risicofactoren, locatie en apparaatvertrouwen  

### Enterprise Integratiepatronen

#### **Integratie Microsoft Beveiligingsecosysteem**  
- **Microsoft Defender for Cloud**: Uitgebreid cloud security posture management  
- **Azure Sentinel**: Cloud-native SIEM en SOAR mogelijkheden voor bescherming van AI-workloads  
- **Microsoft Entra ID**: Enterprise identiteits- en toegangsbeheer met conditionele toegangsbeleid  
- **Azure Key Vault**: Gecentraliseerd geheimbeheer met hardware security module (HSM) ondersteuning  
- **Microsoft Purview**: Data governance en compliance voor AI-databronnen en workflows  

#### **Compliance & Governance**  
- **Regelgevingsafstemming**: Zorg dat MCP-implementaties voldoen aan branchespecifieke compliance-eisen (GDPR, HIPAA, SOC 2)  
- **Dataclassificatie**: Juiste categorisering en behandeling van gevoelige data verwerkt door AI-systemen  
- **Audittrails**: Uitgebreide logging voor naleving van regelgeving en forensisch onderzoek  
- **Privacycontroles**: Implementatie van privacy-by-design principes in AI-systeemarchitectuur  
- **Wijzigingsbeheer**: Formele processen voor beveiligingsreviews van AI-systeemwijzigingen  

Deze fundamentele praktijken creëren een robuuste beveiligingsbasis die de effectiviteit van MCP-specifieke beveiligingscontroles versterkt en uitgebreide bescherming biedt voor AI-gedreven applicaties.

## Belangrijke Beveiligingsinzichten

- **Gelaagde beveiligingsaanpak**: Combineer fundamentele beveiligingspraktijken (veilig coderen, minste privilege, supply chain verificatie, continue monitoring) met AI-specifieke controles voor uitgebreide bescherming  

- **AI-specifieke dreigingslandschap**: MCP-systemen worden geconfronteerd met unieke risico's zoals promptinjectie, toolvergiftiging, sessiekaping, confused deputy problemen, token passthrough kwetsbaarheden en excessieve permissies die gespecialiseerde mitigaties vereisen  

- **Authenticatie & autorisatie-excellentie**: Implementeer robuuste authenticatie met externe identiteitsproviders (Microsoft Entra ID), handhaaf correcte tokenvalidatie en accepteer nooit tokens die niet expliciet voor uw MCP-server zijn uitgegeven  

- **AI-aanvalspreventie**: Zet Microsoft Prompt Shields en Azure Content Safety in om indirecte promptinjectie en toolvergiftigingsaanvallen te bestrijden, terwijl u toolmetadata valideert en dynamische wijzigingen monitort  

- **Sessies & transportbeveiliging**: Gebruik cryptografisch veilige, niet-deterministische sessie-ID's gebonden aan gebruikersidentiteiten, implementeer correcte sessielevenscyclusbeheer en gebruik nooit sessies voor authenticatie  

- **OAuth beveiligingsbest practices**: Voorkom confused deputy aanvallen door expliciete gebruikersconsent voor dynamisch geregistreerde clients, correcte OAuth 2.1 implementatie met PKCE en strikte validatie van redirect-URI's  

- **Tokenbeveiligingsprincipes**: Vermijd token passthrough anti-patronen, valideer audience claims van tokens, implementeer kortdurende tokens met veilige rotatie en onderhoud duidelijke vertrouwensgrenzen  

- **Uitgebreide supply chain beveiliging**: Behandel alle AI-ecosysteemcomponenten (modellen, embeddings, contextproviders, externe API's) met dezelfde beveiligingsrigor als traditionele softwareafhankelijkheden  

- **Continue evolutie**: Blijf up-to-date met snel evoluerende MCP-specificaties, draag bij aan beveiligingscommunity-standaarden en onderhoud adaptieve beveiligingshoudingen naarmate het protocol volwassen wordt  

- **Microsoft beveiligingsintegratie**: Maak gebruik van het uitgebreide beveiligingsecosysteem van Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) voor verbeterde MCP-deploymentbescherming  

## Uitgebreide Bronnen

### **Officiële MCP Beveiligingsdocumentatie**  
- [MCP Specificatie (Huidig: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP Beveiligingsbest Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP Autorisatiespecificatie](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)  

### **Beveiligingsstandaarden & Best Practices**  
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 voor Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft Digital Defense Report](https://aka.ms/mddr)  

### **AI Beveiligingsonderzoek & Analyse**  
- [Promptinjectie in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Toolvergiftigingsaanvallen (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Beveiligingsoplossingen**
- [Microsoft Prompt Shields Documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Beveiliging](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementatiehandleidingen & Tutorials**
- [Azure API Management als MCP Authenticatie Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authenticatie met MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Veilige Tokenopslag en Encryptie (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Supply Chain Beveiliging**
- [Azure DevOps Beveiliging](https://azure.microsoft.com/products/devops)
- [Azure Repos Beveiliging](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Beveiligingsreis](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Aanvullende Beveiligingsdocumentatie**

Voor uitgebreide beveiligingsrichtlijnen, raadpleeg deze gespecialiseerde documenten in deze sectie:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Complete beveiligingsbest practices voor MCP-implementaties
- **[Azure Content Safety Implementatie](./azure-content-safety-implementation.md)** - Praktische implementatievoorbeelden voor Azure Content Safety-integratie  
- **[MCP Security Controls 2025](./mcp-security-controls-2025.md)** - Laatste beveiligingscontroles en technieken voor MCP-implementaties
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Snelle referentiegids voor essentiële MCP-beveiligingspraktijken

---

## Wat Nu

Volgende: [Hoofdstuk 3: Aan de Slag](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->