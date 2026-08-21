# Streaming HTTPS avec le Model Context Protocol (MCP)

Ce chapitre fournit un guide complet pour implémenter un streaming sécurisé, évolutif et en temps réel avec le Model Context Protocol (MCP) en utilisant HTTPS. Il couvre la motivation du streaming, les mécanismes de transport disponibles, comment implémenter HTTP streamable dans MCP, les meilleures pratiques en matière de sécurité, la migration depuis SSE, et des conseils pratiques pour créer vos propres applications MCP en streaming.

> **À venir :** cette leçon décrit HTTP streamable sous **MCP Specification 2025-11-25**, où une session est établie lors de `initialize` et épinglée avec un en-tête `Mcp-Session-Id`. La version candidate `2026-07-28` supprime complètement la négociation et l’identifiant de session, rendant chaque requête autonome et routable vers n’importe quelle instance serveur sans sessions persistantes. Voir [Ce qui change dans MCP : la version candidate 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) pour plus de détails.

## Mécanismes de transport et streaming dans MCP

Cette section explore les différents mécanismes de transport disponibles dans MCP et leur rôle pour permettre les capacités de streaming pour la communication en temps réel entre clients et serveurs.

### Qu’est-ce qu’un mécanisme de transport ?

Un mécanisme de transport définit comment les données sont échangées entre le client et le serveur. MCP supporte plusieurs types de transport pour s’adapter à différents environnements et besoins :

- **stdio** : Entrée/sortie standard, adapté aux outils locaux et en ligne de commande. Simple mais non adapté pour le web ou le cloud.
- **SSE (Server-Sent Events)** : Permet aux serveurs d’envoyer des mises à jour en temps réel aux clients via HTTP. Adapté aux interfaces web, mais limité en scalabilité et flexibilité. Depuis la spécification MCP 2025-06-18, le transport SSE autonome est déprécié et remplacé par le transport "Streamable HTTP".
- **Streamable HTTP** : Transport de streaming moderne basé sur HTTP, supportant les notifications et une meilleure scalabilité. Recommandé pour la plupart des scénarios de production et cloud.

### Tableau comparatif

Consultez le tableau de comparaison ci-dessous pour comprendre les différences entre ces mécanismes de transport :

| Transport         | Mises à jour en temps réel | Streaming | Scalabilité | Cas d’utilisation        |
|-------------------|----------------------------|-----------|-------------|--------------------------|
| stdio             | Non                        | Non       | Faible      | Outils CLI locaux         |
| SSE               | Oui                        | Oui       | Moyenne     | Web, mises à jour en temps réel |
| Streamable HTTP   | Oui                        | Oui       | Élevée      | Cloud, multi-clients     |

> **Astuce :** Le choix du transport impacte les performances, la scalabilité et l’expérience utilisateur. **Streamable HTTP** est recommandé pour des applications modernes, évolutives et prêtes pour le cloud.

Notez les transports stdio et SSE présentés dans les chapitres précédents et comment HTTP streamable est le transport abordé dans ce chapitre.

## Streaming : Concepts et motivation

Comprendre les concepts fondamentaux et les motivations derrière le streaming est essentiel pour mettre en œuvre des systèmes de communication en temps réel efficaces.

**Streaming** est une technique en programmation réseau qui permet d’envoyer et de recevoir des données en petits morceaux gérables ou comme une séquence d’événements, au lieu d’attendre que toute une réponse soit prête. Cela est particulièrement utile pour :

- De gros fichiers ou ensembles de données.
- Des mises à jour en temps réel (ex. : chat, barres de progression).
- Des calculs de longue durée où vous souhaitez tenir l’utilisateur informé.

Voici ce que vous devez savoir sur le streaming à un niveau élevé :

- Les données sont livrées progressivement, pas toutes en une fois.
- Le client peut traiter les données au fur et à mesure de leur arrivée.
- Réduit la latence perçue et améliore l’expérience utilisateur.

### Pourquoi utiliser le streaming ?

Les raisons d’utiliser le streaming sont les suivantes :

- Les utilisateurs reçoivent un retour immédiatement, pas seulement à la fin.
- Permet des applications en temps réel et des interfaces réactives.
- Utilisation plus efficace des ressources réseau et calcul.

### Exemple simple : serveur et client HTTP en streaming

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

Cet exemple démontre un serveur envoyant une série de messages au client au fur et à mesure qu’ils deviennent disponibles, plutôt que d’attendre que tous les messages soient prêts.

**Comment ça marche :**

- Le serveur renvoie chaque message dès qu’il est prêt.
- Le client reçoit et affiche chaque fragment à son arrivée.

**Pré-requis :**

- Le serveur doit utiliser une réponse en streaming (ex. : `StreamingResponse` dans FastAPI).
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

