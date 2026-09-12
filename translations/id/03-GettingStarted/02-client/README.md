# Membuat klien

Klien adalah aplikasi khusus atau skrip yang berkomunikasi langsung dengan Server MCP untuk meminta sumber daya, alat, dan prompt. Berbeda dengan menggunakan alat inspector yang menyediakan antarmuka grafis untuk berinteraksi dengan server, menulis klien Anda sendiri memungkinkan interaksi secara programatik dan otomatis. Ini memungkinkan pengembang mengintegrasikan kemampuan MCP ke dalam alur kerja mereka sendiri, mengotomatisasi tugas, dan membangun solusi khusus yang disesuaikan dengan kebutuhan tertentu.

## Ikhtisar

Pelajaran ini memperkenalkan konsep klien dalam ekosistem Model Context Protocol (MCP). Anda akan belajar bagaimana menulis klien Anda sendiri dan menghubungkannya ke Server MCP.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Memahami apa yang bisa dilakukan klien.
- Menulis klien Anda sendiri.
- Menghubungkan dan menguji klien dengan server MCP untuk memastikan semuanya bekerja sebagaimana mestinya.

## Apa saja yang diperlukan untuk menulis klien?

Untuk menulis klien, Anda perlu melakukan hal-hal berikut:

- **Impor pustaka yang benar**. Anda akan menggunakan pustaka yang sama seperti sebelumnya, hanya dengan konstruksi berbeda.
- **Instansiasi klien**. Ini melibatkan pembuatan instance klien dan menghubungkannya ke metode transportasi yang dipilih.
- **Memutuskan sumber daya apa yang akan didaftarkan**. Server MCP Anda menyediakan sumber daya, alat, dan prompt, Anda perlu menentukan mana yang akan didaftarkan.
- **Mengintegrasikan klien ke aplikasi host**. Setelah mengetahui kemampuan server, Anda perlu mengintegrasikannya ke aplikasi host sehingga ketika pengguna mengetik prompt atau perintah lain, fitur yang sesuai pada server dipanggil.

Sekarang kita telah memahami secara garis besar apa yang akan kita lakukan, mari lihat contoh berikutnya.

### Contoh klien

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

// Daftar prompt
const prompts = await client.listPrompts();

// Dapatkan sebuah prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Daftar sumber daya
const resources = await client.listResources();

// Baca sebuah sumber daya
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Panggil sebuah alat
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Dalam kode sebelumnya kita:

- Mengimpor pustaka
- Membuat instance klien dan menghubungkannya menggunakan stdio sebagai transportasi.
- Mendaftar prompt, sumber daya, dan alat lalu memanggil semuanya.

Itu dia, sebuah klien yang dapat berbicara dengan Server MCP.

Mari kita luangkan waktu di bagian latihan berikutnya untuk menguraikan setiap potongan kode dan menjelaskan apa yang terjadi.

## Latihan: Menulis klien

Seperti yang dikatakan di atas, mari kita jelaskan kode ini dengan seksama, dan silakan ikut koding jika Anda mau.

### -1- Impor pustaka

Mari kita impor pustaka yang kita butuhkan, kita akan membutuhkan referensi ke klien dan ke protokol transportasi yang dipilih, stdio. stdio adalah protokol untuk hal-hal yang dijalankan pada mesin lokal Anda. SSE adalah protokol transportasi lain yang akan kita tunjukkan di bab berikutnya tapi itu opsi lain Anda. Untuk sekarang, mari lanjutkan dengan stdio.

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
```

#### Java

Untuk Java, Anda akan membuat klien yang menghubungkan ke server MCP dari latihan sebelumnya. Menggunakan struktur proyek Java Spring Boot yang sama dari [Memulai dengan Server MCP](../../../../03-GettingStarted/01-first-server/solution/java), buat kelas Java baru bernama `SDKClient` di folder `src/main/java/com/microsoft/mcp/sample/client/` dan tambahkan impor berikut:

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

Anda perlu menambahkan dependensi berikut pada file `Cargo.toml` Anda.

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

Dari sana, Anda dapat mengimpor pustaka yang diperlukan di kode klien Anda.

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

### -2- Instansiasi klien dan transportasi

Kita perlu membuat instance transportasi dan juga instance klien kita:

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

Dalam kode sebelumnya kita telah:

- Membuat instance transportasi stdio. Perhatikan bagaimana perintah dan argumen untuk menemukan dan memulai server ditentukan karena itu perlu kita lakukan saat membuat klien.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Menginstansiasi klien dengan memberikan nama dan versi.

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

Dalam kode sebelumnya kita telah:

- Mengimpor pustaka yang diperlukan
- Menginstansiasi objek parameter server untuk menjalankan server agar kita bisa menghubunginya dengan klien kita.
- Mendefinisikan metode `run` yang pada gilirannya memanggil `stdio_client` untuk memulai sesi klien.
- Membuat titik masuk tempat kita menyediakan metode `run` ke `asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

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

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

