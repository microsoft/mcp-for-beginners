# Rechner LLM Client

> [!NOTE]
> Diese Lösung verbindet sich mit dem Legacy HTTP+SSE Rechnerdienst des Kurses und
> richtet sich an die MCP `2025-11-25` SDK-APIs. Es ist kein `2026-07-28` Streamable HTTP
> Beispiel.

Eine Java-Anwendung, die zeigt, wie man LangChain4j verwendet, um sich über die MiniMax OpenAI-kompatible API mit einem MCP (Model Context Protocol) Rechnerdienst zu verbinden.

## Voraussetzungen

- Java 21 oder höher
- Maven 3.6+ (oder verwenden Sie den inkludierten Maven Wrapper)
- Ein MiniMax API-Schlüssel
- Ein MCP-Rechnerdienst, der auf `http://localhost:8080` läuft

## Den API-Schlüssel erhalten

Diese Anwendung nutzt die MiniMax OpenAI-kompatible API. Folgen Sie diesen Schritten, um Ihren Schlüssel und Endpunkt zu erhalten:

### 1. Wählen Sie einen Endpunkt
1. Verwenden Sie `https://api.minimax.io/v1` für den globalen Endpunkt
2. Verwenden Sie `https://api.minimaxi.com/v1` für den China-Endpunkt

### 2. Erstellen Sie einen API-Schlüssel
1. Erstellen Sie einen MiniMax API-Schlüssel in Ihrem MiniMax-Konto
2. Bewahren Sie den Schlüssel sicher auf

### 3. Setzen Sie die Umgebungsvariablen

#### Unter Windows (Eingabeaufforderung):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Unter Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Unter macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Einrichtung und Installation

1. **Klonen Sie das Projekt oder navigieren Sie zum Projektverzeichnis**

2. **Installieren Sie Abhängigkeiten**:
   ```cmd
   mvnw clean install
   ```
   Oder wenn Sie Maven global installiert haben:
   ```cmd
   mvn clean install
   ```

3. **Richten Sie die Umgebungsvariablen ein** (siehe Abschnitt „Den API-Schlüssel erhalten“ oben)

4. **Starten Sie den MCP Rechnerdienst**:
   Stellen Sie sicher, dass der MCP Rechnerdienst aus Kapitel 1 unter `http://localhost:8080/sse` läuft. Dieser sollte gestartet sein, bevor Sie den Client starten.

## Anwendung ausführen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Was die Anwendung macht

Die Anwendung demonstriert drei Hauptinteraktionen mit dem Rechnerdienst:

1. **Addition**: Berechnet die Summe von 24,5 und 17,3
2. **Quadratwurzel**: Berechnet die Quadratwurzel von 144
3. **Hilfe**: Zeigt verfügbare Rechnerfunktionen an

## Erwartete Ausgabe

Bei erfolgreichem Ablauf sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Fehlersuche

### Häufige Probleme

1. **„OPENAI_API_KEY-Umgebungsvariable ist nicht gesetzt“**
   - Stellen Sie sicher, dass Sie die Umgebungsvariable `OPENAI_API_KEY` gesetzt haben
   - Starten Sie Ihr Terminal/Eingabeaufforderung nach dem Setzen der Variable neu

2. **„Verbindung zu localhost:8080 verweigert“**
   - Stellen Sie sicher, dass der MCP Rechnerdienst auf Port 8080 läuft
   - Prüfen Sie, ob ein anderer Dienst Port 8080 verwendet

3. **„Authentifizierung fehlgeschlagen“**
   - Überprüfen Sie, ob Ihr API-Schlüssel gültig ist
   - Prüfen Sie, ob `OPENAI_BASE_URL` dem gewünschten Endpunkt entspricht

4. **Maven-Build-Fehler**
   - Stellen Sie sicher, dass Sie Java 21 oder höher verwenden: `java -version`
   - Versuchen Sie, den Build zu bereinigen: `mvnw clean`

### Debugging

Um das Debug-Logging zu aktivieren, fügen Sie beim Ausführen folgendes JVM-Argument hinzu:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguration

Die Anwendung ist so konfiguriert, dass sie:
- Standardmäßig MiniMax-M3 verwendet; `MINIMAX_MODEL_ID` kann auf `MiniMax-M3` oder `MiniMax-M2.7` gesetzt werden
- Sich mit `OPENAI_BASE_URL` verbindet, wenn dieser gesetzt ist; andernfalls `https://api.minimaxi.com/v1` verwendet wird, wenn `MINIMAX_REGION=cn_zh`, oder standardmäßig `https://api.minimax.io/v1`
- Sich mit dem MCP-Dienst unter `http://localhost:8080/sse` verbindet
- Eine Timeout-Dauer von 60 Sekunden für Anfragen verwendet

## Abhängigkeiten

Wichtige in diesem Projekt verwendete Abhängigkeiten:
- **LangChain4j**: Für KI-Integration und Werkzeugverwaltung
- **LangChain4j MCP**: Für Model Context Protocol Unterstützung
- **LangChain4j OpenAI offiziell**: Für MiniMax OpenAI-kompatible API Integration
- **Spring Boot**: Für Anwendungsframework und Dependency Injection

## Lizenz

Dieses Projekt ist unter der Apache License 2.0 lizenziert – siehe die [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) Datei für Details.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->