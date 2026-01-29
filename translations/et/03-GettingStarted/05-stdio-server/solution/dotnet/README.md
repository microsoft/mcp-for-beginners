# MCP stdio Server - .NET Lahendus

> **⚠️ Tähtis**: See lahendus on uuendatud, et kasutada **stdio transporti**, nagu soovitatud MCP Spetsifikatsioonis 2025-06-18. Algne SSE transport on nüüdseks aegunud.

## Ülevaade

See .NET lahendus näitab, kuidas ehitada MCP serverit, kasutades praegust stdio transporti. Stdio transport on lihtsam, turvalisem ja pakub paremat jõudlust võrreldes aegunud SSE lähenemisega.

## Eeltingimused

- .NET 9.0 SDK või uuem
- Põhiline arusaam .NET sõltuvuste süstimisest

## Seadistamise juhised

### Samm 1: Taasta sõltuvused

```bash
dotnet restore
```

### Samm 2: Ehita projekt

```bash
dotnet build
```

## Serveri käivitamine

Stdio server töötab erinevalt vanast HTTP-põhisest serverist. Selle asemel, et käivitada veebiserver, suhtleb see stdin/stdout kaudu:

```bash
dotnet run
```

**Tähtis**: Server näib justkui "hangunud" - see on normaalne! See ootab JSON-RPC sõnumeid stdin kaudu.

## Serveri testimine

### Meetod 1: MCP Inspector kasutamine (soovitatav)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

See teeb järgmist:
1. Käivitab teie serveri alamprotsessina
2. Avab veebiliidese testimiseks
3. Võimaldab teil interaktiivselt testida kõiki serveri tööriistu

### Meetod 2: Otsene testimine käsurealt

Võite testida ka Inspektorit otse käivitades:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Saadaval olevad tööriistad

Server pakub järgmisi tööriistu:

- **AddNumbers(a, b)**: Liidab kaks arvu
- **MultiplyNumbers(a, b)**: Korrutab kaks arvu  
- **GetGreeting(name)**: Loob isikupärastatud tervituse
- **GetServerInfo()**: Annab teavet serveri kohta

### Testimine Claude Desktopiga

Selle serveri kasutamiseks Claude Desktopiga lisage järgmine konfiguratsioon oma `claude_desktop_config.json` faili:

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

## Projekti struktuur

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Peamised erinevused HTTP/SSE-ga võrreldes

**stdio transport (Praegune):**
- ✅ Lihtsam seadistamine - veebiserverit pole vaja
- ✅ Parem turvalisus - HTTP lõpp-punkte pole
- ✅ Kasutab `Host.CreateApplicationBuilder()` asemel `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` asemel `WithHttpTransport()`
- ✅ Konsoolirakendus veebirakenduse asemel
- ✅ Parem jõudlus

**HTTP/SSE transport (Aegunud):**
- ❌ Vajalik ASP.NET Core veebiserver
- ❌ Vajas `app.MapMcp()` marsruutimise seadistust
- ❌ Keerulisem konfiguratsioon ja sõltuvused
- ❌ Täiendavad turvalisuse kaalutlused
- ❌ Nüüd MCP 2025-06-18 spetsifikatsioonis aegunud

## Arenduse funktsioonid

- **Sõltuvuste süstimine**: Täielik DI tugi teenuste ja logimise jaoks
- **Struktureeritud logimine**: Korralik logimine stderr kaudu, kasutades `ILogger<T>`
- **Tööriista atribuudid**: Puhas tööriistade määratlemine `[McpServerTool]` atribuutidega
- **Async tugi**: Kõik tööriistad toetavad asünkroonseid operatsioone
- **Vigade käsitlemine**: Sujuv vigade käsitlemine ja logimine

## Arenduse näpunäited

- Kasutage logimiseks `ILogger` (ärge kunagi kirjutage otse stdout-i)
- Ehitage projekt `dotnet build` abil enne testimist
- Testige Inspektoriga visuaalseks silumiseks
- Kõik logimine suunatakse automaatselt stderr-i
- Server käsitleb sujuvalt sulgemissignaale

See lahendus järgib praegust MCP spetsifikatsiooni ja demonstreerib parimaid tavasid stdio transpordi rakendamiseks .NET-is.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.