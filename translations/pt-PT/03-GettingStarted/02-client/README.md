# Criar um cliente

Os clientes são aplicações personalizadas ou scripts que comunicam diretamente com um Servidor MCP para solicitar recursos, ferramentas e prompts. Ao contrário de usar a ferramenta de inspeção, que fornece uma interface gráfica para interagir com o servidor, escrever o seu próprio cliente permite interações programáticas e automatizadas. Isto permite aos desenvolvedores integrar capacidades MCP nos seus próprios fluxos de trabalho, automatizar tarefas e construir soluções personalizadas adaptadas a necessidades específicas.

## Visão geral

Esta lição apresenta o conceito de clientes dentro do ecossistema do Protocolo de Contexto de Modelo (MCP). Aprenderá como escrever o seu próprio cliente e fazê-lo conectar a um Servidor MCP.

## Objetivos de aprendizagem

Até ao final desta lição, será capaz de:

- Compreender o que um cliente pode fazer.
- Escrever o seu próprio cliente.
- Conectar e testar o cliente com um servidor MCP para garantir que este funciona como esperado.

## O que envolve escrever um cliente?

Para escrever um cliente, precisará de fazer o seguinte:

- **Importar as bibliotecas corretas**. Usará a mesma biblioteca que antes, apenas diferentes construtos.
- **Instanciar um cliente**. Isto envolverá criar uma instância do cliente e conectá-la ao método de transporte escolhido.
- **Decidir quais recursos listar**. O seu servidor MCP vem com recursos, ferramentas e prompts, terá de decidir quais listar.
- **Integrar o cliente numa aplicação hospedeira**. Depois de conhecer as capacidades do servidor, precisará integrar isto na sua aplicação hospedeira para que, se um utilizador escrever um prompt ou outro comando, a funcionalidade correspondente do servidor seja invocada.

Agora que compreendemos, a nível geral, o que vamos fazer, vejamos um exemplo a seguir.

### Um exemplo de cliente

Vamos ver este exemplo de cliente:

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

No código anterior nós:

- Importámos as bibliotecas
- Criámos uma instância de um cliente e conectámo-lo usando stdio como transporte.
- Listámos prompts, recursos e ferramentas e invocámo-los todos.

Aqui está, um cliente que pode comunicar com um Servidor MCP.

Vamos demorar o nosso tempo na próxima secção de exercício para analisar cada excerto de código e explicar o que se passa.

## Exercício: Escrever um cliente

Como mencionado acima, vamos demorar o nosso tempo a explicar o código e, por todos os meios, codifique junto se quiser.

### -1- Importar as bibliotecas

Vamos importar as bibliotecas de que precisamos; precisamos de referências a um cliente e ao protocolo de transporte escolhido, stdio. O stdio é um protocolo para coisas destinadas a correr na sua máquina local. SSE é outro protocolo de transporte que mostraremos em capítulos futuros, mas essa é a sua outra opção. Por agora, continuemos com stdio.

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

Para Java, criará um cliente que se conecta ao servidor MCP do exercício anterior. Usando a mesma estrutura de projeto Java Spring Boot do [Início com o Servidor MCP](../../../../03-GettingStarted/01-first-server/solution/java), crie uma nova classe Java chamada `SDKClient` na pasta `src/main/java/com/microsoft/mcp/sample/client/` e adicione as seguintes importações:

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

Vai precisar de adicionar as seguintes dependências ao seu ficheiro `Cargo.toml`.

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

Depois disso, pode importar as bibliotecas necessárias no seu código cliente.

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

### -2- Instanciar cliente e transporte

Precisamos de criar uma instância do transporte e outra do nosso cliente:

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

No código anterior nós:

- Criámos uma instância do transporte stdio. Note como especifica comando e argumentos para como encontrar e iniciar o servidor, pois isso é algo que teremos de fazer ao criar o cliente.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instanciámos um cliente dando-lhe um nome e versão.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Conectámos o cliente ao transporte escolhido.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Criar parâmetros do servidor para ligação stdio
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
            # Inicializar a ligação
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

No código anterior nós:

- Importámos as bibliotecas necessárias
- Instanciámos um objeto de parâmetros do servidor pois o usaremos para correr o servidor para podermos conectar com o nosso cliente.
- Definimos um método `run` que, por sua vez, chama `stdio_client` que inicia uma sessão cliente.
- Criámos um ponto de entrada onde fornecemos o método `run` a `asyncio.run`.

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

No código anterior nós:

- Importámos as bibliotecas necessárias.
- Criámos um transporte stdio e um cliente `mcpClient`. Este último será utilizado para listar e invocar funcionalidades no Servidor MCP.

