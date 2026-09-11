# MCP Beveiligingsrichtlijnen - Update september 2026

Deze uitgebreide gids beschrijft essentiële beveiligingsrichtlijnen voor
het implementeren van Model Context Protocol (MCP)-systemen gebaseerd op
**MCP-specificatie 2026-07-28** en huidige industrienormen. Deze
richtlijnen behandelen zowel traditionele beveiligingsvraagstukken als AI-specifieke bedreigingen
die uniek zijn voor MCP-implementaties.

## Kritische Beveiligingseisen

### Verplichte Beveiligingscontroles (MOET-eisen)

1. **Tokenvalidatie**: MCP-servers **MOETEN GEEN** tokens accepteren die niet expliciet zijn uitgegeven voor de MCP-server zelf
2. **Autorisatieverificatie**: MCP-servers die autorisatie implementeren **MOETEN** ALLE inkomende verzoeken verifiëren en **MOETEN GEEN** sessies gebruiken voor authenticatie  
3. **Gebruikersinzichten**: MCP-proxyservers die statische client-ID's van derden gebruiken **MOETEN** expliciete toestemming verkrijgen voor elke MCP-client voordat een autorisatiestroom wordt doorgestuurd
4. **Beveiliging van State Handles**: MCP-servers **MOETEN GEEN** bezit van een
	application state handle beschouwen als authenticatie en **MOETEN** elke
	aanvraag die er één gebruikt autoriseren

## Kernbeveiligingspraktijken

### 1. Invoervalidatie & Sanitisatie
- **Uitgebreide invoervalidatie**: Valideer en sanitizeer alle invoer om injectieaanvallen, confused deputy-problemen en kwetsbaarheden voor promptinjectie te voorkomen
- **Parameter schema-handhaving**: Implementeer strikte JSON-schema validatie voor alle toolparameters en API-invoer
- **Inhoudsfiltering**: Gebruik Microsoft Prompt Shields en Azure Content Safety om kwaadaardige inhoud in prompts en reacties te filteren
- **Output sanitisatie**: Valideer en sanitizeer alle modeloutputs voordat deze aan gebruikers of downstream systemen worden gepresenteerd

### 2. Authenticatie & Autorisatie Uitmuntendheid  
- **Externe identiteitsproviders**: Delegeer authenticatie aan gevestigde identiteitsproviders (Microsoft Entra ID, OAuth 2.1 providers) in plaats van aangepaste authenticatie te implementeren
- **Clientregistratie**: Geef voorkeur aan Client ID Metadata Documenten of preregistratie; gebruik alleen verouderde Dynamic Client Registration voor compatibiliteit
- **Fijngranulaire permissies**: Implementeer gedetailleerde, tool-specifieke permissies volgens het principe van de minste rechten
- **Token levenscyclusbeheer**: Gebruik kortlevende toegangstokens met veilige rotatie en juiste audience-validatie
- **Multi-Factor Authenticatie**: Vereis MFA voor alle administratieve toegang en gevoelige handelingen

### 3. Veilige Communicatieprotocollen
- **Transportlaagbeveiliging**: Gebruik HTTPS met juiste certificaatvalidatie
	voor externe HTTP MCP-communicatie; gebruik procesisolatie en
	omgevingsreferenties voor lokale stdio-servers
- **End-to-end encryptie**: Implementeer extra versleutellagen voor hoogst gevoelige data tijdens overdracht en in rust
- **Certificaatbeheer**: Onderhoud degelijk certificaatlevenscyclusbeheer met geautomatiseerde verlengingsprocessen
- **Protocolversie-handhaving**: Gebruik MCP `2026-07-28`, neem de vereiste
	versiemetadata op in elk verzoek, en verwerp niet-ondersteunde versies

### 4. Geavanceerde Rate Limiting & Bescherming van Middelen
- **Meerdere lagen rate limiting**: Implementeer rate limiting per gebruiker, referentie,
  operatie, tool, en resource om misbruik te voorkomen
