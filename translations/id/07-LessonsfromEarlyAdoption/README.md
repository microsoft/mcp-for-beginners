<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:37:03+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "id"
}
-->
# Pelajaran dari Pengguna Awal

## Ikhtisar

Pelajaran ini membahas bagaimana pengguna awal memanfaatkan Model Context Protocol (MCP) untuk menyelesaikan tantangan dunia nyata dan mendorong inovasi di berbagai industri. Melalui studi kasus yang mendalam dan proyek langsung, Anda akan melihat bagaimana MCP memungkinkan integrasi AI yang standar, aman, dan skalabel—menghubungkan model bahasa besar, alat, dan data perusahaan dalam satu kerangka kerja terpadu. Anda akan mendapatkan pengalaman praktis dalam merancang dan membangun solusi berbasis MCP, belajar dari pola implementasi yang terbukti, dan menemukan praktik terbaik untuk menerapkan MCP di lingkungan produksi. Pelajaran ini juga menyoroti tren yang muncul, arah masa depan, dan sumber daya open-source untuk membantu Anda tetap berada di garis depan teknologi MCP dan ekosistemnya yang berkembang.

## Tujuan Pembelajaran

- Menganalisis implementasi MCP di dunia nyata di berbagai industri
- Merancang dan membangun aplikasi lengkap berbasis MCP
- Menjelajahi tren yang muncul dan arah masa depan dalam teknologi MCP
- Menerapkan praktik terbaik dalam skenario pengembangan nyata

## Implementasi MCP di Dunia Nyata

### Studi Kasus 1: Otomasi Dukungan Pelanggan Perusahaan

Sebuah perusahaan multinasional menerapkan solusi berbasis MCP untuk menstandarisasi interaksi AI di seluruh sistem dukungan pelanggan mereka. Ini memungkinkan mereka untuk:

- Membuat antarmuka terpadu untuk beberapa penyedia LLM
- Mempertahankan pengelolaan prompt yang konsisten di berbagai departemen
- Menerapkan kontrol keamanan dan kepatuhan yang kuat
- Dengan mudah beralih antar model AI berdasarkan kebutuhan spesifik

**Implementasi Teknis:**  
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

**Hasil:** Pengurangan biaya model sebesar 30%, peningkatan konsistensi respons sebesar 45%, dan peningkatan kepatuhan di seluruh operasi global.

### Studi Kasus 2: Asisten Diagnostik Kesehatan

Penyedia layanan kesehatan mengembangkan infrastruktur MCP untuk mengintegrasikan beberapa model AI medis khusus sambil memastikan data pasien yang sensitif tetap terlindungi:

- Peralihan mulus antara model medis umum dan spesialis
- Kontrol privasi ketat dan jejak audit
- Integrasi dengan sistem Electronic Health Record (EHR) yang ada
- Rekayasa prompt yang konsisten untuk terminologi medis

**Implementasi Teknis:**  
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

**Hasil:** Peningkatan saran diagnostik untuk dokter sambil mempertahankan kepatuhan penuh terhadap HIPAA dan pengurangan signifikan dalam pergantian konteks antar sistem.

### Studi Kasus 3: Analisis Risiko Layanan Keuangan

Sebuah institusi keuangan menerapkan MCP untuk menstandarisasi proses analisis risiko di berbagai departemen:

- Membuat antarmuka terpadu untuk model risiko kredit, deteksi penipuan, dan risiko investasi
- Menerapkan kontrol akses ketat dan versi model
- Memastikan auditabilitas semua rekomendasi AI
- Mempertahankan format data yang konsisten di berbagai sistem

**Implementasi Teknis:**  
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

**Hasil:** Peningkatan kepatuhan regulasi, siklus penerapan model 40% lebih cepat, dan konsistensi penilaian risiko yang lebih baik di seluruh departemen.

### Studi Kasus 4: Microsoft Playwright MCP Server untuk Otomasi Browser

