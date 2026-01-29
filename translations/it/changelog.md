# Changelog: Curriculum MCP per Principianti

Questo documento serve come registro di tutte le modifiche significative apportate al curriculum Model Context Protocol (MCP) per Principianti. Le modifiche sono documentate in ordine cronologico inverso (prime le più recenti).

## 18 dicembre 2025

### Aggiornamento Documentazione di Sicurezza - Specifica MCP 2025-11-25

#### Best Practice di Sicurezza MCP (02-Security/mcp-best-practices.md) - Aggiornamento Versione Specifica
- **Aggiornamento Versione Protocollo**: Aggiornato per fare riferimento all'ultima Specifica MCP 2025-11-25 (rilasciata il 25 novembre 2025)
  - Aggiornati tutti i riferimenti alla versione della specifica da 2025-06-18 a 2025-11-25
  - Aggiornate le date dei documenti da 18 agosto 2025 a 18 dicembre 2025
  - Verificati tutti gli URL delle specifiche puntino alla documentazione corrente
- **Validazione Contenuti**: Validazione completa delle best practice di sicurezza rispetto agli standard più recenti
  - **Soluzioni di Sicurezza Microsoft**: Verificata la terminologia e i link correnti per Prompt Shields (precedentemente "rilevamento rischio Jailbreak"), Azure Content Safety, Microsoft Entra ID e Azure Key Vault
  - **Sicurezza OAuth 2.1**: Confermata l'allineamento con le ultime best practice di sicurezza OAuth
  - **Standard OWASP**: Validati i riferimenti OWASP Top 10 per LLM rimangono aggiornati
  - **Servizi Azure**: Verificati tutti i link alla documentazione Microsoft Azure e le best practice
- **Allineamento agli Standard**: Tutti gli standard di sicurezza citati confermati aggiornati
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Best Practice di Sicurezza OAuth 2.1
  - Framework di sicurezza e conformità Azure
- **Risorse di Implementazione**: Verificati tutti i link e le risorse delle guide di implementazione
  - Pattern di autenticazione Azure API Management
  - Guide di integrazione Microsoft Entra ID
  - Gestione segreti Azure Key Vault
  - Pipeline DevSecOps e soluzioni di monitoraggio

### Assicurazione Qualità Documentazione
- **Conformità Specifica**: Garantito che tutti i requisiti di sicurezza MCP obbligatori (MUST/MUST NOT) siano allineati con l'ultima specifica
- **Aggiornamento Risorse**: Verificati tutti i link esterni alla documentazione Microsoft, standard di sicurezza e guide di implementazione
- **Copertura Best Practice**: Confermata copertura completa di autenticazione, autorizzazione, minacce specifiche AI, sicurezza della supply chain e pattern enterprise

## 6 ottobre 2025

### Espansione Sezione Introduzione – Uso Avanzato Server & Autenticazione Semplice

#### Uso Avanzato Server (03-GettingStarted/10-advanced)
- **Nuovo Capitolo Aggiunto**: Introdotta guida completa all'uso avanzato del server MCP, coprendo architetture server regolari e a basso livello.
  - **Server Regolare vs. Basso Livello**: Confronto dettagliato ed esempi di codice in Python e TypeScript per entrambi gli approcci.
  - **Design Basato su Handler**: Spiegazione della gestione di tool/risorse/prompt basata su handler per implementazioni server scalabili e flessibili.
  - **Pattern Pratici**: Scenari reali in cui i pattern server a basso livello sono utili per funzionalità avanzate e architettura.

#### Autenticazione Semplice (03-GettingStarted/11-simple-auth)
- **Nuovo Capitolo Aggiunto**: Guida passo-passo per implementare autenticazione semplice nei server MCP.
  - **Concetti di Auth**: Spiegazione chiara di autenticazione vs autorizzazione e gestione delle credenziali.
  - **Implementazione Basic Auth**: Pattern di autenticazione middleware in Python (Starlette) e TypeScript (Express), con esempi di codice.
  - **Progressione verso Sicurezza Avanzata**: Indicazioni per iniziare con autenticazione semplice e progredire verso OAuth 2.1 e RBAC, con riferimenti ai moduli di sicurezza avanzata.

