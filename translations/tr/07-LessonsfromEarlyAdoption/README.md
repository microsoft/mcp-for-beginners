<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:20:10+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "tr"
}
-->
# Erken Benimseyenlerden Alınan Dersler

## Genel Bakış

Bu ders, erken benimseyenlerin Model Context Protocol (MCP) kullanarak gerçek dünya sorunlarını nasıl çözdüklerini ve sektörlerde inovasyonu nasıl hızlandırdıklarını inceliyor. Detaylı vaka analizleri ve uygulamalı projeler aracılığıyla, MCP'nin büyük dil modelleri, araçlar ve kurumsal verileri tek bir çatı altında standart, güvenli ve ölçeklenebilir şekilde nasıl entegre ettiğini göreceksiniz. MCP tabanlı çözümler tasarlayıp inşa etme konusunda pratik deneyim kazanacak, kanıtlanmış uygulama desenlerinden öğrenecek ve MCP'yi üretim ortamlarında dağıtmak için en iyi uygulamaları keşfedeceksiniz. Ders ayrıca ortaya çıkan trendleri, gelecekteki yönelimleri ve açık kaynak kaynaklarını vurgulayarak MCP teknolojisi ve gelişen ekosisteminin ön saflarında kalmanıza yardımcı olacak.

## Öğrenme Hedefleri

- Farklı sektörlerdeki gerçek dünya MCP uygulamalarını analiz etmek  
- Tamamlanmış MCP tabanlı uygulamalar tasarlayıp geliştirmek  
- MCP teknolojisindeki yeni trendleri ve gelecek yönelimlerini keşfetmek  
- Gerçek geliştirme senaryolarında en iyi uygulamaları uygulamak  

## Gerçek Dünya MCP Uygulamaları

### Vaka Çalışması 1: Kurumsal Müşteri Destek Otomasyonu

Çok uluslu bir şirket, müşteri destek sistemlerinde AI etkileşimlerini standartlaştırmak için MCP tabanlı bir çözüm uyguladı. Bu sayede:

- Birden çok LLM sağlayıcısı için birleşik bir arayüz oluşturuldu  
- Departmanlar arasında tutarlı prompt yönetimi sağlandı  
- Güçlü güvenlik ve uyumluluk kontrolleri uygulandı  
- Belirli ihtiyaçlara göre farklı AI modelleri arasında kolayca geçiş yapıldı  

**Teknik Uygulama:**  
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

**Sonuçlar:** Model maliyetlerinde %30 azalma, yanıt tutarlılığında %45 iyileşme ve küresel operasyonlarda artırılmış uyumluluk.

### Vaka Çalışması 2: Sağlık Hizmetleri Tanı Asistanı

Bir sağlık hizmeti sağlayıcısı, birden fazla uzmanlaşmış tıbbi AI modelini entegre etmek için MCP altyapısı geliştirdi ve hassas hasta verilerinin korunmasını sağladı:

- Genel ve uzman tıbbi modeller arasında kesintisiz geçiş  
- Sıkı gizlilik kontrolleri ve denetim kayıtları  
- Mevcut Elektronik Sağlık Kayıtları (EHR) sistemleriyle entegrasyon  
- Tıbbi terminoloji için tutarlı prompt mühendisliği  

**Teknik Uygulama:**  
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

**Sonuçlar:** Doktorlar için geliştirilmiş tanı önerileri, tam HIPAA uyumluluğu ve sistemler arası bağlam değiştirme süresinde önemli azalma.

### Vaka Çalışması 3: Finansal Hizmetlerde Risk Analizi

Bir finans kuruluşu, farklı departmanlar arasında risk analiz süreçlerini standartlaştırmak için MCP uyguladı:

- Kredi riski, dolandırıcılık tespiti ve yatırım riski modelleri için birleşik arayüz oluşturuldu  
- Sıkı erişim kontrolleri ve model sürüm yönetimi uygulandı  
- Tüm AI önerilerinin denetlenebilirliği sağlandı  
- Farklı sistemler arasında tutarlı veri formatlama korundu  

**Teknik Uygulama:**  
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

**Sonuçlar:** Artırılmış düzenleyici uyumluluk, %40 daha hızlı model dağıtım döngüleri ve departmanlar arası risk değerlendirme tutarlılığında iyileşme.

### Vaka Çalışması 4: Microsoft Playwright MCP Sunucusu ile Tarayıcı Otomasyonu

