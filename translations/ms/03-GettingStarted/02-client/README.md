# Mewujudkan klien

Klien adalah aplikasi tersuai atau skrip yang berkomunikasi secara langsung dengan Pelayan MCP untuk meminta sumber, alat, dan arahan. Tidak seperti menggunakan alat pemeriksa, yang menyediakan antara muka grafik untuk berinteraksi dengan pelayan, menulis klien anda sendiri membolehkan interaksi secara programatik dan automatik. Ini membolehkan pembangun mengintegrasikan keupayaan MCP ke dalam aliran kerja mereka sendiri, mengautomatikkan tugasan, dan membina penyelesaian tersuai yang disesuaikan dengan keperluan tertentu.

## Gambaran Keseluruhan

Pelajaran ini memperkenalkan konsep klien dalam ekosistem Protokol Konteks Model (MCP). Anda akan belajar cara menulis klien anda sendiri dan menghubungkannya ke Pelayan MCP.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Memahami apa yang boleh dilakukan oleh klien.
- Menulis klien anda sendiri.
- Menghubungkan dan menguji klien dengan pelayan MCP untuk memastikan pelayan berfungsi seperti yang dijangkakan.

## Apa yang perlu dilakukan untuk menulis klien?

Untuk menulis klien, anda perlu melakukan perkara berikut:

- **Import perpustakaan yang betul**. Anda akan menggunakan perpustakaan yang sama seperti sebelum ini, cuma struktur yang berbeza.
- **Buat instans klien**. Ini akan melibatkan penciptaan instans klien dan menyambungkannya ke kaedah pengangkutan yang dipilih.
- **Tentukan sumber apa yang hendak disenaraikan**. Pelayan MCP anda disertakan dengan sumber, alat dan arahan, anda perlu memutuskan yang mana satu untuk disenaraikan.
- **Mengintegrasikan klien ke dalam aplikasi hos**. Setelah anda mengetahui keupayaan pelayan, anda perlu mengintegrasikan ini ke dalam aplikasi hos anda supaya jika pengguna menaip arahan atau arahan lain, ciri pelayan yang bersesuaian akan dipanggil.

Sekarang kita faham secara garis besar apa yang akan kita lakukan, mari kita lihat contoh seterusnya.

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

// Senarai arahan
const prompts = await client.listPrompts();

// Dapatkan satu arahan
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Senarai sumber
const resources = await client.listResources();

// Baca satu sumber
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Panggil alat
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Dalam kod sebelumnya kami:

- Mengimport perpustakaan
- Mencipta instans klien dan menyambungkannya menggunakan stdio sebagai pengangkutan.
- Menyenaraikan arahan, sumber dan alat dan memanggil kesemuanya.

Itulah, sebuah klien yang boleh berbual dengan Pelayan MCP.

Mari kita luangkan masa di bahagian latihan seterusnya dan pecahkan setiap potongan kod serta terangkan apa yang berlaku.

## Latihan: Menulis klien

Seperti yang disebutkan di atas, mari kita luangkan masa menerangkan kod, dan jika mahu, anda boleh menulis kod bersama-sama.

### -1- Import perpustakaan

Mari kita import perpustakaan yang diperlukan, kita akan memerlukan rujukan kepada klien dan kepada protokol pengangkutan yang dipilih, stdio. stdio adalah protokol untuk perkara yang bertujuan dijalankan pada mesin tempatan anda. SSE adalah protokol pengangkutan lain yang akan kami tunjukkan dalam bab akan datang tetapi itu adalah pilihan lain anda. Buat masa ini, mari teruskan dengan stdio.

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

Untuk Java, anda akan mencipta klien yang menyambung ke pelayan MCP dari latihan sebelumnya. Menggunakan struktur projek Java Spring Boot yang sama dari [Memulakan dengan Pelayan MCP](../../../../03-GettingStarted/01-first-server/solution/java), buat kelas Java baru yang dipanggil `SDKClient` dalam folder `src/main/java/com/microsoft/mcp/sample/client/` dan tambah import berikut:

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

Anda perlu menambah kebergantungan berikut ke fail `Cargo.toml` anda.

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

Daripada situ, anda boleh mengimport perpustakaan yang diperlukan dalam kod klien anda.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Mari teruskan dengan penciptaan instans.

### -2- Membuat instans klien dan pengangkutan

Kita perlu mencipta instans pengangkutan dan juga klien kita:

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

Dalam kod sebelumnya kami telah:

- Mencipta instans pengangkutan stdio. Perhatikan bagaimana ia menentukan arahan dan argumen untuk mencari dan memulakan pelayan kerana itulah sesuatu yang perlu kita lakukan semasa mencipta klien.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Menginstansikan klien dengan memberikan nama dan versi.

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

Dalam kod sebelumnya kami telah:

- Mengimport perpustakaan yang diperlukan
- Menginstansikan objek parameter pelayan kerana kita akan menggunakannya untuk menjalankan pelayan supaya kita boleh menyambung kepadanya dengan klien kita.
- Mendefinisikan kaedah `run` yang seterusnya memanggil `stdio_client` yang memulakan sesi klien.
- Mencipta titik masuk di mana kita menyediakan kaedah `run` kepada `asyncio.run`.

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

Dalam kod sebelumnya kami telah:

- Mengimport perpustakaan yang diperlukan.
- Mencipta pengangkutan stdio dan mencipta klien `mcpClient`. Klien ini adalah sesuatu yang kita akan gunakan untuk menyenaraikan dan memanggil ciri pada Pelayan MCP.

Perhatian, dalam "Arguments", anda boleh menunjuk sama ada kepada *.csproj* atau kepada fail boleh laksana.

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
        
        // Logik pelanggan anda dimulakan di sini
    }
}
```

Dalam kod sebelumnya kami telah:

- Mencipta kaedah utama yang menyediakan pengangkutan SSE menunjuk ke `http://localhost:8080` di mana pelayan MCP kita akan dijalankan.
- Mencipta kelas klien yang menerima pengangkutan sebagai parameter konstruktor.
- Dalam kaedah `run`, kita mencipta klien MCP secara sinkron menggunakan pengangkutan dan memulakan sambungan.
- Menggunakan pengangkutan SSE (Server-Sent Events) yang sesuai untuk komunikasi berasaskan HTTP dengan pelayan MCP Java Spring Boot.

#### Rust

Perlu diketahui, klien Rust ini menganggap pelayan adalah projek adik-beradik bernama "calculator-server" dalam direktori yang sama. Kod di bawah ini akan memulakan pelayan dan menyambung kepadanya.

```rust
async fn main() -> Result<(), RmcpError> {
    // Anggap server adalah projek adik-beradik yang bernama "calculator-server" dalam direktori yang sama
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

    // TODO: Senaraikan alat

    // TODO: Panggil tambah alat dengan argumen = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Menyenaraikan ciri pelayan

Kini, kita mempunyai klien yang boleh disambungkan apabila program dijalankan. Namun, ia tidak menyenaraikan ciri-cirinya jadi mari kita lakukan itu seterusnya:

#### TypeScript

```typescript
// Senarai arahan
const prompts = await client.listPrompts();

// Senarai sumber
const resources = await client.listResources();

// senarai alat
const tools = await client.listTools();
```

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
```

Di sini kita menyenaraikan sumber yang ada, `list_resources()` dan alat `list_tools` dan mencetaknya keluar.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Di atas adalah contoh bagaimana kita boleh menyenaraikan alat di pelayan. Untuk setiap alat, kita kemudian mencetak namanya.

#### Java

```java
// Senaraikan dan tunjukkan alat
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Anda juga boleh ping pelayan untuk mengesahkan sambungan
client.ping();
```

Dalam kod sebelumnya kami telah:

- Memanggil `listTools()` untuk mendapatkan semua alat yang tersedia dari pelayan MCP.
- Menggunakan `ping()` untuk mengesahkan bahawa sambungan ke pelayan berfungsi.
- `ListToolsResult` mengandungi maklumat tentang semua alat termasuk nama, penerangan, dan skema input mereka.

Bagus, kini kita telah menangkap semua ciri. Soalannya, bila kita menggunakannya? Baiklah, klien ini agak mudah, mudah dalam erti kata kita perlu memanggil ciri-ciri secara eksplisit apabila kita mahu mereka. Dalam bab seterusnya, kita akan mencipta klien lebih maju yang mempunyai akses kepada model bahasa besarnya sendiri, LLM. Buat masa ini, mari lihat bagaimana kita boleh memanggil ciri pada pelayan:

#### Rust

Dalam fungsi utama, selepas menginisialisasi klien, kita boleh menginisialisasi pelayan dan menyenaraikan beberapa cirinya.

```rust
// Inisialisasi
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Senaraikan alat
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Memanggil ciri

Untuk memanggil ciri, kita perlu memastikan kita menentukan argumen yang betul dan dalam beberapa kes nama apa yang kita cuba panggil.

#### TypeScript

```typescript

