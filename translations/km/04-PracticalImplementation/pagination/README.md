# ការបំបែកទំព័រ និង សំណុំនៃលទ្ធផលធំនៅក្នុង MCP

នៅពេលម៉ាស៊ីនមេ MCP របស់អ្នកដំណើរការ សំណុំទិន្នន័យធំៗ - មិនថា បញ្ជីឯកសារពាន់រយ, បង្កត់ត្រា ទិន្នន័យ ឬ លទ្ធផលស្វែងរក - អ្នកត្រូវការការបំបែកទំព័រ ដើម្បីគ្រប់គ្រងអង្គចងចាំយ៉ាងមានប្រសិទ្ធភាព និងផ្តល់បទពិសោធន៍អ្នកប្រើប្រាស់ឆាប់ដែលមានប្រសិទ្ធភាព។ មាគ្គុទេសក៍នេះគ្របដណ្តប់ពីវិធីអនុវត្តន៍ និង ប្រើប្រាស់ការបំបែកទំព័រនៅក្នុង MCP។

## ហេតុអ្វីបានជា Pagination មានសារៈសំខាន់

ប្រសិនបើគ្មានការបំបែកទំព័រ, លទ្ធផលធំៗអាចបណ្តាលឲ្យមានៈ

- **ការបញ្ចប់អង្គចងចាំ** - ដំណើរការពាក់កណ្តាលលក្ខណៈវិញ្ញាណលើកាលលើកមួយនៃបង្កត់ត្រាច្រេីនលាន
- **ពេលចម្លើយយឺតយ៉ាវ** - អ្នកប្រើប្រាស់រង់ចាំពេលទិន្នន័យទាំងអស់ត្រូវបានដំណើរការ
- **កំហុសពេលអស់កំណត់** - សំណើលើសកំណត់ពេលអស់កំណត់
- **ការសមត្ថភាព AI យឺត** - LLMs មានការលំបាកជាមួយបរិបទធំៗ

MCP ប្រើប្រាស់ **ការបំបែកទំព័រដោយ Cursor** សម្រាប់ការកំណត់ទំព័រដោយទាន់ចិត្ត និងអាចទុកចិត្តបានតាមលំដាប់លទ្ធផល។

---

## របៀបដែលការបំបែកទំព័រនៅ MCP ដំណើរការ

### គំនិត Cursor

**Cursor** គឺជាច្រកពាក្យដែលមិនបញ្ចេញតម្លៃ សម្គាល់ទីតាំងរបស់អ្នកនៅក្នុងសំណុំលទ្ធផល។ គិតថាវាដូចជាគន្លងសៀវភៅនៅក្នុងសៀវភៅវែងមួយ។

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: tools/list (គ្មានកូសរ)
    Server-->>Client: tools [1-10], nextCursor: "abc123"
    
    Client->>Server: tools/list (cursor: "abc123")
    Server-->>Client: tools [11-20], nextCursor: "def456"
    
    Client->>Server: tools/list (cursor: "def456")
    Server-->>Client: tools [21-25], nextCursor: null (បញ្ចប់)
```

### ការបំបែកទំព័រនៅក្នុងវិធីសាស្រ្ត MCP

វិធីសាស្រ្ត MCP ទាំងនេះគាំទ្រការបំបែកទំព័រ៖

| វិធីសាស្រ្ត | ត្រឡប់ | គាំទ្រ Cursor |
|--------|---------|----------------|
| `tools/list` | ការបញ្ជាក់ឧបករណ៍ | ✅ |
| `resources/list` | ការបញ្ជាក់ធនធាន | ✅ |
| `prompts/list` | ការបញ្ជាក់សំណើ | ✅ |
| `resources/templates/list` | គំរូធនធាន | ✅ |

---

## ការអនុវត្តន៍ម៉ាស៊ីនមេ

### Python (FastMCP)

```python
from mcp.server import Server
from mcp.types import Tool, ListToolsResult
import math

app = Server("paginated-server")

# ទិន្នន័យធំដែលបានច្រកស៊ុម
ALL_TOOLS = [
    Tool(name=f"tool_{i}", description=f"Tool number {i}", inputSchema={})
    for i in range(100)
]

PAGE_SIZE = 10

