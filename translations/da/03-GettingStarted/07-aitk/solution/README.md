# 📘 Opgaveløsning: Udvidelse af din Calculator MCP-server med et Kvadratrodsværktøj

## Oversigt
I denne opgave har du udvidet din calculator MCP-server ved at tilføje et nyt værktøj, der beregner kvadratroden af et tal. Denne tilføjelse gør det muligt for din AI-agent at håndtere mere avancerede matematiske forespørgsler, som for eksempel "Hvad er kvadratroden af 16?" eller "Beregn √49," ved hjælp af naturlige sprogkommandoer.

## 🛠️ Implementering af Kvadratrodsværktøjet
For at tilføje denne funktionalitet definerede du en ny værktøjsfunktion i din server.py-fil. Her er implementeringen:

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

## 🔍 Sådan fungerer det

- **Importer `math`-modulet**: For at udføre matematiske operationer ud over grundlæggende regning tilbyder Python det indbyggede `math`-modul. Dette modul indeholder en række matematiske funktioner og konstanter. Ved at importere det med `import math` får du adgang til funktioner som `math.sqrt()`, der beregner kvadratroden af et tal.
- **Funktionsdefinition**: `@server.tool()`-dekorationen registrerer `sqrt`-funktionen som et værktøj, der kan tilgås af din AI-agent.
- **Inputparameter**: Funktionen tager et enkelt argument `a` af typen `float`.
- **Fejlhåndtering**: Hvis `a` er negativ, kaster funktionen en `ValueError` for at forhindre beregning af kvadratroden af et negativt tal, hvilket ikke understøttes af `math.sqrt()`-funktionen.
- **Returneringsværdi**: For ikke-negative input returnerer funktionen kvadratroden af `a` ved hjælp af Pythons indbyggede `math.sqrt()`-metode.

## 🔄 Genstart af serveren
Efter at have tilføjet det nye `sqrt`-værktøj er det vigtigt at genstarte din MCP-server, så agenten kan genkende og bruge den nyligt tilføjede funktionalitet.

## 💬 Eksempelkommandoer til at teste det nye værktøj
Her er nogle naturlige sprogkommandoer, du kan bruge til at teste kvadratrodsfunktionen:

- "Hvad er kvadratroden af 25?"
- "Beregn kvadratroden af 81."
- "Find kvadratroden af 0."
- "Hvad er kvadratroden af 2,25?"

Disse kommandoer skulle få agenten til at kalde `sqrt`-værktøjet og returnere de korrekte resultater.

## ✅ Opsummering
Ved at gennemføre denne opgave har du:

- Udvidet din calculator MCP-server med et nyt `sqrt`-værktøj.
- Givet din AI-agent mulighed for at håndtere kvadratrodsberegninger via naturlige sprogkommandoer.
- Øvet dig i at tilføje nye værktøjer og genstarte serveren for at integrere ekstra funktioner.

Du er velkommen til at eksperimentere videre ved at tilføje flere matematiske værktøjer, som for eksempel potens- eller logaritmefunktioner, for at fortsætte med at forbedre din agents evner!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.