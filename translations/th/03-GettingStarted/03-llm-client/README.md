# การสร้างไคลเอนต์ด้วย LLM

จนถึงตอนนี้ คุณได้เห็นวิธีการสร้างเซิร์ฟเวอร์และไคลเอนต์แล้ว ไคลเอนต์สามารถเรียกเซิร์ฟเวอร์อย่างชัดเจนเพื่อแสดงรายการเครื่องมือ ทรัพยากร และพรอมต์ของมันได้ อย่างไรก็ตาม นี่ไม่ใช่วิธีที่ใช้งานได้จริงมากนัก ผู้ใช้ของคุณอยู่ในยุคของเอเจนต์และคาดหวังที่จะใช้พรอมต์และสื่อสารกับ LLM แทน พวกเขาไม่สนใจว่าคุณใช้ MCP เพื่อเก็บความสามารถอย่างไร พวกเขาเพียงต้องการโต้ตอบโดยใช้ภาษาธรรมชาติ แล้วเราจะแก้ปัญหานี้อย่างไร? วิธีแก้คือการเพิ่ม LLM เข้าไปในไคลเอนต์

## ภาพรวม

ในบทเรียนนี้ เราจะมุ่งเน้นที่การเพิ่ม LLM ให้กับไคลเอนต์ของคุณและแสดงให้เห็นว่าสิ่งนี้ทำให้ประสบการณ์ของผู้ใช้ดีขึ้นอย่างไร

## วัตถุประสงค์การเรียนรู้

เมื่อสิ้นสุดบทเรียนนี้ คุณจะสามารถ:

- สร้างไคลเอนต์พร้อมกับ LLM
- โต้ตอบกับเซิร์ฟเวอร์ MCP โดยใช้ LLM อย่างไร้รอยต่อ
- มอบประสบการณ์ผู้ใช้ปลายทางที่ดีกว่าบนฝั่งไคลเอนต์

## แนวทาง

ลองทำความเข้าใจแนวทางที่เราต้องใช้กันก่อน การเพิ่ม LLM ดูเหมือนง่าย แต่เราจะทำจริงหรือ?

นี่คือวิธีที่ไคลเอนต์จะโต้ตอบกับเซิร์ฟเวอร์:

1. สร้างการเชื่อมต่อกับเซิร์ฟเวอร์

1. แสดงรายการความสามารถ พรอมต์ ทรัพยากร และเครื่องมือ พร้อมบันทึกโครงสร้างข้อมูลของพวกมัน

1. เพิ่ม LLM และส่งต่อความสามารถและโครงสร้างข้อมูลที่บันทึกไว้ในรูปแบบที่ LLM เข้าใจ

1. จัดการพรอมต์ของผู้ใช้โดยส่งต่อไปยัง LLM ร่วมกับเครื่องมือที่ไคลเอนต์แสดงรายการไว้

ดีมาก ตอนนี้เราเข้าใจคร่าวๆ ว่าจะทำอย่างไร ลองมาทดลองในแบบฝึกหัดด้านล่างกัน

## แบบฝึกหัด: การสร้างไคลเอนต์ด้วย LLM

ในแบบฝึกหัดนี้ เราจะเรียนรู้การเพิ่ม LLM ให้กับไคลเอนต์ของเรา

### การตรวจสอบสิทธิ์โดยใช้ GitHub Personal Access Token

การสร้างโทเค็น GitHub เป็นกระบวนการที่ตรงไปตรงมา วิธีทำมีดังนี้:

- ไปที่ GitHub Settings – คลิกที่ภาพโปรไฟล์ของคุณที่มุมขวาบนแล้วเลือก Settings
- ไปที่ Developer Settings – เลื่อนลงมาแล้วคลิกที่ Developer Settings
- เลือก Personal Access Tokens – คลิกที่ Fine-grained tokens แล้วกด Generate new token
- ตั้งค่าโทเค็นของคุณ – เพิ่มบันทึกเพื่ออ้างอิง ตั้งวันที่หมดอายุ และเลือกขอบเขตการอนุญาตที่จำเป็น เช่น เพิ่มสิทธิ์ Models
- สร้างและคัดลอกโทเค็น – กด Generate token และคัดลอกทันที เพราะหลังจากนั้นจะไม่สามารถดูได้อีก

### -1- เชื่อมต่อกับเซิร์ฟเวอร์

