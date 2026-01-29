# Verwenden eines Servers aus der AI Toolkit-Erweiterung für Visual Studio Code

Beim Erstellen eines KI-Agenten geht es nicht nur darum, intelligente Antworten zu generieren, sondern auch darum, dem Agenten die Fähigkeit zu geben, Aktionen auszuführen. Hier kommt das Model Context Protocol (MCP) ins Spiel. MCP ermöglicht es Agenten, externe Tools und Dienste auf konsistente Weise zu nutzen. Stellen Sie sich vor, Sie schließen Ihren Agenten an eine Werkzeugkiste an, die er *tatsächlich* verwenden kann.

Angenommen, Sie verbinden einen Agenten mit Ihrem MCP-Server für einen Taschenrechner. Plötzlich kann Ihr Agent mathematische Operationen ausführen, indem er einfach eine Eingabe wie „Was ergibt 47 mal 89?“ erhält – ohne dass Sie Logik fest einprogrammieren oder benutzerdefinierte APIs erstellen müssen.

## Überblick

In dieser Lektion erfahren Sie, wie Sie einen MCP-Server für einen Taschenrechner mit einem Agenten verbinden, der mit der [AI Toolkit](https://aka.ms/AIToolkit)-Erweiterung in Visual Studio Code arbeitet. Dadurch kann Ihr Agent mathematische Operationen wie Addition, Subtraktion, Multiplikation und Division über natürliche Sprache ausführen.

AI Toolkit ist eine leistungsstarke Erweiterung für Visual Studio Code, die die Entwicklung von KI-Agenten vereinfacht. KI-Ingenieure können KI-Anwendungen einfach erstellen, indem sie generative KI-Modelle lokal oder in der Cloud entwickeln und testen. Die Erweiterung unterstützt die meisten gängigen generativen Modelle, die heute verfügbar sind.

*Hinweis*: Das AI Toolkit unterstützt derzeit Python und TypeScript.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Einen MCP-Server über das AI Toolkit zu nutzen.
- Eine Agentenkonfiguration so einzurichten, dass der Agent die vom MCP-Server bereitgestellten Tools entdecken und verwenden kann.
- MCP-Tools über natürliche Sprache zu nutzen.

## Vorgehensweise

So gehen wir auf hoher Ebene vor:

- Einen Agenten erstellen und dessen System-Prompt definieren.
- Einen MCP-Server mit Taschenrechner-Tools erstellen.
- Den Agent Builder mit dem MCP-Server verbinden.
- Die Tool-Nutzung des Agenten über natürliche Sprache testen.

Super, jetzt, da wir den Ablauf verstehen, konfigurieren wir einen KI-Agenten, um externe Tools über MCP zu nutzen und seine Fähigkeiten zu erweitern!

## Voraussetzungen

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit für Visual Studio Code](https://aka.ms/AIToolkit)

## Übung: Einen Server nutzen

> [!WARNING]
> Hinweis für macOS-Nutzer. Wir untersuchen derzeit ein Problem, das die Installation von Abhängigkeiten auf macOS betrifft. Daher können macOS-Nutzer dieses Tutorial derzeit nicht abschließen. Wir werden die Anweisungen aktualisieren, sobald eine Lösung verfügbar ist. Vielen Dank für Ihre Geduld und Ihr Verständnis!

In dieser Übung erstellen, starten und erweitern Sie einen KI-Agenten mit Tools von einem MCP-Server innerhalb von Visual Studio Code mithilfe des AI Toolkits.

### -0- Vorbereitender Schritt: Das OpenAI GPT-4o-Modell zu „Meine Modelle“ hinzufügen

Die Übung verwendet das **GPT-4o**-Modell. Das Modell sollte zu **Meine Modelle** hinzugefügt werden, bevor der Agent erstellt wird.

1. Öffnen Sie die **AI Toolkit**-Erweiterung in der **Activity Bar**.
1. Wählen Sie im Abschnitt **Katalog** die Option **Modelle**, um den **Modellkatalog** zu öffnen. Durch die Auswahl von **Modelle** wird der **Modellkatalog** in einem neuen Editor-Tab geöffnet.
1. Geben Sie im Suchfeld des **Modellkatalogs** **OpenAI GPT-4o** ein.
1. Klicken Sie auf **+ Hinzufügen**, um das Modell zu Ihrer Liste **Meine Modelle** hinzuzufügen. Stellen Sie sicher, dass Sie das Modell ausgewählt haben, das **von GitHub gehostet wird**.
1. Bestätigen Sie in der **Activity Bar**, dass das **OpenAI GPT-4o**-Modell in der Liste erscheint.

### -1- Einen Agenten erstellen

Der **Agent (Prompt) Builder** ermöglicht es Ihnen, eigene KI-gestützte Agenten zu erstellen und anzupassen. In diesem Abschnitt erstellen Sie einen neuen Agenten und weisen ihm ein Modell zu, das die Konversation antreibt.

1. Öffnen Sie die **AI Toolkit**-Erweiterung in der **Activity Bar**.
1. Wählen Sie im Abschnitt **Tools** die Option **Agent (Prompt) Builder**. Durch die Auswahl von **Agent (Prompt) Builder** wird der **Agent (Prompt) Builder** in einem neuen Editor-Tab geöffnet.
1. Klicken Sie auf die Schaltfläche **+ Neuer Agent**. Die Erweiterung startet einen Einrichtungsassistenten über die **Command Palette**.
1. Geben Sie den Namen **Calculator Agent** ein und drücken Sie **Enter**.
1. Wählen Sie im **Agent (Prompt) Builder** für das Feld **Modell** das Modell **OpenAI GPT-4o (via GitHub)** aus.

### -2- Einen System-Prompt für den Agenten erstellen

Nachdem der Agent erstellt wurde, ist es an der Zeit, seine Persönlichkeit und seinen Zweck zu definieren. In diesem Abschnitt verwenden Sie die Funktion **System-Prompt generieren**, um das beabsichtigte Verhalten des Agenten zu beschreiben – in diesem Fall ein Taschenrechner-Agent – und lassen das Modell den System-Prompt für Sie schreiben.

1. Klicken Sie im Abschnitt **Prompts** auf die Schaltfläche **System-Prompt generieren**. Diese Schaltfläche öffnet den Prompt-Builder, der KI nutzt, um einen System-Prompt für den Agenten zu generieren.
1. Geben Sie im Fenster **Einen Prompt generieren** Folgendes ein: `Du bist ein hilfreicher und effizienter Mathematik-Assistent. Wenn dir ein Problem mit grundlegender Arithmetik gegeben wird, antwortest du mit dem korrekten Ergebnis.`
1. Klicken Sie auf die Schaltfläche **Generieren**. Eine Benachrichtigung erscheint unten rechts, die bestätigt, dass der System-Prompt generiert wird. Sobald die Generierung abgeschlossen ist, erscheint der Prompt im Feld **System-Prompt** des **Agent (Prompt) Builder**.
1. Überprüfen Sie den **System-Prompt** und passen Sie ihn bei Bedarf an.

### -3- Einen MCP-Server erstellen

Nachdem Sie den System-Prompt des Agenten definiert haben, der sein Verhalten und seine Antworten steuert, ist es an der Zeit, den Agenten mit praktischen Fähigkeiten auszustatten. In diesem Abschnitt erstellen Sie einen MCP-Server für einen Taschenrechner mit Tools, die Addition, Subtraktion, Multiplikation und Division ausführen können. Dieser Server ermöglicht es Ihrem Agenten, in Echtzeit mathematische Operationen als Antwort auf natürliche Spracheingaben auszuführen.

Das AI Toolkit ist mit Vorlagen ausgestattet, die das Erstellen eines eigenen MCP-Servers erleichtern. Wir verwenden die Python-Vorlage, um den MCP-Server für den Taschenrechner zu erstellen.

*Hinweis*: Das AI Toolkit unterstützt derzeit Python und TypeScript.

1. Klicken Sie im Abschnitt **Tools** des **Agent (Prompt) Builder** auf die Schaltfläche **+ MCP-Server**. Die Erweiterung startet einen Einrichtungsassistenten über die **Command Palette**.
1. Wählen Sie **+ Server hinzufügen**.
1. Wählen Sie **Einen neuen MCP-Server erstellen**.
1. Wählen Sie **python-weather** als Vorlage.
1. Wählen Sie **Standardordner**, um die MCP-Server-Vorlage zu speichern.
1. Geben Sie den folgenden Namen für den Server ein: **Calculator**
1. Ein neues Visual Studio Code-Fenster wird geöffnet. Wählen Sie **Ja, ich vertraue den Autoren**.
1. Erstellen Sie über das Terminal (**Terminal** > **Neues Terminal**) eine virtuelle Umgebung: `python -m venv .venv`
1. Aktivieren Sie die virtuelle Umgebung über das Terminal:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Installieren Sie die Abhängigkeiten über das Terminal: `pip install -e .[dev]`
1. Erweitern Sie im **Explorer**-Ansicht der **Activity Bar** das Verzeichnis **src** und wählen Sie **server.py**, um die Datei im Editor zu öffnen.
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

Jetzt, da Ihr Agent Tools hat, ist es an der Zeit, diese zu nutzen! In diesem Abschnitt geben Sie Eingaben an den Agenten, um zu testen und zu validieren, ob der Agent das passende Tool vom MCP-Server für den Taschenrechner verwendet.

1. Drücken Sie `F5`, um das Debugging des MCP-Servers zu starten. Der **Agent (Prompt) Builder** wird in einem neuen Editor-Tab geöffnet. Der Status des Servers ist im Terminal sichtbar.
1. Geben Sie im Feld **Benutzer-Prompt** des **Agent (Prompt) Builder** den folgenden Prompt ein: `Ich habe 3 Artikel für je 25 $ gekauft und dann einen Rabatt von 20 $ genutzt. Wie viel habe ich bezahlt?`
1. Klicken Sie auf die Schaltfläche **Ausführen**, um die Antwort des Agenten zu generieren.
1. Überprüfen Sie die Ausgabe des Agenten. Das Modell sollte zu dem Schluss kommen, dass Sie **55 $** bezahlt haben.
1. Hier ist eine Übersicht darüber, was passieren sollte:
    - Der Agent wählt die Tools **multiply** und **subtract**, um bei der Berechnung zu helfen.
    - Die jeweiligen Werte `a` und `b` werden dem Tool **multiply** zugewiesen.
    - Die jeweiligen Werte `a` und `b` werden dem Tool **subtract** zugewiesen.
    - Die Antwort jedes Tools wird in der jeweiligen **Tool-Antwort** bereitgestellt.
    - Die endgültige Ausgabe des Modells wird in der **Modell-Antwort** bereitgestellt.
1. Geben Sie weitere Prompts ein, um den Agenten weiter zu testen. Sie können den bestehenden Prompt im Feld **Benutzer-Prompt** ändern, indem Sie in das Feld klicken und den bestehenden Prompt ersetzen.
1. Sobald Sie mit dem Testen des Agenten fertig sind, können Sie den Server über das **Terminal** stoppen, indem Sie **CTRL/CMD+C** eingeben, um ihn zu beenden.

## Aufgabe

Versuchen Sie, einen zusätzlichen Tool-Eintrag zu Ihrer Datei **server.py** hinzuzufügen (z. B. die Quadratwurzel einer Zahl zurückgeben). Geben Sie zusätzliche Prompts ein, die den Agenten dazu bringen, Ihr neues Tool (oder bestehende Tools) zu nutzen. Stellen Sie sicher, dass Sie den Server neu starten, um neu hinzugefügte Tools zu laden.

## Lösung

[Lösung](./solution/README.md)

## Wichtige Erkenntnisse

Die wichtigsten Erkenntnisse aus diesem Kapitel sind:

- Die AI Toolkit-Erweiterung ist ein großartiger Client, mit dem Sie MCP-Server und deren Tools nutzen können.
- Sie können neue Tools zu MCP-Servern hinzufügen, um die Fähigkeiten des Agenten zu erweitern und sich an sich ändernde Anforderungen anzupassen.
- Das AI Toolkit enthält Vorlagen (z. B. Python-MCP-Server-Vorlagen), um die Erstellung benutzerdefinierter Tools zu vereinfachen.

## Zusätzliche Ressourcen

- [AI Toolkit-Dokumentation](https://aka.ms/AIToolkit/doc)

## Was kommt als Nächstes?
- Weiter: [Testen & Debuggen](../08-testing/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.