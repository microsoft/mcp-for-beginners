# Introduction à l'intégration de bases de données avec MCP

## 🎯 Ce que couvre ce laboratoire

Ce laboratoire d'introduction offre une vue d'ensemble complète sur la création de serveurs Model Context Protocol (MCP) avec intégration de bases de données. Vous comprendrez le cas d'usage métier, l'architecture technique et les applications concrètes à travers l'exemple analytique de Zava Retail disponible sur https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Vue d'ensemble

Le **Model Context Protocol (MCP)** permet aux assistants IA d'accéder de manière sécurisée et d'interagir avec des sources de données externes en temps réel. Lorsqu'il est combiné à une intégration de bases de données, MCP débloque des capacités puissantes pour des applications IA basées sur les données.

Ce parcours d'apprentissage vous enseigne à construire des serveurs MCP prêts pour la production, connectant des assistants IA aux données de ventes au détail via PostgreSQL, tout en mettant en œuvre des modèles d'entreprise tels que la sécurité au niveau des lignes (Row Level Security), la recherche sémantique et l'accès multi-locataires aux données.

## Objectifs d'apprentissage

À la fin de ce laboratoire, vous serez capable de :

- **Définir** le Model Context Protocol et ses principaux avantages pour l'intégration de bases de données
- **Identifier** les composants clés d'une architecture de serveur MCP avec bases de données
- **Comprendre** le cas d'usage de Zava Retail et ses exigences métier
- **Reconnaître** les modèles d'entreprise pour un accès sécurisé et évolutif aux bases de données
- **Lister** les outils et technologies utilisés tout au long de ce parcours d'apprentissage

## 🧭 Le défi : l'IA face aux données du monde réel

### Limites traditionnelles de l'IA

Les assistants IA modernes sont extrêmement puissants, mais ils rencontrent des limites importantes lorsqu'ils travaillent avec des données métier réelles :

| **Défi**            | **Description**                                      | **Impact métier**                     |
|----------------------|------------------------------------------------------|---------------------------------------|
| **Connaissances statiques** | Les modèles IA entraînés sur des ensembles de données fixes ne peuvent pas accéder aux données métier actuelles | Informations obsolètes, opportunités manquées |
| **Silos de données** | Informations enfermées dans des bases de données, API et systèmes inaccessibles à l'IA | Analyses incomplètes, workflows fragmentés |
| **Contraintes de sécurité** | L'accès direct aux bases de données soulève des préoccupations de sécurité et de conformité | Déploiement limité, préparation manuelle des données |
| **Requêtes complexes** | Les utilisateurs métier ont besoin de connaissances techniques pour extraire des informations | Adoption réduite, processus inefficaces |

### La solution MCP

Le Model Context Protocol répond à ces défis en offrant :

- **Accès en temps réel aux données** : Les assistants IA interrogent des bases de données et API en direct
- **Intégration sécurisée** : Accès contrôlé avec authentification et permissions
- **Interface en langage naturel** : Les utilisateurs posent des questions en anglais simple
- **Protocole standardisé** : Fonctionne avec différentes plateformes et outils IA

## 🏪 Découvrez Zava Retail : notre étude de cas https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Tout au long de ce parcours d'apprentissage, nous construirons un serveur MCP pour **Zava Retail**, une chaîne fictive de magasins de bricolage avec plusieurs emplacements. Ce scénario réaliste illustre une mise en œuvre MCP de niveau entreprise.

### Contexte métier

**Zava Retail** exploite :
- **8 magasins physiques** dans l'État de Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 magasin en ligne** pour les ventes e-commerce
- **Un catalogue de produits diversifié** comprenant outils, matériel, fournitures de jardin et matériaux de construction
- **Une gestion à plusieurs niveaux** avec des responsables de magasin, des responsables régionaux et des cadres

### Exigences métier

Les responsables de magasin et les cadres ont besoin d'analyses IA pour :

1. **Analyser les performances de vente** entre magasins et périodes
2. **Suivre les niveaux de stock** et identifier les besoins de réapprovisionnement
3. **Comprendre le comportement des clients** et les tendances d'achat
4. **Découvrir des informations sur les produits** via la recherche sémantique
5. **Générer des rapports** avec des requêtes en langage naturel
6. **Maintenir la sécurité des données** grâce au contrôle d'accès basé sur les rôles