ให้เราสร้างไคลเอนต์ของเราก่อน:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // นำเข้า zod สำหรับการตรวจสอบโครงสร้างข้อมูล

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

- นำเข้าไลบรารีที่จำเป็น
- สร้างคลาสที่มีสมาชิกสองตัว `client` กับ `openai` ซึ่งจะช่วยจัดการไคลเอนต์และโต้ตอบกับ LLM ตามลำดับ
- กำหนดค่าตัวอย่าง LLM ของเราให้ใช้ GitHub Models โดยตั้งค่า `baseUrl` ชี้ไปยัง API การอนุมาน

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

- นำเข้าไลบรารีที่จำเป็นสำหรับ MCP
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

ก่อนอื่น คุณต้องเพิ่ม dependencies ของ LangChain4j ในไฟล์ `pom.xml` ของคุณ เพิ่ม dependencies เหล่านี้เพื่อเปิดใช้งานการรวม MCP และรองรับ GitHub Models:

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

        // สร้างการขนส่ง MCP เพื่อเชื่อมต่อกับเซิร์ฟเวอร์
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

- **เพิ่ม dependencies ของ LangChain4j**: ซึ่งจำเป็นสำหรับการรวม MCP, ไคลเอนต์ทางการของ OpenAI, และการรองรับ GitHub Models
- **นำเข้าไลบรารี LangChain4j**: สำหรับการรวม MCP และฟังก์ชันการทำงานของโมเดลแชท OpenAI
- **สร้าง `ChatLanguageModel`**: ตั้งค่าให้ใช้ GitHub Models พร้อมโทเค็น GitHub ของคุณ
- **ตั้งค่าการขนส่ง HTTP**: ใช้ Server-Sent Events (SSE) เพื่อเชื่อมต่อกับเซิร์ฟเวอร์ MCP
- **สร้างไคลเอนต์ MCP**: ที่จะจัดการการสื่อสารกับเซิร์ฟเวอร์
- **ใช้การสนับสนุน MCP ในตัวของ LangChain4j**: ซึ่งช่วยให้ง่ายต่อการรวมระหว่าง LLM กับเซิร์ฟเวอร์ MCP

#### Rust

ตัวอย่างนี้สมมติว่าคุณมีเซิร์ฟเวอร์ MCP ที่เขียนด้วย Rust กำลังทำงานอยู่ หากไม่มี ให้กลับไปที่บทเรียน [01-first-server](../01-first-server/README.md) เพื่อสร้างเซิร์ฟเวอร์

เมื่อคุณมีเซิร์ฟเวอร์ MCP ของ Rust แล้ว เปิดเทอร์มินัลและไปยังไดเรกทอรีเดียวกับเซิร์ฟเวอร์ แล้วรันคำสั่งนี้เพื่อสร้างโปรเจกต์ไคลเอนต์ LLM ใหม่:

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
> ยังไม่มีไลบรารี Rust ทางการสำหรับ OpenAI อย่างไรก็ตาม `async-openai` crate เป็น [ไลบรารีที่ชุมชนดูแล](https://platform.openai.com/docs/libraries/rust#rust) ที่ใช้กันอย่างแพร่หลาย

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

    // ตั้งค่าไคลเอ็นต์ OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // ตั้งค่าไคลเอ็นต์ MCP
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

    // ที่จะทำ: รับรายการเครื่องมือ MCP

    // ที่จะทำ: สนทนา LLM กับการเรียกเครื่องมือ

    Ok(())
}
```

โค้ดนี้ตั้งค่าแอปพลิเคชัน Rust พื้นฐานที่จะเชื่อมต่อกับเซิร์ฟเวอร์ MCP และ GitHub Models สำหรับโต้ตอบ LLM

> [!IMPORTANT]
> โปรดตั้งค่าตัวแปรสภาพแวดล้อม `OPENAI_API_KEY` ด้วยโทเค็น GitHub ของคุณก่อนรันแอปพลิเคชัน

ดีมาก ขั้นตอนต่อไป มาลิสต์ความสามารถบนเซิร์ฟเวอร์กัน

### -2- แสดงรายการความสามารถของเซิร์ฟเวอร์

ตอนนี้เราจะเชื่อมต่อกับเซิร์ฟเวอร์และขอรายการความสามารถของมัน:

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

    // เครื่องมือสำหรับแสดงรายการ
    const toolsResult = await this.client.listTools();
}
```

