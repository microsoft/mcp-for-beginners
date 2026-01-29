# Asiakkaan luominen

Asiakkaat ovat mukautettuja sovelluksia tai skriptejä, jotka kommunikoivat suoraan MCP-palvelimen kanssa pyytääkseen resursseja, työkaluja ja kehotteita. Toisin kuin tarkastustyökalun käyttö, joka tarjoaa graafisen käyttöliittymän palvelimen kanssa vuorovaikuttamiseen, oman asiakkaan kirjoittaminen mahdollistaa ohjelmalliset ja automatisoidut vuorovaikutukset. Tämä antaa kehittäjille mahdollisuuden integroida MCP-ominaisuudet omiin työnkulkuihinsa, automatisoida tehtäviä ja rakentaa mukautettuja ratkaisuja erityistarpeisiin.

## Yleiskatsaus

Tässä osiossa esitellään asiakkaiden käsite Model Context Protocol (MCP) -ekosysteemissä. Opit kirjoittamaan oman asiakkaan ja yhdistämään sen MCP-palvelimeen.

## Oppimistavoitteet

Tämän osion lopussa osaat:

- Ymmärtää, mitä asiakas voi tehdä.
- Kirjoittaa oman asiakkaan.
- Yhdistää ja testata asiakasta MCP-palvelimen kanssa varmistaaksesi, että palvelin toimii odotetusti.

## Mitä asiakkaan kirjoittaminen vaatii?

Asiakkaan kirjoittamiseksi sinun on tehtävä seuraavat asiat:

- **Tuo oikeat kirjastot**. Käytät samaa kirjastoa kuin aiemmin, mutta eri rakenteita.
- **Luo asiakas**. Tämä sisältää asiakasinstanssin luomisen ja sen yhdistämisen valittuun siirtomenetelmään.
- **Päätä, mitkä resurssit listataan**. MCP-palvelimellasi on resursseja, työkaluja ja kehotteita, ja sinun on päätettävä, mitkä niistä listataan.
- **Integroi asiakas isäntäsovellukseen**. Kun tiedät palvelimen ominaisuudet, sinun on integroitava tämä isäntäsovellukseesi niin, että kun käyttäjä kirjoittaa kehotteen tai muun komennon, vastaava palvelimen ominaisuus aktivoituu.

Nyt kun ymmärrämme yleisellä tasolla, mitä olemme tekemässä, katsotaan seuraavaksi esimerkkiä.

### Esimerkki asiakkaasta

Tarkastellaan tätä esimerkkiä asiakkaasta:

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

Edellisessä koodissa:

- Tuodaan kirjastot.
- Luodaan asiakasinstanssi ja yhdistetään se stdio-siirtomenetelmällä.
- Listataan kehotteet, resurssit ja työkalut ja kutsutaan niitä kaikkia.

Siinä se, asiakas, joka voi kommunikoida MCP-palvelimen kanssa.

Käytetään seuraavassa harjoitusosiossa aikaa ja puretaan jokainen koodinpätkä selittäen, mitä tapahtuu.

## Harjoitus: Asiakkaan kirjoittaminen

Kuten yllä mainittiin, käytetään aikaa koodin selittämiseen, ja voit halutessasi koodata mukana.

### -1- Kirjastojen tuominen

Tuodaan tarvittavat kirjastot. Tarvitsemme viittauksia asiakkaaseen ja valittuun siirtoprotokollaan, stdioon. stdio on protokolla asioille, jotka on tarkoitettu ajettavaksi paikallisella koneellasi. SSE on toinen siirtoprotokolla, jonka näytämme tulevissa luvuissa, mutta se on toinen vaihtoehtosi. Toistaiseksi jatketaan stdiolla.

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

Javaa varten luot asiakkaan, joka yhdistyy edellisen harjoituksen MCP-palvelimeen. Käyttäen samaa Java Spring Boot -projektirakennetta kuin [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), luo uusi Java-luokka nimeltä `SDKClient` kansioon `src/main/java/com/microsoft/mcp/sample/client/` ja lisää seuraavat tuonnit:

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

Sinun on lisättävä seuraavat riippuvuudet `Cargo.toml`-tiedostoosi.

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

Sen jälkeen voit tuoda tarvittavat kirjastot asiakaskoodissasi.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Siirrytään asiakkaan ja siirron alustamiseen.

### -2- Asiakkaan ja siirron alustaminen

