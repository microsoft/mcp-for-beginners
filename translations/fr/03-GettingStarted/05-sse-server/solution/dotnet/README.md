<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2a58caa6e11faa09470b7f81e6729652",
  "translation_date": "2025-07-13T20:07:36+00:00",
  "source_file": "03-GettingStarted/05-sse-server/solution/dotnet/README.md",
  "language_code": "fr"
}
-->
# Exécuter cet exemple

## -1- Installer les dépendances

```bash
dotnet restore
```

## -2- Lancer l'exemple

```bash
dotnet run
```

## -3- Tester l'exemple

Ouvrez un terminal séparé avant d'exécuter la commande ci-dessous (assurez-vous que le serveur est toujours en fonctionnement).

Avec le serveur en marche dans un terminal, ouvrez un autre terminal et lancez la commande suivante :

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Cela devrait démarrer un serveur web avec une interface visuelle vous permettant de tester l'exemple.

> Assurez-vous que le **SSE** est sélectionné comme type de transport, et que l'URL est `http://localhost:3001/sse`.

Une fois le serveur connecté :

- essayez de lister les outils et exécutez `add` avec les arguments 2 et 4, vous devriez voir 6 en résultat.
- allez dans resources et resource template, appelez "greeting", saisissez un nom et vous devriez voir un message de bienvenue avec le nom que vous avez fourni.

### Tester en mode CLI

Vous pouvez le lancer directement en mode CLI en exécutant la commande suivante :

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Cela affichera la liste de tous les outils disponibles sur le serveur. Vous devriez voir la sortie suivante :

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

> ![!TIP]
> Il est généralement beaucoup plus rapide d’exécuter l’inspector en mode CLI que dans le navigateur.
> Pour en savoir plus sur l’inspector, consultez [ici](https://github.com/modelcontextprotocol/inspector).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.