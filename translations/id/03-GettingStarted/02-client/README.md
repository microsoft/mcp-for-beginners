# Membuat Klien

Klien adalah aplikasi atau skrip khusus yang berkomunikasi langsung dengan MCP Server untuk meminta sumber daya, alat, dan prompt. Berbeda dengan menggunakan alat inspeksi yang menyediakan antarmuka grafis untuk berinteraksi dengan server, menulis klien sendiri memungkinkan interaksi yang terprogram dan otomatis. Hal ini memungkinkan pengembang untuk mengintegrasikan kemampuan MCP ke dalam alur kerja mereka sendiri, mengotomatisasi tugas, dan membangun solusi khusus yang disesuaikan dengan kebutuhan tertentu.

## Gambaran Umum

Pelajaran ini memperkenalkan konsep klien dalam ekosistem Model Context Protocol (MCP). Anda akan belajar cara menulis klien sendiri dan menghubungkannya ke MCP Server.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Memahami apa yang dapat dilakukan oleh klien.
- Menulis klien sendiri.
- Menghubungkan dan menguji klien dengan MCP Server untuk memastikan server berfungsi sebagaimana mestinya.

## Apa saja yang diperlukan untuk menulis klien?

Untuk menulis klien, Anda perlu melakukan hal berikut:

- **Mengimpor pustaka yang benar**. Anda akan menggunakan pustaka yang sama seperti sebelumnya, hanya saja dengan konstruksi yang berbeda.
- **Membuat instans klien**. Ini melibatkan pembuatan instans klien dan menghubungkannya ke metode transportasi yang dipilih.
- **Memutuskan sumber daya apa yang akan didaftarkan**. MCP Server Anda memiliki sumber daya, alat, dan prompt; Anda perlu memutuskan mana yang akan didaftarkan.
- **Mengintegrasikan klien ke aplikasi host**. Setelah Anda mengetahui kemampuan server, Anda perlu mengintegrasikannya ke aplikasi host Anda sehingga jika pengguna mengetikkan prompt atau perintah lain, fitur server yang sesuai akan dipanggil.

Sekarang kita memahami secara garis besar apa yang akan kita lakukan, mari kita lihat contohnya berikutnya.

### Contoh Klien

Mari kita lihat contoh klien berikut:

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

Dalam kode di atas, kita:

- Mengimpor pustaka
- Membuat instans klien dan menghubungkannya menggunakan stdio untuk transportasi.
- Mendaftarkan prompt, sumber daya, dan alat, lalu memanggil semuanya.

Itulah klien yang dapat berkomunikasi dengan MCP Server.

Mari kita luangkan waktu di bagian latihan berikutnya untuk memecah setiap cuplikan kode dan menjelaskan apa yang sedang terjadi.

## Latihan: Menulis Klien

Seperti yang disebutkan di atas, mari kita luangkan waktu untuk menjelaskan kode, dan jika Anda ingin, silakan kode bersama.

### -1- Mengimpor pustaka

Mari kita impor pustaka yang kita butuhkan. Kita akan membutuhkan referensi ke klien dan protokol transportasi yang dipilih, stdio. Stdio adalah protokol untuk hal-hal yang dirancang untuk dijalankan di mesin lokal Anda. SSE adalah protokol transportasi lain yang akan kita tunjukkan di bab-bab berikutnya, tetapi itu adalah opsi lain Anda. Untuk saat ini, mari kita lanjutkan dengan stdio.

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

Untuk Java, Anda akan membuat klien yang terhubung ke MCP Server dari latihan sebelumnya. Menggunakan struktur proyek Java Spring Boot yang sama dari [Memulai dengan MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), buat kelas Java baru bernama `SDKClient` di folder `src/main/java/com/microsoft/mcp/sample/client/` dan tambahkan impor berikut:

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

Anda perlu menambahkan dependensi berikut ke file `Cargo.toml` Anda.

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

Dari sana, Anda dapat mengimpor pustaka yang diperlukan dalam kode klien Anda.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Mari kita lanjutkan ke instansiasi.

### -2- Membuat instans klien dan transportasi

Kita perlu membuat instans transportasi dan instans klien kita:

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

Dalam kode di atas, kita:

- Membuat instans transportasi stdio. Perhatikan bagaimana ia menentukan perintah dan argumen untuk menemukan dan memulai server karena itu adalah sesuatu yang perlu kita lakukan saat membuat klien.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Membuat instans klien dengan memberikan nama dan versi.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Menghubungkan klien ke transportasi yang dipilih.

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

Dalam kode di atas, kita:

- Mengimpor pustaka yang diperlukan.
- Membuat objek parameter server karena kita akan menggunakannya untuk menjalankan server sehingga kita dapat terhubung dengannya dengan klien kita.
- Mendefinisikan metode `run` yang pada gilirannya memanggil `stdio_client` yang memulai sesi klien.
- Membuat titik masuk di mana kita menyediakan metode `run` ke `asyncio.run`.

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

Dalam kode di atas, kita:

- Mengimpor pustaka yang diperlukan.
- Membuat transportasi stdio dan membuat klien `mcpClient`. Yang terakhir adalah sesuatu yang akan kita gunakan untuk mendaftarkan dan memanggil fitur di MCP Server.

Catatan, dalam "Arguments", Anda dapat menunjuk ke *.csproj* atau ke executable.

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

Dalam kode di atas, kita:

- Membuat metode utama yang mengatur transportasi SSE yang menunjuk ke `http://localhost:8080` di mana MCP Server kita akan berjalan.
- Membuat kelas klien yang mengambil transportasi sebagai parameter konstruktor.
- Dalam metode `run`, kita membuat klien MCP sinkron menggunakan transportasi dan menginisialisasi koneksi.
- Menggunakan transportasi SSE (Server-Sent Events) yang cocok untuk komunikasi berbasis HTTP dengan MCP Server Java Spring Boot.

#### Rust

Catatan klien Rust ini mengasumsikan server adalah proyek saudara bernama "calculator-server" di direktori yang sama. Kode di bawah ini akan memulai server dan terhubung dengannya.

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

### -3- Mendaftarkan fitur server

Sekarang, kita memiliki klien yang dapat terhubung jika program dijalankan. Namun, klien ini belum mendaftarkan fiturnya, jadi mari kita lakukan itu selanjutnya:

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

Di sini kita mendaftarkan sumber daya yang tersedia, `list_resources()` dan alat, `list_tools` lalu mencetaknya.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Di atas adalah contoh bagaimana kita dapat mendaftarkan alat di server. Untuk setiap alat, kita kemudian mencetak namanya.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Dalam kode di atas, kita:

- Memanggil `listTools()` untuk mendapatkan semua alat yang tersedia dari MCP Server.
- Menggunakan `ping()` untuk memverifikasi bahwa koneksi ke server berfungsi.
- `ListToolsResult` berisi informasi tentang semua alat termasuk nama, deskripsi, dan skema inputnya.

Bagus, sekarang kita telah menangkap semua fitur. Pertanyaannya adalah kapan kita menggunakannya? Nah, klien ini cukup sederhana, sederhana dalam arti bahwa kita perlu secara eksplisit memanggil fitur saat kita menginginkannya. Di bab berikutnya, kita akan membuat klien yang lebih canggih yang memiliki akses ke model bahasa besar (LLM) sendiri. Untuk saat ini, mari kita lihat bagaimana kita dapat memanggil fitur di server:

#### Rust

Dalam fungsi utama, setelah menginisialisasi klien, kita dapat menginisialisasi server dan mendaftarkan beberapa fiturnya.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Memanggil fitur

Untuk memanggil fitur, kita perlu memastikan kita menentukan argumen yang benar dan dalam beberapa kasus nama dari apa yang kita coba panggil.

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

Dalam kode di atas, kita:

- Membaca sumber daya, kita memanggil sumber daya dengan memanggil `readResource()` dan menentukan `uri`. Berikut adalah tampilan server:

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

    Nilai `uri` kita `file://example.txt` cocok dengan `file://{name}` di server. `example.txt` akan dipetakan ke `name`.

- Memanggil alat, kita memanggilnya dengan menentukan `name` dan `arguments` seperti ini:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Mendapatkan prompt, untuk mendapatkan prompt, Anda memanggil `getPrompt()` dengan `name` dan `arguments`. Kode server terlihat seperti ini:

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

    dan kode klien Anda akan terlihat seperti ini untuk mencocokkan apa yang dideklarasikan di server:

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

Dalam kode di atas, kita:

- Memanggil sumber daya bernama `greeting` menggunakan `read_resource`.
- Memanggil alat bernama `add` menggunakan `call_tool`.

#### .NET

1. Tambahkan kode untuk memanggil alat:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Untuk mencetak hasilnya, berikut adalah kode untuk menangani itu:

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

Dalam kode di atas, kita:

- Memanggil beberapa alat kalkulator menggunakan metode `callTool()` dengan objek `CallToolRequest`.
- Setiap panggilan alat menentukan nama alat dan `Map` argumen yang diperlukan oleh alat tersebut.
- Alat server mengharapkan nama parameter tertentu (seperti "a", "b" untuk operasi matematika).
- Hasil dikembalikan sebagai objek `CallToolResult` yang berisi respons dari server.

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

Untuk menjalankan klien, ketik perintah berikut di terminal:

#### TypeScript

Tambahkan entri berikut ke bagian "scripts" di *package.json*:

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

Pertama, pastikan MCP Server Anda berjalan di `http://localhost:8080`. Kemudian jalankan klien:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Sebagai alternatif, Anda dapat menjalankan proyek klien lengkap yang disediakan di folder solusi `03-GettingStarted\02-client\solution\java`:

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

## Tugas

Dalam tugas ini, Anda akan menggunakan apa yang telah Anda pelajari dalam membuat klien tetapi membuat klien Anda sendiri.

Berikut adalah server yang dapat Anda gunakan yang perlu Anda panggil melalui kode klien Anda, lihat apakah Anda dapat menambahkan lebih banyak fitur ke server untuk membuatnya lebih menarik.

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

