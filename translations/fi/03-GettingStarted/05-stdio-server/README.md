# MCP-palvelin stdio-siirrolla

> **⚠️ Tärkeä päivitys**: MCP-määritelmän 2025-06-18 alkaen itsenäinen SSE (Server-Sent Events) -siirtotapa on **poistettu käytöstä** ja korvattu "Streamable HTTP" -siirrolla. Nykyinen MCP-määritelmä määrittelee kaksi pääasiallista siirtotapaa:
> 1. **stdio** - Standardi syöte/ulosotto (suositeltu paikallisille palvelimille)
> 2. **Streamable HTTP** - Etäpalvelimille, jotka voivat käyttää SSE:tä sisäisesti
>
> Tämä oppitunti on päivitetty keskittymään **stdio-siirtoon**, joka on suositeltu lähestymistapa useimmissa MCP-palvelinratkaisuissa.

Stdio-siirto mahdollistaa MCP-palvelimien kommunikoimisen asiakkaiden kanssa standardin syötteen ja ulostulon kautta. Tämä on yleisimmin käytetty ja suositeltu siirtotapa nykyisessä MCP-määritelmässä, tarjoten yksinkertaisen ja tehokkaan tavan rakentaa MCP-palvelimia, jotka voidaan helposti integroida erilaisiin asiakassovelluksiin.

## Yleiskatsaus

Tässä oppitunnissa käydään läpi, miten rakentaa ja hyödyntää MCP-palvelimia stdio-siirrolla.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Rakentaa MCP-palvelimen stdio-siirtoa käyttäen.
- Debuggataa MCP-palvelimen Inspector-työkalulla.
- Käyttää MCP-palvelinta Visual Studio Codella.
- Ymmärtää nykyiset MCP-siirtomekanismit ja miksi stdio on suositeltu.


## stdio-siirto – Miten se toimii

Stdio-siirto on yksi kahdesta MCP-määritelmän
`2026-07-28` standardisiirtotavasta. Näin se toimii:

- **Yksinkertainen viestintä**: Palvelin lukee JSON-RPC-viestejä standardisyötteestä (`stdin`) ja lähettää viestejä standardiulostuloon (`stdout`).
- **Prosessipohjainen**: Asiakas käynnistää MCP-palvelimen aliprosessina.
- **Viestimuoto**: Viestit ovat yksittäisiä JSON-RPC-pyyntöjä, ilmoituksia tai vastauksia, jotka erotetaan rivinvaihdoilla.
- **Lokitus**: Palvelin VOI kirjoittaa UTF-8-merkkijonoja standardivirheeseen (`stderr`) lokitusta varten.

### Keskeiset vaatimukset:
- Viestit TULEE erottaa rivinvaihdoilla eikä niiden sisälle SAA sisältyä rivinvaihtoja
- Palvelimen EI TULE kirjoittaa `stdout`-virtaan mitään muuta kuin kelvollisen MCP-viestin
- Asiakkaan EI TULE kirjoittaa palvelimen `stdin`-virtaan mitään muuta kuin kelvollisen MCP-viestin

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

- Tuodaan `Server`-luokka ja `StdioServerTransport` MCP SDK:sta
- Luodaan palvelininstanssi perusasetuksilla ja ominaisuuksilla
- Luodaan `StdioServerTransport`-instanssi ja yhdistetään palvelin siihen, mahdollistaen kommunikaation stdin/stdout läpi

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

- Luomme palvelimen MCP SDK:ta käyttäen
- Määrittelemme työkalut koristeiden avulla
- Käytämme stdio_server-context manageria siirron hallintaan

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

- Eivät vaadi web-palvelimen käyttöönottoa tai HTTP-päätepisteitä
- Käynnistetään asiakkaan aliprosesseina
- Kommunikoivat stdin/stdout-virtojen kautta
- Ovat yksinkertaisempia toteuttaa ja debugata

## Harjoitus: Stdio-palvelimen luominen

Palvelinta luodessa meidän tulee pitää mielessä kaksi asiaa:

- Meidän pitää käyttää web-palvelinta paljastamaan päätepisteet yhteyttä ja viestejä varten.
## Labra: Yksinkertaisen MCP stdio-palvelimen luominen

Tässä labrassa luomme yksinkertaisen MCP-palvelimen käyttäen suositeltua stdio-siirtoa. Tämä palvelin tarjoaa työkaluja, joita asiakkaat voivat kutsua käyttämällä standardoitua Model Context Protocolia.

### Vaatimukset

