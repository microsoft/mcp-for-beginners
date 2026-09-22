# MCP'de Sayfalama ve Büyük Sonuç Setleri

MCP sunucunuz binlerce dosya, veri tabanı kaydı veya arama sonucu listelemek gibi büyük veri setlerini işlediğinde, belleği verimli yönetmek ve duyarlı kullanıcı deneyimi sağlamak için sayfalama gerekir. Bu kılavuz, MCP'de sayfalamanın nasıl uygulanacağını ve kullanılacağını ele almaktadır.

## Sayfalama Neden Önemlidir

Sayfalama olmadan, büyük yanıtlar şunlara neden olabilir:

- **Bellek tükenmesi** - Milyonlarca kaydı bir kerede yüklemek
- **Yavaş yanıt süreleri** - Tüm veri yüklenene kadar kullanıcılar bekler
- **Zaman aşımı hataları** - Talepler zaman aşımı sınırlarını aşar
- **Zayıf yapay zeka performansı** - LLM'ler devasa bağlamda zorlanır

MCP, sonuç setleri arasında güvenilir ve tutarlı sayfalama için **imleç tabanlı sayfalama** kullanır.

---

## MCP Sayfalaması Nasıl Çalışır

### İmleç Kavramı

**İmleç**, sonuç setindeki konumunuzu işaret eden opak bir dizgedir. Uzun bir kitaptaki yer imi gibi düşünebilirsiniz.

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: araçlar/liste (imleç yok)
    Server-->>Client: araçlar [1-10], sonrakiİmleç: "abc123"
    
    Client->>Server: araçlar/liste (imleç: "abc123")
    Server-->>Client: araçlar [11-20], sonrakiİmleç: "def456"
    
    Client->>Server: araçlar/liste (imleç: "def456")
    Server-->>Client: araçlar [21-25], sonrakiİmleç: null (bitiş)
```

### MCP Metotlarında Sayfalama

Bu MCP metotları sayfalama desteği sunar:

| Metot | Döner | İmleç Desteği |
|--------|---------|----------------|
| `tools/list` | Araç tanımları | ✅ |
| `resources/list` | Kaynak tanımları | ✅ |
| `prompts/list` | İstek tanımları | ✅ |
| `resources/templates/list` | Kaynak şablonları | ✅ |

---

## Sunucu Uygulaması

### Python (FastMCP)

```python
from mcp.server import Server
from mcp.types import Tool, ListToolsResult
import math

app = Server("paginated-server")

# Simüle edilmiş büyük veri seti
ALL_TOOLS = [
    Tool(name=f"tool_{i}", description=f"Tool number {i}", inputSchema={})
    for i in range(100)
]

PAGE_SIZE = 10

@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    """List tools with pagination support."""
    
    # Başlangıç indeksini almak için imleci çöz
    start_index = 0
    if cursor:
        try:
            start_index = int(cursor)
        except ValueError:
            start_index = 0
    
    # Sonuç sayfasını al
    end_index = min(start_index + PAGE_SIZE, len(ALL_TOOLS))
    page_tools = ALL_TOOLS[start_index:end_index]
    
    # Sonraki imleci hesapla
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

// Simüle edilmiş büyük veri seti
const ALL_TOOLS = Array.from({ length: 100 }, (_, i) => ({
  name: `tool_${i}`,
  description: `Tool number ${i}`,
  inputSchema: { type: "object", properties: {} }
}));

const PAGE_SIZE = 10;

server.setRequestHandler(ListToolsResultSchema, async (request) => {
  // İmleci çöz
  let startIndex = 0;
  if (request.params?.cursor) {
    startIndex = parseInt(request.params.cursor, 10) || 0;
  }
  
  // Sonuç sayfasını al
  const endIndex = Math.min(startIndex + PAGE_SIZE, ALL_TOOLS.length);
  const pageTools = ALL_TOOLS.slice(startIndex, endIndex);
  
  // Sonraki imleci hesapla
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
        // Büyük veri setini başlat
        this.allTools = IntStream.range(0, 100)
            .mapToObj(i -> new Tool("tool_" + i, "Tool number " + i, Map.of()))
            .collect(Collectors.toList());
    }
    
    @McpMethod("tools/list")
    public ListToolsResult listTools(@Param("cursor") String cursor) {
        // İmleci çöz
        int startIndex = 0;
        if (cursor != null && !cursor.isEmpty()) {
            try {
                startIndex = Integer.parseInt(cursor);
            } catch (NumberFormatException e) {
                startIndex = 0;
            }
        }
        
        // Sonuç sayfasını al
        int endIndex = Math.min(startIndex + PAGE_SIZE, allTools.size());
        List<Tool> pageTools = allTools.subList(startIndex, endIndex);
        
        // Sonraki imleci hesapla
        String nextCursor = endIndex < allTools.size() ? String.valueOf(endIndex) : null;
        
        return new ListToolsResult(pageTools, nextCursor);
    }
}
```

---

## İstemci Uygulaması

### Python İstemci

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

# Kullanım
async with client_session as session:
    tools = await get_all_tools(session)
    print(f"Found {len(tools)} tools")
```

### TypeScript İstemci

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

// Kullanım
const tools = await getAllTools(client);
console.log(`Found ${tools.length} tools`);
```

### Tembel Yükleme Deseni

Çok büyük veri setleri için, sayfaları talep üzerine yükleyin:

```python
class PaginatedToolIterator:
    """Lazily iterate through paginated tools."""
    
    def __init__(self, session: ClientSession):
        self.session = session
        self.cursor = None
        self.buffer = []
        self.exhausted = False
    
    async def __anext__(self):
        # Mevcutsa tampon içinden dön
        if self.buffer:
            return self.buffer.pop(0)
        
        # Tüm sayfaların tükenip tükenmediğini kontrol et
        if self.exhausted:
            raise StopAsyncIteration
        
        # Sonraki sayfayı getir
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

