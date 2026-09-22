# การสร้างไคลเอนต์

ไคลเอนต์คือแอปพลิเคชันหรือสคริปต์แบบกำหนดเองที่สื่อสารโดยตรงกับ MCP Server เพื่อร้องขอทรัพยากร เครื่องมือ และพรอมต์ ต่างจากการใช้เครื่องมือ inspector ซึ่งให้ส่วนติดต่อกราฟิกสำหรับโต้ตอบกับเซิร์ฟเวอร์ การเขียนไคลเอนต์ของคุณเองทำให้สามารถโต้ตอบแบบโปรแกรมและอัตโนมัติได้ ซึ่งช่วยให้นักพัฒนาสามารถผนวกความสามารถของ MCP เข้ากับเวิร์กโฟลว์ของตนเอง อัตโนมัติงาน และสร้างโซลูชันแบบกำหนดเองที่สอดคล้องกับความต้องการเฉพาะ

## ภาพรวม

บทเรียนนี้จะแนะนำแนวคิดของไคลเอนต์ภายในระบบ Model Context Protocol (MCP) คุณจะได้เรียนรู้วิธีเขียนไคลเอนต์ของคุณเองและให้มันเชื่อมต่อกับ MCP Server

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- เข้าใจสิ่งที่ไคลเอนต์สามารถทำได้
- เขียนไคลเอนต์ของคุณเอง
- เชื่อมต่อและทดสอบไคลเอนต์กับ MCP server เพื่อให้แน่ใจว่าเซิร์ฟเวอร์ทำงานตามที่คาดไว้

## สิ่งที่ต้องมีในการเขียนไคลเอนต์

ในการเขียนไคลเอนต์ คุณจะต้องทำดังนี้:

- **นำเข้าห้องสมุดที่ถูกต้อง** คุณจะใช้ไลบรารีเดิมเช่นก่อนหน้านี้แต่โครงสร้างจะแตกต่างกันเล็กน้อย
- **สร้างอินสแตนซ์ไคลเอนต์** ซึ่งจะเกี่ยวข้องกับการสร้างอินสแตนซ์ไคลเอนต์และเชื่อมต่อกับวิธีการขนส่งที่เลือก
- **ตัดสินใจว่าจะเลือกทรัพยากรอะไรมาแสดง** เซิร์ฟเวอร์ MCP ของคุณมาพร้อมทรัพยากร เครื่องมือ และพรอมต์ คุณต้องเลือกว่าจะซื้ออะไรมาแสดง
- **ผนวกไคลเอนต์กับแอปพลิเคชันโฮสต์** เมื่อคุณรู้ความสามารถของเซิร์ฟเวอร์แล้ว คุณต้องผนวกสิ่งนี้กับแอปพลิเคชันโฮสต์ของคุณ เพื่อให้เมื่อผู้ใช้พิมพ์พรอมต์หรือคำสั่งอื่น ๆ ฟังก์ชันที่เหมาะสมของเซิร์ฟเวอร์จะถูกเรียกใช้งาน

ตอนนี้เราเข้าใจในภาพรวมสิ่งที่เรากำลังจะทำแล้ว มาดูตัวอย่างกันต่อไป

### ตัวอย่างไคลเอนต์

มาดูตัวอย่างไคลเอนต์นี้กัน:

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// รายการพรอมต์
const prompts = await client.listPrompts();

// รับพรอมต์
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// รายการทรัพยากร
const resources = await client.listResources();

// อ่านทรัพยากร
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// เรียกใช้งานเครื่องมือ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ในรหัสที่ผ่านมานั้น เราได้ทำ:

- นำเข้าไลบรารี
- สร้างอินสแตนซ์ไคลเอนต์และเชื่อมต่อโดยใช้ stdio เป็นการขนส่ง
- แสดงรายชื่อพรอมต์ ทรัพยากร และเครื่องมือ และเรียกใช้งานทั้งหมด

นี่แหละคือไคลเอนต์ที่สามารถสื่อสารกับ MCP Server ได้

ให้เราใช้เวลาในส่วนของแบบฝึกหัดถัดไปในการแยกรหัสแต่ละส่วนและอธิบายสิ่งที่เกิดขึ้น

## แบบฝึกหัด: การเขียนไคลเอนต์

อย่างที่กล่าวไว้ข้างต้น ให้เราใช้เวลาอธิบายรหัส และตามสะดวกคุณสามารถโค้ดตามได้เลย

