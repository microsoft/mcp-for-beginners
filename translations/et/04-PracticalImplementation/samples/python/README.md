# Mudeli Konteksti Protokolli (MCP) Pythoni Implementatsioon

See repositoorium sisaldab Mudeli Konteksti Protokolli (MCP) Pythoni implementatsiooni, mis näitab, kuidas luua nii serveri kui ka kliendirakendust, mis suhtlevad MCP standardi abil.

## Ülevaade

MCP implementatsioon koosneb kahest peamisest komponendist:

1. **MCP Server (`server.py`)** - Server, mis pakub:
   - **Tööriistu**: Funktsioonid, mida saab kaugelt kutsuda
   - **Ressursse**: Andmed, mida saab hankida
   - **Küsimusi**: Mallid keelemudelitele küsimuste genereerimiseks

2. **MCP Klient (`client.py`)** - Kliendirakendus, mis ühendub serveriga ja kasutab selle funktsioone

## Funktsioonid

See implementatsioon demonstreerib mitmeid olulisi MCP funktsioone:

### Tööriistad
- `completion` - Genereerib tekstilisi lõpetusi AI mudelitelt (simuleeritud)
- `add` - Lihtne kalkulaator, mis liidab kaks arvu

### Ressursid
- `models://` - Tagastab teavet saadaolevate AI mudelite kohta
- `greeting://{name}` - Tagastab isikupärastatud tervituse antud nimele

### Küsimused
- `review_code` - Genereerib küsimuse koodi ülevaatamiseks

## Paigaldamine

MCP implementatsiooni kasutamiseks paigalda vajalikud paketid:

```powershell
pip install mcp-server mcp-client
```

## Serveri ja Kliendi Käivitamine

### Serveri Käivitamine

Käivita server ühes terminaliaknas:

```powershell
python server.py
```

Serverit saab käivitada ka arendusrežiimis MCP CLI abil:

```powershell
mcp dev server.py
```

Või paigaldada Claude Desktopi (kui saadaval):

```powershell
mcp install server.py
```

### Kliendi Käivitamine

Käivita klient teises terminaliaknas:

```powershell
python client.py
```

See ühendub serveriga ja demonstreerib kõiki saadaolevaid funktsioone.

### Kliendi Kasutamine

Klient (`client.py`) demonstreerib kõiki MCP võimekusi:

```powershell
python client.py
```

See ühendub serveriga ja kasutab kõiki funktsioone, sealhulgas tööriistu, ressursse ja küsimusi. Väljund näitab:

1. Kalkulaatori tööriista tulemust (5 + 7 = 12)
2. Lõpetustööriista vastust küsimusele "Mis on elu mõte?"
3. Saadaolevate AI mudelite loetelu
4. Isikupärastatud tervitust "MCP Explorerile"
5. Koodi ülevaatamise küsimuse malli

## Implementatsiooni Üksikasjad

Server on implementeeritud kasutades `FastMCP` API-d, mis pakub kõrgetasemelisi abstraktsioone MCP teenuste määratlemiseks. Siin on lihtsustatud näide, kuidas tööriistu määratleda:

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

Klient kasutab MCP kliendiraamatukogu serveriga ühenduse loomiseks ja selle kutsumiseks:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Lisateave

Lisateabe saamiseks MCP kohta külastage: https://modelcontextprotocol.io/

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.