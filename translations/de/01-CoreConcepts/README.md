# MCP Grundkonzepte: Beherrschung des Model Context Protocol für die KI-Integration

[![MCP Grundkonzepte](../../../translated_images/de/02.8203e26c6fb5a797.webp)](https://youtu.be/earDzWGtE84)

_(Klicken Sie auf das obige Bild, um das Video dieser Lektion anzusehen)_

Das [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) ist ein leistungsstarker, standardisierter Rahmen, der die Kommunikation zwischen Large Language Models (LLMs) und externen Werkzeugen, Anwendungen und Datenquellen optimiert.
Dieser Leitfaden führt Sie durch die Kernkonzepte von MCP. Sie lernen die Client-Server-Architektur, wesentliche Komponenten, Kommunikationsmechanismen und beste Implementierungspraktiken kennen.

- **Benutzerkontrolle und Einwilligung**: Hosts sollten klar anzeigen, welche Daten und Werkzeuge ein Server bereitstellt, Nutzern das Ablehnen von Vorgängen ermöglichen und für sensible oder folgenschwere Aktionen eine ausdrückliche Bestätigung einholen. MCP erfordert keinen Bestätigungsdialog vor jedem Werkzeugaufruf.




- **Datenschutz**: Benutzerdaten dürfen nur mit ausdrücklicher Zustimmung offengelegt werden und müssen durch robuste Zugriffskontrollen während des gesamten Interaktionszyklus geschützt werden. Implementierungen müssen unbefugte Datenübertragungen verhindern und strenge Datenschutzgrenzen einhalten.

- **Sicherheit bei der Werkzeugausführung**: Hosts sollten Werkzeugaufrufe sichtbar machen und es einem Menschen ermöglichen, diese abzulehnen. Sensible Vorgänge sollten Eingaben und Auswirkungen anzeigen, bevor sie ausgeführt werden, mit Sicherheitsgrenzen, die unbeabsichtigte oder bösartige Aktionen verhindern.




- **Transportsicherheit**: Remote-Verbindungen sollten HTTPS und das MCP-Autorisierungsmodell verwenden. Lokale stdio-Server basieren auf Prozessisolation, vertrauenswürdiger Konfiguration und sicherer Handhabung vererbter Berechtigungen.



#### Implementierungsrichtlinien:

- **Berechtigungsverwaltung**: Implementieren Sie fein abgestufte Berechtigungssysteme, die es Nutzern ermöglichen, zu steuern, welche Server, Werkzeuge und Ressourcen zugänglich sind
- **Authentifizierung & Autorisierung**: Nutzen Sie sichere Authentifizierungsmethoden (OAuth, API-Schlüssel) mit angemessenem Token-Management und Ablaufzeiten
- **Eingabevalidierung**: Validieren Sie alle Parameter und Eingabedaten gemäß definierten Schemata, um Injektionsangriffe zu verhindern
- **Audit-Logging**: Führen Sie umfassende Protokolle aller Vorgänge für Sicherheitsüberwachung und Compliance

## Überblick

Diese Lektion untersucht die grundlegende Architektur und die Komponenten, die das Model Context Protocol (MCP) Ökosystem ausmachen. Sie erfahren mehr über die Client-Server-Architektur, Hauptkomponenten und Kommunikationsmechanismen, die die MCP-Interaktionen ermöglichen.

## Wichtige Lernziele

Am Ende dieser Lektion werden Sie:

- Die MCP Client-Server-Architektur verstehen.
- Rollen und Verantwortlichkeiten von Hosts, Clients und Servern identifizieren.
- Die Kernfunktionen analysieren, die MCP zu einer flexiblen Integrationsschicht machen.
- Lernen, wie Informationen im MCP-Ökosystem fließen.
- Praktische Einblicke durch Codebeispiele in .NET, Java, Python und JavaScript gewinnen.

## MCP Architektur: Ein tieferer Einblick

Das MCP-Ökosystem basiert auf einem Client-Server-Modell. Diese modulare Struktur ermöglicht es KI-Anwendungen, effizient mit Werkzeugen, Datenbanken, APIs und kontextuellen Ressourcen zu interagieren. Lassen Sie uns diese Architektur in ihre Kernkomponenten aufschlüsseln.

Im Kern folgt MCP einer Client-Server-Architektur, bei der eine Host-Anwendung mit mehreren Servern verbunden sein kann:

```mermaid
flowchart LR
    subgraph "Ihr Computer"
        Host["Host mit MCP (Visual Studio, VS Code, IDEs, Tools)"]
        S1["MCP Server A"]
        S2["MCP Server B"]
        S3["MCP Server C"]
        Host <-->|"MCP-Protokoll"| S1
        Host <-->|"MCP-Protokoll"| S2
        Host <-->|"MCP-Protokoll"| S3
        S1 <--> D1[("Lokal\Datenquelle A")]
        S2 <--> D2[("Lokal\Datenquelle B")]
    end
    subgraph "Internet"
        S3 <-->|"Web-APIs"| D3[("Remote\Dienste")]
    end
```

- **MCP Hosts**: Programme wie VSCode, Claude Desktop, IDEs oder KI-Werkzeuge, die über MCP auf Daten zugreifen möchten
- **MCP Clients**: Protokollkomponenten, die eine logische Beziehung zu einem Server pflegen; MCP `2026-07-28` Anfragen sind nicht von einer persistenten Verbindung oder Sitzung abhängig



- **MCP-Server**: Leichtgewichtige Programme, die jeweils spezifische Fähigkeiten über das standardisierte Model Context Protocol bereitstellen
- **Lokale Datenquellen**: Dateien, Datenbanken und Dienste auf Ihrem Computer, auf die MCP-Server sicher zugreifen können
- **Remote-Dienste**: Externe Systeme, die über das Internet verfügbar sind und auf die MCP-Server über APIs zugreifen können.

Das MCP-Protokoll ist ein sich entwickelnder Standard mit datumsbasierter Versionsnummer
(Format JJJJ-MM-TT). Die aktuelle Protokollversion ist **2026-07-28**. Siehe die
[Protokollspezifikation 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/).

> **Aktuelle Version:** MCP `2026-07-28` macht das Protokoll auf der
> Transportschicht zustandslos, indem der `initialize`-Handshake und
> Protokoll-Sitzungs-IDs entfernt werden. Es formalisiert außerdem einen Erweiterungsrahmen und
> depreziert Roots, Sampling und Logging zugunsten neuer Muster. Siehe
> [Was sich im MCP geändert hat: Die Spezifikation vom 2026-07-28](./mcp-2026-07-28.md)
> für eine vollständige Aufschlüsselung und Migrationsanleitung. Beispiele, die explizit
> `2025-11-25` anvisieren, bleiben als Lektionen zur Legacy-Kompatibilität erhalten.

### 1. Hosts

Im Model Context Protocol (MCP) sind **Hosts** KI-Anwendungen, die als primäre Schnittstelle dienen, über die Benutzer mit dem Protokoll interagieren. Hosts koordinieren und verwalten Verbindungen zu mehreren MCP-Servern, indem sie für jede Serververbindung dedizierte MCP-Clients erstellen. Beispiele für Hosts sind:

- **KI-Anwendungen**: Claude Desktop, Visual Studio Code, Claude Code
- **Entwicklungsumgebungen**: IDEs und Code-Editoren mit MCP-Integration  
- **Benutzerdefinierte Anwendungen**: Zweckgebundene KI-Agenten und Werkzeuge

**Hosts** sind Anwendungen, die KI-Modell-Interaktionen koordinieren. Sie:

- **Orchestrieren KI-Modelle**: Führen LLMs aus oder interagieren mit ihnen, um Antworten zu generieren und KI-Workflows zu koordinieren
- **Verwalten Client-Beziehungen**: Erstellen und verwalten für jeden MCP-Server, den der Host verwendet, einen MCP-Client

- **Steuern die Benutzeroberfläche**: Handhabung des Gesprächsflusses, der Benutzerinteraktionen und der Antwortdarstellung  
- **Setzen Sicherheit durch**: Kontrollieren Berechtigungen, Sicherheitsauflagen und Authentifizierung
- **Verwalten Benutzerzustimmungen**: Verwaltet Benutzerfreigaben für Datenfreigabe und Ausführung von Werkzeugen


### 2. Clients

**Clients** sind Protokollkomponenten, die von einem Host für bestimmte MCP
Server erstellt werden. Dies ist eine logische Eins-zu-eins-Beziehung und keine Voraussetzung für eine
dauerhafte Netzwerkverbindung. Im MCP `2026-07-28` ist jede Anfrage
in sich abgeschlossen und kann von jeder Serverinstanz bearbeitet werden.

**Clients** sind Verbindungskomponenten innerhalb der Host-Anwendung. Sie:

- **Protokollkommunikation**: Senden JSON-RPC 2.0-Anfragen mit Eingabeaufforderungen und Anweisungen an Server
- **Fähigkeitserkennung**: Verwenden `server/discover`, um unterstützte Protokollversionen,
  Fähigkeiten und Erweiterungen eines Servers zu ermitteln
- **Werkzeugausführung**: Verwalten Anfragen zur Ausführung von Werkzeugen durch Modelle und verarbeiten Antworten
- **Echtzeit-Updates**: Bearbeiten Benachrichtigungen und Echtzeit-Updates von Servern
- **Antwortverarbeitung**: Verarbeiten und formatieren Serverantworten für die Anzeige an Benutzer

### 3. Server


**Server** sind Programme, die Kontext, Werkzeuge und Fähigkeiten für MCP-Clients bereitstellen. Sie können lokal (auf demselben Rechner wie der Host) oder remote (auf externen Plattformen) ausgeführt werden und sind dafür verantwortlich, Client-Anfragen zu bearbeiten und strukturierte Antworten zu liefern. Server stellen spezifische Funktionalitäten über das standardisierte Model Context Protocol bereit.

**Server** sind Dienste, die Kontext und Fähigkeiten bereitstellen. Sie:


- **Feature-Registrierung**: Registrieren und Bereitstellen verfügbarer Primitiven (Ressourcen, Prompts, Tools) für Clients
- **Anfrageverarbeitung**: Empfangen und Ausführen von Tool-Aufrufen, Ressourcenanforderungen und Prompt-Anfragen von Clients
- **Kontextbereitstellung**: Bereitstellung kontextueller Informationen und Daten zur Verbesserung der Modellantworten
- **Statusverwaltung**: Verwaltung des Anwendungszustands mit expliziten Handles, die bei Bedarf in Anfragen übergeben werden; MCP `2026-07-28` hat keine Protokollsitzungen

- ** Echtzeit-Benachrichtigungen**: Senden von Benachrichtigungen über Fähigkeitsänderungen und Updates an verbundene Clients

Server können von jedem entwickelt werden, um Modellfähigkeiten mit spezialisierter Funktionalität zu erweitern, und sie unterstützen sowohl lokale als auch entfernte Bereitstellungsszenarien.

### 4. Serverprimitiven

Server im Model Context Protocol (MCP) bieten drei Kern-**Primitiven**, die die grundlegenden Bausteine für reichhaltige Interaktionen zwischen Clients, Hosts und Sprachmodellen definieren. Diese Primitiven spezifizieren die Arten von kontextuellen Informationen und Aktionen, die über das Protokoll verfügbar sind.

MCP-Server können jede Kombination der folgenden drei Kernprimitiven bereitstellen:

#### Ressourcen

**Ressourcen** sind Datenquellen, die kontextuelle Informationen für KI-Anwendungen bereitstellen. Sie repräsentieren statische oder dynamische Inhalte, die das Modellverständnis und die Entscheidungsfindung verbessern können:

- **Kontextuelle Daten**: Strukturierte Informationen und Kontext für den KI-Modellgebrauch
- **Wissensdatenbanken**: Dokumentenarchive, Artikel, Handbücher und Forschungsarbeiten
- **Lokale Datenquellen**: Dateien, Datenbanken und lokale Systeminformationen  
- **Externe Daten**: API-Antworten, Webdienste und entfernte Systemdaten
- **Dynamische Inhalte**: Echtzeitdaten, die sich basierend auf externen Bedingungen aktualisieren

Ressourcen werden durch URIs identifiziert und unterstützen die Entdeckung über `resources/list` und das Abrufen über `resources/read`-Methoden:

```text
file://documents/project-spec.md
database://production/users/schema
api://weather/current
```

#### Prompts

**Prompts** sind wiederverwendbare Vorlagen, die helfen, Interaktionen mit Sprachmodellen zu strukturieren. Sie bieten standardisierte Interaktionsmuster und vorformulierte Arbeitsabläufe:

- **Vorlagenbasierte Interaktionen**: Vorgefertigte Nachrichten und Gesprächseinstiege
- **Arbeitsablaufvorlagen**: Standardisierte Abfolgen für gängige Aufgaben und Interaktionen
- **Few-shot-Beispiele**: Beispielbasierte Vorlagen zur Modellanleitung
- **System-Prompts**: Grundlegende Prompts, die das Modellverhalten und den Kontext definieren
- **Dynamische Vorlagen**: Parameterisierte Prompts, die sich an spezifische Kontexte anpassen

Prompts unterstützen Variablenersetzung und können über `prompts/list` entdeckt und mit `prompts/get` abgerufen werden:

```markdown
Generate a {{task_type}} for {{product}} targeting {{audience}} with the following requirements: {{requirements}}
```

#### Tools

**Tools** sind ausführbare Funktionen, die KI-Modelle aufrufen können, um bestimmte Aktionen auszuführen. Sie repräsentieren die „Verben“ des MCP-Ökosystems und ermöglichen es Modellen, mit externen Systemen zu interagieren:

- **Ausführbare Funktionen**: Diskrete Operationen, die Modelle mit spezifischen Parametern aufrufen können
- **Integration externer Systeme**: API-Aufrufe, Datenbankabfragen, Dateioperationen, Berechnungen
- **Eindeutige Identität**: Jedes Tool besitzt einen eindeutigen Namen, Beschreibung und Parameterschema
- **Strukturierte Ein-/Ausgabe**: Tools akzeptieren validierte Parameter und liefern strukturierte, typisierte Antworten zurück
- **Aktionsfähigkeiten**: Ermöglichen Modellen reale Aktionen auszuführen und Live-Daten abzurufen

Tools werden mit JSON-Schema für Parametervalidierung definiert, können über `tools/list` entdeckt und über `tools/call` ausgeführt werden. Tools können auch **Symbole** als zusätzliche Metadaten für eine bessere UI-Präsentation enthalten.

**Tool-Annotationen**: Tools unterstützen Verhaltensannotation (z. B. `readOnlyHint`, `destructiveHint`), die beschreiben, ob ein Tool schreibgeschützt oder destruktiv ist, und helfen Clients, fundierte Entscheidungen über die Ausführung von Tools zu treffen.


Beispiel für eine Tool-Definition:

```typescript
server.tool(
  "search_products", 
  {
    query: z.string().describe("Search query for products"),
    category: z.string().optional().describe("Product category filter"),
    max_results: z.number().default(10).describe("Maximum results to return")
  }, 
  async (params) => {
    // Suche ausführen und strukturierte Ergebnisse zurückgeben
    return await productService.search(params);
  }
);
```

## Client-Primitiven

Im Model Context Protocol (MCP) können **Clients** Primitiven bereitstellen, die es Servern ermöglichen, zusätzliche Funktionen von der Host-Anwendung anzufordern. Diese clientseitigen Primitiven erlauben reichhaltigere, interaktivere Serverimplementierungen, die Zugriff auf KI-Modellfähigkeiten und Benutzerinteraktionen haben.

### Sampling

> **Veraltet im MCP `2026-07-28`:** Sampling bleibt zur
> Kompatibilität verfügbar, neue Implementierungen sollten jedoch direkt mit einer LLM-
> Anbieter-API integriert werden. Es ist für die Entfernung in der ersten Spezifikations-
> revision vorgesehen, die am oder nach dem 28. Juli 2027 veröffentlicht wird. Siehe
> [Was hat sich im MCP geändert: Die Spezifikation vom 2026-07-28](./mcp-2026-07-28.md).

**Sampling** ermöglicht es Servern, Sprachmodell-Vervollständigungen von der KI-Anwendung des Clients anzufordern. Diese Primitive erlaubt es Servern, auf LLM-Fähigkeiten zuzugreifen, ohne eigene Modelleinbindungen zu benötigen:

- **Modellunabhängiger Zugriff**: Server können Vervollständigungen anfordern, ohne LLM-SDKs einzubinden oder den Modellzugang zu verwalten
- **Serverinitiiertes KI**: Ermöglicht Servern, eigenständig Inhalte mit dem KI-Modell des Clients zu generieren
- **Rekursive LLM-Interaktionen**: Unterstützt komplexe Szenarien, bei denen Server KI-Unterstützung zur Verarbeitung benötigen
- **Dynamische Inhaltserstellung**: Erlaubt es Servern, kontextuelle Antworten unter Verwendung des Host-Modells zu erstellen
- **Werkzeugaufruf-Unterstützung**: Server können `tools` und `toolChoice`-Parameter einbinden, um das Modell des Clients während des Samplings Werkzeuge aufrufen zu lassen

Sampling verwendet die Methode `sampling/createMessage`, bei der Server eine
Vervollständigung von Clients anfordern.

### Roots

> **Veraltet im MCP `2026-07-28`:** Roots bleiben zur
> Kompatibilität verfügbar, neue Implementierungen sollten Verzeichnisse oder Dateien über
> Werkzeugparameter, Ressourcen-URIs oder Serverkonfiguration übergeben. Roots sind für die
> Entfernung in der ersten Spezifikationsrevision vorgesehen, die am oder nach dem
> 28. Juli 2027 veröffentlicht wird. Siehe
> [Was hat sich im MCP geändert: Die Spezifikation vom 2026-07-28](./mcp-2026-07-28.md).

**Roots** bieten eine standardisierte Möglichkeit für Clients, Dateisystem-
positionen zu identifizieren, die für Server relevant sind:

- **Dateisystem-Hinweise**: Identifizieren Verzeichnisse und Dateien, die für die Anfrage relevant sind
- **Getrennte Autorisierung**: Gewähren keinen Zugriff und stellen keine Sicherheitsgrenze dar
- **Pro Anfrage Fähigkeit**: Clients werben in den Anfragemetadaten für Unterstützung von Roots
- **URI-basierte Identifikation**: Roots verwenden `file://`-URIs zur Identifikation zugänglicher Verzeichnisse und Dateien

Im MCP `2026-07-28` fordert ein Server `roots/list` durch ein
`InputRequiredResult` im Verlauf der Bearbeitung einer unterstützten Client-Anfrage an. Der Client
gibt die Roots zurück, wenn er die ursprüngliche Anfrage erneut versucht.

### Elicitation  

**Elicitation** ermöglicht es Servern, über die Client-Oberfläche zusätzliche Informationen oder Bestätigungen von Benutzern anzufordern:

- **Benutzereingabe-Anfragen**: Server können bei Bedarf zusätzliche Informationen für die Werkzeugausführung abfragen
- **Bestätigungsdialoge**: Fordern Benutzerzustimmung für sensible oder folgenschwere Operationen an
- **Interaktive Workflows**: Ermöglichen Servern schrittweise Benutzerinteraktionen zu erstellen
- **Dynamische Parametermobilisierung**: Erfassen fehlender oder optionaler Parameter während der Werkzeugausführung

Elicitation verwendet die Methode `elicitation/create` innerhalb eines
`InputRequiredResult`, um Benutzereingaben über die Schnittstelle des Clients zu sammeln.


**URL-Modus-Elicitation**: Server können auch URL-basierte Benutzerinteraktionen anfordern, sodass Server Benutzer zu externen Webseiten für Authentifizierung, Bestätigung oder Dateneingabe weiterleiten können.

### Protokollierung

> **Veraltet in MCP `2026-07-28`:** Protokollierung bleibt zur
> Kompatibilität verfügbar, aber neue Implementierungen sollten `stderr` mit stdio und
> OpenTelemetry für strukturierte Beobachtbarkeit verwenden. Protokollierung ist berechtigt zur Entfernung
> in der ersten Spezifikationsrevision, die am oder nach dem 28. Juli 2027 veröffentlicht wird. Siehe
> [Was hat sich in MCP geändert: Die 2026-07-28-Spezifikation](./mcp-2026-07-28.md).

**Protokollierung** ermöglicht es Servern, strukturierte Protokollnachrichten an Clients zum Debuggen, Überwachen und zur operativen Sichtbarkeit zu senden:

- **Debugging-Unterstützung**: Ermöglicht Servern das Bereitstellen detaillierter Ausführungsprotokolle zur Fehlersuche
- **Betriebsüberwachung**: Sendet Statusaktualisierungen und Leistungsmetriken an Clients
- **Fehlerberichterstattung**: Bietet detaillierten Fehlerkontext und Diagnoseinformationen
- **Prüfpfade**: Erstellt umfassende Protokolle von Serveroperationen und Entscheidungen

Protokollnachrichten werden an Clients gesendet, um Transparenz über Serveroperationen zu schaffen und das Debuggen zu erleichtern.

## Informationsfluss in MCP

Das Model Context Protocol (MCP) definiert einen strukturierten Informationsfluss zwischen Hosts, Clients, Servern und Modellen. Das Verständnis dieses Flusses hilft dabei zu klären, wie Benutzeranfragen verarbeitet und wie externe Werkzeuge und Daten in Modellantworten integriert werden.

- **Host initiiert Verbindung**  
  Die Hostanwendung (wie eine IDE oder Chat-Oberfläche) stellt eine Verbindung zu einem MCP-Server her, typischerweise über STDIO, WebSocket oder ein anderes unterstütztes Transportmittel.

- **Fähigkeitsverhandlung**  
  Der Client (eingebettet im Host) und der Server tauschen Informationen über ihre unterstützten Funktionen, Werkzeuge, Ressourcen und Protokollversionen aus. Dies stellt sicher, dass beide Seiten verstehen, welche Fähigkeiten für die Sitzung verfügbar sind.

- **Benutzeranfrage**  
  Der Benutzer interagiert mit dem Host (z. B. gibt eine Eingabeaufforderung oder einen Befehl ein). Der Host sammelt diese Eingabe und übergibt sie zur Verarbeitung an den Client.

- **Ressourcen- oder Werkzeugnutzung**  
  - Der Client kann zusätzliche Kontextinformationen oder Ressourcen vom Server anfordern (wie Dateien, Datenbankeinträge oder Wissensdatenbankartikel), um das Verständnis des Modells zu erweitern.
  - Wenn das Modell feststellt, dass ein Werkzeug benötigt wird (z. B. zum Abrufen von Daten, zur Durchführung einer Berechnung oder zum Aufrufen einer API), sendet der Client eine Werkzeugaufruf-Anfrage an den Server und spezifiziert den Werkzeugnamen und die Parameter.

- **Serverausführung**  
  Der Server erhält die Ressourcen- oder Werkzeuganfrage, führt die notwendigen Operationen aus (wie das Ausführen einer Funktion, das Abfragen einer Datenbank oder das Abrufen einer Datei) und gibt die Ergebnisse in strukturierter Form an den Client zurück.

- **Antwortgenerierung**  
  Der Client integriert die Serverantworten (Ressourcendaten, Werkzeugausgaben usw.) in die laufende Modellinteraktion. Das Modell verwendet diese Informationen, um eine umfassende und kontextuell relevante Antwort zu generieren.

- **Ergebnispräsentation**  
  Der Host erhält die endgültige Ausgabe vom Client und präsentiert sie dem Benutzer, oft einschließlich sowohl des vom Modell generierten Textes als auch aller Ergebnisse von Werkzeugausführungen oder Ressourcenabfragen.

Dieser Ablauf ermöglicht es MCP, fortschrittliche, interaktive und kontextbewusste KI-Anwendungen zu unterstützen, indem Modelle nahtlos mit externen Werkzeugen und Datenquellen verbunden werden.

## Protokollarchitektur & Schichten

MCP besteht aus zwei unterschiedlichen architektonischen Schichten, die zusammen ein vollständiges Kommunikationsframework bereitstellen:

### Datenschicht

Die **Datenschicht** implementiert das Kernprotokoll von MCP basierend auf **JSON-RPC 2.0**. Diese Schicht definiert Nachrichtenstruktur, Semantik und Interaktionsmuster:

#### Kernkomponenten:

- **JSON-RPC 2.0 Protokoll**: Alle Kommunikation verwendet das standardisierte JSON-RPC 2.0-Nachrichtenformat für Methodenaufrufe, Antworten und Benachrichtigungen
- **Lebenszyklusverwaltung**: Handhabt Verbindungsinitialisierung, Fähigkeitsverhandlung und Sitzungsbeendigung zwischen Clients und Servern
- **Server-Primitiven**: Ermöglicht Servern die Bereitstellung von Kernfunktionen durch Werkzeuge, Ressourcen und Eingabeaufforderungen
- **Client-Primitiven**: Ermöglicht Servern das Anfordern von Abtastungen von LLMs, Elicitation von Benutzereingaben und das Senden von Protokollnachrichten
- **Echtzeit-Benachrichtigungen**: Unterstützt asynchrone Benachrichtigungen für dynamische Aktualisierungen ohne Abfrage

#### Hauptmerkmale:

- **Protokollversionsverhandlung**: Verwendet datumsbasierte Versionierung (JJJJ-MM-TT) zur Gewährleistung der Kompatibilität
- **Fähigkeitsentdeckung**: Clients und Server tauschen während der Initialisierung Informationen zu unterstützten Funktionen aus
- **Zustandsbehaftete Sitzungen**: Bewahrt Verbindungszustand über mehrere Interaktionen hinweg für Kontextkontinuität

### Transportschicht

Die **Transportschicht** verwaltet Kommunikationskanäle, Nachrichtenrahmung und Authentifizierung zwischen MCP-Teilnehmern:

#### Unterstützte Transportmechanismen:

1. **STDIO-Transport**:
   - Verwendet Standard-Ein- und Ausgabeströme für direkte Prozesskommunikation
   - Optimal für lokale Prozesse auf dem gleichen Rechner ohne Netzwerk-Overhead
   - Häufig genutzt für lokale MCP-Serverimplementierungen

2. **Streamfähiger HTTP-Transport**:
   - Verwendet HTTP POST für Client-zu-Server-Nachrichten  
   - Optional Server-Sent Events (SSE) für Server-zu-Client-Streaming
   - Ermöglicht entfernte Serverkommunikation über Netzwerke hinweg
   - Unterstützt standardmäßige HTTP-Authentifizierung (Bearer Tokens, API-Schlüssel, benutzerdefinierte Header)
   - MCP empfiehlt OAuth für sichere tokenbasierte Authentifizierung

#### Transportabstraktion:

Die Transportschicht abstrahiert Kommunikationsdetails von der Datenschicht, sodass das gleiche JSON-RPC 2.0-Nachrichtenformat über alle Transportmechanismen hinweg verwendet werden kann. Diese Abstraktion erlaubt es Anwendungen, nahtlos zwischen lokalen und entfernten Servern zu wechseln.

### Sicherheitsüberlegungen

MCP-Implementierungen müssen mehrere kritische Sicherheitsprinzipien einhalten, um sichere, vertrauenswürdige und geschützte Interaktionen bei allen Protokolloperationen zu gewährleisten:

- **Benutzereinwilligung und -kontrolle**: Benutzer müssen ausdrücklich zustimmen, bevor auf Daten zugegriffen oder Operationen ausgeführt werden. Sie sollten klare Kontrolle darüber haben, welche Daten geteilt und welche Aktionen autorisiert werden, unterstützt durch intuitive Benutzeroberflächen zur Überprüfung und Genehmigung von Aktivitäten.

- **Datenschutz**: Benutzerdaten sollten nur mit ausdrücklicher Zustimmung offengelegt und durch angemessene Zugriffskontrollen geschützt werden. MCP-Implementierungen müssen unbefugte Datenübertragungen verhindern und sicherstellen, dass der Datenschutz während aller Interaktionen gewahrt bleibt.

- **Werkzeugsicherheit**: Vor dem Aufruf eines Werkzeugs ist eine ausdrückliche Benutzereinwilligung erforderlich. Benutzer sollten klare Informationen über die Funktionalität jedes Werkzeugs erhalten, und es müssen robuste Sicherheitsgrenzen durchgesetzt werden, um unbeabsichtigte oder unsichere Werkzeugausführungen zu verhindern.

Durch die Einhaltung dieser Sicherheitsprinzipien stellt MCP sicher, dass Benutzervertrauen, Datenschutz und Sicherheit bei allen Protokollinteraktionen gewährleistet bleiben und gleichzeitig leistungsstarke KI-Integrationen ermöglicht werden.

## Codebeispiele: Schlüsselkomponenten

Nachfolgend finden Sie Codebeispiele in mehreren populären Programmiersprachen, die zeigen, wie Schlüsselkomponenten und Werkzeuge eines MCP-Servers implementiert werden können.

### .NET-Beispiel: Erstellen eines einfachen MCP-Servers mit Werkzeugen

Hier ist ein praktisches .NET-Codebeispiel, das demonstriert, wie man einen einfachen MCP-Server mit benutzerdefinierten Werkzeugen implementiert. Dieses Beispiel zeigt, wie man Werkzeuge definiert und registriert, Anfragen verarbeitet und den Server mit dem Model Context Protocol verbindet.

```csharp
using System;
using System.Threading.Tasks;
using ModelContextProtocol.Server;
using ModelContextProtocol.Server.Transport;
using ModelContextProtocol.Server.Tools;

public class WeatherServer
{
    public static async Task Main(string[] args)
    {
        // Create an MCP server
        var server = new McpServer(
            name: "Weather MCP Server",
            version: "1.0.0"
        );
        
        // Register our custom weather tool
        server.AddTool<string, WeatherData>("weatherTool", 
            description: "Gets current weather for a location",
            execute: async (location) => {
                // Call weather API (simplified)
                var weatherData = await GetWeatherDataAsync(location);
                return weatherData;
            });
        
        // Connect the server using stdio transport
        var transport = new StdioServerTransport();
        await server.ConnectAsync(transport);
        
        Console.WriteLine("Weather MCP Server started");
        
        // Keep the server running until process is terminated
        await Task.Delay(-1);
    }
    
    private static async Task<WeatherData> GetWeatherDataAsync(string location)
    {
        // This would normally call a weather API
        // Simplified for demonstration
        await Task.Delay(100); // Simulate API call
        return new WeatherData { 
            Temperature = 72.5,
            Conditions = "Sunny",
            Location = location
        };
    }
}

public class WeatherData
{
    public double Temperature { get; set; }
    public string Conditions { get; set; }
    public string Location { get; set; }
}
```

### Java-Beispiel: MCP-Serverkomponenten


Dieses Beispiel zeigt denselben MCP-Server und die Werkzeugregistrierung wie das .NET-Beispiel oben, jedoch in Java implementiert.

```java
import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpToolDefinition;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.server.tool.ToolExecutionContext;
import io.modelcontextprotocol.server.tool.ToolResponse;

public class WeatherMcpServer {
    public static void main(String[] args) throws Exception {
        // Erstelle einen MCP-Server
        McpServer server = McpServer.builder()
            .name("Weather MCP Server")
            .version("1.0.0")
            .build();
            
        // Registriere ein Wetter-Tool
        server.registerTool(McpToolDefinition.builder("weatherTool")
            .description("Gets current weather for a location")
            .parameter("location", String.class)
            .execute((ToolExecutionContext ctx) -> {
                String location = ctx.getParameter("location", String.class);
                
                // Wetterdaten abrufen (vereinfacht)
                WeatherData data = getWeatherData(location);
                
                // Formatiere die Antwort zurückgeben
                return ToolResponse.content(
                    String.format("Temperature: %.1f°F, Conditions: %s, Location: %s", 
                    data.getTemperature(), 
                    data.getConditions(), 
                    data.getLocation())
                );
            })
            .build());
        
        // Verbinde den Server über stdio-Transport
        try (StdioServerTransport transport = new StdioServerTransport()) {
            server.connect(transport);
            System.out.println("Weather MCP Server started");
            // Server läuft weiter, bis der Prozess beendet wird
            Thread.currentThread().join();
        }
    }
    
    private static WeatherData getWeatherData(String location) {
        // Implementierung würde eine Wetter-API aufrufen
        // Vereinfachte Darstellung zu Beispielzwecken
        return new WeatherData(72.5, "Sunny", location);
    }
}

class WeatherData {
    private double temperature;
    private String conditions;
    private String location;
    
    public WeatherData(double temperature, String conditions, String location) {
        this.temperature = temperature;
        this.conditions = conditions;
        this.location = location;
    }
    
    public double getTemperature() {
        return temperature;
    }
    
    public String getConditions() {
        return conditions;
    }
    
    public String getLocation() {
        return location;
    }
}
```

### Python-Beispiel: Aufbau eines MCP-Servers

Dieses Beispiel verwendet fastmcp, stellen Sie daher bitte sicher, dass Sie es zuerst installieren:

```python
pip install fastmcp
```
Codebeispiel:

```python
#!/usr/bin/env python3
import asyncio
from fastmcp import FastMCP
from fastmcp.transports.stdio import serve_stdio

# Erstelle einen FastMCP-Server
mcp = FastMCP(
    name="Weather MCP Server",
    version="1.0.0"
)

@mcp.tool()
def get_weather(location: str) -> dict:
    """Gets current weather for a location."""
    return {
        "temperature": 72.5,
        "conditions": "Sunny",
        "location": location
    }

# Alternative Vorgehensweise mit einer Klasse
class WeatherTools:
    @mcp.tool()
    def forecast(self, location: str, days: int = 1) -> dict:
        """Gets weather forecast for a location for the specified number of days."""
        return {
            "location": location,
            "forecast": [
                {"day": i+1, "temperature": 70 + i, "conditions": "Partly Cloudy"}
                for i in range(days)
            ]
        }

# Registriere Klassentools
weather_tools = WeatherTools()

# Starte den Server
if __name__ == "__main__":
    asyncio.run(serve_stdio(mcp))
```

### JavaScript-Beispiel: Erstellen eines MCP-Servers

Dieses Beispiel zeigt, wie man einen MCP-Server in JavaScript erstellt und zwei wetterrelevante Werkzeuge registriert.

```javascript
// Verwendung des offiziellen Model Context Protocol SDK
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod"; // Für die Parametervalidierung

// Erstellen eines MCP-Servers
const server = new McpServer({
  name: "Weather MCP Server",
  version: "1.0.0"
});

// Definieren eines Wetter-Tools
server.tool(
  "weatherTool",
  {
    location: z.string().describe("The location to get weather for")
  },
  async ({ location }) => {
    // Dies würde normalerweise eine Wetter-API aufrufen
    // Vereinfachte Darstellung zum Demonstrationszweck
    const weatherData = await getWeatherData(location);
    
    return {
      content: [
        { 
          type: "text", 
          text: `Temperature: ${weatherData.temperature}°F, Conditions: ${weatherData.conditions}, Location: ${weatherData.location}` 
        }
      ]
    };
  }
);

// Definieren eines Vorhersage-Tools
server.tool(
  "forecastTool",
  {
    location: z.string(),
    days: z.number().default(3).describe("Number of days for forecast")
  },
  async ({ location, days }) => {
    // Dies würde normalerweise eine Wetter-API aufrufen
    // Vereinfachte Darstellung zum Demonstrationszweck
    const forecast = await getForecastData(location, days);
    
    return {
      content: [
        { 
          type: "text", 
          text: `${days}-day forecast for ${location}: ${JSON.stringify(forecast)}` 
        }
      ]
    };
  }
);

// Hilfsfunktionen
async function getWeatherData(location) {
  // API-Aufruf simulieren
  return {
    temperature: 72.5,
    conditions: "Sunny",
    location: location
  };
}

async function getForecastData(location, days) {
  // API-Aufruf simulieren
  return Array.from({ length: days }, (_, i) => ({
    day: i + 1,
    temperature: 70 + Math.floor(Math.random() * 10),
    conditions: i % 2 === 0 ? "Sunny" : "Partly Cloudy"
  }));
}

// Verbinden des Servers über stdio-Transport
const transport = new StdioServerTransport();
server.connect(transport).catch(console.error);

console.log("Weather MCP Server started");
```

Dieses JavaScript-Beispiel demonstriert, wie man mit dem Model Context Protocol SDK einen MCP-Server erstellt. Es zeigt, wie zwei Werkzeuge namens „weatherTool“ und „forecastTool“ registriert und den MCP-Clients über den „StdioServerTransport“ verfügbar gemacht werden.

## Sicherheit und Autorisierung

MCP enthält mehrere integrierte Konzepte und Mechanismen zur Verwaltung von Sicherheit und Autorisierung im gesamten Protokoll:

1. **Werkzeug-Berechtigungskontrolle**:  
  Clients können für jede Anfrage oder jeden Workflow angeben, welche Werkzeuge ein Modell verwenden darf.
  Dies stellt sicher, dass nur ausdrücklich autorisierte Werkzeuge zugänglich sind, was das Risiko unbeabsichtigter oder unsicherer Operationen verringert.


2. **Authentifizierung**:  
  Server können vor dem Zugriff auf Werkzeuge, Ressourcen oder sensible Operationen eine Authentifizierung verlangen. Dies kann API-Schlüssel, OAuth-Token oder andere Authentifizierungsschemata beinhalten. Eine ordnungsgemäße Authentifizierung gewährleistet, dass nur vertrauenswürdige Clients und Benutzer serverseitige Fähigkeiten verwenden können.

3. **Validierung**:  
  Für alle Werkzeugaufrufe wird eine Parametervalidierung durchgeführt. Jedes Werkzeug definiert die erwarteten Typen, Formate und Einschränkungen für seine Parameter, und der Server validiert eingehende Anfragen entsprechend. Dies verhindert, dass fehlerhafte oder bösartige Eingaben die Werkzeugimplementierungen erreichen und trägt zur Wahrung der Integrität der Operationen bei.

4. **Drosselung (Rate Limiting)**:  
  Um Missbrauch zu verhindern und faire Nutzung der Serverressourcen sicherzustellen, können MCP-Server
  eine Drosselung für Werkzeugaufrufe und Ressourcenzugriffe implementieren. Drosselungsgrenzen können
  pro Benutzer, Berechtigung, Operation oder global angewendet werden.

Durch die Kombination dieser Mechanismen bietet MCP eine sichere Grundlage für die Integration von Sprachmodellen mit externen Werkzeugen und Datenquellen, während Benutzern und Entwicklern eine feinkörnige Kontrolle über Zugriff und Nutzung gegeben wird.

## Protokollnachrichten & Kommunikationsfluss

Die MCP-Kommunikation verwendet strukturierte **JSON-RPC 2.0**-Nachrichten, um klare und zuverlässige Interaktionen zwischen Hosts, Clients und Servern zu ermöglichen. Das Protokoll definiert spezifische Nachrichtenmuster für verschiedene Operationstypen:

### Kern-Nachrichtentypen

#### **Anforderungs-Metadaten und Erkennung**

- **Pro-Anfrage-Metadaten**: Jede `2026-07-28`-Anfrage ist in sich abgeschlossen und
  enthält Protokollversion, Client-Identität und Client-Fähigkeiten in `_meta`.
- **`server/discover`-Anfrage**: Ruft unterstützte Protokollversionen, Server
  Identität, Fähigkeiten und Erweiterungen ab, wenn der Client sie benötigt.
- **Streambare HTTP-Header**: HTTP-Anfragen enthalten `MCP-Protocol-Version` und
  `Mcp-Method`; Methoden, die ein benanntes Werkzeug oder eine Ressource adressieren, enthalten auch
  `Mcp-Name`.

Der Handshake `initialize`/`initialized` und Protokollebene-Sitzungs-IDs gehören
zu früheren Protokollrevisionen und sind nicht Teil von MCP `2026-07-28`.

#### **Erkennungsnachrichten**
- **`tools/list`-Anfrage**: Erkennt verfügbare Werkzeuge auf dem Server
- **`resources/list`-Anfrage**: Listet verfügbare Ressourcen (Datenquellen)
- **`prompts/list`-Anfrage**: Ruft verfügbare Prompt-Vorlagen ab

#### **Ausführungsnachrichten**  
- **`tools/call`-Anfrage**: Führt ein bestimmtes Werkzeug mit bereitgestellten Parametern aus
- **`resources/read`-Anfrage**: Ruft Inhalte von einer bestimmten Ressource ab
- **`prompts/get`-Anfrage**: Holt eine Prompt-Vorlage mit optionalen Parametern

#### **Client-seitige Eingabeanforderungen**

- **`elicitation/create`**: Server fordert über die Client-Schnittstelle Benutzereingaben an,
  während eine Client-Anfrage verarbeitet wird.
- **`sampling/createMessage`**: Veraltete Server-Anfrage für eine LLM-Vervollständigung.
- **`roots/list`**: Veraltete Server-Anfrage für Client-Dateisystem-Wurzeln.

Unter `2026-07-28` verwenden serverseitige Eingabeanforderungen das Mehrfach-Round-Trip-
`InputRequiredResult`-Muster, anstatt sich auf eine persistente Sitzung zu verlassen.

#### **Benachrichtigungsnachrichten**
- **`notifications/tools/list_changed`**: Server benachrichtigt Client über Werkzeugänderungen
- **`notifications/resources/list_changed`**: Server benachrichtigt Client über Ressourcenänderungen  
- **`notifications/prompts/list_changed`**: Server benachrichtigt Client über Prompt-Änderungen

### Nachrichtenstruktur:

Alle MCP-Nachrichten folgen dem JSON-RPC 2.0-Format mit:
- **Anforderungsnachrichten**: Enthalten `id`, `method` und optionale `params`
- **Antwortnachrichten**: Enthalten `id` und entweder `result` oder `error`  
- **Benachrichtigungsnachrichten**: Enthalten `method` und optionale `params` (keine `id` oder Antwort erwartet)

Diese strukturierte Kommunikation gewährleistet zuverlässige, nachvollziehbare und erweiterbare Interaktionen, die fortgeschrittene Szenarien wie Echtzeit-Updates, Werkzeugverkettung und robuste Fehlerbehandlung unterstützen.

### Tasks-Erweiterung

In MCP `2026-07-28` ist Tasks eine offizielle Erweiterung und keine experimentelle
Kernfunktion. Es verwendet einen neu gestalteten Lebenszyklus mit `tasks/get`, `tasks/update` und
`tasks/cancel`; `tasks/list` wurde entfernt. Die experimentelle
`2025-11-25` Tasks-API ist mit dieser Erweiterung nicht rückwärtskompatibel. Siehe
[Was hat sich in MCP geändert: Die Spezifikation 2026-07-28](./mcp-2026-07-28.md).

**Tasks** bieten dauerhafte Ausführungshüllen für verzögertes Ergebnis-Abrufen und
Statusverfolgung:

- **Lang andauernde Operationen**: Verfolgen aufwändige Berechnungen, Workflow-Automatisierung und Batch-Verarbeitung
- **Verzögerte Ergebnisse**: Abfragen des Aufgabenstatus und Abrufen der Ergebnisse bei Abschluss der Operationen
- **Statusverfolgung**: Überwachung des Task-Fortschritts durch definierte Lebenszykluszustände
- **Mehrstufige Operationen**: Unterstützung komplexer Workflows, die mehrere Interaktionen umfassen

Tasks kapseln Standard-MCP-Anfragen, um asynchrone Ausführungsmuster für Operationen zu ermöglichen, die nicht sofort abgeschlossen werden können.

## Wichtige Erkenntnisse

- **Architektur**: MCP verwendet eine Client-Server-Architektur, bei der Hosts mehrere Client-Verbindungen zu Servern verwalten
- **Teilnehmer**: Das Ökosystem umfasst Hosts (KI-Anwendungen), Clients (Protokoll-Connectors) und Server (Fähigkeitsanbieter)
- **Transportmechanismen**: Kommunikation unterstützt stdio (lokal) und Streamable
  HTTP (remote); `2026-07-28` entfernt den separaten GET-Ereignisstrom
- **Kernprimitive**: Server bieten Werkzeuge (ausführbare Funktionen), Ressourcen (Datenquellen) und Prompts (Vorlagen)
- **Client-Primitives**: Elicitation unterstützt Benutzereingaben, während Sampling und
  Roots nur noch als veraltete Kompatibilitätsfunktionen erhalten bleiben
- **Erweiterungen**: Die offizielle Tasks-Erweiterung bietet dauerhafte Ausführungshüllen
  für lang andauernde Operationen

- **Protokollgrundlage**: Basierend auf JSON-RPC 2.0 mit datumsbasierter Versionierung
  (aktuell: `2026-07-28`)

- **Echtzeit-Fähigkeiten**: Unterstützt Benachrichtigungen für dynamische Updates und Echtzeit-Synchronisierung
- **Sicherheit zuerst**: Explizite Zustimmung der Benutzer, Datenschutz und sichere Übertragung sind Kernanforderungen

## Übung

Entwerfen Sie ein einfaches MCP-Tool, das in Ihrem Bereich nützlich wäre. Definieren Sie:
1. Wie das Tool heißen würde
2. Welche Parameter es akzeptieren würde
3. Welche Ausgabe es zurückgeben würde
4. Wie ein Modell dieses Tool verwenden könnte, um Benutzerprobleme zu lösen


---

## Was kommt als Nächstes

Weiter: [Kapitel 2: Sicherheit](../02-Security/README.md)

Lesen Sie [Was sich in MCP geändert hat: Die Spezifikation vom 28.07.2026](./mcp-2026-07-28.md)
für Migrationshinweise von `2025-11-25`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->