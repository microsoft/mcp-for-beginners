# Création d'un client avec LLM

Jusqu'à présent, vous avez vu comment créer un serveur et un client. Le client a pu appeler explicitement le serveur pour lister ses outils, ressources et invites. Cependant, ce n'est pas une approche très pratique. Votre utilisateur vit à l'ère agentique et s'attend à utiliser des invites et à communiquer avec un LLM pour ce faire. Pour votre utilisateur, peu importe si vous utilisez MCP ou non pour stocker vos capacités, mais il s'attend à utiliser le langage naturel pour interagir. Alors, comment résoudre cela ? La solution consiste à ajouter un LLM au client.

## Vue d'ensemble

Dans cette leçon, nous nous concentrons sur l'ajout d'un LLM à votre client et montrons comment cela offre une bien meilleure expérience pour votre utilisateur.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Créer un client avec un LLM.
- Interagir de manière fluide avec un serveur MCP en utilisant un LLM.
- Offrir une meilleure expérience utilisateur côté client.

## Approche

Essayons de comprendre l'approche que nous devons adopter. Ajouter un LLM semble simple, mais allons-nous vraiment le faire ?

Voici comment le client interagira avec le serveur :

1. Établir la connexion avec le serveur.

1. Lister les capacités, invites, ressources et outils, et enregistrer leur schéma.

1. Ajouter un LLM et passer les capacités enregistrées ainsi que leur schéma dans un format que le LLM comprend.

1. Gérer une invite utilisateur en la passant au LLM avec les outils listés par le client.

Parfait, maintenant que nous comprenons comment faire cela à un niveau élevé, essayons dans l'exercice ci-dessous.

## Exercice : Créer un client avec un LLM

Dans cet exercice, nous allons apprendre à ajouter un LLM à notre client.

### Authentification avec un jeton d'accès personnel GitHub

Créer un jeton GitHub est un processus simple. Voici comment faire :

- Allez dans Paramètres GitHub – Cliquez sur votre photo de profil en haut à droite et sélectionnez Paramètres.
- Naviguez vers Paramètres développeur – Faites défiler vers le bas et cliquez sur Paramètres développeur.
- Sélectionnez Jetons d'accès personnel – Cliquez sur Jetons à granularité fine puis Générer un nouveau jeton.
- Configurez votre jeton – Ajoutez une note pour référence, définissez une date d'expiration et sélectionnez les portées nécessaires (autorisations). Dans ce cas, assurez-vous d'ajouter l'autorisation Models.
- Générez et copiez le jeton – Cliquez sur Générer le jeton, et assurez-vous de le copier immédiatement, car vous ne pourrez plus le voir.

### -1- Connexion au serveur

