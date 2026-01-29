# Bir istemci oluşturma

İstemciler, kaynaklar, araçlar ve istemler talep etmek için bir MCP Sunucusuyla doğrudan iletişim kuran özel uygulamalar veya betiklerdir. Sunucuyla etkileşim için grafiksel bir arayüz sağlayan denetçi aracını kullanmanın aksine, kendi istemcinizi yazmak, programlanabilir ve otomatikleştirilmiş etkileşimlere olanak tanır. Bu, geliştiricilerin MCP yeteneklerini kendi iş akışlarına entegre etmelerini, görevleri otomatikleştirmelerini ve belirli ihtiyaçlara göre özel çözümler oluşturmalarını sağlar.

## Genel Bakış

Bu ders, Model Context Protocol (MCP) ekosistemindeki istemci kavramını tanıtmaktadır. Kendi istemcinizi nasıl yazacağınızı ve bunu bir MCP Sunucusuna nasıl bağlayacağınızı öğreneceksiniz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Bir istemcinin neler yapabileceğini anlamak.
- Kendi istemcinizi yazmak.
- İstemciyi bir MCP sunucusuna bağlamak ve sunucunun beklendiği gibi çalıştığını test etmek.

## Bir istemci yazmak için neler gerekir?

Bir istemci yazmak için aşağıdakileri yapmanız gerekecek:

- **Doğru kütüphaneleri içe aktarın**. Daha önce kullandığınız kütüphaneyi kullanacaksınız, ancak farklı yapılarla.
- **Bir istemci oluşturun**. Bu, bir istemci örneği oluşturmayı ve bunu seçilen taşıma yöntemine bağlamayı içerecektir.
- **Listelemek istediğiniz kaynaklara karar verin**. MCP sunucunuz kaynaklar, araçlar ve istemlerle birlikte gelir; hangisini listeleyeceğinize karar vermeniz gerekir.
- **İstemciyi bir ana uygulamaya entegre edin**. Sunucunun yeteneklerini öğrendikten sonra, bunu ana uygulamanıza entegre etmeniz gerekir, böylece bir kullanıcı bir istem veya başka bir komut yazdığında, ilgili sunucu özelliği çağrılır.

Şimdi ne yapacağımızı genel olarak anladığımıza göre, bir sonraki bölümde bir örneğe bakalım.

### Bir örnek istemci

Bir örnek istemciye göz atalım:

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

Yukarıdaki kodda şunları yaptık:

- Kütüphaneleri içe aktardık.
- Bir istemci örneği oluşturduk ve bunu taşıma için stdio kullanarak bağladık.
- İstemleri, kaynakları ve araçları listeledik ve hepsini çağırdık.

İşte bu kadar, bir MCP Sunucusuyla konuşabilen bir istemci.

Bir sonraki alıştırma bölümünde her kod parçasını ayırıp neler olduğunu açıklamak için zaman ayıralım.

## Alıştırma: Bir istemci yazma

Yukarıda söylediğimiz gibi, kodu açıklamak için zaman ayıralım ve isterseniz kodu yazarken bize katılın.

### -1- Kütüphaneleri içe aktarma

Gerekli kütüphaneleri içe aktaralım; bir istemciye ve seçtiğimiz taşıma protokolüne, stdio'ya referanslara ihtiyacımız olacak. stdio, yerel makinenizde çalışması amaçlanan şeyler için bir protokoldür. SSE, ilerleyen bölümlerde göstereceğimiz başka bir taşıma protokolüdür, ancak bu sizin diğer seçeneğinizdir. Şimdilik, stdio ile devam edelim.

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

Java için, önceki alıştırmadan MCP sunucusuna bağlanan bir istemci oluşturacaksınız. [MCP Sunucusuyla Başlarken](../../../../03-GettingStarted/01-first-server/solution/java) bölümündeki Java Spring Boot proje yapısını kullanarak, `src/main/java/com/microsoft/mcp/sample/client/` klasöründe `SDKClient` adlı yeni bir Java sınıfı oluşturun ve aşağıdaki içe aktarmaları ekleyin:

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

`Cargo.toml` dosyanıza aşağıdaki bağımlılıkları eklemeniz gerekecek.

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

