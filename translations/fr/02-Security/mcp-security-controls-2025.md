# Contrôles de Sécurité MCP - Mise à jour Décembre 2025

> **Norme actuelle** : Ce document reflète les exigences de sécurité de la [Spécification MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) et les [Bonnes Pratiques de Sécurité MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) officielles.

Le Model Context Protocol (MCP) a considérablement mûri avec des contrôles de sécurité renforcés couvrant à la fois la sécurité logicielle traditionnelle et les menaces spécifiques à l'IA. Ce document fournit des contrôles de sécurité complets pour des implémentations MCP sécurisées à la date de décembre 2025.

## **Exigences de Sécurité OBLIGATOIRES**

### **Interdictions Critiques de la Spécification MCP :**

> **INTERDIT** : Les serveurs MCP **NE DOIVENT PAS** accepter de jetons qui n'ont pas été explicitement émis pour le serveur MCP  
>
> **PROHIBÉ** : Les serveurs MCP **NE DOIVENT PAS** utiliser de sessions pour l'authentification  
>
> **REQUIS** : Les serveurs MCP implémentant l'autorisation **DOIVENT** vérifier TOUTES les requêtes entrantes  
>
> **OBLIGATOIRE** : Les serveurs proxy MCP utilisant des identifiants clients statiques **DOIVENT** obtenir le consentement utilisateur pour chaque client enregistré dynamiquement

---

## 1. **Contrôles d'Authentification & d'Autorisation**

### **Intégration de Fournisseurs d'Identité Externes**

**Norme MCP actuelle (2025-06-18)** permet aux serveurs MCP de déléguer l'authentification à des fournisseurs d'identité externes, représentant une amélioration significative de la sécurité :

### **Intégration de Fournisseurs d'Identité Externes**

**Norme MCP actuelle (2025-11-25)** permet aux serveurs MCP de déléguer l'authentification à des fournisseurs d'identité externes, représentant une amélioration significative de la sécurité :

**Avantages de Sécurité :**  
1. **Élimine les Risques d'Authentification Personnalisée** : Réduit la surface de vulnérabilité en évitant les implémentations d'authentification personnalisées  
2. **Sécurité de Niveau Entreprise** : Exploite des fournisseurs d'identité établis comme Microsoft Entra ID avec des fonctionnalités de sécurité avancées  
3. **Gestion Centralisée des Identités** : Simplifie la gestion du cycle de vie des utilisateurs, le contrôle d'accès et l'audit de conformité  
4. **Authentification Multi-Facteurs** : Hérite des capacités MFA des fournisseurs d'identité d'entreprise  
5. **Politiques d'Accès Conditionnel** : Bénéficie de contrôles d'accès basés sur le risque et d'authentification adaptative  

**Exigences d'Implémentation :**  
- **Validation de l'Audience du Jeton** : Vérifier que tous les jetons sont explicitement émis pour le serveur MCP  
- **Vérification de l'Émetteur** : Valider que l'émetteur du jeton correspond au fournisseur d'identité attendu  
- **Vérification de la Signature** : Validation cryptographique de l'intégrité du jeton  
- **Application de l'Expiration** : Application stricte des limites de durée de vie des jetons  
- **Validation des Scopes** : S'assurer que les jetons contiennent les permissions appropriées pour les opérations demandées  

### **Sécurité de la Logique d'Autorisation**

**Contrôles Critiques :**  
- **Audits Complets d'Autorisation** : Revue régulière de sécurité de tous les points de décision d'autorisation  
- **Défauts Sécurisés** : Refuser l'accès lorsque la logique d'autorisation ne peut pas prendre de décision définitive  
- **Limites de Permissions** : Séparation claire entre différents niveaux de privilèges et accès aux ressources  
- **Journalisation d'Audit** : Enregistrement complet de toutes les décisions d'autorisation pour la surveillance de sécurité  
- **Revue Régulière des Accès** : Validation périodique des permissions utilisateurs et des attributions de privilèges  

## 2. **Sécurité des Jetons & Contrôles Anti-Passthrough**

### **Prévention du Passthrough de Jetons**

**Le passthrough de jetons est explicitement interdit** dans la Spécification d'Autorisation MCP en raison de risques critiques de sécurité :

