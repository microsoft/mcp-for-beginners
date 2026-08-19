# Nutzung eines Servers aus der AI Toolkit-Erweiterung für Visual Studio Code

Wenn Sie einen KI-Agenten erstellen, geht es nicht nur darum, intelligente Antworten zu generieren, sondern auch darum, Ihrem Agenten die Fähigkeit zur Handlung zu geben. Hier kommt das Model Context Protocol (MCP) ins Spiel. MCP macht es einfach für Agenten, konsistent auf externe Werkzeuge und Dienste zuzugreifen. Stellen Sie sich das vor wie das Anschließen Ihres Agenten an einen Werkzeugkasten, den er *wirklich* nutzen kann.

Nehmen wir an, Sie verbinden einen Agenten mit Ihrem Rechner-MCP-Server. Plötzlich kann Ihr Agent mathematische Operationen ausführen, indem er einfach eine Anfrage wie „Was ist 47 mal 89?“ erhält – es ist keine Hardcodierung von Logik oder Erstellung benutzerdefinierter APIs erforderlich.

## Überblick

Diese Lektion behandelt, wie Sie einen Rechner-MCP-Server mit einem Agenten über die [AI Toolkit](https://aka.ms/AIToolkit)-Erweiterung in Visual Studio Code verbinden, damit Ihr Agent mathematische Operationen wie Addition, Subtraktion, Multiplikation und Division über natürliche Sprache ausführen kann.

AI Toolkit ist eine leistungsstarke Erweiterung für Visual Studio Code, die die Entwicklung von Agenten vereinfacht. KI-Ingenieure können KI-Anwendungen ganz einfach bauen, indem sie generative KI-Modelle lokal oder in der Cloud entwickeln und testen. Die Erweiterung unterstützt die meisten wichtigen generativen Modelle, die heute verfügbar sind.

*Hinweis*: Das AI Toolkit unterstützt aktuell Python und TypeScript.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Einen MCP-Server über das AI Toolkit zu nutzen.
- Eine Agentenkonfiguration einzurichten, um das Entdecken und Verwenden von Tools des MCP-Servers zu ermöglichen.
- MCP-Tools mit natürlicher Sprache zu verwenden.

## Vorgehensweise

So gehen wir auf einem hohen Niveau vor:

- Erstellen Sie einen Agenten und definieren Sie seinen System-Prompt.
- Erstellen Sie einen MCP-Server mit Rechner-Tools.
- Verbinden Sie den Agent Builder mit dem MCP-Server.
- Testen Sie die Werkzeugaufrufe des Agenten über natürliche Sprache.

Super, nachdem wir den Ablauf verstanden haben, konfigurieren wir nun einen KI-Agenten, der externe Tools über MCP nutzt, um seine Fähigkeiten zu erweitern!

## Voraussetzungen

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit für Visual Studio Code](https://aka.ms/AIToolkit)

## Übung: Einen Server nutzen

> [!WARNUNG]
> Hinweis für macOS-Nutzer. Wir untersuchen derzeit ein Problem bei der Installation von Abhängigkeiten auf macOS. Daher können macOS-Nutzer dieses Tutorial derzeit nicht abschließen. Wir aktualisieren die Anweisungen, sobald eine Lösung verfügbar ist. Vielen Dank für Ihre Geduld und Ihr Verständnis!

In dieser Übung erstellen, starten und erweitern Sie einen KI-Agenten mit Tools von einem MCP-Server innerhalb von Visual Studio Code mithilfe des AI Toolkits.

### -0- Vorbereitung: Das OpenAI GPT-4o Modell zu „Meine Modelle“ hinzufügen

Die Übung verwendet das **GPT-4o** Modell. Das Modell sollte vor dem Erstellen des Agenten zu **Meine Modelle** hinzugefügt werden.

![Screenshot einer Modellauswahl-Oberfläche in der AI Toolkit-Erweiterung von Visual Studio Code. Die Überschrift lautet „Find the right model for your AI Solution“ mit einem Untertitel, der Nutzer ermutigt, KI-Modelle zu entdecken, zu testen und bereitzustellen. Darunter, unter „Popular Models“, werden sechs Modellkarten angezeigt: DeepSeek-R1 (GitHub-gehostet), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Klein, Schnell) und DeepSeek-R1 (Ollama-gehostet). Jede Karte enthält Optionen zum „Hinzufügen“ des Modells oder „Im Playground ausprobieren“](../../../../translated_images/de/aitk-model-catalog.2acd38953bb9c119.webp)

