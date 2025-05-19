<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:25:06+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "th"
}
-->
# บทเรียนจากผู้ใช้งานรุ่นแรก

## ภาพรวม

บทเรียนนี้สำรวจวิธีที่ผู้ใช้งานรุ่นแรกได้นำ Model Context Protocol (MCP) มาใช้แก้ไขปัญหาในโลกจริงและขับเคลื่อนนวัตกรรมในหลากหลายอุตสาหกรรม ผ่านกรณีศึกษาละเอียดและโปรเจกต์ลงมือทำ คุณจะเห็นว่า MCP ช่วยให้การรวม AI ที่ได้มาตรฐาน ปลอดภัย และขยายตัวได้ง่าย — โดยเชื่อมต่อโมเดลภาษาขนาดใหญ่ เครื่องมือ และข้อมูลขององค์กรในกรอบงานเดียวกัน คุณจะได้รับประสบการณ์จริงในการออกแบบและสร้างโซลูชันที่ใช้ MCP เรียนรู้รูปแบบการใช้งานที่พิสูจน์แล้ว และค้นพบแนวทางปฏิบัติที่ดีที่สุดสำหรับการนำ MCP ไปใช้ในสภาพแวดล้อมการผลิต บทเรียนยังเน้นถึงแนวโน้มใหม่ ทิศทางในอนาคต และแหล่งข้อมูลโอเพนซอร์สที่จะช่วยให้คุณก้าวนำเทคโนโลยี MCP และระบบนิเวศที่กำลังพัฒนา

## วัตถุประสงค์การเรียนรู้

- วิเคราะห์การใช้งาน MCP ในโลกจริงในหลากหลายอุตสาหกรรม
- ออกแบบและสร้างแอปพลิเคชันที่ใช้ MCP ครบวงจร
- สำรวจแนวโน้มใหม่และทิศทางในอนาคตของเทคโนโลยี MCP
- นำแนวทางปฏิบัติที่ดีที่สุดไปใช้ในสถานการณ์พัฒนาจริง

## การใช้งาน MCP ในโลกจริง

### กรณีศึกษา 1: ระบบอัตโนมัติสำหรับฝ่ายสนับสนุนลูกค้าองค์กร

บริษัทข้ามชาติได้ใช้โซลูชันที่ใช้ MCP เพื่อสร้างมาตรฐานการสื่อสาร AI ในระบบสนับสนุนลูกค้าของพวกเขา ทำให้สามารถ:

- สร้างอินเทอร์เฟซรวมสำหรับผู้ให้บริการ LLM หลายราย
- รักษาการจัดการ prompt ให้สอดคล้องกันในทุกแผนก
- ใช้มาตรการรักษาความปลอดภัยและการปฏิบัติตามข้อกำหนดอย่างเข้มงวด
- สลับใช้โมเดล AI ต่างๆ ได้อย่างง่ายดายตามความต้องการเฉพาะ

**การใช้งานเชิงเทคนิค:**  
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

**ผลลัพธ์:** ลดต้นทุนโมเดลลง 30% ปรับปรุงความสม่ำเสมอของการตอบกลับ 45% และเสริมสร้างการปฏิบัติตามข้อกำหนดทั่วโลก

### กรณีศึกษา 2: ผู้ช่วยวินิจฉัยทางการแพทย์

ผู้ให้บริการด้านสุขภาพได้พัฒนาโครงสร้างพื้นฐาน MCP เพื่อรวมโมเดล AI ทางการแพทย์เฉพาะทางหลายตัว พร้อมกับรักษาข้อมูลผู้ป่วยที่ละเอียดอ่อนให้ปลอดภัย:

- สลับใช้โมเดลทางการแพทย์ทั่วไปและเฉพาะทางได้อย่างราบรื่น
- ควบคุมความเป็นส่วนตัวอย่างเข้มงวดและมีบันทึกตรวจสอบ
- รวมกับระบบบันทึกสุขภาพอิเล็กทรอนิกส์ (EHR) ที่มีอยู่
- การจัดการ prompt ที่สอดคล้องกับคำศัพท์ทางการแพทย์

**การใช้งานเชิงเทคนิค:**  
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

