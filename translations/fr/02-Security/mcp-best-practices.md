# Meilleures pratiques de sécurité MCP 2025

Ce guide complet décrit les meilleures pratiques essentielles en matière de sécurité pour la mise en œuvre des systèmes Model Context Protocol (MCP) basées sur la dernière **Spécification MCP 2025-11-25** et les normes industrielles actuelles. Ces pratiques abordent à la fois les préoccupations traditionnelles de sécurité et les menaces spécifiques à l’IA propres aux déploiements MCP.

## Exigences critiques en matière de sécurité

### Contrôles de sécurité obligatoires (exigences MUST)

1. **Validation des jetons** : Les serveurs MCP **NE DOIVENT PAS** accepter de jetons qui n’ont pas été explicitement émis pour le serveur MCP lui-même  
2. **Vérification de l’autorisation** : Les serveurs MCP mettant en œuvre l’autorisation **DOIVENT** vérifier TOUTES les requêtes entrantes et **NE DOIVENT PAS** utiliser de sessions pour l’authentification  
3. **Consentement utilisateur** : Les serveurs proxy MCP utilisant des ID client statiques **DOIVENT** obtenir le consentement explicite de l’utilisateur pour chaque client enregistré dynamiquement  
4. **ID de session sécurisés** : Les serveurs MCP **DOIVENT** utiliser des ID de session cryptographiquement sécurisés, non déterministes, générés avec des générateurs de nombres aléatoires sécurisés

## Pratiques de sécurité fondamentales

### 1. Validation et assainissement des entrées
- **Validation complète des entrées** : Valider et assainir toutes les entrées pour prévenir les attaques par injection, les problèmes de délégué confus et les vulnérabilités d’injection de prompt  
- **Application stricte des schémas de paramètres** : Mettre en œuvre une validation stricte des schémas JSON pour tous les paramètres d’outil et les entrées API  
- **Filtrage de contenu** : Utiliser Microsoft Prompt Shields et Azure Content Safety pour filtrer le contenu malveillant dans les prompts et les réponses  
- **Assainissement des sorties** : Valider et assainir toutes les sorties du modèle avant de les présenter aux utilisateurs ou aux systèmes en aval

### 2. Excellence en authentification et autorisation  
- **Fournisseurs d’identité externes** : Déléguer l’authentification à des fournisseurs d’identité établis (Microsoft Entra ID, fournisseurs OAuth 2.1) plutôt que d’implémenter une authentification personnalisée  
- **Permissions fines** : Mettre en œuvre des permissions granulaires spécifiques aux outils en suivant le principe du moindre privilège  
- **Gestion du cycle de vie des jetons** : Utiliser des jetons d’accès à courte durée de vie avec rotation sécurisée et validation correcte de l’audience  
- **Authentification multi-facteurs** : Exiger la MFA pour tout accès administratif et opérations sensibles

### 3. Protocoles de communication sécurisés
- **Sécurité de la couche transport** : Utiliser HTTPS/TLS 1.3 pour toutes les communications MCP avec validation correcte des certificats  
- **Chiffrement de bout en bout** : Mettre en œuvre des couches de chiffrement supplémentaires pour les données hautement sensibles en transit et au repos  
- **Gestion des certificats** : Maintenir une gestion appropriée du cycle de vie des certificats avec des processus de renouvellement automatisés  
- **Application de la version du protocole** : Utiliser la version actuelle du protocole MCP (2025-11-25) avec une négociation correcte des versions

### 4. Limitation avancée du débit et protection des ressources
- **Limitation multi-couches du débit** : Mettre en œuvre une limitation du débit au niveau utilisateur, session, outil et ressource pour prévenir les abus  
- **Limitation adaptative du débit** : Utiliser une limitation du débit basée sur l’apprentissage automatique qui s’adapte aux schémas d’utilisation et aux indicateurs de menace  
- **Gestion des quotas de ressources** : Définir des limites appropriées pour les ressources de calcul, l’utilisation de la mémoire et le temps d’exécution  
- **Protection contre les DDoS** : Déployer des systèmes complets de protection DDoS et d’analyse du trafic

### 5. Journalisation et surveillance complètes
- **Journalisation d’audit structurée** : Mettre en œuvre des journaux détaillés et consultables pour toutes les opérations MCP, exécutions d’outils et événements de sécurité  
- **Surveillance de sécurité en temps réel** : Déployer des systèmes SIEM avec détection d’anomalies alimentée par l’IA pour les charges de travail MCP  
- **Journalisation conforme à la vie privée** : Journaliser les événements de sécurité tout en respectant les exigences et réglementations en matière de confidentialité des données  
- **Intégration à la réponse aux incidents** : Connecter les systèmes de journalisation aux workflows automatisés de réponse aux incidents

