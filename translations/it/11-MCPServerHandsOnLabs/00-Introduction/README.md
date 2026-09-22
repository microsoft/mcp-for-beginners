# Introduzione all’integrazione del database MCP

> [!NOTE]
> Diagrammi o codice in questo percorso di apprendimento che utilizzano HTTP/SSE o opzioni di inizializzazione riflettono le dipendenze MCP `2025-11-25` del campione. Per nuove implementazioni, utilizzare richieste senza stato `2026-07-28` e HTTP Streamable.
> 
> 

## 🎯 Cosa Copre Questo Laboratorio

Questo laboratorio introduttivo fornisce una panoramica completa sulla costruzione di server Model Context Protocol (MCP) con integrazione al database. Comprenderai il caso aziendale, l’architettura tecnica e le applicazioni reali attraverso il caso d’uso di analisi Zava Retail su https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Panoramica

**Model Context Protocol (MCP)** consente agli assistenti AI di accedere e interagire in modo sicuro con fonti di dati esterne in tempo reale. Quando combinato con l’integrazione al database, MCP sblocca potenti capacità per applicazioni AI basate sui dati.

Questo percorso di apprendimento ti insegna a costruire server MCP pronti per la produzione che collegano assistenti AI ai dati di vendita al dettaglio tramite PostgreSQL, implementando modelli aziendali come la Row Level Security, la ricerca semantica e l’accesso multi-tenant ai dati.

## Obiettivi di Apprendimento

Al termine di questo laboratorio, sarai in grado di:

- **Definire** il Model Context Protocol e i suoi benefici principali per l’integrazione al database
- **Identificare** i componenti chiave dell’architettura di un server MCP con database
- **Comprendere** il caso d’uso Zava Retail e i suoi requisiti aziendali
- **Riconoscere** i modelli enterprise per un accesso sicuro e scalabile ai database
- **Elencare** gli strumenti e le tecnologie utilizzate in questo percorso di apprendimento

## 🧭 La Sfida: L’AI incontra i Dati del Mondo Reale

### Limitazioni Tradizionali dell’AI

Gli assistenti AI moderni sono incredibilmente potenti ma affrontano limitazioni significative quando lavorano con dati aziendali reali:

| **Sfida** | **Descrizione** | **Impatto Aziendale** |
|---------------|-----------------|-------------------|
| **Conoscenza Statica** | Modelli AI addestrati su dataset fissi non possono accedere ai dati aziendali attuali | Informazioni obsolete, opportunità perse |
| **Silos di Dati** | Informazioni bloccate in database, API e sistemi inaccessibili all’AI | Analisi incomplete, workflow frammentati |
| **Vincoli di Sicurezza** | Accesso diretto ai database solleva problemi di sicurezza e conformità | Distribuzione limitata, preparazione manuale dei dati |
| **Query Complesse** | Gli utenti aziendali necessitano conoscenze tecniche per estrarre insight dai dati | Adozione ridotta, processi inefficienti |

### La Soluzione MCP

Il Model Context Protocol affronta queste sfide fornendo:

- **Accesso in Tempo Reale ai Dati**: Gli assistenti AI interrogano database e API live
- **Integrazione Sicura**: Accesso controllato con autenticazione e permessi
- **Interfaccia in Linguaggio Naturale**: Gli utenti aziendali fanno domande in inglese semplice
- **Protocollo Standardizzato**: Funziona attraverso diverse piattaforme e strumenti AI

## 🏪 Incontra Zava Retail: Il Nostro Caso di Studio https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

In questo percorso, costruiremo un server MCP per **Zava Retail**, una catena di negozi fai-da-te fittizia con più sedi. Questo scenario realistico dimostra un’implementazione MCP di livello enterprise.

### Contesto Aziendale

**Zava Retail** opera:
- **8 negozi fisici** nello stato di Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 negozio online** per vendite e-commerce
- **Catalogo prodotti diversificato** che include utensili, ferramenta, forniture da giardino e materiali da costruzione
- **Gestione multilivello** con responsabili di negozio, manager regionali e dirigenti

### Requisiti Aziendali

I responsabili di negozio e i dirigenti necessitano di analisi alimentate da AI per:

1. **Analizzare le prestazioni di vendita** tra negozi e periodi temporali
2. **Monitorare i livelli di inventario** e identificare necessità di rifornimento
3. **Comprendere il comportamento dei clienti** e i modelli di acquisto
4. **Scoprire insight sui prodotti** tramite ricerca semantica
5. **Generare report** con query in linguaggio naturale
6. **Mantenere la sicurezza dei dati** con controllo di accesso basato sui ruoli

