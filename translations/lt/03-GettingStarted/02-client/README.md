# Kliento kūrimas

Klientai yra pasirinktinės programos arba scenarijai, kurie tiesiogiai bendrauja su MCP serveriu, prašydami išteklių, įrankių ir užklausų. Skirtingai nei naudojant inspector įrankį, kuris suteikia grafinę sąsają serveriui valdyti, savo kliento rašymas leidžia programiškai ir automatizuotai bendrauti. Tai leidžia kūrėjams integruoti MCP galimybes į savo darbo eigas, automatizuoti užduotis ir kurti specifiniams poreikiams pritaikytus sprendimus.

## Apžvalga

Ši pamoka pristato klientų sąvoką Model Context Protocol (MCP) ekosistemoje. Išmoksite rašyti savo klientą ir prijungti jį prie MCP serverio.

## Mokymosi tikslai

Pabaigus pamoką, sugebėsite:

- Suprasti, ką gali daryti klientas.
- Parašyti savo klientą.
- Prisijungti ir išbandyti klientą su MCP serveriu, kad įsitikintumėte, jog jis veikia kaip tikėtasi.

## Kas įeina į kliento rašymą?

Norėdami rašyti klientą, turėsite atlikti šiuos veiksmus:

- **Importuoti tinkamas bibliotekas**. Naudosite tą pačią biblioteką kaip ir anksčiau, tik skirtingus konstruktus.
- **Sukurkite kliento egzempliorių**. Tai reikš sukurti kliento instance ir prisijungti prie pasirinktos transportavimo metodikos.
- **Nuspręsti, kokius išteklius išvardinti**. Jūsų MCP serveris turi išteklius, įrankius ir užklausas, reikia nuspręsti, ką iš jų išvardinti.
- **Integruoti klientą į pagrindinę programą**. Kai žinosite serverio galimybes, turite integruoti tai į savo pagrindinę programą, kad jei vartotojas įveda užklausą ar kitą komandą, būtų iškviečiama atitinkama serverio funkcija.

Dabar, kai suprantame aukšto lygio, ką turime daryti, pažvelkime į pavyzdį.

### Pavyzdinis klientas

Pažiūrėkime į šį pavyzdinį klientą:

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

// Sąrašo užklausos
const prompts = await client.listPrompts();

// Gauti užklausą
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Sąrašas išteklių
const resources = await client.listResources();

// Skaityti išteklius
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Iškvietimo įrankis
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Ankstesniame kode mes:

- Importuojame bibliotekas
- Sukuriame kliento egzempliorių ir prijungiame jį naudodami stdio transportą.
- Išvardiname užklausas, išteklius ir įrankius bei iškviečiame visus juos.

Štai jums klientas, kuris gali bendrauti su MCP serveriu.

Skirkime laiko kitame pratimo skyriuje išanalizuoti kiekvieną kodo fragmentą ir paaiškinti, kas vyksta.

## Pratimas: Kliento rašymas

Kaip minėta anksčiau, skirkime laiko paaiškinti kodą, o jei norite, koduokite kartu.

### -1- Bibliotekų importavimas

Importuokime reikiamas bibliotekas, reikės nuorodų į klientą ir mūsų pasirinktą transporto protokolą stdio. stdio yra protokolas, skirtas vietinėms programoms. SSE yra kitas transporto protokolas, kurį pamatysite vėlesniuose skyriuose, bet dabar tęsiame su stdio.

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

Java atveju sukursite klientą, kuris prisijungia prie MCP serverio iš ankstesnio pratimo. Naudodami tą patį Java Spring Boot projekto struktūrą iš [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), sukurkite naują Java klasę pavadinimu `SDKClient` kataloge `src/main/java/com/microsoft/mcp/sample/client/` ir pridėkite šiuos importus:

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

Reikės pridėti šias priklausomybes į savo `Cargo.toml` failą.

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

Tada galėsite importuoti reikalingas bibliotekas savo kliento kode.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Eime prie egzemplioriaus kūrimo.

### -2- Kliento ir transporto instancijos kūrimas

Reikės sukurti transporto ir mūsų kliento egzempliorius:

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

Ankstesniame kode mes:

- Sukūrėme stdio transporto egzempliorių. Pastebėkite, kaip nurodomas komandos ir argumentų sąrašas, naudojamas serveriui paleisti, nes tai reikės daryti kuriant klientą.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Inicializavome klientą, priskirdami jam vardą ir versiją.

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

