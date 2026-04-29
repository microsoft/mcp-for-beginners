# LLM ile bir istemci oluşturma

Şimdiye kadar nasıl bir sunucu ve istemci oluşturulacağını gördünüz. İstemci, sunucuyu açıkça çağırarak araçlarını, kaynaklarını ve istemlerini listeleyebiliyordu. Ancak bu çok pratik bir yaklaşım değildir. Kullanıcılarınız ajan çağına yaşıyor ve istemleri kullanmayı ve bir LLM ile iletişim kurmayı bekliyorlar. Kabiliyetlerinizi depolamak için MCP kullanıp kullanmadığınız umurlarında değil; sadece doğal dil kullanarak etkileşimde bulunmayı bekliyorlar. Peki bunu nasıl çözeriz? Çözüm, istemciye bir LLM eklemektir.

## Genel Bakış

Bu derste, istemcinize bir LLM eklemeye odaklanacağız ve bunun kullanıcı için çok daha iyi bir deneyim sağladığını göstereceğiz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Bir LLM ile istemci oluşturmak.
- Bir LLM kullanarak MCP sunucusu ile sorunsuz etkileşim kurmak.
- İstemci tarafında daha iyi bir son kullanıcı deneyimi sunmak.

## Yaklaşım

Almamız gereken yaklaşımı anlamaya çalışalım. Bir LLM eklemek basit görünüyor, ama bunu gerçekten yapacak mıyız?

İstemcinin sunucu ile etkileşimi şöyle olacak:

1. Sunucu ile bağlantı kurmak.

1. Kabiliyetleri, istemleri, kaynakları ve araçları listelemek ve bunların şemasını kaydetmek.

1. Bir LLM eklemek ve kaydedilen kabiliyetleri ve şemalarını LLM'nin anlayacağı formatta geçirmek.

1. Kullanıcı istemini, istemcinin listelediği araçlarla birlikte LLM'ye iletmek.

Harika, şimdi yüksek seviyede bunu nasıl yapacağımızı anladık, aşağıdaki alıştırmada denemeye başlayalım.

## Alıştırma: LLM ile bir istemci oluşturma

Bu alıştırmada, istemcimize bir LLM eklemeyi öğreneceğiz.

### GitHub Kişisel Erişim Token'ı (PAT) ile Kimlik Doğrulama

GitHub token oluşturmak basit bir işlemdir. İşte nasıl yapacağınız:

- GitHub Ayarlarına gidin – Sağ üst köşedeki profil resminize tıklayın ve Ayarlar kısmını seçin.
- Geliştirici Ayarlarına geçin – Aşağı kaydırın ve Geliştirici Ayarları'na tıklayın.
- Kişisel Erişim Tokenlarını seçin – Hassas tokenlere tıklayın ve Yeni token oluştur seçeneğini seçin.
- Token'ınızı yapılandırın – Referans için bir not ekleyin, son kullanma tarihi belirleyin ve gerekli kapsamları (izinleri) seçin. Bu durumda Models izni eklediğinizden emin olun.
- Token'ı oluşturun ve kopyalayın – Token Oluştur'a tıklayın ve hemen kopyalayın, çünkü bir daha göremeyeceksiniz.

### -1- Sunucuya bağlanma

İstemcimizi önce oluşturalım:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Şema doğrulama için zod'u içe aktar

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

Önceki kodda:

- Gerekli kütüphaneleri içe aktardık.
- `client` ve `openai` adında iki üyeye sahip bir sınıf oluşturduk, bunlar sırasıyla istemce yönetmek ve LLM ile etkileşim kurmak için kullanılır.
- LLM örneğimizi GitHub Modellerini kullanacak şekilde `baseUrl`'yi inference API'ye işaret edecek şekilde yapılandırdık.

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

Önceki kodda:

- MCP için gerekli kütüphaneleri içe aktardık.
- Bir istemci oluşturduk.

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

Öncelikle, MCP entegrasyonu ve GitHub Modelleri desteğini etkinleştirmek için `pom.xml` dosyanıza LangChain4j bağımlılıklarını eklemeniz gerekir:

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