### 6. Pratiques améliorées de stockage sécurisé
- **Modules de sécurité matériels** : Utiliser un stockage de clés soutenu par HSM (Azure Key Vault, AWS CloudHSM) pour les opérations cryptographiques critiques  
- **Gestion des clés de chiffrement** : Mettre en œuvre une rotation, une séparation et des contrôles d’accès appropriés pour les clés de chiffrement  
- **Gestion des secrets** : Stocker toutes les clés API, jetons et identifiants dans des systèmes dédiés de gestion des secrets  
- **Classification des données** : Classifier les données selon les niveaux de sensibilité et appliquer des mesures de protection appropriées

### 7. Gestion avancée des jetons
- **Prévention du passage de jetons** : Interdire explicitement les schémas de passage de jetons qui contournent les contrôles de sécurité  
- **Validation de l’audience** : Toujours vérifier que les revendications d’audience du jeton correspondent à l’identité prévue du serveur MCP  
- **Autorisation basée sur les revendications** : Mettre en œuvre une autorisation fine basée sur les revendications du jeton et les attributs utilisateur  
- **Liaison des jetons** : Lier les jetons à des sessions, utilisateurs ou appareils spécifiques lorsque cela est approprié

### 8. Gestion sécurisée des sessions
- **ID de session cryptographiques** : Générer les ID de session en utilisant des générateurs de nombres aléatoires cryptographiquement sécurisés (pas de séquences prévisibles)  
- **Liaison spécifique à l’utilisateur** : Lier les ID de session aux informations spécifiques à l’utilisateur en utilisant des formats sécurisés comme `<user_id>:<session_id>`  
- **Contrôles du cycle de vie des sessions** : Mettre en œuvre des mécanismes appropriés d’expiration, rotation et invalidation des sessions  
- **En-têtes de sécurité pour les sessions** : Utiliser des en-têtes HTTP de sécurité appropriés pour la protection des sessions

### 9. Contrôles de sécurité spécifiques à l’IA
- **Défense contre l’injection de prompt** : Déployer Microsoft Prompt Shields avec mise en lumière, délimiteurs et techniques de marquage des données  
- **Prévention de l’empoisonnement des outils** : Valider les métadonnées des outils, surveiller les changements dynamiques et vérifier l’intégrité des outils  
- **Validation des sorties du modèle** : Scanner les sorties du modèle pour détecter les fuites potentielles de données, contenus nuisibles ou violations de politique de sécurité  
- **Protection de la fenêtre de contexte** : Mettre en œuvre des contrôles pour prévenir l’empoisonnement et les attaques de manipulation de la fenêtre de contexte

### 10. Sécurité de l’exécution des outils
- **Sandboxing de l’exécution** : Exécuter les outils dans des environnements conteneurisés et isolés avec des limites de ressources  
- **Séparation des privilèges** : Exécuter les outils avec les privilèges minimaux requis et des comptes de service séparés  
- **Isolation réseau** : Mettre en œuvre une segmentation réseau pour les environnements d’exécution des outils  
- **Surveillance de l’exécution** : Surveiller l’exécution des outils pour détecter les comportements anormaux, l’utilisation des ressources et les violations de sécurité

### 11. Validation continue de la sécurité
- **Tests de sécurité automatisés** : Intégrer les tests de sécurité dans les pipelines CI/CD avec des outils comme GitHub Advanced Security  
- **Gestion des vulnérabilités** : Scanner régulièrement toutes les dépendances, y compris les modèles IA et services externes  
- **Tests d’intrusion** : Réaliser des évaluations de sécurité régulières ciblant spécifiquement les implémentations MCP  
- **Revue de code sécurisée** : Mettre en œuvre des revues de sécurité obligatoires pour tous les changements de code liés à MCP

### 12. Sécurité de la chaîne d’approvisionnement pour l’IA
- **Vérification des composants** : Vérifier la provenance, l’intégrité et la sécurité de tous les composants IA (modèles, embeddings, API)  
- **Gestion des dépendances** : Maintenir des inventaires à jour de tous les logiciels et dépendances IA avec suivi des vulnérabilités  
- **Dépôts de confiance** : Utiliser des sources vérifiées et fiables pour tous les modèles IA, bibliothèques et outils  
- **Surveillance de la chaîne d’approvisionnement** : Surveiller en continu les compromissions chez les fournisseurs de services IA et les dépôts de modèles

## Modèles avancés de sécurité

