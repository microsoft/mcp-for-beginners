## Testavimas ir derinimas

Prieš pradėdami testuoti savo MCP serverį, svarbu suprasti prieinamus įrankius ir geriausias derinimo praktikas. Efektyvus testavimas užtikrina, kad jūsų serveris elgtųsi kaip tikėtasi, ir padeda greitai identifikuoti bei išspręsti problemas. Toliau pateikiama skyriuje apžvelgiami rekomenduojami metodai, kaip patikrinti savo MCP įgyvendinimą.

## Apžvalga

Šioje pamokoje aptarsime, kaip pasirinkti tinkamą testavimo metodą ir efektyviausią testavimo įrankį.

## Mokymosi tikslai

Šios pamokos pabaigoje galėsite:

- Apibūdinti įvairius testavimo metodus.
- Naudoti skirtingus įrankius savo kodo efektyviam testavimui.

## MCP serverių testavimas

MCP suteikia įrankius, kurie padeda jums testuoti ir derinti serverius:

- **MCP Inspector**: Komandinės eilutės įrankis, kurį galima naudoti tiek kaip CLI, tiek kaip vizualinį įrankį.
- **Rankinis testavimas**: Galite naudoti įrankį, pvz., curl, norėdami vykdyti tinklo užklausas, tačiau tinkami bet kokie įrankiai, galintys vykdyti HTTP užklausas.
- **Vienetinis testavimas**: Galima naudoti savo norimą testavimo sistemą, kad išbandytumėte tiek serverio, tiek kliento funkcionalumus.

### Naudojant MCP Inspector

Šio įrankio naudojimą aprašėme ankstesnėse pamokose, bet apžvelkime jį aukštesnio lygio požiūriu. Tai Node.js pagrindu sukurtas įrankis, kurį galite naudoti iškviesdami `npx` vykdomąjį failą, kuris laikinai parsisiųs ir įdiegs įrankį ir išvalys save baigus vykdyti jūsų užklausą.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) padeda jums:

- **Aptikti serverio galimybes**: Automatiškai nustatyti prieinamus išteklius, įrankius ir užklausas
- **Testuoti įrankių vykdymą**: Išbandyti įvairius parametrus ir matyti atsakymus realiuoju laiku
- **Peržiūrėti serverio metaduomenis**: Tirti serverio informaciją, schemas ir konfigūracijas

Tipinis įrankio paleidimas atrodo taip:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Aukščiau pateikta komanda paleidžia MCP ir jo vizualinę sąsają bei atidaro vietinę žiniatinklio sąsają jūsų naršyklėje. Galite tikėtis pamatyti informacinę skydelį, rodantį jūsų registruotus MCP serverius, jų prieinamus įrankius, išteklius ir užklausas. Sąsaja leidžia interaktyviai testuoti įrankių vykdymą, tikrinti serverio metaduomenis ir matyti atsakymus realiuoju laiku, kas palengvina MCP serverio įgyvendinimų validavimą ir derinimą.

Taip tai gali atrodyti: ![Inspector](../../../../translated_images/lt/connect.141db0b2bd05f096.webp)

Taip pat galite paleisti šį įrankį CLI režimu pridėdami atributą `--cli`. Štai pavyzdys, kaip paleisti įrankį "CLI" režimu, kuris išveda visus įrankius serveryje:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```


### Rankinis testavimas

Be MCP Inspector įrankio naudojimo serverio galimybėms tikrinti, galima naudoti panašų metodą – paleisti klientą, galintį naudoti HTTP, pavyzdžiui, curl.

Su curl galite tiesiogiai testuoti MCP serverius vykdydami HTTP užklausas:

```bash
# Pavyzdys: Testavimo serverio metaduomenys
curl http://localhost:3000/v1/metadata

# Pavyzdys: Įvykdyti įrankį
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Kaip matote iš aukščiau pateikto curl panaudojimo, POST užklausa skirta įrankio iškvietimui su siuntinio duomenimis, kur nurodytas įrankio pavadinimas ir jo parametrai. Pasirinkite jums labiausiai tinkantį metodą. CLI įrankiai paprastai greičiau naudojami ir gali būti automatizuojami, kas naudinga CI/CD aplinkose.

### Vienetiniai testai

Sukurkite savo įrankių ir išteklių vienetinius testus, kad įsitikintumėte jų veikimu kaip numatyta. Štai pavyzdinis testavimo kodas.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Pažymėkite visą modulį asinchroniniams testams
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Sukurkite keletą testavimo įrankių
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testuoti be žymeklio parametro (praleista)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testuoti su cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testuoti su cursor kaip eilute
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testuoti su tuščiu eilutės žymekliu
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Aukščiau pateiktas kodas daro šiuos veiksmus:

- Naudoja pytest sistemą, leidžiančią kurti testus kaip funkcijas ir naudoti assert sakinius.
- Sukuria MCP serverį su dviem skirtingais įrankiais.
- Naudoja `assert` sakinį, kad patikrintų tam tikrų sąlygų įvykdymą.

Peržiūrėkite [visą failą čia](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Turėdami aukščiau pateiktą failą, galite testuoti savo serverį ir įsitikinti, kad galimybės sukurtos kaip turėtų.

Visos svarbiausios SDK turi panašius testavimo skyrius, tad galite prisitaikyti prie savo pasirinktos vykdymo aplinkos.

## Pavyzdžiai

- [Java skaičiuotuvas](../samples/java/calculator/README.md)
- [.Net skaičiuotuvas](../../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuotuvas](../samples/javascript/README.md)
- [TypeScript skaičiuotuvas](../samples/typescript/README.md)
- [Python skaičiuotuvas](../../../../03-GettingStarted/samples/python)

## Papildomi ištekliai

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Kas toliau

- Toliau: [Diegimas](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogiškas vertimas. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar klaidingus aiškinimus, kylantčius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->