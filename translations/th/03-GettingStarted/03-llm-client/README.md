# การสร้างไคลเอนต์ด้วย LLM

จนถึงตอนนี้ คุณได้เห็นวิธีการสร้างเซิร์ฟเวอร์และไคลเอนต์ ไคลเอนต์สามารถเรียกเซิร์ฟเวอร์โดยตรงเพื่อแสดงรายการเครื่องมือ ทรัพยากร และพรอมต์ อย่างไรก็ตาม นี่ไม่ใช่วิธีที่ใช้งานได้จริงมากนัก ผู้ใช้ของคุณอยู่ในยุคของเอเจนต์และคาดหวังที่จะใช้พรอมต์และสื่อสารกับ LLM เพื่อทำเช่นนั้น สำหรับผู้ใช้ของคุณ พวกเขาไม่สนใจว่าคุณจะใช้ MCP หรือไม่ในการจัดเก็บความสามารถของคุณ แต่พวกเขาคาดหวังที่จะใช้ภาษาธรรมชาติในการโต้ตอบ แล้วเราจะแก้ปัญหานี้อย่างไร? วิธีแก้คือการเพิ่ม LLM ลงในไคลเอนต์

## ภาพรวม

ในบทเรียนนี้ เราจะเน้นการเพิ่ม LLM เพื่อทำงานกับไคลเอนต์ของคุณและแสดงให้เห็นว่าสิ่งนี้ช่วยให้ประสบการณ์ของผู้ใช้ดีขึ้นอย่างไร

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- สร้างไคลเอนต์ที่มี LLM
- โต้ตอบกับเซิร์ฟเวอร์ MCP อย่างราบรื่นโดยใช้ LLM
- มอบประสบการณ์ผู้ใช้ที่ดีกว่าฝั่งไคลเอนต์

## วิธีการ

ลองทำความเข้าใจวิธีการที่เราต้องทำ การเพิ่ม LLM ดูเหมือนง่าย แต่เราจะทำจริงหรือไม่?

นี่คือวิธีที่ไคลเอนต์จะโต้ตอบกับเซิร์ฟเวอร์:

1. สร้างการเชื่อมต่อกับเซิร์ฟเวอร์

1. แสดงรายการความสามารถ, พรอมต์, ทรัพยากร และเครื่องมือ และบันทึกสคีมาของพวกมัน

1. เพิ่ม LLM และส่งความสามารถที่บันทึกไว้พร้อมสคีมาในรูปแบบที่ LLM เข้าใจ

1. จัดการพรอมต์ของผู้ใช้โดยส่งต่อไปยัง LLM พร้อมกับเครื่องมือที่ไคลเอนต์แสดงรายการ

ดีมาก ตอนนี้เราเข้าใจวิธีการทำงานในระดับสูงแล้ว ลองทำในแบบฝึกหัดด้านล่างกัน

## แบบฝึกหัด: การสร้างไคลเอนต์ด้วย LLM

ในแบบฝึกหัดนี้ เราจะเรียนรู้การเพิ่ม LLM ลงในไคลเอนต์ของเรา

### การรับรองความถูกต้องโดยใช้ GitHub Personal Access Token

การสร้างโทเค็น GitHub เป็นกระบวนการที่ตรงไปตรงมา นี่คือวิธีที่คุณทำได้:

- ไปที่การตั้งค่า GitHub – คลิกที่รูปโปรไฟล์ของคุณที่มุมขวาบนแล้วเลือก Settings
- ไปที่ Developer Settings – เลื่อนลงและคลิกที่ Developer Settings
- เลือก Personal Access Tokens – คลิกที่ Fine-grained tokens แล้วเลือก Generate new token
- กำหนดค่าโทเค็นของคุณ – เพิ่มหมายเหตุสำหรับอ้างอิง กำหนดวันหมดอายุ และเลือกขอบเขตที่จำเป็น (สิทธิ์) ในกรณีนี้ให้แน่ใจว่าได้เพิ่มสิทธิ์ Models
- สร้างและคัดลอกโทเค็น – คลิก Generate token และอย่าลืมคัดลอกทันที เพราะคุณจะไม่สามารถเห็นมันอีก

