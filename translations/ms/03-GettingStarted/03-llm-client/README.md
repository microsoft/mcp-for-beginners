# Mewujudkan klien dengan LLM

Sejauh ini, anda telah melihat bagaimana untuk mewujudkan pelayan dan klien. Klien telah dapat memanggil pelayan secara eksplisit untuk menyenaraikan alat, sumber, dan arahan. Walau bagaimanapun, ini bukan pendekatan yang sangat praktikal. Pengguna anda hidup dalam era agen dan mengharapkan untuk menggunakan arahan dan berkomunikasi dengan LLM sebaliknya. Mereka tidak kisah sama ada anda menggunakan MCP untuk menyimpan keupayaan anda; mereka hanya mengharapkan untuk berinteraksi menggunakan bahasa semula jadi. Jadi, bagaimana kita menyelesaikan ini? Penyelesaiannya adalah dengan menambah LLM ke klien.

## Gambaran Keseluruhan

Dalam pelajaran ini kita fokus pada menambah LLM untuk klien anda dan menunjukkan bagaimana ini memberikan pengalaman yang jauh lebih baik untuk pengguna anda.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Mewujudkan klien dengan sebuah LLM.
- Berinteraksi lancar dengan pelayan MCP menggunakan LLM.
- Memberikan pengalaman pengguna akhir yang lebih baik di sisi klien.

## Pendekatan

Mari cuba memahami pendekatan yang perlu diambil. Menambah LLM kedengaran mudah, tetapi adakah kita benar-benar akan melakukannya?

Berikut ialah bagaimana klien akan berinteraksi dengan pelayan:

1. Menjalin sambungan dengan pelayan.

1. Menyenaraikan keupayaan, arahan, sumber dan alat, dan menyimpan skema mereka.

1. Menambah LLM dan mempassing keupayaan yang disimpan serta skema mereka dalam format yang difahami oleh LLM.

1. Mengendalikan arahan pengguna dengan mempassingnya kepada LLM bersama dengan alat yang disenaraikan oleh klien.

Bagus, kini kita faham bagaimana kita boleh melakukan ini secara umum, mari cuba ini dalam latihan di bawah.

## Latihan: Mewujudkan klien dengan LLM

Dalam latihan ini, kita akan belajar untuk menambah LLM ke klien kita.

### Pengesahan menggunakan Token Akses Peribadi GitHub

Membuat token GitHub adalah proses yang mudah. Berikut adalah cara anda boleh melakukannya:

- Pergi ke Tetapan GitHub – Klik pada gambar profil anda di sudut kanan atas dan pilih Tetapan.
- Navigasi ke Tetapan Pembangun – Skrol ke bawah dan klik pada Tetapan Pembangun.
- Pilih Token Akses Peribadi – Klik pada token berbutir halus dan kemudian Jana token baru.
- Konfigurasikan Token Anda – Tambah nota sebagai rujukan, tetapkan tarikh luput, dan pilih skop yang diperlukan (kebenaran). Dalam kes ini pastikan menambah kebenaran Model.
- Jana dan Salin Token – Klik Jana token, dan pastikan anda menyalinnya serta-merta, kerana anda tidak dapat melihatnya semula.

### -1- Sambungkan ke pelayan

Mari kita cipta klien kita dahulu:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod untuk pengesahan skema

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

Dalam kod sebelumnya kita telah:

- Mengimport perpustakaan yang diperlukan
- Mewujudkan kelas dengan dua anggota, `client` dan `openai` yang akan membantu kita menguruskan klien dan berinteraksi dengan LLM masing-masing.
- Mengkonfigurasikan instans LLM kita untuk menggunakan Model GitHub dengan menetapkan `baseUrl` ke API inferens.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Cipta parameter pelayan untuk sambungan stdio
server_params = StdioServerParameters(
    command="mcp",  # Boleh laksana
    args=["run", "server.py"],  # Argumen baris perintah pilihan
    env=None,  # Pembolehubah persekitaran pilihan
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inisialisasi sambungan
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Dalam kod sebelumnya kita telah:

- Mengimport perpustakaan yang diperlukan untuk MCP
- Mewujudkan klien

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

Mula-mula, anda perlu menambah kebergantungan LangChain4j ke fail `pom.xml` anda. Tambah kebergantungan ini untuk mengaktifkan integrasi MCP dan API MiniMax yang serasi dengan OpenAI:

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

Tetapkan kunci API MiniMax anda dan, jika mahu, titik akhir dan model.
`MINIMAX_MODEL_ID` menyokong `MiniMax-M3` dan `MiniMax-M2.7`. Jika
`OPENAI_BASE_URL` tidak ditetapkan, `MINIMAX_REGION` menyokong `global_en` dan `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Untuk memilih titik akhir mengikut wilayah sebaliknya, hilangkan `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Kemudian cipta kelas klien Java anda:

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

        // Cipta pengangkutan MCP untuk menyambung ke pelayan
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Cipta klien MCP
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

Dalam kod sebelumnya kita telah:

- **Menambah kebergantungan LangChain4j**: Diperlukan untuk integrasi MCP dan API MiniMax yang serasi dengan OpenAI
- **Mengimport perpustakaan LangChain4j**: Untuk integrasi MCP dan fungsi model perbualan OpenAI
- **Mewujudkan `ChatLanguageModel`**: Dikonfigurasikan untuk menggunakan MiniMax dengan kunci API MiniMax anda, titik akhir, dan ID model yang disokong
- **Menyediakan pengangkutan HTTP**: Menggunakan Server-Sent Events (SSE) untuk sambung ke pelayan MCP
- **Mewujudkan klien MCP**: Yang akan mengendalikan komunikasi dengan pelayan
- **Menggunakan sokongan MCP terbina dalam LangChain4j**: Yang memudahkan pengintegrasian antara LLM dan pelayan MCP

#### Rust

Contoh ini mengandaikan anda mempunyai pelayan MCP berasaskan Rust yang berjalan. Jika anda tiada, rujuk kembali pelajaran [01-first-server](../01-first-server/README.md) untuk mencipta pelayan.

Setelah anda mempunyai pelayan MCP Rust, buka terminal dan navigasi ke direktori yang sama dengan pelayan. Kemudian jalankan arahan berikut untuk mencipta projek klien LLM baru:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Tambahkan kebergantungan berikut ke fail `Cargo.toml` anda:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Tiada perpustakaan Rust rasmi untuk OpenAI, namun, crate `async-openai` ialah [perpustakaan yang diselenggara komuniti](https://platform.openai.com/docs/libraries/rust#rust) yang biasa digunakan.

Buka fail `src/main.rs` dan gantikan kandungannya dengan kod berikut:

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
    // Mesej awal
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Sediakan klien OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Sediakan klien MCP
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

    // TODO: Dapatkan senarai alat MCP

    // TODO: Perbualan LLM dengan panggilan alat

    Ok(())
}
```

Kod ini menyediakan aplikasi Rust asas yang akan menyambung ke pelayan MCP dan Model GitHub untuk interaksi LLM.

> [!IMPORTANT]
> Pastikan untuk menetapkan pembolehubah persekitaran `OPENAI_API_KEY` dengan token GitHub anda sebelum menjalankan aplikasi.

Bagus, untuk langkah seterusnya, mari kita senaraikan keupayaan di pelayan.

### -2- Senaraikan keupayaan pelayan

Kini kita akan sambung ke pelayan dan minta keupayaannya:

#### Typescript

Dalam kelas yang sama, tambah kaedah berikut:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // menyenaraikan alat
    const toolsResult = await this.client.listTools();
}
```

Dalam kod sebelumnya kita telah:

- Menambah kod untuk menyambung ke pelayan, `connectToServer`.
- Mewujudkan kaedah `run` yang bertanggungjawab mengendalikan aliran aplikasi kita. Sejauh ini ia hanya menyenaraikan alat tetapi kita akan tambah lagi nanti.

#### Python

```python
# Senaraikan sumber yang ada
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Senaraikan alat yang tersedia
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ini apa yang telah kita tambah:

- Menyenaraikan sumber dan alat dan mencetaknya. Untuk alat kami juga menyenaraikan `inputSchema` yang akan kami gunakan kemudian.

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

Dalam kod sebelumnya kita telah:

- Menyenaraikan alat yang ada di Pelayan MCP
- Untuk setiap alat, menyenaraikan nama, keterangan dan skemanya. Yang terakhir ini akan kita gunakan untuk memanggil alat tidak lama lagi.

#### Java

```java
// Buat penyedia alat yang secara automatik mencari alat MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Penyedia alat MCP mengendalikan secara automatik:
// - Menyenaraikan alat yang tersedia dari pelayan MCP
// - Menukar skema alat MCP ke format LangChain4j
// - Mengurus pelaksanaan alat dan tindak balas
```

Dalam kod sebelumnya kita telah:

- Mewujudkan `McpToolProvider` yang secara automatik menemui dan mendaftar semua alat dari pelayan MCP
- Penyedia alat mengendalikan penukaran antara skema alat MCP dan format alat LangChain4j secara dalaman
- Pendekatan ini mengabstrakkan proses penyenaraian alat dan penukaran secara manual

#### Rust

Mendapatkan alat dari pelayan MCP dilakukan menggunakan kaedah `list_tools`. Dalam fungsi `main` anda, selepas menyediakan klien MCP, tambah kod berikut:

```rust
// Dapatkan senarai alat MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Tukar keupayaan pelayan menjadi alat LLM

Langkah seterusnya selepas menyenaraikan keupayaan pelayan adalah menukarnya ke dalam format yang difahami oleh LLM. Setelah kita lakukan itu, kita boleh menyediakan keupayaan ini sebagai alat kepada LLM kita.

#### TypeScript

1. Tambah kod berikut untuk menukar respons dari Pelayan MCP kepada format alat yang boleh digunakan oleh LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Cipta skema zod berdasarkan input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Tetapkan jenis secara eksplisit kepada "function"
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

    Kod di atas mengambil respons dari Pelayan MCP dan menukarnya kepada format definisi alat yang difahami oleh LLM.

2. Mari kita kemaskini kaedah `run` seterusnya untuk menyenaraikan keupayaan pelayan:

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

    Dalam kod sebelumnya, kita telah mengemas kini kaedah `run` untuk memaparkan hasil dan untuk setiap entri memanggil `openAiToolAdapter`.

#### Python

1. Mula-mula, mari kita cipta fungsi penukar berikut

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

    Dalam fungsi di atas `convert_to_llm_tools` kita mengambil respons alat MCP dan menukarnya ke format yang boleh difahami oleh LLM.

2. Seterusnya, mari kita kemaskini kod klien kita untuk menggunakan fungsi ini seperti berikut:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Di sini, kita menambah panggilan kepada `convert_to_llm_tool` untuk menukar respons alat MCP kepada sesuatu yang boleh kita berikan kepada LLM nanti.

#### .NET

1. Mari kita tambah kod untuk menukar respons alat MCP kepada sesuatu yang boleh difahami oleh LLM

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

Dalam kod sebelumnya kita telah:

- Mewujudkan fungsi `ConvertFrom` yang mengambil, nama, penerangan dan skema input.
- Mendefinisikan fungsi yang mewujudkan `FunctionDefinition` yang dipassing kepada `ChatCompletionsDefinition`. Yang terakhir ini adalah sesuatu yang boleh difahami oleh LLM.

2. Mari kita lihat bagaimana kita boleh kemaskini sesetengah kod sedia ada untuk menggunakan fungsi ini:

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
// Cipta antara muka Bot untuk interaksi bahasa semula jadi
public interface Bot {
    String chat(String prompt);
}

// Konfigurasikan perkhidmatan AI dengan alat LLM dan MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Dalam kod sebelumnya kita telah:

- Mendefinisikan antara muka `Bot` mudah untuk interaksi bahasa semula jadi
- Menggunakan `AiServices` LangChain4j untuk mengikat secara automatik LLM dengan penyedia alat MCP
- Rangka kerja secara automatik mengendalikan penukaran skema alat dan pemanggilan fungsi di belakang tabir
- Pendekatan ini menghapuskan penukaran alat manual - LangChain4j mengendalikan segala kerumitan menukar alat MCP kepada format serasi LLM

#### Rust

Untuk menukar respons alat MCP ke format yang difahami oleh LLM, kita akan tambah fungsi pembantu yang memformat senarai alat. Tambah kod berikut ke fail `main.rs` anda di bawah fungsi `main`. Ini akan dipanggil apabila membuat permintaan kepada LLM:

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

Bagus, kita sudah bersedia untuk mengendalikan sebarang permintaan pengguna, jadi mari kita atasi itu seterusnya.

### -4- Mengendalikan permintaan arahan pengguna

Dalam bahagian kod ini, kita akan mengendalikan permintaan pengguna.

#### TypeScript

1. Tambah kaedah yang akan digunakan untuk memanggil LLM kita:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Panggil alat pelayan
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

    Dalam kod sebelumnya kita:

    - Menambah kaedah `callTools`.
    - Kaedah ini menerima respons LLM dan memeriksa alat mana yang telah dipanggil, jika ada:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // alat panggilan
        }
        ```

    - Memanggil alat, jika LLM menunjukkan ia perlu dipanggil:

        ```typescript
        // 2. Panggil alat pelayan
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Lakukan sesuatu dengan hasilnya
        // PERLU DILAKUKAN
        ```

2. Kemas kini kaedah `run` untuk memasukkan panggilan kepada LLM dan pemanggilan `callTools`:

    ```typescript

    // 1. Buat mesej yang menjadi input untuk LLM
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

    // 3. Semak tindak balas LLM, untuk setiap pilihan, periksa jika ada panggilan alat
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Bagus, mari kita senaraikan kod secara penuh:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod untuk pengesahan skema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // mungkin perlu tukar ke url ini pada masa hadapan: https://models.github.ai/inference
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
            type: "function" as const, // Tetapkan jenis secara jelas kepada "function"
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
    
    
          // 2. Panggil alat pelayan
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Lakukan sesuatu dengan keputusan
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
    
        // 3. Telusuri respons LLM, untuk setiap pilihan, periksa jika ia mempunyai panggilan alat
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

