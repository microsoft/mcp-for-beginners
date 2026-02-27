# การสร้างไคลเอนต์

ไคลเอนต์คือแอปพลิเคชันหรือสคริปต์ที่สร้างขึ้นเองซึ่งสื่อสารโดยตรงกับ MCP Server เพื่อขอทรัพยากร เครื่องมือ และพรอมต์ ต่างจากการใช้เครื่องมือ inspector ซึ่งให้ส่วนติดต่อกราฟิกสำหรับการโต้ตอบกับเซิร์ฟเวอร์ การเขียนไคลเอนต์ของคุณเองช่วยให้สามารถโต้ตอบแบบเป็นโปรแกรมและอัตโนมัติได้ ซึ่งช่วยให้นักพัฒนาสามารถผนวกความสามารถของ MCP เข้ากับเวิร์กโฟลว์ของตนเอง อัตโนมัติภารกิจ และสร้างโซลูชันที่ออกแบบเฉพาะสำหรับความต้องการต่าง ๆ

## ภาพรวม

บทเรียนนี้จะแนะนำแนวคิดของไคลเอนต์ในระบบนิเวศ Model Context Protocol (MCP) คุณจะได้เรียนรู้วิธีเขียนไคลเอนต์ของคุณเองและทำให้เชื่อมต่อกับ MCP Server ได้

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- เข้าใจว่าคลไอเอนต์สามารถทำอะไรได้บ้าง
- เขียนไคลเอนต์ของคุณเอง
- เชื่อมต่อและทดสอบไคลเอนต์กับเซิร์ฟเวอร์ MCP เพื่อให้แน่ใจว่าเซิร์ฟเวอร์ทำงานได้ตามที่คาดไว้

## สิ่งที่จำเป็นเมื่อเขียนไคลเอนต์

ในการเขียนไคลเอนต์ คุณจำเป็นต้องทำดังนี้:

- **นำเข้าห้องสมุดที่ถูกต้อง** คุณจะใช้ห้องสมุดเดียวกับที่ใช้อยู่ก่อนหน้านี้ เพียงแต่ใช้โครงสร้างต่างกัน
- **สร้างอินสแตนซ์ไคลเอนต์** ซึ่งจะเกี่ยวข้องกับการสร้างอินสแตนซ์ไคลเอนต์และเชื่อมต่อกับวิธีการขนส่งที่เลือก
- **ตัดสินใจว่าจะรายการทรัพยากรใดบ้าง** เซิร์ฟเวอร์ MCP ของคุณมาพร้อมกับทรัพยากร เครื่องมือ และพรอมต์ คุณต้องตัดสินใจว่าจะรายการอันใดบ้าง
- **ผนวกไคลเอนต์กับแอปโฮสต์** เมื่อคุณทราบความสามารถของเซิร์ฟเวอร์แล้ว คุณจำเป็นต้องผนวกสิ่งนี้กับแอปโฮสต์ของคุณ เพื่อให้เมื่อผู้ใช้พิมพ์พรอมต์หรือคำสั่งอื่น ๆ ฟีเจอร์ของเซิร์ฟเวอร์ที่เกี่ยวข้องถูกเรียกใช้งาน

เมื่อเราเข้าใจภาพรวมแล้วว่ากำลังจะทำอะไร ต่อไปมาดูตัวอย่างกัน

### ตัวอย่างไคลเอนต์

ลองดูตัวอย่างไคลเอนต์นี้:

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

// รายการคำสั่ง
const prompts = await client.listPrompts();

// รับคำสั่ง
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

ในโค้ดด้านบนเราได้:

- นำเข้าห้องสมุด
- สร้างอินสแตนซ์ของไคลเอนต์และเชื่อมต่อโดยใช้ stdio เป็นการขนส่ง
- รายการพรอมต์ ทรัพยากร และเครื่องมือ และเรียกใช้งานทั้งหมด

เท่านี้คุณก็มีไคลเอนต์ที่สามารถพูดคุยกับ MCP Server ได้แล้ว

ตอนต่อไปเราจะใช้เวลาอธิบายแต่ละส่วนของโค้ดอย่างละเอียด

