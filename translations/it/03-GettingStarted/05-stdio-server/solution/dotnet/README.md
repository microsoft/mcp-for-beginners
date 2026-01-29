# MCP stdio Server - Soluzione .NET

> **⚠️ Importante**: Questa soluzione è stata aggiornata per utilizzare il **trasporto stdio** come raccomandato dalla Specifica MCP 2025-06-18. Il trasporto SSE originale è stato deprecato.

## Panoramica

Questa soluzione .NET dimostra come costruire un server MCP utilizzando il trasporto stdio attuale. Il trasporto stdio è più semplice, più sicuro e offre prestazioni migliori rispetto all'approccio SSE deprecato.

## Prerequisiti

- SDK .NET 9.0 o successivo
- Comprensione di base dell'iniezione delle dipendenze in .NET

## Istruzioni di configurazione

### Passaggio 1: Ripristina le dipendenze

```bash
dotnet restore
```

### Passaggio 2: Compila il progetto

```bash
dotnet build
```

## Esecuzione del Server

Il server stdio funziona in modo diverso rispetto al vecchio server basato su HTTP. Invece di avviare un server web, comunica tramite stdin/stdout:

```bash
dotnet run
```

**Importante**: Il server sembrerà bloccarsi - è normale! Sta aspettando messaggi JSON-RPC da stdin.

## Test del Server

### Metodo 1: Utilizzo dell'MCP Inspector (Consigliato)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Questo farà:
1. Avviare il server come sottoprocesso
2. Aprire un'interfaccia web per il test
3. Consentire di testare tutti gli strumenti del server in modo interattivo

### Metodo 2: Test diretto da linea di comando

Puoi anche testare avviando direttamente l'Inspector:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Strumenti Disponibili

Il server fornisce questi strumenti:

- **AddNumbers(a, b)**: Somma due numeri
- **MultiplyNumbers(a, b)**: Moltiplica due numeri  
- **GetGreeting(name)**: Genera un saluto personalizzato
- **GetServerInfo()**: Ottieni informazioni sul server

### Test con Claude Desktop

Per utilizzare questo server con Claude Desktop, aggiungi questa configurazione al tuo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Struttura del Progetto

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Differenze Chiave rispetto a HTTP/SSE

**Trasporto stdio (Attuale):**
- ✅ Configurazione più semplice - non è necessario un server web
- ✅ Maggiore sicurezza - nessun endpoint HTTP
- ✅ Utilizza `Host.CreateApplicationBuilder()` invece di `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` invece di `WithHttpTransport()`
- ✅ Applicazione console invece di applicazione web
- ✅ Prestazioni migliori

**Trasporto HTTP/SSE (Deprecato):**
- ❌ Richiedeva un server web ASP.NET Core
- ❌ Necessitava della configurazione del routing `app.MapMcp()`
- ❌ Configurazione e dipendenze più complesse
- ❌ Considerazioni aggiuntive sulla sicurezza
- ❌ Ora deprecato nella MCP 2025-06-18

## Funzionalità di Sviluppo

- **Iniezione delle Dipendenze**: Supporto completo DI per servizi e logging
- **Logging Strutturato**: Logging corretto su stderr utilizzando `ILogger<T>`
- **Attributi degli Strumenti**: Definizione pulita degli strumenti utilizzando attributi `[McpServerTool]`
- **Supporto Async**: Tutti gli strumenti supportano operazioni asincrone
- **Gestione degli Errori**: Gestione degli errori e logging in modo elegante

## Consigli per lo Sviluppo

- Utilizza `ILogger` per il logging (non scrivere mai direttamente su stdout)
- Compila con `dotnet build` prima di testare
- Testa con l'Inspector per il debug visivo
- Tutti i log vengono automaticamente indirizzati a stderr
- Il server gestisce i segnali di spegnimento in modo elegante

Questa soluzione segue la specifica MCP attuale e dimostra le migliori pratiche per l'implementazione del trasporto stdio utilizzando .NET.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.