# Serveur MCP avec transport stdio

> **⚠️ Mise à jour importante** : À partir de la spécification MCP du 18 juin 2025, le transport SSE (Server-Sent Events) autonome a été **déprécié** et remplacé par le transport "HTTP Streamable". La spécification MCP actuelle définit deux mécanismes de transport principaux :
> 1. **stdio** - Entrée/sortie standard (recommandé pour les serveurs locaux)
> 2. **HTTP Streamable** - Pour les serveurs distants pouvant utiliser SSE en interne
>
> Cette leçon a été mise à jour pour se concentrer sur le **transport stdio**, qui est l'approche recommandée pour la plupart des implémentations de serveurs MCP.

Le transport stdio permet aux serveurs MCP de communiquer avec les clients via les flux d'entrée et de sortie standard. C'est le mécanisme de transport le plus couramment utilisé et recommandé dans la spécification MCP actuelle, offrant une méthode simple et efficace pour construire des serveurs MCP facilement intégrables à diverses applications clientes.

## Vue d'ensemble

Cette leçon explique comment construire et utiliser des serveurs MCP en utilisant le transport stdio.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Construire un serveur MCP en utilisant le transport stdio.
- Déboguer un serveur MCP avec l'Inspector.
- Utiliser un serveur MCP avec Visual Studio Code.
- Comprendre les mécanismes de transport MCP actuels et pourquoi le stdio est recommandé.

## Transport stdio - Comment ça fonctionne

Le transport stdio est l'un des deux types de transport pris en charge dans la spécification MCP actuelle (18 juin 2025). Voici comment il fonctionne :

- **Communication simple** : Le serveur lit les messages JSON-RPC depuis l'entrée standard (`stdin`) et envoie des messages à la sortie standard (`stdout`).
- **Basé sur les processus** : Le client lance le serveur MCP en tant que sous-processus.
- **Format des messages** : Les messages sont des requêtes, notifications ou réponses JSON-RPC individuelles, délimitées par des sauts de ligne.
- **Journalisation** : Le serveur PEUT écrire des chaînes UTF-8 sur la sortie d'erreur standard (`stderr`) à des fins de journalisation.

### Exigences clés :
- Les messages DOIVENT être délimités par des sauts de ligne et NE DOIVENT PAS contenir de sauts de ligne intégrés.
- Le serveur NE DOIT PAS écrire quoi que ce soit sur `stdout` qui ne soit pas un message MCP valide.
- Le client NE DOIT PAS écrire quoi que ce soit sur `stdin` du serveur qui ne soit pas un message MCP valide.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

Dans le code précédent :

- Nous importons la classe `Server` et `StdioServerTransport` depuis le SDK MCP.
- Nous créons une instance de serveur avec une configuration et des capacités de base.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Dans le code précédent, nous :

- Créons une instance de serveur en utilisant le SDK MCP.
- Définissons des outils à l'aide de décorateurs.
- Utilisons le gestionnaire de contexte stdio_server pour gérer le transport.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

La principale différence par rapport au SSE est que les serveurs stdio :

- N'ont pas besoin de configuration de serveur web ou de points de terminaison HTTP.
- Sont lancés en tant que sous-processus par le client.
- Communiquent via les flux stdin/stdout.
- Sont plus simples à implémenter et à déboguer.

## Exercice : Créer un serveur stdio

Pour créer notre serveur, nous devons garder deux choses à l'esprit :

- Nous devons utiliser un serveur web pour exposer des points de terminaison pour la connexion et les messages.

## Atelier : Créer un serveur MCP stdio simple

Dans cet atelier, nous allons créer un serveur MCP simple en utilisant le transport stdio recommandé. Ce serveur exposera des outils que les clients pourront appeler en utilisant le protocole Model Context.

### Prérequis

- Python 3.8 ou version ultérieure
- SDK MCP Python : `pip install mcp`
- Compréhension de base de la programmation asynchrone

Commençons par créer notre premier serveur MCP stdio :

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Différences clés par rapport à l'approche SSE dépréciée

**Transport stdio (norme actuelle) :**
- Modèle simple de sous-processus - le client lance le serveur en tant que processus enfant.
- Communication via stdin/stdout en utilisant des messages JSON-RPC.
- Pas besoin de configuration de serveur HTTP.
- Meilleures performances et sécurité.
- Débogage et développement plus faciles.

