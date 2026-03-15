## Kupima na Kurekebisha Hitilafu

Kabla ya kuanza kupima seva yako ya MCP, ni muhimu kuelewa zana zilizopo na mbinu bora za kurekebisha hitilafu. Upimaji mzuri huhakikisha seva yako inafanya kazi kama inavyotarajiwa na hukusaidia kutambua na kutatua matatizo kwa haraka. Sehemu ifuatayo inaelezea mbinu zinazopendekezwa za kuthibitisha utekelezaji wako wa MCP.

## Muhtasari

Somo hili linashughulikia jinsi ya kuchagua njia sahihi za kupima na zana bora zaidi za upimaji.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelezea mbinu mbalimbali za kupima.
- Kutumia zana tofauti kwa ufanisi kupima msimbo wako.

## Kupima Seva za MCP

MCP inatoa zana za kusaidia kupima na kurekebisha hitilafu za seva zako:

- **MCP Inspector**: Zana ya mstari wa amri inayoweza kutumika kama CLI na pia kama zana ya kuona.
- **Upimaji wa mwongozo**: Unaweza kutumia zana kama curl kuendesha maombi ya wavuti, lakini zana yoyote inayoweza kuendesha HTTP itafanya kazi.
- **Upimaji wa vitengo**: Inawezekana kutumia mfumo wako wa upimaji unaoupendelea kupima vipengele vya seva na mteja.

### Kutumia MCP Inspector

Tumeelezea matumizi ya zana hii katika masomo ya awali lakini hebu tuzungumze kidogo kwa ujumla. Ni zana iliyojengwa kwa Node.js na unaweza kuitumia kwa kupiga amri ya `npx` ambayo itapakua na kusanidi zana hiyo kwa muda mfupi na kisha kuondoa chakavu baada ya mahitaji yako kuendeshwa.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) hukusaidia:

- **Kubaini Uwezo wa Seva**: Kugundua rasilimali, zana, na maelekezo zinazopatikana moja kwa moja
- **Kupima Uendeshaji wa Zana**: Jaribu vigezo mbalimbali na uone majibu kwa wakati halisi
- **Kutazama Metadata ya Seva**: Chunguza taarifa za seva, skimu, na usanidi

Uendeshaji wa kawaida wa zana unaonekana kama ifuatavyo:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Amri iliyo juu inaanzisha MCP na kiolesura chake cha kuona na kuzindua interface ya wavuti ya ndani kwenye kivinjari chako. Unaweza kutarajia kuona dashibodi inayoonyesha seva zako za MCP zilizoregishwa, zana zao zinazopatikana, rasilimali, na maelekezo. Kiolesura kinaruhusu kupima utekelezaji wa zana kwa kushirikiana, kukagua metadata ya seva, na kuona majibu kwa wakati halisi, na kufanya iwe rahisi kuthibitisha na kurekebisha utekelezaji wako wa seva za MCP.

Hili ndilo linaweza kuonekana jinsi: ![Inspector](../../../../translated_images/sw/connect.141db0b2bd05f096.webp)

Pia unaweza kuendesha zana hii katika hali ya CLI ambapo unaitia `--cli`. Hapa ni mfano wa kuendesha zana katika hali ya "CLI" ambayo inaorodhesha zana zote kwenye seva:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Upimaji wa Mwongozo

Mbali na kuendesha zana ya inspector kupima uwezo wa seva, njia nyingine inayofanana ni kuendesha mteja anayezima kutumia HTTP kama mfano curl.

Kwa curl, unaweza kupima seva za MCP moja kwa moja kwa maombi ya HTTP:

```bash
# Mfano: Metadata ya seva ya majaribio
curl http://localhost:3000/v1/metadata

# Mfano: Tekeleza chombo
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Kama unavyoona kutoka matumizi ya curl hapo juu, unatumia ombi la POST kuitisha zana kwa kutumia payload inayojumuisha jina la zana na vigezo vyake. Tumia njia inayokufaa zaidi. Zana za CLI kwa ujumla huwa na kasi kutumia na zinafaa kwa kuandikwa kwa scripts ambavyo vinaweza kuwa vyema katika mazingira ya CI/CD.

### Upimaji wa Vitengo

Tengeneza vipimo vya vitengo kwa zana na rasilimali zako kuhakikisha zinafanya kazi kama inavyotarajiwa. Hapa kuna mfano wa msimbo wa upimaji.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Chagua moduli yote kwa majaribio ya async
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Tengeneza zana chache za majaribio
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Jaribu bila kipengele cha cursor (kimeachwa)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Jaribu kwa cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Jaribu na cursor kama kamba
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Jaribu na cursor isiyo na maandishi
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Msimbo uliotangulia unafanya yafuatayo:

- Unatumia mfumo wa pytest ambao hukuruhusu kuunda vipimo kama kazi na kutumia kauli za assert.
- Unaunda seva ya MCP yenye zana mbili tofauti.
- Unatumia kauli ya `assert` kuchunguza kuwa masharti fulani yametimizwa.

Angalia [faili kamili hapa](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Kwa kuzingatia faili hapo juu, unaweza kupima seva yako kuhakikisha uwezo umeundwa kama inavyostahili.

SDK zote kuu zina sehemu za upimaji zinazofanana hivyo unaweza kuendana na runtime uliyochagua.

## Sampuli

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Rasilimali Za Ziada

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Kifuatacho

- Ifuatayo: [Utekelezaji](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Angalizo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili kwa lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya mtaalamu wa binadamu inashauriwa. Hatubeba dhamana kwa kutoelewana au tafsiri potofu zitakazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->