**ผลลัพธ์:** เพิ่มประสิทธิภาพคำแนะนำวินิจฉัยสำหรับแพทย์ ในขณะที่รักษาการปฏิบัติตาม HIPAA อย่างเต็มที่ และลดการสลับบริบทระหว่างระบบอย่างมาก

### กรณีศึกษา 3: การวิเคราะห์ความเสี่ยงทางการเงิน

สถาบันการเงินได้นำ MCP มาใช้เพื่อมาตรฐานกระบวนการวิเคราะห์ความเสี่ยงในหลายแผนก:

- สร้างอินเทอร์เฟซรวมสำหรับโมเดลความเสี่ยงเครดิต ตรวจจับการทุจริต และความเสี่ยงการลงทุน
- ใช้มาตรการควบคุมการเข้าถึงและการจัดการเวอร์ชันโมเดลอย่างเข้มงวด
- รับประกันความสามารถในการตรวจสอบคำแนะนำ AI ทุกข้อ
- รักษารูปแบบข้อมูลที่สอดคล้องกันในระบบที่หลากหลาย

**การใช้งานเชิงเทคนิค:**  
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

**ผลลัพธ์:** เพิ่มความสอดคล้องกับกฎระเบียบ เร่งรอบการปรับใช้โมเดลเร็วขึ้น 40% และปรับปรุงความสม่ำเสมอของการประเมินความเสี่ยงในทุกแผนก

### กรณีศึกษา 4: Microsoft Playwright MCP Server สำหรับการอัตโนมัติเบราว์เซอร์

Microsoft พัฒนา [Playwright MCP server](https://github.com/microsoft/playwright-mcp) เพื่อเปิดใช้งานการอัตโนมัติเบราว์เซอร์ที่ปลอดภัยและเป็นมาตรฐานผ่าน Model Context Protocol โซลูชันนี้ช่วยให้ AI agent และ LLMs สามารถโต้ตอบกับเว็บเบราว์เซอร์ได้อย่างควบคุม ตรวจสอบได้ และขยายได้ — รองรับการใช้งานเช่น การทดสอบเว็บอัตโนมัติ การดึงข้อมูล และเวิร์กโฟลว์แบบครบวงจร

- เปิดเผยความสามารถในการอัตโนมัติของเบราว์เซอร์ (การนำทาง กรอกแบบฟอร์ม ถ่ายภาพหน้าจอ ฯลฯ) ในรูปแบบเครื่องมือ MCP
- ใช้มาตรการควบคุมการเข้าถึงและ sandboxing อย่างเข้มงวดเพื่อป้องกันการกระทำที่ไม่ได้รับอนุญาต
- จัดทำบันทึกตรวจสอบอย่างละเอียดสำหรับการโต้ตอบกับเบราว์เซอร์ทั้งหมด
- รองรับการรวมกับ Azure OpenAI และผู้ให้บริการ LLM อื่นๆ สำหรับการอัตโนมัติที่ขับเคลื่อนโดย agent

**การใช้งานเชิงเทคนิค:**  
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

**ผลลัพธ์:**  
- เปิดใช้งานการอัตโนมัติเบราว์เซอร์แบบปลอดภัยและโปรแกรมสำหรับ AI agent และ LLMs  
- ลดความพยายามในการทดสอบด้วยมือและเพิ่มความครอบคลุมของการทดสอบเว็บแอปพลิเคชัน  
- มอบกรอบงานที่นำกลับมาใช้ใหม่และขยายได้สำหรับการรวมเครื่องมือที่ใช้เบราว์เซอร์ในสภาพแวดล้อมองค์กร  

**เอกสารอ้างอิง:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### กรณีศึกษา 5: Azure MCP – Model Context Protocol ระดับองค์กรในรูปแบบบริการ

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) คือการใช้งาน Model Context Protocol ระดับองค์กรที่ Microsoft บริหารจัดการในรูปแบบบริการคลาวด์ที่มีความสามารถในการปรับขนาด ปลอดภัย และปฏิบัติตามข้อกำหนด Azure MCP ช่วยให้องค์กรสามารถปรับใช้ จัดการ และรวม MCP server เข้ากับ Azure AI, ข้อมูล และบริการด้านความปลอดภัยได้อย่างรวดเร็ว ลดภาระงานและเร่งการนำ AI มาใช้

