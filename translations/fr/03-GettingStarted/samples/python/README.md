# Serveur MCP Calculator (Python)

Une implémentation simple du serveur Model Context Protocol (MCP) en Python offrant des fonctionnalités de calcul de base.

## Installation

Installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

Ou installez directement le SDK MCP Python :

```bash
pip install mcp>=1.18.0
```

## Utilisation

### Lancer le serveur

Le serveur est conçu pour être utilisé par des clients MCP (comme Claude Desktop). Pour démarrer le serveur :

```bash
python mcp_calculator_server.py
```

**Note** : Lorsqu'il est exécuté directement dans un terminal, vous verrez des erreurs de validation JSON-RPC. C'est un comportement normal - le serveur attend des messages correctement formatés provenant d'un client MCP.

### Tester les fonctions

Pour vérifier que les fonctions du calculateur fonctionnent correctement :

```bash
python test_calculator.py
```

## Résolution des problèmes

### Erreurs d'importation

Si vous voyez `ModuleNotFoundError: No module named 'mcp'`, installez le SDK MCP Python :

```bash
pip install mcp>=1.18.0
```

### Erreurs JSON-RPC lors de l'exécution directe

Des erreurs comme "Invalid JSON: EOF while parsing a value" lors de l'exécution directe du serveur sont normales. Le serveur nécessite des messages provenant d'un client MCP, et non une entrée directe dans le terminal.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.