**Notes d’implémentation Java :**

- Utilise la pile réactive de Spring Boot avec `Flux` pour le streaming
- `ServerSentEvent` fournit un streaming d’événements structuré avec types d’événements
- `WebClient` avec `bodyToFlux()` permet la consommation réactive du flux
- `delayElements()` simule un temps de traitement entre les événements
- Les événements peuvent avoir des types (`info`, `result`) pour une meilleure gestion par le client

### Comparaison : Streaming classique vs Streaming MCP

Les différences entre le streaming "classique" et celui dans MCP peuvent être décrites ainsi :

| Fonctionnalité          | Streaming HTTP Classique         | Streaming MCP (Notifications)     |
|------------------------|---------------------------------|----------------------------------|
| Réponse principale      | Morcelée                        | Unique, à la fin                 |
| Mises à jour de progression | Envoyées sous forme de fragments | Envoyées sous forme de notifications |
| Exigences client       | Doit traiter le flux            | Doit implémenter un gestionnaire de messages |
| Cas d’utilisation      | Grands fichiers, flux de tokens IA | Progression, journaux, retours temps réel |

### Principales différences observées

De plus, voici quelques différences clés :

- **Pattern de communication :**
  - Streaming HTTP classique : utilise un encodage de transfert en morceaux simple pour envoyer des fragments
  - Streaming MCP : utilise un système de notifications structuré avec le protocole JSON-RPC

- **Format des messages :**
  - HTTP classique : fragments en texte clair avec des retours à la ligne
  - MCP : objets LoggingMessageNotification structurés avec métadonnées

- **Implémentation client :**
  - HTTP classique : client simple qui traite les réponses en streaming
  - MCP : client plus sophistiqué avec un gestionnaire de messages pour traiter différents types de messages

- **Mises à jour de progression :**
  - HTTP classique : la progression fait partie du flux principal de réponse
  - MCP : la progression est envoyée via des messages de notification séparés tandis que la réponse principale arrive à la fin

### Recommandations

Voici quelques recommandations concernant le choix entre l’implémentation du streaming classique (comme l’exemple utilisant `/stream`) ou le streaming via MCP.

- **Pour des besoins de streaming simples :** le streaming HTTP classique est plus simple à implémenter et suffisant pour les usages basiques.

- **Pour des applications complexes et interactives :** le streaming MCP offre une approche plus structurée avec des métadonnées riches et une séparation entre notifications et résultats finaux.

- **Pour les applications IA :** le système de notifications MCP est particulièrement utile pour les tâches IA longues où vous souhaitez tenir les utilisateurs informés de la progression.

## Streaming dans MCP

Bien, vous avez vu jusqu’ici quelques recommandations et comparaisons sur la différence entre streaming classique et streaming MCP. Entrons dans le détail de la façon dont vous pouvez exploiter le streaming dans MCP.

Comprendre comment fonctionne le streaming dans le cadre MCP est essentiel pour construire des applications réactives qui fournissent un retour en temps réel aux utilisateurs pendant les opérations longues.

Dans MCP, le streaming ne consiste pas à envoyer la réponse principale en morceaux, mais à envoyer des **notifications** au client pendant qu’un outil traite une requête. Ces notifications peuvent inclure des mises à jour de progression, des journaux ou d’autres événements.

### Comment ça marche

Le résultat principal est toujours envoyé en une seule réponse. Cependant, des notifications peuvent être envoyées sous forme de messages distincts pendant le traitement et ainsi tenir le client à jour en temps réel. Le client doit pouvoir gérer et afficher ces notifications.

## Qu’est-ce qu’une notification ?

Nous avons parlé de "Notification", que signifie-t-elle dans le contexte de MCP ?

Une notification est un message envoyé du serveur au client pour informer de la progression, du statut ou d’autres événements durant une opération longue. Les notifications améliorent la transparence et l’expérience utilisateur.

Par exemple, un client est supposé envoyer une notification une fois que la négociation initiale avec le serveur est effectuée.

