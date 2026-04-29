# Geavanceerde onderwerpen in MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/nl/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Dit hoofdstuk behandelt een reeks geavanceerde onderwerpen in de implementatie van het Model Context Protocol (MCP), waaronder multimodale integratie, schaalbaarheid, beveiligingsbest practices en integratie in ondernemingen. Deze onderwerpen zijn cruciaal voor het bouwen van robuuste en productieklare MCP-toepassingen die kunnen voldoen aan de eisen van moderne AI-systemen.

## Overzicht

Deze les verkent geavanceerde concepten in de implementatie van het Model Context Protocol, met de nadruk op multimodale integratie, schaalbaarheid, beveiligingsbest practices en integratie in ondernemingen. Deze onderwerpen zijn essentieel voor het bouwen van productiekwaliteit MCP-toepassingen die complexe vereisten in bedrijfsomgevingen aankunnen.

## Leerdoelen

Aan het einde van deze les kun je:

- Multimodale mogelijkheden binnen MCP-frameworks implementeren
- Schaalbare MCP-architecturen ontwerpen voor scenario's met hoge vraag
- Beveiligingsbest practices toepassen die aansluiten bij de beveiligingsprincipes van MCP
- MCP integreren met enterprise AI-systemen en frameworks
- De prestaties en betrouwbaarheid in productieomgevingen optimaliseren

## Lessen en voorbeeldprojecten

| Link | Titel | Beschrijving |
|------|-------|--------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integreren met Azure | Leer hoe je je MCP-server op Azure integreert |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP Multimodale voorbeelden | Voorbeelden voor audio-, beeld- en multimodale responsen |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimale Spring Boot-app die OAuth2 met MCP toont, zowel als autorisatie- als resource-server. Demonstreert veilige tokenuitgifte, beschermde eindpunten, Azure Container Apps-deployments en API Management-integratie. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root-contexten | Leer meer over root-contexten en hoe deze te implementeren |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Leer verschillende soorten routing |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Leer hoe je met sampling werkt |
| [5.7 Scaling](./mcp-scaling/README.md) | Schalen | Leer over schalen |
| [5.8 Security](./mcp-security/README.md) | Beveiliging | Beveilig je MCP-server |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web Search MCP | Python MCP-server en client die integreert met SerpAPI voor realtime web-, nieuws- en productzoekopdrachten en Q&A. Demonstreert multi-tool orkestratie, integratie van externe API's en robuuste foutafhandeling. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Realtime datastreaming is essentieel geworden in de data-gedreven wereld van vandaag, waar bedrijven en applicaties onmiddellijke toegang tot informatie nodig hebben om tijdig beslissingen te nemen. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Web Search | Realtime webzoekopdrachten: hoe MCP realtime webzoekopdrachten transformeert door een gestandaardiseerde aanpak voor contextbeheer te bieden tussen AI-modellen, zoekmachines en applicaties. |
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID Authenticatie | Microsoft Entra ID biedt een krachtige cloudgebaseerde identiteit- en toegangsbeheeroplossing, die helpt te garanderen dat alleen geautoriseerde gebruikers en applicaties met je MCP-server kunnen communiceren. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry Integratie | Leer hoe je Model Context Protocol-servers integreert met Azure AI Foundry-agents, wat krachtige tool-orkestratie en enterprise AI-mogelijkheden mogelijk maakt met gestandaardiseerde verbindingen naar externe databronnen. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Context Engineering | De toekomstige mogelijkheden van context engineering-technieken voor MCP-servers, inclusief contextoptimalisatie, dynamisch contextbeheer en strategieën voor effectieve prompt engineering binnen MCP-frameworks. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Aangepast Transport | Leer hoe je aangepaste transportmechanismen implementeert voor gespecialiseerde MCP-communicatiescenario's. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Protocolfuncties | Beheers geavanceerde protocolfuncties zoals voortgangswaarschuwingen, verzoekannuleringen, resourcetemplates en patronen voor foutafhandeling. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Tegengestelde Agenten | Gebruik twee agenten met tegenovergestelde posities, die een enkele MCP-toolset delen, om hallucinaties te detecteren, randgevallen aan het licht te brengen en beter gekalibreerde outputs te produceren via gestructureerde debatten. |

> **Nieuw in MCP-specificatie 2025-11-25**: De specificatie omvat nu experimentele ondersteuning voor **Taken** (langdurige bewerkingen met voortgangsbewaking), **Toolannotaties** (metadata over toolgedrag voor veiligheid), **URL-modus elicitation** (aanvragen van specifieke URL-inhoud van cliënten) en verbeterde **Roots** (voor workspace-contextbeheer). Zie de [MCP-specificatie changelog](https://spec.modelcontextprotocol.io/) voor volledige details.

## Aanvullende verwijzingen

Voor de meest actuele informatie over geavanceerde MCP-onderwerpen, zie:
- [MCP-documentatie](https://modelcontextprotocol.io/)
- [MCP-specificatie (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub-repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Beveiligingsrisico's en mitigaties
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktische beveiligingstraining

## Belangrijkste punten

- Multimodale MCP-implementaties breiden AI-mogelijkheden uit voorbij tekstverwerking
- Schaalbaarheid is essentieel voor bedrijfsimplementaties en kan worden bereikt via horizontale en verticale schaling
- Uitgebreide beveiligingsmaatregelen beschermen data en zorgen voor correcte toegangscontrole
- Integratie in ondernemingen met platforms zoals Azure OpenAI en Microsoft AI Foundry versterkt MCP-capaciteiten
- Geavanceerde MCP-implementaties profiteren van geoptimaliseerde architecturen en zorgvuldige resourcebeheer

## Oefening

Ontwerp een MCP-implementatie van bedrijfsniveau voor een specifieke use case:

1. Identificeer multimodale vereisten voor je use case
2. Omschrijf de beveiligingsmaatregelen die nodig zijn om gevoelige data te beschermen
3. Ontwerp een schaalbare architectuur die variërende belasting aankan
4. Plan integratiepunten met enterprise AI-systemen
5. Documenteer potentiële prestatieknelpunten en mitigatiestrategieën

## Aanvullende bronnen

- [Azure OpenAI-documentatie](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry-documentatie](https://learn.microsoft.com/en-us/ai-services/)

---

## Wat nu?

Verken de lessen in deze module beginnend met: [5.1 MCP Integration](./mcp-integration/README.md)

Als je deze module hebt afgerond, ga dan verder met: [Module 6: Community Contributions](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, houd er rekening mee dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->