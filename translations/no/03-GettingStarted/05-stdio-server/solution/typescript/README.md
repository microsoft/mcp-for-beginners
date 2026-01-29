# MCP stdio Server - TypeScript-løsning

> **⚠️ Viktig**: Denne løsningen er oppdatert til å bruke **stdio transport** som anbefalt av MCP-spesifikasjonen 2025-06-18. Den opprinnelige SSE-transporten er utfaset.

## Oversikt

Denne TypeScript-løsningen viser hvordan man bygger en MCP-server ved hjelp av den nåværende stdio-transporten. Stdio-transporten er enklere, mer sikker og gir bedre ytelse enn den utgåtte SSE-tilnærmingen.

## Forutsetninger

- Node.js 18+ eller nyere
- npm eller yarn pakkebehandler

## Oppsettinstruksjoner

### Steg 1: Installer avhengighetene

```bash
npm install
```

### Steg 2: Bygg prosjektet

```bash
npm run build
```

## Kjøre serveren

Stdio-serveren fungerer annerledes enn den gamle SSE-serveren. I stedet for å starte en webserver, kommuniserer den via stdin/stdout:

```bash
npm start
```

**Viktig**: Serveren vil se ut som den henger – dette er normalt! Den venter på JSON-RPC-meldinger fra stdin.

## Testing av serveren

### Metode 1: Bruke MCP Inspector (Anbefalt)

```bash
npm run inspector
```

Dette vil:
1. Starte serveren din som en underprosess
2. Åpne et webgrensesnitt for testing
3. La deg teste alle serververktøy interaktivt

### Metode 2: Direkte testing via kommandolinjen

Du kan også teste ved å starte Inspector direkte:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Tilgjengelige verktøy

Serveren tilbyr disse verktøyene:

- **add(a, b)**: Legg sammen to tall
- **multiply(a, b)**: Multipliser to tall  
- **get_greeting(name)**: Generer en personlig hilsen
- **get_server_info()**: Hent informasjon om serveren

### Testing med Claude Desktop

For å bruke denne serveren med Claude Desktop, legg til denne konfigurasjonen i `claude_desktop_config.json`:

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

## Prosjektstruktur

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Viktige forskjeller fra SSE

**stdio transport (Nåværende):**
- ✅ Enklere oppsett – ingen HTTP-server nødvendig
- ✅ Bedre sikkerhet – ingen HTTP-endepunkter
- ✅ Kommunikasjon basert på underprosesser
- ✅ JSON-RPC via stdin/stdout
- ✅ Bedre ytelse

**SSE transport (Utfaset):**
- ❌ Krevde oppsett av Express-server
- ❌ Trengte kompleks ruting og sesjonshåndtering
- ❌ Flere avhengigheter (Express, HTTP-håndtering)
- ❌ Ekstra sikkerhetsvurderinger
- ❌ Nå utfaset i MCP 2025-06-18

## Utviklingstips

- Bruk `console.error()` for logging (aldri `console.log()` da det skriver til stdout)
- Bygg med `npm run build` før testing
- Test med Inspector for visuell feilsøking
- Sørg for at alle JSON-meldinger er riktig formatert
- Serveren håndterer automatisk en ryddig avslutning ved SIGINT/SIGTERM

Denne løsningen følger den nåværende MCP-spesifikasjonen og viser beste praksis for implementering av stdio-transport ved bruk av TypeScript.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.