### Exigences techniques

Le serveur MCP doit fournir :

- **Accès multi-locataires aux données**, où les responsables de magasin ne voient que les données de leur magasin
- **Requêtes flexibles** prenant en charge des opérations SQL complexes
- **Recherche sémantique** pour la découverte et les recommandations de produits
- **Données en temps réel** reflétant l'état actuel de l'entreprise
- **Authentification sécurisée** avec sécurité au niveau des lignes
- **Architecture évolutive** prenant en charge plusieurs utilisateurs simultanés

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

#### **1. Couche serveur MCP**
- **Framework FastMCP** : Implémentation moderne de serveur MCP en Python
- **Enregistrement des outils** : Définitions d'outils déclaratives avec typage sécurisé
- **Contexte des requêtes** : Gestion de l'identité utilisateur et des sessions
- **Gestion des erreurs** : Gestion robuste des erreurs et journalisation

#### **2. Couche d'intégration de bases de données**
- **Pooling de connexions** : Gestion efficace des connexions asyncpg
- **Fournisseur de schéma** : Découverte dynamique des schémas de tables
- **Exécuteur de requêtes** : Exécution SQL sécurisée avec contexte RLS
- **Gestion des transactions** : Conformité ACID et gestion des rollbacks

#### **3. Couche de sécurité**
- **Sécurité au niveau des lignes** : RLS PostgreSQL pour l'isolation des données multi-locataires
- **Identité utilisateur** : Authentification et autorisation des responsables de magasin
- **Contrôle d'accès** : Permissions granulaires et pistes d'audit
- **Validation des entrées** : Prévention des injections SQL et validation des requêtes

#### **4. Couche d'amélioration IA**
- **Recherche sémantique** : Embeddings vectoriels pour la découverte de produits
- **Intégration Azure OpenAI** : Génération d'embeddings textuels
- **Algorithmes de similarité** : Recherche de similarité cosine avec pgvector
- **Optimisation de la recherche** : Indexation et optimisation des performances

## 🔧 Pile technologique

### Technologies principales

| **Composant**        | **Technologie**          | **Objectif**                     |
|-----------------------|--------------------------|-----------------------------------|
| **Framework MCP**     | FastMCP (Python)        | Implémentation moderne de serveur MCP |
| **Base de données**   | PostgreSQL 17 + pgvector | Données relationnelles avec recherche vectorielle |
| **Services IA**       | Azure OpenAI            | Embeddings textuels et modèles de langage |
| **Conteneurisation**  | Docker + Docker Compose | Environnement de développement   |
| **Plateforme cloud**  | Microsoft Azure         | Déploiement en production        |
| **Intégration IDE**   | VS Code                 | Chat IA et workflow de développement |

### Outils de développement

| **Outil**             | **Objectif**            |
|-----------------------|--------------------------|
| **asyncpg**           | Pilote PostgreSQL haute performance |
| **Pydantic**          | Validation et sérialisation des données |
| **Azure SDK**         | Intégration des services cloud |
| **pytest**            | Framework de tests      |
| **Docker**            | Conteneurisation et déploiement |

### Pile de production

| **Service**           | **Ressource Azure**     | **Objectif**                     |
|-----------------------|--------------------------|-----------------------------------|
| **Base de données**   | Azure Database for PostgreSQL | Service de base de données managé |
| **Conteneur**         | Azure Container Apps    | Hébergement de conteneurs serverless |
| **Services IA**       | Azure AI Foundry        | Modèles OpenAI et points de terminaison |
| **Surveillance**      | Application Insights    | Observabilité et diagnostics     |
| **Sécurité**          | Azure Key Vault         | Gestion des secrets et configurations |

## 🎬 Scénarios d'utilisation concrets

Explorons comment différents utilisateurs interagissent avec notre serveur MCP :

### Scénario 1 : Revue des performances par un responsable de magasin

**Utilisateur** : Sarah, responsable du magasin de Seattle  
**Objectif** : Analyser les performances de vente du dernier trimestre

**Requête en langage naturel** :  
> "Montre-moi les 10 produits les plus rentables pour mon magasin au T4 2024"

**Ce qui se passe** :
1. Le chat IA de VS Code envoie la requête au serveur MCP
2. Le serveur MCP identifie le contexte du magasin de Sarah (Seattle)
3. Les politiques RLS filtrent les données pour le magasin de Seattle uniquement
4. Une requête SQL est générée et exécutée
5. Les résultats sont formatés et renvoyés au chat IA
6. L'IA fournit une analyse et des insights

