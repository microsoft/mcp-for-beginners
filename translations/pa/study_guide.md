# ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਲਈ ਸ਼ੁਰੂਆਤੀ - ਅਧਿਐਨ ਗਾਈਡ

ਇਹ ਅਧਿਐਨ ਗਾਈਡ "ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਲਈ ਸ਼ੁਰੂਆਤੀ" ਪਾਠਕ੍ਰਮ ਲਈ ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਬਣਤਰ ਅਤੇ ਸਮੱਗਰੀ ਦਾ ਜਾਇਜ਼ਾ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ। ਇਸ ਗਾਈਡ ਦੀ ਵਰਤੋਂ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਕੁਸ਼ਲਤਾਪੂਰਵਕ ਨੇਵੀਗੇਟ ਕਰਨ ਅਤੇ ਉਪਲਬਧ ਸਰੋਤਾਂ ਦਾ ਵਧੇਰੇ ਲਾਭ ਲੈਣ ਲਈ ਕਰੋ।

## ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਜਾਇਜ਼ਾ

ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) AI ਮਾਡਲ ਅਤੇ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰ ਲਈ ਇੱਕ ਮਿਆਰੀ ਫਰੇਮਵਰਕ ਹੈ। ਸ਼ੁਰੂ ਵਿੱਚ Anthropic ਦੁਆਰਾ ਬਣਾਇਆ ਗਿਆ, MCP ਹੁਣ ਵੱਡੇ MCP ਸਮੁਦਾਇ ਦੁਆਰਾ ਅਧਿਕਾਰਤ GitHub ਸੰਗਠਨ ਰਾਹੀਂ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਰਿਪੋਜ਼ਟਰੀ C#, Java, JavaScript, Python, ਅਤੇ TypeScript ਵਿੱਚ ਹੱਥ-ਅਨੁਭਵ ਕੋਡ ਉਦਾਹਰਣਾਂ ਨਾਲ ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਪਾਠਕ੍ਰਮ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਕਿ AI ਡਿਵੈਲਪਰਾਂ, ਸਿਸਟਮ ਆਰਕੀਟੈਕਟਾਂ, ਅਤੇ ਸੌਫਟਵੇਅਰ ਇੰਜੀਨੀਅਰਾਂ ਲਈ ਡਿਜ਼ਾਇਨ ਕੀਤਾ ਗਿਆ ਹੈ।

## ਵਿਜ਼ੁਅਲ ਪਾਠਕ੍ਰਮ ਨਕਸ਼ਾ

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

## ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਬਣਤਰ

ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਗਿਆਰਾਂ ਮੁੱਖ ਭਾਗਾਂ ਵਿੱਚ ਵੰਡਿਆ ਗਿਆ ਹੈ, ਜੋ MCP ਦੇ ਵੱਖ-ਵੱਖ ਪਹਲੂਆਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦੇ ਹਨ:

1. **ਪ੍ਰਸਤਾਵਨਾ (00-Introduction/)**
   - ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ ਦਾ ਜਾਇਜ਼ਾ
   - AI ਪਾਈਪਲਾਈਨ ਵਿੱਚ ਮਿਆਰੀਕਰਨ ਕਿਉਂ ਮਹੱਤਵਪੂਰਨ ਹੈ
   - ਵਿਆਹਕ ਉਪਯੋਗ ਮਾਮਲੇ ਅਤੇ ਫਾਇਦੇ

2. **ਮੁੱਖ ਧਾਰਨਾਵਾਂ (01-CoreConcepts/)**
   - ਕਲਾਇੰਟ-ਸਰਵਰ ਆਰਕੀਟੈਕਚਰ
   - ਮੁੱਖ ਪ੍ਰੋਟੋਕੋਲ ਘਟਕ
   - MCP ਵਿੱਚ ਸੁਨੇਹਾ ਪੈਟਰਨ

