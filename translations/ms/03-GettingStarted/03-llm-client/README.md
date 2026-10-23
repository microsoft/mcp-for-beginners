# Mewujudkan klien dengan LLM

> [!NOTE]
> Contoh klien Java berhubung melalui pengangkutan HTTP+SSE lama dan
> mensasarkan API SDK MCP `2025-11-25`. Gunakan SDK yang serasi `2026-07-28` dan
> HTTP Streamable untuk klien jauh baru.

Setakat ini, anda telah melihat cara untuk mencipta pelayan dan klien. Klien telah dapat memanggil pelayan secara jelas untuk menyenaraikan alat, sumber, dan promptnya. Walau bagaimanapun, ini bukanlah pendekatan yang sangat praktikal. Pengguna anda hidup dalam era agen dan mengharapkan untuk menggunakan prompt dan berkomunikasi dengan LLM. Mereka tidak kisah sama ada anda menggunakan MCP untuk menyimpan keupayaan anda; mereka hanya mengharapkan berinteraksi menggunakan bahasa semula jadi. Jadi bagaimana kita menyelesaikannya? Penyelesaian adalah dengan menambah LLM ke klien.

## Gambaran Keseluruhan

Dalam pelajaran ini, kita fokus pada penambahan LLM ke klien anda dan menunjukkan bagaimana ini menyediakan pengalaman yang lebih baik untuk pengguna anda.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Mewujudkan klien dengan LLM.
- Berinteraksi dengan lancar dengan pelayan MCP menggunakan LLM.
- Memberikan pengalaman pengguna akhir yang lebih baik di pihak klien.

## Pendekatan

Mari kita cuba memahami pendekatan yang perlu kita ambil. Menambah LLM kedengaran mudah, tetapi adakah kita benar-benar akan melakukannya?

Inilah cara klien akan berinteraksi dengan pelayan:

1. Menjalin sambungan dengan pelayan.

1. Menyenaraikan keupayaan, prompt, sumber dan alat, dan menyimpan skema mereka.

1. Menambah LLM dan menghantar keupayaan yang disimpan serta skema mereka dalam format yang difahami oleh LLM.

1. Mengendalikan prompt pengguna dengan menghantarnya ke LLM bersama alat yang disenaraikan oleh klien.

Bagus, kini kita faham bagaimana kita boleh melakukan ini pada peringkat tinggi, mari cuba dalam latihan di bawah.

## Latihan: Mewujudkan klien dengan LLM

Dalam latihan ini, kita akan belajar untuk menambah LLM ke klien kita.

### Konfigurasi Microsoft Foundry

GitHub Models telah ditamatkan pada 30 Julai 2026. Buat sumber Microsoft Foundry,
lancarkan model aktif seperti `gpt-5.1`, dan tetapkan pembolehubah persekitaran ini:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

