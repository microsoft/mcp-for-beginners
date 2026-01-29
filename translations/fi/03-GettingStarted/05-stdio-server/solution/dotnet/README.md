# MCP stdio Server - .NET Ratkaisu

> **⚠️ Tärkeää**: Tämä ratkaisu on päivitetty käyttämään **stdio-kuljetusta**, kuten MCP-määrityksessä 2025-06-18 suositellaan. Alkuperäinen SSE-kuljetus on poistettu käytöstä.

## Yleiskatsaus

Tämä .NET-ratkaisu näyttää, kuinka rakentaa MCP-palvelin käyttäen nykyistä stdio-kuljetusta. Stdio-kuljetus on yksinkertaisempi, turvallisempi ja tarjoaa paremman suorituskyvyn kuin vanhentunut SSE-lähestymistapa.

## Esivaatimukset

- .NET 9.0 SDK tai uudempi
- Perustiedot .NET-riippuvuuksien injektoinnista

## Asennusohjeet

### Vaihe 1: Palauta riippuvuudet

```bash
dotnet restore
```

### Vaihe 2: Rakenna projekti

```bash
dotnet build
```

## Palvelimen käynnistäminen

Stdio-palvelin toimii eri tavalla kuin vanha HTTP-pohjainen palvelin. Sen sijaan, että se käynnistäisi verkkopalvelimen, se kommunikoi stdin/stdoutin kautta:

```bash
dotnet run
```

**Tärkeää**: Palvelin näyttää jäätyvän - tämä on normaalia! Se odottaa JSON-RPC-viestejä stdinistä.

## Palvelimen testaaminen

### Menetelmä 1: Käytä MCP Inspector -työkalua (suositeltu)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Tämä:
1. Käynnistää palvelimesi aliprosessina
2. Avaa verkkokäyttöliittymän testausta varten
3. Mahdollistaa kaikkien palvelintyökalujen interaktiivisen testauksen

### Menetelmä 2: Suora komentorivitestaus

Voit myös testata käynnistämällä Inspectorin suoraan:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Saatavilla olevat työkalut

Palvelin tarjoaa seuraavat työkalut:

- **AddNumbers(a, b)**: Laskee yhteen kaksi lukua
- **MultiplyNumbers(a, b)**: Kertoo kaksi lukua  
- **GetGreeting(name)**: Luo henkilökohtaisen tervehdyksen
- **GetServerInfo()**: Antaa tietoja palvelimesta

### Testaus Claude Desktopilla

Käyttääksesi tätä palvelinta Claude Desktopin kanssa, lisää tämä konfiguraatio tiedostoon `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Projektin rakenne

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Keskeiset erot HTTP/SSE:stä

**stdio-kuljetus (Nykyinen):**
- ✅ Yksinkertaisempi asennus - ei tarvetta verkkopalvelimelle
- ✅ Parempi turvallisuus - ei HTTP-päätepisteitä
- ✅ Käyttää `Host.CreateApplicationBuilder()` eikä `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` HTTP-kuljetuksen sijaan
- ✅ Konsolisovellus verkkosovelluksen sijaan
- ✅ Parempi suorituskyky

**HTTP/SSE-kuljetus (Poistettu käytöstä):**
- ❌ Vaati ASP.NET Core -verkkopalvelimen
- ❌ Tarvitsi `app.MapMcp()` reitityksen asennuksen
- ❌ Monimutkaisempi konfiguraatio ja riippuvuudet
- ❌ Lisäturvallisuusharkinnat
- ❌ Poistettu käytöstä MCP:ssä 2025-06-18

## Kehitysominaisuudet

- **Riippuvuuksien injektio**: Täysi DI-tuki palveluille ja lokitukselle
- **Rakenteellinen lokitus**: Oikea lokitus stderr:iin käyttäen `ILogger<T>`
- **Työkalujen attribuutit**: Selkeä työkalujen määrittely käyttäen `[McpServerTool]` attribuutteja
- **Async-tuki**: Kaikki työkalut tukevat asynkronisia operaatioita
- **Virheenkäsittely**: Hallittu virheenkäsittely ja lokitus

## Kehitysvinkit

- Käytä `ILogger`-luokkaa lokitukseen (älä koskaan kirjoita suoraan stdoutiin)
- Rakenna projekti `dotnet build` -komennolla ennen testausta
- Testaa Inspectorilla visuaalista virheenkorjausta varten
- Kaikki lokitus menee automaattisesti stderr:iin
- Palvelin käsittelee sulkemissignaalit hallitusti

Tämä ratkaisu noudattaa nykyistä MCP-määritystä ja näyttää parhaat käytännöt stdio-kuljetuksen toteuttamiseen .NET:llä.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.