Dalam kode sebelumnya kita telah:

- Mengimpor pustaka yang diperlukan.
- Membuat transportasi stdio dan membuat klien `mcpClient`. Ini akan kita gunakan untuk mendaftar dan memanggil fitur pada Server MCP.

Catatan, pada "Arguments", Anda dapat menunjuk ke *.csproj* atau ke executable.

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
        
        // Logika klien Anda ditulis di sini
    }
}
```

Dalam kode sebelumnya kita telah:

- Membuat metode utama yang mengatur transportasi SSE menunjuk ke `http://localhost:8080` di mana server MCP kita akan berjalan.
- Membuat kelas klien yang menerima transportasi sebagai parameter konstruktor.
- Dalam metode `run`, kita membuat klien MCP sinkron menggunakan transportasi dan menginisialisasi koneksi.
- Menggunakan SSE (Server-Sent Events) transportasi yang cocok untuk komunikasi berbasis HTTP dengan server MCP Java Spring Boot.

#### Rust

Perlu diperhatikan klien Rust ini mengasumsikan server adalah proyek saudara bernama "calculator-server" dalam direktori yang sama. Kode berikut akan memulai server dan menghubungkan ke sana.

```rust
async fn main() -> Result<(), RmcpError> {
    // Asumsikan server adalah proyek saudara bernama "calculator-server" di direktori yang sama
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

    // TODO: Inisialisasi

    // TODO: Daftar alat

    // TODO: Panggil alat tambah dengan argumen = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Mendaftar fitur server

Sekarang, kita punya klien yang bisa terhubung saat program dijalankan. Namun, klien ini belum mendaftar fitur-fiturnya, mari kita lakukan itu:

#### TypeScript

```typescript
// Daftar prompt
const prompts = await client.listPrompts();

// Daftar sumber daya
const resources = await client.listResources();

// daftar alat
const tools = await client.listTools();
```

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
```

Di sini kita daftar sumber daya yang tersedia, `list_resources()` dan alat, `list_tools` lalu mencetaknya.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Di atas adalah contoh bagaimana kita bisa mendaftar alat pada server. Untuk setiap alat, kita cetak namanya.

#### Java

```java
// Daftar dan demonstrasikan alat
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Anda juga dapat melakukan ping ke server untuk memverifikasi koneksi
client.ping();
```

Dalam kode sebelumnya kita telah:

- Memanggil `listTools()` untuk mendapatkan semua alat yang tersedia dari server MCP.
- Menggunakan `ping()` untuk memverifikasi koneksi ke server berfungsi.
- `ListToolsResult` berisi informasi tentang semua alat termasuk nama, deskripsi, dan skema input.

Bagus, kini kita telah menangkap semua fitur. Pertanyaan sekarang kapan kita gunakan fitur tersebut? Klien ini cukup sederhana, artinya kita perlu memanggil fitur tersebut secara eksplisit saat ingin menggunakannya. Pada bab berikutnya, kita akan membuat klien yang lebih maju yang memiliki akses ke model bahasa besar sendiri, LLM. Untuk sekarang, mari kita lihat bagaimana memanggil fitur pada server:

#### Rust

Dalam fungsi utama, setelah menginisialisasi klien, kita bisa menginisialisasi server dan mendaftar beberapa fiturnya.

