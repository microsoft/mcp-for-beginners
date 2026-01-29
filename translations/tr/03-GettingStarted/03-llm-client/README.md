# LLM ile bir istemci oluşturma

Şimdiye kadar bir sunucu ve istemci oluşturmayı gördünüz. İstemci, araçlarını, kaynaklarını ve istemlerini listelemek için sunucuyu açıkça çağırabiliyordu. Ancak bu çok pratik bir yaklaşım değil. Kullanıcınız ajanlık çağında yaşıyor ve bunu yapmak için istemleri kullanmayı ve bir LLM ile iletişim kurmayı bekliyor. Kullanıcınız için yeteneklerinizi depolamak için MCP kullanıp kullanmadığınız önemli değil, ancak doğal dili kullanarak etkileşimde bulunmayı bekliyorlar. Peki bunu nasıl çözeriz? Çözüm, istemciye bir LLM eklemekle ilgilidir.

## Genel Bakış

Bu derste, istemcinize bir LLM eklemeye odaklanacağız ve bunun kullanıcı deneyimini nasıl çok daha iyi hale getirdiğini göstereceğiz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Bir LLM ile istemci oluşturmak.
- Bir LLM kullanarak MCP sunucusuyla sorunsuz etkileşimde bulunmak.
- İstemci tarafında daha iyi bir son kullanıcı deneyimi sağlamak.

## Yaklaşım

Almamız gereken yaklaşımı anlamaya çalışalım. Bir LLM eklemek basit görünüyor, ama gerçekten bunu yapacak mıyız?

İstemcinin sunucuyla nasıl etkileşimde bulunacağı şöyle olacak:

1. Sunucu ile bağlantı kurmak.

1. Yetenekleri, istemleri, kaynakları ve araçları listelemek ve bunların şemasını kaydetmek.

1. Bir LLM eklemek ve kaydedilen yetenekleri ve şemalarını LLM'nin anlayacağı bir formatta geçirmek.

1. Kullanıcı istemini, istemcinin listelediği araçlarla birlikte LLM'ye ileterek işlemek.

Harika, şimdi bunu yüksek seviyede nasıl yapabileceğimizi anladık, aşağıdaki alıştırmada bunu deneyelim.

## Alıştırma: LLM ile bir istemci oluşturma

Bu alıştırmada, istemcimize bir LLM eklemeyi öğreneceğiz.

### GitHub Kişisel Erişim Tokenı ile Kimlik Doğrulama

GitHub tokenı oluşturmak basit bir işlemdir. İşte nasıl yapacağınız:

- GitHub Ayarlarına gidin – Sağ üst köşedeki profil resminize tıklayın ve Ayarlar'ı seçin.
- Geliştirici Ayarlarına gidin – Aşağı kaydırın ve Geliştirici Ayarları'na tıklayın.
- Kişisel Erişim Tokenlarını seçin – İnce ayarlı tokenlara tıklayın ve ardından Yeni token oluşturun.
- Tokenınızı yapılandırın – Referans için bir not ekleyin, bir son kullanma tarihi belirleyin ve gerekli kapsamları (izinleri) seçin. Bu durumda Models iznini eklediğinizden emin olun.
- Tokenı oluşturun ve kopyalayın – Token oluştur'a tıklayın ve hemen kopyalayın, çünkü tekrar göremeyeceksiniz.

### -1- Sunucuya bağlanma

Öncelikle istemcimizi oluşturalım:

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

Yukarıdaki kodda:

- Gerekli kütüphaneleri içe aktardık
- `client` ve `openai` olmak üzere iki üyeye sahip bir sınıf oluşturduk; bunlar sırasıyla istemciyi yönetmemize ve bir LLM ile etkileşim kurmamıza yardımcı olacak.
- LLM örneğimizi, `baseUrl`'yi çıkarım API'sine işaret edecek şekilde ayarlayarak GitHub Modellerini kullanacak şekilde yapılandırdık.

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

- MCP için gerekli kütüphaneleri içe aktardık
- Bir istemci oluşturduk

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

Öncelikle, `pom.xml` dosyanıza LangChain4j bağımlılıklarını eklemeniz gerekir. MCP entegrasyonu ve GitHub Modelleri desteği için bu bağımlılıkları ekleyin:

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

        // Sunucuya bağlanmak için MCP taşıma oluştur
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

Yukarıdaki kodda:

- **LangChain4j bağımlılıklarını ekledik**: MCP entegrasyonu, OpenAI resmi istemcisi ve GitHub Modelleri desteği için gerekli
- **LangChain4j kütüphanelerini içe aktardık**: MCP entegrasyonu ve OpenAI sohbet modeli işlevselliği için
- **GitHub tokenınızla GitHub Modellerini kullanacak şekilde yapılandırılmış bir `ChatLanguageModel` oluşturduk**
- **MCP sunucusuna bağlanmak için Server-Sent Events (SSE) kullanan HTTP taşıma ayarladık**
- **Sunucu ile iletişimi yönetecek bir MCP istemcisi oluşturduk**
- **LangChain4j'nin yerleşik MCP desteğini kullandık**: Bu, LLM'ler ile MCP sunucuları arasındaki entegrasyonu basitleştirir

