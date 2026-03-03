# Création d'un client

Les clients sont des applications ou scripts personnalisés qui communiquent directement avec un serveur MCP pour demander des ressources, outils et invites. Contrairement à l'utilisation de l'outil inspecteur, qui fournit une interface graphique pour interagir avec le serveur, écrire votre propre client permet des interactions programmatiques et automatisées. Cela permet aux développeurs d'intégrer les capacités MCP dans leurs propres flux de travail, d'automatiser des tâches et de créer des solutions personnalisées adaptées à des besoins spécifiques.

## Vue d'ensemble

Cette leçon introduit le concept de clients dans l'écosystème du Model Context Protocol (MCP). Vous apprendrez à écrire votre propre client et à le connecter à un serveur MCP.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Comprendre ce qu'un client peut faire.
- Écrire votre propre client.
- Connecter et tester le client avec un serveur MCP pour s'assurer que ce dernier fonctionne comme prévu.

## Que faut-il pour écrire un client ?

Pour écrire un client, vous devrez faire ce qui suit :

- **Importer les bonnes bibliothèques**. Vous utiliserez la même bibliothèque que précédemment, juste des constructions différentes.
- **Instancier un client**. Cela impliquera de créer une instance de client et de la connecter à la méthode de transport choisie.
- **Décider des ressources à lister**. Votre serveur MCP propose des ressources, outils et invites, vous devez décider lesquels lister.
- **Intégrer le client à une application hôte**. Une fois que vous connaissez les capacités du serveur, vous devez intégrer cela dans votre application hôte afin que lorsqu'un utilisateur saisit une invite ou une autre commande, la fonction serveur correspondante soit invoquée.

Maintenant que nous comprenons globalement ce que nous allons faire, regardons un exemple.

### Un exemple de client

Jetons un œil à ce client d'exemple :

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// Lister les invites
const prompts = await client.listPrompts();

// Obtenir une invite
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Lister les ressources
const resources = await client.listResources();

// Lire une ressource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Appeler un outil
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Dans le code précédent, nous avons :

- Importé les bibliothèques
- Créé une instance de client et l'avons connecté en utilisant stdio comme transport.
- Listé les invites, ressources et outils et les avons tous invoqués.

Voilà un client capable de communiquer avec un serveur MCP.

Prenons le temps dans la section d'exercice suivante de décortiquer chaque extrait de code et d'expliquer ce qui se passe.

## Exercice : Écrire un client

Comme dit précédemment, prenons le temps d'expliquer le code et surtout, n'hésitez pas à coder en même temps si vous le souhaitez.

### -1- Importer les bibliothèques

Importons les bibliothèques dont nous avons besoin, nous aurons besoin de références à un client et à notre protocole de transport choisi, stdio. stdio est un protocole pour les choses destinées à fonctionner sur votre machine locale. SSE est un autre protocole de transport que nous présenterons dans de futurs chapitres, mais c'est votre autre option. Pour l'instant, continuons avec stdio.

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

Pour Java, vous allez créer un client qui se connecte au serveur MCP de l'exercice précédent. En utilisant la même structure de projet Java Spring Boot de [Premiers pas avec MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), créez une nouvelle classe Java appelée `SDKClient` dans le dossier `src/main/java/com/microsoft/mcp/sample/client/` et ajoutez les imports suivants :

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

Vous devrez ajouter les dépendances suivantes à votre fichier `Cargo.toml`.

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

À partir de là, vous pouvez importer les bibliothèques nécessaires dans votre code client.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Passons à l'instanciation.

### -2- Instanciation du client et du transport

Nous devons créer une instance du transport et une de notre client :

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

Dans le code précédent, nous avons :

