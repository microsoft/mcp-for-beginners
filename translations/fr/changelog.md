# Journal des modifications : Programme MCP pour débutants

Ce document sert de registre pour tous les changements importants apportés au programme Model Context Protocol (MCP) pour débutants. Les modifications sont documentées par ordre chronologique inverse (les plus récentes en premier).

## 18 décembre 2025

### Mise à jour de la documentation de sécurité - Spécification MCP 2025-11-25

#### Meilleures pratiques de sécurité MCP (02-Security/mcp-best-practices.md) - Mise à jour de la version de la spécification
- **Mise à jour de la version du protocole** : Mise à jour pour référencer la dernière spécification MCP 2025-11-25 (publiée le 25 novembre 2025)
  - Mise à jour de toutes les références de version de spécification de 2025-06-18 à 2025-11-25
  - Mise à jour des références de date du document du 18 août 2025 au 18 décembre 2025
  - Vérification que toutes les URL de spécification pointent vers la documentation actuelle
- **Validation du contenu** : Validation complète des meilleures pratiques de sécurité selon les normes les plus récentes
  - **Solutions de sécurité Microsoft** : Vérification de la terminologie actuelle et des liens pour Prompt Shields (anciennement « détection des risques de jailbreak »), Azure Content Safety, Microsoft Entra ID et Azure Key Vault
  - **Sécurité OAuth 2.1** : Confirmation de l’alignement avec les meilleures pratiques de sécurité OAuth les plus récentes
  - **Normes OWASP** : Validation que les références OWASP Top 10 pour les LLM restent à jour
  - **Services Azure** : Vérification de tous les liens de documentation Microsoft Azure et des meilleures pratiques
- **Alignement sur les normes** : Toutes les normes de sécurité référencées sont confirmées à jour
  - Cadre de gestion des risques IA NIST
  - ISO 27001:2022
  - Meilleures pratiques de sécurité OAuth 2.1
  - Cadres de sécurité et conformité Azure
- **Ressources d’implémentation** : Validation de tous les liens et ressources des guides d’implémentation
  - Modèles d’authentification Azure API Management
  - Guides d’intégration Microsoft Entra ID
  - Gestion des secrets Azure Key Vault
  - Pipelines DevSecOps et solutions de surveillance

### Assurance qualité de la documentation
- **Conformité à la spécification** : Garantie que toutes les exigences de sécurité MCP obligatoires (DOIT/NE DOIT PAS) sont alignées avec la dernière spécification
- **Actualité des ressources** : Vérification de tous les liens externes vers la documentation Microsoft, les normes de sécurité et les guides d’implémentation
- **Couverture des meilleures pratiques** : Confirmation d’une couverture complète de l’authentification, de l’autorisation, des menaces spécifiques à l’IA, de la sécurité de la chaîne d’approvisionnement et des modèles d’entreprise

## 6 octobre 2025

### Extension de la section Premiers pas – Utilisation avancée du serveur & Authentification simple

#### Utilisation avancée du serveur (03-GettingStarted/10-advanced)
- **Nouveau chapitre ajouté** : Introduction d’un guide complet sur l’utilisation avancée des serveurs MCP, couvrant les architectures serveur régulières et bas niveau.
  - **Serveur régulier vs bas niveau** : Comparaison détaillée et exemples de code en Python et TypeScript pour les deux approches.
  - **Conception basée sur les gestionnaires** : Explication de la gestion des outils/ressources/invites basée sur des gestionnaires pour des implémentations serveur évolutives et flexibles.
  - **Modèles pratiques** : Scénarios réels où les modèles de serveur bas niveau sont bénéfiques pour des fonctionnalités et architectures avancées.

#### Authentification simple (03-GettingStarted/11-simple-auth)
- **Nouveau chapitre ajouté** : Guide étape par étape pour implémenter une authentification simple dans les serveurs MCP.
  - **Concepts d’authentification** : Explication claire de l’authentification vs autorisation, et gestion des identifiants.
  - **Implémentation d’authentification basique** : Modèles d’authentification basés sur middleware en Python (Starlette) et TypeScript (Express), avec exemples de code.
  - **Progression vers la sécurité avancée** : Conseils pour commencer avec une authentification simple et évoluer vers OAuth 2.1 et RBAC, avec références aux modules de sécurité avancée.

