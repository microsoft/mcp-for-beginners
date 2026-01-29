# MCP Serwer z transportem stdio

> **⚠️ Ważna aktualizacja**: Od specyfikacji MCP z dnia 2025-06-18, samodzielny transport SSE (Server-Sent Events) został **wycofany** i zastąpiony transportem "Streamable HTTP". Obecna specyfikacja MCP definiuje dwa główne mechanizmy transportu:
> 1. **stdio** - Standardowe wejście/wyjście (zalecane dla lokalnych serwerów)
> 2. **Streamable HTTP** - Dla zdalnych serwerów, które mogą wewnętrznie korzystać z SSE
>
> Ta lekcja została zaktualizowana, aby skupić się na **transporcie stdio**, który jest zalecanym podejściem dla większości implementacji serwerów MCP.

Transport stdio umożliwia serwerom MCP komunikację z klientami za pomocą standardowych strumieni wejścia i wyjścia. Jest to najczęściej używany i zalecany mechanizm transportu w obecnej specyfikacji MCP, zapewniający prosty i efektywny sposób budowania serwerów MCP, które można łatwo zintegrować z różnymi aplikacjami klienckimi.

## Przegląd

Ta lekcja obejmuje budowanie i korzystanie z serwerów MCP przy użyciu transportu stdio.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Zbudować serwer MCP korzystający z transportu stdio.
- Debugować serwer MCP za pomocą Inspektora.
- Korzystać z serwera MCP w Visual Studio Code.
- Zrozumieć obecne mechanizmy transportu MCP i dlaczego stdio jest zalecane.

## Transport stdio - Jak to działa

Transport stdio jest jednym z dwóch obsługiwanych typów transportu w obecnej specyfikacji MCP (2025-06-18). Oto jak działa:

- **Prosta komunikacja**: Serwer odczytuje wiadomości JSON-RPC ze standardowego wejścia (`stdin`) i wysyła wiadomości na standardowe wyjście (`stdout`).
- **Procesowy model**: Klient uruchamia serwer MCP jako podproces.
- **Format wiadomości**: Wiadomości to pojedyncze żądania, powiadomienia lub odpowiedzi JSON-RPC, oddzielone znakami nowej linii.
- **Logowanie**: Serwer MOŻE zapisywać ciągi UTF-8 na standardowe wyjście błędów (`stderr`) w celu logowania.

