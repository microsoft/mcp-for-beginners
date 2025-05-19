<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:57:59+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "sl"
}
-->
# Lekcije od zgodnjih uporabnikov

## Pregled

Ta lekcija raziskuje, kako so zgodnji uporabniki izkoristili Model Context Protocol (MCP) za reševanje resničnih izzivov in spodbujanje inovacij v različnih panogah. S podrobnimi študijami primerov in praktičnimi projekti boste videli, kako MCP omogoča standardizirano, varno in razširljivo integracijo AI — povezovanje velikih jezikovnih modelov, orodij in podatkov podjetja v enoten okvir. Pridobili boste praktične izkušnje z načrtovanjem in gradnjo rešitev na osnovi MCP, se naučili preverjenih vzorcev implementacije in odkrili najboljše prakse za uvajanje MCP v produkcijskih okoljih. Lekcija prav tako izpostavlja nastajajoče trende, prihodnje smernice in odprtokodne vire, ki vam pomagajo ostati na čelu tehnologije MCP in njenega razvijajočega se ekosistema.

## Cilji učenja

- Analizirati resnične implementacije MCP v različnih panogah  
- Načrtovati in zgraditi celovite aplikacije na osnovi MCP  
- Raziskati nastajajoče trende in prihodnje smernice v tehnologiji MCP  
- Uporabiti najboljše prakse v dejanskih razvojnih scenarijih  

## Resnične implementacije MCP

### Študija primera 1: Avtomatizacija podpore strankam v podjetjih

Mednarodno podjetje je uvedlo rešitev na osnovi MCP za standardizacijo AI interakcij v svojih sistemih za podporo strankam. To jim je omogočilo:

- Ustvariti enoten vmesnik za več ponudnikov LLM  
- Ohranjati dosledno upravljanje pozivov med oddelki  
- Uvesti robustne varnostne in skladnostne kontrole  
- Enostavno preklapljati med različnimi AI modeli glede na specifične potrebe  

**Tehnična implementacija:**  
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

**Rezultati:** 30 % znižanje stroškov modelov, 45 % izboljšanje doslednosti odgovorov in izboljšana skladnost v globalnih operacijah.

### Študija primera 2: Zdravstveni diagnostični pomočnik

Zdravstveni ponudnik je razvil MCP infrastrukturo za integracijo več specializiranih medicinskih AI modelov ob hkratnem zagotavljanju varnosti občutljivih pacientovih podatkov:

- Brezhibno preklapljanje med splošnimi in specialističnimi medicinskimi modeli  
- Strogi nadzor zasebnosti in revizijske sledi  
- Integracija z obstoječimi sistemi elektronskih zdravstvenih kartonov (EHR)  
- Dosledno oblikovanje pozivov za medicinsko terminologijo  

**Tehnična implementacija:**  
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

**Rezultati:** Izboljšani diagnostični predlogi za zdravnike ob popolni skladnosti z HIPAA in znatno zmanjšanje preklapljanja med sistemi.

### Študija primera 3: Analiza tveganj v finančnih storitvah

Finančna institucija je uvedla MCP za standardizacijo svojih procesov analize tveganj v različnih oddelkih:

- Ustvarila enoten vmesnik za modele kreditnega tveganja, zaznavanja prevar in investicijskega tveganja  
- Uvedla stroge kontrole dostopa in verzioniranje modelov  
- Zagotovila revizijsko sled za vse AI priporočila  
- Ohranjala dosledno obliko podatkov med različnimi sistemi  

**Tehnična implementacija:**  
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

**Rezultati:** Izboljšana skladnost z regulativami, 40 % hitrejši cikli uvajanja modelov in izboljšana doslednost ocenjevanja tveganj med oddelki.

### Študija primera 4: Microsoft Playwright MCP strežnik za avtomatizacijo brskalnika

