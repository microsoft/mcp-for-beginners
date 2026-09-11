# Criando um cliente

Clientes são aplicações ou scripts personalizados que se comunicam diretamente com um Servidor MCP para solicitar recursos, ferramentas e prompts. Diferente de usar a ferramenta de inspeção, que fornece uma interface gráfica para interagir com o servidor, escrever seu próprio cliente permite interações programáticas e automatizadas. Isso possibilita aos desenvolvedores integrar as capacidades do MCP em seus próprios fluxos de trabalho, automatizar tarefas e construir soluções personalizadas adequadas a necessidades específicas.

## Visão geral

Esta lição apresenta o conceito de clientes dentro do ecossistema do Protocolo de Contexto de Modelo (MCP). Você aprenderá como escrever seu próprio cliente e conectá-lo a um Servidor MCP.

## Objetivos de aprendizagem

Ao final desta lição, você será capaz de:

- Entender o que um cliente pode fazer.
- Escrever seu próprio cliente.
- Conectar e testar o cliente com um servidor MCP para garantir que ele funciona conforme esperado.

## O que envolve escrever um cliente?

Para escrever um cliente, você precisará realizar o seguinte:

- **Importar as bibliotecas corretas**. Você usará a mesma biblioteca de antes, apenas com construções diferentes.
- **Instanciar um cliente**. Isso envolve criar uma instância do cliente e conectá-la ao método de transporte escolhido.
- **Decidir quais recursos listar**. Seu servidor MCP vem com recursos, ferramentas e prompts, você precisa decidir qual deles listar.
- **Integrar o cliente a uma aplicação host**. Depois de conhecer as capacidades do servidor, você precisa integrar isso à sua aplicação host para que, se um usuário digitar um prompt ou outro comando, o recurso correspondente do servidor seja invocado.

Agora que entendemos em alto nível o que faremos, vamos ver um exemplo a seguir.

### Um exemplo de cliente

Vamos olhar para este exemplo de cliente:

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

// Listar prompts
const prompts = await client.listPrompts();

// Obter um prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Listar recursos
const resources = await client.listResources();

// Ler um recurso
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Chamar uma ferramenta
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

No código acima nós:

- Importamos as bibliotecas
- Criamos uma instância de cliente e a conectamos usando `stdio` para transporte.
- Listamos prompts, recursos e ferramentas e invocamos todos eles.

Aí está, um cliente que pode conversar com um Servidor MCP.

Vamos dedicar um tempo na próxima seção de exercícios para detalhar cada trecho de código e explicar o que está acontecendo.

## Exercício: Escrevendo um cliente

Conforme dito acima, vamos dedicar tempo explicando o código e, por todos os meios, programe junto se quiser.

### -1- Importando as bibliotecas

Vamos importar as bibliotecas necessárias, precisaremos de referências a um cliente e ao protocolo de transporte escolhido, `stdio`. `stdio` é um protocolo para coisas que devem rodar na sua máquina local. SSE é outro protocolo de transporte que mostraremos em capítulos futuros, mas essa é sua outra opção. Por enquanto, vamos continuar com `stdio`.

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

Para Java, você criará um cliente que se conecta ao servidor MCP do exercício anterior. Usando a mesma estrutura de projeto Java Spring Boot de [Introdução ao Servidor MCP](../../../../03-GettingStarted/01-first-server/solution/java), crie uma nova classe Java chamada `SDKClient` na pasta `src/main/java/com/microsoft/mcp/sample/client/` e adicione os seguintes imports:

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

A partir daí, você pode importar as bibliotecas necessárias no seu código cliente.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Vamos avançar para a instanciação.

### -2- Instanciando cliente e transporte

Precisaremos criar uma instância do transporte e do nosso cliente:

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

No código acima nós:

- Criamos uma instância de transporte stdio. Note como especifica comando e argumentos para como encontrar e iniciar o servidor, pois isso será algo que precisaremos fazer ao criarmos o cliente.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instanciamos um cliente dando-lhe um nome e versão.

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

# Criar parâmetros do servidor para conexão stdio
server_params = StdioServerParameters(
    command="mcp",  # Executável
    args=["run", "server.py"],  # Argumentos opcionais da linha de comando
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

No código acima nós:

- Importamos as bibliotecas necessárias
- Instanciamos um objeto de parâmetros do servidor que usaremos para rodar o servidor para então conectarmos com nosso cliente.
- Definimos um método `run` que por sua vez chama `stdio_client` que inicia uma sessão de cliente.
- Criamos um ponto de entrada onde fornecemos o método `run` para `asyncio.run`.

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

No código acima nós:

- Importamos as bibliotecas necessárias.
- Criamos um transporte stdio e um cliente `mcpClient`. Este último será usado para listar e invocar funcionalidades no Servidor MCP.

Note que, em "Arguments", você pode indicar o *.csproj* ou o executável.

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
        
        // Sua lógica de cliente vai aqui
    }
}
```

No código acima nós:

- Criamos um método principal que configura um transporte SSE apontando para `http://localhost:8080` onde nosso servidor MCP estará rodando.
- Criamos uma classe cliente que recebe o transporte como parâmetro no construtor.
- No método `run`, criamos um cliente MCP síncrono usando o transporte e inicializamos a conexão.
- Usamos o transporte SSE (Server-Sent Events) que é adequado para comunicação baseada em HTTP com servidores MCP Java Spring Boot.

