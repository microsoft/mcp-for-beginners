# Bir istemci oluşturma

İstemciler, kaynaklar, araçlar ve istemler talep etmek için doğrudan bir MCP Sunucusuyla iletişim kuran özel uygulamalar veya betiklerdir. Sunucu ile etkileşim için grafiksel arayüz sağlayan denetleyici aracını kullanmaktan farklı olarak, kendi istemcinizi yazmak programlı ve otomatik etkileşimlere olanak tanır. Bu, geliştiricilerin MCP yeteneklerini kendi iş akışlarına entegre etmelerine, görevleri otomatikleştirmelerine ve belirli ihtiyaçlara yönelik özel çözümler inşa etmelerine olanak sağlar.

## Genel Bakış

Bu ders, Model Context Protocol (MCP) ekosisteminde istemciler kavramını tanıtır. Kendi istemcinizi nasıl yazacağınızı ve bunu bir MCP Sunucusuna nasıl bağlayacağınızı öğreneceksiniz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Bir istemcinin neler yapabileceğini anlamak.
- Kendi istemcinizi yazmak.
- İstemciyi bir MCP sunucusuna bağlayıp test etmek, böylece sunucunun beklendiği gibi çalıştığını doğrulamak.

## Bir istemci yazarken neler yapılır?

Bir istemci yazabilmek için aşağıdakileri yapmanız gerekir:

- **Doğru kütüphaneleri içe aktarın**. Öncekiyle aynı kütüphaneyi kullanacaksınız, sadece farklı yapılar olacak.
- **Bir istemci örneği oluşturun**. Bu, bir istemci örneği yaratmayı ve seçilen taşıma yöntemi ile bağlanmayı içerecek.
- **Hangi kaynakların listeleneceğine karar verin**. MCP sunucunuz kaynaklar, araçlar ve istemler içerir, hangilerini listeleyeceğinize karar vermelisiniz.
- **İstemciyi bir ana uygulamaya entegre edin**. Sunucunun yeteneklerini öğrendikten sonra, eğer bir kullanıcı istem veya başka bir komut yazarsa karşılık gelen sunucu özelliğinin çağrılması için bunu ana uygulamanıza entegre etmelisiniz.

Şimdi genel olarak ne yapacağımızı anladığımıza göre, hemen ardından bir örneğe bakalım.

### Bir örnek istemci

Bu örnek istemciye bir göz atalım:

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

// Bir isteği al
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

- Kütüphaneler içe aktarıldı
- Bir istemci örneği oluşturuldu ve stdio ile taşıma için bağlandı.
- İstemler, kaynaklar ve araçlar listelendi ve hepsi çağrıldı.

İşte karşınızda MCP Sunucusu ile konuşabilen bir istemci.

Bir sonraki alıştırma bölümünde her kod parçasını ayrıntılarıyla inceleyip neyin ne olduğunu açıklayalım.

## Alıştırma: Bir istemci yazma

Yukarıda da belirtildiği gibi, kodu açıklarken zaman ayıralım ve isterseniz birlikte kod da yazabilirsiniz.

### -1- Kütüphaneleri içe aktarma

Gereken kütüphaneleri içe aktaralım, bir istemciye ve seçtiğimiz taşıma protokolü olan stdio’ya referans ihtiyacımız olacak. Stdio, yerel makinenizde çalıştırılmak üzere tasarlanmış bir protokoldür. Gelecek bölümlerde göstereceğimiz SSE ise başka bir taşıma protokolüdür, ancak şimdilik stdio ile devam edelim.

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

Java için, önceki alıştırmadaki MCP sunucusuna bağlanan bir istemci oluşturacaksınız. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) içindeki aynı Java Spring Boot proje yapısını kullanarak, `src/main/java/com/microsoft/mcp/sample/client/` klasöründe `SDKClient` adında yeni bir Java sınıfı oluşturup aşağıdaki importları ekleyin:

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

### -2- İstemci ve taşıma örneklemek

Taşımanın ve istemcimizin birer örneğini oluşturmamız gerekir:

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