### Kluczowe wymagania:
- Wiadomości MUSZĄ być oddzielone znakami nowej linii i NIE MOGĄ zawierać wbudowanych znaków nowej linii.
- Serwer NIE MOŻE zapisywać niczego na `stdout`, co nie jest prawidłową wiadomością MCP.
- Klient NIE MOŻE zapisywać niczego na `stdin` serwera, co nie jest prawidłową wiadomością MCP.

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
```

W powyższym kodzie:

- Importujemy klasę `Server` i `StdioServerTransport` z MCP SDK.
- Tworzymy instancję serwera z podstawową konfiguracją i funkcjonalnościami.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

- Tworzymy instancję serwera za pomocą MCP SDK.
- Definiujemy narzędzia za pomocą dekoratorów.
- Używamy kontekstu `stdio_server`, aby obsłużyć transport.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Kluczowa różnica w stosunku do SSE polega na tym, że serwery stdio:

- Nie wymagają konfiguracji serwera WWW ani punktów końcowych HTTP.
- Są uruchamiane jako podprocesy przez klienta.
- Komunikują się za pomocą strumieni stdin/stdout.
- Są prostsze w implementacji i debugowaniu.

## Ćwiczenie: Tworzenie serwera stdio

Aby stworzyć nasz serwer, musimy pamiętać o dwóch rzeczach:

- Musimy użyć serwera WWW, aby udostępnić punkty końcowe dla połączeń i wiadomości.

## Laboratorium: Tworzenie prostego serwera MCP stdio

W tym laboratorium stworzymy prosty serwer MCP korzystający z zalecanego transportu stdio. Ten serwer udostępni narzędzia, które klienci mogą wywoływać za pomocą standardowego protokołu Model Context Protocol.

### Wymagania wstępne

- Python 3.8 lub nowszy.
- MCP Python SDK: `pip install mcp`.
- Podstawowa znajomość programowania asynchronicznego.

Zacznijmy od stworzenia naszego pierwszego serwera MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
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

**Transport stdio (obecny standard):**
- Prosty model podprocesów - klient uruchamia serwer jako proces potomny.
- Komunikacja za pomocą stdin/stdout przy użyciu wiadomości JSON-RPC.
- Brak potrzeby konfiguracji serwera HTTP.
- Lepsza wydajność i bezpieczeństwo.
- Łatwiejsze debugowanie i rozwój.

**Transport SSE (wycofany od MCP 2025-06-18):**
- Wymagał serwera HTTP z punktami końcowymi SSE.
- Bardziej skomplikowana konfiguracja z infrastrukturą serwera WWW.
- Dodatkowe kwestie bezpieczeństwa dla punktów końcowych HTTP.
- Zastąpiony przez Streamable HTTP dla scenariuszy opartych na sieci.

### Tworzenie serwera z transportem stdio

Aby stworzyć nasz serwer stdio, musimy:

1. **Zaimportować wymagane biblioteki** - Potrzebujemy komponentów serwera MCP i transportu stdio.
2. **Stworzyć instancję serwera** - Zdefiniować serwer z jego funkcjonalnościami.
3. **Zdefiniować narzędzia** - Dodać funkcjonalności, które chcemy udostępnić.
4. **Skonfigurować transport** - Ustawić komunikację stdio.
5. **Uruchomić serwer** - Wystartować serwer i obsłużyć wiadomości.

Zbudujmy to krok po kroku:

### Krok 1: Stwórz podstawowy serwer stdio

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

Zapisz kod jako `server.py` i uruchom go z wiersza poleceń:

```bash
python server.py
```

Serwer wystartuje i będzie czekał na dane wejściowe ze stdin. Komunikuje się za pomocą wiadomości JSON-RPC przez transport stdio.

### Krok 4: Testowanie za pomocą Inspektora

Możesz przetestować swój serwer za pomocą MCP Inspector:

1. Zainstaluj Inspektora: `npx @modelcontextprotocol/inspector`.
2. Uruchom Inspektora i wskaż go na swój serwer.
3. Przetestuj narzędzia, które stworzyłeś.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Debugowanie serwera stdio

### Korzystanie z MCP Inspector

MCP Inspector to wartościowe narzędzie do debugowania i testowania serwerów MCP. Oto jak go używać z serwerem stdio:

1. **Zainstaluj Inspektora**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Uruchom Inspektora**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Przetestuj swój serwer**: Inspektor oferuje interfejs webowy, w którym możesz:
   - Zobaczyć możliwości serwera.
   - Testować narzędzia z różnymi parametrami.
   - Monitorować wiadomości JSON-RPC.
   - Debugować problemy z połączeniem.

### Korzystanie z VS Code

Możesz również debugować swój serwer MCP bezpośrednio w VS Code:

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

2. Ustaw punkty przerwania w kodzie serwera.
3. Uruchom debugger i testuj za pomocą Inspektora.

### Wskazówki dotyczące debugowania

- Używaj `stderr` do logowania - nigdy nie zapisuj na `stdout`, ponieważ jest zarezerwowane dla wiadomości MCP.
- Upewnij się, że wszystkie wiadomości JSON-RPC są oddzielone znakami nowej linii.
- Testuj najpierw proste narzędzia, zanim dodasz bardziej złożoną funkcjonalność.
- Używaj Inspektora do weryfikacji formatów wiadomości.

## Korzystanie z serwera stdio w VS Code

Po zbudowaniu serwera MCP stdio możesz zintegrować go z VS Code, aby używać go z Claude lub innymi klientami zgodnymi z MCP.

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

3. **Przetestuj połączenie**: Rozpocznij rozmowę z Claude i spróbuj użyć narzędzi serwera:
   - "Czy możesz mnie przywitać za pomocą narzędzia powitania?"
   - "Oblicz sumę 15 i 27."
   - "Jakie są informacje o serwerze?"

### Przykład serwera stdio w TypeScript

Oto kompletny przykład w TypeScript dla odniesienia:

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

// Add tools
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
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Podsumowanie

W tej zaktualizowanej lekcji nauczyłeś się:

- Budować serwery MCP korzystające z obecnego **transportu stdio** (zalecane podejście).
- Zrozumieć, dlaczego transport SSE został wycofany na rzecz stdio i Streamable HTTP.
- Tworzyć narzędzia, które mogą być wywoływane przez klientów MCP.
- Debugować swój serwer za pomocą MCP Inspector.
- Zintegrować swój serwer stdio z VS Code i Claude.

Transport stdio zapewnia prostszy, bardziej bezpieczny i wydajny sposób budowania serwerów MCP w porównaniu do wycofanego podejścia SSE. Jest to zalecany transport dla większości implementacji serwerów MCP zgodnie ze specyfikacją z dnia 2025-06-18.

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

2. Kod serwera powinien być zapisany (np. jako `server.py`).

### Testowanie za pomocą Inspektora

1. **Uruchom Inspektora ze swoim serwerem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otwórz interfejs webowy**: Inspektor otworzy okno przeglądarki pokazujące możliwości twojego serwera.

3. **Przetestuj narzędzia**: 
   - Wypróbuj narzędzie `get_greeting` z różnymi nazwami.
   - Przetestuj narzędzie `calculate_sum` z różnymi liczbami.
   - Wywołaj narzędzie `get_server_info`, aby zobaczyć metadane serwera.

4. **Monitoruj komunikację**: Inspektor pokazuje wiadomości JSON-RPC wymieniane między klientem a serwerem.

### Co powinieneś zobaczyć

Gdy serwer uruchomi się poprawnie, powinieneś zobaczyć:
- Możliwości serwera wymienione w Inspektorze.
- Narzędzia dostępne do testowania.
- Udane wymiany wiadomości JSON-RPC.
- Odpowiedzi narzędzi wyświetlane w interfejsie.

### Typowe problemy i rozwiązania

**Serwer nie uruchamia się:**
- Sprawdź, czy wszystkie zależności są zainstalowane: `pip install mcp`.
- Zweryfikuj składnię Pythona i wcięcia.
- Poszukaj komunikatów o błędach w konsoli.

**Narzędzia nie pojawiają się:**
- Upewnij się, że dekoratory `@server.tool()` są obecne.
- Sprawdź, czy funkcje narzędzi są zdefiniowane przed `main()`.
- Zweryfikuj, czy serwer jest poprawnie skonfigurowany.

**Problemy z połączeniem:**
- Upewnij się, że serwer poprawnie korzysta z transportu stdio.
- Sprawdź, czy żadne inne procesy nie zakłócają działania.
- Zweryfikuj składnię polecenia Inspektora.

## Zadanie

Spróbuj rozbudować swój serwer o więcej funkcjonalności. Zobacz [tę stronę](https://api.chucknorris.io/), aby na przykład dodać narzędzie, które wywołuje API. Ty decydujesz, jak powinien wyglądać serwer. Miłej zabawy :)

## Rozwiązanie

[Rozwiązanie](./solution/README.md) Oto możliwe rozwiązanie z działającym kodem.

## Kluczowe wnioski

Kluczowe wnioski z tego rozdziału to:

- Transport stdio jest zalecanym mechanizmem dla lokalnych serwerów MCP.
- Transport stdio umożliwia płynną komunikację między serwerami MCP a klientami za pomocą standardowych strumieni wejścia i wyjścia.
- Możesz używać zarówno Inspektora, jak i Visual Studio Code do bezpośredniego korzystania z serwerów stdio, co ułatwia debugowanie i integrację.

## Przykłady 

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python) 

## Dodatkowe zasoby

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Co dalej

## Następne kroki

Teraz, gdy nauczyłeś się budować serwery MCP z transportem stdio, możesz zgłębić bardziej zaawansowane tematy:

- **Następne**: [HTTP Streaming z MCP (Streamable HTTP)](../06-http-streaming/README.md) - Dowiedz się o drugim obsługiwanym mechanizmie transportu dla zdalnych serwerów.
- **Zaawansowane**: [Najlepsze praktyki bezpieczeństwa MCP](../../02-Security/README.md) - Zaimplementuj bezpieczeństwo w swoich serwerach MCP.
- **Produkcja**: [Strategie wdrażania](../09-deployment/README.md) - Wdrażaj swoje serwery do użytku produkcyjnego.

## Dodatkowe zasoby

- [Specyfikacja MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Oficjalna specyfikacja.
- [Dokumentacja MCP SDK](https://github.com/modelcontextprotocol/sdk) - Dokumentacja SDK dla wszystkich języków.
- [Przykłady społeczności](../../06-CommunityContributions/README.md) - Więcej przykładów serwerów od społeczności.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.