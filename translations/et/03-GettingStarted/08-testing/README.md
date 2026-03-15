## Testimine ja silumine

Enne kui alustad oma MCP serveri testimist, on oluline mõista saadaolevaid tööriistu ja parimaid praktikaid silumiseks. Tõhus testimine tagab, et sinu server käitub ootuspäraselt ning aitab kiiresti tuvastada ja lahendada probleeme. Järgmine lõik tutvustab soovitatud lähenemisi MCP rakenduse valideerimiseks.

## Ülevaade

See õppetund käsitleb, kuidas valida sobiv testimismeetod ja kõige tõhusam testimisvahend.

## Õpieesmärgid

Selle õppetunni lõpuks oskad:

- Kirjeldada erinevaid testimislähenemisi.
- Kasutada erinevaid tööriistu oma koodi tõhusaks testimiseks.

## MCP serverite testimine

MCP pakub vahendeid, mis aitavad sul oma servereid testida ja siluda:

- **MCP Inspector**: käsurea tööriist, mida saab käivitada nii CLI tööriistana kui ka visuaalse vahendina.
- **Manuaalne testimine**: võid kasutada tööriista nagu curl veebipäringute tegemiseks, kuid sobib mistahes HTTP päringuid võimaldav vahend.
- **Ühiktestimine**: on võimalik oma eelistatud testiraamistiku abil testida nii serveri kui kliendi funktsioone.

### MCP Inspectori kasutamine

Oleme selle tööriista kasutust käsitlenud varasemates õppetundides, kuid räägime sellest nüüd veidi üldisemalt. See on Node.js-i põhine tööriist, mida saad kasutada, käivitades `npx` käivitatava faili, mis laadib tööriista ajutiselt alla ja installeerib ning kustutab selle pärast päringu täitmist automaatselt.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) aitab sul:

- **Avastada serveri võimalused**: automaatselt tuvastada saadaolevad ressursid, tööriistad ja vihjed
- **Testida tööriistade täitmist**: proovida erinevaid parameetreid ja vaadata vastuseid reaalajas
- **Vaadata serveri metainfot**: uurida serveri infot, skeeme ja konfiguratsioone

Tüüpiline tööriista käivitamine näeb välja selline:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Ülaltoodud käsk käivitab MCP ja selle visuaalse liidese ning avab sinu brauseris kohalik veebiliidese. Võid oodata armatuurlaua nägemist, mis kuvab registreeritud MCP servereid, nende saadaolevaid tööriistu, ressursse ja vihjeid. Liides võimaldab interaktiivselt testida tööriistade täitmist, uurida serveri metainfot ja jälgida vastuseid reaalajas, muutes MCP serveri rakenduste valideerimise ja silumise lihtsamaks.

See võib välja näha selline: ![Inspector](../../../../translated_images/et/connect.141db0b2bd05f096.webp)

Seda tööriista saab käivitada ka CLI režiimis, lisades `--cli` atribuudi. Näiteks tööriista käivitamine "CLI" režiimis, mis kuvab kõik serveri tööriistad:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuaalne testimine

Peale inspectori tööriista käivitamist serveri võimaluste testimiseks on teine sarnane lähenemine kliendi kasutamine, mis toetab HTTP päringuid, näiteks curl.

Curl abil saad MCP servereid otse HTTP päringutega testida:

```bash
# Näide: Testserveri metaandmed
curl http://localhost:3000/v1/metadata

# Näide: Tööriista käivitamine
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Nagu näha ülaltoodud curl näites, kasutatakse tööriista käivitamiseks POST päringut koos koormusega, mis sisaldab tööriista nime ja selle parameetreid. Kasuta sulle sobivat lähenemist. CLI tööriistad on üldiselt kiiremalt kasutatavad ja sobivad skriptimiseks, mis võib olla kasulik CI/CD keskkonnas.

### Ühiktestimine

Loo oma tööriistade ja ressursside jaoks üksustestid, et veenduda, et need töötavad ootuspäraselt. Siin on mõned näidis testikoodid.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Märgi kogu moodul asünkroonsete testide jaoks
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Loo paar testimisvahendit
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testi ilma kursori parameetrita (jäetud välja)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testi kursori väärtusega None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testi kursori väärtusega string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testi tühja stringi kursori väärtusega
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Ülaltoodud kood teeb järgmist:

- Kasutab pytest raamistiku, mis võimaldab luua teste funktsioonidena ja kasutada assert lauseid.
- Loo MCP server kahe erineva tööriistaga.
- Kasutab `assert` lauseid, et kontrollida teatud tingimuste täitumist.

Vaata täispikka faili [siit](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Antud faili põhjal saad testida oma serverit, et veenduda, et võimalused on loodud ootuspäraselt.

Kõigil suurematel SDK-del on sarnased testimislõigud, nii et saad oma valitud runtime'i jaoks kohandada.

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)

## Lisavahendid

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Järgmine teema

- Järgmine: [Deployimine](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud tehisintellektil põhineva tõlkevahendi [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame tõlke täpsust tagada, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->