Ces ajouts fournissent des conseils pratiques et concrets pour construire des implémentations de serveurs MCP plus robustes, sécurisées et flexibles, reliant les concepts fondamentaux aux modèles avancés de production.

## 29 septembre 2025

### Laboratoires d’intégration de base de données MCP Server - Parcours d’apprentissage pratique complet

#### 11-MCPServerHandsOnLabs - Nouveau programme complet d’intégration de base de données
- **Parcours d’apprentissage complet de 13 laboratoires** : Ajout d’un programme pratique complet pour construire des serveurs MCP prêts pour la production avec intégration de base de données PostgreSQL
  - **Implémentation en conditions réelles** : Cas d’usage analytique Zava Retail démontrant des modèles de niveau entreprise
  - **Progression d’apprentissage structurée** :
    - **Laboratoires 00-03 : Fondations** - Introduction, architecture de base, sécurité & multi-tenant, configuration de l’environnement
    - **Laboratoires 04-06 : Construction du serveur MCP** - Conception et schéma de base de données, implémentation du serveur MCP, développement d’outils
    - **Laboratoires 07-09 : Fonctionnalités avancées** - Intégration de recherche sémantique, tests & débogage, intégration VS Code
    - **Laboratoires 10-12 : Production & meilleures pratiques** - Stratégies de déploiement, surveillance & observabilité, meilleures pratiques & optimisation
  - **Technologies d’entreprise** : Framework FastMCP, PostgreSQL avec pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Fonctionnalités avancées** : Sécurité au niveau des lignes (RLS), recherche sémantique, accès multi-tenant aux données, embeddings vectoriels, surveillance en temps réel

#### Standardisation de la terminologie - Conversion de module en laboratoire
- **Mise à jour complète de la documentation** : Mise à jour systématique de tous les fichiers README dans 11-MCPServerHandsOnLabs pour utiliser la terminologie « laboratoire » au lieu de « module »
  - **En-têtes de section** : Mise à jour de « Ce que couvre ce module » en « Ce que couvre ce laboratoire » dans les 13 laboratoires
  - **Description du contenu** : Changement de « Ce module fournit... » en « Ce laboratoire fournit... » dans toute la documentation
  - **Objectifs d’apprentissage** : Mise à jour de « À la fin de ce module... » en « À la fin de ce laboratoire... »
  - **Liens de navigation** : Conversion de toutes les références « Module XX : » en « Laboratoire XX : » dans les références croisées et la navigation
  - **Suivi de progression** : Mise à jour de « Après avoir terminé ce module... » en « Après avoir terminé ce laboratoire... »
  - **Références techniques préservées** : Maintien des références aux modules Python dans les fichiers de configuration (ex. : `"module": "mcp_server.main"`)

#### Amélioration du guide d’étude (study_guide.md)
- **Carte visuelle du programme** : Ajout de la nouvelle section « 11. Laboratoires d’intégration de base de données » avec visualisation complète de la structure des laboratoires
- **Structure du dépôt** : Mise à jour de dix à onze sections principales avec description détaillée de 11-MCPServerHandsOnLabs
- **Orientation du parcours d’apprentissage** : Instructions de navigation améliorées couvrant les sections 00-11
- **Couverture technologique** : Ajout des détails sur FastMCP, PostgreSQL, intégration des services Azure
- **Résultats d’apprentissage** : Mise en avant du développement de serveurs prêts pour la production, des modèles d’intégration de base de données et de la sécurité d’entreprise

#### Amélioration de la structure du README principal
- **Terminologie basée sur les laboratoires** : Mise à jour du README.md principal dans 11-MCPServerHandsOnLabs pour utiliser systématiquement la structure « laboratoire »
- **Organisation du parcours d’apprentissage** : Progression claire des concepts fondamentaux à l’implémentation avancée jusqu’au déploiement en production
- **Focus sur le réel** : Accent sur l’apprentissage pratique avec des modèles et technologies de niveau entreprise

### Améliorations de la qualité et de la cohérence de la documentation
- **Accent sur l’apprentissage pratique** : Renforcement de l’approche basée sur les laboratoires dans toute la documentation
- **Focus sur les modèles d’entreprise** : Mise en avant des implémentations prêtes pour la production et des considérations de sécurité d’entreprise
- **Intégration technologique** : Couverture complète des services Azure modernes et des modèles d’intégration IA
- **Progression d’apprentissage** : Parcours clair et structuré des concepts de base au déploiement en production

