# លក្ខណៈពិសេសរបស់ពិធីការ MCP ក្នុងការស្វែងយល់ជ្រៅ

មគ្គុទេសក៍នេះស្វែងរកលក្ខណៈពិសេសពិធីការដែលកាន់តែខ្ពស់របស់ MCP ដែលលើសពីការគ្រប់គ្រងឧបករណ៍ និងធនធានមូលដ្ឋាន។ ការយល់ដឹងអំពីលក្ខណៈពិសេសទាំងនេះជួយឲ្យអ្នកបង្កើតម៉ាស៊ឺរប្រភេទ MCP ដែលមានភាពរឹងមាំ ជាពិសេសសម្រាប់អ្នកប្រើប្រាស់ និងមានភាពទាន់សម័យសម្រាប់ផលិតផល។

## លក្ខណៈពិសេសដែលបានព្រមាន

1. **ការជូនដំណឹងដំណើរការ** - រាយការណ៍ដំណើរការសម្រាប់ប្រតិបត្តិការដែលចំណាយពេលយូរ
2. **ការលុបចោលសំណើ** - អនុញ្ញាតឲ្យអតិថិជនលុបចោលសំណើដែលកំពុងដំណើរការ
3. **គំរូធនធាន** - អាចបង្កើត URI រួមដោយអថិត្យទិន្នន័យ
4. **ព្រឹត្តិការណ៍អាយុកាលម៉ាស៊ីនបម្រើ** - ការចាប់ផ្តើម និងបិទម៉ាស៊ីនបម្រើយ៉ាងត្រឹមត្រូវ
5. **ការត្រួតពិនិត្យការចុះបញ្ជី** - ការកំណត់កម្រិតការចុះបញ្ជីនៅម៉ាស៊ីនបម្រើ
6. **គំរូការគ្រប់គ្រងកំហុស** - ការឆ្លើយតបកំហុសយ៉ាងសុចរិត

---

## 1. ការជូនដំណឹងដំណើរការ

សម្រាប់ប្រតិបត្តិការដែលចំណាយពេល (ដំណើរការទិន្នន័យ ការទាញយកឯកសារ ការហៅ API) ការជូនដំណឹងដំណើរការជួយឲ្យអ្នកប្រើប្រាស់បានជ្រាប។

### វាសកម្មយ៉ាងដូចម្តេច

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: tools/call (ប្រតិបត្តិការល្អយ dlou)
    Server-->>Client: ជូនដំណឹងៈ ការរីកចម្រើន 10%
    Server-->>Client: ជូនដំណឹងៈ ការរីកចម្រើន 50%
    Server-->>Client: ជូនដំណឹងៈ ការរីកចម្រើន 90%
    Server->>Client: លទ្ធផល (បញ្ចប់)
```
### ការអនុវត្ត Python

```python
from mcp.server import Server, NotificationOptions
from mcp.types import ProgressNotification
import asyncio

app = Server("progress-server")

@app.tool()
async def process_large_file(file_path: str, ctx) -> str:
    """Process a large file with progress updates."""
    
    # ទទួលទំហំឯកសារសម្រាប់ការគណនាការរីកចម្រើន
    file_size = os.path.getsize(file_path)
    processed = 0
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            # ដំណើរការផ្នែក
            await process_chunk(chunk)
            processed += len(chunk)
            
            # ផ្ញើការជូនដំណឹងអំពីការរីកចម្រើន
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
        
        # របាយការណ៍ការរីកចម្រើនបន្ទាប់ពីមួយធាតុរៀងរាល់មួយ
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

### ការអនុវត្ត TypeScript

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
      
      // ផ្ញើ​ការ​ជូនដំណឹង​ពី​ការរីកចម្រើន
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

### ការគ្រប់គ្រងពីភាគីអតិថិជន (Python)

```python
async def handle_progress(notification):
    """Handle progress notifications from server."""
    params = notification.params
    print(f"Progress: {params.progress}/{params.total} - {params.message}")

# ចុះឈ្មោះអ្នកដោះស្រាយ
session.on_notification("notifications/progress", handle_progress)

# ហៅឧបករណ៍ (អាប់ដេតជំពាក់នឹងមកដល់តាមអ្នកដោះស្រាយ)
result = await session.call_tool("process_large_file", {"file_path": "/data/large.csv"})
```

---

## 2. ការលុបចោលសំណើ

អនុញ្ញាតឲ្យអតិថិជនលុបចោលសំណើដែលមិនចាំបាច់ឬកំពុងយឺតពេក។