## แบบฝึกหัด: เขียนไคลเอนต์

ดังที่ได้กล่าวไว้ข้างต้น มาใช้เวลาอธิบายโค้ดกัน และแน่นอนว่าเขียนโค้ดตามไปด้วยได้

### -1- นำเข้าห้องสมุด

นำเข้าห้องสมุดที่ต้องใช้ เราจะต้องอ้างอิงถึงไคลเอนต์และโปรโตคอลการขนส่งที่เราเลือก คือ stdio ซึ่งเป็นโปรโตคอลสำหรับสิ่งที่รันบนเครื่องของคุณเอง SSE เป็นโปรโตคอลอีกตัวที่จะแสดงในบทถัดไป แต่นี่คือทางเลือกอื่นของคุณ ตอนนี้เราจะเริ่มกับ stdio

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

สำหรับ Java คุณจะสร้างไคลเอนต์ที่เชื่อมต่อกับ MCP server จากแบบฝึกหัดก่อนหน้า โดยใช้โครงสร้างโปรเจค Java Spring Boot เดียวกันจาก [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) สร้างคลาสใหม่ชื่อ `SDKClient` ในโฟลเดอร์ `src/main/java/com/microsoft/mcp/sample/client/` และเพิ่มการนำเข้าดังนี้:

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

จากนั้นคุณสามารถนำเข้าห้องสมุดที่จำเป็นในโค้ดไคลเอนต์ของคุณได้

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ต่อไปเป็นการสร้างอินสแตนซ์

### -2- การสร้างอินสแตนซ์ไคลเอนต์และการขนส่ง

เราจะต้องสร้างอินสแตนซ์ของการขนส่งและไคลเอนต์:

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

ในโค้ดด้านบนเราได้:

- สร้างอินสแตนซ์ stdio transport สังเกตว่าได้ระบุคำสั่งและอาร์กิวเมนต์สำหรับการค้นหาและเริ่มเซิร์ฟเวอร์ เพราะนั่นคือสิ่งที่เราต้องทำในตอนสร้างไคลเอนต์

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- สร้างอินสแตนซ์ไคลเอนต์โดยกำหนดชื่อและเวอร์ชัน

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- เชื่อมต่อไคลเอนต์กับการขนส่งที่เลือก

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# สร้างพารามิเตอร์เซิร์ฟเวอร์สำหรับการเชื่อมต่อ stdio
server_params = StdioServerParameters(
    command="mcp",  # ไฟล์ที่สามารถรันได้
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

ในโค้ดด้านบนเราได้:

- นำเข้าห้องสมุดที่จำเป็น
- สร้างอ็อบเจ็กต์ server parameters เพื่อใช้รันเซิร์ฟเวอร์ เพื่อให้เชื่อมต่อกับไคลเอนต์ได้
- นิยามเมธอด `run` ซึ่งเรียก `stdio_client` เพื่อเริ่มเซสชันไคลเอนต์
- สร้างจุดเริ่มต้นโดยให้ `run` method กับ `asyncio.run`

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

ในโค้ดด้านบนเราได้:

- นำเข้าห้องสมุดที่จำเป็น
- สร้าง stdio transport และสร้างไคลเอนต์ `mcpClient` ซึ่งเป็นสิ่งที่จะใช้ในการรายการและเรียกใช้งานฟีเจอร์บน MCP Server

โปรดทราบว่าใน "Arguments" คุณสามารถชี้ไปที่ไฟล์ *.csproj* หรือไฟล์ executable ก็ได้

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
        
        // ตรรกะของไคลเอนต์ของคุณจะอยู่ที่นี่
    }
}
```

ในโค้ดด้านบนเราได้:

- สร้างเมธอด main ที่ตั้งค่า SSE transport ชี้ไปที่ `http://localhost:8080` ซึ่งจะเป็นที่เซิร์ฟเวอร์ MCP ของเราจะรัน
- สร้างคลาสไคลเอนต์ที่รับ transport เป็นพารามิเตอร์ใน constructor
- ในเมธอด `run` เราสร้าง MCP client แบบ synchronous โดยใช้ transport และเริ่มการเชื่อมต่อ
- ใช้ SSE (Server-Sent Events) transport ซึ่งเหมาะสำหรับการสื่อสารแบบ HTTP กับ Java Spring Boot MCP servers

