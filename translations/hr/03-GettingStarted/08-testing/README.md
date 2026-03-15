## Testiranje i ispravljanje pogrešaka

Prije nego što započnete s testiranjem vašeg MCP poslužitelja, važno je razumjeti dostupne alate i najbolje prakse za ispravljanje pogrešaka. Učinkovito testiranje osigurava da se vaš poslužitelj ponaša prema očekivanjima i pomaže vam brzo identificirati i riješiti probleme. Sljedeći odjeljak opisuje preporučene pristupe za provjeru vaše MCP implementacije.

## Pregled

Ova lekcija obuhvaća kako odabrati pravi pristup testiranju i najučinkovitiji alat za testiranje.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Opisati razne pristupe za testiranje.
- Koristiti različite alate za učinkovito testiranje vašeg koda.


## Testiranje MCP poslužitelja

MCP pruža alate koji vam pomažu pri testiranju i ispravljanju pogrešaka vaših poslužitelja:

- **MCP Inspector**: Alat naredbenog retka koji se može pokrenuti i kao CLI alat i kao vizualni alat.
- **Ručno testiranje**: Možete koristiti alat poput curl za izvršavanje web zahtjeva, ali svaki alat sposoban za HTTP će biti prikladan.
- **Testiranje jedinica (unit testing)**: Moguće je koristiti vaš omiljeni okvir za testiranje da testirate značajke i poslužitelja i klijenta.

### Korištenje MCP Inspectora

Opisali smo upotrebu ovog alata u prethodnim lekcijama, ali razgovarajmo malo o njemu na visokou razini. To je alat izgrađen u Node.js i možete ga koristiti pozivanjem izvršne datoteke `npx` koja će privremeno preuzeti i instalirati sam alat te će se očistiti nakon što izvrši vaš zahtjev.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) pomaže vam:

- **Otkriti mogućnosti poslužitelja**: Automatski otkriva dostupne resurse, alate i upite
- **Testirati izvršenje alata**: Isprobajte različite parametre i vidite odgovore u stvarnom vremenu
- **Pregledati metapodatke poslužitelja**: Istražite informacije o poslužitelju, sheme i konfiguracije

Tipično pokretanje alata izgleda ovako:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Gornja naredba pokreće MCP i njegovo vizualno sučelje te pokreće lokalno web sučelje u vašem pregledniku. Možete očekivati da će se prikazati nadzorna ploča koja prikazuje vaše registrirane MCP poslužitelje, njihove dostupne alate, resurse i upite. Sučelje omogućuje interaktivno testiranje izvršenja alata, pregled metapodataka poslužitelja i prikaz odgovora u stvarnom vremenu, što olakšava provjeru i ispravljanje pogrešaka implementacija vašeg MCP poslužitelja.

Evo kako to može izgledati: ![Inspector](../../../../translated_images/hr/connect.141db0b2bd05f096.webp)

Također možete pokrenuti ovaj alat u CLI načinu dodavanjem atributa `--cli`. Evo primjera pokretanja alata u "CLI" načinu koji navodi sve alate na poslužitelju:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Ručno testiranje

Osim pokretanja inspectora za testiranje mogućnosti poslužitelja, drugi sličan pristup je pokretanje klijenta sposobanog za korištenje HTTP-a, kao što je na primjer curl.

Pomoću curl-a možete testirati MCP poslužitelje direktno koristeći HTTP zahtjeve:

```bash
# Primjer: Metadata testnog poslužitelja
curl http://localhost:3000/v1/metadata

# Primjer: Pokretanje alata
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Kao što možete vidjeti iz gornje upotrebe curl-a, koristite POST zahtjev za pozivanje alata s podacima koji se sastoje od imena alata i njegovih parametara. Koristite pristup koji vam najviše odgovara. CLI alati općenito su brži za korištenje i omogućuju automatizaciju, što može biti korisno u CI/CD okruženju.

### Testiranje jedinica (Unit Testing)

Kreirajte testove za vaše alate i resurse kako biste osigurali da rade prema očekivanjima. Evo primjera koda za testiranje.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Oznaci cijeli modul za asinhrone testove
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Kreiraj nekoliko testnih alata
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testiraj bez parametra kursora (izostavljeno)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testiraj s cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testiraj s kursorom kao string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testiraj s praznim stringom kursora
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Gornji kod radi sljedeće:

- Koristi pytest okvir koji vam omogućuje kreiranje testova kao funkcija i korištenje assert izraza.
- Kreira MCP poslužitelj s dva različita alata.
- Koristi `assert` izraz za provjeru ispunjenosti određenih uvjeta.

Pogledajte [cijelu datoteku ovdje](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Na temelju gornje datoteke možete testirati vlastiti poslužitelj kako biste osigurali da su mogućnosti postavljene onako kako trebaju biti.

Svi glavni SDK-i imaju slične odjeljke za testiranje pa se možete prilagoditi odabranom runtimeu.

## Primjeri

- [Java kalkulator](../samples/java/calculator/README.md)
- [.Net kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulator](../samples/javascript/README.md)
- [TypeScript kalkulator](../samples/typescript/README.md)
- [Python kalkulator](../../../../03-GettingStarted/samples/python)

## Dodatni resursi

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Što slijedi

- Dalje: [Implementacija](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI prevodilačke usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->