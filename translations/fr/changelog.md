# Journal des modifications : Programme MCP pour débutants

Ce document sert de registre de tous les changements significatifs apportés au programme Model Context Protocol (MCP) pour débutants. Les changements sont documentés par ordre chronologique inverse (les plus récents en premier).

## 29 juillet 2026

### Nouveau module compagnon 08 : Sidecars de fiabilité et réessais sécurisés

Ajout d'une leçon compagnon indépendante du fournisseur pour les outils MCP qui créent des effets concrets,
alignée avec la spécification finale `2026-07-28`.

- **Nouveau** : La [leçon compagnon sidecar de fiabilité][reliability-sidecar]
  utilise une histoire de ticket de support, deux diagrammes Mermaid et un
  flux de décision de réessai pour expliquer les clés de fonctionnement stable,
  l'admission atomique des doublons, la réconciliation, les preuves, et la limite
  de l'extension Tasks.
- **Nouveau** : Un exercice d'injection de pannes en Python et SQLite utilisant la bibliothèque standard
  utilise des magasins séparés d'opérations et de tickets pour démontrer une réponse perdue
  après la validation d'un effet externe. Six tests déterministes couvrent la
  duplication naïve, la récupération redémarrage protégée, les conflits de charge utile,
  les résultats mis en cache, les réclamations actives, et l'admission concurrente de doublons.
- **Mis à jour** : Le module 08 lie désormais la leçon compagnon, identifie le
  modèle final de requête sans état `2026-07-28`, distingue l'observabilité OpenTelemetry
  de la fonctionnalité MCP de journalisation dépréciée, et limite son exemple
  générique de réessai aux opérations en lecture seule.
- **Optionnel** : La leçon mappe ses concepts portables à une mise en œuvre communautaire taguée sans faire du service hébergé ou d'un appel réseau une partie
  de l'exercice.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 juillet 2026

### Nouvelle leçon : Candidat à la version finale de la spécification MCP 2026-07-28

Ajout de la couverture du candidat à la version finale de la spécification MCP `2026-07-28` (annoncée le 21 mai 2026 ; sortie finale prévue le 28 juillet 2026), résumé à partir du [billet officiel d'annonce sur le blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). La base du programme reste **Spécification MCP 2025-11-25** jusqu'à ce que la nouvelle version soit disponible, ainsi ceci est présenté comme une orientation prospective plutôt qu'une réécriture des leçons existantes.

- **Nouveau** : [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — une leçon complète couvrant le noyau de protocole sans état (suppression de la poignée de main `initialize` et de `Mcp-Session-Id`), les nouveaux en-têtes de routage `Mcp-Method`/`Mcp-Name`, les métadonnées de cache `ttlMs`/`cacheScope`, le contexte de trace W3C dans `_meta`, le cadre formel des Extensions (applications MCP et la nouvelle extension Tasks), six SEP de durcissement de l'autorisation, la dépréciation de Roots/Sampling/Logging, et la transition vers le JSON Schema 2020-12 complet pour les schémas d'outils.
- **Mis à jour** avec des renvois prospectifs vers la nouvelle leçon :
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md) : note sur la version du protocole, sections Sampling/Roots/Logging/Tasks, et "Ce qui suit"
  - [02-Security/README.md](./02-Security/README.md) : renvoi au durcissement de l'autorisation
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md) : renvoi au transport sans état
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md) : renvoi à la dépréciation du Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md) : renvoi à la dépréciation du Logging et à l'extension Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md) : renvoi au routage sans état/session
  - [README.md](./README.md) : note "Regard vers l'avenir" dans la section spécification et une nouvelle entrée `1.1` dans le tableau des modules du programme
  - [study_guide.md](./study_guide.md) : point prospectif sous l'aperçu des Concepts de base et une note d'addendum datée
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md) : renvoi à la carte de transport `mcp-session-id` avant le modèle de requête sans état
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md) : renvoi de présentation du module sur la dépréciation des Contextes racines/Sampling et l'extension Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md) : renvoi au durcissement de l'autorisation

## 24 juin 2026

### Nouvelle leçon : Utilisation de MCP dans l'application Copilot

- [Section Outils](./12-tooling/README.md) Ajout d'une section outils.
- [MCP dans l’application Copilot](./12-tooling/01-copilot-app/README.md)

## 16 juin 2026

### Alignement de la spécification MCP & validation des exemples

Validation du programme par rapport à la **Spécification MCP 2025-11-25** en vigueur et aux derniers SDK officiels, correction des références obsolètes restantes vers la spécification et confirmation que les exemples principaux se compilent et s'exécutent toujours.

#### Corrections de version de spécification (2025-06-18 / 2025-03-26 → 2025-11-25)

Mise à jour du contenu anglophone là où il affirmait encore qu'une révision plus ancienne de la spécification était la norme *actuelle/plus récente*, et redirection des liens vers les chemins canoniques de la spécification `modelcontextprotocol.io` :
- **05-AdvancedTopics/mcp-security/README.md** : mise à jour de la bannière "Norme actuelle", de l’introduction, du titre des principes fondamentaux de sécurité, du titre des exigences obligatoires, section Microsoft Entra ID, liens Références & Ressources, et avis de sécurité final (8 références) vers 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md** : mise à jour du lien des ressources supplémentaires vers la spécification et de la bannière "Norme actuelle" vers 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md** : remplacement du lien obsolète `2025-03-26` sur la sécurité et la confiance par la page actuelle de bonnes pratiques de sécurité 2025-11-25
- **03-GettingStarted/14-sampling/README.md** : mise à jour du lien officiel vers la documentation du sampling vers 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md** : Mise à jour de la référence au "MCP Specification" au présent et du lien vers la spécification Ressources supplémentaires vers 2025-11-25 (notes historiques SSE-deprecation laissées intactes pour précision)

#### Validation des exemples avec les SDK actuels

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)** : `npm install` a résolu `@modelcontextprotocol/sdk@1.29.0` ; `tsc --noEmit` passé sans erreurs de type — les APIs existantes `McpServer`/`StdioServerTransport` restent valides
- **Python (03-GettingStarted/01-first-server/solution/python)** : Validé dans un `.venv` isolé avec `mcp[cli]` (1.27.2) ; `py_compile` réussi et `FastMCP.list_tools()` a correctement renvoyé les outils `add` et `subtract`
- Confirmé que toutes les plages de version d’exemple de `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) résolvent proprement vers la version actuelle `1.29.0` sans rupture d’API

#### Alignement des versions des dépendances (fermeture des écarts)

A augmenté les versions obsolètes des SDK pour que chaque exemple suive la version actuelle de MCP, conformément à la convention globale du dépôt :
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json** : Montée de version de `@modelcontextprotocol/sdk` de `^1.8.0` à `>=1.26.0` et mise à jour de la description de paquet obsolète `"updated for MCP 2025-06-18"` en `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** et **lab4/code/github_mcp_server/pyproject.toml** : Montée de version exacte `mcp==1.23.0` à `mcp>=1.26.0` ; régénération des deux fichiers `uv.lock` (`uv lock`) pour que les lockfiles résolvent la version actuelle `mcp 1.27.2` et restent synchronisés avec les manifests

