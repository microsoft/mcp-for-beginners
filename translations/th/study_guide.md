# คู่มือการศึกษา - Model Context Protocol (MCP) สำหรับผู้เริ่มต้น

คู่มือการศึกษานี้ให้ภาพรวมเกี่ยวกับโครงสร้างและเนื้อหาของที่เก็บข้อมูลสำหรับหลักสูตร "Model Context Protocol (MCP) สำหรับผู้เริ่มต้น" ใช้คู่มือนี้เพื่อสำรวจที่เก็บข้อมูลอย่างมีประสิทธิภาพและใช้ทรัพยากรที่มีอยู่ให้เกิดประโยชน์สูงสุด

## ภาพรวมของที่เก็บข้อมูล

Model Context Protocol (MCP) เป็นกรอบมาตรฐานสำหรับการโต้ตอบระหว่างโมเดล AI และแอปพลิเคชันของลูกค้า ซึ่งในตอนแรกถูกสร้างขึ้นโดย Anthropic และปัจจุบันได้รับการดูแลโดยชุมชน MCP ผ่านองค์กร GitHub อย่างเป็นทางการ ที่เก็บข้อมูลนี้มีหลักสูตรที่ครอบคลุมพร้อมตัวอย่างโค้ดที่สามารถทดลองได้ในภาษา C#, Java, JavaScript, Python และ TypeScript ซึ่งออกแบบมาสำหรับนักพัฒนา AI สถาปนิกระบบ และวิศวกรซอฟต์แวร์