### -1- การนำเข้าไลบรารี

มานำเข้าไลบรารีที่เราต้องการกัน เราจะต้องอ้างอิงถึงไคลเอนต์และโปรโตคอลการขนส่งที่เลือกคือ stdio stdio เป็นโปรโตคอลสำหรับสิ่งที่รันบนเครื่องของคุณโดยตรง SSE เป็นโปรโตคอลขนส่งอีกแบบที่เราจะแสดงในบทต่อไป แต่ชั่วคราวนี้มาลองใช้ stdio กันก่อน

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

สำหรับ Java คุณจะสร้างไคลเอนต์ที่เชื่อมกับ MCP server จากแบบฝึกหัดก่อนหน้า โดยใช้โครงสร้างโปรเจกต์ Java Spring Boot เดิมจาก [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) สร้างคลาส Java ใหม่ชื่อ `SDKClient` ในโฟลเดอร์ `src/main/java/com/microsoft/mcp/sample/client/` และเพิ่มการนำเข้าดังนี้:

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

คุณจะต้องเพิ่ม dependencies ต่อไปนี้ในไฟล์ `Cargo.toml` ของคุณ

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

จากนั้น คุณสามารถนำเข้าไลบรารีที่จำเป็นในโค้ดไคลเอนต์ของคุณได้

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ต่อไปเราจะมาสร้างอินสแตนซ์

### -2- การสร้างอินสแตนซ์ของไคลเอนต์และตัวขนส่ง

เราจะต้องสร้างอินสแตนซ์ของตัวขนส่งและของไคลเอนต์ของเรา:

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

ในโค้ดด้านบน เราได้ทำ:

- สร้างอินสแตนซ์ stdio transport โดยระบุคำสั่งและอาร์กิวเมนต์สำหรับหาตำแหน่งและเริ่มเซิร์ฟเวอร์ เพราะนั่นคือสิ่งที่เราต้องทำขณะที่สร้างไคลเอนต์

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- สร้างอินสแตนซ์ไคลเอนต์โดยให้ชื่อและเวอร์ชัน

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- เชื่อมต่อไคลเอนต์กับตัวขนส่งที่เลือก

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# สร้างพารามิเตอร์เซิร์ฟเวอร์สำหรับการเชื่อมต่อ stdio
server_params = StdioServerParameters(
    command="mcp",  # ไฟล์ปฏิบัติการ
    args=["run", "server.py"],  # อาร์กิวเมนต์บรรทัดคำสั่งที่เป็นทางเลือก
    env=None,  # ตัวแปรสิ่งแวดล้อมที่เป็นทางเลือก
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # เริ่มต้นการเชื่อมต่อ
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

ในโค้ดด้านบน เราได้ทำ:

- นำเข้าไลบรารีที่จำเป็น
- สร้างออบเจกต์พารามิเตอร์เซิร์ฟเวอร์เพื่อใชรันเซิร์ฟเวอร์เพื่อให้เชื่อมต่อกับไคลเอนต์ได้
- กำหนดเมธอด `run` ที่เรียก `stdio_client` เพื่อเริ่มเซสชันไคลเอนต์
- สร้างจุดเข้าใช้งานโดยส่ง `run` ให้กับ `asyncio.run`

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

ในโค้ดด้านบน เราได้ทำ:

- นำเข้าไลบรารีที่จำเป็น
- สร้าง stdio transport และไคลเอนต์ชื่อ `mcpClient` ซึ่งจะใช้สำหรับแสดงรายการและเรียกใช้ฟีเจอร์บน MCP Server

โปรดทราบ ใน "Arguments" คุณสามารถระบุได้ว่าจะใช้ *.csproj* หรือไฟล์ปฏิบัติการ executable

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // โลจิกของไคลเอนต์ของคุณไปที่นี่
    }
}
```

ในโค้ดด้านบน เราได้ทำ:

- สร้าง main method ที่ตั้งค่า SSE transport ชี้ไปที่ `http://localhost:8080` ซึ่งคือที่เซิร์ฟเวอร์ MCP ของเราจะรัน
- สร้างคลาสไคลเอนต์ที่รับ transport เป็นพารามิเตอร์ในคอนสตรัคเตอร์
- ในเมธอด `run` เราสร้าง MCP client แบบ synchronous โดยใช้ transport และเริ่มต้นการเชื่อมต่อ
- ใช้ SSE (Server-Sent Events) transport ซึ่งเหมาะกับการสื่อสาร HTTP กับ MCP server ของ Java Spring Boot

