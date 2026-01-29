# MCP-stdio-Serverlösungen

> **⚠️ Wichtig**: Diese Lösungen wurden aktualisiert, um den **stdio-Transport** gemäß der MCP-Spezifikation vom 18.06.2025 zu verwenden. Der ursprüngliche SSE-Transport (Server-Sent Events) wurde eingestellt.

Hier sind die vollständigen Lösungen für den Aufbau von MCP-Servern mit dem stdio-Transport in den jeweiligen Laufzeitumgebungen:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Vollständige stdio-Server-Implementierung
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python-stdio-Server mit asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET-stdio-Server mit Dependency Injection

Jede Lösung zeigt:
- Einrichtung des stdio-Transports
- Definition von Server-Tools
- Korrekte JSON-RPC-Nachrichtenverarbeitung
- Integration mit MCP-Clients wie Claude

Alle Lösungen entsprechen der aktuellen MCP-Spezifikation und verwenden den empfohlenen stdio-Transport für optimale Leistung und Sicherheit.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.