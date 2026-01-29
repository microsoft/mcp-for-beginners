# Fallstudie: Azure AI Travel Agents – Referensimplementation

## Översikt

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) är en omfattande referenslösning utvecklad av Microsoft som visar hur man bygger en AI-driven reseplaneringsapplikation med flera agenter, baserad på Model Context Protocol (MCP), Azure OpenAI och Azure AI Search. Projektet demonstrerar bästa praxis för att samordna flera AI-agenter, integrera företagsdata och erbjuda en säker, utbyggbar plattform för verkliga scenarier.

## Viktiga funktioner
- **Multi-Agent Orkestrering:** Använder MCP för att koordinera specialiserade agenter (t.ex. FlightAgent, HotelAgent och ItineraryAgent) som samarbetar för att lösa komplexa reseplaneringsuppgifter.
- **Integration av företagsdata:** Kopplar till Azure AI Search och andra företagsdatakällor för att tillhandahålla aktuell och relevant information för reseförslag.
- **Säker och skalbar arkitektur:** Utnyttjar Azure-tjänster för autentisering, auktorisering och skalbar distribution, enligt företagets säkerhetsriktlinjer.
- **Utbyggbara verktyg:** Implementerar återanvändbara MCP-verktyg och promptmallar, vilket möjliggör snabb anpassning till nya domäner eller affärsbehov.
- **Användarupplevelse:** Erbjuder ett konversationsgränssnitt där användare kan interagera med reseagenterna, drivet av Azure OpenAI och MCP.

## Arkitektur
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Beskrivning av arkitekturdiagrammet

Azure AI Travel Agents-lösningen är designad för modularitet, skalbarhet och säker integration av flera AI-agenter och företagsdatakällor. Huvudkomponenterna och dataflödet är följande:

- **Användargränssnitt:** Användare interagerar med systemet via ett konversationsgränssnitt (t.ex. webchatt eller Teams-bot) som skickar användarfrågor och tar emot reseförslag.
- **MCP Server:** Fungerar som central orkestrator, tar emot användarinmatning, hanterar kontext och koordinerar specialiserade agenters (t.ex. FlightAgent, HotelAgent, ItineraryAgent) åtgärder via Model Context Protocol.
- **AI-agenter:** Varje agent ansvarar för ett specifikt område (flyg, hotell, resplaner) och implementeras som ett MCP-verktyg. Agenterna använder promptmallar och logik för att bearbeta förfrågningar och generera svar.
- **Azure OpenAI Service:** Tillhandahåller avancerad förståelse och generering av naturligt språk, vilket gör att agenterna kan tolka användarens avsikt och skapa konversationssvar.
- **Azure AI Search & företagsdata:** Agenterna söker i Azure AI Search och andra företagsdatakällor för att hämta aktuell information om flyg, hotell och resealternativ.
- **Autentisering & säkerhet:** Integreras med Microsoft Entra ID för säker autentisering och tillämpar principen om minsta privilegium för åtkomstkontroller till alla resurser.
- **Distribution:** Designad för distribution på Azure Container Apps, vilket säkerställer skalbarhet, övervakning och driftseffektivitet.

Denna arkitektur möjliggör sömlös orkestrering av flera AI-agenter, säker integration med företagsdata och en robust, utbyggbar plattform för att bygga domänspecifika AI-lösningar.

## Steg-för-steg förklaring av arkitekturdiagrammet
Föreställ dig att du planerar en stor resa och har ett team av experthjälpare som hjälper dig med varje detalj. Azure AI Travel Agents-systemet fungerar på liknande sätt, med olika delar (som teammedlemmar) som var och en har en speciell uppgift. Så här hänger allt ihop:

### Användargränssnitt (UI):
Tänk på detta som din reseagents reception. Här ställer du frågor eller gör förfrågningar, som ”Hitta en flygning till Paris.” Det kan vara ett chattfönster på en webbplats eller en meddelandeapp.

### MCP Server (Koordinatorn):
MCP Server är som chefen som lyssnar på din förfrågan vid receptionen och bestämmer vilken specialist som ska hantera varje del. Den håller koll på din konversation och ser till att allt flyter på smidigt.

### AI-agenter (Specialistassistenter):
Varje agent är expert inom ett specifikt område – en kan allt om flyg, en annan om hotell och en tredje om att planera din resrutt. När du ber om en resa skickar MCP Server din förfrågan till rätt agent(er). Dessa agenter använder sin kunskap och sina verktyg för att hitta de bästa alternativen för dig.

### Azure OpenAI Service (Språkexpert):
Det här är som att ha en språkexpert som förstår exakt vad du menar, oavsett hur du uttrycker dig. Den hjälper agenterna att tolka dina förfrågningar och svara på ett naturligt, konverserande sätt.

### Azure AI Search & företagsdata (Informationsbibliotek):
Föreställ dig ett enormt, uppdaterat bibliotek med all senaste reseinformation – flygtider, hotellbokningar och mer. Agenterna söker i detta bibliotek för att ge dig de mest korrekta svaren.

### Autentisering & säkerhet (Vakt):
Precis som en vakt kontrollerar vem som får komma in på vissa områden, ser denna del till att bara behöriga personer och agenter kan komma åt känslig information. Den skyddar dina data och din integritet.

### Distribution på Azure Container Apps (Byggnaden):
Alla dessa assistenter och verktyg arbetar tillsammans i en säker, skalbar byggnad (molnet). Det betyder att systemet kan hantera många användare samtidigt och alltid finns tillgängligt när du behöver det.

## Hur allt fungerar tillsammans:

Du börjar med att ställa en fråga vid receptionen (UI).  
Chefen (MCP Server) avgör vilken specialist (agent) som ska hjälpa dig.  
Specialisten använder språkexperten (OpenAI) för att förstå din förfrågan och biblioteket (AI Search) för att hitta bästa svaret.  
Vakten (Autentisering) ser till att allt är säkert.  
Allt detta sker i en pålitlig, skalbar byggnad (Azure Container Apps), så din upplevelse blir smidig och trygg.  
Detta samarbete gör att systemet snabbt och säkert kan hjälpa dig att planera din resa, precis som ett team av expertresesäljare som jobbar tillsammans på ett modernt kontor!

## Teknisk implementation
- **MCP Server:** Hanterar kärnlogiken för orkestrering, exponerar agentverktyg och hanterar kontext för flerstegs reseplaneringsflöden.
- **Agenter:** Varje agent (t.ex. FlightAgent, HotelAgent) implementeras som ett MCP-verktyg med egna promptmallar och logik.
- **Azure-integration:** Använder Azure OpenAI för förståelse av naturligt språk och Azure AI Search för datahämtning.
- **Säkerhet:** Integreras med Microsoft Entra ID för autentisering och tillämpar principen om minsta privilegium för åtkomstkontroller.
- **Distribution:** Stöder distribution till Azure Container Apps för skalbarhet och driftseffektivitet.

## Resultat och påverkan
- Visar hur MCP kan användas för att samordna flera AI-agenter i ett verkligt, produktionsklart scenario.
- Påskyndar lösningsutveckling genom att erbjuda återanvändbara mönster för agentkoordinering, dataintegration och säker distribution.
- Fungerar som en mall för att bygga domänspecifika, AI-drivna applikationer med MCP och Azure-tjänster.

## Referenser
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.