# Model Context Protocol (MCP) と Azure AI Foundry の統合

このガイドでは、Model Context Protocol (MCP) サーバーを Azure AI Foundry エージェントと統合し、強力なツールオーケストレーションとエンタープライズ向けAI機能を実現する方法を説明します。

## はじめに

Model Context Protocol (MCP) は、AIアプリケーションが外部のデータソースやツールに安全に接続できるようにするオープンスタンダードです。Azure AI Foundry と統合することで、MCPはエージェントがさまざまな外部サービス、API、データソースに標準化された方法でアクセスし、操作できるようにします。

この統合により、MCPのツールエコシステムの柔軟性と Azure AI Foundry の堅牢なエージェントフレームワークが組み合わさり、カスタマイズ性の高いエンタープライズ向けAIソリューションを提供します。

**Note:** Azure AI Foundry Agent ServiceでMCPを使用する場合、現在サポートされているリージョンは westus、westus2、uaenorth、southindia、switzerlandnorth のみです。

## 学習目標

このガイドを終える頃には、以下ができるようになります：

- Model Context Protocol の概要と利点を理解する
- Azure AI Foundry エージェントで使用するための MCP サーバーをセットアップする
- MCPツール統合を用いたエージェントの作成と設定
- 実際の MCP サーバーを使った実践的な例の実装
- エージェントの会話におけるツールの応答や引用の取り扱い

## 前提条件

開始する前に、以下を準備してください：

- AI Foundry アクセス権のある Azure サブスクリプション
- Python 3.10以上 または .NET 8.0以上
- Azure CLI のインストールと設定
- AIリソース作成に必要な権限

## Model Context Protocol (MCP) とは？

Model Context Protocol は、AIアプリケーションが外部のデータソースやツールに接続するための標準化された方法です。主な利点は以下の通りです：

- **標準化された統合**：異なるツールやサービス間で一貫したインターフェースを提供
- **セキュリティ**：安全な認証と認可の仕組みを備える
- **柔軟性**：多様なデータソース、API、カスタムツールに対応
- **拡張性**：新しい機能や統合を簡単に追加可能

## Azure AI Foundry での MCP セットアップ

### 環境設定

お好みの開発環境を選択してください：

