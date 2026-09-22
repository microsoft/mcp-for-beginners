# การสร้างไคลเอนต์ด้วย LLM

> [!NOTE]
> ตัวอย่างไคลเอนต์ Java เชื่อมต่อผ่านการส่งข้อมูลแบบ HTTP+SSE แบบเก่าและ
> มีเป้าหมาย MCP `2025-11-25` SDK API ใช้ SDK ที่เข้ากันได้กับ `2026-07-28` และ
> Streamable HTTP สำหรับไคลเอนต์ระยะไกลใหม่

จนถึงตอนนี้ คุณเห็นวิธีสร้างเซิร์ฟเวอร์และไคลเอนต์ ไคลเอนต์สามารถเรียกใช้เซิร์ฟเวอร์โดยตรงเพื่อแสดงรายการเครื่องมือ ทรัพยากร และพรอมต์ อย่างไรก็ตาม วิธีนี้ไม่ใช่วิธีที่ใช้งานได้จริงมากนัก ผู้ใช้ของคุณอยู่ในยุคของเอเจนต์ิกและคาดหวังที่จะใช้พรอมต์และสื่อสารกับ LLM แทน พวกเขาไม่สนใจว่าคุณจะใช้ MCP ในการเก็บความสามารถของคุณหรือไม่; พวกเขาคาดหวังที่จะโต้ตอบโดยใช้ภาษาธรรมชาติ แล้วเราจะแก้ไขปัญหานี้อย่างไร? วิธีแก้คือการเพิ่ม LLM ลงในไคลเอนต์

## ภาพรวม

ในบทเรียนนี้ เราจะเน้นการเพิ่ม LLM ให้กับไคลเอนต์ของคุณและแสดงให้เห็นว่าสิ่งนี้ช่วยให้ประสบการณ์ของผู้ใช้ดีขึ้นมากอย่างไร

## วัตถุประสงค์การเรียนรู้

เมื่อสิ้นสุดบทเรียนนี้ คุณจะสามารถ:

- สร้างไคลเอนต์ที่มี LLM
- โต้ตอบกับเซิร์ฟเวอร์ MCP อย่างราบรื่นโดยใช้ LLM
- มอบประสบการณ์ผู้ใช้ที่ดีกว่าฝั่งไคลเอนต์

## วิธีการ

มาลองทำความเข้าใจวิธีการที่เราต้องดำเนินการ การเพิ่ม LLM ฟังดูง่าย แต่เราจะทำจริง ๆ หรือไม่?

นี่คือวิธีที่ไคลเอนต์จะโต้ตอบกับเซิร์ฟเวอร์:

1. สร้างการเชื่อมต่อกับเซิร์ฟเวอร์

1. แสดงรายการความสามารถ พรอมต์ ทรัพยากร และเครื่องมือ แล้วบันทึกสคีมาของพวกมันลงไป

1. เพิ่ม LLM และส่งความสามารถที่บันทึกไว้พร้อมสคีมาในรูปแบบที่ LLM เข้าใจ

1. จัดการพรอมต์ของผู้ใช้โดยส่งต่อไปยัง LLM รวมกับเครื่องมือที่ไคลเอนต์แสดงไว้

ดีมาก ตอนนี้เราเข้าใจภาพรวมของกระบวนการแล้ว มาลองทำแบบฝึกหัดด้านล่างกัน

## แบบฝึกหัด: การสร้างไคลเอนต์ด้วย LLM

ในแบบฝึกหัดนี้ เราจะเรียนรู้การเพิ่ม LLM ให้กับไคลเอนต์ของเรา

### การรับรองความถูกต้องโดยใช้ GitHub Personal Access Token

การสร้างโทเค็น GitHub นั้นเป็นกระบวนการง่าย ๆ นี่คือวิธีที่คุณสามารถทำได้:

- ไปที่การตั้งค่า GitHub – คลิกที่รูปโปรไฟล์ของคุณที่มุมขวาบนแล้วเลือก Settings
- ไปที่ Developer Settings – เลื่อนลงมาแล้วคลิกที่ Developer Settings
- เลือก Personal Access Tokens – คลิกที่ Fine-grained tokens แล้วกด Generate new token
- กำหนดค่าโทเค็นของคุณ – เพิ่มหมายเหตุเพื่ออ้างอิง กำหนดวันหมดอายุ และเลือกสโคป (สิทธิ์) ที่จำเป็น ในกรณีนี้ให้แน่ใจว่าได้เพิ่มสิทธิ์ Models
- สร้างและคัดลอกโทเค็น – คลิก Generate token แล้วอย่าลืมคัดลอกทันที เพราะคุณจะไม่สามารถเห็นมันอีก

