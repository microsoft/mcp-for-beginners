# Criar um cliente com LLM

Até agora, viu como criar um servidor e um cliente. O cliente tem sido capaz de chamar o servidor explicitamente para listar as suas ferramentas, recursos e prompts. No entanto, esta não é uma abordagem muito prática. Os seus utilizadores vivem na era agentiva e esperam usar prompts e comunicar com um LLM em seu lugar. Eles não se preocupam se usa MCP para armazenar as suas capacidades; simplesmente esperam interagir usando linguagem natural. Então, como resolvemos isto? A solução é adicionar um LLM ao cliente.

## Visão Geral

Nesta lição, focamo-nos em adicionar um LLM para o seu cliente e mostrar como isto proporciona uma experiência muito melhor para o seu utilizador.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Criar um cliente com um LLM.
- Interagir sem esforço com um servidor MCP usando um LLM.
- Proporcionar uma melhor experiência ao utilizador final no lado do cliente.

## Abordagem

Vamos tentar compreender a abordagem que precisamos de seguir. Adicionar um LLM parece simples, mas será que de facto o faremos?

Eis como o cliente irá interagir com o servidor:

1. Estabelecer ligação com o servidor.

1. Listar capacidades, prompts, recursos e ferramentas, e guardar o seu esquema.

1. Adicionar um LLM e passar as capacidades guardadas e seus esquemas num formato que o LLM entende.

1. Tratar um prompt do utilizador passando-o para o LLM juntamente com as ferramentas listadas pelo cliente.

Ótimo, agora que entendemos como podemos fazer isto a alto nível, vamos experimentar no exercício abaixo.

## Exercício: Criar um cliente com um LLM

Neste exercício, vamos aprender a adicionar um LLM ao nosso cliente.

### Autenticação usando Token de Acesso Pessoal do GitHub

Criar um token GitHub é um processo simples. Aqui está como pode fazê-lo:

- Vá para as Definições do GitHub – Clique na sua foto de perfil no canto superior direito e selecione Definições.
- Navegue até Definições de Desenvolvedor – Desça a página e clique em Definições de Desenvolvedor.
- Selecione Tokens de Acesso Pessoal – Clique em Tokens de acesso fino (Fine-grained tokens) e depois em Gerar novo token.
- Configure o seu Token – Adicione uma nota para referência, defina uma data de expiração e selecione os privilégios necessários. Neste caso, certifique-se de adicionar a permissão Models.
- Gere e Copie o Token – Clique em Gerar token, e certifique-se de copiá-lo imediatamente, pois não poderá vê-lo novamente.

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

No código anterior, nós:

- Importámos as bibliotecas necessárias
- Criámos uma classe com dois membros, `client` e `openai` que nos ajudarão a gerir um cliente e interagir com um LLM respetivamente.
- Configurámos a nossa instância LLM para usar os Models do GitHub, definindo `baseUrl` para apontar para a API de inferência.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Criar parâmetros de servidor para conexão stdio
server_params = StdioServerParameters(
    command="mcp",  # Executável
    args=["run", "server.py"],  # Argumentos opcionais da linha de comandos
    env=None,  # Variáveis de ambiente opcionais
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializar a conexão
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

No código anterior, nós:

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

Primeiro, precisará adicionar as dependências LangChain4j ao seu ficheiro `pom.xml`. Adicione estas dependências para permitir a integração MCP e suporte aos Models do GitHub:

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

Depois crie a sua classe cliente Java:

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
    
    public static void main(String[] args) throws Exception {        // Configurar o LLM para usar modelos do GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Criar transporte MCP para ligação ao servidor
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
}
```

No código anterior, nós:

- **Adicionámos as dependências LangChain4j**: Necessárias para integração MCP, cliente oficial OpenAI e suporte aos Models do GitHub
- **Importámos as bibliotecas LangChain4j**: Para integração MCP e funcionalidade do modelo de chat OpenAI
- **Criámos um `ChatLanguageModel`**: Configurado para usar os Models do GitHub com o seu token GitHub
- **Configurámos transporte HTTP**: Usando Server-Sent Events (SSE) para conectar ao servidor MCP
- **Criámos um cliente MCP**: Que irá lidar com a comunicação com o servidor
- **Utilizámos o suporte MCP incorporado do LangChain4j**: Que simplifica a integração entre LLMs e servidores MCP

#### Rust

Este exemplo assume que tem um servidor MCP baseado em Rust a correr. Se não tiver, consulte a lição [01-first-server](../01-first-server/README.md) para criar o servidor.

Depois de ter o seu servidor MCP em Rust, abra um terminal e navegue até ao mesmo diretório do servidor. Depois execute o seguinte comando para criar um novo projeto cliente LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Adicione as seguintes dependências ao seu ficheiro `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Não existe uma biblioteca oficial Rust para OpenAI, no entanto, o crate `async-openai` é uma [biblioteca mantida pela comunidade](https://platform.openai.com/docs/libraries/rust#rust) que é comumente utilizada.

Abra o ficheiro `src/main.rs` e substitua o seu conteúdo pelo seguinte código:

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

    // TODO: Conversa LLM com chamadas de ferramenta

    Ok(())
}
```

Este código configura uma aplicação Rust básica que irá conectar a um servidor MCP e aos Models GitHub para interações LLM.

> [!IMPORTANT]
> Certifique-se de definir a variável de ambiente `OPENAI_API_KEY` com o seu token GitHub antes de executar a aplicação.

Ótimo, para o próximo passo, vamos listar as capacidades no servidor.

### -2- Listar capacidades do servidor

Agora vamos ligar-nos ao servidor e perguntar pelas suas capacidades:

#### TypeScript

Na mesma classe, adicione os seguintes métodos:

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

No código anterior, nós:

- Adicionámos código para ligar ao servidor, `connectToServer`.
- Criámos um método `run` responsável por gerir o fluxo da aplicação. Até agora, apenas lista as ferramentas, mas iremos adicionar mais em breve.

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

Isto é o que adicionámos:

- Listagem de recursos e ferramentas e impressão dos mesmos. Para ferramentas também listamos `inputSchema` que usaremos mais tarde.

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

No código anterior, nós:

- Listámos as ferramentas disponíveis no servidor MCP
- Para cada ferramenta, listámos nome, descrição e seu esquema. Este último é algo que usaremos para chamar as ferramentas em breve.

#### Java

```java
// Criar um fornecedor de ferramentas que descubra automaticamente as ferramentas MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// O fornecedor de ferramentas MCP gere automaticamente:
// - Listar as ferramentas disponíveis no servidor MCP
// - Converter esquemas de ferramentas MCP para o formato LangChain4j
// - Gerir a execução das ferramentas e as respostas
```

No código anterior, nós:

- Criámos um `McpToolProvider` que descobre automaticamente e regista todas as ferramentas do servidor MCP
- O provedor de ferramentas gere a conversão entre esquemas de ferramentas MCP e o formato de ferramentas do LangChain4j internamente
- Esta abordagem abstrai a listagem manual de ferramentas e o processo de conversão

#### Rust

A obtenção das ferramentas do servidor MCP é feita utilizando o método `list_tools`. Na sua função `main`, após configurar o cliente MCP, adicione o seguinte código:

```rust
// Obter listagem da ferramenta MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Converter capacidades do servidor para ferramentas LLM

O próximo passo depois de listar as capacidades do servidor é convertê-las num formato que o LLM compreenda. Depois de fazermos isso, podemos fornecer estas capacidades como ferramentas ao nosso LLM.

#### TypeScript

1. Adicione o seguinte código para converter a resposta do servidor MCP para um formato de ferramenta que o LLM pode usar:

    ```typescript
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

    ```

    O código acima pega numa resposta do servidor MCP e converte-a para um formato de definição de ferramenta que o LLM entende.

1. Vamos atualizar o método `run` em seguida para listar as capacidades do servidor:

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

    No código anterior, atualizámos o método `run` para mapear os resultados e, para cada entrada, chamar `openAiToolAdapter`.

#### Python

1. Primeiro, vamos criar a seguinte função conversora

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

    Na função acima, `convert_to_llm_tools`, pegamos numa resposta de ferramenta MCP e convertê-mo-la para um formato que o LLM pode entender.

1. A seguir, vamos atualizar o nosso código cliente para tirar partido desta função assim:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Aqui, estamos a adicionar uma chamada para `convert_to_llm_tool` para converter a resposta da ferramenta MCP para algo que possamos alimentar ao LLM depois.

#### .NET

1. Vamos adicionar código para converter a resposta da ferramenta MCP para algo que o LLM possa entender:

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

No código anterior, nós:

- Criámos uma função `ConvertFrom` que recebe nome, descrição e esquema de entrada.
- Definimos uma funcionalidade que cria uma `FunctionDefinition` que é passada para uma `ChatCompletionsDefinition`. Esta última é algo que o LLM pode compreender.

1. Vamos ver como podemos atualizar algum código existente para tirar proveito desta função acima:

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

No código anterior, nós:

- Definimos uma simples interface `Bot` para interações em linguagem natural
- Usámos os `AiServices` do LangChain4j para ligar automaticamente o LLM com o provedor de ferramentas MCP
- O framework trata automaticamente a conversão do esquema da ferramenta e a invocação da função nos bastidores
- Esta abordagem elimina a conversão manual de ferramentas – o LangChain4j trata de toda a complexidade de converter ferramentas MCP para um formato compatível com LLM

#### Rust

Para converter a resposta de ferramenta MCP para um formato que o LLM entenda, vamos adicionar uma função auxiliar que formata a listagem das ferramentas. Acrescente o seguinte código ao seu ficheiro `main.rs` abaixo da função `main`. Isto será chamado ao fazer pedidos ao LLM:

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

Ótimo, agora estamos preparados para lidar com pedidos de utilizadores; vamos focar nisso a seguir.

### -4- Tratar pedido de prompt do utilizador

Nesta parte do código, iremos tratar os pedidos do utilizador.

#### TypeScript

1. Adicione um método que será usado para chamar o nosso LLM:

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
        // POR FAZER

        }
    }
    ```

    No código anterior, nós:

    - Adicionámos um método `callTools`.
    - O método recebe uma resposta do LLM e verifica que ferramentas foram chamadas, se alguma:

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
        // A FAZER
        ```

