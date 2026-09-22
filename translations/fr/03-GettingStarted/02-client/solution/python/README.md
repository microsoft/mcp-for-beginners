# Exécution de cet exemple

Il est recommandé d’installer `uv` mais ce n’est pas obligatoire, voir [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Créer un environnement virtuel

```bash
python -m venv venv
```

## -1- Activer l’environnement virtuel

```bash
venv\Scripts\activate
```

## -2- Installer les dépendances

```bash
pip install "mcp[cli]"
```

## -3- Exécuter l’exemple

```bash
python client.py
```

Vous devriez voir une sortie similaire à :

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->