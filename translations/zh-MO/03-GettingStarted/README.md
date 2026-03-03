## 開始使用  

[![建立您的第一個 MCP 伺服器](../../../translated_images/zh-MO/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(按上方圖片觀看本課程影片)_

本章包括多個課程：

- **1 您的第一個伺服器**，在第一課中，您將學習如何建立您的第一個伺服器，並使用檢查器工具檢視它，這是測試和除錯伺服器的重要方式，[前往課程](01-first-server/README.md)

- **2 用戶端**，本課您將學習如何撰寫能連接到伺服器的用戶端，[前往課程](02-client/README.md)

- **3 帶有 LLM 的用戶端**，更好的用戶端作法是加入 LLM，使其能與您的伺服器「協商」接下來要 做什麼，[前往課程](03-llm-client/README.md)

- **4 在 Visual Studio Code 消費伺服器的 GitHub Copilot Agent 模式**。此處我們將探討如何從 Visual Studio Code 執行 MCP 伺服器，[前往課程](04-vscode/README.md)

- **5 stdio 傳輸伺服器**，stdio 傳輸是本地 MCP 伺服器與用戶端通訊的推薦標準，提供安全的子程序通訊並具備內建的流程隔離，[前往課程](05-stdio-server/README.md)

- **6 MCP 的 HTTP 串流（可串流的 HTTP）**。學習現代 HTTP 串流傳輸（依據 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http) 推薦遠端 MCP 伺服器的做法），進度通知，以及如何使用可串流 HTTP 實作可擴展的即時 MCP 伺服器與用戶端。[前往課程](06-http-streaming/README.md)

- **7 利用 VSCode 的 AI 工具包** 來消費和測試您的 MCP 用戶端與伺服器，[前往課程](07-aitk/README.md)

- **8 測試**。本章特別聚焦各種方法測試您的伺服器與用戶端，[前往課程](08-testing/README.md)

- **9 部署**。本章將探討不同方式部署您的 MCP 解決方案，[前往課程](09-deployment/README.md)

- **10 進階伺服器使用**。本章涵蓋進階的伺服器使用，[前往課程](./10-advanced/README.md)

- **11 認證**。本章涵蓋如何新增簡易認證，從基本認證到使用 JWT 和 RBAC。建議您先從本章開始，再參考第 5 章的進階主題，和第 2 章中推薦的安全強化措施，[前往課程](./11-simple-auth/README.md)

- **12 MCP Hosts**。設定與使用熱門 MCP 主控端用戶端，包括 Claude Desktop、Cursor、Cline 和 Windsurf。學習傳輸類型和疑難排解，[前往課程](./12-mcp-hosts/README.md)

- **13 MCP 檢查器**。使用 MCP 檢查器工具互動式除錯和測試您的 MCP 伺服器。學習故障排除工具、資源與協議訊息，[前往課程](./13-mcp-inspector/README.md)

- **14 抽樣**。建立 MCP 伺服器協同 MCP 用戶端執行與 LLM 相關的任務。[前往課程](./14-sampling/README.md)

- **15 MCP 應用程式**。建立同時回應 UI 指令的 MCP 伺服器，[前往課程](./15-mcp-apps/README.md)

Model Context Protocol (MCP) 是一個開放協議，標準化應用程式如何向 LLM 提供上下文。可想像 MCP 是 AI 應用的一個 USB-C 連接埠——它提供標準化方式讓 AI 模型連接不同資料來源和工具。

## 學習目標

完成本課程後，您將能夠：

- 為 C#、Java、Python、TypeScript 和 JavaScript 設定 MCP 的開發環境
- 建立和部署具自訂功能的基本 MCP 伺服器（包括資源、提示和工具）
- 建立連接 MCP 伺服器的主控應用程式
- 測試和除錯 MCP 實作
- 理解常見設定挑戰及其解決方案
- 將 MCP 實作連接至熱門 LLM 服務

## 設定您的 MCP 環境

在開始使用 MCP 之前，重要的是要準備開發環境並了解基本工作流程。本節將引導您完成初始設定步驟，確保順利開始使用 MCP。

### 先決條件

在深入 MCP 開發前，請確保您有：

- **開發環境**：符合您選擇語言（C#、Java、Python、TypeScript 或 JavaScript）
- **開發工具/編輯器**：Visual Studio、Visual Studio Code、IntelliJ、Eclipse、PyCharm 或任何現代程式編輯器
- **套件管理工具**：NuGet、Maven/Gradle、pip 或 npm/yarn
- **API 金鑰**：針對您計劃於主控應用使用的任何 AI 服務

### 官方 SDK

接下來章節您將看到使用 Python、TypeScript、Java 和 .NET 建構的解決方案。以下是所有官方支援的 SDK。

MCP 提供多語言官方 SDK（符合 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)）：
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - 與 Microsoft 合作維護
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - 與 Spring AI 合作維護
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 官方 TypeScript 實作
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 官方 Python 實作（FastMCP）
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 官方 Kotlin 實作
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - 與 Loopwork AI 合作維護
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 官方 Rust 實作
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - 官方 Go 實作

## 主要重點

- 使用各語言專屬 SDK 設定 MCP 開發環境簡單方便
- 建立 MCP 伺服器包含創建和註冊帶明確結構的工具
- MCP 用戶端連線至伺服器和模型以發揮擴充功能
- 測試與除錯對可靠的 MCP 實作至關重要
- 部署選項涵蓋本地開發到雲端解決方案

## 練習

我們提供一組範例，補充本節內所有章節的練習。此外每個章節亦有其專屬練習和作業。

- [Java 計算機](./samples/java/calculator/README.md)
- [.Net 計算機](../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](./samples/javascript/README.md)
- [TypeScript 計算機](./samples/typescript/README.md)
- [Python 計算機](../../../03-GettingStarted/samples/python)

## 附加資源

- [使用 Model Context Protocol 在 Azure 建立代理](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [使用 Azure Container Apps 遠端 MCP（Node.js/TypeScript/JavaScript）](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP 代理](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 接下來

從第一課開始：[建立您的第一個 MCP 伺服器](01-first-server/README.md)

完成本模組後，繼續學習：[模組 4：實務實作](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原稿文件以其母語版本為最具權威之資料來源。對於重要資訊，建議採用專業人員進行人工翻譯。因使用本翻譯所引致之任何誤解或誤譯，本公司概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->