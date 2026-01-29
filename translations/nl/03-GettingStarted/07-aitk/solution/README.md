# 📘 Oplossing Opdracht: Je Calculator MCP Server Uitbreiden met een Worteltrekker

## Overzicht
In deze opdracht heb je je calculator MCP server uitgebreid met een nieuwe tool die de wortel van een getal berekent. Hierdoor kan je AI-agent complexere wiskundige vragen aan, zoals "Wat is de wortel van 16?" of "Bereken √49," met behulp van natuurlijke taal.

## 🛠️ De Worteltrekker Implementeren
Om deze functionaliteit toe te voegen, heb je een nieuwe toolfunctie gedefinieerd in je server.py bestand. Dit is de implementatie:

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

## 🔍 Hoe Het Werkt

- **Importeer de `math` module**: Om wiskundige bewerkingen uit te voeren die verder gaan dan basisrekenen, biedt Python de ingebouwde `math` module. Deze module bevat diverse wiskundige functies en constanten. Door `import math` te gebruiken, krijg je toegang tot functies zoals `math.sqrt()`, die de wortel van een getal berekent.
- **Functiedefinitie**: De `@server.tool()` decorator registreert de `sqrt` functie als een tool die je AI-agent kan gebruiken.
- **Invoerveld**: De functie accepteert één argument `a` van het type `float`.
- **Foutafhandeling**: Als `a` negatief is, gooit de functie een `ValueError` om te voorkomen dat de wortel van een negatief getal wordt berekend, wat niet wordt ondersteund door `math.sqrt()`.
- **Retourwaarde**: Voor niet-negatieve invoer geeft de functie de wortel van `a` terug met behulp van de ingebouwde `math.sqrt()` methode.

## 🔄 De Server Herstarten
Na het toevoegen van de nieuwe `sqrt` tool is het belangrijk om je MCP server te herstarten zodat de agent de nieuwe functionaliteit herkent en kan gebruiken.

## 💬 Voorbeelden van Prompts om de Nieuwe Tool te Testen
Hier zijn enkele natuurlijke taal prompts die je kunt gebruiken om de wortelfunctie te testen:

- "Wat is de wortel van 25?"
- "Bereken de wortel van 81."
- "Vind de wortel van 0."
- "Wat is de wortel van 2.25?"

Deze prompts zorgen ervoor dat de agent de `sqrt` tool aanroept en de juiste resultaten teruggeeft.

## ✅ Samenvatting
Door deze opdracht af te ronden heb je:

- Je calculator MCP server uitgebreid met een nieuwe `sqrt` tool.
- Je AI-agent in staat gesteld om wortelberekeningen te doen via natuurlijke taal prompts.
- Geoefend met het toevoegen van nieuwe tools en het herstarten van de server om extra functionaliteiten te integreren.

Voel je vrij om verder te experimenteren door meer wiskundige tools toe te voegen, zoals machtsverheffen of logaritmische functies, om de mogelijkheden van je agent verder uit te breiden!

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.