Sonra Java istemci sınıfınızı oluşturun:

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
    
    public static void main(String[] args) throws Exception {        // LLM'yi GitHub Modellerini kullanacak şekilde yapılandır
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Sunucuya bağlanmak için MCP taşıyıcısı oluştur
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP istemcisi oluştur
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Önceki kodda:

- **LangChain4j bağımlılıklarını ekledik**: MCP entegrasyonu, OpenAI resmi istemcisi ve GitHub Modelleri desteği için gerekli.
- **LangChain4j kütüphanelerini içe aktardık**: MCP entegrasyonu ve OpenAI sohbet modeli işlevselliği için.
- **GitHub token ile yapılandırılmış `ChatLanguageModel` oluşturduk**.
- **HTTP taşıması kurduk**: MCP sunucusuna bağlanmak için Server-Sent Events (SSE) kullanarak.
- **Bir MCP istemcisi oluşturduk**: Sunucu ile iletişimi yönetecek.
- **LangChain4j'nin yerleşik MCP desteği kullanıldı**: LLM'ler ile MCP sunucuları arasındaki entegrasyonu basitleştirir.

#### Rust

Bu örnek, Rust tabanlı bir MCP sunucunuzun çalışıyor olduğunu varsayar. Yoksa, sunucu oluşturmak için [01-first-server](../01-first-server/README.md) dersine bakabilirsiniz.

Rust MCP sunucunuza sahip olduktan sonra terminal açın ve sunucunun bulunduğu dizine gidin. Ardından yeni bir LLM istemci projesi oluşturmak için aşağıdaki komutu çalıştırın:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` dosyanıza aşağıdaki bağımlılıkları ekleyin:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Resmi bir Rust için OpenAI kütüphanesi yok, ancak `async-openai` crate'i yaygın kullanılan bir [topluluk destekli kütüphanedir](https://platform.openai.com/docs/libraries/rust#rust).

`src/main.rs` dosyasını açın ve içeriğini aşağıdaki kodla değiştirin:

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
    // Başlangıç mesajı
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI istemcisi ayarla
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP istemcisi ayarla
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

    // YAPILACAK: MCP araç listesini al

    // YAPILACAK: Araç çağrıları ile LLM sohbeti

    Ok(())
}
```

Bu kod, bir MCP sunucusuna ve LLM etkileşimleri için GitHub Modellerine bağlanacak temel bir Rust uygulaması kurar.

> [!IMPORTANT]
> Uygulamayı çalıştırmadan önce `OPENAI_API_KEY` ortam değişkenini GitHub token'ınızla ayarladığınızdan emin olun.

Harika, sonraki adım olarak sunucudaki kabiliyetleri listeleyelim.

### -2- Sunucu kabiliyetlerini listele

Şimdi sunucuya bağlanıp kabiliyetlerini soracağız:

#### TypeScript

Aynı sınıfa aşağıdaki metodları ekleyin:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // araçları listeleme
    const toolsResult = await this.client.listTools();
}
```

Önceki kodda:

- `connectToServer` metodu ile sunucuya bağlantı kurma kodu ekledik.
- Uygulama akışımızı yönetecek `run` metodu oluşturduk. Şimdilik sadece araçları listeliyor ama yakında daha fazlasını ekleyeceğiz.

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
    print("Tool", tool.inputSchema["properties"])
```

Eklediklerimiz:

- Kaynakları ve araçları listeleyip yazdırdık. Araçlar için ayrıca daha sonra kullanmak üzere `inputSchema`'yı da listeledik.

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

Önceki kodda:

- MCP Sunucusundaki mevcut araçları listeledik.
- Her araç için adını, açıklamasını ve şemasını yazdırdık. Şemayı kısa süre sonra araç çağırmada kullanacağız.

#### Java

```java
// MCP araçlarını otomatik olarak keşfeden bir araç sağlayıcı oluşturun
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP araç sağlayıcı otomatik olarak şunları yönetir:
// - MCP sunucusundan mevcut araçları listeleme
// - MCP araç şemalarını LangChain4j formatına dönüştürme
// - Araç yürütme ve yanıtları yönetme
```

