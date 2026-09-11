# Fejlfinding med MCP Inspector

> [!NOTE]
> Kommandoer, der bruger `--sse` og URL'er, der ender på `/sse`, tester den gamle HTTP+SSE
> transport. For en ny MCP `2026-07-28` server, brug en Inspector-version, der
> understøtter Streamable HTTP og vælg den transport i stedet.

**MCP Inspector** er et vigtigt fejlfindingværktøj, som giver dig mulighed for interaktivt at teste og fejlfinde dine MCP-servere uden at skulle have en fuld AI-værtsapplikation. Tænk på det som "Postman for MCP" - det giver en visuel grænseflade til at sende forespørgsler, se svar og forstå, hvordan din server opfører sig.

## Hvorfor bruge MCP Inspector?

Når du bygger MCP-servere, vil du ofte støde på disse udfordringer:

- **"Kører min server overhovedet?"** - Inspector viser forbindelsesstatus
- **"Er mine værktøjer korrekt registreret?"** - Inspector viser alle tilgængelige værktøjer
- **"Hvad er svarformatet?"** - Inspector viser komplette JSON-svar
- **"Hvorfor virker dette værktøj ikke?"** - Inspector viser detaljerede fejlmeddelelser

## Forudsætninger

- Node.js 18+ installeret
- npm (følger med Node.js)
- En MCP-server til test (se [Module 3.1 - Første Server](../01-first-server/README.md))

## Installation

### Mulighed 1: Kør med npx (anbefalet til hurtig test)

```bash
npx @modelcontextprotocol/inspector
```

### Mulighed 2: Installer globalt

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Mulighed 3: Tilføj til dit projekt

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Tilføj til `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Tilslutning til din server

### stdio-servere (lokal proces)

For servere, der kommunikerer via standard input/output:

```bash
# Python-server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js-server
npx @modelcontextprotocol/inspector node ./build/index.js

# Med miljøvariabler
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP-servere (netværk)

For servere, der kører som HTTP-tjenester:

1. Start din server først:
   ```bash
   python server.py  # Server kører på http://localhost:8080
   ```

2. Start Inspector og opret forbindelse:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Oversigt over Inspector-grænsefladen

Når Inspector starter, vil du se en webgrænseflade (typisk på `http://localhost:5173`):

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

## Test af værktøjer

### Liste over tilgængelige værktøjer

1. Klik på fanen **Værktøjer**
2. Inspector kalder automatisk `tools/list`
3. Du vil se alle registrerede værktøjer med:
   - Værktøjsnavn
   - Beskrivelse
   - Input-skema (parametre)

### Kald et værktøj

1. Vælg et værktøj fra listen
2. Udfyld de nødvendige parametre i formularen
3. Klik på **Kør Værktøj**
4. Se svaret i resultatpanelet

**Eksempel: Test af en lommeregner-værktøj**

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

### Fejlfinding af værktøjsfejl

Når et værktøj fejler, viser Inspector:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Almindelige fejlkoder:
| Kode | Betydning |
|------|---------|
| -32700 | Parse fejl (ugyldig JSON) |
| -32600 | Ugyldig forespørgsel |
| -32601 | Metode ikke fundet |
| -32602 | Ugyldige params |
| -32603 | Intern fejl |

---

## Test af ressourcer

### Liste over ressourcer

1. Klik på fanen **Ressourcer**
2. Inspector kalder `resources/list`
3. Du vil se:
   - Ressource-URI'er
   - Navne og beskrivelser
   - MIME-typer

### Læsning af en ressource

1. Vælg en ressource
2. Klik på **Læs Ressource**
3. Se det returnerede indhold

**Eksempel output:**

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

## Test af prompts

### Liste over prompts

1. Klik på fanen **Prompts**
2. Inspector kalder `prompts/list`
3. Se tilgængelige prompt-skabeloner

### Hent en prompt

1. Vælg en prompt
2. Udfyld eventuelle nødvendige argumenter
3. Klik på **Hent Prompt**
4. Se de gengivne prompt-meddelelser

---

## Analyse af meddelelseslog

