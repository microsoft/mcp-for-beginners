# Paginacja i duże zestawy wyników w MCP

Kiedy twój serwer MCP obsługuje duże zestawy danych - czy to listując tysiące plików, rekordów bazy danych, czy wyników wyszukiwania - potrzebujesz paginacji, aby efektywnie zarządzać pamięcią i zapewnić responsywne doświadczenia użytkownika. Ten przewodnik opisuje, jak zaimplementować i korzystać z paginacji w MCP.

## Dlaczego paginacja jest ważna

Bez paginacji duże odpowiedzi mogą powodować:

- **Wyczerpanie pamięci** - ładowanie milionów rekordów naraz
- **Wolne czasy odpowiedzi** - użytkownicy czekają, aż wszystkie dane się załadują
- **Błędy przekroczenia limitu czasu** - zapytania przekraczają limity czasu oczekiwania
- **Słaba wydajność AI** - modele LLM mają trudności z ogromnym kontekstem

MCP używa **paginacji opartej na kursorze**, aby zapewnić niezawodne i spójne przechodzenie przez zestawy wyników.

---

## Jak działa paginacja w MCP

### Koncepcja kursora

**Kursor** to nieprzejrzysty ciąg znaków, który zaznacza twoją pozycję w zestawie wyników. Można go porównać do zakładki w długiej książce.

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: tools/list (bez wskaźnika)
    Server-->>Client: tools [1-10], nextCursor: "abc123"
    
    Client->>Server: tools/list (wskaźnik: "abc123")
    Server-->>Client: tools [11-20], nextCursor: "def456"
    
    Client->>Server: tools/list (wskaźnik: "def456")
    Server-->>Client: tools [21-25], nextCursor: null (koniec)
```

### Paginacja w metodach MCP

Te metody MCP obsługują paginację:

| Metoda | Zwraca | Obsługa kursora |
|--------|---------|-----------------|
| `tools/list` | Definicje narzędzi | ✅ |
| `resources/list` | Definicje zasobów | ✅ |
| `prompts/list` | Definicje promptów | ✅ |
| `resources/templates/list` | Szablony zasobów | ✅ |

---

## Implementacja serwera

### Python (FastMCP)

```python
from mcp.server import Server
from mcp.types import Tool, ListToolsResult
import math

app = Server("paginated-server")

# Symulowany duży zestaw danych
ALL_TOOLS = [
    Tool(name=f"tool_{i}", description=f"Tool number {i}", inputSchema={})
    for i in range(100)
]

PAGE_SIZE = 10

@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    """List tools with pagination support."""
    
    # Dekoduj kursor, aby uzyskać indeks początkowy
    start_index = 0
    if cursor:
        try:
            start_index = int(cursor)
        except ValueError:
            start_index = 0
    
    # Pobierz stronę wyników
    end_index = min(start_index + PAGE_SIZE, len(ALL_TOOLS))
    page_tools = ALL_TOOLS[start_index:end_index]
    
    # Oblicz następny kursor
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

// Symulowany duży zestaw danych
const ALL_TOOLS = Array.from({ length: 100 }, (_, i) => ({
  name: `tool_${i}`,
  description: `Tool number ${i}`,
  inputSchema: { type: "object", properties: {} }
}));

const PAGE_SIZE = 10;

server.setRequestHandler(ListToolsResultSchema, async (request) => {
  // Dekoduj kursor
  let startIndex = 0;
  if (request.params?.cursor) {
    startIndex = parseInt(request.params.cursor, 10) || 0;
  }
  
  // Pobierz stronę wyników
  const endIndex = Math.min(startIndex + PAGE_SIZE, ALL_TOOLS.length);
  const pageTools = ALL_TOOLS.slice(startIndex, endIndex);
  
  // Oblicz następny kursor
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
        // Inicjalizuj duży zbiór danych
        this.allTools = IntStream.range(0, 100)
            .mapToObj(i -> new Tool("tool_" + i, "Tool number " + i, Map.of()))
            .collect(Collectors.toList());
    }
    
    @McpMethod("tools/list")
    public ListToolsResult listTools(@Param("cursor") String cursor) {
        // Dekoduj kursor
        int startIndex = 0;
        if (cursor != null && !cursor.isEmpty()) {
            try {
                startIndex = Integer.parseInt(cursor);
            } catch (NumberFormatException e) {
                startIndex = 0;
            }
        }
        
        // Pobierz stronę wyników
        int endIndex = Math.min(startIndex + PAGE_SIZE, allTools.size());
        List<Tool> pageTools = allTools.subList(startIndex, endIndex);
        
        // Oblicz następny kursor
        String nextCursor = endIndex < allTools.size() ? String.valueOf(endIndex) : null;
        
        return new ListToolsResult(pageTools, nextCursor);
    }
}
```

---

## Implementacja klienta

### Klient Python

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

# Użycie
async with client_session as session:
    tools = await get_all_tools(session)
    print(f"Found {len(tools)} tools")
```

### Klient TypeScript

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

// Użytkowanie
const tools = await getAllTools(client);
console.log(`Found ${tools.length} tools`);
```

### Wzorzec leniwego ładowania

Dla bardzo dużych zbiorów danych ładuj strony na żądanie:

```python
class PaginatedToolIterator:
    """Lazily iterate through paginated tools."""
    
    def __init__(self, session: ClientSession):
        self.session = session
        self.cursor = None
        self.buffer = []
        self.exhausted = False
    
    async def __anext__(self):
        # Zwróć z bufora, jeśli dostępne
        if self.buffer:
            return self.buffer.pop(0)
        
        # Sprawdź, czy wyczerpaliśmy wszystkie strony
        if self.exhausted:
            raise StopAsyncIteration
        
        # Pobierz następną stronę
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