Önceki kodda:

- MCP sunucusundaki tüm araçları otomatik keşfeden ve kaydeden bir `McpToolProvider` oluşturduk.
- Araç sağlayıcı, MCP araç şemalarının LangChain4j araç formatına dönüşümünü dahili olarak yapıyor.
- Bu yöntem, araçları manuel listeleme ve dönüştürme işini soyutlar.

#### Rust

MCP sunucusundan araçları almak için `list_tools` metodunu kullanıyoruz. `main` fonksiyonunuzda MCP istemcisi kurulduktan sonra şunu ekleyin:

```rust
// MCP araç listesini alın
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Sunucu kabiliyetlerini LLM araçlarına dönüştürme

Sunucu kabiliyetlerini listeledikten sonraki adım, bunları LLM'nin anlayacağı formata dönüştürmektir. Bunu yapınca, bu kabiliyetleri LLM için araçlar olarak sunabiliriz.

#### TypeScript

1. MCP sunucusundan gelen yanıtı LLM'nin kullanabileceği araç formatına dönüştürmek için aşağıdaki kodu ekleyin:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema temel alınarak bir zod şeması oluşturun
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Tür açıkça "function" olarak ayarlandı
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

    Yukarıdaki kod MCP Sunucusundan gelen yanıtı alır ve LLM'nin anlayacağı araç tanımı formatına dönüştürür.

1. Sonra `run` metodunu sunucu kabiliyetlerini listeleyecek şekilde güncelleyelim:

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

    Önceki kodda `run` metodu, sonucu döngüyle dolaşıp her giriş için `openAiToolAdapter`'ı çağıracak şekilde güncellendi.

#### Python

1. Önce aşağıdaki dönüştürücü fonksiyonu oluşturalım

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

    Yukarıdaki `convert_to_llm_tools` fonksiyonu, MCP araç yanıtını LLM'nin anlayacağı formata dönüştürür.

1. Sonra istemci kodumuzu bu fonksiyonu kullanacak şekilde güncelleyelim:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Burada MCP araç yanıtını LLM'ye besleyebileceğimiz bir şeye dönüştürmek için `convert_to_llm_tool` çağrısı ekledik.

#### .NET

1. MCP araç yanıtını LLM'nin anlayacağı formata dönüştüren kod ekleyelim

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

Önceki kodda:

- İsim, açıklama ve girdi şemasını alan `ConvertFrom` fonksiyonu oluşturduk.
- Bir FunctionDefinition yaratan fonksiyonellik tanımlandı ve bu ChatCompletionsDefinition'a geçiriliyor. Bu LLM'nin anlayabileceği bir yapıdır.

1. Yukarıdaki fonksiyondan faydalanmak için mevcut kodu nasıl güncelleyebileceğimize bakalım:

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
// Doğal dil etkileşimi için bir Bot arayüzü oluşturun
public interface Bot {
    String chat(String prompt);
}

// LLM ve MCP araçları ile AI hizmetini yapılandırın
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Önceki kodda:

- Doğal dil etkileşimleri için basit bir `Bot` arayüzü tanımlandı.
- MCP araç sağlayıcısı ile LLM'yi otomatik bağlamak için LangChain4j'nin `AiServices` özelliği kullanıldı.
- Çerçeve, araç şeması dönüşümü ve fonksiyon çağrılarını otomatik olarak yönetiyor.
- Bu yöntem, manuel araç dönüşümünü ortadan kaldırıyor — LangChain4j MCP araçlarını LLM uyumlu formata dönüştürmenin tüm karmaşıklığını hallediyor.

#### Rust

MCP araç yanıtını LLM'nin anlayacağı formata dönüştürmek için yardımcı bir fonksiyon ekleyeceğiz. `main` fonksiyonunuzun altına aşağıdaki kodu ekleyin. Bu fonksiyon LLM istekleri yapılırken çağrılacak:

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

Harika, kullanıcı isteklerini işlemek için ayarlandık, şimdi buna geçelim.

### -4- Kullanıcı istemini işleme

Bu kod kısmında kullanıcı isteklerini ele alacağız.

#### TypeScript

1. LLM'yi çağırmak için kullanılacak metodu ekleyin:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Sunucunun aracını çağır
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Sonuç ile bir şeyler yap
        // YAPILACAKLAR

        }
    }
    ```

    Önceki kodda:

    - `callTools` metodunu ekledik.
    - Bu metod, LLM yanıtını alır ve hangi araçların çağrıldığını kontrol eder, varsa çağırır:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // aracı çağır
        }
        ```

    - LLM çağırılması gereken bir aracı gösteriyorsa o aracı çağırır:

        ```typescript
        // 2. Sunucunun aracını çağır
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Sonuçla bir şey yap
        // YAPILACAKLAR
        ```

1. `run` metodunu LLM çağrısını ve `callTools` çağrısını içerecek şekilde güncelleyin:

    ```typescript

    // 1. LLM için giriş olan mesajlar oluşturun
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM'yi çağırma
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM yanıtını inceleyin, her seçenek için araç çağrısı olup olmadığını kontrol edin
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Harika, kodun tamamı şöyle:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Şema doğrulama için zod'u içe aktar

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // gelecekte bu URL'ye değiştirilmesi gerekebilir: https://models.github.ai/inference
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
          // input_schema'ya dayalı bir zod şeması oluştur
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Türü açıkça "function" olarak ayarla
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
    
    
          // 2. Sunucunun aracını çağır
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Sonuçla bir şeyler yap
          // YAPILACAK
    
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
    
        // 1. LLM yanıtını kontrol et, her seçenek için araç çağrısı olup olmadığını kontrol et
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