## 26 septembre 2025

### Amélioration des études de cas - Intégration du registre MCP GitHub

#### Études de cas (09-CaseStudy/) - Focus sur le développement de l’écosystème
- **README.md** : Expansion majeure avec étude de cas complète sur le registre MCP GitHub
  - **Étude de cas registre MCP GitHub** : Nouvelle étude de cas complète examinant le lancement du registre MCP GitHub en septembre 2025
    - **Analyse du problème** : Examen détaillé des défis liés à la découverte et au déploiement fragmentés des serveurs MCP
    - **Architecture de la solution** : Approche centralisée du registre GitHub avec installation en un clic dans VS Code
    - **Impact commercial** : Améliorations mesurables de l’intégration et de la productivité des développeurs
    - **Valeur stratégique** : Focus sur le déploiement modulaire des agents et l’interopérabilité entre outils
    - **Développement de l’écosystème** : Positionnement comme plateforme fondamentale pour l’intégration agentique
  - **Structure améliorée des études de cas** : Mise à jour des sept études de cas avec formatage cohérent et descriptions complètes
    - Agents de voyage Azure AI : Accent sur l’orchestration multi-agent
    - Intégration Azure DevOps : Focus sur l’automatisation des workflows
    - Récupération documentaire en temps réel : Implémentation client console Python
    - Générateur de plan d’étude interactif : Application web conversationnelle Chainlit
    - Documentation dans l’éditeur : Intégration VS Code et GitHub Copilot
    - Azure API Management : Modèles d’intégration API d’entreprise
    - Registre MCP GitHub : Développement de l’écosystème et plateforme communautaire
  - **Conclusion complète** : Réécriture de la section conclusion mettant en lumière sept études de cas couvrant plusieurs dimensions d’implémentation MCP
    - Intégration d’entreprise, orchestration multi-agent, productivité des développeurs
    - Développement de l’écosystème, applications éducatives
    - Aperçus approfondis des modèles architecturaux, stratégies d’implémentation et meilleures pratiques
    - Accent sur MCP comme protocole mature et prêt pour la production

#### Mises à jour du guide d’étude (study_guide.md)
- **Carte visuelle du programme** : Mise à jour du mindmap pour inclure le registre MCP GitHub dans la section Études de cas
- **Description des études de cas** : Amélioration des descriptions génériques vers une répartition détaillée des sept études de cas complètes
- **Structure du dépôt** : Mise à jour de la section 10 pour refléter la couverture complète des études de cas avec détails spécifiques d’implémentation
- **Intégration du journal des modifications** : Ajout de l’entrée du 26 septembre 2025 documentant l’ajout du registre MCP GitHub et les améliorations des études de cas
- **Mise à jour des dates** : Mise à jour de l’horodatage du pied de page pour refléter la dernière révision (26 septembre 2025)

### Améliorations de la qualité de la documentation
- **Amélioration de la cohérence** : Standardisation du formatage et de la structure des études de cas sur les sept exemples
- **Couverture complète** : Études de cas couvrant désormais les scénarios d’entreprise, de productivité des développeurs et de développement d’écosystème
- **Positionnement stratégique** : Accent renforcé sur MCP comme plateforme fondamentale pour le déploiement de systèmes agentiques
- **Intégration des ressources** : Mise à jour des ressources supplémentaires pour inclure le lien vers le registre MCP GitHub

## 15 septembre 2025

### Extension des sujets avancés - Transports personnalisés & ingénierie du contexte