# Użycie - efektywne pod względem pamięci dla dużych zbiorów danych
async for tool in PaginatedToolIterator(session):
    process_tool(tool)
```

---

## Paginacja zasobów

Zasoby często wymagają paginacji dla katalogów lub dużych zestawów danych:

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
    
    # Dekoduj kursor (indeks pliku)
    start_index = int(cursor) if cursor else 0
    page_size = 20
    end_index = min(start_index + page_size, len(all_files))
    
    # Utwórz listę zasobów dla tej strony
    resources = []
    for filename in all_files[start_index:end_index]:
        filepath = os.path.join(directory, filename)
        resources.append(Resource(
            uri=f"file://{filepath}",
            name=filename,
            mimeType="application/octet-stream"
        ))
    
    # Oblicz następny kursor
    next_cursor = str(end_index) if end_index < len(all_files) else None
    
    return ListResourcesResult(
        resources=resources,
        nextCursor=next_cursor
    )
```

---

## Strategie projektowania kursora

### Strategia 1: Indeksowa (prosta)

```python
# Kursor to tylko indeks
cursor = "50"  # Zacznij od elementu 50
```

**Zalety:** Prosta, bezstanowa
**Wady:** Wyniki mogą się przesuwać, jeśli dodawane/usuwane są elementy

### Strategia 2: Na podstawie ID (stabilna)

```python
# Kursor to ostatnio widziane ID
cursor = "item_abc123"  # Zacznij po tym elemencie
```

**Zalety:** Stabilna nawet przy zmianach elementów
**Wady:** Wymaga uporządkowanych ID

### Strategia 3: Zakodowany stan (złożona)

```python
import base64
import json

def encode_cursor(state: dict) -> str:
    return base64.b64encode(json.dumps(state).encode()).decode()

def decode_cursor(cursor: str) -> dict:
    return json.loads(base64.b64decode(cursor).decode())

# Kursor zawiera wiele pól stanu
cursor = encode_cursor({
    "offset": 50,
    "filter": "active",
    "sort": "name"
})
```

**Zalety:** Może kodować złożony stan
**Wady:** Bardziej złożona, większe ciągi kursora

---

## Najlepsze praktyki

### 1. Wybieraj odpowiednie rozmiary stron

```python
# Rozważ rozmiar danych
PAGE_SIZE_SMALL_ITEMS = 100   # Proste metadane
PAGE_SIZE_MEDIUM_ITEMS = 20   # Bardziej złożone obiekty
PAGE_SIZE_LARGE_ITEMS = 5     # Złożona zawartość
```

### 2. Obsługuj nieprawidłowe kursory łagodnie

```python
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    try:
        start_index = int(cursor) if cursor else 0
        if start_index < 0 or start_index >= len(ALL_TOOLS):
            start_index = 0  # Resetuj do początku
    except (ValueError, TypeError):
        start_index = 0  # Nieprawidłowy kursor, zacznij od nowa
    # ...
```

### 3. Uwzględniaj całkowitą liczbę (opcjonalnie)

```python
return ListToolsResult(
    tools=page_tools,
    nextCursor=next_cursor,
    # Niektóre implementacje zawierają łączną sumę dla postępu interfejsu użytkownika
    _meta={"total": len(ALL_TOOLS)}
)
```

### 4. Testuj przypadki brzegowe

```python
async def test_pagination():
    # Pusty zbiór wyników
    result = await session.list_tools()
    assert result.tools == []
    assert result.nextCursor is None
    
    # Pojedyncza strona
    result = await session.list_tools()
    assert len(result.tools) <= PAGE_SIZE
    
    # Nieprawidłowy kursor
    result = await session.list_tools(cursor="invalid")
    assert result.tools  # Powinno zwrócić pierwszą stronę
```

---

## Typowe pułapki

### ❌ Zwracanie wszystkich wyników, a następnie paginacja po stronie klienta

```python
# ZŁE: Ładuje wszystko do pamięci
@app.list_tools()
async def list_tools() -> ListToolsResult:
    all_tools = load_all_tools()  # 1 milion narzędzi!
    return ListToolsResult(tools=all_tools)
```

### ✅ Paginacja u źródła danych

```python
# DOBRZE: Ładuje tylko to, co jest potrzebne
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    offset = int(cursor) if cursor else 0
    tools = await db.query_tools(offset=offset, limit=PAGE_SIZE)
    return ListToolsResult(tools=tools, nextCursor=...)
```

---

## Co dalej

- [Moduł 5.14 - Inżynieria kontekstu](../../05-AdvancedTopics/mcp-contextengineering/README.md)
- [Moduł 8 - Najlepsze praktyki](../../08-BestPractices/README.md)
- [3.8 - Testowanie twojego serwera MCP](../../03-GettingStarted/08-testing/README.md)

---

## Dodatkowe zasoby

- [Specyfikacja MCP - Paginacja](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Wyjaśnienie paginacji opartej na kursorze](https://slack.engineering/evolving-api-pagination-at-slack/)
- [Testy paginacji w Python SDK](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->