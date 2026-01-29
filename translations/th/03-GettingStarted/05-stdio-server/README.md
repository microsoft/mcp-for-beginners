# MCP Server ด้วย stdio Transport

> **⚠️ การอัปเดตสำคัญ**: ตั้งแต่ MCP Specification วันที่ 2025-06-18 การใช้งาน SSE (Server-Sent Events) แบบเดี่ยวได้ถูก **ยกเลิก** และแทนที่ด้วย "Streamable HTTP" transport สเปค MCP ปัจจุบันกำหนดวิธีการส่งข้อมูลหลักสองแบบ:
> 1. **stdio** - การรับส่งข้อมูลผ่าน standard input/output (แนะนำสำหรับเซิร์ฟเวอร์ที่ทำงานในเครื่อง)
> 2. **Streamable HTTP** - สำหรับเซิร์ฟเวอร์ระยะไกลที่อาจใช้ SSE ภายใน
>
> บทเรียนนี้ได้รับการปรับปรุงให้เน้นที่ **stdio transport** ซึ่งเป็นวิธีที่แนะนำสำหรับการใช้งาน MCP server ส่วนใหญ่

stdio transport ช่วยให้ MCP server สื่อสารกับ client ผ่าน standard input และ output streams ซึ่งเป็นวิธีที่ใช้กันมากที่สุดและแนะนำในสเปค MCP ปัจจุบัน โดยให้วิธีที่ง่ายและมีประสิทธิภาพในการสร้าง MCP server ที่สามารถผสานรวมกับแอปพลิเคชัน client ได้หลากหลาย

## ภาพรวม

บทเรียนนี้ครอบคลุมวิธีการสร้างและใช้งาน MCP Server ด้วย stdio transport

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- สร้าง MCP Server ด้วย stdio transport
- ดีบั๊ก MCP Server ด้วย Inspector
- ใช้งาน MCP Server ผ่าน Visual Studio Code
- เข้าใจกลไกการส่งข้อมูล MCP ปัจจุบันและเหตุผลที่ stdio ถูกแนะนำ

## stdio Transport - วิธีการทำงาน

stdio transport เป็นหนึ่งในสองประเภทการส่งข้อมูลที่รองรับในสเปค MCP ปัจจุบัน (2025-06-18) วิธีการทำงานมีดังนี้:

- **การสื่อสารที่เรียบง่าย**: เซิร์ฟเวอร์อ่านข้อความ JSON-RPC จาก standard input (`stdin`) และส่งข้อความไปยัง standard output (`stdout`)
- **กระบวนการแบบ subprocess**: client เรียกใช้งาน MCP server เป็น subprocess
- **รูปแบบข้อความ**: ข้อความเป็น JSON-RPC requests, notifications หรือ responses ที่แยกด้วย newlines
- **การบันทึก**: เซิร์ฟเวอร์ **อาจ** เขียนข้อความ UTF-8 ไปยัง standard error (`stderr`) เพื่อบันทึกข้อมูล

### ข้อกำหนดสำคัญ:
- ข้อความ **ต้อง** ถูกแยกด้วย newlines และ **ต้องไม่** มี newlines ฝังอยู่ในข้อความ
- เซิร์ฟเวอร์ **ต้องไม่** เขียนสิ่งใดไปยัง `stdout` ที่ไม่ใช่ข้อความ MCP ที่ถูกต้อง
- client **ต้องไม่** เขียนสิ่งใดไปยัง `stdin` ของเซิร์ฟเวอร์ที่ไม่ใช่ข้อความ MCP ที่ถูกต้อง

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

ในโค้ดข้างต้น:

- เรา import `Server` class และ `StdioServerTransport` จาก MCP SDK
- เราสร้าง instance ของเซิร์ฟเวอร์ด้วยการตั้งค่าพื้นฐานและความสามารถ

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

ในโค้ดข้างต้น:

- เราสร้าง instance ของเซิร์ฟเวอร์โดยใช้ MCP SDK
- กำหนด tools ด้วย decorators
- ใช้ stdio_server context manager เพื่อจัดการ transport

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

ความแตกต่างสำคัญจาก SSE คือ stdio servers:

- ไม่ต้องตั้งค่าเว็บเซิร์ฟเวอร์หรือ HTTP endpoints
- ถูกเรียกใช้งานเป็น subprocess โดย client
- สื่อสารผ่าน stdin/stdout streams
- ง่ายต่อการพัฒนาและดีบั๊ก

