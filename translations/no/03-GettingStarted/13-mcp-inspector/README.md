# Feilsøking med MCP Inspector

> [!NOTE]
> Kommandoer som bruker `--sse` og URL-er som slutter med `/sse` tester den gamle HTTP+SSE
> transporten. For en ny MCP `2026-07-28`-server, bruk en Inspector-versjon som
> støtter Streamable HTTP og velg den transporten i stedet.

**MCP Inspector** er et essensielt feilsøkingsverktøy som lar deg interaktivt teste og feilsøke dine MCP-servere uten å måtte bruke en full AI-vertsapplikasjon. Tenk på det som "Postman for MCP" - det gir en visuell grensesnitt for å sende forespørsler, se svar og forstå hvordan serveren din oppfører seg.

## Hvorfor bruke MCP Inspector?

Når du bygger MCP-servere, vil du ofte støte på disse utfordringene:

- **"Kjører serveren min i det hele tatt?"** - Inspector viser tilkoblingsstatus
- **"Er verktøyene mine registrert korrekt?"** - Inspector viser alle tilgjengelige verktøy
- **"Hva er svarformatet?"** - Inspector viser fullstendige JSON-svar
- **"Hvorfor fungerer ikke dette verktøyet?"** - Inspector viser detaljerte feilmeldinger

## Forutsetninger

- Node.js 18+ installert
- npm (leveres med Node.js)
- En MCP-server å teste (se [Modul 3.1 - Første Server](../01-first-server/README.md))

## Installasjon

### Alternativ 1: Kjør med npx (Anbefalt for rask testing)

```bash
npx @modelcontextprotocol/inspector
```

### Alternativ 2: Installer globalt

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Alternativ 3: Legg til i ditt prosjekt

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Legg til i `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Koble til din server

### stdio-servere (lokal prosess)

For servere som kommuniserer via standard inn/ut:

```bash
# Python-server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js-server
npx @modelcontextprotocol/inspector node ./build/index.js

# Med miljøvariabler
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP-servere (nettverk)

For servere som kjører som HTTP-tjenester:

1. Start serveren først:
   ```bash
   python server.py  # Server kjører på http://localhost:8080
   ```

2. Start Inspector og koble til:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Oversikt over Inspector-grensesnittet

Når Inspector startes, vil du se et nettgrensesnitt (vanligvis på `http://localhost:5173`):

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

## Testing av verktøy

### Liste tilgjengelige verktøy

1. Klikk på **Tools**-fanen
2. Inspector kaller automatisk `tools/list`
3. Du vil se alle registrerte verktøy med:
   - Verktøynavn
   - Beskrivelse
   - Input-skjema (parametere)

### Kalle et verktøy

1. Velg et verktøy fra listen
2. Fyll inn påkrevde parametere i skjemaet
3. Klikk **Run Tool**
4. Se svaret i resultatpanelet

**Eksempel: Testing av en kalkulatortjeneste**

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

### Feilsøking av verktøyfeil

Når et verktøy feiler, viser Inspector:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Vanlige feilkoder:
| Kode | Betydning |
|------|-----------|
| -32700 | Parsingsfeil (ugyldig JSON) |
| -32600 | Ugyldig forespørsel |
| -32601 | Metode ikke funnet |
| -32602 | Ugyldige parametere |
| -32603 | Intern feil |

---

## Testing av ressurser

### Liste ressurser

1. Klikk på **Resources**-fanen
2. Inspector kaller `resources/list`
3. Du vil se:
   - Ressurs-URIer
   - Navn og beskrivelser
   - MIME-typer

### Lese en ressurs

1. Velg en ressurs
2. Klikk **Read Resource**
3. Se innholdet som returneres

**Eksempel på utdata:**

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

## Testing av prompt

### Liste prompts

1. Klikk på **Prompts**-fanen
2. Inspector kaller `prompts/list`
3. Se tilgjengelige promptmaler

### Hente en prompt

1. Velg en prompt
2. Fyll inn eventuelle påkrevde argumenter
3. Klikk **Get Prompt**
4. Se de gjengitte promptmeldinger

---

