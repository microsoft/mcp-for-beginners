# 📘 Rozwiązanie zadania: Rozszerzenie serwera MCP kalkulatora o narzędzie do pierwiastkowania

## Przegląd
W tym zadaniu rozbudowałeś swój serwer MCP kalkulatora, dodając nowe narzędzie, które oblicza pierwiastek kwadratowy z liczby. To rozszerzenie pozwala Twojemu agentowi AI obsługiwać bardziej zaawansowane zapytania matematyczne, takie jak „Jaki jest pierwiastek kwadratowy z 16?” lub „Oblicz √49” za pomocą naturalnych poleceń.

## 🛠️ Implementacja narzędzia do pierwiastkowania
Aby dodać tę funkcjonalność, zdefiniowałeś nową funkcję narzędzia w pliku server.py. Oto implementacja:

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

## 🔍 Jak to działa

- **Import modułu `math`**: Aby wykonywać operacje matematyczne wykraczające poza podstawowe działania arytmetyczne, Python oferuje wbudowany moduł `math`. Zawiera on różne funkcje i stałe matematyczne. Importując go za pomocą `import math`, uzyskujesz dostęp do funkcji takich jak `math.sqrt()`, która oblicza pierwiastek kwadratowy z liczby.
- **Definicja funkcji**: Dekorator `@server.tool()` rejestruje funkcję `sqrt` jako narzędzie dostępną dla Twojego agenta AI.
- **Parametr wejściowy**: Funkcja przyjmuje jeden argument `a` typu `float`.
- **Obsługa błędów**: Jeśli `a` jest ujemne, funkcja zgłasza wyjątek `ValueError`, aby zapobiec obliczaniu pierwiastka kwadratowego z liczby ujemnej, co nie jest obsługiwane przez funkcję `math.sqrt()`.
- **Wartość zwracana**: Dla wartości nieujemnych funkcja zwraca pierwiastek kwadratowy z `a` za pomocą wbudowanej metody `math.sqrt()`.

## 🔄 Restart serwera
Po dodaniu nowego narzędzia `sqrt` ważne jest, aby zrestartować serwer MCP, aby agent mógł rozpoznać i korzystać z nowo dodanej funkcjonalności.

## 💬 Przykładowe zapytania do przetestowania nowego narzędzia
Oto kilka naturalnych zapytań, które możesz wykorzystać do sprawdzenia działania funkcji pierwiastkowania:

- „Jaki jest pierwiastek kwadratowy z 25?”
- „Oblicz pierwiastek kwadratowy z 81.”
- „Znajdź pierwiastek kwadratowy z 0.”
- „Jaki jest pierwiastek kwadratowy z 2.25?”

Te zapytania powinny spowodować, że agent wywoła narzędzie `sqrt` i zwróci poprawne wyniki.

## ✅ Podsumowanie
Wykonując to zadanie:

- Rozszerzyłeś swój serwer MCP kalkulatora o nowe narzędzie `sqrt`.
- Umożliwiłeś agentowi AI obsługę obliczeń pierwiastka kwadratowego za pomocą naturalnych poleceń.
- Przećwiczyłeś dodawanie nowych narzędzi i restartowanie serwera, aby zintegrować dodatkowe funkcjonalności.

Zachęcam do dalszych eksperymentów i dodawania kolejnych narzędzi matematycznych, takich jak potęgowanie czy funkcje logarytmiczne, aby jeszcze bardziej rozbudować możliwości swojego agenta!

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.