# 📘 Assignment Solution: Add Square Root Tool for Your Calculator MCP Server

## Overview
For dis assignment, you don improve your calculator MCP server by put new tool wey fit calculate square root of number. Dis new tool go make your AI agent sabi handle more advanced maths question like "Wetin be di square root of 16?" or "Calculate √49," just by using natural language prompts.

## 🛠️ How to Add di Square Root Tool
To add dis feature, you go define new tool function for your server.py file. See di implementation:

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

## 🔍 How E Dey Work

- **Import di `math` module**: To do maths operation wey pass basic arithmetic, Python get built-in `math` module. Dis module get plenty maths functions and constants. If you import am with `import math`, you go fit use functions like `math.sqrt()`, wey dey calculate square root of number.
- **Function Definition**: Di `@server.tool()` decorator go register di `sqrt` function as tool wey your AI agent fit use.
- **Input Parameter**: Di function dey take one argument `a` wey be type `float`.
- **Error Handling**: If `a` na negative number, di function go throw `ValueError` to stop am from trying to calculate square root of negative number, because `math.sqrt()` no dey support am.
- **Return Value**: If di input no be negative, di function go return di square root of `a` using Python built-in `math.sqrt()` method.

## 🔄 Restart di Server
After you don add di new `sqrt` tool, you need to restart your MCP server so dat di agent go sabi and fit use di new feature wey you add.

## 💬 Example Prompts to Test di New Tool
Try use dis natural language prompts to test di square root feature:

- "Wetin be di square root of 25?"
- "Calculate di square root of 81."
- "Find di square root of 0."
- "Wetin be di square root of 2.25?"

Dis prompts go make di agent use di `sqrt` tool and give you di correct answer.

## ✅ Summary
As you don finish dis assignment, you don:

- Add new `sqrt` tool to your calculator MCP server.
- Make your AI agent sabi calculate square root through natural language prompts.
- Practice how to add new tools and restart di server to add more features.

Feel free to try add more maths tools like exponentiation or logarithmic functions to make your agent sabi do more things!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translet service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translet. Even as we dey try make am correct, abeg sabi say AI translet fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important mata, e good make professional human translet am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translet.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->