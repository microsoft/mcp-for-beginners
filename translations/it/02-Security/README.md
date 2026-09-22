# Sicurezza MCP: Protezione Completa per Sistemi AI

[![Migliori Pratiche di Sicurezza MCP](../../../translated_images/it/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Clicca sull'immagine sopra per vedere il video di questa lezione)_

La sicurezza è fondamentale nella progettazione di sistemi AI, ed è per questo che la consideriamo come nostra seconda sezione. Questo è in linea con il principio **Secure by Design** di Microsoft dalla [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Il Model Context Protocol (MCP) introduce potenti nuove capacità nelle applicazioni basate su AI, pur presentando sfide di sicurezza uniche che vanno oltre i rischi software tradizionali. I sistemi MCP affrontano sia preoccupazioni di sicurezza consolidate (codifica sicura, minimo privilegio, sicurezza della supply chain) sia nuove minacce specifiche per l'AI, inclusi prompt injection, avvelenamento degli strumenti, session hijacking, attacchi confused deputy, vulnerabilità di token passthrough e modifiche dinamiche delle capacità.

Questa lezione esplora i rischi di sicurezza più critici nelle implementazioni MCP—coprendo autenticazione, autorizzazione, permessi eccessivi, prompt injection indiretta, sicurezza della sessione, problemi di confused deputy, gestione dei token e vulnerabilità nella supply chain. Imparerai controlli praticabili e migliori pratiche per mitigare questi rischi sfruttando soluzioni Microsoft come Prompt Shields, Azure Content Safety e GitHub Advanced Security per rafforzare il tuo deployment MCP.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- **Identificare Minacce Specifiche MCP**: Riconoscere rischi unici in sistemi MCP tra cui prompt injection, avvelenamento strumenti, permessi eccessivi, session hijacking, problemi di confused deputy, vulnerabilità di token passthrough e rischi della supply chain
- **Applicare Controlli di Sicurezza**: Implementare mitigazioni efficaci tra cui autenticazione robusta, accesso a minimo privilegio, gestione sicura dei token, controlli di sicurezza della sessione e verifica della supply chain
- **Sfruttare Soluzioni di Sicurezza Microsoft**: Comprendere e distribuire Microsoft Prompt Shields, Azure Content Safety e GitHub Advanced Security per la protezione del carico di lavoro MCP
- **Validare la Sicurezza degli Strumenti**: Riconoscere l'importanza della validazione dei metadati degli strumenti, monitorare modifiche dinamiche e difendersi da attacchi di prompt injection indiretti
- **Integrare le Best Practice**: Combinare fondamentali di sicurezza consolidati (codifica sicura, hardening server, zero trust) con controlli specifici MCP per una protezione completa

# Architettura e Controlli di Sicurezza MCP

Le implementazioni moderne MCP richiedono approcci di sicurezza stratificata che affrontino sia la sicurezza software tradizionale che le minacce specifiche per l'AI. La specifica MCP in rapida evoluzione matura continuamente i suoi controlli di sicurezza, permettendo una migliore integrazione con architetture di sicurezza aziendali e migliori pratiche consolidate.

La ricerca dal [Microsoft Digital Defense Report](https://aka.ms/mddr) dimostra che **il 98% delle violazioni segnalate sarebbe prevenuto da una robusta igiene della sicurezza**. La strategia di protezione più efficace combina pratiche di sicurezza fondamentali con controlli specifici MCP—misure di sicurezza di base comprovate rimangono le più impattanti per ridurre il rischio complessivo.

## Scenario di Sicurezza Attuale

> **Nota:** Questo capitolo combina controlli di sicurezza MCP consolidati con le
> attuali linee guida di autorizzazione **MCP Specification 2026-07-28**. Fare sempre riferimento
> alla [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [repository MCP su GitHub](https://github.com/modelcontextprotocol), e
> alla [documentazione delle migliori pratiche di sicurezza](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> quando si implementa codice sensibile alla sicurezza.

> **Aggiornamento Autorizzazione:** MCP `2026-07-28` richiede ai client di validare il
> parametro `iss` nelle risposte di autorizzazione (RFC 9207) e vincolare le credenziali registrate
> al server di autorizzazione che le emette. Dynamic Client Registration
> è deprecato; le nuove implementazioni dovrebbero usare i Documenti Metadata Client ID.
> Vedi [Novità in MCP: Specifica 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> per l'elenco completo delle modifiche all'autorizzazione.

## 🏔️ Workshop MCP Security Summit (Sherpa)

Per una **formazione pratica sulla sicurezza**, consigliamo fortemente il **MCP Security Summit Workshop** (Sherpa) - una spedizione guidata completa per mettere in sicurezza server MCP in Microsoft Azure.

### Panoramica del Workshop

Il [MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) offre formazione pratica e applicabile sulla sicurezza tramite una metodologia collaudata "vulnerabile → exploit → correggi → valida". Potrai:

- **Imparare Rompendo le Cose**: Sperimentare vulnerabilità manipolando server intenzionalmente insicuri
- **Utilizzare la Sicurezza Nativa di Azure**: Sfruttare Azure Entra ID, Key Vault, API Management e AI Content Safety
- **Seguire la Difesa in Profondità**: Procedere attraverso i campi creando strati completi di sicurezza
- **Applicare gli Standard OWASP**: Ogni tecnica è mappata alla [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Ricevere Codice di Produzione**: Ottenere implementazioni funzionanti e testate

### Itinerario della Spedizione

| Campo | Focus | Rischi OWASP Coperti |
|------|-------|---------------------|
| **Campo Base** | Fondamenti MCP e vulnerabilità di autenticazione | MCP01, MCP07 |
| **Campo 1: Identità** | OAuth 2.1, Managed Identity Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Campo 2: Gateway** | API Management, Endpoint Privati, governance | MCP02, MCP06, MCP07, MCP09 |
| **Campo 3: Sicurezza I/O** | Prompt injection, protezione PII, content safety | MCP03, MCP05, MCP06, MCP10 |
| **Campo 4: Monitoraggio** | Log Analytics, dashboard, rilevamento minacce | MCP04, MCP08 |
| **La Vettta** | Test integrazione Red Team / Blue Team | Tutti |

**Inizia Qui**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 Rischi di Sicurezza

La [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) dettaglia i dieci rischi di sicurezza più critici per le implementazioni MCP:

| Rischio | Descrizione | Mitigazione Azure |
|------|-------------|------------------|
| **MCP01** | Cattiva Gestione Token & Esposizione Segreti | Azure Key Vault, Managed Identity |
| **MCP02** | Escalation di Privilegio via Scope Creep | RBAC, Accesso Condizionale |
| **MCP03** | Avvelenamento Strumenti | Validazione strumenti, verifica integrità |
| **MCP04** | Attacchi supply chain software & Manomissione dipendenze | GitHub Advanced Security, scansione dipendenze |
| **MCP05** | Command Injection & Esecuzione | Validazione input, sandboxing |
| **MCP06** | Sottversione del Flusso d'Intento | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Autenticazione & Autorizzazione insufficienti | Azure Entra ID, OAuth 2.1 con PKCE |
| **MCP08** | Mancanza di Audit e Telemetria | Azure Monitor, Application Insights |
| **MCP09** | Server MCP Ombra | Governance API Center, isolamento rete |
| **MCP10** | Context Injection & Over-Sharing | Classificazione dati, esposizione minima |

### Evoluzione dell'Autenticazione MCP

La specifica MCP è evoluta significativamente nel suo approccio ad autenticazione e autorizzazione:

- **Approccio Originale**: Specifiche iniziali richiedevano agli sviluppatori di implementare server di autenticazione personalizzati, con i server MCP come OAuth 2.0 Authorization Server che gestivano direttamente l'autenticazione utenti
- **Standard Attuale (`2026-07-28`)**: I server MCP possono delegare l'autenticazione
  a provider di identità esterni come Microsoft Entra ID. I client devono anche
  applicare i requisiti attuali di validazione dell'emittente e binding delle credenziali.
- **Transport Layer Security**: Supporto migliorato per meccanismi di trasporto sicuri con pattern di autenticazione appropriati per connessioni locali (STDIO) e remote (Streamable HTTP)

## Sicurezza di Autenticazione & Autorizzazione

### Sfide Attuali di Sicurezza

Le implementazioni moderne MCP affrontano diverse sfide di autenticazione e autorizzazione:

### Rischi & Vettori di Minaccia

- **Logica di Autorizzazione Errata**: Implementazioni difettose dell'autorizzazione nei server MCP possono esporre dati sensibili e applicare in modo errato i controlli accesso
- **Compromissione Token OAuth**: Furto di token del server MCP locale permette agli attaccanti di impersonare server e accedere a servizi a valle
- **Vulnerabilità Token Passthrough**: Gestione impropria dei token crea bypass dei controlli di sicurezza e lacune di responsabilità
- **Permessi Eccessivi**: Server MCP sovra-privilegiati violano il principio del minimo privilegio e ampliano le superfici di attacco

#### Token Passthrough: Un Anti-Pattern Critico

**Il token passthrough è esplicitamente vietato** nella specifica di autorizzazione MCP attuale a causa di gravi implicazioni di sicurezza:

##### Circumvenzione dei Controlli di Sicurezza
- I server MCP e le API a valle implementano controlli di sicurezza critici (rate limiting, validazione richieste, monitoraggio traffico) che dipendono dalla corretta validazione dei token
- L'uso diretto di token da client verso API bypassa queste protezioni essenziali, minando l'architettura di sicurezza

##### Sfide di Responsabilità & Audit   
- I server MCP non possono distinguere fra i client che usano token emessi a monte, interrompendo le tracce di audit
- I log di server risorse a valle mostrano origini richieste fuorvianti invece che intermediari server MCP reali
- L'investigazione degli incidenti e le verifiche di conformità diventano significativamente più difficili

##### Rischi di Esfiltrazione Dati
- Reclami di token non validati permettono ad attori malintenzionati con token rubati di usare server MCP come proxy per l'esfiltrazione dati
- Violazioni del confine di fiducia permettono schemi di accesso non autorizzati che bypassano controlli di sicurezza previsti

##### Vettori di Attacco Multi-Servizio
- Token compromessi accettati da più servizi permettono movimenti laterali attraverso sistemi connessi
- Le assunzioni di fiducia tra servizi possono essere violate quando l'origine del token non può essere verificata

### Controlli di Sicurezza & Mitigazioni

**Requisiti Critici di Sicurezza:**

> **OBBLIGATORIO**: I server MCP **NON DEVONO** accettare alcun token che non sia stato esplicitamente emesso per il server MCP

#### Controlli di Autenticazione & Autorizzazione

- **Revisione Rigorosa Autorizzazione**: Condurre audit completi della logica di autorizzazione dei server MCP per garantire che solo utenti e client previsti possano accedere a risorse sensibili
  - **Guida all'Implementazione**: [Azure API Management come Gateway di Autenticazione per Server MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrazione Identità**: [Usare Microsoft Entra ID per Autenticazione Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestione Sicura dei Token**: Implementare le [migliori pratiche di Microsoft per validazione e ciclo di vita del token](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validare che i reclami audience dei token corrispondano all'identità del server MCP
  - Implementare corrette politiche di rotazione ed scadenza dei token
  - Prevenire replay dei token e usi non autorizzati

- **Archiviazione Protetta dei Token**: Conservare token in modo sicuro con crittografia a riposo e in transito
  - **Migliori Pratiche**: [Linee guida per archiviazione sicura e crittografia dei token](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementazione del Controllo Accesso

- **Principio del Minimo Privilegio**: Concedere ai server MCP solo i permessi minimi necessari per la funzionalità prevista
  - Revisioni regolari dei permessi e aggiornamenti per prevenire l'ampliamento involontario
  - **Documentazione Microsoft**: [Accesso Sicuro con Minimi Privilegi](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Controllo Accesso Basato su Ruolo (RBAC)**: Implementare assegnazioni di ruoli granulare
  - Applicare ruoli strettamente a risorse e azioni specifiche
  - Evitare permessi ampi o non necessari che aumentano la superficie di attacco

- **Monitoraggio Continuo dei Permessi**: Implementare auditing e monitoraggio dell'accesso continuo
  - Monitorare modelli di uso dei permessi per anomalie
  - Correggere tempestivamente privilegi eccessivi o inutilizzati

## Minacce di Sicurezza Specifiche per AI

### Attacchi di Prompt Injection & Manipolazione degli Strumenti

Le implementazioni MCP moderne affrontano vettori di attacco AI sofisticati che le misure di sicurezza tradizionali non possono completamente gestire:

#### **Prompt Injection Indiretta (Cross-Domain Prompt Injection)**

La **Prompt Injection Indiretta** rappresenta una delle vulnerabilità più critiche nei sistemi AI abilitati MCP. Gli attaccanti inseriscono istruzioni dannose all'interno di contenuti esterni—documenti, pagine web, email o fonti di dati—che i sistemi AI successivamente elaborano come comandi legittimi.

**Scenari d'Attacco:**
- **Iniezione basata su Documenti**: Istruzioni dannose nascoste in documenti elaborati che causano azioni AI indesiderate
- **Sfruttamento Contenuti Web**: Pagine web compromesse contenenti prompt incorporati che manipolano il comportamento AI se scraping
- **Attacchi via Email**: Prompt malevoli in email che fanno sì che assistenti AI perdano informazioni o eseguano azioni non autorizzate
- **Contaminazione delle Fonti Dati**: Database o API compromessi che forniscono contenuti contaminati ai sistemi AI

**Impatto nel Mondo Reale**: Questi attacchi possono causare esfiltrazione dati, violazioni della privacy, generazione di contenuti dannosi e manipolazione delle interazioni utente. Per analisi dettagliate, vedi [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagramma Attacco Prompt Injection](../../../translated_images/it/prompt-injection.ed9fbfde297ca877.webp)

#### **Attacchi di Avvelenamento degli Strumenti**

L'**Avvelenamento degli Strumenti** prende di mira i metadati che definiscono gli strumenti MCP, sfruttando come i grandi modelli di linguaggio interpretano descrizioni e parametri degli strumenti per prendere decisioni di esecuzione.

**Meccanismi d'Attacco:**
- **Manipolazione Metadati**: Gli attaccanti inseriscono istruzioni dannose nelle descrizioni degli strumenti, definizioni parametri o esempi di utilizzo
- **Istruzioni Invisibili**: Prompt nascosti nei metadati degli strumenti che vengono elaborati dai modelli AI ma sono invisibili agli utenti umani
- **Modifica Dinamica degli Strumenti ("Rug Pulls")**: Strumenti approvati dagli utenti successivamente modificati per compiere azioni malevole senza che l'utente ne sia consapevole
- **Iniezione Parametri**: Contenuti dannosi incorporati nei parametri degli strumenti che influenzano il comportamento del modello


**Rischi dei Server Ospitati**: I server MCP remoti presentano rischi elevati poiché le definizioni degli strumenti possono essere aggiornate dopo l'approvazione iniziale dell'utente, creando scenari in cui strumenti precedentemente sicuri diventano dannosi. Per un'analisi completa, vedere [Attacchi di Avvelenamento degli Strumenti (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagramma Attacco di Iniezione di Strumenti](../../../translated_images/it/tool-injection.3b0b4a6b24de6bef.webp)

#### **Ulteriori Vettori di Attacco AI**

- **Iniezione di Prompt Cross-Dominio (XPIA)**: Attacchi sofisticati che sfruttano contenuti da più domini per eludere i controlli di sicurezza
- **Modifica Dinamica delle Capacità**: Cambiamenti in tempo reale nelle capacità degli strumenti che sfuggono alle valutazioni di sicurezza iniziali
- **Avvelenamento della Finestra di Contesto**: Attacchi che manipolano grandi finestre di contesto per nascondere istruzioni dannose
- **Attacchi di Confusione del Modello**: Sfruttamento dei limiti del modello per creare comportamenti imprevedibili o non sicuri


### Impatto dei Rischi di Sicurezza AI

**Conseguenze ad Alto Impatto:**
- **Esfiltrazione dei Dati**: Accesso non autorizzato e furto di dati sensibili aziendali o personali
- **Violazioni della Privacy**: Esposizione di informazioni identificabili personalmente (PII) e dati aziendali riservati  
- **Manipolazione del Sistema**: Modifiche non intenzionali a sistemi critici e flussi di lavoro
- **Furto delle Credenziali**: Compromissione di token di autenticazione e credenziali di servizio
- **Movimento Laterale**: Uso di sistemi AI compromessi come pivot per attacchi più ampi alla rete

### Soluzioni di Sicurezza AI di Microsoft

#### **AI Prompt Shields: Protezione Avanzata contro Attacchi di Iniezione**

Microsoft **AI Prompt Shields** fornisce una difesa completa contro attacchi di iniezione di prompt diretti e indiretti tramite molteplici livelli di sicurezza:

##### **Meccanismi di Protezione Principali:**

1. **Rilevamento Avanzato & Filtraggio**
   - Algoritmi di machine learning e tecniche NLP rilevano istruzioni dannose in contenuti esterni
   - Analisi in tempo reale di documenti, pagine web, email e fonti dati per minacce incorporate
   - Comprensione contestuale di pattern di prompt legittimi vs. maligni

2. **Tecniche di Spotlighting**  
   - Distingue tra istruzioni di sistema attendibili e input esterni potenzialmente compromessi
   - Metodi di trasformazione del testo che migliorano la rilevanza del modello isolando i contenuti dannosi
   - Aiuta i sistemi AI a mantenere la giusta gerarchia delle istruzioni e ignorare comandi iniettati

3. **Sistemi di Delimitazione & Marcatura Dati**
   - Definizione esplicita dei confini tra messaggi di sistema affidabili e testo di input esterno
   - Marcatori speciali evidenziano i confini tra fonti dati affidabili e non affidabili
   - Separazione chiara previene confusione tra istruzioni ed esecuzione non autorizzata di comandi

4. **Intelligence sulle Minacce Continua**
   - Microsoft monitora continuamente nuovi modelli di attacco e aggiorna le difese
   - Ricerca proattiva di minacce per nuove tecniche di iniezione e vettori di attacco
   - Aggiornamenti regolari dei modelli di sicurezza per mantenere efficacia contro minacce evolutive

5. **Integrazione con Azure Content Safety**
   - Parte della suite completa Azure AI Content Safety
   - Rilevamento aggiuntivo di tentativi di jailbreak, contenuti dannosi e violazioni di policy di sicurezza
   - Controlli di sicurezza unificati tra componenti applicativi AI

**Risorse di Implementazione**: [Documentazione Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Protezione Microsoft Prompt Shields](../../../translated_images/it/prompt-shield.ff5b95be76e9c78c.webp)


## Minacce Avanzate di Sicurezza MCP

### Vulnerabilità di Hijacking della Sessione

Il **session hijacking** rappresenta un vettore di attacco critico nelle implementazioni MCP stateful in cui parti non autorizzate ottengono e abusano di identificatori di sessione legittimi per impersonare client ed eseguire azioni non autorizzate.

#### **Scenari di Attacco & Rischi**

- **Iniezione di Prompt con Hijack di Sessione**: Attaccanti con ID di sessione rubati iniettano eventi dannosi in server che condividono lo stato della sessione, potenzialmente attivando azioni dannose o accedendo a dati sensibili
- **Impersonificazione Diretta**: ID di sessione rubati consentono chiamate dirette ai server MCP che bypassano l'autenticazione, trattando gli attaccanti come utenti legittimi
- **Flussi Riprendibili Compromessi**: Attaccanti possono terminare richieste prematuramente, causando clienti legittimi a riprendere con contenuti potenzialmente dannosi

#### **Controlli di Sicurezza per la Gestione della Sessione**

**Requisiti Critici:**
- **Verifica dell'Autorizzazione**: I server MCP che implementano l'autorizzazione **DEVONO** verificare TUTTE le richieste in ingresso e **NON DEVONO** affidarsi alle sessioni per l'autenticazione
- **Generazione Sicura di Sessioni**: Usare ID di sessione criptograficamente sicuri, non deterministici generati con generatori di numeri casuali sicuri
- **Vincolo Specifico per Utente**: Legare gli ID di sessione a informazioni specifiche dell'utente usando formati come `<user_id>:<session_id>` per prevenire abuso di sessione cross-utente
- **Gestione del Ciclo di Vita della Sessione**: Implementare scadenza, rotazione e invalidazione appropriate per limitare le finestre di vulnerabilità
- **Sicurezza di Trasporto**: HTTPS obbligatorio per tutte le comunicazioni per prevenire intercettazioni degli ID di sessione

### Problema del Deputato Confuso

Il **problema del deputato confuso** si verifica quando i server MCP agiscono da proxy di autenticazione tra client e servizi di terze parti, creando opportunità di bypass dell'autorizzazione attraverso lo sfruttamento di ID client statici.

#### **Meccaniche di Attacco & Rischi**

- **Bypass del Consenso Basato su Cookie**: L'autenticazione precedente dell'utente crea cookie di consenso che gli attaccanti sfruttano attraverso richieste di autorizzazione dannose con URI di reindirizzamento manipolati
- **Furto di Codice di Autorizzazione**: I cookie di consenso esistenti possono far sì che i server di autorizzazione saltino schermate di consenso, reindirizzando codici a endpoint controllati dagli attaccanti  
- **Accesso API Non Autorizzato**: Codici di autorizzazione rubati consentono lo scambio di token e l'impersonificazione dell'utente senza approvazione esplicita

#### **Strategie di Mitigazione**

**Controlli Obbligatori:**
- **Requisiti di Consenso Esplicito**: I server proxy MCP che usano ID client statici **DEVONO** ottenere il consenso dell'utente per ciascun client registrato dinamicamente
- **Implementazione della Sicurezza OAuth 2.1**: Seguire le migliori pratiche di sicurezza OAuth correnti, incluso PKCE (Proof Key for Code Exchange) per tutte le richieste di autorizzazione
- **Validazione Rigorosa dei Client**: Implementare una validazione rigorosa degli URI di reindirizzamento e degli identificatori client per prevenire sfruttamenti

### Vulnerabilità di Token Passthrough  

Il **token passthrough** rappresenta un anti-pattern esplicito in cui i server MCP accettano token client senza una valida convalida e li inoltrano a API downstream, violando le specifiche di autorizzazione MCP.

#### **Implicazioni di Sicurezza**

- **Fuga di Controllo**: L'uso diretto di token da client ad API bypassa controlli critici di limitazione della frequenza, validazione e monitoraggio
- **Corruzione della Traccia di Audit**: I token emessi a monte rendono impossibile l'identificazione del client, compromettendo la capacità di indagine degli incidenti
- **Esfiltrazione Dati via Proxy**: Token non convalidati consentono ad attori dannosi di usare server come proxy per accessi dati non autorizzati
- **Violazioni dei Confini di Fiducia**: Le assunzioni di fiducia dei servizi downstream possono essere violate quando le origini dei token non possono essere verificate
- **Espansione degli Attacchi Multi-Servizio**: Token compromessi accettati su più servizi abilitano movimenti laterali

#### **Controlli di Sicurezza Richiesti**

**Requisiti Non Negoziaibili:**
- **Validazione dei Token**: I server MCP **NON DEVONO** accettare token non esplicitamente emessi per il server MCP
- **Verifica dell'Audience**: Validare sempre che i claim dell’audience del token corrispondano all’identità del server MCP
- **Corretta Gestione del Ciclo di Vita del Token**: Implementare token di accesso a breve durata con pratiche di rotazione sicura


## Sicurezza della Catena di Fornitura per Sistemi AI

La sicurezza della catena di fornitura si è evoluta oltre le tradizionali dipendenze software per includere l'intero ecosistema AI. Le implementazioni MCP moderne devono verificare e monitorare rigorosamente tutti i componenti AI correlati, poiché ciascuno introduce potenziali vulnerabilità che potrebbero compromettere l'integrità del sistema.

### Componenti Estesi della Catena di Fornitura AI

**Dipendenze Software Tradizionali:**
- Librerie e framework open-source
- Immagini container e sistemi base  
- Strumenti di sviluppo e pipeline di build
- Componenti e servizi infrastrutturali

**Elementi Specifici della Catena di Fornitura AI:**
- **Modelli Foundation**: Modelli pre-addestrati da vari fornitori che richiedono verifica della provenienza
- **Servizi di Embedding**: Servizi esterni di vettorizzazione e ricerca semantica
- **Provider di Contesto**: Fonti di dati, basi di conoscenza e repository di documenti  
- **API di Terzi**: Servizi AI esterni, pipeline ML e endpoint di elaborazione dati
- **Artifact dei Modelli**: Pesi, configurazioni e varianti di modelli fine-tuned
- **Fonti di Dati di Addestramento**: Dataset usati per addestramento e affinamento dei modelli

### Strategia Completa di Sicurezza della Catena di Fornitura

#### **Verifica dei Componenti & Fiducia**
- **Validazione della Provenienza**: Verificare origine, licenza e integrità di tutti i componenti AI prima dell'integrazione
- **Valutazione della Sicurezza**: Eseguire scansioni di vulnerabilità e revisioni di sicurezza per modelli, fonti dati e servizi AI
- **Analisi della Reputazione**: Valutare il track record di sicurezza e le pratiche dei fornitori di servizi AI
- **Verifica di Conformità**: Assicurare che tutti i componenti rispettino i requisiti di sicurezza e normativi dell'organizzazione

#### **Pipeline di Distribuzione Sicure**  
- **Sicurezza CI/CD Automatizzata**: Integrare la scansione di sicurezza lungo tutte le pipeline di deployment automatizzate
- **Integrità degli Artifact**: Implementare la verifica crittografica per tutti gli artifact distribuiti (codice, modelli, configurazioni)
- **Distribuzione a Stadi**: Utilizzare strategie di deployment progressive con validazione di sicurezza ad ogni fase
- **Repository di Artifact Affidabili**: Distribuire solo da registry e repository di artifact verificati e sicuri

#### **Monitoraggio & Risposta Continua**
- **Scansione delle Dipendenze**: Monitoraggio continuo delle vulnerabilità per tutte le dipendenze software e componenti AI
- **Monitoraggio del Modello**: Valutazione continua del comportamento del modello, deriva delle prestazioni e anomalie di sicurezza
- **Tracciamento della Salute del Servizio**: Monitoraggio di servizi AI esterni per disponibilità, incidenti di sicurezza e cambiamenti di policy
- **Integrazione Threat Intelligence**: Incorporare feed di minacce specifici per rischi di sicurezza AI e ML

#### **Controllo Accessi & Minor Privilegio**
- **Permessi a Livello di Componente**: Restringere l'accesso a modelli, dati e servizi in base alla necessità aziendale
- **Gestione Account di Servizio**: Implementare account di servizio dedicati con permessi minimi necessari
- **Segmentazione di Rete**: Isolare componenti AI e limitare l'accesso di rete tra servizi
- **Controlli Gateway API**: Usare gateway API centralizzati per controllare e monitorare l’accesso a servizi AI esterni

#### **Risposta agli Incidenti & Recupero**
- **Procedure di Risposta Rapida**: Processi stabiliti per patchare o sostituire componenti AI compromessi
- **Rotazione delle Credenziali**: Sistemi automatizzati per ruotare segreti, chiavi API e credenziali di servizio
- **Capacità di Rollback**: Capacità di tornare rapidamente a versioni precedentemente note e funzionanti dei componenti AI
- **Recupero da Violazioni della Catena di Fornitura**: Procedure specifiche per rispondere a compromissioni di servizi AI a monte

### Strumenti di Sicurezza & Integrazione Microsoft

**GitHub Advanced Security** offre una protezione completa della catena di fornitura inclusi:
- **Scansione dei Segreti**: Rilevamento automatico di credenziali, chiavi API e token nei repository
- **Scansione delle Dipendenze**: Valutazione delle vulnerabilità per dipendenze e librerie open-source
- **Analisi CodeQL**: Analisi statica del codice per vulnerabilità di sicurezza e problemi di codifica
- **Insights sulla Catena di Fornitura**: Visibilità sullo stato di salute e sicurezza delle dipendenze

**Integrazione Azure DevOps & Azure Repos:**
- Integrazione senza interruzioni delle scansioni di sicurezza nelle piattaforme di sviluppo Microsoft
- Controlli di sicurezza automatizzati in Azure Pipelines per carichi di lavoro AI
- Applicazione di policy per un deployment sicuro dei componenti AI

**Pratiche Interne Microsoft:**
Microsoft implementa pratiche estese di sicurezza della catena di fornitura su tutti i prodotti. Scopri gli approcci comprovati in [Il Viaggio per Mettere in Sicurezza la Catena di Fornitura Software presso Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Best Practice di Sicurezza Fondamentali

Le implementazioni MCP ereditano e si basano sulla postura di sicurezza esistente della tua organizzazione. Rafforzare le pratiche di sicurezza fondamentali migliora significativamente la sicurezza complessiva dei sistemi AI e dei deployment MCP.

### Fondamentali di Sicurezza Core

#### **Pratiche di Sviluppo Sicuro**
- **Conformità OWASP**: Protezione contro le vulnerabilità web delle [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Protezione Specifica per AI**: Implementare controlli per le [OWASP Top 10 per LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Gestione Sicura dei Segreti**: Usare vault dedicati per token, chiavi API e dati di configurazione sensibili
- **Crittografia End-to-End**: Implementare comunicazioni sicure in tutti i componenti applicativi e flussi di dati
- **Validazione degli Input**: Validazione rigorosa di tutti gli input utente, parametri API e fonti dati

#### **Indurimento dell'Infrastruttura**
- **Autenticazione Multi-Fattore**: MFA obbligatoria per tutti gli account amministrativi e di servizio
- **Gestione delle Patch**: Patch automatizzate e tempestive per sistemi operativi, framework e dipendenze  
- **Integrazione Provider di Identità**: Gestione centralizzata dell’identità tramite provider aziendali (Microsoft Entra ID, Active Directory)
- **Segmentazione di Rete**: Isolamento logico dei componenti MCP per limitare potenziali movimenti laterali
- **Principio del Minor Privilegio**: Permessi minimi necessari per tutti i componenti di sistema e account

#### **Monitoraggio & Rilevamento della Sicurezza**
- **Logging Completo**: Registrazione dettagliata delle attività dell'applicazione AI, incluse le interazioni client-server MCP
- **Integrazione SIEM**: Gestione centralizzata delle informazioni e degli eventi di sicurezza per rilevamento di anomalie
- **Analisi Comportamentale**: Monitoraggio AI-powered per rilevare pattern insoliti nel comportamento di sistema e utenti
- **Threat Intelligence**: Integrazione di feed di minacce esterni e indicatori di compromissione (IOC)
- **Risposta agli Incidenti**: Procedure ben definite per rilevamento, risposta e recupero da incidenti di sicurezza

#### **Architettura Zero Trust**
- **Mai Fidarsi, Sempre Verificare**: Verifica continua di utenti, dispositivi e connessioni di rete
- **Micro-Segmentazione**: Controlli granulari di rete che isolano singoli carichi di lavoro e servizi
- **Sicurezza Centrata sull'Identità**: Policy di sicurezza basate su identità verificate anziché sulla posizione di rete
- **Valutazione Continua del Rischio**: Valutazione dinamica della postura di sicurezza basata sul contesto e comportamento attuale
- **Accesso Condizionale**: Controlli di accesso che si adattano in base a fattori di rischio, localizzazione e fiducia del dispositivo

### Pattern di Integrazione Aziendale

#### **Integrazione con l'Ecosistema di Sicurezza Microsoft**
- **Microsoft Defender for Cloud**: Gestione completa della postura di sicurezza cloud
- **Azure Sentinel**: SIEM e SOAR nativi cloud per la protezione dei carichi di lavoro AI
- **Microsoft Entra ID**: Gestione aziendale di identità e accessi con policy di accesso condizionale
- **Azure Key Vault**: Gestione centralizzata dei segreti con supporto hardware security module (HSM)
- **Microsoft Purview**: Governance e conformità dei dati per fonti e flussi di lavoro AI

#### **Conformità & Governance**
- **Allineamento Regolatorio**: Assicurare che le implementazioni MCP rispettino i requisiti di conformità settoriali (GDPR, HIPAA, SOC 2)

- **Classificazione dei Dati**: Corretta categorizzazione e gestione dei dati sensibili trattati dai sistemi AI
- **Tracce di Audit**: Registrazioni complete per conformità normativa e indagini forensi
- **Controlli sulla Privacy**: Implementazione dei principi privacy-by-design nell'architettura dei sistemi AI
- **Gestione delle Modifiche**: Processi formali per le revisioni di sicurezza delle modifiche ai sistemi AI

Queste pratiche fondamentali creano una base di sicurezza robusta che migliora l'efficacia dei controlli di sicurezza specifici MCP e fornisce una protezione completa per le applicazioni basate su AI.

## Principali Concetti Chiave di Sicurezza

- **Approccio a Sicurezza Stratificata**: Combinare pratiche di sicurezza fondamentali (codifica sicura, principio del minimo privilegio, verifica della supply chain, monitoraggio continuo) con controlli specifici AI per una protezione completa

- **Scenario di Minacce Specifiche per AI**: I sistemi MCP affrontano rischi unici tra cui iniezione di prompt, avvelenamento degli strumenti, hijacking di sessione, problemi di confused deputy, vulnerabilità di passthrough dei token e permessi eccessivi che richiedono mitigazioni specializzate

- **Eccellenza in Autenticazione e Autorizzazione**: Implementare un'autenticazione robusta usando fornitori di identità esterni (Microsoft Entra ID), applicare una valida convalida dei token e non accettare mai token non esplicitamente emessi per il server MCP

- **Prevenzione degli Attacchi AI**: Distribuire Microsoft Prompt Shields e Azure Content Safety per difendersi contro attacchi indiretti di iniezione di prompt e avvelenamento degli strumenti, convalidando i metadati degli strumenti e monitorando cambiamenti dinamici

- **Sicurezza di Sessione e Trasporto**: Utilizzare ID di sessione crittograficamente sicuri e non deterministici legati alle identità utente, implementare una corretta gestione del ciclo di vita della sessione e non usare mai le sessioni per l'autenticazione

- **Migliori Pratiche di Sicurezza OAuth**: Prevenire attacchi di confused deputy tramite il consenso esplicito degli utenti per i client registrati dinamicamente, implementare correttamente OAuth 2.1 con PKCE e applicare una rigorosa convalida dell'URI di reindirizzamento  

- **Principi di Sicurezza dei Token**: Evitare anti-pattern di passthrough dei token, convalidare i claim audience del token, implementare token a breve durata con rotazione sicura e mantenere limiti chiari di fiducia

- **Sicurezza Completa della Supply Chain**: Trattare tutti i componenti dell'ecosistema AI (modelli, embeddings, provider di contesto, API esterne) con lo stesso rigore di sicurezza delle dipendenze software tradizionali

- **Evoluzione Continua**: Rimanere aggiornati con le specifiche MCP in rapida evoluzione, contribuire agli standard della comunità di sicurezza e mantenere posture di sicurezza adattive man mano che il protocollo matura

- **Integrazione della Sicurezza Microsoft**: Sfruttare l'ecosistema di sicurezza completo di Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) per una protezione rafforzata delle distribuzioni MCP

## Risorse Complete

### **Documentazione Ufficiale di Sicurezza MCP**
- [Specifiche MCP (Corrente: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Migliori Pratiche di Sicurezza MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specifiche di Autorizzazione MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Repository GitHub MCP](https://github.com/modelcontextprotocol)

### **Risorse di Sicurezza OWASP MCP**
- [Guida alla Sicurezza Azure OWASP MCP](https://microsoft.github.io/mcp-azure-security-guide/) - Guida completa OWASP MCP Top 10 con indicazioni di implementazione su Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Rischi di sicurezza ufficiali OWASP MCP
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Formazione pratica sulla sicurezza MCP su Azure

### **Standard di Sicurezza e Migliori Pratiche**
- [Migliori Pratiche di Sicurezza OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Sicurezza delle Applicazioni Web](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 per Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Ricerca e Analisi sulla Sicurezza AI**
- [Iniezione di Prompt in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Attacchi di Avvelenamento degli Strumenti (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Briefing di Ricerca sulla Sicurezza MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Soluzioni di Sicurezza Microsoft**
- [Documentazione Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Servizio Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Sicurezza Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Migliori Pratiche per Gestione Token Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Guide di Implementazione e Tutorial**
- [Azure API Management come Gateway di Autenticazione MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Autenticazione Microsoft Entra ID con server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Archiviazione Sicura dei Token e Crittografia (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Sicurezza DevOps e Supply Chain**
- [Sicurezza Azure DevOps](https://azure.microsoft.com/products/devops)
- [Sicurezza Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Percorso di Sicurezza Microsoft Supply Chain](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentazione di Sicurezza Aggiuntiva**

Per una guida di sicurezza completa, fare riferimento a questi documenti specializzati in questa sezione:

- **[Esempio di Autorizzazione CIMD e DCR](./samples/cimd-dcr-auth/README.md)** - Server risorsa MCP `2026-07-28` eseguibile in TypeScript che compara i Documenti di Metadata Client ID preferiti con il fallback deprecated di Dynamic Client Registration
- **[Migliori Pratiche di Sicurezza MCP](./mcp-security-best-practices.md)** - Pratiche complete di sicurezza per implementazioni MCP
- **[Implementazione Azure Content Safety](./azure-content-safety-implementation.md)** - Esempi pratici di implementazione per integrazione Azure Content Safety  
- **[Controlli di Sicurezza MCP](./mcp-security-controls.md)** - Ultimi controlli e tecniche di sicurezza per distribuzioni MCP
- **[Riferimento Rapido alle Migliori Pratiche MCP](./mcp-best-practices.md)** - Guida rapida per le pratiche di sicurezza essenziali MCP
- **[BlueHat 2026: Mettere in sicurezza il futuro dell'AI: Proteggere MCP con pattern di difesa in profondità](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Pattern di difesa in profondità dal Microsoft Security Response Center (MSRC)

### **Formazione Pratica sulla Sicurezza**

- **[Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Workshop pratico completo per proteggere server MCP in Azure con camp progressivi da Base Camp a Summit
- **[Guida alla Sicurezza Azure OWASP MCP](https://microsoft.github.io/mcp-azure-security-guide/)** - Architettura di riferimento e indicazioni di implementazione per tutti i rischi OWASP MCP Top 10

---

## Cosa Fare Dopo

Prossimo: [Capitolo 3: Iniziare](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->