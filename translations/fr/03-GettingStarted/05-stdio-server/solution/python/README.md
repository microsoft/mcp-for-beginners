# Serveur MCP stdio - Solution Python

> **⚠️ Important** : Cette solution a été mise à jour pour utiliser le **transport stdio** comme recommandé par la spécification MCP 2025-06-18. Le transport SSE original a été déprécié.

## Vue d'ensemble

Cette solution Python montre comment construire un serveur MCP en utilisant le transport stdio actuel. Le transport stdio est plus simple, plus sécurisé et offre de meilleures performances que l'approche SSE dépréciée.

## Prérequis

- Python 3.8 ou version ultérieure
- Il est recommandé d'installer `uv` pour la gestion des packages, voir [instructions](https://docs.astral.sh/uv/#highlights)

## Instructions d'installation

### Étape 1 : Créer un environnement virtuel

```bash
python -m venv venv
```

### Étape 2 : Activer l'environnement virtuel

**Windows :**
```bash
venv\Scripts\activate
```

**macOS/Linux :**
```bash
source venv/bin/activate
```

### Étape 3 : Installer les dépendances

```bash
pip install mcp
```

## Lancer le serveur

Le serveur stdio fonctionne différemment de l'ancien serveur SSE. Au lieu de démarrer un serveur web, il communique via stdin/stdout :

```bash
python server.py
```

**Important** : Le serveur semblera se figer - c'est normal ! Il attend des messages JSON-RPC via stdin.

## Tester le serveur

### Méthode 1 : Utiliser l'inspecteur MCP (Recommandé)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Cela permettra :
1. De lancer votre serveur en tant que sous-processus
2. D'ouvrir une interface web pour les tests
3. De tester tous les outils du serveur de manière interactive

### Méthode 2 : Test direct avec JSON-RPC

Vous pouvez également tester en envoyant directement des messages JSON-RPC :

1. Démarrez le serveur : `python server.py`
2. Envoyez un message JSON-RPC (exemple) :

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Le serveur répondra avec les outils disponibles

### Outils disponibles

Le serveur propose les outils suivants :

- **add(a, b)** : Additionne deux nombres
- **multiply(a, b)** : Multiplie deux nombres  
- **get_greeting(name)** : Génère un message de salutation personnalisé
- **get_server_info()** : Fournit des informations sur le serveur

### Tester avec Claude Desktop

Pour utiliser ce serveur avec Claude Desktop, ajoutez cette configuration à votre fichier `claude_desktop_config.json` :

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Principales différences avec SSE

**Transport stdio (Actuel) :**
- ✅ Configuration simplifiée - pas besoin de serveur web
- ✅ Meilleure sécurité - pas de points de terminaison HTTP
- ✅ Communication basée sur des sous-processus
- ✅ JSON-RPC via stdin/stdout
- ✅ Meilleures performances

**Transport SSE (Déprécié) :**
- ❌ Nécessitait la configuration d'un serveur HTTP
- ❌ Requiert un framework web (Starlette/FastAPI)
- ❌ Gestion plus complexe des routages et des sessions
- ❌ Considérations de sécurité supplémentaires
- ❌ Maintenant déprécié dans MCP 2025-06-18

## Conseils pour le débogage

- Utilisez `stderr` pour les journaux (jamais `stdout`)
- Testez avec l'inspecteur pour un débogage visuel
- Assurez-vous que tous les messages JSON sont délimités par des sauts de ligne
- Vérifiez que le serveur démarre sans erreurs

Cette solution suit la spécification MCP actuelle et illustre les meilleures pratiques pour l'implémentation du transport stdio.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.