- **Adaptieve rate limiting**: Gebruik op machine learning gebaseerde rate limiting die zich aanpast aan gebruikspatronen en dreigingsindicatoren
- **Resource quota beheer**: Stel passende limieten in voor computationele middelen, geheugengebruik en uitvoeringstijd
- **DDoS-bescherming**: Zet uitgebreide DDoS-beschermings- en verkeersanalysetools in

### 5. Uitgebreide Logging & Monitoring
- **Gestructureerde auditlogging**: Implementeer gedetailleerde, doorzoekbare logs voor alle MCP-operaties, tool-uitvoeringen en beveiligingsgebeurtenissen
- **Realtime beveiligingsmonitoring**: Zet SIEM-systemen in met AI-gestuurde anomaliedetectie voor MCP workloads
- **Privacy-conforme logging**: Log beveiligingsgebeurtenissen met respect voor data privacy eisen en regelgeving
- **Integratie incidentrespons**: Koppel logging-systemen aan geautomatiseerde incidentresponsprocessen

### 6. Verbeterde Veilig Opslagpraktijken
- **Hardware Security Modules**: Gebruik HSM-ondersteunde sleutellagring (Azure Key Vault, AWS CloudHSM) voor kritieke cryptografische operaties
- **Encryptiesleutelbeheer**: Implementeer correcte sleutelrotatie, segregatie en toegangscontrole voor encryptiesleutels
- **Geheimbeheer**: Bewaar alle API-sleutels, tokens en referenties in speciale geheime beheersystemen
- **Data-classificatie**: Classificeer data op basis van gevoeligheidsniveau en pas passende beschermingsmaatregelen toe

### 7. Geavanceerd Tokenbeheer
- **Token passthrough-verbod**: Verbied expliciet token passthrough-patronen die beveiligingscontroles omzeilen
- **Audience-validatie**: Verifieer altijd dat token-audience claims overeenkomen met de bedoelde MCP-serveridentiteit
- **Op claims gebaseerde autorisatie**: Implementeer fijnmazige autorisatie op basis van token claims en gebruikersattributen
- **Token binding**: Valideer dat tokens gericht zijn op de bedoelde MCP-resource en
	bind application state handles server-side aan de geauthenticeerde hoofdgebruiker

### 8. Veilige Application State

- **Cryptografische state handles**: Genereer ondoorzichtige, niet-deterministische handles
	voor state die over meerdere verzoeken wordt gebruikt
- **Gebruiker-specifieke binding**: Bind elke handle server-side aan de geauthenticeerde
	hoofdgebruiker; vertrouw niet op een door de client opgegeven gebruikers-ID
- **Levenscycluscontroles**: Laat handles verlopen en intrekken, en definieer hoe aanroepers
	kunnen herstellen van verouderde state
- **Autorisatie per verzoek**: Controleer autorisatie opnieuw telkens wanneer een handle
	wordt gepresenteerd; een handle is een naam, geen referentie

### 9. AI-specifieke Beveiligingscontroles
- **Verdediging tegen promptinjectie**: Zet Microsoft Prompt Shields in met spotlighting, afbakeningen en datamerkerstechnieken
- **Preventie van toolvergiftiging**: Valideer toolmetadata, monitor op dynamische wijzigingen en verifieer toolintegriteit
- **Validatie van modeloutput**: Scan modeloutputs op mogelijke datalekken, schadelijke inhoud of schendingen van beveiligingsbeleid
- **Bescherming van contextvensters**: Implementeer controles om contextvenstervergiftiging en manipulatie-aanvallen te voorkomen

### 10. Beveiliging van Tooluitvoering
- **Uitvoeringssandboxen**: Voer tooluitvoeringen uit in gecontaineriseerde, geïsoleerde omgevingen met resource-limieten
- **Privilegescheiding**: Voer tools uit met minimale vereiste rechten en gescheiden service-accounts
- **Netwerkisolatie**: Implementeer netwerkscheiding voor tooluitvoeringsomgevingen
- **Monitoring van uitvoering**: Monitor tooluitvoering op abnormaal gedrag, resourcegebruik en beveiligingsschendingen

