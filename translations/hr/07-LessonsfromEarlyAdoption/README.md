<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:55:52+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "hr"
}
-->
# Lekcije od rani korisnici

## Pregled

Ova lekcija istražuje kako su rani korisnici iskoristili Model Context Protocol (MCP) za rješavanje stvarnih izazova i poticanje inovacija u različitim industrijama. Kroz detaljne studije slučaja i praktične projekte, vidjet ćete kako MCP omogućava standardiziranu, sigurnu i skalabilnu AI integraciju — povezujući velike jezične modele, alate i podatke poduzeća u jedinstvenom okviru. Steći ćete praktično iskustvo u dizajniranju i izgradnji rješenja temeljenih na MCP-u, naučiti iz provjerenih obrazaca implementacije i otkriti najbolje prakse za primjenu MCP-a u produkcijskim okruženjima. Lekcija također ističe nove trendove, buduće smjerove i open-source resurse koji će vam pomoći da ostanete na čelu MCP tehnologije i njezinog rastućeg ekosustava.

## Ciljevi učenja

- Analizirati stvarne MCP implementacije u različitim industrijama  
- Dizajnirati i izgraditi kompletne aplikacije temeljene na MCP-u  
- Istražiti nove trendove i buduće smjerove MCP tehnologije  
- Primijeniti najbolje prakse u stvarnim razvojnim scenarijima  

## Stvarne MCP implementacije

### Studija slučaja 1: Automatizacija korisničke podrške u poduzećima

Multinacionalna korporacija implementirala je rješenje temeljeno na MCP-u kako bi standardizirala AI interakcije u svojim sustavima korisničke podrške. To im je omogućilo:

- Kreiranje jedinstvenog sučelja za više LLM pružatelja  
- Održavanje dosljednog upravljanja promptovima između odjela  
- Implementaciju snažnih sigurnosnih i usklađenosnih kontrola  
- Jednostavno prebacivanje između različitih AI modela prema specifičnim potrebama  

**Tehnička implementacija:**  
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

**Rezultati:** 30% smanjenje troškova modela, 45% poboljšanje konzistentnosti odgovora i poboljšana usklađenost u globalnim operacijama.

### Studija slučaja 2: Asistent za dijagnostiku u zdravstvu

Zdravstveni pružatelj razvio je MCP infrastrukturu za integraciju više specijaliziranih medicinskih AI modela uz osiguranje zaštite osjetljivih podataka pacijenata:

- Besprijekorno prebacivanje između generalističkih i specijalističkih medicinskih modela  
- Stroge kontrole privatnosti i revizijski tragovi  
- Integracija s postojećim sustavima elektroničkih zdravstvenih kartona (EHR)  
- Dosljedno inženjerstvo promptova za medicinsku terminologiju  

**Tehnička implementacija:**  
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

**Rezultati:** Poboljšani dijagnostički prijedlozi za liječnike uz potpuno poštivanje HIPAA-e i značajno smanjenje prebacivanja konteksta između sustava.

### Studija slučaja 3: Analiza rizika u financijskim uslugama

Financijska institucija implementirala je MCP za standardizaciju procesa analize rizika u različitim odjelima:

- Kreirano jedinstveno sučelje za modele kreditnog rizika, otkrivanja prijevara i investicijskog rizika  
- Implementirane stroge kontrole pristupa i verzioniranje modela  
- Osigurana revizibilnost svih AI preporuka  
- Održavanje dosljednog formatiranja podataka u raznolikim sustavima  

**Tehnička implementacija:**  
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

**Rezultati:** Poboljšana usklađenost s propisima, 40% brži ciklusi implementacije modela i poboljšana konzistentnost procjene rizika između odjela.

### Studija slučaja 4: Microsoft Playwright MCP server za automatizaciju preglednika