Meidän on luotava siirtoinstanssi ja asiakkaan instanssi:

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

Edellisessä koodissa:

- Luodaan stdio-siirtoinstanssi. Huomaa, kuinka se määrittää komennon ja argumentit palvelimen löytämiseen ja käynnistämiseen, koska tämä on jotain, mitä meidän on tehtävä asiakkaan luomisen yhteydessä.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Luodaan asiakas antamalla sille nimi ja versio.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Yhdistetään asiakas valittuun siirtomenetelmään.

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

Edellisessä koodissa:

- Tuodaan tarvittavat kirjastot.
- Luodaan palvelinparametriobjekti, jota käytetään palvelimen käynnistämiseen, jotta siihen voidaan yhdistää asiakas.
- Määritellään `run`-metodi, joka puolestaan kutsuu `stdio_client`-metodia aloittaakseen asiakassession.
- Luodaan aloituspiste, jossa annetaan `run`-metodi `asyncio.run`-kutsulle.

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

Edellisessä koodissa:

- Tuodaan tarvittavat kirjastot.
- Luodaan stdio-siirto ja asiakas `mcpClient`. Jälkimmäistä käytetään MCP-palvelimen ominaisuuksien listaamiseen ja kutsumiseen.

Huomaa, että "Arguments"-kohdassa voit osoittaa joko *.csproj*-tiedostoon tai suoritettavaan tiedostoon.

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

Edellisessä koodissa:

- Luodaan päämetodi, joka määrittää SSE-siirron osoittamaan `http://localhost:8080`, jossa MCP-palvelin toimii.
- Luodaan asiakasluokka, joka ottaa siirron konstruktoriparametrina.
- `run`-metodissa luodaan synkroninen MCP-asiakas käyttäen siirtoa ja alustetaan yhteys.
- Käytetään SSE-siirtoa (Server-Sent Events), joka sopii HTTP-pohjaiseen viestintään Java Spring Boot MCP -palvelimien kanssa.

#### Rust

Tämä Rust-asiakas olettaa, että palvelin on sisarprojekti nimeltä "calculator-server" samassa hakemistossa. Alla oleva koodi käynnistää palvelimen ja yhdistää siihen.

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

### -3- Palvelimen ominaisuuksien listaaminen

Nyt meillä on asiakas, joka voi yhdistyä, jos ohjelma suoritetaan. Se ei kuitenkaan vielä listaa ominaisuuksiaan, joten tehdään se seuraavaksi:

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

Tässä listataan saatavilla olevat resurssit `list_resources()` ja työkalut `list_tools` ja tulostetaan ne.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Yllä on esimerkki, kuinka voimme listata palvelimen työkalut. Jokaiselle työkalulle tulostetaan sen nimi.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Edellisessä koodissa:

- Kutsutaan `listTools()` saadaksemme kaikki saatavilla olevat työkalut MCP-palvelimelta.
- Käytetään `ping()`-metodia varmistaaksemme, että yhteys palvelimeen toimii.
- `ListToolsResult` sisältää tietoja kaikista työkaluista, mukaan lukien niiden nimet, kuvaukset ja syötemallit.

Hienoa, nyt olemme tallentaneet kaikki ominaisuudet. Kysymys kuuluu, milloin käytämme niitä? Tämä asiakas on melko yksinkertainen, yksinkertainen siinä mielessä, että meidän on kutsuttava ominaisuuksia eksplisiittisesti, kun haluamme niitä. Seuraavassa luvussa luomme kehittyneemmän asiakkaan, jolla on pääsy omaan laajaan kielimalliinsa (LLM). Toistaiseksi katsotaan, kuinka voimme kutsua palvelimen ominaisuuksia:

#### Rust

Pääfunktiossa, asiakkaan alustamisen jälkeen, voimme alustaa palvelimen ja listata sen ominaisuuksia.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Ominaisuuksien kutsuminen

Ominaisuuksien kutsumiseksi meidän on varmistettava, että määritämme oikeat argumentit ja joissain tapauksissa kutsuttavan ominaisuuden nimi.

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

Edellisessä koodissa:

- Luetaan resurssi kutsumalla `readResource()` ja määrittämällä `uri`. Näin se todennäköisesti näyttää palvelimen puolella:

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

    `uri`-arvomme `file://example.txt` vastaa palvelimen `file://{name}`-määritystä. `example.txt` yhdistetään `name`-parametriin.

