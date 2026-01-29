# MCP-Rechner-Server (Python)

Eine einfache Implementierung eines Model Context Protocol (MCP)-Servers in Python, der grundlegende Rechnerfunktionen bereitstellt.

## Installation

Installieren Sie die erforderlichen Abhängigkeiten:

```bash
pip install -r requirements.txt
```
  
Oder installieren Sie das MCP Python SDK direkt:

```bash
pip install mcp>=1.18.0
```
  

## Verwendung

### Server starten

Der Server ist für die Nutzung durch MCP-Clients (wie Claude Desktop) konzipiert. Um den Server zu starten:

```bash
python mcp_calculator_server.py
```
  
**Hinweis**: Wenn Sie den Server direkt im Terminal ausführen, werden JSON-RPC-Validierungsfehler angezeigt. Dies ist normales Verhalten – der Server wartet auf korrekt formatierte Nachrichten von MCP-Clients.

### Funktionen testen

Um zu überprüfen, ob die Rechnerfunktionen korrekt funktionieren:

```bash
python test_calculator.py
```
  

## Fehlerbehebung

### Importfehler

Falls die Fehlermeldung `ModuleNotFoundError: No module named 'mcp'` erscheint, installieren Sie das MCP Python SDK:

```bash
pip install mcp>=1.18.0
```
  

### JSON-RPC-Fehler bei direkter Ausführung

Fehler wie "Invalid JSON: EOF while parsing a value" beim direkten Ausführen des Servers sind zu erwarten. Der Server benötigt Nachrichten von MCP-Clients und keine direkte Eingabe im Terminal.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.