**Transport SSE (déprécié depuis le 18 juin 2025) :**
- Nécessitait un serveur HTTP avec des points de terminaison SSE.
- Configuration plus complexe avec une infrastructure de serveur web.
- Considérations de sécurité supplémentaires pour les points de terminaison HTTP.
- Maintenant remplacé par HTTP Streamable pour les scénarios basés sur le web.

### Créer un serveur avec le transport stdio

Pour créer notre serveur stdio, nous devons :

1. **Importer les bibliothèques nécessaires** - Nous avons besoin des composants du serveur MCP et du transport stdio.
2. **Créer une instance de serveur** - Définir le serveur avec ses capacités.
3. **Définir des outils** - Ajouter les fonctionnalités que nous voulons exposer.
4. **Configurer le transport** - Configurer la communication stdio.
5. **Exécuter le serveur** - Démarrer le serveur et gérer les messages.

Construisons cela étape par étape :

### Étape 1 : Créer un serveur stdio de base

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Étape 2 : Ajouter plus d'outils

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Étape 3 : Exécuter le serveur

Enregistrez le code sous `server.py` et exécutez-le depuis la ligne de commande :

```bash
python server.py
```

Le serveur démarrera et attendra des entrées sur stdin. Il communique en utilisant des messages JSON-RPC via le transport stdio.

### Étape 4 : Tester avec l'Inspector

Vous pouvez tester votre serveur en utilisant l'Inspector MCP :

1. Installez l'Inspector : `npx @modelcontextprotocol/inspector`
2. Exécutez l'Inspector et pointez-le vers votre serveur.
3. Testez les outils que vous avez créés.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Déboguer votre serveur stdio

### Utiliser l'Inspector MCP

L'Inspector MCP est un outil précieux pour déboguer et tester les serveurs MCP. Voici comment l'utiliser avec votre serveur stdio :

1. **Installer l'Inspector** :
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Exécuter l'Inspector** :
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Tester votre serveur** : L'Inspector fournit une interface web où vous pouvez :
   - Voir les capacités du serveur.
   - Tester les outils avec différents paramètres.
   - Surveiller les messages JSON-RPC.
   - Déboguer les problèmes de connexion.

### Utiliser VS Code

Vous pouvez également déboguer votre serveur MCP directement dans VS Code :

1. Créez une configuration de lancement dans `.vscode/launch.json` :
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Placez des points d'arrêt dans le code de votre serveur.
3. Exécutez le débogueur et testez avec l'Inspector.

### Conseils de débogage courants

- Utilisez `stderr` pour la journalisation - n'écrivez jamais sur `stdout` car il est réservé aux messages MCP.
- Assurez-vous que tous les messages JSON-RPC sont délimités par des sauts de ligne.
- Testez d'abord avec des outils simples avant d'ajouter des fonctionnalités complexes.
- Utilisez l'Inspector pour vérifier les formats de messages.

## Utiliser votre serveur stdio dans VS Code

Une fois que vous avez construit votre serveur MCP stdio, vous pouvez l'intégrer à VS Code pour l'utiliser avec Claude ou d'autres clients compatibles MCP.

### Configuration

1. **Créez un fichier de configuration MCP** à `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ou `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) :

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Redémarrez Claude** : Fermez et rouvrez Claude pour charger la nouvelle configuration du serveur.

3. **Testez la connexion** : Démarrez une conversation avec Claude et essayez d'utiliser les outils de votre serveur :
   - "Peux-tu me saluer en utilisant l'outil de salutation ?"
   - "Calcule la somme de 15 et 27."
   - "Quelles sont les informations du serveur ?"

### Exemple de serveur stdio en TypeScript

Voici un exemple complet en TypeScript pour référence :

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Exemple de serveur stdio en .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Résumé

Dans cette leçon mise à jour, vous avez appris à :

- Construire des serveurs MCP en utilisant le transport **stdio** actuel (approche recommandée).
- Comprendre pourquoi le transport SSE a été déprécié au profit de stdio et HTTP Streamable.
- Créer des outils pouvant être appelés par des clients MCP.
- Déboguer votre serveur en utilisant l'Inspector MCP.
- Intégrer votre serveur stdio à VS Code et Claude.

