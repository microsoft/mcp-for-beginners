# MCP-palvelin stdio-siirrolla

> **⚠️ Tärkeä päivitys**: MCP-spesifikaation 2025-06-18 versiosta lähtien erillistä SSE (Server-Sent Events) -siirtotapaa on **päivitetty** eikä sitä enää suositella, vaan se on korvattu "Streamable HTTP" -siirtotavalla. Nykyinen MCP-spesifikaatio määrittelee kaksi pääasiallista siirtomekanismia:
> 1. **stdio** - Standardi syöttö/tuotto (suositeltu paikallisille palvelimille)
> 2. **Streamable HTTP** - Etäpalvelimille, jotka voivat käyttää SSE:tä sisäisesti
>
> Tämä oppitunti on päivitetty keskittymään **stdio-siirtoon**, joka on suositeltu lähestymistapa useimmissa MCP-palvelinimplementaatioissa.

Stdio-siirto mahdollistaa MCP-palvelimien kommunikoimisen asiakkaiden kanssa tavallisen syötön ja tulostuksen kautta. Tämä on yleisimmin käytetty ja suositeltu siirtomekanismi nykyisessä MCP-spesifikaatiossa, tarjoten yksinkertaisen ja tehokkaan tavan rakentaa MCP-palvelimia, jotka voidaan helposti integroida erilaisiin asiakasohjelmiin.

## Yleiskatsaus

Tässä oppitunnissa käsitellään, miten rakentaa ja hyödyntää MCP-palvelimia stdio-siirtoa käyttäen.

## Oppimistavoitteet

Oppitunnin lopuksi osaat:

- Rakentaa MCP-palvelimen käyttäen stdio-siirtoa.
- Virheenkorjata MCP-palvelimen Inspector-työkalun avulla.
- Käyttää MCP-palvelinta Visual Studio Codessa.
- Ymmärtää nykyiset MCP-siirtomekanismit ja miksi stdio on suositeltava.

## stdio-siirto - miten se toimii

Stdio-siirto on yksi kahdesta tuetusta siirtotyypistä nykyisessä MCP-spesifikaatiossa (2025-06-18). Näin se toimii:

- **Yksinkertainen viestintä**: Palvelin lukee JSON-RPC-viestejä tavallisesta syötteestä (`stdin`) ja lähettää viestejä tavalliseen tulosteeseen (`stdout`).
- **Prosessipohjainen**: Asiakas käynnistää MCP-palvelimen aliprosessina.
- **Viestimuoto**: Viestit ovat yksittäisiä JSON-RPC-pyyntöjä, ilmoituksia tai vastauksia, jotka erotetaan rivinvaihdoilla.
- **Lokitus**: Palvelin VOI kirjoittaa UTF-8-merkkijonoja standardivirtaan (`stderr`) lokitustarkoituksiin.

### Keskeiset vaatimukset:
- Viestit TULEE erottaa rivinvaihdoilla, eikä niiden sisällä SAA olla upotettuja rivinvaihtoja
- Palvelimen EI SAA kirjoittaa `stdout`iin mitään muuta kuin kelvollisia MCP-viestejä
- Asiakkaan EI SAA kirjoittaa palvelimen `stdin`iin mitään muuta kuin kelvollisia MCP-viestejä

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

- Tuodaan `Server`-luokka ja `StdioServerTransport` MCP SDK:sta
- Luodaan palvelininstanssi perusasetuksilla ja ominaisuuksilla

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Luo palvelimen instanssi
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

- Luodaan MCP SDK:lla palvelininstanssi
- Määritellään käsittelijät koristeiden avulla
- Käytetään `stdio_server`-kontekstinhallintaa siirron käsittelyyn

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

- Eivät vaadi verkkopalvelimen asetusta tai HTTP-päätepisteitä
- Käynnistetään asiakkaan toimesta aliprosesseina
- Kommunikoivat stdin/stdout-virtojen kautta
- Ovat helpompia toteuttaa ja virheenkorjata

## Harjoitus: stdio-palvelimen luominen

Palvelintamme luodessamme meidän tulee pitää mielessä kaksi asiaa:

- Tarvitsemme verkkopalvelimen julkaisemaan päätepisteitä yhteyksiä ja viestejä varten.

## Labra: Yksinkertaisen MCP stdio-palvelimen luominen

Tässä labrassa luomme yksinkertaisen MCP-palvelimen käyttäen suositeltua stdio-siirtoa. Tämä palvelin tarjoaa työkaluja, joita asiakkaat voivat kutsua standardin Model Context Protocolin mukaisesti.

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

