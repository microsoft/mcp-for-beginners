# การสร้างไคลเอนต์ด้วย LLM

จนถึงตอนนี้ คุณได้เห็นวิธีสร้างเซิร์ฟเวอร์และไคลเอนต์แล้ว ไคลเอนต์สามารถเรียกเซิร์ฟเวอร์โดยตรงเพื่อแสดงรายการเครื่องมือ ทรัพยากร และพรอมต์ อย่างไรก็ตาม นี่ไม่ใช่วิธีที่ใช้งานได้จริงมากนัก ผู้ใช้ของคุณอยู่ในยุคที่ใช้ตัวแทนและคาดหวังที่จะใช้พรอมต์และสื่อสารกับ LLM แทน พวกเขาไม่สนใจว่าคุณจะใช้ MCP เพื่อจัดเก็บความสามารถของคุณหรือไม่ พวกเขาเพียงแค่คาดหวังที่จะโต้ตอบโดยใช้ภาษาธรรมชาติ แล้วเราจะแก้ปัญหานี้ได้อย่างไร? วิธีแก้ไขคือเพิ่ม LLM ลงในไคลเอนต์

## ภาพรวม

ในบทเรียนนี้เราจะเน้นการเพิ่ม LLM ให้กับไคลเอนต์ของคุณและแสดงให้เห็นว่าสิ่งนี้ช่วยให้ประสบการณ์สำหรับผู้ใช้ของคุณดีขึ้นได้อย่างไร

## วัตถุประสงค์การเรียนรู้

เมื่อสิ้นสุดบทเรียนนี้ คุณจะสามารถ:

- สร้างไคลเอนต์พร้อม LLM
- โต้ตอบกับเซิร์ฟเวอร์ MCP อย่างลื่นไหลโดยใช้ LLM
- มอบประสบการณ์ผู้ใช้ปลายทางที่ดีขึ้นบนฝั่งไคลเอนต์

## วิธีการ

ลองทำความเข้าใจวิธีที่เราจำเป็นต้องทำ ขั้นตอนการเพิ่ม LLM ดูเหมือนง่าย แต่เราจะทำอย่างไรจริงๆ?

นี่คือวิธีที่ไคลเอนต์จะโต้ตอบกับเซิร์ฟเวอร์:

1. สร้างการเชื่อมต่อกับเซิร์ฟเวอร์

1. แสดงรายการความสามารถ, พรอมต์, ทรัพยากรและเครื่องมือ และบันทึกสคีมาเหล่านั้นไว้

1. เพิ่ม LLM และส่งผ่านความสามารถที่บันทึกไว้พร้อมกับสคีมาในรูปแบบที่ LLM เข้าใจ

1. จัดการพรอมต์ของผู้ใช้โดยส่งไปยัง LLM พร้อมกับรายการเครื่องมือที่ไคลเอนต์แสดง

ยอดเยี่ยม ตอนนี้เราเข้าใจระดับสูงว่าทำอย่างไร ลองมาทดลองทำในแบบฝึกหัดด้านล่างกัน

## แบบฝึกหัด: การสร้างไคลเอนต์ด้วย LLM

ในแบบฝึกหัดนี้ เราจะเรียนรู้การเพิ่ม LLM ลงในไคลเอนต์ของเรา

### การยืนยันตัวตนโดยใช้ GitHub Personal Access Token

การสร้างโทเค็น GitHub เป็นกระบวนการที่ตรงไปตรงมา นี่คือวิธีที่คุณสามารถทำได้:

- ไปที่ GitHub Settings – คลิกที่รูปโปรไฟล์ของคุณที่มุมบนขวาแล้วเลือก Settings
- ไปที่ Developer Settings – เลื่อนลงมาและคลิกที่ Developer Settings
- เลือก Personal Access Tokens – คลิกที่ Fine-grained tokens จากนั้นสร้างโทเค็นใหม่
- กำหนดค่าโทเค็นของคุณ – เพิ่มหมายเหตุสำหรับอ้างอิง, ตั้งค่าวันหมดอายุ, และเลือกขอบเขต (สิทธิ์) ที่จำเป็น ในกรณีนี้ให้แน่ใจว่าเพิ่มสิทธิ์ Models
- สร้างโทเค็นและคัดลอก – คลิก Generate token และแน่ใจว่าคัดลอกทันที เพราะคุณจะไม่สามารถดูได้อีกครั้ง

### -1- เชื่อมต่อกับเซิร์ฟเวอร์

