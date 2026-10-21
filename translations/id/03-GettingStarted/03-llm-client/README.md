# Membuat klien dengan LLM

> [!NOTE]
> Contoh klien Java terhubung melalui transport HTTP+SSE legacy dan
> menargetkan MCP `2025-11-25` SDK APIs. Gunakan SDK kompatibel `2026-07-28` dan
> Streamable HTTP untuk klien jarak jauh baru.

Sejauh ini, Anda telah melihat bagaimana membuat server dan klien. Klien telah dapat memanggil server secara eksplisit untuk daftar alat, sumber daya, dan promptnya. Namun, ini bukan pendekatan yang sangat praktis. Pengguna Anda hidup di era agen dan mengharapkan menggunakan prompt dan berkomunikasi dengan LLM sebagai gantinya. Mereka tidak peduli apakah Anda menggunakan MCP untuk menyimpan kemampuan Anda; mereka hanya mengharapkan berinteraksi menggunakan bahasa alami. Jadi bagaimana kita menyelesaikannya? Solusinya adalah menambahkan LLM ke klien.

## Ikhtisar

Dalam pelajaran ini kita fokus menambahkan LLM ke klien Anda dan menunjukkan bagaimana ini memberikan pengalaman yang jauh lebih baik untuk pengguna Anda.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Membuat klien dengan LLM.
- Berinteraksi mulus dengan server MCP menggunakan LLM.
- Memberikan pengalaman pengguna yang lebih baik di sisi klien.

## Pendekatan

Mari kita coba pahami pendekatan yang harus kita ambil. Menambahkan LLM terdengar sederhana, tapi apakah kita benar-benar akan melakukannya?

Berikut cara klien akan berinteraksi dengan server:

1. Menjalin koneksi dengan server.

1. Daftar kemampuan, prompt, sumber daya dan alat, serta simpan skema mereka.

1. Tambahkan LLM dan berikan kemampuan yang disimpan serta skema mereka dalam format yang dimengerti LLM.

1. Tangani prompt pengguna dengan meneruskannya ke LLM bersama dengan alat yang didaftar oleh klien.

Bagus, sekarang kita mengerti bagaimana melakukan ini secara tingkat tinggi, mari kita coba di latihan berikut.

## Latihan: Membuat klien dengan LLM

Dalam latihan ini, kita akan belajar menambahkan LLM ke klien kita.

### Mengkonfigurasi Microsoft Foundry

GitHub Models dihentikan pada 30 Juli 2026. Buat sumber daya Microsoft Foundry,
terapkan model aktif seperti `gpt-5.1`, dan atur variabel lingkungan berikut:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

