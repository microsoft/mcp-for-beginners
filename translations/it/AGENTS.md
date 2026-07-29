# AGENTS.md

## Panoramica del Progetto

**MCP per Principianti** è un curriculum educativo open-source per l'apprendimento del Model Context Protocol (MCP) - un framework standardizzato per le interazioni tra modelli AI e applicazioni client. Questo repository fornisce materiali di apprendimento completi con esempi di codice pratici in più linguaggi di programmazione.

### Tecnologie Chiave

- **Linguaggi di Programmazione**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework e SDK**: 
  - SDK MCP (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Database**: PostgreSQL con estensione pgvector
- **Piattaforme Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Strumenti di Build**: npm, Maven, pip, Cargo
- **Documentazione**: Markdown con traduzione automatizzata multilingue (oltre 48 lingue)

### Architettura

- **11 Moduli Core (00-11)**: Percorso formativo sequenziale dai fondamenti agli argomenti avanzati
- **Laboratori Pratici**: Esercizi pratici con codice soluzione completo in più linguaggi
- **Progetti di Esempio**: Implementazioni funzionali del server e client MCP
- **Sistema di Traduzione**: Workflow GitHub Actions automatizzato per supporto multilingue
- **Asset Immagini**: Directory immagini centralizzata con versioni tradotte

## Comandi di Configurazione

Questo è un repository focalizzato sulla documentazione. La maggior parte della configurazione avviene all'interno dei singoli progetti di esempio e dei laboratori.

### Configurazione del Repository

```bash
# Clona il repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Lavorare con i Progetti di Esempio

I progetti di esempio si trovano in:
- `03-GettingStarted/samples/` - Esempi specifici per linguaggio
- `03-GettingStarted/01-first-server/solution/` - Implementazioni del primo server
- `03-GettingStarted/02-client/solution/` - Implementazioni client
- `11-MCPServerHandsOnLabs/` - Laboratori completi di integrazione con database

Ogni progetto di esempio contiene proprie istruzioni di configurazione:

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
# o
pip install -e .
python main.py
```

#### Progetti Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Flusso di Lavoro per lo Sviluppo

### Prontezza MCP 7-28

#### Checklist di preparazione del repo

- [x] **Chiarezza per i nuovi contributori**: Questo file definisce lo scopo del repository,
  la struttura, le regole di contributo e i percorsi di configurazione degli esempi.
- [x] **Comandi build/test/lint con flag esatti**:
  - Lint della documentazione del repository:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Verifica del pattern dei link nella documentazione:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validazione esempio TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validazione esempio Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validazione esempio Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Un flusso di lavoro realistico che può diventare uno strumento MCP**:
  `validate_curriculum_change`
- [x] **Ingressi/uscite sono espliciti** (vedi specifica sotto).
- [x] **Permessi e modalità di errore sono documentate** (vedi specifica sotto).
- [x] **Testabilità in CI è esplicita** (comandi deterministici, codici di uscita espliciti,
  e output interpretabili da macchine).

#### Flusso di lavoro candidato come strumento MCP: `validate_curriculum_change`

##### Obiettivo

Validare la salute delle modifiche alla documentazione del curriculum e del codice di esempio rappresentativo
prima del merge.

##### Ingressi

- `changed_paths: string[]` (obbligatorio) - percorsi relativi modificati nel PR.
- `run_docs_lint: boolean` (default `true`)
- `run_links_audit: boolean` (default `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (default tutti `false`)

##### Uscite

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Permessi

- Lettura di file di workspace e scrittura di artefatti generati dallo strumento (ad es. rapporti di lint,
  log di test) solo; niente scritture in `translations/` o
  `translated_images/`.
- Esecuzione di comandi shell locali.
- Accesso di rete opzionale solo per il ripristino di pacchetti (`npm ci`,
  `python -m pip install`, risoluzione dipendenze `mvn`).
- Nessun permesso di push, merge o modifica in `translations/` o
  `translated_images/`.

##### Modalità di fallimento

- `E_NO_INPUT_PATHS`: `changed_paths` vuoto.
- `E_INVALID_PATH`: percorso di input fuori dal root del repository.
- `E_LINT_FAILED`: lint markdown esce con codice diverso da zero.
- `E_LINK_AUDIT_FAILED`: comando di audit link esce con codice diverso da zero.
- `E_SAMPLE_TEST_FAILED`: test/build esempio esce con codice diverso da zero.
- `E_TIMEOUT`: comando ha superato il timeout configurato.

##### Contratto raccomandato per CI

Per automatizzare la validazione, configura un job CI che:

- Si attivi su pull request che interessano `*.md`, codice di esempio, o questo file.
- Esegua i comandi esatti elencati sopra.
- Conservi i log come artefatti.
- Fallisca il job su qualsiasi codice di uscita diverso da zero.

#### Se distribuisci un server MCP da questo repo

- [ ] Leggi il changelog di bozza per MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Testa il tuo server contro le beta SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Rimuovi assunzioni di sessione e handshake; tratta ogni richiesta come
  autonoma:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Invia gli header `Mcp-Method` e `Mcp-Name` per richieste HTTP raw:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Verifica i codici di errore hardcoded (`missing resource` spostato da `-32002` a `-32602`).

- [ ] Segnalare e pianificare la migrazione per radici deprecate, campionamento e
  registrazione:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrare dall’API sperimentale `2025-11-25` Tasks:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Revisionare l'autorizzazione per il rafforzamento di OAuth e OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Struttura della Documentazione

- **Moduli 00-11**: Contenuto del curriculum core in ordine sequenziale
- **translations/**: Versioni specifiche per lingua (auto-generate, non modificare direttamente)
- **translated_images/**: Versioni di immagini localizzate (auto-generate)
- **images/**: Immagini e diagrammi sorgente

### Come Apportare Modifiche alla Documentazione

1. Modificare solo i file markdown in inglese nelle directory dei moduli root (00-11)
2. Aggiornare immagini nella cartella `images/` se necessario
3. L'Action GitHub co-op-translator genererà automaticamente le traduzioni
4. Le traduzioni vengono rigenerate al push sul ramo principale

### Lavorare con le Traduzioni

- **Traduzione automatica**: Il flusso di lavoro GitHub Actions gestisce tutte le traduzioni
- **NON modificare manualmente** i file nella cartella `translations/`
- I metadati delle traduzioni sono incorporati in ogni file tradotto
- Lingue supportate: più di 48 lingue, incluso arabo, cinese, francese, tedesco, hindi, giapponese, coreano, portoghese, russo, spagnolo e molte altre

## Istruzioni per i Test

### Validazione della Documentazione

Poiché questo è principalmente un repository di documentazione, i test si concentrano su:

1. **Audit dei link**: Elenco dei link Markdown per la revisione

   ```bash
   # Elenca i link Markdown (verifica del modello)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Convalida degli esempi di codice**: Verificare che gli esempi di codice compilino/eseguano

   ```bash
   # Naviga al campione specifico ed esegui i suoi test
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting del Markdown**: Controllare la coerenza del formato

   ```bash
   # Usa markdownlint se necessario
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Test dei Progetti di Esempio

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
- Includere esempi di codice in più lingue quando applicabile
- Seguire le migliori pratiche del markdown:
  - Usare intestazioni in stile ATX (sintassi `#`)
  - Usare blocchi di codice delimitati con identificatori di linguaggio
  - Includere testo alternativo descrittivo per le immagini
  - Mantenere una lunghezza ragionevole delle righe (nessun limite rigido, ma essere sensati)

### Stile degli Esempi di Codice

#### TypeScript/JavaScript
- Usare moduli ES (`import`/`export`)
- Seguire le convenzioni della modalità rigorosa di TypeScript
- Includere annotazioni di tipo
- Target ES2022

#### Python
- Seguire le linee guida di stile PEP 8
- Usare suggerimenti di tipo quando appropriato
- Includere docstring per funzioni e classi
- Usare funzionalità Python moderne (3.8+)

#### Java
- Seguire le convenzioni di Spring Boot
- Usare funzionalità Java 21
- Seguire la struttura standard dei progetti Maven
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

Il repository utilizza GitHub Pages o simili per l’hosting della documentazione (se applicabile). Le modifiche al ramo principale attivano:

1. Flusso di lavoro per la traduzione (`.github/workflows/co-op-translator.yml`)
2. Traduzione automatica di tutti i file markdown in inglese
3. Localizzazione delle immagini quando necessario

### Nessun Processo di Compilazione Richiesto

Questo repository contiene principalmente documentazione in markdown. Non è necessaria una fase di compilazione o build per il contenuto del curriculum core.

### Distribuzione dei Progetti di Esempio

I singoli progetti di esempio possono avere istruzioni di distribuzione:
- Vedere `03-GettingStarted/09-deployment/` per indicazioni sulla distribuzione del server MCP
- Esempi di distribuzione Azure Container Apps in `11-MCPServerHandsOnLabs/`

## Linee Guida per i Contributi

### Processo di Pull Request

1. **Fork e Clona**: Effettuare il fork del repository e clonare il proprio fork localmente
2. **Creare un Branch**: Usare nomi descrittivi per il branch (es. `fix/typo-module-3`, `add/python-example`)
3. **Apportare Modifiche**: Modificare solo i file markdown in inglese (non le traduzioni)
4. **Testare Localmente**: Verificare che il markdown venga renderizzato correttamente
5. **Inviare PR**: Usare titoli e descrizioni chiari nella PR
6. **CLA**: Firmare il Microsoft Contributor License Agreement quando richiesto

### Formato del Titolo PR

Usare titoli chiari e descrittivi:
- `[Module XX] Descrizione breve` per modifiche specifiche ai moduli
- `[Samples] Descrizione` per modifiche al codice di esempio
- `[Docs] Descrizione` per aggiornamenti generali alla documentazione

### Cosa Contribuire

- Correzioni di bug nella documentazione o negli esempi di codice
- Nuovi esempi di codice in lingue aggiuntive
- Chiarimenti e miglioramenti ai contenuti esistenti
- Nuovi casi di studio o esempi pratici
- Segnalazioni di problemi per contenuti poco chiari o errati

### Cosa NON Fare

- Non modificare direttamente i file nella cartella `translations/`
- Non modificare la cartella `translated_images/`
- Non aggiungere file binari di grandi dimensioni senza discussione
- Non modificare i file del flusso di lavoro per la traduzione senza coordinamento

## Note Aggiuntive

### Manutenzione del Repository

- **Changelog**: Tutte le modifiche importanti sono documentate in `changelog.md`
- **Guida allo Studio**: Usare `study_guide.md` per una panoramica della navigazione nel curriculum
- **Template per Issue**: Usare i template GitHub per segnalazioni di bug e richieste di funzionalità
- **Codice di Condotta**: Tutti i contributori devono rispettare il Microsoft Open Source Code of Conduct

### Percorso di Apprendimento

Seguire i moduli in ordine sequenziale (00-11) per un apprendimento ottimale:
1. **00-02**: Fondamenti (Introduzione, Concetti Core, Sicurezza)
2. **03**: Introduzione pratica con implementazione hands-on
3. **04-05**: Implementazione pratica e argomenti avanzati
4. **06-10**: Comunità, best practice e applicazioni reali
5. **11**: Laboratori completi di integrazione database (13 laboratori sequenziali)

### Risorse di Supporto

- **Documentazione**: https://modelcontextprotocol.io/
- **Specifiche**: https://spec.modelcontextprotocol.io/
- **Comunità**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Server Microsoft Foundry Discord
- **Corsi Correlati**: Vedere README.md per altri percorsi di apprendimento Microsoft

### Risoluzione Problemi Comuni

**D: La mia PR fallisce il controllo della traduzione**
R: Assicurarsi di aver modificato solo i file markdown in inglese nelle directory dei moduli root, non le versioni tradotte.

**D: Come aggiungo una nuova lingua?**
R: Il supporto linguistico è gestito tramite il flusso di lavoro co-op-translator. Aprire una issue per discutere l'aggiunta di nuove lingue.

**D: Gli esempi di codice non funzionano**

R: Assicurati di aver seguito le istruzioni di configurazione nel README del campione specifico. Verifica di avere le versioni corrette delle dipendenze installate.

**D: Le immagini non vengono visualizzate**
R: Verifica che i percorsi delle immagini siano relativi e utilizzino le barre oblique (/). Le immagini dovrebbero trovarsi nella directory `images/` o `translated_images/` per le versioni localizzate.

### Considerazioni sulle prestazioni

- Il flusso di lavoro di traduzione può richiedere diversi minuti per essere completato
- Le immagini di grandi dimensioni dovrebbero essere ottimizzate prima di essere inviate
- Mantieni i singoli file markdown focalizzati e di dimensioni ragionevoli
- Usa link relativi per una migliore portabilità

### Governance del progetto

Questo progetto segue le pratiche open source di Microsoft:
- Licenza MIT per codice e documentazione
- Codice di Condotta Open Source Microsoft
- CLA richiesta per i contributi
- Problemi di sicurezza: segui le linee guida di SECURITY.md
- Supporto: consulta SUPPORT.md per risorse di aiuto

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->