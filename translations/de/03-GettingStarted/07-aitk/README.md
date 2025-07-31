<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-07-31T01:17:54+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "de"
}
-->
# Verwenden eines Servers aus der AI Toolkit-Erweiterung für Visual Studio Code

Beim Erstellen eines KI-Agents geht es nicht nur darum, intelligente Antworten zu generieren, sondern auch darum, dem Agenten die Fähigkeit zu geben, Aktionen auszuführen. Hier kommt das Model Context Protocol (MCP) ins Spiel. MCP ermöglicht es Agenten, externe Tools und Dienste auf konsistente Weise zu nutzen. Stellen Sie sich vor, Sie schließen Ihren Agenten an eine Werkzeugkiste an, die er *tatsächlich* verwenden kann.

Angenommen, Sie verbinden einen Agenten mit Ihrem MCP-Server für einen Taschenrechner. Plötzlich kann Ihr Agent mathematische Operationen ausführen, indem er einfach eine Eingabe wie „Was ist 47 mal 89?“ erhält – ohne dass Sie Logik fest programmieren oder benutzerdefinierte APIs erstellen müssen.

## Überblick

In dieser Lektion erfahren Sie, wie Sie einen MCP-Server für einen Taschenrechner mit einem Agenten verbinden, indem Sie die [AI Toolkit](https://aka.ms/AIToolkit)-Erweiterung in Visual Studio Code verwenden. Dadurch kann Ihr Agent mathematische Operationen wie Addition, Subtraktion, Multiplikation und Division durch natürliche Sprache ausführen.

AI Toolkit ist eine leistungsstarke Erweiterung für Visual Studio Code, die die Entwicklung von Agenten vereinfacht. KI-Ingenieure können damit generative KI-Modelle lokal oder in der Cloud entwickeln und testen. Die Erweiterung unterstützt die meisten gängigen generativen Modelle, die heute verfügbar sind.

*Hinweis*: Das AI Toolkit unterstützt derzeit Python und TypeScript.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Einen MCP-Server über das AI Toolkit zu nutzen.
- Eine Agentenkonfiguration so einzurichten, dass der Agent die vom MCP-Server bereitgestellten Tools entdecken und verwenden kann.
- MCP-Tools über natürliche Sprache zu verwenden.

## Vorgehensweise

So gehen wir auf hoher Ebene vor:

- Einen Agenten erstellen und dessen System-Prompt definieren.
- Einen MCP-Server mit Taschenrechner-Tools erstellen.
- Den Agent Builder mit dem MCP-Server verbinden.
- Die Tool-Nutzung des Agenten durch natürliche Sprache testen.

Super, jetzt, da wir den Ablauf verstanden haben, konfigurieren wir einen KI-Agenten, um externe Tools über MCP zu nutzen und seine Fähigkeiten zu erweitern!

## Voraussetzungen

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit für Visual Studio Code](https://aka.ms/AIToolkit)

## Übung: Einen Server nutzen

> [!WARNING]
> Hinweis für macOS-Nutzer: Wir untersuchen derzeit ein Problem, das die Installation von Abhängigkeiten auf macOS betrifft. Daher können macOS-Nutzer dieses Tutorial derzeit nicht abschließen. Wir werden die Anweisungen aktualisieren, sobald eine Lösung verfügbar ist. Vielen Dank für Ihre Geduld und Ihr Verständnis!

In dieser Übung erstellen, starten und erweitern Sie einen KI-Agenten mit Tools eines MCP-Servers in Visual Studio Code mithilfe des AI Toolkits.

### -0- Vorbereitender Schritt: OpenAI GPT-4o-Modell zu „Meine Modelle“ hinzufügen

Die Übung verwendet das **GPT-4o**-Modell. Das Modell sollte zu **Meine Modelle** hinzugefügt werden, bevor der Agent erstellt wird.

![Screenshot einer Modellauswahloberfläche in der AI Toolkit-Erweiterung von Visual Studio Code. Die Überschrift lautet „Find the right model for your AI Solution“ mit einem Untertitel, der Benutzer dazu ermutigt, KI-Modelle zu entdecken, zu testen und bereitzustellen. Unten werden unter „Popular Models“ sechs Modellkarten angezeigt: DeepSeek-R1 (GitHub-gehostet), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast) und DeepSeek-R1 (Ollama-gehostet). Jede Karte enthält Optionen zum „Hinzufügen“ des Modells oder „Ausprobieren im Playground“.](../../../../translated_images/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.de.png)

