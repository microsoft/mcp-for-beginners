# MCP-palvelin stdio-siirrolla

> **⚠️ Tärkeä päivitys**: MCP-spesifikaation 2025-06-18 julkaisusta lähtien erillinen SSE (Server-Sent Events) -siirto on **poistettu käytöstä** ja korvattu "Streamable HTTP" -siirrolla. Nykyinen MCP-spesifikaatio määrittelee kaksi pääasiallista siirtomekanismia:
> 1. **stdio** - standardisyöte/ -tuloste (suositeltu paikallisille palvelimille)
> 2. **Streamable HTTP** - etäpalvelimille, jotka voivat käyttää SSE:tä sisäisesti
>
> Tämä oppitunti on päivitetty keskittymään **stdio-siirtoon**, joka on suositeltu lähestymistapa useimmissa MCP-palvelinimplementaatioissa.

Stdio-siirto sallii MCP-palvelinten kommunikoida asiakkaiden kanssa standardisyötteen ja -tulosteen kautta. Tämä on yleisimmin käytetty ja suositeltu siirtomekanismi nykyisessä MCP-spesifikaatiossa, tarjoten yksinkertaisen ja tehokkaan tavan rakentaa MCP-palvelimia, jotka voidaan helposti integroida erilaisiin asiakasohjelmiin.

## Yleiskatsaus

Tämä oppitunti kattaa, kuinka rakentaa ja käyttää MCP-palvelimia stdio-siirrolla.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Rakentaa MCP-palvelimen stdio-siirtoa käyttäen.
- Debugata MCP-palvelinta Inspectorilla.
- Käyttää MCP-palvelinta Visual Studio Codessa.
- Ymmärtää nykyiset MCP-siirtomekanismit ja miksi stdio on suositeltu.

## stdio-siirto – Kuinka se toimii

Stdio-siirto on yksi kahdesta nykyisen MCP-spesifikaation (2025-06-18) tukemasta siirtotyypistä. Näin se toimii:

- **Yksinkertainen kommunikaatio**: Palvelin lukee JSON-RPC-viestejä standardisyötteestä (`stdin`) ja lähettää viestejä standarditulosteeseen (`stdout`).
- **Prosessipohjainen**: Asiakas käynnistää MCP-palvelimen ali\-prosessina.
- **Viestimuoto**: Viestit ovat yksittäisiä JSON-RPC-pyyntöjä, ilmoituksia tai vastauksia, rajattu rivinvaihdoilla.
- **Lokitus**: Palvelin VOI kirjoittaa UTF-8-merkkijonoja standardivirhevirtaukseen (`stderr`) lokitusta varten.

### Tärkeimmät vaatimukset:
- Viestien TÄYTYY olla rivinvaihdoilla rajattuja eivätkä SISÄLLÄ rivinvaihtoja
- Palvelin EI SAA kirjoittaa `stdout`-virtaan mitään, mikä ei ole kelvollinen MCP-viesti
- Asiakas EI SAA kirjoittaa palvelimen `stdin`-virtaan mitään, mikä ei ole kelvollinen MCP-viesti

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

Edellisessä koodissa:

- Tuodaan `Server`-luokka ja `StdioServerTransport` MCP-SDK:sta
- Luodaan palvelininstanssi peruskonfiguraatiolla ja -kapasiteeteilla
- Luodaan `StdioServerTransport` -instanssi ja yhdistetään palvelin siihen, mahdollistaen viestinnän stdin/stdoutia pitkin

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Luo palvelininstanssi
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

Edellisessä koodissa me:

- Luodaan palvelininstanssi MCP-SDK:lla
- Määritellään työkalut koristeiden avulla
- Käytetään stdio_server-context manageria siirron käsittelyyn

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Keskeinen ero SSE:hen on, että stdio-palvelimet:

- Eivät vaadi web-palvelinasetusta tai HTTP-endpointteja
- Käynnistetään ali\-prosesseina asiakkaan toimesta
- Kommunikoivat stdin/stdout-virtauksia pitkin
- Ovat helpompia toteuttaa ja debugata

## Tehtävä: Luodaan stdio-palvelin

Palvelinta tehdessämme meidän tulee pitää mielessä kaksi asiaa:

- Meidän tulee käyttää web-palvelinta endpointien tarjoamiseen yhteyttä varten.

## Harjoitus: Luodaan yksinkertainen MCP stdio-palvelin

Tässä harjoituksessa luomme yksinkertaisen MCP-palvelimen käyttäen suositeltua stdio-siirtoa. Tämä palvelin tarjoaa työkaluja, joita asiakkaat voivat kutsua standardin Model Context Protocol -protokollan kautta.

### Esivaatimukset

- Python 3.8 tai uudempi
- MCP Python SDK: `pip install mcp`
- Perustiedot asynkronisesta ohjelmoinnista

Aloitetaan luomalla ensimmäinen MCP stdio-palvelimemme:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Määritä lokitus
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Luo palvelin
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
    # Käytä stdio-siirtoa
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Keskeiset erot poistettuun SSE-menetelmään verrattuna

