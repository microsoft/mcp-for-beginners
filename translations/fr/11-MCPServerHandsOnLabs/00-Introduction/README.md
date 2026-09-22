# Introduction à l'intégration de base de données MCP

> [!NOTE]
> Les diagrammes ou le code de ce parcours d'apprentissage qui utilisent HTTP/SSE ou les options d'initialisation
> reflètent les dépendances MCP `2025-11-25` de l'exemple. Pour les nouvelles
> implémentations, utilisez les requêtes sans état `2026-07-28` et HTTP Streamable.

## 🎯 Ce que ce laboratoire couvre

Ce laboratoire d'introduction offre un aperçu complet de la construction de serveurs Model Context Protocol (MCP) avec intégration de base de données. Vous comprendrez le cas d'utilisation commerciale, l'architecture technique et les applications réelles à travers l'exemple analytique Zava Retail disponible sur https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Vue d'ensemble

**Model Context Protocol (MCP)** permet aux assistants IA d'accéder et d'interagir de manière sécurisée avec des sources de données externes en temps réel. Combiné avec l'intégration de bases de données, MCP débloque des capacités puissantes pour des applications d'IA basées sur les données.

Ce parcours d'apprentissage vous enseigne comment créer des serveurs MCP prêts pour la production qui connectent les assistants IA aux données de ventes de détail via PostgreSQL, en mettant en œuvre des modèles d'entreprise tels que la sécurité au niveau des lignes, la recherche sémantique et l'accès multi-tenant aux données.

## Objectifs d'apprentissage

À la fin de ce laboratoire, vous serez capable de :

- **Définir** le Model Context Protocol et ses avantages principaux pour l'intégration de bases de données
- **Identifier** les composants clés d'une architecture de serveur MCP avec bases de données
- **Comprendre** le cas d'utilisation Zava Retail et ses exigences business
- **Reconnaître** les modèles d'entreprise pour un accès sécurisé et évolutif aux bases de données
- **Lister** les outils et technologies utilisés tout au long de ce parcours

## 🧭 Le défi : L'IA face aux données du monde réel

### Limites traditionnelles de l'IA

Les assistants IA modernes sont incroyablement puissants mais rencontrent des limites importantes lorsqu'ils travaillent avec des données métier réelles :

| **Défi** | **Description** | **Impact Business** |
|---------------|-----------------|-------------------|
| **Connaissances statiques** | Les modèles IA entraînés sur des jeux de données fixes ne peuvent pas accéder aux données métier actuelles | Informations obsolètes, opportunités manquées |
| **Silos de données** | Informations enfermées dans les bases de données, API et systèmes inaccessibles à l'IA | Analyse incomplète, flux de travail fragmentés |
| **Contraintes de sécurité** | L'accès direct aux bases de données soulève des questions de sécurité et conformité | Déploiement limité, préparation manuelle des données |
| **Requêtes complexes** | Les utilisateurs métiers ont besoin de compétences techniques pour extraire les insights | Adoption réduite, processus inefficaces |

### La solution MCP

Model Context Protocol répond à ces défis en fournissant :

- **Accès aux données en temps réel** : Les assistants IA interrogent des bases de données et API vivantes
- **Intégration sécurisée** : Accès contrôlé via authentification et permissions
- **Interface en langage naturel** : Les utilisateurs métiers posent des questions en anglais simple
- **Protocole standardisé** : Fonctionne à travers différentes plateformes et outils IA

## 🏪 Présentation de Zava Retail : notre cas d'étude https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Tout au long de ce parcours, nous construirons un serveur MCP pour **Zava Retail**, une chaîne fictive de bricolage avec plusieurs magasins. Ce scénario réaliste montre une implémentation MCP de qualité entreprise.

### Contexte métier

**Zava Retail** opère :
- **8 magasins physiques** dans l'État de Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 magasin en ligne** pour les ventes e-commerce
- **Catalogue produit diversifié** incluant outils, quincaillerie, fournitures de jardin et matériaux de construction
- **Gestion multi-niveaux** avec directeurs de magasin, gestionnaires régionaux et cadres

### Exigences métier

Les directeurs de magasin et cadres ont besoin d'analyses propulsées par IA pour :

