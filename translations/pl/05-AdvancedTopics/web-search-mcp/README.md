# Lekcja: Budowa serwera MCP do wyszukiwania w sieci

Ten rozdział pokazuje, jak zbudować praktycznego agenta AI, który integruje się z zewnętrznymi API, obsługuje różnorodne typy danych, zarządza błędami i koordynuje wiele narzędzi — wszystko w formacie gotowym do produkcji. Zobaczysz:

- **Integrację z zewnętrznymi API wymagającymi uwierzytelniania**
- **Obsługę różnych typów danych z wielu punktów końcowych**
- **Solidne strategie obsługi błędów i logowania**
- **Orkiestrację wielu narzędzi w jednym serwerze**

Na koniec zdobędziesz praktyczne doświadczenie z wzorcami i najlepszymi praktykami niezbędnymi w zaawansowanych aplikacjach AI i opartych na LLM.

## Wprowadzenie

W tej lekcji nauczysz się, jak zbudować zaawansowany serwer i klient MCP, który rozszerza możliwości LLM o dane z sieci w czasie rzeczywistym, korzystając z SerpAPI. To kluczowa umiejętność do tworzenia dynamicznych agentów AI, które mają dostęp do aktualnych informacji z internetu.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Bezpiecznie integrować zewnętrzne API (takie jak SerpAPI) z serwerem MCP
- Implementować wiele narzędzi do wyszukiwania w sieci, wiadomości, produktów oraz Q&A
- Parsować i formatować dane strukturalne dla potrzeb LLM
- Skutecznie obsługiwać błędy i zarządzać limitami API
- Budować i testować zarówno zautomatyzowanych, jak i interaktywnych klientów MCP

## Serwer MCP do wyszukiwania w sieci

Ta sekcja przedstawia architekturę i funkcje serwera MCP do wyszukiwania w sieci. Zobaczysz, jak FastMCP i SerpAPI współpracują, by rozszerzyć możliwości LLM o dane z internetu w czasie rzeczywistym.

### Przegląd

Implementacja zawiera cztery narzędzia, które pokazują zdolność MCP do bezpiecznego i efektywnego obsługiwania różnorodnych zadań opartych na zewnętrznych API:

- **general_search**: do szerokich wyników wyszukiwania w sieci
- **news_search**: do najnowszych nagłówków wiadomości
- **product_search**: do danych e-commerce
- **qna**: do fragmentów pytań i odpowiedzi

