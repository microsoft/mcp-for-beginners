# Consommer un serveur depuis l’extension AI Toolkit pour Visual Studio Code

Lorsque vous créez un agent IA, il ne s'agit pas seulement de générer des réponses intelligentes ; il s'agit également de donner à votre agent la capacité d'agir. C’est là qu’intervient le Model Context Protocol (MCP). MCP facilite l'accès des agents à des outils et services externes de manière cohérente. Pensez-y comme si vous branchiez votre agent à une boîte à outils qu'il peut *vraiment* utiliser.

Disons que vous connectez un agent à votre serveur MCP de calculatrice. Soudain, votre agent peut effectuer des opérations mathématiques simplement en recevant une invite comme « Quel est le résultat de 47 fois 89 ? »—pas besoin de coder la logique ou de construire des API personnalisées.

## Vue d'ensemble

Cette leçon explique comment connecter un serveur MCP de calculatrice à un agent avec l'extension [AI Toolkit](https://aka.ms/AIToolkit) dans Visual Studio Code, permettant à votre agent d’exécuter des opérations mathématiques telles que l’addition, la soustraction, la multiplication et la division à travers le langage naturel.

AI Toolkit est une extension puissante pour Visual Studio Code qui simplifie le développement d’agents. Les ingénieurs IA peuvent facilement concevoir des applications IA en développant et testant des modèles génératifs d’IA—localement ou dans le cloud. L'extension supporte la plupart des modèles génératifs majeurs disponibles aujourd’hui.

*Note* : AI Toolkit supporte actuellement Python et TypeScript.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- Consommer un serveur MCP via AI Toolkit.
- Configurer un agent pour lui permettre de découvrir et d’utiliser les outils fournis par le serveur MCP.
- Utiliser les outils MCP via le langage naturel.

## Approche

Voici comment nous allons procéder à un haut niveau :

- Créer un agent et définir son prompt système.
- Créer un serveur MCP avec des outils de calculatrice.
- Connecter l’Agent Builder au serveur MCP.
- Tester l’invocation des outils par l’agent via le langage naturel.

Parfait, maintenant que nous comprenons le déroulement, configurons un agent IA pour exploiter des outils externes via MCP, ce qui améliorera ses capacités !

