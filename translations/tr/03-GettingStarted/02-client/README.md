# Bir istemci oluşturma

İstemciler, doğrudan bir MCP Sunucusuyla iletişim kurarak kaynaklar, araçlar ve istemler talep eden özel uygulamalar veya betiklerdir. Sunucuyla etkileşim için grafiksel bir arayüz sağlayan denetçi aracını kullanmanın aksine, kendi istemcinizi yazmak programatik ve otomatik etkileşimlere olanak tanır. Bu, geliştiricilerin MCP yeteneklerini kendi iş akışlarına entegre etmelerini, görevleri otomatikleştirmelerini ve belirli ihtiyaçlara uygun özel çözümler geliştirmelerini sağlar.

## Genel Bakış

Bu ders, Model Bağlam Protokolü (MCP) ekosistemindeki istemci kavramını tanıtır. Kendi istemcinizi nasıl yazacağınızı ve onu bir MCP Sunucusuna nasıl bağlayacağınızı öğreneceksiniz.

## Öğrenme Hedefleri

Bu dersin sonunda şu becerilere sahip olacaksınız:

- Bir istemcinin neler yapabileceğini anlamak.
- Kendi istemcinizi yazmak.
- İstemciyi MCP sunucusuna bağlayıp test ederek sunucunun beklendiği gibi çalıştığını doğrulamak.

## Bir istemci yazarken nelere dikkat edilmeli?

Bir istemci yazmak için şunları yapmanız gerekir:

- **Doğru kütüphaneleri içe aktarın**. Öncekiyle aynı kütüphaneyi kullanacaksınız, sadece farklı yapılar olacak.
- **Bir istemci örneği oluşturun**. Bu, bir istemci örneği oluşturmayı ve seçilen taşıma yöntemine bağlamayı içerecek.
- **Hangi kaynakları listeleyeceğinize karar verin**. MCP sunucunuz kaynaklar, araçlar ve istemlerle birlikte gelir; hangilerini listeleyeceğinize karar vermelisiniz.
- **İstemciyi bir ana uygulamaya entegre edin**. Sunucunun yeteneklerini öğrendikten sonra, kullanıcı bir istem veya başka bir komut yazdığında ilgili sunucu özelliğinin çağrılmasını sağlamak için bunu ana uygulamanıza entegre etmeniz gerekir.

Artık yüksek seviyede ne yapacağımızı anladığımıza göre, bir sonraki bölüme geçip bir örneğe bakalım.

### Bir örnek istemci

Bu örnek istemciye göz atalım:

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

// İstekleri listele
const prompts = await client.listPrompts();

// Bir istek al
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Kaynakları listele
const resources = await client.listResources();

// Bir kaynağı oku
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Bir aracı çağır
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Yukarıdaki kodda:

- Kütüphaneler içe aktarılıyor.
- Bir istemci örneği oluşturuluyor ve stdio taşıması ile bağlanıyor.
- İstemler, kaynaklar ve araçlar listeleniyor ve hepsi çağrılıyor.

İşte karşınızda, bir MCP Sunucusuyla konuşabilen bir istemci.

Bir sonraki alıştırma bölümünde her kod parçasını ayrıntılı inceleyip ne olduğunu açıklayalım.

## Alıştırma: Bir istemci yazmak

Yukarıda belirtildiği gibi, kodu açıklamaya zaman ayıralım ve isterseniz kodu birlikte yazalım.

### -1- Kütüphaneleri içe aktarma

Gerekli kütüphaneleri içe aktaralım, hem istemci hem de seçilen taşıma protokolü stdio için referanslara ihtiyacımız olacak. Stdio, yerel makinenizde çalışması amaçlanan şeyler için bir protokoldür. SSE, gelecekteki bölümlerde göstereceğimiz başka bir taşıma protokolüdür ama şimdilik stdio ile devam edelim.

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

Java için, önceki alıştırmadan MCP sunucusuna bağlanan bir istemci oluşturacaksınız. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) bölümünde kullanılan aynı Java Spring Boot proje yapısını kullanarak `src/main/java/com/microsoft/mcp/sample/client/` klasöründe `SDKClient` adında yeni bir Java sınıfı oluşturun ve aşağıdaki içe aktarımları ekleyin:

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

`Cargo.toml` dosyanıza aşağıdaki bağımlılıkları eklemeniz gerekir.

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

Bundan sonra, istemci kodunuzda gerekli kütüphaneleri içe aktarabilirsiniz.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Şimdi örneklemeye geçelim.

### -2- İstemci ve taşımanın örneklenmesi

Taşıma ve istemci için bir örnek oluşturmamız gerekecek:

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

