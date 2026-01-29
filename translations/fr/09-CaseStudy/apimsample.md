# Étude de cas : Exposer une API REST dans API Management en tant que serveur MCP

Azure API Management est un service qui fournit une passerelle au-dessus de vos points de terminaison API. Son fonctionnement repose sur le fait qu'Azure API Management agit comme un proxy devant vos API et peut décider quoi faire des requêtes entrantes.

En l'utilisant, vous ajoutez une multitude de fonctionnalités telles que :

- **Sécurité** : vous pouvez utiliser tout, des clés API, JWT à l'identité managée.
- **Limitation de débit** : une fonctionnalité très utile est de pouvoir décider combien d'appels sont autorisés par unité de temps. Cela garantit une expérience optimale pour tous les utilisateurs et évite que votre service ne soit submergé par des requêtes.
- **Mise à l'échelle et équilibrage de charge** : vous pouvez configurer plusieurs points de terminaison pour répartir la charge et décider comment effectuer l'équilibrage de charge.
- **Fonctionnalités d'IA comme la mise en cache sémantique**, la limitation et la surveillance des jetons, et bien plus encore. Ces fonctionnalités améliorent la réactivité et vous aident à mieux gérer votre consommation de jetons. [En savoir plus ici](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Pourquoi MCP + Azure API Management ?

Le Model Context Protocol devient rapidement une norme pour les applications d'IA agentiques et pour exposer des outils et des données de manière cohérente. Azure API Management est un choix naturel lorsque vous devez "gérer" des API. Les serveurs MCP s'intègrent souvent à d'autres API pour résoudre des requêtes vers un outil, par exemple. Par conséquent, combiner Azure API Management et MCP est tout à fait logique.

## Vue d'ensemble

Dans ce cas d'utilisation spécifique, nous allons apprendre à exposer des points de terminaison API en tant que serveur MCP. En procédant ainsi, nous pouvons facilement intégrer ces points de terminaison dans une application agentique tout en tirant parti des fonctionnalités d'Azure API Management.

## Fonctionnalités clés

- Vous sélectionnez les méthodes des points de terminaison que vous souhaitez exposer en tant qu'outils.
- Les fonctionnalités supplémentaires dépendent de ce que vous configurez dans la section des politiques pour votre API. Ici, nous vous montrerons comment ajouter une limitation de débit.

## Étape préalable : importer une API

