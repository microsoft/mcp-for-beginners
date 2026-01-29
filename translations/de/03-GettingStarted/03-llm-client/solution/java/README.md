# Calculator LLM Client

Eine Java-Anwendung, die zeigt, wie man LangChain4j verwendet, um eine Verbindung zu einem MCP (Model Context Protocol) Calculator-Service mit GitHub Models-Integration herzustellen.

## Voraussetzungen

- Java 21 oder höher  
- Maven 3.6+ (oder den enthaltenen Maven Wrapper verwenden)  
- Ein GitHub-Konto mit Zugriff auf GitHub Models  
- Ein MCP Calculator-Service, der unter `http://localhost:8080` läuft  

## Den GitHub Token erhalten

Diese Anwendung nutzt GitHub Models, wofür ein persönlicher GitHub Access Token benötigt wird. Folge diesen Schritten, um deinen Token zu erhalten:

### 1. GitHub Models aufrufen
1. Gehe zu [GitHub Models](https://github.com/marketplace/models)  
2. Melde dich mit deinem GitHub-Konto an  
3. Fordere den Zugriff auf GitHub Models an, falls noch nicht geschehen  

### 2. Einen Personal Access Token erstellen
1. Gehe zu [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)  
2. Klicke auf „Generate new token“ → „Generate new token (classic)“  
3. Vergib einen aussagekräftigen Namen für deinen Token (z. B. „MCP Calculator Client“)  
4. Lege die Ablaufzeit nach Bedarf fest  
5. Wähle folgende Berechtigungen aus:  
   - `repo` (wenn auf private Repositories zugegriffen wird)  
   - `user:email`  
6. Klicke auf „Generate token“  
7. **Wichtig**: Kopiere den Token sofort – du kannst ihn später nicht mehr einsehen!  

### 3. Die Umgebungsvariable setzen

#### Unter Windows (Eingabeaufforderung):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Unter Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Unter macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Einrichtung und Installation

1. **Projekt klonen oder in das Projektverzeichnis wechseln**

2. **Abhängigkeiten installieren**:  
   ```cmd
   mvnw clean install
   ```  
   Oder, falls Maven global installiert ist:  
   ```cmd
   mvn clean install
   ```

3. **Umgebungsvariable setzen** (siehe Abschnitt „Den GitHub Token erhalten“ oben)

4. **MCP Calculator Service starten**:  
   Stelle sicher, dass der MCP Calculator Service aus Kapitel 1 unter `http://localhost:8080/sse` läuft. Dieser muss gestartet sein, bevor der Client gestartet wird.

## Anwendung ausführen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Was die Anwendung macht

Die Anwendung zeigt drei Hauptinteraktionen mit dem Calculator-Service:

1. **Addition**: Berechnet die Summe von 24,5 und 17,3  
2. **Quadratwurzel**: Berechnet die Quadratwurzel von 144  
3. **Hilfe**: Zeigt verfügbare Calculator-Funktionen an  

## Erwartete Ausgabe

Bei erfolgreichem Ablauf solltest du eine Ausgabe ähnlich der folgenden sehen:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Fehlerbehebung

### Häufige Probleme

1. **„GITHUB_TOKEN environment variable not set“**  
   - Stelle sicher, dass die Umgebungsvariable `GITHUB_TOKEN` gesetzt ist  
   - Starte dein Terminal/deine Eingabeaufforderung nach dem Setzen der Variable neu  

2. **„Connection refused to localhost:8080“**  
   - Prüfe, ob der MCP Calculator Service auf Port 8080 läuft  
   - Überprüfe, ob ein anderer Dienst Port 8080 blockiert  

3. **„Authentication failed“**  
   - Verifiziere, dass dein GitHub Token gültig ist und die richtigen Berechtigungen hat  
   - Prüfe, ob du Zugriff auf GitHub Models hast  

4. **Maven Build-Fehler**  
   - Stelle sicher, dass du Java 21 oder höher verwendest: `java -version`  
   - Versuche, den Build zu bereinigen: `mvnw clean`  

### Debugging

Um Debug-Logging zu aktivieren, füge beim Starten folgenden JVM-Parameter hinzu:  
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguration

Die Anwendung ist so konfiguriert, dass sie:  
- GitHub Models mit dem Modell `gpt-4.1-nano` verwendet  
- Eine Verbindung zum MCP-Service unter `http://localhost:8080/sse` herstellt  
- Eine Timeout-Zeit von 60 Sekunden für Anfragen nutzt  
- Request/Response-Logging für Debugging aktiviert  

## Abhängigkeiten

Wichtige Abhängigkeiten in diesem Projekt:  
- **LangChain4j**: Für AI-Integration und Tool-Management  
- **LangChain4j MCP**: Für Model Context Protocol Unterstützung  
- **LangChain4j GitHub Models**: Für GitHub Models Integration  
- **Spring Boot**: Für das Anwendungsframework und Dependency Injection  

## Lizenz

Dieses Projekt ist unter der Apache License 2.0 lizenziert – siehe die [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) Datei für Details.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.