1. Mari kita tambah beberapa import yang diperlukan untuk memanggil LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Seterusnya, mari kita tambah fungsi yang akan memanggil LLM:

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
            # Parameter pilihan
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

    Dalam kod sebelumnya kita telah:

    - Mempassing fungsi kita, yang kita temui pada pelayan MCP dan telah ditukar, kepada LLM.
    - Kemudian kita memanggil LLM dengan fungsi tersebut.
    - Kemudian, kita memeriksa hasil untuk melihat fungsi mana yang harus dipanggil, jika ada.
    - Akhir sekali, kita mempassing tatasusunan fungsi untuk dipanggil.

3. Langkah terakhir, mari kita kemaskini kod utama kita:

    ```python
    prompt = "Add 2 to 20"

    # tanya LLM alat apa yang semuanya, jika ada
    functions_to_call = call_llm(prompt, functions)

    # panggil fungsi yang dicadangkan
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Di situ, itu adalah langkah terakhir, dalam kod di atas kita:

    - Memanggil alat MCP melalui `call_tool` menggunakan fungsi yang LLM fikir kita harus panggil berdasarkan arahan kita.
    - Mencetak hasil panggilan alat ke Pelayan MCP.

#### .NET

1. Mari kita tunjukkan beberapa kod untuk membuat permintaan arahan LLM:

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

    Dalam kod sebelumnya kita telah:

    - Mendapatkan alat dari pelayan MCP, `var tools = await GetMcpTools()`.
    - Mendefinisikan arahan pengguna `userMessage`.
    - Membina objek pilihan yang menentukan model dan alat.
    - Membuat permintaan ke arah LLM.

2. Satu langkah terakhir, mari lihat jika LLM fikir kita harus memanggil fungsi:

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

    Dalam kod sebelumnya kita telah:

    - Melalui satu senarai panggilan fungsi.
    - Untuk setiap panggilan alat, mengurai nama dan argumen dan memanggil alat pada pelayan MCP menggunakan klien MCP. Akhir sekali kami mencetak hasilnya.

Berikut adalah kod secara penuh:

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
    // Laksanakan permintaan bahasa semula jadi yang secara automatik menggunakan alat MCP
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

Dalam kod sebelumnya kita telah:

- Menggunakan arahan bahasa semula jadi yang mudah untuk berinteraksi dengan alat pelayan MCP
- Rangka kerja LangChain4j secara automatik mengendalikan:
  - Menukar arahan pengguna kepada panggilan alat apabila diperlukan
  - Memanggil alat MCP yang sesuai berdasarkan keputusan LLM
  - Mengurus aliran perbualan antara LLM dan pelayan MCP
- Kaedah `bot.chat()` mengembalikan respon bahasa semula jadi yang mungkin termasuk hasil daripada pelaksanaan alat MCP
- Pendekatan ini menyediakan pengalaman pengguna yang lancar di mana pengguna tidak perlu mengetahui pelaksanaan MCP yang mendasari

Contoh kod penuh:

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

Di sinilah kebanyakan kerja berlaku. Kita akan memanggil LLM dengan arahan pengguna awal, kemudian memproses respons untuk melihat jika ada alat yang perlu dipanggil. Jika ada, kita akan memanggil alat tersebut dan meneruskan perbualan dengan LLM sehingga tiada lagi panggilan alat yang diperlukan dan kita mempunyai respons akhir.


Kami akan membuat pelbagai panggilan ke LLM, jadi mari kita takrifkan satu fungsi yang akan mengendalikan panggilan LLM. Tambahkan fungsi berikut ke fail `main.rs` anda:

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

Fungsi ini mengambil klien LLM, senarai mesej (termasuk arahan pengguna), alat dari pelayan MCP, dan menghantar permintaan ke LLM, mengembalikan respons.

Respons dari LLM akan mengandungi satu tatasusunan `choices`. Kita perlu memproses hasil itu untuk melihat sama ada terdapat `tool_calls`. Ini membolehkan kita tahu LLM meminta alat tertentu dipanggil dengan argumen. Tambahkan kod berikut ke bahagian bawah fail `main.rs` anda untuk mentakrifkan fungsi mengendalikan respons LLM:

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

    // Cetak kandungan jika tersedia
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Kendalikan panggilan alat
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Tambah mesej pembantu

        // Laksanakan setiap panggilan alat
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Tambah hasil alat ke mesej
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Teruskan perbualan dengan hasil alat
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

Jika `tool_calls` hadir, ia mengekstrak maklumat alat, memanggil pelayan MCP dengan permintaan alat itu, dan menambah hasilnya ke mesej perbualan. Ia kemudian meneruskan perbualan dengan LLM dan mesej dikemas kini dengan respons pembantu dan hasil panggilan alat.

Untuk mengekstrak maklumat panggilan alat yang LLM kembalikan untuk panggilan MCP, kita akan menambah satu lagi fungsi pembantu untuk mengekstrak segala yang diperlukan untuk membuat panggilan itu. Tambahkan kod berikut ke bahagian bawah fail `main.rs` anda:

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

Dengan semua komponen di tempatnya, kita kini boleh mengendalikan arahan pengguna awal dan memanggil LLM. Kemas kini fungsi `main` anda untuk memasukkan kod berikut:

```rust
// Perbualan LLM dengan panggilan alat
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

