# Journal des modifications : Programme MCP pour débutants

Ce document sert de registre pour tous les changements significatifs apportés au programme Model Context Protocol (MCP) pour débutants. Les changements sont documentés dans l'ordre chronologique inverse (le plus récent en premier).

## 9 septembre 2026

### Alignement avec la spécification finale MCP 2026-07-28

Mise à jour du programme anglais depuis la version candidat à la sortie et le guide de référence `2025-11-25`
vers la spécification finale MCP `2026-07-28`.

- **Mise à jour** : Références à la version actuelle, liens de spécification, guide des requêtes sans état,
  `server/discover`, en-têtes HTTP Streamable, et le cycle de vie de l'extension Tasks
  à travers 38 fichiers de documentation en anglais.
- **Correction** : L'élucidation utilise désormais `elicitation/create`, le Sampling utilise
  `sampling/createMessage`, et `InputRequiredResult.resultType` utilise
  `"input_required"`.
- **Remplacement** : La leçon inexacte sur l'état de conversation Root Context a été remplacée par une
  leçon Roots précise conforme au protocole couvrant les indications informatives sur le système de fichiers,
  le flux multi-allers-retours actuel, les frontières de sécurité, et les options de migration.
- **Clarification** : Roots, Sampling, Logging et Dynamic Client Registration sont
  dépréciés dans `2026-07-28`, avec leurs remplacements recommandés et la date
  la plus ancienne de suppression documentée.
- **Étiquetage** : Les exemples qui dépendent encore de MCP `2025-11-25`, HTTP+SSE,
  des négociations d'initialisation, ou des sessions de protocole sont conservés comme exemples
  de compatibilité héritée plutôt que présentés comme des implémentations actuelles.
- **Conseils de sécurité** : Mise à jour des guides de sécurité autonomes pour utiliser
  une autorisation par requête et des gestionnaires d'état d'application explicites au lieu des
  identifiants de session de protocole supprimés. Les Documents de métadonnées Client ID sont désormais le
  chemin d'enregistrement privilégié, avec DCR documenté comme uniquement compatible.
- **Matériel de support** : Mise à jour du guide d'étude, de la checklist des contributeurs,
  de l'étude de cas Publora, et de l'étude de cas APIM. Le parcours APIM recommande désormais
  son point de terminaison HTTP Streamable `/mcp` actuel au lieu du `/sse` déprécié.
- **Liens canoniques** : Remplacement des URLs de spécifications retirées et brouillons dans
  les fichiers source anglais Markdown par des liens versionnés `2026-07-28`, tout en conservant les
  liens explicites vers les versions héritées lorsque un exemple reste attaché à des outils plus anciens.
- **Noms de fichiers stables** : Renommage du guide final de spécification et de deux guides de
  sécurité pour supprimer les suffixes candidat à la sortie et année, puis mise à jour de tous les
  hyperliens anglais vers leurs chemins stables.
- **Nouveau exemple d'autorisation** : Ajout d’un
  [serveur de ressources MCP `2026-07-28` en TypeScript](./02-Security/samples/cimd-dcr-auth/README.md)
  testé qui compare les Documents de métadonnées Client ID privilégiés avec une solution de repli dépréciée de Dynamic
  Client Registration. L'exemple inclut la découverte RFC 9728, la validation JWKS,
  des scopes par outil, douze tests, et un parcours de configuration Auth0.
- **Portée de la traduction** : Seuls les fichiers source en anglais ont été modifiés ; les traductions
  générées et les images traduites restent inchangées car elles sont traduites automatiquement.

## 29 juillet 2026

### Nouveau module 08 compagnon : Sidecars de fiabilité et nouvelles tentatives sécurisées

Ajout d'une leçon complémentaire neutre au fournisseur pour les outils MCP qui créent des effets réels,
alignée avec la spécification finale `2026-07-28`.

- **Nouveau** : La [leçon compagnon sidecar de fiabilité][reliability-sidecar]
  utilise une histoire de ticket de support, deux diagrammes Mermaid, et un flux de décision de nouvelle tentative
  pour expliquer les clés d'opération stables, l'admission atomique des doublons,
  la réconciliation, les preuves, et la frontière de l'extension Tasks.
- **Nouveau** : Un exercice d'injection de pannes en Python et SQLite bibliothèque standard
  utilise des stores séparés pour opérations et tickets afin de démontrer une réponse perdue
  après validation d'un effet externe. Six tests déterministes couvrent la duplication naïve,
  la récupération de redémarrage protégée, les conflits de charge utile, les résultats mis en cache,
  les revendications actives, et l'admission simultanée des doublons.
- **Mise à jour** : Le module 08 lie désormais la leçon compagnon, identifie le
  modèle de requête sans état final `2026-07-28`, distingue l'observabilité OpenTelemetry
  de la fonction de journalisation MCP dépréciée, et limite son
  exemple générique de nouvelle tentative aux opérations en lecture seule.
- **Optionnel** : La leçon cartographie ses concepts portables sur une implémentation communautaire taguée
  sans faire du service hébergé ou d'un appel réseau une partie de
  l'exercice.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 juillet 2026

### Nouvelle leçon : Version candidate de spécification MCP 2026-07-28

Ajout de la couverture de la version candidate de spécification MCP `2026-07-28` à venir (annoncée le 21 mai 2026 ; sortie finale prévue le 28 juillet 2026), résumée à partir du [billet de blog officiel](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). La base du programme reste **MCP Spécification 2025-11-25** jusqu'à la sortie de la nouvelle version, donc ceci est présenté comme une orientation prospective plutôt qu'une réécriture des leçons existantes.

- **Nouveau** : [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — une leçon complète couvrant le noyau sans état du protocole (suppression de la poignée de main `initialize` et de `Mcp-Session-Id`), les nouveaux en-têtes de routage `Mcp-Method`/`Mcp-Name`, les métadonnées de cache `ttlMs`/`cacheScope`, le Contexte de Trace W3C dans `_meta`, le cadre formel des Extensions (applications MCP et nouvelle extension Tasks), six SEP de durcissement d'autorisation, la dépréciation de Roots/Sampling/Logging, et la transition vers JSON Schema 2020-12 complet pour les schémas d'outil.
- **Mise à jour** avec des appels prospectifs vers la nouvelle leçon :
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md) : note sur la version du protocole, sections Sampling/Roots/Logging/Tasks, et « Ce qui suit »
  - [02-Security/README.md](./02-Security/README.md) : appel au durcissement de l'autorisation
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md) : appel au transport sans état
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md) : appel à la dépréciation de Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md) : appel à la dépréciation de Logging et extension Tasks

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md) : encadré sur le routage stateless/session
  - [README.md](./README.md) : note « Perspectives » dans la section spécification et nouvelle entrée `1.1` dans le tableau du module curriculum
  - [study_guide.md](./study_guide.md) : point prospectif sous la vue d’ensemble des Concepts Clés et note d’addendum datée
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md) : encadré sur la map de transport `mcp-session-id` avant le modèle de requête stateless
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md) : encadré de vue d’ensemble du module sur les dépréciations des Contextes Racine/Échantillonnage et l’extension des Tâches
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md) : encadré sur le renforcement de l’autorisation

## 24 juin 2026

### Nouvelle leçon : Utiliser MCP dans l’application Copilot

- [Section Outils](./12-tooling/README.md) Section outils ajoutée.
- [MCP dans l’application Copilot](./12-tooling/01-copilot-app/README.md)