Meddelelsesloggen viser alle MCP-protokolmeddelelser. Transskriptionen nedenfor er fra en
ældre `2025-11-25` server og inkluderer den fjernede `initialize` håndtryk. En
`2026-07-28` server bruger selvstændige anmodningsmetadata og `server/discover`
i stedet.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Hvad du skal kigge efter

- **Forespørgsel/Svar-par**: Hver `→` bør have en tilsvarende `←`
- **Fejlmeddelelser**: Se efter `"error"` i svar
- **Timing**: Store huller kan indikere ydelsesproblemer
- **Protokolversion**: Sørg for, at server og klient er enige om versionen

---

## VS Code-integration

Du kan køre Inspector direkte fra VS Code:

### Brug af launch.json

Tilføj til `.vscode/launch.json`:

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

### Brug af Tasks

Tilføj til `.vscode/tasks.json`:

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

## Almindelige fejlfindingstilfælde

### Scenario 1: Server vil ikke oprette forbindelse

**Symptomer:** Inspector viser "Afbundet" eller hænger ved "Opretter forbindelse..."

**Tjekliste:**
1. ✅ Er serverkommandoen korrekt?
2. ✅ Er alle afhængigheder installeret?
3. ✅ Er serverstien absolut eller relativ til den aktuelle mappe?
4. ✅ Er nødvendige miljøvariabler sat?

**Fejlfindingstrin:**
```bash
# Test server manuelt først
python -c "import your_server_module; print('OK')"

# Tjek for importfejl
python -m your_server_module 2>&1 | head -20

# Bekræft at MCP SDK er installeret
pip show mcp
```

### Scenario 2: Værktøjer vises ikke

**Symptomer:** Værktøjsfanen viser en tom liste

**Mulige årsager:**
1. Værktøjer ikke registreret under serverinitialisering
2. Server styrtede ned efter opstart
3. `tools/list` handler returnerer tom array

**Fejlfindingstrin:**
1. Tjek meddelelseslog for `tools/list` svar
2. Tilføj logging til din værktøjsregistreringskode
3. Kontroller, at `@mcp.tool()` dekoratorer er til stede (Python)

### Scenario 3: Værktøj returnerer fejl

**Symptomer:** Værktøjskald returnerer fejlrespons

**Fejlfindingstilgang:**
1. Læs fejlmeddelelsen omhyggeligt
2. Tjek at parametertyper matcher skemaet
3. Tilføj try/catch med detaljerede fejlmeddelelser
4. Tjek serverlogs for stack traces

**Eksempel på forbedret fejlhåndtering:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Værktøjslogik her
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenario 4: Ressourceindhold er tomt

**Symptomer:** Ressourcen returnerer, men indholdet er tomt eller nul

**Tjekliste:**
1. ✅ Filsti eller URI er korrekt
2. ✅ Serveren har tilladelse til at læse ressourcen
3. ✅ Ressourceindhold bliver returneret korrekt

---

## Avancerede Inspector-funktioner

### Egendefinerede headers (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Omfattende logging

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Optagelsessessioner

Inspector kan eksportere meddelelseslogs til senere analyse:
1. Klik på **Eksporter Log** i meddelelsespanelet
2. Gem JSON-filen
3. Del med teammedlemmer til fejlfinding

---

## Bedste praksis

1. **Test tidligt og ofte** - Brug Inspector under udvikling, ikke kun når noget går galt
2. **Start simpelt** - Test grundlæggende tilslutning før komplekse værktøjskald
3. **Tjek skemaet** - Mange fejl skyldes fejltyper mellem parametre
4. **Læs fejlmeddelelser** - MCP-fejl er normalt beskrivende
5. **Hold Inspector åben** - Det hjælper med at fange problemer under udvikling

---

## Hvad nu?

Du har fuldført Modul 3: Kom godt i gang! Fortsæt din læring:

- [Modul 4: Praktisk implementering](../../04-PracticalImplementation/README.md)

---

## Yderligere ressourcer

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP-specifikation - Protokolmeddelelser](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Specifikation](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->