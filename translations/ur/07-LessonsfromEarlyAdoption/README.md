<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T17:51:48+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "ur"
}
-->
# ابتدائی اپنانے والوں سے اسباق

## جائزہ

یہ سبق اس بات کا جائزہ لیتا ہے کہ ابتدائی اپنانے والوں نے Model Context Protocol (MCP) کو کیسے استعمال کیا ہے تاکہ حقیقی دنیا کے مسائل حل کیے جا سکیں اور صنعتوں میں جدت کو فروغ دیا جا سکے۔ تفصیلی کیس اسٹڈیز اور عملی منصوبوں کے ذریعے، آپ دیکھیں گے کہ MCP کس طرح معیاری، محفوظ، اور توسیع پذیر AI انضمام کو ممکن بناتا ہے—جو بڑے زبان کے ماڈلز، ٹولز، اور انٹرپرائز ڈیٹا کو ایک متحد فریم ورک میں جوڑتا ہے۔ آپ MCP پر مبنی حل ڈیزائن کرنے اور بنانے کا عملی تجربہ حاصل کریں گے، ثابت شدہ نفاذی نمونوں سے سیکھیں گے، اور پروڈکشن ماحول میں MCP کو نافذ کرنے کے بہترین طریقے دریافت کریں گے۔ سبق ابھرتے ہوئے رجحانات، مستقبل کے راستے، اور اوپن سورس وسائل کو بھی اجاگر کرتا ہے تاکہ آپ MCP ٹیکنالوجی اور اس کے ترقی پذیر ماحولیاتی نظام کے سب سے آگے رہ سکیں۔

## سیکھنے کے مقاصد

- مختلف صنعتوں میں حقیقی دنیا کی MCP نفاذ کا تجزیہ کریں  
- مکمل MCP پر مبنی ایپلیکیشنز ڈیزائن اور بنائیں  
- MCP ٹیکنالوجی میں ابھرتے ہوئے رجحانات اور مستقبل کے راستوں کو دریافت کریں  
- حقیقی ترقیاتی حالات میں بہترین طریقے اپنائیں  

## حقیقی دنیا کی MCP نفاذ

### کیس اسٹڈی 1: انٹرپرائز کسٹمر سپورٹ آٹومیشن

ایک کثیر القومی کمپنی نے MCP پر مبنی حل نافذ کیا تاکہ اپنے کسٹمر سپورٹ سسٹمز میں AI تعاملات کو معیاری بنایا جا سکے۔ اس سے وہ درج ذیل کر سکے:

- متعدد LLM فراہم کنندگان کے لیے ایک متحد انٹرفیس تخلیق کریں  
- محکموں میں مستقل پرامپٹ مینجمنٹ برقرار رکھیں  
- مضبوط سیکیورٹی اور تعمیل کنٹرول نافذ کریں  
- مخصوص ضروریات کی بنیاد پر مختلف AI ماڈلز کے درمیان آسانی سے سوئچ کریں  

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

**نتائج:** ماڈل کے اخراجات میں 30% کمی، جواب کی مستقل مزاجی میں 45% بہتری، اور عالمی آپریشنز میں تعمیل میں اضافہ۔

### کیس اسٹڈی 2: ہیلتھ کیئر تشخیصی معاون

ایک صحت کی دیکھ بھال فراہم کنندہ نے MCP انفراسٹرکچر تیار کیا تاکہ متعدد تخصصی طبی AI ماڈلز کو مربوط کیا جا سکے جبکہ حساس مریض کے ڈیٹا کی حفاظت کو یقینی بنایا جائے:

- جنرل اور اسپیشلسٹ طبی ماڈلز کے درمیان ہموار سوئچنگ  
- سخت پرائیویسی کنٹرولز اور آڈٹ ٹریلز  
- موجودہ Electronic Health Record (EHR) سسٹمز کے ساتھ انضمام  
- طبی اصطلاحات کے لیے مستقل پرامپٹ انجینئرنگ  

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

**نتائج:** ڈاکٹروں کے لیے بہتر تشخیصی تجاویز، مکمل HIPAA تعمیل کے ساتھ، اور سسٹمز کے درمیان کانٹیکسٹ سوئچنگ میں نمایاں کمی۔

### کیس اسٹڈی 3: مالیاتی خدمات رسک تجزیہ