#### Rust

โปรดสังเกตว่าไคลเอนต์ Rust นี้สมมุติว่าเซิร์ฟเวอร์เป็นโปรเจกต์พี่น้องชื่อ "calculator-server" ในไดเรกทอรีเดียวกัน โค้ดด้านล่างจะสตาร์ทเซิร์ฟเวอร์และเชื่อมต่อกับมัน

```rust
async fn main() -> Result<(), RmcpError> {
    // สมมติว่าเซิร์ฟเวอร์เป็นโปรเจกต์พี่น้องชื่อ "calculator-server" ในไดเรกทอรีเดียวกัน
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: เริ่มต้น

    // TODO: แสดงรายการเครื่องมือ

    // TODO: เรียกใช้เครื่องมือเพิ่มด้วยอาร์กิวเมนต์ = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- การแสดงคุณลักษณะของเซิร์ฟเวอร์

ตอนนี้เรามีไคลเอนต์ที่สามารถเชื่อมต่อได้ในขณะรันโปรแกรม แต่มันยังไม่แสดงคุณสมบัติของเซิร์ฟเวอร์ ดังนั้นมาทำการแสดงรายการคุณสมบัติกัน:

#### TypeScript

```typescript
// แสดงรายการพรอมต์
const prompts = await client.listPrompts();

// แสดงรายการแหล่งข้อมูล
const resources = await client.listResources();

// แสดงรายการเครื่องมือ
const tools = await client.listTools();
```

#### Python

```python
# แสดงรายการทรัพยากรที่มีให้ใช้
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# แสดงรายการเครื่องมือที่มีให้ใช้
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ที่นี่ เราแสดงรายการทรัพยากรที่มีอยู่ `list_resources()` และเครื่องมือ `list_tools` และพิมพ์ออกมา

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ข้างต้นคือตัวอย่างของการแสดงรายการเครื่องมือบนเซิร์ฟเวอร์ สำหรับแต่ละเครื่องมือ เราจะพิมพ์ชื่อของมันออกมา

#### Java

```java
// รายการและสาธิตเครื่องมือ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// คุณยังสามารถส่งคำสั่ง ping ไปยังเซิร์ฟเวอร์เพื่อยืนยันการเชื่อมต่อได้
client.ping();
```

ในโค้ดด้านบน เราได้ทำ:

- เรียก `listTools()` เพื่อดึงเครื่องมือทั้งหมดที่ใช้ได้จาก MCP server
- ใช้ `ping()` เพื่อตรวจสอบการเชื่อมต่อกับเซิร์ฟเวอร์
- `ListToolsResult` มีข้อมูลเกี่ยวกับเครื่องมือทั้งหมด รวมชื่อ คำอธิบาย และสคีมารับอินพุต

ดีเยี่ยม ตอนนี้เราได้เก็บข้อมูลคุณลักษณะทั้งหมดไว้แล้ว ตอนนี้คำถามคือเมื่อไหร่เราจะใช้มัน? ไคลเอนต์ตัวนี้ค่อนข้างง่าย หมายความว่าเราต้องเรียกใช้ฟีเจอร์เองเมื่อเราต้องการ ในบทถัดไปเราจะสร้างไคลเอนต์ขั้นสูงที่มีแบบจำลองภาษาใหญ๋ (LLM) ของตัวเอง แต่ชั่วคราวนี้มาดูวิธีเรียกใช้ฟีเจอร์บนเซิร์ฟเวอร์:

#### Rust

ในฟังก์ชันหลัก หลังจากเริ่มไคลเอนต์แล้ว เราสามารถเริ่มเซิร์ฟเวอร์และแสดงรายการฟีเจอร์บางส่วนได้

```rust
// เริ่มต้น
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// รายการเครื่องมือ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- การเรียกใช้ฟีเจอร์

การเรียกใช้ฟีเจอร์เราต้องแน่ใจว่ากำหนดอาร์กิวเมนต์ให้ถูกต้องและในบางกรณีต้องระบุชื่อของสิ่งที่พยายามเรียกใช้ด้วย

#### TypeScript

```typescript

// อ่านทรัพยากร
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// เรียกใช้เครื่องมือ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// เรียก prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