### -1- เชื่อมต่อไปยังเซิร์ฟเวอร์

มาเริ่มสร้างไคลเอนต์ของเราก่อน:

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

ในโค้ดข้างต้น เราได้:

- นำเข้าห้องสมุดที่จำเป็น
- สร้างคลาสที่มีสมาชิกสองตัวคือ `client` และ `openai` ที่ช่วยให้เราจัดการไคลเอนต์และโต้ตอบกับ LLM ตามลำดับ
- กำหนดค่าอินสแตนซ์ LLM ของเราให้ใช้ GitHub Models โดยตั้งค่า `baseUrl` ให้ชี้ไปยัง API อินเฟอเรนซ์

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# สร้างพารามิเตอร์เซิร์ฟเวอร์สำหรับการเชื่อมต่อ stdio
server_params = StdioServerParameters(
    command="mcp",  # ไฟล์ที่สามารถรันได้
    args=["run", "server.py"],  # อาร์กิวเมนต์บรรทัดคำสั่งที่ไม่บังคับ
    env=None,  # ตัวแปรสภาพแวดล้อมที่ไม่จำเป็น
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

ในโค้ดข้างต้น เราได้:

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

ก่อนอื่น คุณต้องเพิ่ม dependencies ของ LangChain4j ลงในไฟล์ `pom.xml` ของคุณ เพิ่ม dependencies เหล่านี้เพื่อเปิดใช้งานการรวม MCP และ API MiniMax ที่เข้ากันได้กับ OpenAI:

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

ตั้งค่า MiniMax API key ของคุณ และถ้าต้องการ ตั้งค่า endpoint และ model ด้วย
`MINIMAX_MODEL_ID` รองรับ `MiniMax-M3` และ `MiniMax-M2.7` ถ้า
`OPENAI_BASE_URL` ไม่ถูกตั้งค่า `MINIMAX_REGION` รองรับ `global_en` และ `cn_zh`

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

เพื่อเลือก endpoint ตามภูมิภาคแทน ให้ละเว้น `OPENAI_BASE_URL`:

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

ในโค้ดข้างต้นเราได้:

- **เพิ่ม dependencies ของ LangChain4j**: จำเป็นสำหรับการรวม MCP และ API MiniMax ที่เข้ากันได้กับ OpenAI
- **นำเข้าไลบรารีของ LangChain4j**: สำหรับการรวม MCP และฟังก์ชันแชทโมเดล OpenAI
- **สร้าง `ChatLanguageModel`**: กำหนดค่าให้ใช้ MiniMax พร้อมกับ MiniMax API key, endpoint และ model ID ที่รองรับของคุณ
- **ตั้งค่าการส่งข้อมูล HTTP**: ใช้ Server-Sent Events (SSE) เพื่อเชื่อมต่อกับเซิร์ฟเวอร์ MCP
- **สร้างไคลเอนต์ MCP**: ที่จะจัดการการสื่อสารกับเซิร์ฟเวอร์
- **ใช้การสนับสนุน MCP ในตัวของ LangChain4j**: ที่ช่วยให้ง่ายต่อการรวม LLM และเซิร์ฟเวอร์ MCP

#### Rust

ตัวอย่างนี้สมมติว่าคุณมีเซิร์ฟเวอร์ MCP ที่ใช้ Rust ทำงานอยู่ หากคุณยังไม่มี ให้กลับไปดูบทเรียน [01-first-server](../01-first-server/README.md) เพื่อสร้างเซิร์ฟเวอร์

เมื่อคุณมีเซิร์ฟเวอร์ MCP Rust แล้ว เปิดเทอร์มินัลและไปที่ไดเรกทอรีเดียวกับเซิร์ฟเวอร์ จากนั้นรันคำสั่งนี้เพื่อสร้างโปรเจกต์ไคลเอนต์ LLM ใหม่:

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
> ยังไม่มีไลบรารี Rust อย่างเป็นทางการสำหรับ OpenAI อย่างไรก็ตาม crate `async-openai` เป็น [ไลบรารีที่ชุมชนดูแล](https://platform.openai.com/docs/libraries/rust#rust) ซึ่งถูกใช้กันทั่วไป

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

    // TODO: การสนทนา LLM กับการเรียกใช้เครื่องมือ

    Ok(())
}
```

โค้ดนี้ตั้งค่าแอปพลิเคชัน Rust พื้นฐานที่จะเชื่อมต่อกับเซิร์ฟเวอร์ MCP และ GitHub Models สำหรับการโต้ตอบกับ LLM

> [!IMPORTANT]
> อย่าลืมตั้งค่าตัวแปรสภาพแวดล้อม `OPENAI_API_KEY` ด้วยโทเค็น GitHub ของคุณก่อนรันแอปพลิเคชัน

ดีมาก สำหรับก้าวต่อไป มาลองแสดงรายการความสามารถบนเซิร์ฟเวอร์กัน

### -2- แสดงรายการความสามารถของเซิร์ฟเวอร์

ตอนนี้เราจะเชื่อมต่อไปยังเซิร์ฟเวอร์และขอข้อมูลความสามารถ:

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

    // เครื่องมือการแสดงรายการ
    const toolsResult = await this.client.listTools();
}
```

ในโค้ดข้างต้นเราได้:

- เพิ่มโค้ดสำหรับเชื่อมต่อไปยังเซิร์ฟเวอร์ `connectToServer`
- สร้างเมธอด `run` ที่รับผิดชอบควบคุมการทำงานของแอปฯ ตอนนี้มันแสดงเฉพาะรายการเครื่องมือ แต่เราจะเพิ่มฟังก์ชันอื่น ๆ ในไม่นาน

#### Python

```python
# แสดงรายการทรัพยากรที่มี
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# แสดงรายการเครื่องมือที่มี
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

สิ่งที่เราเพิ่มคือ:

- แสดงรายการทรัพยากรและเครื่องมือ และพิมพ์ออกมา สำหรับเครื่องมือ เราแสดง `inputSchema` ด้วยซึ่งจะนำมาใช้ต่อไป

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

- ระบุเครื่องมือที่มีใน MCP Server
- สำหรับแต่ละเครื่องมือ ระบุชื่อ คำอธิบาย และโครงร่างของมัน สิ่งหลังนี้จะใช้ในการเรียกเครื่องมือเร็วๆ นี้

#### Java

```java
// สร้างผู้ให้บริการเครื่องมือที่ค้นหาเครื่องมือ MCP โดยอัตโนมัติ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ผู้ให้บริการเครื่องมือ MCP จะจัดการโดยอัตโนมัติ:
// - การแสดงรายการเครื่องมือที่มีจากเซิร์ฟเวอร์ MCP
// - การแปลงสกีม่าเครื่องมือ MCP เป็นรูปแบบ LangChain4j
// - การจัดการการทำงานของเครื่องมือและการตอบกลับ
```

ในโค้ดก่อนหน้านี้เราได้:

- สร้าง `McpToolProvider` ที่ค้นหาและลงทะเบียนเครื่องมือทั้งหมดจาก MCP server โดยอัตโนมัติ
- ตัวจัดห่าเครื่องมือจัดการการแปลงระหว่างโครงร่างของเครื่องมือ MCP กับรูปแบบเครื่องมือของ LangChain4j ภายใน
- วิธีนี้ปกปิดกระบวนการระบุและแปลงเครื่องมือด้วยตนเอง

#### Rust

การดึงข้อมูลเครื่องมือจาก MCP server ทำได้โดยใช้เมธอด `list_tools` ในฟังก์ชัน `main` ของคุณ หลังจากตั้งค่า MCP client แล้ว ให้เพิ่มโค้ดดังนี้:

```rust
// ดึงรายการเครื่องมือ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- แปลงความสามารถของเซิร์ฟเวอร์เป็นเครื่องมือ LLM

ขั้นตอนต่อไปหลังจากการระบุความสามารถของเซิร์ฟเวอร์คือการแปลงให้เป็นรูปแบบที่ LLM เข้าใจ เมื่อทำเสร็จแล้วเราสามารถให้ความสามารถเหล่านั้นเป็นเครื่องมือแก่ LLM ได้

#### TypeScript

1. เพิ่มโค้ดต่อไปนี้เพื่อแปลงการตอบสนองจาก MCP Server เป็นรูปแบบเครื่องมือที่ LLM ใช้งานได้:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // สร้างสคีมา zod โดยอิงจาก input_schema
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

    โค้ดข้างต้นนำการตอบสนองจาก MCP Server มาแปลงเป็นรูปแบบคำจำกัดความเครื่องมือที่ LLM เข้าใจ

2. ต่อไปมาอัปเดตเมธอด `run` เพื่อระบุความสามารถของเซิร์ฟเวอร์:

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

    ในโค้ดก่อนหน้านี้เราอัปเดตเมธอด `run` เพื่อเข้าถึงผลลัพธ์และเรียก `openAiToolAdapter` สำหรับแต่ละรายการ

#### Python

1. ก่อนอื่น มาสร้างฟังก์ชันแปลงดังนี้

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

    ในฟังก์ชัน `convert_to_llm_tools` ข้างต้น เรานำการตอบสนองเครื่องมือจาก MCP มาแปลงเป็นรูปแบบที่ LLM เข้าใจ

2. ต่อไปอัปเดตโค้ด client เพื่อใช้ฟังก์ชันนี้ ดังนี้:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ที่นี่ เราเพิ่มการเรียก `convert_to_llm_tool` เพื่อแปลงการตอบสนองเครื่องมือ MCP เป็นสิ่งที่เราสามารถส่งไปยัง LLM ได้ในภายหลัง

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

ในโค้ดก่อนหน้านี้เราได้:

- สร้างฟังก์ชัน `ConvertFrom` ที่รับชื่อ คำอธิบาย และโครงร่างอินพุต
- กำหนดฟังก์ชันที่สร้าง FunctionDefinition และส่งไปยัง ChatCompletionsDefinition ซึ่งเป็นสิ่งที่ LLM เข้าใจ

2. มาดูวิธีอัปเดตโค้ดที่มีเพื่อใช้ฟังก์ชันนี้กัน:

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

- กำหนดอินเทอร์เฟซ `Bot` อย่างง่ายสำหรับการโต้ตอบด้วยภาษาธรรมชาติ
- ใช้ `AiServices` ของ LangChain4j เพื่อเชื่อมต่อ LLM กับผู้ให้บริการเครื่องมือ MCP โดยอัตโนมัติ
- เฟรมเวิร์กจัดการการแปลงโครงร่างเครื่องมือและการเรียกฟังก์ชันเบื้องหลังโดยอัตโนมัติ
- วิธีนี้ขจัดความยุ่งยากในการแปลงเครื่องมือด้วยตนเอง เพราะ LangChain4j ดูแลการแปลงเครื่องมือ MCP เป็นรูปแบบที่ใช้กับ LLM ได้ทั้งหมด

#### Rust

ในการแปลงการตอบสนองเครื่องมือ MCP เป็นรูปแบบที่ LLM เข้าใจ เราจะเพิ่มฟังก์ชันช่วยที่จะจัดรูปแบบรายการเครื่องมือ เพิ่มโค้ดต่อไปนี้ในไฟล์ `main.rs` ของคุณใต้ฟังก์ชัน `main` ฟังก์ชันนี้จะถูกเรียกเมื่อต้องการส่งคำขอไปยัง LLM:

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

ดีแล้ว เราได้ตั้งค่าพร้อมสำหรับรับคำขอจากผู้ใช้ ดังนั้นเรามาจัดการส่วนนี้กันต่อ

### -4- จัดการคำขอพรอมต์จากผู้ใช้

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
        // งานที่ต้องทำ

        }
    }
    ```

    ในโค้ดก่อนหน้านี้เราได้:

    - เพิ่มเมธอด `callTools`
    - เมธอดนี้รับการตอบสนองจาก LLM และตรวจสอบว่าเครื่องมือใดถูกเรียกใช้งานหรือไม่

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // เรียกใช้เครื่องมือ
        }
        ```

    - เรียกใช้เครื่องมือ หาก LLM ระบุว่าควรเรียกใช้

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

