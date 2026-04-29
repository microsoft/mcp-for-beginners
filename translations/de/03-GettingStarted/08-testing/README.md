## Testen und Debuggen

Bevor Sie mit dem Testen Ihres MCP-Servers beginnen, ist es wichtig, die verfügbaren Werkzeuge und bewährten Praktiken zum Debuggen zu verstehen. Effektives Testen stellt sicher, dass Ihr Server wie erwartet funktioniert und hilft Ihnen, Probleme schnell zu identifizieren und zu beheben. Der folgende Abschnitt beschreibt empfohlene Ansätze zur Validierung Ihrer MCP-Implementierung.

## Überblick

Diese Lektion behandelt, wie Sie den richtigen Testansatz und das effektivste Testwerkzeug auswählen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Verschiedene Ansätze zum Testen zu beschreiben.
- Verschiedene Werkzeuge zu verwenden, um Ihren Code effektiv zu testen.


## Testen von MCP-Servern

MCP stellt Werkzeuge zur Verfügung, die Ihnen beim Testen und Debuggen Ihrer Server helfen:

- **MCP Inspector**: Ein Kommandozeilenwerkzeug, das sowohl als CLI-Werkzeug als auch als visuelles Werkzeug ausgeführt werden kann.
- **Manuelles Testen**: Sie können ein Werkzeug wie curl verwenden, um Web-Anfragen auszuführen, aber jedes Werkzeug, das HTTP ausführen kann, ist geeignet.
- **Unit Testing**: Es ist möglich, Ihr bevorzugtes Testframework zu verwenden, um die Funktionen von Server und Client zu testen.

### Verwendung von MCP Inspector

Wir haben die Nutzung dieses Werkzeugs in vorherigen Lektionen beschrieben, aber lassen Sie uns hier einen kurzen Überblick geben. Es ist ein in Node.js entwickeltes Werkzeug und Sie können es nutzen, indem Sie das `npx`-Kommando aufrufen, das das Werkzeug temporär herunterlädt und installiert und sich nach der Ausführung Ihrer Anfrage wieder selbst entfernt.

Der [MCP Inspector](https://github.com/modelcontextprotocol/inspector) hilft Ihnen dabei:

- **Serverfähigkeiten entdecken**: Automatische Erkennung verfügbarer Ressourcen, Werkzeuge und Eingabeaufforderungen
- **Werkzeugausführung testen**: Verschiedene Parameter ausprobieren und Antworten in Echtzeit sehen
- **Server-Metadaten ansehen**: Serverinformationen, Schemata und Konfigurationen prüfen

Eine typische Ausführung des Werkzeugs sieht so aus:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Der obige Befehl startet einen MCP sowie dessen visuelle Oberfläche und öffnet eine lokale Web-Oberfläche in Ihrem Browser. Sie können ein Dashboard erwarten, das Ihre registrierten MCP-Server, ihre verfügbaren Werkzeuge, Ressourcen und Aufforderungen anzeigt. Die Oberfläche ermöglicht es Ihnen, interaktiv die Werkzeugausführung zu testen, Server-Metadaten zu inspizieren und Echtzeit-Antworten anzusehen, was das Validieren und Debuggen Ihrer MCP-Server-Implementierungen erleichtert.

So könnte es aussehen: ![Inspector](../../../../translated_images/de/connect.141db0b2bd05f096.webp)

Sie können dieses Werkzeug auch im CLI-Modus ausführen, in diesem Fall fügen Sie das Attribut `--cli` hinzu. Hier ein Beispiel für die Ausführung des Werkzeugs im "CLI"-Modus, der alle Werkzeuge auf dem Server auflistet:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuelles Testen

Neben der Ausführung des Inspector-Werkzeugs zum Testen von Serverfähigkeiten gibt es eine ähnliche Möglichkeit: Einen Client zu verwenden, der HTTP-Anfragen stellen kann, wie zum Beispiel curl.

Mit curl können Sie MCP-Server direkt über HTTP-Anfragen testen:

```bash
# Beispiel: Test-Server-Metadaten
curl http://localhost:3000/v1/metadata

# Beispiel: Ein Werkzeug ausführen
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Wie Sie im obigen Beispiel der curl-Nutzung sehen, verwenden Sie eine POST-Anfrage, um ein Werkzeug über eine Nutzlast mit dem Namen des Werkzeugs und dessen Parametern aufzurufen. Wählen Sie den Ansatz, der am besten zu Ihnen passt. CLI-Werkzeuge sind im Allgemeinen schneller nutzbar und lassen sich gut skripten, was in einer CI/CD-Umgebung nützlich sein kann.

### Unit Testing

Erstellen Sie Unit-Tests für Ihre Werkzeuge und Ressourcen, um sicherzustellen, dass sie wie erwartet funktionieren. Hier ein Beispiel für Test-Code.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Markiere das gesamte Modul für asynchrone Tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Erstelle ein paar Testwerkzeuge
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test ohne Cursor-Parameter (weggelassen)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test mit cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test mit Cursor als Zeichenkette
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test mit leerem String-Cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Der obige Code macht Folgendes:

- Nutzt das pytest-Framework, das es Ihnen erlaubt, Tests als Funktionen zu schreiben und assert-Anweisungen zu verwenden.
- Erstellt einen MCP-Server mit zwei verschiedenen Werkzeugen.
- Verwendet `assert`-Anweisungen, um zu überprüfen, ob bestimmte Bedingungen erfüllt sind.

Werfen Sie einen Blick auf die [vollständige Datei hier](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Mit der obigen Datei können Sie Ihren eigenen Server testen, um sicherzustellen, dass die Fähigkeiten wie gewünscht erstellt werden.

Alle großen SDKs haben ähnliche Testabschnitte, sodass Sie sich auf Ihre gewählte Laufzeitumgebung einstellen können.

## Beispiele

- [Java Rechner](../samples/java/calculator/README.md)
- [.Net Rechner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Rechner](../samples/javascript/README.md)
- [TypeScript Rechner](../samples/typescript/README.md)
- [Python Rechner](../../../../03-GettingStarted/samples/python) 

## Zusätzliche Ressourcen

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Was kommt als Nächstes

- Weiter: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in der Ausgangssprache gilt als maßgebliche Quelle. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->