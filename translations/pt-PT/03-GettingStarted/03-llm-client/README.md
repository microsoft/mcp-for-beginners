# Criar um cliente com LLM

Até agora, viste como criar um servidor e um cliente. O cliente tem sido capaz de chamar explicitamente o servidor para listar as suas ferramentas, recursos e prompts. No entanto, esta não é uma abordagem muito prática. Os teus utilizadores vivem na era agentiva e esperam usar prompts e comunicar com um LLM em vez disso. Eles não se preocupam se usas MCP para armazenar as tuas capacidades; simplesmente esperam interagir usando linguagem natural. Então, como é que resolvemos isto? A solução é adicionar um LLM ao cliente.

## Visão Geral

Nesta lição focamo-nos em adicionar um LLM ao teu cliente e mostramos como isso oferece uma experiência muito melhor para o teu utilizador.

## Objetivos de Aprendizagem

No final desta lição, serás capaz de:

- Criar um cliente com um LLM.
- Interagir de forma integrada com um servidor MCP usando um LLM.
- Proporcionar uma melhor experiência ao utilizador final no lado do cliente.

## Abordagem

Vamos tentar perceber a abordagem que precisamos tomar. Adicionar um LLM parece simples, mas será que vamos realmente fazer isto?

Eis como o cliente irá interagir com o servidor:

1. Estabelecer ligação com o servidor.

1. Listar capacidades, prompts, recursos e ferramentas e guardar o seu esquema.

1. Adicionar um LLM e passar as capacidades guardadas e o seu esquema num formato que o LLM compreenda.

1. Tratar um prompt do utilizador passando-o para o LLM juntamente com as ferramentas listadas pelo cliente.

Ótimo, agora que entendemos como podemos fazer isto a alto nível, vamos experimentar no exercício abaixo.

## Exercício: Criar um cliente com um LLM

Neste exercício, vamos aprender a adicionar um LLM ao nosso cliente.

### Autenticação usando Token de Acesso Pessoal do GitHub

Criar um token GitHub é um processo simples. Eis como podes fazê-lo:

- Vai a Definições do GitHub – Clica na tua fotografia de perfil no canto superior direito e seleciona Definições.
- Navega para Definições de Desenvolvedor – Desce e clica em Definições de Desenvolvedor.
- Seleciona Tokens de Acesso Pessoal – Clica em Tokens de granulação fina e depois em Gerar novo token.
- Configura o teu Token – Adiciona uma nota para referência, define uma data de expiração, e seleciona as permissões necessárias. Neste caso certifica-te de adicionar a permissão Models.
- Gera e Copia o Token – Clica em Gerar token e assegura-te de copiar imediatamente, pois não vais poder vê-lo novamente.

### -1- Ligar ao servidor

Vamos criar primeiro o nosso cliente:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importar zod para validação de esquemas

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

No código acima fizemos:

