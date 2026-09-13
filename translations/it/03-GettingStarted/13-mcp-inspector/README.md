# Debugging con MCP Inspector

> [!NOTE]
> I comandi che usano `--sse` e gli URL che finiscono con `/sse` testano il trasporto legacy HTTP+SSE.
> Per un server MCP `2026-07-28` nuovo, usa una versione di Inspector che
> supporta HTTP Streamable e seleziona invece quel trasporto.

Il **MCP Inspector** è uno strumento essenziale per il debugging che ti permette di testare e risolvere interattivamente i tuoi server MCP senza aver bisogno di un'applicazione host AI completa. Pensalo come un "Postman per MCP" - fornisce un'interfaccia visiva per inviare richieste, visualizzare risposte e comprendere come si comporta il tuo server.

## Perché usare MCP Inspector?

Nel costruire server MCP, spesso ti trovi ad affrontare queste sfide:

- **"Il mio server è in esecuzione?"** - Inspector mostra lo stato della connessione
- **"I miei strumenti sono registrati correttamente?"** - Inspector elenca tutti gli strumenti disponibili
- **"Qual è il formato della risposta?"** - Inspector mostra risposte JSON complete
- **"Perché questo strumento non funziona?"** - Inspector mostra messaggi di errore dettagliati

## Prerequisiti

- Node.js 18+ installato
- npm (incluso con Node.js)
- Un server MCP da testare (vedi [Modulo 3.1 - Primo Server](../01-first-server/README.md))

## Installazione

### Opzione 1: Esegui con npx (Raccomandato per test rapidi)

```bash
npx @modelcontextprotocol/inspector
```

### Opzione 2: Installa globalmente

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Opzione 3: Aggiungi al tuo progetto

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Aggiungi a `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Connettersi al tuo server

### Server stdio (processo locale)

Per server che comunicano tramite input/output standard:

```bash
# Server Python
npx @modelcontextprotocol/inspector python -m your_server_module

# Server Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# Con variabili d'ambiente
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### Server SSE/HTTP (rete)

Per server che girano come servizi HTTP:

1. Avvia prima il tuo server:
   ```bash
   python server.py  # Server in esecuzione su http://localhost:8080
   ```

2. Avvia Inspector e connettiti:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Panoramica dell'interfaccia Inspector

Quando Inspector si avvia, vedrai un'interfaccia web (tipicamente su `http://localhost:5173`):

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

## Test degli strumenti

### Elenco degli strumenti disponibili

1. Clicca sulla scheda **Strumenti**
2. Inspector chiama automaticamente `tools/list`
3. Vedrai tutti gli strumenti registrati con:
   - Nome dello strumento
   - Descrizione
   - Schema d'ingresso (parametri)

### Invocare uno strumento

1. Seleziona uno strumento dalla lista
2. Compila i parametri richiesti nel modulo
3. Clicca su **Esegui strumento**
4. Visualizza la risposta nel pannello dei risultati

**Esempio: test di uno strumento calcolatrice**

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

### Debug degli errori degli strumenti

Quando uno strumento fallisce, Inspector mostra:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Codici di errore comuni:
| Codice | Significato |
|--------|------------|
| -32700 | Errore di parsing (JSON non valido) |
| -32600 | Richiesta non valida |
| -32601 | Metodo non trovato |
| -32602 | Parametri non validi |
| -32603 | Errore interno |

---

## Test delle risorse

### Elenco delle risorse

1. Clicca sulla scheda **Risorse**
2. Inspector chiama `resources/list`
3. Vedrai:
   - URI delle risorse
   - Nomi e descrizioni
   - Tipi MIME

### Lettura di una risorsa

1. Seleziona una risorsa
2. Clicca su **Leggi risorsa**
3. Visualizza il contenuto restituito

**Esempio di output:**

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

## Test dei prompt

### Elenco dei prompt

1. Clicca sulla scheda **Prompt**
2. Inspector chiama `prompts/list`
3. Visualizza i modelli di prompt disponibili

### Ottenere un prompt

1. Seleziona un prompt
2. Compila eventuali argomenti richiesti
3. Clicca su **Ottieni prompt**
4. Visualizza i messaggi prompt renderizzati