**Stdio-siirto (nykyinen standardi):**
- Yksinkertainen aliprocess-malli – asiakas käynnistää palvelimen lapsiprosessina
- Kommunikointi stdin/stdout -virtojen kautta JSON-RPC-viesteillä
- Ei HTTP-palvelimen asetusta vaadita
- Parempi suorituskyky ja turvallisuus
- Helpompi debugata ja kehittää

**SSE-siirto (poistettu käytöstä MCP 2025-06-18 alkaen):**
- Vaatimuksena HTTP-palvelin, jossa SSE-endpointit
- Monimutkaisempi asennus web-palvelininfrastruktuurin kanssa
- Lisättyjä turvallisuusseikkoja HTTP-endpointteihin liittyen
- Nyt korvattu Streamable HTTP:llä web-pohjaisiin skenaarioihin

### Palvelimen luonti stdio-siirrolla

Palvelimen luomiseksi meidän tulee:

1. **Tuoda tarvittavat kirjastot** – Tarvitsemme MCP-palvelimen komponentteja ja stdio-siirron
2. **Luoda palvelininstanssi** – Määritellä palvelin ja sen kyvykkyydet
3. **Määritellä työkalut** – Lisätä haluttu toiminnallisuus esille
4. **Konfiguroida siirto** – Asettaa stdio-yhteys
5. **Käynnistää palvelin** – Aloittaa palvelin ja käsitellä viestejä

Rakennetaan tämä vaihe vaiheelta:

### Vaihe 1: Luo perus stdio-palvelin

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Määritä lokitus
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Luo palvelin
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

### Vaihe 3: Käynnistä palvelin

Tallenna koodi tiedostoon `server.py` ja suorita se komentoriviltä:

```bash
python server.py
```

Palvelin käynnistyy ja odottaa syötettä stdin:stä. Se kommunikoi JSON-RPC-viestien kautta stdio-siirrossa.

### Vaihe 4: Testaus Inspectorilla

Voit testata palvelintasi MCP Inspectorilla:

1. Asenna Inspector: `npx @modelcontextprotocol/inspector`
2. Käynnistä Inspector ja osoita se palvelimeesi
3. Testaa luomiasi työkaluja

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Stdio-palvelimen debuggaus

### MCP Inspectorin käyttäminen

MCP Inspector on arvokas työkalu MCP-palvelinten debuggaukseen ja testaukseen. Näin käytät sitä stdio-palvelimesi kanssa:

1. **Asenna Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käynnistä Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testaa palvelimesi**: Inspector tarjoaa web-käyttöliittymän, jossa voit:
   - Näyttää palvelimen kyvykkyydet
   - Testata työkaluja eri parametreilla
   - Tarkkailla JSON-RPC-viestejä
   - Debugata yhteysongelmia

### VS Coden käyttäminen

Voit myös debugata MCP-palvelintasi suoraan VS Codessa:

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

2. Aseta breakpointit palvelinkoodiin
3. Käynnistä debuggeri ja testaa Inspectorilla

### Yleiset debuggausvinkit

- Käytä `stderr`-virtaa lokitukseen – älä kirjoita `stdout`-virtaan, joka on varattu MCP-viesteille
- Varmista, että kaikki JSON-RPC-viestit ovat rivinvaihdoilla rajattuja
- Testaa ensin yksinkertaisia työkaluja ennen monimutkaisten toimintojen lisäämistä
- Käytä Inspectorin avulla viestimuotojen varmistamiseen

## stdio-palvelimesi käyttäminen VS Codessa

Kun olet rakentanut MCP stdio-palvelimesi, voit integroida sen VS Codeen käyttöösi Clauden tai muiden MCP-yhteensopivien asiakkaiden kanssa.

### Konfiguraatio

