# Serveur MCP avec transport stdio

> **⚠️ Mise à jour importante** : À partir de la spécification MCP 2025-06-18, le transport SSE autonome (Server-Sent Events) a été **abandonné** et remplacé par le transport "HTTP Streamable". La spécification MCP actuelle définit deux mécanismes de transport principaux :
> 1. **stdio** - Entrée/sortie standard (recommandé pour les serveurs locaux)
> 2. **HTTP Streamable** - Pour les serveurs distants pouvant utiliser SSE en interne
>
> Cette leçon a été mise à jour pour se concentrer sur le **transport stdio**, qui est l'approche recommandée pour la plupart des implémentations de serveurs MCP.

Le transport stdio permet aux serveurs MCP de communiquer avec les clients via les flux d'entrée et sortie standard. C'est le mécanisme de transport le plus couramment utilisé et recommandé dans la spécification MCP actuelle, offrant une façon simple et efficace de construire des serveurs MCP pouvant être facilement intégrés avec diverses applications clientes.

## Aperçu

Cette leçon explique comment construire et consommer des serveurs MCP utilisant le transport stdio.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Construire un serveur MCP utilisant le transport stdio.
- Déboguer un serveur MCP avec l’Inspector.
- Consommer un serveur MCP via Visual Studio Code.
- Comprendre les mécanismes de transport MCP actuels et pourquoi stdio est recommandé.

## Transport stdio - Comment ça marche

Le transport stdio est l’un des deux types de transport pris en charge dans la spécification MCP actuelle (2025-06-18). Voici comment cela fonctionne :

- **Communication simple** : le serveur lit les messages JSON-RPC depuis l’entrée standard (`stdin`) et envoie des messages à la sortie standard (`stdout`).
- **Basé sur un processus** : le client lance le serveur MCP comme un sous-processus.
- **Format des messages** : les messages sont des requêtes, notifications ou réponses JSON-RPC individuelles, délimitées par des retours à la ligne.
- **Journalisation** : le serveur PEUT écrire des chaînes UTF-8 dans l’erreur standard (`stderr`) pour les logs.

### Exigences clés :
- Les messages DOIVENT être délimités par des retours à la ligne et NE DOIVENT PAS contenir de retours à la ligne intégrés
- Le serveur NE DOIT PAS écrire quoi que ce soit sur `stdout` qui ne soit pas un message MCP valide
- Le client NE DOIT PAS écrire quoi que ce soit sur le `stdin` du serveur qui ne soit pas un message MCP valide

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

- Nous importons la classe `Server` et `StdioServerTransport` du SDK MCP
- Nous créons une instance de serveur avec une configuration et des capacités basiques

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Créer une instance de serveur
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

Dans le code précédent nous :

- Créons une instance de serveur avec le SDK MCP
- Définit les outils à l’aide de décorateurs
- Utilisons le gestionnaire de contexte stdio_server pour gérer le transport

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

La différence clé avec SSE est que les serveurs stdio :

- Ne nécessitent pas de configuration de serveur web ni de points d’accès HTTP
- Sont lancés comme sous-processus par le client
- Communiquent via les flux stdin/stdout
- Sont plus simples à implémenter et à déboguer

## Exercice : Créer un serveur stdio

Pour créer notre serveur, il faut garder deux choses à l’esprit :

- Nous devons utiliser un serveur web pour exposer les points d’accès pour la connexion et les messages.

## Laboratoire : Créer un serveur MCP simple avec stdio

Dans ce laboratoire, nous allons créer un serveur MCP simple utilisant le transport stdio recommandé. Ce serveur exposera des outils que les clients pourront appeler via le protocole Model Context standard.

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

# Configurer la journalisation
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Créer le serveur
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
    # Utiliser le transport stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Différences clés avec l’ancienne approche SSE

**Transport Stdio (standard actuel) :**
- Modèle simple de sous-processus - le client lance le serveur comme processus enfant
- Communication via stdin/stdout en utilisant des messages JSON-RPC
- Pas besoin d’installer un serveur HTTP
- Meilleure performance et sécurité
- Débogage et développement facilités

