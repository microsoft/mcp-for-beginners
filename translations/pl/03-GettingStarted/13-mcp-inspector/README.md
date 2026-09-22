# Debugowanie za pomocą MCP Inspector

> [!NOTE]
> Polecenia używające `--sse` i adresy URL kończące się na `/sse` testują starszy transport HTTP+SSE.
> Dla nowego serwera MCP `2026-07-28` użyj wersji Inspectora, która
> obsługuje Streamable HTTP i wybierz ten transport zamiast tego.

**MCP Inspector** to podstawowe narzędzie do debugowania, które pozwala interaktywnie testować i rozwiązywać problemy z serwerami MCP bez potrzeby pełnej aplikacji hosta AI. Można o nim myśleć jak o "Postmanie dla MCP" - zapewnia wizualny interfejs do wysyłania żądań, przeglądania odpowiedzi i zrozumienia zachowania serwera.

## Dlaczego warto korzystać z MCP Inspector?

Podczas tworzenia serwerów MCP często napotykasz na następujące wyzwania:

- **"Czy mój serwer w ogóle działa?"** - Inspector pokazuje status połączenia
- **"Czy moje narzędzia są poprawnie zarejestrowane?"** - Inspector wyświetla wszystkie dostępne narzędzia
- **"Jaki jest format odpowiedzi?"** - Inspector pokazuje pełne odpowiedzi JSON
- **"Dlaczego to narzędzie nie działa?"** - Inspector pokazuje szczegółowe komunikaty błędów

## Wymagania wstępne

- Zainstalowany Node.js 18+
- npm (dołączony do Node.js)
- Serwer MCP do przetestowania (zobacz [Moduł 3.1 - Pierwszy Serwer](../01-first-server/README.md))

## Instalacja

### Opcja 1: Uruchomienie za pomocą npx (zalecane do szybkiego testowania)

```bash
npx @modelcontextprotocol/inspector
```

### Opcja 2: Instalacja globalna

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Opcja 3: Dodanie do projektu

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Dodaj do `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Łączenie z serwerem

### Serwery stdio (lokalny proces)

Dla serwerów komunikujących się przez standardowe wejście/wyjście:

```bash
# Serwer Pythona
npx @modelcontextprotocol/inspector python -m your_server_module

# Serwer Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# Z zmiennymi środowiskowymi
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### Serwery SSE/HTTP (sieć)

Dla serwerów działających jako usługi HTTP:

1. Najpierw uruchom serwer:
   ```bash
   python server.py  # Serwer działa na http://localhost:8080
   ```

2. Uruchom Inspector i połącz się:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Przegląd interfejsu Inspectora