#### Transports personnalisés MCP (05-AdvancedTopics/mcp-transport/) - Nouveau guide d’implémentation avancée
- **README.md** : Guide complet d’implémentation des mécanismes de transport MCP personnalisés
  - **Transport Azure Event Grid** : Implémentation complète de transport événementiel serverless
    - Exemples en C#, TypeScript et Python avec intégration Azure Functions
    - Modèles d’architecture événementielle pour solutions MCP évolutives
    - Récepteurs webhook et gestion des messages push
  - **Transport Azure Event Hubs** : Implémentation de transport streaming à haut débit
    - Capacités de streaming en temps réel pour scénarios à faible latence
    - Stratégies de partitionnement et gestion des points de contrôle
    - Regroupement de messages et optimisation des performances
  - **Modèles d’intégration d’entreprise** : Exemples architecturaux prêts pour la production
    - Traitement MCP distribué sur plusieurs Azure Functions
    - Architectures hybrides combinant plusieurs types de transport
    - Durabilité des messages, fiabilité et stratégies de gestion des erreurs
  - **Sécurité & surveillance** : Intégration Azure Key Vault et modèles d’observabilité
    - Authentification par identité gérée et accès au moindre privilège
    - Télémétrie Application Insights et surveillance des performances
    - Disjoncteurs et modèles de tolérance aux pannes
  - **Cadres de test** : Stratégies complètes de test pour transports personnalisés
    - Tests unitaires avec doubles de test et frameworks de moquage
    - Tests d’intégration avec Azure Test Containers
    - Considérations sur les tests de performance et de charge

#### Ingénierie du contexte (05-AdvancedTopics/mcp-contextengineering/) - Discipline émergente en IA
- **README.md** : Exploration complète de l’ingénierie du contexte comme domaine émergent
  - **Principes fondamentaux** : Partage complet du contexte, conscience des décisions d’action, gestion de la fenêtre de contexte
  - **Alignement avec le protocole MCP** : Comment la conception MCP répond aux défis de l’ingénierie du contexte
    - Limitations de la fenêtre de contexte et stratégies de chargement progressif
    - Détermination de la pertinence et récupération dynamique du contexte
    - Gestion multimodale du contexte et considérations de sécurité
  - **Approches d’implémentation** : Architectures mono-thread vs multi-agent
    - Fragmentation et priorisation du contexte
    - Chargement progressif du contexte et stratégies de compression
    - Approches en couches du contexte et optimisation de la récupération
  - **Cadre de mesure** : Métriques émergentes pour l’évaluation de l’efficacité du contexte
    - Efficacité des entrées, performances, qualité et expérience utilisateur
    - Approches expérimentales pour l’optimisation du contexte
    - Analyse des échecs et méthodologies d’amélioration

#### Mises à jour de la navigation du programme (README.md)
- **Structure de module améliorée** : Mise à jour du tableau du programme pour inclure les nouveaux sujets avancés
  - Ajout des entrées Ingénierie du contexte (5.14) et Transport personnalisé (5.15)
  - Formatage cohérent et liens de navigation dans tous les modules
  - Descriptions mises à jour pour refléter la portée actuelle du contenu

### Améliorations de la structure des dossiers
- **Standardisation des noms** : Renommage de « mcp transport » en « mcp-transport » pour cohérence avec les autres dossiers de sujets avancés
- **Organisation du contenu** : Tous les dossiers 05-AdvancedTopics suivent désormais un schéma de nommage cohérent (mcp-[topic])

### Améliorations de la qualité de la documentation
- **Alignement avec la spécification MCP** : Tous les nouveaux contenus référencent la spécification MCP 2025-06-18 actuelle
- **Exemples multilingues** : Exemples de code complets en C#, TypeScript et Python
- **Focus entreprise** : Modèles prêts pour la production et intégration cloud Azure tout au long
- **Documentation visuelle** : Diagrammes Mermaid pour visualisation de l’architecture et des flux

## 18 août 2025

### Mise à jour complète de la documentation - Normes MCP 2025-06-18

