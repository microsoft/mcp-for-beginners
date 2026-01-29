# 案例研究：在 API 管理中將 REST API 暴露為 MCP 伺服器

Azure API 管理是一項服務，提供 API 端點之上的網關。其運作方式是 Azure API 管理充當您的 API 前端代理，並決定如何處理傳入的請求。

使用它可以添加一系列功能，例如：

- **安全性**，您可以使用 API 金鑰、JWT 或受管理的身份。
- **速率限制**，一個很棒的功能是能夠決定在特定時間單位內允許多少次呼叫。這有助於確保所有使用者都能有良好的體驗，同時避免您的服務因請求過多而崩潰。
- **擴展性與負載平衡**，您可以設置多個端點來分擔負載，並決定如何進行「負載平衡」。
- **AI 功能，例如語義快取**、令牌限制、令牌監控等。這些功能能提升響應速度，並幫助您掌握令牌使用情況。[了解更多](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 為什麼選擇 MCP + Azure API 管理？

模型上下文協議（Model Context Protocol，MCP）正迅速成為代理型 AI 應用的標準，以及以一致方式暴露工具和數據的方式。當您需要「管理」API 時，Azure API 管理是一個自然的選擇。MCP 伺服器通常會與其他 API 集成，例如解決工具請求。因此，結合 Azure API 管理和 MCP 是非常合理的。

## 概述

在這個特定的使用案例中，我們將學習如何將 API 端點暴露為 MCP 伺服器。通過這樣做，我們可以輕鬆地將這些端點整合到代理型應用中，同時利用 Azure API 管理的功能。

## 主要功能

- 您可以選擇要暴露為工具的端點方法。
- 您獲得的額外功能取決於您在 API 的策略部分中配置的內容。但在這裡，我們將展示如何添加速率限制。

## 前置步驟：導入 API

如果您已經在 Azure API 管理中擁有 API，那很好，您可以跳過此步驟。如果沒有，請查看此連結：[將 API 導入到 Azure API 管理](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 將 API 暴露為 MCP 伺服器

要暴露 API 端點，請按照以下步驟操作：

1. 前往 Azure Portal，並訪問以下地址 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   導航至您的 API 管理實例。

1. 在左側菜單中，選擇 **APIs > MCP Servers > + Create new MCP Server**。

1. 在 API 中，選擇一個 REST API 以暴露為 MCP 伺服器。

1. 選擇一個或多個 API 操作以暴露為工具。您可以選擇所有操作或僅特定操作。

    ![選擇要暴露的方法](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. 選擇 **Create**。

1. 導航至菜單選項 **APIs** 和 **MCP Servers**，您應該看到以下內容：

    ![在主面板中查看 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 伺服器已創建，API 操作已暴露為工具。MCP 伺服器列在 MCP Servers 面板中。URL 列顯示 MCP 伺服器的端點，您可以用於測試或在客戶端應用中使用。

## 可選：配置策略

Azure API 管理的核心概念是策略，您可以為端點設置不同的規則，例如速率限制或語義快取。這些策略是用 XML 編寫的。

以下是如何為 MCP 伺服器設置速率限制策略：

1. 在入口網站中，選擇 **APIs > MCP Servers**。

1. 選擇您創建的 MCP 伺服器。

1. 在左側菜單中，選擇 **Policies**。

1. 在策略編輯器中，添加或編輯您希望應用於 MCP 伺服器工具的策略。這些策略以 XML 格式定義。例如，您可以添加一個策略以限制對 MCP 伺服器工具的呼叫次數（在此示例中，每個客戶端 IP 地址每 30 秒最多 5 次呼叫）。以下是 XML 代碼，將導致速率限制：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    以下是策略編輯器的圖片：

    ![策略編輯器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## 試用

讓我們確保 MCP 伺服器按預期工作。

為此，我們將使用 Visual Studio Code 和 GitHub Copilot 的代理模式。我們將 MCP 伺服器添加到 *mcp.json* 文件中。通過這樣做，Visual Studio Code 將充當具有代理功能的客戶端，最終使用者可以輸入提示並與該伺服器交互。

以下是如何在 Visual Studio Code 中添加 MCP 伺服器：

1. 使用 MCP：**從命令面板添加伺服器命令**。

1. 當提示時，選擇伺服器類型：**HTTP（HTTP 或 Server Sent Events）**。

1. 輸入 API 管理中 MCP 伺服器的 URL。例如：**https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse**（用於 SSE 端點）或 **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp**（用於 MCP 端點），注意傳輸方式的區別是 `/sse` 或 `/mcp`。

1. 輸入您選擇的伺服器 ID。這不是重要的值，但它將幫助您記住該伺服器實例。

1. 選擇是否將配置保存到工作區設置或用戶設置。

  - **工作區設置** - 伺服器配置保存到僅在當前工作區可用的 .vscode/mcp.json 文件。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    或者，如果您選擇流式 HTTP 作為傳輸方式，則會稍有不同：

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **用戶設置** - 伺服器配置添加到您的全局 *settings.json* 文件中，並在所有工作區中可用。配置類似於以下內容：

    ![用戶設置](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. 您還需要添加配置，即一個標頭，以確保它能正確地向 Azure API 管理進行身份驗證。它使用一個名為 **Ocp-Apim-Subscription-Key** 的標頭。

    - 以下是如何將其添加到設置：

    ![添加身份驗證標頭](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，這將導致顯示提示，要求您輸入 API 金鑰值，該值可以在 Azure Portal 的 Azure API 管理實例中找到。

   - 要將其添加到 *mcp.json* 中，您可以這樣添加：

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### 使用代理模式

現在我們已經在設置或 *.vscode/mcp.json* 中完成了配置。讓我們試試看。

應該有一個工具圖標，像這樣，列出了伺服器暴露的工具：

![伺服器中的工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 點擊工具圖標，您應該看到如下工具列表：

    ![工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 在聊天中輸入提示以調用工具。例如，如果您選擇了一個工具來獲取訂單信息，您可以向代理詢問訂單。以下是提示示例：

    ```text
    get information from order 2
    ```

    您現在會看到一個工具圖標，要求您繼續調用工具。選擇繼續運行工具，您應該看到如下輸出：

    ![提示結果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **您看到的內容取決於您設置的工具，但目的是您能獲得如上所示的文本響應**

## 參考資料

以下是更多學習資源：

- [Azure API 管理與 MCP 教程](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 示例：使用 Azure API 管理安全遠程 MCP 伺服器（實驗性）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 客戶端授權實驗室](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Azure API 管理擴展在 VS Code 中導入和管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API Center 中註冊和發現遠程 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 優秀的資源庫，展示了 Azure API 管理的許多 AI 功能
- [AI Gateway 工作坊](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure Portal 的工作坊，是開始評估 AI 功能的好方法

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對於因使用本翻譯而引起的任何誤解或錯誤解讀概不負責。