#### Analyse des lacunes du cursus — Couverture fonctionnelle des dernières spécifications

Vérifié que le cursus couvre déjà tous les éléments primitifs introduits/étendus dans MCP 2025-11-25, aucun contenu manquant n’est présent :
- **Échantillonnage** : Leçon 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Élicitation (y compris mode URL)** : Documenté dans 01-CoreConcepts et 05-AdvancedTopics/mcp-protocol-features
- **Roots** : Documenté dans 00-Introduction, 01-CoreConcepts, et 05-AdvancedTopics/mcp-root-contexts
- **Tâches (expérimentales, opérations longues)** : Documenté dans 01-CoreConcepts et 05-AdvancedTopics/mcp-protocol-features
- **Annotations d’outil** (`readOnlyHint` / `destructiveHint`) : Documenté dans 01-CoreConcepts et 05-AdvancedTopics/mcp-protocol-features

### Renforcement de la sécurité & correction des vulnérabilités des dépendances

Passage complet en revue de la sécurité sur tous les manifests de dépendances et le code exemple, puis correction de tous les avis npm signalés et d’une découverte au niveau du code. Après correction, `npm audit` signale **0 vulnérabilités** dans chaque répertoire audité.

#### Vulnérabilités des dépendances npm (transitives) — Corrigées

Audité tous les 15 fichiers `package-lock.json` commités. Les vulnérabilités étaient limitées aux dépendances transitives ajoutées par l’outil développeur MCP Inspector, le client OpenAI et le SDK MCP ; toutes sont maintenant résolues sans casser les exemples :
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** et **lab3/code/weather_mcp/inspector** : Montée de version de `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), ce qui a levé les avis liés à `ajv`, `brace-expansion`, `diff`, `path-to-regexp` et `ws` intégrés. Ajout d’une entrée npm `overrides` forçant la version corrigée `shell-quote@1.8.4` pour éliminer l’avis critique restant porté par `concurrently` ; régénération des deux lockfiles (maintenant 0 vulnérabilités)
- **03-GettingStarted/samples/typescript** : `npm audit fix` a mis à jour le transitive `qs` (modéré) vers une version corrigée
- **03-GettingStarted/samples/javascript** : `npm audit fix` a mis à jour le transitive `hono` (modéré) vers une version corrigée
- **03-GettingStarted/03-llm-client/solution/typescript** : `npm audit fix` a mis à jour le transitive `form-data` (élevé) vers une version corrigée
- **03-GettingStarted/11-simple-auth/solution/typescript** : Génération du `package-lock.json` manquant pour garantir que le projet est reproductible et auditable (0 vulnérabilités)

#### Correction de sécurité au niveau du code (OWASP A03 : Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py** : Suppression de `shell=True` de l’outil `open_in_vscode`. L’appel précédent `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` permettait l’interprétation par `cmd.exe` de métacaractères shell dans un chemin de dossier (vecteur d’injection de commande). Il lance désormais directement le binaire résolu `Code.exe` avec le dossier en argument — sans shell — ce qui est fonctionnellement équivalent et sûr

#### Audit des dépendances Python

- Audit de chaque ensemble de requirements Python avec `pip-audit`. `05-AdvancedTopics` et `03-GettingStarted/samples/python` n’ont signalé **aucune vulnérabilité connue** (leurs plages `mcp` / `httpx` / `pydantic` / `python-dotenv` résolvent vers des versions corrigées actuelles)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt** : `pip-audit` a pointé la dépendance transitive **`werkzeug` 3.1.1** avec trois avis de déni de service sur Windows liés à `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, et `CVE-2026-27199` (tous corrigés dans 3.1.6). Ajout d’un verrou de sécurité explicite `werkzeug>=3.1.6` pour résoudre la version corrigée ; vérification que la contrainte résout sans problème avec la stack `chainlit` / `mcp` / `semantic-kernel`

### Renommage de produit

Mise à jour de tout le contenu du cursus pour refléter le renommage des produits chez Microsoft :


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md** : Mise à jour du lien de la communauté Discord

- **AGENTS.md**: Référence du serveur Discord mise à jour
- **README.md**: Références de l'écosystème technologique mises à jour
- **study_guide.md**: Références d'étude de cas mises à jour
- **05-AdvancedTopics/README.md**: Titre et description du Module 5.13 mis à jour
- **05-AdvancedTopics/mcp-integration/README.md**: En-tête de section et description mis à jour
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Mise à jour complète du titre et du contenu du module
- **05-AdvancedTopics/mcp-security-entra/README.md**: Lien de référence croisée mis à jour
- **07-LessonsfromEarlyAdoption/README.md**: Références d'étude de cas mises à jour
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: En-tête de la Section 9, badges et capacités mis à jour
- **08-BestPractices/README.md**: Lien de la communauté Discord mis à jour
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Référence du canal Discord mise à jour
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Référence de déploiement de modèle mise à jour
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Tableau des services IA mis à jour
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Références de ressources mises à jour

#### AI Toolkit / AITK → Extension Microsoft Foundry Toolkit pour VS Code
- **README.md**: Références principales du curriculum mises à jour
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Titre du module, vue d'ensemble et tous les en-têtes de module mis à jour
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Titre, objectifs d'apprentissage, instructions d'installation et ressources mis à jour
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Titre, objectifs d'apprentissage, tableau des hôtes MCP et références croisées mis à jour
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Titre, badges, prérequis et ressources mis à jour
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Références Agent Builder et lien de retour d'expérience mis à jour
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Prérequis et références d'extension mis à jour

---

## 11 avril 2026

### Nouvelle leçon, corrections de documentation et mises à jour des dépendances

#### Contenu du curriculum ajouté

**Module 05 - Sujets avancés**
- **Leçon 5.17 : Raisonnement multi-agent adversarial avec MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`) : Nouveau guide complet couvrant le modèle de débat adversarial pour les systèmes multi-agents
  - Diagramme d'architecture Mermaid : deux agents → serveur MCP partagé → transcription du débat → juge → verdict
  - Serveur d'outil MCP partagé (`web_search` + `run_python`) implémenté en Python et TypeScript
  - Invites système opposées (POUR / CONTRE / Juge) avec exigences explicites d'utilisation d'outils
  - Orchestrateur de débat en Python, TypeScript et C# gérant les tours et le routage des arguments
  - Câblage MCP `ClientSession` pour l’orchestrateur vers de véritables appels d’outils
  - Tableau de cas d'usage (détection d'hallucinations, modélisation des menaces, revue de conception API, vérification factuelle, sélection technologique)
  - Considérations de sécurité : exécution sandboxée, validation des appels d’outils, limitation du débit, journalisation d’audit
  - Exercice structuré avec trois scénarios pratiques (revue de code, décision d'architecture, modération de contenu)

#### Corrections de documentation

**Module 03 - Premiers pas**
- **05-stdio-server/README.md** : Exemple incomplet de serveur stdio TypeScript corrigé — ajout de l’instanciation du transport manquante (`new StdioServerTransport()`) et appel `server.connect(transport)` pour correspondre aux exemples Python et .NET dans la même section
- **14-sampling/README.md** : Correction de faute de frappe — corrigé `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Mises à jour du curriculum

