## Pagsusuri at Pag-debug

Bago ka magsimulang magsuri ng iyong MCP server, mahalagang maunawaan ang mga magagamit na kagamitan at pinakamahusay na mga gawain para sa pag-debug. Ang epektibong pagsusuri ay nagsisiguro na ang iyong server ay kumikilos ayon sa inaasahan at tumutulong sa iyong mabilis na matukoy at malutas ang mga isyu. Ang sumusunod na seksyon ay naglalahad ng mga inirerekomendang pamamaraan para sa pag-validate ng iyong implementasyon ng MCP.

## Pangkalahatang-ideya

Tinatalakay sa araling ito kung paano pumili ng tamang paraan ng pagsusuri at ang pinakaepektibong kagamitan sa pagsusuri.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Ilarawan ang iba't ibang pamamaraan para sa pagsusuri.
- Gumamit ng iba't ibang kagamitan upang epektibong masuri ang iyong kodigo.

## Pagsusuri ng MCP Servers

Nagbibigay ang MCP ng mga kagamitan upang tulungan kang suriin at i-debug ang iyong mga server:

- **MCP Inspector**: Isang command line tool na maaaring patakbuhin bilang CLI tool at bilang isang visual tool.
- **Manwal na pagsusuri**: Maaari kang gumamit ng tool tulad ng curl upang magsagawa ng mga kahilingan sa web, ngunit anumang tool na kaya ang HTTP ay maaaring gamitin.
- **Unit testing**: Posibleng gamitin ang iyong paboritong testing framework upang subukan ang mga tampok ng parehong server at client.

### Paggamit ng MCP Inspector

Naipaliwanag na namin ang paggamit ng tool na ito sa mga naunang aralin ngunit pag-usapan natin ito nang bahagya sa mataas na antas. Ito ay isang tool na ginawa sa Node.js at maaari mo itong gamitin sa pamamagitan ng pag-tawag sa `npx` executable na magda-download at mag-i-install ng tool mismo nang pansamantala at lilinisin ang sarili kapag natapos na ang pagpapatakbo ng iyong kahilingan.

Ang [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ay tumutulong sa iyo na:

- **Tuklasin ang Kakayahan ng Server**: Awtomatikong tuklasin ang mga magagamit na resources, tools, at prompts
- **Subukan ang Pagpapatakbo ng Tool**: Subukan ang iba't ibang mga parameter at makita ang mga tugon nang real-time
- **Tingnan ang Metadata ng Server**: Suriin ang impormasyon ng server, mga schema, at mga konfigurasyon

Ang isang tipikal na pagpapatakbo ng tool ay ganito:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Ang utos sa itaas ay nagsisimula ng isang MCP at ang visual interface nito at nagpapalunsad ng lokal na web interface sa iyong browser. Maaari mong asahan makita ang isang dashboard na nagpapakita ng iyong mga rehistradong MCP servers, ang kanilang mga magagamit na tools, resources, at prompts. Pinapayagan ka ng interface na ito na interaktibong subukan ang pagpapatakbo ng tool, siyasatin ang metadata ng server, at tingnan ang mga tugon nang real-time, na nagpapadali upang i-validate at i-debug ang iyong mga implementasyon ng MCP server.

Ganito ang maaaring hitsura nito: ![Inspector](../../../../translated_images/tl/connect.141db0b2bd05f096.webp)

Maaari mo ring patakbuhin ang tool na ito sa CLI mode kung saan idaragdag mo ang `--cli` attribute. Narito ang isang halimbawa ng pagpapatakbo ng tool sa "CLI" mode na naglilista ng lahat ng mga tools sa server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```


### Manwal na Pagsusuri

Bukod sa pagpapatakbo ng inspector tool upang subukan ang kakayahan ng server, isa pang kahalintulad na pamamaraan ay ang pagpapatakbo ng isang client na kayang gumamit ng HTTP tulad ng curl.

Sa curl, maaari mong direktang subukan ang mga MCP servers gamit ang mga HTTP requests:

```bash
# Halimbawa: Metadata ng test server
curl http://localhost:3000/v1/metadata

# Halimbawa: Isagawa ang isang tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Tulad ng makikita mo mula sa paggamit ng curl sa itaas, gumagamit ka ng POST request upang tawagin ang isang tool gamit ang payload na binubuo ng pangalan ng tool at mga parameter nito. Gamitin ang paraan na pinakabagay sa iyo. Karaniwan, mas mabilis gamitin ang mga CLI tools at madalas nitong pinapayagan ang pag-script na maaaring maging kapaki-pakinabang sa isang CI/CD na kapaligiran.

### Unit Testing

Gumawa ng mga unit test para sa iyong mga tools at resources upang matiyak na gumagana ang mga ito ayon sa inaasahan. Narito ang ilang halimbawa ng testing code.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Markahan ang buong module para sa mga async na pagsubok
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Gumawa ng ilang mga kasangkapan sa pagsubok
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Subukan nang walang cursor na parameter (nilaktawan)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Subukan gamit ang cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Subukan gamit ang cursor bilang string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Subukan gamit ang walang laman na string na cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Ang kahinaang kodigo ay gumagawa ng mga sumusunod:

- Ginagamit ang pytest framework na nagpapahintulot sa iyo na gumawa ng mga pagsusuri bilang mga function at gumamit ng mga assert statement.
- Lumilikha ng isang MCP Server na may dalawang magkaibang tools.
- Gumagamit ng `assert` statement upang suriin na natutupad ang ilang mga kundisyon.

Tingnan ang [buong file dito](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Batay sa file sa itaas, maaari mong subukan ang iyong sariling server upang matiyak na ang mga kakayahan ay nalilikha ayon sa inaasahan.

Lahat ng pangunahing SDK ay may katulad na mga seksyon sa pagsusuri kaya maaari kang mag-adjust sa iyong napiling runtime.

## Mga Sample

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Karagdagang mga Mapagkukunan

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Ano Ang Susunod

- Susunod: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->