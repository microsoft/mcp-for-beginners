# 案例研究：在 API 管理中将 REST API 暴露为 MCP 服务器

Azure API 管理是一项服务，它为您的 API 端点提供一个网关。其工作原理是，Azure API 管理充当您的 API 前面的代理，并可以决定如何处理传入的请求。

通过使用它，您可以添加一系列功能，例如：

- **安全性**：您可以使用从 API 密钥、JWT 到托管身份的所有内容。
- **速率限制**：一个很棒的功能是能够决定在特定时间单位内允许通过的调用次数。这有助于确保所有用户都能获得良好的体验，同时也防止您的服务因请求过多而不堪重负。
- **扩展性和负载均衡**：您可以设置多个端点来分担负载，并且可以决定如何进行“负载均衡”。
- **AI 功能**：例如语义缓存、令牌限制和令牌监控等。这些功能不仅提高了响应速度，还帮助您更好地管理令牌使用情况。[了解更多](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 为什么选择 MCP + Azure API 管理？

模型上下文协议（Model Context Protocol, MCP）正在迅速成为代理型 AI 应用程序的标准，用于以一致的方式暴露工具和数据。而当您需要“管理”API 时，Azure API 管理是一个自然的选择。MCP 服务器通常会与其他 API 集成，例如解析工具请求。因此，将 Azure API 管理与 MCP 结合起来非常有意义。

## 概述

在这个具体的用例中，我们将学习如何将 API 端点暴露为 MCP 服务器。通过这样做，我们可以轻松地将这些端点作为代理型应用程序的一部分，同时利用 Azure API 管理的功能。

## 关键功能

- 您可以选择要作为工具暴露的端点方法。
- 您获得的附加功能取决于您在 API 的策略部分中配置的内容。在这里，我们将展示如何添加速率限制。

## 前置步骤：导入 API

如果您已经在 Azure API 管理中有一个 API，那很好，您可以跳过此步骤。如果没有，请查看此链接：[将 API 导入到 Azure API 管理](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 将 API 暴露为 MCP 服务器

要暴露 API 端点，请按照以下步骤操作：

1. 访问 Azure 门户，地址为 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>，导航到您的 API 管理实例。

1. 在左侧菜单中，选择 **APIs > MCP Servers > + Create new MCP Server**。

1. 在 API 中，选择一个 REST API 以暴露为 MCP 服务器。

1. 选择一个或多个 API 操作以作为工具暴露。您可以选择所有操作，也可以仅选择特定操作。

    ![选择要暴露的方法](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. 选择 **Create**。

1. 导航到菜单选项 **APIs** 和 **MCP Servers**，您应该会看到以下内容：

    ![在主面板中查看 MCP 服务器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 服务器已创建，API 操作已作为工具暴露。MCP 服务器列在 MCP Servers 面板中。URL 列显示了 MCP 服务器的端点，您可以通过该端点进行测试或在客户端应用程序中调用。

## 可选：配置策略

Azure API 管理的核心概念是策略，您可以为端点设置不同的规则，例如速率限制或语义缓存。这些策略是用 XML 编写的。

以下是如何为 MCP 服务器设置速率限制策略：

1. 在门户中，进入 **APIs**，选择 **MCP Servers**。

1. 选择您创建的 MCP 服务器。

1. 在左侧菜单中，选择 **Policies**。

1. 在策略编辑器中，添加或编辑您希望应用于 MCP 服务器工具的策略。这些策略以 XML 格式定义。例如，您可以添加一个策略来限制对 MCP 服务器工具的调用（在此示例中，每个客户端 IP 地址每 30 秒最多调用 5 次）。以下是一个会导致速率限制的 XML：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    以下是策略编辑器的图片：

    ![策略编辑器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## 测试

让我们确保 MCP 服务器按预期工作。

为此，我们将使用 Visual Studio Code 和 GitHub Copilot 的代理模式。我们将在 *mcp.json* 文件中添加 MCP 服务器。通过这样做，Visual Studio Code 将充当具有代理功能的客户端，最终用户可以输入提示并与该服务器交互。

以下是如何在 Visual Studio Code 中添加 MCP 服务器：

1. 使用命令面板中的 **MCP: Add Server** 命令。

1. 在提示时，选择服务器类型：**HTTP (HTTP or Server Sent Events)**。

1. 输入 API 管理中 MCP 服务器的 URL。例如：**https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse**（用于 SSE 端点）或 **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp**（用于 MCP 端点），注意两者的区别在于 `/sse` 或 `/mcp`。

1. 输入您选择的服务器 ID。这不是一个重要的值，但它将帮助您记住该服务器实例。

1. 选择是否将配置保存到工作区设置或用户设置。

  - **工作区设置** - 服务器配置将保存到当前工作区中可用的 .vscode/mcp.json 文件。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    或者，如果您选择流式 HTTP 作为传输方式，它会略有不同：

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **用户设置** - 服务器配置将添加到您的全局 *settings.json* 文件中，并在所有工作区中可用。配置类似于以下内容：

    ![用户设置](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. 您还需要添加配置，即一个头部，以确保它能够正确地向 Azure API 管理进行身份验证。它使用一个名为 **Ocp-Apim-Subscription-Key** 的头部。

    - 以下是如何将其添加到设置中的方法：

    ![为身份验证添加头部](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，这将导致显示一个提示，要求您输入 API 密钥值，您可以在 Azure 门户中找到您的 Azure API 管理实例的 API 密钥。

   - 如果要将其添加到 *mcp.json* 中，可以这样添加：

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

现在我们已经在设置或 *.vscode/mcp.json* 中完成了配置。让我们试试。

应该会有一个工具图标，显示如下，列出了来自服务器的暴露工具：

![来自服务器的工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 点击工具图标，您应该会看到如下所示的工具列表：

    ![工具列表](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 在聊天中输入提示以调用工具。例如，如果您选择了一个工具来获取订单信息，您可以向代理询问订单。以下是一个示例提示：

    ```text
    get information from order 2
    ```

    您现在会看到一个工具图标，提示您继续调用工具。选择继续运行工具，您应该会看到如下输出：

    ![提示结果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上面显示的内容取决于您设置的工具，但目的是您会收到如上所示的文本响应。**

## 参考资料

以下是您可以了解更多内容的资源：

- [Azure API 管理和 MCP 教程](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 示例：使用 Azure API 管理保护远程 MCP 服务器（实验性）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 客户端授权实验](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Azure API 管理扩展在 VS Code 中导入和管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API 中心注册和发现远程 MCP 服务器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 一个展示 Azure API 管理多种 AI 功能的优秀仓库
- [AI Gateway 工作坊](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure 门户的工作坊，这是评估 AI 功能的一个很好的起点。

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而导致的任何误解或误读，我们概不负责。