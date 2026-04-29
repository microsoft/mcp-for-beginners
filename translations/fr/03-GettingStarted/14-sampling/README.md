# Échantillonnage - déléguer des fonctionnalités au Client

Parfois, vous avez besoin que le Client MCP et le Serveur MCP collaborent pour atteindre un objectif commun. Vous pouvez avoir un cas où le Serveur nécessite l'aide d'un LLM qui est hébergé sur le client. Pour cette situation, l'échantillonnage est ce que vous devez utiliser.

Explorons quelques cas d'utilisation et comment construire une solution impliquant l'échantillonnage.

## Vue d'ensemble

Dans cette leçon, nous nous concentrons sur l'explication du moment et du lieu pour utiliser l'Échantillonnage et comment le configurer.

## Objectifs d'apprentissage

Dans ce chapitre, nous allons :

- Expliquer ce qu'est l'échantillonnage et quand l'utiliser.
- Montrer comment configurer l'échantillonnage dans MCP.
- Fournir des exemples d'échantillonnage en action.

## Qu'est-ce que l'échantillonnage et pourquoi l'utiliser ?

L'échantillonnage est une fonctionnalité avancée qui fonctionne de la manière suivante :

```mermaid
sequenceDiagram
    participant User
    participant MCP Client
    participant LLM
    participant MCP Server

    User->>MCP Client: Rédiger un article de blog
    MCP Client->>MCP Server: Appel d'outil (brouillon d'article)
    MCP Server->>MCP Client: Demande d'échantillonnage (créer un résumé)
    MCP Client->>LLM: Générer un résumé d'article
    LLM->>MCP Client: Résultat du résumé
    MCP Client->>MCP Server: Réponse d'échantillonnage (résumé)
    MCP Server->>MCP Client: Article complet (brouillon + résumé)
    MCP Client->>User: Article prêt
```
### Requête d'échantillonnage

Ok, maintenant que nous avons une vue d'ensemble d'un scénario crédible, parlons de la requête d'échantillonnage que le serveur renvoie au client. Voici à quoi peut ressembler une telle requête au format JSON-RPC :

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "Create a blog post summary of the following blog post: <BLOG POST>"
        }
      }
    ],
    "modelPreferences": {
      "hints": [
        {
          "name": "claude-3-sonnet"
        }
      ],
      "intelligencePriority": 0.8,
      "speedPriority": 0.5
    },
    "systemPrompt": "You are a helpful assistant.",
    "maxTokens": 100
  }
}
```

Il y a quelques points à souligner ici :

- Prompt, sous content -> text, est notre prompt qui est une instruction pour que le LLM résume le contenu d'un article de blog.

- **modelPreferences**. Cette section est juste cela, une préférence, une recommandation de la configuration à utiliser avec le LLM. L'utilisateur peut choisir de suivre ces recommandations ou de les modifier. Dans ce cas, il y a des recommandations concernant le modèle à utiliser ainsi que la priorité entre vitesse et intelligence.
- **systemPrompt**, c'est votre prompt système normal qui donne une personnalité à votre LLM et contient des instructions de guidage.
- **maxTokens**, c'est une autre propriété qui sert à indiquer combien de tokens sont recommandés pour cette tâche.

### Réponse d'échantillonnage

Cette réponse est ce que le Client MCP finit par renvoyer au Serveur MCP et est le résultat de l'appel du client au LLM, l'attente de cette réponse, puis la construction de ce message. Voici à quoi cela peut ressembler en JSON-RPC :

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "role": "assistant",
    "content": {
      "type": "text",
      "text": "Here's your abstract <ABSTRACT>"
    },
    "model": "gpt-5",
    "stopReason": "endTurn"
  }
}
```

Notez comment la réponse est un résumé de l'article de blog, tout comme nous l'avions demandé. Notez aussi que le `model` utilisé n'est pas celui que nous avons demandé mais "gpt-5" au lieu de "claude-3-sonnet". Cela illustre que l'utilisateur peut changer d'avis sur ce qu'il veut utiliser et que votre requête d'échantillonnage est une recommandation.

Ok, maintenant que nous comprenons le flux principal et une tâche utile pour l'utiliser "création + résumé d'article de blog", voyons ce que nous devons faire pour que cela fonctionne.

### Types de messages

Les messages d'échantillonnage ne sont pas limités au texte mais vous pouvez également envoyer des images et de l'audio. Voici comment le JSON-RPC diffère :

**Texte**

```json
{
  "type": "text",
  "text": "The message content"
}
```

**Contenu d'image**

```json
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/jpeg"
}
```

**Contenu audio**

```json
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```

> NOTE : pour plus d'informations détaillées sur l'échantillonnage, consultez la [documentation officielle](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling)

## Comment configurer l'échantillonnage dans le Client

> Note : si vous ne construisez que le serveur, vous n'avez pas grand-chose à faire ici.

Dans un client, vous devez spécifier la fonctionnalité suivante comme ceci :

```json
{
  "capabilities": {
    "sampling": {}
  }
}
```

