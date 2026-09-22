# AGENTS.md

## Panoramica del Progetto

**MCP per Principianti** è un curriculum educativo open-source per apprendere il Model Context Protocol (MCP) - un framework standardizzato per le interazioni tra modelli AI e applicazioni client. Questo repository offre materiali di apprendimento completi con esempi di codice pratici in diversi linguaggi di programmazione.

### Tecnologie Chiave

- **Linguaggi di Programmazione**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework e SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Database**: PostgreSQL con estensione pgvector
- **Piattaforme Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Strumenti di Build**: npm, Maven, pip, Cargo
- **Documentazione**: Markdown con traduzione automatizzata in più lingue (48+ lingue)

### Architettura

- **11 Moduli Core (00-11)**: Percorso di apprendimento sequenziale dai concetti fondamentali ai temi avanzati
- **Laboratori pratici**: Esercitazioni pratiche con codice di soluzione completo in più lingue
- **Progetti di esempio**: Implementazioni funzionanti di server e client MCP
- **Sistema di Traduzione**: Workflow GitHub Actions automatizzato per supporto multilingue
- **Risorse Immagini**: Directory centralizzata di immagini con versioni tradotte

## Comandi di Setup

Questo è un repository focalizzato sulla documentazione. La maggior parte del setup avviene all’interno dei singoli progetti di esempio e laboratori.

### Setup del Repository

```bash
# Clona il repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Lavorare con i Progetti di Esempio

I progetti di esempio si trovano in:
- `03-GettingStarted/samples/` - Esempi specifici per linguaggio
- `03-GettingStarted/01-first-server/solution/` - Prime implementazioni server
- `03-GettingStarted/02-client/solution/` - Implementazioni client
- `11-MCPServerHandsOnLabs/` - Laboratori completi di integrazione database

Ogni progetto di esempio contiene le proprie istruzioni di setup:

#### Progetti TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Progetti Python
```bash
cd <project-directory>
pip install -r requirements.txt
# oppure
pip install -e .
python main.py
```

#### Progetti Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Workflow di Sviluppo

### Prontezza MCP 7-28

#### Checklist di prontezza del repo

- [x] **Chiarezza per nuovi contributori**: Questo file definisce lo scopo del repository,
  la struttura, le regole di contribuzione e i percorsi di setup di esempio.
- [x] **Comandi di build/test/lint con flag esatti**:
  - Lint documentazione del repository:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Verifica pattern link documentazione:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validazione esempio TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validazione esempio Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validazione esempio Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Un workflow realistico che può diventare uno strumento MCP**:
  `validate_curriculum_change`
- [x] **Input/output sono espliciti** (vedi specifica sotto).
- [x] **Permessi e modalità di errore sono documentati** (vedi specifica sotto).
- [x] **Testabilità CI esplicita** (comandi deterministici, codici di uscita espliciti,
  e output leggibile dalla macchina).

#### Workflow candidato per strumento MCP: `validate_curriculum_change`

##### Obiettivo

Verificare lo stato della documentazione del curriculum e del codice di esempio rappresentativo
prima della fusione (merge).

##### Input

- `changed_paths: string[]` (richiesto) - percorsi relativi modificati nel PR.
- `run_docs_lint: boolean` (predefinito `true`)
- `run_links_audit: boolean` (predefinito `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (predefinito tutto `false`)

##### Output

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Permessi

- Lettura dei file workspace e scrittura di artefatti generati dallo strumento (es. report di lint,
  log di test) solamente; nessuna scrittura in `translations/` o
  `translated_images/`.
- Esecuzione di comandi shell locali.
- Accesso di rete opzionale solo per il ripristino pacchetti (`npm ci`,
  `python -m pip install`, risoluzione dipendenze `mvn`).
- Nessun permesso di push, merge, o modifica in `translations/` o
  `translated_images/`.

##### Modalità di fallimento

- `E_NO_INPUT_PATHS`: `changed_paths` vuoto.
- `E_INVALID_PATH`: il percorso input esce dalla radice del repository.
- `E_LINT_FAILED`: lint markdown termina con codice diverso da zero.
- `E_LINK_AUDIT_FAILED`: comando audit link termina con codice diverso da zero.
- `E_SAMPLE_TEST_FAILED`: test/build esempio termina con codice diverso da zero.
- `E_TIMEOUT`: il comando ha superato il timeout configurato.

##### Contratto CI raccomandato

Per automatizzare la validazione, configurare un job CI che:

