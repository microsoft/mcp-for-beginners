# การแบ่งหน้าและชุดผลลัพธ์ขนาดใหญ่ใน MCP

เมื่อเซิร์ฟเวอร์ MCP ของคุณจัดการชุดข้อมูลขนาดใหญ่ — ไม่ว่าจะเป็นการแสดงรายการไฟล์จำนวนหลายพันรายการ บันทึกฐานข้อมูล หรือผลลัพธ์การค้นหา — คุณจำเป็นต้องมีการแบ่งหน้าเพื่อจัดการหน่วยความจำอย่างมีประสิทธิภาพและมอบประสบการณ์ผู้ใช้ที่ตอบสนองได้ดี คู่มือนี้ครอบคลุมวิธีการใช้งานและการนำการแบ่งหน้ามาใช้ใน MCP

## ทำไมการแบ่งหน้าจึงสำคัญ

หากไม่มีการแบ่งหน้า การตอบสนองที่มีขนาดใหญ่อาจทำให้เกิด:

- **หน่วยความจำหมด** — การโหลดบันทึกจำนวนหลายล้านรายการในครั้งเดียว
- **เวลาตอบสนองช้า** — ผู้ใช้ต้องรอขณะโหลดข้อมูลทั้งหมด
- **ข้อผิดพลาดหมดเวลา** — คำขอเกินขีดจำกัดเวลาที่กำหนด
- **ประสิทธิภาพ AI แย่ลง** — LLMs ประสบปัญหากับบริบทที่มีขนาดมหาศาล

MCP ใช้ **การแบ่งหน้าด้วยเคอร์เซอร์** เพื่อให้การแบ่งหน้ามีความน่าเชื่อถือและสม่ำเสมอในการเลื่อนดูชุดผลลัพธ์

---

## การทำงานของการแบ่งหน้าใน MCP

### แนวคิดของเคอร์เซอร์

**เคอร์เซอร์** คือสตริงที่ไม่โปร่งใสซึ่งแสดงตำแหน่งของคุณในชุดผลลัพธ์ คิดว่ามันเหมือนกับการทำบุ๊คมาร์กในหนังสือเล่มยาว

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: เครื่องมือ/รายการ (ไม่มีเคอร์เซอร์)
    Server-->>Client: เครื่องมือ [1-10], เคอร์เซอร์ถัดไป: "abc123"
    
    Client->>Server: เครื่องมือ/รายการ (เคอร์เซอร์: "abc123")
    Server-->>Client: เครื่องมือ [11-20], เคอร์เซอร์ถัดไป: "def456"
    
    Client->>Server: เครื่องมือ/รายการ (เคอร์เซอร์: "def456")
    Server-->>Client: เครื่องมือ [21-25], เคอร์เซอร์ถัดไป: null (สิ้นสุด)
```

### การแบ่งหน้าในเมธอดของ MCP

เมธอด MCP เหล่านี้รองรับการแบ่งหน้า:

| เมธอด | คืนค่า | รองรับเคอร์เซอร์ |
|--------|---------|----------------|
| `tools/list` | นิยามเครื่องมือ | ✅ |
| `resources/list` | นิยามทรัพยากร | ✅ |
| `prompts/list` | นิยามพรอมต์ | ✅ |
| `resources/templates/list` | เทมเพลตทรัพยากร | ✅ |

---

## การใช้งานฝั่งเซิร์ฟเวอร์

### Python (FastMCP)

```python
from mcp.server import Server
from mcp.types import Tool, ListToolsResult
import math

app = Server("paginated-server")

# ชุดข้อมูลขนาดใหญ่ที่จำลองขึ้น
ALL_TOOLS = [
    Tool(name=f"tool_{i}", description=f"Tool number {i}", inputSchema={})
    for i in range(100)
]

PAGE_SIZE = 10

@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    """List tools with pagination support."""
    
    # ถอดรหัสเคอร์เซอร์เพื่อรับดัชนีเริ่มต้น
    start_index = 0
    if cursor:
        try:
            start_index = int(cursor)
        except ValueError:
            start_index = 0
    
    # รับหน้าของผลลัพธ์
    end_index = min(start_index + PAGE_SIZE, len(ALL_TOOLS))
    page_tools = ALL_TOOLS[start_index:end_index]
    
    # คำนวณเคอร์เซอร์ถัดไป
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

// ชุดข้อมูลขนาดใหญ่จำลอง
const ALL_TOOLS = Array.from({ length: 100 }, (_, i) => ({
  name: `tool_${i}`,
  description: `Tool number ${i}`,
  inputSchema: { type: "object", properties: {} }
}));

const PAGE_SIZE = 10;