- Stdio taşıma örneği oluşturuldu. Komut ve argümanlarıyla sunucunun nasıl bulunup başlatılacağını belirtiyor; çünkü istemciyi oluştururken bunu yapmamız gerekiyor.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Bir isim ve sürüm vererek istemci örnekledi.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- İstemci seçilen taşıma ile bağlandı.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Stdio bağlantısı için sunucu parametreleri oluştur
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

- Gerekli kütüphaneler içe aktarıldı
- Sunucuyu çalıştırmak için kullanılacak parametreler nesnesi oluşturuldu, böylece istemcimizle bağlanabiliriz.
- `stdio_client` çağıran ve istemci oturumu başlatan bir `run` metodu tanımlandı.
- `asyncio.run`'a `run` metodu sağlayan giriş noktası oluşturuldu.

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
- Bir stdio taşıma ve `mcpClient` isminde bir istemci oluşturuldu. Bu, MCP Sunucusu üzerindeki özellikleri listelemek ve çağırmak için kullanılacak.

Dikkat edin, "Arguments" kısmında ya *.csproj* dosyasını ya da yürütülebilir dosyayı gösterebilirsiniz.

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
        
        // İstemci mantığınız buraya gider
    }
}
```

Yukarıdaki kodda:

- MCP sunucumuzun çalışacağı `http://localhost:8080` adresine işaret eden SSE taşıma kuran ana metodu oluşturdu.
- Taşıma nesnesini parametre alan bir istemci sınıfı kurdu.
- `run` metodunda taşıma ile senkron MCP istemcisi oluşturup bağlantıyı başlattı.
- Java Spring Boot MCP sunucuları ile HTTP tabanlı iletişim için uygun SSE (Sunucu Gönderimli Olaylar) taşıma kullanıldı.

#### Rust

Bu Rust istemcisi, sunucunun aynı dizindeki "calculator-server" adlı kardeş proje olduğunu varsayar. Aşağıdaki kod sunucuyu başlatıp ona bağlanacaktır.

```rust
async fn main() -> Result<(), RmcpError> {
    // Sunucunun aynı dizinde "calculator-server" adında bir kardeş proje olduğunu varsay
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

    // TODO: {"a": 3, "b": 2} argümanları ile add aracını çağır

    client.cancel().await?;
    Ok(())
}
```

### -3- Sunucu özelliklerini listeleme

Artık program çalıştırıldığında bağlanabilecek bir istemcimiz var. Ancak, özelliklerini listelemiyor; şimdi bunu yapalım:

#### TypeScript

```typescript
// Promtları listele
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

Burada mevcut kaynaklar `list_resources()` ve araçlar `list_tools` listelenir ve ekrana yazdırılır.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Yukarıda, sunucudaki araçların nasıl listeleneceğine dair bir örnek var. Her araç için adını yazdırıyoruz.

#### Java

```java
// Araçları listeleyin ve gösterin
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Bağlantıyı doğrulamak için sunucuya ping atabilirsiniz
client.ping();
```

Yukarıdaki kodda:

- MCP sunucusundan tüm mevcut araçları almak için `listTools()` çağrıldı.
- Bağlantının çalıştığını doğrulamak için `ping()` kullanıldı.
- `ListToolsResult`, araçların adları, açıklamaları ve giriş şemaları dahil tüm bilgileri içerir.

Harika, şimdi tüm özellikleri aldık. Peki, bunları ne zaman kullanacağız? Bu istemci oldukça basit, yani özellikleri kullanmak istediğimizde açıkça çağırmamız gerekiyor. Sonraki bölümde kendi büyük dil modeline (LLM) erişimi olan daha gelişmiş bir istemci oluşturacağız. Şimdilik, sunucudaki özelliklerin nasıl çağrılacağını görelim:

#### Rust

Main fonksiyonunda, istemciyi başlattıktan sonra sunucuyu başlatabilir ve bazı özelliklerini listeleyebilirsiniz.

```rust
// Başlat
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Araçları listele
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Özellikleri çağırma

Özellikleri çağırmak için doğru argümanları ve bazen çağırmak istediğimiz şeyin adını belirtmemiz gerekir.

#### TypeScript

