# 🌟 從早期採用者學到的課程

[![從 MCP 早期採用者學到的課程](../../../translated_images/zh-HK/08.980bb2babbaadd8a97739effc9b31e5f1abd8f4c4a3fbc90fb9f931a866674d0.png)](https://youtu.be/jds7dSmNptE)

_（點擊上方圖片觀看本課程的影片）_

## 🎯 本模組涵蓋的內容

本模組探討了真實的組織和開發者如何利用 Model Context Protocol (MCP) 解決實際挑戰並推動創新。透過詳細的案例研究和實作項目，您將了解 MCP 如何實現安全、可擴展的 AI 整合，連接語言模型、工具和企業數據。

### 📚 MCP 的實際應用

想了解這些原則如何應用於生產工具？請查看我們的[**10 個正在改變開發者生產力的 Microsoft MCP 伺服器**](microsoft-mcp-servers.md)，其中展示了您今天就可以使用的真實 Microsoft MCP 伺服器。

## 概述

本課程探討了早期採用者如何利用 Model Context Protocol (MCP) 解決實際問題並推動各行業的創新。透過詳細的案例研究和實作項目，您將了解 MCP 如何實現標準化、安全且可擴展的 AI 整合，將大型語言模型、工具和企業數據連接到統一框架中。您將獲得設計和構建基於 MCP 解決方案的實際經驗，學習已驗證的實施模式，並探索在生產環境中部署 MCP 的最佳實踐。本課程還強調了新興趨勢、未來方向以及開源資源，幫助您保持 MCP 技術及其不斷演變的生態系統的前沿。

## 學習目標

- 分析不同行業的真實 MCP 實施案例
- 設計並構建完整的基於 MCP 的應用程序
- 探索 MCP 技術的新興趨勢和未來方向
- 在實際開發場景中應用最佳實踐

## 真實 MCP 實施案例

### 案例研究 1：企業客戶支持自動化

一家跨國公司實施了基於 MCP 的解決方案，以標準化其客戶支持系統中的 AI 交互。這使他們能夠：

- 為多個 LLM 提供商創建統一界面
- 在各部門間保持一致的提示管理
- 實施強大的安全性和合規控制
- 根據具體需求輕鬆切換不同的 AI 模型

**技術實施：**

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

**結果：** 模型成本降低 30%，響應一致性提高 45%，並增強了全球運營的合規性。

### 案例研究 2：醫療診斷助手

一家醫療機構開發了 MCP 基礎架構，以整合多個專業醫療 AI 模型，同時確保敏感患者數據的保護：

- 在通用醫療模型和專業醫療模型之間無縫切換
- 嚴格的隱私控制和審計記錄
- 與現有電子病歷 (EHR) 系統集成
- 對醫學術語進行一致的提示工程

**技術實施：**

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

**結果：** 為醫生提供改進的診斷建議，同時保持完全符合 HIPAA 規範，並顯著減少系統間的上下文切換。

### 案例研究 3：金融服務風險分析

一家金融機構實施了 MCP，以標準化其不同部門的風險分析流程：

- 為信用風險、欺詐檢測和投資風險模型創建統一界面
- 實施嚴格的訪問控制和模型版本管理
- 確保所有 AI 建議的可審計性
- 在多樣化系統間保持一致的數據格式

**技術實施：**

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

**結果：** 增強了監管合規性，模型部署周期加快 40%，並提高了部門間風險評估的一致性。

### 案例研究 4：Microsoft Playwright MCP 伺服器用於瀏覽器自動化

Microsoft 開發了 [Playwright MCP 伺服器](https://github.com/microsoft/playwright-mcp)，以通過 Model Context Protocol 實現安全、標準化的瀏覽器自動化。這個生產就緒的伺服器允許 AI 代理和 LLM 以受控、可審計且可擴展的方式與網頁瀏覽器交互，支持自動化網頁測試、數據提取和端到端工作流程等用例。

> **🎯 生產就緒工具**
> 
> 此案例研究展示了一個您今天就可以使用的真實 MCP 伺服器！了解更多關於 Playwright MCP 伺服器及其他 9 個生產就緒的 Microsoft MCP 伺服器的信息，請參閱我們的[**Microsoft MCP 伺服器指南**](microsoft-mcp-servers.md#8--playwright-mcp-server)。

**主要功能：**
- 將瀏覽器自動化功能（導航、表單填寫、截圖捕捉等）作為 MCP 工具公開
- 實施嚴格的訪問控制和沙盒機制以防止未授權行為
- 提供所有瀏覽器交互的詳細審計記錄
- 支持與 Azure OpenAI 和其他 LLM 提供商集成，用於代理驅動的自動化
- 為 GitHub Copilot 的 Coding Agent 提供網頁瀏覽功能

**技術實施：**

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

**結果：**

- 為 AI 代理和 LLM 實現安全的程式化瀏覽器自動化
- 減少手動測試工作量並提高網頁應用的測試覆蓋率
- 提供可重用、可擴展的框架，用於企業環境中的基於瀏覽器的工具集成
- 為 GitHub Copilot 的網頁瀏覽功能提供支持

**參考資料：**

- [Playwright MCP 伺服器 GitHub 存儲庫](https://github.com/microsoft/playwright-mcp)
- [Microsoft AI 和自動化解決方案](https://azure.microsoft.com/en-us/products/ai-services/)

### 案例研究 5：Azure MCP – 企業級 Model Context Protocol 即服務

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) 是 Microsoft 的企業級 Model Context Protocol 托管實現，旨在提供可擴展、安全且符合規範的 MCP 伺服器能力作為雲服務。Azure MCP 使組織能夠快速部署、管理和整合 MCP 伺服器與 Azure AI、數據和安全服務，減少運營負擔並加速 AI 的採用。

> **🎯 生產就緒工具**
> 
> 這是一個您今天就可以使用的真實 MCP 伺服器！了解更多關於 Azure AI Foundry MCP 伺服器的信息，請參閱我們的[**Microsoft MCP 伺服器指南**](microsoft-mcp-servers.md)。

- 完全托管的 MCP 伺服器托管，內置擴展、監控和安全功能
- 與 Azure OpenAI、Azure AI Search 和其他 Azure 服務的原生集成
- 通過 Microsoft Entra ID 實現企業身份驗證和授權
- 支持自定義工具、提示模板和資源連接器
- 符合企業安全和監管要求

**技術實施：**

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

**結果：**  
- 通過提供即用型、符合規範的 MCP 伺服器平台，縮短企業 AI 項目的價值實現時間
- 簡化 LLM、工具和企業數據源的整合
- 增強 MCP 工作負載的安全性、可觀察性和運營效率
- 使用 Azure SDK 的最佳實踐和當前身份驗證模式提高代碼質量

**參考資料：**  
- [Azure MCP 文檔](https://aka.ms/azmcp)
- [Azure MCP 伺服器 GitHub 存儲庫](https://github.com/Azure/azure-mcp)
- [Azure AI 服務](https://azure.microsoft.com/en-us/products/ai-services/)
- [Microsoft MCP 中心](https://mcp.azure.com)

### 案例研究 6：NLWeb

MCP (Model Context Protocol) 是一種新興協議，用於聊天機器人和 AI 助手與工具交互。每個 NLWeb 實例也是一個 MCP 伺服器，支持一個核心方法——ask，用於以自然語言向網站提問。返回的響應利用了 schema.org，一種廣泛使用的網頁數據描述詞彙。簡而言之，MCP 對 NLWeb 的作用就像 Http 對 HTML 的作用。NLWeb 結合協議、Schema.org 格式和示例代碼，幫助網站快速創建這些端點，既能造福人類，通過對話界面，也能造福機器，通過自然的代理對代理交互。

NLWeb 有兩個明顯的組成部分：
- 一個非常簡單的協議，用於以自然語言與網站交互，以及一種格式，利用 json 和 schema.org 返回答案。請參閱 REST API 文檔以了解更多細節。
- 一個簡單的實現，利用現有標記，適用於可以抽象為項目列表（產品、食譜、景點、評論等）的網站。結合一組用戶界面小部件，網站可以輕鬆為其內容提供對話界面。請參閱聊天查詢的生命周期文檔以了解更多細節。

**參考資料：**  
- [Azure MCP 文檔](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

### 案例研究 7：Azure AI Foundry MCP 伺服器 – 企業 AI 代理整合

Azure AI Foundry MCP 伺服器展示了 MCP 如何用於在企業環境中協調和管理 AI 代理及工作流程。通過將 MCP 與 Azure AI Foundry 整合，組織可以標準化代理交互，利用 Foundry 的工作流程管理，並確保安全、可擴展的部署。

> **🎯 生產就緒工具**
> 
> 這是一個您今天就可以使用的真實 MCP 伺服器！了解更多關於 Azure AI Foundry MCP 伺服器的信息，請參閱我們的[**Microsoft MCP 伺服器指南**](microsoft-mcp-servers.md#9--azure-ai-foundry-mcp-server)。

**主要功能：**
- 全面訪問 Azure 的 AI 生態系統，包括模型目錄和部署管理
- 使用 Azure AI Search 進行 RAG 應用的知識索引
- 用於 AI 模型性能和質量保證的評估工具
- 與 Azure AI Foundry Catalog 和 Labs 集成，用於尖端研究模型
- 用於生產場景的代理管理和評估能力

**結果：**
- 快速原型設計和 AI 代理工作流程的強大監控
- 與 Azure AI 服務無縫集成，用於高級場景
- 用於構建、部署和監控代理管道的統一界面
- 提高企業的安全性、合規性和運營效率
- 加速 AI 採用，同時保持對複雜代理驅動流程的控制

**參考資料：**
- [Azure AI Foundry MCP 伺服器 GitHub 存儲庫](https://github.com/azure-ai-foundry/mcp-foundry)
- [整合 Azure AI 代理與 MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

### 案例研究 8：Foundry MCP Playground – 實驗與原型設計

Foundry MCP Playground 提供了一個即用型環境，用於實驗 MCP 伺服器和 Azure AI Foundry 整合。開發者可以快速原型設計、測試和評估 AI 模型及代理工作流程，使用來自 Azure AI Foundry Catalog 和 Labs 的資源。Playground 簡化了設置，提供示例項目，並支持協作開發，使探索最佳實踐和新場景變得簡單，且幾乎不需要額外的基礎設施。對於希望驗證想法、分享實驗並加速學習的團隊來說，Playground 特別有用。通過降低進入門檻，Playground 有助於促進 MCP 和 Azure AI Foundry 生態系統中的創新和社區貢獻。

**參考資料：**

- [Foundry MCP Playground GitHub 存儲庫](https://github.com/azure-ai-foundry/foundry-mcp-playground)

### 案例研究 9：Microsoft Learn Docs MCP 伺服器 – AI 驅動的文檔訪問

Microsoft Learn Docs MCP 伺服器是一個雲托管服務，通過 Model Context Protocol 為 AI 助手提供實時訪問官方 Microsoft 文檔的能力。這個生產就緒的伺服器連接到全面的 Microsoft Learn 生態系統，並支持跨所有官方 Microsoft 資源的語義搜索。
> **🎯 適用於生產環境的工具**  
>  
> 這是一個你今天就可以使用的真正 MCP 伺服器！想了解更多有關 Microsoft Learn Docs MCP 伺服器的資訊，請參閱我們的[**Microsoft MCP 伺服器指南**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server)。
**主要功能：**
- 即時存取官方 Microsoft 文件、Azure 文件及 Microsoft 365 文件
- 具備理解上下文及意圖的高級語義搜索功能
- 隨 Microsoft Learn 內容發布而保持最新資訊
- 涵蓋 Microsoft Learn、Azure 文件及 Microsoft 365 資源的全面內容
- 返回最多 10 個高質量內容片段，附文章標題及 URL

**為何至關重要：**
- 解決 Microsoft 技術的「過時 AI 知識」問題
- 確保 AI 助手能獲取最新的 .NET、C#、Azure 和 Microsoft 365 功能
- 提供權威的一手資訊以生成準確的代碼
- 對於使用快速演進的 Microsoft 技術的開發者至關重要

**結果：**
- 顯著提升 AI 生成 Microsoft 技術代碼的準確性
- 減少搜尋最新文件及最佳實踐的時間
- 通過上下文感知的文件檢索提升開發者生產力
- 無需離開 IDE 即可無縫整合至開發工作流

**參考資料：**
- [Microsoft Learn Docs MCP Server GitHub Repository](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn Documentation](https://learn.microsoft.com/)

## 實踐項目

### 項目 1：構建多供應商 MCP 伺服器

**目標：** 創建一個 MCP 伺服器，根據特定條件將請求路由至多個 AI 模型供應商。

**需求：**

- 支援至少三個不同的模型供應商（例如 OpenAI、Anthropic、本地模型）
- 實現基於請求元數據的路由機制
- 創建管理供應商憑據的配置系統
- 添加緩存以優化性能和成本
- 構建一個簡單的儀表板以監控使用情況

**實現步驟：**

1. 設置基本的 MCP 伺服器基礎架構
2. 為每個 AI 模型服務實現供應商適配器
3. 創建基於請求屬性的路由邏輯
4. 添加針對頻繁請求的緩存機制
5. 開發監控儀表板
6. 使用各種請求模式進行測試

**技術選擇：** 可選 Python（或 .NET/Java/Python），Redis 作為緩存，及一個簡單的 Web 框架用於儀表板。

### 項目 2：企業級提示管理系統

**目標：** 開發基於 MCP 的系統，用於管理、版本控制及部署組織內的提示模板。

**需求：**

- 創建提示模板的集中式存儲庫
- 實現版本控制及審批工作流
- 構建帶有示例輸入的模板測試功能
- 開發基於角色的訪問控制
- 創建用於模板檢索及部署的 API

**實現步驟：**

1. 設計模板存儲的數據庫架構
2. 創建模板 CRUD 操作的核心 API
3. 實現版本控制系統
4. 構建審批工作流
5. 開發測試框架
6. 創建簡單的 Web 界面進行管理
7. 與 MCP 伺服器集成

**技術選擇：** 自選後端框架、SQL 或 NoSQL 數據庫，以及用於管理界面的前端框架。

### 項目 3：基於 MCP 的內容生成平台

**目標：** 構建一個內容生成平台，利用 MCP 提供不同內容類型的一致結果。

**需求：**

- 支援多種內容格式（博客文章、社交媒體、營銷文案）
- 實現基於模板的生成，並提供自定義選項
- 創建內容審核及反饋系統
- 跟蹤內容性能指標
- 支援內容版本控制及迭代

**實現步驟：**

1. 設置 MCP 客戶端基礎架構
2. 為不同內容類型創建模板
3. 構建內容生成流水線
4. 實現審核系統
5. 開發性能指標跟蹤系統
6. 創建用於模板管理及內容生成的用戶界面

**技術選擇：** 自選編程語言、Web 框架及數據庫系統。

## MCP 技術的未來方向

### 新興趨勢

1. **多模態 MCP**
   - 擴展 MCP 標準以支持圖像、音頻及視頻模型的交互
   - 開發跨模態推理能力
   - 為不同模態標準化提示格式

2. **聯邦 MCP 基礎架構**
   - 分佈式 MCP 網絡，可在組織間共享資源
   - 用於安全模型共享的標準化協議
   - 保護隱私的計算技術

3. **MCP 市場**
   - 用於共享及貨幣化 MCP 模板及插件的生態系統
   - 質量保證及認證流程
   - 與模型市場的集成

4. **針對邊緣計算的 MCP**
   - 為資源受限的邊緣設備適配 MCP 標準
   - 用於低帶寬環境的優化協議
   - 專為物聯網生態系統設計的 MCP 實現

5. **監管框架**
   - 開發支持監管合規的 MCP 擴展
   - 標準化審計記錄及可解釋性接口
   - 與新興 AI 治理框架的集成

### Microsoft 的 MCP 解決方案

Microsoft 和 Azure 已開發多個開源存儲庫，幫助開發者在各種場景中實現 MCP：

#### Microsoft 組織

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - 用於瀏覽器自動化及測試的 Playwright MCP 伺服器
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - 用於本地測試及社區貢獻的 OneDrive MCP 伺服器實現
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWeb 是一組開放協議及相關開源工具，主要專注於為 AI Web 建立基礎層

#### Azure-Samples 組織

1. [mcp](https://github.com/Azure-Samples/mcp) - 提供用多種語言構建及集成 MCP 伺服器的示例、工具及資源
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - 展示當前 Model Context Protocol 規範認證的參考 MCP 伺服器
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - 使用 Azure Functions 實現遠程 MCP 伺服器的登錄頁面，附語言特定的存儲庫鏈接
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Azure Functions 和 Python 構建及部署自定義遠程 MCP 伺服器的快速入門模板
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 Azure Functions 和 .NET/C# 構建及部署自定義遠程 MCP 伺服器的快速入門模板
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Azure Functions 和 TypeScript 構建及部署自定義遠程 MCP 伺服器的快速入門模板
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - 使用 Python 的 Azure API Management 作為遠程 MCP 伺服器的 AI 閘道
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - 包括 MCP 功能的 APIM ❤️ AI 實驗，集成 Azure OpenAI 和 AI Foundry

這些存儲庫提供了針對不同編程語言及 Azure 服務的 Model Context Protocol 的多種實現、模板及資源，涵蓋從基本伺服器實現到認證、雲部署及企業集成場景的廣泛用例。

#### MCP 資源目錄

官方 Microsoft MCP 存儲庫中的 [MCP 資源目錄](https://github.com/microsoft/mcp/tree/main/Resources) 提供了一個精選的示例資源集合、提示模板及工具定義，用於 Model Context Protocol 伺服器。該目錄旨在通過提供可重用的構建模塊及最佳實踐示例，幫助開發者快速入門 MCP：

- **提示模板：** 用於常見 AI 任務及場景的即用型提示模板，可根據需要適配至您的 MCP 伺服器實現。
- **工具定義：** 標準化工具集成及調用的示例工具架構及元數據。
- **資源示例：** MCP 框架內連接數據源、API 及外部服務的示例資源定義。
- **參考實現：** 展示如何在實際 MCP 項目中結構化及組織資源、提示及工具的實用示例。

這些資源加速開發、促進標準化，並幫助確保在構建及部署基於 MCP 的解決方案時採用最佳實踐。

#### MCP 資源目錄

- [MCP 資源（示例提示、工具及資源定義）](https://github.com/microsoft/mcp/tree/main/Resources)

### 研究機會

- MCP 框架內高效提示優化技術
- 多租戶 MCP 部署的安全模型
- 不同 MCP 實現的性能基準測試
- MCP 伺服器的形式化驗證方法

## 結論

Model Context Protocol (MCP) 正迅速塑造跨行業標準化、安全及可互操作的 AI 集成的未來。通過本課程中的案例研究及實踐項目，您已了解早期採用者（包括 Microsoft 和 Azure）如何利用 MCP 解決實際挑戰、加速 AI 採用並確保合規性、安全性及可擴展性。MCP 的模塊化方法使組織能夠在統一、可審計的框架內連接大型語言模型、工具及企業數據。隨著 MCP 的不斷發展，積極參與社區、探索開源資源及應用最佳實踐將是構建穩健、面向未來的 AI 解決方案的關鍵。

## 附加資源

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

## 練習

1. 分析其中一個案例研究，並提出替代的實現方法。
2. 選擇一個項目想法，並創建詳細的技術規範。
3. 研究案例研究中未涵蓋的一個行業，並概述 MCP 如何解決其特定挑戰。
4. 探索未來方向之一，並構思一個支持該方向的新 MCP 擴展。

下一步：[Microsoft MCP Server](../07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。