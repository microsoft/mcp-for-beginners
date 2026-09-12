# 案例研究：在 API 管理中以 MCP 伺服器形式暴露 REST API

Azure API 管理是一項服務，提供在您的 API 端點之上的閘道。其運作方式是 Azure API 管理像是您的 API 之前的一個代理，並且可以決定如何處理傳入的請求。

使用它，您可以加入一整套功能，例如：

- <strong>安全性</strong>，您可以使用從 API 金鑰、JWT 到託管身分識別的所有方法。
- <strong>速率限制</strong>，一個很棒的功能是能夠決定每一特定時間單位內允許多少呼叫通過。這有助於確保所有用戶都有良好的使用體驗，且您的服務不會被請求淹沒。
- <strong>擴充與負載平衡</strong>。您可以設置多個端點以分擔負載，並且還可以決定如何「負載平衡」。
- **AI 功能如語意快取**、代幣限制與代幣監控等。這些是提升反應速度並幫助您掌握代幣使用狀況的絕佳功能。[在這裡閱讀更多](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 為什麼選擇 MCP + Azure API 管理？

Model Context Protocol 正迅速成為代理式 AI 應用及如何以一致方式暴露工具和資料的標準。當您需要「管理」API 時，Azure API 管理是自然而然的選擇。MCP 伺服器通常會整合其他 API 以解決對工具的請求。因此，結合 Azure API 管理與 MCP 是非常合理的。

## 概述

在這個特定的使用案例中，我們將學習如何將 API 端點暴露為 MCP 伺服器。透過此方法，我們能輕鬆將這些端點成為代理式應用的一部分，同時利用 Azure API 管理的功能。

## 主要功能

- 您選擇要暴露為工具的端點方法。
- 您獲得的附加功能取決於您在 API 的政策部分所設定的內容。但在此我們將展示如何加入速率限制。

## 預備步驟：匯入 API

如果您已在 Azure API 管理中有 API，那很好，您可以跳過此步驟。若沒有，請參考此連結，[匯入 API 至 Azure API 管理](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 將 API 暴露為 MCP 伺服器

要暴露 API 端點，請依照以下步驟：

1. 前往 Azure 入口網站，並進入以下網址 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
前往您的 API 管理實例。

1. 在左側選單中，選取 APIs > MCP Servers > + 建立新的 MCP 伺服器。

1. 在 API 中，選擇要暴露為 MCP 伺服器的 REST API。

1. 選擇一個或多個 API 操作暴露為工具。您可以選擇所有操作，或僅特定操作。

    ![選擇要暴露的方法](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. 選擇 <strong>建立</strong>。

1. 前往選單選項 **APIs** 及 **MCP Servers**，您應該會看到以下畫面：

    ![主畫面中的 MCP 伺服器列表](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 伺服器已建立且 API 操作已暴露為工具。MCP 伺服器顯示於 MCP Servers 窗格中。URL 欄位顯示 MCP 伺服器的端點，您可以用於測試或客戶端應用程式中呼叫。

## 選擇性步驟：設定政策

Azure API 管理的核心概念為政策，您可為端點設定不同規則，例如速率限制或語意快取。這些政策是以 XML 撰寫。

以下為如何設定 MCP 伺服器速率限制政策：

1. 在入口網站中，於 APIs 下選擇 **MCP Servers**。

1. 選取您已建立的 MCP 伺服器。

1. 在左側選單中，於 MCP 下選擇 **Policies**。

1. 在政策編輯器中，新增或編輯想套用到 MCP 伺服器工具的政策。這些政策採 XML 格式定義。例如，您可以新增限制呼叫 MCP 伺服器工具的政策（此例為每 30 秒每客戶端 IP 限制 5 次呼叫）。以下 XML 將造成速率限制：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    以下是政策編輯器的圖片：

    ![政策編輯器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## 試用

讓我們確認 MCP 伺服器是否如預期運作。

> [!NOTE]
> Azure API 管理目前透過可串流的
> HTTP `/mcp` 端點來暴露該伺服器。舊版 HTTP+SSE `/sse` 傳輸方式已被淘汰，
> 僅應用於舊式客戶端。

為此，我們將使用 Visual Studio Code 與 GitHub Copilot 及其代理模式。我們將 MCP 伺服器加入至 *mcp.json*。如此一來，Visual Studio Code 將充當具有代理能力的客戶端，最終用戶即可輸入提示並與該伺服器互動。

現在來看看如何在 Visual Studio Code 中加入 MCP 伺服器：

1. 從命令面板使用 MCP: <strong>新增伺服器指令</strong>。

1. 出現提示時，選擇伺服器類型：**HTTP (HTTP 或 Server Sent Events)**。

1. 輸入 API 管理中顯示的 MCP 伺服器可串流 HTTP URL。
    例如：
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`。

1. 輸入您選擇的伺服器 ID。這不是重要值，但會幫助您記住此伺服器實例。

1. 選擇是將設定儲存於工作區設定或使用者設定。

  - <strong>工作區設定</strong> - 伺服器設定將儲存於僅限當前工作區的 .vscode/mcp.json 檔案中。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - <strong>使用者設定</strong> - 伺服器設定會加入您的全域 *settings.json* 檔案中，可在所有工作區使用。設定內容類似如下：

    ![使用者設定](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. 您還需要新增設定，即一個標頭以確保它能正確對 Azure API 管理進行身份驗證。它使用名為 **Ocp-Apim-Subscription-Key** 的標頭。

    - 以下示範如何新增至設定：

    ![新增認證標頭](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，這會導致彈出提示要求您輸入 API 金鑰值，該值可在 Azure 入口網站對您的 Azure API 管理實例找到。

   - 若要改為新增到 *mcp.json*，您可以如此新增：

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

現在無論是設定檔案還是 *.vscode/mcp.json* 都已配置完成。讓我們試試看。

應該會有一個工具圖示，列出您伺服器暴露的工具：

![伺服器工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 點擊工具圖示，您應該會看到如下的工具列表：

    ![工具清單](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 在聊天中輸入提示以呼叫工具。例如，若您選擇的工具是查詢訂單資訊，您可以向代理詢問訂單。以下為範例提示：

    ```text
    get information from order 2
    ```

    您將看到一個工具圖示提示您是否繼續呼叫該工具。選擇繼續執行，您應該會看到類似以下的輸出：

    ![提示輸出結果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **您在上方看到的內容依您設置的工具而異，但概念是您會獲得如上所示的文字回應**


## 參考資料

您可以透過以下方式了解更多：

- [Azure API 管理與 MCP 教學](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 範例：使用 Azure API 管理安全遠端 MCP 伺服器（實驗性）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 客戶端授權實驗室](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Azure API Management 擴充套件於 VS Code 匯入及管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API Center 註冊與搜尋遠端 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 這是個很棒的資源庫，展示許多使用 Azure API 管理的 AI 能力
- [AI Gateway 工作坊](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure 入口網站的工作坊，是開始評估 AI 能力的極好方式。

## 接下來的步驟

- 回到: [案例研究總覽](./README.md)
- 下一篇: [Azure AI 旅遊代理人](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->