1. Öffnen Sie die **AI Toolkit**-Erweiterung in der **Activity Bar**.
1. Wählen Sie im Abschnitt **Catalog** die Option **Models**, um den **Model Catalog** zu öffnen. Die Auswahl von **Models** öffnet den **Model Catalog** in einem neuen Editor-Tab.
1. Geben Sie in die Suchleiste des **Model Catalog** **OpenAI GPT-4o** ein.
1. Klicken Sie auf **+ Add**, um das Modell zu Ihrer Liste **Meine Modelle** hinzuzufügen. Stellen Sie sicher, dass Sie das Modell ausgewählt haben, das **von GitHub gehostet** wird.
1. Überprüfen Sie in der **Activity Bar**, ob das **OpenAI GPT-4o**-Modell in der Liste erscheint.

### -1- Einen Agenten erstellen

Der **Agent (Prompt) Builder** ermöglicht es Ihnen, eigene KI-gestützte Agenten zu erstellen und anzupassen. In diesem Abschnitt erstellen Sie einen neuen Agenten und weisen ihm ein Modell zu, das die Konversation antreibt.

![Screenshot der „Calculator Agent“-Erstellungsoberfläche in der AI Toolkit-Erweiterung für Visual Studio Code. Im linken Bereich ist das ausgewählte Modell „OpenAI GPT-4o (via GitHub)“. Ein System-Prompt lautet „You are a professor in university teaching math“, und der Benutzer-Prompt lautet „Explain to me the Fourier equation in simple terms“. Weitere Optionen umfassen Schaltflächen zum Hinzufügen von Tools, Aktivieren des MCP-Servers und Auswählen strukturierter Ausgaben. Eine blaue „Run“-Schaltfläche befindet sich unten. Im rechten Bereich werden unter „Get Started with Examples“ drei Beispielagenten aufgelistet: Web Developer (mit MCP-Server), Second-Grade Simplifier und Dream Interpreter, jeweils mit kurzen Beschreibungen ihrer Funktionen.](../../../../translated_images/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.de.png)

1. Öffnen Sie die **AI Toolkit**-Erweiterung in der **Activity Bar**.
1. Wählen Sie im Abschnitt **Tools** die Option **Agent (Prompt) Builder**. Die Auswahl von **Agent (Prompt) Builder** öffnet den **Agent (Prompt) Builder** in einem neuen Editor-Tab.
1. Klicken Sie auf die Schaltfläche **+ New Agent**. Die Erweiterung startet einen Einrichtungsassistenten über die **Command Palette**.
1. Geben Sie den Namen **Calculator Agent** ein und drücken Sie **Enter**.
1. Wählen Sie im **Agent (Prompt) Builder** für das Feld **Model** das Modell **OpenAI GPT-4o (via GitHub)** aus.

### -2- Einen System-Prompt für den Agenten erstellen

Nachdem der Agent erstellt wurde, ist es an der Zeit, seine Persönlichkeit und seinen Zweck zu definieren. In diesem Abschnitt verwenden Sie die Funktion **Generate system prompt**, um das beabsichtigte Verhalten des Agenten zu beschreiben – in diesem Fall ein Taschenrechner-Agent – und lassen das Modell den System-Prompt für Sie schreiben.

![Screenshot der „Calculator Agent“-Oberfläche in der AI Toolkit-Erweiterung für Visual Studio Code mit einem geöffneten Modal-Fenster mit dem Titel „Generate a prompt“. Das Modal erklärt, dass eine Prompt-Vorlage durch das Teilen grundlegender Details generiert werden kann, und enthält ein Textfeld mit dem Beispiel-System-Prompt: „You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.“ Unter dem Textfeld befinden sich die Schaltflächen „Close“ und „Generate“. Im Hintergrund ist ein Teil der Agentenkonfiguration sichtbar, einschließlich des ausgewählten Modells „OpenAI GPT-4o (via GitHub)“ und Feldern für System- und Benutzer-Prompts.](../../../../translated_images/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.de.png)

