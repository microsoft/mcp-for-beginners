# Introduction au protocole de contexte de modèle (MCP) : Pourquoi il est essentiel pour des applications IA évolutives

[![Introduction au protocole de contexte de modèle](../../../translated_images/fr/01.a467036d886b5fb5.webp)](https://youtu.be/agBbdiOPLQA)

_(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

Les applications d'IA générative représentent une avancée majeure, car elles permettent souvent à l'utilisateur d'interagir avec l'application via des invites en langage naturel. Cependant, à mesure que davantage de temps et de ressources sont investis dans ces applications, il est crucial de garantir une intégration facile des fonctionnalités et des ressources, de manière à ce qu'elles soient extensibles, capables de prendre en charge plusieurs modèles et de gérer les complexités spécifiques à chaque modèle. En bref, construire des applications d'IA générative est simple au départ, mais à mesure qu'elles se développent et deviennent plus complexes, il devient nécessaire de définir une architecture et probablement de s'appuyer sur une norme pour garantir une construction cohérente. C'est là que le MCP intervient pour organiser les choses et fournir une norme.

---

## **🔍 Qu'est-ce que le protocole de contexte de modèle (MCP) ?**

Le **protocole de contexte de modèle (MCP)** est une **interface ouverte et standardisée** qui permet aux modèles de langage étendu (LLMs) d'interagir de manière fluide avec des outils externes, des API et des sources de données. Il offre une architecture cohérente pour améliorer les fonctionnalités des modèles d'IA au-delà de leurs données d'entraînement, permettant des systèmes d'IA plus intelligents, évolutifs et réactifs.

---

## **🎯 Pourquoi la standardisation dans l'IA est importante**

À mesure que les applications d'IA générative deviennent plus complexes, il est essentiel d'adopter des normes qui garantissent **l'évolutivité, l'extensibilité, la maintenabilité** et **l'évitement de l'enfermement propriétaire**. Le MCP répond à ces besoins en :

- Unifiant les intégrations entre modèles et outils
- Réduisant les solutions personnalisées fragiles et ponctuelles
- Permettant à plusieurs modèles de différents fournisseurs de coexister dans un même écosystème

**Note :** Bien que le MCP se présente comme une norme ouverte, il n'existe aucun plan pour le standardiser via des organismes de normalisation existants tels que IEEE, IETF, W3C, ISO ou tout autre organisme de normalisation.

---

## **📚 Objectifs d'apprentissage**

À la fin de cet article, vous serez capable de :

- Définir le **protocole de contexte de modèle (MCP)** et ses cas d'utilisation
- Comprendre comment le MCP standardise la communication entre modèles et outils
- Identifier les composants principaux de l'architecture MCP
- Explorer des applications concrètes du MCP dans des contextes d'entreprise et de développement

---

## **💡 Pourquoi le protocole de contexte de modèle (MCP) est révolutionnaire**

### **🔗 Le MCP résout la fragmentation dans les interactions IA**

Avant le MCP, intégrer des modèles avec des outils nécessitait :

- Du code personnalisé pour chaque paire outil-modèle
- Des API non standard pour chaque fournisseur
- Des interruptions fréquentes dues aux mises à jour
- Une évolutivité limitée avec davantage d'outils

### **✅ Avantages de la standardisation MCP**

| **Avantage**              | **Description**                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Interopérabilité          | Les LLMs fonctionnent de manière fluide avec des outils de différents fournisseurs |
| Cohérence                 | Comportement uniforme sur les plateformes et outils                            |
| Réutilisabilité           | Les outils créés une fois peuvent être utilisés dans plusieurs projets et systèmes |
| Développement accéléré    | Réduction du temps de développement grâce à des interfaces standardisées et prêtes à l'emploi |

---

## **🧱 Aperçu de l'architecture MCP à haut niveau**

Le MCP suit un modèle **client-serveur**, où :

- Les **hôtes MCP** exécutent les modèles d'IA
- Les **clients MCP** initient les requêtes
- Les **serveurs MCP** fournissent le contexte, les outils et les capacités

### **Composants clés :**

- **Ressources** – Données statiques ou dynamiques pour les modèles  
- **Prompts** – Flux de travail prédéfinis pour une génération guidée  
- **Outils** – Fonctions exécutables comme la recherche, les calculs  
- **Échantillonnage** – Comportement agentique via des interactions récursives  

---

## Comment fonctionnent les serveurs MCP

Les serveurs MCP fonctionnent de la manière suivante :

- **Flux de requêtes** :
    1. Une requête est initiée par un utilisateur final ou un logiciel agissant en son nom.
    2. Le **client MCP** envoie la requête à un **hôte MCP**, qui gère l'exécution du modèle d'IA.
    3. Le **modèle d'IA** reçoit l'invite utilisateur et peut demander l'accès à des outils ou données externes via un ou plusieurs appels d'outils.
    4. L'**hôte MCP**, et non directement le modèle, communique avec les **serveurs MCP** appropriés en utilisant le protocole standardisé.
- **Fonctionnalités de l'hôte MCP** :
    - **Registre d'outils** : Maintient un catalogue des outils disponibles et de leurs capacités.
    - **Authentification** : Vérifie les permissions pour l'accès aux outils.
    - **Gestionnaire de requêtes** : Traite les demandes d'outils provenant du modèle.
    - **Formateur de réponses** : Structure les sorties des outils dans un format compréhensible par le modèle.
- **Exécution du serveur MCP** :
    - L'**hôte MCP** dirige les appels d'outils vers un ou plusieurs **serveurs MCP**, chacun exposant des fonctions spécialisées (par exemple, recherche, calculs, requêtes de base de données).
    - Les **serveurs MCP** exécutent leurs opérations respectives et renvoient les résultats à l'**hôte MCP** dans un format cohérent.
    - L'**hôte MCP** formate et transmet ces résultats au **modèle d'IA**.
- **Finalisation de la réponse** :
    - Le **modèle d'IA** intègre les sorties des outils dans une réponse finale.
    - L'**hôte MCP** envoie cette réponse au **client MCP**, qui la transmet à l'utilisateur final ou au logiciel appelant.

```mermaid
---
title: MCP Architecture and Component Interactions
description: A diagram showing the flows of the components in MCP.
---
graph TD
    Client[MCP Client/Application] -->|Sends Request| H[MCP Host]
    H -->|Invokes| A[AI Model]
    A -->|Tool Call Request| H
    H -->|MCP Protocol| T1[MCP Server Tool 01: Web Search]
    H -->|MCP Protocol| T2[MCP Server Tool 02: Calculator tool]
    H -->|MCP Protocol| T3[MCP Server Tool 03: Database Access tool]
    H -->|MCP Protocol| T4[MCP Server Tool 04: File System tool]
    H -->|Sends Response| Client

    subgraph "MCP Host Components"
        H
        G[Tool Registry]
        I[Authentication]
        J[Request Handler]
        K[Response Formatter]
    end

    H <--> G
    H <--> I
    H <--> J
    H <--> K

    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style H fill:#eeeeee,stroke:#333,stroke-width:2px
    style Client fill:#d5e8f9,stroke:#333,stroke-width:2px
    style G fill:#fffbe6,stroke:#333,stroke-width:1px
    style I fill:#fffbe6,stroke:#333,stroke-width:1px
    style J fill:#fffbe6,stroke:#333,stroke-width:1px
    style K fill:#fffbe6,stroke:#333,stroke-width:1px
    style T1 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T2 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T3 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T4 fill:#c2f0c2,stroke:#333,stroke-width:1px
```

## 👨‍💻 Comment créer un serveur MCP (avec exemples)

Les serveurs MCP permettent d'étendre les capacités des LLMs en fournissant des données et des fonctionnalités.

Prêt à essayer ? Voici des SDK spécifiques à des langages et/ou stacks avec des exemples de création de serveurs MCP simples dans différents langages/stacks :

- **SDK Python** : https://github.com/modelcontextprotocol/python-sdk

- **SDK TypeScript** : https://github.com/modelcontextprotocol/typescript-sdk

- **SDK Java** : https://github.com/modelcontextprotocol/java-sdk

- **SDK C#/.NET** : https://github.com/modelcontextprotocol/csharp-sdk

## 🌍 Cas d'utilisation concrets du MCP

Le MCP permet une large gamme d'applications en étendant les capacités de l'IA :

| **Application**              | **Description**                                                                |
|------------------------------|--------------------------------------------------------------------------------|
| Intégration de données d'entreprise | Connecter les LLMs à des bases de données, CRM ou outils internes              |
| Systèmes d'IA agentiques     | Permettre à des agents autonomes d'accéder à des outils et de suivre des flux de décision |
| Applications multimodales    | Combiner des outils texte, image et audio dans une seule application IA unifiée |
| Intégration de données en temps réel | Apporter des données en direct dans les interactions IA pour des résultats plus précis et actuels |

### 🧠 MCP = Norme universelle pour les interactions IA

Le protocole de contexte de modèle (MCP) agit comme une norme universelle pour les interactions IA, tout comme l'USB-C a standardisé les connexions physiques pour les appareils. Dans le monde de l'IA, le MCP fournit une interface cohérente, permettant aux modèles (clients) de s'intégrer facilement avec des outils externes et des fournisseurs de données (serveurs). Cela élimine le besoin de protocoles divers et personnalisés pour chaque API ou source de données.

Avec le MCP, un outil compatible MCP (appelé serveur MCP) suit une norme unifiée. Ces serveurs peuvent répertorier les outils ou actions qu'ils offrent et exécuter ces actions lorsqu'ils sont sollicités par un agent IA. Les plateformes d'agents IA qui prennent en charge le MCP sont capables de découvrir les outils disponibles sur les serveurs et de les invoquer via ce protocole standard.

### 💡 Facilite l'accès au savoir

Au-delà de la fourniture d'outils, le MCP facilite également l'accès au savoir. Il permet aux applications de fournir un contexte aux modèles de langage étendu (LLMs) en les reliant à diverses sources de données. Par exemple, un serveur MCP pourrait représenter un dépôt de documents d'entreprise, permettant aux agents de récupérer des informations pertinentes à la demande. Un autre serveur pourrait gérer des actions spécifiques comme l'envoi d'e-mails ou la mise à jour de dossiers. Du point de vue de l'agent, ce sont simplement des outils qu'il peut utiliser—certains outils renvoient des données (contexte de savoir), tandis que d'autres exécutent des actions. Le MCP gère efficacement les deux.

Un agent se connectant à un serveur MCP apprend automatiquement les capacités disponibles et les données accessibles du serveur via un format standard. Cette standardisation permet une disponibilité dynamique des outils. Par exemple, ajouter un nouveau serveur MCP au système d'un agent rend ses fonctions immédiatement utilisables sans nécessiter de personnalisation supplémentaire des instructions de l'agent.

Cette intégration simplifiée s'aligne avec le flux représenté dans le diagramme suivant, où les serveurs fournissent à la fois des outils et des connaissances, assurant une collaboration fluide entre les systèmes.

### 👉 Exemple : Solution d'agent évolutive

```mermaid
---
title: Scalable Agent Solution with MCP
description: A diagram illustrating how a user interacts with an LLM that connects to multiple MCP servers, with each server providing both knowledge and tools, creating a scalable AI system architecture
---
graph TD
    User -->|Prompt| LLM
    LLM -->|Response| User
    LLM -->|MCP| ServerA
    LLM -->|MCP| ServerB
    ServerA -->|Universal connector| ServerB
    ServerA --> KnowledgeA
    ServerA --> ToolsA
    ServerB --> KnowledgeB
    ServerB --> ToolsB

    subgraph Server A
        KnowledgeA[Knowledge]
        ToolsA[Tools]
    end

    subgraph Server B
        KnowledgeB[Knowledge]
        ToolsB[Tools]
    end
```
Le connecteur universel permet aux serveurs MCP de communiquer et de partager leurs capacités entre eux, permettant au ServeurA de déléguer des tâches au ServeurB ou d'accéder à ses outils et connaissances. Cela fédère les outils et les données entre les serveurs, soutenant des architectures d'agents évolutives et modulaires. Parce que le MCP standardise l'exposition des outils, les agents peuvent découvrir dynamiquement et router les requêtes entre les serveurs sans intégrations codées en dur.

Fédération des outils et des connaissances : Les outils et les données peuvent être accessibles entre les serveurs, permettant des architectures agentiques plus évolutives et modulaires.

### 🔄 Scénarios avancés MCP avec intégration LLM côté client

Au-delà de l'architecture MCP de base, il existe des scénarios avancés où le client et le serveur contiennent des LLMs, permettant des interactions plus sophistiquées. Dans le diagramme suivant, **Client App** pourrait être un IDE avec un certain nombre d'outils MCP disponibles pour l'utilisateur via le LLM :

```mermaid
---
title: Advanced MCP Scenarios with Client-Server LLM Integration
description: A sequence diagram showing the detailed interaction flow between user, client application, client LLM, multiple MCP servers, and server LLM, illustrating tool discovery, user interaction, direct tool calling, and feature negotiation phases
---
sequenceDiagram
    autonumber
    actor User as 👤 User
    participant ClientApp as 🖥️ Client App
    participant ClientLLM as 🧠 Client LLM
    participant Server1 as 🔧 MCP Server 1
    participant Server2 as 📚 MCP Server 2
    participant ServerLLM as 🤖 Server LLM
    
    %% Discovery Phase
    rect rgb(220, 240, 255)
        Note over ClientApp, Server2: TOOL DISCOVERY PHASE
        ClientApp->>+Server1: Request available tools/resources
        Server1-->>-ClientApp: Return tool list (JSON)
        ClientApp->>+Server2: Request available tools/resources
        Server2-->>-ClientApp: Return tool list (JSON)
        Note right of ClientApp: Store combined tool<br/>catalog locally
    end
    
    %% User Interaction
    rect rgb(255, 240, 220)
        Note over User, ClientLLM: USER INTERACTION PHASE
        User->>+ClientApp: Enter natural language prompt
        ClientApp->>+ClientLLM: Forward prompt + tool catalog
        ClientLLM->>-ClientLLM: Analyze prompt & select tools
    end
    
    %% Scenario A: Direct Tool Calling
    alt Direct Tool Calling
        rect rgb(220, 255, 220)
            Note over ClientApp, Server1: SCENARIO A: DIRECT TOOL CALLING
            ClientLLM->>+ClientApp: Request tool execution
            ClientApp->>+Server1: Execute specific tool
            Server1-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    
    %% Scenario B: Feature Negotiation (VS Code style)
    else Feature Negotiation (VS Code style)
        rect rgb(255, 220, 220)
            Note over ClientApp, ServerLLM: SCENARIO B: FEATURE NEGOTIATION
            ClientLLM->>+ClientApp: Identify needed capabilities
            ClientApp->>+Server2: Negotiate features/capabilities
            Server2->>+ServerLLM: Request additional context
            ServerLLM-->>-Server2: Provide context
            Server2-->>-ClientApp: Return available features
            ClientApp->>+Server2: Call negotiated tools
            Server2-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    end
```

## 🔐 Avantages pratiques du MCP

Voici les avantages pratiques de l'utilisation du MCP :

- **Actualité** : Les modèles peuvent accéder à des informations à jour au-delà de leurs données d'entraînement
- **Extension des capacités** : Les modèles peuvent utiliser des outils spécialisés pour des tâches pour lesquelles ils n'ont pas été entraînés
- **Réduction des hallucinations** : Les sources de données externes fournissent un ancrage factuel
- **Confidentialité** : Les données sensibles peuvent rester dans des environnements sécurisés au lieu d'être intégrées dans les invites

## 📌 Points clés à retenir

Les points clés suivants résument l'utilisation du MCP :

- Le **MCP** standardise la manière dont les modèles d'IA interagissent avec les outils et les données
- Favorise **l'extensibilité, la cohérence et l'interopérabilité**
- Le MCP aide à **réduire le temps de développement, améliorer la fiabilité et étendre les capacités des modèles**
- L'architecture client-serveur **permet des applications IA flexibles et extensibles**

## 🧠 Exercice

Réfléchissez à une application IA que vous souhaitez créer.

- Quels **outils ou données externes** pourraient améliorer ses capacités ?
- Comment le MCP pourrait-il rendre l'intégration **plus simple et fiable** ?

## Ressources supplémentaires

- [Répertoire GitHub MCP](https://github.com/modelcontextprotocol)

## Et après

Prochain chapitre : [Chapitre 1 : Concepts de base](../01-CoreConcepts/README.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.