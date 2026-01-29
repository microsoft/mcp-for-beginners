# Implémentation Python du Model Context Protocol (MCP)

Ce dépôt contient une implémentation Python du Model Context Protocol (MCP), montrant comment créer à la fois une application serveur et une application cliente qui communiquent en utilisant la norme MCP.

## Vue d'ensemble

L’implémentation MCP se compose de deux composants principaux :

1. **Serveur MCP (`server.py`)** - Un serveur qui expose :
   - **Outils** : Fonctions pouvant être appelées à distance
   - **Ressources** : Données pouvant être récupérées
   - **Prompts** : Modèles pour générer des invites pour les modèles de langage

2. **Client MCP (`client.py`)** - Une application cliente qui se connecte au serveur et utilise ses fonctionnalités

## Fonctionnalités

Cette implémentation illustre plusieurs fonctionnalités clés du MCP :

### Outils
- `completion` - Génère des complétions de texte à partir de modèles IA (simulé)
- `add` - Calculatrice simple qui additionne deux nombres

### Ressources
- `models://` - Renvoie des informations sur les modèles IA disponibles
- `greeting://{name}` - Renvoie un message personnalisé pour un nom donné

### Prompts
- `review_code` - Génère un prompt pour la revue de code

## Installation

Pour utiliser cette implémentation MCP, installez les paquets requis :

```powershell
pip install mcp-server mcp-client
```

## Lancement du Serveur et du Client

### Démarrer le Serveur

Lancez le serveur dans une fenêtre de terminal :

```powershell
python server.py
```

Le serveur peut aussi être lancé en mode développement via la CLI MCP :

```powershell
mcp dev server.py
```

Ou installé dans Claude Desktop (si disponible) :

```powershell
mcp install server.py
```

### Lancer le Client

Lancez le client dans une autre fenêtre de terminal :

```powershell
python client.py
```

Cela connectera au serveur et démontrera toutes les fonctionnalités disponibles.

### Utilisation du Client

Le client (`client.py`) illustre toutes les capacités du MCP :

```powershell
python client.py
```

Cela connectera au serveur et testera toutes les fonctionnalités, y compris les outils, ressources et prompts. La sortie affichera :

1. Résultat de l’outil calculatrice (5 + 7 = 12)  
2. Réponse de l’outil completion à la question « What is the meaning of life? »  
3. Liste des modèles IA disponibles  
4. Message personnalisé pour « MCP Explorer »  
5. Modèle de prompt pour la revue de code

## Détails de l’implémentation

Le serveur est implémenté avec l’API `FastMCP`, qui fournit des abstractions de haut niveau pour définir des services MCP. Voici un exemple simplifié de définition des outils :

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Le client utilise la bibliothèque cliente MCP pour se connecter et appeler le serveur :

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## En savoir plus

Pour plus d’informations sur MCP, visitez : https://modelcontextprotocol.io/

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.