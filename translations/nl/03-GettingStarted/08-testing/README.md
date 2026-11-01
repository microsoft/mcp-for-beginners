## Testen en Debuggen

Voordat je begint met het testen van je MCP-server, is het belangrijk om de beschikbare tools en best practices voor debugging te begrijpen. Effectief testen zorgt ervoor dat je server zich gedraagt zoals verwacht en helpt je om snel problemen te identificeren en op te lossen. De volgende sectie beschrijft aanbevolen benaderingen voor het valideren van je MCP-implementatie.

## Overzicht

Deze les behandelt hoe je de juiste testaanpak selecteert en de meest effectieve testtool gebruikt.

## Leerdoelen

Aan het einde van deze les kun je:

- Verschillende benaderingen voor testen beschrijven.
- Verschillende tools gebruiken om je code effectief te testen.


## MCP-servers testen

MCP biedt tools om je te helpen je servers te testen en te debuggen:

- **MCP Inspector**: Een commandoregeltool die zowel als CLI-tool als visueel hulpmiddel kan worden gebruikt.
- **Handmatig testen**: Je kunt een tool zoals curl gebruiken om webverzoeken uit te voeren, maar elke tool die HTTP kan draaien is geschikt.
- **Unit testing**: Het is mogelijk om je favoriete testframework te gebruiken om functies van zowel server als client te testen.

### Gebruik van MCP Inspector

We hebben het gebruik van deze tool in eerdere lessen beschreven, maar laten we er hier kort iets over zeggen. Het is een tool gebouwd in Node.js en je kunt het gebruiken door de `npx` uitvoerbare file aan te roepen, die de tool tijdelijk downloadt en installeert en zichzelf opruimt zodra je verzoek is uitgevoerd.

De [MCP Inspector](https://github.com/modelcontextprotocol/inspector) helpt je met:

- **Servermogelijkheden ontdekken**: Automatisch beschikbare resources, tools en prompts detecteren
- **Test uitvoering van tools**: Probeer verschillende parameters en zie responsen in realtime
- **Servermetadata bekijken**: Bekijk serverinformatie, schema's en configuraties

Een typische uitvoering van de tool ziet er als volgt uit:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Het bovenstaande commando start een MCP en de visuele interface en opent een lokale webinterface in je browser. Je kunt een dashboard verwachten waarin je geregistreerde MCP-servers, hun beschikbare tools, resources en prompts worden weergegeven. De interface stelt je in staat om interactief tools uit te voeren, servermetadata te inspecteren en realtime responsen te bekijken, wat het makkelijker maakt om je MCP-serverimplementaties te valideren en te debuggen.

Zo kan het eruit zien: ![Inspector](../../../../translated_images/nl/connect.141db0b2bd05f096.webp)

Je kunt deze tool ook in CLI-modus draaien, waarvoor je de `--cli` attribuut toevoegt. Hier is een voorbeeld van het draaien van de tool in "CLI"-modus die alle tools op de server opsomt:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Handmatig testen

Afgezien van het draaien van de inspector tool om de servermogelijkheden te testen, is een vergelijkbare aanpak het draaien van een client die HTTP kan gebruiken zoals bijvoorbeeld curl.

Met curl kun je MCP-servers direct testen met HTTP-verzoeken:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Zoals je kunt zien bij het bovenstaande gebruik van curl, gebruik je een POST-verzoek om een tool aan te roepen met een payload die bestaat uit de naam van de tool en de parameters. Gebruik de methode die jou het beste past. CLI-tools zijn over het algemeen sneller in gebruik en lenen zich voor scripting wat nuttig kan zijn in een CI/CD-omgeving.

### Unit Testing

Maak unittests voor je tools en resources om te zorgen dat ze werken zoals verwacht. Hier is voorbeeld testcode.

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

De bovenstaande code doet het volgende:

- Maakt gebruik van het pytest-framework waarmee je tests als functies maakt en assert-statements gebruikt.
- Maakt een MCP-server aan met twee verschillende tools.
- Gebruikt de `assert` statement om te controleren of bepaalde voorwaarden zijn vervuld.

Kijk naar het [volledige bestand hier](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Met het bovenstaande bestand kun je je eigen server testen om te zorgen dat de mogelijkheden worden gecreëerd zoals ze zouden moeten.

Alle belangrijke SDK's hebben vergelijkbare testsecties, zodat je kunt aanpassen aan je gekozen runtime.

## Voorbeelden

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Aanvullende bronnen

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Wat is het volgende

- Volgende: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->