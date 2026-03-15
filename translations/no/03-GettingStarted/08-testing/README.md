## Testing og feilsøking

Før du begynner å teste MCP-serveren din, er det viktig å forstå de tilgjengelige verktøyene og beste praksis for feilsøking. Effektiv testing sørger for at serveren din oppfører seg som forventet og hjelper deg med å raskt identifisere og løse problemer. Følgende seksjon beskriver anbefalte tilnærminger for å validere MCP-implementeringen din.

## Oversikt

Denne leksjonen dekker hvordan du velger riktig testtilnærming og det mest effektive testverktøyet.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Beskrive ulike tilnærminger for testing.
- Bruke forskjellige verktøy for å effektivt teste koden din.


## Testing av MCP-servere

MCP tilbyr verktøy for å hjelpe deg med å teste og feilsøke serverne dine:

- **MCP Inspector**: Et kommandolinjeverktøy som kan kjøres både som et CLI-verktøy og som et visuelt verktøy.
- **Manuell testing**: Du kan bruke et verktøy som curl for å kjøre webforespørsler, men ethvert verktøy som kan kjøre HTTP, fungerer.
- **Enhetstesting**: Det er mulig å bruke ditt foretrukne testframework for å teste funksjonene til både server og klient.

### Bruke MCP Inspector

Vi har beskrevet bruken av dette verktøyet i tidligere leksjoner, men la oss snakke litt om det på et overordnet nivå. Det er et verktøy bygget i Node.js, og du kan bruke det ved å kjøre `npx`-kjørbarheten som vil laste ned og installere verktøyet midlertidig, og deretter rydde det opp når forespørselen din er ferdig kjørt.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) hjelper deg med å:

- **Oppdage serverfunksjoner**: Automatisk oppdage tilgjengelige ressurser, verktøy og prompt
- **Teste verktøykjøring**: Prøve ulike parametere og se svar i sanntid
- **Se servermetadata**: Undersøke serverinfo, skjemaer og konfigurasjoner

Et typisk kjøringskommando for verktøyet ser slik ut:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Kommandoen over starter en MCP og dens visuelle grensesnitt og åpner et lokalt webgrensesnitt i nettleseren din. Du kan forvente å se et dashbord som viser dine registrerte MCP-servere, deres tilgjengelige verktøy, ressurser og prompt. Grensesnittet lar deg interaktivt teste verktøykjøring, inspisere servermetadata og se sanntidssvar, noe som gjør det enklere å validere og feilsøke dine MCP-serverimplementasjoner.

Slik kan det se ut: ![Inspector](../../../../translated_images/no/connect.141db0b2bd05f096.webp)

Du kan også kjøre dette verktøyet i CLI-modus, der du legger til `--cli`-attributtet. Her er et eksempel på å kjøre verktøyet i "CLI"-modus som lister opp alle verktøyene på serveren:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuell testing

Bortsett fra å kjøre inspector-verktøyet for å teste serverfunksjoner, er en annen tilsvarende tilnærming å kjøre en klient som kan bruke HTTP, for eksempel curl.

Med curl kan du teste MCP-servere direkte ved bruk av HTTP-forespørsler:

```bash
# Eksempel: Test server metadata
curl http://localhost:3000/v1/metadata

# Eksempel: Utfør et verktøy
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Som du kan se fra eksempelet med curl over, bruker du en POST-forespørsel for å kalle et verktøy ved hjelp av en nyttelast som består av verktøyets navn og dets parametere. Bruk den tilnærmingen som passer deg best. CLI-verktøy er vanligvis raskere å bruke og egner seg godt for skripting, noe som kan være nyttig i et CI/CD-miljø.

### Enhetstesting

Lag enhetstester for verktøyene og ressursene dine for å sikre at de fungerer som forventet. Her er et eksempel på testkode.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Merk hele modulen for asynkrone tester
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Lag et par testverktøy
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test uten markørparameter (utelatt)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test med markør=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test med markør som streng
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test med tom streng som markør
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Koden ovenfor gjør følgende:

- Bruker pytest-rammeverket som lar deg lage tester som funksjoner og bruker assert-setninger.
- Oppretter en MCP-server med to forskjellige verktøy.
- Bruker `assert`-setning for å sjekke at visse betingelser er oppfylt.

Se [hele filen her](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Gitt filen over kan du teste din egen server for å sikre at funksjonene opprettes som de skal.

Alle større SDK-er har lignende testseksjoner, så du kan tilpasse til ditt valgte kjøretidsmiljø.

## Eksempler

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Ekstra ressurser

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Hva nå

- Neste: [Distribusjon](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på det opprinnelige språket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår fra bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->