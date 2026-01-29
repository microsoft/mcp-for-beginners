# MCP stdio Server - .NET Rješenje

> **⚠️ Važno**: Ovo rješenje je ažurirano kako bi koristilo **stdio transport** prema preporuci MCP Specifikacije 2025-06-18. Izvorni SSE transport je ukinut.

## Pregled

Ovo .NET rješenje pokazuje kako izraditi MCP server koristeći trenutni stdio transport. Stdio transport je jednostavniji, sigurniji i pruža bolje performanse od zastarjelog SSE pristupa.

## Preduvjeti

- .NET 9.0 SDK ili noviji
- Osnovno razumijevanje .NET dependency injectiona

## Upute za postavljanje

### Korak 1: Obnova ovisnosti

```bash
dotnet restore
```

### Korak 2: Izgradnja projekta

```bash
dotnet build
```

## Pokretanje servera

Stdio server radi drugačije od starog servera temeljenog na HTTP-u. Umjesto pokretanja web servera, komunicira putem stdin/stdout:

```bash
dotnet run
```

**Važno**: Server će izgledati kao da se "zamrznuo" - to je normalno! Čeka JSON-RPC poruke putem stdin-a.

## Testiranje servera

### Metoda 1: Korištenje MCP Inspectora (Preporučeno)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Ovo će:
1. Pokrenuti vaš server kao podproces
2. Otvoriti web sučelje za testiranje
3. Omogućiti interaktivno testiranje svih alata servera

### Metoda 2: Testiranje putem naredbenog retka

Možete testirati i pokretanjem Inspectora direktno:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Dostupni alati

Server pruža sljedeće alate:

- **AddNumbers(a, b)**: Zbraja dva broja
- **MultiplyNumbers(a, b)**: Množi dva broja  
- **GetGreeting(name)**: Generira personalizirani pozdrav
- **GetServerInfo()**: Dohvaća informacije o serveru

### Testiranje s Claude Desktopom

Za korištenje ovog servera s Claude Desktopom, dodajte ovu konfiguraciju u vaš `claude_desktop_config.json`:

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

## Struktura projekta

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Ključne razlike između HTTP/SSE

**stdio transport (Trenutni):**
- ✅ Jednostavnije postavljanje - nije potreban web server
- ✅ Bolja sigurnost - nema HTTP endpointa
- ✅ Koristi `Host.CreateApplicationBuilder()` umjesto `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` umjesto `WithHttpTransport()`
- ✅ Konzolna aplikacija umjesto web aplikacije
- ✅ Bolje performanse

**HTTP/SSE transport (Zastarjelo):**
- ❌ Zahtijevao ASP.NET Core web server
- ❌ Trebao `app.MapMcp()` za postavljanje ruta
- ❌ Složenija konfiguracija i ovisnosti
- ❌ Dodatni sigurnosni izazovi
- ❌ Sada ukinut u MCP 2025-06-18

## Značajke razvoja

- **Dependency Injection**: Potpuna podrška za DI za servise i logiranje
- **Strukturirano logiranje**: Ispravno logiranje na stderr koristeći `ILogger<T>`
- **Atributi alata**: Čisto definiranje alata koristeći `[McpServerTool]` atribute
- **Podrška za async**: Svi alati podržavaju asinhrone operacije
- **Rukovanje greškama**: Elegantno rukovanje greškama i logiranje

## Savjeti za razvoj

- Koristite `ILogger` za logiranje (nikada ne pišite direktno na stdout)
- Izgradite projekt s `dotnet build` prije testiranja
- Testirajte s Inspectorom za vizualno otklanjanje grešaka
- Svi logovi automatski idu na stderr
- Server podržava signale za elegantno gašenje

Ovo rješenje slijedi trenutnu MCP specifikaciju i demonstrira najbolje prakse za implementaciju stdio transporta koristeći .NET.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.