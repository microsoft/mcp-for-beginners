# Sette opp populære MCP-hostklienter

> [!NOTE]
> Host-konfigurasjoner som peker til `/sse` er eldre HTTP+SSE-eksempler for
> MCP `2025-11-25`. For MCP `2026-07-28`, velg Streamable HTTP i verter som
> støtter det og bruk endepunktet konfigurert av serveren.

Denne guiden dekker hvordan du konfigurerer og bruker MCP-servere med populære AI-hostapplikasjoner. Hver host har sin egen konfigurasjonsmåte, men når de er satt opp, kommuniserer de alle med MCP-servere ved hjelp av standardisert protokoll.

## Hva er en MCP-host?

En **MCP-host** er en AI-applikasjon som kan koble til MCP-servere for å utvide sine funksjoner. Tenk på det som "frontend" som brukerne interagerer med, mens MCP-servere tilbyr "backend" verktøy og data.

```mermaid
flowchart LR
    User[👤 Bruker] --> Host[🖥️ MCP Vert]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Populære verter"
        H1[Claude Skrivebord]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Forutsetninger

- En MCP-server å koble til (se [Modul 3.1 - Første server](../01-first-server/README.md))
- Host-applikasjonen installert på systemet ditt
- Grunnleggende kjennskap til JSON-konfigurasjonsfiler

---

## 1. Claude Desktop

**Claude Desktop** er Anthropics offisielle skrivebordsapplikasjon som støtter MCP nativt.

### Installasjon

1. Last ned Claude Desktop fra [claude.ai/download](https://claude.ai/download)
2. Installer og logg inn med din Anthropic-konto

### Konfigurasjon

Claude Desktop bruker en JSON-konfigurasjonsfil for å definere MCP-servere.

**Konfigurasjonsfilplassering:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Eksempel på konfigurasjon:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Konfigurasjonsvalg

| Felt | Beskrivelse | Eksempel |
|-------|-------------|---------|
| `command` | Kjørbar fil | `"python"`, `"node"`, `"npx"` |
| `args` | Kommandolinjeargumenter | `["-m", "my_server"]` |
| `env` | Miljøvariabler | `{"API_KEY": "xxx"}` |
| `cwd` | Arbeidskatalog | `"/path/to/server"` |

### Teste oppsettet ditt

1. Lagre konfigurasjonsfilen
2. Start Claude Desktop helt på nytt (avslutt og åpne igjen)
3. Åpne en ny samtale
4. Se etter 🔌-ikonet som indikerer tilkoblede servere
5. Prøv å spørre Claude om å bruke ett av verktøyene dine

### Feilsøking av Claude Desktop

**Server vises ikke:**
- Sjekk syntaks i konfigurasjonsfilen med en JSON-validator
- Sørg for at kommando-banen er korrekt
- Sjekk Claude Desktop logger: Hjelp → Vis logger

**Server krasjer ved oppstart:**
- Test serveren manuelt i terminal først
- Sjekk at miljøvariabler er riktige
- Sørg for at alle avhengigheter er installert

---

## 2. VS Code med GitHub Copilot

VS Code støtter MCP gjennom GitHub Copilot Chat-utvidelser.

### Forutsetninger

1. VS Code 1.99+ installert
2. GitHub Copilot-utvidelse installert
3. GitHub Copilot Chat-utvidelse installert

### Konfigurasjon

VS Code bruker `.vscode/mcp.json` i arbeidsområdet eller brukerinnstillinger.

**Arbeidsområdekonfigurasjon** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Brukerinnstillinger** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Bruke MCP i VS Code

1. Åpne Copilot Chat-panelet (Ctrl+Shift+I / Cmd+Shift+I)
2. Skriv `@` for å se tilgjengelige MCP-verktøy
3. Bruk naturlig språk for å bruke verktøy: "Calculate 25 * 48 using the calculator"

### Feilsøking av VS Code

**MCP-servere lastes ikke:**
- Sjekk Utdata-panelet → "MCP" for feil logger
- Last vinduet på nytt: Ctrl+Shift+P → "Developer: Reload Window"
- Verifiser at serveren kjører selvstendig først

---

## 3. Cursor

**Cursor** er en AI-fokusert kodeeditor med innebygd MCP-støtte.

### Installasjon

1. Last ned Cursor fra [cursor.sh](https://cursor.sh)
2. Installer og logg inn

### Konfigurasjon

Cursor bruker et lignende konfigurasjonsformat som Claude Desktop.

**Konfigurasjonsfilplassering:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Eksempel på konfigurasjon:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Bruke MCP i Cursor

1. Åpne Cursors AI-chat (Ctrl+L / Cmd+L)
2. MCP-verktøy vises automatisk i forslagene
3. Be AI-en utføre oppgaver ved hjelp av tilkoblede servere

---

## 4. Cline (terminalbasert)

**Cline** er en terminalbasert MCP-klient, ideell for arbeidsflyt i kommandolinjen.

### Installasjon

```bash
npm install -g @anthropic/cline
```

### Konfigurasjon

Cline bruker miljøvariabler og kommandolinjeargumenter.

**Bruke miljøvariabler:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Bruke kommandolinjeargumenter:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfigurasjonsfil** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Bruke Cline

```bash
# Start en interaktiv økt
cline

