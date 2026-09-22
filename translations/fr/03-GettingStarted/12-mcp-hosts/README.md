# Configuration des clients hôtes MCP populaires

> [!NOTE]
> Les configurations d'hôtes pointant vers `/sse` sont des exemples hérités HTTP+SSE pour
> MCP `2025-11-25`. Pour MCP `2026-07-28`, sélectionnez Streamable HTTP dans les hôtes qui
> le supportent et utilisez le point de terminaison configuré par le serveur.

Ce guide couvre comment configurer et utiliser les serveurs MCP avec des applications hôtes d'IA populaires. Chaque hôte a sa propre approche de configuration, mais une fois configurés, ils communiquent tous avec les serveurs MCP en utilisant le protocole standardisé.

## Qu'est-ce qu'un hôte MCP ?

Un **Hôte MCP** est une application d'IA qui peut se connecter aux serveurs MCP pour étendre ses fonctionnalités. Pensez-y comme le « front end » avec lequel les utilisateurs interagissent, tandis que les serveurs MCP fournissent les outils et données en « back end ».

```mermaid
flowchart LR
    User[👤 Utilisateur] --> Host[🖥️ Hôte MCP]
    Host --> S1[Serveur MCP A]
    Host --> S2[Serveur MCP B]
    Host --> S3[Serveur MCP C]
    
    subgraph "Hôtes Populaires"
        H1[Claude Bureau]
        H2[VS Code]
        H3[Curseur]
        H4[Cline]
        H5[Planche à voile]
    end
```

## Prérequis

- Un serveur MCP auquel se connecter (voir [Module 3.1 - Premier serveur](../01-first-server/README.md))
- L'application hôte installée sur votre système
- Une connaissance de base des fichiers de configuration JSON

---

## 1. Claude Desktop

**Claude Desktop** est l'application officielle de bureau d'Anthropic qui prend en charge nativement MCP.

### Installation

