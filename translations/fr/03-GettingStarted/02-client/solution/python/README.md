# Exécuter cet exemple

Il est recommandé d’installer `uv` mais ce n’est pas obligatoire, voir [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Créer un environnement virtuel

```bash
python -m venv venv
```

## -1- Activer l’environnement virtuel

```bash
venv\Scrips\activate
```

## -2- Installer les dépendances

```bash
pip install "mcp[cli]"
```

## -3- Lancer l’exemple


```bash
python client.py
```

Vous devriez voir une sortie similaire à :

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.