## แบบฝึกหัด: การสร้าง stdio Server

ในการสร้างเซิร์ฟเวอร์ของเรา เราต้องคำนึงถึงสองสิ่ง:

- เราต้องใช้เว็บเซิร์ฟเวอร์เพื่อเปิด endpoints สำหรับการเชื่อมต่อและข้อความ

## ห้องปฏิบัติการ: การสร้าง MCP stdio server แบบง่าย

ในห้องปฏิบัติการนี้ เราจะสร้าง MCP server แบบง่ายโดยใช้ stdio transport ที่แนะนำ เซิร์ฟเวอร์นี้จะเปิด tools ที่ client สามารถเรียกใช้งานได้ผ่าน Model Context Protocol

### สิ่งที่ต้องเตรียม

- Python 3.8 หรือใหม่กว่า
- MCP Python SDK: `pip install mcp`
- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรมแบบ async

เริ่มต้นสร้าง MCP stdio server แรกของเรา:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ความแตกต่างสำคัญจากวิธี SSE ที่ถูกยกเลิก

**Stdio Transport (มาตรฐานปัจจุบัน):**
- โมเดล subprocess ที่เรียบง่าย - client เรียกใช้งานเซิร์ฟเวอร์เป็น child process
- สื่อสารผ่าน stdin/stdout โดยใช้ข้อความ JSON-RPC
- ไม่ต้องตั้งค่าเว็บเซิร์ฟเวอร์
- ประสิทธิภาพและความปลอดภัยที่ดีกว่า
- ง่ายต่อการดีบั๊กและพัฒนา

**SSE Transport (ถูกยกเลิกตั้งแต่ MCP 2025-06-18):**
- ต้องใช้เว็บเซิร์ฟเวอร์ที่มี SSE endpoints
- การตั้งค่าที่ซับซ้อนมากขึ้นด้วยโครงสร้างเว็บเซิร์ฟเวอร์
- มีข้อพิจารณาด้านความปลอดภัยเพิ่มเติมสำหรับ HTTP endpoints
- ถูกแทนที่ด้วย Streamable HTTP สำหรับกรณีที่ใช้เว็บ

### การสร้างเซิร์ฟเวอร์ด้วย stdio transport

ในการสร้าง stdio server เราต้อง:

1. **Import libraries ที่จำเป็น** - เราต้องใช้ MCP server components และ stdio transport
2. **สร้าง instance ของเซิร์ฟเวอร์** - กำหนดเซิร์ฟเวอร์พร้อมความสามารถ
3. **กำหนด tools** - เพิ่มฟังก์ชันที่เราต้องการเปิดใช้งาน
4. **ตั้งค่า transport** - กำหนดการสื่อสารผ่าน stdio
5. **เรียกใช้งานเซิร์ฟเวอร์** - เริ่มเซิร์ฟเวอร์และจัดการข้อความ

สร้างทีละขั้นตอน:

### ขั้นตอนที่ 1: สร้าง stdio server แบบพื้นฐาน

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### ขั้นตอนที่ 2: เพิ่ม tools เพิ่มเติม

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

### ขั้นตอนที่ 3: เรียกใช้งานเซิร์ฟเวอร์

บันทึกโค้ดเป็น `server.py` และเรียกใช้งานจาก command line:

```bash
python server.py
```

เซิร์ฟเวอร์จะเริ่มต้นและรอรับ input จาก stdin โดยสื่อสารผ่านข้อความ JSON-RPC ผ่าน stdio transport

### ขั้นตอนที่ 4: ทดสอบด้วย Inspector

คุณสามารถทดสอบเซิร์ฟเวอร์ของคุณด้วย MCP Inspector:

1. ติดตั้ง Inspector: `npx @modelcontextprotocol/inspector`
2. เรียกใช้งาน Inspector และชี้ไปยังเซิร์ฟเวอร์ของคุณ
3. ทดสอบ tools ที่คุณสร้างขึ้น

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## การดีบั๊ก stdio server ของคุณ

### การใช้ MCP Inspector

MCP Inspector เป็นเครื่องมือที่มีประโยชน์สำหรับการดีบั๊กและทดสอบ MCP servers วิธีการใช้งานกับ stdio server ของคุณ:

1. **ติดตั้ง Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **เรียกใช้งาน Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **ทดสอบเซิร์ฟเวอร์ของคุณ**: Inspector มี web interface ที่คุณสามารถ:
   - ดูความสามารถของเซิร์ฟเวอร์
   - ทดสอบ tools ด้วยพารามิเตอร์ต่าง ๆ
   - ตรวจสอบข้อความ JSON-RPC
   - ดีบั๊กปัญหาการเชื่อมต่อ

### การใช้ VS Code

คุณสามารถดีบั๊ก MCP server ของคุณโดยตรงใน VS Code:

1. สร้าง launch configuration ใน `.vscode/launch.json`:
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
3. เรียกใช้งาน debugger และทดสอบด้วย Inspector

### เคล็ดลับการดีบั๊กทั่วไป

- ใช้ `stderr` สำหรับการบันทึก - อย่าเขียนไปยัง `stdout` เพราะถูกสงวนไว้สำหรับข้อความ MCP
- ตรวจสอบให้แน่ใจว่าข้อความ JSON-RPC ถูกแยกด้วย newlines
- ทดสอบด้วย tools แบบง่ายก่อนเพิ่มฟังก์ชันที่ซับซ้อน
- ใช้ Inspector เพื่อตรวจสอบรูปแบบข้อความ

## การใช้งาน stdio server ของคุณใน VS Code

เมื่อคุณสร้าง MCP stdio server แล้ว คุณสามารถผสานรวมกับ VS Code เพื่อใช้งานกับ Claude หรือ client ที่รองรับ MCP อื่น ๆ

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

2. **รีสตาร์ท Claude**: ปิดและเปิด Claude ใหม่เพื่อโหลดการตั้งค่าเซิร์ฟเวอร์

3. **ทดสอบการเชื่อมต่อ**: เริ่มการสนทนากับ Claude และลองใช้ tools ของเซิร์ฟเวอร์ของคุณ:
   - "ช่วยทักทายฉันด้วย greeting tool ได้ไหม?"
   - "คำนวณผลรวมของ 15 และ 27"
   - "ข้อมูลเซิร์ฟเวอร์คืออะไร?"

### ตัวอย่าง stdio server ใน TypeScript

นี่คือตัวอย่าง TypeScript แบบสมบูรณ์สำหรับอ้างอิง:

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

// Add tools
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

### ตัวอย่าง stdio server ใน .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## สรุป

ในบทเรียนที่ปรับปรุงนี้ คุณได้เรียนรู้วิธี:

- สร้าง MCP servers โดยใช้ **stdio transport** (วิธีที่แนะนำ)
- เข้าใจเหตุผลที่ SSE transport ถูกยกเลิกและแทนที่ด้วย stdio และ Streamable HTTP
- สร้าง tools ที่ client MCP สามารถเรียกใช้งานได้
- ดีบั๊กเซิร์ฟเวอร์ของคุณด้วย MCP Inspector
- ผสานรวม stdio server ของคุณกับ VS Code และ Claude

stdio transport ให้วิธีที่ง่ายกว่า ปลอดภัยกว่า และมีประสิทธิภาพมากกว่าในการสร้าง MCP servers เมื่อเทียบกับวิธี SSE ที่ถูกยกเลิก เป็นวิธีที่แนะนำสำหรับการใช้งาน MCP server ส่วนใหญ่ตามสเปค 2025-06-18

### .NET

1. สร้าง tools ก่อน โดยสร้างไฟล์ *Tools.cs* ด้วยเนื้อหาดังนี้:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## แบบฝึกหัด: ทดสอบ stdio server ของคุณ

เมื่อคุณสร้าง stdio server แล้ว ลองทดสอบเพื่อให้แน่ใจว่าทำงานได้ถูกต้อง

### สิ่งที่ต้องเตรียม

1. ตรวจสอบให้แน่ใจว่าคุณติดตั้ง MCP Inspector แล้ว:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. โค้ดเซิร์ฟเวอร์ของคุณควรถูกบันทึก (เช่น `server.py`)

### การทดสอบด้วย Inspector

1. **เริ่ม Inspector พร้อมเซิร์ฟเวอร์ของคุณ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **เปิด web interface**: Inspector จะเปิดหน้าต่างเบราว์เซอร์ที่แสดงความสามารถของเซิร์ฟเวอร์ของคุณ