1. Téléchargez Claude Desktop depuis [claude.ai/download](https://claude.ai/download)
2. Installez et connectez-vous avec votre compte Anthropic

### Configuration

Claude Desktop utilise un fichier de configuration JSON pour définir les serveurs MCP.

**Emplacement du fichier de configuration :**
- **macOS** : `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows** : `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux** : `~/.config/Claude/claude_desktop_config.json`

**Exemple de configuration :**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Options de configuration

| Champ | Description | Exemple |
|-------|-------------|---------|
| `command` | L'exécutable à lancer | `"python"`, `"node"`, `"npx"` |
| `args` | Arguments en ligne de commande | `["-m", "my_server"]` |
| `env` | Variables d'environnement | `{"API_KEY": "xxx"}` |
| `cwd` | Répertoire de travail | `"/path/to/server"` |

### Tester votre configuration

1. Enregistrez le fichier de configuration
2. Redémarrez complètement Claude Desktop (quitter et rouvrir)
3. Ouvrez une nouvelle conversation
4. Cherchez l'icône 🔌 indiquant les serveurs connectés
5. Essayez de demander à Claude d'utiliser un de vos outils

### Dépannage Claude Desktop

**Serveur n'apparaît pas :**
- Vérifiez la syntaxe du fichier de configuration avec un validateur JSON
- Assurez-vous que le chemin de la commande est correct
- Consultez les logs de Claude Desktop : Aide → Afficher les logs

**Le serveur plante au démarrage :**
- Testez manuellement votre serveur dans le terminal d'abord
- Vérifiez que les variables d'environnement sont correctement définies
- Assurez-vous que toutes les dépendances sont installées

---

## 2. VS Code avec GitHub Copilot

VS Code supporte MCP via les extensions GitHub Copilot Chat.

### Prérequis

1. VS Code 1.99+ installé
2. Extension GitHub Copilot installée
3. Extension GitHub Copilot Chat installée

### Configuration

VS Code utilise `.vscode/mcp.json` dans les paramètres de votre espace de travail ou d'utilisateur.

**Configuration de l'espace de travail** (`.vscode/mcp.json`) :

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Paramètres utilisateur** (`settings.json`) :

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Utilisation de MCP dans VS Code

1. Ouvrez le panneau Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Tapez `@` pour voir les outils MCP disponibles
3. Utilisez un langage naturel pour invoquer les outils : « Calculer 25 * 48 avec la calculatrice »

### Dépannage VS Code

**Les serveurs MCP ne se chargent pas :**
- Vérifiez le panneau Sortie → « MCP » pour les logs d'erreur
- Rechargez la fenêtre : Ctrl+Shift+P → « Developer : Reload Window »
- Vérifiez que le serveur fonctionne en autonome en premier lieu

---

## 3. Cursor

**Cursor** est un éditeur de code pensé IA avec support intégré MCP.

### Installation

1. Téléchargez Cursor depuis [cursor.sh](https://cursor.sh)
2. Installez et connectez-vous

### Configuration

Cursor utilise un format de configuration similaire à Claude Desktop.

**Emplacement du fichier de configuration :**
- **macOS** : `~/.cursor/mcp.json`
- **Windows** : `%USERPROFILE%\.cursor\mcp.json`
- **Linux** : `~/.cursor/mcp.json`

**Exemple de configuration :**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Utilisation de MCP dans Cursor

1. Ouvrez le chat IA de Cursor (Ctrl+L / Cmd+L)
2. Les outils MCP apparaissent automatiquement dans les suggestions
3. Demandez à l'IA d'exécuter des tâches en utilisant les serveurs connectés

---

## 4. Cline (basé sur le terminal)

**Cline** est un client MCP basé sur le terminal, idéal pour les flux de travail en ligne de commande.

### Installation

```bash
npm install -g @anthropic/cline
```

### Configuration

Cline utilise des variables d'environnement et des arguments en ligne de commande.

**Utilisation des variables d'environnement :**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Utilisation des arguments en ligne de commande :**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Fichier de configuration** (`~/.clinerc`) :

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Utilisation de Cline

```bash
# Démarrer une session interactive
cline

# Requête unique avec MCP
cline "Calculate the square root of 144 using the calculator"

# Lister les outils disponibles
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** est un autre éditeur de code propulsé par IA avec support MCP.

### Installation

1. Téléchargez Windsurf depuis [codeium.com/windsurf](https://codeium.com/windsurf)
2. Installez et créez un compte

### Configuration

La configuration de Windsurf est gérée via l'interface des paramètres :

1. Ouvrez les Paramètres (Ctrl+, / Cmd+,)
2. Recherchez « MCP »
3. Cliquez sur « Modifier dans settings.json »

**Exemple de configuration :**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Comparaison des types de transport

Différents hôtes supportent différents mécanismes de transport :

| Hôte | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (entrée/sortie standard) : Idéal pour les serveurs locaux démarrés par l’hôte
**SSE/HTTP** : Idéal pour les serveurs distants ou partagés entre plusieurs clients

---

## Dépannage courant

### Le serveur ne démarre pas

1. **Testez d'abord manuellement le serveur :**
   ```bash
   # Pour Python
   python -m your_server_module
   
   # Pour Node.js
   node /path/to/server/index.js
   ```

2. **Vérifiez le chemin de la commande :**
   - Utilisez des chemins absolus quand c'est possible
   - Assurez-vous que l'exécutable est dans votre PATH

3. **Vérifiez les dépendances :**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Le serveur se connecte mais les outils ne fonctionnent pas

1. **Vérifiez les logs du serveur** - La plupart des hôtes ont des options de journalisation
2. **Vérifiez l'enregistrement des outils** - Utilisez MCP Inspector pour tester
3. **Vérifiez les permissions** - Certains outils nécessitent un accès aux fichiers/réseau

### Les variables d'environnement ne sont pas transmises

- Certains hôtes nettoient les variables d'environnement
- Utilisez explicitement le champ de configuration `env`
- Évitez les données sensibles dans les fichiers de config (utilisez la gestion de secrets)

---

## Bonnes pratiques de sécurité

1. **Ne jamais commettre de clés API** dans les fichiers de configuration
2. **Utiliser des variables d'environnement** pour les données sensibles
3. **Limiter les permissions du serveur** à ce qui est strictement nécessaire
4. **Relire le code du serveur** avant de lui accorder l'accès à votre système
5. **Utiliser des allowlists** pour l'accès au système de fichiers et au réseau

---

## Étapes suivantes

- [3.13 - Débogage avec MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Créez votre premier serveur MCP](../01-first-server/README.md)
- [Module 5 - Sujets avancés](../../05-AdvancedTopics/README.md)

---

## Ressources supplémentaires

- [Documentation MCP Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Extension MCP VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Spécification MCP - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Registre officiel des serveurs MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->