## Testimine ja silumine

Enne kui hakkate oma MCP-serverit testima, on oluline mõista olemasolevaid tööriistu ja parimaid tavasid silumiseks. Tõhus testimine tagab, et teie server käitub ootuspäraselt ja aitab teil kiiresti leida ning lahendada probleeme. Järgmine jaotis toob välja soovitatavad lähenemised oma MCP-implementatsiooni valideerimiseks.

## Ülevaade

See õppetund käsitleb, kuidas valida sobiv testimisviis ja kõige tõhusam testimisriist.

## Õpieesmärgid

Pärast selle õppetunni lõppu suudate:

- Kirjeldada erinevaid testimisvõtteid.
- Kasutada erinevaid tööriistu koodi tõhusaks testimiseks.


## MCP-serverite testimine

MCP pakub tööriistu teie serverite testimiseks ja silumiseks:

- **MCP Inspector**: käsurea tööriist, mida saab käivitada nii CLI-režiimis kui ka visuaalse tööriistana.
- **Manuaalne testimine**: saate kasutada tööriista nagu curl veebi-päringute käivitamiseks, kuid sobib iga HTTP-i käivitada võimeline tööriist.
- **Ühikutestimine**: saate kasutada eelistatud testiraamistikku nii serveri kui kliendi funktsioonide testimiseks.

### MCP Inspectori kasutamine

Oleme selle tööriista kasutamist varem kirjeldanud, aga räägime sellest lühidalt kõrgtasandil. See on Node.js-is kirjutatud tööriist ja saate seda kasutada, kutsudes käsku `npx`, mis laadib tööriista ajutiselt alla ja installib selle ning puhastab end pärast päringu käivitamist.

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) aitab teid:

- **Serveri võimaluste avastamine**: automaatselt tuvastab saadaolevad ressursid, tööriistad ja promptid
- **Tööriistade käivitamise testimine**: katsetage erinevaid parameetreid ja vaadake vastuseid reaalajas
- **Serveri metaandmete vaatamine**: uurige serveri teavet, skeeme ja konfiguratsioone

Tavapärane tööriista käivitamine näeb välja nii:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Ülaltoodud käsk käivitab MCP-i ja selle visuaalse liidese ning avab teie brauseris kohaliku veebiliidese. Oodata on armatuurlaual registreeritud MCP-servereid, nende saadaolevaid tööriistu, ressursse ja prompte. Liides võimaldab teil interaktiivselt testida tööriistade käivitamist, uurida serveri metaandmeid ja vaadata reaalajas vastuseid, muutes MCP-serveri rakenduste valideerimise ja silumise lihtsamaks.

Nii see võib välja näha: ![Inspektor](../../../../translated_images/et/connect.141db0b2bd05f096.webp)

Seda tööriista saab käivitada ka CLI-režiimis, lisades `--cli` atribuudi. Siin on näide tööriista käivitamisest "CLI" režiimis, mis loetleb kõik serveri tööriistad:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuaalne testimine

Lisaks inspectori tööriista käitamisele serveri võimete testimiseks on teine sarnane lähenemine käivitada klient, mis oskab kasutada HTTP-i, näiteks curl.

Curliga saate MCP-servereid testida otse HTTP-päringutega:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Nagu ülal curl'i kasutamisest näete, kasutatakse tööriista kutsumiseks POST-päringut koos koormisega, mis sisaldab tööriista nime ja selle parameetreid. Kasutage lähenemist, mis teile kõige paremini sobib. CLI-tööriistad on üldiselt kiiremad kasutada ja neid saab skriptida, mis võib olla kasulik CI/CD keskkonnas.

### Ühikutestimine

Looge oma tööriistade ja ressursside jaoks ühikutestid, et tagada nende oodatud toimimine. Siin on näide testkoodist.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Eelnev kood teeb järgmist:

- Kasutab pytest-raamistikku, mis võimaldab teil luua teste funktsioonidena ja kasutada assert-lauseid.
- Loob MCP-serveri kahe erineva tööriistaga.
- Kasutab `assert` lauset, et kontrollida, et teatud tingimused on täidetud.

Vaadake [kogu faili siit](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Eelneva faili põhjal saate testida oma serverit, et veenduda, et võimed on loodud nõutud viisil.

Kõigil suurematel SDK-del on sarnased testimise sektsioonid, nii et saate need kohandada valitud jooksuaega.

## Näited 

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.NET kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python) 

## Täiendavad ressursid

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Mis järgmiseks

- Järgmine: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->