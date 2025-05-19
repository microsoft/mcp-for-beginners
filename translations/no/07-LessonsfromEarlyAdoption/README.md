<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:29:35+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "no"
}
-->
# Lærdommer fra tidlige brukere

## Oversikt

Denne leksjonen utforsker hvordan tidlige brukere har utnyttet Model Context Protocol (MCP) for å løse reelle utfordringer og drive innovasjon på tvers av bransjer. Gjennom detaljerte casestudier og praktiske prosjekter vil du se hvordan MCP muliggjør standardisert, sikker og skalerbar AI-integrasjon – ved å koble store språkmodeller, verktøy og bedriftsdata i en samlet rammeverk. Du vil få praktisk erfaring med å designe og bygge løsninger basert på MCP, lære av velprøvde implementeringsmønstre, og oppdage beste praksis for utrulling av MCP i produksjonsmiljøer. Leksjonen fremhever også nye trender, fremtidige retninger og åpne kildekode-ressurser som hjelper deg å holde deg i forkant av MCP-teknologien og dens stadig utviklende økosystem.

## Læringsmål

- Analysere reelle MCP-implementeringer på tvers av ulike bransjer  
- Designe og bygge komplette MCP-baserte applikasjoner  
- Utforske nye trender og fremtidige retninger innen MCP-teknologi  
- Anvende beste praksis i faktiske utviklingsscenarier  

## Reelle MCP-implementeringer

### Casestudie 1: Automatisering av kundestøtte i bedrifter

Et multinasjonalt selskap implementerte en MCP-basert løsning for å standardisere AI-interaksjoner på tvers av deres kundestøttesystemer. Dette gjorde det mulig å:

- Lage et samlet grensesnitt for flere LLM-leverandører  
- Opprettholde konsekvent prompt-håndtering på tvers av avdelinger  
- Implementere robuste sikkerhets- og samsvarskontroller  
- Enkelt bytte mellom ulike AI-modeller basert på spesifikke behov  

**Teknisk implementering:**  
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

**Resultater:** 30 % reduksjon i modellkostnader, 45 % forbedring i responssamsvar, og økt samsvar på tvers av globale operasjoner.

### Casestudie 2: Helsevesen – diagnostisk assistent

En helseleverandør utviklet en MCP-infrastruktur for å integrere flere spesialiserte medisinske AI-modeller samtidig som sensitiv pasientdata ble beskyttet:

- Sømløs veksling mellom generelle og spesialiserte medisinske modeller  
- Strenge personvernkontroller og revisjonsspor  
- Integrasjon med eksisterende elektroniske pasientjournaler (EHR)  
- Konsistent prompt-design for medisinsk terminologi  

**Teknisk implementering:**  
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

**Resultater:** Forbedrede diagnostiske forslag for leger, full HIPAA-samsvar og betydelig reduksjon i kontekstbytte mellom systemer.

### Casestudie 3: Finans – risikovurdering

En finansinstitusjon implementerte MCP for å standardisere risikovurderingsprosesser på tvers av ulike avdelinger:

- Laget et samlet grensesnitt for modeller innen kreditt-, svindel- og investeringsrisiko  
- Implementerte strenge tilgangskontroller og modellversjonering  
- Sikret revisjonsmuligheter for alle AI-anbefalinger  
- Opprettholdt konsekvent dataformat på tvers av ulike systemer  

**Teknisk implementering:**  
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

**Resultater:** Forbedret regulatorisk samsvar, 40 % raskere modellutrullingssykluser, og økt konsistens i risikovurderinger på tvers av avdelinger.

### Casestudie 4: Microsoft Playwright MCP-server for nettleserautomatisering