1. Öffnen Sie die **AI Toolkit**-Erweiterung über die **Activity Bar**.
1. Wählen Sie im Bereich **Catalog** die Option **Models**, um den **Model Catalog** zu öffnen. Das Öffnen von **Models** öffnet den **Model Catalog** in einem neuen Editor-Tab.
1. Geben Sie in der Suchleiste des **Model Catalog** „OpenAI GPT-4o“ ein.
1. Klicken Sie auf **+ Add**, um das Modell zu Ihrer Liste **Meine Modelle** hinzuzufügen. Achten Sie darauf, das Modell zu wählen, das **von GitHub gehostet wird**.
1. Stellen Sie in der **Activity Bar** sicher, dass das **OpenAI GPT-4o** Modell in der Liste erscheint.

### -1- Einen Agenten erstellen

Der **Agent (Prompt) Builder** ermöglicht es Ihnen, eigene KI-getriebene Agenten zu erstellen und anzupassen. In diesem Abschnitt erstellen Sie einen neuen Agenten und weisen ihm ein Modell zu, das die Unterhaltung steuert.

![Screenshot der "Calculator Agent" Builder-Oberfläche in der AI Toolkit-Erweiterung für Visual Studio Code. Im linken Bereich ist das Modell „OpenAI GPT-4o (via GitHub)“ ausgewählt. Ein System-Prompt lautet „You are a professor in university teaching math“ und der Nutzer-Prompt sagt „Explain to me the Fourier equation in simple terms.“ Weitere Optionen umfassen Schaltflächen zum Hinzufügen von Tools, Aktivieren des MCP Servers und Auswahl von strukturiertem Output. Unten befindet sich ein blauer „Run“-Button. Im rechten Bereich unter „Get Started with Examples“ werden drei Beispiel-Agenten gezeigt: Web Developer (mit MCP Server, Second-Grade Simplifier und Dream Interpreter, jeweils mit kurzen Beschreibungen ihrer Funktionen).](../../../../translated_images/de/aitk-agent-builder.901e3a2960c3e477.webp)

1. Öffnen Sie die **AI Toolkit**-Erweiterung über die **Activity Bar**.
1. Wählen Sie im Bereich **Tools** die Option **Agent (Prompt) Builder**. Das Öffnen von **Agent (Prompt) Builder** startet den Builder in einem neuen Editor-Tab.
1. Klicken Sie auf die **+ New Agent**-Schaltfläche. Die Erweiterung startet einen Einrichtungsassistenten über die **Command Palette**.
1. Geben Sie den Namen **Calculator Agent** ein und drücken Sie **Enter**.
1. Wählen Sie im Feld **Model** des **Agent (Prompt) Builder** das Modell **OpenAI GPT-4o (via GitHub)** aus.

### -2- Einen System-Prompt für den Agenten erstellen

Nachdem der Agent entwickelt wurde, ist es Zeit, seine Persönlichkeit und seinen Zweck zu definieren. In diesem Abschnitt verwenden Sie die Funktion **Generate system prompt**, um das beabsichtigte Verhalten des Agenten – in diesem Fall ein Rechner-Agent – zu beschreiben und das Modell den System-Prompt für Sie schreiben zu lassen.