@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    """List tools with pagination support."""
    
    # បកស្រាយក័រហ្ស័រដើម្បីទទួលបានលេខសម្គាល់ចាប់ផ្ដើម
    start_index = 0
    if cursor:
        try:
            start_index = int(cursor)
        except ValueError:
            start_index = 0
    
    # ទទួលយកទំព័រវិលតប
    end_index = min(start_index + PAGE_SIZE, len(ALL_TOOLS))
    page_tools = ALL_TOOLS[start_index:end_index]
    
    # គណនាក័រហ្ស័របន្ទាប់
    next_cursor = None
    if end_index < len(ALL_TOOLS):
        next_cursor = str(end_index)
    
    return ListToolsResult(
        tools=page_tools,
        nextCursor=next_cursor
    )
```

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { ListToolsResultSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server({
  name: "paginated-server",
  version: "1.0.0"
});

// ចំណងជើងទិន្នន័យធំបានចាក់សោ
const ALL_TOOLS = Array.from({ length: 100 }, (_, i) => ({
  name: `tool_${i}`,
  description: `Tool number ${i}`,
  inputSchema: { type: "object", properties: {} }
}));

const PAGE_SIZE = 10;

server.setRequestHandler(ListToolsResultSchema, async (request) => {
  // បកស្រាយ cursor
  let startIndex = 0;
  if (request.params?.cursor) {
    startIndex = parseInt(request.params.cursor, 10) || 0;
  }
  
  // ទាញយកទំព័រនៃលទ្ធផល
  const endIndex = Math.min(startIndex + PAGE_SIZE, ALL_TOOLS.length);
  const pageTools = ALL_TOOLS.slice(startIndex, endIndex);
  
  // គណនាត្រង់ពេល cursor បន្ទាប់
  const nextCursor = endIndex < ALL_TOOLS.length ? String(endIndex) : undefined;
  
  return {
    tools: pageTools,
    nextCursor
  };
});
```

### Java (Spring MCP)

```java
@Service
public class PaginatedToolService {
    
    private static final int PAGE_SIZE = 10;
    private final List<Tool> allTools;
    
    public PaginatedToolService() {
        // ចាប់ផ្តើមបង្កើតសំណុំទិន្នន័យធំ
        this.allTools = IntStream.range(0, 100)
            .mapToObj(i -> new Tool("tool_" + i, "Tool number " + i, Map.of()))
            .collect(Collectors.toList());
    }
    
    @McpMethod("tools/list")
    public ListToolsResult listTools(@Param("cursor") String cursor) {
        // បកប្រែ cursor
        int startIndex = 0;
        if (cursor != null && !cursor.isEmpty()) {
            try {
                startIndex = Integer.parseInt(cursor);
            } catch (NumberFormatException e) {
                startIndex = 0;
            }
        }
        
        // ទទួលបានទំព័រវិញនៃលទ្ធផល
        int endIndex = Math.min(startIndex + PAGE_SIZE, allTools.size());
        List<Tool> pageTools = allTools.subList(startIndex, endIndex);
        
        // គណនារាបរបួស cursor បន្ទាប់
        String nextCursor = endIndex < allTools.size() ? String.valueOf(endIndex) : null;
        
        return new ListToolsResult(pageTools, nextCursor);
    }
}
```

---

## ការអនុវត្តន៍ភាគីអតិថិជន

### អតិថិជន Python

```python
from mcp import ClientSession

async def get_all_tools(session: ClientSession) -> list:
    """Fetch all tools using pagination."""
    all_tools = []
    cursor = None
    
    while True:
        result = await session.list_tools(cursor=cursor)
        all_tools.extend(result.tools)
        
        if result.nextCursor is None:
            break
        cursor = result.nextCursor
    
    return all_tools

# ការប្រើប្រាស់
async with client_session as session:
    tools = await get_all_tools(session)
    print(f"Found {len(tools)} tools")
```

### អតិថិជន TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";

async function getAllTools(client: Client): Promise<Tool[]> {
  const allTools: Tool[] = [];
  let cursor: string | undefined = undefined;
  
  do {
    const result = await client.listTools({ cursor });
    allTools.push(...result.tools);
    cursor = result.nextCursor;
  } while (cursor);
  
  return allTools;
}