1. LLM çağrısı için gereken bazı kütüphane içe aktarımlarını ekleyelim:

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Ardından LLM'yi çağıracak fonksiyonu ekleyelim:

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
            # İsteğe bağlı parametreler
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

    Önceki kodda:

    - MCP sunucusunda bulduğumuz ve dönüştürdüğümüz fonksiyonları LLM'ye geçtik.
    - Ardından bu fonksiyonlarla LLM'yi çağırdık.
    - Sonucu inceleyerek hangi fonksiyonların çağrılması gerektiğine baktık.
    - Son olarak çağrılacak fonksiyonlar dizisini geçtik.

1. Son adım, ana kodumuzu güncelleyelim:

    ```python
    prompt = "Add 2 to 20"

    # LLM'ye hangi araçların, varsa, kullanılacağını sor
    functions_to_call = call_llm(prompt, functions)

    # önerilen fonksiyonları çağır
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Son adımda kodda:

    - LLM'nizin promptuna göre çağrılması gereken MCP aracını `call_tool` ile çağırıyoruz.
    - MCP Sunucusundan gelen aracın sonuçlarını yazdırıyoruz.

#### .NET

1. LLM istemini çağırmak için örnek kod gösterelim:

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

Önceki kodda:

- MCP sunucusundan araçlar alındı, `var tools = await GetMcpTools()`.
- Kullanıcı promptu tanımlandı, `userMessage`.
- Model ve araçları belirten seçenekler oluşturuldu.
- LLM'ye istek gönderildi.

1. Son olarak, LLM'nin fonksiyon çağrısı yapmak isteyip istemediğine bakalım:

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

Önceki kodda:

- Fonksiyon çağrıları listesinin üzerinden döngü yapıldı.
- Her araç çağrısı için isim ve argümanlar ayrıştırılarak MCP istemci kullanılarak araç çağrıldı. Sonuçlar yazdırıldı.

Kodun tamamı:

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

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // MCP araçlarını otomatik olarak kullanan doğal dil isteklerini çalıştırın
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

Önceki kodda:

- MCP sunucu araçlarıyla basit doğal dil istemleri kullanarak etkileşim sağlandı.
- LangChain4j çerçevesi otomatik olarak:
  - Kullanıcı istemlerini gerektiğinde araç çağrısına dönüştürür.
  - LLM'nin kararına göre uygun MCP araçlarını çağırır.
  - LLM ve MCP sunucu arasında konuşma akışını yönetir.
- `bot.chat()` metodu, MCP araçlarının sonuçlarını içerebilen doğal dil yanıtlarını döner.
- Bu yöntem, kullanıcıların altta yatan MCP uygulamasını bilmelerine gerek kalmadan kesintisiz bir deneyim sağlar.

Tam kod örneği:

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

İşin çoğu burada gerçekleşir. İlk kullanıcı istemi ile LLM'yi çağıracağız, sonra yanıtı işleyip araç çağrısı yapıp yapmama kararı vereceğiz. Eğer araç çağrısı gerekirse çağıracağız ve LLM ile konuşmaya devam edeceğiz, araç çağrısı kalmayana ve nihai yanıt oluşana kadar.

Birden çok kez LLM çağrısı yapacağımız için, LLM çağrısını yönetecek bir fonksiyon tanımlayalım. `main.rs` dosyanıza aşağıdaki fonksiyonu ekleyin:

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

Bu fonksiyon LLM istemcisi, mesaj listesi (kullanıcı istemi dahil), MCP araçları alır ve LLM'ye istek gönderip yanıtı döner.
LLM yanıtı `choices` dizisi içerecektir. Sonuçta herhangi bir `tool_calls` olup olmadığını görmek için sonucu işlememiz gerekecek. Bu, LLM'nin belirtilen argümanlarla belirli bir aracın çağrılmasını istediğini anlamamızı sağlar. Aşağıdaki kodu `main.rs` dosyanızın sonuna ekleyerek LLM yanıtını işlemek için bir fonksiyon tanımlayın:

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

    // İçerik varsa yazdır
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Araç çağrılarını işle
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Asistan mesajı ekle

        // Her araç çağrısını yürüt
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Araç sonucunu mesajlara ekle
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Araç sonuçları ile konuşmaya devam et
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
  
`tool_calls` varsa, araç bilgilerini çıkarır, aracın isteği ile MCP sunucusunu çağırır ve sonuçları sohbet mesajlarına ekler. Daha sonra LLM ile sohbet devam eder ve mesajlar asistanın yanıtı ve araç çağrısı sonuçlarıyla güncellenir.

LLM tarafından MCP çağrıları için döndürülen araç çağrısı bilgisinin tamamını çıkarmak için başka bir yardımcı fonksiyon daha ekleyeceğiz. Aşağıdaki kodu `main.rs` dosyanızın sonuna ekleyin:

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
  
Tüm parçalar yerli yerinde olduğunda, ilk kullanıcı istemini işleyip LLM'yi çağırabiliriz. `main` fonksiyonunuzu aşağıdaki kodu içerecek şekilde güncelleyin:

```rust
// Araç çağrıları ile LLM sohbeti
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
  