Gunakan nama pelancaran dalam panggilan API. Ia mungkin berbeza daripada nama model asas.
Semak
[jadual persaraan model Microsoft Foundry](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
sebelum memilih model.

### -1- Sambung ke pelayan

Mari kita cipta klien kita terlebih dahulu:

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

Dalam kod sebelum ini kami telah:

- Mengimport perpustakaan yang diperlukan
- Mencipta kelas dengan dua anggota, `client` dan `openai` yang akan membantu kita mengurus klien dan berinteraksi dengan LLM masing-masing.
- Mengkonfigurasi klien OpenAI untuk menggunakan titik akhir Microsoft Foundry v1 dan kunci API.

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

Dalam kod sebelum ini kami telah:

- Mengimport perpustakaan yang diperlukan untuk MCP
- Mencipta klien

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

Pertama, anda perlu menambah pergantungan LangChain4j ke fail `pom.xml` anda. Tambah pergantungan ini untuk mengaktifkan integrasi MCP dan API MiniMax yang serasi OpenAI:

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
`OPENAI_BASE_URL` tidak diset, `MINIMAX_REGION` menyokong `global_en` dan `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Untuk memilih titik akhir mengikut rantau, jangan sertakan `OPENAI_BASE_URL`:

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

Dalam kod sebelum ini kami telah:

- **Menambah pergantungan LangChain4j**: Diperlukan untuk integrasi MCP dan API MiniMax yang serasi OpenAI
- **Mengimport perpustakaan LangChain4j**: Untuk integrasi MCP dan fungsi model sembang OpenAI
- **Mencipta `ChatLanguageModel`**: Dikonfigurasi untuk menggunakan MiniMax dengan kunci API MiniMax, titik akhir, dan ID model yang disokong
- **Menetapkan pengangkutan HTTP**: Menggunakan Server-Sent Events (SSE) untuk menyambung ke pelayan MCP
- **Mencipta klien MCP**: Yang akan mengendalikan komunikasi dengan pelayan
- **Menggunakan sokongan MCP terbina dalam LangChain4j**: Yang memudahkan integrasi antara LLM dan pelayan MCP

#### Rust

Contoh ini mengandaikan anda mempunyai pelayan MCP berasaskan Rust yang berjalan. Jika anda belum ada, rujuk kembali pelajaran [01-first-server](../01-first-server/README.md) untuk mencipta pelayan.

Setelah anda mempunyai pelayan MCP Rust anda, buka terminal dan navigasi ke direktori yang sama dengan pelayan. Kemudian jalankan arahan berikut untuk mencipta projek klien LLM baru:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Tambah pergantungan berikut ke fail `Cargo.toml` anda:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Tiada perpustakaan Rust rasmi untuk OpenAI, namun, crate `async-openai` adalah [perpustakaan yang dikendalikan komuniti](https://platform.openai.com/docs/libraries/rust#rust) yang biasa digunakan.

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

Kod ini menyediakan aplikasi Rust yang berhubung ke pelayan MCP dan
pelancaran model Microsoft Foundry untuk interaksi LLM.

> [!IMPORTANT]
> Tetapkan `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, dan
> `AZURE_OPENAI_DEPLOYMENT` sebelum menjalankan aplikasi.

Bagus, untuk langkah seterusnya, mari kita senaraikan keupayaan pada pelayan.

### -2- Senaraikan keupayaan pelayan

Kini kita akan menyambung ke pelayan dan meminta keupayaannya:

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

    // listing tools
    const toolsResult = await this.client.listTools();
}
```

Dalam kod sebelum ini kami telah:

- Menambah kod untuk menyambung ke pelayan, `connectToServer`.
- Mencipta kaedah `run` yang bertanggungjawab mengendalikan aliran aplikasi kami. Setakat ini, ia hanya menyenaraikan alat tetapi kami akan tambah lebih banyak tidak lama lagi.

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

Berikut ialah apa yang kami tambah:

- Menyenaraikan sumber dan alat serta mencetaknya. Untuk alat kami juga menyenaraikan `inputSchema` yang akan kami gunakan nanti.

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

Dalam kod sebelum ini kami telah:

- Menyenaraikan alat-alat yang tersedia pada Pelayan MCP
- Untuk setiap alat, menyenaraikan nama, deskripsi dan skemanya. Yang terakhir adalah sesuatu yang akan kami gunakan untuk memanggil alat tidak lama lagi.

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

Dalam kod sebelum ini kami telah:

- Mencipta `McpToolProvider` yang secara automatik mengesan dan mendaftar semua alat dari pelayan MCP
- Penyedia alat mengendalikan penukaran antara skema alat MCP dan format alat LangChain4j secara dalaman
- Pendekatan ini mengabstrakkan proses penyenaraian dan penukaran alat secara manual

#### Rust

Pengambilan alat dari pelayan MCP dilakukan menggunakan kaedah `list_tools`. Dalam fungsi `main` anda, selepas menyediakan klien MCP, tambahkan kod berikut:

```rust
// Get MCP tool listing 
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Menukar keupayaan pelayan ke alat LLM

Langkah seterusnya selepas menyenaraikan keupayaan pelayan adalah untuk menukarnya ke format yang difahami oleh LLM. Setelah kita melakukan itu, kita boleh menyediakan keupayaan ini sebagai alat kepada LLM kita.

#### TypeScript

1. Tambah kod berikut untuk menukar respons dari Pelayan MCP ke format alat yang boleh digunakan oleh LLM:

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

    Kod di atas mengambil respons dari Pelayan MCP dan menukarnya ke format definisi alat yang difahami oleh LLM.

2. Mari kita kemas kini kaedah `run` seterusnya untuk menyenaraikan keupayaan pelayan:

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

    Dalam kod sebelum ini, kami kemas kini kaedah `run` untuk memetakan melalui hasil dan bagi setiap entri memanggil `openAiToolAdapter`.

#### Python

1. Pertama, mari kita cipta fungsi penukar berikut

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

    Dalam fungsi di atas `convert_to_llm_tools` kami mengambil respons alat MCP dan menukarnya ke format yang boleh difahami LLM.

2. Seterusnya, mari kita kemas kini kod klien kita untuk memanfaatkan fungsi ini seperti berikut:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Di sini, kami menambah panggilan ke `convert_to_llm_tool` untuk menukar respons alat MCP ke sesuatu yang boleh kita beri makan pada LLM kemudian.

