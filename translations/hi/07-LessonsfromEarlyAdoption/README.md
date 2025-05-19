<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:03:47+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "hi"
}
-->
# Lessons from Early Adoprters

## अवलोकन

यह पाठ इस बात की पड़ताल करता है कि शुरुआती उपयोगकर्ताओं ने Model Context Protocol (MCP) का उपयोग कैसे किया है ताकि वास्तविक दुनिया की समस्याओं का समाधान किया जा सके और विभिन्न उद्योगों में नवाचार को बढ़ावा दिया जा सके। विस्तृत केस स्टडीज़ और व्यावहारिक परियोजनाओं के माध्यम से, आप देखेंगे कि MCP कैसे मानकीकृत, सुरक्षित, और स्केलेबल AI एकीकरण को सक्षम बनाता है—जो बड़े भाषा मॉडल, टूल्स, और एंटरप्राइज डेटा को एकीकृत फ्रेमवर्क में जोड़ता है। आप MCP-आधारित समाधानों को डिजाइन और बनाने का व्यावहारिक अनुभव प्राप्त करेंगे, सिद्ध कार्यान्वयन पैटर्न से सीखेंगे, और उत्पादन वातावरण में MCP तैनाती के लिए सर्वोत्तम प्रथाओं को जानेंगे। यह पाठ उभरते रुझानों, भविष्य की दिशा, और ओपन-सोर्स संसाधनों को भी उजागर करता है ताकि आप MCP तकनीक और इसके विकसित होते पारिस्थितिकी तंत्र में आगे बने रहें।

## सीखने के उद्देश्य

- विभिन्न उद्योगों में वास्तविक MCP कार्यान्वयन का विश्लेषण करें
- पूर्ण MCP-आधारित एप्लिकेशन डिजाइन और बनाएं
- MCP तकनीक में उभरते रुझान और भविष्य की दिशा की खोज करें
- वास्तविक विकास परिदृश्यों में सर्वोत्तम प्रथाओं को लागू करें

## वास्तविक MCP कार्यान्वयन

### केस स्टडी 1: एंटरप्राइज ग्राहक सहायता स्वचालन

एक बहुराष्ट्रीय कंपनी ने अपने ग्राहक सहायता सिस्टम्स में AI इंटरैक्शन को मानकीकृत करने के लिए MCP-आधारित समाधान लागू किया। इससे उन्हें निम्नलिखित लाभ मिले:

- कई LLM प्रदाताओं के लिए एकीकृत इंटरफेस बनाना
- विभागों में सुसंगत प्रॉम्प्ट प्रबंधन बनाए रखना
- मजबूत सुरक्षा और अनुपालन नियंत्रण लागू करना
- विशिष्ट आवश्यकताओं के आधार पर विभिन्न AI मॉडलों के बीच आसानी से स्विच करना

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

**परिणाम:** मॉडल लागत में 30% की कमी, प्रतिक्रिया स्थिरता में 45% सुधार, और वैश्विक संचालन में बेहतर अनुपालन।

### केस स्टडी 2: हेल्थकेयर डायग्नोस्टिक असिस्टेंट

एक हेल्थकेयर प्रदाता ने कई विशेषज्ञ चिकित्सा AI मॉडलों को एकीकृत करने के लिए MCP इन्फ्रास्ट्रक्चर विकसित किया, जबकि संवेदनशील रोगी डेटा की सुरक्षा सुनिश्चित की:

- सामान्य और विशेषज्ञ चिकित्सा मॉडलों के बीच सहज स्विचिंग
- कड़े गोपनीयता नियंत्रण और ऑडिट ट्रेल्स
- मौजूदा इलेक्ट्रॉनिक हेल्थ रिकॉर्ड (EHR) सिस्टम के साथ एकीकरण
- चिकित्सा शब्दावली के लिए सुसंगत प्रॉम्प्ट इंजीनियरिंग

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

**परिणाम:** चिकित्सकों के लिए बेहतर डायग्नोस्टिक सुझाव, पूर्ण HIPAA अनुपालन के साथ, और सिस्टम्स के बीच संदर्भ-स्विचिंग में महत्वपूर्ण कमी।

### केस स्टडी 3: वित्तीय सेवाओं में जोखिम विश्लेषण