3. **ਸੁਰੱਖਿਆ (02-Security/)**
   - MCP-ਅਧਾਰਿਤ ਸਿਸਟਮਾਂ ਵਿੱਚ ਸੁਰੱਖਿਆ ਖਤਰੇ
   - ਲਾਗੂ ਕਰਨ ਲਈ ਸੁਰੱਖਿਆ ਦੇ ਸ੍ਰੇਸ਼ਠ ਤਰੀਕੇ
   - ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਅਧਿਕਾਰਣ ਰਣਨੀਤੀਆਂ
   - **ਵਿਸਤ੍ਰਿਤ ਸੁਰੱਖਿਆ ਦਸਤਾਵੇਜ਼**:
     - MCP ਸੁਰੱਖਿਆ ਦੇ ਸ੍ਰੇਸ਼ਠ ਤਰੀਕੇ 2025
     - Azure ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ ਲਾਗੂ ਕਰਨ ਦੀ ਗਾਈਡ
     - MCP ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਅਤੇ ਤਕਨੀਕਾਂ
     - MCP ਸ੍ਰੇਸ਼ਠ ਤਰੀਕੇ ਤੇਜ਼ ਸੰਕੇਤ
   - **ਮੁੱਖ ਸੁਰੱਖਿਆ ਵਿਸ਼ੇ**:
     - ਪ੍ਰੋਮਪਟ ਇੰਜੈਕਸ਼ਨ ਅਤੇ ਟੂਲ ਪੌਇਜ਼ਨਿੰਗ ਹਮਲੇ
     - ਸੈਸ਼ਨ ਹਾਈਜੈਕਿੰਗ ਅਤੇ ਗਲਤ ਡਿਪਟੀ ਸਮੱਸਿਆਵਾਂ
     - ਟੋਕਨ ਪਾਸਥਰੂ ਭਰੋਸੇਮੰਦਤਾ
     - ਅਤਿ ਅਧਿਕਾਰ ਅਤੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ
     - AI ਘਟਕਾਂ ਲਈ ਸਪਲਾਈ ਚੇਨ ਸੁਰੱਖਿਆ
     - Microsoft Prompt Shields ਇੰਟੀਗ੍ਰੇਸ਼ਨ

4. **ਸ਼ੁਰੂਆਤ ਕਰਨਾ (03-GettingStarted/)**
   - ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ ਅਤੇ ਸੰਰਚਨਾ
   - ਬੁਨਿਆਦੀ MCP ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਬਣਾਉਣਾ
   - ਮੌਜੂਦਾ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
   - ਸ਼ਾਮਲ ਭਾਗ:
     - ਪਹਿਲਾ ਸਰਵਰ ਲਾਗੂ ਕਰਨਾ
     - ਕਲਾਇੰਟ ਵਿਕਾਸ
     - LLM ਕਲਾਇੰਟ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
     - VS ਕੋਡ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
     - ਸਰਵਰ-ਭੇਜੇ ਗਤੀਵਿਧੀਆਂ (SSE) ਸਰਵਰ
     - ਉੱਚ-ਸਤਹੀ ਸਰਵਰ ਦੀ ਵਰਤੋਂ
     - HTTP ਸਟ੍ਰੀਮਿੰਗ
     - AI ਟੂਲਕਿਟ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
     - ਟੈਸਟਿੰਗ ਰਣਨੀਤੀਆਂ
     - ਤੈਨਾਤੀ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

5. **ਵਿਆਹਕ ਲਾਗੂ ਕਰਨਾ (04-PracticalImplementation/)**
   - ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ SDKs ਦੀ ਵਰਤੋਂ
   - ਡੀਬੱਗਿੰਗ, ਟੈਸਟਿੰਗ, ਅਤੇ ਵੈਧਤਾ ਤਕਨੀਕਾਂ
   - ਦੁਬਾਰਾ ਵਰਤਣਯੋਗ ਪ੍ਰੋਮਪਟ ਟੈਂਪਲੇਟ ਅਤੇ ਵਰਕਫਲੋ ਬਣਾਉਣਾ
   - ਲਾਗੂ ਕਰਨ ਦੇ ਉਦਾਹਰਣਾਂ ਨਾਲ ਨਮੂਨਾ ਪ੍ਰੋਜੈਕਟ

