# Membuat Klien

Klien adalah aplikasi atau skrip khusus yang berkomunikasi secara langsung dengan MCP Server untuk meminta sumber, alat, dan arahan. Tidak seperti menggunakan alat pemeriksa yang menyediakan antara muka grafik untuk berinteraksi dengan server, menulis klien sendiri membolehkan interaksi secara programatik dan automatik. Ini membolehkan pembangun mengintegrasikan keupayaan MCP ke dalam aliran kerja mereka sendiri, mengautomasi tugas, dan membina penyelesaian khusus yang disesuaikan dengan keperluan tertentu.

## Gambaran Keseluruhan

Pelajaran ini memperkenalkan konsep klien dalam ekosistem Model Context Protocol (MCP). Anda akan belajar cara menulis klien anda sendiri dan menyambungkannya ke MCP Server.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Memahami apa yang boleh dilakukan oleh klien.
- Menulis klien anda sendiri.
- Menyambung dan menguji klien dengan MCP Server untuk memastikan ia berfungsi seperti yang diharapkan.

## Apa yang diperlukan untuk menulis klien?

Untuk menulis klien, anda perlu melakukan perkara berikut:

- **Import pustaka yang betul**. Anda akan menggunakan pustaka yang sama seperti sebelumnya, hanya dengan struktur yang berbeza.
- **Mewujudkan klien**. Ini melibatkan penciptaan instance klien dan menyambungkannya ke kaedah pengangkutan yang dipilih.
- **Memutuskan sumber yang hendak disenaraikan**. MCP Server anda mempunyai sumber, alat, dan arahan; anda perlu memutuskan yang mana satu untuk disenaraikan.
- **Mengintegrasikan klien ke aplikasi hos**. Setelah anda mengetahui keupayaan server, anda perlu mengintegrasikannya ke aplikasi hos anda supaya apabila pengguna menaip arahan atau perintah lain, ciri server yang sesuai akan dipanggil.

Sekarang kita memahami secara umum apa yang akan kita lakukan, mari kita lihat contoh berikut.

### Contoh Klien

Mari kita lihat contoh klien ini:

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Dalam kod di atas, kita:

- Mengimport pustaka.
- Mencipta instance klien dan menyambungkannya menggunakan stdio sebagai pengangkutan.
- Menyenaraikan arahan, sumber, dan alat serta memanggil semuanya.

Itulah dia, klien yang boleh berkomunikasi dengan MCP Server.

Mari kita luangkan masa dalam bahagian latihan seterusnya dan pecahkan setiap petikan kod untuk menerangkan apa yang sedang berlaku.

## Latihan: Menulis Klien

Seperti yang dinyatakan di atas, mari kita luangkan masa menerangkan kod, dan jika anda mahu, anda boleh menulis kod bersama-sama.

### -1- Mengimport pustaka

Mari kita import pustaka yang diperlukan. Kita memerlukan rujukan kepada klien dan protokol pengangkutan yang dipilih, stdio. Stdio adalah protokol untuk perkara yang dijalankan pada mesin tempatan anda. SSE adalah protokol pengangkutan lain yang akan kita tunjukkan dalam bab akan datang, tetapi itu adalah pilihan lain. Buat masa ini, mari kita teruskan dengan stdio.

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
```

#### Java

Untuk Java, anda akan mencipta klien yang menyambung ke MCP Server dari latihan sebelumnya. Menggunakan struktur projek Java Spring Boot yang sama dari [Memulakan dengan MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), buat kelas Java baru bernama `SDKClient` dalam folder `src/main/java/com/microsoft/mcp/sample/client/` dan tambahkan import berikut:

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

Anda perlu menambahkan kebergantungan berikut ke fail `Cargo.toml` anda.

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

Dari situ, anda boleh mengimport pustaka yang diperlukan dalam kod klien anda.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Mari kita teruskan ke instansiasi.

### -2- Mewujudkan klien dan pengangkutan

Kita perlu mencipta instance pengangkutan dan instance klien kita:

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

Dalam kod di atas, kita telah:

- Mencipta instance pengangkutan stdio. Perhatikan bagaimana ia menentukan perintah dan argumen untuk mencari dan memulakan server kerana itu adalah sesuatu yang perlu kita lakukan semasa mencipta klien.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Mewujudkan klien dengan memberikan nama dan versi.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Menyambungkan klien ke pengangkutan yang dipilih.

    ```typescript
    await client.connect(transport);
    ```

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

Dalam kod di atas, kita telah:

- Mengimport pustaka yang diperlukan.
- Mewujudkan objek parameter server kerana kita akan menggunakannya untuk menjalankan server supaya kita boleh menyambung kepadanya dengan klien kita.
- Mendefinisikan kaedah `run` yang seterusnya memanggil `stdio_client` yang memulakan sesi klien.
- Mencipta titik masuk di mana kita menyediakan kaedah `run` kepada `asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