Queste aggiunte forniscono indicazioni pratiche e operative per costruire implementazioni server MCP più robuste, sicure e flessibili, collegando concetti fondamentali a pattern avanzati di produzione.

## 29 settembre 2025

### Laboratori di Integrazione Database Server MCP - Percorso di Apprendimento Pratico Completo

#### 11-MCPServerHandsOnLabs - Nuovo Curriculum Completo di Integrazione Database
- **Percorso di Apprendimento Completo di 13 Laboratori**: Aggiunto curriculum pratico completo per costruire server MCP pronti per la produzione con integrazione database PostgreSQL
  - **Implementazione Reale**: Caso d'uso analitico Zava Retail che dimostra pattern di livello enterprise
  - **Progressione di Apprendimento Strutturata**:
    - **Laboratori 00-03: Fondamenti** - Introduzione, Architettura Core, Sicurezza & Multi-Tenancy, Setup Ambiente
    - **Laboratori 04-06: Costruzione Server MCP** - Design & Schema Database, Implementazione Server MCP, Sviluppo Tool  
    - **Laboratori 07-09: Funzionalità Avanzate** - Integrazione Ricerca Semantica, Testing & Debugging, Integrazione VS Code
    - **Laboratori 10-12: Produzione & Best Practice** - Strategie di Deployment, Monitoraggio & Osservabilità, Best Practice & Ottimizzazione
  - **Tecnologie Enterprise**: Framework FastMCP, PostgreSQL con pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Funzionalità Avanzate**: Row Level Security (RLS), ricerca semantica, accesso dati multi-tenant, vettori embedding, monitoraggio in tempo reale

#### Standardizzazione Terminologia - Conversione Modulo a Laboratorio
- **Aggiornamento Documentazione Completo**: Aggiornati sistematicamente tutti i file README in 11-MCPServerHandsOnLabs per usare la terminologia "Lab" invece di "Module"
  - **Intestazioni Sezioni**: Aggiornato "What This Module Covers" in "What This Lab Covers" in tutti i 13 laboratori
  - **Descrizione Contenuti**: Cambiato "This module provides..." in "This lab provides..." in tutta la documentazione
  - **Obiettivi di Apprendimento**: Aggiornato "By the end of this module..." in "By the end of this lab..."
  - **Link di Navigazione**: Convertiti tutti i riferimenti "Module XX:" in "Lab XX:" nelle cross-referenze e navigazione
  - **Tracciamento Completamento**: Aggiornato "After completing this module..." in "After completing this lab..."
  - **Riferimenti Tecnici Preservati**: Mantenuti riferimenti a moduli Python nei file di configurazione (es. `"module": "mcp_server.main"`)

#### Miglioramento Guida di Studio (study_guide.md)
- **Mappa Visiva del Curriculum**: Aggiunta nuova sezione "11. Database Integration Labs" con visualizzazione completa della struttura dei laboratori
- **Struttura Repository**: Aggiornata da dieci a undici sezioni principali con descrizione dettagliata di 11-MCPServerHandsOnLabs
- **Indicazioni Percorso di Apprendimento**: Migliorate istruzioni di navigazione per coprire sezioni 00-11
- **Copertura Tecnologica**: Aggiunti dettagli su FastMCP, PostgreSQL, integrazione servizi Azure
- **Risultati di Apprendimento**: Enfasi su sviluppo server pronti per la produzione, pattern di integrazione database e sicurezza enterprise

#### Miglioramento Struttura README Principale
- **Terminologia Basata su Laboratori**: Aggiornato README.md principale in 11-MCPServerHandsOnLabs per usare coerentemente la struttura "Lab"
- **Organizzazione Percorso di Apprendimento**: Progressione chiara da concetti fondamentali a implementazione avanzata fino al deployment in produzione
- **Focus sul Mondo Reale**: Enfasi su apprendimento pratico con pattern e tecnologie di livello enterprise

### Miglioramenti Qualità & Coerenza Documentazione
- **Enfasi su Apprendimento Pratico**: Rinforzato approccio pratico basato su laboratori in tutta la documentazione
- **Focus su Pattern Enterprise**: Evidenziate implementazioni pronte per la produzione e considerazioni di sicurezza enterprise
- **Integrazione Tecnologica**: Copertura completa dei moderni servizi Azure e pattern di integrazione AI
- **Progressione di Apprendimento**: Percorso chiaro e strutturato da concetti base a deployment in produzione

