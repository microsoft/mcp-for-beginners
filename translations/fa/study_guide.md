# راهنمای مطالعه پروتکل زمینه مدل (MCP) برای مبتدیان

این راهنمای مطالعه یک نمای کلی از ساختار و محتوای مخزن برای برنامه آموزشی "پروتکل زمینه مدل (MCP) برای مبتدیان" ارائه می‌دهد. از این راهنما برای پیمایش مؤثر در مخزن و بهره‌برداری کامل از منابع موجود استفاده کنید.

## نمای کلی مخزن

پروتکل زمینه مدل (MCP) یک چارچوب استاندارد برای تعاملات بین مدل‌های هوش مصنوعی و برنامه‌های مشتری است. MCP که در ابتدا توسط Anthropic ایجاد شد، اکنون توسط جامعه گسترده MCP از طریق سازمان رسمی GitHub نگهداری می‌شود. این مخزن یک برنامه آموزشی جامع با مثال‌های کدنویسی عملی در زبان‌های C#، Java، JavaScript، Python و TypeScript ارائه می‌دهد که برای توسعه‌دهندگان هوش مصنوعی، معماران سیستم و مهندسان نرم‌افزار طراحی شده است.

## نقشه تصویری برنامه آموزشی

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


## ساختار مخزن

مخزن به یازده بخش اصلی تقسیم شده است که هر کدام بر جنبه‌های مختلف MCP تمرکز دارند:

1. **مقدمه (00-Introduction/)**
   - نمای کلی پروتکل زمینه مدل
   - اهمیت استانداردسازی در خطوط لوله هوش مصنوعی
   - موارد استفاده عملی و مزایا

2. **مفاهیم اصلی (01-CoreConcepts/)**
   - معماری کلاینت-سرور
   - اجزای کلیدی پروتکل
   - الگوهای پیام‌رسانی در MCP

3. **امنیت (02-Security/)**
   - تهدیدات امنیتی در سیستم‌های مبتنی بر MCP
   - بهترین روش‌ها برای ایمن‌سازی پیاده‌سازی‌ها
   - استراتژی‌های احراز هویت و مجوز
   - **مستندات جامع امنیت**:
     - بهترین روش‌های امنیتی MCP 2025
     - راهنمای پیاده‌سازی ایمنی محتوا در Azure
     - کنترل‌ها و تکنیک‌های امنیتی MCP
     - مرجع سریع بهترین روش‌های MCP
   - **موضوعات کلیدی امنیت**:
     - حملات تزریق پرامپت و مسمومیت ابزار
     - ربودن جلسه و مشکلات نماینده گیج
     - آسیب‌پذیری‌های عبور توکن
     - مجوزهای بیش از حد و کنترل دسترسی
     - امنیت زنجیره تأمین برای اجزای هوش مصنوعی
     - یکپارچه‌سازی Microsoft Prompt Shields

4. **شروع کار (03-GettingStarted/)**
   - تنظیم و پیکربندی محیط
   - ایجاد سرورها و کلاینت‌های اولیه MCP
   - یکپارچه‌سازی با برنامه‌های موجود
   - شامل بخش‌هایی برای:
     - پیاده‌سازی اولین سرور
     - توسعه کلاینت
     - یکپارچه‌سازی کلاینت LLM
     - یکپارچه‌سازی VS Code
     - سرور رویدادهای ارسال‌شده توسط سرور (SSE)
     - استفاده پیشرفته از سرور
     - استریم HTTP
     - یکپارچه‌سازی ابزار هوش مصنوعی
     - استراتژی‌های تست
     - دستورالعمل‌های استقرار

5. **پیاده‌سازی عملی (04-PracticalImplementation/)**
   - استفاده از SDKها در زبان‌های برنامه‌نویسی مختلف
   - تکنیک‌های دیباگ، تست و اعتبارسنجی
   - ساخت قالب‌های پرامپت و جریان‌های کاری قابل استفاده مجدد
   - پروژه‌های نمونه با مثال‌های پیاده‌سازی

6. **موضوعات پیشرفته (05-AdvancedTopics/)**
   - تکنیک‌های مهندسی زمینه
   - یکپارچه‌سازی عامل Foundry
   - جریان‌های کاری چند‌مدلی هوش مصنوعی
   - دموهای احراز هویت OAuth2
   - قابلیت‌های جستجوی بلادرنگ
   - استریم بلادرنگ
   - پیاده‌سازی زمینه‌های ریشه
   - استراتژی‌های مسیریابی
   - تکنیک‌های نمونه‌گیری
   - رویکردهای مقیاس‌پذیری
   - ملاحظات امنیتی
   - یکپارچه‌سازی امنیت Entra ID
   - یکپارچه‌سازی جستجوی وب

