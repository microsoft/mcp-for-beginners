# MCP stdio Server - TypeScript-lösning

> **⚠️ Viktigt**: Den här lösningen har uppdaterats för att använda **stdio-transport** enligt rekommendationerna i MCP-specifikationen 2025-06-18. Den ursprungliga SSE-transporten har avvecklats.

## Översikt

Den här TypeScript-lösningen visar hur man bygger en MCP-server med den aktuella stdio-transporten. Stdio-transporten är enklare, säkrare och ger bättre prestanda än den avvecklade SSE-metoden.

## Förutsättningar

- Node.js 18+ eller senare
- npm eller yarn som pakethanterare

## Installationsinstruktioner

### Steg 1: Installera beroenden

```bash
npm install
```

### Steg 2: Bygg projektet

```bash
npm run build
```

## Köra servern

Stdio-servern fungerar annorlunda än den gamla SSE-servern. Istället för att starta en webbserver kommunicerar den via stdin/stdout:

```bash
npm start
```

**Viktigt**: Servern kommer att verka "hänga" – detta är normalt! Den väntar på JSON-RPC-meddelanden från stdin.

## Testa servern

### Metod 1: Använd MCP Inspector (Rekommenderas)

```bash
npm run inspector
```

Detta kommer att:
1. Starta din server som en subprocess
2. Öppna ett webbgränssnitt för testning
3. Låta dig testa alla serververktyg interaktivt

### Metod 2: Direkt testning via kommandoraden

Du kan också testa genom att starta Inspectorn direkt:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Tillgängliga verktyg

Servern tillhandahåller följande verktyg:

- **add(a, b)**: Addera två tal
- **multiply(a, b)**: Multiplicera två tal  
- **get_greeting(name)**: Generera en personlig hälsning
- **get_server_info()**: Hämta information om servern

### Testa med Claude Desktop

För att använda den här servern med Claude Desktop, lägg till följande konfiguration i din `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Projektstruktur

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Viktiga skillnader från SSE

**stdio-transport (Nuvarande):**
- ✅ Enklare installation – ingen HTTP-server behövs
- ✅ Bättre säkerhet – inga HTTP-endpoints
- ✅ Kommunikation baserad på subprocess
- ✅ JSON-RPC via stdin/stdout
- ✅ Bättre prestanda

**SSE-transport (Avvecklad):**
- ❌ Krävde installation av Express-server
- ❌ Behövde komplex routing och sessionshantering
- ❌ Fler beroenden (Express, HTTP-hantering)
- ❌ Ytterligare säkerhetsöverväganden
- ❌ Nu avvecklad i MCP 2025-06-18

## Utvecklingstips

- Använd `console.error()` för loggning (aldrig `console.log()` eftersom det skriver till stdout)
- Bygg med `npm run build` innan testning
- Testa med Inspectorn för visuell felsökning
- Säkerställ att alla JSON-meddelanden är korrekt formaterade
- Servern hanterar automatiskt en smidig avstängning vid SIGINT/SIGTERM

Den här lösningen följer den aktuella MCP-specifikationen och visar bästa praxis för implementering av stdio-transport med TypeScript.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.