server.setRequestHandler(ListToolsResultSchema, async (request) => {
  // ถอดรหัสเคอร์เซอร์
  let startIndex = 0;
  if (request.params?.cursor) {
    startIndex = parseInt(request.params.cursor, 10) || 0;
  }
  
  // ดึงหน้าผลลัพธ์
  const endIndex = Math.min(startIndex + PAGE_SIZE, ALL_TOOLS.length);
  const pageTools = ALL_TOOLS.slice(startIndex, endIndex);
  
  // คำนวณเคอร์เซอร์ถัดไป
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
        // เริ่มต้นชุดข้อมูลขนาดใหญ่
        this.allTools = IntStream.range(0, 100)
            .mapToObj(i -> new Tool("tool_" + i, "Tool number " + i, Map.of()))
            .collect(Collectors.toList());
    }
    
    @McpMethod("tools/list")
    public ListToolsResult listTools(@Param("cursor") String cursor) {
        // ถอดรหัสเคอร์เซอร์
        int startIndex = 0;
        if (cursor != null && !cursor.isEmpty()) {
            try {
                startIndex = Integer.parseInt(cursor);
            } catch (NumberFormatException e) {
                startIndex = 0;
            }
        }
        
        // ดึงหน้าผลลัพธ์
        int endIndex = Math.min(startIndex + PAGE_SIZE, allTools.size());
        List<Tool> pageTools = allTools.subList(startIndex, endIndex);
        
        // คำนวณเคอร์เซอร์ถัดไป
        String nextCursor = endIndex < allTools.size() ? String.valueOf(endIndex) : null;
        
        return new ListToolsResult(pageTools, nextCursor);
    }
}
```

---

## การใช้งานฝั่งไคลเอนต์

### Python Client

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

# การใช้งาน
async with client_session as session:
    tools = await get_all_tools(session)
    print(f"Found {len(tools)} tools")
```

### TypeScript Client

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

// การใช้งาน
const tools = await getAllTools(client);
console.log(`Found ${tools.length} tools`);
```

### รูปแบบการโหลดแบบ Lazy Loading

สำหรับชุดข้อมูลขนาดใหญ่มาก ให้โหลดหน้าเมื่อมีความต้องการ:

```python
class PaginatedToolIterator:
    """Lazily iterate through paginated tools."""
    
    def __init__(self, session: ClientSession):
        self.session = session
        self.cursor = None
        self.buffer = []
        self.exhausted = False
    
    async def __anext__(self):
        # คืนค่าจากบัฟเฟอร์หากมี
        if self.buffer:
            return self.buffer.pop(0)
        
        # ตรวจสอบว่าเราได้ใช้หน้าทั้งหมดหมดแล้วหรือไม่
        if self.exhausted:
            raise StopAsyncIteration
        
        # ดึงหน้าต่อไป
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

# การใช้งาน - มีประสิทธิภาพด้านหน่วยความจำสำหรับชุดข้อมูลขนาดใหญ่
async for tool in PaginatedToolIterator(session):
    process_tool(tool)
```

---

## การแบ่งหน้าสำหรับทรัพยากร

ทรัพยากรมักจะต้องการการแบ่งหน้าสำหรับไดเรกทอรีหรือชุดข้อมูลขนาดใหญ่:

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
    
    # ถอดรหัสเคอร์เซอร์ (ดัชนีไฟล์)
    start_index = int(cursor) if cursor else 0
    page_size = 20
    end_index = min(start_index + page_size, len(all_files))
    
    # สร้างรายการทรัพยากรสำหรับหน้านี้
    resources = []
    for filename in all_files[start_index:end_index]:
        filepath = os.path.join(directory, filename)
        resources.append(Resource(
            uri=f"file://{filepath}",
            name=filename,
            mimeType="application/octet-stream"
        ))
    
    # คำนวณเคอร์เซอร์ถัดไป
    next_cursor = str(end_index) if end_index < len(all_files) else None
    
    return ListResourcesResult(
        resources=resources,
        nextCursor=next_cursor
    )
```

---

## กลยุทธ์การออกแบบเคอร์เซอร์

### กลยุทธ์ที่ 1: อิงดัชนี (ง่าย)

```python
# ตัวชี้ตำแหน่งเป็นแค่ดัชนี
cursor = "50"  # เริ่มที่รายการที่ 50
```

**ข้อดี:** ง่าย ไม่มีสถานะ
**ข้อเสีย:** ผลลัพธ์อาจเปลี่ยนตำแหน่งหากมีการเพิ่ม/ลบรายการ

### กลยุทธ์ที่ 2: อิง ID (เสถียร)

```python
# Cursor คือ ID ล่าสุดที่เห็น
cursor = "item_abc123"  # เริ่มหลังจากรายการนี้
```