# Sukurti serverio parametrus stdio ryšiui
server_params = StdioServerParameters(
    command="mcp",  # Vykdomasis failas
    args=["run", "server.py"],  # Pasirinktiniai komandų eilutės argumentai
    env=None,  # Pasirinktiniai aplinkos kintamieji
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializuoti ryšį
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Ankstesniame kode mes:

- Importavome reikiamas bibliotekas
- Inicializavome serverio parametrų objektą, kurį naudosime serverio paleidimui, kad galėtume prie jo jungtis su klientu.
- Apibrėžėme `run` metodą, kuris iškviečia `stdio_client` – tai paleidžia klientų sesiją.
- Sukūrėme įėjimo tašką, kuriame pateikiame `run` metodą `asyncio.run`.

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

Ankstesniame kode mes:

- Importavome reikiamas bibliotekas.
- Sukūrėme stdio transportą ir inicializavome klientą `mcpClient`. Jį naudosime įrankių išserveriui iškvietimui.

Atkreipkite dėmesį, kad „Arguments“ galite nurodyti arba *.csproj* failą, arba vykdomąjį failą.

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
        
        // Jūsų kliento logika eina čia
    }
}
```

Ankstesniame kode mes:

- Sukūrėme pagrindinį metodą, kuris nustato SSE transportą į `http://localhost:8080`, kuriame veiks mūsų MCP serveris.
- Sukūrėme klientų klasę, kuri paima transportą kaip konstruktoriaus parametrą.
- `run` metode sukūrėme sinchroninį MCP klientą naudodami transportą ir inicializavome ryšį.
- Naudojome SSE (Server-Sent Events) transportą, tinkamą HTTP pagrindu veikiančiai komunikacijai su Java Spring Boot MCP serveriais.

#### Rust

Atkreipkite dėmesį, kad šis Rust klientas daro prielaidą, jog serveris yra kaimyninis projektas pavadinimu „calculator-server“ tame pačiame kataloge. Žemiau pateiktas kodas paleis serverį ir prisijungs prie jo.

```rust
async fn main() -> Result<(), RmcpError> {
    // Tarkime, kad serveris yra brolis projektas pavadinimu "calculator-server" tame pačiame kataloge
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

    // TODO: Inicializuoti

    // TODO: Išvardinti įrankius

    // TODO: Iškvieti add įrankį su argumentais = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Serverio funkcijų išvardinimas

Dabar turime klientą, galintį prisijungti, kai programa bus paleista. Tačiau jis neparodo savo funkcijų, tad darykime tai dabar:

#### TypeScript

```typescript
// Parodyti užklausas
const prompts = await client.listPrompts();

// Parodyti išteklius
const resources = await client.listResources();

// parodyti įrankius
const tools = await client.listTools();
```

#### Python

```python
# Išvardinti galimus išteklius
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Išvardinti galimus įrankius
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Čia išvardijame galimus išteklius, `list_resources()` ir įrankius, `list_tools`, ir atspausdiname juos.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Aukščiau pateiktas pavyzdys, kaip išvardyti įrankius serveryje. Kiekvienam įrankiui atspausdiname jo pavadinimą.

#### Java

```java
// Išvardinti ir parodyti įrankius
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Taip pat galite siųsti ping serveriui, kad patikrintumėte ryšį
client.ping();
```

Ankstesniame kode mes:

- Iškvietėme `listTools()`, kad gautume visus MCP serverio įrankius.
- Naudojome `ping()`, kad patikrintume ryšį su serveriu.
- `ListToolsResult` objektas – tai informacija apie visus įrankius, įskaitant jų pavadinimus, aprašymus ir įvedimo schemas.

Puiku, dabar surinkome visas funkcijas. Klausimas, kada jas naudoti? Šis klientas gana paprastas ir reikalauja aiškiai kviesti funkcijas, kai reikia. Kitame skyriuje kursime pažangesnį klientą, kuris turės prieigą prie savo didelio kalbos modelio (LLM). O dabar pamatykime, kaip galime iškviesti serverio funkcijas:

#### Rust

Pagrindinėje funkcijoje, po kliento inicializacijos, galime inicializuoti serverį ir išvardinti kai kurias jo funkcijas.

```rust
// Inicializuoti
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Įrankių sąrašas
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funkcijų iškvietimas

Kad iškviestume funkcijas, turime nurodyti teisingus argumentus, o kai kada ir funkcijos pavadinimą.

#### TypeScript

```typescript

// Perskaitykite išteklių
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Iškvieskite įrankį
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// iškvieskite užklausą
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Ankstesniame kode mes:

- Perskaityti išteklių, kviečiame išteklių per `readResource()`, nurodydami `uri`. Serverio pusėje tai atrodytų maždaug taip:

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

    Mūsų `uri` reikšmė `file://example.txt` atitinka `file://{name}` serveryje. `example.txt` bus priskirta `name`.

