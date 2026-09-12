# Integrasi Model Context Protocol (MCP) dengan Microsoft Foundry

Panduan ini menunjukkan cara mengintegrasikan server Model Context Protocol (MCP) dengan agen Microsoft Foundry, memungkinkan orkestrasi alat yang kuat dan kemampuan AI tingkat perusahaan.

## Pendahuluan

Model Context Protocol (MCP) adalah standar terbuka yang memungkinkan aplikasi AI untuk terhubung secara aman ke sumber data dan alat eksternal. Saat diintegrasikan dengan Microsoft Foundry, MCP memungkinkan agen untuk mengakses dan berinteraksi dengan berbagai layanan, API, dan sumber data eksternal secara standar.

Integrasi ini menggabungkan fleksibilitas ekosistem alat MCP dengan kerangka kerja agen Microsoft Foundry yang kuat, menyediakan solusi AI tingkat perusahaan dengan kemampuan kustomisasi yang luas.

**Catatan:** Jika Anda ingin menggunakan MCP di Layanan Agen Microsoft Foundry, saat ini hanya wilayah berikut yang didukung: westus, westus2, uaenorth, southindia, dan switzerlandnorth

## Tujuan Pembelajaran

Pada akhir panduan ini, Anda akan mampu:

- Memahami Model Context Protocol dan manfaatnya
- Menyiapkan server MCP untuk digunakan dengan agen Microsoft Foundry
- Membuat dan mengkonfigurasi agen dengan integrasi alat MCP
- Menerapkan contoh praktis menggunakan server MCP nyata
- Menangani respons alat dan sitasi dalam percakapan agen

## Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- Langganan Azure dengan akses Microsoft Foundry
- Python 3.10+ atau .NET 8.0+
- Azure CLI terpasang dan terkonfigurasi
- Izin yang sesuai untuk membuat sumber daya AI

## Apa itu Model Context Protocol (MCP)?

Model Context Protocol adalah cara standar bagi aplikasi AI untuk terhubung ke sumber data dan alat eksternal. Manfaat utamanya meliputi:

- **Integrasi Standar**: Antarmuka yang konsisten di berbagai alat dan layanan
- **Keamanan**: Mekanisme otentikasi dan otorisasi yang aman
- **Fleksibilitas**: Dukungan untuk berbagai sumber data, API, dan alat kustom
- **Ekstensibilitas**: Mudah menambah kemampuan dan integrasi baru

## Menyiapkan MCP dengan Microsoft Foundry

### Konfigurasi Lingkungan

Pilih lingkungan pengembangan pilihan Anda:

- [Implementasi Python](#implementasi-python)
- [Implementasi .NET](#codeblock5)

---

## Implementasi Python

***Catatan*** Anda dapat menjalankan [notebook](./mcp_support_python.ipynb) ini

### 1. Pasang Paket yang Dibutuhkan

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Impor Dependensi

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfigurasi Pengaturan MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inisialisasi Klien Proyek

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Buat Alat MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Opsional: tentukan alat yang diperbolehkan
)
```

### 6. Contoh Lengkap Python

```python
with project_client:
    agents_client = project_client.agents

    # Buat agen baru dengan alat MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Buat thread untuk komunikasi
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Buat pesan ke thread
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Tangani persetujuan alat dan jalankan agen
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

    # Tampilkan percakapan
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

***Catatan*** Anda dapat menjalankan [notebook](./mcp_support_dotnet.ipynb) ini

### 1. Pasang Paket yang Dibutuhkan

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Impor Dependensi

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigurasi Pengaturan

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Buat Definisi Alat MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Buat Agen dengan Alat MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Contoh Lengkap .NET

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

## Opsi Konfigurasi Alat MCP

Saat mengkonfigurasi alat MCP untuk agen Anda, Anda bisa menentukan beberapa parameter penting:

### Konfigurasi Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Pengidentifikasi untuk server MCP
    server_url="https://api.example.com/mcp", # Titik akhir server MCP
    allowed_tools=[],                       # Opsional: tentukan alat yang diizinkan
)
```

### Konfigurasi .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Otentikasi dan Header

Kedua implementasi mendukung header kustom untuk otentikasi:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Pemecahan Masalah Umum

### 1. Masalah Koneksi
- Verifikasi URL server MCP dapat diakses
- Periksa kredensial otentikasi
- Pastikan konektivitas jaringan

### 2. Kegagalan Panggilan Alat
- Tinjau argumen alat dan formatnya
- Periksa persyaratan spesifik server
- Terapkan penanganan kesalahan yang tepat

### 3. Masalah Kinerja
- Optimalkan frekuensi panggilan alat
- Terapkan caching jika sesuai
- Pantau waktu respons server

## Langkah Berikutnya

Untuk meningkatkan integrasi MCP Anda lebih lanjut:

1. **Jelajahi Server MCP Kustom**: Bangun server MCP Anda sendiri untuk sumber data kepemilikan
2. **Terapkan Keamanan Lanjutan**: Tambahkan mekanisme otentikasi OAuth2 atau kustom
3. **Pantau dan Analitik**: Terapkan logging dan pemantauan untuk penggunaan alat
4. **Skalakan Solusi Anda**: Pertimbangkan load balancing dan arsitektur server MCP terdistribusi

## Sumber Daya Tambahan

- [Dokumentasi Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Contoh Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Overview Agen Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Spesifikasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Dukungan

Untuk dukungan dan pertanyaan tambahan:
- Tinjau [dokumentasi Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Periksa [sumber daya komunitas MCP](https://modelcontextprotocol.io/)

## Apa Berikutnya

- [5.14 Rekayasa Konteks MCP](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->