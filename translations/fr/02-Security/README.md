# Sécurité MCP : Protection complète pour les systèmes d'IA

[![Meilleures pratiques de sécurité MCP](../../../translated_images/fr/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

La sécurité est fondamentale dans la conception des systèmes d'IA, c'est pourquoi nous la privilégions comme notre deuxième section. Cela s'aligne avec le principe **Secure by Design** de Microsoft issu de la [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Le Model Context Protocol (MCP) apporte de nouvelles capacités puissantes aux applications pilotées par l'IA tout en introduisant des défis de sécurité uniques qui vont au-delà des risques traditionnels liés aux logiciels. Les systèmes MCP font face à la fois à des soucis de sécurité établis (codage sécurisé, moindre privilège, sécurité de la chaîne d'approvisionnement) et à de nouvelles menaces spécifiques à l'IA, incluant l'injection de prompt, l'empoisonnement d'outils, le détournement de session, les attaques de deputy confus, les vulnérabilités de passage de jeton et la modification dynamique des capacités.

Cette leçon explore les risques de sécurité les plus critiques dans les implémentations MCP—couvrant l'authentification, l'autorisation, les permissions excessives, l'injection de prompt indirecte, la sécurité des sessions, les problèmes de deputy confus, la gestion des jetons, et les vulnérabilités de la chaîne d'approvisionnement. Vous apprendrez des contrôles actionnables et des meilleures pratiques pour atténuer ces risques tout en tirant parti des solutions Microsoft telles que Prompt Shields, Azure Content Safety et GitHub Advanced Security pour renforcer votre déploiement MCP.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- **Identifier les menaces spécifiques au MCP** : Reconnaître les risques uniques en matière de sécurité dans les systèmes MCP, incluant l'injection de prompt, l'empoisonnement d'outils, les permissions excessives, le détournement de session, les problèmes de deputy confus, les vulnérabilités de passage de jeton, et les risques liés à la chaîne d'approvisionnement
- **Appliquer des contrôles de sécurité** : Mettre en œuvre des mesures d'atténuation efficaces incluant une authentification robuste, un accès au moindre privilège, une gestion sécurisée des jetons, des contrôles de sécurité des sessions, et la vérification de la chaîne d'approvisionnement
- **Exploiter les solutions de sécurité Microsoft** : Comprendre et déployer Microsoft Prompt Shields, Azure Content Safety et GitHub Advanced Security pour la protection des charges de travail MCP
- **Valider la sécurité des outils** : Reconnaître l'importance de la validation des métadonnées des outils, la surveillance des modifications dynamiques, et la défense contre les attaques d'injection de prompt indirectes
- **Intégrer les meilleures pratiques** : Combiner les fondamentaux de la sécurité établis (codage sécurisé, durcissement des serveurs, zéro confiance) avec les contrôles spécifiques au MCP pour une protection complète

# Architecture et contrôles de sécurité MCP

Les implémentations modernes du MCP nécessitent des approches de sécurité en couches qui traitent à la fois la sécurité logicielle traditionnelle et les menaces spécifiques à l'IA. La spécification MCP en rapide évolution continue de faire mûrir ses contrôles de sécurité, permettant une meilleure intégration avec les architectures de sécurité d'entreprise et les meilleures pratiques établies.

Des recherches issues du [Microsoft Digital Defense Report](https://aka.ms/mddr) démontrent que **98 % des violations signalées seraient évitées par une hygiène de sécurité rigoureuse**. La stratégie de protection la plus efficace combine des pratiques de sécurité fondamentales avec des contrôles spécifiques au MCP — les mesures de sécurité de base éprouvées restent les plus impactantes pour réduire le risque global de sécurité.

## Paysage actuel de la sécurité

> **Note :** Ce chapitre combine les contrôles de sécurité MCP établis avec les
> directives d'autorisation actuelles de la **Spécification MCP 2026-07-28**.
> Référez-vous toujours à la [Spécification MCP](https://modelcontextprotocol.io/specification/2026-07-28/),
> au [référentiel GitHub MCP](https://github.com/modelcontextprotocol), et à la
> [documentation des meilleures pratiques de sécurité](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> lors de la mise en œuvre de code sensible à la sécurité.

> **Mise à jour d'autorisation :** Le `2026-07-28` MCP exige que les clients valident le
> paramètre `iss` dans les réponses d'autorisation (RFC 9207) et associent les
> identifiants enregistrés au serveur d'autorisation émetteur. L'enregistrement dynamique des clients
> est déprécié ; les nouvelles implémentations doivent utiliser des documents de métadonnées Client ID.
> Voir [Quoi de neuf dans MCP : La spécification 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> pour la liste complète des changements d'autorisation.

## 🏔️ Atelier MCP Security Summit (Sherpa)

Pour une **formation pratique en sécurité**, nous recommandons vivement l'**Atelier MCP Security Summit** (Sherpa) - une expédition guidée complète pour sécuriser les serveurs MCP dans Microsoft Azure.

### Vue d'ensemble de l'atelier

L'[atelier MCP Security Summit](https://azure-samples.github.io/sherpa/) propose une formation en sécurité pratique et actionnable via une méthodologie éprouvée « vulnérable → exploitation → correction → validation ». Vous allez :

- **Apprendre en cassant** : Expérimenter les vulnérabilités de première main en exploitant des serveurs intentionnellement non sécurisés
- **Utiliser la sécurité native d'Azure** : Tirer parti d'Azure Entra ID, Key Vault, API Management et AI Content Safety
- **Suivre la défense en profondeur** : Progresser à travers les camps en construisant des couches complètes de sécurité
- **Appliquer les standards OWASP** : Chaque technique correspond au [Guide de sécurité Azure MCP OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Obtenir du code de production** : Repartir avec des implémentations fonctionnelles et testées

### Parcours de l'expédition

| Camp | Focus | Risques OWASP couverts |
|------|-------|---------------------|
| **Camp de base** | Fondamentaux MCP & vulnérabilités d'authentification | MCP01, MCP07 |
| **Camp 1 : Identité** | OAuth 2.1, identité managée Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Camp 2 : Passerelle** | API Management, points de terminaison privés, gouvernance | MCP02, MCP06, MCP07, MCP09 |
| **Camp 3 : Sécurité I/O** | Injection de prompt, protection PII, sécurité du contenu | MCP03, MCP05, MCP06, MCP10 |
| **Camp 4 : Surveillance** | Log Analytics, tableaux de bord, détection de menaces | MCP04, MCP08 |
| **Le sommet** | Test d'intégration équipe rouge / équipe bleue | Tous |

**Commencer** : [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## Top 10 des risques de sécurité MCP OWASP

Le [Guide de sécurité Azure MCP OWASP](https://microsoft.github.io/mcp-azure-security-guide/) détaille les dix risques de sécurité les plus critiques pour les implémentations MCP :

| Risque | Description | Atténuation Azure |
|------|-------------|------------------|
| **MCP01** | Mauvaise gestion des jetons & exposition des secrets | Azure Key Vault, identité managée |
| **MCP02** | Escalade de privilèges via l'élargissement des scopes | RBAC, accès conditionnel |
| **MCP03** | Empoisonnement d'outils | Validation des outils, vérification d'intégrité |
| **MCP04** | Attaques sur la chaîne d'approvisionnement logicielle & altération des dépendances | GitHub Advanced Security, analyse des dépendances |
| **MCP05** | Injection & exécution de commande | Validation des entrées, sandboxing |
| **MCP06** | Subversion du flux d'intention | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Authentification & autorisation insuffisantes | Azure Entra ID, OAuth 2.1 avec PKCE |
| **MCP08** | Manque d'audit et de télémétrie | Azure Monitor, Application Insights |
| **MCP09** | Serveurs MCP fantômes | Gouvernance API Center, isolation réseau |
| **MCP10** | Injection de contexte & partage excessif | Classification des données, exposition minimale |

### Évolution de l’authentification MCP

La spécification MCP a considérablement évolué dans son approche de l'authentification et de l'autorisation :

- **Approche originale** : Les premières spécifications demandaient aux développeurs d’implémenter des serveurs d'authentification personnalisés, les serveurs MCP agissant en tant que serveurs d’autorisation OAuth 2.0 gérant directement l’authentification utilisateur
- **Norme actuelle (`2026-07-28`)** : Les serveurs MCP peuvent déléguer l’authentification
  à des fournisseurs d’identités externes tels que Microsoft Entra ID. Les clients doivent aussi
  appliquer les exigences actuelles de validation de l’émetteur et de liaison des identifiants.
- **Sécurité de la couche transport** : Support amélioré pour des mécanismes de transport sécurisés avec des schémas d’authentification appropriés pour les connexions locales (STDIO) et distantes (HTTP Streamable)

## Sécurité de l'authentification & de l'autorisation

### Défis de sécurité actuels

Les implémentations modernes du MCP font face à plusieurs défis d'authentification et d'autorisation :

### Risques et vecteurs de menace

- **Logique d'autorisation mal configurée** : Une mise en œuvre défaillante de l'autorisation dans les serveurs MCP peut exposer des données sensibles et appliquer incorrectement les contrôles d’accès
- **Compromission des jetons OAuth** : Le vol local de jetons de serveur MCP permet aux attaquants de se faire passer pour les serveurs et d’accéder aux services en aval
- **Vulnérabilités de passage de jeton** : Une mauvaise gestion des jetons crée des contournements des contrôles de sécurité et des lacunes dans la traçabilité
- **Permissions excessives** : Les serveurs MCP sur-privilégiés violent le principe du moindre privilège et élargissent les surfaces d’attaque

#### Passage de jeton : un anti-pattern critique

**Le passage de jeton est explicitement interdit** dans la spécification d'autorisation MCP en vigueur en raison de graves implications en matière de sécurité :

##### Contournement des contrôles de sécurité
- Les serveurs MCP et les API en aval mettent en œuvre des contrôles critiques (limitation de débit, validation des requêtes, surveillance du trafic) qui dépendent d’une validation correcte des jetons
- L'utilisation directe de jetons client vers API contourne ces protections essentielles, sapant l’architecture de sécurité

##### Défis de responsabilité et d'audit
- Les serveurs MCP ne peuvent pas distinguer les clients utilisant des jetons émis en amont, brisant les pistes de vérification
- Les journaux des serveurs de ressources en aval montrent des origines de requête trompeuses au lieu des véritables intermédiaires des serveurs MCP
- Les enquêtes d'incident et les audits de conformité deviennent beaucoup plus difficiles

##### Risques d'exfiltration de données
- Des revendications de jeton non validées permettent aux acteurs malveillants munis de jetons volés d’utiliser les serveurs MCP comme proxies pour l’exfiltration de données
- Des violations de la frontière de confiance autorisent des modèles d'accès non autorisés qui contournent les contrôles de sécurité prévus

##### Vecteurs d'attaque multi-services
- Des jetons compromis acceptés par plusieurs services permettent des déplacements latéraux à travers les systèmes connectés
- Les hypothèses de confiance entre les services peuvent être violées lorsque l’origine des jetons ne peut être vérifiée

### Contrôles et atténuations de sécurité

**Exigences de sécurité critiques :**

> **OBLIGATOIRE** : Les serveurs MCP **NE DOIVENT PAS** accepter des jetons qui n’ont pas été explicitement émis pour le serveur MCP

#### Contrôles d'authentification et d'autorisation

- **Revue rigoureuse de l'autorisation** : Réaliser des audits complets de la logique d'autorisation des serveurs MCP pour garantir que seuls les utilisateurs et clients intentionnés peuvent accéder aux ressources sensibles
  - **Guide d’implémentation** : [Azure API Management en passerelle d'authentification pour les serveurs MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Intégration d’identité** : [Utilisation de Microsoft Entra ID pour l’authentification des serveurs MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestion sécurisée des jetons** : Mettre en œuvre [les meilleures pratiques Microsoft pour la validation et le cycle de vie des jetons](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Valider que les revendications de l’audience du jeton correspondent à l’identité du serveur MCP
  - Appliquer des politiques adéquates de rotation et d’expiration des jetons
  - Prévenir les attaques par rejeu de jeton et les usages non autorisés

- **Stockage protégé des jetons** : Stocker les jetons en toute sécurité avec chiffrement au repos et en transit
  - **Meilleures pratiques** : [Directives sur le stockage sécurisé et le chiffrement des jetons](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Mise en œuvre du contrôle d’accès

- **Principe du moindre privilège** : Accorder aux serveurs MCP uniquement les permissions minimales requises pour la fonctionnalité souhaitée
  - Revue régulière des permissions et mises à jour pour prévenir l’élargissement des privilèges
  - **Documentation Microsoft** : [Accès sécurisé au moindre privilège](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Contrôle d’accès basé sur les rôles (RBAC)** : Implémenter des attributions de rôles fines
  - Restreindre les rôles étroitement aux ressources et actions spécifiques
  - Éviter les permissions larges ou inutiles qui élargissent les surfaces d’attaque

- **Surveillance continue des permissions** : Mettre en place des audits et une surveillance d'accès en continu
  - Surveiller les modèles d’utilisation des permissions pour détecter des anomalies
  - Corriger rapidement les privilèges excessifs ou inutilisés

## Menaces spécifiques à l'IA

### Attaques d'injection de prompt & de manipulation d'outils

Les implémentations modernes MCP font face à des vecteurs d'attaque sophistiqués spécifiques à l'IA que les mesures de sécurité traditionnelles ne peuvent pas entièrement adresser :

#### **Injection de prompt indirecte (Injection de prompt inter-domaines)**

L’**injection de prompt indirecte** représente une des vulnérabilités les plus critiques dans les systèmes d’IA activés MCP. Les attaquants insèrent des instructions malveillantes dans des contenus externes — documents, pages web, emails, ou sources de données — que les systèmes IA vont ensuite traiter comme des commandes légitimes.

**Scénarios d’attaque :**
- **Injection basée sur des documents** : Instructions malveillantes cachées dans des documents traités qui déclenchent des actions IA non intentionnées
- **Exploitation de contenu web** : Pages web compromises contenant des prompts intégrés qui manipulent le comportement IA lors du scraping
- **Attaques par email** : Prompts malveillants dans des emails qui poussent les assistants IA à divulguer des informations ou effectuer des actions non autorisées
- **Contamination des sources de données** : Bases de données ou APIs compromises fournissant un contenu corrompu aux systèmes IA

**Impact réel** : Ces attaques peuvent entraîner exfiltration de données, violations de la vie privée, génération de contenus nuisibles, et manipulation des interactions utilisateur. Pour une analyse détaillée, voir [Injection de prompt dans MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagramme d'attaque par injection de prompt](../../../translated_images/fr/prompt-injection.ed9fbfde297ca877.webp)

#### **Attaques par empoisonnement d'outils**

L’**empoisonnement d’outils** cible les métadonnées qui définissent les outils MCP, exploitant la manière dont les LLM interprètent les descriptions d’outils et les paramètres pour prendre des décisions d’exécution.

**Mécanismes d’attaque :**
- **Manipulation des métadonnées** : Les attaquants injectent des instructions malveillantes dans les descriptions d’outils, définitions des paramètres, ou exemples d’utilisation
- **Instructions invisibles** : Prompts cachés dans les métadonnées des outils, traités par les modèles IA mais invisibles aux utilisateurs humains
- **Modification dynamique des outils (« Rug Pulls »)** : Outils approuvés par les utilisateurs qui sont ensuite modifiés pour effectuer des actions malveillantes sans que l’utilisateur ne s’en rende compte
- **Injection de paramètres** : Contenu malveillant intégré dans les schémas des paramètres des outils qui influence le comportement du modèle


**Risques des serveurs hébergés** : Les serveurs MCP distants présentent des risques accrus car les définitions des outils peuvent être mises à jour après l'approbation initiale de l'utilisateur, créant des scénarios où des outils auparavant sûrs deviennent malveillants. Pour une analyse complète, voir [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/fr/tool-injection.3b0b4a6b24de6bef.webp)

#### **Vecteurs d'attaque supplémentaires liés à l'IA**

- **Injection de prompt inter-domaines (XPIA)** : Attaques sophistiquées utilisant le contenu provenant de plusieurs domaines pour contourner les contrôles de sécurité
- **Modification dynamique des capacités** : Changements en temps réel des capacités des outils échappant aux évaluations de sécurité initiales
- **Empoisonnement de la fenêtre de contexte** : Attaques manipulant de larges fenêtres de contexte pour dissimuler des instructions malveillantes
- **Attaques de confusion du modèle** : Exploitation des limitations du modèle pour créer des comportements imprévisibles ou dangereux


### Impact des risques liés à la sécurité de l'IA

**Conséquences à fort impact :**
- **Exfiltration de données** : Accès non autorisé et vol de données sensibles d'entreprise ou personnelles
- **Atteintes à la vie privée** : Exposition d'informations personnelles identifiables (PII) et de données commerciales confidentielles  
- **Manipulation des systèmes** : Modifications non intentionnelles des systèmes critiques et des flux de travail
- **Vol de crédentiels** : Compromission des jetons d'authentification et des identifiants de service
- **Mouvement latéral** : Utilisation de systèmes d'IA compromis comme points pivots pour des attaques réseau plus larges

### Solutions de sécurité Microsoft pour l'IA

#### **Boucliers de prompt IA : Protection avancée contre les attaques par injection**

Les **Boucliers de prompt IA** de Microsoft offrent une défense complète contre les attaques par injection de prompt directes et indirectes grâce à plusieurs couches de sécurité :

##### **Mécanismes de protection essentiels :**

1. **Détection avancée & filtrage**
   - Algorithmes d'apprentissage automatique et techniques de traitement du langage naturel détectent les instructions malveillantes dans les contenus externes
   - Analyse en temps réel des documents, pages web, emails et sources de données pour les menaces intégrées
   - Compréhension contextuelle des motifs de prompt légitimes vs malveillants

2. **Techniques d'éclairage**  
   - Distingue entre instructions système de confiance et entrées externes potentiellement compromises
   - Méthodes de transformation de texte qui améliorent la pertinence du modèle tout en isolant le contenu malveillant
   - Aide les systèmes d'IA à maintenir une hiérarchie correcte des instructions et à ignorer les commandes injectées

3. **Systèmes de délimitation & marquage des données**
   - Définition explicite des limites entre messages système de confiance et texte d'entrée externe
   - Marques spéciales mettant en évidence les frontières entre sources de données fiables et non fiables
   - Séparation claire qui évite la confusion des instructions et l'exécution de commandes non autorisées

4. **Veille continue sur les menaces**
   - Microsoft surveille continuellement les nouveaux schémas d'attaque et met à jour les défenses
   - Chasse proactive aux menaces pour les nouvelles techniques d'injection et vecteurs d'attaque
   - Mises à jour régulières des modèles de sécurité pour maintenir l'efficacité face aux menaces évolutives

5. **Intégration Azure Content Safety**
   - Partie intégrante de la suite complète Azure AI Content Safety
   - Détection supplémentaire des tentatives de jailbreak, contenu nuisible, et violations des politiques de sécurité
   - Contrôles de sécurité unifiés à travers les composants de l'application IA

**Ressources de mise en œuvre** : [Documentation Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/fr/prompt-shield.ff5b95be76e9c78c.webp)


## Menaces avancées de sécurité MCP

### Vulnérabilités de détournement de session

Le **détournement de session** représente un vecteur d'attaque critique dans les implémentations MCP avec état où des parties non autorisées obtiennent et abusent d'identifiants de session légitimes pour usurper des clients et effectuer des actions non autorisées.

#### **Scénarios d'attaque & risques**

- **Injection de prompt par détournement de session** : Des attaquants avec des ID de session volés injectent des événements malveillants dans des serveurs partageant l'état de session, déclenchant potentiellement des actions nuisibles ou accédant à des données sensibles
- **Usurpation directe** : Des ID de session volés permettent des appels directs au serveur MCP contournant l'authentification, traitant les attaquants comme des utilisateurs légitimes
- **Flux résumables compromis** : Les attaquants peuvent interrompre prématurément des requêtes, provoquant la reprise par des clients légitimes avec un contenu potentiellement malveillant

#### **Contrôles de sécurité pour la gestion des sessions**

**Exigences critiques :**
- **Vérification des autorisations** : Les serveurs MCP implémentant une autorisation **DOIVENT** vérifier TOUTES les requêtes entrantes et **NE DOIVENT PAS** s'appuyer sur les sessions pour l'authentification
- **Génération sécurisée de sessions** : Utiliser des ID de session cryptographiquement sécurisés, non déterministes, générés avec des générateurs de nombres aléatoires sécurisés
- **Lien spécifique à l'utilisateur** : Lier les ID de session aux informations propres à l'utilisateur en utilisant des formats comme `<user_id>:<session_id>` pour empêcher l'abus inter-utilisateurs
- **Gestion du cycle de vie des sessions** : Implémenter expiration, rotation, et invalidation appropriées pour limiter les fenêtres de vulnérabilité
- **Sécurité des transports** : HTTPS obligatoire pour toutes les communications afin d'éviter l'interception des ID de session

### Problème du délégué confus

Le **problème du délégué confus** survient lorsque les serveurs MCP agissent comme proxies d'authentification entre clients et services tiers, créant des opportunités de contournement d'autorisation via l'exploitation d'ID client statiques.

#### **Mécanismes & risques d'attaque**

- **Contournement du consentement basé sur les cookies** : L'authentification utilisateur précédente crée des cookies de consentement que les attaquants exploitent via des requêtes d'autorisation malveillantes avec des URI de redirection falsifiés
- **Vol de code d'autorisation** : Les cookies de consentement existants peuvent amener les serveurs d'autorisation à sauter les écrans de consentement, redirigeant les codes vers des points de terminaison contrôlés par les attaquants  
- **Accès API non autorisé** : Les codes d'autorisation volés permettent l'échange de jetons et l'usurpation d'utilisateur sans approbation explicite

#### **Stratégies d'atténuation**

**Contrôles obligatoires :**
- **Exigences de consentement explicite** : Les serveurs proxy MCP utilisant des IDs clients statiques **DOIVENT** obtenir le consentement utilisateur pour chaque client enregistré dynamiquement
- **Implémentation sécurisée OAuth 2.1** : Respecter les meilleures pratiques actuelles de sécurité OAuth incluant PKCE (Proof Key for Code Exchange) pour toutes les requêtes d'autorisation
- **Validation stricte des clients** : Mettre en œuvre une validation rigoureuse des URI de redirection et identifiants clients pour prévenir l'exploitation

### Vulnérabilités de passage de token  

Le **passage de token** représente un anti-pattern explicite où les serveurs MCP acceptent les jetons clients sans validation adéquate et les transmettent aux APIs en aval, violant les spécifications d'autorisation MCP.

#### **Implications de sécurité**

- **Contournement des contrôles** : L'utilisation directe des jetons client vers l'API contourne des contrôles critiques de limitation de débit, validation et surveillance
- **Corruption des pistes d'audit** : Les jetons émis en amont rendent impossible l'identification client, compromettant les capacités d'investigation d'incidents
- **Exfiltration de données via proxy** : Les jetons non validés permettent aux acteurs malveillants d'utiliser les serveurs comme proxies pour un accès non autorisé aux données
- **Violation des frontières de confiance** : Les hypothèses de confiance des services en aval peuvent être violées lorsque l'origine des jetons ne peut être vérifiée
- **Expansion des attaques multi-services** : Les jetons compromis acceptés par plusieurs services facilitent le mouvement latéral

#### **Contrôles de sécurité requis**

**Exigences non négociables :**
- **Validation des jetons** : Les serveurs MCP **NE DOIVENT PAS** accepter de jetons non explicitement émis pour le serveur MCP
- **Vérification de l'audience** : Valider systématiquement que la revendication d'audience du jeton correspond à l'identité du serveur MCP
- **Cycle de vie approprié des jetons** : Mettre en œuvre des jetons d'accès à courte durée de vie avec des pratiques sécurisées de rotation


## Sécurité de la chaîne d'approvisionnement pour les systèmes IA

La sécurité de la chaîne d'approvisionnement a évolué au-delà des dépendances logicielles traditionnelles pour englober tout l'écosystème IA. Les implémentations MCP modernes doivent rigoureusement vérifier et surveiller tous les composants liés à l'IA, car chacun introduit des vulnérabilités potentielles pouvant compromettre l'intégrité du système.

### Composants étendus de la chaîne d'approvisionnement IA

**Dépendances logicielles traditionnelles :**
- Bibliothèques et cadres open-source
- Images conteneur et systèmes de base  
- Outils de développement et pipelines de build
- Composants et services d'infrastructure

**Éléments spécifiques de la chaîne d'approvisionnement IA :**
- **Modèles de base** : Modèles pré-entraînés de divers fournisseurs nécessitant une vérification de provenance
- **Services d'embedding** : Services externes de vectorisation et de recherche sémantique
- **Fournisseurs de contexte** : Sources de données, bases de connaissances, et dépôts de documents  
- **APIs tierces** : Services IA externes, pipelines ML, et points de traitement des données
- **Artefacts de modèle** : Poids, configurations et variantes de modèles affinés
- **Sources de données d'entraînement** : Jeux de données utilisés pour l'entraînement et l'affinage des modèles

### Stratégie complète de sécurité de la chaîne d'approvisionnement

#### **Vérification & confiance des composants**
- **Validation de la provenance** : Vérifier l'origine, la licence et l'intégrité de tous les composants IA avant intégration
- **Évaluation de la sécurité** : Effectuer des scans de vulnérabilités et des revues de sécurité pour modèles, sources de données et services IA
- **Analyse de réputation** : Évaluer le bilan de sécurité et les pratiques des fournisseurs de services IA
- **Vérification de conformité** : S'assurer que tous les composants respectent les exigences organisationnelles de sécurité et réglementaires

#### **Pipelines de déploiement sécurisés**  
- **Sécurité CI/CD automatisée** : Intégrer des scans de sécurité tout au long des pipelines de déploiement automatisés
- **Intégrité des artefacts** : Appliquer une vérification cryptographique pour tous les artefacts déployés (code, modèles, configurations)
- **Déploiement par étapes** : Utiliser des stratégies de déploiement progressif avec validation de sécurité à chaque étape
- **Dépôts d'artefacts sécurisés** : Déployer uniquement à partir de registres et dépôts d'artefacts sécurisés et vérifiés

#### **Surveillance et réponse continues**
- **Scan des dépendances** : Surveillance continue des vulnérabilités pour toutes les dépendances logicielles et composants IA
- **Surveillance des modèles** : Évaluation continue du comportement du modèle, dérive de performance, et anomalies de sécurité
- **Suivi de la santé des services** : Monitorer les services IA externes pour disponibilité, incidents de sécurité, et changements de politiques
- **Intégration de renseignement sur les menaces** : Incorporer des flux de menace spécifiques aux risques de sécurité IA et ML

#### **Contrôle d'accès & moindre privilège**
- **Permissions au niveau des composants** : Restreindre l'accès aux modèles, données, et services selon la nécessité métier
- **Gestion des comptes de service** : Implémenter des comptes de service dédiés avec permissions minimales requises
- **Segmentation réseau** : Isoler les composants IA et limiter l'accès réseau entre services
- **Contrôles via API Gateway** : Utiliser des passerelles API centralisées pour contrôler et surveiller l'accès aux services IA externes

#### **Réponse aux incidents & récupération**
- **Procédures de réponse rapide** : Processus établis pour patcher ou remplacer les composants IA compromis
- **Rotation des crédentiels** : Systèmes automatisés pour la rotation des secrets, clés API, et identifiants de service
- **Capacités de retour arrière** : Possibilité de revenir rapidement aux versions antérieures stables des composants IA
- **Récupération après compromission de la chaîne** : Procédures spécifiques pour répondre aux compromissions en amont des services IA

### Outils et intégration Microsoft de sécurité

**GitHub Advanced Security** fournit une protection complète de la chaîne d'approvisionnement incluant :
- **Scan de secrets** : Détection automatisée des identifiants, clés API, et jetons dans les dépôts
- **Scan des dépendances** : Évaluation des vulnérabilités pour les dépendances et bibliothèques open-source
- **Analyse CodeQL** : Analyse statique du code pour vulnérabilités de sécurité et problèmes de codage
- **Informations sur la chaîne d'approvisionnement** : Visibilité sur la santé et le statut de sécurité des dépendances

**Intégration Azure DevOps & Azure Repos :**
- Intégration fluide de scans de sécurité sur les plateformes de développement Microsoft
- Vérifications de sécurité automatisées dans Azure Pipelines pour les charges IA
- Application des politiques pour le déploiement sécurisé des composants IA

**Pratiques internes Microsoft :**
Microsoft met en œuvre des pratiques de sécurité étendues de la chaîne d'approvisionnement à travers tous ses produits. Découvrez des approches éprouvées dans [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Bonnes pratiques de sécurité de base

Les implémentations MCP héritent et s’appuient sur la posture de sécurité existante de votre organisation. Renforcer les pratiques fondamentales améliore considérablement la sécurité globale des systèmes IA et des déploiements MCP.

### Principes fondamentaux de sécurité

#### **Pratiques de développement sécurisé**
- **Conformité OWASP** : Protection contre les vulnérabilités web les plus courantes selon [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Protections spécifiques à l'IA** : Mise en place de contrôles pour le [OWASP Top 10 pour LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Gestion sécurisée des secrets** : Utiliser des coffres-forts dédiés pour les jetons, clés API, et données de configuration sensibles
- **Chiffrement de bout en bout** : Implémenter des communications sécurisées dans tous les composants applicatifs et flux de données
- **Validation des entrées** : Validation rigoureuse de toutes les entrées utilisateur, paramètres API, et sources de données

#### **Renforcement de l'infrastructure**
- **Authentification multi-facteurs** : MFA obligatoire pour tous les comptes administratifs et de service
- **Gestion des patchs** : Application automatisée et rapide des correctifs pour systèmes d'exploitation, frameworks, et dépendances  
- **Intégration de fournisseurs d'identité** : Gestion centralisée via des fournisseurs d'identité d'entreprise (Microsoft Entra ID, Active Directory)
- **Segmentation réseau** : Isolation logique des composants MCP pour limiter le potentiel de mouvement latéral
- **Principe du moindre privilège** : Permissions minimales nécessaires pour tous les composants système et comptes

#### **Surveillance & détection de sécurité**
- **Journalisation complète** : Logs détaillés des activités des applications IA, y compris interactions client-serveur MCP
- **Intégration SIEM** : Gestion centralisée des informations et événements de sécurité pour détection des anomalies
- **Analyse comportementale** : Surveillance pilotée par IA pour détecter les schémas inhabituels dans le comportement systèmes et utilisateurs
- **Renseignement sur les menaces** : Intégration de flux externes de menaces et indicateurs de compromission (IOC)
- **Réponse aux incidents** : Procédures bien définies pour détection, réponse, et récupération après incident de sécurité

#### **Architecture Zero Trust**
- **Ne jamais faire confiance, toujours vérifier** : Vérification continue des utilisateurs, dispositifs, et connexions réseau
- **Micro-segmentation** : Contrôles réseau granulaires isolant charges de travail et services individuels
- **Sécurité centrée sur l'identité** : Politiques de sécurité basées sur des identités vérifiées plutôt que la localisation réseau
- **Évaluation continue des risques** : Évaluation dynamique de la posture de sécurité selon contexte et comportement actuels
- **Accès conditionnel** : Contrôles d'accès qui s'adaptent selon facteurs de risque, localisation, et confiance du dispositif

### Modèles d'intégration d'entreprise

#### **Intégration avec l'écosystème de sécurité Microsoft**
- **Microsoft Defender for Cloud** : Gestion complète de la posture de sécurité cloud
- **Azure Sentinel** : SIEM et SOAR natifs cloud pour la protection des charges IA
- **Microsoft Entra ID** : Gestion d'identité et d'accès en entreprise avec politiques d'accès conditionnel
- **Azure Key Vault** : Gestion centralisée des secrets avec support de module matériel de sécurité (HSM)
- **Microsoft Purview** : Gouvernance des données et conformité pour sources et flux de données IA

#### **Conformité & gouvernance**
- **Alignement réglementaire** : S'assurer que les implémentations MCP respectent les exigences réglementaires sectorielles (RGPD, HIPAA, SOC 2)

- **Classification des données** : Catégorisation et gestion appropriées des données sensibles traitées par les systèmes d’IA
- **Pistes d’audit** : Journalisation exhaustive pour la conformité réglementaire et l’enquête judiciaire
- **Contrôles de confidentialité** : Mise en œuvre de principes de confidentialité dès la conception dans l’architecture des systèmes d’IA
- **Gestion des changements** : Processus formels pour les revues de sécurité des modifications des systèmes d’IA

Ces pratiques fondamentales créent une base de sécurité solide qui renforce l’efficacité des contrôles de sécurité spécifiques à MCP et offre une protection globale aux applications pilotées par l’IA.

## Principaux points de sécurité

- **Approche de sécurité en couches** : Combiner les pratiques de sécurité fondamentales (codage sécurisé, moindre privilège, vérification de la chaîne d’approvisionnement, surveillance continue) avec des contrôles spécifiques à l’IA pour une protection complète

- **Paysage des menaces spécifique à l’IA** : Les systèmes MCP font face à des risques uniques incluant l’injection de prompts, le empoisonnement d’outils, la prise de contrôle de session, les problèmes de délégué confus, les vulnérabilités de passage des jetons et les permissions excessives nécessitant des atténuations spécialisées

- **Excellence en authentification & autorisation** : Mettre en œuvre une authentification robuste avec des fournisseurs d’identité externes (Microsoft Entra ID), appliquer une validation appropriée des jetons et ne jamais accepter de jetons non explicitement émis pour votre serveur MCP

- **Prévention des attaques sur l’IA** : Déployer Microsoft Prompt Shields et Azure Content Safety pour se défendre contre les injections indirectes de prompts et les attaques d’empoisonnement d’outils, tout en validant les métadonnées des outils et en surveillant les modifications dynamiques

- **Sécurité des sessions & du transport** : Utiliser des identifiants de session non déterministes cryptographiquement sécurisés liés aux identités utilisateur, mettre en œuvre une gestion correcte du cycle de vie des sessions et ne jamais utiliser les sessions pour l’authentification

- **Meilleures pratiques de sécurité OAuth** : Prévenir les attaques de délégué confus via un consentement explicite des utilisateurs pour les clients enregistrés dynamiquement, une mise en œuvre correcte d’OAuth 2.1 avec PKCE, et une validation stricte des URI de redirection  

- **Principes de sécurité des jetons** : Éviter les anti-modèles de passage direct de jetons, valider les revendications d’audience des jetons, utiliser des jetons de courte durée avec rotation sécurisée et maintenir des limites de confiance claires

- **Sécurité complète de la chaîne d’approvisionnement** : Traiter tous les composants de l’écosystème IA (modèles, embeddings, fournisseurs de contexte, API externes) avec la même rigueur de sécurité que les dépendances logicielles traditionnelles

- **Évolution continue** : Se tenir à jour avec les spécifications MCP en évolution rapide, contribuer aux normes de la communauté de sécurité, et maintenir des postures de sécurité adaptatives à mesure que le protocole mûrit

- **Intégration de la sécurité Microsoft** : Tirer parti de l’écosystème de sécurité complet de Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) pour une protection renforcée des déploiements MCP

## Ressources complètes

### **Documentation officielle de sécurité MCP**
- [Spécification MCP (Actuel : 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Meilleures pratiques de sécurité MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Spécification d’autorisation MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Dépôt GitHub MCP](https://github.com/modelcontextprotocol)

### **Ressources de sécurité OWASP MCP**
- [Guide de sécurité OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 OWASP MCP complet avec guide d’implémentation Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Risques de sécurité officiels OWASP MCP
- [Atelier du Sommet de Sécurité MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Formation pratique en sécurité MCP sur Azure

### **Normes et meilleures pratiques de sécurité**
- [Meilleures pratiques de sécurité OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [Top 10 OWASP pour la sécurité des applications web](https://owasp.org/www-project-top-ten/)
- [Top 10 OWASP pour les grands modèles de langage](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Rapport Microsoft Digital Defense](https://aka.ms/mddr)

### **Recherche et analyse en sécurité IA**
- [Injection de prompt dans MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Attaques d’empoisonnement d’outils (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Briefing de recherche en sécurité MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Solutions de sécurité Microsoft**
- [Documentation Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Service Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Sécurité Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Meilleures pratiques de gestion des jetons Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Guides de mise en œuvre & tutoriels**
- [Azure API Management en tant que passerelle d’authentification MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Authentification Microsoft Entra ID avec serveurs MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Stockage et chiffrement sécurisé des jetons (Vidéo)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Sécurité DevOps & chaîne d’approvisionnement**
- [Sécurité Azure DevOps](https://azure.microsoft.com/products/devops)
- [Sécurité Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Parcours de sécurité de la chaîne d’approvisionnement Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentation de sécurité supplémentaire**

Pour une orientation complète en sécurité, consultez ces documents spécialisés dans cette section :

- **[Exemple d’autorisation CIMD et DCR](./samples/cimd-dcr-auth/README.md)** - Serveur de ressources MCP `2026-07-28` TypeScript exécutable comparant les documents préférés Client ID Metadata avec un repli Dynamic Client Registration obsolète
- **[Meilleures pratiques de sécurité MCP](./mcp-security-best-practices.md)** - Meilleures pratiques de sécurité complètes pour les implémentations MCP
- **[Implémentation Azure Content Safety](./azure-content-safety-implementation.md)** - Exemples pratiques d’intégration Azure Content Safety  
- **[Contrôles de sécurité MCP](./mcp-security-controls.md)** - Derniers contrôles et techniques de sécurité pour les déploiements MCP
- **[Référence rapide des meilleures pratiques MCP](./mcp-best-practices.md)** - Guide de référence rapide pour les pratiques essentielles de sécurité MCP
- **[BlueHat 2026 : Sécuriser l’avenir de l’IA : sécuriser MCP avec des modèles de défense en profondeur](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Modèles de défense en profondeur du Microsoft Security Response Center (MSRC)

### **Formation pratique en sécurité**

- **[Atelier du Sommet de Sécurité MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - Atelier pratique complet pour sécuriser les serveurs MCP dans Azure avec des camps progressifs de Base Camp à Summit
- **[Guide de sécurité OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Architecture de référence et guide d’implémentation pour tous les risques OWASP MCP Top 10

---

## Et après

Suivant : [Chapitre 3 : Premiers pas](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->