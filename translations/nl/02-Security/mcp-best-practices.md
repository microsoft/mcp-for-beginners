# MCP Security Best Practices 2025

Deze uitgebreide gids beschrijft essentiële beveiligingsbest practices voor het implementeren van Model Context Protocol (MCP) systemen op basis van de nieuwste **MCP Specificatie 2025-11-25** en huidige industrienormen. Deze praktijken behandelen zowel traditionele beveiligingsproblemen als AI-specifieke bedreigingen die uniek zijn voor MCP-implementaties.

## Kritieke Beveiligingseisen

### Verplichte Beveiligingscontroles (MUST Vereisten)

1. **Tokenvalidatie**: MCP-servers **MOGEN GEEN** tokens accepteren die niet expliciet zijn uitgegeven voor de MCP-server zelf  
2. **Autorisatieverificatie**: MCP-servers die autorisatie implementeren **MOETEN** ALLE inkomende verzoeken verifiëren en **MOGEN GEEN** sessies gebruiken voor authenticatie  
3. **Gebruikersconsent**: MCP-proxyservers die statische client-ID's gebruiken **MOETEN** expliciete gebruikersconsent verkrijgen voor elke dynamisch geregistreerde client  
4. **Veilige sessie-ID's**: MCP-servers **MOETEN** cryptografisch veilige, niet-deterministische sessie-ID's gebruiken die gegenereerd zijn met veilige willekeurige getalgeneratoren  

## Kernbeveiligingspraktijken

### 1. Invoervalidatie & Sanitatie
- **Uitgebreide invoervalidatie**: Valideer en saniteer alle invoer om injectieaanvallen, confused deputy-problemen en promptinjectie-kwetsbaarheden te voorkomen  
- **Parameter schema afdwinging**: Implementeer strikte JSON-schema validatie voor alle toolparameters en API-invoer  
- **Contentfiltering**: Gebruik Microsoft Prompt Shields en Azure Content Safety om kwaadaardige inhoud in prompts en reacties te filteren  
- **Outputsanitatie**: Valideer en saniteer alle modeluitvoer voordat deze aan gebruikers of downstream systemen wordt gepresenteerd  

### 2. Uitmuntendheid in Authenticatie & Autorisatie  
- **Externe identiteitsproviders**: Delegeer authenticatie aan gevestigde identiteitsproviders (Microsoft Entra ID, OAuth 2.1 providers) in plaats van eigen authenticatie te implementeren  
- **Fijnmazige permissies**: Implementeer gedetailleerde, tool-specifieke permissies volgens het principe van minste privilege  
- **Token levenscyclusbeheer**: Gebruik kortdurende toegangstokens met veilige rotatie en correcte audience-validatie  
- **Multi-factor authenticatie**: Vereis MFA voor alle administratieve toegang en gevoelige operaties  

### 3. Veilige communicatieprotocollen
- **Transport Layer Security**: Gebruik HTTPS/TLS 1.3 voor alle MCP-communicatie met correcte certificaatvalidatie  
- **End-to-end encryptie**: Implementeer extra encryptielagen voor zeer gevoelige data in transit en in rust  
- **Certificaatbeheer**: Onderhoud correct certificaatlevenscyclusbeheer met geautomatiseerde vernieuwingsprocessen  
- **Protocolversie afdwinging**: Gebruik de huidige MCP-protocolversie (2025-11-25) met correcte versieonderhandeling  

### 4. Geavanceerde rate limiting & resourcebescherming
- **Meervoudige laag rate limiting**: Implementeer rate limiting op gebruikers-, sessie-, tool- en resource-niveau om misbruik te voorkomen  
- **Adaptieve rate limiting**: Gebruik machine learning-gebaseerde rate limiting die zich aanpast aan gebruikspatronen en dreigingsindicatoren  
- **Resource quotabeheer**: Stel passende limieten in voor rekenkracht, geheugengebruik en uitvoeringstijd  
- **DDoS-bescherming**: Zet uitgebreide DDoS-bescherming en verkeersanalysetools in  

### 5. Uitgebreide logging & monitoring
- **Gestructureerde auditlogging**: Implementeer gedetailleerde, doorzoekbare logs voor alle MCP-operaties, tooluitvoeringen en beveiligingsevenementen  
- **Realtime beveiligingsmonitoring**: Zet SIEM-systemen in met AI-gestuurde anomaliedetectie voor MCP workloads  
- **Privacy-compliant logging**: Log beveiligingsevenementen met respect voor privacyvereisten en regelgeving  
- **Integratie incidentrespons**: Verbind loggingsystemen met geautomatiseerde incidentresponsworkflows  

