# Creando un cliente

Los clientes son aplicaciones o scripts personalizados que se comunican directamente con un Servidor MCP para solicitar recursos, herramientas y avisos. A diferencia de usar la herramienta de inspector, que proporciona una interfaz gráfica para interactuar con el servidor, escribir tu propio cliente permite interacciones programáticas y automatizadas. Esto permite a los desarrolladores integrar las capacidades de MCP en sus propios flujos de trabajo, automatizar tareas y construir soluciones personalizadas adaptadas a necesidades específicas.

## Descripción general

Esta lección introduce el concepto de clientes dentro del ecosistema del Protocolo de Contexto de Modelo (MCP). Aprenderás a escribir tu propio cliente y conectarlo a un Servidor MCP.

## Objetivos de aprendizaje

Al final de esta lección, serás capaz de:

- Entender qué puede hacer un cliente.
- Escribir tu propio cliente.
- Conectar y probar el cliente con un servidor MCP para asegurar que este funciona como se espera.

## ¿Qué implica escribir un cliente?

Para escribir un cliente, necesitarás hacer lo siguiente:

- **Importar las librerías correctas**. Usarás la misma librería que antes, solo con diferentes construcciones.
- **Instanciar un cliente**. Esto implicará crear una instancia de cliente y conectarla al método de transporte elegido.
- **Decidir qué recursos listar**. Tu servidor MCP viene con recursos, herramientas y avisos; necesitas decidir cuáles listar.
- **Integrar el cliente en una aplicación anfitriona**. Una vez que conozcas las capacidades del servidor, debes integrar esto en tu aplicación anfitriona para que si un usuario escribe un aviso u otro comando, se invoque la característica correspondiente del servidor.

Ahora que entendemos a un alto nivel lo que vamos a hacer, veamos un ejemplo a continuación.

### Un cliente de ejemplo

Veamos este cliente de ejemplo:

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

// Listar indicaciones
const prompts = await client.listPrompts();

// Obtener una indicación
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Listar recursos
const resources = await client.listResources();

// Leer un recurso
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Llamar a una herramienta
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

En el código anterior:

- Importamos las librerías
- Creamos una instancia de cliente y la conectamos usando stdio como transporte.
- Listamos avisos, recursos y herramientas e invocamos todos.

Ahí lo tienes, un cliente que puede comunicarse con un Servidor MCP.

Tomémonos nuestro tiempo en la siguiente sección de ejercicios y analicemos cada fragmento de código explicando qué sucede.

## Ejercicio: Escribiendo un cliente

Como se dijo antes, tomemos el tiempo para explicar el código, y por supuesto, programa junto si quieres.

### -1- Importar las librerías

Importemos las librerías necesarias, necesitaremos referencias a un cliente y a nuestro protocolo de transporte elegido, stdio. stdio es un protocolo para cosas que se ejecutan en tu máquina local. SSE es otro protocolo de transporte que mostraremos en capítulos futuros pero esa es tu otra opción. Por ahora, continuemos con stdio.

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

Para Java, crearás un cliente que se conecte al servidor MCP del ejercicio anterior. Usando la misma estructura de proyecto Java Spring Boot de [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), crea una clase Java nueva llamada `SDKClient` en la carpeta `src/main/java/com/microsoft/mcp/sample/client/` y agrega las siguientes importaciones:

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

Después, puedes importar las librerías necesarias en tu código cliente.

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

### -2- Instanciando cliente y transporte

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

En el código anterior hemos:

- Creado una instancia de transporte stdio. Nota cómo especifica el comando y los argumentos para cómo encontrar e iniciar el servidor, ya que eso es algo que necesitaremos hacer al crear el cliente.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instanciado un cliente dándole un nombre y versión.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Conectado el cliente al transporte elegido.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Crear parámetros del servidor para la conexión stdio
server_params = StdioServerParameters(
    command="mcp",  # Ejecutable
    args=["run", "server.py"],  # Argumentos opcionales de línea de comandos
    env=None,  # Variables de entorno opcionales
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializar la conexión
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

En el código anterior hemos:

- Importado las librerías necesarias
- Instanciado un objeto de parámetros para el servidor, ya que lo usaremos para correr el servidor y así poder conectar el cliente.
- Definido un método `run` que a su vez llama a `stdio_client` que inicia una sesión de cliente.
- Creado un punto de entrada donde proveemos el método `run` a `asyncio.run`.

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

En el código anterior hemos:

- Importado las librerías necesarias.
- Creado un transporte stdio y un cliente llamado `mcpClient`. Este último es lo que usaremos para listar e invocar características en el Servidor MCP.

Nota: en "Arguments", puedes apuntar ya sea al *.csproj* o al ejecutable.

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
        
        // La lógica de tu cliente va aquí
    }
}
```

En el código anterior hemos:

- Creado un método principal que configura un transporte SSE apuntando a `http://localhost:8080`, donde estará corriendo nuestro servidor MCP.
- Creado una clase cliente que recibe el transporte como parámetro en su constructor.
- En el método `run`, creamos un cliente MCP síncrono usando el transporte e inicializamos la conexión.
- Usado transporte SSE (Server-Sent Events) que es adecuado para comunicación basada en HTTP con servidores MCP Java Spring Boot.

#### Rust

Nota que este cliente Rust asume que el servidor es un proyecto hermano llamado "calculator-server" en el mismo directorio. El código abajo iniciará el servidor y se conectará a él.

```rust
async fn main() -> Result<(), RmcpError> {
    // Asuma que el servidor es un proyecto hermano llamado "calculator-server" en el mismo directorio
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

    // TODO: Listar herramientas

    // TODO: Llamar a la herramienta add con argumentos = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Listando las características del servidor

Ahora tenemos un cliente que puede conectarse si el programa se ejecuta. Sin embargo, realmente no lista sus características, así que hagámoslo a continuación:

#### TypeScript

```typescript
// Listar indicaciones
const prompts = await client.listPrompts();

// Listar recursos
const resources = await client.listResources();

// listar herramientas
const tools = await client.listTools();
```

#### Python

```python
# Listar recursos disponibles
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Listar herramientas disponibles
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Aquí listamos los recursos disponibles, `list_resources()` y las herramientas, `list_tools`, y los imprimimos.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Arriba hay un ejemplo de cómo listar las herramientas en el servidor. Para cada herramienta, imprimimos su nombre.

#### Java

```java
// Enumerar y demostrar herramientas
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// También puedes hacer ping al servidor para verificar la conexión
client.ping();
```

En el código anterior hemos:

- Llamado a `listTools()` para obtener todas las herramientas disponibles del servidor MCP.
- Usado `ping()` para verificar que la conexión con el servidor funciona.
- El `ListToolsResult` contiene información sobre todas las herramientas incluyendo sus nombres, descripciones y esquemas de entrada.

Genial, ahora hemos capturado todas las características. Ahora la pregunta es, ¿cuándo las usamos? Bueno, este cliente es bastante simple, simple en el sentido de que necesitaremos llamar explícitamente a las características cuando las queramos. En el próximo capítulo, crearemos un cliente más avanzado que tenga acceso a su propio modelo de lenguaje grande, LLM. Por ahora, veamos cómo podemos invocar las características del servidor:

#### Rust

En la función principal, después de inicializar el cliente, podemos iniciar el servidor y listar algunas de sus características.

```rust
// Inicializar
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Listar herramientas
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocar características

Para invocar las características debemos asegurar que especificamos los argumentos correctos y en algunos casos el nombre de lo que queremos invocar.

#### TypeScript

```typescript

// Leer un recurso
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Llamar a una herramienta
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// llamar al prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

En el código anterior:

- Leemos un recurso, llamamos al recurso usando `readResource()` especificando `uri`. Así es como probablemente se vea del lado del servidor:

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

    Nuestro valor `uri` `file://example.txt` coincide con `file://{name}` en el servidor. `example.txt` será mapeado a `name`.

- Llamamos una herramienta, la llamamos especificando su `name` y sus `arguments` así:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Obtener aviso, para obtener un aviso, llamas a `getPrompt()` con `name` y `arguments`. El código del servidor se ve así:

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

    y tu código cliente resultante se ve así para coincidir con lo declarado en el servidor:

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
# Leer un recurso
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Llamar a una herramienta
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

En el código anterior, hemos:

- Llamado un recurso llamado `greeting` usando `read_resource`.
- Invocado una herramienta llamada `add` usando `call_tool`.

#### .NET

1. Añadamos código para llamar una herramienta:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Para imprimir el resultado, aquí hay código para manejar eso:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Llamar a varias herramientas de calculadora
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

En el código anterior hemos:

- Llamado múltiples herramientas de calculadora usando el método `callTool()` con objetos `CallToolRequest`.
- Cada llamada a herramienta especifica el nombre de la herramienta y un `Map` de argumentos requeridos por esa herramienta.
- Las herramientas del servidor esperan nombres específicos de parámetros (como "a", "b" para operaciones matemáticas).
- Los resultados son devueltos como objetos `CallToolResult` que contienen la respuesta del servidor.

#### Rust

```rust
// Llamar a la herramienta add con argumentos = {"a": 3, "b": 2}
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

Añade la siguiente entrada a tu sección "scripts" en *package.json*:

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

Primero, asegúrate de que tu servidor MCP esté corriendo en `http://localhost:8080`. Luego ejecuta el cliente:

```bash
# Construye tu proyecto
./mvnw clean compile

# Ejecuta el cliente
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativamente, puedes ejecutar el proyecto cliente completo provisto en la carpeta solución `03-GettingStarted\02-client\solution\java`:

```bash
# Navegar al directorio de la solución
cd 03-GettingStarted/02-client/solution/java

# Compilar y ejecutar el JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Tarea

En esta tarea, usarás lo que has aprendido para crear un cliente pero crea un cliente propio.

Aquí tienes un servidor que puedes usar y que necesitas llamar a través de tu código cliente, intenta agregar más características al servidor para hacerlo más interesante.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Crear un servidor MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Agregar una herramienta de suma
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Agregar un recurso de saludo dinámico
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

// Comenzar a recibir mensajes en stdin y enviar mensajes en stdout

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

# Crear un servidor MCP
mcp = FastMCP("Demo")


# Agregar una herramienta de suma
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Agregar un recurso de saludo dinámico
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