**README.md principal**
- Ajout de l’entrée 5.17 (Raisonnement multi-agent adversarial avec MCP) dans le tableau du curriculum avec lien direct vers la nouvelle leçon

**05-AdvancedTopics/README.md**
- Ajout de la ligne Leçon 5.17 dans le tableau des leçons

**study_guide.md**
- Ajout du sujet Raisonnement multi-agent adversarial dans la carte mentale et la description en prose des Sujets avancés

#### Corrections de code et sécurité

**Module 05 - Agents adversariaux (`mcp-adversarial-agents`)**
- **Correction de sécurité — injection de commande** : Remplacement de l’interpolation shell `execSync` par `execFile` + `promisify` dans l’outil TypeScript `run_python`, éliminant la surface d’injection de commande (le code contrôlé par le LLM est désormais passé comme un argument argv littéral sans intervention du shell)
- **Câblage de la boucle d’outil MCP** : Mise à jour de l’orchestrateur de débat Python pour utiliser le client `AsyncAnthropic` (remplaçant le `Anthropic` synchronisé bloquant), passer une `ClientSession` active directement à chaque tour d’agent, récupérer les définitions des outils via `session.list_tools()` à chaque tour, et dispatcher les blocs `tool_use` via `session.call_tool()` en boucle jusqu’à ce que le modèle produise une réponse finale textuelle

#### Mises à jour des dépendances

- Augmentation de la version de `hono` à 4.12.12 dans plusieurs packages (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Augmentation de la version de `@hono/node-server` de 1.19.11 à 1.19.13 dans les packages TypeScript
- Augmentation de la version de `cryptography` de 46.0.5 à 46.0.7 dans les packages Python (laboratoires 3 et 4 de 10-StreamliningAIWorkflows)
- Augmentation de la version de `lodash` de 4.17.23 à 4.18.1 dans l’inspecteur 10-StreamliningAIWorkflows

#### Traductions

- Synchronisation des traductions pour plus de 48 langues avec les derniers changements source (mise à jour i18n)

---

## 5 février 2026

### Améliorations globales de validation et de navigation du dépôt

#### Contenu du curriculum ajouté

**Module 03 - Premiers pas**
- **12-mcp-hosts/README.md** : Nouveau guide complet pour configurer les hôtes MCP
  - Exemples de configuration Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Modèles de configuration JSON pour tous les hôtes majeurs
  - Tableau comparatif des types de transport (stdio, SSE/HTTP, WebSocket)
  - Résolution des problèmes de connexion courants
  - Bonnes pratiques de sécurité pour la configuration des hôtes

- **13-mcp-inspector/README.md** : Nouveau guide de débogage pour MCP Inspector
  - Méthodes d’installation (npx, npm global, depuis la source)
  - Connexion aux serveurs via stdio et HTTP/SSE
  - Tests d’outils, ressources et workflows d’invites
  - Intégration VS Code avec MCP Inspector
  - Scénarios courants de débogage avec solutions

**Module 04 - Mise en œuvre pratique**
- **pagination/README.md** : Nouveau guide d’implémentation de la pagination
  - Modèles de pagination basés sur curseur en Python, TypeScript, Java
  - Gestion de la pagination côté client
  - Stratégies de conception du curseur (opaque vs structuré)
  - Recommandations pour l’optimisation des performances

**Module 05 - Sujets avancés**
- **mcp-protocol-features/README.md** : Exploration approfondie des fonctionnalités du protocole
  - Implémentation des notifications de progression
  - Modèles d’annulation de requêtes
  - Modèles de ressources avec patterns URI
  - Gestion du cycle de vie du serveur
  - Contrôle du niveau de journalisation
  - Modèles de gestion d’erreurs avec codes JSON-RPC

#### Corrections de navigation (plus de 24 fichiers mis à jour)

**README principaux des modules**
 Liens désormais vers la première leçon ET vers le module suivant

**Sous-fichiers 02-Security**
- Les 5 documents supplémentaires de sécurité disposent désormais d’une navigation « Que faire ensuite » :

**Fichiers 09-CaseStudy**
- Tous les fichiers d’étude de cas ont désormais une navigation séquentielle :

**Laboratoires 10-StreamliningAI**
Ajout de la section « Que faire ensuite » dans la vue d’ensemble du module 10 et dans le module 11

#### Corrections de code et de contenu

**Mises à jour du SDK et des dépendances**
Correction de la version openai vide à `^4.95.0`
Mise à jour du SDK de `^1.8.0` à `>=1.26.0`
Mise à jour des versions mcp en `>=1.26.0`

**Corrections de code**
Correction du modèle invalide `gpt-4o-mini` en `gpt-4.1-mini`

**Corrections de contenu**
Correction du lien cassé `READMEmd` → `README.md`, correction de l’en-tête du curriculum `Module 1-3` → `Module 0-3`, correction du chemin sensible à la casse
Suppression du contenu dupliqué corrompu de l’étude de cas 5

**Améliorations du guidage débutant**
Ajout d’une introduction appropriée, des objectifs d’apprentissage et des prérequis pour les débutants

#### Mises à jour du curriculum

**README.md principal**
- Ajout des entrées 3.12 (Hôtes MCP), 3.13 (Inspecteur MCP), 4.1 (Pagination), 5.16 (Fonctionnalités du protocole) au tableau du curriculum

**README des modules**
Ajout des leçons 12 et 13 à la liste des leçons
Ajout de la section Guides pratiques avec lien pagination
Ajout des leçons 5.15 (Transport personnalisé) et 5.16 (Fonctionnalités du protocole)

**study_guide.md**
- Mise à jour de la carte mentale avec tous les nouveaux sujets : Configuration des hôtes MCP, Inspecteur MCP, Stratégies de pagination, Exploration des fonctionnalités du protocole

## 28 janvier 2026

### Revue de conformité à la spécification MCP 2025-11-25

#### Amélioration des concepts fondamentaux (01-CoreConcepts/)
- **Nouveau primitif client - Roots** : Ajout d’une documentation complète sur le primitif client Roots, permettant aux serveurs de comprendre les limites du système de fichiers et les permissions d'accès
- **Annotations des outils** : Ajout de la documentation sur les annotations comportementales des outils (`readOnlyHint`, `destructiveHint`) pour de meilleures décisions d’exécution des outils
- **Appel d’outils lors de l’échantillonnage** : Mise à jour de la documentation Sampling pour inclure les paramètres `tools` et `toolChoice` pour l’invocation des outils dirigée par le modèle lors des requêtes d’échantillonnage
- **Élicitation en mode URL** : Ajout de la documentation sur l’élicitation basée sur URL pour les interactions web externes initiées par le serveur
- **Tâches (Expérimental)** : Ajout d’une nouvelle section documentant la fonctionnalité expérimentale Tâches pour les wrappers d’exécution durables et la récupération différée des résultats
- **Support des icônes** : Remarque que les outils, ressources, modèles de ressources et invites peuvent désormais inclure des icônes en tant que métadonnées supplémentaires

#### Mises à jour de documentation
- **README.md** : Ajout de la référence à la spécification MCP 2025-11-25 et explication du versionnage daté
- **study_guide.md** : Mise à jour de la carte du curriculum pour inclure Tâches et Annotations d’outils dans la section Concepts fondamentaux ; mise à jour du timestamp du document

#### Vérification de la conformité à la spécification
- **Version du protocole** : Vérification que toute la documentation fait référence à la spécification MCP 2025-11-25 actuelle
- **Alignement de l’architecture** : Confirmation de la précision de la documentation de l’architecture en deux couches (couche données + couche transport)
- **Documentation des primitifs** : Validation des primitifs serveur (Ressources, Invites, Outils) et primitifs client (Sampling, Élicitation, Journalisation, Roots)
- **Mécanismes de transport** : Vérification de la précision de la documentation des transports STDIO et HTTP Streamable
- **Orientation sécurité** : Confirmation de l’alignement avec les meilleures pratiques de sécurité MCP actuelles

#### Principales fonctionnalités MCP 2025-11-25 documentées
- **Découverte OpenID Connect** : Découverte du serveur d’authentification via OIDC
- **Documents de métadonnées OAuth Client ID** : Mécanisme recommandé d’enregistrement client
- **JSON Schema 2020-12** : Dialecte par défaut pour les définitions de schéma MCP
- **Système de classification SDK** : Formalisation des exigences pour le support et la maintenance des fonctionnalités SDK
- **Structure de gouvernance** : Formalisation des groupes de travail et groupes d’intérêt dans la gouvernance MCP

### Mise à jour majeure de la documentation de sécurité (02-Security/)

#### Intégration du Workshop MCP Security Summit (Sherpa)
- **Nouvelle ressource de formation pratique** : Ajout d’une intégration complète avec le [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) dans toute la documentation de sécurité
- **Couverture du parcours de l’expédition** : Documentation complète de la progression camp à camp du Camp de base au Sommet
- **Alignement OWASP** : Toute orientation sécurité fait désormais référence aux risques du guide de sécurité MCP Azure OWASP

#### Intégration OWASP MCP Top 10
- **Nouvelle section** : Ajout d’un tableau des 10 risques de sécurité OWASP MCP avec les mesures d’atténuation Azure dans le README principal Sécurité
- **Documentation basée sur les risques** : Mise à jour de mcp-security-controls-2025.md avec les références aux risques OWASP MCP pour chaque domaine de sécurité
- **Architecture de référence** : Lien vers l’architecture de référence et les modèles de mise en œuvre du guide de sécurité MCP Azure OWASP

#### Fichiers de sécurité mis à jour
- **README.md** : Ajout de la vue d’ensemble du Workshop Sherpa, tableau du parcours d’expédition, résumé des risques OWASP MCP Top 10, et section formation pratique
- **mcp-security-controls-2025.md** : Header mis à jour à février 2026, ajout des références aux risques OWASP (MCP01-MCP08), correction de l’incohérence de version de la spécification
- **mcp-security-best-practices-2025.md** : Ajout de la section ressources Sherpa et OWASP, mise à jour du timestamp
- **mcp-best-practices.md** : Ajout de la section formation pratique avec liens Sherpa et OWASP
- **azure-content-safety-implementation.md** : Ajout de la référence OWASP MCP06, alignement Camp 3 Sherpa, et section ressources supplémentaires

#### Nouveaux liens de ressources ajoutés
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Pages de risque individuelles OWASP MCP (MCP01-MCP10)

### Alignement de la Spécification MCP à l'échelle du curriculum 2025-11-25

#### Module 03 - Premiers pas
- **Documentation SDK** : Ajout du SDK Go à la liste officielle des SDK ; mise à jour de toutes les références SDK pour correspondre à la Spécification MCP 2025-11-25
- **Clarification du transport** : Mises à jour des descriptions des transports STDIO et HTTP Streaming avec références explicites à la spécification

#### Module 04 - Mise en œuvre pratique
- **Mises à jour du SDK** : Ajout du SDK Go ; mise à jour de la liste SDK avec référence à la version de la spécification
- **Spécification d'autorisation** : Mise à jour du lien de la spécification d'autorisation MCP vers la version actuelle 2025-11-25

#### Module 05 - Sujets avancés
- **Nouvelles fonctionnalités** : Ajout d'une note sur les nouvelles fonctionnalités de la Spécification MCP 2025-11-25 (Tâches, Annotations d'outil, Élicitation du mode URL, Racines)
- **Ressources de sécurité** : Ajout des liens OWASP MCP Top 10 et atelier Sherpa aux références supplémentaires