Lihat proyek ini untuk melihat bagaimana Anda dapat [menambahkan prompt dan sumber daya](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Juga, periksa tautan ini untuk cara memanggil [prompt dan sumber daya](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Di [bagian sebelumnya](../../../../03-GettingStarted/01-first-server), Anda belajar cara membuat MCP Server sederhana dengan Rust. Anda dapat melanjutkan membangun di atas itu atau memeriksa tautan ini untuk lebih banyak contoh MCP Server berbasis Rust: [Contoh MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solusi

Folder **solusi** berisi implementasi klien lengkap yang siap dijalankan yang menunjukkan semua konsep yang dibahas dalam tutorial ini. Setiap solusi mencakup kode klien dan server yang diorganisasi dalam proyek terpisah dan mandiri.

### 📁 Struktur Solusi

Direktori solusi diorganisasi berdasarkan bahasa pemrograman:

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

### 🚀 Apa yang Termasuk dalam Setiap Solusi

Setiap solusi spesifik bahasa menyediakan:

- **Implementasi klien lengkap** dengan semua fitur dari tutorial
- **Struktur proyek yang berfungsi** dengan dependensi dan konfigurasi yang tepat
- **Skrip build dan run** untuk pengaturan dan eksekusi yang mudah
- **README yang terperinci** dengan instruksi spesifik bahasa
- **Contoh penanganan error** dan pemrosesan hasil

### 📖 Menggunakan Solusi

1. **Navigasikan ke folder bahasa pilihan Anda**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Ikuti instruksi README** di setiap folder untuk:
   - Menginstal dependensi
   - Membuat proyek
   - Menjalankan klien

3. **Output contoh** yang harus Anda lihat:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Untuk dokumentasi lengkap dan instruksi langkah demi langkah, lihat: **[📖 Dokumentasi Solusi](./solution/README.md)**

## 🎯 Contoh Lengkap

Kami telah menyediakan implementasi klien lengkap yang berfungsi untuk semua bahasa pemrograman yang dibahas dalam tutorial ini. Contoh-contoh ini menunjukkan fungsionalitas penuh yang dijelaskan di atas dan dapat digunakan sebagai implementasi referensi atau titik awal untuk proyek Anda sendiri.

### Contoh Lengkap yang Tersedia

| Bahasa | File | Deskripsi |
|--------|------|-----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Klien Java lengkap menggunakan transportasi SSE dengan penanganan error yang komprehensif |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Klien C# lengkap menggunakan transportasi stdio dengan startup server otomatis |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Klien TypeScript lengkap dengan dukungan penuh protokol MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Klien Python lengkap menggunakan pola async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Klien Rust lengkap menggunakan Tokio untuk operasi async |
Setiap contoh lengkap mencakup:

- ✅ **Pembuatan koneksi** dan penanganan kesalahan
- ✅ **Penemuan server** (alat, sumber daya, prompt jika berlaku)
- ✅ **Operasi kalkulator** (tambah, kurang, kali, bagi, bantuan)
- ✅ **Pemrosesan hasil** dan output yang diformat
- ✅ **Penanganan kesalahan yang komprehensif**
- ✅ **Kode yang bersih dan terdokumentasi** dengan komentar langkah demi langkah

### Memulai dengan Contoh Lengkap

1. **Pilih bahasa yang Anda inginkan** dari tabel di atas
2. **Tinjau file contoh lengkap** untuk memahami implementasi secara menyeluruh
3. **Jalankan contoh** sesuai instruksi dalam [`complete_examples.md`](./complete_examples.md)
4. **Modifikasi dan kembangkan** contoh untuk kebutuhan spesifik Anda

Untuk dokumentasi terperinci tentang menjalankan dan menyesuaikan contoh ini, lihat: **[📖 Dokumentasi Contoh Lengkap](./complete_examples.md)**

### 💡 Solusi vs. Contoh Lengkap

| **Folder Solusi** | **Contoh Lengkap** |
|--------------------|--------------------- |
| Struktur proyek lengkap dengan file build | Implementasi dalam satu file |
| Siap dijalankan dengan dependensi | Contoh kode yang terfokus |
| Pengaturan mirip produksi | Referensi edukasi |
| Alat khusus bahasa | Perbandingan lintas bahasa |

Kedua pendekatan ini memiliki nilai - gunakan **folder solusi** untuk proyek lengkap dan **contoh lengkap** untuk pembelajaran dan referensi.

## Poin Penting

Poin penting dari bab ini tentang klien adalah sebagai berikut:

- Dapat digunakan untuk menemukan dan memanfaatkan fitur pada server.
- Dapat memulai server saat dirinya sendiri mulai (seperti dalam bab ini), tetapi klien juga dapat terhubung ke server yang sudah berjalan.
- Merupakan cara yang bagus untuk menguji kemampuan server selain alternatif seperti Inspector yang dijelaskan di bab sebelumnya.

## Sumber Daya Tambahan

- [Membangun klien di MCP](https://modelcontextprotocol.io/quickstart/client)

## Contoh

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Selanjutnya

- Berikutnya: [Membuat klien dengan LLM](../03-llm-client/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.