# 📘 Suluhisho la Kazi ya Nyumbani: Kupanua Server ya Calculator MCP kwa Zana ya Mizizi ya Mraba

## Muhtasari
Katika kazi hii ya nyumbani, umeongeza server yako ya calculator MCP kwa kuongeza zana mpya inayohesabu mizizi ya mraba ya nambari. Nyongeza hii inaruhusu wakala wako wa AI kushughulikia maswali ya hisabati ya hali ya juu, kama vile "Mizizi ya mraba ya 16 ni nini?" au "Hesabu √49," kwa kutumia maelekezo ya lugha ya asili.

## 🛠️ Kutekeleza Zana ya Mizizi ya Mraba
Ili kuongeza uwezo huu, uliunda kazi mpya ya zana katika faili yako ya server.py. Hapa ni utekelezaji wake:

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

## 🔍 Jinsi Inavyofanya Kazi

- **Ingiza moduli ya `math`**: Ili kufanya operesheni za hisabati zaidi ya hesabu za msingi, Python inatoa moduli ya ndani ya `math`. Moduli hii ina kazi mbalimbali za hisabati na thamani za kudumu. Kwa kuingiza moduli hii kwa kutumia `import math`, unapata ufikiaji wa kazi kama `math.sqrt()`, inayohesabu mizizi ya mraba ya nambari.
- **Ufafanuzi wa Kazi**: Dekoreta `@server.tool()` hujisajili kazi ya `sqrt` kama zana inayopatikana kwa wakala wako wa AI.
- **Kiparameta cha Ingizo**: Kazi inakubali hoja moja `a` ya aina `float`.
- **Kushughulikia Makosa**: Ikiwa `a` ni hasi, kazi itatoa `ValueError` ili kuzuia kuhesabu mizizi ya mraba ya nambari hasi, jambo ambalo halitekelezeki na kazi ya `math.sqrt()`.
- **Thamani ya Kurudisha**: Kwa ingizo zisizo hasi, kazi inarudisha mizizi ya mraba ya `a` kwa kutumia njia ya ndani ya Python `math.sqrt()`.

## 🔄 Kuwasha Upya Server
Baada ya kuongeza zana mpya ya `sqrt`, ni muhimu kuwasha upya server yako ya MCP ili kuhakikisha wakala anaitambua na kuweza kutumia uwezo mpya ulioungwa mkono.

## 💬 Mifano ya Maelekezo ya Kupima Zana Mpya
Hapa kuna mifano ya maelekezo ya lugha ya asili unayoweza kutumia kupima uwezo wa mizizi ya mraba:

- "Mizizi ya mraba ya 25 ni nini?"
- "Hesabu mizizi ya mraba ya 81."
- "Tafuta mizizi ya mraba ya 0."
- "Mizizi ya mraba ya 2.25 ni nini?"

Maelekezo haya yanapaswa kusababisha wakala kuitumia zana ya `sqrt` na kurudisha matokeo sahihi.

## ✅ Muhtasari
Kwa kumaliza kazi hii ya nyumbani, umefanya:

- Kupanua server yako ya calculator MCP kwa zana mpya ya `sqrt`.
- Kumwezesha wakala wako wa AI kushughulikia hesabu za mizizi ya mraba kupitia maelekezo ya lugha ya asili.
- Kufanya mazoezi ya kuongeza zana mpya na kuwasha upya server ili kuunganisha uwezo zaidi.

Jisikie huru kujaribu zaidi kwa kuongeza zana nyingine za hisabati, kama vile nguvu au kazi za logaritimu, ili kuendelea kuboresha uwezo wa wakala wako!

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.