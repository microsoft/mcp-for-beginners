<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-07-31T01:14:53+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "fr"
}
-->
# Consommer un serveur avec l'extension AI Toolkit pour Visual Studio Code

Lorsque vous construisez un agent d'IA, il ne s'agit pas seulement de générer des réponses intelligentes ; il s'agit aussi de donner à votre agent la capacité d'agir. C'est là qu'intervient le protocole Model Context Protocol (MCP). MCP permet aux agents d'accéder facilement à des outils et services externes de manière cohérente. Pensez-y comme à une boîte à outils dans laquelle votre agent peut *réellement* puiser.

Imaginons que vous connectiez un agent à votre serveur MCP de calculatrice. Soudainement, votre agent peut effectuer des opérations mathématiques simplement en recevant une instruction comme « Combien font 47 fois 89 ? »—pas besoin de coder la logique en dur ou de créer des API personnalisées.

## Vue d’ensemble

Cette leçon explique comment connecter un serveur MCP de calculatrice à un agent à l'aide de l'extension [AI Toolkit](https://aka.ms/AIToolkit) dans Visual Studio Code, permettant ainsi à votre agent d'effectuer des opérations mathématiques telles que l'addition, la soustraction, la multiplication et la division via un langage naturel.

AI Toolkit est une extension puissante pour Visual Studio Code qui simplifie le développement d'agents. Les ingénieurs en IA peuvent facilement créer des applications d'IA en développant et testant des modèles génératifs—localement ou dans le cloud. L'extension prend en charge la plupart des principaux modèles génératifs disponibles aujourd'hui.

*Remarque* : L'AI Toolkit prend actuellement en charge Python et TypeScript.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- Consommer un serveur MCP via l'AI Toolkit.
- Configurer un agent pour lui permettre de découvrir et d'utiliser les outils fournis par le serveur MCP.
- Utiliser les outils MCP via un langage naturel.

## Approche

Voici les étapes générales que nous allons suivre :

- Créer un agent et définir son invite système.
- Créer un serveur MCP avec des outils de calculatrice.
- Connecter l'Agent Builder au serveur MCP.
- Tester l'invocation des outils de l'agent via un langage naturel.

Parfait, maintenant que nous comprenons le processus, configurons un agent d'IA pour exploiter des outils externes via MCP, augmentant ainsi ses capacités !

## Prérequis

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pour Visual Studio Code](https://aka.ms/AIToolkit)

## Exercice : Consommer un serveur

> [!WARNING]
> Remarque pour les utilisateurs de macOS. Nous enquêtons actuellement sur un problème affectant l'installation des dépendances sur macOS. Par conséquent, les utilisateurs de macOS ne pourront pas suivre ce tutoriel pour le moment. Nous mettrons à jour les instructions dès qu'une solution sera disponible. Merci pour votre patience et votre compréhension !

Dans cet exercice, vous allez construire, exécuter et améliorer un agent d'IA avec des outils provenant d'un serveur MCP dans Visual Studio Code à l'aide de l'AI Toolkit.

### -0- Étape préliminaire, ajouter le modèle OpenAI GPT-4o à Mes Modèles

L'exercice utilise le modèle **GPT-4o**. Ce modèle doit être ajouté à **Mes Modèles** avant de créer l'agent.

![Capture d’écran d’une interface de sélection de modèles dans l’extension AI Toolkit de Visual Studio Code. Le titre indique "Trouvez le bon modèle pour votre solution d'IA" avec un sous-titre encourageant les utilisateurs à découvrir, tester et déployer des modèles d'IA. En dessous, sous "Modèles populaires," six cartes de modèles sont affichées : DeepSeek-R1 (hébergé sur GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Petit, Rapide), et DeepSeek-R1 (hébergé sur Ollama). Chaque carte inclut des options pour "Ajouter" le modèle ou "Essayer dans le Playground."](../../../../translated_images/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.fr.png)

1. Ouvrez l'extension **AI Toolkit** depuis la **Barre d'activité**.
1. Dans la section **Catalogue**, sélectionnez **Modèles** pour ouvrir le **Catalogue de modèles**. En sélectionnant **Modèles**, le **Catalogue de modèles** s'ouvre dans un nouvel onglet de l'éditeur.
1. Dans la barre de recherche du **Catalogue de modèles**, entrez **OpenAI GPT-4o**.
1. Cliquez sur **+ Ajouter** pour ajouter le modèle à votre liste **Mes Modèles**. Assurez-vous d'avoir sélectionné le modèle **Hébergé par GitHub**.
1. Dans la **Barre d'activité**, confirmez que le modèle **OpenAI GPT-4o** apparaît dans la liste.

### -1- Créer un agent

L'outil **Agent (Prompt) Builder** vous permet de créer et personnaliser vos propres agents alimentés par l'IA. Dans cette section, vous allez créer un nouvel agent et lui attribuer un modèle pour alimenter la conversation.

![Capture d’écran de l’interface du "Calculator Agent" dans l’extension AI Toolkit pour Visual Studio Code. Dans le panneau de gauche, le modèle sélectionné est "OpenAI GPT-4o (via GitHub)." Une invite système indique "Vous êtes un professeur d'université enseignant les mathématiques," et l'invite utilisateur dit, "Expliquez-moi l'équation de Fourier en termes simples." Des options supplémentaires incluent des boutons pour ajouter des outils, activer le serveur MCP et sélectionner une sortie structurée. Un bouton bleu "Exécuter" est en bas. Dans le panneau de droite, sous "Commencez avec des exemples," trois agents exemples sont listés : Développeur Web (avec serveur MCP), Simplificateur pour élèves de CE1, et Interprète de rêves, chacun avec une brève description de leurs fonctions.](../../../../translated_images/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.fr.png)

1. Ouvrez l'extension **AI Toolkit** depuis la **Barre d'activité**.
1. Dans la section **Outils**, sélectionnez **Agent (Prompt) Builder**. En sélectionnant **Agent (Prompt) Builder**, l'outil s'ouvre dans un nouvel onglet de l'éditeur.
1. Cliquez sur le bouton **+ Nouvel Agent**. L'extension lancera un assistant de configuration via la **Palette de commandes**.
1. Entrez le nom **Calculator Agent** et appuyez sur **Entrée**.
1. Dans l'outil **Agent (Prompt) Builder**, pour le champ **Modèle**, sélectionnez le modèle **OpenAI GPT-4o (via GitHub)**.

### -2- Créer une invite système pour l'agent

Avec l'agent configuré, il est temps de définir sa personnalité et son objectif. Dans cette section, vous utiliserez la fonctionnalité **Générer une invite système** pour décrire le comportement attendu de l'agent—dans ce cas, un agent calculatrice—et demander au modèle de rédiger l'invite système pour vous.

![Capture d’écran de l’interface "Calculator Agent" dans l’AI Toolkit pour Visual Studio Code avec une fenêtre modale ouverte intitulée "Générer une invite." La modale explique qu’un modèle d’invite peut être généré en partageant des détails de base et inclut une zone de texte avec l’exemple d’invite système : "Vous êtes un assistant mathématique utile et efficace. Lorsqu’un problème impliquant des calculs arithmétiques de base vous est soumis, vous répondez avec le résultat correct." En dessous de la zone de texte se trouvent des boutons "Fermer" et "Générer." En arrière-plan, une partie de la configuration de l’agent est visible, y compris le modèle sélectionné "OpenAI GPT-4o (via GitHub)" et des champs pour les invites système et utilisateur.](../../../../translated_images/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.fr.png)

1. Dans la section **Invites**, cliquez sur le bouton **Générer une invite système**. Ce bouton ouvre l'outil de génération d'invite qui utilise l'IA pour créer une invite système pour l'agent.
1. Dans la fenêtre **Générer une invite**, entrez le texte suivant : `Vous êtes un assistant mathématique utile et efficace. Lorsqu’un problème impliquant des calculs arithmétiques de base vous est soumis, vous répondez avec le résultat correct.`
1. Cliquez sur le bouton **Générer**. Une notification apparaîtra dans le coin inférieur droit confirmant que l'invite système est en cours de génération. Une fois la génération terminée, l'invite apparaîtra dans le champ **Invite système** de l'outil **Agent (Prompt) Builder**.
1. Passez en revue l'**Invite système** et modifiez-la si nécessaire.

### -3- Créer un serveur MCP

Maintenant que vous avez défini l'invite système de votre agent—guidant son comportement et ses réponses—il est temps de doter l'agent de capacités pratiques. Dans cette section, vous allez créer un serveur MCP de calculatrice avec des outils pour effectuer des calculs d'addition, de soustraction, de multiplication et de division. Ce serveur permettra à votre agent d'effectuer des opérations mathématiques en temps réel en réponse à des instructions en langage naturel.

!["Capture d’écran de la section inférieure de l’interface Calculator Agent dans l’extension AI Toolkit pour Visual Studio Code. Elle montre des menus extensibles pour "Outils" et "Sortie structurée," ainsi qu’un menu déroulant intitulé "Choisir le format de sortie" réglé sur "texte." À droite, un bouton intitulé "+ Serveur MCP" permet d’ajouter un serveur Model Context Protocol. Une icône d’image est affichée au-dessus de la section Outils.](../../../../translated_images/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.fr.png)

AI Toolkit est équipé de modèles pour faciliter la création de votre propre serveur MCP. Nous utiliserons le modèle Python pour créer le serveur MCP de calculatrice.

*Remarque* : L'AI Toolkit prend actuellement en charge Python et TypeScript.

1. Dans la section **Outils** de l'outil **Agent (Prompt) Builder**, cliquez sur le bouton **+ Serveur MCP**. L'extension lancera un assistant de configuration via la **Palette de commandes**.
1. Sélectionnez **+ Ajouter un serveur**.
1. Sélectionnez **Créer un nouveau serveur MCP**.
1. Sélectionnez **python-weather** comme modèle.
1. Sélectionnez **Dossier par défaut** pour enregistrer le modèle de serveur MCP.
1. Entrez le nom suivant pour le serveur : **Calculator**
1. Une nouvelle fenêtre Visual Studio Code s'ouvrira. Sélectionnez **Oui, je fais confiance aux auteurs**.
1. À l'aide du terminal (**Terminal** > **Nouveau terminal**), créez un environnement virtuel : `python -m venv .venv`
1. À l'aide du terminal, activez l'environnement virtuel :
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source venv/bin/activate`
1. À l'aide du terminal, installez les dépendances : `pip install -e .[dev]`
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

Maintenant que votre agent dispose d'outils, il est temps de les utiliser ! Dans cette section, vous soumettrez des instructions à l'agent pour tester et valider si l'agent utilise l'outil approprié du serveur MCP de calculatrice.

![Capture d’écran de l’interface Calculator Agent dans l’extension AI Toolkit pour Visual Studio Code. Dans le panneau de gauche, sous "Outils," un serveur MCP nommé local-server-calculator_server est ajouté, montrant quatre outils disponibles : add, subtract, multiply, et divide. Un badge indique que quatre outils sont actifs. En dessous se trouve une section "Sortie structurée" repliée et un bouton bleu "Exécuter." Dans le panneau de droite, sous "Réponse du modèle," l’agent invoque les outils multiply et subtract avec les entrées {"a": 3, "b": 25} et {"a": 75, "b": 20} respectivement. La "Réponse de l’outil" finale est affichée comme 75.0. Un bouton "Voir le code" apparaît en bas.](../../../../translated_images/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.fr.png)

Vous exécuterez le serveur MCP de calculatrice sur votre machine de développement locale via l'**Agent Builder** en tant que client MCP.

1. Appuyez sur `F5` pour démarrer le débogage du serveur MCP. L'outil **Agent (Prompt) Builder** s'ouvrira dans un nouvel onglet de l'éditeur. Le statut du serveur est visible dans le terminal.
1. Dans le champ **Invite utilisateur** de l'outil **Agent (Prompt) Builder**, entrez l'instruction suivante : `J'ai acheté 3 articles à 25 $ chacun, puis utilisé une remise de 20 $. Combien ai-je payé ?`
1. Cliquez sur le bouton **Exécuter** pour générer la réponse de l'agent.
1. Passez en revue la sortie de l'agent. Le modèle devrait conclure que vous avez payé **55 $**.
1. Voici un résumé de ce qui devrait se produire :
    - L'agent sélectionne les outils **multiply** et **subtract** pour effectuer le calcul.
    - Les valeurs respectives `a` et `b` sont attribuées pour l'outil **multiply**.
    - Les valeurs respectives `a` et `b` sont attribuées pour l'outil **subtract**.
    - La réponse de chaque outil est fournie dans la section **Réponse de l’outil**.
    - La sortie finale du modèle est fournie dans la section **Réponse du modèle**.
1. Soumettez des instructions supplémentaires pour tester davantage l'agent. Vous pouvez modifier l'instruction existante dans le champ **Invite utilisateur** en cliquant dans le champ et en remplaçant l'instruction existante.
1. Une fois vos tests terminés, vous pouvez arrêter le serveur via le **terminal** en entrant **CTRL/CMD+C** pour quitter.

## Devoir

Essayez d'ajouter une nouvelle entrée d'outil à votre fichier **server.py** (par exemple : retourner la racine carrée d'un nombre). Soumettez des instructions supplémentaires qui nécessiteraient que l'agent utilise votre nouvel outil (ou des outils existants). Assurez-vous de redémarrer le serveur pour charger les nouveaux outils ajoutés.

## Solution

[Solution](./solution/README.md)

## Points clés à retenir

Les points clés de ce chapitre sont les suivants :

- L'extension AI Toolkit est un excellent client qui permet de consommer des serveurs MCP et leurs outils.
- Vous pouvez ajouter de nouveaux outils aux serveurs MCP, élargissant ainsi les capacités de l'agent pour répondre à des besoins évolutifs.
- L'AI Toolkit inclut des modèles (par exemple, des modèles de serveurs MCP en Python) pour simplifier la création d'outils personnalisés.

## Ressources supplémentaires

- [Documentation AI Toolkit](https://aka.ms/AIToolkit/doc)

## Prochaine étape
- Suivant : [Tests et débogage](../08-testing/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.