- Créé une instance de transport stdio. Notez comment il spécifie la commande et les arguments pour trouver et démarrer le serveur car c’est quelque chose que nous devrons faire en créant le client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instancié un client en lui donnant un nom et une version.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Connecté le client au transport choisi.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Créer les paramètres du serveur pour la connexion stdio
server_params = StdioServerParameters(
    command="mcp",  # Exécutable
    args=["run", "server.py"],  # Arguments de ligne de commande optionnels
    env=None,  # Variables d'environnement optionnelles
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialiser la connexion
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Dans le code précédent, nous avons :

- Importé les bibliothèques nécessaires
- Instancié un objet paramètres serveur que nous utiliserons pour lancer le serveur afin de pouvoir nous y connecter avec notre client.
- Défini une méthode `run` qui appelle à son tour `stdio_client` qui lance une session client.
- Créé un point d'entrée où nous fournissons la méthode `run` à `asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

Dans le code précédent, nous avons :

- Importé les bibliothèques nécessaires.
- Créé un transport stdio et un client `mcpClient`. Ce dernier sert à lister et invoquer les fonctionnalités sur le serveur MCP.

Notez que dans "Arguments", vous pouvez soit pointer vers le fichier *.csproj* soit vers l'exécutable.

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // Votre logique client va ici
    }
}
```

Dans le code précédent, nous avons :

- Créé une méthode main qui configure un transport SSE pointant vers `http://localhost:8080` où notre serveur MCP sera en fonctionnement.
- Créé une classe client qui prend le transport en paramètre du constructeur.
- Dans la méthode `run`, nous créons un client MCP synchronisé utilisant le transport et initialisons la connexion.
- Utilisé le transport SSE (Server-Sent Events) qui convient à la communication HTTP avec les serveurs MCP Java Spring Boot.

#### Rust

Notez que ce client Rust suppose que le serveur est un projet frère nommé "calculator-server" dans le même répertoire. Le code ci-dessous démarrera le serveur et se connectera à lui.

```rust
async fn main() -> Result<(), RmcpError> {
    // Supposer que le serveur est un projet frère nommé "calculator-server" dans le même répertoire
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // À FAIRE : Initialiser

    // À FAIRE : Lister les outils

    // À FAIRE : Appeler l'outil add avec les arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Lister les fonctionnalités du serveur

Maintenant, nous avons un client capable de se connecter si le programme est exécuté. Cependant, il ne liste pas encore ses fonctionnalités, faisons-le maintenant :

#### TypeScript

```typescript
// Lister les invites
const prompts = await client.listPrompts();

// Lister les ressources
const resources = await client.listResources();

// lister les outils
const tools = await client.listTools();
```

#### Python

```python
# Lister les ressources disponibles
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Lister les outils disponibles
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Ici, nous listons les ressources disponibles, `list_resources()` et les outils, `list_tools` et les affichons.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ci-dessus un exemple de comment lister les outils sur le serveur. Pour chaque outil, nous affichons ensuite son nom.

#### Java

```java
// Liste et démonstration des outils
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Vous pouvez également pinguer le serveur pour vérifier la connexion
client.ping();
```

Dans le code précédent, nous avons :

- Appelé `listTools()` pour obtenir tous les outils disponibles du serveur MCP.
- Utilisé `ping()` pour vérifier que la connexion au serveur fonctionne.
- Le `ListToolsResult` contient des informations sur tous les outils, y compris leurs noms, descriptions et schémas d'entrée.

Parfait, maintenant nous avons capturé toutes les fonctionnalités. À quand les utiliser ? Eh bien, ce client est assez simple, simple dans le sens où nous devrons appeler explicitement les fonctionnalités quand nous les voulons. Dans le chapitre suivant, nous créerons un client plus avancé qui aura accès à son propre modèle de langage large, LLM. Pour l'instant, voyons comment invoquer les fonctionnalités sur le serveur :

#### Rust

Dans la fonction main, après avoir initialisé le client, nous pouvons initialiser le serveur et lister quelques-unes de ses fonctionnalités.

```rust
// Initialiser
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Lister les outils
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocation des fonctionnalités

Pour invoquer les fonctionnalités, il faut s'assurer de spécifier les bons arguments et dans certains cas le nom de ce que nous essayons d'invoquer.

#### TypeScript

```typescript

// Lire une ressource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Appeler un outil
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// appeler une invite
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Dans le code précédent, nous avons :