## Keskeiset erot vanhentuneeseen SSE-lähestymistapaan

**Stdio-siirto (nykyinen standardi):**
- Yksinkertainen aliprosessimalli – asiakas käynnistää palvelimen lapsiprosessina
- Kommunikointi stdin/stdout avulla JSON-RPC-viesteillä
- Ei HTTP-palvelinta tai -päätepisteitä tarvitse
- Parempi suorituskyky ja turvallisuus
- Helpompi virheenkorjaus ja kehitys

**SSE-siirto (poistettu käytöstä MCP 2025-06-18):**
- Vaati HTTP-palvelimen SSE-päätepisteillä
- Monimutkaisempi kokoonpano verkkopalvelininfrastruktuurin kanssa
- Lisäturvallisuusnäkökohdat HTTP-päätepisteissä
- Korvattu nyt Streamable HTTP:llä web-pohjaisissa tapauksissa

### Palvelimen luominen stdio-siirtoa käyttäen

Luodaksemme stdio-palvelimen meidän tulee:

1. **Tuoda tarvittavat kirjastot** - Tarvitsemme MCP-palvelinkomponentit ja stdio-siirron
2. **Luoda palvelininstanssi** - Määritellä palvelin ja sen ominaisuudet
3. **Määritellä työkalut** - Lisätä haluttu toiminnallisuus
4. **Konfiguroida siirto** - Asettaa stdio-yhteys
5. **Käynnistää palvelin** - Aloittaa palvelimen ajaminen ja viestien käsittely

Rakennetaan se vaihe vaiheelta:

### Vaihe 1: Perus stdio-palvelimen luominen

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

### Vaihe 2: Lisää työkaluja

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

Tallenna koodi tiedostoksi `server.py` ja suorita se komentoriviltä:

```bash
python server.py
```

Palvelin käynnistyy ja odottaa syötettä stdin:stä. Se kommunikoi JSON-RPC-viesteillä stdio-siirron yli.

### Vaihe 4: Testaus Inspectorilla

Voit testata palvelinta MCP Inspectorin avulla:

1. Asenna Inspector: `npx @modelcontextprotocol/inspector`
2. Käynnistä Inspector ja osoita se palvelimeen
3. Testaa luomiasi työkaluja

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## Stdio-palvelimesi virheenkorjaus

### MCP Inspectorin käyttö

MCP Inspector on arvokas työkalu MCP-palvelimien virheenkorjaukseen ja testaukseen. Näin käytät sitä stdio-palvelimesi kanssa:

1. **Asenna Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käynnistä Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testaa palvelinta**: Inspector tarjoaa web-käyttöliittymän, jossa voit:
   - Tarkastella palvelimen ominaisuuksia
   - Testata työkaluja eri parametreilla
   - Seurata JSON-RPC-viestejä
   - Virheenkorjata yhteysongelmia

### VS Coden käyttö

Voit myös virheenkorjata MCP-palvelintasi suoraan VS Codessa:

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

2. Aseta breakpointteja palvelinkoodiin
3. Aja virheenkorjaus ja testaa Inspectorilla

### Yleisiä virheenkorjausvinkkejä

- Käytä `stderr`ia lokitukseen – älä koskaan kirjoita `stdout`iin, koska se on varattu MCP-viesteille
- Varmista, että kaikki JSON-RPC-viestit ovat rivinvaihdolla eroteltuja
- Kokeile ensin yksinkertaisia työkaluja, ennen kuin lisäät monimutkaisuutta
- Käytä Inspectoria viestimuotojen tarkistamiseen

## stdio-palvelimen käyttäminen VS Codessa

Rakennettuasi MCP stdio-palvelimesi, voit integroida sen VS Codeen käyttääksesi sitä Clauden tai muiden MCP-yhteensopivien asiakkaiden kanssa.

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

2. **Käynnistä Claude uudelleen**: Sulje ja käynnistä Claude lataamaan uusi palvelinasetus.

3. **Testaa yhteys**: Aloita keskustelu Clauden kanssa ja kokeile palvelimesi työkaluja:
   - "Voisitko tervehtiä minua tervehdyspalvelulla?"
   - "Laske 15 ja 27 summa"
   - "Mikä on palvelimen tieto?"

### TypeScript stdio-palvelin esimerkki

Tässä täydellinen TypeScript-esimerkki:

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

### .NET stdio-palvelin esimerkki

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

