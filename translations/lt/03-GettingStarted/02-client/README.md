# Kliento kūrimas

Klientai yra individualios programos ar skriptai, kurie tiesiogiai bendrauja su MCP serveriu, užklausdami išteklių, įrankių ir užuominų. Skirtingai nei naudojantis inspektoriaus įrankiu, kuris suteikia grafinę sąsają serverio sąveikai, savarankiškas kliento rašymas leidžia programiškai ir automatizuotai bendrauti. Tai leidžia kūrėjams integruoti MCP galimybes į savo darbo eigas, automatizuoti užduotis ir kurti pritaikytus sprendimus pagal konkrečius poreikius.

## Apžvalga

Ši pamoka pristato klientų sąvoką Modelio konteksto protokolo (MCP) ekosistemoje. Sužinosite, kaip parašyti savo klientą ir prisijungti prie MCP serverio.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Suprasti, ką gali atlikti klientas.
- Parašyti savo klientą.
- Prisijungti ir išbandyti klientą su MCP serveriu, kad įsitikintumėte, jog serveris veikia pagal numatymus.

## Kas įeina į kliento rašymą?

Norėdami sukurti klientą, turėsite atlikti šiuos veiksmus:

- **Importuoti reikiamas bibliotekas**. Naudosite tą pačią biblioteką, kaip ir anksčiau, tik kitos konstrukcijos.
- **Inicijuoti klientą**. Tai apims kliento instancijos sukūrimą ir prisijungimą prie pasirinkto transporto metodo.
- **Nuspręsti, kuriuos išteklius listinti**. Jūsų MCP serveris turi išteklius, įrankius ir užuominas, jūs turite nuspręsti, kuriuos rodyti.
- **Integruoti klientą į pagrindinę programą**. Kai žinosite serverio galimybes, turėsite integruoti tai į savo pagrindinę programą, kad vartotojas įvedęs užuominą ar kitą komandą būtų iškviečiama atitinkama serverio funkcija.

Dabar, kai supratome aukšto lygio veiksmus, pažvelkime į pavyzdį.

### Kliento pavyzdys

Pažiūrėkime į šį kliento pavyzdį:

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

// Išvardinti užklausas
const prompts = await client.listPrompts();

// Gauti užklausą
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Išvardinti išteklius
const resources = await client.listResources();

// Perskaityti išteklių
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Iškvieti įrankį
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Aukščiau pateiktame kode mes:

- Importuojame bibliotekas
- Sukuriame kliento instanciją ir prisijungiame naudodami stdio transportą.
- Listiname užuominas, išteklius ir įrankius bei iškviečiame visus.

Štai jums klientas, kuris gali bendrauti su MCP serveriu.

Kitame pratimo skyriuje skirsime laiko detaliai išnagrinėti kiekvieną kodo fragmentą ir paaiškinti, kas vyksta.

## Pratimas: Kliento rašymas

Kaip minėta aukščiau, paaiškinsime kodą ramiai ir, jei norėsite, galite kartu rašyti kodą.

### -1- Bibliotekų importavimas

Importuokime reikiamas bibliotekas, reikės nuorodų į klientą ir pasirinkto transporto protokolą, stdio. stdio – tai protokolas skirtas programoms, kurias paleidžiate vietinėje mašinoje. SSE yra kitas transporto protokolas, kurį pamatysime vėlesniuose skyriuose, bet dabar tęsiame su stdio.

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

Java atveju sukursite klientą, kuris prisijungia prie ankstesnio pratimo MCP serverio. Naudojant tą patį Java Spring Boot projekto struktūrą iš [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), sukurkite naują Java klasę pavadinimu `SDKClient` kataloge `src/main/java/com/microsoft/mcp/sample/client/` ir pridėkite šiuos importus:

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

Turėsite pridėti šiuos priklausomumus į savo `Cargo.toml` failą.

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

Tada galite importuoti reikiamas bibliotekas savo kliento kode.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Eikime prie inicializacijos.

### -2- Kliento ir transporto inicializavimas

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

Aukščiau pateiktame kode mes:

- Sukūrėme stdio transporto instanciją. Atkreipkite dėmesį, kaip nurodomas komandos ir argumentų sąrašas serverio paleidimui – tai reikės kuriant klientą.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Inicijavome klientą suteikdami jam pavadinimą ir versiją.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Prisijungėme klientą prie pasirinkto transporto.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Sukurkite serverio parametrus stdio ryšiui
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

