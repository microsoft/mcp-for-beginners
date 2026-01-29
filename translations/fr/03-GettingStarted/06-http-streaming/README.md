# Diffusion HTTPS avec le protocole Model Context Protocol (MCP)

Ce chapitre offre un guide complet pour mettre en œuvre une diffusion sécurisée, évolutive et en temps réel avec le protocole Model Context Protocol (MCP) en utilisant HTTPS. Il aborde la motivation pour la diffusion, les mécanismes de transport disponibles, comment implémenter HTTP diffusable dans MCP, les meilleures pratiques en matière de sécurité, la migration depuis SSE, et des conseils pratiques pour créer vos propres applications MCP de diffusion.

## Mécanismes de transport et diffusion dans MCP

Cette section explore les différents mécanismes de transport disponibles dans MCP et leur rôle dans l'activation des capacités de diffusion pour une communication en temps réel entre clients et serveurs.

### Qu'est-ce qu'un mécanisme de transport ?

Un mécanisme de transport définit comment les données sont échangées entre le client et le serveur. MCP prend en charge plusieurs types de transport adaptés à différents environnements et besoins :

- **stdio** : Entrée/sortie standard, adapté aux outils locaux et basés sur CLI. Simple mais inadapté pour le web ou le cloud.
- **SSE (Server-Sent Events)** : Permet aux serveurs d'envoyer des mises à jour en temps réel aux clients via HTTP. Idéal pour les interfaces web, mais limité en évolutivité et flexibilité.
- **HTTP diffusable** : Transport moderne basé sur HTTP, prenant en charge les notifications et offrant une meilleure évolutivité. Recommandé pour la plupart des scénarios de production et de cloud.

### Tableau comparatif

Voici un tableau comparatif pour comprendre les différences entre ces mécanismes de transport :

| Transport         | Mises à jour en temps réel | Diffusion | Évolutivité | Cas d'utilisation         |
|-------------------|---------------------------|-----------|-------------|---------------------------|
| stdio             | Non                       | Non       | Faible      | Outils CLI locaux         |
| SSE               | Oui                       | Oui       | Moyenne     | Web, mises à jour en temps réel |
| HTTP diffusable   | Oui                       | Oui       | Élevée      | Cloud, multi-clients      |

> **Astuce :** Le choix du bon transport impacte les performances, l'évolutivité et l'expérience utilisateur. **HTTP diffusable** est recommandé pour les applications modernes, évolutives et prêtes pour le cloud.

Notez les transports stdio et SSE présentés dans les chapitres précédents, ainsi que le transport HTTP diffusable abordé dans ce chapitre.

## Diffusion : Concepts et motivation

Comprendre les concepts fondamentaux et les motivations derrière la diffusion est essentiel pour mettre en œuvre des systèmes de communication en temps réel efficaces.

**La diffusion** est une technique en programmation réseau qui permet d'envoyer et de recevoir des données en petits morceaux gérables ou sous forme de séquence d'événements, plutôt que d'attendre que toute la réponse soit prête. Cela est particulièrement utile pour :

- Les fichiers ou ensembles de données volumineux.
- Les mises à jour en temps réel (par exemple, chat, barres de progression).
- Les calculs de longue durée où vous souhaitez tenir l'utilisateur informé.

Voici ce qu'il faut savoir sur la diffusion à un niveau général :

- Les données sont livrées progressivement, pas toutes en une fois.
- Le client peut traiter les données au fur et à mesure qu'elles arrivent.
- Réduit la latence perçue et améliore l'expérience utilisateur.

### Pourquoi utiliser la diffusion ?

Les raisons d'utiliser la diffusion sont les suivantes :

- Les utilisateurs reçoivent un retour immédiat, pas seulement à la fin.
- Permet des applications en temps réel et des interfaces réactives.
- Utilisation plus efficace des ressources réseau et de calcul.

### Exemple simple : Serveur et client HTTP de diffusion

Voici un exemple simple de mise en œuvre de la diffusion :

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

