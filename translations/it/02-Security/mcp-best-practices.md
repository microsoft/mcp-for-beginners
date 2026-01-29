# Pratiche di Sicurezza MCP 2025

Questa guida completa delinea le pratiche di sicurezza essenziali per l'implementazione di sistemi Model Context Protocol (MCP) basati sulla più recente **Specificazione MCP 2025-11-25** e sugli standard di settore attuali. Queste pratiche affrontano sia le preoccupazioni di sicurezza tradizionali sia le minacce specifiche dell'IA uniche per le implementazioni MCP.

## Requisiti Critici di Sicurezza

### Controlli di Sicurezza Obbligatori (Requisiti MUST)

1. **Validazione del Token**: I server MCP **NON DEVONO** accettare alcun token che non sia stato esplicitamente emesso per il server MCP stesso
2. **Verifica dell'Autorizzazione**: I server MCP che implementano l'autorizzazione **DEVONO** verificare TUTTE le richieste in ingresso e **NON DEVONO** utilizzare sessioni per l'autenticazione  
3. **Consenso dell'Utente**: I server proxy MCP che utilizzano ID client statici **DEVONO** ottenere il consenso esplicito dell'utente per ogni client registrato dinamicamente
4. **ID Sessione Sicuri**: I server MCP **DEVONO** utilizzare ID sessione crittograficamente sicuri, non deterministici, generati con generatori di numeri casuali sicuri

## Pratiche di Sicurezza Fondamentali

### 1. Validazione e Sanitizzazione degli Input
- **Validazione Completa degli Input**: Validare e sanificare tutti gli input per prevenire attacchi di injection, problemi di confused deputy e vulnerabilità di prompt injection
- **Applicazione dello Schema dei Parametri**: Implementare una rigorosa validazione dello schema JSON per tutti i parametri degli strumenti e gli input API
- **Filtraggio dei Contenuti**: Utilizzare Microsoft Prompt Shields e Azure Content Safety per filtrare contenuti dannosi in prompt e risposte
- **Sanitizzazione dell'Output**: Validare e sanificare tutti gli output del modello prima di presentarli agli utenti o ai sistemi a valle

### 2. Eccellenza in Autenticazione e Autorizzazione  
- **Provider di Identità Esterni**: Delegare l'autenticazione a provider di identità consolidati (Microsoft Entra ID, provider OAuth 2.1) anziché implementare autenticazioni personalizzate
- **Permessi Granulari**: Implementare permessi specifici per strumento seguendo il principio del minimo privilegio
- **Gestione del Ciclo di Vita del Token**: Usare token di accesso a breve durata con rotazione sicura e corretta validazione del pubblico
- **Autenticazione Multi-Fattore**: Richiedere MFA per tutti gli accessi amministrativi e operazioni sensibili

### 3. Protocolli di Comunicazione Sicuri
- **Transport Layer Security**: Usare HTTPS/TLS 1.3 per tutte le comunicazioni MCP con corretta validazione dei certificati
- **Crittografia End-to-End**: Implementare livelli aggiuntivi di crittografia per dati altamente sensibili in transito e a riposo
- **Gestione dei Certificati**: Mantenere una corretta gestione del ciclo di vita dei certificati con processi di rinnovo automatizzati
- **Applicazione della Versione del Protocollo**: Usare la versione corrente del protocollo MCP (2025-11-25) con corretta negoziazione della versione.

### 4. Limitazione Avanzata della Velocità e Protezione delle Risorse
- **Limitazione Multi-livello della Velocità**: Implementare limitazioni di velocità a livello di utente, sessione, strumento e risorsa per prevenire abusi
- **Limitazione Adattativa della Velocità**: Usare limitazioni basate su machine learning che si adattano ai modelli di utilizzo e indicatori di minaccia
- **Gestione delle Quote di Risorse**: Impostare limiti appropriati per risorse computazionali, uso della memoria e tempo di esecuzione
- **Protezione DDoS**: Implementare sistemi completi di protezione DDoS e analisi del traffico

### 5. Logging e Monitoraggio Completi
- **Logging di Audit Strutturato**: Implementare log dettagliati e ricercabili per tutte le operazioni MCP, esecuzioni di strumenti ed eventi di sicurezza
- **Monitoraggio di Sicurezza in Tempo Reale**: Implementare sistemi SIEM con rilevamento anomalie potenziato da AI per i carichi di lavoro MCP
- **Logging Conforme alla Privacy**: Registrare eventi di sicurezza rispettando i requisiti e le normative sulla privacy dei dati
- **Integrazione con la Risposta agli Incidenti**: Collegare i sistemi di logging ai flussi di lavoro automatizzati di risposta agli incidenti

