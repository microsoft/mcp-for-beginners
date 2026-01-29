# بروتوكول سياق النموذج (MCP) للمبتدئين - دليل الدراسة

يوفر دليل الدراسة هذا نظرة عامة على هيكل المحتوى والمستودع الخاص بمنهج "بروتوكول سياق النموذج (MCP) للمبتدئين". استخدم هذا الدليل للتنقل بكفاءة في المستودع والاستفادة القصوى من الموارد المتاحة.

## نظرة عامة على المستودع

بروتوكول سياق النموذج (MCP) هو إطار عمل معياري للتفاعل بين نماذج الذكاء الاصطناعي وتطبيقات العملاء. تم إنشاؤه في البداية بواسطة Anthropic، ويتم الآن صيانته من قبل مجتمع MCP الأوسع من خلال المنظمة الرسمية على GitHub. يوفر هذا المستودع منهجًا شاملاً مع أمثلة عملية للرموز في لغات C#، Java، JavaScript، Python، وTypeScript، مصممًا لمطوري الذكاء الاصطناعي، مهندسي الأنظمة، ومهندسي البرمجيات.

## خريطة المنهج البصرية

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

## هيكل المستودع

تم تنظيم المستودع إلى أحد عشر قسمًا رئيسيًا، يركز كل منها على جوانب مختلفة من MCP:

1. **المقدمة (00-Introduction/)**
   - نظرة عامة على بروتوكول سياق النموذج
   - أهمية التوحيد في خطوط أنابيب الذكاء الاصطناعي
   - حالات الاستخدام العملية والفوائد

2. **المفاهيم الأساسية (01-CoreConcepts/)**
   - بنية العميل-الخادم
   - مكونات البروتوكول الرئيسية
   - أنماط الرسائل في MCP

3. **الأمان (02-Security/)**
   - تهديدات الأمان في الأنظمة القائمة على MCP
   - أفضل الممارسات لتأمين التنفيذ
   - استراتيجيات المصادقة والتفويض
   - **وثائق الأمان الشاملة**:
     - أفضل ممارسات أمان MCP لعام 2025
     - دليل تنفيذ أمان محتوى Azure
     - ضوابط وتقنيات أمان MCP
     - مرجع سريع لأفضل ممارسات MCP
   - **مواضيع الأمان الرئيسية**:
     - هجمات حقن المطالبات وتسميم الأدوات
     - اختطاف الجلسات ومشاكل الوكيل المرتبك
     - ثغرات تمرير الرموز
     - الأذونات الزائدة والتحكم في الوصول
     - أمان سلسلة التوريد لمكونات الذكاء الاصطناعي
     - تكامل دروع المطالبات من Microsoft

4. **البدء (03-GettingStarted/)**
   - إعداد البيئة وتكوينها
   - إنشاء خوادم وعملاء MCP الأساسية
   - التكامل مع التطبيقات الحالية
   - يتضمن أقسامًا لـ:
     - تنفيذ أول خادم
     - تطوير العميل
     - تكامل عميل LLM
     - تكامل VS Code
     - خادم أحداث مرسلة من الخادم (SSE)
     - استخدام الخادم المتقدم
     - بث HTTP
     - تكامل أدوات الذكاء الاصطناعي
     - استراتيجيات الاختبار
     - إرشادات النشر

5. **التنفيذ العملي (04-PracticalImplementation/)**
   - استخدام SDKs عبر لغات البرمجة المختلفة
   - تقنيات التصحيح والاختبار والتحقق
   - تصميم قوالب المطالبات القابلة لإعادة الاستخدام وسير العمل
   - مشاريع نموذجية مع أمثلة تنفيذية

6. **المواضيع المتقدمة (05-AdvancedTopics/)**
   - تقنيات هندسة السياق
   - تكامل وكلاء Foundry
   - سير عمل الذكاء الاصطناعي متعدد الوسائط
   - عروض توضيحية للمصادقة باستخدام OAuth2
   - قدرات البحث في الوقت الفعلي
   - البث في الوقت الفعلي
   - تنفيذ السياقات الجذرية
   - استراتيجيات التوجيه
   - تقنيات أخذ العينات
   - نهج التوسع
   - اعتبارات الأمان
   - تكامل أمان Entra ID
   - تكامل البحث على الويب