## 26 settembre 2025

### Miglioramento Case Study - Integrazione GitHub MCP Registry

#### Case Study (09-CaseStudy/) - Focus Sviluppo Ecosistema
- **README.md**: Ampia espansione con case study completo sul GitHub MCP Registry
  - **Case Study GitHub MCP Registry**: Nuovo case study completo che esamina il lancio del GitHub MCP Registry a settembre 2025
    - **Analisi Problema**: Esame dettagliato della frammentazione nella scoperta e deployment dei server MCP
    - **Architettura Soluzione**: Approccio centralizzato del registry GitHub con installazione VS Code con un clic
    - **Impatto Business**: Miglioramenti misurabili nell'onboarding e produttività degli sviluppatori
    - **Valore Strategico**: Focus sul deployment modulare degli agenti e interoperabilità cross-tool
    - **Sviluppo Ecosistema**: Posizionamento come piattaforma fondamentale per integrazione agentica
  - **Struttura Case Study Migliorata**: Aggiornati tutti e sette i case study con formattazione coerente e descrizioni complete
    - Azure AI Travel Agents: Enfasi su orchestrazione multi-agente
    - Integrazione Azure DevOps: Focus su automazione workflow
    - Recupero Documentazione in Tempo Reale: Implementazione client console Python
    - Generatore Piano di Studio Interattivo: Web app conversazionale Chainlit
    - Documentazione In-Editor: Integrazione VS Code e GitHub Copilot
    - Azure API Management: Pattern di integrazione API enterprise
    - GitHub MCP Registry: Sviluppo ecosistema e piattaforma comunitaria
  - **Conclusione Completa**: Sezione conclusiva riscritta evidenziando sette case study che coprono molteplici dimensioni di implementazione MCP
    - Integrazione Enterprise, Orchestrazione Multi-Agente, Produttività Sviluppatori
    - Sviluppo Ecosistema, Applicazioni Educative categorizzate
    - Approfondimenti su pattern architetturali, strategie di implementazione e best practice
    - Enfasi su MCP come protocollo maturo e pronto per la produzione

#### Aggiornamenti Guida di Studio (study_guide.md)
- **Mappa Visiva Curriculum**: Aggiornata mindmap per includere GitHub MCP Registry nella sezione Case Studies
- **Descrizione Case Study**: Migliorata da descrizioni generiche a dettagliata suddivisione di sette case study completi
- **Struttura Repository**: Aggiornata sezione 10 per riflettere copertura completa dei case study con dettagli specifici di implementazione
- **Integrazione Changelog**: Aggiunta voce 26 settembre 2025 documentante l'aggiunta GitHub MCP Registry e miglioramenti case study
- **Aggiornamento Date**: Aggiornato timestamp footer per riflettere ultima revisione (26 settembre 2025)

### Miglioramenti Qualità Documentazione
- **Miglioramento Coerenza**: Standardizzata formattazione e struttura case study in tutti e sette gli esempi
- **Copertura Completa**: Case study ora coprono scenari enterprise, produttività sviluppatori e sviluppo ecosistema
- **Posizionamento Strategico**: Maggiore focus su MCP come piattaforma fondamentale per deployment di sistemi agentici
- **Integrazione Risorse**: Aggiornate risorse aggiuntive per includere link GitHub MCP Registry

## 15 settembre 2025

### Espansione Argomenti Avanzati - Trasporti Personalizzati & Context Engineering

