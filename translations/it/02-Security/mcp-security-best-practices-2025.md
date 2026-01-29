# MCP Security Best Practices - Aggiornamento Dicembre 2025

> **Importante**: Questo documento riflette i più recenti requisiti di sicurezza della [Specificazione MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) e le ufficiali [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Fare sempre riferimento alla specifica corrente per le indicazioni più aggiornate.

## Pratiche di Sicurezza Essenziali per le Implementazioni MCP

Il Model Context Protocol introduce sfide di sicurezza uniche che vanno oltre la sicurezza software tradizionale. Queste pratiche affrontano sia i requisiti di sicurezza fondamentali sia le minacce specifiche MCP, inclusi prompt injection, avvelenamento degli strumenti, hijacking di sessione, problemi di confused deputy e vulnerabilità di token passthrough.

### **Requisiti di Sicurezza OBBLIGATORI** 

**Requisiti Critici dalla Specifica MCP:**

### **Requisiti di Sicurezza OBBLIGATORI** 

**Requisiti Critici dalla Specifica MCP:**

> **NON DEVE**: I server MCP **NON DEVONO** accettare token che non siano stati esplicitamente emessi per il server MCP
> 
> **DEVE**: I server MCP che implementano l’autorizzazione **DEVONO** verificare TUTTE le richieste in ingresso
>  
> **NON DEVE**: I server MCP **NON DEVONO** usare sessioni per l’autenticazione
>
> **DEVE**: I server proxy MCP che usano ID client statici **DEVONO** ottenere il consenso dell’utente per ogni client registrato dinamicamente

---

## 1. **Sicurezza dei Token & Autenticazione**

**Controlli di Autenticazione & Autorizzazione:**
   - **Revisione rigorosa dell’autorizzazione**: Condurre audit completi della logica di autorizzazione del server MCP per garantire che solo utenti e client previsti possano accedere alle risorse
   - **Integrazione con provider di identità esterni**: Usare provider di identità consolidati come Microsoft Entra ID invece di implementare autenticazioni personalizzate
   - **Validazione del pubblico del token**: Validare sempre che i token siano stati esplicitamente emessi per il proprio server MCP - non accettare mai token upstream
   - **Ciclo di vita corretto del token**: Implementare rotazione sicura dei token, politiche di scadenza e prevenire attacchi di replay dei token

**Archiviazione protetta dei token:**
   - Usare Azure Key Vault o archivi di credenziali sicuri simili per tutti i segreti
   - Implementare la crittografia dei token sia a riposo che in transito
   - Rotazione regolare delle credenziali e monitoraggio per accessi non autorizzati

## 2. **Gestione delle Sessioni & Sicurezza del Trasporto**

**Pratiche sicure per le sessioni:**
   - **ID sessione crittograficamente sicuri**: Usare ID sessione sicuri e non deterministici generati con generatori di numeri casuali sicuri
   - **Binding specifico per utente**: Legare gli ID sessione alle identità utente usando formati come `<user_id>:<session_id>` per prevenire abusi di sessione cross-user
   - **Gestione del ciclo di vita della sessione**: Implementare scadenza, rotazione e invalidazione adeguate per limitare le finestre di vulnerabilità
   - **Applicazione di HTTPS/TLS**: HTTPS obbligatorio per tutte le comunicazioni per prevenire intercettazioni degli ID sessione

**Sicurezza del livello di trasporto:**
   - Configurare TLS 1.3 dove possibile con gestione corretta dei certificati
   - Implementare certificate pinning per connessioni critiche
   - Rotazione regolare dei certificati e verifica della validità

## 3. **Protezione dalle Minacce Specifiche AI** 🤖

**Difesa da Prompt Injection:**
   - **Microsoft Prompt Shields**: Distribuire AI Prompt Shields per il rilevamento avanzato e il filtraggio di istruzioni dannose
   - **Sanificazione degli input**: Validare e sanificare tutti gli input per prevenire attacchi di injection e problemi di confused deputy
   - **Confini di contenuto**: Usare sistemi di delimitazione e datamarking per distinguere tra istruzioni affidabili e contenuti esterni

**Prevenzione dell’avvelenamento degli strumenti:**
   - **Validazione dei metadati degli strumenti**: Implementare controlli di integrità per le definizioni degli strumenti e monitorare cambiamenti inattesi
   - **Monitoraggio dinamico degli strumenti**: Monitorare il comportamento in runtime e impostare allarmi per pattern di esecuzione inattesi
   - **Workflow di approvazione**: Richiedere approvazione esplicita dell’utente per modifiche agli strumenti e cambiamenti di capacità

## 4. **Controllo Accessi & Permessi**

**Principio del minimo privilegio:**
   - Concedere ai server MCP solo i permessi minimi necessari per la funzionalità prevista
   - Implementare controllo accessi basato su ruoli (RBAC) con permessi granulati
   - Revisioni regolari dei permessi e monitoraggio continuo per escalation di privilegi

**Controlli dei permessi in runtime:**
   - Applicare limiti di risorse per prevenire attacchi di esaurimento risorse
   - Usare isolamento container per gli ambienti di esecuzione degli strumenti  
   - Implementare accesso just-in-time per funzioni amministrative

## 5. **Sicurezza dei Contenuti & Monitoraggio**

**Implementazione della sicurezza dei contenuti:**
   - **Integrazione Azure Content Safety**: Usare Azure Content Safety per rilevare contenuti dannosi, tentativi di jailbreak e violazioni di policy
   - **Analisi comportamentale**: Implementare monitoraggio comportamentale in runtime per rilevare anomalie nell’esecuzione di server MCP e strumenti
   - **Logging completo**: Registrare tutti i tentativi di autenticazione, invocazioni di strumenti ed eventi di sicurezza con archiviazione sicura e a prova di manomissione

**Monitoraggio continuo:**
   - Allarmi in tempo reale per pattern sospetti e tentativi di accesso non autorizzati  
   - Integrazione con sistemi SIEM per gestione centralizzata degli eventi di sicurezza
   - Audit di sicurezza regolari e penetration test delle implementazioni MCP

## 6. **Sicurezza della Supply Chain**

**Verifica dei componenti:**
   - **Scansione delle dipendenze**: Usare scansione automatizzata delle vulnerabilità per tutte le dipendenze software e componenti AI
   - **Validazione della provenienza**: Verificare origine, licenze e integrità di modelli, fonti dati e servizi esterni
   - **Pacchetti firmati**: Usare pacchetti firmati crittograficamente e verificare le firme prima del deployment

**Pipeline di sviluppo sicura:**
   - **GitHub Advanced Security**: Implementare scansione dei segreti, analisi delle dipendenze e analisi statica CodeQL
   - **Sicurezza CI/CD**: Integrare la validazione della sicurezza in tutte le pipeline di deployment automatizzate
   - **Integrità degli artefatti**: Implementare verifica crittografica per artefatti e configurazioni distribuiti

## 7. **Sicurezza OAuth & Prevenzione Confused Deputy**

**Implementazione OAuth 2.1:**
   - **Implementazione PKCE**: Usare Proof Key for Code Exchange (PKCE) per tutte le richieste di autorizzazione
   - **Consenso esplicito**: Ottenere consenso utente per ogni client registrato dinamicamente per prevenire attacchi confused deputy
   - **Validazione URI di redirect**: Implementare validazione rigorosa degli URI di redirect e degli identificatori client

**Sicurezza del proxy:**
   - Prevenire bypass di autorizzazione tramite sfruttamento di ID client statici
   - Implementare workflow di consenso adeguati per accesso API di terze parti
   - Monitorare furto di codici di autorizzazione e accessi API non autorizzati

## 8. **Risposta agli Incidenti & Recupero**

**Capacità di risposta rapida:**
   - **Risposta automatizzata**: Implementare sistemi automatici per rotazione delle credenziali e contenimento delle minacce
   - **Procedure di rollback**: Capacità di tornare rapidamente a configurazioni e componenti noti come sicuri
   - **Capacità forensi**: Tracce di audit dettagliate e logging per indagini sugli incidenti

**Comunicazione & coordinamento:**
   - Procedure chiare di escalation per incidenti di sicurezza
   - Integrazione con team organizzativi di risposta agli incidenti
   - Simulazioni regolari di incidenti di sicurezza ed esercitazioni tabletop

## 9. **Conformità & Governance**

**Conformità normativa:**
   - Assicurare che le implementazioni MCP rispettino requisiti specifici di settore (GDPR, HIPAA, SOC 2)
   - Implementare classificazione dei dati e controlli di privacy per il trattamento dati AI
   - Mantenere documentazione completa per audit di conformità

**Gestione del cambiamento:**
   - Processi formali di revisione della sicurezza per tutte le modifiche ai sistemi MCP
   - Controllo di versione e workflow di approvazione per modifiche di configurazione
   - Valutazioni regolari di conformità e analisi delle lacune

## 10. **Controlli di Sicurezza Avanzati**

**Architettura Zero Trust:**
   - **Mai fidarsi, sempre verificare**: Verifica continua di utenti, dispositivi e connessioni
   - **Micro-segmentazione**: Controlli di rete granulari che isolano singoli componenti MCP
   - **Accesso condizionale**: Controlli di accesso basati sul rischio che si adattano al contesto e comportamento attuali

**Protezione delle applicazioni in runtime:**
   - **Runtime Application Self-Protection (RASP)**: Distribuire tecniche RASP per rilevamento minacce in tempo reale
   - **Monitoraggio delle prestazioni applicative**: Monitorare anomalie di prestazioni che possono indicare attacchi
   - **Policy di sicurezza dinamiche**: Implementare policy di sicurezza che si adattano in base al panorama delle minacce attuale

## 11. **Integrazione con l’Ecosistema di Sicurezza Microsoft**

**Sicurezza Microsoft completa:**
   - **Microsoft Defender for Cloud**: Gestione della postura di sicurezza cloud per carichi di lavoro MCP
   - **Azure Sentinel**: SIEM e SOAR nativi cloud per rilevamento avanzato delle minacce
   - **Microsoft Purview**: Governance dei dati e conformità per workflow AI e fonti dati

**Gestione identità e accessi:**
   - **Microsoft Entra ID**: Gestione identità aziendale con policy di accesso condizionale
   - **Privileged Identity Management (PIM)**: Accesso just-in-time e workflow di approvazione per funzioni amministrative
   - **Protezione dell’identità**: Accesso condizionale basato sul rischio e risposta automatizzata alle minacce

## 12. **Evoluzione Continua della Sicurezza**

**Rimanere aggiornati:**
   - **Monitoraggio della specifica**: Revisione regolare degli aggiornamenti della specifica MCP e dei cambiamenti nelle linee guida di sicurezza
   - **Intelligence sulle minacce**: Integrazione di feed di minacce specifiche AI e indicatori di compromissione
   - **Coinvolgimento nella comunità di sicurezza**: Partecipazione attiva nella comunità di sicurezza MCP e programmi di disclosure delle vulnerabilità

**Sicurezza adattativa:**
   - **Sicurezza basata su Machine Learning**: Usare rilevamento anomalie basato su ML per identificare nuovi pattern di attacco
   - **Analisi predittiva della sicurezza**: Implementare modelli predittivi per identificazione proattiva delle minacce
   - **Automazione della sicurezza**: Aggiornamenti automatici delle policy di sicurezza basati su intelligence sulle minacce e cambiamenti della specifica

---

## **Risorse Critiche per la Sicurezza**

### **Documentazione Ufficiale MCP**
- [Specificazione MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Specificazione Autorizzazione MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Soluzioni di Sicurezza Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Sicurezza Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Standard di Sicurezza**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 per Large Language Models](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Guide di Implementazione**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID con server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Avviso di Sicurezza**: Le pratiche di sicurezza MCP evolvono rapidamente. Verificare sempre rispetto alla [specifica MCP corrente](https://spec.modelcontextprotocol.io/) e alla [documentazione ufficiale di sicurezza](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) prima dell’implementazione.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->