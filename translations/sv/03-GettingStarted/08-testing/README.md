## Testning och Felsökning

Innan du börjar testa din MCP-server är det viktigt att förstå vilka verktyg som finns tillgängliga och bästa praxis för felsökning. Effektiv testning säkerställer att din server beter sig som förväntat och hjälper dig snabbt identifiera och åtgärda problem. Följande avsnitt beskriver rekommenderade tillvägagångssätt för att validera din MCP-implementering.

## Översikt

Den här lektionen täcker hur du väljer rätt testmetod och det mest effektiva testverktyget.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Beskriva olika metoder för testning.
- Använda olika verktyg för att effektivt testa din kod.

## Testa MCP-servrar

MCP tillhandahåller verktyg för att hjälpa dig testa och felsöka dina servrar:

- **MCP Inspector**: Ett kommandoradsverktyg som kan köras både som CLI-verktyg och som ett visuellt verktyg.
- **Manuell testning**: Du kan använda ett verktyg som curl för att köra webbförfrågningar, men vilket verktyg som helst som kan köra HTTP fungerar.
- **Enhetstestning**: Det är möjligt att använda ditt föredragna testningsramverk för att testa funktionerna hos både server och klient.

### Använda MCP Inspector

Vi har beskrivit användningen av detta verktyg i tidigare lektioner men låt oss prata om det lite på en övergripande nivå. Det är ett verktyg byggt i Node.js och du kan använda det genom att köra `npx`-exekverbara filen, vilket temporärt laddar ner och installerar verktyget självt och städar upp efter sig när din förfrågan är kört.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) hjälper dig att:

- **Upptäcka serverkapabiliteter**: Automatiskt upptäcka tillgängliga resurser, verktyg och prompts
- **Testa verktygsexekvering**: Prova olika parametrar och se svar i realtid
- **Visa servermetadata**: Granska serverinformation, scheman och konfigurationer

Ett vanligt körningsexempel av verktyget ser ut så här:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Kommandot ovan startar en MCP och dess visuella gränssnitt och öppnar ett lokalt webbgränssnitt i din webbläsare. Du kan förvänta dig att se en instrumentpanel som visar dina registrerade MCP-servrar, deras tillgängliga verktyg, resurser och prompts. Gränssnittet låter dig interaktivt testa verktygsexekvering, inspektera servermetadata och se svar i realtid, vilket gör det enklare att validera och felsöka dina MCP-serverimplementationer.

Så här kan det se ut: ![Inspector](../../../../translated_images/sv/connect.141db0b2bd05f096.webp)

Du kan också köra detta verktyg i CLI-läge genom att lägga till attributet `--cli`. Här är ett exempel på att köra verktyget i "CLI"-läge som listar alla verktyg på servern:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuell testning

Förutom att köra inspector-verktyget för att testa serverkapabiliteter är en liknande metod att köra en klient som kan använda HTTP, till exempel curl.

Med curl kan du testa MCP-servrar direkt med HTTP-förfrågningar:

```bash
# Exempel: Testa servermetadata
curl http://localhost:3000/v1/metadata

# Exempel: Kör ett verktyg
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Som du kan se från ovanstående exempel på användning av curl, använder du en POST-förfrågan för att anropa ett verktyg med en nyttolast som består av verktygets namn och dess parametrar. Använd den metod som passar dig bäst. CLI-verktyg tenderar generellt att vara snabbare att använda och lämpar sig för automatisering, vilket kan vara användbart i en CI/CD-miljö.

### Enhetstestning

Skapa enhetstester för dina verktyg och resurser för att säkerställa att de fungerar som förväntat. Här är exempel på testkod.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Markera hela modulen för asynkrona tester
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Skapa ett par testverktyg
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testa utan cursor-parameter (utelämnad)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testa med cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testa med cursor som sträng
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testa med tom sträng som cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Den ovanstående koden gör följande:

- Använder pytest-ramverket som låter dig skapa tester som funktioner och använda assert-satser.
- Skapar en MCP-server med två olika verktyg.
- Använder `assert`-satser för att kontrollera att vissa villkor uppfylls.

Ta en titt på [hela filen här](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Med filen ovan kan du testa din egen server för att säkerställa att kapabiliteter skapas som de ska.

Alla större SDK:er har liknande testavsnitt så du kan anpassa till din valda runtime.

## Exempel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Ytterligare resurser

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Vad kommer härnäst

- Nästa: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungsspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->