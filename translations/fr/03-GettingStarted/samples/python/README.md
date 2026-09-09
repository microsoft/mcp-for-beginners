# Serveur Calculatrice MCP (Python)



Une implémentation simple d'un serveur Model Context Protocol (MCP) en Python qui fournit une fonctionnalité basique de calculatrice.


## Installation

Installez les dépendances requises :

```bash
pip install -r requirements.txt
```

Ou installez directement le SDK Python MCP :

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Utilisation

### Lancer le serveur

Le serveur est conçu pour être utilisé par les clients MCP (comme Claude Desktop). Pour démarrer le serveur :

```bash
python mcp_calculator_server.py
```

**Note** : Lorsqu'il est exécuté directement dans un terminal, vous verrez des erreurs de validation JSON-RPC. C’est un comportement normal – le serveur attend des messages clients MCP correctement formatés.

### Tester les fonctions

Pour tester que les fonctions de la calculatrice fonctionnent correctement :

```bash
python test_calculator.py
```

## Dépannage

### Erreurs d'importation

Si vous voyez `ModuleNotFoundError: No module named 'mcp'`, installez le SDK Python MCP :

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Erreurs JSON-RPC lors de l'exécution directe

Des erreurs comme "Invalid JSON: EOF while parsing a value" lors de l'exécution directe du serveur sont attendues. Le serveur nécessite des messages clients MCP, pas une saisie directe depuis le terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->