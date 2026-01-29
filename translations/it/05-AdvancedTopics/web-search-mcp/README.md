# Lezione: Costruire un Server MCP per la Ricerca Web

Questo capitolo mostra come costruire un agente AI reale che si integra con API esterne, gestisce diversi tipi di dati, gestisce errori e coordina più strumenti—tutto in un formato pronto per la produzione. Vedrai:

- **Integrazione con API esterne che richiedono autenticazione**
- **Gestione di diversi tipi di dati da molteplici endpoint**
- **Strategie robuste di gestione degli errori e logging**
- **Orchestrazione multi-strumento in un unico server**

Alla fine, avrai esperienza pratica con pattern e best practice essenziali per applicazioni avanzate basate su AI e LLM.

## Introduzione

In questa lezione imparerai a costruire un server e un client MCP avanzati che estendono le capacità LLM con dati web in tempo reale usando SerpAPI. Questa è una competenza fondamentale per sviluppare agenti AI dinamici in grado di accedere a informazioni aggiornate dal web.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Integrare API esterne (come SerpAPI) in modo sicuro in un server MCP
- Implementare più strumenti per ricerca web, notizie, prodotti e Q&A
- Analizzare e formattare dati strutturati per il consumo da parte di LLM
- Gestire errori e limiti di chiamata API in modo efficace
- Costruire e testare sia client MCP automatizzati che interattivi

## Server MCP per la Ricerca Web

Questa sezione introduce l’architettura e le funzionalità del Server MCP per la Ricerca Web. Vedrai come FastMCP e SerpAPI vengono usati insieme per estendere le capacità LLM con dati web in tempo reale.

### Panoramica

Questa implementazione include quattro strumenti che mostrano la capacità di MCP di gestire compiti diversi, basati su API esterne, in modo sicuro ed efficiente:

- **general_search**: per risultati web generali
- **news_search**: per le ultime notizie
- **product_search**: per dati e-commerce
- **qna**: per domande e risposte

