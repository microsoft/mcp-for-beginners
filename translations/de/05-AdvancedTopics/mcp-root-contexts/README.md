# MCP Roots (Legacy-Funktion)

> [!WARNING]
> Roots sind ab MCP `2026-07-28` veraltet. Sie bleiben in dieser Revision zur
> Kompatibilität enthalten und können in der ersten Spezifikationsüberarbeitung,
> die am oder nach dem 28. Juli 2027 veröffentlicht wird, entfernt werden. Neue
> Implementierungen sollten Verzeichnisse oder Dateien über Werkzeugparameter,
> Ressourcen-URIs oder Serverkonfiguration übergeben.

## Überblick

Roots ermöglichen es einem MCP-Client, einem Server mitzuteilen, welche Dateisystemorte
für die aktuelle Anforderung relevant sind. Eine Root enthält eine erforderliche
`file://` URI und optional einen menschenlesbaren Namen.

Roots sind informative Hinweise. Sie sind keine Container für Gesprächshistorien,
Protokoll-Sitzungen oder ein Zugangskontrollmechanismus. Das Protokoll erzwingt nicht,
dass ein Server sich innerhalb der aufgelisteten Roots aufhält.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Zu erklären, was MCP Roots repräsentieren und was nicht.
- Den aktuellen `roots/list` Multi-Round-Trip-Flow zu erkennen.
- Sicherheitskontrollen unabhängig von Roots anzuwenden.
- Neue Implementierungen auf unterstützte Alternativen umzusteigen.

## Root-Daten

Ein Client gibt jede Root als `file://` URI mit optionalem Anzeigenamen zurück:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Clients sollten nur vom Benutzer genehmigte Orte preisgeben. Server sollten
das Ergebnis als Hinweis auf relevante Dateien behandeln, nicht als Autorisierungsnachweis.

## MCP 2026-07-28 Ablauf

Ein Client, der Roots unterstützt, deklariert die Fähigkeit bei jeder Anfrage:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Während der Verarbeitung einer Client-Anfrage kann ein Server ein
`InputRequiredResult` mit einer `roots/list` Eingabeanforderung zurückgeben:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Der Client sammelt die genehmigten Roots und versucht die ursprüngliche Anfrage mit den
passenden `inputResponses` und unverändertem `requestState` erneut. Dieses Multi-Round-Trip-
Muster hält das Protokoll zustandslos; es gibt keinen `initialize`-Handshake oder
Protokoll-Sitzung auf Ebene des Protokolls.

## Legacy-Verhalten 2025-11-25

In MCP `2025-11-25` beworben Clients Roots während der Initialisierung. Ein Server
konnte direkt eine `roots/list` Anfrage stellen, und ein Client konnte
`notifications/roots/list_changed` senden, wenn sich seine Roots änderten.

Dieser Lebenszyklus ist Legacy-Verhalten. Kombinieren Sie seine Initialisierungs- oder
Benachrichtigungsbeispiele nicht mit einer `2026-07-28` Implementierung.

## Empfohlene Alternativen

### Werkzeugparameter

Machen Sie das erforderliche Verzeichnis oder die Datei im Werkzeugschema explizit:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### Ressourcen-URIs

Verwenden Sie MCP Resources, wenn der Server die relevanten Dateien über stabile
URIs bereitstellen kann. Dies macht Entdeckung und Zugriff explizit.

### Serverkonfiguration

Für feste Bereitstellungen konfigurieren Sie die erlaubten Verzeichnisse beim Start des Servers.
Dies ist oft klarer, als sie während eines Werkzeugaufrufs zu entdecken.

## Sicherheitsanforderungen

Welche Alternative Sie auch wählen:

- Holen Sie vor der Offenlegung von Dateisystemorten die Zustimmung des Nutzers ein.
- Kanonisieren und validieren Sie Pfade, um Traversal zu verhindern.
- Erzwingen Sie Autorisierung und Sandboxing unabhängig von Root-Werten.
- Überprüfen Sie Berechtigungen beim Zugriff auf eine Datei, nicht nur bei der Auflistung.
- Vermeiden Sie die Rückgabe sensibler Pfade in Logs oder Fehlermeldungen.

## Wichtige Erkenntnisse

- Roots beschreiben relevante Dateisystemorte; sie speichern keinen Gesprächszustand.

- Roots sind Hinweise, keine Zugangskontrollgrenze.
- MCP `2026-07-28` trägt die Fähigkeit pro Anfrage und verwendet
  `InputRequiredResult` für `roots/list`.
- Neue Implementierungen sollten stattdessen Werkzeugparameter, Ressourcen-URIs oder Server-
  konfiguration verwenden.

## Weitere Ressourcen

- [Roots in MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Veraltete Funktionen Registrierung](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Was sich in MCP geändert hat: Die Spezifikation 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->