Note que, em "Argumentos", pode apontar para o *.csproj* ou para o executável.

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
        
        // A lógica do seu cliente vai aqui
    }
}
```

No código anterior nós:

- Criámos um método main que configura um transporte SSE apontando para `http://localhost:8080` onde o nosso servidor MCP estará a correr.
- Criámos uma classe cliente que recebe o transporte como parâmetro do construtor.
- No método `run`, criamos um cliente MCP síncrono usando o transporte e inicializamos a ligação.
- Usámos o transporte SSE (Server-Sent Events) que é adequado para comunicação HTTP com servidores MCP Java Spring Boot.

#### Rust

Note que este cliente Rust presume que o servidor é um projeto irmão chamado "calculator-server" no mesmo diretório. O código abaixo irá iniciar o servidor e conectar-se a ele.

```rust
async fn main() -> Result<(), RmcpError> {
    // Suponha que o servidor seja um projeto irmão chamado "calculator-server" no mesmo diretório
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

    // TODO: Chamar a ferramenta add com argumentos = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Listar as funcionalidades do servidor

Agora, temos um cliente que pode conectar-se caso o programa seja executado. No entanto, ele não lista realmente as suas funcionalidades, por isso façamo-lo a seguir:

#### TypeScript

```typescript
// Lista de prompts
const prompts = await client.listPrompts();

// Lista de recursos
const resources = await client.listResources();

// lista de ferramentas
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

Aqui listamos os recursos disponíveis, `list_resources()`, e ferramentas, `list_tools`, e imprimimo-los.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Em cima está um exemplo de como podemos listar as ferramentas no servidor. Para cada ferramenta, imprimimos o seu nome.

#### Java

```java
// Listar e demonstrar ferramentas
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Também pode fazer ping ao servidor para verificar a ligação
client.ping();
```

No código anterior nós:

- Chamámos `listTools()` para obter todas as ferramentas disponíveis do servidor MCP.
- Usámos `ping()` para verificar que a ligação ao servidor está a funcionar.
- O `ListToolsResult` contém informação sobre todas as ferramentas, incluindo nomes, descrições e esquemas de entrada.

Excelente, agora capturámos todas as funcionalidades. A questão agora é quando as usamos? Bem, este cliente é bastante simples, simples no sentido em que precisaremos de chamar explicitamente as funcionalidades quando as quisermos. No próximo capítulo, criaremos um cliente mais avançado que terá acesso ao seu próprio modelo de linguagem grande, LLM. Por agora, vamos ver como podemos invocar as funcionalidades no servidor:

#### Rust

Na função main, depois de inicializar o cliente, podemos inicializar o servidor e listar algumas das suas funcionalidades.

```rust
// Inicializar
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Listar ferramentas
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocar funcionalidades

Para invocar as funcionalidades, precisamos garantir que especificamos os argumentos corretos e, em alguns casos, o nome do que estamos a tentar invocar.

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

No código anterior nós:

- Lemos um recurso, chamamos o recurso usando `readResource()` especificando `uri`. Eis como provavelmente se parece do lado do servidor:

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

    O valor `uri` `file://example.txt` corresponde a `file://{name}` no servidor. `example.txt` será mapeado para `name`.

- Chamamos uma ferramenta especificando o seu `name` e os seus `arguments` assim:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Obtemos um prompt, para obter um prompt, chamamos `getPrompt()` com `name` e `arguments`. O código do servidor é o seguinte:

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

    e o código resultante do cliente é, portanto, assim para corresponder ao declarado no servidor:

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

No código anterior nós:

- Chamámos um recurso chamado `greeting` usando `read_resource`.
- Invocámos uma ferramenta chamada `add` usando `call_tool`.

#### .NET

1. Vamos adicionar algum código para chamar uma ferramenta:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Para imprimir o resultado, aqui está algum código para tratar disso:

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

No código anterior nós:

- Chamámos múltiplas ferramentas de calculadora usando o método `callTool()` com objetos `CallToolRequest`.
- Cada chamada de ferramenta especifica o nome da ferramenta e um `Map` de argumentos requeridos pela ferramenta.
- As ferramentas do servidor esperam nomes de parâmetros específicos (como "a", "b" para operações matemáticas).
- Os resultados são retornados como objetos `CallToolResult` contendo a resposta do servidor.

#### Rust

```rust
// Chamar a ferramenta add com argumentos = {"a": 3, "b": 2}
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

Adicione a seguinte entrada à sua secção "scripts" no *package.json*:

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

Primeiro, assegure-se de que o seu servidor MCP está a correr em `http://localhost:8080`. Depois execute o cliente:

```bash
# Construa o seu projeto
./mvnw clean compile

# Execute o cliente
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativamente, pode executar o projeto completo do cliente fornecido na pasta de solução `03-GettingStarted\02-client\solution\java`:

```bash
# Navegar para o diretório da solução
cd 03-GettingStarted/02-client/solution/java

# Construir e executar o JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Tarefa

Nesta tarefa, usará o que aprendeu a criar um cliente, mas crie um cliente próprio.

Aqui está um servidor que pode usar para chamar via o seu código cliente; veja se consegue adicionar mais funcionalidades ao servidor para o tornar mais interessante.

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