#### Meilleures pratiques de sécurité MCP (02-Security/) - Modernisation complète
- **MCP-SECURITY-BEST-PRACTICES-2025.md** : Réécriture complète alignée avec la spécification MCP 2025-06-18
  - **Exigences Obligatoires** : Ajout des exigences explicites DOIT/NE DOIT PAS issues de la spécification officielle avec des indicateurs visuels clairs  
  - **12 Pratiques de Sécurité Clés** : Restructuration de la liste de 15 éléments en domaines de sécurité complets  
    - Sécurité des Jetons & Authentification avec intégration de fournisseur d'identité externe  
    - Gestion des Sessions & Sécurité du Transport avec exigences cryptographiques  
    - Protection Contre les Menaces Spécifiques à l'IA avec intégration de Microsoft Prompt Shields  
    - Contrôle d'Accès & Permissions avec principe du moindre privilège  
    - Sécurité & Surveillance du Contenu avec intégration Azure Content Safety  
    - Sécurité de la Chaîne d'Approvisionnement avec vérification complète des composants  
    - Sécurité OAuth & Prévention des Confused Deputy avec implémentation PKCE  
    - Réponse aux Incidents & Récupération avec capacités automatisées  
    - Conformité & Gouvernance avec alignement réglementaire  
    - Contrôles de Sécurité Avancés avec architecture zero trust  
    - Intégration de l'Écosystème de Sécurité Microsoft avec solutions complètes  
    - Évolution Continue de la Sécurité avec pratiques adaptatives  
  - **Solutions de Sécurité Microsoft** : Guide d'intégration amélioré pour Prompt Shields, Azure Content Safety, Entra ID et GitHub Advanced Security  
  - **Ressources d'Implémentation** : Liens de ressources complets catégorisés par Documentation Officielle MCP, Solutions de Sécurité Microsoft, Normes de Sécurité et Guides d'Implémentation  

#### Contrôles de Sécurité Avancés (02-Security/) - Implémentation Entreprise  
- **MCP-SECURITY-CONTROLS-2025.md** : Refonte complète avec cadre de sécurité de niveau entreprise  
  - **9 Domaines de Sécurité Complets** : Extension des contrôles basiques vers un cadre détaillé pour entreprise  
    - Authentification & Autorisation Avancées avec intégration Microsoft Entra ID  
    - Sécurité des Jetons & Contrôles Anti-Passthrough avec validation complète  
    - Contrôles de Sécurité des Sessions avec prévention du détournement  
    - Contrôles de Sécurité Spécifiques à l'IA avec prévention des injections de prompt et empoisonnement d'outils  
    - Prévention des Attaques Confused Deputy avec sécurité proxy OAuth  
    - Sécurité d'Exécution des Outils avec sandboxing et isolation  
    - Contrôles de Sécurité de la Chaîne d'Approvisionnement avec vérification des dépendances  
    - Contrôles de Surveillance & Détection avec intégration SIEM  
    - Réponse aux Incidents & Récupération avec capacités automatisées  
  - **Exemples d'Implémentation** : Ajout de blocs de configuration YAML détaillés et exemples de code  
  - **Intégration des Solutions Microsoft** : Couverture complète des services de sécurité Azure, GitHub Advanced Security et gestion d'identité entreprise  

#### Sécurité des Sujets Avancés (05-AdvancedTopics/mcp-security/) - Implémentation Prête pour la Production  
- **README.md** : Réécriture complète pour implémentation de sécurité entreprise  
  - **Alignement sur la Spécification Actuelle** : Mise à jour vers la Spécification MCP 2025-06-18 avec exigences de sécurité obligatoires  
  - **Authentification Améliorée** : Intégration Microsoft Entra ID avec exemples complets en .NET et Java Spring Security  
  - **Intégration Sécurité IA** : Implémentation Microsoft Prompt Shields et Azure Content Safety avec exemples Python détaillés  
  - **Atténuation Avancée des Menaces** : Exemples complets d'implémentation pour  
    - Prévention des Attaques Confused Deputy avec PKCE et validation du consentement utilisateur  
    - Prévention du Passthrough de Jetons avec validation d'audience et gestion sécurisée des jetons  
    - Prévention du Détournement de Session avec liaison cryptographique et analyse comportementale  
  - **Intégration Sécurité Entreprise** : Surveillance Azure Application Insights, pipelines de détection des menaces et sécurité de la chaîne d'approvisionnement  
  - **Checklist d'Implémentation** : Contrôles de sécurité obligatoires vs recommandés clairement identifiés avec bénéfices de l'écosystème de sécurité Microsoft  

### Qualité de la Documentation & Alignement aux Normes  
- **Références de Spécification** : Mise à jour de toutes les références vers la Spécification MCP 2025-06-18 actuelle  
- **Écosystème de Sécurité Microsoft** : Guide d'intégration amélioré dans toute la documentation de sécurité  
- **Implémentation Pratique** : Ajout d'exemples de code détaillés en .NET, Java et Python avec modèles entreprise  
- **Organisation des Ressources** : Catégorisation complète des documents officiels, normes de sécurité et guides d'implémentation  
- **Indicateurs Visuels** : Marquage clair des exigences obligatoires vs pratiques recommandées  

