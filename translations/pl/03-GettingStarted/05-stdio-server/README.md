# Serwer MCP z transportem stdio

> **⚠️ Ważna aktualizacja**: Od specyfikacji MCP z dnia 2025-06-18, samodzielny transport SSE (Server-Sent Events) został **wycofany** i zastąpiony przez transport „Streamable HTTP”. Obecna specyfikacja MCP definiuje dwa główne mechanizmy transportu:
> 1. **stdio** - standardowe wejście/wyjście (zalecane dla serwerów lokalnych)
> 2. **Streamable HTTP** - dla serwerów zdalnych, które mogą używać SSE wewnętrznie
>
> Ta lekcja została zaktualizowana, aby skupić się na **transporcie stdio**, który jest zalecanym podejściem dla większości implementacji serwerów MCP.

Transport stdio pozwala serwerom MCP komunikować się z klientami poprzez standardowe strumienie wejścia i wyjścia. Jest to najczęściej używany i zalecany mechanizm transportowy w obecnej specyfikacji MCP, zapewniający prosty i efektywny sposób budowy serwerów MCP, które mogą być łatwo integrowane z różnymi aplikacjami klienckimi.

## Przegląd

Ta lekcja omawia, jak tworzyć i korzystać z serwerów MCP wykorzystujących transport stdio.

## Cele nauki

Po zakończeniu tej lekcji będziesz potrafił:

- Zbudować serwer MCP z użyciem transportu stdio.
- Debugować serwer MCP za pomocą Inspektora.
- Korzystać z serwera MCP w Visual Studio Code.
- Zrozumieć obecne mechanizmy transportu MCP i dlaczego stdio jest rekomendowane.

## Transport stdio – jak to działa

Transport stdio jest jednym z dwóch obsługiwanych typów transportu w obecnej specyfikacji MCP (2025-06-18). Oto jak to działa:

- **Prosta komunikacja**: Serwer odczytuje wiadomości JSON-RPC ze standardowego wejścia (`stdin`) i wysyła wiadomości na standardowe wyjście (`stdout`).
- **Procesowy model**: Klient uruchamia serwer MCP jako proces potomny.
- **Format wiadomości**: Wiadomości to pojedyncze żądania, powiadomienia lub odpowiedzi JSON-RPC, rozdzielone znakami nowej linii.
- **Logowanie**: Serwer MOŻE pisać ciągi UTF-8 do standardowego błędu (`stderr`) w celach logowania.

### Kluczowe wymagania:
- Wiadomości MUSZĄ być rozdzielone znakami nowej linii i NIE MOGĄ zawierać osadzonych nowych linii
- Serwer NIE MOŻE pisać do `stdout` niczego, co nie jest ważną wiadomością MCP
- Klient NIE MOŻE pisać do `stdin` serwera niczego, co nie jest ważną wiadomością MCP

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
- Tworzymy instancję `StdioServerTransport` i łączymy z nią serwer, umożliwiając komunikację poprzez stdin/stdout

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
- Używamy kontekstowego menedżera stdio_server do obsługi transportu

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

Kluczowa różnica względem SSE polega na tym, że serwery stdio:

- Nie wymagają konfiguracji serwera WWW ani punktów końcowych HTTP
- Są uruchamiane jako procesy podrzędne przez klienta
- Komunikują się przez strumienie stdin/stdout
- Są prostsze do implementacji i debugowania

## Ćwiczenie: Tworzenie serwera stdio

Aby stworzyć nasz serwer, musimy pamiętać o dwóch rzeczach:

- Potrzebujemy użyć serwera WWW do udostępniania punktów końcowych do połączenia i wymiany wiadomości.

## Laboratorium: Tworzenie prostego serwera MCP stdio

W tym laboratorium stworzymy prosty serwer MCP korzystający z zalecanego transportu stdio. Serwer ten udostępni narzędzia, które klienci mogą wywoływać za pomocą standardowego protokołu Model Context Protocol.

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

# Skonfiguruj logowanie
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

## Kluczowe różnice w stosunku do wycofanego podejścia SSE

**Transport stdio (aktualny standard):**
- Prosty model procesu potomnego – klient uruchamia serwer jako proces potomny
- Komunikacja przez stdin/stdout za pomocą wiadomości JSON-RPC
- Nie wymaga konfiguracji serwera HTTP
- Lepsza wydajność i bezpieczeństwo
- Łatwiejsze debugowanie i rozwój