### -1- เชื่อมต่อกับเซิร์ฟเวอร์

มาสร้างไคลเอนต์ของเรากันก่อน:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // นำเข้า zod สำหรับการตรวจสอบสคีมา

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

ในโค้ดก่อนหน้านี้ เราได้:

- นำเข้าห้องสมุดที่จำเป็น
- สร้างคลาสที่มีสมาชิกสองตัว คือ `client` และ `openai` ซึ่งจะช่วยจัดการไคลเอนต์และโต้ตอบกับ LLM ตามลำดับ
- กำหนดค่าอินสแตนซ์ LLM ของเราให้ใช้ GitHub Models โดยตั้งค่า `baseUrl` ให้ชี้ไปที่ inference API

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# สร้างพารามิเตอร์เซิร์ฟเวอร์สำหรับการเชื่อมต่อ stdio
server_params = StdioServerParameters(
    command="mcp",  # ไฟล์ที่สามารถรันได้
    args=["run", "server.py"],  # อาร์กิวเมนต์บรรทัดคำสั่งที่เป็นทางเลือก
    env=None,  # ตัวแปรสภาพแวดล้อมที่เป็นทางเลือก
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

ในโค้ดก่อนหน้านี้ เราได้:

- นำเข้าห้องสมุดที่จำเป็นสำหรับ MCP
- สร้างไคลเอนต์

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

ก่อนอื่น คุณต้องเพิ่ม dependencies ของ LangChain4j ลงในไฟล์ `pom.xml` ของคุณ เพิ่ม dependencies เหล่านี้เพื่อเปิดใช้งานการรวม MCP และสนับสนุน GitHub Models:

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
    
    public static void main(String[] args) throws Exception {        // กำหนดค่า LLM ให้ใช้โมเดล GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // สร้างการขนส่ง MCP สำหรับเชื่อมต่อกับเซิร์ฟเวอร์
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // สร้างไคลเอนต์ MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

ในโค้ดก่อนหน้านี้ เราได้:

- **เพิ่ม dependencies ของ LangChain4j**: จำเป็นสำหรับการรวม MCP, ไคลเอนต์ OpenAI อย่างเป็นทางการ และสนับสนุน GitHub Models
- **นำเข้าห้องสมุด LangChain4j**: สำหรับการรวม MCP และฟังก์ชันโมเดลแชท OpenAI
- **สร้าง `ChatLanguageModel`**: กำหนดค่าให้ใช้ GitHub Models พร้อมโทเค็น GitHub ของคุณ
- **ตั้งค่าการขนส่ง HTTP**: ใช้ Server-Sent Events (SSE) เพื่อเชื่อมต่อกับเซิร์ฟเวอร์ MCP
- **สร้างไคลเอนต์ MCP**: ที่จะจัดการการสื่อสารกับเซิร์ฟเวอร์
- **ใช้การสนับสนุน MCP ในตัวของ LangChain4j**: ซึ่งช่วยให้ง่ายต่อการรวมระหว่าง LLM และเซิร์ฟเวอร์ MCP

#### Rust

ตัวอย่างนี้สมมติว่าคุณมีเซิร์ฟเวอร์ MCP ที่เขียนด้วย Rust กำลังทำงานอยู่ หากคุณยังไม่มี ให้ย้อนกลับไปที่บทเรียน [01-first-server](../01-first-server/README.md) เพื่อสร้างเซิร์ฟเวอร์

เมื่อคุณมีเซิร์ฟเวอร์ MCP Rust แล้ว เปิดเทอร์มินัลและไปยังไดเรกทอรีเดียวกับเซิร์ฟเวอร์ จากนั้นรันคำสั่งต่อไปนี้เพื่อสร้างโปรเจกต์ไคลเอนต์ LLM ใหม่:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

เพิ่ม dependencies ต่อไปนี้ในไฟล์ `Cargo.toml` ของคุณ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> ยังไม่มีไลบรารี Rust อย่างเป็นทางการสำหรับ OpenAI แต่ `async-openai` crate เป็น [ไลบรารีที่ชุมชนดูแล](https://platform.openai.com/docs/libraries/rust#rust) ที่ใช้กันทั่วไป

เปิดไฟล์ `src/main.rs` และแทนที่เนื้อหาด้วยโค้ดต่อไปนี้:

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

    // TODO: ดึงรายการเครื่องมือ MCP

    // TODO: การสนทนา LLM พร้อมการเรียกใช้เครื่องมือ

    Ok(())
}
```

โค้ดนี้ตั้งค่าแอปพลิเคชัน Rust พื้นฐานที่จะเชื่อมต่อกับเซิร์ฟเวอร์ MCP และ GitHub Models สำหรับการโต้ตอบกับ LLM

> [!IMPORTANT]
> อย่าลืมตั้งค่าตัวแปรสภาพแวดล้อม `OPENAI_API_KEY` ด้วยโทเค็น GitHub ของคุณก่อนรันแอปพลิเคชัน

ดีมาก ขั้นตอนถัดไป เรามาแสดงรายการความสามารถบนเซิร์ฟเวอร์กัน

### -2- แสดงรายการความสามารถของเซิร์ฟเวอร์

ตอนนี้เราจะเชื่อมต่อกับเซิร์ฟเวอร์และขอความสามารถของมัน:

#### Typescript

ในคลาสเดียวกัน ให้เพิ่มเมธอดต่อไปนี้:

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

ในโค้ดก่อนหน้านี้ เราได้:

- เพิ่มโค้ดสำหรับเชื่อมต่อกับเซิร์ฟเวอร์ `connectToServer`
- สร้างเมธอด `run` ที่รับผิดชอบจัดการลำดับการทำงานของแอป ตอนนี้มันแสดงเฉพาะรายการเครื่องมือ แต่เราจะเพิ่มฟังก์ชันอื่นๆ ในไม่ช้า

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

- แสดงรายการทรัพยากรและเครื่องมือและพิมพ์ออกมา สำหรับเครื่องมือเรายังแสดง `inputSchema` ซึ่งจะใช้ในภายหลัง

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

ในโค้ดก่อนหน้านี้ เราได้:

- แสดงรายการเครื่องมือที่มีในเซิร์ฟเวอร์ MCP
- สำหรับแต่ละเครื่องมือ แสดงชื่อ คำอธิบาย และสคีมาของมัน ซึ่งเราจะใช้เรียกเครื่องมือในไม่ช้า

#### Java

```java
// สร้างผู้ให้บริการเครื่องมือที่ค้นหาเครื่องมือ MCP โดยอัตโนมัติ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ผู้ให้บริการเครื่องมือ MCP จะจัดการโดยอัตโนมัติ:
// - แสดงรายการเครื่องมือที่มีจากเซิร์ฟเวอร์ MCP
// - แปลงสคีมาของเครื่องมือ MCP เป็นรูปแบบ LangChain4j
// - จัดการการดำเนินการเครื่องมือและการตอบกลับ
```

ในโค้ดก่อนหน้านี้ เราได้:

- สร้าง `McpToolProvider` ที่ค้นหาและลงทะเบียนเครื่องมือทั้งหมดจากเซิร์ฟเวอร์ MCP โดยอัตโนมัติ
- ตัวจัดหาเครื่องมือจัดการการแปลงระหว่างสคีมาของเครื่องมือ MCP และรูปแบบเครื่องมือของ LangChain4j ภายใน
- วิธีนี้ช่วยให้ไม่ต้องแสดงรายการเครื่องมือและแปลงด้วยตนเอง

#### Rust

การดึงเครื่องมือจากเซิร์ฟเวอร์ MCP ทำได้โดยใช้เมธอด `list_tools` ในฟังก์ชัน `main` ของคุณ หลังจากตั้งค่าไคลเอนต์ MCP แล้ว ให้เพิ่มโค้ดต่อไปนี้:

```rust
// รับรายการเครื่องมือ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- แปลงความสามารถของเซิร์ฟเวอร์เป็นเครื่องมือ LLM

ขั้นตอนถัดไปหลังจากแสดงรายการความสามารถของเซิร์ฟเวอร์คือการแปลงเป็นรูปแบบที่ LLM เข้าใจ เมื่อทำเสร็จแล้ว เราสามารถให้ความสามารถเหล่านี้เป็นเครื่องมือกับ LLM ของเราได้

#### TypeScript

1. เพิ่มโค้ดต่อไปนี้เพื่อแปลงการตอบสนองจากเซิร์ฟเวอร์ MCP เป็นรูปแบบเครื่องมือที่ LLM ใช้ได้:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // สร้างสคีมา zod ตาม input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // กำหนดประเภทเป็น "function" อย่างชัดเจน
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

    โค้ดข้างต้นรับการตอบสนองจากเซิร์ฟเวอร์ MCP และแปลงเป็นรูปแบบการกำหนดเครื่องมือที่ LLM เข้าใจ

1. ต่อไปอัปเดตเมธอด `run` เพื่อแสดงรายการความสามารถของเซิร์ฟเวอร์:

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

    ในโค้ดก่อนหน้านี้ เราอัปเดตเมธอด `run` เพื่อวนลูปผ่านผลลัพธ์และสำหรับแต่ละรายการเรียก `openAiToolAdapter`

#### Python

1. ก่อนอื่น สร้างฟังก์ชันแปลงดังนี้

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

    ในฟังก์ชัน `convert_to_llm_tools` ข้างต้น เรารับการตอบสนองเครื่องมือ MCP และแปลงเป็นรูปแบบที่ LLM เข้าใจ

1. ต่อไป อัปเดตโค้ดไคลเอนต์ของเราเพื่อใช้ฟังก์ชันนี้ดังนี้:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ที่นี่ เราเพิ่มการเรียก `convert_to_llm_tool` เพื่อแปลงการตอบสนองเครื่องมือ MCP เป็นสิ่งที่เราสามารถส่งให้ LLM ได้ในภายหลัง

#### .NET

1. เพิ่มโค้ดเพื่อแปลงการตอบสนองเครื่องมือ MCP เป็นสิ่งที่ LLM เข้าใจ

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

ในโค้ดก่อนหน้านี้ เราได้:

- สร้างฟังก์ชัน `ConvertFrom` ที่รับชื่อ คำอธิบาย และสคีมาป้อนเข้า
- กำหนดฟังก์ชันที่สร้าง `FunctionDefinition` ซึ่งถูกส่งไปยัง `ChatCompletionsDefinition` ซึ่งเป็นสิ่งที่ LLM เข้าใจ

1. มาดูวิธีอัปเดตโค้ดที่มีอยู่เพื่อใช้ฟังก์ชันนี้:

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

ในโค้ดก่อนหน้านี้ เราได้:

- กำหนดอินเทอร์เฟซ `Bot` ง่ายๆ สำหรับการโต้ตอบด้วยภาษาธรรมชาติ
- ใช้ `AiServices` ของ LangChain4j เพื่อผูก LLM กับผู้ให้บริการเครื่องมือ MCP โดยอัตโนมัติ
- เฟรมเวิร์กจัดการการแปลงสคีมาของเครื่องมือและการเรียกฟังก์ชันเบื้องหลังโดยอัตโนมัติ
- วิธีนี้ช่วยขจัดการแปลงเครื่องมือด้วยตนเอง — LangChain4j จัดการความซับซ้อนทั้งหมดของการแปลงเครื่องมือ MCP เป็นรูปแบบที่เข้ากันได้กับ LLM

#### Rust

เพื่อแปลงการตอบสนองเครื่องมือ MCP เป็นรูปแบบที่ LLM เข้าใจ เราจะเพิ่มฟังก์ชันช่วยที่จัดรูปแบบรายการเครื่องมือ เพิ่มโค้ดต่อไปนี้ในไฟล์ `main.rs` ของคุณใต้ฟังก์ชัน `main` ฟังก์ชันนี้จะถูกเรียกเมื่อส่งคำขอไปยัง LLM:

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

ดีมาก ตอนนี้เราพร้อมจัดการคำขอของผู้ใช้แล้ว มาดูขั้นตอนถัดไปกัน

### -4- จัดการคำขอพรอมต์ของผู้ใช้

ในส่วนนี้ของโค้ด เราจะจัดการคำขอของผู้ใช้

#### TypeScript

1. เพิ่มเมธอดที่จะใช้เรียก LLM ของเรา:

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
        // ต้องทำ

        }
    }
    ```

    ในโค้ดก่อนหน้านี้ เราได้:

    - เพิ่มเมธอด `callTools`
    - เมธอดนี้รับการตอบสนองจาก LLM และตรวจสอบว่าเครื่องมือใดถูกเรียกใช้งานหรือไม่:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // เรียกใช้เครื่องมือ
        }
        ```

    - เรียกเครื่องมือ หาก LLM ระบุว่าควรเรียก:

        ```typescript
        // 2. เรียกใช้เครื่องมือของเซิร์ฟเวอร์
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ทำบางอย่างกับผลลัพธ์
        // ต้องทำ
        ```

