<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T17:56:29+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "hk"
}
-->
# 早期採用者的經驗分享

## 概覽

本課程探討早期採用者如何利用 Model Context Protocol (MCP) 解決實際問題，並推動各行業的創新。透過詳盡的案例研究及實作專案，你將了解 MCP 如何實現標準化、安全及可擴展的 AI 整合，將大型語言模型、工具與企業數據統一連接在同一框架內。你將獲得設計與構建基於 MCP 解決方案的實務經驗，學習成熟的實作模式，並掌握在生產環境部署 MCP 的最佳做法。本課程亦會介紹新興趨勢、未來發展方向及開源資源，助你保持在 MCP 技術及其生態系的前沿。

## 學習目標

- 分析不同行業中 MCP 的實際應用案例
- 設計並建置完整的 MCP 應用程式
- 探索 MCP 技術的新興趨勢與未來方向
- 在實際開發情境中應用最佳實踐

## MCP 實際應用案例

### 案例研究 1：企業客戶支援自動化

一家跨國企業導入基於 MCP 的解決方案，標準化其客戶支援系統中的 AI 互動。此方案使他們能：

- 為多個 LLM 供應商建立統一介面
- 跨部門維持一致的提示管理
- 實施強健的安全與合規控管
- 根據需求輕鬆切換不同 AI 模型

**技術實作：**  
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

**成果：** 模型成本降低 30%，回應一致性提升 45%，並加強全球營運的合規性。

### 案例研究 2：醫療診斷助理

一家醫療機構建立 MCP 基礎架構，整合多個專業醫療 AI 模型，同時確保敏感的病患資料安全：

- 在通用與專科醫療模型間無縫切換
- 嚴格的隱私控管與審計紀錄
- 與現有電子健康紀錄（EHR）系統整合
- 醫療術語提示工程保持一致性

**技術實作：**  
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

**成果：** 提升醫師診斷建議品質，完全符合 HIPAA 規範，並顯著減少系統間切換的負擔。

### 案例研究 3：金融服務風險分析

一家金融機構採用 MCP 標準化不同部門的風險分析流程：

- 建立信用風險、詐欺偵測及投資風險模型的統一介面
- 實施嚴格的存取控管及模型版本管理
- 確保所有 AI 建議可審計
- 維持跨系統資料格式一致性

**技術實作：**  
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

**成果：** 強化法規遵循，模型部署週期加快 40%，風險評估一致性提升。

### 案例研究 4：Microsoft Playwright MCP 伺服器用於瀏覽器自動化

Microsoft 開發了 [Playwright MCP server](https://github.com/microsoft/playwright-mcp)，透過 Model Context Protocol 實現安全且標準化的瀏覽器自動化。此方案讓 AI 代理與 LLM 能在受控、可審計且可擴充的環境下與瀏覽器互動，支援自動化網頁測試、資料擷取及端到端工作流程。

- 將瀏覽器自動化功能（導航、表單填寫、截圖等）作為 MCP 工具公開
- 實施嚴格的存取控管與沙盒機制，防止未授權操作
- 提供詳細的瀏覽器互動審計日誌
- 支援與 Azure OpenAI 及其他 LLM 供應商整合，實現代理驅動的自動化

**技術實作：**  
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

**成果：**  
- 為 AI 代理及 LLM 啟用安全的程式化瀏覽器自動化  
- 降低手動測試工作量，提升網頁應用測試覆蓋率  
- 提供可重用且可擴充的瀏覽器工具整合框架，適用於企業環境  

**參考資料：**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### 案例研究 5：Azure MCP – 企業級 Model Context Protocol 即服務

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) 是 Microsoft 提供的託管型企業級 MCP 實作，設計用於作為雲端服務提供可擴展、安全且合規的 MCP 伺服器能力。Azure MCP 幫助組織快速部署、管理並整合 MCP 伺服器與 Azure AI、資料及安全服務，降低營運負擔，加速 AI 採用。

- 完全託管的 MCP 伺服器主機，內建擴展性、監控與安全功能
- 原生整合 Azure OpenAI、Azure AI Search 及其他 Azure 服務
- 透過 Microsoft Entra ID 實現企業級身份驗證與授權
- 支援自訂工具、提示模板及資源連接器
- 符合企業安全及法規要求

