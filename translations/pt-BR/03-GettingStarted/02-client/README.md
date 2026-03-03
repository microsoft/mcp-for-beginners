# Criando um cliente

Clientes são aplicações ou scripts personalizados que se comunicam diretamente com um Servidor MCP para solicitar recursos, ferramentas e prompts. Diferente de usar a ferramenta de inspetor, que fornece uma interface gráfica para interagir com o servidor, escrever seu próprio cliente permite interações programáticas e automatizadas. Isso possibilita aos desenvolvedores integrar capacidades do MCP em seus próprios fluxos de trabalho, automatizar tarefas e construir soluções personalizadas adaptadas a necessidades específicas.

## Visão geral

Esta lição introduz o conceito de clientes dentro do ecossistema do Protocolo de Contexto de Modelo (MCP). Você aprenderá como escrever seu próprio cliente e conectá-lo a um Servidor MCP.

## Objetivos de aprendizagem

Ao final desta lição, você será capaz de:

- Entender o que um cliente pode fazer.
- Escrever seu próprio cliente.
- Conectar e testar o cliente com um servidor MCP para garantir que ele funciona como esperado.

## O que envolve escrever um cliente?

Para escrever um cliente, você precisará fazer o seguinte:

- **Importar as bibliotecas corretas**. Você usará a mesma biblioteca de antes, apenas com diferentes construções.
- **Instanciar um cliente**. Isso envolverá criar uma instância do cliente e conectá-la ao método de transporte escolhido.
- **Decidir quais recursos listar**. Seu servidor MCP vem com recursos, ferramentas e prompts; você precisa decidir qual listar.
- **Integrar o cliente a uma aplicação host**. Uma vez que você conhece as capacidades do servidor, precisa integrar isso à sua aplicação host para que, quando um usuário digitar um prompt ou outro comando, o recurso correspondente do servidor seja acionado.

Agora que entendemos em alto nível o que vamos fazer, vamos ver um exemplo a seguir.

### Um cliente de exemplo

Vamos dar uma olhada neste cliente de exemplo:

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
- Criamos uma instância de um cliente e conectamos usando stdio como transporte.
- Listamos prompts, recursos e ferramentas e invocamos todos eles.

E aqui está, um cliente que pode se comunicar com um Servidor MCP.

Vamos dedicar tempo na próxima seção de exercícios para analisar cada trecho de código e explicar o que está acontecendo.

## Exercício: Escrevendo um cliente

Como dito acima, vamos com calma explicando o código, e fique à vontade para codificar junto se quiser.

### -1- Importar as bibliotecas

Vamos importar as bibliotecas necessárias, precisaremos de referências a um cliente e ao protocolo de transporte escolhido, stdio. stdio é um protocolo para coisas que devem rodar na sua máquina local. SSE é outro protocolo de transporte que mostraremos em capítulos futuros, mas essa é sua outra opção. Por enquanto, vamos continuar com stdio.

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

Para Java, você criará um cliente que conecta ao servidor MCP do exercício anterior. Usando a mesma estrutura do projeto Java Spring Boot de [Introdução ao Servidor MCP](../../../../03-GettingStarted/01-first-server/solution/java), crie uma nova classe Java chamada `SDKClient` na pasta `src/main/java/com/microsoft/mcp/sample/client/` e adicione os seguintes imports:

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

Você precisará adicionar as seguintes dependências em seu arquivo `Cargo.toml`.

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

Vamos avançar para a instanciação.

### -2- Instanciando cliente e transporte

Precisamos criar uma instância do transporte e do nosso cliente:

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

- Criamos uma instância do transporte stdio. Note como especifica o comando e argumentos para encontrar e iniciar o servidor, pois isso será necessário ao criarmos o cliente.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instanciamos um cliente dando um nome e versão.

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

# Criar parâmetros de servidor para conexão stdio
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

No código anterior nós:

- Importamos as bibliotecas necessárias
- Instanciamos um objeto com parâmetros do servidor, que usaremos para rodar o servidor e assim conectar o cliente.
- Definimos um método `run` que por sua vez chama `stdio_client` que inicia uma sessão do cliente.
- Criamos um ponto de entrada onde passamos o método `run` para `asyncio.run`.

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

- Importamos as bibliotecas necessárias.
- Criamos um transporte stdio e um cliente `mcpClient`. Este será usado para listar e invocar recursos no Servidor MCP.

Nota: em "Arguments", você pode indicar o arquivo *.csproj* ou o executável.

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