## Prérequis

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pour Visual Studio Code](https://aka.ms/AIToolkit)

## Exercice : Consommer un serveur

> [!WARNING]
> Note pour les utilisateurs macOS. Nous enquêtons actuellement sur un problème affectant l’installation des dépendances sur macOS. En conséquence, les utilisateurs macOS ne pourront pas compléter ce tutoriel pour le moment. Nous mettrons à jour les instructions dès qu'une solution sera disponible. Merci pour votre patience et votre compréhension !

Dans cet exercice, vous allez construire, exécuter et améliorer un agent IA avec des outils d’un serveur MCP à l’intérieur de Visual Studio Code, en utilisant AI Toolkit.

### -0- Étape préalable, ajouter le modèle OpenAI GPT-4o à Mes Modèles

L’exercice utilise le modèle **GPT-4o**. Le modèle doit être ajouté à **Mes Modèles** avant de créer l’agent.

![Capture d'écran d’une interface de sélection de modèle dans l'extension AI Toolkit de Visual Studio Code. Le titre indique « Trouvez le bon modèle pour votre solution IA » avec un sous-titre encourageant à découvrir, tester et déployer des modèles IA. En dessous, sous « Modèles populaires », six cartes de modèles sont affichées : DeepSeek-R1 (hébergé par GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Petit, Rapide), et DeepSeek-R1 (hébergé par Ollama). Chaque carte inclut des options pour « Ajouter » le modèle ou « Essayer dans le Playground ».](../../../../translated_images/fr/aitk-model-catalog.2acd38953bb9c119.webp)

1. Ouvrez l’extension **AI Toolkit** depuis la **Barre d’activités**.
1. Dans la section **Catalogue**, sélectionnez **Modèles** pour ouvrir le **Catalogue de Modèles**. Sélectionner **Modèles** ouvre le **Catalogue de Modèles** dans un nouvel onglet d’éditeur.
1. Dans la barre de recherche du **Catalogue de Modèles**, tapez **OpenAI GPT-4o**.
1. Cliquez sur **+ Ajouter** pour ajouter le modèle à votre liste **Mes Modèles**. Assurez-vous d’avoir sélectionné le modèle **hébergé par GitHub**.
1. Dans la **Barre d’activités**, confirmez que le modèle **OpenAI GPT-4o** apparaît dans la liste.

### -1- Créer un agent

Le **Agent (Prompt) Builder** vous permet de créer et personnaliser vos propres agents alimentés par IA. Dans cette section, vous créez un nouvel agent et lui assignez un modèle pour piloter la conversation.

![Capture d’écran de l’interface « Calculator Agent » dans l’extension AI Toolkit pour Visual Studio Code. Sur le panneau de gauche, le modèle sélectionné est « OpenAI GPT-4o (via GitHub). » Un prompt système indique « Vous êtes un professeur à l’université enseignant les mathématiques », et le prompt utilisateur : « Explique-moi l’équation de Fourier en termes simples. » D’autres options incluent des boutons pour ajouter des outils, activer le serveur MCP, et sélectionner la sortie structurée. Un bouton bleu « Exécuter » est en bas. Sur le panneau de droite, sous « Commencer avec des exemples », trois agents types sont listés : Développeur Web (avec serveur MCP, Simplificateur CE1, Interprète de rêve, avec de brèves descriptions de leurs fonctions).](../../../../translated_images/fr/aitk-agent-builder.901e3a2960c3e477.webp)

1. Ouvrez l’extension **AI Toolkit** dans la **Barre d’activités**.
1. Dans la section **Outils**, sélectionnez **Agent (Prompt) Builder**. Cela ouvre l’**Agent (Prompt) Builder** dans un nouvel onglet de l’éditeur.
1. Cliquez sur le bouton **+ Nouvel Agent**. L’extension lance un assistant via la **Palette de commandes**.
1. Entrez le nom **Calculator Agent** et appuyez sur **Entrée**.
1. Dans l’**Agent (Prompt) Builder**, pour le champ **Modèle**, sélectionnez le modèle **OpenAI GPT-4o (via GitHub)**.

### -2- Créer un prompt système pour l’agent

Avec l’agent en place, il est temps de définir sa personnalité et son objectif. Dans cette section, vous utiliserez la fonction **Générer un prompt système** pour décrire le comportement attendu de l’agent — ici, un agent calculatrice — et laisser le modèle rédiger le prompt système pour vous.

![Capture d’écran de l'interface « Calculator Agent » dans AI Toolkit de Visual Studio Code avec une fenêtre modale ouverte intitulée « Générer un prompt ». La modale explique qu’un modèle de prompt peut être généré en partageant des détails basiques et inclut une zone de texte avec l’exemple de prompt système : « Vous êtes un assistant mathématique utile et efficace. Lorsqu’un problème d’arithmétique de base est donné, vous répondez avec le résultat correct. » En dessous, les boutons « Fermer » et « Générer ». En arrière-plan, une partie de la configuration de l’agent est visible, y compris le modèle sélectionné « OpenAI GPT-4o (via GitHub) » et les champs pour les prompts système et utilisateur.](../../../../translated_images/fr/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Pour la section **Prompts**, cliquez sur le bouton **Générer un prompt système**. Ce bouton ouvre le générateur de prompt qui utilise l'IA pour produire un prompt système pour l’agent.
1. Dans la fenêtre **Générer un prompt**, saisissez : `Vous êtes un assistant mathématique utile et efficace. Lorsqu’un problème d’arithmétique de base est donné, vous répondez avec le résultat correct.`
1. Cliquez sur le bouton **Générer**. Une notification apparaîtra en bas à droite confirmant la génération du prompt système. Une fois la génération terminée, le prompt s’affichera dans le champ **Prompt système** de l’**Agent (Prompt) Builder**.
1. Relisez le **Prompt système** et modifiez-le si nécessaire.

### -3- Créer un serveur MCP

Maintenant que vous avez défini le prompt système de votre agent — qui guide son comportement et ses réponses — il est temps d’équiper l’agent avec des capacités pratiques. Dans cette section, vous allez créer un serveur MCP calculatrice avec des outils pour effectuer des additions, soustractions, multiplications et divisions. Ce serveur permettra à votre agent d’exécuter des opérations mathématiques en temps réel en réponse à des requêtes en langage naturel.

![Capture d'écran de la section inférieure de l’interface Calculator Agent dans l’extension AI Toolkit pour Visual Studio Code. Elle montre des menus extensibles pour « Outils » et « Sortie structurée », ainsi qu’un menu déroulant intitulé « Choisissez le format de sortie » réglé sur « texte ». À droite, un bouton marqué « + MCP Server » pour ajouter un serveur Model Context Protocol. Un espace réservé pour icône d’image est visible au-dessus de la section Outils.](../../../../translated_images/fr/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit est doté de modèles pour faciliter la création de votre propre serveur MCP. Nous utiliserons le modèle Python pour créer le serveur MCP calculatrice.

*Note* : AI Toolkit supporte actuellement Python et TypeScript.

1. Dans la section **Outils** de l’**Agent (Prompt) Builder**, cliquez sur le bouton **+ MCP Server**. L’extension lancera un assistant via la **Palette de commandes**.
1. Sélectionnez **+ Ajouter un serveur**.
1. Sélectionnez **Créer un nouveau serveur MCP**.
1. Sélectionnez **python-weather** comme modèle.
1. Sélectionnez **Dossier par défaut** pour enregistrer le modèle de serveur MCP.
1. Entrez le nom suivant pour le serveur : **Calculator**
1. Une nouvelle fenêtre Visual Studio Code s'ouvrira. Sélectionnez **Oui, je fais confiance aux auteurs**.
1. Dans le terminal (**Terminal** > **Nouveau terminal**), créez un environnement virtuel : `python -m venv .venv`
1. Dans le terminal, activez l’environnement virtuel :
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Dans le terminal, installez les dépendances : `pip install -e .[dev]`
1. Dans la vue **Explorateur** de la **Barre d’activités**, développez le répertoire **src** et sélectionnez **server.py** pour ouvrir le fichier dans l’éditeur.
1. Remplacez le code dans le fichier **server.py** par ce qui suit et enregistrez :

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

### -4- Exécuter l’agent avec le serveur MCP calculatrice

Maintenant que votre agent dispose d’outils, il est temps de les utiliser ! Dans cette section, vous soumettrez des invites à l’agent pour tester et valider si l’agent utilise l’outil adéquat depuis le serveur MCP calculatrice.

![Capture d’écran de l’interface Calculator Agent dans l’extension AI Toolkit pour Visual Studio Code. Sur le panneau de gauche, sous « Outils », un serveur MCP nommé local-server-calculator_server est ajouté, affichant quatre outils disponibles : addition, soustraction, multiplication et division. Un badge montre que quatre outils sont actifs. En dessous se trouve une section « Sortie structurée » repliée et un bouton bleu « Exécuter ». Sur le panneau de droite, sous « Réponse du Modèle », l’agent invoque les outils multiplier et soustraire avec les entrées {"a": 3, "b": 25} et {"a": 75, "b": 20} respectivement. La « Réponse de l’Outil » finale est montrée comme 75,0. Un bouton « Voir le code » apparaît en bas.](../../../../translated_images/fr/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Vous exécuterez le serveur MCP calculatrice sur votre machine de développement locale via **Agent Builder** en tant que client MCP.

1. Appuyez sur la touche `F5` pour démarrer le débogage du serveur MCP. L’**Agent (Prompt) Builder** s’ouvrira dans un nouvel onglet d’éditeur. Le statut du serveur est visible dans le terminal.
1. Dans le champ **Prompt utilisateur** de l’**Agent (Prompt) Builder**, saisissez l’invite suivante : `J’ai acheté 3 articles à 25 $ chacun, puis utilisé une remise de 20 $. Combien ai-je payé ?`
1. Cliquez sur le bouton **Exécuter** pour générer la réponse de l’agent.
1. Examinez la sortie de l’agent. Le modèle devrait conclure que vous avez payé **55 $**.
1. Voici un résumé de ce qui doit se produire :
    - L’agent sélectionne les outils **multiplier** et **soustraire** pour aider au calcul.
    - Les valeurs `a` et `b` respectives sont assignées pour l’outil **multiplier**.
    - Les valeurs `a` et `b` respectives sont assignées pour l’outil **soustraire**.
    - La réponse de chaque outil est fournie dans la **Réponse de l’Outil** respective.
    - La sortie finale du modèle est fournie dans la **Réponse du Modèle** finale.
1. Soumettez d’autres invites pour tester davantage l’agent. Vous pouvez modifier l’invite existante dans le champ **Prompt utilisateur** en cliquant dans ce champ et en remplaçant l’invite actuelle.
1. Une fois que vous avez fini de tester l’agent, vous pouvez arrêter le serveur via le **terminal** en entrant **CTRL/CMD+C** pour quitter.

## Exercice

Essayez d’ajouter une entrée d’outil supplémentaire dans votre fichier **server.py** (ex : retourner la racine carrée d’un nombre). Soumettez des invites supplémentaires qui obligeraient l’agent à utiliser votre nouvel outil (ou des outils existants). Assurez-vous de redémarrer le serveur pour charger les outils nouvellement ajoutés.

## Solution

[Solution](./solution/README.md)

## Points clés à retenir

Voici les points clés de ce chapitre :

- L’extension AI Toolkit est un excellent client qui vous permet de consommer des serveurs MCP et leurs outils.
- Vous pouvez ajouter de nouveaux outils aux serveurs MCP, étendant les capacités de l’agent pour répondre aux besoins évolutifs.
- AI Toolkit inclut des modèles (par exemple, des modèles de serveurs MCP en Python) pour simplifier la création d’outils personnalisés.

## Ressources supplémentaires

- [Documentation AI Toolkit](https://aka.ms/AIToolkit/doc)

## Et après ?
- Suivant : [Tests & Débogage](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->