#### Concepts de Base (01-CoreConcepts/) - Modernisation Complète  
- **Mise à Jour de la Version du Protocole** : Référence à la Spécification MCP 2025-06-18 avec versionnement basé sur la date (format AAAA-MM-JJ)  
- **Affinement de l'Architecture** : Descriptions améliorées des Hôtes, Clients et Serveurs pour refléter les modèles d'architecture MCP actuels  
  - Hôtes désormais clairement définis comme applications IA coordonnant plusieurs connexions clients MCP  
  - Clients décrits comme connecteurs de protocole maintenant des relations un-à-un avec les serveurs  
  - Serveurs améliorés avec scénarios de déploiement local vs distant  
- **Restructuration des Primitives** : Refonte complète des primitives serveur et client  
  - Primitives Serveur : Ressources (sources de données), Prompts (modèles), Outils (fonctions exécutables) avec explications et exemples détaillés  
  - Primitives Client : Échantillonnage (complétions LLM), Sollicitation (entrée utilisateur), Journalisation (debug/surveillance)  
  - Mise à jour avec les modèles actuels de méthodes discovery (`*/list`), récupération (`*/get`) et exécution (`*/call`)  
- **Architecture du Protocole** : Introduction d'un modèle d'architecture à deux couches  
  - Couche Données : Fondation JSON-RPC 2.0 avec gestion du cycle de vie et primitives  
  - Couche Transport : STDIO (local) et HTTP Streamable avec SSE (transport distant)  
- **Cadre de Sécurité** : Principes de sécurité complets incluant consentement explicite utilisateur, protection de la vie privée des données, sécurité d'exécution des outils et sécurité de la couche transport  
- **Schémas de Communication** : Messages du protocole mis à jour pour montrer initialisation, découverte, exécution et flux de notification  
- **Exemples de Code** : Actualisation des exemples multilingues (.NET, Java, Python, JavaScript) pour refléter les modèles SDK MCP actuels  

#### Sécurité (02-Security/) - Refonte Complète de la Sécurité  
- **Alignement aux Normes** : Alignement total avec les exigences de sécurité de la Spécification MCP 2025-06-18  
- **Évolution de l'Authentification** : Documentation de l'évolution des serveurs OAuth personnalisés vers la délégation fournisseur d'identité externe (Microsoft Entra ID)  
- **Analyse des Menaces Spécifiques à l'IA** : Couverture améliorée des vecteurs d'attaque IA modernes  
  - Scénarios détaillés d'attaques par injection de prompt avec exemples concrets  
  - Mécanismes d'empoisonnement d'outils et schémas d'attaque "rug pull"  
  - Empoisonnement de la fenêtre de contexte et attaques de confusion de modèle  
- **Solutions de Sécurité IA Microsoft** : Couverture complète de l'écosystème de sécurité Microsoft  
  - AI Prompt Shields avec détection avancée, mise en lumière et techniques de délimitation  
  - Modèles d'intégration Azure Content Safety  
  - GitHub Advanced Security pour protection de la chaîne d'approvisionnement  
- **Atténuation Avancée des Menaces** : Contrôles de sécurité détaillés pour  
  - Détournement de session avec scénarios d'attaque spécifiques MCP et exigences cryptographiques d'ID de session  
  - Problèmes de confused deputy dans les scénarios proxy MCP avec exigences explicites de consentement  
  - Vulnérabilités de passthrough de jetons avec contrôles de validation obligatoires  