- Lu une ressource, nous appelons la ressource en appelant `readResource()` en spécifiant `uri`. Voici ce que cela ressemble probablement côté serveur :

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    Notre valeur `uri` `file://example.txt` correspond à `file://{name}` sur le serveur. `example.txt` sera mappé à `name`.

- Appelé un outil, nous l'appelons en spécifiant son `name` et ses `arguments` ainsi :

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Obtenu une invite, pour obtenir une invite, vous appelez `getPrompt()` avec `name` et `arguments`. Le code serveur ressemble à ceci :

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    et votre code client résultant ressemble donc à ceci pour correspondre à ce qui est déclaré côté serveur :

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# Lire une ressource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Appeler un outil
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Dans le code précédent, nous avons :

- Appelé une ressource appelée `greeting` en utilisant `read_resource`.
- Invoqué un outil appelé `add` en utilisant `call_tool`.

#### .NET

1. Ajoutons du code pour appeler un outil :

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Pour afficher le résultat, voici un code pour gérer cela :

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Appeler divers outils de calculatrice
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

Dans le code précédent, nous avons :

- Appelé plusieurs outils calculatrice en utilisant la méthode `callTool()` avec des objets `CallToolRequest`.
- Chaque appel d'outil spécifie le nom de l'outil et une `Map` des arguments requis par cet outil.
- Les outils du serveur attendent des noms de paramètres spécifiques (comme "a", "b" pour des opérations mathématiques).
- Les résultats sont retournés sous forme d'objets `CallToolResult` contenant la réponse du serveur.

#### Rust

```rust
// Appeler l'outil add avec les arguments = {"a": 3, "b": 2}
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- Exécuter le client

Pour exécuter le client, tapez la commande suivante dans le terminal :

#### TypeScript

Ajoutez l'entrée suivante à votre section "scripts" dans *package.json* :

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Appelez le client avec la commande suivante :

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Assurez-vous d'abord que votre serveur MCP fonctionne sur `http://localhost:8080`. Ensuite, lancez le client :

```bash
# Construisez votre projet
./mvnw clean compile

# Exécutez le client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Vous pouvez également exécuter le projet client complet fourni dans le dossier solution `03-GettingStarted\02-client\solution\java` :

```bash
# Naviguer vers le répertoire de la solution
cd 03-GettingStarted/02-client/solution/java

# Construire et exécuter le JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Exercice

Dans cet exercice, vous allez utiliser ce que vous avez appris pour créer un client, mais créez un client de votre cru.

Voici un serveur que vous pouvez utiliser et auquel vous devez accéder via votre code client, voyez si vous pouvez ajouter plus de fonctionnalités au serveur pour le rendre plus intéressant.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Créer un serveur MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Ajouter un outil d'addition
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Ajouter une ressource de salutation dynamique
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Commencer à recevoir des messages sur stdin et à envoyer des messages sur stdout

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Créer un serveur MCP
mcp = FastMCP("Demo")


# Ajouter un outil d'addition
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Ajouter une ressource de salutation dynamique
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