ในโค้ดด้านบน เราได้ทำ:

- อ่านทรัพยากรหนึ่ง เราเรียกทรัพยากรโดยการเรียก `readResource()` พร้อม `uri` นี่คือตัวอย่างรูปแบบบนเซิร์ฟเวอร์:

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    ค่าของ `uri` คือ `file://example.txt` จะตรงกับ `file://{name}` บนเซิร์ฟเวอร์ โดย `example.txt` จะถูกแมปไปที่ `name`

- เรียกเครื่องมือโดยระบุ `name` และ `arguments` ดังนี้:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- รับพรอมต์โดยเรียก `getPrompt()` พร้อม `name` และ `arguments` โค้ดเซิร์ฟเวอร์จะเป็นแบบนี้:

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    ดังนั้นรหัสของไคลเอนต์จะเป็นแบบนี้เพื่อให้ตรงกับเซิร์ฟเวอร์

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# อ่านทรัพยากร
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# เรียกใช้เครื่องมือ
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

ในโค้ดด้านบน เราได้ทำ:

- เรียกทรัพยากรชื่อ `greeting` ด้วย `read_resource`
- เรียกเครื่องมือชื่อ `add` ด้วย `call_tool`

#### .NET

1. มาเพิ่มโค้ดเพื่อเรียกเครื่องมือ:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. สำหรับการพิมพ์ผลลัพธ์ นี่คือโค้ดที่จัดการเรื่องนั้น:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// เรียกใช้เครื่องมือเครื่องคิดเลขต่างๆ
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

ในโค้ดด้านบน เราได้ทำ:

- เรียกเครื่องมือเครื่องคิดเลขหลายตัวโดยใช้เมธอด `callTool()` กับออบเจกต์ `CallToolRequest`
- แต่ละการเรียกเครื่องมือจะระบุชื่อและแผนที่ `Map` ของอาร์กิวเมนต์ที่เครื่องมือแต่ละตัวต้องใช้
- เครื่องมือบนเซิร์ฟเวอร์คาดหวังชื่อพารามิเตอร์เฉพาะ (เช่น "a", "b" สำหรับการดำเนินการทางคณิตศาสตร์)
- ผลลัพธ์จะถูกส่งกลับในรูปแบบออบเจกต์ `CallToolResult` ที่มีการตอบสนองจากเซิร์ฟเวอร์

#### Rust

```rust
// เรียกใช้เครื่องมือเพิ่มโดยมีอาร์กิวเมนต์ = {"a": 3, "b": 2}
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- รันไคลเอนต์

ในการรันไคลเอนต์ ให้พิมพ์คำสั่งนี้ในเทอร์มินัล:

#### TypeScript

เพิ่มรายการต่อไปนี้ในส่วน "scripts" ของ *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

เรียกไคลเอนต์ด้วยคำสั่งนี้:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

ก่อนอื่นให้แน่ใจว่า MCP server ของคุณกำลังรันที่ `http://localhost:8080` แล้วจึงรันไคลเอนต์:

```bash
# สร้างโปรเจกต์ของคุณ
./mvnw clean compile

# รันไคลเอนต์
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

หรือคุณสามารถรันโปรเจกต์ไคลเอนต์เต็มรูปแบบที่ให้ไว้ในโฟลเดอร์ solution `03-GettingStarted\02-client\solution\java`:

```bash
# ไปที่ไดเรกทอรีของโซลูชัน
cd 03-GettingStarted/02-client/solution/java

# สร้างและรัน JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## การบ้าน

ในการบ้านนี้ คุณจะใช้สิ่งที่คุณได้เรียนรู้ในการสร้างไคลเอนต์ แต่สร้างไคลเอนต์ของคุณเอง

นี่คือเซิร์ฟเวอร์ที่คุณสามารถใช้ซึ่งคุณต้องเรียกผ่านโค้ดไคลเอนต์ของคุณ ลองดูว่าคุณสามารถเพิ่มฟีเจอร์เพิ่มเติมให้เซิร์ฟเวอร์เพื่อทำให้มันน่าสนใจมากขึ้นได้หรือไม่

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// สร้างเซิร์ฟเวอร์ MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// เพิ่มเครื่องมือบวก
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// เพิ่มแหล่งคำทักทายแบบไดนามิก
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// เริ่มรับข้อความจาก stdin และส่งข้อความไปยัง stdout

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# สร้างเซิร์ฟเวอร์ MCP
mcp = FastMCP("Demo")