#### Trasporti Personalizzati MCP (05-AdvancedTopics/mcp-transport/) - Nuova Guida di Implementazione Avanzata
- **README.md**: Guida completa all'implementazione di meccanismi di trasporto MCP personalizzati
  - **Trasporto Azure Event Grid**: Implementazione serverless di trasporto event-driven
    - Esempi in C#, TypeScript e Python con integrazione Azure Functions
    - Pattern architetturali event-driven per soluzioni MCP scalabili
    - Ricevitori webhook e gestione messaggi push
  - **Trasporto Azure Event Hubs**: Implementazione trasporto streaming ad alta velocità
    - Capacità streaming in tempo reale per scenari a bassa latenza
    - Strategie di partizionamento e gestione checkpoint
    - Batch di messaggi e ottimizzazione prestazioni
  - **Pattern Integrazione Enterprise**: Esempi architetturali pronti per la produzione
    - Elaborazione MCP distribuita su più Azure Functions
    - Architetture ibride di trasporto combinando più tipi di trasporto
    - Strategie di durabilità, affidabilità e gestione errori messaggi
  - **Sicurezza & Monitoraggio**: Integrazione Azure Key Vault e pattern di osservabilità
    - Autenticazione con identità gestita e accesso a privilegi minimi
    - Telemetria Application Insights e monitoraggio prestazioni
    - Circuit breaker e pattern di tolleranza ai guasti
  - **Framework di Testing**: Strategie di test complete per trasporti personalizzati
    - Test unitari con test doubles e mocking framework
    - Test di integrazione con Azure Test Containers
    - Considerazioni su test di performance e carico

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Disciplina AI Emergente
- **README.md**: Esplorazione completa del context engineering come campo emergente
  - **Principi Fondamentali**: Condivisione completa del contesto, consapevolezza decisionale azioni, gestione finestra contesto
  - **Allineamento Protocollo MCP**: Come il design MCP affronta le sfide del context engineering
    - Limitazioni finestra contesto e strategie di caricamento progressivo
    - Determinazione rilevanza e recupero dinamico del contesto
    - Gestione contesto multimodale e considerazioni di sicurezza
  - **Approcci di Implementazione**: Architetture single-threaded vs multi-agente
    - Tecniche di suddivisione e prioritizzazione del contesto
    - Caricamento progressivo e strategie di compressione del contesto
    - Approcci stratificati e ottimizzazione del recupero contesto
  - **Framework di Misurazione**: Metriche emergenti per valutazione efficacia contesto
    - Efficienza input, prestazioni, qualità e considerazioni esperienza utente
    - Approcci sperimentali all'ottimizzazione del contesto
    - Analisi dei fallimenti e metodologie di miglioramento

#### Aggiornamenti Navigazione Curriculum (README.md)
- **Struttura Moduli Migliorata**: Aggiornata tabella curriculum per includere nuovi argomenti avanzati
  - Aggiunti Context Engineering (5.14) e Custom Transport (5.15)
  - Formattazione coerente e link di navigazione in tutti i moduli
  - Aggiornate descrizioni per riflettere l'attuale ambito dei contenuti

### Miglioramenti Struttura Directory
- **Standardizzazione Nomi**: Rinominato "mcp transport" in "mcp-transport" per coerenza con altre cartelle argomenti avanzati
- **Organizzazione Contenuti**: Tutte le cartelle 05-AdvancedTopics ora seguono pattern di denominazione coerente (mcp-[topic])

### Miglioramenti Qualità Documentazione
- **Allineamento Specifica MCP**: Tutti i nuovi contenuti fanno riferimento alla Specifica MCP 2025-06-18
- **Esempi Multilingua**: Esempi di codice completi in C#, TypeScript e Python
- **Focus Enterprise**: Pattern pronti per la produzione e integrazione cloud Azure in tutto il materiale
- **Documentazione Visiva**: Diagrammi Mermaid per visualizzazione architettura e flussi

## 18 agosto 2025

### Aggiornamento Completo Documentazione - Standard MCP 2025-06-18