Microsoft mengembangkan [Playwright MCP server](https://github.com/microsoft/playwright-mcp) untuk memungkinkan otomasi browser yang aman dan standar melalui Model Context Protocol. Solusi ini memungkinkan agen AI dan LLM berinteraksi dengan browser web secara terkontrol, dapat diaudit, dan dapat diperluas—mendukung kasus penggunaan seperti pengujian web otomatis, ekstraksi data, dan alur kerja ujung-ke-ujung.

- Menyediakan kemampuan otomasi browser (navigasi, pengisian formulir, tangkapan layar, dll.) sebagai alat MCP
- Menerapkan kontrol akses ketat dan sandboxing untuk mencegah tindakan tidak sah
- Menyediakan log audit terperinci untuk semua interaksi browser
- Mendukung integrasi dengan Azure OpenAI dan penyedia LLM lainnya untuk otomasi berbasis agen

**Implementasi Teknis:**  
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

**Hasil:**  
- Memungkinkan otomasi browser yang aman dan terprogram untuk agen AI dan LLM  
- Mengurangi usaha pengujian manual dan meningkatkan cakupan pengujian aplikasi web  
- Menyediakan kerangka kerja yang dapat digunakan kembali dan diperluas untuk integrasi alat berbasis browser di lingkungan perusahaan

**Referensi:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### Studi Kasus 5: Azure MCP – Model Context Protocol Enterprise-Grade sebagai Layanan

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) adalah implementasi MCP kelas enterprise yang dikelola oleh Microsoft, dirancang untuk menyediakan kemampuan server MCP yang skalabel, aman, dan patuh sebagai layanan cloud. Azure MCP memungkinkan organisasi untuk dengan cepat menerapkan, mengelola, dan mengintegrasikan server MCP dengan layanan Azure AI, data, dan keamanan, mengurangi beban operasional dan mempercepat adopsi AI.

- Hosting server MCP yang sepenuhnya dikelola dengan skalabilitas, pemantauan, dan keamanan bawaan
- Integrasi native dengan Azure OpenAI, Azure AI Search, dan layanan Azure lainnya
- Otentikasi dan otorisasi perusahaan melalui Microsoft Entra ID
- Dukungan untuk alat kustom, template prompt, dan konektor sumber daya
- Kepatuhan dengan persyaratan keamanan dan regulasi perusahaan

**Implementasi Teknis:**  
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

**Hasil:**  
- Mengurangi waktu pencapaian nilai untuk proyek AI perusahaan dengan menyediakan platform server MCP yang siap pakai dan patuh  
- Menyederhanakan integrasi LLM, alat, dan sumber data perusahaan  
- Meningkatkan keamanan, observabilitas, dan efisiensi operasional untuk beban kerja MCP  

**Referensi:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## Studi Kasus 6: NLWeb  
MCP (Model Context Protocol) adalah protokol yang sedang berkembang untuk chatbot dan asisten AI berinteraksi dengan alat. Setiap instance NLWeb juga merupakan server MCP, yang mendukung satu metode inti, ask, yang digunakan untuk mengajukan pertanyaan ke situs web dalam bahasa alami. Respons yang dikembalikan menggunakan schema.org, kosakata yang banyak digunakan untuk mendeskripsikan data web. Secara sederhana, MCP adalah NLWeb seperti Http terhadap HTML. NLWeb menggabungkan protokol, format Schema.org, dan kode contoh untuk membantu situs dengan cepat membuat endpoint ini, memberikan manfaat bagi manusia melalui antarmuka percakapan dan mesin melalui interaksi agen-ke-agen yang alami.

Ada dua komponen berbeda dalam NLWeb.  
- Sebuah protokol, sangat sederhana untuk memulai, untuk berinteraksi dengan situs dalam bahasa alami dan format, memanfaatkan json dan schema.org untuk jawaban yang dikembalikan. Lihat dokumentasi API REST untuk detail lebih lanjut.  
- Implementasi sederhana dari (1) yang memanfaatkan markup yang ada, untuk situs yang dapat diabstraksi sebagai daftar item (produk, resep, atraksi, ulasan, dll.). Bersama dengan seperangkat widget antarmuka pengguna, situs dapat dengan mudah menyediakan antarmuka percakapan untuk kontennya. Lihat dokumentasi Life of a chat query untuk detail lebih lanjut tentang cara kerjanya.

**Referensi:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## Proyek Praktik

### Proyek 1: Membangun Server MCP Multi-Penyedia

**Tujuan:** Membuat server MCP yang dapat mengarahkan permintaan ke beberapa penyedia model AI berdasarkan kriteria tertentu.

**Persyaratan:**  
- Mendukung setidaknya tiga penyedia model berbeda (misalnya, OpenAI, Anthropic, model lokal)  
- Menerapkan mekanisme routing berdasarkan metadata permintaan  
- Membuat sistem konfigurasi untuk mengelola kredensial penyedia  
- Menambahkan caching untuk mengoptimalkan performa dan biaya  
- Membangun dashboard sederhana untuk memantau penggunaan

