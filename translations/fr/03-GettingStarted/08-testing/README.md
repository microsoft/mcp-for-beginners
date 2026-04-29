## Tests et débogage

Avant de commencer à tester votre serveur MCP, il est important de comprendre les outils disponibles et les meilleures pratiques pour le débogage. Des tests efficaces garantissent que votre serveur se comporte comme prévu et vous aident à identifier et résoudre rapidement les problèmes. La section suivante décrit les approches recommandées pour valider votre implémentation MCP.

## Aperçu

Cette leçon explique comment choisir la bonne approche de test et l’outil de test le plus efficace.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- Décrire différentes approches pour les tests.
- Utiliser différents outils pour tester efficacement votre code.


## Test des serveurs MCP

MCP fournit des outils pour vous aider à tester et déboguer vos serveurs :

- **MCP Inspector** : Un outil en ligne de commande qui peut être utilisé à la fois comme outil CLI et comme outil visuel.
- **Tests manuels** : Vous pouvez utiliser un outil tel que curl pour exécuter des requêtes web, mais tout outil capable d’exécuter du HTTP convient.
- **Tests unitaires** : Il est possible d’utiliser votre framework de test préféré pour tester les fonctionnalités tant du serveur que du client.

### Utilisation de MCP Inspector

Nous avons décrit l’utilisation de cet outil dans les leçons précédentes, mais parlons-en un peu à un niveau général. C’est un outil construit en Node.js, que vous pouvez utiliser en appelant l’exécutable `npx` qui téléchargera et installera temporairement l’outil avant de le nettoyer une fois votre requête terminée.

Le [MCP Inspector](https://github.com/modelcontextprotocol/inspector) vous aide à :

- **Découvrir les capacités du serveur** : détecter automatiquement les ressources, outils et invites disponibles
- **Tester l’exécution des outils** : essayer différents paramètres et voir les réponses en temps réel
- **Afficher les métadonnées du serveur** : examiner les informations du serveur, les schémas et les configurations

Une exécution typique de l’outil ressemble à ceci :

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

La commande ci-dessus lance un MCP et son interface visuelle et démarre une interface web locale dans votre navigateur. Vous pouvez vous attendre à voir un tableau de bord affichant vos serveurs MCP enregistrés, leurs outils, ressources et invites disponibles. L’interface vous permet de tester de manière interactive l’exécution des outils, d’inspecter les métadonnées du serveur et de voir les réponses en temps réel, ce qui facilite la validation et le débogage de vos implémentations de serveur MCP.

Voici à quoi cela peut ressembler : ![Inspector](../../../../translated_images/fr/connect.141db0b2bd05f096.webp)

Vous pouvez également exécuter cet outil en mode CLI, auquel cas vous ajoutez l’attribut `--cli`. Voici un exemple d’exécution de l’outil en mode « CLI » qui liste tous les outils sur le serveur :

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Test manuel

En plus de lancer l’outil inspector pour tester les capacités du serveur, une autre approche similaire est d’exécuter un client capable d’utiliser HTTP comme, par exemple, curl.

Avec curl, vous pouvez tester les serveurs MCP directement via des requêtes HTTP :

```bash
# Exemple : Métadonnées du serveur de test
curl http://localhost:3000/v1/metadata

# Exemple : Exécuter un outil
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Comme vous pouvez le voir dans l’exemple ci-dessus d’utilisation de curl, vous utilisez une requête POST pour invoquer un outil en envoyant une charge utile comprenant le nom de l’outil et ses paramètres. Utilisez l’approche qui vous convient le mieux. Les outils CLI sont généralement plus rapides à utiliser et se prêtent facilement à l’écriture de scripts, ce qui peut être utile dans un environnement CI/CD.

### Tests unitaires

Créez des tests unitaires pour vos outils et ressources afin de garantir qu’ils fonctionnent comme prévu. Voici un exemple de code de test.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Marquer tout le module pour les tests asynchrones
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Créer quelques outils de test
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Tester sans paramètre de curseur (omission)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Tester avec cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Tester avec cursor en tant que chaîne de caractères
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Tester avec un curseur chaîne vide
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Le code précédent fait ce qui suit :

- Utilise le framework pytest qui vous permet de créer des tests sous forme de fonctions et d’utiliser des assertions.
- Crée un serveur MCP avec deux outils différents.
- Utilise l’instruction `assert` pour vérifier que certaines conditions sont remplies.

Consultez le [fichier complet ici](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py).

À partir du fichier ci-dessus, vous pouvez tester votre propre serveur pour assurer que les capacités sont créées comme elles doivent l’être.

Tous les principaux SDK ont des sections de test similaires afin que vous puissiez vous adapter à votre environnement d’exécution choisi.

## Exemples

- [Calculatrice Java](../samples/java/calculator/README.md)
- [Calculatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculatrice JavaScript](../samples/javascript/README.md)
- [Calculatrice TypeScript](../samples/typescript/README.md)
- [Calculatrice Python](../../../../03-GettingStarted/samples/python)

## Ressources supplémentaires

- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)

## Et ensuite

- Suivant : [Déploiement](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue natale doit être considéré comme la source faisant foi. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous déclinons toute responsabilité pour tout malentendu ou mauvaise interprétation résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->