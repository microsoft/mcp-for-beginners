# Criando um cliente

Clientes são aplicativos ou scripts personalizados que se comunicam diretamente com um servidor MCP para solicitar recursos, ferramentas e prompts. Diferentemente do uso da ferramenta de inspeção, que fornece uma interface gráfica para interagir com o servidor, escrever seu próprio cliente permite interações programáticas e automatizadas. Isso possibilita que os desenvolvedores integrem as capacidades do MCP em seus próprios fluxos de trabalho, automatizem tarefas e criem soluções personalizadas adaptadas às necessidades específicas.

## Visão Geral

Esta lição introduz o conceito de clientes dentro do ecossistema do Model Context Protocol (MCP). Você aprenderá como escrever seu próprio cliente e conectá-lo a um servidor MCP.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Entender o que um cliente pode fazer.
- Escrever seu próprio cliente.
- Conectar e testar o cliente com um servidor MCP para garantir que este funcione conforme esperado.

## O que envolve escrever um cliente?

Para escrever um cliente, você precisará fazer o seguinte:

- **Importar as bibliotecas corretas**. Você usará a mesma biblioteca de antes, apenas com diferentes construções.
- **Instanciar um cliente**. Isso envolverá criar uma instância de cliente e conectá-la ao método de transporte escolhido.
- **Decidir quais recursos listar**. Seu servidor MCP vem com recursos, ferramentas e prompts; você precisa decidir quais listar.
- **Integrar o cliente a um aplicativo host**. Depois de conhecer as capacidades do servidor, você precisa integrá-lo ao seu aplicativo host para que, se um usuário digitar um prompt ou outro comando, o recurso correspondente do servidor seja invocado.

Agora que entendemos em alto nível o que estamos prestes a fazer, vamos olhar um exemplo a seguir.

### Um exemplo de cliente

Vamos dar uma olhada neste exemplo de cliente:

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

No código anterior, nós:

- Importamos as bibliotecas.
- Criamos uma instância de cliente e a conectamos usando stdio como transporte.
- Listamos prompts, recursos e ferramentas e os invocamos.

Pronto, você tem um cliente que pode se comunicar com um servidor MCP.

Vamos dedicar nosso tempo na próxima seção de exercícios para analisar cada trecho de código e explicar o que está acontecendo.

## Exercício: Escrevendo um cliente

Como mencionado acima, vamos dedicar nosso tempo explicando o código e, se quiser, acompanhe codificando.

### -1- Importar as bibliotecas

Vamos importar as bibliotecas necessárias. Precisaremos de referências a um cliente e ao protocolo de transporte escolhido, stdio. stdio é um protocolo para coisas que devem ser executadas na sua máquina local. SSE é outro protocolo de transporte que mostraremos em capítulos futuros, mas essa é sua outra opção. Por enquanto, vamos continuar com stdio.

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

Para Java, você criará um cliente que se conecta ao servidor MCP do exercício anterior. Usando a mesma estrutura de projeto Java Spring Boot de [Introdução ao Servidor MCP](../../../../03-GettingStarted/01-first-server/solution/java), crie uma nova classe Java chamada `SDKClient` na pasta `src/main/java/com/microsoft/mcp/sample/client/` e adicione as seguintes importações:

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

Você precisará adicionar as seguintes dependências ao seu arquivo `Cargo.toml`.

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

A partir daí, você pode importar as bibliotecas necessárias no código do cliente.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Vamos avançar para a instância.

### -2- Instanciando cliente e transporte

Precisaremos criar uma instância do transporte e outra do cliente:

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

No código anterior, nós:

- Criamos uma instância de transporte stdio. Note como ela especifica o comando e os argumentos para localizar e iniciar o servidor, pois isso é algo que precisaremos fazer ao criar o cliente.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instanciamos um cliente fornecendo um nome e uma versão.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Conectamos o cliente ao transporte escolhido.

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

No código anterior, nós:

- Importamos as bibliotecas necessárias.
- Instanciamos um objeto de parâmetros do servidor, pois usaremos isso para executar o servidor e conectá-lo ao nosso cliente.
- Definimos um método `run` que, por sua vez, chama `stdio_client`, iniciando uma sessão de cliente.
- Criamos um ponto de entrada onde fornecemos o método `run` para `asyncio.run`.

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

No código anterior, nós:

- Importamos as bibliotecas necessárias.
- Criamos um transporte stdio e um cliente `mcpClient`. Este último será usado para listar e invocar recursos no servidor MCP.

Nota: em "Arguments", você pode apontar para o arquivo *.csproj* ou para o executável.

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

No código anterior, nós:

- Criamos um método principal que configura um transporte SSE apontando para `http://localhost:8080`, onde nosso servidor MCP estará em execução.
- Criamos uma classe de cliente que recebe o transporte como parâmetro do construtor.
- No método `run`, criamos um cliente MCP síncrono usando o transporte e inicializamos a conexão.
- Usamos o transporte SSE (Server-Sent Events), que é adequado para comunicação baseada em HTTP com servidores MCP Java Spring Boot.

#### Rust

Este cliente Rust assume que o servidor é um projeto irmão chamado "calculator-server" no mesmo diretório. O código abaixo iniciará o servidor e se conectará a ele.

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

### -3- Listando os recursos do servidor

Agora, temos um cliente que pode se conectar caso o programa seja executado. No entanto, ele não lista seus recursos, então vamos fazer isso a seguir:

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

Aqui, listamos os recursos disponíveis, `list_resources()` e ferramentas, `list_tools`, e os imprimimos.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Acima está um exemplo de como podemos listar as ferramentas no servidor. Para cada ferramenta, imprimimos seu nome.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

No código anterior, nós:

- Chamamos `listTools()` para obter todas as ferramentas disponíveis no servidor MCP.
- Usamos `ping()` para verificar se a conexão com o servidor está funcionando.
- O `ListToolsResult` contém informações sobre todas as ferramentas, incluindo seus nomes, descrições e esquemas de entrada.

Ótimo, agora capturamos todos os recursos. A questão agora é: quando os usamos? Bem, este cliente é bastante simples, no sentido de que precisaremos chamar explicitamente os recursos quando quisermos. No próximo capítulo, criaremos um cliente mais avançado que terá acesso ao seu próprio modelo de linguagem grande, LLM. Por enquanto, vamos ver como podemos invocar os recursos no servidor:

#### Rust

Na função principal, após inicializar o cliente, podemos inicializar o servidor e listar alguns de seus recursos.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocar recursos

Para invocar os recursos, precisamos garantir que especificamos os argumentos corretos e, em alguns casos, o nome do que estamos tentando invocar.

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

No código anterior, nós:

- Lemos um recurso, chamamos o recurso usando `readResource()` especificando `uri`. Veja como isso provavelmente se parece no lado do servidor:

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

    Nosso valor `uri` `file://example.txt` corresponde a `file://{name}` no servidor. `example.txt` será mapeado para `name`.

- Chamamos uma ferramenta, especificamos seu `name` e seus `arguments` assim:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Obtemos um prompt, para obter um prompt, chamamos `getPrompt()` com `name` e `arguments`. O código do servidor se parece com isso:

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

    E, portanto, o código do cliente resultante se parece com isso para corresponder ao que foi declarado no servidor:

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

No código anterior, nós:

- Chamamos um recurso chamado `greeting` usando `read_resource`.
- Invocamos uma ferramenta chamada `add` usando `call_tool`.

#### .NET

1. Vamos adicionar algum código para chamar uma ferramenta:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Para imprimir o resultado, aqui está um código para lidar com isso:

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

No código anterior, nós:

- Chamamos várias ferramentas de calculadora usando o método `callTool()` com objetos `CallToolRequest`.
- Cada chamada de ferramenta especifica o nome da ferramenta e um `Map` de argumentos necessários para essa ferramenta.
- As ferramentas do servidor esperam nomes de parâmetros específicos (como "a", "b" para operações matemáticas).
- Os resultados são retornados como objetos `CallToolResult` contendo a resposta do servidor.

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

### -5- Executar o cliente

Para executar o cliente, digite o seguinte comando no terminal:

#### TypeScript

Adicione a seguinte entrada à seção "scripts" em *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Chame o cliente com o seguinte comando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Primeiro, certifique-se de que seu servidor MCP está em execução em `http://localhost:8080`. Em seguida, execute o cliente:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativamente, você pode executar o projeto completo do cliente fornecido na pasta de solução `03-GettingStarted\02-client\solution\java`:

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

## Tarefa

Nesta tarefa, você usará o que aprendeu ao criar um cliente, mas criará um cliente próprio.

Aqui está um servidor que você pode usar e que precisa ser chamado via seu código de cliente. Veja se consegue adicionar mais recursos ao servidor para torná-lo mais interessante.

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