สร้างไคลเอนต์ของเราก่อน:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // นำเข้า zod สำหรับตรวจสอบโครงสร้างข้อมูล

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", 
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }
}
```

ในโค้ดก่อนหน้านี้เราได้:

- นำเข้าสิ่งที่จำเป็นจากไลบรารี
- สร้างคลาสที่มีสมาชิกสองตัวคือ `client` และ `openai` เพื่อช่วยจัดการไคลเอนต์และโต้ตอบกับ LLM ตามลำดับ
- กำหนดค่าอินสแตนซ์ LLM ของเราให้ใช้ GitHub Models โดยตั้งค่า `baseUrl` ให้ชี้ไปยัง inference API

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# สร้างพารามิเตอร์เซิร์ฟเวอร์สำหรับการเชื่อมต่อ stdio
server_params = StdioServerParameters(
    command="mcp",  # ไฟล์ที่สามารถรันได้
    args=["run", "server.py"],  # อาร์กิวเมนต์แถวคำสั่งแบบเลือกได้
    env=None,  # ตัวแปรสภาพแวดล้อมแบบเลือกได้
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

ในโค้ดก่อนหน้านี้เราได้:

- นำเข้าสิ่งที่จำเป็นสำหรับ MCP
- สร้างไคลเอนต์

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

ก่อนอื่น คุณต้องเพิ่มไลบรารี LangChain4j ลงในไฟล์ `pom.xml` ของคุณ เพิ่มการพึ่งพาเหล่านี้เพื่อเปิดใช้งานการรวม MCP และการรองรับ GitHub Models:

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- LangChain4j MCP Integration -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-mcp</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- OpenAI Official API Client -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai-official</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- GitHub Models Support -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-github-models</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

จากนั้นสร้างคลาสไคลเอนต์ Java ของคุณ:

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // กำหนดค่า LLM ให้ใช้โมเดลของ GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // สร้าง MCP transport สำหรับเชื่อมต่อกับเซิร์ฟเวอร์
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // สร้าง MCP client
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

ในโค้ดก่อนหน้านี้เราได้:

- **เพิ่มการพึ่งพา LangChain4j**: จำเป็นสำหรับการรวม MCP, ไคลเอนต์ OpenAI อย่างเป็นทางการ และการรองรับ GitHub Models
- **นำเข้าไลบรารี LangChain4j**: สำหรับการรวม MCP และฟังก์ชันโมเดลแชทของ OpenAI
- **สร้าง `ChatLanguageModel`**: กำหนดใช้ GitHub Models ด้วยโทเค็น GitHub ของคุณ
- **ตั้งค่าการส่งผ่าน HTTP**: ใช้ Server-Sent Events (SSE) เพื่อเชื่อมต่อกับเซิร์ฟเวอร์ MCP
- **สร้างไคลเอนต์ MCP**: ซึ่งจะจัดการการสื่อสารกับเซิร์ฟเวอร์
- **ใช้การสนับสนุน MCP ในตัวของ LangChain4j**: ช่วยให้งานรวมกันระหว่าง LLMs และเซิร์ฟเวอร์ MCP ง่ายขึ้น

#### Rust

ตัวอย่างนี้สมมติว่าคุณมีเซิร์ฟเวอร์ MCP ที่เขียนด้วย Rust กำลังรันอยู่ ถ้าคุณยังไม่มี ให้กลับไปดูบทเรียน [01-first-server](../01-first-server/README.md) เพื่อสร้างเซิร์ฟเวอร์

เมื่อคุณมีเซิร์ฟเวอร์ Rust MCP แล้ว เปิดเทอร์มินัลแล้วไปที่ไดเรกทอรีเดียวกับเซิร์ฟเวอร์ จากนั้นรันคำสั่งต่อไปนี้เพื่อสร้างโปรเจ็กต์ไคลเอนต์ LLM ใหม่:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

เพิ่มการพึ่งพาต่อไปนี้ในไฟล์ `Cargo.toml` ของคุณ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> ยังไม่มีไลบรารี Rust อย่างเป็นทางการสำหรับ OpenAI แต่ `async-openai` crate คือ [ไลบรารีที่ชุมชนดูแล](https://platform.openai.com/docs/libraries/rust#rust) ที่ถูกใช้งานเป็นที่นิยม

เปิดไฟล์ `src/main.rs` แล้วแทนที่เนื้อหาด้วยโค้ดต่อไปนี้:

```rust
use async_openai::{Client, config::OpenAIConfig};
use rmcp::{
    RmcpError,
    model::{CallToolRequestParam, ListToolsResult},
    service::{RoleClient, RunningService, ServiceExt},
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use serde_json::{Value, json};
use std::error::Error;
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // ข้อความเริ่มต้น
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // ตั้งค่าไคลเอนต์ OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // ตั้งค่าไคลเอนต์ MCP
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("calculator-server");

    let mcp_client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // สิ่งที่ต้องทำ: รับรายการเครื่องมือ MCP

    // สิ่งที่ต้องทำ: การสนทนา LLM พร้อมการเรียกใช้เครื่องมือ

    Ok(())
}
```

โค้ดนี้ตั้งค่าแอปพลิเคชัน Rust ขั้นพื้นฐานที่เชื่อมต่อกับเซิร์ฟเวอร์ MCP และ GitHub Models เพื่อโต้ตอบกับ LLM

> [!IMPORTANT]
> โปรดตรวจสอบให้แน่ใจว่ากำหนดตัวแปรสภาพแวดล้อม `OPENAI_API_KEY` ด้วยโทเค็น GitHub ของคุณก่อนรันแอปพลิเคชัน

ดีแล้ว สำหรับขั้นตอนถัดไป เราจะดูรายการความสามารถในเซิร์ฟเวอร์

### -2- แสดงรายการความสามารถของเซิร์ฟเวอร์

ตอนนี้เราจะเชื่อมต่อกับเซิร์ฟเวอร์และขอข้อมูลความสามารถ:

#### Typescript

ในคลาสเดียวกัน เพิ่มเมทอดต่อไปนี้:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // รายการเครื่องมือ
    const toolsResult = await this.client.listTools();
}
```

