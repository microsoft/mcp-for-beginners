# 📘 Soluția temei: Extinderea serverului MCP al calculatorului tău cu un instrument pentru rădăcina pătrată

## Prezentare generală
În această temă, ai îmbunătățit serverul MCP al calculatorului tău prin adăugarea unui nou instrument care calculează rădăcina pătrată a unui număr. Această completare permite agentului tău AI să gestioneze interogări matematice mai avansate, cum ar fi „Care este rădăcina pătrată a lui 16?” sau „Calculează √49,” folosind comenzi în limbaj natural.

## 🛠️ Implementarea instrumentului pentru rădăcina pătrată
Pentru a adăuga această funcționalitate, ai definit o nouă funcție de instrument în fișierul server.py. Iată implementarea:

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

## 🔍 Cum funcționează

- **Importarea modulului `math`**: Pentru a efectua operații matematice dincolo de aritmetica de bază, Python oferă modulul încorporat `math`. Acest modul include o varietate de funcții și constante matematice. Prin importarea lui cu `import math`, ai acces la funcții precum `math.sqrt()`, care calculează rădăcina pătrată a unui număr.
- **Definirea funcției**: Decoratorul `@server.tool()` înregistrează funcția `sqrt` ca un instrument accesibil agentului tău AI.
- **Parametrul de intrare**: Funcția primește un singur argument `a` de tip `float`.
- **Gestionarea erorilor**: Dacă `a` este negativ, funcția ridică o excepție `ValueError` pentru a preveni calcularea rădăcinii pătrate a unui număr negativ, ceea ce nu este suportat de funcția `math.sqrt()`.
- **Valoarea returnată**: Pentru valori nenegative, funcția returnează rădăcina pătrată a lui `a` folosind metoda încorporată `math.sqrt()` din Python.

## 🔄 Repornirea serverului
După adăugarea noului instrument `sqrt`, este esențial să repornești serverul MCP pentru ca agentul să recunoască și să poată folosi funcționalitatea nou adăugată.

## 💬 Exemple de comenzi pentru testarea noului instrument
Iată câteva comenzi în limbaj natural pe care le poți folosi pentru a testa funcționalitatea rădăcinii pătrate:

- „Care este rădăcina pătrată a lui 25?”
- „Calculează rădăcina pătrată a lui 81.”
- „Găsește rădăcina pătrată a lui 0.”
- „Care este rădăcina pătrată a lui 2.25?”

Aceste comenzi ar trebui să determine agentul să apeleze instrumentul `sqrt` și să returneze rezultatele corecte.

## ✅ Rezumat
Prin finalizarea acestei teme, ai:

- Extins serverul MCP al calculatorului tău cu un nou instrument `sqrt`.
- Permis agentului tău AI să efectueze calcule cu rădăcina pătrată prin comenzi în limbaj natural.
- Exersat adăugarea de noi instrumente și repornirea serverului pentru a integra funcționalități suplimentare.

Simte-te liber să experimentezi mai departe adăugând alte instrumente matematice, cum ar fi ridicarea la putere sau funcții logaritmice, pentru a continua să îmbunătățești capabilitățile agentului tău!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.