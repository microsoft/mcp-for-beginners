<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-08-07T08:33:00+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "de"
}
-->
# Verwenden eines Servers aus der AI Toolkit-Erweiterung für Visual Studio Code

Beim Erstellen eines KI-Agenten geht es nicht nur darum, intelligente Antworten zu generieren, sondern auch darum, dem Agenten die Fähigkeit zu geben, Aktionen auszuführen. Hier kommt das Model Context Protocol (MCP) ins Spiel. MCP ermöglicht es Agenten, externe Tools und Dienste auf konsistente Weise zu nutzen. Stellen Sie sich vor, Sie schließen Ihren Agenten an eine Werkzeugkiste an, die er *tatsächlich* verwenden kann.

Angenommen, Sie verbinden einen Agenten mit Ihrem MCP-Server für einen Taschenrechner. Plötzlich kann Ihr Agent mathematische Operationen ausführen, indem er einfach eine Eingabe wie „Was ist 47 mal 89?“ erhält – ohne dass Sie Logik fest programmieren oder benutzerdefinierte APIs erstellen müssen.

## Überblick

In dieser Lektion erfahren Sie, wie Sie einen MCP-Server für einen Taschenrechner mit einem Agenten verbinden, indem Sie die [AI Toolkit](https://aka.ms/AIToolkit)-Erweiterung in Visual Studio Code verwenden. Dadurch kann Ihr Agent mathematische Operationen wie Addition, Subtraktion, Multiplikation und Division in natürlicher Sprache ausführen.

Das AI Toolkit ist eine leistungsstarke Erweiterung für Visual Studio Code, die die Entwicklung von Agenten vereinfacht. KI-Ingenieure können damit KI-Anwendungen entwickeln und generative KI-Modelle lokal oder in der Cloud testen. Die Erweiterung unterstützt die meisten gängigen generativen Modelle, die heute verfügbar sind.

*Hinweis*: Das AI Toolkit unterstützt derzeit Python und TypeScript.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Einen MCP-Server über das AI Toolkit zu nutzen.
- Eine Agentenkonfiguration so einzurichten, dass der Agent die vom MCP-Server bereitgestellten Tools entdecken und verwenden kann.
- MCP-Tools über natürliche Sprache zu verwenden.

## Vorgehensweise

So gehen wir auf hoher Ebene vor:

- Einen Agenten erstellen und dessen Systemaufforderung definieren.
- Einen MCP-Server mit Taschenrechner-Tools erstellen.
- Den Agent Builder mit dem MCP-Server verbinden.
- Die Tool-Nutzung des Agenten über natürliche Sprache testen.

Super, jetzt, da wir den Ablauf verstanden haben, konfigurieren wir einen KI-Agenten, um externe Tools über MCP zu nutzen und seine Fähigkeiten zu erweitern!

## Voraussetzungen

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit für Visual Studio Code](https://aka.ms/AIToolkit)

## Übung: Einen Server nutzen

> [!WARNING]
> Hinweis für macOS-Nutzer: Wir untersuchen derzeit ein Problem, das die Installation von Abhängigkeiten auf macOS betrifft. Daher können macOS-Nutzer dieses Tutorial momentan nicht abschließen. Wir werden die Anweisungen aktualisieren, sobald eine Lösung verfügbar ist. Vielen Dank für Ihre Geduld und Ihr Verständnis!

In dieser Übung erstellen, starten und erweitern Sie einen KI-Agenten mit Tools eines MCP-Servers in Visual Studio Code mithilfe des AI Toolkits.

### -0- Vorbereitender Schritt: OpenAI GPT-4o-Modell zu „Meine Modelle“ hinzufügen

Die Übung verwendet das **GPT-4o**-Modell. Das Modell sollte zu **Meine Modelle** hinzugefügt werden, bevor der Agent erstellt wird.

1. Öffnen Sie die **AI Toolkit**-Erweiterung in der **Activity Bar**.
1. Wählen Sie im Abschnitt **Katalog** die Option **Modelle**, um den **Modellkatalog** zu öffnen. Die Auswahl von **Modelle** öffnet den **Modellkatalog** in einem neuen Editor-Tab.
1. Geben Sie im Suchfeld des **Modellkatalogs** **OpenAI GPT-4o** ein.
1. Klicken Sie auf **+ Hinzufügen**, um das Modell zu Ihrer Liste **Meine Modelle** hinzuzufügen. Stellen Sie sicher, dass Sie das Modell auswählen, das **von GitHub gehostet** wird.
1. Bestätigen Sie in der **Activity Bar**, dass das **OpenAI GPT-4o**-Modell in der Liste erscheint.

### -1- Einen Agenten erstellen

Der **Agent (Prompt) Builder** ermöglicht es Ihnen, eigene KI-gestützte Agenten zu erstellen und anzupassen. In diesem Abschnitt erstellen Sie einen neuen Agenten und weisen ihm ein Modell zu, das die Konversation antreibt.

1. Öffnen Sie die **AI Toolkit**-Erweiterung in der **Activity Bar**.
1. Wählen Sie im Abschnitt **Tools** die Option **Agent (Prompt) Builder**. Die Auswahl von **Agent (Prompt) Builder** öffnet den **Agent (Prompt) Builder** in einem neuen Editor-Tab.
1. Klicken Sie auf die Schaltfläche **+ Neuer Agent**. Die Erweiterung startet einen Einrichtungsassistenten über die **Befehls-Palette**.
1. Geben Sie den Namen **Calculator Agent** ein und drücken Sie **Enter**.
1. Wählen Sie im **Agent (Prompt) Builder** für das Feld **Modell** das Modell **OpenAI GPT-4o (via GitHub)** aus.

### -2- Eine Systemaufforderung für den Agenten erstellen

Nachdem der Agent erstellt wurde, ist es an der Zeit, seine Persönlichkeit und seinen Zweck zu definieren. In diesem Abschnitt verwenden Sie die Funktion **Systemaufforderung generieren**, um das beabsichtigte Verhalten des Agenten zu beschreiben – in diesem Fall ein Taschenrechner-Agent – und lassen das Modell die Systemaufforderung für Sie schreiben.

1. Klicken Sie im Abschnitt **Aufforderungen** auf die Schaltfläche **Systemaufforderung generieren**. Diese Schaltfläche öffnet den Prompt-Builder, der KI verwendet, um eine Systemaufforderung für den Agenten zu generieren.
1. Geben Sie im Fenster **Eine Aufforderung generieren** Folgendes ein: `Sie sind ein hilfreicher und effizienter Mathematik-Assistent. Bei Problemen mit grundlegender Arithmetik geben Sie das korrekte Ergebnis zurück.`
1. Klicken Sie auf die Schaltfläche **Generieren**. Eine Benachrichtigung erscheint in der unteren rechten Ecke, die bestätigt, dass die Systemaufforderung generiert wird. Sobald die Generierung abgeschlossen ist, erscheint die Aufforderung im Feld **Systemaufforderung** des **Agent (Prompt) Builders**.
1. Überprüfen Sie die **Systemaufforderung** und passen Sie sie bei Bedarf an.

### -3- Einen MCP-Server erstellen

Nachdem Sie die Systemaufforderung Ihres Agenten definiert haben, die sein Verhalten und seine Antworten steuert, ist es an der Zeit, den Agenten mit praktischen Fähigkeiten auszustatten. In diesem Abschnitt erstellen Sie einen MCP-Server für einen Taschenrechner mit Tools zur Ausführung von Additions-, Subtraktions-, Multiplikations- und Divisionsberechnungen. Dieser Server ermöglicht es Ihrem Agenten, in Echtzeit mathematische Operationen als Antwort auf Eingaben in natürlicher Sprache auszuführen.

Das AI Toolkit enthält Vorlagen, die das Erstellen eigener MCP-Server erleichtern. Wir verwenden die Python-Vorlage, um den MCP-Server für den Taschenrechner zu erstellen.

*Hinweis*: Das AI Toolkit unterstützt derzeit Python und TypeScript.

1. Klicken Sie im Abschnitt **Tools** des **Agent (Prompt) Builders** auf die Schaltfläche **+ MCP Server**. Die Erweiterung startet einen Einrichtungsassistenten über die **Befehls-Palette**.
1. Wählen Sie **+ Server hinzufügen**.
1. Wählen Sie **Einen neuen MCP-Server erstellen**.
1. Wählen Sie **python-weather** als Vorlage.
1. Wählen Sie **Standardordner**, um die MCP-Server-Vorlage zu speichern.
1. Geben Sie den folgenden Namen für den Server ein: **Calculator**
1. Ein neues Visual Studio Code-Fenster wird geöffnet. Wählen Sie **Ja, ich vertraue den Autoren**.
1. Erstellen Sie im Terminal (**Terminal** > **Neues Terminal**) eine virtuelle Umgebung: `python -m venv .venv`
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

Jetzt, da Ihr Agent über Tools verfügt, ist es an der Zeit, diese zu nutzen! In diesem Abschnitt senden Sie Eingaben an den Agenten, um zu testen und zu validieren, ob der Agent das passende Tool des MCP-Servers für den Taschenrechner verwendet.

1. Drücken Sie `F5`, um den MCP-Server zu debuggen. Der **Agent (Prompt) Builder** wird in einem neuen Editor-Tab geöffnet. Der Status des Servers ist im Terminal sichtbar.
1. Geben Sie im Feld **Benutzeraufforderung** des **Agent (Prompt) Builders** die folgende Eingabe ein: `Ich habe 3 Artikel zu je 25 $ gekauft und dann einen Rabatt von 20 $ genutzt. Wie viel habe ich bezahlt?`
1. Klicken Sie auf die Schaltfläche **Ausführen**, um die Antwort des Agenten zu generieren.
1. Überprüfen Sie die Ausgabe des Agenten. Das Modell sollte zu dem Schluss kommen, dass Sie **55 $** bezahlt haben.
1. Hier ist eine Aufschlüsselung dessen, was passieren sollte:
    - Der Agent wählt die Tools **multiply** und **subtract**, um bei der Berechnung zu helfen.
    - Die jeweiligen Werte für `a` und `b` werden dem Tool **multiply** zugewiesen.
    - Die jeweiligen Werte für `a` und `b` werden dem Tool **subtract** zugewiesen.
    - Die Antwort jedes Tools wird in der jeweiligen **Tool-Antwort** bereitgestellt.
    - Die endgültige Ausgabe des Modells wird in der **Modellantwort** bereitgestellt.
1. Geben Sie zusätzliche Eingaben ein, um den Agenten weiter zu testen. Sie können die vorhandene Eingabe im Feld **Benutzeraufforderung** ändern, indem Sie in das Feld klicken und die vorhandene Eingabe ersetzen.
1. Sobald Sie mit dem Testen des Agenten fertig sind, können Sie den Server über das **Terminal** beenden, indem Sie **CTRL/CMD+C** eingeben.

## Aufgabe

Versuchen Sie, Ihrem **server.py**-File einen zusätzlichen Tool-Eintrag hinzuzufügen (z. B. die Quadratwurzel einer Zahl zurückgeben). Geben Sie zusätzliche Eingaben ein, die den Agenten dazu bringen, Ihr neues Tool (oder bestehende Tools) zu verwenden. Starten Sie den Server neu, um neu hinzugefügte Tools zu laden.

## Lösung

[Lösung](./solution/README.md)

## Wichtige Erkenntnisse

Die wichtigsten Erkenntnisse aus diesem Kapitel sind:

- Die AI Toolkit-Erweiterung ist ein großartiger Client, mit dem Sie MCP-Server und deren Tools nutzen können.
- Sie können neue Tools zu MCP-Servern hinzufügen, um die Fähigkeiten des Agenten an sich ändernde Anforderungen anzupassen.
- Das AI Toolkit enthält Vorlagen (z. B. Python-MCP-Server-Vorlagen), um die Erstellung benutzerdefinierter Tools zu vereinfachen.

## Zusätzliche Ressourcen

- [AI Toolkit-Dokumentation](https://aka.ms/AIToolkit/doc)

## Was kommt als Nächstes?
- Weiter: [Testen & Debuggen](../08-testing/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.