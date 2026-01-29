# MCP stdio Server - .NET Rešitev

> **⚠️ Pomembno**: Ta rešitev je bila posodobljena za uporabo **stdio transporta**, kot je priporočeno v MCP specifikaciji 2025-06-18. Prvotni SSE transport je bil ukinjen.

## Pregled

Ta .NET rešitev prikazuje, kako zgraditi MCP strežnik z uporabo trenutnega stdio transporta. Stdio transport je enostavnejši, bolj varen in zagotavlja boljšo zmogljivost kot ukinjeni SSE pristop.

## Predpogoji

- .NET 9.0 SDK ali novejši
- Osnovno razumevanje .NET odvisnostne injekcije

## Navodila za nastavitev

### Korak 1: Obnovitev odvisnosti

```bash
dotnet restore
```

### Korak 2: Gradnja projekta

```bash
dotnet build
```

## Zagon strežnika

Stdio strežnik deluje drugače kot stari strežnik, ki temelji na HTTP. Namesto zagona spletnega strežnika komunicira prek stdin/stdout:

```bash
dotnet run
```

**Pomembno**: Strežnik se bo zdel, kot da je "zamrznjen" - to je normalno! Čaka na JSON-RPC sporočila prek stdin.

## Testiranje strežnika

### Metoda 1: Uporaba MCP Inspectorja (Priporočeno)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

To bo:
1. Zagnalo vaš strežnik kot podproces
2. Odprlo spletni vmesnik za testiranje
3. Omogočilo interaktivno testiranje vseh orodij strežnika

### Metoda 2: Neposredno testiranje prek ukazne vrstice

Strežnik lahko testirate tudi z neposrednim zagonom Inspectorja:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Razpoložljiva orodja

Strežnik ponuja naslednja orodja:

- **AddNumbers(a, b)**: Sešteje dve števili
- **MultiplyNumbers(a, b)**: Pomnoži dve števili  
- **GetGreeting(name)**: Ustvari personalizirano pozdravno sporočilo
- **GetServerInfo()**: Pridobi informacije o strežniku

### Testiranje s Claude Desktop

Za uporabo tega strežnika s Claude Desktop dodajte to konfiguracijo v vaš `claude_desktop_config.json`:

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

## Ključne razlike med HTTP/SSE

**stdio transport (Trenutni):**
- ✅ Enostavnejša nastavitev - ni potreben spletni strežnik
- ✅ Boljša varnost - ni HTTP končnih točk
- ✅ Uporablja `Host.CreateApplicationBuilder()` namesto `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` namesto `WithHttpTransport()`
- ✅ Konzolna aplikacija namesto spletne aplikacije
- ✅ Boljša zmogljivost

**HTTP/SSE transport (Ukinjen):**
- ❌ Zahteval ASP.NET Core spletni strežnik
- ❌ Potreboval nastavitev `app.MapMcp()` za usmerjanje
- ❌ Bolj zapletena konfiguracija in odvisnosti
- ❌ Dodatni varnostni vidiki
- ❌ Zdaj ukinjen v MCP 2025-06-18

## Razvojne funkcije

- **Odvisnostna injekcija**: Polna podpora DI za storitve in beleženje
- **Strukturirano beleženje**: Pravilno beleženje na stderr z uporabo `ILogger<T>`
- **Atributi orodij**: Čista definicija orodij z uporabo atributov `[McpServerTool]`
- **Podpora za asinhrono delovanje**: Vsa orodja podpirajo asinhrone operacije
- **Obravnava napak**: Elegantno obravnavanje napak in beleženje

## Nasveti za razvoj

- Uporabljajte `ILogger` za beleženje (nikoli neposredno ne pišite na stdout)
- Pred testiranjem gradite z `dotnet build`
- Testirajte z Inspectorjem za vizualno odpravljanje napak
- Vse beleženje se samodejno usmeri na stderr
- Strežnik obravnava signale za elegantno zaustavitev

Ta rešitev sledi trenutni MCP specifikaciji in prikazuje najboljše prakse za implementacijo stdio transporta z uporabo .NET.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.