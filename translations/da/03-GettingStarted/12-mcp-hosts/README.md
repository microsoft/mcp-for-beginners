# Opsætning af populære MCP Host-klienter

> [!NOTE]
> Host-konfigurationer, der peger på `/sse`, er ældre HTTP+SSE-eksempler for
> MCP `2025-11-25`. For MCP `2026-07-28` skal du vælge Streamable HTTP i værter, der
> understøtter det og bruge den endpoint, som serveren har konfigureret.

Denne vejledning dækker, hvordan man konfigurerer og bruger MCP-servere med populære AI host-programmer. Hver host har sin egen konfigurationsmetode, men når de først er sat op, kommunikerer de alle med MCP-servere ved hjælp af den standardiserede protokol.

## Hvad er en MCP Host?

En **MCP Host** er en AI-applikation, der kan oprette forbindelse til MCP-servere for at udvide sine funktioner. Tænk på det som "frontenden", som brugerne interagerer med, mens MCP-servere leverer "backend"-værktøjer og data.

```mermaid
flowchart LR
    User[👤 Bruger] --> Host[🖥️ MCP Værtsmaskine]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Populære værter"
        H1[Claude Skrivebord]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Forudsætninger

- En MCP-server at forbinde til (se [Module 3.1 - First Server](../01-first-server/README.md))
- Host-applikationen installeret på dit system
- Grundlæggende kendskab til JSON-konfigurationsfiler

---

## 1. Claude Desktop

**Claude Desktop** er Anthropics officielle skrivebordapplikation, der understøtter MCP nativt.

### Installation

1. Download Claude Desktop fra [claude.ai/download](https://claude.ai/download)
2. Installer og log ind med din Anthropic-konto

### Konfiguration

Claude Desktop bruger en JSON-konfigurationsfil til at definere MCP-servere.

**Placering af konfigurationsfil:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Eksempel på konfiguration:**

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

### Konfigurationsmuligheder

| Felt | Beskrivelse | Eksempel |
|-------|-------------|---------|
| `command` | Det eksekverbare program der skal køres | `"python"`, `"node"`, `"npx"` |
| `args` | Kommandolinjens argumenter | `["-m", "my_server"]` |
| `env` | Miljøvariabler | `{"API_KEY": "xxx"}` |
| `cwd` | Arbejdsmappe | `"/path/to/server"` |

### Test af din opsætning

1. Gem konfigurationsfilen
2. Genstart Claude Desktop helt (luk og åbn igen)
3. Åbn en ny samtale
4. Kig efter ikonet 🔌, der indikerer tilsluttede servere
5. Prøv at bede Claude bruge et af dine værktøjer

### Fejlfinding af Claude Desktop

**Server vises ikke:**
- Tjek syntaks i konfigurationsfilen med en JSON-validator
- Sørg for, at kommandoens sti er korrekt
- Tjek Claude Desktop logs: Hjælp → Vis logfiler

**Server crasher ved opstart:**
- Test din server manuelt i terminalen først
- Tjek at miljøvariabler er korrekt sat
- Sørg for at alle afhængigheder er installeret

---

## 2. VS Code med GitHub Copilot

VS Code understøtter MCP via GitHub Copilot Chat-udvidelser.

### Forudsætninger

1. VS Code 1.99+ installeret
2. GitHub Copilot-udvidelsen installeret
3. GitHub Copilot Chat-udvidelsen installeret

### Konfiguration

VS Code bruger `.vscode/mcp.json` i dit workspace eller brugerindstillinger.

**Workspace-konfiguration** (`.vscode/mcp.json`):

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

**Brugerindstillinger** (`settings.json`):

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

### Brug af MCP i VS Code

1. Åbn Copilot Chat-panelet (Ctrl+Shift+I / Cmd+Shift+I)
2. Skriv `@` for at se tilgængelige MCP-værktøjer
3. Brug naturligt sprog til at aktivere værktøjer: "Beregn 25 * 48 med lommeregneren"

### Fejlfinding i VS Code

**MCP-servere indlæses ikke:**
- Tjek Output-panelet → "MCP" for fejlmeddelelser
- Genindlæs vinduet: Ctrl+Shift+P → "Udvikler: Genindlæs vindue"
- Bekræft at serveren kører standalone først

---

## 3. Cursor

**Cursor** er en AI-først kodeeditor med indbygget MCP-understøttelse.

### Installation

1. Download Cursor fra [cursor.sh](https://cursor.sh)
2. Installer og log ind

### Konfiguration

Cursor bruger et lignende konfigurationsformat som Claude Desktop.

**Placering af konfigurationsfil:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Eksempel på konfiguration:**

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

### Brug af MCP i Cursor

1. Åbn Cursors AI-chat (Ctrl+L / Cmd+L)
2. MCP-værktøjer vises automatisk i forslagene
3. Bed AI'en om at udføre opgaver med tilsluttede servere

---

## 4. Cline (Terminal-baseret)

**Cline** er en terminal-baseret MCP-klient, ideel til arbejdsflow i kommandolinjen.

### Installation

```bash
npm install -g @anthropic/cline
```

### Konfiguration

Cline bruger miljøvariabler og kommandolinjeargumenter.

**Brug af miljøvariabler:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Brug af kommandolinjeargumenter:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfigurationsfil** (`~/.clinerc`):

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

### Brug af Cline

```bash
# Start en interaktiv session
cline

