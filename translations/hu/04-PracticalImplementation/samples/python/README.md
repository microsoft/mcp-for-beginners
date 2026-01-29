# Model Context Protocol (MCP) Python megvalósítás

Ez a tároló tartalmaz egy Python megvalósítást a Model Context Protocol (MCP) számára, bemutatva, hogyan lehet létrehozni egy szerver és kliens alkalmazást, amelyek az MCP szabvány szerint kommunikálnak.

## Áttekintés

Az MCP megvalósítás két fő részből áll:

1. **MCP szerver (`server.py`)** – Egy szerver, amely elérhetővé teszi:
   - **Eszközök**: Távolról hívható függvények
   - **Erőforrások**: Lekérdezhető adatok
   - **Promptok**: Nyelvi modellek számára generált prompt sablonok

2. **MCP kliens (`client.py`)** – Egy kliens alkalmazás, amely kapcsolódik a szerverhez és használja annak funkcióit

## Jellemzők

Ez a megvalósítás több fontos MCP funkciót mutat be:

### Eszközök
- `completion` – Szövegkiegészítéseket generál AI modellektől (szimulált)
- `add` – Egyszerű kalkulátor, amely két számot ad össze

### Erőforrások
- `models://` – Információkat ad vissza az elérhető AI modellekről
- `greeting://{name}` – Személyre szabott üdvözletet ad megadott névhez

### Promptok
- `review_code` – Kód átnézéséhez generál promptot

## Telepítés

Az MCP megvalósítás használatához telepítsd a szükséges csomagokat:

```powershell
pip install mcp-server mcp-client
```

## Szerver és kliens indítása

### Szerver indítása

Indítsd el a szervert egy terminál ablakban:

```powershell
python server.py
```

A szerver fejlesztői módban is futtatható az MCP CLI segítségével:

```powershell
mcp dev server.py
```

Vagy telepíthető Claude Desktopba (ha elérhető):

```powershell
mcp install server.py
```

### Kliens futtatása

Indítsd el a klienst egy másik terminál ablakban:

```powershell
python client.py
```

Ez csatlakozik a szerverhez és bemutatja az összes elérhető funkciót.

### Kliens használata

A kliens (`client.py`) bemutatja az MCP összes képességét:

```powershell
python client.py
```

Ez csatlakozik a szerverhez és használja az összes funkciót, beleértve az eszközöket, erőforrásokat és promptokat. A kimenet a következőket mutatja:

1. Kalkulátor eszköz eredménye (5 + 7 = 12)
2. Completion eszköz válasza a "What is the meaning of life?" kérdésre
3. Elérhető AI modellek listája
4. Személyre szabott üdvözlet "MCP Explorer" számára
5. Kód átnéző prompt sablon

## Megvalósítás részletei

A szerver a `FastMCP` API-val készült, amely magas szintű absztrakciókat biztosít MCP szolgáltatások definiálásához. Íme egy egyszerűsített példa az eszközök definiálására:

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

A kliens az MCP kliens könyvtárat használja a szerverhez való kapcsolódáshoz és hívásokhoz:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## További információk

További részletekért az MCP-ről látogass el ide: https://modelcontextprotocol.io/

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.