Buradan, istemci kodunuzda gerekli kütüphaneleri içe aktarabilirsiniz.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Şimdi istemciyi başlatmaya geçelim.

### -2- İstemci ve taşıma oluşturma

Bir taşıma örneği ve istemci örneği oluşturmamız gerekecek:

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

Yukarıdaki kodda şunları yaptık:

- Bir stdio taşıma örneği oluşturduk. Bunun, sunucuyu nasıl bulacağımızı ve başlatacağımızı belirtmek için komut ve argümanları nasıl belirttiğine dikkat edin; bu, istemciyi oluştururken yapmamız gereken bir şeydir.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Bir istemci oluşturduk ve ona bir ad ve sürüm verdik.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- İstemciyi seçilen taşımaya bağladık.

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

Yukarıdaki kodda şunları yaptık:

- Gerekli kütüphaneleri içe aktardık.
- Sunucu parametreleri nesnesini başlattık; bunu, istemciyle bağlanabilmemiz için sunucuyu çalıştırmak için kullanacağız.
- `run` adlı bir yöntem tanımladık; bu yöntem, bir istemci oturumu başlatan `stdio_client` yöntemini çağırır.
- `run` yöntemini `asyncio.run`'a sağladığımız bir giriş noktası oluşturduk.

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

Yukarıdaki kodda şunları yaptık:

- Gerekli kütüphaneleri içe aktardık.
- Bir stdio taşıma ve bir `mcpClient` istemcisi oluşturduk. Bu istemciyi, MCP Sunucusundaki özellikleri listelemek ve çağırmak için kullanacağız.

Not: "Arguments" bölümünde, ya *.csproj* dosyasına ya da çalıştırılabilir dosyaya işaret edebilirsiniz.

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

Yukarıdaki kodda şunları yaptık:

- MCP sunucumuzun çalışacağı `http://localhost:8080` adresine işaret eden bir SSE taşıma ayarlayan bir ana yöntem oluşturduk.
- Taşımayı bir yapıcı parametresi olarak alan bir istemci sınıfı oluşturduk.
- `run` yönteminde, taşımayı kullanarak senkron bir MCP istemcisi oluşturduk ve bağlantıyı başlattık.
- Java Spring Boot MCP sunucularıyla HTTP tabanlı iletişim için uygun olan SSE (Sunucu Tarafından Gönderilen Olaylar) taşımayı kullandık.

#### Rust

Bu Rust istemcisi, sunucunun aynı dizindeki "calculator-server" adlı bir kardeş proje olduğunu varsayar. Aşağıdaki kod, sunucuyu başlatır ve ona bağlanır.

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

### -3- Sunucu özelliklerini listeleme

Şimdi, program çalıştırıldığında bağlanabilen bir istemcimiz var. Ancak, özelliklerini listelemiyor, bu yüzden bunu bir sonraki adımda yapalım:

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

Burada mevcut kaynakları `list_resources()` ve araçları `list_tools` listeledik ve bunları yazdırdık.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Yukarıda, sunucudaki araçları nasıl listeleyebileceğimize dair bir örnek bulunmaktadır. Her araç için, adını yazdırıyoruz.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Yukarıdaki kodda şunları yaptık:

- MCP sunucusundan mevcut tüm araçları almak için `listTools()` yöntemini çağırdık.
- Sunucuyla bağlantının çalıştığını doğrulamak için `ping()` yöntemini kullandık.
- `ListToolsResult`, araçların adları, açıklamaları ve giriş şemaları gibi bilgileri içerir.

Harika, şimdi tüm özellikleri yakaladık. Şimdi soru şu: Bunları ne zaman kullanacağız? Bu istemci oldukça basit; basit derken, özellikleri istediğimizde açıkça çağırmamız gerektiğini kastediyoruz. Bir sonraki bölümde, kendi büyük dil modeline (LLM) erişimi olan daha gelişmiş bir istemci oluşturacağız. Şimdilik, sunucudaki özellikleri nasıl çağırabileceğimize bakalım:

#### Rust