Créons d'abord notre client :

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importer zod pour la validation de schéma

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", 
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }
}
```

Dans le code précédent, nous avons :

- Importé les bibliothèques nécessaires
- Créé une classe avec deux membres, `client` et `openai` qui nous aideront respectivement à gérer un client et à interagir avec un LLM.
- Configuré notre instance LLM pour utiliser les modèles GitHub en définissant `baseUrl` pour pointer vers l'API d'inférence.

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

- Importé les bibliothèques nécessaires pour MCP
- Créé un client

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

Tout d'abord, vous devez ajouter les dépendances LangChain4j à votre fichier `pom.xml`. Ajoutez ces dépendances pour activer l'intégration MCP et le support des modèles GitHub :

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- LangChain4j MCP Integration -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-mcp</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- OpenAI Official API Client -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai-official</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- GitHub Models Support -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-github-models</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

Puis créez votre classe client Java :

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // Configurer le LLM pour utiliser les modèles GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Créer un transport MCP pour se connecter au serveur
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Créer un client MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Dans le code précédent, nous avons :

- **Ajouté les dépendances LangChain4j** : nécessaires pour l'intégration MCP, le client officiel OpenAI, et le support des modèles GitHub
- **Importé les bibliothèques LangChain4j** : pour l'intégration MCP et la fonctionnalité du modèle de chat OpenAI
- **Créé un `ChatLanguageModel`** : configuré pour utiliser les modèles GitHub avec votre jeton GitHub
- **Configuré le transport HTTP** : en utilisant Server-Sent Events (SSE) pour se connecter au serveur MCP
- **Créé un client MCP** : qui gérera la communication avec le serveur
- **Utilisé le support MCP intégré de LangChain4j** : qui simplifie l'intégration entre les LLM et les serveurs MCP

#### Rust

Cet exemple suppose que vous avez un serveur MCP basé sur Rust en fonctionnement. Si vous n'en avez pas, référez-vous à la leçon [01-first-server](../01-first-server/README.md) pour créer le serveur.

Une fois que vous avez votre serveur MCP Rust, ouvrez un terminal et naviguez vers le même répertoire que le serveur. Ensuite, exécutez la commande suivante pour créer un nouveau projet client LLM :

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Ajoutez les dépendances suivantes à votre fichier `Cargo.toml` :

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Il n'existe pas de bibliothèque officielle Rust pour OpenAI, cependant, la crate `async-openai` est une [bibliothèque maintenue par la communauté](https://platform.openai.com/docs/libraries/rust#rust) qui est couramment utilisée.

Ouvrez le fichier `src/main.rs` et remplacez son contenu par le code suivant :

```rust
use async_openai::{Client, config::OpenAIConfig};
use rmcp::{
    RmcpError,
    model::{CallToolRequestParam, ListToolsResult},
    service::{RoleClient, RunningService, ServiceExt},
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use serde_json::{Value, json};
use std::error::Error;
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Message initial
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Configuration du client OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Configuration du client MCP
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("calculator-server");

    let mcp_client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // À FAIRE : Obtenir la liste des outils MCP

    // À FAIRE : Conversation LLM avec appels d'outils

    Ok(())
}
```

Ce code configure une application Rust basique qui se connectera à un serveur MCP et aux modèles GitHub pour les interactions LLM.

> [!IMPORTANT]
> Assurez-vous de définir la variable d'environnement `OPENAI_API_KEY` avec votre jeton GitHub avant d'exécuter l'application.

Parfait, pour notre prochaine étape, listons les capacités sur le serveur.

### -2- Lister les capacités du serveur

Nous allons maintenant nous connecter au serveur et demander ses capacités :

#### Typescript

Dans la même classe, ajoutez les méthodes suivantes :

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // outils de liste
    const toolsResult = await this.client.listTools();
}
```

Dans le code précédent, nous avons :

- Ajouté le code pour se connecter au serveur, `connectToServer`.
- Créé une méthode `run` responsable de gérer le flux de notre application. Jusqu'à présent, elle liste seulement les outils mais nous allons y ajouter plus bientôt.

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
    print("Tool", tool.inputSchema["properties"])
```

Voici ce que nous avons ajouté :

- Listé les ressources et outils et les avons affichés. Pour les outils, nous listons aussi `inputSchema` que nous utiliserons plus tard.

#### .NET

```csharp
async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        // TODO: convert tool definition from MCP tool to LLm tool     
    }

    return toolDefinitions;
}
```

Dans le code précédent, nous avons :

- Listé les outils disponibles sur le serveur MCP
- Pour chaque outil, listé le nom, la description et son schéma. Ce dernier est quelque chose que nous utiliserons pour appeler les outils bientôt.

#### Java

```java
// Créez un fournisseur d'outils qui découvre automatiquement les outils MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Le fournisseur d'outils MCP gère automatiquement :
// - La liste des outils disponibles depuis le serveur MCP
// - La conversion des schémas d'outils MCP au format LangChain4j
// - La gestion de l'exécution des outils et des réponses
```

Dans le code précédent, nous avons :

- Créé un `McpToolProvider` qui découvre automatiquement et enregistre tous les outils du serveur MCP
- Le fournisseur d'outils gère la conversion entre les schémas d'outils MCP et le format d'outil de LangChain4j en interne
- Cette approche abstrait le processus manuel de listing et de conversion des outils

#### Rust

La récupération des outils depuis le serveur MCP se fait via la méthode `list_tools`. Dans votre fonction `main`, après avoir configuré le client MCP, ajoutez le code suivant :

```rust
// Obtenir la liste des outils MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Convertir les capacités du serveur en outils LLM

L'étape suivante après avoir listé les capacités du serveur est de les convertir dans un format que le LLM comprend. Une fois cela fait, nous pouvons fournir ces capacités comme outils à notre LLM.

#### TypeScript

