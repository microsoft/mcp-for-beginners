<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:09:49+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "ne"
}
-->
# Lessons from Early Adopters

## Overview

यो पाठले प्रारम्भिक अपनाउनेहरूले Model Context Protocol (MCP) लाई कसरी वास्तविक चुनौतीहरू समाधान गर्न र उद्योगहरूमा नवप्रवर्तन अघि बढाउन प्रयोग गरेका छन् भन्ने कुरा अन्वेषण गर्छ। विस्तृत केस स्टडीहरू र व्यावहारिक परियोजनाहरू मार्फत, तपाईंले देख्नु हुनेछ कि MCP कसरी मानकीकृत, सुरक्षित, र स्केलेबल AI एकीकरण सक्षम पार्छ—ठूला भाषा मोडेलहरू, उपकरणहरू, र उद्यम डेटा एकीकृत गर्ने एउटै फ्रेमवर्कमा जोड्ने। तपाईंले MCP आधारित समाधानहरू डिजाइन र निर्माण गर्ने व्यावहारिक अनुभव पाउनुहुनेछ, प्रमाणित कार्यान्वयन ढाँचाहरूबाट सिक्नुहुनेछ, र उत्पादन वातावरणमा MCP लागू गर्दा उत्कृष्ट अभ्यासहरू पत्ता लगाउनुहुनेछ। यस पाठले नयाँ ट्रेन्डहरू, भविष्यका दिशाहरू, र खुला स्रोत स्रोतहरूलाई पनि उजागर गर्छ जसले तपाईंलाई MCP प्रविधि र यसको विकासशील इकोसिस्टममा अगाडि राख्न मद्दत गर्नेछ।

## Learning Objectives

- विभिन्न उद्योगहरूमा वास्तविक MCP कार्यान्वयनहरू विश्लेषण गर्ने
- पूर्ण MCP आधारित अनुप्रयोगहरू डिजाइन र निर्माण गर्ने
- MCP प्रविधिमा उदीयमान ट्रेन्डहरू र भविष्यका दिशाहरू अन्वेषण गर्ने
- वास्तविक विकास परिदृश्यहरूमा उत्कृष्ट अभ्यासहरू लागू गर्ने

## Real-world MCP Implementations

### Case Study 1: Enterprise Customer Support Automation

एक बहुराष्ट्रिय कम्पनीले आफ्नो ग्राहक सहायता प्रणालीहरूमा AI अन्तरक्रियालाई मानकीकृत गर्न MCP आधारित समाधान लागू गर्यो। यसले उनीहरूलाई अनुमति दियो:

- विभिन्न LLM प्रदायकहरूको लागि एउटै एकीकृत इन्टरफेस सिर्जना गर्न
- विभागहरूमा निरन्तर प्रॉम्प्ट व्यवस्थापन कायम गर्न
- बलियो सुरक्षा र अनुपालन नियन्त्रणहरू लागू गर्न
- विशिष्ट आवश्यकताहरू अनुसार विभिन्न AI मोडेलहरू बीच सजिलै स्विच गर्न

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

**Results:** मोडेल लागतमा ३०% कटौती, प्रतिक्रिया स्थिरतामा ४५% सुधार, र विश्वव्यापी अपरेशनहरूमा अनुपालनमा वृद्धि।

### Case Study 2: Healthcare Diagnostic Assistant

एक स्वास्थ्य सेवा प्रदायकले धेरै विशेषज्ञ चिकित्सा AI मोडेलहरू एकीकृत गर्न MCP पूर्वाधार विकास गर्यो र संवेदनशील बिरामी डेटा सुरक्षित राख्यो:

- सामान्य र विशेषज्ञ चिकित्सा मोडेलहरू बीच सहज स्विचिंग
- कडा गोपनीयता नियन्त्रण र अडिट ट्रेलहरू
- विद्यमान Electronic Health Record (EHR) प्रणालीहरूसँग एकीकरण
- चिकित्सा शब्दावलीका लागि समान प्रॉम्प्ट इन्जिनियरिङ

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

