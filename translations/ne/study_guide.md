# मोडेल कन्टेक्स्ट प्रोटोकल (MCP) का लागि शुरुआतीहरू - अध्ययन मार्गदर्शक

यो अध्ययन मार्गदर्शकले "मोडेल कन्टेक्स्ट प्रोटोकल (MCP) का लागि शुरुआतीहरू" पाठ्यक्रमको भण्डार संरचना र सामग्रीको अवलोकन प्रदान गर्दछ। भण्डारलाई प्रभावकारी रूपमा नेभिगेट गर्न र उपलब्ध स्रोतहरूको अधिकतम उपयोग गर्न यो मार्गदर्शक प्रयोग गर्नुहोस्।

## भण्डारको अवलोकन

मोडेल कन्टेक्स्ट प्रोटोकल (MCP) AI मोडेलहरू र क्लाइन्ट एप्लिकेसनहरू बीचको अन्तरक्रियाको लागि एक मानकीकृत फ्रेमवर्क हो। प्रारम्भमा Anthropic द्वारा सिर्जना गरिएको, MCP अब व्यापक MCP समुदायद्वारा आधिकारिक GitHub संगठन मार्फत व्यवस्थापन गरिन्छ। यो भण्डारले C#, Java, JavaScript, Python, र TypeScript मा व्यावहारिक कोड उदाहरणहरू सहितको व्यापक पाठ्यक्रम प्रदान गर्दछ, जुन AI विकासकर्ता, प्रणाली वास्तुकार, र सफ्टवेयर इन्जिनियरहरूको लागि डिजाइन गरिएको हो।

## दृश्य पाठ्यक्रम नक्सा

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

## भण्डार संरचना

भण्डार ११ मुख्य खण्डहरूमा विभाजित छ, प्रत्येक MCP का विभिन्न पक्षहरूमा केन्द्रित छ:

1. **परिचय (00-Introduction/)**
   - मोडेल कन्टेक्स्ट प्रोटोकलको अवलोकन
   - AI पाइपलाइनहरूमा मानकीकरण किन महत्त्वपूर्ण छ
   - व्यावहारिक प्रयोगका केसहरू र फाइदाहरू

2. **मुख्य अवधारणाहरू (01-CoreConcepts/)**
   - क्लाइन्ट-सर्भर आर्किटेक्चर
   - प्रमुख प्रोटोकल घटकहरू
   - MCP मा सन्देश आदानप्रदानका ढाँचाहरू

3. **सुरक्षा (02-Security/)**
   - MCP-आधारित प्रणालीहरूमा सुरक्षा खतराहरू
   - कार्यान्वयनहरू सुरक्षित गर्नका लागि उत्तम अभ्यासहरू
   - प्रमाणीकरण र अनुमति रणनीतिहरू
   - **व्यापक सुरक्षा दस्तावेजहरू**:
     - MCP सुरक्षा उत्तम अभ्यासहरू २०२५
     - Azure सामग्री सुरक्षा कार्यान्वयन मार्गदर्शक
     - MCP सुरक्षा नियन्त्रण र प्रविधिहरू
     - MCP उत्तम अभ्यासहरू छोटो सन्दर्भ
   - **महत्त्वपूर्ण सुरक्षा विषयहरू**:
     - प्रम्प्ट इन्जेक्सन र टूल विषाक्तता आक्रमणहरू
     - सत्र अपहरण र भ्रमित डेप्युटी समस्याहरू
     - टोकन पासथ्रु कमजोरीहरू
     - अत्यधिक अनुमति र पहुँच नियन्त्रण
     - AI घटकहरूको आपूर्ति श्रृंखला सुरक्षा
     - Microsoft Prompt Shields एकीकरण