- Python 3.8 tai uudempi
- MCP Python SDK: `pip install mcp`
- Perusymmärrys asynkronisesta ohjelmoinnista

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

## Keskeiset erot vanhentuneeseen SSE-malliin verrattuna

**Stdio-siirto (nykyinen standardi):**
- Yksinkertainen aliprosessimalli - asiakas käynnistää palvelimen lapsiprosessina
- Kommunikaatio stdin/stdout -virtana JSON-RPC-viesteillä
- Ei HTTP-palvelimen asennusta vaadita
- Parempi suorituskyky ja turvallisuus
- Helpompi debuggaus ja kehitys

**SSE-siirto (poistettu käytöstä MCP 2025-06-18 alkaen):**
- Vaatimuksena HTTP-palvelin SSE-päätepisteillä
- Monimutkaisempi asennus web-palvelininfrastruktuurilla
- Lisäturvatoimet HTTP-päätepisteille
- Nyt korvattu Streamable HTTP:llä web-pohjaisissa skenaarioissa

### Palvelimen luominen stdio-siirrolla

Palvelimemme luomiseksi meidän tulee:

1. **Tuoda tarvittavat kirjastot** - Tarvitsemme MCP-palvelinkomponentit ja stdio-siirron
2. **Luoda palvelininstanssi** - Määritellä palvelin sen ominaisuuksineen
3. **Määritellä työkalut** - Lisätä haluttu toiminnallisuus
4. **Konfiguroida siirto** - Asettaa stdio-viestintä
5. **Käynnistää palvelin** - Aloittaa palvelin ja käsitellä viestejä

Rakennetaan tämä vaihe vaiheelta:

### Vaihe 1: Luo perustason stdio-palvelin

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

### Vaihe 3: Palvelimen käynnistäminen

Tallenna koodi tiedostoon `server.py` ja suorita se komentoriviltä:

```bash
python server.py
```

Palvelin käynnistyy ja odottaa syötettä stdin:stä. Se kommunikoi JSON-RPC-viestien avulla stdio-siirron kautta.

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
## Saat vianetsinnän käyntiin stdio-palvelimelle

### MCP Inspectorin käyttö

MCP Inspector on arvokas työkalu MCP-palvelinten debuggaamiseen ja testaamiseen. Näin käytät sitä stdio-palvelimesi kanssa:

1. **Asenna Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käynnistä Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testaa palvelimesi**: Inspector tarjoaa web-käyttöliittymän, jossa voit:
   - Näyttää palvelimen ominaisuudet
   - Testata työkaluja eri parametreilla
   - Tarkkailla JSON-RPC-viestejä
   - Debuggataa yhteysongelmia

### VS Coden käyttö

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

2. Aseta breakpointit palvelinkoodiisi
3. Käynnistä debugger ja testaa Inspectorilla

### Yleisiä vianetsintävinkkejä

- Käytä `stderr`-virtaa lokitukseen - älä koskaan kirjoita `stdout`-virtuun, sillä se on varattu MCP-viesteille
- Varmista, että kaikki JSON-RPC-viestit ovat rivinvaihdolla erotettuja
- Testaa ensin yksinkertaisilla työkaluilla ennen monimutkaisen toiminnallisuuden lisäämistä
- Käytä Inspector-työkalua viestimuotojen varmistukseen

## Stdio-palvelimen käyttö VS Codessa

Kun olet rakentanut MCP stdio-palvelimesi, voit integroida sen VS Codeen käytettäväksi Clauden tai muiden MCP-yhteensopivien asiakkaiden kanssa.

### Konfigurointi

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

3. **Testaa yhteys**: Aloita keskustelu Clauden kanssa ja kokeile palvelimesi työkaluja:
   - "Voitko tervehtiä minua tervehdystyökalulla?"
   - "Laske lukujen 15 ja 27 summa"
   - "Mikä on palvelimen tiedot?"

### TypeScript stdio-palvelinesimerkki

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

### .NET stdio-palvelinesimerkki

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

Tässä päivitetystä oppitunnissa opit:

- Rakentamaan MCP-palvelimia nykyisellä **stdio-siirrolla** (suositeltu tapa)
- Ymmärtämään, miksi SSE-siirto poistettiin käytöstä stdio- ja Streamable HTTP -siirtojen hyväksi
- Luomaan työkaluja, joita MCP-asiakkaat voivat kutsua
- Debuggaamaan palvelinta MCP Inspectorilla
- Integroimaan stdio-palvelimen VS Codeen ja Claudeen