ایک مالیاتی ادارے نے MCP نافذ کیا تاکہ مختلف محکموں میں اپنے رسک تجزیہ کے عمل کو معیاری بنایا جا سکے:

- کریڈٹ رسک، فراڈ ڈیٹیکشن، اور سرمایہ کاری کے رسک ماڈلز کے لیے ایک متحد انٹرفیس تخلیق کیا  
- سخت رسائی کنٹرولز اور ماڈل ورژننگ نافذ کی  
- تمام AI سفارشات کی آڈیٹیبلٹی کو یقینی بنایا  
- مختلف سسٹمز میں مستقل ڈیٹا فارمیٹنگ برقرار رکھی  

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

**نتائج:** ریگولیٹری تعمیل میں بہتری، ماڈل کی تعیناتی کے چکر 40% تیز، اور محکموں میں رسک اسیسمنٹ کی مستقل مزاجی میں اضافہ۔

### کیس اسٹڈی 4: Microsoft Playwright MCP سرور براؤزر آٹومیشن کے لیے

Microsoft نے [Playwright MCP server](https://github.com/microsoft/playwright-mcp) تیار کیا تاکہ Model Context Protocol کے ذریعے محفوظ، معیاری براؤزر آٹومیشن ممکن ہو سکے۔ یہ حل AI ایجنٹس اور LLMs کو کنٹرول شدہ، قابل آڈٹ، اور توسیع پذیر طریقے سے ویب براؤزرز کے ساتھ تعامل کرنے کی اجازت دیتا ہے—جیسے خودکار ویب ٹیسٹنگ، ڈیٹا نکالنا، اور مکمل ورک فلو۔

- براؤزر آٹومیشن کی صلاحیتوں (نیویگیشن، فارم فلنگ، اسکرین شاٹ کیپچر، وغیرہ) کو MCP ٹولز کے طور پر فراہم کرتا ہے  
- غیر مجاز کارروائیوں کو روکنے کے لیے سخت رسائی کنٹرولز اور سینڈ باکسنگ نافذ کرتا ہے  
- تمام براؤزر تعاملات کے لیے تفصیلی آڈٹ لاگز فراہم کرتا ہے  
- ایجنٹ ڈرائیون آٹومیشن کے لیے Azure OpenAI اور دیگر LLM فراہم کنندگان کے ساتھ انضمام کی حمایت کرتا ہے  

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

**نتائج:**  
- AI ایجنٹس اور LLMs کے لیے محفوظ، پروگراماتی براؤزر آٹومیشن ممکن بنایا  
- دستی ٹیسٹنگ کی کوششوں کو کم کیا اور ویب ایپلیکیشنز کے لیے ٹیسٹ کوریج بہتر کی  
- انٹرپرائز ماحول میں براؤزر بیسڈ ٹول انٹیگریشن کے لیے قابل استعمال، توسیع پذیر فریم ورک فراہم کیا  

**References:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)  

### کیس اسٹڈی 5: Azure MCP – انٹرپرائز گریڈ Model Context Protocol بطور سروس

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) Microsoft کا منظم، انٹرپرائز گریڈ نفاذ ہے جو Model Context Protocol کو کلاؤڈ سروس کے طور پر توسیع پذیر، محفوظ، اور تعمیل کرنے والے MCP سرور کی صلاحیتیں فراہم کرتا ہے۔ Azure MCP تنظیموں کو تیزی سے MCP سرورز کو تعینات، انتظام، اور Azure AI، ڈیٹا، اور سیکیورٹی سروسز کے ساتھ مربوط کرنے کی اجازت دیتا ہے، جس سے آپریشنل بوجھ کم ہوتا ہے اور AI اپنانے میں تیزی آتی ہے۔

- مکمل طور پر منظم MCP سرور ہوسٹنگ، جس میں بلٹ ان اسکیلنگ، مانیٹرنگ، اور سیکیورٹی شامل ہے  
- Azure OpenAI، Azure AI Search، اور دیگر Azure سروسز کے ساتھ مقامی انضمام  
- Microsoft Entra ID کے ذریعے انٹرپرائز تصدیق اور اجازت  
- کسٹم ٹولز، پرامپٹ ٹیمپلیٹس، اور ریسورس کنیکٹرز کی حمایت  
- انٹرپرائز سیکیورٹی اور ریگولیٹری تقاضوں کے ساتھ تعمیل  

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

