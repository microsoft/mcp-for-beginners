# Controlli di Sicurezza MCP - Aggiornamento Settembre 2026

> **Standard attuale:** Questo documento riflette
> [Specifiche MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> e le ufficiali
> [Best Practice di Sicurezza MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Il Model Context Protocol (MCP) è maturato significativamente con controlli di sicurezza migliorati che affrontano sia la sicurezza software tradizionale sia le minacce specifiche dell’AI. Questo documento fornisce controlli di sicurezza completi per implementazioni MCP sicure allineate al framework OWASP MCP Top 10.

## 🏔️ Formazione Pratica sulla Sicurezza

Per un’esperienza pratica nell’implementazione della sicurezza, raccomandiamo il **[Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - una spedizione guidata completa per mettere in sicurezza i server MCP in Azure utilizzando la metodologia "vulnerabile → exploit → correzione → convalida".

Tutti i controlli di sicurezza in questo documento sono allineati con la **[Guida di Sicurezza Azure MCP OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, che fornisce architetture di riferimento e indicazioni specifiche per l’implementazione Azure sui rischi OWASP MCP Top 10.

## **Requisiti di Sicurezza OBBLIGATORI**

### **Divieti Critici dalle Specifiche MCP:**

> **VIETATO**: I server MCP **NON DEVONO** accettare alcun token che non sia stato esplicitamente emesso per il server MCP
>
> **PROIBITO**: I server MCP **NON DEVONO** utilizzare sessioni per l’autenticazione  
>
> **RICHIESTO**: I server MCP che implementano l’autorizzazione **DEVONO** verificare TUTTE le richieste in ingresso
>
> **OBBLIGATORIO**: I proxy server MCP che utilizzano un client ID statico di terze parti
> **DEVONO** ottenere il consenso per ogni client MCP prima di inoltrare l’autorizzazione

---

## 1. **Controlli di Autenticazione e Autorizzazione**

### **Integrazione con Fornitore di Identità Esterno**

**Specifica MCP `2026-07-28`** consente ai server MCP di delegare
l'autenticazione a fornitori di identità esterni. L’autorizzazione per
trasporti HTTP è valutata per richiesta; i server locali stdio invece ottengono
le credenziali dal proprio ambiente.

**Rischio OWASP MCP affrontato**: [MCP07 - Autenticazione & Autorizzazione Insufficienti](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Benefici di Sicurezza:**
1. **Elimina Rischi di Autenticazione Personalizzata**: Riduce la superficie di vulnerabilità evitando implementazioni di autenticazione personalizzate
2. **Sicurezza di Livello Aziendale**: Sfrutta provider di identità affermati come Microsoft Entra ID con funzionalità di sicurezza avanzate
3. **Gestione Centralizzata dell’Identità**: Semplifica gestione del ciclo di vita utente, controllo accessi e auditing di compliance
4. **Autenticazione Multi-Fattore**: Eredita capacità MFA dai provider di identità aziendali
5. **Policy di Accesso Condizionale**: Beneficia di controlli di accesso basati sul rischio e autenticazione adattiva

**Requisiti di Implementazione:**
- **Registrazione Client**: Preferire Documenti di Metadata Client ID o
  la preregistrazione; usare la Registrazione Dinamica Client deprecata solo per
  compatibilità
- **Validazione Audience Token**: Verificare che tutti i token siano esplicitamente emessi per il server MCP
- **Verifica Emittente**: Validare che l’emittente del token corrisponda al provider di identità atteso
- **Verifica Firma**: Validazione crittografica dell’integrità del token
- **Applicazione Scadenza**: Applicazione rigorosa dei limiti di vita del token
- **Validazione Scope**: Assicurare che i token contengano le autorizzazioni appropriate per le operazioni richieste

### **Sicurezza della Logica di Autorizzazione**

**Controlli Critici:**
- **Audit Completi di Autorizzazione**: Revisioni di sicurezza regolari di tutti i punti decisionali di autorizzazione
- **Default Sicuri**: Negare accesso quando la logica di autorizzazione non può prendere una decisione definitiva
- **Confini di Permesso**: Separazione chiara tra diversi livelli di privilegi e accesso alle risorse
- **Registrazione Auditing**: Logging completo di tutte le decisioni di autorizzazione per monitoraggio di sicurezza
- **Revisioni di Accesso Regolari**: Convalida periodica dei permessi degli utenti e assegnazioni di privilegi

## 2. **Controlli di Sicurezza dei Token & Anti-Passthrough**

**Rischio OWASP MCP affrontato**: [MCP01 - Errata Gestione Token & Esposizione Segreti](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Prevenzione del Passthrough dei Token**

**Il passthrough dei token è esplicitamente proibito** nelle Specifiche di Autorizzazione MCP a causa di rischi critici di sicurezza:

**Rischi di Sicurezza Affrontati:**
- **Circumvenzione dei Controlli**: Elude controlli essenziali come limitazione di velocità, convalida richieste e monitoraggio traffico
- **Rottura di Responsabilità**: Rende impossibile identificare il client, compromettendo tracce di auditing e indagini sugli incidenti
- **Esfiltrazione tramite Proxy**: Consente attori malevoli di usare server come proxy per accesso non autorizzato ai dati
- **Violazioni del Confine di Fiducia**: Rompe assunzioni di fiducia dei servizi a valle riguardo l'origine dei token
- **Movimento Laterale**: Token compromessi su più servizi permettono una più ampia espansione degli attacchi

**Controlli di Implementazione:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **Modelli di Gestione Sicura dei Token**

**Best Practice:**
- **Token a Vita Breve**: Minimizzare la finestra di esposizione con frequente rotazione dei token
- **Emissione Just-in-Time**: Emettere token solo quando necessari per operazioni specifiche
- **Archiviazione Sicura**: Usare moduli di sicurezza hardware (HSM) o vault di chiavi sicuri
- **Binding del Token**: Validare audience e emittente del token per la risorsa, client e operazione MCP prevista
  
- **Monitoraggio & Allerta**: Rilevazione in tempo reale di uso improprio dei token o modelli di accesso non autorizzati

## 3. **Controlli di Sicurezza dello Stato dell’Applicazione**

### **Prevenzione del Dirottamento dello Stato Handle**

**Vettori di Attacco Affrontati:**
- **Individuazione Handle**: Identificatori prevedibili espongono lo stato di un altro chiamante
- **Riutilizzo tra Utenti**: Un handle rubato è usato con un’identità differente
- **Autorizzazione Implicita**: Il possesso di un handle è trattato erroneamente come prova di accesso
  

**Controlli sullo Stato Handle:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**Sicurezza del Trasporto:**
- **Applicazione HTTPS**: Richiedere HTTPS per trasporti HTTP remoti
- **Gestione Credenziali**: Inviare e validare autorizzazioni a ogni richiesta HTTP
- **Isolamento stdio**: Proteggere i server locali stdio tramite isolamento del processo e
  controlli credenziali ambiente

### **Considerazioni Stateful vs Stateless**

MCP `2026-07-28` è stateless al livello protocollo. Le applicazioni possono comunque
mantenere stato restituendo un handle esplicito da una chiamata tool e accettandolo
come argomento ordinario nelle chiamate successive.

- Memorizzare lo stato indipendentemente da una singola connessione di trasporto.
- Legare gli state handle al principale autenticato lato server.
- Trattare un handle come un nome, non come una credenziale di tipo bearer.
- Definire comportamento di scadenza e recupero per handle obsoleti.

## 4. **Controlli di Sicurezza Specifici per AI**

**Rischi OWASP MCP affrontati**:

- [MCP06 - Sovversione del Flusso di Intenti](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Avvelenamento degli Strumenti](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Iniezione e Esecuzione di Comandi](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Difesa contro l'Iniezione di Prompt**

**Integrazione Microsoft Prompt Shields:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**Controlli di Implementazione:**
- **Sanitizzazione dell'Input**: Validazione e filtraggio completi di tutti gli input utente
- **Definizione dei Confini del Contenuto**: Separazione chiara tra istruzioni di sistema e contenuto utente
- **Gerarchia delle Istruzioni**: Regole di precedenza adeguate per istruzioni in conflitto
- **Monitoraggio dell'Output**: Rilevamento di output potenzialmente dannosi o manipolati

### **Prevenzione dell'Avvelenamento degli Strumenti**

**Framework di Sicurezza degli Strumenti:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**Gestione Dinamica degli Strumenti:**
- **Workflow di Approvazione**: Consenso esplicito dell'utente per modifiche agli strumenti
- **Capacità di Ripristino**: Possibilità di tornare a versioni precedenti degli strumenti
- **Audit delle Modifiche**: Storico completo delle modifiche nella definizione degli strumenti
- **Valutazione del Rischio**: Valutazione automatizzata della postura di sicurezza degli strumenti

## 5. **Prevenzione degli Attacchi Confused Deputy**

### **Sicurezza del Proxy OAuth**

**Controlli per la Prevenzione degli Attacchi:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Requisiti di Implementazione:**
- **Registrazione del Client**: Preferire la preregistrazione o i Documenti Metadata Client ID
  ; trattare la Registrazione Dinamica del Client come fallback di compatibilità
- **Verifica del Consenso Utente**: I proxy MCP che usano un client di terze parti statico
  devono ottenere il consenso per cliente prima di inoltrare l'autorizzazione
- **Validazione URI di Redirect**: Validazione rigorosa basata su whitelist delle destinazioni di redirect
- **Protezione del Codice di Autorizzazione**: Codici a breve durata con enforcement di uso singolo
- **Verifica dell'Identità del Client**: Validazione robusta delle credenziali e metadata del client

## 6. **Sicurezza dell'Esecuzione degli Strumenti**

### **Sandboxing e Isolamento**

**Isolamento Basato su Container:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**Isolamento dei Processi:**
- **Contesti di Processo Separati**: Ogni esecuzione di strumento in uno spazio di processo isolato
- **Comunicazione Inter-Processo**: Meccanismi IPC sicuri con validazione
- **Monitoraggio dei Processi**: Analisi del comportamento in runtime e rilevamento anomalie
- **Applicazione delle Risorse**: Limiti rigidi su CPU, memoria e operazioni I/O

### **Implementazione del Principio del Minimo Privilegio**

**Gestione dei Permessi:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **Controlli di Sicurezza della Supply Chain**

**Rischio MCP OWASP Affrontato**: [MCP04 - Attacchi alla Supply Chain Software & Manomissione delle Dipendenze](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Verifica delle Dipendenze**

**Sicurezza Completa dei Componenti:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **Monitoraggio Continuo**

**Rilevamento delle Minacce alla Supply Chain:**
- **Monitoraggio della Salute delle Dipendenze**: Valutazione continua di tutte le dipendenze per problemi di sicurezza
- **Integrazione di Threat Intelligence**: Aggiornamenti in tempo reale sulle minacce emergenti alla supply chain
- **Analisi Comportamentale**: Rilevamento di comportamenti insoliti in componenti esterni
- **Risposta Automatizzata**: Contenimento immediato dei componenti compromessi

## 8. **Controlli di Monitoraggio e Rilevamento**

**Rischio MCP OWASP Affrontato**: [MCP08 - Mancanza di Audit e Telemetria](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Security Information and Event Management (SIEM)**

**Strategia Completa di Logging:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **Rilevamento delle Minacce in Tempo Reale**

**Analisi Comportamentale:**
- **User Behavior Analytics (UBA)**: Rilevamento di modelli insoliti di accesso utente
- **Entity Behavior Analytics (EBA)**: Monitoraggio del comportamento di server MCP e strumenti
- **Rilevamento Anomalie con Machine Learning**: Identificazione di minacce di sicurezza potenziata dall'IA
- **Correlazione con Threat Intelligence**: Confronto delle attività osservate con schemi di attacco noti

## 9. **Risposta agli Incidenti e Recupero**

### **Capacità di Risposta Automatizzata**

**Azioni di Risposta Immediata:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **Capacità Forensi**

**Supporto alle Indagini:**
- **Conservazione del Registro di Audit**: Log immutabili con integrità crittografica
- **Raccolta di Prove**: Raccolta automatizzata di artefatti di sicurezza rilevanti
- **Ricostruzione della Timeline**: Sequenza dettagliata degli eventi che portano agli incidenti di sicurezza
- **Valutazione dell'Impatto**: Valutazione dell'estensione della compromissione e dell'esposizione dei dati

## **Principi Chiave dell'Architettura di Sicurezza**

### **Difesa in Profondità**
- **Molteplici Livelli di Sicurezza**: Nessun singolo punto di fallimento nell'architettura di sicurezza
- **Controlli Ridondanti**: Misure di sicurezza sovrapposte per funzioni critiche
- **Meccanismi Fail-Safe**: Impostazioni di default sicure quando i sistemi incontrano errori o attacchi

### **Implementazione Zero Trust**
- **Mai Fidarsi, Sempre Verificare**: Validazione continua di tutte le entità e richieste
- **Principio del Minimo Privilegio**: Diritti di accesso minimi per tutti i componenti
- **Micro-Segmentazione**: Controlli granolari di rete e accesso

### **Evoluzione Continua della Sicurezza**
- **Adattamento al Panorama delle Minacce**: Aggiornamenti regolari per affrontare le minacce emergenti
- **Efficacia dei Controlli di Sicurezza**: Valutazione e miglioramento continui dei controlli
- **Conformità alle Specifiche**: Allineamento con gli standard di sicurezza MCP in evoluzione

---

## **Risorse per l'Implementazione**

### **Documentazione Ufficiale MCP**
- [Specifiche MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Best Practice di Sicurezza MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specifiche Autorizzazione MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Risorse di Sicurezza OWASP MCP**
- [Guida di Sicurezza OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 OWASP MCP completo con implementazione su Azure
- [Top 10 OWASP MCP](https://owasp.org/www-project-mcp-top-10/) - Rischi di sicurezza ufficiali OWASP MCP
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Formazione pratica sulla sicurezza per MCP su Azure

### **Soluzioni di Sicurezza Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Standard di Sicurezza**
- [Best Practice di Sicurezza OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 per i Modelli di Linguaggio di Grandi Dimensioni](https://genai.owasp.org/)

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Importante:** Questi controlli di sicurezza riflettono la Specifica MCP
> `2026-07-28`. Verificare sempre rispetto alla
> [documentazione ufficiale corrente](https://modelcontextprotocol.io/specification/2026-07-28/)
> poiché gli standard continuano a evolversi.

## Cosa c'è dopo

- Torna a: [Panoramica del Modulo di Sicurezza](./README.md)
- Continua a: [Modulo 3: Per Iniziare](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->