### ការអនុវត្ត Python

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
        for page in range(100):  # ស្វែងរកតាមទំព័រច្រើន
            # ពិនិត្យមើលថាតើបានស្នើសុំបោះបង់ឬអត់
            if ctx.is_cancelled:
                raise CancelledError("Search cancelled by user")
            
            # ចម្លងការស្វែងរកតាមទំព័រ
            page_results = await search_page(query, page)
            results.extend(page_results)
            
            # ពន្យារពេលតិចតួចអនុញ្ញាតឲ្យពិនិត្យការបោះបង់
            await asyncio.sleep(0.1)
            
    except CancelledError:
        # ត្រឡប់លទ្ធផលផ្នែកមួយ
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

### ការអនុវត្ត Context សម្រាប់ការលុបចោល

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
            pass  # ពេលវេលាដែលធម្មតា, ការបន្ត
```

### ការលុបចោលពីភាគីអតិថិជន

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
        # សំណើរ​លុប​បោះ​បង់
        await session.send_notification({
            "method": "notifications/cancelled",
            "params": {"requestId": task.request_id, "reason": "Timeout"}
        })
        return "Search timed out"
```

---

## 3. គំរូធនធាន

គំរូធនធានអនុញ្ញាតឲ្យបង្កើត URI យ៉ាងអាចបត់បែនបានដោយប្រើប៉ារ៉ាម៉ែត្រ សមស្របសម្រាប់ API និងមូលដ្ឋានទិន្នន័យ។

### ការបង្កើតគំរូ

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
    
    # វាយតម្លៃ URI ដើម្បីដក parameters
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

### ការអនុវត្ត TypeScript

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
  
  // បំបែក URI បញ្ហា GitHub
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

## 4. ព្រឹត្តិការណ៍អាយុកាលម៉ាស៊ីនបម្រើ

ការចាប់ផ្តើម និងបិទម៉ាស៊ីនបម្រើយ៉ាងត្រឹមត្រូវធានាថាការគ្រប់គ្រងធនធានមានភាពស្អាតនិងត្រឹមត្រូវ។

### ការគ្រប់គ្រងអាយុកាល Python

```python
from mcp.server import Server
from contextlib import asynccontextmanager

app = Server("lifecycle-server")

# រដ្ឋចែករំលែក
db_connection = None
cache = None

@asynccontextmanager
async def lifespan(server: Server):
    """Manage server lifecycle."""
    global db_connection, cache
    
    # ការចាប់ផ្តើម
    print("🚀 Server starting...")
    db_connection = await create_database_connection()
    cache = await create_cache_client()
    print("✅ Resources initialized")
    
    yield  # ម៉ាស៊ីនមេដំណើរការនៅទីនេះ
    
    # បិទដោយសុវត្ថិភាព
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

### អាយុកាល TypeScript

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
    // ចាប់ផ្តើមធនធាន
    console.log("🚀 Server starting...");
    this.dbConnection = await createDatabaseConnection();
    console.log("✅ Database connected");
    
    // ចាប់ផ្តើមម៉ាស៊ីនបម្រើ
    await this.server.connect(transport);
  }
  
  async stop() {
    // សម្អាតធនធាន
    console.log("🛑 Server shutting down...");
    if (this.dbConnection) {
      await this.dbConnection.close();
    }
    await this.server.close();
    console.log("✅ Cleanup complete");
  }
  
  private setupHandlers() {
    this.server.setRequestHandler(CallToolSchema, async (request) => {
      // ប្រើ this.dbConnection យ៉ាងមានសុវត្ថិភាព
      // ...
    });
  }
}

// ការប្រើប្រាស់ជាមួយការបិទម៉ាស៊ីនយ៉ាងរលូន
const server = new ManagedServer();

process.on('SIGINT', async () => {
  await server.stop();
  process.exit(0);
});

await server.start();
```

---

## 5. ការត្រួតពិនិត្យការចុះបញ្ជី

MCP គាំទ្រកម្រិតការចុះបញ្ជីនៅម៉ាស៊ីនបម្រើដែលអតិថិជនអាចគ្រប់គ្រងបាន។

### ការអនុវត្តកម្រិតការចុះបញ្ជី

```python
from mcp.server import Server
from mcp.types import LoggingLevel
import logging

app = Server("logging-server")

# ផ្ទាំងកម្រិត MCP ទៅកម្រិតកំណត់ហេតុ Python
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

### ការផ្ញើសារចុះបញ្ជីទៅអតិថិជន

```python
@app.tool()
async def complex_operation(input: str, ctx) -> str:
    """Operation that logs to client."""
    
    # ផ្ញើការជូនដំណឹងកំណត់ហេតុទៅអតិថិជន
    await ctx.send_log(
        level="info",
        message=f"Starting complex operation with input: {input}"
    )
    
    # ធ្វើការងារ...
    result = await do_work(input)
    
    await ctx.send_log(
        level="debug",
        message=f"Operation complete, result size: {len(result)}"
    )
    
    return result