Dalam kod di atas, kita telah:

- Mengimport pustaka yang diperlukan.
- Mencipta pengangkutan stdio dan mencipta klien `mcpClient`. Yang terakhir adalah sesuatu yang akan kita gunakan untuk menyenaraikan dan memanggil ciri pada MCP Server.

Perhatikan, dalam "Arguments", anda boleh menunjuk kepada *.csproj* atau kepada executable.

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // Your client logic goes here
    }
}
```

Dalam kod di atas, kita telah:

- Mencipta kaedah utama yang menyediakan pengangkutan SSE yang menunjuk kepada `http://localhost:8080` di mana MCP Server kita akan berjalan.
- Mencipta kelas klien yang mengambil pengangkutan sebagai parameter konstruktor.
- Dalam kaedah `run`, kita mencipta klien MCP secara segerak menggunakan pengangkutan dan memulakan sambungan.
- Menggunakan pengangkutan SSE (Server-Sent Events) yang sesuai untuk komunikasi berasaskan HTTP dengan MCP Server Java Spring Boot.

#### Rust

Klien Rust ini mengandaikan server adalah projek saudara bernama "calculator-server" dalam direktori yang sama. Kod di bawah akan memulakan server dan menyambung kepadanya.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Menyenaraikan ciri server

Sekarang, kita mempunyai klien yang boleh menyambung jika program dijalankan. Walau bagaimanapun, ia tidak benar-benar menyenaraikan cirinya, jadi mari kita lakukan itu seterusnya:

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

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
```

Di sini kita menyenaraikan sumber yang tersedia, `list_resources()` dan alat, `list_tools` dan mencetaknya.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Di atas adalah contoh bagaimana kita boleh menyenaraikan alat pada server. Untuk setiap alat, kita kemudian mencetak namanya.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Dalam kod di atas, kita telah:

- Memanggil `listTools()` untuk mendapatkan semua alat yang tersedia dari MCP Server.
- Menggunakan `ping()` untuk mengesahkan bahawa sambungan ke server berfungsi.
- `ListToolsResult` mengandungi maklumat tentang semua alat termasuk nama, deskripsi, dan skema input mereka.

Bagus, sekarang kita telah menangkap semua ciri. Persoalannya sekarang ialah bila kita menggunakannya? Klien ini agak mudah, mudah dalam erti kata bahawa kita perlu secara eksplisit memanggil ciri apabila kita mahu. Dalam bab seterusnya, kita akan mencipta klien yang lebih maju yang mempunyai akses kepada model bahasa besar (LLM) sendiri. Buat masa ini, mari kita lihat bagaimana kita boleh memanggil ciri pada server:

#### Rust

Dalam fungsi utama, selepas memulakan klien, kita boleh memulakan server dan menyenaraikan beberapa cirinya.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Memanggil ciri

Untuk memanggil ciri, kita perlu memastikan kita menentukan argumen yang betul dan dalam beberapa kes nama apa yang kita cuba panggil.

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Dalam kod di atas, kita:

- Membaca sumber, kita memanggil sumber dengan memanggil `readResource()` dan menentukan `uri`. Inilah yang mungkin kelihatan di sisi server:

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    Nilai `uri` kita `file://example.txt` sepadan dengan `file://{name}` pada server. `example.txt` akan dipetakan kepada `name`.

