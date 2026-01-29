# Serveur MCP Météo

Ceci est un exemple de serveur MCP en Python implémentant des outils météo avec des réponses simulées. Il peut servir de base pour votre propre serveur MCP. Il inclut les fonctionnalités suivantes :

- **Outil Météo** : Un outil qui fournit des informations météo simulées en fonction de la localisation donnée.
- **Connexion à Agent Builder** : Une fonctionnalité qui vous permet de connecter le serveur MCP à Agent Builder pour les tests et le débogage.
- **Débogage dans [MCP Inspector](https://github.com/modelcontextprotocol/inspector)** : Une fonctionnalité qui permet de déboguer le serveur MCP en utilisant MCP Inspector.

## Démarrer avec le modèle de serveur MCP Météo

> **Prérequis**
>
> Pour exécuter le serveur MCP sur votre machine de développement locale, vous aurez besoin de :
>
> - [Python](https://www.python.org/)
> - (*Optionnel - si vous préférez uv*) [uv](https://github.com/astral-sh/uv)
> - [Extension Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Préparer l’environnement

Il existe deux méthodes pour configurer l’environnement de ce projet. Vous pouvez choisir celle qui vous convient le mieux.

> Note : Rechargez VSCode ou le terminal pour vous assurer que le Python de l’environnement virtuel est utilisé après sa création.

| Méthode | Étapes |
| -------- | ----- |
| Utilisation de `uv` | 1. Créez l’environnement virtuel : `uv venv` <br>2. Lancez la commande VSCode "***Python: Select Interpreter***" et sélectionnez le Python de l’environnement virtuel créé <br>3. Installez les dépendances (y compris les dépendances de développement) : `uv pip install -r pyproject.toml --extra dev` |
| Utilisation de `pip` | 1. Créez l’environnement virtuel : `python -m venv .venv` <br>2. Lancez la commande VSCode "***Python: Select Interpreter***" et sélectionnez le Python de l’environnement virtuel créé<br>3. Installez les dépendances (y compris les dépendances de développement) : `pip install -e .[dev]` |

Une fois l’environnement configuré, vous pouvez lancer le serveur sur votre machine locale via Agent Builder en tant que client MCP pour commencer :
1. Ouvrez le panneau de débogage de VS Code. Sélectionnez `Debug in Agent Builder` ou appuyez sur `F5` pour démarrer le débogage du serveur MCP.
2. Utilisez AI Toolkit Agent Builder pour tester le serveur avec [ce prompt](../../../../../../../../../../open_prompt_builder). Le serveur sera automatiquement connecté à Agent Builder.
3. Cliquez sur `Run` pour tester le serveur avec le prompt.

**Félicitations** ! Vous avez réussi à lancer le serveur MCP Météo sur votre machine locale via Agent Builder en tant que client MCP.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Contenu du modèle

| Dossier / Fichier | Contenu                                     |
| ----------------- | ------------------------------------------- |
| `.vscode`         | Fichiers VSCode pour le débogage            |
| `.aitk`           | Configurations pour AI Toolkit               |
| `src`             | Le code source du serveur MCP météo         |

## Comment déboguer le serveur MCP Météo

> Notes :
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) est un outil visuel pour développeurs permettant de tester et déboguer les serveurs MCP.
> - Tous les modes de débogage supportent les points d’arrêt, vous pouvez donc en ajouter dans le code d’implémentation des outils.

| Mode de débogage | Description | Étapes pour déboguer |
| ---------------- | ----------- | -------------------- |
| Agent Builder | Déboguer le serveur MCP dans Agent Builder via AI Toolkit. | 1. Ouvrez le panneau de débogage de VS Code. Sélectionnez `Debug in Agent Builder` et appuyez sur `F5` pour démarrer le débogage du serveur MCP.<br>2. Utilisez AI Toolkit Agent Builder pour tester le serveur avec [ce prompt](../../../../../../../../../../open_prompt_builder). Le serveur sera automatiquement connecté à Agent Builder.<br>3. Cliquez sur `Run` pour tester le serveur avec le prompt. |
| MCP Inspector | Déboguer le serveur MCP en utilisant MCP Inspector. | 1. Installez [Node.js](https://nodejs.org/)<br>2. Configurez Inspector : `cd inspector` && `npm install` <br>3. Ouvrez le panneau de débogage de VS Code. Sélectionnez `Debug SSE in Inspector (Edge)` ou `Debug SSE in Inspector (Chrome)`. Appuyez sur F5 pour démarrer le débogage.<br>4. Lorsque MCP Inspector s’ouvre dans le navigateur, cliquez sur le bouton `Connect` pour connecter ce serveur MCP.<br>5. Vous pouvez alors `List Tools`, sélectionner un outil, saisir des paramètres, et `Run Tool` pour déboguer votre code serveur.<br> |

## Ports par défaut et personnalisations

| Mode de débogage | Ports | Définitions | Personnalisations | Remarque |
| ---------------- | ----- | ----------- | ----------------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Modifiez [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) pour changer ces ports. | N/A |
| MCP Inspector | 3001 (Serveur) ; 5173 et 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Modifiez [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) pour changer ces ports. | N/A |

## Retour d’expérience

Si vous avez des retours ou des suggestions concernant ce modèle, veuillez ouvrir une issue sur le [dépôt GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.