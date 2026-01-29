## Tests et Débogage

Avant de commencer à tester votre serveur MCP, il est important de bien comprendre les outils disponibles et les bonnes pratiques pour le débogage. Un test efficace garantit que votre serveur fonctionne comme prévu et vous aide à identifier et résoudre rapidement les problèmes. La section suivante présente les approches recommandées pour valider votre implémentation MCP.

## Vue d'ensemble

Cette leçon explique comment choisir la bonne méthode de test et l’outil de test le plus efficace.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- Décrire différentes approches pour les tests.
- Utiliser divers outils pour tester efficacement votre code.

## Tester les serveurs MCP

MCP fournit des outils pour vous aider à tester et déboguer vos serveurs :

- **MCP Inspector** : Un outil en ligne de commande qui peut être utilisé à la fois en mode CLI et en mode visuel.
- **Tests manuels** : Vous pouvez utiliser un outil comme curl pour effectuer des requêtes web, mais tout outil capable d’exécuter des requêtes HTTP convient.
- **Tests unitaires** : Il est possible d’utiliser votre framework de test préféré pour tester les fonctionnalités du serveur et du client.

### Utilisation de MCP Inspector

Nous avons déjà décrit l’utilisation de cet outil dans les leçons précédentes, mais parlons-en brièvement ici. C’est un outil développé en Node.js que vous pouvez utiliser en appelant l’exécutable `npx`, qui téléchargera et installera temporairement l’outil, puis le supprimera une fois la requête terminée.

Le [MCP Inspector](https://github.com/modelcontextprotocol/inspector) vous permet de :

- **Découvrir les capacités du serveur** : détecter automatiquement les ressources, outils et invites disponibles
- **Tester l’exécution des outils** : essayer différents paramètres et voir les réponses en temps réel
- **Consulter les métadonnées du serveur** : examiner les informations, schémas et configurations du serveur

Une utilisation typique de l’outil ressemble à ceci :

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

La commande ci-dessus lance un MCP avec son interface visuelle et ouvre une interface web locale dans votre navigateur. Vous verrez un tableau de bord affichant vos serveurs MCP enregistrés, leurs outils, ressources et invites disponibles. L’interface vous permet de tester l’exécution des outils de manière interactive, d’inspecter les métadonnées du serveur et de visualiser les réponses en temps réel, ce qui facilite la validation et le débogage de vos implémentations MCP.

Voici à quoi cela peut ressembler : ![Inspector](../../../../translated_images/fr/connect.141db0b2bd05f096.webp)

Vous pouvez aussi exécuter cet outil en mode CLI en ajoutant l’attribut `--cli`. Voici un exemple d’exécution en mode "CLI" qui liste tous les outils du serveur :

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Tests manuels

En plus d’utiliser l’outil inspector pour tester les capacités du serveur, une autre approche similaire consiste à utiliser un client capable d’effectuer des requêtes HTTP, comme curl par exemple.

Avec curl, vous pouvez tester directement les serveurs MCP via des requêtes HTTP :

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Comme vous pouvez le voir dans l’exemple ci-dessus, vous utilisez une requête POST pour invoquer un outil avec une charge utile contenant le nom de l’outil et ses paramètres. Choisissez l’approche qui vous convient le mieux. Les outils CLI sont généralement plus rapides à utiliser et peuvent être facilement scriptés, ce qui est utile dans un environnement CI/CD.

### Tests unitaires

Créez des tests unitaires pour vos outils et ressources afin de vous assurer qu’ils fonctionnent comme prévu. Voici un exemple de code de test.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Le code précédent fait ce qui suit :

- Utilise le framework pytest qui vous permet de créer des tests sous forme de fonctions et d’utiliser des assertions.
- Crée un serveur MCP avec deux outils différents.
- Utilise l’instruction `assert` pour vérifier que certaines conditions sont remplies.

Consultez le [fichier complet ici](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

À partir de ce fichier, vous pouvez tester votre propre serveur pour vous assurer que les capacités sont créées comme prévu.

Tous les SDK majeurs disposent de sections de test similaires, vous pouvez donc vous adapter à votre environnement d’exécution choisi.

## Exemples

- [Calculatrice Java](../samples/java/calculator/README.md)
- [Calculatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculatrice JavaScript](../samples/javascript/README.md)
- [Calculatrice TypeScript](../samples/typescript/README.md)
- [Calculatrice Python](../../../../03-GettingStarted/samples/python)

## Ressources supplémentaires

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Et ensuite

- Suivant : [Déploiement](../09-deployment/README.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.