ในโค้ดก่อนหน้านี้เราได้:

- เพิ่มโค้ดสำหรับเชื่อมต่อกับเซิร์ฟเวอร์ `connectToServer`
- สร้างเมธอด `run` ที่รับผิดชอบจัดการลำดับการทำงานของแอป ตอนนี้ยังแค่แสดงรายการเครื่องมือ แต่เราจะเพิ่มอีกเร็วๆ นี้

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

สิ่งที่เราเพิ่มเข้าไปคือ:

- แสดงรายการทรัพยากรและเครื่องมือ และพิมพ์ออกมา สำหรับเครื่องมือ เราแสดง `inputSchema` ซึ่งจะใช้ต่อไป

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

- แสดงรายการเครื่องมือที่มีใน MCP Server
- สำหรับแต่ละเครื่องมือ แสดงชื่อ คำอธิบาย และโค้ดสคีมาของมัน ซึ่งสิ่งหลังนี้เราจะใช้เรียกเครื่องมือเร็วๆ นี้

#### Java

```java
// สร้างผู้ให้บริการเครื่องมือที่ค้นหาเครื่องมือ MCP โดยอัตโนมัติ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ผู้ให้บริการเครื่องมือ MCP จะจัดการโดยอัตโนมัติ:
// - แสดงรายการเครื่องมือที่มีอยู่จากเซิร์ฟเวอร์ MCP
// - แปลงโครงร่างเครื่องมือ MCP เป็นรูปแบบ LangChain4j
// - จัดการการเรียกใช้เครื่องมือและการตอบกลับ
```

ในโค้ดก่อนหน้านี้เราได้:

- สร้าง `McpToolProvider` ซึ่งค้นหาและลงทะเบียนเครื่องมือทั้งหมดจากเซิร์ฟเวอร์ MCP โดยอัตโนมัติ
- ตัวจัดหาเครื่องมือจัดการการแปลงระหว่างโค้ดสคีมาของเครื่องมือ MCP กับรูปแบบเครื่องมือของ LangChain4j ภายใน
- แนวทางนี้ทำให้ไม่ต้องลิสต์เครื่องมือและแปลงด้วยมือ

#### Rust

การดึงเครื่องมือจาก MCP Server ทำได้โดยใช้เมธอด `list_tools` ในฟังก์ชัน `main` หลังจากตั้งค่าไคลเอนต์ MCP ให้เพิ่มโค้ดนี้:

```rust
// ดึงรายการเครื่องมือ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- แปลงความสามารถของเซิร์ฟเวอร์เป็นเครื่องมือ LLM

ขั้นตอนถัดไปหลังจากลิสต์ความสามารถของเซิร์ฟเวอร์คือ แปลงความสามารถเหล่านั้นให้อยู่ในรูปแบบที่ LLM เข้าใจ เมื่อทำเสร็จ เราสามารถนำเสนอความสามารถเหล่านี้เป็นเครื่องมือให้ LLM ได้

#### TypeScript

1. เพิ่มโค้ดต่อไปนี้เพื่อแปลงคำตอบจาก MCP Server เป็นรูปแบบเครื่องมือที่ LLM ใช้งานได้:

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

    โค้ดด้านบนรับคำตอบจาก MCP Server และแปลงเป็นรูปแบบนิยามเครื่องมือที่ LLM เข้าใจ

1. ต่อไป อัปเดตเมธอด `run` เพื่อแสดงรายการความสามารถของเซิร์ฟเวอร์ดังนี้:

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

    ในโค้ดนี้ เราอัปเดตเมธอด `run` เพื่อวนลูปรายการผลลัพธ์และสำหรับแต่ละรายการเรียก `openAiToolAdapter`

#### Python

1. ก่อนอื่น สร้างฟังก์ชันแปลงข้อมูลดังนี้

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

    ในฟังก์ชัน `convert_to_llm_tools` เราจะรับคำตอบเครื่องมือ MCP แล้วแปลงเป็นรูปแบบที่ LLM เข้าใจได้

1. ต่อไป อัปเดตโค้ดไคลเอนต์ให้ใช้ฟังก์ชันนี้ดังนี้:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ที่นี่ เราเพิ่มการเรียก `convert_to_llm_tool` เพื่อแปลงคำตอบเครื่องมือ MCP เป็นสิ่งที่เราจะส่งให้ LLM ต่อไป

#### .NET

1. เพิ่มโค้ดเพื่อแปลงคำตอบเครื่องมือ MCP เป็นสิ่งที่ LLM เข้าใจ

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

- สร้างฟังก์ชัน `ConvertFrom` ที่ใช้ชื่อ คำอธิบาย และโค้ดสคีมาอินพุต
- กำหนดฟังก์ชันการทำงานที่สร้าง `FunctionDefinition` ซึ่งจะถูกส่งไปยัง `ChatCompletionsDefinition` ซึ่งเป็นสิ่งที่ LLM เข้าใจ

1. มาอัปเดตโค้ดเดิมเพื่อใช้ฟังก์ชันนี้กัน:

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
// สร้างอินเทอร์เฟซ Bot สำหรับการโต้ตอบด้วยภาษาธรรมชาติ
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

- กำหนดอินเทอร์เฟซ `Bot` ง่ายๆ สำหรับการโต้ตอบด้วยภาษาธรรมชาติ
- ใช้ `AiServices` ของ LangChain4j เพื่อผูก LLM กับผู้ให้บริการเครื่องมือ MCP โดยอัตโนมัติ
- เฟรมเวิร์กจัดการการแปลงโค้ดสคีมาของเครื่องมือและการเรียกใช้งานฟังก์ชันเบื้องหลังทั้งหมด
- แนวทางนี้กำจัดความยุ่งยากจากการแปลงเครื่องมือด้วยมือ – LangChain4j ดูแลความซับซ้อนทั้งหมดของการแปลงเครื่องมือ MCP ให้เข้ากับรูปแบบที่ LLM รองรับ

#### Rust

เพื่อแปลงคำตอบเครื่องมือ MCP ให้เป็นรูปแบบที่ LLM เข้าใจ เราจะเพิ่มฟังก์ชันช่วยที่จัดรูปแบบรายการเครื่องมือ เพิ่มโค้ดต่อไปนี้ลงในไฟล์ `main.rs` ใต้ฟังก์ชัน `main` ฟังก์ชันนี้จะถูกเรียกเมื่อทำคำขอไปยัง LLM:

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

ดีเยี่ยม ตอนนี้เราพร้อมจัดการคำขอผู้ใช้แล้ว ลองมาทำกันต่อ

### -4- จัดการคำขอพรอมต์จากผู้ใช้

ในส่วนนี้ของโค้ด เราจะจัดการกับคำขอจากผู้ใช้

#### TypeScript

1. เพิ่มเมธอดที่จะใช้เรียก LLM:

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
        // งานที่ต้องทำ

        }
    }
    ```

    ในโค้ดก่อนหน้านี้เราได้:

    - เพิ่มเมธอด `callTools`
    - เมธอดนี้รับผลลัพธ์จาก LLM และตรวจสอบว่าเครื่องมือใดถูกเรียกใช้งานหรือไม่

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // เรียกเครื่องมือ
        }
        ```

    - เรียกใช้เครื่องมือถ้า LLM ระบุว่าควรเรียก:

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

1. อัปเดตเมธอด `run` ให้รวมการเรียก LLM และเรียกใช้ `callTools` ด้วย:

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

    // 3. ตรวจสอบการตอบกลับของ LLM สำหรับแต่ละตัวเลือก เพื่อตรวจดูว่ามีการเรียกเครื่องมือหรือไม่
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
          // TODO
    
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
    
        // 1. ตรวจสอบการตอบกลับของ LLM สำหรับแต่ละตัวเลือก ว่ามีการเรียกเครื่องมือหรือไม่
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

1. เพิ่มการนำเข้าไลบรารีที่จำเป็นสำหรับเรียก LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. ต่อไป เพิ่มฟังก์ชันที่เรียก LLM:

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
            # พารามิเตอร์ที่ไม่บังคับ
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

    - ส่งฟังก์ชันที่ได้จากเซิร์ฟเวอร์ MCP และแปลงแล้วให้กับ LLM
    - เรียก LLM พร้อมกับฟังก์ชันเหล่านั้น
    - ตรวจสอบผลลัพธ์เพื่อดูว่าควรเรียกฟังก์ชันใด ถ้ามี
    - สุดท้าย ส่งอาร์เรย์ของฟังก์ชันที่ต้องเรียกออกไป

1. ขั้นตอนสุดท้าย อัปเดตโค้ดหลักของเรา:

    ```python
    prompt = "Add 2 to 20"

    # ถาม LLM ว่ามีเครื่องมืออะไรบ้าง หากมี
    functions_to_call = call_llm(prompt, functions)

    # เรียกใช้ฟังก์ชันที่แนะนำ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    นี่คือขั้นตอนสุดท้าย ในโค้ดข้างบน เรา:

    - เรียกเครื่องมือ MCP ผ่าน `call_tool` โดยใช้ฟังก์ชันที่ LLM คิดว่าน่าจะเรียกจากพรอมต์ของเรา
    - พิมพ์ผลลัพธ์จากการเรียกเครื่องมือไปยัง MCP Server

