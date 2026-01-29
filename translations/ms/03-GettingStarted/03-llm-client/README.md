# Mewujudkan klien dengan LLM

Setakat ini, anda telah melihat bagaimana untuk mewujudkan pelayan dan klien. Klien telah dapat memanggil pelayan secara eksplisit untuk menyenaraikan alat, sumber dan arahan. Walau bagaimanapun, ini bukan pendekatan yang sangat praktikal. Pengguna anda hidup dalam era agen dan mengharapkan untuk menggunakan arahan dan berkomunikasi dengan LLM untuk berbuat demikian. Bagi pengguna anda, mereka tidak kisah jika anda menggunakan MCP atau tidak untuk menyimpan keupayaan anda tetapi mereka mengharapkan untuk menggunakan bahasa semula jadi untuk berinteraksi. Jadi bagaimana kita menyelesaikan ini? Penyelesaiannya adalah dengan menambah LLM ke klien.

## Gambaran Keseluruhan

Dalam pelajaran ini kita fokus pada menambah LLM untuk klien anda dan menunjukkan bagaimana ini memberikan pengalaman yang jauh lebih baik untuk pengguna anda.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Mewujudkan klien dengan LLM.
- Berinteraksi dengan lancar dengan pelayan MCP menggunakan LLM.
- Memberikan pengalaman pengguna akhir yang lebih baik di pihak klien.

## Pendekatan

Mari kita cuba memahami pendekatan yang perlu kita ambil. Menambah LLM kedengaran mudah, tetapi adakah kita benar-benar akan melakukannya?

Berikut adalah bagaimana klien akan berinteraksi dengan pelayan:

1. Menjalin sambungan dengan pelayan.

1. Menyenaraikan keupayaan, arahan, sumber dan alat, dan menyimpan skema mereka.

1. Menambah LLM dan menghantar keupayaan yang disimpan dan skema mereka dalam format yang difahami oleh LLM.

1. Mengendalikan arahan pengguna dengan menghantarnya ke LLM bersama-sama dengan alat yang disenaraikan oleh klien.

Bagus, sekarang kita faham bagaimana kita boleh melakukan ini pada tahap tinggi, mari cuba dalam latihan di bawah.

## Latihan: Mewujudkan klien dengan LLM

Dalam latihan ini, kita akan belajar menambah LLM ke klien kita.

### Pengesahan menggunakan Token Akses Peribadi GitHub

Mewujudkan token GitHub adalah proses yang mudah. Berikut adalah cara anda boleh melakukannya:

- Pergi ke Tetapan GitHub – Klik pada gambar profil anda di sudut kanan atas dan pilih Tetapan.
- Navigasi ke Tetapan Pembangun – Skrol ke bawah dan klik pada Tetapan Pembangun.
- Pilih Token Akses Peribadi – Klik pada token Berbutir Halus dan kemudian Hasilkan token baru.
- Konfigurasikan Token Anda – Tambah nota untuk rujukan, tetapkan tarikh luput, dan pilih skop (kebenaran) yang diperlukan. Dalam kes ini pastikan untuk menambah kebenaran Models.
- Hasilkan dan Salin Token – Klik Hasilkan token, dan pastikan untuk menyalinnya dengan segera, kerana anda tidak akan dapat melihatnya lagi.

### -1- Sambung ke pelayan

Mari kita buat klien kita terlebih dahulu:

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

Dalam kod sebelum ini kami telah:

- Mengimport perpustakaan yang diperlukan
- Mewujudkan kelas dengan dua anggota, `client` dan `openai` yang akan membantu kita menguruskan klien dan berinteraksi dengan LLM masing-masing.
- Mengkonfigurasi instans LLM kami untuk menggunakan Models GitHub dengan menetapkan `baseUrl` untuk menunjuk ke API inferens.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Cipta parameter pelayan untuk sambungan stdio
server_params = StdioServerParameters(
    command="mcp",  # Boleh laksana
    args=["run", "server.py"],  # Argumen baris arahan pilihan
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

Dalam kod sebelum ini kami telah:

- Mengimport perpustakaan yang diperlukan untuk MCP
- Mewujudkan klien

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

Pertama, anda perlu menambah kebergantungan LangChain4j ke fail `pom.xml` anda. Tambah kebergantungan ini untuk membolehkan integrasi MCP dan sokongan Models GitHub:

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
    
    <!-- GitHub Models Support -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-github-models</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

Kemudian buat kelas klien Java anda:

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

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // Konfigurasikan LLM untuk menggunakan Model GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Buat pengangkutan MCP untuk menyambung ke pelayan
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
}
```

Dalam kod sebelum ini kami telah:

- **Menambah kebergantungan LangChain4j**: Diperlukan untuk integrasi MCP, klien rasmi OpenAI, dan sokongan Models GitHub
- **Mengimport perpustakaan LangChain4j**: Untuk integrasi MCP dan fungsi model chat OpenAI
- **Mewujudkan `ChatLanguageModel`**: Dikemaskini untuk menggunakan Models GitHub dengan token GitHub anda
- **Menyiapkan pengangkutan HTTP**: Menggunakan Server-Sent Events (SSE) untuk menyambung ke pelayan MCP
- **Mewujudkan klien MCP**: Yang akan mengendalikan komunikasi dengan pelayan
- **Menggunakan sokongan MCP terbina dalam LangChain4j**: Yang memudahkan integrasi antara LLM dan pelayan MCP

#### Rust

Contoh ini mengandaikan anda mempunyai pelayan MCP berasaskan Rust yang berjalan. Jika anda tidak mempunyai satu, rujuk kembali pelajaran [01-first-server](../01-first-server/README.md) untuk membuat pelayan.

Setelah anda mempunyai pelayan MCP Rust anda, buka terminal dan navigasi ke direktori yang sama dengan pelayan. Kemudian jalankan arahan berikut untuk membuat projek klien LLM baru:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Tambah kebergantungan berikut ke fail `Cargo.toml` anda:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Tiada perpustakaan rasmi Rust untuk OpenAI, namun, `async-openai` crate adalah [perpustakaan yang diselenggara oleh komuniti](https://platform.openai.com/docs/libraries/rust#rust) yang biasa digunakan.

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

Kod ini menyediakan aplikasi Rust asas yang akan menyambung ke pelayan MCP dan Models GitHub untuk interaksi LLM.

> [!IMPORTANT]
> Pastikan untuk menetapkan pembolehubah persekitaran `OPENAI_API_KEY` dengan token GitHub anda sebelum menjalankan aplikasi.

Bagus, untuk langkah seterusnya, mari kita senaraikan keupayaan pada pelayan.

### -2- Senaraikan keupayaan pelayan

Sekarang kita akan menyambung ke pelayan dan meminta keupayaannya:

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

Dalam kod sebelum ini kami telah:

- Menambah kod untuk menyambung ke pelayan, `connectToServer`.
- Mewujudkan kaedah `run` yang bertanggungjawab untuk mengendalikan aliran aplikasi kami. Setakat ini ia hanya menyenaraikan alat tetapi kami akan menambah lebih banyak lagi tidak lama lagi.

#### Python

```python
# Senaraikan sumber yang tersedia
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

Ini yang kami tambah:

- Menyenaraikan sumber dan alat dan mencetaknya. Untuk alat kami juga menyenaraikan `inputSchema` yang kami gunakan kemudian.

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

Dalam kod sebelum ini kami telah:

- Menyenaraikan alat yang tersedia di Pelayan MCP
- Untuk setiap alat, menyenaraikan nama, penerangan dan skemanya. Yang terakhir adalah sesuatu yang akan kami gunakan untuk memanggil alat tidak lama lagi.

#### Java

```java
// Cipta penyedia alat yang secara automatik menemui alat MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Penyedia alat MCP secara automatik mengendalikan:
// - Menyenaraikan alat yang tersedia dari pelayan MCP
// - Menukar skema alat MCP ke format LangChain4j
// - Menguruskan pelaksanaan alat dan respons
```

Dalam kod sebelum ini kami telah:

- Mewujudkan `McpToolProvider` yang secara automatik mengesan dan mendaftar semua alat dari pelayan MCP
- Penyedia alat mengendalikan penukaran antara skema alat MCP dan format alat LangChain4j secara dalaman
- Pendekatan ini mengabstrakkan proses penyenaraian alat manual dan penukaran

#### Rust

Mengambil alat dari pelayan MCP dilakukan menggunakan kaedah `list_tools`. Dalam fungsi `main` anda, selepas menyediakan klien MCP, tambah kod berikut:

```rust
// Dapatkan senarai alat MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Tukar keupayaan pelayan kepada alat LLM

Langkah seterusnya selepas menyenaraikan keupayaan pelayan adalah menukarnya ke format yang difahami oleh LLM. Setelah kita lakukan itu, kita boleh menyediakan keupayaan ini sebagai alat kepada LLM kita.

#### TypeScript

1. Tambah kod berikut untuk menukar respons dari Pelayan MCP ke format alat yang boleh digunakan oleh LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Cipta skema zod berdasarkan input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Tetapkan jenis secara eksplisit kepada "fungsi"
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

    Kod di atas mengambil respons dari Pelayan MCP dan menukarnya ke format definisi alat yang boleh difahami oleh LLM.

1. Mari kita kemas kini kaedah `run` seterusnya untuk menyenaraikan keupayaan pelayan:

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

    Dalam kod sebelum ini, kami telah mengemas kini kaedah `run` untuk memetakan melalui hasil dan untuk setiap entri memanggil `openAiToolAdapter`.

#### Python

1. Pertama, mari kita buat fungsi penukar berikut

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

    Dalam fungsi di atas `convert_to_llm_tools` kami mengambil respons alat MCP dan menukarnya ke format yang boleh difahami oleh LLM.

1. Seterusnya, mari kita kemas kini kod klien kita untuk menggunakan fungsi ini seperti berikut:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Di sini, kami menambah panggilan ke `convert_to_llm_tool` untuk menukar respons alat MCP kepada sesuatu yang boleh kami berikan kepada LLM kemudian.

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

Dalam kod sebelum ini kami telah:

- Mewujudkan fungsi `ConvertFrom` yang mengambil nama, penerangan dan skema input.
- Mendefinisikan fungsi yang mencipta FunctionDefinition yang dihantar ke ChatCompletionsDefinition. Yang terakhir adalah sesuatu yang boleh difahami oleh LLM.

1. Mari kita lihat bagaimana kita boleh mengemas kini beberapa kod sedia ada untuk mengambil kesempatan fungsi di atas:

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

Dalam kod sebelum ini kami telah:

- Mendefinisikan antara muka `Bot` ringkas untuk interaksi bahasa semula jadi
- Menggunakan `AiServices` LangChain4j untuk mengikat LLM secara automatik dengan penyedia alat MCP
- Rangka kerja secara automatik mengendalikan penukaran skema alat dan panggilan fungsi di belakang tabir
- Pendekatan ini menghapuskan penukaran alat manual - LangChain4j mengendalikan semua kerumitan menukar alat MCP ke format yang serasi dengan LLM

#### Rust

Untuk menukar respons alat MCP ke format yang boleh difahami oleh LLM, kita akan menambah fungsi pembantu yang memformat senarai alat. Tambah kod berikut ke fail `main.rs` anda di bawah fungsi `main`. Ini akan dipanggil apabila membuat permintaan ke LLM:

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

Bagus, kita sudah bersedia untuk mengendalikan sebarang permintaan pengguna, jadi mari kita tangani itu seterusnya.

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

    Dalam kod sebelum ini kami:

    - Menambah kaedah `callTools`.
    - Kaedah ini mengambil respons LLM dan memeriksa alat apa yang telah dipanggil, jika ada:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // panggil alat
        }
        ```

    - Memanggil alat, jika LLM menunjukkan ia harus dipanggil:

        ```typescript
        // 2. Panggil alat pelayan
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Lakukan sesuatu dengan hasilnya
        // TODO
        ```

1. Kemas kini kaedah `run` untuk memasukkan panggilan ke LLM dan memanggil `callTools`:

    ```typescript

    // 1. Cipta mesej yang menjadi input untuk LLM
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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Semak respons LLM, untuk setiap pilihan, periksa jika ia mempunyai panggilan alat
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Bagus, mari kita senaraikan kod penuh:

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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Teliti respons LLM, untuk setiap pilihan, periksa jika ia mempunyai panggilan alat
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

1. Seterusnya, mari kita tambah fungsi yang akan memanggil LLM:

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

    Dalam kod sebelum ini kami telah:

    - Menghantar fungsi kami, yang kami temui di pelayan MCP dan ditukar, ke LLM.
    - Kemudian kami memanggil LLM dengan fungsi tersebut.
    - Kemudian, kami memeriksa hasil untuk melihat fungsi apa yang harus kami panggil, jika ada.
    - Akhirnya, kami menghantar tatasusunan fungsi untuk dipanggil.

1. Langkah terakhir, mari kita kemas kini kod utama kita:

    ```python
    prompt = "Add 2 to 20"

    # tanya LLM alat apa yang perlu digunakan, jika ada
    functions_to_call = call_llm(prompt, functions)

    # panggil fungsi yang dicadangkan
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Itu, itu adalah langkah terakhir, dalam kod di atas kami:

    - Memanggil alat MCP melalui `call_tool` menggunakan fungsi yang LLM fikir kami harus panggil berdasarkan arahan kami.
    - Mencetak hasil panggilan alat ke Pelayan MCP.

#### .NET