ในโค้ดก่อนหน้านี้เราได้:

- เพิ่มโค้ดสำหรับการเชื่อมต่อกับเซิร์ฟเวอร์ `connectToServer`
- สร้างเมทอด `run` เพื่อจัดการลำดับการทำงานของแอป ตอนนี้ยังแค่แสดงรายการเครื่องมือ แต่ว่าจะเพิ่มมากขึ้นในเร็วๆ นี้

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
    print("Tool", tool.inputSchema["properties"])
```

นี่คือสิ่งที่เราเพิ่ม:

- แสดงรายการทรัพยากรและเครื่องมือและพิมพ์ออกมา สำหรับเครื่องมือนั้นเรายังแสดง `inputSchema` ที่จะใช้ในภายหลัง

#### .NET

```csharp
async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        // TODO: convert tool definition from MCP tool to LLm tool     
    }

    return toolDefinitions;
}
```

ในโค้ดก่อนหน้านี้เราได้:

- แสดงรายการเครื่องมือที่มีในเซิร์ฟเวอร์ MCP
- สำหรับแต่ละเครื่องมือ แสดงชื่อ คำอธิบาย และสคีมา เราจะใช้สคีมาเรียกเครื่องมือในไม่ช้า

#### Java

```java
// สร้างผู้ให้บริการเครื่องมือที่ค้นหาเครื่องมือ MCP โดยอัตโนมัติ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ผู้ให้บริการเครื่องมือ MCP จัดการโดยอัตโนมัติ:
// - แสดงรายการเครื่องมือที่มีจากเซิร์ฟเวอร์ MCP
// - แปลงสคีมาของเครื่องมือ MCP เป็นรูปแบบ LangChain4j
// - จัดการการเรียกใช้งานเครื่องมือและการตอบสนอง
```

ในโค้ดก่อนหน้านี้เราได้:

- สร้าง `McpToolProvider` ที่ค้นหาและลงทะเบียนเครื่องมือทั้งหมดจากเซิร์ฟเวอร์ MCP อัตโนมัติ
- ผู้ให้บริการเครื่องมือจัดการแปลงสคีมาเครื่องมือ MCP เป็นรูปแบบของ LangChain4j ภายใน
- วิธีนี้ช่วยปกปิดกระบวนการแปลงและแสดงรายการเครื่องมือด้วยตนเอง

#### Rust

การดึงเครื่องมือจากเซิร์ฟเวอร์ MCP ทำได้โดยใช้เมทอด `list_tools` ในฟังก์ชัน `main` ของคุณ หลังจากตั้งค่าไคลเอนต์ MCP แล้ว ให้เพิ่มโค้ดต่อไปนี้:

```rust
// รับรายชื่อเครื่องมือ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- แปลงความสามารถของเซิร์ฟเวอร์เป็นเครื่องมือ LLM

ขั้นตอนถัดไปหลังจากแสดงรายการความสามารถของเซิร์ฟเวอร์คือการแปลงให้เป็นรูปแบบที่ LLM เข้าใจได้ เมื่อแปลงเสร็จแล้ว เราสามารถมอบความสามารถเหล่านี้เป็นเครื่องมือให้กับ LLM ได้

#### TypeScript