Veja este projeto para saber como [adicionar prompts e recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Além disso, confira este link para saber como invocar [prompts e recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Na [seção anterior](../../../../03-GettingStarted/01-first-server), você aprendeu como criar um servidor MCP simples com Rust. Você pode continuar a construir sobre isso ou verificar este link para mais exemplos de servidores MCP baseados em Rust: [Exemplos de Servidores MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solução

A **pasta de solução** contém implementações completas e prontas para uso de clientes que demonstram todos os conceitos abordados neste tutorial. Cada solução inclui código de cliente e servidor organizado em projetos separados e autossuficientes.

### 📁 Estrutura da Solução

O diretório de solução está organizado por linguagem de programação:

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

### 🚀 O que cada solução inclui

Cada solução específica de linguagem fornece:

- **Implementação completa do cliente** com todos os recursos do tutorial.
- **Estrutura de projeto funcional** com dependências e configuração adequadas.
- **Scripts de construção e execução** para configuração e execução fáceis.
- **README detalhado** com instruções específicas para cada linguagem.
- **Exemplos de tratamento de erros** e processamento de resultados.

### 📖 Usando as Soluções

1. **Navegue até a pasta da sua linguagem preferida**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Siga as instruções do README** em cada pasta para:
   - Instalar dependências.
   - Construir o projeto.
   - Executar o cliente.

3. **Exemplo de saída** que você deve ver:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para documentação completa e instruções passo a passo, veja: **[📖 Documentação da Solução](./solution/README.md)**

## 🎯 Exemplos Completos

Fornecemos implementações completas e funcionais de clientes para todas as linguagens de programação abordadas neste tutorial. Esses exemplos demonstram toda a funcionalidade descrita acima e podem ser usados como implementações de referência ou pontos de partida para seus próprios projetos.

### Exemplos Completos Disponíveis

| Linguagem | Arquivo | Descrição |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Cliente Java completo usando transporte SSE com tratamento abrangente de erros |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Cliente C# completo usando transporte stdio com inicialização automática do servidor |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Cliente TypeScript completo com suporte total ao protocolo MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Cliente Python completo usando padrões async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Cliente Rust completo usando Tokio para operações assíncronas |
Cada exemplo completo inclui:

- ✅ **Estabelecimento de conexão** e tratamento de erros  
- ✅ **Descoberta do servidor** (ferramentas, recursos, prompts, onde aplicável)  
- ✅ **Operações da calculadora** (somar, subtrair, multiplicar, dividir, ajuda)  
- ✅ **Processamento de resultados** e saída formatada  
- ✅ **Tratamento abrangente de erros**  
- ✅ **Código limpo e documentado** com comentários passo a passo  

### Começando com Exemplos Completos

1. **Escolha seu idioma preferido** na tabela acima  
2. **Revise o arquivo de exemplo completo** para entender a implementação completa  
3. **Execute o exemplo** seguindo as instruções em [`complete_examples.md`](./complete_examples.md)  
4. **Modifique e amplie** o exemplo para atender ao seu caso de uso específico  

Para documentação detalhada sobre como executar e personalizar esses exemplos, veja: **[📖 Documentação de Exemplos Completos](./complete_examples.md)**  

### 💡 Solução vs. Exemplos Completos

| **Pasta de Solução**       | **Exemplos Completos**       |
|----------------------------|-----------------------------|
| Estrutura completa do projeto com arquivos de build | Implementações em arquivo único |
| Pronto para executar com dependências              | Exemplos de código focados      |
| Configuração semelhante à produção                 | Referência educacional          |
| Ferramentas específicas para cada linguagem        | Comparação entre linguagens     |

Ambas as abordagens são valiosas - use a **pasta de solução** para projetos completos e os **exemplos completos** para aprendizado e referência.

## Principais Pontos

Os principais pontos deste capítulo sobre clientes são os seguintes:

- Podem ser usados tanto para descobrir quanto para invocar funcionalidades no servidor.  
- Podem iniciar um servidor enquanto se iniciam (como neste capítulo), mas também podem se conectar a servidores já em execução.  
- São uma ótima maneira de testar as capacidades do servidor, além de alternativas como o Inspector, descrito no capítulo anterior.  

## Recursos Adicionais

- [Construindo clientes em MCP](https://modelcontextprotocol.io/quickstart/client)  

## Exemplos

- [Calculadora em Java](../samples/java/calculator/README.md)  
- [Calculadora em .Net](../../../../03-GettingStarted/samples/csharp)  
- [Calculadora em JavaScript](../samples/javascript/README.md)  
- [Calculadora em TypeScript](../samples/typescript/README.md)  
- [Calculadora em Python](../../../../03-GettingStarted/samples/python)  
- [Calculadora em Rust](../../../../03-GettingStarted/samples/rust)  

## O Que Vem a Seguir

- Próximo: [Criando um cliente com um LLM](../03-llm-client/README.md)  

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.