2. อัปเดตเมธอด `run` ให้รวมการเรียกไปยัง LLM และการเรียก `callTools`:

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

    // 3. ตรวจสอบคำตอบจาก LLM สำหรับแต่ละตัวเลือกว่า มีการเรียกใช้เครื่องมือหรือไม่
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ดีแล้ว มาดูโค้ดเต็มกัน:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // นำเข้า zod สำหรับตรวจสอบสคีมา

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
            type: "function" as const, // กำหนด type เป็น "function" อย่างชัดเจน
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
    
        // 3. ตรวจสอบผลตอบกลับจาก LLM สำหรับแต่ละตัวเลือก ตรวจสอบว่ามีการเรียกใช้เครื่องมือหรือไม่
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

1. เพิ่มการนำเข้าบางอย่างที่จำเป็นในการเรียก LLM

    ```python
    # โมเดลภาษาใหญ่
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. ต่อมาเพิ่มฟังก์ชันที่จะเรียก LLM:

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
            # พารามิเตอร์เสริมเลือกใช้ได้
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

    - ส่งผ่านฟังก์ชันที่เราค้นพบจาก MCP server และแปลงแล้วไปยัง LLM
    - จากนั้นเรียก LLM พร้อมฟังก์ชันเหล่านั้น
    - แล้วตรวจสอบผลลัพธ์เพื่อดูว่าควรเรียกฟังก์ชันใดบ้าง ถ้ามี
    - สุดท้ายส่งอาร์เรย์ฟังก์ชันที่ต้องเรียก

3. ขั้นตอนสุดท้าย อัปเดตโค้ดหลักของเรา:

    ```python
    prompt = "Add 2 to 20"

    # ถาม LLM ว่ามีเครื่องมืออะไรให้ใช้บ้าง ถ้ามี
    functions_to_call = call_llm(prompt, functions)

    # เรียกใช้ฟังก์ชันที่แนะนำ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    นั่นคือขั้นตอนสุดท้าย ในโค้ดข้างต้นเราได้:

    - เรียกใช้เครื่องมือ MCP ผ่าน `call_tool` โดยใช้ฟังก์ชันที่ LLM คิดว่าเราควรเรียกตามพรอมต์ของเรา
    - พิมพ์ผลลัพธ์จากการเรียกเครื่องมือไปยัง MCP Server

