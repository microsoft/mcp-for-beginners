# Best Practice di Sicurezza MCP - Aggiornamento Settembre 2026

Questa guida completa delinea le best practice essenziali per la sicurezza nell'implementazione di sistemi Model Context Protocol (MCP) basati su
**Specifiche MCP 2026-07-28** e gli standard industriali attuali. Queste
pratiche affrontano sia le tradizionali preoccupazioni di sicurezza sia le minacce specifiche dell'IA
uniche per le implementazioni MCP.


## Requisiti Critici di Sicurezza

### Controlli di Sicurezza Obbligatori (Requisiti MUST)

1. **Validazione del Token**: I server MCP **NON DEVONO** accettare alcun token che non sia stato esplicitamente emesso per il server MCP stesso
2. **Verifica dell'Autorizzazione**: I server MCP che implementano l'autorizzazione **DEVONO** verificare TUTTE le richieste in ingresso e **NON DEVONO** utilizzare sessioni per l'autenticazione  
3. **Consenso dell'Utente**: I server proxy MCP che utilizzano ID client statici di terze parti **DEVONO** ottenere il consenso esplicito per ogni client MCP prima di inoltrare un flusso di autorizzazione
4. **Sicurezza dello State Handle**: I server MCP **NON DEVONO** trattare il possesso di un
	state handle dell'applicazione come autenticazione e **DEVONO** autorizzare ogni
	richiesta che lo utilizza

## Pratiche Fondamentali di Sicurezza

### 1. Validazione e Sanitizzazione degli Input
- **Validazione Completa degli Input**: Validare e sanificare tutti gli input per prevenire attacchi di injection, problemi di confused deputy e vulnerabilità di prompt injection
- **Applicazione dello Schema dei Parametri**: Implementare una rigorosa validazione dello schema JSON per tutti i parametri degli strumenti e gli input API
- **Filtro dei Contenuti**: Usare Microsoft Prompt Shields e Azure Content Safety per filtrare contenuti dannosi in prompt e risposte
- **Sanitizzazione degli Output**: Validare e sanificare tutti gli output del modello prima di presentarli agli utenti o a sistemi a valle

### 2. Eccellenza in Autenticazione e Autorizzazione  
- **Provider di Identità Esterni**: Delegare l'autenticazione a provider di identità consolidati (Microsoft Entra ID, provider OAuth 2.1) invece di implementare autenticazioni personalizzate
- **Registrazione Client**: Preferire i Documenti Metadata Client ID o la preregistrazione; usare la Registrazione Dinamica Client deprecata solo per compatibilità
- **Permessi Granulari**: Implementare permessi specifici e dettagliati per ogni strumento seguendo il principio del minimo privilegio
- **Gestione del Ciclo di Vita dei Token**: Usare token di accesso a breve durata con rotazione sicura e valida con il pubblico appropriato
- **Autenticazione Multi-Fattore**: Richiedere MFA per tutti gli accessi amministrativi e operazioni sensibili

### 3. Protocolli di Comunicazione Sicuri
- **Transport Layer Security**: Usare HTTPS con corretta validazione del certificato
	per comunicazioni HTTP MCP remote; usare isolamento processo e
	credenziali d'ambiente per server stdio locali
- **Crittografia End-to-End**: Implementare livelli aggiuntivi di crittografia per dati altamente sensibili in transito e a riposo
- **Gestione dei Certificati**: Mantenere una corretta gestione del ciclo di vita dei certificati con processi automatizzati di rinnovo
- **Applicazione della Versione del Protocollo**: Usare MCP `2026-07-28`, includere i metadati di versione richiesti in ogni richiesta e rifiutare versioni non supportate


### 4. Limitazione Avanzata della Velocità e Protezione delle Risorse
- **Limitazione Multi-livello della Velocità**: Implementare limitazioni di velocità per utente, credenziale,
  operazione, strumento e risorsa per prevenire abusi
- **Limitazione Adattiva della Velocità**: Usare limitazioni basate su apprendimento automatico che si adattano ai modelli d'uso e indicatori di minaccia
- **Gestione della Quota delle Risorse**: Impostare limiti appropriati per risorse computazionali, uso di memoria e tempo di esecuzione
- **Protezione DDoS**: Deploy sistemi completi di protezione DDoS e analisi del traffico

### 5. Registrazione e Monitoraggio Completi
- **Audit Logging Strutturato**: Implementare log dettagliati e ricercabili per tutte le operazioni MCP, esecuzioni strumenti e eventi di sicurezza
- **Monitoraggio della Sicurezza in Tempo Reale**: Deploy sistemi SIEM con rilevamento anomalie potenziato da IA per carichi di lavoro MCP
- **Logging conforme alla Privacy**: Registrare eventi di sicurezza rispettando requisiti e normative sulla privacy dei dati
- **Integrazione Risposta Incidenti**: Collegare i sistemi di logging a flussi di lavoro automatizzati di risposta agli incidenti