Si vous avez déjà une API dans Azure API Management, parfait, vous pouvez passer cette étape. Sinon, consultez ce lien : [importer une API dans Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Exposer une API en tant que serveur MCP

Pour exposer les points de terminaison API, suivez ces étapes :

1. Accédez au portail Azure à l'adresse suivante : <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Naviguez jusqu'à votre instance API Management.

1. Dans le menu de gauche, sélectionnez **APIs > MCP Servers > + Create new MCP Server**.

1. Dans **API**, sélectionnez une API REST à exposer en tant que serveur MCP.

1. Sélectionnez une ou plusieurs opérations API à exposer en tant qu'outils. Vous pouvez sélectionner toutes les opérations ou seulement certaines.

    ![Sélectionner les méthodes à exposer](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Cliquez sur **Create**.

1. Naviguez dans le menu **APIs** et **MCP Servers**, vous devriez voir ce qui suit :

    ![Voir le serveur MCP dans le panneau principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Le serveur MCP est créé et les opérations API sont exposées en tant qu'outils. Le serveur MCP est listé dans le panneau MCP Servers. La colonne URL montre le point de terminaison du serveur MCP que vous pouvez appeler pour tester ou utiliser dans une application cliente.

## Optionnel : Configurer des politiques

Azure API Management repose sur le concept central de politiques, où vous configurez différentes règles pour vos points de terminaison, comme la limitation de débit ou la mise en cache sémantique. Ces politiques sont rédigées en XML.

Voici comment configurer une politique pour limiter le débit de votre serveur MCP :

1. Dans le portail, sous **APIs**, sélectionnez **MCP Servers**.

1. Sélectionnez le serveur MCP que vous avez créé.

1. Dans le menu de gauche, sous **MCP**, sélectionnez **Policies**.

1. Dans l'éditeur de politiques, ajoutez ou modifiez les politiques que vous souhaitez appliquer aux outils du serveur MCP. Les politiques sont définies en format XML. Par exemple, vous pouvez ajouter une politique pour limiter les appels aux outils du serveur MCP (dans cet exemple, 5 appels toutes les 30 secondes par adresse IP client). Voici un exemple de XML pour limiter le débit :

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Voici une image de l'éditeur de politiques :

    ![Éditeur de politiques](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Tester

Assurons-nous que notre serveur MCP fonctionne comme prévu.

Pour cela, nous utiliserons Visual Studio Code, GitHub Copilot et son mode Agent. Nous ajouterons le serveur MCP à un fichier *mcp.json*. En procédant ainsi, Visual Studio Code agira comme un client avec des capacités agentiques, et les utilisateurs finaux pourront saisir une invite et interagir avec ce serveur.

Voici comment ajouter le serveur MCP dans Visual Studio Code :

1. Utilisez la commande **MCP: Add Server** depuis la palette de commandes.

1. Lorsque vous y êtes invité, sélectionnez le type de serveur : **HTTP (HTTP ou Server Sent Events)**.

1. Entrez l'URL du serveur MCP dans API Management. Exemple : **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (pour le point de terminaison SSE) ou **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (pour le point de terminaison MCP). Notez la différence entre les transports : `/sse` ou `/mcp`.

1. Entrez un identifiant de serveur de votre choix. Cette valeur n'est pas importante, mais elle vous aidera à vous souvenir de cette instance de serveur.

1. Sélectionnez si vous souhaitez enregistrer la configuration dans les paramètres de votre espace de travail ou dans les paramètres utilisateur.

  - **Paramètres de l'espace de travail** : la configuration du serveur est enregistrée dans un fichier *.vscode/mcp.json* uniquement disponible dans l'espace de travail actuel.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ou si vous choisissez HTTP en streaming comme transport, ce serait légèrement différent :

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Paramètres utilisateur** : la configuration du serveur est ajoutée à votre fichier global *settings.json* et est disponible dans tous les espaces de travail. La configuration ressemble à ceci :

    ![Paramètre utilisateur](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Vous devez également ajouter une configuration, un en-tête pour vous assurer que l'authentification fonctionne correctement avec Azure API Management. Cela utilise un en-tête appelé **Ocp-Apim-Subscription-Key**.

    - Voici comment l'ajouter aux paramètres :

    ![Ajout d'un en-tête pour l'authentification](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). Cela affichera une invite pour saisir la valeur de la clé API, que vous pouvez trouver dans le portail Azure pour votre instance Azure API Management.

   - Pour l'ajouter à *mcp.json*, vous pouvez le faire comme suit :

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Utiliser le mode Agent

Nous sommes maintenant prêts, que ce soit dans les paramètres ou dans *.vscode/mcp.json*. Essayons.

Il devrait y avoir une icône d'outils comme celle-ci, où les outils exposés depuis votre serveur sont listés :

![Outils depuis le serveur](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Cliquez sur l'icône des outils, et vous devriez voir une liste d'outils comme ceci :

    ![Outils](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Saisissez une invite dans le chat pour invoquer l'outil. Par exemple, si vous avez sélectionné un outil pour obtenir des informations sur une commande, vous pouvez demander à l'agent des informations sur une commande. Voici un exemple d'invite :

    ```text
    get information from order 2
    ```

    Vous verrez maintenant une icône d'outils vous demandant de continuer à appeler un outil. Sélectionnez pour continuer l'exécution de l'outil, et vous devriez voir un résultat comme ceci :

    ![Résultat de l'invite](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Ce que vous voyez ci-dessus dépend des outils que vous avez configurés, mais l'idée est que vous obtenez une réponse textuelle comme ci-dessus.**

## Références

Voici comment en apprendre davantage :

- [Tutoriel sur Azure API Management et MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemple Python : Sécuriser des serveurs MCP distants avec Azure API Management (expérimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratoire d'autorisation client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Utiliser l'extension Azure API Management pour VS Code pour importer et gérer des API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Enregistrer et découvrir des serveurs MCP distants dans Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) : Excellent dépôt montrant de nombreuses capacités d'IA avec Azure API Management.
- [Ateliers AI Gateway](https://azure-samples.github.io/AI-Gateway/) : Contient des ateliers utilisant le portail Azure, une excellente façon de commencer à évaluer les capacités d'IA.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.