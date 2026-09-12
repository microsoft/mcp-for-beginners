# Diffusion HTTPS avec le protocole Model Context Protocol (MCP)

Ce chapitre fournit un guide complet pour mettre en œuvre la diffusion sécurisée, évolutive et en temps réel avec le Model Context Protocol (MCP) utilisant HTTPS. Il couvre la motivation pour la diffusion, les mécanismes de transport disponibles, comment mettre en œuvre le HTTP diffusible dans MCP, les meilleures pratiques de sécurité, la migration depuis SSE, et des conseils pratiques pour construire vos propres applications MCP diffusibles. 

> [!WARNING]
> Les exemples d'implémentation dans cette leçon ciblent la **spécification MCP
> `2025-11-25`** et démontrent la poignée de main héritée `initialize`,
> `Mcp-Session-Id`, le flux d'événements GET, et le modèle de reprise. MCP `2026-07-28`
> supprime ces fonctionnalités. Les requêtes HTTP diffusibles actuelles sont des requêtes POST autonomes
> avec les en-têtes `MCP-Protocol-Version` et `Mcp-Method`, plus `Mcp-Name` le cas échéant. Voir
> [Qu'est-ce qui a changé dans MCP : la spécification 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> avant d'utiliser ces exemples dans une nouvelle implémentation.


## Mécanismes de transport et diffusion dans MCP

Cette section explore les différents mécanismes de transport disponibles dans MCP et leur rôle pour permettre les capacités de diffusion pour la communication en temps réel entre clients et serveurs.

### Qu'est-ce qu'un mécanisme de transport ?

Un mécanisme de transport définit comment les données sont échangées entre le client et le serveur. MCP supporte plusieurs types de transport pour s'adapter à différents environnements et besoins :

- **stdio** : Entrée/sortie standard, adapté aux outils locaux et en ligne de commande. Simple mais non adapté au web ou au cloud.
- **HTTP+SSE** : Transport distant hérité, obsolète dans MCP `2025-03-26`
    et remplacé par HTTP diffusible. Ne l'utilisez pas pour de nouvelles implémentations.
- **HTTP diffusible** : Transport de diffusion moderne basé sur HTTP, prenant en charge les notifications et une meilleure évolutivité. Recommandé pour la plupart des scénarios de production et cloud.

### Tableau comparatif

Consultez le tableau comparatif ci-dessous pour comprendre les différences entre ces mécanismes de transport :

| Transport | Statut | Notifications | Usage typique |
|---|---|---|---|
| stdio | Actuel | Oui | Sous-processus locaux |
| HTTP+SSE | Obsolète | Oui | Implémentations distantes héritées |
| HTTP diffusible | Actuel | Oui | Serveurs distants et cloud |

> **Conseil :** Le choix du transport approprié impacte les performances, l'évolutivité et l'expérience utilisateur. **HTTP diffusible** est recommandé pour les applications modernes, évolutives et prêtes pour le cloud.

Les transports standards sont stdio et HTTP diffusible. HTTP+SSE apparaît uniquement
dans d'anciens exemples.

## Diffusion : concepts et motivation

Comprendre les concepts fondamentaux et les motivations derrière la diffusion est essentiel pour mettre en œuvre des systèmes de communication en temps réel efficaces.

**La diffusion** est une technique de programmation réseau qui permet d'envoyer et recevoir des données en petits morceaux gérables ou comme une séquence d'événements, plutôt que d'attendre qu'une réponse complète soit prête. Ceci est particulièrement utile pour :

- Fichiers ou ensembles de données volumineux.
- Mises à jour en temps réel (par ex., chat, barres de progression).
- Calculs longs où vous voulez tenir l'utilisateur informé.

Voici ce que vous devez savoir sur la diffusion à un niveau élevé :

- Les données sont délivrées progressivement, pas toutes en même temps.
- Le client peut traiter les données dès leur arrivée.
- Réduit la latence perçue et améliore l'expérience utilisateur.

### Pourquoi utiliser la diffusion ?

Les raisons d'utiliser la diffusion sont les suivantes :


- Les utilisateurs reçoivent un retour immédiatement, pas seulement à la fin
- Permet des applications en temps réel et des interfaces utilisateur réactives
- Utilisation plus efficace des ressources réseau et de calcul

### Exemple simple : Serveur et client HTTP Streaming

Voici un exemple simple de mise en œuvre du streaming :

#### Python

**Serveur (Python, utilisant FastAPI et StreamingResponse) :**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Client (Python, utilisant requests) :**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Cet exemple montre un serveur envoyant une série de messages au client dès qu'ils sont disponibles, plutôt que d'attendre que tous les messages soient prêts.

**Comment ça fonctionne :**

- Le serveur émet chaque message dès qu'il est prêt.
- Le client reçoit et affiche chaque segment dès son arrivée.

**Exigences :**

- Le serveur doit utiliser une réponse en streaming (par ex., `StreamingResponse` dans FastAPI).
- Le client doit traiter la réponse comme un flux (`stream=True` dans requests).
- Le Content-Type est généralement `text/event-stream` ou `application/octet-stream`.

#### Java

**Serveur (Java, utilisant Spring Boot et Server-Sent Events) :**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Client (Java, utilisant Spring WebFlux WebClient) :**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Notes d'implémentation Java :**

- Utilise la pile réactive Spring Boot avec `Flux` pour le streaming
- `ServerSentEvent` fournit un flux d'événements structuré avec des types d'événements
- `WebClient` avec `bodyToFlux()` permet la consommation réactive du streaming
- `delayElements()` simule le temps de traitement entre les événements
- Les événements peuvent avoir des types (`info`, `result`) pour une meilleure gestion côté client

### Comparaison : Streaming classique vs Streaming MCP

Les différences entre la manière dont le streaming fonctionne de façon "classique" et la manière dont il fonctionne dans MCP peuvent être présentées ainsi :

| Fonctionnalité         | Streaming HTTP classique       | Streaming MCP (Notifications)        |
|------------------------|-------------------------------|-------------------------------------|
| Réponse principale     | Morcelée                     | Unique, à la fin                     |
| Mises à jour de progression | Envoyées en morceaux de données | Envoyées en notifications           |
| Exigences client       | Doit traiter le flux          | Doit implémenter un gestionnaire de messages |
| Cas d'utilisation      | Grands fichiers, flux de tokens IA | Progression, journaux, retours en temps réel |

### Principales différences observées

En outre, voici quelques différences clés :

- **Modèle de communication :**
  - Streaming HTTP classique : utilise un simple encodage de transfert par morceaux pour envoyer des données en segments
  - Streaming MCP : utilise un système de notification structuré avec le protocole JSON-RPC

- **Format des messages :**
  - HTTP classique : morceaux de texte brut avec des sauts de ligne
  - MCP : objets LoggingMessageNotification structurés avec métadonnées

- **Implémentation client :**
  - HTTP classique : client simple qui traite les réponses en streaming
  - MCP : client plus sophistiqué avec un gestionnaire de messages pour traiter différents types de messages

- **Mises à jour de progression :**
  - HTTP classique : la progression fait partie du flux de réponse principal
  - MCP : la progression est envoyée via des messages de notification séparés tandis que la réponse principale arrive à la fin

### Recommandations

Voici quelques recommandations concernant le choix entre l’implémentation du streaming classique (comme l’endpoint montré plus haut utilisant `/stream`) et le streaming via MCP.

- **Pour des besoins simples de streaming :** Le streaming HTTP classique est plus simple à mettre en œuvre et suffisant pour des besoins basiques.


- **Pour les applications complexes et interactives :** le streaming MCP offre une approche plus structurée avec des métadonnées enrichies et une séparation entre les notifications et les résultats finaux.

- **Pour les applications d'IA :** le système de notification de MCP est particulièrement utile pour les tâches d'IA longues où vous souhaitez tenir les utilisateurs informés de la progression.

## Streaming dans MCP

D'accord, vous avez vu jusqu'à présent quelques recommandations et comparaisons sur la différence entre le streaming classique et le streaming dans MCP. Entrons dans le détail sur la manière dont vous pouvez exploiter le streaming dans MCP.

Comprendre comment le streaming fonctionne dans le cadre MCP est essentiel pour construire des applications réactives qui fournissent un retour en temps réel aux utilisateurs pendant les opérations longues.

Dans MCP, le streaming ne consiste pas à envoyer la réponse principale en morceaux, mais à envoyer des **notifications** au client pendant qu'un outil traite une requête. Ces notifications peuvent inclure des mises à jour de progression, des journaux ou d'autres événements.

### Comment ça fonctionne

Le résultat principal est toujours envoyé en une seule réponse. Cependant, des notifications peuvent être envoyées comme messages séparés pendant le traitement et ainsi mettre à jour le client en temps réel. Le client doit être capable de gérer et d'afficher ces notifications.

### Exercice optionnel : se connecter à un serveur MCP hébergé

Vous pouvez également utiliser Streamable HTTP sans exécuter de serveur local. Cet exemple
se connecte à [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
découvre ses outils, et recherche la documentation publique MCP en utilisant le même
SDK Python que le [client local](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Le point de terminaison anonyme de Parallel ne nécessite ni compte ni clé API. L'accès gratuit est
soumis à une limitation de débit. L'exécution de ce script envoie les requêtes de recherche, l'objectif, et un
identifiant de session aléatoire à Parallel. Le service offre aussi `web_fetch`,
qui envoie les URL demandées et tout contexte fourni à Parallel. Utilisez des informations publiques
pour cet exercice ; consultez ses [conditions](https://parallel.ai/customer-terms)
et sa [politique de confidentialité](https://parallel.ai/privacy-policy).

Avec Python 3.10 ou plus récent et un environnement virtuel activé, installez le SDK :

```sh
python -m pip install "mcp>=1.10,<2"
```

Enregistrez ceci sous `hosted_search.py` et lancez `python hosted_search.py` :

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

Attendez-vous à ce que la découverte inclue `web_search` et `web_fetch`, suivie d'une réponse
de recherche contenant les URL sources et des extraits. Les résultats peuvent varier ou être vides.
Le script vérifie `isError` car un outil peut échouer même si la requête HTTP
réussit. En cas de limitation de débit, attendez avant de réessayer. Réutilisez le même
`session_id` si vous étendez le script avec des appels de recherche ou de récupération liés.

Streamable HTTP permet des réponses JSON et SSE ; ce serveur peut retourner un
résultat JSON complet sans notifications de progression. Le SDK gère
le transport. Continuez avec l'exemple local ci-dessous pour apprendre les notifications.
Ce script optionnel effectue une recherche explicite et ferme sa connexion lorsqu’
elle se termine. Si vous exposez plus tard ces outils à un agent, l'agent peut les invoquer
pendant son travail ; considérez le texte web récupéré comme des données non fiables.

## Qu'est-ce qu'une Notification ?

Nous avons dit "Notification", qu'est-ce que cela signifie dans le contexte MCP ?

Une notification est un message JSON-RPC qui n'a pas d’`id` et ne
reçoit pas de réponse. MCP utilise les notifications pour la progression, l'annulation, et
d'autres événements unidirectionnels.

Dans MCP `2025-11-25`, un client envoie `notifications/initialized` après le

poignée de main d'initialisation. MCP `2026-07-28` n'a pas de poignée de main d'initialisation, donc
cette notification est un comportement hérité.

Une notification ressemble à ceci sous forme de message JSON :

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

La journalisation est une fonctionnalité qui utilise les notifications ; les notifications elles-mêmes sont un
type général de message JSON-RPC.

> **Obsolète dans MCP `2026-07-28` :** la fonctionnalité de journalisation reste disponible
> pour compatibilité mais peut être supprimée lors de la première révision de la spécification
> publiée à partir du 28 juillet 2027. Les nouvelles implémentations devraient utiliser
> `stderr` avec stdio ou OpenTelemetry pour une observabilité structurée.

Pour une implémentation héritée `2025-11-25`, le serveur active la capacité de journalisation
de la manière suivante :

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Selon le SDK utilisé, la journalisation peut être activée par défaut, ou vous devrez peut-être l'activer explicitement dans la configuration de votre serveur.

Il existe différents types de notifications :

| Niveau    | Description                   | Cas d'utilisation exemple     |
|-----------|------------------------------|-------------------------------|
| debug     | Informations détaillées de débogage | Points d'entrée/sortie des fonctions |
| info      | Messages d'information générale | Mises à jour de progression opérationnelle |
| notice    | Événements normaux mais significatifs | Modifications de configuration    |
| warning   | Conditions d'avertissement    | Utilisation de fonctionnalités obsolètes |
| error     | Conditions d'erreur           | Échecs d'opération             |
| critical  | Conditions critiques          | Pannes de composants systèmes  |
| alert     | Action immédiate requise      | Détection de corruption de données |
| emergency | Système inutilisable          | Panne complète du système      |

## Implémentation des notifications dans MCP

Pour implémenter les notifications dans MCP, vous devez configurer à la fois le serveur et le client pour gérer les mises à jour en temps réel. Cela permet à votre application de fournir un retour immédiat aux utilisateurs lors d'opérations longues.

### Côté serveur : envoi des notifications

Commençons par le côté serveur. Dans MCP, vous définissez des outils capables d'envoyer des notifications pendant le traitement des requêtes. Le serveur utilise l'objet contexte (généralement `ctx`) pour envoyer des messages au client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Dans l'exemple précédent, l'outil `process_files` envoie trois notifications au client pendant le traitement de chaque fichier. La méthode `ctx.info()` est utilisée pour envoyer des messages d'information.

De plus, pour activer les notifications, assurez-vous que votre serveur utilise un transport en streaming (comme `streamable-http`) et que votre client implémente un gestionnaire de messages pour traiter les notifications. Voici comment configurer le serveur pour utiliser le transport `streamable-http`:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

Dans cet exemple .NET, l'outil `ProcessFiles` est décoré avec l'attribut `Tool` et envoie trois notifications au client pendant le traitement de chaque fichier. La méthode `ctx.Info()` est utilisée pour envoyer des messages d'information.

Pour activer les notifications dans votre serveur MCP .NET, assurez-vous d'utiliser un transport en streaming :

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Côté client : réception des notifications

Le client doit implémenter un gestionnaire de messages pour traiter et afficher les notifications dès leur arrivée.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```


Dans le code précédent, la fonction `message_handler` vérifie si le message entrant est une notification. Si c'est le cas, elle affiche la notification ; sinon, elle le traite comme un message serveur classique. Notez également comment le `ClientSession` est initialisé avec le `message_handler` pour gérer les notifications entrantes.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```


Dans cet exemple .NET, la fonction `MessageHandler` vérifie si le message entrant est une notification. Si c'est le cas, elle affiche la notification ; sinon, elle le traite comme un message serveur classique. `ClientSession` est initialisé avec le gestionnaire de messages via `ClientSessionOptions`.

Pour activer les notifications, assurez-vous que votre serveur utilise un transport en flux (comme `streamable-http`) et que votre client implémente un gestionnaire de messages pour traiter les notifications.

## Notifications de progression & scénarios

Cette section explique le concept de notifications de progression dans MCP, pourquoi elles sont importantes et comment les implémenter avec Streamable HTTP. Vous y trouverez également un exercice pratique pour renforcer votre compréhension.

Les notifications de progression sont des messages en temps réel envoyés du serveur au client pendant les opérations longues. Au lieu d’attendre la fin complète du processus, le serveur informe le client du statut actuel. Cela améliore la transparence, l’expérience utilisateur et facilite le débogage.

**Exemple :**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Pourquoi utiliser les notifications de progression ?

Les notifications de progression sont essentielles pour plusieurs raisons :

- **Meilleure expérience utilisateur :** Les utilisateurs voient les mises à jour au fur et à mesure, pas seulement à la fin.
- **Retour en temps réel :** Les clients peuvent afficher des barres de progression ou des journaux, rendant l’application réactive.
- **Débogage et surveillance facilités :** Développeurs et utilisateurs voient où un processus peut être lent ou bloqué.

### Comment implémenter les notifications de progression

Voici comment vous pouvez implémenter les notifications de progression dans MCP :

- **Côté serveur :** Utilisez `ctx.info()` ou `ctx.log()` pour envoyer des notifications à mesure que chaque élément est traité. Cela envoie un message au client avant que le résultat principal ne soit prêt.
- **Côté client :** Implémentez un gestionnaire de messages qui écoute et affiche les notifications à leur arrivée. Ce gestionnaire fait la distinction entre notifications et résultat final.

**Exemple serveur :**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Exemple client :**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Considérations de sécurité

La sécurité doit être une priorité absolue lors de l’implémentation de tout serveur, surtout avec des transports HTTP comme Streamable HTTP dans MCP.

Lors de l’implémentation de serveurs MCP avec des transports basés sur HTTP, la sécurité devient une préoccupation majeure nécessitant une attention soigneuse aux multiples vecteurs d’attaque et aux mécanismes de protection.

### Aperçu

La sécurité est critique lors de l’exposition de serveurs MCP via HTTP. Streamable HTTP introduit de nouvelles surfaces d’attaque et nécessite une configuration rigoureuse.

Voici quelques considérations clés de sécurité :

- **Validation de l’en-tête Origin** : Validez toujours l’en-tête `Origin` pour prévenir les attaques de DNS rebinding.
- **Binding localhost** : Pour le développement local, liez les serveurs à `localhost` pour éviter leur exposition sur Internet public.
- **Authentification** : Implémentez une authentification (ex. clés API, OAuth) pour les déploiements en production.
- **CORS** : Configurez les politiques Cross-Origin Resource Sharing (CORS) pour restreindre l’accès.
- **HTTPS** : Utilisez HTTPS en production pour chiffrer le trafic.

### Bonnes pratiques

De plus, voici quelques bonnes pratiques à suivre lors de la mise en œuvre de la sécurité dans votre serveur de streaming MCP :

- Ne faites jamais confiance aux requêtes entrantes sans validation.
- Enregistrez et surveillez tous les accès et erreurs.
- Mettez régulièrement à jour les dépendances pour corriger les vulnérabilités de sécurité.

### Défis

Vous rencontrerez certains défis lors de la mise en œuvre de la sécurité dans les serveurs de streaming MCP :

- Trouver l’équilibre entre sécurité et facilité de développement
- Assurer la compatibilité avec divers environnements clients


## Migration de SSE vers Streamable HTTP

Pour les applications utilisant actuellement les Server-Sent Events (SSE), migrer vers Streamable HTTP offre des capacités améliorées et une meilleure durabilité sur le long terme pour vos implémentations MCP.

### Pourquoi migrer ?

Deux raisons majeures motivent la migration de SSE vers Streamable HTTP :

- Streamable HTTP offre une meilleure scalabilité, compatibilité et un support plus riche de notifications que SSE.
- C’est le transport recommandé pour les nouvelles applications MCP.

### Étapes de migration

Voici comment migrer de SSE vers Streamable HTTP dans vos applications MCP :

- **Mettez à jour le code serveur** pour utiliser `transport="streamable-http"` dans `mcp.run()`.
- **Mettez à jour le code client** pour utiliser `streamablehttp_client` au lieu du client SSE.
- **Implémentez un gestionnaire de messages** dans le client pour traiter les notifications.
- **Testez la compatibilité** avec les outils et workflows existants.

### Maintien de la compatibilité

Il est recommandé de maintenir la compatibilité avec les clients SSE existants pendant la migration. Voici quelques stratégies :

- Vous pouvez supporter à la fois SSE et Streamable HTTP en exécutant les deux transports sur des points de terminaison différents.
- Migrez progressivement les clients vers le nouveau transport.

### Défis

Assurez-vous de résoudre les défis suivants pendant la migration :

- Veiller à ce que tous les clients soient mis à jour
- Gérer les différences dans la livraison des notifications

### Exercice : Construisez votre propre application MCP en streaming

**Scénario :**
Construisez un serveur et un client MCP où le serveur traite une liste d’éléments (ex. fichiers ou documents) et envoie une notification pour chaque élément traité. Le client doit afficher chaque notification à son arrivée.

**Étapes :**

1. Implémentez un outil serveur qui traite une liste et envoie des notifications pour chaque élément.
2. Implémentez un client avec un gestionnaire de messages pour afficher les notifications en temps réel.
3. Testez votre implémentation en lançant le serveur et le client, et observez les notifications.

[Solution](./solution/README.md)

## Lectures complémentaires & Suite ?

Pour poursuivre votre apprentissage du streaming MCP et approfondir vos connaissances, cette section fournit des ressources supplémentaires et les étapes suggérées pour construire des applications plus avancées.

### Lectures complémentaires

- [Microsoft : Introduction au streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft : Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft : CORS dans ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests : Requêtes en streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Suite ?

- Essayez de construire des outils MCP plus avancés utilisant le streaming pour des analyses en temps réel, le chat ou l’édition collaborative.
- Explorez l’intégration du streaming MCP avec des frameworks frontend (React, Vue, etc.) pour des mises à jour d’interface en direct.
- Suivant : [Utilisation de AI Toolkit pour VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->