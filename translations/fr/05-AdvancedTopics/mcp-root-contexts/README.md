# Racines MCP (Fonctionnalité Héritée)

> [!WARNING]
> Les racines sont dépréciées à partir de MCP `2026-07-28`. Elles restent dans cette révision pour
> compatibilité et peuvent être supprimées dans la première révision de la spécification
> publiée à partir du 28 juillet 2027. Les nouvelles implémentations doivent passer
> des répertoires ou fichiers via des paramètres d’outil, des URI de ressource ou une
> configuration serveur.

## Vue d'ensemble

Les racines permettent à un client MCP d’indiquer à un serveur quels emplacements du système de fichiers sont pertinents
pour la requête en cours. Une racine contient un URI `file://` obligatoire et un nom optionnel
lisible par un humain.

Les racines sont des indications informatives. Elles ne sont pas des conteneurs d’historique de conversation,
des sessions de protocole, ni un mécanisme de contrôle d’accès. Le protocole n’impose pas
qu’un serveur reste dans les racines listées.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Expliquer ce que représentent les Racines MCP et ce qu’elles ne représentent pas.
- Reconnaître le flux multi-aller-retour actuel `roots/list`.
- Appliquer des contrôles de sécurité indépendamment des Racines.
- Migrer les nouvelles implémentations vers des alternatives prises en charge.

## Données des racines

Un client renvoie chaque racine comme un URI `file://` avec un nom d’affichage optionnel :

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Les clients doivent exposer uniquement les emplacements approuvés par l’utilisateur. Les serveurs doivent considérer
le résultat comme une indication des fichiers pertinents, non comme une preuve d’autorisation.

## Flux MCP 2026-07-28

Un client qui prend en charge les Racines déclare cette capacité dans chaque requête :

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Lors du traitement d’une requête client, un serveur peut renvoyer un
`InputRequiredResult` contenant une requête d’entrée `roots/list` :

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Le client collecte les racines approuvées et retente la requête originale avec les
`inputResponses` correspondantes et l’`requestState` inchangé. Ce schéma multi-aller-retour
maintient le protocole sans état ; il n’y a pas de poignée de main `initialize` ni
de session au niveau du protocole.

## Comportement Hérité 2025-11-25

Dans MCP `2025-11-25`, les clients annonçaient les Racines durant l’initialisation. Un serveur
pouvait émettre une requête directe `roots/list`, et un client pouvait envoyer
des `notifications/roots/list_changed` lorsque ses racines changeaient.

Ce cycle de vie est un comportement hérité. Ne combinez pas ses exemples d’initialisation ou de
notification avec une implémentation `2026-07-28`.

## Remplacements Recommandés

### Paramètres d’outil

Rendez explicites le répertoire ou le fichier requis dans le schéma de l’outil :

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URI de ressource

Utilisez les ressources MCP lorsque le serveur peut exposer les fichiers pertinents via des URI stables.
Cela rend la découverte et la récupération explicites.

### Configuration serveur

Pour les déploiements fixes, configurez les répertoires autorisés au démarrage du serveur.
Cela est souvent plus clair que de les découvrir lors d’un appel d’outil.

## Exigences de sécurité

Quel que soit le remplacement choisi :

- Obtenir le consentement de l’utilisateur avant d’exposer les emplacements du système de fichiers.
- Canonicaliser et valider les chemins pour prévenir les traversées.
- Appliquer l’autorisation et l’isolation indépendamment des valeurs des racines.
- Vérifier les autorisations lors de l’accès à un fichier, pas seulement lorsqu’il est listé.
- Éviter de retourner des chemins sensibles dans les journaux ou messages d’erreur.

## Points clés

- Les racines décrivent des emplacements pertinents du système de fichiers ; elles ne stockent pas l’état de la conversation.

- Les racines sont une indication, pas une frontière de contrôle d’accès.
- MCP `2026-07-28` transmet la capacité par requête et utilise
  `InputRequiredResult` pour `roots/list`.
- Les nouvelles implémentations doivent plutôt utiliser des paramètres d’outil, des URI de ressource ou une
  configuration serveur.

## Ressources supplémentaires

- [Racines dans MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Registre des fonctionnalités dépréciées](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Quoi de neuf dans MCP : la spécification 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->