## Analyse av meldingslogg

Meldingsloggen viser alle MCP protokollmeldinger. Transkripsjonen nedenfor er fra en
legacy `2025-11-25`-server og inkluderer den fjernede `initialize`-håndtrykksekvensen. En
`2026-07-28`-server bruker selvstendige forespørselsmetadata og `server/discover`
i stedet.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Hva du bør se etter

- **Forespørsel/svar-par**: Hver `→` bør ha en tilsvarende `←`
- **Feilmeldinger**: Se etter `"error"` i svarene
- **Tidsbruk**: Store hull kan indikere ytelsesproblemer
- **Protokollversjon**: Sørg for at server og klient er enige om versjon

---

## Integrasjon med VS Code

Du kan kjøre Inspector direkte fra VS Code:

### Bruke launch.json

Legg til i `.vscode/launch.json`:

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

### Bruke Tasks

Legg til i `.vscode/tasks.json`:

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

## Vanlige feilsøkingsscenarier

### Scenario 1: Server vil ikke koble til

**Symptomer:** Inspector viser "Disconnected" eller henger på "Connecting..."

**Sjekkliste:**
1. ✅ Er serverkommandoen korrekt?
2. ✅ Er alle avhengigheter installert?
3. ✅ Er serverstien absolutt eller relativ til gjeldende katalog?
4. ✅ Er nødvendige miljøvariabler satt?

**Feilsøkingstrinn:**
```bash
# Test serveren manuelt først
python -c "import your_server_module; print('OK')"

# Sjekk for importfeil
python -m your_server_module 2>&1 | head -20

# Bekreft at MCP SDK er installert
pip show mcp
```

### Scenario 2: Verktøy vises ikke

**Symptomer:** Verktøyfanen viser tom liste

**Mulige årsaker:**
1. Verktøy ikke registrert under serverinitialisering
2. Server krasjet etter oppstart
3. `tools/list` behandler returnerer tom matrise

**Feilsøkingstrinn:**
1. Sjekk meldingsloggen for `tools/list`-svar
2. Legg til logging i kode for verktøyregistrering
3. Verifiser at `@mcp.tool()` dekoratører er tilstede (Python)

### Scenario 3: Verktøy returnerer feil

**Symptomer:** Verktøykall returnerer feilsvar

**Feilsøkingsmetode:**
1. Les feilmeldingen nøye
2. Sjekk at parametertyper stemmer med skjemaet
3. Legg til try/catch med detaljerte feilmeldinger
4. Sjekk serverlogger for stacktraces

**Eksempel på forbedret feilhåndtering:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Verktøylogikk her
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenario 4: Ressursinnhold tomt

**Symptomer:** Ressurs returnerer, men innholdet er tomt eller null

**Sjekkliste:**
1. ✅ Filsti eller URI er korrekt
2. ✅ Server har tillatelse til å lese ressursen
3. ✅ Ressursinnhold returneres korrekt

---

## Avanserte Inspector-funksjoner

### Egendefinerte headere (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Detaljert logging

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Opptak av økter

Inspector kan eksportere meldingslogger for senere analyse:
1. Klikk **Export Log** i meldingspanelet
2. Lagre JSON-filen
3. Del med teammedlemmer for feilsøking

---

## Beste praksis

1. **Test tidlig og ofte** - Bruk Inspector under utvikling, ikke bare når ting bryter
2. **Start enkelt** - Test grunnleggende tilkobling før komplekse verktøyskall
3. **Sjekk skjemaet** - Mange feil skyldes parameter-typefeil
4. **Les feilmeldinger** - MCP-feil er vanligvis beskrivende
5. **Hold Inspector åpen** - Det hjelper deg å fange opp problemer mens du utvikler

---

## Hva nå?

Du har fullført Modul 3: Komme i gang! Fortsett læringen din:

- [Modul 4: Praktisk implementering](../../04-PracticalImplementation/README.md)

---

## Ytterligere ressurser

- [MCP Inspector GitHub-repositorium](https://github.com/modelcontextprotocol/inspector)
- [MCP Spesifikasjon - Protokollmeldinger](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Spesifikasjon](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->