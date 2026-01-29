# Exécuter cet exemple

Il est recommandé d'installer `uv`, mais ce n'est pas obligatoire. Voir [instructions](https://docs.astral.sh/uv/#highlights)

## -1- Installer les dépendances

```bash
npm install
```

## -3- Exécuter l'exemple

```bash
npm run build
```

## -4- Tester l'exemple

Avec le serveur en cours d'exécution dans un terminal, ouvrez un autre terminal et exécutez la commande suivante :

```bash
npm run inspector
```

Cela devrait démarrer un serveur web avec une interface visuelle vous permettant de tester l'exemple.

Une fois le serveur connecté :

- Essayez de lister les outils et exécutez `add`, avec les arguments 2 et 4. Vous devriez voir 6 dans le résultat.
- Allez dans les ressources et le modèle de ressource, puis appelez "greeting". Entrez un nom et vous devriez voir un message de salutation avec le nom que vous avez fourni.

### Tester en mode CLI

L'inspecteur que vous avez lancé est en réalité une application Node.js, et `mcp dev` est un wrapper autour de celle-ci.

Vous pouvez le lancer directement en mode CLI en exécutant la commande suivante :

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Cela listera tous les outils disponibles sur le serveur. Vous devriez voir la sortie suivante :

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Pour invoquer un outil, tapez :

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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