Stdio-siirto tarjoaa yksinkertaisemman, turvallisemman ja suorituskykyisemmän tavan rakentaa MCP-palvelimia verrattuna poistettuun SSE-malliin. Se on suositeltu siirtotapa useimpiin MCP-palvelinratkaisuihin 2025-06-18 määritelmän jälkeen.


### .NET

1. Luodaan ensin muutama työkalu, tähän luomme tiedoston *Tools.cs* seuraavalla sisällöllä:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjoitus: Stdio-palvelimen testaaminen

Nyt kun olet rakentanut stdio-palvelimesi, testaamme sen, jotta varmistamme että se toimii oikein.

### Vaaditut asiat

1. Varmista, että MCP Inspector on asennettu:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Palvelinkoodisi tulee olla tallennettuna (esim. `server.py`)

### Testaus Inspectorilla

1. **Käynnistä Inspector palvelimesi kanssa**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Avaa web-käyttöliittymä**: Inspector avaa selaimen ikkunan, jossa näkyvät palvelimesi ominaisuudet.

3. **Testaa työkalut**: 
   - Kokeile `get_greeting`-työkalua eri nimillä
   - Testaa `calculate_sum`-työkalua eri luvuilla
   - Kutsu `get_server_info`-työkalua nähdäksesi palvelimen metatiedot

4. **Valvo viestintää**: Inspector näyttää JSON-RPC-viestit, joita vaihdetaan asiakkaan ja palvelimen välillä.

### Mitä sinun pitäisi nähdä

Kun palvelimesi käynnistyy oikein, sinun pitäisi nähdä:
- Palvelimen ominaisuudet listattuna Inspectorissa
- Työkalut käytettävissä testaukseen
- Onnistuneita JSON-RPC-viestinvaihtoja
- Työkalujen vastaukset näytetty käyttöliittymässä

### Yleisiä ongelmia ja ratkaisuja

**Palvelin ei käynnisty:**
- Tarkista että kaikki riippuvuudet on asennettu: `pip install mcp`
- Varmista Python-koodin syntaksi ja sisennykset
- Tarkkaile konsolin virheilmoituksia

**Työkalut eivät näy:**
- Varmista, että `@server.tool()` -koristeet ovat paikallaan
- Tarkista, että työkalufunktiot määritellään ennen `main()`-funktiota
- Varmista, että palvelin on oikein konfiguroitu

**Yhteysongelmat:**
- Varmista, että palvelin käyttää stdio-siirtoa oikein
- Tarkista, ettei muut prosessit häiritse
- Tarkista Inspector-komentojen syntaksi

## Tehtävä

Yritä lisätä palvelimellesi enemmän ominaisuuksia. Katso [tätä sivua](https://api.chucknorris.io/) esimerkiksi lisätäksesi työkalun, joka kutsuu API:a. Sinä päätät miltä palvelimen tulisi näyttää. Hauskaa :)
## Ratkaisu

[Ratkaisu](./solution/README.md) Tässä on mahdollinen ratkaisu toimivalla koodilla.

## Tärkeimmät opit

Tässä luvussa tärkeimmät opit ovat:

- Stdio-siirto on suositeltu mekanismi paikallisille MCP-palvelimille.
- Stdio-siirto mahdollistaa saumattoman kommunikoinnin MCP-palvelimien ja asiakkaiden välillä käyttämällä standardia syöttö- ja tulostustuloa.
- Voit käyttää sekä Inspectoria että Visual Studio Codea stdio-palvelinten kuluttamiseen suoraan, mikä tekee debuggaamisesta ja integraatiosta vaivatonta.

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

Nyt kun olet oppinut rakentamaan MCP-palvelimia stdio-siirrolla, voit tutustua edistyneempiin aiheisiin:

- **Seuraava**: [HTTP Streaming MCP:llä (Streamable HTTP)](../06-http-streaming/README.md) – Tutustu toiseen tuettuun siirtomekanismiin etäpalvelimille
- **Edistynyt**: [MCP:n turvallisuusohjeet](../../02-Security/README.md) – Toteuta turvallisuus MCP-palvelimissasi
- **Tuotanto**: [Jälleenlanseerausstrategiat](../09-deployment/README.md) – Ota palvelimesi käyttöön tuotantoympäristössä

## Lisäresurssit

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) – Nykyinen spesifikaatio
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) – SDK-viitteet kaikille kielille
- [Yhteisön esimerkit](../../06-CommunityContributions/README.md) – Lisää palvelinesimerkkejä yhteisöltä

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->