एक वित्तीय संस्था ने विभिन्न विभागों में अपने जोखिम विश्लेषण प्रक्रियाओं को मानकीकृत करने के लिए MCP लागू किया:

- क्रेडिट जोखिम, धोखाधड़ी पहचान, और निवेश जोखिम मॉडलों के लिए एकीकृत इंटरफेस बनाया
- सख्त एक्सेस नियंत्रण और मॉडल संस्करण प्रबंधन लागू किया
- सभी AI सिफारिशों की ऑडिटेबिलिटी सुनिश्चित की
- विभिन्न सिस्टम्स में सुसंगत डेटा फॉर्मेटिंग बनाए रखा

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

**परिणाम:** बेहतर नियामक अनुपालन, 40% तेज मॉडल तैनाती चक्र, और विभागों में जोखिम मूल्यांकन की स्थिरता में सुधार।

### केस स्टडी 4: Microsoft Playwright MCP सर्वर ब्राउज़र स्वचालन के लिए

Microsoft ने [Playwright MCP server](https://github.com/microsoft/playwright-mcp) विकसित किया है जो Model Context Protocol के माध्यम से सुरक्षित, मानकीकृत ब्राउज़र स्वचालन को सक्षम बनाता है। यह समाधान AI एजेंट्स और LLMs को नियंत्रित, ऑडिटेबल, और विस्तारित तरीके से वेब ब्राउज़रों के साथ इंटरैक्ट करने देता है—जिससे स्वचालित वेब परीक्षण, डेटा निष्कर्षण, और एंड-टू-एंड वर्कफ़्लो जैसे उपयोग मामलों को सक्षम किया जा सकता है।

- ब्राउज़र स्वचालन क्षमताओं (नेविगेशन, फॉर्म भरना, स्क्रीनशॉट कैप्चर, आदि) को MCP टूल्स के रूप में एक्सपोज़ करता है
- अनधिकृत क्रियाओं को रोकने के लिए सख्त एक्सेस कंट्रोल और सैंडबॉक्सिंग लागू करता है
- सभी ब्राउज़र इंटरैक्शन के लिए विस्तृत ऑडिट लॉग प्रदान करता है
- एजेंट-ड्रिवन स्वचालन के लिए Azure OpenAI और अन्य LLM प्रदाताओं के साथ एकीकरण का समर्थन करता है

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

**परिणाम:**  
- AI एजेंट्स और LLMs के लिए सुरक्षित, प्रोग्रामेटिक ब्राउज़र स्वचालन सक्षम किया  
- मैनुअल परीक्षण प्रयास कम किए और वेब एप्लिकेशन के लिए परीक्षण कवरेज बेहतर किया  
- एंटरप्राइज वातावरण में ब्राउज़र-आधारित टूल एकीकरण के लिए पुन: प्रयोज्य, विस्तारित फ्रेमवर्क प्रदान किया

**References:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### केस स्टडी 5: Azure MCP – एंटरप्राइज-ग्रेड Model Context Protocol as a Service

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) Microsoft का प्रबंधित, एंटरप्राइज-ग्रेड Model Context Protocol कार्यान्वयन है, जिसे क्लाउड सेवा के रूप में स्केलेबल, सुरक्षित, और अनुपालन MCP सर्वर क्षमताएं प्रदान करने के लिए डिज़ाइन किया गया है। Azure MCP संगठनों को तेजी से MCP सर्वर तैनात करने, प्रबंधित करने, और Azure AI, डेटा, और सुरक्षा सेवाओं के साथ एकीकृत करने में सक्षम बनाता है, जिससे संचालन लागत कम होती है और AI अपनाने में तेजी आती है।

- अंतर्निहित स्केलिंग, निगरानी, और सुरक्षा के साथ पूर्ण रूप से प्रबंधित MCP सर्वर होस्टिंग  
- Azure OpenAI, Azure AI Search, और अन्य Azure सेवाओं के साथ मूल एकीकरण  
- Microsoft Entra ID के माध्यम से एंटरप्राइज प्रमाणीकरण और प्राधिकरण  
- कस्टम टूल्स, प्रॉम्प्ट टेम्पलेट्स, और संसाधन कनेक्टर्स का समर्थन  
- एंटरप्राइज सुरक्षा और नियामक आवश्यकताओं के साथ अनुपालन

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

