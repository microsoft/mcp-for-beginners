# Model Context Protocol (MCP)와 Azure AI Foundry 통합

이 가이드는 Model Context Protocol (MCP) 서버를 Azure AI Foundry 에이전트와 통합하여 강력한 도구 오케스트레이션과 엔터프라이즈 AI 기능을 구현하는 방법을 보여줍니다.

## 소개

Model Context Protocol (MCP)은 AI 애플리케이션이 외부 데이터 소스와 도구에 안전하게 연결할 수 있도록 하는 오픈 표준입니다. Azure AI Foundry와 통합하면 MCP를 통해 에이전트가 다양한 외부 서비스, API 및 데이터 소스에 표준화된 방식으로 접근하고 상호작용할 수 있습니다.

이 통합은 MCP의 도구 생태계의 유연성과 Azure AI Foundry의 견고한 에이전트 프레임워크를 결합하여 광범위한 맞춤화가 가능한 엔터프라이즈급 AI 솔루션을 제공합니다.

**Note:** Azure AI Foundry Agent Service에서 MCP를 사용하려면 현재 다음 지역만 지원됩니다: westus, westus2, uaenorth, southindia, switzerlandnorth

## 학습 목표

이 가이드를 완료하면 다음을 할 수 있습니다:

- Model Context Protocol과 그 이점 이해하기
- Azure AI Foundry 에이전트와 함께 사용할 MCP 서버 설정하기
- MCP 도구 통합으로 에이전트 생성 및 구성하기
- 실제 MCP 서버를 활용한 실용적인 예제 구현하기
- 에이전트 대화에서 도구 응답과 인용 처리하기

## 사전 준비 사항

시작하기 전에 다음을 준비하세요:

- AI Foundry에 액세스할 수 있는 Azure 구독
- Python 3.10 이상 또는 .NET 8.0 이상
- 설치 및 구성된 Azure CLI
- AI 리소스 생성 권한

## Model Context Protocol (MCP)란?

Model Context Protocol은 AI 애플리케이션이 외부 데이터 소스와 도구에 연결할 수 있도록 표준화된 방법입니다. 주요 이점은 다음과 같습니다:

- **표준화된 통합**: 다양한 도구와 서비스에 일관된 인터페이스 제공
- **보안**: 안전한 인증 및 권한 부여 메커니즘
- **유연성**: 다양한 데이터 소스, API, 맞춤형 도구 지원
- **확장성**: 새로운 기능과 통합을 쉽게 추가 가능

## Azure AI Foundry와 MCP 설정하기

### 환경 구성

선호하는 개발 환경을 선택하세요:

- [Python 구현](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET 구현](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python 구현

***Note*** 이 [노트북](mcp_support_python.ipynb)을 실행할 수 있습니다

### 1. 필요한 패키지 설치

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. 의존성 가져오기

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP 설정 구성

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. 프로젝트 클라이언트 초기화

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP 도구 생성

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. 완성된 Python 예제

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

## .NET 구현

***Note*** 이 [노트북](mcp_support_dotnet.ipynb)을 실행할 수 있습니다

### 1. 필요한 패키지 설치

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. 의존성 가져오기

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. 설정 구성

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP 도구 정의 생성

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP 도구를 포함한 에이전트 생성

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. 완성된 .NET 예제

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

## MCP 도구 구성 옵션

에이전트용 MCP 도구를 구성할 때 다음과 같은 중요한 매개변수를 지정할 수 있습니다:

### Python 구성

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET 구성

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## 인증 및 헤더

두 구현 모두 인증을 위한 맞춤 헤더를 지원합니다:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## 자주 발생하는 문제 해결

### 1. 연결 문제
- MCP 서버 URL이 접근 가능한지 확인하세요
- 인증 자격 증명을 점검하세요
- 네트워크 연결 상태를 확인하세요

### 2. 도구 호출 실패
- 도구 인수와 형식을 검토하세요
- 서버별 요구사항을 확인하세요
- 적절한 오류 처리를 구현하세요

### 3. 성능 문제
- 도구 호출 빈도를 최적화하세요
- 적절한 캐싱을 적용하세요
- 서버 응답 시간을 모니터링하세요

## 다음 단계

MCP 통합을 더욱 향상시키려면:

1. **맞춤 MCP 서버 탐색**: 독자적인 데이터 소스를 위한 MCP 서버 구축
2. **고급 보안 구현**: OAuth2 또는 맞춤 인증 메커니즘 추가
3. **모니터링 및 분석**: 도구 사용에 대한 로깅 및 모니터링 구현
4. **솔루션 확장**: 부하 분산 및 분산 MCP 서버 아키텍처 고려

## 추가 자료

- [Azure AI Foundry 문서](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol 샘플](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry 에이전트 개요](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP 사양](https://spec.modelcontextprotocol.io/)

## 지원

추가 지원 및 문의 사항은 다음을 참고하세요:
- [Azure AI Foundry 문서](https://learn.microsoft.com/azure/ai-foundry/)
- [MCP 커뮤니티 자료](https://modelcontextprotocol.io/)

## 다음 내용

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.