# เพิ่มเครื่องมือบวกเลข
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# เพิ่มทรัพยากรคำทักทายแบบไดนามิก
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

ดูโปรเจกต์นี้เพื่อดูวิธีที่คุณสามารถ [เพิ่มพรอมต์และทรัพยากร](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)

นอกจากนี้ ให้ตรวจสอบลิงก์นี้สำหรับวิธีเรียกใช้ [พรอมต์และทรัพยากร](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)

### Rust

ใน [ส่วนก่อนหน้า](../../../../03-GettingStarted/01-first-server) คุณได้เรียนรู้วิธีสร้าง MCP server แบบง่ายด้วย Rust คุณสามารถพัฒนาต่อจากนั้น หรือดูตัวอย่าง MCP server ที่เขียนด้วย Rust เพิ่มเติมได้ที่: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## โซลูชัน

**โฟลเดอร์โซลูชัน** มีการนำเสนอการใช้งานไคลเอนต์ที่สมบูรณ์พร้อมรันจริง ซึ่งแสดงให้เห็นแนวคิดทั้งหมดที่อธิบายในบทแนะนำนี้ แต่ละโซลูชันมีโค้ดไคลเอนต์และเซิร์ฟเวอร์ในโปรเจกต์แยกส่วนที่สมบูรณ์

### 📁 โครงสร้างโซลูชัน

โฟลเดอร์โซลูชันถูกจัดตามภาษาโปรแกรมมิ่ง:

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 สิ่งที่แต่ละโซลูชันมี

โซลูชันเฉพาะแต่ละภาษา มี:

- **การใช้งานไคลเอนต์สมบูรณ์** พร้อมคุณสมบัติทั้งหมดจากบทแนะนำ
- **โครงสร้างโปรเจกต์ที่ใช้งานได้จริง** พร้อม dependencies และการตั้งค่าที่ถูกต้อง
- **สคริปต์สร้างและรัน** เพื่อความสะดวกในการตั้งค่าและใช้งาน
- **README รายละเอียด** พร้อมคำแนะนำเฉพาะภาษา
- **ตัวอย่างการจัดการข้อผิดพลาด** และการประมวลผลผลลัพธ์

### 📖 การใช้โซลูชัน

1. **ไปยังโฟลเดอร์ภาษาที่คุณต้องการ**:

   ```bash
   cd solution/typescript/    # สำหรับ TypeScript
   cd solution/java/          # สำหรับ Java
   cd solution/python/        # สำหรับ Python
   cd solution/dotnet/        # สำหรับ .NET
   ```

2. **ทำตามคำแนะนำใน README** ในแต่ละโฟลเดอร์เพื่อ:
   - ติดตั้ง dependencies
   - สร้างโปรเจกต์
   - รันไคลเอนต์

3. **ตัวอย่างผลลัพธ์** ที่คุณควรเห็น:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

สำหรับเอกสารฉบับสมบูรณ์และคำแนะนำทีละขั้นตอน ดูที่: **[📖 เอกสารโซลูชัน](./solution/README.md)**

## 🎯 ตัวอย่างการใช้งานสมบูรณ์

เราได้จัดเตรียมไคลเอนต์ที่ทำงานสมบูรณ์ในทุกภาษาที่ครอบคลุมในบทแนะนำนี้ ตัวอย่างเหล่านี้แสดงฟังก์ชันการทำงานอย่างครบถ้วนตามที่อธิบายข้างต้น และสามารถใช้เป็นข้อมูลอ้างอิงหรือต้นแบบสำหรับโปรเจกต์ของคุณเอง

### ตัวอย่างสมบูรณ์ที่มีให้ใช้

| ภาษา | ไฟล์ | คำอธิบาย |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | ไคลเอนต์ Java สมบูรณ์โดยใช้ SSE transport พร้อมการจัดการข้อผิดพลาดอย่างละเอียด |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | ไคลเอนต์ C# สมบูรณ์โดยใช้ stdio transport พร้อมการสตาร์ทเซิร์ฟเวอร์อัตโนมัติ |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | ไคลเอนต์ TypeScript สมบูรณ์ที่รองรับโปรโตคอล MCP ทั้งหมด |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | ไคลเอนต์ Python สมบูรณ์โดยใช้แบบ async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | ไคลเอนต์ Rust สมบูรณ์โดยใช้ Tokio สำหรับการทำงานแบบอะซิงโครนัส |