Yukarıdaki kodda:

- Bir stdio taşıma örneği oluşturduk. Komut ve argümanlarla sunucunun nasıl bulunup başlatılacağını belirtmek gerekiyor, çünkü istemci oluştururken bunu yapmamız gerekecek.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Bir istemci yaratıp ona isim ve sürüm verdik.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- İstemciyi seçilen taşıma yöntemine bağladık.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio bağlantısı için sunucu parametreleri oluştur
server_params = StdioServerParameters(
    command="mcp",  # Çalıştırılabilir dosya
    args=["run", "server.py"],  # İsteğe bağlı komut satırı argümanları
    env=None,  # İsteğe bağlı ortam değişkenleri
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Bağlantıyı başlat
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Yukarıdaki kodda:

- Gerekli kütüphaneler içe aktarıldı.
- Bağlantı için kullanılacak olan sunucu parametreleri nesnesi oluşturuldu.
- `stdio_client` çağıran `run` adlı bir metot tanımlandı, bu da istemci oturumunu başlatır.
- `asyncio.run` içine `run` metodu giriş noktası olarak verildi.

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

Yukarıdaki kodda:

- Gerekli kütüphaneler içe aktarıldı.
- Bir stdio taşıma oluşturuldu ve `mcpClient` adlı bir istemci yaratıldı. Bunu MCP Sunucudaki özellikleri listelemek ve çağırmak için kullanacağız.

Not: "Arguments" bölümünde *.csproj* dosyasına veya çalıştırılabilir dosyaya işaret edebilirsiniz.

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
        
        // Müşteri mantığınız buraya gelir
    }
}
```

Yukarıdaki kodda:

- MCP sunucumuzu çalıştıracak olan `http://localhost:8080` adresine işaret eden bir SSE taşıma oluşturuldu.
- Taşıma parametresi alan bir istemci sınıfı yaratıldı.
- `run` metodunda taşıma kullanılarak senkron bir MCP istemcisi oluşturulup bağlantı başlatıldı.
- Java Spring Boot MCP sunucularıyla HTTP tabanlı iletişim için uygun olan SSE (Sunucu Gönderimli Olaylar) taşıması kullanıldı.

#### Rust

Bu Rust istemcisi, sunucunun aynı dizinde "calculator-server" adlı kardeş bir proje olduğunu varsayıyor. Aşağıdaki kod sunucuyu başlatacak ve ona bağlanacaktır.

```rust
async fn main() -> Result<(), RmcpError> {
    // Sunucunun aynı dizinde "calculator-server" adında kardeş bir proje olduğunu varsayın
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

    // TODO: Başlat

    // TODO: Araçları listele

    // TODO: add aracını argümanlarla çağır = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Sunucu özelliklerini listeleme

Şimdi program çalıştırıldığında bağlanacak bir istemcimiz var. Ancak özelliklerini listelemiyor, bunu şimdi yapalım:

#### TypeScript

```typescript
// İstekleri listele
const prompts = await client.listPrompts();

// Kaynakları listele
const resources = await client.listResources();

// araçları listele
const tools = await client.listTools();
```

#### Python

```python
# Mevcut kaynakları listele
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Mevcut araçları listele
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Burada mevcut kaynakları (`list_resources()`) ve araçları (`list_tools`) listeliyoruz ve yazdırıyoruz.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Yukarıda, sunucudaki araçları nasıl listeleyebileceğimize dair bir örnek var. Her araç için adı yazdırıyoruz.

#### Java

```java
// Araçları listeleyin ve gösterin
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Bağlantıyı doğrulamak için sunucuya ping atabilirsiniz
client.ping();
```

Yukarıdaki kodda:

- MCP sunucudan tüm mevcut araçları almak için `listTools()` çağrıldı.
- Bağlantının çalıştığını doğrulamak için `ping()` kullanıldı.
- `ListToolsResult` içinde araçların adlarını, açıklamalarını ve giriş şemalarını içeren bilgiler bulunur.

Harika, şimdi tüm özellikleri yakaladık. Şimdi soralım ne zaman kullanacağız? Bu istemci oldukça basit; özellikleri kullanmak istediğimizde açıkça çağırmamız gerekiyor. Sonraki bölümde kendi büyük dil modeli (LLM)'ne erişimi olan daha gelişmiş bir istemci oluşturacağız. Şimdilik, sunucudaki özelliklerin nasıl çağrılabileceğine bakalım:

#### Rust

Ana fonksiyonda, istemciyi başlattıktan sonra sunucuyu başlatabilir ve bazı özelliklerini listeleyebiliriz.

