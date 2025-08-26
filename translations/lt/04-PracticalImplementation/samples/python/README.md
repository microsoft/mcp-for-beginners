<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "706b9b075dc484b73a053e6e9c709b4b",
  "translation_date": "2025-08-26T16:19:09+00:00",
  "source_file": "04-PracticalImplementation/samples/python/README.md",
  "language_code": "lt"
}
-->
# Modelio Konteksto Protokolo (MCP) Python Įgyvendinimas

Šiame saugykloje pateikiamas Python įgyvendinimas Modelio Konteksto Protokolo (MCP), kuris demonstruoja, kaip sukurti tiek serverio, tiek kliento programą, bendraujančią pagal MCP standartą.

## Apžvalga

MCP įgyvendinimas susideda iš dviejų pagrindinių komponentų:

1. **MCP serveris (`server.py`)** - Serveris, kuris teikia:
   - **Įrankius**: Funkcijas, kurias galima kviesti nuotoliniu būdu
   - **Išteklius**: Duomenis, kuriuos galima gauti
   - **Šablonus**: Šablonus, skirtus generuoti kalbos modelių užklausas

2. **MCP klientas (`client.py`)** - Kliento programa, kuri prisijungia prie serverio ir naudoja jo funkcijas

## Funkcijos

Šis įgyvendinimas demonstruoja kelias pagrindines MCP funkcijas:

### Įrankiai
- `completion` - Generuoja tekstinius užbaigimus iš AI modelių (simuliuota)
- `add` - Paprastas skaičiuotuvas, kuris sudeda du skaičius

### Išteklius
- `models://` - Grąžina informaciją apie galimus AI modelius
- `greeting://{name}` - Grąžina asmeninį pasisveikinimą nurodytam vardui

### Šablonai
- `review_code` - Generuoja šabloną kodo peržiūrai

## Įdiegimas

Norėdami naudoti šį MCP įgyvendinimą, įdiekite reikalingus paketus:

```powershell
pip install mcp-server mcp-client
```

## Serverio ir Kliento Paleidimas

### Serverio Paleidimas

Paleiskite serverį viename terminalo lange:

```powershell
python server.py
```

Serverį taip pat galima paleisti kūrimo režimu naudojant MCP CLI:

```powershell
mcp dev server.py
```

Arba įdiegti Claude Desktop (jei prieinama):

```powershell
mcp install server.py
```

### Kliento Paleidimas

Paleiskite klientą kitame terminalo lange:

```powershell
python client.py
```

Tai prisijungs prie serverio ir demonstruos visas galimas funkcijas.

### Kliento Naudojimas

Klientas (`client.py`) demonstruoja visas MCP galimybes:

```powershell
python client.py
```

Tai prisijungs prie serverio ir išbandys visas funkcijas, įskaitant įrankius, išteklius ir šablonus. Rezultatai parodys:

1. Skaičiuotuvo įrankio rezultatą (5 + 7 = 12)
2. Užbaigimo įrankio atsakymą į „Kokia gyvenimo prasmė?“
3. Galimų AI modelių sąrašą
4. Asmeninį pasisveikinimą „MCP Explorer“
5. Kodo peržiūros šablono šabloną

## Įgyvendinimo Detalės

Serveris įgyvendintas naudojant `FastMCP` API, kuris suteikia aukšto lygio abstrakcijas MCP paslaugoms apibrėžti. Štai supaprastintas pavyzdys, kaip apibrėžiami įrankiai:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Klientas naudoja MCP kliento biblioteką, kad prisijungtų prie serverio ir kviestų jo funkcijas:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Sužinokite Daugiau

Daugiau informacijos apie MCP rasite: https://modelcontextprotocol.io/

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.