**Langkah Implementasi:**  
1. Menyiapkan infrastruktur server MCP dasar  
2. Mengimplementasikan adapter penyedia untuk setiap layanan model AI  
3. Membuat logika routing berdasarkan atribut permintaan  
4. Menambahkan mekanisme caching untuk permintaan yang sering  
5. Mengembangkan dashboard pemantauan  
6. Menguji dengan berbagai pola permintaan

**Teknologi:** Pilih dari Python (.NET/Java/Python sesuai preferensi Anda), Redis untuk caching, dan framework web sederhana untuk dashboard.

### Proyek 2: Sistem Manajemen Prompt Perusahaan

**Tujuan:** Mengembangkan sistem berbasis MCP untuk mengelola, melakukan versioning, dan menerapkan template prompt di seluruh organisasi.

**Persyaratan:**  
- Membuat repositori terpusat untuk template prompt  
- Menerapkan versioning dan alur kerja persetujuan  
- Membangun kemampuan pengujian template dengan input contoh  
- Mengembangkan kontrol akses berbasis peran  
- Membuat API untuk pengambilan dan penerapan template

**Langkah Implementasi:**  
1. Merancang skema database untuk penyimpanan template  
2. Membuat API inti untuk operasi CRUD template  
3. Mengimplementasikan sistem versioning  
4. Membangun alur kerja persetujuan  
5. Mengembangkan kerangka pengujian  
6. Membuat antarmuka web sederhana untuk manajemen  
7. Mengintegrasikan dengan server MCP

**Teknologi:** Pilih framework backend, basis data SQL atau NoSQL, dan framework frontend untuk antarmuka manajemen sesuai pilihan Anda.

### Proyek 3: Platform Pembuatan Konten Berbasis MCP

**Tujuan:** Membangun platform pembuatan konten yang memanfaatkan MCP untuk memberikan hasil yang konsisten di berbagai jenis konten.

**Persyaratan:**  
- Mendukung berbagai format konten (posting blog, media sosial, salinan pemasaran)  
- Menerapkan pembuatan berbasis template dengan opsi kustomisasi  
- Membuat sistem tinjau dan umpan balik konten  
- Melacak metrik performa konten  
- Mendukung versioning dan iterasi konten

**Langkah Implementasi:**  
1. Menyiapkan infrastruktur klien MCP  
2. Membuat template untuk berbagai jenis konten  
3. Membangun pipeline pembuatan konten  
4. Mengimplementasikan sistem tinjauan  
5. Mengembangkan sistem pelacakan metrik  
6. Membuat antarmuka pengguna untuk manajemen template dan pembuatan konten

**Teknologi:** Bahasa pemrograman, framework web, dan sistem basis data pilihan Anda.

## Arah Masa Depan Teknologi MCP

### Tren yang Muncul

1. **MCP Multi-Modal**  
   - Perluasan MCP untuk menstandarisasi interaksi dengan model gambar, audio, dan video  
   - Pengembangan kemampuan penalaran lintas modalitas  
   - Format prompt standar untuk berbagai modalitas

2. **Infrastruktur MCP Terdistribusi**  
   - Jaringan MCP terdistribusi yang dapat berbagi sumber daya antar organisasi  
   - Protokol standar untuk berbagi model secara aman  
   - Teknik komputasi yang menjaga privasi

3. **Pasar MCP**  
   - Ekosistem untuk berbagi dan memonetisasi template dan plugin MCP  
   - Proses jaminan kualitas dan sertifikasi  
   - Integrasi dengan pasar model

4. **MCP untuk Edge Computing**  
   - Adaptasi standar MCP untuk perangkat edge dengan sumber daya terbatas  
   - Protokol yang dioptimalkan untuk lingkungan dengan bandwidth rendah  
   - Implementasi MCP khusus untuk ekosistem IoT

5. **Kerangka Regulasi**  
   - Pengembangan ekstensi MCP untuk kepatuhan regulasi  
   - Jejak audit standar dan antarmuka penjelasan  
   - Integrasi dengan kerangka tata kelola AI yang sedang berkembang

### Solusi MCP dari Microsoft

Microsoft dan Azure telah mengembangkan beberapa repositori open-source untuk membantu pengembang menerapkan MCP dalam berbagai skenario:

#### Organisasi Microsoft  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - Server Playwright MCP untuk otomasi dan pengujian browser  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - Implementasi server MCP OneDrive untuk pengujian lokal dan kontribusi komunitas  
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWeb adalah kumpulan protokol terbuka dan alat open source terkait. Fokus utamanya adalah membangun lapisan dasar untuk AI Web

