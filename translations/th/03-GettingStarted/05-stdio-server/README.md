# MCP Server with stdio Transport

> **⚠️ อัปเดตสำคัญ**: ตั้งแต่ MCP Specification 2025-06-18 เป็นต้นไป การขนส่ง SSE (Server-Sent Events) แบบ standalone ได้ถูก **เลิกใช้** และถูกแทนที่ด้วยการขนส่ง "Streamable HTTP" สเปค MCP ปัจจุบันกำหนดกลไกการขนส่งหลัก 2 แบบ:
> 1. **stdio** - การส่งข้อมูลผ่านมาตรฐานอินพุต/เอาต์พุต (แนะนำสำหรับเซิร์ฟเวอร์ภายในเครื่อง)
> 2. **Streamable HTTP** - สำหรับเซิร์ฟเวอร์ที่อยู่ระยะไกลซึ่งอาจใช้ SSE ภายใน
>
> บทเรียนนี้ได้รับการอัปเดตเพื่อเน้นไปที่ **stdio transport** ซึ่งเป็นวิธีที่แนะนำสำหรับการใช้งาน MCP server ส่วนใหญ่

การขนส่ง stdio อนุญาตให้ MCP เซิร์ฟเวอร์สื่อสารกับไคลเอนต์ผ่านสตรีมมาตรฐานอินพุตและเอาต์พุต ซึ่งเป็นกลไกการขนส่งที่ใช้บ่อยที่สุดและแนะนำในสเปค MCP ปัจจุบัน มอบวิธีง่ายและมีประสิทธิภาพสำหรับการสร้าง MCP เซิร์ฟเวอร์ที่สามารถรวมกับแอปพลิเคชันไคลเอนต์ต่าง ๆ ได้ง่าย

## ภาพรวม

บทเรียนนี้ครอบคลุมวิธีการสร้างและใช้งาน MCP Servers โดยใช้ stdio transport

## วัตถุประสงค์การเรียนรู้

หลังจากจบบทเรียนนี้คุณจะสามารถ:

- สร้าง MCP Server โดยใช้ stdio transport
- ดีบัก MCP Server โดยใช้ Inspector
- ใช้งาน MCP Server โดยใช้ Visual Studio Code
- เข้าใจกลไกการขนส่ง MCP ปัจจุบันและเหตุผลที่แนะนำ stdio

## stdio Transport - วิธีการทำงาน

stdio transport เป็นหนึ่งในสองประเภทขนส่งที่รองรับในสเปค MCP ปัจจุบัน (2025-06-18) วิธีการทำงานคือ:

- **การสื่อสารแบบเรียบง่าย**: เซิร์ฟเวอร์อ่านข้อความ JSON-RPC จากมาตรฐานอินพุต (`stdin`) และส่งข้อความผ่านมาตรฐานเอาต์พุต (`stdout`)
- **กระบวนการแบบ subprocess**: ไคลเอนต์จะเรียกใช้ MCP server เป็น subprocess
- **รูปแบบข้อความ**: ข้อความเป็นคำร้องขอ JSON-RPC, การแจ้งเตือน หรือการตอบกลับแต่ละรายการ แยกด้วยบรรทัดใหม่
- **การบันทึก**: เซิร์ฟเวอร์สามารถเขียนข้อความ UTF-8 ไปยังมาตรฐานข้อผิดพลาด (`stderr`) เพื่อวัตถุประสงค์ในการบันทึก

### ข้อกำหนดสำคัญ:
- ข้อความต้องถูกแยกด้วยบรรทัดใหม่และต้องไม่มีบรรทัดใหม่ฝังอยู่ในข้อความ
- เซิร์ฟเวอร์ต้องไม่เขียนข้อมูลใดที่ไม่ใช่ข้อความ MCP ที่ถูกต้องไปยัง `stdout`
- ไคลเอนต์ต้องไม่เขียนข้อมูลใดที่ไม่ใช่ข้อความ MCP ที่ถูกต้องไปยัง `stdin` ของเซิร์ฟเวอร์

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

ในโค้ดก่อนหน้า:

- เรานำเข้า `Server` คลาสและ `StdioServerTransport` จาก MCP SDK
- เราสร้างอินสแตนซ์เซิร์ฟเวอร์โดยมีการกำหนดค่าพื้นฐานและความสามารถ

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# สร้างอินสแตนซ์เซิร์ฟเวอร์
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

ในโค้ดก่อนหน้าเรา:

- สร้างอินสแตนซ์เซิร์ฟเวอร์โดยใช้ MCP SDK
- กำหนดเครื่องมือโดยใช้ decorators
- ใช้บริบทผู้จัดการ stdio_server เพื่อจัดการขนส่ง

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

ความแตกต่างหลักจาก SSE คือ stdio servers:

- ไม่ต้องติดตั้งเว็บเซิร์ฟเวอร์หรือสร้าง HTTP endpoints
- ถูกเรียกใช้เป็น subprocess โดยไคลเอนต์
- สื่อสารผ่านสตรีม stdin/stdout
- ง่ายต่อการใช้งานและดีบัก

## แบบฝึกหัด: สร้าง stdio Server

เพื่อสร้างเซิร์ฟเวอร์ของเรา เราต้องจำสองอย่างนี้:

- เราต้องใช้เว็บเซิร์ฟเวอร์เพื่อเปิดเผย endpoints สำหรับการเชื่อมต่อและข้อความ
## ห้องปฏิบัติการ: สร้าง MCP stdio server อย่างง่าย

ในห้องปฏิบัติการนี้ เราจะสร้าง MCP server อย่างง่ายโดยใช้ stdio transport ที่แนะนำ เซิร์ฟเวอร์นี้จะเปิดเผยเครื่องมือที่ไคลเอนต์สามารถเรียกใช้โดยใช้ Model Context Protocol มาตรฐาน

### ข้อกำหนดเบื้องต้น

- Python 3.8 หรือสูงกว่า
- MCP Python SDK: `pip install mcp`
- พื้นฐานการเขียนโปรแกรมแบบ async

เริ่มต้นโดยสร้าง MCP stdio server ตัวแรกของเรา:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# กำหนดค่าการบันทึก
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# สร้างเซิร์ฟเวอร์
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
    # ใช้การส่งผ่าน stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ความแตกต่างสำคัญจากวิธีการ SSE ที่เลิกใช้แล้ว

**Stdio Transport (มาตรฐานปัจจุบัน):**
- โมเดล subprocess ง่าย ๆ - ไคลเอนต์เรียกเซิร์ฟเวอร์เป็น child process
- สื่อสารผ่าน stdin/stdout โดยใช้ข้อความ JSON-RPC
- ไม่ต้องตั้งค่า HTTP server
- ประสิทธิภาพและความปลอดภัยดีกว่า
- ง่ายต่อการดีบักและพัฒนา

**SSE Transport (เลิกใช้ตั้งแต่ MCP 2025-06-18):**
- ต้องมี HTTP server พร้อม SSE endpoints
- ตั้งค่าซับซ้อนมากกว่าด้วยโครงสร้างพื้นฐานเว็บเซิร์ฟเวอร์
- ต้องพิจารณาความปลอดภัยเพิ่มเติมสำหรับ HTTP endpoints
- ตอนนี้ถูกแทนที่ด้วย Streamable HTTP สำหรับสถานการณ์เว็บ

### การสร้างเซิร์ฟเวอร์โดยใช้ stdio transport

เพื่อสร้าง stdio server ของเรา เราต้อง:

1. **นำเข้าไลบรารีที่จำเป็น** - ต้องใช้องค์ประกอบเซิร์ฟเวอร์ MCP และ stdio transport
2. **สร้างอินสแตนซ์เซิร์ฟเวอร์** - กำหนดเซิร์ฟเวอร์พร้อมความสามารถของมัน
3. **กำหนดเครื่องมือ** - เพิ่มฟังก์ชันที่ต้องการเปิดเผย
4. **ตั้งค่าการขนส่ง** - กำหนดค่า stdio การสื่อสาร
5. **รันเซิร์ฟเวอร์** - เริ่มเซิร์ฟเวอร์และจัดการข้อความ

สร้างด้วยกันทีละขั้นตอน:

### ขั้นตอนที่ 1: สร้าง stdio server เบื้องต้น

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# กำหนดการบันทึกไฟล์ล็อก
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# สร้างเซิร์ฟเวอร์
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

### ขั้นตอนที่ 2: เพิ่มเครื่องมือมากขึ้น

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

### ขั้นตอนที่ 3: รันเซิร์ฟเวอร์

บันทึกโค้ดเป็น `server.py` และรันจากบรรทัดคำสั่ง:

```bash
python server.py
```

เซิร์ฟเวอร์จะเริ่มและรอรับข้อมูลจาก stdin โดยสื่อสารผ่านข้อความ JSON-RPC บน stdio transport

### ขั้นตอนที่ 4: ทดสอบกับ Inspector

คุณสามารถทดสอบเซิร์ฟเวอร์ของคุณโดยใช้ MCP Inspector:

1. ติดตั้ง Inspector: `npx @modelcontextprotocol/inspector`
2. รัน Inspector และชี้ไปที่เซิร์ฟเวอร์ของคุณ
3. ทดสอบเครื่องมือที่คุณสร้าง

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## การดีบัก stdio server ของคุณ

### การใช้ MCP Inspector

MCP Inspector เป็นเครื่องมือที่มีคุณค่าสำหรับการดีบักและทดสอบ MCP servers นี่คือวิธีใช้กับ stdio server ของคุณ:

1. **ติดตั้ง Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **รัน Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **ทดสอบเซิร์ฟเวอร์ของคุณ**: Inspector มีอินเทอร์เฟซเว็บที่คุณสามารถ:
   - ดูความสามารถของเซิร์ฟเวอร์
   - ทดสอบเครื่องมือด้วยพารามิเตอร์ต่าง ๆ
   - ติดตามข้อความ JSON-RPC
   - ดีบักปัญหาการเชื่อมต่อ

### การใช้ VS Code

คุณสามารถดีบัก MCP server โดยตรงใน VS Code ได้ด้วย:

1. สร้างการตั้งค่า launch ใน `.vscode/launch.json`:
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

2. ตั้ง breakpoint ในโค้ดเซิร์ฟเวอร์ของคุณ
3. รันดีบักเกอร์และทดสอบกับ Inspector

### เคล็ดลับการดีบักทั่วไป

- ใช้ `stderr` สำหรับบันทึก - อย่าเขียนอะไรไปยัง `stdout` เพราะจองไว้สำหรับข้อความ MCP
- ตรวจสอบให้แน่ใจว่าข้อความ JSON-RPC ทั้งหมดถูกแยกด้วยบรรทัดใหม่
- ทดสอบกับเครื่องมือเรียบง่ายก่อนเพิ่มฟังก์ชันซับซ้อน
- ใช้ Inspector เพื่อตรวจสอบรูปแบบข้อความ

## การใช้งาน stdio server ใน VS Code

เมื่อคุณสร้าง MCP stdio server แล้ว คุณสามารถรวมมันกับ VS Code เพื่อใช้งานร่วมกับ Claude หรือไคลเอนต์ MCP อื่น ๆ ได้

### การตั้งค่า

1. **สร้างไฟล์การตั้งค่า MCP** ที่ `%APPDATA%\Claude\claude_desktop_config.json` (Windows) หรือ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **รีสตาร์ท Claude**: ปิดและเปิดใหม่เพื่อโหลดการตั้งค่าเซิร์ฟเวอร์ใหม่

3. **ทดสอบการเชื่อมต่อ**: เริ่มสนทนากับ Claude และลองใช้เครื่องมือของเซิร์ฟเวอร์คุณ:
   - "ช่วยทักทายฉันด้วยเครื่องมือทักทายได้ไหม?"
   - "คำนวณผลบวกของ 15 และ 27"
   - "ข้อมูลเซิร์ฟเวอร์คืออะไร?"

### ตัวอย่าง TypeScript stdio server

นี่คือตัวอย่าง TypeScript สมบูรณ์เพื่อเป็นข้อมูลอ้างอิง:

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

// เพิ่มเครื่องมือ
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

### ตัวอย่าง .NET stdio server

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## สรุป

ในบทเรียนที่อัปเดตนี้ คุณได้เรียนรู้วิธี:

- สร้าง MCP servers โดยใช้ **stdio transport** ปัจจุบัน (วิธีที่แนะนำ)
- เข้าใจเหตุผลที่เลิกใช้ SSE และเปลี่ยนมาใช้ stdio และ Streamable HTTP
- สร้างเครื่องมือที่ไคลเอนต์ MCP สามารถเรียกใช้ได้
- ดีบักเซิร์ฟเวอร์ของคุณโดยใช้ MCP Inspector
- รวม stdio server กับ VS Code และ Claude

stdio transport ให้วิธีการสร้าง MCP servers ที่ง่ายขึ้น ปลอดภัยขึ้น และมีประสิทธิภาพมากขึ้นเมื่อเทียบกับวิธีการ SSE ที่เลิกใช้แล้ว เป็นวิธีการขนส่งที่แนะนำสำหรับการใช้งาน MCP server ส่วนใหญ่ ณ สเปค 2025-06-18


### .NET

1. เรามาสร้างเครื่องมือกันก่อน สำหรับนี้เราจะสร้างไฟล์ *Tools.cs* ที่มีเนื้อหาดังนี้:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## แบบฝึกหัด: ทดสอบ stdio server ของคุณ

ตอนนี้ที่คุณสร้าง stdio server แล้ว ลองทดสอบดูว่าใช้งานได้ถูกต้องไหม

### ข้อกำหนดเบื้องต้น

1. ตรวจสอบว่าคุณติดตั้ง MCP Inspector แล้ว:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. โค้ดเซิร์ฟเวอร์ของคุณควรถูกบันทึกไว้แล้ว (เช่น `server.py`)

### การทดสอบกับ Inspector

1. **เริ่ม Inspector พร้อมเซิร์ฟเวอร์ของคุณ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **เปิดอินเทอร์เฟซเว็บ**: Inspector จะเปิดหน้าต่างเบราว์เซอร์แสดงความสามารถของเซิร์ฟเวอร์คุณ