#### .NET

1. มาดูโค้ดสำหรับการส่งพรอมต์คำขอไปยัง LLM:

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

    - ดึงเครื่องมือจาก MCP server ด้วย `var tools = await GetMcpTools()`
    - กำหนดพรอมต์ของผู้ใช้ `userMessage`
    - สร้างอ็อบเจกต์ options ที่ระบุโมเดลและเครื่องมือ
    - ส่งคำขอไปยัง LLM

2. ขั้นตอนสุดท้าย มาดูว่า LLM คิดว่าเราควรเรียกฟังก์ชันใดหรือไม่:

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
    - สำหรับแต่ละการเรียกเครื่องมือ แยกชื่อและอาร์กิวเมนต์แล้วเรียกเครื่องมือบน MCP server ผ่าน MCP client สุดท้ายพิมพ์ผลลัพธ์

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

ในโค้ดก่อนหน้านี้เราได้:

- ใช้พรอมต์ภาษาธรรมชาติอย่างง่ายเพื่อโต้ตอบกับเครื่องมือ MCP server
- เฟรมเวิร์ก LangChain4j จัดการโดยอัตโนมัติ:
  - แปลงพรอมต์ผู้ใช้เป็นการเรียกเครื่องมือเมื่อจำเป็น
  - เรียกใช้งานเครื่องมือ MCP ที่เหมาะสมตามการตัดสินใจของ LLM
  - จัดการการไหลของการสนทนาระหว่าง LLM กับ MCP server
