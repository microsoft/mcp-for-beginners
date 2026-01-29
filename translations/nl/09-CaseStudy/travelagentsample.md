# Case Study: Azure AI Travel Agents – Referentie-implementatie

## Overzicht

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) is een uitgebreide referentieoplossing ontwikkeld door Microsoft die laat zien hoe je een multi-agent, AI-gestuurde reisplanningsapplicatie bouwt met behulp van het Model Context Protocol (MCP), Azure OpenAI en Azure AI Search. Dit project toont best practices voor het coördineren van meerdere AI-agents, het integreren van bedrijfsdata en het bieden van een veilige, uitbreidbare platform voor scenario’s uit de praktijk.

## Belangrijkste Kenmerken
- **Multi-Agent Orkestratie:** Maakt gebruik van MCP om gespecialiseerde agents (bijv. vlucht-, hotel- en reisroute-agents) te coördineren die samenwerken om complexe reisplanningsopdrachten uit te voeren.
- **Integratie van Bedrijfsdata:** Verbindt met Azure AI Search en andere bedrijfsdatabronnen om actuele, relevante informatie te bieden voor reisaanbevelingen.
- **Veilige, Schaalbare Architectuur:** Benut Azure-diensten voor authenticatie, autorisatie en schaalbare implementatie, volgens de beste beveiligingspraktijken voor bedrijven.
- **Uitbreidbare Tools:** Implementeert herbruikbare MCP-tools en prompt-sjablonen, waardoor snelle aanpassing aan nieuwe domeinen of zakelijke eisen mogelijk is.
- **Gebruikerservaring:** Biedt een conversatie-interface waarmee gebruikers kunnen communiceren met de reisagents, aangedreven door Azure OpenAI en MCP.