```typescript

// Bir kaynağı oku
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Bir arac çağır
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// istemi çağır
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Yukarıdaki kodda:

- Bir kaynağı okuduk; `readResource()`'ı `uri`yi belirterek çağırdık. Sunucu tarafında muhtemelen şöyle görünür:

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

    `uri` değerimiz `file://example.txt`, sunucuda `file://{name}` ile eşleşir. `example.txt`, `name` olarak eşlenir.

- Bir aracı çağırdık, ismini ve argümanlarını şu şekilde belirterek:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Bir istem almak için, `getPrompt()`'u `name` ve `arguments` ile çağırdık. Sunucu kodu şöyle görünüyor:

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

    Böylece istemci kodunuz sunucuda tanımlanana uygun olur:

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

# Bir araç çağır
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Yukarıdaki kodda:

- `greeting` adındaki kaynağı `read_resource` ile çağırdık.
- `add` adındaki aracı `call_tool` ile çağırdık.

#### .NET

1. Bir aracı çağırmak için biraz kod ekleyelim:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Sonucu yazdırmak için işte biraz kod:

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

- `callTool()` metodunu kullanarak `CallToolRequest` nesneleriyle birçok hesap makinesi aracını çağırdı.
- Her çağrıda aracın adı ve o araç için gereken argümanların bir `Map`i verildi.
- Sunucu araçları, matematiksel işlemler için "a", "b" gibi belirli parametre isimleri bekler.
- Sonuçlar, sunucudan gelen yanıtı içeren `CallToolResult` nesneleri olarak döner.

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

İstemciyi çalıştırmak için terminalde aşağıdaki komutu yazın:

#### TypeScript

*package.json* dosyanızdaki "scripts" bölümüne aşağıdaki girdiyi ekleyin:

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

Alternatif olarak, çözüm klasöründeki `03-GettingStarted\02-client\solution\java` içindeki tamamlanmış istemci projesini çalıştırabilirsiniz:

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

Kullanmanız gereken bir sunucu var; istemci kodunuzla bu sunucuyu çağırmanız gerekiyor. Sunucuyu daha ilginç hale getirmek için ona daha fazla özellik ekleyip ekleyemeyeceğinize bakın.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Bir MCP sunucusu oluştur
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Bir ek araç ekle
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dinamik bir karşılama kaynağı ekle
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

// stdin üzerinde mesaj almayı ve stdout üzerinde mesaj göndermeyi başlat

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

# Bir MCP sunucusu oluştur
mcp = FastMCP("Demo")


# Bir toplama aracı ekle
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dinamik bir karşılama kaynağı ekle
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

Bu projeye bakarak [istemler ve kaynaklar nasıl eklenir](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) öğrenebilirsiniz.

Ayrıca, bu bağlantı üzerinden [istemler ve kaynaklar nasıl çağrılır](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) bakabilirsiniz.

### Rust

[Önceki bölümde](../../../../03-GettingStarted/01-first-server), Rust ile basit bir MCP sunucusunun nasıl oluşturulacağını öğrendiniz. Devam edebilir veya daha fazla Rust temelli MCP sunucusu örnekleri için şu bağlantıya bakabilirsiniz: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Çözüm

**Çözüm klasörü** bu eğitimde ele alınan tüm kavramları gösteren tam, çalışmaya hazır istemci uygulamalarını içerir. Her çözüm, istemci ve sunucu kodunu ayrı, bağımsız projelerde düzenler.

### 📁 Çözüm Yapısı

Çözüm dizini programlama dillerine göre organize edilmiştir:

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

### 🚀 Her Çözüm Neler İçerir

Her dil özel çözümünde:

- **Eğitimdeki tüm özellikleri içeren tam istemci uygulaması**
- **Doğru bağımlılıklar ve yapılandırmalarla çalışan proje yapısı**
- **Kolay kurulum ve çalıştırma için build ve çalıştırma scriptleri**
- **Dil özel yönergelerle ayrıntılı README dosyası**
- **Hata yönetimi ve sonuç işleme örnekleri**

### 📖 Çözümleri Kullanma