1. **Analyser la performance des ventes** entre magasins et périodes
2. **Suivre les niveaux de stock** et identifier les besoins de réapprovisionnement
3. **Comprendre le comportement client** et les tendances d'achat
4. **Découvrir des insights produits** via la recherche sémantique
5. **Générer des rapports** avec des requêtes en langage naturel
6. **Maintenir la sécurité des données** avec un contrôle d'accès basé sur les rôles

### Exigences techniques

Le serveur MCP doit fournir :

- **Accès multi-tenant aux données** où les directeurs de magasin ne voient que les données de leur magasin
- **Requêtage flexible** supportant des opérations SQL complexes
- **Recherche sémantique** pour la découverte de produits et recommandations
- **Données en temps réel** reflétant l'état commercial actuel
- **Authentification sécurisée** avec sécurité au niveau des lignes (RLS)
- **Architecture évolutive** supportant plusieurs utilisateurs concurrents

## 🏗️ Vue d'ensemble de l'architecture du serveur MCP

Notre serveur MCP met en œuvre une architecture en couches optimisée pour l'intégration de bases de données :

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Composants clés

#### **1. Couche Serveur MCP**
- **Framework FastMCP** : Implémentation moderne du serveur MCP en Python
- **Enregistrement des outils** : Définitions déclaratives d'outils avec sécurité de type
- **Contexte des requêtes** : Gestion de l'identité utilisateur et de session
- **Gestion des erreurs** : Gestion et journalisation robuste des erreurs

#### **2. Couche d'intégration Base de données**
- **Pool de connexions** : Gestion efficace des connexions asyncpg
- **Fournisseur de schéma** : Découverte dynamique des schémas de tables
- **Exécutant de requêtes** : Exécution SQL sécurisée avec contexte RLS
- **Gestion des transactions** : Conformité ACID et gestion des rollback

#### **3. Couche Sécurité**
- **Sécurité au niveau des lignes** : RLS PostgreSQL pour isolation multi-tenant des données
- **Identité utilisateur** : Authentification et autorisation des directeurs de magasin
- **Contrôle d'accès** : Permissions fines et pistes d'audit
- **Validation des entrées** : Prévention des injections SQL et validation des requêtes

#### **4. Couche d'amélioration IA**
- **Recherche sémantique** : Embeddings vectoriels pour la découverte produit
- **Intégration Azure OpenAI** : Génération d'embeddings textuels
- **Algorithmes de similarité** : Recherche cosinus de similarité pgvector
- **Optimisation de la recherche** : Indexation et tuning des performances

## 🔧 Stack technologique

### Technologies principales

| **Composant** | **Technologie** | **But** |
|---------------|----------------|-------------|
| **Framework MCP** | FastMCP (Python) | Implémentation moderne du serveur MCP |
| **Base de données** | PostgreSQL 17 + pgvector | Données relationnelles avec recherche vectorielle |
| **Services IA** | Azure OpenAI | Embeddings textuels et modèles de langage |
| **Containerisation** | Docker + Docker Compose | Environnement de développement |
| **Plateforme Cloud** | Microsoft Azure | Déploiement en production |
| **Intégration IDE** | VS Code | Chat IA et workflow de développement |

### Outils de développement

| **Outil** | **Objectif** |
|----------|-------------|
| **asyncpg** | Pilote performant PostgreSQL |
| **Pydantic** | Validation et sérialisation de données |
| **Azure SDK** | Intégration des services cloud |
| **pytest** | Framework de tests |
| **Docker** | Containerisation et déploiement |

### Stack de production

| **Service** | **Ressource Azure** | **But** |
|-------------|-------------------|-------------|
| **Base de données** | Azure Database for PostgreSQL | Service de base de données managé |
| **Container** | Azure Container Apps | Hébergement de conteneurs serverless |
| **Services IA** | Microsoft Foundry | Modèles et endpoints OpenAI |
| **Surveillance** | Application Insights | Observabilité et diagnostic |
| **Sécurité** | Azure Key Vault | Gestion des secrets et configuration |

## 🎬 Scénarios d'usage réels

Explorons comment différents utilisateurs interagissent avec notre serveur MCP :

### Scénario 1 : Revue de performance du directeur de magasin

**Utilisateur** : Sarah, directrice du magasin de Seattle  
**Objectif** : Analyser les ventes du dernier trimestre

**Requête en langage naturel** :
> "Montre-moi les 10 produits principaux par chiffre d'affaires pour mon magasin au T4 2024"

