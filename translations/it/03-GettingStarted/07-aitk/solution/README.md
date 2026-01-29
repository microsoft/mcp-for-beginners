# 📘 Soluzione dell’Assegnazione: Estendere il tuo Server MCP del Calcolatore con uno Strumento per la Radice Quadrata

## Panoramica
In questa assegnazione, hai migliorato il tuo server MCP del calcolatore aggiungendo un nuovo strumento che calcola la radice quadrata di un numero. Questa aggiunta permette al tuo agente AI di gestire query matematiche più avanzate, come "Qual è la radice quadrata di 16?" o "Calcola √49," utilizzando comandi in linguaggio naturale.

## 🛠️ Implementazione dello Strumento Radice Quadrata
Per aggiungere questa funzionalità, hai definito una nuova funzione strumento nel file server.py. Ecco l’implementazione:

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

## 🔍 Come Funziona

- **Importare il modulo `math`**: Per eseguire operazioni matematiche oltre l’aritmetica di base, Python offre il modulo integrato `math`. Questo modulo include diverse funzioni e costanti matematiche. Importandolo con `import math`, puoi usare funzioni come `math.sqrt()`, che calcola la radice quadrata di un numero.
- **Definizione della funzione**: Il decoratore `@server.tool()` registra la funzione `sqrt` come uno strumento accessibile dal tuo agente AI.
- **Parametro di input**: La funzione accetta un singolo argomento `a` di tipo `float`.
- **Gestione degli errori**: Se `a` è negativo, la funzione solleva un `ValueError` per evitare di calcolare la radice quadrata di un numero negativo, operazione non supportata da `math.sqrt()`.
- **Valore di ritorno**: Per input non negativi, la funzione restituisce la radice quadrata di `a` usando il metodo integrato `math.sqrt()` di Python.

## 🔄 Riavvio del Server
Dopo aver aggiunto il nuovo strumento `sqrt`, è fondamentale riavviare il server MCP per assicurarti che l’agente riconosca e possa utilizzare la nuova funzionalità.

## 💬 Esempi di Comandi per Testare il Nuovo Strumento
Ecco alcuni comandi in linguaggio naturale che puoi usare per testare la funzionalità della radice quadrata:

- "Qual è la radice quadrata di 25?"
- "Calcola la radice quadrata di 81."
- "Trova la radice quadrata di 0."
- "Qual è la radice quadrata di 2.25?"

Questi comandi dovrebbero far sì che l’agente invochi lo strumento `sqrt` e restituisca i risultati corretti.

## ✅ Riepilogo
Completando questa assegnazione, hai:

- Esteso il tuo server MCP del calcolatore con un nuovo strumento `sqrt`.
- Permesso al tuo agente AI di gestire calcoli di radice quadrata tramite comandi in linguaggio naturale.
- Messo in pratica l’aggiunta di nuovi strumenti e il riavvio del server per integrare funzionalità aggiuntive.

Sentiti libero di sperimentare ulteriormente aggiungendo altri strumenti matematici, come l’esponenziazione o le funzioni logaritmiche, per continuare a potenziare le capacità del tuo agente!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.