<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:39:53+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "tl"
}
-->
# Mga Aral mula sa Maagang Gumamit

## Pangkalahatang-ideya

Tinutuklas ng araling ito kung paano ginamit ng mga maagang gumamit ang Model Context Protocol (MCP) upang lutasin ang mga totoong problema at pasiglahin ang inobasyon sa iba't ibang industriya. Sa pamamagitan ng detalyadong mga case study at praktikal na proyekto, makikita mo kung paano pinapagana ng MCP ang standardized, secure, at scalable na integrasyon ng AI—na nag-uugnay ng malalaking language model, mga tool, at data ng negosyo sa isang pinag-isang framework. Makakakuha ka ng praktikal na karanasan sa pagdidisenyo at paggawa ng mga solusyong nakabase sa MCP, matututo mula sa mga napatunayang pattern ng implementasyon, at matutuklasan ang mga pinakamahuhusay na gawain para sa pag-deploy ng MCP sa mga production environment. Binibigyang-diin din ng aralin ang mga umuusbong na trend, mga direksyon sa hinaharap, at mga open-source na mapagkukunan upang matulungan kang manatiling nangunguna sa teknolohiya ng MCP at sa patuloy nitong pag-unlad.

## Mga Layunin sa Pagkatuto

- Suriin ang mga totoong implementasyon ng MCP sa iba't ibang industriya  
- Magdisenyo at bumuo ng kumpletong aplikasyon na nakabase sa MCP  
- Tuklasin ang mga umuusbong na trend at mga direksyon sa hinaharap ng teknolohiyang MCP  
- Ipatupad ang mga pinakamahusay na gawain sa aktwal na mga sitwasyon ng pag-unlad  

## Mga Totoong Implementasyon ng MCP

### Case Study 1: Automation ng Enterprise Customer Support

Isang multinasyunal na korporasyon ang nagpatupad ng solusyong nakabase sa MCP upang i-standardize ang mga AI interaction sa kanilang mga sistema ng customer support. Pinayagan nito silang:

- Gumawa ng pinag-isang interface para sa iba't ibang LLM provider  
- Panatilihin ang pare-parehong pamamahala ng prompt sa mga departamento  
- Magpatupad ng matibay na seguridad at mga kontrol sa pagsunod  
- Madaling lumipat sa pagitan ng iba't ibang AI model base sa pangangailangan  

**Technical Implementation:**  
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

**Mga Resulta:** 30% na pagbawas sa gastos sa modelo, 45% na pagbuti sa consistency ng tugon, at pinahusay na pagsunod sa buong operasyon sa buong mundo.

### Case Study 2: Healthcare Diagnostic Assistant

Isang healthcare provider ang bumuo ng MCP infrastructure upang pagsamahin ang iba't ibang espesyalistang medikal na AI model habang tinitiyak na protektado ang sensitibong data ng pasyente:

- Madaling paglipat sa pagitan ng generalist at specialist na medikal na mga modelo  
- Mahigpit na mga kontrol sa privacy at audit trails  
- Integrasyon sa umiiral na Electronic Health Record (EHR) system  
- Konsistenteng prompt engineering para sa terminolohiyang medikal  

**Technical Implementation:**  
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

**Mga Resulta:** Pinahusay na mga suhestiyon sa diagnosis para sa mga doktor habang pinananatili ang buong HIPAA compliance at malaking pagbawas sa context-switching sa pagitan ng mga sistema.

### Case Study 3: Pagsusuri ng Panganib sa Serbisyong Pinansyal

Isang institusyong pinansyal ang nagpatupad ng MCP upang i-standardize ang kanilang mga proseso sa pagsusuri ng panganib sa iba't ibang departamento:

- Nilikha ang pinag-isang interface para sa credit risk, fraud detection, at investment risk models  
- Nagpatupad ng mahigpit na access controls at versioning ng mga modelo  
- Tiniyak ang auditability ng lahat ng rekomendasyon ng AI  
- Pinanatili ang konsistenteng pag-format ng data sa iba't ibang sistema  

**Technical Implementation:**  
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

**Mga Resulta:** Pinahusay na pagsunod sa regulasyon, 40% na mas mabilis na cycle ng deployment ng modelo, at pinabuting consistency sa pagsusuri ng panganib sa mga departamento.

### Case Study 4: Microsoft Playwright MCP Server para sa Browser Automation