1. Ajoutez le code suivant pour convertir la réponse du serveur MCP en un format d'outil que le LLM peut utiliser :

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Créez un schéma zod basé sur le input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Définissez explicitement le type sur "function"
            function: {
            name: tool.name,
            description: tool.description,
            parameters: {
            type: "object",
            properties: tool.input_schema.properties,
            required: tool.input_schema.required,
            },
            },
        };
    }

    ```

    Le code ci-dessus prend une réponse du serveur MCP et la convertit en un format de définition d'outil que le LLM peut comprendre.

1. Mettons à jour la méthode `run` ensuite pour lister les capacités du serveur :

    ```typescript
    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
            });
        });
    }
    ```

    Dans le code précédent, nous avons mis à jour la méthode `run` pour parcourir le résultat et pour chaque entrée appeler `openAiToolAdapter`.

#### Python

1. D'abord, créons la fonction de conversion suivante

    ```python
    def convert_to_llm_tool(tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }

        return tool_schema
    ```

    Dans la fonction ci-dessus `convert_to_llm_tools`, nous prenons une réponse d'outil MCP et la convertissons en un format que le LLM peut comprendre.

1. Ensuite, mettons à jour notre code client pour utiliser cette fonction comme suit :

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Ici, nous ajoutons un appel à `convert_to_llm_tool` pour convertir la réponse d'outil MCP en quelque chose que nous pouvons fournir au LLM plus tard.

#### .NET

1. Ajoutons du code pour convertir la réponse d'outil MCP en quelque chose que le LLM peut comprendre

```csharp
ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}
```

Dans le code précédent, nous avons :

- Créé une fonction `ConvertFrom` qui prend le nom, la description et le schéma d'entrée.
- Défini une fonctionnalité qui crée une `FunctionDefinition` qui est passée à une `ChatCompletionsDefinition`. Cette dernière est quelque chose que le LLM peut comprendre.

1. Voyons comment nous pouvons mettre à jour un code existant pour profiter de cette fonction ci-dessus :

    ```csharp
    async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            JsonElement propertiesElement;
            tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

            var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);

            Console.WriteLine($"Properties: {propertiesElement}");        
        }

        return toolDefinitions;
    }
    ```    In the preceding code, we've:

    - Update the function to convert the MCP tool response to an LLm tool. Let's highlight the code we added:

        ```csharp
        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
        ```

        The input schema is part of the tool response but on the "properties" attribute, so we need to extract. Furthermore, we now call `ConvertFrom` with the tool details. Now we've done the heavy lifting, let's see how it call comes together as we handle a user prompt next.

#### Java

```java
// Créer une interface Bot pour l'interaction en langage naturel
public interface Bot {
    String chat(String prompt);
}

// Configurer le service IA avec les outils LLM et MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Dans le code précédent, nous avons :

- Défini une interface simple `Bot` pour les interactions en langage naturel
- Utilisé `AiServices` de LangChain4j pour lier automatiquement le LLM avec le fournisseur d'outils MCP
- Le framework gère automatiquement la conversion des schémas d'outils et l'appel des fonctions en arrière-plan
- Cette approche élimine la conversion manuelle des outils - LangChain4j gère toute la complexité de la conversion des outils MCP au format compatible LLM

#### Rust

Pour convertir la réponse d'outil MCP en un format que le LLM peut comprendre, nous allons ajouter une fonction d'aide qui formate la liste des outils. Ajoutez le code suivant à votre fichier `main.rs` sous la fonction `main`. Cela sera appelé lors des requêtes au LLM :

```rust
async fn format_tools(tools: &ListToolsResult) -> Result<Vec<Value>, Box<dyn Error>> {
    let tools_json = serde_json::to_value(tools)?;
    let Some(tools_array) = tools_json.get("tools").and_then(|t| t.as_array()) else {
        return Ok(vec![]);
    };

    let formatted_tools = tools_array
        .iter()
        .filter_map(|tool| {
            let name = tool.get("name")?.as_str()?;
            let description = tool.get("description")?.as_str()?;
            let schema = tool.get("inputSchema")?;

            Some(json!({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": schema.get("properties").unwrap_or(&json!({})),
                        "required": schema.get("required").unwrap_or(&json!([]))
                    }
                }
            }))
        })
        .collect();

    Ok(formatted_tools)
}
```

Parfait, nous sommes maintenant prêts à gérer les requêtes utilisateur, attaquons cela.

### -4- Gérer la requête d'invite utilisateur

Dans cette partie du code, nous allons gérer les requêtes utilisateur.

#### TypeScript

