# การสร้างไคลเอนต์ด้วย LLM

จนถึงตอนนี้ คุณได้เห็นวิธีการสร้างเซิร์ฟเวอร์และไคลเอนต์ ไคลเอนต์สามารถเรียกเซิร์ฟเวอร์โดยตรงเพื่อแสดงรายการเครื่องมือ ทรัพยากร และพรอมต์ของมัน อย่างไรก็ตาม นี่ไม่ใช่วิธีการที่ใช้งานได้จริงมากนัก ผู้ใช้ของคุณอยู่ในยุคของตัวแทนและคาดหวังที่จะใช้พรอมต์และสื่อสารกับ LLM แทน พวกเขาไม่สนใจว่าคุณจะใช้ MCP เพื่อเก็บความสามารถของคุณหรือไม่; พวกเขาคาดหวังที่จะโต้ตอบโดยใช้ภาษาธรรมชาติ ดังนั้นเราจะแก้ปัญหานี้อย่างไร? วิธีแก้คือการเพิ่ม LLM ลงในไคลเอนต์

## ภาพรวม

ในบทเรียนนี้ เราจะเน้นที่การเพิ่ม LLM ไปยังไคลเอนต์ของคุณและแสดงให้เห็นว่าสิ่งนี้จะช่วยให้ประสบการณ์ของผู้ใช้ดีขึ้นมาก

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- สร้างไคลเอนต์ที่มี LLM
- โต้ตอบกับเซิร์ฟเวอร์ MCP อย่างไร้รอยต่อโดยใช้ LLM
- มอบประสบการณ์ผู้ใช้ปลายทางที่ดีกว่าบนฝั่งไคลเอนต์

## แนวทาง

มาลองเข้าใจแนวทางที่เราต้องทำกัน การเพิ่ม LLM ดูเหมือนจะง่าย แต่ว่าเราจะทำจริงๆ หรือไม่?

นี่คือวิธีที่ไคลเอนต์จะโต้ตอบกับเซิร์ฟเวอร์:

1. สร้างการเชื่อมต่อกับเซิร์ฟเวอร์

1. แสดงรายการความสามารถ พรอมต์ ทรัพยากร และเครื่องมือ พร้อมบันทึกสคีมาไว้

1. เพิ่ม LLM และส่งผ่านความสามารถที่บันทึกไว้พร้อมสคีมาในรูปแบบที่ LLM เข้าใจ

1. จัดการพรอมต์ของผู้ใช้โดยส่งต่อไปยัง LLM พร้อมกับเครื่องมือที่ไคลเอนต์แสดงรายการ

ดีมาก ตอนนี้เราเข้าใจระดับสูงว่าเราสามารถทำสิ่งนี้ได้อย่างไร มาลองทำในแบบฝึกหัดด้านล่างนี้

## แบบฝึกหัด: การสร้างไคลเอนต์ด้วย LLM

ในแบบฝึกหัดนี้ เราจะเรียนรู้การเพิ่ม LLM ลงในไคลเอนต์ของเรา

### การรับรองความถูกต้องโดยใช้โทเค็นส่วนตัว GitHub

การสร้างโทเค็น GitHub เป็นกระบวนการที่ตรงไปตรงมา นี่คือวิธีที่คุณสามารถทำได้:

- ไปที่การตั้งค่า GitHub – คลิกที่รูปโปรไฟล์ของคุณที่มุมขวาบนและเลือก การตั้งค่า
- ไปที่ Developer Settings – เลื่อนลงและคลิกที่ Developer Settings
- เลือก Personal Access Tokens – คลิกที่ Fine-grained tokens แล้วสร้างโทเค็นใหม่
- กำหนดค่าโทเค็นของคุณ – เพิ่มหมายเหตุเพื่ออ้างอิง ตั้งวันที่หมดอายุ และเลือกสโคป (สิทธิ์) ที่จำเป็น ในกรณีนี้ ต้องแน่ใจว่าเพิ่มสิทธิ์ Models ด้วย
- สร้างและคัดลอกโทเค็น – คลิกสร้างโทเค็น และอย่าลืมคัดลอกทันที เพราะคุณจะไม่สามารถเห็นมันอีก

### -1- เชื่อมต่อกับเซิร์ฟเวอร์

มาสร้างไคลเอนต์ของเราก่อน:

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

ในโค้ดก่อนหน้านี้ เราได้:

- นำเข้าห้องสมุดที่จำเป็น
- สร้างคลาสที่มีสมาชิกสองตัว คือ `client` และ `openai` เพื่อช่วยในการจัดการไคลเอนต์และโต้ตอบกับ LLM ตามลำดับ
- กำหนดค่าอินสแตนซ์ LLM ของเราให้ใช้ GitHub Models โดยตั้งค่า `baseUrl` ให้ชี้ไปยัง inference API

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# สร้างพารามิเตอร์เซิร์ฟเวอร์สำหรับการเชื่อมต่อ stdio
server_params = StdioServerParameters(
    command="mcp",  # ไฟล์ที่สามารถรันได้
    args=["run", "server.py"],  # อาร์กิวเมนต์บรรทัดคำสั่งที่ไม่จำเป็น
    env=None,  # ตัวแปรแวดล้อมที่ไม่จำเป็น
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

ก่อนอื่น คุณต้องเพิ่มการพึ่งพา LangChain4j ลงในไฟล์ `pom.xml` ของคุณ เพิ่มการพึ่งพาเหล่านี้เพื่อเปิดใช้งานการรวม MCP และ MiniMax API ที่เข้ากันได้กับ OpenAI:

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
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

ตั้งค่าคีย์ MiniMax API ของคุณ และระบุจุดสิ้นสุดและโมเดล (ถ้าต้องการ)
`MINIMAX_MODEL_ID` รองรับ `MiniMax-M3` และ `MiniMax-M2.7` หาก
ไม่ได้ตั้งค่า `OPENAI_BASE_URL` `MINIMAX_REGION` รองรับ `global_en` และ `cn_zh`

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

หากต้องการเลือกจุดสิ้นสุดตามภูมิภาค ให้ละเว้น `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

ในโค้ดก่อนหน้านี้ เราได้:

- **เพิ่มการพึ่งพาของ LangChain4j**: จำเป็นสำหรับการรวม MCP และ MiniMax API ที่เข้ากันได้กับ OpenAI
- **นำเข้าห้องสมุด LangChain4j**: สำหรับการรวม MCP และฟังก์ชันโมเดลแชทของ OpenAI
- **สร้าง `ChatLanguageModel`**: กำหนดค่าให้ใช้ MiniMax พร้อมคีย์ MiniMax API จุดสิ้นสุด และ ID โมเดลที่รองรับ
- **ตั้งค่าการขนส่ง HTTP**: ใช้ Server-Sent Events (SSE) เพื่อเชื่อมต่อกับเซิร์ฟเวอร์ MCP
- **สร้างไคลเอนต์ MCP**: สำหรับจัดการการสื่อสารกับเซิร์ฟเวอร์
- **ใช้การสนับสนุน MCP ในตัวของ LangChain4j**: ซึ่งทำให้การรวมระหว่าง LLM และเซิร์ฟเวอร์ MCP ง่ายขึ้น

#### Rust

ตัวอย่างนี้สมมติว่าคุณมีเซิร์ฟเวอร์ MCP ที่ใช้งานบน Rust หากคุณยังไม่มี ให้ย้อนกลับไปดูบทเรียน [01-first-server](../01-first-server/README.md) เพื่อสร้างเซิร์ฟเวอร์

เมื่อคุณมีเซิร์ฟเวอร์ MCP Rust แล้ว เปิดเทอร์มินัลและไปยังไดเรกทอรีเดียวกับเซิร์ฟเวอร์ จากนั้นรันคำสั่งต่อไปนี้เพื่อสร้างโครงการไคลเอนต์ LLM ใหม่:

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
> ยังไม่มีห้องสมุด Rust อย่างเป็นทางการสำหรับ OpenAI อย่างไรก็ตาม crate `async-openai` เป็น [ห้องสมุดที่ดูแลโดยชุมชน](https://platform.openai.com/docs/libraries/rust#rust) ที่นิยมใช้กัน

เปิดไฟล์ `src/main.rs` และแทนที่เนื้อหาด้วยโค้ดดังนี้:

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

    // ต้องทำ: รับรายชื่อเครื่องมือ MCP

    // ต้องทำ: การสนทนา LLM พร้อมการเรียกใช้เครื่องมือ

    Ok(())
}
```

โค้ดนี้ตั้งค่าแอปพลิเคชัน Rust เบื้องต้นที่จะเชื่อมต่อกับเซิร์ฟเวอร์ MCP และ GitHub Models สำหรับการโต้ตอบกับ LLM

> [!IMPORTANT]
> ตรวจสอบให้แน่ใจว่าตั้งค่าตัวแปรสภาพแวดล้อม `OPENAI_API_KEY` ด้วยโทเค็น GitHub ของคุณก่อนที่รันแอปพลิเคชันนี้

ดีมาก ขั้นตอนต่อไป มาลิสต์ความสามารถบนเซิร์ฟเวอร์กัน

### -2- ลิสต์ความสามารถของเซิร์ฟเวอร์

ตอนนี้เราจะเชื่อมต่อกับเซิร์ฟเวอร์และถามความสามารถของมัน:

#### Typescript

ในคลาสเดียวกัน เพิ่มเมธอดต่อไปนี้:

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
- สร้างเมธอด `run` ซึ่งรับผิดชอบจัดการลำดับแอปของเรา ตอนนี้เพียงแค่ลิสต์เครื่องมือ แต่เราจะเพิ่มมากขึ้นในเร็วๆ นี้

#### Python

```python
# แสดงรายการทรัพยากรที่มี
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

สิ่งที่เราเพิ่ม:

- รายการทรัพยากรและเครื่องมือและพิมพ์ออก สำหรับเครื่องมือ เราลิสต์ `inputSchema` ซึ่งจะใช้ในภายหลังด้วย

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

- ลิสต์เครื่องมือที่มีในเซิร์ฟเวอร์ MCP
- สำหรับเครื่องมือแต่ละตัว ลิสต์ชื่อ คำอธิบาย และสคีมา ซึ่งเราจะใช้เรียกเครื่องมือในเร็วๆ นี้

#### Java

```java
// สร้างเครื่องมือผู้ให้บริการที่ค้นหาเครื่องมือ MCP โดยอัตโนมัติ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ผู้ให้บริการเครื่องมือ MCP จัดการโดยอัตโนมัติ:
// - แสดงรายชื่อเครื่องมือที่มีจากเซิร์ฟเวอร์ MCP
// - แปลงสคีมาของเครื่องมือ MCP เป็นรูปแบบ LangChain4j
// - จัดการการเรียกใช้เครื่องมือและการตอบสนอง
```

ในโค้ดก่อนหน้านี้ เราได้:

- สร้าง `McpToolProvider` ที่ค้นหาและลงทะเบียนเครื่องมือทั้งหมดจากเซิร์ฟเวอร์ MCP โดยอัตโนมัติ
- ผู้ให้บริการเครื่องมือจัดการการแปลงสคีมาของเครื่องมือ MCP และรูปแบบเครื่องมือของ LangChain4j ภายใน
- วิธีนี้ช่วยกำจัดขั้นตอนการลิสต์และแปลงเครื่องมือด้วยมือ

#### Rust

การดึงเครื่องมือจากเซิร์ฟเวอร์ MCP ทำได้โดยใช้เมธอด `list_tools` ในฟังก์ชัน `main` ของคุณ หลังเตรียมไคลเอนต์ MCP แล้ว เพิ่มโค้ดนี้:

```rust
// รับรายการเครื่องมือ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- แปลงความสามารถของเซิร์ฟเวอร์เป็นเครื่องมือ LLM

ขั้นตอนถัดไปหลังจากลิสต์ความสามารถของเซิร์ฟเวอร์คือการแปลงเป็นรูปแบบที่ LLM เข้าใจ เมื่อทำเช่นนั้น เราสามารถให้ความสามารถเหล่านี้เป็นเครื่องมือกับ LLM ของเรา

#### TypeScript

1. เพิ่มโค้ดต่อไปนี้เพื่อแปลงคำตอบจากเซิร์ฟเวอร์ MCP เป็นรูปแบบเครื่องมือที่ LLM ใช้ได้:

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

    โค้ดด้านบนรับคำตอบจากเซิร์ฟเวอร์ MCP และแปลงเป็นรูปแบบนิยามเครื่องมือที่ LLM เข้าใจ

2. ต่อไปอัปเดตเมธอด `run` เพื่อแสดงความสามารถของเซิร์ฟเวอร์:

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

    ในโค้ดก่อนหน้านี้ เราได้อัปเดตเมธอด `run` เพื่อแมปผ่านผลลัพธ์ และสำหรับแต่ละรายการเรียก `openAiToolAdapter`

#### Python

1. เริ่มด้วยสร้างฟังก์ชันแปลงข้อมูลนี้:

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

    ในฟังก์ชัน `convert_to_llm_tools` เรารับคำตอบเครื่องมือ MCP และแปลงเป็นรูปแบบที่ LLM เข้าใจ

2. ต่อไปอัปเดตโค้ดไคลเอนต์ของเราเพื่อใช้ฟังก์ชันนี้แบบนี้:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ที่นี่ เราเพิ่มการเรียก `convert_to_llm_tool` เพื่อแปลงคำตอบเครื่องมือ MCP เป็นข้อมูลที่จะส่งให้ LLM ในภายหลัง

#### .NET

1. เพิ่มโค้ดแปลงคำตอบเครื่องมือ MCP เป็นรูปแบบที่ LLM เข้าใจ

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

- สร้างฟังก์ชัน `ConvertFrom` ซึ่งรับชื่อ คำอธิบาย และสคีมาป้อนเข้า
- กำหนดฟังก์ชันซึ่งสร้าง `FunctionDefinition` ที่จะถูกส่งใน `ChatCompletionsDefinition` ซึ่งเป็นรูปแบบที่ LLM เข้าใจ

2. ดูวิธีอัปเดตโค้ดที่มีอยู่เพื่อใช้ฟังก์ชันนี้:

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
// สร้างอินเตอร์เฟสบอทสำหรับการโต้ตอบด้วยภาษาธรรมชาติ
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

- กำหนดอินเทอร์เฟส `Bot` ง่ายๆ สำหรับการโต้ตอบด้วยภาษาธรรมชาติ
- ใช้ `AiServices` ของ LangChain4j เพื่อผูก LLM กับผู้ให้บริการเครื่องมือ MCP อัตโนมัติ
- เฟรมเวิร์กจัดการการแปลงสคีมาของเครื่องมือและการเรียกฟังก์ชันเบื้องหลังให้อัตโนมัติ
- วิธีนี้ช่วยให้ไม่ต้องแปลงเครื่องมือด้วยมือ LangChain4j จะจัดการความซับซ้อนทั้งหมดของการแปลงเครื่องมือ MCP เป็นรูปแบบที่ LLM รองรับ

#### Rust

เพื่อแปลงคำตอบเครื่องมือ MCP เป็นรูปแบบที่ LLM เข้าใจ เราจะเพิ่มฟังก์ชันช่วยสำหรับจัดรูปแบบรายการเครื่องมือ เพิ่มโค้ดนี้ในไฟล์ `main.rs` ของคุณใต้ฟังก์ชัน `main` ฟังก์ชันนี้จะถูกเรียกเมื่อมีการส่งคำขอไปยัง LLM:

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

ดีมาก เราได้เตรียมพร้อมสำหรับจัดการคำขอผู้ใช้แล้ว ต่อไปมาดูวิธีจัดการกัน

### -4- จัดการคำขอพรอมต์ของผู้ใช้

ในส่วนโค้ดนี้ เราจะจัดการคำขอของผู้ใช้

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
    - เมธอดนี้รับตอบกลับจาก LLM และตรวจสอบว่าเครื่องมือใดถูกเรียกใช้บ้าง ถ้ามี:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // เรียกใช้เครื่องมือ
        }
        ```

    - เรียกใช้เครื่องมือถ้า LLM ระบุว่าควรเรียกใช้:

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

2. อัปเดตเมธอด `run` ให้รวมการเรียก LLM และเรียก `callTools`:

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

    // 3. ตรวจสอบการตอบกลับจาก LLM สำหรับแต่ละตัวเลือก ตรวจดูว่ามีการเรียกใช้เครื่องมือหรือไม่
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ดีมาก ลิสต์โค้ดทั้งหมด:

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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. ตรวจสอบการตอบกลับของ LLM ในแต่ละตัวเลือก ดูว่ามีการเรียกใช้เครื่องมือหรือไม่
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

2. ต่อไปเพิ่มฟังก์ชันที่จะเรียก LLM:

    ```python
    # แอลแอลเอ็ม

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
            # พารามิเตอร์ที่เป็นทางเลือก
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

    - ส่งผ่านฟังก์ชันของเราที่เราเจอบนเซิร์ฟเวอร์ MCP และแปลงแล้วให้กับ LLM
    - จากนั้นเรียกใช้ LLM ด้วยฟังก์ชันเหล่านั้น
    - ต่อมาเราตรวจสอบผลลัพธ์เพื่อดูว่าควรเรียกฟังก์ชันใดบ้าง ถ้ามี
    - สุดท้าย เราส่งอาร์เรย์ของฟังก์ชันเพื่อเรียกใช้