**技術實作：**  
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

**成果：**  
- 為企業 AI 專案提供即用型、合規的 MCP 伺服器平台，縮短價值實現時間  
- 簡化 LLM、工具及企業資料源整合  
- 強化 MCP 工作負載的安全性、可觀察性與營運效率  

**參考資料：**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## 案例研究 6：NLWeb

MCP (Model Context Protocol) 是一種新興協議，讓聊天機器人和 AI 助理能與工具互動。每個 NLWeb 實例同時也是 MCP 伺服器，支援一個核心方法 ask，用於以自然語言向網站提問。回傳的回應採用 schema.org，一個廣泛使用的網頁資料描述詞彙。簡單來說，MCP 對 NLWeb 的關係，就像 Http 對 HTML。NLWeb 結合協議、Schema.org 格式及範例程式碼，協助網站快速建立這些端點，既方便人類透過對話介面使用，也利於機器間自然代理互動。

NLWeb 有兩個主要組成部分：  
- 一個簡單的協議，用於自然語言介面與網站互動，回傳格式採用 json 與 schema.org。詳細內容請參考 REST API 文件。  
- 一個簡易實作，利用現有標記，適用於可抽象為項目清單（產品、食譜、景點、評論等）的網站。配合一組用戶介面元件，網站能輕鬆提供對話式內容介面。詳見 Life of a chat query 文件說明運作方式。  

**參考資料：**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## 實作專案

### 專案 1：建置多供應商 MCP 伺服器

**目標：** 建立一個 MCP 伺服器，能根據特定條件將請求路由至多個 AI 模型供應商。

**需求：**  
- 支援至少三個不同模型供應商（如 OpenAI、Anthropic、本地模型）  
- 實作基於請求元資料的路由機制  
- 建立管理供應商憑證的設定系統  
- 加入快取以優化效能與成本  
- 建置簡易儀表板監控使用情況

**實作步驟：**  
1. 建置基本 MCP 伺服器架構  
2. 為每個 AI 模型服務實作供應商適配器  
3. 根據請求屬性實作路由邏輯  
4. 加入快取機制處理頻繁請求  
5. 開發監控儀表板  
6. 以多種請求模式進行測試

**技術選擇：** 可選 Python（或 .NET/Java/Python 任一你偏好的語言）、Redis 作為快取、簡易網頁框架用於儀表板。

### 專案 2：企業提示管理系統

**目標：** 開發基於 MCP 的系統，管理、版本控管及部署企業內的提示模板。

**需求：**  
- 建立集中式提示模板儲存庫  
- 實作版本控管及審核流程  
- 建置模板測試功能，含範例輸入  
- 發展角色基礎存取控制  
- 提供模板檢索與部署 API

**實作步驟：**  
1. 設計模板存儲資料庫結構  
2. 建立模板 CRUD 核心 API  
3. 實作版本控管系統  
4. 建置審核流程  
5. 開發測試框架  
6. 製作簡易管理網頁介面  
7. 與 MCP 伺服器整合

**技術選擇：** 自行選擇後端框架、SQL 或 NoSQL 資料庫，及管理介面前端框架。

### 專案 3：基於 MCP 的內容生成平台

**目標：** 建立一個內容生成平台，利用 MCP 提供跨不同內容類型的一致產出。

**需求：**  
- 支援多種內容格式（部落格文章、社群媒體、行銷文案）  
- 實作模板生成並提供自訂選項  
- 建立內容審核與回饋系統  
- 追蹤內容效能指標  
- 支援內容版本控管與迭代

**實作步驟：**  
1. 建置 MCP 用戶端架構  
2. 建立不同內容類型模板  
3. 建構內容生成流程  
4. 實作審核系統  
5. 發展指標追蹤系統  
6. 製作模板管理與內容生成的使用者介面

**技術選擇：** 依喜好選擇程式語言、網頁框架及資料庫系統。

## MCP 技術未來發展方向

### 新興趨勢

1. **多模態 MCP**  
   - 擴展 MCP 以標準化影像、音訊及影片模型的互動  
   - 發展跨模態推理能力  
   - 為不同模態制定標準化提示格式

2. **聯邦 MCP 基礎架構**  
   - 建立可跨組織共享資源的分散式 MCP 網路  
   - 標準化安全模型共享協議  
   - 採用隱私保護的運算技術