Une notification ressemble à cela sous forme de message JSON :

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Les notifications appartiennent à un sujet dans MCP appelé ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Avis de dépréciation :** la version candidate de la spécification MCP du `2026-07-28` marque la primitive Logging comme dépréciée en faveur de `stderr` pour les transports stdio et OpenTelemetry pour l’observabilité structurée. Le Logging continue de fonctionner dans la version `2025-11-25` et au moins un an après toute dépréciation officielle. Voir [Ce qui change dans MCP : la version candidate 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Pour que le logging fonctionne, le serveur doit l’activer en tant que fonctionnalité/capacité comme suit :

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Selon le SDK utilisé, le logging peut être activé par défaut, ou vous devrez peut-être l’activer explicitement dans la configuration du serveur.

Il existe différents types de notifications :

| Niveau    | Description                   | Exemple d’usage               |
|-----------|-------------------------------|------------------------------|
| debug     | Informations de débogage détaillées | Points d’entrée/sortie de fonction |
| info      | Messages d’information générale | Mises à jour de progression  |
| notice    | Événements normaux mais importants | Changements de configuration |
| warning   | Conditions d’avertissement     | Usage de fonctionnalités dépréciées |
| error     | Conditions d’erreur           | Échecs d’opération           |
| critical  | Conditions critiques          | Pannes de composants système  |
| alert     | Action immédiate requise     | Détection de corruption de données |
| emergency | Système inutilisable          | Panne complète du système     |

## Implémentation des notifications dans MCP

Pour implémenter les notifications dans MCP, vous devez configurer les deux côtés, serveur et client, pour gérer les mises à jour en temps réel. Cela permet à votre application de fournir un retour immédiat aux utilisateurs pendant les opérations longues.

### Côté serveur : envoyer des notifications

Commençons par le côté serveur. Dans MCP, vous définissez des outils qui peuvent envoyer des notifications pendant le traitement des requêtes. Le serveur utilise l’objet contexte (généralement `ctx`) pour envoyer des messages au client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Dans l’exemple précédent, l’outil `process_files` envoie trois notifications au client pendant qu’il traite chaque fichier. La méthode `ctx.info()` est utilisée pour envoyer des messages d’information.

De plus, pour activer les notifications, assurez-vous que votre serveur utilise un transport en streaming (comme `streamable-http`) et que votre client implémente un gestionnaire de messages pour traiter les notifications. Voici comment configurer le serveur pour utiliser le transport `streamable-http` :

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

Dans cet exemple .NET, l’outil `ProcessFiles` est décoré avec l’attribut `Tool` et envoie trois notifications au client pendant qu’il traite chaque fichier. La méthode `ctx.Info()` est utilisée pour envoyer des messages d’information.

Pour activer les notifications dans votre serveur MCP .NET, assurez-vous d’utiliser un transport en streaming :

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Côté client : recevoir des notifications

Le client doit implémenter un gestionnaire de messages pour traiter et afficher les notifications à leur arrivée.

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

Dans le code précédent, la fonction `message_handler` vérifie si le message entrant est une notification. Si c’est le cas, elle affiche la notification ; sinon, elle le traite comme un message serveur classique. Notez aussi comment la `ClientSession` est initialisée avec le `message_handler` pour gérer les notifications entrantes.

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

Dans cet exemple .NET, la fonction `MessageHandler` vérifie si le message entrant est une notification. Si c’est le cas, elle affiche la notification ; sinon, elle le traite comme un message serveur classique. La `ClientSession` est initialisée avec le gestionnaire de messages via les `ClientSessionOptions`.

Pour activer les notifications, assurez-vous que votre serveur utilise un transport en streaming (comme `streamable-http`) et que votre client implémente un gestionnaire de messages pour traiter les notifications.

## Notifications de progression & scénarios

Cette section explique le concept des notifications de progression dans MCP, pourquoi elles sont importantes, et comment les implémenter avec Streamable HTTP. Vous trouverez également un exercice pratique pour renforcer votre compréhension.

Les notifications de progression sont des messages envoyés en temps réel du serveur vers le client pendant des opérations longues. Au lieu d’attendre que le processus soit entièrement terminé, le serveur tient le client informé du statut actuel. Cela améliore la transparence, l’expérience utilisateur et facilite le débogage.

**Exemple :**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Pourquoi utiliser les notifications de progression ?

Les notifications de progression sont essentielles pour plusieurs raisons :

- **Meilleure expérience utilisateur :** les utilisateurs voient des mises à jour au fur et à mesure, pas uniquement à la fin.
- **Retour en temps réel :** les clients peuvent afficher des barres de progression ou des journaux, rendant l’application réactive.
- **Débogage et surveillance facilités :** développeurs et utilisateurs peuvent voir où un processus est lent ou bloqué.

### Comment implémenter les notifications de progression

Voici comment vous pouvez implémenter des notifications de progression dans MCP :

- **Côté serveur :** utilisez `ctx.info()` ou `ctx.log()` pour envoyer des notifications à chaque traitement d’élément. Cela envoie un message au client avant que le résultat principal soit prêt.
- **Côté client :** implémentez un gestionnaire de messages qui écoute et affiche les notifications dès leur arrivée. Ce gestionnaire distingue les notifications du résultat final.

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

**Exemple Client :**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Considérations de Sécurité

La sécurité doit être une priorité absolue lors de la mise en œuvre de tout serveur, en particulier lorsqu'on utilise des transports basés sur HTTP comme Streamable HTTP dans MCP.

Lors de l'implémentation de serveurs MCP avec des transports basés sur HTTP, la sécurité devient une préoccupation majeure qui nécessite une attention rigoureuse à plusieurs vecteurs d'attaque et mécanismes de protection.

### Vue d'Ensemble

La sécurité est critique lorsqu'on expose des serveurs MCP via HTTP. Streamable HTTP introduit de nouvelles surfaces d'attaque et nécessite une configuration minutieuse.

Voici quelques considérations clés de sécurité :

- **Validation de l'en-tête Origin** : Toujours valider l'en-tête `Origin` pour prévenir les attaques de rebinding DNS.
- **Liaison à localhost** : Pour le développement local, lier les serveurs à `localhost` afin d'éviter de les exposer à l'internet public.
- **Authentification** : Mettre en œuvre une authentification (par exemple, clés API, OAuth) pour les déploiements en production.
- **CORS** : Configurer les politiques Cross-Origin Resource Sharing (CORS) pour restreindre l'accès.
- **HTTPS** : Utiliser HTTPS en production pour chiffrer le trafic.

### Bonnes Pratiques

De plus, voici quelques bonnes pratiques à suivre lors de l'implémentation de la sécurité dans votre serveur de streaming MCP :

- Ne jamais faire confiance aux requêtes entrantes sans validation.
- Journaliser et surveiller tous les accès et erreurs.
- Mettre à jour régulièrement les dépendances pour corriger les vulnérabilités de sécurité.

### Défis

Vous rencontrerez certains défis lors de l'implémentation de la sécurité dans les serveurs de streaming MCP :

- Trouver un équilibre entre sécurité et facilité de développement
- Assurer la compatibilité avec différents environnements clients


## Passage de SSE à Streamable HTTP

Pour les applications utilisant actuellement les Server-Sent Events (SSE), migrer vers Streamable HTTP offre des capacités améliorées et une meilleure durabilité à long terme pour vos implémentations MCP.

### Pourquoi Migrer ?

Il y a deux raisons convaincantes pour passer de SSE à Streamable HTTP :

- Streamable HTTP offre une meilleure évolutivité, compatibilité, et un support de notifications plus riche que SSE.
- C'est le transport recommandé pour les nouvelles applications MCP.

### Étapes de Migration

Voici comment vous pouvez migrer de SSE à Streamable HTTP dans vos applications MCP :

- **Mettre à jour le code serveur** pour utiliser `transport="streamable-http"` dans `mcp.run()`.
- **Mettre à jour le code client** pour utiliser `streamablehttp_client` au lieu du client SSE.
- **Implémenter un gestionnaire de messages** côté client pour traiter les notifications.
- **Tester la compatibilité** avec les outils et flux existants.

### Maintenir la Compatibilité

Il est recommandé de maintenir la compatibilité avec les clients SSE existants durant le processus de migration. Voici quelques stratégies :

- Vous pouvez supporter à la fois SSE et Streamable HTTP en faisant tourner les deux transports sur des points de terminaison différents.
- Migrer progressivement les clients vers le nouveau transport.

### Défis

Assurez-vous de relever les défis suivants durant la migration :

- S'assurer que tous les clients soient mis à jour
- Gérer les différences dans la livraison des notifications

### Exercice : Construisez votre propre application MCP en streaming

**Scénario :**
Construisez un serveur et un client MCP où le serveur traite une liste d'éléments (par exemple, fichiers ou documents) et envoie une notification pour chaque élément traité. Le client doit afficher chaque notification à son arrivée.

**Étapes :**

1. Implémentez un outil serveur qui traite une liste et envoie des notifications pour chaque élément.
2. Implémentez un client avec un gestionnaire de messages pour afficher les notifications en temps réel.
3. Testez votre implémentation en faisant tourner serveur et client, et observez les notifications.

[Solution](./solution/README.md)

## Lecture Complémentaire & Quelles Étapes Suivantes ?

Pour continuer votre parcours avec le streaming MCP et approfondir vos connaissances, cette section fournit des ressources supplémentaires et des étapes suggérées pour construire des applications plus avancées.

### Lecture Complémentaire

- [Microsoft : Introduction au Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft : Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft : CORS dans ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests : Requêtes en Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Quelles Étapes Suivantes ?

- Essayez de construire des outils MCP plus avancés qui utilisent le streaming pour l'analytique en temps réel, le chat, ou la collaboration en édition.
- Explorez l'intégration du streaming MCP avec des frameworks frontend (React, Vue, etc.) pour des mises à jour d'interface utilisateur en direct.
- Suivant : [Utilisation de AI Toolkit pour VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->