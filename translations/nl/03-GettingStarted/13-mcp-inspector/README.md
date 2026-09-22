# Debuggen met MCP Inspector

> [!NOTE]
> Opdrachten die `--sse` gebruiken en URL's die eindigen op `/sse` testen de legacy HTTP+SSE
> transport. Voor een nieuwe MCP `2026-07-28` server, gebruik een Inspector-versie die
> Streamable HTTP ondersteunt en selecteer die transportmodus in plaats daarvan.

De **MCP Inspector** is een essentieel debughulpmiddel waarmee je interactieve tests kunt uitvoeren en je MCP-servers kunt troubleshooten zonder een volledige AI-hostapplicatie nodig te hebben. Zie het als de "Postman voor MCP" - het biedt een visuele interface om verzoeken te verzenden, antwoorden te bekijken en te begrijpen hoe je server zich gedraagt.

## Waarom MCP Inspector gebruiken?

Bij het bouwen van MCP-servers kom je vaak de volgende uitdagingen tegen:

- **"Draait mijn server eigenlijk?"** - Inspector toont de verbindingsstatus
- **"Zijn mijn tools correct geregistreerd?"** - Inspector toont alle beschikbare tools
- **"Wat is het antwoordformaat?"** - Inspector toont volledige JSON-antwoorden
- **"Waarom werkt deze tool niet?"** - Inspector toont gedetailleerde foutmeldingen

## Vereisten

- Node.js 18+ geïnstalleerd
- npm (wordt meegeleverd met Node.js)
- Een MCP-server om te testen (zie [Module 3.1 - Eerste Server](../01-first-server/README.md))

## Installatie

### Optie 1: Direct uitvoeren met npx (Aanbevolen voor snelle tests)

```bash
npx @modelcontextprotocol/inspector
```

### Optie 2: Globaal installeren

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Optie 3: Toevoegen aan je project

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Toevoegen aan `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Verbinden met je server

### stdio-servers (Lokaal proces)

Voor servers die communiceren via standaard invoer/uitvoer:

```bash
# Python-server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js-server
npx @modelcontextprotocol/inspector node ./build/index.js

# Met omgevingsvariabelen
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP-servers (Netwerk)

Voor servers die draaien als HTTP-services:

1. Start eerst je server:
   ```bash
   python server.py  # Server draait op http://localhost:8080
   ```

2. Start Inspector en maak verbinding:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Overzicht van de Inspector-interface