1. อัปเดตเมธอด `run` เพื่อรวมการเรียก LLM และเรียก `callTools`:

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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. ตรวจสอบการตอบกลับจาก LLM สำหรับแต่ละตัวเลือก ว่ามีการเรียกใช้เครื่องมือหรือไม่
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ดีมาก มาดูโค้ดทั้งหมดกัน:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // นำเข้า zod สำหรับการตรวจสอบสคีมา

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
          // สร้างสคีมา zod ตาม input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // กำหนดประเภทเป็น "function" อย่างชัดเจน
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
          // ต้องทำ
    
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. ตรวจสอบการตอบกลับของ LLM สำหรับแต่ละตัวเลือก ว่ามีการเรียกใช้เครื่องมือหรือไม่
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

1. เพิ่มการนำเข้าที่จำเป็นสำหรับการเรียก LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. ต่อไป เพิ่มฟังก์ชันที่จะเรียก LLM:

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
            # พารามิเตอร์ที่เลือกได้
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

    ในโค้ดก่อนหน้านี้ เราได้:

    - ส่งฟังก์ชันที่เราค้นพบบนเซิร์ฟเวอร์ MCP และแปลงแล้วไปยัง LLM
    - จากนั้นเรียก LLM ด้วยฟังก์ชันเหล่านั้น
    - ตรวจสอบผลลัพธ์เพื่อดูว่าควรเรียกฟังก์ชันใดหรือไม่
    - สุดท้ายส่งอาร์เรย์ของฟังก์ชันที่จะเรียก

