# Example: Basic Host

Una implementazione di riferimento che mostra come costruire un'applicazione host MCP che si connette ai server MCP e rende le interfacce utente degli strumenti in un sandbox sicuro.

Questo host di base può anche essere usato per testare le App MCP durante lo sviluppo locale.

## Key Files

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Host UI React con selezione degli strumenti, input dei parametri e gestione degli iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy dell'iframe esterno con validazione di sicurezza e rimbalzo dei messaggi bidirezionale
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Logica principale: connessione al server, chiamata degli strumenti e configurazione di AppBridge

## Getting Started

```bash
npm install
npm run start
# Apri http://localhost:8080
```

Per impostazione predefinita, l'applicazione host cercherà di connettersi a un server MCP su `http://localhost:3001/mcp`. Puoi configurare questo comportamento impostando la variabile d'ambiente `SERVERS` con un array JSON di URL di server:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architecture

Questo esempio utilizza un modello sandbox a doppio iframe per un'isolamento sicuro dell'interfaccia utente:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Perché due iframe?**

- L'iframe esterno gira su un'origine separata (porta 8081) impedendo l'accesso diretto all'host
- L'iframe interno riceve HTML tramite `srcdoc` ed è limitato dagli attributi sandbox
- I messaggi fluiscono attraverso l'iframe esterno che li valida e li trasmette bidirezionalmente

Questa architettura garantisce che anche se il codice UI dello strumento fosse dannoso, non potrebbe accedere al DOM dell'applicazione host, ai cookie o al contesto JavaScript.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avvertenza**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non ci assumiamo alcuna responsabilità per fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->