Microsoft utviklet [Playwright MCP-serveren](https://github.com/microsoft/playwright-mcp) for å muliggjøre sikker, standardisert nettleserautomatisering gjennom Model Context Protocol. Denne løsningen lar AI-agenter og LLM-er samhandle med nettlesere på en kontrollert, revisjonsbar og utvidbar måte – og støtter brukstilfeller som automatisert webtesting, datauttrekk og helhetlige arbeidsflyter.

- Eksponerer nettleserautomatiseringsfunksjoner (navigasjon, skjemautfylling, skjermbildeopptak osv.) som MCP-verktøy  
- Implementerer strenge tilgangskontroller og sandkassemiljø for å forhindre uautoriserte handlinger  
- Gir detaljerte revisjonslogger for alle nettleserinteraksjoner  
- Støtter integrasjon med Azure OpenAI og andre LLM-leverandører for agentdrevet automatisering  

**Teknisk implementering:**  
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

**Resultater:**  
- Muliggjorde sikker, programmatisk nettleserautomatisering for AI-agenter og LLM-er  
- Reduserte manuelt testarbeid og forbedret testdekning for webapplikasjoner  
- Levererte et gjenbrukbart og utvidbart rammeverk for nettleserbasert verktøyintegrasjon i bedriftsmiljøer  

**Referanser:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)  

### Casestudie 5: Azure MCP – Enterprise-klasse Model Context Protocol som tjeneste

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) er Microsofts administrerte, enterprise-klare implementering av Model Context Protocol, designet for å tilby skalerbare, sikre og samsvarende MCP-serverkapasiteter som en skybasert tjeneste. Azure MCP gjør det mulig for organisasjoner å raskt distribuere, administrere og integrere MCP-servere med Azure AI, data og sikkerhetstjenester, noe som reduserer driftskostnader og akselererer AI-adopsjon.

- Fullt administrert MCP-serverhosting med innebygd skalering, overvåking og sikkerhet  
- Native integrasjon med Azure OpenAI, Azure AI Search og andre Azure-tjenester  
- Enterprise-autentisering og autorisasjon via Microsoft Entra ID  
- Støtte for tilpassede verktøy, promptmaler og ressurskoblinger  
- Samsvar med bedriftens sikkerhets- og regulatoriske krav  

**Teknisk implementering:**  
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

**Resultater:**  
- Redusert tid til verdi for bedrifts-AI-prosjekter ved å tilby en ferdig, samsvarende MCP-serverplattform  
- Forenklet integrasjon av LLM-er, verktøy og bedriftsdatakilder  
- Økt sikkerhet, observasjonsevne og driftseffektivitet for MCP-arbeidsbelastninger  

**Referanser:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)  

## Casestudie 6: NLWeb

MCP (Model Context Protocol) er en ny protokoll for chatboter og AI-assistenter som skal samhandle med verktøy. Hver NLWeb-instans er også en MCP-server som støtter én kjernefunksjon, ask, som brukes for å stille et nettsted et spørsmål på naturlig språk. Det returnerte svaret bruker schema.org, et mye brukt vokabular for å beskrive webdata. Forenklet sagt er MCP for NLWeb det Http er for HTML. NLWeb kombinerer protokoller, Schema.org-formater og eksempelkode for å hjelpe nettsteder raskt å opprette disse endepunktene, noe som gagner både mennesker gjennom samtalegrensesnitt og maskiner gjennom naturlig agent-til-agent-interaksjon.

NLWeb består av to distinkte komponenter:  
- En protokoll, veldig enkel å begynne med, for å kommunisere med et nettsted på naturlig språk og et format som bruker json og schema.org for det returnerte svaret. Se dokumentasjonen for REST API for mer informasjon.  
- En enkel implementering av (1) som utnytter eksisterende markup, for nettsteder som kan abstrakteres som lister av elementer (produkter, oppskrifter, attraksjoner, anmeldelser osv.). Sammen med et sett brukergrensesnitt-widgeter kan nettsteder enkelt tilby samtalegrensesnitt til innholdet sitt. Se dokumentasjonen for Life of a chat query for mer informasjon om hvordan dette fungerer.  

**Referanser:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)  

## Praktiske prosjekter

### Prosjekt 1: Bygg en MCP-server med flere leverandører

**Mål:** Lag en MCP-server som kan rute forespørsler til flere AI-modelleverandører basert på bestemte kriterier.

**Krav:**  
- Støtte minst tre ulike modellleverandører (f.eks. OpenAI, Anthropic, lokale modeller)  
- Implementere en rutemekanisme basert på metadata i forespørselen  
- Lage et konfigurasjonssystem for håndtering av leverandørlegitimasjon  
- Legge til caching for å optimalisere ytelse og kostnader  
- Bygge et enkelt dashbord for overvåking av bruk  