6. **ਉੱਚ-ਸਤਹੀ ਵਿਸ਼ੇ (05-AdvancedTopics/)**
   - ਸੰਦਰਭ ਇੰਜੀਨੀਅਰਿੰਗ ਤਕਨੀਕਾਂ
   - Foundry ਏਜੰਟ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
   - ਮਲਟੀ-ਮੋਡਲ AI ਵਰਕਫਲੋ
   - OAuth2 ਪ੍ਰਮਾਣਿਕਤਾ ਡੈਮੋ
   - ਰੀਅਲ-ਟਾਈਮ ਖੋਜ ਸਮਰੱਥਾ
   - ਰੀਅਲ-ਟਾਈਮ ਸਟ੍ਰੀਮਿੰਗ
   - ਰੂਟ ਸੰਦਰਭ ਲਾਗੂ ਕਰਨਾ
   - ਰੂਟਿੰਗ ਰਣਨੀਤੀਆਂ
   - ਸੈਂਪਲਿੰਗ ਤਕਨੀਕਾਂ
   - ਸਕੇਲਿੰਗ ਪਹੁੰਚ
   - ਸੁਰੱਖਿਆ ਵਿਚਾਰ
   - Entra ID ਸੁਰੱਖਿਆ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
   - ਵੈੱਬ ਖੋਜ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

7. **ਸਮੁਦਾਇ ਯੋਗਦਾਨ (06-CommunityContributions/)**
   - ਕੋਡ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਯੋਗਦਾਨ ਦੇਣ ਦਾ ਤਰੀਕਾ
   - GitHub ਰਾਹੀਂ ਸਹਿਯੋਗ
   - ਸਮੁਦਾਇ-ਚਲਿਤ ਸੁਧਾਰ ਅਤੇ ਪ੍ਰਤੀਕਰਮ
   - ਵੱਖ-ਵੱਖ MCP ਕਲਾਇੰਟਾਂ ਦੀ ਵਰਤੋਂ (Claude Desktop, Cline, VSCode)
   - ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਸਮੇਤ ਪ੍ਰਸਿੱਧ MCP ਸਰਵਰਾਂ ਨਾਲ ਕੰਮ ਕਰਨਾ

8. **ਸ਼ੁਰੂਆਤੀ ਅਪਨਾਉਣ ਤੋਂ ਸਿੱਖਿਆ (07-LessonsfromEarlyAdoption/)**
   - ਅਸਲ-ਦੁਨੀਆ ਲਾਗੂ ਕਰਨ ਅਤੇ ਸਫਲਤਾ ਦੀਆਂ ਕਹਾਣੀਆਂ
   - MCP-ਅਧਾਰਿਤ ਹੱਲ ਬਣਾਉਣਾ ਅਤੇ ਤੈਨਾਤ ਕਰਨਾ
   - ਰੁਝਾਨ ਅਤੇ ਭਵਿੱਖ ਦਾ ਰੋਡਮੈਪ
   - **Microsoft MCP Servers Guide**: 10 ਉਤਪਾਦਨ-ਤਿਆਰ Microsoft MCP ਸਰਵਰਾਂ ਲਈ ਵਿਸਤ੍ਰਿਤ ਗਾਈਡ ਜਿਸ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:
     - Microsoft Learn Docs MCP Server
     - Azure MCP Server (15+ ਵਿਸ਼ੇਸ਼ ਕਨੈਕਟਰ)
     - GitHub MCP Server
     - Azure DevOps MCP Server
     - MarkItDown MCP Server
     - SQL Server MCP Server
     - Playwright MCP Server
     - Dev Box MCP Server
     - Azure AI Foundry MCP Server
     - Microsoft 365 Agents Toolkit MCP Server

9. **ਸ੍ਰੇਸ਼ਠ ਤਰੀਕੇ (08-BestPractices/)**
   - ਪ੍ਰਦਰਸ਼ਨ ਟਿਊਨਿੰਗ ਅਤੇ ਅਨੁਕੂਲਤਾ
   - ਫਾਲਟ-ਟੋਲਰੈਂਟ MCP ਸਿਸਟਮ ਡਿਜ਼ਾਈਨ ਕਰਨਾ
   - ਟੈਸਟਿੰਗ ਅਤੇ ਲਚੀਲਾਪਨ ਰਣਨੀਤੀਆਂ

