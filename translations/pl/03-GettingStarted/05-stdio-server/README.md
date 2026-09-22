# Serwer MCP z transportem stdio

> **⚠️ Ważna aktualizacja**: Od specyfikacji MCP z dnia 2025-06-18, samodzielny transport SSE (Server-Sent Events) został **wycofany** i zastąpiony przez transport "Streamable HTTP". Obecna specyfikacja MCP definiuje dwa główne mechanizmy transportu:
> 1. **stdio** - standardowy wejście/wyjście (zalecany dla lokalnych serwerów)
> 2. **Streamable HTTP** - dla zdalnych serwerów, które mogą wewnętrznie używać SSE
>
> Ta lekcja została zaktualizowana, aby skupić się na **transporcie stdio**, który jest zalecanym rozwiązaniem dla większości implementacji serwera MCP.

Transport stdio umożliwia serwerom MCP komunikację z klientami poprzez standardowe strumienie wejścia i wyjścia. Jest to najczęściej używany i zalecany mechanizm transportu w obecnej specyfikacji MCP, zapewniający prosty i efektywny sposób budowania serwerów MCP, które można łatwo integrować z różnymi aplikacjami klienckimi.

## Przegląd

Ta lekcja omawia jak budować i korzystać z serwerów MCP używając transportu stdio.

## Cele nauki

Po zakończeniu tej lekcji będziesz potrafił:

- Zbudować serwer MCP używając transportu stdio.
- Debugować serwer MCP za pomocą Inspector.
- Korzystać z serwera MCP w Visual Studio Code.
- Zrozumieć obecne mechanizmy transportu MCP i dlaczego stdio jest zalecane.


## Transport stdio - jak to działa

Transport stdio jest jednym z dwóch standardowych transportów w specyfikacji MCP
`2026-07-28`. Oto jak to działa:

- **Prosta komunikacja**: serwer czyta komunikaty JSON-RPC ze standardowego wejścia (`stdin`) i wysyła komunikaty na standardowe wyjście (`stdout`).
- **Oparty na procesach**: klient uruchamia serwer MCP jako proces podrzędny.
- **Format komunikatów**: komunikaty to pojedyncze zapytania, powiadomienia lub odpowiedzi JSON-RPC, rozdzielone znakami nowej linii.
- **Logowanie**: serwer MOŻE zapisywać ciągi UTF-8 na standardowe wyjście błędów (`stderr`) w celu logowania.

### Kluczowe wymagania:
- Komunikaty MUSZĄ być rozdzielone znakami nowej linii i NIE MOGĄ zawierać wbudowanych znaków nowej linii
- Serwer NIE MOŻE pisać nic na `stdout` co nie jest prawidłowym komunikatem MCP
- Klient NIE MOŻE pisać nic do `stdin` serwera co nie jest prawidłowym komunikatem MCP

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

W powyższym kodzie:

- Importujemy klasę `Server` oraz `StdioServerTransport` z MCP SDK
- Tworzymy instancję serwera z podstawową konfiguracją i możliwościami
- Tworzymy instancję `StdioServerTransport` i łączymy z serwerem, umożliwiając komunikację przez stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Utwórz instancję serwera
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

W powyższym kodzie:

- Tworzymy instancję serwera używając MCP SDK
- Definiujemy narzędzia za pomocą dekoratorów
- Używamy menedżera kontekstu stdio_server do obsługi transportu

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Kluczowa różnica względem SSE jest taka, że serwery stdio:

- Nie wymagają konfiguracji serwera WWW ani punktów końcowych HTTP
- Są uruchamiane jako procesy podrzędne przez klienta
- Komunikują się za pomocą strumieni stdin/stdout
- Są prostsze do implementacji i debugowania

## Ćwiczenie: Tworzenie serwera stdio

Aby stworzyć nasz serwer, musimy pamiętać o dwóch rzeczach:

- Musimy użyć serwera WWW do udostępnienia punktów końcowych dla połączeń i komunikatów.
## Laboratorium: Tworzenie prostego serwera MCP stdio

W tym laboratorium stworzymy prosty serwer MCP używając zalecanego transportu stdio. Serwer będzie udostępniał narzędzia, które klienci mogą wywoływać korzystając ze standardowego Model Context Protocol.

### Wymagania wstępne

- Python 3.8 lub nowszy
- MCP Python SDK: `pip install mcp`
- Podstawowa znajomość programowania asynchronicznego

Zacznijmy od stworzenia naszego pierwszego serwera MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfiguruj logowanie
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Utwórz serwer
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Użyj transportu stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Kluczowe różnice względem wycofanego podejścia SSE