Cet exemple montre un serveur envoyant une série de messages au client au fur et à mesure qu'ils deviennent disponibles, plutôt que d'attendre que tous les messages soient prêts.

**Comment cela fonctionne :**

- Le serveur génère chaque message dès qu'il est prêt.
- Le client reçoit et imprime chaque morceau dès qu'il arrive.

**Exigences :**

- Le serveur doit utiliser une réponse diffusable (par exemple, `StreamingResponse` dans FastAPI).
- Le client doit traiter la réponse comme un flux (`stream=True` dans requests).
- Le type de contenu est généralement `text/event-stream` ou `application/octet-stream`.

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

**Notes sur l'implémentation en Java :**

- Utilise la pile réactive de Spring Boot avec `Flux` pour la diffusion.
- `ServerSentEvent` fournit une diffusion structurée d'événements avec des types d'événements.
- `WebClient` avec `bodyToFlux()` permet une consommation réactive de la diffusion.
- `delayElements()` simule le temps de traitement entre les événements.
- Les événements peuvent avoir des types (`info`, `result`) pour une meilleure gestion côté client.

### Comparaison : Diffusion classique vs diffusion MCP

Les différences entre la diffusion classique et la diffusion dans MCP peuvent être décrites comme suit :

| Fonctionnalité          | Diffusion HTTP classique       | Diffusion MCP (Notifications)      |
|-------------------------|-------------------------------|-------------------------------------|
| Réponse principale      | En morceaux                   | Unique, à la fin                   |
| Mises à jour de progrès | Envoyées sous forme de morceaux | Envoyées sous forme de notifications |
| Exigences côté client    | Doit traiter le flux          | Doit implémenter un gestionnaire de messages |
| Cas d'utilisation        | Fichiers volumineux, flux AI  | Progrès, journaux, retour en temps réel |

### Différences clés observées

Voici quelques différences clés supplémentaires :

- **Modèle de communication :**
  - Diffusion HTTP classique : Utilise un encodage de transfert par morceaux pour envoyer des données en morceaux.
  - Diffusion MCP : Utilise un système de notifications structuré avec le protocole JSON-RPC.

- **Format des messages :**
  - HTTP classique : Morceaux de texte brut avec des sauts de ligne.
  - MCP : Objets LoggingMessageNotification structurés avec des métadonnées.

- **Implémentation côté client :**
  - HTTP classique : Client simple qui traite les réponses diffusées.
  - MCP : Client plus sophistiqué avec un gestionnaire de messages pour traiter différents types de messages.

- **Mises à jour de progrès :**
  - HTTP classique : Le progrès fait partie du flux de réponse principal.
  - MCP : Le progrès est envoyé via des messages de notification séparés tandis que la réponse principale arrive à la fin.

### Recommandations

Voici quelques recommandations pour choisir entre la mise en œuvre de la diffusion classique (comme un point de terminaison que nous avons montré ci-dessus en utilisant `/stream`) et la diffusion via MCP.

- **Pour des besoins de diffusion simples :** La diffusion HTTP classique est plus simple à implémenter et suffisante pour des besoins de diffusion basiques.

- **Pour des applications complexes et interactives :** La diffusion MCP offre une approche plus structurée avec des métadonnées enrichies et une séparation entre les notifications et les résultats finaux.

- **Pour les applications d'IA :** Le système de notifications de MCP est particulièrement utile pour les tâches d'IA de longue durée où vous souhaitez tenir les utilisateurs informés des progrès.

## Diffusion dans MCP

D'accord, vous avez vu quelques recommandations et comparaisons sur la différence entre la diffusion classique et la diffusion dans MCP. Entrons dans les détails sur la manière de tirer parti de la diffusion dans MCP.

Comprendre comment la diffusion fonctionne dans le cadre de MCP est essentiel pour créer des applications réactives qui fournissent un retour en temps réel aux utilisateurs pendant les opérations de longue durée.

Dans MCP, la diffusion ne consiste pas à envoyer la réponse principale en morceaux, mais à envoyer **des notifications** au client pendant qu'un outil traite une requête. Ces notifications peuvent inclure des mises à jour de progrès, des journaux ou d'autres événements.

