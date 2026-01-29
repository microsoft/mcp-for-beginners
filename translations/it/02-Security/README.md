# MCP Security: Protezione Completa per i Sistemi AI

[![MCP Security Best Practices](../../../translated_images/it/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Clicca sull'immagine sopra per vedere il video di questa lezione)_

La sicurezza è fondamentale nella progettazione dei sistemi AI, motivo per cui la consideriamo la nostra seconda sezione. Questo è in linea con il principio **Secure by Design** di Microsoft dall'[Iniziativa Secure Future](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Il Model Context Protocol (MCP) porta potenti nuove capacità alle applicazioni guidate dall'AI introducendo al contempo sfide di sicurezza uniche che vanno oltre i rischi tradizionali del software. I sistemi MCP affrontano sia preoccupazioni di sicurezza consolidate (codifica sicura, minimo privilegio, sicurezza della catena di fornitura) sia nuove minacce specifiche dell'AI, tra cui prompt injection, avvelenamento degli strumenti, session hijacking, attacchi confused deputy, vulnerabilità di token passthrough e modifiche dinamiche delle capacità.

Questa lezione esplora i rischi di sicurezza più critici nelle implementazioni MCP—coprendo autenticazione, autorizzazione, permessi eccessivi, prompt injection indiretta, sicurezza delle sessioni, problemi confused deputy, gestione dei token e vulnerabilità della catena di fornitura. Imparerai controlli pratici e best practice per mitigare questi rischi sfruttando soluzioni Microsoft come Prompt Shields, Azure Content Safety e GitHub Advanced Security per rafforzare il tuo deployment MCP.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- **Identificare Minacce Specifiche MCP**: Riconoscere rischi di sicurezza unici nei sistemi MCP inclusi prompt injection, avvelenamento degli strumenti, permessi eccessivi, session hijacking, problemi confused deputy, vulnerabilità di token passthrough e rischi della catena di fornitura
- **Applicare Controlli di Sicurezza**: Implementare mitigazioni efficaci tra cui autenticazione robusta, accesso a minimo privilegio, gestione sicura dei token, controlli di sicurezza delle sessioni e verifica della catena di fornitura
- **Sfruttare Soluzioni di Sicurezza Microsoft**: Comprendere e distribuire Microsoft Prompt Shields, Azure Content Safety e GitHub Advanced Security per la protezione dei carichi di lavoro MCP
- **Validare la Sicurezza degli Strumenti**: Riconoscere l'importanza della validazione dei metadati degli strumenti, monitorare cambiamenti dinamici e difendersi dagli attacchi di prompt injection indiretta
- **Integrare Best Practice**: Combinare fondamenta di sicurezza consolidate (codifica sicura, hardening del server, zero trust) con controlli specifici MCP per una protezione completa

# Architettura e Controlli di Sicurezza MCP

Le implementazioni moderne MCP richiedono approcci di sicurezza stratificati che affrontino sia la sicurezza tradizionale del software sia le minacce specifiche dell'AI. La specifica MCP in rapida evoluzione continua a maturare i suoi controlli di sicurezza, permettendo una migliore integrazione con le architetture di sicurezza aziendali e le best practice consolidate.

La ricerca dal [Microsoft Digital Defense Report](https://aka.ms/mddr) dimostra che **il 98% delle violazioni segnalate sarebbe prevenuto da una rigorosa igiene di sicurezza**. La strategia di protezione più efficace combina pratiche di sicurezza fondamentali con controlli specifici MCP—le misure di sicurezza di base comprovate rimangono le più impattanti nella riduzione del rischio complessivo.

## Scenario Attuale della Sicurezza

> **Nota:** Queste informazioni riflettono gli standard di sicurezza MCP al **18 dicembre 2025**. Il protocollo MCP continua a evolversi rapidamente e le future implementazioni potrebbero introdurre nuovi schemi di autenticazione e controlli migliorati. Consulta sempre la [Specificazione MCP](https://spec.modelcontextprotocol.io/), il [repository GitHub MCP](https://github.com/modelcontextprotocol) e la [documentazione delle best practice di sicurezza](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) per le indicazioni più aggiornate.

### Evoluzione dell'Autenticazione MCP

La specifica MCP è evoluta significativamente nel suo approccio ad autenticazione e autorizzazione:

- **Approccio Originale**: Le prime specifiche richiedevano agli sviluppatori di implementare server di autenticazione personalizzati, con i server MCP che agivano come OAuth 2.0 Authorization Server gestendo direttamente l'autenticazione degli utenti
- **Standard Attuale (2025-11-25)**: La specifica aggiornata consente ai server MCP di delegare l'autenticazione a provider di identità esterni (come Microsoft Entra ID), migliorando la postura di sicurezza e riducendo la complessità di implementazione
- **Transport Layer Security**: Supporto migliorato per meccanismi di trasporto sicuri con schemi di autenticazione appropriati sia per connessioni locali (STDIO) sia remote (Streamable HTTP)

## Sicurezza di Autenticazione e Autorizzazione

### Sfide di Sicurezza Attuali

Le implementazioni moderne MCP affrontano diverse sfide di autenticazione e autorizzazione:

### Rischi e Vettori di Minaccia

- **Logica di Autorizzazione Errata**: Implementazioni difettose dell'autorizzazione nei server MCP possono esporre dati sensibili e applicare in modo errato i controlli di accesso
- **Compromissione del Token OAuth**: Il furto di token del server MCP locale consente agli attaccanti di impersonare server e accedere a servizi a valle
- **Vulnerabilità di Token Passthrough**: La gestione impropria dei token crea bypass dei controlli di sicurezza e lacune di responsabilità
- **Permessi Eccessivi**: Server MCP con privilegi troppo ampi violano il principio del minimo privilegio ed espandono la superficie di attacco

#### Token Passthrough: Un Anti-Pattern Critico

**Il token passthrough è esplicitamente vietato** nella specifica di autorizzazione MCP attuale a causa delle gravi implicazioni di sicurezza:

##### Circumvenzione dei Controlli di Sicurezza
- I server MCP e le API a valle implementano controlli di sicurezza critici (limitazione della frequenza, validazione delle richieste, monitoraggio del traffico) che dipendono dalla corretta validazione del token
- L'uso diretto del token da client a API bypassa queste protezioni essenziali, compromettendo l'architettura di sicurezza

##### Sfide di Responsabilità e Audit  
- I server MCP non possono distinguere tra client che usano token emessi a monte, interrompendo le tracce di audit
- I log dei server risorsa a valle mostrano origini di richieste fuorvianti invece degli effettivi intermediari server MCP
- L'investigazione degli incidenti e la verifica della conformità diventano significativamente più difficili

##### Rischi di Esfiltrazione Dati
- Le affermazioni di token non validate permettono ad attori malintenzionati con token rubati di usare i server MCP come proxy per l'esfiltrazione di dati
- Le violazioni del confine di fiducia consentono schemi di accesso non autorizzati che bypassano i controlli di sicurezza previsti

##### Vettori di Attacco Multi-Servizio
- Token compromessi accettati da più servizi consentono movimenti laterali attraverso sistemi connessi
- Le assunzioni di fiducia tra servizi possono essere violate quando l'origine del token non può essere verificata

### Controlli di Sicurezza e Mitigazioni

**Requisiti Critici di Sicurezza:**

> **OBBLIGATORIO**: I server MCP **NON DEVONO** accettare alcun token che non sia stato esplicitamente emesso per il server MCP

#### Controlli di Autenticazione e Autorizzazione

- **Revisione Rigorosa dell'Autorizzazione**: Condurre audit completi della logica di autorizzazione del server MCP per garantire che solo utenti e client previsti possano accedere a risorse sensibili
  - **Guida all'Implementazione**: [Azure API Management come Gateway di Autenticazione per Server MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrazione Identità**: [Uso di Microsoft Entra ID per l'Autenticazione del Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestione Sicura dei Token**: Implementare le [best practice Microsoft per la validazione e il ciclo di vita dei token](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validare che le affermazioni audience del token corrispondano all'identità del server MCP
  - Implementare politiche corrette di rotazione e scadenza dei token
  - Prevenire attacchi di replay e usi non autorizzati dei token

- **Archiviazione Protetta dei Token**: Conservare i token in modo sicuro con crittografia sia a riposo che in transito
  - **Best Practice**: [Linee guida per l'archiviazione sicura e la crittografia dei token](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementazione del Controllo Accessi

- **Principio del Minimo Privilegio**: Concedere ai server MCP solo i permessi minimi necessari per la funzionalità prevista
  - Revisioni regolari dei permessi e aggiornamenti per prevenire l'accumulo di privilegi
  - **Documentazione Microsoft**: [Accesso Sicuro a Minimo Privilegio](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Controllo Accessi Basato su Ruoli (RBAC)**: Implementare assegnazioni di ruolo granulari
  - Limitare i ruoli strettamente a risorse e azioni specifiche
  - Evitare permessi ampi o non necessari che espandono la superficie di attacco

- **Monitoraggio Continuo dei Permessi**: Implementare auditing e monitoraggio continuo degli accessi
  - Monitorare i modelli di utilizzo dei permessi per anomalie
  - Correggere tempestivamente privilegi eccessivi o inutilizzati

## Minacce di Sicurezza Specifiche per l'AI

### Attacchi di Prompt Injection e Manipolazione degli Strumenti

Le implementazioni moderne MCP affrontano vettori di attacco sofisticati specifici dell'AI che le misure di sicurezza tradizionali non possono affrontare completamente:

#### **Prompt Injection Indiretta (Cross-Domain Prompt Injection)**

La **Prompt Injection Indiretta** rappresenta una delle vulnerabilità più critiche nei sistemi AI abilitati MCP. Gli attaccanti inseriscono istruzioni dannose all'interno di contenuti esterni—documenti, pagine web, email o fonti dati—che i sistemi AI successivamente elaborano come comandi legittimi.

**Scenari di Attacco:**
- **Injection basata su Documenti**: Istruzioni dannose nascoste in documenti elaborati che attivano azioni AI non intenzionali
- **Sfruttamento di Contenuti Web**: Pagine web compromesse contenenti prompt incorporati che manipolano il comportamento AI quando vengono estratti
- **Attacchi via Email**: Prompt dannosi nelle email che inducono assistenti AI a divulgare informazioni o eseguire azioni non autorizzate
- **Contaminazione di Fonti Dati**: Database o API compromessi che forniscono contenuti contaminati ai sistemi AI

**Impatto nel Mondo Reale**: Questi attacchi possono causare esfiltrazione di dati, violazioni della privacy, generazione di contenuti dannosi e manipolazione delle interazioni con gli utenti. Per un'analisi dettagliata, vedi [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/it/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Attacchi di Avvelenamento degli Strumenti**

Il **Tool Poisoning** prende di mira i metadati che definiscono gli strumenti MCP, sfruttando il modo in cui i LLM interpretano descrizioni e parametri degli strumenti per prendere decisioni di esecuzione.

**Meccanismi di Attacco:**
- **Manipolazione dei Metadati**: Gli attaccanti iniettano istruzioni dannose nelle descrizioni degli strumenti, definizioni dei parametri o esempi d'uso
- **Istruzioni Invisibili**: Prompt nascosti nei metadati degli strumenti che vengono elaborati dai modelli AI ma sono invisibili agli utenti umani
- **Modifica Dinamica degli Strumenti ("Rug Pulls")**: Strumenti approvati dagli utenti che vengono successivamente modificati per eseguire azioni dannose senza che l'utente ne sia consapevole
- **Injection di Parametri**: Contenuti dannosi incorporati negli schemi dei parametri degli strumenti che influenzano il comportamento del modello

**Rischi dei Server Ospitati**: I server MCP remoti presentano rischi elevati poiché le definizioni degli strumenti possono essere aggiornate dopo l'approvazione iniziale dell'utente, creando scenari in cui strumenti precedentemente sicuri diventano dannosi. Per un'analisi completa, vedi [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/it/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Ulteriori Vettori di Attacco AI**

- **Cross-Domain Prompt Injection (XPIA)**: Attacchi sofisticati che sfruttano contenuti da più domini per bypassare i controlli di sicurezza
- **Modifica Dinamica delle Capacità**: Cambiamenti in tempo reale delle capacità degli strumenti che sfuggono alle valutazioni di sicurezza iniziali
- **Avvelenamento della Finestra di Contesto**: Attacchi che manipolano ampie finestre di contesto per nascondere istruzioni dannose
- **Attacchi di Confusione del Modello**: Sfruttamento dei limiti del modello per creare comportamenti imprevedibili o non sicuri

### Impatto dei Rischi di Sicurezza AI

**Conseguenze ad Alto Impatto:**
- **Esfiltrazione di Dati**: Accesso non autorizzato e furto di dati sensibili aziendali o personali
- **Violazioni della Privacy**: Esposizione di informazioni personali identificabili (PII) e dati aziendali riservati  
- **Manipolazione del Sistema**: Modifiche non intenzionali a sistemi e flussi di lavoro critici
- **Furto di Credenziali**: Compromissione di token di autenticazione e credenziali di servizio
- **Movimenti Laterali**: Uso di sistemi AI compromessi come pivot per attacchi più ampi nella rete

### Soluzioni di Sicurezza AI Microsoft

#### **AI Prompt Shields: Protezione Avanzata Contro Attacchi di Injection**

I **Microsoft AI Prompt Shields** forniscono una difesa completa contro attacchi di prompt injection diretti e indiretti attraverso molteplici livelli di sicurezza:

##### **Meccanismi di Protezione Principali:**

1. **Rilevamento e Filtraggio Avanzati**
   - Algoritmi di machine learning e tecniche NLP rilevano istruzioni dannose nei contenuti esterni
   - Analisi in tempo reale di documenti, pagine web, email e fonti dati per minacce incorporate
   - Comprensione contestuale di pattern di prompt legittimi vs dannosi

2. **Tecniche di Spotlighting**  
   - Distingue tra istruzioni di sistema affidabili e input esterni potenzialmente compromessi
   - Metodi di trasformazione del testo che migliorano la rilevanza del modello isolando contenuti dannosi
   - Aiuta i sistemi AI a mantenere la gerarchia corretta delle istruzioni e ignorare comandi iniettati

3. **Sistemi di Delimitazione e Datamarking**
   - Definizione esplicita dei confini tra messaggi di sistema affidabili e testo di input esterno
   - Marcatori speciali evidenziano i confini tra fonti dati affidabili e non affidabili
   - Separazione chiara previene confusione nelle istruzioni ed esecuzione non autorizzata di comandi

4. **Intelligence sulle Minacce Continua**
   - Microsoft monitora costantemente i pattern di attacco emergenti e aggiorna le difese
   - Ricerca proattiva di nuove tecniche di injection e vettori di attacco
   - Aggiornamenti regolari dei modelli di sicurezza per mantenere efficacia contro minacce in evoluzione

5. **Integrazione con Azure Content Safety**
   - Parte della suite completa Azure AI Content Safety
   - Rilevamento aggiuntivo di tentativi di jailbreak, contenuti dannosi e violazioni delle policy di sicurezza
   - Controlli di sicurezza unificati attraverso i componenti dell'applicazione AI

**Risorse per l'Implementazione**: [Documentazione Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/it/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Minacce Avanzate di Sicurezza MCP

### Vulnerabilità di Session Hijacking

Il **session hijacking** rappresenta un vettore di attacco critico nelle implementazioni MCP stateful dove parti non autorizzate ottengono e abusano di identificatori di sessione legittimi per impersonare client ed eseguire azioni non autorizzate.

#### **Scenari di Attacco e Rischi**

- **Session Hijack Prompt Injection**: Attaccanti con ID di sessione rubati iniettano eventi dannosi in server che condividono lo stato di sessione, potenzialmente attivando azioni dannose o accedendo a dati sensibili
- **Impersonazione Diretta**: ID di sessione rubati consentono chiamate dirette al server MCP che bypassano l'autenticazione, trattando gli attaccanti come utenti legittimi
- **Stream Resumable Compromessi**: Gli attaccanti possono terminare prematuramente le richieste, causando la ripresa da parte di client legittimi con contenuti potenzialmente dannosi

#### **Controlli di Sicurezza per la Gestione delle Sessioni**

**Requisiti Critici:**
- **Verifica dell'Autorizzazione**: I server MCP che implementano l'autorizzazione **DEVONO** verificare TUTTE le richieste in ingresso e **NON DEVONO** fare affidamento sulle sessioni per l'autenticazione  
- **Generazione Sicura della Sessione**: Utilizzare ID di sessione crittograficamente sicuri e non deterministici generati con generatori di numeri casuali sicuri  
- **Associazione Specifica all'Utente**: Associare gli ID di sessione alle informazioni specifiche dell'utente usando formati come `<user_id>:<session_id>` per prevenire abusi di sessione tra utenti diversi  
- **Gestione del Ciclo di Vita della Sessione**: Implementare una corretta scadenza, rotazione e invalidazione per limitare le finestre di vulnerabilità  
- **Sicurezza del Trasporto**: HTTPS obbligatorio per tutte le comunicazioni per prevenire l'intercettazione degli ID di sessione  

### Problema del Confused Deputy

Il **problema del confused deputy** si verifica quando i server MCP agiscono come proxy di autenticazione tra i client e servizi di terze parti, creando opportunità per bypassare l'autorizzazione tramite lo sfruttamento di ID client statici.

#### **Meccaniche dell'Attacco e Rischi**

- **Bypass del Consenso Basato su Cookie**: L'autenticazione utente precedente crea cookie di consenso che gli attaccanti sfruttano tramite richieste di autorizzazione malevole con URI di reindirizzamento manipolati  
- **Furto del Codice di Autorizzazione**: I cookie di consenso esistenti possono far sì che i server di autorizzazione saltino le schermate di consenso, reindirizzando i codici a endpoint controllati dall'attaccante  
- **Accesso API Non Autorizzato**: I codici di autorizzazione rubati consentono lo scambio di token e l'impersonificazione dell'utente senza approvazione esplicita  

#### **Strategie di Mitigazione**

**Controlli Obbligatori:**  
- **Requisiti di Consenso Esplicito**: I server proxy MCP che utilizzano ID client statici **DEVONO** ottenere il consenso dell'utente per ogni client registrato dinamicamente  
- **Implementazione della Sicurezza OAuth 2.1**: Seguire le migliori pratiche di sicurezza OAuth attuali, incluso PKCE (Proof Key for Code Exchange) per tutte le richieste di autorizzazione  
- **Validazione Rigorosa del Client**: Implementare una rigorosa validazione degli URI di reindirizzamento e degli identificatori client per prevenire sfruttamenti  

### Vulnerabilità di Token Passthrough  

Il **token passthrough** rappresenta un anti-pattern esplicito in cui i server MCP accettano token client senza una corretta validazione e li inoltrano alle API a valle, violando le specifiche di autorizzazione MCP.

#### **Implicazioni di Sicurezza**

- **Circumvenzione del Controllo**: L'uso diretto di token client verso API bypassa controlli critici di limitazione della frequenza, validazione e monitoraggio  
- **Corruzione della Traccia di Audit**: I token emessi a monte rendono impossibile l'identificazione del client, compromettendo le capacità di indagine sugli incidenti  
- **Esfiltrazione Dati tramite Proxy**: Token non validati permettono ad attori malevoli di usare i server come proxy per accessi non autorizzati ai dati  
- **Violazioni del Confine di Fiducia**: Le assunzioni di fiducia dei servizi a valle possono essere violate quando non è possibile verificare l'origine dei token  
- **Espansione degli Attacchi Multi-servizio**: Token compromessi accettati su più servizi consentono movimenti laterali  

#### **Controlli di Sicurezza Richiesti**

**Requisiti Non Negoziali:**  
- **Validazione del Token**: I server MCP **NON DEVONO** accettare token non esplicitamente emessi per il server MCP  
- **Verifica del Pubblico (Audience)**: Validare sempre che le affermazioni sul pubblico del token corrispondano all'identità del server MCP  
- **Ciclo di Vita Corretto del Token**: Implementare token di accesso a breve durata con pratiche sicure di rotazione  

## Sicurezza della Supply Chain per Sistemi AI

La sicurezza della supply chain si è evoluta oltre le tradizionali dipendenze software per includere l'intero ecosistema AI. Le implementazioni moderne di MCP devono verificare e monitorare rigorosamente tutti i componenti AI, poiché ciascuno introduce potenziali vulnerabilità che potrebbero compromettere l'integrità del sistema.

### Componenti Estesi della Supply Chain AI

**Dipendenze Software Tradizionali:**  
- Librerie e framework open-source  
- Immagini container e sistemi base  
- Strumenti di sviluppo e pipeline di build  
- Componenti e servizi infrastrutturali  

**Elementi Specifici della Supply Chain AI:**  
- **Modelli Fondamentali**: Modelli pre-addestrati da vari fornitori che richiedono verifica della provenienza  
- **Servizi di Embedding**: Servizi esterni di vettorizzazione e ricerca semantica  
- **Provider di Contesto**: Fonti dati, basi di conoscenza e repository di documenti  
- **API di Terze Parti**: Servizi AI esterni, pipeline ML e endpoint di elaborazione dati  
- **Artefatti del Modello**: Pesi, configurazioni e varianti di modelli fine-tuned  
- **Fonti di Dati di Addestramento**: Dataset utilizzati per l'addestramento e il fine-tuning dei modelli  

### Strategia Completa di Sicurezza della Supply Chain

#### **Verifica dei Componenti e Fiducia**  
- **Validazione della Provenienza**: Verificare origine, licenze e integrità di tutti i componenti AI prima dell'integrazione  
- **Valutazione della Sicurezza**: Condurre scansioni di vulnerabilità e revisioni di sicurezza per modelli, fonti dati e servizi AI  
- **Analisi della Reputazione**: Valutare il track record di sicurezza e le pratiche dei fornitori di servizi AI  
- **Verifica della Conformità**: Assicurarsi che tutti i componenti rispettino i requisiti di sicurezza e normativi dell'organizzazione  

#### **Pipeline di Distribuzione Sicure**  
- **Sicurezza CI/CD Automatizzata**: Integrare la scansione di sicurezza in tutte le pipeline di distribuzione automatizzate  
- **Integrità degli Artefatti**: Implementare la verifica crittografica per tutti gli artefatti distribuiti (codice, modelli, configurazioni)  
- **Distribuzione a Stadi**: Usare strategie di distribuzione progressive con validazione di sicurezza a ogni fase  
- **Repository di Artefatti Affidabili**: Distribuire solo da registri e repository di artefatti verificati e sicuri  

#### **Monitoraggio Continuo e Risposta**  
- **Scansione delle Dipendenze**: Monitoraggio continuo delle vulnerabilità per tutte le dipendenze software e componenti AI  
- **Monitoraggio del Modello**: Valutazione continua del comportamento del modello, deriva delle prestazioni e anomalie di sicurezza  
- **Monitoraggio della Salute del Servizio**: Controllo dei servizi AI esterni per disponibilità, incidenti di sicurezza e cambiamenti di policy  
- **Integrazione di Threat Intelligence**: Incorporare feed di minacce specifici per rischi di sicurezza AI e ML  

#### **Controllo Accessi e Privilegio Minimo**  
- **Permessi a Livello di Componente**: Limitare l'accesso a modelli, dati e servizi in base alla necessità di business  
- **Gestione degli Account di Servizio**: Implementare account di servizio dedicati con permessi minimi necessari  
- **Segmentazione di Rete**: Isolare i componenti AI e limitare l'accesso di rete tra i servizi  
- **Controlli tramite API Gateway**: Usare gateway API centralizzati per controllare e monitorare l'accesso ai servizi AI esterni  

#### **Risposta agli Incidenti e Recupero**  
- **Procedure di Risposta Rapida**: Processi stabiliti per patchare o sostituire componenti AI compromessi  
- **Rotazione delle Credenziali**: Sistemi automatizzati per la rotazione di segreti, chiavi API e credenziali di servizio  
- **Capacità di Rollback**: Possibilità di tornare rapidamente a versioni precedenti note e sicure dei componenti AI  
- **Recupero da Violazioni della Supply Chain**: Procedure specifiche per rispondere a compromissioni di servizi AI a monte  

### Strumenti di Sicurezza Microsoft e Integrazione

**GitHub Advanced Security** fornisce una protezione completa della supply chain includendo:  
- **Scansione dei Segreti**: Rilevamento automatico di credenziali, chiavi API e token nei repository  
- **Scansione delle Dipendenze**: Valutazione delle vulnerabilità per dipendenze e librerie open-source  
- **Analisi CodeQL**: Analisi statica del codice per vulnerabilità di sicurezza e problemi di codifica  
- **Insight sulla Supply Chain**: Visibilità sulla salute e stato di sicurezza delle dipendenze  

**Integrazione con Azure DevOps & Azure Repos:**  
- Integrazione fluida della scansione di sicurezza nelle piattaforme di sviluppo Microsoft  
- Controlli di sicurezza automatizzati in Azure Pipelines per carichi di lavoro AI  
- Applicazione di policy per distribuzioni sicure di componenti AI  

**Pratiche Interne Microsoft:**  
Microsoft implementa estese pratiche di sicurezza della supply chain in tutti i prodotti. Scopri gli approcci comprovati in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Best Practice di Sicurezza Fondamentale

Le implementazioni MCP ereditano e si basano sulla postura di sicurezza esistente della tua organizzazione. Rafforzare le pratiche di sicurezza fondamentali migliora significativamente la sicurezza complessiva dei sistemi AI e delle distribuzioni MCP.

### Fondamenti di Sicurezza Core

#### **Pratiche di Sviluppo Sicuro**  
- **Conformità OWASP**: Protezione contro le vulnerabilità web delle [OWASP Top 10](https://owasp.org/www-project-top-ten/)  
- **Protezione Specifica per AI**: Implementare controlli per le [OWASP Top 10 per LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Gestione Sicura dei Segreti**: Usare vault dedicati per token, chiavi API e dati di configurazione sensibili  
- **Crittografia End-to-End**: Implementare comunicazioni sicure in tutti i componenti applicativi e flussi di dati  
- **Validazione degli Input**: Validazione rigorosa di tutti gli input utente, parametri API e fonti dati  

#### **Indurimento dell'Infrastruttura**  
- **Autenticazione Multi-Fattore**: MFA obbligatorio per tutti gli account amministrativi e di servizio  
- **Gestione delle Patch**: Patch automatizzate e tempestive per sistemi operativi, framework e dipendenze  
- **Integrazione con Provider di Identità**: Gestione centralizzata delle identità tramite provider aziendali (Microsoft Entra ID, Active Directory)  
- **Segmentazione di Rete**: Isolamento logico dei componenti MCP per limitare i movimenti laterali  
- **Principio del Privilegio Minimo**: Permessi minimi necessari per tutti i componenti di sistema e account  

#### **Monitoraggio e Rilevamento di Sicurezza**  
- **Logging Completo**: Registrazione dettagliata delle attività applicative AI, incluse le interazioni client-server MCP  
- **Integrazione SIEM**: Gestione centralizzata delle informazioni e degli eventi di sicurezza per il rilevamento di anomalie  
- **Analisi Comportamentale**: Monitoraggio AI-powered per rilevare pattern insoliti nei comportamenti di sistema e utente  
- **Threat Intelligence**: Integrazione di feed di minacce esterni e indicatori di compromissione (IOC)  
- **Risposta agli Incidenti**: Procedure ben definite per il rilevamento, risposta e recupero da incidenti di sicurezza  

#### **Architettura Zero Trust**  
- **Mai Fidarsi, Sempre Verificare**: Verifica continua di utenti, dispositivi e connessioni di rete  
- **Micro-Segmentazione**: Controlli di rete granulari che isolano singoli workload e servizi  
- **Sicurezza Centrata sull'Identità**: Policy di sicurezza basate su identità verificate anziché sulla posizione di rete  
- **Valutazione Continua del Rischio**: Valutazione dinamica della postura di sicurezza basata sul contesto e comportamento attuali  
- **Accesso Condizionale**: Controlli di accesso che si adattano in base a fattori di rischio, posizione e affidabilità del dispositivo  

### Pattern di Integrazione Enterprise

#### **Integrazione nell'Ecosistema di Sicurezza Microsoft**  
- **Microsoft Defender for Cloud**: Gestione completa della postura di sicurezza cloud  
- **Azure Sentinel**: SIEM e SOAR nativi cloud per la protezione dei carichi di lavoro AI  
- **Microsoft Entra ID**: Gestione enterprise di identità e accessi con policy di accesso condizionale  
- **Azure Key Vault**: Gestione centralizzata dei segreti con supporto hardware HSM  
- **Microsoft Purview**: Governance e conformità dei dati per fonti e flussi di lavoro AI  

#### **Conformità e Governance**  
- **Allineamento Normativo**: Assicurare che le implementazioni MCP rispettino i requisiti di conformità specifici del settore (GDPR, HIPAA, SOC 2)  
- **Classificazione dei Dati**: Categorizzazione e gestione adeguata dei dati sensibili elaborati dai sistemi AI  
- **Tracce di Audit**: Logging completo per conformità normativa e indagini forensi  
- **Controlli sulla Privacy**: Implementazione di principi privacy-by-design nell'architettura dei sistemi AI  
- **Gestione del Cambiamento**: Processi formali per revisioni di sicurezza delle modifiche ai sistemi AI  

Queste pratiche fondamentali creano una solida base di sicurezza che migliora l'efficacia dei controlli specifici MCP e fornisce una protezione completa per le applicazioni AI-driven.

## Punti Chiave di Sicurezza

- **Approccio di Sicurezza Stratificato**: Combinare pratiche di sicurezza fondamentali (codifica sicura, privilegio minimo, verifica della supply chain, monitoraggio continuo) con controlli specifici AI per una protezione completa  

- **Panorama delle Minacce Specifiche AI**: I sistemi MCP affrontano rischi unici come injection di prompt, avvelenamento di strumenti, hijacking di sessione, problemi di confused deputy, vulnerabilità di token passthrough e permessi eccessivi che richiedono mitigazioni specializzate  

- **Eccellenza in Autenticazione e Autorizzazione**: Implementare autenticazione robusta usando provider di identità esterni (Microsoft Entra ID), applicare corretta validazione dei token e non accettare mai token non esplicitamente emessi per il proprio server MCP  

- **Prevenzione degli Attacchi AI**: Distribuire Microsoft Prompt Shields e Azure Content Safety per difendersi da injection indiretta di prompt e attacchi di avvelenamento strumenti, validando i metadati degli strumenti e monitorando cambiamenti dinamici  

- **Sicurezza di Sessione e Trasporto**: Usare ID di sessione crittograficamente sicuri, non deterministici e associati all'identità utente, implementare una corretta gestione del ciclo di vita della sessione e non usare mai le sessioni per l'autenticazione  

- **Best Practice di Sicurezza OAuth**: Prevenire attacchi confused deputy tramite consenso esplicito dell'utente per client registrati dinamicamente, corretta implementazione OAuth 2.1 con PKCE e rigorosa validazione degli URI di reindirizzamento  

- **Principi di Sicurezza dei Token**: Evitare anti-pattern di token passthrough, validare le affermazioni sul pubblico del token, implementare token a breve durata con rotazione sicura e mantenere confini di fiducia chiari  

- **Sicurezza Completa della Supply Chain**: Trattare tutti i componenti dell'ecosistema AI (modelli, embedding, provider di contesto, API esterne) con la stessa rigorosità di sicurezza delle dipendenze software tradizionali  

- **Evoluzione Continua**: Rimanere aggiornati con le specifiche MCP in rapido sviluppo, contribuire agli standard della comunità di sicurezza e mantenere posture di sicurezza adattive man mano che il protocollo matura  

- **Integrazione con la Sicurezza Microsoft**: Sfruttare l'ecosistema di sicurezza completo di Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) per una protezione avanzata delle distribuzioni MCP  

## Risorse Complete

### **Documentazione Ufficiale di Sicurezza MCP**  
- [Specifiche MCP (Corrente: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [Best Practice di Sicurezza MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [Specifiche di Autorizzazione MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [Repository GitHub MCP](https://github.com/modelcontextprotocol)  

### **Standard di Sicurezza e Best Practice**  
- [Best Practice di Sicurezza OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Sicurezza Applicazioni Web](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 per Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft Digital Defense Report](https://aka.ms/mddr)  

### **Ricerca e Analisi sulla Sicurezza AI**  
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Attacchi di Avvelenamento Strumenti (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Soluzioni di Sicurezza Microsoft**
- [Documentazione Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Servizio Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Sicurezza Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Best Practice per la Gestione dei Token Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Guide di Implementazione e Tutorial**
- [Azure API Management come Gateway di Autenticazione MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Autenticazione Microsoft Entra ID con Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Archiviazione Sicura dei Token e Crittografia (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps e Sicurezza della Supply Chain**
- [Sicurezza Azure DevOps](https://azure.microsoft.com/products/devops)
- [Sicurezza Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Il Viaggio di Microsoft nella Sicurezza della Supply Chain](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentazione Aggiuntiva sulla Sicurezza**

Per una guida completa sulla sicurezza, fare riferimento a questi documenti specializzati in questa sezione:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Best practice complete per la sicurezza nelle implementazioni MCP
- **[Implementazione Azure Content Safety](./azure-content-safety-implementation.md)** - Esempi pratici di implementazione per l'integrazione di Azure Content Safety  
- **[Controlli di Sicurezza MCP 2025](./mcp-security-controls-2025.md)** - Controlli e tecniche di sicurezza più recenti per le distribuzioni MCP
- **[Riferimento Rapido Best Practice MCP](./mcp-best-practices.md)** - Guida rapida per le pratiche essenziali di sicurezza MCP

---

## Cosa c'è dopo

Successivo: [Capitolo 3: Iniziare](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->