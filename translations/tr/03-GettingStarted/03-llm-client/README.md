# LLM ile bir istemci oluşturma

> [!NOTE]
> Java istemci örnekleri, eski HTTP+SSE taşımacılığı üzerinden bağlanır ve
> MCP `2025-11-25` SDK API'lerine hedeflenir. Yeni uzak istemciler için `2026-07-28` uyumlu SDK ve Streamable HTTP kullanın.




## Genel Bakış

Bu derste, istemcinize bir LLM eklemeye odaklanıyoruz ve bunun kullanıcı deneyimini nasıl çok daha iyi hale getirdiğini göstereceğiz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabilirsiniz:

- Bir LLM ile istemci oluşturmak.
- LLM kullanarak MCP sunucusuyla sorunsuz etkileşimde bulunmak.
- İstemci tarafında daha iyi son kullanıcı deneyimi sağlamak.

## Yaklaşım

Almamız gereken yaklaşımı anlamaya çalışalım. Bir LLM eklemek basit görünüyor, ama gerçekten bunu yapacak mıyız?

İşte istemcinin sunucu ile nasıl etkileşeceği:

1. Sunucu ile bağlantı kur.

1. Yetenekleri, istemleri, kaynakları ve araçları listele ve şemalarını kaydet.

1. Bir LLM ekle ve kaydedilen yetenekleri ve şemalarını LLM'nin anlayacağı biçimde geç.

1. Kullanıcı isteğini, istemci tarafından listelenen araçlarla birlikte LLM'ye ilet.

Harika, şimdi bunu yüksek seviyede nasıl yapabileceğimizi anladık, aşağıdaki egzersizde bunu deneyelim.

## Alıştırma: LLM ile bir istemci oluşturma

Bu alıştırmada istemcimize bir LLM eklemeyi öğreneceğiz.

### GitHub Kişisel Erişim Belgesi ile Kimlik Doğrulama

GitHub token oluşturmak basit bir işlemdir. İşte nasıl yapabileceğiniz:

- GitHub Ayarlarına git – Sağ üst köşedeki profil resminize tıklayın ve Ayarlar'ı seçin.
- Geliştirici Ayarlarına geç – Aşağı kaydırın ve Geliştirici Ayarları'na tıklayın.
- Kişisel Erişim Belirtecini seçin – Hassasiyetli tokenlere tıklayın ve ardından Yeni token oluşturun.
- Tokeninizi yapılandırın – Referans için bir not ekleyin, sona erme tarihi belirleyin ve gerekli kapsamları (izinleri) seçin. Bu durumda Modeller iznini eklediğinizden emin olun.
- Token oluştur ve kopyala – Token oluştur'a tıklayın ve hemen kopyalayın, çünkü bir daha göremeyeceksiniz.

### -1- Sunucuya Bağlan

Önce istemcimizi oluşturalım:

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

Önceki kodda şunları yaptık:

- Gerekli kütüphaneleri içe aktardık
- `client` ve `openai` adlı iki üyeye sahip bir sınıf oluşturduk; bunlar sırasıyla istemciyi yönetmeye ve LLM ile etkileşime yardımcı olacak.
- LLM örneğimizi, `baseUrl`'i çıkarım API'sine yönlendirerek GitHub Modellerini kullanacak şekilde yapılandırdık.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio bağlantısı için sunucu parametreleri oluşturun
server_params = StdioServerParameters(
    command="mcp",  # Çalıştırılabilir
    args=["run", "server.py"],  # İsteğe bağlı komut satırı argümanları
    env=None,  # İsteğe bağlı ortam değişkenleri
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Bağlantıyı başlatın
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Önceki kodda şunları yaptık:

- MCP için gereken kütüphaneleri içe aktardık
- Bir istemci oluşturduk

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

Öncelikle, `pom.xml` dosyanıza LangChain4j bağımlılıklarını eklemeniz gerekiyor. MCP entegrasyonu ve OpenAI uyumlu MiniMax API için bu bağımlılıkları ekleyin:

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
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

MiniMax API anahtarınızı ve isteğe bağlı olarak uç noktayı ve modeli ayarlayın.
`MINIMAX_MODEL_ID` `MiniMax-M3` ve `MiniMax-M2.7` destekler. Eğer
`OPENAI_BASE_URL` ayarlanmazsa, `MINIMAX_REGION` `global_en` ve `cn_zh`'yi destekler.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Bölgeye göre uç nokta seçmek için `OPENAI_BASE_URL`'i atlayın:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Ardından Java istemci sınıfınızı oluşturun:

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

Önceki kodda şunları yaptık:

- **LangChain4j bağımlılıklarını ekledik**: MCP entegrasyonu ve OpenAI uyumlu MiniMax API için gerekli
- **LangChain4j kütüphanelerini içe aktardık**: MCP entegrasyonu ve OpenAI sohbet modeli işlevselliği için
- **Bir `ChatLanguageModel` oluşturduk**: MiniMax'ı MiniMax API anahtarınız, uç nokta ve desteklenen model kimliği ile kullanacak şekilde yapılandırdık
- **HTTP taşıma yapılandırıldı**: MCP sunucusuna bağlanmak için Server-Sent Events (SSE) kullanıyoruz
- **Bir MCP istemcisi oluşturduk**: Sunucu ile iletişimi yönetecek
- **LangChain4j'nin yerleşik MCP desteğini kullandık**: LLM'ler ile MCP sunucuları arasındaki entegrasyonu kolaylaştırıyor

#### Rust

Bu örnek, Rust tabanlı bir MCP sunucusunun çalıştığı varsayımıyla yapılmıştır. Henüz bir MCP sunucunuz yoksa, sunucuyu oluşturmak için [01-first-server](../01-first-server/README.md) dersine geri dönün.

Rust MCP sunucunuz hazır olduktan sonra bir terminal açın ve sunucunun bulunduğu dizine gidin. Ardından yeni bir LLM istemci projesi oluşturmak için şu komutu çalıştırın:

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
> Resmi bir Rust OpenAI kütüphanesi yok, ancak `async-openai` crate'i yaygın olarak kullanılan bir [topluluk destekli kütüphanedir](https://platform.openai.com/docs/libraries/rust#rust).

`src/main.rs` dosyasını açın ve içeriğini aşağıdaki kod ile değiştirin:

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

    // OpenAI istemcisi kur
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP istemcisi kur
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
> Uygulamayı çalıştırmadan önce `OPENAI_API_KEY` ortam değişkenini GitHub tokenınızla ayarlamayı unutmayın.

Harika, sonraki adımda sunucunun yeteneklerini listeleyelim.

### -2- Sunucu yeteneklerini listele

Şimdi sunucuya bağlanacağız ve yeteneklerini soracağız:

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

Önceki kodda şunları yaptık:

- Sunucuya bağlanmak için `connectToServer` kodu ekledik.
- Uygulama akışımızı yöneten `run` metodunu oluşturduk. Şimdiye kadar sadece araçları listeliyor ama yakında daha fazlasını ekleyeceğiz.

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

Eklediğimiz şeyler:

- Kaynakları ve araçları listeledik ve yazdırdık. Araçlar için ayrıca `inputSchema`'yı listeledik ki bunu sonra kullanacağız.

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

- MCP Sunucuda mevcut araçları listeledik
- Her araç için adını, açıklamasını ve şemasını listeledik. Bunlar kısa süre içinde araçları çağırmak için kullanacağımız şeyler.

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

Önceki kodda:

- MCP sunucusundaki tüm araçları otomatik keşfeden ve kaydeden bir `McpToolProvider` oluşturduk
- Araç sağlayıcı, MCP araç şemalarını LangChain4j araç formatına dahili olarak dönüştürüyor
- Bu yöntem manuel araç listeleme ve dönüştürmeyi soyutlar

#### Rust

MCP sunucusundan araçları almak için `list_tools` metodunu kullanıyoruz. `main` fonksiyonunuzda MCP istemcisini kurduktan sonra aşağıdaki kodu ekleyin:

```rust
// MCP araç listesini al
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Sunucu yeteneklerini LLM araçlarına dönüştür

Sunucu yeteneklerini listeledikten sonra bir sonraki adım, bunları LLM'nin anlayacağı formata dönüştürmek. Böylece bu yetenekleri LLM'imize araç olarak sunabiliriz.

#### TypeScript

1. MCP Sunucusundan gelen yanıtı LLM'nin kullanabileceği araç formatına dönüştürmek için aşağıdaki kodu ekleyin:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Girdi şemasına dayalı bir zod şeması oluşturun
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Türü açıkça "fonksiyon" olarak ayarlayın
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

    Yukarıdaki kod, MCP Sunucusundan gelen yanıtı LLM'nin anlayabileceği bir araç tanımı formatına dönüştürür.

2. Şimdi `run` metodunu güncelleyelim ve sunucu yeteneklerini listeleyelim:

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

    Önceki kodda, `run` metodunu sonuç üzerinde gezinmek ve her giriş için `openAiToolAdapter` çağırmak üzere güncelledik.

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

    `convert_to_llm_tools` fonksiyonunda MCP araç yanıtını LLM'nin anlayacağı biçime dönüştürüyoruz.

2. Sonra istemci kodumuzu bu fonksiyonu kullanacak şekilde güncelleyelim:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Burada, MCP araç yanıtını LLM'ye besleyebileceğimiz bir biçime dönüştürmek için `convert_to_llm_tool` çağrısı ekledik.

#### .NET

1. MCP araç yanıtını LLM'nin anlayabileceği bir biçime dönüştürmek için kod ekleyelim

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

Önceki kodda şunları yaptık:

- `ConvertFrom` fonksiyonunu oluşturduk; ad, açıklama ve giriş şemasını alıyor.
- Bir `FunctionDefinition` oluşturuyor; bu da `ChatCompletionsDefinition`'a geçiliyor. Bu, LLM'nin anlayabileceği bir şey.

2. Şimdi bu fonksiyonu kullanacak şekilde bazı mevcut kodları nasıl güncelleyeceğimize bakalım:

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

Önceki kodda şunları yaptık:

- Doğal dil etkileşimleri için basit bir `Bot` arayüzü tanımladık
- LangChain4j'nin `AiServices` kullanılarak LLM ile MCP araç sağlayıcı otomatik bağlandı
- Çerçeve, araç şeması dönüştürme ve fonksiyon çağrısını arka planda otomatik yönetiyor
- Bu yaklaşım manuel araç dönüştürmeyi ortadan kaldırıyor; LangChain4j MCP araçlarını LLM uyumlu formata dönüştürmenin tüm karmaşıklığını hallediyor

#### Rust

MCP araç yanıtını LLM'nin anlayabileceği bir biçime dönüştürmek için araç listesini formatlayan yardımcı bir fonksiyon ekleyeceğiz. `main` fonksiyonunun altına aşağıdaki kodu `main.rs` dosyanıza ekleyin. Bu, LLM'ye istek yapıldığında çağrılacak:

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

Harika, şimdi kullanıcı isteklerini işlemek için hazırız, bunu ele alalım.

### -4- Kullanıcı istemi isteğini işle

Bu kod bölümünde kullanıcı isteklerini işleyeceğiz.

#### TypeScript

1. LLM'yi çağırmak için kullanılacak bir metot ekleyin:

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

        // 3. Sonuçla bir şeyler yap
        // YAPILACAKLAR

        }
    }
    ```

    Önceki kodda:

    - `callTools` metodunu ekledik.
    - Metot, bir LLM yanıtı alır ve hangi araçların çağrıldığını kontrol eder, varsa:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // aracı çağır
        }
        ```

    - LLM çağrılması gerektiğini belirtirse aracı çağırır:

        ```typescript
        // 2. Sunucunun aracını çağır
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Sonuçla bir şey yap
        // YAPILACAK
        ```

2. `run` metodunu LLM çağrılarını ve `callTools` çağrısını içerecek şekilde güncelleyin:

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
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM yanıtını inceleyin, her seçenek için araç çağrıları olup olmadığını kontrol edin
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Harika, tüm kodu listeleyelim:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Şema doğrulaması için zod'u içe aktar

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // gelecekte bu url'ye değiştirilmesi gerekebilir: https://models.github.ai/inference
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
          // input_schema temel alınarak bir zod şeması oluştur
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
    
        // 3. LLM yanıtını incele, her seçenek için araç çağrıları olup olmadığını kontrol et
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

1. LLM'yi çağırmak için gereken bazı içe aktarımları yapalım

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Ardından, LLM'yi çağıracak fonksiyonu ekleyelim:

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
    - Sonra LLM'yi bu fonksiyonlarla çağırdık.
    - Sonrasında, çağrılması gereken fonksiyonları görmek için sonucu inceledik.
    - Son olarak, çağrılacak fonksiyonların bir dizisini geçtik.

3. Son adım olarak ana kodu güncelleyelim:

    ```python
    prompt = "Add 2 to 20"

    # LLM'ye tüm araçları sor, varsa
    functions_to_call = call_llm(prompt, functions)

    # önerilen fonksiyonları çağır
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    İşte, son adımdı, yukarıdaki kodda:

    - İstem üzerine LLM'nin çağırmamız gerektiğini düşündüğü bir MCP aracını `call_tool` ile çağırıyoruz.
    - Araç çağrısının MCP Sunucusu'ndan aldığı sonucu yazdırıyoruz.

