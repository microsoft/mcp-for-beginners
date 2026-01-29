# Exécuter l'exemple

Cet exemple démarre un serveur MCP avec un middleware qui vérifie la présence d'un en-tête Authorization valide.

## Installer les dépendances

```bash
pip install "mcp[cli]" 
```

## Démarrer le serveur

```bash
python server.py
```

démarrez le client dans un autre terminal

```bash
python client.py
```

Vous devriez voir un résultat similaire à :

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Cela signifie que les identifiants envoyés sont acceptés.

Essayez de modifier les identifiants dans `client.py` en "secret-token2", puis vous devriez voir ce texte dans la réponse :

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Cela signifie que vous avez été authentifié (vous aviez des identifiants), mais ils étaient invalides.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.