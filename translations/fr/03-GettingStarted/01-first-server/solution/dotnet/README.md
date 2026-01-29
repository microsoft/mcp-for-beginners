# Exécuter cet exemple

## -1- Installer les dépendances

```bash
dotnet restore
```

## -3- Exécuter l'exemple

```bash
dotnet run
```

## -4- Tester l'exemple

Avec le serveur en cours d'exécution dans un terminal, ouvrez un autre terminal et exécutez la commande suivante :

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Cela devrait démarrer un serveur web avec une interface visuelle vous permettant de tester l'exemple.

Une fois le serveur connecté :

- Essayez de lister les outils et exécutez `add`, avec les arguments 2 et 4, vous devriez voir 6 dans le résultat.
- Allez dans les ressources et le modèle de ressource, appelez "greeting", entrez un nom et vous devriez voir un message de bienvenue avec le nom que vous avez fourni.

### Tester en mode CLI

Vous pouvez le lancer directement en mode CLI en exécutant la commande suivante :

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Cela listera tous les outils disponibles sur le serveur. Vous devriez voir la sortie suivante :

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
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
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Vous devriez voir la sortie suivante :

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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