#### .NET

1. LLM istemci isteği yapmak için bazı kod örnekleri gösterelim:

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

    - MCP sunucusundan araçları aldık: `var tools = await GetMcpTools()`.
    - Bir kullanıcı istemi `userMessage` tanımladık.
    - Model ve araçları belirten bir seçenek nesnesi oluşturduk.
    - LLM'ye istek yaptık.

2. Son bir adım, LLM'nin fonksiyon çağrısı yapmamızı isteyip istemediğini görelim:

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

    - Bir fonksiyon çağrısı listesi üzerinde döngü yaptık.
    - Her araç çağrısı için adı ve argümanları ayrıştırdık ve MCP istemcisi ile MCP sunucuda aracı çağırdık. Sonuçları yazdırdık.

İşte tüm kod:

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

// 6. Print the generic response
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

Önceki kodda şunları yaptık:

- MCP sunucu araçları ile doğal dil istemlerini kullandık
- LangChain4j çerçevesi otomatik olarak:
  - Kullanıcı istemlerini gerekirse araç çağrılarına dönüştürür
  - LLM kararına göre uygun MCP araçlarını çağırır
  - LLM ile MCP sunucu arasındaki konuşma akışını yönetir
- `bot.chat()` yöntemi MCP araç yürütme sonuçları da dahil olmak üzere doğal dil yanıtları döndürür
- Bu yaklaşım kullanıcıların MCP altyapısını bilmesine gerek kalmadan sorunsuz bir deneyim sağlar

