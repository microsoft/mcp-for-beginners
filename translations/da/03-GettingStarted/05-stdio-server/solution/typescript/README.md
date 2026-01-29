# MCP stdio Server - TypeScript-løsning

> **⚠️ Vigtigt**: Denne løsning er blevet opdateret til at bruge **stdio transport** som anbefalet i MCP-specifikationen 2025-06-18. Den oprindelige SSE-transport er blevet udfaset.

## Oversigt

Denne TypeScript-løsning viser, hvordan man bygger en MCP-server ved hjælp af den nuværende stdio transport. Stdio transport er enklere, mere sikker og giver bedre ydeevne end den udfasede SSE-metode.

## Forudsætninger

- Node.js 18+ eller nyere
- npm eller yarn pakkehåndtering

## Opsætningsinstruktioner

### Trin 1: Installer afhængigheder

```bash
npm install
```

### Trin 2: Byg projektet

```bash
npm run build
```

## Kørsel af serveren

Stdio-serveren fungerer anderledes end den gamle SSE-server. I stedet for at starte en webserver kommunikerer den via stdin/stdout:

```bash
npm start
```

**Vigtigt**: Serveren vil tilsyneladende fryse - dette er normalt! Den venter på JSON-RPC-beskeder fra stdin.

## Test af serveren

### Metode 1: Brug af MCP Inspector (Anbefalet)

```bash
npm run inspector
```

Dette vil:
1. Starte din server som en underproces
2. Åbne en webgrænseflade til test
3. Give dig mulighed for at teste alle serverværktøjer interaktivt

### Metode 2: Direkte test via kommandolinjen

Du kan også teste ved at starte Inspector direkte:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Tilgængelige værktøjer

Serveren tilbyder følgende værktøjer:

- **add(a, b)**: Læg to tal sammen
- **multiply(a, b)**: Gang to tal sammen  
- **get_greeting(name)**: Generer en personlig hilsen
- **get_server_info()**: Hent information om serveren

### Test med Claude Desktop

For at bruge denne server med Claude Desktop, tilføj denne konfiguration til din `claude_desktop_config.json`:

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

## Vigtige forskelle fra SSE

**stdio transport (Nuværende):**
- ✅ Simpel opsætning - ingen HTTP-server nødvendig
- ✅ Bedre sikkerhed - ingen HTTP-endpoints
- ✅ Kommunikation baseret på underprocesser
- ✅ JSON-RPC via stdin/stdout
- ✅ Bedre ydeevne

**SSE transport (Udfaset):**
- ❌ Krævede opsætning af Express-server
- ❌ Krævede kompleks routing og sessionhåndtering
- ❌ Flere afhængigheder (Express, HTTP-håndtering)
- ❌ Yderligere sikkerhedsovervejelser
- ❌ Nu udfaset i MCP 2025-06-18

## Udviklingstips

- Brug `console.error()` til logning (aldrig `console.log()`, da det skriver til stdout)
- Byg med `npm run build` før test
- Test med Inspector for visuel fejlfinding
- Sørg for, at alle JSON-beskeder er korrekt formateret
- Serveren håndterer automatisk en korrekt nedlukning ved SIGINT/SIGTERM

Denne løsning følger den nuværende MCP-specifikation og demonstrerer bedste praksis for stdio transport-implementering med TypeScript.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.