- เมธอด `bot.chat()` คืนค่าการตอบสนองภาษาธรรมชาติที่อาจรวมผลลัพธ์จากการรันเครื่องมือ MCP
- วิธีนี้มอบประสบการณ์ผู้ใช้ที่ราบรื่นซึ่งไม่ต้องรู้เรื่องการทำงานภายในของ MCP

ตัวอย่างโค้ดครบถ้วน:

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


นี่คือจุดที่การทำงานส่วนใหญ่เกิดขึ้น เราจะเรียกใช้งาน LLM ด้วยพรอมต์ผู้ใช้เริ่มต้น จากนั้นประมวลผลการตอบกลับเพื่อดูว่าจำเป็นต้องเรียกใช้เครื่องมือใดๆ หรือไม่ หากใช่ เราจะเรียกใช้เครื่องมือเหล่านั้นและดำเนินการสนทนาต่อกับ LLM จนไม่ต้องเรียกใช้เครื่องมือเพิ่มเติมและเราได้คำตอบสุดท้าย

เราจะเรียก LLM หลายครั้ง ดังนั้นมาสร้างฟังก์ชันที่จัดการการเรียก LLM กัน เพิ่มฟังก์ชันต่อไปนี้ลงในไฟล์ `main.rs` ของคุณ:

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

ฟังก์ชันนี้รับลูกค้า LLM รายการข้อความ (รวมถึงพรอมต์ผู้ใช้) เครื่องมือจากเซิร์ฟเวอร์ MCP และส่งคำขอไปยัง LLM พร้อมส่งกลับผลลัพธ์