Binuo ng Microsoft ang [Playwright MCP server](https://github.com/microsoft/playwright-mcp) upang paganahin ang secure at standardized na browser automation gamit ang Model Context Protocol. Pinapayagan ng solusyong ito ang AI agents at LLMs na makipag-ugnayan sa mga web browser sa kontrolado, auditable, at extensible na paraan—na nagbibigay-daan sa mga use case tulad ng automated web testing, data extraction, at end-to-end workflows.

- Ipinapakita ang mga kakayahan ng browser automation (navigation, form filling, screenshot capture, atbp.) bilang MCP tools  
- Nagpapatupad ng mahigpit na access controls at sandboxing para maiwasan ang hindi awtorisadong aksyon  
- Nagbibigay ng detalyadong audit logs para sa lahat ng browser interaction  
- Sinusuportahan ang integrasyon sa Azure OpenAI at iba pang LLM provider para sa agent-driven automation  

**Technical Implementation:**  
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

**Mga Resulta:**  
- Nagbigay-daan sa secure, programmatic browser automation para sa AI agents at LLMs  
- Nabawasan ang manual testing effort at pinahusay ang test coverage para sa mga web application  
- Nagbigay ng reusable at extensible na framework para sa integrasyon ng mga browser-based tool sa enterprise environment  

**Mga Sanggunian:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### Case Study 5: Azure MCP – Enterprise-Grade Model Context Protocol bilang Serbisyo

Ang Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) ay managed, enterprise-grade na implementasyon ng Model Context Protocol ng Microsoft, na dinisenyo upang magbigay ng scalable, secure, at compliant na MCP server capabilities bilang cloud service. Pinapahintulutan ng Azure MCP ang mga organisasyon na mabilis na mag-deploy, mag-manage, at mag-integrate ng MCP server sa Azure AI, data, at security services, na nagpapababa ng operational overhead at nagpapabilis ng AI adoption.

- Fully managed MCP server hosting na may built-in scaling, monitoring, at security  
- Native integration sa Azure OpenAI, Azure AI Search, at iba pang Azure services  
- Enterprise authentication at authorization gamit ang Microsoft Entra ID  
- Suporta para sa custom tools, prompt templates, at resource connectors  
- Pagsunod sa mga enterprise security at regulatory requirements  

**Technical Implementation:**  
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

**Mga Resulta:**  
- Pinababa ang time-to-value para sa mga enterprise AI project sa pamamagitan ng pagbibigay ng ready-to-use, compliant MCP server platform  
- Pinadali ang integrasyon ng LLMs, tools, at mga enterprise data source  
- Pinahusay ang seguridad, observability, at operational efficiency para sa MCP workloads  

**Mga Sanggunian:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## Case Study 6: NLWeb

Ang MCP (Model Context Protocol) ay isang umuusbong na protocol para sa mga chatbot at AI assistant upang makipag-ugnayan sa mga tool. Bawat NLWeb instance ay isang MCP server rin, na sumusuporta sa isang pangunahing method, ang ask, na ginagamit upang magtanong sa isang website gamit ang natural na wika. Ang ibinalik na sagot ay gumagamit ng schema.org, isang malawakang ginagamit na bokabularyo para ilarawan ang web data. Sa madaling salita, ang MCP ay parang NLWeb sa HTTP tulad ng HTML. Pinagsasama ng NLWeb ang mga protocol, schema.org na format, at sample code upang tulungan ang mga site na mabilis na makalikha ng mga endpoint na ito, na nakikinabang sa mga tao sa pamamagitan ng conversational interfaces at sa mga makina sa pamamagitan ng natural na agent-to-agent na interaksyon.

May dalawang pangunahing bahagi ang NLWeb.  
- Isang protocol, na napakasimple bilang panimula, upang makipag-interface sa isang site gamit ang natural na wika at isang format na gumagamit ng json at schema.org para sa sagot. Tingnan ang dokumentasyon ng REST API para sa karagdagang detalye.  
- Isang direktang implementasyon ng (1) na gumagamit ng umiiral na markup, para sa mga site na maaaring i-abstract bilang listahan ng mga item (produkto, recipe, atraksyon, review, atbp.). Kasama ang hanay ng mga user interface widget, madaling makapagbigay ang mga site ng conversational interfaces para sa kanilang nilalaman. Tingnan ang dokumentasyon sa Life of a chat query para sa karagdagang paliwanag kung paano ito gumagana.

**Mga Sanggunian:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## Mga Hands-on na Proyekto

### Proyekto 1: Gumawa ng Multi-Provider MCP Server

**Layunin:** Gumawa ng MCP server na maaaring mag-route ng mga request sa iba't ibang AI model provider base sa tiyak na mga pamantayan.

