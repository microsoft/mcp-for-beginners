# Service de Calculatrice Basique MCP

Ce service fournit des opérations de calcul basiques via le Model Context Protocol (MCP). Il est conçu comme un exemple simple pour les débutants qui souhaitent apprendre les implémentations MCP.

Pour plus d’informations, voir [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Fonctionnalités

Ce service de calculatrice offre les capacités suivantes :

1. **Opérations arithmétiques de base** :
   - Addition de deux nombres
   - Soustraction d’un nombre par rapport à un autre
   - Multiplication de deux nombres
   - Division d’un nombre par un autre (avec vérification de la division par zéro)

## Utilisation du type `stdio`
  
## Configuration

1. **Configurer les serveurs MCP** :
   - Ouvrez votre espace de travail dans VS Code.
   - Créez un fichier `.vscode/mcp.json` dans le dossier de votre espace de travail pour configurer les serveurs MCP. Exemple de configuration :

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Il vous sera demandé d’indiquer la racine du dépôt GitHub, que vous pouvez obtenir avec la commande `git rev-parse --show-toplevel`.

## Utilisation du Service

Le service expose les points d’API suivants via le protocole MCP :

- `add(a, b)` : Additionne deux nombres
- `subtract(a, b)` : Soustrait le second nombre du premier
- `multiply(a, b)` : Multiplie deux nombres
- `divide(a, b)` : Divise le premier nombre par le second (avec vérification de zéro)
- isPrime(n) : Vérifie si un nombre est premier

## Test avec Github Copilot Chat dans VS Code

1. Essayez de faire une requête au service en utilisant le protocole MCP. Par exemple, vous pouvez demander :
   - « Additionne 5 et 3 »
   - « Soustrais 10 de 4 »
   - « Multiplie 6 et 7 »
   - « Divise 8 par 2 »
   - « Est-ce que 37854 est premier ? »
   - « Quels sont les 3 nombres premiers avant et après 4242 ? »
2. Pour vous assurer que les outils sont utilisés, ajoutez #MyCalculator dans la requête. Par exemple :
   - « Additionne 5 et 3 #MyCalculator »
   - « Soustrais 10 de 4 #MyCalculator »

## Version Conteneurisée

La solution précédente est idéale lorsque vous avez le SDK .NET installé et que toutes les dépendances sont en place. Cependant, si vous souhaitez partager la solution ou l’exécuter dans un environnement différent, vous pouvez utiliser la version conteneurisée.

1. Démarrez Docker et assurez-vous qu’il fonctionne.
1. Depuis un terminal, placez-vous dans le dossier `03-GettingStarted\samples\csharp\src`
1. Pour construire l’image Docker du service calculatrice, exécutez la commande suivante (remplacez `<YOUR-DOCKER-USERNAME>` par votre nom d’utilisateur Docker Hub) :
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Une fois l’image construite, téléchargeons-la sur Docker Hub. Lancez la commande suivante :
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Utiliser la Version Dockerisée

1. Dans le fichier `.vscode/mcp.json`, remplacez la configuration du serveur par ce qui suit :
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   En regardant la configuration, vous pouvez voir que la commande est `docker` et les arguments sont `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. L’option `--rm` garantit que le conteneur est supprimé après son arrêt, et l’option `-i` permet d’interagir avec l’entrée standard du conteneur. Le dernier argument est le nom de l’image que nous venons de construire et de pousser sur Docker Hub.

## Tester la Version Dockerisée

Démarrez le serveur MCP en cliquant sur le petit bouton Démarrer au-dessus de `"mcp-calc": {`, et comme précédemment, vous pouvez demander au service calculatrice de faire des calculs pour vous.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.