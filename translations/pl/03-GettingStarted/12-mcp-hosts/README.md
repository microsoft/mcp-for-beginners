# Konfigurowanie popularnych klientów hosta MCP

> [!NOTE]
> Konfiguracje hostów wskazujące na `/sse` to przykłady legacy HTTP+SSE dla
> MCP `2025-11-25`. Dla MCP `2026-07-28` wybierz Streamable HTTP w hostach, które
> to obsługują i używaj punktu końcowego skonfigurowanego przez serwer.

Ten przewodnik opisuje, jak konfigurować i używać serwery MCP z popularnymi aplikacjami hosta AI. Każdy host ma własne podejście do konfiguracji, ale po ustawieniu wszyscy komunikują się z serwerami MCP za pomocą ustandaryzowanego protokołu.

## Co to jest host MCP?

**Host MCP** to aplikacja AI, która może łączyć się z serwerami MCP, aby rozszerzyć swoje możliwości. Można go traktować jako „front end”, z którym użytkownicy wchodzą w interakcję, podczas gdy serwery MCP zapewniają narzędzia i dane „back end”.

```mermaid
flowchart LR
    User[👤 Użytkownik] --> Host[🖥️ Gospodarz MCP]
    Host --> S1[Serwer MCP A]
    Host --> S2[Serwer MCP B]
    Host --> S3[Serwer MCP C]
    
    subgraph "Popularni gospodarze"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Wymagania wstępne

- Serwer MCP do połączenia (zobacz [Moduł 3.1 - Pierwszy serwer](../01-first-server/README.md))
- Aplikacja hosta zainstalowana w Twoim systemie
- Podstawowa znajomość plików konfiguracyjnych JSON

---

## 1. Claude Desktop

**Claude Desktop** to oficjalna aplikacja desktopowa Anthropic z natywnym wsparciem MCP.

### Instalacja

1. Pobierz Claude Desktop z [claude.ai/download](https://claude.ai/download)
2. Zainstaluj i zaloguj się przy użyciu konta Anthropic

### Konfiguracja

Claude Desktop używa pliku konfiguracyjnego JSON do definiowania serwerów MCP.

**Lokalizacja pliku konfiguracyjnego:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Przykładowa konfiguracja:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Opcje konfiguracji

| Pole | Opis | Przykład |
|-------|-------------|---------|
| `command` | Program do uruchomienia | `"python"`, `"node"`, `"npx"` |
| `args` | Argumenty wiersza poleceń | `["-m", "my_server"]` |
| `env` | Zmienne środowiskowe | `{"API_KEY": "xxx"}` |
| `cwd` | Katalog roboczy | `"/path/to/server"` |

### Testowanie konfiguracji

1. Zapisz plik konfiguracyjny
2. Całkowicie zrestartuj Claude Desktop (zamknij i otwórz ponownie)
3. Otwórz nową rozmowę
4. Szukaj ikony 🔌 wskazującej podłączone serwery
5. Spróbuj poprosić Claude o użycie jednego z narzędzi

### Rozwiązywanie problemów Claude Desktop

**Serwer się nie pojawia:**
- Sprawdź składnię pliku konfiguracyjnego za pomocą walidatora JSON
- Upewnij się, że ścieżka polecenia jest poprawna
- Sprawdź logi Claude Desktop: Pomoc → Pokaż logi

**Serwer się zawiesza podczas uruchamiania:**
- Przetestuj serwer ręcznie w terminalu
- Sprawdź poprawność ustawienia zmiennych środowiskowych
- Upewnij się, że wszystkie zależności są zainstalowane

---

## 2. VS Code z GitHub Copilot

VS Code obsługuje MCP dzięki rozszerzeniom GitHub Copilot Chat.

### Wymagania wstępne

1. Zainstalowany VS Code w wersji 1.99+
2. Zainstalowane rozszerzenie GitHub Copilot
3. Zainstalowane rozszerzenie GitHub Copilot Chat

### Konfiguracja

VS Code używa pliku `.vscode/mcp.json` w ustawieniach przestrzeni roboczej lub użytkownika.

**Konfiguracja przestrzeni roboczej** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Ustawienia użytkownika** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Używanie MCP w VS Code

1. Otwórz panel Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Wpisz `@`, aby zobaczyć dostępne narzędzia MCP
3. Używaj naturalnego języka, aby wywoływać narzędzia: "Calculate 25 * 48 using the calculator"

### Rozwiązywanie problemów VS Code

**Serwery MCP się nie ładują:**
- Sprawdź panel Wyjście → "MCP" pod kątem logów błędów
- Przeładuj okno: Ctrl+Shift+P → "Developer: Reload Window"
- Zweryfikuj, czy serwer działa samodzielnie

---

## 3. Cursor

**Cursor** to edytor kodu z orientacją AI z wbudowanym wsparciem MCP.

### Instalacja

1. Pobierz Cursor z [cursor.sh](https://cursor.sh)
2. Zainstaluj i zaloguj się

### Konfiguracja

Cursor używa podobnego formatu konfiguracji jak Claude Desktop.

**Lokalizacja pliku konfiguracyjnego:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Przykładowa konfiguracja:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Używanie MCP w Cursor

1. Otwórz czat AI Cursor (Ctrl+L / Cmd+L)
2. Narzędzia MCP pojawiają się automatycznie w sugestiach
3. Poproś AI o wykonanie zadań z użyciem połączonych serwerów

---

## 4. Cline (na bazie terminala)

**Cline** to klient MCP działający w terminalu, idealny do pracy w wierszu poleceń.

### Instalacja

```bash
npm install -g @anthropic/cline
```

### Konfiguracja

Cline używa zmiennych środowiskowych oraz argumentów wiersza poleceń.

**Używanie zmiennych środowiskowych:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Używanie argumentów wiersza poleceń:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Plik konfiguracyjny** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Używanie Cline

```bash
# Rozpocznij sesję interaktywną
cline