- Kviesti įrankį, kviesdami jį nurodant jo `name` ir `arguments` taip:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Gauti užklausą, `getPrompt()` kviečiame su `name` ir `arguments`. Serverio kodas atrodo taip:

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

    Tad jūsų kliento kodo fragmentas atrodys taip, kad atitiktų serverio deklaracijas:

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
# Perskaityti išteklių
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Iškviesti įrankį
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Ankstesniame kode mes:

- Iškvietėme išteklių, vadinamą `greeting`, naudodami `read_resource`.
- Iškvietėme įrankį, vadinamą `add`, naudodami `call_tool`.

#### .NET

1. Pridėkime šiek tiek kodo įrankio kvietimui:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Kad atspausdintume rezultatą, štai kodo fragmentas, kuris tai aptarnauja:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Skambinkite įvairiems skaičiuotuvo įrankiams
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

Ankstesniame kode mes:

- Kviečiame kelis skaičiuotuvo įrankius naudodami `callTool()` metodą su `CallToolRequest` objektais.
- Kiekviename įrankių kvietime nurodomas įrankio pavadinimas ir argumentų `Map`.
- Serverio įrankiai tikisi specifinių parametrų pavadinimų (pvz., "a", "b" matematiniams veiksmams).
- Rezultatai pateikiami kaip `CallToolResult` objektai, turintys serverio atsakymą.

#### Rust

```rust
// Iškvieskite add įrankį su argumentais = {"a": 3, "b": 2}
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

Klientą paleiskite įvesdami šią komandą terminale:

#### TypeScript

Įtraukite šį įrašą į savo "scripts" skyrių *package.json* faile:

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

Pirmiausia įsitikinkite, kad MCP serveris veikia adresu `http://localhost:8080`. Tuomet paleiskite klientą:

```bash
# Sukurkite savo projektą
./mvnw clean compile

# Paleiskite klientą
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Arba galite paleisti visą klientų projektą, pateiktą sprendimo kataloge `03-GettingStarted\02-client\solution\java`:

```bash
# Eikite į sprendinio katalogą
cd 03-GettingStarted/02-client/solution/java

# Sukurkite ir paleiskite JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Užduotis

Šioje užduotyje panaudosite ką išmokote kurdami klientą, bet sukursite savo klientą.

Štai serveris, kurį galite naudoti ir kuriuo turite kreiptis per savo kliento kodą. Pažiūrėkite, ar galite pridėti daugiau funkcijų serveriui, kad jis būtų įdomesnis.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Sukurkite MCP serverį
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Pridėti papildomą įrankį
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Pridėti dinamišką pasveikinimo išteklių
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

// Pradėkite priimti žinutes iš stdin ir siųsti žinutes per stdout

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

# Sukurkite MCP serverį
mcp = FastMCP("Demo")


# Pridėti sudėties įrankį
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Pridėti dinaminę pasveikinimo priemonę
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

