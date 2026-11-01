# MCP-palvelin stdio-siirrolla

> **⚠️ Tärkeä päivitys**: MCP-spesifikaation 2025-06-18 mukaisesti erillinen SSE (Server-Sent Events) -siirtotapa on **vanhentunut** ja korvattu "Streamable HTTP" -siirtotavalla. Nykyinen MCP-spesifikaatio määrittelee kaksi pääasiallista siirtomekanismia:
> 1. **stdio** – Vakio syöte/ulosotto (suositellaan paikallisille palvelimille)
> 2. **Streamable HTTP** – Etäpalvelimille, jotka voivat käyttää SSE:tä sisäisesti
>
> Tämä oppitunti on päivitetty keskittymään **stdio-siirtoon**, joka on suositeltu tapa useimmissa MCP-palvelinratkaisuissa.

Stdio-siirto mahdollistaa MCP-palvelimien kommunikoinnin asiakkaiden kanssa vakio syöte- ja ulostulovirtojen kautta. Tämä on yleisimmin käytetty ja suositeltu siirtotapa nykyisessä MCP-spesifikaatiossa, tarjoten yksinkertaisen ja tehokkaan tavan rakentaa MCP-palvelimia, jotka voidaan helposti integroida eri asiakasohjelmiin.

## Yleiskatsaus

Tässä oppitunnissa käydään läpi, miten rakentaa ja käyttää MCP-palvelimia stdio-siirtotavan avulla.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Rakentaa MCP-palvelimen käyttäen stdio-siirtoa.
- Virheenkorjata MCP-palvelinta Inspectorilla.
- Käyttää MCP-palvelinta Visual Studio Codessa.
- Ymmärtää nykyiset MCP-siirtomekanismit ja miksi stdio on suositeltu.


## stdio-siirto – Kuinka se toimii

Stdio-siirto on yksi kahdesta MCP-spesifikaation standardisiirtotavasta
`2026-07-28`. Näin se toimii:

- **Yksinkertainen kommunikaatio**: Palvelin lukee JSON-RPC-viestejä vakiosyötteestä (`stdin`) ja lähettää viestejä vakio-ulostuloon (`stdout`).
- **Prosessipohjainen**: Asiakas käynnistää MCP-palvelimen aliprosessina.
- **Viestimuoto**: Viestit ovat yksittäisiä JSON-RPC-pyyntöjä, ilmoituksia tai vastauksia, eritelty rivinvaihdoin.
- **Lokitus**: Palvelin VOI kirjoittaa UTF-8-merkkijonoja vakiovirheeseen (`stderr`) lokitusta varten.

### Keskeiset vaatimukset:
- Viestit TULEE erottaa rivinvaihdoilla eikä niissä TULE sisältää upotettuja rivinvaihtoja
- Palvelin EI SAA kirjoittaa mitään `stdout`, joka ei ole kelvollinen MCP-viesti
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

- Tuomme `Server`-luokan ja `StdioServerTransport` MCP SDK:sta
- Luomme palvelininstanssin perusasetuksin ja -ominaisuuksin
- Luomme `StdioServerTransport`-instanssin ja yhdistämme palvelimen siihen, mahdollistaen kommunikoinnin stdin/stdoutin yli

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

Edellisessä koodissa me:

- Luomme palvelininstanssin MCP SDK:lla
- Määrittelemme työkalut koristelijoilla
- Käytämme stdio_server-kontekstinhallintaa siirron käsittelemiseen

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

Keskeinen ero SSE:hen nähden on, että stdio-palvelimet:

- Eivät vaadi web-palvelimen asennusta tai HTTP-päätepisteitä
- Käynnistetään asiakasprosessin aliprosessina
- Kommunikoivat stdin/stdout-virtojen kautta
- Ovat helpompia toteuttaa ja virheenkorjata

## Harjoitus: Stdio-palvelimen luominen

Palvelinta luodessa on pidettävä mielessä kaksi asiaa:

- Tarvitsemme web-palvelimen tarjoamaan päätepisteet yhteydelle ja viesteille.
## Laboratorio: Yksinkertaisen MCP stdio-palvelimen luominen

Tässä laboratoriossa luomme yksinkertaisen MCP-palvelimen käyttäen suositeltua stdio-siirtotapaa. Palvelin tarjoaa työkaluja, joita asiakkaat voivat kutsua standardoidulla Model Context Protocolilla.

### Esivaatimukset

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

## Keskeiset erot vanhentuneeseen SSE-tapaan verrattuna

