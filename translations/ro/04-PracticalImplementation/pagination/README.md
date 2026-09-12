# Paginarea și Seturile Mari de Rezultate în MCP

Când serverul tău MCP gestionează seturi mari de date - fie listând mii de fișiere, înregistrări din bazele de date sau rezultate ale căutărilor - ai nevoie de paginare pentru a gestiona memoria eficient și a oferi experiențe de utilizator rapide. Acest ghid explică cum să implementezi și să folosești paginarea în MCP.

## De ce este importantă Paginarea

Fără paginare, răspunsurile mari pot cauza:

- **Epuizarea memoriei** - Încărcarea a milioane de înregistrări simultan
- **Timpuri lente de răspuns** - Utilizatorii așteaptă până când toate datele se încarcă
- **Erori de timeout** - Cererile depășesc limitele de timp
- **Performanță slabă AI** - LLM-urile au dificultăți cu un context masiv

MCP folosește **paginare bazată pe cursor** pentru o paginare fiabilă și constantă prin seturile de rezultate.

---

## Cum Funcționează Paginarea în MCP

### Conceptul de Cursor

Un **cursor** este un șir opac care marchează poziția ta într-un set de rezultate. Gândește-te la el ca la un semn de carte într-o carte lungă.

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: tools/list (fără cursor)
    Server-->>Client: tools [1-10], nextCursor: "abc123"
    
    Client->>Server: tools/list (cursor: "abc123")
    Server-->>Client: tools [11-20], nextCursor: "def456"
    
    Client->>Server: tools/list (cursor: "def456")
    Server-->>Client: tools [21-25], nextCursor: null (sfârșit)
```

### Paginarea în Metodele MCP

Aceste metode MCP suportă paginare:

| Metodă | Returnează | Suport Cursor |
|--------|---------|----------------|
| `tools/list` | Definiții unelte | ✅ |
| `resources/list` | Definiții resurse | ✅ |
| `prompts/list` | Definiții prompturi | ✅ |
| `resources/templates/list` | Șabloane resurse | ✅ |

---

## Implementare Server

### Python (FastMCP)

```python
from mcp.server import Server
from mcp.types import Tool, ListToolsResult
import math

app = Server("paginated-server")

# Set de date simulat mare
ALL_TOOLS = [
    Tool(name=f"tool_{i}", description=f"Tool number {i}", inputSchema={})
    for i in range(100)
]

PAGE_SIZE = 10

@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    """List tools with pagination support."""
    
    # Decodează cursorul pentru a obține indexul de pornire
    start_index = 0
    if cursor:
        try:
            start_index = int(cursor)
        except ValueError:
            start_index = 0
    
    # Obține pagina de rezultate
    end_index = min(start_index + PAGE_SIZE, len(ALL_TOOLS))
    page_tools = ALL_TOOLS[start_index:end_index]
    
    # Calculează următorul cursor
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

// Set de date mare simulat
const ALL_TOOLS = Array.from({ length: 100 }, (_, i) => ({
  name: `tool_${i}`,
  description: `Tool number ${i}`,
  inputSchema: { type: "object", properties: {} }
}));

const PAGE_SIZE = 10;

server.setRequestHandler(ListToolsResultSchema, async (request) => {
  // Decodează cursorul
  let startIndex = 0;
  if (request.params?.cursor) {
    startIndex = parseInt(request.params.cursor, 10) || 0;
  }
  
  // Obține pagina de rezultate
  const endIndex = Math.min(startIndex + PAGE_SIZE, ALL_TOOLS.length);
  const pageTools = ALL_TOOLS.slice(startIndex, endIndex);
  
  // Calculează cursorul următor
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
        // Inițializează setul mare de date
        this.allTools = IntStream.range(0, 100)
            .mapToObj(i -> new Tool("tool_" + i, "Tool number " + i, Map.of()))
            .collect(Collectors.toList());
    }
    
    @McpMethod("tools/list")
    public ListToolsResult listTools(@Param("cursor") String cursor) {
        // Decodează cursorul
        int startIndex = 0;
        if (cursor != null && !cursor.isEmpty()) {
            try {
                startIndex = Integer.parseInt(cursor);
            } catch (NumberFormatException e) {
                startIndex = 0;
            }
        }
        
        // Obține pagina de rezultate
        int endIndex = Math.min(startIndex + PAGE_SIZE, allTools.size());
        List<Tool> pageTools = allTools.subList(startIndex, endIndex);
        
        // Calculează următorul cursor
        String nextCursor = endIndex < allTools.size() ? String.valueOf(endIndex) : null;
        
        return new ListToolsResult(pageTools, nextCursor);
    }
}
```

---

## Implementare Client

### Client Python

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

# Utilizare
async with client_session as session:
    tools = await get_all_tools(session)
    print(f"Found {len(tools)} tools")
```

### Client TypeScript

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

