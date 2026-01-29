# MCP-palvelin stdio-kuljetuksella

> **⚠️ Tärkeä päivitys**: MCP-määrittelyn 2025-06-18 mukaan itsenäinen SSE (Server-Sent Events) -kuljetus on **poistettu käytöstä** ja korvattu "Streamable HTTP" -kuljetuksella. Nykyinen MCP-määrittely määrittelee kaksi ensisijaista kuljetusmekanismia:
> 1. **stdio** - Vakiosyöttö/-tulostus (suositeltu paikallisille palvelimille)
> 2. **Streamable HTTP** - Etäpalvelimille, jotka voivat käyttää sisäisesti SSE:tä
>
> Tämä oppitunti on päivitetty keskittymään **stdio-kuljetukseen**, joka on suositeltu lähestymistapa useimmille MCP-palvelinratkaisuille.

Stdio-kuljetus mahdollistaa MCP-palvelimien ja asiakkaiden välisen viestinnän vakiosyöttö- ja tulostusvirtojen kautta. Tämä on nykyisen MCP-määrittelyn yleisimmin käytetty ja suositeltu kuljetusmekanismi, joka tarjoaa yksinkertaisen ja tehokkaan tavan rakentaa MCP-palvelimia, jotka voidaan helposti integroida eri asiakassovelluksiin.

## Yleiskatsaus

Tämä oppitunti käsittelee MCP-palvelimien rakentamista ja käyttämistä stdio-kuljetuksen avulla.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Rakentaa MCP-palvelimen stdio-kuljetusta käyttäen.
- Vianmäärittää MCP-palvelimen Inspectorin avulla.
- Käyttää MCP-palvelinta Visual Studio Codessa.
- Ymmärtää nykyiset MCP-kuljetusmekanismit ja miksi stdio on suositeltu.

## Stdio-kuljetus – Miten se toimii

Stdio-kuljetus on yksi kahdesta tuetusta kuljetustyypistä nykyisessä MCP-määrittelyssä (2025-06-18). Näin se toimii:

- **Yksinkertainen viestintä**: Palvelin lukee JSON-RPC-viestejä vakiosyötöstä (`stdin`) ja lähettää viestejä vakio-tulostukseen (`stdout`).
- **Prosessipohjainen**: Asiakas käynnistää MCP-palvelimen aliprosessina.
- **Viestimuoto**: Viestit ovat yksittäisiä JSON-RPC-pyyntöjä, ilmoituksia tai vastauksia, jotka erotetaan rivinvaihdolla.
- **Lokitus**: Palvelin VOI kirjoittaa UTF-8-merkkijonoja vakio-virheeseen (`stderr`) lokitusta varten.

### Keskeiset vaatimukset:
- Viestit TÄYTYY erottaa rivinvaihdolla, eikä niissä SAA olla sisäisiä rivinvaihtoja.
- Palvelin EI SAA kirjoittaa mitään `stdout`-virtaan, mikä ei ole kelvollinen MCP-viesti.
- Asiakas EI SAA kirjoittaa mitään palvelimen `stdin`-virtaan, mikä ei ole kelvollinen MCP-viesti.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

Edellisessä koodissa:

- Tuomme `Server`-luokan ja `StdioServerTransport`-kuljetuksen MCP SDK:sta.
- Luomme palvelininstanssin peruskonfiguraatiolla ja ominaisuuksilla.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Edellisessä koodissa:

- Luomme palvelininstanssin MCP SDK:ta käyttäen.
- Määrittelemme työkalut koristeiden avulla.
- Käytämme stdio_server-kontekstinhallintaa kuljetuksen käsittelyyn.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Keskeinen ero SSE:hen verrattuna on, että stdio-palvelimet:

- Eivät vaadi verkkopalvelimen asennusta tai HTTP-päätepisteitä.
- Käynnistetään asiakasohjelman aliprosesseina.
- Viestivät stdin/stdout-virtojen kautta.
- Ovat yksinkertaisempia toteuttaa ja vianmäärittää.

## Harjoitus: Stdio-palvelimen luominen

Palvelimen luomisessa on huomioitava kaksi asiaa:

- Meidän täytyy käyttää verkkopalvelinta päätepisteiden ja viestien tarjoamiseen.

## Lab: Yksinkertaisen MCP stdio-palvelimen luominen

Tässä laboratoriossa luomme yksinkertaisen MCP-palvelimen käyttäen suositeltua stdio-kuljetusta. Tämä palvelin tarjoaa työkaluja, joita asiakkaat voivat kutsua standardin Model Context Protocolin avulla.

### Esivaatimukset

- Python 3.8 tai uudempi
- MCP Python SDK: `pip install mcp`
- Perustiedot asynkronisesta ohjelmoinnista

Aloitetaan ensimmäisen MCP stdio-palvelimen luomisella:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Keskeiset erot vanhentuneeseen SSE-lähestymistapaan

