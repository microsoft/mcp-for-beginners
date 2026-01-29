## Testowanie i debugowanie

Zanim zaczniesz testować swój serwer MCP, ważne jest, aby zrozumieć dostępne narzędzia i najlepsze praktyki debugowania. Skuteczne testowanie zapewnia, że serwer działa zgodnie z oczekiwaniami i pomaga szybko zidentyfikować oraz rozwiązać problemy. Poniższa sekcja przedstawia zalecane podejścia do weryfikacji implementacji MCP.

## Przegląd

Ta lekcja omawia, jak wybrać odpowiednie podejście do testowania oraz najskuteczniejsze narzędzie do testów.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Opisać różne podejścia do testowania.
- Korzystać z różnych narzędzi do efektywnego testowania kodu.

## Testowanie serwerów MCP

MCP udostępnia narzędzia, które pomogą Ci testować i debugować serwery:

- **MCP Inspector**: narzędzie wiersza poleceń, które można uruchomić zarówno jako CLI, jak i w wersji wizualnej.
- **Testowanie manualne**: możesz użyć narzędzia takiego jak curl do wykonywania zapytań webowych, ale każde narzędzie obsługujące HTTP będzie odpowiednie.
- **Testy jednostkowe**: możesz użyć swojego ulubionego frameworka testowego do testowania funkcji zarówno serwera, jak i klienta.

### Korzystanie z MCP Inspector

Opisaliśmy użycie tego narzędzia w poprzednich lekcjach, ale omówmy je teraz na poziomie ogólnym. To narzędzie napisane w Node.js, które możesz uruchomić za pomocą `npx`. Polecenie to tymczasowo pobierze i zainstaluje narzędzie, a po wykonaniu żądania samo się posprząta.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) pomaga:

- **Odkrywać możliwości serwera**: automatycznie wykrywa dostępne zasoby, narzędzia i promptsy
- **Testować wykonanie narzędzi**: wypróbuj różne parametry i zobacz odpowiedzi w czasie rzeczywistym
- **Przeglądać metadane serwera**: sprawdź informacje o serwerze, schematy i konfiguracje

Typowe uruchomienie narzędzia wygląda tak:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Powyższe polecenie uruchamia MCP wraz z interfejsem wizualnym i otwiera lokalny interfejs webowy w przeglądarce. Możesz spodziewać się pulpitu nawigacyjnego pokazującego zarejestrowane serwery MCP, dostępne narzędzia, zasoby i promptsy. Interfejs pozwala interaktywnie testować wykonanie narzędzi, przeglądać metadane serwera oraz obserwować odpowiedzi w czasie rzeczywistym, co ułatwia weryfikację i debugowanie implementacji serwera MCP.

Tak to może wyglądać: ![Inspector](../../../../translated_images/pl/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

Możesz też uruchomić to narzędzie w trybie CLI, dodając atrybut `--cli`. Oto przykład uruchomienia narzędzia w trybie "CLI", który wyświetla listę wszystkich narzędzi na serwerze:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Testowanie manualne

Poza uruchamianiem narzędzia inspector do testowania możliwości serwera, innym podobnym podejściem jest użycie klienta obsługującego HTTP, na przykład curl.

Za pomocą curl możesz testować serwery MCP bezpośrednio, wysyłając zapytania HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Jak widać z powyższego przykładu użycia curl, korzystasz z zapytania POST, aby wywołać narzędzie, przesyłając w ładunku nazwę narzędzia i jego parametry. Wybierz podejście, które najbardziej Ci odpowiada. Narzędzia CLI zazwyczaj są szybsze w użyciu i łatwo je zautomatyzować, co może być przydatne w środowisku CI/CD.

### Testy jednostkowe

Twórz testy jednostkowe dla swoich narzędzi i zasobów, aby upewnić się, że działają zgodnie z oczekiwaniami. Oto przykładowy kod testowy.

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

Powyższy kod robi następujące rzeczy:

- Wykorzystuje framework pytest, który pozwala tworzyć testy jako funkcje i używać instrukcji assert.
- Tworzy serwer MCP z dwoma różnymi narzędziami.
- Używa instrukcji `assert`, aby sprawdzić, czy spełnione są określone warunki.

Zobacz [pełny plik tutaj](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Na podstawie powyższego pliku możesz testować własny serwer, aby upewnić się, że możliwości są tworzone zgodnie z oczekiwaniami.

Wszystkie główne SDK mają podobne sekcje testowe, więc możesz dostosować je do wybranego środowiska uruchomieniowego.

## Przykłady

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Dodatkowe zasoby

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Co dalej

- Następny: [Deployment](../09-deployment/README.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.