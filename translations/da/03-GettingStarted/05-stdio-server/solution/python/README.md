# MCP stdio Server - Python-løsning

> **⚠️ Vigtigt**: Denne løsning er blevet opdateret til at bruge **stdio transport** som anbefalet i MCP-specifikationen 2025-06-18. Den oprindelige SSE transport er blevet udfaset.

## Oversigt

Denne Python-løsning viser, hvordan man bygger en MCP-server ved hjælp af den nuværende stdio transport. Stdio transport er enklere, mere sikker og giver bedre ydeevne end den udfasede SSE-metode.

## Forudsætninger

- Python 3.8 eller nyere
- Det anbefales at installere `uv` til pakkehåndtering, se [instruktioner](https://docs.astral.sh/uv/#highlights)

## Opsætningsinstruktioner

### Trin 1: Opret et virtuelt miljø

```bash
python -m venv venv
```

### Trin 2: Aktivér det virtuelle miljø

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Trin 3: Installer afhængighederne

```bash
pip install mcp
```

## Kørsel af serveren

Stdio-serveren fungerer anderledes end den gamle SSE-server. I stedet for at starte en webserver kommunikerer den via stdin/stdout:

```bash
python server.py
```

**Vigtigt**: Serveren vil tilsyneladende fryse - dette er normalt! Den venter på JSON-RPC-beskeder fra stdin.

## Test af serveren

### Metode 1: Brug MCP Inspector (Anbefalet)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Dette vil:
1. Starte din server som en underproces
2. Åbne en webgrænseflade til test
3. Give dig mulighed for at teste alle serverværktøjer interaktivt

### Metode 2: Direkte JSON-RPC-test

Du kan også teste ved at sende JSON-RPC-beskeder direkte:

1. Start serveren: `python server.py`
2. Send en JSON-RPC-besked (eksempel):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Serveren vil svare med tilgængelige værktøjer

### Tilgængelige værktøjer

Serveren tilbyder disse værktøjer:

- **add(a, b)**: Læg to tal sammen
- **multiply(a, b)**: Gang to tal sammen  
- **get_greeting(name)**: Generer en personlig hilsen
- **get_server_info()**: Få information om serveren

### Test med Claude Desktop

For at bruge denne server med Claude Desktop, tilføj denne konfiguration til din `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Vigtige forskelle fra SSE

**stdio transport (Nuværende):**
- ✅ Enkel opsætning - ingen webserver nødvendig
- ✅ Bedre sikkerhed - ingen HTTP-endpoints
- ✅ Kommunikation baseret på underprocesser
- ✅ JSON-RPC via stdin/stdout
- ✅ Bedre ydeevne

**SSE transport (Udfaset):**
- ❌ Krævede opsætning af HTTP-server
- ❌ Krævede webframework (Starlette/FastAPI)
- ❌ Mere kompleks routing og sessionhåndtering
- ❌ Yderligere sikkerhedsovervejelser
- ❌ Nu udfaset i MCP 2025-06-18

## Fejlfindingstips

- Brug `stderr` til logning (aldrig `stdout`)
- Test med Inspector for visuel fejlfinding
- Sørg for, at alle JSON-beskeder er linjeafgrænsede
- Kontroller, at serveren starter uden fejl

Denne løsning følger den nuværende MCP-specifikation og demonstrerer bedste praksis for stdio transport-implementering.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.