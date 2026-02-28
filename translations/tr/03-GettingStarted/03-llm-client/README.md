# LLM ile bir istemci oluşturmak

Şimdiye kadar, bir sunucu ve istemci oluşturmayı gördünüz. İstemci, araçlarını, kaynaklarını ve istemlerini listelemek için sunucuyu açıkça çağırabiliyordu. Ancak bu çok pratik bir yaklaşım değil. Kullanıcılarınız ajan çağı yaşamakta ve istemleri kullanmayı, bir LLM ile iletişim kurmayı bekliyorlar. Yeteneklerinizi depolamak için MCP kullanıp kullanmadığınız umurlarında değil; sadece doğal dil kullanarak etkileşim kurmayı bekliyorlar. Peki bunu nasıl çözeriz? Çözüm, istemciye bir LLM eklemektir.

## Genel Bakış

Bu derste, istemcinize bir LLM eklemeye odaklanacağız ve bunun kullanıcılarınız için nasıl çok daha iyi bir deneyim sağladığını göstereceğiz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Bir LLM ile istemci oluşturmak.
- LLM kullanarak MCP sunucusu ile sorunsuz etkileşimde bulunmak.
- İstemci tarafında daha iyi bir son kullanıcı deneyimi sunmak.

## Yaklaşım

Almamız gereken yaklaşımı anlamaya çalışalım. LLM eklemek basit görünüyor, ama gerçekten bunu yapacak mıyız?

İstemci sunucu ile şöyle etkileşimde bulunacak:

1. Sunucu ile bağlantı kurmak.

1. Yetkinlikleri, istemleri, kaynakları ve araçları listelemek ve şemalarını kaydetmek.

1. Bir LLM eklemek ve kaydedilen yetkinlikleri ve şemalarını LLM'nin anlayacağı formatta geçirmek.

1. Kullanıcı istemini, istemcinin listelediği araçlarla birlikte LLM'ye ileterek işlemek.

Harika, şimdi bunu yüksek seviyede nasıl yapabileceğimizi anladık, aşağıdaki alıştırmada deneyelim.

## Alıştırma: Bir LLM ile istemci oluşturma

Bu alıştırmada, istemcimize bir LLM eklemeyi öğreneceğiz.

### GitHub Kişisel Erişim Belirtisi ile Kimlik Doğrulama

Bir GitHub belirtisi oluşturmak kolay bir süreçtir. İşte nasıl yapacağınız:

- GitHub Ayarlarına gidin – Sağ üst köşedeki profil resminize tıklayın ve Ayarlar'ı seçin.
- Geliştirici Ayarlarına gidin – Aşağı kaydırıp Geliştirici Ayarları'na tıklayın.
- Kişisel Erişim Belirtilerini seçin – İnce taneli belirtilere tıklayın ve Yeni belirti oluştur'u seçin.
- Belirtinizi yapılandırın – Referans için bir not ekleyin, bir son kullanma tarihi ayarlayın ve gerekli kapsamları (izinleri) seçin. Bu durumda Models iznini eklediğinizden emin olun.
- Belirtileri oluşturup kopyalayın – Belirtiyi oluştur'a tıklayın ve hemen kopyalayın, çünkü bir daha göremeyeceksiniz.

### -1- Sunucuya bağlanmak

Öncelikle istemcimizi oluşturalım:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Şema doğrulaması için zod'u içe aktarın

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

Yukarıdaki kodda şunları yaptık:

- Gerekli kütüphaneleri içe aktardık.
- İstemciyi yönetmemize ve LLM ile etkileşime geçmemize yardımcı olacak `client` ve `openai` adlı iki üyeye sahip bir sınıf oluşturduk.
- LLM örneğimizi, `baseUrl`'i çıkarım API'sine işaret edecek şekilde GitHub Modellerini kullanacak şekilde yapılandırdık.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio bağlantısı için sunucu parametreleri oluştur
server_params = StdioServerParameters(
    command="mcp",  # Çalıştırılabilir
    args=["run", "server.py"],  # Opsiyonel komut satırı argümanları
    env=None,  # Opsiyonel ortam değişkenleri
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

Yukarıdaki kodda şunları yaptık:

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

Öncelikle, LangChain4j bağımlılıklarını `pom.xml` dosyanıza eklemeniz gerekir. MCP entegrasyonu ve GitHub Modelleri desteği için şu bağımlılıkları ekleyin:

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
    
    public static void main(String[] args) throws Exception {        // LLM'yi GitHub Modellerini kullanacak şekilde yapılandırın
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Sunucuya bağlanmak için MCP iletimi oluşturun
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP istemcisi oluşturun
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Yukarıdaki kodda şunları yaptık:

- **LangChain4j bağımlılıklarını ekledik**: MCP entegrasyonu, OpenAI resmi istemcisi ve GitHub Modelleri desteği için gerekli
- **LangChain4j kütüphanelerini içe aktardık**: MCP entegrasyonu ve OpenAI sohbet modeli işlevselliği için
- **Bir `ChatLanguageModel` oluşturduk**: GitHub Modellerini GitHub belirti ile kullanacak şekilde yapılandırdık
- **HTTP taşımasını ayarladık**: MCP sunucusuna bağlanmak için Server-Sent Events (SSE) kullandık
- **Bir MCP istemcisi oluşturduk**: Sunucu ile iletişim kuracak
- **LangChain4j'nin yerleşik MCP desteğini kullandık**: Bu, LLM'ler ile MCP sunucuları arasındaki entegrasyonu kolaylaştırır

#### Rust

Bu örnek, Rust tabanlı bir MCP sunucusuna sahip olduğunuzu varsayar. Eğer yoksa, sunucuyu oluşturmak için [01-first-server](../01-first-server/README.md) dersine geri dönün.

Rust MCP sunucunuzu aldıktan sonra, bir terminal açın ve sunucu ile aynı dizine gidin. Sonra yeni bir LLM istemci projesi oluşturmak için aşağıdaki komutu çalıştırın:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` dosyanıza şu bağımlılıkları ekleyin:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Resmi bir Rust OpenAI kütüphanesi yoktur, ancak `async-openai` crate'i [topluluk tarafından bakılan bir kütüphanedir](https://platform.openai.com/docs/libraries/rust#rust) ve yaygın kullanılır.

`src/main.rs` dosyasını açın ve içeriğini şu kodla değiştirin:

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
    // İlk mesaj
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI istemcisi kurulumu
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP istemcisi kurulumu
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

    // YAPILACAK: MCP araç listesini alma

    // YAPILACAK: Araç çağrıları ile LLM sohbeti

    Ok(())
}
```

Bu kod, MCP sunucusuna ve LLM etkileşimleri için GitHub Modellerine bağlanacak temel bir Rust uygulaması kurar.

> [!IMPORTANT]
> Uygulamayı çalıştırmadan önce `OPENAI_API_KEY` ortam değişkenini GitHub belirti ile ayarladığınızdan emin olun.

Harika, şimdi bir sonraki adım olarak, sunucudaki yetenekleri listeleyelim.

### -2- Sunucu yeteneklerini listele

Şimdi sunucuya bağlanacağız ve yeteneklerini soracağız:

#### Typescript

Aynı sınıfa şu metodları ekleyin:

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

Yukarıdaki kodda şunları yaptık:

- Sunucuya bağlanmak için `connectToServer` fonksiyonunu ekledik.
- Uygulama akışımızı yöneten `run` metodunu oluşturduk. Şu ana kadar sadece araçları listeliyor ama yakında daha fazlasını ekleyeceğiz.

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

- Kaynakları ve araçları listelemek ve yazdırmak. Araçlar için ayrıca daha sonra kullanacağımız `inputSchema`'yı da listeledik.

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

Yukarıdaki kodda:

- MCP Sunucusundaki mevcut araçları listeledik.
- Her araç için isim, açıklama ve şemasını listeledik. Bu sonrakileri çağırmak için kullanacağız.

#### Java

```java
// MCP araçlarını otomatik olarak keşfeden bir araç sağlayıcı oluşturun
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP araç sağlayıcısı otomatik olarak şunları yönetir:
// - MCP sunucusundan mevcut araçları listeleme
// - MCP araç şemalarını LangChain4j formatına dönüştürme
// - Araç çalıştırma ve yanıtlarını yönetme
```

Yukarıdaki kodda:

- MCP sunucusundan tüm araçları otomatik keşfeden ve kaydeden bir `McpToolProvider` oluşturduk.
- Araç sağlayıcı, MCP araç şemalarını LangChain4j’nin araç formatına dahili olarak dönüştürür.
- Bu yöntem, manuel araç listeleme ve dönüştürme sürecini soyutlar.

#### Rust

MCP sunucusundan araç listesi almak için `list_tools` metodunu kullanıyoruz. `main` fonksiyonunuzda, MCP istemcisini ayarladıktan sonra şu kodu ekleyin:

```rust
// MCP araç listesini al
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Sunucu yeteneklerini LLM araçlarına dönüştürmek

Sunucu yeteneklerini listeledikten sonraki adım, bunları LLM'nin anlayacağı formata dönüştürmektir. Bunu yapınca bu yetenekleri LLM'ye araç olarak sağlayabiliriz.

#### TypeScript

1. MCP Sunucusunun yanıtını LLM'nin kullanabileceği araç formatına dönüştürmek için şu kodu ekleyin:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema'ye dayalı bir zod şeması oluşturun
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Türü açıkça "function" olarak ayarlayın
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

    Yukarıdaki kod, MCP Sunucu yanıtını alır ve LLM'nin anlayabileceği bir araç tanım formatına dönüştürür.

1. Şimdi `run` metodunu, sunucu yeteneklerini listeleyecek şekilde güncelleyelim:

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

    Yukarıdaki kodda, `run` metodunu sonuç üzerinden geçecek ve her girdiye `openAiToolAdapter`'ı çağıracak şekilde güncelledik.

#### Python

1. Önce şu dönüştürücü fonksiyonu oluşturalım:

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

    `convert_to_llm_tools` fonksiyonunda MCP araç yanıtını alıp LLM’nin anlayacağı formata dönüştürüyoruz.

1. Ardından, istemci kodumuzu bu fonksiyonu kullanacak şekilde güncelleyelim:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Burada, MCP araç yanıtını LLM'ye besleyebileceğimiz bir formata dönüştürmek için `convert_to_llm_tool` fonksiyonunu çağırıyoruz.

#### .NET

1. MCP araç yanıtını LLM’nin anlayacağı bir formata dönüştürmek için kod ekleyelim

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

Yukarıdaki kodda:

- İsim, açıklama ve giriş şemasını alan `ConvertFrom` fonksiyonunu oluşturduk.
- Bir `FunctionDefinition` oluşturup bunu `ChatCompletionsDefinition` içine aktaracak fonksiyonelliği tanımladık. Sonraki LLM'nin anlayabileceği formata dönüştürme kısmıdır.

1. Bu fonksiyonu kullanmak için mevcut kodlardan bazılarını güncelleyelim:

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

// LLM ve MCP araçları ile AI servisini yapılandırın
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Yukarıdaki kodda:

- Doğal dil etkileşimleri için basit bir `Bot` arayüzü tanımladık.
- LangChain4j'nin `AiServices`'ini kullanarak LLM ile MCP araç sağlayıcıyı otomatik bağladık.
- Çerçeve, arka planda araç şeması dönüştürme ve fonksiyon çağrısını otomatik yapar.
- Bu yöntem manuel araç dönüştürmesini ortadan kaldırır – LangChain4j MCP araçlarını LLM uyumlu formatlara dönüştürmenin tüm karmaşıklığını halleder.

#### Rust

MCP araç yanıtını LLM'nin anlayacağı bir formata dönüştürmek için araç listesini formatlayan yardımcı bir fonksiyon ekleyeceğiz. `main.rs` dosyanıza `main` fonksiyonunun altına şu kodu ekleyin. Bu, LLM'ye yapılacak isteklerde çağrılacaktır:

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

Harika, şimdi kullanıcı isteklerini işlemeye hazırız, bunu ele alalım.

### -4- Kullanıcı istemi isteğini işlemek

Bu kısımda kullanıcı isteklerini işliyor olacağız.

#### TypeScript

1. LLM'yi çağırmak için kullanılacak bir metod ekleyin:

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

        // 3. Sonuçla bir şey yap
        // YAPILACAKLAR

        }
    }
    ```

    Yukarıdaki kodda:

    - `callTools` metodunu ekledik.
    - Metod, LLM yanıtını alır ve hangi araçların çağrıldığını kontrol eder, varsa çağırır:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // aracı çağır
        }
        ```

    - LLM bir aracı çağırması gerektiğini belirtirse, aracı çağırır:

        ```typescript
        // 2. Sunucunun aracını çağır
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Sonuç ile bir şeyler yap
        // YAPILACAKLAR
        ```

1. `run` metodunu, LLM çağrılarını ve `callTools` çağrısını içerecek şekilde güncelleyelim:

    ```typescript

    // 1. LLM için giriş olan mesajları oluşturun
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM çağrılıyor
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM yanıtını inceleyin, her seçim için araç çağrısı olup olmadığını kontrol edin
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Harika, tüm kodu aşağıda listeleyelim:

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
            baseURL: "https://models.inference.ai.azure.com", // gelecekte bu URL'ye geçilmesi gerekebilir: https://models.github.ai/inference
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
    
          // 3. Sonuçla bir şey yap
          // YAPILACAKLAR
    
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
    
        // 1. LLM yanıtını incele, her seçim için araç çağrıları olup olmadığını kontrol et
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

1. LLM çağırmak için gereken bazı importları ekleyelim

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Sonra, LLM'yi çağıracak fonksiyonu ekleyelim:

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

    Yukarıdaki kodda:

    - MCP sunucusunda bulunan ve dönüştürülmüş fonksiyonları LLM'ye geçtik.
    - Ardından LLM'yi bu fonksiyonlarla çağırdık.
    - Sonucu kontrol edip hangi fonksiyonları çağırmamız gerektiğine baktık.
    - Son olarak çağrılacak fonksiyon dizisini ilettik.

1. Son adım olarak, ana kodumuzu güncelleyelim:

    ```python
    prompt = "Add 2 to 20"

    # Tüm araçları, varsa, LLM'ye sor
    functions_to_call = call_llm(prompt, functions)

    # Önerilen fonksiyonları çağır
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    İşte son adımdı, yukarıdaki kodda:

    - Promptumuza göre LLM’nin çağırması gerektiğini düşündüğü bir fonksiyon ile MCP aracını `call_tool` ile çağırıyoruz.
    - Araç çağrısının sonucunu MCP Sunucusuna yazdırıyoruz.

#### .NET

1. LLM istemi isteği yapmak için örnek kod gösterelim:

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

Yukarıdaki kodda:

- MCP sunucusundan araçları aldık, `var tools = await GetMcpTools()`.
- Bir kullanıcı istemi `userMessage` tanımladık.
- Model ve araçları belirten bir seçenekler nesnesi oluşturduk.
- LLM'ye bir istek yaptık.

1. Son adım, LLM’nin bir fonksiyon çağırması gerektiğini düşünmesi durumunu görelim:

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

Yukarıdaki kodda:

- Fonksiyon çağrıları arasında döngü yaptık.
- Her araç çağrısı için adı ve argümanları ayırdık, MCP istemcisi kullanarak aracını çağırdık. Son olarak sonucu yazdırdık.

Tam kod şöyle:

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
    // MCP araçlarını otomatik olarak kullanan doğal dil isteklerini yürütün
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

Yukarıdaki kodda:

- MCP sunucu araçları ile basit doğal dil istemlerini kullandık.
- LangChain4j çerçevesi otomatik olarak şunları yapar:
  - Gerekli durumlarda kullanıcı istemlerini araç çağrılarına dönüştürür.
  - LLM'nin kararına göre uygun MCP araçlarını çağırır.
  - LLM ve MCP sunucusu arasındaki konuşma akışını yönetir.
- `bot.chat()` metodu, MCP araç yürütme sonuçlarını da içerebilen doğal dil yanıtları döner.
- Bu yaklaşım, kullanıcıların altta yatan MCP uygulamasını bilmesine gerek kalmadan sorunsuz bir kullanıcı deneyimi sağlar.

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

İşte işin çoğu burada gerçekleşiyor. LLM'yi ilk kullanıcı istemi ile çağıracağız, ardından yanıtı işleyeceğiz ve herhangi bir araç çağrısı gerekip gerekmediğine bakacağız. Gerekirse, o araçları çağıracağız ve daha fazla araç çağrısı gerekmeyene kadar ve nihai bir yanıt alınana kadar LLM ile sohbeti sürdüreceğiz.

Birden fazla LLM çağrısı yapacağız, bu yüzden LLM çağrısını yapacak bir fonksiyon tanımlayalım. `main.rs` dosyanıza şu fonksiyonu ekleyin:

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

Bu fonksiyon LLM istemcisini, mesaj listesini (kullanıcı istemi dahil), MCP sunucusundan araçları alır ve LLM’ye bir istek gönderir, yanıtı döner.
LLM'den dönen yanıt `choices` adlı bir dizi içerecektir. Sonuçta herhangi bir `tool_calls` (araç çağrısı) olup olmadığını kontrol etmemiz gerekecek. Bu, LLM'nin belirli bir aracın argümanlarla çağrılmasını istediğini anlamamızı sağlar. `main.rs` dosyanızın sonuna LLM yanıtını işlemek için bir fonksiyon tanımlamak üzere aşağıdaki kodu ekleyin:

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

    // İçerik mevcutsa yazdır
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Araç çağrılarını yönet
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Asistan mesajı ekle

        // Her araç çağrısını çalıştır
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

        // Araç sonuçlarıyla sohbeti sürdür
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

Eğer `tool_calls` mevcutsa, araç bilgilerini çıkarır, MCP sunucusunu araç isteği ile çağırır ve sonuçları konuşma mesajlarına ekler. Ardından LLM ile sohbet devam eder ve mesajlar asistanın yanıtı ile araç çağrısı sonuçlarıyla güncellenir.

LLM'nin MCP çağrıları için döndürdüğü araç çağrısı bilgilerini çıkarmak için, çağrıyı yapmak için gereken her şeyi çıkartan başka bir yardımcı fonksiyon ekleyeceğiz. `main.rs` dosyanızın sonuna aşağıdaki kodu ekleyin:

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

Tüm parçalar yerine oturduğuna göre, artık ilk kullanıcı istemini işleyip LLM'yi çağırabiliriz. `main` fonksiyonunuzu aşağıdaki kodu içerecek şekilde güncelleyin:

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

Bu, iki sayının toplamını istemek için ilk kullanıcı istemiyle LLM'yi sorgulayacak ve yanıtı işleyerek araç çağrılarını dinamik olarak yönetecektir.

Harika, başardınız!

## Ödev

Egzersizdeki kodu alın ve sunucunuzu birkaç araç daha ekleyerek geliştirin. Ardından egzersizdeki gibi bir LLM içeren bir istemci oluşturun ve farklı istemler ile test edin; böylece tüm sunucu araçlarınızın dinamik olarak çağrıldığından emin olun. Bu istemci oluşturma şekli, son kullanıcının tam istemci komutları yerine istemleri kullanabilmesini sağlayarak harika bir kullanıcı deneyimi sunar ve herhangi bir MCP sunucusunun çağrıldığından habersiz olmalarını sağlar.

## Çözüm

[Çözüm](/03-GettingStarted/03-llm-client/solution/README.md)

## Temel Çıkarımlar

- İstemcinize LLM eklemek, kullanıcıların MCP Sunucularıyla etkileşimini iyileştirir.
- MCP Sunucu yanıtını, LLM'nin anlayabileceği bir hale dönüştürmeniz gerekir.

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python)
- [Rust Hesap Makinesi](../../../../03-GettingStarted/samples/rust)

## Ek Kaynaklar

## Sonraki Adım

- Sonraki: [Visual Studio Code kullanarak bir sunucuyu tüketme](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki versiyonu yetkili kaynak olarak kabul edilmelidir. Kritik bilgilerin çevirisi için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımıyla ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->