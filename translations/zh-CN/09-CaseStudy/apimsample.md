# 案例研究：在 API 管理中将 REST API 作为 MCP 服务器暴露

Azure API 管理是一项在您的 API 端点之上提供网关的服务。其工作原理是 Azure API 管理充当您 API 前面的代理，可以决定如何处理传入请求。

通过使用它，您可以添加一整套功能，例如：

- <strong>安全性</strong>，您可以使用从 API 密钥、JWT 到托管身份的所有认证方式。
- <strong>速率限制</strong>，一个很棒的功能是能够决定在特定时间单位内允许多少次调用通过。这有助于确保所有用户都拥有良好的体验，同时也防止您的服务被请求压垮。
- <strong>扩展与负载均衡</strong>。您可以设置多个端点以平衡负载，还可以决定如何进行“负载均衡”。
- **AI 功能，如语义缓存**、令牌限制和令牌监控等。这些都是很棒的功能，提升响应速度，同时帮助您掌控令牌消耗情况。[在这里阅读更多](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 为什么选择 MCP + Azure API 管理？

模型上下文协议（Model Context Protocol，MCP）正在迅速成为智能代理 AI 应用以及以一致方式暴露工具和数据的标准。当您需要“管理”API 时，Azure API 管理是一个自然的选择。MCP 服务器通常会集成其他 API 来解决对工具的请求。因此结合 Azure API 管理和 MCP 非常合理。

## 概述

在这个具体用例中，我们将学习如何将 API 端点暴露为 MCP 服务器。通过这样做，我们可以轻松地将这些端点作为智能代理应用的一部分，同时利用 Azure API 管理的功能。

## 主要功能

- 您选择要作为工具暴露的端点方法。
- 您获得的附加功能取决于您在 API 的策略部分配置的内容。但在这里，我们会展示如何添加速率限制。

## 预备步骤：导入 API

如果您已经在 Azure API 管理中拥有 API，那很好，可以跳过此步骤。如果没有，请查看此链接，[将 API 导入 Azure API 管理](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 将 API 作为 MCP 服务器暴露

要暴露 API 端点，请按照以下步骤操作：

1. 前往 Azure 门户并打开以下地址 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
前往您的 API 管理实例。

1. 在左侧菜单中，选择 APIs > MCP Servers > + 创建新的 MCP 服务器。

1. 在 API 中选择一个 REST API，将其暴露为 MCP 服务器。

1. 选择一个或多个 API 操作，将其作为工具暴露。您可以选择所有操作或仅特定操作。

    ![选择要暴露的方法](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. 选择 <strong>创建</strong>。

1. 前往菜单选项 **APIs** 和 **MCP Servers**，您应该会看到如下内容：

    ![在主面板中查看 MCP 服务器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 服务器已创建，且 API 操作已作为工具暴露。MCP 服务器列在 MCP Servers 面板中。URL 列显示您可调用用于测试或客户端应用的 MCP 服务器端点。

## 可选步骤：配置策略

Azure API 管理的核心概念是策略，您可在其中为端点设置不同规则，例如速率限制或语义缓存。策略以 XML 形式编写。

以下为如何设置速率限制策略以限制您的 MCP 服务器：

1. 在门户中，展开 APIs，选择 **MCP Servers**。

1. 选择您创建的 MCP 服务器。

1. 在左侧菜单中 MCP 下，选择 **Policies**。

1. 在策略编辑器中，添加或编辑要应用于 MCP 服务器工具的策略。策略以 XML 格式定义。例如，您可以添加策略限制对 MCP 服务器工具的调用（本示例为每个客户端 IP 每 30 秒最多 5 次调用）。以下 XML 可实现速率限制：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    以下是策略编辑器的截图：

    ![策略编辑器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## 试用

让我们确保 MCP 服务器按预期工作。

> [!NOTE]
> Azure API 管理目前通过 Streamable 的 HTTP `/mcp` 端点暴露此服务器。
> 旧的 HTTP+SSE `/sse` 传输已弃用，仅用于旧版客户端。


为此，我们将使用 Visual Studio Code 和 GitHub Copilot 及其 Agent 模式。我们将 MCP 服务器添加到 *mcp.json* 文件中。如此，Visual Studio Code 将作为具有代理能力的客户端，最终用户能够输入提示并与该服务器交互。

下面展示如何在 Visual Studio Code 中添加 MCP 服务器：

1. 通过命令面板使用 MCP: <strong>添加服务器命令</strong>。

1. 提示时，选择服务器类型：**HTTP（HTTP 或服务器发送事件）**。

1. 输入 API 管理中 MCP 服务器显示的 Streamable HTTP URL。
    例如：
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`。

1. 输入您选择的服务器 ID。这不是重要值，但将帮助您记住此服务器实例。

1. 选择将配置保存到工作区设置或用户设置。

  - <strong>工作区设置</strong> - 服务器配置保存至当前工作区可见的 .vscode/mcp.json 文件。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - <strong>用户设置</strong> - 服务器配置添加到全局 *settings.json* 文件，在所有工作区中可用。配置如下所示：

    ![用户设置](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. 您还需要添加配置，一个头部以确保正确向 Azure API 管理进行身份验证。它使用名为 **Ocp-Apim-Subscription-Key** 的头部。

    - 以下为添加到设置的方法：

    ![添加身份验证头部](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，这会提示输入 API 密钥值，您可以在 Azure 门户中您的 Azure API 管理实例找到该密钥。

   - 若添加到 *mcp.json*，可以这样添加：

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

现在我们已在设置中或 *.vscode/mcp.json* 中完成配置。让我们试用一下。

应该会有一个工具图标，如下所示，列出服务器暴露的工具：

![来自服务器的工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 点击工具图标，您应该会看到工具列表，如下所示：

    ![工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 在聊天中输入提示以调用工具。例如，如果您选择了一个获取订单信息的工具，可以向代理询问订单。下面是示例提示：

    ```text
    get information from order 2
    ```

    这时会显示一个工具图标，提示您是否继续调用工具。选择继续运行工具，您应该会看到如下输出：

    ![提示结果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上方显示内容取决于您设置的工具，但思路是您将获得类似的文本回复**


## 参考资料

以下是您可以进一步学习的资源：

- [Azure API 管理与 MCP 教程](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 示例：使用 Azure API 管理安全远程 MCP 服务器（实验性质）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 客户端授权实验室](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 VS Code 的 Azure API 管理扩展导入和管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API 中心注册和发现远程 MCP 服务器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 一个极好的代码仓库，展示了许多使用 Azure API 管理的 AI 功能
- [AI Gateway 研讨会](https://azure-samples.github.io/AI-Gateway/)  包含使用 Azure 门户的研讨会，是开始评估 AI 功能的绝佳方式。

## 后续内容

- 返回：[案例研究概览](./README.md)
- 下一篇：[Azure AI 旅行代理](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->