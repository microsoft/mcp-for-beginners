# Serveur MCP Météo

Ceci est un exemple de serveur MCP en Python qui implémente des outils météo avec des réponses simulées. Il peut servir de base pour votre propre serveur MCP. Il inclut les fonctionnalités suivantes :

- **Outil Météo** : Un outil qui fournit des informations météo simulées basées sur l'emplacement donné.
- **Outil de Clonage Git** : Un outil qui clone un dépôt Git dans un dossier spécifié.
- **Outil d'Ouverture VS Code** : Un outil qui ouvre un dossier dans VS Code ou VS Code Insiders.
- **Connexion au Constructeur d'Agent** : Une fonctionnalité permettant de connecter le serveur MCP au Constructeur d'Agent pour tester et déboguer.
- **Débogage dans [MCP Inspector](https://github.com/modelcontextprotocol/inspector)** : Une fonctionnalité permettant de déboguer le serveur MCP à l'aide de MCP Inspector.

## Commencer avec le modèle de serveur MCP Météo

> **Prérequis**
>
> Pour exécuter le serveur MCP sur votre machine de développement locale, vous aurez besoin de :
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Requis pour l'outil git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) ou [VS Code Insiders](https://code.visualstudio.com/insiders/) (Requis pour l'outil open_in_vscode)
> - (*Optionnel - si vous préférez uv*) [uv](https://github.com/astral-sh/uv)
> - [Extension de Débogage Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Préparer l'environnement

Il existe deux approches pour configurer l'environnement de ce projet. Vous pouvez choisir celle qui vous convient le mieux.

> Remarque : Rechargez VSCode ou le terminal pour vous assurer que l'environnement virtuel Python est utilisé après sa création.

| Approche | Étapes |
| -------- | ------ |
| Utilisation de `uv` | 1. Créer un environnement virtuel : `uv venv` <br>2. Exécuter la commande VSCode "***Python: Select Interpreter***" et sélectionner le Python de l'environnement virtuel créé <br>3. Installer les dépendances (y compris les dépendances de développement) : `uv pip install -r pyproject.toml --extra dev` |
| Utilisation de `pip` | 1. Créer un environnement virtuel : `python -m venv .venv` <br>2. Exécuter la commande VSCode "***Python: Select Interpreter***" et sélectionner le Python de l'environnement virtuel créé <br>3. Installer les dépendances (y compris les dépendances de développement) : `pip install -e .[dev]` |

Après avoir configuré l'environnement, vous pouvez exécuter le serveur sur votre machine de développement locale via le Constructeur d'Agent en tant que client MCP pour commencer :
1. Ouvrez le panneau de débogage de VS Code. Sélectionnez `Debug in Agent Builder` ou appuyez sur `F5` pour démarrer le débogage du serveur MCP.
2. Utilisez AI Toolkit Agent Builder pour tester le serveur avec [ce prompt](../../../../../../../../../../../open_prompt_builder). Le serveur sera automatiquement connecté au Constructeur d'Agent.
3. Cliquez sur `Run` pour tester le serveur avec le prompt.

**Félicitations** ! Vous avez réussi à exécuter le serveur MCP Météo sur votre machine de développement locale via le Constructeur d'Agent en tant que client MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Contenu inclus dans le modèle

| Dossier / Fichier | Contenu                                     |
| ----------------- | ------------------------------------------- |
| `.vscode`         | Fichiers VSCode pour le débogage            |
| `.aitk`           | Configurations pour AI Toolkit              |
| `src`             | Code source du serveur MCP Météo            |

## Comment déboguer le serveur MCP Météo

> Remarques :
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) est un outil visuel de développement pour tester et déboguer les serveurs MCP.
> - Tous les modes de débogage prennent en charge les points d'arrêt, vous pouvez donc ajouter des points d'arrêt au code d'implémentation des outils.

## Outils disponibles

### Outil Météo
L'outil `get_weather` fournit des informations météo simulées pour un emplacement spécifié.

| Paramètre | Type   | Description |
| --------- | ------ | ----------- |
| `location` | string | Emplacement pour obtenir les informations météo (par exemple, nom de la ville, état ou coordonnées) |

### Outil de Clonage Git
L'outil `git_clone_repo` clone un dépôt Git dans un dossier spécifié.

| Paramètre       | Type   | Description |
| --------------- | ------ | ----------- |
| `repo_url`      | string | URL du dépôt Git à cloner |
| `target_folder` | string | Chemin vers le dossier où le dépôt doit être cloné |

L'outil retourne un objet JSON avec :
- `success` : Booléen indiquant si l'opération a réussi
- `target_folder` ou `error` : Le chemin du dépôt cloné ou un message d'erreur

### Outil d'Ouverture VS Code
L'outil `open_in_vscode` ouvre un dossier dans l'application VS Code ou VS Code Insiders.

| Paramètre      | Type               | Description |
| -------------- | ------------------ | ----------- |
| `folder_path`  | string             | Chemin vers le dossier à ouvrir |
| `use_insiders` | boolean (optionnel) | Indique si VS Code Insiders doit être utilisé à la place de VS Code classique |

L'outil retourne un objet JSON avec :
- `success` : Booléen indiquant si l'opération a réussi
- `message` ou `error` : Un message de confirmation ou un message d'erreur

| Mode de Débogage | Description | Étapes pour déboguer |
| ---------------- | ----------- | -------------------- |
| Constructeur d'Agent | Déboguer le serveur MCP dans le Constructeur d'Agent via AI Toolkit. | 1. Ouvrez le panneau de débogage de VS Code. Sélectionnez `Debug in Agent Builder` et appuyez sur `F5` pour démarrer le débogage du serveur MCP.<br>2. Utilisez AI Toolkit Agent Builder pour tester le serveur avec [ce prompt](../../../../../../../../../../../open_prompt_builder). Le serveur sera automatiquement connecté au Constructeur d'Agent.<br>3. Cliquez sur `Run` pour tester le serveur avec le prompt. |
| MCP Inspector | Déboguer le serveur MCP à l'aide de MCP Inspector. | 1. Installer [Node.js](https://nodejs.org/)<br> 2. Configurer Inspector : `cd inspector` && `npm install` <br> 3. Ouvrez le panneau de débogage de VS Code. Sélectionnez `Debug SSE in Inspector (Edge)` ou `Debug SSE in Inspector (Chrome)`. Appuyez sur F5 pour démarrer le débogage.<br> 4. Lorsque MCP Inspector se lance dans le navigateur, cliquez sur le bouton `Connect` pour connecter ce serveur MCP.<br> 5. Ensuite, vous pouvez `List Tools`, sélectionner un outil, entrer des paramètres, et `Run Tool` pour déboguer votre code serveur.<br> |

## Ports par défaut et personnalisations

| Mode de Débogage | Ports | Définitions | Personnalisations | Remarque |
| ---------------- | ----- | ----------- | ----------------- | -------- |
| Constructeur d'Agent | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Modifier [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) pour changer les ports ci-dessus. | N/A |
| MCP Inspector | 3001 (Serveur); 5173 et 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Modifier [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) pour changer les ports ci-dessus. | N/A |

## Retour d'information

Si vous avez des commentaires ou des suggestions pour ce modèle, veuillez ouvrir un problème sur le [dépôt GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle effectuée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.