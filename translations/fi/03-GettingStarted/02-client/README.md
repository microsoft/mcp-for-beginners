# Asiakkaan luominen

Asiakkaat ovat räätälöityjä sovelluksia tai skriptejä, jotka kommunikoivat suoraan MCP-palvelimen kanssa pyytääkseen resursseja, työkaluja ja kehotteita. Toisin kuin tarkastustyökalun käyttäminen, joka tarjoaa graafisen käyttöliittymän palvelimen kanssa vuorovaikutukseen, oman asiakkaan kirjoittaminen mahdollistaa ohjelmalliset ja automatisoidut toiminnot. Tämä antaa kehittäjille mahdollisuuden integroida MCP-ominaisuuksia omiin työnkulkuihinsa, automatisoida tehtäviä ja rakentaa erityistarpeisiin räätälöityjä ratkaisuja.

## Yleiskatsaus

Tämä oppitunti esittelee asiakkaiden käsitteen Model Context Protocol (MCP) -ekosysteemissä. Opit kirjoittamaan oman asiakkaan ja liittämään sen MCP-palvelimeen.

## Oppimistavoitteet

Tämän oppitunnin lopuksi osaat:

- Ymmärtää, mitä asiakas voi tehdä.
- Kirjoittaa oman asiakkaan.
- Yhdistää ja testata asiakasta MCP-palvelimen kanssa varmistaaksesi, että palvelin toimii odotetusti.

## Mitä asiakkaan kirjoittamiseen kuuluu?

Asiakkaan kirjoittamiseksi sinun tulee tehdä seuraavat asiat:

- **Tuoda oikeat kirjastot**. Käytät samaa kirjastoa kuin aiemmin, mutta erilaisia rakenteita.
- **Ilmentää asiakas**. Tämä sisältää asiakkaan instanssin luomisen ja sen liittämisen valittuun siirtomenetelmään.
- **Päättää, mitä resursseja listataan**. MCP-palvelimellasi on resursseja, työkaluja ja kehotteita, sinun täytyy päättää, mitä niistä listataan.
- **Integroida asiakas isäntäohjelmaan**. Kun tiedät palvelimen ominaisuudet, sinun tulee integroida tämä isäntäohjelmaasi niin, että jos käyttäjä kirjoittaa kehotteen tai muun komennon, vastaava palvelimen toiminto kutsutaan.

Nyt kun ymmärrämme yleisellä tasolla, mitä olemme tekemässä, katsotaan seuraavaksi esimerkkiä.

### Esimerkki asiakkaasta

Katsotaan tätä esimerkkiasiakasta:

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

// Listaa kehotteet
const prompts = await client.listPrompts();

// Hae kehote
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Listaa resurssit
const resources = await client.listResources();

// Lue resurssi
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kutsu työkalua
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Edellisessä koodissa me:

- Tuomme kirjastot
- Luomme asiakkaan instanssin ja yhdistämme sen käyttämällä stdio-siirtoa.
- Listaamme kehotteet, resurssit ja työkalut ja kutsumme niitä kaikkia.

Siinä se, asiakas, joka voi keskustella MCP-palvelimen kanssa.

Käydään seuraavassa harjoitustehtävässä rauhassa läpi kukin koodinpätkä ja selitetään, mitä tapahtuu.

## Harjoitus: Asiakkaan kirjoittaminen

Kuten edellä mainittiin, otetaan aikaa koodin selittämiseen, ja voit ehdottomasti koodata mukana, jos haluat.

### -1- Kirjastojen tuonti

Tuodaan tarvitsemamme kirjastot, tarvitsemme viitteet asiakkaaseen ja valittuun siirtoprotokollaan, stdio. stdio on protokolla paikallisella koneella ajettaville asioille. SSE on toinen siirtoprotokolla, jota esitämme tulevissa luvuissa, mutta se on toinen vaihtoehtosi. Nyt jatketaan kuitenkin stdio:n kanssa.

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

