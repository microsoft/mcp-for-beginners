# Exécuter cet exemple

Cet exemple consiste à avoir un LLM côté client. Le LLM nécessite que vous exécutiez cela dans un Codespaces ou que vous configuriez un token d'accès personnel sur GitHub pour que cela fonctionne.

## -1- Installer les dépendances

```bash
npm install
```

## -3- Démarrer le serveur

```bash
npm run build
```

## -4- Lancer le client

```sh
npm run client
```

Vous devriez voir un résultat similaire à :

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.