1. **Luo MCP-konfiguraatiotiedosto** polkuun `%APPDATA%\Claude\claude_desktop_config.json` (Windows) tai `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Käynnistä Claude uudelleen**: Sulje ja avaa Claude uudelleen, jotta palvelinkonfiguraatio latautuu.

3. **Testaa yhteys**: Aloita keskustelu Clauden kanssa ja kokeile palvelimen työkaluja:
   - "Voisitko tervehtiä minua tervehdystyökalulla?"
   - "Laske luvut 15 ja 27 yhteen"
   - "Mikä on palvelimen tiedot?"

### TypeScript stdio-palvelimen esimerkki

Tässä on täydellinen TypeScript-esimerkki viitteeksi:

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

// Lisää työkaluja
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
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Yhteenveto

Tässä päivitetussa oppitunnissa opit:

- Rakentamaan MCP-palvelimia käyttäen nykyistä **stdio-siirtoa** (suositeltu menetelmä)
- Ymmärtämään miksi SSE-siirto poistettiin käytöstä stdio- ja Streamable HTTP -siirtojen hyväksi
- Luomaan työkaluja, joita MCP-asiakkaat voivat kutsua
- Debuggaamaan palvelintasi MCP Inspectorilla
- Integroimaan stdio-palvelimesi VS Codeen ja Claudeen

Stdio-siirto tarjoaa yksinkertaisemman, turvallisemman ja suorituskykyisemmän tavan rakentaa MCP-palvelimia poistettuun SSE-lähestymistapaan verrattuna. Se on suositeltu siirto suurimmalle osalle MCP-palvelinimplementaatioita alkaen 2025-06-18 spesifikaatiosta.

### .NET

1. Luodaan ensin joitain työkaluja. Tätä varten luomme tiedoston *Tools.cs*, jossa on seuraava sisältö:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Tehtävä: Testaa stdio-palvelintasi

Nyt kun olet rakentanut stdio-palvelimesi, testataan sitä varmistaaksemme, että se toimii oikein.

### Esivaatimukset

1. Varmista, että MCP Inspector on asennettu:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Palvelinkoodisi on tallennettu (esim. `server.py`)

### Testaus Inspectorilla

1. **Käynnistä Inspector palvelimesi kanssa**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Avaa web-käyttöliittymä**: Inspector avaa selaimen, jossa näet palvelimesi kyvykkyydet.

3. **Testaa työkaluja**:
   - Kokeile `get_greeting`-työkalua eri nimillä
   - Testaa `calculate_sum` -työkalua eri luvuilla
   - Kutsu `get_server_info`-työkalua nähdäksesi palvelinmetatiedot

4. **Seuraa viestintää**: Inspector näyttää JSON-RPC-viestit, joita asiakas ja palvelin vaihtavat.

### Mitä sinun pitäisi nähdä

Kun palvelimesi käynnistyy oikein, sinun pitäisi nähdä:
- Palvelimen kyvykkyydet Inspectorissa listattuna
- Työkaluja testattavaksi
- Onnistuneita JSON-RPC-viestinvaihtoja
- Työkalujen vastaukset käyttöliittymässä

### Yleisiä ongelmia ja ratkaisuja

**Palvelin ei käynnisty:**
- Tarkista, että kaikki riippuvuudet on asennettu: `pip install mcp`
- Tarkista Python-syntaksi ja sisennykset
- Katso virheilmoitukset konsolista

**Työkaluja ei näy:**
- Varmista, että `@server.tool()` -koristeet ovat paikallaan
- Tarkista, että työkalufunktiot on määritelty ennen `main()`-funktiota
- Varmista, että palvelin on oikein konfiguroitu

**Yhteysongelmia:**
- Varmista, että palvelin käyttää stdio-siirtoa oikein
- Tarkista ettei muita prosesseja häiritse
- Varmista Inspector-komennon syntaksi

## Tehtävänanto

Kokeile kehittää palvelintasi lisäämällä kyvykkyyksiä. Katso [täältä](https://api.chucknorris.io/) esimerkiksi työkalu, joka tekee API-kutsun. Sinä päätät, miltä palvelimen tulisi näyttää. Hauskaa koodausta :)

## Ratkaisu

[Ratkaisu](./solution/README.md) Tässä on mahdollinen ratkaisu toimivalla koodilla.

## Tärkeimmät opit

Tämän luvun tärkeimmät opit ovat seuraavat:

- Stdio-siirto on suositeltu mekanismi paikallisille MCP-palvelimille.
- Stdio-siirto mahdollistaa saumattoman kommunikoinnin MCP-palvelinten ja asiakkaiden välillä standardisyötteen ja -tulosteen avulla.
- Voit käyttää sekä Inspector-työkalua että Visual Studio Codea stdio-palvelinten käyttöön, mikä helpottaa debuggausta ja integrointia.

## Esimerkit

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Lisäresurssit

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mitä seuraavaksi

## Seuraavat askeleet

Nyt kun osaat rakentaa MCP-palvelimia stdio-siirrolla, voit tutkia edistyneempiä aiheita:

- **Seuraavaksi**: [HTTP Streaming MCP:llä (Streamable HTTP)](../06-http-streaming/README.md) – Tutustu toiseen tuettuun siirtomekanismiin etäpalvelimille
- **Edistynyt**: [MCP:n turvallisuuskäytännöt](../../02-Security/README.md) – Toteuta turvallisuus MCP-palvelimissasi
- **Tuotanto**: [Julkaisustrategiat](../09-deployment/README.md) – Julkaise palvelimesi tuotantokäyttöön

## Lisäresurssit

- [MCP Spesifikaatio 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Virallinen spesifikaatio
- [MCP SDK Dokumentaatio](https://github.com/modelcontextprotocol/sdk) – SDK-viitteet kaikille kielille
- [Yhteisön esimerkit](../../06-CommunityContributions/README.md) – Lisää palvelin-esimerkkejä yhteisöltä

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja huomioi, että automaattisissa käännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suosittelemme ammattilaisen tekemää ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->