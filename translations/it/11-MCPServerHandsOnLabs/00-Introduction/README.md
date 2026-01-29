# Introduzione all'integrazione del database MCP

## 🎯 Cosa copre questo laboratorio

Questo laboratorio introduttivo offre una panoramica completa sulla creazione di server Model Context Protocol (MCP) con integrazione al database. Comprenderai il caso aziendale, l'architettura tecnica e le applicazioni reali attraverso il caso d'uso di analisi di Zava Retail disponibile su https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Panoramica

**Model Context Protocol (MCP)** consente agli assistenti AI di accedere e interagire in modo sicuro con fonti di dati esterne in tempo reale. Quando combinato con l'integrazione al database, MCP sblocca potenti capacità per applicazioni AI basate sui dati.

Questo percorso di apprendimento ti insegna a costruire server MCP pronti per la produzione che collegano gli assistenti AI ai dati di vendita al dettaglio tramite PostgreSQL, implementando modelli aziendali come la sicurezza a livello di riga, la ricerca semantica e l'accesso ai dati multi-tenant.

## Obiettivi di apprendimento

Alla fine di questo laboratorio, sarai in grado di:

- **Definire** il Model Context Protocol e i suoi principali vantaggi per l'integrazione al database
- **Identificare** i componenti chiave di un'architettura server MCP con database
- **Comprendere** il caso d'uso di Zava Retail e i suoi requisiti aziendali
- **Riconoscere** modelli aziendali per un accesso sicuro e scalabile ai database
- **Elencare** gli strumenti e le tecnologie utilizzati in questo percorso di apprendimento

## 🧭 La sfida: l'AI incontra i dati reali

### Limitazioni tradizionali dell'AI

Gli assistenti AI moderni sono incredibilmente potenti ma affrontano significative limitazioni quando lavorano con dati aziendali reali:

| **Sfida** | **Descrizione** | **Impatto aziendale** |
|-----------|-----------------|-----------------------|
| **Conoscenza statica** | I modelli AI addestrati su dataset fissi non possono accedere ai dati aziendali attuali | Insight obsoleti, opportunità perse |
| **Silos di dati** | Informazioni bloccate in database, API e sistemi che l'AI non può raggiungere | Analisi incomplete, flussi di lavoro frammentati |
| **Vincoli di sicurezza** | L'accesso diretto al database solleva preoccupazioni di sicurezza e conformità | Distribuzione limitata, preparazione manuale dei dati |
| **Query complesse** | Gli utenti aziendali necessitano di conoscenze tecniche per estrarre insight dai dati | Ridotta adozione, processi inefficienti |

### La soluzione MCP

Model Context Protocol affronta queste sfide fornendo:

- **Accesso ai dati in tempo reale**: Gli assistenti AI interrogano database e API live
- **Integrazione sicura**: Accesso controllato con autenticazione e permessi
- **Interfaccia in linguaggio naturale**: Gli utenti aziendali pongono domande in inglese semplice
- **Protocollo standardizzato**: Funziona su diverse piattaforme e strumenti AI

## 🏪 Conosci Zava Retail: il nostro caso studio https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Durante questo percorso di apprendimento, costruiremo un server MCP per **Zava Retail**, una catena di fai-da-te fittizia con più sedi. Questo scenario realistico dimostra un'implementazione MCP di livello aziendale.

### Contesto aziendale

**Zava Retail** gestisce:
- **8 negozi fisici** nello stato di Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 negozio online** per le vendite e-commerce
- **Catalogo prodotti diversificato** che include utensili, hardware, forniture per giardini e materiali da costruzione
- **Gestione multilivello** con responsabili di negozio, responsabili regionali e dirigenti

### Requisiti aziendali

I responsabili di negozio e i dirigenti necessitano di analisi AI per:

1. **Analizzare le prestazioni di vendita** tra negozi e periodi di tempo
2. **Monitorare i livelli di inventario** e identificare le necessità di riassortimento
3. **Comprendere il comportamento dei clienti** e i modelli di acquisto
4. **Scoprire insight sui prodotti** tramite ricerca semantica
5. **Generare report** con query in linguaggio naturale
6. **Mantenere la sicurezza dei dati** con controllo degli accessi basato sui ruoli

### Requisiti tecnici

Il server MCP deve fornire:

- **Accesso ai dati multi-tenant** dove i responsabili di negozio vedono solo i dati del proprio negozio
- **Query flessibili** che supportano operazioni SQL complesse
- **Ricerca semantica** per la scoperta e le raccomandazioni sui prodotti
- **Dati in tempo reale** che riflettono lo stato aziendale attuale
- **Autenticazione sicura** con sicurezza a livello di riga
- **Architettura scalabile** che supporta più utenti simultanei

## 🏗️ Panoramica dell'architettura del server MCP

Il nostro server MCP implementa un'architettura stratificata ottimizzata per l'integrazione al database:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Componenti chiave

#### **1. Livello server MCP**
- **Framework FastMCP**: Implementazione moderna del server MCP in Python
- **Registrazione degli strumenti**: Definizioni dichiarative degli strumenti con sicurezza dei tipi
- **Contesto delle richieste**: Gestione dell'identità utente e delle sessioni
- **Gestione degli errori**: Gestione robusta degli errori e logging

#### **2. Livello di integrazione al database**
- **Pooling delle connessioni**: Gestione efficiente delle connessioni asyncpg
- **Provider dello schema**: Scoperta dinamica dello schema delle tabelle
- **Esecutore delle query**: Esecuzione SQL sicura con contesto RLS
- **Gestione delle transazioni**: Conformità ACID e gestione dei rollback

#### **3. Livello di sicurezza**
- **Sicurezza a livello di riga**: RLS di PostgreSQL per l'isolamento dei dati multi-tenant
- **Identità utente**: Autenticazione e autorizzazione dei responsabili di negozio
- **Controllo degli accessi**: Permessi dettagliati e tracciabilità
- **Validazione degli input**: Prevenzione delle iniezioni SQL e validazione delle query

#### **4. Livello di miglioramento AI**
- **Ricerca semantica**: Embedding vettoriali per la scoperta dei prodotti
- **Integrazione Azure OpenAI**: Generazione di embedding testuali
- **Algoritmi di similarità**: Ricerca di similarità con pgvector e coseno
- **Ottimizzazione della ricerca**: Indicizzazione e tuning delle prestazioni

## 🔧 Stack tecnologico

### Tecnologie principali

| **Componente** | **Tecnologia** | **Scopo** |
|----------------|----------------|-----------|
| **Framework MCP** | FastMCP (Python) | Implementazione moderna del server MCP |
| **Database** | PostgreSQL 17 + pgvector | Dati relazionali con ricerca vettoriale |
| **Servizi AI** | Azure OpenAI | Embedding testuali e modelli linguistici |
| **Containerizzazione** | Docker + Docker Compose | Ambiente di sviluppo |
| **Piattaforma cloud** | Microsoft Azure | Distribuzione in produzione |
| **Integrazione IDE** | VS Code | Chat AI e flusso di lavoro di sviluppo |

### Strumenti di sviluppo

| **Strumento** | **Scopo** |
|---------------|-----------|
| **asyncpg** | Driver PostgreSQL ad alte prestazioni |
| **Pydantic** | Validazione e serializzazione dei dati |
| **SDK Azure** | Integrazione dei servizi cloud |
| **pytest** | Framework di test |
| **Docker** | Containerizzazione e distribuzione |

### Stack di produzione

| **Servizio** | **Risorsa Azure** | **Scopo** |
|--------------|-------------------|-----------|
| **Database** | Azure Database for PostgreSQL | Servizio di database gestito |
| **Container** | Azure Container Apps | Hosting serverless di container |
| **Servizi AI** | Azure AI Foundry | Modelli OpenAI e endpoint |
| **Monitoraggio** | Application Insights | Osservabilità e diagnostica |
| **Sicurezza** | Azure Key Vault | Gestione di segreti e configurazioni |

## 🎬 Scenari di utilizzo reale

Esploriamo come diversi utenti interagiscono con il nostro server MCP:

### Scenario 1: Revisione delle prestazioni del responsabile di negozio

**Utente**: Sarah, responsabile del negozio di Seattle  
**Obiettivo**: Analizzare le prestazioni di vendita dell'ultimo trimestre

**Query in linguaggio naturale**:
> "Mostrami i 10 prodotti principali per ricavi nel mio negozio nel Q4 2024"

**Cosa succede**:
1. La chat AI di VS Code invia la query al server MCP
2. Il server MCP identifica il contesto del negozio di Sarah (Seattle)
3. Le politiche RLS filtrano i dati solo per il negozio di Seattle
4. La query SQL viene generata ed eseguita
5. I risultati vengono formattati e restituiti alla chat AI
6. L'AI fornisce analisi e insight

