# เซิร์ฟเวอร์ MCP กับการขนส่ง stdio

> **⚠️ อัปเดตสำคัญ**: ตั้งแต่ข้อกำหนด MCP วันที่ 2025-06-18 การขนส่ง SSE แบบสแตนด์อโลน (Server-Sent Events) ได้ถูก **เลิกใช้** และถูกแทนที่ด้วยการขนส่ง "Streamable HTTP" ข้อกำหนด MCP ปัจจุบันกำหนดกลไกการขนส่งหลักสองแบบ:
> 1. **stdio** - อินพุต/เอาต์พุตมาตรฐาน (แนะนำสำหรับเซิร์ฟเวอร์ในเครื่อง)
> 2. **Streamable HTTP** - สำหรับเซิร์ฟเวอร์ระยะไกลที่อาจใช้ SSE ภายใน
>
> บทเรียนนี้ได้รับการอัปเดตเพื่อเน้นที่ **การขนส่ง stdio** ซึ่งเป็นวิธีที่แนะนำสำหรับการใช้งานเซิร์ฟเวอร์ MCP ส่วนใหญ่

การขนส่ง stdio ช่วยให้เซิร์ฟเวอร์ MCP สื่อสารกับไคลเอนต์ผ่านทางสตรีมอินพุตและเอาต์พุตมาตรฐาน นี่คือกลไกการขนส่งที่ใช้งานบ่อยที่สุดและแนะนำในข้อกำหนด MCP ปัจจุบัน โดยให้วิธีที่ง่ายและมีประสิทธิภาพในการสร้างเซิร์ฟเวอร์ MCP ที่สามารถรวมเข้ากับแอปพลิเคชันไคลเอนต์หลากหลายได้อย่างง่ายดาย

## ภาพรวม

บทเรียนนี้ครอบคลุมวิธีการสร้างและใช้งานเซิร์ฟเวอร์ MCP โดยใช้การขนส่ง stdio

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- สร้างเซิร์ฟเวอร์ MCP โดยใช้การขนส่ง stdio
- ดีบักเซิร์ฟเวอร์ MCP โดยใช้ Inspector
- ใช้งานเซิร์ฟเวอร์ MCP ผ่าน Visual Studio Code
- เข้าใจกลไกการขนส่ง MCP ปัจจุบันและเหตุผลว่าทำไม stdio ถึงได้รับการแนะนำ


## การขนส่ง stdio - วิธีการทำงาน

การขนส่ง stdio เป็นหนึ่งในสองกลไกการขนส่งมาตรฐานในข้อกำหนด MCP
`2026-07-28` นี่คือวิธีการทำงาน:

- **การสื่อสารที่เรียบง่าย**: เซิร์ฟเวอร์อ่านข้อความ JSON-RPC จากอินพุตมาตรฐาน (`stdin`) และส่งข้อความไปยังเอาต์พุตมาตรฐาน (`stdout`)
- **กระบวนการ**: ไคลเอนต์เปิดเซิร์ฟเวอร์ MCP เป็นกระบวนการย่อย
- **รูปแบบข้อความ**: ข้อความเป็นคำขอ แจ้งเตือน หรือการตอบสนองแบบ JSON-RPC ทีละข้อความ โดยแยกด้วยบรรทัดใหม่
- **การบันทึก**: เซิร์ฟเวอร์สามารถเขียนสตริง UTF-8 ลงในข้อผิดพลาดมาตรฐาน (`stderr`) เพื่อบันทึกได้

### ข้อกำหนดหลัก:
- ข้อความต้องถูกแยกด้วยบรรทัดใหม่ และห้ามมีบรรทัดใหม่ฝังอยู่ในข้อความ
- เซิร์ฟเวอร์ห้ามเขียนอะไรลง `stdout` ที่ไม่ใช่ข้อความ MCP ที่ถูกต้อง
- ไคลเอนต์ห้ามเขียนอะไรลง `stdin` ของเซิร์ฟเวอร์ที่ไม่ใช่ข้อความ MCP ที่ถูกต้อง

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

ในโค้ดก่อนหน้านี้:

- เรานำเข้า `Server` class และ `StdioServerTransport` จาก MCP SDK
- สร้างอินสแตนซ์เซิร์ฟเวอร์ด้วยการกำหนดค่าพื้นฐานและความสามารถ
- สร้างอินสแตนซ์ `StdioServerTransport` และเชื่อมต่อเซิร์ฟเวอร์กับมัน ทำให้สื่อสารผ่าน stdin/stdout ได้

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

ในโค้ดก่อนหน้านี้เราทำ:

- สร้างอินสแตนซ์เซิร์ฟเวอร์โดยใช้ MCP SDK
- กำหนดเครื่องมือโดยใช้ตัวตกแต่ง (decorators)
- ใช้ตัวจัดการบริบท stdio_server เพื่อจัดการการขนส่ง

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

ความแตกต่างที่สำคัญจาก SSE คือเซิร์ฟเวอร์ stdio:

- ไม่ต้องตั้งค่าเว็บเซิร์ฟเวอร์หรือจุดปลาย HTTP
- ถูกเปิดเป็นกระบวนการย่อยโดยไคลเอนต์
- สื่อสารผ่านสตรีม stdin/stdout
- ง่ายต่อการติดตั้งและดีบัก

## แบบฝึกหัด: การสร้างเซิร์ฟเวอร์ stdio

เพื่อสร้างเซิร์ฟเวอร์ของเรา เราต้องระลึกถึงสองสิ่ง:

- เราต้องใช้เว็บเซิร์ฟเวอร์เพื่อเปิดเผยจุดปลายสำหรับการเชื่อมต่อและข้อความ
## แล็บ: การสร้างเซิร์ฟเวอร์ MCP stdio ที่เรียบง่าย

ในแล็บนี้ เราจะสร้างเซิร์ฟเวอร์ MCP เรียบง่ายโดยใช้การขนส่ง stdio ที่แนะนำ เซิร์ฟเวอร์นี้จะเปิดเผยเครื่องมือที่ไคลเอนต์สามารถเรียกโดยใช้โปรโตคอล Model Context มาตรฐาน

### ข้อกำหนดเบื้องต้น

- Python 3.8 หรือสูงกว่า
- MCP Python SDK: `pip install mcp`
- ความเข้าใจพื้นฐานเกี่ยวกับโปรแกรมแบบอะซิงโครนัส

มาเริ่มสร้างเซิร์ฟเวอร์ MCP stdio แรกของเรากัน:

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
    # ใช้การขนส่ง stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ความแตกต่างหลักจากวิธีที่เลิกใช้ SSE

**การขนส่ง Stdio (มาตรฐานปัจจุบัน):**
- แบบโมเดลกระบวนการย่อยง่าย ๆ - ไคลเอนต์เปิดเซิร์ฟเวอร์ในฐานะกระบวนการลูก
- สื่อสารผ่าน stdin/stdout โดยใช้ข้อความ JSON-RPC
- ไม่ต้องตั้งค่าเว็บเซิร์ฟเวอร์ HTTP
- มีประสิทธิภาพและความปลอดภัยที่ดีขึ้น
- ง่ายต่อการดีบักและพัฒนา

**การขนส่ง SSE (เลิกใช้ตั้งแต่ MCP 2025-06-18):**
- ต้องการเว็บเซิร์ฟเวอร์พร้อมจุดปลาย SSE
- การตั้งค่าซับซ้อนกับโครงสร้างพื้นฐานเว็บเซิร์ฟเวอร์
- พิจารณาเรื่องความปลอดภัยเพิ่มเติมสำหรับจุดปลาย HTTP
- ปัจจุบันถูกแทนที่ด้วย Streamable HTTP สำหรับสถานการณ์บนเว็บ

### การสร้างเซิร์ฟเวอร์ด้วยการขนส่ง stdio

เพื่อสร้างเซิร์ฟเวอร์ stdio ของเรา เราต้อง:

1. **นำเข้าห้องสมุดที่จำเป็น** - เราต้องการส่วนประกอบเซิร์ฟเวอร์ MCP และการขนส่ง stdio
2. **สร้างอินสแตนซ์เซิร์ฟเวอร์** - กำหนดเซิร์ฟเวอร์และความสามารถของมัน
3. **กำหนดเครื่องมือ** - เพิ่มฟังก์ชันที่ต้องการเปิดเผย
4. **ตั้งค่าการขนส่ง** - กำหนดค่าการสื่อสาร stdio
5. **รันเซิร์ฟเวอร์** - เริ่มเซิร์ฟเวอร์และจัดการกับข้อความ

มาสร้างทีละขั้นตอนกัน:

### ขั้นตอนที่ 1: สร้างเซิร์ฟเวอร์ stdio เบื้องต้น

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# กำหนดการบันทึกเหตุการณ์
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

### ขั้นตอนที่ 3: การรันเซิร์ฟเวอร์

บันทึกโค้ดเป็น `server.py` และรันจากบรรทัดคำสั่ง:

```bash
python server.py
```

เซิร์ฟเวอร์จะเริ่มและรอการป้อนข้อมูลจาก stdin มันสื่อสารโดยใช้ข้อความ JSON-RPC ผ่านการขนส่ง stdio

### ขั้นตอนที่ 4: การทดสอบด้วย Inspector

คุณสามารถทดสอบเซิร์ฟเวอร์ของคุณโดยใช้ MCP Inspector:

1. ติดตั้ง Inspector: `npx @modelcontextprotocol/inspector`
2. รัน Inspector และชี้ไปยังเซิร์ฟเวอร์ของคุณ
3. ทดสอบเครื่องมือที่คุณสร้าง

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## การดีบักเซิร์ฟเวอร์ stdio ของคุณ

### การใช้ MCP Inspector

MCP Inspector เป็นเครื่องมือที่มีคุณค่าสำหรับการดีบักและทดสอบเซิร์ฟเวอร์ MCP นี่คือวิธีใช้กับเซิร์ฟเวอร์ stdio ของคุณ:

1. **ติดตั้ง Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **รัน Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **ทดสอบเซิร์ฟเวอร์ของคุณ**: Inspector มีส่วนติดต่อเว็บที่คุณสามารถ:
   - ดูความสามารถของเซิร์ฟเวอร์
   - ทดสอบเครื่องมือด้วยพารามิเตอร์ต่าง ๆ
   - ติดตามข้อความ JSON-RPC
   - ดีบักปัญหาการเชื่อมต่อ

### การใช้ VS Code

คุณยังสามารถดีบักเซิร์ฟเวอร์ MCP ของคุณโดยตรงใน VS Code:

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

2. ตั้งจุดหยุดในโค้ดเซิร์ฟเวอร์ของคุณ
3. รันดีบักเกอร์และทดสอบกับ Inspector

### เคล็ดลับการดีบักทั่วไป

- ใช้ `stderr` สำหรับบันทึก - ห้ามเขียนอะไรไปยัง `stdout` เพราะสงวนไว้สำหรับข้อความ MCP
- ตรวจสอบให้แน่ใจว่าข้อความ JSON-RPC ทุกข้อความถูกแยกด้วยบรรทัดใหม่
- ทดสอบด้วยเครื่องมือเรียบง่ายก่อนเพิ่มฟังก์ชันซับซ้อน
- ใช้ Inspector เพื่อตรวจสอบรูปแบบข้อความ

## การใช้งานเซิร์ฟเวอร์ stdio ของคุณใน VS Code

เมื่อตัวคุณสร้างเซิร์ฟเวอร์ MCP stdio แล้ว คุณสามารถรวมเข้ากับ VS Code เพื่อใช้กับ Claude หรือไคลเอนต์ MCP ที่รองรับอื่น ๆ

### การกำหนดค่า

1. **สร้างไฟล์การกำหนดค่า MCP** ที่ `%APPDATA%\Claude\claude_desktop_config.json` (Windows) หรือ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

3. **ทดสอบการเชื่อมต่อ**: เริ่มต้นการสนทนากับ Claude และลองใช้เครื่องมือของเซิร์ฟเวอร์:
   - "ช่วยทักทายฉันโดยใช้เครื่องมือทักทายได้ไหม?"
   - "คำนวณผลรวมของ 15 และ 27"
   - "ขอข้อมูลเซิร์ฟเวอร์ได้ไหม?"