## 16 juin 2026

### Alignement de la spécification MCP & validation des exemples

Validation du curriculum à l’aune de la **Spécification MCP 2025-11-25** actuelle et des derniers SDK officiels, correction des références périmées restantes à la spécification et confirmation que les exemples principaux compilent toujours et fonctionnent.

#### Corrections de versions de la spécification (2025-06-18 / 2025-03-26 → 2025-11-25)

Mise à jour du contenu anglais indiquant encore une ancienne révision de spécification comme norme *courante/dernière*, et redirection des liens vers les chemins canoniques de la spécification sur `modelcontextprotocol.io` :
- **05-AdvancedTopics/mcp-security/README.md** : Mise à jour de la bannière « Norme Courante », introduction, rubrique des principes clés de sécurité, rubrique des exigences obligatoires, section Microsoft Entra ID, liens Références & Ressources, et note de clôture sur la sécurité (8 références) à 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md** : Mise à jour du lien vers les ressources additionnelles et de la bannière « Norme Courante » vers 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md** : Remplacement du lien périmé `2025-03-26` sur la sécurité et la confiance par la page actuelle des bonnes pratiques de sécurité 2025-11-25
- **03-GettingStarted/14-sampling/README.md** : Mise à jour du lien officiel vers la documentation sur l’échantillonnage vers 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md** : Mise à jour de la référence au présent « spécification MCP actuelle » et du lien vers les ressources additionnelles à 2025-11-25 (notes historiques sur la dépréciation SSE laissées intactes pour exactitude)

#### Validation des exemples avec les SDK actuels

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)** : `npm install` a résolu `@modelcontextprotocol/sdk@1.29.0` ; `tsc --noEmit` passé sans erreurs de type — APIs existantes `McpServer`/`StdioServerTransport` restent valides
- **Python (03-GettingStarted/01-first-server/solution/python)** : Validation dans un `.venv` isolé avec `mcp[cli]` (1.27.2) ; `py_compile` passé et `FastMCP.list_tools()` retourne correctement les outils `add` et `subtract`
- Confirmation que toutes les plages de versions d’exemples `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) se résolvent proprement vers la version courante `1.29.0` sans changements incompatibles de l’API

#### Alignement des dépendances (comblement des écarts de version)

Rehaussement des versions de SDK périmées pour que chaque exemple suive la release MCP courante, conformément à la convention du dépôt :
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json** : Passage de `@modelcontextprotocol/sdk` de `^1.8.0` → `>=1.26.0` et mise à jour de la description du package périmé `"updated for MCP 2025-06-18"` en `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** et **lab4/code/github_mcp_server/pyproject.toml** : Passage de la version exacte `mcp==1.23.0` → `mcp>=1.26.0` ; régénération des deux fichiers `uv.lock` (`uv lock`) pour que les fichiers verrouillés résolvent la version `mcp 1.27.2` actuelle et restent synchronisés avec les manifestes

#### Analyse des lacunes du curriculum — Couverture des dernières fonctionnalités de la spec

Vérification que le curriculum couvre déjà tous les primitifs introduits/étendus dans MCP 2025-11-25, sans lacunes de contenu restantes :
- **Échantillonnage** : Leçon 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Élicitation (incl. mode URL)** : Documenté dans 01-CoreConcepts et 05-AdvancedTopics/mcp-protocol-features
- **Racines** : Documenté dans 00-Introduction, 01-CoreConcepts, et 05-AdvancedTopics/mcp-root-contexts
- **Tâches (expérimental, opérations longues)** : Documenté dans 01-CoreConcepts et 05-AdvancedTopics/mcp-protocol-features
- **Annotations d’outil** (`readOnlyHint` / `destructiveHint`) : Documenté dans 01-CoreConcepts et 05-AdvancedTopics/mcp-protocol-features

### Renforcement de la sécurité & remédiation des vulnérabilités des dépendances

Audit complet de la sécurité sur chaque manifeste de dépendances et le code source des exemples, puis remédiation de tous les avis signalés par npm et d’un problème au niveau code. Après remédiation, `npm audit` signale **0 vulnérabilités** dans chaque répertoire audité.

#### Vulnérabilités transitives dans les dépendances npm — Corrigées

Audit de tous les 15 fichiers `package-lock.json` commités. Les vulnérabilités se limitaient aux dépendances transitives embarquées par l’outil de développement MCP Inspector, le client OpenAI et le SDK MCP ; toutes sont maintenant résolues sans casser les exemples :

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** et **lab3/code/weather_mcp/inspector** : Mise à jour de `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), ce qui a éliminé les avis de sécurité liés à `ajv`, `brace-expansion`, `diff`, `path-to-regexp` et `ws` inclus. Ajout d'une entrée npm `overrides` forçant la version corrigée de `shell-quote@1.8.4` pour éliminer l'avis critique restant porté par `concurrently` ; régénération des deux fichiers de verrouillage (maintenant 0 vulnérabilités)
- **03-GettingStarted/samples/typescript** : `npm audit fix` a mis à jour la dépendance transitive `qs` (modérée) vers une version corrigée
- **03-GettingStarted/samples/javascript** : `npm audit fix` a mis à jour la dépendance transitive `hono` (modérée) vers une version corrigée
- **03-GettingStarted/03-llm-client/solution/typescript** : `npm audit fix` a mis à jour la dépendance transitive `form-data` (élevée) vers une version corrigée
- **03-GettingStarted/11-simple-auth/solution/typescript** : Génération du fichier manquant `package-lock.json` pour assurer la reproductibilité et l'auditabilité du projet (0 vulnérabilités)

#### Correction de Sécurité au Niveau du Code (OWASP A03 : Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py** : Suppression de `shell=True` de l'outil `open_in_vscode`. La commande précédente `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` permettait à des méta-caractères shell dans un chemin de dossier d'être interprétés par `cmd.exe` (vecteur d'injection de commande). Elle lance désormais directement `Code.exe` résolu avec le dossier en argument — sans shell — ce qui est fonctionnellement équivalent et sûr

#### Audit des Dépendances Python

- Audit de chaque liste de dépendances Python avec `pip-audit`. `05-AdvancedTopics` et `03-GettingStarted/samples/python` n'ont signalé **aucune vulnérabilité connue** (leurs plages `mcp` / `httpx` / `pydantic` / `python-dotenv` correspondent à des versions corrigées actuelles)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt** : `pip-audit` a signalé la dépendance transitive **`werkzeug` 3.1.1** avec trois avis de déni de service `safe_join` sur les noms de périphériques Windows — `CVE-2025-66221`, `CVE-2026-21860` et `CVE-2026-27199` (tous corrigés en 3.1.6). Ajout d'un verrou de sécurité explicite `werkzeug>=3.1.6` pour résoudre la version corrigée ; vérification que la contrainte se résout proprement avec la pile `chainlit` / `mcp` / `semantic-kernel`

### Changement de Nom du Produit

Mise à jour de tout le contenu du programme pour refléter le changement de nom des produits Microsoft :

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md** : Mise à jour du lien de la communauté Discord
- **AGENTS.md** : Mise à jour de la référence au serveur Discord
- **README.md** : Mise à jour des références à l’écosystème technologique
- **study_guide.md** : Mise à jour des références aux études de cas
- **05-AdvancedTopics/README.md** : Mise à jour du titre et de la description du Module 5.13
- **05-AdvancedTopics/mcp-integration/README.md** : Mise à jour de l’en-tête de section et de la description
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md** : Mise à jour complète du titre et du contenu du module
- **05-AdvancedTopics/mcp-security-entra/README.md** : Mise à jour du lien de référence croisée
- **07-LessonsfromEarlyAdoption/README.md** : Mise à jour des références aux études de cas
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md** : Mise à jour de l’en-tête de la section 9, des badges et des capacités
- **08-BestPractices/README.md** : Mise à jour du lien de la communauté Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md** : Mise à jour de la référence au canal Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md** : Mise à jour de la référence au déploiement du modèle
- **11-MCPServerHandsOnLabs/00-Introduction/README.md** : Mise à jour du tableau des services IA
- **11-MCPServerHandsOnLabs/03-Setup/README.md** : Mise à jour des références aux ressources

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension pour VS Code
- **README.md** : Mise à jour des références principales du curriculum
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md** : Mise à jour du titre du module, de la vue d’ensemble, et des en-têtes du module
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md** : Mise à jour du titre, des objectifs d’apprentissage, des instructions d’installation, et des ressources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md** : Mise à jour du titre, des objectifs d’apprentissage, du tableau des hôtes MCP, et des références croisées
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md** : Mise à jour du titre, des badges, des prérequis, et des ressources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md** : Mise à jour des références à Agent Builder et du lien de feedback
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md** : Mise à jour des prérequis et des références à l’extension

---

## 11 avril 2026

### Nouvelle Leçon, Correctifs de Documentation, et Mises à Jour des Dépendances

#### Ajout de Nouveau Contenu de Curriculum

**Module 05 - Sujets Avancés**
- **Leçon 5.17 : Raisonnement Multi-Agent Adversarial avec MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`) : Nouveau guide complet couvrant le motif de débat adversarial pour les systèmes multi-agents
  - Diagramme d’architecture Mermaid : deux agents → serveur MCP partagé → transcription du débat → juge → verdict
  - Serveur d’outils MCP partagé (`web_search` + `run_python`) implémenté en Python et TypeScript
  - Invites système adverses (POUR / CONTRE / Juge) avec exigences explicites d’utilisation d’outils
  - Orchestrateur de débat en Python, TypeScript et C# gérant les tours et le routage des arguments
  - Câblage MCP `ClientSession` pour l’orchestrateur vers les appels réels aux outils
  - Tableau des cas d’usage (détection d’hallucination, modélisation de menaces, revue de conception d’API, vérification factuelle, sélection technologique)
  - Considérations de sécurité : exécution en bac à sable, validation des appels d’outils, limitation de débit, journalisation d’audit
  - Exercice structuré avec trois scénarios pratiques (revue de code, décision d’architecture, modération de contenu)

