# MCP stdio Server - .NET Suluhisho

> **⚠️ Muhimu**: Suluhisho hili limeboreshwa kutumia **stdio transport** kama ilivyopendekezwa na MCP Specification 2025-06-18. Njia ya awali ya SSE imeachwa.

## Muhtasari

Suluhisho hili la .NET linaonyesha jinsi ya kujenga seva ya MCP kwa kutumia stdio transport ya sasa. Stdio transport ni rahisi, salama zaidi, na inatoa utendaji bora kuliko njia ya zamani ya SSE.

## Mahitaji ya Awali

- .NET 9.0 SDK au toleo jipya zaidi
- Uelewa wa msingi wa sindikizo la utegemezi la .NET

## Maelekezo ya Usanidi

### Hatua ya 1: Rejesha utegemezi

```bash
dotnet restore
```

### Hatua ya 2: Jenga mradi

```bash
dotnet build
```

## Kuendesha Seva

Seva ya stdio inaendeshwa tofauti na seva ya zamani inayotegemea HTTP. Badala ya kuanzisha seva ya wavuti, inawasiliana kupitia stdin/stdout:

```bash
dotnet run
```

**Muhimu**: Seva itaonekana kama imekwama - hili ni la kawaida! Inasubiri ujumbe wa JSON-RPC kutoka stdin.

## Kupima Seva

### Njia ya 1: Kutumia MCP Inspector (Inapendekezwa)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Hii itafanya:
1. Kuzindua seva yako kama mchakato wa chini
2. Kufungua kiolesura cha wavuti kwa ajili ya kupima
3. Kukuruhusu kupima zana zote za seva kwa njia ya mwingiliano

### Njia ya 2: Kupima moja kwa moja kupitia mstari wa amri

Unaweza pia kupima kwa kuzindua Inspector moja kwa moja:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Zana Zinazopatikana

Seva inatoa zana hizi:

- **AddNumbers(a, b)**: Ongeza namba mbili pamoja
- **MultiplyNumbers(a, b)**: Zidisha namba mbili  
- **GetGreeting(name)**: Tengeneza salamu ya kibinafsi
- **GetServerInfo()**: Pata taarifa kuhusu seva

### Kupima na Claude Desktop

Ili kutumia seva hii na Claude Desktop, ongeza usanidi huu kwenye `claude_desktop_config.json`:

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

## Muundo wa Mradi

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Tofauti Muhimu kutoka HTTP/SSE

**Stdio transport (Ya sasa):**
- ✅ Usanidi rahisi - hakuna seva ya wavuti inayohitajika
- ✅ Usalama bora - hakuna sehemu za mwisho za HTTP
- ✅ Inatumia `Host.CreateApplicationBuilder()` badala ya `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` badala ya `WithHttpTransport()`
- ✅ Programu ya console badala ya programu ya wavuti
- ✅ Utendaji bora

**HTTP/SSE transport (Imeachwa):**
- ❌ Ilihitaji seva ya wavuti ya ASP.NET Core
- ❌ Ilihitaji usanidi wa njia `app.MapMcp()`
- ❌ Usanidi na utegemezi tata zaidi
- ❌ Masuala ya ziada ya usalama
- ❌ Sasa imeachwa katika MCP 2025-06-18

## Vipengele vya Maendeleo

- **Sindikizo la Utegemezi**: Msaada kamili wa DI kwa huduma na uandishi wa kumbukumbu
- **Uandishi wa Kumbukumbu Ulioandaliwa**: Uandishi sahihi wa kumbukumbu kwa stderr ukitumia `ILogger<T>`
- **Sifa za Zana**: Ufafanuzi safi wa zana ukitumia sifa za `[McpServerTool]`
- **Msaada wa Async**: Zana zote zina msaada wa operesheni za async
- **Ushughulikiaji wa Makosa**: Ushughulikiaji mzuri wa makosa na uandishi wa kumbukumbu

## Vidokezo vya Maendeleo

- Tumia `ILogger` kwa uandishi wa kumbukumbu (kamwe usiandike moja kwa moja kwa stdout)
- Jenga kwa `dotnet build` kabla ya kupima
- Pima na Inspector kwa ufuatiliaji wa kuona
- Kumbukumbu zote zinaenda moja kwa moja kwa stderr
- Seva inashughulikia ishara za kuzimwa kwa utaratibu

Suluhisho hili linafuata maelezo ya sasa ya MCP na linaonyesha mbinu bora za utekelezaji wa stdio transport kwa kutumia .NET.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.