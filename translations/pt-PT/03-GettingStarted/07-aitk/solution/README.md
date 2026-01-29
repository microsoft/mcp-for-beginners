# 📘 Solução do Exercício: Expandir o Seu Servidor MCP da Calculadora com uma Ferramenta de Raiz Quadrada

## Visão Geral
Neste exercício, melhorou o seu servidor MCP da calculadora ao adicionar uma nova ferramenta que calcula a raiz quadrada de um número. Esta adição permite que o seu agente de IA lide com consultas matemáticas mais avançadas, como "Qual é a raiz quadrada de 16?" ou "Calcula √49", usando comandos em linguagem natural.

## 🛠️ Implementação da Ferramenta de Raiz Quadrada
Para adicionar esta funcionalidade, definiu uma nova função de ferramenta no seu ficheiro server.py. Eis a implementação:

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

## 🔍 Como Funciona

- **Importar o módulo `math`**: Para realizar operações matemáticas além da aritmética básica, o Python disponibiliza o módulo incorporado `math`. Este módulo inclui várias funções e constantes matemáticas. Ao importá-lo com `import math`, tem acesso a funções como `math.sqrt()`, que calcula a raiz quadrada de um número.
- **Definição da Função**: O decorador `@server.tool()` regista a função `sqrt` como uma ferramenta acessível pelo seu agente de IA.
- **Parâmetro de Entrada**: A função aceita um único argumento `a` do tipo `float`.
- **Gestão de Erros**: Se `a` for negativo, a função lança um `ValueError` para evitar calcular a raiz quadrada de um número negativo, o que não é suportado pela função `math.sqrt()`.
- **Valor de Retorno**: Para entradas não negativas, a função devolve a raiz quadrada de `a` usando o método incorporado `math.sqrt()` do Python.

## 🔄 Reiniciar o Servidor
Após adicionar a nova ferramenta `sqrt`, é essencial reiniciar o seu servidor MCP para garantir que o agente reconhece e pode utilizar a funcionalidade recém-adicionada.

## 💬 Exemplos de Comandos para Testar a Nova Ferramenta
Aqui estão alguns comandos em linguagem natural que pode usar para testar a funcionalidade da raiz quadrada:

- "Qual é a raiz quadrada de 25?"
- "Calcula a raiz quadrada de 81."
- "Encontra a raiz quadrada de 0."
- "Qual é a raiz quadrada de 2.25?"

Estes comandos devem fazer com que o agente invoque a ferramenta `sqrt` e devolva os resultados corretos.

## ✅ Resumo
Ao completar este exercício, você:

- Expandiu o seu servidor MCP da calculadora com uma nova ferramenta `sqrt`.
- Permitiu que o seu agente de IA realizasse cálculos de raiz quadrada através de comandos em linguagem natural.
- Praticou a adição de novas ferramentas e o reinício do servidor para integrar funcionalidades adicionais.

Sinta-se à vontade para experimentar mais, adicionando outras ferramentas matemáticas, como exponenciação ou funções logarítmicas, para continuar a melhorar as capacidades do seu agente!

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.