**Results:** चिकित्सकहरूका लागि सुधारिएको निदान सुझावहरू, पूर्ण HIPAA अनुपालन कायम राख्दै, र प्रणालीहरू बीच सन्दर्भ स्विचिंगमा महत्वपूर्ण कमी।

### Case Study 3: Financial Services Risk Analysis

एक वित्तीय संस्था ले विभिन्न विभागहरूमा जोखिम विश्लेषण प्रक्रियाहरू मानकीकृत गर्न MCP लागू गर्यो:

- क्रेडिट जोखिम, ठगी पहिचान, र लगानी जोखिम मोडेलहरूको लागि एउटै इन्टरफेस सिर्जना गर्यो
- कडा पहुँच नियन्त्रण र मोडेल संस्करण व्यवस्थापन लागू गर्यो
- सबै AI सिफारिसहरूको अडिटयोग्यता सुनिश्चित गर्यो
- विभिन्न प्रणालीहरूमा डेटा स्वरूपणमा निरन्तरता कायम गर्यो

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

**Results:** नियामक अनुपालनमा सुधार, मोडेल परिनियोजन चक्रहरू ४०% छिटो, र विभागहरूमा जोखिम मूल्यांकन स्थिरता बढ्यो।

### Case Study 4: Microsoft Playwright MCP Server for Browser Automation

Microsoft ले Model Context Protocol मार्फत सुरक्षित, मानकीकृत ब्राउजर स्वचालन सक्षम गर्न [Playwright MCP server](https://github.com/microsoft/playwright-mcp) विकास गर्यो। यस समाधानले AI एजेन्टहरू र LLMs लाई वेब ब्राउजरहरूसँग नियन्त्रणयोग्य, अडिटयोग्य, र विस्तारयोग्य तरिकाले अन्तरक्रिया गर्न सक्षम बनाउँछ—जस्तै स्वचालित वेब परीक्षण, डेटा निष्कर्षण, र अन्त-देखि-अन्त कार्यप्रवाहहरू।

- ब्राउजर स्वचालन क्षमताहरू (नेभिगेसन, फर्म भर्ने, स्क्रिनसट क्याप्चर आदि) लाई MCP उपकरणको रूपमा उपलब्ध गराउँछ
- अवैध कार्यहरू रोक्न कडा पहुँच नियन्त्रण र स्यान्डबक्सिङ लागू गर्छ
- सबै ब्राउजर अन्तरक्रियाहरूका लागि विस्तृत अडिट लगहरू प्रदान गर्छ
- एजेन्ट-चालित स्वचालनका लागि Azure OpenAI र अन्य LLM प्रदायकहरूसँग एकीकरण समर्थन गर्छ

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

**Results:**  
- AI एजेन्टहरू र LLMs का लागि सुरक्षित, प्रोग्राम्याटिक ब्राउजर स्वचालन सक्षम गर्यो  
- म्यानुअल परीक्षण प्रयास घटायो र वेब अनुप्रयोगहरूको परीक्षण कवरेज सुधार गर्यो  
- उद्यम वातावरणहरूमा ब्राउजर-आधारित उपकरण एकीकरणका लागि पुन: प्रयोगयोग्य र विस्तारयोग्य फ्रेमवर्क प्रदान गर्यो  

**References:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### Case Study 5: Azure MCP – Enterprise-Grade Model Context Protocol as a Service

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) Microsoft को व्यवस्थापित, उद्यम-स्तरीय Model Context Protocol कार्यान्वयन हो, जसले स्केलेबल, सुरक्षित, र अनुपालक MCP सर्भर क्षमताहरू क्लाउड सेवाको रूपमा प्रदान गर्दछ। Azure MCP ले संगठनहरूलाई छिटो MCP सर्भरहरू परिनियोजन, व्यवस्थापन, र Azure AI, डेटा, र सुरक्षा सेवाहरू सँग एकीकृत गर्न सक्षम बनाउँछ, जसले सञ्चालन खर्च कम गर्छ र AI अपनत्वलाई तीव्र बनाउँछ।

