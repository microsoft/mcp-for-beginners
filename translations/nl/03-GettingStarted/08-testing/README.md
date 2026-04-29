## Testen en Debuggen

Voordat je begint met het testen van je MCP-server, is het belangrijk om de beschikbare tools en best practices voor debugging te begrijpen. Effectief testen zorgt ervoor dat je server zich gedraagt zoals verwacht en helpt je snel problemen te identificeren en op te lossen. De volgende sectie beschrijft aanbevolen benaderingen voor het valideren van je MCP-implementatie.

## Overzicht

Deze les behandelt hoe je de juiste testbenadering kiest en de meest effectieve testtool gebruikt.

## Leerdoelen

Aan het einde van deze les kun je:

- Verschillende benaderingen voor testen beschrijven.
- Verschillende tools gebruiken om je code effectief te testen.

## MCP-Servers Testen

MCP biedt tools om je te helpen je servers te testen en debuggen:

- **MCP Inspector**: Een commandoregeltool die zowel als CLI-tool als visuele tool kan worden gebruikt.
- **Handmatig testen**: Je kunt een tool zoals curl gebruiken om webverzoeken uit te voeren, maar elke tool die HTTP kan gebruiken is geschikt.
- **Unittesten**: Het is mogelijk om je favoriete testframework te gebruiken om de functionaliteiten van zowel server als client te testen.

### MCP Inspector Gebruiken

We hebben het gebruik van deze tool al in eerdere lessen beschreven, maar laten we er hier op hoofdlijnen iets over zeggen. Het is een in Node.js gebouwd hulpmiddel dat je kunt gebruiken door het `npx` uitvoerbare bestand aan te roepen, dat de tool zelf tijdelijk downloadt en installeert en zichzelf weer opruimt zodra het klaar is met het uitvoeren van je verzoek.

De [MCP Inspector](https://github.com/modelcontextprotocol/inspector) helpt je met:

- **Servercapaciteiten Ontdekken**: Detecteert automatisch beschikbare resources, tools en prompts
- **Testen van Tooluitvoering**: Probeer verschillende parameters en zie de reacties in real-time
- **Bekijk Servermetadata**: Bekijk serverinformatie, schema's en configuraties

Een typische uitvoering van de tool ziet er als volgt uit:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Bovenstaande opdracht start een MCP en de visuele interface en opent een lokale webinterface in je browser. Je kunt een dashboard verwachten met je geregistreerde MCP-servers, hun beschikbare tools, resources en prompts. De interface stelt je in staat interactief tooluitvoering te testen, servermetadata te inspecteren en realtime reacties te bekijken, wat het gemakkelijker maakt om je MCP-serverimplementaties te valideren en te debuggen.

Zo kan het eruitzien: ![Inspector](../../../../translated_images/nl/connect.141db0b2bd05f096.webp)

Je kunt deze tool ook in CLI-modus uitvoeren door de `--cli` optie toe te voegen. Hier is een voorbeeld om de tool in "CLI"-modus te draaien, wat een lijst van alle tools op de server geeft:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Handmatig Testen

Naast het uitvoeren van de inspector-tool om servercapaciteiten te testen, is een andere vergelijkbare aanpak het draaien van een client die HTTP kan gebruiken, zoals bijvoorbeeld curl.

Met curl kun je MCP-servers direct testen met HTTP-verzoeken:

```bash
# Voorbeeld: Metadata van testserver
curl http://localhost:3000/v1/metadata

# Voorbeeld: Voer een hulpmiddel uit
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Zoals je ziet in het bovenstaande gebruik van curl, gebruik je een POST-verzoek om een tool aan te roepen met een payload die de naam van de tool en de parameters bevat. Gebruik de methode die jou het beste past. CLI-tools zijn over het algemeen sneller in gebruik en lenen zich goed voor scripting, wat handig kan zijn in een CI/CD-omgeving.

### Unittesten

Maak unittests voor je tools en resources om te zorgen dat ze correct werken. Hier is wat voorbeeldcode voor testen.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Markeer de hele module voor async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Maak een paar testtools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test zonder cursorparameter (weggelaten)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test met cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test met cursor als string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test met lege string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

De bovenstaande code doet het volgende:

- Maakt gebruik van het pytest-framework waarmee je tests als functies kunt maken en assert-statements kunt gebruiken.
- Creëert een MCP-server met twee verschillende tools.
- Gebruikt een `assert` statement om te controleren of bepaalde voorwaarden zijn vervuld.

Bekijk het [volledige bestand hier](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Met dat bestand kun je je eigen server testen om te zorgen dat de capaciteiten correct zijn aangemaakt.

Alle grote SDK's hebben vergelijkbare testsecties, dus je kunt dit aanpassen aan je gekozen runtime.

## Voorbeelden

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Aanvullende Bronnen

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Wat Nu

- Volgende: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel wij streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->