### Requisiti Tecnici

Il server MCP deve fornire:

- **Accesso multi-tenant ai dati** dove i responsabili vedono solo i dati del proprio negozio
- **Query flessibili** che supportano operazioni SQL complesse
- **Ricerca semantica** per scoperta prodotti e raccomandazioni
- **Dati in tempo reale** che riflettono lo stato attuale dell’azienda
- **Autenticazione sicura** con row-level security
- **Architettura scalabile** che supporta utenti multipli simultanei

## 🏗️ Panoramica dell’Architettura del Server MCP

Il nostro server MCP implementa un’architettura a strati ottimizzata per l’integrazione database:

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

### Componenti Chiave

#### **1. Strato Server MCP**
- **Framework FastMCP**: Implementazione moderna in Python del server MCP
- **Registrazione Strumenti**: Definizioni dichiarative di strumenti con sicurezza di tipo
- **Contesto Richiesta**: Gestione identità utente e sessione
- **Gestione Errori**: Gestione robusta degli errori e logging

#### **2. Strato di Integrazione Database**
- **Connection Pooling**: Gestione efficiente delle connessioni asyncpg
- **Provider Schema**: Scoperta dinamica degli schemi delle tabelle
- **Executor Query**: Esecuzione sicura di SQL con contesto RLS
- **Gestione Transazioni**: Conformità ACID e gestione rollback

#### **3. Strato di Sicurezza**
- **Row Level Security**: RLS PostgreSQL per isolamento dati multi-tenant
- **Identità Utente**: Autenticazione e autorizzazione dei responsabili negozio
- **Controllo Accessi**: Permessi granulari e audit trail
- **Validazione Input**: Prevenzione SQL injection e validazione query

#### **4. Strato di Potenziamento AI**
- **Ricerca Semantica**: Embedding vettoriali per scoperta prodotti
- **Integrazione Azure OpenAI**: Generazione embedding testuali
- **Algoritmi di Similarità**: Ricerca di similarità coseno con pgvector
- **Ottimizzazione della Ricerca**: Indicizzazione e tuning delle performance

## 🔧 Stack Tecnologico

### Tecnologie Principali

| **Componente** | **Tecnologia** | **Scopo** |
|---------------|----------------|-------------|
| **Framework MCP** | FastMCP (Python) | Implementazione moderna server MCP |
| **Database** | PostgreSQL 17 + pgvector | Dati relazionali con ricerca vettoriale |
| **Servizi AI** | Azure OpenAI | Embedding testuali e modelli linguistici |
| **Containerizzazione** | Docker + Docker Compose | Ambiente di sviluppo |
| **Piattaforma Cloud** | Microsoft Azure | Distribuzione in produzione |
| **Integrazione IDE** | VS Code | AI Chat e workflow di sviluppo |

### Strumenti di Sviluppo

| **Strumento** | **Scopo** |
|----------|-------------|
| **asyncpg** | Driver PostgreSQL ad alte prestazioni |
| **Pydantic** | Validazione e serializzazione dati |
| **Azure SDK** | Integrazione servizi cloud |
| **pytest** | Framework di testing |
| **Docker** | Containerizzazione e distribuzione |

### Stack di Produzione

| **Servizio** | **Risorsa Azure** | **Scopo** |
|-------------|-------------------|-------------|
| **Database** | Azure Database for PostgreSQL | Servizio database gestito |
| **Container** | Azure Container Apps | Hosting container serverless |
| **Servizi AI** | Microsoft Foundry | Modelli e endpoint OpenAI |
| **Monitoraggio** | Application Insights | Osservabilità e diagnostica |
| **Sicurezza** | Azure Key Vault | Gestione segreti e configurazioni |

## 🎬 Scenari d’Uso nel Mondo Reale

Esploriamo come diversi utenti interagiscono con il nostro server MCP:

### Scenario 1: Revisione delle Prestazioni del Responsabile di Negozio

**Utente**: Sarah, Responsabile Negozio di Seattle  
**Obiettivo**: Analizzare le prestazioni di vendita dell’ultimo trimestre

**Query in Linguaggio Naturale**:
> "Mostrami i primi 10 prodotti per fatturato nel mio negozio nel Q4 2024"