**Risques de Sécurité Adressés :**  
- **Contournement des Contrôles** : Bypass des contrôles essentiels comme la limitation de débit, la validation des requêtes et la surveillance du trafic  
- **Rupture de Responsabilité** : Rend impossible l'identification du client, corrompant les pistes d'audit et les enquêtes d'incidents  
- **Exfiltration via Proxy** : Permet aux acteurs malveillants d'utiliser les serveurs comme proxy pour un accès non autorisé aux données  
- **Violation des Frontières de Confiance** : Brise les hypothèses de confiance des services en aval concernant l'origine des jetons  
- **Mouvement Latéral** : Les jetons compromis sur plusieurs services permettent une expansion plus large des attaques  

**Contrôles d'Implémentation :**  
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
  
### **Modèles de Gestion Sécurisée des Jetons**

**Bonnes Pratiques :**  
- **Jetons à Durée Courte** : Minimiser la fenêtre d'exposition avec une rotation fréquente des jetons  
- **Émission Juste-à-Temps** : Émettre les jetons uniquement lorsque nécessaire pour des opérations spécifiques  
- **Stockage Sécurisé** : Utiliser des modules de sécurité matériels (HSM) ou des coffres-forts sécurisés  
- **Liaison des Jetons** : Lier les jetons à des clients, sessions ou opérations spécifiques lorsque possible  
- **Surveillance & Alertes** : Détection en temps réel des usages abusifs ou des accès non autorisés aux jetons  

## 3. **Contrôles de Sécurité des Sessions**

### **Prévention du Détournement de Session**

**Vecteurs d'Attaque Adressés :**  
- **Injection de Prompt de Détournement de Session** : Événements malveillants injectés dans l'état de session partagé  
- **Usurpation de Session** : Utilisation non autorisée d'ID de session volés pour contourner l'authentification  
- **Attaques de Reprise de Flux** : Exploitation de la reprise d'événements envoyés par le serveur pour injection de contenu malveillant  

**Contrôles Obligatoires de Session :**  
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```
  
**Sécurité du Transport :**  
- **Application de HTTPS** : Toute communication de session via TLS 1.3  
- **Attributs Sécurisés des Cookies** : HttpOnly, Secure, SameSite=Strict  
- **Pinning de Certificat** : Pour les connexions critiques afin de prévenir les attaques MITM  

### **Considérations Stateful vs Stateless**

**Pour les Implémentations Stateful :**  
- L'état de session partagé nécessite une protection supplémentaire contre les attaques par injection  
- La gestion de session basée sur file d'attente nécessite une vérification d'intégrité  
- Plusieurs instances serveur nécessitent une synchronisation sécurisée de l'état de session  

**Pour les Implémentations Stateless :**  
- Gestion de session basée sur JWT ou jetons similaires  
- Vérification cryptographique de l'intégrité de l'état de session  
- Surface d'attaque réduite mais nécessite une validation robuste des jetons  

## 4. **Contrôles de Sécurité Spécifiques à l'IA**

### **Défense contre l'Injection de Prompt**

**Intégration Microsoft Prompt Shields :**  
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
  
**Contrôles d'Implémentation :**  
- **Assainissement des Entrées** : Validation et filtrage complets de toutes les entrées utilisateur  
- **Définition des Limites de Contenu** : Séparation claire entre instructions système et contenu utilisateur  
- **Hiérarchie des Instructions** : Règles de priorité appropriées pour les instructions conflictuelles  
- **Surveillance des Sorties** : Détection des sorties potentiellement nuisibles ou manipulées  

### **Prévention de l'Empoisonnement d'Outils**

**Cadre de Sécurité des Outils :**  
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
  
**Gestion Dynamique des Outils :**  
- **Flux d'Approbation** : Consentement explicite de l'utilisateur pour les modifications d'outils  
- **Capacités de Restauration** : Possibilité de revenir à des versions antérieures des outils  
- **Audit des Modifications** : Historique complet des modifications des définitions d'outils  
- **Évaluation des Risques** : Évaluation automatisée de la posture de sécurité des outils  

## 5. **Prévention des Attaques de Député Confus**

### **Sécurité du Proxy OAuth**

**Contrôles de Prévention des Attaques :**  
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```
  
**Exigences d'Implémentation :**  
- **Vérification du Consentement Utilisateur** : Ne jamais sauter les écrans de consentement pour l'enregistrement dynamique des clients  
- **Validation des URI de Redirection** : Validation stricte basée sur une liste blanche des destinations de redirection  
- **Protection du Code d'Autorisation** : Codes à durée courte avec application d'utilisation unique  
- **Vérification de l'Identité Client** : Validation robuste des identifiants clients et métadonnées  

## 6. **Sécurité d'Exécution des Outils**

### **Sandboxing & Isolation**