Consultez ce projet pour voir comment vous pouvez [ajouter des invites et des ressources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Consultez aussi ce lien pour savoir comment invoquer [invites et ressources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Dans la [section précédente](../../../../03-GettingStarted/01-first-server), vous avez appris à créer un serveur MCP simple avec Rust. Vous pouvez continuer à construire dessus ou consulter ce lien pour davantage d'exemples de serveurs MCP basés sur Rust : [Exemples MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solution

Le **dossier solution** contient des implémentations complètes et prêtes à l’emploi de clients qui démontrent tous les concepts abordés dans ce tutoriel. Chaque solution inclut à la fois le code client et serveur organisés en projets distincts et autonomes.

### 📁 Structure de la solution

Le répertoire de la solution est organisé par langage de programmation :

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 Ce que chaque solution inclut

Chaque solution spécifique au langage fournit :

- **Implémentation complète du client** avec toutes les fonctionnalités du tutoriel
- **Structure du projet fonctionnelle** avec les dépendances et configurations appropriées
- **Scripts de build et d’exécution** pour une installation et un lancement faciles
- **README détaillé** avec instructions spécifiques au langage
- **Gestion des erreurs** et exemples de traitement des résultats

### 📖 Utilisation des solutions

1. **Naviguez vers votre dossier de langage préféré** :

   ```bash
   cd solution/typescript/    # Pour TypeScript
   cd solution/java/          # Pour Java
   cd solution/python/        # Pour Python
   cd solution/dotnet/        # Pour .NET
   ```

2. **Suivez les instructions du README** dans chaque dossier pour :
   - Installer les dépendances
   - Compiler le projet
   - Lancer le client

3. **Sortie exemple** que vous devriez voir :

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pour une documentation complète et des instructions pas à pas, consultez : **[📖 Documentation de la solution](./solution/README.md)**

## 🎯 Exemples complets

Nous avons fourni des implémentations client complètes et fonctionnelles pour tous les langages de programmation couverts dans ce tutoriel. Ces exemples démontrent toute la fonctionnalité décrite ci-dessus et peuvent être utilisés comme références ou points de départ pour vos propres projets.

### Exemples complets disponibles

| Langage | Fichier | Description |
|---------|---------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Client Java complet utilisant le transport SSE avec gestion complète des erreurs |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Client C# complet utilisant le transport stdio avec démarrage automatique du serveur |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Client TypeScript complet avec support total du protocole MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Client Python complet utilisant les patterns async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Client Rust complet utilisant Tokio pour les opérations asynchrones |

Chaque exemple complet inclut :
- ✅ **Établissement de la connexion** et gestion des erreurs  
- ✅ **Découverte du serveur** (outils, ressources, invites lorsque applicable)  
- ✅ **Opérations calculatrices** (addition, soustraction, multiplication, division, aide)  
- ✅ **Traitement des résultats** et sortie formatée  
- ✅ **Gestion complète des erreurs**  
- ✅ **Code propre et documenté** avec des commentaires étape par étape  

### Démarrage avec des exemples complets

1. **Choisissez votre langue préférée** dans le tableau ci-dessus  
2. **Consultez le fichier d'exemple complet** pour comprendre l'implémentation complète  
3. **Exécutez l'exemple** en suivant les instructions dans [`complete_examples.md`](./complete_examples.md)  
4. **Modifiez et étendez** l'exemple selon votre cas d'usage spécifique  

Pour une documentation détaillée sur l'exécution et la personnalisation de ces exemples, voir : **[📖 Documentation des exemples complets](./complete_examples.md)**  

### 💡 Solution vs. Exemples complets  

| **Dossier Solution**       | **Exemples Complets**    |  
|---------------------------|--------------------------|  
| Structure complète du projet avec fichiers de build | Implémentations en fichier unique |  
| Prêt à l'emploi avec dépendances | Exemples de code ciblés |  
| Configuration proche de la production | Référence pédagogique |  
| Outils spécifiques au langage | Comparaison inter-langages |  

Les deux approches sont précieuses - utilisez le **dossier solution** pour des projets complets et les **exemples complets** pour l'apprentissage et la référence.  

## Points clés à retenir  

Les points clés de ce chapitre à propos des clients :  

- Peuvent être utilisés à la fois pour découvrir et invoquer des fonctionnalités sur le serveur.  
- Peuvent démarrer un serveur pendant qu'ils démarrent eux-mêmes (comme dans ce chapitre) mais les clients peuvent également se connecter à des serveurs déjà en fonctionnement.  
- Sont un excellent moyen de tester les capacités du serveur à côté d'alternatives comme l'Inspecteur, comme décrit dans le chapitre précédent.  

## Ressources supplémentaires  

- [Création de clients dans MCP](https://modelcontextprotocol.io/quickstart/client)  

## Exemples  

- [Calculatrice Java](../samples/java/calculator/README.md)  
- [Calculatrice .Net](../../../../03-GettingStarted/samples/csharp)  
- [Calculatrice JavaScript](../samples/javascript/README.md)  
- [Calculatrice TypeScript](../samples/typescript/README.md)  
- [Calculatrice Python](../../../../03-GettingStarted/samples/python)  
- [Calculatrice Rust](../../../../03-GettingStarted/samples/rust)  

## Et ensuite  

- Suivant : [Création d'un client avec un LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->