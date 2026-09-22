# Déploiement des serveurs MCP

> [!NOTE]
> Les exemples de configuration utilisant un point de terminaison `/sse` ciblent le transport HTTP+SSE hérité. Les serveurs distants MCP `2026-07-28` utilisent Streamable HTTP, normalement à un point de terminaison défini par le serveur tel que `/mcp`.
> transport. MCP `2026-07-28` remote servers use Streamable HTTP, normally at a
> server-defined endpoint such as `/mcp`.

Le déploiement de votre serveur MCP permet à d'autres d'accéder à ses outils et ressources au-delà de votre environnement local. Plusieurs stratégies de déploiement sont à considérer, selon vos besoins en matière de scalabilité, de fiabilité et de facilité de gestion. Vous trouverez ci-dessous des conseils pour déployer des serveurs MCP localement, dans des conteneurs et dans le cloud.

## Aperçu

Cette leçon explique comment déployer votre application serveur MCP.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- Évaluer différentes approches de déploiement.
- Déployer votre application.

## Développement et déploiement local

Si votre serveur est destiné à être utilisé sur les machines des utilisateurs, vous pouvez suivre les étapes suivantes :

1. **Télécharger le serveur**. Si vous n'avez pas écrit le serveur, téléchargez-le d'abord sur votre machine.
1. **Démarrer le processus serveur** : Exécutez votre application serveur MCP

Pour SSE (non nécessaire pour un serveur de type stdio)

1. **Configurer le réseau** : Assurez-vous que le serveur est accessible via le port attendu
1. **Connecter les clients** : Utilisez des URLs de connexion locales comme `http://localhost:3000`

## Déploiement Cloud

Les serveurs MCP peuvent être déployés sur diverses plateformes cloud :

- **Fonctions sans serveur** : Déployer des serveurs MCP légers en tant que fonctions serverless
- **Services de conteneur** : Utiliser des services tels que Azure Container Apps, AWS ECS, ou Google Cloud Run
- **Kubernetes** : Déployer et gérer des serveurs MCP dans des clusters Kubernetes pour une haute disponibilité

### Exemple : Azure Container Apps

Azure Container Apps prend en charge le déploiement des serveurs MCP. C’est encore un travail en cours et il supporte actuellement les serveurs SSE.

Voici comment procéder :

1. Clonez un dépôt :

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Exécutez-le localement pour tester :

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Pour l’essayer localement, créez un fichier *mcp.json* dans un répertoire *.vscode* et ajoutez le contenu suivant :

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  Une fois le serveur SSE démarré, vous pouvez cliquer sur l'icône de lecture dans le fichier JSON, vous devriez désormais voir les outils du serveur détectés par GitHub Copilot, voir l'icône Outil.

1. Pour déployer, exécutez la commande suivante :

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Voilà, déployez-le localement ou sur Azure via ces étapes.

## Ressources supplémentaires

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Article Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Dépôt MCP Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Et après

- Suivant : [Sujets avancés sur les serveurs](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->