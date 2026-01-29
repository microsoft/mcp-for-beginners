# Consommer un serveur avec l'extension AI Toolkit pour Visual Studio Code

Lorsque vous construisez un agent d'IA, il ne s'agit pas seulement de générer des réponses intelligentes ; il s'agit également de donner à votre agent la capacité d'agir. C'est là que le protocole Model Context Protocol (MCP) entre en jeu. MCP permet aux agents d'accéder facilement à des outils et services externes de manière cohérente. Imaginez que vous connectez votre agent à une boîte à outils qu'il peut *vraiment* utiliser.

Supposons que vous connectiez un agent à votre serveur MCP de calculatrice. Tout à coup, votre agent peut effectuer des opérations mathématiques simplement en recevant une instruction comme « Combien font 47 fois 89 ? »—pas besoin de coder des logiques complexes ou de créer des API personnalisées.

## Vue d'ensemble

Cette leçon explique comment connecter un serveur MCP de calculatrice à un agent avec l'extension [AI Toolkit](https://aka.ms/AIToolkit) dans Visual Studio Code, permettant à votre agent d'effectuer des opérations mathématiques telles que l'addition, la soustraction, la multiplication et la division via un langage naturel.

AI Toolkit est une extension puissante pour Visual Studio Code qui simplifie le développement d'agents. Les ingénieurs en IA peuvent facilement créer des applications d'IA en développant et testant des modèles génératifs—localement ou dans le cloud. L'extension prend en charge la plupart des modèles génératifs majeurs disponibles aujourd'hui.

*Note*: AI Toolkit prend actuellement en charge Python et TypeScript.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Consommer un serveur MCP via AI Toolkit.
- Configurer un agent pour lui permettre de découvrir et d'utiliser les outils fournis par le serveur MCP.
- Utiliser les outils MCP via un langage naturel.

## Approche

Voici comment nous allons procéder à un niveau général :

- Créer un agent et définir son prompt système.
- Créer un serveur MCP avec des outils de calculatrice.
- Connecter le générateur d'agents au serveur MCP.
- Tester l'invocation des outils de l'agent via un langage naturel.

Parfait, maintenant que nous comprenons le processus, configurons un agent d'IA pour exploiter des outils externes via MCP, augmentant ainsi ses capacités !