3. **MCP 市場平台**  
   - 打造 MCP 模板及插件的分享與營利生態系  
   - 品質保證與認證流程  
   - 與模型市場整合

4. **用於邊緣運算的 MCP**  
   - 調整 MCP 標準以適應資源有限的邊緣裝置  
   - 優化低頻寬環境的協議  
   - 專門為物聯網生態系設計的 MCP 實作

5. **法規架構**  
   - 發展 MCP 擴充以符合法規要求  
   - 標準化審計紀錄與可解釋性介面  
   - 與新興 AI 治理框架整合

### Microsoft 的 MCP 解決方案

Microsoft 與 Azure 開發了多個開源資源，協助開發者在不同場景實作 MCP：

#### Microsoft 組織  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - 用於瀏覽器自動化與測試的 Playwright MCP 伺服器  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - OneDrive MCP 伺服器實作，供本地測試及社群貢獻  
3. [NLWeb](https://github.com/microsoft/NlWeb) - 一組開放協議與開源工具，主力建立 AI 網路的基礎層

#### Azure-Samples 組織  
1. [mcp](https://github.com/Azure-Samples/mcp) - 提供多語言 MCP 伺服器建置與整合的範例、工具及資源  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - 示範符合當前 MCP 規範的認證伺服器  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure Functions 上遠端 MCP 伺服器實作的入口頁及語言專屬資源連結  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Python 建置及部署自訂遠端 MCP 伺服器的快速入門範本  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 .NET/C# 建置及部署自訂遠端 MCP 伺服器的快速入門範本  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 TypeScript 建置及部署自訂遠端 MCP 伺服器的快速入門範本  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - 使用 Python 透過 Azure API 管理作為遠端 MCP 伺服器的 AI 閘道  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM 與 AI 實驗，包括 MCP 功能，整合 Azure OpenAI 及 AI Foundry

這些資源涵蓋從基本伺服器實作到認證、雲端部署及企業整合的多種 MCP 應用場景，支援多種程式語言與 Azure 服務。

#### MCP 資源目錄

官方 Microsoft MCP 倉庫中的 [MCP Resources directory](https://github.com/microsoft/mcp/tree/main/Resources) 提供精選的範例資源、提示模板及工具定義，協助開發者快速上手 MCP，包含：

- **提示模板：** 可直接使用並調整的常見 AI 任務提示模板  
- **工具定義：** 範例工具結構與元資料，標準化工具整合與呼叫  
- **資源範例：** 連接資料來源、API 及外部服務的範例資源定義  
- **參考實作：** 展示如何在實際 MCP 專案中組織資源、提示與工具的實務範例

這些資源加速開發、促進標準化，並幫助確保 MCP 解決方案的最佳實踐。

#### MCP 資源目錄連結  
- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)

### 研究機會

- MCP 框架中的高效提示優化技術  
- 多租戶 MCP 部署的安全模型  
- 不同 MCP 實作的效能基準測試  
- MCP 伺服器的形式化驗證方法

## 結語

Model Context Protocol (MCP) 正快速塑造標準化、安全且可互操作的 AI 整合未來。透過本課程的案例研究與實作專案，你已了解早期採用者（包括 Microsoft 與 Azure）如何利用 MCP 解決實際挑戰，加速 AI 採用，並確保合規、安全與可擴展性。MCP 的模組化架構讓組織能在統一且可審計的框架中連接大型語言模型、工具及企業資料。隨著 MCP 持續演進，積極參與社群、探索開源資源及應用最佳實踐，將是打造強韌且面向未來的 AI 解決方案的關鍵。

## 額外資源

- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)  
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)  
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Playwright MCP Server GitHub Repository](
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## 練習

1. 分析其中一個案例研究，並提出另一種實現方法。
2. 選擇一個專案構想，並撰寫詳細的技術規格。
3. 研究一個案例研究未涵蓋的行業，並概述 MCP 如何解決該行業的特定挑戰。
4. 探討其中一個未來發展方向，並構思一個新的 MCP 擴充功能來支持它。

下一章節: [Best Practices](../08-BestPractices/README.md)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資料，建議使用專業人工翻譯。我們不對因使用本翻譯而引致的任何誤解或誤釋負責。