ตัวอย่างสมบูรณ์แต่ละตัวมี:

- ✅ **การสร้างการเชื่อมต่อ** และการจัดการข้อผิดพลาด
- ✅ **การค้นหาเซิร์ฟเวอร์** (เครื่องมือ ทรัพยากร พรอมต์ ถ้ามี)
- ✅ **งานเครื่องคิดเลข** (บวก ลบ คูณ หาร ช่วยเหลือ)
- ✅ **การประมวลผลผลลัพธ์** และการแสดงผลแบบฟอร์แมต
- ✅ **การจัดการข้อผิดพลาดอย่างครอบคลุม**

- ✅ **โค้ดสะอาด มีเอกสารประกอบอย่างชัดเจน** พร้อมคอมเมนต์ทีละขั้นตอน

### การเริ่มต้นใช้งานพร้อมตัวอย่างสมบูรณ์

1. **เลือกภาษาที่คุณต้องการใช้** จากตารางด้านบน
2. **ตรวจสอบไฟล์ตัวอย่างสมบูรณ์** เพื่อเข้าใจวิธีการใช้งานทั้งหมด
3. **รันตัวอย่าง** ตามคำแนะนำใน [`complete_examples.md`](./complete_examples.md)
4. **แก้ไขและขยาย** ตัวอย่างตามกรณีการใช้งานเฉพาะของคุณ

สำหรับเอกสารรายละเอียดเกี่ยวกับการรันและปรับแต่งตัวอย่างเหล่านี้ ดูได้ที่: **[📖 เอกสารตัวอย่างสมบูรณ์](./complete_examples.md)**

### 💡 โซลูชัน vs ตัวอย่างสมบูรณ์

| **โฟลเดอร์โซลูชัน** | **ตัวอย่างสมบูรณ์** |
|--------------------|--------------------- |
| โครงสร้างโปรเจกต์เต็มพร้อมไฟล์บิลด์ | การใช้งานแบบไฟล์เดียว |
| พร้อมใช้งานรวมถึง dependencies | ตัวอย่างโค้ดที่เจาะจง |
| การตั้งค่าเหมือนโปรดักชัน | ใช้อ้างอิงเพื่อการศึกษา |
| เครื่องมือเฉพาะภาษานั้นๆ | การเปรียบเทียบข้ามภาษา |

ทั้งสองแนวทางมีคุณค่า - ใช้ **โฟลเดอร์โซลูชัน** สำหรับโปรเจกต์เต็ม และ **ตัวอย่างสมบูรณ์** สำหรับการเรียนรู้และอ้างอิง

## ข้อสรุปสำคัญ

ข้อสรุปสำคัญสำหรับบทนี้คือเรื่องของไคลเอนต์:

- สามารถใช้เพื่อค้นหาและเรียกใช้ฟีเจอร์บนเซิร์ฟเวอร์ได้
- สามารถเริ่มเซิร์ฟเวอร์ในขณะที่มันเริ่มทำงาน (เช่นในบทนี้) แต่ไคลเอนต์สามารถเชื่อมต่อกับเซิร์ฟเวอร์ที่กำลังทำงานอยู่ได้เช่นกัน
- เป็นวิธีที่ดีในการทดสอบความสามารถของเซิร์ฟเวอร์ เปรียบเทียบกับทางเลือกอื่น เช่น Inspector ที่อธิบายในบทก่อนหน้า

## แหล่งข้อมูลเพิ่มเติม

- [การสร้างไคลเอนต์ใน MCP](https://modelcontextprotocol.io/quickstart/client)

## ตัวอย่าง

- [เครื่องคิดเลข Java](../samples/java/calculator/README.md)
- [เครื่องคิดเลข .NET](../../../../03-GettingStarted/samples/csharp)
- [เครื่องคิดเลข JavaScript](../samples/javascript/README.md)
- [เครื่องคิดเลข TypeScript](../samples/typescript/README.md)
- [เครื่องคิดเลข Python](../../../../03-GettingStarted/samples/python)
- [เครื่องคิดเลข Rust](../../../../03-GettingStarted/samples/rust)

## ต่อไปคืออะไร

- ต่อไป: [การสร้างไคลเอนต์ด้วย LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->