Ini akan menyoal LLM dengan arahan pengguna awal yang meminta jumlah dua nombor, dan ia akan memproses respons untuk mengendalikan panggilan alat secara dinamik.

Bagus, anda berjaya!

## Tugasan

Ambil kod dari latihan ini dan bina pelayan dengan lebih banyak alat. Kemudian buat klien dengan LLM, seperti dalam latihan, dan uji dengan arahan yang berbeza untuk memastikan semua alat pelayan anda dipanggil secara dinamik. Cara membina klien ini bermakna pengguna akhir akan mendapat pengalaman pengguna yang hebat kerana mereka dapat menggunakan arahan, bukan arahan klien tepat, dan tidak menyedari sebarang pelayan MCP yang dipanggil.

## Penyelesaian

[Penyelesaian](./solution/README.md)

## Perkara Penting

- Menambah LLM ke klien anda menyediakan cara yang lebih baik bagi pengguna berinteraksi dengan Pelayan MCP.
- Anda perlu menukar respons Pelayan MCP kepada sesuatu yang LLM boleh fahami.

## Contoh

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)
- [Kalkulator Rust](../../../../03-GettingStarted/samples/rust)

## Sumber Tambahan

## Apa Seterusnya

- Seterusnya: [Mengkonsum pelayan menggunakan Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->