#### Rust

โค้ดไคลเอนต์ Rust นี้สมมุติว่าเซิร์ฟเวอร์เป็นโปรเจกต์พี่น้องชื่อ "calculator-server" ในไดเรกทอรีเดียวกัน โค้ดด้านล่างนี้จะเริ่มเซิร์ฟเวอร์และเชื่อมต่อกับมัน

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

    // งานที่จะทำ: เริ่มต้น

    // งานที่จะทำ: แสดงรายการเครื่องมือ

    // งานที่จะทำ: เรียกใช้เครื่องมือเพิ่มด้วยอาร์กิวเมนต์ = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- การรายการฟีเจอร์ของเซิร์ฟเวอร์

ตอนนี้เรามีไคลเอนต์ที่สามารถเชื่อมต่อได้เมื่อตอนรันโปรแกรมแล้ว แต่ยังไม่ได้รายการฟีเจอร์ของเซิร์ฟเวอร์ ดังนั้นมาทำตรงนี้ต่อกัน:

#### TypeScript

```typescript
// รายการพร้อมท์
const prompts = await client.listPrompts();

// รายการทรัพยากร
const resources = await client.listResources();

// รายการเครื่องมือ
const tools = await client.listTools();
```

#### Python

```python
# แสดงรายการทรัพยากรที่มีอยู่
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# แสดงรายการเครื่องมือที่มีอยู่
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ที่นี่เรารายการทรัพยากรที่มี `list_resources()` และเครื่องมือ `list_tools` และพิมพ์ออกมา

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ข้างบนเป็นตัวอย่างวิธีรายการเครื่องมือบนเซิร์ฟเวอร์ สำหรับแต่ละเครื่องมือ เราจะพิมพ์ชื่อของมันออกมา

#### Java

```java
// แสดงรายการและสาธิตเครื่องมือ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// คุณสามารถ ping เซิร์ฟเวอร์เพื่อตรวจสอบการเชื่อมต่อได้ด้วย
client.ping();
```

ในโค้ดนี้เราได้:

- เรียก `listTools()` เพื่อรับเครื่องมือทั้งหมดที่มีอยู่บน MCP server
- ใช้ `ping()` เพื่อตรวจสอบว่าเชื่อมต่อกับเซิร์ฟเวอร์ได้
- `ListToolsResult` มีข้อมูลเกี่ยวกับเครื่องมือทั้งหมดรวมถึงชื่อ คำอธิบาย และสกีมาอินพุต

เยี่ยมมาก ตอนนี้เราได้เก็บข้อมูลฟีเจอร์ทั้งหมดแล้ว คำถามคือเมื่อไหร่เราจะใช้? ไคลเอนต์นี้ค่อนข้างเรียบง่าย ต้องเรียกใช้ฟีเจอร์เหล่านั้นอย่างชัดเจนเมื่อเราต้องการ ในบทถัดไป เราจะสร้างไคลเอนต์ขั้นสูงที่เข้าถึงโมเดลภาษาใหญ่ของตัวเอง (LLM) ได้ แต่ตอนนี้มาดูวิธีเรียกใช้ฟีเจอร์บนเซิร์ฟเวอร์กันก่อน:

#### Rust

ในฟังก์ชัน main หลังจากเริ่มไคลเอนต์แล้ว เราสามารถเริ่มเซิร์ฟเวอร์และรายการฟีเจอร์บางอย่างของมันได้

```rust
// เริ่มต้น
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// รายการเครื่องมือ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- การเรียกใช้ฟีเจอร์

เพื่อเรียกใช้ฟีเจอร์ เราต้องแน่ใจว่าได้ระบุอาร์กิวเมนต์ที่ถูกต้องและในบางกรณีชื่อของสิ่งที่ต้องการเรียกใช้งาน

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