#### Correctifs de Documentation

**Module 03 - Premiers Pas**
- **05-stdio-server/README.md** : Correction de l’exemple incomplet de serveur stdio TypeScript — ajout de l’instanciation manquante du transport (`new StdioServerTransport()`) et de l’appel `server.connect(transport)` pour correspondre aux exemples Python et .NET dans la même section
- **14-sampling/README.md** : Correction d’une faute de frappe — correction de `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Mises à Jour du Curriculum

**README principal.md**
- Ajout de l’entrée 5.17 (Raisonnement Multi-Agent Adversarial avec MCP) dans le tableau du curriculum avec un lien direct vers la nouvelle leçon

**05-AdvancedTopics/README.md**
- Ajout de la ligne Leçon 5.17 dans le tableau des leçons

**study_guide.md**
- Ajout du sujet Raisonnement Multi-Agent Adversarial à la carte mentale et à la description en prose des Sujets Avancés

#### Correctifs de Code et de Sécurité

**Module 05 - Agents Adversaires (`mcp-adversarial-agents`)**
- **Correction de sécurité — injection de commande** : remplacement de l’interpolation shell `execSync` par `execFile` + `promisify` dans l’outil TypeScript `run_python`, éliminant la surface d’injection de commande (le code contrôlé par LLM est désormais passé comme élément argv littéral sans implication shell)
- **Câblage de la boucle d’outil MCP** : mise à jour de l’orchestrateur de débat Python pour utiliser le client asynchrone `AsyncAnthropic` (remplaçant le `Anthropic` synchronisé bloquant), passer une `ClientSession` en direct directement à chaque tour d’agent, récupérer les définitions d’outils via `session.list_tools()` à chaque tour, et dispatcher les blocs `tool_use` via `session.call_tool()` en boucle jusqu’à émission finale de la réponse texte par le modèle

#### Mises à Jour des Dépendances

- Mise à jour de `hono` à 4.12.12 dans plusieurs packages (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Mise à jour de `@hono/node-server` de 1.19.11 à 1.19.13 dans les packages TypeScript
- Mise à jour de `cryptography` de 46.0.5 à 46.0.7 dans les packages Python (labs 3 et 4 de 10-StreamliningAIWorkflows)
- Mise à jour de `lodash` de 4.17.23 à 4.18.1 dans l’inspecteur 10-StreamliningAIWorkflows

#### Traductions

- Synchronisation des traductions dans plus de 48 langues avec les derniers changements de source (mise à jour i18n)

---

## 5 février 2026

### Validation et Améliorations de Navigation à l’Échelle du Dépôt

#### Ajout de Nouveau Contenu de Curriculum

**Module 03 - Premiers Pas**
- **12-mcp-hosts/README.md** : Nouveau guide complet pour la configuration des hôtes MCP
  - Exemples de configuration pour Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Modèles de configuration JSON pour tous les principaux hôtes
  - Tableau comparatif des types de transports (stdio, SSE/HTTP, WebSocket)
  - Résolution des problèmes de connexion courants
  - Bonnes pratiques de sécurité pour la configuration des hôtes

- **13-mcp-inspector/README.md** : Nouveau guide de débogage pour MCP Inspector
  - Méthodes d’installation (npx, npm global, depuis la source)
  - Connexion aux serveurs via stdio et HTTP/SSE
  - Tests des outils, ressources, et workflows des invites
  - Intégration VS Code avec MCP Inspector
  - Scénarios courants de débogage avec solutions

**Module 04 - Implémentation Pratique**
- **pagination/README.md** : Nouveau guide d’implémentation de pagination
  - Modèles de pagination par curseur en Python, TypeScript, Java
  - Gestion de la pagination côté client
  - Stratégies de conception des curseurs (opaque vs structuré)
  - Recommandations d’optimisation des performances

**Module 05 - Sujets Avancés**
- **mcp-protocol-features/README.md** : Nouvelle plongée approfondie sur les fonctionnalités du protocole
  - Implémentation des notifications de progression
  - Modèles d’annulation de requête
  - Modèles de ressources avec motifs URI
  - Gestion du cycle de vie du serveur
  - Contrôle du niveau de journalisation
  - Modèles de gestion des erreurs avec codes JSON-RPC

#### Correctifs de Navigation (24+ fichiers mis à jour)

**README des Modules Principaux**
 Inclut désormais des liens vers la première leçon ET le module suivant

**Sous-fichiers 02-Sécurité**
- Les 5 documents de sécurité supplémentaires ont désormais une navigation "Et ensuite"

**Fichiers 09-CaseStudy**
- Tous les fichiers des études de cas ont une navigation séquentielle

**Labs 10-StreamliningAI**
Ajout de la section Et ensuite à la vue d’ensemble du Module 10 et au Module 11

#### Correctifs de Code et de Contenu

**Mises à Jour SDK et Dépendances**
Correction de la version openai vide à `^4.95.0`
Mise à jour du SDK de `^1.8.0` à `>=1.26.0`
Mise à jour des verrous de version mcp à `>=1.26.0`

**Correctifs de Code**
Correction du modèle invalide `gpt-4o-mini` en `gpt-4.1-mini`

**Correctifs de Contenu**
Correction du lien cassé `READMEmd` → `README.md`, correction de l’en-tête du curriculum `Module 1-3` → `Module 0-3`, correction d’un chemin sensible à la casse
Suppression du contenu dupliqué corrompu de l’étude de cas 5

**Améliorations pour Débutants**
Ajout d’une introduction appropriée, d’objectifs d’apprentissage, et de prérequis pour les débutants

#### Mises à Jour du Curriculum

**README principal.md**
- Ajout des entrées 3.12 (Hôtes MCP), 3.13 (Inspecteur MCP), 4.1 (Pagination), 5.16 (Fonctionnalités du Protocole) au tableau du curriculum

**README des Modules**
Ajout des leçons 12 et 13 à la liste des leçons
Ajout de la section Guides Pratiques avec le lien pagination
Ajout des leçons 5.15 (Transport Personnalisé) et 5.16 (Fonctionnalités du Protocole)

**study_guide.md**
- Mise à jour de la carte mentale avec tous les nouveaux sujets : Configuration des hôtes MCP, Inspecteur MCP, Stratégies de Pagination, Plongée approfondie des Fonctionnalités du Protocole

## 28 janvier 2026

### Revue de Conformité de la Spécification MCP 2025-11-25

#### Amélioration des Concepts de Base (01-CoreConcepts/)
- **Nouveau Primitif Client - Roots** : Ajout d’une documentation complète sur le primitif client Roots, permettant aux serveurs de comprendre les limites du système de fichiers et les permissions d’accès
- **Annotations des Outils** : Ajout de documentation sur les annotations comportementales d’outils (`readOnlyHint`, `destructiveHint`) pour de meilleures décisions d’exécution d’outils
- **Appels d’Outils dans l’Échantillonnage** : Mise à jour de la documentation Sampling pour inclure les paramètres `tools` et `toolChoice` pour l’invocation d’outils pilotée par le modèle durant les requêtes d’échantillonnage
- **Mode d’Élicitation d’URL** : Ajout d’une documentation sur l’élicitation basée sur URL pour les interactions web externes initiées par le serveur
- **Tâches (Expérimental)** : Ajout d’une nouvelle section documentant la fonctionnalité expérimentale Tasks pour des wrappers d’exécution durables et la récupération différée des résultats

- **Support des icônes** : Remarqué que les outils, ressources, modèles de ressources et invites peuvent désormais inclure des icônes en tant que métadonnées supplémentaires

#### Mises à jour de la documentation
- **README.md** : Ajout de la référence à la version de la spécification MCP 2025-11-25 et explication de la gestion des versions par date
- **study_guide.md** : Mise à jour de la carte curriculaire pour inclure les tâches et annotations d'outils dans la section Concepts fondamentaux ; mise à jour de la date du document

#### Vérification de la conformité à la spécification
- **Version du protocole** : Vérification que toute la documentation référence la spécification MCP 2025-11-25 actuelle
- **Alignement architectural** : Confirmation de la précision de la documentation sur l’architecture à deux couches (couche données + couche transport)
- **Documentation des primitives** : Validation des primitives serveur (Ressources, Invites, Outils) et primitives client (Échantillonnage, Élicitation, Journalisation, Racines)
- **Mécanismes de transport** : Vérification de la précision de la documentation pour les transports STDIO et HTTP en flux
- **Conseils de sécurité** : Confirmation de l’alignement avec la documentation actuelle des meilleures pratiques de sécurité MCP

#### Principales fonctionnalités MCP 2025-11-25 documentées
- **Découverte OpenID Connect** : Découverte du serveur d’authentification via OIDC
- **Documents de métadonnées OAuth Client ID** : Mécanisme recommandé d’enregistrement des clients
- **JSON Schema 2020-12** : Dialecte par défaut pour les définitions de schéma MCP
- **Système de niveau SDK** : Formalisation des exigences de support et maintenance des fonctionnalités SDK
- **Structure de gouvernance** : Formalisation des groupes de travail et groupes d’intérêt dans la gouvernance MCP

### Mise à jour majeure de la documentation sécurité (02-Security/)

#### Intégration du workshop MCP Security Summit (Sherpa)
- **Nouvelle ressource de formation pratique** : Ajout d’une intégration complète avec le [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) dans toute la documentation sécurité
- **Couverture de la route de l’expédition** : Documentation complète de la progression camp à camp du camp de base au sommet
- **Alignement OWASP** : Tous les conseils de sécurité correspondent désormais aux risques du guide Azure Security Guide OWASP MCP

#### Intégration OWASP MCP Top 10
- **Nouvelle section** : Ajout d’un tableau des risques de sécurité OWASP MCP Top 10 avec les mesures d’atténuation Azure dans le README de sécurité principal
- **Documentation axée sur les risques** : Mise à jour de mcp-security-controls-2025.md avec références OWASP MCP pour chaque domaine de sécurité
- **Architecture de référence** : Lien vers l'architecture de référence et les modèles d’implémentation du guide Azure Security Guide OWASP MCP

#### Fichiers sécurité mis à jour
- **README.md** : Ajout de la présentation du workshop Sherpa, tableau de la route de l’expédition, résumé des risques OWASP MCP Top 10, section formation pratique
- **mcp-security-controls-2025.md** : Mise à jour de l’en-tête à février 2026, ajout des références aux risques OWASP (MCP01-MCP08), correction de l’incohérence de version de la spécification
- **mcp-security-best-practices-2025.md** : Ajout de la section ressources Sherpa et OWASP, mise à jour de la date
- **mcp-best-practices.md** : Ajout de la section formation pratique avec liens Sherpa et OWASP
- **azure-content-safety-implementation.md** : Ajout de la référence OWASP MCP06, alignement avec Sherpa Camp 3, section ressources supplémentaires

#### Nouveaux liens de ressources ajoutés
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Pages individuelles de risques OWASP MCP (MCP01-MCP10)

### Alignement sur la spécification MCP 2025-11-25 dans tout le curriculum

#### Module 03 - Premiers pas
- **Documentation SDK** : Ajout de Go SDK à la liste officielle des SDK ; mise à jour de toutes les références SDK pour alignement avec la spécification MCP 2025-11-25
- **Clarification sur le transport** : Mise à jour des descriptions des transports STDIO et HTTP Streaming avec références explicites à la spécification

#### Module 04 - Mise en œuvre pratique
- **Mises à jour SDK** : Ajout de Go SDK ; mise à jour de la liste SDK avec référence à la version de la spécification
- **Spécification d’autorisation** : Mise à jour du lien vers la spécification MCP Authorization à la version actuelle 2025-11-25

#### Module 05 - Sujets avancés
- **Nouvelles fonctionnalités** : Ajout d’une note concernant les nouvelles fonctionnalités de la spécification MCP 2025-11-25 (Tâches, annotations d’outils, élicitation en mode URL, racines)
- **Ressources de sécurité** : Ajout des liens OWASP MCP Top 10 et workshop Sherpa aux références supplémentaires

#### Module 06 - Contributions de la communauté
- **Liste SDK** : Ajout des SDK Swift et Rust ; mise à jour du lien de spécification à 2025-11-25
- **Référence de spécification** : Mise à jour du lien vers la spécification MCP vers l’URL directe de la spécification

#### Module 07 - Leçons issues des premières utilisations
- **Mises à jour ressources** : Ajout du lien vers la spécification MCP 2025-11-25 et OWASP MCP Top 10 aux ressources supplémentaires

#### Module 08 - Meilleures pratiques
- **Version de la spécification** : Mise à jour de la référence à la spécification MCP à 2025-11-25
- **Ressources de sécurité** : Ajout des OWASP MCP Top 10 et workshop Sherpa aux références supplémentaires

#### Module 10 - Rationalisation des flux de travail IA
- **Mise à jour du badge** : Changement du badge de version MCP de la version SDK (1.9.3) à la version de spécification (2025-11-25)
- **Liens ressources** : Mise à jour du lien vers la spécification MCP ; ajout de OWASP MCP Top 10

#### Module 11 - Labs pratiques MCP Server
- **Référence de spécification** : Mise à jour du lien vers la spécification MCP à la version 2025-11-25
- **Ressources de sécurité** : Ajout de OWASP MCP Top 10 aux ressources officielles

## 18 décembre 2025

### Mise à jour de la documentation de sécurité - Spécification MCP 2025-11-25

#### Meilleures pratiques de sécurité MCP (02-Security/mcp-best-practices.md) - Mise à jour de la version de spécification
- **Mise à jour de la version du protocole** : Passage à la dernière spécification MCP 2025-11-25 (sortie le 25 novembre 2025)
  - Mise à jour de toutes les références de version de la spécification de 2025-06-18 à 2025-11-25
  - Mise à jour des références de date du document de 18 août 2025 à 18 décembre 2025
  - Vérification que toutes les URL de spécifications pointent vers la documentation actuelle
- **Validation du contenu** : Validation complète des meilleures pratiques de sécurité par rapport aux normes les plus récentes
  - **Solutions de sécurité Microsoft** : Vérification de la terminologie actuelle et des liens pour Prompt Shields (précédemment "détection des risques de jailbreak"), Azure Content Safety, Microsoft Entra ID, et Azure Key Vault
  - **Sécurité OAuth 2.1** : Confirmation de l’alignement avec les meilleures pratiques de sécurité OAuth les plus récentes
  - **Normes OWASP** : Validation de la pertinence des références OWASP Top 10 pour les LLM
  - **Services Azure** : Vérification de tous les liens Microsoft Azure documentation et meilleures pratiques
- **Alignement avec les normes** : Confirmation de l’actualité de toutes les normes de sécurité référencées
  - Cadre de gestion des risques IA NIST
  - ISO 27001:2022
  - Meilleures pratiques de sécurité OAuth 2.1
  - Cadres de sécurité et conformité Azure
- **Ressources d’implémentation** : Validation de tous les liens des guides d’implémentation et ressources
  - Modèles d’authentification Azure API Management
  - Guides d’intégration Microsoft Entra ID
  - Gestion des secrets Azure Key Vault
  - Pipelines DevSecOps et solutions de monitoring

### Assurance qualité de la documentation
- **Conformité à la spécification** : Garantie que toutes les exigences de sécurité MCP obligatoires (DOIT/DOIT PAS) respectent la dernière spécification
- **Actualité des ressources** : Vérification de tous les liens externes vers la documentation Microsoft, normes de sécurité et guides d’implémentation
- **Couverture des meilleures pratiques** : Confirmation de la couverture complète de l’authentification, de l’autorisation, des menaces spécifiques IA, de la sécurité de la chaîne logistique, et des modèles en entreprise

## 6 octobre 2025

### Expansion de la section Premiers pas – Utilisation avancée du serveur & authentification simple

#### Utilisation avancée du serveur (03-GettingStarted/10-advanced)
- **Nouveau chapitre ajouté** : Introduction d’un guide complet sur l’utilisation avancée des serveurs MCP, couvrant les architectures serveur régulières et bas niveau.
  - **Serveur régulier vs bas niveau** : Comparaison détaillée et exemples de code en Python et TypeScript pour les deux approches.
  - **Conception basée sur gestionnaires** : Explication de la gestion des outils/ressources/invites basée sur des gestionnaires pour des implémentations serveur évolutives et flexibles.
  - **Modèles pratiques** : Scénarios réels où les modèles serveur bas niveau sont bénéfiques pour les fonctionnalités avancées et l’architecture.

#### Authentification simple (03-GettingStarted/11-simple-auth)
- **Nouveau chapitre ajouté** : Guide pas à pas pour la mise en œuvre d’une authentification simple dans les serveurs MCP.
  - **Concepts d’authentification** : Explication claire entre authentification et autorisation, et gestion des identifiants.
  - **Implémentation d’authentification basique** : Modèles de middleware d’authentification en Python (Starlette) et TypeScript (Express), avec exemples de code.
  - **Progression vers la sécurité avancée** : Conseils pour débuter avec une authentification simple et évoluer vers OAuth 2.1 et RBAC, avec références aux modules de sécurité avancée.

Ces ajouts offrent des conseils pratiques et concrets pour construire des implémentations MCP serveurs plus robustes, sécurisées et flexibles, faisant le lien entre concepts fondamentaux et modèles avancés de production.

## 29 septembre 2025

### Labs d’intégration de base de données MCP Server – Parcours d’apprentissage pratique complet

#### 11-MCPServerHandsOnLabs - Nouveau curriculum complet d’intégration de base de données
- **Parcours complet de 13 labs** : Ajout d’un curriculum pratique complet pour construire des serveurs MCP prêts pour la production avec intégration de base PostgreSQL
  - **Implémentation réelle** : Cas d’usage analytique Zava Retail démontrant des modèles d’entreprise
  - **Progression d’apprentissage structurée** :
    - **Labs 00-03 : Fondations** - Introduction, architecture centrale, sécurité & multi-tenancy, mise en place de l’environnement
    - **Labs 04-06 : Construction du serveur MCP** - Conception et schéma de base de données, implémentation du serveur MCP, développement des outils  
    - **Labs 07-09 : Fonctionnalités avancées** - Intégration de recherche sémantique, tests & débogage, intégration VS Code
    - **Labs 10-12 : Production & meilleures pratiques** - Stratégies de déploiement, monitoring & observabilité, bonnes pratiques & optimisation
  - **Technologies d’entreprise** : Framework FastMCP, PostgreSQL avec pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Fonctionnalités avancées** : Sécurité au niveau des lignes (RLS), recherche sémantique, accès aux données multi-locataires, embeddings vectoriels, monitoring en temps réel

#### Standardisation terminologique – Conversion de module à lab
- **Mise à jour complète de la documentation** : Mise à jour systématique de tous les fichiers README du dossier 11-MCPServerHandsOnLabs pour utiliser la terminologie "Lab" au lieu de "Module"
  - **En-têtes de sections** : Mise à jour de "What This Module Covers" à "What This Lab Covers" dans les 13 labs
  - **Descriptions de contenu** : Changement de "This module provides..." à "This lab provides..." dans toute la documentation
  - **Objectifs d’apprentissage** : Mise à jour de "By the end of this module..." à "By the end of this lab..."
  - **Liens de navigation** : Conversion de toutes les références "Module XX :" à "Lab XX :" dans les références croisées et navigation
  - **Suivi d’achèvement** : Mise à jour de "After completing this module..." à "After completing this lab..."
  - **Références techniques inchangées** : Maintien des références de module Python dans les fichiers de configuration (ex. `"module": "mcp_server.main"`)

#### Amélioration du guide d’étude (study_guide.md)
- **Carte curriculaire visuelle** : Ajout de la nouvelle section "11. Database Integration Labs" avec visualisation détaillée de la structure des labs
- **Structure du dépôt** : Mise à jour de dix à onze sections principales avec description détaillée de 11-MCPServerHandsOnLabs
- **Orientation du parcours d’apprentissage** : Amélioration des instructions de navigation couvrant les sections 00-11
- **Couverture technologique** : Ajout des détails sur FastMCP, PostgreSQL, intégration des services Azure
- **Résultats d’apprentissage** : Mise en avant du développement de serveurs prêts pour la production, des modèles d’intégration de base de données et de la sécurité en entreprise

#### Amélioration de la structure du README principal
- **Terminologie basée sur les labs** : Mise à jour du README.md principal dans 11-MCPServerHandsOnLabs pour l’usage cohérent de la structure "Lab"
- **Organisation du parcours d’apprentissage** : Progression claire des concepts fondamentaux à l’implémentation avancée jusqu’au déploiement en production
- **Orientation pratique** : Accent mis sur l’apprentissage pratique avec modèles et technologies d’entreprise

### Améliorations de la qualité & de la cohérence de la documentation
- **Accent sur l’apprentissage pratique** : Renforcement de l’approche pratique basée sur les labs dans toute la documentation
- **Focus sur les modèles d’entreprise** : Mise en avant des implémentations prêtes pour la production et des considérations de sécurité en entreprise
- **Intégration technologique** : Couverture complète des services Azure modernes et des modèles d’intégration IA
- **Progression d’apprentissage** : Parcours clair et structuré des concepts de base jusqu’au déploiement en production

## 26 septembre 2025

### Amélioration des études de cas – Intégration du registre MCP GitHub

#### Études de cas (09-CaseStudy/) - Focus développement écosystémique
- **README.md** : Extension majeure avec étude de cas complète du registre MCP GitHub
  - **Étude de cas du registre MCP GitHub** : Nouvelle étude complète examinant le lancement du registre MCP GitHub en septembre 2025
    - **Analyse du problème** : Examen détaillé des défis de découverte et déploiement fragmentés des serveurs MCP
    - **Architecture de la solution** : Approche centralisée du registre GitHub avec installation VS Code en un clic
    - **Impact commercial** : Améliorations mesurables de l’intégration et de la productivité des développeurs
    - **Valeur stratégique** : Focus sur le déploiement modulaire des agents et l’interopérabilité multi-outils
    - **Développement de l’écosystème** : Positionnement comme plateforme fondamentale pour l’intégration agentique
  - **Structure améliorée de l’étude de cas** : Mise à jour cohérente des sept études de cas avec formatage et descriptions complètes
    - Agents de voyage Azure AI : Accent sur l’orchestration multi-agents
    - Intégration Azure DevOps : Focus sur l’automatisation des workflows
    - Récupération documentaire en temps réel : Implémentation client console Python
    - Générateur interactif de plans d’étude : Application web conversationnelle Chainlit

    - Documentation dans l’Éditeur : Intégration de VS Code et GitHub Copilot
    - Gestion des API Azure : Modèles d’intégration API d’entreprise
    - Registre GitHub MCP : Développement de l’écosystème et plateforme communautaire
  - **Conclusion Complète** : Section de conclusion réécrite mettant en valeur sept études de cas couvrant plusieurs dimensions d’implémentation MCP
    - Intégration d’Entreprise, Orchestration Multi-Agent, Productivité des Développeurs
    - Développement de l’Écosystème, Catégorisation des Applications Éducatives
    - Perspectives améliorées sur les modèles architecturaux, stratégies d’implémentation et meilleures pratiques
    - Accent sur le MCP comme protocole mature prêt pour la production

#### Mises à jour du Guide d’Étude (study_guide.md)
- **Carte Visuelle du Curriculum** : Mindmap mise à jour pour inclure le Registre GitHub MCP dans la section Études de Cas
- **Description des Études de Cas** : Améliorée, passant de descriptions génériques à une analyse détaillée de sept études de cas complètes
- **Structure du Dépôt** : Section 10 mise à jour pour refléter la couverture complète des études de cas avec des détails d’implémentation spécifiques
- **Intégration du Changelog** : Ajout de l’entrée du 26 septembre 2025 documentant l’ajout du Registre GitHub MCP et les améliorations des études de cas
- **Mises à jour des Dates** : Timestamp du pied de page mis à jour pour refléter la dernière révision (26 septembre 2025)

### Améliorations de la Qualité de la Documentation
- **Renforcement de la Cohérence** : Formatage et structure des études de cas standardisés sur les sept exemples
- **Couverture Complète** : Études de cas couvrant désormais les scénarios d’entreprise, de productivité développeur et de développement d’écosystème
- **Positionnement Stratégique** : Accent renforcé sur MCP comme plateforme fondamentale pour le déploiement des systèmes agents
- **Intégration des Ressources** : Ressources supplémentaires mises à jour pour inclure le lien vers le Registre GitHub MCP

## 15 septembre 2025

### Extension des Sujets Avancés - Transports Personnalisés & Ingénierie du Contexte

#### Transports Personnalisés MCP (05-AdvancedTopics/mcp-transport/) - Nouveau Guide d’Implémentation Avancée
- **README.md** : Guide complet d’implémentation des mécanismes de transport MCP personnalisés
  - **Transport Azure Event Grid** : Implémentation complète de transport serveurless basé sur les événements
    - Exemples en C#, TypeScript et Python avec intégration Azure Functions
    - Modèles d’architecture événementielle pour solutions MCP scalables
    - Récepteurs Webhook et gestion des messages par poussée
  - **Transport Azure Event Hubs** : Implémentation du transport de streaming à haut débit
    - Capacités de streaming en temps réel pour scénarios à faible latence
    - Stratégies de partitionnement et gestion des points de contrôle
    - Regroupement des messages et optimisation des performances
  - **Modèles d’Intégration d’Entreprise** : Exemples architecturaux prêts pour la production
    - Traitement MCP distribué à travers plusieurs Azure Functions
    - Architectures de transport hybrides combinant plusieurs types de transport
    - Stratégies de durabilité, fiabilité et gestion des erreurs des messages
  - **Sécurité & Surveillance** : Intégration Azure Key Vault et modèles d’observabilité
    - Authentification par identité gérée et accès au moindre privilège
    - Télémétrie Application Insights et surveillance des performances
    - Coupe-circuits et modèles de tolérance aux pannes
  - **Cadres de Test** : Stratégies complètes de test pour transports personnalisés
    - Tests unitaires avec mock et doubles de test
    - Tests d’intégration avec Azure Test Containers
    - Considérations sur les tests de performance et de charge

#### Ingénierie du Contexte (05-AdvancedTopics/mcp-contextengineering/) - Discipline IA Émergente
- **README.md** : Exploration complète de l’ingénierie du contexte comme domaine émergent
  - **Principes Fondamentaux** : Partage complet du contexte, prise de décision basée sur actions, gestion de la fenêtre de contexte
  - **Alignement avec le Protocole MCP** : Comment la conception MCP répond aux défis de l’ingénierie du contexte
    - Limitations de la fenêtre de contexte et stratégies de chargement progressif
    - Détermination de la pertinence et récupération dynamique du contexte
    - Gestion multimodale du contexte et considérations de sécurité
  - **Approches d’Implémentation** : Architectures mono-thread vs multi-agent
    - Techniques de découpage et priorisation du contexte
    - Chargement progressif et stratégies de compression du contexte
    - Approches en couches du contexte et optimisation de la récupération
  - **Cadre de Mesure** : Métriques émergentes pour l’évaluation de l’efficacité du contexte
    - Efficacité de l’entrée, performance, qualité et expérience utilisateur
    - Approches expérimentales à l’optimisation du contexte
    - Analyse des échecs et méthodologies d’amélioration

#### Mises à jour de la Navigation du Curriculum (README.md)
- **Structure de Module Améliorée** : Tableau de curriculum mis à jour pour inclure les nouveaux sujets avancés
  - Ajout des entrées Ingénierie du Contexte (5.14) et Transport Personnalisé (5.15)
  - Formatage cohérent et liens de navigation dans tous les modules
  - Descriptions actualisées pour refléter la portée actuelle du contenu

### Améliorations de la Structure des Dossiers
- **Normalisation des Noms** : Renommage de "mcp transport" en "mcp-transport" pour cohérence avec les autres dossiers de sujets avancés
- **Organisation du Contenu** : Tous les dossiers 05-AdvancedTopics suivent désormais un schéma de nommage cohérent (mcp-[sujet])

### Améliorations de la Qualité de la Documentation
- **Alignement avec la Spécification MCP** : Tous les nouveaux contenus font référence à la Spécification MCP actuelle 2025-06-18
- **Exemples Multilingues** : Exemples de code complets en C#, TypeScript et Python
- **Orientation Entreprise** : Modèles prêts pour la production et intégration cloud Azure
- **Documentation Visuelle** : Diagrammes Mermaid pour visualisation d’architecture et de flux

## 18 août 2025

### Mise à jour Complète de la Documentation - Normes MCP 2025-06-18

#### Bonnes Pratiques de Sécurité MCP (02-Security/) - Modernisation Complète
- **MCP-SECURITY-BEST-PRACTICES-2025.md** : Réécriture complète alignée avec la Spécification MCP 2025-06-18
  - **Exigences Obligatoires** : Ajout des exigences MUST/MUST NOT explicites de la spécification officielle avec indicateurs visuels clairs
  - **12 Pratiques Clés de Sécurité** : Restructuration d’une liste de 15 points en domaines de sécurité complets
    - Sécurité des Jetons & Authentification avec intégration fournisseur d’identité externe
    - Gestion de Session & Sécurité du Transport avec exigences cryptographiques
    - Protection contre Menaces Spécifiques IA avec intégration Microsoft Prompt Shields
    - Contrôle d’Accès & Permissions avec principe du moindre privilège
    - Sécurité du Contenu & Surveillance avec intégration Azure Content Safety
    - Sécurité de la Chaîne d’Approvisionnement avec vérification complète des composants
    - Sécurité OAuth & Prévention des Confused Deputy avec mise en œuvre PKCE
    - Réponse aux Incidents & Récupération avec capacités automatisées
    - Conformité & Gouvernance avec alignement réglementaire
    - Contrôles de Sécurité Avancés avec architecture zero trust
    - Intégration de l’Écosystème de Sécurité Microsoft avec solutions complètes
    - Évolution Continue de la Sécurité avec pratiques adaptatives
  - **Solutions de Sécurité Microsoft** : Guide d’intégration amélioré pour Prompt Shields, Azure Content Safety, Entra ID, et GitHub Advanced Security
  - **Ressources d’Implémentation** : Liens de ressources classifiés par Documentation Officielle MCP, Solutions Microsoft, Normes de Sécurité et Guides d’Implémentation

#### Contrôles de Sécurité Avancés (02-Security/) - Implémentation Entreprise
- **MCP-SECURITY-CONTROLS-2025.md** : Refonte complète avec cadre de sécurité niveau entreprise
  - **9 Domaines de Sécurité Complets** : Extension des contrôles basiques vers un cadre détaillé pour entreprise
    - Authentification & Autorisation Avancées avec intégration Microsoft Entra ID
    - Sécurité des Jetons & Contrôles Anti-Passthrough avec validation complète
    - Contrôles de Sécurité des Sessions avec prévention du détournement
    - Contrôles Spécifiques IA avec prévention d’injection de prompt et empoisonnement d’outils
    - Prévention des Attaques Confused Deputy avec sécurité proxy OAuth
    - Sécurité d’Exécution des Outils avec sandboxing et isolation
    - Contrôles de Sécurité de la Chaîne d’Approvisionnement avec vérification des dépendances
    - Contrôles de Surveillance & Détection avec intégration SIEM
    - Réponse aux Incidents & Récupération avec capacités automatisées
  - **Exemples d’Implémentation** : Ajout de blocs de configuration YAML détaillés et exemples de code
  - **Intégration des Solutions Microsoft** : Couverture complète des services de sécurité Azure, GitHub Advanced Security et gestion d’identité entreprise

#### Sécurité des Sujets Avancés (05-AdvancedTopics/mcp-security/) - Implémentation Prête pour la Production
- **README.md** : Réécriture complète pour implémentation sécurité entreprise
  - **Alignement avec Spécification Actuelle** : Mise à jour vers Spécification MCP 2025-06-18 avec exigences de sécurité obligatoires
  - **Authentification Renforcée** : Intégration Microsoft Entra ID avec exemples complets .NET et Java Spring Security
  - **Intégration Sécurité IA** : Mise en œuvre Microsoft Prompt Shields et Azure Content Safety avec exemples détaillés Python
  - **Atténuation Avancée des Menaces** : Exemples complets d’implémentation pour
    - Prévention des Attaques Confused Deputy avec PKCE et validation du consentement utilisateur
    - Prévention du Passthrough de Jeton avec validation d’audience et gestion sécurisée des jetons
    - Prévention du Détournement de Session avec liaison cryptographique et analyse comportementale
  - **Intégration Sécurité Entreprise** : Surveillance Azure Application Insights, pipelines de détection de menaces, et sécurité de la chaîne d’approvisionnement
  - **Checklist d’Implémentation** : Contrôles de sécurité obligatoires vs recommandés clairs avec bénéfices de l’écosystème Microsoft

### Qualité de la Documentation & Alignement des Normes
- **Références de Spécification** : Mise à jour de toutes les références vers la Spécification MCP actuelle 2025-06-18
- **Écosystème de Sécurité Microsoft** : Guide d’intégration amélioré dans toute la documentation de sécurité
- **Implémentation Pratique** : Ajout d’exemples de code détaillés en .NET, Java et Python avec modèles entreprise
- **Organisation des Ressources** : Catégorisation complète des documents officiels, normes de sécurité, et guides d’implémentation
- **Indicateurs Visuels** : Marquage clair des exigences obligatoires vs pratiques recommandées


#### Concepts Clés (01-CoreConcepts/) - Modernisation Complète
- **Mise à jour de la Version du Protocole** : Mise à jour pour référencer la Spécification MCP actuelle 2025-06-18 avec versionnement basé sur la date (format AAAA-MM-JJ)
- **Affinement de l’Architecture** : Descriptions améliorées des Hôtes, Clients et Serveurs pour refléter les modèles architecturaux MCP actuels
  - Les Hôtes sont maintenant clairement définis comme applications IA coordonnant plusieurs connexions clients MCP
  - Les Clients sont décrits comme connecteurs de protocole maintenant des relations serveur un-à-un
  - Les Serveurs sont améliorés avec scénarios de déploiement local vs distant
- **Restructuration des Primitives** : Remaniement complet des primitives serveur et client
  - Primitives Serveur : Ressources (sources de données), Prompts (modèles), Outils (fonctions exécutables) avec explications détaillées et exemples
  - Primitives Client : Échantillonnage (complétions LLM), Élicitation (entrée utilisateur), Journalisation (débogage/surveillance)
  - Mise à jour avec modèles actuels de méthodes de découverte (`*/list`), récupération (`*/get`), et exécution (`*/call`)
- **Architecture du Protocole** : Introduction d’un modèle d’architecture à deux couches
  - Couche Données : Fondation JSON-RPC 2.0 avec gestion du cycle de vie et primitives
  - Couche Transport : STDIO (local) et HTTP Streamable avec SSE (transport distant)
- **Cadre de Sécurité** : Principes de sécurité complets incluant consentement utilisateur explicite, protection de la vie privée des données, sécurité d’exécution des outils, et sécurité de la couche transport
- **Modèles de Communication** : Messages du protocole mis à jour pour montrer initialisation, découverte, exécution, et flux de notification
- **Exemples de Code** : Exemples multilingues rafraîchis (.NET, Java, Python, JavaScript) pour refléter les modèles SDK MCP actuels

#### Sécurité (02-Security/) - Refonte Complète de la Sécurité  
- **Alignement aux Normes** : Alignement complet avec les exigences de sécurité de la Spécification MCP 2025-06-18
- **Évolution de l’Authentification** : Documentation de l’évolution des serveurs OAuth custom vers délégation fournisseur d’identité externe (Microsoft Entra ID)
- **Analyse des Menaces Spécifiques IA** : Couverture renforcée des vecteurs d’attaque modernes en IA
  - Scénarios détaillés d’attaques par injection de prompt avec exemples concrets
  - Mécanismes d’empoisonnement d’outils et modèles d’attaques « rug pull »
  - Empoisonnement de la fenêtre de contexte et attaques de confusion de modèle
- **Solutions de Sécurité IA Microsoft** : Couverture complète de l’écosystème de sécurité Microsoft
  - AI Prompt Shields avec détection avancée, mise en lumière et techniques de délimitation
  - Modèles d’intégration Azure Content Safety
  - GitHub Advanced Security pour la protection de la chaîne d’approvisionnement
- **Atténuation des Menaces Avancées** : Contrôles de sécurité détaillés pour
  - Détournement de sessions avec scénarios d’attaque spécifiques MCP et exigences sur ID de session cryptographique
  - Problèmes Confused Deputy en scénarios proxy MCP avec exigences explicites de consentement
  - Vulnérabilités Passthrough de jeton avec contrôles de validation obligatoires
- **Sécurité de la Chaîne d’Approvisionnement** : Extension de la couverture sur la chaîne d’approvisionnement IA incluant modèles fondamentaux, services d’embeddings, fournisseurs de contexte et API tierces
- **Sécurité Fondamentale** : Intégration renforcée avec modèles de sécurité entreprise incluant architecture zero trust et écosystème Microsoft de sécurité
- **Organisation des Ressources** : Liens complets classifiés par type (Docs Officiels, Normes, Recherches, Solutions Microsoft, Guides d’Implémentation)

### Améliorations de la Qualité de la Documentation
- **Objectifs d’Apprentissage Structurés** : Objectifs d’apprentissage améliorés avec résultats spécifiques et actionnables 
- **Références Croisées** : Ajout de liens entre sujets liés à la sécurité et aux concepts clés
- **Informations à Jour** : Références de date et liens de spécification mis à jour selon les normes actuelles
- **Guide d’Implémentation** : Ajout de directives spécifiques et actionnables dans les deux sections

## 16 juillet 2025

### Améliorations du README et de la Navigation
- Navigation du curriculum entièrement repensée dans README.md
- Remplacement des balises `<details>` par un format plus accessible basé sur les tableaux
- Création d’options de mise en page alternatives dans le nouveau dossier "alternative_layouts"
- Ajout d’exemples de navigation sous forme de cartes, onglets, et accordéons
- Mise à jour de la section structure du dépôt pour inclure tous les fichiers récents
- Amélioration de la section "Comment utiliser ce curriculum" avec recommandations claires
- Mise à jour des liens de spécification MCP pour pointer vers les URLs correctes
- Ajout de la section Ingénierie du Contexte (5.14) dans la structure du curriculum

### Mises à jour du Guide d’Étude
- Guide d’étude complètement révisé pour s’aligner sur la structure actuelle du dépôt
- Ajout de nouvelles sections pour Clients et Outils MCP, et Serveurs MCP Populaires
- Mise à jour de la Carte Visuelle du Curriculum pour refléter avec précision tous les sujets
- Amélioration des descriptions des Sujets Avancés pour couvrir toutes les zones spécialisées
- Mise à jour de la section Études de Cas pour refléter les exemples réels
- Ajout de ce changelog complet

### Contributions Communautaires (06-CommunityContributions/)
- Ajout d’informations détaillées sur les serveurs MCP pour génération d’images
- Ajout d’une section complète sur l’utilisation de Claude dans VSCode
- Ajout des instructions d’installation et d’utilisation du client terminal Cline
- Mise à jour de la section clients MCP pour inclure toutes les options populaires
- Amélioration des exemples de contribution avec des échantillons de code plus précis

### Sujets Avancés (05-AdvancedTopics/)
- Organisation de tous les dossiers de sujets spécialisés avec un nommage cohérent
- Ajout de matériaux et exemples d’ingénierie du contexte
- Ajout de documentation d’intégration agent Foundry
- Amélioration de la documentation d’intégration sécuritaire Entra ID

## 11 juin 2025

### Création Initiale
- Publication de la première version du curriculum MCP pour débutants

- Création de la structure de base pour les 10 sections principales
- Mise en place de la carte de parcours visuelle pour la navigation
- Ajout des projets exemples initiaux en plusieurs langages de programmation

### Démarrage (03-GettingStarted/)
- Création des premiers exemples d’implémentation serveur
- Ajout des conseils pour le développement client
- Inclusion des instructions d’intégration du client LLM
- Ajout de la documentation d’intégration de VS Code
- Mise en place des exemples serveur Server-Sent Events (SSE)

### Concepts de base (01-CoreConcepts/)
- Ajout d’une explication détaillée de l’architecture client-serveur
- Création de la documentation sur les composants clés du protocole
- Documentation des modèles de messagerie dans MCP

## 23 mai 2025

### Structure du dépôt
- Initialisation du dépôt avec une structure de dossiers basique
- Création des fichiers README pour chaque section majeure
- Mise en place de l’infrastructure de traduction
- Ajout des ressources visuelles et des diagrammes

### Documentation
- Création du README.md initial avec aperçu du programme
- Ajout de CODE_OF_CONDUCT.md et SECURITY.md
- Mise en place de SUPPORT.md avec les conseils pour obtenir de l’aide
- Création de la structure préliminaire du guide d’étude

## 15 avril 2025

### Planification et cadre
- Planification initiale du cursus MCP pour débutants
- Définition des objectifs d’apprentissage et du public cible
- Esquisse de la structure en 10 sections du cursus
- Élaboration du cadre conceptuel pour les exemples et études de cas
- Création des prototypes initiaux d’exemples pour les concepts clés

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->