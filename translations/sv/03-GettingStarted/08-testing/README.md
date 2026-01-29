## Testning och Felsökning

Innan du börjar testa din MCP-server är det viktigt att förstå vilka verktyg som finns tillgängliga och vilka bästa metoder som gäller för felsökning. Effektiv testning säkerställer att din server fungerar som förväntat och hjälper dig att snabbt identifiera och åtgärda problem. Följande avsnitt beskriver rekommenderade metoder för att validera din MCP-implementation.

## Översikt

Den här lektionen handlar om hur du väljer rätt testmetod och det mest effektiva testverktyget.

## Lärandemål

Efter den här lektionen kommer du att kunna:

- Beskriva olika metoder för testning.
- Använda olika verktyg för att effektivt testa din kod.

## Testa MCP-servrar

MCP erbjuder verktyg som hjälper dig att testa och felsöka dina servrar:

- **MCP Inspector**: Ett kommandoradsverktyg som kan köras både som CLI-verktyg och som ett visuellt verktyg.
- **Manuell testning**: Du kan använda ett verktyg som curl för att göra webbförfrågningar, men vilket verktyg som helst som kan hantera HTTP fungerar.
- **Enhetstestning**: Det går att använda ditt föredragna testningsramverk för att testa funktioner i både server och klient.

### Använda MCP Inspector

Vi har beskrivit hur man använder detta verktyg i tidigare lektioner, men låt oss ta en kort översikt. Det är ett verktyg byggt i Node.js och du kan använda det genom att köra `npx`-exekverbara filen, som laddar ner och installerar verktyget temporärt och sedan städar upp efter sig när din förfrågan är klar.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) hjälper dig att:

- **Upptäcka serverfunktioner**: Identifiera automatiskt tillgängliga resurser, verktyg och prompts
- **Testa verktygsexekvering**: Prova olika parametrar och se svar i realtid
- **Visa servermetadata**: Granska serverinformation, scheman och konfigurationer

Ett typiskt körningskommando ser ut så här:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Ovanstående kommando startar en MCP och dess visuella gränssnitt och öppnar en lokal webbgränssnitt i din webbläsare. Du kan förvänta dig att se en instrumentpanel som visar dina registrerade MCP-servrar, deras tillgängliga verktyg, resurser och prompts. Gränssnittet låter dig interaktivt testa verktygsexekvering, inspektera servermetadata och se svar i realtid, vilket gör det enklare att validera och felsöka dina MCP-serverimplementationer.

Så här kan det se ut: ![Inspector](../../../../translated_images/sv/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

Du kan också köra verktyget i CLI-läge genom att lägga till attributet `--cli`. Här är ett exempel på att köra verktyget i "CLI"-läge som listar alla verktyg på servern:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuell testning

Förutom att köra inspector-verktyget för att testa serverfunktioner kan du använda en klient som kan hantera HTTP, till exempel curl.

Med curl kan du testa MCP-servrar direkt med HTTP-förfrågningar:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Som du kan se i exemplet ovan använder du en POST-förfrågan för att anropa ett verktyg med en payload som innehåller verktygets namn och dess parametrar. Använd den metod som passar dig bäst. CLI-verktyg är generellt snabbare att använda och lämpar sig väl för skriptning, vilket kan vara användbart i en CI/CD-miljö.

### Enhetstestning

Skapa enhetstester för dina verktyg och resurser för att säkerställa att de fungerar som förväntat. Här är ett exempel på testkod.

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

Koden ovan gör följande:

- Använder pytest-ramverket som låter dig skapa tester som funktioner och använda assert-satser.
- Skapar en MCP-server med två olika verktyg.
- Använder `assert` för att kontrollera att vissa villkor uppfylls.

Ta en titt på [hela filen här](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Med hjälp av filen ovan kan du testa din egen server för att säkerställa att funktionerna skapas som de ska.

Alla större SDK:er har liknande testavsnitt så du kan anpassa efter din valda runtime.

## Exempel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Ytterligare resurser

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Vad händer härnäst

- Nästa: [Deployment](../09-deployment/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.