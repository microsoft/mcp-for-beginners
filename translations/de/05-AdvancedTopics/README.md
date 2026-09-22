# Fortgeschrittene Themen im MCP

[![Fortgeschrittenes MCP: Sichere, skalierbare und multimodale KI-Agenten](../../../translated_images/de/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Dieses Kapitel behandelt eine Reihe fortgeschrittener Themen zur Implementierung des Model Context Protocol (MCP), einschließlich multimodaler Integration, Skalierbarkeit, Sicherheitsbest Practices und Unternehmensintegration. Diese Themen sind entscheidend für den Aufbau robuster und produktionsbereiter MCP-Anwendungen, die den Anforderungen moderner KI-Systeme gerecht werden können.

## Übersicht

Diese Lektion erkundet fortgeschrittene Konzepte in der Implementierung des Model Context Protocols mit Schwerpunkt auf multimodaler Integration, Skalierbarkeit, Sicherheitsbest Practices und Unternehmensintegration. Diese Themen sind essenziell für die Erstellung produktionsreifer MCP-Anwendungen, die komplexe Anforderungen in Unternehmensumgebungen bewältigen können.

> **Hinweis zur aktuellen Spezifikation:** MCP `2026-07-28` verwirft die Roots- und
> Sampling-Primitiven, die in den Lektionen 5.4 und 5.6 behandelt werden. Es verschiebt auch das
> experimentelle Tasks-Feature, das in Protocol Features (5.16) erwähnt wird, in eine
> eigene Tasks-Erweiterung. Diese Lektionen bleiben für Legacy-
> `2025-11-25` Implementierungen erhalten und beinhalten Migrationshinweise. Siehe
> [Was sich in MCP geändert hat: Die Spezifikation vom 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md).

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Multimodale Fähigkeiten innerhalb von MCP-Frameworks zu implementieren
- Skalierbare MCP-Architekturen für anspruchsvolle Szenarien zu entwerfen
- Sicherheitsbest Practices anzuwenden, die mit den Sicherheitsprinzipien von MCP übereinstimmen
- MCP mit Unternehmens-KI-Systemen und Frameworks zu integrieren
- Leistung und Zuverlässigkeit in Produktionsumgebungen zu optimieren

## Lektionen und Beispielprojekte

| Link | Titel | Beschreibung |
|------|-------|-------------|
| [5.1 Integration mit Azure](./mcp-integration/README.md) | Integration mit Azure | Lernen Sie, wie Sie Ihren MCP-Server auf Azure integrieren |
| [5.2 Multimodales Beispiel](./mcp-multi-modality/README.md) | MCP Multimodale Beispiele | Beispiele für Audio-, Bild- und multimodale Antworten |
| [5.3 MCP OAuth2 Beispiel](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimale Spring-Boot-App, die OAuth2 mit MCP sowohl als Autorisierungs- als auch als Ressourcenserver zeigt. Demonstriert sichere Token-Ausgabe, geschützte Endpunkte, Bereitstellung in Azure Container Apps und API-Management-Integration. |
| [5.4 Root-Kontexte](./mcp-root-contexts/README.md) | Root-Kontexte | Lernen Sie die Legacy-`2025-11-25` Roots-Primitiven und aktuelle Migrationsmöglichkeiten (veraltet in `2026-07-28`) |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Lernen Sie verschiedene Arten von Routing kennen |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Lernen Sie die Legacy-`2025-11-25` Sampling-Primitiven und aktuelle Migrationsmöglichkeiten (veraltet in `2026-07-28`) |
| [5.7 Skalierung](./mcp-scaling/README.md) | Skalierung | Lernen Sie etwas über Skalierung |
| [5.8 Sicherheit](./mcp-security/README.md) | Sicherheit | Sichern Sie Ihren MCP-Server |
| [5.9 Websuch-Beispiel](./web-search-mcp/README.md) | Websuche MCP | Python MCP-Server und Client, die sich mit SerpAPI zur Echtzeit-Web-, Nachrichten-, Produkt-Suche und Q&A integrieren. Demonstriert Multi-Tool-Orchestrierung, Integration externer APIs und robuste Fehlerbehandlung. |
| [5.10 Echtzeit-Streaming](./mcp-realtimestreaming/README.md) | Streaming | Echtzeit-Daten-Streaming ist in der heutigen datengetriebenen Welt essenziell geworden, in der Unternehmen und Anwendungen sofortigen Zugriff auf Informationen benötigen, um zeitnahe Entscheidungen zu treffen. |
| [5.11 Echtzeit-Websuche](./mcp-realtimesearch/README.md) | Websuche | Wie MCP die Echtzeit-Websuche durch einen standardisierten Ansatz für Kontextmanagement zwischen KI-Modellen, Suchmaschinen und Anwendungen verändert. |
| [5.12 Entra ID Authentifizierung für Model Context Protocol Server](./mcp-security-entra/README.md) | Entra ID Authentifizierung | Microsoft Entra ID bietet eine robuste cloudbasierte Lösung für Identitäts- und Zugriffsmanagement, die sicherstellt, dass nur autorisierte Benutzer und Anwendungen mit Ihrem MCP-Server interagieren können. |
| [5.13 Integration des Microsoft Foundry Agenten](./mcp-foundry-agent-integration/README.md) | Microsoft Foundry Integration | Lernen Sie, wie Sie Model Context Protocol-Server mit Microsoft Foundry-Agenten integrieren, um leistungsstarke Tool-Orchestrierung und Unternehmens-KI-Fähigkeiten mit standardisierten Verbindungen zu externen Datenquellen zu ermöglichen. |
| [5.14 Kontext-Engineering](./mcp-contextengineering/README.md) | Kontext-Engineering | Die zukünftigen Möglichkeiten von Kontext-Engineering-Techniken für MCP-Server, einschließlich Kontextoptimierung, dynamisches Kontextmanagement und Strategien für effektives Prompt-Engineering innerhalb von MCP-Frameworks. |
| [5.15 MCP Benutzerdefinierte Übertragung](./mcp-transport/README.md) | Benutzerdefinierte Übertragung | Lernen Sie, wie Sie benutzerdefinierte Übertragungsmechanismen für spezialisierte MCP-Kommunikationsszenarien implementieren. |
| [5.16 Protokoll-Features im Detail](./mcp-protocol-features/README.md) | Protokoll-Features | Beherrschen Sie fortgeschrittene Protokoll-Features wie Fortschrittsbenachrichtigungen, Anfragestornierung, Ressourcenvorlagen und Muster zur Fehlerbehandlung. |
| [5.17 Adversariales Multi-Agenten-Denken](./mcp-adversarial-agents/README.md) | Adversariale Agenten | Setzen Sie zwei Agenten mit gegensätzlichen Positionen ein, die einen einzigen MCP-Werkzeugkasten teilen, um Halluzinationen zu erkennen, Randfälle hervorzuheben und durch strukturierte Debatten besser kalibrierte Ausgaben zu erzeugen. |

> **Historischer `2025-11-25` Hinweis:** Diese Version führte experimentelle
> Aufgaben ein und erweiterte mehrere Protokollfunktionen. In `2026-07-28` wurden die Aufgaben in
> eine offizielle Erweiterung verschoben und Roots wurden veraltet. Verwenden Sie den
> Feature-Status von `2025-11-25` nicht als aktuelle Anleitung; siehe
> [2026-07-28 Changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## Zusätzliche Referenzen

Für die aktuellsten Informationen zu fortgeschrittenen MCP-Themen verweisen wir auf:
- [MCP Dokumentation](https://modelcontextprotocol.io/)
- [MCP Spezifikation (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Sicherheitsrisiken und Gegenmaßnahmen
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) – Praktisches Sicherheitstraining

## Wichtige Erkenntnisse

- Multimodale MCP-Implementierungen erweitern KI-Fähigkeiten über die Textverarbeitung hinaus
- Skalierbarkeit ist für Unternehmensbereitstellungen essentiell und kann durch horizontale und vertikale Skalierung erreicht werden
- Umfassende Sicherheitsmaßnahmen schützen Daten und gewährleisten kontrollierten Zugriff
- Unternehmensintegration mit Plattformen wie Azure OpenAI und Microsoft AI Foundry verbessert die MCP-Fähigkeiten
- Fortgeschrittene MCP-Implementierungen profitieren von optimierten Architekturen und sorgfältigem Ressourcenmanagement

## Übung

Entwerfen Sie eine MCP-Implementierung auf Unternehmensniveau für einen spezifischen Anwendungsfall:

1. Identifizieren Sie multimodale Anforderungen für Ihren Anwendungsfall
2. Skizzieren Sie die Sicherheitskontrollen, die zum Schutz sensibler Daten erforderlich sind
3. Entwerfen Sie eine skalierbare Architektur, die variable Last bewältigen kann
4. Planen Sie Integrationspunkte mit Unternehmens-KI-Systemen
5. Dokumentieren Sie potenzielle Leistungsengpässe und Gegenmaßnahmen

## Zusätzliche Ressourcen

- [Azure OpenAI Dokumentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Dokumentation](https://learn.microsoft.com/en-us/ai-services/)

---

## Was kommt als Nächstes

Erforschen Sie die Lektionen in diesem Modul beginnend mit: [5.1 MCP Integration](./mcp-integration/README.md)

Nach Abschluss dieses Moduls fahren Sie fort mit: [Modul 6: Community-Beiträge](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->