**ข้อดี:** เสถียรแม้ว่ารายการจะเปลี่ยนแปลง
**ข้อเสีย:** ต้องการ ID ที่เรียงลำดับ

### กลยุทธ์ที่ 3: สถานะเข้ารหัส (ซับซ้อน)

```python
import base64
import json

def encode_cursor(state: dict) -> str:
    return base64.b64encode(json.dumps(state).encode()).decode()

def decode_cursor(cursor: str) -> dict:
    return json.loads(base64.b64decode(cursor).decode())

# ตัวชี้ตำแหน่งมีหลายฟิลด์สถานะ
cursor = encode_cursor({
    "offset": 50,
    "filter": "active",
    "sort": "name"
})
```

**ข้อดี:** สามารถเข้ารหัสสถานะที่ซับซ้อนได้
**ข้อเสีย:** ซับซ้อนกว่า สตริงเคอร์เซอร์มีขนาดใหญ่ขึ้น

---

## แนวทางปฏิบัติที่ดีที่สุด

### 1. เลือกขนาดหน้าที่เหมาะสม

```python
# พิจารณาขนาดข้อมูล
PAGE_SIZE_SMALL_ITEMS = 100   # เมตาดาตาง่ายๆ
PAGE_SIZE_MEDIUM_ITEMS = 20   # วัตถุที่มีรายละเอียดมากขึ้น
PAGE_SIZE_LARGE_ITEMS = 5     # เนื้อหาที่ซับซ้อน
```

### 2. จัดการเคอร์เซอร์ที่ไม่ถูกต้องอย่างเหมาะสม

```python
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    try:
        start_index = int(cursor) if cursor else 0
        if start_index < 0 or start_index >= len(ALL_TOOLS):
            start_index = 0  # รีเซ็ตไปที่จุดเริ่มต้น
    except (ValueError, TypeError):
        start_index = 0  # ตำแหน่งเคอร์เซอร์ไม่ถูกต้อง เริ่มต้นใหม่
    # ...
```

### 3. รวมจำนวนทั้งหมด (ถ้ามี)

```python
return ListToolsResult(
    tools=page_tools,
    nextCursor=next_cursor,
    # การใช้งานบางส่วนรวมถึงผลรวมสำหรับความคืบหน้าของ UI
    _meta={"total": len(ALL_TOOLS)}
)
```

### 4. ทดสอบกรณีขอบ

```python
async def test_pagination():
    # ชุดผลลัพธ์ว่างเปล่า
    result = await session.list_tools()
    assert result.tools == []
    assert result.nextCursor is None
    
    # หน้าหนึ่งหน้า
    result = await session.list_tools()
    assert len(result.tools) <= PAGE_SIZE
    
    # ตัวชี้ตำแหน่งไม่ถูกต้อง
    result = await session.list_tools(cursor="invalid")
    assert result.tools  # ควรส่งคืนหน้าที่หนึ่ง
```

---

## กับดักทั่วไป

### ❌ การคืนค่าผลลัพธ์ทั้งหมดแล้วแบ่งหน้าที่ฝั่งไคลเอนต์

```python
# แย่: โหลดทุกอย่างเข้าสู่หน่วยความจำ
@app.list_tools()
async def list_tools() -> ListToolsResult:
    all_tools = load_all_tools()  # 1 ล้านเครื่องมือ!
    return ListToolsResult(tools=all_tools)
```

### ✅ การแบ่งหน้าที่แหล่งข้อมูล

```python
# ดี: โหลดเฉพาะสิ่งที่จำเป็นเท่านั้น
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    offset = int(cursor) if cursor else 0
    tools = await db.query_tools(offset=offset, limit=PAGE_SIZE)
    return ListToolsResult(tools=tools, nextCursor=...)
```

---

## ต่อไปคืออะไร

- [โมดูล 5.14 - วิศวกรรมบริบท](../../05-AdvancedTopics/mcp-contextengineering/README.md)
- [โมดูล 8 - แนวทางปฏิบัติที่ดีที่สุด](../../08-BestPractices/README.md)
- [3.8 - การทดสอบเซิร์ฟเวอร์ MCP ของคุณ](../../03-GettingStarted/08-testing/README.md)

---

## แหล่งข้อมูลเพิ่มเติม

- [ข้อกำหนด MCP - การแบ่งหน้า](https://modelcontextprotocol.io/specification/2026-07-28/)
- [อธิบายการแบ่งหน้าด้วยเคอร์เซอร์](https://slack.engineering/evolving-api-pagination-at-slack/)
- [การทดสอบการแบ่งหน้า SDK ของ Python](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->