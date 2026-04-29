## Testare și depanare

Înainte de a începe să testați serverul MCP, este important să înțelegeți instrumentele disponibile și cele mai bune practici pentru depanare. Testarea eficientă asigură că serverul dvs. se comportă conform așteptărilor și vă ajută să identificați și să rezolvați rapid problemele. Secțiunea următoare prezintă abordările recomandate pentru validarea implementării MCP.

## Prezentare generală

Această lecție acoperă cum să selectați abordarea potrivită pentru testare și cel mai eficient instrument de testare.

## Obiectivele de învățare

La finalul acestei lecții, veți putea:

- Descrie diverse abordări pentru testare.
- Folosi diferite instrumente pentru a testa eficient codul.

## Testarea serverelor MCP

MCP oferă instrumente pentru a vă ajuta să testați și să depanați serverele:

- **MCP Inspector**: Un instrument de linie de comandă ce poate fi folosit atât ca un utilitar CLI, cât și ca un instrument vizual.
- **Testare manuală**: Puteți folosi un instrument precum curl pentru a rula cereri web, dar orice instrument capabil să ruleze HTTP este util.
- **Testare unitară**: Este posibil să folosiți cadrul de testare preferat pentru a testa funcționalitățile atât ale serverului, cât și ale clientului.

### Folosind MCP Inspector

Am descris utilizarea acestui instrument în lecțiile anterioare, dar să vorbim puțin la nivel înalt. Este un instrument construit în Node.js și îl puteți folosi apelând executabilul `npx`, care va descărca și instala temporar instrumentul și se va curăța singur după ce va rula cererea dvs.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) vă ajută să:

- **Descoperiți capabilitățile serverului**: Detectați automat resursele disponibile, instrumentele și comenzile
- **Testați execuția instrumentelor**: Încercați diferiți parametri și vedeți răspunsurile în timp real
- **Vizualizați metadatele serverului**: Examinați informațiile serverului, schemele și configurațiile

O rulare tipică a instrumentului arată astfel:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Comanda de mai sus pornește un MCP împreună cu interfața sa vizuală și lansează o interfață web locală în browser. Vă puteți aștepta să vedeți un panou de control care afișează serverele MCP înregistrate, instrumentele, resursele și comenzile disponibile. Interfața vă permite să testați interactiv execuția instrumentelor, să inspectați metadatele serverului și să vizualizați răspunsurile în timp real, făcând mai ușoară validarea și depanarea implementărilor serverului MCP.

Iată cum poate arăta: ![Inspector](../../../../translated_images/ro/connect.141db0b2bd05f096.webp)

De asemenea, puteți rula acest instrument în modul CLI, caz în care adăugați atributul `--cli`. Iată un exemplu de rulare a instrumentului în modul "CLI" care listează toate instrumentele de pe server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Testare manuală

Pe lângă rularea instrumentului inspector pentru a testa capabilitățile serverului, o altă abordare similară este să rulați un client capabil să utilizeze HTTP, cum ar fi de exemplu curl.

Cu curl, puteți testa serverele MCP direct folosind cereri HTTP:

```bash
# Exemplu: Metadatele serverului de test
curl http://localhost:3000/v1/metadata

# Exemplu: Execută un instrument
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

După cum se vede din utilizarea curl prezentată mai sus, folosiți o cerere POST pentru a invoca un instrument utilizând o sarcină utilă care conține numele instrumentului și parametrii săi. Folosiți abordarea care vi se potrivește cel mai bine. Instrumentele CLI, în general, tind să fie mai rapide de folosit și se pretează la scripturi, ceea ce poate fi util într-un mediu CI/CD.

### Testare unitară

Creați teste unitare pentru instrumentele și resursele dvs. pentru a vă asigura că funcționează conform așteptărilor. Iată un exemplu de cod pentru testare.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Marchează întregul modul pentru teste asincrone
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Creează câteva unelte de testare
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testează fără parametrul cursor (omis)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testează cu cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testează cu cursor ca șir de caractere
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testează cu cursor șir gol
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Codul precedent face următoarele:

- Folosește cadrul pytest care vă permite să creați teste ca funcții și să folosiți expresii assert.
- Creează un server MCP cu două instrumente diferite.
- Folosește expresia `assert` pentru a verifica că anumite condiții sunt îndeplinite.

Consultați [fișierul complet aici](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Având acest fișier, puteți testa propriul server pentru a vă asigura că capabilitățile sunt create așa cum trebuie.

Toate SDK-urile majore au secțiuni similare de testare, astfel încât vă puteți adapta la mediul de rulare ales.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventuale neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->