**Cosa Succede**:
1. VS Code AI Chat invia la query al server MCP
2. Il server MCP identifica il contesto del negozio di Sarah (Seattle)
3. Le policy RLS filtrano i dati solo per il negozio di Seattle
4. Viene generata ed eseguita la query SQL
5. I risultati vengono formattati e restituiti all’AI Chat
6. L’AI fornisce analisi e insight

### Scenario 2: Scoperta Prodotti con Ricerca Semantica

**Utente**: Mike, Responsabile Inventario  
**Obiettivo**: Trovare prodotti simili a una richiesta cliente

**Query in Linguaggio Naturale**:
> "Quali prodotti vendiamo simili a ‘connettori elettrici impermeabili per uso esterno’?"

**Cosa Succede**:
1. Query elaborata dallo strumento di ricerca semantica
2. Azure OpenAI genera l’embedding vettoriale
3. pgvector esegue la ricerca di similarità
4. I prodotti correlati sono classificati per rilevanza
5. I risultati includono dettagli prodotto e disponibilità
6. L’AI suggerisce alternative e opportunità di bundle

### Scenario 3: Analisi Cross-Negozio

**Utente**: Jennifer, Manager Regionale  
**Obiettivo**: Confrontare le prestazioni di tutti i negozi

**Query in Linguaggio Naturale**:
> "Confronta le vendite per categoria in tutti i negozi negli ultimi 6 mesi"

**Cosa Succede**:
1. Contesto RLS impostato per l’accesso del manager regionale
2. Query complessa multi-negozio generata
3. Dati aggregati tra le sedi
4. Risultati includono trend e confronti
5. L’AI identifica insight e raccomandazioni

## 🔒 Approfondimento su Sicurezza e Multi-Tenancy

La nostra implementazione dà priorità alla sicurezza di livello enterprise:

### Row Level Security (RLS)

PostgreSQL RLS assicura l’isolamento dei dati:

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

### Gestione Identità Utente

Ogni connessione MCP include:
- **ID Responsabile Negozio**: Identificatore unico per contesto RLS
- **Assegnazione Ruoli**: Permessi e livelli di accesso
- **Gestione Sessione**: Token di autenticazione sicuri
- **Audit Logging**: Storico completo degli accessi

### Protezione dei Dati

Molteplici livelli di sicurezza:
- **Crittografia Connessioni**: TLS per tutte le connessioni al database
- **Prevenzione SQL Injection**: Solo query parametrizzate
- **Validazione Input**: Validazione completa delle richieste
- **Gestione Errori**: Nessun dato sensibile nei messaggi di errore

## 🎯 Punti Chiave da Ricordare

Dopo aver completato questa introduzione, dovresti comprendere:

✅ **Valore MCP**: Come MCP collega assistenti AI e dati reali  
✅ **Contesto Aziendale**: Requisiti e sfide di Zava Retail  
✅ **Panoramica Architettura**: Componenti chiave e loro interazioni  
✅ **Stack Tecnologico**: Strumenti e framework utilizzati  
✅ **Modello di Sicurezza**: Accesso multi-tenant e protezione  
✅ **Pattern d’Uso**: Scenari di query reali e workflow  

## 🚀 Cosa Fare Dopo

Pronto a approfondire? Continua con:

**[Lab 01: Concetti Chiave di Architettura](../01-Architecture/README.md)**

Scopri i pattern architetturali del server MCP, i principi di progettazione database e l’implementazione tecnica dettagliata alla base della nostra soluzione di analisi retail.

## 📚 Risorse Aggiuntive

### Documentazione MCP
- [Specifiche MCP](https://modelcontextprotocol.io/docs/) - Documentazione ufficiale del protocollo
- [MCP per Principianti](https://aka.ms/mcp-for-beginners) - Guida completa all’apprendimento MCP
- [Documentazione FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentazione SDK Python

### Integrazione Database
- [Documentazione PostgreSQL](https://www.postgresql.org/docs/) - Riferimento completo PostgreSQL
- [Guida pgvector](https://github.com/pgvector/pgvector) - Documentazione estensione vettoriale
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guida RLS PostgreSQL

### Servizi Azure
- [Documentazione Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrazione servizio AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Servizio database gestito
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Container serverless

---

**Disclaimer**: Questo è un esercizio di apprendimento che utilizza dati retail fittizi. Segui sempre le politiche di governance e sicurezza dei dati della tua organizzazione quando implementi soluzioni simili in ambienti di produzione.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->