// Utilizare
const tools = await getAllTools(client);
console.log(`Found ${tools.length} tools`);
```

### Pattern de Încărcare Lazy

Pentru seturi foarte mari de date, încarcă paginile la cerere:

```python
class PaginatedToolIterator:
    """Lazily iterate through paginated tools."""
    
    def __init__(self, session: ClientSession):
        self.session = session
        self.cursor = None
        self.buffer = []
        self.exhausted = False
    
    async def __anext__(self):
        # Returnează din buffer dacă este disponibil
        if self.buffer:
            return self.buffer.pop(0)
        
        # Verifică dacă am epuizat toate paginile
        if self.exhausted:
            raise StopAsyncIteration
        
        # Preia pagina următoare
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

# Utilizare - eficient din punct de vedere al memoriei pentru seturi mari de date
async for tool in PaginatedToolIterator(session):
    process_tool(tool)
```

---

## Paginarea pentru Resurse

Resursele au adesea nevoie de paginare pentru directoare sau seturi mari de date:

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
    
    # Decodează cursorul (indexul fișierului)
    start_index = int(cursor) if cursor else 0
    page_size = 20
    end_index = min(start_index + page_size, len(all_files))
    
    # Creează lista de resurse pentru această pagină
    resources = []
    for filename in all_files[start_index:end_index]:
        filepath = os.path.join(directory, filename)
        resources.append(Resource(
            uri=f"file://{filepath}",
            name=filename,
            mimeType="application/octet-stream"
        ))
    
    # Calculează următorul cursor
    next_cursor = str(end_index) if end_index < len(all_files) else None
    
    return ListResourcesResult(
        resources=resources,
        nextCursor=next_cursor
    )
```

---

## Strategii de Design pentru Cursor

### Strategia 1: Bazată pe Index (Simplă)

```python
# Cursorul este doar indexul
cursor = "50"  # Începe la elementul 50
```

**Pro:** Simplu, fără stare
**Contra:** Rezultatele pot fi modificate dacă se adaugă/scoate elemente

### Strategia 2: Bazată pe ID (Stabilă)

```python
# Cursorul este ultimul ID văzut
cursor = "item_abc123"  # Începe după acest element
```

**Pro:** Stabil chiar dacă elementele se schimbă
**Contra:** Necesită ID-uri ordonate

### Strategia 3: Stare Codificată (Complexă)

```python
import base64
import json

def encode_cursor(state: dict) -> str:
    return base64.b64encode(json.dumps(state).encode()).decode()

def decode_cursor(cursor: str) -> dict:
    return json.loads(base64.b64decode(cursor).decode())

# Cursorul conține mai multe câmpuri de stare
cursor = encode_cursor({
    "offset": 50,
    "filter": "active",
    "sort": "name"
})
```

**Pro:** Poate codifica stări complexe
**Contra:** Mai complexă, șiruri de cursor mai mari

---

## Cele Mai Bune Practici

### 1. Alege Dimensiuni Potrivite pentru Pagină

```python
# Ia în considerare dimensiunea datelor
PAGE_SIZE_SMALL_ITEMS = 100   # Metadate simple
PAGE_SIZE_MEDIUM_ITEMS = 20   # Obiecte mai bogate
PAGE_SIZE_LARGE_ITEMS = 5     # Conținut complex
```

### 2. Gestionează Cursorii Invălizi cu Grație

```python
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    try:
        start_index = int(cursor) if cursor else 0
        if start_index < 0 or start_index >= len(ALL_TOOLS):
            start_index = 0  # Resetează la început
    except (ValueError, TypeError):
        start_index = 0  # Cursor nevalid, începe de la capăt
    # ...
```

### 3. Include Numărul Total (Opțional)

```python
return ListToolsResult(
    tools=page_tools,
    nextCursor=next_cursor,
    # Unele implementări includ totalul pentru progresul UI
    _meta={"total": len(ALL_TOOLS)}
)
```

### 4. Testează Cazurile Limită

```python
async def test_pagination():
    # Set de rezultate gol
    result = await session.list_tools()
    assert result.tools == []
    assert result.nextCursor is None
    
    # Pagină unică
    result = await session.list_tools()
    assert len(result.tools) <= PAGE_SIZE
    
    # Cursor invalid
    result = await session.list_tools(cursor="invalid")
    assert result.tools  # Ar trebui să returneze prima pagină
```

---

## Capcane Comune

### ❌ Returnarea tuturor rezultatelor apoi paginarea pe client

```python
# RĂU: Încarcă totul în memorie
@app.list_tools()
async def list_tools() -> ListToolsResult:
    all_tools = load_all_tools()  # 1 milion de unelte!
    return ListToolsResult(tools=all_tools)
```

### ✅ Paginați la Sursa de Date

```python
# BUN: Încarcă doar ce este necesar
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    offset = int(cursor) if cursor else 0
    tools = await db.query_tools(offset=offset, limit=PAGE_SIZE)
    return ListToolsResult(tools=tools, nextCursor=...)
```

---

## Ce Urmează

- [Modul 5.14 - Ingineria Contextului](../../05-AdvancedTopics/mcp-contextengineering/README.md)
- [Modul 8 - Cele Mai Bune Practici](../../08-BestPractices/README.md)
- [3.8 - Testarea Serverului MCP](../../03-GettingStarted/08-testing/README.md)

---

## Resurse Suplimentare

- [Specificația MCP - Paginare](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Paginarea bazată pe cursor explicată](https://slack.engineering/evolving-api-pagination-at-slack/)
- [Teste paginare SDK Python](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->