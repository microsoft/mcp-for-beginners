# 🚀 Serveur MCP avec PostgreSQL - Guide complet d'apprentissage

## 🧠 Vue d'ensemble du parcours d'intégration de base de données MCP

Ce guide d'apprentissage complet vous enseigne comment construire des **serveurs Model Context Protocol (MCP)** prêts pour la production qui s'intègrent avec des bases de données via une mise en œuvre pratique d'analytique retail. Vous apprendrez des modèles de qualité entreprise incluant la **Sécurité au niveau des lignes (RLS)**, la **recherche sémantique**, l'**intégration Azure AI** et l'**accès multi-tenant aux données**.

Que vous soyez développeur backend, ingénieur IA ou architecte de données, ce guide offre un apprentissage structuré avec des exemples réels et des exercices pratiques vous guidant à travers le serveur MCP suivant https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Ressources officielles MCP

- 📘 [Documentation MCP](https://modelcontextprotocol.io/) – Tutoriels détaillés et guides utilisateurs
- 📜 [Spécification MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Architecture du protocole et références techniques
- 🧑‍💻 [Dépôt GitHub MCP](https://github.com/modelcontextprotocol) – SDK open-source, outils et exemples de code
- 🌐 [Communauté MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Participez aux discussions et contribuez à la communauté
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Meilleures pratiques de sécurité et atténuations des risques


## 🧭 Parcours d'intégration de base de données MCP

### 📚 Structure complète d'apprentissage pour https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Lab | Sujet | Description | Lien |
|--------|-------|-------------|------|
| **Lab 1-3 : Fondations** | | | |
| 00 | [Introduction à l'intégration de base de données MCP](./00-Introduction/README.md) | Vue d'ensemble de MCP avec intégration base de données et cas d'utilisation retail analytique | [Commencer ici](./00-Introduction/README.md) |
| 01 | [Concepts d'architecture de base](./01-Architecture/README.md) | Compréhension de l'architecture serveur MCP, couches base de données et modèles de sécurité | [Apprendre](./01-Architecture/README.md) |
| 02 | [Sécurité et multi-tenant](./02-Security/README.md) | Sécurité au niveau des lignes, authentification, et accès multi-tenant aux données | [Apprendre](./02-Security/README.md) |
| 03 | [Configuration de l'environnement](./03-Setup/README.md) | Mise en place de l'environnement de développement, Docker, ressources Azure | [Configurer](./03-Setup/README.md) |
| **Lab 4-6 : Construction du serveur MCP** | | | |
| 04 | [Conception de base de données et schéma](./04-Database/README.md) | Configuration PostgreSQL, conception du schéma retail et données exemples | [Construire](./04-Database/README.md) |
| 05 | [Implémentation du serveur MCP](./05-MCP-Server/README.md) | Construction du serveur FastMCP avec intégration base de données | [Construire](./05-MCP-Server/README.md) |
| 06 | [Développement d'outils](./06-Tools/README.md) | Création d'outils de requête base de données et introspection de schéma | [Construire](./06-Tools/README.md) |
| **Lab 7-9 : Fonctionnalités avancées** | | | |
| 07 | [Intégration de recherche sémantique](./07-Semantic-Search/README.md) | Mise en œuvre des embeddings vectoriels avec Azure OpenAI et pgvector | [Avancer](./07-Semantic-Search/README.md) |
| 08 | [Tests et débogage](./08-Testing/README.md) | Stratégies de test, outils de débogage et approches de validation | [Tester](./08-Testing/README.md) |
| 09 | [Intégration VS Code](./09-VS-Code/README.md) | Configuration de l'intégration MCP dans VS Code et utilisation du chat AI | [Intégrer](./09-VS-Code/README.md) |
| **Lab 10-12 : Production et bonnes pratiques** | | | |
| 10 | [Stratégies de déploiement](./10-Deployment/README.md) | Déploiement Docker, Azure Container Apps, et considérations de scalabilité | [Déployer](./10-Deployment/README.md) |
| 11 | [Surveillance et observabilité](./11-Monitoring/README.md) | Application Insights, journalisation, surveillance des performances | [Surveiller](./11-Monitoring/README.md) |
| 12 | [Bonnes pratiques et optimisation](./12-Best-Practices/README.md) | Optimisation des performances, renforcement de la sécurité et astuces pour la production | [Optimiser](./12-Best-Practices/README.md) |

### 💻 Ce que vous construirez

À la fin de ce parcours, vous aurez construit un **serveur MCP Zava Retail Analytics complet** comprenant :

- **Base de données retail multi-tables** avec commandes clients, produits et inventaire
- **Sécurité au niveau des lignes** pour l'isolation des données par magasin
- **Recherche sémantique de produits** utilisant les embeddings Azure OpenAI
- **Intégration du chat AI dans VS Code** pour requêtes en langage naturel
- **Déploiement prêt pour la production** avec Docker et Azure
- **Surveillance complète** avec Application Insights

## 🎯 Prérequis pour l'apprentissage

Pour tirer le meilleur parti de ce parcours, vous devriez avoir :

- **Expérience en programmation** : Familiarité avec Python (préféré) ou langages similaires
- **Connaissances en base de données** : Compréhension basique du SQL et des bases relationnelles
- **Concepts API** : Compréhension des API REST et concepts HTTP
- **Outils de développement** : Expérience avec la ligne de commande, Git et éditeurs de code
- **Bases du cloud** : (Optionnel) Connaissance basique d'Azure ou plateformes cloud similaires
- **Familiarité Docker** : (Optionnel) Compréhension des concepts de conteneurisation

### Outils requis

- **Docker Desktop** - Pour faire tourner PostgreSQL et le serveur MCP
- **Azure CLI** - Pour déploiement des ressources cloud
- **VS Code** - Pour développement et intégration MCP
- **Git** - Pour contrôle de version
- **Python 3.8+** - Pour développement serveur MCP

## 📚 Guide d'étude et ressources

Ce parcours inclut des ressources complètes pour vous guider efficacement :

### Guide d'étude

Chaque lab comprend :
- **Objectifs d'apprentissage clairs** - Ce que vous atteindrez
- **Instructions pas à pas** - Guides détaillés de mise en œuvre
- **Exemples de code** - Exemples fonctionnels avec explications
- **Exercices** - Opportunités de pratique concrète
- **Guides de dépannage** - Problèmes courants et solutions
- **Ressources supplémentaires** - Lectures et explorations complémentaires

### Vérification des prérequis

Avant de commencer chaque lab, vous trouverez :
- **Connaissances requises** - Ce que vous devez maîtriser au préalable
- **Validation de configuration** - Comment vérifier votre environnement
- **Estimation de temps** - Temps prévu pour compléter
- **Résultats d'apprentissage** - Ce que vous saurez à la fin

### Parcours d'apprentissage recommandés

Choisissez votre parcours selon votre niveau d'expérience :

#### 🟢 **Parcours débutant** (Nouveau en MCP)
1. Assurez-vous d'avoir complété les labs 0-10 de [MCP pour débutants](https://aka.ms/mcp-for-beginners) d'abord
2. Faites les labs 00-03 pour renforcer vos bases
3. Suivez les labs 04-06 pour construire concrètement
4. Essayez les labs 07-09 pour une utilisation pratique

#### 🟡 **Parcours intermédiaire** (Quelques expériences MCP)
1. Revoyez les labs 00-01 pour concepts liés à la base de données
2. Concentrez-vous sur les labs 02-06 pour l'implémentation
3. Approfondissez avec les labs 07-12 pour les fonctionnalités avancées

#### 🔴 **Parcours avancé** (Expérimenté avec MCP)
1. Parcourez rapidement les labs 00-03 pour le contexte
2. Focalisez-vous sur les labs 04-09 pour l'intégration base de données
3. Concentrez-vous sur les labs 10-12 pour le déploiement en production

## 🛠️ Comment utiliser ce parcours d'apprentissage efficacement

### Apprentissage séquentiel (recommandé)

Parcourez les labs dans l'ordre pour une compréhension complète :

1. **Lisez la vue d'ensemble** - Comprenez ce que vous allez apprendre
2. **Vérifiez les prérequis** - Assurez-vous de posséder les connaissances requises
3. **Suivez les guides pas à pas** - Implémentez au fur et à mesure
4. **Complétez les exercices** - Renforcez votre compréhension
5. **Revoyez les points clés** - Consolidez les résultats d'apprentissage

### Apprentissage ciblé

Si vous avez besoin de compétences spécifiques :

- **Intégration base de données** : Concentrez-vous sur les labs 04-06
- **Implémentation sécurité** : Privilégiez les labs 02, 08, 12
- **IA / Recherche sémantique** : Approfondissez le lab 07
- **Déploiement en production** : Étudiez les labs 10-12

### Pratique concrète

Chaque lab inclut :
- **Exemples de code fonctionnels** - Copier, modifier et expérimenter
- **Scénarios réels** - Cas d'utilisation pratiques d'analytique retail
- **Complexité progressive** - Construction du simple au avancé
- **Étapes de validation** - Vérifiez que votre implantation fonctionne

## 🌟 Communauté et support

### Obtenez de l'aide

- **Discord Azure AI** : [Rejoignez pour support expert](https://discord.com/invite/ByRwuEEgH4)
- **Dépôt GitHub et exemple d'implémentation** : [Exemples de déploiement et ressources](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Communauté MCP** : [Rejoignez les discussions MCP plus larges](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Prêt à commencer ?

Commencez votre parcours avec **[Lab 00 : Introduction à l'intégration de base de données MCP](./00-Introduction/README.md)**

---

*Maîtrisez la construction de serveurs MCP prêts pour la production avec intégration base de données à travers cette expérience d'apprentissage complète et pratique.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->