- [Python 実装](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET 実装](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python 実装

***Note*** この [ノートブック](mcp_support_python.ipynb) を実行できます

### 1. 必要なパッケージのインストール

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. 依存関係のインポート

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP 設定の構成

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. プロジェクトクライアントの初期化

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP ツールの作成

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Python 完全例

```python
with project_client:
    agents_client = project_client.agents

    # Create a new agent with MCP tools
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Create thread for communication
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Create message to thread
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Handle tool approvals and run agent
    mcp_tool.update_headers("SuperSecret", "123456")
    run = agents_client.runs.create(thread_id=thread.id, agent_id=agent.id, tool_resources=mcp_tool.resources)
    print(f"Created run, ID: {run.id}")

    while run.status in ["queued", "in_progress", "requires_action"]:
        time.sleep(1)
        run = agents_client.runs.get(thread_id=thread.id, run_id=run.id)

        if run.status == "requires_action" and isinstance(run.required_action, SubmitToolApprovalAction):
            tool_calls = run.required_action.submit_tool_approval.tool_calls
            if not tool_calls:
                print("No tool calls provided - cancelling run")
                agents_client.runs.cancel(thread_id=thread.id, run_id=run.id)
                break

            tool_approvals = []
            for tool_call in tool_calls:
                if isinstance(tool_call, RequiredMcpToolCall):
                    try:
                        print(f"Approving tool call: {tool_call}")
                        tool_approvals.append(
                            ToolApproval(
                                tool_call_id=tool_call.id,
                                approve=True,
                                headers=mcp_tool.headers,
                            )
                        )
                    except Exception as e:
                        print(f"Error approving tool_call {tool_call.id}: {e}")

            if tool_approvals:
                agents_client.runs.submit_tool_outputs(
                    thread_id=thread.id, run_id=run.id, tool_approvals=tool_approvals
                )

        print(f"Current run status: {run.status}")

    print(f"Run completed with status: {run.status}")

    # Display conversation
    messages = agents_client.messages.list(thread_id=thread.id)
    print("\nConversation:")
    print("-" * 50)
    for msg in messages:
        if msg.text_messages:
            last_text = msg.text_messages[-1]
            print(f"{msg.role.upper()}: {last_text.text.value}")
            print("-" * 50)
```

---

## .NET 実装

***Note*** この [ノートブック](mcp_support_dotnet.ipynb) を実行できます

### 1. 必要なパッケージのインストール

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. 依存関係のインポート

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. 設定の構成

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP ツール定義の作成

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP ツールを使ったエージェントの作成

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. .NET 完全例

```csharp
// Create thread and message
PersistentAgentThread thread = await agentClient.Threads.CreateThreadAsync();

PersistentThreadMessage message = await agentClient.Messages.CreateMessageAsync(
    thread.Id,
    MessageRole.User,
    "What's difference between Azure OpenAI and OpenAI?");

// Configure tool resources with headers
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
ToolResources toolResources = mcpToolResource.ToToolResources();

// Create and handle run
ThreadRun run = await agentClient.Runs.CreateRunAsync(thread, agent, toolResources);

while (run.Status == RunStatus.Queued || run.Status == RunStatus.InProgress || run.Status == RunStatus.RequiresAction)
{
    await Task.Delay(TimeSpan.FromMilliseconds(1000));
    run = await agentClient.Runs.GetRunAsync(thread.Id, run.Id);

    if (run.Status == RunStatus.RequiresAction && run.RequiredAction is SubmitToolApprovalAction toolApprovalAction)
    {
        var toolApprovals = new List<ToolApproval>();
        foreach (var toolCall in toolApprovalAction.SubmitToolApproval.ToolCalls)
        {
            if (toolCall is RequiredMcpToolCall mcpToolCall)
            {
                Console.WriteLine($"Approving MCP tool call: {mcpToolCall.Name}");
                toolApprovals.Add(new ToolApproval(mcpToolCall.Id, approve: true)
                {
                    Headers = { ["SuperSecret"] = "123456" }
                });
            }
        }

        if (toolApprovals.Count > 0)
        {
            run = await agentClient.Runs.SubmitToolOutputsToRunAsync(thread.Id, run.Id, toolApprovals: toolApprovals);
        }
    }
}

// Display messages
using Azure;

AsyncPageable<PersistentThreadMessage> messages = agentClient.Messages.GetMessagesAsync(
    threadId: thread.Id,
    order: ListSortOrder.Ascending
);

await foreach (PersistentThreadMessage threadMessage in messages)
{
    Console.Write($"{threadMessage.CreatedAt:yyyy-MM-dd HH:mm:ss} - {threadMessage.Role,10}: ");
    foreach (MessageContent contentItem in threadMessage.ContentItems)
    {
        if (contentItem is MessageTextContent textItem)
        {
            Console.Write(textItem.Text);
        }
        else if (contentItem is MessageImageFileContent imageFileItem)
        {
            Console.Write($"<image from ID: {imageFileItem.FileId}>");
        }
        Console.WriteLine();
    }
}
```

---

## MCP ツールの設定オプション

エージェント用に MCP ツールを設定する際、いくつかの重要なパラメーターを指定できます：

### Python 設定

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET 設定

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## 認証とヘッダー

両実装とも認証用のカスタムヘッダーをサポートしています：

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## よくある問題のトラブルシューティング

### 1. 接続の問題
- MCPサーバーのURLがアクセス可能か確認する
- 認証情報をチェックする
- ネットワーク接続を確認する

### 2. ツール呼び出しの失敗
- ツールの引数やフォーマットを見直す
- サーバー固有の要件を確認する
- 適切なエラーハンドリングを実装する

### 3. パフォーマンスの問題
- ツール呼び出しの頻度を最適化する
- 適切なキャッシュを導入する
- サーバーの応答時間を監視する

## 次のステップ

MCP統合をさらに強化するために：

1. **カスタム MCP サーバーの構築**：独自のデータソース向けに MCP サーバーを作成する
2. **高度なセキュリティの実装**：OAuth2 やカスタム認証機構を追加する
3. **監視と分析**：ツール使用状況のログ記録と監視を実装する
4. **ソリューションのスケールアップ**：負荷分散や分散型 MCP サーバーアーキテクチャを検討する

## 追加リソース

- [Azure AI Foundry ドキュメント](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol サンプル](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry エージェント概要](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP 仕様](https://spec.modelcontextprotocol.io/)

## サポート

追加のサポートや質問については：
- [Azure AI Foundry ドキュメント](https://learn.microsoft.com/azure/ai-foundry/) をご覧ください
- [MCP コミュニティリソース](https://modelcontextprotocol.io/) を確認してください

## 次に進む

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。