#### Best Practice di Sicurezza MCP (02-Security/) - Modernizzazione Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Riscrittura completa allineata con Specifica MCP 2025-06-18
  - **Requisiti Obbligatori**: Aggiunti requisiti espliciti MUST/MUST NOT dalla specifica ufficiale con chiari indicatori visivi  
  - **12 Pratiche di Sicurezza Core**: Ristrutturato da lista di 15 elementi a domini di sicurezza completi  
    - Sicurezza dei Token & Autenticazione con integrazione di provider di identità esterni  
    - Gestione della Sessione & Sicurezza del Trasporto con requisiti crittografici  
    - Protezione Specifica per AI con integrazione Microsoft Prompt Shields  
    - Controllo Accessi & Permessi con principio del minimo privilegio  
    - Sicurezza e Monitoraggio dei Contenuti con integrazione Azure Content Safety  
    - Sicurezza della Catena di Fornitura con verifica completa dei componenti  
    - Sicurezza OAuth & Prevenzione Confused Deputy con implementazione PKCE  
    - Risposta agli Incidenti & Recupero con capacità automatizzate  
    - Conformità & Governance con allineamento normativo  
    - Controlli di Sicurezza Avanzati con architettura zero trust  
    - Integrazione Ecosistema di Sicurezza Microsoft con soluzioni complete  
    - Evoluzione Continua della Sicurezza con pratiche adattive  
  - **Soluzioni di Sicurezza Microsoft**: Guida all’integrazione migliorata per Prompt Shields, Azure Content Safety, Entra ID e GitHub Advanced Security  
  - **Risorse per l’Implementazione**: Collegamenti risorse completi categorizzati in Documentazione Ufficiale MCP, Soluzioni di Sicurezza Microsoft, Standard di Sicurezza e Guide all’Implementazione  

#### Controlli di Sicurezza Avanzati (02-Security/) - Implementazione Enterprise  
- **MCP-SECURITY-CONTROLS-2025.md**: Revisione completa con framework di sicurezza di livello enterprise  
  - **9 Domini di Sicurezza Completi**: Espansi da controlli base a framework dettagliato enterprise  
    - Autenticazione & Autorizzazione Avanzate con integrazione Microsoft Entra ID  
    - Sicurezza dei Token & Controlli Anti-Passthrough con validazione completa  
    - Controlli di Sicurezza della Sessione con prevenzione di hijacking  
    - Controlli di Sicurezza Specifici per AI con prevenzione di prompt injection e avvelenamento strumenti  
    - Prevenzione Attacchi Confused Deputy con sicurezza proxy OAuth  
    - Sicurezza Esecuzione Strumenti con sandboxing e isolamento  
    - Controlli di Sicurezza della Catena di Fornitura con verifica delle dipendenze  
    - Controlli di Monitoraggio & Rilevamento con integrazione SIEM  
    - Risposta agli Incidenti & Recupero con capacità automatizzate  
  - **Esempi di Implementazione**: Aggiunti blocchi di configurazione YAML dettagliati ed esempi di codice  
  - **Integrazione Soluzioni Microsoft**: Copertura completa dei servizi di sicurezza Azure, GitHub Advanced Security e gestione identità enterprise  

#### Argomenti Avanzati di Sicurezza (05-AdvancedTopics/mcp-security/) - Implementazione Pronta per la Produzione  
- **README.md**: Riscrittura completa per implementazione di sicurezza enterprise  
  - **Allineamento alla Specifica Corrente**: Aggiornato alla Specifica MCP 2025-06-18 con requisiti di sicurezza obbligatori  
  - **Autenticazione Avanzata**: Integrazione Microsoft Entra ID con esempi completi in .NET e Java Spring Security  
  - **Integrazione Sicurezza AI**: Implementazione Microsoft Prompt Shields e Azure Content Safety con esempi dettagliati in Python  
  - **Mitigazione Minacce Avanzate**: Esempi completi di implementazione per  
    - Prevenzione Attacchi Confused Deputy con PKCE e validazione consenso utente  
    - Prevenzione Token Passthrough con validazione audience e gestione sicura token  
    - Prevenzione Hijacking Sessione con binding crittografico e analisi comportamentale  
  - **Integrazione Sicurezza Enterprise**: Monitoraggio Azure Application Insights, pipeline di rilevamento minacce e sicurezza catena di fornitura  
  - **Checklist di Implementazione**: Controlli di sicurezza obbligatori vs raccomandati con benefici dell’ecosistema di sicurezza Microsoft  

### Qualità della Documentazione & Allineamento agli Standard  
- **Riferimenti alla Specifica**: Aggiornati tutti i riferimenti alla Specifica MCP corrente 2025-06-18  
- **Ecosistema di Sicurezza Microsoft**: Guida all’integrazione migliorata in tutta la documentazione di sicurezza  
- **Implementazione Pratica**: Aggiunti esempi di codice dettagliati in .NET, Java e Python con pattern enterprise  
- **Organizzazione delle Risorse**: Categorizzazione completa di documentazione ufficiale, standard di sicurezza e guide all’implementazione  
- **Indicatori Visivi**: Marcatura chiara di requisiti obbligatori vs pratiche raccomandate  