1. เพิ่มโค้ดต่อไปนี้เพื่อแปลงการตอบสนองจาก MCP Server เป็นรูปแบบเครื่องมือที่ LLM ใช้ได้:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // สร้างสคีมา zod ตาม input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // กำหนดชนิดเป็น "function" อย่างชัดเจน
            function: {
            name: tool.name,
            description: tool.description,
            parameters: {
            type: "object",
            properties: tool.input_schema.properties,
            required: tool.input_schema.required,
            },
            },
        };
    }

    ```

    โค้ดข้างต้นรับการตอบสนองจาก MCP Server และแปลงเป็นรูปแบบการกำหนดเครื่องมือที่ LLM เข้าใจ

1. อัปเดตเมทอด `run` ต่อไปเพื่อแสดงรายการความสามารถของเซิร์ฟเวอร์:

    ```typescript
    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
            });
        });
    }
    ```

    ในโค้ดข้างต้น เราอัปเดตเมทอด `run` ให้แปลงผลลัพธ์และสำหรับแต่ละรายการเรียก `openAiToolAdapter`

#### Python

1. เริ่มด้วยการสร้างฟังก์ชันแปลงดังต่อไปนี้

    ```python
    def convert_to_llm_tool(tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }

        return tool_schema
    ```

    ในฟังก์ชัน `convert_to_llm_tools` เรารับการตอบสนองจาก MCP tool และแปลงเป็นรูปแบบที่ LLM เข้าใจได้

1. ต่อไป อัปเดตโค้ดไคลเอนต์ของเราให้ใช้ฟังก์ชันนี้ดังนี้:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ที่นี่เราเพิ่มการเรียก `convert_to_llm_tool` เพื่อแปลงการตอบสนองเครื่องมือ MCP เป็นข้อมูลที่เราจะส่งให้ LLM ในภายหลัง

#### .NET

1. เพิ่มโค้ดเพื่อแปลงการตอบสนองเครื่องมือ MCP เป็นรูปแบบที่ LLM เข้าใจ

```csharp
ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}
```

ในโค้ดก่อนหน้านี้เราได้:

- สร้างฟังก์ชัน `ConvertFrom` ที่รับชื่อ คำอธิบาย และสคีมาอินพุต
- กำหนดฟังก์ชันที่สร้าง `FunctionDefinition` ซึ่งถูกส่งต่อให้กับ `ChatCompletionsDefinition` ซึ่ง LLM เข้าใจได้

1. มาดูวิธีอัปเดตโค้ดที่มีอยู่ให้ใช้ฟังก์ชันนี้:

    ```csharp
    async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            JsonElement propertiesElement;
            tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

            var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);

            Console.WriteLine($"Properties: {propertiesElement}");        
        }

        return toolDefinitions;
    }
    ```    In the preceding code, we've:

    - Update the function to convert the MCP tool response to an LLm tool. Let's highlight the code we added:

        ```csharp
        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
        ```

        The input schema is part of the tool response but on the "properties" attribute, so we need to extract. Furthermore, we now call `ConvertFrom` with the tool details. Now we've done the heavy lifting, let's see how it call comes together as we handle a user prompt next.

#### Java

```java
// สร้างอินเทอร์เฟซบอทสำหรับการโต้ตอบด้วยภาษาธรรมชาติ
public interface Bot {
    String chat(String prompt);
}

// กำหนดค่าบริการ AI ด้วยเครื่องมือ LLM และ MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ในโค้ดก่อนหน้านี้เราได้:

- กำหนดอินเทอร์เฟซ `Bot` แบบง่ายสำหรับการโต้ตอบด้วยภาษาธรรมชาติ
- ใช้ `AiServices` ของ LangChain4j เพื่อเชื่อมโยง LLM กับ MCP tool provider โดยอัตโนมัติ
- เฟรมเวิร์กจัดการการแปลงสคีมาของเครื่องมือและเรียกฟังก์ชันเบื้องหลังโดยอัตโนมัติ
- วิธีนี้ช่วยลดความยุ่งยากในการแปลงเครื่องมือด้วยตนเอง เพราะ LangChain4j รับผิดชอบการแปลง MCP tools ให้เข้ากับรูปแบบที่ LLM รองรับทั้งหมด

#### Rust

เพื่อแปลงการตอบสนองเครื่องมือ MCP เป็นรูปแบบที่ LLM เข้าใจ เราจะเพิ่มฟังก์ชันช่วยที่จัดรูปแบบรายการเครื่องมือ เพิ่มโค้ดนี้ในไฟล์ `main.rs` ของคุณด้านล่างฟังก์ชัน `main` ซึ่งจะถูกเรียกเมื่อส่งคำขอถึง LLM:

```rust
async fn format_tools(tools: &ListToolsResult) -> Result<Vec<Value>, Box<dyn Error>> {
    let tools_json = serde_json::to_value(tools)?;
    let Some(tools_array) = tools_json.get("tools").and_then(|t| t.as_array()) else {
        return Ok(vec![]);
    };

    let formatted_tools = tools_array
        .iter()
        .filter_map(|tool| {
            let name = tool.get("name")?.as_str()?;
            let description = tool.get("description")?.as_str()?;
            let schema = tool.get("inputSchema")?;

            Some(json!({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": schema.get("properties").unwrap_or(&json!({})),
                        "required": schema.get("required").unwrap_or(&json!([]))
                    }
                }
            }))
        })
        .collect();

    Ok(formatted_tools)
}
```

เยี่ยม เรายังไม่ได้ตั้งค่าจัดการคำขอของผู้ใช้ ดังนั้นให้ทำส่วนนี้ต่อไป

### -4- จัดการคำขอพรอมต์จากผู้ใช้

ในส่วนของโค้ดนี้ เราจะจัดการคำขอจากผู้ใช้

#### TypeScript

1. เพิ่มเมทอดที่จะใช้เรียก LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. เรียกใช้เครื่องมือของเซิร์ฟเวอร์
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ทำบางอย่างกับผลลัพธ์
        // TODO

        }
    }
    ```

    ในโค้ดก่อนหน้านี้เรา:

    - เพิ่มเมทอด `callTools`
    - เมทอดนี้รับการตอบสนองจาก LLM และตรวจสอบว่าเรียกเครื่องมือใดบ้างหรือไม่:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // เรียกใช้เครื่องมือ
        }
        ```

    - เรียกเครื่องมือ หาก LLM แสดงว่าควรเรียก:

        ```typescript
        // 2. เรียกใช้เครื่องมือของเซิร์ฟเวอร์
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ทำบางอย่างกับผลลัพธ์
        // งานที่ต้องทำ
        ```

1. อัปเดตเมทอด `run` เพื่อรวมการเรียก LLM และเรียก `callTools` ดังนี้:

    ```typescript

    // 1. สร้างข้อความที่เป็นอินพุตสำหรับ LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. เรียกใช้ LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. ตรวจสอบการตอบกลับของ LLM สำหรับแต่ละตัวเลือก ว่ามีการเรียกใช้เครื่องมือหรือไม่
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

เยี่ยม แสดงโค้ดทั้งหมด:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // นำเข้า zod สำหรับการตรวจสอบโครงสร้างข้อมูล

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // อาจต้องเปลี่ยนเป็น URL นี้ในอนาคต: https://models.github.ai/inference
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }

    async connectToServer(transport: Transport) {
        await this.client.connect(transport);
        this.run();
        console.error("MCPClient started on stdin/stdout");
    }

    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
          }) {
          // สร้างโครงสร้างข้อมูล zod โดยอิงจาก input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // กำหนดชนิดเป็น "function" อย่างชัดเจน
            function: {
              name: tool.name,
              description: tool.description,
              parameters: {
              type: "object",
              properties: tool.input_schema.properties,
              required: tool.input_schema.required,
              },
            },
          };
    }
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. เรียกใช้เครื่องมือของเซิร์ฟเวอร์
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ทำบางอย่างกับผลลัพธ์
          // สิ่งที่ต้องทำ
    
         }
    }

    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
              name: tool.name,
              description: tool.description,
              input_schema: tool.inputSchema,
            });
        });

        const prompt = "What is the sum of 2 and 3?";
    
        const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

        console.log("Querying LLM: ", messages[0].content);
        let response = this.openai.chat.completions.create({
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. ตรวจสอบการตอบกลับของ LLM สำหรับแต่ละตัวเลือก ตรวจสอบว่ามีการเรียกใช้เครื่องมือหรือไม่
        (await response).choices.map(async (choice: { message: any; }) => {
          const message = choice.message;
          if (message.tool_calls) {
              console.log("Making tool call")
              await this.callTools(message.tool_calls, results);
          }
        });
    }
    
}

let client = new MyClient();
 const transport = new StdioClientTransport({
            command: "node",
            args: ["./build/index.js"]
        });

client.connectToServer(transport);
```

#### Python