**Stdio-siirto (Nykyinen standardi):**
- Yksinkertainen aliprosessimalli – asiakas käynnistää palvelimen lapsiprosessina
- Kommunikointi stdin/stdoutin kautta JSON-RPC-viesteillä
- Ei vaadi HTTP-palvelimen asennusta
- Parempi suorituskyky ja turvallisuus
- Helpompi virheenkorjaus ja kehitys

**SSE-siirto (vanhentunut 2025-06-18):**
- Vaatii HTTP-palvelimen SSE-päätepisteillä
- Monimutkaisempi asennus web-palvelininfrastruktuurin kanssa
- Lisäturvavaatimuksia HTTP-päätepisteille
- Korvattu Streamable HTTP:llä verkkopohjaisissa skenaarioissa

### Palvelimen luominen stdio-siirrolla

Palvelimen luomiseksi stdio-siirrolla:

1. **Tuodaan tarvittavat kirjastot** – Tarvitsemme MCP-palvelin-komponentit ja stdio-siirron
2. **Luodaan palvelininstanssi** – Määritellään palvelimen ominaisuudet
3. **Määritellään työkalut** – Lisätään tarjottavat toiminnot
4. **Kokoonpano siirrolle** – Konfiguroidaan stdio-kommunikointi
5. **Ajetaan palvelinta** – Käynnistetään palvelin ja käsitellään viestejä

Rakennetaan tätä vaihe vaiheelta:

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

Tallenna koodi tiedostoksi `server.py` ja suorita komentoriviltä:

```bash
python server.py
```

Palvelin käynnistyy ja odottaa syötettä stdin:stä. Se kommunikoi JSON-RPC-viestien avulla stdio-siirron ylitse.

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
## Virheenkorjaus stdio-palvelimessasi

### MCP Inspectorin käyttäminen

MCP Inspector on arvokas työkalu MCP-palvelinten virheenkorjaukseen ja testaukseen. Näin käytät sitä stdio-palvelimessasi:

1. **Asenna Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käynnistä Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testaa palvelintasi**: Inspector tarjoaa web-käyttöliittymän, jossa voit:
   - Tarkastella palvelimen ominaisuuksia
   - Testata työkaluja erilaisilla parametreilla
   - Seurata JSON-RPC-viestejä
   - Virheenkorjata yhteysongelmia

### VS Coden käyttäminen

Voit myös virheenkorjata MCP-palvelintasi suoraan VS Codessa:

1. Luo ajokonfiguraatio tiedostoon `.vscode/launch.json`:
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

2. Aseta katkaisupisteet palvelinkoodiin
3. Käynnistä virheenkorjaus ja testaa Inspectorilla

### Yleisiä virheenkorjausvinkkejä

- Käytä `stderr` lokitukseen – älä koskaan kirjoita `stdout`-virtaan, koska se on varattu MCP-viesteille
- Varmista, että kaikki JSON-RPC-viestit on erotettu rivinvaihdoilla
- Testaa ensin yksinkertaisilla työkaluilla ennen monimutkaisten toimintojen lisäämistä
- Käytä Inspectoria viestimuotojen tarkistamiseen

## MCP stdio-palvelimen käyttäminen VS Codessa

Rakennettuasi MCP stdio-palvelimen voit integroida sen VS Codeen käyttääksesi sitä Clauden tai muiden MCP-yhteensopivien asiakkaiden kanssa.

### Konfiguraatio