#### Concetti Core (01-CoreConcepts/) - Modernizzazione Completa  
- **Aggiornamento Versione Protocollo**: Aggiornato a riferimento Specifica MCP corrente 2025-06-18 con versionamento basato su data (formato YYYY-MM-DD)  
- **Raffinamento Architettura**: Descrizioni migliorate di Host, Client e Server per riflettere pattern architetturali MCP attuali  
  - Host ora chiaramente definiti come applicazioni AI che coordinano molteplici connessioni client MCP  
  - Client descritti come connettori di protocollo che mantengono relazioni uno a uno con server  
  - Server migliorati con scenari di deployment locale vs remoto  
- **Ristrutturazione Primitive**: Revisione completa delle primitive server e client  
  - Primitive Server: Risorse (fonti dati), Prompt (template), Strumenti (funzioni eseguibili) con spiegazioni ed esempi dettagliati  
  - Primitive Client: Campionamento (completamenti LLM), Elicitazione (input utente), Logging (debugging/monitoraggio)  
  - Aggiornate con pattern attuali di metodi discovery (`*/list`), retrieval (`*/get`) ed esecuzione (`*/call`)  
- **Architettura Protocollo**: Introdotto modello architetturale a due livelli  
  - Livello Dati: Fondazione JSON-RPC 2.0 con gestione ciclo di vita e primitive  
  - Livello Trasporto: STDIO (locale) e HTTP Streamable con SSE (trasporto remoto)  
- **Framework di Sicurezza**: Principi di sicurezza completi inclusi consenso esplicito utente, protezione privacy dati, sicurezza esecuzione strumenti e sicurezza livello trasporto  
- **Pattern di Comunicazione**: Aggiornati messaggi protocollo per mostrare flussi di inizializzazione, discovery, esecuzione e notifica  
- **Esempi di Codice**: Aggiornati esempi multi-lingua (.NET, Java, Python, JavaScript) per riflettere pattern SDK MCP attuali  

#### Sicurezza (02-Security/) - Revisione Completa della Sicurezza  
- **Allineamento Standard**: Pieno allineamento ai requisiti di sicurezza della Specifica MCP 2025-06-18  
- **Evoluzione Autenticazione**: Documentata evoluzione da server OAuth custom a delega provider identità esterni (Microsoft Entra ID)  
- **Analisi Minacce Specifiche AI**: Copertura migliorata dei vettori di attacco AI moderni  
  - Scenari dettagliati di attacchi prompt injection con esempi reali  
  - Meccanismi di avvelenamento strumenti e pattern di attacchi "rug pull"  
  - Avvelenamento finestra contesto e attacchi di confusione modello  
- **Soluzioni Sicurezza AI Microsoft**: Copertura completa dell’ecosistema di sicurezza Microsoft  
  - AI Prompt Shields con rilevamento avanzato, spotlighting e tecniche delimitatori  
  - Pattern di integrazione Azure Content Safety  
  - GitHub Advanced Security per protezione catena di fornitura  
- **Mitigazione Minacce Avanzate**: Controlli di sicurezza dettagliati per  
  - Hijacking sessione con scenari attacco specifici MCP e requisiti crittografici ID sessione  
  - Problemi Confused Deputy in scenari proxy MCP con requisiti espliciti di consenso  
  - Vulnerabilità token passthrough con controlli di validazione obbligatori  
- **Sicurezza Catena di Fornitura**: Copertura estesa della catena di fornitura AI inclusi modelli foundation, servizi embedding, provider contesto e API di terze parti  
- **Sicurezza Foundation**: Integrazione migliorata con pattern di sicurezza enterprise inclusa architettura zero trust e ecosistema sicurezza Microsoft  
- **Organizzazione Risorse**: Collegamenti risorse completi categorizzati per tipo (Documenti Ufficiali, Standard, Ricerca, Soluzioni Microsoft, Guide Implementazione)  

