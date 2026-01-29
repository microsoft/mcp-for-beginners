# 📘 Solución de la Tarea: Ampliando tu Servidor MCP de Calculadora con una Herramienta de Raíz Cuadrada

## Resumen
En esta tarea, mejoraste tu servidor MCP de calculadora añadiendo una nueva herramienta que calcula la raíz cuadrada de un número. Esta adición permite que tu agente de IA maneje consultas matemáticas más avanzadas, como "¿Cuál es la raíz cuadrada de 16?" o "Calcula √49", usando indicaciones en lenguaje natural.

## 🛠️ Implementación de la Herramienta de Raíz Cuadrada
Para agregar esta funcionalidad, definiste una nueva función herramienta en tu archivo server.py. Aquí está la implementación:

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

## 🔍 Cómo Funciona

- **Importar el módulo `math`**: Para realizar operaciones matemáticas más allá de la aritmética básica, Python ofrece el módulo incorporado `math`. Este módulo incluye una variedad de funciones y constantes matemáticas. Al importarlo con `import math`, tienes acceso a funciones como `math.sqrt()`, que calcula la raíz cuadrada de un número.
- **Definición de la función**: El decorador `@server.tool()` registra la función `sqrt` como una herramienta accesible para tu agente de IA.
- **Parámetro de entrada**: La función acepta un único argumento `a` de tipo `float`.
- **Manejo de errores**: Si `a` es negativo, la función lanza un `ValueError` para evitar calcular la raíz cuadrada de un número negativo, lo cual no está soportado por la función `math.sqrt()`.
- **Valor de retorno**: Para entradas no negativas, la función devuelve la raíz cuadrada de `a` usando el método incorporado `math.sqrt()` de Python.

## 🔄 Reiniciando el Servidor
Después de agregar la nueva herramienta `sqrt`, es fundamental reiniciar tu servidor MCP para asegurarte de que el agente reconozca y pueda utilizar la funcionalidad recién añadida.

## 💬 Ejemplos de Indicaciones para Probar la Nueva Herramienta
Aquí tienes algunas indicaciones en lenguaje natural que puedes usar para probar la funcionalidad de la raíz cuadrada:

- "¿Cuál es la raíz cuadrada de 25?"
- "Calcula la raíz cuadrada de 81."
- "Encuentra la raíz cuadrada de 0."
- "¿Cuál es la raíz cuadrada de 2.25?"

Estas indicaciones deberían hacer que el agente invoque la herramienta `sqrt` y devuelva los resultados correctos.

## ✅ Resumen
Al completar esta tarea, has:

- Ampliado tu servidor MCP de calculadora con una nueva herramienta `sqrt`.
- Permitido que tu agente de IA maneje cálculos de raíz cuadrada mediante indicaciones en lenguaje natural.
- Practicado cómo agregar nuevas herramientas y reiniciar el servidor para integrar funcionalidades adicionales.

¡Siéntete libre de experimentar añadiendo más herramientas matemáticas, como exponenciación o funciones logarítmicas, para seguir mejorando las capacidades de tu agente!

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.