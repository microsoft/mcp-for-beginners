# Studienplan-Generator mit Chainlit & Microsoft Learn Docs MCP

## Voraussetzungen

- Python 3.8 oder höher
- pip (Python-Paketmanager)
- Internetzugang, um eine Verbindung zum Microsoft Learn Docs MCP-Server herzustellen

## Installation

1. Klonen Sie dieses Repository oder laden Sie die Projektdateien herunter.
2. Installieren Sie die erforderlichen Abhängigkeiten:

   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

### Szenario 1: Einfache Abfrage an Docs MCP
Ein Kommandozeilen-Client, der sich mit dem Docs MCP-Server verbindet, eine Abfrage sendet und das Ergebnis ausgibt.

1. Führen Sie das Skript aus:
   ```bash
   python scenario1.py
   ```
2. Geben Sie Ihre Dokumentationsfrage in der Eingabeaufforderung ein.

### Szenario 2: Studienplan-Generator (Chainlit-Web-App)
Eine webbasierte Oberfläche (mit Chainlit), die es Nutzern ermöglicht, einen personalisierten, wöchentlichen Studienplan für ein beliebiges technisches Thema zu erstellen.

1. Starten Sie die Chainlit-App:
   ```bash
   chainlit run scenario2.py
   ```
2. Öffnen Sie die lokale URL, die in Ihrem Terminal angezeigt wird (z. B. http://localhost:8000), in Ihrem Browser.
3. Geben Sie im Chatfenster Ihr Studien-Thema und die Anzahl der Wochen ein, die Sie studieren möchten (z. B. "AI-900 Zertifizierung, 8 Wochen").
4. Die App antwortet mit einem wöchentlichen Studienplan, einschließlich Links zu relevanten Microsoft Learn-Dokumentationen.

**Erforderliche Umgebungsvariablen:**

Um Szenario 2 (die Chainlit-Web-App mit Azure OpenAI) zu nutzen, müssen Sie die folgenden Umgebungsvariablen in einer `.env`-Datei im `python`-Verzeichnis festlegen:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Füllen Sie diese Werte mit den Details Ihrer Azure OpenAI-Ressource aus, bevor Sie die App ausführen.

> [!TIP]
> Sie können Ihre eigenen Modelle ganz einfach mit [Azure AI Foundry](https://ai.azure.com/) bereitstellen.

### Szenario 3: Dokumentation in VS Code mit MCP-Server

Anstatt zwischen Browser-Tabs zu wechseln, um Dokumentationen zu suchen, können Sie Microsoft Learn Docs direkt in VS Code integrieren, indem Sie den MCP-Server verwenden. Dies ermöglicht Ihnen:
- Dokumentationen direkt in VS Code zu durchsuchen und zu lesen, ohne Ihre Entwicklungsumgebung zu verlassen.
- Dokumentationslinks direkt in Ihre README- oder Kursdateien einzufügen.
- GitHub Copilot und MCP zusammen für einen nahtlosen, KI-gestützten Dokumentations-Workflow zu nutzen.

**Beispielanwendungen:**
- Schnell Referenzlinks zu einer README hinzufügen, während Sie eine Kurs- oder Projektdokumentation schreiben.
- Copilot verwenden, um Code zu generieren, und MCP, um relevante Dokumentationen sofort zu finden und zu zitieren.
- In Ihrem Editor fokussiert bleiben und die Produktivität steigern.

> [!IMPORTANT]
> Stellen Sie sicher, dass Sie eine gültige [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json)-Konfiguration in Ihrem Arbeitsbereich haben (Standort: `.vscode/mcp.json`).

## Warum Chainlit für Szenario 2?

Chainlit ist ein modernes Open-Source-Framework zum Erstellen von konversationellen Webanwendungen. Es vereinfacht die Erstellung von chatbasierten Benutzeroberflächen, die mit Backend-Diensten wie dem Microsoft Learn Docs MCP-Server verbunden sind. Dieses Projekt verwendet Chainlit, um eine einfache, interaktive Möglichkeit zu bieten, personalisierte Studienpläne in Echtzeit zu erstellen. Mit Chainlit können Sie schnell chatbasierte Tools entwickeln und bereitstellen, die Produktivität und Lernen fördern.

## Was diese App macht

Diese App ermöglicht es Nutzern, einen personalisierten Studienplan zu erstellen, indem sie einfach ein Thema und eine Dauer eingeben. Die App analysiert Ihre Eingabe, fragt den Microsoft Learn Docs MCP-Server nach relevanten Inhalten ab und organisiert die Ergebnisse in einen strukturierten, wöchentlichen Plan. Die Empfehlungen für jede Woche werden im Chat angezeigt, sodass Sie Ihren Fortschritt leicht verfolgen können. Die Integration stellt sicher, dass Sie immer die neuesten und relevantesten Lernressourcen erhalten.

## Beispielanfragen

Probieren Sie diese Anfragen im Chatfenster aus, um zu sehen, wie die App reagiert:

- `AI-900 Zertifizierung, 8 Wochen`
- `Azure Functions lernen, 4 Wochen`
- `Azure DevOps, 6 Wochen`
- `Datenengineering auf Azure, 10 Wochen`
- `Microsoft Sicherheitsgrundlagen, 5 Wochen`
- `Power Platform, 7 Wochen`
- `Azure KI-Dienste, 12 Wochen`
- `Cloud-Architektur, 9 Wochen`

Diese Beispiele zeigen die Flexibilität der App für unterschiedliche Lernziele und Zeitrahmen.

## Referenzen

- [Chainlit Dokumentation](https://docs.chainlit.io/)
- [MCP Dokumentation](https://github.com/MicrosoftDocs/mcp)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.