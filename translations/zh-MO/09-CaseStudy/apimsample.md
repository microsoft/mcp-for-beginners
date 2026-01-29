# 案例研究：在 API 管理中將 REST API 暴露為 MCP 伺服器

Azure API 管理是一項服務，為您的 API 端點提供一個網關。其運作方式是，Azure API 管理作為您的 API 前端代理，並決定如何處理進入的請求。

使用該服務，您可以添加一系列功能，例如：

- **安全性**：您可以使用 API 金鑰、JWT 或受管理的身份等多種方式。
- **速率限制**：一個很棒的功能是能夠決定在特定時間單位內允許的請求數量。這有助於確保所有用戶都能獲得良好的體驗，並防止您的服務因請求過多而超載。
- **擴展性與負載平衡**：您可以設置多個端點來分擔負載，並決定如何進行「負載平衡」。
- **AI 功能，例如語義快取**、令牌限制、令牌監控等。這些功能不僅提升了響應速度，還能幫助您更好地管理令牌使用情況。[了解更多](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 為什麼選擇 MCP + Azure API 管理？

模型上下文協議（Model Context Protocol, MCP）正迅速成為代理型 AI 應用程式的標準，並提供了一種一致的方式來暴露工具和數據。而當需要「管理」API 時，Azure API 管理是一個自然的選擇。MCP 伺服器通常會與其他 API 集成，例如解決工具請求。因此，將 Azure API 管理與 MCP 結合非常合理。

## 概述

在這個特定的用例中，我們將學習如何將 API 端點暴露為 MCP 伺服器。通過這樣做，我們可以輕鬆地將這些端點整合到代理型應用程式中，同時利用 Azure API 管理的功能。

## 關鍵功能

- 您可以選擇希望暴露為工具的端點方法。
- 您獲得的附加功能取決於您在 API 的策略部分中配置的內容。在這裡，我們將展示如何添加速率限制。

## 預備步驟：導入 API

如果您已經在 Azure API 管理中擁有一個 API，那麼可以跳過此步驟。如果沒有，請參考此鏈接：[將 API 導入到 Azure API 管理](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 將 API 暴露為 MCP 伺服器

要暴露 API 端點，請按照以下步驟操作：

1. 前往 Azure 入口網站，訪問以下地址 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>，進入您的 API 管理實例。

1. 在左側菜單中，選擇 **APIs > MCP Servers > + Create new MCP Server**。

1. 在 API 中，選擇一個 REST API，將其暴露為 MCP 伺服器。

1. 選擇一個或多個 API 操作以暴露為工具。您可以選擇所有操作，也可以僅選擇特定操作。

    ![選擇要暴露的方法](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. 點擊 **Create**。

1. 前往菜單選項 **APIs** 和 **MCP Servers**，您應該會看到以下內容：

    ![在主面板中查看 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 伺服器已創建，API 操作已作為工具暴露。MCP 伺服器列在 MCP Servers 面板中。URL 列顯示了 MCP 伺服器的端點，您可以用於測試或在客戶端應用程式中調用。

## 可選：配置策略

Azure API 管理的核心概念是策略，您可以為端點設置不同的規則，例如速率限制或語義快取。這些策略是用 XML 編寫的。

以下是如何為 MCP 伺服器設置速率限制策略：

1. 在入口網站中，進入 **APIs**，選擇 **MCP Servers**。

1. 選擇您創建的 MCP 伺服器。

1. 在左側菜單中，選擇 **Policies**。

1. 在策略編輯器中，添加或編輯您希望應用於 MCP 伺服器工具的策略。這些策略以 XML 格式定義。例如，您可以添加一個策略來限制對 MCP 伺服器工具的調用次數（在此示例中，每個客戶端 IP 地址每 30 秒最多 5 次調用）。以下是會導致速率限制的 XML：

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

讓我們確保 MCP 伺服器按預期運行。

為此，我們將使用 Visual Studio Code 和 GitHub Copilot 的代理模式。我們將 MCP 伺服器添加到 *mcp.json* 文件中。通過這樣做，Visual Studio Code 將作為具有代理功能的客戶端，最終用戶可以輸入提示並與該伺服器交互。

以下是如何在 Visual Studio Code 中添加 MCP 伺服器：

1. 使用 MCP：從命令面板中選擇 **Add Server** 命令。

1. 當被提示時，選擇伺服器類型：**HTTP (HTTP or Server Sent Events)**。

1. 輸入 API 管理中 MCP 伺服器的 URL。例如：**https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse**（對於 SSE 端點）或 **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp**（對於 MCP 端點），注意傳輸方式的區別在於 `/sse` 或 `/mcp`。

1. 輸入您選擇的伺服器 ID。這不是一個重要的值，但它將幫助您記住該伺服器實例。

1. 選擇是否將配置保存到您的工作區設置或用戶設置。

  - **工作區設置** - 伺服器配置將保存到僅在當前工作區可用的 .vscode/mcp.json 文件中。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    如果您選擇流式 HTTP 作為傳輸方式，則會略有不同：

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **用戶設置** - 伺服器配置將添加到您的全局 *settings.json* 文件中，並在所有工作區中可用。配置如下所示：

    ![用戶設置](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. 您還需要添加配置，即一個標頭，以確保正確地向 Azure API 管理進行身份驗證。它使用一個名為 **Ocp-Apim-Subscription-Key** 的標頭。

    - 以下是如何將其添加到設置中的方法：

    ![為身份驗證添加標頭](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，這將導致出現提示，要求您輸入 API 金鑰值，該值可以在 Azure 入口網站的 Azure API 管理實例中找到。

   - 如果要將其添加到 *mcp.json* 中，可以這樣添加：

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

應該會有一個工具圖標，列出來自伺服器的暴露工具：

![伺服器中的工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 點擊工具圖標，您應該會看到如下所示的工具列表：

    ![工具列表](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 在聊天中輸入提示以調用工具。例如，如果您選擇了一個工具來獲取訂單信息，您可以向代理詢問訂單。以下是示例提示：

    ```text
    get information from order 2
    ```

    您現在會看到一個工具圖標，提示您繼續調用工具。選擇繼續運行工具，您應該會看到如下所示的輸出：

    ![提示結果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上面顯示的內容取決於您設置的工具，但目的是獲得如上所示的文本響應。**

## 參考資料

以下是更多學習資源：

- [Azure API 管理與 MCP 教程](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 示例：使用 Azure API 管理保護遠程 MCP 伺服器（實驗性）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 客戶端授權實驗室](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Visual Studio Code 的 Azure API 管理擴展導入和管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API 中心中註冊和發現遠程 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 優秀的資源庫，展示了 Azure API 管理的多種 AI 功能
- [AI Gateway 工作坊](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure 入口網站的工作坊，是開始評估 AI 功能的好方法。

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀概不負責。