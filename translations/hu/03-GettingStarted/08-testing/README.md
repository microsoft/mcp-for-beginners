## Tesztelés és hibakeresés

Mielőtt elkezdené tesztelni az MCP szerverét, fontos megérteni az elérhető eszközöket és a hibakeresés legjobb gyakorlatait. A hatékony tesztelés biztosítja, hogy a szervere a vártnak megfelelően működjön, és segít gyorsan azonosítani és megoldani a problémákat. A következő szakasz az MCP implementációjának érvényesítésére ajánlott megközelítéseket ismerteti.

## Áttekintés

Ez a lecke bemutatja, hogyan válasszuk ki a megfelelő tesztelési megközelítést és a leghatékonyabb tesztelő eszközt.

## Tanulási célok

A lecke végére képes lesz:

- Leírni a különböző tesztelési megközelítéseket.
- Különböző eszközöket használni a kód hatékony teszteléséhez.

## MCP szerverek tesztelése

Az MCP eszközöket biztosít a szerverek teszteléséhez és hibakereséséhez:

- **MCP Inspector**: Egy parancssoros eszköz, amely CLI eszközként és vizuális eszközként is használható.
- **Kézi tesztelés**: Használhat egy curl-hez hasonló eszközt webkérelmek futtatásához, de bármely, HTTP-t futtatni képes eszköz megteszi.
- **Egységtesztelés**: Lehetséges kedvenc tesztelési keretrendszerével tesztelni a szerver és a kliens funkcióit is.

### MCP Inspector használata

Ennek az eszköznek a használatát korábbi leckékben már leírtuk, de beszéljünk róla egy kicsit magasabb szinten. Ez egy Node.js-ben készült eszköz, amelyet az `npx` végrehajtható fájl hívásával használhat, amely ideiglenesen letölti és telepíti az eszközt, majd a futtatás után törli önmagát.

Az [MCP Inspector](https://github.com/modelcontextprotocol/inspector) segít Önnek:

- **Szerver képességek felfedezése**: Automatikusan észleli az elérhető erőforrásokat, eszközöket és promptokat
- **Eszköz végrehajtásának tesztelése**: Próbáljon ki különböző paramétereket, és valós időben lássa a válaszokat
- **Szerver metaadatai megtekintése**: Vizsgálja meg a szerver információkat, sémákat és konfigurációkat

Az eszköz tipikus futtatása így néz ki:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

A fenti parancs elindít egy MCP-t és annak vizuális felületét, valamint megnyit egy helyi webes felületet a böngészőjében. Egy irányítópultot láthat majd, amely megjeleníti a regisztrált MCP szervereit, azok elérhető eszközeit, erőforrásait és promptjait. A felület lehetővé teszi az eszköz végrehajtásának interaktív tesztelését, a szerver metaadatainak ellenőrzését és a valós idejű válaszok megtekintését, megkönnyítve ezzel az MCP szerver implementációinak érvényesítését és hibakeresését.

Így nézhet ki: ![Inspector](../../../../translated_images/hu/connect.141db0b2bd05f096.webp)

Az eszközt CLI módban is futtathatja, ilyenkor hozzá kell adnia a `--cli` paramétert. Íme egy példa az eszköz „CLI” módban történő futtatására, amely listázza a szerveren lévő összes eszközt:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Kézi tesztelés

Az inspector eszköz futtatásán kívül egy másik hasonló megközelítés egy HTTP-képes kliens futtatása, például curl.

A curl segítségével közvetlenül HTTP kérésekkel tesztelheti az MCP szervereket:

```bash
# Példa: Teszt szerver metaadata
curl http://localhost:3000/v1/metadata

# Példa: Eszköz végrehajtása
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Ahogy a fenti curl használatából látható, egy POST kérést használ az eszköz meghívására úgy, hogy a terhelés az eszköz nevét és paramétereit tartalmazza. Használja azt a megközelítést, amely a legjobban megfelel Önnek. Általában a CLI eszközök gyorsabbak és könnyebben szkriptezhetők, ami hasznos lehet CI/CD környezetben.

### Egységtesztelés

Készítsen egységteszteket az eszközeihez és erőforrásaihoz, hogy biztosítsa, hogy azok a vártnak megfelelően működnek. Íme egy példa tesztkód.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Jelöld meg az egész modult aszinkron tesztekhez
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Hozz létre néhány teszteszközt
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Teszt kurzor paraméter nélkül (kihagyva)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Teszt kurzor None értékkel
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Teszt kurzor stringként
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Teszt üres string kurzorral
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

A fenti kód a következőket teszi:

- Használja a pytest keretrendszert, amely lehetővé teszi, hogy teszteket függvényekként hozzon létre, és assert állításokat használjon.
- Létrehoz egy MCP szervert két különböző eszközzel.
- `assert` állítást használ bizonyos feltételek ellenőrzésére.

Tekintse meg a [teljes fájlt itt](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

A fenti fájl alapján tesztelheti saját szerverét, hogy megbizonyosodjon arról, hogy a képességek a kívánt módon jönnek létre.

Minden fő SDK hasonló tesztelési szakaszokkal rendelkezik, így alkalmazkodhat a kiválasztott futtatókörnyezethez.

## Minta projektek

- [Java Számológép](../samples/java/calculator/README.md)
- [.Net Számológép](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Számológép](../samples/javascript/README.md)
- [TypeScript Számológép](../samples/typescript/README.md)
- [Python Számológép](../../../../03-GettingStarted/samples/python)

## További források

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Mi következik?

- Következő: [Telepítés](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordító szolgáltatás segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy a gépi fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén ajánlott professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->