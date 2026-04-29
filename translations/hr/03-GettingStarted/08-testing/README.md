## Testiranje i otklanjanje pogrešaka

Prije nego što započnete s testiranjem vašeg MCP poslužitelja, važno je razumjeti dostupne alate i najbolje prakse za otklanjanje pogrešaka. Učinkovito testiranje osigurava da se vaš poslužitelj ponaša kako je očekivano i pomaže vam brzo identificirati i riješiti probleme. Sljedeći odjeljak prikazuje preporučene pristupe za provjeru vaše MCP implementacije.

## Pregled

Ova lekcija obuhvaća kako odabrati pravi pristup testiranju i najučinkovitiji alat za testiranje.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:

- Opisati različite pristupe testiranju.
- Koristiti različite alate za učinkovito testiranje svojeg koda.

## Testiranje MCP poslužitelja

MCP pruža alate koji vam pomažu u testiranju i otklanjanju pogrešaka na vašim poslužiteljima:

- **MCP Inspector**: Alat za naredbeni redak koji se može koristiti i kao CLI alat i kao vizualni alat.
- **Ručni testovi**: Možete koristiti alat poput curl za pokretanje web zahtjeva, ali bilo koji alat sposoban za pokretanje HTTP zahtjeva će odgovarati.
- **Jedinično testiranje**: Moguće je koristiti odabrani okvir za testiranje za provjeru značajki poslužitelja i klijenta.

### Korištenje MCP Inspectora

Opisali smo uporabu ovog alata u prethodnim lekcijama, no razgovarajmo o njemu ukratko na višoj razini. To je alat izgrađen u Node.js i možete ga koristiti pozivanjem izvršnog `npx` programa koji će privremeno preuzeti i instalirati alat, a zatim ga očistiti nakon izvršenja vašeg zahtjeva.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) vam pomaže:

- **Otkriti mogućnosti poslužitelja**: Automatski otkriti dostupne resurse, alate i upite
- **Testirati izvođenje alata**: Isprobati različite parametre i vidjeti odgovore u stvarnom vremenu
- **Pogledati metapodatke poslužitelja**: Pregledati informacije o poslužitelju, sheme i konfiguracije

Tipičan pokret alata izgleda ovako:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Gornja naredba pokreće MCP i njegov vizualni sučelje te otvara lokalno web sučelje u vašem pregledniku. Možete očekivati nadzornu ploču koja prikazuje vaše registrirane MCP poslužitelje, njihove dostupne alate, resurse i upite. Sučelje vam omogućuje interaktivno testiranje izvršavanja alata, pregled metapodataka poslužitelja i gledanje odgovora u stvarnom vremenu, što olakšava provjeru i otklanjanje pogrešaka u implementacijama MCP poslužitelja.

Evo kako to može izgledati: ![Inspector](../../../../translated_images/hr/connect.141db0b2bd05f096.webp)

Također možete pokrenuti ovaj alat u CLI načinu, pri čemu dodate atribut `--cli`. Evo primjera pokretanja alata u "CLI" načinu koji navodi sve alate na poslužitelju:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Ručno testiranje

Osim korištenja alata inspector za ispitivanje mogućnosti poslužitelja, sličan pristup je korištenje klijenta koji može koristiti HTTP, poput curl.

Pomoću curl alata možete direktno testirati MCP poslužitelje pomoću HTTP zahtjeva:

```bash
# Primjer: Metapodaci testnog poslužitelja
curl http://localhost:3000/v1/metadata

# Primjer: Izvrši alat
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Kao što vidite u gornjoj upotrebi curl alata, koristite POST zahtjev za pozivanje alata koristeći payload koji se sastoji od imena alata i njegovih parametara. Koristite pristup koji vam najviše odgovara. CLI alati općenito su brži za korištenje i pogodni za skriptiranje što može biti korisno u CI/CD okruženju.

### Jedinično testiranje

Napravite jedinične testove za svoje alate i resurse kako biste bili sigurni da rade kako se očekuje. Evo primjera koda za testiranje.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Označi cijeli modul za asinhrone testove
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Napravi nekoliko testnih alata
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

        # Testiraj s kursorem kao stringom
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testiraj s praznim stringom kao kursorem
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Gornji kod radi sljedeće:

- Koristi pytest okvir koji vam omogućava kreiranje testova kao funkcija i korištenje assert naredbi.
- Stvara MCP poslužitelj sa dva različita alata.
- Koristi `assert` izjavu za provjeru ispunjenosti određenih uvjeta.

Pogledajte [cijelu datoteku ovdje](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Na temelju navedene datoteke, možete testirati svoj vlastiti poslužitelj da biste osigurali da su mogućnosti kreirane kako treba.

Svi glavni SDK-ovi imaju slične odjeljke za testiranje pa se možete prilagoditi svom odabranom runtimeu.

## Primjeri

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Dodatni resursi

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Što slijedi

- Sljedeće: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati općeprihvaćenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakve nesporazume ili krive interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->