**نتائج:**  
- انٹرپرائز AI منصوبوں کے لیے ویلیو حاصل کرنے کا وقت کم کیا، ایک تیار استعمال، تعمیل شدہ MCP سرور پلیٹ فارم فراہم کر کے  
- LLMs، ٹولز، اور انٹرپرائز ڈیٹا ذرائع کے انضمام کو آسان بنایا  
- MCP ورک لوڈز کے لیے سیکیورٹی، قابل مشاہدہ پن، اور آپریشنل کارکردگی میں اضافہ کیا  

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)  

## کیس اسٹڈی 6: NLWeb

MCP (Model Context Protocol) چیٹ بوٹس اور AI اسسٹنٹس کے لیے ایک ابھرتا ہوا پروٹوکول ہے جو ٹولز کے ساتھ تعامل کو ممکن بناتا ہے۔ ہر NLWeb انسٹانس بھی ایک MCP سرور ہے، جو ایک بنیادی طریقہ، ask، کو سپورٹ کرتا ہے، جس کے ذریعے ویب سائٹ سے قدرتی زبان میں سوال پوچھا جاتا ہے۔ واپس آنے والا جواب schema.org کا استعمال کرتا ہے، جو ویب ڈیٹا کی وضاحت کے لیے ایک وسیع پیمانے پر استعمال ہونے والا لغت ہے۔ آسان الفاظ میں، MCP NLWeb کی طرح ہے جیسے HTTP HTML کے لیے ہے۔ NLWeb پروٹوکولز، Schema.org فارمیٹس، اور نمونہ کوڈ کو یکجا کرتا ہے تاکہ سائٹس تیزی سے یہ اینڈپوائنٹس بنا سکیں، جو انسانی صارفین کو بات چیت کے انٹرفیس کے ذریعے اور مشینوں کو قدرتی ایجنٹ ٹو ایجنٹ تعامل کے ذریعے فائدہ پہنچاتے ہیں۔

NLWeb کے دو مختلف اجزاء ہیں:  
- ایک پروٹوکول، جو شروع کرنے میں بہت آسان ہے، جو سائٹ کے ساتھ قدرتی زبان میں انٹرفیس کے لیے ہے اور ایک فارمیٹ، جو جواب کے لیے json اور schema.org کا استعمال کرتا ہے۔ REST API کی دستاویزات میں مزید تفصیلات دیکھیں۔  
- ایک سیدھا سادہ نفاذ جو (1) کا فائدہ اٹھاتا ہے، موجودہ مارک اپ کا استعمال کرتے ہوئے، ان سائٹس کے لیے جو اشیاء کی فہرستوں (مصنوعات، ترکیبیں، تفریحات، جائزے، وغیرہ) کی طرح سمجھی جا سکتی ہیں۔ صارف انٹرفیس وجیٹس کے ساتھ مل کر، سائٹس اپنے مواد کے لیے آسانی سے بات چیت کے انٹرفیس فراہم کر سکتی ہیں۔ Life of a chat query کی دستاویزات میں اس کے کام کرنے کے طریقہ کار کی مزید تفصیلات دیکھیں۔  

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)  

## عملی منصوبے

### منصوبہ 1: ملٹی-پرووائیڈر MCP سرور بنائیں

**مقصد:** ایک ایسا MCP سرور بنائیں جو مخصوص معیار کی بنیاد پر متعدد AI ماڈل فراہم کنندگان کو درخواستیں بھیج سکے۔

**ضروریات:**  
- کم از کم تین مختلف ماڈل فراہم کنندگان کی حمایت کریں (مثلاً OpenAI، Anthropic، لوکل ماڈلز)  
- درخواست کے میٹا ڈیٹا کی بنیاد پر روٹنگ میکانزم نافذ کریں  
- فراہم کنندگان کے اسناد کے انتظام کے لیے کنفیگریشن سسٹم بنائیں  
- کارکردگی اور اخراجات کو بہتر بنانے کے لیے کیشنگ شامل کریں  
- استعمال کی نگرانی کے لیے ایک سادہ ڈیش بورڈ بنائیں  