## แผนภาพหลักสูตร

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```


## โครงสร้างที่เก็บข้อมูล

ที่เก็บข้อมูลนี้แบ่งออกเป็น 11 ส่วนหลัก โดยแต่ละส่วนมุ่งเน้นไปที่แง่มุมต่าง ๆ ของ MCP:

1. **บทนำ (00-Introduction/)**
   - ภาพรวมของ Model Context Protocol
   - เหตุผลที่การสร้างมาตรฐานมีความสำคัญในกระบวนการ AI
   - กรณีการใช้งานและประโยชน์ในทางปฏิบัติ

2. **แนวคิดหลัก (01-CoreConcepts/)**
   - สถาปัตยกรรมแบบไคลเอนต์-เซิร์ฟเวอร์
   - องค์ประกอบสำคัญของโปรโตคอล
   - รูปแบบการส่งข้อความใน MCP

3. **ความปลอดภัย (02-Security/)**
   - ภัยคุกคามด้านความปลอดภัยในระบบที่ใช้ MCP
   - แนวทางปฏิบัติที่ดีที่สุดในการรักษาความปลอดภัย
   - กลยุทธ์การตรวจสอบสิทธิ์และการอนุญาต
   - **เอกสารความปลอดภัยที่ครอบคลุม**:
     - MCP Security Best Practices 2025
     - Azure Content Safety Implementation Guide
     - MCP Security Controls and Techniques
     - MCP Best Practices Quick Reference
   - **หัวข้อสำคัญด้านความปลอดภัย**:
     - การโจมตีด้วยการฉีดคำสั่งและการปนเปื้อนเครื่องมือ
     - การแย่งชิงเซสชันและปัญหาการมอบหมายที่สับสน
     - ช่องโหว่ในการส่งผ่านโทเค็น
     - การอนุญาตที่มากเกินไปและการควบคุมการเข้าถึง
     - ความปลอดภัยในห่วงโซ่อุปทานสำหรับส่วนประกอบ AI
     - การผสานรวม Microsoft Prompt Shields

4. **เริ่มต้นใช้งาน (03-GettingStarted/)**
   - การตั้งค่าและการกำหนดค่าของสภาพแวดล้อม
   - การสร้างเซิร์ฟเวอร์และไคลเอนต์ MCP เบื้องต้น
   - การผสานรวมกับแอปพลิเคชันที่มีอยู่
   - รวมถึงส่วนต่าง ๆ เช่น:
     - การสร้างเซิร์ฟเวอร์ครั้งแรก
     - การพัฒนาไคลเอนต์
     - การผสานรวม LLM ไคลเอนต์
     - การผสานรวม VS Code
     - เซิร์ฟเวอร์ Server-Sent Events (SSE)
     - การใช้งานเซิร์ฟเวอร์ขั้นสูง
     - การสตรีม HTTP
     - การผสานรวม AI Toolkit
     - กลยุทธ์การทดสอบ
     - แนวทางการปรับใช้

5. **การใช้งานในทางปฏิบัติ (04-PracticalImplementation/)**
   - การใช้ SDK ในภาษาการเขียนโปรแกรมต่าง ๆ
   - เทคนิคการดีบัก ทดสอบ และตรวจสอบ
   - การสร้างเทมเพลตคำสั่งและเวิร์กโฟลว์ที่นำกลับมาใช้ใหม่ได้
   - โครงการตัวอย่างพร้อมตัวอย่างการใช้งาน

6. **หัวข้อขั้นสูง (05-AdvancedTopics/)**
   - เทคนิคการออกแบบบริบท
   - การผสานรวม Foundry agent
   - เวิร์กโฟลว์ AI แบบหลายรูปแบบ
   - การสาธิตการตรวจสอบสิทธิ์ OAuth2
   - ความสามารถในการค้นหาแบบเรียลไทม์
   - การสตรีมแบบเรียลไทม์
   - การใช้งานบริบทรากฐาน
   - กลยุทธ์การกำหนดเส้นทาง
   - เทคนิคการสุ่มตัวอย่าง
   - วิธีการปรับขนาด
   - การพิจารณาด้านความปลอดภัย
   - การผสานรวมความปลอดภัย Entra ID
   - การผสานรวมการค้นหาเว็บ

7. **การมีส่วนร่วมของชุมชน (06-CommunityContributions/)**
   - วิธีการมีส่วนร่วมในโค้ดและเอกสาร
   - การทำงานร่วมกันผ่าน GitHub
   - การปรับปรุงและข้อเสนอแนะที่ขับเคลื่อนโดยชุมชน
   - การใช้ไคลเอนต์ MCP ต่าง ๆ (Claude Desktop, Cline, VSCode)
   - การทำงานกับเซิร์ฟเวอร์ MCP ยอดนิยม รวมถึงการสร้างภาพ

8. **บทเรียนจากการใช้งานในช่วงแรก (07-LessonsfromEarlyAdoption/)**
   - การใช้งานจริงและเรื่องราวความสำเร็จ
   - การสร้างและปรับใช้โซลูชันที่ใช้ MCP
   - แนวโน้มและแผนงานในอนาคต
   - **Microsoft MCP Servers Guide**: คู่มือที่ครอบคลุมสำหรับเซิร์ฟเวอร์ MCP ของ Microsoft ที่พร้อมใช้งานในระดับการผลิต 10 เซิร์ฟเวอร์ รวมถึง:
     - Microsoft Learn Docs MCP Server
     - Azure MCP Server (ตัวเชื่อมต่อเฉพาะทางกว่า 15 ตัว)
     - GitHub MCP Server
     - Azure DevOps MCP Server
     - MarkItDown MCP Server
     - SQL Server MCP Server
     - Playwright MCP Server
     - Dev Box MCP Server
     - Azure AI Foundry MCP Server
     - Microsoft 365 Agents Toolkit MCP Server

9. **แนวทางปฏิบัติที่ดีที่สุด (08-BestPractices/)**
   - การปรับแต่งประสิทธิภาพและการเพิ่มประสิทธิภาพ
   - การออกแบบระบบ MCP ที่ทนทานต่อความผิดพลาด
   - กลยุทธ์การทดสอบและความยืดหยุ่น

10. **กรณีศึกษา (09-CaseStudy/)**
    - **กรณีศึกษาที่ครอบคลุมเจ็ดกรณี** แสดงให้เห็นถึงความหลากหลายของ MCP ในสถานการณ์ต่าง ๆ:
    - **Azure AI Travel Agents**: การจัดการหลายตัวแทนด้วย Azure OpenAI และ AI Search
    - **การผสานรวม Azure DevOps**: การทำงานอัตโนมัติของกระบวนการเวิร์กโฟลว์ด้วยการอัปเดตข้อมูล YouTube
    - **การดึงเอกสารแบบเรียลไทม์**: ไคลเอนต์คอนโซล Python พร้อมการสตรีม HTTP
    - **ตัวสร้างแผนการศึกษาแบบโต้ตอบ**: แอปเว็บ Chainlit พร้อม AI เชิงสนทนา
    - **เอกสารในตัวแก้ไข**: การผสานรวม VS Code กับเวิร์กโฟลว์ GitHub Copilot
    - **การจัดการ API ของ Azure**: การผสานรวม API ระดับองค์กรพร้อมการสร้างเซิร์ฟเวอร์ MCP
    - **GitHub MCP Registry**: การพัฒนาและแพลตฟอร์มการผสานรวมแบบตัวแทน
    - ตัวอย่างการใช้งานที่ครอบคลุมการผสานรวมระดับองค์กร การเพิ่มประสิทธิภาพนักพัฒนา และการพัฒนาอีโคซิสเต็ม

11. **เวิร์กช็อปแบบลงมือปฏิบัติ (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - เวิร์กช็อปแบบลงมือปฏิบัติที่ครอบคลุมซึ่งผสาน MCP กับ AI Toolkit
    - การสร้างแอปพลิเคชันอัจฉริยะที่เชื่อมโยงโมเดล AI กับเครื่องมือในโลกจริง
    - โมดูลเชิงปฏิบัติที่ครอบคลุมพื้นฐาน การพัฒนาเซิร์ฟเวอร์แบบกำหนดเอง และกลยุทธ์การปรับใช้ในระดับการผลิต
    - **โครงสร้างห้องปฏิบัติการ**:
      - ห้องปฏิบัติการ 1: พื้นฐานเซิร์ฟเวอร์ MCP
      - ห้องปฏิบัติการ 2: การพัฒนาเซิร์ฟเวอร์ MCP ขั้นสูง
      - ห้องปฏิบัติการ 3: การผสานรวม AI Toolkit
      - ห้องปฏิบัติการ 4: การปรับใช้และการปรับขนาดในระดับการผลิต
    - วิธีการเรียนรู้แบบห้องปฏิบัติการพร้อมคำแนะนำทีละขั้นตอน

12. **ห้องปฏิบัติการการผสานรวมฐานข้อมูลเซิร์ฟเวอร์ MCP (11-MCPServerHandsOnLabs/)**
    - **เส้นทางการเรียนรู้ 13 ห้องปฏิบัติการที่ครอบคลุม** สำหรับการสร้างเซิร์ฟเวอร์ MCP ที่พร้อมใช้งานในระดับการผลิตพร้อมการผสานรวม PostgreSQL
    - **การใช้งานการวิเคราะห์ค้าปลีกในโลกจริง** โดยใช้กรณีศึกษา Zava Retail
    - **รูปแบบระดับองค์กร** รวมถึง Row Level Security (RLS), การค้นหาเชิงความหมาย และการเข้าถึงข้อมูลแบบหลายผู้เช่า
    - **โครงสร้างห้องปฏิบัติการที่สมบูรณ์**:
      - **ห้องปฏิบัติการ 00-03: พื้นฐาน** - บทนำ สถาปัตยกรรม ความปลอดภัย การตั้งค่าสภาพแวดล้อม
      - **ห้องปฏิบัติการ 04-06: การสร้างเซิร์ฟเวอร์ MCP** - การออกแบบฐานข้อมูล การใช้งานเซิร์ฟเวอร์ MCP การพัฒนาเครื่องมือ
      - **ห้องปฏิบัติการ 07-09: คุณสมบัติขั้นสูง** - การค้นหาเชิงความหมาย การทดสอบและดีบัก การผสานรวม VS Code
      - **ห้องปฏิบัติการ 10-12: การผลิตและแนวทางปฏิบัติที่ดีที่สุด** - การปรับใช้ การตรวจสอบ การเพิ่มประสิทธิภาพ
    - **เทคโนโลยีที่ครอบคลุม**: FastMCP framework, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **ผลลัพธ์การเรียนรู้**: เซิร์ฟเวอร์ MCP ที่พร้อมใช้งานในระดับการผลิต รูปแบบการผสานรวมฐานข้อมูล การวิเคราะห์ที่ขับเคลื่อนด้วย AI ความปลอดภัยระดับองค์กร

## ทรัพยากรเพิ่มเติม

ที่เก็บข้อมูลนี้มีทรัพยากรสนับสนุนดังนี้:

- **โฟลเดอร์ภาพ**: มีแผนภาพและภาพประกอบที่ใช้ตลอดหลักสูตร
- **การแปลภาษา**: รองรับหลายภาษา พร้อมการแปลเอกสารอัตโนมัติ
- **ทรัพยากร MCP อย่างเป็นทางการ**:
  - [เอกสาร MCP](https://modelcontextprotocol.io/)
  - [ข้อกำหนด MCP](https://spec.modelcontextprotocol.io/)
  - [ที่เก็บ GitHub MCP](https://github.com/modelcontextprotocol)

## วิธีการใช้ที่เก็บข้อมูลนี้

1. **การเรียนรู้แบบลำดับขั้น**: ทำตามบทต่าง ๆ ตามลำดับ (00 ถึง 11) เพื่อประสบการณ์การเรียนรู้ที่มีโครงสร้าง
2. **มุ่งเน้นเฉพาะภาษา**: หากคุณสนใจภาษาโปรแกรมใดเป็นพิเศษ ให้สำรวจไดเรกทอรีตัวอย่างสำหรับการใช้งานในภาษาที่คุณต้องการ
3. **การใช้งานในทางปฏิบัติ**: เริ่มต้นที่ส่วน "เริ่มต้นใช้งาน" เพื่อตั้งค่าสภาพแวดล้อมของคุณและสร้างเซิร์ฟเวอร์และไคลเอนต์ MCP ครั้งแรก
4. **การสำรวจขั้นสูง**: เมื่อคุณคุ้นเคยกับพื้นฐานแล้ว ให้เจาะลึกหัวข้อขั้นสูงเพื่อขยายความรู้ของคุณ
5. **การมีส่วนร่วมของชุมชน**: เข้าร่วมชุมชน MCP ผ่านการสนทนาใน GitHub และช่องทาง Discord เพื่อเชื่อมต่อกับผู้เชี่ยวชาญและนักพัฒนาคนอื่น ๆ

## ไคลเอนต์และเครื่องมือ MCP

หลักสูตรนี้ครอบคลุมไคลเอนต์และเครื่องมือ MCP ต่าง ๆ:

1. **ไคลเอนต์อย่างเป็นทางการ**:
   - Visual Studio Code
   - MCP ใน Visual Studio Code
   - Claude Desktop
   - Claude ใน VSCode
   - Claude API

2. **ไคลเอนต์ชุมชน**:
   - Cline (แบบเทอร์มินัล)
   - Cursor (ตัวแก้ไขโค้ด)
   - ChatMCP
   - Windsurf

3. **เครื่องมือจัดการ MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## เซิร์ฟเวอร์ MCP ยอดนิยม

ที่เก็บข้อมูลนี้แนะนำเซิร์ฟเวอร์ MCP ต่าง ๆ รวมถึง:

1. **เซิร์ฟเวอร์ MCP ของ Microsoft อย่างเป็นทางการ**:
   - Microsoft Learn Docs MCP Server
   - Azure MCP Server (ตัวเชื่อมต่อเฉพาะทางกว่า 15 ตัว)
   - GitHub MCP Server
   - Azure DevOps MCP Server
   - MarkItDown MCP Server
   - SQL Server MCP Server
   - Playwright MCP Server
   - Dev Box MCP Server
   - Azure AI Foundry MCP Server
   - Microsoft 365 Agents Toolkit MCP Server

2. **เซิร์ฟเวอร์อ้างอิงอย่างเป็นทางการ**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **การสร้างภาพ**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **เครื่องมือพัฒนา**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **เซิร์ฟเวอร์เฉพาะทาง**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## การมีส่วนร่วม

ที่เก็บข้อมูลนี้ยินดีต้อนรับการมีส่วนร่วมจากชุมชน ดูส่วนการมีส่วนร่วมของชุมชนสำหรับคำแนะนำเกี่ยวกับวิธีการมีส่วนร่วมอย่างมีประสิทธิภาพในระบบนิเวศ MCP

----

*คู่มือการศึกษานี้ได้รับการอัปเดตเมื่อวันที่ 6 ตุลาคม 2025 และให้ภาพรวมของที่เก็บข้อมูล ณ วันที่ดังกล่าว เนื้อหาของที่เก็บข้อมูลอาจมีการอัปเดตหลังจากวันที่นี้*

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้