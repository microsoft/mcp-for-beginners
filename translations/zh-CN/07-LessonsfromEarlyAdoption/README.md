# 🌟 早期采用者的经验教训

[![MCP 早期采用者的经验教训](../../../translated_images/zh-CN/08.980bb2babbaadd8a.webp)](https://youtu.be/jds7dSmNptE)

_(点击上方图片观看本课程视频)_

## 🎯 本模块涵盖内容

本模块探讨了真实组织和开发者如何利用模型上下文协议（MCP）解决实际挑战并推动创新。通过详细的案例分析、动手项目和实用示例，您将发现 MCP 如何实现安全、可扩展的 AI 集成，连接语言模型、工具和企业数据。

### 📚 观看 MCP 实际应用

想看这些原则如何应用于生产就绪的工具？请查看我们的[**10 个正在改变开发者生产力的微软 MCP 服务器**](microsoft-mcp-servers.md)，展示您今天可以使用的真实微软 MCP 服务器。

## 概述

本课程探讨了早期采用者如何利用模型上下文协议（MCP）解决现实世界的难题并推动跨行业创新。通过详细案例和动手项目，您将了解 MCP 如何实现标准化、安全且可扩展的 AI 集成——在统一框架内连接大型语言模型、工具和企业数据。您将获得设计和构建基于 MCP 解决方案的实用经验，学习成熟的实现模式，并发现生产环境部署 MCP 的最佳实践。课程还将重点介绍新兴趋势、未来方向及开源资源，助您保持 MCP 技术及其不断发展的生态系统的前沿地位。

## 学习目标

- 分析不同行业中的真实 MCP 实现
- 设计并构建完整的基于 MCP 的应用
- 探索 MCP 技术的新兴趋势和未来方向
- 在实际开发场景中应用最佳实践

## 真实世界的 MCP 实现

### 案例研究 1：企业客户支持自动化

一家跨国公司实施了基于 MCP 的解决方案，以标准化其客户支持系统中的 AI 交互。该方案使他们能够：

- 为多个 LLM 提供商创建统一接口
- 跨部门保持一致的提示管理
- 实施强有力的安全与合规控制
- 根据特定需求轻松切换不同 AI 模型

**技术实现：**

```python
# Python MCP 服务器实现用于客户支持
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# 配置日志记录
logging.basicConfig(level=logging.INFO)

async def main():
    # 创建服务器配置
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # 初始化 MCP 服务器
    server = create_server(config)
    
    # 注册知识库资源
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # 注册提示模板
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # 注册支持工具
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # 使用 HTTP 传输启动服务器
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**结果：** 模型成本降低 30%，响应一致性提升 45%，并增强了全球运营的合规性。

### 案例研究 2：医疗诊断助手

一家医疗提供者开发了 MCP 基础设施以集成多个专业医疗 AI 模型，同时确保敏感患者数据受到保护：

- 无缝切换通用和专业医疗模型
- 严格的隐私控制和审计轨迹
- 与现有电子健康记录 (EHR) 系统集成
- 医学术语一致的提示工程

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

**结果：** 改进了医生的诊断建议，同时保持完全的 HIPAA 合规性，并显著减少了系统间的上下文切换。

### 案例研究 3：金融服务风险分析

一家金融机构采用 MCP 标准化其在不同部门的风险分析流程：

- 创建了信用风险、欺诈检测和投资风险模型的统一接口
- 实施严格的访问控制和模型版本管理
- 确保所有 AI 建议的可审计性
- 维护各系统间一致的数据格式

**技术实现：**

```java
// 用于金融风险评估的Java MCP服务器
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // 创建具有金融合规功能的MCP服务器
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

**结果：** 改善了监管合规性，模型部署周期加快了 40%，各部门的风险评估一致性提升。

### 案例研究 4：微软 Playwright MCP 服务器用于浏览器自动化

微软开发了 [Playwright MCP 服务器](https://github.com/microsoft/playwright-mcp)，通过模型上下文协议实现安全、标准化的浏览器自动化。此生产就绪服务器允许 AI 代理和 LLM 在受控、可审计且可扩展的环境中与网页浏览器交互——支持自动化网页测试、数据提取和端到端工作流程等用例。

> **🎯 生产就绪工具**
> 
> 本案例展示了您今天可以使用的真实 MCP 服务器！了解更多关于 Playwright MCP 服务器以及其他 9 个生产就绪微软 MCP 服务器，见我们的[**微软 MCP 服务器指南**](microsoft-mcp-servers.md#8--playwright-mcp-server)。

**核心特性：**
- 将浏览器自动化功能（导航、表单填写、截图等）作为 MCP 工具暴露
- 实施严格的访问控制和沙箱机制，防止未经授权的操作
- 提供详细的浏览器交互审计日志
- 支持与 Azure OpenAI 及其他 LLM 提供商集成实现代理驱动自动化
- 为 GitHub Copilot 的编程代理提供网页浏览能力

**技术实现：**

```typescript
// TypeScript：在 MCP 服务器中注册 Playwright 浏览器自动化工具
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// 注册一个用于导航到 URL 并捕获屏幕截图的工具
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

// 启动 MCP 服务器
server.listen(8080);
```

**结果：**

- 实现了 AI 代理和 LLM 的安全程序化浏览器自动化
- 减少了手动测试工作，提升了网页应用测试覆盖率
- 提供了企业环境中基于浏览器工具集成的可重用、可扩展框架
- 支持 GitHub Copilot 的网页浏览功能

**参考资料：**

- [Playwright MCP 服务器 GitHub 仓库](https://github.com/microsoft/playwright-mcp)
- [微软 AI 与自动化解决方案](https://azure.microsoft.com/en-us/products/ai-services/)

### 案例研究 5：Azure MCP – 企业级模型上下文协议即服务

Azure MCP 服务器 ([https://aka.ms/azmcp](https://aka.ms/azmcp)) 是微软的托管企业级模型上下文协议实现，旨在作为云服务提供可扩展、安全且合规的 MCP 服务器能力。Azure MCP 使组织能够快速部署、管理并集成 MCP 服务器与 Azure AI、数据和安全服务，降低运营负担，加速 AI 采纳。

> **🎯 生产就绪工具**
> 
> 这是一个您今天可以使用的真实 MCP 服务器！更多关于微软 Foundry MCP 服务器的信息，请参阅我们的[**微软 MCP 服务器指南**](microsoft-mcp-servers.md)。


- 完全托管的 MCP 服务器托管，内置弹性扩展、监控和安全
- 与 Azure OpenAI、Azure AI 搜索及其他 Azure 服务的原生集成
- 通过 Microsoft Entra ID 实现企业认证与授权
- 支持自定义工具、提示模板和资源连接器
- 符合企业安全与监管要求

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
- 通过提供即用型合规的 MCP 服务器平台，缩短企业 AI 项目的价值实现时间
- 简化了 LLM、工具及企业数据源的集成
- 增强了 MCP 工作负载的安全性、可观察性和运营效率
- 借助 Azure SDK 最佳实践和最新认证模式提升代码质量

**参考资料：**  
- [Azure MCP 文档](https://aka.ms/azmcp)
- [Azure MCP 服务器 GitHub 仓库](https://github.com/Azure/azure-mcp)
- [Azure AI 服务](https://azure.microsoft.com/en-us/products/ai-services/)
- [微软 MCP 中心](https://mcp.azure.com)

## 案例研究 6：NLWeb 
MCP（模型上下文协议）是一种新兴协议，用于聊天机器人和 AI 助手与工具交互。每个 NLWeb 实例同时也是 MCP 服务器，支持一个核心方法 ask，用于以自然语言向网站提问。返回的响应利用了 schema.org，这是一种广泛使用的描述网页数据的词汇。从广义上讲，MCP 之于 NLWeb，就如 HTTP 之于 HTML。NLWeb 结合了协议、Schema.org 格式及示例代码，帮助网站快速创建这些端点，既惠及通过对话界面的用户，也便于代理间的自然交互。

NLWeb 包含两个不同的组成部分。
- 一个协议，非常简单，旨在通过自然语言与站点交互，返回答案采用 json 和 schema.org 格式。详见 REST API 文档。
- 一个简单实现（第一点），利用现有标记，适用于可抽象为项目列表的网站（产品、食谱、景点、评论等）。结合一组用户界面小部件，网站能轻松为内容提供对话式接口。详见聊天查询流程文档了解详情。
 
**参考资料：**  
- [Azure MCP 文档](https://aka.ms/azmcp)
- [NLWeb](https://github.com/microsoft/NlWeb)

### 案例研究 7：微软 Foundry MCP 服务器 – 企业 AI 代理集成

微软 Foundry MCP 服务器演示了 MCP 如何用于企业环境中编排和管理 AI 代理与工作流。通过将 MCP 与微软 Foundry 整合，组织能标准化代理交互，利用 Foundry 的工作流管理，并保障部署的安全性与可扩展性。

> **🎯 生产就绪工具**
> 
> 这是您今天可以使用的真实 MCP 服务器！更多信息请参阅我们的[**微软 MCP 服务器指南**](microsoft-mcp-servers.md#9--microsoft-foundry-mcp-server)。

**关键特性：**
- 全面访问 Azure AI 生态系统，包括模型目录和部署管理
- 利用 Azure AI 搜索进行知识索引，支持 RAG 应用
- AI 模型性能及质量保障的评估工具
- 与微软 Foundry 目录和实验室集成，支持前沿研究模型
- 针对生产场景的代理管理与评估能力

**结果：**
- 快速原型设计和健壮的 AI 代理工作流监控
- 与 Azure AI 服务无缝集成，支持高级场景
- 用于构建、部署和监控代理流水线的统一接口
- 改善企业的安全、合规及运营效率
- 加速 AI 采纳，同时保持对复杂代理驱动流程的控制

**参考资料：**
- [微软 Foundry MCP 服务器 GitHub 仓库](https://github.com/azure-ai-foundry/mcp-foundry)
- [使用 MCP 集成 Azure AI 代理（微软 Foundry 博客）](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

### 案例研究 8：Foundry MCP Playground – 实验和原型设计

Foundry MCP Playground 提供了一个现成环境，用于 MCP 服务器和微软 Foundry 集成的实验。开发者可以快速原型设计、测试和评估 AI 模型及代理工作流，使用微软 Foundry 目录和实验室的资源。该 playground 简化了设置，提供示例项目，支持协作开发，使探索最佳实践和新场景变得轻松且低成本。它特别适合想验证理念、共享实验和加速学习的团队，无需复杂基础设施。通过降低门槛，该 playground 有助于推动 MCP 与微软 Foundry 生态的创新和社区贡献。

**参考资料：**

- [Foundry MCP Playground GitHub 仓库](https://github.com/azure-ai-foundry/foundry-mcp-playground)

### 案例研究 9：微软 Learn Docs MCP 服务器 – AI 驱动的文档访问

微软 Learn Docs MCP 服务器是一项云托管服务，通过模型上下文协议为 AI 助手提供对微软官方文档的实时访问。该生产就绪服务器连接到全面的微软 Learn 生态系统，实现对所有官方微软资源的语义搜索。

> **🎯 生产就绪工具**
> 
> 这是您今天可以使用的真实 MCP 服务器！更多信息请参阅我们的[**微软 MCP 服务器指南**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server)。

**核心特性：**
- 实时访问微软官方文档、Azure 文档和 Microsoft 365 文档
- 先进的语义搜索能力，理解上下文和意图
- 随微软 Learn 内容发布保持信息时刻更新
- 涵盖微软 Learn、Azure 文档和 Microsoft 365 资源的全面内容
- 返回最多 10 个优质内容块，包含文章标题和 URL

**重要性：**
- 解决微软技术中存在的“AI 知识过时”问题
- 确保 AI 助手掌握最新的 .NET、C#、Azure 和 Microsoft 365 功能
- 提供权威的一手信息，确保代码生成准确
- 对快速演进的微软技术开发者至关重要

**结果：**
- 大幅提升针对微软技术的 AI 生成代码准确性
- 减少寻找最新文档和最佳实践的时间
- 通过上下文感知的文档检索提升开发者生产力
- 与开发流程无缝集成，无需离开 IDE

**参考资料：**
- [微软 Learn Docs MCP 服务器 GitHub 仓库](https://github.com/MicrosoftDocs/mcp)
- [微软 Learn 文档](https://learn.microsoft.com/)

## 动手项目

### 项目 1：构建多提供商 MCP 服务器

**目标：** 创建一个 MCP 服务器，可以根据特定条件将请求路由到多个 AI 模型提供商。

**需求：**

- 支持至少三种不同的模型提供商（例如 OpenAI、Anthropic、本地模型）
- 实现基于请求元数据的路由机制
- 创建用于管理提供商凭据的配置系统
- 添加缓存以优化性能和成本
- 构建简单的仪表盘监控使用情况

**实施步骤：**

1. 搭建基础 MCP 服务器基础设施
2. 为每个 AI 模型服务实现提供商适配器
3. 创建基于请求属性的路由逻辑
4. 添加频繁请求的缓存机制
5. 开发监控仪表盘
6. 测试各种请求模式

**技术：** 可选用 Python（或根据偏好选择 .NET/Java/Python），Redis 用于缓存，以及简单的 Web 框架开发仪表盘。

### 项目 2：企业提示管理系统

**目标：** 开发一个基于 MCP 的系统，用于管理、版本控制和部署整个组织的提示模板。

**需求：**


- 创建一个集中式的提示模板库
- 实施版本控制和审批工作流
- 构建带有示例输入的模板测试能力
- 开发基于角色的访问控制
- 创建模板检索和部署的 API

**实施步骤：**

1. 设计模板存储的数据库架构
2. 创建模板的核心 CRUD 操作 API
3. 实施版本控制系统
4. 构建审批工作流
5. 研发测试框架
6. 创建简单的管理网页界面
7. 集成 MCP 服务器

**技术：** 您选择的后端框架、SQL 或 NoSQL 数据库，以及用于管理界面的前端框架。

### 项目 3：基于 MCP 的内容生成平台

**目标：** 构建一个利用 MCP 提供不同内容类型一致结果的内容生成平台。

**需求：**

- 支持多种内容格式（博客文章、社交媒体内容、营销文案）
- 实施基于模板的生成，并支持定制化选项
- 创建内容审核和反馈系统
- 跟踪内容表现指标
- 支持内容版本管理和迭代

**实施步骤：**

1. 搭建 MCP 客户端基础设施
2. 为不同内容类型创建模板
3. 构建内容生成流水线
4. 实施审核系统
5. 研发指标跟踪系统
6. 创建模板管理和内容生成的用户界面

**技术：** 您偏好的编程语言、网络框架和数据库系统。

## MCP 技术的未来方向

### 新兴趋势

1. **多模态 MCP**
   - 扩展 MCP，实现与图像、音频和视频模型的标准交互
   - 发展跨模态推理能力
   - 针对不同模态的标准化提示格式

2. **联邦 MCP 基础设施**
   - 可跨组织共享资源的分布式 MCP 网络
   - 用于安全模型共享的标准协议
   - 隐私保护计算技术

3. **MCP 市场**
   - 用于共享和货币化 MCP 模板及插件的生态系统
   - 质量保证和认证流程
   - 与模型市场的集成

4. **边缘计算的 MCP**
   - 适配资源受限的边缘设备的 MCP 标准
   - 针对低带宽环境的优化协议
   - 专用于物联网生态系统的 MCP 实现

5. <strong>监管框架</strong>
   - MCP 扩展以满足监管合规性的开发
   - 标准化审计轨迹与可解释性接口
   - 与新兴 AI 治理框架的集成

### 来自微软的 MCP 解决方案

微软和 Azure 开发了多个开源仓库，帮助开发者在各种场景下实现 MCP：

#### Microsoft 组织

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - 用于浏览器自动化和测试的 Playwright MCP 服务器
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - OneDrive MCP 服务器实现，用于本地测试和社区贡献
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWeb 是一组开放协议及相关开源工具，重点构建 AI Web 的基础层

#### Azure-Samples 组织

1. [mcp](https://github.com/Azure-Samples/mcp) - 多语言在 Azure 上构建与集成 MCP 服务器的示例、工具和资源链接
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - 参考 MCP 服务器，演示当前 Model Context Protocol 规范下的身份验证
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure 函数中远程 MCP 服务器实现的首页，含语言特定仓库链接
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Python 在 Azure 函数上构建和部署自定义远程 MCP 服务器的快速模板
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 .NET/C# 在 Azure 函数上构建和部署自定义远程 MCP 服务器的快速模板
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 TypeScript 在 Azure 函数上构建和部署自定义远程 MCP 服务器的快速模板
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - 使用 Python 的 Azure API 管理作为远程 MCP 服务器的 AI 网关
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI 实验包含 MCP 功能，集成 Azure OpenAI 和 AI Foundry

这些仓库提供了跨不同编程语言和 Azure 服务的 Model Context Protocol 各种实现、模板和资源。覆盖从基础服务器实现到身份验证、云端部署和企业集成等多种用例。

#### MCP 资源目录

官方微软 MCP 仓库中的 [MCP Resources 目录](https://github.com/microsoft/mcp/tree/main/Resources) 提供了精心整理的示例资源、提示模板和工具定义，供 Model Context Protocol 服务器使用。该目录旨在通过提供可复用的构建模块和最佳实践示例，帮助开发者快速启动 MCP：

- **提示模板：** 常见 AI 任务和场景的即用型提示模板，可根据自有 MCP 服务器实现进行调整。
- **工具定义：** 标准化工具集成与调用的示例工具架构和元数据，适用于不同 MCP 服务器。
- **资源示例：** 在 MCP 框架内连接数据源、API 和外部服务的示例资源定义。
- **参考实现：** 实际示范如何在真实 MCP 项目中构建和组织资源、提示和工具的样例。

这些资源可加快开发进度，促进标准化，并帮助确保构建和部署基于 MCP 的解决方案时采用最佳实践。

#### MCP 资源目录

- [MCP Resources（示例提示、工具和资源定义）](https://github.com/microsoft/mcp/tree/main/Resources)

### 研究机会

- MCP 框架内的高效提示优化技术
- 多租户 MCP 部署的安全模型
- 不同 MCP 实现的性能基准测试
- MCP 服务器的形式化验证方法

## 结论

Model Context Protocol（MCP）正在迅速塑造跨行业标准化、安全且互操作的 AI 集成未来。通过本课程中的案例研究和实操项目，您已经了解到早期采用者——包括微软和 Azure——如何利用 MCP 解决现实挑战，加速 AI 采用，并确保合规性、安全性和可扩展性。MCP 的模块化方式使组织能够在统一且可审计的框架中连接大型语言模型、工具和企业数据。随着 MCP 的不断演进，保持与社区的互动，探索开源资源，并应用最佳实践，将是构建强健且面向未来的 AI 解决方案的关键。

## 附加资源

- [MCP Foundry GitHub 仓库](https://github.com/azure-ai-foundry/mcp-foundry)
- [Foundry MCP 沙箱](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [将 Azure AI Agents 集成到 MCP（微软 Foundry 博客）](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
- [MCP GitHub 仓库（微软）](https://github.com/microsoft/mcp)
- [MCP 资源目录（示例提示、工具和资源定义）](https://github.com/microsoft/mcp/tree/main/Resources)
- [MCP 社区与文档](https://modelcontextprotocol.io/introduction)
- [MCP 规范（2026-07-28）](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Azure MCP 文档](https://aka.ms/azmcp)
- [OWASP MCP 十大](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - 安全最佳实践
- [Playwright MCP 服务器 GitHub 仓库](https://github.com/microsoft/playwright-mcp)
- [Files MCP 服务器（OneDrive）](https://github.com/microsoft/files-mcp-server)
- [Azure-Samples MCP](https://github.com/Azure-Samples/mcp)
- [MCP Auth Servers（Azure-Samples）](https://github.com/Azure-Samples/mcp-auth-servers)
- [Remote MCP Functions（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-functions)
- [Remote MCP Functions Python（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway（Azure-Samples）](https://github.com/Azure-Samples/AI-Gateway)
- [微软 AI 与自动化解决方案](https://azure.microsoft.com/en-us/products/ai-services/)

## 练习

1. 分析一个案例研究，并提出另一种实现方案。
2. 选择一个项目创意，制定详细的技术规格说明。
3. 研究一个案例中未涉及的行业，概述 MCP 如何应对其特定挑战。
4. 探索一个未来方向，为其设计一个新的 MCP 扩展概念。

## 后续内容

继续探索：[Microsoft MCP 服务器](./microsoft-mcp-servers.md)

继续学习：[第8模块：最佳实践](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->