#### Rust

Note que este cliente Rust assume que o servidor é um projeto irmão chamado "calculator-server" no mesmo diretório. O código abaixo iniciará o servidor e se conectará a ele.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assuma que o servidor é um projeto irmão chamado "calculator-server" no mesmo diretório
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

    // TODO: Inicializar

    // TODO: Listar ferramentas

    // TODO: Chamar a ferramenta adicionar com argumentos = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Listando as funcionalidades do servidor

Agora, temos um cliente que pode se conectar caso o programa seja executado. No entanto, ele não lista suas funcionalidades, então vamos fazer isso a seguir:

#### TypeScript

```typescript
// Listar prompts
const prompts = await client.listPrompts();

// Listar recursos
const resources = await client.listResources();

// listar ferramentas
const tools = await client.listTools();
```

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
```

Aqui listamos os recursos disponíveis, `list_resources()` e as ferramentas, `list_tools`, e os imprimimos.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Acima está um exemplo de como podemos listar as ferramentas no servidor. Para cada ferramenta, então imprimimos seu nome.

#### Java

```java
// Listar e demonstrar ferramentas
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Você também pode pingar o servidor para verificar a conexão
client.ping();
```

No código acima nós:

- Chamamos `listTools()` para obter todas as ferramentas disponíveis do servidor MCP.
- Usamos `ping()` para verificar se a conexão com o servidor está funcionando.
- O `ListToolsResult` contém informações sobre todas as ferramentas incluindo seus nomes, descrições e esquemas de entrada.

Ótimo, agora capturamos todas as funcionalidades. Agora a questão é: quando usamos elas? Bem, este cliente é bem simples, simples no sentido que precisaremos chamar explicitamente as funcionalidades quando quisermos. No próximo capítulo, criaremos um cliente mais avançado que terá acesso ao seu próprio modelo de linguagem grande, LLM. Por enquanto, vamos ver como invocar as funcionalidades no servidor:

#### Rust

Na função principal, após inicializar o cliente, podemos inicializar o servidor e listar algumas de suas funcionalidades.

```rust
// Inicializar
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Listar ferramentas
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocar funcionalidades

Para invocar as funcionalidades precisamos garantir que especificamos os argumentos corretos e em alguns casos o nome do que estamos tentando invocar.

#### TypeScript

```typescript

// Ler um recurso
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Chamar uma ferramenta
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// chamar prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

No código acima nós:

- Lemos um recurso, chamamos o recurso utilizando `readResource()` especificando `uri`. Veja como provavelmente é no lado do servidor:

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

- Chamamos uma ferramenta, fazemos isso especificando seu `name` e seus `arguments` assim:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Pegamos um prompt, para obter um prompt, chamamos `getPrompt()` com `name` e `arguments`. O código do servidor se parece com isso:

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

    e assim o código resultante do cliente fica para casar com o que foi declarado no servidor:

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
# Ler um recurso
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Chamar uma ferramenta
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

No código acima, nós:

- Chamamos o recurso chamado `greeting` usando `read_resource`.
- Invocamos a ferramenta chamada `add` usando `call_tool`.

#### .NET

1. Vamos adicionar código para chamar uma ferramenta:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Para imprimir o resultado, aqui está o código para lidar com isso:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Chamar várias ferramentas de calculadora
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

No código acima nós:

- Chamamos múltiplas ferramentas de calculadora usando o método `callTool()` com objetos `CallToolRequest`.
- Cada chamada de ferramenta especifica o nome da ferramenta e um `Map` de argumentos requeridos por aquela ferramenta.
- As ferramentas do servidor esperam nomes de parâmetros específicos (como "a", "b" para operações matemáticas).
- Resultados são retornados como objetos `CallToolResult` contendo a resposta do servidor.

#### Rust

```rust
// Chame a ferramenta add com argumentos = {"a": 3, "b": 2}
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

Adicione a seguinte entrada à sua seção "scripts" no *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Execute o cliente com o seguinte comando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Primeiro, certifique-se de que seu servidor MCP está rodando em `http://localhost:8080`. Depois, execute o cliente:

```bash
# Construa seu projeto
./mvnw clean compile

# Execute o cliente
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativamente, você pode executar o projeto cliente completo fornecido na pasta de solução `03-GettingStarted\02-client\solution\java`:

```bash
# Navegue até o diretório da solução
cd 03-GettingStarted/02-client/solution/java

# Compile e execute o JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Tarefa

Nesta tarefa, você usará o que aprendeu para criar um cliente, mas crie um cliente seu próprio.

Aqui está um servidor que você pode usar e que precisa chamar via seu código cliente; veja se consegue adicionar mais funcionalidades ao servidor para torná-lo mais interessante.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Criar um servidor MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Adicionar uma ferramenta de adição
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Adicionar um recurso de saudação dinâmica
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

// Começar a receber mensagens na entrada padrão e enviar mensagens na saída padrão

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