**Transport SSE (abandonné depuis MCP 2025-06-18) :**
- Requiert un serveur HTTP avec points d’accès SSE
- Mise en place plus complexe avec infrastructure serveur web
- Considérations de sécurité supplémentaires pour les points HTTP
- Maintenant remplacé par HTTP Streamable pour les scénarios web

### Créer un serveur avec le transport stdio

Pour créer notre serveur stdio, nous devons :

1. **Importer les bibliothèques requises** - composants serveur MCP et transport stdio
2. **Créer une instance serveur** - définir le serveur avec ses capacités
3. **Définir les outils** - ajouter la fonctionnalité à exposer
4. **Configurer le transport** - configurer la communication stdio
5. **Lancer le serveur** - démarrer le serveur et gérer les messages

Construisons cela étape par étape :

### Étape 1 : Créer un serveur stdio basique

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configurer la journalisation
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Créer le serveur
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

### Étape 2 : Ajouter plus d’outils

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

### Étape 3 : Lancer le serveur

Enregistrez le code sous `server.py` et lancez-le depuis la ligne de commande :

```bash
python server.py
```

Le serveur démarrera et attendra les entrées depuis stdin. Il communique via des messages JSON-RPC sur le transport stdio.

### Étape 4 : Test avec l’Inspector

Vous pouvez tester votre serveur avec l’Inspector MCP :

1. Installez l’Inspector : `npx @modelcontextprotocol/inspector`
2. Lancez l’Inspector et connectez-le à votre serveur
3. Testez les outils que vous avez créés

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Déboguer votre serveur stdio

### Avec le MCP Inspector

Le MCP Inspector est un outil précieux pour le débogage et le test des serveurs MCP. Voici comment l’utiliser avec votre serveur stdio :

1. **Installer l’Inspector** :
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Lancer l’Inspector** :
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Tester votre serveur** : L’Inspector offre une interface web où vous pouvez :
   - Voir les capacités du serveur
   - Tester les outils avec différents paramètres
   - Surveiller les messages JSON-RPC
   - Déboguer les problèmes de connexion

### Avec VS Code

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

2. Placez des points d’arrêt dans le code serveur
3. Lancez le débogueur et testez avec l’Inspector

### Conseils courants de débogage

- Utilisez `stderr` pour la journalisation – ne jamais écrire sur `stdout` qui est réservé aux messages MCP
- Assurez-vous que tous les messages JSON-RPC sont délimités par des retours à la ligne
- Testez d’abord avec des outils simples avant d’ajouter des fonctionnalités complexes
- Utilisez l’Inspector pour vérifier le format des messages

## Consommer votre serveur stdio dans VS Code

Une fois votre serveur MCP stdio construit, vous pouvez l’intégrer à VS Code pour l’utiliser avec Claude ou d’autres clients compatibles MCP.

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

2. **Redémarrez Claude** : fermez et rouvrez Claude pour charger la nouvelle configuration du serveur.

3. **Testez la connexion** : démarrez une conversation avec Claude et essayez vos outils serveur :
   - "Peux-tu me saluer en utilisant l’outil de salutation ?"
   - "Calcule la somme de 15 et 27"
   - "Quelles sont les infos du serveur ?"

### Exemple de serveur stdio TypeScript

Voici un exemple complet en TypeScript à titre de référence :

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

// Ajouter des outils
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

### Exemple de serveur stdio .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Résumé

Dans cette leçon mise à jour, vous avez appris à :

- Construire des serveurs MCP avec le transport **stdio** actuel (approche recommandée)
- Comprendre pourquoi le transport SSE a été déprécié au profit de stdio et HTTP Streamable
- Créer des outils appelables par des clients MCP
- Déboguer votre serveur avec MCP Inspector
- Intégrer votre serveur stdio avec VS Code et Claude

Le transport stdio offre une façon plus simple, sécurisée et performante de construire des serveurs MCP par rapport à l’approche SSE abandonnée. C’est le transport recommandé pour la plupart des implémentations serveur MCP depuis la spécification du 2025-06-18.