- Importámos as bibliotecas necessárias
- Criámos uma classe com dois membros, `client` e `openai` que nos ajudarão a gerir um cliente e a interagir com um LLM respetivamente.
- Configurámos a nossa instância LLM para usar os Modelos do GitHub configurando `baseUrl` para apontar para a API de inferência.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Criar parâmetros do servidor para ligação stdio
server_params = StdioServerParameters(
    command="mcp",  # Executável
    args=["run", "server.py"],  # Argumentos da linha de comando opcionais
    env=None,  # Variáveis de ambiente opcionais
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializar a ligação
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

No código acima fizemos:

- Importámos as bibliotecas necessárias para MCP
- Criámos um cliente

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

Primeiro, precisarás de adicionar as dependências LangChain4j ao teu ficheiro `pom.xml`. Adiciona estas dependências para permitir a integração MCP e a API MiniMax compatível com OpenAI:

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

Define a tua chave API MiniMax e, opcionalmente, o endpoint e modelo.
`MINIMAX_MODEL_ID` suporta `MiniMax-M3` e `MiniMax-M2.7`. Se
`OPENAI_BASE_URL` não estiver definido, `MINIMAX_REGION` suporta `global_en` e `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Para selecionar o endpoint por região em vez disso, omite `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Depois cria a tua classe cliente Java:

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

        // Criar transporte MCP para ligar ao servidor
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Criar cliente MCP
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

No código acima fizemos:

- **Adicionámos dependências LangChain4j**: Necessárias para integração MCP e a API MiniMax compatível com OpenAI
- **Importámos as bibliotecas LangChain4j**: Para integração MCP e funcionalidade do modelo de chat OpenAI
- **Criámos um `ChatLanguageModel`**: Configurado para usar MiniMax com a tua chave API MiniMax, endpoint e ID de modelo suportado
- **Configurámos o transporte HTTP**: Usando Server-Sent Events (SSE) para ligação ao servidor MCP
- **Criámos um cliente MCP**: Que irá gerir a comunicação com o servidor
- **Usámos o suporte integrado MCP do LangChain4j**: Que simplifica a integração entre LLMs e servidores MCP

#### Rust

Este exemplo assume que tens um servidor MCP baseado em Rust a correr. Se não tens, consulta a lição [01-first-server](../01-first-server/README.md) para criar o servidor.

Uma vez que tens o servidor MCP Rust, abre um terminal e navega até à mesma diretoria do servidor. Depois executa o seguinte comando para criar um novo projeto cliente LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Adiciona as seguintes dependências ao teu ficheiro `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Não existe uma biblioteca oficial Rust para OpenAI, no entanto, o crate `async-openai` é uma [biblioteca mantida pela comunidade](https://platform.openai.com/docs/libraries/rust#rust) que é comumente usada.

Abre o ficheiro `src/main.rs` e substitui o seu conteúdo pelo seguinte código:

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
    // Mensagem inicial
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Configurar cliente OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Configurar cliente MCP
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

    // TODO: Obter lista de ferramentas MCP

    // TODO: Conversa LLM com chamadas de ferramentas

    Ok(())
}
```

Este código configura uma aplicação básica Rust que irá ligar a um servidor MCP e aos Modelos do GitHub para interações LLM.

> [!IMPORTANT]
> Assegura-te de definir a variável de ambiente `OPENAI_API_KEY` com o teu token GitHub antes de executar a aplicação.

Ótimo, para o próximo passo, vamos listar as capacidades no servidor.

### -2- Listar capacidades do servidor

Agora vamos ligar ao servidor e pedir as suas capacidades:

#### TypeScript

Na mesma classe, adiciona os seguintes métodos:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // listando ferramentas
    const toolsResult = await this.client.listTools();
}
```

No código acima fizemos:

- Adicionámos código para ligar ao servidor, `connectToServer`.
- Criámos um método `run` responsável por gerir o fluxo da aplicação. Até agora só lista as ferramentas mas vamos adicionar mais em breve.

#### Python

```python
# Listar recursos disponíveis
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Listar ferramentas disponíveis
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Eis o que adicionámos:

- Listagem de recursos e ferramentas e impressão dos mesmos. Para ferramentas também listamos o `inputSchema` que usamos mais tarde.

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

No código acima fizemos:

- Listámos as ferramentas disponíveis no Servidor MCP
- Para cada ferramenta, listámos nome, descrição e o seu esquema. Este último é algo que iremos usar para chamar as ferramentas em breve.

#### Java

```java
// Criar um fornecedor de ferramentas que descubra automaticamente ferramentas MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// O fornecedor de ferramentas MCP gere automaticamente:
// - Listar ferramentas disponíveis do servidor MCP
// - Converter esquemas de ferramentas MCP para o formato LangChain4j
// - Gerir a execução de ferramentas e respostas
```

No código acima fizemos:

- Criámos um `McpToolProvider` que descobre automaticamente e regista todas as ferramentas do servidor MCP
- O provedor de ferramentas trata internamente da conversão entre esquemas das ferramentas MCP e o formato das ferramentas LangChain4j
- Esta abordagem abstrai o processo manual de listagem e conversão das ferramentas

#### Rust

A obtenção das ferramentas do servidor MCP é feita usando o método `list_tools`. Na tua função `main`, depois de configurar o cliente MCP, adiciona o seguinte código:

```rust
// Obter listagem da ferramenta MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Converter capacidades do servidor para ferramentas LLM

O próximo passo depois de listar as capacidades do servidor é convertê-las para um formato que o LLM entenda. Depois de o fazermos, podemos fornecer estas capacidades como ferramentas ao nosso LLM.

#### TypeScript

1. Adiciona o seguinte código para converter a resposta do Servidor MCP para um formato de ferramentas que o LLM possa usar:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Criar um esquema zod baseado no input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Definir explicitamente o tipo para "function"
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

    O código acima pega uma resposta do Servidor MCP e converte-a para um formato de definição de ferramenta que o LLM consegue entender.

2. Vamos atualizar o método `run` para listar capacidades do servidor:

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

    No código acima, atualizámos o método `run` para mapear através do resultado e, para cada entrada, chamar `openAiToolAdapter`.

#### Python

1. Primeiro, vamos criar a seguinte função de conversão

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

    Na função acima `convert_to_llm_tools` pegamos numa resposta de ferramenta MCP e convertemo-la para um formato que o LLM pode entender.

2. A seguir, vamos atualizar o nosso código cliente para usar esta função assim:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Aqui, estamos a adicionar uma chamada a `convert_to_llm_tool` para converter a resposta da ferramenta MCP para algo que podemos alimentar ao LLM depois.

#### .NET

1. Vamos adicionar código para converter a resposta da ferramenta MCP para algo que o LLM compreenda

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

No código acima fizemos:

- Criámos uma função `ConvertFrom` que recebe nome, descrição e esquema de input.
- Definimos uma funcionalidade que cria uma FunçãoDefinição que é passada para uma Definição de ChatCompletions. Esta é algo que o LLM entende.

2. Vamos ver como podemos atualizar algum código existente para tirar partido desta função acima:

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
// Criar uma interface de Bot para interação em linguagem natural
public interface Bot {
    String chat(String prompt);
}

// Configurar o serviço de IA com ferramentas LLM e MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

No código acima fizemos:

- Definimos uma interface simples `Bot` para interações em linguagem natural
- Usámos os `AiServices` do LangChain4j para ligar automaticamente o LLM com o provedor de ferramentas MCP
- O framework trata automaticamente a conversão de esquema de ferramentas e chamadas de funções nos bastidores
- Esta abordagem elimina a conversão manual de ferramentas - o LangChain4j trata de toda a complexidade de converter ferramentas MCP para formato compatível com LLM

#### Rust

Para converter a resposta da ferramenta MCP para um formato que o LLM compreenda, vamos adicionar uma função auxiliar que formata a listagem de ferramentas. Adiciona o seguinte código ao teu ficheiro `main.rs` abaixo da função `main`. Isto será chamado ao fazer pedidos ao LLM:

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

Ótimo, estamos preparados para tratar os pedidos dos utilizadores, por isso vamos a isso a seguir.

### -4- Tratar pedido de prompt do utilizador

Nesta parte do código, vamos tratar pedidos dos utilizadores.

#### TypeScript

1. Adiciona um método que será usado para chamar o nosso LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Chamar a ferramenta do servidor
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fazer algo com o resultado
        // FAZER

        }
    }
    ```

    No código acima fizemos:

    - Adicionámos um método `callTools`.
    - O método recebe uma resposta LLM e verifica que ferramentas foram chamadas, se houver:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // chamar ferramenta
        }
        ```

    - Chama uma ferramenta, se o LLM indicar que deve ser chamada:

        ```typescript
        // 2. Chamar a ferramenta do servidor
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fazer algo com o resultado
        // POR FAZER
        ```

2. Atualiza o método `run` para incluir chamadas ao LLM e chamar `callTools`:

    ```typescript

    // 1. Criar mensagens que são a entrada para o LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Chamar o LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Analisar a resposta do LLM, para cada escolha, verificar se contém chamadas a ferramentas
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Ótimo, vamos listar o código completo:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importar zod para validação de esquema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // pode ser necessário mudar para este url no futuro: https://models.github.ai/inference
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
          // Criar um esquema zod baseado no input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Definir explicitamente o tipo como "function"
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
    
    
          // 2. Chamar a ferramenta do servidor
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Fazer algo com o resultado
          // POR FAZER
    
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
    
        // 3. Analisar a resposta do LLM, para cada escolha, verificar se tem chamadas de ferramentas
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

1. Vamos adicionar algumas importações necessárias para chamar um LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. A seguir, vamos adicionar a função que irá chamar o LLM:

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
            # Parâmetros opcionais
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

    No código acima fizemos:

    - Passámos as nossas funções, que encontramos no servidor MCP e convertidas, para o LLM.
    - Depois chamámos o LLM com essas funções.
    - Depois, estamos a inspecionar o resultado para ver que funções devemos chamar, se houver.
    - Finalmente, passamos um array de funções para chamar.

