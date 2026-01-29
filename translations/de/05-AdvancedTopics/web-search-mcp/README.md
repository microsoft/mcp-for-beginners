# Lektion: Aufbau eines Web Search MCP Servers

Dieses Kapitel zeigt, wie man einen praxisnahen KI-Agenten entwickelt, der externe APIs integriert, verschiedene Datentypen verarbeitet, Fehler handhabt und mehrere Tools orchestriert – alles in einem produktionsreifen Format. Du wirst sehen:

- **Integration externer APIs mit Authentifizierung**
- **Umgang mit unterschiedlichen Datentypen von mehreren Endpunkten**
- **Robuste Fehlerbehandlung und Protokollierungsstrategien**
- **Multi-Tool-Orchestrierung in einem einzigen Server**

Am Ende hast du praktische Erfahrung mit Mustern und Best Practices, die für fortgeschrittene KI- und LLM-basierte Anwendungen unerlässlich sind.

## Einführung

In dieser Lektion lernst du, wie man einen fortgeschrittenen MCP-Server und -Client baut, der LLM-Fähigkeiten mit Echtzeit-Webdaten über SerpAPI erweitert. Diese Fähigkeit ist entscheidend, um dynamische KI-Agenten zu entwickeln, die auf aktuelle Informationen aus dem Web zugreifen können.

## Lernziele

Am Ende dieser Lektion wirst du in der Lage sein:

- Externe APIs (wie SerpAPI) sicher in einen MCP-Server zu integrieren
- Mehrere Tools für Web-, Nachrichten-, Produktsuche und Q&A zu implementieren
- Strukturierte Daten für die Nutzung durch LLMs zu parsen und zu formatieren
- Fehler zu behandeln und API-Rate-Limits effektiv zu managen
- Sowohl automatisierte als auch interaktive MCP-Clients zu bauen und zu testen

## Web Search MCP Server

Dieser Abschnitt stellt die Architektur und Funktionen des Web Search MCP Servers vor. Du siehst, wie FastMCP und SerpAPI zusammenarbeiten, um LLM-Fähigkeiten mit Echtzeit-Webdaten zu erweitern.

### Überblick

Diese Implementierung umfasst vier Tools, die die Fähigkeit von MCP demonstrieren, vielfältige, externe API-gesteuerte Aufgaben sicher und effizient zu bewältigen:

- **general_search**: Für allgemeine Web-Ergebnisse
- **news_search**: Für aktuelle Schlagzeilen
- **product_search**: Für E-Commerce-Daten
- **qna**: Für Frage-Antwort-Snippets

### Funktionen
- **Code-Beispiele**: Enthält sprachspezifische Codeblöcke für Python (und leicht auf andere Sprachen erweiterbar) mit Code-Pivots zur besseren Übersicht

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Bevor du den Client startest, ist es hilfreich zu verstehen, was der Server macht. Die Datei [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementiert den MCP-Server, der Tools für Web-, Nachrichten-, Produktsuche und Q&A bereitstellt, indem er SerpAPI integriert. Er verarbeitet eingehende Anfragen, verwaltet API-Aufrufe, parst Antworten und liefert strukturierte Ergebnisse an den Client zurück.

Die vollständige Implementierung kannst du in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) nachlesen.

Hier ein kurzes Beispiel, wie der Server ein Tool definiert und registriert:

### Python Server

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Integration externer APIs**: Zeigt den sicheren Umgang mit API-Schlüsseln und externen Anfragen
- **Strukturierte Datenverarbeitung**: Veranschaulicht, wie API-Antworten in LLM-freundliche Formate umgewandelt werden
- **Fehlerbehandlung**: Robuste Fehlerbehandlung mit passender Protokollierung
- **Interaktiver Client**: Beinhaltet automatisierte Tests und einen interaktiven Modus zum Testen
- **Kontextmanagement**: Nutzt MCP Context für Logging und Nachverfolgung von Anfragen

## Voraussetzungen

Bevor du beginnst, stelle sicher, dass deine Umgebung richtig eingerichtet ist, indem du diese Schritte befolgst. So sind alle Abhängigkeiten installiert und deine API-Schlüssel korrekt konfiguriert für eine reibungslose Entwicklung und Tests.