### 6. Pratiche Avanzate di Archiviazione Sicura
- **Moduli di Sicurezza Hardware**: Usare archiviazione di chiavi supportata da HSM (Azure Key Vault, AWS CloudHSM) per operazioni crittografiche critiche
- **Gestione delle Chiavi di Crittografia**: Implementare rotazione, segregazione e controlli di accesso appropriati per le chiavi di crittografia
- **Gestione dei Segreti**: Conservare tutte le chiavi API, token e credenziali in sistemi dedicati di gestione dei segreti
- **Classificazione dei Dati**: Classificare i dati in base ai livelli di sensibilità e applicare misure di protezione appropriate

### 7. Gestione Avanzata dei Token
- **Prevenzione del Passaggio Diretto dei Token**: Vietare esplicitamente i pattern di passaggio diretto dei token che bypassano i controlli di sicurezza
- **Validazione del Pubblico**: Verificare sempre che le affermazioni sul pubblico del token corrispondano all'identità prevista del server MCP
- **Autorizzazione Basata su Claims**: Implementare autorizzazioni granulari basate su claims del token e attributi utente
- **Binding del Token**: Legare i token a sessioni, utenti o dispositivi specifici ove appropriato

### 8. Gestione Sicura delle Sessioni
- **ID Sessione Crittografici**: Generare ID sessione usando generatori di numeri casuali crittograficamente sicuri (non sequenze prevedibili)
- **Binding Specifico per Utente**: Legare gli ID sessione a informazioni specifiche dell'utente usando formati sicuri come `<user_id>:<session_id>`
- **Controlli sul Ciclo di Vita della Sessione**: Implementare meccanismi corretti di scadenza, rotazione e invalidazione della sessione
- **Header di Sicurezza per la Sessione**: Usare header HTTP di sicurezza appropriati per la protezione della sessione

### 9. Controlli di Sicurezza Specifici per l'IA
- **Difesa contro Prompt Injection**: Implementare Microsoft Prompt Shields con spotlighting, delimitatori e tecniche di datamarking
- **Prevenzione dell'Avvelenamento degli Strumenti**: Validare i metadati degli strumenti, monitorare cambiamenti dinamici e verificare l'integrità degli strumenti
- **Validazione dell'Output del Modello**: Scansionare gli output del modello per potenziali fughe di dati, contenuti dannosi o violazioni delle politiche di sicurezza
- **Protezione della Finestra di Contesto**: Implementare controlli per prevenire avvelenamento e manipolazione della finestra di contesto

### 10. Sicurezza nell'Esecuzione degli Strumenti
- **Sandboxing dell'Esecuzione**: Eseguire gli strumenti in ambienti containerizzati e isolati con limiti di risorse
- **Separazione dei Privilegi**: Eseguire gli strumenti con privilegi minimi necessari e account di servizio separati
- **Isolamento di Rete**: Implementare segmentazione di rete per gli ambienti di esecuzione degli strumenti
- **Monitoraggio dell'Esecuzione**: Monitorare l'esecuzione degli strumenti per comportamenti anomali, uso delle risorse e violazioni di sicurezza

### 11. Validazione Continua della Sicurezza
- **Test di Sicurezza Automatizzati**: Integrare test di sicurezza nelle pipeline CI/CD con strumenti come GitHub Advanced Security
- **Gestione delle Vulnerabilità**: Scansionare regolarmente tutte le dipendenze, inclusi modelli IA e servizi esterni
- **Penetration Testing**: Condurre valutazioni di sicurezza regolari specifiche per le implementazioni MCP
- **Revisioni del Codice di Sicurezza**: Implementare revisioni di sicurezza obbligatorie per tutte le modifiche al codice relative a MCP

### 12. Sicurezza della Supply Chain per l'IA
- **Verifica dei Componenti**: Verificare provenienza, integrità e sicurezza di tutti i componenti IA (modelli, embeddings, API)
- **Gestione delle Dipendenze**: Mantenere inventari aggiornati di tutte le dipendenze software e IA con tracciamento delle vulnerabilità
- **Repository Affidabili**: Usare fonti verificate e affidabili per tutti i modelli IA, librerie e strumenti
- **Monitoraggio della Supply Chain**: Monitorare continuamente compromissioni nei fornitori di servizi IA e repository di modelli

## Pattern Avanzati di Sicurezza

### Architettura Zero Trust per MCP
- **Mai Fidarsi, Sempre Verificare**: Implementare verifica continua per tutti i partecipanti MCP
- **Micro-segmentazione**: Isolare i componenti MCP con controlli granulari di rete e identità
- **Accesso Condizionale**: Implementare controlli di accesso basati sul rischio che si adattano al contesto e al comportamento
- **Valutazione Continua del Rischio**: Valutare dinamicamente la postura di sicurezza basata sugli indicatori di minaccia attuali

