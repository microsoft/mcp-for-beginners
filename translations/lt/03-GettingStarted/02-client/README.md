# Kliento kūrimas

Klientai yra pritaikytos programos arba skriptai, kurie tiesiogiai bendrauja su MCP serveriu, siekdami gauti išteklius, įrankius ir užklausas. Skirtingai nei naudojant inspektoriaus įrankį, kuris suteikia grafinę sąsają sąveikai su serveriu, savo kliento rašymas leidžia programiškai ir automatiškai vykdyti užduotis. Tai leidžia kūrėjams integruoti MCP galimybes į savo darbo eigą, automatizuoti procesus ir kurti pritaikytus sprendimus, atitinkančius specifinius poreikius.

## Apžvalga

Ši pamoka supažindina su klientų koncepcija Model Context Protocol (MCP) ekosistemoje. Jūs išmoksite, kaip parašyti savo klientą ir prijungti jį prie MCP serverio.

## Mokymosi tikslai

Šios pamokos pabaigoje jūs galėsite:

- Suprasti, ką gali atlikti klientas.
- Parašyti savo klientą.
- Prijungti ir išbandyti klientą su MCP serveriu, kad įsitikintumėte, jog jis veikia tinkamai.

## Kas įeina į kliento kūrimą?

Norėdami parašyti klientą, turėsite atlikti šiuos veiksmus:

- **Importuoti tinkamas bibliotekas**. Naudosite tą pačią biblioteką kaip ir anksčiau, tik su kitais konstruktais.
- **Sukurti kliento egzempliorių**. Tai apims kliento instancijos sukūrimą ir jos prijungimą prie pasirinkto transporto metodo.
- **Nuspręsti, kokius išteklius išvardinti**. Jūsų MCP serveris turi išteklius, įrankius ir užklausas, todėl turite nuspręsti, kuriuos iš jų išvardinti.
- **Integruoti klientą į pagrindinę programą**. Kai žinosite serverio galimybes, turėsite integruoti jas į pagrindinę programą, kad vartotojas, įvedęs užklausą ar kitą komandą, galėtų iškviesti atitinkamą serverio funkciją.

Dabar, kai suprantame, ką darysime aukštu lygiu, pažvelkime į pavyzdį.

### Kliento pavyzdys

Pažvelkime į šį kliento pavyzdį:

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

Šiame kode mes:

- Importuojame bibliotekas.
- Sukuriame kliento egzempliorių ir prijungiame jį naudodami `stdio` kaip transporto metodą.
- Išvardijame užklausas, išteklius ir įrankius bei juos visus iškviečiame.

Štai ir viskas – klientas, kuris gali bendrauti su MCP serveriu.

Skirkime laiko kitame pratimų skyriuje, kad išskaidytume kiekvieną kodo fragmentą ir paaiškintume, kas vyksta.

## Pratimas: Kliento rašymas

Kaip minėta aukščiau, skirkime laiko paaiškinimui, ir, jei norite, galite koduoti kartu.

### -1- Bibliotekų importavimas

Importuokime reikalingas bibliotekas. Mums reikės nuorodų į klientą ir pasirinktą transporto protokolą, `stdio`. `stdio` yra protokolas, skirtas programoms, veikiančioms jūsų vietiniame kompiuteryje. `SSE` yra kitas transporto protokolas, kurį parodysime būsimuose skyriuose, tačiau dabar tęskime su `stdio`.

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

Java atveju sukursite klientą, kuris jungiasi prie MCP serverio iš ankstesnio pratimo. Naudodami tą pačią Java Spring Boot projekto struktūrą iš [Pradžia su MCP serveriu](../../../../03-GettingStarted/01-first-server/solution/java), sukurkite naują Java klasę pavadinimu `SDKClient` aplanke `src/main/java/com/microsoft/mcp/sample/client/` ir pridėkite šiuos importus:

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

Pridėkite šias priklausomybes į savo `Cargo.toml` failą.

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

Tada galite importuoti reikalingas bibliotekas savo kliento kode.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Pereikime prie instancijos kūrimo.

### -2- Kliento ir transporto instancijos kūrimas

Turėsime sukurti transporto ir kliento instancijas:

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