7. **مشارکت‌های جامعه (06-CommunityContributions/)**
   - نحوه مشارکت در کد و مستندات
   - همکاری از طریق GitHub
   - بهبودها و بازخوردهای جامعه‌محور
   - استفاده از کلاینت‌های مختلف MCP (Claude Desktop، Cline، VSCode)
   - کار با سرورهای محبوب MCP از جمله تولید تصویر

8. **درس‌هایی از پذیرش اولیه (07-LessonsfromEarlyAdoption/)**
   - پیاده‌سازی‌های واقعی و داستان‌های موفقیت
   - ساخت و استقرار راه‌حل‌های مبتنی بر MCP
   - روندها و نقشه راه آینده
   - **راهنمای سرورهای MCP مایکروسافت**: راهنمای جامع برای 10 سرور MCP آماده تولید مایکروسافت از جمله:
     - سرور MCP مستندات Microsoft Learn
     - سرور MCP Azure (بیش از 15 کانکتور تخصصی)
     - سرور MCP GitHub
     - سرور MCP Azure DevOps
     - سرور MCP MarkItDown
     - سرور MCP SQL Server
     - سرور MCP Playwright
     - سرور MCP Dev Box
     - سرور MCP Azure AI Foundry
     - سرور MCP ابزارهای عامل Microsoft 365

9. **بهترین روش‌ها (08-BestPractices/)**
   - تنظیم عملکرد و بهینه‌سازی
   - طراحی سیستم‌های MCP مقاوم در برابر خطا
   - استراتژی‌های تست و تاب‌آوری

10. **مطالعات موردی (09-CaseStudy/)**
    - **هفت مطالعه موردی جامع** که تطبیق‌پذیری MCP را در سناریوهای مختلف نشان می‌دهد:
    - **نمایندگان سفر هوش مصنوعی Azure**: ارکستراسیون چند‌عاملی با Azure OpenAI و جستجوی هوش مصنوعی
    - **یکپارچه‌سازی Azure DevOps**: خودکارسازی فرآیندهای جریان کاری با به‌روزرسانی داده‌های YouTube
    - **بازیابی مستندات بلادرنگ**: کلاینت کنسول Python با استریم HTTP
    - **تولیدکننده برنامه مطالعه تعاملی**: اپلیکیشن وب Chainlit با هوش مصنوعی مکالمه‌ای
    - **مستندات درون ویرایشگر**: یکپارچه‌سازی VS Code با جریان‌های کاری GitHub Copilot
    - **مدیریت API Azure**: یکپارچه‌سازی API سازمانی با ایجاد سرور MCP
    - **ثبت MCP GitHub**: توسعه اکوسیستم و پلتفرم یکپارچه‌سازی عامل
    - مثال‌های پیاده‌سازی شامل یکپارچه‌سازی سازمانی، بهره‌وری توسعه‌دهنده و توسعه اکوسیستم