#### Module 06 - Contributions communautaires
- **Liste SDK** : Ajout des SDK Swift et Rust ; mise à jour du lien de spécification vers 2025-11-25
- **Référence de la spécification** : Mise à jour du lien de la Spécification MCP vers l'URL directe de la spécification

#### Module 07 - Leçons tirées des premières adoptons
- **Mises à jour des ressources** : Ajout du lien vers la Spécification MCP 2025-11-25 et OWASP MCP Top 10 aux ressources supplémentaires

#### Module 08 - Bonnes pratiques
- **Version de spécification** : Mise à jour de la référence de la Spécification MCP vers 2025-11-25
- **Ressources de sécurité** : Ajout de OWASP MCP Top 10 et de l'atelier Sherpa aux références supplémentaires

#### Module 10 - Rationalisation des flux de travail IA
- **Mise à jour du badge** : Changement du badge de version MCP de la version SDK (1.9.3) à la version de la spécification (2025-11-25)
- **Liens de ressources** : Mise à jour du lien de la Spécification MCP ; ajout de OWASP MCP Top 10

#### Module 11 - Laboratoires pratiques MCP Server
- **Référence de spécification** : Mise à jour du lien de la Spécification MCP vers la version 2025-11-25
- **Ressources de sécurité** : Ajout de OWASP MCP Top 10 aux ressources officielles

## 18 décembre 2025

### Mise à jour de la documentation de sécurité - Spécification MCP 2025-11-25

#### Bonnes pratiques de sécurité MCP (02-Security/mcp-best-practices.md) - Mise à jour de la version de la spécification
- **Mise à jour de la version du protocole** : Mise à jour pour référencer la dernière Spécification MCP 2025-11-25 (publiée le 25 novembre 2025)
  - Mise à jour de toutes les références de version de spécification de 2025-06-18 à 2025-11-25
  - Mise à jour des références de dates du document du 18 août 2025 au 18 décembre 2025
  - Vérification que toutes les URL de spécification pointent vers la documentation actuelle
