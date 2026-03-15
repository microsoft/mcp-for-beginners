## Testning och Felsökning

Innan du börjar testa din MCP-server är det viktigt att förstå de tillgängliga verktygen och bästa praxis för felsökning. Effektiv testning säkerställer att din server beter sig som förväntat och hjälper dig att snabbt identifiera och lösa problem. Följande avsnitt beskriver rekommenderade tillvägagångssätt för att validera din MCP-implementering.

## Översikt

Denna lektion täcker hur du väljer rätt testningsmetod och den mest effektiva testverktyget.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Beskriva olika metoder för testning.
- Använda olika verktyg för att effektivt testa din kod.

## Testa MCP-servrar

MCP erbjuder verktyg som hjälper dig att testa och felsöka dina servrar:

- **MCP Inspector**: Ett kommandoradsverktyg som kan köras både som CLI-verktyg och som ett visuellt verktyg.
- **Manuell testning**: Du kan använda ett verktyg som curl för att köra webbförfrågningar, men vilket verktyg som helst som kan köra HTTP fungerar.
- **Enhetstestning**: Det är möjligt att använda ditt föredragna testningsramverk för att testa funktionerna hos både server och klient.

### Använda MCP Inspector

Vi har beskrivit användningen av detta verktyg i tidigare lektioner, men låt oss prata om det lite på hög nivå. Det är ett verktyg byggt i Node.js och du kan använda det genom att kalla på `npx`-körbar fil som tillfälligt laddar ner och installerar verktyget och sedan städar upp sig när det har kört din förfrågan.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) hjälper dig att:

- **Upptäcka serverfunktioner**: Upptäck automatiskt tillgängliga resurser, verktyg och uppmaningar
- **Testa verktygsexekvering**: Prova olika parametrar och se svar i realtid
- **Visa servermetadata**: Undersök serverinformation, scheman och konfigurationer

Ett typiskt körningskommando ser ut så här:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Ovanstående kommando startar en MCP och dess visuella gränssnitt och öppnar en lokal webbgränssnitt i din webbläsare. Du kan förvänta dig att se en instrumentpanel som visar dina registrerade MCP-servrar, deras tillgängliga verktyg, resurser och uppmaningar. Gränssnittet möjliggör interaktiv testning av verktygsexekvering, inspektion av servermetadata och visning av svar i realtid, vilket gör det enklare att validera och felsöka dina MCP-serverimplementationer.

Så här kan det se ut: ![Inspector](../../../../translated_images/sv/connect.141db0b2bd05f096.webp)

Du kan också köra detta verktyg i CLI-läge, då lägger du till attributet `--cli`. Här är ett exempel på att köra verktyget i "CLI"-läge som listar alla verktyg på servern:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuell Testning

Förutom att köra inspector-verktyget för att testa serverfunktioner finns ett annat liknande sätt att köra en klient som kan använda HTTP, till exempel curl.

Med curl kan du testa MCP-servrar direkt via HTTP-förfrågningar:

```bash
# Exempel: Testa servermetadata
curl http://localhost:3000/v1/metadata

# Exempel: Utför ett verktyg
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Som du kan se från ovanstående användning av curl använder du en POST-förfrågan för att anropa ett verktyg med en belastning som består av verktygets namn och dess parametrar. Använd det tillvägagångssätt som passar dig bäst. CLI-verktyg är i allmänhet snabbare att använda och lämpar sig väl för skriptning, vilket kan vara användbart i en CI/CD-miljö.

### Enhetstestning

Skapa enhetstester för dina verktyg och resurser för att säkerställa att de fungerar som de ska. Här är ett exempel på testkod.

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
        # Testa utan cursor-parameter (utlämnad)
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

Ovanstående kod gör följande:

- Använder pytest-ramverket som låter dig skapa tester som funktioner och använda assert-satser.
- Skapar en MCP-server med två olika verktyg.
- Använder `assert`-satsen för att kontrollera att vissa villkor uppfylls.

Ta en titt på [hela filen här](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Med ovanstående fil kan du testa din egen server för att se till att funktioner skapas som de ska.

Alla större SDK:er har liknande testavsnitt så du kan anpassa dig till den miljö du valt.

## Exempel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Ytterligare Resurser

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Vad som kommer härnäst

- Nästa: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->