# Configurare Client Host MCP Popolari

> [!NOTE]
> Le configurazioni host che puntano a `/sse` sono esempi legacy HTTP+SSE per
> MCP `2025-11-25`. Per MCP `2026-07-28`, selezionare Streamable HTTP negli host che
> lo supportano e utilizzare l'endpoint configurato dal server.

Questa guida spiega come configurare e utilizzare server MCP con popolari applicazioni host AI. Ogni host ha il proprio approccio di configurazione, ma una volta impostato, tutti comunicano con i server MCP usando il protocollo standardizzato.

## Cos'è un Host MCP?

Un **Host MCP** è un'applicazione AI che può connettersi a server MCP per estendere le sue capacità. Pensalo come il "front end" con cui gli utenti interagiscono, mentre i server MCP forniscono gli strumenti e i dati del "back end".

```mermaid
flowchart LR
    User[👤 Utente] --> Host[🖥️ Host MCP]
    Host --> S1[Server MCP A]
    Host --> S2[Server MCP B]
    Host --> S3[Server MCP C]
    
    subgraph "Host Popolari"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Prerequisiti

- Un server MCP a cui connettersi (vedi [Modulo 3.1 - Primo Server](../01-first-server/README.md))
- L'applicazione host installata sul tuo sistema
- Familiarità di base con i file di configurazione JSON

---

## 1. Claude Desktop

**Claude Desktop** è l'applicazione desktop ufficiale di Anthropic che supporta nativamente MCP.

### Installazione

1. Scarica Claude Desktop da [claude.ai/download](https://claude.ai/download)
2. Installa e accedi con il tuo account Anthropic

### Configurazione

Claude Desktop usa un file di configurazione JSON per definire i server MCP.

**Posizione del file di configurazione:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Esempio di configurazione:**

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

### Opzioni di Configurazione

| Campo | Descrizione | Esempio |
|-------|-------------|---------|
| `command` | L'eseguibile da avviare | `"python"`, `"node"`, `"npx"` |
| `args` | Argomenti da linea di comando | `["-m", "my_server"]` |
| `env` | Variabili d'ambiente | `{"API_KEY": "xxx"}` |
| `cwd` | Cartella di lavoro | `"/path/to/server"` |

### Testare la Configurazione

1. Salva il file di configurazione
2. Riavvia completamente Claude Desktop (esci e riapri)
3. Apri una nuova conversazione
4. Cerca l'icona 🔌 che indica i server connessi
5. Prova a chiedere a Claude di usare uno dei tuoi strumenti

### Risoluzione dei Problemi in Claude Desktop

**Server non appare:**
- Verifica la sintassi del file di configurazione con un validatore JSON
- Assicurati che il percorso del comando sia corretto
- Controlla i log di Claude Desktop: Aiuto → Mostra Log

**Il server si blocca all'avvio:**
- Testa manualmente il server nel terminale prima
- Controlla che le variabili d'ambiente siano impostate correttamente
- Assicurati che tutte le dipendenze siano installate

---

## 2. VS Code con GitHub Copilot

VS Code supporta MCP tramite le estensioni GitHub Copilot Chat.

### Prerequisiti

1. VS Code 1.99+ installato
2. Estensione GitHub Copilot installata
3. Estensione GitHub Copilot Chat installata

### Configurazione

VS Code usa `.vscode/mcp.json` nella tua area di lavoro o nelle impostazioni utente.

**Configurazione area di lavoro** (`.vscode/mcp.json`):

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

**Impostazioni utente** (`settings.json`):

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

### Usare MCP in VS Code

1. Apri il pannello Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Digita `@` per vedere gli strumenti MCP disponibili
3. Usa un linguaggio naturale per invocare strumenti: "Calcola 25 * 48 usando la calcolatrice"

### Risoluzione dei Problemi in VS Code

**I server MCP non si caricano:**
- Controlla il pannello Output → "MCP" per i log di errore
- Ricarica la finestra: Ctrl+Shift+P → "Developer: Reload Window"
- Verifica che il server funzioni in modo standalone prima

---

## 3. Cursor

**Cursor** è un editor di codice AI-first con supporto MCP integrato.

### Installazione

1. Scarica Cursor da [cursor.sh](https://cursor.sh)
2. Installa e accedi

### Configurazione

Cursor usa un formato di configurazione simile a Claude Desktop.

**Posizione del file di configurazione:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Esempio di configurazione:**

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

### Usare MCP in Cursor

1. Apri la chat AI di Cursor (Ctrl+L / Cmd+L)
2. Gli strumenti MCP appaiono automaticamente nei suggerimenti
3. Chiedi all'AI di eseguire compiti usando i server connessi

---

## 4. Cline (Basato su Terminale)

**Cline** è un client MCP basato su terminale, ideale per flussi di lavoro da linea di comando.

### Installazione

```bash
npm install -g @anthropic/cline
```

### Configurazione

Cline usa variabili d'ambiente e argomenti da linea di comando.

**Uso di variabili d'ambiente:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Uso di argomenti da linea di comando:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**File di configurazione** (`~/.clinerc`):

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

### Usare Cline

```bash
# Avviare una sessione interattiva
cline

# Singola query con MCP
cline "Calculate the square root of 144 using the calculator"

# Elenca gli strumenti disponibili
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** è un altro editor di codice potenziato da AI con supporto MCP.

### Installazione

1. Scarica Windsurf da [codeium.com/windsurf](https://codeium.com/windsurf)
2. Installa e crea un account

### Configurazione

La configurazione di Windsurf è gestita tramite l'interfaccia impostazioni:

1. Apri Impostazioni (Ctrl+, / Cmd+,)
2. Cerca "MCP"
3. Clicca su "Modifica in settings.json"

**Esempio di configurazione:**

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

## Confronto Tipi di Trasporto

Diversi host supportano differenti meccanismi di trasporto:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (input/output standard): Migliore per server locali avviati dall'host
**SSE/HTTP**: Migliore per server remoti o server condivisi tra più client

---

## Risoluzione Problemi Comuni

### Il server non si avvia

1. **Testa prima manualmente il server:**
   ```bash
   # Per Python
   python -m your_server_module
   
   # Per Node.js
   node /path/to/server/index.js
   ```

2. **Controlla il percorso del comando:**
   - Usa percorsi assoluti quando possibile
   - Assicurati che l'eseguibile sia nel tuo PATH

3. **Verifica le dipendenze:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Il server si connette ma gli strumenti non funzionano

1. **Controlla i log del server** - La maggior parte degli host ha opzioni di log
2. **Verifica la registrazione degli strumenti** - Usa MCP Inspector per testare
3. **Controlla i permessi** - Alcuni strumenti necessitano accesso a file/rete

### Variabili d'ambiente non passate

- Alcuni host filtrano le variabili d'ambiente
- Usa esplicitamente il campo di configurazione `env`
- Evita dati sensibili nei file di configurazione (usa la gestione segreti)

---

## Best Practice per la Sicurezza

1. **Non commettere mai API key** nei file di configurazione
2. **Usa variabili d'ambiente** per dati sensibili
3. **Limita i permessi del server** solo a quelli necessari
4. **Revisione del codice del server** prima di concedere accesso al sistema
5. **Usa allowlist** per accesso a file system e rete

---

## Cosa Fare Dopo

- [3.13 - Debug con MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Crea il tuo primo server MCP](../01-first-server/README.md)
- [Modulo 5 - Argomenti Avanzati](../../05-AdvancedTopics/README.md)

---

## Risorse Supplementari

- [Documentazione MCP Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Estensione MCP VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Specifiche MCP - Trasporti](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Registro Ufficiale Server MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->