3. ขั้นตอนสุดท้าย อัปเดตโค้ดหลักของเรา:

    ```python
    prompt = "Add 2 to 20"

    # ถาม LLM ว่าควรใช้เครื่องมือใดบ้าง ถ้ามี
    functions_to_call = call_llm(prompt, functions)

    # เรียกฟังก์ชันที่แนะนำ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    นั่นคือขั้นตอนสุดท้าย ในโค้ดด้านบนนี้ เราได้:

    - เรียกเครื่องมือ MCP ผ่าน `call_tool` ด้วยฟังก์ชันที่ LLM คิดว่าควรเรียกตามพรอมต์ของเรา
    - พิมพ์ผลลัพธ์ของการเรียกเครื่องมือไปยังเซิร์ฟเวอร์ MCP

#### .NET

1. แสดงตัวอย่างโค้ดสำหรับการร้องขอพรอมต์ต่อ LLM:

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

    ในโค้ดก่อนหน้านี้ เราได้:

    - ดึงเครื่องมือจากเซิร์ฟเวอร์ MCP `var tools = await GetMcpTools()`
    - กำหนดพรอมต์ผู้ใช้ `userMessage`
    - สร้างอ็อบเจกต์ options ที่ระบุโมเดลและเครื่องมือ
    - ส่งคำขอไปยัง LLM

2. ขั้นตอนสุดท้าย ดูว่า LLM คิดว่าเราควรเรียกฟังก์ชันหรือไม่:

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

    - วนลูปรายการเรียกฟังก์ชัน
    - สำหรับแต่ละการเรียกเครื่องมือ แยกชื่อและอาร์กิวเมนต์ แล้วเรียกเครื่องมือบนเซิร์ฟเวอร์ MCP โดยใช้ไคลเอนต์ MCP จากนั้นพิมพ์ผลลัพธ์

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

// 6. Print the generic response
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

- ใช้พรอมต์ภาษาธรรมชาติง่ายๆ เพื่อโต้ตอบกับเครื่องมือของเซิร์ฟเวอร์ MCP
- เฟรมเวิร์ก LangChain4j ดูแลเรื่อง:
  - การแปลงพรอมต์ผู้ใช้เป็นการเรียกเครื่องมือเมื่อจำเป็น
  - การเรียกเครื่องมือ MCP ที่เหมาะสมตามการตัดสินใจของ LLM
  - การจัดการการไหลของบทสนทนาระหว่าง LLM กับเซิร์ฟเวอร์ MCP
- เมธอด `bot.chat()` ส่งผลลัพธ์เป็นการตอบกลับด้วยภาษาธรรมชาติที่อาจรวมผลลัพธ์จากการทำงานของเครื่องมือ MCP ด้วย
- วิธีนี้ให้ประสบการณ์ผู้ใช้ที่ราบรื่น โดยผู้ใช้ไม่จำเป็นต้องรู้เรื่องการประมวลผล MCP เบื้องหลัง

ตัวอย่างโค้ดสมบูรณ์:

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

#### Rust

ที่นี่เป็นที่ที่ส่วนใหญ่ของงานเกิดขึ้น เราจะเรียก LLM ด้วยพรอมต์ผู้ใช้เริ่มต้น จากนั้นประมวลผลคำตอบเพื่อดูว่าต้องเรียกใช้งานเครื่องมือใดหรือไม่ หากต้องเรียก เราจะเรียกใช้เครื่องมือเหล่านั้นและดำเนินการสนทนากับ LLM ต่อไปจนกว่าจะไม่มีคำขอเรียกเครื่องมือเพิ่มเติมและได้รับคำตอบสุดท้าย


เราจะเรียกใช้ LLM หลายครั้ง ดังนั้นให้เรากำหนดฟังก์ชันที่จะจัดการการเรียก LLM กันก่อน เพิ่มฟังก์ชันต่อไปนี้ลงในไฟล์ `main.rs` ของคุณ:

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

ฟังก์ชันนี้จะรับ client ของ LLM รายการข้อความ (รวมถึงข้อความจากผู้ใช้) เครื่องมือจาก MCP server แล้วส่งคำขอไปยัง LLM และส่งคืนคำตอบ

คำตอบจาก LLM จะมีอาเรย์ของ `choices` เราจะต้องประมวลผลผลลัพธ์เพื่อดูว่ามี `tool_calls` ปรากฏอยู่หรือไม่ ซึ่งจะบอกเราว่า LLM กำลังร้องขอให้เรียกเครื่องมือเฉพาะพร้อมกับอาร์กิวเมนต์ ใส่โค้ดต่อไปนี้ไว้ที่ด้านล่างของไฟล์ `main.rs` ของคุณเพื่อกำหนดฟังก์ชันจัดการการตอบกลับจาก LLM:

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

    // จัดการการเรียกเครื่องมือ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // เพิ่มข้อความผู้ช่วย

        // ดำเนินการเรียกเครื่องมือแต่ละรายการ
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

หากพบ `tool_calls` มันจะดึงข้อมูลเครื่องมือ เรียกใช้ MCP server ด้วยคำขอเครื่องมือนั้น และเพิ่มผลลัพธ์ลงในข้อความบทสนทนา จากนั้นจะดำเนินการสนทนาต่อกับ LLM และข้อความจะได้รับการอัปเดตด้วยคำตอบของผู้ช่วยและผลลัพธ์จากการเรียกเครื่องมือ

เพื่อดึงข้อมูลการเรียกเครื่องมือที่ LLM ส่งกลับสำหรับการเรียก MCP เราจะเพิ่มฟังก์ชันช่วยเหลืออีกตัวเพื่อดึงทุกสิ่งที่จำเป็นสำหรับการเรียกนั้น เพิ่มโค้ดต่อไปนี้ไว้ที่ด้านล่างของไฟล์ `main.rs` ของคุณ:

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

ด้วยทุกส่วนที่พร้อมแล้ว เราสามารถจัดการกับข้อความเริ่มต้นของผู้ใช้และเรียก LLM ได้ อัปเดตฟังก์ชัน `main` ของคุณให้รวมโค้ดต่อไปนี้:

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

โค้ดนี้จะสอบถาม LLM ด้วยข้อความเริ่มต้นของผู้ใช้ที่ถามหาผลรวมของตัวเลขสองตัว และจะประมวลผลคำตอบเพื่อจัดการการเรียกเครื่องมือแบบไดนามิก

เยี่ยมมาก คุณทำได้แล้ว!

## การบ้าน

นำโค้ดจากแบบฝึกหัดนี้ไปสร้างเซิร์ฟเวอร์พร้อมด้วยเครื่องมือเพิ่มขึ้น จากนั้นสร้าง client ที่มี LLM เหมือนในแบบฝึกหัดและทดสอบด้วยคำถามต่าง ๆ เพื่อให้แน่ใจว่าเครื่องมือทั้งหมดในเซิร์ฟเวอร์ของคุณถูกเรียกแบบไดนามิก วิธีการสร้าง client แบบนี้หมายความว่าผู้ใช้ปลายทางจะได้รับประสบการณ์ที่ดี เพราะพวกเขาสามารถใช้ข้อความคำสั่งแทนที่จะเป็นคำสั่งเฉพาะของ client และไม่ต้องสนใจว่า MCP server ใดจะถูกเรียกใช้งาน

## ตัวอย่างคำตอบ

[Solution](./solution/README.md)

## ประเด็นสำคัญที่ต้องจดจำ

- การเพิ่ม LLM เข้าไปใน client ช่วยให้ผู้ใช้มีวิธีที่ดีกว่าในการโต้ตอบกับ MCP Servers
- คุณต้องแปลงการตอบกลับของ MCP Server ให้เป็นสิ่งที่ LLM เข้าใจได้

## ตัวอย่าง

- [เครื่องคิดเลข Java](../samples/java/calculator/README.md)
- [เครื่องคิดเลข .Net](../../../../03-GettingStarted/samples/csharp)
- [เครื่องคิดเลข JavaScript](../samples/javascript/README.md)
- [เครื่องคิดเลข TypeScript](../samples/typescript/README.md)
- [เครื่องคิดเลข Python](../../../../03-GettingStarted/samples/python)
- [เครื่องคิดเลข Rust](../../../../03-GettingStarted/samples/rust)

## แหล่งข้อมูลเพิ่มเติม

## ต่อไป

- ถัดไป: [การใช้งานเซิร์ฟเวอร์ด้วย Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->