#### Rust

Bu örnek, Rust tabanlı bir MCP sunucusunun çalıştığını varsayar. Eğer yoksa, sunucuyu oluşturmak için [01-first-server](../01-first-server/README.md) dersine geri dönün.

Rust MCP sunucunuz hazırsa, bir terminal açın ve sunucunun bulunduğu dizine gidin. Ardından yeni bir LLM istemci projesi oluşturmak için aşağıdaki komutu çalıştırın:

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
> Resmi bir Rust OpenAI kütüphanesi yoktur, ancak `async-openai` crate'i yaygın olarak kullanılan bir [topluluk tarafından sürdürülen kütüphanedir](https://platform.openai.com/docs/libraries/rust#rust).

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

    // YAPILACAK: MCP araç listesini al

    // YAPILACAK: Araç çağrıları ile LLM sohbeti

    Ok(())
}
```

Bu kod, MCP sunucusuna ve LLM etkileşimleri için GitHub Modellerine bağlanacak temel bir Rust uygulaması kurar.

> [!IMPORTANT]
> Uygulamayı çalıştırmadan önce `OPENAI_API_KEY` ortam değişkenini GitHub tokenınızla ayarladığınızdan emin olun.

Harika, bir sonraki adımımız olarak sunucudaki yetenekleri listeleyelim.

### -2- Sunucu yeteneklerini listeleme

Şimdi sunucuya bağlanacağız ve yeteneklerini isteyeceğiz:

#### Typescript

Aynı sınıfa aşağıdaki yöntemleri ekleyin:

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

Yukarıdaki kodda:

- Sunucuya bağlanmak için `connectToServer` kodu ekledik.
- Uygulama akışımızı yöneten `run` metodunu oluşturduk. Şu ana kadar sadece araçları listeliyor, ancak yakında daha fazlasını ekleyeceğiz.

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

- Kaynakları ve araçları listeledik ve yazdırdık. Araçlar için ayrıca daha sonra kullanacağımız `inputSchema`'yı da listeledik.

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

- MCP Sunucusunda mevcut araçları listeledik
- Her araç için ad, açıklama ve şemasını listeledik. Şema, araçları çağırmak için kullanacağımız bir şey.

#### Java

```java
// MCP araçlarını otomatik olarak keşfeden bir araç sağlayıcı oluşturun
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP araç sağlayıcı otomatik olarak şunları yönetir:
// - MCP sunucusundan mevcut araçları listeleme
// - MCP araç şemalarını LangChain4j formatına dönüştürme
// - Araç yürütme ve yanıtlarını yönetme
```

Yukarıdaki kodda:

- MCP sunucusundaki tüm araçları otomatik olarak keşfeden ve kaydeden bir `McpToolProvider` oluşturduk
- Araç sağlayıcı, MCP araç şemaları ile LangChain4j'nin araç formatı arasındaki dönüşümü dahili olarak yönetir
- Bu yaklaşım, manuel araç listeleme ve dönüştürme sürecini soyutlar

#### Rust

MCP sunucusundan araçları almak için `list_tools` yöntemi kullanılır. `main` fonksiyonunuzda, MCP istemcisini kurduktan sonra aşağıdaki kodu ekleyin:

```rust
// MCP araç listesini al
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Sunucu yeteneklerini LLM araçlarına dönüştürme

Sunucu yeteneklerini listeledikten sonraki adım, bunları LLM'nin anlayacağı bir formata dönüştürmektir. Bunu yaptıktan sonra, bu yetenekleri LLM'imize araç olarak sağlayabiliriz.

#### TypeScript

1. MCP Sunucusundan gelen yanıtı LLM'nin kullanabileceği araç formatına dönüştürmek için aşağıdaki kodu ekleyin:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema temel alınarak bir zod şeması oluşturun
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

    Yukarıdaki kod, MCP Sunucusundan gelen yanıtı alır ve LLM'nin anlayabileceği bir araç tanımı formatına dönüştürür.

1. Sonra `run` metodunu sunucu yeteneklerini listeleyecek şekilde güncelleyelim:

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

    Yukarıdaki kodda, `run` metodunu sonucu haritalandıracak ve her giriş için `openAiToolAdapter` çağrısı yapacak şekilde güncelledik.

#### Python

1. Öncelikle aşağıdaki dönüştürücü fonksiyonu oluşturalım

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

    Yukarıdaki `convert_to_llm_tools` fonksiyonunda, MCP araç yanıtını alıp LLM'nin anlayabileceği bir formata dönüştürüyoruz.