1. Klicken Sie im Abschnitt **Prompts** auf die Schaltfläche **Generate system prompt**. Diese Schaltfläche öffnet den Prompt-Builder, der KI verwendet, um einen System-Prompt für den Agenten zu generieren.
1. Geben Sie im Fenster **Generate a prompt** Folgendes ein: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Klicken Sie auf die Schaltfläche **Generate**. Eine Benachrichtigung erscheint in der unteren rechten Ecke, die bestätigt, dass der System-Prompt generiert wird. Sobald die Generierung abgeschlossen ist, erscheint der Prompt im Feld **System prompt** des **Agent (Prompt) Builder**.
1. Überprüfen Sie den **System prompt** und passen Sie ihn bei Bedarf an.

### -3- Einen MCP-Server erstellen

Nachdem Sie den System-Prompt Ihres Agenten definiert haben, der sein Verhalten und seine Antworten steuert, ist es an der Zeit, den Agenten mit praktischen Fähigkeiten auszustatten. In diesem Abschnitt erstellen Sie einen MCP-Server für einen Taschenrechner mit Tools zur Durchführung von Additions-, Subtraktions-, Multiplikations- und Divisionsberechnungen. Dieser Server ermöglicht es Ihrem Agenten, in Echtzeit mathematische Operationen als Antwort auf natürliche Sprache auszuführen.

![Screenshot des unteren Abschnitts der „Calculator Agent“-Oberfläche in der AI Toolkit-Erweiterung für Visual Studio Code. Es zeigt erweiterbare Menüs für „Tools“ und „Structure output“ sowie ein Dropdown-Menü mit der Bezeichnung „Choose output format“, das auf „text“ eingestellt ist. Rechts befindet sich eine Schaltfläche mit der Bezeichnung „+ MCP Server“ zum Hinzufügen eines Model Context Protocol-Servers. Ein Bildsymbol-Platzhalter wird über dem Abschnitt „Tools“ angezeigt.](../../../../translated_images/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.de.png)

Das AI Toolkit ist mit Vorlagen ausgestattet, die das Erstellen eines eigenen MCP-Servers erleichtern. Wir verwenden die Python-Vorlage, um den MCP-Server für den Taschenrechner zu erstellen.

*Hinweis*: Das AI Toolkit unterstützt derzeit Python und TypeScript.