- Rakentamaan MCP-palvelimia nykyisellä **stdio-siirtotavalla** (suositeltu tapa)
- Ymmärtämään, miksi SSE-siirto poistettiin ja stdio sekä Streamable HTTP otettiin käyttöön
- Luomaan työkaluja, joita MCP-asiakkaat voivat kutsua
- Virheenkorjaamaan palvelinta MCP Inspectorilla
- Integroimaan stdio-palvelimen VS Codessa ja Clauden kanssa

Stdio-siirto tarjoaa yksinkertaisemman, turvallisemman ja suorituskykyisemmän tavan rakentaa MCP-palvelimia verrattuna vanhentuneeseen SSE-malliin. Se on suositeltu siirtotapa useimpiin MCP-palvelinratkaisuihin 2025-06-18 spesifikaation mukaisesti.

### .NET

1. Luodaan ensin muutama työkalu, tähän teemme tiedoston *Tools.cs* seuraavalla sisällöllä:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjoitus: stdio-palvelimen testaaminen

Nyt kun olet rakentanut stdio-palvelimesi, testataan että se toimii oikein.

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

2. **Avaa web-käyttöliittymä**: Inspector avaa selaimen, jossa näet palvelimesi ominaisuudet.

3. **Testaa työkalut**: 
   - Kokeile `get_greeting`-työkalua eri nimillä
   - Testaa `calculate_sum`-työkalua eri luvuilla
   - Kutsu `get_server_info`-työkalua nähdäksesi palvelimen metatiedot

4. **Seuraa viestintää**: Inspector näyttää JSON-RPC-viestit, joita vaihdetaan asiakkaan ja palvelimen välillä.

### Mitä sinun tulisi nähdä

Kun palvelimesi käynnistyy oikein, näet:
- Palvelimen ominaisuudet listattuna Inspectorissa
- Työkalut testattavaksi
- Onnistuneet JSON-RPC-viestinvaihdot
- Työkalujen vastaukset käyttöliittymässä

### Yleisiä ongelmia ja ratkaisuja

**Palvelin ei käynnisty:**
- Tarkista, että kaikki riippuvuudet on asennettu: `pip install mcp`
- Varmista Python-syntaksi ja sisennykset
- Tarkista virheilmoitukset konsolista

**Työkalut eivät näy:**
- Varmista, että `@server.tool()` -koristeet ovat paikallaan
- Tarkista, että työkalufunktiot on määritelty ennen `main()`-funktiota
- Varmista, että palvelin on oikein konfiguroitu

**Yhteysongelmat:**
- Varmista, että palvelin käyttää stdio-siirtoa oikein
- Tarkista, ettei muita prosesseja häiritse
- Varmista Inspector-komennon syntaksi

## Tehtävä

Yritä laajentaa palvelintasi lisäämällä enemmän ominaisuuksia. Katso [tästä sivusta](https://api.chucknorris.io/) esimerkiksi, miten lisäät työkalun, joka kutsuu APIa. Voit itse päättää, miltä palvelimesi näyttää. Hauskaa koodausta :)

## Ratkaisu

[Ratkaisu](./solution/README.md) Tässä on mahdollista ratkaisua toimivalla koodilla.

## Keskeiset opit

Tämän luvun keskeiset opit ovat:

- Stdio-siirto on suositeltu mekanismi paikallisille MCP-palvelimille.
- Stdio-siirto mahdollistaa saumattoman kommunikoinnin MCP-palvelimien ja asiakkaiden välillä käyttäen tavallisia syöte- ja tulostusvirtoja.
- Voit käyttää sekä Inspectoria että Visual Studio Codea stdio-palvelimien kuluttamiseen, mikä tekee virheenkorjauksesta ja integroinnista helppoa.

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

- **Seuraava**: [HTTP Streaming MCP:llä (Streamable HTTP)](../06-http-streaming/README.md) - Opi toisesta tuetusta siirtomekanismista etäpalvelimille
- **Edistynyt**: [MCP:n turvallisuusparhaat käytännöt](../../02-Security/README.md) - Toteuta turvallisuus MCP-palvelimiisi
- **Tuotanto**: [Julkaisustrategiat](../09-deployment/README.md) - Julkaise palvelimesi tuotantokäyttöön

## Lisäresurssit

- [MCP Spesifikaatio 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Virallinen spesifikaatio
- [MCP SDK Dokumentaatio](https://github.com/modelcontextprotocol/sdk) - SDK-viitteet kaikille kielille
- [Yhteisön Esimerkit](../../06-CommunityContributions/README.md) - Lisää palvelinesimerkkejä yhteisöltä

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta on hyvä huomioida, että konekäännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä katsotaan ensisijaiseksi lähteeksi. Tärkeissä tiedoissa suositellaan ammattilaisen tekemää ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä mahdollisesti aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->