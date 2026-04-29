## Testovanie a ladenie

Pred začatím testovania vášho MCP servera je dôležité pochopiť dostupné nástroje a najlepšie postupy pre ladenie. Efektívne testovanie zabezpečuje, že váš server sa správa očakávaným spôsobom a pomáha vám rýchlo identifikovať a vyriešiť problémy. Nasledujúca časť popisuje odporúčané prístupy na overenie implementácie MCP.

## Prehľad

Táto lekcia pokrýva, ako vybrať správny prístup k testovaniu a najefektívnejší nástroj na testovanie.

## Ciele učenia

Na konci tejto lekcie budete vedieť:

- Opísať rôzne prístupy k testovaniu.
- Použiť rôzne nástroje na efektívne testovanie vášho kódu.


## Testovanie MCP serverov

MCP poskytuje nástroje na pomoc s testovaním a ladením vašich serverov:

- **MCP Inspector**: Nástroj príkazového riadku, ktorý možno spustiť ako CLI nástroj aj ako vizuálny nástroj.
- **Manuálne testovanie**: Môžete použiť nástroj ako curl na vykonávanie webových požiadaviek, ale akýkoľvek nástroj schopný spustiť HTTP bude vyhovujúci.
- **Jednotkové testovanie**: Je možné použiť preferovaný testovací rámec na testovanie funkcií servera aj klienta.

### Použitie MCP Inspector

Použitie tohto nástroja sme popísali v predchádzajúcich lekciách, ale poďme o ňom hovoriť aj vo všeobecnosti. Je to nástroj postavený na Node.js a môžete ho použiť zavolaním spustiteľného súboru `npx`, ktorý si nástroj dočasne stiahne a nainštaluje a po dokončení behu požiadavky sa sám vyčistí.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) vám pomáha:

- **Objavovanie schopností servera**: Automaticky zistí dostupné zdroje, nástroje a výzvy
- **Testovanie spustenia nástrojov**: Vyskúšajte rôzne parametre a sledujte odpovede v reálnom čase
- **Zobrazenie metadát servera**: Preskúmajte informácie o serveri, schémy a konfigurácie

Typické spustenie tohto nástroja vyzerá takto:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Príkaz vyššie spustí MCP a jeho vizuálne rozhranie a otvorí lokálne webové rozhranie vo vašom prehliadači. Môžete očakávať zobrazenie dashboardu, ktorý zobrazuje zaregistrované MCP servery, ich dostupné nástroje, zdroje a výzvy. Rozhranie vám umožní interaktívne testovať spustenie nástrojov, kontrolovať metadáta servera a vidieť odpovede v reálnom čase, čo uľahčuje overovanie a ladenie implementácií vášho MCP servera.

Takto to môže vyzerať: ![Inspector](../../../../translated_images/sk/connect.141db0b2bd05f096.webp)

Tento nástroj môžete spustiť aj v režime CLI, kde pridáte atribút `--cli`. Tu je príklad spustenia nástroja v „CLI“ režime, ktorý vypíše všetky nástroje na serveri:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuálne testovanie

Okrem spustenia inspector nástroja na testovanie schopností servera, ďalším podobným prístupom je spustenie klienta schopného používať HTTP, napríklad curl.

S curl môžete testovať MCP servery priamo pomocou HTTP požiadaviek:

```bash
# Príklad: Metadáta testovacieho servera
curl http://localhost:3000/v1/metadata

# Príklad: Spustiť nástroj
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Ako vidíte z vyššie uvedeného použitia curl, použijete POST požiadavku na vyvolanie nástroja so zaťažením pozostávajúcim z názvu nástroja a jeho parametrov. Použite prístup, ktorý vám najviac vyhovuje. CLI nástroje sú všeobecne rýchlejšie na použitie a dobre sa hodia na skriptovanie, čo môže byť užitočné v prostredí CI/CD.

### Jednotkové testovanie

Vytvorte jednotkové testy pre vaše nástroje a zdroje, aby ste zabezpečili, že fungujú podľa očakávaní. Tu je príklad testovacieho kódu.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Označiť celý modul pre asynchrónne testy
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Vytvoriť zopár testovacích nástrojov
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testovať bez parametra kurzora (vynechané)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testovať s kurzorom=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testovať s kurzorom ako reťazec
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testovať s prázdnym reťazcom kurzora
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Predchádzajúci kód robí nasledovné:

- Využíva testovací rámec pytest, ktorý vám umožňuje vytvárať testy ako funkcie a používať assert príkazy.
- Vytvára MCP server so dvoma rôznymi nástrojmi.
- Používa príkaz `assert` na overenie, či sú splnené určité podmienky.

Pozrite si [plný súbor tu](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Na základe vyššie uvedeného súboru môžete otestovať vlastný server, aby ste sa uistili, že schopnosti sú vytvorené tak, ako majú byť.

Všetky hlavné SDK majú podobné sekcie na testovanie, takže ich môžete prispôsobiť vášmu zvolenému runtime.

## Ukážky

- [Java kalkulačka](../samples/java/calculator/README.md)
- [.Net kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulačka](../samples/javascript/README.md)
- [TypeScript kalkulačka](../samples/typescript/README.md)
- [Python kalkulačka](../../../../03-GettingStarted/samples/python) 

## Ďalšie zdroje

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Čo nasleduje

- Ďalej: [Nasadenie](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vzniknuté použitím tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->