// ការប្រើប្រាស់
const tools = await getAllTools(client);
console.log(`Found ${tools.length} tools`);
```

### លំនាំបញ្ចូលដាក់យឺត

សម្រាប់សំណុំទិន្នន័យធំធេង, ដាក់បង្ហាញទំព័រតាមតម្រូវការ៖

```python
class PaginatedToolIterator:
    """Lazily iterate through paginated tools."""
    
    def __init__(self, session: ClientSession):
        self.session = session
        self.cursor = None
        self.buffer = []
        self.exhausted = False
    
    async def __anext__(self):
        # ត្រឡប់ពីហត្ថភារក្នុងបារម្ភបើមាន
        if self.buffer:
            return self.buffer.pop(0)
        
        # ពិនិត្យមើលថាតើយើងបានប្រើប្រាស់ទំព័រទាំងអស់រួចរួមទេ
        if self.exhausted:
            raise StopAsyncIteration
        
        # ទាញយកទំព័របន្ទាប់
        result = await self.session.list_tools(cursor=self.cursor)
        self.buffer = list(result.tools)
        self.cursor = result.nextCursor
        
        if self.cursor is None:
            self.exhausted = True
        
        if not self.buffer:
            raise StopAsyncIteration
        
        return self.buffer.pop(0)
    
    def __aiter__(self):
        return self

# ការប្រើប្រាស់ - មានប្រសិទ្ធភាពកន្លះចងចាំសម្រាប់ប្រភេទទិន្នន័យធំនា
async for tool in PaginatedToolIterator(session):
    process_tool(tool)
```

---

## ការបំបែកទំព័រសម្រាប់ធនធាន

ធនធានជាញឹកញាប់ត្រូវការការបំបែកទំព័រសម្រាប់ថតឯកសារ ឬសំណុំទិន្នន័យធំៗ៖

```python
from mcp.server import Server
from mcp.types import Resource, ListResourcesResult
import os

app = Server("file-server")

@app.list_resources()
async def list_resources(cursor: str | None = None) -> ListResourcesResult:
    """List files in directory with pagination."""
    
    directory = "/data/files"
    all_files = sorted(os.listdir(directory))
    
    # បកប្រែ​សរសេរ​យោង (ផ្សាយ​ឯកសារ)
    start_index = int(cursor) if cursor else 0
    page_size = 20
    end_index = min(start_index + page_size, len(all_files))
    
    # បង្កើត បញ្ជីធនធាន សម្រាប់ទំព័រនេះ
    resources = []
    for filename in all_files[start_index:end_index]:
        filepath = os.path.join(directory, filename)
        resources.append(Resource(
            uri=f"file://{filepath}",
            name=filename,
            mimeType="application/octet-stream"
        ))
    
    # គណនា​សរសេរ​យោង​បន្ទាប់
    next_cursor = str(end_index) if end_index < len(all_files) else None
    
    return ListResourcesResult(
        resources=resources,
        nextCursor=next_cursor
    )
```

---

## យុទ្ធសាស្រ្តការរចនា Cursor

### យុទ្ធសាស្រ្ត ១៖ អាស្រ័យលើវិញ្ញាណ (សាមញ្ញ)

```python
# អក្សរម៉ោងគឺជាផ្ទាំងលេខតែប៉ុណ្ណោះ
cursor = "50"  # ចាប់ផ្តើមពីធាតុ ៥០
```

**អត្ថប្រយោជន៍៖** សាមញ្ញ, មិនអាចរកឃើញស្ថានភាព
**គុណវិបត្តិ៖** លទ្ធផលអាចផ្លាស់ប្តូរបើធាតុត្រូវបានបន្ថែម/យកចេញ

### យុទ្ធសាស្រ្ត ២៖ អាស្រ័យលើ ID (មានស្ថិតិភាព)

```python
# កូនសោគឺជាផ្ទាំង ID ចុងក្រោយដែលបានឃើញ
cursor = "item_abc123"  # ចាប់ផ្តើមបន្ទាប់ពីធាតុនេះ
```

**អត្ថប្រយោជន៍៖** មានស្ថិតិភាពទោះបីធាតុផ្លាស់ប្តូរនោះក៏ដោយ
**គុណវិបត្តិ៖** ត្រូវការលំដាប់ ID

### យុទ្ធសាស្រ្ត ៣៖ ស្ថានភាពអាស្រ័យលើកូដ (ស្មុគស្មាញ)

```python
import base64
import json