4. **सुरु गर्दै (03-GettingStarted/)**
   - वातावरण सेटअप र कन्फिगरेसन
   - आधारभूत MCP सर्भरहरू र क्लाइन्टहरू सिर्जना गर्दै
   - विद्यमान एप्लिकेसनहरूसँग एकीकरण
   - समावेश खण्डहरू:
     - पहिलो सर्भर कार्यान्वयन
     - क्लाइन्ट विकास
     - LLM क्लाइन्ट एकीकरण
     - VS Code एकीकरण
     - सर्भर-सेन्ट इभेन्ट्स (SSE) सर्भर
     - उन्नत सर्भर प्रयोग
     - HTTP स्ट्रिमिङ
     - AI टूलकिट एकीकरण
     - परीक्षण रणनीतिहरू
     - परिनियोजन दिशानिर्देशहरू

5. **व्यावहारिक कार्यान्वयन (04-PracticalImplementation/)**
   - विभिन्न प्रोग्रामिङ भाषाहरूमा SDK प्रयोग गर्दै
   - डिबगिङ, परीक्षण, र मान्यकरण प्रविधिहरू
   - पुन: प्रयोग गर्न मिल्ने प्रम्प्ट टेम्प्लेटहरू र वर्कफ्लोहरू निर्माण गर्दै
   - कार्यान्वयन उदाहरणहरू सहितका नमूना परियोजनाहरू

6. **उन्नत विषयहरू (05-AdvancedTopics/)**
   - कन्टेक्स्ट इन्जिनियरिङ प्रविधिहरू
   - Foundry एजेन्ट एकीकरण
   - मल्टी-मोडल AI वर्कफ्लोहरू
   - OAuth2 प्रमाणीकरण डेमोहरू
   - वास्तविक-समय खोज क्षमताहरू
   - वास्तविक-समय स्ट्रिमिङ
   - रूट कन्टेक्स्ट कार्यान्वयन
   - राउटिङ रणनीतिहरू
   - नमूना प्रविधिहरू
   - स्केलिङ दृष्टिकोणहरू
   - सुरक्षा विचारहरू
   - Entra ID सुरक्षा एकीकरण
   - वेब खोज एकीकरण

7. **समुदाय योगदानहरू (06-CommunityContributions/)**
   - कोड र दस्तावेजहरू योगदान गर्ने तरिका
   - GitHub मार्फत सहयोग गर्दै
   - समुदाय-चालित सुधारहरू र प्रतिक्रिया
   - विभिन्न MCP क्लाइन्टहरू प्रयोग गर्दै (Claude Desktop, Cline, VSCode)
   - छवि उत्पादन सहितका लोकप्रिय MCP सर्भरहरूसँग काम गर्दै

8. **प्रारम्भिक अपनाउनेबाट सिकाइ (07-LessonsfromEarlyAdoption/)**
   - वास्तविक-विश्व कार्यान्वयनहरू र सफलताको कथाहरू
   - MCP-आधारित समाधानहरू निर्माण र परिनियोजन गर्दै
   - प्रवृत्तिहरू र भविष्यको रोडम्याप
   - **Microsoft MCP सर्भरहरू मार्गदर्शक**: १० उत्पादन-तयार Microsoft MCP सर्भरहरूको व्यापक मार्गदर्शक, जसमा समावेश छ:
     - Microsoft Learn Docs MCP सर्भर
     - Azure MCP सर्भर (१५+ विशेष कनेक्टरहरू)
     - GitHub MCP सर्भर
     - Azure DevOps MCP सर्भर
     - MarkItDown MCP सर्भर
     - SQL Server MCP सर्भर
     - Playwright MCP सर्भर
     - Dev Box MCP सर्भर
     - Azure AI Foundry MCP सर्भर
     - Microsoft 365 Agents Toolkit MCP सर्भर

9. **उत्तम अभ्यासहरू (08-BestPractices/)**
   - प्रदर्शन ट्युनिङ र अनुकूलन
   - दोष-सहनशील MCP प्रणालीहरू डिजाइन गर्दै
   - परीक्षण र लचिलोपन रणनीतिहरू

