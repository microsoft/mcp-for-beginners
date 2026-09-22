# 案例研究：在 API 管理中以 MCP 伺服器方式公開 REST API

Azure API Management 是一項在您的 API 端點之上提供閘道的服務。其運作方式是 Azure API Management 作為您 API 前端的代理，可以決定如何處理進入的請求。

使用它，您可以新增許多功能，例如：

- <strong>安全性</strong>，您可以使用 API 金鑰、JWT 到託管身份識別等各種方式。
- <strong>速率限制</strong>，此功能允許您決定在特定時間單位內通過多少呼叫，這有助於確保所有使用者都有良好的體驗，並且您的服務不會因請求過多而超載。
- <strong>擴展性與負載平衡</strong>。您可以設定多個端點以分擔負載，也可以決定如何「負載平衡」。
- **AI 功能，如語義快取**、令牌限制、令牌監控等功能。這些優秀的功能不僅提升響應速度，也有助於您掌握令牌的使用狀況。[在此閱讀更多](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 為什麼選擇 MCP + Azure API Management？

Model Context Protocol 正迅速成為代理 AI 應用和一致性公開工具及資料的標準。Azure API Management 是「管理」API 時的自然選擇。MCP 伺服器通常會整合其他 API 以解析請求指向工具。例如，結合 Azure API Management 與 MCP 意義重大。

## 概覽

在此特定使用案例中，我們將學習如何以 MCP 伺服器公開 API 端點。如此一來，我們可以輕鬆將此端點納入代理應用，同時利用 Azure API Management 的功能。

## 主要功能

- 您可以選擇欲公開為工具的端點方法。
- 所獲得的其他功能取決於您在 API 政策區段中配置的內容。不過這裡我們將示範如何新增速率限制。

## 預備步驟：匯入 API

如果您已在 Azure API Management 擁有 API，太好了，可以跳過此步驟。若沒有，請參考此連結，[匯入 API 至 Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 將 API 公開為 MCP 伺服器

若要公開 API 端點，請遵循以下步驟：

1. 前往 Azure 入口網站並訪問以下地址 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
進入您的 API Management 實例。

1. 在左側選單中，選擇 APIs > MCP Servers > + 建立新的 MCP 伺服器。

1. 在 API 項目中，選擇一個 REST API 作為 MCP 伺服器公開。

1. 選擇一個或多個 API 操作以公開為工具。您可以選擇全部操作，或只選特定操作。

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. 選擇 <strong>建立</strong>。


1. 導覽至選單選項 **APIs** 和 **MCP Servers**，您應該會看到以下畫面：

    ![在主面板中查看 MCP Server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 伺服器已建立，且 API 操作已作為工具公開。MCP 伺服器會列在 MCP Servers 面板中。URL 欄顯示您可用來進行測試或在用戶端應用程式中呼叫 MCP 伺服器的端點。

## 選用：設定政策

Azure API Management 有核心概念「政策」，您可以為端點設定不同規則，例如速率限制或語意快取。這些政策以 XML 撰寫。

以下說明如何設定速率限制政策給您的 MCP Server：

1. 在入口網站中，於 APIs 項目下，選取 **MCP Servers**。

1. 選擇您所建立的 MCP 伺服器。

1. 在左側選單中的 MCP 項目下，選擇 **Policies**。

1. 在政策編輯器中，新增或編輯您想套用於 MCP 伺服器的工具的政策。政策以 XML 格式定義。例如，您可以加上政策以限制對 MCP 伺服器工具的呼叫次數（此範例中為每個客戶端 IP 地址每 30 秒最多 5 次呼叫）。以下是會造成速率限制的 XML：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    以下是政策編輯器的圖片：

    ![政策編輯器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## 試用看看

讓我們確認 MCP Server 運作正常。

> [!NOTE]
> Azure API Management 目前透過可串流
> 的 HTTP `/mcp` 端點公開此伺服器。舊版的 HTTP+SSE `/sse` 傳輸已被棄用，
> 僅應用於舊有用戶端。

為此，我們將使用 Visual Studio Code 和 GitHub Copilot 及其代理模式。我們會將 MCP 伺服器新增至 *mcp.json* 檔案中。這樣 Visual Studio Code 將能作用為代理功能的用戶端，最終使用者可以輸入提示字串並與該伺服器互動。

現在讓我們看看如何在 Visual Studio Code 中新增 MCP 伺服器：

1. 使用命令面板中的 MCP：**Add Server 命令**。

1. 當提示時，選擇伺服器類型：**HTTP (HTTP 或 Server Sent Events)**。

1. 輸入可串流 HTTP 的 MCP 伺服器端點 URL，此 URL 可在 API Management 中看到。
    例如：
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`。

1. 輸入您喜歡的伺服器 ID。此值不重要，但能幫助您辨識此伺服器實例。

1. 選擇將配置儲存至工作區設定或使用者設定。

  - <strong>工作區設定</strong> - 伺服器設定將儲存在僅限當前工作區的 .vscode/mcp.json 檔案中。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - <strong>使用者設定</strong> - 伺服器設定會加入您的全域 *settings.json* 檔中，可用於所有工作區。設定內容如下所示：

    ![使用者設定](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)


1. 您還需要添加配置，一個標頭以確保它能正確地向 Azure API 管理進行身份驗證。它使用一個名為 **Ocp-Apim-Subscription-Key** 的標頭。


    - 這是您如何將其新增到設定中的方式：

    ![新增用於驗證的標頭](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，這會顯示一個提示，要求您輸入 API 金鑰值，該值可在 Azure 入口網站中針對您的 Azure API 管理實例找到。

   - 若要改為將其新增到 *mcp.json*，您可以這樣新增：

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

現在無論是在設定中或 *.vscode/mcp.json* 中都已設定完成。讓我們試試看。

應該會有一個工具圖示，如下，列出您伺服器所公開的工具：

![來自伺服器的工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 點擊工具圖示，您應該會看到一個工具清單，如下：

    ![工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 在聊天框中輸入提示來調用該工具。例如，如果您選擇了一個工具來獲取訂單資訊，您可以詢問代理有關訂單的問題。以下是一個提示範例：

    ```text
    get information from order 2
    ```

    接著您將看到一個工具圖示，請選擇繼續呼叫該工具。選擇繼續後，您應該會看到如下的輸出結果：

    ![提示結果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **您在上方看到的內容依您設置的工具而定，但概念是您會看到類似上述的文字回應**


## 參考資料

這是您如何學習更多：

- [Azure API 管理與 MCP 教學](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 範例：使用 Azure API 管理保護遠端 MCP 伺服器 (實驗性)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 客戶端授權實驗室](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Azure API 管理擴充功能於 VS Code 匯入與管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API Center 註冊並探索遠端 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 很棒的資源庫，展示許多使用 Azure API 管理的 AI 功能
- [AI Gateway 工作坊](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure 入口網站的工作坊，是開始評估 AI 功能的好方式。

## 下一步

- 回到：[案例研究總覽](./README.md)
- 下一個：[Azure AI 旅行代理](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->