# Детаљан преглед карактеристика MCP протокола

Овај водич истражује напредне карактеристике MCP протокола које превазилазе основно управљање алатима и ресурсима. Разумевање ових функција помаже вам да изградите робусније, пријатније за кориснике и спремније за производњу MCP сервере.

> **Обим MCP `2026-07-28`:** покретање и гашење процеса сервера остају
> брине апликације, али MCP `initialize` руковање и сесије на нивоу протокола
> су уклоњене. Одељак о евидентирању испод је задржан за наслеђе
> имплементације; нови сервери треба да користе `stderr` или OpenTelemetry. Задатке је
> сада одвојено верзионирани екстензија. Погледајте
> [Шта се променило у MCP: Спецификација 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

## Обухваћене карактеристике

1. **Обавештења о напредовању** - Извештавање о напретку дуготрајних операција
2. **Отказивање захтева** - Омогућава клијентима да отказују захтеве у току
3. **Шаблони ресурса** - Динамички URI ресурса са параметрима
4. **Животни циклус апликације** - Покретање и гашење процеса сервера
5. **Контрола евидентирања (наследна)** - Застарела конфигурација MCP евидентирања
6. **Обрасци руковања грешкама** - Конзистентни одговори на грешке

---

## 1. Обавештења о напредовању

За операције које захтевају време (обрада података, преузимање фајлова, API позиви), обавештења о напредовању држе кориснике информисаним.

### Како функционише

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: tools/call (дужа операција)
    Server-->>Client: обавештење: напредак 10%
    Server-->>Client: обавештење: напредак 50%
    Server-->>Client: обавештење: напредак 90%
    Server->>Client: резултат (завршено)
```

### Питхон имплементација

```python
from mcp.server import Server, NotificationOptions
from mcp.types import ProgressNotification
import asyncio

app = Server("progress-server")

@app.tool()
async def process_large_file(file_path: str, ctx) -> str:
    """Process a large file with progress updates."""
    
    # Добиј величину фајла за прорачун напретка
    file_size = os.path.getsize(file_path)
    processed = 0
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            # Обради део
            await process_chunk(chunk)
            processed += len(chunk)
            
            # Пошаљи обавештење о напретку
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
        
        # Пријави напредак након сваког предмета
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

### TypeScript имплементација

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
      
      // Пошаљи обавештење о напретку
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

### Руковање на клијентској страни (Питхон)

```python
async def handle_progress(notification):
    """Handle progress notifications from server."""
    params = notification.params
    print(f"Progress: {params.progress}/{params.total} - {params.message}")

# Региструјте обрађивач
session.on_notification("notifications/progress", handle_progress)

# Позовите алат (ажурирања напретка ће стизати преко обрађивача)
result = await session.call_tool("process_large_file", {"file_path": "/data/large.csv"})
```

---

## 2. Отказивање захтева

Омогућите клијентима да отказују захтеве који више нису потребни или трају предуго.

### Питхон имплементација

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
        for page in range(100):  # Претражи кроз много страница
            # Проверити да ли је захтевано отказивање
            if ctx.is_cancelled:
                raise CancelledError("Search cancelled by user")
            
            # Симулирај претрагу странице
            page_results = await search_page(query, page)
            results.extend(page_results)
            
            # Мала пауза омогућава провере отказивања
            await asyncio.sleep(0.1)
            
    except CancelledError:
        # Врати делимичне резултате
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

### Имплементација контекста отказивања

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
            pass  # Нормално време истека, настави
```

### Отказивање на клијентској страни

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
        # Захтев за отказивање
        await session.send_notification({
            "method": "notifications/cancelled",
            "params": {"requestId": task.request_id, "reason": "Timeout"}
        })
        return "Search timed out"
```

---

## 3. Шаблони ресурса

Шаблони ресурса омогућавају динамичку конструкцију URI-ја са параметрима, корисно за API и базе података.

### Дефинисање шаблона

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
    
    # Анализирај URI да извучеш параметре
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

### TypeScript имплементација

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
  
  // Парсирај URI GitHub проблема
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

## 4. Животни циклус апликације

Овај одељак покрива покретање и гашење процеса апликације, а не уклоњени
MCP `initialize` руковање. Правилно руковање животним циклусом обезбеђује чисто управљање ресурсима.


### Управљање животним циклусом у Питхон-у

```python
from mcp.server import Server
from contextlib import asynccontextmanager

app = Server("lifecycle-server")

# Заједничко стање
db_connection = None
cache = None

@asynccontextmanager
async def lifespan(server: Server):
    """Manage server lifecycle."""
    global db_connection, cache
    
    # Покретање
    print("🚀 Server starting...")
    db_connection = await create_database_connection()
    cache = await create_cache_client()
    print("✅ Resources initialized")
    
    yield  # Сервер ради овде
    
    # Искључивање
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

### Животни циклус у TypeScript-у

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
    // Иницијализуј ресурсе
    console.log("🚀 Server starting...");
    this.dbConnection = await createDatabaseConnection();
    console.log("✅ Database connected");
    
    // Покрени сервер
    await this.server.connect(transport);
  }
  
  async stop() {
    // Очисти ресурсе
    console.log("🛑 Server shutting down...");
    if (this.dbConnection) {
      await this.dbConnection.close();
    }
    await this.server.close();
    console.log("✅ Cleanup complete");
  }
  
  private setupHandlers() {
    this.server.setRequestHandler(CallToolSchema, async (request) => {
      // Користи this.dbConnection безбедно
      // ...
    });
  }
}

// Коришћење са благим искључењем
const server = new ManagedServer();

process.on('SIGINT', async () => {
  await server.stop();
  process.exit(0);
});

await server.start();
```

---

## 5. Контрола евидентирања (наследна)

> [!WARNING]
> Писање логова у MCP је застарело у `2026-07-28` и може бити уклоњено
> у првој ревизији спецификације издатој 28. јула 2027. или након ње. Примери
> испод су за компатибилност са старијим имплементацијама. Користите `stderr` уз
> stdio и OpenTelemetry за структуирану видљивост у новим серверима.

Наслеђене верзије MCP подржавају нивое евидентирања са сервера које клијенти могу контролисати.

### Имплементација нивоа евидентирања

```python
from mcp.server import Server
from mcp.types import LoggingLevel
import logging

app = Server("logging-server")

# Мапирајте MCP нивое на Питхон нивое логовања
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

### Слање лог порука клијенту

```python
@app.tool()
async def complex_operation(input: str, ctx) -> str:
    """Operation that logs to client."""
    
    # Пошаљи обавештење о запису клијенту
    await ctx.send_log(
        level="info",
        message=f"Starting complex operation with input: {input}"
    )
    
    # Обави посао...
    result = await do_work(input)
    
    await ctx.send_log(
        level="debug",
        message=f"Operation complete, result size: {len(result)}"
    )
    
    return result
```

---

## 6. Обрасци руковања грешкама

Конзистентно руковање грешкама побољшава отклањање грешака и корисничко искуство.

### MCP кодови грешака

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

### Структурирани одговори на грешке

```python
@app.tool()
async def safe_operation(input: str) -> str:
    """Tool with comprehensive error handling."""
    
    # Валидација улаза
    if not input:
        raise ValidationError("Input cannot be empty")
    
    if len(input) > 10000:
        raise ValidationError(f"Input too large: {len(input)} chars (max 10000)")
    
    try:
        # Провера дозвола
        if not await check_permission(input):
            raise PermissionError(f"read {input}")
        
        # Изврши операцију
        result = await perform_operation(input)
        
        if result is None:
            raise NotFoundError(input)
        
        return result
        
    except ConnectionError as e:
        raise InternalError(f"Database connection failed: {e}")
    except TimeoutError as e:
        raise InternalError(f"Operation timed out: {e}")
    except Exception as e:
        # Забележи необјашњиве грешке
        logger.exception(f"Unexpected error in safe_operation")
        raise InternalError(f"Unexpected error: {type(e).__name__}")
```

### Руковање грешкама у TypeScript-у

```typescript
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";

function validateInput(data: unknown): asserts data is ValidInput {
  if (typeof data !== "object" || data === null) {
    throw new McpError(
      ErrorCode.InvalidParams,
      "Input must be an object"
    );
  }
  // Више валидације...
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
      throw error;  // Већ MCP грешка
    }
    
    // Конвертуј друге грешке
    if (error instanceof NotFoundError) {
      throw new McpError(ErrorCode.InvalidRequest, error.message);
    }
    
    // Непозната грешка
    console.error("Unexpected error:", error);
    throw new McpError(
      ErrorCode.InternalError,
      "An unexpected error occurred"
    );
  }
});
```

---

## Карактеристике осетљиве на верзију

### Задатци Екстензија

Задатци су званична, одвојено верзионирана екстензија у MCP `2026-07-28`. Сервер може
вратити контролу задатка из позива алата, а клијент управља задатком преко `tasks/get`,
`tasks/update` и `tasks/cancel`. Експериментални
API за задатке `2025-11-25` није уназад компатибилан, и `tasks/list` више
не постоји.

### Аннотације алата

Аннотације алата описују понашање као што су само за читање, деструктивно, идемпотентно,
или отворени свет операција. То су наговештаји и не смеју се третирати као поуздана
овлашћења или гаранције безбедности осим ако не долазе са поузданог сервера.

---

## Шта следи

- [Модул 8 - Најбоље праксе](../../08-BestPractices/README.md)
- [5.14 - Инжењеринг контекста](../mcp-contextengineering/README.md)
- [MCP ревизија спецификације](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

---

## Додатни ресурси

- [MCP спецификација 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Кодови грешака](https://www.jsonrpc.org/specification#error_object)
- [Питхон SDK примери](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples)
- [TypeScript SDK примери](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->