การตอบกลับจาก LLM จะมีอาร์เรย์ของ `choices` เราต้องประมวลผลผลลัพธ์เพื่อดูว่ามี `tool_calls` หรือไม่ ซึ่งบอกเราว่า LLM กำลังขอเรียกใช้เครื่องมือเฉพาะพร้อมอาร์กิวเมนต์หรือไม่ เพิ่มโค้ดต่อไปนี้ไปที่ส่วนล่างของไฟล์ `main.rs` ของคุณเพื่อกำหนดฟังก์ชันสำหรับจัดการการตอบกลับของ LLM:

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

    // พิมพ์เนื้อหาหากมีพร้อมใช้งาน
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // จัดการการเรียกใช้งานเครื่องมือ
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

หากพบ `tool_calls` จะดึงข้อมูลเครื่องมือ เรียกเซิร์ฟเวอร์ MCP ด้วยคำขอเครื่องมือ และเพิ่มผลลัพธ์ลงในข้อความสนทนา จากนั้นดำเนินการสนทนาต่อกับ LLM ข้อความจะได้รับการอัปเดตด้วยคำตอบของผู้ช่วยและผลลัพธ์การเรียกเครื่องมือ

เพื่อดึงข้อมูลการเรียกเครื่องมือที่ LLM ส่งคืนสำหรับการเรียก MCP เราจะเพิ่มฟังก์ชันช่วยเพิ่มเติมเพื่อดึงทุกอย่างที่จำเป็นสำหรับการเรียก เพิ่มโค้ดต่อไปนี้ลงในส่วนล่างของไฟล์ `main.rs` ของคุณ:

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

เมื่อทุกส่วนถูกวางแล้ว เราสามารถจัดการพรอมต์ผู้ใช้เริ่มต้นและเรียก LLM ได้แล้ว ปรับปรุงฟังก์ชัน `main` ของคุณให้รวมโค้ดต่อไปนี้:

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

นี้จะส่งคำถามไปยัง LLM ด้วยพรอมต์ผู้ใช้เริ่มต้นที่ถามหาผลบวกของตัวเลขสองตัว และจะประมวลผลการตอบกลับเพื่อจัดการการเรียกเครื่องมือแบบไดนามิก

ดีมาก คุณทำสำเร็จแล้ว!

## งานที่ได้รับมอบหมาย

นำโค้ดจากแบบฝึกหัดไปสร้างเซิร์ฟเวอร์ที่มีเครื่องมือเพิ่มเติม จากนั้นสร้างไคลเอนต์ที่มี LLM เหมือนในแบบฝึกหัด และทดสอบด้วยพรอมต์ต่างๆ เพื่อให้แน่ใจว่าเครื่องมือทั้งหมดบนเซิร์ฟเวอร์ของคุณถูกเรียกใช้แบบไดนามิก การสร้างไคลเอนต์แบบนี้ทำให้ผู้ใช้ปลายทางมีประสบการณ์ที่ดีเพราะสามารถใช้พรอมต์แทนคำสั่งไคลเอนต์ที่แน่นอนได้ และไม่รู้สึกถึงการเรียกใช้เซิร์ฟเวอร์ MCP ใดๆ

## วิธีแก้ปัญหา

[วิธีแก้ปัญหา](./solution/README.md)

## ข้อสรุปสำคัญ

- การเพิ่ม LLM ในไคลเอนต์ของคุณช่วยให้ผู้ใช้โต้ตอบกับเซิร์ฟเวอร์ MCP ได้วิธีที่ดีขึ้น
- คุณต้องแปลงการตอบกลับของเซิร์ฟเวอร์ MCP ให้เป็นสิ่งที่ LLM เข้าใจได้

## ตัวอย่าง

- [เครื่องคิดเลข Java](../samples/java/calculator/README.md)
- [เครื่องคิดเลข .Net](../../../../03-GettingStarted/samples/csharp)
- [เครื่องคิดเลข JavaScript](../samples/javascript/README.md)
- [เครื่องคิดเลข TypeScript](../samples/typescript/README.md)
- [เครื่องคิดเลข Python](../../../../03-GettingStarted/samples/python)
- [เครื่องคิดเลข Rust](../../../../03-GettingStarted/samples/rust)

## แหล่งข้อมูลเพิ่มเติม

## สิ่งถัดไป

- ต่อไป: [การใช้งานเซิร์ฟเวอร์ด้วย Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->