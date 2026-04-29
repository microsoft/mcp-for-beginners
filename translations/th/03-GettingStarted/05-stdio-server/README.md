# เซิร์ฟเวอร์ MCP กับการขนส่ง stdio

> **⚠️ การอัปเดตสำคัญ**: ตั้งแต่ MCP Specification 2025-06-18 การขนส่ง SSE (Server-Sent Events) แบบแยกเดี่ยว ได้ถูก **เลิกใช้** และแทนที่ด้วยการขนส่ง "Streamable HTTP" ข้อกำหนด MCP ปัจจุบันกำหนดกลไกการขนส่งหลักสองแบบ:
> 1. **stdio** - อินพุต/เอาต์พุตมาตรฐาน (แนะนำสำหรับเซิร์ฟเวอร์ในเครื่อง)
> 2. **Streamable HTTP** - สำหรับเซิร์ฟเวอร์ระยะไกลที่อาจใช้ SSE ภายใน
>
> บทเรียนนี้ได้รับการอัปเดตเพื่อเน้นที่ **การขนส่ง stdio** ซึ่งเป็นวิธีที่แนะนำสำหรับการใช้งานเซิร์ฟเวอร์ MCP ส่วนใหญ่

การขนส่ง stdio ช่วยให้เซิร์ฟเวอร์ MCP สามารถสื่อสารกับไคลเอนต์ผ่านสตรีมอินพุตและเอาต์พุตมาตรฐาน ซึ่งเป็นกลไกการขนส่งที่ใช้บ่อยและแนะนำในข้อกำหนด MCP ปัจจุบัน ให้วิธีที่เรียบง่ายและมีประสิทธิภาพในการสร้างเซิร์ฟเวอร์ MCP ที่สามารถผสานรวมกับแอปพลิเคชันไคลเอนต์ต่าง ๆ ได้อย่างง่ายดาย

## ภาพรวม

บทเรียนนี้ครอบคลุมวิธีการสร้างและใช้งานเซิร์ฟเวอร์ MCP โดยใช้การขนส่ง stdio

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- สร้างเซิร์ฟเวอร์ MCP โดยใช้การขนส่ง stdio
- ดีบักเซิร์ฟเวอร์ MCP โดยใช้ Inspector
- ใช้งานเซิร์ฟเวอร์ MCP โดยใช้ Visual Studio Code
- เข้าใจกลไกการขนส่ง MCP ปัจจุบันและเหตุผลที่แนะนำใช้ stdio


## การขนส่ง stdio - วิธีการทำงาน

การขนส่ง stdio เป็นหนึ่งในสองประเภทการขนส่งที่รองรับในข้อกำหนด MCP ปัจจุบัน (2025-06-18) วิธีการทำงานคือ:

- **การสื่อสารที่เรียบง่าย**: เซิร์ฟเวอร์อ่านข้อความ JSON-RPC จากอินพุตมาตรฐาน (`stdin`) และส่งข้อความไปยังเอาต์พุตมาตรฐาน (`stdout`)
- **ฐานกระบวนการ**: ไคลเอนต์จะเรียกเซิร์ฟเวอร์ MCP เป็นซับโปรเซสส์
- **รูปแบบข้อความ**: ข้อความเป็นคำขอ JSON-RPC แจ้งเตือน หรือการตอบสนองแต่ละรายการ แยกด้วยบรรทัดใหม่
- **การบันทึก**: เซิร์ฟเวอร์สามารถเขียนสตริง UTF-8 ลงในข้อผิดพลาดมาตรฐาน (`stderr`) เพื่อการบันทึก

### ข้อกำหนดสำคัญ:
- ข้อความต้องถูกแยกด้วยบรรทัดใหม่และห้ามมีบรรทัดย่อยภายใน
- เซิร์ฟเวอร์ต้องไม่เขียนอะไรที่ไม่ใช่ข้อความ MCP ที่ถูกต้องลงใน `stdout`
- ไคลเอนต์ต้องไม่เขียนอะไรที่ไม่ใช่ข้อความ MCP ที่ถูกต้องไปยัง `stdin` ของเซิร์ฟเวอร์

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