// เรียกคำสั่ง prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

ในโค้ดด้านบนเราได้:

- อ่านทรัพยากรโดยเรียกใช้ `readResource()` โดยระบุ `uri` นี่คือตัวอย่างว่าฝั่งเซิร์ฟเวอร์เป็นอย่างไร:

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

    ค่า `uri` ของเรา `file://example.txt` ตรงกับ `file://{name}` บนเซิร์ฟเวอร์ โดย `example.txt` จะถูกแมปเป็น `name`

- เรียกใช้เครื่องมือโดยระบุ `name` และ `arguments` ดังนี้:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- รับพรอมต์ โดยเรียก `getPrompt()` พร้อมกับ `name` และ `arguments` โค้ดบนเซิร์ฟเวอร์หน้าตาดังนี้:

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

    และโค้ดไคลเอนต์ที่ได้จึงต้องเขียนให้ตรงกับที่ประกาศในเซิร์ฟเวอร์:

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

ในโค้ดนี้เราได้:

- เรียกทรัพยากรชื่อ `greeting` โดยใช้ `read_resource`
- เรียกใช้เครื่องมือชื่อ `add` โดยใช้ `call_tool`

#### .NET

1. เพิ่มโค้ดสำหรับเรียกใช้เครื่องมือ:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. สำหรับการพิมพ์ผลลัพธ์ นี่คือตัวอย่างโค้ดที่จัดการกับผลลัพธ์:

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

ในโค้ดนี้เราได้:

- เรียกใช้เครื่องมือคำนวณหลายรายการ โดยใช้เมธอด `callTool()` กับอ็อบเจ็กต์ `CallToolRequest`
- การเรียกแต่ละเครื่องมือจะระบุชื่อเครื่องมือและ `Map` ของอาร์กิวเมนต์ที่เครื่องมือต้องการ
- เครื่องมือบนเซิร์ฟเวอร์คาดหวังชื่อพารามิเตอร์เฉพาะ (เช่น "a", "b" สำหรับการคำนวณ)
- ผลลัพธ์จะถูกส่งกลับมาในอ็อบเจ็กต์ `CallToolResult` ซึ่งมีการตอบกลับจากเซิร์ฟเวอร์

#### Rust

```rust
// เรียกใช้เครื่องมือเพิ่มด้วยอาร์กิวเมนต์ = {"a": 3, "b": 2}
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

### -5- การรันไคลเอนต์

เพื่อรันไคลเอนต์ ให้พิมพ์คำสั่งนี้ในเทอร์มินัล:

#### TypeScript

เพิ่มรายการนี้ในส่วน "scripts" ของ *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

เรียกไคลเอนต์โดยใช้คำสั่งดังนี้:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

ก่อนอื่น ให้แน่ใจว่า MCP server ของคุณกำลังรันที่ `http://localhost:8080` แล้วจึงรันไคลเอนต์:

```bash
# สร้างโปรเจกต์ของคุณ
./mvnw clean compile

# รันไคลเอนต์
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

หรือคุณสามารถรันโปรเจคไคลเอนต์ครบชุดในโฟลเดอร์ solution `03-GettingStarted\02-client\solution\java`:

```bash
# ไปยังไดเรกทอรีโซลูชัน
cd 03-GettingStarted/02-client/solution/java

# สร้างและรันไฟล์ JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## การบ้าน

ในการบ้านนี้ คุณจะใช้สิ่งที่เรียนรู้ในการสร้างไคลเอนต์ แต่ให้สร้างไคลเอนต์ของคุณเอง

นี่คือเซิร์ฟเวอร์ที่คุณสามารถใช้และเรียกผ่านโค้ดไคลเอนต์ของคุณ ลองเพิ่มฟีเจอร์เพิ่มเติมในเซิร์ฟเวอร์เพื่อทำให้มันน่าสนใจขึ้น

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

// เพิ่มแหล่งทรัพยากรทักทายแบบไดนามิก
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


# เพิ่มเครื่องมือบวก
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# เพิ่มทรัพยากรทักทายแบบไดนามิก
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