Microsoft, Model Context Protocol aracılığıyla güvenli, standartlaştırılmış tarayıcı otomasyonu sağlamak için [Playwright MCP sunucusunu](https://github.com/microsoft/playwright-mcp) geliştirdi. Bu çözüm, AI ajanlarının ve LLM'lerin web tarayıcıları ile kontrollü, denetlenebilir ve genişletilebilir şekilde etkileşim kurmasına olanak tanır; otomatik web testi, veri çıkarımı ve uçtan uca iş akışları gibi kullanım senaryolarını destekler.

- Tarayıcı otomasyon yeteneklerini (navigasyon, form doldurma, ekran görüntüsü alma vb.) MCP araçları olarak sunar  
- Yetkisiz işlemleri önlemek için sıkı erişim kontrolleri ve sandbox uygulaması yapar  
- Tüm tarayıcı etkileşimleri için ayrıntılı denetim kayıtları sağlar  
- Ajan odaklı otomasyon için Azure OpenAI ve diğer LLM sağlayıcılarıyla entegrasyonu destekler  

**Teknik Uygulama:**  
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

**Sonuçlar:**  
- AI ajanları ve LLM'ler için güvenli, programlı tarayıcı otomasyonu sağlandı  
- Manuel test çabaları azaldı ve web uygulamaları için test kapsamı genişledi  
- Kurumsal ortamda tarayıcı tabanlı araç entegrasyonu için yeniden kullanılabilir, genişletilebilir bir çerçeve sunuldu  

**Referanslar:**  
- [Playwright MCP Server GitHub Deposu](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI ve Otomasyon Çözümleri](https://azure.microsoft.com/en-us/products/ai-services/)  

### Vaka Çalışması 5: Azure MCP – Kurumsal Düzeyde Model Context Protocol Hizmeti

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)), Microsoft’un Model Context Protocol’ün yönetilen, kurumsal düzeyde uygulaması olup, ölçeklenebilir, güvenli ve uyumlu MCP sunucu yeteneklerini bulut hizmeti olarak sunmak üzere tasarlanmıştır. Azure MCP, kuruluşların MCP sunucularını Azure AI, veri ve güvenlik hizmetleriyle hızlıca dağıtmasını, yönetmesini ve entegre etmesini sağlayarak operasyonel yükü azaltır ve AI benimsemeyi hızlandırır.

- Yerleşik ölçeklendirme, izleme ve güvenlik özellikleriyle tam yönetilen MCP sunucu barındırma  
- Azure OpenAI, Azure AI Search ve diğer Azure hizmetleri ile yerel entegrasyon  
- Microsoft Entra ID üzerinden kurumsal kimlik doğrulama ve yetkilendirme  
- Özel araçlar, prompt şablonları ve kaynak bağlayıcıları desteği  
- Kurumsal güvenlik ve düzenleyici gereksinimlere uyum  

**Teknik Uygulama:**  
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

**Sonuçlar:**  
- Kurumsal AI projeleri için hazır, uyumlu MCP sunucu platformu sunarak değer elde etme süresini kısalttı  
- LLM’ler, araçlar ve kurumsal veri kaynaklarının entegrasyonunu kolaylaştırdı  
- MCP iş yükleri için güvenlik, gözlemlenebilirlik ve operasyonel verimliliği artırdı  

