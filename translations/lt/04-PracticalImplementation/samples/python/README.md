# Modelio Konteksto Protokolo (MCP) Python Įgyvendinimas

Šiame saugykloje pateikiamas Modelio Konteksto Protokolo (MCP) Python įgyvendinimas, parodantis, kaip sukurti tiek serverio, tiek kliento programą, kurios bendrauja naudodamos MCP standartą.

## Apžvalga

MCP įgyvendinimas susideda iš dviejų pagrindinių komponentų:

1. **MCP Serveris (`server.py`)** - Serveris, kuris teikia:
   - **Įrankius**: Funkcijas, kurias galima iškviesti nuotoliniu būdu
   - **Išteklius**: Duomenis, kuriuos galima gauti
   - **Šablonus**: Šablonus, skirtus kalbos modelių užklausoms generuoti

2. **MCP Klientas (`client.py`)** - Kliento programa, kuri jungiasi prie serverio ir naudoja jo funkcijas

## Funkcijos

Šis įgyvendinimas demonstruoja keletą pagrindinių MCP funkcijų:

### Įrankiai
- `completion` - Generuoja teksto užbaigimus iš AI modelių (simuliuota)
- `add` - Paprastas skaičiuotuvas, kuris sudeda du skaičius

### Ištekliai
- `models://` - Grąžina informaciją apie galimus AI modelius
- `greeting://{name}` - Grąžina asmeninį pasveikinimą pagal pateiktą vardą

### Šablonai
- `review_code` - Generuoja šabloną kodo peržiūrai

## Diegimas

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

Serveris taip pat gali būti paleistas kūrimo režimu naudojant MCP CLI:

```powershell
mcp dev server.py
```

Arba įdiegtas Claude Desktop (jei prieinama):

```powershell
mcp install server.py
```

### Kliento Paleidimas

Paleiskite klientą kitame terminalo lange:

```powershell
python client.py
```

Tai prisijungs prie serverio ir pademonstruos visas galimas funkcijas.

### Kliento Naudojimas

Klientas (`client.py`) demonstruoja visas MCP galimybes:

```powershell
python client.py
```

Tai prisijungs prie serverio ir išbandys visas funkcijas, įskaitant įrankius, išteklius ir šablonus. Rezultatai parodys:

1. Skaičiuotuvo įrankio rezultatą (5 + 7 = 12)
2. Užbaigimo įrankio atsakymą į „Kokia gyvenimo prasmė?“
3. Galimų AI modelių sąrašą
4. Asmeninį pasveikinimą „MCP Explorer“
5. Kodo peržiūros šablono pavyzdį

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

Klientas naudoja MCP kliento biblioteką, kad prisijungtų prie serverio ir iškviestų jo funkcijas:

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