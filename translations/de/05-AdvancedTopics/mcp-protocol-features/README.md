# MCP Protokoll Features im Detail

Diese Anleitung untersucht erweiterte MCP-Protokollfunktionen, die über die grundlegende Handhabung von Tools und Ressourcen hinausgehen. Das Verständnis dieser Funktionen hilft Ihnen, robustere, benutzerfreundlichere und produktionsreife MCP-Server zu erstellen.

> **Ausblick:** Der Release-Kandidat `2026-07-28` depreziert die Logging-Primitive (zugunsten von `stderr` für stdio und OpenTelemetry für strukturierte Beobachtbarkeit), entfernt das unten unter Server Lifecycle Events erwähnte `initialize`/Sitzungsmodell und verschiebt die experimentelle Tasks-Funktion in eine eigene Tasks-Erweiterung mit einem neuen `tasks/get`/`tasks/update`/`tasks/cancel`-Lebenszyklus. Siehe [Was sich im MCP ändert: Der Release-Kandidat 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Abgedeckte Funktionen

1. **Fortschrittsbenachrichtigungen** – Melden den Fortschritt bei lang laufenden Operationen
2. **Anfrageabbruch** – Ermöglichen es Clients, laufende Anfragen abzubrechen
3. **Ressourcenvorlagen** – Dynamische Ressourcen-URIs mit Parametern
4. **Server Lifecycle Events** – Korrekte Initialisierung und Herunterfahren
5. **Logging-Steuerung** – Logging-Konfiguration auf Serverseite
6. **Fehlerbehandlungsmuster** – Konsistente Fehlerantworten

---

## 1. Fortschrittsbenachrichtigungen

Für Vorgänge, die Zeit in Anspruch nehmen (Datenverarbeitung, Dateidownloads, API-Aufrufe), halten Fortschrittsbenachrichtigungen die Benutzer informiert.

### Funktionsweise

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: tools/call (lange Operation)
    Server-->>Client: Benachrichtigung: Fortschritt 10%
    Server-->>Client: Benachrichtigung: Fortschritt 50%
    Server-->>Client: Benachrichtigung: Fortschritt 90%
    Server->>Client: Ergebnis (abgeschlossen)
```

### Python-Implementierung

```python
from mcp.server import Server, NotificationOptions
from mcp.types import ProgressNotification
import asyncio

app = Server("progress-server")

@app.tool()
async def process_large_file(file_path: str, ctx) -> str:
    """Process a large file with progress updates."""
    
    # Dateigröße für die Fortschrittsberechnung ermitteln
    file_size = os.path.getsize(file_path)
    processed = 0
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            # Chunk verarbeiten
            await process_chunk(chunk)
            processed += len(chunk)
            
            # Fortschrittsbenachrichtigung senden
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
        
        # Fortschritt nach jedem Element melden
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

### TypeScript-Implementierung

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
      
      // Fortschrittsbenachrichtigung senden
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

### Client-Behandlung (Python)

```python
async def handle_progress(notification):
    """Handle progress notifications from server."""
    params = notification.params
    print(f"Progress: {params.progress}/{params.total} - {params.message}")

# Registriere Handler
session.on_notification("notifications/progress", handle_progress)

# Rufe Werkzeug auf (Fortschrittsupdates werden über den Handler empfangen)
result = await session.call_tool("process_large_file", {"file_path": "/data/large.csv"})
```

---

## 2. Anfrageabbruch

Ermöglichen Sie es Clients, Anfragen abzubrechen, die nicht mehr benötigt werden oder zu lange dauern.

### Python-Implementierung

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
        for page in range(100):  # Durchsuche viele Seiten
            # Prüfen, ob eine Stornierung angefordert wurde
            if ctx.is_cancelled:
                raise CancelledError("Search cancelled by user")
            
            # Seitensuche simulieren
            page_results = await search_page(query, page)
            results.extend(page_results)
            
            # Kleine Verzögerung ermöglicht Stornierungsprüfungen
            await asyncio.sleep(0.1)
            
    except CancelledError:
        # Teilweise Ergebnisse zurückgeben
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

### Implementierung des Abbruchkontexts

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
            pass  # Normaler Timeout, fortfahren
```

### Clientseitiger Abbruch

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
        # Stornierungsanfrage
        await session.send_notification({
            "method": "notifications/cancelled",
            "params": {"requestId": task.request_id, "reason": "Timeout"}
        })
        return "Search timed out"
```

---

## 3. Ressourcenvorlagen

Ressourcenvorlagen erlauben die dynamische URI-Erstellung mit Parametern und sind nützlich für APIs und Datenbanken.

### Definition von Vorlagen

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
    
    # Analysiere die URI, um Parameter zu extrahieren
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

### TypeScript-Implementierung

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
  
  // GitHub-Issue-URI analysieren
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

## 4. Server Lifecycle Events

Eine korrekte Initialisierung und Herunterfahren sorgt für eine saubere Ressourcenverwaltung.

### Python Lifecycle-Management

```python
from mcp.server import Server
from contextlib import asynccontextmanager

app = Server("lifecycle-server")

# Gemeinsamer Zustand
db_connection = None
cache = None

@asynccontextmanager
async def lifespan(server: Server):
    """Manage server lifecycle."""
    global db_connection, cache
    
    # Start
    print("🚀 Server starting...")
    db_connection = await create_database_connection()
    cache = await create_cache_client()
    print("✅ Resources initialized")
    
    yield  # Server läuft hier
    
    # Herunterfahren
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

### TypeScript Lifecycle

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
    // Ressourcen initialisieren
    console.log("🚀 Server starting...");
    this.dbConnection = await createDatabaseConnection();
    console.log("✅ Database connected");
    
    // Server starten
    await this.server.connect(transport);
  }
  
  async stop() {
    // Ressourcen bereinigen
    console.log("🛑 Server shutting down...");
    if (this.dbConnection) {
      await this.dbConnection.close();
    }
    await this.server.close();
    console.log("✅ Cleanup complete");
  }
  
  private setupHandlers() {
    this.server.setRequestHandler(CallToolSchema, async (request) => {
      // Verwenden Sie diese.dbConnection sicher
      // ...
    });
  }
}

// Verwendung mit sanftem Herunterfahren
const server = new ManagedServer();

process.on('SIGINT', async () => {
  await server.stop();
  process.exit(0);
});

await server.start();
```

---

## 5. Logging-Steuerung

MCP unterstützt Logging-Ebenen auf Serverseite, die Clients steuern können.

### Implementierung von Logging-Leveln

```python
from mcp.server import Server
from mcp.types import LoggingLevel
import logging

app = Server("logging-server")

# Ordne MCP-Stufen Python-Protokollierungsstufen zu
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

### Senden von Log-Nachrichten an den Client

```python
@app.tool()
async def complex_operation(input: str, ctx) -> str:
    """Operation that logs to client."""
    
    # Sende Protokollbenachrichtigung an den Client
    await ctx.send_log(
        level="info",
        message=f"Starting complex operation with input: {input}"
    )
    
    # Arbeite...
    result = await do_work(input)
    
    await ctx.send_log(
        level="debug",
        message=f"Operation complete, result size: {len(result)}"
    )
    
    return result
```

---

## 6. Fehlerbehandlungsmuster

Konsistente Fehlerbehandlung verbessert das Debugging und die Benutzererfahrung.

### MCP-Fehlercodes

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

### Strukturierte Fehlerantworten

```python
@app.tool()
async def safe_operation(input: str) -> str:
    """Tool with comprehensive error handling."""
    
    # Eingabe validieren
    if not input:
        raise ValidationError("Input cannot be empty")
    
    if len(input) > 10000:
        raise ValidationError(f"Input too large: {len(input)} chars (max 10000)")
    
    try:
        # Berechtigungen überprüfen
        if not await check_permission(input):
            raise PermissionError(f"read {input}")
        
        # Operation ausführen
        result = await perform_operation(input)
        
        if result is None:
            raise NotFoundError(input)
        
        return result
        
    except ConnectionError as e:
        raise InternalError(f"Database connection failed: {e}")
    except TimeoutError as e:
        raise InternalError(f"Operation timed out: {e}")
    except Exception as e:
        # Unerwartete Fehler protokollieren
        logger.exception(f"Unexpected error in safe_operation")
        raise InternalError(f"Unexpected error: {type(e).__name__}")
```

### Fehlerbehandlung in TypeScript

```typescript
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";

function validateInput(data: unknown): asserts data is ValidInput {
  if (typeof data !== "object" || data === null) {
    throw new McpError(
      ErrorCode.InvalidParams,
      "Input must be an object"
    );
  }
  // Mehr Validierung...
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
      throw error;  // Bereits ein MCP-Fehler
    }
    
    // Andere Fehler konvertieren
    if (error instanceof NotFoundError) {
      throw new McpError(ErrorCode.InvalidRequest, error.message);
    }
    
    // Unbekannter Fehler
    console.error("Unexpected error:", error);
    throw new McpError(
      ErrorCode.InternalError,
      "An unexpected error occurred"
    );
  }
});
```

---

## Experimentelle Features (MCP 2025-11-25)

Diese Funktionen sind in der Spezifikation als experimentell gekennzeichnet:

### Tasks (Lang laufende Operationen)

```python
# Aufgaben ermöglichen das Nachverfolgen von lang andauernden Operationen mit Status
@app.task()
async def training_task(model_id: str, data_path: str, ctx) -> str:
    """Long-running ML training task."""
    
    # Aufgabe gestartet melden
    await ctx.report_status("running", "Initializing training...")
    
    # Trainingsschleife
    for epoch in range(100):
        await train_epoch(model_id, data_path, epoch)
        await ctx.report_status(
            "running",
            f"Training epoch {epoch + 1}/100",
            progress=epoch + 1,
            total=100
        )
    
    await ctx.report_status("completed", "Training finished")
    return f"Model {model_id} trained successfully"
```

### Tool-Anmerkungen

```python
# Anmerkungen liefern Metadaten über das Verhalten des Werkzeugs
@app.tool(
    annotations={
        "destructive": False,      # Ändert keine Daten
        "idempotent": True,        # Sicher zum erneuten Versuch
        "timeout_seconds": 30,     # Erwartete maximale Dauer
        "requires_approval": False # Keine Benutzerfreigabe erforderlich
    }
)
async def safe_query(query: str) -> str:
    """A read-only database query tool."""
    return await execute_read_query(query)
```

---

## Was kommt als Nächstes

- [Modul 8 – Best Practices](../../08-BestPractices/README.md)
- [5.14 – Context Engineering](../mcp-contextengineering/README.md)
- [MCP Spezifikations-Changelog](https://spec.modelcontextprotocol.io/)

---

## Zusätzliche Ressourcen

- [MCP Spezifikation 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [JSON-RPC 2.0 Fehlercodes](https://www.jsonrpc.org/specification#error_object)
- [Python SDK Beispiele](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples)
- [TypeScript SDK Beispiele](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->