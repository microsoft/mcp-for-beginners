# 🌟 प्रारम्भिक स्वीकर्ताहरूबाट सिकाइहरू

[![MCP प्रारम्भिक स्वीकर्ताहरूबाट सिकाइहरू](../../../translated_images/ne/08.980bb2babbaadd8a.webp)](https://youtu.be/jds7dSmNptE)

_(यस पाठको भिडियो हेर्न माथिको छवि क्लिक गर्नुहोस्)_

## 🎯 यो मोड्युल के समेट्छ

यो मोड्युलले वास्तविक संगठनहरू र विकासकर्ताहरूले मोडेल सन्दर्भ प्रोटोकल (MCP) कसरी प्रयोग गरी वास्तविक चुनौतीहरू समाधान गर्दै छन् र नवप्रवर्तनलाई अघि बढाइरहेको छ भनी अन्वेषण गर्दछ। विस्तृत केस अध्ययनहरू, व्यावहारिक परियोजनाहरू, र व्यवहारिक उदाहरणहरू मार्फत, तपाईंले पत्ता लगाउनु हुनेछ कि MCP कसरी सुरक्षित, मापनयोग्य AI एकीकरण सक्षम पार्छ जुन भाषा मोडेलहरू, उपकरणहरू, र उद्यम डेटा जोड्दछ।

### 📚 MCP लाई क्रियाशील अवस्थामा हेर्नुहोस्

उत्पादन-तयार उपकरणहरूमा यी सिद्धान्तहरू लागू भएको देख्न चाहनुहुन्छ? हाम्रो [**१० माइक्रोसफ्ट MCP सर्भरहरू जुन विकासकर्ता उत्पादकत्वमा रुपान्तरण गर्दैछन्**](microsoft-mcp-servers.md) अवलोकन गर्नुहोस्, जसमा वास्तविक माइक्रोसफ्ट MCP सर्भरहरू छन् जुन तपाईं आज प्रयोग गर्न सक्नुहुन्छ।

## अवलोकन

यो पाठले प्रारम्भिक स्वीकर्ताहरूले मोडेल सन्दर्भ प्रोटोकल (MCP) लाई कसरी प्रयोग गरेर वास्तविक संसारका चुनौतीहरू समाधान गरेका छन् र उद्योगभर नवप्रवर्तन अगाडि बढाएका छन् भनी अन्वेषण गर्दछ। विस्तृत केस अध्ययन र व्यावहारिक परियोजनाहरू मार्फत, तपाईंले देख्नु हुनेछ कि MCP कसरी मानकीकृत, सुरक्षित, र मापनयोग्य AI एकीकरण सक्षम पार्छ—बृहत् भाषा मोडेलहरू, उपकरणहरू, र उद्यम डेटालाई एकीकृत फ्रेमवर्कमा जोड्दै। तपाईंले MCP-आधारित समाधानहरू डिजाइन र निर्माण गर्ने व्यावहारिक अनुभव प्राप्त गर्नुहुनेछ, प्रमाणित कार्यान्वयन ढाँचाबाट सिक्नुहुनेछ, र उत्पादन वातावरणहरूमा MCP तैनाथ गर्दा उत्कृष्ट अभ्यासहरू पत्ता लगाउनुहुनेछ। पाठले उदाउँदो प्रवृत्तिहरू, भविष्यका दिशाहरू, र खुला स्रोत स्रोतहरू पनि हाइलाइट गर्छ जसले तपाईंलाई MCP प्राविधि र यसको विकास हुँदै गरेको पारिस्थितिकी प्रणालीमा अगाडि रहन मद्दत पुर्‍याउँछ।

## सिकाइ उद्देश्यहरू

- विभिन्न उद्योगहरूमा वास्तविक MCP कार्यान्वयनहरू विश्लेषण गर्नुहोस्
- पूर्ण MCP-आधारित अनुप्रयोगहरू डिजाइन र निर्माण गर्नुहोस्
- MCP प्राविधिमा उदाउँदो प्रवृत्तिहरू र भविष्यका दिशाहरू अन्वेषण गर्नुहोस्
- वास्तविक विकास परिदृश्यहरूमा उत्कृष्ट अभ्यासहरू लागू गर्नुहोस्

## वास्तविक संसारका MCP कार्यान्वयनहरू

### केस अध्ययन १: उद्यम ग्राहक समर्थन स्वचालन

एक बहुराष्ट्रिय कम्पनीले आफ्नो ग्राहक समर्थन प्रणालीहरूमा AI अन्तरक्रियाहरूलाई मानकीकृत गर्न MCP-आधारित समाधान लागू गर्‍यो। यसले तिनीहरूलाई अनुमति दियो:

- बहु LLM प्रदायकहरूको लागि एकीकृत इन्टरफेस सिर्जना गर्न
- विभागहरूमा निरन्तर प्रॉम्प्ट व्यवस्थापन कायम राख्न
- बलियो सुरक्षा र अनुपालन नियन्त्रणहरू लागू गर्न
- विशेष आवश्यकताका आधारमा विभिन्न AI मोडेलहरू बीच सजिलै स्विच गर्न

**प्राविधिक कार्यान्वयन:**

```python
# ग्राहक समर्थनका लागि Python MCP सर्भर कार्यान्वयन
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# लगिङ कन्फिगर गर्नुहोस्
logging.basicConfig(level=logging.INFO)

async def main():
    # सर्भर कन्फिगरेसन सिर्जना गर्नुहोस्
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # MCP सर्भर आरम्भ गर्नुहोस्
    server = create_server(config)
    
    # ज्ञान आधार स्रोतहरू दर्ता गर्नुहोस्
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # प्रॉम्प्ट टेम्प्लेटहरू दर्ता गर्नुहोस्
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # समर्थन उपकरणहरू दर्ता गर्नुहोस्
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # HTTP ट्रान्सपोर्टसहित सर्भर सुरु गर्नुहोस्
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**परिणामहरू:** मोडेल खर्चहरूमा ३०% कटौती, प्रतिक्रिया निरन्तरतामा ४५% सुधार, र विश्वव्यापी सञ्चालनहरूमा बृद्धि गरिएको अनुपालन।

### केस अध्ययन २: स्वास्थ्य सेवा डायग्नोस्टिक सहायक

एक स्वास्थ्य सेवा प्रदायकले बहु विशेषज्ञ चिकित्सा AI मोडेलहरू सँग जोडिएको MCP पूर्वाधार विकास गर्‍यो भने संवेदनशील बिरामी डेटा सुरक्षित रह्यो:

- सामान्य र विशेषज्ञ चिकित्सा मोडेलहरू बीच सहज स्विचिंग
- कडा गोपनीयता नियन्त्रणहरू र अडिट ट्रेलहरू
- विद्यमान इलेक्ट्रोनिक हेल्थ रेकर्ड (EHR) प्रणालीहरूसँग एकीकरण
- चिकित्सा टर्मिनोलोजीका लागि सुसंगत प्रॉम्प्ट इन्जिनीयरिङ

**प्राविधिक कार्यान्वयन:**

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

**परिणामहरू:** चिकित्सकहरूको लागि सुधारिएको डायग्नोस्टिक सिफारिसहरू पूर्ण HIPAA अनुपालनमा राख्दै र प्रणालीहरू बीच सन्दर्भ स्विचिङमा उल्लेखनीय कटौती।

### केस अध्ययन ३: वित्तीय सेवाहरू जोखिम विश्लेषण

एक वित्तीय संस्था ले विभिन्न विभागहरूमा आफ्नो जोखिम विश्लेषण प्रक्रियाहरू मानकीकृत गर्न MCP लागू गर्‍यो:

- क्रेडिट जोखिम, ठगी पहिचान, र लगानी जोखिम मोडेलहरूको लागि एकीकृत इन्टरफेस सिर्जना गर्‍यो
- कडा पहुँच नियन्त्रण र मोडेल संस्करण व्यवस्थापन लागू गर्‍यो
- सबै AI सिफारिसहरूको अडिटयोग्यता सुनिश्चित गर्‍यो
- विविध प्रणालीहरूमा डाटा ढाँचा निरन्तर कायम राख्यो

**प्राविधिक कार्यान्वयन:**

```java
// वित्तीय जोखिम मूल्यांकनको लागि Java MCP सर्भर
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // वित्तीय अनुपालन सुविधाहरू सहित MCP सर्भर सिर्जना गर्नुहोस्
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

**परिणामहरू:** सुधारिएको नियामक अनुपालन, ४०% छिटो मोडेल तैनाथ चक्रहरू, र विभागहरूमा जोखिम मूल्याङ्कन निरन्तरता।

### केस अध्ययन ४: माइक्रोसफ्ट प्लेइराइट MCP सर्भर ब्राउजर स्वचालनका लागि

माइक्रोसफ्टले [प्लेइराइट MCP सर्भर](https://github.com/microsoft/playwright-mcp) विकास गर्‍यो जसले मोडेल सन्दर्भ प्रोटोकल मार्फत सुरक्षित, मानकीकृत ब्राउजर स्वचालन सक्षम गर्छ। यो उत्पादन-तयार सर्भरले AI एजेन्ट र LLM हरूलाई नियन्त्रणयोग्य, अडिटयोग्य, र विस्तारयोग्य तरिकाले वेब ब्राउजरहरूसँग अन्तरक्रिया गर्न अनुमति दिन्छ—स्वचालित वेब परीक्षण, डेटा निष्कर्षण, र अन्त-हुँदै- workflow जस्ता प्रयोगहरू सक्षम पार्दै।

> **🎯 उत्पादन-तयार उपकरण**
> 
> यो केस अध्ययनले तपाइँले आज प्रयोग गर्न सक्ने वास्तविक MCP सर्भर देखाउँछ! प्लेइराइट MCP सर्भर र ९ अन्य उत्पादन-तयार माइक्रोसफ्ट MCP सर्भरहरूबारे थप जान्न हाम्रो [**माइक्रोसफ्ट MCP सर्भरहरू मार्गदर्शन**](microsoft-mcp-servers.md#8--playwright-mcp-server) मा जानुहोस्।

**मुख्य सुविधाहरू:**
- ब्राउजर स्वचालन कार्यक्षमताहरू (नेभिगेसन, फारम भर्नु, स्क्रीनसट लिनु, आदि) MCP उपकरणहरूका रूपमा प्रकट गर्दछ
- अनधिकृत क्रियाकलाप रोक्न कडा पहुँच नियन्त्रण र स्यान्डबक्सिंग लागू गर्दछ
- सबै ब्राउजर अन्तरक्रियाहरूका लागि विस्तृत अडिट लगहरू प्रदान गर्दछ
- एजेन्ट-चालित स्वचालनका लागि Azur OpenAI र अन्य LLM प्रदायकहरूसँग एकीकरण समर्थन गर्दछ
- GitHub Copilot को कोडिङ एजेन्टलाई वेब ब्राउजिङ क्षमताहरू दिने

**प्राविधिक कार्यान्वयन:**

```typescript
// TypeScript: MCP सर्भरमा Playwright ब्राउजर स्वचालन उपकरणहरू दर्ता गर्दै
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// URL मा जान र स्क्रिनशट क्याप्चर गर्न उपकरण दर्ता गर्नुहोस्
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

// MCP सर्भर सुरु गर्नुहोस्
server.listen(8080);
```

**परिणामहरू:**

- AI एजेन्ट र LLM हरूका लागि सुरक्षित, प्रोग्रामात्मक ब्राउजर स्वचालन सक्षम बनायो
- म्यानुअल परीक्षण प्रयास घटायो र वेब आवेदनहरूको परीक्षण कवरेज सुधार गर्‍यो
- उद्यम वातावरणहरूमा ब्राउजर-आधारित उपकरण एकीकरणका लागि पुन: प्रयोगयोग्य, विस्तारयोग्य फ्रेमवर्क प्रदान गर्‍यो
- GitHub Copilot को वेब ब्राउजिङ क्षमताहरूलाई समर्थन गर्‍यो

**सन्दर्भहरू:**

- [प्लेइराइट MCP सर्भर GitHub रिपोजिटरी](https://github.com/microsoft/playwright-mcp)
- [माइक्रोसफ्ट AI र स्वचालन समाधानहरू](https://azure.microsoft.com/en-us/products/ai-services/)

### केस अध्ययन ५: Azure MCP – सेवा रूपमा उद्यम ग्रेड मोडेल सन्दर्भ प्रोटोकल

Azure MCP सर्भर ([https://aka.ms/azmcp](https://aka.ms/azmcp)) माइक्रोसफ्टको व्यवस्थापन गरिएको, उद्यम-ग्रेड मोडेल सन्दर्भ प्रोटोकल कार्यान्वयन हो, जुन स्केलेबल, सुरक्षित, र अनुपालन गर्ने MCP सर्भर क्षमताहरू क्लाउड सेवाका रूपमा प्रदान गर्ने उद्देश्यले डिजाइन गरिएको हो। Azure MCP ले संगठनहरूलाई छिटो MCP सर्भरहरू Azure AI, डेटा, र सुरक्षा सेवाहरूसँग एकीकृत गर्न, व्यवस्थापन गर्न, र तैनाथ गर्न मद्दत गर्दछ, ऑपरेशनल ओभरहेड घटाउँदै र AI स्वीकृति तीव्र बनाउँदै।

> **🎯 उत्पादन-तयार उपकरण**
> 
> यो वास्तविक MCP सर्भर हो जुन तपाईं आजै प्रयोग गर्न सक्नुहुन्छ! Microsoft Foundry MCP Server को बारेमा थप जान्न हाम्रो [**माइक्रोसफ्ट MCP सर्भरहरू मार्गदर्शन**](microsoft-mcp-servers.md) मा जानुहोस्।


- पूर्ण रूपमा व्यवस्थापन गरिएको MCP सर्भर होस्टिंग जसमा बिल्ट-इन स्केलिङ, मोनिटरिङ, र सुरक्षा छ
- Azure OpenAI, Azure AI Search, र अन्य Azure सेवाहरूसँग मूल एकीकरण
- Microsoft Entra ID द्वारा उद्यम प्रमाणीकरण र प्राधिकरण
- कस्टम उपकरणहरू, प्रॉम्प्ट टेम्प्लेटहरू, र स्रोत कनेक्टरहरूको समर्थन
- उद्यम सुरक्षा र नियामक आवश्यकतासँग अनुपालन

**प्राविधिक कार्यान्वयन:**

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

**परिणामहरू:**  
- उद्यम AI परियोजनाहरूको लागि मूल्य-लिन समय घटाइयो र तयार-प्रयोगयोग्य, अनुपालनीय MCP सर्भर प्लेटफार्म प्रदान गर्‍यो
- LLMs, उपकरणहरू, र उद्यम डेटा स्रोतहरूको एकीकरण सरल बनायो
- MCP वर्कलोडहरूका लागि सुरक्षा, अवलोकनयोग्यता, र संचालन कुशलता बढायो
- Azure SDK को उत्कृष्ट अभ्यासहरू र वर्तमान प्रमाणीकरण ढाँचाहरू प्रयोग गरेर कोड गुणस्तर सुधार गर्‍यो

**सन्दर्भहरू:**  
- [Azure MCP डकुमेन्टेशन](https://aka.ms/azmcp)
- [Azure MCP सर्भर GitHub रिपोजिटरी](https://github.com/Azure/azure-mcp)
- [Azure AI सेवाहरू](https://azure.microsoft.com/en-us/products/ai-services/)
- [Microsoft MCP केन्द्र](https://mcp.azure.com)

## केस अध्ययन ६: NLWeb 
MCP (मोडेल सन्दर्भ प्रोटोकल) च्याटबोट र AI सहायकहरूलाई उपकरणहरूसँग अन्तरक्रिया गर्न उदीयमान प्रोटोकल हो। प्रत्येक NLWeb उदाहरण पनि MCP सर्भर हो, जसले एक मुख्य विधि, सोध्न (ask), समर्थन गर्दछ जुन प्राकृतिक भाषामा वेबसाइटलाई प्रश्न सोध्न प्रयोग गरिन्छ। फर्काइएको उत्तरले schema.org प्रयोग गर्छ, जुन वेब डाटालाई वर्णन गर्ने लोकप्रिय शब्दावली हो। सरल भाषामा भन्नुपर्दा, MCP भनेको NLWeb हो जसरी Http HTML हो। NLWeb ले प्रोटोकलहरू, Schema.org ढाँचाहरू, र नमूना कोड संयोजन गरेर साइटहरूलाई ती अन्तबिन्दुहरू छिटो सिर्जना गर्न मद्दत गर्दछ, जसले कन्भर्सेशनल इन्टरफेस मार्फत मानवहरूलाई र प्राकृतिक एजेन्ट-बाट-एजेन्ट अन्तरक्रियाबाट मेसिनहरूलाई लाभ पुर्‍याउँछ।

NLWeb का दुई फरक कम्पोनेन्टहरू छन्।
- एउटा प्रोटोकल, प्रकृतिक भाषामा साइटसँग अन्तरक्रिया गर्नका लागि सुरुमा धेरै सरल, र फर्काइएको जवाफको लागि json र schema.org प्रयोग गर्ने ढाँचा। थप विवरणहरूको लागि REST API को डकुमेन्टेशन हेर्नुहोस्।
- (1) को एक सरल कार्यान्वयन जसले अवस्थित मार्कअप प्रयोग गर्छ, ती साइटहरूका लागि जुन वस्तुहरूको सूची (उत्पादनहरू, रेसिपीहरू, आकर्षणहरू, समीक्षा, आदि) को रूपमा प्रतिनिधित्व गर्न सकिन्छ। प्रयोगकर्ता अन्तरफलक विजेटहरूको सेटसँगै, साइटहरूले सजिलै आफ्नो सामग्रीको लागि कन्भर्सेशनल इन्टरफेसहरू प्रदान गर्न सक्छन्। यो कसरी काम गर्छ भन्ने विस्तृत जानकारीका लागि Life of a chat query को डकुमेन्टेशन हेर्नुहोस्।
 
**सन्दर्भहरू:**  
- [Azure MCP डकुमेन्टेशन](https://aka.ms/azmcp)
- [NLWeb](https://github.com/microsoft/NlWeb)

### केस अध्ययन ७: माइक्रोसफ्ट फाउन्ड्री MCP सर्भर – उद्यम AI एजेन्ट एकीकरण

माइक्रोसफ्ट फाउन्ड्री MCP सर्भरहरूले देखाउँछन् कि MCP कसरी उद्यम वातावरणहरूमा AI एजेन्ट र workflow हरूलाई व्यवस्थापन र समन्वय गर्न प्रयोग गर्न सकिन्छ। MCP लाई माइक्रोसफ्ट फाउन्ड्रीसँग एकीकृत गरेर, संगठनहरूले एजेन्ट अन्तरक्रियाहरू मानकीकृत गर्न, फाउन्ड्रीको workflow व्यवस्थापन प्रयोग गर्न, र सुरक्षित, मापनयोग्य तैनाथी सुनिश्चित गर्न सक्छन्।

> **🎯 उत्पादन-तयार उपकरण**
> 
> यो वास्तविक MCP सर्भर हो जुन तपाईं आजै प्रयोग गर्न सक्नुहुन्छ! माइक्रोसफ्ट फाउन्ड्री MCP सर्भरको बारेमा थप जान्न हाम्रो [**माइक्रोसफ्ट MCP सर्भरहरू मार्गदर्शन**](microsoft-mcp-servers.md#9--microsoft-foundry-mcp-server) मार्फत हेर्नुहोस्।

**मुख्य सुविधाहरू:**
- Azure को AI पारिस्थितिकी तन्त्रमा व्यापक पहुँच, मोडेल क्याटलगहरू र तैनाथी व्यवस्थापन सहित
- RAG अनुप्रयोगहरूको लागि Azure AI Search सँग ज्ञान अनुक्रमणिका
- AI मोडेल प्रदर्शन र गुणस्तर आश्वासनका लागि मूल्याङ्कन उपकरणहरू
- Microsoft Foundry क्याटलग र ल्याबहरूसँग एकीकरणले नयाँ अनुसन्धान मोडेलहरू
- उत्पादन अवस्थामा एजेन्ट व्यवस्थापन र मूल्याङ्कन क्षमता

**परिणामहरू:**
- AI एजेन्ट workflow हरूको छिटो प्रोटोटाइपिङ र बलियो मोनिटरिङ
- उन्नत परिदृश्यहरूका लागि Azure AI सेवाहरूसँग सहज एकीकरण
- एजेन्ट पाइपलाइनहरू निर्माण, तैनाथ, र मोनिटर गर्ने एकीकृत इन्टरफेस
- उद्यमहरूको लागि सुरक्षा, अनुपालन, र संचालन कुशलता सुधार
- जटिल एजेन्ट-चालित प्रक्रियाहरूमा नियन्त्रण कायम राख्दै AI स्वीकृतिलाई तीव्र बनायो

**सन्दर्भहरू:**
- [Microsoft Foundry MCP Server GitHub रिपोजिटरी](https://github.com/azure-ai-foundry/mcp-foundry)
- [Azure AI एजेन्टहरूलाई MCP सँग एकीकृत गर्ने (Microsoft Foundry ब्लग)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

### केस अध्ययन ८: फाउन्ड्री MCP प्लेग्राउण्ड – प्रयोग र प्रोटोटाइपिङ

फाउन्ड्री MCP प्लेग्राउण्ड MCP सर्भर र माइक्रोसफ्ट फाउन्ड्री एकीकरणहरूसँग प्रयोग गर्न तयार वातावरण प्रदान गर्दछ। विकासकर्ताहरूले छिटो प्रोटोटाइप, परीक्षण, र AI मोडेल र एजेन्ट workflow हरूको मूल्याङ्कन गर्न सक्छन् Microsoft Foundry क्याटलग र ल्याबका स्रोतहरूको प्रयोगले। प्लेग्राउण्ड सेटअप सजिलो बनाउँछ, नमूना परियोजनाहरू उपलब्ध गराउँछ, र सहकार्यात्मक विकास समर्थन गर्दछ, जसले न्यूनतम खर्चमा उत्कृष्ट अभ्यास र नयाँ परिदृश्यहरू अन्वेषण गर्न सजिलो बनाउँछ। यो विशेष गरी विचारहरू प्रमाणित गर्न, प्रयोगहरू साझा गर्न, र जटिल पूर्वाधार बिना सिकाइ तीव्र बनाउन चाहने टोलीहरूका लागि उपयोगी छ। बारम्बार प्रवेशद्वार घटाएर, प्लेग्राउण्डले MCP र माइक्रोसफ्ट फाउन्ड्री पारिस्थितिकी तन्त्रमा नवप्रवर्तन र समुदाय योगदानलाई प्रोत्साहित गर्दछ।

**सन्दर्भहरू:**

- [फाउन्ड्री MCP प्लेग्राउण्ड GitHub रिपोजिटरी](https://github.com/azure-ai-foundry/foundry-mcp-playground)

### केस अध्ययन ९: माइक्रोसफ्ट लर्न डक्स MCP सर्भर – AI-सञ्चालित डकुमेन्टेसन पहुँच

माइक्रोसफ्ट लर्न डक्स MCP सर्भर एउटा क्लाउड होस्ट गरिएको सेवा हो जसले AI सहायकहरूलाई आधिकारिक माइक्रोसफ्ट डकुमेन्टेसनमा वास्तविक समयमा पहुँच प्रदान गर्दछ मोडेल सन्दर्भ प्रोटोकल मार्फत। यो उत्पादन-तयार सर्भरले समग्र माइक्रोसफ्ट लर्न पारिस्थितिकी तन्त्रसँग जोडिन्छ र सबै आधिकारिक माइक्रोसफ्ट स्रोतहरूमा सेमेन्टिक खोज सक्षम पार्दछ।

> **🎯 उत्पादन-तयार उपकरण**
> 
> यो वास्तविक MCP सर्भर हो जुन तपाईं आज प्रयोग गर्न सक्नुहुन्छ! माइक्रोसफ्ट लर्न डक्स MCP सर्भरको बारेमा थप जान्न हाम्रो [**माइक्रोसफ्ट MCP सर्भरहरू मार्गदर्शन**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server) मा हेर्नुहोस्।

**मुख्य सुविधाहरू:**
- आधिकारिक माइक्रोसफ्ट डकुमेन्टेसन, Azure डक्स, र माइक्रोसफ्ट 365 डकुमेन्टेसनमा वास्तविक-समय पहुँच
- सन्दर्भ र उद्देश्य बुझ्ने उन्नत सेमेन्टिक खोज क्षमताहरू
- माइक्रोसफ्ट लर्न सामग्री प्रकाशित हुने बित्तिकै सधैं अपडेट हुने जानकारी
- माइक्रोसफ्ट लर्न, Azure डकुमेन्टेसन, र माइक्रोसफ्ट 365 स्रोतहरूमा व्यापक आवरण
- लेख शीर्षक र URL हरू सहित उच्च-गुणस्तर सामग्री चंकहरूमा १० सम्म फर्काउँछ

**किन यो महत्वपूर्ण छ:**
- माइक्रोसफ्ट प्रविधिहरूका लागि "पुरानो AI ज्ञान" समस्या समाधान गर्छ
- AI सहायकहरूले नयाँ .NET, C#, Azure, र माइक्रोसफ्ट 365 सुविधाहरूको पहुँच सुनिश्चित गर्छ
- सही कोड निर्माणको लागि अधिकारिक, पहिलो पक्ष जानकारी प्रदान गर्छ
- तीव्र विकास भइरहेका माइक्रोसफ्ट प्रविधिहरूसँग काम गर्ने विकासकर्ताहरूका लागि आवश्यक

**परिणामहरू:**
- माइक्रोसफ्ट प्रविधिहरूका लागि AI-जनित कोडको शुद्धता नाटकीय रूपमा सुधार भयो
- वर्तमान डकुमेन्टेसन र उत्कृष्ट अभ्यासहरूको खोजीमा समय कटौती गर्‍यो
- सन्दर्भ-आधारित डकुमेन्टेसन पुनःप्राप्तिले विकासकर्ता उत्पादकत्व बढायो
- IDE छोड्नु नपर्ने गरी विकास workflow सँग सहज एकीकरण

**सन्दर्भहरू:**
- [माइक्रोसफ्ट लर्न डक्स MCP सर्भर GitHub रिपोजिटरी](https://github.com/MicrosoftDocs/mcp)
- [माइक्रोसफ्ट लर्न डकुमेन्टेसन](https://learn.microsoft.com/)

## व्यावहारिक परियोजनाहरू

### परियोजना १: बहु-प्रदायक MCP सर्भर निर्माण गर्नुहोस्

**उद्देश्य:** विशिष्ट मापदण्डहरूका आधारमा अनुरोधहरू बहु AI मोडेल प्रदायकहरूमा मार्गनिर्देशन गर्न सक्ने MCP सर्भर सिर्जना गर्नुहोस्।

**आवश्यकताहरू:**

- कम्तिमा तीन फरक मोडेल प्रदायकहरूलाई समर्थन गर्न (जस्तै OpenAI, Anthropic, स्थानीय मोडेलहरू)
- अनुरोध मेटाडाटा आधारित मार्गनिर्देशन यन्त्र लागू गर्न
- प्रदायक प्रमाणपत्र व्यवस्थापनको लागि कन्फिगरेसन प्रणाली सिर्जना गर्न
- प्रदर्शन र लागतका लागि क्याचिङ थप्न
- प्रयोग अनुगमनको लागि सरल ड्यासबोर्ड बनाउनुहोस्

**कार्यान्वयन चरणहरू:**

1. आधारभूत MCP सर्भर पूर्वाधार सेटअप गर्नुहोस्
2. प्रत्येक AI मोडेल सेवाका लागि प्रदायक एडेप्टरहरू कार्यान्वयन गर्नुहोस्
3. अनुरोध विशेषताहरूका आधारमा मार्गनिर्देशन तर्क सिर्जना गर्नुहोस्
4. बारम्बार अनुरोधहरूको लागि क्याचिङ यन्त्रहरू थप्नुहोस्
5. मोनिटरिङ ड्यासबोर्ड विकास गर्नुहोस्
6. विभिन्न अनुरोध ढाँचाहरूमा परीक्षण गर्नुहोस्

**प्रविधिहरू:** Python (.NET/Java/Python तपाईंको प्राथमिकतामा आधारित), Redis क्याचिङका लागि, र ड्यासबोर्डका लागि सरल वेब फ्रेमवर्कबाट छनौट गर्नुहोस्।

### परियोजना २: उद्यम प्रॉम्प्ट व्यवस्थापन प्रणाली

**उद्देश्य:** एउटा MCP-आधारित प्रणाली विकास गर्नुहोस् जसले संगठनभर प्रॉम्प्ट टेम्प्लेटहरूको व्यवस्थापन, संस्करण नियन्त्रण, र तैनाथी गर्न सकोस्।

**आवश्यकताहरू:**


- प्रम्प्ट टेम्प्लेटहरूको लागि एक केन्द्रिय रेपो बनाउनुहोस्
- संस्करण व्यवस्थापन र स्वीकृति कार्यप्रवाहहरू लागू गर्नुहोस्
- नमूना इनपुटहरूसँग टेम्प्लेट परीक्षण क्षमताहरू विकास गर्नुहोस्
- भूमिका-आधारित पहुँच नियन्त्रणहरू विकास गर्नुहोस्
- टेम्प्लेट पुनःप्राप्ति र डिप्लोइमेन्टको लागि API सिर्जना गर्नुहोस्

**कार्यान्वयन चरणहरू:**

1. टेम्प्लेट भण्डारणको लागि डाटाबेस स्किमा डिजाइन गर्नुहोस्
2. टेम्प्लेट CRUD अपरेशन्सको लागि कोर API सिर्जना गर्नुहोस्
3. संस्करण व्यवस्थापन प्रणाली लागू गर्नुहोस्
4. स्वीकृति कार्यप्रवाह विकास गर्नुहोस्
5. परीक्षण फ्रेमवर्क विकास गर्नुहोस्
6. व्यवस्थापनको लागि सरल वेब इन्टरफेस सिर्जना गर्नुहोस्
7. MCP सर्भरसँग एकीकरण गर्नुहोस्

**प्रविधिहरू:** व्यवस्थापन इन्टरफेसको लागि तपाईँको रोजाइको ब्याकएन्ड फ्रेमवर्क, SQL वा NoSQL डाटाबेस, र फ्रन्टएन्ड फ्रेमवर्क।

### परियोजना ३: MCP-आधारित सामग्री उत्पादन प्लेटफर्म

**उद्देश्य:** MCP प्रयोग गरेर विभिन्न सामग्री प्रकारहरूमा निरन्तर परिणामहरू प्रदान गर्ने सामग्री उत्पादन प्लेटफर्म निर्माण गर्नुहोस्।

**आवश्यकताहरू:**

- बहु सामग्री ढाँचाहरूलाई समर्थन गर्नुहोस् (ब्लग पोस्टहरू, सामाजिक मिडिया, मार्केटिङ प्रति)
- अनुकूलन विकल्पहरूसँग टेम्प्लेट-आधारित उत्पादन लागू गर्नुहोस्
- सामग्री समीक्षा र प्रतिक्रिया प्रणाली सिर्जना गर्नुहोस्
- सामग्री प्रदर्शन मेट्रिक्स ट्र्याक गर्नुहोस्
- सामग्री संस्करण र पुनरावृत्तिलाई समर्थन गर्नुहोस्

**कार्यान्वयन चरणहरू:**

1. MCP क्लाइन्ट पूर्वाधार स्थापना गर्नुहोस्
2. विभिन्न सामग्री प्रकारहरूको लागि टेम्प्लेट सिर्जना गर्नुहोस्
3. सामग्री उत्पादन पाइपलाइन निर्माण गर्नुहोस्
4. समीक्षा प्रणाली लागू गर्नुहोस्
5. मेट्रिक्स ट्र्याकिंग प्रणाली विकास गर्नुहोस्
6. टेम्प्लेट व्यवस्थापन र सामग्री उत्पादनको लागि प्रयोगकर्ता इन्टरफेस सिर्जना गर्नुहोस्

**प्रविधिहरू:** तपाईँको रोजाइको प्रोग्रामिङ भाषा, वेब फ्रेमवर्क, र डाटाबेस प्रणाली।

## MCP प्रविधिका लागि भविष्यका दिशाहरू

### उदाउँदै गरेका प्रवृत्तिहरू

1. **बहु-मोडल MCP**
   - तस्वीर, अडियो, र भिडियो मोडेलहरूसँग अन्तरक्रियालाई मानकीकृत गर्न MCP को विस्तार
   - क्रस-मोडल तर्क क्षमताहरूको विकास
   - विभिन्न मोडालिटीहरूको लागि मानकीकृत प्रम्प्ट ढाँचाहरू

2. **फेडेरेटेड MCP पूर्वाधार**
   - संगठनहरू बीच स्रोतहरू साझा गर्न सक्ने वितरित MCP नेटवर्कहरू
   - सुरक्षित मोडेल साझेदारीका लागि मानकीकृत प्रोटोकलहरू
   - गोपनीयता-संरक्षण गणना प्रविधिहरू

3. **MCP बजारहरू**
   - MCP टेम्प्लेट र प्लगइनहरू साझेदारी र मुद्रीकरण गर्नका लागि पारिस्थितिकी तन्त्रहरू
   - गुणस्तर सुनिश्चितता र प्रमाणिकरण प्रक्रियाहरू
   - मोडेल बजारहरूसँग एकीकरण

4. **एज कम्प्युटिङको लागि MCP**
   - स्रोत-सीमित एज उपकरणहरूको लागि MCP मानकहरूको अनुकूलन
   - कम-ब्यान्डविथ वातावरणका लागि अनुकूलित प्रोटोकलहरू
   - IoT पारिस्थितिकी तन्त्रहरूको लागि विशेष MCP कार्यान्वयनहरू

5. **नियामक फ्रेमवर्कहरू**
   - नियामक अनुपालनका लागि MCP विस्तारहरूको विकास
   - मानकीकृत अडिट ट्रेलहरू र व्याख्यात्मक अन्तरफेसहरू
   - उदाउँदै गरेका AI शासन फ्रेमवर्कहरूसँग एकीकरण

### माइक्रोसफ्टबाट MCP समाधानहरू

माइक्रोसफ्ट र एजुरले विभिन्न परिप्रेक्ष्यहरूमा विकासकर्ताहरूलाई MCP लागू गर्न मद्दत गर्न धेरै खुला-स्रोत रेपोहरू विकास गरेको छ:

#### माइक्रोसफ्ट संगठन

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - ब्राउजर स्वचालन र परीक्षणका लागि प्लेयराइट MCP सर्भर
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - स्थानीय परीक्षण र समुदाय योगदानका लागि OneDrive MCP सर्भर कार्यान्वयन
3. [NLWeb](https://github.com/microsoft/NlWeb) - खुला प्रोटोकलहरूको संग्रह र सम्बन्धित खुला स्रोत उपकरणहरू। यसको मुख्य फोकस AI वेबको आधारभूत तह स्थापना गर्नु हो

#### Azure-Samples संगठन

1. [mcp](https://github.com/Azure-Samples/mcp) - Azure मा विभिन्न भाषाहरू प्रयोग गरेर MCP सर्भरहरू निर्माण र एकीकरण गर्नका लागि नमूना, उपकरणहरू, र स्रोतहरूका लिंकहरू
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - वर्तमान मोडेल सन्दर्भ प्रोटोकल विशिष्टतासँग प्रमाणीकरण देखाउने सन्दर्भ MCP सर्भरहरू
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure Functions मा रिमोट MCP सर्भर कार्यान्वयनहरूको ल्यान्डिङ पृष्ठ, भाषा-विशिष्ट भण्डारका लिंकहरू सहित
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure Functions सँग Python प्रयोग गरेर अनुकूल रिमोट MCP सर्भर निर्माण र डिप्लोइ गर्न त्वरित प्रारम्भ टेम्प्लेट
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Azure Functions सँग .NET/C# प्रयोग गरेर अनुकूल रिमोट MCP सर्भर निर्माण र डिप्लोइ गर्न त्वरित प्रारम्भ टेम्प्लेट
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Azure Functions सँग TypeScript प्रयोग गरेर अनुकूल रिमोट MCP सर्भर निर्माण र डिप्लोइ गर्न त्वरित प्रारम्भ टेम्प्लेट
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Python प्रयोग गरेर रिमोट MCP सर्भरहरूमा Azure API व्यवस्थापनलाई AI गेटवेको रूपमा प्रयोग
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI प्रयोगहरू सहित MCP क्षमताहरू, Azure OpenAI र AI Foundry सँग एकीकृत

यी रेपोहरूले विभिन्न प्रोग्रामिङ भाषाहरू र Azure सेवाहरूमा मोडेल सन्दर्भ प्रोटोकलसँग काम गर्दा विभिन्न कार्यान्वयनहरू, टेम्प्लेटहरू, र स्रोतहरू प्रदान गर्दछन्। तिनीहरूले आधारभूत सर्भर कार्यान्वयनहरूदेखि लिएर प्रमाणीकरण, क्लाउड डिप्लोइमेन्ट, र उद्यम एकीकरण परिदृश्यहरू सम्मका प्रयोगहरू समेट्छन्।

#### MCP स्रोत निर्देशिका

आधिकारिक माइक्रोसफ्ट MCP रेपोमा रहेको [MCP स्रोत निर्देशिका](https://github.com/microsoft/mcp/tree/main/Resources) ले नमूना स्रोतहरू, प्रम्प्ट टेम्प्लेटहरू, र उपकरण परिभाषाहरूको क्युरेटेड सङ्ग्रह प्रदान गर्दछ जुन मोडेल सन्दर्भ प्रोटोकल सर्भरहरूसँग प्रयोगका लागि तयार गरिएको हो। यो निर्देशिका विकासकर्ताहरूलाई MCP छिटो सुरु गर्न सहयोग पुर्‍याउन पुन: प्रयोगयोग्य निर्माण ब्लकहरू र उत्कृष्ट अभ्यासका उदाहरणहरू प्रस्तुत गर्दछ:

- **प्रम्प्ट टेम्प्लेटहरू:** समान्य AI कार्यहरू र परिदृश्यहरूका लागि तयार-प्रयोग टेम्प्लेटहरू, जुन तपाईँको आफ्नै MCP सर्भर कार्यान्वयनको लागि अनुकूलन गर्न सकिन्छ।
- **उपकरण परिभाषाहरू:** विभिन्न MCP सर्भरहरूमा उपकरण एकीकरण र आह्वानलाई मानकीकृत गर्न उदाहरण उपकरण स्किमाहरू र मेटाडेटा।
- **स्रोत नमूना:** MCP फ्रेमवर्क भित्र डेटा स्रोतहरू, API हरू, र बाह्य सेवाहरूमा जडान गर्ने उदाहरण स्रोत परिभाषाहरू।
- **सन्दर्भ कार्यान्वयनहरू:** वास्तविक MCP परियोजनाहरूमा स्रोतहरू, प्रम्प्टहरू, र उपकरणहरू कसरी संरचना र व्यवस्थापन गर्ने भनेर देखाउने व्यावहारिक नमूनाहरू।

यी स्रोतहरूले विकासलाई तीव्र पार्छन्, मानकीकरणलाई प्रवर्द्धन गर्छन्, र MCP-आधारित समाधानहरू निर्माण र डिप्लोइ गर्दा उत्कृष्ट अभ्यासहरू सुनिश्चित गर्न मद्दत गर्छन्।

#### MCP स्रोत निर्देशिका

- [MCP स्रोतहरू (नमूना प्रम्प्टहरू, उपकरणहरू, र स्रोत परिभाषाहरू)](https://github.com/microsoft/mcp/tree/main/Resources)

### अनुसन्धान अवसरहरू

- MCP फ्रेमवर्क भित्र कुशल प्रम्प्ट अनुकूलन प्रविधिहरू
- बहु-टेनेंट MCP डिप्लोइमेन्टहरूको लागि सुरक्षा मोडलहरू
- विभिन्न MCP कार्यान्वयनहरूमा प्रदर्शन मापन
- MCP सर्भरहरूको औपचारिक पुष्टि विधिहरू

## निष्कर्ष

मोडेल सन्दर्भ प्रोटोकल (MCP) उद्योगभर मानकीकृत, सुरक्षित, र अन्तरक्रियाशील AI एकीकरणको भविष्यलाई छिटो आकार दिँदैछ। यस पाठका केस स्टडिज र ह्यान्ड्स-ऑन परियोजनाहरू मार्फत, तपाईँले देख्नुभयो कसरी प्रारम्भिक प्रयोगकर्ताहरू—माइक्रोसफ्ट र एजुर सामेल—ले MCP लाई वास्तविक विश्व चुनौतीहरू समाधान गर्न, AI अंगिकारलाई तिब्र बनाउने, र अनुपालन, सुरक्षा, र मापनशीलता सुनिश्चित गर्न प्रयोग गरिरहेका छन्। MCP को मोडुलर दृष्टिकोणले संगठनहरूलाई ठूलो भाषा मोडेलहरू, उपकरणहरू, र उद्यम डेटा unified, auditable framework मा जडान गर्न सक्षम गर्दछ। MCP विकास भइरहेकोले, समुदायसँग संलग्न रहनु, खुला स्रोत स्रोतहरू अन्वेषण गर्नु, र उत्कृष्ट अभ्यासहरू लागू गर्नु मजबूत, भविष्य-तयार AI समाधानहरू निर्माण गर्न मुख्य हुन्छ।

## अतिरिक्त स्रोतहरू

- [MCP Foundry GitHub Repository](https://github.com/azure-ai-foundry/mcp-foundry)
- [Foundry MCP Playground](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [Integrating Azure AI Agents with MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - सुरक्षा उत्कृष्ट अभ्यासहरू
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

## अभ्यासहरू

1. एक केस स्टडी विश्लेषण गर्नुहोस् र वैकल्पिक कार्यान्वयन दृष्टिकोण प्रस्ताव गर्नुहोस्।
2. एक परियोजना विचार छान्नुहोस् र विस्तृत प्राविधिक विशिष्टता तयार गर्नुहोस्।
3. केस स्टडीहरूमा समेटिएको छैन भन्ने कुनै उद्योग अनुसंधान गर्नुहोस् र MCP त्यहाँका विशिष्ट चुनौतिहरू कसरी सम्बोधन गर्न सक्छ भन्ने रूपरेखा तयार गर्नुहोस्।
4. भविष्यका दिशाहरू मध्ये एउटा अन्वेषण गर्नुहोस् र त्यसलाई समर्थन गर्न नयाँ MCP विस्तारको अवधारणा सिर्जना गर्नुहोस्।

## के गर्ने अर्को

थप अन्वेषण गर्नुहोस्: [Microsoft MCP Servers](./microsoft-mcp-servers.md)

जारी राख्नुहोस्: [Module 8: Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->