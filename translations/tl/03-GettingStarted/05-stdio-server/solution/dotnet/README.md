# MCP stdio Server - .NET Solusyon

> **⚠️ Mahalagang Paalala**: Ang solusyong ito ay na-update upang gamitin ang **stdio transport** ayon sa rekomendasyon ng MCP Specification 2025-06-18. Ang orihinal na SSE transport ay hindi na ginagamit.

## Pangkalahatang-ideya

Ang .NET solusyong ito ay nagpapakita kung paano bumuo ng isang MCP server gamit ang kasalukuyang stdio transport. Ang stdio transport ay mas simple, mas ligtas, at nagbibigay ng mas mahusay na performance kumpara sa hindi na ginagamit na SSE approach.

## Mga Kinakailangan

- .NET 9.0 SDK o mas bago
- Pangunahing kaalaman sa .NET dependency injection

## Mga Hakbang sa Setup

### Hakbang 1: I-restore ang mga dependency

```bash
dotnet restore
```

### Hakbang 2: I-build ang proyekto

```bash
dotnet build
```

## Pagpapatakbo ng Server

Ang stdio server ay tumatakbo nang iba kumpara sa lumang HTTP-based server. Sa halip na magpatakbo ng web server, ito ay nakikipag-ugnayan sa pamamagitan ng stdin/stdout:

```bash
dotnet run
```

**Mahalaga**: Ang server ay magmumukhang nakabitin - normal ito! Naghihintay ito ng mga JSON-RPC na mensahe mula sa stdin.

## Pagsusuri ng Server

### Paraan 1: Gamitin ang MCP Inspector (Inirerekomenda)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Ito ay:
1. Ilulunsad ang iyong server bilang subprocess
2. Magbubukas ng web interface para sa pagsusuri
3. Papayagan kang subukan ang lahat ng tools ng server nang interactive

### Paraan 2: Direktang pagsusuri gamit ang command line

Maaari mo ring subukan sa pamamagitan ng direktang paglulunsad ng Inspector:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Mga Available na Tools

Ang server ay nagbibigay ng mga sumusunod na tools:

- **AddNumbers(a, b)**: Pinagsasama ang dalawang numero
- **MultiplyNumbers(a, b)**: Minumultiply ang dalawang numero  
- **GetGreeting(name)**: Gumagawa ng personalized na pagbati
- **GetServerInfo()**: Nagbibigay ng impormasyon tungkol sa server

### Pagsusuri gamit ang Claude Desktop

Upang magamit ang server na ito sa Claude Desktop, idagdag ang configuration na ito sa iyong `claude_desktop_config.json`:

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

## Estruktura ng Proyekto

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Mga Pangunahing Pagkakaiba mula sa HTTP/SSE

**stdio transport (Kasalukuyan):**
- ✅ Mas simpleng setup - walang kinakailangang web server
- ✅ Mas ligtas - walang HTTP endpoints
- ✅ Gumagamit ng `Host.CreateApplicationBuilder()` sa halip na `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` sa halip na `WithHttpTransport()`
- ✅ Console application sa halip na web application
- ✅ Mas mahusay na performance

**HTTP/SSE transport (Hindi na ginagamit):**
- ❌ Kinakailangan ang ASP.NET Core web server
- ❌ Nangangailangan ng `app.MapMcp()` routing setup
- ❌ Mas kumplikadong configuration at dependencies
- ❌ Karagdagang mga konsiderasyon sa seguridad
- ❌ Hindi na ginagamit simula MCP 2025-06-18

## Mga Tampok sa Pag-develop

- **Dependency Injection**: Buong suporta sa DI para sa mga serbisyo at logging
- **Structured Logging**: Maayos na pag-log sa stderr gamit ang `ILogger<T>`
- **Tool Attributes**: Malinis na pagdedeklara ng tools gamit ang `[McpServerTool]` attributes
- **Async Support**: Lahat ng tools ay sumusuporta sa async operations
- **Error Handling**: Maayos na paghawak ng mga error at pag-log

## Mga Tip sa Pag-develop

- Gamitin ang `ILogger` para sa pag-log (huwag direktang magsulat sa stdout)
- I-build gamit ang `dotnet build` bago mag-test
- Subukan gamit ang Inspector para sa visual debugging
- Ang lahat ng pag-log ay awtomatikong napupunta sa stderr
- Ang server ay maayos na humahawak ng shutdown signals

Ang solusyong ito ay sumusunod sa kasalukuyang MCP specification at nagpapakita ng pinakamahusay na mga kasanayan para sa stdio transport implementation gamit ang .NET.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.