- บริการโฮสต์ MCP server ที่บริหารจัดการเต็มรูปแบบ พร้อมการปรับขนาด การตรวจสอบ และความปลอดภัยในตัว
- การรวมระบบแบบเนทีฟกับ Azure OpenAI, Azure AI Search และบริการ Azure อื่นๆ
- ระบบยืนยันตัวตนและอนุญาตระดับองค์กรผ่าน Microsoft Entra ID
- รองรับเครื่องมือแบบกำหนดเอง, เทมเพลต prompt และตัวเชื่อมต่อทรัพยากร
- ปฏิบัติตามมาตรฐานความปลอดภัยและข้อกำหนดขององค์กร

**การใช้งานเชิงเทคนิค:**  
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

**ผลลัพธ์:**  
- ลดระยะเวลาสู่การใช้งานสำหรับโครงการ AI ระดับองค์กรด้วยการให้แพลตฟอร์ม MCP server ที่พร้อมใช้งานและปฏิบัติตามข้อกำหนด  
- ทำให้ง่ายต่อการรวม LLMs, เครื่องมือ และแหล่งข้อมูลขององค์กร  
- เสริมความปลอดภัย การสังเกตการณ์ และประสิทธิภาพการปฏิบัติงานสำหรับงาน MCP  

**เอกสารอ้างอิง:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## กรณีศึกษา 6: NLWeb  
MCP (Model Context Protocol) เป็นโปรโตคอลที่เกิดขึ้นใหม่สำหรับแชทบอทและผู้ช่วย AI ในการโต้ตอบกับเครื่องมือ ทุกอินสแตนซ์ของ NLWeb ก็เป็น MCP server ที่รองรับเมธอดหลักหนึ่งตัวคือ ask ซึ่งใช้ถามเว็บไซต์เป็นภาษาธรรมชาติ คำตอบที่ส่งกลับใช้ schema.org ซึ่งเป็นคำศัพท์ที่ใช้กันอย่างแพร่หลายสำหรับการอธิบายข้อมูลเว็บ โดยเปรียบเทียบง่ายๆ MCP ก็คือ NLWeb เหมือนกับ Http ที่เป็น HTML NLWeb รวมโปรโตคอล รูปแบบ Schema.org และโค้ดตัวอย่างเพื่อช่วยให้เว็บไซต์สร้างจุดเชื่อมต่อเหล่านี้ได้อย่างรวดเร็ว ให้ประโยชน์ทั้งกับมนุษย์ผ่านอินเทอร์เฟซสนทนา และกับเครื่องจักรผ่านการโต้ตอบแบบ agent-to-agent ที่เป็นธรรมชาติ

NLWeb มีส่วนประกอบหลักสองอย่าง  
- โปรโตคอลที่เรียบง่ายสำหรับเริ่มต้น ใช้เชื่อมต่อกับไซต์ในภาษาธรรมชาติ และรูปแบบที่ใช้ json และ schema.org สำหรับคำตอบ ดูเอกสาร REST API เพื่อรายละเอียดเพิ่มเติม  
- การใช้งานที่ตรงไปตรงมาของข้อ (1) ที่ใช้ประโยชน์จาก markup ที่มีอยู่ สำหรับไซต์ที่สามารถสรุปเป็นรายการของรายการ (สินค้า สูตรอาหาร สถานที่ท่องเที่ยว รีวิว ฯลฯ) ร่วมกับชุดวิดเจ็ตอินเทอร์เฟซผู้ใช้ ทำให้ไซต์สามารถให้บริการอินเทอร์เฟซสนทนาแก่เนื้อหาได้อย่างง่ายดาย ดูเอกสาร Life of a chat query เพื่อดูรายละเอียดวิธีการทำงาน

**เอกสารอ้างอิง:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## โปรเจกต์ลงมือทำ

### โปรเจกต์ 1: สร้าง MCP Server ที่รองรับผู้ให้บริการหลายราย

**วัตถุประสงค์:** สร้าง MCP server ที่สามารถส่งคำขอไปยังผู้ให้บริการโมเดล AI หลายรายตามเกณฑ์เฉพาะ

