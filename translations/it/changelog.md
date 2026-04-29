# Registro delle Modifiche: Curriculum MCP per Principianti

Questo documento serve come registro di tutti i cambiamenti significativi apportati al curriculum Model Context Protocol (MCP) per principianti. I cambiamenti sono documentati in ordine cronologico inverso (modifiche più recenti prima).

## 11 aprile 2026

### Nuova Lezione, Correzioni della Documentazione e Aggiornamenti delle Dipendenze

#### Nuovi Contenuti del Curriculum Aggiunti

**Modulo 05 - Argomenti Avanzati**
- **Lezione 5.17: Ragionamento Adversariale Multi-Agente con MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nuova guida completa che copre il modello di dibattito adversariale per sistemi multi-agente
  - Diagramma architetturale Mermaid: due agenti → server MCP condiviso → trascrizione del dibattito → giudice → verdetto
  - Server strumento MCP condiviso (`web_search` + `run_python`) implementato in Python e TypeScript
  - Prompt di sistema opposti (PER / CONTRO / Giudice) con requisiti espliciti per l’uso degli strumenti
  - Orchestratore del dibattito in Python, TypeScript e C# che gestisce i round e instrada gli argomenti
  - Collegamento MCP `ClientSession` per l’orchestratore alle chiamate reali degli strumenti
  - Tabella dei casi d’uso (rilevazione di allucinazioni, modellazione delle minacce, revisione del design API, verifica fattuale, selezione tecnologica)
  - Considerazioni sulla sicurezza: esecuzione sandbox, validazione chiamate strumento, limitazione del tasso, registrazione audit
  - Esercizio strutturato con tre scenari pratici (revisione codice, decisione architetturale, moderazione contenuti)

#### Correzioni della Documentazione