def encode_cursor(state: dict) -> str:
    return base64.b64encode(json.dumps(state).encode()).decode()

def decode_cursor(cursor: str) -> dict:
    return json.loads(base64.b64decode(cursor).decode())

# មួយចំនួននៃកន្លែងស្ថិតិក្នុងអ័ក្សឈរ​មានច្រើន​ស្ថានភាព
cursor = encode_cursor({
    "offset": 50,
    "filter": "active",
    "sort": "name"
})
```

**អត្ថប្រយោជន៍៖** អាចកូដស្ថានភាពស្មុគស្មាញ
**គុណវិបត្តិ៖** ស្មុគស្មាញជាងនេះ, ខ្សែឈរនៃ Cursor ធំជាង

---

## គោលបទល្អបំផុត

### ១. ជ្រើសរើសទំហំទំព័រឱ្យសមរម្យ

```python
# ពិចារណាអំពីទំហំទិន្នន័យ
PAGE_SIZE_SMALL_ITEMS = 100   # ព័ត៌មានមេតាទិន្នន័យងាយស្រួល
PAGE_SIZE_MEDIUM_ITEMS = 20   # វត្ថុមានភាពសំបូរជាង
PAGE_SIZE_LARGE_ITEMS = 5     # មាតិកាស្មុគស្មាញ
```

### ២. ជួយកាន់តែផ្តោតលើ Cursor មិនត្រឹមត្រូវ

```python
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    try:
        start_index = int(cursor) if cursor else 0
        if start_index < 0 or start_index >= len(ALL_TOOLS):
            start_index = 0  # កំណត់ឡើងវិញទៅដើម
    except (ValueError, TypeError):
        start_index = 0  # តំណក្រិចមិនត្រឹមត្រូវ ចាប់ផ្តើមថ្មី
    # ...
```

### ៣. បញ្ចូល បរិមាណសរុប (អាចជាជម្រើស)

```python
return ListToolsResult(
    tools=page_tools,
    nextCursor=next_cursor,
    # ការអនុវត្តខ្លះមានរួមបញ្ចូលទាំងសរុបសម្រាប់វឌ្ឍនភាព UI
    _meta={"total": len(ALL_TOOLS)}
)
```

### ៤. សាកល្បងករណីគ្រោងកាច់

```python
async def test_pagination():
    # តម្លៃលទ្ធផលទទេ
    result = await session.list_tools()
    assert result.tools == []
    assert result.nextCursor is None
    
    # មួយទំព័រ
    result = await session.list_tools()
    assert len(result.tools) <= PAGE_SIZE
    
    # អក្សរបង្ហាញមិនត្រឹមត្រូវ
    result = await session.list_tools(cursor="invalid")
    assert result.tools  # ត្រូវតែបញ្ជូនទំព័រដំបូងវិញ
```

---

## កំហុសទូទៅ

### ❌ ត្រឡប់លទ្ធផលទាំងអស់ហើយធ្វើការបំបែកទំព័រក្នុងភាគីអតិថិជន

```python
# អាក្រក់៖ ផ្ទុករឿងគ្រប់យ៉ាងចូលទៅក្នុងអង្គចងចាំ
@app.list_tools()
async def list_tools() -> ListToolsResult:
    all_tools = load_all_tools()  # ឧបករណ៍ 1 លាន!
    return ListToolsResult(tools=all_tools)
```

### ✅ បំបែកទំព័រនៅប្រភពទិន្នន័យ

```python
# ល្អ: ផ្ទុកតែអ្វីដែលចាំបាច់តែប៉ុណ្ណោះ
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    offset = int(cursor) if cursor else 0
    tools = await db.query_tools(offset=offset, limit=PAGE_SIZE)
    return ListToolsResult(tools=tools, nextCursor=...)
```

---

## តើអ្វីទៅជាផ្នែកបន្ទាប់

- [Module 5.14 - Context Engineering](../../05-AdvancedTopics/mcp-contextengineering/README.md)
- [Module 8 - Best Practices](../../08-BestPractices/README.md)
- [3.8 - Testing Your MCP Server](../../03-GettingStarted/08-testing/README.md)

---

## ធនធានបន្ថែម

- [MCP Specification - Pagination](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Cursor-Based Pagination Explained](https://slack.engineering/evolving-api-pagination-at-slack/)
- [Python SDK pagination tests](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->