Microsoft je razvio [Playwright MCP server](https://github.com/microsoft/playwright-mcp) za omogućavanje sigurne i standardizirane automatizacije preglednika putem Model Context Protocol-a. Ovo rješenje omogućava AI agentima i LLM-ovima interakciju s web preglednicima na kontroliran, revizibilan i proširiv način — omogućujući slučajeve upotrebe poput automatiziranog web testiranja, ekstrakcije podataka i end-to-end radnih tokova.

- Izlaže mogućnosti automatizacije preglednika (navigacija, popunjavanje obrazaca, snimanje zaslona itd.) kao MCP alate  
- Implementira stroge kontrole pristupa i sandboxing za sprječavanje neovlaštenih radnji  
- Pruža detaljne revizijske zapise za sve interakcije s preglednikom  
- Podržava integraciju s Azure OpenAI i drugim LLM pružateljima za automatizaciju vođenu agentima  

**Tehnička implementacija:**  
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

**Rezultati:**  
- Omogućena sigurna, programska automatizacija preglednika za AI agente i LLM-ove  
- Smanjen ručni napor testiranja i poboljšano pokrivanje testova web aplikacija  
- Pružena višekratno upotrebljiva, proširiva platforma za integraciju alata temeljenih na pregledniku u poslovnim okruženjima  

**Reference:**  
- [Playwright MCP Server GitHub repozitorij](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI i rješenja za automatizaciju](https://azure.microsoft.com/en-us/products/ai-services/)

### Studija slučaja 5: Azure MCP – Enterprise-grade Model Context Protocol kao usluga

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) je Microsoftova upravljana, enterprise-grade implementacija Model Context Protocol-a, dizajnirana za pružanje skalabilnih, sigurnih i usklađenih MCP server mogućnosti kao cloud usluge. Azure MCP omogućava organizacijama brzo postavljanje, upravljanje i integraciju MCP servera s Azure AI, podacima i sigurnosnim uslugama, smanjujući operativne troškove i ubrzavajući usvajanje AI-a.

- Potpuno upravljano hosting MCP servera s ugrađenim skaliranjem, nadzorom i sigurnošću  
- Izvorna integracija s Azure OpenAI, Azure AI Search i drugim Azure uslugama  
- Enterprise autentikacija i autorizacija putem Microsoft Entra ID-a  
- Podrška za prilagođene alate, predloške promptova i konektore resursa  
- Usklađenost s sigurnosnim i regulatornim zahtjevima poduzeća  

**Tehnička implementacija:**  
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

**Rezultati:**  
- Smanjeno vrijeme do vrijednosti za enterprise AI projekte pružajući spremnu, usklađenu MCP server platformu  
- Pojednostavljena integracija LLM-ova, alata i izvora podataka poduzeća  
- Poboljšana sigurnost, vidljivost i operativna učinkovitost za MCP radna opterećenja  

**Reference:**  
- [Azure MCP dokumentacija](https://aka.ms/azmcp)  
- [Azure AI usluge](https://azure.microsoft.com/en-us/products/ai-services/)

## Studija slučaja 6: NLWeb

MCP (Model Context Protocol) je novi protokol za chatbote i AI asistente za interakciju s alatima. Svaka NLWeb instanca također je MCP server koji podržava jednu osnovnu metodu, ask, koja se koristi za postavljanje pitanja web stranici na prirodnom jeziku. Vraćeni odgovor koristi schema.org, široko korišteni vokabular za opis web podataka. U slobodnom prijevodu, MCP je za NLWeb kao što je Http za HTML. NLWeb kombinira protokole, formate Schema.org i primjere koda kako bi pomogao stranicama brzo kreirati ove krajnje točke, koristeći ih za korisničke sučelja temeljena na razgovoru i strojnu interakciju između agenata.

NLWeb se sastoji od dva različita dijela:  
- Protokol, vrlo jednostavan za početak, za sučelje sa stranicom na prirodnom jeziku i format koji koristi json i schema.org za vraćeni odgovor. Detalje potražite u dokumentaciji REST API-ja.  
- Jednostavna implementacija (1) koja koristi postojeći markup za stranice koje se mogu apstrahirati kao liste stavki (proizvodi, recepti, atrakcije, recenzije itd.). Zajedno s nizom korisničkih widgeta, stranice lako mogu pružiti razgovorna sučelja za svoj sadržaj. Detalje potražite u dokumentaciji Life of a chat query.  

**Reference:**  
- [Azure MCP dokumentacija](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## Praktični projekti

### Projekt 1: Izgradnja MCP servera s više pružatelja

**Cilj:** Kreirati MCP server koji može usmjeravati zahtjeve prema različitim AI model pružateljima na temelju specifičnih kriterija.

**Zahtjevi:**  
- Podrška za najmanje tri različita pružatelja modela (npr. OpenAI, Anthropic, lokalni modeli)  
- Implementacija mehanizma usmjeravanja temeljenog na metapodacima zahtjeva  
- Kreiranje sustava konfiguracije za upravljanje vjerodajnicama pružatelja  
- Dodavanje cacheiranja za optimizaciju performansi i troškova  
- Izrada jednostavne nadzorne ploče za praćenje korištenja  

**Koraci implementacije:**  
1. Postaviti osnovnu MCP server infrastrukturu  
2. Implementirati adaptere pružatelja za svaku AI model uslugu  
3. Kreirati logiku usmjeravanja na temelju atributa zahtjeva  
4. Dodati cache mehanizme za česte zahtjeve  
5. Razviti nadzornu ploču za praćenje  
6. Testirati s različitim obrascima zahtjeva  

**Tehnologije:** Odaberite između Python (.NET/Java/Python prema vašim preferencijama), Redis za cacheiranje i jednostavan web framework za nadzornu ploču.

### Projekt 2: Enterprise sustav upravljanja promptovima

**Cilj:** Razviti sustav temeljen na MCP-u za upravljanje, verzioniranje i implementaciju predložaka promptova unutar organizacije.

**Zahtjevi:**  
- Kreirati centralizirani repozitorij za predloške promptova  
- Implementirati verzioniranje i tijekove odobrenja  
- Izgraditi mogućnosti testiranja predložaka s primjerima unosa  
- Razviti kontrole pristupa temeljene na ulogama  
- Kreirati API za dohvat i implementaciju predložaka  

**Koraci implementacije:**  
1. Dizajnirati shemu baze podataka za pohranu predložaka  
2. Kreirati osnovni API za CRUD operacije predložaka  
3. Implementirati sustav verzioniranja  
4. Izgraditi tijek odobrenja  
5. Razviti testni okvir  
6. Kreirati jednostavno web sučelje za upravljanje  
7. Integrirati s MCP serverom  

**Tehnologije:** Po vašem izboru backend framework, SQL ili NoSQL baza podataka i frontend framework za upravljanje.

### Projekt 3: Platforma za generiranje sadržaja temeljena na MCP-u

**Cilj:** Izgraditi platformu za generiranje sadržaja koja koristi MCP za dosljedne rezultate u različitim vrstama sadržaja.

**Zahtjevi:**  
- Podrška za više formata sadržaja (blog postovi, društvene mreže, marketinški tekstovi)  
- Implementacija generiranja temeljenog na predlošcima s opcijama prilagodbe  
- Kreiranje sustava za pregled i povratne informacije o sadržaju  
- Praćenje metrike performansi sadržaja  
- Podrška za verzioniranje i iteraciju sadržaja  

**Koraci implementacije:**  
1. Postaviti MCP klijentsku infrastrukturu  
2. Kreirati predloške za različite vrste sadržaja  
3. Izgraditi pipeline za generiranje sadržaja  
4. Implementirati sustav pregleda  
5. Razviti sustav praćenja metrika  
6. Kreirati korisničko sučelje za upravljanje predlošcima i generiranje sadržaja  

**Tehnologije:** Po vašem izboru programski jezik, web framework i sustav baze podataka.

## Budući smjerovi MCP tehnologije

### Novi trendovi

1. **Multi-modalni MCP**  
   - Proširenje MCP-a za standardizaciju interakcija s modelima za slike, zvuk i video  
   - Razvoj sposobnosti za cross-modalno rezoniranje  
   - Standardizirani formati promptova za različite modalitete  

2. **Federirana MCP infrastruktura**  
   - Distribuirane MCP mreže koje mogu dijeliti resurse između organizacija  
   - Standardizirani protokoli za sigurnu razmjenu modela  
   - Tehnike privatnosti u računanju  

3. **MCP tržišta**  
   - Ekosustavi za dijeljenje i monetizaciju MCP predložaka i dodataka  
   - Procesi osiguranja kvalitete i certifikacije  
   - Integracija s tržištima modela  

4. **MCP za Edge računarstvo**  
   - Prilagodba MCP standarda za uređaje s ograničenim resursima na rubu mreže  
   - Optimizirani protokoli za okruženja s niskom propusnošću  
   - Specijalizirane MCP implementacije za IoT ekosustave  

5. **Regulatorni okviri**  
   - Razvoj MCP proširenja za usklađenost s propisima  
   - Standardizirani revizijski tragovi i sučelja za objašnjivost  
   - Integracija s novim okvirima za upravljanje AI-jem  

### MCP rješenja iz Microsofta

Microsoft i Azure razvili su nekoliko open-source repozitorija koji pomažu developerima u implementaciji MCP-a u različitim scenarijima:

#### Microsoft organizacija  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - Playwright MCP server za automatizaciju i testiranje preglednika  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - OneDrive MCP server implementacija za lokalno testiranje i doprinos zajednice  
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWeb je kolekcija otvorenih protokola i pridruženih open source alata. Glavni fokus je uspostava temeljne razine za AI Web  

#### Azure-Samples organizacija  
1. [mcp](https://github.com/Azure-Samples/mcp) - Linkovi na primjere, alate i resurse za izgradnju i integraciju MCP servera na Azureu koristeći različite jezike  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - Referentni MCP serveri koji demonstriraju autentikaciju prema Model Context Protocol specifikaciji  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Početna stranica za implementacije Remote MCP servera u Azure Functions s linkovima na jezične repozitorije  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Predložak za brzo pokretanje i implementaciju prilagođenih Remote MCP servera koristeći Azure Functions i Python  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Predložak za brzo pokretanje i implementaciju prilagođenih Remote MCP servera koristeći Azure Functions i .NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Predložak za brzo pokretanje i implementaciju prilagođenih Remote MCP servera koristeći Azure Functions i TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Azure API Management kao AI Gateway za Remote MCP servere koristeći Python  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI eksperimenti uključujući MCP mogućnosti, integraciju s Azure OpenAI i AI Foundry  

Ovi repozitoriji nude različite implementacije, predloške i resurse za rad s Model Context Protocolom na različitim programskim jezicima i Azure uslugama. Pokrivaju širok spektar primjena od osnovnih server implementacija do autentikacije, cloud deploymenta i enterprise integracije.

#### MCP direktorij resursa

[Direktorij MCP resursa](https://github.com/microsoft/mcp/tree/main/Resources) u službenom Microsoft MCP repozitoriju pruža pažljivo odabranu kolekciju primjera resursa, predložaka promptova i definicija alata za korištenje s Model Context Protocol serverima. Ovaj direktorij je dizajniran da pomogne developerima brzo započeti s MCP-om nudeći višekratno upotrebljive gradivne blokove i najbolje primjere za:

- **Predloške promptova:** Spremni predlošci za uobičajene AI zadatke i scenarije koje možete prilagoditi vlastitim MCP implementacijama.  
- **Definicije alata:** Primjeri shema alata i metapodataka za standardizaciju integracije i poziva alata preko različitih MCP servera.  
- **Primjeri resursa:** Definicije resursa za povezivanje s izvorima podataka, API-jima i vanjskim uslugama unutar MCP okvira.  

- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Vježbe

1. Analizirajte jedan od studija slučaja i predložite alternativni pristup implementaciji.
2. Odaberite jednu od ideja za projekt i izradite detaljnu tehničku specifikaciju.
3. Istražite industriju koja nije obuhvaćena studijama slučaja i izložite kako bi MCP mogao riješiti njezine specifične izazove.
4. Istražite jedan od budućih smjerova i kreirajte koncept za novu MCP ekstenziju koja bi ga podržavala.

Sljedeće: [Best Practices](../08-BestPractices/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.