- पूर्ण रूपमा व्यवस्थापित MCP सर्भर होस्टिंग जसमा स्केलिङ, अनुगमन, र सुरक्षा समावेश छ  
- Azure OpenAI, Azure AI Search, र अन्य Azure सेवाहरूसँग नेटिभ एकीकरण  
- Microsoft Entra ID मार्फत उद्यम प्रमाणीकरण र अधिकृतकरण  
- कस्टम उपकरणहरू, प्रॉम्प्ट टेम्प्लेटहरू, र स्रोत कनेक्टरहरूको समर्थन  
- उद्यम सुरक्षा र नियामक आवश्यकताहरूको अनुपालन  

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

**Results:**  
- उद्यम AI परियोजनाहरूको लागि समय-देखि-मूल्य घटायो, तयार प्रयोगयोग्य, अनुपालक MCP सर्भर प्लेटफर्म प्रदान गरेर  
- LLMs, उपकरणहरू, र उद्यम डेटा स्रोतहरूको एकीकरण सजिलो बनायो  
- MCP कार्यभारहरूको लागि सुरक्षा, अवलोकनयोग्यता, र सञ्चालन दक्षता बढायो  

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## Case Study 6: NLWeb  
MCP (Model Context Protocol) च्याटबोटहरू र AI सहायकहरूले उपकरणहरूसँग अन्तरक्रिया गर्न emerging protocol हो। प्रत्येक NLWeb इन्स्टेन्स पनि MCP सर्भर हो, जसले एउटा मुख्य विधि, ask, समर्थन गर्छ जुन वेबसाइटलाई प्राकृतिक भाषामा प्रश्न सोध्न प्रयोग गरिन्छ। फर्काइएको प्रतिक्रिया schema.org प्रयोग गर्छ, जुन वेब डेटा वर्णन गर्न व्यापक रूपमा प्रयोग हुने शब्दावली हो। साधारण रूपमा भन्नुपर्दा, MCP भनेको NLWeb हो जस्तो HTTP हो HTML को लागि। NLWeb ले प्रोटोकलहरू, Schema.org ढाँचाहरू, र नमूना कोडहरूलाई संयोजन गरेर साइटहरूलाई छिटो यी अन्त बिन्दुहरू सिर्जना गर्न मद्दत गर्दछ, जसले मानिसहरूलाई संवादात्मक इन्टरफेसमार्फत र मेसिनहरूलाई प्राकृतिक एजेन्ट-टु-एजेन्ट अन्तरक्रियाबाट लाभान्वित बनाउँछ।

NLWeb का दुई फरक कम्पोनेन्टहरू छन्।  
- एउटा प्रोटोकल, सुरुमा धेरै सरल, जसले साइटसँग प्राकृतिक भाषामा अन्तरक्रिया गर्न र फर्काइएको उत्तरको लागि json र schema.org ढाँचा प्रयोग गर्छ। REST API सम्बन्धी दस्तावेज हेर्नुहोस्।  
- (१) को सरल कार्यान्वयन जसले विद्यमान मार्कअपलाई प्रयोग गर्छ, ती साइटहरूको लागि जुन वस्तुहरूको सूची (उत्पादनहरू, विधिहरू, आकर्षणहरू, समीक्षा आदि) को रूपमा सारांशित गर्न सकिन्छ। प्रयोगकर्ता इन्टरफेस विजेटहरूको सेटसँगै, साइटहरूले सजिलै आफ्नो सामग्रीमा संवादात्मक इन्टरफेसहरू प्रदान गर्न सक्छन्। यो कसरी काम गर्छ भन्ने थप विवरणका लागि Life of a chat query दस्तावेज हेर्नुहोस्।  

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## Hands-on Projects

### Project 1: Build a Multi-Provider MCP Server