Gunakan nama deployment dalam panggilan API. Mungkin berbeda dari nama model dasar.
Tinjau
[Jadwal penghentian model Microsoft Foundry](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
sebelum memilih model.

### -1- Sambungkan ke server

Mari buat klien kita terlebih dahulu:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
            }
            );    
    }
}
```

Dalam kode sebelumnya kami telah:

- Mengimpor pustaka yang diperlukan
- Membuat kelas dengan dua anggota, `client` dan `openai` yang akan membantu kita mengelola klien dan berinteraksi dengan LLM masing-masing.
- Mengonfigurasi klien OpenAI untuk menggunakan endpoint Microsoft Foundry v1 dan kunci API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Dalam kode sebelumnya kami telah:

- Mengimpor pustaka yang diperlukan untuk MCP
- Membuat klien

#### .NET

```csharp
using ModelContextProtocol.Client;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
var client = new ChatClient(
    deployment,
    new ApiKeyCredential(apiKey),
    new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

Pertama, Anda perlu menambahkan dependensi LangChain4j ke file `pom.xml` Anda. Tambahkan dependensi ini untuk mengaktifkan integrasi MCP dan API MiniMax kompatibel OpenAI:

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- LangChain4j MCP Integration -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-mcp</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- OpenAI Official API Client -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai-official</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

Masukkan kunci API MiniMax Anda dan, opsional, endpoint dan model.
`MINIMAX_MODEL_ID` mendukung `MiniMax-M3` dan `MiniMax-M2.7`. Jika
`OPENAI_BASE_URL` tidak disetel, `MINIMAX_REGION` mendukung `global_en` dan `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Untuk memilih endpoint berdasarkan wilayah, hilangkan `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Kemudian buat kelas klien Java Anda:

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
                .build();

        // Create MCP transport for connecting to server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Create MCP client
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

Dalam kode sebelumnya kami telah:

- **Menambahkan dependensi LangChain4j**: Diperlukan untuk integrasi MCP dan API MiniMax kompatibel OpenAI
- **Mengimpor pustaka LangChain4j**: Untuk integrasi MCP dan fungsi model chat OpenAI
- **Membuat `ChatLanguageModel`**: Dikondisikan untuk menggunakan MiniMax dengan kunci API, endpoint, dan ID model yang didukung
- **Mengatur transport HTTP**: Menggunakan Server-Sent Events (SSE) untuk menghubungkan ke server MCP
- **Membuat klien MCP**: Yang akan menangani komunikasi dengan server
- **Menggunakan dukungan MCP bawaan LangChain4j**: Yang menyederhanakan integrasi antara LLM dan server MCP

#### Rust

Contoh ini mengasumsikan Anda memiliki server MCP berbasis Rust yang berjalan. Jika belum, lihat kembali pelajaran [01-first-server](../01-first-server/README.md) untuk membuat server.

Setelah memiliki server MCP Rust, buka terminal dan navigasikan ke direktori yang sama dengan server. Lalu jalankan perintah berikut untuk membuat proyek klien LLM baru:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Tambahkan dependensi berikut ke file `Cargo.toml` Anda:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Tidak ada pustaka Rust resmi untuk OpenAI, namun crate `async-openai` adalah [pustaka yang dipelihara komunitas](https://platform.openai.com/docs/libraries/rust#rust) yang umum digunakan.

Buka file `src/main.rs` dan ganti isinya dengan kode berikut:

```rust
use async_openai::{Client, config::OpenAIConfig};
use rmcp::{
    RmcpError,
    model::{CallToolRequestParam, ListToolsResult},
    service::{RoleClient, RunningService, ServiceExt},
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use serde_json::{Value, json};
use std::error::Error;
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Initial message
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Setup Microsoft Foundry client
    let endpoint = std::env::var("AZURE_OPENAI_ENDPOINT")?;
    let api_key = std::env::var("AZURE_OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base(format!("{}/openai/v1", endpoint.trim_end_matches('/')))
            .with_api_key(api_key),
    );

    // Setup MCP client
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("calculator-server");

    let mcp_client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: Get MCP tool listing 

    // TODO: LLM conversation with tool calls

    Ok(())
}
```

Kode ini menyiapkan aplikasi Rust yang terhubung ke server MCP dan
deployment model Microsoft Foundry untuk interaksi LLM.

> [!IMPORTANT]
> Atur `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, dan
> `AZURE_OPENAI_DEPLOYMENT` sebelum menjalankan aplikasi.

Bagus, langkah berikutnya, mari kita daftar kemampuan server.

### -2- Daftar kemampuan server

Sekarang kita akan terhubung ke server dan menanyakan kemampuannya:

#### Typescript

Dalam kelas yang sama, tambahkan metode berikut:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // listing tools
    const toolsResult = await this.client.listTools();
}
```

Dalam kode sebelumnya kami telah:

- Menambahkan kode untuk menghubungkan ke server, `connectToServer`.
- Membuat metode `run` yang bertanggung jawab menangani aliran aplikasi kami. Sejauh ini hanya mendaftar alat tetapi kami akan menambahkan lebih banyak segera.

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Berikut yang kita tambahkan:

- Mendaftar sumber daya dan alat serta mencetaknya. Untuk alat kami juga mendaftar `inputSchema` yang akan kita gunakan nanti.

#### .NET

```csharp
async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        // TODO: convert tool definition from MCP tool to LLm tool     
    }

    return toolDefinitions;
}
```

Dalam kode sebelumnya kami telah:

- Mendaftar alat yang tersedia di Server MCP
- Untuk setiap alat, daftarkan nama, deskripsi dan skema. Yang terakhir adalah sesuatu yang akan kita gunakan untuk memanggil alat sebentar lagi.

#### Java

```java
// Create a tool provider that automatically discovers MCP tools
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// The MCP tool provider automatically handles:
// - Listing available tools from the MCP server
// - Converting MCP tool schemas to LangChain4j format
// - Managing tool execution and responses
```

Dalam kode sebelumnya kami telah:

- Membuat `McpToolProvider` yang otomatis menemukan dan mendaftarkan semua alat dari server MCP
- Penyedia alat menangani konversi antara skema alat MCP dan format alat LangChain4j secara internal
- Pendekatan ini mengabstraksi proses daftar dan konversi alat manual

#### Rust

Mengambil alat dari server MCP dilakukan menggunakan metode `list_tools`. Dalam fungsi `main` Anda, setelah menyiapkan klien MCP, tambahkan kode berikut:

```rust
// Get MCP tool listing 
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konversi kemampuan server menjadi alat LLM

Langkah berikutnya setelah mendaftar kemampuan server adalah mengonversinya ke format yang dipahami LLM. Setelah itu, kita dapat menyediakan kemampuan ini sebagai alat ke LLM kita.

#### TypeScript

1. Tambahkan kode berikut untuk mengonversi respons dari server MCP ke format alat yang dapat digunakan LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Create a zod schema based on the input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Explicitly set type to "function"
            function: {
            name: tool.name,
            description: tool.description,
            parameters: {
            type: "object",
            properties: tool.input_schema.properties,
            required: tool.input_schema.required,
            },
            },
        };
    }

    ```

    Kode di atas mengambil respons dari server MCP dan mengonversinya ke format definisi alat yang dapat dipahami LLM.

2. Mari perbarui metode `run` berikut untuk mendaftar kemampuan server:

    ```typescript
    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
            });
        });
    }
    ```

    Dalam kode sebelumnya, kita memperbarui metode `run` untuk memetakan hasil dan untuk setiap entri memanggil `openAiToolAdapter`.

#### Python

1. Pertama, mari buat fungsi konverter berikut

    ```python
    def convert_to_llm_tool(tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }

        return tool_schema
    ```

    Dalam fungsi `convert_to_llm_tools` di atas kita mengambil respons alat MCP dan mengonversinya ke format yang dipahami LLM.

2. Selanjutnya, mari perbarui kode klien kita untuk memanfaatkan fungsi ini seperti berikut:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Di sini, kita menambahkan panggilan ke `convert_to_llm_tool` untuk mengonversi respons alat MCP menjadi sesuatu yang bisa kita beri ke LLM nanti.

#### .NET

1. Mari tambahkan kode untuk mengonversi respons alat MCP menjadi sesuatu yang dapat dimengerti LLM

```csharp
ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}
```

Dalam kode sebelumnya kami telah:

- Membuat fungsi `ConvertFrom` yang mengambil nama, deskripsi dan skema input.
- Membuat objek OpenAI `ChatTool` dari skema JSON alat MCP.

2. Mari lihat bagaimana kita dapat memperbarui kode yang ada untuk memanfaatkan fungsi di atas:

    ```csharp
    async Task<List<ChatTool>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatTool> toolDefinitions = [];

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);
        }

        return toolDefinitions;
    }
    ```
    
Dalam kode sebelumnya, kami:

- Memperbarui fungsi untuk mengonversi respons alat MCP menjadi alat LLM. Mari soroti kode yang kami tambahkan:

   ```csharp
   JsonElement propertiesElement;
   tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

   var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
   Console.WriteLine($"Tool definition: {def}");
   toolDefinitions.Add(def);
   ```

Skema input adalah bagian dari respons alat namun pada atribut "properties", jadi kita harus ekstrak. Selanjutnya, kita sekarang memanggil `ConvertFrom` dengan detail alat. Sekarang kita telah menyelesaikan pekerjaan berat, mari kita lihat bagaimana panggilan berlangsung saat kita menangani prompt pengguna selanjutnya.

#### Java

```java
// Create a Bot interface for natural language interaction
public interface Bot {
    String chat(String prompt);
}

// Configure the AI service with LLM and MCP tools
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Dalam kode sebelumnya kami telah:

- Mendefinisikan antarmuka `Bot` sederhana untuk interaksi bahasa alami
- Menggunakan `AiServices` LangChain4j untuk mengikat otomatis LLM dengan penyedia alat MCP
- Kerangka menangani otomatis konversi skema alat dan pemanggilan fungsi secara latar belakang
- Pendekatan ini menghilangkan konversi alat manual - LangChain4j menangani semua kompleksitas konversi alat MCP ke format kompatibel LLM

#### Rust

Untuk mengonversi respons alat MCP ke format yang dapat dipahami LLM, kita akan menambahkan fungsi pembantu yang memformat daftar alat. Tambahkan kode berikut ke file `main.rs` Anda di bawah fungsi `main`. Ini akan dipanggil saat membuat permintaan ke LLM:

```rust
async fn format_tools(tools: &ListToolsResult) -> Result<Vec<Value>, Box<dyn Error>> {
    let tools_json = serde_json::to_value(tools)?;
    let Some(tools_array) = tools_json.get("tools").and_then(|t| t.as_array()) else {
        return Ok(vec![]);
    };

    let formatted_tools = tools_array
        .iter()
        .filter_map(|tool| {
            let name = tool.get("name")?.as_str()?;
            let description = tool.get("description")?.as_str()?;
            let schema = tool.get("inputSchema")?;

            Some(json!({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": schema.get("properties").unwrap_or(&json!({})),
                        "required": schema.get("required").unwrap_or(&json!([]))
                    }
                }
            }))
        })
        .collect();

    Ok(formatted_tools)
}
```

Bagus, kita sudah siap menangani permintaan pengguna, mari kita selesaikan itu selanjutnya.

### -4- Menangani permintaan prompt pengguna

Pada bagian kode ini, kita akan menangani permintaan pengguna.

#### TypeScript

1. Tambahkan metode yang akan digunakan untuk memanggil LLM kita:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  

        }
    }
    ```

    Dalam kode sebelumnya kita:

    - Menambahkan metode `callTools`.
    - Metode ini mengambil respons LLM dan memeriksa alat apa yang telah dipanggil, jika ada:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // call tool
        }
        ```

    - Memanggil alat, jika LLM menunjukkan harus dipanggil:

        ```typescript
        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  
        ```

2. Perbarui metode `run` untuk menyertakan panggilan ke LLM dan pemanggilan `callTools`:

    ```typescript

    // 1. Create messages that's input for the LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Calling the LLM
    let response = this.openai.chat.completions.create({
        model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
        max_completion_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Go through the LLM response,for each choice, check if it has tool calls 
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Bagus, mari daftar kode lengkapnya:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
            }
            );    
    }

    async connectToServer(transport: Transport) {
        await this.client.connect(transport);
        this.run();
        console.error("MCPClient started on stdin/stdout");
    }

    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
          }) {
          // Create a zod schema based on the input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Explicitly set type to "function"
            function: {
              name: tool.name,
              description: tool.description,
              parameters: {
              type: "object",
              properties: tool.input_schema.properties,
              required: tool.input_schema.required,
              },
            },
          };
    }
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. Call the server's tool 
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Do something with the result
          // TODO  
    
         }
    }

    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
              name: tool.name,
              description: tool.description,
              input_schema: tool.inputSchema,
            });
        });

        const prompt = "What is the sum of 2 and 3?";
    
        const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

        console.log("Querying LLM: ", messages[0].content);
        let response = this.openai.chat.completions.create({
            model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
            max_completion_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. Go through the LLM response, for each choice, check if it has tool calls 
        (await response).choices.map(async (choice: { message: any; }) => {
          const message = choice.message;
          if (message.tool_calls) {
              console.log("Making tool call")
              await this.callTools(message.tool_calls, results);
          }
        });
    }
    
}

