# MCP stdio Server - .NET Oplossing

> **⚠️ Belangrijk**: Deze oplossing is bijgewerkt om gebruik te maken van het **stdio transport**, zoals aanbevolen in de MCP Specificatie 2025-06-18. Het oorspronkelijke SSE transport is afgeschaft.

## Overzicht

Deze .NET oplossing laat zien hoe je een MCP-server bouwt met het huidige stdio transport. Het stdio transport is eenvoudiger, veiliger en biedt betere prestaties dan de verouderde SSE aanpak.

## Vereisten

- .NET 9.0 SDK of later
- Basiskennis van .NET dependency injection

## Installatie-instructies

### Stap 1: Herstel afhankelijkheden

```bash
dotnet restore
```

### Stap 2: Bouw het project

```bash
dotnet build
```

## De server uitvoeren

De stdio server werkt anders dan de oude HTTP-gebaseerde server. In plaats van een webserver te starten, communiceert hij via stdin/stdout:

```bash
dotnet run
```

**Belangrijk**: Het lijkt alsof de server vastloopt - dit is normaal! Hij wacht op JSON-RPC berichten via stdin.

## De server testen

### Methode 1: Gebruik de MCP Inspector (Aanbevolen)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dit zal:
1. Je server als subprocess starten
2. Een webinterface openen voor testen
3. Je in staat stellen om alle servertools interactief te testen

### Methode 2: Testen via de commandoregel

Je kunt ook testen door de Inspector direct te starten:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Beschikbare tools

De server biedt de volgende tools:

- **AddNumbers(a, b)**: Twee getallen bij elkaar optellen
- **MultiplyNumbers(a, b)**: Twee getallen met elkaar vermenigvuldigen  
- **GetGreeting(name)**: Een gepersonaliseerde begroeting genereren
- **GetServerInfo()**: Informatie over de server ophalen

### Testen met Claude Desktop

Om deze server te gebruiken met Claude Desktop, voeg je deze configuratie toe aan je `claude_desktop_config.json`:

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

## Projectstructuur

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Belangrijke verschillen met HTTP/SSE

**stdio transport (Huidig):**
- ✅ Eenvoudigere setup - geen webserver nodig
- ✅ Betere beveiliging - geen HTTP endpoints
- ✅ Gebruikt `Host.CreateApplicationBuilder()` in plaats van `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` in plaats van `WithHttpTransport()`
- ✅ Console applicatie in plaats van webapplicatie
- ✅ Betere prestaties

**HTTP/SSE transport (Afgeschaft):**
- ❌ Vereiste een ASP.NET Core webserver
- ❌ Had `app.MapMcp()` routing setup nodig
- ❌ Complexere configuratie en afhankelijkheden
- ❌ Extra beveiligingsmaatregelen
- ❌ Nu afgeschaft in MCP 2025-06-18

## Ontwikkelingsfuncties

- **Dependency Injection**: Volledige DI-ondersteuning voor services en logging
- **Gestructureerde Logging**: Correcte logging naar stderr met `ILogger<T>`
- **Tool Attributen**: Schone tooldefinitie met `[McpServerTool]` attributen
- **Async Ondersteuning**: Alle tools ondersteunen asynchrone operaties
- **Foutafhandeling**: Zorgvuldige foutafhandeling en logging

## Ontwikkelingstips

- Gebruik `ILogger` voor logging (schrijf nooit direct naar stdout)
- Bouw met `dotnet build` voordat je test
- Test met de Inspector voor visuele debugging
- Alle logging gaat automatisch naar stderr
- De server verwerkt afsluitsignalen op een nette manier

Deze oplossing volgt de huidige MCP specificatie en demonstreert best practices voor stdio transport implementatie met .NET.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.