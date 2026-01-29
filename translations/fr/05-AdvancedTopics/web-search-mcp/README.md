# Leçon : Construire un serveur MCP de recherche web

Ce chapitre montre comment créer un agent IA réel qui s’intègre à des API externes, gère différents types de données, traite les erreurs et orchestre plusieurs outils — le tout dans un format prêt pour la production. Vous découvrirez :

- **Intégration avec des API externes nécessitant une authentification**
- **Gestion de types de données variés provenant de plusieurs points d’accès**
- **Stratégies robustes de gestion des erreurs et de journalisation**
- **Orchestration multi-outils dans un seul serveur**

À la fin, vous aurez une expérience pratique des modèles et bonnes pratiques essentiels pour des applications avancées basées sur l’IA et les LLM.

## Introduction

Dans cette leçon, vous apprendrez à construire un serveur MCP avancé et un client qui étendent les capacités des LLM avec des données web en temps réel grâce à SerpAPI. C’est une compétence clé pour développer des agents IA dynamiques capables d’accéder à des informations à jour sur le web.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- Intégrer des API externes (comme SerpAPI) de manière sécurisée dans un serveur MCP
- Implémenter plusieurs outils pour la recherche web, d’actualités, de produits et Q&R
- Analyser et formater des données structurées pour la consommation par les LLM
- Gérer efficacement les erreurs et les limites de taux des API
- Construire et tester des clients MCP automatisés et interactifs

## Serveur MCP de recherche web

Cette section présente l’architecture et les fonctionnalités du serveur MCP de recherche web. Vous verrez comment FastMCP et SerpAPI sont utilisés ensemble pour étendre les capacités des LLM avec des données web en temps réel.

### Vue d’ensemble

Cette implémentation comprend quatre outils qui illustrent la capacité de MCP à gérer des tâches diverses, pilotées par des API externes, de manière sécurisée et efficace :

- **general_search** : Pour des résultats web généraux
- **news_search** : Pour les dernières actualités
- **product_search** : Pour les données e-commerce
- **qna** : Pour des extraits questions-réponses