# Criar um servidor MCP
mcp = FastMCP("Demo")


# Adicionar uma ferramenta de adição
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Adicionar um recurso dinâmico de saudação
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

Veja este projeto para ver como você pode [adicionar prompts e recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Também, confira este link para como invocar [prompts e recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Na [seção anterior](../../../../03-GettingStarted/01-first-server), você aprendeu a criar um servidor MCP simples com Rust. Você pode continuar construindo a partir disso ou conferir este link para mais exemplos de servidores MCP baseados em Rust: [Exemplos de Servidores MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solução

A **pasta da solução** contém implementações completas de clientes prontas para rodar que demonstram todos os conceitos abordados neste tutorial. Cada solução inclui tanto o código do cliente quanto do servidor organizados em projetos separados e autônomos.

### 📁 Estrutura da Solução

O diretório da solução está organizado por linguagem de programação:

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

Cada solução específica para a linguagem fornece:

- **Implementação completa do cliente** com todas as funcionalidades do tutorial
- **Estrutura do projeto funcional** com dependências e configurações adequadas
- **Scripts de build e execução** para fácil configuração e execução
- **README detalhado** com instruções específicas para cada linguagem
- **Exemplos de tratamento de erros** e processamento de resultados

### 📖 Usando as Soluções

1. **Navegue até a pasta da linguagem preferida**:

   ```bash
   cd solution/typescript/    # Para TypeScript
   cd solution/java/          # Para Java
   cd solution/python/        # Para Python
   cd solution/dotnet/        # Para .NET
   ```

2. **Siga as instruções no README** em cada pasta para:
   - Instalar dependências
   - Construir o projeto
   - Executar o cliente

3. **Exemplo de saída** que você deve ver:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para documentação completa e instruções passo a passo, veja: **[📖 Documentação da Solução](./solution/README.md)**

## 🎯 Exemplos Completos

Fornecemos implementações completas e funcionais de clientes para todas as linguagens de programação abordadas neste tutorial. Estes exemplos demonstram toda a funcionalidade descrita acima e podem ser usados como implementações de referência ou pontos de partida para seus próprios projetos.

### Exemplos Completos Disponíveis

| Linguagem | Arquivo | Descrição |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Cliente Java completo usando transporte SSE com tratamento completo de erros |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Cliente C# completo usando transporte stdio com inicialização automática do servidor |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Cliente TypeScript completo com suporte total ao protocolo MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Cliente Python completo usando padrões async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Cliente Rust completo usando Tokio para operações assíncronas |

Cada exemplo completo inclui:

- ✅ **Estabelecimento de conexão** e tratamento de erros
- ✅ **Descoberta do servidor** (ferramentas, recursos, prompts onde aplicável)
- ✅ **Operações da calculadora** (adicionar, subtrair, multiplicar, dividir, ajuda)
- ✅ **Processamento de resultados** e saída formatada
- ✅ **Tratamento abrangente de erros**

- ✅ **Código limpo e documentado** com comentários passo a passo

### Começando com Exemplos Completos

1. **Escolha sua linguagem preferida** na tabela acima
2. **Revise o arquivo de exemplo completo** para entender a implementação completa
3. **Execute o exemplo** seguindo as instruções em [`complete_examples.md`](./complete_examples.md)
4. **Modifique e expanda** o exemplo para seu caso de uso específico

Para documentação detalhada sobre como executar e personalizar esses exemplos, veja: **[📖 Documentação dos Exemplos Completos](./complete_examples.md)**

### 💡 Solução vs. Exemplos Completos

| **Pasta da Solução** | **Exemplos Completos** |
|--------------------|--------------------- |
| Estrutura completa do projeto com arquivos de build | Implementações em arquivo único |
| Pronto para rodar com dependências | Exemplos de código focados |
| Configuração semelhante à produção | Referência educacional |
| Ferramentas específicas para a linguagem | Comparação entre linguagens |

Ambas as abordagens são valiosas - use a **pasta da solução** para projetos completos e os **exemplos completos** para aprendizado e referência.

## Principais Conclusões

As principais conclusões deste capítulo sobre clientes são as seguintes:

- Podem ser usados tanto para descobrir quanto para invocar funcionalidades no servidor.
- Podem iniciar um servidor enquanto ele se inicia sozinho (como neste capítulo), mas clientes também podem se conectar a servidores em execução.
- São uma ótima maneira de testar capacidades do servidor ao lado de alternativas como o Inspector, conforme descrito no capítulo anterior.

## Recursos Adicionais

- [Construindo clientes em MCP](https://modelcontextprotocol.io/quickstart/client)

## Exemplos

- [Calculadora em Java](../samples/java/calculator/README.md)
- [Calculadora em .NET](../../../../03-GettingStarted/samples/csharp)
- [Calculadora em JavaScript](../samples/javascript/README.md)
- [Calculadora em TypeScript](../samples/typescript/README.md)
- [Calculadora em Python](../../../../03-GettingStarted/samples/python)
- [Calculadora em Rust](../../../../03-GettingStarted/samples/rust)

## O que Vem a Seguir

- Próximo: [Criando um cliente com um LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->