7. **مساهمات المجتمع (06-CommunityContributions/)**
   - كيفية المساهمة في الكود والوثائق
   - التعاون عبر GitHub
   - تحسينات وردود فعل يقودها المجتمع
   - استخدام عملاء MCP المختلفين (Claude Desktop، Cline، VSCode)
   - العمل مع خوادم MCP الشهيرة بما في ذلك توليد الصور

8. **دروس من التبني المبكر (07-LessonsfromEarlyAdoption/)**
   - تنفيذات واقعية وقصص نجاح
   - بناء ونشر حلول قائمة على MCP
   - الاتجاهات وخارطة الطريق المستقبلية
   - **دليل خوادم Microsoft MCP**: دليل شامل لـ 10 خوادم MCP جاهزة للإنتاج من Microsoft بما في ذلك:
     - خادم MCP لوثائق Microsoft Learn
     - خادم MCP لـ Azure (15+ موصلات متخصصة)
     - خادم MCP لـ GitHub
     - خادم MCP لـ Azure DevOps
     - خادم MCP لـ MarkItDown
     - خادم MCP لـ SQL Server
     - خادم MCP لـ Playwright
     - خادم MCP لـ Dev Box
     - خادم MCP لـ Azure AI Foundry
     - خادم MCP لـ Microsoft 365 Agents Toolkit

9. **أفضل الممارسات (08-BestPractices/)**
   - تحسين الأداء وضبطه
   - تصميم أنظمة MCP مقاومة للأعطال
   - استراتيجيات الاختبار والمرونة

10. **دراسات الحالة (09-CaseStudy/)**
    - **سبع دراسات حالة شاملة** توضح تنوع MCP عبر سيناريوهات مختلفة:
    - **وكلاء السفر الذكاء الاصطناعي في Azure**: تنسيق متعدد الوكلاء مع Azure OpenAI وAI Search
    - **تكامل Azure DevOps**: أتمتة عمليات سير العمل مع تحديثات بيانات YouTube
    - **استرجاع الوثائق في الوقت الفعلي**: عميل Python console مع بث HTTP
    - **مولد خطة دراسة تفاعلية**: تطبيق ويب Chainlit مع الذكاء الاصطناعي الحواري
    - **الوثائق داخل المحرر**: تكامل VS Code مع سير عمل GitHub Copilot
    - **إدارة واجهات برمجة التطبيقات في Azure**: تكامل واجهات برمجة التطبيقات المؤسسية مع إنشاء خادم MCP
    - **سجل MCP لـ GitHub**: تطوير النظام البيئي ومنصة تكامل الوكلاء
    - أمثلة تنفيذية تمتد عبر تكامل المؤسسات، إنتاجية المطورين، وتطوير النظام البيئي