### Fonctionnalités
- **Exemples de code** : Inclut des blocs de code spécifiques à Python (et facilement extensibles à d’autres langages) utilisant des pivots de code pour plus de clarté

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Avant de lancer le client, il est utile de comprendre ce que fait le serveur. Le fichier [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implémente le serveur MCP, exposant des outils pour la recherche web, d’actualités, de produits et Q&R en intégrant SerpAPI. Il gère les requêtes entrantes, les appels API, analyse les réponses et renvoie des résultats structurés au client.

Vous pouvez consulter l’implémentation complète dans [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Voici un bref exemple montrant comment le serveur définit et enregistre un outil :

### Serveur Python

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Intégration API externe** : Montre la gestion sécurisée des clés API et des requêtes externes
- **Analyse de données structurées** : Explique comment transformer les réponses API en formats adaptés aux LLM
- **Gestion des erreurs** : Gestion robuste des erreurs avec journalisation appropriée
- **Client interactif** : Inclut des tests automatisés et un mode interactif pour les essais
- **Gestion du contexte** : Utilise MCP Context pour la journalisation et le suivi des requêtes

## Prérequis

Avant de commencer, assurez-vous que votre environnement est correctement configuré en suivant ces étapes. Cela garantira que toutes les dépendances sont installées et que vos clés API sont configurées pour un développement et des tests sans accroc.

- Python 3.8 ou supérieur
- Clé API SerpAPI (Inscrivez-vous sur [SerpAPI](https://serpapi.com/) - offre gratuite disponible)

## Installation

Pour démarrer, suivez ces étapes pour configurer votre environnement :

1. Installez les dépendances avec uv (recommandé) ou pip :

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Créez un fichier `.env` à la racine du projet avec votre clé SerpAPI :

```
SERPAPI_KEY=your_serpapi_key_here
```

## Utilisation

Le serveur MCP de recherche web est le composant central qui expose des outils pour la recherche web, d’actualités, de produits et Q&R en intégrant SerpAPI. Il gère les requêtes entrantes, les appels API, analyse les réponses et renvoie des résultats structurés au client.

Vous pouvez consulter l’implémentation complète dans [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Lancer le serveur

Pour démarrer le serveur MCP, utilisez la commande suivante :

```bash
python server.py
```

Le serveur fonctionnera comme un serveur MCP basé sur stdio auquel le client peut se connecter directement.

### Modes client

Le client (`client.py`) supporte deux modes pour interagir avec le serveur MCP :

- **Mode normal** : Exécute des tests automatisés qui sollicitent tous les outils et vérifient leurs réponses. Utile pour vérifier rapidement que le serveur et les outils fonctionnent comme prévu.
- **Mode interactif** : Lance une interface à menu où vous pouvez sélectionner et appeler manuellement les outils, saisir des requêtes personnalisées et voir les résultats en temps réel. Idéal pour explorer les capacités du serveur et expérimenter différentes entrées.

Vous pouvez consulter l’implémentation complète dans [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Lancer le client

Pour exécuter les tests automatisés (cela démarrera automatiquement le serveur) :

```bash
python client.py
```

Ou lancez en mode interactif :

```bash
python client.py --interactive
```

### Tester avec différentes méthodes

Il existe plusieurs façons de tester et d’interagir avec les outils fournis par le serveur, selon vos besoins et votre flux de travail.

#### Écrire des scripts de test personnalisés avec le SDK Python MCP
Vous pouvez aussi créer vos propres scripts de test en utilisant le SDK Python MCP :

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

Dans ce contexte, un « script de test » désigne un programme Python personnalisé que vous écrivez pour agir comme client du serveur MCP. Plutôt qu’un test unitaire formel, ce script vous permet de vous connecter au serveur de manière programmatique, d’appeler n’importe quel outil avec les paramètres de votre choix et d’inspecter les résultats. Cette approche est utile pour :
- Prototyper et expérimenter des appels d’outils
- Valider la réponse du serveur à différentes entrées
- Automatiser des appels d’outils répétés
- Construire vos propres workflows ou intégrations au-dessus du serveur MCP

Vous pouvez utiliser ces scripts pour tester rapidement de nouvelles requêtes, déboguer le comportement des outils, ou même comme point de départ pour une automatisation plus avancée. Voici un exemple d’utilisation du SDK Python MCP pour créer un tel script :

## Description des outils

Vous pouvez utiliser les outils suivants fournis par le serveur pour effectuer différents types de recherches et requêtes. Chaque outil est décrit ci-dessous avec ses paramètres et un exemple d’utilisation.

Cette section détaille chaque outil disponible et leurs paramètres.

### general_search

Effectue une recherche web générale et renvoie des résultats formatés.

**Comment appeler cet outil :**

Vous pouvez appeler `general_search` depuis votre propre script en utilisant le SDK Python MCP, ou de manière interactive via l’Inspector ou le mode client interactif. Voici un exemple de code utilisant le SDK :

# [Exemple Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Sinon, en mode interactif, sélectionnez `general_search` dans le menu et saisissez votre requête lorsqu’on vous le demande.

**Paramètres :**
- `query` (chaîne) : La requête de recherche

**Exemple de requête :**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Recherche des articles d’actualité récents liés à une requête.

**Comment appeler cet outil :**

Vous pouvez appeler `news_search` depuis votre propre script en utilisant le SDK Python MCP, ou de manière interactive via l’Inspector ou le mode client interactif. Voici un exemple de code utilisant le SDK :

# [Exemple Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Sinon, en mode interactif, sélectionnez `news_search` dans le menu et saisissez votre requête lorsqu’on vous le demande.

**Paramètres :**
- `query` (chaîne) : La requête de recherche

**Exemple de requête :**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Recherche des produits correspondant à une requête.

**Comment appeler cet outil :**

Vous pouvez appeler `product_search` depuis votre propre script en utilisant le SDK Python MCP, ou de manière interactive via l’Inspector ou le mode client interactif. Voici un exemple de code utilisant le SDK :

# [Exemple Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Sinon, en mode interactif, sélectionnez `product_search` dans le menu et saisissez votre requête lorsqu’on vous le demande.

**Paramètres :**
- `query` (chaîne) : La requête de recherche de produit

**Exemple de requête :**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Obtient des réponses directes à des questions depuis les moteurs de recherche.

**Comment appeler cet outil :**

Vous pouvez appeler `qna` depuis votre propre script en utilisant le SDK Python MCP, ou de manière interactive via l’Inspector ou le mode client interactif. Voici un exemple de code utilisant le SDK :

# [Exemple Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Sinon, en mode interactif, sélectionnez `qna` dans le menu et saisissez votre question lorsqu’on vous le demande.

**Paramètres :**
- `question` (chaîne) : La question à laquelle trouver une réponse

**Exemple de requête :**

```json
{
  "question": "what is artificial intelligence"
}
```

## Détails du code

Cette section fournit des extraits de code et des références pour les implémentations serveur et client.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Consultez [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) et [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) pour les détails complets de l’implémentation.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Concepts avancés dans cette leçon

Avant de commencer à construire, voici quelques concepts avancés importants qui apparaîtront tout au long de ce chapitre. Les comprendre vous aidera à suivre, même si vous les découvrez :

- **Orchestration multi-outils** : Cela signifie exécuter plusieurs outils différents (comme recherche web, actualités, produits et Q&R) dans un seul serveur MCP. Cela permet à votre serveur de gérer une variété de tâches, pas seulement une.
- **Gestion des limites de taux API** : Beaucoup d’API externes (comme SerpAPI) limitent le nombre de requêtes que vous pouvez faire dans un certain temps. Un bon code vérifie ces limites et les gère avec élégance, pour que votre application ne plante pas si vous atteignez une limite.
- **Analyse de données structurées** : Les réponses API sont souvent complexes et imbriquées. Ce concept consiste à transformer ces réponses en formats propres et faciles à utiliser, adaptés aux LLM ou autres programmes.
- **Récupération d’erreur** : Parfois, ça coince — peut-être un problème réseau, ou l’API ne renvoie pas ce que vous attendez. La récupération d’erreur signifie que votre code peut gérer ces problèmes et fournir un retour utile, au lieu de planter.
- **Validation des paramètres** : Il s’agit de vérifier que toutes les entrées de vos outils sont correctes et sûres à utiliser. Cela inclut la définition de valeurs par défaut et la vérification des types, ce qui aide à éviter bugs et confusions.

Cette section vous aidera à diagnostiquer et résoudre les problèmes courants que vous pourriez rencontrer en travaillant avec le serveur MCP de recherche web. Si vous rencontrez des erreurs ou un comportement inattendu, cette section de dépannage propose des solutions aux problèmes les plus fréquents. Consultez ces conseils avant de demander de l’aide — ils résolvent souvent rapidement les problèmes.

## Dépannage

Lorsque vous travaillez avec le serveur MCP de recherche web, il est normal de rencontrer parfois des problèmes — c’est courant lors du développement avec des API externes et de nouveaux outils. Cette section propose des solutions pratiques aux problèmes les plus fréquents, pour vous remettre rapidement sur les rails. Si vous avez une erreur, commencez ici : les conseils ci-dessous traitent des problèmes que la plupart des utilisateurs rencontrent et peuvent souvent résoudre votre souci sans aide supplémentaire.

### Problèmes courants

Voici quelques-uns des problèmes les plus fréquents rencontrés par les utilisateurs, avec des explications claires et des étapes pour les résoudre :

1. **Clé SERPAPI_KEY manquante dans le fichier .env**
   - Si vous voyez l’erreur `SERPAPI_KEY environment variable not found`, cela signifie que votre application ne trouve pas la clé API nécessaire pour accéder à SerpAPI. Pour corriger cela, créez un fichier nommé `.env` à la racine de votre projet (s’il n’existe pas déjà) et ajoutez une ligne comme `SERPAPI_KEY=your_serpapi_key_here`. Veillez à remplacer `your_serpapi_key_here` par votre clé réelle obtenue sur le site SerpAPI.

2. **Erreurs de module introuvable**
   - Des erreurs telles que `ModuleNotFoundError: No module named 'httpx'` indiquent qu’un paquet Python requis est manquant. Cela arrive généralement si vous n’avez pas installé toutes les dépendances. Pour résoudre cela, lancez `pip install -r requirements.txt` dans votre terminal pour installer tout ce dont votre projet a besoin.

3. **Problèmes de connexion**
   - Si vous obtenez une erreur comme `Error during client execution`, cela signifie souvent que le client ne peut pas se connecter au serveur, ou que le serveur ne fonctionne pas comme prévu. Vérifiez que le client et le serveur sont des versions compatibles, que `server.py` est bien présent et lancé dans le bon répertoire. Redémarrer le serveur et le client peut aussi aider.

4. **Erreurs SerpAPI**
   - Voir `Search API returned error status: 401` signifie que votre clé SerpAPI est manquante, incorrecte ou expirée. Rendez-vous sur votre tableau de bord SerpAPI, vérifiez votre clé et mettez à jour votre fichier `.env` si nécessaire. Si votre clé est correcte mais que l’erreur persiste, vérifiez si votre quota gratuit est épuisé.

### Mode Debug

Par défaut, l’application ne journalise que les informations importantes. Si vous souhaitez voir plus de détails sur ce qui se passe (par exemple pour diagnostiquer des problèmes complexes), vous pouvez activer le mode DEBUG. Cela affichera beaucoup plus d’informations à chaque étape.

**Exemple : sortie normale**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Exemple : sortie DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Notez que le mode DEBUG inclut des lignes supplémentaires sur les requêtes HTTP, les réponses et d’autres détails internes. Cela peut être très utile pour le dépannage.
Pour activer le mode DEBUG, définissez le niveau de journalisation sur DEBUG en haut de votre `client.py` ou `server.py` :

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Et ensuite

- [5.10 Streaming en temps réel](../mcp-realtimestreaming/README.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.