**Transport stdio (obecny standard):**
- Prosty model procesu podrzędnego - klient uruchamia serwer jako proces potomny
- Komunikacja przez stdin/stdout za pomocą komunikatów JSON-RPC
- Brak konieczności konfiguracji serwera HTTP
- Lepsza wydajność i bezpieczeństwo
- Łatwiejsze debugowanie i rozwój

**Transport SSE (wycofany od MCP 2025-06-18):**
- Wymagany serwer HTTP z punktami końcowymi SSE
- Bardziej skomplikowana konfiguracja z infrastrukturą serwera WWW
- Dodatkowe wymagania bezpieczeństwa dla punktów końcowych HTTP
- Zastąpiony teraz przez Streamable HTTP dla scenariuszy webowych

### Tworzenie serwera z transportem stdio

Aby stworzyć nasz serwer stdio, musimy:

1. **Zaimportować wymagane biblioteki** - potrzebujemy komponentów serwera MCP oraz transportu stdio
2. **Stworzyć instancję serwera** - zdefiniować serwer z jego możliwościami
3. **Zdefiniować narzędzia** - dodać funkcjonalności, które chcemy udostępnić
4. **Skonfigurować transport** - ustawić komunikację stdio
5. **Uruchomić serwer** - wystartować serwer i obsługiwać komunikaty

Budujmy to krok po kroku:

### Krok 1: Stwórz podstawowy serwer stdio

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Skonfiguruj logowanie
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Utwórz serwer
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Krok 2: Dodaj więcej narzędzi

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Krok 3: Uruchamianie serwera

Zapisz kod jako `server.py` i uruchom go z linii poleceń:

```bash
python server.py
```

Serwer rozpocznie działanie i będzie czekał na dane z stdin. Komunikuje się za pomocą komunikatów JSON-RPC przez transport stdio.

### Krok 4: Testowanie z Inspector

Możesz przetestować swój serwer za pomocą MCP Inspector:

1. Zainstaluj Inspector: `npx @modelcontextprotocol/inspector`
2. Uruchom Inspector i wskaż go na swój serwer
3. Testuj stworzone narzędzia

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debugowanie twojego serwera stdio

### Użycie MCP Inspector

MCP Inspector to cenne narzędzie do debugowania i testowania serwerów MCP. Oto jak używać go z twoim serwerem stdio:

1. **Zainstaluj Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Uruchom Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testuj swój serwer**: Inspector oferuje interfejs webowy, gdzie możesz:
   - Przeglądać możliwości serwera
   - Testować narzędzia z różnymi parametrami
   - Monitorować komunikaty JSON-RPC
   - Debugować problemy z połączeniem

### Użycie VS Code

Możesz też debugować serwer MCP bezpośrednio w VS Code:

1. Stwórz konfigurację uruchamiania w `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Ustaw punkty przerwania w kodzie serwera
3. Uruchom debuger i testuj z Inspector

### Typowe wskazówki dotyczące debugowania

- Używaj `stderr` do logowania - nigdy nie pisz do `stdout`, bo jest zarezerwowane dla komunikatów MCP
- Upewnij się, że wszystkie komunikaty JSON-RPC są oddzielone znakami nowej linii
- Testuj najpierw proste narzędzia zanim dodasz złożoną funkcjonalność
- Używaj Inspector do weryfikacji formatu komunikatów

## Konsumpcja twojego serwera stdio w VS Code


Po zbudowaniu serwera MCP stdio możesz go zintegrować z VS Code, aby używać go z Claude lub innymi klientami kompatybilnymi z MCP.

### Konfiguracja

1. **Utwórz plik konfiguracyjny MCP** w `%APPDATA%\Claude\claude_desktop_config.json` (Windows) lub `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Uruchom ponownie Claude**: Zamknij i ponownie otwórz Claude, aby załadować nową konfigurację serwera.

3. **Przetestuj połączenie**: Zacznij rozmowę z Claude i spróbuj użyć narzędzi swojego serwera:
   - "Czy możesz mnie przywitać, korzystając z narzędzia powitania?"
   - "Oblicz sumę 15 i 27"
   - "Jakie są informacje o serwerze?"

### Przykład serwera stdio w TypeScript

Oto kompletne przykładowe rozwiązanie w TypeScript do referencji:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Dodaj narzędzia
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Przykład serwera stdio w .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Podsumowanie

W tej zaktualizowanej lekcji nauczyłeś się:

- Budować serwery MCP używając aktualnego **transportu stdio** (zalecany sposób)
- Rozumieć, dlaczego transport SSE został wycofany na rzecz stdio i Streamable HTTP
- Tworzyć narzędzia wywoływane przez klientów MCP
- Debugować swój serwer przy użyciu MCP Inspector
- Integrować serwer stdio z VS Code i Claude