let client = new MyClient();
 const transport = new StdioClientTransport({
            command: "node",
            args: ["./build/index.js"]
        });

client.connectToServer(transport);
```

#### Python

1. Mari tambahkan beberapa impor yang dibutuhkan untuk memanggil LLM

    ```python
    # llm
    import os
    from openai import OpenAI
    import json
    ```

2. Selanjutnya, tambahkan fungsi yang akan memanggil LLM. Contoh ini menggunakan
    model aktif `gpt-5.1`. Tinjau
    [Jadwal penghentian model Microsoft Foundry](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
    saat memilih model untuk aplikasi Anda.

    ```python
    # llm

    def call_llm(prompt, functions):
        client = OpenAI(
            base_url=(
                f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/"
            ),
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )

        print("CALLING LLM")
        response = client.chat.completions.create(
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant.",
                },
                {
                "role": "user",
                "content": prompt,
                },
            ],
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"),
            tools=functions,
            max_completion_tokens=1000,
        )

        response_message = response.choices[0].message
        
        functions_to_call = []

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                print("TOOL: ", tool_call)
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                functions_to_call.append({ "name": name, "args": args })

        return functions_to_call
    ```

    Dalam kode sebelumnya kami telah:

    - Memberikan fungsi kami, yang kami temukan di server MCP dan konversi, ke LLM.
    - Kemudian memanggil LLM dengan fungsi tersebut.
    - Kemudian, kami memeriksa hasil untuk melihat fungsi apa yang harus kami panggil, jika ada.
    - Akhirnya, kami melewatkan array fungsi untuk dipanggil.

3. Langkah terakhir, mari perbarui kode utama kita:

    ```python
    prompt = "Add 2 to 20"

    # ask LLM what tools to all, if any
    functions_to_call = call_llm(prompt, functions)

    # call suggested functions
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Itu dia, langkah terakhir, pada kode di atas kita:

    - Memanggil alat MCP via `call_tool` menggunakan fungsi yang dipilih LLM berdasarkan prompt kita.
    - Mencetak hasil panggilan alat ke Server MCP.

