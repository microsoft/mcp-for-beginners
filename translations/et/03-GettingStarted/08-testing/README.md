## Testimine ja silumine

Enne kui hakkate oma MCP serverit testima, on oluline mõista saadaolevaid tööriistu ja parimaid tavasid silumiseks. Tõhus testimine tagab, et teie server käitub ootuspäraselt ning aitab kiiresti tuvastada ja lahendada probleeme. Järgmises osas on kirjeldatud soovitatud lähenemisviise teie MCP rakenduse valideerimiseks.

## Ülevaade

See õppetükk käsitleb, kuidas valida õige testimisviis ja kõige tõhusam testimistööriist.

## Õpieesmärgid

Selle õppetüki lõpuks oskate:

- Kirjeldada erinevaid testimisviise.
- Kasutada erinevaid tööriistu oma koodi tõhusaks testimiseks.


## MCP serverite testimine

MCP pakub tööriistu, mis aitavad teil oma servereid testida ja siluda:

- **MCP Inspector**: käsurea tööriist, mida saab kasutada nii CLI tööriistana kui ka visuaalses vormis.
- **Manuaalne testimine**: saate kasutada tööriista nagu curl veebipäringute tegemiseks, kuid sobib ka iga tööriist, mis suudab läbi viia HTTP päringuid.
- **Ühiktestimine**: saate oma eelistatud testimisraamistiku abil testida nii serveri kui kliendi funktsioone.

### MCP Inspectori kasutamine

Oleme seda tööriista varasemates õppetükkides käsitlenud, kuid räägime sellest pisut ülevaatlikult. See on Node.js-is loodud tööriist, mida saate kasutada käivitades `npx` kasutamisel täidetava faili – see laadib tööriista ajutiselt alla ja paigaldab ning pärast päringu täitmist puhastab end ise.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) aitab teil:

- **Avastada serveri võimeid**: automaatselt tuvastada olemasolevad ressursid, tööriistad ja viited
- **Testida tööriistade täitmist**: proovida erinevaid parameetreid ja näha vastuseid reaalajas
- **Vaadata serveri metainfot**: uurida serveri infot, skeeme ja konfiguratsioone

Tavapärane tööriista käivitamine näeb välja selline:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Ülaltoodud käsk käivitab MCP koos selle visuaalse liidesega ning avab brauseris kohalikku veebiliidest. Võite oodata juhtpaneeli, mis kuvab teie registreeritud MCP serverid, nende kasutatavad tööriistad, ressursid ja viited. Liides võimaldab interaktiivselt testida tööriistade käivitamist, uurida serveri metainfot ja vaadata vastuseid reaalajas, muutes MCP serveri rakenduste valideerimise ja silumise hõlpsamaks.

See võib välja näha nii: ![Inspector](../../../../translated_images/et/connect.141db0b2bd05f096.webp)

Seda tööriista saab käivitada ka CLI režiimis, lisades `--cli` parameetri. Näide tööriista käivitamisest "CLI" režiimis, mis kuvab serveri kõik tööriistad:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuaalne testimine

Lisaks inspectori tööriista kasutamisele serveri võimete testimiseks, on sarnane lähenemine klient, mis toetab HTTP kasutamist, näiteks curl.

Curl abil saate otse HTTP päringute kaudu MCP servereid testida:

```bash
# Näide: Testserveri metaandmed
curl http://localhost:3000/v1/metadata

# Näide: Tööriista käivitamine
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Nagu curl'i näitest näha, kasutatakse POST päringut tööriista käivitamiseks koos päringuga, mis sisaldab tööriista nime ja selle parameetreid. Valige endale sobiv lähenemine. CLI tööriistad on üldjuhul kiiremad kasutada ning neid saab skriptida, mis võib olla kasulik CI/CD keskkonnas.

### Ühiktestimine

Looge oma tööriistade ja ressursside jaoks ühikutestid, et tagada nende ootuspärane töötamine. Siin on näide testimise koodist.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Märgi kogu moodul asünkroonseteks testideks
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Loo paar testi tööriista
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testi ilma kursoriparameetrita (jäetud välja)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testi kursori väärtusega None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testi kursoriga stringina
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testi tühja stringi kursori väärtusega
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Ülaltoodud kood teeb järgmist:

- Kasutab pytest raamistikku, mis võimaldab teil teste luua funktsioonidena ja kasutada assert lauseid.
- Loob MCP serveri kahe erineva tööriistaga.
- Kontrollib assert lausega, et teatud tingimused oleksid täidetud.

Vaadake [täispikka faili siin](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Selle faili põhjal saate testida oma serverit, et veenduda võimete loomises nii, nagu peab.

Kõigil suurematel SDK-del on sarnased testimise juhud, nii et saate neid vastavalt oma valitud jooksutuskeskkonnale kohandada.

## Näidised

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)

## Täiendavad ressursid

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Mis järgmisena

- Järgmine: [Paigaldus](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiseletus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->