**ข้อกำหนด:**  
- รองรับผู้ให้บริการโมเดลอย่างน้อยสามราย (เช่น OpenAI, Anthropic, โมเดลภายใน)  
- ใช้กลไกการกำหนดเส้นทางตามข้อมูลเมตาของคำขอ  
- สร้างระบบกำหนดค่าสำหรับจัดการข้อมูลรับรองของผู้ให้บริการ  
- เพิ่มการแคชเพื่อเพิ่มประสิทธิภาพและลดต้นทุน  
- สร้างแดชบอร์ดง่ายๆ สำหรับตรวจสอบการใช้งาน

**ขั้นตอนการใช้งาน:**  
1. ตั้งค่าโครงสร้างพื้นฐาน MCP server เบื้องต้น  
2. สร้างตัวปรับแต่งผู้ให้บริการสำหรับแต่ละบริการโมเดล AI  
3. สร้างตรรกะการกำหนดเส้นทางตามคุณลักษณะคำขอ  
4. เพิ่มกลไกแคชสำหรับคำขอบ่อย  
5. พัฒนาแดชบอร์ดตรวจสอบ  
6. ทดสอบด้วยรูปแบบคำขอต่างๆ

**เทคโนโลยี:** เลือกใช้ Python (.NET/Java/Python ตามความชอบ), Redis สำหรับแคช และเว็บเฟรมเวิร์กง่ายๆ สำหรับแดชบอร์ด

### โปรเจกต์ 2: ระบบจัดการ Prompt ระดับองค์กร

**วัตถุประสงค์:** พัฒนาระบบที่ใช้ MCP สำหรับจัดการ การควบคุมเวอร์ชัน และปรับใช้เทมเพลต prompt ในองค์กร

**ข้อกำหนด:**  
- สร้างคลังเก็บเทมเพลต prompt แบบศูนย์กลาง  
- ใช้ระบบควบคุมเวอร์ชันและเวิร์กโฟลว์การอนุมัติ  
- สร้างความสามารถทดสอบเทมเพลตด้วยข้อมูลตัวอย่าง  
- พัฒนาการควบคุมการเข้าถึงตามบทบาท  
- สร้าง API สำหรับดึงและปรับใช้เทมเพลต

**ขั้นตอนการใช้งาน:**  
1. ออกแบบสคีมาฐานข้อมูลสำหรับเก็บเทมเพลต  
2. สร้าง API หลักสำหรับ CRUD เทมเพลต  
3. ใช้ระบบควบคุมเวอร์ชัน  
4. สร้างเวิร์กโฟลว์การอนุมัติ  
5. พัฒนากรอบทดสอบ  
6. สร้างอินเทอร์เฟซเว็บง่ายๆ สำหรับการจัดการ  
7. รวมระบบเข้ากับ MCP server

**เทคโนโลยี:** เลือกเฟรมเวิร์กแบ็กเอนด์ ฐานข้อมูล SQL หรือ NoSQL และเฟรมเวิร์กฟรอนต์เอนด์ตามต้องการ

### โปรเจกต์ 3: แพลตฟอร์มสร้างเนื้อหาที่ใช้ MCP

**วัตถุประสงค์:** สร้างแพลตฟอร์มสร้างเนื้อหาที่ใช้ MCP เพื่อให้ผลลัพธ์ที่สม่ำเสมอในเนื้อหาหลากหลายประเภท

**ข้อกำหนด:**  
- รองรับหลายรูปแบบเนื้อหา (บทความบล็อก โซเชียลมีเดีย คัดลอกการตลาด)  
- ใช้การสร้างตามเทมเพลตพร้อมตัวเลือกปรับแต่ง  
- สร้างระบบรีวิวและข้อเสนอแนะเนื้อหา  
- ติดตามตัวชี้วัดประสิทธิภาพเนื้อหา  
- รองรับการควบคุมเวอร์ชันและการปรับปรุงเนื้อหา

**ขั้นตอนการใช้งาน:**  
1. ตั้งค่าโครงสร้างพื้นฐาน MCP client  
2. สร้างเทมเพลตสำหรับเนื้อหาประเภทต่างๆ  
3. สร้างสายงานการสร้างเนื้อหา  
4. ใช้ระบบรีวิว  
5. พัฒนาระบบติดตามตัวชี้วัด  
6. สร้างอินเทอร์เฟซผู้ใช้สำหรับจัดการเทมเพลตและสร้างเนื้อหา

