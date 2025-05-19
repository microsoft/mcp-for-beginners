<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:32:55+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "nl"
}
-->
# Lessen van vroege gebruikers

## Overzicht

Deze les onderzoekt hoe vroege gebruikers het Model Context Protocol (MCP) hebben ingezet om echte uitdagingen op te lossen en innovatie in verschillende sectoren te stimuleren. Aan de hand van gedetailleerde casestudy's en praktische projecten zie je hoe MCP gestandaardiseerde, veilige en schaalbare AI-integratie mogelijk maakt—door grote taalmodellen, tools en bedrijfsdata te verbinden in één uniform kader. Je krijgt praktische ervaring met het ontwerpen en bouwen van MCP-gebaseerde oplossingen, leert van bewezen implementatiepatronen en ontdekt best practices voor het uitrollen van MCP in productieomgevingen. De les belicht ook opkomende trends, toekomstige richtingen en open-source bronnen om je te helpen voorop te blijven lopen in MCP-technologie en het zich ontwikkelende ecosysteem.

## Leerdoelen

- Analyseer echte MCP-implementaties in verschillende sectoren  
- Ontwerp en bouw complete MCP-gebaseerde applicaties  
- Verken opkomende trends en toekomstige richtingen in MCP-technologie  
- Pas best practices toe in praktische ontwikkelscenario's  

## Echte MCP-implementaties

### Casestudy 1: Enterprise Klantenservice Automatisering

Een multinational implementeerde een MCP-gebaseerde oplossing om AI-interacties binnen hun klantenservicesystemen te standaardiseren. Dit stelde hen in staat om:

- Een uniforme interface te creëren voor meerdere LLM-aanbieders  
- Consistent promptbeheer te behouden tussen afdelingen  
- Robuuste beveiligings- en compliance-controles te implementeren  
- Gemakkelijk te wisselen tussen verschillende AI-modellen op basis van specifieke behoeften  

**Technische implementatie:**  
```python
# Python MCP server implementation for customer support
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# Configure logging
logging.basicConfig(level=logging.INFO)

async def main():
    # Create server configuration
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # Initialize MCP server
    server = create_server(config)
    
    # Register knowledge base resources
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # Register prompt templates
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # Register support tools
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # Start server with HTTP transport
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**Resultaten:** 30% reductie in modelkosten, 45% verbetering in consistentie van antwoorden, en verbeterde compliance wereldwijd.

### Casestudy 2: Diagnostische Assistent in de Zorg

Een zorgaanbieder ontwikkelde een MCP-infrastructuur om meerdere gespecialiseerde medische AI-modellen te integreren, terwijl gevoelige patiëntgegevens beschermd bleven:

- Naadloze wisseling tussen generalistische en specialistische medische modellen  
- Strikte privacycontroles en audit-trails  
- Integratie met bestaande Elektronische Patiëntendossiers (EHR)  
- Consistente prompt-engineering voor medische terminologie  

**Technische implementatie:**  
```csharp
// C# MCP host application implementation in healthcare application
using Microsoft.Extensions.DependencyInjection;
using ModelContextProtocol.SDK.Client;
using ModelContextProtocol.SDK.Security;
using ModelContextProtocol.SDK.Resources;

public class DiagnosticAssistant
{
    private readonly MCPHostClient _mcpClient;
    private readonly PatientContext _patientContext;
    
    public DiagnosticAssistant(PatientContext patientContext)
    {
        _patientContext = patientContext;
        
        // Configure MCP client with healthcare-specific settings
        var clientOptions = new ClientOptions
        {
            Name = "Healthcare Diagnostic Assistant",
            Version = "1.0.0",
            Security = new SecurityOptions
            {
                Encryption = EncryptionLevel.Medical,
                AuditEnabled = true
            }
        };
        
        _mcpClient = new MCPHostClientBuilder()
            .WithOptions(clientOptions)
            .WithTransport(new HttpTransport("https://healthcare-mcp.example.org"))
            .WithAuthentication(new HIPAACompliantAuthProvider())
            .Build();
    }
    
