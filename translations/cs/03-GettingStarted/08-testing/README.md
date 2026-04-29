## Testování a ladění

Než začnete testovat svůj MCP server, je důležité porozumět dostupným nástrojům a osvědčeným postupům pro ladění. Efektivní testování zajistí, že váš server bude fungovat podle očekávání, a pomůže vám rychle identifikovat a vyřešit problémy. Následující část uvádí doporučené přístupy k ověřování vaší implementace MCP.

## Přehled

Tato lekce pokrývá, jak vybrat správný přístup k testování a nejefektivnější testovací nástroj.

## Výukové cíle

Na konci této lekce budete schopni:

- Popsat různé přístupy k testování.
- Použít různé nástroje k efektivnímu testování vašeho kódu.


## Testování MCP serverů

MCP poskytuje nástroje, které vám pomohou testovat a ladit vaše servery:

- **MCP Inspector**: Nástroj příkazové řádky, který lze spustit jak jako CLI nástroj, tak i jako vizuální nástroj.
- **Manuální testování**: Můžete použít nástroj jako curl pro odesílání webových požadavků, ale jakýkoliv nástroj schopný provozovat HTTP bude stačit.
- **Unit testing**: Je možné použít váš preferovaný testovací framework k otestování funkcí jak serveru, tak klienta.

### Použití MCP Inspector

Použití tohoto nástroje jsme popsali v předchozích lekcích, ale proberme je trochu obecně. Je to nástroj postavený na Node.js a použijete ho zavoláním spustitelného souboru `npx`, který si nástroj dočasně stáhne a nainstaluje a po dokončení vašeho požadavku se sám vyčistí.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) vám pomáhá:

- **Objevit schopnosti serveru**: Automaticky detekuje dostupné zdroje, nástroje a výzvy
- **Testovat spuštění nástrojů**: Vyzkoušet různé parametry a sledovat odpovědi v reálném čase
- **Zobrazit metadata serveru**: Prohlédnout informace o serveru, schémata a konfigurace

Typické spuštění nástroje vypadá takto:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Výše uvedený příkaz spustí MCP a jeho vizuální rozhraní a otevře lokální webové rozhraní ve vašem prohlížeči. Můžete očekávat, že uvidíte dashboard zobrazující vaše registrované MCP servery, jejich dostupné nástroje, zdroje a výzvy. Rozhraní umožňuje interaktivně testovat spuštění nástrojů, prohlížet metadata serveru a sledovat odpovědi v reálném čase, což usnadňuje ověřování a ladění implementací MCP serveru.

Takto může vypadat: ![Inspector](../../../../translated_images/cs/connect.141db0b2bd05f096.webp)

Tento nástroj můžete také spustit v CLI režimu, kdy přidáte atribut `--cli`. Zde je příklad spuštění nástroje v "CLI" režimu, který vypíše všechny nástroje na serveru:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuální testování

Kromě používání inspektoru k testování schopností serveru je další podobný přístup spustit klienta schopného používat HTTP, například curl.

Pomocí curl můžete přímo testovat MCP servery pomocí HTTP požadavků:

```bash
# Příklad: Metadata testovacího serveru
curl http://localhost:3000/v1/metadata

# Příklad: Spustit nástroj
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Jak vidíte z výše uvedeného použití curl, používáte POST požadavek k volání nástroje s payloadem obsahujícím jméno nástroje a jeho parametry. Vyberte přístup, který vám nejlépe vyhovuje. CLI nástroje jsou obecně rychlejší na použití a dobře se skriptují, což může být užitečné v CI/CD prostředí.

### Unit testing

Vytvořte jednotkové testy pro vaše nástroje a zdroje, abyste zajistili, že fungují podle očekávání. Zde je ukázka testovacího kódu.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Označit celý modul pro asynchronní testy
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Vytvořit pár testovacích nástrojů
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test bez parametru cursor (vynecháno)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test s cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test s cursor jako řetězcem
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test s prázdným řetězcem jako cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Výše uvedený kód:

- Využívá framework pytest, který umožňuje vytvářet testy jako funkce a používat assert příkazy.
- Vytváří MCP server se dvěma různými nástroji.
- Používá příkaz `assert` k ověření, že jsou splněny určité podmínky.

Podívejte se na [celý soubor zde](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Na základě tohoto souboru můžete otestovat svůj vlastní server, abyste zajistili, že schopnosti jsou vytvořeny, jak mají být.

Všechny hlavní SDK mají podobné testovací sekce, takže je můžete přizpůsobit vámi zvolenému runtime.

## Ukázky

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Další zdroje

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Co dál

- Další: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí služby AI překladatele [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakákoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->