1. เพิ่มการนำเข้าที่จำเป็นสำหรับเรียก LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. ถัดไปเพิ่มฟังก์ชันที่เรียก LLM:

    ```python
    # llm

    def call_llm(prompt, functions):
        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.inference.ai.azure.com"

        model_name = "gpt-4o"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        print("CALLING LLM")
        response = client.complete(
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant.",
                },
                {
                "role": "user",
                "content": prompt,
                },
            ],
            model=model_name,
            tools = functions,
            # พารามิเตอร์เสริม
            temperature=1.,
            max_tokens=1000,
            top_p=1.    
        )

        response_message = response.choices[0].message
        
        functions_to_call = []

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                print("TOOL: ", tool_call)
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                functions_to_call.append({ "name": name, "args": args })

        return functions_to_call
    ```

    ในโค้ดก่อนหน้านี้เราได้:

    - ส่งผ่านฟังก์ชันที่เราได้มาจากเซิร์ฟเวอร์ MCP และแปลงให้ LLM
    - จากนั้นเรียก LLM พร้อมกับฟังก์ชันเหล่านั้น
    - ตรวจสอบผลลัพธ์ว่าเราควรเรียกฟังก์ชันใดบ้างหรือไม่
    - ส่งต่ออาร์เรย์ฟังก์ชันที่จะเรียก

1. ขั้นตอนสุดท้าย อัปเดตโค้ดหลักของเรา:

    ```python
    prompt = "Add 2 to 20"

    # ถาม LLM ว่าจะใช้เครื่องมืออะไรบ้าง ถ้ามี
    functions_to_call = call_llm(prompt, functions)

    # เรียกใช้ฟังก์ชันที่แนะนำ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    นี่คือขั้นตอนสุดท้าย ในโค้ดข้างต้นเรา:

    - เรียกเครื่องมือ MCP ผ่าน `call_tool` โดยใช้ฟังก์ชันที่ LLM ตัดสินใจว่าจะเรียกตามพรอมต์ของเรา
    - พิมพ์ผลลัพธ์ของการเรียกเครื่องมือที่ส่งไปยัง MCP Server

#### .NET

1. แสดงโค้ดตัวอย่างการใช้งานพรอมต์ LLM:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new ChatRequestUserMessage(userMessage));

    // 1. Define tools
    ChatCompletionsToolDefinition def = CreateToolDefinition();


    // 2. Define options, including the tools
    var options = new ChatCompletionsOptions(chatHistory)
    {
        Model = "gpt-4.1-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    ในโค้ดก่อนหน้านี้เราได้:

    - ดึงเครื่องมือจากเซิร์ฟเวอร์ MCP ด้วย `var tools = await GetMcpTools()`
    - กำหนดพรอมต์ผู้ใช้ `userMessage`
    - สร้างอ็อปชันที่ระบุโมเดลและเครื่องมือ
    - ส่งคำขอไปยัง LLM

1. ขั้นตอนสุดท้าย ตรวจสอบว่า LLM คิดว่าเราควรเรียกฟังก์ชันหรือไม่:

    ```csharp
    // 4. Check if the response contains a function call
    ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
        var result = await mcpClient.CallToolAsync(
            call.Name,
            dict!,
            cancellationToken: CancellationToken.None
        );

        Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

    }
    ```

    ในโค้ดก่อนหน้านี้เราได้:

    - วนลูปผ่านรายการการเรียกฟังก์ชัน
    - สำหรับแต่ละการเรียกเครื่องมือ แยกชื่อและอาร์กิวเมนต์ จากนั้นเรียกเครื่องมือบนเซิร์ฟเวอร์ MCP ผ่านไคลเอนต์ MCP สุดท้ายพิมพ์ผลลัพธ์ออกมา

นี่คือโค้ดทั้งหมด:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;

var endpoint = "https://models.inference.ai.azure.com";
var token = Environment.GetEnvironmentVariable("GITHUB_TOKEN"); // Your GitHub Access Token
var client = new ChatCompletionsClient(new Uri(endpoint), new AzureKeyCredential(token));
var chatHistory = new List<ChatRequestMessage>
{
    new ChatRequestSystemMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}



async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);

        Console.WriteLine($"Properties: {propertiesElement}");        
    }

    return toolDefinitions;
}

// 1. List tools on mcp server

var tools = await GetMcpTools();
for (int i = 0; i < tools.Count; i++)
{
    var tool = tools[i];
    Console.WriteLine($"MCP Tools def: {i}: {tool}");
}

// 2. Define the chat history and the user message
var userMessage = "add 2 and 4";

chatHistory.Add(new ChatRequestUserMessage(userMessage));


// 3. Define options, including the tools
var options = new ChatCompletionsOptions(chatHistory)
{
    Model = "gpt-4.1-mini",
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletions? response = await client.CompleteAsync(options);
var content = response.Content;

// 5. Check if the response contains a function call
ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
    var result = await mcpClient.CallToolAsync(
        call.Name,
        dict!,
        cancellationToken: CancellationToken.None
    );

    Console.WriteLine(result.Content.OfType<TextContentBlock>().First().Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // ดำเนินการคำขอภาษาธรรมชาติที่ใช้เครื่องมือ MCP อัตโนมัติ
    String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
    System.out.println(response);

    response = bot.chat("What's the square root of 144?");
    System.out.println(response);

    response = bot.chat("Show me the help for the calculator service");
    System.out.println(response);
} finally {
    mcpClient.close();
}
```