    public async Task<DiagnosticSuggestion> GetDiagnosticAssistance(
        string symptoms, string patientHistory)
    {
        // Create request with appropriate resources and tool access
        var resourceRequest = new ResourceRequest
        {
            Name = "patient_records",
            Parameters = new Dictionary<string, object>
            {
                ["patientId"] = _patientContext.PatientId,
                ["requestingProvider"] = _patientContext.ProviderId
            }
        };
        
        // Request diagnostic assistance using appropriate prompt
        var response = await _mcpClient.SendPromptRequestAsync(
            promptName: "diagnostic_assistance",
            parameters: new Dictionary<string, object>
            {
                ["symptoms"] = symptoms,
                patientHistory = patientHistory,
                relevantGuidelines = _patientContext.GetRelevantGuidelines()
            });
            
        return DiagnosticSuggestion.FromMCPResponse(response);
    }
}
```

**Resultaten:** Verbeterde diagnostische suggesties voor artsen met volledige HIPAA-compliance en aanzienlijke vermindering van contextwisselingen tussen systemen.

### Casestudy 3: Risicoanalyse in Financiële Diensten

Een financiële instelling implementeerde MCP om hun risicoanalyseprocessen te standaardiseren over verschillende afdelingen:

- Een uniforme interface voor kredietrisico, fraudedetectie en investeringsrisicomodellen  
- Strikte toegangscontroles en modelversiebeheer  
- Auditbaarheid van alle AI-aanbevelingen gewaarborgd  
- Consistente dataformattering over diverse systemen  

**Technische implementatie:**  
```java
// Java MCP server for financial risk assessment
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // Create MCP server with financial compliance features
        MCPServer server = new MCPServerBuilder()
            .withModelProviders(
                new ModelProvider("risk-assessment-primary", new AzureOpenAIProvider()),
                new ModelProvider("risk-assessment-audit", new LocalLlamaProvider())
            )
            .withPromptTemplateDirectory("./compliance/templates")
            .withAccessControls(new SOCCompliantAccessControl())
            .withDataEncryption(EncryptionStandard.FINANCIAL_GRADE)
            .withVersionControl(true)
            .withAuditLogging(new DatabaseAuditLogger())
            .build();
            
        server.addRequestValidator(new FinancialDataValidator());
        server.addResponseFilter(new PII_RedactionFilter());
        
        server.start(9000);
        
        System.out.println("Financial Risk MCP Server running on port 9000");
    }
}
```

**Resultaten:** Verbeterde naleving van regelgeving, 40% snellere uitrol van modellen, en verbeterde consistentie in risicobeoordeling over afdelingen.

### Casestudy 4: Microsoft Playwright MCP Server voor Browserautomatisering

Microsoft ontwikkelde de [Playwright MCP server](https://github.com/microsoft/playwright-mcp) om veilige, gestandaardiseerde browserautomatisering mogelijk te maken via het Model Context Protocol. Deze oplossing stelt AI-agenten en LLM’s in staat om op een gecontroleerde, controleerbare en uitbreidbare manier met webbrowsers te communiceren—waardoor use cases zoals geautomatiseerd webtesten, data-extractie en end-to-end workflows mogelijk worden.

- Browserautomatiseringsfuncties (navigatie, formulier invullen, screenshots maken, etc.) als MCP-tools beschikbaar  
- Strikte toegangscontroles en sandboxing ter voorkoming van ongeautoriseerde acties  
- Gedetailleerde auditlogs van alle browserinteracties  
- Ondersteuning voor integratie met Azure OpenAI en andere LLM-aanbieders voor agentgestuurde automatisering  

**Technische implementatie:**  
```typescript
// TypeScript: Registering Playwright browser automation tools in an MCP server
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// Register a tool for navigating to a URL and capturing a screenshot
server.tools.register(
  new ToolDefinition({
    name: 'navigate_and_screenshot',
    description: 'Navigate to a URL and capture a screenshot',
    parameters: {
      url: { type: 'string', description: 'The URL to visit' }
    }
  }),
  async ({ url }) => {
    const browser = await launch();
    const page = await browser.newPage();
    await page.goto(url);
    const screenshot = await page.screenshot();
    await browser.close();
    return { screenshot };
  }
);

