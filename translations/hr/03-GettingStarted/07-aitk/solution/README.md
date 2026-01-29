# 📘 Rješenje zadatka: Proširenje vašeg Calculator MCP servera s alatom za izračunavanje kvadratnog korijena

## Pregled
U ovom zadatku ste proširili svoj Calculator MCP server dodavanjem novog alata koji izračunava kvadratni korijen broja. Ova nadogradnja omogućuje vašem AI agentu da rješava složenije matematičke upite, poput "Koliki je kvadratni korijen od 16?" ili "Izračunaj √49," koristeći prirodni jezik.

## 🛠️ Implementacija alata za kvadratni korijen
Da biste dodali ovu funkcionalnost, definirali ste novu funkciju alata u datoteci server.py. Evo implementacije:

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

## 🔍 Kako to radi

- **Uvoz modula `math`**: Za izvođenje matematičkih operacija izvan osnovne aritmetike, Python nudi ugrađeni modul `math`. Ovaj modul sadrži razne matematičke funkcije i konstante. Uvođenjem `import math` dobivate pristup funkcijama poput `math.sqrt()`, koja računa kvadratni korijen broja.
- **Definicija funkcije**: Dekorator `@server.tool()` registrira funkciju `sqrt` kao alat dostupan vašem AI agentu.
- **Ulazni parametar**: Funkcija prima jedan argument `a` tipa `float`.
- **Rukovanje pogreškama**: Ako je `a` negativan, funkcija baca `ValueError` kako bi spriječila izračun kvadratnog korijena negativnog broja, što nije podržano funkcijom `math.sqrt()`.
- **Povratna vrijednost**: Za nenegativne ulaze, funkcija vraća kvadratni korijen broja `a` koristeći ugrađenu Pythonovu metodu `math.sqrt()`.

## 🔄 Ponovno pokretanje servera
Nakon dodavanja novog alata `sqrt`, važno je ponovno pokrenuti MCP server kako bi agent prepoznao i mogao koristiti novu funkcionalnost.

## 💬 Primjeri upita za testiranje novog alata
Evo nekoliko primjera upita na prirodnom jeziku koje možete koristiti za testiranje funkcionalnosti kvadratnog korijena:

- "Koliki je kvadratni korijen od 25?"
- "Izračunaj kvadratni korijen od 81."
- "Pronađi kvadratni korijen od 0."
- "Koliki je kvadratni korijen od 2.25?"

Ovi upiti trebali bi potaknuti agenta da pozove alat `sqrt` i vrati točne rezultate.

## ✅ Sažetak
Završetkom ovog zadatka ste:

- Proširili svoj Calculator MCP server novim alatom `sqrt`.
- Omogućili svom AI agentu da obrađuje izračune kvadratnog korijena putem upita na prirodnom jeziku.
- Vježbali dodavanje novih alata i ponovno pokretanje servera radi integracije dodatnih funkcionalnosti.

Slobodno nastavite s eksperimentiranjem dodavanjem još matematičkih alata, poput potenciranja ili logaritamskih funkcija, kako biste dodatno unaprijedili mogućnosti svog agenta!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.