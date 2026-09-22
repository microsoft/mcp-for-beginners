# Radici MCP (Funzionalità Legacy)

> [!WARNING]
> Le radici sono deprecate a partire da MCP `2026-07-28`. Rimangono in questa revisione per
> compatibilità e sono idonee per la rimozione nella prima revisione della specifica
> rilasciata il o dopo il 28 luglio 2027. Le nuove implementazioni dovrebbero passare
> directory o file tramite parametri degli strumenti, URI di risorse o configurazione
> del server.

## Panoramica

Le radici permettono a un client MCP di indicare a un server quali posizioni del filesystem sono rilevanti
per la richiesta corrente. Una radice contiene un URI `file://` richiesto e un nome
leggibile opzionale.

Le radici sono suggerimenti informativi. Non sono contenitori per la cronologia delle conversazioni,
sessioni di protocollo o un meccanismo di controllo di accesso. Il protocollo non
impone che un server rimanga entro le radici elencate.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Spiegare cosa rappresentano le Radici MCP e cosa non rappresentano.
- Riconoscere il flusso multiplo `roots/list` attuale.
- Applicare controlli di sicurezza indipendentemente dalle Radici.
- Migrare nuove implementazioni a alternative supportate.

## Dati delle Radici

Un client restituisce ogni radice come un URI `file://` con un nome di visualizzazione opzionale:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

I client dovrebbero esporre solo le posizioni approvate dall’utente. I server dovrebbero trattare
il risultato come una guida sui file rilevanti, non come prova di autorizzazione.

## Flusso MCP 2026-07-28

Un client che supporta le Radici dichiara questa capacità in ogni richiesta:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Durante l’elaborazione di una richiesta client, un server può restituire un
`InputRequiredResult` contenente una richiesta di input `roots/list`:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Il client raccoglie le radici approvate e riprova la richiesta originale con le
`inputResponses` corrispondenti e lo stesso `requestState`. Questo schema multi-giro
mantiene il protocollo senza stato; non esiste un handshake `initialize` o
una sessione a livello di protocollo.

## Comportamento Legacy 2025-11-25

In MCP `2025-11-25`, i client pubblicizzavano le Radici durante l’inizializzazione. Un server
poteva inviare una richiesta diretta `roots/list`, e un client poteva inviare
`notifications/roots/list_changed` quando le sue radici cambiavano.

Quel ciclo di vita è un comportamento legacy. Non combinare i suoi esempi di inizializzazione o
notifica con un’implementazione `2026-07-28`.

## Sostituzioni Consigliate

### Parametri dello Strumento

Rendi esplicita la directory o il file richiesto nello schema dello strumento:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URI delle Risorse

Usa le Risorse MCP quando il server può esporre i file rilevanti tramite URI stabili.
Questo mantiene esplicita la scoperta e il recupero.

### Configurazione del Server

Per distribuzioni fisse, configura le directory consentite all’avvio del server.
Questo è spesso più chiaro che scoprirle durante una chiamata dello strumento.

## Requisiti di Sicurezza

Qualunque sostituzione tu scelga:

- Ottieni il consenso dell’utente prima di esporre posizioni del filesystem.
- Canonicalizza e convalida i percorsi per prevenire traversal.
- Applica l’autorizzazione e il sandboxing indipendentemente dai valori delle radici.
- Ricontrolla i permessi quando un file è accesso, non solo quando viene elencato.
- Evita di restituire percorsi sensibili nei log o messaggi di errore.

## Punti Chiave

- Le radici descrivono posizioni rilevanti nel filesystem; non memorizzano lo
  stato della conversazione.
- Le radici sono una guida, non un confine di controllo di accesso.
- MCP `2026-07-28` porta la capacità per richiesta e usa
  `InputRequiredResult` per `roots/list`.
- Le nuove implementazioni dovrebbero usare parametri dello strumento, URI di risorse, o
  configurazione del server invece.

## Risorse Aggiuntive

- [Radici in MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Registro delle funzionalità deprecate](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Cosa è cambiato in MCP: La specifica 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->