// Baca sebuah sumber
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Panggil satu alat
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// panggil arahan segera
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Dalam kod sebelumnya kami:

- Membaca sumber, kita panggil sumber dengan memanggil `readResource()` dengan menyatakan `uri`. Ini kemungkinan besar seperti berikut di sisi pelayan:

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

    Nilai `uri` kita `file://example.txt` sepadan dengan `file://{name}` di pelayan. `example.txt` akan dipetakan kepada `name`.

- Memanggil alat, kita panggil dengan menyatakan `name` dan `arguments` seperti berikut:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Mendapatkan arahan, untuk mendapatkan arahan, anda panggil `getPrompt()` dengan `name` dan `arguments`. Kod pelayan kelihatan seperti ini:

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

    maka kod klien anda yang terhasil kelihatan seperti ini untuk sepadan dengan yang diisytiharkan di pelayan:

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
# Baca sumber
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Panggil alat
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Dalam kod sebelumnya, kami telah:

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

1. Untuk mencetak hasilnya, berikut beberapa kod untuk mengendalikan itu:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Panggil pelbagai alat kalkulator
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

Dalam kod sebelumnya kami telah:

- Memanggil beberapa alat kalkulator menggunakan kaedah `callTool()` dengan objek `CallToolRequest`.
- Setiap panggilan alat menentukan nama alat dan `Map` argumen yang diperlukan oleh alat tersebut.
- Alat pelayan mengharapkan nama parameter tertentu (seperti "a", "b" untuk operasi matematik).
- Keputusan dikembalikan sebagai objek `CallToolResult` yang mengandungi respons dari pelayan.

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

### -5- Jalankan klien

Untuk menjalankan klien, taip arahan berikut di terminal:

#### TypeScript

Tambah entri berikut ke bahagian "scripts" dalam *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Panggil klien dengan arahan berikut:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Pertama, pastikan pelayan MCP anda berjalan di `http://localhost:8080`. Kemudian jalankan klien:

```bash
# Bina projek anda
./mvnw clean compile

# Jalankan klien
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Secara alternatif, anda boleh menjalankan projek klien lengkap yang disediakan dalam folder penyelesaian `03-GettingStarted\02-client\solution\java`:

```bash
# Navigasi ke direktori penyelesaian
cd 03-GettingStarted/02-client/solution/java

# Bina dan jalankan JAR
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

Berikut adalah pelayan yang boleh anda gunakan yang anda perlu panggil melalui kod klien anda, lihat jika anda boleh menambah lebih banyak ciri kepada pelayan untuk menjadikannya lebih menarik.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Cipta pelayan MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Tambah alat penambahan
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Tambah sumber ucapan dinamik
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

// Mula menerima mesej pada stdin dan menghantar mesej pada stdout

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

# Cipta pelayan MCP
mcp = FastMCP("Demo")


# Tambah alat penjumlahan
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Tambah sumber salam dinamik
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