- **Sécurité de la Chaîne d'Approvisionnement** : Extension de la couverture de la chaîne d'approvisionnement IA incluant modèles de base, services d'embeddings, fournisseurs de contexte et API tierces  
- **Sécurité Fondamentale** : Intégration améliorée avec les modèles de sécurité entreprise incluant architecture zero trust et écosystème de sécurité Microsoft  
- **Organisation des Ressources** : Liens de ressources complets catégorisés par type (Docs Officiels, Normes, Recherche, Solutions Microsoft, Guides d'Implémentation)  

### Améliorations de la Qualité de la Documentation  
- **Objectifs d'Apprentissage Structurés** : Objectifs d'apprentissage améliorés avec résultats spécifiques et actionnables  
- **Références Croisées** : Ajout de liens entre sujets de sécurité et concepts de base liés  
- **Informations à Jour** : Mise à jour de toutes les références de date et liens de spécification vers les normes actuelles  
- **Guides d'Implémentation** : Ajout de directives d'implémentation spécifiques et actionnables dans les deux sections  

## 16 juillet 2025  

### Améliorations du README et de la Navigation  
- Refonte complète de la navigation du curriculum dans README.md  
- Remplacement des balises `<details>` par un format plus accessible basé sur des tableaux  
- Création d'options de mise en page alternatives dans le nouveau dossier "alternative_layouts"  
- Ajout d'exemples de navigation par cartes, onglets et accordéon  
- Mise à jour de la section structure du dépôt pour inclure tous les fichiers récents  
- Amélioration de la section "Comment utiliser ce curriculum" avec recommandations claires  
- Mise à jour des liens de spécification MCP vers les URL correctes  
- Ajout de la section Ingénierie du Contexte (5.14) à la structure du curriculum  

### Mises à Jour du Guide d'Étude  
- Révision complète du guide d'étude pour alignement avec la structure actuelle du dépôt  
- Ajout de nouvelles sections pour MCP Clients et Outils, et Serveurs MCP Populaires  
- Mise à jour de la Carte Visuelle du Curriculum pour refléter précisément tous les sujets  
- Amélioration des descriptions des Sujets Avancés pour couvrir toutes les zones spécialisées  
- Mise à jour de la section Études de Cas pour refléter des exemples réels  
- Ajout de ce journal des modifications complet  

### Contributions Communautaires (06-CommunityContributions/)  
- Ajout d'informations détaillées sur les serveurs MCP pour génération d'images  
- Ajout d'une section complète sur l'utilisation de Claude dans VSCode  
- Ajout des instructions d'installation et d'utilisation du client terminal Cline  
- Mise à jour de la section client MCP pour inclure toutes les options populaires  
- Amélioration des exemples de contribution avec des échantillons de code plus précis  

### Sujets Avancés (05-AdvancedTopics/)  
- Organisation de tous les dossiers de sujets spécialisés avec une nomenclature cohérente  
- Ajout de matériaux et exemples d'ingénierie du contexte  
- Ajout de la documentation d'intégration de l'agent Foundry  
- Amélioration de la documentation d'intégration de sécurité Entra ID  

## 11 juin 2025  

### Création Initiale  
- Publication de la première version du curriculum MCP pour débutants  
- Création de la structure de base pour les 10 sections principales  
- Implémentation de la Carte Visuelle du Curriculum pour la navigation  
- Ajout de projets exemples initiaux en plusieurs langages de programmation  

### Premiers Pas (03-GettingStarted/)  
- Création des premiers exemples d'implémentation serveur  
- Ajout de guides de développement client  
- Inclusion des instructions d'intégration client LLM  
- Ajout de la documentation d'intégration VS Code  
- Implémentation d'exemples de serveurs Server-Sent Events (SSE)  

### Concepts de Base (01-CoreConcepts/)  
- Ajout d'explications détaillées sur l'architecture client-serveur  
- Création de la documentation sur les composants clés du protocole  
- Documentation des schémas de messagerie dans MCP  

## 23 mai 2025  

### Structure du Dépôt  
- Initialisation du dépôt avec structure de dossiers basique  
- Création des fichiers README pour chaque section majeure  
- Mise en place de l'infrastructure de traduction  
- Ajout des ressources images et diagrammes  

### Documentation  
- Création du README.md initial avec aperçu du curriculum  
- Ajout des fichiers CODE_OF_CONDUCT.md et SECURITY.md  
- Mise en place du SUPPORT.md avec guide d'aide  
- Création de la structure préliminaire du guide d'étude  

## 15 avril 2025  

### Planification et Cadre  
- Planification initiale du curriculum MCP pour débutants  
- Définition des objectifs d'apprentissage et du public cible  
- Esquisse de la structure en 10 sections du curriculum  
- Développement du cadre conceptuel pour exemples et études de cas  
- Création des prototypes initiaux d'exemples pour concepts clés  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->