**Referanslar:**  
- [Azure MCP Dokümantasyonu](https://aka.ms/azmcp)  
- [Azure AI Hizmetleri](https://azure.microsoft.com/en-us/products/ai-services/)  

## Vaka Çalışması 6: NLWeb  
MCP (Model Context Protocol), sohbet botları ve AI asistanlarının araçlarla etkileşim kurması için ortaya çıkan bir protokoldür. Her NLWeb örneği aynı zamanda bir MCP sunucusudur ve tek bir temel yöntem olan ask’i destekler; bu yöntem bir web sitesine doğal dilde soru sormak için kullanılır. Dönen yanıt, web verilerini tanımlamak için yaygın kullanılan schema.org sözlüğünü kullanır. Basitçe söylemek gerekirse, MCP, NLWeb’in Http’nin HTML’ye karşılık gelmesi gibidir. NLWeb, protokolleri, Schema.org formatlarını ve örnek kodları birleştirerek sitelerin bu uç noktaları hızlıca oluşturmasına yardımcı olur; böylece insanlar için konuşma arayüzleri ve makineler için doğal ajanlar arası etkileşim sağlanır.

NLWeb’in iki ayrı bileşeni vardır.  
- Doğal dilde bir siteyle etkileşim için çok basit bir protokol ve dönen yanıt için json ve schema.org kullanan bir format. Daha fazla detay için REST API dokümantasyonuna bakınız.  
- (1) numaralı bileşenin basit bir uygulaması; ürünler, tarifler, gezilecek yerler, yorumlar gibi öğe listeleri olarak soyutlanabilen siteler için mevcut işaretlemeyi kullanır. Kullanıcı arayüzü widget seti ile birlikte, siteler içeriklerine kolayca konuşma arayüzleri sunabilir. Bu işleyişle ilgili daha fazla detay için Life of a chat query dokümantasyonuna bakınız.  

**Referanslar:**  
- [Azure MCP Dokümantasyonu](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)  

## Uygulamalı Projeler

### Proje 1: Çok Sağlayıcılı MCP Sunucusu Oluşturma

**Amaç:** Belirli kriterlere göre istekleri birden fazla AI model sağlayıcısına yönlendirebilen bir MCP sunucusu oluşturmak.

**Gereksinimler:**  
- En az üç farklı model sağlayıcısını desteklemek (örneğin OpenAI, Anthropic, yerel modeller)  
- İstek meta verilerine dayalı yönlendirme mekanizması uygulamak  
- Sağlayıcı kimlik bilgilerini yönetmek için yapılandırma sistemi oluşturmak  
- Performans ve maliyet optimizasyonu için önbellekleme eklemek  
- Kullanım izleme için basit bir kontrol paneli oluşturmak  

**Uygulama Adımları:**  
1. Temel MCP sunucu altyapısını kurmak  
2. Her AI model servisi için sağlayıcı adaptörlerini uygulamak  
3. İstek özelliklerine göre yönlendirme mantığını oluşturmak  
4. Sık istekler için önbellekleme mekanizmaları eklemek  
5. İzleme panelini geliştirmek  
6. Çeşitli istek desenleriyle test etmek  

**Teknolojiler:** Tercihinize göre Python (.NET/Java/Python), önbellekleme için Redis ve kontrol paneli için basit bir web framework.

### Proje 2: Kurumsal Prompt Yönetim Sistemi

**Amaç:** Kurum genelinde prompt şablonlarını yönetmek, sürümlemek ve dağıtmak için MCP tabanlı bir sistem geliştirmek.

**Gereksinimler:**  
- Prompt şablonları için merkezi bir depo oluşturmak  
- Sürümleme ve onay iş akışları uygulamak  
- Örnek girdilerle şablon test yetenekleri geliştirmek  
- Rol tabanlı erişim kontrolleri oluşturmak  
- Şablonların alınması ve dağıtımı için API sağlamak  

**Uygulama Adımları:**  
1. Şablon depolama için veri tabanı şeması tasarlamak  
2. Şablon CRUD işlemleri için temel API oluşturmak  
3. Sürümleme sistemini uygulamak  
4. Onay iş akışını geliştirmek  
5. Test çerçevesini oluşturmak  
6. Yönetim için basit bir web arayüzü geliştirmek  
7. MCP sunucusuyla entegrasyon sağlamak  

**Teknolojiler:** Tercih ettiğiniz backend framework, SQL veya NoSQL veri tabanı ve yönetim arayüzü için frontend framework.

### Proje 3: MCP Tabanlı İçerik Üretim Platformu

**Amaç:** MCP kullanarak farklı içerik türlerinde tutarlı sonuçlar sunan bir içerik üretim platformu oluşturmak.

**Gereksinimler:**  
- Birden fazla içerik formatını desteklemek (blog yazıları, sosyal medya, pazarlama metni)  
- Özelleştirme seçenekleri ile şablon tabanlı üretim uygulamak  
- İçerik inceleme ve geri bildirim sistemi oluşturmak  
- İçerik performans metriklerini takip etmek  
- İçerik sürümleme ve yineleme desteği sağlamak  

**Uygulama Adımları:**  
1. MCP istemci altyapısını kurmak  
2. Farklı içerik türleri için şablonlar oluşturmak  
3. İçerik üretim hattını inşa etmek  
4. İnceleme sistemini uygulamak  
5. Metrik takip sistemini geliştirmek  
6. Şablon yönetimi ve içerik üretimi için kullanıcı arayüzü oluşturmak  

**Teknolojiler:** Tercih ettiğiniz programlama dili, web framework ve veri tabanı sistemi.

## MCP Teknolojisi için Gelecek Yönelimleri

### Ortaya Çıkan Trendler

1. **Çok Modlu MCP**  
   - Görüntü, ses ve video modelleri ile etkileşimleri standartlaştırmak için MCP’nin genişletilmesi  
   - Modlar arası akıl yürütme yeteneklerinin geliştirilmesi  
   - Farklı modaliteler için standart prompt formatları  

2. **Federasyonlu MCP Altyapısı**  
   - Kuruluşlar arasında kaynak paylaşımı yapabilen dağıtık MCP ağları  
   - Güvenli model paylaşımı için standart protokoller  
   - Gizliliği koruyan hesaplama teknikleri  

3. **MCP Pazar Yerleri**  
   - MCP şablonları ve eklentilerinin paylaşımı ve ticarileştirilmesi için ekosistemler  
   - Kalite güvencesi ve sertifikasyon süreçleri  
   - Model pazar yerleri ile entegrasyon  

4. **Uç Bilişim için MCP**  
   - Kaynak kısıtlı uç cihazlar için MCP standartlarının uyarlanması  
   - Düşük bant genişliği ortamları için optimize protokoller  
   - IoT ekosistemleri için özel MCP uygulamaları  

5. **Düzenleyici Çerçeveler**  
   - Düzenleyici uyumluluk için MCP genişletmelerinin geliştirilmesi  
   - Standart denetim kayıtları ve açıklanabilirlik arayüzleri  
   - Ortaya çıkan AI yönetişim çerçeveleri ile entegrasyon  

### Microsoft’tan MCP Çözümleri

Microsoft ve Azure, geliştiricilerin farklı senaryolarda MCP uygulamalarını kolaylaştırmak için çeşitli açık kaynak depoları geliştirdi:

#### Microsoft Organizasyonu  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - Tarayıcı otomasyonu ve testi için Playwright MCP sunucusu  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - Yerel test ve topluluk katkısı için OneDrive MCP sunucu uygulaması  
3. [NLWeb](https://github.com/microsoft/NlWeb) - Açık protokoller ve ilişkili açık kaynak araçlar koleksiyonu; AI Web için temel katman oluşturma  

#### Azure-Samples Organizasyonu  
1. [mcp](https://github.com/Azure-Samples/mcp) - Azure üzerinde MCP sunucuları oluşturmak ve entegre etmek için örnekler, araçlar ve kaynaklar  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - Model Context Protocol spesifikasyonuyla kimlik doğrulama gösteren referans MCP sunucuları  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure Functions içinde Remote MCP Sunucu uygulamalarının ana sayfası ve dil bazlı bağlantılar  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure Functions ile Python kullanarak özel uzak MCP sunucuları oluşturma ve dağıtma için hızlı başlangıç şablonu  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - .NET/C# kullanarak Azure Functions ile uzak MCP sunucuları için hızlı başlangıç şablonu  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - TypeScript ile Azure Functions kullanarak uzak MCP sunucuları için hızlı başlangıç şablonu  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Python kullanarak Azure API Management ile Uzak MCP sunucularına AI Geçidi  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - MCP özelliklerini içeren APIM ❤️ AI deneyleri; Azure OpenAI ve AI Foundry entegrasyonu  

Bu depolar, Model Context Protocol ile çalışmak için farklı programlama dilleri ve Azure hizmetleri üzerinde çeşitli uygulamalar, şablonlar ve kaynaklar sağlar. Temel sunucu uygulamalarından kimlik doğrulama, bulut dağıtımı ve kurumsal entegrasyon senaryolarına kadar geniş bir kullanım alanını kapsar.

#### MCP Kaynaklar Dizini

Resmi Microsoft MCP deposundaki [MCP Resources dizini](https://github.com/microsoft/mcp/tree/main/Resources), Model Context Protocol sunucularında kullanılmak üzere örnek kaynaklar, prompt şablonları ve araç tanımlamalarından oluşan seçilmiş bir koleksiyon sunar. Bu dizin, geliştiricilerin MCP ile hızlıca başlamasına yardımcı olmak için yeniden kullanılabilir yapı taşları ve en iyi uygulama örnekleri sağlar:

- **Prompt Şablonları:** Yaygın AI görevleri ve senaryoları için kullanıma hazır prompt şablonları, kendi MCP sunucu uygulamalarınıza uyarlanabilir.  
- **Araç Tanımları:** Farklı MCP sunucularında araç entegrasyonu ve çağrısını standartlaştırmak için örnek araç şemaları ve meta veriler.  
- **Kaynak Örnekleri:** MCP çerçevesinde veri kaynakları, API’ler ve dış hizmetlerle bağlantı kurmak için örnek kaynak tanımları.  
- **Referans Uygulamalar:** Gerçek dünya MCP projelerinde kaynaklar, promptlar ve araçların nasıl yapılandırılıp organize edileceğini gösteren pratik örnekler.  

Bu kaynaklar geliştirmeyi hızlandırır, standartlaşmayı teş
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Egzersizler

1. Vaka çalışmalarından birini analiz edin ve alternatif bir uygulama yaklaşımı önerin.
2. Proje fikirlerinden birini seçin ve ayrıntılı bir teknik spesifikasyon oluşturun.
3. Vaka çalışmalarında yer almayan bir sektörü araştırın ve MCP'nin bu sektörün özel zorluklarını nasıl çözebileceğini özetleyin.
4. Gelecekteki yönlerden birini inceleyin ve bunu destekleyecek yeni bir MCP uzantısı için bir konsept oluşturun.

Sonraki: [Best Practices](../08-BestPractices/README.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorumlamalardan sorumlu değiliz.