- Si attiva su pull request che toccano `*.md`, codice di esempio, o questo file.
- Esegue esattamente i comandi elencati sopra.
- Conserva i log come artefatti.
- Fa fallire il lavoro su ogni codice di uscita diverso da zero.

#### Se distribuisci un server MCP da questo repo

- [ ] Leggi il changelog finale MCP `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verifica che la release SDK scelta supporti MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Rimuovi le assunzioni su sessione e handshake; tratta ogni richiesta come
  autonoma:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Invia intestazioni `Mcp-Method` e `Mcp-Name` per richieste HTTP raw:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Controlla i codici di errore hardcoded (`missing resource` spostato da `-32002` a `-32602`).

- [ ] Migrare Roots, Sampling, Logging e Registrazione Client Dinamici deprecati
  Registrazione:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrare via dall'API sperimentale `2025-11-25` Tasks:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Riesaminare l'autorizzazione per il rafforzamento di OAuth e OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Struttura della Documentazione

- **Moduli 00-11**: Contenuto del curriculum principale in ordine sequenziale
- **translations/**: Versioni specifiche per lingua (auto-generate, non modificare direttamente)
- **translated_images/**: Versioni localizzate delle immagini (auto-generate)
- **images/**: Immagini e diagrammi sorgente

### Apportare Modifiche alla Documentazione

1. Modificare solo i file markdown in inglese nelle directory root dei moduli (00-11)
2. Aggiornare le immagini nella directory `images/` se necessario
3. L'azione GitHub co-op-translator genera automaticamente le traduzioni
4. Le traduzioni sono rigenerate al push sul ramo main

### Lavorare con le Traduzioni

- **Traduzione automatica**: Il workflow GitHub Actions gestisce tutte le traduzioni
- **NON modificare manualmente** i file nella directory `translations/`
- I metadati della traduzione sono incorporati in ogni file tradotto
- Lingue supportate: oltre 48, inclusi Arabo, Cinese, Francese, Tedesco, Hindi, Giapponese, Coreano, Portoghese, Russo, Spagnolo e molte altre

## Istruzioni per il Testing

### Validazione della Documentazione

Poiché questo è principalmente un repository di documentazione, il testing si concentra su:

1. **Audit dei pattern di link**: Elencare i link Markdown per la revisione

   ```bash
   # Elenca i link Markdown (verifica del modello)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validazione degli esempi di codice**: Verificare che gli esempi di codice compilino/eseguano

   ```bash
   # Naviga al campione specifico ed esegui i suoi test
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting Markdown**: Controllare la coerenza nel formato

   ```bash
   # Usa markdownlint se necessario
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testing dei Progetti Esempio

Ogni esempio specifico per lingua include il proprio approccio di test:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Linee Guida per lo Stile del Codice

### Stile della Documentazione

- Usare un linguaggio chiaro e adatto ai principianti
- Includere esempi di codice in più lingue dove applicabile
- Seguire le migliori pratiche markdown:
  - Usare intestazioni in stile ATX (sintassi `#`)
  - Usare blocchi di codice fenced con identificatori di linguaggio
  - Includere testo alternativo descrittivo per le immagini
  - Mantenere lunghezze delle righe ragionevoli (nessun limite rigido, ma essere sensati)

### Stile degli Esempi di Codice

#### TypeScript/JavaScript
- Usare moduli ES (`import`/`export`)
- Seguire le convenzioni della modalità strict di TypeScript
- Includere annotazioni di tipo
- Target ES2022

#### Python
- Seguire le linee guida di stile PEP 8
- Usare type hint dove appropriato
- Includere docstring per funzioni e classi
- Usare funzionalità Python moderne (3.8+)

#### Java
- Seguire le convenzioni di Spring Boot
- Usare funzionalità di Java 21
- Seguire la struttura standard del progetto Maven
- Includere commenti Javadoc

### Organizzazione dei File

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Compilazione e Distribuzione

### Distribuzione della Documentazione

Il repository usa GitHub Pages o simili per l'hosting della documentazione (se applicabile). Le modifiche al ramo main attivano:

1. Workflow di traduzione (`.github/workflows/co-op-translator.yml`)
2. Traduzione automatica di tutti i file markdown in inglese
3. Localizzazione delle immagini se necessario

### Nessun Processo di Compilazione Richiesto

Questo repository contiene principalmente documentazione markdown. Non è necessaria alcuna fase di compilazione o build per il contenuto del curriculum principale.

### Distribuzione dei Progetti Esempio

