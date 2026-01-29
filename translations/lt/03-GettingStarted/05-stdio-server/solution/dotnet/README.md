# MCP stdio Server - .NET Sprendimas

> **⚠️ Svarbu**: Šis sprendimas buvo atnaujintas, kad naudotų **stdio transportą**, kaip rekomenduojama MCP specifikacijoje 2025-06-18. Originalus SSE transportas yra nebenaudojamas.

## Apžvalga

Šis .NET sprendimas demonstruoja, kaip sukurti MCP serverį naudojant dabartinį stdio transportą. Stdio transportas yra paprastesnis, saugesnis ir užtikrina geresnį našumą nei nebenaudojamas SSE metodas.

## Reikalavimai

- .NET 9.0 SDK ar naujesnė versija
- Pagrindinės žinios apie .NET priklausomybių injekciją

## Nustatymo instrukcijos

### 1 žingsnis: Atkurkite priklausomybes

```bash
dotnet restore
```

### 2 žingsnis: Sukurkite projektą

```bash
dotnet build
```

## Serverio paleidimas

Stdio serveris veikia kitaip nei senasis HTTP pagrindu sukurtas serveris. Vietoj interneto serverio paleidimo jis komunikuoja per stdin/stdout:

```bash
dotnet run
```

**Svarbu**: Serveris gali atrodyti kaip užstrigęs – tai normalu! Jis laukia JSON-RPC pranešimų iš stdin.

## Serverio testavimas

### 1 metodas: Naudojant MCP Inspector (Rekomenduojama)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Tai atliks:
1. Paleis jūsų serverį kaip subprocesą
2. Atidarys interneto sąsają testavimui
3. Leis interaktyviai testuoti visus serverio įrankius

### 2 metodas: Tiesioginis testavimas komandinėje eilutėje

Taip pat galite testuoti paleisdami Inspector tiesiogiai:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Galimi įrankiai

Serveris siūlo šiuos įrankius:

- **AddNumbers(a, b)**: Sudėti du skaičius
- **MultiplyNumbers(a, b)**: Padauginti du skaičius  
- **GetGreeting(name)**: Sukurti asmeninį pasveikinimą
- **GetServerInfo()**: Gauti informaciją apie serverį

### Testavimas su Claude Desktop

Norėdami naudoti šį serverį su Claude Desktop, pridėkite šią konfigūraciją į savo `claude_desktop_config.json`:

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

## Projekto struktūra

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Pagrindiniai skirtumai nuo HTTP/SSE

**Stdio transportas (Dabartinis):**
- ✅ Paprastesnis nustatymas – nereikia interneto serverio
- ✅ Geresnis saugumas – nėra HTTP galinių taškų
- ✅ Naudoja `Host.CreateApplicationBuilder()` vietoj `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` vietoj `WithHttpTransport()`
- ✅ Konsolės programa vietoj interneto programos
- ✅ Geresnis našumas

**HTTP/SSE transportas (Nebenaudojamas):**
- ❌ Reikėjo ASP.NET Core interneto serverio
- ❌ Reikėjo `app.MapMcp()` maršrutų nustatymo
- ❌ Sudėtingesnė konfigūracija ir priklausomybės
- ❌ Papildomi saugumo aspektai
- ❌ Nebenaudojamas MCP 2025-06-18 specifikacijoje

## Kūrimo funkcijos

- **Priklausomybių injekcija**: Pilnas DI palaikymas paslaugoms ir registravimui
- **Struktūrizuotas registravimas**: Tinkamas registravimas į stderr naudojant `ILogger<T>`
- **Įrankių atributai**: Švarus įrankių apibrėžimas naudojant `[McpServerTool]` atributus
- **Async palaikymas**: Visi įrankiai palaiko asinchronines operacijas
- **Klaidų tvarkymas**: Sklandus klaidų tvarkymas ir registravimas

## Kūrimo patarimai

- Naudokite `ILogger` registravimui (niekada nerašykite tiesiogiai į stdout)
- Sukurkite projektą su `dotnet build` prieš testavimą
- Testuokite su Inspector vizualiam derinimui
- Visi registravimo duomenys automatiškai siunčiami į stderr
- Serveris tvarko sklandų uždarymo signalų apdorojimą

Šis sprendimas atitinka dabartinę MCP specifikaciją ir demonstruoja geriausią praktiką stdio transporto įgyvendinimui naudojant .NET.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.