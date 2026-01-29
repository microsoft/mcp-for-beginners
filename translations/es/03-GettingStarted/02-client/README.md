# Creando un cliente

Los clientes son aplicaciones o scripts personalizados que se comunican directamente con un servidor MCP para solicitar recursos, herramientas y prompts. A diferencia de usar la herramienta de inspección, que proporciona una interfaz gráfica para interactuar con el servidor, escribir tu propio cliente permite interacciones programáticas y automatizadas. Esto permite a los desarrolladores integrar las capacidades de MCP en sus propios flujos de trabajo, automatizar tareas y construir soluciones personalizadas adaptadas a necesidades específicas.

## Descripción general

Esta lección introduce el concepto de clientes dentro del ecosistema del Protocolo de Contexto de Modelo (MCP). Aprenderás a escribir tu propio cliente y conectarlo a un servidor MCP.

## Objetivos de aprendizaje

Al final de esta lección, serás capaz de:

- Comprender qué puede hacer un cliente.
- Escribir tu propio cliente.
- Conectar y probar el cliente con un servidor MCP para asegurarte de que este funcione como se espera.

## ¿Qué implica escribir un cliente?

Para escribir un cliente, necesitarás hacer lo siguiente:

- **Importar las bibliotecas correctas**. Usarás la misma biblioteca que antes, solo que con diferentes constructos.
- **Instanciar un cliente**. Esto implicará crear una instancia de cliente y conectarla al método de transporte elegido.
- **Decidir qué recursos listar**. Tu servidor MCP incluye recursos, herramientas y prompts; necesitas decidir cuáles listar.
- **Integrar el cliente en una aplicación anfitriona**. Una vez que conozcas las capacidades del servidor, necesitas integrarlo en tu aplicación anfitriona para que, si un usuario escribe un prompt u otro comando, se invoque la funcionalidad correspondiente del servidor.

Ahora que entendemos a alto nivel lo que vamos a hacer, veamos un ejemplo a continuación.

### Un ejemplo de cliente

Echemos un vistazo a este ejemplo de cliente:

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

En el código anterior:

- Importamos las bibliotecas.
- Creamos una instancia de un cliente y la conectamos usando stdio como transporte.
- Listamos prompts, recursos y herramientas, e invocamos todos ellos.

Ahí lo tienes, un cliente que puede comunicarse con un servidor MCP.

Tomémonos nuestro tiempo en la siguiente sección de ejercicios para desglosar cada fragmento de código y explicar qué está sucediendo.

## Ejercicio: Escribiendo un cliente

Como se mencionó anteriormente, tomémonos nuestro tiempo explicando el código, y si lo deseas, sigue el código mientras avanzamos.

### -1- Importar las bibliotecas

Importemos las bibliotecas que necesitamos. Necesitaremos referencias a un cliente y a nuestro protocolo de transporte elegido, stdio. stdio es un protocolo para cosas que se ejecutan en tu máquina local. SSE es otro protocolo de transporte que mostraremos en capítulos futuros, pero esa es tu otra opción. Por ahora, continuemos con stdio.

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

Para Java, crearás un cliente que se conecte al servidor MCP del ejercicio anterior. Usando la misma estructura de proyecto Java Spring Boot de [Primeros pasos con el servidor MCP](../../../../03-GettingStarted/01-first-server/solution/java), crea una nueva clase Java llamada `SDKClient` en la carpeta `src/main/java/com/microsoft/mcp/sample/client/` y agrega las siguientes importaciones:

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

Necesitarás agregar las siguientes dependencias a tu archivo `Cargo.toml`.

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

Desde allí, puedes importar las bibliotecas necesarias en tu código de cliente.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Pasemos a la instanciación.

### -2- Instanciar cliente y transporte

Necesitaremos crear una instancia del transporte y otra de nuestro cliente:

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

En el código anterior:

- Creamos una instancia de transporte stdio. Nota cómo especifica el comando y los argumentos para encontrar e iniciar el servidor, ya que eso es algo que necesitaremos hacer al crear el cliente.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instanciamos un cliente dándole un nombre y una versión.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Conectamos el cliente al transporte elegido.

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

En el código anterior:

- Importamos las bibliotecas necesarias.
- Instanciamos un objeto de parámetros del servidor, ya que lo usaremos para ejecutar el servidor y conectarnos a él con nuestro cliente.
- Definimos un método `run` que a su vez llama a `stdio_client`, el cual inicia una sesión de cliente.
- Creamos un punto de entrada donde proporcionamos el método `run` a `asyncio.run`.

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

En el código anterior:

- Importamos las bibliotecas necesarias.
- Creamos un transporte stdio y un cliente `mcpClient`. Este último lo usaremos para listar e invocar características en el servidor MCP.

