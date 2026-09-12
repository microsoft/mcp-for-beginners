# 🌟 প্রাথমিক গ্রহণকারীদের থেকে পাঠ

[![MCP প্রাথমিক গ্রহণকারীদের থেকে পাঠ](../../../translated_images/bn/08.980bb2babbaadd8a.webp)](https://youtu.be/jds7dSmNptE)

_(এই পাঠের ভিডিও দেখতে উপরের ইমেজে ক্লিক করুন)_

## 🎯 এই মডিউল কী কিছু অন্তর্ভুক্ত করে

এই মডিউলটি কীভাবে বাস্তব সংগঠন এবং ডেভেলপাররা Model Context Protocol (MCP) ব্যবহার করে প্রকৃত চ্যালেঞ্জ সমাধান করছে এবং উদ্ভাবন চালিয়ে নিচ্ছে তা অনুসন্ধান করে। বিস্তারিত কেস স্টাডি, হাতে কলমে প্রকল্প এবং বাস্তব উদাহরণের মাধ্যমে আপনি আবিষ্কার করবেন কীভাবে MCP নিরাপদ, স্কেলযোগ্য AI ইন্টিগ্রেশন সক্ষম করে যা ভাষার মডেল, সরঞ্জাম এবং এন্টারপ্রাইজ ডেটাকে সংযুক্ত করে।

### 📚 MCP কে কার্যকরভাবে দেখুন

আপনি কি এই নীতিগুলো প্রোডাকশন-রেডি টুলে প্রয়োগ দেখতে চান? আমাদের [**10টি Microsoft MCP সার্ভার যা ডেভেলপার উৎপাদনশীলতা রূপান্তরিত করছে**](microsoft-mcp-servers.md) দেখুন, যেখানে আপনি আজই ব্যবহার করতে পারবেন এমন বাস্তব Microsoft MCP সার্ভারগুলি প্রদর্শিত হয়েছে।

## ওভারভিউ

এই পাঠটি খতিয়ে দেখে কীভাবে প্রাথমিক গ্রহণকারীরা Model Context Protocol (MCP) ব্যবহার করে বাস্তব বিশ্ব সমস্যার সমাধান এবং শিল্পজুড়ে উদ্ভাবন চালিয়েছে। বিস্তারিত কেস স্টাডি এবং হাতে কলমে প্রকল্পের মাধ্যমে আপনি দেখতে পাবেন কীভাবে MCP স্ট্যান্ডার্ড, নিরাপদ এবং স্কেলযোগ্য AI ইন্টিগ্রেশন সক্ষম করে — যা বড় ভাষার মডেল, সরঞ্জাম, এবং এন্টারপ্রাইজ ডেটাকে একটি একক কাঠামোতে সংযুক্ত করে। আপনি MCP-ভিত্তিক সমাধান ডিজাইন এবং নির্মাণের ব্যবহারিক অভিজ্ঞতা অর্জন করবেন, প্রমাণিত বাস্তবায়ন প্যাটার্ন থেকে শিখবেন, এবং MCP প্রোডাকশন পরিবেশে মোতায়েনের জন্য সেরা অনুশীলন আবিষ্কার করবেন। এই পাঠটি উদীয়মান প্রবণতা, ভবিষ্যৎ দিকনির্দেশ এবং ওপেন-সোর্স সম্পদগুলোকেও হাইলাইট করে যা আপনাকে MCP প্রযুক্তি এবং এর বিবর্তমান ইকোসিস্টেমের শীর্ষে থাকতে সাহায্য করবে।

## শেখার উদ্দেশ্য

- বিভিন্ন শিল্পে বাস্তব MCP বাস্তবায়ন বিশ্লেষণ করা
- সম্পূর্ণ MCP-ভিত্তিক অ্যাপ্লিকেশন ডিজাইন ও নির্মাণ করা
- MCP প্রযুক্তির উদীয়মান প্রবণতা ও ভবিষ্যৎ দিকনির্দেশ অনুসন্ধান করা
- প্রকৃত উন্নয়ন পরিস্থিতিতে সেরা অনুশীলন প্রয়োগ করা

## বাস্তব MCP বাস্তবায়ন

### কেস স্টাডি ১: এন্টারপ্রাইজ কাস্টমার সাপোর্ট অটোমেশন

একটি বহুজাতিক প্রতিষ্ঠান তাদের গ্রাহক সাপোর্ট সিস্টেম জুড়ে AI ইন্টারঅ্যাকশন স্ট্যান্ডার্ডাইজ করার জন্য MCP-ভিত্তিক সমাধান বাস্তবায়ন করেছে। এর ফলে তারা সক্ষম হয়েছে:

- একাধিক LLM প্রদানকারীর জন্য একটি একক ইন্টারফেস তৈরি করতে
- বিভাগগুলোর মধ্যে ধারাবাহিক প্রম্পট ব্যবস্থাপনা বজায় রাখতে
- শক্তিশালী নিরাপত্তা ও সম্মতি নিয়ন্ত্রণ প্রয়োগ করতে
- নির্দিষ্ট প্রয়োজন অনুযায়ী বিভিন্ন AI মডেলের মধ্যে সহজে পরিবর্তন করতে

**প্রযুক্তিগত বাস্তবায়ন:**

```python
# গ্রাহক সমর্থনের জন্য পাইথন এমসিপি সার্ভার বাস্তবায়ন
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# লগিং কনফিগার করুন
logging.basicConfig(level=logging.INFO)

async def main():
    # সার্ভার কনফিগারেশন তৈরি করুন
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # এমসিপি সার্ভার প্রাথমিকরণ করুন
    server = create_server(config)
    
    # জ্ঞানভিত্তিক সম্পদ নিবন্ধন করুন
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # প্রম্পট টেমপ্লেট নিবন্ধন করুন
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # সমর্থন সরঞ্জাম নিবন্ধন করুন
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # HTTP পরিবহনের সাথে সার্ভার শুরু করুন
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**ফলাফল:** মডেল ব্যয়ের ৩০% হ্রাস, প্রতিক্রিয়ার ধারাবাহিকতায় ৪৫% উন্নতি, এবং বিশ্বব্যাপী অপারেশন জুড়ে বাড়ানো সম্মতি।

### কেস স্টাডি ২: স্বাস্থ্যসেবা ডায়াগনস্টিক সহকারী

একটি স্বাস্থ্যসেবা প্রদানকারী MCP অবকাঠামো তৈরি করেছে যা একাধিক বিশেষায়িত মেডিক্যাল AI মডেল সংহত করে, একই সাথে সংবেদনশীল রোগীর ডেটা সুরক্ষিত রাখে:

- সাধারণ ও বিশেষজ্ঞ মেডিক্যাল মডেলের মধ্যে সিলসিলা-মুক্ত পরিবর্তন
- কঠোর গোপনীয়তা নিয়ন্ত্রণ এবং নিরীক্ষা ট্রেইলস
- বিদ্যমান ইলেকট্রনিক হেল্থ রেকর্ড (EHR) সিস্টেমের সাথে ইন্টিগ্রেশন
- মেডিক্যাল টার্মিনোলজির জন্য ধারাবাহিক প্রম্পট ইঞ্জিনিয়ারিং

**প্রযুক্তিগত বাস্তবায়ন:**

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

**ফলাফল:** চিকিৎসকদের জন্য ডায়াগনস্টিক পরামর্শ উন্নত করা হয়েছে, সম্পূর্ণ HIPAA সম্মতি বজায় রেখে এবং সিস্টেমের মধ্যে প্রেক্ষাপট-পরিবর্তনের উল্লেখযোগ্য হ্রাস ঘটিয়েছে।

### কেস স্টাডি ৩: আর্থিক সেবা ঝুঁকি বিশ্লেষণ

একটি আর্থিক প্রতিষ্ঠান তাদের ঝুঁকি বিশ্লেষণ প্রক্রিয়াগুলো MCP দিয়ে স্ট্যান্ডার্ডাইজ করেছে বিভিন্ন বিভাগ জুড়ে:

- ক্রেডিট ঝুঁকি, প্রতারণা সনাক্তকরণ এবং বিনিয়োগ ঝুঁকি মডেলের জন্য একটি একক ইন্টারফেস তৈরি করা
- কঠোর প্রবেশাধিকার নিয়ন্ত্রণ এবং মডেল সংস্করণিং বাস্তবায়ন
- সব AI সুপারিশের নিরীক্ষণযোগ্যতা নিশ্চিত করা
- বিভিন্ন সিস্টেম জুড়ে ধারাবাহিক ডেটা ফরম্যাট বজায় রাখা

**প্রযুক্তিগত বাস্তবায়ন:**

```java
// আর্থিক ঝুঁকি মূল্যায়নের জন্য জাভা MCP সার্ভার
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // আর্থিক সম্মতি বৈশিষ্ট্য সহ MCP সার্ভার তৈরি করুন
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

**ফলাফল:** উন্নত নিয়ন্ত্রণ সম্মতি, মডেল মোতায়েন চক্র ৪০% দ্রুততর, এবং বিভাগ জুড়ে ঝুঁকি মূল্যায়নের ধারাবাহিকতা উন্নত।

### কেস স্টাডি ৪: Microsoft Playwright MCP সার্ভার ব্রাউজার অটোমেশনের জন্য

Microsoft [Playwright MCP সার্ভার](https://github.com/microsoft/playwright-mcp) তৈরি করেছে যা Model Context Protocol এর মাধ্যমে নিরাপদ, স্ট্যান্ডার্ডাইজড ব্রাউজার অটোমেশন সক্ষম করে। এই প্রোডাকশন-রেডি সার্ভার AI এজেন্ট এবং LLM কে নিয়ন্ত্রিত, নিরীক্ষণযোগ্য ও সম্প্রসারিত উপায়ে ওয়েব ব্রাউজারের সঙ্গে ইন্টারঅ্যাক্ট করার সুযোগ দেয় — যা স্বয়ংক্রিয় ওয়েব টেস্টিং, ডেটা নিষ্কাশন এবং সম্পূর্ণ ওয়ার্কফ্লোর মত ব্যবহারের ক্ষেত্রে সক্ষম করে।

> **🎯 প্রোডাকশন-রেডি টুল**
> 
> এই কেস স্টাডিটি একটি বাস্তব MCP সার্ভার প্রদর্শন করে যা আপনি আজই ব্যবহার করতে পারেন! আরও জানুন Playwright MCP সার্ভার এবং অন্যান্য ৯টি প্রোডাকশন-রেডি Microsoft MCP সার্ভার সম্পর্কে আমাদের [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#8--playwright-mcp-server) এ।

**মূল বৈশিষ্ট্যসমূহ:**
- MCP সরঞ্জাম হিসেবে ব্রাউজার অটোমেশন সক্ষমতা (নেভিগেশন, ফর্ম পূরণ, স্ক্রীনশট ক্যাপচার ইত্যাদি) প্রকাশ করে
- অননুমোদিত ক্রিয়া প্রতিরোধ করার জন্য কঠোর প্রবেশাধিকার নিয়ন্ত্রণ এবং স্যান্ডবক্সিং প্রয়োগ করে
- সমস্ত ব্রাউজার ইন্টারঅ্যাকশনের জন্য বিস্তারিত নিরীক্ষা লগ প্রদান করে
- এজেন্ট-চালিত অটোমেশনের জন্য Azure OpenAI এবং অন্যান্য LLM প্রদানকারীদের সাথে ইন্টিগ্রেশন সমর্থন করে
- GitHub Copilot এর কোডিং এজেন্টকে ওয়েব ব্রাউজিং সক্ষমতা প্রদান করে

**প্রযুক্তিগত বাস্তবায়ন:**

```typescript
// টাইপস্ক্রিপ্ট: একটি MCP সার্ভারে প্লেওরাইট ব্রাউজার অটোমেশন টুল রেজিস্টার করা হচ্ছে
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// একটি URL এ নেভিগেট করার এবং স্ক্রিনশট ক্যাপচার করার জন্য একটি টুল রেজিস্টার করুন
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

// MCP সার্ভার শুরু করুন
server.listen(8080);
```

**ফলাফল:**

- AI এজেন্ট ও LLM এর জন্য নিরাপদ, প্রোগ্রাম্যাটিক ব্রাউজার অটোমেশন সক্ষম করেছে
- ম্যানুয়াল টেস্টিং প্রচেষ্টা কমিয়েছে এবং ওয়েব অ্যাপ্লিকেশনগুলোর জন্য টেস্ট কভারেজ উন্নত করেছে
- এন্টারপ্রাইজ পরিবেশে ব্রাউজার-ভিত্তিক টুল ইন্টিগ্রেশনের জন্য পুনরায় ব্যবহারের যোগ্য, সম্প্রসারযোগ্য ফ্রেমওয়ার্ক প্রদান করেছে
- GitHub Copilot এর ওয়েব ব্রাউজিং সক্ষমতা চালায়

**রেফারেন্স:**

- [Playwright MCP সার্ভার GitHub রিপোজিটরি](https://github.com/microsoft/playwright-mcp)
- [Microsoft AI এবং অটোমেশন সলিউশনস](https://azure.microsoft.com/en-us/products/ai-services/)

### কেস স্টাডি ৫: Azure MCP – এন্টারপ্রাইজ-গ্রেড Model Context Protocol সার্ভার হিসেবে

Azure MCP সার্ভার ([https://aka.ms/azmcp](https://aka.ms/azmcp)) হলো Microsoft এর পরিচালিত, এন্টারপ্রাইজ-গ্রেড Model Context Protocol বাস্তবায়ন, যা MCP সার্ভার সক্ষমতাগুলো স্কেলযোগ্য, নিরাপদ ও সম্মতিসম্পন্ন ক্লাউড সেবায় প্রদান করে। Azure MCP সংগঠনগুলোকে দ্রুত MCP সার্ভার মোতায়েন, পরিচালনা এবং Azure AI, ডেটা ও সিকিউরিটি সার্ভিসের সাথে সংযুক্ত করার সুযোগ দেয়, যা অপারেশনাল ওভারহেড কমায় এবং AI গ্রহণ দ্রুততর করে।

> **🎯 প্রোডাকশন-রেডি টুল**
> 
> এটি একটি বাস্তব MCP সার্ভার যা আপনি আজই ব্যবহার করতে পারেন! Microsoft Foundry MCP সার্ভার সম্পর্কে আরও জানতে আমাদের [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md) দেখুন।


- পূর্ণ ব্যবস্থাপনা করা MCP সার্ভার হোস্টিং বিল্ট-ইন স্কেলিং, মনিটরিং এবং নিরাপত্তা সহ
- Azure OpenAI, Azure AI Search এবং অন্যান্য Azure সার্ভিসের সাথে নেটিভ ইন্টিগ্রেশন
- Microsoft Entra ID এর মাধ্যমে এন্টারপ্রাইজ প্রমাণীকরণ এবং অথরাইজেশন
- কাস্টম টুল, প্রম্পট টেম্পলেট এবং রিসোর্স কানেক্টরের জন্য সমর্থন
- এন্টারপ্রাইজ নিরাপত্তা এবং নিয়ন্ত্রক প্রয়োজনীয়তার সাথে সামঞ্জস্যতা

**প্রযুক্তিগত বাস্তবায়ন:**

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

**ফলাফল:**  
- প্রস্তুত MCP সার্ভার প্ল্যাটফর্ম প্রদান করে এন্টারপ্রাইজ AI প্রকল্পগুলোর জন্য মূল্য সময় হ্রাস
- LLM, সরঞ্জাম এবং এন্টারপ্রাইজ ডেটা সুতার ইন্টিগ্রেশন সরলীকৃত
- MCP কর্মভারগুলোর জন্য নিরাপত্তা, পর্যবেক্ষণ ও পরিচালন দক্ষতা উন্নত
- Azure SDK সেরা অনুশীলন এবং বর্তমান প্রমাণীকরণ প্যাটার্নের মাধ্যমে কোড মান উন্নত

**রেফারেন্স:**  
- [Azure MCP ডকুমেন্টেশন](https://aka.ms/azmcp)
- [Azure MCP সার্ভার GitHub রিপোজিটরি](https://github.com/Azure/azure-mcp)
- [Azure AI সার্ভিসেস](https://azure.microsoft.com/en-us/products/ai-services/)
- [Microsoft MCP সেন্টার](https://mcp.azure.com)

## কেস স্টাডি ৬: NLWeb
MCP (Model Context Protocol) হল একটি উদীয়মান প্রটোকল যা চ্যাটবট এবং AI সহকারীরা সরঞ্জামের সাথে ইন্টারঅ্যাক্ট করতে ব্যবহার করে। প্রতিটি NLWeb ইনস্ট্যান্সও একটি MCP সার্ভার, যা একক মুল পদ্ধতি, ask, সমর্থন করে, যা একটি ওয়েবসাইটকে প্রাকৃতিক ভাষায় প্রশ্ন করতে ব্যবহৃত হয়। প্রত্যাবর্তিত প্রতিক্রিয়া schema.org ব্যবহার করে, যা ওয়েব ডেটা বর্ণনার জন্য বিস্তৃত ব্যবহৃত শব্দভাণ্ডার। সহজভাবে বলতে গেলে, MCP হল NLWeb ঠিক যেমন HTTP হল HTML। NLWeb প্রটোকল, Schema.org ফরম্যাট এবং নমুনা কোড মিশিয়ে সাইটগুলোকে দ্রুত এই এন্ডপয়েন্ট তৈরি করতে সাহায্য করে, যা কথোপকথনমূলক ইন্টারফেসের মাধ্যমে মানুষ এবং প্রাকৃতিক এজেন্ট-টু-এজেন্ট ইন্টারঅ্যাকশনের মাধ্যমে মেশিন উভয়ের জন্য উপকারী।

NLWeb এর দুটি ভিন্ন উপাদান আছে।
- একটি প্রটোকল, খুবই সহজ শুরু করার জন্য, একটি সাইটের সাথে প্রাকৃতিক ভাষায় ইন্টারফেস করার জন্য এবং একটি ফরম্যাট, যা প্রত্যাবর্তিত উত্তরের জন্য json এবং schema.org ব্যবহার করে। REST API ডকুমেন্টেশন এ আরও বিস্তারিত দেখুন।
- (1) এর সরল বাস্তবায়ন যা বিদ্যমান মার্কআপ ব্যবহার করে, সাইট যা আইটেমের তালিকা (পণ্য, রেসিপি, আকর্ষণ, পর্যালোচনা ইত্যাদি) হিসেবে বিমূর্ত করা যায় তাদের জন্য। ইউআই উইজেটসের একটি সেটের সঙ্গে, সাইটগুলো সহজে তাদের বিষয়বস্তুতে কথোপকথনমূলক ইন্টারফেস প্রদান করতে পারে। এই কাজের পদ্ধতি জানতে Life of a chat query ডকুমেন্টেশন দেখুন।
 
**রেফারেন্স:**  
- [Azure MCP ডকুমেন্টেশন](https://aka.ms/azmcp)
- [NLWeb](https://github.com/microsoft/NlWeb)

### কেস স্টাডি ৭: Microsoft Foundry MCP সার্ভার – এন্টারপ্রাইজ AI এজেন্ট ইন্টিগ্রেশন

Microsoft Foundry MCP সার্ভার দেখায় কীভাবে MCP ব্যবহার করে এন্টারপ্রাইজ পরিবেশে AI এজেন্ট এবং ওয়ার্কফ্লো গুলোকে পরিচালনা এবং ব্যবস্থাপনা করা যায়। MCP কে Microsoft Foundry এর সাথে একত্রিত করে সংগঠনগুলো এজেন্ট ইন্টারঅ্যাকশন স্ট্যান্ডার্ডাইজ করতে, Foundry এর ওয়ার্কফ্লো ব্যবস্থাপনাকে কাজে লাগাতে এবং নিরাপদ, স্কেলযোগ্য মোতায়েন নিশ্চিত করতে পারে।

> **🎯 প্রোডাকশন-রেডি টুল**
> 
> এটি একটি বাস্তব MCP সার্ভার যা আপনি আজই ব্যবহার করতে পারেন! Microsoft Foundry MCP সার্ভার সম্পর্কে আরও জানতে আমাদের [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#9--microsoft-foundry-mcp-server) দেখুন।

**মূল বৈশিষ্ট্যসমূহ:**
- মডেল ক্যাটালগ এবং মোতায়েন ব্যবস্থাপনা সহ Azure এর AI ইকোসিস্টেমে ব্যাপক অ্যাক্সেস
- RAG অ্যাপ্লিকেশনের জন্য Azure AI Search এর সাথে জ্ঞান ইনডেক্সিং
- AI মডেল পারফরম্যান্স এবং গুণমান নিশ্চিতকরণের জন্য মূল্যায়ন সরঞ্জাম
- সর্বাধুনিক গবেষণা মডেলের জন্য Microsoft Foundry ক্যাটালগ এবং ল্যাবের সাথে ইন্টিগ্রেশন
- প্রোডাকশন পরিস্থিতির জন্য এজেন্ট ব্যবস্থাপনা এবং মূল্যায়ন সক্ষমতা

**ফলাফল:**
- AI এজেন্ট ওয়ার্কফ্লোর দ্রুত প্রোটোটাইপিং এবং নির্ভরযোগ্য মনিটরিং
- উন্নত ব্যবহারের জন্য Azure AI সার্ভিসের সাথে সুনির্দিষ্ট সংহতি
- এজেন্ট পাইপলাইন নির্মাণ, মোতায়েন এবং মনিটরিংয়ের জন্য একক ইন্টারফেস
- এন্টারপ্রাইজের জন্য উন্নত নিরাপত্তা, সম্মতি এবং অপারেশন দক্ষতা
- জটিল এজেন্ট-চালিত প্রক্রিয়াগুলোর ওপর নিয়ন্ত্রণ বজায় রেখে AI গ্রহণ দ্রুততর করা

**রেফারেন্স:**
- [Microsoft Foundry MCP সার্ভার GitHub রিপোজিটরি](https://github.com/azure-ai-foundry/mcp-foundry)
- [Azure AI এজেন্টদের MCP এর সাথে একত্রিকরণ (Microsoft Foundry ব্লগ)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

### কেস স্টাডি ৮: Foundry MCP প্লেগ্রাউন্ড – পরীক্ষা ও প্রোটোটাইপিং

Foundry MCP প্লেগ্রাউন্ড MCP সার্ভার এবং Microsoft Foundry ইন্টিগ্রেশনের জন্য একটি প্রস্তুত ব্যবহারের পরিবেশ প্রদান করে। ডেভেলপাররা দ্রুত AI মডেল এবং এজেন্ট ওয়ার্কফ্লো প্রোটোটাইপ, পরীক্ষা এবং মূল্যায়ন করতে পারে Microsoft Foundry ক্যাটালগ এবং ল্যাব থেকে উৎস ব্যবহার করে। প্লেগ্রাউন্ড সেটআপ সহজ করে, নমুনা প্রকল্প দেয় এবং সমবায় উন্নয়ন সমর্থন করে, সেরা অনুশীলন এবং নতুন পরিস্থিতি অন্বেষণ করা সহজ করে তোলে কম ওভারহেডে। এটি বিশেষ করে দলের জন্য উপকারী যারা আইডিয়া যাচাই করতে, পরীক্ষা শেয়ার করতে এবং জটিল অবকাঠামোর প্রয়োজন ছাড়াই শেখার গতি বাড়াতে চায়। বাধা কমিয়ে প্লেগ্রাউন্ড MCP এবং Microsoft Foundry ইকোসিস্টেমে উদ্ভাবন এবং সম্প্রদায় অবদানে সহায়তা করে।

**রেফারেন্স:**

- [Foundry MCP প্লেগ্রাউন্ড GitHub রিপোজিটরি](https://github.com/azure-ai-foundry/foundry-mcp-playground)

### কেস স্টাডি ৯: Microsoft Learn Docs MCP সার্ভার – AI চালিত ডকুমেন্টেশন অ্যাক্সেস

Microsoft Learn Docs MCP সার্ভার একটি ক্লাউড-হোস্টেড সেবা যা AI সহকারীদের আধিকারিক Microsoft ডকুমেন্টেশনের রিয়েল-টাইম অ্যাক্সেস দেয় Model Context Protocol এর মাধ্যমে। এই প্রোডাকশন-রেডি সার্ভার ব্যাপক Microsoft Learn ইকোসিস্টেমের সাথে সংযুক্ত এবং সমস্ত অফিসিয়াল Microsoft উৎসের ওপর সেমান্টিক সন্ধান সক্ষম করে।

> **🎯 প্রোডাকশন-রেডি টুল**
> 
> এটি একটি বাস্তব MCP সার্ভার যা আপনি আজই ব্যবহার করতে পারেন! Microsoft Learn Docs MCP সার্ভার সম্পর্কে আরও জানতে আমাদের [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server) দেখুন।

**মূল বৈশিষ্ট্যসমূহ:**
- অফিসিয়াল Microsoft ডকুমেন্টেশন, Azure ডকুমেন্ট এবং Microsoft 365 ডকুমেন্টেশনের রিয়েল-টাইম অ্যাক্সেস
- প্রসঙ্গ এবং উদ্দেশ্য বুঝতে সক্ষম উন্নত সেমান্টিক সার্চ সক্ষমতা
- Microsoft Learn বিষয়বস্তু প্রকাশের সাথে সবসময় আপ-টু-ডেট তথ্য
- Microsoft Learn, Azure ডকুমেন্টেশন এবং Microsoft 365 উৎসে বিস্তৃত কভারেজ
- নিবন্ধ শিরোনাম এবং URL সহ সর্বোচ্চ ১০টি উচ্চমানের বিষয়বস্তু অংশ প্রদান করে

**কেন এটি গুরুত্বপূর্ণ:**
- Microsoft প্রযুক্তির "পতিত AI জ্ঞান" সমস্যা সমাধান করে
- AI সহকারীদের সর্বশেষ .NET, C#, Azure এবং Microsoft 365 বৈশিষ্ট্যগুলোতে অ্যাক্সেস নিশ্চিত করে
- সঠিক কোড উৎপাদনের জন্য কর্তৃত্বপূর্ণ, প্রথম পক্ষের তথ্য প্রদান করে
- দ্রুত পরিবর্তিত Microsoft প্রযুক্তি নিয়ে কাজ করা ডেভেলপারদের জন্য অপরিহার্য

**ফলাফল:**
- Microsoft প্রযুক্তির জন্য AI-উৎপাদিত কোডের নির্ভুলতা নাটকীয়ভাবে উন্নত হয়েছে
- বর্তমান ডকুমেন্টেশন এবং সেরা অনুশীলন অনুসন্ধানে ব্যয়িত সময় কমেছে
- প্রসঙ্গ-সচেতন ডকুমেন্টেশন পুনঃ আহরণের মাধ্যমে ডেভেলপার উৎপাদনশীলতা উন্নত হয়েছে
- IDE ছাড়াই উন্নয়ন ওয়ার্কফ্লোর সাথে নির্বিঘ্ন সংহতি

**রেফারেন্স:**
- [Microsoft Learn Docs MCP সার্ভার GitHub রিপোজিটরি](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn ডকুমেন্টেশন](https://learn.microsoft.com/)

## হাতে কলমে প্রকল্প

### প্রকল্প ১: মাল্টি-প্রোভাইডার MCP সার্ভার তৈরি করুন

**উদ্দেশ্য:** একটি MCP সার্ভার তৈরি করা যা নির্দিষ্ট শর্ত অনুসারে একাধিক AI মডেল প্রদানকারীকে অনুরোধ পাঠাতে পারে।

**প্রয়োজনীয়তা:**

- অন্তত তিনটি ভিন্ন মডেল প্রদানকারী (যেমন OpenAI, Anthropic, স্থানীয় মডেল) সমর্থন করা
- অনুরোধের মেটাডেটা ভিত্তিক রাউটিং মেকানিজম বাস্তবায়ন করা
- প্রদানকারীর ক্রেডেনশিয়াল ব্যবস্থাপনার জন্য কনফিগারেশন সিস্টেম তৈরি করা
- কর্মদক্ষতা এবং খরচ অপ্টিমাইজ করার জন্য ক্যাশিং যুক্ত করা
- ব্যবহারের মনিটরিংয়ের জন্য একটি সরল ড্যাশবোর্ড তৈরি করা

**বাস্তবায়ন ধাপ:**

1. মৌলিক MCP সার্ভার অবকাঠামো সাজানো
2. প্রতিটি AI মডেল সেবার জন্য প্রদানকারী অ্যাডাপ্টার বাস্তবায়ন করা
3. অনুরোধ বৈশিষ্ট্যের উপর ভিত্তি করে রাউটিং লজিক তৈরি করা
4. ঘন ঘন অনুরোধের জন্য ক্যাশিং মেকানিজম যুক্ত করা
5. মনিটরিং ড্যাশবোর্ড উন্নয়ন করা
6. বিভিন্ন অনুরোধ প্যাটার্ন দিয়ে পরীক্ষা করা

**প্রযুক্তি:** আপনার পছন্দ অনুযায়ী Python (.NET/Java/Python ভিত্তিক), ক্যাশিংয়ের জন্য Redis, এবং ড্যাশবোর্ডের জন্য সরল ওয়েব ফ্রেমওয়ার্ক বেছে নিন।

### প্রকল্প ২: এন্টারপ্রাইজ প্রম্পট ম্যানেজমেন্ট সিস্টেম

**উদ্দেশ্য:** একটি MCP-ভিত্তিক সিস্টেম তৈরি করা যা একটি সংগঠনের মধ্যে প্রম্পট টেমপ্লেটগুলোর ম্যানেজমেন্ট, সংস্করণ নিয়ন্ত্রণ এবং মোতায়েন নিশ্চিত করে।

**প্রয়োজনীয়তা:**


- প্রম্পট টেমপ্লেটের জন্য একটি কেন্দ্রীয় রিপোজিটরি তৈরি করুন
- সংস্করণ নিয়ন্ত্রণ এবং অনুমোদন কর্মপ্রবাহ বাস্তবায়ন করুন
- নমুনা ইনপুট সহ টেমপ্লেট পরীক্ষার ক্ষমতা গড়ে তুলুন
- ভূমিকা ভিত্তিক অ্যাক্সেস নিয়ন্ত্রণ উন্নয়ন করুন
- টেমপ্লেট পুনরুদ্ধার এবং প্রয়োগের জন্য একটি API তৈরি করুন

**বাস্তবায়ন ধাপসমূহ:**

1. টেমপ্লেট সংরক্ষণের জন্য ডাটাবেস স্কিমা ডিজাইন করুন
2. টেমপ্লেট CRUD অপারেশনগুলির জন্য মূল API তৈরি করুন
3. সংস্করণ ব্যবস্থা বাস্তবায়ন করুন
4. অনুমোদন কর্মপ্রবাহ তৈরি করুন
5. পরীক্ষার ফ্রেমওয়ার্ক উন্নয়ন করুন
6. ব্যবস্থাপনার জন্য একটি সহজ ওয়েব ইন্টারফেস তৈরি করুন
7. একটি MCP সার্ভারের সাথে ইন্টিগ্রেশন করুন

**প্রযুক্তি:** আপনার পছন্দ অনুযায়ী ব্যাকএন্ড ফ্রেমওয়ার্ক, SQL বা NoSQL ডাটাবেস, এবং ব্যবস্থাপনা ইন্টারফেসের জন্য একটি ফ্রন্টএন্ড ফ্রেমওয়ার্ক।

### প্রকল্প ৩: MCP-ভিত্তিক কন্টেন্ট জেনারেশন প্ল্যাটফর্ম

**উদ্দেশ্য:** MCP ব্যবহার করে একটি কন্টেন্ট জেনারেশন প্ল্যাটফর্ম তৈরি করুন যা বিভিন্ন কন্টেন্ট ধরণের ক্ষেত্রে সঙ্গতিপূর্ণ ফলাফল প্রদান করে।

**প্রয়োজনীয়তাসমূহ:**

- একাধিক কন্টেন্ট ফরম্যাট সমর্থন করুন (ব্লগ পোস্ট, সামাজিক মিডিয়া, মার্কেটিং কপি)
- কাস্টমাইজেশন অপশন সহ টেমপ্লেট-ভিত্তিক জেনারেশন বাস্তবায়ন করুন
- কন্টেন্ট পর্যালোচনা এবং প্রতিক্রিয়া ব্যবস্থা তৈরি করুন
- কন্টেন্ট কর্মক্ষমতা পরিমাপের তথ্য সংগ্রহ করুন
- কন্টেন্ট সংস্করণ নিয়ন্ত্রণ এবং পুনরাবৃত্তি সমর্থন করুন

**বাস্তবায়ন ধাপসমূহ:**

1. MCP ক্লায়েন্ট অবকাঠামো সেটআপ করুন
2. বিভিন্ন কন্টেন্ট ধরণের জন্য টেমপ্লেট তৈরি করুন
3. কন্টেন্ট জেনারেশন পাইপলাইন গড়ে তুলুন
4. পর্যালোচনা ব্যবস্থা বাস্তবায়ন করুন
5. তথ্য পরিমাপ ব্যবস্থার উন্নয়ন করুন
6. টেমপ্লেট ব্যবস্থাপনা এবং কন্টেন্ট জেনারেশনের জন্য একটি ব্যবহারকারী ইন্টারফেস তৈরি করুন

**প্রযুক্তি:** আপনার পছন্দের প্রোগ্রামিং ভাষা, ওয়েব ফ্রেমওয়ার্ক এবং ডাটাবেস সিস্টেম।

## MCP প্রযুক্তির ভবিষ্যৎ দিকনির্দেশনা

### উদীয়মান প্রবণতাসমূহ

1. **মাল্টি-মোডাল MCP**
   - চিত্র, অডিও, এবং ভিডিও মডেলের সাথে MCP ইন্টারঅ্যাকশন মানকরণ সম্প্রসারণ
   - ক্রস-মোডাল রিজনিং ক্ষমতা উন্নয়ন
   - ভিন্ন ভিন্ন মোডালিটিগুলোর জন্য মানসম্মত প্রম্পট ফরম্যাট

2. **ফেডারেটেড MCP অবকাঠামো**
   - বিতরণকৃত MCP নেটওয়ার্ক যা প্রতিষ্ঠানগুলোর মধ্যে সম্পদ ভাগাভাগি করতে পারে
   - নিরাপদ মডেল শেয়ারিংয়ের জন্য মানসম্মত প্রোটোকল
   - গোপনীয়তা-রক্ষা করা গণনা কৌশলসমূহ

3. **MCP মার্কেটপ্লেস**
   - MCP টেমপ্লেট এবং প্লাগইন ভাগাভাগি ও অর্থোপার্জনের পরিবেশ
   - গুণগত নিরীক্ষণ এবং সার্টিফিকেশন প্রক্রিয়া
   - মডেল মার্কেটপ্লেসের সাথে ইন্টিগ্রেশন

4. **এজ কম্পিউটিংয়ের জন্য MCP**
   - সম্পদ-সংকীর্ণ এজ ডিভাইসের জন্য MCP স্ট্যান্ডার্ডের অভিযোজন
   - কম-ব্যান্ডউইথ পরিবেশের জন্য অপটিমাইজড প্রোটোকল
   - IoT পরিবেশের জন্য বিশেষায়িত MCP বাস্তবায়ন

5. **নিয়ন্ত্রক কাঠামো**
   - নিয়ন্ত্রক সম্মতির জন্য MCP সম্প্রসারণ তৈরি
   - মানসম্মত অডিট ট্রেইল এবং ব্যাখ্যামূলক ইন্টারফেস
   - উদীয়মান AI শাসন কাঠামোর সাথে ইন্টিগ্রেশন

### মাইক্রোসফট থেকে MCP সমাধান

মাইক্রোসফট এবং আজুর বিভিন্ন ওপেন সোর্স রিপোজিটরি উন্নয়ন করেছে যা বিকাশকারীদের বিভিন্ন দৃশ্যে MCP বাস্তবায়নে সাহায্য করে:

#### Microsoft Organization

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - ব্রাউজার অটোমেশন এবং পরীক্ষার জন্য একটি Playwright MCP সার্ভার
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - লোকাল পরীক্ষার এবং কমিউনিটি অবদান জন্য OneDrive MCP সার্ভার বাস্তবায়ন
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWeb হলো খোলা প্রোটোকল এবং সংশ্লিষ্ট ওপেন সোর্স টুলসের সংগ্রহ। এর মূল লক্ষ্য হলো AI ওয়েবের জন্য একটি ভিত্তি স্তর প্রতিষ্ঠা করা

#### Azure-Samples Organization

1. [mcp](https://github.com/Azure-Samples/mcp) - Azure-এ বহু ভাষা ব্যবহার করে MCP সার্ভার তৈরি এবং ইন্টিগ্রেট করার জন্য নমুনা, টুলস, এবং রিসোর্সের লিংকসমূহ
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - মডেল কন্টেক্সট প্রোটোকল স্পেসিফিকেশনের সাথে প্রমাণীকরণ প্রদর্শনকারী রেফারেন্স MCP সার্ভারসমূহ
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure ফাংশনে রিমোট MCP সার্ভার বাস্তবায়নের ল্যান্ডিং পেজ এবং নির্দিষ্ট ভাষার রিপোজিটরি লিংকসমূহ
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure ফাংশন ব্যবহার করে পাইথনের মাধ্যমে কাস্টম রিমোট MCP সার্ভার তৈরি ও মোতায়েনের জন্য দ্রুত শুরু করার টেমপ্লেট
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - .NET/C# ব্যবহার করে Azure ফাংশনের মাধ্যমে কাস্টম রিমোট MCP সার্ভার নির্মাণের দ্রুত শুরু টেমপ্লেট
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - TypeScript দিয়ে Azure ফাংশন ব্যবহার করে কাস্টম রিমোট MCP সার্ভার তৈরির দ্রুত শুরু টেমপ্লেট
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - পাইথন ব্যবহার করে রিমোট MCP সার্ভারের জন্য Azure API ম্যানেজমেন্ট AI গেটওয়ে হিসেবে
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - MCP ক্ষমতা সহ APIM ❤️ AI এক্সপেরিমেন্টস, Azure OpenAI এবং AI Foundry এর সাথে ইন্টিগ্রেশন

এই রিপোজিটরিগুলো বিভিন্ন প্রোগ্রামিং ভাষা এবং Azure সেবার মধ্যে মডেল কন্টেক্সট প্রোটোকল নিয়ে কাজ করার জন্য বাস্তবায়ন, টেমপ্লেট এবং রিসোর্স সরবরাহ করে। এগুলো সাধারণ সার্ভার নির্মাণ থেকে শুরু করে প্রমাণীকরণ, ক্লাউড ডিপ্লয়মেন্ট এবং এন্টারপ্রাইজ ইন্টিগ্রেশন পর্যন্ত বিভিন্ন ব্যবহারিক ক্ষেত্র কভার করে।

#### MCP রিসোর্স ডিরেক্টরি

অফিসিয়াল Microsoft MCP রিপোজিটরির [MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) মডেল কন্টেক্সট প্রোটোকল সার্ভার ব্যবহার করার জন্য নমুনা রিসোর্স, প্রম্পট টেমপ্লেট এবং টুল সংজ্ঞার একটি সুসংগঠিত সংগ্রহ প্রদান করে। এই ডিরেক্টরিটি বিকাশকারীদের দ্রুত MCP শুরু করতে সাহায্য করার জন্য পুনঃব্যবহারযোগ্য বিল্ডিং ব্লক এবং সেরা অনুশীলনের উদাহরণ সরবরাহ করে:

- **প্রম্পট টেমপ্লেট:** সাধারণ AI কাজ এবং দৃশ্যের জন্য প্রস্তুত প্রম্পট টেমপ্লেট, যা আপনার MCP সার্ভার বাস্তবায়নের জন্য অভিযোজিত হতে পারে।
- **টুল সংজ্ঞা:** বিভিন্ন MCP সার্ভারে টুল ইন্টিগ্রেশন এবং কল করার জন্য মানসম্মত টুল স্কিমা এবং মেটাডেটার উদাহরণ।
- **রিসোর্স নমুনা:** MCP ফ্রেমওয়ার্কের আওতায় ডেটা সোর্স, API এবং বহিঃসেবা সংযোগের জন্য উদাহরণ রিসোর্স সংজ্ঞা।
- **রেফারেন্স বাস্তবায়ন:** প্রায়োগিক নমুনা যা দেখায় কিভাবে রিসোর্স, প্রম্পট এবং টুল গঠন ও সংস্থাবদ্ধ করতে হয় বাস্তব MCP প্রকল্পে।

এই রিসোর্সগুলো উন্নয়ন ত্বরান্বিত করে, মানসম্মত উন্নয়ন প্রচার করে, এবং MCP ভিত্তিক সমাধান নির্মাণ ও প্রয়োগের সময় সেরা অনুশীলনের নিশ্চয়তা দেয়।

#### MCP রিসোর্স ডিরেক্টরি

- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)

### গবেষণার সুযোগসমূহ

- MCP ফ্রেমওয়ার্কের মধ্যে কার্যকর প্রম্পট অপটিমাইজেশন পদ্ধতি
- মাল্টি-টেন্যান্ট MCP ডিপ্লয়মেন্টের জন্য নিরাপত্তা মডেল
- বিভিন্ন MCP বাস্তবায়নের পারফরম্যান্স বেঞ্চমার্কিং
- MCP সার্ভারের জন্য ফরমাল ভেরিফিকেশন পদ্ধতি

## উপসংহার

মডেল কন্টেক্সট প্রোটোকল (MCP) দ্রুত গতিতে শিল্পব্যাপী মানসম্মত, নিরাপদ, এবং আন্তঃঅপারেবল AI ইন্টিগ্রেশনের ভবিষ্যত তৈরি করছে। এই পাঠের ক্ষেত্রে অধ্যয়ন এবং হাতে কলম প্রকল্পের মাধ্যমে, আপনি দেখেছেন কিভাবে প্রাথমিক গ্রাহকরা—মাইক্রোসফট এবং আজুরসহ—MCP ব্যবহার করে বাস্তব জগতের সমস্যা সমাধান করছে, AI গ্রহণ দ্রুততর করছে, এবং সম্মতি, নিরাপত্তা, ও স্কেলেবল নকশা নিশ্চিত করছে। MCP এর মডুলার পদ্ধতি প্রতিষ্ঠানগুলোকে বৃহৎ ভাষা মডেল, টুলস, এবং এন্টারপ্রাইজ ডেটাকে একটি ঐক্যবদ্ধ, পরিদর্শনযোগ্য ফ্রেমওয়ার্কে সংযুক্ত করতে সক্ষম করে। MCP অব্যাহত বিকাশের সাথে, সম্প্রদায়ের সাথে জড়িত থাকা, ওপেন সোর্স রিসোর্স আবিষ্কার করা, এবং সেরা অনুশীলন প্রয়োগ করাই শক্তিশালী, ভবিষ্যত-পরিপক্ক AI সমাধান নির্মাণের চাবিকাঠি হবে।

## অতিরিক্ত রিসোর্সসমূহ

- [MCP Foundry GitHub Repository](https://github.com/azure-ai-foundry/mcp-foundry)
- [Foundry MCP Playground](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [Integrating Azure AI Agents with MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - নিরাপত্তার সেরা অনুশীলন
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

## অনুশীলনসমূহ

1. একটি কেস স্টাডি বিশ্লেষণ করুন এবং বিকল্প বাস্তবায়ন পন্থা প্রস্তাব করুন।
2. একটি প্রকল্প আইডিয়া নির্বাচন করুন এবং বিস্তারিত প্রযুক্তিগত স্পেসিফিকেশন তৈরি করুন।
3. কেস স্টাডিতে অন্তর্ভুক্ত নয় এমন একটি শিল্প গবেষণা করুন এবং ব্যাখ্যা করুন কিভাবে MCP তার নির্দিষ্ট চ্যালেঞ্জ মোকাবেলা করতে পারে।
4. ভবিষ্যত দিকনির্দেশনার একটি অংশ অন্বেষণ করুন এবং এটি সমর্থনের জন্য একটি নতুন MCP এক্সটেনশনের ধারণা তৈরি করুন।

## পরবর্তী ধাপ

আরও জানুন: [Microsoft MCP Servers](./microsoft-mcp-servers.md)

চালিয়ে যান: [Module 8: Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->