# Pojedyncze zapytanie z MCP
cline "Calculate the square root of 144 using the calculator"

# Wyświetl dostępne narzędzia
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** to kolejny edytor kodu zasilany AI z wsparciem MCP.

### Instalacja

1. Pobierz Windsurf z [codeium.com/windsurf](https://codeium.com/windsurf)
2. Zainstaluj i utwórz konto

### Konfiguracja

Konfiguracja Windsurf jest zarządzana przez interfejs ustawień:

1. Otwórz Ustawienia (Ctrl+, / Cmd+,)
2. Wyszukaj "MCP"
3. Kliknij "Edytuj w settings.json"

**Przykładowa konfiguracja:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Porównanie typów transportu

Różne hosty obsługują różne mechanizmy transportu:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standardowe wejście/wyjście): Najlepsze dla lokalnych serwerów uruchomionych przez hosta
**SSE/HTTP**: Najlepsze dla serwerów zdalnych lub współdzielonych między kilkoma klientami

---

## Częste problemy i ich rozwiązywanie

### Serwer nie chce się uruchomić

1. **Najpierw przetestuj serwer ręcznie:**
   ```bash
   # Dla Pythona
   python -m your_server_module
   
   # Dla Node.js
   node /path/to/server/index.js
   ```

2. **Sprawdź ścieżkę polecenia:**
   - Tam gdzie to możliwe używaj ścieżek absolutnych
   - Upewnij się, że program wykonywalny jest w Twojej ścieżce PATH

3. **Zweryfikuj zależności:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Serwer się łączy, ale narzędzia nie działają

1. **Sprawdź logi serwera** - Większość hostów oferuje opcje logowania
2. **Zweryfikuj rejestrację narzędzi** - Użyj MCP Inspector do testów
3. **Sprawdź uprawnienia** - Niektóre narzędzia wymagają dostępu do plików/sieci

### Zmienne środowiskowe nie są przekazywane

- Niektóre hosty oczyszczają zmienne środowiskowe
- Używaj wyraźnie pola konfiguracyjnego `env`
- Unikaj wrażliwych danych w plikach konfiguracyjnych (używaj zarządzania sekretami)

---

## Najlepsze praktyki bezpieczeństwa

1. **Nigdy nie zamieszczaj kluczy API** w plikach konfiguracyjnych
2. **Używaj zmiennych środowiskowych** do danych wrażliwych
3. **Ogranicz uprawnienia serwera** tylko do niezbędnych
4. **Przejrzyj kod serwera** przed udzieleniem dostępu do systemu
5. **Używaj list dozwolonych** dla dostępu do systemu plików i sieci

---

## Co dalej

- [3.13 - Debugowanie z MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Utwórz swój pierwszy serwer MCP](../01-first-server/README.md)
- [Moduł 5 - Tematy zaawansowane](../../05-AdvancedTopics/README.md)

---

## Dodatkowe zasoby

- [Dokumentacja MCP Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Rozszerzenie MCP do VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Specyfikacja MCP - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Oficjalny rejestr serwerów MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->