- Kutsutaan työkalua määrittämällä sen `name` ja `arguments` seuraavasti:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Haetaan kehotetta kutsumalla `getPrompt()` käyttäen `name` ja `arguments`. Palvelinkoodi näyttää tältä:

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

    Ja vastaava asiakaskoodi näyttää tältä, jotta se vastaa palvelimella määriteltyä:

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

Edellisessä koodissa:

- Kutsutaan resurssia nimeltä `greeting` käyttäen `read_resource`.
- Kutsutaan työkalua nimeltä `add` käyttäen `call_tool`.

#### .NET

1. Lisätään koodi työkalun kutsumiseen:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Tulostetaan tulos seuraavalla koodilla:

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

Edellisessä koodissa:

- Kutsutaan useita laskintyökaluja käyttäen `callTool()`-metodia ja `CallToolRequest`-objekteja.
- Jokainen työkalukutsu määrittää työkalun nimen ja `Map`-objektin, joka sisältää työkalun tarvitsemat argumentit.
- Palvelimen työkalut odottavat tiettyjä parametreja (kuten "a", "b" matemaattisiin operaatioihin).
- Tulokset palautetaan `CallToolResult`-objekteina, jotka sisältävät palvelimen vastauksen.

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

### -5- Asiakkaan suorittaminen

Asiakkaan suorittamiseksi kirjoita seuraava komento terminaaliin:

#### TypeScript

Lisää seuraava merkintä "scripts"-osioon *package.json*-tiedostossa:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Kutsu asiakasta seuraavalla komennolla:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Varmista ensin, että MCP-palvelimesi toimii osoitteessa `http://localhost:8080`. Suorita sitten asiakas:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Vaihtoehtoisesti voit suorittaa täydellisen asiakasprojektin, joka löytyy ratkaisukansiosta `03-GettingStarted\02-client\solution\java`:

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

## Tehtävä

Tässä tehtävässä käytät oppimaasi luodaksesi oman asiakkaan.

Tässä on palvelin, jota voit käyttää ja johon sinun on soitettava asiakaskoodillasi. Katso, voitko lisätä palvelimeen lisää ominaisuuksia tehdäksesi siitä mielenkiintoisemman.

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

