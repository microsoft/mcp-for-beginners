## Kupima na Kurekebisha Hitilafu

Kabla ya kuanza kupima seva yako ya MCP, ni muhimu kuelewa zana zilizopo na mbinu bora za kurekebisha hitilafu. Kupima kwa ufanisi kunahakikisha seva yako inafanya kazi kama inavyotarajiwa na kunakusaidia utambue na kutatua matatizo haraka. Sehemu ifuatayo inaelezea mbinu zilizopendekezwa za kuthibitisha utekelezaji wako wa MCP.

## Muhtasari

Somo hili linajumuisha jinsi ya kuchagua mbinu sahihi ya kupima na zana bora zaidi za kupima.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelezea mbinu mbalimbali za kupima.
- Kutumia zana tofauti kupima msimbo wako kwa ufanisi.


## Kupima Seva za MCP

MCP huleta zana za kusaidia kupima na kurekebisha hitilafu za seva zako:

- **MCP Inspector**: Zana ya mstari wa amri inayoweza kutumika kama zana ya CLI na pia kama zana ya kuona.
- **Kupima kwa mkono**: Unaweza kutumia zana kama curl kutekeleza ombi za wavuti, lakini zana yoyote inayoweza kutekeleza HTTP itafanya.
- **Kupima kwa vipande**: Inawezekana kutumia mfumo wako wa kupima unaopendelea kupima vipengele vya seva na mteja.

### Kutumia MCP Inspector

Tumesema matumizi ya zana hii katika masomo ya awali lakini tuzungumzie kwa kiwango cha juu. Ni zana iliyojengwa kwa Node.js na unaweza kuitumia kwa kuitisha executable ya `npx` ambayo itapakua na kusanidi zana hiyo kwa muda mfupi na kuiondoa yenyewe mara baada ya kuendeshwa kwa ombi lako.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) hukusaidia:

- **Gundua Uwezo wa Seva**: Kugundua moja kwa moja rasilimali, zana, na maelezo yaliyopo
- **Jaribu Uendeshaji wa Zana**: Jaribu vigezo tofauti na uone majibu kwa wakati halisi
- **Tazama Metadata ya Seva**: Chunguza taarifa za seva, skimu, na usanidi

Uzito wa kawaida wa zana unaonekana kama ifuatavyo:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Amri hapo juu inaanzisha MCP na kiolesura chake cha kuona na kuanzisha interface ya wavuti ya ndani kwenye kivinjari chako. Unaweza kutarajia kuona dashibodi inayoonyesha seva zako za MCP zilizosajiliwa, zana zao zinazopatikana, rasilimali, na maelezo. Kiolesura huru kuruhusu kupima kwa mwingiliano wa uendeshaji wa zana, kuchunguza metadata ya seva, na kuona majibu kwa wakati halisi, na kufanya iwe rahisi kuthibitisha na kurekebisha utekelezaji wa seva zako za MCP.

Hivi ndivyo zinaweza kuonekana: ![Inspector](../../../../translated_images/sw/connect.141db0b2bd05f096.webp)

Unaweza pia kuendesha zana hii katika hali ya CLI ambapo unazidisha alama `--cli`. Hapa ni mfano wa kuendesha zana katika hali ya "CLI" inayoorodhesha zana zote kwenye seva:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Kupima kwa Mkono

Mbali na kuendesha zana ya inspector kupima uwezo wa seva, njia nyingine inayofanana ni kuendesha mteja anayeweza kutumia HTTP kama curl kwa mfano.

Kwa curl, unaweza kupima seva za MCP moja kwa moja kwa kutumia maombi ya HTTP:

```bash
# Mfano: Metadata ya seva ya mtihani
curl http://localhost:3000/v1/metadata

# Mfano: Endesha chombo
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Kama unavyoweza kuona kutoka matumizi ya curl hapo juu, unatumia ombi la POST kuitisha zana kwa kutumia payload inayojumuisha jina la zana na vigezo vyake. Tumia njia inayokufaa zaidi. Zana za CLI kwa ujumla huwa rahisi na zinaweza kuandikwa kwa maandishi ambayo inaweza kuwa muhimu katika mazingira ya CI/CD.

### Kupima kwa Vipande

Tengeneza vipimo vya vipande kwa zana na rasilimali zako ili kuhakikisha zinafanya kazi kama inavyotarajiwa. Hapa kuna mfano wa msimbo wa kupima.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Taja moduli yote kwa ajili ya majaribio ya async
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Tengeneza baadhi ya zana za majaribio
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

        # Jaribu na cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Jaribu na cursor kama mfuatiliaji wa maandishi
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Jaribu na cursor kama mfuatiliaji wa maandishi mtupu
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Msimbo huu ulio hapo juu hufanya yafuatayo:

- Kutumia mfumo wa pytest unaokuwezesha kuunda vipimo kama kazi na kutumia taarifa za assert.
- Kuunda Seva ya MCP yenye zana mbili tofauti.
- Kutumia taarifa ya `assert` kuhakikisha hali fulani zimekutana.

Tazama [faili kamili hapa](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Kwa kutumia faili hapo juu, unaweza kupima seva yako mwenyewe kuhakikisha uwezo umeundwa kama unavyotakiwa.

SDK zote kuu zina sehemu sawa za kupima hivyo unaweza kubadilisha kulingana na runtime uliyochagua.

## Sampuli

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Rasilimali Zaidi

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Kitu Kinachofuata

- Ifuatayo: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Hukumu**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mwaminifu. Kwa habari muhimu, tafsiri ya mtaalamu wa kibinadamu inapendekezwa. Hatuwajibiki kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->