# Serveur MCP stdio - Solution .NET

> **⚠️ Important** : Cette solution a été mise à jour pour utiliser le **transport stdio** conformément à la spécification MCP 2025-06-18. Le transport SSE original a été abandonné.

## Aperçu

Cette solution .NET montre comment construire un serveur MCP en utilisant le transport stdio actuel. Le transport stdio est plus simple, plus sécurisé et offre de meilleures performances que l'approche SSE obsolète.

## Prérequis

- SDK .NET 9.0 ou version ultérieure
- Compréhension de base de l'injection de dépendances .NET

## Instructions de configuration

### Étape 1 : Restaurer les dépendances

```bash
dotnet restore
```

### Étape 2 : Compiler le projet

```bash
dotnet build
```

## Exécution du serveur

Le serveur stdio fonctionne différemment de l'ancien serveur basé sur HTTP. Au lieu de démarrer un serveur web, il communique via stdin/stdout :

```bash
dotnet run
```

**Important** : Le serveur semblera se bloquer - c'est normal ! Il attend des messages JSON-RPC via stdin.

## Tester le serveur

### Méthode 1 : Utiliser l'Inspecteur MCP (Recommandé)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Cela permettra :
1. De lancer votre serveur en tant que sous-processus
2. D'ouvrir une interface web pour les tests
3. De tester tous les outils du serveur de manière interactive

### Méthode 2 : Test direct en ligne de commande

Vous pouvez également tester en lançant directement l'Inspecteur :

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Outils disponibles

Le serveur propose les outils suivants :

- **AddNumbers(a, b)** : Additionner deux nombres
- **MultiplyNumbers(a, b)** : Multiplier deux nombres  
- **GetGreeting(name)** : Générer un message de salutation personnalisé
- **GetServerInfo()** : Obtenir des informations sur le serveur

### Tester avec Claude Desktop

Pour utiliser ce serveur avec Claude Desktop, ajoutez cette configuration à votre fichier `claude_desktop_config.json` :

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Structure du projet

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Différences clés entre HTTP/SSE et stdio

**Transport stdio (Actuel) :**
- ✅ Configuration simplifiée - pas besoin de serveur web
- ✅ Meilleure sécurité - pas de points de terminaison HTTP
- ✅ Utilise `Host.CreateApplicationBuilder()` au lieu de `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` au lieu de `WithHttpTransport()`
- ✅ Application console au lieu d'application web
- ✅ Meilleures performances

**Transport HTTP/SSE (Obsolète) :**
- ❌ Nécessitait un serveur web ASP.NET Core
- ❌ Requiert une configuration de routage `app.MapMcp()`
- ❌ Configuration et dépendances plus complexes
- ❌ Considérations supplémentaires en matière de sécurité
- ❌ Désormais abandonné dans MCP 2025-06-18

## Fonctionnalités de développement

- **Injection de dépendances** : Support complet de l'injection de dépendances pour les services et la journalisation
- **Journalisation structurée** : Journalisation appropriée vers stderr en utilisant `ILogger<T>`
- **Attributs d'outils** : Définition claire des outils avec les attributs `[McpServerTool]`
- **Support asynchrone** : Tous les outils prennent en charge les opérations asynchrones
- **Gestion des erreurs** : Gestion des erreurs et journalisation élégantes

## Conseils de développement

- Utilisez `ILogger` pour la journalisation (ne jamais écrire directement sur stdout)
- Compilez avec `dotnet build` avant de tester
- Testez avec l'Inspecteur pour un débogage visuel
- Toute la journalisation est automatiquement dirigée vers stderr
- Le serveur gère les signaux d'arrêt de manière élégante

Cette solution suit la spécification MCP actuelle et illustre les meilleures pratiques pour l'implémentation du transport stdio avec .NET.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.