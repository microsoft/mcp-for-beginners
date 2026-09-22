# 🌟 ابتدائی اختیار کنندگان سے اسباق

[![Lessons from MCP Early Adopters](../../../translated_images/ur/08.980bb2babbaadd8a.webp)](https://youtu.be/jds7dSmNptE)

_(ویڈیو دیکھنے کے لیے اوپر دی گئی تصویر پر کلک کریں)_

## 🎯 یہ ماڈیول کیا کور کرتا ہے

یہ ماڈیول بتاتا ہے کہ حقیقی تنظیمیں اور ڈویلپرز ماڈل کانٹیکسٹ پروٹوکول (MCP) کا استعمال کس طرح کرتے ہوئے حقیقی چیلنجز کو حل کر رہے ہیں اور جدت کو آگے بڑھا رہے ہیں۔ تفصیلی کیس اسٹڈیز، عملی منصوبے، اور قابلِ عمل مثالوں کے ذریعے، آپ دریافت کریں گے کہ MCP کیسے محفوظ، پھیلنے والا AI انٹگریشن فراہم کرتا ہے جو زبان کے ماڈلز، ٹولز، اور انٹرپرائز ڈیٹا کو مربوط کرتا ہے۔

### 📚 MCP کو عملی طور پر دیکھیں

کیا آپ چاہتے ہیں کہ یہ اصول پیداوار کے قابل ٹولز میں استعمال ہوتے ہوئے دیکھیں؟ ہمارے [**10 مائیکروسافٹ MCP سرورز جو ڈویلپر کی پیداواریت کو تبدیل کر رہے ہیں**](microsoft-mcp-servers.md) ملاحظہ کریں، جو حقیقی مائیکروسافٹ MCP سرورز کی نمائش کرتے ہیں جنہیں آپ آج استعمال کر سکتے ہیں۔

## جائزہ

یہ سبق یہ بتاتا ہے کہ ابتدائی اختیار کنندگان نے ماڈل کانٹیکسٹ پروٹوکول (MCP) کو کس طرح استعمال کرتے ہوئے واقعی دنیا کے چیلنجز کو حل کیا اور مختلف صنعتوں میں جدت کو فروغ دیا۔ تفصیلی کیس اسٹڈیز اور عملی منصوبوں کے ذریعے، آپ دیکھیں گے کہ MCP کس طرح معیاری، محفوظ، اور پھیلنے والا AI انضمام مہیا کرتا ہے — بڑے زبان کے ماڈلز، ٹولز، اور انٹرپرائز ڈیٹا کو ایک مربوط فریم ورک میں جوڑتا ہے۔ آپ MCP پر مبنی حل ڈیزائن اور تعمیر کرنے کا عملی تجربہ حاصل کریں گے، ثابت شدہ نفاذ کے نمونوں سے سیکھیں گے، اور پروڈکشن ماحول میں MCP کو تعینات کرنے کے لیے بہترین طریقوں کو دریافت کریں گے۔ یہ سبق ابھرتے ہوئے رجحانات، مستقبل کی سمتوں، اور اوپن سورس وسائل کو بھی اجاگر کرتا ہے تاکہ آپ MCP ٹیکنالوجی اور اس کے ارتقائی ماحولیاتی نظام کے صف اول میں رہیں۔

## تعلیمی مقاصد

- مختلف صنعتوں میں حقیقی MCP نفاذ کا تجزیہ کریں
- مکمل MCP پر مبنی ایپلیکیشنز ڈیزائن اور تعمیر کریں
- MCP ٹیکنالوجی میں ابھرتے ہوئے رجحانات اور مستقبل کی سمتوں کو دریافت کریں
- حقیقی ترقیاتی حالات میں بہترین طریقے استعمال کریں

## حقیقی دنیا میں MCP نفاذ

### کیس اسٹڈی 1: انٹرپرائز کسٹمر سپورٹ آٹومیشن

ایک کثیر القومی کمپنی نے اپنے کسٹمر سپورٹ سسٹمز کے درمیان AI تعاملات کو یکساں کرنے کے لیے MCP پر مبنی حل نافذ کیا۔ اس سے انہیں یہ کام کرنے میں مدد ملی:

- متعدد LLM فراہم کنندگان کے لیے ایک متحد انٹرفیس بنائیں
- ڈیپارٹمنٹوں میں یکساں پرامپٹ مینجمنٹ برقرار رکھیں
- مضبوط سیکیورٹی اور تعمیل کنٹرولز نافذ کریں
- مخصوص ضرورتوں کی بنیاد پر مختلف AI ماڈلز کے درمیان آسانی سے سوئچ کریں

**تکنیکی نفاذ:**

```python
# کسٹمر سپورٹ کے لیے Python MCP سرور کا نفاذ
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# لاگنگ کو ترتیب دیں
logging.basicConfig(level=logging.INFO)

async def main():
    # سرور کی ترتیب بنائیں
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # MCP سرور کو initialize کریں
    server = create_server(config)
    
    # علم کے بیس کے وسائل رجسٹر کریں
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # پرامپٹ ٹیمپلیٹس رجسٹر کریں
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # سپورٹ ٹولز رجسٹر کریں
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # HTTP ٹرانسپورٹ کے ساتھ سرور شروع کریں
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**نتائج:** ماڈل کی لاگت میں 30٪ کمی، جواب کی مستقل مزاجی میں 45٪ بہتری، اور عالمی آپریشنز میں بہتر تعمیل۔

### کیس اسٹڈی 2: صحت کی دیکھ بھال کے تشخیصی معاون

ایک صحت کی دیکھ بھال فراہم کرنے والے نے متعدد مخصوص طبی AI ماڈلز کو ضم کرنے کے لیے MCP کا انفراسٹرکچر تیار کیا جبکہ حساس مریض کے ڈیٹا کی حفاظت کو یقینی بنایا:

- جنرل اور اسپیشلسٹ میڈیکل ماڈلز کے درمیان آسان سوئچنگ
- سخت پرائیویسی کنٹرولز اور آڈٹ ٹریل
- موجودہ الیکٹرانک ہیلتھ ریکارڈ (EHR) سسٹمز کے ساتھ انضمام
- طبّی اصطلاحات کے لیے یکساں پرامپٹ انجینئرنگ

**تکنیکی نفاذ:**

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

**نتائج:** ڈاکٹروں کے لیے تشخیصی تجاویز میں بہتری جبکہ مکمل HIPAA تعمیل اور سسٹمز کے درمیان سیاق و سباق کی تبدیلی میں نمایاں کمی۔

### کیس اسٹڈی 3: مالیاتی خدمات میں رسک اینالیسس

ایک مالیاتی ادارے نے اپنے مختلف شعبوں میں رسک اینالیسس کے عمل کو یکسان کرنے کے لیے MCP نافذ کیا:

- کریڈٹ رسک، فراڈ ڈیٹیکشن، اور سرمایہ کاری کے رسک ماڈلز کے لیے ایک متحد انٹرفیس بنایا
- سخت رسائی کنٹرولز اور ماڈل ورژنینگ نافذ کی
- تمام AI سفارشات کی آڈٹ ایبلٹی کی ضمانت دی
- مختلف سسٹمز میں ڈیٹا کی یکساں فارمیٹنگ برقرار رکھی

**تکنیکی نفاذ:**

```java
// مالی خطروں کے اندازہ کے لیے جاوا MCP سرور
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // مالیاتی تعمیل کی خصوصیات کے ساتھ MCP سرور بنائیں
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

**نتائج:** بہتر ریگولیٹری تعمیل، ماڈل کی تعیناتی کے دورانیے میں 40٪ تیزی، اور شعبوں میں رسک اسیسمنٹ کی مستقل مزاجی۔

### کیس اسٹڈی 4: مائیکروسافٹ پلے رائٹ MCP سرور براؤزر آٹومیشن کے لیے

مائیکروسافٹ نے [Playwright MCP سرور](https://github.com/microsoft/playwright-mcp) تیار کیا تاکہ ماڈل کانٹیکسٹ پروٹوکول کے ذریعے محفوظ، معیاری براؤزر آٹومیشن کی سہولت فراہم کی جا سکے۔ یہ پیداوار کے لیے تیار سرور AI ایجنٹس اور LLMs کو کنٹرول شدہ، آڈٹ کے قابل، اور قابل توسیع طریقے سے ویب براؤزرز کے ساتھ بات چیت کرنے کی اجازت دیتا ہے — خودکار ویب ٹیسٹنگ، ڈیٹا استخراج، اور مکمل ورک فلو کے استعمال کے لیے۔

> **🎯 پیداوار کے لیے تیار ٹول**
>
> یہ کیس اسٹڈی ایک حقیقی MCP سرور پیش کرتی ہے جسے آپ آج استعمال کر سکتے ہیں! Playwright MCP سرور اور دیگر 9 پیداواری مائیکروسافٹ MCP سرورز کے بارے میں مزید جاننے کے لیے ہماری [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#8--playwright-mcp-server) دیکھیں۔

**اہم خصوصیات:**
- براؤزر آٹومیشن صلاحیتیں (نیوی گیشن، فارم بھرنا، اسکرین شاٹ، وغیرہ) MCP ٹولز کے طور پر فراہم کرتا ہے
- غیر مجاز ایکشنز کو روکنے کے لیے سخت رسائی کنٹرولز اور سینڈ باکسنگ نافذ کرتا ہے
- تمام براؤزر تعاملات کے تفصیلی آڈٹ لاگز فراہم کرتا ہے
- ایجنٹ کے زیر انتظام آٹومیشن کے لیے Azure OpenAI اور دیگر LLM فراہم کنندگان کے ساتھ انضمام کی حمایت کرتا ہے
- GitHub Copilot کے کوڈنگ ایجنٹ کو ویب براؤزنگ صلاحیت دیتا ہے

**تکنیکی نفاذ:**

```typescript
// ٹائپ اسکرپٹ: ایم سی پی سرور میں پلے رائٹ براؤزر آٹومیشن ٹولز کو رجسٹر کرنا
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// یو آر ایل پر نیویگیٹ کرنے اور اسکرین شاٹ لینے کے لیے ایک ٹول رجسٹر کریں
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

// ایم سی پی سرور شروع کریں
server.listen(8080);
```

**نتائج:**

- AI ایجنٹس اور LLMs کے لیے محفوظ، پروگراماتیبراؤزر آٹومیشن کو فعال کیا
- دستی ٹیسٹنگ کی کوششوں کو کم کیا اور ویب درخواستوں کے لیے ٹیسٹ کوریج کو بہتر بنایا
- انٹرپرائز ماحول میں براؤزر پر مبنی ٹول انٹیگریشن کے لیے ایک قابل استعمال، قابل توسیع فریم ورک فراہم کیا
- GitHub Copilot کی ویب براؤزنگ صلاحیت کو تقویت دی

**حوالہ جات:**

- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### کیس اسٹڈی 5: Azure MCP – انٹرپرائز گریڈ ماڈل کانٹیکسٹ پروٹوکول بطور سروس

Azure MCP Server ([https://aka.ms/azmcp](https://aka.ms/azmcp)) مائیکروسافٹ کا مکمل منظم، انٹرپرائز گریڈ ماڈل کانٹیکسٹ پروٹوکول کا نفاذ ہے، جو کلاؤڈ سروس کے طور پر پھیلنے، محفوظ، اور تعمیل کرنے والی MCP سرور صلاحیتیں فراہم کرنے کے لیے ڈیزائن کیا گیا ہے۔ Azure MCP تنظیموں کو تیزی سے MCP سرورز تعینات کرنے، مینج کرنے، اور Azure AI، ڈیٹا، اور سیکیورٹی خدمات کے ساتھ مربوط کرنے کی اجازت دیتا ہے، آپریشنل بوجھ کو کم کرتا ہے اور AI اپنانے میں تیزی لاتا ہے۔

> **🎯 پیداوار کے لیے تیار ٹول**
>
> یہ ایک حقیقی MCP سرور ہے جسے آپ آج استعمال کر سکتے ہیں! Microsoft Foundry MCP Server کے بارے میں مزید جاننے کے لیے ہماری [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md) دیکھیں۔


- مکمل منظم MCP سرور ہوسٹنگ، جس میں اسکيلنگ، مانیٹرنگ، اور سیکیورٹی شامل ہے
- Azure OpenAI، Azure AI سرچ، اور دیگر Azure خدمات کے ساتھ مقامی انضمام
- Microsoft Entra ID کے ذریعے انٹرپرائز تصدیق اور اجازت
- کسٹم ٹولز، پرامپٹ ٹیمپلیٹس، اور ریسورس کنیکٹرز کی حمایت
- انٹرپرائز سیکیورٹی اور ریگولیٹری تقاضوں کے ساتھ تعمیل

**تکنیکی نفاذ:**

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

**نتائج:**  
- انٹرپرائز AI منصوبوں کے لیے قیمت حاصل کرنے کے وقت کو کم کیا کیونکہ ایک تیار استعمال، تعمیل شدہ MCP سرور پلیٹ فارم فراہم کیا گیا
- LLMs، ٹولز، اور انٹرپرائز ڈیٹا ذرائع کے انضمام کو آسان بنایا
- MCP ورک لوڈز کے لیے بہتر سیکیورٹی، مشاہدہ پذیری، اور آپریشنل کارکردگی
- Azure SDK کے بہترین طریقوں اور موجودہ تصدیقی پیٹرنز کے ساتھ کوڈ معیار کو بہتر بنایا

**حوالہ جات:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [Azure MCP Server GitHub Repository](https://github.com/Azure/azure-mcp)
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)
- [Microsoft MCP Center](https://mcp.azure.com)

## کیس اسٹڈی 6: NLWeb 
MCP (ماڈل کانٹیکسٹ پروٹوکول) ایک ابھرتا ہوا پروٹوکول ہے جو چیٹ بوٹس اور AI معاونین کو ٹولز کے ساتھ بات چیت کرنے کے لیے استعمال ہوتا ہے۔ ہر NLWeb انسٹانس بھی ایک MCP سرور ہے، جو ایک بنیادی طریقہ کار، ask، کی حمایت کرتا ہے، جسے ویب سائٹ سے قدرتی زبان میں سوال کرنے کے لیے استعمال کیا جاتا ہے۔ موصولہ جواب schema.org کا استعمال کرتا ہے، جو ویب ڈیٹا کی وضاحت کے لیے ایک وسیع پیمانے پر استعمال شدہ لغت ہے۔ آسان الفاظ میں، MCP ویسا ہی ہے جیسا HTTP ہے HTML کے لیے۔ NLWeb پروٹوکولز، Schema.org فارمیٹس، اور نمونہ کوڈ کو یکجا کرتا ہے تاکہ سائٹس تیزی سے یہ اینڈ پوائنٹس بنا سکیں، جس سے انسانی گفتگو پر مبنی انٹرفیسز اور قدرتی ایجنٹ سے ایجنٹ بات چیت دونوں کو فائدہ پہنچتا ہے۔

NLWeb کے دو مختلف اجزاء ہیں۔
- ایک پروٹوکول، جو شروع کرنے کے لیے بہت آسان ہے، جو قدرتی زبان میں سائٹ کے ساتھ انٹرفیس کے لیے ہے اور ایک فارمیٹ، جو واپس آنے والے جواب کے لیے json اور schema.org استعمال کرتا ہے۔ مزید تفصیلات کے لیے REST API کی دستاویزات دیکھیں۔
- ایک سیدھا سادہ نفاذ جو (1) کا فائدہ اٹھاتا ہے اور موجودہ مارک اپ استعمال کرتا ہے، ان سائٹس کے لیے جو آئٹمز کی فہرستوں (مصنوعات، ترکیبیں، سیاحتی مقامات، جائزے، وغیرہ) کے طور پر خلاصہ کی جا سکتی ہیں۔ صارف انٹرفیس وجیٹس کے ایک سیٹ کے ساتھ، سائٹس آسانی سے اپنے مواد کے لیے بات چیت کے انٹرفیس فراہم کر سکتی ہیں۔ مزید تفصیلات کے لیے Life of a chat query کی دستاویزات دیکھیں کہ یہ کیسے کام کرتا ہے۔

**حوالہ جات:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [NLWeb](https://github.com/microsoft/NlWeb)

### کیس اسٹڈی 7: Microsoft Foundry MCP سرور – انٹرپرائز AI ایجنٹ انضمام

Microsoft Foundry MCP سرورز یہ ظاہر کرتے ہیں کہ MCP کو کس طرح استعمال کیا جا سکتا ہے تاکہ انٹرپرائز ماحول میں AI ایجنٹس اور ورک فلو کو منظم اور منظّم کیا جا سکے۔ MCP کو Microsoft Foundry کے ساتھ یکجا کر کے، تنظیمیں ایجنٹ بات چیت کو معیاری بنا سکتی ہیں، Foundry کے ورک فلو مینجمنٹ سے فائدہ اٹھا سکتی ہیں، اور محفوظ، وسعت پذیر تعیناتی کو یقینی بنا سکتی ہیں۔

> **🎯 پیداوار کے لیے تیار ٹول**
>
> یہ ایک حقیقی MCP سرور ہے جسے آپ آج استعمال کر سکتے ہیں! Microsoft Foundry MCP Server کے بارے میں مزید جاننے کے لیے ہماری [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#9--microsoft-foundry-mcp-server) دیکھیں۔

**اہم خصوصیات:**
- Azure کے AI ماحولیاتی نظام تک مکمل رسائی، بشمول ماڈل کیٹلاگز اور تعیناتی مینجمنٹ
- RAG ایپلیکیشنز کے لیے Azure AI سرچ کے ساتھ نالج انڈیکسنگ
- AI ماڈل کی کارکردگی اور معیار کی یقین دہانی کے لیے تشخیصی ٹولز
- Microsoft Foundry کیٹلاگ اور لیبز کے ساتھ انضمام برائے جدید تحقیقاتی ماڈلز
- پیداواری مناظر کے لیے ایجنٹ مینجمنٹ اور تشخیصی صلاحیتیں

**نتائج:**
- AI ایجنٹ ورک فلو کی تیز رفتار پروٹو ٹائپنگ اور مضبوط نگرانی
- جدید مناظر کے لیے Azure AI خدمات کے ساتھ بغیر رکاوٹ انضمام
- ایجنٹ پائپ لائنز کی تعمیر، تعیناتی، اور نگرانی کے لیے متحد انٹرفیس
- انٹرپرائزز کے لیے بہتر سیکیورٹی، تعمیل، اور آپریشنل کارکردگی
- پیچیدہ ایجنٹ زیر نگرانی عمل پر قابو رکھتے ہوئے AI اپنانے میں تیز رفتاری

**حوالہ جات:**
- [Microsoft Foundry MCP Server GitHub Repository](https://github.com/azure-ai-foundry/mcp-foundry)
- [Integrating Azure AI Agents with MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

### کیس اسٹڈی 8: Foundry MCP Playground – تجربات اور پروٹو ٹائپنگ

Foundry MCP Playground MCP سرورز اور Microsoft Foundry انضمام کے ساتھ تجربہ کرنے کے لیے تیار استعمال ماحول فراہم کرتا ہے۔ ڈویلپرز جلدی سے AI ماڈلز اور ایجنٹ ورک فلو کا پروٹو ٹائپ، ٹیسٹ، اور تشخیص کر سکتے ہیں، Microsoft Foundry کیٹلاگ اور لیبز کے وسائل استعمال کرتے ہوئے۔ یہ پلیگراؤنڈ سیٹ اپ کو آسان بناتا ہے، نمونہ منصوبے فراہم کرتا ہے، اور مشترکہ ترقی کی حمایت کرتا ہے، جس سے نئے منظرناموں اور بہترین طریقوں کی آسان تلاش ممکن ہوتی ہے۔ یہ خاص طور پر اُن ٹیموں کے لیے مفید ہے جو خیالات کی تصدیق، تجربات کا اشتراک، اور سیکھی کی تیز رفتاری چاہتے ہیں بغیر پیچیدہ انفراسٹرکچر کے۔ داخلے کی رکاوٹ کو کم کر کے، یہ MCP اور Microsoft Foundry کے ماحولیاتی نظام میں جدت اور کمیونٹی شراکت کو فروغ دیتا ہے۔

**حوالہ جات:**

- [Foundry MCP Playground GitHub Repository](https://github.com/azure-ai-foundry/foundry-mcp-playground)

### کیس اسٹڈی 9: Microsoft Learn Docs MCP سرور – AI سے چلنے والی دستاویزات کی رسائی

Microsoft Learn Docs MCP سرور ایک کلاؤڈ ہوسٹڈ سروس ہے جو AI معاونین کو ماڈل کانٹیکسٹ پروٹوکول کے ذریعے حقیقی وقت میں مائیکروسافٹ کی سرکاری دستاویزات تک رسائی فراہم کرتی ہے۔ یہ پیداوار کے لیے تیار سرور جامع Microsoft Learn ماحولیاتی نظام سے جڑتا ہے اور تمام سرکاری Microsoft ذرائع میں معنوی تلاش ممکن بناتا ہے۔

> **🎯 پیداوار کے لیے تیار ٹول**
>
> یہ ایک حقیقی MCP سرور ہے جسے آپ آج استعمال کر سکتے ہیں! Microsoft Learn Docs MCP Server کے بارے میں مزید جاننے کے لیے ہماری [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server) دیکھیں۔

**اہم خصوصیات:**
- Microsoft کی سرکاری دستاویزات، Azure دستاویزات، اور Microsoft 365 دستاویزات تک حقیقی وقت میں رسائی
- اعلیٰ سطحی معنوی تلاش کی صلاحیتیں جو سیاق و سباق اور نیت کو سمجھتی ہیں
- Microsoft Learn کے مواد کی اشاعت کے مطابق ہمیشہ جدید معلومات
- Microsoft Learn، Azure دستاویزات، اور Microsoft 365 ذرائع کے مکمل احاطہ
- آرٹیکل عنوانات اور URLs کے ساتھ 10 اعلیٰ معیار کے مواد کے چنکس واپس کرتی ہے

**یہ کیوں ضروری ہے:**
- مائیکروسافٹ ٹیکنالوجیز کے لیے "پرانا AI علم" مسئلہ حل کرتا ہے
- AI معاونین کو جدید .NET، C#, Azure، اور Microsoft 365 خصوصیات تک رسائی کی ضمانت دیتا ہے
- درست کوڈ جنریشن کے لیے مستند، پہلی پارٹی معلومات فراہم کرتا ہے
- ان ڈویلپرز کے لیے ضروری جو تیزی سے بدلتی ہوئی Microsoft ٹیکنالوجیز کے ساتھ کام کر رہے ہیں

**نتائج:**
- Microsoft ٹیکنالوجیز کے لیے AI تیار کردہ کوڈ کی درستگی میں نمایاں اضافہ
- موجودہ دستاویزات اور بہترین طریقوں کی تلاش کے لیے وقت میں کمی
- تناظر کے مطابق دستاویزات کی بازیافت کے ساتھ ڈویلپر کی پیداواری صلاحیت میں اضافہ
- IDE چھوڑے بغیر ڈیولپمنٹ ورک فلو کے ساتھ بے جوڑ انضمام

**حوالہ جات:**
- [Microsoft Learn Docs MCP Server GitHub Repository](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn Documentation](https://learn.microsoft.com/)

## عملی منصوبے

### منصوبہ 1: ملٹی فراہم کنندہ MCP سرور بنائیں

**مقصد:** ایک MCP سرور تخلیق کریں جو مخصوص معیار کی بنیاد پر متعدد AI ماڈل فراہم کنندگان کو درخواستیں روٹ کر سکے۔

**ضروریات:**

- کم از کم تین مختلف ماڈل فراہم کنندگان کی حمایت کریں (جیسے OpenAI، Anthropic، مقامی ماڈلز)
- درخواست کے میٹا ڈیٹا کی بنیاد پر روٹنگ میکانزم نافذ کریں
- فراہم کنندہ کے اسناد کے انتظام کے لیے ایک کنفیگریشن سسٹم بنائیں
- کارکردگی اور لاگت کو بہتر بنانے کے لیے کیشنگ شامل کریں
- استعمال کی نگرانی کے لیے ایک سادہ ڈیش بورڈ بنائیں

**نفاذ کے اقدامات:**

1. بنیادی MCP سرور انفراسٹرکچر مرتب کریں
2. ہر AI ماڈل سروس کے لیے فراہم کنندہ ایڈاپٹرز نافذ کریں
3. درخواست کی خصوصیات کی بنیاد پر روٹنگ لاجک بنائیں
4. بار بار آنے والی درخواستوں کے لیے کیشنگ میکانزم شامل کریں
5. نگرانی کے ڈیش بورڈ کی ترقی کریں
6. مختلف درخواست کے نمونوں کے ساتھ ٹیسٹ کریں

**ٹیکنالوجیز:** Python (.NET/Java/Python حسبِ پسند)، کیشنگ کے لیے Redis، اور ڈیش بورڈ کے لیے ایک سادہ ویب فریم ورک کا انتخاب کریں۔

### منصوبہ 2: انٹرپرائز پرامپٹ مینجمنٹ سسٹم

**مقصد:** ایک MCP پر مبنی نظام تیار کریں جو ادارے میں پرامپٹ ٹیمپلیٹس کے انتظام، ورژننگ، اور تعیناتی کے لیے ہو۔

**ضروریات:**


- پرامپٹ ٹیمپلیٹس کے لیے ایک مرکزی ذخیرہ بنائیں
- ورژننگ اور منظوری کے ورک فلو نافذ کریں
- نمونہ ان پٹ کے ساتھ ٹیمپلیٹ ٹیسٹنگ کی صلاحیتیں تیار کریں
- کردار کی بنیاد پر رسائی کنٹرول تیار کریں
- ٹیمپلیٹ بازیافت اور تعیناتی کے لیے API بنائیں

**نفاذ کے مراحل:**

1. ٹیمپلیٹ اسٹوریج کے لیے ڈیٹا بیس اسکیمہ ڈیزائن کریں
2. ٹیمپلیٹ CRUD آپریشنز کے لیے بنیادی API بنائیں
3. ورژننگ سسٹم نافذ کریں
4. منظوری کے ورک فلو کو تعمیر کریں
5. ٹیسٹنگ فریم ورک تیار کریں
6. انتظام کے لیے سادہ ویب انٹرفیس بنائیں
7. MCP سرور کے ساتھ انٹیگریٹ کریں

**ٹیکنالوجیز:** آپ کی پسند کا بیک اینڈ فریم ورک، SQL یا NoSQL ڈیٹا بیس، اور مینجمنٹ انٹرفیس کے لیے فرنٹ اینڈ فریم ورک۔

### پروجیکٹ 3: MCP پر مبنی مواد بنانے کا پلیٹ فارم

**مقصد:** ایک مواد بنانے کا پلیٹ فارم تیار کریں جو MCP کا استعمال کرتا ہو تاکہ مختلف مواد کی اقسام میں مستقل نتائج فراہم کیے جا سکیں۔

**ضروریات:**

- متعدد مواد کے فارمیٹس کی حمایت (بلاگ پوسٹس، سوشل میڈیا، مارکیٹنگ کاپی)
- ٹیمپلیٹ پر مبنی جنریشن نفاذ کریں جس میں تخصیص کے اختیارات ہوں
- مواد کا جائزہ اور فیڈبیک کا نظام تیار کریں
- مواد کی کارکردگی کے میٹرکس کو ٹریک کریں
- مواد کے ورژننگ اور دوبارہ تکرار کی حمایت کریں

**نفاذ کے مراحل:**

1. MCP کلائنٹ انفراسٹرکچر سیٹ اپ کریں
2. مختلف مواد کی اقسام کے لیے ٹیمپلیٹس بنائیں
3. مواد بنانے کی پائپ لائن تیار کریں
4. جائزہ نظام نافذ کریں
5. میٹرکس ٹریکنگ سسٹم تیار کریں
6. ٹیمپلیٹ مینجمنٹ اور مواد بنانے کے لیے صارف انٹرفیس بنائیں

**ٹیکنالوجیز:** آپ کی پسندیدہ پروگرامنگ زبان، ویب فریم ورک، اور ڈیٹا بیس سسٹم۔

## MCP ٹیکنالوجی کے لیے مستقبل کے راستے

### ابھرتے ہوئے رجحانات

1. **کثیر النوع MCP**
   - MCP کی توسیع تاکہ تصویر، آڈیو، اور ویڈیو ماڈلز کے ساتھ تعاملات کو معیاری بنایا جا سکے
   - کراس-موڈل استدلال کی صلاحیتوں کی ترقی
   - مختلف موڈالٹیز کے لیے معیاری پرامپٹ فارمیٹس

2. **وفاقی MCP انفراسٹرکچر**
   - تقسیم شدہ MCP نیٹ ورکس جو تنظیموں کے درمیان وسائل کا اشتراک کر سکتے ہیں
   - ماڈل شیئرنگ کے لیے معیاری پروٹوکولز برائے سیکیورٹی
   - رازداری کی حفاظت کرنے والی کمپیوٹیشن تکنیکیں

3. **MCP مارکیٹ پلیسز**
   - MCP ٹیمپلیٹس اور پلگ انز کے اشتراک اور منیٹائزیشن کے لیے ماحولیاتی نظام
   - معیار کی یقین دہانی اور سرٹیفیکیشن کے عمل
   - ماڈل مارکیٹ پلیسز کے ساتھ انٹیگریشن

4. **ایج کمپیوٹنگ کے لیے MCP**
   - وسائل محدود ایج ڈیوائسز کے لیے MCP معیارات کی مطابقت پذیری
   - کم بینڈوڈتھ ماحول کے لیے بہتر کردہ پروٹوکولز
   - IoT ایکو سسٹمز کے لیے مخصوص MCP نفاذات

5. **ریگولیٹری فریم ورکس**
   - ریگولیٹری تعمیل کے لیے MCP کی توسیعات کی تیاری
   - معیاری آڈٹ ٹریلز اور وضاحت کے انٹرفیسز
   - ابھرتے ہوئے AI گورننس فریم ورکس کے ساتھ انٹیگریشن

### مائیکروسافٹ کے MCP حل

مائیکروسافٹ اور ایزور نے مختلف منظرناموں میں MCP کو نافذ کرنے کے لیے کئی اوپن سورس ذخیرے تیار کیے ہیں:

#### مائیکروسافٹ آرگنائزیشن

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - براؤزر آٹومیشن اور ٹیسٹنگ کے لیے ایک Playwright MCP سرور
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - لوکل ٹیسٹنگ اور کمیونٹی شراکت کے لیے OneDrive MCP سرور کا نفاذ
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWeb اوپن پروٹوکولز اور متعلقہ اوپن سورس ٹولز کا مجموعہ ہے۔ اس کا مرکزی فوکس AI ویب کے لیے بنیاد قائم کرنا ہے

#### Azure-Samples آرگنائزیشن

1. [mcp](https://github.com/Azure-Samples/mcp) - Azure پر متعدد زبانوں کا استعمال کرتے ہوئے MCP سرورز کی تعمیر اور انٹیگریشن کے لیے نمونے، ٹولز، اور وسائل کے لنکس
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - موجودہ ماڈل کانٹیکسٹ پروٹوکول وضاحت کے ساتھ توثیق ظاہر کرنے والے MCP سرورز کی مثالیں
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure فنکشنز میں ریموٹ MCP سرور کے نفاذ کے لیے لینڈنگ پیج اور زبان مخصوص ذخائر کے لنکس
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure فنکشنز کے ساتھ Python استعمال کرتے ہوئے ریموٹ MCP سرورز بنانے اور تعینات کرنے کے لیے کوئیک اسٹارٹ ٹیمپلیٹ
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - .NET/C# استعمال کرتے ہوئے ریموٹ MCP سرورز کی تعمیر اور تعیناتی کے لیے کوئیک اسٹارٹ ٹیمپلیٹ
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - TypeScript استعمال کرتے ہوئے ریموٹ MCP سرورز بنانے اور تعینات کرنے کے لیے کوئیک اسٹارٹ ٹیمپلیٹ
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Python استعمال کرتے ہوئے ریموٹ MCP سرورز کے لیے Azure API مینجمنٹ بطور AI گیٹ وے
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI تجربات بشمول MCP صلاحیتیں، Azure OpenAI اور AI Foundry کے ساتھ انٹیگریشن

یہ ذخیرے مختلف پروگرامنگ زبانوں اور Azure خدمات کے درمیان ماڈل کانٹیکسٹ پروٹوکول کے ساتھ کام کرنے کے لیے مختلف نفاذات، ٹیمپلیٹس، اور وسائل فراہم کرتے ہیں۔ یہ بنیادی سرور نفاذات سے لے کر توثیق، کلاؤڈ تعیناتی، اور انٹرپرائز انٹیگریشن منظرناموں تک کے وسیع استعمال کے معاملات کا احاطہ کرتے ہیں۔

#### MCP وسائل ڈائرکٹری

سرکاری Microsoft MCP ذخیرے میں [MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) ایک منظم مجموعہ ہے جو ماڈل کانٹیکسٹ پروٹوکول سرورز کے ساتھ استعمال کے لیے نمونہ وسائل، پرامپٹ ٹیمپلیٹس، اور ٹول تعریفیں فراہم کرتا ہے۔ یہ ڈائرکٹری ڈویلپرز کی مدد کے لیے تیار کی گئی ہے تاکہ وہ MCP کے ساتھ جلدی آغاز کر سکیں، قابلِ استعمال بلاکس اور بہترین عمل کی مثالیں پیش کرکے:

- **پرامپٹ ٹیمپلیٹس:** عام AI کاموں اور منظرناموں کے لیے تیار استعمال ہونے والے پرامپٹ ٹیمپلیٹس، جنہیں آپ اپنے MCP سرور کے نفاذات کے لیے ڈھال سکتے ہیں۔
- **ٹول تعریفیں:** ٹول انٹیگریشن اور کال کے معیاری بنانے کے لیے مثالیں ٹول اسکیمہ اور میٹاڈیٹا۔
- **وسائل کے نمونے:** MCP فریم ورک میں ڈیٹا ذرائع، APIs، اور بیرونی خدمات سے منسلک ہونے کے لیے مثالیں وسائل کی تعریفیں۔
- **حوالہ نفاذات:** عملی نمونے جو دکھاتے ہیں کہ MCP کے پروجیکٹس میں وسائل، پرامپٹس، اور ٹولز کو کس طرح منظم اور ترتیب دیا جا سکتا ہے۔

یہ وسائل ترقی کو تیز کرتے ہیں، معیاری بنانے کو فروغ دیتے ہیں، اور MCP پر مبنی حل بنانے اور تعینات کرنے کے دوران بہترین عمل کے نفاذ کو یقینی بنانے میں مدد کرتے ہیں۔

#### MCP وسائل ڈائرکٹری

- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)

### تحقیقی مواقع

- MCP فریم ورکس میں مؤثر پرامپٹ اصلاح کی تکنیکیں
- ملٹی ٹیننٹ MCP تعیناتیوں کے لیے سیکیورٹی ماڈلز
- مختلف MCP نفاذات کے مابین کارکردگی کا جائزہ لینا
- MCP سرورز کے لیے رسمی تصدیقی طریقے

## نتیجہ

ماڈل کانٹیکسٹ پروٹوکول (MCP) تیزی سے ان صنعتوں میں معیاری، محفوظ، اور باہم قابلِ عمل AI انضمام کے مستقبل کو تشکیل دے رہا ہے۔ اس سبق میں کیس اسٹڈیز اور عملی پروجیکٹس کے ذریعے، آپ نے دیکھا کہ مائیکروسافٹ اور ایزور جیسے ابتدائی اپنانے والے کس طرح MCP کو حقیقی دنیا کے مسائل حل کرنے، AI کی اپنانے کی رفتار بڑھانے، اور تعمیل، سیکیورٹی، اور اسکیل ایبلٹی کو یقینی بنانے کے لیے استعمال کر رہے ہیں۔ MCP کا ماڈیولر انداز تنظیموں کو بڑے زبان کے ماڈلز، ٹولز، اور انٹرپرائز ڈیٹا کو ایک متحد، قابلِ آڈٹ فریم ورک میں منسلک کرنے کی سہولت دیتا ہے۔ جیسے جیسے MCP ترقی کرتا رہے گا، کمیونٹی کے ساتھ جڑے رہنا، اوپن سورس وسائل کو دریافت کرنا، اور بہترین طریقوں کو اپنانا مضبوط، مستقبل کے لیے تیار AI حل بنانے کی کلید ہوگی۔

## اضافی وسائل

- [MCP Foundry GitHub Repository](https://github.com/azure-ai-foundry/mcp-foundry)
- [Foundry MCP Playground](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [Integrating Azure AI Agents with MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - سیکیورٹی کے بہترین طریقے
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

## مشقیں

1. ایک کیس اسٹڈی کا تجزیہ کریں اور ایک متبادل نفاذ کا طریقہ تجویز کریں۔
2. ایک پروجیکٹ آئیڈیا منتخب کریں اور ایک مفصل تکنیکی وضاحت تیار کریں۔
3. ایک ایسی صنعت پر تحقیق کریں جو کیس اسٹڈیز میں شامل نہیں ہے اور یہ بیان کریں کہ MCP اس کی مخصوص مشکلات کو کیسے حل کر سکتا ہے۔
4. مستقبل کے راستوں میں سے ایک کو دریافت کریں اور اس کی حمایت کے لیے MCP کے ایک نئے توسیع کے لیے تصور تیار کریں۔

## آگے کیا ہے

مزید تلاش کریں: [Microsoft MCP Servers](./microsoft-mcp-servers.md)

جاری رکھیں: [Module 8: Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->