**เทคโนโลยี:** เลือกภาษาการเขียนโปรแกรม เว็บเฟรมเวิร์ก และระบบฐานข้อมูลตามชอบ

## ทิศทางในอนาคตของเทคโนโลยี MCP

### แนวโน้มใหม่

1. **Multi-Modal MCP**  
   - ขยาย MCP เพื่อมาตรฐานการโต้ตอบกับโมเดลภาพ เสียง และวิดีโอ  
   - พัฒนาความสามารถในการวิเคราะห์ข้ามโมดัล  
   - รูปแบบ prompt ที่ได้มาตรฐานสำหรับโมดัลต่างๆ

2. **โครงสร้างพื้นฐาน MCP แบบกระจาย**  
   - เครือข่าย MCP แบบกระจายที่สามารถแชร์ทรัพยากรข้ามองค์กร  
   - โปรโตคอลมาตรฐานสำหรับการแชร์โมเดลอย่างปลอดภัย  
   - เทคนิคการคำนวณที่รักษาความเป็นส่วนตัว

3. **ตลาด MCP**  
   - ระบบนิเวศสำหรับแชร์และสร้างรายได้จากเทมเพลตและปลั๊กอิน MCP  
   - กระบวนการรับรองคุณภาพและการรับรอง  
   - การรวมกับตลาดโมเดล

4. **MCP สำหรับ Edge Computing**  
   - ปรับมาตรฐาน MCP สำหรับอุปกรณ์ edge ที่มีทรัพยากรจำกัด  
   - โปรโตคอลที่ปรับให้เหมาะสมกับสภาพแวดล้อมแบนด์วิดท์ต่ำ  
   - การใช้งาน MCP เฉพาะสำหรับระบบ IoT

5. **กรอบกฎหมายและข้อบังคับ**  
   - พัฒนา MCP ขยายเพื่อรองรับการปฏิบัติตามกฎระเบียบ  
   - บันทึกตรวจสอบและอินเทอร์เฟซอธิบายผลที่ได้มาตรฐาน  
   - การรวมกับกรอบการกำกับดูแล AI ที่กำลังเกิดขึ้น

### โซลูชัน MCP จาก Microsoft

Microsoft และ Azure ได้พัฒนาคลังโอเพนซอร์สหลายแห่งเพื่อช่วยนักพัฒนาใช้งาน MCP ในสถานการณ์ต่างๆ:

#### Microsoft Organization  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - Playwright MCP server สำหรับการอัตโนมัติและทดสอบเบราว์เซอร์  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - การใช้งาน OneDrive MCP server สำหรับการทดสอบในเครื่องและการมีส่วนร่วมของชุมชน  
3. [NLWeb](https://github.com/microsoft/NlWeb) - ชุดโปรโตคอลเปิดและเครื่องมือโอเพนซอร์สที่เกี่ยวข้อง มุ่งเน้นการสร้างชั้นพื้นฐานสำหรับ AI Web  

#### Azure-Samples Organization  
1. [mcp](https://github.com/Azure-Samples/mcp) - ลิงก์ไปยังตัวอย่าง เครื่องมือ และทรัพยากรสำหรับสร้างและรวม MCP server บน Azure ด้วยหลายภาษา  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - ตัวอย่าง MCP server ที่แสดงการยืนยันตัวตนตามสเปค Model Context Protocol ปัจจุบัน  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)  
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)  
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)  
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)  
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## แบบฝึกหัด

1. วิเคราะห์หนึ่งในกรณีศึกษาและเสนอแนวทางการดำเนินงานทางเลือก  
2. เลือกหนึ่งในไอเดียโครงการและจัดทำข้อกำหนดทางเทคนิคอย่างละเอียด  
3. ศึกษาอุตสาหกรรมที่ไม่ได้รวมอยู่ในกรณีศึกษาและสรุปว่า MCP จะช่วยแก้ไขปัญหาเฉพาะของอุตสาหกรรมนั้นได้อย่างไร  
4. สำรวจหนึ่งในทิศทางอนาคตและสร้างแนวคิดสำหรับส่วนขยาย MCP ใหม่เพื่อรองรับทิศทางนั้น  

ถัดไป: [Best Practices](../08-BestPractices/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้