Katso tämä projekti nähdäksesi, kuinka voit [lisätä kehotteita ja resursseja](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Katso myös tämä linkki, kuinka [kutsua kehotteita ja resursseja](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Edellisessä osiossa (../01-first-server) opit luomaan yksinkertaisen MCP-palvelimen Rustilla. Voit jatkaa sen kehittämistä tai katsoa tämän linkin lisätietoja Rust-pohjaisista MCP-palvelinesimerkeistä: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Ratkaisu

**Ratkaisukansio** sisältää täydelliset, valmiit asiakasratkaisut, jotka havainnollistavat kaikkia tämän oppaan käsitteitä. Jokainen ratkaisu sisältää sekä asiakas- että palvelinkoodin, jotka on järjestetty erillisiin, itsenäisiin projekteihin.

### 📁 Ratkaisun rakenne

Ratkaisuhakemisto on järjestetty ohjelmointikielen mukaan:

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

### 🚀 Mitä kukin ratkaisu sisältää

Jokainen kielikohtainen ratkaisu tarjoaa:

- **Täydellisen asiakasratkaisun**, joka sisältää kaikki oppaan ominaisuudet.
- **Toimivan projektirakenteen**, jossa on oikeat riippuvuudet ja konfiguraatiot.
- **Rakennus- ja suorituskomennot** helppoa käyttöönottoa ja suorittamista varten.
- **Yksityiskohtaisen README-tiedoston**, jossa on kielikohtaiset ohjeet.
- **Virheenkäsittely- ja tulosprosessointiesimerkit**.

### 📖 Ratkaisujen käyttö

1. **Siirry haluamasi kielen kansioon**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Noudata README-tiedoston ohjeita** kussakin kansiossa:
   - Asenna riippuvuudet.
   - Rakenna projekti.
   - Suorita asiakas.

3. **Esimerkkituloste**, jonka pitäisi näkyä:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Täydelliset dokumentaatiot ja vaiheittaiset ohjeet löytyvät täältä: **[📖 Ratkaisudokumentaatio](./solution/README.md)**

## 🎯 Täydelliset esimerkit

Olemme tarjonneet täydelliset, toimivat asiakasratkaisut kaikille tämän oppaan käsittelemille ohjelmointikielille. Nämä esimerkit havainnollistavat kaikkia yllä kuvattuja toimintoja ja niitä voidaan käyttää viite- tai lähtökohtana omille projekteillesi.

### Saatavilla olevat täydelliset esimerkit

| Kieli       | Tiedosto                          | Kuvaus                                                                 |
|-------------|-----------------------------------|------------------------------------------------------------------------|
| **Java**    | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Täydellinen Java-asiakas, joka käyttää SSE-siirtoa ja kattavaa virheenkäsittelyä |
| **C#**      | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Täydellinen C#-asiakas, joka käyttää stdio-siirtoa ja automaattista palvelimen käynnistystä |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Täydellinen TypeScript-asiakas, jossa on täysi MCP-protokollatuki |
| **Python**  | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Täydellinen Python-asiakas, joka käyttää async/await-malleja |
| **Rust**    | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Täydellinen Rust-asiakas, joka käyttää Tokio-kirjastoa asynkronisiin operaatioihin |
Jokainen esimerkki sisältää:

- ✅ **Yhteyden muodostaminen** ja virheenkäsittely
- ✅ **Palvelimen etsintä** (työkalut, resurssit, kehotteet, jos sovellettavissa)
- ✅ **Laskinoperaatiot** (lisää, vähennä, kerro, jaa, apu)
- ✅ **Tulosten käsittely** ja muotoiltu tulostus
- ✅ **Kattava virheenkäsittely**
- ✅ **Selkeä, dokumentoitu koodi** vaiheittaisilla kommenteilla

### Aloittaminen täydellisten esimerkkien kanssa

1. **Valitse haluamasi kieli** yllä olevasta taulukosta
2. **Tarkista täydellinen esimerkkitiedosto** ymmärtääksesi koko toteutuksen
3. **Suorita esimerkki** noudattamalla ohjeita tiedostossa [`complete_examples.md`](./complete_examples.md)
4. **Muokkaa ja laajenna** esimerkkiä omaan käyttötarkoitukseesi

Yksityiskohtaiset ohjeet esimerkkien suorittamisesta ja mukauttamisesta löytyvät täältä: **[📖 Täydellisten esimerkkien dokumentaatio](./complete_examples.md)**

### 💡 Ratkaisu vs. Täydelliset esimerkit

| **Ratkaisukansio** | **Täydelliset esimerkit** |
|--------------------|--------------------- |
| Täysi projektirakenne rakennustiedostoilla | Yhden tiedoston toteutukset |
| Valmis suoritettavaksi riippuvuuksien kanssa | Keskittyneet koodiesimerkit |
| Tuotantomainen asennus | Opetuksellinen viite |
| Kieleen liittyvät työkalut | Kielten välinen vertailu |

Molemmat lähestymistavat ovat arvokkaita - käytä **ratkaisukansiota** täydellisiin projekteihin ja **täydellisiä esimerkkejä** oppimiseen ja viitteeksi.

## Keskeiset huomiot

Tämän luvun keskeiset huomiot asiakkaista ovat seuraavat:

- Voidaan käyttää sekä palvelimen ominaisuuksien löytämiseen että niiden käyttämiseen.
- Voi käynnistää palvelimen samalla kun käynnistää itsensä (kuten tässä luvussa), mutta asiakkaat voivat myös muodostaa yhteyden jo käynnissä oleviin palvelimiin.
- Erinomainen tapa testata palvelimen ominaisuuksia vaihtoehtojen, kuten Inspectorin, rinnalla, kuten edellisessä luvussa kuvattiin.

## Lisäresurssit

- [Asiakkaiden rakentaminen MCP:ssä](https://modelcontextprotocol.io/quickstart/client)

## Esimerkit

- [Java-laskin](../samples/java/calculator/README.md)
- [.Net-laskin](../../../../03-GettingStarted/samples/csharp)
- [JavaScript-laskin](../samples/javascript/README.md)
- [TypeScript-laskin](../samples/typescript/README.md)
- [Python-laskin](../../../../03-GettingStarted/samples/python)
- [Rust-laskin](../../../../03-GettingStarted/samples/rust)

## Mitä seuraavaksi

- Seuraavaksi: [Asiakkaan luominen LLM:n avulla](../03-llm-client/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.