1. ขั้นตอนสุดท้าย อัปเดตโค้ดหลักของเรา:

    ```python
    prompt = "Add 2 to 20"

    # ถาม LLM ว่ามีเครื่องมืออะไรบ้าง ถ้ามี
    functions_to_call = call_llm(prompt, functions)

    # เรียกใช้ฟังก์ชันที่แนะนำ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    นั่นคือขั้นตอนสุดท้าย ในโค้ดข้างต้น เรา:

    - เรียกเครื่องมือ MCP ผ่าน `call_tool` โดยใช้ฟังก์ชันที่ LLM คิดว่าเราควรเรียกตามพรอมต์ของเรา
    - พิมพ์ผลลัพธ์ของการเรียกเครื่องมือไปยังเซิร์ฟเวอร์ MCP

#### .NET

1. แสดงโค้ดสำหรับการร้องขอพรอมต์ LLM:

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
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    ในโค้ดก่อนหน้านี้ เราได้:

    - ดึงเครื่องมือจากเซิร์ฟเวอร์ MCP, `var tools = await GetMcpTools()`
    - กำหนดพรอมต์ผู้ใช้ `userMessage`
    - สร้างอ็อบเจ็กต์ options ระบุโมเดลและเครื่องมือ
    - ส่งคำขอไปยัง LLM

1. ขั้นตอนสุดท้าย มาดูว่า LLM คิดว่าเราควรเรียกฟังก์ชันหรือไม่:

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

    ในโค้ดก่อนหน้านี้ เราได้:

    - วนลูปผ่านรายการการเรียกฟังก์ชัน
    - สำหรับแต่ละการเรียกเครื่องมือ แยกชื่อและอาร์กิวเมนต์ แล้วเรียกเครื่องมือบนเซิร์ฟเวอร์ MCP โดยใช้ไคลเอนต์ MCP สุดท้ายพิมพ์ผลลัพธ์

นี่คือโค้ดทั้งหมด:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

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
    Model = "gpt-4o-mini",
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

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // ดำเนินการคำขอภาษาธรรมชาติที่ใช้เครื่องมือ MCP โดยอัตโนมัติ
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

ในโค้ดก่อนหน้านี้ เราได้:

- ใช้พรอมต์ภาษาธรรมชาติอย่างง่ายเพื่อโต้ตอบกับเครื่องมือเซิร์ฟเวอร์ MCP
- เฟรมเวิร์ก LangChain4j จัดการโดยอัตโนมัติ:
  - การแปลงพรอมต์ผู้ใช้เป็นการเรียกเครื่องมือเมื่อจำเป็น
  - การเรียกเครื่องมือ MCP ที่เหมาะสมตามการตัดสินใจของ LLM
  - การจัดการลำดับการสนทนาระหว่าง LLM และเซิร์ฟเวอร์ MCP
- เมธอด `bot.chat()` คืนค่าการตอบกลับภาษาธรรมชาติที่อาจรวมผลลัพธ์จากการเรียกใช้เครื่องมือ MCP
- วิธีนี้มอบประสบการณ์ผู้ใช้ที่ราบรื่นโดยที่ผู้ใช้ไม่จำเป็นต้องรู้เกี่ยวกับการทำงานภายในของ MCP

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

นี่คือส่วนที่งานส่วนใหญ่เกิดขึ้น เราจะเรียก LLM ด้วยพรอมต์ผู้ใช้เริ่มต้น จากนั้นประมวลผลการตอบสนองเพื่อดูว่าต้องเรียกเครื่องมือใดหรือไม่ หากต้อง เราจะเรียกเครื่องมือเหล่านั้นและดำเนินการสนทนากับ LLM ต่อไปจนกว่าจะไม่มีการเรียกเครื่องมือเพิ่มเติมและเราได้รับการตอบกลับสุดท้าย

เราจะเรียก LLM หลายครั้ง ดังนั้นมาสร้างฟังก์ชันที่จะจัดการการเรียก LLM กัน เพิ่มฟังก์ชันต่อไปนี้ในไฟล์ `main.rs` ของคุณ:

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

ฟังก์ชันนี้รับไคลเอนต์ LLM รายการข้อความ (รวมพรอมต์ผู้ใช้) เครื่องมือจากเซิร์ฟเวอร์ MCP และส่งคำขอไปยัง LLM พร้อมส่งกลับการตอบสนอง
การตอบกลับจาก LLM จะประกอบด้วยอาร์เรย์ของ `choices` เราจะต้องประมวลผลผลลัพธ์เพื่อดูว่ามี `tool_calls` อยู่หรือไม่ ซึ่งจะทำให้เราทราบว่า LLM กำลังร้องขอให้เรียกใช้เครื่องมือเฉพาะพร้อมอาร์กิวเมนต์ เพิ่มโค้ดต่อไปนี้ที่ด้านล่างของไฟล์ `main.rs` ของคุณเพื่อกำหนดฟังก์ชันสำหรับจัดการการตอบกลับของ LLM:

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

            // เพิ่มผลลัพธ์ของเครื่องมือในข้อความ
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

หากมี `tool_calls` ฟังก์ชันจะดึงข้อมูลเครื่องมือ เรียกเซิร์ฟเวอร์ MCP ด้วยคำขอเครื่องมือ และเพิ่มผลลัพธ์ลงในข้อความสนทนา จากนั้นจะดำเนินการสนทนาต่อกับ LLM และข้อความจะได้รับการอัปเดตด้วยการตอบกลับของผู้ช่วยและผลลัพธ์การเรียกใช้เครื่องมือ

เพื่อดึงข้อมูลการเรียกใช้เครื่องมือที่ LLM ส่งกลับสำหรับการเรียก MCP เราจะเพิ่มฟังก์ชันช่วยเหลืออีกตัวหนึ่งเพื่อดึงทุกอย่างที่จำเป็นสำหรับการเรียกใช้ เพิ่มโค้ดต่อไปนี้ที่ด้านล่างของไฟล์ `main.rs` ของคุณ:

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

เมื่อมีทุกส่วนพร้อมแล้ว เราสามารถจัดการกับคำสั่งเริ่มต้นของผู้ใช้และเรียก LLM ได้ อัปเดตฟังก์ชัน `main` ของคุณให้รวมโค้ดต่อไปนี้:

```rust
// การสนทนา LLM พร้อมการเรียกใช้เครื่องมือ
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