**Stdio-kuljetus (nykyinen standardi):**
- Yksinkertainen aliprosessimalli – asiakas käynnistää palvelimen lapsiprosessina.
- Viestintä stdin/stdout:n kautta JSON-RPC-viesteillä.
- Ei vaadi HTTP-palvelimen asennusta.
- Parempi suorituskyky ja turvallisuus.
- Helpompi vianmäärittää ja kehittää.

**SSE-kuljetus (poistettu käytöstä MCP 2025-06-18):**
- Vaati HTTP-palvelimen SSE-päätepisteillä.
- Monimutkaisempi asennus verkkopalvelininfrastruktuurin kanssa.
- Lisäturvahuomioita HTTP-päätepisteille.
- Korvattu Streamable HTTP:llä verkkopohjaisiin skenaarioihin.

### Palvelimen luominen stdio-kuljetuksella

Stdio-palvelimen luomiseksi meidän täytyy:

1. **Tuoda tarvittavat kirjastot** – Tarvitsemme MCP-palvelinkomponentit ja stdio-kuljetuksen.
2. **Luoda palvelininstanssi** – Määritellä palvelin sen ominaisuuksilla.
3. **Määritellä työkalut** – Lisätä haluttu toiminnallisuus.
4. **Asettaa kuljetus** – Konfiguroida stdio-viestintä.
5. **Käynnistää palvelin** – Käynnistää palvelin ja käsitellä viestit.

Rakennetaan tämä vaihe vaiheelta:

### Vaihe 1: Luo perus stdio-palvelin

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Vaihe 2: Lisää lisää työkaluja

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Vaihe 3: Palvelimen käynnistäminen

Tallenna koodi tiedostoon `server.py` ja suorita se komentoriviltä:

```bash
python server.py
```

Palvelin käynnistyy ja odottaa syötettä stdin:stä. Se viestii JSON-RPC-viesteillä stdio-kuljetuksen kautta.

### Vaihe 4: Testaus Inspectorilla

Voit testata palvelintasi MCP Inspectorilla:

1. Asenna Inspector: `npx @modelcontextprotocol/inspector`
2. Käynnistä Inspector ja osoita se palvelimeesi.
3. Testaa luomiasi työkaluja.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Stdio-palvelimen vianmääritys

### MCP Inspectorin käyttö

MCP Inspector on arvokas työkalu MCP-palvelimien vianmääritykseen ja testaukseen. Näin käytät sitä stdio-palvelimen kanssa:

1. **Asenna Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käynnistä Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testaa palvelinta**: Inspector tarjoaa verkkokäyttöliittymän, jossa voit:
   - Tarkastella palvelimen ominaisuuksia.
   - Testata työkaluja eri parametreilla.
   - Seurata JSON-RPC-viestejä.
   - Vianmäärittää yhteysongelmia.

### VS Coden käyttö

Voit myös vianmäärittää MCP-palvelintasi suoraan VS Codessa:

1. Luo käynnistyskonfiguraatio tiedostoon `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Aseta katkaisupisteitä palvelinkoodiin.
3. Käynnistä debuggeri ja testaa Inspectorilla.

### Yleisiä vianmääritysvinkkejä

- Käytä `stderr`-virtaa lokitukseen – älä koskaan kirjoita `stdout`-virtaan, sillä se on varattu MCP-viesteille.
- Varmista, että kaikki JSON-RPC-viestit ovat rivinvaihdolla erotettuja.
- Testaa ensin yksinkertaisia työkaluja ennen monimutkaisen toiminnallisuuden lisäämistä.
- Käytä Inspectoria viestimuotojen tarkistamiseen.

## Stdio-palvelimen käyttäminen VS Codessa

Kun olet rakentanut MCP stdio-palvelimen, voit integroida sen VS Codeen ja käyttää sitä Clauden tai muiden MCP-yhteensopivien asiakkaiden kanssa.

### Konfiguraatio

1. **Luo MCP-konfiguraatiotiedosto** sijaintiin `%APPDATA%\Claude\claude_desktop_config.json` (Windows) tai `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Käynnistä Claude uudelleen**: Sulje ja avaa Claude uudelleen ladataksesi uuden palvelinkonfiguraation.

3. **Testaa yhteyttä**: Aloita keskustelu Clauden kanssa ja kokeile palvelimesi työkaluja:
   - "Voitko tervehtiä minua tervehdystyökalulla?"
   - "Laske 15 ja 27 summa."
   - "Mikä on palvelimen tiedot?"

### TypeScript stdio-palvelimen esimerkki

Tässä täydellinen TypeScript-esimerkki viitteeksi:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio-palvelimen esimerkki

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Yhteenveto

Tässä päivitetty oppitunnissa opit:

- Rakentamaan MCP-palvelimia nykyisellä **stdio-kuljetuksella** (suositeltu lähestymistapa).
- Ymmärtämään, miksi SSE-kuljetus poistettiin käytöstä stdio:n ja Streamable HTTP:n hyväksi.
- Luomaan työkaluja, joita MCP-asiakkaat voivat kutsua.
- Vianmäärittämään palvelintasi MCP Inspectorilla.
- Integroimaan stdio-palvelimesi VS Codeen ja Claudeen.

