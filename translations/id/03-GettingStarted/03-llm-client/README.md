# Membuat klien dengan LLM

Sejauh ini, Anda telah melihat bagaimana membuat server dan klien. Klien telah dapat memanggil server secara eksplisit untuk mendaftar alat, sumber daya, dan prompt-nya. Namun, ini bukan pendekatan yang sangat praktis. Pengguna Anda hidup di era agentik dan mengharapkan menggunakan prompt serta berkomunikasi dengan LLM sebagai gantinya. Mereka tidak peduli apakah Anda menggunakan MCP untuk menyimpan kapabilitas Anda; mereka cukup mengharapkan interaksi menggunakan bahasa alami. Jadi, bagaimana kita menyelesaikannya? Solusinya adalah menambahkan LLM ke klien.

## Ikhtisar

Dalam pelajaran ini kami fokus menambahkan LLM untuk klien Anda dan menunjukkan bagaimana ini memberikan pengalaman yang jauh lebih baik bagi pengguna Anda.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Membuat klien dengan LLM.
- Berinteraksi dengan mulus dengan server MCP menggunakan LLM.
- Memberikan pengalaman pengguna akhir yang lebih baik di sisi klien.

## Pendekatan

Mari kita coba pahami pendekatan yang harus kita ambil. Menambahkan LLM terdengar sederhana, tetapi apakah kita benar-benar akan melakukannya?

Berikut cara klien akan berinteraksi dengan server:

1. Membuat koneksi dengan server.

1. Mendaftar kapabilitas, prompt, sumber daya dan alat, dan menyimpan skema mereka.

1. Menambahkan LLM dan melewatkan kapabilitas yang tersimpan dan skema mereka dalam format yang bisa dipahami LLM.

1. Menangani prompt pengguna dengan meneruskannya ke LLM bersama alat yang terdaftar oleh klien.

Bagus, sekarang kita paham bagaimana kita bisa melakukan ini secara garis besar, mari kita coba dalam latihan di bawah ini.

## Latihan: Membuat klien dengan LLM

Dalam latihan ini, kita akan belajar menambahkan LLM ke klien kita.

### Autentikasi menggunakan GitHub Personal Access Token

Membuat token GitHub adalah proses yang mudah. Berikut cara melakukannya:

- Pergi ke Pengaturan GitHub – Klik gambar profil Anda di pojok kanan atas dan pilih Settings.
- Navigasi ke Developer Settings – Gulir ke bawah dan klik Developer Settings.
- Pilih Personal Access Tokens – Klik Fine-grained tokens lalu Generate new token.
- Konfigurasikan Token Anda – Tambahkan catatan untuk referensi, atur tanggal kadaluarsa, dan pilih cakupan yang diperlukan (izin). Dalam kasus ini pastikan menambahkan izin Models.
- Buat dan Salin Token – Klik Generate token, dan pastikan untuk menyalinnya segera, karena Anda tidak akan bisa melihatnya lagi.

### -1- Terhubung ke server