#### .NET

1. Mari kita tambah kod untuk menukar respons alat MCP ke sesuatu yang boleh difahami LLM

```csharp
ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}
```

Dalam kod sebelum ini kami telah:

- Mencipta fungsi `ConvertFrom` yang mengambil, nama, deskripsi dan skema input.
- Mencipta OpenAI `ChatTool` dari skema JSON alat MCP.

2. Mari lihat bagaimana kami boleh mengemas kini beberapa kod sedia ada untuk memanfaatkan fungsi ini:

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
    
Dalam kod sebelum ini, kami telah:

- Kemas kini fungsi untuk menukar respons alat MCP ke alat LLM. Mari tandakan kod yang kami tambah:

   ```csharp
   JsonElement propertiesElement;
   tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

   var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
   Console.WriteLine($"Tool definition: {def}");
   toolDefinitions.Add(def);
   ```

Skema input adalah sebahagian daripada respons alat tetapi pada atribut "properties", jadi kita perlu mengeluarkan. Selanjutnya, kita kini memanggil `ConvertFrom` dengan butiran alat. Kini kita telah melakukan kerja berat, mari lihat bagaimana panggilan itu digabungkan semasa kita mengendalikan prompt pengguna seterusnya.

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

Dalam kod sebelum ini kami telah:

- Mendefinisikan antara muka `Bot` mudah untuk interaksi bahasa semula jadi
- Menggunakan `AiServices` LangChain4j untuk secara automatik mengikat LLM dengan penyedia alat MCP
- Rangka kerja mengendalikan penukaran skema alat dan panggilan fungsi di belakang tabir secara automatik
- Pendekatan ini menghapuskan penukaran alat manual - LangChain4j mengendalikan semua kerumitan menukar alat MCP ke format serasi LLM

#### Rust

Untuk menukar respons alat MCP ke format yang boleh difahami oleh LLM, kita akan tambah fungsi pembantu yang memformat senarai alat. Tambah kod berikut pada fail `main.rs` anda di bawah fungsi `main`. Ini akan dipanggil apabila membuat permintaan ke LLM:

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

Bagus, kita sudah sedia untuk mengendalikan sebarang permintaan pengguna, jadi mari kita tangani itu seterusnya.

### -4- Mengendalikan permintaan prompt pengguna

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

    Dalam kod sebelum ini kita:

    - Menambah kaedah `callTools`.
    - Kaedah ini mengambil respons LLM dan menyemak alat apa yang telah dipanggil, jika ada:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // call tool
        }
        ```

    - Memanggil alat, jika LLM menunjukkan ia harus dipanggil:

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

2. Kemas kini kaedah `run` untuk memasukkan panggilan ke LLM dan panggilan `callTools`:

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

Bagus, mari senaraikan kod penuh:

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

1. Mari tambah beberapa import yang diperlukan untuk memanggil LLM

    ```python
    # llm
    import os
    from openai import OpenAI
    import json
    ```

2. Seterusnya, mari tambah fungsi yang akan memanggil LLM. Contoh ini menggunakan
    model `gpt-5.1` aktif. Semak
    [jadual persaraan model Microsoft Foundry](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
    semasa memilih model untuk aplikasi anda.

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

    Dalam kod sebelum ini kami telah:

    - Meneruskan fungsi kami, yang kami temukan pada pelayan MCP dan tukar, kepada LLM.
    - Kemudian kami memanggil LLM dengan fungsi tersebut.
    - Kemudian, kami memeriksa hasil untuk melihat fungsi mana yang harus kami panggil, kalau ada.
    - Akhir sekali, kami meneruskan susunan fungsi untuk dipanggil.

3. Langkah akhir, mari kemas kini kod utama kami:

    ```python
    prompt = "Add 2 to 20"

    # ask LLM what tools to all, if any
    functions_to_call = call_llm(prompt, functions)

    # call suggested functions
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Itu, itulah langkah terakhir, dalam kod di atas kami:

    - Memanggil alat MCP melalui `call_tool` menggunakan fungsi yang LLM fikir kami harus panggil berdasarkan prompt kami.
    - Mencetak hasil panggilan alat ke Pelayan MCP.

#### .NET

1. Mari tunjukkan kod untuk membuat permintaan prompt LLM:

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

    Dalam kod sebelum ini kami telah:

    - Alat diambil dari pelayan MCP, `var tools = await GetMcpTools()`.
    - Ditakrifkan prompt pengguna `userMessage`.
    - Pembina objek pilihan yang menentukan model dan alat.
    - Membuat permintaan ke arah LLM.

