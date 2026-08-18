# Registro delle modifiche: Curriculum MCP per Principianti

Questo documento funge da registro di tutte le modifiche significative apportate al curriculum Model Context Protocol (MCP) per Principianti. Le modifiche sono documentate in ordine cronologico inverso (prime le più recenti).

## 29 luglio 2026

### Nuovo Modulo 08 Companion: Sidecar di Affidabilità e Riprova Sicura

Aggiunta una lezione companion neutra rispetto al fornitore per gli strumenti MCP che creano effetti nel mondo reale,
in linea con la specifica definitiva `2026-07-28`.

- **Nuovo**: La [lezione companion sidecar di affidabilità][reliability-sidecar]
  usa una storia di ticket di supporto, due diagrammi Mermaid e un flusso
  decisionale per la riprova per spiegare chiavi di operazione stabili, ammissione duplicata atomica,
  riconciliazione, prove, e il confine dell'estensione Tasks.
- **Nuovo**: Un esercizio di iniezione di guasti in Python e SQLite della libreria standard
  usa archivi separati per operazioni e ticket per dimostrare una risposta persa
  dopo il commit di un effetto esterno. Sei test deterministici coprono duplicazione ingenua,
  recupero protetto da riavvio, conflitti di payload, risultati memorizzati nella cache,
  rivendicazioni attive, e ammissione duplicata concorrente.
- **Aggiornato**: Il Modulo 08 ora collega la lezione companion, identifica il
  modello di richiesta senza stato `2026-07-28` finale, distingue l'osservabilità OpenTelemetry
  dalla funzione di logging MCP deprecata e limita il suo esempio generico di riprova
  alle operazioni di sola lettura.
- **Opzionale**: La lezione mappa i suoi concetti portatili a una singola implementazione
  comunitaria taggata senza rendere il servizio ospitato o una chiamata di rete parte
  dell'esercizio.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 luglio 2026

### Nuova Lezione: Release Candidate della Specifica MCP 2026-07-28

Copertura aggiunta della prossima release candidate della specifica MCP `2026-07-28` (annunciata il 21 maggio 2026; rilascio finale previsto per il 28 luglio 2026), riassunta dal [post ufficiale di annuncio sul blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). La base del curriculum rimane la **Specificazione MCP 2025-11-25** fino a quando non sarà rilasciata la nuova versione, quindi questo è presentato come una guida prospettica piuttosto che una riscrittura delle lezioni esistenti.

- **Nuovo**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — una lezione completa che copre il nucleo del protocollo senza stato (rimozione della stretta di mano `initialize` e `Mcp-Session-Id`), i nuovi header di routing `Mcp-Method`/`Mcp-Name`, i metadati di caching `ttlMs`/`cacheScope`, il W3C Trace Context in `_meta`, il framework formale Extensions (app MCP e la nuova estensione Tasks), sei SEP di rafforzamento dell'autorizzazione, la deprecazione di Roots/Sampling/Logging e il passaggio completo allo JSON Schema 2020-12 per gli schemi degli strumenti.
- **Aggiornato** con collegamenti prospettici alla nuova lezione:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): nota sulla versione del protocollo, sezioni Sampling/Roots/Logging/Tasks e "Cosa c'è dopo"
  - [02-Security/README.md](./02-Security/README.md): raccolta di rafforzamento autorizzazione
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): segnalazione trasporto senza stato
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): segnalazione deprecazione Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): segnalazione deprecazione Logging ed estensione Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): segnalazione routing senza stato/sessione
  - [README.md](./README.md): nota "Guardando avanti" nella sezione specifica e una nuova voce `1.1` nella tabella del modulo curriculare
  - [study_guide.md](./study_guide.md): punto prospettico sotto la panoramica Concetti Chiave e una nota aggiuntiva datata
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): segnalazione sulla mappa di trasporto `mcp-session-id` prima del modello di richiesta senza stato
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): segnalazione panoramica modulo su deprecazioni Root Contexts/Sampling e sull’estensione Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): segnalazione rafforzamento autorizzazione

## 24 giugno 2026

### Nuova Lezione: Uso di MCP nell'app Copilot