11. **کارگاه عملی (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - کارگاه عملی جامع ترکیب MCP با ابزار هوش مصنوعی
    - ساخت برنامه‌های هوشمند که مدل‌های هوش مصنوعی را با ابزارهای دنیای واقعی پیوند می‌دهد
    - ماژول‌های عملی که اصول، توسعه سرور سفارشی و استراتژی‌های استقرار تولید را پوشش می‌دهد
    - **ساختار آزمایشگاه**:
      - آزمایشگاه 1: اصول سرور MCP
      - آزمایشگاه 2: توسعه پیشرفته سرور MCP
      - آزمایشگاه 3: یکپارچه‌سازی ابزار هوش مصنوعی
      - آزمایشگاه 4: استقرار تولید و مقیاس‌پذیری
    - رویکرد یادگیری مبتنی بر آزمایشگاه با دستورالعمل‌های گام‌به‌گام

12. **آزمایشگاه‌های یکپارچه‌سازی پایگاه داده سرور MCP (11-MCPServerHandsOnLabs/)**
    - **مسیر یادگیری جامع 13 آزمایشگاه** برای ساخت سرورهای MCP آماده تولید با یکپارچه‌سازی PostgreSQL
    - **پیاده‌سازی تجزیه و تحلیل خرده‌فروشی واقعی** با استفاده از مورد استفاده Zava Retail
    - **الگوهای درجه سازمانی** شامل امنیت سطح ردیف (RLS)، جستجوی معنایی و دسترسی داده چند‌مستأجری
    - **ساختار کامل آزمایشگاه**:
      - **آزمایشگاه‌های 00-03: مبانی** - مقدمه، معماری، امنیت، تنظیم محیط
      - **آزمایشگاه‌های 04-06: ساخت سرور MCP** - طراحی پایگاه داده، پیاده‌سازی سرور MCP، توسعه ابزار
      - **آزمایشگاه‌های 07-09: ویژگی‌های پیشرفته** - جستجوی معنایی، تست و دیباگ، یکپارچه‌سازی VS Code
      - **آزمایشگاه‌های 10-12: تولید و بهترین روش‌ها** - استقرار، نظارت، بهینه‌سازی
    - **فناوری‌های پوشش داده شده**: چارچوب FastMCP، PostgreSQL، Azure OpenAI، برنامه‌های کانتینری Azure، Application Insights
    - **نتایج یادگیری**: سرورهای MCP آماده تولید، الگوهای یکپارچه‌سازی پایگاه داده، تجزیه و تحلیل مبتنی بر هوش مصنوعی، امنیت سازمانی

## منابع اضافی

مخزن شامل منابع پشتیبانی‌کننده است:

- **پوشه تصاویر**: شامل نمودارها و تصاویر استفاده‌شده در سراسر برنامه آموزشی
- **ترجمه‌ها**: پشتیبانی چند‌زبانه با ترجمه‌های خودکار مستندات
- **منابع رسمی MCP**:
  - [مستندات MCP](https://modelcontextprotocol.io/)
  - [مشخصات MCP](https://spec.modelcontextprotocol.io/)
  - [مخزن GitHub MCP](https://github.com/modelcontextprotocol)

## نحوه استفاده از این مخزن

1. **یادگیری ترتیبی**: فصل‌ها را به ترتیب (00 تا 11) دنبال کنید تا تجربه یادگیری ساختاریافته‌ای داشته باشید.
2. **تمرکز زبان‌محور**: اگر به یک زبان برنامه‌نویسی خاص علاقه دارید، دایرکتوری‌های نمونه را برای پیاده‌سازی‌ها در زبان مورد نظر خود بررسی کنید.
3. **پیاده‌سازی عملی**: با بخش "شروع کار" شروع کنید تا محیط خود را تنظیم کرده و اولین سرور و کلاینت MCP خود را ایجاد کنید.
4. **کاوش پیشرفته**: پس از آشنایی با اصول، به موضوعات پیشرفته بپردازید تا دانش خود را گسترش دهید.
5. **تعامل جامعه**: از طریق بحث‌های GitHub و کانال‌های Discord به جامعه MCP بپیوندید تا با کارشناسان و توسعه‌دهندگان دیگر ارتباط برقرار کنید.

## کلاینت‌ها و ابزارهای MCP

برنامه آموزشی کلاینت‌ها و ابزارهای مختلف MCP را پوشش می‌دهد:

1. **کلاینت‌های رسمی**:
   - Visual Studio Code
   - MCP در Visual Studio Code
   - Claude Desktop
   - Claude در VSCode
   - Claude API

2. **کلاینت‌های جامعه**:
   - Cline (مبتنی بر ترمینال)
   - Cursor (ویرایشگر کد)
   - ChatMCP
   - Windsurf

3. **ابزارهای مدیریت MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## سرورهای محبوب MCP

مخزن سرورهای مختلف MCP را معرفی می‌کند، از جمله:

1. **سرورهای رسمی MCP مایکروسافت**:
   - سرور MCP مستندات Microsoft Learn
   - سرور MCP Azure (بیش از 15 کانکتور تخصصی)
   - سرور MCP GitHub
   - سرور MCP Azure DevOps
   - سرور MCP MarkItDown
   - سرور MCP SQL Server
   - سرور MCP Playwright
   - سرور MCP Dev Box
   - سرور MCP Azure AI Foundry
   - سرور MCP ابزارهای عامل Microsoft 365

2. **سرورهای مرجع رسمی**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **تولید تصویر**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **ابزارهای توسعه**:
   - Git MCP
   - کنترل ترمینال
   - دستیار کد

5. **سرورهای تخصصی**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## مشارکت

این مخزن از مشارکت‌های جامعه استقبال می‌کند. بخش مشارکت‌های جامعه را برای راهنمایی در مورد نحوه مشارکت مؤثر در اکوسیستم MCP مشاهده کنید.

----

*این راهنمای مطالعه در تاریخ 6 اکتبر 2025 به‌روزرسانی شده و نمای کلی از مخزن تا آن تاریخ ارائه می‌دهد. محتوای مخزن ممکن است پس از این تاریخ به‌روزرسانی شود.*

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.