- Criamos um método main que configura um transporte SSE apontando para `http://localhost:8080` onde nosso servidor MCP estará rodando.
- Criamos uma classe cliente que recebe o transporte como parâmetro no construtor.
- No método `run`, criamos um cliente MCP síncrono usando o transporte e inicializamos a conexão.
- Usamos o transporte SSE (Server-Sent Events), adequado para comunicação HTTP com servidores MCP Spring Boot Java.

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

    // TODO: Chamar a ferramenta add com argumentos = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Listando as funcionalidades do servidor

Agora temos um cliente que pode se conectar caso o programa seja executado. Contudo, ele ainda não lista suas funcionalidades, então vamos fazer isso a seguir:

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

Aqui listamos os recursos disponíveis, `list_resources()` e ferramentas, `list_tools` e os imprimimos.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Acima está um exemplo de como listar as ferramentas no servidor. Para cada ferramenta, imprimimos seu nome.

#### Java

```java
// Listar e demonstrar ferramentas
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Você também pode usar ping no servidor para verificar a conexão
client.ping();
```

No código acima nós:

- Chamamos `listTools()` para obter todas as ferramentas disponíveis do servidor MCP.
- Usamos `ping()` para verificar se a conexão com o servidor está funcionando.
- O `ListToolsResult` contém informações sobre todas as ferramentas, incluindo seus nomes, descrições e esquemas de entrada.

Ótimo, agora capturamos todas as funcionalidades. Agora, quando as usamos? Bem, este cliente é bem simples, simples no sentido de que precisaremos chamar explicitamente as funcionalidades quando quisermos. No próximo capítulo, criaremos um cliente mais avançado que tem acesso a seu próprio modelo de linguagem grande, LLM. Por enquanto, vamos ver como invocar as funcionalidades no servidor:

#### Rust

Na função main, após inicializar o cliente, podemos inicializar o servidor e listar algumas funcionalidades dele.

```rust
// Inicializar
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Listar ferramentas
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocando funcionalidades

Para invocar as funcionalidades precisamos garantir que especificamos os argumentos corretos e, em alguns casos, o nome do que estamos tentando invocar.

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

- Lemos um recurso, chamamos o recurso usando `readResource()` especificando o `uri`. Veja como isso provavelmente é no lado do servidor:

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

- Chamamos uma ferramenta, chamamos especificando seu `name` e seus `arguments` assim:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Obtemos um prompt, para obter um prompt, você chama `getPrompt()` com `name` e `arguments`. O código do servidor é assim:

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

    e o código do cliente resultante fica assim para corresponder ao declarado no servidor:

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

No código acima nós:

- Chamamos um recurso chamado `greeting` usando `read_resource`.
- Invocamos uma ferramenta chamada `add` usando `call_tool`.

#### .NET

1. Vamos adicionar código para chamar uma ferramenta:

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

- Chamamos múltiplas ferramentas de calculadora usando o método `callTool()` com objetos `CallToolRequest`.
- Cada chamada especifica o nome da ferramenta e um `Map` de argumentos requeridos.
- As ferramentas do servidor esperam nomes específicos de parâmetros (como "a", "b" para operações matemáticas).
- Os resultados retornam em objetos `CallToolResult` contendo a resposta do servidor.

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

### -5- Executando o cliente

Para executar o cliente, digite o seguinte comando no terminal:

#### TypeScript

Adicione a seguinte entrada na seção "scripts" do seu *package.json*:

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

Primeiro, certifique-se de que seu servidor MCP está rodando em `http://localhost:8080`. Em seguida, execute o cliente:

```bash
# Compile seu projeto
./mvnw clean compile

# Execute o cliente
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativamente, você pode executar o projeto cliente completo fornecido na pasta de solução `03-GettingStarted\02-client\solution\java`:

```bash
# Navegar até o diretório da solução
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

Nesta tarefa, você usará o que aprendeu para criar um cliente, mas crie um cliente por conta própria.

Aqui está um servidor que você pode usar e que precisa chamar via seu código cliente, veja se consegue adicionar mais funcionalidades ao servidor para torná-lo mais interessante.

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


# Adicionar um recurso de saudação dinâmica
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

