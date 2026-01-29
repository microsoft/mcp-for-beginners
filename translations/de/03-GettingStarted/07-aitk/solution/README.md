# 📘 Lösung der Aufgabe: Erweiterung Ihres Calculator MCP Servers mit einem Quadratwurzel-Tool

## Überblick
In dieser Aufgabe haben Sie Ihren Calculator MCP Server erweitert, indem Sie ein neues Tool hinzugefügt haben, das die Quadratwurzel einer Zahl berechnet. Diese Erweiterung ermöglicht es Ihrem KI-Agenten, komplexere mathematische Anfragen zu bearbeiten, wie zum Beispiel „Was ist die Quadratwurzel von 16?“ oder „Berechne √49“ mithilfe von natürlichsprachlichen Eingaben.

## 🛠️ Implementierung des Quadratwurzel-Tools
Um diese Funktion hinzuzufügen, haben Sie eine neue Tool-Funktion in Ihrer server.py Datei definiert. Hier ist die Implementierung:

```python
"""
Sample MCP Calculator Server implementation in Python.

This module demonstrates how to create a simple MCP server with calculator tools
that can perform basic arithmetic operations (add, subtract, multiply, divide).
"""

from mcp.server.fastmcp import FastMCP
import math

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

@server.tool()
def sqrt(a: float) -> float:
    """
    Return the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(a)
```

## 🔍 So funktioniert es

- **Import des `math` Moduls**: Um mathematische Operationen über einfache Arithmetik hinaus durchzuführen, stellt Python das eingebaute `math` Modul bereit. Dieses Modul enthält eine Vielzahl mathematischer Funktionen und Konstanten. Durch den Import mit `import math` erhalten Sie Zugriff auf Funktionen wie `math.sqrt()`, die die Quadratwurzel einer Zahl berechnet.
- **Funktionsdefinition**: Der `@server.tool()` Dekorator registriert die Funktion `sqrt` als Tool, das von Ihrem KI-Agenten genutzt werden kann.
- **Eingabeparameter**: Die Funktion nimmt ein einzelnes Argument `a` vom Typ `float` entgegen.
- **Fehlerbehandlung**: Wenn `a` negativ ist, wirft die Funktion einen `ValueError`, um zu verhindern, dass die Quadratwurzel einer negativen Zahl berechnet wird, was von der Funktion `math.sqrt()` nicht unterstützt wird.
- **Rückgabewert**: Für nicht-negative Eingaben gibt die Funktion die Quadratwurzel von `a` zurück, berechnet mit der eingebauten Python-Methode `math.sqrt()`.

## 🔄 Neustart des Servers
Nachdem Sie das neue `sqrt` Tool hinzugefügt haben, ist es wichtig, Ihren MCP Server neu zu starten, damit der Agent die neue Funktionalität erkennt und nutzen kann.

## 💬 Beispielhafte Eingaben zum Testen des neuen Tools
Hier sind einige natürlichsprachliche Eingaben, mit denen Sie die Quadratwurzelfunktion testen können:

- „Was ist die Quadratwurzel von 25?“
- „Berechne die Quadratwurzel von 81.“
- „Finde die Quadratwurzel von 0.“
- „Was ist die Quadratwurzel von 2,25?“

Diese Eingaben sollten den Agenten dazu veranlassen, das `sqrt` Tool aufzurufen und die korrekten Ergebnisse zurückzugeben.

## ✅ Zusammenfassung
Mit Abschluss dieser Aufgabe haben Sie:

- Ihren Calculator MCP Server um ein neues `sqrt` Tool erweitert.
- Ihrem KI-Agenten ermöglicht, Quadratwurzel-Berechnungen über natürlichsprachliche Eingaben durchzuführen.
- Geübt, neue Tools hinzuzufügen und den Server neu zu starten, um zusätzliche Funktionen zu integrieren.

Probieren Sie gerne weitere mathematische Tools aus, wie Potenz- oder Logarithmusfunktionen, um die Fähigkeiten Ihres Agenten weiter zu verbessern!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.