Javalla luot asiakkaan, joka yhdistyy MCP-palvelimeen edellisestä harjoituksesta. Käyttäen samaa Java Spring Boot -projektirakennetta kuin [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) -osiossa, luo uusi Java-luokka nimeltä `SDKClient` kansioon `src/main/java/com/microsoft/mcp/sample/client/` ja lisää seuraavat importit:

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

Sinun täytyy lisätä seuraavat riippuvuudet `Cargo.toml`-tiedostoosi.

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

Tästä voit tuoda tarvittavat kirjastot asiakkaasi koodiin.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Siirrytään instansointiin.

### -2- Asiakkaan ja siirron instansointi

Meidän täytyy luoda instanssit siirrolle ja asiakkaalle:

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

Edellisessä koodissa me:

- Loimme stdio-siirto-instanssin. Huomaa, miten se määrittää komennon ja argumentit palvelimen löytämiseksi ja käynnistämiseksi, koska se on asia, jonka meidän täytyy tehdä kirjoittaessamme asiakasta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Ilmestyimme asiakkaan antamalla sille nimen ja version.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Yhdistimme asiakkaan valittuun siirtoon.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Luo palvelimen parametrit stdio-yhteydelle
server_params = StdioServerParameters(
    command="mcp",  # Suoritettava tiedosto
    args=["run", "server.py"],  # Valinnaiset komentoriviparametrit
    env=None,  # Valinnaiset ympäristömuuttujat
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Alusta yhteys
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Edellisessä koodissa me:

- Toimme tarvittavat kirjastot
- Instansioimme palvelimen parametrien olion, koska käytämme sitä palvelimen ajamiseksi, jotta voimme yhdistää siihen asiakkaalla.
- Määrittelimme metodin `run`, joka puolestaan kutsuu `stdio_client`-funktiota, joka käynnistää asiakassession.
- Loimme sisäänkäyntipisteen, jossa annamme `run`-metodin `asyncio.run`-funktiolle.

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

Edellisessä koodissa me:

- Toimme tarvittavat kirjastot.
- Loimme stdio-siirron ja asiakkaan `mcpClient`. Tätä käytämme työkalujen listaamiseen ja käynnistämiseen MCP-palvelimella.

Huomaa, että "Arguments"-kentässä voit osoittaa joko *.csproj*-tiedostoon tai suoritettavaan tiedostoon.

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
        
        // Asiakaslogiikkasi menee tähän
    }
}
```

Edellisessä koodissa me:

- Loimme päämetodin, joka asettaa SSE-siirron osoittamaan `http://localhost:8080`-osoitteeseen, missä MCP-palvelimemme toimii.
- Loimme asiakkaan luokan, joka ottaa siirron konstruktoriparametrina.
- `run`-metodissa loimme synkronisen MCP-asiakkaan käyttäen siirtoa ja alustimme yhteyden.
- Käytimme SSE (Server-Sent Events) siirtoa, joka soveltuu HTTP-pohjaisiin yhteyksiin Java Spring Boot MCP-palvelimien kanssa.

#### Rust

Huomaa, että tämä Rust-asiakas olettaa palvelimen olevan samaan hakemistoon sijoittuva sisaraprojekti nimeltä "calculator-server". Alla oleva koodi käynnistää palvelimen ja yhdistää siihen.

```rust
async fn main() -> Result<(), RmcpError> {
    // Oleta, että palvelin on samaan hakemistoon sijoitettu sisarprojekti nimeltä "calculator-server"
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

    // TODO: Alusta

    // TODO: Listaa työkalut

    // TODO: Kutsu add-työkalu argumenteilla = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Palvelimen ominaisuuksien listaaminen

Nyt meillä on asiakas, joka voi yhdistää, jos ohjelma ajetaan. Kuitenkaan se ei vielä listaa ominaisuuksiaan, tehdään se seuraavaksi:

#### TypeScript

```typescript
// Luo kehotteita
const prompts = await client.listPrompts();

