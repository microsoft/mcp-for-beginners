# 📘 Uppgiftslösning: Utöka din Calculator MCP-server med ett verktyg för kvadratroten

## Översikt
I denna uppgift har du förbättrat din calculator MCP-server genom att lägga till ett nytt verktyg som beräknar kvadratroten av ett tal. Denna tillägg gör det möjligt för din AI-agent att hantera mer avancerade matematiska frågor, som "Vad är kvadratroten av 16?" eller "Beräkna √49," med hjälp av naturliga språkkommandon.

## 🛠️ Implementera verktyget för kvadratroten
För att lägga till denna funktionalitet definierade du en ny verktygsfunktion i din server.py-fil. Här är implementeringen:

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

## 🔍 Så fungerar det

- **Importera `math`-modulen**: För att utföra matematiska operationer utöver grundläggande aritmetik erbjuder Python den inbyggda `math`-modulen. Denna modul innehåller en mängd matematiska funktioner och konstanter. Genom att importera den med `import math` får du tillgång till funktioner som `math.sqrt()`, som beräknar kvadratroten av ett tal.
- **Funktionsdefinition**: Dekoratorn `@server.tool()` registrerar funktionen `sqrt` som ett verktyg som din AI-agent kan använda.
- **Inparametrar**: Funktionen tar emot ett argument `a` av typen `float`.
- **Felhantering**: Om `a` är negativt kastar funktionen ett `ValueError` för att förhindra beräkning av kvadratroten av ett negativt tal, vilket inte stöds av `math.sqrt()`.
- **Returvärde**: För icke-negativa värden returnerar funktionen kvadratroten av `a` med hjälp av Pythons inbyggda metod `math.sqrt()`.

## 🔄 Starta om servern
Efter att ha lagt till det nya verktyget `sqrt` är det viktigt att starta om din MCP-server för att säkerställa att agenten känner igen och kan använda den nya funktionaliteten.

## 💬 Exempel på kommandon för att testa det nya verktyget
Här är några naturliga språkkommandon du kan använda för att testa kvadratrotsfunktionen:

- "Vad är kvadratroten av 25?"
- "Beräkna kvadratroten av 81."
- "Hitta kvadratroten av 0."
- "Vad är kvadratroten av 2.25?"

Dessa kommandon bör få agenten att anropa verktyget `sqrt` och returnera rätt resultat.

## ✅ Sammanfattning
Genom att slutföra denna uppgift har du:

- Utökat din calculator MCP-server med ett nytt verktyg `sqrt`.
- Gjort det möjligt för din AI-agent att hantera kvadratrotsberäkningar via naturliga språkkommandon.
- Övat på att lägga till nya verktyg och starta om servern för att integrera ytterligare funktioner.

Känn dig fri att experimentera vidare genom att lägga till fler matematiska verktyg, som exponentiering eller logaritmfunktioner, för att fortsätta förbättra din agents kapacitet!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.