- **Validation du contenu** : Validation complète des meilleures pratiques de sécurité selon les dernières normes
  - **Solutions de sécurité Microsoft** : Vérification de la terminologie et des liens actuels pour Prompt Shields (anciennement "détection du risque de jailbreak"), Azure Content Safety, Microsoft Entra ID et Azure Key Vault
  - **Sécurité OAuth 2.1** : Confirmation de l'alignement avec les meilleures pratiques de sécurité OAuth les plus récentes
  - **Normes OWASP** : Validation que les références OWASP Top 10 pour les LLM restent à jour
  - **Services Azure** : Vérification de tous les liens Microsoft Azure et des meilleures pratiques associées
- **Alignement aux normes** : Confirmation que toutes les normes de sécurité référencées sont actuelles
  - Cadre de gestion des risques IA NIST
  - ISO 27001:2022
  - Meilleures pratiques de sécurité OAuth 2.1
  - Cadres de conformité et sécurité Azure
- **Ressources de mise en œuvre** : Validation de tous les liens de guides et ressources d'implémentation
  - Modèles d'authentification Azure API Management
  - Guides d'intégration Microsoft Entra ID
  - Gestion des secrets Azure Key Vault
  - Pipelines DevSecOps et solutions de surveillance

### Assurance qualité de la documentation
- **Conformité à la spécification** : Garantie que toutes les exigences de sécurité MCP obligatoires (DOIT/NE DOIT PAS) sont alignées sur la spécification la plus récente
- **Actualisation des ressources** : Vérification de tous les liens externes vers la documentation Microsoft, normes de sécurité et guides d'implémentation
- **Couverture des bonnes pratiques** : Confirmation de la couverture complète des sujets d'authentification, d'autorisation, des menaces spécifiques à l'IA, de la sécurité de la chaîne d'approvisionnement et des modèles d'entreprise

## 6 octobre 2025

### Expansion de la section Premiers Pas – Usage avancé du serveur & Authentification simple

#### Usage avancé du serveur (03-GettingStarted/10-advanced)
- **Nouveau chapitre ajouté** : Introduction d'un guide complet sur l'utilisation avancée du serveur MCP, couvrant les architectures serveur régulière et bas niveau.
  - **Serveur régulier vs. bas niveau** : Comparaison détaillée et exemples de code en Python et TypeScript pour les deux approches.
  - **Conception basée sur les handlers** : Explication de la gestion basée sur les gestionnaires d'outils/ressources/prompts pour des implémentations serveur évolutives et flexibles.
  - **Modèles pratiques** : Scénarios réels où les modèles serveur bas niveau sont avantageux pour des fonctionnalités avancées et l'architecture.

#### Authentification simple (03-GettingStarted/11-simple-auth)
- **Nouveau chapitre ajouté** : Guide étape par étape pour implémenter une authentification simple dans les serveurs MCP.
  - **Concepts d'authentification** : Explication claire de l'authentification vs. l'autorisation, et de la gestion des identifiants.
  - **Implémentation Auth de base** : Modèles d'authentification basés sur middleware en Python (Starlette) et TypeScript (Express), avec exemples de code.
  - **Progression vers la sécurité avancée** : Conseils pour débuter avec une auth simple et évoluer vers OAuth 2.1 et RBAC, avec références aux modules de sécurité avancée.

Ces ajouts fournissent des conseils pratiques et concrets pour construire des implémentations serveur MCP plus robustes, sécurisées et flexibles, établissant un pont entre concepts fondamentaux et modèles avancés pour la production.

## 29 septembre 2025

### Laboratoires d'intégration base de données MCP Server - Parcours complet d'apprentissage pratique

#### 11-MCPServerHandsOnLabs - Nouveau curriculum complet d'intégration base de données
- **Parcours complet de 13 laboratoires** : Ajout d'un curriculum pratique complet pour construire des serveurs MCP prêts pour la production avec intégration base de données PostgreSQL
  - **Implémentation concrète** : Cas d'usage analytique de Zava Retail démontrant des modèles de niveau entreprise
  - **Progression d'apprentissage structurée** :
    - **Labs 00-03 : Fondations** - Introduction, Architecture centrale, Sécurité & Multi-Tenancy, Configuration de l'environnement
    - **Labs 04-06 : Construction du serveur MCP** - Conception de la base de données & schéma, Implémentation du serveur MCP, Développement d'outils  
    - **Labs 07-09 : Fonctionnalités avancées** - Intégration de recherche sémantique, Tests & débogage, Intégration VS Code
    - **Labs 10-12 : Production & bonnes pratiques** - Stratégies de déploiement, Surveillance & observabilité, Bonnes pratiques & optimisation
  - **Technologies d'entreprise** : Framework FastMCP, PostgreSQL avec pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Fonctionnalités avancées** : Sécurité au niveau de la ligne (RLS), recherche sémantique, accès multi-tenant aux données, embeddings vectoriels, surveillance en temps réel

#### Standardisation de la terminologie - Conversion de modules en laboratoires
- **Mise à jour complète de la documentation** : Mise à jour systématique de tous les fichiers README dans 11-MCPServerHandsOnLabs pour utiliser la terminologie "Lab" au lieu de "Module"
  - **En-têtes de section** : Changement de "Ce module couvre" en "Ce laboratoire couvre" à travers les 13 laboratoires
  - **Description du contenu** : Modification de "Ce module fournit..." en "Ce laboratoire fournit..." partout dans la documentation
  - **Objectifs d'apprentissage** : Modification de "À la fin de ce module..." en "À la fin de ce laboratoire..." 
  - **Liens de navigation** : Conversion de toutes les références "Module XX :" en "Lab XX :" dans les références croisées et la navigation
  - **Suivi de complétion** : Mise à jour de "Après avoir terminé ce module..." en "Après avoir terminé ce laboratoire..."
  - **Références techniques conservées** : Maintien des références aux modules Python dans les fichiers de configuration (ex. : `"module": "mcp_server.main"`)

#### Amélioration du guide d'étude (study_guide.md)
- **Carte visuelle du curriculum** : Ajout d'une nouvelle section "11. Laboratoires d'intégration base de données" avec une visualisation complète de la structure des laboratoires
- **Structure du dépôt** : Mise à jour de dix à onze sections principales avec description détaillée de 11-MCPServerHandsOnLabs
- **Orientation du parcours d'apprentissage** : Amélioration des instructions de navigation couvrant les sections 00 à 11
- **Couverture technologique** : Ajout de détails sur FastMCP, PostgreSQL, intégration des services Azure
- **Résultats d'apprentissage** : Accent sur le développement de serveurs prêts pour la production, modèles d'intégration base de données, sécurité entreprise

