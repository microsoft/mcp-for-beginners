# 📘 Oppgaveløsning: Utvidelse av kalkulator-MCP-serveren din med et verktøy for kvadratrot

## Oversikt
I denne oppgaven har du utvidet kalkulator-MCP-serveren din ved å legge til et nytt verktøy som beregner kvadratroten av et tall. Denne tilleggsmuligheten gjør at AI-agenten din kan håndtere mer avanserte matematiske spørsmål, som for eksempel «Hva er kvadratroten av 16?» eller «Beregn √49», ved hjelp av naturlige språkkommandoer.

## 🛠️ Implementering av verktøyet for kvadratrot
For å legge til denne funksjonaliteten definerte du en ny verktøyfunksjon i filen server.py. Her er implementeringen:

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

## 🔍 Slik fungerer det

- **Importer `math`-modulen**: For å utføre matematiske operasjoner utover enkel aritmetikk, tilbyr Python den innebygde `math`-modulen. Denne modulen inneholder en rekke matematiske funksjoner og konstanter. Ved å importere den med `import math` får du tilgang til funksjoner som `math.sqrt()`, som beregner kvadratroten av et tall.
- **Funksjonsdefinisjon**: Dekoratoren `@server.tool()` registrerer funksjonen `sqrt` som et verktøy som AI-agenten din kan bruke.
- **Inndata**: Funksjonen tar ett argument `a` av typen `float`.
- **Feilhåndtering**: Hvis `a` er negativ, kaster funksjonen en `ValueError` for å forhindre at kvadratroten av et negativt tall beregnes, noe som ikke støttes av `math.sqrt()`.
- **Returverdi**: For ikke-negative verdier returnerer funksjonen kvadratroten av `a` ved hjelp av Pythons innebygde `math.sqrt()`-metode.

## 🔄 Restart av serveren
Etter å ha lagt til det nye `sqrt`-verktøyet, er det viktig å restarte MCP-serveren slik at agenten gjenkjenner og kan bruke den nye funksjonaliteten.

## 💬 Eksempelkommandoer for å teste det nye verktøyet
Her er noen naturlige språkkommandoer du kan bruke for å teste kvadratrot-funksjonaliteten:

- «Hva er kvadratroten av 25?»
- «Beregn kvadratroten av 81.»
- «Finn kvadratroten av 0.»
- «Hva er kvadratroten av 2,25?»

Disse kommandoene skal få agenten til å kalle `sqrt`-verktøyet og returnere riktige resultater.

## ✅ Oppsummering
Ved å fullføre denne oppgaven har du:

- Utvidet kalkulator-MCP-serveren din med et nytt `sqrt`-verktøy.
- Gjort det mulig for AI-agenten å håndtere kvadratrotberegninger via naturlige språkkommandoer.
- Øvd på å legge til nye verktøy og restarte serveren for å integrere ekstra funksjonalitet.

Prøv gjerne å eksperimentere videre ved å legge til flere matematiske verktøy, som potensregning eller logaritmefunksjoner, for å fortsette å forbedre agentens evner!

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.