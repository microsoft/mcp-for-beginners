## Testiranje in odpravljanje napak

Preden začnete testirati svoj MCP strežnik, je pomembno razumeti razpoložljiva orodja in najboljše prakse za odpravljanje napak. Učinkovito testiranje zagotavlja, da se vaš strežnik obnaša kot pričakovano in vam pomaga hitro prepoznati ter odpraviti težave. Naslednji odsek opisuje priporočene pristope za preverjanje vaše implementacije MCP.

## Pregled

Ta lekcija zajema, kako izbrati pravi pristop k testiranju in najučinkovitejše orodje za testiranje.

## Cilji učenja

Ob koncu te lekcije boste lahko:

- Opisali različne pristope za testiranje.
- Uporabili različna orodja za učinkovito testiranje vaše kode.


## Testiranje MCP strežnikov

MCP vam nudi orodja, ki vam pomagajo testirati in odpravljati napake na vaših strežnikih:

- **MCP Inspector**: Orodje ukazne vrstice, ki ga lahko uporabljate tako v CLI načinu kot tudi s vizualnim vmesnikom.
- **Ročno testiranje**: Lahko uporabite orodje, kot je curl, za izvajanje spletnih zahtevkov, prav tako pa ustrezno orodje, ki zmore izvajati HTTP zahteve.
- **Enotno testiranje**: Možno je uporabiti vašo priljubljeno testno ogrodje za testiranje funkcionalnosti tako strežnika kot tudi odjemalca.

### Uporaba MCP Inspector

Uporabo tega orodja smo opisali v prejšnjih lekcijah, vendar pa si poglejmo še na splošno. Gre za orodje izdelano v Node.js, ki ga lahko uporabite z zagonom izvršljive datoteke `npx`, ki začasno prenese in namesti orodje ter se po koncu izvajanja vašega zahtevka samodejno odstrani.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) vam pomaga:

- **Odkriti zmogljivosti strežnika**: Samodejno zaznajte razpoložljive vire, orodja in pozive
- **Testirati izvajanje orodij**: Preizkusite različne parametre in si oglejte odzive v realnem času
- **Pogledati metapodatke strežnika**: Preučite informacije o strežniku, sheme in nastavitve

Tipični zagon orodja izgleda takole:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Zgornji ukaz zažene MCP in njegov vizualni vmesnik ter odpre lokalni spletni vmesnik v vašem brskalniku. Pričakujete lahko nadzorno ploščo, ki prikazuje vaše registrirane MCP strežnike, njihova razpoložljiva orodja, vire in pozive. Vmesnik omogoča interaktivno testiranje izvajanja orodij, pregledovanje metapodatkov strežnika in ogled odzivov v realnem času, kar olajša preverjanje in odpravljanje napak v implementacijah MCP strežnika.

Tako lahko izgleda: ![Inspector](../../../../translated_images/sl/connect.141db0b2bd05f096.webp)

Orodje lahko zaženete tudi v CLI načinu, pri čemer dodate atribut `--cli`. Tukaj je primer zagona orodja v "CLI" načinu, ki izpiše vsa orodja na strežniku:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Ročno testiranje

Poleg zagona orodja inspector za testiranje zmogljivosti strežnika je še en podoben pristop zagon odjemalca, ki zna uporabljati HTTP, kot na primer curl.

Z orodjem curl lahko testirate MCP strežnike neposredno z HTTP zahtevki:

```bash
# Primer: Preizkusi strežniške metapodatke
curl http://localhost:3000/v1/metadata

# Primer: Izvedi orodje
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Kot vidite zgoraj, s curl uporabite POST zahtevek za klic orodja z uporabo vsebine, ki vsebuje ime orodja in njegove parametre. Uporabite pristop, ki vam najbolj ustreza. CLI orodja so na splošno hitrejša za uporabo in se zlahka avtomatizirajo, kar je lahko koristno v CI/CD okolju.

### Enotno testiranje

Ustvarite enotne teste za vaša orodja in vire, da zagotovite njihovo pravilno delovanje. Tukaj je nekaj primerov testne kode.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Označi celoten modul za asinhrone teste
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Ustvari nekaj testnih orodij
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test brez parametra cursor (izpuščeno)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test z cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test z cursor kot niz
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test z praznim nizom cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Prej prikazana koda naredi naslednje:

- Uporablja pytest ogrodje, ki vam omogoča ustvarjanje testov kot funkcij in uporabo assert trditev.
- Ustvari MCP strežnik z dvema različnima orodjema.
- Uporablja `assert` izjavo za preverjanje, da so izpolnjeni določeni pogoji.

Oglejte si [celotno datoteko tukaj](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Glede na zgornjo datoteko lahko testirate svoj strežnik, da zagotovite, da so zmogljivosti ustvarjene takšne, kot naj bi bile.

Vsa glavna SDK imajo podobne testne oddelke, tako da se lahko prilagodite svojemu izbranemu runtime okolju.

## Primeri

- [Java kalkulator](../samples/java/calculator/README.md)
- [.Net kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulator](../samples/javascript/README.md)
- [TypeScript kalkulator](../samples/typescript/README.md)
- [Python kalkulator](../../../../03-GettingStarted/samples/python)

## Dodatni viri

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Kaj sledi

- Naslednje: [Implementacija](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije je priporočljiv strokovni človeški prevod. Nismo odgovorni za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->