**Objective:** विशेष मापदण्डहरूमा आधारित अनुरोधहरूलाई विभिन्न AI मोडेल प्रदायकहरूमा राउट गर्न सक्ने MCP सर्भर सिर्जना गर्ने।

**Requirements:**  
- कम्तीमा तीन फरक मोडेल प्रदायकहरू समर्थन गर्ने (जस्तै OpenAI, Anthropic, स्थानीय मोडेलहरू)  
- अनुरोध मेटाडाटा आधारमा राउटिङ मेकानिज्म लागू गर्ने  
- प्रदायक प्रमाणपत्रहरू व्यवस्थापन गर्न कन्फिगरेसन प्रणाली सिर्जना गर्ने  
- प्रदर्शन र लागत अनुकूलन गर्न क्यासिङ थप्ने  
- प्रयोग अनुगमनका लागि सरल ड्यासबोर्ड निर्माण गर्ने  

**Implementation Steps:**  
1. आधारभूत MCP सर्भर पूर्वाधार सेटअप गर्ने  
2. प्रत्येक AI मोडेल सेवाको लागि प्रदायक एडाप्टरहरू लागू गर्ने  
3. अनुरोध विशेषताहरूमा आधारित राउटिङ तर्क सिर्जना गर्ने  
4. बारम्बार आउने अनुरोधहरूको लागि क्यासिङ मेकानिज्म थप्ने  
5. अनुगमन ड्यासबोर्ड विकास गर्ने  
6. विभिन्न अनुरोध ढाँचाहरूको साथ परीक्षण गर्ने  

**Technologies:** तपाईंको रोजाइ अनुसार Python (.NET/Java/Python), Redis क्यासिङका लागि, र ड्यासबोर्डका लागि सरल वेब फ्रेमवर्क।

### Project 2: Enterprise Prompt Management System

**Objective:** संगठनभरि प्रॉम्प्ट टेम्प्लेटहरूको व्यवस्थापन, संस्करण नियन्त्रण, र परिनियोजनका लागि MCP आधारित प्रणाली विकास गर्ने।

**Requirements:**  
- प्रॉम्प्ट टेम्प्लेटहरूको लागि केन्द्रीय रिपोजिटरी सिर्जना गर्ने  
- संस्करण नियन्त्रण र अनुमोदन कार्यप्रवाह लागू गर्ने  
- नमूना इनपुटहरूसँग टेम्प्लेट परीक्षण क्षमता विकास गर्ने  
- भूमिका आधारित पहुँच नियन्त्रणहरू विकास गर्ने  
- टेम्प्लेट पुनःप्राप्ति र परिनियोजनका लागि API सिर्जना गर्ने  

**Implementation Steps:**  
1. टेम्प्लेट भण्डारणका लागि डाटाबेस स्किमा डिजाइन गर्ने  
2. टेम्प्लेट CRUD अपरेसनहरूको लागि मुख्य API सिर्जना गर्ने  
3. संस्करण नियन्त्रण प्रणाली लागू गर्ने  
4. अनुमोदन कार्यप्रवाह निर्माण गर्ने  
5. परीक्षण फ्रेमवर्क विकास गर्ने  
6. व्यवस्थापनका लागि सरल वेब इन्टरफेस सिर्जना गर्ने  
7. MCP सर्भरसँग एकीकरण गर्ने  

**Technologies:** तपाईंको रोजाइको ब्याकएन्ड फ्रेमवर्क, SQL वा NoSQL डाटाबेस, र व्यवस्थापन इन्टरफेसका लागि फ्रन्टएन्ड फ्रेमवर्क।

### Project 3: MCP-Based Content Generation Platform

**Objective:** विभिन्न सामग्री प्रकारहरूमा समान परिणाम दिन MCP प्रयोग गरेर सामग्री उत्पादन प्लेटफर्म बनाउने।