3. **ทดสอบเครื่องมือ**: 
   - ลองใช้เครื่องมือ `get_greeting` กับชื่อที่ต่างกัน
   - ทดสอบ `calculate_sum` ด้วยตัวเลขต่าง ๆ
   - เรียกใช้ `get_server_info` เพื่อดูเมตาดาต้าเซิร์ฟเวอร์

4. **ติดตามการสื่อสาร**: Inspector แสดงข้อความ JSON-RPC ที่แลกเปลี่ยนกันระหว่างไคลเอนต์และเซิร์ฟเวอร์

### สิ่งที่ควรเห็น

เมื่อเซิร์ฟเวอร์เริ่มต้นถูกต้อง คุณควรเห็น:
- รายการความสามารถของเซิร์ฟเวอร์ใน Inspector
- เครื่องมือพร้อมใช้งานสำหรับการทดสอบ
- การแลกเปลี่ยนข้อความ JSON-RPC สำเร็จ
- การตอบกลับของเครื่องมือแสดงในอินเทอร์เฟซ

### ปัญหาทั่วไปและวิธีแก้ไข

**เซิร์ฟเวอร์ไม่เริ่ม:**
- ตรวจสอบว่าติดตั้ง dependencies ครบ: `pip install mcp`
- ตรวจสอบไวยากรณ์ Python และการเยื้องบรรทัด
- ดูข้อความผิดพลาดในคอนโซล

**เครื่องมือไม่แสดง:**
- ตรวจสอบว่ามี decorators `@server.tool()` อยู่
- ตรวจสอบว่าเครื่องมือถูกประกาศก่อนฟังก์ชัน `main()`
- ตรวจสอบว่าเซิร์ฟเวอร์ตั้งค่าอย่างถูกต้อง

**ปัญหาการเชื่อมต่อ:**
- ตรวจสอบให้แน่ใจว่าเซิร์ฟเวอร์ใช้ stdio transport ถูกต้อง
- ตรวจสอบไม่มีโปรเซสอื่นรบกวน
- ตรวจสอบไวยากรณ์คำสั่ง Inspector

## การบ้าน

ลองขยายเซิร์ฟเวอร์ของคุณด้วยความสามารถมากขึ้น ดูที่ [หน้านี้](https://api.chucknorris.io/) เพื่อเพิ่มเครื่องมือเรียก API ตัวอย่าง คุณตัดสินใจได้ว่าเซิร์ฟเวอร์จะเป็นอย่างไร สนุกกับการทำ :)

## ตัวอย่างคำตอบ

[Solution](./solution/README.md) นี่คือตัวอย่างคำตอบพร้อมโค้ดที่ใช้งานได้

## ข้อคิดสำคัญ

ข้อคิดสำคัญจากบทนี้ได้แก่:

- stdio transport เป็นกลไกที่แนะนำสำหรับเซิร์ฟเวอร์ MCP ภายในเครื่อง
- stdio transport อนุญาตการสื่อสารระหว่าง MCP servers และ clients อย่างราบรื่นผ่านสตรีมอินพุตและเอาต์พุตมาตรฐาน
- คุณสามารถใช้ทั้ง Inspector และ Visual Studio Code ในการใช้งาน stdio servers โดยตรง ทำให้การดีบักและการรวมระบบง่ายขึ้น

## ตัวอย่าง

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## แหล่งข้อมูลเพิ่มเติม

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ต่อไปคืออะไร

## ก้าวต่อไป

ตอนนี้คุณได้เรียนรู้วิธีสร้าง MCP servers ด้วย stdio transport แล้ว คุณสามารถสำรวจหัวข้อขั้นสูงเพิ่มเติมได้:

- **ถัดไป**: [HTTP Streaming กับ MCP (Streamable HTTP)](../06-http-streaming/README.md) - เรียนรู้เกี่ยวกับกลไกขนส่งที่รองรับอีกแบบสำหรับเซิร์ฟเวอร์ระยะไกล
- **ขั้นสูง**: [แนวทางการรักษาความปลอดภัย MCP](../../02-Security/README.md) - การนำความปลอดภัยมาใช้ใน MCP servers ของคุณ
- **ใช้งานจริง**: [กลยุทธ์การปรับใช้](../09-deployment/README.md) - การปรับใช้เซิร์ฟเวอร์สำหรับการใช้งานจริง

## แหล่งข้อมูลเพิ่มเติม

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - สเปคอย่างเป็นทางการ
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - เอกสาร SDK สำหรับทุกภาษา
- [ตัวอย่างจากชุมชน](../../06-CommunityContributions/README.md) - ตัวอย่างเซิร์ฟเวอร์เพิ่มเติมจากชุมชน

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้บริการแปลโดยมืออาชีพที่เป็นมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->