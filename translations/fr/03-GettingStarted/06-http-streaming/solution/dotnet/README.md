# Exécuter cet exemple

## -1- Installer les dépendances

```bash
dotnet restore
```

## -2- Exécuter l'exemple

```bash
dotnet run
```

## -3- Tester l'exemple

Lancez un terminal séparé avant d'exécuter la commande ci-dessous (assurez-vous que le serveur est toujours en cours d'exécution).

Avec le serveur actif dans un terminal, ouvrez un autre terminal et exécutez la commande suivante :

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Cela devrait démarrer un serveur web avec une interface visuelle vous permettant de tester l'exemple.

> Assurez-vous que le **HTTP Streamable** est sélectionné comme type de transport, et que l'URL est `http://localhost:3001/mcp`.

Une fois le serveur connecté :

- essayez de lister les outils et exécutez `add`, avec les arguments 2 et 4, vous devriez voir 6 dans le résultat.
- allez dans ressources et modèle de ressource, et appelez "greeting", entrez un nom et vous devriez voir un message de bienvenue avec le nom que vous avez fourni.

### Tester en mode CLI

Vous pouvez le lancer directement en mode CLI en exécutant la commande suivante :

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Cela listera tous les outils disponibles sur le serveur. Vous devriez voir la sortie suivante :

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Pour invoquer un outil, tapez :

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Vous devriez voir la sortie suivante :

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Il est généralement beaucoup plus rapide d'exécuter l'inspecteur en mode CLI que dans le navigateur.
> En savoir plus sur l'inspecteur [ici](https://github.com/modelcontextprotocol/inspector).

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.