ดูโปรเจคนี้เพื่อดูวิธี [เพิ่มพรอมต์และทรัพยากร](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)

นอกจากนี้ดูลิงก์นี้เพื่อเรียนรู้วิธีเรียกใช้ [พรอมต์และทรัพยากร](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)

### Rust

ใน [ส่วนก่อนหน้า](../../../../03-GettingStarted/01-first-server) คุณได้เรียนรู้วิธีสร้าง MCP server แบบง่ายด้วย Rust คุณสามารถสร้างต่อจากนั้นได้ หรือดูลิงก์นี้สำหรับตัวอย่าง MCP server ที่ใช้ Rust เพิ่มเติม: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## โซลูชัน

**โฟลเดอร์โซลูชัน** ประกอบด้วยตัวอย่างไคลเอนต์ที่สมบูรณ์พร้อมรัน ซึ่งแสดงแนวคิดทั้งหมดที่สอนในบทเรียนนี้ โซลูชันแต่ละชุดประกอบด้วยโค้ดไคลเอนต์และเซิร์ฟเวอร์ที่จัดในโครงการแยกอิสระ

### 📁 โครงสร้างโซลูชัน

ไดเรกทอรีโซลูชันจัดเรียงตามภาษาโปรแกรม:

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

### 🚀 สิ่งที่โซลูชันแต่ละชุดรวมถึง

โซลูชันสำหรับแต่ละภาษาจะประกอบด้วย:

- **ไคลเอนต์ที่สมบูรณ์** ที่มีฟีเจอร์ทั้งหมดจากบทเรียน
- **โครงสร้างโปรเจคที่ใช้งานได้จริง** พร้อม dependencies และการกำหนดค่าที่เหมาะสม
- **สคริปต์การสร้างและรัน** เพื่อการตั้งค่าและใช้งานง่าย
- **README รายละเอียด** พร้อมคำแนะนำเฉพาะสำหรับแต่ละภาษา
- **ตัวอย่างการจัดการข้อผิดพลาด** และการประมวลผลผลลัพธ์

### 📖 การใช้โซลูชัน

1. **ไปที่โฟลเดอร์ภาษาที่คุณต้องการ**:

   ```bash
   cd solution/typescript/    # สำหรับ TypeScript
   cd solution/java/          # สำหรับ Java
   cd solution/python/        # สำหรับ Python
   cd solution/dotnet/        # สำหรับ .NET
   ```

2. **ปฏิบัติตามคำแนะนำใน README ของแต่ละโฟลเดอร์** สำหรับ:
   - การติดตั้ง dependencies
   - การสร้างโปรเจค
   - การรันไคลเอนต์

3. **ตัวอย่างเอาต์พุตที่คุณควรเห็น**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

สำหรับเอกสารฉบับสมบูรณ์และคำแนะนำแบบทีละขั้นตอน โปรดดูที่: **[📖 เอกสารโซลูชัน](./solution/README.md)**

## 🎯 ตัวอย่างสมบูรณ์

เราได้จัดเตรียมตัวอย่างไคลเอนต์ที่สมบูรณ์และใช้งานได้สำหรับทุกภาษาที่สอนในบทเรียนนี้ ตัวอย่างเหล่านี้แสดงฟังก์ชันการทำงานเต็มรูปแบบที่อธิบายไว้ข้างต้น และสามารถใช้เป็นตัวอย่างหรือจุดเริ่มต้นสำหรับโปรเจคของคุณเอง

### ตัวอย่างสมบูรณ์ที่มีให้

| ภาษา       | ไฟล์                             | รายละเอียด                                                   |
|------------|---------------------------------|-------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)       | ไคลเอนต์ Java สมบูรณ์โดยใช้ SSE transport พร้อมการจัดการข้อผิดพลาดครบถ้วน     |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)       | ไคลเอนต์ C# สมบูรณ์โดยใช้ stdio transport ที่เริ่มเซิร์ฟเวอร์โดยอัตโนมัติ           |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | ไคลเอนต์ TypeScript สมบูรณ์ที่รองรับโปรโตคอล MCP เต็มรูปแบบ              |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)       | ไคลเอนต์ Python สมบูรณ์ที่ใช้รูปแบบ async/await                      |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)           | ไคลเอนต์ Rust สมบูรณ์ที่ใช้ Tokio สำหรับงานแบบ async                  |