```rust
// Başlat
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Araçları listele
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Özellikleri çağırma

Özellikleri çağırmak için doğru argümanları ve bazı durumlarda çağırdığımız şeyin adını belirtmemiz gerekir.

#### TypeScript

```typescript

// Bir kaynağı oku
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Bir aracı çağır
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// isteği çağır
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Yukarıdaki kodda:

- Bir kaynağı okuduk, `uri` belirterek `readResource()` çağrıldı. Sunucu tarafında muhtemel görünümü şudur:

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

    `uri` değerimiz `file://example.txt` sunucudaki `file://{name}` ile eşleşir. `example.txt`, `name` olarak eşlenir.

- Bir aracı çağırmak için adını (`name`) ve argümanlarını (`arguments`) belirtiyoruz:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Bir istem almak için, ismi ve argümanları ile `getPrompt()` çağrılır. Sunucu kodu şöyledir:

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

   Böylece istemci tarafı da sunucu tarafına uyacak şekilde aşağıdaki gibidir:

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
# Bir kaynağı oku
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Bir aracı çağır
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Yukarıdaki kodda:

- `greeting` adlı kaynağı `read_resource` ile çağırdık.
- `add` adlı aracı `call_tool` ile çalıştırdık.

#### .NET

1. Bir aracı çağırmak için kod ekleyelim:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Sonucu yazdırmak için ise şu kodu ekleyelim:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Çeşitli hesap makinesi araçlarını çağırın
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

Yukarıdaki kodda:

- `CallToolRequest` nesneleri ile `callTool()` metodunu kullanarak hesap makinesi araçlarından birden fazlasını çağırdık.
- Her araç çağrısı, araç adını ve o aracın ihtiyaç duyduğu argümanlar (`Map`) ile birlikte yapılır.
- Sunucu araçları matematiksel işlemler için belirli parametre adları (örn. "a", "b") bekler.
- Sonuçlar, sunucudan gelen yanıtları içeren `CallToolResult` nesneleri olarak döner.

#### Rust

```rust
// add aracını şu argümanlarla çağır = {"a": 3, "b": 2}
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

İstemciyi çalıştırmak için terminalde aşağıdaki komutu girin:

#### TypeScript

*package.json* dosyanızın "scripts" bölümüne aşağıdaki girdiyi ekleyin:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

İstemciyi aşağıdaki komutla çağırın:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Öncelikle MCP sunucunuzun `http://localhost:8080` adresinde çalıştığından emin olun. Ardından istemciyi çalıştırın:

```bash
# Projenizi derleyin
./mvnw clean compile

# İstemciyi çalıştırın
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatif olarak, çözüm klasöründe bulunan `03-GettingStarted\02-client\solution\java` tam istemci projesini çalıştırabilirsiniz:

```bash
# Çözüm dizinine gidin
cd 03-GettingStarted/02-client/solution/java

# JAR dosyasını derleyin ve çalıştırın
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Ödev

Bu ödevde, öğrendiklerinizi kullanarak kendi istemcinizi oluşturacaksınız.

Aşağıda, istemci kodunuzdan çağırmanız gereken bir sunucu var; sunucuyu daha ilginç hale getirmek için ona daha fazla özellik ekleyip ekleyemeyeceğinizi görün.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Bir MCP sunucusu oluşturun
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Bir toplama aracı ekleyin
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dinamik bir karşılama kaynağı ekleyin
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

// stdin üzerinde mesaj almayı ve stdout üzerinde mesaj göndermeyi başlatın

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

# Bir MCP sunucusu oluşturun
mcp = FastMCP("Demo")


# Bir toplama aracı ekleyin
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dinamik bir karşılama kaynağı ekleyin
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

Bu projeye bakarak [istemleri ve kaynakları nasıl ekleyebileceğinizi](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) görebilirsiniz.

Ayrıca, şu bağlantıda [istemleri ve kaynakları nasıl çağıracağınız](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) açıklanmıştır.

### Rust