**Ce qui se passe** :
1. Le chat IA de VS Code envoie la requête au serveur MCP
2. Le serveur MCP identifie le contexte du magasin de Sarah (Seattle)
3. Les politiques RLS filtrent les données pour le magasin de Seattle uniquement
4. La requête SQL est générée et exécutée
5. Les résultats sont formatés et renvoyés au chat IA
6. L'IA fournit analyse et insights

### Scénario 2 : Découverte produit avec recherche sémantique

**Utilisateur** : Mike, gestionnaire des stocks  
**Objectif** : Trouver des produits similaires à une demande client

**Requête en langage naturel** :
> "Quels produits vendons-nous qui sont similaires à 'connecteurs électriques étanches pour usage extérieur' ?"

**Ce qui se passe** :
1. La requête est traitée par l’outil de recherche sémantique
2. Azure OpenAI génère un vecteur d'embedding
3. pgvector réalise une recherche de similarité
4. Les produits liés sont classés par pertinence
5. Les résultats incluent détails produit et disponibilité
6. L'IA suggère des alternatives et des opportunités de bundling

### Scénario 3 : Analyse multi-magasins

**Utilisateur** : Jennifer, gestionnaire régional  
**Objectif** : Comparer les performances de tous les magasins

**Requête en langage naturel** :
> "Compare les ventes par catégorie pour tous les magasins sur les 6 derniers mois"

**Ce qui se passe** :
1. Le contexte RLS est défini pour l'accès du gestionnaire régional
2. Une requête multi-magasin complexe est générée
3. Les données sont agrégées à travers les sites
4. Les résultats incluent tendances et comparaisons
5. L'IA identifie insights et recommandations

## 🔒 Sécurité et multi-tenancy en détail

Notre implémentation priorise la sécurité de niveau entreprise :

### Sécurité au niveau des lignes (RLS)

PostgreSQL RLS garantit l'isolation des données :

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Gestion de l'identité utilisateur

Chaque connexion MCP inclut :
- **ID du directeur de magasin** : Identifiant unique pour le contexte RLS
- **Attribution des rôles** : Permissions et niveaux d'accès
- **Gestion des sessions** : Jetons d'authentification sécurisés
- **Journalisation d'audit** : Historique complet des accès

### Protection des données

Plusieurs couches de sécurité :
- **Chiffrement des connexions** : TLS pour toutes les connexions base de données
- **Prévention des injections SQL** : Requêtes paramétrées uniquement
- **Validation des entrées** : Validation complète des requêtes
- **Gestion des erreurs** : Pas de données sensibles dans les messages d'erreur

## 🎯 Points clés à retenir

Après avoir terminé cette introduction, vous devriez comprendre :

✅ **Proposition de valeur MCP** : Comment MCP relie assistants IA et données réelles  
✅ **Contexte métier** : Exigences et défis de Zava Retail  
✅ **Vue architecturale** : Composants clés et interactions  
✅ **Stack technologique** : Outils et frameworks utilisés  
✅ **Modèle de sécurité** : Accès multi-tenant et protection des données  
✅ **Modèles d’usage** : Scénarios réels de requêtes et workflows  

## 🚀 Et ensuite

Prêt à approfondir ? Continuez avec :

**[Lab 01 : Concepts d'architecture de base](../01-Architecture/README.md)**

Découvrez les modèles d'architecture serveur MCP, les principes de conception de base de données et l'implémentation technique détaillée qui alimente notre solution d'analyse retail.

## 📚 Ressources supplémentaires

### Documentation MCP
- [Spécification MCP](https://modelcontextprotocol.io/docs/) - Documentation officielle du protocole
- [MCP pour débutants](https://aka.ms/mcp-for-beginners) - Guide d'apprentissage complet MCP
- [Documentation FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentation SDK Python

### Intégration Base de données
- [Documentation PostgreSQL](https://www.postgresql.org/docs/) - Référence complète PostgreSQL
- [Guide pgvector](https://github.com/pgvector/pgvector) - Documentation de l'extension vectorielle
- [Sécurité au niveau des lignes](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guide PostgreSQL RLS

### Services Azure
- [Documentation Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Intégration des services IA
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Service de base de données managé
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Conteneurs serverless

---

**Avertissement** : Il s'agit d'un exercice d'apprentissage utilisant des données retail fictives. Respectez toujours les politiques de gouvernance et de sécurité des données de votre organisation lors de la mise en œuvre de solutions similaires en production.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->