# Enkeltforespørsel med MCP
cline "Calculate the square root of 144 using the calculator"

# List tilgjengelige verktøy
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** er en annen AI-drevet kodeeditor med MCP-støtte.

### Installasjon

1. Last ned Windsurf fra [codeium.com/windsurf](https://codeium.com/windsurf)
2. Installer og opprett en konto

### Konfigurasjon

Windsurf-konfigurasjon håndteres gjennom innstillingsgrensesnittet:

1. Åpne Innstillinger (Ctrl+, / Cmd+,)
2. Søk etter "MCP"
3. Klikk "Rediger i settings.json"

**Eksempel på konfigurasjon:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Sammenligning av transporttyper

Ulike verter støtter forskjellige transportmekanismer:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard input/output): Best for lokale servere startet av hosten
**SSE/HTTP**: Best for eksterne servere eller servere delt mellom flere klienter

---

## Vanlige feilsøkingsproblemer

### Serveren starter ikke

1. **Test serveren manuelt først:**
   ```bash
   # For Python
   python -m your_server_module
   
   # For Node.js
   node /path/to/server/index.js
   ```

2. **Sjekk kommando-banen:**
   - Bruk absolutte baner når mulig
   - Sørg for at kjørbar fil er i PATH

3. **Verifiser avhengigheter:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server kobler til men verktøy fungerer ikke

1. **Sjekk serverlogger** - De fleste verter har loggalternativer
2. **Verifiser verktøyregistrering** - Bruk MCP Inspector for testing
3. **Sjekk tillatelser** - Noen verktøy trenger fil-/nettverkstilgang

### Miljøvariabler blir ikke videreført

- Noen verter rensker miljøvariabler
- Bruk `env`-konfigurasjonsfeltet eksplisitt
- Unngå sensitiv data i konfigurasjonsfiler (bruk hemmelighetshåndtering)

---

## Sikkerhetsanbefalinger

1. **Ikke legg API-nøkler i konfigurasjonsfiler**
2. **Bruk miljøvariabler** for sensitiv data
3. **Begrens servertillatelser** til bare det som trengs
4. **Gå gjennom serverkoden** før du gir tilgang til systemet ditt
5. **Bruk tillatlister** for filsystem- og nettverkstilgang

---

## Hva nå

- [3.13 - Feilsøking med MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Lag din første MCP-server](../01-first-server/README.md)
- [Modul 5 - Avanserte emner](../../05-AdvancedTopics/README.md)

---

## Ytterligere ressurser

- [Claude Desktop MCP-dokumentasjon](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP-utvidelse](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Spesifikasjon - Transporter](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Offisiell MCP-serverregister](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->