Microsoft je razvil [Playwright MCP strežnik](https://github.com/microsoft/playwright-mcp) za varno, standardizirano avtomatizacijo brskalnikov prek Model Context Protocola. Ta rešitev omogoča AI agentom in LLM-om interakcijo z brskalniki na nadzorovan, revizijski in razširljiv način — kar omogoča primere uporabe, kot so avtomatizirano testiranje spletnih strani, izvleček podatkov in celoviti delovni tokovi.

- Izpostavlja zmogljivosti avtomatizacije brskalnika (navigacija, izpolnjevanje obrazcev, zajem zaslonskih slik itd.) kot MCP orodja  
- Uvaja stroge kontrole dostopa in peskovnik za preprečevanje nepooblaščenih dejanj  
- Ponuja podrobne revizijske dnevnike vseh interakcij z brskalnikom  
- Podpira integracijo z Azure OpenAI in drugimi ponudniki LLM za avtomatizacijo, ki jo vodijo agenti  

**Tehnična implementacija:**  
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
- Omogočena varna, programska avtomatizacija brskalnikov za AI agente in LLM  
- Zmanjšan ročni napor pri testiranju in izboljšano pokritje testov spletnih aplikacij  
- Ponuja ponovno uporabljiv, razširljiv okvir za integracijo orodij, temelječih na brskalniku, v podjetniških okoljih  

**Reference:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)  

### Študija primera 5: Azure MCP – Podjetniška storitev Model Context Protocol

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) je Microsoftova upravljana, podjetniška implementacija Model Context Protocola, zasnovana za zagotavljanje razširljivih, varnih in skladnih MCP strežniških zmogljivosti kot oblačne storitve. Azure MCP omogoča organizacijam hitro uvajanje, upravljanje in integracijo MCP strežnikov z Azure AI, podatkovnimi in varnostnimi storitvami, kar zmanjšuje operativno breme in pospešuje sprejemanje AI.

- Popolnoma upravljano gostovanje MCP strežnikov z vgrajenim skaliranjem, nadzorom in varnostjo  
- Naravna integracija z Azure OpenAI, Azure AI Search in drugimi Azure storitvami  
- Podjetniška avtentikacija in avtorizacija prek Microsoft Entra ID  
- Podpora za prilagojena orodja, predloge pozivov in priključke virov  
- Skladnost s podjetniškimi varnostnimi in regulativnimi zahtevami  

**Tehnična implementacija:**  
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
- Skrajšan čas do vrednosti za podjetniške AI projekte z zagotavljanjem takoj uporabne, skladne MCP strežniške platforme  
- Poenostavljena integracija LLM, orodij in virov podatkov podjetja  
- Izboljšana varnost, opazovanje in operativna učinkovitost za delovne obremenitve MCP  

**Reference:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)  

## Študija primera 6: NLWeb

MCP (Model Context Protocol) je nastajajoči protokol za klepetalne bote in AI asistente za interakcijo z orodji. Vsak primer NLWeb je tudi MCP strežnik, ki podpira eno osnovno metodo, ask, s katero lahko spletno stran vprašate v naravnem jeziku. Vrnjeni odgovor uporablja schema.org, široko uporabljeno slovarico za opis spletnih podatkov. Po domače rečeno, MCP je NLWeb, kot je Http za HTML. NLWeb združuje protokole, formate Schema.org in vzorčno kodo, da pomaga spletnim mestom hitro ustvariti te končne točke, kar koristi tako ljudem prek pogovornih vmesnikov kot strojem prek naravne agent-agent interakcije.

NLWeb ima dve ločeni komponenti.  
- Protokol, zelo preprost za začetek, za vmesnik s spletnim mestom v naravnem jeziku in format, ki uporablja json in schema.org za vrnjeni odgovor. Več podrobnosti najdete v dokumentaciji o REST API.  
- Enostavna implementacija (1), ki izkorišča obstoječo označbo za spletna mesta, ki jih lahko povzamemo kot sezname elementov (izdelki, recepti, atrakcije, ocene itd.). Skupaj z naborom uporabniških vmesnikov lahko spletna mesta enostavno ponudijo pogovorne vmesnike za svojo vsebino. Več o delovanju najdete v dokumentaciji o življenjskem ciklu poizvedbe klepeta.  

**Reference:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)  