**परिणाम:**  
- एंटरप्राइज AI परियोजनाओं के लिए त्वरित मूल्य प्राप्ति, एक तैयार-उपयोग, अनुपालन MCP सर्वर प्लेटफ़ॉर्म प्रदान करके  
- LLMs, टूल्स, और एंटरप्राइज डेटा स्रोतों के एकीकरण को सरल बनाया  
- MCP वर्कलोड के लिए बेहतर सुरक्षा, अवलोकनीयता, और संचालन दक्षता

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## केस स्टडी 6: NLWeb

MCP (Model Context Protocol) एक उभरता हुआ प्रोटोकॉल है जो चैटबॉट्स और AI सहायकों को टूल्स के साथ इंटरैक्ट करने की अनुमति देता है। प्रत्येक NLWeb इंस्टेंस भी एक MCP सर्वर होता है, जो एक मुख्य मेथड, ask, का समर्थन करता है, जिसका उपयोग वेबसाइट से प्राकृतिक भाषा में प्रश्न पूछने के लिए किया जाता है। प्राप्त प्रतिक्रिया schema.org का उपयोग करती है, जो वेब डेटा का वर्णन करने के लिए व्यापक रूप से उपयोग किया जाने वाला शब्दकोश है। सरल शब्दों में, MCP वैसा ही है जैसे Http है HTML के लिए। NLWeb प्रोटोकॉल, Schema.org फॉर्मेट्स, और नमूना कोड को मिलाकर साइट्स को तेजी से ऐसे एंडपॉइंट्स बनाने में मदद करता है, जो बातचीत आधारित इंटरफेस और एजेंट-टू-एजेंट संवाद दोनों के लिए लाभकारी हैं।

NLWeb के दो मुख्य घटक हैं:  
- एक प्रोटोकॉल, जो प्राकृतिक भाषा में साइट से इंटरफेस करने के लिए बहुत सरल है, और एक फॉर्मेट, जो json और schema.org का उपयोग करता है उत्तर देने के लिए। REST API पर अधिक जानकारी के लिए दस्तावेज़ देखें।  
- (1) का एक सरल कार्यान्वयन जो मौजूदा मार्कअप का उपयोग करता है, उन साइटों के लिए जो वस्तुओं (उत्पाद, रेसिपी, आकर्षण, समीक्षा, आदि) की सूचियों के रूप में अमूर्त की जा सकती हैं। उपयोगकर्ता इंटरफेस विजेट्स के साथ, साइटें अपने कंटेंट के लिए बातचीत इंटरफेस आसानी से प्रदान कर सकती हैं। यह कैसे काम करता है, इसके लिए Life of a chat query के दस्तावेज़ देखें।

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## व्यावहारिक परियोजनाएँ

### परियोजना 1: मल्टी-प्रोवाइडर MCP सर्वर बनाएं

**उद्देश्य:** एक MCP सर्वर बनाएं जो विशिष्ट मानदंडों के आधार पर कई AI मॉडल प्रदाताओं को अनुरोध भेज सके।

**आवश्यकताएं:**  
- कम से कम तीन अलग-अलग मॉडल प्रदाताओं का समर्थन करें (जैसे OpenAI, Anthropic, स्थानीय मॉडल)  
- अनुरोध मेटाडेटा के आधार पर रूटिंग तंत्र लागू करें  
- प्रदाता क्रेडेंशियल्स प्रबंधन के लिए कॉन्फ़िगरेशन सिस्टम बनाएं  
- प्रदर्शन और लागत को अनुकूलित करने के लिए कैशिंग जोड़ें  
- उपयोग की निगरानी के लिए एक सरल डैशबोर्ड बनाएं

**कार्यान्वयन चरण:**  
1. बुनियादी MCP सर्वर इन्फ्रास्ट्रक्चर सेट करें  
2. प्रत्येक AI मॉडल सेवा के लिए प्रदाता एडाप्टर लागू करें  
3. अनुरोध विशेषताओं के आधार पर रूटिंग लॉजिक बनाएं  
4. अक्सर पूछे जाने वाले अनुरोधों के लिए कैशिंग तंत्र जोड़ें  
5. निगरानी डैशबोर्ड विकसित करें  
6. विभिन्न अनुरोध पैटर्न के साथ परीक्षण करें

**प्रौद्योगिकियां:** Python (.NET/Java/Python आपकी पसंद के अनुसार), Redis कैशिंग के लिए, और डैशबोर्ड के लिए एक सरल वेब फ्रेमवर्क।