- Memanggil alat, kita memanggilnya dengan menentukan `name` dan `arguments` seperti berikut:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Mendapatkan arahan, untuk mendapatkan arahan, anda memanggil `getPrompt()` dengan `name` dan `arguments`. Kod server kelihatan seperti berikut:

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    dan kod klien anda kelihatan seperti berikut untuk sepadan dengan apa yang diisytiharkan pada server:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Dalam kod di atas, kita telah:

- Memanggil sumber bernama `greeting` menggunakan `read_resource`.
- Memanggil alat bernama `add` menggunakan `call_tool`.

#### .NET

1. Mari tambahkan kod untuk memanggil alat:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Untuk mencetak hasilnya, berikut adalah kod untuk mengendalikannya:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

Dalam kod di atas, kita telah:

- Memanggil beberapa alat kalkulator menggunakan kaedah `callTool()` dengan objek `CallToolRequest`.
- Setiap panggilan alat menentukan nama alat dan `Map` argumen yang diperlukan oleh alat tersebut.
- Alat server mengharapkan nama parameter tertentu (seperti "a", "b" untuk operasi matematik).
- Hasil dikembalikan sebagai objek `CallToolResult` yang mengandungi respons dari server.

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- Menjalankan klien

Untuk menjalankan klien, taipkan perintah berikut di terminal:

#### TypeScript

Tambahkan entri berikut ke bahagian "scripts" dalam *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Panggil klien dengan perintah berikut:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Pertama, pastikan MCP Server anda berjalan di `http://localhost:8080`. Kemudian jalankan klien:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Sebagai alternatif, anda boleh menjalankan projek klien lengkap yang disediakan dalam folder penyelesaian `03-GettingStarted\02-client\solution\java`:

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Tugasan

Dalam tugasan ini, anda akan menggunakan apa yang telah anda pelajari dalam mencipta klien tetapi mencipta klien anda sendiri.

Berikut adalah server yang boleh anda gunakan yang perlu anda panggil melalui kod klien anda, lihat jika anda boleh menambahkan lebih banyak ciri ke server untuk menjadikannya lebih menarik.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Start receiving messages on stdin and sending messages on stdout

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