Nota: en "Arguments", puedes apuntar al archivo *.csproj* o al ejecutable.

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

En el código anterior:

- Creamos un método principal que configura un transporte SSE apuntando a `http://localhost:8080`, donde estará ejecutándose nuestro servidor MCP.
- Creamos una clase cliente que toma el transporte como parámetro del constructor.
- En el método `run`, creamos un cliente MCP síncrono usando el transporte e inicializamos la conexión.
- Usamos el transporte SSE (Eventos Enviados por el Servidor), que es adecuado para la comunicación basada en HTTP con servidores MCP de Java Spring Boot.

#### Rust

Este cliente Rust asume que el servidor es un proyecto hermano llamado "calculator-server" en el mismo directorio. El código a continuación iniciará el servidor y se conectará a él.

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

### -3- Listar las características del servidor

Ahora tenemos un cliente que puede conectarse si se ejecuta el programa. Sin embargo, no lista sus características, así que hagámoslo a continuación:

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

Aquí listamos los recursos disponibles con `list_resources()` y las herramientas con `list_tools`, y los imprimimos.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Arriba hay un ejemplo de cómo podemos listar las herramientas en el servidor. Para cada herramienta, imprimimos su nombre.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

En el código anterior:

- Llamamos a `listTools()` para obtener todas las herramientas disponibles del servidor MCP.
- Usamos `ping()` para verificar que la conexión con el servidor funciona.
- `ListToolsResult` contiene información sobre todas las herramientas, incluidos sus nombres, descripciones y esquemas de entrada.

Genial, ahora hemos capturado todas las características. La pregunta es, ¿cuándo las usamos? Bueno, este cliente es bastante simple, en el sentido de que necesitaremos llamar explícitamente a las características cuando las queramos. En el próximo capítulo, crearemos un cliente más avanzado que tenga acceso a su propio modelo de lenguaje grande (LLM). Por ahora, veamos cómo podemos invocar las características en el servidor:

#### Rust

En la función principal, después de inicializar el cliente, podemos inicializar el servidor y listar algunas de sus características.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocar características

Para invocar las características, necesitamos asegurarnos de especificar los argumentos correctos y, en algunos casos, el nombre de lo que estamos intentando invocar.

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

En el código anterior:

- Leemos un recurso llamando a `readResource()` y especificando `uri`. Así es como probablemente se verá del lado del servidor:

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

    Nuestro valor `uri` `file://example.txt` coincide con `file://{name}` en el servidor. `example.txt` se asignará a `name`.

- Llamamos a una herramienta especificando su `name` y sus `arguments`, como sigue:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Obtenemos un prompt llamando a `getPrompt()` con `name` y `arguments`. El código del servidor se ve así:

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

    Y tu código de cliente resultante se verá así para coincidir con lo declarado en el servidor:

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

En el código anterior:

- Llamamos a un recurso llamado `greeting` usando `read_resource`.
- Invocamos una herramienta llamada `add` usando `call_tool`.

#### .NET

1. Agreguemos algo de código para llamar a una herramienta:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Para imprimir el resultado, aquí hay un código para manejarlo:

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

En el código anterior:

- Llamamos a múltiples herramientas de cálculo usando el método `callTool()` con objetos `CallToolRequest`.
- Cada llamada a la herramienta especifica el nombre de la herramienta y un `Map` de argumentos requeridos por esa herramienta.
- Las herramientas del servidor esperan nombres de parámetros específicos (como "a", "b" para operaciones matemáticas).
- Los resultados se devuelven como objetos `CallToolResult` que contienen la respuesta del servidor.

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

### -5- Ejecutar el cliente

Para ejecutar el cliente, escribe el siguiente comando en la terminal:

#### TypeScript

Agrega la siguiente entrada a la sección "scripts" en *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Llama al cliente con el siguiente comando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Primero, asegúrate de que tu servidor MCP esté ejecutándose en `http://localhost:8080`. Luego ejecuta el cliente:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativamente, puedes ejecutar el proyecto completo del cliente proporcionado en la carpeta de solución `03-GettingStarted\02-client\solution\java`:

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

## Tarea

En esta tarea, usarás lo que has aprendido para crear un cliente propio.

Aquí tienes un servidor que puedes usar y al que necesitas llamar desde tu código de cliente. Intenta agregar más características al servidor para hacerlo más interesante.

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