---

## Analisi del log dei messaggi

Il log dei messaggi mostra tutti i messaggi del protocollo MCP. La trascrizione qui sotto è da un
server legacy `2025-11-25` e include la stretta di mano `initialize` rimossa. Un
server `2026-07-28` usa metadata della richiesta autonomi e `server/discover`
al loro posto.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Cosa osservare

- **Coppie richiesta/risposta**: Ogni `→` dovrebbe avere un corrispondente `←`
- **Messaggi di errore**: Cerca `"error"` nelle risposte
- **Tempi**: Lunghi intervalli possono indicare problemi di performance
- **Versione del protocollo**: Assicurati che server e client usino la stessa versione

---

## Integrazione con VS Code

Puoi eseguire Inspector direttamente da VS Code:

### Usando launch.json

Aggiungi a `.vscode/launch.json`:

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

### Usando Tasks

Aggiungi a `.vscode/tasks.json`:

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

## Scenari comuni di debugging

### Scenario 1: Il server non si connette

**Sintomi:** Inspector mostra "Disconnected" o rimane bloccato su "Connecting..."

**Lista di controllo:**
1. ✅ Il comando del server è corretto?
2. ✅ Sono installate tutte le dipendenze?
3. ✅ Il percorso del server è assoluto o relativo alla directory corrente?
4. ✅ Sono impostate le variabili d'ambiente necessarie?

**Passi per il debug:**
```bash
# Testa manualmente prima il server
python -c "import your_server_module; print('OK')"

# Controlla errori di importazione
python -m your_server_module 2>&1 | head -20

# Verifica che MCP SDK sia installato
pip show mcp
```

### Scenario 2: Gli strumenti non appaiono

**Sintomi:** La scheda strumenti mostra una lista vuota

**Cause possibili:**
1. Strumenti non registrati durante l'inizializzazione del server
2. Crash del server dopo l'avvio
3. L'handler di `tools/list` restituisce un array vuoto

**Passi per il debug:**
1. Controlla il log dei messaggi per la risposta di `tools/list`
2. Aggiungi logging al codice di registrazione degli strumenti
3. Verifica che i decoratori `@mcp.tool()` siano presenti (Python)

### Scenario 3: Lo strumento restituisce errore

**Sintomi:** La chiamata allo strumento restituisce una risposta di errore

**Approccio di debug:**
1. Leggi con attenzione il messaggio di errore
2. Controlla che i tipi dei parametri corrispondano allo schema
3. Aggiungi try/catch con messaggi di errore dettagliati
4. Controlla i log del server per stack trace

**Esempio di gestione errori migliorata:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Logica dello strumento qui
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenario 4: Contenuto risorsa vuoto

**Sintomi:** La risorsa restituisce ma il contenuto è vuoto o nullo

**Lista di controllo:**
1. ✅ Il percorso del file o URI è corretto
2. ✅ Il server ha i permessi per leggere la risorsa
3. ✅ Il contenuto della risorsa viene restituito correttamente

---

## Funzionalità avanzate di Inspector

### Header personalizzati (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Logging dettagliato

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Registrazione delle sessioni

Inspector può esportare i log dei messaggi per analisi successive:
1. Clicca su **Esporta log** nel pannello dei messaggi
2. Salva il file JSON
3. Condividi con i membri del team per il debugging

---

## Buone pratiche

1. **Testa presto e spesso** - Usa Inspector durante lo sviluppo, non solo quando qualcosa si rompe
2. **Inizia semplice** - Testa la connettività base prima di chiamate complesse
3. **Controlla lo schema** - Molti errori derivano da discrepanze nei tipi dei parametri
4. **Leggi i messaggi di errore** - Gli errori MCP sono di solito descrittivi
5. **Tieni Inspector aperto** - Aiuta a catturare problemi mentre sviluppi

---

## Cosa c'è dopo

Hai completato il Modulo 3: Introduzione! Continua il tuo apprendimento:

- [Modulo 4: Implementazione Pratica](../../04-PracticalImplementation/README.md)

---

## Risorse aggiuntive

- [Repository GitHub MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [Specifiche MCP - Messaggi del protocollo](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Specifiche JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->