```rust
// Inisialisasi
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Daftar alat
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Memanggil fitur

Untuk memanggil fitur kita harus memastikan menentukan argumen yang benar dan dalam beberapa kasus nama fitur yang akan dipanggil.

#### TypeScript

```typescript

// Baca sebuah sumber daya
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Panggil sebuah alat
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// panggil prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Dalam kode sebelumnya kita:

- Membaca sumber daya, kita memanggil sumber daya dengan memanggil `readResource()` dengan parameter `uri`. Berikut kira-kira seperti apa di sisi server:

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

- Memanggil alat, kita panggil dengan menentukan `name` dan `arguments` seperti ini:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Mengambil prompt, untuk mendapatkan prompt, panggil `getPrompt()` dengan `name` dan `arguments`. Kode servernya seperti ini:

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

    sehingga kode klien Anda akan tampak seperti ini agar cocok dengan deklarasi di server:

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
# Baca sebuah sumber daya
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Panggil sebuah alat
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Dalam kode sebelumnya kita telah:

- Memanggil sumber daya bernama `greeting` menggunakan `read_resource`.
- Memanggil alat bernama `add` menggunakan `call_tool`.

#### .NET

1. Mari tambahkan kode untuk memanggil alat:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Untuk menampilkan hasil, ini adalah kode untuk menanganinya:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Memanggil berbagai alat kalkulator
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

Dalam kode sebelumnya kita telah:

- Memanggil beberapa alat kalkulator menggunakan metode `callTool()` dengan objek `CallToolRequest`.
- Setiap panggilan alat menentukan nama alat dan `Map` argumen yang dibutuhkan alat tersebut.
- Alat server mengharapkan nama parameter khusus (seperti "a", "b" untuk operasi matematika).
- Hasil dikembalikan sebagai objek `CallToolResult` yang berisi respons dari server.

#### Rust

```rust
// Panggil alat tambah dengan argumen = {"a": 3, "b": 2}
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

Tambahkan entri berikut ke bagian "scripts" pada *package.json* Anda:

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

Pastikan server MCP Anda berjalan di `http://localhost:8080`. Kemudian jalankan klien:

```bash
# Bangun proyek Anda
./mvnw clean compile

# Jalankan klien
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatifnya, Anda dapat menjalankan proyek klien lengkap yang disediakan di folder solusi `03-GettingStarted\02-client\solution\java`:

```bash
# Navigasi ke direktori solusi
cd 03-GettingStarted/02-client/solution/java

# Bangun dan jalankan JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Tugas

Dalam tugas ini, Anda akan menggunakan apa yang telah Anda pelajari dalam membuat klien, tapi buat klien Anda sendiri.

Ini adalah server yang dapat Anda gunakan dan harus Anda panggil melalui kode klien Anda, coba lihat apakah Anda bisa menambahkan lebih banyak fitur ke server ini agar lebih menarik.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Buat server MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Tambahkan alat penjumlahan
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Tambahkan sumber sapaan dinamis
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

// Mulai menerima pesan di stdin dan mengirim pesan di stdout

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

# Buat server MCP
mcp = FastMCP("Demo")


# Tambahkan alat penjumlahan
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Tambahkan sumber sapaan dinamis
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

