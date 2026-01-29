# MCP stdio Server - Python-lösning

> **⚠️ Viktigt**: Den här lösningen har uppdaterats för att använda **stdio-transport** enligt rekommendationerna i MCP-specifikationen 2025-06-18. Den ursprungliga SSE-transporten har blivit föråldrad.

## Översikt

Den här Python-lösningen visar hur man bygger en MCP-server med den aktuella stdio-transporten. Stdio-transporten är enklare, säkrare och ger bättre prestanda än den föråldrade SSE-metoden.

## Förutsättningar

- Python 3.8 eller senare
- Det rekommenderas att du installerar `uv` för pakethantering, se [instruktioner](https://docs.astral.sh/uv/#highlights)

## Installationsinstruktioner

### Steg 1: Skapa en virtuell miljö

```bash
python -m venv venv
```

### Steg 2: Aktivera den virtuella miljön

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Steg 3: Installera beroenden

```bash
pip install mcp
```

## Köra servern

Stdio-servern fungerar annorlunda än den gamla SSE-servern. Istället för att starta en webbserver kommunicerar den via stdin/stdout:

```bash
python server.py
```

**Viktigt**: Servern kommer att verka hänga sig – detta är normalt! Den väntar på JSON-RPC-meddelanden från stdin.

## Testa servern

### Metod 1: Använd MCP Inspector (Rekommenderas)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Detta kommer att:
1. Starta din server som en subprocess
2. Öppna ett webbgränssnitt för testning
3. Låta dig testa alla serververktyg interaktivt

### Metod 2: Direkt JSON-RPC-testning

Du kan också testa genom att skicka JSON-RPC-meddelanden direkt:

1. Starta servern: `python server.py`
2. Skicka ett JSON-RPC-meddelande (exempel):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Servern svarar med tillgängliga verktyg

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
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Viktiga skillnader från SSE

**Stdio-transport (Nuvarande):**
- ✅ Enklare installation - ingen webbserver behövs
- ✅ Bättre säkerhet - inga HTTP-endpoints
- ✅ Kommunikation baserad på subprocess
- ✅ JSON-RPC via stdin/stdout
- ✅ Bättre prestanda

**SSE-transport (Föråldrad):**
- ❌ Krävde inställning av webbserver
- ❌ Behövde webbframework (Starlette/FastAPI)
- ❌ Mer komplex routing och sessionshantering
- ❌ Ytterligare säkerhetsöverväganden
- ❌ Nu föråldrad i MCP 2025-06-18

## Felsökningstips

- Använd `stderr` för loggning (aldrig `stdout`)
- Testa med Inspector för visuell felsökning
- Se till att alla JSON-meddelanden är avgränsade med ny rad
- Kontrollera att servern startar utan fel

Den här lösningen följer den aktuella MCP-specifikationen och visar bästa praxis för implementering av stdio-transport.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.