- Python 3.8 oder höher
- SerpAPI API-Schlüssel (Registrierung unter [SerpAPI](https://serpapi.com/) – kostenlose Stufe verfügbar)

## Installation

Um loszulegen, folge diesen Schritten zur Einrichtung deiner Umgebung:

1. Installiere die Abhängigkeiten mit uv (empfohlen) oder pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Erstelle eine `.env`-Datei im Projektstammverzeichnis mit deinem SerpAPI-Schlüssel:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Nutzung

Der Web Search MCP Server ist die zentrale Komponente, die Tools für Web-, Nachrichten-, Produktsuche und Q&A bereitstellt, indem er SerpAPI integriert. Er verarbeitet eingehende Anfragen, verwaltet API-Aufrufe, parst Antworten und liefert strukturierte Ergebnisse an den Client zurück.

Die vollständige Implementierung findest du in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Server starten

Um den MCP-Server zu starten, verwende folgenden Befehl:

```bash
python server.py
```

Der Server läuft dann als stdio-basierter MCP-Server, mit dem sich der Client direkt verbinden kann.

### Client-Modi

Der Client (`client.py`) unterstützt zwei Modi zur Interaktion mit dem MCP-Server:

- **Normalmodus**: Führt automatisierte Tests aus, die alle Tools durchlaufen und deren Antworten überprüfen. Nützlich, um schnell zu prüfen, ob Server und Tools wie erwartet funktionieren.
- **Interaktiver Modus**: Startet eine menügesteuerte Oberfläche, in der du Tools manuell auswählen, eigene Anfragen eingeben und Ergebnisse in Echtzeit sehen kannst. Ideal, um die Fähigkeiten des Servers zu erkunden und mit verschiedenen Eingaben zu experimentieren.

Die vollständige Implementierung findest du in [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Client ausführen

Um die automatisierten Tests auszuführen (dies startet den Server automatisch):

```bash
python client.py
```

Oder im interaktiven Modus starten:

```bash
python client.py --interactive
```

### Testen mit verschiedenen Methoden

Es gibt mehrere Möglichkeiten, die vom Server bereitgestellten Tools zu testen und zu nutzen, je nach Bedarf und Arbeitsweise.

#### Eigene Testskripte mit dem MCP Python SDK schreiben
Du kannst auch eigene Testskripte mit dem MCP Python SDK erstellen:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

In diesem Zusammenhang bedeutet ein „Testskript“ ein eigenes Python-Programm, das du schreibst, um als Client für den MCP-Server zu fungieren. Statt ein formaler Unit-Test zu sein, erlaubt dir dieses Skript, programmatisch eine Verbindung zum Server herzustellen, beliebige Tools mit selbst gewählten Parametern aufzurufen und die Ergebnisse zu prüfen. Diese Methode ist nützlich für:
- Prototyping und Experimentieren mit Tool-Aufrufen
- Validierung der Serverreaktionen auf verschiedene Eingaben
- Automatisierung wiederholter Tool-Aufrufe
- Aufbau eigener Workflows oder Integrationen auf Basis des MCP-Servers

Mit Testskripten kannst du schnell neue Anfragen ausprobieren, das Verhalten der Tools debuggen oder als Ausgangspunkt für komplexere Automatisierungen nutzen. Unten findest du ein Beispiel, wie du mit dem MCP Python SDK ein solches Skript erstellst:

## Tool-Beschreibungen

Die folgenden Tools, die vom Server bereitgestellt werden, kannst du für verschiedene Such- und Abfragearten verwenden. Jedes Tool wird mit seinen Parametern und Beispielanwendungen beschrieben.

Dieser Abschnitt liefert Details zu jedem verfügbaren Tool und dessen Parametern.

### general_search

Führt eine allgemeine Websuche durch und liefert formatierte Ergebnisse zurück.

**So rufst du dieses Tool auf:**

Du kannst `general_search` aus deinem eigenen Skript mit dem MCP Python SDK aufrufen oder interaktiv über den Inspector oder den interaktiven Client-Modus. Hier ein Codebeispiel mit dem SDK:

# [Python Beispiel](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Alternativ kannst du im interaktiven Modus `general_search` im Menü auswählen und deine Suchanfrage eingeben, wenn du dazu aufgefordert wirst.

**Parameter:**
- `query` (string): Die Suchanfrage

**Beispielanfrage:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Sucht nach aktuellen Nachrichtenartikeln zu einer Anfrage.

**So rufst du dieses Tool auf:**

Du kannst `news_search` aus deinem eigenen Skript mit dem MCP Python SDK aufrufen oder interaktiv über den Inspector oder den interaktiven Client-Modus. Hier ein Codebeispiel mit dem SDK:

# [Python Beispiel](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Alternativ kannst du im interaktiven Modus `news_search` im Menü auswählen und deine Suchanfrage eingeben, wenn du dazu aufgefordert wirst.

**Parameter:**
- `query` (string): Die Suchanfrage

**Beispielanfrage:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Sucht nach Produkten, die zu einer Anfrage passen.

**So rufst du dieses Tool auf:**

Du kannst `product_search` aus deinem eigenen Skript mit dem MCP Python SDK aufrufen oder interaktiv über den Inspector oder den interaktiven Client-Modus. Hier ein Codebeispiel mit dem SDK:

# [Python Beispiel](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Alternativ kannst du im interaktiven Modus `product_search` im Menü auswählen und deine Suchanfrage eingeben, wenn du dazu aufgefordert wirst.

**Parameter:**
- `query` (string): Die Produktsuchanfrage

**Beispielanfrage:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Gibt direkte Antworten auf Fragen aus Suchmaschinen zurück.

**So rufst du dieses Tool auf:**

Du kannst `qna` aus deinem eigenen Skript mit dem MCP Python SDK aufrufen oder interaktiv über den Inspector oder den interaktiven Client-Modus. Hier ein Codebeispiel mit dem SDK:

# [Python Beispiel](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Alternativ kannst du im interaktiven Modus `qna` im Menü auswählen und deine Frage eingeben, wenn du dazu aufgefordert wirst.

**Parameter:**
- `question` (string): Die Frage, auf die eine Antwort gefunden werden soll

**Beispielanfrage:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Code-Details

Dieser Abschnitt liefert Codeausschnitte und Verweise zu den Server- und Client-Implementierungen.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Siehe [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) und [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) für die vollständigen Implementierungsdetails.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Fortgeschrittene Konzepte in dieser Lektion

Bevor du mit dem Bau beginnst, hier einige wichtige fortgeschrittene Konzepte, die im Verlauf dieses Kapitels immer wieder auftauchen. Ihr Verständnis hilft dir, besser folgen zu können, auch wenn du mit ihnen noch nicht vertraut bist:

- **Multi-Tool-Orchestrierung**: Bedeutet, dass mehrere verschiedene Tools (wie Websuche, Nachrichtensuche, Produktsuche und Q&A) innerhalb eines einzigen MCP-Servers laufen. So kann dein Server eine Vielzahl von Aufgaben erledigen, nicht nur eine.
- **Umgang mit API-Rate-Limits**: Viele externe APIs (wie SerpAPI) begrenzen, wie viele Anfragen du in einer bestimmten Zeit stellen kannst. Gute Programme prüfen diese Limits und gehen damit geschickt um, damit deine App nicht abstürzt, wenn du das Limit erreichst.
- **Strukturierte Datenverarbeitung**: API-Antworten sind oft komplex und verschachtelt. Dieses Konzept beschreibt, wie man diese Antworten in saubere, leicht nutzbare Formate umwandelt, die für LLMs oder andere Programme geeignet sind.
- **Fehlerbehebung und -wiederherstellung**: Manchmal läuft etwas schief – vielleicht fällt das Netzwerk aus oder die API liefert unerwartete Daten. Fehlerbehebung bedeutet, dass dein Code solche Probleme abfangen kann und trotzdem nützliche Rückmeldungen gibt, statt abzustürzen.
- **Parameter-Validierung**: Dabei wird geprüft, ob alle Eingaben für deine Tools korrekt und sicher sind. Das umfasst das Setzen von Standardwerten und die Sicherstellung der richtigen Datentypen, was Fehler und Verwirrung vorbeugt.

Dieser Abschnitt hilft dir, häufige Probleme zu erkennen und zu lösen, die beim Arbeiten mit dem Web Search MCP Server auftreten können. Wenn du auf Fehler oder unerwartetes Verhalten stößt, findest du hier Lösungen für die gängigsten Probleme. Schau dir diese Tipps zuerst an – oft lassen sich Probleme so schnell beheben.

## Fehlerbehebung

Beim Arbeiten mit dem Web Search MCP Server können gelegentlich Probleme auftreten – das ist normal bei der Entwicklung mit externen APIs und neuen Tools. Dieser Abschnitt bietet praktische Lösungen für die häufigsten Probleme, damit du schnell wieder weiterarbeiten kannst. Wenn du auf einen Fehler stößt, beginne hier: Die folgenden Tipps behandeln die Probleme, die die meisten Nutzer haben, und lösen dein Problem oft ohne weitere Hilfe.

### Häufige Probleme

Hier sind einige der häufigsten Probleme, auf die Nutzer stoßen, mit klaren Erklärungen und Lösungsschritten:

1. **Fehlender SERPAPI_KEY in der .env-Datei**
   - Wenn du den Fehler `SERPAPI_KEY environment variable not found` siehst, bedeutet das, dass deine Anwendung den API-Schlüssel für SerpAPI nicht findet. Erstelle eine Datei namens `.env` im Projektstammverzeichnis (falls noch nicht vorhanden) und füge eine Zeile wie `SERPAPI_KEY=dein_serpapi_schluessel` hinzu. Ersetze `dein_serpapi_schluessel` durch deinen tatsächlichen Schlüssel von der SerpAPI-Webseite.

2. **Modul nicht gefunden Fehler**
   - Fehler wie `ModuleNotFoundError: No module named 'httpx'` zeigen an, dass ein benötigtes Python-Paket fehlt. Das passiert meist, wenn du nicht alle Abhängigkeiten installiert hast. Führe `pip install -r requirements.txt` im Terminal aus, um alle benötigten Pakete zu installieren.

3. **Verbindungsprobleme**
   - Wenn du einen Fehler wie `Error during client execution` bekommst, kann das bedeuten, dass der Client keine Verbindung zum Server herstellen kann oder der Server nicht wie erwartet läuft. Überprüfe, ob Client und Server kompatible Versionen sind und ob `server.py` im richtigen Verzeichnis vorhanden und gestartet ist. Ein Neustart von Server und Client kann ebenfalls helfen.

4. **SerpAPI-Fehler**
   - Die Meldung `Search API returned error status: 401` bedeutet, dass dein SerpAPI-Schlüssel fehlt, falsch oder abgelaufen ist. Prüfe dein SerpAPI-Dashboard, verifiziere deinen Schlüssel und aktualisiere gegebenenfalls die `.env`-Datei. Wenn der Schlüssel korrekt ist, aber der Fehler weiterhin auftritt, überprüfe, ob dein kostenloses Kontingent aufgebraucht ist.

### Debug-Modus

Standardmäßig protokolliert die App nur wichtige Informationen. Wenn du mehr Details sehen möchtest (z. B. zur Diagnose schwieriger Probleme), kannst du den DEBUG-Modus aktivieren. Dann werden viel mehr Informationen zu jedem Schritt angezeigt.

**Beispiel: Normale Ausgabe**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Beispiel: DEBUG-Ausgabe**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Beachte, dass der DEBUG-Modus zusätzliche Zeilen zu HTTP-Anfragen, Antworten und anderen internen Details enthält. Das ist sehr hilfreich bei der Fehlersuche.
Um den DEBUG-Modus zu aktivieren, setzen Sie das Protokollierungslevel oben in Ihrer `client.py` oder `server.py` auf DEBUG:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Was kommt als Nächstes

- [5.10 Echtzeit-Streaming](../mcp-realtimestreaming/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.