#### Amélioration de la structure du README principal
- **Terminologie basée sur les laboratoires** : Mise à jour du README.md principal dans 11-MCPServerHandsOnLabs pour utiliser systématiquement la structure "Laboratoire"
- **Organisation du parcours d'apprentissage** : Progression claire des concepts fondamentaux à la mise en œuvre avancée jusqu'au déploiement en production
- **Focalisation terrain** : Accent sur l'apprentissage pratique avec des modèles et technologies de niveau entreprise

### Améliorations de la qualité et de la cohérence de la documentation
- **Accent sur la formation pratique** : Renforcement de l'approche pratique basée sur les laboratoires dans toute la documentation
- **Focalisation sur les modèles d'entreprise** : Mise en avant des implémentations prêtes pour la production et des considérations de sécurité entreprise
- **Intégration technologique** : Couverture complète des services modernes Azure et des modèles d'intégration IA
- **Progression d'apprentissage** : Parcours clair et structuré des concepts de base au déploiement en production

## 26 septembre 2025

### Amélioration des études de cas - Intégration du registre MCP GitHub

#### Études de cas (09-CaseStudy/) - Focus sur le développement de l'écosystème
- **README.md** : Expansion majeure avec étude de cas complète sur le registre MCP GitHub
  - **Étude de cas du registre MCP GitHub** : Nouvelle étude détaillée examinant le lancement du registre MCP GitHub en septembre 2025
    - **Analyse des problèmes** : Examen approfondi des défis de découverte et de déploiement fragmentés des serveurs MCP
    - **Architecture de la solution** : Approche de registre centralisé de GitHub avec installation VS Code en un clic
    - **Impact commercial** : Améliorations mesurables dans l'intégration et la productivité des développeurs
    - **Valeur stratégique** : Focus sur le déploiement modulaire d'agents et l'interopérabilité entre outils
    - **Développement de l'écosystème** : Positionnement comme plateforme fondatrice pour l'intégration agentique
  - **Structure optimisée des études de cas** : Mise à jour de toutes les sept études avec formatage cohérent et descriptions complètes
    - Agents de voyage IA Azure : Accent sur l'orchestration multi-agent
    - Intégration Azure DevOps : Focus sur l'automatisation des workflows
    - Récupération de documentation en temps réel : Mise en œuvre client console Python
    - Générateur de plans d'étude interactif : Application web conversationnelle Chainlit
    - Documentation intégrée à l'éditeur : Intégration VS Code et GitHub Copilot
    - Azure API Management : Modèles d'intégration API entreprise
    - Registre MCP GitHub : Développement d'écosystème et plateforme communautaire
  - **Conclusion complète** : Réécriture de la section conclusion mettant en avant sept études couvrant plusieurs dimensions d'implémentation MCP
    - Intégration entreprise, orchestration multi-agent, productivité des développeurs
    - Développement de l'écosystème, catégorisation des applications éducatives
    - Aperçus améliorés sur les modèles architecturaux, stratégies d'implémentation et meilleures pratiques
    - Accent sur MCP en tant que protocole mature et prêt pour la production

#### Mises à jour du guide d'étude (study_guide.md)
- **Carte visuelle du curriculum** : Mise à jour du mindmap pour inclure le registre MCP GitHub dans la section Études de cas
- **Description des études de cas** : Amélioration des descriptions génériques vers un décryptage détaillé de sept études de cas complètes
- **Structure du dépôt** : Mise à jour de la section 10 pour refléter une couverture complète des études avec détails spécifiques d'implémentation
- **Intégration du changelog** : Ajout de l'entrée du 26 septembre 2025 documentant l'ajout du registre MCP GitHub et améliorations des études de cas
- **Mises à jour des dates** : Mise à jour du timestamp du pied de page pour refléter la révision la plus récente (26 septembre 2025)

### Améliorations de la qualité de la documentation
- **Amélioration de la cohérence** : Normalisation du formatage et de la structure des études de cas sur les sept exemples
- **Couverture complète** : Les études couvrent désormais les scénarios d'entreprise, productivité des développeurs et développement d'écosystème
- **Positionnement stratégique** : Accent renforcé sur MCP comme plateforme fondatrice pour le déploiement de systèmes agents
- **Intégration des ressources** : Mise à jour des ressources supplémentaires pour inclure le lien vers le registre MCP GitHub

## 15 septembre 2025

### Expansion des sujets avancés - Transports personnalisés & ingénierie du contexte

#### Transports personnalisés MCP (05-AdvancedTopics/mcp-transport/) - Nouveau guide d'implémentation avancée
- **README.md** : Guide complet d'implémentation des mécanismes de transport personnalisés MCP
  - **Transport Azure Event Grid** : Mise en œuvre complète de transport événementiel serverless
    - Exemples en C#, TypeScript et Python avec intégration Azure Functions
    - Modèles d'architecture événementielle pour solutions MCP évolutives
    - Récepteurs webhook et gestion de messages push
  - **Transport Azure Event Hubs** : Mise en œuvre de transport streaming à haut débit
    - Capacités de streaming en temps réel pour scénarios à faible latence
    - Stratégies de partitionnement et gestion des checkpoints
    - Regroupement de messages et optimisation des performances
  - **Modèles d'intégration entreprise** : Exemples architecturaux prêts pour la production
    - Traitement MCP distribué sur plusieurs Azure Functions
    - Architectures de transport hybrides combinant plusieurs types de transport
    - Durabilité des messages, fiabilité et stratégies de gestion des erreurs
  - **Sécurité & surveillance** : Intégration Azure Key Vault et modèles d'observabilité
    - Authentification par identité gérée et principe du moindre privilège
    - Télémétrie Application Insights et surveillance des performances
    - Coupe-circuits et modèles de tolérance aux pannes
  - **Cadres de test** : Stratégies de test complètes pour transports personnalisés
    - Tests unitaires avec doubles de test et frameworks de mock
    - Tests d'intégration avec Azure Test Containers
    - Considérations pour tests de performance et de charge

#### Ingénierie du contexte (05-AdvancedTopics/mcp-contextengineering/) - Discipline émergente en IA
- **README.md** : Exploration complète de l'ingénierie du contexte comme domaine émergent
  - **Principes fondamentaux** : Partage complet du contexte, conscience des décisions d'action, et gestion des fenêtres de contexte

  - **Alignement du protocole MCP** : Comment la conception MCP répond aux défis de l'ingénierie du contexte
    - Limitations de la fenêtre de contexte et stratégies de chargement progressif
    - Détermination de la pertinence et récupération dynamique du contexte
    - Gestion multimodale du contexte et considérations de sécurité
  - **Approches de mise en œuvre** : Architectures mono-thread vs multi-agents
    - Techniques de découpage et de priorisation du contexte
    - Stratégies de chargement progressif et de compression du contexte
    - Approches en couches du contexte et optimisation de la récupération
  - **Cadre de mesure** : Métriques émergentes pour l'évaluation de l'efficacité du contexte
    - Efficacité des entrées, performances, qualité et considérations d'expérience utilisateur
    - Approches expérimentales pour l'optimisation du contexte
    - Analyse des échecs et méthodologies d'amélioration