## Prérequis

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pour Visual Studio Code](https://aka.ms/AIToolkit)

## Exercice : Consommer un serveur

> [!WARNING]
> Note pour les utilisateurs de macOS. Nous enquêtons actuellement sur un problème affectant l'installation des dépendances sur macOS. En conséquence, les utilisateurs de macOS ne pourront pas compléter ce tutoriel pour le moment. Nous mettrons à jour les instructions dès qu'une solution sera disponible. Merci pour votre patience et votre compréhension !

Dans cet exercice, vous allez construire, exécuter et améliorer un agent d'IA avec des outils provenant d'un serveur MCP dans Visual Studio Code en utilisant AI Toolkit.

### -0- Étape préliminaire, ajouter le modèle OpenAI GPT-4o à Mes Modèles

L'exercice utilise le modèle **GPT-4o**. Le modèle doit être ajouté à **Mes Modèles** avant de créer l'agent.

1. Ouvrez l'extension **AI Toolkit** depuis la **Barre d'activité**.
1. Dans la section **Catalogue**, sélectionnez **Modèles** pour ouvrir le **Catalogue de modèles**. Sélectionner **Modèles** ouvre le **Catalogue de modèles** dans un nouvel onglet de l'éditeur.
1. Dans la barre de recherche du **Catalogue de modèles**, entrez **OpenAI GPT-4o**.
1. Cliquez sur **+ Ajouter** pour ajouter le modèle à votre liste **Mes Modèles**. Assurez-vous d'avoir sélectionné le modèle **Hébergé par GitHub**.
1. Dans la **Barre d'activité**, confirmez que le modèle **OpenAI GPT-4o** apparaît dans la liste.

### -1- Créer un agent

Le **Générateur d'agents (Prompt)** vous permet de créer et personnaliser vos propres agents alimentés par l'IA. Dans cette section, vous allez créer un nouvel agent et lui attribuer un modèle pour alimenter la conversation.

1. Ouvrez l'extension **AI Toolkit** depuis la **Barre d'activité**.
1. Dans la section **Outils**, sélectionnez **Générateur d'agents (Prompt)**. Sélectionner **Générateur d'agents (Prompt)** ouvre le **Générateur d'agents (Prompt)** dans un nouvel onglet de l'éditeur.
1. Cliquez sur le bouton **+ Nouvel Agent**. L'extension lancera un assistant de configuration via la **Palette de commandes**.
1. Entrez le nom **Agent Calculatrice** et appuyez sur **Entrée**.
1. Dans le **Générateur d'agents (Prompt)**, pour le champ **Modèle**, sélectionnez le modèle **OpenAI GPT-4o (via GitHub)**.

### -2- Créer un prompt système pour l'agent

Avec l'agent configuré, il est temps de définir sa personnalité et son objectif. Dans cette section, vous utiliserez la fonctionnalité **Générer un prompt système** pour décrire le comportement attendu de l'agent—dans ce cas, un agent calculatrice—et demander au modèle de rédiger le prompt système pour vous.

1. Pour la section **Prompts**, cliquez sur le bouton **Générer un prompt système**. Ce bouton ouvre le générateur de prompts qui utilise l'IA pour générer un prompt système pour l'agent.
1. Dans la fenêtre **Générer un prompt**, entrez le texte suivant : `Vous êtes un assistant mathématique utile et efficace. Lorsqu'on vous donne un problème impliquant des calculs arithmétiques de base, vous répondez avec le résultat correct.`
1. Cliquez sur le bouton **Générer**. Une notification apparaîtra dans le coin inférieur droit confirmant que le prompt système est en cours de génération. Une fois la génération terminée, le prompt apparaîtra dans le champ **Prompt système** du **Générateur d'agents (Prompt)**.
1. Examinez le **Prompt système** et modifiez-le si nécessaire.

### -3- Créer un serveur MCP

Maintenant que vous avez défini le prompt système de votre agent—guidant son comportement et ses réponses—il est temps de doter l'agent de capacités pratiques. Dans cette section, vous allez créer un serveur MCP de calculatrice avec des outils pour effectuer des calculs d'addition, de soustraction, de multiplication et de division. Ce serveur permettra à votre agent d'effectuer des opérations mathématiques en temps réel en réponse à des instructions en langage naturel.

AI Toolkit est équipé de modèles pour faciliter la création de votre propre serveur MCP. Nous utiliserons le modèle Python pour créer le serveur MCP de calculatrice.

*Note*: AI Toolkit prend actuellement en charge Python et TypeScript.

1. Dans la section **Outils** du **Générateur d'agents (Prompt)**, cliquez sur le bouton **+ Serveur MCP**. L'extension lancera un assistant de configuration via la **Palette de commandes**.
1. Sélectionnez **+ Ajouter un serveur**.
1. Sélectionnez **Créer un nouveau serveur MCP**.
1. Sélectionnez **python-weather** comme modèle.
1. Sélectionnez **Dossier par défaut** pour enregistrer le modèle de serveur MCP.
1. Entrez le nom suivant pour le serveur : **Calculatrice**
1. Une nouvelle fenêtre Visual Studio Code s'ouvrira. Sélectionnez **Oui, je fais confiance aux auteurs**.
1. Utilisez le terminal (**Terminal** > **Nouveau terminal**) pour créer un environnement virtuel : `python -m venv .venv`
1. Utilisez le terminal pour activer l'environnement virtuel :
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Utilisez le terminal pour installer les dépendances : `pip install -e .[dev]`
1. Dans la vue **Explorateur** de la **Barre d'activité**, développez le répertoire **src** et sélectionnez **server.py** pour ouvrir le fichier dans l'éditeur.
1. Remplacez le code dans le fichier **server.py** par le suivant et enregistrez :

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Exécuter l'agent avec le serveur MCP de calculatrice

Maintenant que votre agent dispose d'outils, il est temps de les utiliser ! Dans cette section, vous soumettrez des instructions à l'agent pour tester et valider si l'agent utilise l'outil approprié du serveur MCP de calculatrice.

Vous exécuterez le serveur MCP de calculatrice sur votre machine de développement locale via le **Générateur d'agents** en tant que client MCP.

1. Appuyez sur `F5` pour démarrer le débogage du serveur MCP. Le **Générateur d'agents (Prompt)** s'ouvrira dans un nouvel onglet de l'éditeur. Le statut du serveur est visible dans le terminal.
1. Dans le champ **Prompt utilisateur** du **Générateur d'agents (Prompt)**, entrez l'instruction suivante : `J'ai acheté 3 articles à 25 $ chacun, puis utilisé une réduction de 20 $. Combien ai-je payé ?`
1. Cliquez sur le bouton **Exécuter** pour générer la réponse de l'agent.
1. Examinez la sortie de l'agent. Le modèle devrait conclure que vous avez payé **55 $**.
1. Voici un résumé de ce qui devrait se produire :
    - L'agent sélectionne les outils **multiply** et **subtract** pour effectuer le calcul.
    - Les valeurs respectives `a` et `b` sont attribuées pour l'outil **multiply**.
    - Les valeurs respectives `a` et `b` sont attribuées pour l'outil **subtract**.
    - La réponse de chaque outil est fournie dans la section **Réponse de l'outil**.
    - La sortie finale du modèle est fournie dans la section **Réponse du modèle**.
1. Soumettez des instructions supplémentaires pour tester davantage l'agent. Vous pouvez modifier l'instruction existante dans le champ **Prompt utilisateur** en cliquant dans le champ et en remplaçant l'instruction existante.
1. Une fois que vous avez terminé de tester l'agent, vous pouvez arrêter le serveur via le **terminal** en entrant **CTRL/CMD+C** pour quitter.

## Devoir

Essayez d'ajouter une entrée d'outil supplémentaire à votre fichier **server.py** (ex : retourner la racine carrée d'un nombre). Soumettez des instructions supplémentaires qui nécessiteraient que l'agent utilise votre nouvel outil (ou les outils existants). Assurez-vous de redémarrer le serveur pour charger les nouveaux outils ajoutés.

## Solution

[Solution](./solution/README.md)

## Points clés à retenir

Les points clés de ce chapitre sont les suivants :

- L'extension AI Toolkit est un excellent client qui permet de consommer des serveurs MCP et leurs outils.
- Vous pouvez ajouter de nouveaux outils aux serveurs MCP, augmentant les capacités de l'agent pour répondre à des besoins évolutifs.
- AI Toolkit inclut des modèles (par exemple, des modèles de serveurs MCP Python) pour simplifier la création d'outils personnalisés.

## Ressources supplémentaires

- [Documentation AI Toolkit](https://aka.ms/AIToolkit/doc)

## Et après
- Suivant : [Tests et débogage](../08-testing/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.