#### .NET

1. Mari tunjukkan kode untuk melakukan permintaan prompt LLM:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new UserChatMessage(userMessage));


    // 2. Define options, including the tools
    var options = new ChatCompletionOptions
    {
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
    var content = response.Content.FirstOrDefault()?.Text;

    ```

    Dalam kode sebelumnya kami telah:

    - Mengambil alat dari server MCP, `var tools = await GetMcpTools()`.
    - Mendefinisikan prompt pengguna `userMessage`.
    - Membuat objek opsi yang menentukan model dan alat.
    - Membuat permintaan ke LLM.

2. Satu langkah terakhir, mari kita lihat apakah LLM berpikir kita harus memanggil fungsi:

    ```csharp
    // 4. Check if the response contains a function call
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
        var result = await mcpClient.CallToolAsync(
            call.FunctionName,
            dict!,
            cancellationToken: CancellationToken.None
        );

        var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
        if (textBlock != null)
        {
            Console.WriteLine(textBlock.Text);
        }

    }
    ```

    Dalam kode sebelumnya kami telah:

    - Melakukan pengulangan melalui daftar panggilan fungsi.
    - Untuk setiap panggilan alat, mengurai nama dan argumen serta memanggil alat tersebut di server MCP menggunakan klien MCP. Akhirnya, kami mencetak hasilnya.

Berikut kode secara lengkap:

```csharp
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
if (string.IsNullOrWhiteSpace(endpoint) || string.IsNullOrWhiteSpace(apiKey))
{
    Console.WriteLine("Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY.");
    return;
}