### 6. Verbeterde veilige opslagpraktijken
- **Hardware Security Modules**: Gebruik HSM-ondersteunde sleutelopslag (Azure Key Vault, AWS CloudHSM) voor kritieke cryptografische operaties  
- **Encryptiesleutelbeheer**: Implementeer correcte sleutelrotatie, scheiding en toegangscontrole voor encryptiesleutels  
- **Secrets management**: Sla alle API-sleutels, tokens en referenties op in speciale geheimbeheer systemen  
- **Dataclassificatie**: Classificeer data op basis van gevoeligheidsniveau en pas passende beschermingsmaatregelen toe  

### 7. Geavanceerd tokenbeheer
- **Voorkoming token passthrough**: Verbied expliciet token passthrough-patronen die beveiligingscontroles omzeilen  
- **Audience-validatie**: Verifieer altijd dat token audience claims overeenkomen met de bedoelde MCP-serveridentiteit  
- **Claims-gebaseerde autorisatie**: Implementeer fijnmazige autorisatie op basis van tokenclaims en gebruikersattributen  
- **Token binding**: Bind tokens aan specifieke sessies, gebruikers of apparaten waar passend  

### 8. Veilig sessiebeheer
- **Cryptografische sessie-ID's**: Genereer sessie-ID's met cryptografisch veilige willekeurige getalgeneratoren (geen voorspelbare reeksen)  
- **Gebruikersspecifieke binding**: Bind sessie-ID's aan gebruikersspecifieke informatie met veilige formaten zoals `<user_id>:<session_id>`  
- **Sessielevenscycluscontroles**: Implementeer correcte sessieverval, rotatie en ongeldigmakingsmechanismen  
- **Sessiebeveiligingsheaders**: Gebruik passende HTTP-beveiligingsheaders voor sessiebescherming  

### 9. AI-specifieke beveiligingscontroles
- **Promptinjectie verdediging**: Zet Microsoft Prompt Shields in met spotlighting, delimiters en datamarking technieken  
- **Voorkoming toolvergiftiging**: Valideer toolmetadata, monitor dynamische wijzigingen en verifieer toolintegriteit  
- **Modeluitvoer validatie**: Scan modeluitvoer op mogelijke datalekken, schadelijke inhoud of overtredingen van beveiligingsbeleid  
- **Context window bescherming**: Implementeer controles om context window vergiftiging en manipulatieaanvallen te voorkomen  

### 10. Tooluitvoeringsbeveiliging
- **Uitvoeringssandboxing**: Voer tooluitvoeringen uit in containerized, geïsoleerde omgevingen met resourcebeperkingen  
- **Privilegiescheiding**: Voer tools uit met minimale vereiste privileges en gescheiden service-accounts  
- **Netwerkisolatie**: Implementeer netwerksegmentatie voor tooluitvoeringsomgevingen  
- **Uitvoeringsmonitoring**: Monitor tooluitvoering op afwijkend gedrag, resourcegebruik en beveiligingsschendingen  

### 11. Continue beveiligingsvalidatie
- **Geautomatiseerd beveiligingstesten**: Integreer beveiligingstesten in CI/CD-pijplijnen met tools zoals GitHub Advanced Security  
- **Kwetsbaarheidsbeheer**: Scan regelmatig alle afhankelijkheden, inclusief AI-modellen en externe services  
- **Penetratietesten**: Voer regelmatige beveiligingsbeoordelingen uit die specifiek MCP-implementaties targeten  
- **Beveiligingscode reviews**: Implementeer verplichte beveiligingsreviews voor alle MCP-gerelateerde codewijzigingen  