**Isolation Basée sur Conteneurs :**  
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
  
**Isolation des Processus :**  
- **Contextes de Processus Séparés** : Chaque exécution d'outil dans un espace de processus isolé  
- **Communication Inter-Processus** : Mécanismes IPC sécurisés avec validation  
- **Surveillance des Processus** : Analyse comportementale en temps réel et détection d'anomalies  
- **Application des Ressources** : Limites strictes sur CPU, mémoire et opérations I/O  

### **Implémentation du Moindre Privilège**

**Gestion des Permissions :**  
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
  
## 7. **Contrôles de Sécurité de la Chaîne d'Approvisionnement**

### **Vérification des Dépendances**

**Sécurité Complète des Composants :**  
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
  
### **Surveillance Continue**

**Détection des Menaces de la Chaîne d'Approvisionnement :**  
- **Surveillance de la Santé des Dépendances** : Évaluation continue de toutes les dépendances pour les problèmes de sécurité  
- **Intégration du Renseignement sur les Menaces** : Mises à jour en temps réel sur les menaces émergentes de la chaîne d'approvisionnement  
- **Analyse Comportementale** : Détection de comportements inhabituels dans les composants externes  
- **Réponse Automatisée** : Contention immédiate des composants compromis  

## 8. **Contrôles de Surveillance & Détection**

### **Gestion des Informations et Événements de Sécurité (SIEM)**

**Stratégie Complète de Journalisation :**  
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
  
### **Détection des Menaces en Temps Réel**

**Analytique Comportementale :**  
- **Analyse du Comportement Utilisateur (UBA)** : Détection des schémas d'accès utilisateur inhabituels  
- **Analyse du Comportement des Entités (EBA)** : Surveillance du comportement des serveurs MCP et des outils  
- **Détection d'Anomalies par Apprentissage Automatique** : Identification des menaces de sécurité assistée par IA  
- **Corrélation du Renseignement sur les Menaces** : Mise en correspondance des activités observées avec des schémas d'attaque connus  

## 9. **Réponse aux Incidents & Récupération**

### **Capacités de Réponse Automatisée**

**Actions de Réponse Immédiate :**  
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
  
### **Capacités Médico-Légales**

**Support à l'Enquête :**  
- **Préservation des Pistes d'Audit** : Journalisation immuable avec intégrité cryptographique  
- **Collecte de Preuves** : Rassemblement automatisé des artefacts de sécurité pertinents  
- **Reconstruction de la Chronologie** : Séquence détaillée des événements menant aux incidents de sécurité  
- **Évaluation de l'Impact** : Évaluation de l'étendue de la compromission et de l'exposition des données  

## **Principes Clés de l'Architecture de Sécurité**

### **Défense en Profondeur**  
- **Multiples Couches de Sécurité** : Aucun point de défaillance unique dans l'architecture de sécurité  
- **Contrôles Redondants** : Mesures de sécurité chevauchantes pour les fonctions critiques  
- **Mécanismes de Sécurité par Défaut** : Paramètres sécurisés par défaut en cas d'erreurs ou d'attaques  

### **Implémentation du Zero Trust**  
- **Ne Jamais Faire Confiance, Toujours Vérifier** : Validation continue de toutes les entités et requêtes  
- **Principe du Moindre Privilège** : Droits d'accès minimaux pour tous les composants  
- **Micro-Segmentation** : Contrôles granulaires du réseau et des accès  

### **Évolution Continue de la Sécurité**  
- **Adaptation au Paysage des Menaces** : Mises à jour régulières pour adresser les menaces émergentes  
- **Efficacité des Contrôles de Sécurité** : Évaluation et amélioration continues des contrôles  
- **Conformité aux Spécifications** : Alignement avec les normes de sécurité MCP en évolution  

---

## **Ressources d'Implémentation**

### **Documentation Officielle MCP**  
- [Spécification MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [Bonnes Pratiques de Sécurité MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [Spécification d'Autorisation MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  

### **Solutions de Sécurité Microsoft**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)  

### **Normes de Sécurité**  
- [Bonnes Pratiques de Sécurité OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 pour les Modèles de Langage Large](https://genai.owasp.org/)  
- [Cadre de Cybersécurité NIST](https://www.nist.gov/cyberframework)  

---

> **Important** : Ces contrôles de sécurité reflètent la spécification MCP actuelle (2025-06-18). Vérifiez toujours avec la [documentation officielle](https://spec.modelcontextprotocol.io/) la plus récente car les normes évoluent rapidement.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->