### Comment cela fonctionne

Le résultat principal est toujours envoyé sous forme de réponse unique. Cependant, des notifications peuvent être envoyées sous forme de messages séparés pendant le traitement, mettant ainsi à jour le client en temps réel. Le client doit être capable de gérer et d'afficher ces notifications.

## Qu'est-ce qu'une notification ?

Nous avons mentionné "Notification", qu'est-ce que cela signifie dans le contexte de MCP ?

Une notification est un message envoyé par le serveur au client pour informer sur le progrès, le statut ou d'autres événements pendant une opération de longue durée. Les notifications améliorent la transparence et l'expérience utilisateur.

Par exemple, un client doit envoyer une notification une fois que la poignée de main initiale avec le serveur a été effectuée.

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

Les notifications appartiennent à un sujet dans MCP appelé ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Pour que le journal fonctionne, le serveur doit l'activer en tant que fonctionnalité/capacité comme suit :

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Selon le SDK utilisé, le journal peut être activé par défaut ou vous devrez peut-être l'activer explicitement dans la configuration de votre serveur.

Il existe différents types de notifications :

| Niveau     | Description                    | Exemple d'utilisation           |
|------------|--------------------------------|----------------------------------|
| debug      | Informations détaillées de débogage | Points d'entrée/sortie de fonction |
| info       | Messages d'information générale | Mises à jour de progrès          |
| notice     | Événements normaux mais significatifs | Changements de configuration     |
| warning    | Conditions d'avertissement     | Utilisation de fonctionnalités obsolètes |
| error      | Conditions d'erreur            | Échecs d'opération               |
| critical   | Conditions critiques           | Échecs de composants système     |
| alert      | Action immédiate requise       | Corruption de données détectée   |
| emergency  | Système inutilisable           | Panne complète du système        |

## Mise en œuvre des notifications dans MCP

Pour mettre en œuvre des notifications dans MCP, vous devez configurer à la fois le côté serveur et le côté client pour gérer les mises à jour en temps réel. Cela permet à votre application de fournir un retour immédiat aux utilisateurs pendant les opérations de longue durée.

### Côté serveur : Envoi de notifications

Commençons par le côté serveur. Dans MCP, vous définissez des outils qui peuvent envoyer des notifications pendant le traitement des requêtes. Le serveur utilise l'objet de contexte (généralement `ctx`) pour envoyer des messages au client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Dans l'exemple précédent, l'outil `process_files` envoie trois notifications au client pendant qu'il traite chaque fichier. La méthode `ctx.info()` est utilisée pour envoyer des messages d'information.

De plus, pour activer les notifications, assurez-vous que votre serveur utilise un transport diffusable (comme `streamable-http`) et que votre client implémente un gestionnaire de messages pour traiter les notifications. Voici comment configurer le serveur pour utiliser le transport `streamable-http` :

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

Dans cet exemple .NET, l'outil `ProcessFiles` est décoré avec l'attribut `Tool` et envoie trois notifications au client pendant qu'il traite chaque fichier. La méthode `ctx.Info()` est utilisée pour envoyer des messages d'information.

Pour activer les notifications dans votre serveur MCP .NET, assurez-vous d'utiliser un transport diffusable :

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Côté client : Réception des notifications

Le client doit implémenter un gestionnaire de messages pour traiter et afficher les notifications dès qu'elles arrivent.

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

Dans le code précédent, la fonction `message_handler` vérifie si le message entrant est une notification. Si c'est le cas, elle imprime la notification ; sinon, elle le traite comme un message serveur classique. Notez également comment la `ClientSession` est initialisée avec le `message_handler` pour gérer les notifications entrantes.

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

Dans cet exemple .NET, la fonction `MessageHandler` vérifie si le message entrant est une notification. Si c'est le cas, elle imprime la notification ; sinon, elle le traite comme un message serveur classique. La `ClientSession` est initialisée avec le gestionnaire de messages via les `ClientSessionOptions`.

