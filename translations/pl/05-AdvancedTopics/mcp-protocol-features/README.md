# Głębokie Zanurzenie w Funkcje Protokołu MCP

Ten przewodnik bada zaawansowane funkcje protokołu MCP, które wykraczają poza podstawową obsługę narzędzi i zasobów. Zrozumienie tych funkcji pomaga w budowie mocniejszych, przyjaznych dla użytkownika i produkcyjnie gotowych serwerów MCP.

> **Zakres MCP `2026-07-28`:** uruchamianie i zamykanie procesu serwera pozostają
> kwestiami aplikacji, ale protokolarna inicjalizacja MCP i sesje na poziomie protokołu
> zostały usunięte. Poniższa sekcja Logowania jest zachowana dla starych
> implementacji; nowe serwery powinny korzystać z `stderr` lub OpenTelemetry. Tasks to
> teraz osobno wersjonowane rozszerzenie. Zobacz
> [Co się zmieniło w MCP: Specyfikacja 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

## Omówione Funkcje

1. **Powiadomienia o Postępie** - raportowanie postępu dla długotrwałych operacji
2. **Anulowanie Żądań** - umożliwienie klientom anulowania trwających żądań
3. **Szablony Zasobów** - dynamiczne URI zasobów z parametrami
4. **Cykl Życia Aplikacji** - uruchamianie i zamykanie procesu serwera
5. **Kontrola Logowania (Legacy)** - przestarzała konfiguracja rejestrowania MCP
6. **Wzorce Obsługi Błędów** - spójne odpowiedzi błędów

---

## 1. Powiadomienia o Postępie

Dla operacji, które zajmują czas (przetwarzanie danych, pobieranie plików, wywołania API), powiadomienia o postępie informują użytkowników.

### Jak to działa

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: tools/call (długotrwała operacja)
    Server-->>Client: powiadomienie: postęp 10%
    Server-->>Client: powiadomienie: postęp 50%
    Server-->>Client: powiadomienie: postęp 90%
    Server->>Client: wynik (ukończono)
```

### Implementacja w Python

```python
from mcp.server import Server, NotificationOptions
from mcp.types import ProgressNotification
import asyncio

app = Server("progress-server")

@app.tool()
async def process_large_file(file_path: str, ctx) -> str:
    """Process a large file with progress updates."""
    
    # Pobierz rozmiar pliku do obliczania postępu
    file_size = os.path.getsize(file_path)
    processed = 0
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            # Przetwórz fragment
            await process_chunk(chunk)
            processed += len(chunk)
            
            # Wyślij powiadomienie o postępie
            progress = (processed / file_size) * 100
            await ctx.send_notification(
                ProgressNotification(
                    progressToken=ctx.request_id,
                    progress=progress,
                    total=100,
                    message=f"Processing: {progress:.1f}%"
                )
            )
    
    return f"Processed {file_size} bytes"

@app.tool()
async def batch_operation(items: list[str], ctx) -> str:
    """Process multiple items with progress."""
    
    results = []
    total = len(items)
    
    for i, item in enumerate(items):
        result = await process_item(item)
        results.append(result)
        
        # Raportuj postęp po każdym elemencie
        await ctx.send_notification(
            ProgressNotification(
                progressToken=ctx.request_id,
                progress=i + 1,
                total=total,
                message=f"Processed {i + 1}/{total}: {item}"
            )
        )
    
    return f"Completed {total} items"
```

### Implementacja w TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

server.setRequestHandler(CallToolSchema, async (request, extra) => {
  const { name, arguments: args } = request.params;
  
  if (name === "process_data") {
    const items = args.items as string[];
    const results = [];
    
    for (let i = 0; i < items.length; i++) {
      const result = await processItem(items[i]);
      results.push(result);
      
      // Wyślij powiadomienie o postępie
      await extra.sendNotification({
        method: "notifications/progress",
        params: {
          progressToken: request.id,
          progress: i + 1,
          total: items.length,
          message: `Processing item ${i + 1}/${items.length}`
        }
      });
    }
    
    return { content: [{ type: "text", text: JSON.stringify(results) }] };
  }
});
```

### Obsługa Klienta (Python)

```python
async def handle_progress(notification):
    """Handle progress notifications from server."""
    params = notification.params
    print(f"Progress: {params.progress}/{params.total} - {params.message}")

# Rejestracja obsługi
session.on_notification("notifications/progress", handle_progress)

# Wywołaj narzędzie (aktualizacje postępu będą przychodzić przez obsługę)
result = await session.call_tool("process_large_file", {"file_path": "/data/large.csv"})
```

---

## 2. Anulowanie Żądań

Pozwól klientom na anulowanie żądań, które nie są już potrzebne lub trwają zbyt długo.

### Implementacja w Python

```python
from mcp.server import Server
from mcp.types import CancelledError
import asyncio

app = Server("cancellable-server")

@app.tool()
async def long_running_search(query: str, ctx) -> str:
    """Search that can be cancelled."""
    
    results = []
    
    try:
        for page in range(100):  # Przeszukaj wiele stron
            # Sprawdź, czy anulowanie zostało zażądane
            if ctx.is_cancelled:
                raise CancelledError("Search cancelled by user")
            
            # Symuluj wyszukiwanie na stronie
            page_results = await search_page(query, page)
            results.extend(page_results)
            
            # Krótkie opóźnienie pozwala na sprawdzanie anulowania
            await asyncio.sleep(0.1)
            
    except CancelledError:
        # Zwróć częściowe wyniki
        return f"Cancelled. Found {len(results)} results before cancellation."
    
    return f"Found {len(results)} total results"

@app.tool()
async def download_file(url: str, ctx) -> str:
    """Download with cancellation support."""
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            chunks = []
            
            async for chunk in response.content.iter_chunked(8192):
                if ctx.is_cancelled:
                    return f"Download cancelled at {downloaded}/{total_size} bytes"
                
                chunks.append(chunk)
                downloaded += len(chunk)
            
            return f"Downloaded {downloaded} bytes"
```

### Implementacja Kontekstu Anulowania

```python
class CancellableContext:
    """Context object that tracks cancellation state."""
    
    def __init__(self, request_id: str):
        self.request_id = request_id
        self._cancelled = asyncio.Event()
        self._cancel_reason = None
    
    @property
    def is_cancelled(self) -> bool:
        return self._cancelled.is_set()
    
    def cancel(self, reason: str = "Cancelled"):
        self._cancel_reason = reason
        self._cancelled.set()
    
    async def check_cancelled(self):
        """Raise if cancelled, otherwise continue."""
        if self.is_cancelled:
            raise CancelledError(self._cancel_reason)
    
    async def sleep_or_cancel(self, seconds: float):
        """Sleep that can be interrupted by cancellation."""
        try:
            await asyncio.wait_for(
                self._cancelled.wait(),
                timeout=seconds
            )
            raise CancelledError(self._cancel_reason)
        except asyncio.TimeoutError:
            pass  # Normalny limit czasu, kontynuuj
```

### Anulowanie po stronie klienta

```python
import asyncio

async def search_with_timeout(session, query, timeout=30):
    """Search with automatic cancellation on timeout."""
    
    task = asyncio.create_task(
        session.call_tool("long_running_search", {"query": query})
    )
    
    try:
        result = await asyncio.wait_for(task, timeout=timeout)
        return result
    except asyncio.TimeoutError:
        # Żądanie anulowania
        await session.send_notification({
            "method": "notifications/cancelled",
            "params": {"requestId": task.request_id, "reason": "Timeout"}
        })
        return "Search timed out"
```

---

## 3. Szablony Zasobów

Szablony zasobów pozwalają na dynamiczne tworzenie URI z parametrami, co jest przydatne dla API i baz danych.

### Definiowanie Szablonów

```python
from mcp.server import Server
from mcp.types import ResourceTemplate

app = Server("template-server")

@app.list_resource_templates()
async def list_templates() -> list[ResourceTemplate]:
    """Return available resource templates."""
    return [
        ResourceTemplate(
            uriTemplate="db://users/{user_id}",
            name="User Profile",
            description="Fetch user profile by ID",
            mimeType="application/json"
        ),
        ResourceTemplate(
            uriTemplate="api://weather/{city}/{date}",
            name="Weather Data",
            description="Historical weather for city and date",
            mimeType="application/json"
        ),
        ResourceTemplate(
            uriTemplate="file://{path}",
            name="File Content",
            description="Read file at given path",
            mimeType="text/plain"
        )
    ]

@app.read_resource()
async def read_resource(uri: str) -> str:
    """Read resource, expanding template parameters."""
    
    # Parsuj URI, aby wyodrębnić parametry
    if uri.startswith("db://users/"):
        user_id = uri.split("/")[-1]
        return await fetch_user(user_id)
    
    elif uri.startswith("api://weather/"):
        parts = uri.replace("api://weather/", "").split("/")
        city, date = parts[0], parts[1]
        return await fetch_weather(city, date)
    
    elif uri.startswith("file://"):
        path = uri.replace("file://", "")
        return await read_file(path)
    
    raise ValueError(f"Unknown resource URI: {uri}")
```

### Implementacja w TypeScript

```typescript
server.setRequestHandler(ListResourceTemplatesSchema, async () => {
  return {
    resourceTemplates: [
      {
        uriTemplate: "github://repos/{owner}/{repo}/issues/{issue_number}",
        name: "GitHub Issue",
        description: "Fetch a specific GitHub issue",
        mimeType: "application/json"
      },
      {
        uriTemplate: "db://tables/{table}/rows/{id}",
        name: "Database Row",
        description: "Fetch a row from a database table",
        mimeType: "application/json"
      }
    ]
  };
});

server.setRequestHandler(ReadResourceSchema, async (request) => {
  const uri = request.params.uri;
  
  // Analizuj URI zgłoszenia GitHub
  const githubMatch = uri.match(/^github:\/\/repos\/([^/]+)\/([^/]+)\/issues\/(\d+)$/);
  if (githubMatch) {
    const [_, owner, repo, issueNumber] = githubMatch;
    const issue = await fetchGitHubIssue(owner, repo, parseInt(issueNumber));
    return {
      contents: [{
        uri,
        mimeType: "application/json",
        text: JSON.stringify(issue, null, 2)
      }]
    };
  }
  
  throw new Error(`Unknown resource URI: ${uri}`);
});
```

---

## 4. Cykl Życia Aplikacji

Ta sekcja dotyczy uruchamiania i zamykania procesu aplikacji, nie usuniętego
inicjalizacyjnego uścisku dłoni MCP. Poprawne zarządzanie cyklem życia zapewnia czyste zarządzanie zasobami.


### Zarządzanie Cyklami Życia w Python

```python
from mcp.server import Server
from contextlib import asynccontextmanager

app = Server("lifecycle-server")

# Stan współdzielony
db_connection = None
cache = None

@asynccontextmanager
async def lifespan(server: Server):
    """Manage server lifecycle."""
    global db_connection, cache
    
    # Uruchamianie
    print("🚀 Server starting...")
    db_connection = await create_database_connection()
    cache = await create_cache_client()
    print("✅ Resources initialized")
    
    yield  # Serwer działa tutaj
    
    # Zamknięcie
    print("🛑 Server shutting down...")
    await db_connection.close()
    await cache.close()
    print("✅ Resources cleaned up")

app = Server("lifecycle-server", lifespan=lifespan)

@app.tool()
async def query_database(sql: str) -> str:
    """Use the shared database connection."""
    result = await db_connection.execute(sql)
    return str(result)
```

### Cykl życia w TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

class ManagedServer {
  private server: Server;
  private dbConnection: DatabaseConnection | null = null;
  
  constructor() {
    this.server = new Server({
      name: "lifecycle-server",
      version: "1.0.0"
    });
    
    this.setupHandlers();
  }
  
  async start() {
    // Zainicjuj zasoby
    console.log("🚀 Server starting...");
    this.dbConnection = await createDatabaseConnection();
    console.log("✅ Database connected");
    
    // Uruchom serwer
    await this.server.connect(transport);
  }
  
  async stop() {
    // Wyczyść zasoby
    console.log("🛑 Server shutting down...");
    if (this.dbConnection) {
      await this.dbConnection.close();
    }
    await this.server.close();
    console.log("✅ Cleanup complete");
  }
  
  private setupHandlers() {
    this.server.setRequestHandler(CallToolSchema, async (request) => {
      // Bezpiecznie używaj this.dbConnection
      // ...
    });
  }
}

// Użycie z łagodnym zamknięciem
const server = new ManagedServer();

process.on('SIGINT', async () => {
  await server.stop();
  process.exit(0);
});

await server.start();
```

---

## 5. Kontrola Logowania (Legacy)

> [!WARNING]
> Logowanie w MCP jest przestarzałe w wersji `2026-07-28` i może zostać usunięte w
> pierwszej rewizji specyfikacji wydanej 28 lipca 2027 lub później. Przykłady
> poniżej służą kompatybilności ze starszymi implementacjami. Używaj `stderr` przy
> stdio oraz OpenTelemetry dla ustrukturyzowanej obserwowalności w nowych serwerach.

Starsze wersje MCP wspierają poziomy logowania po stronie serwera, którymi klienci mogą zarządzać.

### Implementacja Poziomów Logowania

```python
from mcp.server import Server
from mcp.types import LoggingLevel
import logging

app = Server("logging-server")

# Mapuj poziomy MCP na poziomy logowania Pythona
LEVEL_MAP = {
    LoggingLevel.DEBUG: logging.DEBUG,
    LoggingLevel.INFO: logging.INFO,
    LoggingLevel.WARNING: logging.WARNING,
    LoggingLevel.ERROR: logging.ERROR,
}

logger = logging.getLogger("mcp-server")

@app.set_logging_level()
async def set_logging_level(level: LoggingLevel) -> None:
    """Handle client request to change logging level."""
    python_level = LEVEL_MAP.get(level, logging.INFO)
    logger.setLevel(python_level)
    logger.info(f"Logging level set to {level}")

@app.tool()
async def debug_operation(data: str) -> str:
    """Tool with various logging levels."""
    logger.debug(f"Processing data: {data}")
    
    try:
        result = process(data)
        logger.info(f"Successfully processed: {result}")
        return result
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise
```

### Wysyłanie komunikatów logów do klienta

```python
@app.tool()
async def complex_operation(input: str, ctx) -> str:
    """Operation that logs to client."""
    
    # Wyślij powiadomienie o logu do klienta
    await ctx.send_log(
        level="info",
        message=f"Starting complex operation with input: {input}"
    )
    
    # Wykonaj pracę...
    result = await do_work(input)
    
    await ctx.send_log(
        level="debug",
        message=f"Operation complete, result size: {len(result)}"
    )
    
    return result
```

---

## 6. Wzorce Obsługi Błędów

Spójna obsługa błędów poprawia debugowanie i doświadczenie użytkownika.

### Kody błędów MCP

```python
from mcp.types import McpError, ErrorCode

class ToolError(McpError):
    """Base class for tool errors."""
    pass

class ValidationError(ToolError):
    """Invalid input parameters."""
    def __init__(self, message: str):
        super().__init__(ErrorCode.INVALID_PARAMS, message)

class NotFoundError(ToolError):
    """Requested resource not found."""
    def __init__(self, resource: str):
        super().__init__(ErrorCode.INVALID_REQUEST, f"Not found: {resource}")

class PermissionError(ToolError):
    """Access denied."""
    def __init__(self, action: str):
        super().__init__(ErrorCode.INVALID_REQUEST, f"Permission denied: {action}")

class InternalError(ToolError):
    """Internal server error."""
    def __init__(self, message: str):
        super().__init__(ErrorCode.INTERNAL_ERROR, message)
```

### Ustrukturyzowane odpowiedzi błędów

```python
@app.tool()
async def safe_operation(input: str) -> str:
    """Tool with comprehensive error handling."""
    
    # Waliduj dane wejściowe
    if not input:
        raise ValidationError("Input cannot be empty")
    
    if len(input) > 10000:
        raise ValidationError(f"Input too large: {len(input)} chars (max 10000)")
    
    try:
        # Sprawdź uprawnienia
        if not await check_permission(input):
            raise PermissionError(f"read {input}")
        
        # Wykonaj operację
        result = await perform_operation(input)
        
        if result is None:
            raise NotFoundError(input)
        
        return result
        
    except ConnectionError as e:
        raise InternalError(f"Database connection failed: {e}")
    except TimeoutError as e:
        raise InternalError(f"Operation timed out: {e}")
    except Exception as e:
        # Zaloguj nieoczekiwane błędy
        logger.exception(f"Unexpected error in safe_operation")
        raise InternalError(f"Unexpected error: {type(e).__name__}")
```

### Obsługa błędów w TypeScript

```typescript
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";

function validateInput(data: unknown): asserts data is ValidInput {
  if (typeof data !== "object" || data === null) {
    throw new McpError(
      ErrorCode.InvalidParams,
      "Input must be an object"
    );
  }
  // Więcej walidacji...
}

server.setRequestHandler(CallToolSchema, async (request) => {
  try {
    validateInput(request.params.arguments);
    
    const result = await performOperation(request.params.arguments);
    
    return {
      content: [{ type: "text", text: JSON.stringify(result) }]
    };
    
  } catch (error) {
    if (error instanceof McpError) {
      throw error;  // Już jest błąd MCP
    }
    
    // Konwertuj inne błędy
    if (error instanceof NotFoundError) {
      throw new McpError(ErrorCode.InvalidRequest, error.message);
    }
    
    // Nieznany błąd
    console.error("Unexpected error:", error);
    throw new McpError(
      ErrorCode.InternalError,
      "An unexpected error occurred"
    );
  }
});
```

---

## Funkcje czułe na wersję

### Rozszerzenie Tasks

Tasks to oficjalne, osobno wersjonowane rozszerzenie w MCP `2026-07-28`. Serwer
może zwracać uchwyt zadania z wywołania narzędzia, a klient steruje zadaniem
za pomocą `tasks/get`, `tasks/update` i `tasks/cancel`. Eksperymentalne
API Tasks `2025-11-25` nie jest kompatybilne wstecz, a `tasks/list` już nie istnieje.




lub działanie w otwartym świecie. Są to wskazówki i nie powinny być traktowane jako zaufane
gwarancje autoryzacji ani bezpieczeństwa, chyba że pochodzą z zaufanego serwera.


---

## Co dalej

- [Moduł 8 - Najlepsze Praktyki](../../08-BestPractices/README.md)
- [5.14 - Inżynieria Kontekstu](../mcp-contextengineering/README.md)
- [Dziennik zmian specyfikacji MCP](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

---

## Dodatkowe Zasoby

- [Specyfikacja MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Kody błędów JSON-RPC 2.0](https://www.jsonrpc.org/specification#error_object)
- [Przykłady SDK Python](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples)
- [Przykłady SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->