### Architecture Zero Trust pour MCP
- **Ne jamais faire confiance, toujours vérifier** : Mettre en œuvre une vérification continue pour tous les participants MCP  
- **Micro-segmentation** : Isoler les composants MCP avec des contrôles granulaires réseau et d’identité  
- **Accès conditionnel** : Mettre en œuvre des contrôles d’accès basés sur le risque qui s’adaptent au contexte et au comportement  
- **Évaluation continue des risques** : Évaluer dynamiquement la posture de sécurité en fonction des indicateurs de menace actuels

### Mise en œuvre d’une IA respectueuse de la vie privée
- **Minimisation des données** : Ne divulguer que le minimum de données nécessaires pour chaque opération MCP  
- **Confidentialité différentielle** : Mettre en œuvre des techniques de préservation de la vie privée pour le traitement des données sensibles  
- **Chiffrement homomorphe** : Utiliser des techniques avancées de chiffrement pour le calcul sécurisé sur des données chiffrées  
- **Apprentissage fédéré** : Mettre en œuvre des approches d’apprentissage distribué qui préservent la localisation et la confidentialité des données

### Réponse aux incidents pour les systèmes IA
- **Procédures spécifiques aux incidents IA** : Développer des procédures de réponse aux incidents adaptées aux menaces spécifiques à l’IA et MCP  
- **Réponse automatisée** : Mettre en œuvre un confinement et une remédiation automatisés pour les incidents de sécurité IA courants  
- **Capacités médico-légales** : Maintenir une préparation médico-légale pour les compromissions des systèmes IA et les violations de données  
- **Procédures de récupération** : Établir des procédures pour récupérer des empoisonnements de modèles IA, attaques d’injection de prompt et compromissions de services

## Ressources et normes de mise en œuvre

### Documentation officielle MCP
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Spécification actuelle du protocole MCP  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Guide officiel de sécurité  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Modèles d’authentification et d’autorisation  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Exigences de sécurité de la couche transport

### Solutions de sécurité Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Protection avancée contre l’injection de prompt  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Filtrage complet du contenu IA  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Gestion d’identité et d’accès d’entreprise  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Gestion sécurisée des secrets et identifiants  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Analyse de la sécurité de la chaîne d’approvisionnement et du code

### Normes et cadres de sécurité
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Guide actuel de sécurité OAuth  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Risques de sécurité des applications web  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Risques de sécurité spécifiques à l’IA  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Gestion complète des risques IA  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Systèmes de gestion de la sécurité de l’information

### Guides et tutoriels de mise en œuvre
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Modèles d’authentification d’entreprise  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Intégration de fournisseur d’identité  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Meilleures pratiques de gestion des jetons  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Modèles avancés de chiffrement

### Ressources avancées de sécurité
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Pratiques de développement sécurisé  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Tests de sécurité spécifiques à l’IA  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Méthodologie de modélisation des menaces IA  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Techniques d’IA respectueuses de la vie privée

### Conformité et gouvernance
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Conformité à la vie privée dans les systèmes IA  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Mise en œuvre responsable de l’IA  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Contrôles de sécurité pour les fournisseurs de services IA  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Exigences de conformité IA en santé

### DevSecOps et automatisation
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Pipelines de développement IA sécurisés  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Validation continue de la sécurité  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Déploiement sécurisé de l’infrastructure  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sécurité de la conteneurisation des charges IA

### Surveillance et réponse aux incidents  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Solutions complètes de surveillance  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procédures spécifiques aux incidents IA  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Gestion des informations et événements de sécurité  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Sources de renseignement sur les menaces IA

## 🔄 Amélioration continue

### Restez à jour avec les normes évolutives
- **Mises à jour de la spécification MCP** : Surveiller les changements officiels de la spécification MCP et les avis de sécurité  
- **Renseignement sur les menaces** : S’abonner aux flux de menaces de sécurité IA et bases de données de vulnérabilités  
- **Engagement communautaire** : Participer aux discussions et groupes de travail de la communauté de sécurité MCP  
- **Évaluation régulière** : Réaliser des évaluations trimestrielles de la posture de sécurité et mettre à jour les pratiques en conséquence

### Contribution à la sécurité MCP
- **Recherche en sécurité** : Contribuer à la recherche en sécurité MCP et aux programmes de divulgation de vulnérabilités  
- **Partage des meilleures pratiques** : Partager les implémentations de sécurité et les leçons apprises avec la communauté
- **Développement standard** : Participer au développement des spécifications MCP et à la création de normes de sécurité  
- **Développement d’outils** : Développer et partager des outils et bibliothèques de sécurité pour l’écosystème MCP

---

*Ce document reflète les meilleures pratiques de sécurité MCP au 18 décembre 2025, basées sur la spécification MCP 2025-11-25. Les pratiques de sécurité doivent être régulièrement revues et mises à jour à mesure que le protocole et le paysage des menaces évoluent.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->