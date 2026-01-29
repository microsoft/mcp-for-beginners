## Testovanie a ladenie

Predtým, než začnete testovať svoj MCP server, je dôležité porozumieť dostupným nástrojom a osvedčeným postupom pri ladení. Efektívne testovanie zabezpečí, že váš server bude fungovať podľa očakávaní a pomôže vám rýchlo identifikovať a vyriešiť problémy. Nasledujúca časť popisuje odporúčané prístupy na overenie implementácie MCP.

## Prehľad

Táto lekcia sa zaoberá výberom správneho prístupu k testovaniu a najefektívnejším testovacím nástrojom.

## Ciele učenia

Na konci tejto lekcie budete vedieť:

- Opísať rôzne prístupy k testovaniu.
- Použiť rôzne nástroje na efektívne testovanie vášho kódu.

## Testovanie MCP serverov

MCP poskytuje nástroje, ktoré vám pomôžu testovať a ladiť vaše servery:

- **MCP Inspector**: Nástroj príkazového riadku, ktorý môžete spustiť ako CLI nástroj alebo ako vizuálny nástroj.
- **Manuálne testovanie**: Môžete použiť nástroj ako curl na spúšťanie webových požiadaviek, ale postačí akýkoľvek nástroj schopný vykonávať HTTP požiadavky.
- **Jednotkové testovanie**: Je možné použiť váš obľúbený testovací framework na testovanie funkcií servera aj klienta.

### Použitie MCP Inspector

Použitie tohto nástroja sme popisovali v predchádzajúcich lekciách, ale poďme si to zhrnúť na vyššej úrovni. Je to nástroj postavený na Node.js a môžete ho použiť spustením `npx` príkazu, ktorý dočasne stiahne a nainštaluje nástroj a po dokončení spustenia vášho požiadavku sa sám vyčistí.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) vám pomáha:

- **Objaviť schopnosti servera**: Automaticky detekuje dostupné zdroje, nástroje a výzvy
- **Testovať spustenie nástrojov**: Vyskúšať rôzne parametre a vidieť odpovede v reálnom čase
- **Zobraziť metadata servera**: Preskúmať informácie o serveri, schémy a konfigurácie

Typické spustenie nástroja vyzerá takto:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Vyššie uvedený príkaz spustí MCP a jeho vizuálne rozhranie a otvorí lokálne webové rozhranie vo vašom prehliadači. Môžete očakávať zobrazenie dashboardu s registrovanými MCP servermi, ich dostupnými nástrojmi, zdrojmi a výzvami. Rozhranie umožňuje interaktívne testovať spustenie nástrojov, prezerať metadata servera a sledovať odpovede v reálnom čase, čo uľahčuje overenie a ladenie implementácií MCP servera.

Takto to môže vyzerať: ![Inspector](../../../../translated_images/sk/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

Tento nástroj môžete tiež spustiť v režime CLI, v tom prípade pridajte atribút `--cli`. Tu je príklad spustenia nástroja v režime "CLI", ktorý vypíše všetky nástroje na serveri:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuálne testovanie

Okrem spustenia nástroja inspector na testovanie schopností servera je ďalším podobným prístupom spustenie klienta schopného používať HTTP, napríklad curl.

Pomocou curl môžete priamo testovať MCP servery cez HTTP požiadavky:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Ako vidíte z vyššie uvedeného použitia curl, používate POST požiadavku na vyvolanie nástroja s payloadom obsahujúcim názov nástroja a jeho parametre. Použite prístup, ktorý vám najviac vyhovuje. CLI nástroje sú všeobecne rýchlejšie na použitie a dajú sa dobre skriptovať, čo môže byť užitočné v CI/CD prostredí.

### Jednotkové testovanie

Vytvorte jednotkové testy pre vaše nástroje a zdroje, aby ste zabezpečili, že fungujú podľa očakávaní. Tu je príklad testovacieho kódu.

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

Predchádzajúci kód robí nasledovné:

- Využíva framework pytest, ktorý umožňuje vytvárať testy ako funkcie a používať assert príkazy.
- Vytvára MCP Server s dvoma rôznymi nástrojmi.
- Používa príkaz `assert` na overenie, že sú splnené určité podmienky.

Pozrite si [celý súbor tu](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Na základe tohto súboru môžete otestovať svoj vlastný server, aby ste sa uistili, že schopnosti sú vytvorené tak, ako majú byť.

Všetky hlavné SDK majú podobné sekcie na testovanie, takže si ich môžete prispôsobiť podľa vášho runtime.

## Ukážky

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Dodatočné zdroje

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Čo nasleduje

- Ďalej: [Deployment](../09-deployment/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.