#### .NET

1. แสดงตัวอย่างโค้ดสำหรับการขอพรอมต์กับ LLM:

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

    - ดึงเครื่องมือจาก MCP เซิร์ฟเวอร์ `var tools = await GetMcpTools()`
    - กำหนดพรอมต์ผู้ใช้ `userMessage`
    - สร้างอ็อบเจ็กต์ options กำหนดโมเดลและเครื่องมือ
    - ทำคำขอไปยัง LLM

1. ขั้นตอนสุดท้าย มาดูว่าถ้า LLM คิดว่าเราควรเรียกฟังก์ชันใดไหม:

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

    - วนลูปรายการของการเรียกฟังก์ชัน
    - สำหรับแต่ละการเรียกเครื่องมือ แยกชื่อและอาร์กิวเมนต์ แล้วเรียกเครื่องมือบน MCP เซิร์ฟเวอร์โดยใช้ไคลเอนต์ MCP สุดท้ายพิมพ์ผลลัพธ์

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

ในโค้ดก่อนหน้านี้เราได้:

- ใช้พรอมต์ภาษาธรรมชาติที่ง่ายเพื่อโต้ตอบกับเครื่องมือ MCP เซิร์ฟเวอร์
- เฟรมเวิร์ก LangChain4j จัดการโดยอัตโนมัติ:
  - แปลงพรอมต์ผู้ใช้เป็นการเรียกเครื่องมือเมื่อจำเป็น
  - เรียกเครื่องมือ MCP ที่เหมาะสมตามคำตัดสินของ LLM
  - จัดการลำดับการสนทนาระหว่าง LLM กับ MCP เซิร์ฟเวอร์
- เมธอด `bot.chat()` คืนค่าการตอบสนองในภาษาธรรมชาติที่อาจรวมผลลัพธ์จากการทำงานของเครื่องมือ MCP
- แนวทางนี้มอบประสบการณ์ผู้ใช้ที่ราบรื่น ซึ่งผู้ใช้ไม่จำเป็นต้องรู้จักการทำงานภายในของ MCP

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

สิ่งที่เกิดขึ้นเป็นส่วนใหญ่จะอยู่ที่นี่ เราจะเรียก LLM ด้วยพรอมต์ผู้ใช้เริ่มต้น จากนั้นประมวลผลคำตอบเพื่อดูว่าจำเป็นต้องเรียกเครื่องมือใดหรือไม่ ถ้าใช่ เราจะเรียกเครื่องมือเหล่านั้นและดำเนินการสนทนาต่อกับ LLM จนไม่จำเป็นต้องเรียกเครื่องมือเพิ่มเติมแล้วเราจึงได้คำตอบสุดท้าย

เราจะเรียก LLM หลายครั้ง ดังนั้นให้กำหนดฟังก์ชันที่จะจัดการการเรียก LLM เพิ่มโค้ดต่อไปนี้ในไฟล์ `main.rs`:

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

ฟังก์ชันนี้รับไคลเอนต์ LLM รายการข้อความ (รวมพรอมต์ของผู้ใช้) เครื่องมือจาก MCP เซิร์ฟเวอร์ และส่งคำขอไปยัง LLM พร้อมส่งคืนคำตอบกลับมา
การตอบกลับจาก LLM จะประกอบด้วยอาร์เรย์ของ `choices` เราจำเป็นต้องประมวลผลผลลัพธ์เพื่อตรวจสอบว่ามี `tool_calls` อยู่หรือไม่ ซึ่งจะช่วยให้เราทราบว่า LLM กำลังขอเรียกใช้เครื่องมือเฉพาะพร้อมอาร์กิวเมนต์ ให้เพิ่มโค้ดต่อไปนี้ไปด้านล่างของไฟล์ `main.rs` ของคุณเพื่อกำหนดฟังก์ชันจัดการการตอบกลับจาก LLM:

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

    // แสดงเนื้อหาถ้าพร้อมใช้งาน
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