ในโค้ดข้างต้น:

- เรานำเข้าคลาส `Server` และ `StdioServerTransport` จาก MCP SDK
- สร้างอินสแตนซ์เซิร์ฟเวอร์ด้วยการตั้งค่าพื้นฐานและความสามารถ
- สร้างอินสแตนซ์ `StdioServerTransport` และเชื่อมต่อเซิร์ฟเวอร์กับมัน เพื่อเปิดใช้งานการสื่อสารผ่าน stdin/stdout

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

ในโค้ดข้างต้นเรา:

- สร้างอินสแตนซ์เซิร์ฟเวอร์โดยใช้ MCP SDK
- กำหนดเครื่องมือโดยใช้ decorators
- ใช้ context manager stdio_server เพื่อจัดการการขนส่ง

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

ความแตกต่างหลักจาก SSE คือเซิร์ฟเวอร์ stdio:

- ไม่ต้องตั้งค่าเว็บเซิร์ฟเวอร์หรือ HTTP endpoints
- ถูกเรียกเป็นซับโปรเซสส์โดยไคลเอนต์
- สื่อสารผ่านสตรีม stdin/stdout
- ง่ายต่อการติดตั้งและดีบัก

## แบบฝึกหัด: การสร้างเซิร์ฟเวอร์ stdio

เพื่อสร้างเซิร์ฟเวอร์ของเรา เราต้องคำนึงถึงสองเรื่อง:

- เราต้องใช้เว็บเซิร์ฟเวอร์เพื่อเปิดเผย endpoints สำหรับการเชื่อมต่อและข้อความ
## ห้องปฏิบัติการ: การสร้างเซิร์ฟเวอร์ MCP stdio อย่างง่าย

ในห้องปฏิบัติการนี้ เราจะสร้างเซิร์ฟเวอร์ MCP อย่างง่ายโดยใช้การขนส่ง stdio ที่แนะนำ เซิร์ฟเวอร์นี้จะเปิดเผยเครื่องมือที่ไคลเอนต์สามารถเรียกใช้โดยใช้โปรโตคอล Model Context มาตรฐาน

### ก่อนเริ่ม

- Python 3.8 หรือใหม่กว่า
- MCP Python SDK: `pip install mcp`
- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรมแบบ async

เริ่มต้นโดยสร้างเซิร์ฟเวอร์ MCP stdio ตัวแรกของเรา:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# กำหนดค่าการบันทึกเหตุการณ์
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
    # ใช้การส่งข้อมูล stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ความแตกต่างสำคัญจากวิธี SSE ที่เลิกใช้

**การขนส่ง Stdio (มาตรฐานปัจจุบัน):**
- โมเดลซับโปรเซสง่าย ๆ - ไคลเอนต์เรียกใช้เซิร์ฟเวอร์เป็น child process
- การสื่อสารผ่าน stdin/stdout ด้วยข้อความ JSON-RPC
- ไม่ต้องตั้งค่า HTTP server
- ประสิทธิภาพและความปลอดภัยดีกว่า
- ง่ายต่อการดีบักและพัฒนา

**การขนส่ง SSE (เลิกใช้ตั้งแต่ MCP 2025-06-18):**
- ต้องใช้ HTTP server ที่มี SSE endpoints
- ตั้งค่าซับซ้อนกว่าและมีโครงสร้างเว็บเซิร์ฟเวอร์
- มีข้อควรพิจารณาด้านความปลอดภัยเพิ่มเติมสำหรับ HTTP endpoints
- ถูกแทนที่ด้วย Streamable HTTP สำหรับสถานการณ์เว็บ

### การสร้างเซิร์ฟเวอร์ด้วยการขนส่ง stdio

เพื่อสร้างเซิร์ฟเวอร์ stdio ของเรา เราต้อง:

1. **นำเข้าห้องสมุดที่จำเป็น** - ต้องใช้ส่วนประกอบเซิร์ฟเวอร์ MCP และการขนส่ง stdio
2. **สร้างอินสแตนซ์เซิร์ฟเวอร์** - กำหนดเซิร์ฟเวอร์พร้อมความสามารถ
3. **กำหนดเครื่องมือ** - เพิ่มฟังก์ชันที่ต้องการเปิดเผย
4. **ตั้งค่าการขนส่ง** - กำหนดค่าการสื่อสาร stdio
5. **รันเซิร์ฟเวอร์** - เริ่มเซิร์ฟเวอร์และจัดการข้อความ

เรามาสร้างทีละขั้นตอน:

### ขั้นตอนที่ 1: สร้างเซิร์ฟเวอร์ stdio พื้นฐาน

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# กำหนดค่า logging
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

### ขั้นตอนที่ 2: เพิ่มเครื่องมือเพิ่มเติม

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

### ขั้นตอนที่ 3: การรันเซิร์ฟเวอร์

บันทึกโค้ดเป็น `server.py` และรันจากบรรทัดคำสั่ง:

```bash
python server.py
```

เซิร์ฟเวอร์จะเริ่มและรอรับค่าอินพุตจาก stdin มันสื่อสารโดยใช้ข้อความ JSON-RPC ผ่านการขนส่ง stdio

### ขั้นตอนที่ 4: ทดสอบด้วยตัวตรวจสอบ Inspector

คุณสามารถทดสอบเซิร์ฟเวอร์ของคุณโดยใช้ MCP Inspector:

1. ติดตั้ง Inspector: `npx @modelcontextprotocol/inspector`
2. รัน Inspector แล้วชี้ไปที่เซิร์ฟเวอร์ของคุณ
3. ทดสอบเครื่องมือที่คุณสร้าง

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## การดีบักเซิร์ฟเวอร์ stdio ของคุณ

### การใช้ MCP Inspector

MCP Inspector เป็นเครื่องมือที่มีประโยชน์สำหรับการดีบักและทดสอบเซิร์ฟเวอร์ MCP นี่คือวิธีใช้กับเซิร์ฟเวอร์ stdio ของคุณ:

1. **ติดตั้ง Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **รัน Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **ทดสอบเซิร์ฟเวอร์ของคุณ**: Inspector มีเว็บอินเทอร์เฟซที่คุณสามารถ:
   - ดูความสามารถของเซิร์ฟเวอร์
   - ทดสอบเครื่องมือด้วยพารามิเตอร์ต่าง ๆ
   - ตรวจสอบข้อความ JSON-RPC
   - ดีบักปัญหาการเชื่อมต่อ

### การใช้ VS Code

คุณยังสามารถดีบักเซิร์ฟเวอร์ MCP ของคุณโดยตรงใน VS Code ได้:

1. สร้างการกำหนดค่า launch ใน `.vscode/launch.json`:
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

2. ตั้ง breakpoints ในโค้ดเซิร์ฟเวอร์ของคุณ
3. รันดีบักเกอร์และทดสอบด้วย Inspector

### เคล็ดลับการดีบักทั่วไป

- ใช้ `stderr` สำหรับการบันทึก – อย่าเขียนลง `stdout` เพราะสงวนไว้สำหรับข้อความ MCP
- ตรวจสอบให้แน่ใจว่าข้อความ JSON-RPC ทั้งหมดถูกแยกด้วยบรรทัดใหม่
- ทดสอบด้วยเครื่องมือที่ง่ายก่อนเพิ่มฟังก์ชันซับซ้อน
- ใช้ Inspector เพื่อตรวจสอบรูปแบบข้อความ

## การใช้งานเซิร์ฟเวอร์ stdio ของคุณใน VS Code

เมื่อคุณสร้างเซิร์ฟเวอร์ MCP stdio แล้ว คุณสามารถผสานรวมกับ VS Code เพื่อใช้งานร่วมกับ Claude หรือไคลเอนต์ MCP อื่น ๆ ได้

### การกำหนดค่า

1. **สร้างไฟล์กำหนดค่า MCP** ที่ `%APPDATA%\Claude\claude_desktop_config.json` (Windows) หรือ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **รีสตาร์ท Claude**: ปิดและเปิด Claude ใหม่เพื่อโหลดการกำหนดค่าเซิร์ฟเวอร์ใหม่