Pour activer les notifications, assurez-vous que votre serveur utilise un transport diffusable (comme `streamable-http`) et que votre client implémente un gestionnaire de messages pour traiter les notifications.

## Notifications de progrès et scénarios

Cette section explique le concept des notifications de progrès dans MCP, pourquoi elles sont importantes, et comment les implémenter en utilisant HTTP diffusable. Vous trouverez également un exercice pratique pour renforcer votre compréhension.

Les notifications de progrès sont des messages en temps réel envoyés par le serveur au client pendant les opérations de longue durée. Au lieu d'attendre que tout le processus soit terminé, le serveur tient le client informé de l'état actuel. Cela améliore la transparence, l'expérience utilisateur et facilite le débogage.

**Exemple :**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Pourquoi utiliser les notifications de progrès ?

Les notifications de progrès sont essentielles pour plusieurs raisons :

- **Meilleure expérience utilisateur :** Les utilisateurs voient des mises à jour au fur et à mesure que le travail progresse, pas seulement à la fin.
- **Retour en temps réel :** Les clients peuvent afficher des barres de progression ou des journaux, rendant l'application plus réactive.
- **Débogage et surveillance facilités :** Les développeurs et les utilisateurs peuvent voir où un processus pourrait être lent ou bloqué.

### Comment implémenter les notifications de progrès

Voici comment vous pouvez implémenter les notifications de progrès dans MCP :

- **Côté serveur :** Utilisez `ctx.info()` ou `ctx.log()` pour envoyer des notifications à mesure que chaque élément est traité. Cela envoie un message au client avant que le résultat principal ne soit prêt.
- **Côté client :** Implémentez un gestionnaire de messages qui écoute et affiche les notifications dès qu'elles arrivent. Ce gestionnaire distingue les notifications du résultat final.

**Exemple côté serveur :**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Exemple côté client :**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Considérations de sécurité

Lors de la mise en œuvre de serveurs MCP avec des transports basés sur HTTP, la sécurité devient une préoccupation primordiale qui nécessite une attention particulière à plusieurs vecteurs d'attaque et mécanismes de protection.

### Aperçu

La sécurité est cruciale lorsque vous exposez des serveurs MCP via HTTP. HTTP diffusable introduit de nouvelles surfaces d'attaque et nécessite une configuration minutieuse.

### Points clés

- **Validation de l'en-tête Origin** : Validez toujours l'en-tête `Origin` pour éviter les attaques de rebinding DNS.
- **Binding à localhost** : Pour le développement local, liez les serveurs à `localhost` pour éviter de les exposer à Internet.
- **Authentification** : Implémentez une authentification (par exemple, clés API, OAuth) pour les déploiements en production.
- **CORS** : Configurez des politiques de partage des ressources entre origines (CORS) pour restreindre l'accès.
- **HTTPS** : Utilisez HTTPS en production pour chiffrer le trafic.

### Meilleures pratiques

- Ne faites jamais confiance aux requêtes entrantes sans validation.
- Enregistrez et surveillez tous les accès et erreurs.
- Mettez régulièrement à jour les dépendances pour corriger les vulnérabilités de sécurité.

### Défis

- Équilibrer la sécurité avec la facilité de développement.
- Assurer la compatibilité avec divers environnements clients.

## Migration de SSE à HTTP diffusable

Pour les applications utilisant actuellement Server-Sent Events (SSE), migrer vers HTTP diffusable offre des capacités améliorées et une meilleure durabilité à long terme pour vos implémentations MCP.

### Pourquoi migrer ?
Il existe deux raisons convaincantes de passer de SSE à Streamable HTTP :

- Streamable HTTP offre une meilleure scalabilité, compatibilité et un support de notifications plus riche que SSE.
- C'est le transport recommandé pour les nouvelles applications MCP.

### Étapes de migration

Voici comment migrer de SSE à Streamable HTTP dans vos applications MCP :

