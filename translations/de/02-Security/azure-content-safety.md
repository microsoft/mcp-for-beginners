# Erweiterte MCP-Sicherheit mit Azure Content Safety

Azure Content Safety bietet mehrere leistungsstarke Werkzeuge, die die Sicherheit Ihrer MCP-Implementierungen verbessern können:

## Prompt Shields

Microsofts AI Prompt Shields bieten einen starken Schutz gegen direkte und indirekte Prompt-Injection-Angriffe durch:

1. **Fortschrittliche Erkennung**: Nutzt maschinelles Lernen, um bösartige Anweisungen, die im Inhalt eingebettet sind, zu identifizieren.
2. **Spotlighting**: Wandelt Eingabetext um, damit KI-Systeme zwischen gültigen Anweisungen und externen Eingaben unterscheiden können.
3. **Trennzeichen und Datenmarkierung**: Markiert Grenzen zwischen vertrauenswürdigen und nicht vertrauenswürdigen Daten.
4. **Integration mit Content Safety**: Arbeitet mit Azure AI Content Safety zusammen, um Jailbreak-Versuche und schädliche Inhalte zu erkennen.
5. **Kontinuierliche Updates**: Microsoft aktualisiert regelmäßig die Schutzmechanismen gegen neue Bedrohungen.

## Implementierung von Azure Content Safety mit MCP

Dieser Ansatz bietet mehrschichtigen Schutz:
- Scannen der Eingaben vor der Verarbeitung
- Validierung der Ausgaben vor der Rückgabe
- Verwendung von Blocklisten für bekannte schädliche Muster
- Nutzung der kontinuierlich aktualisierten Content Safety-Modelle von Azure

## Azure Content Safety Ressourcen

Um mehr über die Implementierung von Azure Content Safety mit Ihren MCP-Servern zu erfahren, konsultieren Sie diese offiziellen Ressourcen:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) – Offizielle Dokumentation zu Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) – Erfahren Sie, wie Sie Prompt-Injection-Angriffe verhindern.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) – Detaillierte API-Referenz zur Implementierung von Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) – Schnellstart-Anleitung zur Implementierung mit C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) – Client-Bibliotheken für verschiedene Programmiersprachen.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) – Spezifische Hinweise zum Erkennen und Verhindern von Jailbreak-Versuchen.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) – Best Practices für eine effektive Umsetzung von Content Safety.

Für eine ausführlichere Implementierung siehe unseren [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.