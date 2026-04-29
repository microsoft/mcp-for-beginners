## Testowanie i debugowanie

Zanim zaczniesz testować swój serwer MCP, ważne jest, aby zrozumieć dostępne narzędzia i najlepsze praktyki dotyczące debugowania. Skuteczne testowanie zapewnia, że serwer działa zgodnie z oczekiwaniami i pomaga szybko wykrywać oraz rozwiązywać problemy. Poniższa sekcja przedstawia zalecane podejścia do weryfikacji implementacji MCP.

## Przegląd

Ta lekcja omawia, jak wybrać odpowiednie podejście do testowania oraz najskuteczniejsze narzędzie do testów.

## Cele nauki

Na koniec tej lekcji będziesz potrafił:

- Opisać różne podejścia do testowania.
- Wykorzystać różne narzędzia do skutecznego testowania swojego kodu.

## Testowanie serwerów MCP

MCP dostarcza narzędzia pomagające w testowaniu i debugowaniu serwerów:

- **MCP Inspector**: Narzędzie wiersza poleceń, które można uruchomić zarówno jako narzędzie CLI, jak i wizualne.
- **Testowanie ręczne**: Możesz użyć narzędzia takiego jak curl do wykonywania zapytań sieciowych, ale każde narzędzie obsługujące HTTP będzie odpowiednie.
- **Testowanie jednostkowe**: Możliwe jest użycie preferowanego frameworka testowania do testowania funkcji zarówno serwera, jak i klienta.

### Używanie MCP Inspector

Opisaliśmy użycie tego narzędzia w poprzednich lekcjach, ale omówmy je teraz na poziomie ogólnym. To narzędzie zbudowane w Node.js, które możesz uruchomić przez wywołanie wykonywalnego pliku `npx`. Pobrałoby ono i tymczasowo zainstalowało narzędzie, a po zakończeniu wykonania Twojego zapytania samo się wyczyści.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) pomaga Ci:

- **Odkrywać możliwości serwera**: Automatycznie wykrywa dostępne zasoby, narzędzia i podpowiedzi
- **Testować działanie narzędzi**: Próbować różne parametry i oglądać odpowiedzi w czasie rzeczywistym
- **Przeglądać metadane serwera**: Badać informacje o serwerze, schematach oraz konfiguracjach

Typowe uruchomienie narzędzia wygląda tak:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Powyższa komenda uruchamia MCP z jego interfejsem wizualnym i otwiera lokalny interfejs webowy w Twojej przeglądarce. Możesz spodziewać się kokpitu pokazującego zarejestrowane serwery MCP, dostępne narzędzia, zasoby i podpowiedzi. Interfejs umożliwia interaktywne testowanie działania narzędzi, przeglądanie metadanych serwera oraz oglądanie odpowiedzi w czasie rzeczywistym, co ułatwia weryfikację i debugowanie implementacji serwera MCP.

Tak to może wyglądać: ![Inspector](../../../../translated_images/pl/connect.141db0b2bd05f096.webp)

Możesz również uruchomić to narzędzie w trybie CLI, dodając atrybut `--cli`. Oto przykład uruchomienia narzędzia w trybie "CLI", które wypisuje wszystkie narzędzia na serwerze:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Testowanie ręczne

Poza uruchamianiem narzędzia inspector do testowania możliwości serwera, podobnym podejściem jest użycie klienta zdolnego do komunikacji HTTP, na przykład curl.

Za pomocą curl możesz testować serwery MCP bezpośrednio przy użyciu zapytań HTTP:

```bash
# Przykład: Metadane serwera testowego
curl http://localhost:3000/v1/metadata

# Przykład: Uruchom narzędzie
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Jak widzisz z powyższego przykładu użycia curl, wykorzystujesz zapytanie POST do wywołania narzędzia, wysyłając ładunek zawierający nazwę narzędzia oraz jego parametry. Wybierz podejście, które najlepiej Ci odpowiada. Narzędzia CLI zazwyczaj działają szybciej i łatwiej je skryptować, co może być przydatne w środowisku CI/CD.

### Testowanie jednostkowe

Twórz testy jednostkowe dla swoich narzędzi i zasobów, aby upewnić się, że działają zgodnie z oczekiwaniami. Oto przykładowy kod testowy:

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Oznacz cały moduł do testów asynchronicznych
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Utwórz kilka narzędzi testowych
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test bez parametru cursor (pominięty)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test z cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test z cursor jako string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test z pustym stringiem jako cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Powyższy kod wykonuje następujące czynności:

- Wykorzystuje framework pytest, który pozwala tworzyć testy jako funkcje i używać instrukcji assert.
- Tworzy serwer MCP z dwoma różnymi narzędziami.
- Używa instrukcji `assert` do sprawdzania, czy określone warunki są spełnione.

Zapoznaj się z [pełnym plikiem tutaj](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dysponując powyższym plikiem, możesz przetestować swój własny serwer, aby upewnić się, że możliwości są tworzone prawidłowo.

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

- Dalej: [Wdrożenie](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego, ludzkiego tłumaczenia. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->