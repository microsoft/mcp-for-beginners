# Sécurité MCP : Protection complète pour les systèmes d'IA

[![Meilleures pratiques de sécurité MCP](../../../translated_images/fr/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

La sécurité est fondamentale dans la conception des systèmes d'IA, c'est pourquoi nous la priorisons comme notre deuxième section. Cela s'aligne avec le principe **Secure by Design** de Microsoft issu de l’[Initiative Secure Future](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Le protocole Model Context Protocol (MCP) apporte de puissantes nouvelles capacités aux applications pilotées par l’IA tout en introduisant des défis de sécurité uniques qui vont au-delà des risques logiciels traditionnels. Les systèmes MCP font face à la fois à des préoccupations de sécurité établies (codage sécurisé, moindre privilège, sécurité de la chaîne d’approvisionnement) et à de nouvelles menaces spécifiques à l’IA, notamment l’injection de prompt, l’empoisonnement d’outils, le détournement de session, les attaques de délégué confus, les vulnérabilités de passage de jetons et la modification dynamique des capacités.

Cette leçon explore les risques de sécurité les plus critiques dans les implémentations MCP — couvrant l’authentification, l’autorisation, les permissions excessives, l’injection indirecte de prompt, la sécurité des sessions, les problèmes de délégué confus, la gestion des jetons et les vulnérabilités de la chaîne d’approvisionnement. Vous apprendrez des contrôles exploitables et des meilleures pratiques pour atténuer ces risques tout en tirant parti des solutions Microsoft telles que Prompt Shields, Azure Content Safety et GitHub Advanced Security pour renforcer votre déploiement MCP.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- **Identifier les menaces spécifiques au MCP** : Reconnaître les risques de sécurité uniques dans les systèmes MCP, y compris l’injection de prompt, l’empoisonnement d’outils, les permissions excessives, le détournement de session, les problèmes de délégué confus, les vulnérabilités de passage de jetons et les risques liés à la chaîne d’approvisionnement
- **Appliquer des contrôles de sécurité** : Mettre en œuvre des atténuations efficaces incluant une authentification robuste, un accès au moindre privilège, une gestion sécurisée des jetons, des contrôles de sécurité des sessions et une vérification de la chaîne d’approvisionnement
- **Exploiter les solutions de sécurité Microsoft** : Comprendre et déployer Microsoft Prompt Shields, Azure Content Safety et GitHub Advanced Security pour la protection des charges de travail MCP
- **Valider la sécurité des outils** : Reconnaître l’importance de la validation des métadonnées des outils, de la surveillance des modifications dynamiques et de la défense contre les attaques d’injection indirecte de prompt
- **Intégrer les meilleures pratiques** : Combiner les fondamentaux établis de la sécurité (codage sécurisé, durcissement des serveurs, zero trust) avec les contrôles spécifiques au MCP pour une protection complète

# Architecture et contrôles de sécurité MCP

Les implémentations modernes de MCP nécessitent des approches de sécurité en couches qui traitent à la fois la sécurité logicielle traditionnelle et les menaces spécifiques à l’IA. La spécification MCP en évolution rapide continue de mûrir ses contrôles de sécurité, permettant une meilleure intégration avec les architectures de sécurité d’entreprise et les meilleures pratiques établies.

Les recherches du [Microsoft Digital Defense Report](https://aka.ms/mddr) démontrent que **98 % des violations signalées seraient évitées par une hygiène de sécurité robuste**. La stratégie de protection la plus efficace combine des pratiques de sécurité fondamentales avec des contrôles spécifiques au MCP — les mesures de sécurité de base éprouvées restent les plus impactantes pour réduire le risque global.

## Paysage actuel de la sécurité

> **Note :** Ces informations reflètent les normes de sécurité MCP au **18 décembre 2025**. Le protocole MCP continue d’évoluer rapidement, et les futures implémentations pourraient introduire de nouveaux modèles d’authentification et des contrôles renforcés. Référez-vous toujours à la [Spécification MCP](https://spec.modelcontextprotocol.io/), au [dépôt GitHub MCP](https://github.com/modelcontextprotocol) et à la [documentation des meilleures pratiques de sécurité](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) pour les dernières recommandations.

### Évolution de l’authentification MCP

La spécification MCP a considérablement évolué dans son approche de l’authentification et de l’autorisation :

- **Approche originale** : Les premières spécifications exigeaient que les développeurs implémentent des serveurs d’authentification personnalisés, les serveurs MCP agissant comme serveurs d’autorisation OAuth 2.0 gérant directement l’authentification des utilisateurs
- **Norme actuelle (2025-11-25)** : La spécification mise à jour permet aux serveurs MCP de déléguer l’authentification à des fournisseurs d’identité externes (comme Microsoft Entra ID), améliorant la posture de sécurité et réduisant la complexité d’implémentation
- **Sécurité de la couche transport** : Support renforcé des mécanismes de transport sécurisés avec des modèles d’authentification appropriés pour les connexions locales (STDIO) et distantes (HTTP Streamable)

## Sécurité de l’authentification et de l’autorisation

### Défis actuels de sécurité

Les implémentations modernes de MCP font face à plusieurs défis d’authentification et d’autorisation :

### Risques et vecteurs d’attaque

- **Logique d’autorisation mal configurée** : Une implémentation défaillante de l’autorisation dans les serveurs MCP peut exposer des données sensibles et appliquer incorrectement les contrôles d’accès
- **Compromission des jetons OAuth** : Le vol de jetons sur un serveur MCP local permet aux attaquants de se faire passer pour le serveur et d’accéder aux services en aval
- **Vulnérabilités de passage de jetons** : Une mauvaise gestion des jetons crée des contournements des contrôles de sécurité et des lacunes de responsabilité
- **Permissions excessives** : Des serveurs MCP sur-privilegiés violent le principe du moindre privilège et élargissent la surface d’attaque

#### Passage de jetons : un anti-pattern critique

**Le passage de jetons est explicitement interdit** dans la spécification d’autorisation MCP actuelle en raison de graves implications de sécurité :

##### Contournement des contrôles de sécurité
- Les serveurs MCP et les API en aval mettent en œuvre des contrôles critiques (limitation de débit, validation des requêtes, surveillance du trafic) qui dépendent d’une validation correcte des jetons
- L’utilisation directe des jetons client vers API contourne ces protections essentielles, sapant l’architecture de sécurité

##### Défis de responsabilité et d’audit  
- Les serveurs MCP ne peuvent pas distinguer les clients utilisant des jetons émis en amont, rompant les pistes d’audit
- Les journaux des serveurs de ressources en aval montrent des origines de requêtes trompeuses plutôt que les véritables intermédiaires MCP
- L’investigation des incidents et l’audit de conformité deviennent beaucoup plus difficiles

##### Risques d’exfiltration de données
- Les revendications de jetons non validées permettent aux acteurs malveillants avec des jetons volés d’utiliser les serveurs MCP comme proxies pour l’exfiltration de données
- Les violations des frontières de confiance permettent des accès non autorisés contournant les contrôles de sécurité prévus

##### Vecteurs d’attaque multi-services
- Les jetons compromis acceptés par plusieurs services permettent des mouvements latéraux à travers les systèmes connectés
- Les hypothèses de confiance entre services peuvent être violées lorsque l’origine des jetons ne peut être vérifiée

### Contrôles de sécurité et atténuations

**Exigences critiques de sécurité :**

> **OBLIGATOIRE** : Les serveurs MCP **NE DOIVENT PAS** accepter de jetons qui n’ont pas été explicitement émis pour le serveur MCP

#### Contrôles d’authentification et d’autorisation

- **Revue rigoureuse de l’autorisation** : Effectuer des audits complets de la logique d’autorisation des serveurs MCP pour garantir que seuls les utilisateurs et clients prévus peuvent accéder aux ressources sensibles
  - **Guide d’implémentation** : [Azure API Management comme passerelle d’authentification pour les serveurs MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Intégration d’identité** : [Utilisation de Microsoft Entra ID pour l’authentification des serveurs MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestion sécurisée des jetons** : Mettre en œuvre les [meilleures pratiques de validation et de cycle de vie des jetons de Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Valider que les revendications d’audience du jeton correspondent à l’identité du serveur MCP
  - Appliquer des politiques appropriées de rotation et d’expiration des jetons
  - Prévenir les attaques de rejeu de jetons et les usages non autorisés

- **Stockage protégé des jetons** : Sécuriser le stockage des jetons avec chiffrement au repos et en transit
  - **Meilleures pratiques** : [Directives pour le stockage sécurisé et le chiffrement des jetons](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Mise en œuvre du contrôle d’accès

- **Principe du moindre privilège** : Accorder aux serveurs MCP uniquement les permissions minimales requises pour la fonctionnalité prévue
  - Revue régulière des permissions et mises à jour pour éviter l’accumulation de privilèges
  - **Documentation Microsoft** : [Accès sécurisé au moindre privilège](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Contrôle d’accès basé sur les rôles (RBAC)** : Mettre en œuvre des attributions de rôles fines
  - Restreindre les rôles à des ressources et actions spécifiques
  - Éviter les permissions larges ou inutiles qui élargissent la surface d’attaque

- **Surveillance continue des permissions** : Mettre en place un audit et une surveillance d’accès continus
  - Surveiller les schémas d’utilisation des permissions pour détecter les anomalies
  - Remédier rapidement aux privilèges excessifs ou inutilisés

## Menaces spécifiques à la sécurité de l’IA

### Attaques d’injection de prompt et de manipulation d’outils

Les implémentations modernes de MCP font face à des vecteurs d’attaque sophistiqués spécifiques à l’IA que les mesures de sécurité traditionnelles ne peuvent pas entièrement adresser :

#### **Injection indirecte de prompt (Injection de prompt inter-domaines)**

L’**injection indirecte de prompt** représente l’une des vulnérabilités les plus critiques dans les systèmes d’IA activés par MCP. Les attaquants intègrent des instructions malveillantes dans des contenus externes — documents, pages web, emails ou sources de données — que les systèmes d’IA traitent ensuite comme des commandes légitimes.

**Scénarios d’attaque :**
- **Injection basée sur des documents** : Instructions malveillantes cachées dans des documents traités qui déclenchent des actions IA non prévues
- **Exploitation de contenu web** : Pages web compromises contenant des prompts intégrés qui manipulent le comportement de l’IA lors du scraping
- **Attaques par email** : Prompts malveillants dans des emails qui poussent les assistants IA à divulguer des informations ou à effectuer des actions non autorisées
- **Contamination de sources de données** : Bases de données ou API compromises servant du contenu altéré aux systèmes IA

**Impact réel** : Ces attaques peuvent entraîner l’exfiltration de données, des violations de la vie privée, la génération de contenu nuisible et la manipulation des interactions utilisateur. Pour une analyse détaillée, voir [Injection de prompt dans MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagramme d’attaque par injection de prompt](../../../translated_images/fr/prompt-injection.ed9fbfde297ca877.webp)

#### **Attaques d’empoisonnement d’outils**

L’**empoisonnement d’outils** cible les métadonnées qui définissent les outils MCP, exploitant la manière dont les LLM interprètent les descriptions et paramètres des outils pour prendre des décisions d’exécution.

**Mécanismes d’attaque :**
- **Manipulation des métadonnées** : Les attaquants injectent des instructions malveillantes dans les descriptions d’outils, les définitions de paramètres ou les exemples d’utilisation
- **Instructions invisibles** : Prompts cachés dans les métadonnées des outils, traités par les modèles IA mais invisibles pour les utilisateurs humains
- **Modification dynamique d’outils (« Rug Pulls »)** : Des outils approuvés par les utilisateurs sont modifiés ultérieurement pour effectuer des actions malveillantes sans que l’utilisateur en soit informé
- **Injection de paramètres** : Contenu malveillant intégré dans les schémas de paramètres des outils influençant le comportement du modèle

**Risques des serveurs hébergés** : Les serveurs MCP distants présentent des risques accrus car les définitions d’outils peuvent être mises à jour après l’approbation initiale de l’utilisateur, créant des scénarios où des outils auparavant sûrs deviennent malveillants. Pour une analyse complète, voir [Attaques d’empoisonnement d’outils (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagramme d’attaque par injection d’outil](../../../translated_images/fr/tool-injection.3b0b4a6b24de6bef.webp)

#### **Autres vecteurs d’attaque IA**

- **Injection de prompt inter-domaines (XPIA)** : Attaques sophistiquées exploitant du contenu provenant de multiples domaines pour contourner les contrôles de sécurité
- **Modification dynamique des capacités** : Changements en temps réel des capacités des outils échappant aux évaluations de sécurité initiales
- **Empoisonnement de la fenêtre de contexte** : Attaques manipulant de larges fenêtres de contexte pour cacher des instructions malveillantes
- **Attaques de confusion du modèle** : Exploitation des limites du modèle pour créer des comportements imprévisibles ou dangereux

### Impact des risques de sécurité IA

**Conséquences à fort impact :**
- **Exfiltration de données** : Accès non autorisé et vol de données sensibles d’entreprise ou personnelles
- **Violations de la vie privée** : Exposition d’informations personnelles identifiables (PII) et de données commerciales confidentielles  
- **Manipulation des systèmes** : Modifications non intentionnelles des systèmes et flux de travail critiques
- **Vol d’identifiants** : Compromission des jetons d’authentification et des identifiants de service
- **Mouvement latéral** : Utilisation des systèmes IA compromis comme pivots pour des attaques réseau plus larges

### Solutions Microsoft pour la sécurité IA

#### **AI Prompt Shields : Protection avancée contre les attaques d’injection**

Microsoft **AI Prompt Shields** offrent une défense complète contre les attaques d’injection de prompt directes et indirectes via plusieurs couches de sécurité :

##### **Mécanismes de protection principaux :**

1. **Détection avancée et filtrage**
   - Algorithmes d’apprentissage automatique et techniques de NLP détectent les instructions malveillantes dans le contenu externe
   - Analyse en temps réel des documents, pages web, emails et sources de données pour les menaces intégrées
   - Compréhension contextuelle des modèles de prompt légitimes vs malveillants

2. **Techniques de mise en lumière**  
   - Distinction entre instructions système de confiance et entrées externes potentiellement compromises
   - Méthodes de transformation de texte améliorant la pertinence du modèle tout en isolant le contenu malveillant
   - Aide les systèmes IA à maintenir une hiérarchie d’instructions correcte et à ignorer les commandes injectées

3. **Systèmes de délimitation et de marquage des données**
   - Définition explicite des frontières entre messages système de confiance et texte d’entrée externe
   - Marqueurs spéciaux soulignant les limites entre sources de données fiables et non fiables
   - Séparation claire empêchant la confusion des instructions et l’exécution non autorisée de commandes

4. **Renseignement continu sur les menaces**
   - Microsoft surveille en continu les nouveaux schémas d’attaque et met à jour les défenses
   - Recherche proactive de nouvelles techniques d’injection et vecteurs d’attaque
   - Mises à jour régulières des modèles de sécurité pour maintenir l’efficacité face aux menaces évolutives

5. **Intégration Azure Content Safety**
   - Partie intégrante de la suite complète Azure AI Content Safety
   - Détection supplémentaire des tentatives de jailbreak, contenu nuisible et violations des politiques de sécurité
   - Contrôles de sécurité unifiés à travers les composants des applications IA

**Ressources d’implémentation** : [Documentation Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Protection Microsoft Prompt Shields](../../../translated_images/fr/prompt-shield.ff5b95be76e9c78c.webp)


## Menaces avancées de sécurité MCP

### Vulnérabilités de détournement de session

Le **détournement de session** représente un vecteur d’attaque critique dans les implémentations MCP à état où des parties non autorisées obtiennent et abusent d’identifiants de session légitimes pour se faire passer pour des clients et effectuer des actions non autorisées.

#### **Scénarios d’attaque et risques**

- **Injection de prompt par détournement de session** : Les attaquants disposant d’ID de session volés injectent des événements malveillants dans des serveurs partageant l’état de session, pouvant déclencher des actions nuisibles ou accéder à des données sensibles
- **Impersonation directe** : Les ID de session volés permettent des appels directs au serveur MCP contournant l’authentification, traitant les attaquants comme des utilisateurs légitimes
- **Flux résumables compromis** : Les attaquants peuvent interrompre prématurément des requêtes, forçant les clients légitimes à reprendre avec un contenu potentiellement malveillant

#### **Contrôles de sécurité pour la gestion des sessions**

**Exigences critiques :**
- **Vérification de l’autorisation** : Les serveurs MCP mettant en œuvre l’autorisation **DOIVENT** vérifier TOUTES les requêtes entrantes et **NE DOIVENT PAS** se fier aux sessions pour l’authentification  
- **Génération sécurisée de session** : Utiliser des identifiants de session cryptographiquement sécurisés, non déterministes, générés avec des générateurs de nombres aléatoires sécurisés  
- **Liaison spécifique à l’utilisateur** : Lier les identifiants de session aux informations spécifiques à l’utilisateur en utilisant des formats comme `<user_id>:<session_id>` pour éviter les abus de session entre utilisateurs  
- **Gestion du cycle de vie des sessions** : Mettre en œuvre une expiration, une rotation et une invalidation appropriées pour limiter les fenêtres de vulnérabilité  
- **Sécurité du transport** : HTTPS obligatoire pour toutes les communications afin d’éviter l’interception des identifiants de session  

### Problème du délégué confus

Le **problème du délégué confus** survient lorsque les serveurs MCP agissent comme des proxys d’authentification entre les clients et des services tiers, créant des opportunités de contournement d’autorisation via l’exploitation d’identifiants clients statiques.

#### **Mécanismes d’attaque et risques**

- **Contournement du consentement basé sur les cookies** : L’authentification utilisateur précédente crée des cookies de consentement que les attaquants exploitent via des requêtes d’autorisation malveillantes avec des URI de redirection falsifiées  
- **Vol de code d’autorisation** : Les cookies de consentement existants peuvent amener les serveurs d’autorisation à sauter les écrans de consentement, redirigeant les codes vers des points de terminaison contrôlés par l’attaquant  
- **Accès non autorisé à l’API** : Les codes d’autorisation volés permettent l’échange de jetons et l’usurpation d’identité utilisateur sans approbation explicite  

#### **Stratégies d’atténuation**

**Contrôles obligatoires :**  
- **Exigences de consentement explicite** : Les serveurs proxy MCP utilisant des identifiants clients statiques **DOIVENT** obtenir le consentement de l’utilisateur pour chaque client enregistré dynamiquement  
- **Mise en œuvre sécurisée d’OAuth 2.1** : Suivre les meilleures pratiques de sécurité OAuth actuelles, y compris PKCE (Proof Key for Code Exchange) pour toutes les requêtes d’autorisation  
- **Validation stricte des clients** : Mettre en œuvre une validation rigoureuse des URI de redirection et des identifiants clients pour prévenir l’exploitation  

### Vulnérabilités de passage de jetons  

Le **passage de jetons** représente un anti-pattern explicite où les serveurs MCP acceptent des jetons clients sans validation appropriée et les transmettent aux API en aval, violant les spécifications d’autorisation MCP.

#### **Implications de sécurité**

- **Contournement des contrôles** : L’utilisation directe des jetons client vers l’API contourne les contrôles critiques de limitation de débit, validation et surveillance  
- **Corruption de la traçabilité** : Les jetons émis en amont rendent impossible l’identification du client, compromettant les capacités d’investigation des incidents  
- **Exfiltration de données via proxy** : Les jetons non validés permettent aux acteurs malveillants d’utiliser les serveurs comme proxy pour un accès non autorisé aux données  
- **Violation des frontières de confiance** : Les hypothèses de confiance des services en aval peuvent être violées lorsque l’origine des jetons ne peut être vérifiée  
- **Expansion des attaques multi-services** : Les jetons compromis acceptés sur plusieurs services permettent des mouvements latéraux  

#### **Contrôles de sécurité requis**

**Exigences non négociables :**  
- **Validation des jetons** : Les serveurs MCP **NE DOIVENT PAS** accepter des jetons non explicitement émis pour le serveur MCP  
- **Vérification de l’audience** : Toujours valider que les revendications d’audience du jeton correspondent à l’identité du serveur MCP  
- **Cycle de vie approprié des jetons** : Mettre en œuvre des jetons d’accès à courte durée de vie avec des pratiques sécurisées de rotation  

## Sécurité de la chaîne d’approvisionnement pour les systèmes IA

La sécurité de la chaîne d’approvisionnement a évolué au-delà des dépendances logicielles traditionnelles pour englober l’ensemble de l’écosystème IA. Les implémentations modernes de MCP doivent vérifier et surveiller rigoureusement tous les composants liés à l’IA, car chacun introduit des vulnérabilités potentielles pouvant compromettre l’intégrité du système.

### Composants étendus de la chaîne d’approvisionnement IA

**Dépendances logicielles traditionnelles :**  
- Bibliothèques et frameworks open source  
- Images de conteneurs et systèmes de base  
- Outils de développement et pipelines de build  
- Composants et services d’infrastructure  

**Éléments spécifiques à la chaîne d’approvisionnement IA :**  
- **Modèles fondamentaux** : Modèles pré-entraînés de divers fournisseurs nécessitant une vérification de provenance  
- **Services d’embedding** : Services externes de vectorisation et de recherche sémantique  
- **Fournisseurs de contexte** : Sources de données, bases de connaissances et dépôts de documents  
- **APIs tierces** : Services IA externes, pipelines ML et points de traitement de données  
- **Artefacts de modèles** : Poids, configurations et variantes de modèles affinés  
- **Sources de données d’entraînement** : Jeux de données utilisés pour l’entraînement et l’affinage des modèles  

### Stratégie complète de sécurité de la chaîne d’approvisionnement

#### **Vérification des composants et confiance**  
- **Validation de provenance** : Vérifier l’origine, la licence et l’intégrité de tous les composants IA avant intégration  
- **Évaluation de sécurité** : Effectuer des analyses de vulnérabilités et des revues de sécurité pour les modèles, sources de données et services IA  
- **Analyse de réputation** : Évaluer le bilan de sécurité et les pratiques des fournisseurs de services IA  
- **Vérification de conformité** : S’assurer que tous les composants respectent les exigences de sécurité et réglementaires de l’organisation  

#### **Pipelines de déploiement sécurisés**  
- **Sécurité CI/CD automatisée** : Intégrer des analyses de sécurité tout au long des pipelines de déploiement automatisés  
- **Intégrité des artefacts** : Mettre en œuvre une vérification cryptographique pour tous les artefacts déployés (code, modèles, configurations)  
- **Déploiement par étapes** : Utiliser des stratégies de déploiement progressif avec validation de sécurité à chaque étape  
- **Dépôts d’artefacts de confiance** : Déployer uniquement à partir de registres et dépôts d’artefacts vérifiés et sécurisés  

#### **Surveillance continue et réponse**  
- **Analyse des dépendances** : Surveillance continue des vulnérabilités pour toutes les dépendances logicielles et composants IA  
- **Surveillance des modèles** : Évaluation continue du comportement des modèles, dérive de performance et anomalies de sécurité  
- **Suivi de la santé des services** : Surveillance des services IA externes pour disponibilité, incidents de sécurité et changements de politique  
- **Intégration du renseignement sur les menaces** : Incorporer des flux de menaces spécifiques aux risques de sécurité IA et ML  

#### **Contrôle d’accès et moindre privilège**  
- **Permissions au niveau des composants** : Restreindre l’accès aux modèles, données et services selon la nécessité métier  
- **Gestion des comptes de service** : Mettre en œuvre des comptes de service dédiés avec les permissions minimales requises  
- **Segmentation réseau** : Isoler les composants IA et limiter l’accès réseau entre services  
- **Contrôles de passerelle API** : Utiliser des passerelles API centralisées pour contrôler et surveiller l’accès aux services IA externes  

#### **Réponse aux incidents et récupération**  
- **Procédures de réponse rapide** : Processus établis pour patcher ou remplacer les composants IA compromis  
- **Rotation des identifiants** : Systèmes automatisés pour la rotation des secrets, clés API et identifiants de service  
- **Capacités de retour arrière** : Possibilité de revenir rapidement à des versions antérieures connues comme sûres des composants IA  
- **Récupération après compromission de la chaîne d’approvisionnement** : Procédures spécifiques pour répondre aux compromissions des services IA en amont  

### Outils et intégration de sécurité Microsoft

**GitHub Advanced Security** offre une protection complète de la chaîne d’approvisionnement incluant :  
- **Analyse des secrets** : Détection automatisée des identifiants, clés API et jetons dans les dépôts  
- **Analyse des dépendances** : Évaluation des vulnérabilités des dépendances open source et bibliothèques  
- **Analyse CodeQL** : Analyse statique du code pour vulnérabilités de sécurité et problèmes de codage  
- **Insights sur la chaîne d’approvisionnement** : Visibilité sur la santé et le statut de sécurité des dépendances  

**Intégration Azure DevOps & Azure Repos :**  
- Intégration fluide des analyses de sécurité sur les plateformes de développement Microsoft  
- Contrôles de sécurité automatisés dans Azure Pipelines pour les charges IA  
- Application des politiques pour un déploiement sécurisé des composants IA  

**Pratiques internes Microsoft :**  
Microsoft met en œuvre des pratiques étendues de sécurité de la chaîne d’approvisionnement sur tous ses produits. Découvrez les approches éprouvées dans [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Bonnes pratiques fondamentales de sécurité

Les implémentations MCP héritent et s’appuient sur la posture de sécurité existante de votre organisation. Renforcer les pratiques fondamentales de sécurité améliore significativement la sécurité globale des systèmes IA et des déploiements MCP.

### Principes fondamentaux de sécurité

#### **Pratiques de développement sécurisé**  
- **Conformité OWASP** : Protection contre les vulnérabilités web [OWASP Top 10](https://owasp.org/www-project-top-ten/)  
- **Protections spécifiques IA** : Mise en œuvre de contrôles pour [OWASP Top 10 pour LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Gestion sécurisée des secrets** : Utilisation de coffres dédiés pour jetons, clés API et données de configuration sensibles  
- **Chiffrement de bout en bout** : Mise en œuvre de communications sécurisées sur tous les composants applicatifs et flux de données  
- **Validation des entrées** : Validation rigoureuse de toutes les entrées utilisateur, paramètres API et sources de données  

#### **Renforcement de l’infrastructure**  
- **Authentification multi-facteurs** : MFA obligatoire pour tous les comptes administratifs et de service  
- **Gestion des correctifs** : Application automatisée et rapide des correctifs pour systèmes d’exploitation, frameworks et dépendances  
- **Intégration des fournisseurs d’identité** : Gestion centralisée des identités via fournisseurs d’identité d’entreprise (Microsoft Entra ID, Active Directory)  
- **Segmentation réseau** : Isolation logique des composants MCP pour limiter les mouvements latéraux  
- **Principe du moindre privilège** : Permissions minimales requises pour tous les composants et comptes système  

#### **Surveillance et détection de sécurité**  
- **Journalisation complète** : Journalisation détaillée des activités des applications IA, y compris interactions client-serveur MCP  
- **Intégration SIEM** : Gestion centralisée des informations et événements de sécurité pour détection d’anomalies  
- **Analyse comportementale** : Surveillance assistée par IA pour détecter les comportements inhabituels des systèmes et utilisateurs  
- **Renseignement sur les menaces** : Intégration de flux externes de menaces et indicateurs de compromission (IOC)  
- **Réponse aux incidents** : Procédures bien définies pour la détection, la réponse et la récupération des incidents de sécurité  

#### **Architecture Zero Trust**  
- **Ne jamais faire confiance, toujours vérifier** : Vérification continue des utilisateurs, appareils et connexions réseau  
- **Micro-segmentation** : Contrôles réseau granulaires isolant les charges de travail et services individuels  
- **Sécurité centrée sur l’identité** : Politiques de sécurité basées sur des identités vérifiées plutôt que sur la localisation réseau  
- **Évaluation continue des risques** : Évaluation dynamique de la posture de sécurité selon le contexte et le comportement actuels  
- **Accès conditionnel** : Contrôles d’accès adaptatifs basés sur les facteurs de risque, la localisation et la confiance de l’appareil  

### Modèles d’intégration d’entreprise

#### **Intégration dans l’écosystème de sécurité Microsoft**  
- **Microsoft Defender for Cloud** : Gestion complète de la posture de sécurité cloud  
- **Azure Sentinel** : Capacités SIEM et SOAR natives cloud pour la protection des charges IA  
- **Microsoft Entra ID** : Gestion d’identité et d’accès d’entreprise avec politiques d’accès conditionnel  
- **Azure Key Vault** : Gestion centralisée des secrets avec support de module matériel de sécurité (HSM)  
- **Microsoft Purview** : Gouvernance des données et conformité pour les sources et flux de données IA  

#### **Conformité et gouvernance**  
- **Alignement réglementaire** : S’assurer que les implémentations MCP respectent les exigences de conformité sectorielles (RGPD, HIPAA, SOC 2)  
- **Classification des données** : Catégorisation et gestion appropriées des données sensibles traitées par les systèmes IA  
- **Traçabilité** : Journalisation complète pour conformité réglementaire et enquêtes judiciaires  
- **Contrôles de confidentialité** : Mise en œuvre des principes de confidentialité dès la conception dans l’architecture IA  
- **Gestion des changements** : Processus formels pour les revues de sécurité des modifications des systèmes IA  

Ces pratiques fondamentales créent une base de sécurité robuste qui améliore l’efficacité des contrôles spécifiques MCP et offre une protection complète pour les applications pilotées par IA.

## Points clés de sécurité

- **Approche de sécurité en couches** : Combiner les pratiques fondamentales de sécurité (codage sécurisé, moindre privilège, vérification de la chaîne d’approvisionnement, surveillance continue) avec des contrôles spécifiques IA pour une protection complète  

- **Paysage des menaces spécifique à l’IA** : Les systèmes MCP font face à des risques uniques incluant injection de prompt, empoisonnement d’outils, détournement de session, problème du délégué confus, vulnérabilités de passage de jetons et permissions excessives nécessitant des atténuations spécialisées  

- **Excellence en authentification et autorisation** : Mettre en œuvre une authentification robuste via des fournisseurs d’identité externes (Microsoft Entra ID), appliquer une validation correcte des jetons et ne jamais accepter de jetons non explicitement émis pour votre serveur MCP  

- **Prévention des attaques IA** : Déployer Microsoft Prompt Shields et Azure Content Safety pour se défendre contre les injections indirectes de prompt et les attaques d’empoisonnement d’outils, tout en validant les métadonnées des outils et en surveillant les changements dynamiques  

- **Sécurité des sessions et du transport** : Utiliser des identifiants de session cryptographiquement sécurisés, non déterministes, liés aux identités utilisateur, mettre en œuvre une gestion appropriée du cycle de vie des sessions et ne jamais utiliser les sessions pour l’authentification  

- **Meilleures pratiques OAuth** : Prévenir les attaques du délégué confus par un consentement utilisateur explicite pour les clients enregistrés dynamiquement, une mise en œuvre correcte d’OAuth 2.1 avec PKCE et une validation stricte des URI de redirection  

- **Principes de sécurité des jetons** : Éviter les anti-patterns de passage de jetons, valider les revendications d’audience des jetons, mettre en œuvre des jetons à courte durée de vie avec rotation sécurisée et maintenir des frontières de confiance claires  

- **Sécurité complète de la chaîne d’approvisionnement** : Traiter tous les composants de l’écosystème IA (modèles, embeddings, fournisseurs de contexte, APIs externes) avec la même rigueur de sécurité que les dépendances logicielles traditionnelles  

- **Évolution continue** : Se tenir à jour avec les spécifications MCP en rapide évolution, contribuer aux standards de la communauté de sécurité et maintenir des postures de sécurité adaptatives à mesure que le protocole mûrit  

- **Intégration de la sécurité Microsoft** : Tirer parti de l’écosystème complet de sécurité Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) pour une protection renforcée des déploiements MCP  

## Ressources complètes

### **Documentation officielle de sécurité MCP**  
- [Spécification MCP (Actuelle : 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [Bonnes pratiques de sécurité MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [Spécification d’autorisation MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [Dépôt GitHub MCP](https://github.com/modelcontextprotocol)  

### **Normes et bonnes pratiques de sécurité**  
- [Meilleures pratiques de sécurité OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Sécurité des applications web](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 pour les grands modèles de langage](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Rapport Microsoft Digital Defense](https://aka.ms/mddr)  

### **Recherche et analyse en sécurité IA**  
- [Injection de prompt dans MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Attaques d’empoisonnement d’outils (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Briefing sur la recherche en sécurité MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Solutions de sécurité Microsoft**
- [Documentation Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Service Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Sécurité Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Bonnes pratiques de gestion des jetons Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Guides de mise en œuvre & Tutoriels**
- [Gestion des API Azure comme passerelle d’authentification MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Authentification Microsoft Entra ID avec les serveurs MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Stockage sécurisé des jetons et chiffrement (Vidéo)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Sécurité DevOps & chaîne d’approvisionnement**
- [Sécurité Azure DevOps](https://azure.microsoft.com/products/devops)
- [Sécurité Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Parcours de sécurité de la chaîne d’approvisionnement Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentation supplémentaire sur la sécurité**

Pour des conseils de sécurité complets, consultez ces documents spécialisés dans cette section :

- **[Bonnes pratiques de sécurité MCP 2025](./mcp-security-best-practices-2025.md)** - Bonnes pratiques complètes de sécurité pour les implémentations MCP
- **[Mise en œuvre Azure Content Safety](./azure-content-safety-implementation.md)** - Exemples pratiques d’intégration Azure Content Safety  
- **[Contrôles de sécurité MCP 2025](./mcp-security-controls-2025.md)** - Derniers contrôles et techniques de sécurité pour les déploiements MCP
- **[Référence rapide des bonnes pratiques MCP](./mcp-best-practices.md)** - Guide de référence rapide pour les pratiques essentielles de sécurité MCP

---

## Et ensuite

Suivant : [Chapitre 3 : Premiers pas](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->