## Architectuur
![Architectuur](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Beschrijving Architectuurdiagram

De Azure AI Travel Agents-oplossing is ontworpen voor modulariteit, schaalbaarheid en veilige integratie van meerdere AI-agents en bedrijfsdatabronnen. De belangrijkste componenten en datastromen zijn als volgt:

- **Gebruikersinterface:** Gebruikers communiceren met het systeem via een conversatie-UI (zoals een webchat of Teams-bot), die gebruikersvragen verzendt en reisaanbevelingen ontvangt.
- **MCP Server:** Dient als centrale orkestrator, ontvangt gebruikersinvoer, beheert context en coördineert de acties van gespecialiseerde agents (bijv. FlightAgent, HotelAgent, ItineraryAgent) via het Model Context Protocol.
- **AI Agents:** Elke agent is verantwoordelijk voor een specifiek domein (vluchten, hotels, reisroutes) en is geïmplementeerd als een MCP-tool. Agents gebruiken prompt-sjablonen en logica om verzoeken te verwerken en antwoorden te genereren.
- **Azure OpenAI Service:** Biedt geavanceerd begrip en generatie van natuurlijke taal, waardoor agents de intentie van gebruikers kunnen interpreteren en conversatie-antwoorden kunnen genereren.
- **Azure AI Search & Bedrijfsdata:** Agents raadplegen Azure AI Search en andere bedrijfsdatabronnen om actuele informatie over vluchten, hotels en reisopties op te halen.
- **Authenticatie & Beveiliging:** Integreert met Microsoft Entra ID voor veilige authenticatie en past het principe van minste rechten toe op alle resources.
- **Implementatie:** Ontworpen voor uitrol op Azure Container Apps, wat schaalbaarheid, monitoring en operationele efficiëntie garandeert.

Deze architectuur maakt naadloze orkestratie van meerdere AI-agents mogelijk, veilige integratie met bedrijfsdata en een robuust, uitbreidbaar platform voor het bouwen van domeinspecifieke AI-oplossingen.

## Stapsgewijze Uitleg van het Architectuurdiagram
Stel je voor dat je een grote reis plant en een team van deskundige assistenten hebt die je bij elk detail helpen. Het Azure AI Travel Agents-systeem werkt op een vergelijkbare manier, met verschillende onderdelen (zoals teamleden) die elk een speciale taak hebben. Zo werkt het samen:

### Gebruikersinterface (UI):
Zie dit als de balie van je reisagent. Hier stel je vragen of doe je verzoeken, zoals “Vind een vlucht naar Parijs.” Dit kan een chatvenster op een website zijn of een berichtendienst.

### MCP Server (De Coördinator):
De MCP Server is als de manager die naar je verzoek luistert bij de balie en bepaalt welke specialist welk deel afhandelt. Hij houdt de conversatie bij en zorgt dat alles soepel verloopt.

### AI Agents (Specialistische Assistenten):
Elke agent is een expert in een bepaald gebied – de ene weet alles van vluchten, de andere van hotels, weer een andere van het plannen van je reisroute. Wanneer je een reis aanvraagt, stuurt de MCP Server je verzoek naar de juiste agent(s). Deze agents gebruiken hun kennis en tools om de beste opties voor je te vinden.

### Azure OpenAI Service (Taalexpert):
Dit is alsof je een taalexpert hebt die precies begrijpt wat je vraagt, ongeacht hoe je het formuleert. Het helpt de agents om je verzoeken te begrijpen en natuurlijk klinkende antwoorden te geven.

### Azure AI Search & Bedrijfsdata (Informatiebibliotheek):
Stel je een enorme, actuele bibliotheek voor met alle nieuwste reisinformatie – vluchtschema’s, hotelbeschikbaarheid en meer. De agents doorzoeken deze bibliotheek om de meest accurate antwoorden voor je te vinden.

### Authenticatie & Beveiliging (Beveiligingsbeambte):
Net zoals een beveiligingsbeambte controleert wie bepaalde ruimtes mag betreden, zorgt dit onderdeel ervoor dat alleen geautoriseerde personen en agents toegang hebben tot gevoelige informatie. Het houdt je data veilig en privé.

### Implementatie op Azure Container Apps (Het Gebouw):
Al deze assistenten en tools werken samen binnen een veilig, schaalbaar gebouw (de cloud). Dit betekent dat het systeem veel gebruikers tegelijk aankan en altijd beschikbaar is wanneer je het nodig hebt.

## Hoe het allemaal samenwerkt:

Je begint met een vraag bij de balie (UI).  
De manager (MCP Server) bepaalt welke specialist (agent) je kan helpen.  
De specialist gebruikt de taalexpert (OpenAI) om je verzoek te begrijpen en de bibliotheek (AI Search) om het beste antwoord te vinden.  
De beveiligingsbeambte (Authenticatie) zorgt dat alles veilig verloopt.  
Dit alles gebeurt binnen een betrouwbaar, schaalbaar gebouw (Azure Container Apps), zodat je ervaring soepel en veilig is.  
Deze samenwerking stelt het systeem in staat om je snel en veilig te helpen bij het plannen van je reis, net als een team van deskundige reisagenten die samenwerken in een modern kantoor!

## Technische Implementatie
- **MCP Server:** Beheert de kernlogica voor orkestratie, biedt agenttools aan en beheert context voor meerstaps-reisplanningsworkflows.
- **Agents:** Elke agent (bijv. FlightAgent, HotelAgent) is geïmplementeerd als een MCP-tool met eigen prompt-sjablonen en logica.
- **Azure Integratie:** Maakt gebruik van Azure OpenAI voor begrip van natuurlijke taal en Azure AI Search voor data-opvraging.
- **Beveiliging:** Integreert met Microsoft Entra ID voor authenticatie en past het principe van minste rechten toe op alle resources.
- **Implementatie:** Ondersteunt uitrol naar Azure Container Apps voor schaalbaarheid en operationele efficiëntie.

## Resultaten en Impact
- Toont aan hoe MCP kan worden gebruikt om meerdere AI-agents te orkestreren in een scenario van productiekwaliteit uit de praktijk.
- Versnelt de ontwikkeling van oplossingen door herbruikbare patronen te bieden voor agentcoördinatie, dataintegratie en veilige implementatie.
- Dient als blauwdruk voor het bouwen van domeinspecifieke, AI-gestuurde applicaties met MCP en Azure-diensten.

## Referenties
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.