หากมี `tool_calls` อยู่ ฟังก์ชันจะดึงข้อมูลเครื่องมือ, เรียกใช้เซิร์ฟเวอร์ MCP ด้วยคำขอของเครื่องมือ และเพิ่มผลลัพธ์เข้าไปในข้อความการสนทนา จากนั้นจะดำเนินการสนทนาต่อกับ LLM และข้อความจะได้รับการอัปเดตด้วยการตอบกลับของผู้ช่วยและผลลัพธ์ของการเรียกใช้เครื่องมือ

เพื่อดึงข้อมูลการเรียกใช้เครื่องมือที่ LLM ส่งคืนสำหรับการเรียกใช้ MCP เราจะเพิ่มฟังก์ชันช่วยเหลืออีกตัวเพื่อดึงข้อมูลทั้งหมดที่จำเป็นในการเรียกใช้ ให้เพิ่มโค้ดต่อไปนี้ไปด้านล่างของไฟล์ `main.rs` ของคุณ:

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

ด้วยองค์ประกอบทั้งหมดที่จัดเตรียมไว้ เราสามารถจัดการกับพรอมต์เริ่มต้นของผู้ใช้และเรียกใช้ LLM ได้แล้ว ให้ปรับปรุงฟังก์ชัน `main` ของคุณโดยเพิ่มโค้ดดังต่อไปนี้:

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

โค้ดนี้จะสอบถาม LLM ด้วยพรอมต์เริ่มต้นของผู้ใช้ที่ขอหาผลรวมของตัวเลขสองตัว และจะประมวลผลการตอบกลับเพื่อจัดการการเรียกใช้เครื่องมืออย่างไดนามิก

เยี่ยมมาก คุณทำได้แล้ว!

## งานที่ได้รับมอบหมาย

นำโค้ดจากแบบฝึกหัดไปสร้างเซิร์ฟเวอร์ที่มีเครื่องมือมากขึ้น จากนั้นสร้างไคลเอนต์ที่มี LLM คล้ายกับในแบบฝึกหัดและทดสอบด้วยพรอมต์ต่างๆ เพื่อตรวจสอบให้แน่ใจว่าเครื่องมือทั้งหมดในเซิร์ฟเวอร์ของคุณถูกเรียกใช้อย่างไดนามิก วิธีการสร้างไคลเอนต์แบบนี้หมายความว่าผู้ใช้ปลายทางจะได้รับประสบการณ์ที่ยอดเยี่ยมเนื่องจากพวกเขาสามารถใช้พรอมต์แทนคำสั่งไคลเอนต์ที่แน่นอนได้ และจะไม่รู้ตัวเลยว่ามีการเรียกใช้เซิร์ฟเวอร์ MCP อยู่เบื้องหลัง

## ทางออก

[ทางออก](/03-GettingStarted/03-llm-client/solution/README.md)

## ประเด็นสำคัญที่ควรจดจำ

- การเพิ่ม LLM ลงในไคลเอนต์ของคุณช่วยให้ผู้ใช้มีวิธีที่ดีกว่าในการโต้ตอบกับเซิร์ฟเวอร์ MCP
- คุณจำเป็นต้องแปลงการตอบกลับจากเซิร์ฟเวอร์ MCP ให้เป็นสิ่งที่ LLM เข้าใจได้

## ตัวอย่าง

- [เครื่องคิดเลข Java](../samples/java/calculator/README.md)
- [เครื่องคิดเลข .Net](../../../../03-GettingStarted/samples/csharp)
- [เครื่องคิดเลข JavaScript](../samples/javascript/README.md)
- [เครื่องคิดเลข TypeScript](../samples/typescript/README.md)
- [เครื่องคิดเลข Python](../../../../03-GettingStarted/samples/python)
- [เครื่องคิดเลข Rust](../../../../03-GettingStarted/samples/rust)

## แหล่งข้อมูลเพิ่มเติม

## ต่อไป

- ต่อไป: [การใช้งานเซิร์ฟเวอร์ด้วย Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถูกพิจารณาเป็นแหล่งข้อมูลที่น่าเชื่อถือ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->