### Implementazione di IA che Preserva la Privacy
- **Minimizzazione dei Dati**: Esporre solo i dati strettamente necessari per ogni operazione MCP
- **Privacy Differenziale**: Implementare tecniche di preservazione della privacy per il trattamento di dati sensibili
- **Crittografia Omomorfica**: Usare tecniche avanzate di crittografia per calcoli sicuri su dati cifrati
- **Apprendimento Federato**: Implementare approcci di apprendimento distribuito che preservano la località e la privacy dei dati

### Risposta agli Incidenti per Sistemi IA
- **Procedure Specifiche per Incidenti IA**: Sviluppare procedure di risposta agli incidenti su misura per minacce specifiche di IA e MCP
- **Risposta Automatizzata**: Implementare contenimento e rimedio automatizzati per incidenti di sicurezza IA comuni  
- **Capacità Forensi**: Mantenere prontezza forense per compromissioni di sistemi IA e violazioni di dati
- **Procedure di Recupero**: Stabilire procedure per il recupero da avvelenamento di modelli IA, attacchi di prompt injection e compromissioni di servizio

## Risorse e Standard per l'Implementazione

### Documentazione Ufficiale MCP
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Specifica corrente del protocollo MCP
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Linee guida ufficiali di sicurezza
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Pattern di autenticazione e autorizzazione
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Requisiti di sicurezza del livello di trasporto

### Soluzioni di Sicurezza Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Protezione avanzata contro prompt injection
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Filtraggio completo dei contenuti IA
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Gestione identità e accessi aziendali
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Gestione sicura di segreti e credenziali
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Scansione della sicurezza della supply chain e del codice

### Standard e Framework di Sicurezza
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Linee guida di sicurezza OAuth attuali
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Rischi di sicurezza per applicazioni web
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Rischi di sicurezza specifici per IA
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Gestione completa del rischio IA
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistemi di gestione della sicurezza delle informazioni

### Guide e Tutorial per l'Implementazione
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Pattern di autenticazione aziendale
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrazione provider di identità
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Pratiche migliori per la gestione dei token
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Pattern avanzati di crittografia

### Risorse Avanzate di Sicurezza
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Pratiche di sviluppo sicuro
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Test di sicurezza specifici per IA
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologia di modellazione delle minacce IA
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Tecniche di IA che preservano la privacy

### Conformità e Governance
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Conformità alla privacy nei sistemi IA
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Implementazione responsabile dell'IA
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Controlli di sicurezza per fornitori di servizi IA
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Requisiti di conformità IA per la sanità

### DevSecOps e Automazione
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Pipeline di sviluppo IA sicure
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Validazione continua della sicurezza
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Distribuzione sicura dell'infrastruttura
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sicurezza della containerizzazione dei carichi IA

### Monitoraggio e Risposta agli Incidenti  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Soluzioni di monitoraggio complete
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procedure specifiche per incidenti IA
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Gestione delle informazioni e degli eventi di sicurezza
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Fonti di intelligence sulle minacce IA

## 🔄 Miglioramento Continuo

### Rimanere Aggiornati con Standard in Evoluzione
- **Aggiornamenti della Specifica MCP**: Monitorare i cambiamenti ufficiali della specifica MCP e gli avvisi di sicurezza
- **Intelligence sulle Minacce**: Iscriversi a feed di minacce di sicurezza IA e database di vulnerabilità  
- **Coinvolgimento nella Comunità**: Partecipare a discussioni e gruppi di lavoro sulla sicurezza MCP
- **Valutazione Regolare**: Condurre valutazioni trimestrali della postura di sicurezza e aggiornare le pratiche di conseguenza

### Contribuire alla Sicurezza MCP
- **Ricerca sulla Sicurezza**: Contribuire alla ricerca sulla sicurezza MCP e ai programmi di divulgazione delle vulnerabilità
- **Condivisione delle Best Practice**: Condividere implementazioni di sicurezza e lezioni apprese con la comunità
- **Sviluppo Standard**: Partecipare allo sviluppo delle specifiche MCP e alla creazione di standard di sicurezza  
- **Sviluppo Strumenti**: Sviluppare e condividere strumenti e librerie di sicurezza per l'ecosistema MCP  

---

*Questo documento riflette le migliori pratiche di sicurezza MCP al 18 dicembre 2025, basate sulla Specifica MCP 2025-11-25. Le pratiche di sicurezza dovrebbero essere regolarmente riviste e aggiornate man mano che il protocollo e il panorama delle minacce evolvono.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->