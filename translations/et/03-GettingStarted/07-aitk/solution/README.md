# 📘 Ülesande lahendus: Kalkulaatori MCP serveri laiendamine ruutjuure tööriistaga

## Ülevaade
Selles ülesandes täiustasite oma kalkulaatori MCP serverit, lisades uue tööriista, mis arvutab arvu ruutjuure. See täiendus võimaldab teie AI-agendil käsitleda keerukamaid matemaatilisi päringuid, nagu "Mis on 16 ruutjuur?" või "Arvuta √49," kasutades loomuliku keele päringuid.

## 🛠️ Ruutjuure tööriista rakendamine
Selle funktsionaalsuse lisamiseks määrasite server.py failis uue tööriista funktsiooni. Siin on selle rakendus:

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

## 🔍 Kuidas see töötab

- **`math` mooduli importimine**: Pythoni sisseehitatud `math` moodul võimaldab teostada matemaatilisi operatsioone, mis ületavad lihtsat aritmeetikat. Selle mooduli kaudu on saadaval mitmesugused matemaatilised funktsioonid ja konstandid. Mooduli importimisega (`import math`) saate kasutada funktsioone nagu `math.sqrt()`, mis arvutab arvu ruutjuure.
- **Funktsiooni määratlus**: `@server.tool()` dekoratsioon registreerib `sqrt` funktsiooni tööriistana, millele teie AI-agent pääseb ligi.
- **Sisendparameeter**: Funktsioon võtab vastu ühe argumendi `a`, mille tüüp on `float`.
- **Vigade käsitlemine**: Kui `a` on negatiivne, viskab funktsioon `ValueError`i, et vältida negatiivse arvu ruutjuure arvutamist, mida `math.sqrt()` funktsioon ei toeta.
- **Tagastusväärtus**: Positiivsete sisendite korral tagastab funktsioon `a` ruutjuure, kasutades Pythoni sisseehitatud `math.sqrt()` meetodit.

## 🔄 Serveri taaskäivitamine
Pärast uue `sqrt` tööriista lisamist on oluline MCP server taaskäivitada, et tagada agendi võimekus tunnustada ja kasutada äsja lisatud funktsionaalsust.

## 💬 Näitepäringud uue tööriista testimiseks
Siin on mõned loomuliku keele päringud, mida saate kasutada ruutjuure funktsionaalsuse testimiseks:

- "Mis on 25 ruutjuur?"
- "Arvuta 81 ruutjuur."
- "Leia 0 ruutjuur."
- "Mis on 2.25 ruutjuur?"

Need päringud peaksid käivitama agendi, et kasutada `sqrt` tööriista ja tagastada õiged tulemused.

## ✅ Kokkuvõte
Selle ülesande täitmisega olete:

- Laiendanud oma kalkulaatori MCP serverit uue `sqrt` tööriistaga.
- Võimaldanud oma AI-agendil käsitleda ruutjuure arvutusi loomuliku keele päringute kaudu.
- Harjutanud uute tööriistade lisamist ja serveri taaskäivitamist, et integreerida täiendavaid funktsioone.

Katsetage julgelt edasi, lisades rohkem matemaatilisi tööriistu, nagu astendamine või logaritmilised funktsioonid, et jätkata oma agendi võimekuse suurendamist!

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.