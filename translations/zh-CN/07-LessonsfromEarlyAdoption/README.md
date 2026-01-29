# 🌟 从早期采用者中学习

[![从 MCP 早期采用者中学习](../../../translated_images/zh-CN/08.980bb2babbaadd8a97739effc9b31e5f1abd8f4c4a3fbc90fb9f931a866674d0.png)](https://youtu.be/jds7dSmNptE)

_（点击上方图片观看本课视频）_

## 🎯 本模块涵盖内容

本模块探讨了真实的组织和开发者如何利用 Model Context Protocol (MCP) 来解决实际问题并推动创新。通过详细的案例研究和实践项目，您将了解 MCP 如何实现安全、可扩展的 AI 集成，将语言模型、工具和企业数据连接在一起。

### 📚 了解 MCP 的实际应用

想看看这些原则如何应用于生产工具？请查看我们的 [**10 个正在改变开发者生产力的 Microsoft MCP 服务器**](microsoft-mcp-servers.md)，其中展示了您今天就可以使用的真实 Microsoft MCP 服务器。

## 概述

本课程探讨了早期采用者如何利用 Model Context Protocol (MCP) 来解决现实中的挑战，并推动各行业的创新。通过详细的案例研究和实践项目，您将看到 MCP 如何实现标准化、安全且可扩展的 AI 集成——在一个统一框架中连接大型语言模型、工具和企业数据。您将获得设计和构建基于 MCP 的解决方案的实践经验，学习经过验证的实施模式，并发现将 MCP 部署到生产环境中的最佳实践。本课程还重点介绍了新兴趋势、未来方向以及帮助您保持 MCP 技术及其生态系统前沿的开源资源。

## 学习目标

- 分析不同行业的实际 MCP 实现
- 设计并构建完整的基于 MCP 的应用程序
- 探索 MCP 技术的新兴趋势和未来方向
- 在实际开发场景中应用最佳实践

## 实际 MCP 实现

### 案例研究 1：企业客户支持自动化

一家跨国公司实施了基于 MCP 的解决方案，以标准化其客户支持系统中的 AI 交互。这使他们能够：

- 为多个 LLM 提供商创建统一接口
- 在各部门之间保持一致的提示管理
- 实现强大的安全性和合规性控制
- 根据具体需求轻松切换不同的 AI 模型

**技术实现：**

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

**结果：** 模型成本降低 30%，响应一致性提高 45%，并增强了全球运营的合规性。

### 案例研究 2：医疗诊断助手

一家医疗服务提供商开发了 MCP 基础设施，以集成多个专业医疗 AI 模型，同时确保敏感的患者数据得到保护：

- 在通用和专业医疗模型之间无缝切换
- 严格的隐私控制和审计记录
- 与现有电子健康记录 (EHR) 系统集成
- 针对医学术语的一致提示工程

**技术实现：**

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

**结果：** 为医生提供改进的诊断建议，同时完全符合 HIPAA 标准，并显著减少了系统间的上下文切换。

### 案例研究 3：金融服务风险分析

一家金融机构实施了 MCP，以标准化其不同部门的风险分析流程：

- 为信用风险、欺诈检测和投资风险模型创建统一接口
- 实施严格的访问控制和模型版本管理
- 确保所有 AI 推荐的可审计性
- 在不同系统之间保持一致的数据格式

**技术实现：**

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

**结果：** 增强了监管合规性，模型部署周期加快 40%，并提高了各部门的风险评估一致性。

### 案例研究 4：Microsoft Playwright MCP 服务器用于浏览器自动化

Microsoft 开发了 [Playwright MCP 服务器](https://github.com/microsoft/playwright-mcp)，通过 Model Context Protocol 实现安全、标准化的浏览器自动化。这个生产级服务器允许 AI 代理和 LLM 在受控、可审计和可扩展的环境中与网页浏览器交互，支持自动化网页测试、数据提取和端到端工作流等用例。

> **🎯 生产级工具**
> 
> 本案例展示了一个您今天就可以使用的真实 MCP 服务器！了解更多关于 Playwright MCP 服务器及其他 9 个生产级 Microsoft MCP 服务器的信息，请参阅我们的 [**Microsoft MCP 服务器指南**](microsoft-mcp-servers.md#8--playwright-mcp-server)。

**主要功能：**
- 将浏览器自动化功能（导航、表单填写、截图捕获等）作为 MCP 工具暴露
- 实现严格的访问控制和沙箱机制以防止未经授权的操作
- 提供所有浏览器交互的详细审计日志
- 支持与 Azure OpenAI 和其他 LLM 提供商集成，实现代理驱动的自动化
- 为 GitHub Copilot 的编码代理提供网页浏览功能

**技术实现：**

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

**结果：**

- 为 AI 代理和 LLM 实现了安全的程序化浏览器自动化
- 减少了手动测试工作量，提高了网页应用的测试覆盖率
- 提供了一个可重用、可扩展的框架，用于企业环境中的基于浏览器的工具集成
- 为 GitHub Copilot 提供了网页浏览功能

**参考资料：**

- [Playwright MCP 服务器 GitHub 仓库](https://github.com/microsoft/playwright-mcp)
- [Microsoft AI 和自动化解决方案](https://azure.microsoft.com/en-us/products/ai-services/)

### 案例研究 5：Azure MCP – 企业级 Model Context Protocol 即服务

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) 是 Microsoft 提供的企业级托管 Model Context Protocol 实现，旨在作为云服务提供可扩展、安全且合规的 MCP 服务器功能。Azure MCP 使组织能够快速部署、管理和集成 MCP 服务器与 Azure AI、数据和安全服务，从而减少运营开销并加速 AI 采用。

> **🎯 生产级工具**
> 
> 这是一个您今天就可以使用的真实 MCP 服务器！了解更多关于 Azure AI Foundry MCP 服务器的信息，请参阅我们的 [**Microsoft MCP 服务器指南**](microsoft-mcp-servers.md)。

- 提供内置扩展、监控和安全功能的完全托管 MCP 服务器托管服务
- 与 Azure OpenAI、Azure AI Search 和其他 Azure 服务的原生集成
- 通过 Microsoft Entra ID 实现企业级身份验证和授权
- 支持自定义工具、提示模板和资源连接器
- 符合企业安全和监管要求

**技术实现：**

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

**结果：**  
- 通过提供即用型、合规的 MCP 服务器平台，缩短了企业 AI 项目的价值实现时间  
- 简化了 LLM、工具和企业数据源的集成  
- 增强了 MCP 工作负载的安全性、可观测性和运营效率  
- 使用 Azure SDK 最佳实践和当前身份验证模式提高了代码质量  

**参考资料：**  
- [Azure MCP 文档](https://aka.ms/azmcp)  
- [Azure MCP 服务器 GitHub 仓库](https://github.com/Azure/azure-mcp)  
- [Azure AI 服务](https://azure.microsoft.com/en-us/products/ai-services/)  
- [Microsoft MCP 中心](https://mcp.azure.com)  

### 案例研究 6：NLWeb

MCP（Model Context Protocol）是一种新兴协议，用于让聊天机器人和 AI 助手与工具交互。每个 NLWeb 实例也是一个 MCP 服务器，支持一个核心方法 `ask`，用于以自然语言向网站提问。返回的响应利用了 schema.org，这是一种广泛使用的描述网页数据的词汇表。简单来说，MCP 之于 NLWeb 就像 Http 之于 HTML。NLWeb 结合了协议、Schema.org 格式和示例代码，帮助网站快速创建这些端点，从而通过对话界面为人类提供便利，并通过自然的代理间交互为机器提供支持。

NLWeb 包含两个主要组件：
- 一个简单的协议，用于以自然语言与网站交互，以及一种格式，利用 JSON 和 schema.org 返回答案。有关 REST API 的更多详细信息，请参阅文档。
- 一个基于现有标记的简单实现，适用于可以抽象为项目列表（如产品、食谱、景点、评论等）的站点。结合一组用户界面小部件，网站可以轻松为其内容提供对话界面。有关聊天查询生命周期的更多详细信息，请参阅文档。

**参考资料：**  
- [Azure MCP 文档](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)  

### 案例研究 7：Azure AI Foundry MCP 服务器 – 企业 AI 代理集成

Azure AI Foundry MCP 服务器展示了 MCP 如何用于在企业环境中编排和管理 AI 代理及工作流。通过将 MCP 与 Azure AI Foundry 集成，组织可以标准化代理交互，利用 Foundry 的工作流管理，并确保安全、可扩展的部署。

> **🎯 生产级工具**
> 
> 这是一个您今天就可以使用的真实 MCP 服务器！了解更多关于 Azure AI Foundry MCP 服务器的信息，请参阅我们的 [**Microsoft MCP 服务器指南**](microsoft-mcp-servers.md#9--azure-ai-foundry-mcp-server)。

**主要功能：**
- 全面访问 Azure 的 AI 生态系统，包括模型目录和部署管理
- 使用 Azure AI Search 进行知识索引，支持 RAG 应用
- 提供 AI 模型性能和质量保证的评估工具
- 与 Azure AI Foundry Catalog 和 Labs 集成，支持前沿研究模型
- 为生产场景提供代理管理和评估能力

**结果：**
- 快速原型设计和对 AI 代理工作流的强大监控
- 与 Azure AI 服务无缝集成，支持高级场景
- 为构建、部署和监控代理管道提供统一接口
- 提高了企业的安全性、合规性和运营效率
- 在保持对复杂代理驱动流程控制的同时，加速了 AI 的采用

**参考资料：**
- [Azure AI Foundry MCP 服务器 GitHub 仓库](https://github.com/azure-ai-foundry/mcp-foundry)  
- [将 Azure AI 代理与 MCP 集成（Microsoft Foundry 博客）](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)  

### 案例研究 8：Foundry MCP Playground – 实验与原型设计

Foundry MCP Playground 提供了一个即用型环境，用于实验 MCP 服务器和 Azure AI Foundry 集成。开发者可以快速原型设计、测试和评估 AI 模型及代理工作流，利用 Azure AI Foundry Catalog 和 Labs 的资源。Playground 简化了设置，提供示例项目，并支持协作开发，使团队能够以最小的开销探索最佳实践和新场景。通过降低入门门槛，Playground 有助于在 MCP 和 Azure AI Foundry 生态系统中促进创新和社区贡献。

**参考资料：**

- [Foundry MCP Playground GitHub 仓库](https://github.com/azure-ai-foundry/foundry-mcp-playground)  

### 案例研究 9：Microsoft Learn Docs MCP 服务器 – AI 驱动的文档访问

Microsoft Learn Docs MCP 服务器是一个云托管服务，通过 Model Context Protocol 为 AI 助手提供实时访问官方 Microsoft 文档的能力。这个生产级服务器连接到全面的 Microsoft Learn 生态系统，并支持对所有官方 Microsoft 资源的语义搜索。
> **🎯 适用于生产环境的工具**  
>  
> 这是一个可以立即使用的真实 MCP 服务器！在我们的 [**Microsoft MCP 服务器指南**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server) 中了解更多信息。
**主要功能：**
- 实时访问官方微软文档、Azure文档和Microsoft 365文档
- 高级语义搜索功能，能够理解上下文和意图
- 随着Microsoft Learn内容发布，信息始终保持最新
- 全面覆盖Microsoft Learn、Azure文档和Microsoft 365资源
- 返回最多10个高质量内容片段，包括文章标题和URL

**为什么至关重要：**
- 解决微软技术领域“过时的AI知识”问题
- 确保AI助手能够访问最新的.NET、C#、Azure和Microsoft 365功能
- 提供权威的一手信息以生成准确的代码
- 对于使用快速发展的微软技术的开发者来说至关重要

**结果：**
- 显著提高AI生成的微软技术代码的准确性
- 减少查找最新文档和最佳实践所花费的时间
- 通过上下文感知的文档检索提升开发者生产力
- 无需离开IDE即可与开发工作流无缝集成

**参考资料：**
- [Microsoft Learn Docs MCP Server GitHub Repository](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn Documentation](https://learn.microsoft.com/)

## 实践项目

### 项目1：构建多提供商MCP服务器

**目标：** 创建一个MCP服务器，根据特定条件将请求路由到多个AI模型提供商。

**需求：**
- 支持至少三个不同的模型提供商（例如OpenAI、Anthropic、本地模型）
- 实现基于请求元数据的路由机制
- 创建一个配置系统以管理提供商凭证
- 添加缓存以优化性能和成本
- 构建一个简单的仪表板以监控使用情况

**实施步骤：**
1. 设置基本的MCP服务器基础架构
2. 为每个AI模型服务实现提供商适配器
3. 创建基于请求属性的路由逻辑
4. 添加频繁请求的缓存机制
5. 开发监控仪表板
6. 使用各种请求模式进行测试

**技术选择：** 可选择Python（.NET/Java/Python根据偏好），Redis用于缓存，以及一个简单的Web框架用于仪表板。

### 项目2：企业提示管理系统

**目标：** 开发一个基于MCP的系统，用于管理、版本控制和部署组织内的提示模板。

**需求：**
- 创建一个集中式提示模板存储库
- 实现版本控制和审批工作流
- 构建带有示例输入的模板测试功能
- 开发基于角色的访问控制
- 创建一个用于模板检索和部署的API

**实施步骤：**
1. 设计用于模板存储的数据库架构
2. 创建用于模板CRUD操作的核心API
3. 实现版本控制系统
4. 构建审批工作流
5. 开发测试框架
6. 创建一个简单的Web界面用于管理
7. 与MCP服务器集成

**技术选择：** 可选择后端框架、SQL或NoSQL数据库，以及一个前端框架用于管理界面。

### 项目3：基于MCP的内容生成平台

**目标：** 构建一个内容生成平台，利用MCP为不同内容类型提供一致的结果。

**需求：**
- 支持多种内容格式（博客文章、社交媒体、营销文案）
- 实现基于模板的生成并提供自定义选项
- 创建内容审查和反馈系统
- 跟踪内容性能指标
- 支持内容版本控制和迭代

**实施步骤：**
1. 设置MCP客户端基础架构
2. 为不同内容类型创建模板
3. 构建内容生成管道
4. 实现审查系统
5. 开发指标跟踪系统
6. 创建用于模板管理和内容生成的用户界面

**技术选择：** 可选择的编程语言、Web框架和数据库系统。

## MCP技术的未来方向

### 新兴趋势

1. **多模态MCP**
   - 扩展MCP以标准化与图像、音频和视频模型的交互
   - 开发跨模态推理能力
   - 为不同模态制定标准化提示格式

2. **联邦MCP基础架构**
   - 分布式MCP网络，可在组织间共享资源
   - 安全模型共享的标准化协议
   - 隐私保护计算技术

3. **MCP市场**
   - 用于共享和货币化MCP模板和插件的生态系统
   - 质量保证和认证流程
   - 与模型市场集成

4. **用于边缘计算的MCP**
   - 针对资源受限的边缘设备优化MCP标准
   - 低带宽环境的优化协议
   - 专为物联网生态系统设计的MCP实现

5. **监管框架**
   - 开发用于监管合规的MCP扩展
   - 标准化审计记录和可解释性接口
   - 与新兴AI治理框架集成

### 来自微软的MCP解决方案

微软和Azure开发了多个开源存储库，帮助开发者在各种场景中实现MCP：

#### Microsoft组织

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - 用于浏览器自动化和测试的Playwright MCP服务器
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - 用于本地测试和社区贡献的OneDrive MCP服务器实现
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWeb是开放协议和相关开源工具的集合，主要关注建立AI Web的基础层

#### Azure-Samples组织

1. [mcp](https://github.com/Azure-Samples/mcp) - 提供样例、工具和资源，用于使用多种语言在Azure上构建和集成MCP服务器
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - 展示当前模型上下文协议规范的认证参考MCP服务器
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - 使用Azure Functions实现远程MCP服务器的主页，包含语言特定的存储库链接
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用Python构建和部署自定义远程MCP服务器的快速入门模板
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用.NET/C#构建和部署自定义远程MCP服务器的快速入门模板
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用TypeScript构建和部署自定义远程MCP服务器的快速入门模板
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - 使用Python将Azure API管理作为远程MCP服务器的AI网关
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - 包括MCP功能的APIM ❤️ AI实验，集成Azure OpenAI和AI Foundry

这些存储库提供了各种实现、模板和资源，用于在不同编程语言和Azure服务中使用模型上下文协议。它们涵盖了从基本服务器实现到认证、云部署和企业集成场景的广泛用例。

#### MCP资源目录

官方微软MCP存储库中的[MCP资源目录](https://github.com/microsoft/mcp/tree/main/Resources)提供了一系列样例资源、提示模板和工具定义，用于模型上下文协议服务器。这些资源旨在帮助开发者快速入门MCP，提供可重用的构建模块和最佳实践示例，包括：

- **提示模板：** 可用于常见AI任务和场景的现成提示模板，可根据自己的MCP服务器实现进行调整。
- **工具定义：** 标准化工具集成和调用的示例工具架构和元数据。
- **资源样例：** 用于在MCP框架中连接数据源、API和外部服务的示例资源定义。
- **参考实现：** 展示如何在实际MCP项目中结构化和组织资源、提示和工具的实用样例。

这些资源加速开发，促进标准化，并帮助确保在构建和部署基于MCP的解决方案时采用最佳实践。

#### MCP资源目录

- [MCP资源（样例提示、工具和资源定义）](https://github.com/microsoft/mcp/tree/main/Resources)

### 研究机会

- MCP框架内高效提示优化技术
- 多租户MCP部署的安全模型
- 不同MCP实现的性能基准测试
- MCP服务器的形式化验证方法

## 结论

模型上下文协议（MCP）正在快速塑造跨行业标准化、安全和可互操作的AI集成的未来。通过本课程中的案例研究和实践项目，你已经看到早期采用者（包括微软和Azure）如何利用MCP解决现实世界的挑战，加速AI采用，并确保合规性、安全性和可扩展性。MCP的模块化方法使组织能够在统一、可审计的框架中连接大型语言模型、工具和企业数据。随着MCP的不断发展，积极参与社区、探索开源资源并应用最佳实践将是构建强大、面向未来的AI解决方案的关键。

## 其他资源

- [MCP Foundry GitHub Repository](https://github.com/azure-ai-foundry/mcp-foundry)
- [Foundry MCP Playground](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [Integrating Azure AI Agents with MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
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

## 练习

1. 分析一个案例研究并提出替代的实施方法。
2. 选择一个项目想法并创建详细的技术规范。
3. 研究案例研究中未涉及的行业，并概述MCP如何解决其特定挑战。
4. 探索一个未来方向并设计一个新的MCP扩展概念以支持该方向。

下一步：[Microsoft MCP Server](../07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们概不负责。