// Luo resursseja
const resources = await client.listResources();

// luo työkaluja
const tools = await client.listTools();
```

#### Python

```python
# Listaa käytettävissä olevat resurssit
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Listaa käytettävissä olevat työkalut
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Tässä listaamme saatavilla olevat resurssit `list_resources()` ja työkalut `list_tools` ja tulostamme ne.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Yllä esimerkki, miten voimme listata työkalut palvelimella. Jokaiselle työkalulle tulostamme sen nimen.

#### Java

```java
// Luettele ja esittele työkalut
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Voit myös pingata palvelinta yhteyden varmistamiseksi
client.ping();
```

Edellisessä koodissa me:

- Kutsumme `listTools()` saadaksemme kaikki saatavilla olevat työkalut MCP-palvelimelta.
- Käytämme `ping()` vahvistaaksemme, että palvelimeen yhdistäminen toimii.
- `ListToolsResult` sisältää tietoa kaikista työkaluista, mukaan lukien nimet, kuvaukset ja syöttökaaviot.

Hienoa, nyt olemme saaneet kaikki ominaisuudet talteen. Kysymys on, milloin käytämme niitä? Tämä asiakas on melko yksinkertainen siinä mielessä, että meidän täytyy nimenomaan kutsua ominaisuudet, kun haluamme niitä. Seuraavassa luvussa luomme edistyneemmän asiakkaan, jolla on käytössään oma suuri kielimalli, LLM. Nyt kuitenkin katsotaan, miten voimme kutsua palvelimen ominaisuuksia:

#### Rust

Pääfunktiossa, kun asiakas on alustettu, voimme alustaa palvelimen ja listata joitakin sen ominaisuuksia.

```rust
// Alusta
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Listaa työkalut
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Ominaisuuksien kutsuminen

Ominaisuuksien kutsumiseen meidän täytyy varmistaa, että määrittelemme oikeat argumentit ja joissakin tapauksissa nimen sille, mitä yritämme kutsua.

#### TypeScript

```typescript

// Lue resurssi
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kutsu työkalua
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// kutsu kehotetta
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Edellisessä koodissa me:

- Luemme resurssin, kutsumme resurssia `readResource()`-metodilla ja määritämme `uri`. Tässä miten palvelin todennäköisesti käsittelee sen:

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

    Arvomme `uri` `file://example.txt` vastaa palvelimen `file://{name}` mallia. `example.txt` sovitetaan `name`-arvoksi.

- Kutsumme työkalua, määrittelemme sen `name` ja `arguments` näin:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Haemme kehotteen, kutsumme `getPrompt()` metodilla, jolla annamme `name` ja `arguments`. Palvelin näyttää tältä:

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

    ja siitä syntyy lopullinen koodi asiakkaallasi, vastaamaan palvelimella määriteltyä:

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
# Lue resurssi
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Kutsu työkalua
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Edellisessä koodissa me:

- Kutsumme resurssia nimeltä `greeting` käyttäen `read_resource`.
- Käytämme työkalua nimeltä `add` kutsumalla `call_tool`.

#### .NET

1. Lisätään koodia työkalun kutsumiseen:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Tulostetaan tulos, tässä koodi sen käsittelyyn:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Kutsu erilaisia laskutyökaluja
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

Edellisessä koodissa me:

- Kutsumme useita laskutyökaluja käyttämällä `callTool()`-metodia `CallToolRequest` -objektien kanssa.
- Jokainen työkalu määrittelee työkalun nimen ja tarvittavien argumenttien `Map`-kartan.
- Palvelimen työkalut odottavat tiettyjä parametrien nimiä (kuten "a", "b" matemaattisissa laskutoimituksissa).
- Tulokset palautetaan `CallToolResult`-objekteina, jotka sisältävät palvelimen vastauksen.

#### Rust

