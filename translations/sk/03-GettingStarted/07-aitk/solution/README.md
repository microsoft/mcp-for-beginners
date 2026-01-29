# 📘 Riešenie úlohy: Rozšírenie vášho kalkulačkového MCP servera o nástroj na druhú odmocninu

## Prehľad
V tejto úlohe ste rozšírili svoj kalkulačkový MCP server pridaním nového nástroja, ktorý vypočíta druhú odmocninu čísla. Toto rozšírenie umožňuje vášmu AI agentovi riešiť pokročilejšie matematické otázky, ako napríklad „Aká je druhá odmocnina z 16?“ alebo „Vypočítaj √49“ pomocou prirodzených jazykových príkazov.

## 🛠️ Implementácia nástroja na druhú odmocninu
Na pridanie tejto funkcie ste definovali novú funkciu nástroja v súbore server.py. Tu je implementácia:

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

## 🔍 Ako to funguje

- **Import modulu `math`**: Na vykonávanie matematických operácií nad rámec základnej aritmetiky Python poskytuje vstavaný modul `math`. Tento modul obsahuje množstvo matematických funkcií a konštánt. Importovaním pomocou `import math` získate prístup k funkciám ako `math.sqrt()`, ktorá vypočíta druhú odmocninu čísla.
- **Definícia funkcie**: Dekorátor `@server.tool()` zaregistruje funkciu `sqrt` ako nástroj, ktorý môže používať váš AI agent.
- **Vstupný parameter**: Funkcia prijíma jeden argument `a` typu `float`.
- **Spracovanie chýb**: Ak je `a` záporné, funkcia vyvolá výnimku `ValueError`, aby zabránila výpočtu druhej odmocniny zo záporného čísla, čo funkcia `math.sqrt()` nepodporuje.
- **Návratová hodnota**: Pre nezáporné vstupy funkcia vráti druhú odmocninu čísla `a` pomocou vstavaného Pythonovho `math.sqrt()`.

## 🔄 Reštartovanie servera
Po pridaní nového nástroja `sqrt` je nevyhnutné reštartovať váš MCP server, aby agent rozpoznal a mohol využívať novú funkciu.

## 💬 Príklady príkazov na otestovanie nového nástroja
Tu je niekoľko prirodzených jazykových príkazov, ktoré môžete použiť na otestovanie funkcie druhej odmocniny:

- „Aká je druhá odmocnina z 25?“
- „Vypočítaj druhú odmocninu z 81.“
- „Nájdi druhú odmocninu z 0.“
- „Aká je druhá odmocnina z 2,25?“

Tieto príkazy by mali spustiť volanie nástroja `sqrt` a vrátiť správne výsledky.

## ✅ Zhrnutie
Splnením tejto úlohy ste:

- Rozšírili svoj kalkulačkový MCP server o nový nástroj `sqrt`.
- Umožnili svojmu AI agentovi riešiť výpočty druhej odmocniny pomocou prirodzených jazykových príkazov.
- Precvičili si pridávanie nových nástrojov a reštartovanie servera na integráciu ďalších funkcií.

Neváhajte experimentovať ďalej a pridávať ďalšie matematické nástroje, ako sú umocňovanie alebo logaritmické funkcie, aby ste ešte viac rozšírili schopnosti svojho agenta!

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.