Celle-ci sera alors prise en compte lorsque votre client choisi s'initialisera avec le serveur.

## Exemple d'échantillonnage en action - Créer un article de blog

Codons ensemble un serveur d'échantillonnage, nous devrons faire les étapes suivantes :

1. Créer un outil sur le Serveur.
1. Cet outil doit créer une requête d'échantillonnage.
1. L'outil doit attendre la réponse à la requête d'échantillonnage du client.
1. Puis le résultat de l'outil doit être produit.

Voyons le code étape par étape :

### -1- Créer l'outil

**python**

```python
@mcp.tool()
async def create_blog(title: str, content: str, ctx: Context[ServerSession, None]) -> str:
    """Create a blog post and generate a summary"""

```

### -2- Créer une requête d'échantillonnage

Étendez votre outil avec le code suivant :

**python**

```python
post = BlogPost(
        id=len(posts) + 1,
        title=title,
        content=content,
        abstract=""
    )

prompt = f"Create an abstract of the following blog post: title: {title} and draft: {content} "

result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
)

```

### -3- Attendre la réponse et retourner la réponse

**python**

```python
post.abstract = result.content.text

posts.append(post)

# renvoyer le produit complet
return json.dumps({
    "id": post.title,
    "abstract": post.abstract
})
```

### -4- Code complet

**python**

```python
from starlette.applications import Starlette
from starlette.routing import Mount, Host

from mcp.server.fastmcp import Context, FastMCP

from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

import json


from uuid import uuid4
from typing import List
from pydantic import BaseModel


mcp = FastMCP("Blog post generator")

# app = FastAPI()

posts = []

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    abstract: str

posts: List[BlogPost] = []

@mcp.tool()
async def create_blog(title: str, content: str, ctx: Context[ServerSession, None]) -> str:
    """Create a blog post and generate a summary"""

    post = BlogPost(
        id=len(posts) + 1,
        title=title,
        content=content,
        abstract=""
    )

    prompt = f"Create an abstract of the following blog post: title: {title} and draft: {content} "

    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
    )

    post.abstract = result.content.text

    posts.append(post)

    # retourner l'article complet du blog
    return json.dumps({
        "id": post.title,
        "abstract": post.abstract
    })

if __name__ == "__main__":
    print("Starting server...")
    # mcp.run()
    mcp.run(transport="streamable-http")

# exécuter l'application avec : python server.py
```

### -5- Tester dans Visual Studio Code

Pour tester cela dans Visual Studio Code, faites ce qui suit :

1. Démarrez le serveur dans le terminal
1. Ajoutez-le à *mcp.json* (et assurez-vous qu'il est lancé) comme ceci par exemple :

   ```json
   "servers": {
      "blog-server": {
        "type": "http",
        "url": "http://localhost:8000/mcp"
      }
   }
   ```

1. Tapez un prompt :

   ```text
   create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
   ```

1. Laissez l'échantillonnage se faire. La première fois que vous testerez cela, une boîte de dialogue supplémentaire vous sera présentée et que vous devrez accepter, puis vous verrez la boîte de dialogue normale vous demandant de lancer un outil.

1. Inspectez les résultats. Vous verrez les résultats bien rendus dans GitHub Copilot Chat mais vous pouvez aussi inspecter la réponse JSON brute.

**Bonus**. Les outils de Visual Studio Code supportent très bien l'échantillonnage. Vous pouvez configurer l'accès à l'échantillonnage sur votre serveur installé en procédant ainsi :

1. Naviguez vers la section d'extensions.
1. Sélectionnez l'icône d'engrenage pour votre serveur installé dans la section "MCP SERVERS - INSTALLED".
1. Sélectionnez "Configure Model Access", ici vous pouvez choisir quels modèles GitHub Copilot est autorisé à utiliser lors d'échantillonnages. Vous pouvez aussi voir toutes les requêtes d'échantillonnage récentes en sélectionnant "Show Sampling requests".

## Exercice

Dans cet exercice, vous allez construire un échantillonnage légèrement différent, à savoir une intégration d'échantillonnage qui supporte la génération d'une description de produit. Voici votre scénario :

**Scénario** : L'employé du back office d'un e-commerce a besoin d'aide, cela prend trop de temps de générer des descriptions de produit. Par conséquent, vous devez construire une solution où vous pouvez appeler un outil "create_product" avec "title" et "keywords" comme arguments et il devrait produire un produit complet incluant un champ "description" qui doit être rempli par le LLM d'un client.

CONSEIL : utilisez ce que vous avez appris plus tôt pour construire ce serveur et son outil en utilisant une requête d'échantillonnage.

## Solution

[Solution](./solution/README.md)

## Points clés à retenir

L'échantillonnage est une fonctionnalité puissante qui permet au serveur de déléguer des tâches au client lorsqu'il a besoin de l'aide d'un LLM.

## Et après ?

- [Chapitre 4 - Implémentation pratique](../../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avis de non-responsabilité** :  
Ce document a été traduit à l’aide du service de traduction automatisée [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->