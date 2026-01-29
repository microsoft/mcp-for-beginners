# Exécuter l'exemple

## Créer l'environnement

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installer les dépendances

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Générer un jeton

Vous devrez générer un jeton que le client utilisera pour communiquer avec le serveur.

Appelez :

```sh
python util.py
```

## Exécuter le code

Exécutez le code avec :

```sh
python server.py
```

Dans un terminal séparé, tapez :

```sh
python client.py
```

Dans le terminal du serveur, vous devriez voir quelque chose comme :

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Dans la fenêtre du client, vous devriez voir un texte similaire à :

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Cela signifie que tout fonctionne.

### Modifier les informations pour voir une erreur

Repérez ce code dans *server.py* :

```python
 if not has_scope(has_header, "Admin.Write"):
```

Modifiez-le pour qu'il indique "User.Write". Votre jeton actuel n'a pas ce niveau de permission, donc si vous redémarrez le serveur et essayez de relancer le client, vous devriez voir une erreur similaire à la suivante dans le terminal du serveur :

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Vous pouvez soit revenir à votre code serveur précédent, soit générer un nouveau jeton contenant cette portée supplémentaire, à vous de choisir.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.