**Requirements:**  
- बहु सामग्री ढाँचाहरू समर्थन गर्ने (ब्लग पोस्ट, सामाजिक मिडिया, मार्केटिङ कपी)  
- अनुकूलन विकल्पहरूसँग टेम्प्लेट-आधारित उत्पादन लागू गर्ने  
- सामग्री समीक्षा र प्रतिक्रिया प्रणाली सिर्जना गर्ने  
- सामग्री प्रदर्शन मेट्रिक्स ट्र्याक गर्ने  
- सामग्री संस्करण र पुनरावृत्ति समर्थन गर्ने  

**Implementation Steps:**  
1. MCP क्लाइन्ट पूर्वाधार सेटअप गर्ने  
2. विभिन्न सामग्री प्रकारका लागि टेम्प्लेटहरू सिर्जना गर्ने  
3. सामग्री उत्पादन पाइपलाइन निर्माण गर्ने  
4. समीक्षा प्रणाली लागू गर्ने  
5. मेट्रिक्स ट्र्याकिङ प्रणाली विकास गर्ने  
6. टेम्प्लेट व्यवस्थापन र सामग्री उत्पादनका लागि प्रयोगकर्ता इन्टरफेस सिर्जना गर्ने  

**Technologies:** तपाईंको मनपर्ने प्रोग्रामिङ भाषा, वेब फ्रेमवर्क, र डाटाबेस प्रणाली।

## Future Directions for MCP Technology

### Emerging Trends

1. **Multi-Modal MCP**  
   - छवि, अडियो, र भिडियो मोडेलहरूसँग अन्तरक्रियालाई मानकीकृत गर्न MCP को विस्तार  
   - क्रस-मोडल reasoning क्षमता विकास  
   - विभिन्न मोडालिटीहरूको लागि मानकीकृत प्रॉम्प्ट ढाँचाहरू  

2. **Federated MCP Infrastructure**  
   - संगठनहरूबीच स्रोतहरू साझा गर्न सक्ने वितरित MCP नेटवर्कहरू  
   - सुरक्षित मोडेल साझेदारीका लागि मानकीकृत प्रोटोकलहरू  
   - गोपनीयता-संरक्षण गणना प्रविधिहरू  

3. **MCP Marketplaces**  
   - MCP टेम्प्लेटहरू र प्लगइनहरू साझेदारी र मुद्रीकरण गर्ने पारिस्थितिकी तन्त्रहरू  
   - गुणस्तर सुनिश्चितता र प्रमाणपत्र प्रक्रियाहरू  
   - मोडेल बजारहरूसँग एकीकरण  

4. **MCP for Edge Computing**  
   - स्रोत सीमित एज डिभाइसहरूको लागि MCP मानकहरू अनुकूलन  
   - कम ब्यान्डविथ वातावरणका लागि अनुकूलित प्रोटोकलहरू  
   - IoT पारिस्थितिकी तन्त्रहरूको लागि विशेष MCP कार्यान्वयनहरू  

5. **Regulatory Frameworks**  
   - नियामक अनुपालनका लागि MCP विस्तार विकास  
   - मानकीकृत अडिट ट्रेलहरू र व्याख्यात्मक इन्टरफेसहरू  
   - उदयमान AI शासन फ्रेमवर्कहरूसँग एकीकरण  

### MCP Solutions from Microsoft

Microsoft र Azure ले विभिन्न परिदृश्यहरूमा MCP कार्यान्वयन गर्न सहयोग गर्ने खुला स्रोत रिपोजिटरीहरू विकास गरेका छन्:

#### Microsoft Organization  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - ब्राउजर स्वचालन र परीक्षणका लागि Playwright MCP सर्भर  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - स्थानीय परीक्षण र समुदाय योगदानका लागि OneDrive MCP सर्भर कार्यान्वयन  
3. [NLWeb](https://github.com/microsoft/NlWeb) - खुला प्रोटोकल र सम्बन्धित खुला स्रोत उपकरणहरूको संग्रह, मुख्य रूपमा AI वेबको आधार तयार गर्ने  

#### Azure-Samples Organization  
1. [mcp](https://github.com/Azure-Samples/mcp) - Azure मा MCP सर्भरहरू निर्माण र एकीकृत गर्न नमूना, उपकरणहरू, र स्रोतहरू  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - हालको Model Context Protocol विशिष्टतासँग प्रमाणीकरण देखाउने सन्दर्भ MCP सर्भरहरू  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure Functions मा Remote MCP सर्भर कार्यान्वयनहरूको ल्यान्डिङ पृष्ठ र भाषागत रिपोजिटरी लिंकहरू  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure Functions र Python प्रयोग गरी कस्टम Remote MCP सर्भरहरू निर्माण र परिनियोजनको लागि क्विकस्टार्ट टेम्प्लेट  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - .NET/C# मा Azure Functions प्रयोग गरी कस्टम Remote MCP सर्भरहरू निर्माण र परिनियोजनको लागि क्विकस्टार्ट टेम्प्लेट  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - TypeScript मा Azure Functions प्रयोग गरी कस्टम Remote MCP सर्भरहरू निर्माण र परिनियोजनको लागि क्विकस्टार्ट टेम्प्लेट  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Python प्रयोग गरी Azure API Management लाई Remote MCP सर्भरहरूको लागि AI गेटवेको रूपमा  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI प्रयोगहरू जसमा MCP क्षमता समावेश छ, Azure OpenAI र AI Foundry सँग एकीकरण  

यी रिपोजिटरीहरूले विभिन्न प्रोग्रामिङ भाषाहरू र Azure सेवाहरूमा Model Context Protocol सँग काम गर्न विभिन्न कार्यान्वयनहरू, टेम्प्लेटहरू, र स्रोतहरू प्रदान गर्दछन्। यीले आधारभूत सर्भर कार्यान्वयनदेखि प्रमाणीकरण, क्लाउड परिनियोजन, र उद्यम एकीकरण परिदृश्यहरू सम्मका प्रयोग केसहरू समेट्छन्।

#### MCP Resources Directory

[Microsoft को आधिकारिक MCP रिपोजिटरीमा रहेको MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) ले Model Context Protocol सर्भरहरूसँग प्रयोग गर्नका लागि नमूना स्रोतहरू, प्रॉम्प्ट टेम्प्लेटहरू, र उपकरण परिभाषाहरूको छनोट संग्रह प्रदान गर्छ। यो डाइरेक्टरीले विकासकर्ताहरूलाई पुन: प्रयोगयोग्य निर्माण ब्लकहरू र उत्कृष्ट अभ्यासका उदाहरणहरू उपलब्ध गराएर MCP सँग छिटो काम सुरु गर्न मद्दत गर्दछ:

- **Prompt Templates:** सामान्य AI कार्य र परिदृश्यहरूको लागि तयार प्रयोगयोग्य प्रॉम्प्ट टेम्प्लेटहरू, जुन तपाईंको आफ्नै MCP सर्भर कार्यान्वयनहरूमा अनुकूलन गर्न सकिन्छ।  
- **Tool Definitions:** उपकरण एक
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## अभ्यासहरू

1. एउटा केस स्टडी विश्लेषण गर्नुहोस् र वैकल्पिक कार्यान्वयन विधि प्रस्ताव गर्नुहोस्।
2. एउटा परियोजना विचार रोज्नुहोस् र विस्तृत प्राविधिक विशिष्टता तयार गर्नुहोस्।
3. केस स्टडीहरूमा समेटिएको छैन भनेको कुनै उद्योगको अनुसन्धान गर्नुहोस् र MCP ले त्यसका विशिष्ट चुनौतीहरू कसरी समाधान गर्न सक्छ भन्ने रूपरेखा तयार गर्नुहोस्।
4. भविष्यका दिशाहरू मध्ये एउटा अन्वेषण गर्नुहोस् र त्यसलाई समर्थन गर्न नयाँ MCP विस्तारको अवधारणा बनाउनुहोस्।

अर्को: [Best Practices](../08-BestPractices/README.md)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।