Lihat proyek ini untuk bagaimana Anda bisa [menambahkan prompt dan sumber daya](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Juga, cek tautan ini untuk bagaimana memanggil [prompt dan sumber daya](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Di [bagian sebelumnya](../../../../03-GettingStarted/01-first-server), Anda belajar bagaimana membuat server MCP sederhana dengan Rust. Anda bisa melanjutkan membangun dari situ atau lihat tautan ini untuk contoh server MCP berbasis Rust lainnya: [Contoh Server MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solusi

Folder **solusi** berisi implementasi klien lengkap yang siap dijalankan dan mendemonstrasikan semua konsep yang dibahas dalam tutorial ini. Setiap solusi mencakup kode klien dan server yang diorganisir dalam proyek terpisah yang berdiri sendiri.

### 📁 Struktur Solusi

Direktori solusi diorganisir berdasarkan bahasa pemrograman:

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
- **Struktur proyek yang bekerja** dengan dependensi dan konfigurasi yang tepat
- **Skrip bangun dan jalankan** untuk kemudahan pengaturan dan eksekusi
- **README detil** dengan instruksi spesifik bahasa
- **Contoh penanganan error** dan pemrosesan hasil

### 📖 Menggunakan Solusi

1. **Navigasi ke folder bahasa pilihan Anda**:

   ```bash
   cd solution/typescript/    # Untuk TypeScript
   cd solution/java/          # Untuk Java
   cd solution/python/        # Untuk Python
   cd solution/dotnet/        # Untuk .NET
   ```

2. **Ikuti instruksi README** di setiap folder untuk:
   - Menginstal dependensi
   - Membangun proyek
   - Menjalankan klien

3. **Output contoh** yang seharusnya Anda lihat:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Untuk dokumentasi lengkap dan instruksi langkah demi langkah, lihat: **[📖 Dokumentasi Solusi](./solution/README.md)**

## 🎯 Contoh Lengkap

Kami menyediakan implementasi klien yang lengkap dan berfungsi untuk semua bahasa pemrograman yang dibahas dalam tutorial ini. Contoh-contoh ini mendemonstrasikan fungsi penuh sebagaimana dijelaskan di atas dan dapat digunakan sebagai referensi implementasi atau sebagai titik awal proyek Anda sendiri.

### Contoh Lengkap yang Tersedia

| Bahasa | File | Deskripsi |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Klien Java lengkap menggunakan transportasi SSE dengan penanganan error komprehensif |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Klien C# lengkap menggunakan transportasi stdio dengan startup server otomatis |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Klien TypeScript lengkap dengan dukungan penuh protokol MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Klien Python lengkap menggunakan pola async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Klien Rust lengkap menggunakan Tokio untuk operasi async |

Setiap contoh lengkap mencakup:

- ✅ **Pembentukan koneksi** dan penanganan error
- ✅ **Penemuan server** (alat, sumber daya, prompt jika tersedia)
- ✅ **Operasi kalkulator** (tambah, kurang, kali, bagi, bantuan)
- ✅ **Pemrosesan hasil** dan output terformat
- ✅ **Penanganan error lengkap**

- ✅ **Kode bersih dan terdokumentasi** dengan komentar langkah demi langkah

### Memulai dengan Contoh Lengkap

1. **Pilih bahasa yang Anda inginkan** dari tabel di atas
2. **Tinjau file contoh lengkap** untuk memahami implementasi secara penuh
3. **Jalankan contoh** mengikuti instruksi di [`complete_examples.md`](./complete_examples.md)
4. **Modifikasi dan perluas** contoh untuk penggunaan spesifik Anda

Untuk dokumentasi rinci tentang menjalankan dan menyesuaikan contoh-contoh ini, lihat: **[📖 Dokumentasi Contoh Lengkap](./complete_examples.md)**

### 💡 Solusi vs. Contoh Lengkap

| **Folder Solusi** | **Contoh Lengkap** |
|--------------------|--------------------- |
| Struktur proyek penuh dengan file build | Implementasi satu file |
| Siap dijalankan dengan dependensi | Contoh kode terfokus |
| Pengaturan seperti produksi | Referensi edukasi |
| Tooling spesifik bahasa | Perbandingan lintas bahasa |

Kedua pendekatan bernilai - gunakan **folder solusi** untuk proyek lengkap dan **contoh lengkap** untuk pembelajaran dan referensi.

## Poin Penting

Poin penting untuk bab ini mengenai klien adalah sebagai berikut:

- Dapat digunakan untuk menemukan dan memanggil fitur di server.
- Dapat memulai server saat mereka memulai sendiri (seperti di bab ini) tetapi klien juga dapat terhubung ke server yang sudah berjalan.
- Merupakan cara yang bagus untuk menguji kemampuan server selain alternatif seperti Inspector seperti yang dijelaskan di bab sebelumnya.

## Sumber Daya Tambahan

- [Membangun klien di MCP](https://modelcontextprotocol.io/quickstart/client)

## Contoh

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .NET](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)
- [Kalkulator Rust](../../../../03-GettingStarted/samples/rust)

## Selanjutnya

- Selanjutnya: [Membuat klien dengan LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->