Peržiūrėkite šį projektą, kad pamatytumėte, kaip galite [pridėti užklausų ir išteklių](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Taip pat pasižiūrėkite šią nuorodą apie tai, kaip iškviesti [užklausas ir išteklius](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Ankstesniame skyriuje [../01-first-server] išmokote sukurti paprastą MCP serverį naudojant Rust. Galite tęsti puoselėti tą serverį arba pažiūrėti šią nuorodą su daugiau Rust pagrindu sukurtų MCP serverių pavyzdžių: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Sprendimas

**Sprendimo kataloge** yra pilni, paruošti paleisti klientų įgyvendinimai, demonstruojantys visas šio vadovo idėjas. Kiekviename sprendime yra sovariantis kliento ir serverio kodas, organizuotas kaip atskiri, savarankiški projektai.

### 📁 Sprendimo struktūra

Sprendimo katalogas yra organizuotas pagal programavimo kalbas:

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

### 🚀 Ką kiekvienas sprendimas apima

Kiekvienas kalbai skirtas sprendimas:

- **Pilną kliento įgyvendinimą**, su visomis pamokoje aprašytomis funkcijomis
- **Veikiančią projekto struktūrą** su tinkamomis priklausomybėmis ir konfigūracija
- **Komandų skriptus** lengvam kūrimui ir paleidimui
- **Išsamų README** su kalbai specifinėmis instrukcijomis
- **Klaidų tvarkymo** ir rezultatų apdorojimo pavyzdžius

### 📖 Sprendimų naudojimas

1. **Eikite į pageidaujamos kalbos katalogą**:

   ```bash
   cd solution/typescript/    # Skirta TypeScript
   cd solution/java/          # Skirta Java
   cd solution/python/        # Skirta Python
   cd solution/dotnet/        # Skirta .NET
   ```

2. **Sekite README nurodymus kiekviename kataloge, kad:**
   - Įdiegtumėte priklausomybes
   - Sukurtumėte projektą
   - Paleistumėte klientą

3. **Pavyzdinis išvestis, kurią turėtumėte pamatyti:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pilną dokumentaciją ir žingsnis po žingsnio instrukcijas rasite: **[📖 Sprendimo dokumentacija](./solution/README.md)**

## 🎯 Pilni pavyzdžiai

Pateikėme pilnus, veikiančius klientų įgyvendinimus visomis šio vadovo programavimo kalbomis. Šie pavyzdžiai demonstruoja visas aukščiau aprašytas funkcijas ir gali būti naudojami kaip atspirties taškai arba pavyzdinės įgyvendinimo versijos.

### Galimi pilni pavyzdžiai

| Kalba | Failas | Aprašymas |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Pilnas Java klientas naudojantis SSE transportą su išsamia klaidų tvarka |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Pilnas C# klientas su stdio transportu ir automatiniu serverio paleidimu |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Pilnas TypeScript klientas pilnai palaikantis MCP protokolą |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Pilnas Python klientas naudojantis async/await paradigmas |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Pilnas Rust klientas naudojantis Tokio asinchroniniams veiksmams |

Kiekvienas pilnas pavyzdys apima:

- ✅ **Ryšio užmezgimą** ir klaidų tvarkymą
- ✅ **Serverio identifikavimą** (įrankius, išteklius, užklausas, jei taikoma)
- ✅ **Skaičiuotuvo operacijas** (sudėti, atimti, dauginti, dalyti, pagalba)
- ✅ **Rezultatų apdorojimą** ir formatavimą
- ✅ **Išsamų klaidų tvarkymą**

- ✅ **Švarus, dokumentuotas kodas** su žingsnis po žingsnio komentarais

### Pradžia su pilnais pavyzdžiais

1. **Pasirinkite pageidaujamą kalbą** iš aukščiau pateiktos lentelės
2. **Peržiūrėkite pilną pavyzdžių failą** norėdami suprasti visą įgyvendinimą
3. **Paleiskite pavyzdį** vadovaudamiesi instrukcijomis [`complete_examples.md`](./complete_examples.md)
4. **Modifikuokite ir išplėskite** pavyzdį pagal savo konkretų naudojimą

Dėl išsamios dokumentacijos apie šių pavyzdžių paleidimą ir pritaikymą žr.: **[📖 Pilnų pavyzdžių dokumentacija](./complete_examples.md)**

### 💡 Sprendimas vs. pilni pavyzdžiai

| **Sprendimo aplankas** | **Pilni pavyzdžiai** |
|----------------------|-----------------------|
| Visas projekto struktūra su build failais | Vieno failo įgyvendinimai |
| Paruošta paleidimui su priklausomybėmis | Koncentruoti kodo pavyzdžiai |
| Produkcijai artima aplinka | Mokomoji medžiaga |
| Kalbai specifiniai įrankiai | Kalbų tarpusavio palyginimas |

Abi prieigos yra vertingos - naudokite **sprendimo aplanką** pilniems projektams ir **pilnus pavyzdžius** mokymuisi bei kaip atskaitos tašką.

## Pagrindinės išvados

Pagrindinės šio skyriaus išvados apie klientus yra šios:

- Gali būti naudojami tiek funkcijoms serveryje atrasti, tiek jas iškviesti.
- Gali paleisti serverį kol pats paleidžiasi (kaip šiame skyriuje), bet klientai taip pat gali prisijungti prie jau veikiančių serverių.
- Yra puikus būdas išbandyti serverio galimybes, greta alternatyvų, kaip Inspector, kaip aprašyta ankstesniame skyriuje.

## Papildomi ištekliai

- [Klientų kūrimas MCP](https://modelcontextprotocol.io/quickstart/client)

## Pavyzdžiai

- [Java skaičiuoklė](../samples/java/calculator/README.md)
- [.NET skaičiuoklė](../../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuoklė](../samples/javascript/README.md)
- [TypeScript skaičiuoklė](../samples/typescript/README.md)
- [Python skaičiuoklė](../../../../03-GettingStarted/samples/python)
- [Rust skaičiuoklė](../../../../03-GettingStarted/samples/rust)

## Kas toliau

- Toliau: [Kliento kūrimas su LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->