Mari kita buat klien kita terlebih dahulu:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Impor zod untuk validasi skema

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", 
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }
}
```

Dalam kode sebelumnya kami telah:

- Mengimpor perpustakaan yang dibutuhkan
- Membuat kelas dengan dua anggota, `client` dan `openai` yang akan membantu kita mengelola klien dan berinteraksi dengan LLM masing-masing.
- Mengkonfigurasi instance LLM kita untuk menggunakan GitHub Models dengan mengatur `baseUrl` mengarah ke API inferensi.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Buat parameter server untuk koneksi stdio
server_params = StdioServerParameters(
    command="mcp",  # Dapat dieksekusi
    args=["run", "server.py"],  # Argumen baris perintah opsional
    env=None,  # Variabel lingkungan opsional
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inisialisasi koneksi
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Dalam kode sebelumnya kami telah:

- Mengimpor perpustakaan yang dibutuhkan untuk MCP
- Membuat klien

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

Pertama, Anda perlu menambahkan dependency LangChain4j ke file `pom.xml` Anda. Tambahkan dependency ini untuk mengaktifkan integrasi MCP dan API MiniMax yang kompatibel dengan OpenAI:

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

Atur kunci API MiniMax Anda dan, opsional, endpoint serta model.
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

        // Buat transport MCP untuk menghubungkan ke server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Buat klien MCP
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

- **Menambahkan dependency LangChain4j**: Diperlukan untuk integrasi MCP dan API MiniMax yang kompatibel dengan OpenAI
- **Mengimpor perpustakaan LangChain4j**: Untuk integrasi MCP dan fungsi model chat OpenAI
- **Membuat `ChatLanguageModel`**: Dikonfigurasi untuk menggunakan MiniMax dengan kunci API MiniMax Anda, endpoint, dan ID model yang didukung
- **Mengatur transport HTTP**: Menggunakan Server-Sent Events (SSE) untuk menghubungkan ke server MCP
- **Membuat klien MCP**: Yang akan menangani komunikasi dengan server
- **Menggunakan dukungan MCP bawaan LangChain4j**: Yang menyederhanakan integrasi antara LLM dan server MCP

#### Rust

Contoh ini mengasumsikan Anda memiliki server MCP berbasis Rust yang berjalan. Jika Anda tidak memilikinya, lihat kembali pelajaran [01-first-server](../01-first-server/README.md) untuk membuat server.

Setelah Anda memiliki server MCP Rust, buka terminal dan navigasikan ke direktori yang sama dengan server. Kemudian jalankan perintah berikut untuk membuat proyek klien LLM baru:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Tambahkan dependency berikut ke file `Cargo.toml` Anda:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Tidak ada perpustakaan resmi Rust untuk OpenAI, namun crate `async-openai` adalah [perpustakaan yang dipelihara oleh komunitas](https://platform.openai.com/docs/libraries/rust#rust) yang umum digunakan.

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
    // Pesan awal
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Siapkan klien OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Siapkan klien MCP
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

    // TODO: Dapatkan daftar alat MCP

    // TODO: Percakapan LLM dengan panggilan alat

    Ok(())
}
```

Kode ini menyiapkan aplikasi Rust dasar yang akan terhubung ke server MCP dan GitHub Models untuk interaksi LLM.

> [!IMPORTANT]
> Pastikan untuk mengatur variabel lingkungan `OPENAI_API_KEY` dengan token GitHub Anda sebelum menjalankan aplikasi.

Bagus, untuk langkah berikutnya, mari kita daftar kapabilitas pada server.

### -2- Daftar kapabilitas server

Sekarang kita akan terhubung ke server dan meminta kapabilitasnya:

#### Typescript

Di kelas yang sama, tambahkan metode berikut:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // alat pencantuman
    const toolsResult = await this.client.listTools();
}
```

Dalam kode sebelumnya kami telah:

- Menambahkan kode untuk menghubungkan ke server, `connectToServer`.
- Membuat metode `run` yang bertanggung jawab untuk menangani alur aplikasi kami. Sejauh ini hanya mendaftar alat tapi kami akan menambahkan lebih banyak sesaat lagi.

#### Python

```python
# Daftar sumber daya yang tersedia
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Daftar alat yang tersedia
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Berikut yang kami tambahkan:

- Mendaftar sumber daya dan alat lalu mencetaknya. Untuk alat, kami juga mendaftar `inputSchema` yang kami gunakan nanti.

#### .NET

```csharp
async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

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
- Untuk setiap alat, mendaftar nama, deskripsi dan skema-nya. Ini adalah sesuatu yang akan kita gunakan untuk memanggil alat nanti.

#### Java

```java
// Buat penyedia alat yang secara otomatis menemukan alat MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Penyedia alat MCP secara otomatis menangani:
// - Mendaftar alat yang tersedia dari server MCP
// - Mengonversi skema alat MCP ke format LangChain4j
// - Mengelola eksekusi alat dan tanggapan
```

Dalam kode sebelumnya kami telah:

- Membuat `McpToolProvider` yang otomatis menemukan dan mendaftarkan semua alat dari server MCP
- Penyedia alat mengurus konversi antara skema alat MCP dan format alat LangChain4j secara internal
- Pendekatan ini menyederhanakan proses listing alat dan konversi manual

#### Rust

Mengambil alat dari server MCP dilakukan menggunakan metode `list_tools`. Di fungsi `main` Anda, setelah menyiapkan klien MCP, tambahkan kode berikut:

```rust
// Dapatkan daftar alat MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konversi kapabilitas server ke alat LLM