#### Mises à jour de la navigation du curriculum (README.md)
- **Structure de module améliorée** : Table du curriculum mise à jour pour inclure de nouveaux sujets avancés
  - Ajout des entrées Ingénierie du Contexte (5.14) et Transport personnalisé (5.15)
  - Formatage cohérent et liens de navigation à travers tous les modules
  - Descriptions mises à jour pour refléter le périmètre actuel du contenu

### Améliorations de la structure des dossiers
- **Normalisation des noms** : Renommé "mcp transport" en "mcp-transport" pour cohérence avec les autres dossiers de sujets avancés
- **Organisation du contenu** : Tous les dossiers 05-AdvancedTopics suivent désormais un schéma de nommage cohérent (mcp-[topic])

### Améliorations de la qualité de la documentation
- **Alignement sur la spécification MCP** : Tous les nouveaux contenus réfèrent à la spécification MCP en date du 18-06-2025
- **Exemples multilingues** : Exemples de code complets en C#, TypeScript, et Python
- **Orientation entreprise** : Modèles prêts pour la production et intégration Azure cloud partout
- **Documentation visuelle** : Diagrammes Mermaid pour visualiser l'architecture et les flux

## 18 août 2025

### Mise à jour complète de la documentation - Normes MCP 18-06-2025

#### Bonnes pratiques de sécurité MCP (02-Security/) - Modernisation complète
- **MCP-SECURITY-BEST-PRACTICES-2025.md** : Réécriture complète alignée avec la spécification MCP du 18-06-2025
  - **Exigences obligatoires** : Ajout des exigences EXIGÉ/NE DOIT PAS issues de la spécification officielle avec indicateurs visuels clairs
  - **12 pratiques de sécurité clés** : Restructuration d’une liste de 15 items en domaines de sécurité complets
    - Sécurité des jetons & authentification avec intégration fournisseur d'identité externe
    - Gestion des sessions & sécurité du transport avec exigences cryptographiques
    - Protection spécifique aux menaces IA avec intégration Microsoft Prompt Shields
    - Contrôle d’accès & permissions avec principe du moindre privilège
    - Sécurité & surveillance du contenu avec intégration Azure Content Safety
    - Sécurité de la chaîne d’approvisionnement avec vérification complète des composants
    - Sécurité OAuth & prévention des attaques déléguées avec implémentation PKCE
    - Réponse aux incidents & récupération avec capacités automatisées
    - Conformité & gouvernance avec alignement réglementaire
    - Contrôles de sécurité avancés avec architecture zero trust
    - Intégration de l’écosystème Microsoft Security avec solutions complètes
    - Évolution continue de la sécurité avec pratiques adaptatives
  - **Solutions Microsoft Security** : Guide d’intégration renforcé pour Prompt Shields, Azure Content Safety, Entra ID, et GitHub Advanced Security
  - **Ressources de mise en œuvre** : Liens de ressources catégorisés par documentation officielle MCP, solutions Microsoft Security, normes de sécurité, et guides de mise en œuvre

#### Contrôles de sécurité avancés (02-Security/) - Mise en œuvre entreprise
- **MCP-SECURITY-CONTROLS-2025.md** : Refondation complète avec cadre de sécurité de niveau entreprise
  - **9 domaines de sécurité complets** : Étendu des contrôles basiques vers un cadre d’entreprise détaillé
    - Authentification & autorisation avancées avec intégration Microsoft Entra ID
    - Sécurité des jetons & contrôles anti-passthrough avec validation complète
    - Contrôles de sécurité des sessions avec prévention du détournement
    - Contrôles de sécurité spécifiques à l’IA avec prévention des injections de prompt et empoisonnement d’outils
    - Prévention des attaques déléguées avec sécurité proxy OAuth
    - Sécurité d’exécution des outils avec sandboxing et isolation
    - Contrôles de sécurité de la chaîne d’approvisionnement avec vérification des dépendances
    - Contrôles de surveillance & détection avec intégration SIEM
    - Réponse aux incidents & récupération avec capacités automatisées
  - **Exemples de mise en œuvre** : Ajout de blocs de configuration YAML détaillés et exemples de code
  - **Intégration solutions Microsoft** : Couverture complète des services de sécurité Azure, GitHub Advanced Security, et gestion d’identités en entreprise

#### Sécurité des sujets avancés (05-AdvancedTopics/mcp-security/) - Mise en œuvre prête pour production
- **README.md** : Réécriture complète pour la mise en œuvre de sécurité en entreprise
  - **Alignement sur la spécification actuelle** : Mise à jour selon la spécification MCP du 18-06-2025 avec exigences de sécurité obligatoires
  - **Authentification améliorée** : Intégration Microsoft Entra ID avec exemples complets en .NET et Java Spring Security
  - **Intégration sécurité IA** : Implémentation Microsoft Prompt Shields et Azure Content Safety avec exemples Python détaillés
  - **Atténuation avancée des menaces** : Exemples complets de mise en œuvre pour
    - Prévention des attaques déléguées avec validation PKCE et consentement utilisateur
    - Prévention de passage des jetons avec validation d’audience et gestion sécurisée des jetons
    - Prévention du détournement de session avec liaison cryptographique et analyse comportementale
  - **Intégration sécurité entreprise** : Surveillance Azure Application Insights, pipelines de détection des menaces, et sécurité de la chaîne d’approvisionnement
  - **Liste de contrôle de mise en œuvre** : Contrôles de sécurité obligatoires vs recommandés clairs avec bénéfices de l’écosystème Microsoft Security

### Qualité de la documentation & alignement des normes
- **Références à la spécification** : Mise à jour de toutes les références à la spécification MCP du 18-06-2025
- **Écosystème Microsoft Security** : Guide d’intégration renforcé dans toute la documentation de sécurité
- **Mise en œuvre pratique** : Ajout d’exemples de code détaillés en .NET, Java, et Python avec modèles d’entreprise
- **Organisation des ressources** : Catégorisation complète de la documentation officielle, normes de sécurité, et guides d’implémentation
- **Indicateurs visuels** : Marquage clair des exigences obligatoires vs pratiques recommandées


#### Concepts de base (01-CoreConcepts/) - Modernisation complète
- **Mise à jour de la version du protocole** : Référence mise à jour à la spécification MCP du 18-06-2025 avec versionnement basé sur la date (format AAAA-MM-JJ)
- **Affinement de l’architecture** : Descriptions améliorées des hôtes, clients, et serveurs pour refléter les modèles d’architecture MCP actuels
  - Les hôtes sont désormais clairement définis comme applications IA coordonnant plusieurs connexions clients MCP
  - Les clients décrits comme connecteurs de protocole maintenant une relation un-à-un avec les serveurs
  - Serveurs enrichis avec scénarios de déploiement local vs distant
- **Restructuration des primitives** : Refonte complète des primitives serveur et client
  - Primitives serveur : Ressources (sources de données), Prompts (modèles), Outils (fonctions exécutables) avec explications et exemples détaillés
  - Primitives client : Échantillonnage (complétions LLM), Sollicitation (entrée utilisateur), Journalisation (débogage/surveillance)
  - Mise à jour avec les modèles actuels de méthodes découverte (`*/list`), récupération (`*/get`) et exécution (`*/call`)