ตัวอย่างสมบูรณ์แต่ละชิ้นประกอบด้วย:
- ✅ **การสร้างการเชื่อมต่อ** และการจัดการข้อผิดพลาด  
- ✅ **การค้นหาเซิร์ฟเวอร์** (เครื่องมือ, แหล่งข้อมูล, คำสั่งแนะนำถ้ามี)  
- ✅ **การดำเนินการเครื่องคิดเลข** (บวก, ลบ, คูณ, หาร, ช่วยเหลือ)  
- ✅ **การประมวลผลผลลัพธ์** และการแสดงผลแบบฟอร์แมต  
- ✅ **การจัดการข้อผิดพลาดอย่างครอบคลุม**  
- ✅ **โค้ดสะอาดและมีเอกสารประกอบ** พร้อมคอมเมนต์ทีละขั้นตอน  

### เริ่มต้นด้วยตัวอย่างครบถ้วน  

1. **เลือกภาษาที่คุณต้องการ** จากตารางด้านบน  
2. **ตรวจสอบไฟล์ตัวอย่างครบถ้วน** เพื่อทำความเข้าใจการใช้งานทั้งหมด  
3. **รันตัวอย่าง** ตามคำแนะนำใน [`complete_examples.md`](./complete_examples.md)  
4. **แก้ไขและขยาย** ตัวอย่างให้เหมาะกับกรณีใช้งานของคุณ  

สำหรับเอกสารรายละเอียดเกี่ยวกับการรันและการปรับแต่งตัวอย่างเหล่านี้ ดูได้ที่: **[📖 เอกสารตัวอย่างครบถ้วน](./complete_examples.md)**  

### 💡 โซลูชัน vs ตัวอย่างครบถ้วน  

| **โฟลเดอร์โซลูชัน** | **ตัวอย่างครบถ้วน** |  
|--------------------|--------------------- |  
| โครงสร้างโปรเจกต์เต็มพร้อมไฟล์บิวด์ | การใช้งานแบบไฟล์เดี่ยว |  
| พร้อมใช้งานพร้อม dependencies | ตัวอย่างโค้ดเฉพาะส่วน |  
| การตั้งค่าแบบโปรดักชัน | อ้างอิงเพื่อการศึกษา |  
| เครื่องมือเฉพาะภาษา | การเปรียบเทียบหลายภาษา |  

ทั้งสองแบบมีคุณค่า - ใช้ **โฟลเดอร์โซลูชัน** สำหรับโปรเจกต์ครบถ้วน และ **ตัวอย่างครบถ้วน** สำหรับการเรียนรู้และอ้างอิง  

## ประเด็นสำคัญที่รับไป  

ประเด็นสำคัญของบทนี้เกี่ยวกับไคลเอนต์คือ:  

- สามารถใช้ทั้งค้นหาและเรียกใช้ฟีเจอร์บนเซิร์ฟเวอร์ได้  
- สามารถเริ่มเซิร์ฟเวอร์ในขณะที่ตัวเองเริ่มทำงาน (เหมือนในบทนี้) แต่ไคลเอนต์ยังสามารถเชื่อมต่อกับเซิร์ฟเวอร์ที่กำลังรันได้ด้วย  
- เป็นวิธีที่ดีในการทดสอบความสามารถของเซิร์ฟเวอร์เคียงข้างทางเลือกอื่น เช่น Inspector ตามที่อธิบายในบทก่อนหน้า  

## แหล่งข้อมูลเพิ่มเติม  

- [การสร้างไคลเอนต์ใน MCP](https://modelcontextprotocol.io/quickstart/client)  

## ตัวอย่าง  

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)  

## ต่อไปคือ  

- ถัดไป: [สร้างไคลเอนต์กับ LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วยปัญญาประดิษฐ์ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->