// Start the MCP server
server.listen(8080);
```

**Resultaten:**  
- Veilige, programmeerbare browserautomatisering voor AI-agenten en LLM’s mogelijk gemaakt  
- Vermindering van handmatige testinspanningen en verbetering van testdekking voor webapplicaties  
- Een herbruikbaar, uitbreidbaar framework voor browsergebaseerde toolintegratie in enterprise-omgevingen  

**Referenties:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### Casestudy 5: Azure MCP – Enterprise-Grade Model Context Protocol als Service

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) is Microsoft’s beheerde, enterprise-grade implementatie van het Model Context Protocol, ontworpen om schaalbare, veilige en compliant MCP-serverfunctionaliteit als cloudservice te bieden. Azure MCP stelt organisaties in staat om MCP-servers snel uit te rollen, te beheren en te integreren met Azure AI, data- en beveiligingsdiensten, waardoor operationele lasten verminderen en AI-adoptie versnelt.

- Volledig beheerde MCP-serverhosting met ingebouwde schaalbaarheid, monitoring en beveiliging  
- Native integratie met Azure OpenAI, Azure AI Search en andere Azure-diensten  
- Enterprise-authenticatie en autorisatie via Microsoft Entra ID  
- Ondersteuning voor aangepaste tools, prompttemplates en resource connectors  
- Naleving van enterprise beveiligings- en regelgevingsvereisten  

**Technische implementatie:**  
```yaml
# Example: Azure MCP server deployment configuration (YAML)
apiVersion: mcp.microsoft.com/v1
kind: McpServer
metadata:
  name: enterprise-mcp-server
spec:
  modelProviders:
    - name: azure-openai
      type: AzureOpenAI
      endpoint: https://<your-openai-resource>.openai.azure.com/
      apiKeySecret: <your-azure-keyvault-secret>
  tools:
    - name: document_search
      type: AzureAISearch
      endpoint: https://<your-search-resource>.search.windows.net/
      apiKeySecret: <your-azure-keyvault-secret>
  authentication:
    type: EntraID
    tenantId: <your-tenant-id>
  monitoring:
    enabled: true
    logAnalyticsWorkspace: <your-log-analytics-id>