**Mga Kinakailangan:**  
- Suportahan ang hindi bababa sa tatlong magkakaibang model provider (hal., OpenAI, Anthropic, lokal na modelo)  
- Magpatupad ng mekanismo sa pag-route base sa metadata ng request  
- Gumawa ng configuration system para sa pamamahala ng provider credentials  
- Magdagdag ng caching para i-optimize ang performance at gastos  
- Gumawa ng simpleng dashboard para sa monitoring ng paggamit  

**Mga Hakbang sa Implementasyon:**  
1. I-set up ang basic MCP server infrastructure  
2. Ipatupad ang mga provider adapter para sa bawat AI model service  
3. Gumawa ng routing logic base sa mga attribute ng request  
4. Magdagdag ng caching mechanism para sa madalas na mga request  
5. Bumuo ng monitoring dashboard  
6. Subukan gamit ang iba't ibang pattern ng request  

**Mga Teknolohiya:** Pumili mula sa Python (.NET/Java/Python base sa gusto mo), Redis para sa caching, at simpleng web framework para sa dashboard.

### Proyekto 2: Enterprise Prompt Management System

**Layunin:** Bumuo ng MCP-based na sistema para sa pamamahala, versioning, at deployment ng prompt templates sa buong organisasyon.

**Mga Kinakailangan:**  
- Gumawa ng centralized repository para sa prompt templates  
- Magpatupad ng versioning at approval workflows  
- Bumuo ng kakayahan sa pagsubok ng template gamit ang sample inputs  
- Mag-develop ng role-based access controls  
- Gumawa ng API para sa retrieval at deployment ng template  

**Mga Hakbang sa Implementasyon:**  
1. Disenyuhin ang database schema para sa storage ng template  
2. Gumawa ng core API para sa CRUD operations ng template  
3. Ipatupad ang versioning system  
4. Bumuo ng approval workflow  
5. Mag-develop ng testing framework  
6. Gumawa ng simpleng web interface para sa pamamahala  
7. I-integrate sa MCP server  

**Mga Teknolohiya:** Piliin ang backend framework, SQL o NoSQL database, at frontend framework para sa management interface.

### Proyekto 3: MCP-Based Content Generation Platform

**Layunin:** Bumuo ng content generation platform na gumagamit ng MCP upang magbigay ng konsistenteng resulta sa iba't ibang uri ng nilalaman.

**Mga Kinakailangan:**  
- Suportahan ang iba't ibang content format (blog post, social media, marketing copy)  
- Magpatupad ng template-based generation na may customization options  
- Gumawa ng content review at feedback system  
- Subaybayan ang performance metrics ng content  
- Suportahan ang content versioning at iteration  

**Mga Hakbang sa Implementasyon:**  
1. I-set up ang MCP client infrastructure  
2. Gumawa ng mga template para sa iba't ibang content type  
3. Bumuo ng content generation pipeline  
4. Ipatupad ang review system  
5. Mag-develop ng metrics tracking system  
6. Gumawa ng user interface para sa template management at content generation  

**Mga Teknolohiya:** Piliin ang programming language, web framework, at database system na gusto mo.

## Mga Direksyon sa Hinaharap para sa Teknolohiya ng MCP

### Mga Umuusbong na Trend

1. **Multi-Modal MCP**  
   - Pagpapalawak ng MCP para i-standardize ang interaksyon sa mga image, audio, at video model  
   - Pag-develop ng cross-modal reasoning capabilities  
   - Standardized na prompt format para sa iba't ibang modality  

2. **Federated MCP Infrastructure**  
   - Distributed na MCP network na maaaring magbahagi ng resources sa iba't ibang organisasyon  
   - Standardized na protocol para sa secure na pagbabahagi ng modelo  
   - Mga teknik para sa privacy-preserving computation  

3. **MCP Marketplaces**  
   - Ecosystem para sa pagbabahagi at pagkita mula sa MCP template at plugin  
   - Quality assurance at certification process  
   - Integrasyon sa mga model marketplace  

4. **MCP para sa Edge Computing**  
   - Adaptasyon ng MCP standard para sa mga resource-constrained na edge device  
   - Optimized na protocol para sa low-bandwidth na kapaligiran  
   - Espesyal na implementasyon ng MCP para sa IoT ecosystem  

5. **Regulatory Frameworks**  
   - Pag-develop ng MCP extension para sa regulatory compliance  
   - Standardized audit trail at explainability interface  
   - Integrasyon sa mga umuusbong na AI governance framework  

### Mga Solusyon ng MCP mula sa Microsoft

Nag-develop ang Microsoft at Azure ng ilang open-source repository upang tulungan ang mga developer na mag-implement ng MCP sa iba't ibang scenario:

#### Microsoft Organization  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - Playwright MCP server para sa browser automation at testing  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - OneDrive MCP server implementation para sa lokal na testing at community contribution  
3. [NLWeb](https://github.com/microsoft/NlWeb) - Koleksyon ng open protocol at kaugnay na open source tools na nakatuon sa pagtatatag ng foundational layer para sa AI Web  

#### Azure-Samples Organization  
1. [mcp](https://github.com/Azure-Samples/mcp) - Mga sample, tool, at resources para sa paggawa at integrasyon ng MCP server sa Azure gamit ang iba't ibang wika  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - Reference MCP server na nagpapakita ng authentication gamit ang kasalukuyang Model Context Protocol spec  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Landing page para sa Remote MCP Server implementation gamit ang Azure Functions na may mga link sa language-specific repo  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Quickstart template para sa paggawa at deployment ng custom remote MCP server gamit ang Azure Functions at Python  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Quickstart template para sa paggawa at deployment ng custom remote MCP server gamit ang Azure Functions at .NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Quickstart template para sa paggawa at deployment ng custom remote MCP server gamit ang Azure Functions at TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Azure API Management bilang AI Gateway para sa Remote MCP server gamit ang Python  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI experiments kabilang ang MCP capabilities, integrasyon sa Azure OpenAI at AI Foundry  

Nagbibigay ang mga repository na ito ng iba't ibang implementasyon, template, at resource para sa Model Context Protocol sa iba't ibang programming language at Azure services. Saklaw nito ang mga use case mula sa basic server implementation hanggang sa authentication, cloud deployment, at enterprise integration scenario.

#### MCP Resources Directory

Ang [MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) sa opisyal na Microsoft MCP repository ay naglalaman ng maingat na piniling koleksyon ng sample resources, prompt templates, at tool definitions para magamit sa Model Context Protocol server. Dinisenyo ang direktoryong ito upang tulungan ang mga developer na mabilis na makapagsimula sa MCP sa pamamagitan ng mga reusable building block at mga halimbawa ng best practice para sa:

- **Prompt Templates:** Ready-to-use na prompt template para sa karaniwang AI task at scenario, na maaaring i-adapt para sa sarili mong MCP server implementation.  
- **Tool Definitions:** Halimbawa ng tool schema at metadata upang i-standardize ang tool integration at invocation sa iba't ibang MCP server.  
- **Resource Samples:** Halimbawa ng resource definition para sa pagkonekta sa mga data source, API, at external service sa loob ng MCP framework.  
- **Reference Implementations:** Praktikal na sample na nagpapakita kung paano istrukturahin at i-organisa ang mga resource, prompt, at tool sa totoong MCP project.  

Pinapabilis ng mga resource na ito ang pag-unlad, nagpo-promote ng standardization, at tumutulong upang matiyak ang best practice sa paggawa at pag-deploy ng MCP-based na solusyon.

#### MCP Resources Directory  
- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)

### Mga Oportunidad sa Pananaliksik

- Epektibong teknik sa prompt optimization sa loob ng MCP framework  
- Mga security model para sa multi-tenant MCP deployment  
- Benchmarking ng performance sa iba't ibang MCP implementation  
- Formal verification methods para sa MCP server  

## Konklusyon

Ang Model Context Protocol (MCP) ay mabilis na humuhubog sa hinaharap ng standardized, secure, at interoperable na integrasyon ng AI sa iba't ibang industriya. Sa pamamagitan ng mga case study at hands-on na proyekto sa araling ito, nakita mo kung paano ginagamit ng mga maagang gumamit—kabilang ang Microsoft at Azure—ang MCP upang lutasin ang totoong problema, pabilisin ang AI adoption, at matiyak ang pagsunod, seguridad, at scalability. Ang modular na approach ng MCP ay nagpapahintulot sa mga organisasyon na iugnay ang malalaking language model, mga tool, at data ng negosyo sa isang pinag-isang, auditable na framework. Habang patuloy na umuunlad ang MCP, ang pananat
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Mga Ehersisyo

1. Suriin ang isa sa mga case study at magmungkahi ng alternatibong paraan ng pagpapatupad.
2. Pumili ng isa sa mga ideya ng proyekto at gumawa ng detalyadong teknikal na espesipikasyon.
3. Mag-research ng industriya na hindi sakop sa mga case study at ilahad kung paano matutugunan ng MCP ang mga partikular na hamon nito.
4. Tuklasin ang isa sa mga hinaharap na direksyon at bumuo ng konsepto para sa bagong MCP extension upang suportahan ito.

Susunod: [Best Practices](../08-BestPractices/README.md)

**Pagtatangi**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.