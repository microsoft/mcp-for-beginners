# Integrasi Model Context Protocol (MCP) dengan Microsoft Foundry

Panduan ini menunjukkan cara mengintegrasikan pelayan Model Context Protocol (MCP) dengan ejen Microsoft Foundry, membolehkan orkestrasi alat yang berkuasa dan keupayaan AI perusahaan.

## Pengenalan

Model Context Protocol (MCP) ialah piawaian terbuka yang membolehkan aplikasi AI berhubung dengan selamat ke sumber data dan alat luaran. Apabila diintegrasikan dengan Microsoft Foundry, MCP membolehkan ejen mengakses dan berinteraksi dengan pelbagai perkhidmatan, API, dan sumber data luaran secara berstandard.

Integrasi ini menggabungkan fleksibiliti ekosistem alat MCP dengan rangka kerja ejen Microsoft Foundry yang mantap, menyediakan penyelesaian AI bertaraf perusahaan dengan keupayaan penyesuaian yang meluas.

**Nota:** Jika anda ingin menggunakan MCP dalam Perkhidmatan Ejen Microsoft Foundry, buat masa ini hanya wilayah berikut disokong: westus, westus2, uaenorth, southindia dan switzerlandnorth

## Objektif Pembelajaran

Menjelang tamat panduan ini, anda akan dapat:

- Memahami Model Context Protocol dan manfaatnya
- Menyediakan pelayan MCP untuk digunakan dengan ejen Microsoft Foundry
- Membuat dan mengkonfigurasi ejen dengan integrasi alat MCP
- Melaksanakan contoh praktikal menggunakan pelayan MCP sebenar
- Mengendalikan tindak balas alat dan rujukan dalam perbualan ejen

## Prasyarat

Sebelum bermula, pastikan anda mempunyai:

- Langganan Azure dengan akses Microsoft Foundry
- Python 3.10+ atau .NET 8.0+
- Azure CLI yang dipasang dan dikonfigurasi
- Kebenaran yang sesuai untuk mencipta sumber AI

## Apa itu Model Context Protocol (MCP)?

Model Context Protocol ialah cara berstandard bagi aplikasi AI untuk berhubung ke sumber data dan alat luaran. Manfaat utama termasuk:

- **Integrasi Berstandard**: Antara muka konsisten merentasi pelbagai alat dan perkhidmatan
- **Keselamatan**: Mekanisme pengesahan dan kebenaran yang selamat
- **Fleksibiliti**: Sokongan untuk pelbagai sumber data, API, dan alat tersuai
- **Keterluasan**: Mudah untuk menambah keupayaan dan integrasi baru

## Menyediakan MCP dengan Microsoft Foundry

### Konfigurasi Persekitaran

Pilih persekitaran pembangunan pilihan anda:

- [Implementasi Python](#implementasi-python)
- [Implementasi .NET](#codeblock5)

---

## Implementasi Python

***Nota*** Anda boleh menjalankan [notebook](./mcp_support_python.ipynb) ini

### 1. Pasang Pek Perlu

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Import Kebergantungan

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfigurasi Tetapan MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inisialisasi Klien Projek

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Cipta Alat MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Pilihan: nyatakan alat yang dibenarkan
)
```

### 6. Contoh Python Lengkap

```python
with project_client:
    agents_client = project_client.agents

    # Cipta ejen baru dengan alat MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Cipta benang untuk komunikasi
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Cipta mesej ke benang
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Urus kelulusan alat dan jalankan ejen
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

    # Paparkan perbualan
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

## Implementasi .NET

***Nota*** Anda boleh menjalankan [notebook](./mcp_support_dotnet.ipynb) ini

### 1. Pasang Pek Perlu

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Import Kebergantungan

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigurasi Tetapan

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Cipta Definisi Alat MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Cipta Ejen dengan Alat MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Contoh .NET Lengkap

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

## Pilihan Konfigurasi Alat MCP

Apabila mengkonfigurasi alat MCP untuk ejen anda, anda boleh menentukan beberapa parameter penting:

### Konfigurasi Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Pengecam untuk pelayan MCP
    server_url="https://api.example.com/mcp", # Titik akhir pelayan MCP
    allowed_tools=[],                       # Pilihan: nyatakan alat yang dibenarkan
)
```

### Konfigurasi .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Pengesahan dan Tajuk

Kedua-dua implementasi menyokong tajuk tersuai untuk pengesahan:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Menyelesaikan Isu Biasa

### 1. Isu Sambungan
- Sahkan URL pelayan MCP boleh diakses
- Semak kelayakan pengesahan
- Pastikan sambungan rangkaian

### 2. Kegagalan Panggilan Alat
- Semak argumen dan format alat
- Semak keperluan khusus pelayan
- Laksanakan pengendalian ralat yang betul

### 3. Isu Prestasi
- Optimumkan kekerapan panggilan alat
- Laksanakan caching jika sesuai
- Pantau masa respons pelayan

## Langkah Seterusnya

Untuk lebih meningkatkan integrasi MCP anda:

1. **Terokai Pelayan MCP Tersuai**: Bina pelayan MCP anda sendiri untuk sumber data proprietari
2. **Laksanakan Keselamatan Lanjutan**: Tambah OAuth2 atau mekanisme pengesahan tersuai
3. **Pantauan dan Analitik**: Laksanakan pencatatan dan pemantauan untuk penggunaan alat
4. **Skalakan Penyelesaian Anda**: Pertimbangkan pengimbangan beban dan seni bina pelayan MCP teragih

## Sumber Tambahan

- [Dokumentasi Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Contoh Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Gambaran Keseluruhan Ejen Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Spesifikasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Sokongan

Untuk sokongan dan pertanyaan tambahan:
- Semak [dokumentasi Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Periksa [sumber komuniti MCP](https://modelcontextprotocol.io/)

## Apa Seterusnya

- [5.14 Kejuruteraan Konteks MCP](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->