Consulta este proyecto para ver cómo puedes [añadir avisos y recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Además, revisa este enlace para cómo invocar [avisos y recursos](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

En la [sección anterior](../../../../03-GettingStarted/01-first-server) aprendiste cómo crear un servidor MCP simple con Rust. Puedes continuar construyendo sobre eso o revisar este enlace para más ejemplos de servidores MCP basados en Rust: [Ejemplos de Servidores MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solución

La **carpeta de soluciones** contiene implementaciones completas y listas para ejecutar de clientes que demuestran todos los conceptos cubiertos en este tutorial. Cada solución incluye código tanto de cliente como de servidor organizado en proyectos separados y autónomos.

### 📁 Estructura de la solución

El directorio de la solución está organizado por lenguaje de programación:

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

Cada solución específica de lenguaje provee:

- **Implementación completa del cliente** con todas las características del tutorial
- **Estructura de proyecto funcional** con dependencias y configuración adecuadas
- **Scripts para construir y ejecutar** para configuración y ejecución fáciles
- **README detallado** con instrucciones específicas por lenguaje
- **Manejo de errores** y ejemplos de procesamiento de resultados

### 📖 Uso de las soluciones

1. **Navega a la carpeta de tu lenguaje preferido**:

   ```bash
   cd solution/typescript/    # Para TypeScript
   cd solution/java/          # Para Java
   cd solution/python/        # Para Python
   cd solution/dotnet/        # Para .NET
   ```

2. **Sigue las instrucciones del README** en cada carpeta para:
   - Instalar dependencias
   - Construir el proyecto
   - Ejecutar el cliente

3. **Salida de ejemplo** que deberías ver:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para documentación completa e instrucciones paso a paso, consulta: **[📖 Documentación de la Solución](./solution/README.md)**

## 🎯 Ejemplos completos

Hemos provisto implementaciones completas y funcionales de clientes para todos los lenguajes de programación cubiertos en este tutorial. Estos ejemplos demuestran todas las funcionalidades descritas arriba y pueden usarse como implementaciones de referencia o puntos de partida para tus propios proyectos.

### Ejemplos completos disponibles

| Lenguaje | Archivo | Descripción |
|----------|---------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Cliente Java completo usando transporte SSE con manejo de errores detallado |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Cliente C# completo usando transporte stdio con inicio automático del servidor |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Cliente TypeScript completo con soporte total para protocolo MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Cliente Python completo usando patrones async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Cliente Rust completo usando Tokio para operaciones async |

Cada ejemplo completo incluye:
- ✅ **Establecimiento de conexión** y manejo de errores  
- ✅ **Descubrimiento del servidor** (herramientas, recursos, indicaciones donde aplique)  
- ✅ **Operaciones de calculadora** (sumar, restar, multiplicar, dividir, ayuda)  
- ✅ **Procesamiento de resultados** y salida formateada  
- ✅ **Manejo exhaustivo de errores**  
- ✅ **Código limpio y documentado** con comentarios paso a paso  

### Primeros pasos con ejemplos completos

1. **Elige tu lenguaje preferido** de la tabla de arriba  
2. **Revisa el archivo de ejemplo completo** para entender la implementación total  
3. **Ejecuta el ejemplo** siguiendo las instrucciones en [`complete_examples.md`](./complete_examples.md)  
4. **Modifica y extiende** el ejemplo para tu caso de uso específico  

Para documentación detallada sobre cómo ejecutar y personalizar estos ejemplos, consulta: **[📖 Documentación de ejemplos completos](./complete_examples.md)**  

### 💡 Solución vs. Ejemplos Completos

| **Carpeta de Solución** | **Ejemplos Completos** |
|------------------------|-----------------------|
| Estructura completa del proyecto con archivos de compilación | Implementaciones en un solo archivo |
| Listo para ejecutar con dependencias | Ejemplos de código enfocados |
| Configuración parecida a producción | Referencia educativa |
| Herramientas específicas del lenguaje | Comparación entre lenguajes |

Ambos enfoques son valiosos: usa la **carpeta de solución** para proyectos completos y los **ejemplos completos** para aprendizaje y referencia.  

## Puntos clave

Los puntos clave de este capítulo sobre clientes son los siguientes:

- Pueden usarse tanto para descubrir como para invocar funcionalidades en el servidor.  
- Pueden iniciar un servidor mientras se inician a sí mismos (como en este capítulo), pero los clientes también pueden conectarse a servidores ya en ejecución.  
- Son una excelente forma de probar las capacidades del servidor junto a alternativas como el Inspector, como se describió en el capítulo anterior.  

## Recursos adicionales

- [Construcción de clientes en MCP](https://modelcontextprotocol.io/quickstart/client)  

## Ejemplos

- [Calculadora Java](../samples/java/calculator/README.md)  
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)  
- [Calculadora JavaScript](../samples/javascript/README.md)  
- [Calculadora TypeScript](../samples/typescript/README.md)  
- [Calculadora Python](../../../../03-GettingStarted/samples/python)  
- [Calculadora Rust](../../../../03-GettingStarted/samples/rust)  

## Qué sigue

- Siguiente: [Creando un cliente con un LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automatizada [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->