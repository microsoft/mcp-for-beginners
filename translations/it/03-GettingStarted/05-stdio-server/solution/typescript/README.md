# Server MCP stdio - Soluzione TypeScript

> **⚠️ Importante**: Questa soluzione è stata aggiornata per utilizzare il **trasporto stdio** come raccomandato dalla Specifica MCP 2025-06-18. Il trasporto SSE originale è stato deprecato.

## Panoramica

Questa soluzione in TypeScript dimostra come costruire un server MCP utilizzando il trasporto stdio attuale. Il trasporto stdio è più semplice, più sicuro e offre prestazioni migliori rispetto all'approccio SSE deprecato.

## Prerequisiti

- Node.js 18+ o versioni successive
- Gestore di pacchetti npm o yarn

## Istruzioni per la configurazione

### Passo 1: Installa le dipendenze

```bash
npm install
```

### Passo 2: Compila il progetto

```bash
npm run build
```

## Esecuzione del Server

Il server stdio funziona in modo diverso rispetto al vecchio server SSE. Invece di avviare un server web, comunica tramite stdin/stdout:

```bash
npm start
```

**Importante**: Il server sembrerà bloccarsi - è normale! Sta aspettando messaggi JSON-RPC da stdin.

## Test del Server

### Metodo 1: Utilizzo del MCP Inspector (Consigliato)

```bash
npm run inspector
```

Questo farà:
1. Avviare il server come sottoprocesso
2. Aprire un'interfaccia web per i test
3. Consentire di testare tutti gli strumenti del server in modo interattivo

### Metodo 2: Test diretto da riga di comando

Puoi anche testare avviando direttamente l'Inspector:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Strumenti Disponibili

Il server fornisce questi strumenti:

- **add(a, b)**: Somma due numeri
- **multiply(a, b)**: Moltiplica due numeri  
- **get_greeting(name)**: Genera un saluto personalizzato
- **get_server_info()**: Ottieni informazioni sul server

### Test con Claude Desktop

Per utilizzare questo server con Claude Desktop, aggiungi questa configurazione al tuo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Struttura del Progetto

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Differenze Chiave rispetto a SSE

**Trasporto stdio (Attuale):**
- ✅ Configurazione più semplice - non è necessario un server HTTP
- ✅ Maggiore sicurezza - nessun endpoint HTTP
- ✅ Comunicazione basata su sottoprocessi
- ✅ JSON-RPC tramite stdin/stdout
- ✅ Prestazioni migliori

**Trasporto SSE (Deprecato):**
- ❌ Richiedeva la configurazione di un server Express
- ❌ Necessitava di routing complesso e gestione delle sessioni
- ❌ Più dipendenze (Express, gestione HTTP)
- ❌ Ulteriori considerazioni sulla sicurezza
- ❌ Ora deprecato nella MCP 2025-06-18

## Consigli per lo Sviluppo

- Usa `console.error()` per il logging (mai `console.log()` poiché scrive su stdout)
- Compila con `npm run build` prima di testare
- Testa con l'Inspector per il debug visivo
- Assicurati che tutti i messaggi JSON siano formattati correttamente
- Il server gestisce automaticamente lo spegnimento graduale su SIGINT/SIGTERM

Questa soluzione segue la specifica MCP attuale e dimostra le migliori pratiche per l'implementazione del trasporto stdio utilizzando TypeScript.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.