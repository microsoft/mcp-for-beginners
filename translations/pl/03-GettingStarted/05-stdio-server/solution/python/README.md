# MCP stdio Server - Rozwiązanie w Pythonie

> **⚠️ Ważne**: To rozwiązanie zostało zaktualizowane, aby korzystać z **transportu stdio**, zgodnie z zaleceniami Specyfikacji MCP z dnia 2025-06-18. Pierwotny transport SSE został wycofany.

## Przegląd

To rozwiązanie w Pythonie pokazuje, jak zbudować serwer MCP, korzystając z aktualnego transportu stdio. Transport stdio jest prostszy, bardziej bezpieczny i zapewnia lepszą wydajność niż wycofane podejście SSE.

## Wymagania wstępne

- Python 3.8 lub nowszy
- Zaleca się zainstalowanie `uv` do zarządzania pakietami, zobacz [instrukcje](https://docs.astral.sh/uv/#highlights)

## Instrukcje konfiguracji

### Krok 1: Utwórz wirtualne środowisko

```bash
python -m venv venv
```

### Krok 2: Aktywuj wirtualne środowisko

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Krok 3: Zainstaluj zależności

```bash
pip install mcp
```

## Uruchamianie serwera

Serwer stdio działa inaczej niż stary serwer SSE. Zamiast uruchamiania serwera WWW, komunikuje się przez stdin/stdout:

```bash
python server.py
```

**Ważne**: Serwer może wydawać się zawieszony - to normalne! Czeka na wiadomości JSON-RPC z stdin.

## Testowanie serwera

### Metoda 1: Korzystanie z MCP Inspector (Zalecane)

```bash
npx @modelcontextprotocol/inspector python server.py
```

To pozwoli:
1. Uruchomić serwer jako podproces
2. Otworzyć interfejs webowy do testowania
3. Testować wszystkie narzędzia serwera interaktywnie

### Metoda 2: Bezpośrednie testowanie JSON-RPC

Możesz również testować, wysyłając wiadomości JSON-RPC bezpośrednio:

1. Uruchom serwer: `python server.py`
2. Wyślij wiadomość JSON-RPC (przykład):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Serwer odpowie dostępnymi narzędziami

### Dostępne narzędzia

Serwer udostępnia następujące narzędzia:

- **add(a, b)**: Dodaj dwie liczby
- **multiply(a, b)**: Pomnóż dwie liczby  
- **get_greeting(name)**: Wygeneruj spersonalizowane powitanie
- **get_server_info()**: Pobierz informacje o serwerze

### Testowanie z Claude Desktop

Aby używać tego serwera z Claude Desktop, dodaj tę konfigurację do swojego pliku `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Kluczowe różnice w stosunku do SSE

**Transport stdio (Aktualny):**
- ✅ Prostsza konfiguracja - brak potrzeby serwera WWW
- ✅ Lepsze bezpieczeństwo - brak punktów końcowych HTTP
- ✅ Komunikacja oparta na podprocesach
- ✅ JSON-RPC przez stdin/stdout
- ✅ Lepsza wydajność

**Transport SSE (Wycofany):**
- ❌ Wymagał konfiguracji serwera HTTP
- ❌ Potrzebował frameworka webowego (Starlette/FastAPI)
- ❌ Bardziej skomplikowane zarządzanie trasami i sesjami
- ❌ Dodatkowe kwestie bezpieczeństwa
- ❌ Wycofany w MCP 2025-06-18

## Wskazówki dotyczące debugowania

- Używaj `stderr` do logowania (nigdy `stdout`)
- Testuj za pomocą Inspectora dla wizualnego debugowania
- Upewnij się, że wszystkie wiadomości JSON są oddzielone znakami nowej linii
- Sprawdź, czy serwer uruchamia się bez błędów

To rozwiązanie jest zgodne z aktualną specyfikacją MCP i pokazuje najlepsze praktyki implementacji transportu stdio.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.