### ตัวอย่างเซิร์ฟเวอร์ stdio ด้วย TypeScript

นี่คือตัวอย่าง TypeScript ที่สมบูรณ์สำหรับอ้างอิง:

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

### ตัวอย่างเซิร์ฟเวอร์ stdio ด้วย .NET

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

- สร้างเซิร์ฟเวอร์ MCP โดยใช้การขนส่ง **stdio** ปัจจุบัน (วิธีที่แนะนำ)
- เข้าใจเหตุผลที่เลิกใช้การขนส่ง SSE และหันมาใช้ stdio และ Streamable HTTP
- สร้างเครื่องมือที่ไคลเอนต์ MCP สามารถเรียกใช้งานได้
- ดีบักเซิร์ฟเวอร์ของคุณโดยใช้ MCP Inspector
- รวมเซิร์ฟเวอร์ stdio ของคุณกับ VS Code และ Claude

การขนส่ง stdio ให้วิธีการที่ง่ายกว่า ปลอดภัยกว่า และมีประสิทธิภาพมากกว่าในการสร้างเซิร์ฟเวอร์ MCP เมื่อเทียบกับวิธี SSE ที่เลิกใช้ เป็นวิธีขนส่งที่แนะนำสำหรับการใช้งานเซิร์ฟเวอร์ MCP ส่วนใหญ่ตั้งแต่ข้อกำหนด 2025-06-18


### .NET

1. มาเริ่มสร้างเครื่องมือกันก่อน สำหรับนี้เราจะสร้างไฟล์ *Tools.cs* ด้วยเนื้อหาดังต่อไปนี้:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## แบบฝึกหัด: การทดสอบเซิร์ฟเวอร์ stdio ของคุณ

ตอนนี้ที่คุณได้สร้างเซิร์ฟเวอร์ stdio แล้ว ลองทดสอบเพื่อให้แน่ใจว่าทำงานถูกต้อง

### ข้อกำหนดเบื้องต้น

1. ตรวจสอบให้แน่ใจว่าคุณติดตั้ง MCP Inspector แล้ว:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. โค้ดเซิร์ฟเวอร์ของคุณควรถูกบันทึก (เช่น เป็น `server.py`)

### การทดสอบด้วย Inspector

1. **เริ่ม Inspector พร้อมกับเซิร์ฟเวอร์ของคุณ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **เปิดส่วนติดต่อเว็บ**: Inspector จะเปิดหน้าต่างเบราว์เซอร์แสดงความสามารถของเซิร์ฟเวอร์ของคุณ

3. **ทดสอบเครื่องมือ**: 
   - ลองใช้เครื่องมือ `get_greeting` กับชื่อที่แตกต่างกัน
   - ทดสอบเครื่องมือ `calculate_sum` กับตัวเลขต่าง ๆ
   - เรียกเครื่องมือ `get_server_info` เพื่อดูข้อมูลเมตาของเซิร์ฟเวอร์

4. **ติดตามการสื่อสาร**: Inspector แสดงข้อความ JSON-RPC ที่แลกเปลี่ยนระหว่างไคลเอนต์และเซิร์ฟเวอร์

### สิ่งที่คุณควรเห็น

เมื่อเซิร์ฟเวอร์ของคุณเริ่มต้นอย่างถูกต้อง คุณจะเห็น:
- ความสามารถของเซิร์ฟเวอร์ใน Inspector
- เครื่องมือที่พร้อมสำหรับการทดสอบ
- การแลกเปลี่ยนข้อความ JSON-RPC ที่สำเร็จ
- การตอบสนองของเครื่องมือแสดงในส่วนติดต่อ

### ปัญหาทั่วไปและวิธีแก้ไข

**เซิร์ฟเวอร์ไม่เริ่ม:**
- ตรวจสอบว่าติดตั้ง dependencies ครบ: `pip install mcp`
- ตรวจสอบไวยากรณ์และการเยื้องบรรทัดของ Python
- มองหาข้อความผิดพลาดในคอนโซล