Tam kod örneği:

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

#### Rust


İşin çoğunun yapıldığı yer burasıdır. LLM'yi ilk kullanıcı istemi ile çağıracağız, ardından yanıtı işleyerek herhangi bir aracın çağrılıp çağrılmayacağını göreceğiz. Eğer gerekiyorsa, o araçları çağıracağız ve daha fazla araç çağrısı gerekene kadar LLM ile sohbeti sürdüreceğiz ve nihai bir yanıt alacağız.

LLM'ye birden fazla kez çağrı yapacağımız için, LLM çağrısını yönetecek bir fonksiyon tanımlayalım. `main.rs` dosyanıza aşağıdaki fonksiyonu ekleyin:

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

Bu fonksiyon, LLM istemcisini, bir mesaj listesi (kullanıcı istemi dahil), MCP sunucusundan araçları alır ve LLM'ye bir istek gönderir; yanıtı döndürür.

LLM'den gelen yanıt, bir `choices` dizisi içerecektir. Sonucu işleyerek herhangi bir `tool_calls` (araç çağrısı) olup olmadığını kontrol etmemiz gerekecek. Bu, LLM'nin belirli bir aracın çağrılmasını argümanlarla istediğini gösterir. LLM yanıtını işlemek için aşağıdaki kodu `main.rs` dosyanızın sonuna ekleyin:

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

Eğer `tool_calls` varsa, araç bilgilerini çıkarır, MCP sunucusunu araç isteği ile çağırır ve sonuçları sohbet mesajlarına ekler. Sonra LLM ile sohbeti devam ettirir ve mesajlar asistanın yanıtı ve araç çağrısı sonuçları ile güncellenir.

LLM'nin MCP çağrıları için döndürdüğü araç çağrısı bilgilerini çıkarmak için, çağrıyı yapmak için gereken her şeyi çıkaran bir başka yardımcı fonksiyon ekleyeceğiz. Aşağıdaki kodu `main.rs` dosyanızın sonuna ekleyin:

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

Tüm parçalar yerli yerinde, artık ilk kullanıcı istemini işleyebilir ve LLM'yi çağırabiliriz. `main` fonksiyonunuzu aşağıdaki kodla güncelleyin:

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

Bu, iki sayının toplamını sorgulayan ilk kullanıcı istemiyle LLM'ye sorgu yapacak ve yanıtı işleyerek dinamik olarak araç çağrılarını yönetecektir.

Harika, başardınız!

## Ödev

Egzersizden aldığınız kodu kullanarak sunucuyu daha fazla araçla geliştirin. Sonra, egzersizde olduğu gibi bir LLM ile bir istemci oluşturun ve farklı istemlerle test ederek tüm sunucu araçlarınızın dinamik olarak çağrıldığından emin olun. Bu şekilde bir istemci oluşturmak, son kullanıcıların tam istemci komutları yerine istemleri kullanarak harika bir kullanıcı deneyimi yaşamalarını sağlar ve herhangi bir MCP sunucusunun çağrıldığından habersiz olmalarını sağlar.

## Çözüm

[Çözüm](./solution/README.md)

## Temel Noktalar

- İstemcinize bir LLM eklemek, kullanıcıların MCP Sunucularıyla daha iyi etkileşime geçmesini sağlar.
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

- Sonraki: [Visual Studio Code Kullanarak Bir Sunucu Tüketmek](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->