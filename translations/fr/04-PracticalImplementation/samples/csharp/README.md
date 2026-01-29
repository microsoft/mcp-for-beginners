# Exemple

L'exemple précédent montre comment utiliser un projet .NET local avec le type `stdio`. Et comment exécuter le serveur localement dans un conteneur. C’est une bonne solution dans de nombreuses situations. Cependant, il peut être utile d’avoir le serveur qui tourne à distance, par exemple dans un environnement cloud. C’est là qu’intervient le type `http`.

En regardant la solution dans le dossier `04-PracticalImplementation`, elle peut sembler bien plus complexe que la précédente. Mais en réalité, ce n’est pas le cas. Si vous regardez de près le projet `src/Calculator`, vous verrez que c’est essentiellement le même code que dans l’exemple précédent. La seule différence est que nous utilisons une bibliothèque différente, `ModelContextProtocol.AspNetCore`, pour gérer les requêtes HTTP. Et nous modifions la méthode `IsPrime` pour la rendre privée, juste pour montrer que vous pouvez avoir des méthodes privées dans votre code. Le reste du code est identique à avant.

Les autres projets proviennent de [.NET Aspire](https://learn.microsoft.com/dotnet/aspire/get-started/aspire-overview). Avoir .NET Aspire dans la solution améliore l’expérience du développeur lors du développement et des tests, et aide à l’observabilité. Ce n’est pas obligatoire pour faire tourner le serveur, mais c’est une bonne pratique de l’avoir dans votre solution.

## Démarrer le serveur localement

1. Depuis VS Code (avec l’extension C# DevKit), naviguez jusqu’au répertoire `04-PracticalImplementation/samples/csharp`.
1. Exécutez la commande suivante pour démarrer le serveur :

   ```bash
    dotnet watch run --project ./src/AppHost
   ```

1. Quand un navigateur web ouvre le tableau de bord .NET Aspire, notez l’URL `http`. Elle devrait ressembler à `http://localhost:5058/`.

   ![.NET Aspire Dashboard](../../../../../translated_images/fr/dotnet-aspire-dashboard.0a7095710e9301e9.webp)

## Tester Streamable HTTP avec le MCP Inspector

Si vous avez Node.js 22.7.5 ou une version supérieure, vous pouvez utiliser le MCP Inspector pour tester votre serveur.

Démarrez le serveur et lancez la commande suivante dans un terminal :

```bash
npx @modelcontextprotocol/inspector http://localhost:5058
```

![MCP Inspector](../../../../../translated_images/fr/mcp-inspector.c223422b9b494fb4.webp)

- Sélectionnez `Streamable HTTP` comme type de transport.
- Dans le champ Url, entrez l’URL du serveur notée précédemment, en ajoutant `/mcp`. Cela doit être en `http` (pas en `https`), par exemple `http://localhost:5058/mcp`.
- Cliquez sur le bouton Connect.

Un avantage de l’Inspector est qu’il offre une bonne visibilité sur ce qui se passe.

- Essayez de lister les outils disponibles
- Testez-en quelques-uns, cela devrait fonctionner comme avant.

## Tester le serveur MCP avec GitHub Copilot Chat dans VS Code

Pour utiliser le transport Streamable HTTP avec GitHub Copilot Chat, modifiez la configuration du serveur `calc-mcp` créé précédemment pour qu’elle ressemble à ceci :

```jsonc
// .vscode/mcp.json
{
  "servers": {
    "calc-mcp": {
      "type": "http",
      "url": "http://localhost:5058/mcp"
    }
  }
}
```

Faites quelques tests :

- Demandez « 3 nombres premiers après 6780 ». Notez que Copilot utilisera les nouveaux outils `NextFivePrimeNumbers` et ne retournera que les 3 premiers nombres premiers.
- Demandez « 7 nombres premiers après 111 », pour voir ce qui se passe.
- Demandez « John a 24 sucettes et veut les distribuer à ses 3 enfants. Combien de sucettes chaque enfant reçoit-il ? », pour voir ce qui se passe.

## Déployer le serveur sur Azure

Déployons le serveur sur Azure pour que plus de personnes puissent l’utiliser.

Depuis un terminal, naviguez dans le dossier `04-PracticalImplementation/samples/csharp` et exécutez la commande suivante :

```bash
azd up
```

Une fois le déploiement terminé, vous devriez voir un message comme celui-ci :

![Azd deployment success](../../../../../translated_images/fr/azd-deployment-success.bd42940493f1b834.webp)

Récupérez l’URL et utilisez-la dans le MCP Inspector et dans GitHub Copilot Chat.

```jsonc
// .vscode/mcp.json
{
  "servers": {
    "calc-mcp": {
      "type": "http",
      "url": "https://calc-mcp.gentleriver-3977fbcf.australiaeast.azurecontainerapps.io/mcp"
    }
  }
}
```

## Et ensuite ?

Nous avons essayé différents types de transport et outils de test. Nous avons aussi déployé votre serveur MCP sur Azure. Mais que faire si notre serveur doit accéder à des ressources privées ? Par exemple, une base de données ou une API privée ? Dans le chapitre suivant, nous verrons comment renforcer la sécurité de notre serveur.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.