Langkah berikutnya setelah mendaftar kapabilitas server adalah mengonversinya ke format yang dimengerti LLM. Setelah itu, kita bisa menyediakan kapabilitas ini sebagai alat untuk LLM kita.

#### TypeScript

1. Tambahkan kode berikut untuk mengonversi respons dari Server MCP ke format alat yang LLM bisa gunakan:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Buat skema zod berdasarkan input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Secara eksplisit atur tipe menjadi "function"
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

    Kode di atas mengambil respons dari Server MCP dan mengonversinya ke format definisi alat yang dimengerti LLM.

2. Selanjutnya kita update metode `run` untuk mendaftar kapabilitas server:

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

    Dalam kode sebelumnya, kita update metode `run` untuk memetakan hasil dan untuk setiap entri memanggil `openAiToolAdapter`.

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

    Dalam fungsi `convert_to_llm_tools` di atas kita mengambil respons alat MCP dan mengonversinya ke format yang bisa dimengerti LLM.

2. Selanjutnya, update kode klien kita untuk memanfaatkan fungsi ini seperti berikut:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Di sini, kita menambahkan panggilan ke `convert_to_llm_tool` untuk mengonversi respons alat MCP ke sesuatu yang bisa kita beri ke LLM nanti.

#### .NET

1. Mari tambahkan kode untuk mengonversi respons alat MCP ke sesuatu yang bisa dimengerti LLM

```csharp
ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}
```

Dalam kode sebelumnya kami telah:

- Membuat fungsi `ConvertFrom` yang menerima nama, deskripsi, dan skema input.
- Mendefinisikan fungsi yang membuat FunctionDefinition yang diteruskan ke ChatCompletionsDefinition. Ini adalah sesuatu yang dimengerti LLM.

2. Mari lihat bagaimana kita bisa update kode yang ada untuk memanfaatkan fungsi di atas:

    ```csharp
    async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            JsonElement propertiesElement;
            tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

            var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);

            Console.WriteLine($"Properties: {propertiesElement}");        
        }

        return toolDefinitions;
    }
    ```    In the preceding code, we've:

    - Update the function to convert the MCP tool response to an LLm tool. Let's highlight the code we added:

        ```csharp
        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
        ```

        The input schema is part of the tool response but on the "properties" attribute, so we need to extract. Furthermore, we now call `ConvertFrom` with the tool details. Now we've done the heavy lifting, let's see how it call comes together as we handle a user prompt next.

#### Java

```java
// Buat antarmuka Bot untuk interaksi bahasa alami
public interface Bot {
    String chat(String prompt);
}

// Konfigurasikan layanan AI dengan alat LLM dan MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Dalam kode sebelumnya kami telah:

- Mendefinisikan interface `Bot` sederhana untuk interaksi bahasa alami
- Menggunakan `AiServices` LangChain4j untuk mengikat LLM dengan penyedia alat MCP secara otomatis
- Framework secara otomatis mengurus konversi skema alat dan pemanggilan fungsi di belakang layar
- Pendekatan ini menghilangkan konversi alat manual - LangChain4j menangani semua kompleksitas mengonversi alat MCP ke format yang kompatibel dengan LLM

#### Rust

Untuk mengonversi respons alat MCP ke format yang bisa dimengerti LLM, kita akan menambahkan fungsi bantu yang memformat daftar alat. Tambahkan kode berikut ke file `main.rs` Anda di bawah fungsi `main`. Ini akan dipanggil saat membuat permintaan ke LLM:

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

Bagus, kita sudah siap menangani permintaan pengguna, jadi mari lanjutkan itu berikutnya.

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


        // 2. Panggil alat server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Lakukan sesuatu dengan hasilnya
        // TODO

        }
    }
    ```

    Dalam kode sebelumnya kami:

    - Menambahkan metode `callTools`.
    - Metode tersebut mengambil respons LLM dan memeriksa alat apa yang dipanggil, jika ada:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // panggil alat
        }
        ```

    - Memanggil alat, jika LLM menunjukkan perlu dipanggil:

        ```typescript
        // 2. Panggil alat server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Lakukan sesuatu dengan hasilnya
        // TODO
        ```

2. Update metode `run` untuk menyertakan panggilan ke LLM dan memanggil `callTools`:

    ```typescript

    // 1. Buat pesan yang menjadi input untuk LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Memanggil LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Periksa respons LLM, untuk setiap pilihan, periksa apakah ada pemanggilan alat
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Bagus, mari kita lihat kode lengkapnya:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Impor zod untuk validasi skema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // mungkin perlu mengubah ke url ini di masa depan: https://models.github.ai/inference
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
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
          // Buat skema zod berdasarkan input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Tetapkan tipe secara eksplisit ke "function"
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
    
    
          // 2. Panggil alat server
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Lakukan sesuatu dengan hasilnya
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. Periksa respons LLM, untuk setiap pilihan, periksa apakah ada panggilan alat
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