### Scénario 2 : Découverte de produits avec recherche sémantique

**Utilisateur** : Mike, responsable des stocks  
**Objectif** : Trouver des produits similaires à une demande client

**Requête en langage naturel** :  
> "Quels produits vendons-nous qui ressemblent à 'connecteurs électriques étanches pour usage extérieur' ?"

**Ce qui se passe** :
1. La requête est traitée par l'outil de recherche sémantique
2. Azure OpenAI génère un vecteur d'embedding
3. pgvector effectue une recherche de similarité
4. Les produits associés sont classés par pertinence
5. Les résultats incluent les détails des produits et leur disponibilité
6. L'IA suggère des alternatives et des opportunités de regroupement

### Scénario 3 : Analyse inter-magasins

**Utilisateur** : Jennifer, responsable régionale  
**Objectif** : Comparer les performances entre tous les magasins

**Requête en langage naturel** :  
> "Compare les ventes par catégorie pour tous les magasins au cours des 6 derniers mois"

**Ce qui se passe** :
1. Le contexte RLS est défini pour l'accès du responsable régional
2. Une requête complexe multi-magasins est générée
3. Les données sont agrégées entre les emplacements des magasins
4. Les résultats incluent des tendances et des comparaisons
5. L'IA identifie des insights et des recommandations

## 🔒 Analyse approfondie de la sécurité et de la multi-location

Notre implémentation met l'accent sur une sécurité de niveau entreprise :

### Sécurité au niveau des lignes (RLS)

La RLS PostgreSQL garantit l'isolation des données :

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
- **ID du responsable de magasin** : Identifiant unique pour le contexte RLS
- **Attribution de rôles** : Permissions et niveaux d'accès
- **Gestion des sessions** : Jetons d'authentification sécurisés
- **Journalisation des audits** : Historique complet des accès

### Protection des données

Plusieurs couches de sécurité :
- **Chiffrement des connexions** : TLS pour toutes les connexions à la base de données
- **Prévention des injections SQL** : Requêtes paramétrées uniquement
- **Validation des entrées** : Validation complète des requêtes
- **Gestion des erreurs** : Aucune donnée sensible dans les messages d'erreur

## 🎯 Points clés à retenir

Après avoir terminé cette introduction, vous devriez comprendre :

✅ **Proposition de valeur de MCP** : Comment MCP relie les assistants IA et les données du monde réel  
✅ **Contexte métier** : Les exigences et défis de Zava Retail  
✅ **Vue d'ensemble de l'architecture** : Composants clés et leurs interactions  
✅ **Pile technologique** : Outils et frameworks utilisés tout au long  
✅ **Modèle de sécurité** : Accès multi-locataires et protection des données  
✅ **Modèles d'utilisation** : Scénarios de requêtes réels et workflows  

## 🚀 Et après ?

Prêt à aller plus loin ? Continuez avec :

**[Lab 01 : Concepts fondamentaux de l'architecture](../01-Architecture/README.md)**

Apprenez les modèles d'architecture des serveurs MCP, les principes de conception des bases de données et la mise en œuvre technique détaillée qui alimente notre solution analytique pour le commerce de détail.

## 📚 Ressources supplémentaires

### Documentation MCP
- [Spécification MCP](https://modelcontextprotocol.io/docs/) - Documentation officielle du protocole
- [MCP pour débutants](https://aka.ms/mcp-for-beginners) - Guide complet d'apprentissage MCP
- [Documentation FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentation du SDK Python

### Intégration de bases de données
- [Documentation PostgreSQL](https://www.postgresql.org/docs/) - Référence complète de PostgreSQL
- [Guide pgvector](https://github.com/pgvector/pgvector) - Documentation de l'extension vectorielle
- [Sécurité au niveau des lignes](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guide RLS PostgreSQL

### Services Azure
- [Documentation Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Intégration des services IA
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Service de base de données managé
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Conteneurs serverless

---

**Avertissement** : Ceci est un exercice d'apprentissage utilisant des données fictives de commerce de détail. Suivez toujours les politiques de gouvernance et de sécurité des données de votre organisation lors de la mise en œuvre de solutions similaires en environnement de production.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.