```rust
// Kutsu lisää työkalu argumenteilla = {"a": 3, "b": 2}
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

### -5- Asiakkaan ajo

Asiakkaan ajamiseksi kirjoita seuraava komento terminaaliin:

#### TypeScript

Lisää seuraava merkintä "scripts"-osioon tiedostossa *package.json*:

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

Varmista ensin, että MCP-palvelimesi on käynnissä osoitteessa `http://localhost:8080`. Sitten aja asiakas:

```bash
# Käännä projektisi
./mvnw clean compile

# Suorita asiakasohjelma
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Vaihtoehtoisesti voit ajaa täydellisen asiakasprojektin, joka on mukana ratkaisukansiossa `03-GettingStarted\02-client\solution\java`:

```bash
# Siirry ratkaisuhakemistoon
cd 03-GettingStarted/02-client/solution/java

# Käännä ja suorita JAR-tiedosto
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Tehtävä

Tässä tehtävässä käytät oppimaasi asiakkaan luomiseksi, mutta luot oman asiakkaan.

Tässä on palvelin, jota voit käyttää ja johon sinun täytyy kutsua asiakaskoodillasi. Katso, voitko lisätä palvelimeen lisää ominaisuuksia tehdäkseen siitä kiinnostavamman.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Luo MCP-palvelin
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Lisää lisäystyökalu
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lisää dynaaminen tervehdysresurssi
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

// Aloita viestien vastaanotto stdin:stä ja viestien lähetys stdout:iin

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

# Luo MCP-palvelimen
mcp = FastMCP("Demo")


# Lisää lisäystyökalu
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Lisää dynaaminen tervehdysresurssi
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