3. **ทดสอบการเชื่อมต่อ**: เริ่มการสนทนากับ Claude และลองใช้เครื่องมือในเซิร์ฟเวอร์ของคุณ:
   - "ช่วยทักทายฉันโดยใช้เครื่องมือทักทายได้ไหม?"
   - "คำนวณผลรวมของ 15 กับ 27"
   - "ข้อมูลเซิร์ฟเวอร์คืออะไร?"

### ตัวอย่างเซิร์ฟเวอร์ stdio ใน TypeScript

นี่คือตัวอย่าง TypeScript อย่างสมบูรณ์สำหรับอ้างอิง:

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

### ตัวอย่างเซิร์ฟเวอร์ stdio ใน .NET

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

- สร้างเซิร์ฟเวอร์ MCP โดยใช้ **การขนส่ง stdio** ปัจจุบัน (วิธีที่แนะนำ)
- เข้าใจเหตุผลว่าทำไมการขนส่ง SSE ถูกเลิกใช้และเปลี่ยนไปใช้ stdio กับ Streamable HTTP
- สร้างเครื่องมือที่สามารถเรียกโดยไคลเอนต์ MCP
- ดีบักเซิร์ฟเวอร์โดยใช้ MCP Inspector
- ผสานเซิร์ฟเวอร์ stdio เข้ากับ VS Code และ Claude

การขนส่ง stdio ให้วิธีที่เรียบง่าย ปลอดภัย และมีประสิทธิภาพมากขึ้นในการสร้างเซิร์ฟเวอร์ MCP เมื่อเทียบกับวิธี SSE ที่เลิกใช้แล้ว เป็นวิธีที่แนะนำสำหรับเซิร์ฟเวอร์ MCP ส่วนใหญ่ตามข้อกำหนด 2025-06-18


### .NET

1. มาสร้างเครื่องมือกันก่อน สำหรับสิ่งนี้เราจะสร้างไฟล์ *Tools.cs* โดยมีเนื้อหาดังนี้:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## แบบฝึกหัด: การทดสอบเซิร์ฟเวอร์ stdio ของคุณ

เมื่อคุณสร้างเซิร์ฟเวอร์ stdio แล้ว ลองทดสอบเพื่อให้แน่ใจว่าทำงานได้ถูกต้อง

### ก่อนเริ่ม

1. ตรวจสอบว่าคุณติดตั้ง MCP Inspector แล้ว:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. โค้ดเซิร์ฟเวอร์ของคุณควรถูกบันทึกไว้ (เช่น `server.py`)

### การทดสอบด้วย Inspector

1. **เริ่ม Inspector กับเซิร์ฟเวอร์ของคุณ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **เปิดเว็บอินเทอร์เฟซ**: Inspector จะเปิดหน้าต่างเบราว์เซอร์ที่แสดงความสามารถของเซิร์ฟเวอร์คุณ

3. **ทดสอบเครื่องมือ**: 
   - ลองใช้เครื่องมือ `get_greeting` กับชื่อที่ต่างกัน
   - ทดสอบเครื่องมือ `calculate_sum` กับตัวเลขหลากหลาย
   - เรียกใช้เครื่องมือ `get_server_info` เพื่อดูข้อมูลเมตาเซิร์ฟเวอร์

4. **ติดตามการสื่อสาร**: Inspector จะแสดงข้อความ JSON-RPC ที่แลกเปลี่ยนระหว่างไคลเอนต์และเซิร์ฟเวอร์

### สิ่งที่คุณควรเห็น

เมื่อเซิร์ฟเวอร์เริ่มทำงานถูกต้อง คุณควรเห็น:
- ความสามารถของเซิร์ฟเวอร์แสดงใน Inspector
- เครื่องมือพร้อมให้ทดสอบ
- แลกเปลี่ยนข้อความ JSON-RPC สำเร็จ
- การตอบสนองเครื่องมือแสดงในอินเทอร์เฟซ

### ปัญหาทั่วไปและวิธีแก้ไข