ในโค้ดก่อนหน้านี้เราได้:

- ใช้พรอมต์ภาษาธรรมชาติแบบง่ายในการโต้ตอบกับเครื่องมือเซิร์ฟเวอร์ MCP
- เฟรมเวิร์ก LangChain4j จัดการโดยอัตโนมัติ:
  - แปลงพรอมต์ผู้ใช้เป็นการเรียกเครื่องมือเมื่อจำเป็น
  - เรียกเครื่องมือ MCP ที่เหมาะสมตามการตัดสินใจของ LLM
  - จัดการลำดับการสนทนาระหว่าง LLM กับเซิร์ฟเวอร์ MCP
- เมทอด `bot.chat()` คืนคำตอบเป็นภาษาธรรมชาติที่อาจรวมผลลัพธ์จากการใช้งานเครื่องมือ MCP
- วิธีนี้มอบประสบการณ์ผู้ใช้ที่ลื่นไหลโดยที่ผู้ใช้ไม่จำเป็นต้องทราบการดำเนินการเบื้องหลังของ MCP

ตัวอย่างโค้ดสมบูรณ์:

```java
public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofSeconds(60))
                .build();

        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        Bot bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();

        try {
            String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
            System.out.println(response);

            response = bot.chat("What's the square root of 144?");
            System.out.println(response);

            response = bot.chat("Show me the help for the calculator service");
            System.out.println(response);
        } finally {
            mcpClient.close();
        }
    }
}
```

#### Rust

นี่คือส่วนที่งานหลักเกิดขึ้น เราจะเรียก LLM ด้วยพรอมต์ผู้ใช้เบื้องต้น จากนั้นประมวลผลคำตอบเพื่อตรวจสอบว่าจำเป็นต้องเรียกเครื่องมือใดหรือไม่ หากใช่ เราจะเรียกเครื่องมือเหล่านั้นและดำเนินการสนทนาต่อกับ LLM จนกว่าจะไม่มีคำขอเรียกเครื่องมืออีก และเราได้รับคำตอบสุดท้าย

เราจะเรียก LLM หลายครั้ง ดังนั้นให้กำหนดฟังก์ชันที่จะจัดการการเรียก LLM เพิ่มโค้ดนี้ในไฟล์ `main.rs` ของคุณ:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": "openai/gpt-4.1",
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

ฟังก์ชันนี้รับไคลเอนต์ LLM, รายการข้อความ (รวมพรอมต์ผู้ใช้), เครื่องมือจากเซิร์ฟเวอร์ MCP แล้วส่งคำขอไปยัง LLM พร้อมทั้งคืนคำตอบกลับมา
คำตอบจาก LLM จะประกอบด้วยอาร์เรย์ของ `choices` เราจะต้องประมวลผลผลลัพธ์เพื่อตรวจสอบว่ามี `tool_calls` อยู่หรือไม่ สิ่งนี้ช่วยให้เรารู้ว่า LLM กำลังร้องขอให้เรียกใช้เครื่องมือเฉพาะด้วยอาร์กิวเมนต์ เพิ่มโค้ดต่อไปนี้ที่ส่วนล่างของไฟล์ `main.rs` ของคุณเพื่อกำหนดฟังก์ชันสำหรับจัดการกับการตอบกลับของ LLM:

```rust
async fn process_llm_response(
    llm_response: &Value,
    mcp_client: &RunningService<RoleClient, ()>,
    openai_client: &Client<OpenAIConfig>,
    mcp_tools: &ListToolsResult,
    messages: &mut Vec<Value>,
) -> Result<(), Box<dyn Error>> {
    let Some(message) = llm_response
        .get("choices")
        .and_then(|c| c.as_array())
        .and_then(|choices| choices.first())
        .and_then(|choice| choice.get("message"))
    else {
        return Ok(());
    };

    // พิมพ์เนื้อหาหากมี
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // จัดการการเรียกใช้เครื่องมือ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // เพิ่มข้อความผู้ช่วย

        // ดำเนินการเรียกใช้เครื่องมือแต่ละรายการ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // เพิ่มผลลัพธ์ของเครื่องมือไปยังข้อความ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ดำเนินการสนทนาต่อด้วยผลลัพธ์ของเครื่องมือ
        let response = call_llm(openai_client, messages, mcp_tools).await?;
        Box::pin(process_llm_response(
            &response,
            mcp_client,
            openai_client,
            mcp_tools,
            messages,
        ))
        .await?;
    }
    Ok(())
}
```
  