1. Mari kita tambahkan beberapa impor yang diperlukan untuk memanggil LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Selanjutnya, tambahkan fungsi yang akan memanggil LLM:

    ```python
    # llm

    def call_llm(prompt, functions):
        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.inference.ai.azure.com"

        model_name = "gpt-4o"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        print("CALLING LLM")
        response = client.complete(
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
            model=model_name,
            tools = functions,
            # Parameter opsional
            temperature=1.,
            max_tokens=1000,
            top_p=1.    
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

    Dalam kode sebelumnya kami:

    - Melewatkan fungsi yang kami temukan di server MCP dan dikonversi ke LLM.
    - Lalu memanggil LLM dengan fungsi tersebut.
    - Memeriksa hasil untuk melihat fungsi apa yang harus dipanggil, jika ada.
    - Akhirnya, melewatkan array fungsi yang akan dipanggil.

3. Langkah terakhir, mari update kode utama kita:

    ```python
    prompt = "Add 2 to 20"

    # tanyakan LLM alat apa yang tersedia, jika ada
    functions_to_call = call_llm(prompt, functions)

    # panggil fungsi yang disarankan
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Nah, itu langkah terakhir, dalam kode di atas kami:

    - Memanggil alat MCP melalui `call_tool` menggunakan fungsi yang LLM anggap harus dipanggil berdasar prompt kita.
    - Mencetak hasil pemanggilan alat ke Server MCP.

#### .NET

1. Mari kita lihat kode untuk melakukan permintaan prompt LLM:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new ChatRequestUserMessage(userMessage));

    // 1. Define tools
    ChatCompletionsToolDefinition def = CreateToolDefinition();


    // 2. Define options, including the tools
    var options = new ChatCompletionsOptions(chatHistory)
    {
        Model = "gpt-4.1-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    Dalam kode sebelumnya kami:

    - Mengambil alat dari server MCP, `var tools = await GetMcpTools()`.
    - Mendefinisikan prompt pengguna `userMessage`.
    - Membuat objek opsi yang menentukan model dan alat.
    - Membuat permintaan ke LLM.

2. Satu langkah lagi, mari lihat jika LLM pikir kita harus memanggil fungsi:

    ```csharp
    // 4. Check if the response contains a function call
    ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
        var result = await mcpClient.CallToolAsync(
            call.Name,
            dict!,
            cancellationToken: CancellationToken.None
        );

        Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

    }
    ```

    Dalam kode sebelumnya kami:

    - Melakukan loop melalui daftar panggilan fungsi.
    - Untuk setiap panggilan alat, ambil nama dan argumen dan panggil alat di server MCP menggunakan klien MCP. Akhirnya cetak hasilnya.

Berikut kode lengkapnya:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;

var endpoint = "https://models.inference.ai.azure.com";
var token = Environment.GetEnvironmentVariable("GITHUB_TOKEN"); // Your GitHub Access Token
var client = new ChatCompletionsClient(new Uri(endpoint), new AzureKeyCredential(token));
var chatHistory = new List<ChatRequestMessage>
{
    new ChatRequestSystemMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}



async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);

        Console.WriteLine($"Properties: {propertiesElement}");        
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

chatHistory.Add(new ChatRequestUserMessage(userMessage));


// 3. Define options, including the tools
var options = new ChatCompletionsOptions(chatHistory)
{
    Model = "gpt-4.1-mini",
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletions? response = await client.CompleteAsync(options);
var content = response.Content;

// 5. Check if the response contains a function call
ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
    var result = await mcpClient.CallToolAsync(
        call.Name,
        dict!,
        cancellationToken: CancellationToken.None
    );

    Console.WriteLine(result.Content.OfType<TextContentBlock>().First().Text);

}

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Jalankan permintaan bahasa alami yang secara otomatis menggunakan alat MCP
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

Dalam kode sebelumnya kami:

- Menggunakan prompt bahasa alami sederhana untuk berinteraksi dengan alat server MCP
- Framework LangChain4j menangani secara otomatis:
  - Mengkonversi prompt pengguna menjadi panggilan alat saat dibutuhkan
  - Memanggil alat MCP yang sesuai berdasarkan keputusan LLM
  - Mengelola alur percakapan antara LLM dan server MCP
- Metode `bot.chat()` mengembalikan respons bahasa alami yang dapat mencakup hasil dari eksekusi alat MCP
- Pendekatan ini memberikan pengalaman pengguna mulus dimana pengguna tidak perlu tahu tentang implementasi MCP yang mendasarinya

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

Di sinilah sebagian besar kerja terjadi. Kita akan memanggil LLM dengan prompt pengguna awal, kemudian memproses respons untuk melihat apakah ada alat yang perlu dipanggil. Jika iya, kita akan memanggil alat-alat itu dan melanjutkan percakapan dengan LLM sampai tidak ada lagi panggilan alat yang diperlukan dan kita mendapatkan respons akhir.


Kami akan melakukan beberapa panggilan ke LLM, jadi mari kita definisikan sebuah fungsi yang akan menangani panggilan LLM. Tambahkan fungsi berikut ke berkas `main.rs` Anda:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": "openai/gpt-4.1",
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

Fungsi ini menerima klien LLM, daftar pesan (termasuk prompt pengguna), alat dari server MCP, dan mengirimkan permintaan ke LLM, mengembalikan responsnya.

Respons dari LLM akan berisi array `choices`. Kita perlu memproses hasilnya untuk melihat apakah ada `tool_calls`. Ini memberi tahu kita bahwa LLM meminta alat tertentu untuk dipanggil dengan argumen. Tambahkan kode berikut di bagian bawah berkas `main.rs` Anda untuk mendefinisikan fungsi yang menangani respons LLM:

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

    // Cetak konten jika tersedia
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Tangani panggilan alat
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Tambahkan pesan asisten

        // Jalankan setiap panggilan alat
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Tambahkan hasil alat ke pesan
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Lanjutkan percakapan dengan hasil alat
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

Jika `tool_calls` ada, fungsi akan mengekstrak informasi alat, memanggil server MCP dengan permintaan alat tersebut, dan menambahkan hasilnya ke pesan percakapan. Kemudian melanjutkan percakapan dengan LLM dan pesan diperbarui dengan respons asisten dan hasil panggilan alat.

Untuk mengekstrak informasi panggilan alat yang dikembalikan LLM untuk panggilan MCP, kita akan menambahkan fungsi pembantu lain untuk mengekstrak semua yang dibutuhkan agar panggilan dapat dilakukan. Tambahkan kode berikut di bagian bawah berkas `main.rs` Anda:

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

Dengan semua bagian lengkap, sekarang kita dapat menangani prompt awal pengguna dan memanggil LLM. Perbarui fungsi `main` Anda untuk menyertakan kode berikut:

```rust
// Percakapan LLM dengan panggilan alat
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

Ini akan mengajukan pertanyaan ke LLM dengan prompt awal pengguna yang meminta jumlah dari dua angka, dan akan memproses respons untuk secara dinamis menangani panggilan alat.

Hebat, Anda berhasil!

## Tugas

Ambil kode dari latihan ini dan bangun server dengan beberapa alat tambahan. Kemudian buat klien dengan LLM, seperti di latihan, dan uji dengan berbagai prompt untuk memastikan semua alat server Anda dapat dipanggil secara dinamis. Cara membangun klien seperti ini memberikan pengalaman pengguna yang hebat karena pengguna dapat menggunakan prompt, bukan perintah klien yang tepat, dan tidak menyadari adanya pemanggilan server MCP.

## Solusi

[Solusi](./solution/README.md)

## Poin-Poin Penting

- Menambahkan LLM ke klien Anda memberikan cara yang lebih baik bagi pengguna untuk berinteraksi dengan Server MCP.
- Anda perlu mengonversi respons Server MCP menjadi sesuatu yang dapat dipahami LLM.

## Contoh

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)
- [Kalkulator Rust](../../../../03-GettingStarted/samples/rust)

## Sumber Tambahan

## Selanjutnya

- Selanjutnya: [Mengonsumsi server menggunakan Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->