Stdio-kuljetus tarjoaa yksinkertaisemman, turvallisemman ja suorituskykyisemmän tavan rakentaa MCP-palvelimia verrattuna vanhentuneeseen SSE-lähestymistapaan. Se on suositeltu kuljetus useimmille MCP-palvelinratkaisuille MCP-määrittelyn 2025-06-18 mukaan.

### .NET

1. Luodaan ensin joitakin työkaluja, tätä varten luomme tiedoston *Tools.cs* seuraavalla sisällöllä:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjoitus: Stdio-palvelimen testaus

Nyt kun olet rakentanut stdio-palvelimesi, testataan sen toimivuus.

### Esivaatimukset

1. Varmista, että MCP Inspector on asennettu:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Palvelinkoodisi tulisi olla tallennettuna (esim. `server.py`).

### Testaus Inspectorilla

1. **Käynnistä Inspector palvelimesi kanssa**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Avaa verkkokäyttöliittymä**: Inspector avaa selaimen ikkunan, jossa näkyvät palvelimesi ominaisuudet.

3. **Testaa työkaluja**: 
   - Kokeile `get_greeting`-työkalua eri nimillä.
   - Testaa `calculate_sum`-työkalua eri numeroilla.
   - Kutsu `get_server_info`-työkalua nähdäksesi palvelimen metadataa.

4. **Seuraa viestintää**: Inspector näyttää JSON-RPC-viestit, joita asiakas ja palvelin vaihtavat.

### Mitä sinun pitäisi nähdä

Kun palvelimesi käynnistyy oikein, näet:
- Palvelimen ominaisuudet listattuna Inspectorissa.
- Työkalut testattavissa.
- Onnistuneet JSON-RPC-viestinvaihdot.
- Työkalujen vastaukset käyttöliittymässä.

### Yleisiä ongelmia ja ratkaisuja

**Palvelin ei käynnisty:**
- Tarkista, että kaikki riippuvuudet on asennettu: `pip install mcp`.
- Varmista Python-syntaksi ja sisennys.
- Etsi virheilmoituksia konsolista.

**Työkalut eivät näy:**
- Varmista, että `@server.tool()`-koristeet ovat käytössä.
- Tarkista, että työkalufunktiot on määritelty ennen `main()`-funktiota.
- Varmista, että palvelin on oikein konfiguroitu.

**Yhteysongelmat:**
- Varmista, että palvelin käyttää stdio-kuljetusta oikein.
- Tarkista, ettei muut prosessit häiritse.
- Varmista Inspector-komennon syntaksi.

## Tehtävä

Kokeile laajentaa palvelintasi lisäämällä ominaisuuksia. Katso [tämä sivu](https://api.chucknorris.io/) ja lisää esimerkiksi työkalu, joka kutsuu API:ta. Päätä itse, miltä palvelimen tulisi näyttää. Pidä hauskaa :)

## Ratkaisu

[Ratkaisu](./solution/README.md) Tässä mahdollinen ratkaisu toimivalla koodilla.

## Keskeiset opit

Tämän luvun keskeiset opit ovat seuraavat:

- Stdio-kuljetus on suositeltu mekanismi paikallisille MCP-palvelimille.
- Stdio-kuljetus mahdollistaa saumattoman viestinnän MCP-palvelimien ja asiakkaiden välillä vakiosyöttö- ja tulostusvirtojen avulla.
- Voit käyttää sekä Inspectoria että Visual Studio Codea stdio-palvelimien suoraan käyttämiseen, mikä tekee vianmäärityksestä ja integroinnista yksinkertaista.

## Esimerkit 

- [Java-laskin](../samples/java/calculator/README.md)
- [.Net-laskin](../../../../03-GettingStarted/samples/csharp)
- [JavaScript-laskin](../samples/javascript/README.md)
- [TypeScript-laskin](../samples/typescript/README.md)
- [Python-laskin](../../../../03-GettingStarted/samples/python) 

## Lisäresurssit

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mitä seuraavaksi

## Seuraavat askeleet

Nyt kun olet oppinut rakentamaan MCP-palvelimia stdio-kuljetuksella, voit tutkia edistyneempiä aiheita:

- **Seuraavaksi**: [HTTP Streaming MCP:n kanssa (Streamable HTTP)](../06-http-streaming/README.md) – Opi toinen tuettu kuljetusmekanismi etäpalvelimille.
- **Edistynyt**: [MCP:n turvallisuuden parhaat käytännöt](../../02-Security/README.md) – Toteuta turvallisuus MCP-palvelimissasi.
- **Tuotanto**: [Julkaisustrategiat](../09-deployment/README.md) – Julkaise palvelimesi tuotantokäyttöön.

## Lisäresurssit

- [MCP-määrittely 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Virallinen määrittely.
- [MCP SDK -dokumentaatio](https://github.com/modelcontextprotocol/sdk) – SDK-viitteet kaikille kielille.
- [Yhteisön esimerkit](../../06-CommunityContributions/README.md) – Lisää palvelinesimerkkejä yhteisöltä.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.