### 6. Pratiche Avanzate di Archiviazione Sicura
- **Moduli di Sicurezza Hardware**: Usare archiviazione chiavi supportata da HSM (Azure Key Vault, AWS CloudHSM) per operazioni crittografiche critiche
- **Gestione delle Chiavi di Crittografia**: Implementare rotazione, segregazione e controlli d'accesso appropriati per le chiavi di crittografia
- **Gestione dei Segreti**: Archiviare tutte le chiavi API, token e credenziali in sistemi dedicati di gestione dei segreti
- **Classificazione dei Dati**: Classificare i dati in base ai livelli di sensibilità e applicare misure di protezione appropriate

### 7. Gestione Avanzata dei Token
- **Prevenzione del Passaggio Diretto dei Token**: Vietare esplicitamente schemi di token passthrough che bypassano i controlli di sicurezza
- **Validazione del Pubblico**: Verificare sempre che le audience claim del token corrispondano all'identità MCP prevista
- **Autorizzazione Basata su Claims**: Implementare autorizzazioni dettagliate basate su claims del token e attributi utente
- **Binding del Token**: Validare che i token siano destinati alla risorsa MCP prevista e
	legare gli state handle applicativi lato server al principale autenticato

### 8. Stato Applicativo Sicuro

- **State Handle Crittografici**: Generare handle opachi e non deterministici
	per lo stato che attraversa richieste
- **Binding Specifico per Utente**: Legare ogni handle lato server al principale autenticato; non fidarsi di un ID utente fornito dal client
- **Controlli del Ciclo di Vita**: Scadere e revocare handle, e definire come i chiamanti
	recuperano da stato obsoleto
- **Autorizzazione per ogni Richiesta**: Ricontrollare l'autorizzazione ogni volta che un handle viene
	presentato; un handle è un nome, non una credenziale


### 9. Controlli di Sicurezza Specifici per l'IA
- **Difesa da Prompt Injection**: Distribuire Microsoft Prompt Shields con spotlighting, delimitatori e tecniche di datamarking
- **Prevenzione di Avvelenamento degli Strumenti**: Validare i metadata degli strumenti, monitorare cambiamenti dinamici e verificare l'integrità degli strumenti
- **Validazione degli Output del Modello**: Scansionare gli output dei modelli per potenziali fughe di dati, contenuti dannosi o violazioni delle politiche di sicurezza
- **Protezione della Finestra di Contesto**: Implementare controlli per prevenire avvelenamenti della finestra di contesto e attacchi di manipolazione

### 10. Sicurezza nell'Esecuzione degli Strumenti
- **Sandboxing dell'Esecuzione**: Eseguire gli strumenti in ambienti containerizzati e isolati con limiti di risorse
- **Separazione dei Privilegi**: Eseguire gli strumenti con privilegi minimi necessari e account di servizio separati
- **Isolamento di Rete**: Implementare segmentazione di rete per gli ambienti di esecuzione degli strumenti
- **Monitoraggio dell'Esecuzione**: Monitorare l'esecuzione degli strumenti per comportamenti anomali, uso delle risorse e violazioni di sicurezza

### 11. Validazione Continua della Sicurezza
- **Test di Sicurezza Automatizzati**: Integrare test di sicurezza nelle pipeline CI/CD con strumenti come GitHub Advanced Security
- **Gestione delle Vulnerabilità**: Scansionare regolarmente tutte le dipendenze, inclusi modelli IA e servizi esterni
- **Test di Penetrazione**: Condurre valutazioni regolari di sicurezza specificamente rivolte alle implementazioni MCP
- **Revisioni del Codice di Sicurezza**: Implementare revisioni di sicurezza obbligatorie per tutte le modifiche di codice relative a MCP

### 12. Sicurezza della Supply Chain per l'IA
- **Verifica dei Componenti**: Verificare provenienza, integrità e sicurezza di tutti i componenti IA (modelli, embeddings, API)
- **Gestione delle Dipendenze**: Mantenere inventari aggiornati di tutti i software e dipendenze IA con tracciamento delle vulnerabilità
- **Repository Affidabili**: Usare fonti verificate e affidabili per tutti i modelli IA, librerie e strumenti
- **Monitoraggio della Supply Chain**: Monitorare continuamente compromissioni nei fornitori di servizi IA e repository di modelli


## Modelli di Sicurezza Avanzati

### Architettura Zero Trust per MCP
- **Mai Fidarsi, Sempre Verificare**: Implementare una verifica continua per tutti i partecipanti MCP
- **Micro-segmentazione**: Isolare i componenti MCP con controlli granulari di rete e identità
- **Accesso Condizionale**: Implementare controlli di accesso basati sul rischio che si adattano al contesto e al comportamento
- **Valutazione del Rischio Continua**: Valutare dinamicamente la postura di sicurezza basata sugli indicatori di minaccia attuali