1. **Tercih ettiğiniz dil klasörüne gidin**:

   ```bash
   cd solution/typescript/    # TypeScript için
   cd solution/java/          # Java için
   cd solution/python/        # Python için
   cd solution/dotnet/        # .NET için
   ```

2. **Her klasördeki README talimatlarını izleyin**:
   - Bağımlılıkların kurulumu
   - Projenin derlenmesi
   - İstemcinin çalıştırılması

3. **Görmeniz gereken örnek çıktı**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Tam belgeler ve adım adım talimatlar için bkz: **[📖 Çözüm Belgelendirmesi](./solution/README.md)**

## 🎯 Tam Örnekler

Bu eğitimde ele alınan tüm programlama dilleri için tam, çalışan istemci uygulamaları sağladık. Bu örnekler yukarıda açıklanan tüm işlevselliği gösterir ve referans uygulamalar veya kendi projeleriniz için başlangıç noktası olarak kullanılabilir.

### Mevcut Tam Örnekler

| Dil | Dosya | Açıklama |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kapsamlı hata yönetimiyle SSE taşıma kullanan tam Java istemcisi |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Otomatik sunucu başlatma ile stdio taşıma kullanan tam C# istemcisi |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Tüm MCP protokolü desteğine sahip tam TypeScript istemcisi |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Async/await desenleri kullanan tam Python istemcisi |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio ile asenkron işlemleri yürüten tam Rust istemcisi |

Her tam örnek şunları içerir:

- ✅ **Bağlantı kurulumu ve hata yönetimi**
- ✅ **Sunucu keşfi** (araçlar, kaynaklar, istemler uygulanabiliyorsa)
- ✅ **Hesap makinesi işlemleri** (toplama, çıkarma, çarpma, bölme, yardım)
- ✅ **Sonuç işlemler ve biçimlendirilmiş çıktı**
- ✅ **Kapsamlı hata yönetimi**

- ✅ **Adım adım yorumlarla temiz, belgelenmiş kod**

### Tam Örneklerle Başlarken

1. Yukarıdaki tablodan **tercih ettiğiniz dili seçin**
2. Tam uygulamayı anlamak için **tam örnek dosyasını inceleyin**
3. [`complete_examples.md`](./complete_examples.md) içindeki talimatlara göre **örneği çalıştırın**
4. Özel kullanım durumunuz için örneği **değiştirin ve genişletin**

Bu örneklerin çalıştırılması ve özelleştirilmesi hakkında ayrıntılı dokümantasyon için bkz: **[📖 Tam Örnekler Dokümantasyonu](./complete_examples.md)**

### 💡 Çözüm vs. Tam Örnekler

| **Çözüm Klasörü** | **Tam Örnekler** |
|--------------------|--------------------- |
| Derleme dosyaları ile tam proje yapısı | Tek dosya uygulamaları |
| Bağımlılıklarıyla çalıştırmaya hazır | Odaklanmış kod örnekleri |
| Prodüksiyona benzer kurulum | Öğretici referans |
| Dil spesifik araçlar | Diller arası karşılaştırma |

Her iki yaklaşım da değerlidir - **çözüm klasörünü** tam projeler için, **tam örnekleri** ise öğrenme ve referans için kullanın.

## Ana Hatlar

Bu bölüm için müşterilerle ilgili ana çıkarımlar şunlardır:

- Hem sunucudaki özellikleri keşfetmek hem de çağırmak için kullanılabilir.
- Kendi kendini başlatırken bir sunucu çalıştırabilir (bu bölümde olduğu gibi), ama müşteriler zaten çalışan sunuculara da bağlanabilir.
- Önceki bölümde açıklandığı gibi Inspector gibi alternatiflerin yanında sunucu yeteneklerini test etmek için harika bir yöntemdir.

## Ek Kaynaklar

- [MCP'de müşteriler oluşturma](https://modelcontextprotocol.io/quickstart/client)

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.NET Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python)
- [Rust Hesap Makinesi](../../../../03-GettingStarted/samples/rust)

## Sırada Ne Var

- Sonraki: [LLM ile bir müşteri oluşturmak](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->