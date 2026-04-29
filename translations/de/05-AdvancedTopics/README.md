# Fortgeschrittene Themen in MCP

[![Fortgeschrittenes MCP: Sichere, skalierbare und multimodale KI-Agenten](../../../translated_images/de/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

Dieses Kapitel behandelt eine Reihe fortgeschrittener Themen bei der Implementierung des Model Context Protocol (MCP), einschließlich multimodaler Integration, Skalierbarkeit, Sicherheitsbest Practices und Unternehmensintegration. Diese Themen sind entscheidend für den Aufbau robuster und produktionsreifer MCP-Anwendungen, die den Anforderungen moderner KI-Systeme gerecht werden.

## Überblick

Diese Lektion untersucht fortgeschrittene Konzepte in der Implementierung des Model Context Protocols, mit Schwerpunkt auf multimodaler Integration, Skalierbarkeit, Sicherheitsbest Practices und Unternehmensintegration. Diese Themen sind wesentlich für den Aufbau produktionsfähiger MCP-Anwendungen, die komplexe Anforderungen in Unternehmensumgebungen bewältigen können.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Multimodale Fähigkeiten innerhalb von MCP-Frameworks zu implementieren
- Skalierbare MCP-Architekturen für hochbeanspruchte Szenarien zu entwerfen
- Sicherheitsbest Practices anzuwenden, die mit den Sicherheitsprinzipien von MCP übereinstimmen
- MCP mit Unternehmens-KI-Systemen und -Frameworks zu integrieren
- Leistung und Zuverlässigkeit in Produktionsumgebungen zu optimieren

## Lektionen und Beispielprojekte

| Link | Titel | Beschreibung |
|------|-------|-------------|
| [5.1 Integration mit Azure](./mcp-integration/README.md) | Integration mit Azure | Lernen Sie, wie Sie Ihren MCP-Server auf Azure integrieren |
| [5.2 Multimodales Beispiel](./mcp-multi-modality/README.md) | MCP Multimodale Beispiele | Beispiele für Audio-, Bild- und multimodale Antworten |
| [5.3 MCP OAuth2 Beispiel](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimalistische Spring Boot-App, die OAuth2 mit MCP zeigt, sowohl als Autorisierungs- als auch als Ressourcenserver. Demonstriert sichere Token-Ausstellung, geschützte Endpunkte, Azure Container Apps Deployment und API Management Integration. |
| [5.4 Root-Kontexte](./mcp-root-contexts/README.md) | Root-Kontexte | Erfahren Sie mehr über Root-Kontexte und deren Implementierung |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Lernen Sie verschiedene Routing-Typen kennen |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Lernen Sie den Umgang mit Sampling |
| [5.7 Skalierung](./mcp-scaling/README.md) | Skalierung | Lernen Sie über Skalierung |
| [5.8 Sicherheit](./mcp-security/README.md) | Sicherheit | Schützen Sie Ihren MCP-Server |
| [5.9 Web-Such-Beispiel](./web-search-mcp/README.md) | Web Search MCP | Python MCP-Server und Client, die SerpAPI zur Echtzeit-Web-, Nachrichten- und Produktsuche sowie Q&A integrieren. Demonstriert Multitool-Orchestrierung, externe API-Integration und robuste Fehlerbehandlung. |
| [5.10 Echtzeit-Streaming](./mcp-realtimestreaming/README.md) | Streaming | Echtzeit-Datenstreaming ist in der heutigen datengetriebenen Welt unerlässlich, wo Unternehmen und Anwendungen sofortigen Informationszugang zur rechtzeitigen Entscheidungsfindung benötigen. |
| [5.11 Echtzeit-Web-Suche](./mcp-realtimesearch/README.md) | Web-Suche | Echtzeit-Web-Suche: Wie MCP die Echtzeit-Websuche durch einen standardisierten Ansatz für Kontextmanagement über KI-Modelle, Suchmaschinen und Anwendungen transformiert. |
| [5.12 Entra ID Authentifizierung für Model Context Protocol Server](./mcp-security-entra/README.md) | Entra ID Authentifizierung | Microsoft Entra ID bietet eine robuste cloudbasierte Identitäts- und Zugriffsverwaltungslösung, die sicherstellt, dass nur autorisierte Benutzer und Anwendungen mit Ihrem MCP-Server interagieren können. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry Integration | Lernen Sie, wie Sie Model Context Protocol Server mit Azure AI Foundry Agenten integrieren, um leistungsstarke Tool-Orchestrierung und Enterprise-KI-Fähigkeiten mit standardisierten externen Datenquellen-Verbindungen zu ermöglichen. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Context Engineering | Die zukünftigen Möglichkeiten der Kontexttechnik für MCP-Server, einschließlich Kontextoptimierung, dynamischem Kontextmanagement und Strategien für effektives Prompt Engineering innerhalb von MCP-Frameworks. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Benutzerdefinierter Transport | Erfahren Sie, wie Sie benutzerdefinierte Transportmechanismen für spezialisierte MCP-Kommunikationsszenarien implementieren können. |
| [5.16 Tiefgehende Protokollfunktionen](./mcp-protocol-features/README.md) | Protokollfunktionen | Beherrschen Sie fortgeschrittene Protokollfunktionen, einschließlich Fortschrittsbenachrichtigungen, Anfragestornierung, Ressourcenvorlagen und Fehlerbehandlungsmuster. |
| [5.17 Adversariale Multi-Agenten-Argumentation](./mcp-adversarial-agents/README.md) | Adversariale Agenten | Verwenden Sie zwei Agenten mit entgegengesetzten Positionen, die ein gemeinsames MCP-Toolset teilen, um Halluzinationen zu erkennen, Randfälle aufzuzeigen und besser kalibrierte Ausgaben durch strukturierte Debatten zu produzieren. |

> **Neu in der MCP-Spezifikation 2025-11-25**: Die Spezifikation umfasst jetzt experimentelle Unterstützung für **Aufgaben** (langlaufende Operationen mit Fortschrittsverfolgung), **Tool-Anmerkungen** (Metadaten über das Tool-Verhalten für Sicherheit), **URL-Modus-Elicitation** (Anforderung spezifischer URL-Inhalte von Clients) und erweiterte **Roots** (für das Kontextmanagement von Arbeitsbereichen). Details finden Sie im [MCP-Spezifikations-Änderungsprotokoll](https://spec.modelcontextprotocol.io/).

## Zusätzliche Referenzen

Für die aktuellsten Informationen zu fortgeschrittenen MCP-Themen konsultieren Sie:
- [MCP Dokumentation](https://modelcontextprotocol.io/)
- [MCP Spezifikation (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Sicherheitsrisiken und Gegenmaßnahmen
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) – Praktische Sicherheitsschulung

## Wichtige Erkenntnisse

- Multimodale MCP-Implementierungen erweitern KI-Fähigkeiten über die reine Textverarbeitung hinaus
- Skalierbarkeit ist für Unternehmenseinsätze essenziell und kann durch horizontale und vertikale Skalierung adressiert werden
- Umfassende Sicherheitsmaßnahmen schützen Daten und gewährleisten angemessene Zugriffskontrolle
- Unternehmensintegration mit Plattformen wie Azure OpenAI und Microsoft AI Foundry verbessert die MCP-Fähigkeiten
- Fortgeschrittene MCP-Implementierungen profitieren von optimierten Architekturen und sorgfältigem Ressourcenmanagement

## Übung

Entwerfen Sie eine produktionsreife MCP-Implementierung für einen spezifischen Anwendungsfall:

1. Identifizieren Sie multimodale Anforderungen für Ihren Anwendungsfall
2. Skizzieren Sie die erforderlichen Sicherheitskontrollen zum Schutz sensibler Daten
3. Entwerfen Sie eine skalierbare Architektur, die wechselnde Last bewältigen kann
4. Planen Sie Integrationspunkte mit Unternehmens-KI-Systemen
5. Dokumentieren Sie potenzielle Leistungsengpässe und Gegenmaßnahmen

## Zusätzliche Ressourcen

- [Azure OpenAI Dokumentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Dokumentation](https://learn.microsoft.com/en-us/ai-services/)

---

## Was kommt als nächstes

Entdecken Sie die Lektionen in diesem Modul beginnend mit: [5.1 MCP Integration](./mcp-integration/README.md)

Nachdem Sie dieses Modul abgeschlossen haben, fahren Sie fort zu: [Modul 6: Community-Beiträge](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->