- **Mettez à jour le code serveur** pour utiliser `transport="streamable-http"` dans `mcp.run()`.
- **Mettez à jour le code client** pour utiliser `streamablehttp_client` à la place du client SSE.
- **Implémentez un gestionnaire de messages** dans le client pour traiter les notifications.
- **Testez la compatibilité** avec les outils et flux de travail existants.

### Maintenir la compatibilité

Il est recommandé de maintenir la compatibilité avec les clients SSE existants pendant le processus de migration. Voici quelques stratégies :

- Vous pouvez prendre en charge à la fois SSE et Streamable HTTP en exécutant les deux transports sur des points de terminaison différents.
- Migrez progressivement les clients vers le nouveau transport.

### Défis

Assurez-vous de relever les défis suivants lors de la migration :

- S'assurer que tous les clients sont mis à jour
- Gérer les différences dans la livraison des notifications

## Considérations de sécurité

La sécurité doit être une priorité absolue lors de l'implémentation de tout serveur, en particulier lorsqu'on utilise des transports basés sur HTTP comme Streamable HTTP dans MCP.

Lors de l'implémentation de serveurs MCP avec des transports basés sur HTTP, la sécurité devient une préoccupation majeure nécessitant une attention particulière aux multiples vecteurs d'attaque et mécanismes de protection.

### Aperçu

La sécurité est essentielle lorsque vous exposez des serveurs MCP via HTTP. Streamable HTTP introduit de nouvelles surfaces d'attaque et nécessite une configuration minutieuse.

Voici quelques considérations clés en matière de sécurité :

- **Validation de l'en-tête Origin** : Validez toujours l'en-tête `Origin` pour prévenir les attaques de rebinding DNS.
- **Liaison à localhost** : Pour le développement local, liez les serveurs à `localhost` pour éviter de les exposer à Internet.
- **Authentification** : Implémentez une authentification (par exemple, clés API, OAuth) pour les déploiements en production.
- **CORS** : Configurez les politiques de Cross-Origin Resource Sharing (CORS) pour restreindre l'accès.
- **HTTPS** : Utilisez HTTPS en production pour chiffrer le trafic.

### Bonnes pratiques

De plus, voici quelques bonnes pratiques à suivre lors de l'implémentation de la sécurité dans votre serveur de streaming MCP :

- Ne faites jamais confiance aux requêtes entrantes sans validation.
- Enregistrez et surveillez tous les accès et erreurs.
- Mettez régulièrement à jour les dépendances pour corriger les vulnérabilités de sécurité.

### Défis

Vous rencontrerez certains défis lors de l'implémentation de la sécurité dans les serveurs de streaming MCP :

- Trouver un équilibre entre sécurité et facilité de développement
- Assurer la compatibilité avec divers environnements clients

### Exercice : Construisez votre propre application MCP de streaming

**Scénario :**
Construisez un serveur et un client MCP où le serveur traite une liste d'éléments (par exemple, fichiers ou documents) et envoie une notification pour chaque élément traité. Le client doit afficher chaque notification dès qu'elle arrive.

**Étapes :**

1. Implémentez un outil serveur qui traite une liste et envoie des notifications pour chaque élément.
2. Implémentez un client avec un gestionnaire de messages pour afficher les notifications en temps réel.
3. Testez votre implémentation en exécutant à la fois le serveur et le client, et observez les notifications.

[Solution](./solution/README.md)

## Lectures complémentaires et prochaines étapes

Pour poursuivre votre apprentissage avec le streaming MCP et approfondir vos connaissances, cette section fournit des ressources supplémentaires et des suggestions pour développer des applications plus avancées.

### Lectures complémentaires

- [Microsoft : Introduction au streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft : Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft : CORS dans ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests : Requêtes en streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Prochaines étapes

- Essayez de construire des outils MCP plus avancés qui utilisent le streaming pour l'analyse en temps réel, le chat ou l'édition collaborative.
- Explorez l'intégration du streaming MCP avec des frameworks frontend (React, Vue, etc.) pour des mises à jour d'interface utilisateur en direct.
- Prochaine étape : [Utiliser l'outil AI pour VSCode](../07-aitk/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.