I singoli progetti esempio possono avere istruzioni di distribuzione:
- Vedere `03-GettingStarted/09-deployment/` per la guida alla distribuzione del server MCP
- Esempi di distribuzione su Azure Container Apps in `11-MCPServerHandsOnLabs/`

## Linee Guida per il Contributo

### Processo di Pull Request

1. **Fork e Clona**: Fai il fork del repository e clona localmente il tuo fork
2. **Crea un Branch**: Usa nomi di branch descrittivi (es. `fix/typo-module-3`, `add/python-example`)
3. **Effettua Modifiche**: Modifica solo i file markdown in inglese (non le traduzioni)
4. **Testa Localmente**: Verifica che il markdown venga renderizzato correttamente
5. **Invia PR**: Usa titoli e descrizioni PR chiare
6. **CLA**: Firma il Microsoft Contributor License Agreement quando richiesto

### Formato del Titolo della PR

Usa titoli chiari e descrittivi:
- `[Module XX] Breve descrizione` per modifiche specifiche del modulo
- `[Samples] Descrizione` per modifiche agli esempi di codice
- `[Docs] Descrizione` per aggiornamenti generali della documentazione

### Cosa Contribuire

- Correzioni di bug nella documentazione o negli esempi di codice
- Nuovi esempi di codice in lingue aggiuntive
- Chiarimenti e miglioramenti dei contenuti esistenti
- Nuovi casi di studio o esempi pratici
- Segnalazioni di problemi per contenuti poco chiari o errati

### Cosa NON fare

- Non modificare direttamente i file nella directory `translations/`
- Non modificare la directory `translated_images/`
- Non aggiungere file binari di grandi dimensioni senza discussione
- Non modificare i file del workflow di traduzione senza coordinamento

## Note Aggiuntive

### Manutenzione del Repository

- **Changelog**: Tutte le modifiche significative sono documentate in `changelog.md`
- **Guida di Studio**: Usa `study_guide.md` per una panoramica della navigazione del curriculum
- **Template per Issue**: Usa i template GitHub per segnalazioni di bug e richieste di funzionalità
- **Codice di Condotta**: Tutti i contributori devono seguire il Codice di Condotta Open Source Microsoft

### Percorso di Apprendimento

Seguire i moduli in ordine sequenziale (00-11) per un apprendimento ottimale:
1. **00-02**: Fondamentali (Introduzione, Concetti Base, Sicurezza)
2. **03**: Inizio pratico con implementazioni hands-on
3. **04-05**: Implementazione pratica e argomenti avanzati
4. **06-10**: Comunità, best practice e applicazioni reali
5. **11**: Laboratori completi di integrazione database (13 laboratori sequenziali)

### Risorse di Supporto

- **Documentazione**: https://modelcontextprotocol.io/
- **Specifiche**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Comunità**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Server Discord Microsoft Foundry
- **Corsi Correlati**: Vedi README.md per altri percorsi di apprendimento Microsoft

### Risoluzione Comuni di Problemi

**D: La mia PR non supera la verifica di traduzione**
R: Assicurati di aver modificato solo i file markdown in inglese nelle directory root dei moduli, non le versioni tradotte.

**D: Come aggiungo una nuova lingua?**
R: Il supporto alle lingue è gestito attraverso il workflow co-op-translator. Apri un issue per discutere l'aggiunta di nuove lingue.

**D: Gli esempi di codice non funzionano**
R: Assicurati di aver seguito le istruzioni di configurazione nel README specifico dell'esempio. Verifica di avere le versioni corrette delle dipendenze installate.


**D: Le immagini non vengono visualizzate** 

A: Verificare che i percorsi delle immagini siano relativi e utilizzino le barre oblique. Le immagini dovrebbero trovarsi nella directory `images/` o in `translated_images/` per le versioni localizzate.

### Considerazioni sulle prestazioni

- Il flusso di lavoro di traduzione potrebbe richiedere diversi minuti per completarsi
- Le immagini di grandi dimensioni devono essere ottimizzate prima di effettuare il commit
- Mantenere i singoli file markdown focalizzati e di dimensioni ragionevoli
- Usare collegamenti relativi per una migliore portabilità

### Governance del progetto

Questo progetto segue le pratiche open source di Microsoft:
- Licenza MIT per il codice e la documentazione
- Codice di condotta Open Source Microsoft
- CLA richiesta per i contributi
- Problemi di sicurezza: seguire le linee guida di SECURITY.md
- Supporto: consultare SUPPORT.md per le risorse di aiuto

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->