Po uruchomieniu Inspectora zobaczysz interfejs webowy (zwykle pod adresem `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Testowanie narzędzi

### Wyświetlanie listy dostępnych narzędzi

1. Kliknij zakładkę **Tools**
2. Inspector automatycznie wywołuje `tools/list`
3. Zobaczysz wszystkie zarejestrowane narzędzia z:
   - nazwą narzędzia
   - opisem
   - schematem wejściowym (parametry)

### Wywołanie narzędzia

1. Wybierz narzędzie z listy
2. Wypełnij wymagane parametry w formularzu
3. Kliknij **Run Tool**
4. Zobacz odpowiedź w panelu wyników

**Przykład: Testowanie narzędzia kalkulatora**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Debugowanie błędów narzędzi

Kiedy narzędzie zawiedzie, Inspector pokazuje:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Popularne kody błędów:
| Kod | Znaczenie |
|------|---------|
| -32700 | Błąd parsowania (niepoprawny JSON) |
| -32600 | Nieprawidłowe żądanie |
| -32601 | Nie znaleziono metody |
| -32602 | Nieprawidłowe parametry |
| -32603 | Błąd wewnętrzny |

---

## Testowanie zasobów

### Wyświetlanie listy zasobów

1. Kliknij zakładkę **Resources**
2. Inspector wywołuje `resources/list`
3. Zobaczysz:
   - URI zasobów
   - Nazwy i opisy
   - Typy MIME

### Odczyt zasobu

1. Wybierz zasób
2. Kliknij **Read Resource**
3. Zobacz zwróconą zawartość

**Przykładowy wynik:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Testowanie promptów

### Wyświetlanie listy promptów

1. Kliknij zakładkę **Prompts**
2. Inspector wywołuje `prompts/list`
3. Zobacz dostępne szablony promptów

### Pobieranie promptu

1. Wybierz prompt
2. Wypełnij wymagane argumenty
3. Kliknij **Get Prompt**
4. Zobacz wygenerowane wiadomości promptów

---

## Analiza logu wiadomości

Log wiadomości pokazuje wszystkie komunikaty protokołu MCP. Poniższa rozmowa pochodzi z
starszego serwera `2025-11-25` i zawiera usunięte `initialize` handshake. Serwer
`2026-07-28` używa samodzielnych metadanych żądań i `server/discover`
w zamian.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Na co zwrócić uwagę

- **Pary żądań/odpowiedzi**: Każde `→` powinno mieć dopasowane `←`
- **Komunikaty błędów**: Szukaj `"error"` w odpowiedziach
- **Czas**: Duże przerwy mogą wskazywać na problemy z wydajnością
- **Wersja protokołu**: Upewnij się, że serwer i klient zgadzają się co do wersji

---

## Integracja z VS Code

Inspector możesz uruchomić bezpośrednio z VS Code:

### Korzystanie z launch.json

Dodaj do `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Korzystanie z zadań (Tasks)

Dodaj do `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Typowe scenariusze debugowania

### Scenariusz 1: Serwer nie łączy się

**Objawy:** Inspector pokazuje "Disconnected" albo zawiesza się na "Connecting..."

**Lista kontrolna:**
1. ✅ Czy polecenie serwera jest poprawne?
2. ✅ Czy wszystkie zależności są zainstalowane?
3. ✅ Czy ścieżka do serwera jest absolutna lub względem bieżącego katalogu?
4. ✅ Czy wymagane zmienne środowiskowe są ustawione?

**Kroki debugowania:**
```bash
# Najpierw przetestuj serwer ręcznie
python -c "import your_server_module; print('OK')"

# Sprawdź, czy nie ma błędów importu
python -m your_server_module 2>&1 | head -20

# Zweryfikuj, czy SDK MCP jest zainstalowane
pip show mcp
```

### Scenariusz 2: Brak wyświetlanych narzędzi

**Objawy:** Zakładka Tools pokazuje pustą listę

**Możliwe przyczyny:**
1. Narzędzia nie zostały zarejestrowane podczas inicjalizacji serwera
2. Serwer uległ awarii po uruchomieniu
3. Handler `tools/list` zwraca pustą tablicę

**Kroki debugowania:**
1. Sprawdź log wiadomości pod kątem odpowiedzi `tools/list`
2. Dodaj logowanie do kodu rejestracji narzędzi
3. Zweryfikuj obecność dekoratorów `@mcp.tool()` (Python)

### Scenariusz 3: Narzędzie zwraca błąd

**Objawy:** Wywołanie narzędzia zwraca błąd

**Podejście debugowania:**
1. Przeczytaj uważnie komunikat błędu
2. Sprawdź czy typy parametrów odpowiadają schematowi
3. Dodaj try/catch z szczegółowymi komunikatami błędów
4. Przejrzyj logi serwera pod kątem stack trace'ów

**Przykład ulepszonego obsługi błędów:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Logika narzędzia tutaj
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenariusz 4: Zawartość zasobu pusta

**Objawy:** Zasób zwraca zawartość pustą lub null

**Lista kontrolna:**
1. ✅ Ścieżka do pliku lub URI jest poprawna
2. ✅ Serwer ma uprawnienia do odczytu zasobu
3. ✅ Zawartość zasobu jest poprawnie zwracana

---

## Zaawansowane funkcje Inspectora

### Niestandardowe nagłówki (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Szczegółowe logowanie

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Nagrywanie sesji

Inspector potrafi eksportować logi wiadomości do późniejszej analizy:
1. Kliknij **Export Log** w panelu wiadomości
2. Zapisz plik JSON
3. Udostępnij członkom zespołu do debugowania

---

## Dobre praktyki

1. **Testuj wcześnie i często** - Korzystaj z Inspectora podczas rozwoju, nie tylko gdy coś przestaje działać
2. **Zacznij od prostego** - Sprawdź podstawowe połączenie zanim wywołasz skomplikowane narzędzia
3. **Sprawdź schemat** - Wiele błędów wynika z niezgodności typów parametrów
4. **Czytaj komunikaty błędów** - Błędy MCP zazwyczaj są opisowe
5. **Trzymaj Inspectora otwartego** - Pomaga wykryć problemy podczas rozwoju

---

## Co dalej

Ukończyłeś Moduł 3: Pierwsze kroki! Kontynuuj naukę:

- [Moduł 4: Praktyczna implementacja](../../04-PracticalImplementation/README.md)

---

## Dodatkowe zasoby

- [Repozytorium MCP Inspector na GitHub](https://github.com/modelcontextprotocol/inspector)
- [Specyfikacja MCP - komunikaty protokołu](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Specyfikacja JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->