Tarkista myös tämä linkki siitä, miten kutsua [kehotteita ja resursseja](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Edellisessä osassa [previous section](../../../../03-GettingStarted/01-first-server) opit, miten luodaan yksinkertainen MCP-palvelin Rustilla. Voit jatkaa sen rakentamista tai tarkistaa nämä Rust-pohjaiset MCP-palvelin-esimerkit: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Ratkaisu

**Ratkaisukansio** sisältää valmiit, ajettavat asiakasimplementaatiot, jotka demonstroivat kaikkia tässä opetusohjelmassa käsiteltyjä konsepteja. Jokainen ratkaisu sisältää sekä asiakas- että palvelinkoodin erillisissä, itsenäisissä projekteissa.

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

Kunkin kielikohtainen ratkaisu sisältää:

- **Täydellisen asiakasimplementaation**, jossa ovat kaikki opetusohjelman toiminnot
- **Toimivan projektirakenteen** oikeilla riippuvuuksilla ja konfiguraatiolla
- **Käännä ja aja -skriptit** helppoa käyttöönottoa ja suorittamista varten
- **Yksityiskohtaisen README-tiedoston** kielikohtaisilla ohjeilla
- **Virheenkäsittelyn** ja tulosten käsittelyn esimerkit

### 📖 Ratkaisujen käyttäminen

1. **Siirry haluamaasi kielikansioon**:

   ```bash
   cd solution/typescript/    # TypeScriptille
   cd solution/java/          # Javalle
   cd solution/python/        # Pythonille
   cd solution/dotnet/        # .NET:lle
   ```

2. **Noudata kunkin kansion README-ohjeita**:
   - Riippuvuuksien asentamiseen
   - Projektin kääntämiseen
   - Asiakkaan suorittamiseen

3. **Esimerkkituloste**, jonka näet:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Täydelliseen dokumentaatioon ja vaiheittaiseen opastukseen tutustu: **[📖 Ratkaisudokumentaatio](./solution/README.md)**

## 🎯 Täydelliset esimerkit

Olemme toimittaneet täydelliset ja toimivat asiakasimplementaatiot kaikilla tässä opetusohjelmassa käsitellyillä ohjelmointikielillä. Nämä esimerkit demonstroivat edellä kuvatun koko toiminnallisuuden ja niitä voi käyttää viitteinä tai lähtökohtina omille projekteillesi.

### Saatavilla olevat täydelliset esimerkit

| Kieli    | Tiedosto                      | Kuvaus                                                          |
|----------|-------------------------------|-----------------------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Täydellinen Java-asiakas SSE-siirrolla, sisältäen kattavan virheenkäsittelyn |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Täydellinen C#-asiakas stdio-siirrolla, joka käynnistää palvelimen automaattisesti |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Täydellinen TypeScript-asiakas, joka tukee MCP-protokollaa kokonaisuudessaan |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Täydellinen Python-asiakas, joka käyttää async/await -kuvioita |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Täydellinen Rust-asiakas, joka käyttää Tokio-kirjastoa asynkronisiin operaatioihin |

Jokainen täydellinen esimerkki sisältää:
- ✅ **Yhteyden muodostaminen** ja virheiden käsittely
- ✅ **Palvelimen löytäminen** (työkalut, resurssit, kehotteet tarvittaessa)
- ✅ **Laskinoperaatiot** (yhteenlasku, vähennyslasku, kertolasku, jakolasku, apu)
- ✅ **Tulosten käsittely** ja muotoiltu tulostus
- ✅ **Kattava virheiden käsittely**
- ✅ **Selkeä, dokumentoitu koodi** vaiheittaisilla kommenteilla

### Aloittaminen täydellisten esimerkkien avulla

1. **Valitse haluamasi kieli** yllä olevasta taulukosta
2. **Tutustu täydelliseen esimerkkitiedostoon** ymmärtääksesi koko toteutus
3. **Suorita esimerkki** noudattamalla ohjeita tiedostossa [`complete_examples.md`](./complete_examples.md)
4. **Muokkaa ja laajenna** esimerkkiä omaa käyttötarkoitustasi varten

Yksityiskohtaista dokumentaatiota esimerkkien suorittamisesta ja muokkaamisesta löydät: **[📖 Täydellisten esimerkkien dokumentaatio](./complete_examples.md)**

### 💡 Ratkaisu vs. täydelliset esimerkit

| **Ratkaisukansio** | **Täydelliset esimerkit** |
|--------------------|------------------------- |
| Kokonaisrakenne projektille rakennustiedostoineen | Yksittäisen tiedoston toteutuksia |
| Valmis ajettavaksi riippuvuuksineen | Keskittyneet koodiesimerkit |
| Tuotantoluokan ympäristö | Opetuksellinen viite |
| Kielikohtaiset työkalut | Kielten välinen vertailu |

Molemmat lähestymistavat ovat hyödyllisiä – käytä **ratkaisukansiota** kokonaisiin projekteihin ja **täydellisiä esimerkkejä** oppimiseen ja vertailuun.

## Tärkeimmät opit

Tämän luvun tärkeimmät opit client-sovelluksista:

- Niillä voidaan sekä löytää että kutsua palvelimen ominaisuuksia.
- Ne voivat käynnistää palvelimen samalla kun itse käynnistyvät (kuten tässä luvussa), mutta clientit voivat myös yhdistää jo käynnissä oleviin palvelimiin.
- Ne ovat loistava tapa testata palvelimen toiminnallisuuksia vaihtoehtojen, kuten Inspectorin, rinnalla kuten edellisessä luvussa kuvattiin.

## Lisäresurssit

- [Clientien rakentaminen MCP:ssä](https://modelcontextprotocol.io/quickstart/client)

## Näytteitä

- [Java-laskin](../samples/java/calculator/README.md)
- [.Net-laskin](../../../../03-GettingStarted/samples/csharp)
- [JavaScript-laskin](../samples/javascript/README.md)
- [TypeScript-laskin](../samples/typescript/README.md)
- [Python-laskin](../../../../03-GettingStarted/samples/python)
- [Rust-laskin](../../../../03-GettingStarted/samples/rust)

## Mitä seuraavaksi

- Seuraavaksi: [Clientin luominen LLM:n kanssa](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä asioissa suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa mistään väärinymmärryksistä tai tulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->