Šiame kode mes:

- Sukūrėme `stdio` transporto instanciją. Atkreipkite dėmesį, kaip nurodomi komanda ir argumentai, kad būtų galima rasti ir paleisti serverį – tai reikės atlikti kuriant klientą.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Sukūrėme klientą, nurodydami jo pavadinimą ir versiją.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Prijungėme klientą prie pasirinkto transporto.

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

Šiame kode mes:

- Importavome reikalingas bibliotekas.
- Sukūrėme serverio parametrų objektą, kurį naudosime paleisti serverį, kad galėtume prie jo prisijungti su klientu.
- Apibrėžėme metodą `run`, kuris savo ruožtu iškviečia `stdio_client`, pradėdamas kliento sesiją.
- Sukūrėme įėjimo tašką, kuriame `run` metodas perduodamas `asyncio.run`.

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

Šiame kode mes:

- Importavome reikalingas bibliotekas.
- Sukūrėme `stdio` transportą ir klientą `mcpClient`. Pastarasis bus naudojamas išvardinti ir iškviesti MCP serverio funkcijas.

Atkreipkite dėmesį, kad "Arguments" galite nurodyti arba *.csproj* failą, arba vykdomąjį failą.

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

Šiame kode mes:

- Sukūrėme pagrindinį metodą, kuris nustato `SSE` transportą, nukreiptą į `http://localhost:8080`, kur veiks mūsų MCP serveris.
- Sukūrėme kliento klasę, kuri priima transportą kaip konstruktoriaus parametrą.
- Metode `run` sukūrėme sinchroninį MCP klientą, naudodami transportą, ir inicijavome ryšį.
- Naudojome `SSE` (Server-Sent Events) transportą, kuris tinka HTTP pagrindu veikiančiai komunikacijai su Java Spring Boot MCP serveriais.

#### Rust

Šis Rust klientas daro prielaidą, kad serveris yra gretimas projektas, pavadintas "calculator-server", tame pačiame kataloge. Žemiau pateiktas kodas paleis serverį ir prisijungs prie jo.

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

### -3- Serverio funkcijų išvardijimas

Dabar turime klientą, kuris gali prisijungti, jei programa bus paleista. Tačiau jis dar neišvardija savo funkcijų, todėl padarykime tai:

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

Čia išvardijame galimus išteklius, naudodami `list_resources()`, ir įrankius, naudodami `list_tools`, bei juos atspausdiname.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Aukščiau pateiktas pavyzdys parodo, kaip galime išvardyti serverio įrankius. Kiekvienam įrankiui atspausdiname jo pavadinimą.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Šiame kode mes:

- Iškvietėme `listTools()`, kad gautume visus galimus įrankius iš MCP serverio.
- Naudojome `ping()`, kad patikrintume, ar ryšys su serveriu veikia.
- `ListToolsResult` pateikia informaciją apie visus įrankius, įskaitant jų pavadinimus, aprašymus ir įvesties schemas.

Puiku, dabar užfiksavome visas funkcijas. Dabar klausimas – kada jas naudoti? Šis klientas yra gana paprastas, paprastas ta prasme, kad funkcijas turėsime iškviesti tiesiogiai, kai jų prireiks. Kitame skyriuje sukursime pažangesnį klientą, kuris turės prieigą prie savo didelio kalbos modelio (LLM). Dabar pažiūrėkime, kaip galime iškviesti serverio funkcijas:

#### Rust

Pagrindinėje funkcijoje, inicijavę klientą, galime inicijuoti serverį ir išvardyti kai kurias jo funkcijas.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funkcijų iškvietimas

Norėdami iškviesti funkcijas, turime užtikrinti, kad nurodome tinkamus argumentus ir kai kuriais atvejais pavadinimą, ką bandome iškviesti.

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

Šiame kode mes:

- Skaitome išteklių, iškviesdami `readResource()` ir nurodydami `uri`. Štai kaip tai greičiausiai atrodo serverio pusėje:

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

    Mūsų `uri` reikšmė `file://example.txt` atitinka `file://{name}` serverio pusėje. `example.txt` bus susietas su `name`.

