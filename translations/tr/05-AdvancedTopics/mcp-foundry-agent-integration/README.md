# Model Context Protocol (MCP) Entegrasyonu Azure AI Foundry ile

Bu rehber, Model Context Protocol (MCP) sunucularını Azure AI Foundry ajanlarıyla nasıl entegre edeceğinizi gösterir; böylece güçlü araç orkestrasyonu ve kurumsal yapay zeka yetenekleri sağlanır.

## Giriş

Model Context Protocol (MCP), yapay zeka uygulamalarının dış veri kaynakları ve araçlara güvenli bir şekilde bağlanmasını sağlayan açık bir standarttır. Azure AI Foundry ile entegre edildiğinde, MCP ajanların çeşitli dış hizmetlere, API’lere ve veri kaynaklarına standart bir şekilde erişip etkileşimde bulunmasına olanak tanır.

Bu entegrasyon, MCP’nin araç ekosisteminin esnekliğini Azure AI Foundry’nin sağlam ajan çerçevesiyle birleştirerek, kapsamlı özelleştirme imkanları sunan kurumsal düzeyde yapay zeka çözümleri sağlar.

**Not:** MCP’yi Azure AI Foundry Agent Service içinde kullanmak isterseniz, şu anda yalnızca şu bölgeler desteklenmektedir: westus, westus2, uaenorth, southindia ve switzerlandnorth

## Öğrenme Hedefleri

Bu rehberin sonunda şunları yapabileceksiniz:

- Model Context Protocol’ü ve faydalarını anlamak
- Azure AI Foundry ajanlarıyla kullanmak üzere MCP sunucularını kurmak
- MCP araç entegrasyonlu ajanlar oluşturup yapılandırmak
- Gerçek MCP sunucuları kullanarak pratik örnekler uygulamak
- Ajan konuşmalarında araç yanıtları ve atıfları yönetmek

## Ön Koşullar

Başlamadan önce şunlara sahip olduğunuzdan emin olun:

- AI Foundry erişimi olan bir Azure aboneliği
- Python 3.10+ veya .NET 8.0+
- Azure CLI yüklü ve yapılandırılmış
- AI kaynakları oluşturmak için uygun izinler

## Model Context Protocol (MCP) Nedir?

Model Context Protocol, yapay zeka uygulamalarının dış veri kaynakları ve araçlara bağlanması için standart bir yöntemdir. Temel faydaları şunlardır:

- **Standartlaştırılmış Entegrasyon**: Farklı araçlar ve hizmetler arasında tutarlı arayüz
- **Güvenlik**: Güvenli kimlik doğrulama ve yetkilendirme mekanizmaları
- **Esneklik**: Çeşitli veri kaynakları, API’ler ve özel araçları destekler
- **Genişletilebilirlik**: Yeni yetenekler ve entegrasyonlar kolayca eklenebilir

## Azure AI Foundry ile MCP Kurulumu

### Ortam Yapılandırması

Tercih ettiğiniz geliştirme ortamını seçin:

- [Python Uygulaması](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Uygulaması](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Uygulaması

***Not*** Bu [notebook’u](mcp_support_python.ipynb) çalıştırabilirsiniz

### 1. Gerekli Paketleri Yükleyin

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Bağımlılıkları İçe Aktarın

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP Ayarlarını Yapılandırın

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Proje İstemcisini Başlatın

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP Aracını Oluşturun

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Tam Python Örneği

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

## .NET Uygulaması

***Not*** Bu [notebook’u](mcp_support_dotnet.ipynb) çalıştırabilirsiniz

### 1. Gerekli Paketleri Yükleyin

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Bağımlılıkları İçe Aktarın

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Ayarları Yapılandırın

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP Araç Tanımını Oluşturun

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP Araçlarıyla Ajan Oluşturun

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Tam .NET Örneği

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

## MCP Araç Yapılandırma Seçenekleri

Ajanınız için MCP araçlarını yapılandırırken birkaç önemli parametre belirtebilirsiniz:

### Python Yapılandırması

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET Yapılandırması

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Kimlik Doğrulama ve Başlıklar

Her iki uygulama da kimlik doğrulama için özel başlıkları destekler:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Yaygın Sorun Giderme

### 1. Bağlantı Sorunları
- MCP sunucu URL’sinin erişilebilir olduğunu doğrulayın
- Kimlik doğrulama bilgilerini kontrol edin
- Ağ bağlantısını sağlayın

### 2. Araç Çağrısı Hataları
- Araç argümanları ve biçimlendirmesini gözden geçirin
- Sunucuya özgü gereksinimleri kontrol edin
- Doğru hata yönetimi uygulayın

### 3. Performans Sorunları
- Araç çağrı sıklığını optimize edin
- Uygun yerlerde önbellekleme yapın
- Sunucu yanıt sürelerini izleyin

## Sonraki Adımlar

MCP entegrasyonunuzu daha da geliştirmek için:

1. **Özel MCP Sunucuları Keşfedin**: Kendi MCP sunucularınızı kurarak özel veri kaynakları oluşturun
2. **Gelişmiş Güvenlik Uygulayın**: OAuth2 veya özel kimlik doğrulama mekanizmaları ekleyin
3. **İzleme ve Analitik**: Araç kullanımını kaydetme ve izleme sistemleri kurun
4. **Çözümünüzü Ölçeklendirin**: Yük dengeleme ve dağıtık MCP sunucu mimarilerini değerlendirin

## Ek Kaynaklar

- [Azure AI Foundry Dokümantasyonu](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Örnekleri](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Ajanları Genel Bakış](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Spesifikasyonu](https://spec.modelcontextprotocol.io/)

## Destek

Ek destek ve sorular için:
- [Azure AI Foundry dokümantasyonunu](https://learn.microsoft.com/azure/ai-foundry/) inceleyin
- [MCP topluluk kaynaklarını](https://modelcontextprotocol.io/) kontrol edin

## Sonraki Konu

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.