# 📘 Užduoties sprendimas: Skaičiuoklės MCP serverio išplėtimas kvadratinės šaknies įrankiu

## Apžvalga
Šioje užduotyje jūs patobulinote savo skaičiuoklės MCP serverį, pridėdami naują įrankį, kuris apskaičiuoja skaičiaus kvadratinę šaknį. Šis papildymas leidžia jūsų AI agentui spręsti sudėtingesnius matematinius užklausimus, tokius kaip „Kokia yra 16 kvadratinė šaknis?“ arba „Apskaičiuokite √49“, naudojant natūralios kalbos užklausas.

## 🛠️ Kvadratinės šaknies įrankio įgyvendinimas
Norėdami pridėti šią funkciją, jūs apibrėžėte naują įrankio funkciją savo server.py faile. Štai jos įgyvendinimas:

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

## 🔍 Kaip tai veikia

- **`math` modulio importavimas**: Norint atlikti matematines operacijas, kurios viršija paprastą aritmetiką, Python siūlo įmontuotą `math` modulį. Šis modulis apima įvairias matematines funkcijas ir konstantas. Importuodami jį su `import math`, jūs gaunate prieigą prie funkcijų, tokių kaip `math.sqrt()`, kuri apskaičiuoja skaičiaus kvadratinę šaknį.
- **Funkcijos apibrėžimas**: Dekoratorius `@server.tool()` registruoja `sqrt` funkciją kaip įrankį, prieinamą jūsų AI agentui.
- **Įvesties parametras**: Funkcija priima vieną argumentą `a`, kurio tipas yra `float`.
- **Klaidų tvarkymas**: Jei `a` yra neigiamas, funkcija iškelia `ValueError`, kad išvengtų bandymo apskaičiuoti neigiamo skaičiaus kvadratinę šaknį, nes `math.sqrt()` funkcija to nepalaiko.
- **Grąžinimo reikšmė**: Jei įvestis yra neneigiama, funkcija grąžina skaičiaus `a` kvadratinę šaknį, naudodama Python įmontuotą `math.sqrt()` metodą.

## 🔄 Serverio paleidimas iš naujo
Pridėjus naują `sqrt` įrankį, būtina iš naujo paleisti MCP serverį, kad agentas atpažintų ir galėtų naudoti naujai pridėtą funkcionalumą.

## 💬 Pavyzdinės užklausos naujo įrankio testavimui
Štai keletas natūralios kalbos užklausų, kurias galite naudoti kvadratinės šaknies funkcionalumo testavimui:

- „Kokia yra 25 kvadratinė šaknis?“
- „Apskaičiuokite 81 kvadratinę šaknį.“
- „Raskite 0 kvadratinę šaknį.“
- „Kokia yra 2.25 kvadratinė šaknis?“

Šios užklausos turėtų paskatinti agentą iškviesti `sqrt` įrankį ir grąžinti teisingus rezultatus.

## ✅ Santrauka
Atlikdami šią užduotį, jūs:

- Išplėtėte savo skaičiuoklės MCP serverį nauju `sqrt` įrankiu.
- Suteikėte savo AI agentui galimybę atlikti kvadratinės šaknies skaičiavimus naudojant natūralios kalbos užklausas.
- Praktikavotės pridėdami naujus įrankius ir paleisdami serverį iš naujo, kad integruotumėte papildomas funkcijas.

Eksperimentuokite toliau, pridėdami daugiau matematinių įrankių, tokių kaip laipsniavimas ar logaritminės funkcijos, kad dar labiau praplėstumėte savo agento galimybes!

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.