Consulta este proyecto para ver cómo puedes [agregar prompts y recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Además, revisa este enlace para aprender a invocar [prompts y recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

En la [sección anterior](../../../../03-GettingStarted/01-first-server), aprendiste a crear un servidor MCP simple con Rust. Puedes continuar construyendo sobre eso o consultar este enlace para más ejemplos de servidores MCP basados en Rust: [Ejemplos de servidores MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solución

La **carpeta de solución** contiene implementaciones completas y listas para ejecutar de clientes que demuestran todos los conceptos cubiertos en este tutorial. Cada solución incluye código tanto del cliente como del servidor organizados en proyectos separados y autónomos.

### 📁 Estructura de la solución

El directorio de solución está organizado por lenguaje de programación:

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

### 🚀 Qué incluye cada solución

Cada solución específica de lenguaje proporciona:

- **Implementación completa del cliente** con todas las características del tutorial.
- **Estructura de proyecto funcional** con dependencias y configuración adecuadas.
- **Scripts de construcción y ejecución** para una configuración y ejecución fáciles.
- **README detallado** con instrucciones específicas del lenguaje.
- **Ejemplos de manejo de errores** y procesamiento de resultados.

### 📖 Usando las soluciones

1. **Navega a la carpeta de tu lenguaje preferido**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Sigue las instrucciones del README** en cada carpeta para:
   - Instalar dependencias.
   - Construir el proyecto.
   - Ejecutar el cliente.

3. **Ejemplo de salida** que deberías ver:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para documentación completa e instrucciones paso a paso, consulta: **[📖 Documentación de la solución](./solution/README.md)**

## 🎯 Ejemplos completos

Hemos proporcionado implementaciones completas y funcionales de clientes para todos los lenguajes de programación cubiertos en este tutorial. Estos ejemplos demuestran toda la funcionalidad descrita anteriormente y pueden usarse como implementaciones de referencia o puntos de partida para tus propios proyectos.

### Ejemplos completos disponibles

| Lenguaje | Archivo | Descripción |
|----------|---------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Cliente Java completo usando transporte SSE con manejo de errores integral |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Cliente C# completo usando transporte stdio con inicio automático del servidor |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Cliente TypeScript completo con soporte completo para el protocolo MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Cliente Python completo usando patrones async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Cliente Rust completo usando Tokio para operaciones asíncronas |
Cada ejemplo completo incluye:

- ✅ **Establecimiento de conexión** y manejo de errores
- ✅ **Descubrimiento del servidor** (herramientas, recursos, indicaciones donde sea aplicable)
- ✅ **Operaciones de calculadora** (sumar, restar, multiplicar, dividir, ayuda)
- ✅ **Procesamiento de resultados** y salida formateada
- ✅ **Manejo integral de errores**
- ✅ **Código limpio y documentado** con comentarios paso a paso

### Comenzando con Ejemplos Completos

1. **Elige tu idioma preferido** de la tabla anterior  
2. **Revisa el archivo de ejemplo completo** para entender la implementación completa  
3. **Ejecuta el ejemplo** siguiendo las instrucciones en [`complete_examples.md`](./complete_examples.md)  
4. **Modifica y amplía** el ejemplo para tu caso de uso específico  

Para documentación detallada sobre cómo ejecutar y personalizar estos ejemplos, consulta: **[📖 Documentación de Ejemplos Completos](./complete_examples.md)**

### 💡 Solución vs. Ejemplos Completos

| **Carpeta de Solución** | **Ejemplos Completos** |
|-------------------------|-----------------------|
| Estructura completa del proyecto con archivos de compilación | Implementaciones en un solo archivo |
| Listo para ejecutar con dependencias | Ejemplos de código enfocados |
| Configuración similar a producción | Referencia educativa |
| Herramientas específicas del lenguaje | Comparación entre lenguajes |

Ambos enfoques son valiosos: utiliza la **carpeta de solución** para proyectos completos y los **ejemplos completos** para aprendizaje y referencia.

## Puntos Clave

Los puntos clave de este capítulo sobre los clientes son los siguientes:

- Se pueden usar tanto para descubrir como para invocar funcionalidades en el servidor.  
- Pueden iniciar un servidor mientras se inician ellos mismos (como en este capítulo), pero los clientes también pueden conectarse a servidores en ejecución.  
- Son una excelente manera de probar las capacidades del servidor junto con alternativas como el Inspector, descrito en el capítulo anterior.  

## Recursos Adicionales

- [Construcción de clientes en MCP](https://modelcontextprotocol.io/quickstart/client)

## Ejemplos

- [Calculadora en Java](../samples/java/calculator/README.md)  
- [Calculadora en .Net](../../../../03-GettingStarted/samples/csharp)  
- [Calculadora en JavaScript](../samples/javascript/README.md)  
- [Calculadora en TypeScript](../samples/typescript/README.md)  
- [Calculadora en Python](../../../../03-GettingStarted/samples/python)  
- [Calculadora en Rust](../../../../03-GettingStarted/samples/rust)  

## ¿Qué sigue?

- Siguiente: [Crear un cliente con un LLM](../03-llm-client/README.md)  

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.