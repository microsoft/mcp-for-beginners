# 📘 Solusyon sa Takdang-Aralin: Pagpapalawak ng Iyong Calculator MCP Server gamit ang Square Root Tool

## Pangkalahatang-ideya
Sa takdang-aralin na ito, pinalawak mo ang iyong calculator MCP server sa pamamagitan ng pagdagdag ng bagong tool na nagkakalkula ng square root ng isang numero. Ang dagdag na ito ay nagpapahintulot sa iyong AI agent na sagutin ang mas komplikadong mga tanong sa matematika, tulad ng "Ano ang square root ng 16?" o "Kalkulahin ang √49," gamit ang natural na wika.

## 🛠️ Pagpapatupad ng Square Root Tool
Para maidagdag ang functionality na ito, nagdefine ka ng bagong tool function sa iyong server.py file. Narito ang implementasyon:

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

## 🔍 Paano Ito Gumagana

- **I-import ang `math` module**: Para makagawa ng mga operasyong matematika na lampas sa simpleng aritmetika, nagbibigay ang Python ng built-in na `math` module. Kasama dito ang iba't ibang mga mathematical functions at constants. Sa pag-import gamit ang `import math`, nagkakaroon ka ng access sa mga function tulad ng `math.sqrt()`, na nagkakalkula ng square root ng isang numero.
- **Pagdeklara ng Function**: Ang `@server.tool()` decorator ay nagrerehistro sa `sqrt` function bilang isang tool na maaaring gamitin ng iyong AI agent.
- **Input Parameter**: Tumatanggap ang function ng isang argumento na `a` na may uri na `float`.
- **Pag-handle ng Error**: Kung ang `a` ay negatibo, magtataas ang function ng `ValueError` upang maiwasan ang pagkalkula ng square root ng negatibong numero, na hindi sinusuportahan ng `math.sqrt()` function.
- **Return Value**: Para sa mga hindi negatibong input, ibinabalik ng function ang square root ng `a` gamit ang built-in na `math.sqrt()` method ng Python.

## 🔄 Pag-restart ng Server
Matapos maidagdag ang bagong `sqrt` tool, mahalagang i-restart ang iyong MCP server upang matiyak na makikilala at magagamit ng agent ang bagong functionality.

## 💬 Mga Halimbawang Prompt para Subukan ang Bagong Tool
Narito ang ilang natural na wika na prompt na maaari mong gamitin upang subukan ang square root functionality:

- "Ano ang square root ng 25?"
- "Kalkulahin ang square root ng 81."
- "Hanapin ang square root ng 0."
- "Ano ang square root ng 2.25?"

Dapat mag-trigger ang mga prompt na ito sa agent na gamitin ang `sqrt` tool at ibalik ang tamang resulta.

## ✅ Buod
Sa pagtapos ng takdang-aralin na ito, nagawa mong:

- Palawakin ang iyong calculator MCP server gamit ang bagong `sqrt` tool.
- Pahintulutan ang iyong AI agent na magsagawa ng kalkulasyon ng square root gamit ang natural na wika.
- Magpraktis sa pagdagdag ng mga bagong tool at pag-restart ng server para maisama ang karagdagang functionality.

Huwag mag-atubiling mag-eksperimento pa sa pagdagdag ng iba pang mga mathematical tools, tulad ng exponentiation o logarithmic functions, upang lalo pang mapahusay ang kakayahan ng iyong agent!

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.