### Funzionalità
- **Esempi di Codice**: Include blocchi di codice specifici per Python (e facilmente estendibili ad altri linguaggi) usando code pivot per chiarezza

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Prima di eseguire il client, è utile capire cosa fa il server. Il file [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementa il server MCP, esponendo strumenti per ricerca web, notizie, prodotti e Q&A integrandosi con SerpAPI. Gestisce le richieste in arrivo, le chiamate API, analizza le risposte e restituisce risultati strutturati al client.

Puoi consultare l’implementazione completa in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Ecco un breve esempio di come il server definisce e registra uno strumento:

### Server Python

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Integrazione API Esterne**: Dimostra la gestione sicura delle chiavi API e delle richieste esterne
- **Parsing Dati Strutturati**: Mostra come trasformare le risposte API in formati adatti agli LLM
- **Gestione Errori**: Gestione robusta degli errori con logging appropriato
- **Client Interattivo**: Include sia test automatizzati che una modalità interattiva per il testing
- **Gestione del Contesto**: Sfrutta MCP Context per logging e tracciamento delle richieste

## Prerequisiti

Prima di iniziare, assicurati che il tuo ambiente sia configurato correttamente seguendo questi passaggi. Questo garantirà che tutte le dipendenze siano installate e che le chiavi API siano configurate correttamente per uno sviluppo e test senza intoppi.

- Python 3.8 o superiore
- Chiave API SerpAPI (Registrati su [SerpAPI](https://serpapi.com/) - disponibile piano gratuito)

## Installazione

Per iniziare, segui questi passaggi per configurare il tuo ambiente:

1. Installa le dipendenze usando uv (consigliato) o pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Crea un file `.env` nella root del progetto con la tua chiave SerpAPI:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Utilizzo

Il Server MCP per la Ricerca Web è il componente centrale che espone strumenti per ricerca web, notizie, prodotti e Q&A integrandosi con SerpAPI. Gestisce le richieste in arrivo, le chiamate API, analizza le risposte e restituisce risultati strutturati al client.

Puoi consultare l’implementazione completa in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Avvio del Server

Per avviare il server MCP, usa il seguente comando:

```bash
python server.py
```

Il server funzionerà come un server MCP basato su stdio a cui il client può connettersi direttamente.

### Modalità Client

Il client (`client.py`) supporta due modalità per interagire con il server MCP:

- **Modalità Normale**: Esegue test automatizzati che utilizzano tutti gli strumenti e verificano le risposte. Utile per controllare rapidamente che server e strumenti funzionino come previsto.
- **Modalità Interattiva**: Avvia un’interfaccia a menu dove puoi selezionare manualmente gli strumenti, inserire query personalizzate e vedere i risultati in tempo reale. Ideale per esplorare le capacità del server e sperimentare con input diversi.

Puoi consultare l’implementazione completa in [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Esecuzione del Client

Per eseguire i test automatizzati (questo avvierà automaticamente il server):

```bash
python client.py
```

Oppure esegui in modalità interattiva:

```bash
python client.py --interactive
```

### Test con Metodi Diversi

Ci sono diversi modi per testare e interagire con gli strumenti forniti dal server, a seconda delle tue esigenze e del tuo flusso di lavoro.

#### Scrivere Script di Test Personalizzati con MCP Python SDK
Puoi anche creare i tuoi script di test usando MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

In questo contesto, uno "script di test" è un programma Python personalizzato che scrivi per agire come client del server MCP. Invece di essere un test unitario formale, questo script ti permette di connetterti programmaticamente al server, chiamare uno qualsiasi dei suoi strumenti con parametri a tua scelta e ispezionare i risultati. Questo approccio è utile per:
- Prototipare e sperimentare con le chiamate agli strumenti
- Validare come il server risponde a input diversi
- Automatizzare invocazioni ripetute degli strumenti
- Costruire i tuoi flussi di lavoro o integrazioni sopra il server MCP

Puoi usare gli script di test per provare rapidamente nuove query, fare debug del comportamento degli strumenti o anche come punto di partenza per automazioni più avanzate. Di seguito un esempio di come usare MCP Python SDK per creare uno script del genere:

## Descrizione degli Strumenti

Puoi usare i seguenti strumenti forniti dal server per eseguire diversi tipi di ricerche e query. Ogni strumento è descritto con i suoi parametri e un esempio d’uso.

Questa sezione fornisce dettagli su ogni strumento disponibile e i relativi parametri.

### general_search

Esegue una ricerca web generale e restituisce risultati formattati.

**Come chiamare questo strumento:**

Puoi chiamare `general_search` dal tuo script usando MCP Python SDK, o interattivamente tramite l’Inspector o la modalità client interattiva. Ecco un esempio di codice con l’SDK:

# [Esempio Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

In alternativa, in modalità interattiva, seleziona `general_search` dal menu e inserisci la tua query quando richiesto.

**Parametri:**
- `query` (stringa): La query di ricerca

**Esempio di Richiesta:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Cerca articoli di notizie recenti relativi a una query.

**Come chiamare questo strumento:**

Puoi chiamare `news_search` dal tuo script usando MCP Python SDK, o interattivamente tramite l’Inspector o la modalità client interattiva. Ecco un esempio di codice con l’SDK:

# [Esempio Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

In alternativa, in modalità interattiva, seleziona `news_search` dal menu e inserisci la tua query quando richiesto.

**Parametri:**
- `query` (stringa): La query di ricerca

**Esempio di Richiesta:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Cerca prodotti corrispondenti a una query.

**Come chiamare questo strumento:**

Puoi chiamare `product_search` dal tuo script usando MCP Python SDK, o interattivamente tramite l’Inspector o la modalità client interattiva. Ecco un esempio di codice con l’SDK:

# [Esempio Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

In alternativa, in modalità interattiva, seleziona `product_search` dal menu e inserisci la tua query quando richiesto.

**Parametri:**
- `query` (stringa): La query di ricerca prodotti

**Esempio di Richiesta:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Ottiene risposte dirette a domande dai motori di ricerca.

**Come chiamare questo strumento:**

Puoi chiamare `qna` dal tuo script usando MCP Python SDK, o interattivamente tramite l’Inspector o la modalità client interattiva. Ecco un esempio di codice con l’SDK:

# [Esempio Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

In alternativa, in modalità interattiva, seleziona `qna` dal menu e inserisci la tua domanda quando richiesto.

**Parametri:**
- `question` (stringa): La domanda a cui trovare risposta

**Esempio di Richiesta:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Dettagli del Codice

Questa sezione fornisce frammenti di codice e riferimenti per le implementazioni di server e client.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Consulta [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) e [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) per i dettagli completi dell’implementazione.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Concetti Avanzati in Questa Lezione

Prima di iniziare a costruire, ecco alcuni concetti avanzati importanti che appariranno in tutto il capitolo. Comprenderli ti aiuterà a seguire meglio, anche se sono nuovi per te:

- **Orchestrazione Multi-strumento**: significa eseguire diversi strumenti (come ricerca web, notizie, prodotti e Q&A) all’interno di un unico server MCP. Permette al server di gestire una varietà di compiti, non solo uno.
- **Gestione dei Limiti di Chiamata API**: molte API esterne (come SerpAPI) limitano quante richieste puoi fare in un certo tempo. Un buon codice verifica questi limiti e li gestisce con eleganza, così l’app non si blocca se superi un limite.
- **Parsing di Dati Strutturati**: le risposte API sono spesso complesse e annidate. Questo concetto riguarda la trasformazione di quelle risposte in formati puliti e facili da usare, adatti a LLM o altri programmi.
- **Recupero dagli Errori**: a volte qualcosa va storto—magari la rete fallisce o l’API non restituisce ciò che ti aspetti. Il recupero dagli errori significa che il codice può gestire questi problemi e fornire feedback utili, invece di bloccarsi.
- **Validazione dei Parametri**: riguarda il controllo che tutti gli input agli strumenti siano corretti e sicuri da usare. Include l’impostazione di valori di default e la verifica dei tipi, aiutando a prevenire bug e confusione.

Questa sezione ti aiuterà a diagnosticare e risolvere problemi comuni che potresti incontrare lavorando con il Server MCP per la Ricerca Web. Se incontri errori o comportamenti inattesi, questa sezione di troubleshooting offre soluzioni ai problemi più frequenti. Consulta questi suggerimenti prima di chiedere aiuto—spesso risolvono rapidamente i problemi.

## Risoluzione dei Problemi

Quando lavori con il Server MCP per la Ricerca Web, potresti occasionalmente incontrare problemi—è normale quando si sviluppa con API esterne e nuovi strumenti. Questa sezione fornisce soluzioni pratiche ai problemi più comuni, così puoi tornare rapidamente operativo. Se incontri un errore, inizia da qui: i suggerimenti seguenti affrontano i problemi più frequenti e spesso risolvono il problema senza bisogno di ulteriore assistenza.

### Problemi Comuni

Di seguito alcuni dei problemi più frequenti riscontrati dagli utenti, con spiegazioni chiare e passaggi per risolverli:

1. **Manca SERPAPI_KEY nel file .env**
   - Se vedi l’errore `SERPAPI_KEY environment variable not found`, significa che l’applicazione non riesce a trovare la chiave API necessaria per accedere a SerpAPI. Per risolvere, crea un file chiamato `.env` nella root del progetto (se non esiste già) e aggiungi una riga come `SERPAPI_KEY=tuo_serpapi_key_qui`. Assicurati di sostituire `tuo_serpapi_key_qui` con la tua chiave reale dal sito SerpAPI.

2. **Errori di modulo non trovato**
   - Errori come `ModuleNotFoundError: No module named 'httpx'` indicano che manca un pacchetto Python richiesto. Succede di solito se non hai installato tutte le dipendenze. Per risolvere, esegui `pip install -r requirements.txt` nel terminale per installare tutto ciò che serve al progetto.

3. **Problemi di connessione**
   - Se ricevi un errore tipo `Error during client execution`, spesso significa che il client non riesce a connettersi al server, o che il server non è in esecuzione come previsto. Controlla che client e server siano versioni compatibili, e che `server.py` sia presente e in esecuzione nella directory corretta. Riavviare sia server che client può aiutare.

4. **Errori SerpAPI**
   - Se vedi `Search API returned error status: 401` significa che la tua chiave SerpAPI è mancante, errata o scaduta. Vai al tuo dashboard SerpAPI, verifica la chiave e aggiorna il file `.env` se necessario. Se la chiave è corretta ma l’errore persiste, controlla se il tuo piano gratuito ha esaurito la quota.

### Modalità Debug

Di default, l’app registra solo informazioni importanti. Se vuoi vedere più dettagli su cosa sta succedendo (ad esempio per diagnosticare problemi complessi), puoi abilitare la modalità DEBUG. Questo ti mostrerà molto di più su ogni passaggio che l’app compie.

**Esempio: Output Normale**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Esempio: Output DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Nota come la modalità DEBUG includa righe extra su richieste HTTP, risposte e altri dettagli interni. Questo può essere molto utile per il troubleshooting.
Per abilitare la modalità DEBUG, imposta il livello di logging su DEBUG all'inizio del tuo `client.py` o `server.py`:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Cosa fare dopo

- [5.10 Streaming in tempo reale](../mcp-realtimestreaming/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.