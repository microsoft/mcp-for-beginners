## Pagsusuri at Pag-debug

Bago ka magsimulang subukan ang iyong MCP server, mahalagang maunawaan ang mga magagamit na kasangkapan at pinakamahuhusay na pamamaraan para sa pag-debug. Ang epektibong pagsusuri ay nagsisiguro na ang iyong server ay kumikilos nang naaayon sa inaasahan at tumutulong sa iyo na mabilis na matukoy at malutas ang mga isyu. Ang sumusunod na seksyon ay naglalahad ng mga inirerekomendang pamamaraan para sa pag-validate ng iyong implementasyon ng MCP.

## Pangkalahatang Pagsusuri

Tinutukoy ng leksyong ito kung paano pumili ng tamang pamamaraan sa pagsusuri at ang pinakaepektibong kasangkapan sa pagsusuri.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng leksyong ito, magagawa mong:

- Ilarawan ang iba't ibang pamamaraan para sa pagsusuri.
- Gumamit ng iba't ibang kasangkapan upang epektibong subukan ang iyong code.


## Pagsusuri ng MCP Servers

Nagbibigay ang MCP ng mga kasangkapan upang tumulong sa pagsusuri at pag-debug ng iyong mga server:

- **MCP Inspector**: Isang command line tool na maaaring patakbuhin bilang CLI tool at bilang visual tool.
- **Manwal na pagsusuri**: Maaari kang gumamit ng tool tulad ng curl upang magpatakbo ng mga web request, ngunit anumang kasangkapan na kayang magpatakbo ng HTTP ay maaaring gamitin.
- **Unit testing**: Posibleng gamitin ang iyong paboritong testing framework upang subukan ang mga feature ng parehong server at client.

### Paggamit ng MCP Inspector

Nailarawan namin ang paggamit ng tool na ito sa mga naunang leksyon ngunit pag-usapan muna natin ito sa pangkalahatang antas. Isa itong tool na ginawa sa Node.js at maaari mo itong gamitin sa pamamagitan ng pagtawag sa `npx` executable na magda-download at mag-iinstall ng tool mismo pansamantala at lilinisin ang sarili pagkatapos nitong patakbuhin ang iyong kahilingan.

Ang [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ay tumutulong sa iyo na:

- **Matuklasan ang mga Kakayahan ng Server**: Awtomatikong tuklasin ang mga magagamit na resources, tools, at prompts
- **Subukan ang Pagpapatakbo ng Tool**: Subukan ang iba't ibang mga parameter at tingnan ang mga tugon nang real-time
- **Tingnan ang Metadata ng Server**: Suriin ang impormasyon ng server, mga schema, at mga configuration

Ang isang tipikal na pagpapatakbo ng tool ay ganito:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Sinisimulan ng utos sa itaas ang MCP at ang visual interface nito at inilulunsad ang lokal na web interface sa iyong browser. Maaari mong asahan na makita ang isang dashboard na nagpapakita ng iyong mga nakarehistrong MCP servers, ang kanilang mga magagamit na tools, resources, at prompts. Pinapayagan ka ng interface na subukan ang pagpapatakbo ng mga tool nang interactive, siyasatin ang metadata ng server, at tingnan ang mga tugon nang real-time, na nagpapadali upang i-validate at i-debug ang iyong mga implementasyon ng MCP server.

Ganito ang maaaring itsura nito: ![Inspector](../../../../translated_images/tl/connect.141db0b2bd05f096.webp)

Maaari mo ring patakbuhin ang tool na ito sa CLI mode kung saan magdadagdag ka ng `--cli` na katangian. Narito ang isang halimbawa ng pagpapatakbo ng tool sa "CLI" mode na naglilista ng lahat ng mga tools sa server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manwal na Pagsusuri

Bukod sa pagpapatakbo ng inspector tool upang subukan ang kakayahan ng server, isa pang katulad na pamamaraan ay ang paggamit ng client na kayang gumamit ng HTTP gaya ng halimbawa ay curl.

Sa curl, maaari mong direktang subukan ang MCP servers gamit ang mga HTTP request:

```bash
# Halimbawa: Metadata ng test server
curl http://localhost:3000/v1/metadata

# Halimbawa: Patakbuhin ang isang tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Gaya ng makikita sa paggamit ng curl sa itaas, gumamit ka ng POST request upang tawagan ang isang tool gamit ang payload na binubuo ng pangalan ng tool at ang mga parameter nito. Gamitin ang pamamaraang pinakaangkop sa iyo. Ang mga CLI tool sa pangkalahatan ay mas mabilis gamitin at maaaring iskript na kapaki-pakinabang sa isang CI/CD na kapaligiran.

### Unit Testing

Gumawa ng mga unit test para sa iyong mga tools at resources upang masiguro na gumagana ang mga ito ayon sa inaasahan. Narito ang ilang halimbawa ng code para sa pagsusuri.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Markahan ang buong module para sa async na mga pagsubok
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
        # Subukang walang parameter na cursor (hiniwalay)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Subukang may cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Subukang may cursor bilang string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Subukang may blangkong string na cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Ang naunang code ay gumagawa ng mga sumusunod:

- Ginagamit ang pytest framework na nagpapahintulot sa iyo na gumawa ng mga pagsusuri bilang mga function at gumamit ng assert statements.
- Lumilikha ng MCP Server na may dalawang magkaibang tools.
- Gumagamit ng `assert` statement upang suriin na ang ilang mga kondisyon ay natutupad.

Tingnan ang [buong file dito](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Batay sa file sa itaas, maaari mong subukan ang iyong sariling server upang matiyak na ang mga kakayahan ay nalikha ayon sa dapat.

Lahat ng pangunahing SDK ay may katulad na mga seksyon ng pagsusuri kaya maaari kang mag-adjust ayon sa iyong piniling runtime.

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Karagdagang Mga Kagamitan

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Ano ang Susunod

- Susunod: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagsisi**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na pinagsanggunian ng katotohanan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->