1. Klicken Sie im Abschnitt **Tools** des **Agent (Prompt) Builder** auf die Schaltfläche **+ MCP Server**. Die Erweiterung startet einen Einrichtungsassistenten über die **Command Palette**.
1. Wählen Sie **+ Add Server**.
1. Wählen Sie **Create a New MCP Server**.
1. Wählen Sie **python-weather** als Vorlage.
1. Wählen Sie **Default folder**, um die MCP-Server-Vorlage zu speichern.
1. Geben Sie folgenden Namen für den Server ein: **Calculator**.
1. Ein neues Visual Studio Code-Fenster wird geöffnet. Wählen Sie **Yes, I trust the authors**.
1. Erstellen Sie im Terminal (**Terminal** > **New Terminal**) eine virtuelle Umgebung: `python -m venv .venv`
1. Aktivieren Sie die virtuelle Umgebung im Terminal:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source venv/bin/activate`
1. Installieren Sie die Abhängigkeiten im Terminal: `pip install -e .[dev]`
1. Erweitern Sie im **Explorer**-Ansichtsbereich der **Activity Bar** das Verzeichnis **src** und wählen Sie **server.py**, um die Datei im Editor zu öffnen.
1. Ersetzen Sie den Code in der Datei **server.py** durch Folgendes und speichern Sie:

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

### -4- Den Agenten mit dem MCP-Server für den Taschenrechner ausführen

Jetzt, da Ihr Agent Tools hat, ist es an der Zeit, diese zu verwenden! In diesem Abschnitt senden Sie Eingaben an den Agenten, um zu testen und zu überprüfen, ob der Agent das entsprechende Tool des MCP-Servers für den Taschenrechner verwendet.

![Screenshot der „Calculator Agent“-Oberfläche in der AI Toolkit-Erweiterung für Visual Studio Code. Im linken Bereich ist unter „Tools“ ein MCP-Server namens local-server-calculator_server hinzugefügt, der vier verfügbare Tools zeigt: add, subtract, multiply und divide. Ein Badge zeigt an, dass vier Tools aktiv sind. Darunter befindet sich ein zusammengeklappter Abschnitt „Structure output“ und eine blaue „Run“-Schaltfläche. Im rechten Bereich wird unter „Model Response“ gezeigt, wie der Agent die Tools multiply und subtract mit den Eingaben {"a": 3, "b": 25} und {"a": 75, "b": 20} aufruft. Die endgültige „Tool Response“ wird als 75.0 angezeigt. Unten erscheint eine Schaltfläche „View Code“.](../../../../translated_images/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.de.png)

Sie führen den MCP-Server für den Taschenrechner auf Ihrem lokalen Entwicklungsrechner über den **Agent Builder** als MCP-Client aus.

1. Drücken Sie `F5`, um das Debugging des MCP-Servers zu starten. Der **Agent (Prompt) Builder** wird in einem neuen Editor-Tab geöffnet. Der Status des Servers ist im Terminal sichtbar.
1. Geben Sie im Feld **User prompt** des **Agent (Prompt) Builder** folgenden Prompt ein: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Klicken Sie auf die Schaltfläche **Run**, um die Antwort des Agenten zu generieren.
1. Überprüfen Sie die Ausgabe des Agenten. Das Modell sollte zu dem Schluss kommen, dass Sie **$55** bezahlt haben.
1. Hier ist eine Aufschlüsselung dessen, was passieren sollte:
    - Der Agent wählt die Tools **multiply** und **subtract**, um bei der Berechnung zu helfen.
    - Die jeweiligen Werte für `a` und `b` werden dem Tool **multiply** zugewiesen.
    - Die jeweiligen Werte für `a` und `b` werden dem Tool **subtract** zugewiesen.
    - Die Antwort jedes Tools wird in der jeweiligen **Tool Response** bereitgestellt.
    - Die endgültige Ausgabe des Modells wird in der abschließenden **Model Response** bereitgestellt.
1. Geben Sie zusätzliche Prompts ein, um den Agenten weiter zu testen. Sie können den vorhandenen Prompt im Feld **User prompt** ändern, indem Sie in das Feld klicken und den vorhandenen Prompt ersetzen.
1. Sobald Sie mit dem Testen des Agenten fertig sind, können Sie den Server über das **Terminal** beenden, indem Sie **CTRL/CMD+C** eingeben, um den Vorgang zu beenden.

## Aufgabe

Versuchen Sie, einen zusätzlichen Tool-Eintrag in Ihrer **server.py**-Datei hinzuzufügen (z. B. die Quadratwurzel einer Zahl zurückgeben). Geben Sie zusätzliche Prompts ein, die den Agenten dazu bringen, Ihr neues Tool (oder bestehende Tools) zu verwenden. Stellen Sie sicher, dass Sie den Server neu starten, um neu hinzugefügte Tools zu laden.

## Lösung

[Lösung](./solution/README.md)

## Wichtige Erkenntnisse

Die wichtigsten Erkenntnisse aus diesem Kapitel sind:

- Die AI Toolkit-Erweiterung ist ein großartiger Client, mit dem Sie MCP-Server und deren Tools nutzen können.
- Sie können neue Tools zu MCP-Servern hinzufügen, um die Fähigkeiten des Agenten zu erweitern und sich entwickelnden Anforderungen anzupassen.
- Das AI Toolkit enthält Vorlagen (z. B. Python-MCP-Server-Vorlagen), um die Erstellung benutzerdefinierter Tools zu vereinfachen.

## Zusätzliche Ressourcen

- [AI Toolkit-Dokumentation](https://aka.ms/AIToolkit/doc)

## Was kommt als Nächstes?
- Weiter: [Testen & Debuggen](../08-testing/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.