Lihat projek ini untuk melihat bagaimana anda boleh [menambah arahan dan sumber](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Juga, semak pautan ini tentang bagaimana untuk memanggil [arahan dan sumber](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Dalam [bahagian sebelumnya](../../../../03-GettingStarted/01-first-server), anda telah belajar bagaimana mencipta pelayan MCP yang mudah dengan Rust. Anda boleh terus membina di atas itu atau semak pautan ini untuk contoh pelayan MCP berasaskan Rust yang lebih banyak: [Contoh Pelayan MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Penyelesaian

**folder penyelesaian** mengandungi pelaksanaan klien lengkap yang sedia untuk dijalankan yang menunjukkan semua konsep yang dibincangkan dalam tutorial ini. Setiap penyelesaian merangkumi kod klien dan pelayan yang dianjurkan dalam projek yang berasingan dan berdiri sendiri.

### 📁 Struktur Penyelesaian

Direktori penyelesaian dianjurkan mengikut bahasa pengaturcaraan:

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

- **Pelaksanaan klien lengkap** dengan semua ciri dari tutorial
- **Struktur projek yang berfungsi** dengan kebergantungan dan konfigurasi yang betul
- **Skrip bina dan jalankan** untuk kemudahan penyediaan dan pelaksanaan
- **README terperinci** dengan arahan khusus bahasa
- **Pengendalian ralat** dan contoh pemprosesan keputusan

### 📖 Menggunakan Penyelesaian

1. **Navigasi ke folder bahasa pilihan anda**:

   ```bash
   cd solution/typescript/    # Untuk TypeScript
   cd solution/java/          # Untuk Java
   cd solution/python/        # Untuk Python
   cd solution/dotnet/        # Untuk .NET
   ```

2. **Ikuti arahan README dalam setiap folder untuk:**
   - Memasang kebergantungan
   - Membina projek
   - Menjalankan klien

3. **Contoh output** yang sepatutnya anda lihat:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Untuk dokumentasi lengkap dan arahan langkah demi langkah, lihat: **[📖 Dokumentasi Penyelesaian](./solution/README.md)**

## 🎯 Contoh Lengkap

Kami telah menyediakan pelaksanaan klien lengkap dan berfungsi untuk semua bahasa pengaturcaraan yang diliputi dalam tutorial ini. Contoh ini menunjukkan fungsi penuh yang diterangkan di atas dan boleh digunakan sebagai pelaksanaan rujukan atau titik mula untuk projek anda sendiri.

### Contoh Lengkap Tersedia

| Bahasa   | Fail                                | Penerangan                                                     |
|----------|-----------------------------------|----------------------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Klien Java lengkap menggunakan pengangkutan SSE dengan pengendalian ralat menyeluruh |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Klien C# lengkap menggunakan pengangkutan stdio dengan permulaan pelayan automatik |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Klien TypeScript lengkap dengan sokongan protokol MCP penuh |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Klien Python lengkap menggunakan corak async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Klien Rust lengkap menggunakan Tokio untuk operasi async |

Setiap contoh lengkap merangkumi:
- ✅ **Penubuhan sambungan** dan pengendalian ralat  
- ✅ **Penemuan pelayan** (alat, sumber, arahan jika berkenaan)  
- ✅ **Operasi kalkulator** (tambah, tolak, darab, bahagi, bantuan)  
- ✅ **Pemprosesan keputusan** dan output yang diformatkan  
- ✅ **Pengendalian ralat yang menyeluruh**  
- ✅ **Kod yang bersih dan didokumentasi** dengan komen langkah demi langkah  

### Bermula dengan Contoh Lengkap

1. **Pilih bahasa pilihan anda** dari jadual di atas  
2. **Semak fail contoh lengkap** untuk memahami pelaksanaan penuh  
3. **Jalankan contoh** mengikut arahan dalam [`complete_examples.md`](./complete_examples.md)  
4. **Ubah suai dan kembangkan** contoh untuk kes penggunaan khusus anda  

Untuk dokumentasi terperinci mengenai menjalankan dan menyesuaikan contoh-contoh ini, lihat: **[📖 Dokumentasi Contoh Lengkap](./complete_examples.md)**  

### 💡 Penyelesaian vs. Contoh Lengkap

| **Folder Penyelesaian** | **Contoh Lengkap** |
|------------------------|--------------------|
| Struktur projek penuh dengan fail binaan | Pelaksanaan satu fail |
| Sedia untuk dijalankan dengan kebergantungan | Contoh kod fokus |
| Persediaan seperti produksi | Rujukan pendidikan |
| Alat khusus bahasa | Perbandingan lintas bahasa |

Kedua-dua pendekatan adalah bernilai - guna **folder penyelesaian** untuk projek lengkap dan **contoh lengkap** untuk pembelajaran dan rujukan.  

## Pengajaran Utama

Pengajaran utama untuk bab ini mengenai klien adalah seperti berikut:  

- Boleh digunakan untuk menemui dan memanggil ciri pada pelayan.  
- Boleh memulakan pelayan semasa ia sendiri bermula (seperti dalam bab ini) tetapi klien juga boleh menyambung ke pelayan yang sedang berjalan.  
- Merupakan cara yang bagus untuk menguji kemampuan pelayan berbanding alternatif seperti Inspector seperti yang diterangkan dalam bab sebelumnya.  

## Sumber Tambahan

- [Membina klien dalam MCP](https://modelcontextprotocol.io/quickstart/client)  

## Sampel

- [Kalkulator Java](../samples/java/calculator/README.md)  
- [Kalkulator .Net](../../../../03-GettingStarted/samples/csharp)  
- [Kalkulator JavaScript](../samples/javascript/README.md)  
- [Kalkulator TypeScript](../samples/typescript/README.md)  
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)  
- [Kalkulator Rust](../../../../03-GettingStarted/samples/rust)  

## Apa Seterusnya

- Seterusnya: [Membina klien dengan LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->