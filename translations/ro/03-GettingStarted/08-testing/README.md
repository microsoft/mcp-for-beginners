## Testare și depanare

Înainte de a începe testarea serverului tău MCP, este important să înțelegi uneltele disponibile și cele mai bune practici pentru depanare. Testarea eficientă asigură că serverul tău funcționează conform așteptărilor și te ajută să identifici și să rezolvi rapid problemele. Secțiunea următoare prezintă metode recomandate pentru validarea implementării MCP.

## Prezentare generală

Această lecție explică cum să alegi abordarea potrivită pentru testare și cel mai eficient instrument de testare.

## Obiective de învățare

La finalul acestei lecții, vei putea să:

- Descrii diferite metode de testare.
- Folosești diverse unelte pentru a testa eficient codul tău.

## Testarea serverelor MCP

MCP oferă unelte care te ajută să testezi și să depanezi serverele tale:

- **MCP Inspector**: Un instrument de linie de comandă care poate fi folosit atât ca CLI, cât și ca interfață vizuală.
- **Testare manuală**: Poți folosi un instrument precum curl pentru a rula cereri web, dar orice unealtă capabilă să ruleze HTTP este potrivită.
- **Testare unitară**: Poți folosi cadrul de testare preferat pentru a testa funcționalitățile atât ale serverului, cât și ale clientului.

### Folosirea MCP Inspector

Am descris utilizarea acestui instrument în lecțiile anterioare, dar să discutăm puțin la nivel general. Este un instrument construit în Node.js și îl poți folosi apelând executabilul `npx`, care va descărca și instala temporar instrumentul și se va curăța automat după ce a terminat de rulat cererea ta.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) te ajută să:

- **Descoperi capabilitățile serverului**: Detectează automat resursele, uneltele și prompturile disponibile
- **Testezi execuția uneltelor**: Încearcă diferiți parametri și vezi răspunsurile în timp real
- **Vizualizezi metadatele serverului**: Examinează informațiile serverului, schemele și configurațiile

O rulare tipică a instrumentului arată astfel:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Comanda de mai sus pornește un MCP și interfața sa vizuală și lansează o interfață web locală în browserul tău. Te poți aștepta să vezi un panou de control care afișează serverele MCP înregistrate, uneltele, resursele și prompturile disponibile. Interfața îți permite să testezi interactiv execuția uneltelor, să inspectezi metadatele serverului și să vezi răspunsurile în timp real, facilitând validarea și depanarea implementărilor serverului MCP.

Iată cum poate arăta: ![Inspector](../../../../translated_images/ro/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

Poți rula acest instrument și în modul CLI, caz în care adaugi atributul `--cli`. Iată un exemplu de rulare în modul "CLI" care listează toate uneltele de pe server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Testare manuală

Pe lângă rularea instrumentului inspector pentru a testa capabilitățile serverului, o altă abordare similară este să folosești un client capabil să folosească HTTP, cum ar fi curl.

Cu curl, poți testa serverele MCP direct folosind cereri HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

După cum vezi din exemplul de mai sus cu curl, folosești o cerere POST pentru a invoca o unealtă folosind un payload care conține numele uneltei și parametrii săi. Folosește abordarea care ți se potrivește cel mai bine. Uneltele CLI sunt în general mai rapide și pot fi ușor integrate în scripturi, ceea ce poate fi util într-un mediu CI/CD.

### Testare unitară

Creează teste unitare pentru uneltele și resursele tale pentru a te asigura că funcționează conform așteptărilor. Iată un exemplu de cod pentru testare.

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

Codul de mai sus face următoarele:

- Folosește cadrul pytest care îți permite să creezi teste ca funcții și să folosești instrucțiuni assert.
- Creează un server MCP cu două unelte diferite.
- Folosește instrucțiunea `assert` pentru a verifica dacă anumite condiții sunt îndeplinite.

Aruncă o privire la [fișierul complet aici](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Având acest fișier, poți testa propriul server pentru a te asigura că capabilitățile sunt create corect.

Toate SDK-urile majore au secțiuni similare de testare, așa că poți adapta la runtime-ul ales.

## Exemple

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Resurse suplimentare

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Ce urmează

- Următorul: [Deployment](../09-deployment/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.