```

---

## 6. គំរូការគ្រប់គ្រងកំហុស

ការគ្រប់គ្រងកំហុសយ៉ាងសំរាប់គ្នាធ្វើឲ្យការកែកំហុស និងបទពិសោធ៍អ្នកប្រើប្រាស់មានប្រសិទ្ធភាព។

### លេខកូដកំហុស MCP

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

### ការឆ្លើយតបកំហុសដែលមានរចនាសម្ព័ន្ធ

```python
@app.tool()
async def safe_operation(input: str) -> str:
    """Tool with comprehensive error handling."""
    
    # ផ្ទៀងផ្ទាត់ការបញ្ចូល
    if not input:
        raise ValidationError("Input cannot be empty")
    
    if len(input) > 10000:
        raise ValidationError(f"Input too large: {len(input)} chars (max 10000)")
    
    try:
        # ពិនិត្យការអនុញ្ញាត
        if not await check_permission(input):
            raise PermissionError(f"read {input}")
        
        # អនុវត្តប្រតិបត្តិការ
        result = await perform_operation(input)
        
        if result is None:
            raise NotFoundError(input)
        
        return result
        
    except ConnectionError as e:
        raise InternalError(f"Database connection failed: {e}")
    except TimeoutError as e:
        raise InternalError(f"Operation timed out: {e}")
    except Exception as e:
        # ចុះបញ្ជីកំហុសដែលមិនបានរំពឹងទុក
        logger.exception(f"Unexpected error in safe_operation")
        raise InternalError(f"Unexpected error: {type(e).__name__}")
```

### ការគ្រប់គ្រងកំហុសក្នុង TypeScript

```typescript
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";

function validateInput(data: unknown): asserts data is ValidInput {
  if (typeof data !== "object" || data === null) {
    throw new McpError(
      ErrorCode.InvalidParams,
      "Input must be an object"
    );
  }
  // ការផ្ទៀងផ្ទាត់បន្ថែមទៀត...
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
      throw error;  // ខុសបន្លំ MCP មានរួចហើយ
    }
    
    // បម្លែងការខុសផ្សេងទៀត
    if (error instanceof NotFoundError) {
      throw new McpError(ErrorCode.InvalidRequest, error.message);
    }
    
    // ការខុសមិនស្គាល់
    console.error("Unexpected error:", error);
    throw new McpError(
      ErrorCode.InternalError,
      "An unexpected error occurred"
    );
  }
});
```

---

## លក្ខណៈពិសេសសាកល្បង (MCP 2025-11-25)

លក្ខណៈពិសេសទាំងនេះត្រូវបានសម្គាល់ថាជាការសាកល្បងក្នុងលក្ខណៈពិសេស៖

### ភារកិច្ច (ប្រតិបត្តិការដែលចំណាយពេលយូរ)

```python
# ការងារអនុញ្ញាតឲ្យតាមដានប្រតិបត្តិការដែលរត់យូរជាមួយស្ថានភាព
@app.task()
async def training_task(model_id: str, data_path: str, ctx) -> str:
    """Long-running ML training task."""
    
    # រាយការណ៍ការងារចាប់ផ្តើម
    await ctx.report_status("running", "Initializing training...")
    
    # វដ្តបណ្តុះបណ្តាល
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

### ការកំណត់សម្គាល់ឧបករណ៍

```python
# ការប្រាប់ព័ត៌មានផ្តល់ព័ត៌មានអំពីឧបករណ៍ប្រតិបត្តិការ
@app.tool(
    annotations={
        "destructive": False,      # មិនផ្លាស់ប្តូរទិន្នន័យ
        "idempotent": True,        # មានសុវត្ថិភាពក្នុងការព្យាយាមម្តងទៀត
        "timeout_seconds": 30,     # រយៈពេលអតិបរមារង់ចាំ
        "requires_approval": False # មិនចាំបាច់ការអនុម័តពីអ្នកប្រើប្រាស់
    }
)
async def safe_query(query: str) -> str:
    """A read-only database query tool."""
    return await execute_read_query(query)
```

---

## អ្វីជាប់ក្រោយ

- [Module 8 - ល្បិចល្អបំផុត](../../08-BestPractices/README.md)
- [5.14 - វិស្វកម្ម Context](../mcp-contextengineering/README.md)
- [បម្លាស់ប្តូរពិធីការបញ្ជាក់ MCP](https://spec.modelcontextprotocol.io/)

---

## ធនធានបន្ថែម

- [ពិធីការបញ្ជាក់ MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [លេខកូដកំហុស JSON-RPC 2.0](https://www.jsonrpc.org/specification#error_object)
- [ឧទាហរណ៍ Python SDK](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples)
- [ឧទាហរណ៍ TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខិតខំសម្រាប់ភាពត្រឹមត្រូវ ក៏សូមយល់ព្រមថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមដោយភាសាដើមគួរត្រូវបានគិតថាជាតំណភក្តីចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរត្រូវបានបកប្រែដោយអ្នកបកប្រែវិជ្ជាជីវៈមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសបណ្តាលមកពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->