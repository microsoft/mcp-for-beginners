# Calculator HTTP Streaming Demo

Dieses Projekt demonstriert HTTP-Streaming mit Server-Sent Events (SSE) unter Verwendung von Spring Boot WebFlux. Es besteht aus zwei Anwendungen:

- **Calculator Server**: Ein reaktiver Webservice, der Berechnungen durchführt und Ergebnisse über SSE streamt
- **Calculator Client**: Eine Client-Anwendung, die den Streaming-Endpunkt konsumiert

## Voraussetzungen

- Java 17 oder höher
- Maven 3.6 oder höher

## Projektstruktur

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Funktionsweise

1. Der **Calculator Server** stellt einen `/calculate`-Endpunkt bereit, der:
   - Abfrageparameter akzeptiert: `a` (Zahl), `b` (Zahl), `op` (Operation)
   - Unterstützte Operationen: `add`, `sub`, `mul`, `div`
   - Server-Sent Events mit dem Fortschritt der Berechnung und dem Ergebnis zurückgibt

2. Der **Calculator Client** verbindet sich mit dem Server und:
   - Sendet eine Anfrage zur Berechnung von `7 * 5`
   - Verarbeitet die Streaming-Antwort
   - Gibt jedes Event in der Konsole aus

## Ausführen der Anwendungen

### Option 1: Mit Maven (empfohlen)

#### 1. Starte den Calculator Server

Öffne ein Terminal und navigiere in das Server-Verzeichnis:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Der Server startet unter `http://localhost:8080`

Du solltest eine Ausgabe wie diese sehen:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Starte den Calculator Client

Öffne ein **neues Terminal** und navigiere in das Client-Verzeichnis:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Der Client verbindet sich mit dem Server, führt die Berechnung durch und zeigt die Streaming-Ergebnisse an.

### Option 2: Direkt mit Java

#### 1. Server kompilieren und starten:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Client kompilieren und starten:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Server manuell testen

Du kannst den Server auch mit einem Webbrowser oder curl testen:

### Mit einem Webbrowser:
Besuche: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Mit curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Erwartete Ausgabe

Beim Ausführen des Clients solltest du eine Streaming-Ausgabe ähnlich der folgenden sehen:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Unterstützte Operationen

- `add` - Addition (a + b)
- `sub` - Subtraktion (a - b)
- `mul` - Multiplikation (a * b)
- `div` - Division (a / b, gibt NaN zurück, wenn b = 0)

## API Referenz

### GET /calculate

**Parameter:**
- `a` (erforderlich): Erste Zahl (double)
- `b` (erforderlich): Zweite Zahl (double)
- `op` (erforderlich): Operation (`add`, `sub`, `mul`, `div`)

**Antwort:**
- Content-Type: `text/event-stream`
- Gibt Server-Sent Events mit dem Fortschritt der Berechnung und dem Ergebnis zurück

**Beispielanfrage:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Beispielantwort:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Fehlerbehebung

### Häufige Probleme

1. **Port 8080 bereits belegt**
   - Beende andere Anwendungen, die Port 8080 verwenden
   - Oder ändere den Server-Port in `calculator-server/src/main/resources/application.yml`

2. **Verbindung abgelehnt**
   - Stelle sicher, dass der Server läuft, bevor du den Client startest
   - Prüfe, ob der Server erfolgreich auf Port 8080 gestartet wurde

3. **Probleme mit Parameternamen**
   - Dieses Projekt enthält eine Maven-Compiler-Konfiguration mit dem Flag `-parameters`
   - Wenn Probleme bei der Parameterbindung auftreten, stelle sicher, dass das Projekt mit dieser Konfiguration gebaut wurde

### Anwendungen stoppen

- Drücke `Ctrl+C` im Terminal, in dem die jeweilige Anwendung läuft
- Oder verwende `mvn spring-boot:stop`, wenn die Anwendung im Hintergrund läuft

## Technologiestack

- **Spring Boot 3.3.1** - Anwendungsframework
- **Spring WebFlux** - Reaktives Webframework
- **Project Reactor** - Reactive Streams Bibliothek
- **Netty** - Non-blocking I/O Server
- **Maven** - Build-Tool
- **Java 17+** - Programmiersprache

## Nächste Schritte

Versuche den Code zu ändern, um:
- Weitere mathematische Operationen hinzuzufügen
- Fehlerbehandlung für ungültige Operationen einzubauen
- Request/Response-Logging hinzuzufügen
- Authentifizierung zu implementieren
- Unit-Tests zu ergänzen

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.