```

**Resultaten:**  
- Verkortte time-to-value voor enterprise AI-projecten door een kant-en-klare, compliant MCP-serverplatform te bieden  
- Vereenvoudigde integratie van LLM’s, tools en bedrijfsdatasources  
- Verbeterde beveiliging, observeerbaarheid en operationele efficiëntie voor MCP workloads  

**Referenties:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## Casestudy 6: NLWeb  
MCP (Model Context Protocol) is een opkomend protocol waarmee chatbots en AI-assistenten kunnen communiceren met tools. Elke NLWeb-instantie is ook een MCP-server die één kernmethode ondersteunt, ask, waarmee je een website een vraag in natuurlijke taal kunt stellen. Het antwoord maakt gebruik van schema.org, een veelgebruikte vocabulaire om webdata te beschrijven. Vrij vertaald is MCP voor NLWeb wat HTTP is voor HTML. NLWeb combineert protocollen, Schema.org-formaten en voorbeeldcode om sites snel deze endpoints te laten maken, wat zowel mensen via conversatie-interfaces als machines via natuurlijke agent-naar-agent interactie ten goede komt.

NLWeb bestaat uit twee aparte componenten:  
- Een protocol, heel eenvoudig om mee te starten, om in natuurlijke taal met een site te communiceren en een formaat dat json en schema.org gebruikt voor het antwoord. Zie de documentatie over de REST API voor meer details.  
- Een eenvoudige implementatie van (1) die bestaande markup gebruikt, voor sites die geabstraheerd kunnen worden als lijsten met items (producten, recepten, attracties, reviews, etc.). Samen met een set gebruikersinterface-widgets kunnen sites gemakkelijk conversatie-interfaces voor hun content bieden. Zie de documentatie over Life of a chat query voor meer uitleg.  

**Referenties:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## Praktische projecten

### Project 1: Bouw een Multi-Provider MCP Server

**Doel:** Maak een MCP-server die verzoeken kan routeren naar meerdere AI-modelaanbieders op basis van specifieke criteria.

**Vereisten:**  
- Ondersteuning voor minimaal drie verschillende modelaanbieders (bijv. OpenAI, Anthropic, lokale modellen)  
- Implementeer een routeringsmechanisme gebaseerd op metadata van verzoeken  
- Creëer een configuratiesysteem voor beheer van provider-credentials  
- Voeg caching toe om prestaties en kosten te optimaliseren  
- Bouw een eenvoudig dashboard voor gebruiksmonitoring  

**Implementatiestappen:**  
1. Zet de basisinfrastructuur van de MCP-server op  
2. Implementeer provider-adapters voor elke AI-modelservice  
3. Maak de routeringslogica op basis van verzoekattributen  
4. Voeg cachingmechanismen toe voor veelvoorkomende verzoeken  
5. Ontwikkel het monitoring-dashboard  
6. Test met verschillende verzoekpatronen  

**Technologieën:** Kies uit Python (.NET/Java/Python naar voorkeur), Redis voor caching en een eenvoudig webframework voor het dashboard.

### Project 2: Enterprise Prompt Management Systeem

**Doel:** Ontwikkel een MCP-gebaseerd systeem voor het beheren, versioneren en uitrollen van prompt-templates binnen een organisatie.

**Vereisten:**  
- Creëer een gecentraliseerde opslagplaats voor prompt-templates  
- Implementeer versiebeheer en goedkeuringsworkflows  
- Bouw testmogelijkheden voor templates met voorbeeldinputs  
- Ontwikkel rolgebaseerde toegangscontroles  
- Maak een API voor het ophalen en uitrollen van templates  

**Implementatiestappen:**  
1. Ontwerp het databaseschema voor template-opslag  
2. Maak de kern-API voor CRUD-operaties op templates  
3. Implementeer het versiebeheersysteem  
4. Bouw de goedkeuringsworkflow  
5. Ontwikkel het testframework  
6. Maak een eenvoudige webinterface voor beheer  
7. Integreer met een MCP-server  

**Technologieën:** Je keuze van backend-framework, SQL of NoSQL database en frontend-framework voor de beheerinterface.

### Project 3: MCP-gebaseerd Contentgeneratieplatform

**Doel:** Bouw een contentgeneratieplatform dat MCP gebruikt om consistente resultaten te leveren voor verschillende contenttypes.

**Vereisten:**  
- Ondersteuning voor meerdere contentformaten (blogposts, social media, marketingteksten)  
- Template-gebaseerde generatie met aanpassingsopties  
- Creëer een contentreview- en feedbacksysteem  
- Volg contentprestatie-metrics  
- Ondersteuning voor contentversiebeheer en iteratie  

**Implementatiestappen:**  
1. Zet de MCP-clientinfrastructuur op  
2. Maak templates voor verschillende contenttypes  
3. Bouw de contentgeneratie-pijplijn  
4. Implementeer het reviewsysteem  
5. Ontwikkel het metrics tracking-systeem  
6. Maak een gebruikersinterface voor templatebeheer en contentgeneratie  

**Technologieën:** Je favoriete programmeertaal, webframework en databasesysteem.

## Toekomstige richtingen voor MCP-technologie

### Opkomende trends

1. **Multi-Modal MCP**  
   - Uitbreiding van MCP om interacties met beeld-, audio- en videomodellen te standaardiseren  
   - Ontwikkeling van cross-modale redeneermogelijkheden  
   - Gestandaardiseerde promptformaten voor verschillende modaliteiten  

2. **Gefedereerde MCP-infrastructuur**  
   - Gedistribueerde MCP-netwerken die resources kunnen delen tussen organisaties  
   - Gestandaardiseerde protocollen voor veilige modeldeling  
   - Privacybewarende rekenmethoden  

3. **MCP-marktplaatsen**  
   - Ecosystemen voor het delen en vermarkten van MCP-templates en plugins  
   - Kwaliteitsborging en certificeringsprocessen  
   - Integratie met modelmarktplaatsen  

4. **MCP voor Edge Computing**  
   - Aanpassing van MCP-standaarden voor resource-beperkte edge-apparaten  
   - Geoptimaliseerde protocollen voor omgevingen met lage bandbreedte  
   - Gespecialiseerde MCP-implementaties voor IoT-ecosystemen  

5. **Regelgevingskaders**  
   - Ontwikkeling van MCP-uitbreidingen voor naleving van regelgeving  
   - Gestandaardiseerde audit-trails en uitlegbaarheidsinterfaces  
   - Integratie met opkomende AI-governance frameworks  

### MCP-oplossingen van Microsoft

Microsoft en Azure hebben diverse open-source repositories ontwikkeld om ontwikkelaars te helpen MCP in verschillende scenario’s te implementeren:

#### Microsoft-organisatie  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - Een Playwright MCP-server voor browserautomatisering en testen  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - Een OneDrive MCP-serverimplementatie voor lokaal testen en communitybijdragen  
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWeb is een verzameling open protocollen en bijbehorende open source tools. De focus ligt op het creëren van een fundamentele laag voor het AI Web  

#### Azure-Samples-organisatie  
1. [mcp](https://github.com/Azure-Samples/mcp) - Links naar voorbeelden, tools en bronnen voor het bouwen en integreren van MCP-servers op Azure met verschillende talen  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - Referentie-MCP-servers die authenticatie demonstreren volgens de huidige Model Context Protocol-specificatie  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Landingspagina voor Remote MCP Server-implementaties in Azure Functions met links naar taalspecifieke repositories  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Quickstart-template voor het bouwen en uitrollen van custom remote MCP-servers met Azure Functions in Python  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Quickstart-template voor het bouwen en uitrollen van custom remote MCP-servers met Azure Functions in .NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Quickstart-template voor het bouwen en uitrollen van custom remote MCP-servers met Azure Functions in TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Azure API Management als AI Gateway naar Remote MCP-servers met Python  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI-experimenten inclusief MCP-functionaliteiten, integratie met Azure OpenAI en AI Foundry  

Deze repositories bieden diverse implementaties, templates en bronnen voor het werken met het Model Context Protocol in verschillende programmeertalen en Azure-diensten. Ze bestrijken uiteenlopende use cases, van basisserverimplementaties tot authenticatie, clouddeployment en enterprise-integratie.

#### MCP Resources Directory

De [MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) in de officiële Microsoft MCP-repository bevat een zorgvuldig samengestelde collectie voorbeeldbronnen, prompttemplates en tooldefinities voor gebruik met Model Context Protocol-servers. Deze directory helpt ontwikkelaars snel aan de slag te gaan met MCP door herbruikbare bouwstenen en best-practice voorbeelden te bieden voor:

- **Prompt Templates:** Klaar-voor-gebruik prompttemplates voor veelvoorkomende AI-taken en scenario’s, aanpasbaar voor eigen MCP-serverimplementaties.  
- **Tool Definitions:** Voorbeeld toolschemas en metadata om toolintegratie en -aanroepen te standaardiseren over verschillende MCP-servers.  
- **Resource Samples:** Voorbeeld resource-definities voor koppeling met databronnen, API’s en externe diensten binnen het MCP-framework.  
- **Reference Implementations:** Praktische voorbeelden die laten zien hoe resources, prompts en tools gestructureerd en georganiseerd kunnen worden in echte MCP-projecten.  

Deze bronnen versnellen ontwikkeling, bevorderen standaardisatie en helpen best practices te waarborgen bij het bouwen en uitrollen van MCP-gebaseerde oplossingen.

#### MCP Resources Directory  
- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)

### Onderzoeksmogelijkheden

- Efficiënte promptoptimalisatietechnieken binnen MCP-frameworks  
- Beveiligingsmodellen voor multi-tenant MCP-implementaties  
- Prestatiebenchmarking van verschillende MCP-implementaties  
- Formele verificatiemethoden voor MCP-servers  

## Conclusie

Het Model Context Protocol (MCP) vormt snel de toekomst van gestandaardiseerde, veilige en interoperabele AI-integratie in diverse sectoren. Via de casestudy's en hands-on projecten in deze les heb je gezien hoe vroege gebruikers—waaronder Microsoft en Azure—MCP inzetten om echte uitdagingen op te lossen, AI-adoptie te versnellen en compliance, beveiliging en schaalbaarheid te waarborgen. De modulaire aanpak van MCP stelt organisaties in staat grote taalmodellen, tools en bedrijfsdata te verbinden in een uniform, controleerbaar kader. Terwijl MCP zich blijft ontwikkelen, is het belangrijk om betrokken te blijven bij de community, open-source bronnen te verkennen en best practices toe te passen om robuuste, toekomstbestendige AI-oplossingen te bouwen.

## Aanvullende bronnen

- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)  
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)  
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Files MCP Server (OneDrive)](https://github.com/microsoft/files-mcp-server)  
- [Azure-Samples MCP](https://github.com/Azure-Samples/mcp)  
- [MCP Auth Servers (Azure-Samples)](https://github.com/Azure-Samples/mcp-auth-servers)  
- [Remote MCP Functions (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions)
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Oefeningen

1. Analyseer een van de casestudy’s en stel een alternatieve implementatie-aanpak voor.
2. Kies een van de projectideeën en maak een gedetailleerde technische specificatie.
3. Onderzoek een branche die niet in de casestudy’s wordt behandeld en schets hoe MCP de specifieke uitdagingen daarvan kan aanpakken.
4. Verken een van de toekomstige richtingen en bedenk een concept voor een nieuwe MCP-uitbreiding ter ondersteuning daarvan.

Volgende: [Best Practices](../08-BestPractices/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.