### Funkcje
- **Przykłady kodu**: Zawiera bloki kodu specyficzne dla języka Python (łatwe do rozszerzenia na inne języki) z użyciem pivotów kodu dla przejrzystości

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Przed uruchomieniem klienta warto zrozumieć, co robi serwer. Plik [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementuje serwer MCP, udostępniając narzędzia do wyszukiwania w sieci, wiadomości, produktów i Q&A poprzez integrację z SerpAPI. Obsługuje przychodzące żądania, zarządza wywołaniami API, parsuje odpowiedzi i zwraca klientowi uporządkowane wyniki.

Pełną implementację możesz przejrzeć w [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Poniżej krótki przykład, jak serwer definiuje i rejestruje narzędzie:

### Serwer Python

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Integracja z zewnętrznym API**: Pokazuje bezpieczne zarządzanie kluczami API i zapytaniami zewnętrznymi
- **Parsowanie danych strukturalnych**: Przekształcanie odpowiedzi API na formaty przyjazne dla LLM
- **Obsługa błędów**: Solidna obsługa błędów z odpowiednim logowaniem
- **Interaktywny klient**: Zawiera zarówno testy automatyczne, jak i tryb interaktywny do testowania
- **Zarządzanie kontekstem**: Wykorzystuje MCP Context do logowania i śledzenia żądań

## Wymagania wstępne

Zanim zaczniesz, upewnij się, że środowisko jest poprawnie skonfigurowane, wykonując poniższe kroki. Zapewni to instalację wszystkich zależności i poprawną konfigurację kluczy API, co umożliwi płynny rozwój i testowanie.

- Python 3.8 lub nowszy
- Klucz API SerpAPI (zarejestruj się na [SerpAPI](https://serpapi.com/) — dostępny darmowy plan)

## Instalacja

Aby rozpocząć, wykonaj następujące kroki, aby skonfigurować środowisko:

1. Zainstaluj zależności za pomocą uv (zalecane) lub pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Utwórz plik `.env` w katalogu głównym projektu z Twoim kluczem SerpAPI:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Użytkowanie

Serwer MCP do wyszukiwania w sieci to główny komponent, który udostępnia narzędzia do wyszukiwania w sieci, wiadomości, produktów i Q&A, integrując się z SerpAPI. Obsługuje przychodzące żądania, zarządza wywołaniami API, parsuje odpowiedzi i zwraca uporządkowane wyniki klientowi.

Pełną implementację możesz przejrzeć w [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Uruchamianie serwera

Aby uruchomić serwer MCP, użyj następującego polecenia:

```bash
python server.py
```

Serwer będzie działał jako MCP oparty na stdio, do którego klient może się bezpośrednio podłączyć.

### Tryby klienta

Klient (`client.py`) obsługuje dwa tryby interakcji z serwerem MCP:

- **Tryb normalny**: Uruchamia automatyczne testy, które sprawdzają wszystkie narzędzia i weryfikują ich odpowiedzi. Przydatne do szybkiego sprawdzenia, czy serwer i narzędzia działają poprawnie.
- **Tryb interaktywny**: Uruchamia interfejs menu, w którym możesz ręcznie wybierać i wywoływać narzędzia, wpisywać własne zapytania i na bieżąco oglądać wyniki. Idealny do eksploracji możliwości serwera i eksperymentowania z różnymi danymi wejściowymi.

Pełną implementację możesz przejrzeć w [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Uruchamianie klienta

Aby uruchomić testy automatyczne (uruchomi to automatycznie serwer):

```bash
python client.py
```

Lub uruchom w trybie interaktywnym:

```bash
python client.py --interactive
```

### Testowanie różnymi metodami

Istnieje kilka sposobów testowania i interakcji z narzędziami udostępnianymi przez serwer, w zależności od Twoich potrzeb i sposobu pracy.

#### Pisanie własnych skryptów testowych z MCP Python SDK
Możesz też tworzyć własne skrypty testowe, korzystając z MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

W tym kontekście „skrypt testowy” oznacza niestandardowy program w Pythonie, który piszesz, aby działać jako klient serwera MCP. Zamiast formalnego testu jednostkowego, ten skrypt pozwala programowo łączyć się z serwerem, wywoływać dowolne narzędzia z wybranymi parametrami i analizować wyniki. To podejście jest przydatne do:
- Prototypowania i eksperymentowania z wywołaniami narzędzi
- Weryfikacji, jak serwer reaguje na różne dane wejściowe
- Automatyzacji powtarzających się wywołań narzędzi
- Budowania własnych przepływów pracy lub integracji na bazie serwera MCP

Możesz używać skryptów testowych do szybkiego wypróbowania nowych zapytań, debugowania zachowania narzędzi lub jako punktu wyjścia do bardziej zaawansowanej automatyzacji. Poniżej przykład użycia MCP Python SDK do stworzenia takiego skryptu:

## Opisy narzędzi

Możesz korzystać z poniższych narzędzi udostępnianych przez serwer do wykonywania różnych typów wyszukiwań i zapytań. Każde narzędzie opisano poniżej wraz z parametrami i przykładowym użyciem.

Ta sekcja zawiera szczegóły dotyczące każdego dostępnego narzędzia i ich parametrów.

### general_search

Wykonuje ogólne wyszukiwanie w sieci i zwraca sformatowane wyniki.

**Jak wywołać to narzędzie:**

Możesz wywołać `general_search` ze swojego skryptu, korzystając z MCP Python SDK, lub interaktywnie za pomocą Inspektora albo trybu interaktywnego klienta. Oto przykład kodu z użyciem SDK:

# [Przykład w Pythonie](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Alternatywnie, w trybie interaktywnym wybierz `general_search` z menu i wpisz zapytanie, gdy zostaniesz o to poproszony.

**Parametry:**
- `query` (string): zapytanie wyszukiwania

**Przykładowe zapytanie:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Wyszukuje najnowsze artykuły wiadomości związane z zapytaniem.

**Jak wywołać to narzędzie:**

Możesz wywołać `news_search` ze swojego skryptu, korzystając z MCP Python SDK, lub interaktywnie za pomocą Inspektora albo trybu interaktywnego klienta. Oto przykład kodu z użyciem SDK:

# [Przykład w Pythonie](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Alternatywnie, w trybie interaktywnym wybierz `news_search` z menu i wpisz zapytanie, gdy zostaniesz o to poproszony.

**Parametry:**
- `query` (string): zapytanie wyszukiwania

**Przykładowe zapytanie:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Wyszukuje produkty pasujące do zapytania.

**Jak wywołać to narzędzie:**

Możesz wywołać `product_search` ze swojego skryptu, korzystając z MCP Python SDK, lub interaktywnie za pomocą Inspektora albo trybu interaktywnego klienta. Oto przykład kodu z użyciem SDK:

# [Przykład w Pythonie](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Alternatywnie, w trybie interaktywnym wybierz `product_search` z menu i wpisz zapytanie, gdy zostaniesz o to poproszony.

**Parametry:**
- `query` (string): zapytanie wyszukiwania produktów

**Przykładowe zapytanie:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Uzyskuje bezpośrednie odpowiedzi na pytania z wyszukiwarek.

**Jak wywołać to narzędzie:**

Możesz wywołać `qna` ze swojego skryptu, korzystając z MCP Python SDK, lub interaktywnie za pomocą Inspektora albo trybu interaktywnego klienta. Oto przykład kodu z użyciem SDK:

# [Przykład w Pythonie](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Alternatywnie, w trybie interaktywnym wybierz `qna` z menu i wpisz pytanie, gdy zostaniesz o to poproszony.

**Parametry:**
- `question` (string): pytanie, na które chcesz uzyskać odpowiedź

**Przykładowe zapytanie:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Szczegóły kodu

Ta sekcja zawiera fragmenty kodu i odniesienia do implementacji serwera i klienta.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Pełne szczegóły implementacji znajdziesz w [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) i [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Zaawansowane koncepcje w tej lekcji

Zanim zaczniesz budować, oto kilka ważnych zaawansowanych koncepcji, które pojawią się w całym rozdziale. Ich zrozumienie pomoże Ci lepiej śledzić materiał, nawet jeśli są dla Ciebie nowe:

- **Orkiestracja wielu narzędzi**: Oznacza uruchamianie kilku różnych narzędzi (takich jak wyszukiwanie w sieci, wiadomości, produkty i Q&A) w jednym serwerze MCP. Pozwala to serwerowi obsługiwać różnorodne zadania, a nie tylko jedno.
- **Obsługa limitów API**: Wiele zewnętrznych API (np. SerpAPI) ogranicza liczbę zapytań w określonym czasie. Dobry kod sprawdza te limity i radzi sobie z nimi w sposób łagodny, aby aplikacja nie przestała działać po przekroczeniu limitu.
- **Parsowanie danych strukturalnych**: Odpowiedzi API są często złożone i zagnieżdżone. Ta koncepcja polega na przekształcaniu tych odpowiedzi w czyste, łatwe do użycia formaty, przyjazne dla LLM lub innych programów.
- **Odzyskiwanie po błędach**: Czasem coś idzie nie tak — może zawiedzie sieć lub API nie zwróci oczekiwanych danych. Odzyskiwanie po błędach oznacza, że Twój kod potrafi poradzić sobie z tymi problemami i nadal dostarczyć użyteczne informacje, zamiast się zawiesić.
- **Walidacja parametrów**: Chodzi o sprawdzanie, czy wszystkie dane wejściowe do narzędzi są poprawne i bezpieczne w użyciu. Obejmuje to ustawianie wartości domyślnych i upewnianie się, że typy są właściwe, co pomaga zapobiegać błędom i nieporozumieniom.

Ta sekcja pomoże Ci diagnozować i rozwiązywać typowe problemy, które mogą się pojawić podczas pracy z serwerem MCP do wyszukiwania w sieci. Jeśli napotkasz błędy lub nieoczekiwane zachowanie, ta część zawiera rozwiązania najczęstszych problemów. Przejrzyj te wskazówki przed szukaniem dalszej pomocy — często szybko rozwiązują problemy.

## Rozwiązywanie problemów

Podczas pracy z serwerem MCP do wyszukiwania w sieci mogą się zdarzyć problemy — to normalne przy pracy z zewnętrznymi API i nowymi narzędziami. Ta sekcja zawiera praktyczne rozwiązania najczęstszych problemów, dzięki czemu szybko wrócisz do pracy. Jeśli napotkasz błąd, zacznij tutaj: poniższe wskazówki dotyczą problemów, z którymi najczęściej spotykają się użytkownicy i często pozwalają rozwiązać problem bez dodatkowej pomocy.

### Najczęstsze problemy

Poniżej znajdziesz najczęściej występujące problemy wraz z jasnymi wyjaśnieniami i krokami do ich rozwiązania:

1. **Brak SERPAPI_KEY w pliku .env**
   - Jeśli pojawi się błąd `SERPAPI_KEY environment variable not found`, oznacza to, że aplikacja nie może znaleźć klucza API potrzebnego do dostępu do SerpAPI. Aby to naprawić, utwórz plik `.env` w katalogu głównym projektu (jeśli jeszcze go nie ma) i dodaj linię `SERPAPI_KEY=twoj_klucz_serpapi`. Pamiętaj, aby zastąpić `twoj_klucz_serpapi` faktycznym kluczem z serwisu SerpAPI.

2. **Błędy typu Module not found**
   - Błędy takie jak `ModuleNotFoundError: No module named 'httpx'` oznaczają, że brakuje wymaganego pakietu Pythona. Zwykle dzieje się tak, gdy nie zainstalowano wszystkich zależności. Aby to naprawić, uruchom w terminalu `pip install -r requirements.txt`, aby zainstalować wszystkie potrzebne pakiety.

3. **Problemy z połączeniem**
   - Jeśli pojawi się błąd `Error during client execution`, często oznacza to, że klient nie może połączyć się z serwerem lub serwer nie działa poprawnie. Sprawdź, czy klient i serwer mają kompatybilne wersje oraz czy plik `server.py` jest obecny i uruchomiony w odpowiednim katalogu. Pomocne może być też ponowne uruchomienie serwera i klienta.

4. **Błędy SerpAPI**
   - Komunikat `Search API returned error status: 401` oznacza, że klucz SerpAPI jest nieobecny, nieprawidłowy lub wygasł. Wejdź na swoje konto SerpAPI, zweryfikuj klucz i w razie potrzeby zaktualizuj plik `.env`. Jeśli klucz jest poprawny, a błąd nadal występuje, sprawdź, czy nie wyczerpał się limit darmowego planu.

### Tryb debugowania

Domyślnie aplikacja loguje tylko ważne informacje. Jeśli chcesz zobaczyć więcej szczegółów o tym, co się dzieje (
Aby włączyć tryb DEBUG, ustaw poziom logowania na DEBUG na początku pliku `client.py` lub `server.py`:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Co dalej

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.