Veja este projeto para aprender como [adicionar prompts e recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Também, confira este link para aprender como invocar [prompts e recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Na [seção anterior](../../../../03-GettingStarted/01-first-server), você aprendeu como criar um servidor MCP simples com Rust. Você pode continuar a construir a partir disso ou conferir este link para mais exemplos de servidores MCP baseados em Rust: [Exemplos de Servidor MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solução

A **pasta de solução** contém implementações completas e prontas para executar de clientes que demonstram todos os conceitos abordados neste tutorial. Cada solução inclui código do cliente e do servidor organizados em projetos separados e independentes.

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

Cada solução específica de linguagem fornece:

- **Implementação completa do cliente** com todos os recursos do tutorial
- **Estrutura do projeto funcional** com dependências e configurações adequadas
- **Scripts para construção e execução** para fácil configuração e uso
- **README detalhado** com instruções específicas da linguagem
- **Exemplos de tratamento de erros** e processamento de resultados

### 📖 Usando as Soluções

1. **Navegue para a pasta da linguagem preferida**:

   ```bash
   cd solution/typescript/    # Para TypeScript
   cd solution/java/          # Para Java
   cd solution/python/        # Para Python
   cd solution/dotnet/        # Para .NET
   ```

2. **Siga as instruções do README em cada pasta para:**
   - Instalar dependências
   - Construir o projeto
   - Executar o cliente

3. **Saída de exemplo** que você deve ver:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para documentação completa e instruções passo a passo, veja: **[📖 Documentação da Solução](./solution/README.md)**

## 🎯 Exemplos Completos

Fornecemos implementações completas e funcionais de clientes para todas as linguagens de programação abordadas neste tutorial. Esses exemplos demonstram a funcionalidade completa descrita acima e podem ser usados como referência ou ponto de partida para seus próprios projetos.

### Exemplos Completos Disponíveis

| Linguagem | Arquivo | Descrição |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Cliente Java completo usando transporte SSE com tratamento abrangente de erros |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Cliente C# completo usando transporte stdio com inicialização automática do servidor |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Cliente TypeScript completo com suporte integral ao protocolo MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Cliente Python completo usando padrões async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Cliente Rust completo usando Tokio para operações assíncronas |

Cada exemplo completo inclui:
- ✅ **Estabelecimento de conexão** e tratamento de erros  
- ✅ **Descoberta do servidor** (ferramentas, recursos, prompts quando aplicável)  
- ✅ **Operações da calculadora** (adicionar, subtrair, multiplicar, dividir, ajuda)  
- ✅ **Processamento de resultados** e saída formatada  
- ✅ **Tratamento abrangente de erros**  
- ✅ **Código limpo e documentado** com comentários passo a passo  

### Começando com Exemplos Completos

1. **Escolha sua linguagem preferida** na tabela acima  
2. **Revise o arquivo de exemplo completo** para entender a implementação total  
3. **Execute o exemplo** seguindo as instruções em [`complete_examples.md`](./complete_examples.md)  
4. **Modifique e estenda** o exemplo para seu caso de uso específico  

Para documentação detalhada sobre execução e customização desses exemplos, veja: **[📖 Documentação de Exemplos Completos](./complete_examples.md)**  

### 💡 Solução vs. Exemplos Completos

| **Pasta da Solução**          | **Exemplos Completos**  |
|------------------------------|------------------------|
| Estrutura completa do projeto com arquivos de build | Implementações em arquivo único |
| Pronto para rodar com dependências   | Exemplos focados de código |
| Configuração semelhante a produção | Referência educacional |
| Ferramentas específicas por linguagem | Comparação entre linguagens |

Ambas as abordagens são valiosas – use a **pasta da solução** para projetos completos e os **exemplos completos** para aprendizado e referência.  

## Principais Lições

Os pontos principais deste capítulo sobre clientes são:

- Podem ser usados tanto para descobrir quanto para invocar funcionalidades no servidor.  
- Podem iniciar um servidor enquanto eles mesmos iniciam (como neste capítulo), mas os clientes também podem se conectar a servidores em execução.  
- São uma ótima maneira de testar as capacidades do servidor ao lado de alternativas como o Inspector, conforme descrito no capítulo anterior.  

## Recursos Adicionais

- [Construindo clientes no MCP](https://modelcontextprotocol.io/quickstart/client)  

## Exemplos

- [Calculadora Java](../samples/java/calculator/README.md)  
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)  
- [Calculadora JavaScript](../samples/javascript/README.md)  
- [Calculadora TypeScript](../samples/typescript/README.md)  
- [Calculadora Python](../../../../03-GettingStarted/samples/python)  
- [Calculadora Rust](../../../../03-GettingStarted/samples/rust)  

## Próximos Passos

- Próximo: [Criando um cliente com um LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora busquemos precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->