Aukščiau mes:

- Importavome reikalingas bibliotekas
- Inicijavome serverio parametrų objektą, kad galėtume paleisti serverį ir jungtis prie jo su klientu.
- Apibrėžėme metodą `run`, kuris savo ruožtu iškviečia `stdio_client`, pradedant klientų sesiją.
- Sukūrėme įėjimo tašką, kuriame perduodame `run` metodą `asyncio.run`.

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

Aukščiau mes:

- Importavome reikalingas bibliotekas.
- Sukūrėme stdio transportą ir klientą `mcpClient`. Pastarasis bus naudojamas įrankiams listinti ir iškvietimui MCP serveryje.

Pastaba, "Arguments" galite nurodyti arba *.csproj* failą, arba vykdomąjį failą.

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

Šiame kode mes:

- Sukūrėme pagrindinį metodą, kuris nustato SSE transportą, nukreiptą į `http://localhost:8080`, kur veiks MCP serveris.
- Sukūrėme klientų klasę, kuri gauna transportą konstruktoriaus parametru.
- Metode `run` sukuriame sinchroninį MCP klientą naudodami transportą ir inicializuojame ryšį.
- Naudojame SSE (Server-Sent Events) transporto protokolą, tinkantį HTTP pagrindu veikiančių Java Spring Boot MCP serverių komunikacijai.

#### Rust

Atkreipkite dėmesį, kad šis Rust klientas daro prielaidą, jog serveris yra broliškas projektas pavadinimu "calculator-server" tame pačiame kataloge. Šis kodas paleis serverį ir prisijungs prie jo.

```rust
async fn main() -> Result<(), RmcpError> {
    // Laikykime, kad serveris yra brolis projektas pavadinimu "calculator-server" toje pačioje direktorijoje
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

    // TODO: Iškvieskite add įrankį su argumentais = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Serverio funkcijų listinimas

Dabar turime klientą, kuris gali prisijungti, jei paleista programa. Tačiau jis neišrašo jokių funkcijų, tad padarykime tai:

#### TypeScript

```typescript
// Sąrašas užklausų
const prompts = await client.listPrompts();

// Sąrašas išteklių
const resources = await client.listResources();

// sąrašas įrankių
const tools = await client.listTools();
```

#### Python

```python
# Išvardinti turimus išteklius
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Išvardinti turimus įrankius
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Čia mes listiname turimus išteklius `list_resources()` ir įrankius `list_tools` ir išvedame juos.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Čia pavyzdys, kaip galime listinti serverio įrankius. Kiekvienam įrankiui atspausdiname jo pavadinimą.

#### Java

```java
// Išvardykite ir parodykite įrankius
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Taip pat galite naudoti ping komandą serveriui patikrinti ryšį
client.ping();
```

Aukščiau mes:

- Iškvietėme `listTools()`, kad gautume visus MCP serverio įrankius.
- Naudojome `ping()`, kad patikrintume ryšį su serveriu.
- `ListToolsResult` pateikia informaciją apie visus įrankius, įskaitant jų pavadinimus, aprašymus ir įvesties schemas.

Puiku, dabar turime visas funkcijas. O kada jas naudoti? Šis klientas gana paprastas, reiškia, funkcijos turi būti kviečiamos tiesiogiai, kai jų reikia. Kitame skyriuje kursime pažangesnį klientą, turintį savo didelį kalbos modelį (LLM). O dabar pažiūrėkime, kaip iškviesti serverio funkcijas:

#### Rust

Pagrindinėje funkcijoje, po kliento inicializavimo, galime inicializuoti serverį ir listinti kelias jo funkcijas.

```rust
// Inicializuoti
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Įrankių sąrašas
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funkcijų iškvietimas

Norėdami iškviesti funkcijas, turime nurodyti teisingus argumentus ir kai kuriais atvejais funkcijos pavadinimą.

#### TypeScript

```typescript

// Skaityti išteklių
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kvieskite įrankį
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// kvietimo užklausa
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Šiame kode mes:

- Skaitome išteklių, kviesdami `readResource()` su `uri`. Štai kaip tai greičiausiai atrodo serverio pusėje:

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

    Mūsų `uri` reikšmė `file://example.txt` atitinka serverio `file://{name}`. `example.txt` bus priskirtas `name`.