#### Organisasi Azure-Samples  
1. [mcp](https://github.com/Azure-Samples/mcp) - Tautan ke contoh, alat, dan sumber daya untuk membangun dan mengintegrasikan server MCP di Azure dengan berbagai bahasa pemrograman  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - Server MCP referensi yang menunjukkan otentikasi dengan spesifikasi Model Context Protocol saat ini  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Halaman landing untuk implementasi Remote MCP Server di Azure Functions dengan tautan ke repositori bahasa spesifik  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Template quickstart untuk membangun dan menerapkan server MCP remote kustom menggunakan Azure Functions dengan Python  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Template quickstart untuk membangun dan menerapkan server MCP remote kustom menggunakan Azure Functions dengan .NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Template quickstart untuk membangun dan menerapkan server MCP remote kustom menggunakan Azure Functions dengan TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Azure API Management sebagai AI Gateway ke server MCP remote menggunakan Python  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - Eksperimen APIM ❤️ AI termasuk kemampuan MCP, integrasi dengan Azure OpenAI dan AI Foundry

Repositori ini menyediakan berbagai implementasi, template, dan sumber daya untuk bekerja dengan Model Context Protocol di berbagai bahasa pemrograman dan layanan Azure. Mereka mencakup beragam kasus penggunaan mulai dari implementasi server dasar hingga otentikasi, penerapan cloud, dan skenario integrasi perusahaan.

#### Direktori Sumber Daya MCP

Direktori [MCP Resources](https://github.com/microsoft/mcp/tree/main/Resources) di repositori resmi Microsoft MCP menyediakan kumpulan sumber daya contoh, template prompt, dan definisi alat yang dikurasi untuk digunakan dengan server Model Context Protocol. Direktori ini dirancang untuk membantu pengembang memulai dengan cepat menggunakan MCP dengan menawarkan blok bangunan yang dapat digunakan ulang dan contoh praktik terbaik untuk:

- **Template Prompt:** Template prompt siap pakai untuk tugas dan skenario AI umum, yang dapat disesuaikan untuk implementasi server MCP Anda sendiri.  
- **Definisi Alat:** Skema alat contoh dan metadata untuk menstandarisasi integrasi dan pemanggilan alat di berbagai server MCP.  
- **Contoh Sumber Daya:** Definisi sumber daya contoh untuk menghubungkan ke sumber data, API, dan layanan eksternal dalam kerangka kerja MCP.  
- **Implementasi Referensi:** Contoh praktis yang menunjukkan cara menyusun dan mengorganisasi sumber daya, prompt, dan alat dalam proyek MCP dunia nyata.

Sumber daya ini mempercepat pengembangan, mendorong standarisasi, dan membantu memastikan praktik terbaik saat membangun dan menerapkan solusi berbasis MCP.

#### Direktori Sumber Daya MCP  
- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)

### Peluang Riset

- Teknik optimasi prompt yang efisien dalam kerangka MCP  
- Model keamanan untuk penerapan MCP multi-penyewa  
- Benchmark performa di berbagai implementasi MCP  
- Metode verifikasi formal untuk server MCP

## Kesimpulan

Model Context Protocol (MCP) dengan cepat membentuk masa depan integrasi AI yang standar, aman, dan interoperabel di berbagai industri. Melalui studi kasus dan proyek langsung dalam pelajaran ini, Anda telah melihat bagaimana pengguna awal—termasuk Microsoft dan Azure—memanfaatkan MCP untuk menyelesaikan tantangan dunia nyata, mempercepat adopsi AI, dan memastikan kepatuhan, keamanan, serta skalabilitas. Pendekatan modular MCP memungkinkan organisasi menghubungkan model bahasa besar, alat, dan data perusahaan dalam kerangka kerja yang terpadu dan dapat diaudit. Seiring MCP terus berkembang, tetap terlibat dengan komunitas, menjelajahi sumber daya open-source, dan menerapkan praktik terbaik akan menjadi kunci untuk membangun solusi AI yang kuat dan siap masa depan.

## Sumber Daya Tambahan

- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)  
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)  
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
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

## Latihan

1. Analisis salah satu studi kasus dan usulkan pendekatan implementasi alternatif.
2. Pilih salah satu ide proyek dan buat spesifikasi teknis yang rinci.
3. Teliti sebuah industri yang tidak tercakup dalam studi kasus dan jelaskan bagaimana MCP dapat mengatasi tantangan spesifiknya.
4. Jelajahi salah satu arah masa depan dan buat konsep untuk ekstensi MCP baru yang mendukungnya.

Selanjutnya: [Best Practices](../08-BestPractices/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.