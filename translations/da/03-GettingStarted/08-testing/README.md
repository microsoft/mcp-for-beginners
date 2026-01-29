## Test og fejlfinding

Før du begynder at teste din MCP-server, er det vigtigt at forstå de tilgængelige værktøjer og bedste praksis for fejlfinding. Effektiv test sikrer, at din server opfører sig som forventet og hjælper dig med hurtigt at identificere og løse problemer. Følgende afsnit beskriver anbefalede metoder til at validere din MCP-implementering.

## Oversigt

Denne lektion handler om, hvordan du vælger den rette testmetode og det mest effektive testværktøj.

## Læringsmål

Når du har gennemført denne lektion, vil du kunne:

- Beskrive forskellige tilgange til test.
- Bruge forskellige værktøjer til effektivt at teste din kode.

## Test af MCP-servere

MCP tilbyder værktøjer, der hjælper dig med at teste og fejlsøge dine servere:

- **MCP Inspector**: Et kommandolinjeværktøj, der kan køres både som CLI-værktøj og som et visuelt værktøj.
- **Manuel test**: Du kan bruge et værktøj som curl til at køre web-forespørgsler, men ethvert værktøj, der kan håndtere HTTP, kan bruges.
- **Unit testing**: Det er muligt at bruge dit foretrukne testframework til at teste funktionerne i både server og klient.

### Brug af MCP Inspector

Vi har tidligere beskrevet brugen af dette værktøj, men lad os tage et overblik. Det er et værktøj bygget i Node.js, og du kan bruge det ved at kalde `npx`-eksekverbaren, som midlertidigt downloader og installerer værktøjet og rydder op, når din forespørgsel er kørt færdig.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) hjælper dig med at:

- **Opdage serverfunktioner**: Automatisk finde tilgængelige ressourcer, værktøjer og prompts
- **Teste værktøjsudførelse**: Prøve forskellige parametre og se svar i realtid
- **Se servermetadata**: Undersøge serverinfo, skemaer og konfigurationer

Et typisk kørsel af værktøjet ser sådan ud:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Ovenstående kommando starter en MCP og dens visuelle interface og åbner en lokal webgrænseflade i din browser. Du kan forvente at se et dashboard, der viser dine registrerede MCP-servere, deres tilgængelige værktøjer, ressourcer og prompts. Interfacet giver dig mulighed for interaktivt at teste værktøjsudførelse, inspicere servermetadata og se svar i realtid, hvilket gør det nemmere at validere og fejlsøge dine MCP-serverimplementeringer.

Sådan kan det se ud: ![Inspector](../../../../translated_images/da/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

Du kan også køre dette værktøj i CLI-tilstand ved at tilføje `--cli` attributten. Her er et eksempel på at køre værktøjet i "CLI"-tilstand, som viser alle værktøjer på serveren:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuel test

Udover at køre inspector-værktøjet for at teste serverfunktioner, kan du også bruge en klient, der kan håndtere HTTP, som for eksempel curl.

Med curl kan du teste MCP-servere direkte ved hjælp af HTTP-forespørgsler:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Som du kan se i eksemplet med curl, bruger du en POST-forespørgsel til at kalde et værktøj med en payload bestående af værktøjets navn og dets parametre. Brug den metode, der passer dig bedst. CLI-værktøjer er generelt hurtigere at bruge og egner sig godt til scripting, hvilket kan være nyttigt i et CI/CD-miljø.

### Unit testing

Lav unit tests for dine værktøjer og ressourcer for at sikre, at de fungerer som forventet. Her er et eksempel på testkode.

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

Koden ovenfor gør følgende:

- Benytter pytest-frameworket, som lader dig oprette tests som funktioner og bruge assert-udsagn.
- Opretter en MCP-server med to forskellige værktøjer.
- Bruger `assert`-udsagn til at kontrollere, at visse betingelser er opfyldt.

Tag et kig på [den fulde fil her](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Med udgangspunkt i denne fil kan du teste din egen server for at sikre, at funktionaliteterne oprettes som de skal.

Alle større SDK’er har lignende testsektioner, så du kan tilpasse det til dit valgte runtime-miljø.

## Eksempler

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Yderligere ressourcer

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Hvad er det næste

- Næste: [Deployment](../09-deployment/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.