Als Inspector start, zie je een webinterface (meestal op `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Tools testen

### Beschikbare tools weergeven

1. Klik op het tabblad **Tools**
2. Inspector roept automatisch `tools/list` op
3. Je ziet alle geregistreerde tools met:
   - Naam van de tool
   - Beschrijving
   - Invoerschema (parameters)

### Een tool aanroepen

1. Selecteer een tool uit de lijst
2. Vul de vereiste parameters in het formulier in
3. Klik op **Run Tool**
4. Bekijk het antwoord in het resultatenpaneel

**Voorbeeld: testen van een rekenmachinetool**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Fouten in tools debuggen

Als een tool faalt, toont Inspector:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Veelvoorkomende foutcodes:
| Code | Betekenis |
|------|-----------|
| -32700 | Parse-fout (ongeldige JSON) |
| -32600 | Ongeldig verzoek |
| -32601 | Methode niet gevonden |
| -32602 | Ongeldige parameters |
| -32603 | Interne fout |

---

## Resources testen

### Resources weergeven

1. Klik op het tabblad **Resources**
2. Inspector roept `resources/list` op
3. Je ziet:
   - Resource-URI's
   - Namen en beschrijvingen
   - MIME-typen

### Een resource lezen

1. Selecteer een resource
2. Klik op **Read Resource**
3. Bekijk de teruggegeven inhoud

**Voorbeelduitvoer:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Prompts testen

### Prompts weergeven

1. Klik op het tabblad **Prompts**
2. Inspector roept `prompts/list` op
3. Bekijk beschikbare prompt-sjablonen

### Een prompt ophalen

1. Selecteer een prompt
2. Vul vereiste argumenten in
3. Klik op **Get Prompt**
4. Bekijk de gerenderde promptberichten

---

## Analyse van berichtlogboeken

Het berichtlogboek toont alle MCP-protocolberichten. De transcriptie hieronder is van een
legacy `2025-11-25` server en bevat de verwijderde `initialize` handshake. Een
`2026-07-28` server gebruikt zelfvoorzienende requestmetadata en `server/discover`
in plaats daarvan.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Waar op te letten

- **Request/Response-paren**: Elke `→` moet een bijpassende `←` hebben
- **Foutmeldingen**: Zoek naar `"error"` in antwoorden
- **Tijdstip**: Grote pauzes kunnen prestatieproblemen aangeven
- **Protocolversie**: Zorg dat server en client het eens zijn over de versie

---

## VS Code-integratie

Je kunt Inspector direct vanuit VS Code starten:

### Met launch.json

Toevoegen aan `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Met Tasks

Toevoegen aan `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Veelvoorkomende debugscenario's

### Scenario 1: Server maakt geen verbinding

**Symptomen:** Inspector toont "Disconnected" of blijft hangen op "Connecting..."

**Checklist:**
1. ✅ Is de serveropdracht correct?
2. ✅ Zijn alle afhankelijkheden geïnstalleerd?
3. ✅ Is het serverpad absoluut of relatief ten opzichte van de huidige map?
4. ✅ Zijn vereiste omgevingsvariabelen ingesteld?

**Debugstappen:**
```bash
# Test de server eerst handmatig
python -c "import your_server_module; print('OK')"

# Controleer op importfouten
python -m your_server_module 2>&1 | head -20

# Controleer of MCP SDK is geïnstalleerd
pip show mcp
```

### Scenario 2: Tools verschijnen niet

**Symptomen:** Het tabblad Tools toont een lege lijst

**Mogelijke oorzaken:**
1. Tools niet geregistreerd tijdens serverinitialisatie
2. Server crashte na het opstarten
3. `tools/list` handler retourneert een lege array

**Debugstappen:**
1. Controleer het berichtlogboek op `tools/list` antwoord
2. Voeg logging toe aan je tool-registratiecode
3. Controleer of `@mcp.tool()` decorateurs aanwezig zijn (Python)

### Scenario 3: Tool retourneert fout

**Symptomen:** Tool-aanroep geeft een foutantwoord terug

**Debug-aanpak:**
1. Lees het foutbericht zorgvuldig
2. Controleer of parametertypen overeenkomen met het schema
3. Voeg try/catch toe met gedetailleerde foutmeldingen
4. Controleer serverlogboeken op stacktraces

**Voorbeeld van verbeterde foutafhandeling:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Gereedschapslogica hier
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenario 4: Inhoud resource is leeg

**Symptomen:** Resource wordt geretourneerd, maar de inhoud is leeg of null

**Checklist:**
1. ✅ Bestandspad of URI is correct
2. ✅ Server heeft toestemming om de resource te lezen
3. ✅ Resource-inhoud wordt correct teruggegeven

---

## Geavanceerde Inspector-functies

### Aangepaste headers (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Uitgebreide logging

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Sessies opnemen

Inspector kan berichtlogboeken exporteren voor latere analyse:
1. Klik op **Export Log** in het berichtenpaneel
2. Sla het JSON-bestand op
3. Deel met teamleden voor debugging

---

## Beste praktijken

1. **Test vroeg en vaak** - Gebruik Inspector tijdens ontwikkeling, niet alleen als er iets misgaat
2. **Begin eenvoudig** - Test basisconnectiviteit voordat je complexe toolaanroepen doet
3. **Controleer het schema** - Veel fouten ontstaan door verkeerde parameter-types
4. **Lees foutmeldingen** - MCP-fouten zijn meestal beschrijvend
5. **Houd Inspector open** - Het helpt problemen te signaleren tijdens ontwikkeling

---

## Wat nu?

Je hebt Module 3: Aan de slag voltooid! Ga verder met je leren:

- [Module 4: Praktische implementatie](../../04-PracticalImplementation/README.md)

---

## Extra bronnen

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Specificatie - Protocolberichten](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Specificatie](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->