1. Sonra istemci kodumuzu bu fonksiyonu kullanacak şekilde güncelleyelim:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Burada, MCP araç yanıtını LLM'ye besleyebileceğimiz bir şeye dönüştürmek için `convert_to_llm_tool` çağrısı ekliyoruz.

#### .NET

1. MCP araç yanıtını LLM'nin anlayabileceği bir şeye dönüştürmek için kod ekleyelim

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

- Ad, açıklama ve giriş şemasını alan `ConvertFrom` fonksiyonu oluşturduk.
- Bu fonksiyon, LLM'nin anlayabileceği bir `ChatCompletionsDefinition`'a geçirilen bir `FunctionDefinition` oluşturuyor.

1. Yukarıdaki fonksiyonu kullanmak için mevcut kodu nasıl güncelleyebileceğimize bakalım:

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

// AI hizmetini LLM ve MCP araçlarıyla yapılandırın
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Yukarıdaki kodda:

- Doğal dil etkileşimleri için basit bir `Bot` arayüzü tanımladık
- LangChain4j'nin `AiServices`'ini kullanarak LLM'yi MCP araç sağlayıcısıyla otomatik olarak bağladık
- Çerçeve, araç şeması dönüşümünü ve fonksiyon çağrısını otomatik olarak arka planda yönetir
- Bu yaklaşım manuel araç dönüşümünü ortadan kaldırır - LangChain4j MCP araçlarını LLM uyumlu formata dönüştürmenin tüm karmaşıklığını halleder

#### Rust

MCP araç yanıtını LLM'nin anlayabileceği bir formata dönüştürmek için, araç listesini biçimlendiren yardımcı bir fonksiyon ekleyeceğiz. `main` fonksiyonunun altına `main.rs` dosyanıza aşağıdaki kodu ekleyin. Bu, LLM'ye istek yaparken çağrılacak:

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

Harika, şimdi kullanıcı isteklerini işlemek için hazırız, bunu da ele alalım.

### -4- Kullanıcı istemi isteğini işleme

Bu kod bölümünde, kullanıcı isteklerini işleyeceğiz.

#### TypeScript

1. LLM'mizi çağırmak için kullanılacak bir yöntem ekleyin:

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

    - `callTools` adlı bir yöntem ekledik.
    - Yöntem, bir LLM yanıtı alır ve hangi araçların çağrıldığını kontrol eder, varsa:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // aracı çağır
        }
        ```

    - LLM çağrılması gerektiğini belirtirse bir aracı çağırır:

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

1. `run` metodunu LLM çağrılarını ve `callTools` çağrısını içerecek şekilde güncelleyin:

    ```typescript

    // 1. LLM için girdi olan mesajları oluşturun
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
        model: "gpt-4o-mini",
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

Harika, kodu tam olarak listeleyelim:

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
            baseURL: "https://models.inference.ai.azure.com", // Gelecekte bu URL'ye değiştirilmesi gerekebilir: https://models.github.ai/inference
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM yanıtını incele, her seçim için araç çağrısı olup olmadığını kontrol et
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

1. LLM çağrısı yapmak için gereken bazı içe aktarımları ekleyelim

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Sonra LLM'yi çağıracak fonksiyonu ekleyelim:

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

    - MCP sunucusunda bulduğumuz ve dönüştürdüğümüz fonksiyonları LLM'ye geçtik.
    - Ardından LLM'yi bu fonksiyonlarla çağırdık.
    - Sonucu inceleyip hangi fonksiyonların çağrılması gerektiğine baktık.
    - Son olarak çağrılacak fonksiyonların bir dizisini geçtik.

