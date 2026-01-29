# Basic Calculator MCP Service

Dieser Service bietet grundlegende Taschenrechnerfunktionen über das Model Context Protocol (MCP) an. Er ist als einfaches Beispiel für Einsteiger gedacht, die MCP-Implementierungen kennenlernen möchten.

Für weitere Informationen siehe [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funktionen

Dieser Taschenrechner-Service bietet folgende Möglichkeiten:

1. **Grundlegende arithmetische Operationen**:
   - Addition von zwei Zahlen
   - Subtraktion einer Zahl von einer anderen
   - Multiplikation von zwei Zahlen
   - Division einer Zahl durch eine andere (mit Prüfung auf Division durch Null)

## Verwendung des `stdio`-Typs

## Konfiguration

1. **MCP-Server konfigurieren**:
   - Öffnen Sie Ihren Arbeitsbereich in VS Code.
   - Erstellen Sie eine `.vscode/mcp.json`-Datei in Ihrem Arbeitsbereichsordner, um MCP-Server zu konfigurieren. Beispielkonfiguration:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Sie werden aufgefordert, das Root-Verzeichnis des GitHub-Repositories anzugeben, das Sie mit dem Befehl `git rev-parse --show-toplevel` ermitteln können.

## Verwendung des Services

Der Service stellt über das MCP-Protokoll folgende API-Endpunkte bereit:

- `add(a, b)`: Addiert zwei Zahlen
- `subtract(a, b)`: Subtrahiert die zweite Zahl von der ersten
- `multiply(a, b)`: Multipliziert zwei Zahlen
- `divide(a, b)`: Teilt die erste Zahl durch die zweite (mit Nullprüfung)
- isPrime(n): Prüft, ob eine Zahl eine Primzahl ist

## Testen mit Github Copilot Chat in VS Code

1. Versuchen Sie, eine Anfrage an den Service über das MCP-Protokoll zu stellen. Zum Beispiel können Sie fragen:
   - „Addiere 5 und 3“
   - „Subtrahiere 10 von 4“
   - „Multipliziere 6 und 7“
   - „Teile 8 durch 2“
   - „Ist 37854 eine Primzahl?“
   - „Was sind die 3 Primzahlen vor und nach 4242?“
2. Um sicherzustellen, dass die Tools verwendet werden, fügen Sie dem Prompt #MyCalculator hinzu. Zum Beispiel:
   - „Addiere 5 und 3 #MyCalculator“
   - „Subtrahiere 10 von 4 #MyCalculator“

## Containerisierte Version

Die vorherige Lösung ist ideal, wenn das .NET SDK installiert ist und alle Abhängigkeiten vorhanden sind. Möchten Sie die Lösung jedoch teilen oder in einer anderen Umgebung ausführen, können Sie die containerisierte Version verwenden.

1. Starten Sie Docker und stellen Sie sicher, dass es läuft.
1. Navigieren Sie im Terminal in den Ordner `03-GettingStarted\samples\csharp\src`
1. Um das Docker-Image für den Taschenrechner-Service zu erstellen, führen Sie folgenden Befehl aus (ersetzen Sie `<YOUR-DOCKER-USERNAME>` durch Ihren Docker-Hub-Benutzernamen):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Nachdem das Image erstellt wurde, laden wir es zu Docker Hub hoch. Führen Sie dazu folgenden Befehl aus:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Verwendung der Docker-Version

1. Ersetzen Sie in der Datei `.vscode/mcp.json` die Serverkonfiguration durch Folgendes:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   In der Konfiguration sehen Sie, dass der Befehl `docker` lautet und die Argumente `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc` sind. Der `--rm`-Parameter sorgt dafür, dass der Container nach dem Stoppen entfernt wird, und der `-i`-Parameter ermöglicht die Interaktion mit der Standardeingabe des Containers. Das letzte Argument ist der Name des Images, das wir gerade gebaut und zu Docker Hub hochgeladen haben.

## Testen der Docker-Version

Starten Sie den MCP-Server, indem Sie auf den kleinen Start-Button oberhalb von `"mcp-calc": {` klicken, und wie zuvor können Sie den Taschenrechner-Service bitten, Berechnungen für Sie durchzuführen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.