**نفاذ کے مراحل:**  
1. بنیادی MCP سرور انفراسٹرکچر سیٹ اپ کریں  
2. ہر AI ماڈل سروس کے لیے فراہم کنندہ ایڈاپٹر نافذ کریں  
3. درخواست کی خصوصیات کی بنیاد پر روٹنگ لاجک بنائیں  
4. بار بار آنے والی درخواستوں کے لیے کیشنگ میکانزم شامل کریں  
5. مانیٹرنگ ڈیش بورڈ تیار کریں  
6. مختلف درخواست پیٹرنز کے ساتھ ٹیسٹ کریں  

**ٹیکنالوجیز:** اپنی پسند کے مطابق Python (.NET/Java/Python)، کیشنگ کے لیے Redis، اور ڈیش بورڈ کے لیے سادہ ویب فریم ورک منتخب کریں۔

### منصوبہ 2: انٹرپرائز پرامپٹ مینجمنٹ سسٹم

**مقصد:** ایک MCP پر مبنی سسٹم تیار کریں جو تنظیم بھر میں پرامپٹ ٹیمپلیٹس کا انتظام، ورژننگ، اور تعیناتی کرے۔

**ضروریات:**  
- پرامپٹ ٹیمپلیٹس کے لیے مرکزی ذخیرہ بنائیں  
- ورژننگ اور منظوری کے ورک فلو نافذ کریں  
- نمونہ ان پٹ کے ساتھ ٹیمپلیٹ ٹیسٹنگ کی صلاحیتیں بنائیں  
- رول پر مبنی رسائی کنٹرولز تیار کریں  
- ٹیمپلیٹ بازیافت اور تعیناتی کے لیے API بنائیں  

**نفاذ کے مراحل:**  
1. ٹیمپلیٹ اسٹوریج کے لیے ڈیٹا بیس اسکیمہ ڈیزائن کریں  
2. ٹیمپلیٹ CRUD آپریشنز کے لیے بنیادی API بنائیں  
3. ورژننگ سسٹم نافذ کریں  
4. منظوری کے ورک فلو تیار کریں  
5. ٹیسٹنگ فریم ورک بنائیں  
6. مینجمنٹ کے لیے سادہ ویب انٹرفیس تیار کریں  
7. MCP سرور کے ساتھ انضمام کریں  

**ٹیکنالوجیز:** اپنی پسند کے مطابق بیک اینڈ فریم ورک، SQL یا NoSQL ڈیٹا بیس، اور فرنٹ اینڈ فریم ورک استعمال کریں۔

### منصوبہ 3: MCP پر مبنی مواد تخلیق کا پلیٹ فارم

**مقصد:** ایک ایسا مواد تخلیق کا پلیٹ فارم بنائیں جو MCP کا فائدہ اٹھاتے ہوئے مختلف مواد کی اقسام میں مستقل نتائج فراہم کرے۔

**ضروریات:**  
- متعدد مواد کے فارمیٹس کی حمایت کریں (بلاگ پوسٹس، سوشل میڈیا، مارکیٹنگ کاپی)  
- ٹیمپلیٹ پر مبنی تخلیق کو حسب ضرورت اختیارات کے ساتھ نافذ کریں  
- مواد کا جائزہ اور فیڈبیک سسٹم بنائیں  
- مواد کی کارکردگی کے میٹرکس کا ٹریک رکھیں  
- مواد کی ورژننگ اور تکرار کی حمایت کریں  

**نفاذ کے مراحل:**  
1. MCP کلائنٹ انفراسٹرکچر سیٹ اپ کریں  
2. مختلف مواد کی اقسام کے لیے ٹیمپلیٹس بنائیں  
3. مواد تخلیق کی پائپ لائن تیار کریں  
4. جائزہ سسٹم نافذ کریں  
5. میٹرکس ٹریکنگ سسٹم بنائیں  
6. ٹیمپلیٹ مینجمنٹ اور مواد تخلیق کے لیے یوزر انٹرفیس تیار کریں  

**ٹیکنالوجیز:** اپنی پسند کی پروگرامنگ زبان، ویب فریم ورک، اور ڈیٹا بیس سسٹم منتخب کریں۔

## MCP ٹیکنالوجی کے لیے مستقبل کے راستے

### ابھرتے ہوئے رجحانات

1. **ملٹی موڈل MCP**  
   - تصویر، آڈیو، اور ویڈیو ماڈلز کے ساتھ تعاملات کو معیاری بنانے کے لیے MCP کا توسیع  
   - کراس موڈل استدلال کی صلاحیتوں کی ترقی  
   - مختلف موڈالیٹیز کے لیے معیاری پرامپٹ فارمیٹس  