1. Son adım olarak ana kodumuzu güncelleyelim:

    ```python
    prompt = "Add 2 to 20"

    # LLM'ye hangi araçların kullanılacağını sor, eğer varsa
    functions_to_call = call_llm(prompt, functions)

    # önerilen fonksiyonları çağır
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Yukarıdaki kodda:

    - LLM'nin istemimize dayanarak çağırmamız gerektiğini düşündüğü bir fonksiyon kullanarak MCP aracını `call_tool` ile çağırıyoruz.
    - Araç çağrısının sonucunu MCP Sunucusuna yazdırıyoruz.

#### .NET

1. LLM istemi isteği yapmak için bazı kodlar gösterelim:

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

    Yukarıdaki kodda:

    - MCP sunucusundan araçları aldık, `var tools = await GetMcpTools()`.
    - Bir kullanıcı istemi tanımladık `userMessage`.
    - Model ve araçları belirten bir seçenekler nesnesi oluşturduk.
    - LLM'ye istek yaptık.

1. Son bir adım, LLM'nin bir fonksiyon çağırması gerektiğini düşünüp düşünmediğine bakalım:

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

    - Fonksiyon çağrıları listesini döngüye aldık.
    - Her araç çağrısı için adı ve argümanları ayrıştırdık ve MCP istemcisini kullanarak MCP sunucusundaki aracı çağırdık. Sonuçları yazdırdık.

Kodun tamamı:

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

- MCP sunucu araçlarıyla etkileşim için basit doğal dil istemleri kullandık
- LangChain4j çerçevesi otomatik olarak:
  - Kullanıcı istemlerini gerektiğinde araç çağrılarına dönüştürür
  - LLM'nin kararına göre uygun MCP araçlarını çağırır
  - LLM ile MCP sunucusu arasındaki konuşma akışını yönetir
- `bot.chat()` metodu, MCP araç yürütme sonuçlarını içerebilen doğal dil yanıtları döner
- Bu yaklaşım, kullanıcıların altta yatan MCP uygulamasını bilmesine gerek kalmadan sorunsuz bir kullanıcı deneyimi sağlar

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

İşin çoğunun yapıldığı yer burasıdır. İlk kullanıcı istemi ile LLM'yi çağıracağız, ardından yanıtı işleyip herhangi bir aracın çağrılması gerekip gerekmediğine bakacağız. Gerekirse, bu araçları çağıracağız ve daha fazla araç çağrısı gerekmediğinde ve nihai yanıtı aldığımızda LLM ile sohbeti sürdüreceğiz.

LLM'ye birden fazla çağrı yapacağız, bu yüzden LLM çağrısını yönetecek bir fonksiyon tanımlayalım. `main.rs` dosyanıza aşağıdaki fonksiyonu ekleyin:

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

Bu fonksiyon, LLM istemcisini, mesaj listesini (kullanıcı istemi dahil), MCP sunucusundan araçları alır ve LLM'ye istek gönderir, yanıtı döner.
LLM'den gelen yanıt, bir `choices` dizisi içerecektir. Sonuçta herhangi bir `tool_calls` olup olmadığını kontrol etmemiz gerekecek. Bu, LLM'nin belirli bir aracın argümanlarla çağrılmasını istediğini anlamamızı sağlar. LLM yanıtını işlemek için bir fonksiyon tanımlamak üzere `main.rs` dosyanızın en altına aşağıdaki kodu ekleyin:

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

    // Araç çağrılarını işle
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

        // Araç sonuçlarıyla konuşmaya devam et
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

Eğer `tool_calls` mevcutsa, araç bilgilerini çıkarır, MCP sunucusunu araç isteği ile çağırır ve sonuçları konuşma mesajlarına ekler. Ardından LLM ile konuşmaya devam eder ve mesajlar asistanın yanıtı ve araç çağrısı sonuçları ile güncellenir.

LLM'nin MCP çağrıları için döndürdüğü araç çağrısı bilgilerini çıkarmak için, çağrıyı yapmak için gereken her şeyi çıkaran başka bir yardımcı fonksiyon ekleyeceğiz. `main.rs` dosyanızın en altına aşağıdaki kodu ekleyin:

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

Tüm parçalar yerli yerine oturduğuna göre, artık ilk kullanıcı istemini işleyebilir ve LLM'yi çağırabiliriz. `main` fonksiyonunuzu aşağıdaki kodu içerecek şekilde güncelleyin:

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

Bu, iki sayının toplamını isteyen ilk kullanıcı istemi ile LLM'yi sorgulayacak ve yanıtı işleyerek araç çağrılarını dinamik olarak yönetecektir.

Harika, başardınız!

## Ödev

Egzersizden aldığınız kodu kullanarak sunucuyu daha fazla araçla genişletin. Ardından egzersizdeki gibi bir LLM ile bir istemci oluşturun ve farklı istemlerle test ederek tüm sunucu araçlarınızın dinamik olarak çağrıldığından emin olun. Bu şekilde bir istemci oluşturmak, son kullanıcının tam istemci komutları yerine istemleri kullanabilmesini sağlar ve herhangi bir MCP sunucusunun çağrıldığından habersiz harika bir kullanıcı deneyimi sunar.

## Çözüm

[Çözüm](/03-GettingStarted/03-llm-client/solution/README.md)

## Temel Çıkarımlar

- İstemcinize bir LLM eklemek, kullanıcıların MCP Sunucularıyla etkileşim kurmasının daha iyi bir yolunu sağlar.
- MCP Sunucu yanıtını LLM'nin anlayabileceği bir şeye dönüştürmeniz gerekir.

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python)
- [Rust Hesap Makinesi](../../../../03-GettingStarted/samples/rust)

## Ek Kaynaklar

## Sonraki Adım

- Sonraki: [Visual Studio Code kullanarak bir sunucuyu tüketmek](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->