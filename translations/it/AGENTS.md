# AGENTS.md

## Panoramica del Progetto

**MCP for Beginners** è un curriculum educativo open-source per apprendere il Model Context Protocol (MCP) - un framework standardizzato per le interazioni tra modelli di intelligenza artificiale e applicazioni client. Questo repository fornisce materiali di apprendimento completi con esempi di codice pratici in diversi linguaggi di programmazione.

### Tecnologie Chiave

- **Linguaggi di Programmazione**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Database**: PostgreSQL con estensione pgvector
- **Piattaforme Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Strumenti di Build**: npm, Maven, pip, Cargo
- **Documentazione**: Markdown con traduzione automatica in più lingue (48+ lingue)

### Architettura

- **11 Moduli Core (00-11)**: Percorso di apprendimento sequenziale dai fondamenti agli argomenti avanzati
- **Laboratori Pratici**: Esercizi pratici con codice di soluzione completo in più linguaggi
- **Progetti di Esempio**: Implementazioni funzionanti di server e client MCP
- **Sistema di Traduzione**: Workflow automatizzato di GitHub Actions per il supporto multilingue
- **Risorse Immagini**: Directory centralizzata di immagini con versioni tradotte

## Comandi di Configurazione

Questo è un repository incentrato sulla documentazione. La maggior parte della configurazione avviene all'interno dei singoli progetti di esempio e laboratori.

### Configurazione del Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Lavorare con i Progetti di Esempio

I progetti di esempio si trovano in:
- `03-GettingStarted/samples/` - Esempi specifici per linguaggio
- `03-GettingStarted/01-first-server/solution/` - Implementazioni del primo server
- `03-GettingStarted/02-client/solution/` - Implementazioni del client
- `11-MCPServerHandsOnLabs/` - Laboratori completi di integrazione con database

Ogni progetto di esempio contiene istruzioni di configurazione proprie:

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
# or
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

### Struttura della Documentazione

