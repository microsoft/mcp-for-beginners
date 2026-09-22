# Model Context Protocol (MCP) と Microsoft Foundry の統合

このガイドでは、Model Context Protocol (MCP) サーバーを Microsoft Foundry エージェントと統合し、強力なツールオーケストレーションおよびエンタープライズ AI 機能を実現する方法を説明します。

## はじめに

Model Context Protocol (MCP) は、AI アプリケーションが外部データソースやツールに安全に接続できるようにするオープン標準です。Microsoft Foundry と統合することで、MCP はエージェントがさまざまな外部サービス、API、およびデータソースに標準化された方法でアクセスし、対話することを可能にします。

この統合により、MCP のツールエコシステムの柔軟性と Microsoft Foundry の堅牢なエージェントフレームワークが結合され、幅広いカスタマイズ機能を持つエンタープライズグレードの AI ソリューションが提供されます。

> **注意:** Microsoft Foundry Agent Service で MCP を使用したい場合、現在サポートされているリージョンは westus、westus2、uaenorth、southindia、および switzerlandnorth のみです。

## 学習目標

このガイドの終了時には、以下ができるようになります：

- Model Context Protocol とその利点を理解する
- Microsoft Foundry エージェントで使用するための MCP サーバーをセットアップする
- MCP ツール統合を行ったエージェントを作成および設定する
- 実際の MCP サーバーを使用した実用例を実装する
- エージェントとの対話でのツールの応答および引用を適切に処理する

## 前提条件

開始する前に、以下を確認してください：

- Microsoft Foundry へのアクセス権を持つ Azure サブスクリプション
- Python 3.10+ または .NET 8.0+
- Azure CLI がインストールされ設定済みであること
- AI リソースを作成するための適切な権限

## Model Context Protocol (MCP) とは？

Model Context Protocol は、AI アプリケーションが外部データソースやツールに接続するための標準化された方法です。主な利点は以下の通りです：

- <strong>標準化された統合</strong>：異なるツールやサービス間で一貫したインターフェース
- <strong>セキュリティ</strong>：安全な認証および承認機構
- <strong>柔軟性</strong>：様々なデータソース、API、カスタムツールをサポート
- <strong>拡張性</strong>：新機能や統合の追加が容易

## Microsoft Foundry における MCP のセットアップ

### 環境設定

お好みの開発環境を選択してください：

- [Python 実装](#python-実装)
- [.NET 実装](#codeblock5)

---

## Python 実装

***Note*** この [ノートブック](./mcp_support_python.ipynb) を実行できます

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
    allowed_tools=[],  # オプション: 使用可能なツールを指定してください
)
```

### 6. 完成した Python 例

```python
with project_client:
    agents_client = project_client.agents

    # MCPツールを使って新しいエージェントを作成する
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # 通信のためのスレッドを作成する
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # スレッドにメッセージを作成する
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # ツールの承認を処理し、エージェントを実行する
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

    # 会話を表示する
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

***Note*** この [ノートブック](./mcp_support_dotnet.ipynb) を実行できます

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

### 5. MCP ツール付きエージェントの作成

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. 完成した .NET 例

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

## MCP ツール設定オプション

エージェント用の MCP ツールを設定する際には、いくつかの重要なパラメーターを指定できます：

### Python 設定

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCPサーバーの識別子
    server_url="https://api.example.com/mcp", # MCPサーバーのエンドポイント
    allowed_tools=[],                       # オプション: 許可されたツールを指定する
)
```

### .NET 設定

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## 認証およびヘッダー

両実装は認証のためにカスタムヘッダーをサポートしています：

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
- MCP サーバーの URL がアクセス可能か確認
- 認証情報を確認
- ネットワーク接続を確保

### 2. ツール呼び出しの失敗
- ツールの引数やフォーマットを見直す
- サーバー固有の要件をチェック
- 適切なエラー処理を実装

### 3. パフォーマンスの問題
- ツール呼び出し頻度を最適化
- キャッシュを適切に実装
- サーバーの応答時間を監視

## 次のステップ

MCP 統合をさらに強化するには：

1. **カスタム MCP サーバーの探求**：独自のデータソース向け MCP サーバーを構築
2. <strong>高度なセキュリティの実装</strong>：OAuth2 やカスタム認証機構を追加
3. <strong>監視と分析</strong>：ツール使用のログおよび監視を実装
4. <strong>ソリューションのスケール</strong>：負荷分散や分散 MCP サーバーアーキテクチャを検討

## 追加リソース

- [Microsoft Foundry ドキュメント](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol サンプル](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry エージェント概要](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP 仕様](https://spec.modelcontextprotocol.io/)

## サポート

追加サポートや質問については：
- [Microsoft Foundry ドキュメント](https://learn.microsoft.com/azure/ai-foundry/) を参照
- [MCP コミュニティリソース](https://modelcontextprotocol.io/) を確認

## 次へ 

- [5.14 MCP コンテキストエンジニアリング](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
