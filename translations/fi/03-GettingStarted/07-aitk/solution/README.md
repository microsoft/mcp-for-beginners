# 📘 Tehtävän Ratkaisu: Laajenna Laskimesi MCP-palvelinta Neliöjuurityökalulla

## Yleiskatsaus
Tässä tehtävässä laajensit laskimesi MCP-palvelinta lisäämällä uuden työkalun, joka laskee luvun neliöjuuren. Tämä lisäys mahdollistaa AI-agenttisi käsitellä monimutkaisempia matemaattisia kyselyjä, kuten "Mikä on luvun 16 neliöjuuri?" tai "Laske √49" luonnollisella kielellä annettujen kehotteiden avulla.

## 🛠️ Neliöjuurityökalun Toteutus
Lisätäksesi tämän toiminnallisuuden määrittelit uuden työkalufunktion server.py-tiedostossasi. Tässä toteutus:

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

## 🔍 Miten Se Toimii

- **Tuodaan `math`-moduuli**: Peruslaskutoimitusten lisäksi Python tarjoaa sisäänrakennetun `math`-moduulin matemaattisten operaatioiden suorittamiseen. Tämä moduuli sisältää monia matemaattisia funktioita ja vakioita. Tuomalla sen `import math` -komennolla saat käyttöösi esimerkiksi `math.sqrt()`-funktion, joka laskee luvun neliöjuuren.
- **Funktion määrittely**: `@server.tool()`-koristetta käytetään rekisteröimään `sqrt`-funktio työkaluksi, johon AI-agenttisi voi päästä käsiksi.
- **Syöteparametri**: Funktio ottaa vastaan yhden argumentin `a`, joka on tyypiltään `float`.
- **Virheenkäsittely**: Jos `a` on negatiivinen, funktio nostaa `ValueError`-poikkeuksen estääkseen negatiivisen luvun neliöjuuren laskemisen, mikä ei ole tuettua `math.sqrt()`-funktiolla.
- **Paluuarvo**: Ei-negatiivisille syötteille funktio palauttaa luvun `a` neliöjuuren Pythonin sisäänrakennetulla `math.sqrt()`-menetelmällä.

## 🔄 Palvelimen Uudelleenkäynnistys
Uuden `sqrt`-työkalun lisäämisen jälkeen on tärkeää käynnistää MCP-palvelimesi uudelleen, jotta agentti tunnistaa ja voi käyttää uutta toiminnallisuutta.

## 💬 Esimerkkikehotteita Uuden Työkalun Testaamiseen
Tässä muutamia luonnollisen kielen kehotteita, joilla voit testata neliöjuuritoimintoa:

- "Mikä on luvun 25 neliöjuuri?"
- "Laske luvun 81 neliöjuuri."
- "Etsi luvun 0 neliöjuuri."
- "Mikä on luvun 2.25 neliöjuuri?"

Nämä kehotteet saavat agentin kutsumaan `sqrt`-työkalua ja palauttamaan oikeat tulokset.

## ✅ Yhteenveto
Tämän tehtävän suorittamalla olet:

- Laajentanut laskimesi MCP-palvelinta uudella `sqrt`-työkalulla.
- Mahdollistanut AI-agentillesi neliöjuurilaskujen tekemisen luonnollisen kielen kehotteilla.
- Harjoitellut uusien työkalujen lisäämistä ja palvelimen uudelleenkäynnistystä lisätoiminnallisuuksien integroimiseksi.

Kokeile rohkeasti lisäämällä muita matemaattisia työkaluja, kuten potenssi- tai logaritmifunktioita, jatkaaksesi agenttisi kykyjen kehittämistä!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.