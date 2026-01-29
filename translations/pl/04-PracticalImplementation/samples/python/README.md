# Model Context Protocol (MCP) Implementacja w Pythonie

To repozytorium zawiera implementację Model Context Protocol (MCP) w Pythonie, pokazującą, jak stworzyć zarówno serwer, jak i klienta komunikujących się za pomocą standardu MCP.

## Przegląd

Implementacja MCP składa się z dwóch głównych komponentów:

1. **MCP Server (`server.py`)** – Serwer udostępniający:
   - **Narzędzia**: Funkcje, które można wywoływać zdalnie
   - **Zasoby**: Dane, które można pobierać
   - **Prompty**: Szablony do generowania promptów dla modeli językowych

2. **MCP Client (`client.py`)** – Aplikacja kliencka łącząca się z serwerem i korzystająca z jego funkcji

## Funkcje

Ta implementacja demonstruje kilka kluczowych funkcji MCP:

### Narzędzia
- `completion` – Generuje uzupełnienia tekstu z modeli AI (symulowane)
- `add` – Prosty kalkulator dodający dwie liczby

### Zasoby
- `models://` – Zwraca informacje o dostępnych modelach AI
- `greeting://{name}` – Zwraca spersonalizowane powitanie dla podanego imienia

### Prompty
- `review_code` – Generuje prompt do przeglądu kodu

## Instalacja

Aby korzystać z tej implementacji MCP, zainstaluj wymagane pakiety:

```powershell
pip install mcp-server mcp-client
```

## Uruchamianie Serwera i Klienta

### Uruchamianie Serwera

Uruchom serwer w jednym oknie terminala:

```powershell
python server.py
```

Serwer można też uruchomić w trybie deweloperskim za pomocą MCP CLI:

```powershell
mcp dev server.py
```

Lub zainstalować w Claude Desktop (jeśli dostępne):

```powershell
mcp install server.py
```

### Uruchamianie Klienta

Uruchom klienta w innym oknie terminala:

```powershell
python client.py
```

To połączy się z serwerem i pokaże wszystkie dostępne funkcje.

### Użycie Klienta

Klient (`client.py`) demonstruje wszystkie możliwości MCP:

```powershell
python client.py
```

To połączy się z serwerem i przetestuje wszystkie funkcje, w tym narzędzia, zasoby i prompty. Wynik pokaże:

1. Wynik działania kalkulatora (5 + 7 = 12)
2. Odpowiedź narzędzia completion na pytanie "What is the meaning of life?"
3. Listę dostępnych modeli AI
4. Spersonalizowane powitanie dla "MCP Explorer"
5. Szablon promptu do przeglądu kodu

## Szczegóły Implementacji

Serwer jest zaimplementowany przy użyciu API `FastMCP`, które oferuje wysokopoziomowe abstrakcje do definiowania usług MCP. Oto uproszczony przykład definiowania narzędzi:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Klient korzysta z biblioteki MCP client, aby połączyć się i wywołać serwer:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Dowiedz się więcej

Więcej informacji o MCP znajdziesz na: https://modelcontextprotocol.io/

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.