**Implementeringstrinn:**  
1. Sett opp grunnleggende MCP-serverinfrastruktur  
2. Implementer adaptere for hver AI-modelltjeneste  
3. Lag rutelogikk basert på forespørselsattributter  
4. Legg til cachingmekanismer for hyppige forespørsler  
5. Utvikle overvåkingsdashbord  
6. Test med ulike forespørselsmønstre  

**Teknologier:** Velg blant Python (.NET/Java/Python etter preferanse), Redis for caching og et enkelt web-rammeverk for dashbordet.

### Prosjekt 2: Enterprise prompt-administrasjonssystem

**Mål:** Utvikle et MCP-basert system for å håndtere, versjonere og distribuere promptmaler i en organisasjon.

**Krav:**  
- Lag et sentralisert depot for promptmaler  
- Implementer versjonering og godkjenningsflyter  
- Bygg testfunksjoner for maler med eksempler på input  
- Utvikle rollebaserte tilgangskontroller  
- Lag et API for henting og distribusjon av maler  

**Implementeringstrinn:**  
1. Design databaseskjema for lagring av maler  
2. Lag kjernen i API-et for CRUD-operasjoner på maler  
3. Implementer versjoneringssystemet  
4. Bygg godkjenningsflyt  
5. Utvikle testrammeverk  
6. Lag et enkelt webgrensesnitt for administrasjon  
7. Integrer med en MCP-server  

**Teknologier:** Valgfritt backend-rammeverk, SQL eller NoSQL-database, og frontend-rammeverk for administrasjonsgrensesnittet.

### Prosjekt 3: MCP-basert plattform for innholdsgenerering

**Mål:** Bygg en plattform for innholdsgenerering som bruker MCP for å gi konsistente resultater på tvers av ulike innholdstyper.

**Krav:**  
- Støtte flere innholdsformater (blogginnlegg, sosiale medier, markedsføringskopi)  
- Implementer malbasert generering med tilpasningsmuligheter  
- Lag et system for innholdsrevisjon og tilbakemelding  
- Spor ytelsesmetrikker for innhold  
- Støtt versjonering og iterasjon av innhold  

**Implementeringstrinn:**  
1. Sett opp MCP-klientinfrastruktur  
2. Lag maler for ulike innholdstyper  
3. Bygg innholdsgenereringspipeline  
4. Implementer revisjonssystem  
5. Utvikle metrikksystem for ytelsessporing  
6. Lag brukergrensesnitt for maladministrasjon og innholdsgenerering  

**Teknologier:** Valgt programmeringsspråk, web-rammeverk og databasesystem.

## Fremtidige retninger for MCP-teknologi

### Nye trender

1. **Multi-modalt MCP**  
   - Utvidelse av MCP for å standardisere interaksjoner med bilde-, lyd- og videomodeller  
   - Utvikling av tverrmodale resonneringsmuligheter  
   - Standardiserte prompt-formater for ulike modaliteter  

2. **Føderert MCP-infrastruktur**  
   - Distribuerte MCP-nettverk som kan dele ressurser på tvers av organisasjoner  
   - Standardiserte protokoller for sikker deling av modeller  
   - Personvernbevarende beregningsteknikker  

3. **MCP-markedsplasser**  
   - Økosystemer for deling og inntektsgenerering av MCP-maler og plugins  
   - Kvalitetssikring og sertifiseringsprosesser  
   - Integrasjon med modellmarkedsplasser  

4. **MCP for edge computing**  
   - Tilpasning av MCP-standarder for ressursbegrensede edge-enheter  
   - Optimaliserte protokoller for lavbåndbredde-miljøer  
   - Spesialiserte MCP-implementeringer for IoT-økosystemer  

5. **Regulatoriske rammeverk**  
   - Utvikling av MCP-utvidelser for regulatorisk samsvar  
   - Standardiserte revisjonsspor og forklaringsgrensesnitt  
   - Integrasjon med nye AI-styringsrammeverk  

### MCP-løsninger fra Microsoft