3. **ทดสอบ tools**: 
   - ลองใช้ `get_greeting` tool กับชื่อที่ต่างกัน
   - ทดสอบ `calculate_sum` tool กับตัวเลขต่าง ๆ
   - เรียกใช้ `get_server_info` tool เพื่อดู metadata ของเซิร์ฟเวอร์

4. **ตรวจสอบการสื่อสาร**: Inspector แสดงข้อความ JSON-RPC ที่ถูกแลกเปลี่ยนระหว่าง client และเซิร์ฟเวอร์

### สิ่งที่คุณควรเห็น

เมื่อเซิร์ฟเวอร์ของคุณเริ่มต้นอย่างถูกต้อง คุณควรเห็น:
- ความสามารถของเซิร์ฟเวอร์ที่แสดงใน Inspector
- tools ที่พร้อมใช้งานสำหรับการทดสอบ
- การแลกเปลี่ยนข้อความ JSON-RPC ที่สำเร็จ
- การตอบกลับ tools ที่แสดงใน interface

### ปัญหาทั่วไปและวิธีแก้ไข

**เซิร์ฟเวอร์ไม่เริ่มต้น:**
- ตรวจสอบว่าติดตั้ง dependencies ทั้งหมดแล้ว: `pip install mcp`
- ตรวจสอบ syntax และการจัดวาง Python
- ดูข้อความ error ใน console

**tools ไม่ปรากฏ:**
- ตรวจสอบว่ามี `@server.tool()` decorators
- ตรวจสอบว่าฟังก์ชัน tools ถูกกำหนดก่อน `main()`
- ตรวจสอบว่าเซิร์ฟเวอร์ถูกตั้งค่าอย่างถูกต้อง

**ปัญหาการเชื่อมต่อ:**
- ตรวจสอบว่าเซิร์ฟเวอร์ใช้ stdio transport อย่างถูกต้อง
- ตรวจสอบว่าไม่มี process อื่นรบกวน
- ตรวจสอบ syntax คำสั่ง Inspector

## การบ้าน

ลองสร้างเซิร์ฟเวอร์ของคุณด้วยความสามารถเพิ่มเติม ดู [หน้านี้](https://api.chucknorris.io/) เพื่อเพิ่ม tool ที่เรียก API ตัวอย่าง คุณสามารถออกแบบเซิร์ฟเวอร์ได้ตามใจ สนุกกับการสร้าง!

## ทางแก้ไข

[Solution](./solution/README.md) นี่คือตัวอย่างโค้ดที่ทำงานได้

## ประเด็นสำคัญ

ประเด็นสำคัญจากบทนี้คือ:

- stdio transport เป็นกลไกที่แนะนำสำหรับ MCP servers ที่ทำงานในเครื่อง
- stdio transport ช่วยให้การสื่อสารระหว่าง MCP servers และ clients เป็นไปอย่างราบรื่นผ่าน standard input และ output streams
- คุณสามารถใช้ Inspector และ Visual Studio Code เพื่อใช้งาน stdio servers ได้โดยตรง ทำให้การดีบั๊กและการผสานรวมเป็นเรื่องง่าย

## ตัวอย่าง

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## แหล่งข้อมูลเพิ่มเติม

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## สิ่งที่จะเรียนรู้ต่อไป

## ขั้นตอนถัดไป

เมื่อคุณเรียนรู้วิธีสร้าง MCP servers ด้วย stdio transport แล้ว คุณสามารถสำรวจหัวข้อขั้นสูงเพิ่มเติม:

- **ถัดไป**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - เรียนรู้เกี่ยวกับกลไกการส่งข้อมูลที่รองรับสำหรับเซิร์ฟเวอร์ระยะไกล
- **ขั้นสูง**: [MCP Security Best Practices](../../02-Security/README.md) - ใช้การรักษาความปลอดภัยใน MCP servers ของคุณ
- **การใช้งานจริง**: [Deployment Strategies](../09-deployment/README.md) - นำเซิร์ฟเวอร์ของคุณไปใช้งานจริง

## แหล่งข้อมูลเพิ่มเติม

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - สเปคอย่างเป็นทางการ
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - เอกสารอ้างอิง SDK สำหรับทุกภาษา
- [Community Examples](../../06-CommunityContributions/README.md) - ตัวอย่างเซิร์ฟเวอร์เพิ่มเติมจากชุมชน

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้