### .NET

1. Créons d’abord quelques outils, pour cela nous allons créer un fichier *Tools.cs* avec le contenu suivant :

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercice : Tester votre serveur stdio

Maintenant que vous avez construit votre serveur stdio, testons-le pour s’assurer qu’il fonctionne correctement.

### Prérequis

1. Assurez-vous d’avoir installé MCP Inspector :
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Votre code serveur doit être sauvegardé (ex. `server.py`)

### Test avec l’Inspector

1. **Démarrez l’Inspector avec votre serveur** :
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ouvrez l’interface web** : l’Inspector ouvrira une fenêtre dans le navigateur affichant les capacités de votre serveur.

3. **Testez les outils** :
   - Essayez l’outil `get_greeting` avec différents noms
   - Testez l’outil `calculate_sum` avec plusieurs nombres
   - Appelez l’outil `get_server_info` pour voir les métadonnées du serveur

4. **Surveillez la communication** : L’Inspector montre les messages JSON-RPC échangés entre client et serveur.

### Ce que vous devriez voir

Quand votre serveur démarre bien, vous devriez voir :
- Les capacités du serveur listées dans l’Inspector
- Les outils disponibles pour les tests
- Des échanges de messages JSON-RPC réussis
- Les réponses des outils affichées dans l’interface

### Problèmes courants et solutions

**Le serveur ne démarre pas :**
- Vérifiez que toutes les dépendances sont installées : `pip install mcp`
- Vérifiez la syntaxe et l’indentation Python
- Cherchez des messages d’erreur dans la console

**Outils n’apparaissant pas :**
- Assurez-vous que les décorateurs `@server.tool()` sont présents
- Vérifiez que les fonctions outils sont définies avant `main()`
- Assurez-vous que le serveur est bien configuré

**Problèmes de connexion :**
- Vérifiez que le serveur utilise correctement le transport stdio
- Assurez-vous qu’aucun autre processus n’interfère
- Vérifiez la syntaxe de la commande Inspector

## Devoir

Essayez d’ajouter plus de capacités à votre serveur. Consultez [cette page](https://api.chucknorris.io/) pour, par exemple, ajouter un outil qui appelle une API. C’est vous qui décidez de l’apparence du serveur. Amusez-vous :)

## Solution

[Solution](./solution/README.md) Voici une solution possible avec un code fonctionnel.

## Points clés à retenir

Les points clés de ce chapitre sont les suivants :

- Le transport stdio est le mécanisme recommandé pour les serveurs MCP locaux.
- Le transport stdio permet une communication fluide entre serveurs MCP et clients en utilisant les flux standard d’entrée et sortie.
- Vous pouvez utiliser à la fois Inspector et Visual Studio Code pour consommer directement les serveurs stdio, ce qui rend le débogage et l’intégration simples.

## Échantillons 

- [Calculatrice Java](../samples/java/calculator/README.md)
- [Calculatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculatrice JavaScript](../samples/javascript/README.md)
- [Calculatrice TypeScript](../samples/typescript/README.md)
- [Calculatrice Python](../../../../03-GettingStarted/samples/python) 

## Ressources supplémentaires

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Et ensuite

## Prochaines étapes

Maintenant que vous savez construire des serveurs MCP avec le transport stdio, vous pouvez explorer des sujets plus avancés :

- **Suivant** : [Streaming HTTP avec MCP (HTTP Streamable)](../06-http-streaming/README.md) - Découvrez l’autre mécanisme de transport supporté pour les serveurs distants
- **Avancé** : [Bonnes pratiques de sécurité MCP](../../02-Security/README.md) - Implémentez la sécurité dans vos serveurs MCP
- **Production** : [Stratégies de déploiement](../09-deployment/README.md) - Déployez vos serveurs en production

## Ressources additionnelles

- [Spécification MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Spécification officielle
- [Documentation SDK MCP](https://github.com/modelcontextprotocol/sdk) - Références SDK pour tous les langages
- [Exemples communautaires](../../06-CommunityContributions/README.md) - Plus d’exemples de serveurs issus de la communauté

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->