### Scenario 2: Scoperta di prodotti con ricerca semantica

**Utente**: Mike, responsabile dell'inventario  
**Obiettivo**: Trovare prodotti simili a una richiesta del cliente

**Query in linguaggio naturale**:
> "Quali prodotti vendiamo simili a 'connettori elettrici impermeabili per uso esterno'?"

**Cosa succede**:
1. La query viene elaborata dallo strumento di ricerca semantica
2. Azure OpenAI genera un vettore di embedding
3. pgvector esegue la ricerca di similarità
4. I prodotti correlati vengono classificati per rilevanza
5. I risultati includono dettagli sui prodotti e disponibilità
6. L'AI suggerisce alternative e opportunità di bundle

### Scenario 3: Analisi trasversale tra negozi

**Utente**: Jennifer, responsabile regionale  
**Obiettivo**: Confrontare le prestazioni tra tutti i negozi

**Query in linguaggio naturale**:
> "Confronta le vendite per categoria in tutti i negozi negli ultimi 6 mesi"

**Cosa succede**:
1. Il contesto RLS viene impostato per l'accesso del responsabile regionale
2. Viene generata una query complessa multi-negozio
3. I dati vengono aggregati tra le sedi dei negozi
4. I risultati includono tendenze e confronti
5. L'AI identifica insight e raccomandazioni

## 🔒 Approfondimento sulla sicurezza e multi-tenancy

La nostra implementazione dà priorità alla sicurezza di livello aziendale:

### Sicurezza a livello di riga (RLS)

PostgreSQL RLS garantisce l'isolamento dei dati:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Gestione dell'identità utente

Ogni connessione MCP include:
- **ID del responsabile di negozio**: Identificatore univoco per il contesto RLS
- **Assegnazione dei ruoli**: Permessi e livelli di accesso
- **Gestione delle sessioni**: Token di autenticazione sicuri
- **Registrazione degli audit**: Storico completo degli accessi

### Protezione dei dati

Molteplici livelli di sicurezza:
- **Crittografia delle connessioni**: TLS per tutte le connessioni al database
- **Prevenzione delle iniezioni SQL**: Solo query parametrizzate
- **Validazione degli input**: Validazione completa delle richieste
- **Gestione degli errori**: Nessun dato sensibile nei messaggi di errore

## 🎯 Punti chiave

Dopo aver completato questa introduzione, dovresti comprendere:

✅ **Proposta di valore MCP**: Come MCP collega gli assistenti AI ai dati reali  
✅ **Contesto aziendale**: Requisiti e sfide di Zava Retail  
✅ **Panoramica dell'architettura**: Componenti chiave e loro interazioni  
✅ **Stack tecnologico**: Strumenti e framework utilizzati  
✅ **Modello di sicurezza**: Accesso ai dati multi-tenant e protezione  
✅ **Modelli di utilizzo**: Scenari di query reali e flussi di lavoro  

## 🚀 Prossimi passi

Pronto per approfondire? Continua con:

**[Lab 01: Concetti di architettura di base](../01-Architecture/README.md)**

Scopri i modelli di architettura del server MCP, i principi di progettazione del database e l'implementazione tecnica dettagliata che alimenta la nostra soluzione di analisi al dettaglio.

## 📚 Risorse aggiuntive

### Documentazione MCP
- [Specifiche MCP](https://modelcontextprotocol.io/docs/) - Documentazione ufficiale del protocollo
- [MCP per principianti](https://aka.ms/mcp-for-beginners) - Guida completa all'apprendimento MCP
- [Documentazione FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentazione SDK Python

### Integrazione al database
- [Documentazione PostgreSQL](https://www.postgresql.org/docs/) - Riferimento completo PostgreSQL
- [Guida pgvector](https://github.com/pgvector/pgvector) - Documentazione dell'estensione vettoriale
- [Sicurezza a livello di riga](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guida RLS PostgreSQL

### Servizi Azure
- [Documentazione Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrazione dei servizi AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Servizio di database gestito
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Container serverless

---

**Disclaimer**: Questo è un esercizio di apprendimento che utilizza dati al dettaglio fittizi. Segui sempre le politiche di governance e sicurezza dei dati della tua organizzazione quando implementi soluzioni simili in ambienti di produzione.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.