10. **केस अध्ययनहरू (09-CaseStudy/)**
    - **सात व्यापक केस अध्ययनहरू** जसले विविध परिदृश्यहरूमा MCP को बहुमुखी प्रतिभा प्रदर्शन गर्छ:
    - **Azure AI यात्रा एजेन्टहरू**: Azure OpenAI र AI खोजको साथ मल्टी-एजेन्ट समन्वय
    - **Azure DevOps एकीकरण**: YouTube डेटा अपडेटहरूसँग कार्यप्रवाह प्रक्रियाहरू स्वचालित गर्दै
    - **वास्तविक-समय दस्तावेज पुनःप्राप्ति**: स्ट्रिमिङ HTTP सहितको Python कन्सोल क्लाइन्ट
    - **इंटरएक्टिभ अध्ययन योजना जनरेटर**: Chainlit वेब एप्लिकेसनसँग संवादात्मक AI
    - **इन-एडिटर दस्तावेजीकरण**: GitHub Copilot वर्कफ्लोहरूसँग VS Code एकीकरण
    - **Azure API व्यवस्थापन**: MCP सर्भर सिर्जनासँग उद्यम API एकीकरण
    - **GitHub MCP रजिस्ट्री**: इकोसिस्टम विकास र एजेन्टिक एकीकरण प्लेटफर्म
    - कार्यान्वयन उदाहरणहरू उद्यम एकीकरण, विकासकर्ता उत्पादकता, र इकोसिस्टम विकासमा फैलिएको