3. Passo final, vamos atualizar o nosso código principal:

    ```python
    prompt = "Add 2 to 20"

    # perguntar ao LLM quais ferramentas usar, se houver
    functions_to_call = call_llm(prompt, functions)

    # chamar funções sugeridas
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    E pronto, esse foi o passo final, no código acima estamos:

    - A chamar uma ferramenta MCP via `call_tool` usando uma função que o LLM achou que devíamos chamar com base no nosso prompt.
    - A imprimir o resultado da chamada à ferramenta no servidor MCP.

#### .NET

1. Vamos mostrar um pouco de código para fazer um pedido de prompt ao LLM:

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

    No código acima fizemos:

    - Obtivemos ferramentas do servidor MCP, `var tools = await GetMcpTools()`.
    - Definimos um prompt de utilizador `userMessage`.
    - Construímos um objeto de opções especificando o modelo e as ferramentas.
    - Fizemos um pedido ao LLM.

2. Um último passo, vamos ver se o LLM acha que devemos chamar uma função:

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

    No código acima fizemos:

    - Iterámos por uma lista de chamadas de funções.
    - Para cada chamada de ferramenta, analisámos o nome e os argumentos e chamámos a ferramenta no servidor MCP usando o cliente MCP. Por fim, imprimimos os resultados.

Eis o código completo:

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
    // Execute pedidos em linguagem natural que utilizam automaticamente as ferramentas MCP
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

No código acima fizemos:

- Usámos prompts simples em linguagem natural para interagir com as ferramentas do servidor MCP
- O framework LangChain4j trata automaticamente:
  - Da conversão de prompts de utilizador para chamadas de ferramentas quando necessário
  - Da chamada às ferramentas MCP apropriadas com base na decisão do LLM
  - Da gestão do fluxo de conversa entre o LLM e o servidor MCP
- O método `bot.chat()` retorna respostas em linguagem natural que podem incluir resultados de execuções de ferramentas MCP
- Esta abordagem proporciona uma experiência contínua ao utilizador onde não é necessário conhecer a implementação subjacente MCP

Exemplo de código completo:

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

Aqui é onde a maioria do trabalho acontece. Iremos chamar o LLM com o prompt inicial do utilizador, depois processar a resposta para ver se alguma ferramenta precisa ser chamada. Se sim, iremos chamar essas ferramentas e continuar a conversa com o LLM até que não sejam necessárias mais chamadas de ferramentas e tenhamos uma resposta final.


Vamos fazer várias chamadas ao LLM, por isso vamos definir uma função que irá tratar da chamada ao LLM. Adicione a seguinte função ao seu ficheiro `main.rs`:

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

Esta função recebe o cliente LLM, uma lista de mensagens (incluindo o prompt do utilizador), ferramentas do servidor MCP, e envia um pedido ao LLM, retornando a resposta.

A resposta do LLM conterá uma matriz de `choices`. Precisamos de processar o resultado para ver se existem `tool_calls` presentes. Isto indica que o LLM está a pedir que uma ferramenta específica seja chamada com argumentos. Adicione o seguinte código no final do seu ficheiro `main.rs` para definir uma função para tratar a resposta do LLM:

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

    // Imprimir conteúdo se disponível
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Lidar com chamadas de ferramentas
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Adicionar mensagem do assistente

        // Executar cada chamada de ferramenta
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Adicionar resultado da ferramenta às mensagens
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continuar conversa com resultados da ferramenta
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

Se os `tool_calls` estiverem presentes, extrai a informação da ferramenta, chama o servidor MCP com o pedido da ferramenta, e adiciona os resultados às mensagens da conversa. Depois continua a conversa com o LLM e as mensagens são atualizadas com a resposta do assistente e os resultados da chamada à ferramenta.

Para extrair a informação da chamada à ferramenta que o LLM devolve para chamadas MCP, vamos adicionar outra função auxiliar para extrair tudo o que é necessário para efetuar a chamada. Adicione o seguinte código no final do seu ficheiro `main.rs`:

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

Com todas as partes no lugar, agora podemos tratar o prompt inicial do utilizador e chamar o LLM. Atualize a sua função `main` para incluir o seguinte código:

```rust
// Conversa LLM com chamadas a ferramentas
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

Isto irá consultar o LLM com o prompt inicial do utilizador a pedir a soma de dois números, e irá processar a resposta para tratar dinamicamente as chamadas às ferramentas.

Excelente, conseguiu!

## Tarefa

Pegue no código do exercício e construa o servidor com mais ferramentas. Depois crie um cliente com um LLM, como no exercício, e teste com diferentes prompts para garantir que todas as ferramentas do servidor MCP são chamadas dinamicamente. Esta forma de construir um cliente significa que o utilizador final terá uma excelente experiência, pois poderá usar prompts em vez de comandos exatos do cliente, sem se aperceber que algum servidor MCP está a ser chamado.

## Solução

[Solução](./solution/README.md)

## Pontos Principais

- Adicionar um LLM ao seu cliente oferece uma melhor forma para os utilizadores interagirem com servidores MCP.
- É necessário converter a resposta do servidor MCP para algo que o LLM consiga entender.

## Exemplos

- [Calculadora Java](../samples/java/calculator/README.md)
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](../samples/javascript/README.md)
- [Calculadora TypeScript](../samples/typescript/README.md)
- [Calculadora Python](../../../../03-GettingStarted/samples/python)
- [Calculadora Rust](../../../../03-GettingStarted/samples/rust)

## Recursos Adicionais

## O que vem a seguir

- A seguir: [Consumir um servidor usando Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->