2. **فیڈریٹڈ MCP انفراسٹرکچر**  
   - تنظیموں کے درمیان وسائل شیئر کرنے والے تقسیم شدہ MCP نیٹ ورکس  
   - محفوظ ماڈل شیئرنگ کے لیے معیاری پروٹوکولز  
   - پرائیویسی محفوظ کرنے والی کمپیوٹیشن تکنیکیں  

3. **MCP مارکیٹ پلیسز**  
   - MCP ٹیمپلیٹس اور پلگ انز کے اشتراک اور مونیٹائزیشن کے لیے ماحولیاتی نظام  
   - معیار کی یقین دہانی اور سرٹیفیکیشن کے عمل  
   - ماڈل مارکیٹ پلیسز کے ساتھ انضمام  

4. **ایج کمپیوٹنگ کے لیے MCP**  
   - وسائل محدود ایج ڈیوائسز کے لیے MCP معیارات کی تطبیق  
   - کم بینڈوڈتھ ماحول کے لیے بہتر پروٹوکولز  
   - IoT ماحولیاتی نظام کے لیے مخصوص MCP نفاذ  

5. **ریگولیٹری فریم ورکس**  
   - ریگولیٹری تعمیل کے لیے MCP توسیعات کی ترقی  
   - معیاری آڈٹ ٹریلز اور وضاحت کے انٹرفیس  
   - ابھرتے ہوئے AI گورننس فریم ورکس کے ساتھ انضمام  

### Microsoft کی جانب سے MCP حل

Microsoft اور Azure نے کئی اوپن سورس ریپوزیٹریز تیار کی ہیں تاکہ ڈیولپرز کو مختلف منظرناموں میں MCP نافذ کرنے میں مدد ملے:

#### Microsoft آرگنائزیشن  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - براؤزر آٹومیشن اور ٹیسٹنگ کے لیے Playwright MCP سرور  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - لوکل ٹیسٹنگ اور کمیونٹی تعاون کے لیے OneDrive MCP سرور نفاذ  
3. [NLWeb](https://github.com/microsoft/NlWeb) - اوپن پروٹوکولز اور متعلقہ اوپن سورس ٹولز کا مجموعہ، AI ویب کے لیے بنیادی پرت  

#### Azure-Samples آرگنائزیشن  
1. [mcp](https://github.com/Azure-Samples/mcp) - Azure پر MCP سرورز بنانے اور مربوط کرنے کے لیے نمونے، ٹولز، اور وسائل  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - موجودہ Model Context Protocol وضاحت کے ساتھ تصدیق دکھانے والے MCP سرورز  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure Functions میں Remote MCP سرور نفاذ کے لیے لینڈنگ پیج  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure Functions کے ساتھ Python میں کسٹم Remote MCP سرورز بنانے کا کوئیک اسٹارٹ ٹیمپلیٹ  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Azure Functions کے ساتھ .NET/C# میں کسٹم Remote MCP سرورز بنانے کا کوئیک اسٹارٹ ٹیمپلیٹ  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Azure Functions کے ساتھ TypeScript میں کسٹم Remote MCP سرورز بنانے کا کوئیک اسٹارٹ ٹیمپلیٹ  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Python کا استعمال کرتے ہوئے Azure API Management کو AI گیٹ وے کے طور پر Remote MCP سرورز کے لیے  
8. [AI-Gateway](https://github.com/Azure-Samples
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## مشقیں

1. کسی ایک کیس اسٹڈی کا تجزیہ کریں اور ایک متبادل نفاذ کا طریقہ تجویز کریں۔
2. کسی ایک پروجیکٹ آئیڈیا کا انتخاب کریں اور ایک تفصیلی تکنیکی وضاحت تیار کریں۔
3. کسی ایسی صنعت پر تحقیق کریں جو کیس اسٹڈیز میں شامل نہیں ہے اور بیان کریں کہ MCP اس کی مخصوص چیلنجز کو کیسے حل کر سکتا ہے۔
4. مستقبل کے کسی ایک رخ کا جائزہ لیں اور اسے سپورٹ کرنے کے لیے ایک نئے MCP توسیع کا تصور تیار کریں۔

اگلا: [Best Practices](../08-BestPractices/README.md)

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