### परियोजना 2: एंटरप्राइज प्रॉम्प्ट प्रबंधन प्रणाली

**उद्देश्य:** संगठन में प्रॉम्प्ट टेम्पलेट्स के प्रबंधन, संस्करण नियंत्रण, और तैनाती के लिए MCP-आधारित प्रणाली विकसित करें।

**आवश्यकताएं:**  
- प्रॉम्प्ट टेम्पलेट्स के लिए केंद्रीकृत रिपॉजिटरी बनाएं  
- संस्करण नियंत्रण और अनुमोदन वर्कफ़्लो लागू करें  
- नमूना इनपुट के साथ टेम्पलेट परीक्षण क्षमताएं बनाएं  
- भूमिका-आधारित एक्सेस नियंत्रण विकसित करें  
- टेम्पलेट पुनःप्राप्ति और तैनाती के लिए API बनाएं

**कार्यान्वयन चरण:**  
1. टेम्पलेट भंडारण के लिए डेटाबेस स्कीमा डिज़ाइन करें  
2. टेम्पलेट CRUD ऑपरेशन्स के लिए कोर API बनाएं  
3. संस्करण नियंत्रण प्रणाली लागू करें  
4. अनुमोदन वर्कफ़्लो बनाएं  
5. परीक्षण फ्रेमवर्क विकसित करें  
6. प्रबंधन के लिए सरल वेब इंटरफेस बनाएं  
7. MCP सर्वर के साथ एकीकरण करें

**प्रौद्योगिकियां:** आपकी पसंद का बैकएंड फ्रेमवर्क, SQL या NoSQL डेटाबेस, और प्रबंधन इंटरफेस के लिए फ्रंटएंड फ्रेमवर्क।

### परियोजना 3: MCP-आधारित कंटेंट जनरेशन प्लेटफ़ॉर्म

**उद्देश्य:** एक कंटेंट जनरेशन प्लेटफ़ॉर्म बनाएं जो MCP का उपयोग करके विभिन्न कंटेंट प्रकारों में सुसंगत परिणाम प्रदान करे।

**आवश्यकताएं:**  
- कई कंटेंट फॉर्मेट्स का समर्थन करें (ब्लॉग पोस्ट, सोशल मीडिया, मार्केटिंग कॉपी)  
- कस्टमाइज़ेशन विकल्पों के साथ टेम्पलेट-आधारित जनरेशन लागू करें  
- कंटेंट समीक्षा और फीडबैक सिस्टम बनाएं  
- कंटेंट प्रदर्शन मेट्रिक्स ट्रैक करें  
- कंटेंट संस्करण नियंत्रण और पुनरावृत्ति का समर्थन करें

**कार्यान्वयन चरण:**  
1. MCP क्लाइंट इन्फ्रास्ट्रक्चर सेट करें  
2. विभिन्न कंटेंट प्रकारों के लिए टेम्पलेट बनाएं  
3. कंटेंट जनरेशन पाइपलाइन बनाएं  
4. समीक्षा प्रणाली लागू करें  
5. मेट्रिक्स ट्रैकिंग सिस्टम विकसित करें  
6. टेम्पलेट प्रबंधन और कंटेंट जनरेशन के लिए यूजर इंटरफेस बनाएं

**प्रौद्योगिकियां:** आपकी पसंदीदा प्रोग्रामिंग भाषा, वेब फ्रेमवर्क, और डेटाबेस सिस्टम।

## MCP तकनीक के लिए भविष्य की दिशा

### उभरते रुझान

1. **मल्टी-मोडल MCP**  
   - छवि, ऑडियो, और वीडियो मॉडलों के साथ इंटरैक्शन को मानकीकृत करने के लिए MCP का विस्तार  
   - क्रॉस-मोडल तर्क क्षमताओं का विकास  
   - विभिन्न मोडैलिटी के लिए मानकीकृत प्रॉम्प्ट फॉर्मेट

2. **फेडरेटेड MCP इन्फ्रास्ट्रक्चर**  
   - वितरित MCP नेटवर्क जो संगठनों के बीच संसाधन साझा कर सकते हैं  
   - सुरक्षित मॉडल साझा करने के लिए मानकीकृत प्रोटोकॉल  
   - गोपनीयता-संरक्षित गणना तकनीकें

