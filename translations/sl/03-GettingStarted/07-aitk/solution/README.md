# 📘 Rešitev naloge: Razširitev vašega kalkulator MCP strežnika z orodjem za kvadratni koren

## Pregled
V tej nalogi ste izboljšali svoj kalkulator MCP strežnik z dodajanjem novega orodja, ki izračuna kvadratni koren števila. Ta dodatek omogoča vašemu AI agentu, da obravnava bolj zahtevna matematična vprašanja, kot so "Kolikšen je kvadratni koren števila 16?" ali "Izračunaj √49," z uporabo naravnih jezikovnih ukazov.

## 🛠️ Implementacija orodja za kvadratni koren
Za dodajanje te funkcionalnosti ste v datoteki server.py definirali novo funkcijo orodja. Tukaj je implementacija:

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

## 🔍 Kako deluje

- **Uvoz modula `math`**: Za izvajanje matematičnih operacij, ki presegajo osnovno aritmetiko, Python ponuja vgrajeni modul `math`. Ta modul vsebuje različne matematične funkcije in konstante. Z uvozom z `import math` pridobite dostop do funkcij, kot je `math.sqrt()`, ki izračuna kvadratni koren števila.
- **Definicija funkcije**: Dekorator `@server.tool()` registrira funkcijo `sqrt` kot orodje, ki je dostopno vašemu AI agentu.
- **Vhodni parameter**: Funkcija sprejme en argument `a` tipa `float`.
- **Obravnava napak**: Če je `a` negativno, funkcija sproži izjemo `ValueError`, da prepreči izračun kvadratnega korena negativnega števila, kar funkcija `math.sqrt()` ne podpira.
- **Vrednost, ki jo vrne**: Za nenegativne vrednosti funkcija vrne kvadratni koren `a` z uporabo vgrajene metode `math.sqrt()`.

## 🔄 Ponovni zagon strežnika
Po dodajanju novega orodja `sqrt` je pomembno, da ponovno zaženete MCP strežnik, da agent prepozna in lahko uporablja novo funkcionalnost.

## 💬 Primeri ukazov za testiranje novega orodja
Tukaj je nekaj naravnih jezikovnih ukazov, ki jih lahko uporabite za testiranje funkcionalnosti kvadratnega korena:

- "Kolikšen je kvadratni koren števila 25?"
- "Izračunaj kvadratni koren števila 81."
- "Poišči kvadratni koren števila 0."
- "Kolikšen je kvadratni koren števila 2.25?"

Ti ukazi bi morali sprožiti agenta, da pokliče orodje `sqrt` in vrne pravilne rezultate.

## ✅ Povzetek
Z dokončanjem te naloge ste:

- Razširili svoj kalkulator MCP strežnik z novim orodjem `sqrt`.
- Omogočili vašemu AI agentu, da izračunava kvadratne korene preko naravnih jezikovnih ukazov.
- Vadili dodajanje novih orodij in ponovni zagon strežnika za integracijo dodatnih funkcionalnosti.

Brez zadržkov nadaljujte z eksperimentiranjem in dodajanjem še več matematičnih orodij, kot so potenciranje ali logaritmične funkcije, da še naprej izboljšujete zmogljivosti vašega agenta!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.