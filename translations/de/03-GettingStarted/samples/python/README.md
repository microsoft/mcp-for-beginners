# MCP Rechner Server (Python)



Eine einfache Model Context Protocol (MCP) Server-Implementierung in Python, die grundlegende Rechnerfunktionen bereitstellt.


## Installation

Installiere die erforderlichen Abhängigkeiten:

```bash
pip install -r requirements.txt
```

Oder installiere direkt das MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Nutzung

### Server starten

Der Server ist für die Nutzung durch MCP-Clients (wie Claude Desktop) ausgelegt. Um den Server zu starten:

```bash
python mcp_calculator_server.py
```

**Hinweis**: Wenn der Server direkt im Terminal ausgeführt wird, wirst du JSON-RPC Validierungsfehler sehen. Das ist normales Verhalten – der Server wartet auf korrekt formatierte MCP-Client-Nachrichten.

### Funktionen testen

Um zu testen, ob die Rechnerfunktionen korrekt funktionieren:

```bash
python test_calculator.py
```

## Fehlerbehebung

### Importfehler

Wenn du den Fehler `ModuleNotFoundError: No module named 'mcp'` siehst, installiere das MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC Fehler beim direkten Ausführen

Fehler wie „Invalid JSON: EOF while parsing a value“ beim direkten Ausführen des Servers sind zu erwarten. Der Server benötigt MCP-Client-Nachrichten, keine direkte Eingabe im Terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->