**Transport SSE (wycofany od MCP 2025-06-18):**
- Wymagał serwera HTTP z punktami końcowymi SSE
- Bardziej skomplikowana konfiguracja z infrastrukturą serwera WWW
- Dodatkowe kwestie bezpieczeństwa dotyczące punktów HTTP
- Zastąpiony teraz przez Streamable HTTP dla scenariuszy webowych

### Tworzenie serwera z transportem stdio

Aby stworzyć nasz serwer stdio, musimy:

1. **Zaimportować wymagane biblioteki** – potrzebujemy komponentów serwera MCP i transportu stdio
2. **Utworzyć instancję serwera** – zdefiniować serwer i jego możliwości
3. **Zdefiniować narzędzia** – dodać funkcjonalności, które chcemy udostępnić
4. **Skonfigurować transport** – ustawić komunikację stdio
5. **Uruchomić serwer** – rozpocząć działanie serwera i obsługę wiadomości

Budujmy to krok po kroku:

### Krok 1: Utwórz podstawowy serwer stdio

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

### Krok 3: Uruchom serwer

Zapisz kod jako `server.py` i uruchom go z linii poleceń:

```bash
python server.py
```

Serwer wystartuje i będzie oczekiwał na dane z stdin. Komunikuje się za pomocą wiadomości JSON-RPC przez transport stdio.

### Krok 4: Testowanie za pomocą Inspektora

Możesz przetestować swój serwer używając MCP Inspector:

1. Zainstaluj Inspektora: `npx @modelcontextprotocol/inspector`
2. Uruchom Inspektora i wskaż go na swój serwer
3. Testuj utworzone narzędzia

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debugowanie serwera stdio

### Używanie MCP Inspektora

MCP Inspector to wartościowe narzędzie do debugowania i testowania serwerów MCP. Oto jak z niego korzystać z serwerem stdio:

1. **Zainstaluj Inspektora**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Uruchom Inspektora**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testuj serwer**: Inspektor oferuje interfejs webowy, gdzie możesz:
   - Przeglądać możliwości serwera
   - Testować narzędzia z różnymi parametrami
   - Monitorować wiadomości JSON-RPC
   - Debugować problemy z połączeniem

### Używanie VS Code

Możesz również debugować serwer MCP bezpośrednio w VS Code:

1. Utwórz konfigurację uruchamiania w `.vscode/launch.json`:
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
3. Uruchom debugger i testuj za pomocą Inspektora

### Typowe wskazówki debugowania

- Używaj `stderr` do logowania - nigdy nie pisz na `stdout`, ponieważ jest zarezerwowany dla wiadomości MCP
- Upewnij się, że wszystkie wiadomości JSON-RPC są rozdzielone nowymi liniami
- Najpierw testuj proste narzędzia, zanim dodasz bardziej skomplikowaną funkcjonalność
- Użyj Inspektora, aby zweryfikować format wiadomości

## Konsumpcja serwera stdio w VS Code

Gdy zbudujesz swój serwer MCP stdio, możesz go zintegrować z VS Code, aby używać go z Claude lub innymi klientami kompatybilnymi z MCP.

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

2. **Zrestartuj Claude**: Zamknij i otwórz ponownie Claude, aby wczytać nową konfigurację serwera.

3. **Przetestuj połączenie**: Rozpocznij rozmowę z Claude i spróbuj użyć narzędzi swojego serwera:
   - „Czy możesz powitać mnie za pomocą narzędzia greeting?”
   - „Oblicz sumę 15 i 27”
   - „Jakie są informacje o serwerze?”

### Przykład serwera stdio w TypeScript

Oto kompletny przykład w TypeScript do odniesienia:

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

- Budować serwery MCP używając obecnego **transportu stdio** (zalecane podejście)
- Zrozumieć, dlaczego transport SSE został wycofany na rzecz stdio i Streamable HTTP
- Tworzyć narzędzia, które mogą wywoływać klienci MCP
- Debugować serwer za pomocą MCP Inspectora
- Integrować serwer stdio z VS Code i Claude

Transport stdio zapewnia prostszy, bezpieczniejszy i bardziej wydajny sposób tworzenia serwerów MCP w porównaniu do wycofanego podejścia SSE. Jest to zalecany transport dla większości implementacji serwerów MCP według specyfikacji z dnia 2025-06-18.

