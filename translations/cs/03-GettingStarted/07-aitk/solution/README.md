# 📘 Řešení úkolu: Rozšíření vašeho kalkulačního MCP serveru o nástroj pro druhou odmocninu

## Přehled
V tomto úkolu jste rozšířili svůj kalkulační MCP server přidáním nového nástroje, který počítá druhou odmocninu čísla. Toto rozšíření umožňuje vašemu AI agentovi zpracovávat pokročilejší matematické dotazy, jako například „Jaká je druhá odmocnina z 16?“ nebo „Spočítej √49“ pomocí přirozených jazykových příkazů.

## 🛠️ Implementace nástroje pro druhou odmocninu
Pro přidání této funkce jste definovali novou funkci nástroje ve vašem souboru server.py. Zde je implementace:

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

## 🔍 Jak to funguje

- **Import modulu `math`**: Pro provádění matematických operací nad rámec základních aritmetických funkcí Python nabízí vestavěný modul `math`. Tento modul obsahuje různé matematické funkce a konstanty. Importem pomocí `import math` získáte přístup k funkcím jako `math.sqrt()`, která vypočítá druhou odmocninu čísla.
- **Definice funkce**: Dekorátor `@server.tool()` zaregistruje funkci `sqrt` jako nástroj, ke kterému má váš AI agent přístup.
- **Vstupní parametr**: Funkce přijímá jeden argument `a` typu `float`.
- **Zpracování chyb**: Pokud je `a` záporné, funkce vyvolá `ValueError`, aby zabránila výpočtu druhé odmocniny ze záporného čísla, což funkce `math.sqrt()` nepodporuje.
- **Návratová hodnota**: Pro nezáporné vstupy funkce vrací druhou odmocninu čísla `a` pomocí vestavěné metody `math.sqrt()`.

## 🔄 Restartování serveru
Po přidání nového nástroje `sqrt` je důležité restartovat váš MCP server, aby agent rozpoznal a mohl využívat nově přidanou funkčnost.

## 💬 Příklady příkazů pro otestování nového nástroje
Zde je několik přirozených jazykových příkazů, které můžete použít k otestování funkce druhé odmocniny:

- „Jaká je druhá odmocnina z 25?“
- „Spočítej druhou odmocninu z 81.“
- „Najdi druhou odmocninu z 0.“
- „Jaká je druhá odmocnina z 2.25?“

Tyto příkazy by měly vyvolat volání nástroje `sqrt` a vrátit správné výsledky.

## ✅ Shrnutí
Dokončením tohoto úkolu jste:

- Rozšířili svůj kalkulační MCP server o nový nástroj `sqrt`.
- Umožnili vašemu AI agentovi provádět výpočty druhé odmocniny pomocí přirozených jazykových příkazů.
- Procvičili si přidávání nových nástrojů a restartování serveru pro integraci dalších funkcí.

Neváhejte dále experimentovat přidáváním dalších matematických nástrojů, jako jsou umocňování nebo logaritmické funkce, a pokračujte tak v rozšiřování schopností vašeho agenta!

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.