- Iškviečiame įrankį, nurodydami jo `name` ir `arguments` taip:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Gauname užklausą, iškviesdami `getPrompt()` su `name` ir `arguments`. Serverio kodas atrodo taip:

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

    Todėl jūsų kliento kodas atrodys taip, kad atitiktų tai, kas deklaruota serveryje:

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

Šiame kode mes:

- Iškvietėme išteklių, pavadintą `greeting`, naudodami `read_resource`.
- Iškvietėme įrankį, pavadintą `add`, naudodami `call_tool`.

#### .NET

1. Pridėkime kodą įrankio iškvietimui:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Norėdami atspausdinti rezultatą, pateikiame kodą, kuris tai apdoroja:

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

Šiame kode mes:

- Iškvietėme kelis skaičiuotuvo įrankius, naudodami `callTool()` metodą su `CallToolRequest` objektais.
- Kiekvienas įrankio iškvietimas nurodo įrankio pavadinimą ir `Map` argumentų, reikalingų tam įrankiui.
- Serverio įrankiai tikisi specifinių parametrų pavadinimų (pvz., "a", "b" matematinėms operacijoms).
- Rezultatai grąžinami kaip `CallToolResult` objektai, kuriuose yra serverio atsakymas.

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

### -5- Kliento paleidimas

Norėdami paleisti klientą, terminale įveskite šią komandą:

#### TypeScript

Pridėkite šį įrašą į savo "scripts" sekciją *package.json* faile:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Paleiskite klientą naudodami šią komandą:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Pirmiausia įsitikinkite, kad jūsų MCP serveris veikia adresu `http://localhost:8080`. Tada paleiskite klientą:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Arba galite paleisti pilną kliento projektą, pateiktą sprendimų aplanke `03-GettingStarted\02-client\solution\java`:

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

## Užduotis

Šioje užduotyje naudosite tai, ką išmokote kurdami klientą, tačiau sukursite savo klientą.

Štai serveris, kurį galite naudoti, ir kurį turite iškviesti per savo kliento kodą. Pabandykite pridėti daugiau funkcijų prie serverio, kad jis būtų įdomesnis.

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