1. Atualize o método `run` para incluir chamadas ao LLM e chamar `callTools`:

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

    // 3. Analisar a resposta do LLM, para cada escolha, verificar se tem chamadas a ferramentas
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
import { z } from "zod"; // Importar zod para validação do esquema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // pode ser necessário mudar para este URL no futuro: https://models.github.ai/inference
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
          // Criar um esquema zod baseado no esquema_de_entrada
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Definir explicitamente o tipo como "função"
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
    
        // 1. Analisar a resposta do LLM, para cada escolha, verificar se tem chamadas de ferramentas
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

1. Em seguida, vamos adicionar a função que chamará o LLM:

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

    No código anterior, nós:

    - Passámos as funções que encontramos no servidor MCP e convertidas para o LLM.
    - Chamámos o LLM com essas funções.
    - Depois, inspecionamos o resultado para ver que funções devemos chamar, se houver alguma.
    - Finalmente, passamos um array de funções para chamar.

1. Passo final, vamos atualizar o nosso código principal:

    ```python
    prompt = "Add 2 to 20"

    # perguntar ao LLM quais ferramentas usar, se houver
    functions_to_call = call_llm(prompt, functions)

    # chamar as funções sugeridas
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Aí está, foi o passo final, no código acima nós:

    - Chamamos uma ferramenta MCP via `call_tool` usando uma função que o LLM achou que deveríamos chamar com base no nosso prompt.
    - Imprimimos o resultado da chamada da ferramenta ao servidor MCP.

#### .NET

1. Vamos mostrar algum código para fazer um pedido de prompt LLM:

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

    No código anterior, nós:

    - Obtivemos as ferramentas do servidor MCP, `var tools = await GetMcpTools()`.
    - Definimos um prompt de utilizador `userMessage`.
    - Construímos um objeto de opções especificando modelo e ferramentas.
    - Fizemos um pedido ao LLM.

1. Um último passo, vamos ver se o LLM acha que devemos chamar uma função:

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

    No código anterior, nós:

    - Percorremos uma lista de chamadas a funções.
    - Para cada chamada a ferramenta, extraímos nome e argumentos e chamamos a ferramenta no servidor MCP usando o cliente MCP. Finalmente imprimimos os resultados.

Aqui está o código completo:

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

No código anterior, nós:

- Usámos simples prompts em linguagem natural para interagir com as ferramentas do servidor MCP
- O framework LangChain4j trata automaticamente:
  - A conversão dos prompts do utilizador em chamadas às ferramentas quando necessário
  - Chamar as ferramentas MCP apropriadas baseadas na decisão do LLM
  - Gerir o fluxo de conversação entre o LLM e o servidor MCP
- O método `bot.chat()` retorna respostas em linguagem natural que podem incluir resultados das execuções das ferramentas MCP
- Esta abordagem proporciona uma experiência de utilizador integrada onde os utilizadores não precisam de saber sobre a implementação MCP subjacente

Exemplo completo do código:

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

Aqui é onde a maior parte do trabalho acontece. Chamaremos o LLM com o prompt inicial do utilizador, depois processaremos a resposta para ver se alguma ferramenta precisa ser chamada. Se assim for, chamaremos essas ferramentas e continuaremos a conversa com o LLM até que não sejam necessárias mais chamadas e tenhamos uma resposta final.

Faremos múltiplas chamadas ao LLM, por isso vamos definir uma função que irá tratar a chamada ao LLM. Adicione a seguinte função ao seu ficheiro `main.rs`:

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

Esta função recebe o cliente LLM, uma lista de mensagens (incluindo o prompt do utilizador), as ferramentas do servidor MCP, envia um pedido ao LLM e retorna a resposta.
A resposta do LLM conterá um array de `choices`. Precisamos processar o resultado para ver se existem `tool_calls`. Isto indica que o LLM está a pedir que uma ferramenta específica seja chamada com argumentos. Adicione o seguinte código ao final do seu ficheiro `main.rs` para definir uma função que trata a resposta do LLM:

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

    // Executar chamadas de ferramenta
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

Se existirem `tool_calls`, extrai a informação da ferramenta, chama o servidor MCP com o pedido da ferramenta e adiciona os resultados às mensagens da conversa. Depois, continua a conversa com o LLM e as mensagens são atualizadas com a resposta do assistente e os resultados da chamada da ferramenta.

Para extrair a informação da chamada de ferramentas que o LLM retorna para chamadas MCP, iremos adicionar outra função auxiliar para extrair tudo o que é necessário para fazer a chamada. Adicione o seguinte código ao final do seu ficheiro `main.rs`:

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
// Conversa LLM com chamadas de ferramentas
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

Isto irá consultar o LLM com o prompt inicial do utilizador a pedir a soma de dois números, e irá processar a resposta para lidar de forma dinâmica com chamadas de ferramentas.

Ótimo, conseguiu!

## Tarefa

Pegue no código do exercício e construa o servidor com mais algumas ferramentas. Depois crie um cliente com um LLM, como no exercício, e teste com diferentes prompts para garantir que todas as suas ferramentas do servidor são chamadas de forma dinâmica. Esta forma de construir um cliente significa que o utilizador final terá uma ótima experiência ao poder usar prompts, em vez de comandos exatos do cliente, sem se aperceber de qualquer servidor MCP a ser chamado.

## Solução

[Solution](./solution/README.md)

## Principais Conclusões

- Adicionar um LLM ao seu cliente oferece uma forma melhor para os utilizadores interagirem com Servidores MCP.
- É necessário converter a resposta do Servidor MCP para algo que o LLM possa compreender.

## Exemplos

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Recursos Adicionais

## Próximos Passos

- Seguinte: [Consumir um servidor usando Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->