1. **Luo MCP-konfiguraatiotiedosto** osoitteeseen `%APPDATA%\Claude\claude_desktop_config.json` (Windows) tai `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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
   - "Voisitko tervehtiä minua tervehdystyökalulla?"
   - "Laske luvun 15 ja 27 summa"
   - "Mikä on palvelimen tiedot?"

### TypeScript stdio-palvelinesimerkki

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

Tässä päivitettyssä oppitunnissa opit:

- Rakentamaan MCP-palvelimia käyttäen nykyistä **stdio-siirtoa** (suositeltu tapa)
- Ymmärtämään, miksi SSE-siirto vanhentui ja miksi stdio ja Streamable HTTP korvasivat sen
- Luomaan työkaluja, joita MCP-asiakkaat voivat kutsua
- Virheenkorjaamaan palvelintasi MCP Inspectorilla
- Integroimaan stdio-palvelimesi VS Codeen ja Claudeen

Stdio-siirto tarjoaa yksinkertaisemman, turvallisemman ja tehokkaamman tavan rakentaa MCP-palvelimia verrattuna vanhentuneeseen SSE-tapaan. Se on suositeltu siirtotapa useimmille MCP-palvelinratkaisuille 2025-06-18 spesifikaation mukaisesti.


### .NET

1. Luodaan ensin joitakin työkaluja, teemme tiedoston *Tools.cs* seuraavalla sisällöllä:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjoitus: Testaa stdio-palvelintasi

Nyt kun olet luonut stdio-palvelimesi, testataan se varmistaaksemme, että se toimii oikein.

### Esivaatimukset

1. Varmista, että sinulla on asennettuna MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Palvelinkoodisi tulisi olla tallennettuna (esim. tiedostona `server.py`)

### Testaus Inspectorilla

1. **Käynnistä Inspector palvelimesi kanssa**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Avaa web-käyttöliittymä**: Inspector avaa selaimen ikkunan, jossa näkyvät palvelimesi ominaisuudet.

3. **Testaa työkalut**: 
   - Kokeile `get_greeting`-työkalua eri nimillä
   - Testaa `calculate_sum`-työkalua eri numeroilla
   - Kutsu `get_server_info`-työkalua nähdäksesi palvelimen metatiedot

4. **Seuraa kommunikointia**: Inspector näyttää JSON-RPC-viestit, joita vaihdetaan asiakkaan ja palvelimen välillä.

### Mitä sinun pitäisi nähdä

Kun palvelin käynnistyy oikein, sinun pitäisi nähdä:
- Palvelimen ominaisuudet listattuna Inspectorissa
- Testattavat työkalut käytettävissä
- Onnistuneet JSON-RPC-viestinvaihdot
- Työkalujen vastaukset näkyvissä käyttöliittymässä

### Yleisiä ongelmia ja ratkaisuja

**Palvelin ei käynnisty:**
- Tarkista, että kaikki riippuvuudet on asennettu: `pip install mcp`
- Varmista Python-syntaksin ja sisennyksen oikeellisuus
- Etsi virheilmoituksia konsolista

**Työkalut eivät näy:**
- Varmista, että `@server.tool()`-koristelijat ovat paikoillaan
- Tarkista, että työkalufunktiot on määritelty ennen `main()`
- Varmista palvelimen oikea konfigurointi

**Yhteysongelmat:**
- Varmista, että palvelin käyttää stdio-siirtoa oikein
- Tarkista, ettei muut prosessit häiritse
- Varmista Inspectorin komentorivikäskyjen oikeellisuus

## Tehtävä

Kokeile rakentaa palvelimesi monipuolisemmaksi. Katso [tältä sivulta](https://api.chucknorris.io/) esimerkiksi, miten voit lisätä työkalun, joka kutsuu APIa. Sinä päätät, miltä palvelimen tulisi näyttää. Hauskaa:)
## Ratkaisu

[Ratkaisu](./solution/README.md) Tässä mahdollinen ratkaisu toimivalla koodilla.

## Keskeiset opit

Tässä luvussa opitut keskeiset asiat ovat:

- Stdio-siirto on suositeltu mekanismi paikallisille MCP-palvelimille.
- Stdio-siirto mahdollistaa saumattoman kommunikoinnin MCP-palvelimien ja asiakkaiden välillä käyttämällä vakio syöte- ja ulostulovirtoja.
- Voit käyttää sekä Inspectoria että Visual Studio Codea stdio-palvelimien kuluttamiseen suoraan, mikä tekee virheenkorjauksesta ja integraatiosta sujuvaa.

## Esimerkit 

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Lisäresurssit

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mitä seuraavaksi

## Seuraavat vaiheet

Nyt kun olet oppinut rakentamaan MCP-palvelimia stdio-siirrolla, voit tutustua edistyneempiin aiheisiin:

- **Seuraava**: [HTTP Streaming MCP:llä (Streamable HTTP)](../06-http-streaming/README.md) – Opi toisesta tuetusta siirtomekanismista etäpalvelimille
- **Edistynyt**: [MCP:n turvallisuusparhaat käytännöt](../../02-Security/README.md) – Toteuta turvallisuutta MCP-palvelimissasi
- **Tuotanto**: [Julkaisustrategiat](../09-deployment/README.md) – Ota palvelimesi käyttöön tuotantoympäristössä

## Lisäresurssit

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) – Nykyinen spesifikaatio
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) – SDK-tiedot kaikille kielille
- [Community Examples](../../06-CommunityContributions/README.md) – Lisää palvelinesimerkkejä yhteisöltä

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->