Ana işlevde, istemciyi başlattıktan sonra sunucuyu başlatabilir ve bazı özelliklerini listeleyebilirsiniz.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Özellikleri çağırma

Özellikleri çağırmak için doğru argümanları ve bazı durumlarda çağırmaya çalıştığımız şeyin adını belirtmemiz gerekir.

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

Yukarıdaki kodda şunları yaptık:

- Bir kaynağı okuduk, kaynağı `readResource()` çağırarak ve `uri` belirterek çağırdık. İşte sunucu tarafında nasıl görünebileceği:

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

    Sunucudaki `file://{name}` ile `uri` değerimiz `file://example.txt` eşleşir. `example.txt`, `name` ile eşleştirilir.

- Bir aracı çağırdık, bunu `name` ve `arguments` belirterek yaptık:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Bir istem aldık, bir istem almak için `getPrompt()` yöntemini `name` ve `arguments` ile çağırdık. Sunucu kodu şu şekilde görünür:

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

    ve istemci kodunuz, sunucuda tanımlananlarla eşleşmesi için şu şekilde görünür:

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

Yukarıdaki kodda şunları yaptık:

- `read_resource` kullanarak `greeting` adlı bir kaynağı çağırdık.
- `call_tool` kullanarak `add` adlı bir aracı çağırdık.

#### .NET

1. Bir aracı çağırmak için biraz kod ekleyelim:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Sonucu yazdırmak için, işte bunu ele alacak biraz kod:

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

Yukarıdaki kodda şunları yaptık:

- `CallToolRequest` nesneleriyle `callTool()` yöntemini kullanarak birden fazla hesap makinesi aracını çağırdık.
- Her araç çağrısı, o araca ait adı ve gerekli argümanların bir `Map`'ini belirtir.
- Sunucu araçları, belirli parametre adlarını (örneğin, matematiksel işlemler için "a", "b") bekler.
- Sonuçlar, sunucudan gelen yanıtı içeren `CallToolResult` nesneleri olarak döndürülür.

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

### -5- İstemciyi çalıştırma

İstemciyi çalıştırmak için terminalde şu komutu yazın:

#### TypeScript

*package.json* dosyanızdaki "scripts" bölümüne aşağıdaki girdiyi ekleyin:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

İstemciyi şu komutla çağırın:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Öncelikle, MCP sunucunuzun `http://localhost:8080` adresinde çalıştığından emin olun. Ardından istemciyi çalıştırın:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatif olarak, çözüm klasöründe sağlanan tam istemci projesini çalıştırabilirsiniz: `03-GettingStarted\02-client\solution\java`:

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

## Ödev

Bu ödevde, bir istemci oluşturmayı öğrendiklerinizi kullanacaksınız, ancak kendi istemcinizi oluşturacaksınız.

İşte istemci kodunuz aracılığıyla çağırmanız gereken bir sunucu; sunucuya daha fazla özellik ekleyip ilginç hale getirebilir misiniz bir bakın.

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