2. Satu langkah terakhir, mari kita lihat jika LLM berfikir kita perlu memanggil fungsi:

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

    Dalam kod sebelumnya kami telah:

    - Melalui senarai panggilan fungsi.
    - Untuk setiap panggilan alat, mengurai nama dan argumen serta memanggil alat di pelayan MCP menggunakan klien MCP. Akhir sekali kami cetak hasilnya.

Berikut adalah kod secara penuh:

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

Dalam kod sebelumnya kami telah:

- Menggunakan arahan bahasa semula jadi yang mudah untuk berinteraksi dengan alat pelayan MCP
- Rangka kerja LangChain4j secara automatik mengendalikan:
  - Menukar arahan pengguna menjadi panggilan alat apabila diperlukan
  - Memanggil alat MCP yang sesuai berdasarkan keputusan LLM
  - Menguruskan aliran perbualan antara LLM dan pelayan MCP
- Kaedah `bot.chat()` mengembalikan respons bahasa semula jadi yang mungkin termasuk hasil dari pelaksanaan alat MCP
- Pendekatan ini menyediakan pengalaman pengguna yang lancar di mana pengguna tidak perlu mengetahui tentang pelaksanaan MCP yang mendasari

Contoh kod lengkap:

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

Di sinilah sebahagian besar kerja dilakukan. Kami akan memanggil LLM dengan arahan pengguna awal, kemudian memproses respons untuk melihat jika ada alat yang perlu dipanggil. Jika ya, kami akan memanggil alat tersebut dan meneruskan perbualan dengan LLM sehingga tiada panggilan alat lagi diperlukan dan kami mendapat respons akhir.

Kami akan membuat pelbagai panggilan ke LLM, jadi mari kita definisikan fungsi yang akan mengendalikan panggilan LLM. Tambahkan fungsi berikut ke dalam fail `main.rs` anda:

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

Fungsi ini mengambil klien LLM, senarai mesej (termasuk arahan pengguna), alat dari pelayan MCP, dan menghantar permintaan ke LLM, mengembalikan respons.

Respons dari LLM akan mengandungi array `choices`. Kami perlu memproses hasil untuk melihat jika ada `tool_calls` yang hadir. Ini membolehkan kita mengetahui LLM meminta alat tertentu dipanggil dengan argumen. Tambahkan kod berikut di bahagian bawah fail `main.rs` anda untuk mendefinisikan fungsi bagi mengendalikan respons LLM:

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

Jika `tool_calls` hadir, ia mengekstrak maklumat alat, memanggil pelayan MCP dengan permintaan alat, dan menambah hasilnya ke mesej perbualan. Kemudian ia meneruskan perbualan dengan LLM dan mesej dikemas kini dengan respons pembantu dan hasil panggilan alat.

Untuk mengekstrak maklumat panggilan alat yang LLM kembalikan untuk panggilan MCP, kami akan menambah satu fungsi pembantu lagi untuk mengekstrak segala yang diperlukan untuk membuat panggilan itu. Tambahkan kod berikut ke bahagian bawah fail `main.rs` anda:

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

Dengan semua bahagian sudah tersedia, kini kami boleh mengendalikan arahan pengguna awal dan memanggil LLM. Kemas kini fungsi `main` anda untuk memasukkan kod berikut:

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

Ini akan membuat pertanyaan kepada LLM dengan arahan pengguna awal yang meminta jumlah dua nombor, dan memproses respons untuk mengendalikan panggilan alat secara dinamik.

Hebat, anda berjaya!

## Tugasan

Ambil kod dari latihan dan bina pelayan dengan lebih banyak alat. Kemudian buat klien dengan LLM, seperti dalam latihan, dan uji dengan arahan berbeza untuk memastikan semua alat pelayan anda dipanggil secara dinamik. Cara membina klien ini membolehkan pengguna akhir mempunyai pengalaman pengguna yang hebat kerana mereka dapat menggunakan arahan, bukannya arahan klien yang tepat, dan tidak menyedari sebarang pelayan MCP yang dipanggil.

## Penyelesaian

[Penyelesaian](./solution/README.md)

## Perkara Penting

- Menambah LLM ke klien anda menyediakan cara yang lebih baik untuk pengguna berinteraksi dengan Pelayan MCP.
- Anda perlu menukar respons Pelayan MCP kepada sesuatu yang LLM boleh fahami.

## Contoh

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Sumber Tambahan

## Apa Seterusnya

- Seterusnya: [Menggunakan pelayan dengan Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->