- [Sezione Tooling](./12-tooling/README.md) Aggiunta sezione tooling.
- [MCP nell'app Copilot](./12-tooling/01-copilot-app/README.md)

## 16 giugno 2026

### Allineamento Specifica MCP & Validazione Esempi

Validato il curriculum con l'attuale **Specificazione MCP 2025-11-25** e gli ultimi SDK ufficiali, quindi corrette le restanti referenze obsolete della specifica e confermato che gli esempi core si compilano e funzionano ancora.

#### Correzioni Versione Specifica (2025-06-18 / 2025-03-26 → 2025-11-25)

Aggiornato il contenuto in inglese dove affermava ancora che una revisione della spec più vecchia era lo standard *corrente/ultimo*, e ricollegati i link ai percorsi canonici della specifica `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Aggiornato il banner "Current Standard", l'introduzione, l'intestazione dei principi core di sicurezza, l'intestazione dei requisiti obbligatori, la sezione Microsoft Entra ID, i link a Riferimenti & Risorse e l'avviso finale sulla sicurezza (8 riferimenti) al 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Aggiornato il link alla risorsa aggiuntiva della specifica e il banner "Current Standard" al 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Sostituito il link obsoleto `2025-03-26` di sicurezza e fiducia con la pagina delle migliori pratiche di sicurezza attuale 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Aggiornato il link ufficiale della documentazione sampling al 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Aggiornato il riferimento alla "specifica MCP corrente" al tempo presente e il link alla Specifica Risorse Aggiuntive al 25-11-2025 (note storiche sulla deprecazione SSE lasciate intatte per precisione)

#### Validazione del campione contro gli SDK attuali

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` ha risolto `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` superato senza errori di tipo — le API esistenti `McpServer`/`StdioServerTransport` rimangono valide
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validato in un `.venv` isolato con `mcp[cli]` (1.27.2); `py_compile` superato e `FastMCP.list_tools()` ha correttamente restituito gli strumenti `add` e `subtract`
- Confermato che tutte le versioni dei campioni `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) si risolvono correttamente all’attuale `1.29.0` senza cambiamenti API incompatibili

#### Allineamento delle dipendenze (chiusura dei gap di versione)

Aggiornate le versioni obsolete degli SDK in modo che ogni esempio segua la release MCP corrente, in linea con la convenzione del repository:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Aggiornato `@modelcontextprotocol/sdk` da `^1.8.0` → `>=1.26.0` e modificata la descrizione del pacchetto obsoleta `"aggiornato per MCP 2025-06-18"` in `"allineato alla Specifica MCP 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** e **lab4/code/github_mcp_server/pyproject.toml**: Aggiornato il vincolo preciso `mcp==1.23.0` → `mcp>=1.26.0`; rigenerati entrambi i file `uv.lock` (`uv lock`) per risolvere i lockfile all’attuale `mcp 1.27.2` e mantenerli sincronizzati con i manifesti

#### Analisi delle lacune nel curriculum — Copertura delle funzionalità della specifica più recente

Verificato che il curriculum copra già tutte le primitive introdotte/espanse in MCP 2025-11-25, quindi non rimangono lacune nei contenuti:
- **Sampling**: Lezione 03-GettingStarted/14-sampling più 05-AdvancedTopics/mcp-sampling
- **Elicitation (incl. modalità URL)**: Documentato in 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Documentato in 00-Introduction, 01-CoreConcepts e 05-AdvancedTopics/mcp-root-contexts
- **Tasks (sperimentale, operazioni di lunga durata)**: Documentato in 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features
- **Annotazioni degli strumenti** (`readOnlyHint` / `destructiveHint`): Documentato in 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features

### Rafforzamento della sicurezza e risoluzione delle vulnerabilità delle dipendenze

Effettuata una revisione completa della sicurezza su tutti i manifesti di dipendenze e sul codice sorgente dei campioni, quindi risolti tutti gli avvisi npm segnalati e un problema a livello di codice. Dopo la risoluzione, `npm audit` riporta **0 vulnerabilità** in ogni directory controllata.

#### Vulnerabilità delle dipendenze npm (transitive) — Risolte

Controllati tutti i 15 file `package-lock.json` impegnati. Le vulnerabilità erano limitate a dipendenze transitive introdotte dallo strumento di sviluppo MCP Inspector, dal client OpenAI e dall’SDK MCP; tutte ora risolte senza rompere i campioni:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** e **lab3/code/weather_mcp/inspector**: Aggiornato `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), che ha risolto gli avvisi sui pacchetti inclusi `ajv`, `brace-expansion`, `diff`, `path-to-regexp` e `ws`. Aggiunta una voce npm `overrides` che forza la versione corretta `shell-quote@1.8.4` per eliminare l’ultimo avviso critico trasportato da `concurrently`; rigenerati entrambi i lockfile (ora 0 vulnerabilità)
- **03-GettingStarted/samples/typescript**: `npm audit fix` ha aggiornato la dipendenza transitiva `qs` (moderata) a una release corretta
- **03-GettingStarted/samples/javascript**: `npm audit fix` ha aggiornato la dipendenza transitiva `hono` (moderata) a una release corretta
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` ha aggiornato la dipendenza transitiva `form-data` (alta) a una release corretta
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generato il `package-lock.json` mancante in modo che il progetto sia riproducibile e controllabile (0 vulnerabilità)

#### Correzione della sicurezza a livello di codice (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Rimosso `shell=True` dallo strumento `open_in_vscode`. Il precedente `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` permetteva ai metacaratteri di shell in un percorso di cartella di essere interpretati da `cmd.exe` (vettore di injection di comandi). Ora avvia direttamente `Code.exe` risolto con la cartella come argomento — senza shell — il che è funzionalmente equivalente e sicuro

#### Audit delle dipendenze Python

- Controllate tutte le richieste Python con `pip-audit`. `05-AdvancedTopics` e `03-GettingStarted/samples/python` non segnalano **vulnerabilità conosciute** (le versioni di `mcp` / `httpx` / `pydantic` / `python-dotenv` si risolvono in release corrette attuali)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` ha segnalato la dipendenza transitiva **`werkzeug` 3.1.1** con tre avvisi DoS del nome dispositivo di Windows `safe_join` — `CVE-2025-66221`, `CVE-2026-21860` e `CVE-2026-27199` (tutti risolti nella 3.1.6). Aggiunta una versione esplicita di sicurezza `werkzeug>=3.1.6` in modo che la release corretta venga risolta; verificato che il vincolo si risolve correttamente con lo stack `chainlit` / `mcp` / `semantic-kernel`

### Ridenominazione del nome del prodotto

Aggiornati tutti i contenuti del curriculum per riflettere la ridenominazione del prodotto Microsoft:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Link della community Discord aggiornato

- **AGENTS.md**: Riferimento al server Discord aggiornato
- **README.md**: Riferimenti all'ecosistema tecnologico aggiornati
- **study_guide.md**: Riferimenti agli studi di caso aggiornati
- **05-AdvancedTopics/README.md**: Titolo e descrizione del Modulo 5.13 aggiornati
- **05-AdvancedTopics/mcp-integration/README.md**: Intestazione della sezione e descrizione aggiornate
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Titolo completo del modulo e aggiornamento dei contenuti
- **05-AdvancedTopics/mcp-security-entra/README.md**: Link di riferimento incrociato aggiornato
- **07-LessonsfromEarlyAdoption/README.md**: Riferimenti agli studi di caso aggiornati
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Intestazione della Sezione 9, badge e capacità aggiornati
- **08-BestPractices/README.md**: Link alla community Discord aggiornato
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Riferimento al canale Discord aggiornato
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Riferimento al deployment del modello aggiornato
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Tabella dei Servizi AI aggiornata
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Riferimenti alle risorse aggiornati

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension per VS Code
- **README.md**: Riferimenti principali al curriculum aggiornati
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Titolo del modulo, panoramica e tutte le intestazioni dei moduli aggiornati
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Titolo, obiettivi didattici, istruzioni di configurazione e risorse aggiornati
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Titolo, obiettivi didattici, tabella degli host MCP e riferimenti incrociati aggiornati
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Titolo, badge, prerequisiti e risorse aggiornati
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Riferimenti ad Agent Builder e link al feedback aggiornati
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Prerequisiti e riferimenti alle estensioni aggiornati

---

## 11 aprile 2026

### Nuova lezione, correzioni della documentazione e aggiornamenti delle dipendenze

#### Nuovi contenuti del curriculum aggiunti

**Modulo 05 - Argomenti Avanzati**
- **Lezione 5.17: Ragionamento multi-agente avversariale con MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nuova guida completa che copre il modello di dibattito avversariale per sistemi multi-agente
  - Diagramma di architettura Mermaid: due agenti → server MCP condiviso → trascrizione del dibattito → giudice → verdetto
  - Server di strumenti MCP condiviso (`web_search` + `run_python`) implementato in Python e TypeScript
  - Prompt di sistema opposti (PER / CONTRO / Giudice) con richieste esplicite di utilizzo degli strumenti
  - Orchestratore del dibattito in Python, TypeScript e C# che gestisce i turni e instrada gli argomenti
  - Cablaggio MCP `ClientSession` per l'orchestratore alle chiamate reali degli strumenti
  - Tabella dei casi d'uso (rilevamento di allucinazioni, modellazione delle minacce, revisione del design API, verifica fattuale, selezione tecnologica)
  - Considerazioni sulla sicurezza: esecuzione sandboxata, convalida delle chiamate agli strumenti, limitazione del tasso, audit logging
  - Esercizio strutturato con tre scenari pratici (revisione del codice, decisione architetturale, moderazione dei contenuti)

#### Correzioni della documentazione

**Modulo 03 - Introduzione**
- **05-stdio-server/README.md**: Corretto esempio parziale di server stdio TypeScript — aggiunta l'istanza di transport mancante (`new StdioServerTransport()`) e la chiamata `server.connect(transport)` per allineare agli esempi Python e .NET nella stessa sezione
- **14-sampling/README.md**: Corretto errore di battitura — corretto da `"Sampling is an davanced features"` a `"Sampling is an advanced feature"`

#### Aggiornamenti del curriculum

**README.md principale**
- Aggiunto voce 5.17 (Ragionamento multi-agente avversariale con MCP) nella tabella del curriculum con link diretto alla nuova lezione

**05-AdvancedTopics/README.md**
- Aggiunta riga Lezione 5.17 alla tabella delle lezioni

**study_guide.md**
- Aggiunto l'argomento Ragionamento multi-agente avversariale alla mappa mentale e alla descrizione in prosa degli Argomenti Avanzati

#### Correzioni del codice e della sicurezza

**Modulo 05 - Agenti Avversari (`mcp-adversarial-agents`)**
- **Correzione di sicurezza — iniezione comandi**: Sostituito l'interpolazione di shell `execSync` con `execFile` + `promisify` nello strumento TypeScript `run_python`, eliminando la superficie di iniezione comandi (il codice controllato da LLM ora viene passato come elemento argv letterale senza coinvolgimento della shell)
- **Cablaggio del ciclo degli strumenti MCP**: Aggiornato l'orchestratore dibattito Python per usare il client `AsyncAnthropic` (sostituendo il blocco sincrono `Anthropic`), passare una `ClientSession` live direttamente a ogni turno agente, recuperare la definizione degli strumenti tramite `session.list_tools()` a ogni turno e inviare i blocchi `tool_use` tramite `session.call_tool()` in un ciclo fino a che il modello emette una risposta testuale finale

#### Aggiornamenti delle dipendenze

- Aggiornato `hono` alla versione 4.12.12 in più pacchetti (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Aggiornato `@hono/node-server` da 1.19.11 a 1.19.13 nei pacchetti TypeScript
- Aggiornato `cryptography` da 46.0.5 a 46.0.7 nei pacchetti Python (lab 3 e 4 di 10-StreamliningAIWorkflows)
- Aggiornato `lodash` da 4.17.23 a 4.18.1 in 10-StreamliningAIWorkflows inspector

#### Traduzioni

- Sincronizzate le traduzioni per oltre 48 lingue con le ultime modifiche al codice sorgente (aggiornamento i18n)

---

## 5 febbraio 2026

### Miglioramenti alla validazione e navigazione nell'intero repository

#### Nuovi contenuti del curriculum aggiunti

**Modulo 03 - Introduzione**
- **12-mcp-hosts/README.md**: Nuova guida completa per la configurazione degli host MCP
  - Esempi di configurazione per Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Template di configurazione JSON per tutti i principali host
  - Tabella di confronto tipi di trasporto (stdio, SSE/HTTP, WebSocket)
  - Risoluzione di problemi comuni di connessione
  - Best practice di sicurezza per la configurazione degli host

- **13-mcp-inspector/README.md**: Nuova guida al debug per MCP Inspector
  - Metodi di installazione (npx, npm globale, da sorgente)
  - Connessione a server via stdio e HTTP/SSE
  - Test di strumenti, risorse e flussi di lavoro dei prompt
  - Integrazione con VS Code tramite MCP Inspector
  - Scenari comuni di debug con soluzioni

**Modulo 04 - Implementazione Pratica**
- **pagination/README.md**: Nuova guida all'implementazione della paginazione
  - Modelli di paginazione basata su cursore in Python, TypeScript, Java
  - Gestione della paginazione lato client
  - Strategie di progettazione del cursore (opaco vs strutturato)
  - Raccomandazioni per l'ottimizzazione delle prestazioni

**Modulo 05 - Argomenti Avanzati**
- **mcp-protocol-features/README.md**: Approfondimento sulle funzionalità del protocollo
  - Implementazione delle notifiche di progresso
  - Modelli di cancellazione delle richieste
  - Template di risorse con pattern URI
  - Gestione del ciclo di vita del server
  - Controllo dei livelli di logging
  - Modelli di gestione degli errori con codici JSON-RPC

#### Correzioni della navigazione (oltre 24 file aggiornati)

**README principali dei Moduli**
 Ora collegano sia alla prima lezione CHE al modulo successivo

**Sotto-file sicurezza 02-Security**
- Tutti i 5 documenti supplementari di sicurezza ora hanno la navigazione "Cosa c'è dopo":

**File di Case Study 09-CaseStudy**
- Tutti i file degli studi di caso ora hanno navigazione sequenziale:

**Lab 10-StreamliningAI**
Aggiunta sezione Cosa c'è dopo alla panoramica del Modulo 10 e al Modulo 11

#### Correzioni al codice e ai contenuti

**Aggiornamenti SDK e dipendenze**
Versione vuota di openai corretta a `^4.95.0`
SDK aggiornata da `^1.8.0` a `>=1.26.0`
Versioni di mcp aggiornate a `>=1.26.0`

**Correzioni del codice**
Modello invalido `gpt-4o-mini` corretto in `gpt-4.1-mini`

**Correzioni dei contenuti**
Link rotto `READMEmd` corretto in `README.md`, intestazione curriculum `Module 1-3` corretta in `Module 0-3`, percorso case-sensitive corretto
Contenuto duplicato corrotto del Case Study 5 rimosso

**Miglioramenti per i principianti**
Aggiunta introduzione appropriata, obiettivi didattici e prerequisiti per i principianti

#### Aggiornamenti del curriculum

**README.md principale**
- Aggiunte voci 3.12 (Host MCP), 3.13 (MCP Inspector), 4.1 (Paginazione), 5.16 (Funzionalità Protocollo) alla tabella del curriculum

**README dei Moduli**
Aggiunte lezioni 12 e 13 alla lista delle lezioni
Aggiunta sezione Guide Pratiche con link alla paginazione
Aggiunte lezioni 5.15 (Trasporto Personalizzato) e 5.16 (Funzionalità Protocollo)

**study_guide.md**
- Mindmap aggiornata con tutti i nuovi argomenti: Configurazione Host MCP, MCP Inspector, Strategie di Paginazione, Approfondimento funzionalità Protocollo

## 28 gennaio 2026

### Revisione conformità specifica MCP 2025-11-25

#### Miglioramento dei concetti fondamentali (01-CoreConcepts/)
- **Nuovo primitivo client - Roots**: Aggiunta documentazione completa sul primitivo client Roots, che consente ai server di comprendere i confini del filesystem e i permessi di accesso
- **Annotazioni degli strumenti**: Aggiunta documentazione sulle annotazioni comportamentali degli strumenti (`readOnlyHint`, `destructiveHint`) per migliori decisioni sull’esecuzione degli strumenti
- **Chiamata agli strumenti nel Sampling**: Aggiornata la documentazione di Sampling per includere i parametri `tools` e `toolChoice` per l’invocazione degli strumenti guidata dal modello durante le richieste di sampling
- **Elicitazione Modalità URL**: Aggiunta documentazione sull’elicitazione basata su URL per interazioni web esterne avviate dal server
- **Tasks (Sperimentale)**: Aggiunta nuova sezione che documenta la funzionalità sperimentale Tasks per wrapper di esecuzione duratura e recupero risultato differito
- **Supporto Icone**: Segnalato che strumenti, risorse, template di risorse e prompt possono ora includere icone come metadati aggiuntivi

#### Aggiornamenti della documentazione
- **README.md**: Aggiunta referenza alla versione MCP Specifica 2025-11-25 e spiegazione della versione basata sulla data
- **study_guide.md**: Aggiornata mappa del curriculum per includere Tasks e Annotazioni degli strumenti nella sezione Concetti fondamentali; aggiornato timestamp del documento

#### Verifica di conformità alla specifica
- **Versione del protocollo**: Verificata l’attualità della documentazione rispetto alla specifica MCP 2025-11-25
- **Allineamento architetturale**: Confermata accuratezza della documentazione sull’architettura a due livelli (Data Layer + Transport Layer)
- **Documentazione dei primitivi**: Validati primitivi server (Risorse, Prompt, Strumenti) e primitivi client (Sampling, Elicitation, Logging, Roots)
- **Meccanismi di trasporto**: Verificata accuratezza della documentazione su trasporto STDIO e HTTP streamable
- **Linee guida di sicurezza**: Confermata conformità con le best practice di sicurezza MCP attuali

#### Principali funzionalità MCP 2025-11-25 documentate
- **OpenID Connect Discovery**: Scoperta del server di autenticazione tramite OIDC
- **Documenti dei metadati OAuth Client ID**: Meccanismo di registrazione del client raccomandato
- **JSON Schema 2020-12**: Dialetto predefinito per le definizioni di schema MCP
- **Sistema di classificazione SDK**: Formalizzazione dei requisiti di supporto e manutenzione delle funzionalità SDK
- **Struttura di governance**: Formalizzazione di Working Groups e Interest Groups nella governance MCP

### Aggiornamento importante della documentazione di sicurezza (02-Security/)

#### Integrazione Workshop MCP Security Summit (Sherpa)
- **Nuova risorsa di formazione pratica**: Aggiunta integrazione completa con il [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) in tutta la documentazione di sicurezza
- **Copertura del percorso spedizione**: Documentata la progressione completa campo per campo dalla Base Camp alla vetta
- **Allineamento OWASP**: Tutte le linee guida di sicurezza ora mappano ai rischi dell’OWASP MCP Azure Security Guide

#### Integrazione OWASP MCP Top 10
- **Nuova sezione**: Aggiunta tabella dei rischi di sicurezza OWASP MCP Top 10 con mitigazioni Azure nel README principale sulla sicurezza
- **Documentazione basata sui rischi**: Aggiornato mcp-security-controls-2025.md con riferimenti ai rischi OWASP MCP per ciascun dominio di sicurezza
- **Architettura di riferimento**: Collegamenti all’architettura di riferimento e ai pattern di implementazione dell’OWASP MCP Azure Security Guide

#### File di sicurezza aggiornati
- **README.md**: Aggiunta panoramica del Workshop Sherpa, tabella del percorso della spedizione, riepilogo rischi OWASP MCP Top 10 e sezione formazione pratica
- **mcp-security-controls-2025.md**: Intestazione aggiornata a febbraio 2026, aggiunti riferimenti ai rischi OWASP (MCP01-MCP08), correzione incongruenze versione specifica
- **mcp-security-best-practices-2025.md**: Aggiunta sezione risorse Sherpa e OWASP, aggiornato timestamp
- **mcp-best-practices.md**: Aggiunta sezione formazione pratica con link a Sherpa e OWASP
- **azure-content-safety-implementation.md**: Aggiunto riferimento OWASP MCP06, allineamento Sherpa Campo 3 e sezione risorse aggiuntive

#### Nuovi link a risorse aggiunti
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Pagine dei singoli rischi OWASP MCP (MCP01-MCP10)

### Allineamento della Specifica MCP per il Curriculum 2025-11-25

#### Modulo 03 - Introduzione
- **Documentazione SDK**: Aggiunto Go SDK alla lista ufficiale degli SDK; aggiornati tutti i riferimenti SDK per allinearsi con la Specifica MCP 2025-11-25
- **Chiarimento Trasporto**: Aggiornate le descrizioni dei trasporti STDIO e HTTP Streaming con riferimenti espliciti alla specifica

#### Modulo 04 - Implementazione Pratica
- **Aggiornamenti SDK**: Aggiunto Go SDK; aggiornata la lista SDK con riferimento alla versione della specifica
- **Specifica Autorizzazione**: Aggiornato il link alla specifica MCP Authorization alla versione attuale 2025-11-25

#### Modulo 05 - Argomenti Avanzati
- **Nuove Funzionalità**: Aggiunta nota sulle nuove funzionalità della Specifica MCP 2025-11-25 (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Risorse di Sicurezza**: Aggiunti link a OWASP MCP Top 10 e workshop Sherpa tra i riferimenti aggiuntivi

#### Modulo 06 - Contributi della Comunità
- **Lista SDK**: Aggiunti SDK Swift e Rust; aggiornato il link alla specifica alla data 2025-11-25
- **Riferimento Specifica**: Aggiornato il link alla Specifica MCP all'URL diretto della specifica

#### Modulo 07 - Lezioni dall’Adozione Precoce
- **Aggiornamenti Risorse**: Aggiunto link alla Specifica MCP 2025-11-25 e OWASP MCP Top 10 tra le risorse aggiuntive

#### Modulo 08 - Best Practices
- **Versione Specifica**: Aggiornato riferimento alla Specifica MCP al 2025-11-25
- **Risorse di Sicurezza**: Aggiunti OWASP MCP Top 10 e workshop Sherpa tra i riferimenti aggiuntivi

#### Modulo 10 - Ottimizzazione dei Workflow AI
- **Aggiornamento Badge**: Cambiato il badge della versione MCP da versione SDK (1.9.3) a versione specifica (2025-11-25)
- **Link Risorse**: Aggiornato link alla Specifica MCP; aggiunto OWASP MCP Top 10

#### Modulo 11 - Laboratori Pratici MCP Server
- **Riferimento Specifica**: Aggiornato link alla Specifica MCP alla versione 2025-11-25
- **Risorse di Sicurezza**: Aggiunto OWASP MCP Top 10 alle risorse ufficiali

## 18 dicembre 2025

### Aggiornamento Documentazione di Sicurezza - Specifica MCP 2025-11-25

#### Pratiche di Sicurezza MCP (02-Security/mcp-best-practices.md) - Aggiornamento versione specifica
- **Aggiornamento Versione Protocollo**: Aggiornato per fare riferimento alla più recente Specifica MCP 2025-11-25 (rilasciata il 25 novembre 2025)
  - Aggiornati tutti i riferimenti alla versione della specifica da 2025-06-18 a 2025-11-25
  - Aggiornate le date di riferimento del documento da 18 agosto 2025 a 18 dicembre 2025
  - Verificati tutti gli URL della specifica puntano alla documentazione attuale
- **Validazione Contenuti**: Validazione completa delle best practice di sicurezza rispetto agli standard più recenti
  - **Soluzioni di Sicurezza Microsoft**: Verificata la terminologia attuale e i link per Prompt Shields (precedentemente "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID e Azure Key Vault
  - **Sicurezza OAuth 2.1**: Confermata l’allineamento con le più recenti best practice di sicurezza OAuth
  - **Standard OWASP**: Validati i riferimenti a OWASP Top 10 per LLM rimangono aggiornati
  - **Servizi Azure**: Verificati tutti i link della documentazione Microsoft Azure e le best practice
- **Allineamento agli Standard**: Confermati tutti gli standard di sicurezza referenziati come attuali
  - Quadro di Gestione dei Rischi AI NIST
  - ISO 27001:2022
  - Best practice di sicurezza OAuth 2.1
  - Framework di sicurezza e conformità Azure
- **Risorse per l’Implementazione**: Validati tutti i link e le risorse delle guide di implementazione
  - Pattern di autenticazione Azure API Management
  - Guide d’integrazione Microsoft Entra ID
  - Gestione segreti Azure Key Vault
  - Pipeline DevSecOps e soluzioni di monitoraggio

### Assicurazione Qualità della Documentazione
- **Conformità alla Specifica**: Garantito che tutti i requisiti di sicurezza MCP obbligatori (MUST/MUST NOT) siano conformi alla specifica più recente
- **Aggiornamento Risorse**: Verificati tutti i link esterni verso la documentazione Microsoft, standard di sicurezza e guide d’implementazione
- **Copertura Best Practice**: Confermato il trattamento completo di autenticazione, autorizzazione, minacce specifiche AI, sicurezza della supply chain e pattern enterprise

## 6 ottobre 2025

### Espansione Sezione Getting Started – Uso Avanzato Server & Autenticazione Semplice

#### Uso Avanzato Server (03-GettingStarted/10-advanced)
- **Nuovo Capitolo Aggiunto**: Introdotta guida completa all’uso avanzato del server MCP, includendo architetture server regolari e low-level.
  - **Server Regolare vs Low-Level**: Confronto dettagliato ed esempi di codice in Python e TypeScript per entrambi gli approcci.
  - **Design Basato su Handler**: Spiegazione della gestione di tool/risorse/prompt tramite handler per implementazioni server scalabili e flessibili.
  - **Pattern Pratici**: Scenari reali in cui i pattern server low-level sono vantaggiosi per funzionalità avanzate e architettura.

#### Autenticazione Semplice (03-GettingStarted/11-simple-auth)
- **Nuovo Capitolo Aggiunto**: Guida passo-passo all’implementazione di autenticazione semplice nei server MCP.
  - **Concetti di Auth**: Spiegazione chiara di autenticazione vs autorizzazione e gestione delle credenziali.
  - **Implementazione Basic Auth**: Pattern di autenticazione basati su middleware in Python (Starlette) e TypeScript (Express), con esempi di codice.
  - **Progresso verso Sicurezza Avanzata**: Indicazioni sul passaggio da autenticazione semplice a OAuth 2.1 e RBAC, con riferimenti ai moduli di sicurezza avanzata.

Queste aggiunte forniscono indicazioni pratiche e operative per costruire implementazioni server MCP più robuste, sicure e flessibili, collegando concetti fondamentali a pattern avanzati di produzione.

## 29 settembre 2025

### Laboratori di Integrazione Database MCP Server - Percorso di Apprendimento Pratico Completo

#### 11-MCPServerHandsOnLabs - Nuovo Curriculum Completo di Integrazione Database
- **Percorso Completo di 13 Laboratori**: Aggiunto curriculum pratico completo per costruire server MCP pronti per la produzione con integrazione database PostgreSQL
  - **Implementazione Real-World**: Caso d’uso di analisi Zava Retail che dimostra pattern di livello enterprise
  - **Progressione di Apprendimento Strutturata**:
    - **Laboratori 00-03: Fondamenti** - Introduzione, Architettura Base, Sicurezza & Multi-Tenancy, Configurazione Ambiente
    - **Laboratori 04-06: Costruzione MCP Server** - Design Database & Schema, Implementazione MCP Server, Sviluppo Tool  
    - **Laboratori 07-09: Funzionalità Avanzate** - Integrazione Ricerca Semantica, Testing & Debugging, Integrazione VS Code
    - **Laboratori 10-12: Produzione & Best Practices** - Strategie di Deployment, Monitoraggio & Osservabilità, Best Practice & Ottimizzazione
  - **Tecnologie Enterprise**: Framework FastMCP, PostgreSQL con pgvector, embedding Azure OpenAI, Azure Container Apps, Application Insights
  - **Funzionalità Avanzate**: Row Level Security (RLS), ricerca semantica, accesso multi-tenant ai dati, embedding vettoriali, monitoraggio in tempo reale

#### Standardizzazione Terminologia - Conversione da Modulo a Laboratorio
- **Aggiornamento Completo Documentazione**: Aggiornati sistematicamente tutti i file README in 11-MCPServerHandsOnLabs per usare la terminologia "Laboratorio" invece di "Modulo"
  - **Intestazioni Sezioni**: Aggiornato "Cosa copre questo modulo" in "Cosa copre questo laboratorio" in tutti e 13 i laboratori
  - **Descrizione Contenuto**: Cambiato "Questo modulo fornisce..." in "Questo laboratorio fornisce..." in tutta la documentazione
  - **Obiettivi di Apprendimento**: Aggiornato "Al termine di questo modulo..." in "Al termine di questo laboratorio..."
  - **Link di Navigazione**: Convertiti tutti i riferimenti "Modulo XX:" in "Laboratorio XX:" nei riferimenti incrociati e nella navigazione
  - **Tracciamento Stato Completamento**: Aggiornato "Dopo aver completato questo modulo..." in "Dopo aver completato questo laboratorio..."
  - **Riferimenti Tecnici Preservati**: Mantenuti i riferimenti ai moduli Python nei file di configurazione (es. `"module": "mcp_server.main"`)

#### Miglioramento Guida di Studio (study_guide.md)
- **Mappa Visuale del Curriculum**: Aggiunta nuova sezione "11. Laboratori di Integrazione Database" con visualizzazione completa della struttura dei laboratori
- **Struttura del Repository**: Aggiornate da dieci a undici le sezioni principali con descrizione dettagliata di 11-MCPServerHandsOnLabs
- **Indicazioni Percorso di Apprendimento**: Migliorate le istruzioni di navigazione per coprire le sezioni 00-11
- **Copertura Tecnologica**: Aggiunti dettagli su integrazione FastMCP, PostgreSQL e servizi Azure
- **Risultati di Apprendimento**: Enfatizzato sviluppo di server pronti per la produzione, pattern di integrazione database e sicurezza enterprise

#### Miglioramento Struttura README Principale
- **Terminologia Basata su Laboratori**: Aggiornato README.md principale in 11-MCPServerHandsOnLabs per usare coerentemente la struttura "Laboratorio"
- **Organizzazione Percorso di Apprendimento**: Progressione chiara da concetti fondamentali a implementazione avanzata fino a deployment in produzione
- **Focus Real-World**: Enfasi su apprendimento pratico con pattern e tecnologie enterprise

### Miglioramenti Qualità & Coerenza Documentazione
- **Enfasi Apprendimento Pratico**: Rinforzato approccio pratico basato su laboratori in tutta la documentazione
- **Focus Pattern Enterprise**: Evidenziate implementazioni pronte per la produzione e considerazioni di sicurezza enterprise
- **Integrazione Tecnologica**: Copertura completa dei moderni servizi Azure e pattern di integrazione AI
- **Progressione Apprendimento**: Percorso chiaro e strutturato da concetti base a deployment in produzione

## 26 settembre 2025

### Miglioramento Case Studies - Integrazione Registro MCP su GitHub

#### Case Studies (09-CaseStudy/) - Focus sullo Sviluppo dell’Ecosistema
- **README.md**: Ampia espansione con case study completo sul Registro MCP GitHub
  - **Case Study Registro MCP GitHub**: Nuovo case study esaustivo sull’avvio del Registro MCP GitHub a settembre 2025
    - **Analisi del Problema**: Esame dettagliato della frammentazione discovery e delle sfide di deployment MCP server
    - **Architettura della Soluzione**: Approccio di registro centralizzato di GitHub con installazione VS Code con un solo clic
    - **Impatto Business**: Miglioramenti misurabili su onboarding e produttività sviluppatori
    - **Valore Strategico**: Focus sul deployment modulare di agenti e interoperabilità cross-tool
    - **Sviluppo Ecosistema**: Posizionamento come piattaforma fondamentale per integrazione agentica
  - **Struttura Case Study Migliorata**: Aggiornati tutti e sette i case studies con formato coerente e descrizioni complete
    - Azure AI Travel Agents: enfasi su orchestrazione multi-agente
    - Integrazione Azure DevOps: focus sull’automazione workflow
    - Recupero Documentazione in Tempo Reale: implementazione client console Python
    - Generatore Interattivo Piano di Studio: web app conversazionale Chainlit
    - Documentazione In-Editor: integrazione VS Code e GitHub Copilot
    - Azure API Management: pattern di integrazione API enterprise
    - Registro MCP GitHub: sviluppo ecosistema e piattaforma comunitaria
  - **Conclusione Completa**: Sezione conclusiva riscritta che evidenzia sette case studies coprendo molteplici dimensioni di implementazione MCP
    - Integrazione Enterprise, Orchestrazione Multi-Agente, Produttività Sviluppatori
    - Sviluppo Ecosistema, categorizzazione Applicazioni Educative
    - Approfondimenti potenziati su pattern architetturali, strategie di implementazione e best practice
    - Enfasi su MCP come protocollo maturo e pronto per la produzione

#### Aggiornamenti Guida di Studio (study_guide.md)
- **Mappa Visuale Curriculum**: Aggiornata mindmap per includere Registro MCP GitHub nella sezione Case Studies
- **Descrizione Case Studies**: Migliorata da descrizioni generiche a dettaglio di sette case studies completi
- **Struttura Repository**: Aggiornata sezione 10 per riflettere la copertura completa dei case studies con dettagli di implementazione specifici
- **Integrazione Changelog**: Aggiunta voce del 26 settembre 2025 che documenta aggiunta Registro MCP GitHub e miglioramenti case studies
- **Aggiornamento Date**: Aggiornata data a piè di pagina per riflettere l’ultima revisione (26 settembre 2025)

### Miglioramenti Qualità Documentazione
- **Miglioramento Coerenza**: Standardizzato formato e struttura case study in tutti e sette gli esempi
- **Copertura Completa**: Case studies ora coprono scenari enterprise, produttività sviluppatori e sviluppo ecosistema
- **Posizionamento Strategico**: Rafforzato focus su MCP come piattaforma fondamentale per il deployment di sistemi agentici
- **Integrazione Risorse**: Aggiornate risorse aggiuntive per includere link a Registro MCP GitHub

## 15 settembre 2025

### Espansione Argomenti Avanzati - Trasporti Personalizzati & Context Engineering

#### Trasporti Personalizzati MCP (05-AdvancedTopics/mcp-transport/) - Nuova Guida Avanzata all’Implementazione
- **README.md**: Guida completa all’implementazione di meccanismi di trasporto personalizzati MCP
  - **Trasporto Azure Event Grid**: Implementazione completa di trasporto serverless event-driven
    - Esempi C#, TypeScript e Python con integrazione Azure Functions
    - Pattern di architettura event-driven per soluzioni MCP scalabili
    - Ricevitori webhook e gestione messaggi push-based
  - **Trasporto Azure Event Hubs**: Implementazione di trasporto streaming ad alta capacità
    - Capacità di streaming in tempo reale per scenari low-latency
    - Strategie di partizionamento e gestione checkpoint
    - Batch di messaggi e ottimizzazione delle prestazioni
  - **Pattern di Integrazione Enterprise**: Esempi architetturali pronti per la produzione
    - Elaborazione MCP distribuita su più Azure Functions
    - Architetture di trasporto ibride combinando più tipi di trasporto
    - Durabilità messaggi, affidabilità e strategie di gestione errori
  - **Sicurezza & Monitoraggio**: Integrazione Azure Key Vault e pattern di osservabilità
    - Autenticazione managed identity e accesso con privilegi minimi
    - Telemetria Application Insights e monitoraggio delle prestazioni
    - Circuit breakers e pattern di tolleranza agli errori
  - **Framework di Test**: Strategie complete di testing per trasporti personalizzati
    - Test unitari con test doubles e framework di mocking
    - Test di integrazione con Azure Test Containers
    - Considerazioni su test di prestazioni e carico

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente AI
- **README.md**: Esplorazione completa di context engineering come campo emergente
  - **Principi Fondamentali**: Condivisione completa del contesto, consapevolezza decisionale delle azioni, e gestione della finestra di contesto

  - **Allineamento del Protocollo MCP**: Come il design MCP affronta le sfide dell’ingegneria del contesto
    - Limitazioni della finestra di contesto e strategie di caricamento progressivo
    - Determinazione della rilevanza e recupero dinamico del contesto
    - Gestione multimodale del contesto e considerazioni sulla sicurezza
  - **Approcci di Implementazione**: Architetture single-threaded vs multi-agente
    - Tecniche di suddivisione e prioritarizzazione del contesto
    - Strategie di caricamento progressivo e compressione del contesto
    - Approcci stratificati del contesto e ottimizzazione del recupero
  - **Framework di Misurazione**: Metriche emergenti per la valutazione dell’efficacia del contesto
    - Efficienza in input, prestazioni, qualità e considerazioni sull’esperienza utente
    - Approcci sperimentali all’ottimizzazione del contesto
    - Analisi dei fallimenti e metodologie di miglioramento

#### Aggiornamenti nella Navigazione del Curriculum (README.md)
- **Struttura del Modulo Potenziata**: Tabella del curriculum aggiornata per includere nuovi argomenti avanzati
  - Inserite le voci Ingegneria del Contesto (5.14) e Trasporto Personalizzato (5.15)
  - Formattazione e link di navigazione coerenti in tutti i moduli
  - Descrizioni aggiornate per riflettere l’attuale ambito dei contenuti

### Migliorie nella Struttura della Directory
- **Standardizzazione dei Nomi**: Rinominata la cartella "mcp transport" in "mcp-transport" per coerenza con altre cartelle di argomenti avanzati
- **Organizzazione dei Contenuti**: Tutte le cartelle 05-AdvancedTopics ora seguono un pattern di denominazione coerente (mcp-[topic])

### Miglioramenti della Qualità della Documentazione
- **Allineamento con la Specifica MCP**: Tutti i nuovi contenuti si riferiscono alla specifica MCP 2025-06-18
- **Esempi Multilingue**: Esempi di codice completi in C#, TypeScript e Python
- **Focus Aziendale**: Pattern pronti per la produzione e integrazione con il cloud Azure
- **Documentazione Visiva**: Diagrammi Mermaid per visualizzare l’architettura e i flussi

## 18 agosto 2025

### Aggiornamento Completo della Documentazione - Standard MCP 2025-06-18

#### Best Practices di Sicurezza MCP (02-Security/) - Modernizzazione Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Riscrittura completa allineata con la specifica MCP 2025-06-18
  - **Requisiti Obbligatori**: Inseriti requisiti espliciti MUST/MUST NOT dalla specifica ufficiale con chiari indicatori visivi
  - **12 Pratiche Fondamentali di Sicurezza**: Ristrutturazione da lista di 15 punti a domini di sicurezza completi
    - Sicurezza del Token e Autenticazione con integrazione provider di identità esterni
    - Gestione della Sessione e Sicurezza del Trasporto con requisiti crittografici
    - Protezione Specifica per AI con integrazione Microsoft Prompt Shields
    - Controllo Accessi e Permessi con principio del minimo privilegio
    - Sicurezza e Monitoraggio dei Contenuti con integrazione Azure Content Safety
    - Sicurezza della Catena di Fornitura con verifica completa dei componenti
    - Sicurezza OAuth e Prevenzione Confused Deputy con implementazione PKCE
    - Risposta agli Incidenti e Recupero con capacità automatizzate
    - Conformità e Governance con allineamento regolamentare
    - Controlli Avanzati di Sicurezza con architettura zero trust
    - Integrazione nell’Ecosistema di Sicurezza Microsoft con soluzioni complete
    - Evoluzione Continua della Sicurezza con pratiche adattative
  - **Soluzioni di Sicurezza Microsoft**: Guida migliorata per integrazione di Prompt Shields, Azure Content Safety, Entra ID e GitHub Advanced Security
  - **Risorse per l’Implementazione**: Link risorse categorizzati per Documentazione Ufficiale MCP, Soluzioni di Sicurezza Microsoft, Standard di Sicurezza e Guide di Implementazione

#### Controlli Avanzati di Sicurezza (02-Security/) - Implementazione Aziendale
- **MCP-SECURITY-CONTROLS-2025.md**: Revisione completa con framework di sicurezza di livello enterprise
  - **9 Domini di Sicurezza Completi**: Espanso da controlli base a framework aziendale dettagliato
    - Autenticazione e Autorizzazione Avanzate con integrazione Microsoft Entra ID
    - Sicurezza del Token e Controlli Anti-Passthrough con validazione completa
    - Controlli di Sicurezza delle Sessioni con prevenzione del dirottamento
    - Controlli Specifici di Sicurezza AI con prevenzione di prompt injection e avvelenamento strumenti
    - Prevenzione degli Attacchi Confused Deputy con sicurezza proxy OAuth
    - Sicurezza Esecuzione Strumenti con sandboxing e isolamento
    - Controlli di Sicurezza della Catena di Fornitura con verifica dipendenze
    - Controlli di Monitoraggio e Rilevazione con integrazione SIEM
    - Risposta agli Incidenti e Recupero con capacità automatizzate
  - **Esempi di Implementazione**: Aggiunti blocchi di configurazione YAML dettagliati e esempi di codice
  - **Integrazione Soluzioni Microsoft**: Copertura completa di servizi di sicurezza Azure, GitHub Advanced Security e gestione dell’identità aziendale

#### Sicurezza Argomenti Avanzati (05-AdvancedTopics/mcp-security/) - Implementazione Pronta per la Produzione
- **README.md**: Riscrittura completa per implementazione sicurezza aziendale
  - **Allineamento con Specifica Attuale**: Aggiornato alla Specifica MCP 2025-06-18 con requisiti di sicurezza obbligatori
  - **Autenticazione Potenziata**: Integrazione Microsoft Entra ID con esempi completi in .NET e Java Spring Security
  - **Integrazione Sicurezza AI**: Implementazione Microsoft Prompt Shields e Azure Content Safety con esempi dettagliati in Python
  - **Mitigazione Avanzata delle Minacce**: Esempi completi di implementazione per
    - Prevenzione degli attacchi Confused Deputy con PKCE e validazione consenso utente
    - Prevenzione del Token Passthrough con validazione audience e gestione sicura del token
    - Prevenzione dirottamento sessione con binding crittografico e analisi comportamentale
  - **Integrazione Sicurezza Aziendale**: Monitoraggio Azure Application Insights, pipeline di rilevazione minacce e sicurezza della catena di fornitura
  - **Checklist di Implementazione**: Chiara distinzione tra controlli di sicurezza obbligatori e raccomandati con beneficio dell’ecosistema di sicurezza Microsoft

### Qualità della Documentazione e Allineamento agli Standard
- **Riferimenti alla Specifica**: Aggiornati tutti i riferimenti alla Specifica MCP 2025-06-18
- **Ecosistema di Sicurezza Microsoft**: Guida all’integrazione potenziata in tutta la documentazione di sicurezza
- **Implementazione Pratica**: Aggiunti esempi di codice dettagliati in .NET, Java e Python con pattern aziendali
- **Organizzazione delle Risorse**: Categorizzazione completa di documentazione ufficiale, standard di sicurezza e guide di implementazione
- **Indicatori Visivi**: Marcatore chiaro dei requisiti obbligatori rispetto alle pratiche raccomandate


#### Concetti Base (01-CoreConcepts/) - Modernizzazione Completa
- **Aggiornamento Versione Protocollo**: Aggiornato per fare riferimento alla Specifica MCP 2025-06-18 con versionamento basato su data (formato YYYY-MM-DD)
- **Raffinamento dell’Architettura**: Descrizioni migliorate di Host, Client e Server per riflettere i pattern architetturali MCP attuali
  - Host ora definiti chiaramente come applicazioni AI che coordinano più connessioni client MCP
  - Client descritti come connettori di protocollo che mantengono relazioni uno-a-uno con i server
  - Server migliorati con scenari di deployment locale vs remoto
- **Ristrutturazione Primitive**: Revisione completa delle primitive server e client
  - Primitive Server: Risorse (fonti dati), Prompt (template), Strumenti (funzioni eseguibili) con spiegazioni dettagliate ed esempi
  - Primitive Client: Campionamento (completamenti LLM), Estrazione (input utente), Registrazione (debug/monitoraggio)
  - Aggiornato con pattern correnti per metodi di scoperta (`*/list`), recupero (`*/get`) ed esecuzione (`*/call`)
- **Architettura del Protocollo**: Introdotto modello architetturale a due livelli
  - Livello Dati: Fondamenta JSON-RPC 2.0 con gestione del ciclo di vita e primitive
  - Livello Trasporto: STDIO (locale) e HTTP streamabile con SSE (trasporto remoto)
- **Framework di Sicurezza**: Principi di sicurezza completi tra cui consenso esplicito utente, protezione della privacy, sicurezza esecuzione strumenti e sicurezza livello trasporto
- **Pattern di Comunicazione**: Aggiornati messaggi di protocollo per mostrare flussi di inizializzazione, scoperta, esecuzione e notifica
- **Esempi di Codice**: Aggiornati esempi multilingua (.NET, Java, Python, JavaScript) per riflettere i pattern SDK MCP attuali

#### Sicurezza (02-Security/) - Revisione Completa della Sicurezza  
- **Allineamento agli Standard**: Completo con i requisiti di sicurezza della Specifica MCP 2025-06-18
- **Evoluzione dell’Autenticazione**: Documentata evoluzione dai server OAuth personalizzati alla delega provider di identità esterni (Microsoft Entra ID)
- **Analisi delle Minacce Specifiche AI**: Copertura migliorata dei vettori di attacco AI moderni
  - Scenari dettagliati di attacchi di prompt injection con esempi reali
  - Meccanismi di avvelenamento strumenti e pattern di attacco "rug pull"
  - Avvelenamento finestra di contesto e attacchi di confusione del modello
- **Soluzioni Microsoft AI per la Sicurezza**: Copertura completa dell’ecosistema di sicurezza Microsoft
  - AI Prompt Shields con avanzate tecniche di rilevazione, spotlighting e delimitazione
  - Pattern di integrazione Azure Content Safety
  - GitHub Advanced Security per la protezione della catena di fornitura
- **Mitigazione Avanzata delle Minacce**: Controlli di sicurezza dettagliati per
  - Dirottamento di sessione con scenari di attacco specifici MCP e requisiti crittografici ID sessione
  - Problemi Confused Deputy in scenari proxy MCP con requisiti di consenso esplicito
  - Vulnerabilità passthrough token con controlli obbligatori di validazione
- **Sicurezza Catena di Fornitura**: Copertura ampliata della catena AI includendo modelli base, servizi embedding, fornitori di contesto e API di terze parti
- **Sicurezza di Base**: Integrazione migliorata con pattern di sicurezza enterprise tra cui architettura zero trust ed ecosistema sicurezza Microsoft
- **Organizzazione Risorse**: Link risorse categorizzati per tipo (Documentazione Ufficiale, Standard, Ricerca, Soluzioni Microsoft, Guide di Implementazione)

### Miglioramenti nella Qualità della Documentazione
- **Obiettivi di Apprendimento Strutturati**: Migliorati con risultati specifici e attuabili
- **Riferimenti Incrociati**: Aggiunti link tra argomenti di sicurezza e concetti base correlati
- **Informazioni Aggiornate**: Aggiornate tutte le date e link alle specifiche agli standard correnti
- **Guida all’Implementazione**: Aggiunte linee guida specifiche e attuabili per l’implementazione in entrambe le sezioni

## 16 luglio 2025

### Miglioramenti README e Navigazione
- Navigazione del curriculum completamente ridisegnata in README.md
- Sostituiti i tag `<details>` con formato basato su tabelle più accessibile
- Create opzioni di layout alternative nella nuova cartella "alternative_layouts"
- Aggiunti esempi di navigazione a schede, basata su card e accordion
- Aggiornata sezione struttura del repository per includere tutti i file più recenti
- Potenziata la sezione "Come Usare Questo Curriculum" con chiare raccomandazioni
- Aggiornati link specifica MCP con URL corretti
- Aggiunta sezione Ingegneria del Contesto (5.14) alla struttura del curriculum

### Aggiornamenti Guida allo Studio
- Guida allo studio completamente rivista per allinearsi all’attuale struttura del repository
- Aggiunte nuove sezioni per MCP Clients e Tools, e MCP Servers Popolari
- Aggiornata la Mappa Visuale del Curriculum per riflettere accuratamente tutti i temi
- Potenziate descrizioni degli Argomenti Avanzati per coprire tutte le aree specializzate
- Aggiornata la sezione Case Studies per riflettere esempi reali
- Aggiunto questo changelog completo

### Contributi Comunitari (06-CommunityContributions/)
- Aggiunte informazioni dettagliate sui server MCP per generazione immagini
- Aggiunta sezione completa su utilizzo di Claude in VSCode
- Aggiunte istruzioni di configurazione e uso client terminale Cline
- Aggiornata sezione client MCP per includere tutte le opzioni popolari
- Potenziati esempi di contributo con campioni di codice più precisi

### Argomenti Avanzati (05-AdvancedTopics/)
- Organizzate tutte le cartelle di argomenti specializzati con denominazione coerente
- Aggiunti materiali ed esempi di ingegneria del contesto
- Aggiunta documentazione integrazione agente Foundry
- Potenziata documentazione integrazione sicurezza Entra ID

## 11 giugno 2025

### Creazione Iniziale
- Rilasciata prima versione del curriculum MCP per Principianti
- Creato struttura base per tutte e 10 le sezioni principali
- Implementata la Mappa Visuale del Curriculum per la navigazione
- Aggiunti progetti di esempio iniziali in più linguaggi di programmazione

### Introduzione (03-GettingStarted/)
- Creati primi esempi di implementazione server
- Aggiunta guida allo sviluppo client
- Incorporate istruzioni integrazione client LLM
- Aggiunta documentazione integrazione VS Code
- Implementati esempi server Server-Sent Events (SSE)

### Concetti Base (01-CoreConcepts/)
- Aggiunta spiegazione dettagliata dell’architettura client-server
- Creata documentazione sui componenti chiave del protocollo
- Documentati pattern di messaggistica in MCP

## 23 maggio 2025

### Struttura del Repository
- Inizializzato repository con struttura base di cartelle
- Creati file README per ogni sezione principale
- Impostata infrastruttura di traduzione
- Aggiunti asset immagini e diagrammi

### Documentazione
- Creato README.md iniziale con panoramica curriculum
- Aggiunti CODE_OF_CONDUCT.md e SECURITY.md
- Impostato SUPPORT.md con guida per richiedere aiuto
- Creato struttura preliminare guida allo studio

## 15 aprile 2025

### Pianificazione e Framework
- Pianificazione iniziale per il curriculum MCP per Principianti
- Definiti obiettivi di apprendimento e pubblico target
- Strutturato curriculum in 10 sezioni
- Sviluppato framework concettuale per esempi e case study
- Creati esempi prototipo iniziali per concetti chiave

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->