Bu projeyi görmek için şu bağlantıya bakın: [İstemler ve kaynaklar ekleme](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Ayrıca, şu bağlantıya göz atın: [İstemleri ve kaynakları çağırma](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

[Önceki bölümde](../../../../03-GettingStarted/01-first-server), Rust ile basit bir MCP sunucusu oluşturmayı öğrendiniz. Buna devam edebilir veya daha fazla Rust tabanlı MCP sunucu örneği için şu bağlantıya göz atabilirsiniz: [MCP Sunucu Örnekleri](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Çözüm

**Çözüm klasörü**, bu öğreticide ele alınan tüm kavramları gösteren, çalışmaya hazır istemci uygulamalarını içerir. Her çözüm, istemci ve sunucu kodunu ayrı, kendi kendine yeterli projeler halinde düzenler.

### 📁 Çözüm Yapısı

Çözüm dizini, programlama diline göre düzenlenmiştir:

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

### 🚀 Her Çözümde Neler Var

Her dil için özel çözüm şunları sağlar:

- **Tam istemci uygulaması**, öğreticideki tüm özelliklerle
- **Çalışan proje yapısı**, uygun bağımlılıklar ve yapılandırmalarla
- **Kolay kurulum ve çalıştırma için betikler**
- **Detaylı README**, dile özel talimatlarla
- **Hata işleme** ve sonuç işleme örnekleri

### 📖 Çözümleri Kullanma

1. **Tercih ettiğiniz dil klasörüne gidin**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Her klasördeki README talimatlarını izleyin**:
   - Bağımlılıkları yükleme
   - Projeyi derleme
   - İstemciyi çalıştırma

3. **Görmeniz gereken örnek çıktı**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Tam dokümantasyon ve adım adım talimatlar için şu bağlantıya bakın: **[📖 Çözüm Dokümantasyonu](./solution/README.md)**

## 🎯 Tam Örnekler

Bu öğreticide ele alınan tüm işlevselliği gösteren, tüm programlama dilleri için eksiksiz, çalışan istemci uygulamaları sağladık. Bu örnekler, referans uygulamaları veya kendi projeleriniz için başlangıç noktaları olarak kullanılabilir.

### Mevcut Tam Örnekler

| Dil | Dosya | Açıklama |
|-----|-------|----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Hata işleme ile kapsamlı SSE taşımayı kullanan tam Java istemcisi |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Otomatik sunucu başlatma ile stdio taşımayı kullanan tam C# istemcisi |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Tam MCP protokol desteği ile eksiksiz TypeScript istemcisi |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Async/await desenlerini kullanan eksiksiz Python istemcisi |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Async işlemler için Tokio kullanan eksiksiz Rust istemcisi |
Her bir tam örnek şunları içerir:

- ✅ **Bağlantı kurulumu** ve hata yönetimi
- ✅ **Sunucu keşfi** (araçlar, kaynaklar, uygun yerlerde istemler)
- ✅ **Hesap makinesi işlemleri** (toplama, çıkarma, çarpma, bölme, yardım)
- ✅ **Sonuç işleme** ve biçimlendirilmiş çıktı
- ✅ **Kapsamlı hata yönetimi**
- ✅ **Temiz, belgelenmiş kod** ile adım adım açıklamalar

### Tam Örneklerle Başlarken

1. Yukarıdaki tablodan **tercih ettiğiniz dili seçin**
2. **Tam örnek dosyasını inceleyin** ve tam uygulamayı anlayın
3. [`complete_examples.md`](./complete_examples.md) dosyasındaki talimatları izleyerek **örneği çalıştırın**
4. **Kendi özel kullanım durumunuza göre** örneği değiştirin ve genişletin

Bu örnekleri çalıştırma ve özelleştirme hakkında ayrıntılı belgeler için şu bağlantıya bakın: **[📖 Tam Örnekler Belgeleri](./complete_examples.md)**

### 💡 Çözüm vs. Tam Örnekler

| **Çözüm Klasörü** | **Tam Örnekler** |
|--------------------|--------------------- |
| Derleme dosyalarıyla tam proje yapısı | Tek dosyalık uygulamalar |
| Bağımlılıklarla çalıştırmaya hazır | Odaklanmış kod örnekleri |
| Üretim benzeri kurulum | Eğitici referans |
| Dile özel araçlar | Diller arası karşılaştırma |

Her iki yaklaşım da değerlidir - **çözüm klasörünü** tam projeler için, **tam örnekleri** ise öğrenme ve referans için kullanın.

## Temel Çıkarımlar

Bu bölümdeki temel çıkarımlar şunlardır:

- İstemciler, hem sunucudaki özellikleri keşfetmek hem de çağırmak için kullanılabilir.
- Kendisi başlarken bir sunucu başlatabilir (bu bölümde olduğu gibi), ancak istemciler çalışan sunuculara da bağlanabilir.
- Bir önceki bölümde açıklanan Inspector gibi alternatiflerin yanında, sunucu yeteneklerini test etmek için harika bir yoldur.

## Ek Kaynaklar

- [MCP'de istemci oluşturma](https://modelcontextprotocol.io/quickstart/client)

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python)
- [Rust Hesap Makinesi](../../../../03-GettingStarted/samples/rust)

## Sıradaki Adımlar

- Sonraki: [Bir LLM ile istemci oluşturma](../03-llm-client/README.md)

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.