10. **ਕੇਸ ਸਟਡੀਜ਼ (09-CaseStudy/)**
    - **ਸੱਤ ਵਿਸਤ੍ਰਿਤ ਕੇਸ ਸਟਡੀਜ਼** ਜੋ ਵੱਖ-ਵੱਖ ਸਥਿਤੀਆਂ ਵਿੱਚ MCP ਦੀ ਬਹੁ-ਪੱਖਤਾ ਨੂੰ ਦਰਸਾਉਂਦੀਆਂ ਹਨ:
    - **Azure AI Travel Agents**: Azure OpenAI ਅਤੇ AI Search ਨਾਲ ਮਲਟੀ-ਏਜੰਟ ਆਰਕੈਸਟ੍ਰੇਸ਼ਨ
    - **Azure DevOps ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: YouTube ਡੇਟਾ ਅਪਡੇਟਾਂ ਨਾਲ ਵਰਕਫਲੋ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਆਟੋਮੇਟ ਕਰਨਾ
    - **ਰੀਅਲ-ਟਾਈਮ ਦਸਤਾਵੇਜ਼ ਪ੍ਰਾਪਤੀ**: ਸਟ੍ਰੀਮਿੰਗ HTTP ਨਾਲ Python ਕਨਸੋਲ ਕਲਾਇੰਟ
    - **ਇੰਟਰਐਕਟਿਵ ਅਧਿਐਨ ਯੋਜਨਾ ਜਨਰੇਟਰ**: ਚੇਨਲਿਟ ਵੈੱਬ ਐਪ ਨਾਲ ਗੱਲਬਾਤੀ AI
    - **ਇਨ-ਐਡੀਟਰ ਦਸਤਾਵੇਜ਼**: GitHub Copilot ਵਰਕਫਲੋ ਨਾਲ VS Code ਇੰਟੀਗ੍ਰੇਸ਼ਨ
    - **Azure API ਪ੍ਰਬੰਧਨ**: MCP ਸਰਵਰ ਬਣਾਉਣ ਨਾਲ ਐਨਟਰਪ੍ਰਾਈਜ਼ API ਇੰਟੀਗ੍ਰੇਸ਼ਨ
    - **GitHub MCP ਰਜਿਸਟਰੀ**: ਪਰਿਸਰ ਵਿਕਾਸ ਅਤੇ ਏਜੰਟਿਕ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਪਲੇਟਫਾਰਮ
    - ਕਾਰੋਬਾਰੀ ਇੰਟੀਗ੍ਰੇਸ਼ਨ, ਡਿਵੈਲਪਰ ਉਤਪਾਦਕਤਾ, ਅਤੇ ਪਰਿਸਰ ਵਿਕਾਸ ਨੂੰ ਕਵਰ ਕਰਨ ਵਾਲੇ ਲਾਗੂ ਕਰਨ ਦੇ ਉਦਾਹਰਣ