**เซิร์ฟเวอร์ไม่เริ่มทำงาน:**
- ตรวจสอบว่าติดตั้ง dependencies ทั้งหมดแล้ว: `pip install mcp`
- ตรวจสอบไวยากรณ์และการเยื้องใน Python
- มองหาข้อความแสดงข้อผิดพลาดในคอนโซล

**เครื่องมือไม่แสดง:**
- ตรวจสอบว่ามี decorator `@server.tool()` อยู่
- ตรวจสอบว่าได้กำหนดฟังก์ชันเครื่องมือก่อน `main()`
- ยืนยันว่าเซิร์ฟเวอร์ถูกตั้งค่าอย่างถูกต้อง

**ปัญหาการเชื่อมต่อ:**
- ตรวจสอบว่าเซิร์ฟเวอร์ใช้การขนส่ง stdio ถูกต้อง
- ตรวจสอบว่าไม่มีโปรเซสอื่นมาขัดจังหวะ
- ตรวจสอบไวยากรณ์คำสั่ง Inspector

## การบ้าน

ลองสร้างเซิร์ฟเวอร์ของคุณด้วยความสามารถเพิ่มเติม ดู [หน้านี้](https://api.chucknorris.io/) ตัวอย่างเช่น เพิ่มเครื่องมือที่เรียก API ได้ คุณกำหนดเองว่าเซิร์ฟเวอร์ควรเป็นอย่างไร ขอให้สนุก :)

## แนวทางแก้ไข

[แนวทางแก้ไข](./solution/README.md) นี่เป็นแนวทางแก้ไขที่เป็นไปได้พร้อมโค้ดทำงาน

## ประเด็นสำคัญ

ประเด็นสำคัญจากบทนี้คือ:

- การขนส่ง stdio เป็นกลไกที่แนะนำสำหรับเซิร์ฟเวอร์ MCP ในเครื่อง
- การขนส่ง stdio ช่วยให้การสื่อสารระหว่างเซิร์ฟเวอร์และไคลเอนต์ MCP ด้วยสตรีมอินพุตและเอาต์พุตมาตรฐานไร้รอยต่อ
- คุณสามารถใช้ทั้ง Inspector และ Visual Studio Code เพื่อใช้งานเซิร์ฟเวอร์ stdio ได้โดยตรง ทำให้การดีบักและผสานรวมง่ายขึ้น

## ตัวอย่าง 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## แหล่งข้อมูลเพิ่มเติม

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ต่อไป

## ขั้นตอนถัดไป

เมื่อคุณเรียนรู้วิธีสร้างเซิร์ฟเวอร์ MCP ด้วยการขนส่ง stdio แล้ว คุณสามารถสำรวจหัวข้อขั้นสูงเพิ่มเติม:

- **ถัดไป**: [HTTP Streaming กับ MCP (Streamable HTTP)](../06-http-streaming/README.md) - เรียนรู้เกี่ยวกับกลไกการขนส่งอีกแบบที่รองรับสำหรับเซิร์ฟเวอร์ระยะไกล
- **ขั้นสูง**: [แนวทางปฏิบัติที่ดีที่สุดสำหรับความปลอดภัย MCP](../../02-Security/README.md) - นำความปลอดภัยไปใช้ในเซิร์ฟเวอร์ MCP ของคุณ
- **ระดับผลิตจริง**: [กลยุทธ์การดีพลอย](../09-deployment/README.md) - นำเซิร์ฟเวอร์ของคุณไปใช้ในสภาพแวดล้อมผลิตจริง

## แหล่งข้อมูลเพิ่มเติม

- [ข้อกำหนด MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - ข้อกำหนดอย่างเป็นทางการ
- [เอกสาร MCP SDK](https://github.com/modelcontextprotocol/sdk) - เอกสาร SDK สำหรับทุกภาษา
- [ตัวอย่างจากชุมชน](../../06-CommunityContributions/README.md) - ตัวอย่างเซิร์ฟเวอร์เพิ่มเติมจากชุมชน

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมืออาชีพที่เป็นมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->