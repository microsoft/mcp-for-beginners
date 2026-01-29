# 📘 Solution de l’exercice : Étendre votre serveur MCP de calculatrice avec un outil de racine carrée

## Vue d’ensemble
Dans cet exercice, vous avez amélioré votre serveur MCP de calculatrice en ajoutant un nouvel outil qui calcule la racine carrée d’un nombre. Cette extension permet à votre agent IA de gérer des requêtes mathématiques plus avancées, comme « Quelle est la racine carrée de 16 ? » ou « Calcule √49 », en utilisant des instructions en langage naturel.

## 🛠️ Implémentation de l’outil racine carrée
Pour ajouter cette fonctionnalité, vous avez défini une nouvelle fonction outil dans votre fichier server.py. Voici l’implémentation :

```python
"""
Sample MCP Calculator Server implementation in Python.

This module demonstrates how to create a simple MCP server with calculator tools
that can perform basic arithmetic operations (add, subtract, multiply, divide).
"""

from mcp.server.fastmcp import FastMCP
import math

server = FastMCP("calculator")

@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b

@server.tool()
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@server.tool()
def sqrt(a: float) -> float:
    """
    Return the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(a)
```

## 🔍 Comment ça fonctionne

- **Importer le module `math`** : Pour effectuer des opérations mathématiques plus complexes que l’arithmétique de base, Python propose le module intégré `math`. Ce module contient de nombreuses fonctions et constantes mathématiques. En l’important avec `import math`, vous accédez à des fonctions comme `math.sqrt()`, qui calcule la racine carrée d’un nombre.
- **Définition de la fonction** : Le décorateur `@server.tool()` enregistre la fonction `sqrt` comme un outil accessible par votre agent IA.
- **Paramètre d’entrée** : La fonction prend un seul argument `a` de type `float`.
- **Gestion des erreurs** : Si `a` est négatif, la fonction lève une `ValueError` pour éviter de calculer la racine carrée d’un nombre négatif, ce qui n’est pas pris en charge par `math.sqrt()`.
- **Valeur de retour** : Pour des entrées non négatives, la fonction retourne la racine carrée de `a` en utilisant la méthode intégrée `math.sqrt()` de Python.

## 🔄 Redémarrage du serveur
Après avoir ajouté le nouvel outil `sqrt`, il est essentiel de redémarrer votre serveur MCP pour que l’agent reconnaisse et puisse utiliser cette nouvelle fonctionnalité.

## 💬 Exemples d’instructions pour tester le nouvel outil
Voici quelques exemples d’instructions en langage naturel que vous pouvez utiliser pour tester la fonctionnalité racine carrée :

- « Quelle est la racine carrée de 25 ? »
- « Calcule la racine carrée de 81. »
- « Trouve la racine carrée de 0. »
- « Quelle est la racine carrée de 2,25 ? »

Ces instructions devraient déclencher l’appel de l’outil `sqrt` par l’agent et retourner les résultats corrects.

## ✅ Résumé
En réalisant cet exercice, vous avez :

- Étendu votre serveur MCP de calculatrice avec un nouvel outil `sqrt`.
- Permis à votre agent IA de gérer les calculs de racine carrée via des instructions en langage naturel.
- Pratiqué l’ajout de nouveaux outils et le redémarrage du serveur pour intégrer des fonctionnalités supplémentaires.

N’hésitez pas à expérimenter davantage en ajoutant d’autres outils mathématiques, comme l’exponentiation ou les fonctions logarithmiques, pour continuer à enrichir les capacités de votre agent !

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.