**เครื่องมือไม่แสดง:**
- ตรวจสอบว่ามีตัวตกแต่ง `@server.tool()` อยู่
- ตรวจสอบว่าได้กำหนดฟังก์ชันของเครื่องมือก่อน `main()`
- ยืนยันว่าเซิร์ฟเวอร์ถูกตั้งค่าอย่างถูกต้อง

**ปัญหาการเชื่อมต่อ:**
- ตรวจสอบว่าเซิร์ฟเวอร์ใช้การขนส่ง stdio อย่างถูกต้อง
- ตรวจสอบว่าไม่มีโปรเซสอื่นรบกวน
- ยืนยันไวยากรณ์คำสั่ง Inspector

## การบ้าน

ลองสร้างเซิร์ฟเวอร์ของคุณโดยเพิ่มความสามารถมากขึ้น ดูที่ [หน้านี้](https://api.chucknorris.io/) เพื่อเพิ่มเครื่องมือที่เรียกใช้ API ได้ตามที่คุณต้องการ เซิร์ฟเวอร์จะออกมาเป็นอย่างไรก็ตัดสินใจได้ตามใจคุณ สนุกกับการสร้าง :)
## ตัวอย่างคำตอบ

[ตัวอย่างคำตอบ](./solution/README.md) นี่คือตัวอย่างคำตอบที่เป็นไปได้พร้อมโค้ดที่ทำงานได้

## ข้อสรุปที่สำคัญ

ข้อสรุปหลักจากบทนี้คือ:

- การขนส่ง stdio เป็นกลไกที่แนะนำสำหรับเซิร์ฟเวอร์ MCP ในเครื่อง
- การขนส่ง stdio อนุญาตให้สื่อสารอย่างราบรื่นระหว่างเซิร์ฟเวอร์ MCP และไคลเอนต์โดยใช้สตรีมอินพุตและเอาต์พุตมาตรฐาน
- คุณสามารถใช้ทั้ง Inspector และ Visual Studio Code เพื่อใช้งานเซิร์ฟเวอร์ stdio โดยตรง ทำให้การดีบักและการรวมระบบง่ายขึ้นมาก

## ตัวอย่าง

- [เครื่องคิดเลข Java](../samples/java/calculator/README.md)
- [เครื่องคิดเลข .Net](../../../../03-GettingStarted/samples/csharp)
- [เครื่องคิดเลข JavaScript](../samples/javascript/README.md)
- [เครื่องคิดเลข TypeScript](../samples/typescript/README.md)
- [เครื่องคิดเลข Python](../../../../03-GettingStarted/samples/python) 

## แหล่งข้อมูลเพิ่มเติม

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ต่อไปคืออะไร

## ขั้นตอนถัดไป

ตอนนี้คุณได้เรียนรู้วิธีการสร้างเซิร์ฟเวอร์ MCP ด้วยการขนส่ง stdio แล้ว คุณสามารถสำรวจหัวข้อขั้นสูงเพิ่มเติมได้:

- **ถัดไป**: [HTTP Streaming กับ MCP (Streamable HTTP)](../06-http-streaming/README.md) - เรียนรู้เกี่ยวกับกลไกการขนส่งอีกแบบที่รองรับสำหรับเซิร์ฟเวอร์ระยะไกล
- **ขั้นสูง**: [แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัยของ MCP](../../02-Security/README.md) - นำความปลอดภัยมาประยุกต์ใช้ในเซิร์ฟเวอร์ MCP ของคุณ
- **ผลิตจริง**: [กลยุทธ์การใช้งาน](../09-deployment/README.md) - นำเซิร์ฟเวอร์ของคุณไปใช้งานจริง

## แหล่งข้อมูลเพิ่มเติม

- [ข้อกำหนด MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - ข้อกำหนดปัจจุบัน
- [เอกสาร SDK MCP](https://github.com/modelcontextprotocol/sdk) - เอกสารอ้างอิง SDK สำหรับทุกภาษา
- [ตัวอย่างจากชุมชน](../../06-CommunityContributions/README.md) - ตัวอย่างเซิร์ฟเวอร์เพิ่มเติมจากชุมชน

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->