Transport stdio zapewnia prostszy, bezpieczniejszy i wydajniejszy sposób budowy serwerów MCP w porównaniu z wycofanym rozwiązaniem SSE. Jest to zalecany transport dla większości implementacji serwerów MCP zgodnie ze specyfikacją z 2025-06-18.


### .NET

1. Najpierw stwórzmy kilka narzędzi, w tym celu utworzymy plik *Tools.cs* z następującą zawartością:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Ćwiczenie: Testowanie serwera stdio

Teraz, gdy zbudowałeś swój serwer stdio, przetestuj go, aby upewnić się, że działa poprawnie.

### Wymagania wstępne

1. Upewnij się, że masz zainstalowany MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Kod serwera powinien być zapisany (np. jako `server.py`)

### Testowanie z Inspector

1. **Uruchom Inspector z Twoim serwerem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otwórz interfejs WWW**: Inspector otworzy okno przeglądarki pokazujące możliwości Twojego serwera.

3. **Testuj narzędzia**: 
   - Wypróbuj narzędzie `get_greeting` z różnymi imionami
   - Przetestuj narzędzie `calculate_sum` z różnymi liczbami
   - Wywołaj narzędzie `get_server_info`, aby zobaczyć metadane serwera

4. **Monitoruj komunikację**: Inspector pokazuje wiadomości JSON-RPC wymieniane między klientem a serwerem.

### Co powinieneś zobaczyć

Gdy Twój serwer wystartuje poprawnie, powinieneś zobaczyć:
- Możliwości serwera wymienione w Inspectorze
- Dostępne narzędzia do testowania
- Udane wymiany wiadomości JSON-RPC
- Odpowiedzi narzędzi wyświetlone w interfejsie

### Typowe problemy i rozwiązania

**Serwer się nie uruchamia:**
- Sprawdź, czy wszystkie zależności są zainstalowane: `pip install mcp`
- Zweryfikuj składnię i wcięcia w Pythonie
- Poszukaj komunikatów o błędach w konsoli

**Narzędzia się nie pojawiają:**
- Upewnij się, że dekoratory `@server.tool()` są obecne
- Sprawdź, czy funkcje narzędzi są zdefiniowane przed `main()`
- Zweryfikuj, że serwer jest poprawnie skonfigurowany

**Problemy z połączeniem:**
- Upewnij się, że serwer używa prawidłowo transportu stdio
- Sprawdź, że inne procesy nie zakłócają działania
- Zweryfikuj składnię poleceń Inspector

## Zadanie

Spróbuj rozbudować swój serwer o więcej możliwości. Zobacz [tę stronę](https://api.chucknorris.io/), aby na przykład dodać narzędzie wywołujące API. Ty decydujesz, jak powinien wyglądać serwer. Powodzenia :)
## Rozwiązanie

[Rozwiązanie](./solution/README.md) Oto możliwe rozwiązanie z działającym kodem.

## Kluczowe wnioski

Kluczowe wnioski z tego rozdziału to:

- Transport stdio jest zalecanym mechanizmem dla lokalnych serwerów MCP.
- Transport stdio pozwala na płynną komunikację między serwerami MCP a klientami poprzez standardowe strumienie wejścia i wyjścia.
- Możesz używać zarówno Inspector, jak i Visual Studio Code do bezpośredniej obsługi serwerów stdio, co ułatwia debugowanie i integrację.

## Przykłady 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Dodatkowe zasoby

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Co dalej

## Kolejne kroki

Teraz, kiedy nauczyłeś się budować serwery MCP z transportem stdio, możesz poznać bardziej zaawansowane tematy:

- **Dalej**: [HTTP Streaming z MCP (Streamable HTTP)](../06-http-streaming/README.md) - Poznaj inny obsługiwany mechanizm transportowy dla serwerów zdalnych
- **Zaawansowane**: [Najlepsze praktyki bezpieczeństwa MCP](../../02-Security/README.md) - Zaimplementuj bezpieczeństwo w swoich serwerach MCP
- **Produkcyjne**: [Strategie wdrażania](../09-deployment/README.md) - Wdróż swoje serwery do użycia produkcyjnego

## Dodatkowe zasoby

- [Specyfikacja MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Aktualna specyfikacja
- [Dokumentacja MCP SDK](https://github.com/modelcontextprotocol/sdk) - Odniesienia SDK dla wszystkich języków
- [Przykłady społeczności](../../06-CommunityContributions/README.md) - Więcej przykładów serwerów od społeczności

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->