[Önceki bölümde](../../../../03-GettingStarted/01-first-server) Rust ile basit bir MCP sunucu oluşturmayı öğrendiniz. Üzerine eklemeye devam edebilir veya şu bağlantıdan daha fazla Rust tabanlı MCP sunucu örneklerine bakabilirsiniz: [MCP Sunucu Örnekleri](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Çözüm

**Çözüm klasörü**, bu öğretide ele alınan tüm kavramları gösteren tam ve çalıştırmaya hazır istemci uygulamalarını içerir. Her çözüm, istemci ve sunucu kodunu ayrı ve kendi içinde bağımsız projelerde organize eder.

### 📁 Çözüm Yapısı

Çözüm dizini programlama diline göre organize edilmiştir:

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

### 🚀 Her Çözüm Neleri İçerir

Her dil için çözüm,

- Öğretideki tüm özelliklerle **tam istemci uygulaması**
- Doğru bağımlılıkları ve yapılandırmayı içeren **çalışan proje yapısı**
- Kurulum ve çalıştırma için **yapı ve çalıştırma betikleri**
- Dil özelinde talimatlar içeren **detaylı README**
- Hata yönetimi ve sonuç işleme örnekleri

### 📖 Çözümleri Kullanma

1. **Tercih ettiğiniz dil klasörüne gidin**:

   ```bash
   cd solution/typescript/    # TypeScript için
   cd solution/java/          # Java için
   cd solution/python/        # Python için
   cd solution/dotnet/        # .NET için
   ```

2. **Her klasördeki README talimatlarını izleyin**:
   - Bağımlılıkların kurulması
   - Projenin derlenmesi
   - İstemcinin çalıştırılması

3. **Görmeniz gereken örnek çıktı**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Tam dokümantasyon ve adım adım talimatlar için bkz.: **[📖 Çözüm Dokümantasyonu](./solution/README.md)**

## 🎯 Tam Örnekler

Bu öğretide yer alan tüm programlama dilleri için tam ve çalışan istemci uygulamaları sağladık. Bu örnekler yukarıda açıklanan tüm işlevselliği gösterir ve kendi projeleriniz için referans veya başlangıç noktası olarak kullanılabilir.

### Mevcut Tam Örnekler

| Dil | Dosya | Açıklama |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kapsamlı hata yönetimi ile SSE taşımasını kullanan tam Java istemcisi |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Otomatik sunucu başlatma özellikli stdio taşıması kullanan tam C# istemcisi |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Tam MCP protokol desteği içeren TypeScript istemcisi |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Async/await desenlerini kullanan tam Python istemcisi |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Async işlemler için Tokio kullanan tam Rust istemcisi |

Her tam örnek, şunları içerir:
- ✅ **Bağlantı kurulumu** ve hata yönetimi
- ✅ **Sunucu keşfi** (uygulandığı yerlerde araçlar, kaynaklar, istemler)
- ✅ **Hesap makinesi işlemleri** (toplama, çıkarma, çarpma, bölme, yardım)
- ✅ **Sonuç işleme** ve biçimlendirilmiş çıktı
- ✅ **Kapsamlı hata yönetimi**
- ✅ **Temiz, belgelenmiş kod** adım adım açıklamalarla

### Tam Örneklerle Başlangıç

1. **Tercih ettiğiniz dili seçin** yukarıdaki tablodan
2. **Tam örnek dosyasını inceleyin** tam uygulamayı anlamak için
3. **Örneği çalıştırın** [`complete_examples.md`](./complete_examples.md) içindeki talimatları takip ederek
4. **Örneği değiştirin ve genişletin** kendi kullanım durumunuz için

Bu örneklerin çalıştırılması ve özelleştirilmesi hakkında ayrıntılı dokümantasyon için bkz: **[📖 Tam Örnekler Dokümantasyonu](./complete_examples.md)**

### 💡 Çözüm Klasörü vs. Tam Örnekler

| **Çözüm Klasörü** | **Tam Örnekler** |
|--------------------|--------------------- |
| Derleme dosyaları ile tam proje yapısı | Tek dosyalık uygulamalar |
| Bağımlılıklarla çalışmaya hazır | Odaklanmış kod örnekleri |
| Üretim benzeri kurulum | Eğitici referans |
| Dil spesifik araçlar | Diller arası karşılaştırma |

Her iki yaklaşım değerlidir - tam projeler için **çözüm klasörünü** ve öğrenme ve referans için **tam örnekleri** kullanın.

## Ana Noktalar

Bu bölümün ana noktaları müşteriler hakkında şunlardır:

- Hem sunucu özelliklerini keşfetmek hem de çağırmak için kullanılabilirler.
- Kendi başına başlarken bir sunucuyu başlatabilirler (bu bölümde olduğu gibi) ancak müşteriler aynı zamanda çalışan sunuculara da bağlanabilir.
- Önceki bölümde açıklandığı gibi, Inspector gibi alternatiflerin yanında sunucu yeteneklerini test etmek için harika bir yöntemdir.

## Ek Kaynaklar

- [MCP'de istemci oluşturma](https://modelcontextprotocol.io/quickstart/client)

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python)
- [Rust Hesap Makinesi](../../../../03-GettingStarted/samples/rust)

## Sonraki

- Sonraki: [LLM ile istemci oluşturma](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->