11. **व्यावहारिक कार्यशाला (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - MCP र AI टूलकिटलाई संयोजन गर्दै व्यापक व्यावहारिक कार्यशाला
    - वास्तविक-विश्व उपकरणहरूसँग AI मोडेलहरू पुल गर्दै बुद्धिमान एप्लिकेसनहरू निर्माण गर्दै
    - आधारभूत, अनुकूलित सर्भर विकास, र उत्पादन परिनियोजन रणनीतिहरू समेट्ने व्यावहारिक मोड्युलहरू
    - **प्रयोगशाला संरचना**:
      - प्रयोगशाला १: MCP सर्भर आधारभूत
      - प्रयोगशाला २: उन्नत MCP सर्भर विकास
      - प्रयोगशाला ३: AI टूलकिट एकीकरण
      - प्रयोगशाला ४: उत्पादन परिनियोजन र स्केलिङ
    - चरण-दर-चरण निर्देशनहरूसहितको प्रयोगशाला-आधारित शिक्षण दृष्टिकोण

12. **MCP सर्भर डाटाबेस एकीकरण प्रयोगशालाहरू (11-MCPServerHandsOnLabs/)**
    - **१३ व्यापक प्रयोगशाला शिक्षण मार्ग** PostgreSQL एकीकरणको साथ उत्पादन-तयार MCP सर्भरहरू निर्माण गर्न
    - **Zava Retail प्रयोग केस प्रयोग गर्दै वास्तविक-विश्व खुद्रा विश्लेषण कार्यान्वयन**
    - **उद्यम-ग्रेड ढाँचाहरू** जसमा Row Level Security (RLS), अर्थपूर्ण खोज, र बहु-भाडावाल डेटा पहुँच समावेश छ
    - **पूर्ण प्रयोगशाला संरचना**:
      - **प्रयोगशालाहरू ००-०३: आधारहरू** - परिचय, आर्किटेक्चर, सुरक्षा, वातावरण सेटअप
      - **प्रयोगशालाहरू ०४-०६: MCP सर्भर निर्माण गर्दै** - डाटाबेस डिजाइन, MCP सर्भर कार्यान्वयन, उपकरण विकास
      - **प्रयोगशालाहरू ०७-०९: उन्नत सुविधाहरू** - अर्थपूर्ण खोज, परीक्षण र डिबगिङ, VS Code एकीकरण
      - **प्रयोगशालाहरू १०-१२: उत्पादन र उत्तम अभ्यासहरू** - परिनियोजन, निगरानी, अनुकूलन
    - **समावेश प्रविधिहरू**: FastMCP फ्रेमवर्क, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **शिक्षण परिणामहरू**: उत्पादन-तयार MCP सर्भरहरू, डाटाबेस एकीकरण ढाँचाहरू, AI-संचालित विश्लेषण, उद्यम सुरक्षा

## अतिरिक्त स्रोतहरू

भण्डारले सहयोगी स्रोतहरू समावेश गर्दछ:

- **छविहरू फोल्डर**: पाठ्यक्रमभर प्रयोग गरिएका रेखाचित्रहरू र चित्रहरू समावेश गर्दछ
- **अनुवादहरू**: दस्तावेजहरूको स्वचालित अनुवादको साथ बहु-भाषा समर्थन
- **आधिकारिक MCP स्रोतहरू**:
  - [MCP दस्तावेजीकरण](https://modelcontextprotocol.io/)
  - [MCP विशिष्टता](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub भण्डार](https://github.com/modelcontextprotocol)

## यो भण्डार कसरी प्रयोग गर्ने

1. **क्रमिक शिक्षण**: संरचित शिक्षण अनुभवको लागि अध्यायहरू क्रमशः (०० देखि ११ सम्म) अनुसरण गर्नुहोस्।
2. **भाषा-विशिष्ट ध्यान**: यदि तपाईं कुनै विशेष प्रोग्रामिङ भाषामा रुचि राख्नुहुन्छ भने, आफ्नो रुचि अनुसार कार्यान्वयनहरूको लागि नमूना निर्देशिकाहरू अन्वेषण गर्नुहोस्।
3. **व्यावहारिक कार्यान्वयन**: आफ्नो वातावरण सेटअप गर्न र आफ्नो पहिलो MCP सर्भर र क्लाइन्ट सिर्जना गर्न "सुरु गर्दै" खण्डबाट सुरु गर्नुहोस्।
4. **उन्नत अन्वेषण**: आधारभूत कुराहरूमा सहज भएपछि, उन्नत विषयहरूमा डुबुल्की मारेर आफ्नो ज्ञान विस्तार गर्नुहोस्।
5. **समुदाय संलग्नता**: GitHub छलफलहरू र Discord च्यानलहरू मार्फत MCP समुदायमा सामेल भएर विशेषज्ञहरू र अन्य विकासकर्ताहरूसँग जडान गर्नुहोस्।

## MCP क्लाइन्टहरू र उपकरणहरू

पाठ्यक्रमले विभिन्न MCP क्लाइन्टहरू र उपकरणहरू समेट्छ:

1. **आधिकारिक क्लाइन्टहरू**:
   - Visual Studio Code 
   - MCP in Visual Studio Code
   - Claude Desktop
   - Claude in VSCode 
   - Claude API

2. **समुदाय क्लाइन्टहरू**:
   - Cline (टर्मिनल-आधारित)
   - Cursor (कोड सम्पादक)
   - ChatMCP
   - Windsurf

3. **MCP व्यवस्थापन उपकरणहरू**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## लोकप्रिय MCP सर्भरहरू

भण्डारले विभिन्न MCP सर्भरहरू प्रस्तुत गर्दछ, जसमा समावेश छ:

1. **आधिकारिक Microsoft MCP सर्भरहरू**:
   - Microsoft Learn Docs MCP सर्भर
   - Azure MCP सर्भर (१५+ विशेष कनेक्टरहरू)
   - GitHub MCP सर्भर
   - Azure DevOps MCP सर्भर
   - MarkItDown MCP सर्भर
   - SQL Server MCP सर्भर
   - Playwright MCP सर्भर
   - Dev Box MCP सर्भर
   - Azure AI Foundry MCP सर्भर
   - Microsoft 365 Agents Toolkit MCP सर्भर

2. **आधिकारिक सन्दर्भ सर्भरहरू**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **छवि उत्पादन**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **विकास उपकरणहरू**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **विशेष सर्भरहरू**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## योगदान

यो भण्डारले समुदायबाट योगदानहरूलाई स्वागत गर्दछ। MCP इकोसिस्टममा प्रभावकारी रूपमा योगदान गर्ने तरिकाको लागि समुदाय योगदान खण्ड हेर्नुहोस्।

----

*यो अध्ययन मार्गदर्शक अक्टोबर ६, २०२५ मा अद्यावधिक गरिएको थियो र सो मितिको रूपमा भण्डारको अवलोकन प्रदान गर्दछ। यो मितिपछि भण्डार सामग्री अद्यावधिक हुन सक्छ।*

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।