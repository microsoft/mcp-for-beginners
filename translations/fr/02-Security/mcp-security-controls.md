# Contrôles de Sécurité MCP - Mise à jour de septembre 2026

> **Norme actuelle :** Ce document reflète
> [Spécification MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> et les
> [Meilleures Pratiques de Sécurité MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) officielles.

Le Model Context Protocol (MCP) a considérablement mûri avec des contrôles de sécurité renforcés traitant à la fois la sécurité logicielle traditionnelle et les menaces spécifiques à l'IA. Ce document fournit des contrôles de sécurité complets pour des implémentations MCP sécurisées alignées avec le cadre OWASP MCP Top 10.

## 🏔️ Formation Pratique en Sécurité

Pour une expérience pratique de mise en œuvre de la sécurité, nous recommandons l'**[Atelier Sommet de Sécurité MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - une expédition guidée complète pour sécuriser les serveurs MCP sur Azure en utilisant une méthodologie "vulnérable → exploiter → corriger → valider".

Tous les contrôles de sécurité de ce document sont conformes au **[Guide de Sécurité Azure MCP OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, qui fournit des architectures de référence et des directives spécifiques à Azure pour les risques OWASP MCP Top 10.

## **Exigences de Sécurité OBLIGATOIRES**

### **Interdictions Critiques de la Spécification MCP :**

> **INTERDIT** : Les serveurs MCP **NE DOIVENT PAS** accepter de jetons non explicitement émis pour le serveur MCP
>
> **PROHIBÉ** : Les serveurs MCP **NE DOIVENT PAS** utiliser de sessions pour l'authentification  
>
> **EXIGÉ** : Les serveurs MCP implémentant l'autorisation **DOIVENT** vérifier TOUTES les requêtes entrantes
>
> **OBLIGATOIRE** : Les serveurs proxy MCP utilisant un ID client tiers statique
> **DOIVENT** obtenir le consentement pour chaque client MCP avant de transférer l'autorisation

---

## 1. **Contrôles d'Authentification & d'Autorisation**

### **Intégration d'un Fournisseur d'Identité Externe**

**Spécification MCP `2026-07-28`** permet aux serveurs MCP de déléguer
l'authentification aux fournisseurs d'identité externes. L'autorisation pour les transports HTTP
est évaluée pour chaque requête ; les serveurs stdio locaux obtiennent plutôt leurs identifiants
depuis leur environnement.

**Risque OWASP MCP adressé** : [MCP07 - Authentification & Autorisation Insuffisantes](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Avantages en matière de sécurité :**
1. **Élimine les Risques d'Authentification Personnalisée** : Réduit la surface de vulnérabilité en évitant les implémentations d'authentification personnalisées
2. **Sécurité de Niveau Entreprise** : Exploite des fournisseurs d'identité établis comme Microsoft Entra ID avec des fonctionnalités de sécurité avancées
3. **Gestion Centralisée des Identités** : Simplifie la gestion du cycle de vie des utilisateurs, le contrôle d'accès et les audits de conformité
4. **Authentification Multi-facteurs** : Hérite des capacités de MFA des fournisseurs d'identité d'entreprise
5. **Politiques d'Accès Conditionnel** : Bénéficie de contrôles d'accès basés sur les risques et de l'authentification adaptative

**Exigences d'implémentation :**
- **Enregistrement du Client** : Préférer les Documents de Métadonnées d'ID Client ou
  le pré-enregistrement ; utiliser l'Enregistrement Dynamique de Client obsolète uniquement pour
  la compatibilité
- **Validation de l'Audience des Jetons** : Vérifier que tous les jetons sont explicitement émis pour le serveur MCP
- **Vérification de l'Émetteur** : Valider que l'émetteur du jeton correspond au fournisseur d'identité attendu
- **Vérification de la Signature** : Validation cryptographique de l'intégrité du jeton
- **Application des Dates d'Expiration** : Application stricte des limites de durée de vie des jetons
- **Validation des Portées** : S'assurer que les jetons contiennent les permissions appropriées pour les opérations demandées

### **Sécurité de la Logique d'Autorisation**


**Contrôles Critiques :**
- **Audits d'Autorisation Complets** : Examens réguliers de sécurité de tous les points de décision d'autorisation
- **Paramètres par Défaut Infaillibles** : Refuser l'accès lorsque la logique d'autorisation ne peut pas prendre une décision définitive
- **Limites de Permission** : Séparation claire entre différents niveaux de privilèges et accès aux ressources
- **Journalisation d'Audit** : Journaux complets de toutes les décisions d'autorisation pour la surveillance de sécurité
- **Revues Régulières des Accès** : Validation périodique des permissions des utilisateurs et des attributions de privilèges

## 2. **Contrôles de Sécurité des Jetons & Anti-Passthrough**

**Risque OWASP MCP Traité** : [MCP01 - Mauvaise gestion des jetons & Exposition de secrets](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Prévention du Passthrough de Jeton**

**Le passthrough de jeton est explicitement interdit** dans la Spécification d'Autorisation MCP en raison de risques de sécurité critiques :

**Risques de Sécurité Traités :**
- **Contournement des Contrôles** : Bypass des contrôles de sécurité essentiels tels que la limitation de débit, la validation des requêtes et la surveillance du trafic
- **Rupture de Responsabilité** : Rend impossible l'identification du client, corrompant les pistes d'audit et l'enquête sur les incidents
- **Exfiltration par Proxy** : Permet aux acteurs malveillants d'utiliser les serveurs comme proxy pour un accès non autorisé aux données
- **Violations des Frontières de Confiance** : Brise les hypothèses de confiance des services en aval concernant l'origine des jetons
- **Mouvement Latéral** : Des jetons compromis à travers plusieurs services permettent une expansion d'attaque plus large

**Contrôles de Mise en Œuvre :**
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

**Meilleures Pratiques :**
- **Jetons Éphémères** : Minimiser la fenêtre d'exposition avec une rotation fréquente des jetons
- **Émission à la Demande** : Émettre les jetons uniquement lorsqu'ils sont nécessaires pour des opérations spécifiques
- **Stockage Sécurisé** : Utiliser des modules de sécurité matérielle (HSM) ou des coffres-forts de clés sécurisés
- **Liaison de Jeton** : Valider l'audience et l'émetteur du jeton pour la ressource MCP, le client et l'opération prévues

- **Surveillance & Alertes** : Détection en temps réel des usages abusifs de jetons ou des schémas d'accès non autorisés

## 3. **Contrôles de Sécurité de l'État de l'Application**

### **Prévention du Détournement de Handle d'État**

**Vecteurs d'Attaque Traités :**
- **Deviner le Handle** : Des identifiants prévisibles exposent l'état d'un autre appelant
- **Réutilisation Cross-utilisateur** : Un handle volé est utilisé avec une identité différente
- **Autorisation Implicite** : La possession d'un handle est incorrectement traitée comme une preuve d'accès


**Contrôles des Handles d'État :**

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

**Sécurité du Transport :**
- **Application de HTTPS** : Exiger HTTPS pour les transports HTTP distants
- **Gestion des Identifiants** : Envoyer et valider l'autorisation à chaque requête HTTP
- **Isolation stdio** : Protéger les serveurs stdio locaux par isolement des processus et contrôles d'identifiants d'environnement


### **Considérations Stateful vs Stateless**

MCP `2026-07-28` est sans état au niveau protocolaire. Les applications peuvent néanmoins
maintenir l'état en renvoyant un handle explicite d'un appel d'outil et en l'acceptant
comme argument ordinaire lors des appels ultérieurs.

- Stocker l'état indépendamment de toute connexion de transport.
- Lier les handles d'état au principal authentifié côté serveur.
- Traiter un handle comme un nom, non comme un identifiant porteur.
- Définir le comportement d'expiration et de récupération pour les handles obsolètes.

## 4. **Contrôles de Sécurité Spécifiques à l'IA**

**Risques OWASP MCP Traités** :

- [MCP06 - Subversion du flux d'intention](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Empoisonnement d'outil](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Injection et exécution de commandes](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Défense contre l'injection de prompt**

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

**Contrôles d'implémentation :**
- **Assainissement des entrées** : Validation et filtrage complets de toutes les entrées utilisateur
- **Définition des limites de contenu** : Séparation claire entre les instructions système et le contenu utilisateur
- **Hiérarchie des instructions** : Règles de précédence appropriées pour les instructions conflictuelles
- **Surveillance de la sortie** : Détection des sorties potentiellement nuisibles ou manipulées

### **Prévention de l'empoisonnement d'outil**

**Cadre de sécurité des outils :**
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

**Gestion dynamique des outils :**
- **Flux d'approbation** : Consentement explicite de l'utilisateur pour les modifications d'outils
- **Capacités de rollback** : Possibilité de revenir aux versions précédentes des outils
- **Audit des modifications** : Historique complet des modifications des définitions d'outils
- **Évaluation des risques** : Évaluation automatisée de la posture de sécurité des outils

## 5. **Prévention des attaques du commis confus**

### **Sécurité du proxy OAuth**

**Contrôles de prévention des attaques :**
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

**Exigences de mise en œuvre :**
- **Enregistrement du client** : Préférer la pré-enregistrement ou la métadonnée d'identifiant client
  Documents ; traiter l'enregistrement dynamique du client comme un repli de compatibilité
- **Vérification du consentement utilisateur** : Les proxys MCP utilisant un identifiant client tiers statique
  doivent obtenir le consentement par client avant de transmettre l'autorisation
- **Validation de l'URI de redirection** : Validation stricte basée sur une liste blanche des destinations de redirection
- **Protection du code d'autorisation** : Codes à courte durée de vie avec application d'utilisation unique
- **Vérification de l'identité du client** : Validation robuste des identifiants clients et des métadonnées

## 6. **Sécurité de l'exécution des outils**

### **Sandboxing et isolation**

**Isolation basée sur des conteneurs :**
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

**Isolation des processus :**
- **Contextes de processus séparés** : Chaque exécution d'outil dans un espace de processus isolé
- **Communication inter-processus** : Mécanismes IPC sécurisés avec validation
- **Surveillance des processus** : Analyse du comportement en temps réel et détection d'anomalies
- **Application des ressources** : Limites strictes sur l'utilisation CPU, mémoire et opérations I/O

### **Implémentation du moindre privilège**

**Gestion des permissions :**
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

## 7. **Contrôles de sécurité de la chaîne d'approvisionnement**

**Risque OWASP MCP abordé** : [MCP04 - Attaques sur la chaîne d'approvisionnement logicielle et altération des dépendances](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Vérification des dépendances**

**Sécurité complète des composants :**
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

### **Surveillance continue**

**Détection des menaces sur la chaîne d'approvisionnement :**
- **Surveillance de la santé des dépendances** : Évaluation continue de toutes les dépendances pour les problèmes de sécurité
- **Intégration du renseignement sur les menaces** : Mises à jour en temps réel sur les menaces émergentes dans la chaîne d'approvisionnement
- **Analyse comportementale** : Détection des comportements inhabituels dans les composants externes
- **Réponse automatique** : Confinement immédiat des composants compromis

## 8. **Contrôles de surveillance et de détection**

**Risque OWASP MCP abordé** : [MCP08 - Absence d'audit et de télémétrie](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Gestion des informations et des événements de sécurité (SIEM)**

**Stratégie complète de journalisation :**
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

### **Détection des menaces en temps réel**

**Analyse comportementale :**
- **Analyse du comportement utilisateur (UBA)** : Détection des schémas d'accès utilisateur inhabituels
- **Analyse du comportement des entités (EBA)** : Surveillance du comportement des serveurs MCP et des outils
- **Détection d'anomalies par apprentissage machine** : Identification alimentée par IA des menaces de sécurité
- **Corrélation du renseignement sur les menaces** : Mise en correspondance des activités observées avec des schémas d'attaque connus

## 9. **Réponse aux incidents et récupération**

### **Capacités de réponse automatisée**

**Actions de réponse immédiates :**
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

### **Capacités médico-légales**

**Support à l'investigation :**
- **Conservation de la piste d'audit** : Journalisation immuable avec intégrité cryptographique
- **Collecte de preuves** : Collecte automatisée des artefacts de sécurité pertinents
- **Reconstitution de la chronologie** : Séquence détaillée des événements menant aux incidents de sécurité
- **Évaluation de l'impact** : Évaluation de l'étendue de la compromission et de l'exposition des données

## **Principes clés de l'architecture de sécurité**

### **Défense en profondeur**
- **Multiples couches de sécurité** : Pas de point de défaillance unique dans l'architecture de sécurité
- **Contrôles redondants** : Mesures de sécurité chevauchantes pour les fonctions critiques
- **Mécanismes à sécurité par défaut** : Défauts sécurisés lors des erreurs ou attaques des systèmes

### **Implémentation du zéro confiance**
- **Ne jamais faire confiance, toujours vérifier** : Validation continue de toutes les entités et requêtes
- **Principe du moindre privilège** : Droits d'accès minimaux pour tous les composants
- **Micro-segmentation** : Contrôles granulaires du réseau et d'accès

### **Evolution continue de la sécurité**
- **Adaptation au paysage des menaces** : Mises à jour régulières pour traiter les menaces émergentes
- **Efficacité des contrôles de sécurité** : Évaluation et amélioration continues des contrôles
- **Conformité aux spécifications** : Alignement avec les normes de sécurité MCP en évolution

---

## **Ressources d'implémentation**

### **Documentation officielle MCP**
- [Spécification MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Meilleures pratiques de sécurité MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Spécification d'autorisation MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Ressources de sécurité OWASP MCP**
- [Guide de sécurité MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 complet OWASP MCP avec implémentation Azure
- [Top 10 OWASP MCP](https://owasp.org/www-project-mcp-top-10/) - Risques officiels de sécurité MCP OWASP
- [Atelier du sommet de sécurité MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Formation pratique en sécurité pour MCP sur Azure

### **Solutions de sécurité Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Normes de sécurité**
- [Meilleures pratiques de sécurité OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 pour les grands modèles de langage](https://genai.owasp.org/)

- [Cadre de cybersécurité du NIST](https://www.nist.gov/cyberframework)

---

> **Important :** Ces contrôles de sécurité reflètent la Spécification MCP
> `2026-07-28`. Vérifiez toujours avec la
> [documentation officielle actuelle](https://modelcontextprotocol.io/specification/2026-07-28/)
> car les normes continuent d’évoluer.

## Et après ?

- Retour à : [Présentation du module de sécurité](./README.md)
- Continuer vers : [Module 3 : Premiers pas](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->