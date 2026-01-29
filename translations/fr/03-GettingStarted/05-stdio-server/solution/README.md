# Solutions de Serveur MCP stdio

> **⚠️ Important** : Ces solutions ont été mises à jour pour utiliser le **transport stdio** conformément aux recommandations de la spécification MCP du 18/06/2025. Le transport SSE (Server-Sent Events) original a été déprécié.

Voici les solutions complètes pour construire des serveurs MCP en utilisant le transport stdio dans chaque environnement d'exécution :

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Implémentation complète d'un serveur stdio
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Serveur stdio Python avec asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Serveur stdio .NET avec injection de dépendances

Chaque solution illustre :
- La configuration du transport stdio
- La définition des outils du serveur
- Une gestion correcte des messages JSON-RPC
- L'intégration avec des clients MCP comme Claude

Toutes les solutions respectent la spécification MCP actuelle et utilisent le transport stdio recommandé pour des performances et une sécurité optimales.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.