- Kviesdami įrankį nurodome jo `name` ir `arguments`:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Norint gauti užuominą, kviečiame `getPrompt()` su `name` ir `arguments`. Serverio kodas atrodo taip:

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

    todėl jūsų kliento kodas atrodys taip, kad atitiktų serverio deklaracijas:

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
# Skaityti išteklių
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Iškviesti įrankį
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Šiame kode mes:

- Kvietėme išteklių `greeting` naudodami `read_resource`.
- Iškvietėme įrankį `add` naudodami `call_tool`.

#### .NET

1. Pridėkime kodą įrankio iškvietimui:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Štai kaip atspausdinti rezultatus:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Iškvieskite įvairius skaičiuotuvo įrankius
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

Aukščiau mes:

- Iškvietėme kelis skaičiuotuvo įrankius naudodami `callTool()` su `CallToolRequest` objektais.
- Kiekvienas įrankio kvietimas nurodo įrankio pavadinimą ir `Map`, kur sudėti reikalingi argumentai.
- Serverio įrankiai tikisi specifinių parametrų pavadinimų (pvz., „a“, „b“ matematinėms operacijoms).
- Rezultatai grąžinami kaip `CallToolResult` objektai su serverio atsakymu.

#### Rust

```rust
// Iškvieskite pridėjimo įrankį su argumentais = {"a": 3, "b": 2}
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

Pridėkite šį įrašą į "scripts" sekciją faile *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Klientą paleiskite šia komanda:

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

Arba galite paleisti visą klientų projektą, pateiktą sprendimo aplanke `03-GettingStarted\02-client\solution\java`:

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

Šioje užduotyje panaudosite įgytas žinias kurdami savo klientą.

Štai serveris, kurį galėsite naudoti, jį skambinkite per savo kliento kodą, pabandykite pridėti daugiau funkcijų, kad serveris taptų įdomesnis.

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

// Pridėkite papildomą įrankį
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Pridėkite dinaminį pasveikinimo išteklių
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

// Pradėkite gauti žinutes iš stdin ir siųsti žinutes į stdout

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


# Pridėkite sudėties įrankį
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Pridėkite dinamišką pasveikinimo išteklių
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

Peržiūrėkite šį projektą, kad sužinotumėte, kaip [pridėti užuominas ir išteklius](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Taip pat patikrinkite šią nuorodą, kaip iškviesti [užuominas ir išteklius](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Ankstesniame skyriuje [previous section](../../../../03-GettingStarted/01-first-server) sužinojote, kaip sukurti paprastą MCP serverį su Rust. Galite tęsti jį plėsdami arba patikrinti šią nuorodą su kitais Rust pagrindu MCP serverių pavyzdžiais: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Sprendimas

**Sprendimo aplanke** rasite pilnai veikiančius klientų implementacijos pavyzdžius, demonstruojančius visus šiame vadove aptartus konceptus. Kiekviename sprendime yra tiek kliento, tiek serverio kodas, organizuotas atskiruose savarankiškuose projektuose.

### 📁 Sprendimo struktūra

Sprendimo katalogas suskirstytas pagal programavimo kalbas:

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

Kiekvienas kalbai skirtas sprendimas suteikia:

- **Pilną kliento implementaciją** su visomis pamokoje aptartomis funkcijomis
- **Veikiančią projekto struktūrą** su tinkamomis priklausomybėmis ir konfigūracija
- **Statybos ir paleidimo scenarijus** paprastam nustatymui ir vykdymui
- **Išsamų README** su kalbai specifiniais nurodymais
- **Klaidų tvarkymo ir rezultatų apdorojimo pavyzdžius**

### 📖 Kaip naudoti sprendimus

1. **Eikite į jums patinkančios kalbos aplanką**:

   ```bash
   cd solution/typescript/    # Skirta TypeScript
   cd solution/java/          # Skirta Java
   cd solution/python/        # Skirta Python
   cd solution/dotnet/        # Skirta .NET
   ```

2. **Vadovaukitės README nurodymais kiekviename aplanke dėl**:
   - Priklausomybių diegimo
   - Projekto statymo
   - Kliento paleidimo

3. **Turėtumėte matyti tokį rezultatą**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Norėdami gauti visą dokumentaciją ir žingsnis po žingsnio instrukcijas, žiūrėkite: **[📖 Sprendimo dokumentacija](./solution/README.md)**

## 🎯 Pilni pavyzdžiai

Mes pateikiame pilnai veikiančius klientų pavyzdžius visose šio vadovo aptartose programavimo kalbose. Šie pavyzdžiai demonstruoja visas aukščiau aprašytas funkcijas ir gali būti naudojami kaip atspirties taškai jūsų projektams ar referencijomis.

### Galimi pilni pavyzdžiai

| Kalba | Failas | Aprašymas |
|-------|---------|-----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Pilnas Java klientas su SSE transportu ir išsamia klaidų tvarkymo logika |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Pilnas C# klientas su stdio transportu ir automatinio serverio paleidimo palaikymu |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Pilnas TypeScript klientas su visa MCP protokolo palaikymu |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Pilnas Python klientas su async/await modeliu |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Pilnas Rust klientas su Tokio asinchroninių operacijų palaikymu |

Kiekvienas pilnas pavyzdys apima:
- ✅ **Ryšio užmezgimas** ir klaidų valdymas
- ✅ **Serverio aptikimas** (įrankiai, ištekliai, raginimai, kur taikoma)
- ✅ **Skaičiuoklės operacijos** (sudėti, atimti, dauginti, dalyti, pagalba)
- ✅ **Rezultatų apdorojimas** ir suformatuotas išvedimas
- ✅ **Išsamus klaidų valdymas**
- ✅ **Švarus, dokumentuotas kodas** su žingsnis po žingsnio komentarais

### Pradžia su pilnais pavyzdžiais

1. **Pasirinkite pageidaujamą kalbą** lentelėje viršuje
2. **Peržiūrėkite pilną pavyzdinį failą**, kad suprastumėte visą įgyvendinimą
3. **Paleiskite pavyzdį** sekdami instrukcijas faile [`complete_examples.md`](./complete_examples.md)
4. **Modifikuokite ir išplėskite** pavyzdį pagal savo konkrečius poreikius

Daugiau detalių apie šių pavyzdžių paleidimą ir pritaikymą rasite: **[📖 Pilnų pavyzdžių dokumentacija](./complete_examples.md)**

### 💡 Sprendimas prieš Pilnus Pavyzdžius

| **Sprendimo aplankas** | **Pilni pavyzdžiai**            |
|------------------------|--------------------------------|
| Pilna projekto struktūra su statybos failais | Vieno failo įgyvendinimai          |
| Paruošta paleidimui su priklausomybėmis     | Koncentruoti kodo pavyzdžiai     |
| Produkcijai artima aplinka                    | Edukacinė referencija             |
| Kalbai specifiniai įrankiai                   | Tarpkalbinis palyginimas          |

Abu požiūriai yra vertingi – naudokite **sprendimo aplanką** pilniems projektams ir **pilnus pavyzdžius** mokymuisi bei nuorodoms.

## Svarbiausios Išvados

Pagrindinės šio skyriaus išvados apie klientus:

- Gali būti naudojami tiek funkcijoms serveryje atrasti, tiek iškviesti.
- Gali paleisti serverį tuo pačiu metu, kai pats paleidžiamas (kaip šiame skyriuje), bet klientai taip pat gali jungtis prie veikiančių serverių.
- Tai puikus būdas išbandyti serverio galimybes šalia alternatyvų, tokių kaip Inspector, kaip buvo aprašyta ankstesniame skyriuje.

## Papildomi Ištekliai

- [Klientų kūrimas MCP](https://modelcontextprotocol.io/quickstart/client)

## Pavyzdžiai

- [Java Skaičiuoklė](../samples/java/calculator/README.md)
- [.Net Skaičiuoklė](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Skaičiuoklė](../samples/javascript/README.md)
- [TypeScript Skaičiuoklė](../samples/typescript/README.md)
- [Python Skaičiuoklė](../../../../03-GettingStarted/samples/python)
- [Rust Skaičiuoklė](../../../../03-GettingStarted/samples/rust)

## Kas Toliau

- Toliau: [Kliento kūrimas su LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas natūralia kalba turėtų būti laikomas pagrindiniu šaltiniu. Svarbiai informacijai rekomenduojama pasinaudoti profesionalaus žmogaus vertimu. Mes neneame atsakingi už bet kokius nesusipratimus ar neteisingus interpretavimus, kylančius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->