# Kullanım - büyük veri setleri için bellek tasarruflu
async for tool in PaginatedToolIterator(session):
    process_tool(tool)
```

---

## Kaynaklar İçin Sayfalama

Kaynaklar genellikle dizinler veya büyük veri setleri için sayfalama gerektirir:

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
    
    # İmleci çöz (dosya indeksi)
    start_index = int(cursor) if cursor else 0
    page_size = 20
    end_index = min(start_index + page_size, len(all_files))
    
    # Bu sayfa için kaynak listesi oluştur
    resources = []
    for filename in all_files[start_index:end_index]:
        filepath = os.path.join(directory, filename)
        resources.append(Resource(
            uri=f"file://{filepath}",
            name=filename,
            mimeType="application/octet-stream"
        ))
    
    # Sonraki imleci hesapla
    next_cursor = str(end_index) if end_index < len(all_files) else None
    
    return ListResourcesResult(
        resources=resources,
        nextCursor=next_cursor
    )
```

---

## İmleç Tasarım Stratejileri

### Strateji 1: İndeks Tabanlı (Basit)

```python
# İmleç sadece indekstir
cursor = "50"  # 50. öğeden başla
```

**Artıları:** Basit, durum bilgisi yok
**Eksileri:** Eleman eklenip çıkarılırsa sonuçlar kayabilir

### Strateji 2: ID Tabanlı (Kararlı)

```python
# İmleç, en son görülen kimliktir
cursor = "item_abc123"  # Bu öğeden sonra başla
```

**Artıları:** Elemanlar değişse bile kararlı
**Eksileri:** Sıralı ID gerektirir

### Strateji 3: Kodlanmış Durum (Karmaşık)

```python
import base64
import json

def encode_cursor(state: dict) -> str:
    return base64.b64encode(json.dumps(state).encode()).decode()

def decode_cursor(cursor: str) -> dict:
    return json.loads(base64.b64decode(cursor).decode())

# İmleç birden fazla durum alanı içerir
cursor = encode_cursor({
    "offset": 50,
    "filter": "active",
    "sort": "name"
})
```

**Artıları:** Karmaşık durumu kodlayabilir
**Eksileri:** Daha karmaşık, daha büyük imleç dizeleri

---

## En İyi Uygulamalar

### 1. Uygun Sayfa Boyutlarını Seçin

```python
# Veri boyutunu dikkate alın
PAGE_SIZE_SMALL_ITEMS = 100   # Basit metadata
PAGE_SIZE_MEDIUM_ITEMS = 20   # Daha zengin nesneler
PAGE_SIZE_LARGE_ITEMS = 5     # Karmaşık içerik
```

### 2. Geçersiz İmleçleri Zarifçe Ele Alın

```python
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    try:
        start_index = int(cursor) if cursor else 0
        if start_index < 0 or start_index >= len(ALL_TOOLS):
            start_index = 0  # Başlangıca sıfırla
    except (ValueError, TypeError):
        start_index = 0  # Geçersiz imleç, yeniden başla
    # ...
```

### 3. Toplam Sayıyı Dahil Edin (İsteğe Bağlı)

```python
return ListToolsResult(
    tools=page_tools,
    nextCursor=next_cursor,
    # Bazı uygulamalar kullanıcı arayüzü ilerlemesi için toplamı içerir
    _meta={"total": len(ALL_TOOLS)}
)
```

### 4. Kenar Durumlarını Test Edin

```python
async def test_pagination():
    # Boş sonuç kümesi
    result = await session.list_tools()
    assert result.tools == []
    assert result.nextCursor is None
    
    # Tek sayfa
    result = await session.list_tools()
    assert len(result.tools) <= PAGE_SIZE
    
    # Geçersiz gösterge
    result = await session.list_tools(cursor="invalid")
    assert result.tools  # İlk sayfayı döndürmeli
```

---

## Yaygın Tuzaklar

### ❌ Tüm Sonuçları Döndürüp Sonra İstemci Tarafında Sayfalama Yapmak

```python
# KÖTÜ: Her şeyi belleğe yüklüyor
@app.list_tools()
async def list_tools() -> ListToolsResult:
    all_tools = load_all_tools()  # 1 milyon araç!
    return ListToolsResult(tools=all_tools)
```

### ✅ Veri Kaynağında Sayfalama Yapmak

```python
# İYİ: Yalnızca gerekenleri yükler
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    offset = int(cursor) if cursor else 0
    tools = await db.query_tools(offset=offset, limit=PAGE_SIZE)
    return ListToolsResult(tools=tools, nextCursor=...)
```

---

## Sonraki Adımlar

- [Modül 5.14 - Bağlam Mühendisliği](../../05-AdvancedTopics/mcp-contextengineering/README.md)
- [Modül 8 - En İyi Uygulamalar](../../08-BestPractices/README.md)
- [3.8 - MCP Sunucunuzu Test Etmek](../../03-GettingStarted/08-testing/README.md)

---

## Ek Kaynaklar

- [MCP Spesifikasyonu - Sayfalama](https://modelcontextprotocol.io/specification/2026-07-28/)
- [İmleç Tabanlı Sayfalama Açıklaması](https://slack.engineering/evolving-api-pagination-at-slack/)
- [Python SDK sayfalama testleri](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->