ถ้ามี `tool_calls` จะทำการดึงข้อมูลเครื่องมือ, เรียกเซิร์ฟเวอร์ MCP ด้วยคำขอเครื่องมือ และเพิ่มผลลัพธ์ลงในข้อความของการสนทนา จากนั้นจะดำเนินการสนทนาต่อกับ LLM และข้อความจะได้รับการอัปเดตด้วยการตอบกลับของผู้ช่วยและผลลัพธ์การเรียกใช้เครื่องมือ

เพื่อดึงข้อมูลการเรียกใช้เครื่องมือที่ LLM ส่งกลับสำหรับการเรียก MCP เราจะเพิ่มฟังก์ชันช่วยเหลืออีกตัวหนึ่งเพื่อดึงทุกอย่างที่จำเป็นสำหรับการเรียก ใช้โค้ดต่อไปนี้ที่ส่วนล่างของไฟล์ `main.rs` ของคุณ:

```rust
fn extract_tool_call_info(tool_call: &Value) -> Result<(String, String, String), Box<dyn Error>> {
    let tool_id = tool_call
        .get("id")
        .and_then(|id| id.as_str())
        .unwrap_or("")
        .to_string();
    let function = tool_call.get("function").ok_or("Missing function")?;
    let name = function
        .get("name")
        .and_then(|n| n.as_str())
        .unwrap_or("")
        .to_string();
    let args = function
        .get("arguments")
        .and_then(|a| a.as_str())
        .unwrap_or("{}")
        .to_string();
    Ok((tool_id, name, args))
}
```
  
ด้วยทุกส่วนพร้อมแล้ว เราสามารถจัดการกับคำร้องเริ่มต้นของผู้ใช้และเรียกใช้ LLM ได้ อัปเดตฟังก์ชัน `main` ของคุณให้รวมโค้ดต่อไปนี้:

```rust
// การสนทนา LLM พร้อมการเรียกเครื่องมือ
let response = call_llm(&openai_client, &messages, &tools).await?;
process_llm_response(
    &response,
    &mcp_client,
    &openai_client,
    &tools,
    &mut messages,
)
.await?;
```
  
สิ่งนี้จะส่งคำถามไปยัง LLM ด้วยคำร้องเริ่มต้นของผู้ใช้ที่ถามหาผลบวกของตัวเลขสองตัว และจะประมวลผลการตอบกลับเพื่อจัดการการเรียกใช้เครื่องมือแบบไดนามิก

เยี่ยมมาก คุณทำได้!

## การบ้าน

นำโค้ดจากแบบฝึกหัดไปสร้างเซิร์ฟเวอร์ที่มีเครื่องมือเพิ่มขึ้น จากนั้นสร้างไคลเอนต์ที่ใช้ LLM เหมือนในแบบฝึกหัด และทดสอบด้วยคำร้องต่าง ๆ เพื่อให้แน่ใจว่าเครื่องมือในเซิร์ฟเวอร์ของคุณถูกเรียกใช้แบบไดนามิก วิธีการสร้างไคลเอนต์แบบนี้หมายความว่าผู้ใช้ปลายทางจะได้รับประสบการณ์ผู้ใช้ที่ยอดเยี่ยม เพราะพวกเขาสามารถใช้คำร้องแทนคำสั่งไคลเอนต์ที่ชัดเจน และไม่รู้ตัวว่าเซิร์ฟเวอร์ MCP ใดถูกเรียกใช้

## วิธีแก้ปัญหา

[วิธีแก้ปัญหา](./solution/README.md)

## ประเด็นสำคัญ

- การเพิ่ม LLM ลงในไคลเอนต์ของคุณช่วยให้ผู้ใช้มีวิธีที่ดีขึ้นในการโต้ตอบกับ MCP Servers  
- คุณต้องแปลงผลลัพธ์จาก MCP Server ให้เป็นสิ่งที่ LLM เข้าใจได้

## ตัวอย่าง

- [เครื่องคิดเลข Java](../samples/java/calculator/README.md)  
- [เครื่องคิดเลข .Net](../../../../03-GettingStarted/samples/csharp)  
- [เครื่องคิดเลข JavaScript](../samples/javascript/README.md)  
- [เครื่องคิดเลข TypeScript](../samples/typescript/README.md)  
- [เครื่องคิดเลข Python](../../../../03-GettingStarted/samples/python)  
- [เครื่องคิดเลข Rust](../../../../03-GettingStarted/samples/rust)

## แหล่งข้อมูลเพิ่มเติม

## สิ่งที่ต่อไป

- ถัดไป: [การใช้งานเซิร์ฟเวอร์ผ่าน Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามอย่างดีที่สุดเพื่อความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นฉบับควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->