## Praktični projekti

### Projekt 1: Zgradite MCP strežnik z več ponudniki

**Cilj:** Ustvariti MCP strežnik, ki lahko usmerja zahteve do več ponudnikov AI modelov glede na določena merila.

**Zahteve:**  
- Podpora za vsaj tri različne ponudnike modelov (npr. OpenAI, Anthropic, lokalni modeli)  
- Implementacija mehanizma usmerjanja na podlagi metapodatkov zahtev  
- Ustvarjanje konfiguracijskega sistema za upravljanje poverilnic ponudnikov  
- Dodajanje predpomnjenja za optimizacijo zmogljivosti in stroškov  
- Izgradnja preprostega nadzornega panela za spremljanje uporabe  

**Koraki implementacije:**  
1. Postavite osnovno infrastrukturo MCP strežnika  
2. Implementirajte adapterje ponudnikov za vsako AI storitev modela  
3. Ustvarite logiko usmerjanja na podlagi atributov zahtev  
4. Dodajte mehanizme predpomnjenja za pogoste zahteve  
5. Razvijte nadzorni panel za spremljanje  
6. Testirajte z različnimi vzorci zahtev  

**Tehnologije:** Izberite med Python (.NET/Java/Python glede na vašo izbiro), Redis za predpomnjenje in preprost spletni okvir za nadzorni panel.

### Projekt 2: Podjetniški sistem upravljanja pozivov

**Cilj:** Razviti sistem na osnovi MCP za upravljanje, verzioniranje in uvajanje predlog pozivov v organizaciji.

**Zahteve:**  
- Ustvariti centraliziran repozitorij za predloge pozivov  
- Implementirati verzioniranje in odobritvene delovne tokove  
- Izgraditi zmožnosti testiranja predlog z vzorčnimi vnosi  
- Razviti nadzor dostopa na podlagi vlog  
- Ustvariti API za pridobivanje in uvajanje predlog  

**Koraki implementacije:**  
1. Načrtujte shemo baze podatkov za shranjevanje predlog  
2. Ustvarite osnovni API za operacije CRUD s predlogami  
3. Implementirajte sistem verzioniranja  
4. Zgradite odobritveni delovni tok  
5. Razvijte testni okvir  
6. Ustvarite preprost spletni vmesnik za upravljanje  
7. Integrirajte z MCP strežnikom  

**Tehnologije:** Vaša izbira ogrodja za backend, SQL ali NoSQL baza podatkov in frontend ogrodje za upravljalski vmesnik.

### Projekt 3: Platforma za generiranje vsebin na osnovi MCP

**Cilj:** Zgraditi platformo za generiranje vsebin, ki izkorišča MCP za zagotavljanje doslednih rezultatov za različne vrste vsebin.

**Zahteve:**  
- Podpora za več formatov vsebin (blog zapisi, družbeni mediji, marketinški teksti)  
- Implementacija generiranja na osnovi predlog z možnostmi prilagoditev  
- Ustvarjanje sistema pregleda in povratnih informacij za vsebine  
- Spremljanje metrik uspešnosti vsebin  
- Podpora verzioniranju in iteraciji vsebin  

**Koraki implementacije:**  
1. Postavite infrastrukturo MCP odjemalca  
2. Ustvarite predloge za različne vrste vsebin  
3. Zgradite cevovod za generiranje vsebin  
4. Implementirajte sistem pregleda  
5. Razvijte sistem za spremljanje metrik  
6. Ustvarite uporabniški vmesnik za upravljanje predlog in generiranje vsebin  

**Tehnologije:** Vaš priljubljeni programski jezik, spletni okvir in sistem baze podatkov.

## Prihodnje smernice za tehnologijo MCP

### Nastajajoči trendi

1. **Večmodalni MCP**  
   - Razširitev MCP za standardizacijo interakcij z modeli za slike, zvok in video  
   - Razvoj zmožnosti medmodalnega sklepanja  
   - Standardizirani formati pozivov za različne modalitete  