Peržiūrėkite šį projektą, kad sužinotumėte, kaip [pridėti užklausas ir išteklius](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Taip pat patikrinkite šią nuorodą, kaip iškviesti [užklausas ir išteklius](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Ankstesniame skyriuje (../01-first-server) išmokote sukurti paprastą MCP serverį su Rust. Galite tęsti darbą su tuo arba peržiūrėti šią nuorodą, kur rasite daugiau Rust pagrindu veikiančių MCP serverio pavyzdžių: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Sprendimas

**Sprendimų aplankas** apima pilnus, paruoštus naudoti kliento įgyvendinimus, kurie demonstruoja visas šioje pamokoje aptartas koncepcijas. Kiekvienas sprendimas apima tiek kliento, tiek serverio kodą, organizuotą atskiruose, savarankiškuose projektuose.

### 📁 Sprendimų struktūra

Sprendimų katalogas organizuotas pagal programavimo kalbą:

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

### 🚀 Ką apima kiekvienas sprendimas

Kiekvienas kalbai skirtas sprendimas pateikia:

- **Pilną kliento įgyvendinimą** su visomis pamokoje aptartomis funkcijomis.
- **Veikiantį projekto struktūrą** su tinkamomis priklausomybėmis ir konfigūracija.
- **Kūrimo ir paleidimo skriptus** lengvam nustatymui ir vykdymui.
- **Išsamų README** su kalbai specifinėmis instrukcijomis.
- **Klaidų tvarkymo** ir rezultatų apdorojimo pavyzdžius.

### 📖 Kaip naudoti sprendimus

1. **Eikite į norimos kalbos aplanką**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Sekite README instrukcijas** kiekviename aplanke:
   - Priklausomybių diegimas
   - Projekto kūrimas
   - Kliento paleidimas

3. **Pavyzdinė išvestis**, kurią turėtumėte matyti:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Dėl išsamios dokumentacijos ir žingsnis po žingsnio instrukcijų žiūrėkite: **[📖 Sprendimų dokumentacija](./solution/README.md)**

## 🎯 Pilni pavyzdžiai

Pateikėme pilnus, veikiančius kliento įgyvendinimus visoms šioje pamokoje aptartoms programavimo kalboms. Šie pavyzdžiai demonstruoja visą aprašytą funkcionalumą ir gali būti naudojami kaip atskaitos taškai arba pradiniai taškai jūsų projektams.

### Galimi pilni pavyzdžiai

| Kalba       | Failas                          | Aprašymas                                                                 |
|-------------|---------------------------------|---------------------------------------------------------------------------|
| **Java**    | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Pilnas Java klientas su SSE transportu ir išsamia klaidų tvarkyba         |
| **C#**      | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Pilnas C# klientas su `stdio` transportu ir automatiniu serverio paleidimu |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Pilnas TypeScript klientas su pilnu MCP protokolo palaikymu               |
| **Python**  | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Pilnas Python klientas su asinchroninio vykdymo modeliu                   |
| **Rust**    | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | Pilnas Rust klientas su Tokio asinchroniniu vykdymu                       |
Kiekvienas pilnas pavyzdys apima:

- ✅ **Ryšio užmezgimą** ir klaidų tvarkymą
- ✅ **Serverio paiešką** (įrankiai, ištekliai, užklausos, kur taikoma)
- ✅ **Skaičiuotuvo operacijas** (sudėti, atimti, dauginti, dalinti, pagalba)
- ✅ **Rezultatų apdorojimą** ir suformatuotą išvestį
- ✅ **Išsamų klaidų tvarkymą**
- ✅ **Švarų, dokumentuotą kodą** su žingsnis po žingsnio komentarais

### Pradžia su pilnais pavyzdžiais

1. **Pasirinkite norimą kalbą** iš aukščiau pateiktos lentelės
2. **Peržiūrėkite pilną pavyzdžio failą**, kad suprastumėte visą įgyvendinimą
3. **Paleiskite pavyzdį**, vadovaudamiesi instrukcijomis [`complete_examples.md`](./complete_examples.md)
4. **Modifikuokite ir praplėskite** pavyzdį pagal savo specifinius poreikius

Išsamią dokumentaciją apie pavyzdžių paleidimą ir pritaikymą rasite čia: **[📖 Pilnų pavyzdžių dokumentacija](./complete_examples.md)**

### 💡 Sprendimas vs. Pilni pavyzdžiai

| **Sprendimų aplankas** | **Pilni pavyzdžiai** |
|--------------------|--------------------- |
| Pilna projekto struktūra su surinkimo failais | Vieno failo įgyvendinimai |
| Paruošta paleidimui su priklausomybėmis | Koncentruoti kodo pavyzdžiai |
| Produkcijai pritaikyta aplinka | Mokomoji medžiaga |
| Kalbai specifiniai įrankiai | Kryžminės kalbų palyginimas |

Abi prieigos yra vertingos - naudokite **sprendimų aplanką** pilniems projektams ir **pilnus pavyzdžius** mokymuisi ir nuorodoms.

## Pagrindinės mintys

Pagrindinės šio skyriaus mintys apie klientus:

- Gali būti naudojami tiek serverio funkcijų paieškai, tiek jų vykdymui.
- Gali paleisti serverį tuo pačiu metu, kai paleidžiamas pats (kaip šiame skyriuje), tačiau klientai taip pat gali prisijungti prie jau veikiančių serverių.
- Puikus būdas išbandyti serverio galimybes, greta alternatyvų, tokių kaip Inspektorius, aprašytas ankstesniame skyriuje.

## Papildomi ištekliai

- [Klientų kūrimas MCP](https://modelcontextprotocol.io/quickstart/client)

## Pavyzdžiai

- [Java skaičiuotuvas](../samples/java/calculator/README.md)
- [.Net skaičiuotuvas](../../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuotuvas](../samples/javascript/README.md)
- [TypeScript skaičiuotuvas](../samples/typescript/README.md)
- [Python skaičiuotuvas](../../../../03-GettingStarted/samples/python)
- [Rust skaičiuotuvas](../../../../03-GettingStarted/samples/rust)

## Kas toliau

- Toliau: [Kliento kūrimas su LLM](../03-llm-client/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.