Lihat projek ini untuk melihat bagaimana anda boleh [menambahkan arahan dan sumber](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Juga, periksa pautan ini untuk cara memanggil [arahan dan sumber](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Dalam [bahagian sebelumnya](../../../../03-GettingStarted/01-first-server), anda telah belajar cara mencipta MCP Server sederhana dengan Rust. Anda boleh terus membina di atasnya atau periksa pautan ini untuk lebih banyak contoh MCP Server berasaskan Rust: [Contoh MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Penyelesaian

Folder **penyelesaian** mengandungi implementasi klien lengkap yang siap dijalankan yang menunjukkan semua konsep yang dibahas dalam tutorial ini. Setiap penyelesaian termasuk kod klien dan server yang diatur dalam projek yang terpisah dan mandiri.

### 📁 Struktur Penyelesaian

Direktori penyelesaian diatur mengikut bahasa pengaturcaraan:

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 Apa yang Termasuk dalam Setiap Penyelesaian

Setiap penyelesaian khusus bahasa menyediakan:

- **Implementasi klien lengkap** dengan semua ciri dari tutorial.
- **Struktur projek yang berfungsi** dengan kebergantungan dan konfigurasi yang betul.
- **Skrip binaan dan jalankan** untuk penyediaan dan pelaksanaan yang mudah.
- **README terperinci** dengan arahan khusus bahasa.
- **Contoh pengendalian kesalahan** dan pemprosesan hasil.

### 📖 Menggunakan Penyelesaian

1. **Navigasi ke folder bahasa pilihan anda**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Ikuti arahan README** dalam setiap folder untuk:
   - Memasang kebergantungan.
   - Membina projek.
   - Menjalankan klien.

3. **Contoh output** yang sepatutnya anda lihat:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Untuk dokumentasi lengkap dan arahan langkah demi langkah, lihat: **[📖 Dokumentasi Penyelesaian](./solution/README.md)**

## 🎯 Contoh Lengkap

Kami telah menyediakan implementasi klien lengkap yang berfungsi untuk semua bahasa pengaturcaraan yang dibahas dalam tutorial ini. Contoh-contoh ini menunjukkan fungsi penuh yang dijelaskan di atas dan boleh digunakan sebagai implementasi rujukan atau titik permulaan untuk projek anda sendiri.

### Contoh Lengkap yang Tersedia

| Bahasa | Fail | Deskripsi |
|--------|------|-----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Klien Java lengkap menggunakan pengangkutan SSE dengan pengendalian kesalahan yang komprehensif |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Klien C# lengkap menggunakan pengangkutan stdio dengan permulaan server automatik |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Klien TypeScript lengkap dengan sokongan penuh protokol MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Klien Python lengkap menggunakan corak async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Klien Rust lengkap menggunakan Tokio untuk operasi async |
Setiap contoh lengkap merangkumi:

- ✅ **Penyambungan sambungan** dan pengendalian ralat
- ✅ **Penemuan pelayan** (alat, sumber, arahan di mana sesuai)
- ✅ **Operasi kalkulator** (tambah, tolak, darab, bahagi, bantuan)
- ✅ **Pemprosesan hasil** dan output yang diformat
- ✅ **Pengendalian ralat yang menyeluruh**
- ✅ **Kod yang bersih dan didokumentasikan** dengan komen langkah demi langkah

### Memulakan dengan Contoh Lengkap

1. **Pilih bahasa pilihan anda** daripada jadual di atas
2. **Semak fail contoh lengkap** untuk memahami pelaksanaan penuh
3. **Jalankan contoh** mengikut arahan dalam [`complete_examples.md`](./complete_examples.md)
4. **Ubah suai dan kembangkan** contoh untuk kes penggunaan spesifik anda

Untuk dokumentasi terperinci tentang menjalankan dan menyesuaikan contoh ini, lihat: **[📖 Dokumentasi Contoh Lengkap](./complete_examples.md)**

### 💡 Penyelesaian vs. Contoh Lengkap

| **Folder Penyelesaian** | **Contoh Lengkap** |
|-------------------------|--------------------|
| Struktur projek penuh dengan fail binaan | Pelaksanaan dalam satu fail |
| Sedia dijalankan dengan kebergantungan | Contoh kod yang fokus |
| Persediaan seperti produksi | Rujukan pendidikan |
| Alat khusus bahasa | Perbandingan antara bahasa |

Kedua-dua pendekatan ini bernilai - gunakan **folder penyelesaian** untuk projek lengkap dan **contoh lengkap** untuk pembelajaran dan rujukan.

## Perkara Penting

Perkara penting untuk bab ini adalah seperti berikut tentang klien:

- Boleh digunakan untuk kedua-dua penemuan dan pelaksanaan ciri pada pelayan.
- Boleh memulakan pelayan semasa ia bermula sendiri (seperti dalam bab ini) tetapi klien juga boleh menyambung ke pelayan yang sedang berjalan.
- Merupakan cara yang hebat untuk menguji keupayaan pelayan berbanding alternatif seperti Inspector seperti yang diterangkan dalam bab sebelumnya.

## Sumber Tambahan

- [Membina klien dalam MCP](https://modelcontextprotocol.io/quickstart/client)

## Sampel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Apa Seterusnya

- Seterusnya: [Membuat klien dengan LLM](../03-llm-client/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.