# Enkelt forespørgsel med MCP
cline "Calculate the square root of 144 using the calculator"

# Liste over tilgængelige værktøjer
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** er en anden AI-drevet kodeeditor med MCP-understøttelse.

### Installation

1. Download Windsurf fra [codeium.com/windsurf](https://codeium.com/windsurf)
2. Installer og opret en konto

### Konfiguration

Windsurfs konfiguration styres via indstillingsbrugerfladen:

1. Åbn Indstillinger (Ctrl+, / Cmd+,)
2. Søg efter "MCP"
3. Klik på "Rediger i settings.json"

**Eksempel på konfiguration:**

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

## Sammenligning af transporttyper

Forskellige hosts understøtter forskellige transportmekanismer:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard input/output): Bedst til lokale servere startet af hosten
**SSE/HTTP**: Bedst til fjernservere eller servere delt mellem flere klienter

---

## Almindelig fejlfinding

### Serveren vil ikke starte

1. **Test serveren manuelt først:**
   ```bash
   # Til Python
   python -m your_server_module
   
   # Til Node.js
   node /path/to/server/index.js
   ```

2. **Tjek kommandoens sti:**
   - Brug absolutte stier når det er muligt
   - Sørg for at det eksekverbare program er i din PATH

3. **Bekræft afhængigheder:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server opretter forbindelse, men værktøjer virker ikke

1. **Tjek serverlogs** - De fleste hosts har logningsmuligheder
2. **Bekræft værktøjsregistrering** - Brug MCP Inspector til at teste
3. **Tjek tilladelser** - Nogle værktøjer kræver fil-/netværksadgang

### Miljøvariabler overføres ikke

- Nogle hosts renser miljøvariabler
- Brug `env` konfigurationsfeltet eksplicit
- Undgå følsomme data i konfigurationsfiler (brug hemmelighedsstyring)

---

## Sikkerhedspraksis

1. **Aldrig commit API-nøgler** i konfigurationsfiler
2. **Brug miljøvariabler** til følsomme data
3. **Begræns servertilladelser** til kun det nødvendige
4. **Gennemgå serverkode** før du giver systemadgang
5. **Brug tilladelseslister** for filsystem- og netværksadgang

---

## Hvad er det næste

- [3.13 - Debugging med MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Opret din første MCP-server](../01-first-server/README.md)
- [Module 5 - Avancerede emner](../../05-AdvancedTopics/README.md)

---

## Yderligere ressourcer

- [Claude Desktop MCP Dokumentation](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Udvidelse](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Specifikation - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Officiel MCP Server Registry](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->