### Miglioramenti Qualità Documentazione  
- **Obiettivi di Apprendimento Strutturati**: Obiettivi di apprendimento migliorati con risultati specifici e azionabili  
- **Riferimenti Incrociati**: Aggiunti link tra argomenti correlati di sicurezza e concetti core  
- **Informazioni Correnti**: Aggiornate tutte le date e link specifica agli standard correnti  
- **Guida all’Implementazione**: Aggiunte linee guida specifiche e azionabili in entrambe le sezioni  

## 16 Luglio 2025  

### Miglioramenti README e Navigazione  
- Navigazione curriculum completamente ridisegnata in README.md  
- Sostituiti tag `<details>` con formato tabellare più accessibile  
- Create opzioni di layout alternative nella nuova cartella "alternative_layouts"  
- Aggiunti esempi di navigazione a schede, a card e a fisarmonica  
- Aggiornata sezione struttura repository per includere tutti i file più recenti  
- Migliorata sezione "Come Usare Questo Curriculum" con raccomandazioni chiare  
- Aggiornati link specifica MCP per puntare agli URL corretti  
- Aggiunta sezione Context Engineering (5.14) alla struttura del curriculum  

### Aggiornamenti Guida di Studio  
- Guida di studio completamente rivista per allinearsi alla struttura repository corrente  
- Aggiunte nuove sezioni per MCP Clients e Tools, e MCP Servers popolari  
- Aggiornata Mappa Visuale del Curriculum per riflettere accuratamente tutti gli argomenti  
- Migliorate descrizioni degli Argomenti Avanzati per coprire tutte le aree specializzate  
- Aggiornata sezione Case Studies per riflettere esempi reali  
- Aggiunto questo changelog completo  

### Contributi della Comunità (06-CommunityContributions/)  
- Aggiunte informazioni dettagliate su server MCP per generazione immagini  
- Aggiunta sezione completa su utilizzo di Claude in VSCode  
- Aggiunte istruzioni setup e uso client terminale Cline  
- Aggiornata sezione client MCP per includere tutte le opzioni client popolari  
- Migliorati esempi di contributo con campioni di codice più accurati  

### Argomenti Avanzati (05-AdvancedTopics/)  
- Organizzate tutte le cartelle di argomenti specializzati con naming coerente  
- Aggiunti materiali ed esempi di context engineering  
- Aggiunta documentazione integrazione agente Foundry  
- Migliorata documentazione integrazione sicurezza Entra ID  

## 11 Giugno 2025  

### Creazione Iniziale  
- Rilasciata prima versione del curriculum MCP per principianti  
- Creata struttura base per tutte le 10 sezioni principali  
- Implementata Mappa Visuale del Curriculum per navigazione  
- Aggiunti progetti di esempio iniziali in più linguaggi di programmazione  

### Getting Started (03-GettingStarted/)  
- Creati primi esempi di implementazione server  
- Aggiunte linee guida per sviluppo client  
- Includere istruzioni integrazione client LLM  
- Aggiunta documentazione integrazione VS Code  
- Implementati esempi server Server-Sent Events (SSE)  

### Concetti Core (01-CoreConcepts/)  
- Aggiunta spiegazione dettagliata architettura client-server  
- Creata documentazione componenti chiave protocollo  
- Documentati pattern di messaggistica in MCP  

## 23 Maggio 2025  

### Struttura Repository  
- Inizializzato repository con struttura cartelle base  
- Creati file README per ogni sezione principale  
- Configurata infrastruttura traduzione  
- Aggiunte risorse immagini e diagrammi  

### Documentazione  
- Creato README.md iniziale con panoramica curriculum  
- Aggiunti CODE_OF_CONDUCT.md e SECURITY.md  
- Configurato SUPPORT.md con guida per assistenza  
- Creata struttura preliminare guida di studio  

## 15 Aprile 2025  

### Pianificazione e Framework  
- Pianificazione iniziale per curriculum MCP per principianti  
- Definiti obiettivi di apprendimento e pubblico target  
- Delineata struttura curriculum a 10 sezioni  
- Sviluppato framework concettuale per esempi e case study  
- Creati prototipi iniziali di esempi per concetti chiave  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->