Le transport stdio offre une méthode plus simple, plus sécurisée et plus performante pour construire des serveurs MCP par rapport à l'approche SSE dépréciée. C'est le transport recommandé pour la plupart des implémentations de serveurs MCP selon la spécification du 18 juin 2025.

### .NET

1. Créons d'abord quelques outils. Pour cela, nous allons créer un fichier *Tools.cs* avec le contenu suivant :

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercice : Tester votre serveur stdio

Maintenant que vous avez construit votre serveur stdio, testons-le pour nous assurer qu'il fonctionne correctement.

### Prérequis

1. Assurez-vous que l'Inspector MCP est installé :
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Votre code serveur doit être enregistré (par exemple, sous `server.py`).

### Tester avec l'Inspector

1. **Démarrez l'Inspector avec votre serveur** :
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ouvrez l'interface web** : L'Inspector ouvrira une fenêtre de navigateur affichant les capacités de votre serveur.

3. **Testez les outils** : 
   - Essayez l'outil `get_greeting` avec différents noms.
   - Testez l'outil `calculate_sum` avec divers nombres.
   - Appelez l'outil `get_server_info` pour voir les métadonnées du serveur.

4. **Surveillez la communication** : L'Inspector montre les messages JSON-RPC échangés entre le client et le serveur.

### Ce que vous devriez voir

Lorsque votre serveur démarre correctement, vous devriez voir :
- Les capacités du serveur listées dans l'Inspector.
- Les outils disponibles pour les tests.
- Des échanges de messages JSON-RPC réussis.
- Les réponses des outils affichées dans l'interface.

### Problèmes courants et solutions

**Le serveur ne démarre pas :**
- Vérifiez que toutes les dépendances sont installées : `pip install mcp`.
- Vérifiez la syntaxe Python et l'indentation.
- Recherchez les messages d'erreur dans la console.

**Les outils n'apparaissent pas :**
- Assurez-vous que les décorateurs `@server.tool()` sont présents.
- Vérifiez que les fonctions des outils sont définies avant `main()`.
- Assurez-vous que le serveur est correctement configuré.

**Problèmes de connexion :**
- Assurez-vous que le serveur utilise correctement le transport stdio.
- Vérifiez qu'aucun autre processus n'interfère.
- Vérifiez la syntaxe de la commande Inspector.

## Devoir

Essayez d'ajouter plus de fonctionnalités à votre serveur. Consultez [cette page](https://api.chucknorris.io/) pour, par exemple, ajouter un outil qui appelle une API. Vous décidez de l'apparence du serveur. Amusez-vous :)

## Solution

[Solution](./solution/README.md) Voici une solution possible avec du code fonctionnel.

## Points clés

Les points clés de ce chapitre sont les suivants :

- Le transport stdio est le mécanisme recommandé pour les serveurs MCP locaux.
- Le transport stdio permet une communication fluide entre les serveurs MCP et les clients en utilisant les flux d'entrée et de sortie standard.
- Vous pouvez utiliser l'Inspector et Visual Studio Code pour consommer directement les serveurs stdio, ce qui facilite le débogage et l'intégration.

## Exemples 

- [Calculatrice Java](../samples/java/calculator/README.md)
- [Calculatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculatrice JavaScript](../samples/javascript/README.md)
- [Calculatrice TypeScript](../samples/typescript/README.md)
- [Calculatrice Python](../../../../03-GettingStarted/samples/python) 

## Ressources supplémentaires

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Et après

## Prochaines étapes

Maintenant que vous avez appris à construire des serveurs MCP avec le transport stdio, vous pouvez explorer des sujets plus avancés :

- **Suivant** : [Streaming HTTP avec MCP (HTTP Streamable)](../06-http-streaming/README.md) - Découvrez l'autre mécanisme de transport pris en charge pour les serveurs distants.
- **Avancé** : [Meilleures pratiques de sécurité MCP](../../02-Security/README.md) - Implémentez la sécurité dans vos serveurs MCP.
- **Production** : [Stratégies de déploiement](../09-deployment/README.md) - Déployez vos serveurs pour une utilisation en production.

## Ressources supplémentaires

- [Spécification MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Spécification officielle.
- [Documentation SDK MCP](https://github.com/modelcontextprotocol/sdk) - Références SDK pour tous les langages.
- [Exemples communautaires](../../06-CommunityContributions/README.md) - Plus d'exemples de serveurs de la communauté.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.