Microsoft og Azure har utviklet flere åpne kildekode-repositorier for å hjelpe utviklere med å implementere MCP i ulike scenarier:

#### Microsoft-organisasjonen  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) – En Playwright MCP-server for nettleserautomatisering og testing  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) – En OneDrive MCP-serverimplementering for lokal testing og fellesskapsbidrag  
3. [NLWeb](https://github.com/microsoft/NlWeb) – NLWeb er en samling av åpne protokoller og tilhørende åpne verktøy. Hovedfokus er å etablere et grunnleggende lag for AI Web  

#### Azure-Samples-organisasjonen  
1. [mcp](https://github.com/Azure-Samples/mcp) – Lenker til eksempler, verktøy og ressurser for bygging og integrasjon av MCP-servere på Azure med flere språk  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) – Referanse MCP-servere som demonstrerer autentisering med gjeldende Model Context Protocol-spesifikasjon  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) – Landingsside for Remote MCP Server-implementeringer i Azure Functions med lenker til språkspesifikke repos  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) – Hurtigstartmal for bygging og utrulling av tilpassede remote MCP-servere med Azure Functions i Python  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – Hurtigstartmal for bygging og utrulling av tilpassede remote MCP-servere med Azure Functions i .NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – Hurtigstartmal for bygging og utrulling av tilpassede remote MCP-servere med Azure Functions i TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) – Azure API Management som AI-gateway til Remote MCP-servere med Python  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) – APIM ❤️ AI-eksperimenter inkludert MCP-funksjonalitet, integrert med Azure OpenAI og AI Foundry  

Disse repositoriene tilbyr ulike implementeringer, maler og ressurser for arbeid med Model Context Protocol på tvers av programmeringsspråk og Azure-tjenester. De dekker en rekke brukstilfeller fra grunnleggende serverimplementeringer til autentisering, skyutrulling og bedriftsintegrasjon.

#### MCP Resources Directory

[MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) i den offisielle Microsoft MCP-repositorien tilbyr en kuratert samling av eksempler på ressurser, promptmaler og verktøydefinisjoner for bruk med Model Context Protocol-servere. Denne katalogen er laget for å hjelpe utviklere raskt i gang med MCP ved å tilby gjenbrukbare byggeklosser og beste praksis-eksempler for:

- **Promptmaler:** Ferdige promptmaler for vanlige AI-oppgaver og scenarier, som kan tilpasses dine egne MCP-serverimplementeringer.  
- **Verktøydefinisjoner:** Eksempel på verktøyskjemaer og metadata for å standardisere verktøyintegrasjon og kall på tvers av MCP-servere.  
- **Ressurseksempler:** Eksempler på ressursdefinisjoner for tilkobling til datakilder, API-er og eksterne tjenester innen MCP-rammeverket.  
- **Referanseimplementeringer:** Praktiske eksempler som viser hvordan man strukturerer og organiserer ressurser, prompt og verktøy i reelle MCP-prosjekter.  

Disse ressursene akselererer utvikling, fremmer standardisering og bidrar til å sikre beste praksis ved bygging og utrulling av MCP-baserte løsninger.

#### MCP Resources Directory  
- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)  

### Forskningsmuligheter

- Effektive teknikker for promptoptimalisering innen MCP-rammeverk  
- Sikkerhetsmodeller for multi-tenant MCP-distribusjoner  
- Ytelsesmålinger på tvers av ulike MCP-implementeringer  
- Formelle verifikasjonsmetoder for MCP-servere  

## Konklusjon

Model Context Protocol (MCP) former raskt fremtiden for standardisert, sikker og interoperabel AI-integrasjon på tvers av br
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Øvelser

1. Analyser en av casestudiene og foreslå en alternativ implementeringsmetode.
2. Velg et av prosjektideene og lag en detaljert teknisk spesifikasjon.
3. Undersøk en bransje som ikke er dekket i casestudiene, og skisser hvordan MCP kan løse dens spesifikke utfordringer.
4. Utforsk en av fremtidige retninger og lag et konsept for en ny MCP-utvidelse som støtter dette.

Neste: [Best Practices](../08-BestPractices/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.