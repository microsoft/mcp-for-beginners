# MCP stdio Server - Python-løsning

> **⚠️ Viktig**: Denne løsningen er oppdatert til å bruke **stdio transport** som anbefalt av MCP-spesifikasjonen 2025-06-18. Den opprinnelige SSE-transporten er utfaset.

## Oversikt

Denne Python-løsningen viser hvordan man bygger en MCP-server ved hjelp av den nåværende stdio-transporten. Stdio-transporten er enklere, mer sikker og gir bedre ytelse enn den utgåtte SSE-metoden.

## Forutsetninger

- Python 3.8 eller nyere
- Det anbefales å installere `uv` for pakkebehandling, se [instruksjoner](https://docs.astral.sh/uv/#highlights)

## Oppsettinstruksjoner

### Steg 1: Opprett et virtuelt miljø

```bash
python -m venv venv
```

### Steg 2: Aktiver det virtuelle miljøet

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Steg 3: Installer avhengighetene

```bash
pip install mcp
```

## Kjøre serveren

Stdio-serveren fungerer annerledes enn den gamle SSE-serveren. I stedet for å starte en webserver, kommuniserer den via stdin/stdout:

```bash
python server.py
```

**Viktig**: Serveren vil se ut som den henger – dette er normalt! Den venter på JSON-RPC-meldinger fra stdin.

## Testing av serveren

### Metode 1: Bruke MCP Inspector (Anbefalt)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Dette vil:
1. Starte serveren som en underprosess
2. Åpne et webgrensesnitt for testing
3. La deg teste alle serververktøy interaktivt

### Metode 2: Direkte JSON-RPC-testing

Du kan også teste ved å sende JSON-RPC-meldinger direkte:

1. Start serveren: `python server.py`
2. Send en JSON-RPC-melding (eksempel):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Serveren vil svare med tilgjengelige verktøy

### Tilgjengelige verktøy

Serveren tilbyr disse verktøyene:

- **add(a, b)**: Legg sammen to tall
- **multiply(a, b)**: Multipliser to tall  
- **get_greeting(name)**: Generer en personlig hilsen
- **get_server_info()**: Få informasjon om serveren

### Testing med Claude Desktop

For å bruke denne serveren med Claude Desktop, legg til denne konfigurasjonen i `claude_desktop_config.json`:

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

## Viktige forskjeller fra SSE

**stdio transport (Nåværende):**
- ✅ Enklere oppsett – ingen webserver nødvendig
- ✅ Bedre sikkerhet – ingen HTTP-endepunkter
- ✅ Kommunikasjon basert på underprosesser
- ✅ JSON-RPC via stdin/stdout
- ✅ Bedre ytelse

**SSE transport (Utfaset):**
- ❌ Krevde oppsett av HTTP-server
- ❌ Trengte webrammeverk (Starlette/FastAPI)
- ❌ Mer kompleks ruting og sesjonshåndtering
- ❌ Ekstra sikkerhetsvurderinger
- ❌ Nå utfaset i MCP 2025-06-18

## Feilsøkingsråd

- Bruk `stderr` for logging (aldri `stdout`)
- Test med Inspector for visuell feilsøking
- Sørg for at alle JSON-meldinger er linjeavgrenset
- Sjekk at serveren starter uten feil

Denne løsningen følger den nåværende MCP-spesifikasjonen og viser beste praksis for implementering av stdio-transport.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.