3. **MCP मार्केटप्लेस**  
   - MCP टेम्पलेट्स और प्लगइन्स साझा करने और मुद्रीकृत करने के लिए इकोसिस्टम  
   - गुणवत्ता आश्वासन और प्रमाणन प्रक्रियाएं  
   - मॉडल मार्केटप्लेस के साथ एकीकरण

4. **एज कंप्यूटिंग के लिए MCP**  
   - संसाधन-सीमित एज डिवाइसेज के लिए MCP मानकों का अनुकूलन  
   - कम-बैंडविड्थ वातावरण के लिए अनुकूलित प्रोटोकॉल  
   - IoT इकोसिस्टम के लिए विशेष MCP कार्यान्वयन

5. **नियामक ढांचे**  
   - नियामक अनुपालन के लिए MCP एक्सटेंशन्स का विकास  
   - मानकीकृत ऑडिट ट्रेल्स और व्याख्यात्मक इंटरफेस  
   - उभरते AI गवर्नेंस फ्रेमवर्क के साथ एकीकरण

### Microsoft से MCP समाधान

Microsoft और Azure ने कई ओपन-सोर्स रिपॉजिटरी विकसित की हैं जो डेवलपर्स को विभिन्न परिदृश्यों में MCP कार्यान्वित करने में मदद करती हैं:

#### Microsoft Organization  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - ब्राउज़र स्वचालन और परीक्षण के लिए Playwright MCP सर्वर  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - स्थानीय परीक्षण और सामुदायिक योगदान के लिए OneDrive MCP सर्वर कार्यान्वयन  
3. [NLWeb](https://github.com/microsoft/NlWeb) - AI वेब के लिए आधारभूत परत स्थापित करने पर केंद्रित ओपन प्रोटोकॉल और संबंधित ओपन सोर्स टूल्स का संग्रह

#### Azure-Samples Organization  
1. [mcp](https://github.com/Azure-Samples/mcp) - Azure पर MCP सर्वर बनाने और एकीकृत करने के लिए नमूने, टूल्स, और संसाधनों के लिंक  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - Model Context Protocol विनिर्देशन के साथ प्रमाणीकरण दिखाने वाले संदर्भ MCP सर्वर  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure Functions में Remote MCP Server कार्यान्वयन के लिए लैंडिंग पेज  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure Functions के साथ Python में कस्टम Remote MCP सर्वर बनाने और तैनात करने के लिए क्विकस्टार्ट टेम्पलेट  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - .NET/C# के लिए क्विकस्टार्ट टेम्पलेट  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - TypeScript के लिए क्विकस्टार्ट टेम्पलेट  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Python का उपयोग करके Remote MCP सर्वरों के लिए Azure API Management को AI गेटवे के रूप में  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - MCP क्षमताओं सहित APIM ❤️ AI प्रयोग, Azure OpenAI और AI Foundry के साथ एकीकरण

ये रिपॉजिटरी Model Context Protocol के साथ काम करने के लिए विभिन्न कार्यान्वयन, टेम्पलेट्स, और संसाधन प्रदान करती हैं, जो विभिन्न प्रोग्रामिंग भाषाओं और Azure सेवाओं को कवर करती हैं। ये बुनियादी सर्वर कार्यान्वयन से लेकर प्रमाणीकरण, क्लाउड तैनाती, और एंटरप्राइज एकीकरण परिदृश्यों तक के उपयोग मामलों को शामिल करती हैं।

#### MCP Resources Directory

[Microsoft MCP रिपॉजिटरी के MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) में Model
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## अभ्यास

1. किसी एक केस स्टडी का विश्लेषण करें और एक वैकल्पिक कार्यान्वयन दृष्टिकोण प्रस्तावित करें।
2. किसी एक प्रोजेक्ट आइडिया को चुनें और एक विस्तृत तकनीकी विनिर्देशन बनाएं।
3. एक ऐसा उद्योग खोजें जो केस स्टडी में शामिल नहीं है और बताएं कि MCP उसके विशिष्ट चुनौतियों को कैसे हल कर सकता है।
4. भविष्य के किसी एक दिशा की खोज करें और उसे समर्थन देने के लिए एक नया MCP एक्सटेंशन का कॉन्सेप्ट बनाएं।

अगला: [Best Practices](../08-BestPractices/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।