11. **ਹੱਥ-ਅਨੁਭਵ ਵਰਕਸ਼ਾਪ (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - MCP ਨੂੰ AI ਟੂਲਕਿਟ ਨਾਲ ਜੋੜਨ ਵਾਲੀ ਵਿਸਤ੍ਰਿਤ ਹੱਥ-ਅਨੁਭਵ ਵਰਕਸ਼ਾਪ
    - ਅੰਮੂਹ ਮਾਡਲਾਂ ਨੂੰ ਅਸਲ-ਦੁਨੀਆ ਦੇ ਟੂਲਾਂ ਨਾਲ ਜੋੜਨ ਵਾਲੇ ਬੁੱਧੀਮਾਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ
    - ਬੁਨਿਆਦੀਆਂ, ਕਸਟਮ ਸਰਵਰ ਵਿਕਾਸ, ਅਤੇ ਉਤਪਾਦਨ ਤੈਨਾਤੀ ਰਣਨੀਤੀਆਂ ਨੂੰ ਕਵਰ ਕਰਨ ਵਾਲੇ ਵਿਹਾਰਕ ਮੌਡਿਊਲ
    - **ਲੈਬ ਬਣਤਰ**:
      - ਲੈਬ 1: MCP ਸਰਵਰ ਬੁਨਿਆਦੀਆਂ
      - ਲੈਬ 2: ਉੱਚ-ਸਤਹੀ MCP ਸਰਵਰ ਵਿਕਾਸ
      - ਲੈਬ 3: AI ਟੂਲਕਿਟ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
      - ਲੈਬ 4: ਉਤਪਾਦਨ ਤੈਨਾਤੀ ਅਤੇ ਸਕੇਲਿੰਗ
    - ਕਦਮ-ਦਰ-ਕਦਮ ਹਦਾਇਤਾਂ ਨਾਲ ਲੈਬ-ਅਧਾਰਿਤ ਸਿੱਖਣ ਦਾ ਦ੍ਰਿਸ਼ਟੀਕੋਣ

12. **MCP ਸਰਵਰ ਡੇਟਾਬੇਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲੈਬਜ਼ (11-MCPServerHandsOnLabs/)**
    - **13-ਲੈਬ ਸਿੱਖਣ ਪਾਠਕ੍ਰਮ** ਜੋ PostgreSQL ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨਾਲ ਉਤਪਾਦਨ-ਤਿਆਰ MCP ਸਰਵਰ ਬਣਾਉਣ ਲਈ ਹੈ
    - **ਅਸਲ-ਦੁਨੀਆ ਰਿਟੇਲ ਵਿਸ਼ਲੇਸ਼ਣ ਲਾਗੂ ਕਰਨਾ** Zava Retail ਵਰਤੋਂ ਦੇ ਕੇਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ
    - **ਐਨਟਰਪ੍ਰਾਈਜ਼-ਗਰੇਡ ਪੈਟਰਨ** ਜਿਸ ਵਿੱਚ Row Level Security (RLS), ਸੈਮੈਂਟਿਕ ਖੋਜ, ਅਤੇ ਮਲਟੀ-ਟੈਨੈਂਟ ਡੇਟਾ ਪਹੁੰਚ ਸ਼ਾਮਲ ਹੈ
    - **ਪੂਰੀ ਲੈਬ ਬਣਤਰ**:
      - **ਲੈਬਜ਼ 00-03: ਬੁਨਿਆਦੀਆਂ** - ਪ੍ਰਸਤਾਵਨਾ, ਆਰਕੀਟੈਕਚਰ, ਸੁਰੱਖਿਆ, ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ
      - **ਲੈਬਜ਼ 04-06: MCP ਸਰਵਰ ਬਣਾਉਣਾ** - ਡੇਟਾਬੇਸ ਡਿਜ਼ਾਈਨ, MCP ਸਰਵਰ ਲਾਗੂ ਕਰਨਾ, ਟੂਲ ਵਿਕਾਸ
      - **ਲੈਬਜ਼ 07-09: ਉੱਚ-ਸਤਹੀ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ** - ਸੈਮੈਂਟਿਕ ਖੋਜ, ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ, VS Code ਇੰਟੀਗ੍ਰੇਸ਼ਨ
      - **ਲੈਬਜ਼ 10-12: ਉਤਪਾਦਨ ਅਤੇ ਸ੍ਰੇਸ਼ਠ ਤਰੀਕੇ** - ਤੈਨਾਤੀ, ਨਿਗਰਾਨੀ, ਅਨੁਕੂਲਤਾ
    - **ਕਵਰ ਕੀਤੀਆਂ ਤਕਨੀਕਾਂ**: FastMCP ਫਰੇਮਵਰਕ, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **ਸਿੱਖਣ ਦੇ ਨਤੀਜੇ**: ਉਤਪਾਦਨ-ਤਿਆਰ MCP ਸਰਵਰ, ਡੇਟਾਬੇਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਪੈਟਰਨ, AI-ਚਲਿਤ ਵਿਸ਼ਲੇਸ਼ਣ, ਐਨਟਰਪ੍ਰਾਈਜ਼ ਸੁਰੱਖਿਆ

## ਵਾਧੂ ਸਰੋਤ

ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਸਹਾਇਕ ਸਰੋਤ ਸ਼ਾਮਲ ਹਨ:

- **ਚਿੱਤਰਾਂ ਫੋਲਡਰ**: ਪਾਠਕ੍ਰਮ ਵਿੱਚ ਵਰਤੇ ਗਏ ਡਾਇਗ੍ਰਾਮ ਅਤੇ ਚਿੱਤਰਾਂ ਸ਼ਾਮਲ ਹਨ
- **ਅਨੁਵਾਦ**: ਦਸਤਾਵੇਜ਼ਾਂ ਦੇ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਨਾਲ ਬਹੁ-ਭਾਸ਼ਾ ਸਹਾਇਤਾ
- **ਅਧਿਕਾਰਤ MCP ਸਰੋਤ**:
  - [MCP ਦਸਤਾਵੇਜ਼](https://modelcontextprotocol.io/)
  - [MCP ਵਿਸ਼ੇਸ਼ਤਾ](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub ਰਿਪੋਜ਼ਟਰੀ](https://github.com/modelcontextprotocol)

## ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ

1. **ਕ੍ਰਮਵਾਰ ਸਿੱਖਣਾ**: ਇੱਕ ਸੰਰਚਿਤ ਸਿੱਖਣ ਅਨੁਭਵ ਲਈ ਅਧਿਆਇ 00 ਤੋਂ 11 ਤੱਕ ਕ੍ਰਮਵਾਰ ਅਨੁਸਰਣ ਕਰੋ।
2. **ਭਾਸ਼ਾ-ਵਿਸ਼ੇਸ਼ ਧਿਆਨ**: ਜੇ ਤੁਸੀਂ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਪ੍ਰੋਗਰਾਮਿੰਗ ਭਾਸ਼ਾ ਵਿੱਚ ਦਿਲਚਸਪੀ ਰੱਖਦੇ ਹੋ, ਤਾਂ ਆਪਣੇ ਪਸੰਦੀਦਾ ਭਾਸ਼ਾ ਵਿੱਚ ਲਾਗੂ ਕਰਨ ਲਈ ਨਮੂਨਾ ਡਾਇਰੈਕਟਰੀਜ਼ ਦੀ ਖੋਜ ਕਰੋ।
3. **ਵਿਆਹਕ ਲਾਗੂ ਕਰਨਾ**: "ਸ਼ੁਰੂਆਤ ਕਰਨਾ" ਭਾਗ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ ਤਾਂ ਜੋ ਆਪਣਾ ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ ਕਰੋ ਅਤੇ ਆਪਣਾ ਪਹਿਲਾ MCP ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਬਣਾਓ।
4. **ਉੱਚ-ਸਤਹੀ ਖੋਜ**: ਜਦੋਂ ਬੁਨਿਆਦੀਆਂ ਨਾਲ ਆਰਾਮਦਾਇਕ ਹੋ ਜਾਓ, ਤਾਂ ਉੱਚ-ਸਤਹੀ ਵਿਸ਼ਿਆਂ ਵਿੱਚ ਡੁੱਬੋ ਤਾਂ ਜੋ ਆਪਣਾ ਗਿਆਨ ਵਧਾਓ।
5. **ਸਮੁਦਾਇ ਸਹਿਭਾਗਤਾ**: GitHub ਚਰਚਾ ਅਤੇ Discord ਚੈਨਲਾਂ ਰਾਹੀਂ MCP ਸਮੁਦਾਇ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ ਤਾਂ ਜੋ ਮਾਹਰਾਂ ਅਤੇ ਸਾਥੀ ਡਿਵੈਲਪਰਾਂ ਨਾਲ ਜੁੜ ਸਕੋ।

## MCP ਕਲਾਇੰਟ ਅਤੇ ਟੂਲ

ਪਾਠਕ੍ਰਮ ਵੱਖ-ਵੱਖ MCP ਕਲਾਇੰਟਾਂ ਅਤੇ ਟੂਲਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ:

1. **ਅਧਿਕਾਰਤ ਕਲਾਇੰਟ**:
   - Visual Studio Code 
   - MCP in Visual Studio Code
   - Claude Desktop
   - Claude in VSCode 
   - Claude API

2. **ਸਮੁਦਾਇ ਕਲਾਇੰਟ**:
   - Cline (ਟਰਮੀਨਲ-ਅਧਾਰਿਤ)
   - Cursor (ਕੋਡ ਐਡੀਟਰ)
   - ChatMCP
   - Windsurf

3. **MCP ਪ੍ਰਬੰਧਨ ਟੂਲ**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## ਪ੍ਰਸਿੱਧ MCP ਸਰਵਰ

ਰਿਪੋਜ਼ਟਰੀ ਵੱਖ-ਵੱਖ MCP ਸਰਵਰਾਂ ਨੂੰ ਪੇਸ਼ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

1. **ਅਧਿਕਾਰਤ Microsoft MCP ਸਰਵਰ**:
   - Microsoft Learn Docs MCP Server
   - Azure MCP Server (15+ ਵਿਸ਼ੇਸ਼ ਕਨੈਕਟਰ)
   - GitHub MCP Server
   - Azure DevOps MCP Server
   - MarkItDown MCP Server
   - SQL Server MCP Server
   - Playwright MCP Server
   - Dev Box MCP Server
   - Azure AI Foundry MCP Server
   - Microsoft 365 Agents Toolkit MCP Server

2. **ਅਧਿਕਾਰਤ ਰਿਫਰੈਂਸ ਸਰਵਰ**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **ਵਿਕਾਸ ਟੂਲ**:
   - Git MCP
  

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।