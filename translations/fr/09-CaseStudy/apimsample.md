# Étude de cas : Exposer une API REST dans API Management en tant que serveur MCP

Azure API Management est un service qui fournit une passerelle au-dessus de vos points de terminaison API. Son fonctionnement consiste à ce qu'Azure API Management agit comme un proxy devant vos API et peut décider quoi faire avec les requêtes entrantes.

En l'utilisant, vous ajoutez toute une série de fonctionnalités telles que :

- **Sécurité**, vous pouvez utiliser tout, des clés API, JWT à l'identité gérée.
- **Limitation de débit**, une fonctionnalité intéressante est de pouvoir décider du nombre d'appels autorisés par unité de temps. Cela aide à garantir que tous les utilisateurs ont une excellente expérience et également que votre service n'est pas submergé de requêtes.
- **Mise à l'échelle & Équilibrage de charge**. Vous pouvez configurer plusieurs points de terminaison pour répartir la charge et vous pouvez également décider comment "équilibrer la charge".
- **Fonctionnalités IA comme le cache sémantique**, la limitation et la surveillance des jetons, et plus encore. Ce sont d'excellentes fonctionnalités qui améliorent la réactivité ainsi que vous aident à contrôler vos dépenses en jetons. [En savoir plus ici](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Pourquoi MCP + Azure API Management ?

Le Model Context Protocol devient rapidement une norme pour les applications IA agentiques et la manière d'exposer les outils et données de manière cohérente. Azure API Management est un choix naturel lorsque vous avez besoin de "gérer" des API. Les serveurs MCP s'intègrent souvent à d'autres API pour résoudre des requêtes à un outil par exemple. Par conséquent, combiner Azure API Management et MCP a beaucoup de sens.

## Aperçu

Dans ce cas d'utilisation spécifique, nous allons apprendre à exposer les points de terminaison d'une API en tant que serveur MCP. Ce faisant, nous pouvons facilement intégrer ces points de terminaison dans une application agentique tout en profitant des fonctionnalités d'Azure API Management.

## Fonctionnalités clés

- Vous sélectionnez les méthodes du point de terminaison que vous souhaitez exposer en tant qu'outils.
- Les fonctionnalités supplémentaires dépendent de ce que vous configurez dans la section politique de votre API. Ici, nous allons vous montrer comment ajouter une limitation de débit.

## Pré-étape : importer une API

Si vous avez déjà une API dans Azure API Management, c'est parfait, vous pouvez alors sauter cette étape. Sinon, consultez ce lien, [importer une API dans Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Exposer l'API en tant que serveur MCP

Pour exposer les points de terminaison de l'API, suivez ces étapes :

1. Rendez-vous sur Azure Portal à l'adresse suivante <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Rendez-vous sur votre instance API Management.

1. Dans le menu de gauche, sélectionnez APIs > MCP Servers > + Créer un nouveau serveur MCP.

1. Dans API, sélectionnez une API REST à exposer en tant que serveur MCP.

