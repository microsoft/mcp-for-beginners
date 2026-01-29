# MCP stdio Server - Rozwiązanie .NET

> **⚠️ Ważne**: To rozwiązanie zostało zaktualizowane, aby korzystać z **transportu stdio**, zgodnie z zaleceniami Specyfikacji MCP z dnia 2025-06-18. Oryginalny transport SSE został wycofany.

## Przegląd

To rozwiązanie .NET pokazuje, jak zbudować serwer MCP, korzystając z aktualnego transportu stdio. Transport stdio jest prostszy, bardziej bezpieczny i zapewnia lepszą wydajność niż wycofane podejście SSE.

## Wymagania wstępne

- .NET 9.0 SDK lub nowszy
- Podstawowa znajomość wstrzykiwania zależności w .NET

## Instrukcje konfiguracji

### Krok 1: Przywróć zależności

```bash
dotnet restore
```

### Krok 2: Zbuduj projekt

```bash
dotnet build
```

## Uruchamianie serwera

Serwer stdio działa inaczej niż stary serwer oparty na HTTP. Zamiast uruchamiania serwera webowego, komunikuje się przez stdin/stdout:

```bash
dotnet run
```

**Ważne**: Serwer może wydawać się zawieszony - to normalne! Czeka na wiadomości JSON-RPC z stdin.

## Testowanie serwera

### Metoda 1: Korzystanie z MCP Inspector (zalecane)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

To spowoduje:
1. Uruchomienie serwera jako podprocesu
2. Otworzenie interfejsu webowego do testowania
3. Umożliwienie interaktywnego testowania wszystkich narzędzi serwera

### Metoda 2: Testowanie bezpośrednio z linii poleceń

Możesz również testować, uruchamiając Inspektora bezpośrednio:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Dostępne narzędzia

Serwer udostępnia następujące narzędzia:

- **AddNumbers(a, b)**: Dodaje dwie liczby
- **MultiplyNumbers(a, b)**: Mnoży dwie liczby  
- **GetGreeting(name)**: Generuje spersonalizowane powitanie
- **GetServerInfo()**: Pobiera informacje o serwerze

### Testowanie z Claude Desktop

Aby używać tego serwera z Claude Desktop, dodaj tę konfigurację do pliku `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Struktura projektu

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Kluczowe różnice między HTTP/SSE

**Transport stdio (obecny):**
- ✅ Prostsza konfiguracja - brak potrzeby serwera webowego
- ✅ Lepsze bezpieczeństwo - brak punktów końcowych HTTP
- ✅ Używa `Host.CreateApplicationBuilder()` zamiast `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` zamiast `WithHttpTransport()`
- ✅ Aplikacja konsolowa zamiast aplikacji webowej
- ✅ Lepsza wydajność

**Transport HTTP/SSE (wycofany):**
- ❌ Wymagał serwera webowego ASP.NET Core
- ❌ Potrzebował konfiguracji routingu `app.MapMcp()`
- ❌ Bardziej skomplikowana konfiguracja i zależności
- ❌ Dodatkowe kwestie bezpieczeństwa
- ❌ Wycofany w MCP 2025-06-18

## Funkcje rozwojowe

- **Wstrzykiwanie zależności**: Pełne wsparcie DI dla usług i logowania
- **Strukturalne logowanie**: Poprawne logowanie do stderr za pomocą `ILogger<T>`
- **Atrybuty narzędzi**: Czysta definicja narzędzi za pomocą atrybutów `[McpServerTool]`
- **Wsparcie dla async**: Wszystkie narzędzia obsługują operacje asynchroniczne
- **Obsługa błędów**: Łagodne zarządzanie błędami i logowanie

## Wskazówki rozwojowe

- Używaj `ILogger` do logowania (nigdy nie pisz bezpośrednio do stdout)
- Buduj projekt za pomocą `dotnet build` przed testowaniem
- Testuj za pomocą Inspektora dla wizualnego debugowania
- Wszystkie logi trafiają automatycznie do stderr
- Serwer obsługuje sygnały łagodnego zamykania

To rozwiązanie jest zgodne z aktualną specyfikacją MCP i pokazuje najlepsze praktyki implementacji transportu stdio w .NET.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.