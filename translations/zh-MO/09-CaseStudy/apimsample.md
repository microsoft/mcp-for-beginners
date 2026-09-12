# 個案研究：在 API 管理中以 MCP 伺服器方式公開 REST API

Azure API 管理是一項在您的 API 端點之上提供閘道服務的產品。其運作方式是 Azure API 管理充當您 API 之前的代理，並可以決定如何處理傳入請求。

使用它，您可以新增一整套功能，例如：

- <strong>安全性</strong>，您可以使用從 API 金鑰、JWT 到受管理身份的各種機制。
- <strong>速率限制</strong>，一項很棒的功能是能決定每個特定時間單位內允許通過的呼叫數量。這有助於確保所有用戶都有良好的使用體驗，也確保您的服務不會因請求過多而不堪負荷。
- <strong>擴展與負載平衡</strong>。您可以設定多個端點來分攤負載，並且可以決定如何「負載平衡」。
- **AI 功能，例如語意快取**、令牌限制與監控等。這些都是提升響應速度及協助您掌握令牌消耗的好功能。[點此閱讀詳情](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 為何選擇 MCP + Azure API 管理？

模型上下文協定(Model Context Protocol, MCP) 日益成為代理型 AI 應用的標準，以及如何以一致方式公開工具和資料。當您需要「管理」API 時，Azure API 管理自然是首選。MCP 伺服器通常會與其他 API 整合以解析對工具的請求，因此結合 Azure API 管理與 MCP 十分合理。

## 概覽

在本用例中，我們將學習如何將 API 端點公開為 MCP 伺服器。透過此方式，我們不僅能輕鬆讓這些端點成為代理型應用的一部分，還可利用 Azure API 管理的各項功能。

## 主要功能

- 您可選擇欲公開為工具的端點方法。
- 額外功能取決於您在 API 的政策區段中如何設定，但這裡會示範如何新增速率限制。

## 前置步驟：匯入 API

如果您在 Azure API 管理已有 API，非常好，可以跳過此步驟。若沒有，請參考此連結，[將 API 匯入 Azure API 管理](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 將 API 公開為 MCP 伺服器

要公開 API 端點，請遵循以下步驟：

1. 前往 Azure 入口網站，並訪問 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
進入您的 API 管理實例。

1. 在左側功能表中，選取 APIs > MCP Servers > + 建立新的 MCP 伺服器。

1. 在 API 中，選擇欲公開為 MCP 伺服器的 REST API。

1. 選擇一個或多個 API 操作公開為工具。您可以選擇全部操作或只有特定操作。

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. 選擇 <strong>建立</strong>。

1. 前往功能表選項 **APIs** 和 **MCP Servers**，您應該會看到以下畫面：

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 伺服器已建立，API 操作公開為工具。MCP 伺服器會列在 MCP Servers 面板中。URL 欄位顯示 MCP 伺服器的端點，您可以用來進行測試或在客戶端應用中呼叫。

## 選擇性：設定政策

Azure API 管理有一個核心概念是政策，您可以為端點設定各種規則，例如速率限制或語意快取。這些政策皆以 XML 編寫。

以下示範如何為 MCP 伺服器設定速率限制政策：

1. 在入口網站中，於 APIs 下，選擇 **MCP Servers**。

1. 選取您所建立的 MCP 伺服器。

1. 在左側選單下的 MCP 部分，選擇 **Policies**。

1. 在政策編輯器中，新增或編輯您想套用於 MCP 伺服器工具的政策。政策以 XML 格式定義。例如，您可以新增政策限制 MCP 伺服器工具的呼叫數量（本範例為每 30 秒每個客戶端 IP 地址限制 5 次呼叫）。以下 XML 會啟用速率限制：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    這是政策編輯器的圖片：

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## 嘗試使用

讓我們確認 MCP 伺服器是否依預期運作。

> [!NOTE]
> Azure API 管理目前透過可串流
> HTTP `/mcp` 端點公開此伺服器。舊有的 HTTP+SSE `/sse` 傳輸方式已棄用，
> 僅建議於舊版客戶端中使用。

為此，我們將使用 Visual Studio Code 與 GitHub Copilot 及其代理模式。我們將 MCP 伺服器加入 *mcp.json*。透過此方式，Visual Studio Code 將成為具代理功能的客戶端，終端使用者能輸入提示詞並與伺服器互動。

現在示範如何在 Visual Studio Code 中加入 MCP 伺服器：

1. 使用 MCP：「從命令面板中執行新增伺服器命令」。

1. 當系統提示時，選擇伺服器類型：**HTTP（HTTP 或 Server Sent Events）**。

1. 輸入 MCP 伺服器在 API 管理中顯示的可串流 HTTP URL。
    例如：
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`。

1. 輸入您選擇的伺服器 ID。此值不重要，但可幫助您記住此伺服器實例。

1. 選擇把設定儲存到工作區設定或是使用者設定。

  - <strong>工作區設定</strong> - 伺服器設定儲存在當前工作區專屬的 .vscode/mcp.json 檔案內。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - <strong>使用者設定</strong> - 伺服器設定會加入全域 *settings.json* 檔案，可在所有工作區使用。設定內容大致如下：

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. 您還需新增一個標頭以確保能正確向 Azure API 管理進行驗證。它使用一個名為 **Ocp-Apim-Subscription-Key** 的標頭。

    - 以下示範如何加入此標頭至設定：

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，此設定會促使系統顯示提示，請您輸入在 Azure 入口網站中 Azure API 管理實例的 API 金鑰值。

   - 若要改為加入 *mcp.json*，可以如此新增：

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

現在設定完成(無論是在設定或 *.vscode/mcp.json* 中)。讓我們試試看。

右上方應會有一個工具按鈕，該工具列出伺服器公開的工具：

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 點選工具按鈕，您會看到如下的工具清單：

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 在聊天視窗輸入提示以喚用相應工具。例如，如果您選擇了查詢訂單資訊的工具，可以向代理詢問訂單。以下是示例提示：

    ```text
    get information from order 2
    ```

    接著系統會顯示工具按鈕，詢問您是否繼續執行該工具。選擇繼續後，您將看到類似以下的輸出結果：

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上圖所呈現結果視您設定的工具而異，基本上概念就是顯示類似的文字回應**


## 參考資料

以下資源可供您了解更多：

- [Azure API 管理與 MCP 教學](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 範例：使用 Azure API 管理保護遠端 MCP 伺服器(實驗性功能)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 用戶端授權實驗室](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Azure API 管理擴充功能於 VS Code 匯入與管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API Center 註冊與探索遠端 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 精彩的開源倉庫，展現 Azure API 管理的多種 AI 功能
- [AI Gateway 工作坊](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure 入口網站進行的工作坊，是開始探索 AI 功能的絕佳途徑。

## 接下來

- 返回： [個案研究總覽](./README.md)
- 下一步： [Azure AI 旅遊代理](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->