- **Moduli 00-11**: Contenuti del curriculum core in ordine sequenziale
- **translations/**: Versioni specifiche per lingua (generate automaticamente, non modificare direttamente)
- **translated_images/**: Versioni localizzate delle immagini (generate automaticamente)
- **images/**: Immagini e diagrammi di origine

### Modificare la Documentazione

1. Modificare solo i file markdown in inglese nelle directory dei moduli principali (00-11)
2. Aggiornare le immagini nella directory `images/` se necessario
3. L'azione GitHub co-op-translator genererà automaticamente le traduzioni
4. Le traduzioni vengono rigenerate al push sul branch principale

### Lavorare con le Traduzioni

- **Traduzione Automatica**: Il workflow di GitHub Actions gestisce tutte le traduzioni
- **NON modificare manualmente** i file nella directory `translations/`
- I metadati di traduzione sono incorporati in ogni file tradotto
- Lingue supportate: 48+ lingue tra cui arabo, cinese, francese, tedesco, hindi, giapponese, coreano, portoghese, russo, spagnolo e molte altre

## Istruzioni per il Testing

### Validazione della Documentazione

Poiché questo è principalmente un repository di documentazione, il testing si concentra su:

1. **Validazione dei Link**: Verificare che tutti i link interni funzionino
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validazione degli Esempi di Codice**: Testare che gli esempi di codice si compilino/eseguano
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting Markdown**: Controllare la coerenza del formato
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testing dei Progetti di Esempio

Ogni esempio specifico per linguaggio include il proprio approccio di testing:

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
- Includere esempi di codice in più linguaggi dove applicabile
- Seguire le migliori pratiche per il markdown:
  - Usare intestazioni in stile ATX (`#` sintassi)
  - Usare blocchi di codice delimitati con identificatori di linguaggio
  - Includere testo alternativo descrittivo per le immagini
  - Mantenere lunghezze di riga ragionevoli (senza limite rigido, ma sensato)

### Stile degli Esempi di Codice

#### TypeScript/JavaScript
- Usare moduli ES (`import`/`export`)
- Seguire le convenzioni della modalità rigorosa di TypeScript
- Includere annotazioni di tipo
- Target ES2022

#### Python
- Seguire le linee guida di stile PEP 8
- Usare suggerimenti di tipo dove appropriato
- Includere docstring per funzioni e classi
- Usare funzionalità moderne di Python (3.8+)

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

## Build e Deployment

### Deployment della Documentazione

Il repository utilizza GitHub Pages o simili per l'hosting della documentazione (se applicabile). Le modifiche al branch principale attivano:

1. Workflow di traduzione (`.github/workflows/co-op-translator.yml`)
2. Traduzione automatica di tutti i file markdown in inglese
3. Localizzazione delle immagini se necessario

### Nessun Processo di Build Necessario

Questo repository contiene principalmente documentazione markdown. Non è necessario alcun passaggio di compilazione o build per i contenuti del curriculum core.

### Deployment dei Progetti di Esempio

I singoli progetti di esempio possono avere istruzioni di deployment:
- Vedere `03-GettingStarted/09-deployment/` per le indicazioni sul deployment del server MCP
- Esempi di deployment su Azure Container Apps in `11-MCPServerHandsOnLabs/`

## Linee Guida per i Contributi

### Processo di Pull Request

1. **Fork e Clone**: Effettuare il fork del repository e clonare il proprio fork localmente
2. **Creare un Branch**: Usare nomi di branch descrittivi (es. `fix/typo-module-3`, `add/python-example`)
3. **Apportare Modifiche**: Modificare solo i file markdown in inglese (non le traduzioni)
4. **Testare Localmente**: Verificare che il markdown venga renderizzato correttamente
5. **Inviare PR**: Usare titoli e descrizioni chiari per la PR
6. **CLA**: Firmare il Microsoft Contributor License Agreement quando richiesto

### Formato del Titolo della PR

Usare titoli chiari e descrittivi:
- `[Module XX] Breve descrizione` per modifiche specifiche ai moduli
- `[Samples] Descrizione` per modifiche al codice di esempio
- `[Docs] Descrizione` per aggiornamenti generali alla documentazione

### Cosa Contribuire

- Correzioni di bug nella documentazione o negli esempi di codice
- Nuovi esempi di codice in lingue aggiuntive
- Chiarimenti e miglioramenti ai contenuti esistenti
- Nuovi casi studio o esempi pratici
- Segnalazioni di problemi per contenuti poco chiari o errati

### Cosa NON Fare

- Non modificare direttamente i file nella directory `translations/`
- Non modificare la directory `translated_images/`
- Non aggiungere file binari di grandi dimensioni senza discussione
- Non modificare i file del workflow di traduzione senza coordinamento

## Note Aggiuntive

### Manutenzione del Repository

- **Changelog**: Tutte le modifiche significative sono documentate in `changelog.md`
- **Guida allo Studio**: Usare `study_guide.md` per una panoramica della navigazione del curriculum
- **Template per i Problemi**: Usare i template di GitHub per segnalazioni di bug e richieste di funzionalità
- **Codice di Condotta**: Tutti i contributori devono seguire il Microsoft Open Source Code of Conduct

### Percorso di Apprendimento

Seguire i moduli in ordine sequenziale (00-11) per un apprendimento ottimale:
1. **00-02**: Fondamenti (Introduzione, Concetti Core, Sicurezza)
2. **03**: Introduzione con implementazione pratica
3. **04-05**: Implementazione pratica e argomenti avanzati
4. **06-10**: Comunità, migliori pratiche e applicazioni reali
5. **11**: Laboratori completi di integrazione con database (13 laboratori sequenziali)

### Risorse di Supporto

- **Documentazione**: https://modelcontextprotocol.io/
- **Specifiche**: https://spec.modelcontextprotocol.io/
- **Comunità**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Server Discord Microsoft Azure AI Foundry
- **Corsi Correlati**: Vedere README.md per altri percorsi di apprendimento Microsoft

### Risoluzione dei Problemi Comuni

**D: La mia PR non supera il controllo di traduzione**
R: Assicurarsi di aver modificato solo i file markdown in inglese nelle directory dei moduli principali, non le versioni tradotte.

**D: Come posso aggiungere una nuova lingua?**
R: Il supporto linguistico è gestito tramite il workflow co-op-translator. Aprire un problema per discutere l'aggiunta di nuove lingue.

**D: Gli esempi di codice non funzionano**
R: Assicurarsi di aver seguito le istruzioni di configurazione nel README specifico dell'esempio. Verificare di avere le versioni corrette delle dipendenze installate.

**D: Le immagini non vengono visualizzate**
R: Verificare che i percorsi delle immagini siano relativi e utilizzino barre oblique. Le immagini devono essere nella directory `images/` o `translated_images/` per le versioni localizzate.

### Considerazioni sulle Prestazioni

- Il workflow di traduzione può richiedere diversi minuti per completarsi
- Le immagini di grandi dimensioni devono essere ottimizzate prima di essere commesse
- Mantenere i singoli file markdown focalizzati e di dimensioni ragionevoli
- Usare link relativi per una migliore portabilità

### Governance del Progetto

Questo progetto segue le pratiche open source di Microsoft:
- Licenza MIT per codice e documentazione
- Microsoft Open Source Code of Conduct
- CLA richiesto per i contributi
- Problemi di sicurezza: Seguire le linee guida di SECURITY.md
- Supporto: Vedere SUPPORT.md per risorse di aiuto

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.