### 11. Continue Beveiligingsvalidatie
- **Geautomatiseerd beveiligingstesten**: Integreer beveiligingstests in CI/CD-pijplijnen met tools zoals GitHub Advanced Security
- **Kwetsbaarheidsbeheer**: Scan regelmatig alle afhankelijkheden, inclusief AI-modellen en externe services
- **Penetratietesten**: Voer regelmatige beveiligingsevaluaties uit die specifiek gericht zijn op MCP-implementaties
- **Beveiligingscodebeoordelingen**: Implementeer verplichte beveiligingsreviews voor alle MCP-gerelateerde codewijzigingen

### 12. Supply Chain Beveiliging voor AI
- **Componentverificatie**: Verifieer herkomst, integriteit en beveiliging van alle AI-componenten (modellen, embeddings, API's)
- **Afhankelijkheidsbeheer**: Houd actuele inventarissen bij van alle software- en AI-afhankelijkheden met kwetsbaarheidstracking
- **Vertrouwde repositories**: Gebruik geverifieerde, vertrouwde bronnen voor alle AI-modellen, bibliotheken en tools
- **Supply chain monitoring**: Monitor continu op compromitteringen bij AI-serviceproviders en modelrepositories

## Geavanceerde Beveiligingspatronen

### Zero Trust Architectuur voor MCP
- **Nooit vertrouwen, altijd verifiëren**: Implementeer continue verificatie voor alle MCP-deelnemers
- **Microsegmentatie**: Isoleer MCP-componenten met gedetailleerde netwerk- en identiteitscontroles
- **Conditionele toegang**: Implementeer risicogebaseerde toegangscontroles die zich aanpassen aan context en gedrag
- **Continue risicobeoordeling**: Evalueer dynamisch de beveiligingspositie op basis van actuele dreigingsindicatoren

### Privacyvriendelijke AI-implementatie
- **Dataminimalisatie**: Stel alleen de minimaal noodzakelijke data bloot voor elke MCP-operatie
- **Differentiële privacy**: Implementeer privacy-beschermende technieken voor verwerking van gevoelige data
- **Homomorfe encryptie**: Gebruik geavanceerde versleutelingsmethoden voor beveiligde berekeningen op versleutelde data
- **Federated learning**: Implementeer gedistribueerde leerbenaderingen die datalocaliteit en privacy behouden

### Incidentrespons voor AI-systemen
- **AI-specifieke incidentprocedures**: Ontwikkel incidentresponsprocedures op maat van AI- en MCP-specifieke bedreigingen
- **Geautomatiseerde respons**: Implementeer automatische beperking en herstel voor veelvoorkomende AI-beveiligingsincidenten  
- **Forensische mogelijkheden**: Zorg voor forensische gereedheid voor AI-systeemcompromitteringen en datalekken
- **Herstelprocedures**: Stel procedures op voor herstel van AI-modelvergiftiging, promptinjectie-aanvallen en servicecompromitteringen

## Implementatiemiddelen & Normen

### 🏔️ Praktische Beveiligingstraining
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Uitgebreide praktische workshop voor het beveiligen van MCP-servers in Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referentiearchitectuur en implementatierichtlijnen voor OWASP MCP Top 10

### Officiële MCP-documentatie
- [MCP-specificatie 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Huidige MCP-protocolspecificatie
- [MCP Beveiligingsrichtlijnen](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Officiële beveiligingsrichtlijnen
- [MCP Autorisatiespecificatie](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP-autorisatiepatronen
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Transportvereisten

### Microsoft Beveiligingsoplossingen
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Geavanceerde bescherming tegen promptinjectie
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Uitgebreide AI-inhoudsfiltering
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Enterprise identiteits- en toegangsbeheer
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Veilige geheime opslag en referentiebeheer
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Supply chain en codebeveiligingsscans

### Beveiligingsnormen & Frameworks
- [OAuth 2.1 Beveiligingsrichtlijnen](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Recente OAuth-beveiligingsrichtlijnen
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Risico's van webapplicatiebeveiliging
- [OWASP Top 10 voor LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifieke beveiligingsrisico's
- [NIST AI Risicobeheer Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Uitgebreid AI risicobeheer
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Managementsystemen voor informatiebeveiliging

### Implementatierichtlijnen & Tutorials
- [Azure API Management als MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Enterprise authenticatiepatronen
- [Microsoft Entra ID met MCP-servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integratie van identiteitsprovider
- [Veilige tokenopslag implementatie](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Best practices voor tokenbeheer
- [End-to-end encryptie voor AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Geavanceerde encryptiepatronen

### Geavanceerde beveiligingsbronnen
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Praktijken voor veilige ontwikkeling
- [AI Red Team Richtlijnen](https://learn.microsoft.com/security/ai-red-team/) - AI-specifieke beveiligingstests
- [Threat Modeling voor AI-systemen](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Methodologie voor AI-dreigingsmodellering
- [Privacy Engineering voor AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Privacyvriendelijke AI-technieken

### Compliance & Governance
- [GDPR-compliance voor AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Privacycompliance in AI-systemen
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Verantwoorde AI-implementatie
- [SOC 2 voor AI-services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Beveiligingscontroles voor AI-serviceproviders
- [HIPAA-compliance voor AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Compliance-eisen voor AI in de gezondheidszorg

### DevSecOps & Automatisering
- [DevSecOps-pijplijn voor AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Veilige AI-ontwikkelpijplijnen
- [Geautomatiseerd beveiligingstesten](https://learn.microsoft.com/security/engineering/devsecops) - Continue beveiligingsvalidatie
- [Infrastructure as Code-beveiliging](https://learn.microsoft.com/security/engineering/infrastructure-security) - Veilige infrastructuuruitrol
- [Containerveiligheid voor AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Beveiliging van AI workload-containerisatie

### Monitoring & Incidentrespons  
- [Azure Monitor voor AI workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Uitgebreide monitoringsoplossingen
- [AI-beveiligingsincidentrespons](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifieke incidentprocedures
- [SIEM voor AI-systemen](https://learn.microsoft.com/azure/sentinel/overview) - Beveiligingsinformatie- en gebeurtenisbeheer

- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI bronnen voor dreigingsinformatie

## 🔄 Continu Verbeteren

### Blijf Op De Hoogte van Ontwikkelende Standaarden
- **MCP Specificatie-updates**: Volg officiële MCP specificatiewijzigingen en beveiligingsadviezen
- **Dreigingsinformatie**: Abonneer op AI-beveiligingsdreigingsfeeds en kwetsbaarheidsdatabanken  
- **Gemeenschapsbetrokkenheid**: Neem deel aan MCP beveiligingscommunity-discussies en werkgroepen
- **Regelmatige Beoordeling**: Voer elk kwartaal een beoordeling van de beveiligingspositie uit en werk praktijken bij

### Bijdragen aan MCP Beveiliging
- **Beveiligingsonderzoek**: Draag bij aan MCP beveiligingsonderzoek en programma's voor het melden van kwetsbaarheden
- **Delen van Best Practices**: Deel beveiligingsimplementaties en geleerde lessen met de community
- **Ontwikkeling van Standaarden**: Neem deel aan de ontwikkeling van MCP-specificaties en het creëren van beveiligingsstandaarden
- **Ontwikkeling van Tools**: Ontwikkel en deel beveiligingstools en -bibliotheken voor het MCP-ecosysteem

---

*Dit document weerspiegelt MCP beveiligingsbest practices per 9 september 2026,
gebaseerd op MCP Specificatie `2026-07-28`. Beveiligingspraktijken moeten regelmatig
worden herzien naarmate het protocol en het dreigingslandschap evolueren.*

## Wat Nu?

- Lees: [MCP Security Best Practices](./mcp-security-best-practices.md)
- Terug naar: [Security Module Overview](./README.md)
- Ga verder naar: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->