![Screenshot der "Calculator Agent" Oberfläche im AI Toolkit für Visual Studio Code mit einem geöffneten Modalfenster „Generate a prompt“. Das Modal erklärt, dass eine Prompt-Vorlage generiert werden kann, indem grundlegende Details geteilt werden, und enthält ein Textfeld mit dem Beispiel-System-Prompt: „You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.“ Unter dem Textfeld befinden sich die Schaltflächen „Close“ und „Generate“. Im Hintergrund ist ein Teil der Agentenkonfiguration sichtbar, einschließlich des ausgewählten Modells „OpenAI GPT-4o (via GitHub)“ sowie Felder für System- und Nutzer-Prompts.](../../../../translated_images/de/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Klicken Sie im Bereich **Prompts** auf die Schaltfläche **Generate system prompt**. Diese öffnet den Prompt Builder, der KI nutzt, um den System-Prompt für den Agenten zu generieren.
1. Geben Sie im Fenster **Generate a prompt** Folgendes ein: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Klicken Sie auf die Schaltfläche **Generate**. Eine Benachrichtigung erscheint unten rechts, die bestätigt, dass der System-Prompt generiert wird. Nach der Fertigstellung erscheint der Prompt im Feld **System prompt** im **Agent (Prompt) Builder**.
1. Überprüfen Sie den **System prompt** und passen Sie ihn bei Bedarf an.

### -3- Einen MCP-Server erstellen

Nachdem Sie den System-Prompt Ihres Agenten definiert haben – der sein Verhalten und seine Antworten steuert – ist es Zeit, den Agenten mit praktischen Fähigkeiten auszustatten. In diesem Abschnitt erstellen Sie einen Rechner-MCP-Server mit Tools, die Addition, Subtraktion, Multiplikation und Division ausführen können. Dieser Server ermöglicht Ihrem Agenten, Echtzeit-Mathematikoperationen als Reaktion auf natürliche Spracheingaben durchzuführen.

![Screenshot des unteren Bereichs der Calculator Agent-Oberfläche in der AI Toolkit-Erweiterung für Visual Studio Code. Es zeigt aufklappbare Menüs für „Tools“ und „Structure output“ sowie ein Dropdown-Menü „Choose output format“ mit der Einstellung „text.“ Rechts befindet sich eine Schaltfläche „+ MCP Server“ zum Hinzufügen eines Model Context Protocol Servers. Oberhalb des Tools-Bereichs ist ein Bildsymbol-Platzhalter angezeigt.](../../../../translated_images/de/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit ist mit Vorlagen ausgestattet, die die Erstellung Ihres eigenen MCP-Servers erleichtern. Wir verwenden die Python-Vorlage zur Erstellung des Rechner-MCP-Servers.

*Hinweis*: Das AI Toolkit unterstützt aktuell Python und TypeScript.

1. Klicken Sie im Bereich **Tools** des **Agent (Prompt) Builder** auf die Schaltfläche **+ MCP Server**. Die Erweiterung startet einen Einrichtungsassistenten über die **Command Palette**.
1. Wählen Sie **+ Add Server**.
1. Wählen Sie **Create a New MCP Server**.
1. Wählen Sie die Vorlage **python-weather**.
1. Wählen Sie **Default folder**, um die MCP-Server-Vorlage zu speichern.
1. Geben Sie folgenden Namen für den Server ein: **Calculator**
1. Ein neues Visual Studio Code-Fenster öffnet sich. Wählen Sie **Yes, I trust the authors**.
1. Erstellen Sie mit dem Terminal (**Terminal** > **New Terminal**) eine virtuelle Umgebung: `python -m venv .venv`
1. Aktivieren Sie mit dem Terminal die virtuelle Umgebung:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Installieren Sie mit dem Terminal die Abhängigkeiten: `pip install -e .[dev]`
1. Erweitern Sie im **Explorer**-Bereich der **Activity Bar** das Verzeichnis **src** und wählen Sie **server.py**, um die Datei im Editor zu öffnen.
1. Ersetzen Sie den Code in der Datei **server.py** durch den folgenden und speichern Sie:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Den Agenten mit dem Rechner-MCP-Server ausführen

Nun, da Ihr Agent Tools hat, ist es Zeit, diese zu nutzen! In diesem Abschnitt senden Sie Eingaben an den Agenten, um zu testen und zu validieren, ob der Agent das passende Tool vom Rechner-MCP-Server verwendet.

![Screenshot der Calculator Agent-Oberfläche in der AI Toolkit-Erweiterung für Visual Studio Code. Im linken Bereich unter „Tools“ ist ein MCP Server namens local-server-calculator_server hinzugefügt, der vier verfügbare Tools zeigt: add, subtract, multiply und divide. Eine Markierung zeigt, dass vier Tools aktiv sind. Darunter ist ein eingeklappter Bereich „Structure output“ und ein blauer „Run“-Button. Im rechten Bereich unter „Model Response“ ruft der Agent die multiply- und subtract-Tools mit Eingaben {"a": 3, "b": 25} beziehungsweise {"a": 75, "b": 20} auf. Die finale „Tool Response“ wird mit 75.0 angezeigt. Unten ist eine Schaltfläche „View Code“.](../../../../translated_images/de/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Sie führen den Rechner-MCP-Server auf Ihrem lokalen Entwicklungsrechner über den **Agent Builder** als MCP-Client aus.

1. Drücken Sie `F5`, um das Debugging des MCP-Servers zu starten. Der **Agent (Prompt) Builder** wird in einem neuen Editor-Tab geöffnet. Der Serverstatus ist im Terminal sichtbar.
1. Geben Sie im Feld **User prompt** des **Agent (Prompt) Builder** folgenden Text ein: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Klicken Sie auf den **Run**-Button, um die Antwort des Agenten zu generieren.
1. Überprüfen Sie die Ausgabe des Agenten. Das Modell sollte zu dem Schluss kommen, dass Sie **55 $** bezahlt haben.
1. Hier ist eine Aufschlüsselung dessen, was passieren sollte:
    - Der Agent wählt die Tools **multiply** und **subtract** zur Unterstützung bei der Berechnung aus.
    - Die jeweiligen Werte für `a` und `b` werden für das Tool **multiply** zugewiesen.
    - Die jeweiligen Werte für `a` und `b` werden für das Tool **subtract** zugewiesen.
    - Die Antwort jedes Tools wird im jeweiligen **Tool Response** bereitgestellt.
    - Die finale Ausgabe des Modells wird in der abschließenden **Model Response** angezeigt.
1. Senden Sie weitere Eingaben zur weiteren Testung des Agenten. Sie können den bestehenden Prompt im Feld **User prompt** ändern, indem Sie in das Feld klicken und den vorhandenen Prompt ersetzen.
1. Wenn Sie mit dem Testen fertig sind, können Sie den Server über das **Terminal** mit **STRG/CMD+C** beenden.

## Aufgabe

Versuchen Sie, einen zusätzlichen Tool-Eintrag in Ihre **server.py**-Datei hinzuzufügen (z. B. die Rückgabe der Quadratwurzel einer Zahl). Senden Sie weitere Eingaben, die den Agenten dazu veranlassen, Ihr neues Tool (oder bestehende Tools) zu nutzen. Vergessen Sie nicht, den Server neu zu starten, um die neu hinzugefügten Tools zu laden.

## Lösung

[Lösung](./solution/README.md)

## Zentrale Erkenntnisse

Die wichtigsten Erkenntnisse aus diesem Kapitel sind:

- Die AI Toolkit-Erweiterung ist ein großartiger Client, mit dem Sie MCP-Server und deren Tools nutzen können.
- Sie können neue Tools zu MCP-Servern hinzufügen und so die Fähigkeiten des Agenten erweitern, um aktuellen Anforderungen gerecht zu werden.
- Das AI Toolkit enthält Vorlagen (z. B. Python MCP Server-Vorlagen), um die Erstellung benutzerdefinierter Tools zu vereinfachen.

## Zusätzliche Ressourcen

- [AI Toolkit-Dokumentation](https://aka.ms/AIToolkit/doc)

## Was kommt als Nächstes
- Als Nächstes: [Testen & Debuggen](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->