# Changelog : Programme MCP pour débutants

Ce document sert de registre de toutes les modifications importantes apportées au programme Model Context Protocol (MCP) pour débutants. Les modifications sont documentées par ordre chronologique inverse (les plus récentes en premier).

## 11 avril 2026

### Nouvelle leçon, corrections de documentation et mises à jour des dépendances

#### Nouveau contenu du programme ajouté

**Module 05 - Sujets avancés**
- **Leçon 5.17 : Raisonnement multi-agent antagoniste avec MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`) : nouveau guide complet couvrant le modèle de débat antagoniste pour les systèmes multi-agents
  - Diagramme d’architecture Mermaid : deux agents → serveur MCP partagé → transcription du débat → juge → verdict
  - Serveur d’outils MCP partagé (`web_search` + `run_python`) implémenté en Python et TypeScript
  - Invites système opposées (POUR / CONTRE / Juge) avec exigences explicites d’utilisation d’outils
  - Orchestrateur de débat en Python, TypeScript et C# gérant les tours et le routage des arguments
  - Câblage MCP `ClientSession` pour l’orchestrateur vers appels réels d’outils
  - Tableau d’usages (détection d’hallucination, modélisation des menaces, revue de conception d’API, vérification factuelle, sélection technologique)
  - Considérations de sécurité : exécution en bac à sable, validation des appels d’outils, limitation de débit, journalisation d’audit
  - Exercice structuré avec trois scénarios pratiques (revue de code, décision d’architecture, modération de contenu)

#### Corrections de documentation

**Module 03 - Premiers pas**
- **05-stdio-server/README.md** : correction de l’exemple incomplet du serveur stdio TypeScript — ajout de l’instanciation du transport manquante (`new StdioServerTransport()`) et de l’appel `server.connect(transport)` pour correspondre aux exemples Python et .NET dans la même section
- **14-sampling/README.md** : correction de faute de frappe — correction de « Sampling is an davanced features » → « Sampling is an advanced feature »

#### Mises à jour du programme

**README.md principal**
- Ajout de l’entrée 5.17 (Raisonnement multi-agent antagoniste avec MCP) au tableau du programme avec lien direct vers la nouvelle leçon

**05-AdvancedTopics/README.md**
- Ajout de la ligne Leçon 5.17 au tableau des leçons

**study_guide.md**
- Ajout du sujet Raisonnement multi-agent antagoniste à la carte mentale et à la description en prose des Sujets avancés

#### Corrections de code et de sécurité

**Module 05 - Agents antagonistes (`mcp-adversarial-agents`)**
- **Correction de sécurité — injection de commande** : remplacement de l’interpolation shell `execSync` par `execFile` + `promisify` dans l’outil TypeScript `run_python`, supprimant la surface d’injection de commande (le code contrôlé par LLM est désormais transmis comme élément littéral argv sans intervention du shell)
- **Câblage boucle outil MCP** : mise à jour de l’orchestrateur de débat Python pour utiliser le client `AsyncAnthropic` (remplaçant le `Anthropic` synchrone bloquant), passer une `ClientSession` en direct à chaque tour d’agent, récupérer la liste des outils via `session.list_tools()` à chaque tour, et envoyer les blocs `tool_use` via `session.call_tool()` en boucle jusqu’à ce que le modèle émette une réponse texte finale

#### Mises à jour des dépendances

- Mise à jour de `hono` en version 4.12.12 dans plusieurs paquets (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Mise à jour de `@hono/node-server` de 1.19.11 à 1.19.13 dans les paquets TypeScript
- Mise à jour de `cryptography` de 46.0.5 à 46.0.7 dans les paquets Python (labs 3 et 4 de 10-StreamliningAIWorkflows)
- Mise à jour de `lodash` de 4.17.23 à 4.18.1 dans l’inspecteur 10-StreamliningAIWorkflows

#### Traductions

- Synchronisation des traductions pour plus de 48 langues avec les derniers changements sources (mise à jour i18n)

---

## 5 février 2026

### Validation et améliorations de navigation à l’échelle du dépôt

#### Nouveau contenu du programme ajouté

**Module 03 - Premiers pas**
- **12-mcp-hosts/README.md** : nouveau guide complet pour la configuration des hôtes MCP
  - Exemples de configuration Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Modèles de configuration JSON pour tous les hôtes majeurs
  - Tableau comparatif des types de transport (stdio, SSE/HTTP, WebSocket)
  - Résolution des problèmes de connexion courants
  - Bonnes pratiques de sécurité pour la configuration des hôtes

- **13-mcp-inspector/README.md** : nouveau guide de débogage pour MCP Inspector
  - Méthodes d’installation (npx, npm global, depuis la source)
  - Connexion aux serveurs via stdio et HTTP/SSE
  - Tests d’outils, ressources et workflows d’invitations
  - Intégration VS Code avec MCP Inspector
  - Scénarios de débogage fréquents avec solutions

**Module 04 - Mise en œuvre pratique**
- **pagination/README.md** : nouveau guide d’implémentation de pagination
  - Modèles de pagination basée sur curseur en Python, TypeScript, Java
  - Gestion côté client de la pagination
  - Stratégies de design de curseurs (opaque vs structuré)
  - Recommandations d’optimisation des performances

**Module 05 - Sujets avancés**
- **mcp-protocol-features/README.md** : exposition approfondie des fonctionnalités du protocole
  - Implémentation des notifications de progression
  - Modèles d’annulation des requêtes
  - Modèles de ressources avec modèles d’URI
  - Gestion du cycle de vie des serveurs
  - Contrôle du niveau de journalisation
  - Modèles de gestion des erreurs avec codes JSON-RPC

#### Corrections de navigation (plus de 24 fichiers modifiés)

**README principaux des modules**
- Liens désormais vers la première leçon ET le module suivant

**Sous-fichiers 02-Security**
- Les 5 documents supplémentaires de sécurité disposent désormais d’une navigation « Quoi suivre »

**Fichiers 09-CaseStudy**
- Tous les fichiers d’étude de cas disposent désormais d’une navigation séquentielle

**Labs 10-StreamliningAI**
- Ajout de la section « Quoi suivre » dans la vue d’ensemble du Module 10 et du Module 11

#### Corrections de code et contenu

**Mises à jour SDK et dépendances**
- Correction de la version openai vide à `^4.95.0`
- Mise à jour du SDK de `^1.8.0` à `>=1.26.0`
- Mise à jour des pins de version mcp à `>=1.26.0`

**Corrections de code**
- Correction du modèle invalide `gpt-4o-mini` en `gpt-4.1-mini`

**Corrections de contenu**
- Correction de lien cassé `READMEmd` → `README.md`, correction de l’en-tête de programme `Module 1-3` → `Module 0-3`, correction de casse sensible de chemin
- Suppression du contenu en double corrompu du Case Study 5

**Améliorations pour débutants**
- Ajout d’introduction appropriée, objectifs d’apprentissage, et prérequis pour les débutants

#### Mises à jour du programme

**README.md principal**
- Ajout des entrées 3.12 (Hôtes MCP), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Fonctionnalités du protocole) dans le tableau de programme

**README des modules**
- Ajout des leçons 12 et 13 à la liste des leçons
- Ajout de la section Guides pratiques avec lien vers la pagination
- Ajout des leçons 5.15 (Transport personnalisé) et 5.16 (Fonctionnalités du protocole)

**study_guide.md**
- Mise à jour de la carte mentale avec tous les nouveaux sujets : Configuration Hôtes MCP, MCP Inspector, Stratégies de Pagination, Exploration des Fonctionnalités du Protocole

## 28 janvier 2026

### Revue de conformité à la spécification MCP 2025-11-25

#### Amélioration des concepts de base (01-CoreConcepts/)
- **Nouvelle primitive client - Roots** : ajout d’une documentation complète sur la primitive client Roots, permettant aux serveurs de comprendre les limites du système de fichiers et les permissions d’accès
- **Annotations d’outils** : ajout de documentation sur les annotations comportementales des outils (`readOnlyHint`, `destructiveHint`) pour améliorer les décisions d’exécution des outils
- **Appel d’outils dans l’échantillonnage** : mise à jour de la documentation Sampling d’inclusion des paramètres `tools` et `toolChoice` pour l’invocation pilotée par modèle d’outils pendant les requêtes Sampling
- **Élicitation par mode URL** : ajout de documentation sur l’élicitation basée sur URL pour les interactions web externes initiées par le serveur
- **Tâches (Expérimental)** : ajout d’une nouvelle section documentant la fonctionnalité expérimentale Tâches pour les wrappers d’exécution durables et la récupération différée des résultats
- **Support des icônes** : mention que les outils, ressources, modèles de ressources et invites peuvent désormais inclure des icônes comme métadonnées supplémentaires

#### Mises à jour de la documentation
- **README.md** : ajout de la référence à la spécification MCP 2025-11-25 et explication du versionnage par date
- **study_guide.md** : mise à jour de la carte du programme pour inclure les Tâches et Annotations d’outils dans la section Concepts de base ; mise à jour du timestamp du document

#### Vérification de conformité à la spécification
- **Version du protocole** : vérification que toute la documentation référence la spécification MCP 2025-11-25 actuelle
- **Alignement de l’architecture** : confirmation de l’exactitude de la documentation sur l’architecture à deux couches (couche données + couche transport)
- **Documentation des primitives** : validation des primitives serveur (Ressources, Invites, Outils) et primitives client (Sampling, Élicitation, Journalisation, Roots)
- **Mécanismes de transport** : vérification de la documentation des transports STDIO et HTTP streamable
- **Conseils de sécurité** : confirmation de la conformité avec les bonnes pratiques actuelles de sécurité MCP

#### Principales fonctionnalités MCP 2025-11-25 documentées
- **Découverte OpenID Connect** : découverte des serveurs d’authentification via OIDC
- **Documents de métadonnées OAuth Client ID** : mécanisme recommandé d’enregistrement client
- **JSON Schema 2020-12** : dialecte par défaut pour les définitions de schémas MCP
- **Système de paliers SDK** : exigences formalisées pour le support et la maintenance des fonctionnalités SDK
- **Structure de gouvernance** : formalisation des groupes de travail et groupes d’intérêt dans la gouvernance MCP

### Mise à jour majeure de la documentation de sécurité (02-Security/)

#### Intégration du workshop Sherpa MCP Security Summit
- **Nouvelle ressource de formation pratique** : ajout d’une intégration complète avec le [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) dans toute la documentation sécurité
- **Couverture de la progression expéditionnaire** : documentation complète du parcours camp à camp, du camp de base au sommet
- **Alignement OWASP** : tous les conseils de sécurité sont désormais cartographiés aux risques du guide OWASP MCP Azure Security

#### Intégration OWASP MCP Top 10
- **Nouvelle section** : ajout d’un tableau des risques OWASP MCP Top 10 avec mesures d’atténuation Azure dans le README principal de sécurité
- **Documentation basée sur les risques** : mise à jour de mcp-security-controls-2025.md avec références aux risques OWASP MCP pour chaque domaine de sécurité
- **Architecture de référence** : lien vers l’architecture de référence OWASP MCP Azure Security Guide et modèles d’implémentation

#### Fichiers de sécurité mis à jour
- **README.md** : ajout de l’aperçu du workshop Sherpa, tableau du parcours d’expédition, résumé des risques OWASP MCP Top 10 et section formation pratique
- **mcp-security-controls-2025.md** : mise à jour de l’en-tête à février 2026, ajout des références risques OWASP (MCP01-MCP08), correction d’incohérence de version de spécification
- **mcp-security-best-practices-2025.md** : ajout de la section ressources Sherpa et OWASP, mise à jour du timestamp
- **mcp-best-practices.md** : ajout de la section formation pratique avec liens Sherpa et OWASP
- **azure-content-safety-implementation.md** : ajout de la référence OWASP MCP06, alignement sur Camp 3 Sherpa, et section ressources supplémentaires

#### Nouveaux liens de ressources ajoutés
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Pages individuelles des risques OWASP MCP (MCP01-MCP10)

### Alignement à l’échelle du programme avec la spécification MCP 2025-11-25

#### Module 03 - Premiers pas
- **Documentation SDK** : ajout du SDK Go à la liste officielle des SDK ; mise à jour de toutes les références SDK pour alignement avec la spécification MCP 2025-11-25
- **Clarification des transports** : mise à jour des descriptions des transports STDIO et HTTP Streaming avec références explicites à la spécification

#### Module 04 - Mise en œuvre pratique
- **Mises à jour SDK** : ajout du SDK Go ; mise à jour de la liste SDK avec référence à la version de spécification
- **Spécifications d’autorisation** : mise à jour du lien vers la spécification MCP Authorization version 2025-11-25 actuelle

#### Module 05 - Sujets avancés
- **Nouvelles fonctionnalités** : ajout d’une note sur les nouvelles fonctionnalités de la spécification MCP 2025-11-25 (Tâches, Annotations d’outils, Élicitation par mode URL, Roots)
- **Ressources de sécurité** : ajout des liens OWASP MCP Top 10 et workshop Sherpa aux références supplémentaires

#### Module 06 - Contributions communautaires
- **Liste SDK** : ajout des SDK Swift et Rust ; mise à jour du lien de spécification vers 2025-11-25
- **Référence spécification** : mise à jour du lien vers l’URL directe de la spécification MCP

#### Module 07 - Leçons des premiers utilisateurs
- **Mises à jour des ressources** : ajout du lien MCP Specification 2025-11-25 et OWASP MCP Top 10 dans les ressources supplémentaires

#### Module 08 - Bonnes pratiques
- **Version de spécification** : mise à jour de la référence à MCP Specification 2025-11-25
- **Ressources de sécurité** : ajout d’OWASP MCP Top 10 et du workshop Sherpa aux références supplémentaires

#### Module 10 - Optimisation des flux AI
- **Mise à jour du badge** : passage du badge version MCP de la version SDK (1.9.3) à la version spécification (2025-11-25)
- **Liens ressources** : mise à jour du lien MCP Specification ; ajout de OWASP MCP Top 10

#### Module 11 - Laboratoires pratiques MCP Server
- **Référence spécification** : mise à jour du lien MCP Specification à la version 2025-11-25
- **Ressources de sécurité** : ajout de OWASP MCP Top 10 aux ressources officielles

## 18 décembre 2025
### Mise à jour de la documentation de sécurité - Spécification MCP 2025-11-25

#### Bonnes pratiques de sécurité MCP (02-Security/mcp-best-practices.md) - Mise à jour de la version de la spécification
- **Mise à jour de la version du protocole** : Mise à jour pour référencer la dernière spécification MCP 2025-11-25 (publiée le 25 novembre 2025)
  - Mise à jour de toutes les références à la version de la spécification de 2025-06-18 à 2025-11-25
  - Mise à jour des références de date des documents d’août 18, 2025 à décembre 18, 2025
  - Vérification de toutes les URL de spécifications pointant vers la documentation actuelle
- **Validation du contenu** : Validation complète des bonnes pratiques de sécurité selon les dernières normes
  - **Solutions de sécurité Microsoft** : Vérification de la terminologie et des liens actuels pour Prompt Shields (anciennement « Risk de jailbreak »), Azure Content Safety, Microsoft Entra ID, et Azure Key Vault
  - **Sécurité OAuth 2.1** : Confirmation de l’alignement avec les meilleures pratiques de sécurité OAuth les plus récentes
  - **Normes OWASP** : Validation que les références OWASP Top 10 pour LLM restent actuelles
  - **Services Azure** : Vérification de tous les liens de documentation Microsoft Azure et bonnes pratiques
- **Alignement aux normes** : Tous les standards de sécurité référencés sont confirmés à jour
  - Cadre de gestion des risques de l’IA NIST
  - ISO 27001:2022
  - Bonnes pratiques de sécurité OAuth 2.1
  - Cadres de sécurité et conformité Azure
- **Ressources pour l’implémentation** : Validation de tous les liens de guides et ressources d’implémentation
  - Modèles d’authentification Azure API Management
  - Guides d’intégration Microsoft Entra ID
  - Gestion des secrets Azure Key Vault
  - Pipelines DevSecOps et solutions de surveillance

### Assurance qualité de la documentation
- **Conformité à la spécification** : Garantie que toutes les exigences de sécurité MCP obligatoires (DOIT/NE DOIT PAS) sont alignées avec la dernière spécification
- **Actualité des ressources** : Vérification de tous les liens externes vers la documentation Microsoft, normes de sécurité et guides d’implémentation
- **Couverture des bonnes pratiques** : Confirmation de la couverture complète des thématiques d’authentification, d’autorisation, menaces spécifiques à l’IA, sécurité de la chaîne d’approvisionnement et modèles d’entreprise

## 6 octobre 2025

### Extension de la section Premiers Pas – Utilisation avancée du serveur & Authentification simple

#### Utilisation avancée du serveur (03-GettingStarted/10-advanced)
- **Nouveau chapitre ajouté** : Introduction d’un guide complet d’utilisation avancée des serveurs MCP, couvrant les architectures serveur régulières et bas niveau.
  - **Serveur régulier vs bas niveau** : Comparaison détaillée et exemples de code en Python et TypeScript pour les deux approches.
  - **Conception basée sur des handlers** : Explication de la gestion des outils/ressources/prompt via des handlers pour des implémentations serveur évolutives et flexibles.
  - **Modèles pratiques** : Scénarios d’utilisation réels où les modèles serveur bas niveau sont bénéfiques pour des fonctionnalités et architectures avancées.

#### Authentification simple (03-GettingStarted/11-simple-auth)
- **Nouveau chapitre ajouté** : Guide étape par étape pour implémenter une authentification simple sur les serveurs MCP.
  - **Concepts d’authentification** : Explication claire de l’authentification vs autorisation, et gestion des identifiants.
  - **Implémentation d’une auth basique** : Modèles d’authentification basés sur middleware en Python (Starlette) et TypeScript (Express), avec exemples de code.
  - **Progression vers une sécurité avancée** : Guide pour démarrer avec une authentification simple puis évoluer vers OAuth 2.1 et RBAC, avec références aux modules de sécurité avancée.

Ces ajouts offrent des conseils pratiques et concrets pour construire des implémentations serveur MCP plus robustes, sécurisées et flexibles, faisant le pont entre concepts fondamentaux et modèles avancés en production.

## 29 septembre 2025

### Laboratoires d’intégration base de données MCP Server – Parcours complet d’apprentissage pratique

#### 11-MCPServerHandsOnLabs - Nouveau cursus complet d’intégration base de données
- **Parcours complet de 13 laboratoires** : Ajout d’un curriculum pratique complet pour construire des serveurs MCP prêts pour la production avec intégration de base PostgreSQL
  - **Cas d’utilisation concret** : Analyse de données Zava Retail démontrant les modèles d’entreprise
  - **Progression d’apprentissage structurée** :
    - **Labs 00-03 : Fondations** – Introduction, Architecture fondamentale, Sécurité & Multi-tenant, Configuration de l’environnement
    - **Labs 04-06 : Construction du serveur MCP** – Conception et schéma de base de données, Implémentation serveur MCP, Développement d’outils  
    - **Labs 07-09 : Fonctionnalités avancées** – Intégration de recherche sémantique, Tests & débogage, Intégration VS Code
    - **Labs 10-12 : Production & bonnes pratiques** – Stratégies de déploiement, Surveillance & observabilité, Bonnes pratiques & optimisation
  - **Technologies d’entreprise** : Framework FastMCP, PostgreSQL avec pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Fonctionnalités avancées** : Sécurité au niveau des lignes (RLS), recherche sémantique, accès multi-tenant aux données, vecteurs d’embeddings, surveillance en temps réel

#### Standardisation terminologique – Conversion de module en laboratoire
- **Mise à jour documentaire complète** : Mise à jour systématique de tous les fichiers README dans 11-MCPServerHandsOnLabs pour utiliser la terminologie « Laboratoire » au lieu de « Module »
  - **En-têtes de section** : Mise à jour de « Ce que couvre ce module » en « Ce que couvre ce laboratoire » dans les 13 laboratoires
  - **Description du contenu** : Remplacement de « Ce module fournit… » par « Ce laboratoire fournit… » dans toute la documentation
  - **Objectifs pédagogiques** : Mise à jour de « À la fin de ce module… » en « À la fin de ce laboratoire… »
  - **Liens de navigation** : Conversion de toutes les références « Module XX : » en « Laboratoire XX : » dans les renvois et la navigation
  - **Suivi d’achèvement** : Changement de « Après avoir complété ce module… » en « Après avoir complété ce laboratoire… »
  - **Références techniques préservées** : Maintien des références aux modules Python dans les fichiers de configuration (ex. « "module": "mcp_server.main" »)

#### Amélioration du guide d’étude (study_guide.md)
- **Carte visuelle du curriculum** : Ajout de la nouvelle section « 11. Laboratoires d’intégration base de données » avec visualisation complète de la structure des laboratoires
- **Structure du dépôt** : Mise à jour de dix à onze sections principales avec description détaillée de 11-MCPServerHandsOnLabs
- **Conseils du parcours pédagogique** : Amélioration des instructions de navigation couvrant les sections 00-11
- **Couverture technologique** : Ajout des détails sur FastMCP, PostgreSQL, intégration des services Azure
- **Résultats d’apprentissage** : Mise en avant du développement de serveurs prêts pour la production, modèles d’intégration base de données et sécurité d’entreprise

#### Amélioration de la structure du README principal
- **Terminologie basée sur les laboratoires** : Mise à jour du README.md principal dans 11-MCPServerHandsOnLabs pour un usage cohérent de la structure « Laboratoire »
- **Organisation du parcours pédagogique** : Progression claire allant des concepts fondamentaux à l’implémentation avancée puis au déploiement en production
- **Focus terrain réel** : Accent sur l’apprentissage pratique avec modèles et technologies d’entreprise

### Améliorations qualité et cohérence documentaire
- **Accent apprentissage pratique** : Renforcement de l’approche par laboratoires tout au long de la documentation
- **Mise en avant des modèles d’entreprise** : Soulignement des implémentations prêtes pour la production et des considérations de sécurité d’entreprise
- **Intégration technologique** : Couverture complète des services Azure modernes et modèles d’intégration IA
- **Progression pédagogique** : Parcours clair et structuré des concepts de base au déploiement en production

## 26 septembre 2025

### Amélioration des études de cas – Intégration du registre MCP GitHub

#### Études de cas (09-CaseStudy/) – Focus développement de l’écosystème
- **README.md** : Expansion majeure avec étude de cas complète du registre MCP GitHub
  - **Étude de cas registre MCP GitHub** : Nouvelle étude détaillée examinant le lancement du registre MCP GitHub en septembre 2025
    - **Analyse des problèmes** : Examen approfondi de la fragmentation de la découverte et du déploiement des serveurs MCP
    - **Architecture de la solution** : Approche registre centralisé GitHub avec installation VS Code en un clic
    - **Impact business** : Améliorations mesurables de l’intégration développeur et productivité
    - **Valeur stratégique** : Focus sur déploiement d’agents modulaires et interopérabilité entre outils
    - **Développement de l’écosystème** : Positionnement comme plateforme fondatrice pour l’intégration agentique
  - **Structure enrichie des études de cas** : Mise à jour des sept études de cas avec formatage cohérent et description complète
    - Agents de voyage Azure AI : mise en orchestration multi-agents
    - Intégration Azure DevOps : automatisation des workflows
    - Récupération documentaire en temps réel : client console Python
    - Générateur de plan d’étude interactif : web app conversationnelle Chainlit
    - Documentation dans l’éditeur : intégration VS Code & GitHub Copilot
    - Azure API Management : modèles d’intégration API entreprise
    - Registre MCP GitHub : développement de l’écosystème et plateforme communautaire
  - **Conclusion complète** : Réécriture de la section conclusion soulignant les sept études de cas couvrant plusieurs dimensions d’implémentation MCP
    - Intégration entreprise, orchestration multi-agent, productivité développeur
    - Développement de l’écosystème, applications éducatives
    - Meilleure compréhension des modèles architecturaux, stratégies d’implémentation et bonnes pratiques
    - Mise en avant de MCP comme protocole mature et prêt pour la production

#### Mises à jour du guide d’étude (study_guide.md)
- **Carte visuelle du curriculum** : Mise à jour de la carte mentale pour inclure le registre MCP GitHub dans la section études de cas
- **Description des études de cas** : Enrichissement des descriptions génériques vers une décomposition détaillée des sept études
- **Structure du dépôt** : Mise à jour de la section 10 pour refléter la couverture complète avec détails spécifiques d’implémentation
- **Intégration changelog** : Ajout de l’entrée du 26 septembre 2025 documentant l’ajout du registre MCP GitHub et les améliorations des études de cas
- **Mise à jour des dates** : Actualisation du timestamp du pied de page pour refléter la dernière révision (26 septembre 2025)

### Améliorations qualité documentaire
- **Uniformisation** : Standardisation du format et de la structure des études de cas sur les sept exemples
- **Couverture complète** : Études couvrant dorénavant les scénarios entreprise, productivité développeur et développement d’écosystème
- **Positionnement stratégique** : Accent renforcé sur MCP comme plateforme fondatrice pour déploiement de systèmes agentiques
- **Intégration des ressources** : Mise à jour des ressources additionnelles incluant le lien vers le registre MCP GitHub

## 15 septembre 2025

### Extension des sujets avancés – Transports personnalisés & ingénierie du contexte

#### Transports personnalisés MCP (05-AdvancedTopics/mcp-transport/) – Nouveau guide d’implémentation avancée
- **README.md** : Guide complet d’implémentation pour les mécanismes de transport MCP personnalisés
  - **Transport Azure Event Grid** : Implémentation complète de transport événementiel serverless
    - Exemples en C#, TypeScript et Python avec intégration Azure Functions
    - Modèles d’architecture événementielle pour solutions MCP évolutives
    - Récepteurs webhook et gestion des messages en push
  - **Transport Azure Event Hubs** : Implémentation de transport streaming à haut débit
    - Capacités de streaming en temps réel pour scénarios à faible latence
    - Stratégies de partitionnement et gestion des checkpoints
    - Regroupement de messages et optimisation des performances
  - **Modèles d’intégration entreprise** : Exemples architecturaux prêts pour production
    - Traitement MCP distribué sur plusieurs Azure Functions
    - Architectures hybrides combinant plusieurs types de transport
    - Durabilité, fiabilité et gestion d’erreurs des messages
  - **Sécurité & surveillance** : Intégration Azure Key Vault et modèles d’observabilité
    - Authentification par identité managée et accès au moindre privilège
    - Télémetry Application Insights et suivi des performances
    - Disjoncteurs et modèles de tolérance aux pannes
  - **Cadres de test** : Stratégies complètes pour tests des transports personnalisés
    - Tests unitaires avec mocks et doubles de test
    - Tests d’intégration avec Azure Test Containers
    - Considérations pour tests de charge et performance

#### Ingénierie du contexte (05-AdvancedTopics/mcp-contextengineering/) – Discipline IA émergente
- **README.md** : Exploration complète de l’ingénierie du contexte en tant que champ émergent
  - **Principes fondamentaux** : Partage complet du contexte, prise de décision par actions, gestion de la fenêtre contextuelle
  - **Alignement avec le protocole MCP** : Comment le design MCP répond aux défis d’ingénierie du contexte
    - Limitations des fenêtres contextuelles et stratégies de chargement progressif
    - Détermination de pertinence et récupération dynamique du contexte
    - Gestion multimodale du contexte et considérations de sécurité
  - **Approches d’implémentation** : Architectures mono-thread vs multi-agents
    - Fragmentation et priorisation du contexte
    - Chargement progressif du contexte et stratégies de compression
    - Approches du contexte en couches et optimisation de récupération
  - **Cadre de mesure** : Métriques émergentes pour évaluation de l’efficacité du contexte
    - Efficacité d’entrée, performances, qualité et expérience utilisateur
    - Approches expérimentales pour optimisation du contexte
    - Analyse des échecs et méthodologies d’amélioration

#### Mise à jour de la navigation du curriculum (README.md)
- **Structure de module enrichie** : Mise à jour du tableau de curriculum pour inclure les nouveaux sujets avancés
  - Ajout des entrées Ingénierie du contexte (5.14) et Transport personnalisé (5.15)
  - Formatage cohérent et liens de navigation pour tous les modules
  - Descriptions mises à jour reflétant le périmètre actuel du contenu

### Améliorations de la structure des dossiers
- **Standardisation des noms** : Renommage de « mcp transport » en « mcp-transport » pour cohérence avec autres dossiers des sujets avancés
- **Organisation du contenu** : Tous les dossiers 05-AdvancedTopics suivent désormais un modèle de nommage cohérent (mcp-[topic])

### Améliorations qualité documentaire
- **Alignement avec la spécification MCP** : Tout nouveau contenu réfère à la spécification MCP 2025-06-18 actuelle
- **Exemples multi-langages** : Exemples complets en C#, TypeScript, et Python
- **Focalisation entreprise** : Modèles prêts pour production et intégration cloud Azure
- **Documentation visuelle** : Diagrammes Mermaid pour visualisation architecturale et flux

## 18 août 2025

### Mise à jour complète documentation – Normes MCP 2025-06-18

#### Bonnes pratiques de sécurité MCP (02-Security/) – Modernisation complète
- **MCP-SECURITY-BEST-PRACTICES-2025.md** : Réécriture complète alignée sur la Spécification MCP 2025-06-18  
  - **Exigences Obligatoires** : Ajout des exigences explicites DOIT/NE DOIT PAS de la spécification officielle avec des indicateurs visuels clairs  
  - **12 Pratiques de Sécurité Clés** : Restructuration de la liste de 15 éléments en domaines de sécurité complets  
    - Sécurité des Tokens & Authentification avec intégration de fournisseur d'identité externe  
    - Gestion des Sessions & Sécurité des Transports avec exigences cryptographiques  
    - Protection Contre les Menaces Spécifiques à l’IA avec intégration Microsoft Prompt Shields  
    - Contrôle d’Accès & Permissions avec principe du moindre privilège  
    - Sécurité et Monitoring du Contenu avec intégration Azure Content Safety  
    - Sécurité de la Chaîne d’Approvisionnement avec vérification complète des composants  
    - Sécurité OAuth & Prévention du Confused Deputy avec mise en œuvre PKCE  
    - Réponse aux Incidents & Reprise avec capacités automatisées  
    - Conformité & Gouvernance avec alignement réglementaire  
    - Contrôles de Sécurité Avancés avec architecture Zero Trust  
    - Intégration de l’Écosystème de Sécurité Microsoft avec solutions complètes  
    - Évolution Continue de la Sécurité avec pratiques adaptatives  
  - **Solutions de Sécurité Microsoft** : Orientation améliorée pour l’intégration de Prompt Shields, Azure Content Safety, Entra ID, et GitHub Advanced Security  
  - **Ressources de Mise en Œuvre** : Liens complets classés par Documentation Officielle MCP, Solutions de Sécurité Microsoft, Normes de Sécurité, et Guides d’Implémentation  

#### Contrôles de Sécurité Avancés (02-Security/) - Implémentation Entreprise  
- **MCP-SECURITY-CONTROLS-2025.md** : Refondation complète avec cadre de sécurité de niveau entreprise  
  - **9 Domaines de Sécurité Complets** : Extension des contrôles basiques à un cadre détaillé pour entreprises  
    - Authentification & Autorisation Avancées avec intégration Microsoft Entra ID  
    - Sécurité des Tokens & Contrôles Anti-Passthrough avec validation complète  
    - Contrôles de Sécurité des Sessions avec prévention du détournement  
    - Contrôles de Sécurité Spécifiques à l’IA avec prévention d’injection de prompt et empoisonnement d’outil  
    - Prévention des Attaques de Confused Deputy avec sécurité proxy OAuth  
    - Sécurité d’Exécution des Outils avec sandboxing et isolation  
    - Contrôles de Sécurité de la Chaîne d’Approvisionnement avec vérification des dépendances  
    - Contrôles de Surveillance & Détection avec intégration SIEM  
    - Réponse aux Incidents & Reprise avec capacités automatisées  
  - **Exemples de Mise en Œuvre** : Ajout de blocs de configuration YAML détaillés et exemples de code  
  - **Intégration des Solutions Microsoft** : Couverture complète des services de sécurité Azure, GitHub Advanced Security, et gestion d'identité entreprise  

#### Sécurité des Sujets Avancés (05-AdvancedTopics/mcp-security/) - Implémentation Prête pour Production  
- **README.md** : Réécriture complète pour implémentation de sécurité en entreprise  
  - **Alignement avec la Spécification Courante** : Mise à jour vers Spécification MCP 2025-06-18 avec exigences de sécurité obligatoires  
  - **Authentification Améliorée** : Intégration Microsoft Entra ID avec exemples complets en .NET et Java Spring Security  
  - **Intégration de la Sécurité IA** : Mise en œuvre de Microsoft Prompt Shields et Azure Content Safety avec exemples Python détaillés  
  - **Atténuation Avancée des Menaces** : Exemples complets d’implémentation pour  
    - Prévention des Attaques de Confused Deputy avec PKCE et validation du consentement utilisateur  
    - Prévention du Passthrough de Token avec validation audience et gestion sécurisée des tokens  
    - Prévention du Détournement de Session avec liaison cryptographique et analyse comportementale  
  - **Intégration de la Sécurité Entreprise** : Monitoring Azure Application Insights, pipelines de détection des menaces, et sécurité de la chaîne d’approvisionnement  
  - **Liste de Contrôle d’Implémentation** : Contrôles de sécurité obligatoires vs. recommandés clairement différenciés avec bénéfices écosystème sécurité Microsoft  

### Qualité de la Documentation & Alignement Normatif  
- **Références de Spécification** : Mise à jour de toutes les références vers la Spécification MCP 2025-06-18  
- **Écosystème de Sécurité Microsoft** : Orientation d’intégration renforcée dans toute la documentation de sécurité  
- **Implémentation Pratique** : Ajout d’exemples de code détaillés en .NET, Java et Python avec patrons professionnels  
- **Organisation des Ressources** : Classification complète des documentations officielles, normes de sécurité, et guides d’implémentation  
- **Indicateurs Visuels** : Marquage clair des exigences obligatoires vs. bonnes pratiques recommandées  

#### Concepts Clés (01-CoreConcepts/) - Modernisation Complète  
- **Mise à Jour de la Version du Protocole** : Passage à la Spécification MCP 2025-06-18 avec versionnement basé sur la date (format AAAA-MM-JJ)  
- **Affinement de l’Architecture** : Descriptions améliorées des Hôtes, Clients et Serveurs pour refléter les architectures MCP actuelles  
  - Hôtes désormais clairement définis comme applications IA coordonnant plusieurs connexions clients MCP  
  - Clients décrits comme connecteurs de protocole maintenant des relations un-à-un avec serveurs  
  - Serveurs enrichis avec scénarios de déploiement local vs. distant  
- **Restructuration des Primitives** : Refonte complète des primitives serveur et client  
  - Primitives Serveur : Ressources (sources de données), Prompts (modèles), Outils (fonctions exécutables) avec explications et exemples détaillés  
  - Primitives Client : Échantillonnage (complétions LLM), Sollicitation (entrée utilisateur), Journalisation (debug/surveillance)  
  - Mise à jour avec les modèles actuels de découverte (`*/list`), récupération (`*/get`), et exécution (`*/call`)  
- **Architecture du Protocole** : Introduction d’un modèle à deux couches  
  - Couche Données : Fondation JSON-RPC 2.0 avec gestion du cycle de vie et primitives  
  - Couche Transport : STDIO (local) et HTTP Streamable avec SSE (transport distant)  
- **Cadre de Sécurité** : Principes de sécurité détaillés incluant consentement explicite utilisateur, protection de la vie privée, sécurité d'exécution des outils, et sécurité du transport  
- **Modèles de Communication** : Messages du protocole mis à jour pour montrer initialisation, découverte, exécution et notification  
- **Exemples de Code** : Actualisation des exemples multilingues (.NET, Java, Python, JavaScript) pour refléter les patrons SDK MCP contemporains  

#### Sécurité (02-Security/) - Refondation Complète de la Sécurité  
- **Alignement Normatif** : Plein alignement avec les exigences de sécurité de la Spécification MCP 2025-06-18  
- **Évolution de l’Authentification** : Documentée depuis serveurs OAuth personnalisés vers délégation à fournisseur d’identité externe (Microsoft Entra ID)  
- **Analyse des Menaces Spécifiques à l’IA** : Couverture améliorée des vecteurs d’attaque IA modernes  
  - Scénarios détaillés d’attaques par injection de prompt avec exemples réels  
  - Mécanismes d’empoisonnement d’outil et attaques de type « rug pull »  
  - Empoisonnement de fenêtre contextuelle et attaques de confusion de modèle  
- **Solutions de Sécurité IA Microsoft** : Couverture complète de l’écosystème de sécurité Microsoft  
  - AI Prompt Shields avec détection avancée, mise en lumière, et techniques de délimitation  
  - Modèles d’intégration Azure Content Safety  
  - GitHub Advanced Security pour protection de la chaîne d’approvisionnement  
- **Atténuation Avancée des Menaces** : Contrôles de sécurité détaillés pour  
  - Détournement de session avec scénarios d’attaque spécifiques MCP et exigences cryptographiques pour ID de session  
  - Problèmes de Confused Deputy dans scénarios proxy MCP avec exigences explicites de consentement  
  - Vulnérabilités de passthrough de token avec contrôles de validation obligatoires  
- **Sécurité de la Chaîne d’Approvisionnement** : Amélioration de la couverture incluant modèles foundation, services d’embedding, fournisseurs de contexte et API tierces  
- **Sécurité de la Fondation** : Intégration renforcée avec les patrons de sécurité entreprise incluant architecture Zero Trust et écosystème de sécurité Microsoft  
- **Organisation des Ressources** : Liens complets classés par type (Docs Officiels, Normes, Recherche, Solutions Microsoft, Guides d’Implémentation)  

### Améliorations de la Qualité Documentaire  
- **Objectifs d’Apprentissage Structurés** : Objectifs enrichis avec résultats spécifiques et exploitables  
- **Références Croisées** : Ajout de liens entre sujets de sécurité et concepts clés  
- **Informations Actuelles** : Mise à jour de toutes les dates et liens vers normes courantes  
- **Orientation à l’Implémentation** : Ajout de directives précises et exploitables dans les deux sections  

## 16 juillet 2025  

### Améliorations du README et de la Navigation  
- Refonte complète de la navigation du curriculum dans README.md  
- Remplacement des balises `<details>` par un format tableau plus accessible  
- Création d’options de mise en page alternatives dans le nouveau dossier "alternative_layouts"  
- Ajout d’exemples de navigation par cartes, onglets, et accordéon  
- Mise à jour de la section structure du dépôt pour inclure tous les fichiers récents  
- Amélioration de la section "Comment utiliser ce curriculum" avec recommandations claires  
- Mise à jour des liens vers la spécification MCP vers les URL correctes  
- Ajout de la section Ingénierie du Contexte (5.14) à la structure du curriculum  

### Mises à Jour du Guide d’Étude  
- Révision complète du guide d’étude pour alignement avec la structure actuelle du dépôt  
- Ajout de nouvelles sections pour MCP Clients & Outils, et MCP Servers populaires  
- Mise à jour de la carte visuelle du curriculum pour refléter tous les sujets  
- Amélioration des descriptions des Sujets Avancés pour couvrir tous les domaines spécialisés  
- Mise à jour de la section Études de Cas pour refléter des exemples réels  
- Ajout de ce journal de modifications complet  

### Contributions Communautaires (06-CommunityContributions/)  
- Ajout d’informations détaillées sur les serveurs MCP pour génération d’images  
- Ajout d’une section complète sur l’utilisation de Claude dans VSCode  
- Ajout d’instructions d’installation et d’utilisation du client terminal Cline  
- Mise à jour de la section MCP client pour inclure toutes les options populaires  
- Amélioration des exemples de contribution avec des échantillons de code plus précis  

### Sujets Avancés (05-AdvancedTopics/)  
- Organisation de tous les dossiers de sujets spécialisés avec une nomination cohérente  
- Ajout de matériel et exemples d’ingénierie contextuelle  
- Ajout de documentation d’intégration de l’agent Foundry  
- Amélioration de la documentation d’intégration de sécurité Entra ID  

## 11 juin 2025  

### Création Initiale  
- Publication de la première version du curriculum MCP pour Débutants  
- Création de la structure basique des 10 sections principales  
- Implémentation de la carte visuelle du curriculum pour navigation  
- Ajout de projets exemples initiaux en plusieurs langages de programmation  

### Prise en Main (03-GettingStarted/)  
- Création des premiers exemples d’implémentation serveur  
- Ajout de conseils pour le développement client  
- Inclusion d’instructions d’intégration client LLM  
- Ajout de documentation d’intégration VS Code  
- Implémentation d’exemples serveur Server-Sent Events (SSE)  

### Concepts Clés (01-CoreConcepts/)  
- Ajout d'explications détaillées sur l’architecture client-serveur  
- Création de documentation sur les composants clés du protocole  
- Documentation des modèles de messagerie dans MCP  

## 23 mai 2025  

### Structure du Dépôt  
- Initialisation du dépôt avec structure de dossiers basique  
- Création des fichiers README pour chaque section majeure  
- Mise en place de l’infrastructure de traduction  
- Ajout d’assets images et diagrammes  

### Documentation  
- Création du README.md initial avec vue d’ensemble du curriculum  
- Ajout de CODE_OF_CONDUCT.md et SECURITY.md  
- Mise en place de SUPPORT.md avec conseils pour obtenir de l’aide  
- Création de la structure préliminaire du guide d’étude  

## 15 avril 2025  

### Planification et Cadre  
- Planification initiale du curriculum MCP pour Débutants  
- Définition des objectifs d’apprentissage et public cible  
- Esquisse de la structure en 10 sections du curriculum  
- Élaboration du cadre conceptuel pour exemples et études de cas  
- Création des premiers prototypes d’exemples pour concepts clés

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer la précision, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->