2. **Federirana MCP infrastruktura**  
   - Razpršene MCP mreže, ki lahko delijo vire med organizacijami  
   - Standardizirani protokoli za varno deljenje modelov  
   - Tehnike zasebnostno varne obdelave  

3. **Tržnice MCP**  
   - Ekosistemi za deljenje in monetizacijo predlog in vtičnikov MCP  
   - Procesi zagotavljanja kakovosti in certificiranja  
   - Integracija s tržnicami modelov  

4. **MCP za edge računalništvo**  
   - Prilagoditev MCP standardov za naprave z omejenimi viri na robu omrežja  
   - Optimizirani protokoli za okolja z nizko pasovno širino  
   - Specializirane implementacije MCP za IoT ekosisteme  

5. **Regulativni okviri**  
   - Razvoj razširitev MCP za skladnost z regulativami  
   - Standardizirane revizijske sledi in vmesniki za razložljivost  
   - Integracija z nastajajočimi okviri upravljanja AI  

### MCP rešitve iz Microsofta

Microsoft in Azure sta razvila več odprtokodnih repozitorijev, ki razvijalcem pomagajo implementirati MCP v različnih scenarijih:

#### Microsoft Organization  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) – Playwright MCP strežnik za avtomatizacijo in testiranje brskalnikov  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) – OneDrive MCP strežnik za lokalno testiranje in prispevke skupnosti  
3. [NLWeb](https://github.com/microsoft/NlWeb) – NLWeb je zbirka odprtih protokolov in pripadajočih odprtokodnih orodij. Glavni fokus je vzpostavitev temeljnega sloja za AI splet  

#### Azure-Samples Organization  
1. [mcp](https://github.com/Azure-Samples/mcp) – Povezave do vzorcev, orodij in virov za gradnjo in integracijo MCP strežnikov na Azure z več jeziki  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) – Referenčni MCP strežniki, ki prikazujejo avtentikacijo z aktualno specifikacijo Model Context Protocol  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) – Vstopna stran za implementacije Remote MCP strežnikov v Azure Functions z jezikovno specifičnimi repozitoriji  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) – Predloga za hitro začetek gradnje in uvajanja prilagojenih oddaljenih MCP strežnikov z Azure Functions v Pythonu  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – Predloga za hitro začetek gradnje in uvajanja prilagojenih oddaljenih MCP strežnikov z Azure Functions v .NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – Predloga za hitro začetek gradnje in uvajanja prilagojenih oddaljenih MCP strežnikov z Azure Functions v TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) – Azure API Management kot AI prehod do oddaljenih MCP strežnikov z uporabo Pythona  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) – APIM ❤️ AI eksperimenti z MCP zmogljivostmi, integracija z Azure OpenAI in AI Foundry  

Ti repozitoriji ponujajo različne implementacije, predloge in vire za delo z Model Context Protocolom v različnih programskih jezikih in Azure storitvah. Pokrivajo širok nabor primerov uporabe od osnovnih strežniških implementacij do avtentikacije, oblačnega uvajanja in integracije v podjetjih.

#### MCP Resources Directory

[Mapa MCP Resources](https://github.com/microsoft/mcp/tree/main/Resources) v uradnem Microsoft MCP repozitoriju vsebuje skrbno izbrano zbirko vzorčnih virov, predlog pozivov in definicij orodij za uporabo z MCP strežniki. Ta mapa je namenjena, da razvijalcem pomaga hitro začeti z MCP, saj ponuja ponovno uporabne gradnike in primere najboljših praks za:

- **Predloge pozivov:** Pripravljen
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Vježbe

1. Analizirajte jedan od studija slučaja i predložite alternativni pristup implementaciji.
2. Odaberite jednu od ideja za projekte i izradite detaljnu tehničku specifikaciju.
3. Istražite industriju koja nije obrađena u studijama slučaja i izložite kako bi MCP mogao riješiti njene specifične izazove.
4. Istražite jedan od budućih smjerova i osmislite koncept novog MCP proširenja koje bi ga podržavalo.

Sljedeće: [Najbolje prakse](../08-BestPractices/README.md)

**Opozorilo**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.