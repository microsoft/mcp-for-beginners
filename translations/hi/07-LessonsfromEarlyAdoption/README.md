# 🌟 शुरुआती अपनाने वालों से सीख

[![Lessons from MCP Early Adopters](../../../translated_images/hi/08.980bb2babbaadd8a.webp)](https://youtu.be/jds7dSmNptE)

_(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

## 🎯 यह मॉड्यूल क्या कवर करता है

यह मॉड्यूल यह जांचता है कि कैसे वास्तविक संगठन और डेवलपर्स मॉडल कंटेक्स्ट प्रोटोकॉल (MCP) का उपयोग असली चुनौतियों को हल करने और नवाचार को बढ़ावा देने के लिए कर रहे हैं। विस्तृत केस स्टडीज़, हैंड्स-ऑन प्रोजेक्ट्स, और व्यावहारिक उदाहरणों के माध्यम से, आप जानेंगे कि MCP कैसे सुरक्षित, स्केलेबल AI इंटीग्रेशन को सक्षम बनाता है जो भाषा मॉडल, टूल्स, और एंटरप्राइज डेटा को जोड़ता है।

### 📚 MCP को क्रियान्वित होते देखें

क्या आप इन सिद्धांतों को प्रोडक्शन-रेडी टूल्स में लागू होते देखना चाहते हैं? हमारे [**10 Microsoft MCP सर्वर्स जो डेवलपर उत्पादकता को बदल रहे हैं**](microsoft-mcp-servers.md) देखें, जो असली Microsoft MCP सर्वर्स प्रदर्शित करता है जिन्हें आप आज ही इस्तेमाल कर सकते हैं।

## अवलोकन

यह पाठ इस बात का अन्वेषण करता है कि शुरुआती अपनाने वालों ने मॉडल कंटेक्स्ट प्रोटोकॉल (MCP) का उपयोग कैसे किया है ताकि वास्तविक दुनिया की चुनौतियों को हल किया जा सके और विभिन्न उद्योगों में नवाचार को बढ़ावा दिया जा सके। विस्तृत केस स्टडीज़ और हैंड्स-ऑन प्रोजेक्ट्स के माध्यम से, आप देखेंगे कि कैसे MCP मानकीकृत, सुरक्षित, और स्केलेबल AI इंटीग्रेशन को संभव बनाता है—जो बड़े भाषा मॉडल, टूल्स, और एंटरप्राइज डेटा को एकीकृत ढांचे में जोड़ता है। आप MCP-आधारित समाधान डिज़ाइन और निर्माण का व्यावहारिक अनुभव प्राप्त करेंगे, सिद्ध कार्यान्वयन पैटर्न से सीखेंगे, और उत्पादन वातावरण में MCP को तैनात करने के लिए सर्वोत्तम प्रथाओं को जानेंगे। यह पाठ उभरती हुई प्रवृत्तियों, भविष्य की दिशाओं और खुले स्रोत संसाधनों को भी उजागर करता है जो आपको MCP प्रौद्योगिकी और इसके विकसित हो रहे पारिस्थितिकी तंत्र के अग्रिम में बने रहने में मदद करेंगे।

## सीखने के उद्देश्य

- विभिन्न उद्योगों में वास्तविक MCP कार्यान्वयनों का विश्लेषण करना
- संपूर्ण MCP-आधारित अनुप्रयोग डिजाइन और निर्माण करना
- MCP प्रौद्योगिकी में उभरती प्रवृत्तियों और भविष्य की दिशाओं का अन्वेषण करना
- वास्तविक विकास परिदृश्यों में सर्वोत्तम प्रथाओं को लागू करना

## वास्तविक wereld MCP कार्यान्वयन

### केस स्टडी 1: एंटरप्राइज ग्राहक सहायता स्वचालन

एक बहुराष्ट्रीय कंपनी ने एक MCP-आधारित समाधान लागू किया ताकि उनके ग्राहक सहायता सिस्टमों के बीच AI इंटरैक्शन को मानकीकृत किया जा सके। इससे वे सक्षम हुए:

- कई LLM प्रदाताओं के लिए एक एकीकृत इंटरफ़ेस बनाना
- विभागों में सुसंगत प्रॉम्प्ट प्रबंधन बनाए रखना
- मजबूत सुरक्षा और अनुपालन नियंत्रण लागू करना
- विशिष्ट आवश्यकताओं के आधार पर विभिन्न AI मॉडलों के बीच आसानी से स्विच करना

**तकनीकी कार्यान्वयन:**

```python
# ग्राहक समर्थन के लिए पायथन MCP सर्वर कार्यान्वयन
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# लॉगिंग कॉन्फ़िगर करें
logging.basicConfig(level=logging.INFO)

async def main():
    # सर्वर कॉन्फ़िगरेशन बनाएँ
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # MCP सर्वर प्रारंभ करें
    server = create_server(config)
    
    # नॉलेज बेस संसाधनों को पंजीकृत करें
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # प्रॉम्प्ट टेम्प्लेट पंजीकृत करें
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # समर्थन उपकरण पंजीकृत करें
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # HTTP ट्रांसपोर्ट के साथ सर्वर शुरू करें
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**परिणाम:** मॉडल लागत में 30% कमी, प्रतिक्रिया स्थिरता में 45% सुधार, और वैश्विक संचालन में बेहतर अनुपालन।

### केस स्टडी 2: स्वास्थ्य देखभाल निदान सहायक

एक स्वास्थ्य सेवा प्रदाता ने कई विशेषज्ञ मेडिकल AI मॉडलों को जोड़ने के लिए MCP आधारभूत संरचना विकसित की जबकि संवेदनशील रोगी डेटा की सुरक्षा सुनिश्चित की:

- सामान्य और विशेषज्ञ चिकित्सा मॉडलों के बीच सहज स्विचिंग
- कड़ाई से गोपनीयता नियंत्रण और ऑडिट ट्रेल्स
- मौजूदा इलेक्ट्रॉनिक हेल्थ रिकॉर्ड (EHR) सिस्टम्स के साथ इंटीग्रेशन
- चिकित्सा पदावली के लिए सुसंगत प्रॉम्प्ट इंजीनियरिंग

**तकनीकी कार्यान्वयन:**

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

**परिणाम:** चिकित्सकों के लिए बेहतर निदान सुझाव, पूर्ण HIPAA अनुपालन बनाए रखते हुए, और सिस्टम्स के बीच संदर्भ-स्विचिंग में उल्लेखनीय कमी।

### केस स्टडी 3: वित्तीय सेवाओं जोखिम विश्लेषण

एक वित्तीय संस्था ने MCP लागू किया ताकि विभिन्न विभागों में उनके जोखिम विश्लेषण प्रक्रियाओं को मानकीकृत किया जा सके:

- क्रेडिट जोखिम, धोखाधड़ी पहचान, और निवेश जोखिम मॉडलों के लिए एकीकृत इंटरफ़ेस बनाया
- कड़े पहुँच नियंत्रण और मॉडल संस्करण नियंत्रण लागू किया
- सभी AI सिफारिशों की ऑडिटेबिलिटी सुनिश्चित की
- विविध प्रणालियों में सुसंगत डेटा प्रारूपण बनाए रखा

**तकनीकी कार्यान्वयन:**

```java
// वित्तीय जोखिम आकलन के लिए जावा MCP सर्वर
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // वित्तीय अनुपालन विशेषताओं के साथ MCP सर्वर बनाएं
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

**परिणाम:** बेहतर नियामक अनुपालन, 40% तेज़ मॉडल तैनाती चक्र, और विभागों में जोखिम आकलन की स्थिरता में सुधार।

### केस स्टडी 4: माइक्रोसॉफ्ट प्लेव्राइट MCP सर्वर ब्राउजर स्वचालन के लिए

माइक्रोसॉफ्ट ने [Playwright MCP सर्वर](https://github.com/microsoft/playwright-mcp) विकसित किया ताकि मॉडल कंटेक्स्ट प्रोटोकॉल के माध्यम से सुरक्षित, मानकीकृत ब्राउजर स्वचालन सक्षम किया जा सके। यह उत्पादन-तैयार सर्वर AI एजेंट्स और LLMs को नियंत्रित, ऑडिटेबल, और विस्तार योग्य तरीके से वेब ब्राउजर के साथ इंटरैक्ट करने की अनुमति देता है - स्वचालित वेब टेस्टिंग, डेटा एक्सट्रैक्शन, और एंड-टू-एंड वर्कफ़्लो जैसी उपयोग केस संभव बनाता है।

> **🎯 उत्पादन-तैयार टूल**
> 
> यह केस स्टडी एक वास्तविक MCP सर्वर प्रदर्शित करती है जिसका उपयोग आप आज कर सकते हैं! Playwright MCP सर्वर और 9 अन्य उत्पादन-तैयार माइक्रोसॉफ्ट MCP सर्वरों के बारे में हमारे [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#8--playwright-mcp-server) में अधिक जानें।

**मुख्य विशेषताएं:**
- ब्राउजर स्वचालन क्षमताओं (नेविगेशन, फॉर्म भरना, स्क्रीनशॉट कैप्चर, आदि) को MCP टूल्स के रूप में प्रकट करता है
- अनधिकृत क्रियाओं को रोकने के लिए कड़े पहुँच नियंत्रण और सैंडबॉक्सिंग लागू करता है
- सभी ब्राउजर इंटरैक्शन के लिए विस्तृत ऑडिट लॉग प्रदान करता है
- एजेंट-चालित स्वचालन के लिए Azure OpenAI और अन्य LLM प्रदाताओं के साथ इंटीग्रेशन का समर्थन करता है
- GitHub Copilot के कोडिंग एजेंट को वेब ब्राउज़िंग क्षमताओं से सक्षम करता है

**तकनीकी कार्यान्वयन:**

```typescript
// TypeScript: MCP सर्वर में Playwright ब्राउज़र ऑटोमेशन टूल्स को रजिस्टर करना
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// URL पर नेविगेट करने और स्क्रीनशॉट कैप्चर करने के लिए टूल रजिस्टर करें
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

// MCP सर्वर शुरू करें
server.listen(8080);
```

**परिणाम:**

- AI एजेंट्स और LLMs के लिए सुरक्षित, प्रोग्रामेटिक ब्राउजर स्वचालन सक्षम किया
- मैनुअल टेस्टिंग प्रयास कम किए और वेब एप्लिकेशन के लिए टेस्ट कवरेज में सुधार किया
- एंटरप्राइज वातावरण में ब्राउजर-आधारित टूल इंटीग्रेशन के लिए पुन: प्रयोज्य, विस्तार योग्य फ्रेमवर्क प्रदान किया
- GitHub Copilot की वेब ब्राउज़िंग क्षमताओं को शक्ति प्रदान की

**संदर्भ:**

- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### केस स्टडी 5: Azure MCP – एंटरप्राइज-ग्रेड मॉडल कंटेक्स्ट प्रोटोकॉल सेवा के रूप में

Azure MCP Server ([https://aka.ms/azmcp](https://aka.ms/azmcp)) माइक्रोसॉफ्ट का एक प्रबंधित, एंटरप्राइज-ग्रेड मॉडल कंटेक्स्ट प्रोटोकॉल कार्यान्वयन है, जिसे स्केलेबल, सुरक्षित, और अनुपालन योग्य MCP सर्वर क्षमताओं को क्लाउड सेवा के रूप में प्रदान करने के लिए डिज़ाइन किया गया है। Azure MCP संगठनों को तेज़ी से MCP सर्वर्स को Azure AI, डेटा, और सुरक्षा सेवाओं के साथ तैनात, प्रबंधित, और एकीकृत करने में सक्षम बनाता है, जिससे संचालन ओवरहेड कम होता है और AI अपनाने में तेजी आती है।

> **🎯 उत्पादन-तैयार टूल**
> 
> यह एक वास्तविक MCP सर्वर है जिसका आप आज उपयोग कर सकते हैं! माइक्रोसॉफ्ट फाउंड्री MCP सर्वर के बारे में अधिक जानें हमारे [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md) में।


- पूर्ण रूप से प्रबंधित MCP सर्वर होस्टिंग जिसमें अंतर्निर्मित स्केलिंग, निगरानी, और सुरक्षा शामिल है
- Azure OpenAI, Azure AI Search, और अन्य Azure सेवाओं के साथ देशी एकीकरण
- Microsoft Entra ID के माध्यम से एंटरप्राइज प्रमाणीकरण और प्राधिकरण
- कस्टम टूल्स, प्रॉम्प्ट टेम्पलेट्स, और संसाधन कनेक्टर्स का समर्थन
- एंटरप्राइज सुरक्षा और नियामक आवश्यकताओं के साथ अनुपालन

**तकनीकी कार्यान्वयन:**

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
- एंटरप्राइज AI परियोजनाओं के लिए तैयार-से-प्रयोग, अनुपालन MCP सर्वर प्लेटफ़ॉर्म प्रदान करके समय-से-मूल्य कम किया
- LLMs, टूल्स, और एंटरप्राइज डेटा स्रोतों के एकीकरण को सरल बनाया
- MCP वर्कलोड के लिए सुरक्षा, अवलोकनशीलता, और संचालन दक्षता में सुधार किया
- Azure SDK सर्वोत्तम प्रथाओं और वर्तमान प्रमाणीकरण पैटर्न के साथ कोड गुणवत्ता में सुधार किया

**संदर्भ:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [Azure MCP Server GitHub Repository](https://github.com/Azure/azure-mcp)
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)
- [Microsoft MCP Center](https://mcp.azure.com)

## केस स्टडी 6: NLWeb 
MCP (मॉडल कंटेक्स्ट प्रोटोकॉल) चैटबॉट्स और AI सहायकों के लिए टूल्स के साथ इंटरैक्ट करने के लिए एक उभरता हुआ प्रोटोकॉल है। हर NLWeb इंस्टेंस भी एक MCP सर्वर है, जो एक मुख्य विधि, ask, का समर्थन करता है, जिसका उपयोग किसी वेबसाइट से प्राकृतिक भाषा में प्रश्न पूछने के लिए किया जाता है। लौटाया गया उत्तर schema.org का उपयोग करता है, जो वेब डेटा का वर्णन करने के लिए व्यापक रूप से उपयोग किया जाने वाला शब्दावली है। आसान शब्दों में कहें, तो MCP NLWeb के समान है जैसे Http HTML के लिए है। NLWeb प्रोटोकॉल, Schema.org प्रारूप, और नमूना कोड को जोड़ता है ताकि साइटें तेजी से ये एंडपॉइंट बना सकें, जिससे संवादात्मक इंटरफेस के माध्यम से मानव और प्राकृतिक एजेंट-से-एजेंट इंटरैक्शन के माध्यम से मशीनों दोनों को लाभ होता है।

NLWeb के दो अलग-अलग घटक हैं।
- एक प्रोटोकॉल, शुरू करने के लिए बहुत सरल, जो साइट के साथ प्राकृतिक भाषा में इंटरफेस करता है और एक प्रारूप, जो लौटाए गए उत्तर के लिए json और schema.org का उपयोग करता है। अधिक विवरण के लिए REST API पर दस्तावेज देखें।
- (1) का एक सरल कार्यान्वयन जो मौजूदा मार्कअप का उपयोग करता है, उन साइटों के लिए जिन्हें वस्तुओं की सूची (उत्पाद, व्यंजन, आकर्षण, समीक्षाएं, आदि) के रूप में अमूर्त किया जा सकता है। उपयोगकर्ता इंटरफ़ेस विजेट्स के साथ, साइटें अपने सामग्री के लिए संवादात्मक इंटरफेस आसानी से प्रदान कर सकती हैं। यह कैसे काम करता है, इसके बारे में अधिक जानने के लिए Life of a chat query पर दस्तावेज देखें।
 
**संदर्भ:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [NLWeb](https://github.com/microsoft/NlWeb)

### केस स्टडी 7: Microsoft Foundry MCP Server – एंटरप्राइज AI एजेंट एकीकरण

Microsoft Foundry MCP सर्वर दिखाते हैं कि MCP का उपयोग एंटरप्राइज वातावरण में AI एजेंट्स और वर्कफ़्लो को संयोजित और प्रबंधित करने के लिए कैसे किया जा सकता है। MCP को Microsoft Foundry के साथ एकीकृत करके, संगठन एजेंट इंटरैक्शन को मानकीकृत कर सकते हैं, Foundry के वर्कफ़्लो प्रबंधन का उपयोग कर सकते हैं, और सुरक्षित, स्केलेबल तैनाती सुनिश्चित कर सकते हैं।

> **🎯 उत्पादन-तैयार टूल**
> 
> यह एक वास्तविक MCP सर्वर है जिसका आप आज उपयोग कर सकते हैं! Microsoft Foundry MCP सर्वर के बारे में अधिक जानने के लिए हमारे [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#9--microsoft-foundry-mcp-server) देखें।

**मुख्य विशेषताएं:**
- Azure के AI पारिस्थितिकी तंत्र तक व्यापक पहुँच, जिसमें मॉडल कैटलॉग और तैनाती प्रबंधन शामिल हैं
- RAG अनुप्रयोगों के लिए Azure AI Search के साथ ज्ञान अनुक्रमण
- AI मॉडल प्रदर्शन और गुणवत्ता आश्वासन के लिए मूल्यांकन उपकरण
- Microsoft Foundry कैटलॉग और लैब्स के साथ एकीकरण अत्याधुनिक अनुसंधान मॉडलों के लिए
- उत्पादन परिदृश्यों के लिए एजेंट प्रबंधन और मूल्यांकन क्षमताएं

**परिणाम:**
- AI एजेंट वर्कफ़्लो के त्वरित प्रोटोटाइपिंग और मजबूत निगरानी
- उन्नत परिदृश्यों के लिए Azure AI सेवाओं के साथ सहज एकीकरण
- एजेंट पाइपलाइनों के निर्माण, तैनाती, और निगरानी के लिए एकीकृत इंटरफेस
- एंटरप्राइज के लिए बेहतर सुरक्षा, अनुपालन, और संचालन दक्षता
- जटिल एजेंट-चालित प्रक्रियाओं पर नियंत्रण बनाए रखते हुए AI अपनाने में तेजी

**संदर्भ:**
- [Microsoft Foundry MCP Server GitHub Repository](https://github.com/azure-ai-foundry/mcp-foundry)
- [Integrating Azure AI Agents with MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

### केस स्टडी 8: Foundry MCP Playground – प्रयोग और प्रोटोटाइपिंग

Foundry MCP Playground एक प्रयोगात्मक उपयोग के लिए तैयार वातावरण प्रदान करता है जहाँ MCP सर्वर्स और Microsoft Foundry इंटीग्रेशन का परीक्षण किया जा सकता है। डेवलपर्स Microsoft Foundry कैटलॉग और लैब्स के संसाधनों का उपयोग करके AI मॉडलों और एजेंट वर्कफ़्लोज का तेजी से प्रोटोटाइप, परीक्षण, और मूल्यांकन कर सकते हैं। प्लेग्राउंड सेटअप को सरल बनाता है, नमूना प्रोजेक्ट प्रदान करता है, और सहयोगी विकास का समर्थन करता है, जिससे न्यूनतम ओवरहेड के साथ सर्वोत्तम प्रथाओं और नए परिदृश्यों का अन्वेषण आसान हो जाता है। यह विशेष रूप से टीमों के लिए उपयोगी है जो विचारों को वैधता प्रदान करना, प्रयोग साझा करना, और जटिल अवसंरचना की आवश्यकता के बिना सीखने को तेज़ करना चाहते हैं। प्रवेश में बाधा कम करके, प्लेग्राउंड MCP और Microsoft Foundry इकोसिस्टम में नवाचार और समुदाय योगदान को बढ़ावा देता है।

**संदर्भ:**

- [Foundry MCP Playground GitHub Repository](https://github.com/azure-ai-foundry/foundry-mcp-playground)

### केस स्टडी 9: Microsoft Learn Docs MCP Server – AI-संचालित दस्तावेज़ीकरण पहुँच

Microsoft Learn Docs MCP Server एक क्लाउड-होस्टेड सेवा है जो मॉडल कंटेक्स्ट प्रोटोकॉल के माध्यम से AI सहायकों को वास्तविक समय में आधिकारिक Microsoft दस्तावेज़ीकरण तक पहुँच प्रदान करती है। यह उत्पादन-तैयार सर्वर व्यापक Microsoft Learn पारिस्थितिकी तंत्र से जुड़ता है और सभी आधिकारिक Microsoft स्रोतों में सैमांटिक खोज सक्षम करता है।

> **🎯 उत्पादन-तैयार टूल**
> 
> यह एक वास्तविक MCP सर्वर है जिसका आप आज उपयोग कर सकते हैं! Microsoft Learn Docs MCP Server के बारे में अधिक जानने के लिए हमारे [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server) देखें।

**मुख्य विशेषताएं:**
- आधिकारिक Microsoft दस्तावेज़, Azure डॉक्युमेंट्स, और Microsoft 365 दस्तावेज़ीकरण के लिए वास्तविक समय पहुँच
- परिष्कृत सैमांटिक खोज क्षमताएं जो संदर्भ और आशय को समझती हैं
- Microsoft Learn सामग्री प्रकाशित होते ही हमेशा अपडेट रहने वाली जानकारी
- Microsoft Learn, Azure दस्तावेज़ीकरण, और Microsoft 365 स्रोतों में व्यापक कवरेज
- लेख शीर्षक और URL के साथ 10 उच्च गुणवत्ता वाले सामग्री खंड तक लौटता है

**यह क्यों महत्वपूर्ण है:**
- Microsoft प्रौद्योगिकियों के लिए "पुरानी AI ज्ञान" समस्या को हल करता है
- AI सहायकों को नवीनतम .NET, C#, Azure, और Microsoft 365 फीचर्स की पहुँच सुनिश्चित करता है
- सटीक कोड जनरेशन के लिए अधिकारिक, प्रथम-पक्ष जानकारी प्रदान करता है
- तेजी से विकसित हो रही Microsoft प्रौद्योगिकियों के साथ काम करने वाले डेवलपर्स के लिए आवश्यक

**परिणाम:**
- Microsoft प्रौद्योगिकियों के लिए AI-जनित कोड की नाटकीय रूप से बेहतर सटीकता
- वर्तमान दस्तावेज़ीकरण और सर्वोत्तम प्रथाओं की खोज में समय में कमी
- संदर्भ-सचेत दस्तावेज़ प्राप्ति के साथ बढ़ी हुई डेवलपर उत्पादकता
- IDE छोड़ें बिना विकास वर्कफ़्लो के साथ सहज एकीकरण

**संदर्भ:**
- [Microsoft Learn Docs MCP Server GitHub Repository](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn Documentation](https://learn.microsoft.com/)

## हैंड्स-ऑन प्रोजेक्ट्स

### प्रोजेक्ट 1: मल्टी-प्रोवाइडर MCP सर्वर बनाएं

**लक्ष्य:** एक MCP सर्वर बनाएँ जो विशिष्ट मानदंडों के आधार पर कई AI मॉडल प्रदाताओं को अनुरोध मार्गदर्शन कर सके।

**आवश्यकताएँ:**

- कम से कम तीन विभिन्न मॉडल प्रदाताओं का समर्थन करें (जैसे, OpenAI, Anthropic, स्थानीय मॉडल)
- अनुरोध मेटाडेटा के आधार पर मार्गदर्शन तंत्र लागू करें
- प्रदाता क्रेडेंशियल प्रबंधन के लिए एक कॉन्फ़िगरेशन सिस्टम बनाएँ
- प्रदर्शन और लागत को अनुकूलित करने के लिए कैशिंग जोड़ें
- उपयोग निगरानी के लिए एक सरल डैशबोर्ड बनाएं

**कार्यान्वयन चरण:**

1. मूल MCP सर्वर अवसंरचना स्थापित करें
2. प्रत्येक AI मॉडल सेवा के लिए प्रदाता एडेप्टर लागू करें
3. अनुरोध गुणों के आधार पर मार्गदर्शन लॉजिक बनाएँ
4. बार-बार अनुरोधों के लिए कैशिंग तंत्र जोड़ें
5. निगरानी डैशबोर्ड विकसित करें
6. विभिन्न अनुरोध पैटर्न के साथ परीक्षण करें

**प्रौद्योगिकियां:** Python (.NET/Java/Python आपकी पसंद के अनुसार), Redis कैशिंग के लिए, और डैशबोर्ड के लिए एक सरल वेब फ्रेमवर्क चुनें।

### प्रोजेक्ट 2: एंटरप्राइज प्रॉम्प्ट प्रबंधन प्रणाली

**लक्ष्य:** एक MCP-आधारित प्रणाली विकसित करें जो संगठन में प्रॉम्प्ट टेम्पलेट्स का प्रबंधन, संस्करण नियंत्रण, और तैनाती करे।

**आवश्यकताएँ:**


- प्रॉम्प्ट टेम्प्लेट्स के लिए एक केंद्रीकृत रिपॉजिटरी बनाएं
- संस्करण नियंत्रण और अनुमोदन वर्कफ़्लो लागू करें
- नमूना इनपुट के साथ टेम्प्लेट परीक्षण क्षमताएं बनाएं
- भूमिका-आधारित पहुँच नियंत्रण विकसित करें
- टेम्प्लेट प्राप्ति और तैनाती के लिए एक API बनाएं

**कार्यान्वयन चरण:**

1. टेम्प्लेट संग्रहण के लिए डेटाबेस स्कीमा डिजाइन करें
2. टेम्प्लेट CRUD ऑपरेशनों के लिए कोर API बनाएं
3. संस्करण नियंत्रण प्रणाली लागू करें
4. अनुमोदन वर्कफ़्लो बनाएं
5. परीक्षण ढांचा विकसित करें
6. प्रबंधन के लिए एक सरल वेब इंटरफेस बनाएं
7. एक MCP सर्वर के साथ एकीकृत करें

**प्रौद्योगिकियां:** आपके पसंदीदा बैकएंड फ्रेमवर्क, SQL या NoSQL डेटाबेस, और प्रबंधन इंटरफेस के लिए एक फ्रंटएंड फ्रेमवर्क।

### परियोजना 3: MCP-आधारित कंटेंट जनरेशन प्लेटफ़ॉर्म

**उद्देश्य:** एक कंटेंट जनरेशन प्लेटफ़ॉर्म बनाएं जो MCP का उपयोग करके विभिन्न कंटेंट प्रकारों में सुसंगत परिणाम प्रदान करे।

**आवश्यकताएं:**

- कई कंटेंट प्रारूपों का समर्थन करें (ब्लॉग पोस्ट, सोशल मीडिया, मार्केटिंग कॉपी)
- कस्टमाइज़ेशन विकल्पों के साथ टेम्प्लेट-आधारित जनरेशन लागू करें
- कंटेंट समीक्षा और प्रतिक्रिया प्रणाली बनाएं
- कंटेंट प्रदर्शन मीट्रिक ट्रैक करें
- कंटेंट संस्करण नियंत्रण और पुनरावृत्ति का समर्थन करें

**कार्यान्वयन चरण:**

1. MCP क्लाइंट इन्फ्रास्ट्रक्चर सेटअप करें
2. विभिन्न कंटेंट प्रकारों के लिए टेम्प्लेट बनाएं
3. कंटेंट जनरेशन पाइपलाइन बनाएं
4. समीक्षा प्रणाली लागू करें
5. मीट्रिक्स ट्रैकिंग सिस्टम विकसित करें
6. टेम्प्लेट प्रबंधन और कंटेंट जनरेशन के लिए यूजर इंटरफेस बनाएं

**प्रौद्योगिकियां:** आपकी पसंदीदा प्रोग्रामिंग भाषा, वेब फ्रेमवर्क, और डेटाबेस सिस्टम।

## MCP प्रौद्योगिकी के लिए भविष्य के दिशानिर्देश

### उभरते रुझान

1. **मल्टी-मोडल MCP**
   - छवि, ऑडियो, और वीडियो मॉडल के साथ इंटरैक्शन को मानकीकृत करने के लिए MCP का विस्तार
   - क्रॉस-मोडल तर्क क्षमताओं का विकास
   - विभिन्न मोडालिटीज़ के लिए मानकीकृत प्रॉम्प्ट फॉर्मेट्स

2. **फेडेरेटेड MCP इन्फ्रास्ट्रक्चर**
   - संगठन के बीच संसाधन साझा करने वाले वितरित MCP नेटवर्क
   - सुरक्षित मॉडल साझाकरण के लिए मानकीकृत प्रोटोकॉल
   - गोपनीयता-संरक्षण कंप्यूटेशन तकनीकें

3. **MCP मार्केटप्लेस**
   - MCP टेम्प्लेट्स और प्लगइन्स साझा करने और मुद्रीकृत करने के लिए इकोसिस्टम
   - गुणवत्ता आश्वासन और प्रमाणन प्रक्रियाएं
   - मॉडल मार्केटप्लेस के साथ एकीकरण

4. **एज कंप्यूटिंग के लिए MCP**
   - संसाधन-संकुचित एज डिवाइसेस के लिए MCP मानकों का अनुकूलन
   - कम बैंडविड्थ पर्यावरण के लिए अनुकूलित प्रोटोकॉल
   - IoT इकोसिस्टम के लिए विशेष MCP कार्यान्वयन

5. **नियामक फ्रेमवर्क**
   - नियामक अनुपालन के लिए MCP एक्सटेंशन्स का विकास
   - मानकीकृत ऑडिट ट्रेल्स और व्याख्यात्मक इंटरफेस
   - उभरते AI शासन फ्रेमवर्क के साथ एकीकरण

### माइक्रोसॉफ्ट से MCP समाधान

माइक्रोसॉफ्ट और अजूर ने विभिन्न परिदृश्यों में MCP को लागू करने के लिए कई ओपन-सोर्स रिपॉजिटरी विकसित की हैं:

#### माइक्रोसॉफ्ट संगठन

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - ब्राउज़र स्वचालन और परीक्षण के लिए Playwright MCP सर्वर
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - स्थानीय परीक्षण और सामुदायिक योगदान के लिए OneDrive MCP सर्वर कार्यान्वयन
3. [NLWeb](https://github.com/microsoft/NlWeb) - ओपन प्रोटोकॉल्स और संबंधित ओपन सोर्स टूल्स का संग्रह, जिसका मुख्य फोकस AI वेब के लिए बुनियादी परत स्थापित करना है

#### Azure-Samples संगठन

1. [mcp](https://github.com/Azure-Samples/mcp) - Azure पर विभिन्न भाषाओं का उपयोग करके MCP सर्वर बनाने और एकीकृत करने के लिए नमूने, टूल्स, और संसाधन
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - वर्तमान मॉडल कंटेक्स्ट प्रोटोकॉल विनिर्देश के साथ प्रमाणीकरण प्रदर्शित करने वाले संदर्भ MCP सर्वर
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure Functions में रिमोट MCP सर्वर कार्यान्वयन के लिए लैंडिंग पेज और भाषा-विशिष्ट रिपॉजिटरी के लिंक
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Python के साथ Azure Functions का उपयोग करके कस्टम रिमोट MCP सर्वर बनाने और तैनात करने के लिए त्वरित प्रारंभ टेम्प्लेट
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - .NET/C# के साथ Azure Functions का उपयोग करके कस्टम रिमोट MCP सर्वर बनाने और तैनात करने के लिए त्वरित प्रारंभ टेम्प्लेट
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - TypeScript के साथ Azure Functions का उपयोग करके कस्टम रिमोट MCP सर्वर बनाने और तैनात करने के लिए त्वरित प्रारंभ टेम्प्लेट
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Python का उपयोग करके रिमोट MCP सर्वरों के लिए Azure API Management को AI गेटवे के रूप में उपयोग करना
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI प्रयोग जिनमें MCP क्षमताएं शामिल हैं, Azure OpenAI और AI Foundry के साथ एकीकरण

ये रिपॉजिटरी विभिन्न प्रोग्रामिंग भाषाओं और Azure सेवाओं में मॉडल कंटेक्स्ट प्रोटोकॉल के साथ काम करने के लिए विभिन्न कार्यान्वयन, टेम्प्लेट और संसाधन प्रदान करती हैं। वे बुनियादी सर्वर कार्यान्वयन से लेकर प्रमाणीकरण, क्लाउड तैनाती, और उद्यम एकीकरण परिदृश्यों तक के उपयोग के मामलों को कवर करती हैं।

#### MCP संसाधन निर्देशिका

आधिकारिक Microsoft MCP रिपॉजिटरी में [MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) मॉडल कंटेक्स्ट प्रोटोकॉल सर्वरों के लिए नमूना संसाधन, प्रॉम्प्ट टेम्प्लेट्स, और टूल परिभाषाओं का एक क्यूरेटेड संग्रह प्रदान करता है। यह निर्देशिका डेवलपर्स को MCP के साथ तेजी से शुरू करने में सहायता करने के लिए पुन: प्रयोज्य बिल्डिंग ब्लॉक्स और सर्वोत्तम प्रथाओं के उदाहरण प्रदान करती है:

- **प्रॉम्प्ट टेम्प्लेट्स:** सामान्य AI कार्यों और परिदृश्यों के लिए तैयार-से-उपयोग प्रॉम्प्ट टेम्प्लेट्स, जिन्हें आप अपने MCP सर्वर कार्यान्वयन के लिए अनुकूलित कर सकते हैं।
- **टूल परिभाषाएं:** विभिन्न MCP सर्वरों में टूल एकीकरण और आह्वान को मानकीकृत करने के लिए उदाहरण टूल स्कीमाओं और मेटाडेटा।
- **संसाधन नमूने:** MCP फ्रेमवर्क के भीतर डेटा स्रोतों, APIs, और बाहरी सेवाओं से कनेक्ट करने के लिए उदाहरण संसाधन परिभाषाएं।
- **संदर्भ कार्यान्वयन:** व्यावहारिक नमूने जो दिखाते हैं कि वास्तविक MCP परियोजनाओं में संसाधन, प्रॉम्प्ट और टूल्स को कैसे संरचित और आयोजित किया जाए।

ये संसाधन विकास को तेज करते हैं, मानकीकरण को बढ़ावा देते हैं, और MCP-आधारित समाधानों के निर्माण और तैनाती के दौरान सर्वोत्तम प्रथाओं को सुनिश्चित करने में मदद करते हैं।

#### MCP संसाधन निर्देशिका

- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)

### अनुसंधान के अवसर

- MCP फ्रेमवर्क में कुशल प्रॉम्प्ट अनुकूलन तकनीकें
- मल्टी-टेनेंट MCP तैनातियों के लिए सुरक्षा मॉडल
- विभिन्न MCP कार्यान्वयन के बीच प्रदर्शन बेंचमार्किंग
- MCP सर्वरों के लिए औपचारिक सत्यापन विधियां

## निष्कर्ष

मॉडल कंटेक्स्ट प्रोटोकॉल (MCP) उद्योगों में मानकीकृत, सुरक्षित, और इंटरऑपरेबल AI एकीकरण के भविष्य को तेज़ी से आकार दे रहा है। इस पाठ में दी गई केस स्टडीज़ और प्रायोगिक परियोजनाओं के माध्यम से, आपने देखा कि प्रारंभिक अपनाने वाले—जिनमें Microsoft और Azure शामिल हैं—MCP का उपयोग वास्तविक दुनिया की समस्याओं को हल करने, AI अपनाने को तेज़ करने, और अनुपालन, सुरक्षा, और स्केलेबिलिटी सुनिश्चित करने के लिए कैसे कर रहे हैं। MCP का मॉड्यूलर दृष्टिकोण संगठनों को बड़े भाषा मॉडल, टूल्स, और एंटरप्राइज़ डेटा को एक एकीकृत, ऑडिटेबल फ्रेमवर्क में जोड़ने में सक्षम बनाता है। जैसे-जैसे MCP विकसित होता रहेगा, समुदाय के साथ जुड़ा रहना, ओपन-सोर्स संसाधनों का अन्वेषण करना, और सर्वोत्तम प्रथाओं को लागू करना मजबूत और भविष्य के लिए तैयार AI समाधानों का निर्माण करने की कुंजी होगी।

## अतिरिक्त संसाधन

- [MCP Foundry GitHub Repository](https://github.com/azure-ai-foundry/mcp-foundry)
- [Foundry MCP Playground](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [Integrating Azure AI Agents with MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - सुरक्षा सर्वोत्तम प्रथाएँ
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

## अभ्यास

1. किसी एक केस स्टडी का विश्लेषण करें और एक वैकल्पिक कार्यान्वयन दृष्टिकोण प्रस्तावित करें।
2. परियोजना विचारों में से किसी एक को चुनें और एक विस्तृत तकनीकी विनिर्देश बनाएं।
3. उस उद्योग पर शोध करें जो केस स्टडीज़ में शामिल नहीं है और यह बताएं कि MCP कैसे उसकी विशिष्ट चुनौतियों का समाधान कर सकता है।
4. भविष्य के दिशानिर्देशों में से किसी एक की खोज करें और इसे समर्थन देने के लिए एक नए MCP एक्सटेंशन की अवधारणा बनाएं।

## आगे क्या

अधिक खोजें: [Microsoft MCP Servers](./microsoft-mcp-servers.md)

जारी रखें: [Module 8: Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->