11. **ورشة العمل العملية (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - ورشة عمل عملية شاملة تجمع بين MCP وأدوات الذكاء الاصطناعي
    - بناء تطبيقات ذكية تربط نماذج الذكاء الاصطناعي بالأدوات الواقعية
    - وحدات عملية تغطي الأساسيات، تطوير الخادم المخصص، واستراتيجيات نشر الإنتاج
    - **هيكل الورشة**:
      - المختبر 1: أساسيات خادم MCP
      - المختبر 2: تطوير خادم MCP المتقدم
      - المختبر 3: تكامل أدوات الذكاء الاصطناعي
      - المختبر 4: نشر الإنتاج والتوسع
    - نهج التعلم القائم على المختبر مع تعليمات خطوة بخطوة

12. **مختبرات تكامل قاعدة بيانات خادم MCP (11-MCPServerHandsOnLabs/)**
    - **مسار تعلم شامل من 13 مختبرًا** لبناء خوادم MCP جاهزة للإنتاج مع تكامل PostgreSQL
    - **تنفيذ تحليلات البيع بالتجزئة الواقعية** باستخدام حالة استخدام Zava Retail
    - **أنماط على مستوى المؤسسات** بما في ذلك أمان مستوى الصف (RLS)، البحث الدلالي، والوصول إلى البيانات متعددة المستأجرين
    - **هيكل المختبر الكامل**:
      - **المختبرات 00-03: الأساسيات** - المقدمة، الهندسة المعمارية، الأمان، إعداد البيئة
      - **المختبرات 04-06: بناء خادم MCP** - تصميم قاعدة البيانات، تنفيذ خادم MCP، تطوير الأدوات
      - **المختبرات 07-09: الميزات المتقدمة** - البحث الدلالي، الاختبار والتصحيح، تكامل VS Code
      - **المختبرات 10-12: الإنتاج وأفضل الممارسات** - النشر، المراقبة، التحسين
    - **التقنيات المغطاة**: إطار عمل FastMCP، PostgreSQL، Azure OpenAI، تطبيقات Azure Container، رؤى التطبيقات
    - **نتائج التعلم**: خوادم MCP جاهزة للإنتاج، أنماط تكامل قاعدة البيانات، تحليلات مدعومة بالذكاء الاصطناعي، أمان المؤسسات

## موارد إضافية

يتضمن المستودع موارد داعمة:

- **مجلد الصور**: يحتوي على الرسوم البيانية والرسوم التوضيحية المستخدمة في جميع أنحاء المنهج
- **الترجمات**: دعم متعدد اللغات مع ترجمات تلقائية للوثائق
- **موارد MCP الرسمية**:
  - [وثائق MCP](https://modelcontextprotocol.io/)
  - [مواصفات MCP](https://spec.modelcontextprotocol.io/)
  - [مستودع MCP على GitHub](https://github.com/modelcontextprotocol)

## كيفية استخدام هذا المستودع

1. **التعلم المتسلسل**: اتبع الفصول بالترتيب (00 إلى 11) لتجربة تعلم منظمة.
2. **التركيز على لغة معينة**: إذا كنت مهتمًا بلغة برمجة معينة، استكشف أدلة العينات للتنفيذات في لغتك المفضلة.
3. **التنفيذ العملي**: ابدأ بقسم "البدء" لإعداد بيئتك وإنشاء أول خادم وعميل MCP.
4. **الاستكشاف المتقدم**: بمجرد أن تصبح مرتاحًا مع الأساسيات، استكشف المواضيع المتقدمة لتوسيع معرفتك.
5. **التفاعل المجتمعي**: انضم إلى مجتمع MCP من خلال مناقشات GitHub وقنوات Discord للتواصل مع الخبراء والمطورين الآخرين.

## عملاء وأدوات MCP

يغطي المنهج مختلف عملاء وأدوات MCP:

1. **العملاء الرسميون**:
   - Visual Studio Code
   - MCP في Visual Studio Code
   - Claude Desktop
   - Claude في VSCode
   - Claude API

2. **عملاء المجتمع**:
   - Cline (مبني على الطرفية)
   - Cursor (محرر الأكواد)
   - ChatMCP
   - Windsurf

3. **أدوات إدارة MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## خوادم MCP الشهيرة

يقدم المستودع مختلف خوادم MCP، بما في ذلك:

1. **خوادم Microsoft MCP الرسمية**:
   - خادم MCP لوثائق Microsoft Learn
   - خادم MCP لـ Azure (15+ موصلات متخصصة)
   - خادم MCP لـ GitHub
   - خادم MCP لـ Azure DevOps
   - خادم MCP لـ MarkItDown
   - خادم MCP لـ SQL Server
   - خادم MCP لـ Playwright
   - خادم MCP لـ Dev Box
   - خادم MCP لـ Azure AI Foundry
   - خادم MCP لـ Microsoft 365 Agents Toolkit

2. **الخوادم المرجعية الرسمية**:
   - نظام الملفات
   - Fetch
   - الذاكرة
   - التفكير المتسلسل

3. **توليد الصور**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **أدوات التطوير**:
   - Git MCP
   - التحكم في الطرفية
   - مساعد الأكواد

5. **الخوادم المتخصصة**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## المساهمة

يرحب هذا المستودع بمساهمات المجتمع. راجع قسم مساهمات المجتمع للحصول على إرشادات حول كيفية المساهمة بفعالية في نظام MCP البيئي.

----

*تم تحديث دليل الدراسة هذا في 6 أكتوبر 2025، ويوفر نظرة عامة على المستودع اعتبارًا من هذا التاريخ. قد يتم تحديث محتوى المستودع بعد هذا التاريخ.*

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.