1. Ajoutez une méthode qui sera utilisée pour appeler notre LLM :

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Appeler l'outil du serveur
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Faire quelque chose avec le résultat
        // À FAIRE

        }
    }
    ```

    Dans le code précédent, nous avons :

    - Ajouté une méthode `callTools`.
    - La méthode prend une réponse LLM et vérifie quels outils ont été appelés, le cas échéant :

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // appeler l'outil
        }
        ```

    - Appelle un outil, si le LLM indique qu'il doit être appelé :

        ```typescript
        // 2. Appeler l'outil du serveur
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Faire quelque chose avec le résultat
        // À FAIRE
        ```

1. Mettez à jour la méthode `run` pour inclure les appels au LLM et appeler `callTools` :

    ```typescript

    // 1. Créez des messages qui sont l'entrée pour le LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Appeler le LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Parcourez la réponse du LLM, pour chaque choix, vérifiez s'il contient des appels d'outils
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Parfait, listons le code complet :

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importer zod pour la validation du schéma

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // pourrait devoir changer pour cette URL à l'avenir : https://models.github.ai/inference
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }

    async connectToServer(transport: Transport) {
        await this.client.connect(transport);
        this.run();
        console.error("MCPClient started on stdin/stdout");
    }

    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
          }) {
          // Créer un schéma zod basé sur le input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Définir explicitement le type sur "function"
            function: {
              name: tool.name,
              description: tool.description,
              parameters: {
              type: "object",
              properties: tool.input_schema.properties,
              required: tool.input_schema.required,
              },
            },
          };
    }
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. Appeler l'outil du serveur
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Faire quelque chose avec le résultat
          // À FAIRE
    
         }
    }

    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
              name: tool.name,
              description: tool.description,
              input_schema: tool.inputSchema,
            });
        });

        const prompt = "What is the sum of 2 and 3?";
    
        const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

        console.log("Querying LLM: ", messages[0].content);
        let response = this.openai.chat.completions.create({
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Parcourir la réponse LLM, pour chaque choix, vérifier s'il y a des appels d'outil
        (await response).choices.map(async (choice: { message: any; }) => {
          const message = choice.message;
          if (message.tool_calls) {
              console.log("Making tool call")
              await this.callTools(message.tool_calls, results);
          }
        });
    }
    
}

let client = new MyClient();
 const transport = new StdioClientTransport({
            command: "node",
            args: ["./build/index.js"]
        });

client.connectToServer(transport);
```

#### Python

1. Ajoutons quelques imports nécessaires pour appeler un LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Ensuite, ajoutons la fonction qui appellera le LLM :

    ```python
    # llm

    def call_llm(prompt, functions):
        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.inference.ai.azure.com"

        model_name = "gpt-4o"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        print("CALLING LLM")
        response = client.complete(
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant.",
                },
                {
                "role": "user",
                "content": prompt,
                },
            ],
            model=model_name,
            tools = functions,
            # Paramètres optionnels
            temperature=1.,
            max_tokens=1000,
            top_p=1.    
        )

        response_message = response.choices[0].message
        
        functions_to_call = []

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                print("TOOL: ", tool_call)
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                functions_to_call.append({ "name": name, "args": args })

        return functions_to_call
    ```

    Dans le code précédent, nous avons :

    - Passé nos fonctions, que nous avons trouvées sur le serveur MCP et converties, au LLM.
    - Puis appelé le LLM avec ces fonctions.
    - Ensuite, nous inspectons le résultat pour voir quelles fonctions nous devrions appeler, le cas échéant.
    - Enfin, nous passons un tableau de fonctions à appeler.