- **Architecture du protocole** : Introduction d’un modèle d’architecture à deux couches
  - Couche de données : fondation JSON-RPC 2.0 avec gestion du cycle de vie et primitives
  - Couche de transport : mécanismes de transport STDIO (local) et HTTP streamable avec SSE (à distance)
- **Cadre de sécurité** : Principes de sécurité complets incluant consentement utilisateur explicite, protection des données, sécurité d’exécution des outils, et sécurité couche transport
- **Schémas de communication** : Mise à jour des messages de protocole pour montrer les flux d’initialisation, découverte, exécution, et notification
- **Exemples de code** : Mise à jour des exemples multilingues (.NET, Java, Python, JavaScript) pour refléter les modèles MCP SDK actuels

#### Sécurité (02-Security/) - Refonte complète de la sécurité  
- **Alignement aux normes** : Alignement complet avec les exigences de sécurité de la spécification MCP du 18-06-2025
- **Évolution de l’authentification** : Documentation de l’évolution des serveurs OAuth personnalisés vers délégation fournisseur d’identité externe (Microsoft Entra ID)
- **Analyse des menaces spécifiques à l’IA** : Couverture renforcée des vecteurs d’attaque IA modernes
  - Scénarios détaillés d’attaques par injection de prompt avec exemples réels
  - Mécanismes d’empoisonnement d’outils et modèles d’attaque « rug pull »
  - Empoisonnement de la fenêtre de contexte et attaques de confusion de modèle
- **Solutions Microsoft pour la sécurité IA** : Couverture complète de l’écosystème Microsoft Security
  - Prompt Shields IA avec détection avancée, spotlighting, et techniques de délimitation
  - Modèles d’intégration Azure Content Safety
  - GitHub Advanced Security pour la protection de la chaîne d’approvisionnement
- **Atténuation avancée des menaces** : Contrôles de sécurité détaillés pour
  - Détournement de session avec scénarios d’attaque spécifiques MCP et exigences cryptographiques pour l’ID de session
  - Problèmes d’attaque déléguée dans les scénarios proxy MCP avec exigences de consentement explicite
  - Vulnérabilités de passage des jetons avec contrôles de validation obligatoires
- **Sécurité de la chaîne d’approvisionnement** : Couverture élargie de la chaîne d’approvisionnement IA incluant modèles fondateurs, services d’embedings, fournisseurs de contexte, et API tierces
- **Sécurité fondationnelle** : Intégration renforcée avec les modèles de sécurité d’entreprise, incluant architecture zero trust et écosystème Microsoft Security
- **Organisation des ressources** : Liens de ressources catégorisés par type (Documentation officielle, normes, recherche, solutions Microsoft, guides d’implémentation)

### Améliorations de la qualité de la documentation
- **Objectifs d’apprentissage structurés** : Objectifs d’apprentissage améliorés avec résultats spécifiques et actionnables 
- **Références croisées** : Ajout de liens entre sujets de sécurité et concepts de base liés
- **Informations à jour** : Mise à jour de toutes les références de date et liens vers les normes actuelles
- **Guides de mise en œuvre** : Ajout de directives spécifiques et actionnables tout au long des deux sections

## 16 juillet 2025

### Améliorations de README et de la navigation
- Navigation du curriculum entièrement repensée dans README.md
- Remplacé les balises `<details>` par un format basé sur des tableaux plus accessible
- Créé des options de mise en page alternative dans un nouveau dossier "alternative_layouts"
- Ajout d’exemples de navigation en style cartes, onglets, et accordéon
- Mise à jour de la section structure du dépôt pour inclure tous les fichiers récents
- Amélioration de la section "Comment utiliser ce curriculum" avec recommandations claires
- Mise à jour des liens vers la spécification MCP vers les bonnes URLs
- Ajout de la section Ingénierie du contexte (5.14) à la structure du curriculum

### Mises à jour du guide d’études
- Révision complète du guide d’études pour s’aligner sur la structure actuelle du dépôt
- Ajout de nouvelles sections pour les clients MCP et outils, ainsi que les serveurs MCP populaires
- Mise à jour de la carte visuelle du curriculum pour refléter précisément tous les sujets
- Amélioration des descriptions des sujets avancés pour couvrir toutes les spécialisations
- Mise à jour de la section études de cas pour refléter des exemples réels
- Ajout de ce journal des modifications complet

### Contributions de la communauté (06-CommunityContributions/)
- Ajout d’informations détaillées sur les serveurs MCP pour génération d’images
- Ajout d’une section complète sur l’utilisation de Claude dans VSCode
- Ajout des instructions de configuration et d’utilisation du client terminal Cline
- Mise à jour de la section clients MCP pour inclure toutes les options populaires
- Amélioration des exemples de contribution avec des exemples de code plus précis

### Sujets avancés (05-AdvancedTopics/)
- Organisation cohérente de tous les dossiers des sujets spécialisés suivant un nommage unifié
- Ajout des supports et exemples sur l’ingénierie du contexte
- Ajout de la documentation d’intégration de l’agent Foundry
- Amélioration de la documentation d’intégration de sécurité Entra ID

## 11 juin 2025

### Création initiale
- Publication de la première version du curriculum MCP pour débutants
- Création de la structure de base pour les 10 sections principales
- Mise en place de la carte visuelle du curriculum pour la navigation
- Ajout de projets exemples initiaux en plusieurs langages de programmation

### Premiers pas (03-GettingStarted/)
- Création des premiers exemples de mise en œuvre serveur
- Ajout de guides de développement client
- Inclusion des instructions d’intégration client LLM
- Ajout de la documentation pour intégration VS Code
- Mise en œuvre d’exemples de serveurs utilisant Server-Sent Events (SSE)

### Concepts de base (01-CoreConcepts/)
- Ajout d’expllications détaillées sur l’architecture client-serveur
- Création de la documentation sur les composants clés du protocole
- Documentation des schémas de messagerie dans MCP

## 23 mai 2025

### Structure du dépôt
- Initialisation du dépôt avec structure de dossier basique
- Création des fichiers README pour chaque section majeure
- Mise en place de l’infrastructure de traduction
- Ajout des assets images et diagrammes

### Documentation
- Création du README.md initial avec aperçu du curriculum
- Ajout de CODE_OF_CONDUCT.md et SECURITY.md
- Mise en place du SUPPORT.md avec directives d’assistance
- Création de la structure préliminaire du guide d’études

## 15 avril 2025

### Planification et cadre
- Planification initiale du curriculum MCP pour débutants
- Définition des objectifs d’apprentissage et du public cible
- Esquisse de la structure en 10 sections du curriculum
- Développement du cadre conceptuel pour exemples et études de cas
- Création d’exemples prototypes initiaux pour concepts clés

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->