// Começar a receber mensagens no stdin e a enviar mensagens no stdout

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

Veja este projeto para ver como pode [adicionar prompts e recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Também, consulte este link para saber como invocar [prompts e recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Na [secção anterior](../../../../03-GettingStarted/01-first-server), aprendeu a criar um servidor MCP simples com Rust. Pode continuar a desenvolver essa base ou consultar este link para mais exemplos de servidores MCP baseados em Rust: [Exemplos de Servidor MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solução

A **pasta da solução** contém implementações completas e prontas a executar de clientes que demonstram todos os conceitos abordados neste tutorial. Cada solução inclui código tanto do cliente quanto do servidor organizado em projetos separados e autónomos.

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

Cada solução específica da linguagem fornece:

- **Implementação completa do cliente** com todas as funcionalidades do tutorial
- **Estrutura de projeto funcional** com as dependências e configurações adequadas
- **Scripts de construção e execução** para fácil configuração e execução
- **README detalhado** com instruções específicas por linguagem
- **Exemplos de tratamento de erros** e processamento de resultados

### 📖 Usando as Soluções

1. **Navegue até à pasta da linguagem preferida**:

   ```bash
   cd solution/typescript/    # Para TypeScript
   cd solution/java/          # Para Java
   cd solution/python/        # Para Python
   cd solution/dotnet/        # Para .NET
   ```

2. **Siga as instruções do README** em cada pasta para:
   - Instalar dependências
   - Construir o projeto
   - Executar o cliente

3. **Saída de exemplo** que deverá ver:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para documentação completa e instruções passo a passo, consulte: **[📖 Documentação da Solução](./solution/README.md)**

## 🎯 Exemplos Completos

Fornecemos implementações completas e funcionais de clientes para todas as linguagens de programação abordadas neste tutorial. Estes exemplos demonstram a funcionalidade completa descrita acima e podem ser usados como implementações de referência ou como pontos de partida para os seus próprios projetos.

### Exemplos Completos Disponíveis

| Linguagem | Ficheiro | Descrição |
|----------|----------|-----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Cliente Java completo usando transporte SSE com tratamento abrangente de erros |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Cliente C# completo usando transporte stdio com arranque automático do servidor |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Cliente TypeScript completo com suporte total ao protocolo MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Cliente Python completo usando padrões async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Cliente Rust completo usando Tokio para operações assíncronas |

Cada exemplo completo inclui:

- ✅ **Estabelecimento da ligação** e tratamento de erros
- ✅ **Descoberta do servidor** (ferramentas, recursos, prompts onde aplicável)
- ✅ **Operações da calculadora** (adicionar, subtrair, multiplicar, dividir, ajuda)
- ✅ **Processamento de resultados** e saída formatada
- ✅ **Tratamento de erros abrangente**

- ✅ **Código limpo e documentado** com comentários passo a passo

### Começar com Exemplos Completos

1. **Escolha a sua linguagem preferida** na tabela acima
2. **Reveja o ficheiro de exemplo completo** para compreender a implementação total
3. **Execute o exemplo** seguindo as instruções em [`complete_examples.md`](./complete_examples.md)
4. **Modifique e amplie** o exemplo para o seu caso específico

Para documentação detalhada sobre como executar e personalizar estes exemplos, veja: **[📖 Documentação dos Exemplos Completos](./complete_examples.md)**

### 💡 Solução vs. Exemplos Completos

| **Pasta da Solução** | **Exemplos Completos** |
|--------------------|--------------------- |
| Estrutura completa do projeto com ficheiros de compilação | Implementações em ficheiro único |
| Pronto a executar com dependências | Exemplos de código focados |
| Configuração semelhante à produção | Referência educativa |
| Ferramentas específicas para a linguagem | Comparação entre linguagens |

Ambas as abordagens são valiosas - use a **pasta da solução** para projetos completos e os **exemplos completos** para aprendizagem e referência.

## Principais Conclusões

As principais conclusões deste capítulo sobre clientes são as seguintes:

- Podem ser usados tanto para descobrir como invocar funcionalidades no servidor.
- Podem iniciar um servidor enquanto este próprio inicia (como neste capítulo), mas os clientes podem também conectar a servidores em execução.
- São uma excelente forma de testar capacidades do servidor, ao lado de alternativas como o Inspector, conforme descrito no capítulo anterior.

## Recursos Adicionais

- [Construção de clientes em MCP](https://modelcontextprotocol.io/quickstart/client)

## Exemplos

- [Calculadora Java](../samples/java/calculator/README.md)
- [Calculadora .NET](../../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](../samples/javascript/README.md)
- [Calculadora TypeScript](../samples/typescript/README.md)
- [Calculadora Python](../../../../03-GettingStarted/samples/python)
- [Calculadora Rust](../../../../03-GettingStarted/samples/rust)

## O Que Vem a Seguir

- Seguir: [Criar um cliente com um LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->