var client = new ChatClient(
    model: deployment,
    credential: new ApiKeyCredential(apiKey),
    options: new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });
var chatHistory = new List<ChatMessage>
{
    new SystemChatMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}

async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
    }

    return toolDefinitions;
}

// 1. List tools on mcp server

var tools = await GetMcpTools();
for (int i = 0; i < tools.Count; i++)
{
    var tool = tools[i];
    Console.WriteLine($"MCP Tools def: {i}: {tool}");
}

// 2. Define the chat history and the user message
var userMessage = "add 2 and 4";

chatHistory.Add(new UserChatMessage(userMessage));

// 3. Define options, including the tools
var options = new ChatCompletionOptions
{
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
var content = response.Content.FirstOrDefault()?.Text;

// 5. Check if the response contains a function call
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
    var result = await mcpClient.CallToolAsync(
        call.FunctionName,
        dict!,
        cancellationToken: CancellationToken.None
    );

    var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
    if (textBlock != null)
    {
        Console.WriteLine(textBlock.Text);
    }

}

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Execute natural language requests that automatically use MCP tools
    String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
    System.out.println(response);

    response = bot.chat("What's the square root of 144?");
    System.out.println(response);

    response = bot.chat("Show me the help for the calculator service");
    System.out.println(response);
} finally {
    mcpClient.close();
}
```

Dalam kode sebelumnya kami telah:

- Menggunakan prompt bahasa alami sederhana untuk berinteraksi dengan alat server MCP
- Kerangka LangChain4j secara otomatis menangani:
  - Mengonversi prompt pengguna menjadi panggilan alat saat dibutuhkan
  - Memanggil alat MCP yang sesuai berdasarkan keputusan LLM
  - Mengelola alur percakapan antara LLM dan server MCP
- Metode `bot.chat()` mengembalikan respons bahasa alami yang mungkin termasuk hasil dari eksekusi alat MCP
- Pendekatan ini memberikan pengalaman pengguna yang mulus di mana pengguna tidak perlu mengetahui implementasi MCP yang mendasarinya

Contoh kode lengkap:

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
                .build();

        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        Bot bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();

        try {
            String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
            System.out.println(response);

            response = bot.chat("What's the square root of 144?");
            System.out.println(response);

            response = bot.chat("Show me the help for the calculator service");
            System.out.println(response);
        } finally {
            mcpClient.close();
        }
    }

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

#### Rust

Di sinilah sebagian besar pekerjaan terjadi. Kami akan memanggil LLM dengan prompt awal dari pengguna, lalu memproses respons untuk melihat apakah ada alat yang perlu dipanggil. Jika ya, kami akan memanggil alat-alat tersebut dan melanjutkan percakapan dengan LLM sampai tidak ada panggilan alat lagi yang dibutuhkan dan kami memiliki respons akhir.

Kami akan melakukan beberapa panggilan ke LLM, jadi mari kita definisikan fungsi yang akan menangani panggilan LLM. Tambahkan fungsi berikut ke file `main.rs` Anda:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let model = std::env::var("AZURE_OPENAI_DEPLOYMENT")
        .unwrap_or_else(|_| "gpt-5.1".to_string());
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": model,
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

Fungsi ini mengambil klien LLM, daftar pesan (termasuk prompt pengguna), alat dari server MCP, dan mengirim permintaan ke LLM, mengembalikan respons.

Respons dari LLM akan berisi array `choices`. Kami perlu memproses hasilnya untuk melihat apakah ada `tool_calls` yang hadir. Ini memberitahu kita bahwa LLM meminta alat tertentu harus dipanggil dengan argumen. Tambahkan kode berikut ke bagian bawah file `main.rs` Anda untuk mendefinisikan fungsi yang menangani respons LLM:

```rust
async fn process_llm_response(
    llm_response: &Value,
    mcp_client: &RunningService<RoleClient, ()>,
    openai_client: &Client<OpenAIConfig>,
    mcp_tools: &ListToolsResult,
    messages: &mut Vec<Value>,
) -> Result<(), Box<dyn Error>> {
    let Some(message) = llm_response
        .get("choices")
        .and_then(|c| c.as_array())
        .and_then(|choices| choices.first())
        .and_then(|choice| choice.get("message"))
    else {
        return Ok(());
    };

    // Print content if available
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Handle tool calls
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Add assistant message

        // Execute each tool call
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Add tool result to messages
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continue conversation with tool results
        let response = call_llm(openai_client, messages, mcp_tools).await?;
        Box::pin(process_llm_response(
            &response,
            mcp_client,
            openai_client,
            mcp_tools,
            messages,
        ))
        .await?;
    }
    Ok(())
}
```

Jika `tool_calls` ada, ia mengekstrak informasi alat, memanggil server MCP dengan permintaan alat, dan menambahkan hasil ke pesan percakapan. Kemudian melanjutkan percakapan dengan LLM dan pesan diperbarui dengan respons asisten dan hasil panggilan alat.

Untuk mengekstrak informasi panggilan alat yang LLM kembalikan untuk panggilan MCP, kami akan menambahkan fungsi bantu lain untuk mengekstrak semua yang diperlukan untuk melakukan panggilan. Tambahkan kode berikut ke bagian bawah file `main.rs` Anda:

```rust
fn extract_tool_call_info(tool_call: &Value) -> Result<(String, String, String), Box<dyn Error>> {
    let tool_id = tool_call
        .get("id")
        .and_then(|id| id.as_str())
        .unwrap_or("")
        .to_string();
    let function = tool_call.get("function").ok_or("Missing function")?;
    let name = function
        .get("name")
        .and_then(|n| n.as_str())
        .unwrap_or("")
        .to_string();
    let args = function
        .get("arguments")
        .and_then(|a| a.as_str())
        .unwrap_or("{}")
        .to_string();
    Ok((tool_id, name, args))
}
```

Dengan semua bagian lengkap, sekarang kita bisa menangani prompt awal pengguna dan memanggil LLM. Perbarui fungsi `main` Anda untuk menyertakan kode berikut:

```rust
// LLM conversation with tool calls
let response = call_llm(&openai_client, &messages, &tools).await?;
process_llm_response(
    &response,
    &mcp_client,
    &openai_client,
    &tools,
    &mut messages,
)
.await?;
```

Ini akan meminta LLM dengan prompt awal pengguna yang menanyakan jumlah dari dua angka, dan akan memproses respons untuk menangani panggilan alat secara dinamis.

Bagus, Anda berhasil!

## Tugas

Ambil kode dari latihan dan bangun server dengan beberapa alat tambahan. Kemudian buat klien dengan LLM, seperti di latihan, dan uji dengan berbagai prompt untuk memastikan semua alat server Anda dipanggil secara dinamis. Cara membangun klien ini berarti pengguna akhir akan memiliki pengalaman pengguna yang hebat karena mereka dapat menggunakan prompt, bukan perintah klien yang tepat, dan tidak menyadari ada server MCP yang dipanggil.

## Solusi

[Solusi](./solution/README.md)

## Poin Penting

- Menambahkan LLM ke klien Anda memberikan cara yang lebih baik bagi pengguna untuk berinteraksi dengan Server MCP.
- Anda perlu mengonversi respons Server MCP menjadi sesuatu yang dapat dimengerti oleh LLM.

## Sampel

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Sumber Tambahan

## Selanjutnya

- Selanjutnya: [Mengonsumsi server menggunakan Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->