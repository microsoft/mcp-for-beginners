# Exécuter l'exemple

## Installer les dépendances

```sh
npm install
```

## Construire

```sh
npm run build
```

## Générer des jetons

```sh
npm run generate
```

Cela crée un jeton dans un fichier *.env*. Le client lira à partir de ce fichier.

## Exécuter le code

Démarrez le serveur avec :

```sh
npm start
```

Exécutez le client, dans un terminal séparé, avec :

```sh
npm run client
```

Dans le terminal du serveur, vous devriez voir une sortie similaire à :

```text
User exists
User has required scopes
Middleware executed
```

et dans le terminal du client, vous devriez voir une sortie similaire à :

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Modifier les paramètres

Assurons-nous de comprendre les portées. Trouvez le fichier *server.ts* et ce code :

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Cela indique que le jeton transmis doit avoir "User.Read". Changeons cela en "User.Write". Ensuite, exécutez `npm run build` et redémarrez le serveur avec `npm start`. Vous devriez maintenant voir l'authentification échouer car nous n'avons pas cette portée (nous avons User.Read et Admin.Write) :

Le client indique maintenant

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

et vous pouvez voir dans le terminal du serveur qu'il indique :

```text
User exists
```

et qu'il ne va pas au-delà de ce point.

Ajoutez soit cette portée "User.Write" et exécutez `npm run generate`, puis relancez le client, soit modifiez à nouveau le code du serveur.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.