# 📘 Feladatmegoldás: A számológép MCP szerverének bővítése négyzetgyök eszközzel

## Áttekintés
Ebben a feladatban kibővítetted a számológép MCP szerveredet egy új eszközzel, amely egy szám négyzetgyökét számolja ki. Ez a kiegészítés lehetővé teszi, hogy az AI ügynököd összetettebb matematikai kérdéseket is kezeljen, például: „Mi 16 négyzetgyöke?” vagy „Számold ki √49”-et, természetes nyelvű utasítások alapján.

## 🛠️ A négyzetgyök eszköz megvalósítása
A funkció hozzáadásához definiáltál egy új eszközfüggvényt a server.py fájlban. Íme a megvalósítás:

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

## 🔍 Hogyan működik

- **A `math` modul importálása**: A Python beépített `math` modulja lehetővé teszi az alapműveleteken túli matematikai számításokat. Ez a modul számos matematikai függvényt és állandót tartalmaz. Az `import math` használatával elérhetővé válik például a `math.sqrt()` függvény, amely egy szám négyzetgyökét számolja ki.
- **Függvénydefiníció**: A `@server.tool()` dekorátor regisztrálja a `sqrt` függvényt eszközként, amelyet az AI ügynök elérhet.
- **Bemeneti paraméter**: A függvény egyetlen `a` nevű, `float` típusú argumentumot fogad.
- **Hibakezelés**: Ha `a` negatív, a függvény `ValueError` kivételt dob, hogy megakadályozza a negatív szám négyzetgyökének kiszámítását, amit a `math.sqrt()` nem támogat.
- **Visszatérési érték**: Nem negatív bemenet esetén a függvény a Python beépített `math.sqrt()` metódusával visszaadja `a` négyzetgyökét.

## 🔄 A szerver újraindítása
Az új `sqrt` eszköz hozzáadása után fontos újraindítani az MCP szervert, hogy az ügynök felismerje és használni tudja az új funkciót.

## 💬 Példamondatok az új eszköz teszteléséhez
Íme néhány természetes nyelvű példa, amivel kipróbálhatod a négyzetgyök funkciót:

- „Mi 25 négyzetgyöke?”
- „Számold ki 81 négyzetgyökét.”
- „Add meg 0 négyzetgyökét.”
- „Mi 2,25 négyzetgyöke?”

Ezek a kérdések az ügynököt a `sqrt` eszköz meghívására ösztönzik, és a helyes eredményt adják vissza.

## ✅ Összefoglalás
A feladat elvégzésével:

- Kibővítetted a számológép MCP szerveredet egy új `sqrt` eszközzel.
- Lehetővé tetted, hogy az AI ügynök négyzetgyök számításokat végezzen természetes nyelvű utasítások alapján.
- Gyakoroltad új eszközök hozzáadását és a szerver újraindítását az új funkciók integrálásához.

Nyugodtan kísérletezz tovább további matematikai eszközök, például hatványozás vagy logaritmusok hozzáadásával, hogy még tovább fejleszd az ügynök képességeit!

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.