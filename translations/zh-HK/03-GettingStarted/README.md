## 開始使用  

[![建立你的第一個 MCP 伺服器](../../../translated_images/zh-HK/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(點擊上方圖片觀看本課影片)_

本章節包含多個課程：

- **1 你的第一個伺服器**，在第一堂課中，你將學習如何建立你的第一個伺服器，並使用 inspector 工具進行檢查，這是測試及除錯伺服器的寶貴方法， [看課程](01-first-server/README.md)

- **2 客戶端**，在此課程中，你將學會如何編寫能連接伺服器的客戶端， [看課程](02-client/README.md)

- **3 帶 LLM 的客戶端**，一個更好的寫法是為客戶端加入 LLM，使其能與伺服器「協商」應該做什麼， [看課程](03-llm-client/README.md)

- **4 在 Visual Studio Code 使用伺服器 GitHub Copilot Agent 模式**。在本課中，我們會探討如何在 Visual Studio Code 中運行 MCP 伺服器， [看課程](04-vscode/README.md)

- **5 stdio 傳輸伺服器** stdio 傳輸是本地 MCP 伺服器與客戶端通訊的推薦標準，提供基於子程序的安全通訊與內建的程序隔離 [看課程](05-stdio-server/README.md)

- **6 MCP 的 HTTP 串流（可串流 HTTP）**。學習現代 HTTP 串流傳輸（根據 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http) 推薦方案），進度通知，以及如何使用可串流 HTTP 實作可擴充且即時的 MCP 伺服器及客戶端，[看課程](06-http-streaming/README.md)

- **7 使用 AI 工具包於 VSCode** 以使用並測試你的 MCP 客戶端及伺服器 [看課程](07-aitk/README.md)

- **8 測試**。本課重點介紹如何用多種方式測試伺服器與客戶端，[看課程](08-testing/README.md)

- **9 部署**。本章探討 MCP 解決方案的不同部署方式，[看課程](09-deployment/README.md)

- **10 進階伺服器使用**。本章包含進階伺服器使用方法，[看課程](./10-advanced/README.md)

- **11 認證**。本章涵蓋如何加入簡單認證，從基本認證到使用 JWT 與 RBAC。建議由此開始，然後參考第 5 章的進階主題及第 2 章中安全強化的建議，[看課程](./11-simple-auth/README.md)

- **12 MCP 主機**。設定及使用熱門 MCP 主機客戶端，包括 Claude Desktop、Cursor、Cline 和 Windsurf。學習傳輸類型及除錯方法，[看課程](./12-mcp-hosts/README.md)

- **13 MCP 檢查器**。使用 MCP 檢查器工具互動式除錯及測試 MCP 伺服器。學習工具、資源及協定訊息除錯，[看課程](./13-mcp-inspector/README.md)

- **14 取樣**。建立 MCP 伺服器與 MCP 客戶端協作處理 LLM 相關任務，[看課程](./14-sampling/README.md)

- **15 MCP Apps**。打造同時回應 UI 指令的 MCP 伺服器，[看課程](./15-mcp-apps/README.md)

Model Context Protocol (MCP) 是一個開放協定，標準化應用程式如何為 LLM 提供背景資料。可將 MCP 想像成 AI 應用程式的 USB-C 端口——提供一個標準化的方式將 AI 模型連接至不同資料來源與工具。

## 學習目標

完成本課後，你將能：

- 為 C#、Java、Python、TypeScript 及 JavaScript 設定 MCP 開發環境
- 建立並部署具自訂功能（資源、提示及工具）的基本 MCP 伺服器
- 建立連接 MCP 伺服器的主機應用程式
- 測試與除錯 MCP 實作
- 理解常見設定難題及其解決方案
- 連接你的 MCP 實作與熱門 LLM 服務

## 設定你的 MCP 環境

開始使用 MCP 前，準備好你的開發環境並了解基本工作流程很重要。本節將引導你完成初始設定步驟，確保 MCP 使用順利。

### 前置需求

開始 MCP 開發前，請確保你擁有：

- **開發環境**：適合你所選語言（C#、Java、Python、TypeScript 或 JavaScript）
- **IDE/編輯器**：Visual Studio、Visual Studio Code、IntelliJ、Eclipse、PyCharm 或任何現代程式編輯器
- **套件管理工具**：NuGet、Maven/Gradle、pip 或 npm/yarn
- **API 金鑰**：用於你計劃在主機應用程式使用的任何 AI 服務

### 官方 SDK

接下來的章節中，你會看到 Python、TypeScript、Java 和 .NET 的範例。以下是所有官方支援的 SDK。

MCP 提供多種語言的官方 SDK（依據 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)）：
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - 與 Microsoft 合作維護
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - 與 Spring AI 合作維護
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 官方 TypeScript 實作
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 官方 Python 實作（FastMCP）
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 官方 Kotlin 實作
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - 與 Loopwork AI 合作維護
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 官方 Rust 實作
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - 官方 Go 實作

## 重要重點

- 利用語言專用的 SDK，設定 MCP 開發環境相當簡單
- 建立 MCP 伺服器需創建並註冊具有明確結構的工具
- MCP 客戶端連接伺服器與模型，擴充功能
- 測試與除錯對 MCP 實作至關重要
- 部署方案涵蓋本地開發到雲端解決方案

## 練習範例

我們準備了一組範例，輔助你完成本章所有章節中的練習。此外，每章也包含專屬練習與作業。

- [Java 計算機](./samples/java/calculator/README.md)
- [.Net 計算機](../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](./samples/javascript/README.md)
- [TypeScript 計算機](./samples/typescript/README.md)
- [Python 計算機](../../../03-GettingStarted/samples/python)

## 額外資源

- [使用 Model Context Protocol 在 Azure 上建立代理](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [透過 Azure Container Apps 遠端 MCP（Node.js/TypeScript/JavaScript）](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP 代理](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 接下來做什麼

從第一課開始學習：[建立你的第一個 MCP 伺服器](01-first-server/README.md)

完成此模組後，繼續進階學習：[模組 4：實務應用](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提升準確度，但請注意，自動翻譯可能包含錯誤或不準確之處。原文的母語版本應視為權威版本。對於重要資訊，建議尋求專業人工翻譯。本公司概不對因使用此翻譯而導致的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->