**Modulo 03 - Iniziare**
- **05-stdio-server/README.md**: Corretto esempio incompleto del server stdio TypeScript — aggiunta istanziazione mancante del trasporto (`new StdioServerTransport()`) e chiamata `server.connect(transport)` per allinearsi agli esempi Python e .NET nella stessa sezione
- **14-sampling/README.md**: Corretto errore di battitura — corretto `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Aggiornamenti del Curriculum

**README principale.md**
- Aggiunta voce 5.17 (Ragionamento Adversariale Multi-Agente con MCP) alla tabella del curriculum con link diretto alla nuova lezione

**05-AdvancedTopics/README.md**
- Aggiunta la riga Lezione 5.17 alla tabella delle lezioni

**study_guide.md**
- Aggiunto il tema Ragionamento Adversariale Multi-Agente alla mappa mentale e alla descrizione in prosa degli Argomenti Avanzati

#### Correzioni di Codice e Sicurezza

**Modulo 05 - Agenti Adversariali (`mcp-adversarial-agents`)**
- **Correzione sicurezza — iniezione di comando**: Sostituita interpolazione shell `execSync` con `execFile` + `promisify` nello strumento TypeScript `run_python`, eliminando la superficie di iniezione di comando (il codice controllato LLM ora è passato come elemento argv letterale senza invocazione shell)
- **Collegamento ciclo strumento MCP**: Aggiornato orchestratore del dibattito Python per usare client `AsyncAnthropic` (sostituisce `Anthropic` sincrono bloccante), passare una `ClientSession` live direttamente a ogni turno agente, recuperare definizioni strumenti via `session.list_tools()` ad ogni turno, e inviare blocchi `tool_use` tramite `session.call_tool()` in ciclo fino alla risposta finale del modello

#### Aggiornamenti delle Dipendenze

- Aggiornato `hono` a 4.12.12 in più pacchetti (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Aggiornato `@hono/node-server` da 1.19.11 a 1.19.13 nei pacchetti TypeScript
- Aggiornato `cryptography` da 46.0.5 a 46.0.7 nei pacchetti Python (laboratori 3 e 4 di 10-StreamliningAIWorkflows)
- Aggiornato `lodash` da 4.17.23 a 4.18.1 nell’ispezione 10-StreamliningAIWorkflows

#### Traduzioni

- Sincronizzate le traduzioni per oltre 48 lingue con le ultime modifiche della sorgente (aggiornamento i18n)

---

## 5 febbraio 2026

### Validazioni Trasversali del Repository e Miglioramenti di Navigazione

#### Nuovi Contenuti del Curriculum Aggiunti

**Modulo 03 - Iniziare**
- **12-mcp-hosts/README.md**: Nuova guida completa per la configurazione degli host MCP
  - Esempi di configurazione Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Template di configurazione JSON per tutti gli host principali
  - Tabella comparativa dei tipi di trasporto (stdio, SSE/HTTP, WebSocket)
  - Risoluzione dei problemi comuni di connessione
  - Best practice di sicurezza per la configurazione dell’host

- **13-mcp-inspector/README.md**: Nuova guida al debug per MCP Inspector
  - Metodi di installazione (npx, npm globale, da sorgente)
  - Connessione a server via stdio e HTTP/SSE
  - Strumenti di testing, risorse e workflow di prompt
  - Integrazione VS Code con MCP Inspector
  - Scenari comuni di debug con soluzioni

**Modulo 04 - Implementazione Pratica**
- **pagination/README.md**: Nuova guida all’implementazione della paginazione
  - Pattern di paginazione basati su cursore in Python, TypeScript, Java
  - Gestione della paginazione client-side
  - Strategie di design del cursore (opaco vs strutturato)
  - Raccomandazioni per ottimizzazione delle prestazioni

**Modulo 05 - Argomenti Avanzati**
- **mcp-protocol-features/README.md**: Approfondimento sulle nuove funzionalità del protocollo
  - Implementazione di notifiche di progresso
  - Pattern di cancellazione richiesta
  - Template di risorse con pattern URI
  - Gestione del ciclo di vita del server
  - Controllo del livello di logging
  - Pattern di gestione errori con codici JSON-RPC

#### Correzioni di Navigazione (oltre 24 file aggiornati)

**README moduli principali**
 Ora link a prima lezione E al modulo successivo

**Sotto-file 02-Security**
- Tutti i 5 documenti di sicurezza supplementari ora hanno navigazione "Cosa c’è dopo"

**File 09-CaseStudy**
- Tutti i case study ora hanno navigazione sequenziale

**Laboratori 10-StreamliningAI**
Aggiunta sezione "Cosa c’è dopo" all’overview Modulo 10 e Modulo 11

#### Correzioni di Codice e Contenuti

**Aggiornamenti SDK e Dipendenze**
Versione openai vuota fissata a `^4.95.0`
Aggiornamento SDK da `^1.8.0` a `>=1.26.0`
Aggiornamento pin versione mcp a `>=1.26.0`

**Correzioni codice**
Corretto modello invalido `gpt-4o-mini` in `gpt-4.1-mini`

**Correzioni contenuti**
Corretto link rotto `READMEmd` → `README.md`, corretto header curriculum `Module 1-3` → `Module 0-3`, corretto percorso case-sensitive 
Rimosso contenuto duplicato corrotto Case Study 5

**Miglioramenti guida principianti**
Introdotto corretto introduzione, obiettivi di apprendimento e prerequisiti per principianti

#### Aggiornamenti del Curriculum

**README principale.md**
- Aggiunte voci 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) nella tabella del curriculum

**README moduli**
Aggiunte lezioni 12 e 13 alla lista lezioni
Aggiunta sezione Guide Pratiche con link a pagination
Aggiunte lezioni 5.15 (Trasporto Personalizzato) e 5.16 (Protocol Features)

**study_guide.md**
- Aggiornata mappa mentale con tutti i nuovi argomenti: Configurazione MCP Hosts, MCP Inspector, Strategie di Paginazione, Approfondimento Funzionalità Protocollo

## 28 gennaio 2026

### Revisione Conformità Specifica MCP 2025-11-25

#### Potenziamento Concetti Base (01-CoreConcepts/)
- **Nuova Primitiva Client - Roots**: Aggiunta documentazione completa sulla primitiva client Roots, che consente ai server di comprendere i confini del filesystem e i permessi di accesso
- **Annotazioni per Strumenti**: Aggiunta documentazione sulle annotazioni comportamentali degli strumenti (`readOnlyHint`, `destructiveHint`) per decisioni migliori sull’esecuzione
- **Chiamata Strumenti nel Sampling**: Aggiornata documentazione Sampling per includere parametri `tools` e `toolChoice` per invocazione di strumenti guidata dal modello durante le richieste di campionamento
- **Elicitation Modalità URL**: Aggiunta documentazione sull’elicitation via URL per interazioni web esterne avviate dal server
- **Tasks (Sperimentale)**: Aggiunta nuova sezione che documenta la funzionalità sperimentale Tasks per wrapper di esecuzione duratura e recupero ritardato dei risultati
- **Supporto Icone**: Segnalato che strumenti, risorse, template di risorse e prompt possono ora includere icone come metadati aggiuntivi

#### Aggiornamenti Documentazione
- **README.md**: Aggiunto riferimento versione MCP Specification 2025-11-25 e spiegazione versioning basato sulla data
- **study_guide.md**: Aggiornata mappa del curriculum per includere Tasks e Annotazioni per Strumenti nella sezione Concetti Base; aggiornato timestamp documento

#### Verifica Conformità Specifica
- **Versione Protocollo**: Verificate tutte le documentazioni al riferimento corrente MCP Specification 2025-11-25
- **Allineamento Architetturale**: Confermata accuratezza documentazione architettura a due livelli (Data Layer + Transport Layer)
- **Documentazione Primitive**: Validate primitive server (Risorse, Prompt, Strumenti) e client (Sampling, Elicitation, Logging, Roots)
- **Meccanismi di Trasporto**: Verificata accuratezza documentazione trasporti STDIO e HTTP Streaming
- **Indicazioni di Sicurezza**: Confermato allineamento con la documentazione Best Practices di Sicurezza MCP attuali

#### Funzionalità Chiave MCP 2025-11-25 Documentate
- **OpenID Connect Discovery**: Scoperta server di autenticazione tramite OIDC
- **Documenti Metadata Client ID OAuth**: Meccanismo raccomandato per registrazione client
- **JSON Schema 2020-12**: Dialetto predefinito per definizioni schema MCP
- **Sistema di Livelli SDK**: Requisiti formalizzati per supporto e manutenzione funzionalità SDK
- **Struttura di Governance**: Formalizzazione Working Groups e Interest Groups nella governance MCP

### Aggiornamento Principale Documentazione Sicurezza (02-Security/)

#### Integrazione MCP Security Summit Workshop (Sherpa)
- **Nuova Risorsa Formativa Pratica**: Aggiunta integrazione completa con [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) in tutta la documentazione di sicurezza
- **Copertura Itinerario Spedizione**: Documentata progressione completa da Base Camp a Summit
- **Allineamento OWASP**: Tutte le indicazioni di sicurezza ora mappate ai rischi OWASP MCP Azure Security Guide

#### Integrazione OWASP MCP Top 10
- **Nuova Sezione**: Aggiunta tabella dei Rischi di Sicurezza OWASP MCP Top 10 con mitigazioni Azure nel README principale Sicurezza
- **Documentazione Basata su Rischi**: Aggiornato mcp-security-controls-2025.md con riferimenti rischi OWASP MCP per ogni dominio di sicurezza
- **Architettura di Riferimento**: Linkata architettura di riferimento OWASP MCP Azure Security Guide e pattern di implementazione

#### File di Sicurezza Aggiornati
- **README.md**: Aggiunta overview Sherpa Workshop, tabella itinerario spedizione, riepilogo rischi OWASP MCP Top 10 e sezione formazione pratica
- **mcp-security-controls-2025.md**: Aggiornato header a febbraio 2026, aggiunti riferimenti rischi OWASP (MCP01-MCP08), corretta inconsistenza versione spec
- **mcp-security-best-practices-2025.md**: Aggiunte risorse Sherpa e OWASP, aggiornato timestamp
- **mcp-best-practices.md**: Aggiunta sezione formazione pratica con link Sherpa e OWASP
- **azure-content-safety-implementation.md**: Aggiunto riferimento OWASP MCP06, allineamento Sherpa Camp 3 e sezione risorse aggiuntive

#### Nuovi Link Risorse Aggiunti
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Pagine rischi individuali OWASP MCP (MCP01-MCP10)

### Allineamento Curriculum alla Specifica MCP 2025-11-25

#### Modulo 03 - Iniziare
- **Documentazione SDK**: Aggiunto Go SDK alla lista ufficiale SDK; aggiornati tutti riferimenti SDK per allineamento MCP Specification 2025-11-25
- **Chiarimenti Trasporto**: Aggiornate descrizioni trasporto STDIO e HTTP Streaming con riferimenti espliciti alla specifica

#### Modulo 04 - Implementazione Pratica
- **Aggiornamenti SDK**: Aggiunto Go SDK; aggiornata lista SDK con riferimento alla versione specifica
- **Spec Autorizzazione**: Aggiornato link specifica MCP Authorization alla versione corrente 2025-11-25

#### Modulo 05 - Argomenti Avanzati
- **Nuove Funzionalità**: Aggiunta nota sulle nuove funzionalità MCP Specification 2025-11-25 (Tasks, Annotazioni Strumenti, Elicitation Modalità URL, Roots)
- **Risorse Sicurezza**: Aggiunti link OWASP MCP Top 10 e Sherpa workshop alle referenze aggiuntive

#### Modulo 06 - Contributi Comunitari
- **Lista SDK**: Aggiunti SDK Swift e Rust; aggiornato link specifica a 2025-11-25
- **Riferimento Spec**: Aggiornato link MCP Specification a URL diretto della specifica

#### Modulo 07 - Lezioni dai Primi Adozioni
- **Aggiornamenti Risorse**: Aggiunto link MCP Specification 2025-11-25 e OWASP MCP Top 10 alle risorse aggiuntive

#### Modulo 08 - Best Practices
- **Versione Spec**: Aggiornato riferimento MCP Specification a 2025-11-25
- **Risorse Sicurezza**: Aggiunti OWASP MCP Top 10 e Sherpa workshop alle referenze aggiuntive

#### Modulo 10 - Ottimizzazione Flussi AI
- **Aggiornamento Badge**: Cambiata badge versione MCP da versione SDK (1.9.3) a versione specifica (2025-11-25)
- **Link Risorse**: Aggiornato link MCP Specification; aggiunto OWASP MCP Top 10

#### Modulo 11 - Laboratori MCP Server Hands-On
- **Riferimento Spec**: Aggiornato link MCP Specification alla versione 2025-11-25
- **Risorse Sicurezza**: Aggiunto OWASP MCP Top 10 alle risorse ufficiali

## 18 dicembre 2025
### Aggiornamento Documentazione sulla Sicurezza - Specifica MCP 2025-11-25

#### Best Practice di Sicurezza MCP (02-Security/mcp-best-practices.md) - Aggiornamento Versione Specifica
- **Aggiornamento Versione Protocollo**: Aggiornato per fare riferimento all’ultima Specifica MCP 2025-11-25 (rilasciata il 25 Novembre 2025)
  - Aggiornati tutti i riferimenti alla versione della specifica da 2025-06-18 a 2025-11-25
  - Aggiornate le date del documento da 18 Agosto 2025 a 18 Dicembre 2025
  - Verificati tutti gli URL della specifica puntano alla documentazione corrente
- **Validazione dei Contenuti**: Convalida completa delle best practice di sicurezza rispetto agli standard più recenti
  - **Soluzioni di Sicurezza Microsoft**: Verificata la terminologia attuale e i link per Prompt Shields (precedentemente "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, e Azure Key Vault
  - **Sicurezza OAuth 2.1**: Confermata l’allineamento con le più recenti best practice di sicurezza OAuth
  - **Standard OWASP**: Validati i riferimenti OWASP Top 10 per LLM rimangono aggiornati
  - **Servizi Azure**: Verificati tutti i link alla documentazione Microsoft Azure e alle best practice
- **Allineamento agli Standard**: Tutti gli standard di sicurezza citati confermati aggiornati
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Best Practice di Sicurezza OAuth 2.1
  - Framework di sicurezza e conformità Azure
- **Risorse di Implementazione**: Verificati tutti i link alle guide di implementazione e risorse
  - Pattern di autenticazione Azure API Management
  - Guide di integrazione Microsoft Entra ID
  - Gestione segreti Azure Key Vault
  - Pipeline DevSecOps e soluzioni di monitoraggio

### Garanzia di Qualità della Documentazione
- **Conformità alla Specifica**: Assicurata la corrispondenza di tutti i requisiti di sicurezza MCP obbligatori (MUST/MUST NOT) con l’ultima specifica
- **Aggiornamento Risorse**: Verificati tutti i link esterni a documentazione Microsoft, standard di sicurezza e guide di implementazione
- **Copertura delle Best Practice**: Confermata la copertura completa di autenticazione, autorizzazione, minacce specifiche AI, sicurezza della supply chain e pattern aziendali

## 6 Ottobre 2025

### Espansione della Sezione Getting Started – Uso Avanzato del Server & Autenticazione Semplice

#### Uso Avanzato del Server (03-GettingStarted/10-advanced)
- **Nuovo Capitolo Aggiunto**: Introdotta guida completa all’uso avanzato dei server MCP, coprendo sia architetture server regolari che di basso livello.
  - **Server Regolare vs. di Basso Livello**: Comparazione dettagliata ed esempi di codice in Python e TypeScript per entrambi gli approcci.
  - **Design Basato su Handler**: Spiegazione della gestione di strumenti/risorse/prompt basata su handler per implementazioni server scalabili e flessibili.
  - **Pattern Pratici**: Scenari reali in cui i pattern di server di basso livello sono utili per funzionalità avanzate e architetture complesse.

#### Autenticazione Semplice (03-GettingStarted/11-simple-auth)
- **Nuovo Capitolo Aggiunto**: Guida passo-passo per implementare autenticazione semplice nei server MCP.
  - **Concetti di Auth**: Spiegazione chiara di autenticazione vs autorizzazione e gestione delle credenziali.
  - **Implementazione Basic Auth**: Pattern di autenticazione basati su middleware in Python (Starlette) e TypeScript (Express), con esempi di codice.
  - **Evoluzione verso Sicurezza Avanzata**: Indicazioni per partire con autenticazione semplice e passare a OAuth 2.1 e RBAC, con riferimenti a moduli di sicurezza avanzati.

Queste aggiunte forniscono indicazioni pratiche per costruire implementazioni server MCP più robuste, sicure e flessibili, collegando concetti fondamentali a pattern avanzati di produzione.

## 29 Settembre 2025

### Lab di Integrazione Database per MCP Server - Percorso Completo di Apprendimento Pratico

#### 11-MCPServerHandsOnLabs - Nuovo Curriculum Completo per Integrazione Database
- **Percorso Completo in 13 Lab**: Aggiunto curriculum esaustivo per costruire server MCP pronti per la produzione con integrazione database PostgreSQL
  - **Implementazione nel Mondo Reale**: Caso d’uso analitico Zava Retail con pattern aziendali di livello enterprise
  - **Progressione di Apprendimento Strutturata**:
    - **Lab 00-03: Fondamenti** - Introduzione, architettura base, sicurezza e multi-tenant, configurazione ambiente
    - **Lab 04-06: Costruzione del Server MCP** - Design database e schema, implementazione server MCP, sviluppo strumenti  
    - **Lab 07-09: Funzionalità Avanzate** - Integrazione ricerca semantica, testing & debugging, integrazione VS Code
    - **Lab 10-12: Produzione & Best Practice** - Strategie di distribuzione, monitoraggio & osservabilità, best practice & ottimizzazione
  - **Tecnologie Enterprise**: Framework FastMCP, PostgreSQL con pgvector, embedding Azure OpenAI, Azure Container Apps, Application Insights
  - **Funzionalità Avanzate**: Row Level Security (RLS), ricerca semantica, accesso multi-tenant ai dati, embedding vettoriali, monitoraggio in tempo reale

#### Standardizzazione della Terminologia - Conversione Modulo in Lab
- **Aggiornamento Completo della Documentazione**: Tutti i file README in 11-MCPServerHandsOnLabs aggiornati per usare "Lab" invece di "Modulo"
  - **Intestazioni Sezioni**: "What This Module Covers" modificato in "What This Lab Covers" in tutti e 13 i lab
  - **Descrizione Contenuti**: "This module provides..." cambiato in "This lab provides..." in tutta la documentazione
  - **Obiettivi di Apprendimento**: "By the end of this module..." aggiornato a "By the end of this lab..."
  - **Link di Navigazione**: Tutti i riferimenti "Module XX:" convertiti in "Lab XX:" nei riferimenti incrociati e navigazione
  - **Tracciamento del Completamento**: "After completing this module..." aggiornato in "After completing this lab..."
  - **Riferimenti Tecnici Preservati**: Mantenuti riferimenti a moduli Python nei file di configurazione (es. `"module": "mcp_server.main"`)

#### Miglioramento della Guida allo Studio (study_guide.md)
- **Mappa Visiva del Curriculum**: Aggiunta sezione "11. Database Integration Labs" con visualizzazione completa della struttura dei lab
- **Struttura Repository**: Aggiornata da dieci a undici sezioni principali con dettagli su 11-MCPServerHandsOnLabs
- **Indicazioni Percorso di Apprendimento**: Migliorata la navigazione per coprire le sezioni 00-11
- **Copertura Tecnologica**: Nuove aggiunte su FastMCP, PostgreSQL, integrazione servizi Azure
- **Risultati di Apprendimento**: Enfasi su sviluppo server pronti per produzione, pattern di integrazione database e sicurezza enterprise

#### Miglioramento Struttura README Principale
- **Terminologia Basata su Lab**: Aggiornato README.md principale in 11-MCPServerHandsOnLabs per usare coerentemente la struttura "Lab"
- **Organizzazione del Percorso di Apprendimento**: Progressione chiara dai concetti base alle implementazioni avanzate fino al deploy in produzione
- **Focus sul Mondo Reale**: Enfasi su apprendimento pratico con pattern e tecnologie di livello enterprise

### Miglioramenti Qualità e Coerenza della Documentazione
- **Enfasi sul Learning by Doing**: Rinforzata l’approccio pratico basato su lab in tutta la documentazione
- **Focus su Pattern Enterprise**: Evidenziate implementazioni pronte per la produzione e considerazioni di sicurezza aziendale
- **Integrazione Tecnologica**: Copertura completa di servizi Azure moderni e pattern di integrazione AI
- **Progressione di Apprendimento**: Percorso chiaro e strutturato dai concetti base fino al deploy in produzione

## 26 Settembre 2025

### Miglioramento Case Study - Integrazione GitHub MCP Registry

#### Case Study (09-CaseStudy/) - Focus su Sviluppo Ecosistema
- **README.md**: Espansione importante con case study completo sul GitHub MCP Registry
  - **Case Study GitHub MCP Registry**: Nuovo approfondito studio che analizza il lancio del MCP Registry di GitHub nel settembre 2025
    - **Analisi del Problema**: Esame dettagliato della frammentazione nella scoperta e distribuzione dei server MCP
    - **Architettura della Soluzione**: Approccio centralizzato di registry GitHub con installazione one-click su VS Code
    - **Impatto sul Business**: Miglioramenti misurabili in onboarding e produttività degli sviluppatori
    - **Valore Strategico**: Focus su deployment modulare degli agenti e interoperabilità cross-tool
    - **Sviluppo Ecosistema**: Posizionamento come piattaforma fondamentale per integrazione agentica
  - **Struttura Case Study Potenziata**: Aggiornati tutti e sette i case study con formato coerente e descrizioni complete
    - Azure AI Travel Agents: enfasi su orchestrazione multi-agente
    - Azure DevOps Integration: focus su automazione workflow
    - Real-Time Documentation Retrieval: implementazione client console Python
    - Interactive Study Plan Generator: app conversazionale Chainlit
    - In-Editor Documentation: integrazione VS Code e GitHub Copilot
    - Azure API Management: pattern di integrazione API enterprise
    - GitHub MCP Registry: sviluppo ecosistema e piattaforma comunitaria
  - **Conclusione Esaustiva**: Sezione conclusiva riscritta evidenziando sette case study che coprono molteplici dimensioni di implementazione MCP
    - Integrazione enterprise, orchestrazione multi-agente, produttività sviluppatori
    - Sviluppo ecosistema, applicazioni educative categorizzate
    - Approfondimenti su pattern architetturali, strategie di implementazione e best practice
    - Enfasi su MCP come protocollo maturo e pronto per la produzione

#### Aggiornamenti Guida allo Studio (study_guide.md)
- **Mappa Visiva del Curriculum**: Mappa mentale aggiornata per includere GitHub MCP Registry nella sezione Case Studies
- **Descrizione Case Study**: Arricchita da descrizioni generiche a dettagliate per i sette case study completi
- **Struttura Repository**: Sezione 10 aggiornata per riflettere la copertura completa dei case study con dettagli di implementazione specifici
- **Integrazione Changelog**: Entry del 26 Settembre 2025 che documenta l’aggiunta del GitHub MCP Registry e i miglioramenti del case study
- **Aggiornamento Date**: Footer temporale aggiornato con la revisione più recente (26 Settembre 2025)

### Miglioramenti Qualità Documentazione
- **Coerenza Incrementata**: Formattazione e struttura standardizzate in tutti e sette i case study
- **Copertura Completa**: Case study che ora coprono scenari enterprise, produttività sviluppatori e sviluppo ecosistema
- **Posizionamento Strategico**: Maggiore enfasi su MCP come piattaforma fondamentale per il deployment di sistemi agentici
- **Integrazione Risorse**: Aggiornati i riferimenti aggiuntivi per includere il link al GitHub MCP Registry

## 15 Settembre 2025

### Espansione Argomenti Avanzati - Trasporti Personalizzati & Ingegneria del Contesto

#### Trasporti Personalizzati MCP (05-AdvancedTopics/mcp-transport/) - Guida Completa a Implementazioni Avanzate
- **README.md**: Guida completa all’implementazione di meccanismi di trasporto MCP personalizzati
  - **Trasporto Azure Event Grid**: Implementazione serverless evento-driven
    - Esempi in C#, TypeScript e Python con integrazione Azure Functions
    - Pattern di architettura evento-driven per soluzioni MCP scalabili
    - Ricevitori webhook e gestione push dei messaggi
  - **Trasporto Azure Event Hubs**: Implementazione streaming ad alta velocità
    - Capacità di streaming in tempo reale per scenari a bassa latenza
    - Strategie di partizionamento e gestione checkpoint
    - Batch di messaggi e ottimizzazione performance
  - **Pattern di Integrazione Enterprise**: Esempi architetturali pronti per la produzione
    - Elaborazione MCP distribuita su più Azure Functions
    - Architetture ibride che combinano più tipi di trasporto
    - Strategie di durabilità, affidabilità e gestione errori dei messaggi
  - **Sicurezza & Monitoraggio**: Integrazione Azure Key Vault e pattern di osservabilità
    - Autenticazione managed identity e accesso a privilegi minimi
    - Telemetria Application Insights e monitoraggio delle performance
    - Circuit breaker e pattern di tolleranza ai guasti
  - **Framework di Testing**: Strategie complete di testing per trasporti personalizzati
    - Unit test con test double e mocking framework
    - Integration test con Azure Test Containers
    - Considerazioni su performance e load testing

#### Ingegneria del Contesto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina AI Emergente
- **README.md**: Esplorazione approfondita dell’ingegneria del contesto come campo emergente
  - **Principi Fondamentali**: Condivisione completa del contesto, awareness decisioni azione, e gestione della finestra di contesto
  - **Allineamento con MCP Protocol**: Come il design MCP affronta le sfide dell’ingegneria del contesto
    - Limitazioni della finestra di contesto e strategie di caricamento progressivo
    - Determinazione della rilevanza e recupero dinamico del contesto
    - Gestione multi-modale del contesto e considerazioni di sicurezza
  - **Approcci di Implementazione**: Architetture single-threaded vs multi-agente
    - Tecniche di suddivisione e prioritizzazione del contesto
    - Caricamento progressivo e strategie di compressione del contesto
    - Approcci a strati e ottimizzazione del recupero del contesto
  - **Framework di Misurazione**: Metriche emergenti per valutare l’efficacia del contesto
    - Efficienza input, performance, qualità e esperienza utente
    - Approcci sperimentali per l’ottimizzazione del contesto
    - Analisi dei fallimenti e metodologie di miglioramento

#### Aggiornamenti nella Navigazione del Curriculum (README.md)
- **Struttura Moduli Potenziata**: Tabella del curriculum aggiornata per includere i nuovi argomenti avanzati
  - Aggiunte voci Ingegneria del Contesto (5.14) e Trasporti Personalizzati (5.15)
  - Formattazione e link di navigazione coerenti in tutti i moduli
  - Descrizioni aggiornate per riflettere l’attuale ambito dei contenuti

### Miglioramenti Struttura delle Cartelle
- **Standardizzazione dei Nomi**: Rinominato "mcp transport" in "mcp-transport" per coerenza con altre cartelle di argomenti avanzati
- **Organizzazione dei Contenuti**: Tutte le cartelle 05-AdvancedTopics ora seguono il pattern di denominazione coerente (mcp-[topic])

### Miglioramenti Qualità della Documentazione
- **Allineamento Specifica MCP**: Tutti i nuovi contenuti fanno riferimento alla Specifica MCP 2025-06-18
- **Esempi Multilingua**: Esempi completi di codice in C#, TypeScript e Python
- **Focus Enterprise**: Pattern pronti per la produzione e integrazione cloud Azure ovunque
- **Documentazione Visiva**: Diagrammi Mermaid per visualizzare architettura e flussi

## 18 Agosto 2025

### Aggiornamento Completo Documentazione - Standard MCP 2025-06-18

#### Best Practice di Sicurezza MCP (02-Security/) - Modernizzazione Totale
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Riscrittura completa allineata alla Specifica MCP 2025-06-18  
  - **Requisiti Obbligatori**: Aggiunti requisiti espliciti MUST/MUST NOT dalla specifica ufficiale con chiari indicatori visivi  
  - **12 Pratiche di Sicurezza Core**: Ristrutturate da lista di 15 punti a domini di sicurezza completi  
    - Sicurezza dei Token & Autenticazione con integrazione provider di identità esterni  
    - Gestione delle Sessioni & Sicurezza del Trasporto con requisiti crittografici  
    - Protezione dalle Minacce Specifiche AI con integrazione Microsoft Prompt Shields  
    - Controllo Accessi & Permessi con principio del minimo privilegio  
    - Sicurezza del Contenuto & Monitoraggio con integrazione Azure Content Safety  
    - Sicurezza della Catena di Fornitura con verifica completa dei componenti  
    - Sicurezza OAuth & Prevenzione Confused Deputy con implementazione PKCE  
    - Risposta agli Incidenti & Recupero con capacità automatizzate  
    - Conformità & Governance con allineamento regolatorio  
    - Controlli di Sicurezza Avanzati con architettura zero trust  
    - Integrazione Ecosistema Sicurezza Microsoft con soluzioni complete  
    - Evoluzione Continua della Sicurezza con pratiche adattive  
  - **Soluzioni di Sicurezza Microsoft**: Guida migliorata per l’integrazione di Prompt Shields, Azure Content Safety, Entra ID e GitHub Advanced Security  
  - **Risorse per l’Implementazione**: Collegamenti completi categorizzati in Documentazione Ufficiale MCP, Soluzioni Microsoft di Sicurezza, Standard di Sicurezza e Guide all’Implementazione  

#### Controlli di Sicurezza Avanzati (02-Security/) - Implementazione Enterprise  
- **MCP-SECURITY-CONTROLS-2025.md**: Revisione completa con framework di sicurezza a livello enterprise  
  - **9 Domini di Sicurezza Completi**: Espanso dai controlli base a dettagliato framework enterprise  
    - Autenticazione Avanzata & Autorizzazione con integrazione Microsoft Entra ID  
    - Sicurezza Token & Controlli Anti-Passthrough con validazione completa  
    - Controlli di Sicurezza delle Sessioni con prevenzione del dirottamento  
    - Controlli di Sicurezza Specifici AI con prevenzione iniezione prompt e avvelenamento strumenti  
    - Prevenzione attacchi Confused Deputy con sicurezza proxy OAuth  
    - Sicurezza Esecuzione Strumenti con sandboxing e isolamento  
    - Controlli Sicurezza Catena di Fornitura con verifica dipendenze  
    - Controlli Monitoraggio & Rilevamento con integrazione SIEM  
    - Risposta agli Incidenti & Recupero con capacità automatizzate  
  - **Esempi di Implementazione**: Aggiunti blocchi di configurazione YAML dettagliati ed esempi di codice  
  - **Integrazione Soluzioni Microsoft**: Copertura completa dei servizi di sicurezza Azure, GitHub Advanced Security e gestione identità enterprise  

#### Sicurezza Argomenti Avanzati (05-AdvancedTopics/mcp-security/) - Implementazione Pronta per la Produzione  
- **README.md**: Riscrittura completa per implementazione sicurezza enterprise  
  - **Allineamento Specifica Corrente**: Aggiornato alla Specifica MCP 2025-06-18 con requisiti di sicurezza obbligatori  
  - **Autenticazione Avanzata**: Integrazione Microsoft Entra ID con esempi completi in .NET e Java Spring Security  
  - **Integrazione Sicurezza AI**: Implementazione Microsoft Prompt Shields e Azure Content Safety con esempi Python dettagliati  
  - **Mitigazione Avanzata delle Minacce**: Esempi completi di implementazione per  
    - Prevenzione attacchi Confused Deputy con PKCE e validazione consenso utente  
    - Prevenzione Passthrough Token con validazione audience e gestione sicura token  
    - Prevenzione dirottamento Sessione con binding crittografico e analisi comportamentale  
  - **Integrazione Sicurezza Enterprise**: Monitoraggio Azure Application Insights, pipeline rilevamento minacce e sicurezza catena di fornitura  
  - **Checklist di Implementazione**: Controlli di sicurezza chiaramente separati in obbligatori vs raccomandati con benefici ecosistema sicurezza Microsoft  

### Qualità della Documentazione & Allineamento Standard  
- **Riferimenti Specifica**: Aggiornati tutti i riferimenti alla Specifica MCP 2025-06-18  
- **Ecosistema Sicurezza Microsoft**: Guida per l’integrazione migliorata in tutta la documentazione sicurezza  
- **Implementazione Pratica**: Aggiunti esempi di codice dettagliati in .NET, Java e Python con pattern enterprise  
- **Organizzazione Risorse**: Categorizzazione completa di documentazione ufficiale, standard di sicurezza e guide di implementazione  
- **Indicatori Visivi**: Segnalazione chiara di requisiti obbligatori vs pratiche raccomandate  

#### Concetti Base (01-CoreConcepts/) - Modernizzazione Completa  
- **Aggiornamento Versione Protocollo**: Aggiornato al riferimento della Specifica MCP 2025-06-18 con versione basata su data (formato YYYY-MM-DD)  
- **Raffinamento Architettura**: Descrizioni migliorate di Hosts, Client e Server per riflettere pattern attuali MCP  
  - Hosts ora chiaramente definiti come applicazioni AI che coordinano molteplici connessioni client MCP  
  - Client descritti come connettori di protocollo che mantengono relazioni uno a uno col server  
  - Server migliorati con scenari di deployment locale vs remoto  
- **Ristrutturazione Primitive**: Revisione completa delle primitive server e client  
  - Primitive Server: Risorse (fonti dati), Prompt (template), Strumenti (funzioni eseguibili) con spiegazioni ed esempi dettagliati  
  - Primitive Client: Campionamento (completamenti LLM), Elicitazione (input utente), Logging (debug/monitoraggio)  
  - Aggiornate con pattern metodi discovery (`*/list`), recupero (`*/get`) ed esecuzione (`*/call`) correnti  
- **Architettura Protocollo**: Introdotto modello architetturale a due livelli  
  - Livello Dati: Fondazione JSON-RPC 2.0 con gestione lifecycle e primitive  
  - Livello Trasporto: STDIO (locale) e HTTP Streamable con SSE (trasporto remoto)  
- **Framework di Sicurezza**: Principi di sicurezza completi incluse esplicita autorizzazione utente, protezione della privacy dati, sicurezza esecuzione strumenti e sicurezza livello trasporto  
- **Pattern di Comunicazione**: Aggiornate le message protocol per mostrare flussi di inizializzazione, discovery, esecuzione e notifica  
- **Esempi di Codice**: Aggiornati esempi multi-lingua (.NET, Java, Python, JavaScript) per riflettere pattern attuali SDK MCP  

#### Sicurezza (02-Security/) - Revisione Completa della Sicurezza  
- **Allineamento Standard**: Pieno allineamento ai requisiti sicurezza Specifica MCP 2025-06-18  
- **Evoluzione Autenticazione**: Documentata evoluzione da server OAuth custom a delega provider identità esterni (Microsoft Entra ID)  
- **Analisi Minacce Specifiche AI**: Copertura migliorata dei moderni vettori di attacco AI  
  - Scenari dettagliati di attacchi iniezione prompt con esempi reali  
  - Meccanismi di avvelenamento strumenti e attacchi "rug pull"  
  - Avvelenamento contesto finestra e attacchi di confusione modello  
- **Soluzioni Sicurezza AI Microsoft**: Copertura completa ecosistema sicurezza Microsoft  
  - AI Prompt Shields con rilevamento avanzato, spotlighting e tecniche delimitatori  
  - Pattern integrazione Azure Content Safety  
  - GitHub Advanced Security per protezione catena di fornitura  
- **Mitigazione Minacce Avanzate**: Controlli sicurezza dettagliati per  
  - Dirottamento sessione con scenari attacco MCP specifici e requisiti crittografici session ID  
  - Problemi Confused Deputy in scenari proxy MCP con requisiti di consenso esplicito  
  - Vulnerabilità passthrough token con controlli validazione obbligatori  
- **Sicurezza Catena di Fornitura**: Estesa copertura supply chain AI inclusi modelli foundation, servizi embeddings, provider contesto e API terze parti  
- **Sicurezza Foundation**: Integrazione migliorata con pattern sicurezza enterprise inclusa architettura zero trust ed ecosistema sicurezza Microsoft  
- **Organizzazione Risorse**: Collegamenti completi categorizzati per tipo (Doc Ufficiali, Standard, Ricerca, Soluzioni Microsoft, Guide Implementazione)  

### Miglioramenti Qualità Documentazione  
- **Obiettivi di Apprendimento Strutturati**: Obiettivi di apprendimento migliorati con risultati specifici e azionabili  
- **Riferimenti Incrociati**: Aggiunti collegamenti tra argomenti sicurezza e concetti base correlati  
- **Informazioni Correnti**: Aggiornati tutti riferimenti date e link specifica agli standard correnti  
- **Linee Guida Implementazione**: Aggiunte indicazioni implementative specifiche e azionabili in entrambe le sezioni  

## 16 luglio 2025

### Miglioramenti README e Navigazione  
- Riprogettazione completa della navigazione curriculum in README.md  
- Sostituiti tag `<details>` con formato tabellare più accessibile  
- Creato opzioni layout alternative nella nuova cartella "alternative_layouts"  
- Aggiunti esempi di navigazione a schede, basata su card e stile fisarmonica  
- Aggiornata sezione struttura repository includendo tutti i file più recenti  
- Potenziata sezione "Come Usare Questo Curriculum" con raccomandazioni chiare  
- Aggiornati link specifica MCP ai URL corretti  
- Aggiunta sezione Ingegneria del Contesto (5.14) nella struttura curriculum  

### Aggiornamenti Guida di Studio  
- Guida di studio completamente rivista per allineamento alla struttura repository corrente  
- Aggiunte nuove sezioni per MCP Clients e Tools, e Server MCP Popolari  
- Aggiornata Mappa Visiva Curriculum per riflettere tutti gli argomenti accuratamente  
- Migliorate descrizioni degli Argomenti Avanzati per coprire tutte le aree specializzate  
- Aggiornata sezione Case Studies per riflettere esempi reali  
- Aggiunto questo changelog completo  

### Contributi Comunitari (06-CommunityContributions/)  
- Informazioni dettagliate aggiunte su server MCP per generazione immagini  
- Sezione completa sull’uso di Claude in VSCode  
- Istruzioni di configurazione e utilizzo client terminale Cline  
- Sezione client MCP aggiornata includendo tutte le opzioni client popolari  
- Esempi contributi migliorati con campioni di codice più accurati  

### Argomenti Avanzati (05-AdvancedTopics/)  
- Organizzate tutte le cartelle argomenti specializzati con naming coerente  
- Aggiunti materiali e esempi ingegneria del contesto  
- Documentazione integrazione agente Foundry  
- Documentazione integrazione sicurezza Entra ID migliorata  

## 11 giugno 2025

### Creazione Iniziale  
- Rilasciata prima versione del curriculum MCP per principianti  
- Creato struttura base per tutte le 10 sezioni principali  
- Implementata Mappa Visiva Curriculum per navigazione  
- Aggiunti progetti campione iniziali in vari linguaggi di programmazione  

### Getting Started (03-GettingStarted/)  
- Creati primi esempi implementazione server  
- Aggiunte linee guida sviluppo client  
- Incluse istruzioni integrazione client LLM  
- Aggiunta documentazione integrazione VS Code  
- Esempi server Server-Sent Events (SSE) implementati  

### Concetti Base (01-CoreConcepts/)  
- Aggiunta spiegazione dettagliata architettura client-server  
- Creata documentazione componenti chiave protocollo  
- Documentati pattern di messaggistica MCP  

## 23 maggio 2025

### Struttura Repository  
- Inizializzato repository con struttura cartelle base  
- Creati file README per ogni sezione principale  
- Impostata infrastruttura di traduzione  
- Aggiunti asset immagine e diagrammi  

### Documentazione  
- Creato README.md iniziale con panoramica curriculum  
- Aggiunti CODE_OF_CONDUCT.md e SECURITY.md  
- Impostato SUPPORT.md con linee guida per ottenere supporto  
- Creato struttura preliminare guida di studio  

## 15 aprile 2025

### Pianificazione e Framework  
- Pianificazione iniziale per curriculum MCP per principianti  
- Definiti obiettivi di apprendimento e pubblico target  
- Delineata struttura in 10 sezioni del curriculum  
- Sviluppato framework concettuale per esempi e case studies  
- Creati prototipi iniziali di esempio per concetti chiave

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->