### .NET

1. Najpierw stwórzmy narzędzia, do tego stworzymy plik *Tools.cs* z następującą zawartością:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Ćwiczenie: Testowanie swojego serwera stdio

Po zbudowaniu serwera stdio, przetestujmy go, aby upewnić się, że działa poprawnie.

### Wymagania wstępne

1. Upewnij się, że masz zainstalowany MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Twój kod serwera powinien być zapisany (np. jako `server.py`)

### Testowanie za pomocą Inspektora

1. **Uruchom Inspektora z twoim serwerem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otwórz interfejs webowy**: Inspektor otworzy okno przeglądarki pokazujące możliwości twojego serwera.

3. **Testuj narzędzia**:
   - Wypróbuj narzędzie `get_greeting` z różnymi imionami
   - Testuj narzędzie `calculate_sum` z różnymi liczbami
   - Wywołaj narzędzie `get_server_info`, aby zobaczyć metadane serwera

4. **Monitoruj komunikację**: Inspektor pokazuje wymianę wiadomości JSON-RPC między klientem a serwerem.

### Co powinieneś zobaczyć

Gdy serwer uruchomi się poprawnie, powinieneś zobaczyć:
- Możliwości serwera wyświetlone w Inspektorze
- Narzędzia dostępne do testowania
- Udane wymiany wiadomości JSON-RPC
- Odpowiedzi narzędzi widoczne w interfejsie

### Typowe problemy i rozwiązania

**Serwer nie startuje:**
- Sprawdź, czy wszystkie zależności są zainstalowane: `pip install mcp`
- Zweryfikuj składnię i wcięcia w Pythonie
- Sprawdź komunikaty o błędach w konsoli

**Brak narzędzi:**
- Upewnij się, że obecne są dekoratory `@server.tool()`
- Sprawdź, czy funkcje narzędzi są zdefiniowane przed funkcją `main()`
- Sprawdź poprawność konfiguracji serwera

**Problemy z połączeniem:**
- Upewnij się, że serwer używa transportu stdio poprawnie
- Sprawdź, czy nie kolidują inne procesy
- Zweryfikuj składnię polecenia Inspektora

## Zadanie

Spróbuj rozbudować serwer o więcej funkcjonalności. Zobacz [tę stronę](https://api.chucknorris.io/), aby na przykład dodać narzędzie wywołujące API. Ty decydujesz, jak ma wyglądać serwer. Powodzenia :)
## Rozwiązanie

[Rozwiązanie](./solution/README.md) Oto możliwe rozwiązanie z działającym kodem.

## Najważniejsze wnioski

Najważniejsze wnioski z tego rozdziału to:

- Transport stdio jest zalecanym mechanizmem dla lokalnych serwerów MCP.
- Transport stdio umożliwia płynną komunikację między serwerami MCP i klientami za pomocą standardowych strumieni wejścia i wyjścia.
- Możesz używać zarówno Inspektora, jak i Visual Studio Code do bezpośredniej konsumpcji serwerów stdio, co ułatwia debugowanie i integrację.

## Przykłady

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)

## Dodatkowe zasoby

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Co dalej

## Następne kroki

Teraz, gdy nauczyłeś się budować serwery MCP z transportem stdio, możesz zgłębić bardziej zaawansowane tematy:

- **Dalej**: [HTTP Streaming z MCP (Streamable HTTP)](../06-http-streaming/README.md) – Poznaj drugi obsługiwany mechanizm transportu dla serwerów zdalnych
- **Zaawansowane**: [Najlepsze praktyki bezpieczeństwa MCP](../../02-Security/README.md) – Wdrażaj zabezpieczenia w swoich serwerach MCP
- **Produkcja**: [Strategie wdrażania](../09-deployment/README.md) – Wdrażaj serwery do użytku produkcyjnego

## Dodatkowe zasoby

- [Specyfikacja MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Oficjalna specyfikacja
- [Dokumentacja MCP SDK](https://github.com/modelcontextprotocol/sdk) – Referencje SDK dla wszystkich języków
- [Przykłady społeczności](../../06-CommunityContributions/README.md) – Więcej przykładów serwerów od społeczności

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Dokument ten został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku rodzimym należy uważać za źródło wiarygodne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->