1. Mari kita tunjukkan beberapa kod untuk melakukan permintaan arahan LLM:

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
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    Dalam kod sebelum ini kami telah:

    - Mendapatkan alat dari pelayan MCP, `var tools = await GetMcpTools()`.
    - Mendefinisikan arahan pengguna `userMessage`.
    - Membina objek pilihan yang menentukan model dan alat.
    - Membuat permintaan ke LLM.

1. Satu langkah terakhir, mari kita lihat jika LLM fikir kita harus memanggil fungsi:

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

    Dalam kod sebelum ini kami telah:

    - Melalui senarai panggilan fungsi.
    - Untuk setiap panggilan alat, mengurai nama dan argumen dan memanggil alat di pelayan MCP menggunakan klien MCP. Akhirnya kami mencetak hasilnya.

Berikut adalah kod penuh:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

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
    Model = "gpt-4o-mini",
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

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
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

Dalam kod sebelum ini kami telah:

- Menggunakan arahan bahasa semula jadi yang mudah untuk berinteraksi dengan alat pelayan MCP
- Rangka kerja LangChain4j secara automatik mengendalikan:
  - Menukar arahan pengguna kepada panggilan alat apabila diperlukan
  - Memanggil alat MCP yang sesuai berdasarkan keputusan LLM
  - Mengurus aliran perbualan antara LLM dan pelayan MCP
- Kaedah `bot.chat()` mengembalikan respons bahasa semula jadi yang mungkin termasuk hasil dari pelaksanaan alat MCP
- Pendekatan ini menyediakan pengalaman pengguna yang lancar di mana pengguna tidak perlu mengetahui tentang pelaksanaan MCP yang mendasari

Contoh kod lengkap:

```java
public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofSeconds(60))
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
}
```

#### Rust

Di sinilah sebahagian besar kerja berlaku. Kami akan memanggil LLM dengan arahan pengguna awal, kemudian memproses respons untuk melihat jika ada alat yang perlu dipanggil. Jika ya, kami akan memanggil alat tersebut dan meneruskan perbualan dengan LLM sehingga tiada lagi panggilan alat diperlukan dan kami mempunyai respons akhir.

Kami akan membuat beberapa panggilan ke LLM, jadi mari kita definisikan fungsi yang akan mengendalikan panggilan LLM. Tambah fungsi berikut ke fail `main.rs` anda:

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
Respons daripada LLM akan mengandungi satu tatasusunan `choices`. Kita perlu memproses keputusan untuk melihat jika ada `tool_calls` yang hadir. Ini membolehkan kita tahu LLM sedang meminta alat tertentu dipanggil dengan argumen. Tambahkan kod berikut di bahagian bawah fail `main.rs` anda untuk mentakrifkan fungsi bagi mengendalikan respons LLM:

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

    // Cetak kandungan jika ada
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

Jika `tool_calls` hadir, ia mengekstrak maklumat alat, memanggil pelayan MCP dengan permintaan alat tersebut, dan menambah keputusan ke dalam mesej perbualan. Ia kemudian meneruskan perbualan dengan LLM dan mesej dikemas kini dengan respons pembantu dan keputusan panggilan alat.

Untuk mengekstrak maklumat panggilan alat yang LLM kembalikan untuk panggilan MCP, kita akan menambah satu lagi fungsi pembantu untuk mengekstrak segala yang diperlukan untuk membuat panggilan tersebut. Tambahkan kod berikut di bahagian bawah fail `main.rs` anda:

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

Dengan semua bahagian lengkap, kita kini boleh mengendalikan prompt pengguna awal dan memanggil LLM. Kemas kini fungsi `main` anda untuk memasukkan kod berikut:

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

Ini akan membuat pertanyaan kepada LLM dengan prompt pengguna awal yang meminta jumlah dua nombor, dan ia akan memproses respons untuk mengendalikan panggilan alat secara dinamik.

Bagus, anda berjaya!

## Tugasan

Ambil kod dari latihan dan bina pelayan dengan beberapa alat lagi. Kemudian cipta klien dengan LLM, seperti dalam latihan, dan uji dengan pelbagai prompt untuk memastikan semua alat pelayan anda dipanggil secara dinamik. Cara membina klien ini bermakna pengguna akhir akan mendapat pengalaman pengguna yang hebat kerana mereka boleh menggunakan prompt, bukannya arahan klien yang tepat, dan tidak menyedari sebarang pelayan MCP sedang dipanggil.

## Penyelesaian

[Penyelesaian](/03-GettingStarted/03-llm-client/solution/README.md)

## Perkara Penting

- Menambah LLM ke klien anda menyediakan cara yang lebih baik untuk pengguna berinteraksi dengan Pelayan MCP.
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

- Seterusnya: [Menggunakan pelayan dengan Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->