1. Dernière étape, mettons à jour notre code principal :

    ```python
    prompt = "Add 2 to 20"

    # demander au LLM quels outils utiliser, le cas échéant
    functions_to_call = call_llm(prompt, functions)

    # appeler les fonctions suggérées
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Voilà, c'était la dernière étape, dans le code ci-dessus nous :

    - Appelons un outil MCP via `call_tool` en utilisant une fonction que le LLM a estimé que nous devrions appeler en fonction de notre invite.
    - Affichons le résultat de l'appel d'outil au serveur MCP.

#### .NET

1. Montrons un peu de code pour faire une requête d'invite LLM :

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new ChatRequestUserMessage(userMessage));

    // 1. Define tools
    ChatCompletionsToolDefinition def = CreateToolDefinition();


    // 2. Define options, including the tools
    var options = new ChatCompletionsOptions(chatHistory)
    {
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    Dans le code précédent, nous avons :

    - Récupéré les outils du serveur MCP, `var tools = await GetMcpTools()`.
    - Défini une invite utilisateur `userMessage`.
    - Construit un objet options spécifiant le modèle et les outils.
    - Fait une requête vers le LLM.

1. Une dernière étape, voyons si le LLM pense que nous devrions appeler une fonction :

    ```csharp
    // 4. Check if the response contains a function call
    ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
        var result = await mcpClient.CallToolAsync(
            call.Name,
            dict!,
            cancellationToken: CancellationToken.None
        );

        Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

    }
    ```

    Dans le code précédent, nous avons :

    - Bouclé à travers une liste d'appels de fonctions.
    - Pour chaque appel d'outil, extrait le nom et les arguments et appelé l'outil sur le serveur MCP en utilisant le client MCP. Enfin, nous affichons les résultats.

Voici le code complet :

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var endpoint = "https://models.inference.ai.azure.com";
var token = Environment.GetEnvironmentVariable("GITHUB_TOKEN"); // Your GitHub Access Token
var client = new ChatCompletionsClient(new Uri(endpoint), new AzureKeyCredential(token));
var chatHistory = new List<ChatRequestMessage>
{
    new ChatRequestSystemMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}



async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);

        Console.WriteLine($"Properties: {propertiesElement}");        
    }

    return toolDefinitions;
}

// 1. List tools on mcp server

var tools = await GetMcpTools();
for (int i = 0; i < tools.Count; i++)
{
    var tool = tools[i];
    Console.WriteLine($"MCP Tools def: {i}: {tool}");
}

// 2. Define the chat history and the user message
var userMessage = "add 2 and 4";

chatHistory.Add(new ChatRequestUserMessage(userMessage));


// 3. Define options, including the tools
var options = new ChatCompletionsOptions(chatHistory)
{
    Model = "gpt-4o-mini",
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletions? response = await client.CompleteAsync(options);
var content = response.Content;

// 5. Check if the response contains a function call
ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
    var result = await mcpClient.CallToolAsync(
        call.Name,
        dict!,
        cancellationToken: CancellationToken.None
    );

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Exécuter des requêtes en langage naturel qui utilisent automatiquement les outils MCP
    String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
    System.out.println(response);

    response = bot.chat("What's the square root of 144?");
    System.out.println(response);

    response = bot.chat("Show me the help for the calculator service");
    System.out.println(response);
} finally {
    mcpClient.close();
}
```

Dans le code précédent, nous avons :

- Utilisé des invites en langage naturel simples pour interagir avec les outils du serveur MCP
- Le framework LangChain4j gère automatiquement :
  - La conversion des invites utilisateur en appels d'outils lorsque nécessaire
  - L'appel des outils MCP appropriés selon la décision du LLM
  - La gestion du flux de conversation entre le LLM et le serveur MCP
- La méthode `bot.chat()` retourne des réponses en langage naturel qui peuvent inclure les résultats des exécutions d'outils MCP
- Cette approche offre une expérience utilisateur fluide où les utilisateurs n'ont pas besoin de connaître l'implémentation MCP sous-jacente

Exemple de code complet :

```java
public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofSeconds(60))
                .build();

        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        Bot bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();

        try {
            String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
            System.out.println(response);

            response = bot.chat("What's the square root of 144?");
            System.out.println(response);

            response = bot.chat("Show me the help for the calculator service");
            System.out.println(response);
        } finally {
            mcpClient.close();
        }
    }
}
```

#### Rust

C'est ici que la majorité du travail se fait. Nous allons appeler le LLM avec l'invite utilisateur initiale, puis traiter la réponse pour voir si des outils doivent être appelés. Si oui, nous appellerons ces outils et continuerons la conversation avec le LLM jusqu'à ce qu'aucun autre appel d'outil ne soit nécessaire et que nous ayons une réponse finale.

Nous ferons plusieurs appels au LLM, définissons donc une fonction qui gérera l'appel au LLM. Ajoutez la fonction suivante à votre fichier `main.rs` :

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": "openai/gpt-4.1",
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