### Implementazione di AI che Preserva la Privacy
- **Minimizzazione dei Dati**: Esporre solo i dati minimi necessari per ogni operazione MCP
- **Privacy Differenziale**: Implementare tecniche che preservano la privacy per l'elaborazione di dati sensibili
- **Crittografia Omonima**: Usare tecniche crittografiche avanzate per il calcolo sicuro su dati crittografati
- **Apprendimento Federato**: Implementare approcci di apprendimento distribuito che preservano la località e la privacy dei dati

### Risposta agli Incidenti per Sistemi AI
- **Procedure Specifiche per Incidenti AI**: Sviluppare procedure di risposta agli incidenti su misura per minacce specifiche di AI e MCP
- **Risposta Automatica**: Implementare contenimento e rimedio automatizzati per incidenti comuni di sicurezza AI  
- **Capacità Forensi**: Mantenere la prontezza forense per compromissioni di sistemi AI e violazioni di dati
- **Procedure di Recupero**: Stabilire procedure per il recupero da avvelenamento di modelli AI, attacchi di iniezione prompt e compromissioni di servizi

## Risorse & Standard per l'Implementazione

### 🏔️ Formazione Pratica sulla Sicurezza
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Workshop pratico completo per la sicurezza dei server MCP in Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Architettura di riferimento e guida all'implementazione OWASP MCP Top 10

### Documentazione Ufficiale MCP
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Specifica attuale del protocollo MCP
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Linee guida ufficiali sulla sicurezza
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Modelli di autorizzazione HTTP
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Requisiti di trasporto

### Soluzioni Microsoft per la Sicurezza
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Protezione avanzata contro l'iniezione di prompt
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Filtraggio completo dei contenuti AI
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Gestione enterprise di identità e accessi
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Gestione sicura di segreti e credenziali
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Scansione della sicurezza della catena di fornitura e del codice

### Standard & Framework di Sicurezza
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Linee guida attuali per la sicurezza OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Rischi di sicurezza per applicazioni web
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Rischi specifici di sicurezza AI
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Gestione completa del rischio AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistemi di gestione della sicurezza delle informazioni

### Guide & Tutorial di Implementazione
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Modelli di autenticazione aziendale
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrazione provider di identità
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Best practice per la gestione dei token
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Modelli avanzati di crittografia

### Risorse Avanzate di Sicurezza
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Pratiche di sviluppo sicuro
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Test di sicurezza specifici per AI
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologia di modellazione delle minacce AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Tecniche AI che preservano la privacy

### Conformità & Governance
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Conformità sulla privacy nei sistemi AI
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Implementazione responsabile di AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Controlli di sicurezza per fornitori di servizi AI
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Requisiti di conformità per AI in ambito sanitario

### DevSecOps & Automazione
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Pipeline di sviluppo AI sicure
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Validazione continua della sicurezza
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Distribuzione sicura dell'infrastruttura
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sicurezza della containerizzazione per carichi AI

### Monitoraggio & Risposta agli Incidenti  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Soluzioni di monitoraggio complete
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procedure specifiche per incidenti AI
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Gestione delle informazioni e degli eventi di sicurezza

- [Threat Intelligence per l'IA](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - fonti di threat intelligence per l'IA

## 🔄 Miglioramento Continuo

### Rimanere Aggiornati con gli Standard in Evoluzione
- **Aggiornamenti delle Specifiche MCP**: Monitorare le modifiche alle specifiche ufficiali MCP e gli avvisi di sicurezza
- **Threat Intelligence**: Iscriversi a feed di minacce di sicurezza per IA e banche dati di vulnerabilità  
- **Coinvolgimento della Comunità**: Partecipare alle discussioni della comunità di sicurezza MCP e ai gruppi di lavoro
- **Valutazione Regolare**: Condurre valutazioni trimestrali della postura di sicurezza e aggiornare le pratiche di conseguenza

### Contribuire alla Sicurezza MCP
- **Ricerca sulla Sicurezza**: Contribuire alla ricerca sulla sicurezza MCP e ai programmi di divulgazione delle vulnerabilità
- **Condivisione delle Migliori Pratiche**: Condividere implementazioni di sicurezza e lezioni apprese con la comunità
- **Sviluppo degli Standard**: Partecipare allo sviluppo delle specifiche MCP e alla creazione di standard di sicurezza
- **Sviluppo di Strumenti**: Sviluppare e condividere strumenti e librerie di sicurezza per l'ecosistema MCP

---

*Questo documento riflette le migliori pratiche di sicurezza MCP al 9 settembre 2026,
basate sulla specifica MCP `2026-07-28`. Le pratiche di sicurezza dovrebbero essere
regolarmente riviste man mano che il protocollo e il panorama delle minacce evolvono.*

## Cosa Succede Dopo

- Leggi: [Migliori Pratiche di Sicurezza MCP](./mcp-security-best-practices.md)
- Torna a: [Panoramica del Modulo di Sicurezza](./README.md)
- Continua con: [Modulo 3: Iniziare](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->