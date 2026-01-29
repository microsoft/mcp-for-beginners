# MCP stdio Server - Rozwiązanie w TypeScript

> **⚠️ Ważne**: To rozwiązanie zostało zaktualizowane, aby korzystać z **transportu stdio**, zgodnie z zaleceniami Specyfikacji MCP z dnia 2025-06-18. Oryginalny transport SSE został wycofany.

## Przegląd

To rozwiązanie w TypeScript pokazuje, jak zbudować serwer MCP, korzystając z aktualnego transportu stdio. Transport stdio jest prostszy, bardziej bezpieczny i zapewnia lepszą wydajność w porównaniu do wycofanego podejścia SSE.

## Wymagania wstępne

- Node.js 18+ lub nowszy
- Menedżer pakietów npm lub yarn

## Instrukcja konfiguracji

### Krok 1: Zainstaluj zależności

```bash
npm install
```

### Krok 2: Zbuduj projekt

```bash
npm run build
```

## Uruchamianie serwera

Serwer stdio działa inaczej niż stary serwer SSE. Zamiast uruchamiania serwera WWW, komunikuje się on za pomocą stdin/stdout:

```bash
npm start
```

**Ważne**: Serwer może wydawać się zawieszony - to normalne! Oczekuje na wiadomości JSON-RPC z stdin.

## Testowanie serwera

### Metoda 1: Korzystanie z MCP Inspector (Zalecane)

```bash
npm run inspector
```

To spowoduje:
1. Uruchomienie serwera jako procesu podrzędnego
2. Otworzenie interfejsu webowego do testowania
3. Możliwość interaktywnego testowania wszystkich narzędzi serwera

### Metoda 2: Testowanie bezpośrednio z wiersza poleceń

Możesz również testować, uruchamiając Inspektora bezpośrednio:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Dostępne narzędzia

Serwer udostępnia następujące narzędzia:

- **add(a, b)**: Dodaje dwie liczby
- **multiply(a, b)**: Mnoży dwie liczby  
- **get_greeting(name)**: Generuje spersonalizowane powitanie
- **get_server_info()**: Zwraca informacje o serwerze

### Testowanie z Claude Desktop

Aby używać tego serwera z Claude Desktop, dodaj tę konfigurację do pliku `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Struktura projektu

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Kluczowe różnice w stosunku do SSE

**Transport stdio (obecny):**
- ✅ Prostsza konfiguracja - brak potrzeby serwera HTTP
- ✅ Lepsze bezpieczeństwo - brak punktów końcowych HTTP
- ✅ Komunikacja oparta na procesach podrzędnych
- ✅ JSON-RPC przez stdin/stdout
- ✅ Lepsza wydajność

**Transport SSE (wycofany):**
- ❌ Wymagał konfiguracji serwera Express
- ❌ Potrzebował złożonego routingu i zarządzania sesjami
- ❌ Więcej zależności (Express, obsługa HTTP)
- ❌ Dodatkowe kwestie bezpieczeństwa
- ❌ Obecnie wycofany w MCP 2025-06-18

## Wskazówki dotyczące rozwoju

- Używaj `console.error()` do logowania (nigdy `console.log()`, ponieważ zapisuje do stdout)
- Buduj projekt za pomocą `npm run build` przed testowaniem
- Testuj za pomocą Inspektora, aby uzyskać wizualne debugowanie
- Upewnij się, że wszystkie wiadomości JSON są poprawnie sformatowane
- Serwer automatycznie obsługuje łagodne zamykanie przy SIGINT/SIGTERM

To rozwiązanie jest zgodne z aktualną specyfikacją MCP i pokazuje najlepsze praktyki implementacji transportu stdio w TypeScript.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.