1. Sélectionnez une ou plusieurs opérations API à exposer en tant qu'outils. Vous pouvez sélectionner toutes les opérations ou uniquement certaines spécifiques.

    ![Sélectionnez les méthodes à exposer](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Sélectionnez **Créer**.

1. Allez dans le menu **APIs** puis **MCP Servers**, vous devriez voir ceci :

    ![Voir le serveur MCP dans le panneau principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Le serveur MCP est créé et les opérations API sont exposées en tant qu'outils. Le serveur MCP est listé dans le panneau MCP Servers. La colonne URL montre le point de terminaison du serveur MCP que vous pouvez appeler pour tester ou depuis une application cliente.

## Optionnel : Configurer les politiques

Azure API Management possède le concept central de politiques où vous définissez différentes règles pour vos points de terminaison, par exemple la limitation de débit ou le cache sémantique. Ces politiques sont écrites en XML.

Voici comment configurer une politique pour limiter le débit de votre serveur MCP :

1. Dans le portail, sous APIs, sélectionnez **MCP Servers**.

1. Sélectionnez le serveur MCP que vous avez créé.

1. Dans le menu à gauche, sous MCP, sélectionnez **Politiques**.

1. Dans l’éditeur de politiques, ajoutez ou modifiez les politiques que vous souhaitez appliquer aux outils du serveur MCP. Les politiques sont définies au format XML. Par exemple, vous pouvez ajouter une politique pour limiter les appels aux outils du serveur MCP (dans cet exemple, 5 appels toutes les 30 secondes par adresse IP client). Voici un XML qui impose cette limitation :

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Voici une image de l’éditeur de politiques :

    ![Éditeur de politiques](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Essayez-le

Assurons-nous que notre serveur MCP fonctionne comme prévu.

> [!NOTE]
> Azure API Management expose actuellement ce serveur via le point de terminaison HTTP Streamable `/mcp`.
> L'ancien transport HTTP+SSE `/sse` est obsolète et
> doit être utilisé uniquement avec des clients hérités.

Pour cela, nous allons utiliser Visual Studio Code, GitHub Copilot et son mode Agent. Nous ajouterons le serveur MCP à un fichier *mcp.json*. Ce faisant, Visual Studio Code agira comme un client avec des capacités agentiques et les utilisateurs finaux pourront taper une invite et interagir avec ce serveur.

Voyons comment, pour ajouter le serveur MCP dans Visual Studio Code :

1. Utilisez la commande MCP : **Ajouter un serveur depuis la palette de commandes**.

1. Lorsqu'on vous le demande, sélectionnez le type de serveur : **HTTP (HTTP ou Server Sent Events)**.

1. Entrez l’URL HTTP Streamable affichée pour le serveur MCP dans API Management.
    Par exemple :
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Entrez un ID de serveur de votre choix. Cette valeur n’est pas importante mais elle vous aidera à vous souvenir de cette instance de serveur.

1. Sélectionnez si vous voulez enregistrer la configuration dans les paramètres de votre espace de travail ou dans les paramètres utilisateur.

  - **Paramètres de l’espace de travail** - La configuration du serveur est enregistrée dans un fichier .vscode/mcp.json uniquement disponible dans l’espace de travail actuel.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Paramètres utilisateur** - La configuration du serveur est ajoutée à votre fichier global *settings.json* et est disponible dans tous les espaces de travail. La configuration ressemble à ceci :

    ![Paramètre utilisateur](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Vous devez également ajouter une configuration, un en-tête pour vous assurer qu’il s’authentifie correctement vers Azure API Management. Il utilise un en-tête appelé **Ocp-Apim-Subscription-Key**. 

    - Voici comment vous pouvez l’ajouter aux paramètres :

    ![Ajout de l’en-tête pour l’authentification](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), cela provoquera l’affichage d’une invite vous demandant la valeur de la clé API que vous pouvez trouver dans Azure Portal pour votre instance Azure API Management.

   - Pour l’ajouter dans *mcp.json* à la place, vous pouvez le faire comme ceci :

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

Nous sommes maintenant configurés soit dans les paramètres soit dans *.vscode/mcp.json*. Essayons-le. 

Il devrait y avoir une icône Outils comme ceci, où les outils exposés par votre serveur sont listés :

![Outils du serveur](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Cliquez sur l’icône outils et vous devriez voir une liste d’outils comme ceci :

    ![Outils](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Entrez une invite dans le chat pour invoquer l’outil. Par exemple, si vous avez sélectionné un outil pour obtenir des informations sur une commande, vous pouvez demander à l’agent à propos d’une commande. Voici un exemple d’invite :

    ```text
    get information from order 2
    ```

    Vous verrez maintenant une icône outils vous demandant de procéder à l’appel d’un outil. Sélectionnez pour continuer l’exécution de l’outil, vous devriez voir une sortie comme ceci :

    ![Résultat de l’invite](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ce que vous voyez ci-dessus dépend des outils que vous avez configurés, mais l’idée est que vous obteniez une réponse textuelle comme ci-dessus**


## Références

Voici comment en apprendre davantage :

- [Tutoriel sur Azure API Management et MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemple Python : Sécuriser les serveurs MCP distants avec Azure API Management (expérimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratoire d’autorisation client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Utilisez l’extension Azure API Management pour VS Code afin d’importer et gérer les API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Enregistrer et découvrir les serveurs MCP distants dans Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Excellent dépôt montrant de nombreuses capacités IA avec Azure API Management
- [Ateliers AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contient des ateliers utilisant Azure Portal, une excellente manière de commencer à évaluer les capacités IA.

## Quelles sont les prochaines étapes

- Retour à : [Aperçu des études de cas](./README.md)
- Suivant : [Agents de voyage Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->