Bu, LLM'yi iki sayının toplamını isteyen ilk kullanıcı istemiyle sorgulayacak ve yanıtı işleyerek dinamik olarak araç çağrılarını işleyecektir.

Harika, başardınız!

## Ödev

Egzersizden aldığınız kodu kullanarak sunucuyu daha fazla araçla oluşturun. Ardından egzersizdeki gibi bir LLM ile istemci oluşturun ve farklı istemlerle test ederek tüm sunucu araçlarınızın dinamik olarak çağrıldığından emin olun. Bu istemci oluşturma yöntemi, son kullanıcının kesin istemci komutları yerine istemler kullanabilmesine ve arka planda herhangi bir MCP sunucusunun çağrılmasından habersiz iyi bir kullanıcı deneyimi yaşamasına olanak tanır.

## Çözüm

[Çözüm](./solution/README.md)

## Temel Çıkarımlar

- İstemcinize bir LLM eklemek, kullanıcıların MCP Sunucularıyla etkileşimini daha iyi hale getirir.
- MCP Sunucu yanıtını LLM'nin anlayabileceği bir şeye dönüştürmeniz gerekir.

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python)
- [Rust Hesap Makinesi](../../../../03-GettingStarted/samples/rust)

## Ek Kaynaklar

## Sonraki Adımlar

- Sonraki: [Visual Studio Code kullanarak bir sunucu tüketmek](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanılması nedeniyle ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->