Cette fonction prend le client LLM, une liste de messages (y compris l'invite utilisateur), les outils du serveur MCP, et envoie une requête au LLM, retournant la réponse.
La réponse du LLM contiendra un tableau de `choices`. Nous devrons traiter le résultat pour voir si des `tool_calls` sont présents. Cela nous permet de savoir que le LLM demande qu’un outil spécifique soit appelé avec des arguments. Ajoutez le code suivant à la fin de votre fichier `main.rs` pour définir une fonction qui gère la réponse du LLM :

```rust
async fn process_llm_response(
    llm_response: &Value,
    mcp_client: &RunningService<RoleClient, ()>,
    openai_client: &Client<OpenAIConfig>,
    mcp_tools: &ListToolsResult,
    messages: &mut Vec<Value>,
) -> Result<(), Box<dyn Error>> {
    let Some(message) = llm_response
        .get("choices")
        .and_then(|c| c.as_array())
        .and_then(|choices| choices.first())
        .and_then(|choice| choice.get("message"))
    else {
        return Ok(());
    };

    // Imprimer le contenu si disponible
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Gérer les appels d'outil
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Ajouter un message d'assistant

        // Exécuter chaque appel d'outil
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Ajouter le résultat de l'outil aux messages
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continuer la conversation avec les résultats de l'outil
        let response = call_llm(openai_client, messages, mcp_tools).await?;
        Box::pin(process_llm_response(
            &response,
            mcp_client,
            openai_client,
            mcp_tools,
            messages,
        ))
        .await?;
    }
    Ok(())
}
```

Si des `tool_calls` sont présents, il extrait les informations de l’outil, appelle le serveur MCP avec la requête de l’outil, et ajoute les résultats aux messages de la conversation. Il continue ensuite la conversation avec le LLM et les messages sont mis à jour avec la réponse de l’assistant et les résultats de l’appel de l’outil.

Pour extraire les informations d’appel d’outil que le LLM retourne pour les appels MCP, nous allons ajouter une autre fonction d’aide pour extraire tout ce qui est nécessaire pour effectuer l’appel. Ajoutez le code suivant à la fin de votre fichier `main.rs` :

```rust
fn extract_tool_call_info(tool_call: &Value) -> Result<(String, String, String), Box<dyn Error>> {
    let tool_id = tool_call
        .get("id")
        .and_then(|id| id.as_str())
        .unwrap_or("")
        .to_string();
    let function = tool_call.get("function").ok_or("Missing function")?;
    let name = function
        .get("name")
        .and_then(|n| n.as_str())
        .unwrap_or("")
        .to_string();
    let args = function
        .get("arguments")
        .and_then(|a| a.as_str())
        .unwrap_or("{}")
        .to_string();
    Ok((tool_id, name, args))
}
```

Avec toutes les pièces en place, nous pouvons maintenant gérer l’invite initiale de l’utilisateur et appeler le LLM. Mettez à jour votre fonction `main` pour inclure le code suivant :

```rust
// Conversation LLM avec appels d'outils
let response = call_llm(&openai_client, &messages, &tools).await?;
process_llm_response(
    &response,
    &mcp_client,
    &openai_client,
    &tools,
    &mut messages,
)
.await?;
```

Cela interrogera le LLM avec l’invite initiale de l’utilisateur demandant la somme de deux nombres, et il traitera la réponse pour gérer dynamiquement les appels d’outils.

Super, vous l’avez fait !

## Exercice

Prenez le code de l’exercice et développez le serveur avec quelques outils supplémentaires. Ensuite, créez un client avec un LLM, comme dans l’exercice, et testez-le avec différentes invites pour vous assurer que tous vos outils serveur sont appelés dynamiquement. Cette façon de construire un client signifie que l’utilisateur final aura une excellente expérience utilisateur car il pourra utiliser des invites, au lieu de commandes client exactes, et ignorer totalement tout appel au serveur MCP.

## Solution

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## Points clés à retenir

- Ajouter un LLM à votre client offre une meilleure façon pour les utilisateurs d’interagir avec les serveurs MCP.
- Vous devez convertir la réponse du serveur MCP en quelque chose que le LLM peut comprendre.

## Exemples

- [Calculatrice Java](../samples/java/calculator/README.md)
- [Calculatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculatrice JavaScript](../samples/javascript/README.md)
- [Calculatrice TypeScript](../samples/typescript/README.md)
- [Calculatrice Python](../../../../03-GettingStarted/samples/python)
- [Calculatrice Rust](../../../../03-GettingStarted/samples/rust)

## Ressources supplémentaires

## Et après ?

- Suivant : [Consommer un serveur avec Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->