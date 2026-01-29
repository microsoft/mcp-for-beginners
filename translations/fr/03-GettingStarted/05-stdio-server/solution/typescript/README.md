# Serveur MCP stdio - Solution TypeScript

> **⚠️ Important** : Cette solution a été mise à jour pour utiliser le **transport stdio** comme recommandé par la spécification MCP 2025-06-18. Le transport SSE original a été déprécié.

## Aperçu

Cette solution TypeScript montre comment construire un serveur MCP en utilisant le transport stdio actuel. Le transport stdio est plus simple, plus sécurisé et offre de meilleures performances que l'approche SSE dépréciée.

## Prérequis

- Node.js 18+ ou version ultérieure
- Gestionnaire de paquets npm ou yarn

## Instructions d'installation

### Étape 1 : Installer les dépendances

```bash
npm install
```

### Étape 2 : Construire le projet

```bash
npm run build
```

## Lancer le serveur

Le serveur stdio fonctionne différemment de l'ancien serveur SSE. Au lieu de démarrer un serveur web, il communique via stdin/stdout :

```bash
npm start
```

**Important** : Le serveur semblera se figer - c'est normal ! Il attend des messages JSON-RPC via stdin.

## Tester le serveur

### Méthode 1 : Utiliser l'Inspecteur MCP (Recommandé)

```bash
npm run inspector
```

Cela permettra de :
1. Lancer votre serveur en tant que sous-processus
2. Ouvrir une interface web pour les tests
3. Tester tous les outils du serveur de manière interactive

### Méthode 2 : Tester directement en ligne de commande

Vous pouvez également tester en lançant directement l'Inspecteur :

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

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
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Structure du projet

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Principales différences avec SSE

**Transport stdio (Actuel) :**
- ✅ Configuration simplifiée - pas besoin de serveur HTTP
- ✅ Meilleure sécurité - pas de points d'accès HTTP
- ✅ Communication basée sur les sous-processus
- ✅ JSON-RPC via stdin/stdout
- ✅ Meilleures performances

**Transport SSE (Déprécié) :**
- ❌ Nécessitait la configuration d'un serveur Express
- ❌ Requiert une gestion complexe des routes et des sessions
- ❌ Plus de dépendances (Express, gestion HTTP)
- ❌ Considérations de sécurité supplémentaires
- ❌ Maintenant déprécié dans MCP 2025-06-18

## Conseils pour le développement

- Utilisez `console.error()` pour les journaux (jamais `console.log()` car il écrit sur stdout)
- Construisez avec `npm run build` avant de tester
- Testez avec l'Inspecteur pour un débogage visuel
- Assurez-vous que tous les messages JSON sont correctement formatés
- Le serveur gère automatiquement l'arrêt en douceur sur SIGINT/SIGTERM

Cette solution suit la spécification MCP actuelle et illustre les meilleures pratiques pour l'implémentation du transport stdio avec TypeScript.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.