โค้ดนี้จะส่งคำถามเริ่มต้นของผู้ใช้ไปยัง LLM เพื่อขอผลรวมของตัวเลขสองตัว และจะประมวลผลการตอบกลับเพื่อจัดการการเรียกใช้เครื่องมืออย่างไดนามิก

เยี่ยมมาก คุณทำได้แล้ว!

## การบ้าน

นำโค้ดจากแบบฝึกหัดไปสร้างเซิร์ฟเวอร์ที่มีเครื่องมือเพิ่มเติม จากนั้นสร้างไคลเอนต์ที่มี LLM เหมือนในแบบฝึกหัด และทดสอบด้วยคำสั่งต่าง ๆ เพื่อให้แน่ใจว่าเครื่องมือทั้งหมดในเซิร์ฟเวอร์ของคุณถูกเรียกใช้อย่างไดนามิก วิธีการสร้างไคลเอนต์แบบนี้หมายความว่าผู้ใช้ปลายทางจะได้รับประสบการณ์ที่ดีเพราะสามารถใช้คำสั่งในรูปแบบข้อความแทนคำสั่งไคลเอนต์ที่แน่นอน และไม่ต้องรู้ตัวเลยว่ามีการเรียกใช้เซิร์ฟเวอร์ MCP

## วิธีแก้ปัญหา

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## ประเด็นสำคัญ

- การเพิ่ม LLM ลงในไคลเอนต์ของคุณช่วยให้ผู้ใช้มีวิธีโต้ตอบกับ MCP Servers ที่ดียิ่งขึ้น
- คุณต้องแปลงการตอบกลับของ MCP Server ให้เป็นสิ่งที่ LLM เข้าใจได้

## ตัวอย่าง

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## แหล่งข้อมูลเพิ่มเติม

## ต่อไป

- ต่อไป: [การใช้งานเซิร์ฟเวอร์ผ่าน Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->