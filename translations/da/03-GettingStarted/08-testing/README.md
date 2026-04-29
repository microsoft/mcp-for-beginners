## Testning og Fejlfinding

Før du begynder at teste din MCP-server, er det vigtigt at forstå de tilgængelige værktøjer og bedste praksis for fejlfinding. Effektiv test sikrer, at din server opfører sig som forventet og hjælper dig med hurtigt at identificere og løse problemer. Den følgende sektion skitserer anbefalede tilgange til validering af din MCP-implementering.

## Oversigt

Denne lektion dækker, hvordan du vælger den rette testmetode og det mest effektive testværktøj.

## Læringsmål

Når du er færdig med denne lektion, vil du kunne:

- Beskrive forskellige tilgange til testning.
- Bruge forskellige værktøjer til effektivt at teste din kode.


## Testning af MCP-servere

MCP tilbyder værktøjer, der hjælper dig med at teste og fejlsøge dine servere:

- **MCP Inspector**: Et kommandolinjeværktøj, der kan køres både som CLI-værktøj og som et visuelt værktøj.
- **Manuel testning**: Du kan bruge et værktøj som curl til at køre webanmodninger, men ethvert værktøj, der kan håndtere HTTP, vil fungere.
- **Unit testing**: Det er muligt at bruge dit foretrukne testframework til at teste funktionerne i både server og klient.

### Brug af MCP Inspector

Vi har beskrevet brugen af dette værktøj i tidligere lektioner, men lad os tale lidt om det på et overordnet niveau. Det er et værktøj bygget i Node.js, og du kan bruge det ved at kalde `npx`-eksekverbare fil, som midlertidigt downloader og installerer værktøjet og rydder op, når dit kald er færdigt.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) hjælper dig med:

- **Opdage serverfunktioner**: Automatisk at finde tilgængelige ressourcer, værktøjer og prompts
- **Teste værktøjsudførelse**: Prøv forskellige parametre og se svar i realtid
- **Se servermetadata**: Undersøg serverinfo, skemaer og konfigurationer

Et typisk kørsel af værktøjet ser sådan ud:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Ovenstående kommando starter en MCP og dens visuelle interface og åbner et lokalt webinterface i din browser. Du kan forvente at se et dashboard, der viser dine registrerede MCP-servere, deres tilgængelige værktøjer, ressourcer og prompts. Interfacet giver dig mulighed for interaktivt at teste værktøjsudførelse, inspicere servermetadata og se svar i realtid, hvilket gør det lettere at validere og fejlsøge dine MCP-serverimplementeringer.

Sådan kan det se ud: ![Inspector](../../../../translated_images/da/connect.141db0b2bd05f096.webp)

Du kan også køre dette værktøj i CLI-tilstand ved at tilføje `--cli` attributten. Her er et eksempel på at køre værktøjet i "CLI"-tilstand, som viser alle værktøjer på serveren:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuel Testning

Udover at køre inspector-værktøjet til at teste serverfunktioner, er en anden lignende tilgang at køre en klient, der kan anvende HTTP, for eksempel curl.

Med curl kan du teste MCP-servere direkte via HTTP-forespørgsler:

```bash
# Eksempel: Test server metadata
curl http://localhost:3000/v1/metadata

# Eksempel: Udfør et værktøj
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Som du kan se fra ovenstående brug af curl, bruger du en POST-forespørgsel til at kalde et værktøj ved hjælp af en payload bestående af værktøjets navn og dets parametre. Brug den tilgang, der passer dig bedst. CLI-værktøjer er generelt hurtigere at bruge og giver sig til scripting, hvilket kan være nyttigt i en CI/CD-miljø.

### Unit Testing

Opret enhedstests for dine værktøjer og ressourcer for at sikre, at de fungerer som forventet. Her er noget eksempelkode til test.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Marker hele modulet for asynkrone tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Opret et par testværktøjer
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test uden cursor-parameter (uteladt)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test med cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test med cursor som streng
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test med tom streng cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Den forudgående kode gør følgende:

- Udnytter pytest-rammen, som lader dig oprette tests som funktioner og bruge assert-sætninger.
- Opretter en MCP-server med to forskellige værktøjer.
- Bruger `assert`-sætningen til at kontrollere, at visse betingelser er opfyldt.

Se [hele filen her](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Med den ovenfor nævnte fil kan du teste din egen server for at sikre, at kapaciteter oprettes som forventet.

Alle større SDK'er har lignende testsektioner, så du kan tilpasse til dit valgte runtime.

## Eksempler

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Yderligere Ressourcer

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Hvad Er Næste Skridt

- Næste: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, som måtte opstå ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->