### 12. Supply chain beveiliging voor AI
- **Componentverificatie**: Verifieer herkomst, integriteit en beveiliging van alle AI-componenten (modellen, embeddings, API's)  
- **Afhankelijkheidsbeheer**: Houd actuele inventarissen bij van alle software- en AI-afhankelijkheden met kwetsbaarheidsmonitoring  
- **Vertrouwde repositories**: Gebruik geverifieerde, vertrouwde bronnen voor alle AI-modellen, bibliotheken en tools  
- **Supply chain monitoring**: Monitor continu op compromittering bij AI-dienstverleners en modelrepositories  

## Geavanceerde beveiligingspatronen

### Zero Trust Architectuur voor MCP
- **Nooit vertrouwen, altijd verifiëren**: Implementeer continue verificatie voor alle MCP-deelnemers  
- **Micro-segmentatie**: Isoleer MCP-componenten met fijnmazige netwerk- en identiteitscontroles  
- **Conditionele toegang**: Implementeer risicogebaseerde toegangscontroles die zich aanpassen aan context en gedrag  
- **Continue risicobeoordeling**: Evalueer dynamisch de beveiligingshouding op basis van actuele dreigingsindicatoren  

### Privacy-beschermende AI-implementatie
- **Dataminimalisatie**: Stel alleen de minimaal noodzakelijke data bloot voor elke MCP-operatie  
- **Differentiële privacy**: Implementeer privacy-beschermende technieken voor verwerking van gevoelige data  
- **Homomorfe encryptie**: Gebruik geavanceerde encryptietechnieken voor veilige berekeningen op versleutelde data  
- **Federated learning**: Implementeer gedistribueerde leerbenaderingen die datalocaliteit en privacy behouden  

### Incidentrespons voor AI-systemen
- **AI-specifieke incidentprocedures**: Ontwikkel incidentresponsprocedures die zijn toegespitst op AI- en MCP-specifieke bedreigingen  
- **Geautomatiseerde respons**: Implementeer geautomatiseerde containment en herstel voor veelvoorkomende AI-beveiligingsincidenten  
- **Forensische capaciteiten**: Onderhoud forensische gereedheid voor AI-systeemcompromitteringen en datalekken  
- **Herstelprocedures**: Stel procedures op voor herstel van AI-modelvergiftiging, promptinjectieaanvallen en servicecompromitteringen  

## Implementatieresources & standaarden

### Officiële MCP-documentatie
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Huidige MCP-protocolspecificatie  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Officiële beveiligingsrichtlijnen  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Authenticatie- en autorisatiepatronen  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Transportlaag beveiligingseisen  

### Microsoft beveiligingsoplossingen
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Geavanceerde bescherming tegen promptinjectie  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Uitgebreide AI-contentfiltering  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Enterprise identiteit- en toegangsbeheer  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Veilige geheimen- en referentiebeheer  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Supply chain en codebeveiligingsscanning  

### Beveiligingsstandaarden & frameworks
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Huidige OAuth-beveiligingsrichtlijnen  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Webapplicatiebeveiligingsrisico's  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifieke beveiligingsrisico's  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Uitgebreid AI-risicomanagement  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Informatiebeveiligingsmanagementsystemen  

### Implementatiegidsen & tutorials
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Enterprise authenticatiepatronen  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integratie van identiteitsprovider  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Best practices tokenbeheer  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Geavanceerde encryptiepatronen  

### Geavanceerde beveiligingsresources
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Veilige ontwikkelingspraktijken  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifieke beveiligingstesten  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Methodologie voor AI-dreigingsmodellering  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Privacy-beschermende AI-technieken  

### Compliance & governance
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Privacycompliance in AI-systemen  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Verantwoorde AI-implementatie  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Beveiligingscontroles voor AI-dienstverleners  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Compliance-eisen voor gezondheidszorg AI  

### DevSecOps & automatisering
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Veilige AI-ontwikkelpijplijnen  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Continue beveiligingsvalidatie  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Veilige infrastructuurimplementatie  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Beveiliging van AI workload-containerisatie  

### Monitoring & incidentrespons  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Uitgebreide monitoringsoplossingen  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifieke incidentprocedures  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Security information and event management  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI-dreigingsinformatiebronnen  

## 🔄 Continue Verbetering

### Blijf actueel met evoluerende standaarden
- **MCP Specificatie-updates**: Volg officiële MCP-specificatiewijzigingen en beveiligingsadviezen  
- **Dreigingsinformatie**: Abonneer op AI-beveiligingsdreigingsfeeds en kwetsbaarheidsdatabases  
- **Communitybetrokkenheid**: Neem deel aan MCP-beveiligingscommunitydiscussies en werkgroepen  
- **Regelmatige beoordeling**: Voer elk kwartaal beveiligingshoudingsbeoordelingen uit en werk praktijken bij  

### Bijdragen aan MCP-beveiliging
- **Beveiligingsonderzoek**: Draag bij aan MCP-beveiligingsonderzoek en kwetsbaarheidsrapportageprogramma's  
- **Delen van best practices**: Deel beveiligingsimplementaties en geleerde lessen met de community  
- **Standaardontwikkeling**: Deelname aan de ontwikkeling van MCP-specificaties en het opstellen van beveiligingsnormen  
- **Toolontwikkeling**: Ontwikkelen en delen van beveiligingstools en bibliotheken voor het MCP-ecosysteem

---

*Dit document weerspiegelt de beste beveiligingspraktijken van MCP per 18 december 2025, gebaseerd op MCP-specificatie 2025-11-25. Beveiligingspraktijken moeten regelmatig worden herzien en bijgewerkt naarmate het protocol en het dreigingslandschap evolueren.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->