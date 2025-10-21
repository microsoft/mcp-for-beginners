<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "726b74589522653d930c7395c9e1fab8",
  "translation_date": "2025-10-20T17:18:11+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "my"
}
-->
# MCP စတင်အသုံးပြုခြင်း

Model Context Protocol (MCP) နှင့် စတင်လေ့လာရန် ကြိုဆိုပါတယ်! MCP အသစ်ဖြစ်စေ၊ MCP ကို နက်နက်ရှိုင်းရှိုင်းနားလည်လိုစေ၊ ဒီလမ်းညွှန်စာအုပ်က သင့်ကို အရေးကြီးသော စနစ်တပ်ဆင်ခြင်းနှင့် ဖွံ့ဖြိုးတိုးတက်မှု လုပ်ငန်းစဉ်များကို လမ်းညွှန်ပေးပါမည်။ MCP သည် AI မော်ဒယ်များနှင့် အက်ပလီကေးရှင်းများအကြား အဆင်ပြေစွာ ပေါင်းစည်းမှုကို ဘယ်လိုဖြစ်စေတယ်ဆိုတာကို ရှာဖွေတွေ့ရှိပြီး MCP-powered ဖြေရှင်းချက်များကို တည်ဆောက်ခြင်းနှင့် စမ်းသပ်ခြင်းအတွက် သင့်ပတ်ဝန်းကျင်ကို အလျင်အမြန် ပြင်ဆင်နိုင်ရန် လေ့လာပါ။

> TLDR; သင် AI အက်ပလီကေးရှင်းများကို တည်ဆောက်ပါက LLM (large language model) ကို ပိုမိုအသိပညာရှိစေရန် အထောက်အကူပစ္စည်းများနှင့် အခြားအရင်းအမြစ်များကို ထည့်သွင်းနိုင်သည်ကို သင်သိပါသည်။ သို့သော် အထောက်အကူပစ္စည်းများနှင့် အရင်းအမြစ်များကို server ပေါ်တွင်ထားပါက အက်ပလီကေးရှင်းနှင့် server ၏ စွမ်းရည်များကို LLM ရှိ/မရှိ သုံးစွဲသူများအားလုံး အသုံးပြုနိုင်ပါသည်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာက MCP ပတ်ဝန်းကျင်များကို တပ်ဆင်ခြင်းနှင့် သင့်ရဲ့ ပထမဆုံး MCP အက်ပလီကေးရှင်းများကို တည်ဆောက်ခြင်းအတွက် လက်တွေ့လမ်းညွှန်ချက်များပေးပါမည်။ MCP server များကို အခြေခံပုံစံဖြင့် တည်ဆောက်ခြင်း၊ host applications များကို ဖန်တီးခြင်းနှင့် သင့်ရဲ့ အကောင်အထည်ဖော်မှုများကို စမ်းသပ်ခြင်းတို့ကို လေ့လာပါမည်။

Model Context Protocol (MCP) သည် LLM များကို context ပေးရန် အက်ပလီကေးရှင်းများကို စံပြလုပ်ပုံကို သတ်မှတ်ပေးသော open protocol တစ်ခုဖြစ်သည်။ MCP ကို AI အက်ပလီကေးရှင်းများအတွက် USB-C port တစ်ခုလိုပဲ စဉ်ဆက်မပြတ် data sources နှင့် tools များကို ချိတ်ဆက်ပေးသော စံပြနည်းလမ်းတစ်ခုအဖြစ် စဉ်းစားပါ။

## သင်ယူရမည့်ရည်ရွယ်ချက်များ

ဒီသင်ခန်းစာအဆုံးတွင် သင်သည် အောက်ပါအရာများကို လုပ်နိုင်ပါမည်-

- C#, Java, Python, TypeScript, Rust တို့တွင် MCP အတွက် ဖွံ့ဖြိုးတိုးတက်မှု ပတ်ဝန်းကျင်များကို တပ်ဆင်ခြင်း
- အထောက်အကူပစ္စည်းများ၊ prompts နှင့် tools များပါဝင်သော အခြေခံ MCP server များကို တည်ဆောက်ပြီး deploy လုပ်ခြင်း
- MCP server များနှင့် ချိတ်ဆက်သော host applications များကို ဖန်တီးခြင်း
- MCP အကောင်အထည်ဖော်မှုများကို စမ်းသပ်ခြင်းနှင့် debugging လုပ်ခြင်း

## MCP ပတ်ဝန်းကျင်ကို တပ်ဆင်ခြင်း

MCP နှင့် အလုပ်လုပ်ရန် မစတင်မီ သင့်ဖွံ့ဖြိုးတိုးတက်မှု ပတ်ဝန်းကျင်ကို ပြင်ဆင်ပြီး workflow အခြေခံကို နားလည်ရန် အရေးကြီးသည်။ ဒီအပိုင်းက MCP နှင့် စတင်အလုပ်လုပ်ရန် အဆင်ပြေစေရန် အစပိုင်းအဆင့်များကို လမ်းညွှန်ပေးပါမည်။

### လိုအပ်ချက်များ

MCP ဖွံ့ဖြိုးတိုးတက်မှုကို စတင်မီ သင့်တွင် အောက်ပါအရာများရှိကြောင်း သေချာပါစေ-

- **ဖွံ့ဖြိုးတိုးတက်မှု ပတ်ဝန်းကျင်**: သင်ရွေးချယ်ထားသော ဘာသာစကား (C#, Java, Python, TypeScript, Rust) အတွက်
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, သို့မဟုတ် ခေတ်မီ code editor များ
- **Package Managers**: NuGet, Maven/Gradle, pip, npm/yarn, Cargo
- **API Keys**: Host applications တွင် အသုံးပြုမည့် AI services များအတွက်

## အခြေခံ MCP Server ဖွဲ့စည်းပုံ

MCP server တစ်ခုတွင် အောက်ပါအရာများပါဝင်သည်-

- **Server Configuration**: Port, authentication နှင့် အခြား settings များကို တပ်ဆင်ခြင်း
- **Resources**: LLM များအတွက် ရရှိနိုင်သော data နှင့် context
- **Tools**: မော်ဒယ်များက invoke လုပ်နိုင်သော လုပ်ဆောင်ချက်များ
- **Prompts**: Text ကို ဖန်တီးခြင်း သို့မဟုတ် ဖွဲ့စည်းပုံအတွက် templates

TypeScript ဖြင့် ရိုးရှင်းသော ဥပမာတစ်ခုမှာ-

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
server.resource(
  "file",
  // The 'list' parameter controls how the resource lists available files. Setting it to undefined disables listing for this resource.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Add a file resource that reads the file contents
server.resource(
  "file",
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => {
    let text;
    try {
      text = await fs.readFile(path, "utf8");
    } catch (err) {
      text = `Error reading file: ${err.message}`;
    }
    return {
      contents: [{
        uri: uri.href,
        text
      }]
    };
  }
);

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

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

အထက်ပါ code တွင်-

- MCP TypeScript SDK မှ လိုအပ်သော classes များကို import လုပ်ပါသည်။
- MCP server instance အသစ်တစ်ခုကို ဖန်တီးပြီး configure လုပ်ပါသည်။
- Handler function ပါသော custom tool (`calculator`) ကို register လုပ်ပါသည်။
- MCP requests များကို နားထောင်ရန် server ကို စတင်ပါသည်။

## စမ်းသပ်ခြင်းနှင့် Debugging

MCP server ကို စမ်းသပ်မတိုင်မီ debugging အတွက် ရရှိနိုင်သော tools များနှင့် အကောင်းဆုံးလေ့ကျင့်မှုများကို နားလည်ရန် အရေးကြီးသည်။ ထိရောက်သော စမ်းသပ်မှုသည် သင့် server သည် မျှော်လင့်ထားသည့်အတိုင်း လုပ်ဆောင်မှုရှိကြောင်း သေချာစေပြီး ပြဿနာများကို အလျင်အမြန် ရှာဖွေပြီး ဖြေရှင်းနိုင်စေသည်။ အောက်ပါအပိုင်းတွင် MCP အကောင်အထည်ဖော်မှုကို အတည်ပြုရန် အကြံပြုထားသော လမ်းလျှောက်မှုများကို ဖော်ပြထားသည်။

MCP သည် သင့် server များကို စမ်းသပ်ခြင်းနှင့် debugging လုပ်ရန် အထောက်အကူပစ္စည်းများကို ပေးသည်-

- **Inspector tool**: ဒီ graphical interface က သင့် server ကို ချိတ်ဆက်ပြီး tools, prompts, resources များကို စမ်းသပ်နိုင်သည်။
- **curl**: Command line tool တစ်ခုဖြစ်သော curl သို့မဟုတ် HTTP commands များကို ဖန်တီးပြီး run လုပ်နိုင်သော client များကို သုံးပြီး server ကို ချိတ်ဆက်နိုင်သည်။

### MCP Inspector ကို အသုံးပြုခြင်း

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) သည် သင့်ကို အောက်ပါအရာများကို ကူညီပေးသော visual testing tool တစ်ခုဖြစ်သည်-

1. **Server Capabilities ရှာဖွေခြင်း**: ရရှိနိုင်သော resources, tools, prompts များကို အလိုအလျောက် detect လုပ်ပါသည်။
2. **Tool Execution စမ်းသပ်ခြင်း**: အမျိုးမျိုးသော parameters များကို စမ်းသပ်ပြီး အချိန်နှင့်တပြေးညီ အဖြေများကို ကြည့်ရှုနိုင်သည်။
3. **Server Metadata ကြည့်ရှုခြင်း**: Server info, schemas, configurations များကို စစ်ဆေးပါသည်။

```bash
# ex TypeScript, installing and running MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

အထက်ပါ commands များကို run လုပ်သောအခါ MCP Inspector သည် သင့် browser တွင် local web interface ကို ဖွင့်လှစ်ပါမည်။ MCP servers များ၊ tools, resources, prompts များကို ပြသထားသော dashboard ကို တွေ့မြင်နိုင်ပါသည်။ ဒီ interface က tool execution ကို စမ်းသပ်ခြင်း၊ server metadata ကို စစ်ဆေးခြင်းနှင့် အချိန်နှင့်တပြေးညီ response များကို ကြည့်ရှုခြင်းတို့ကို interactive ဖြစ်စေပြီး သင့် MCP server အကောင်အထည်ဖော်မှုများကို အတည်ပြုရန်နှင့် debugging လုပ်ရန် ပိုမိုလွယ်ကူစေပါသည်။

ဒီလိုပုံစံဖြစ်နိုင်သည်-

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.my.png)

## Setup အခက်အခဲများနှင့် ဖြေရှင်းနည်းများ

| ပြဿနာ | ဖြစ်နိုင်သော ဖြေရှင်းနည်း |
|-------|-------------------|
| Connection refused | Server run နေကြောင်းနှင့် port မှန်ကြောင်း စစ်ဆေးပါ |
| Tool execution errors | Parameter validation နှင့် error handling ကို ပြန်လည်သုံးသပ်ပါ |
| Authentication failures | API keys နှင့် permissions ကို အတည်ပြုပါ |
| Schema validation errors | Parameters များသည် သတ်မှတ်ထားသော schema နှင့် ကိုက်ညီကြောင်း သေချာပါစေ |
| Server not starting | Port conflicts သို့မဟုတ် လိုအပ်သော dependencies မရှိခြင်းကို စစ်ဆေးပါ |
| CORS errors | Cross-origin requests အတွက် CORS headers ကို configure လုပ်ပါ |
| Authentication issues | Token သက်တမ်းနှင့် permissions ကို အတည်ပြုပါ |

## Local Development

Local development နှင့် testing အတွက် MCP servers များကို သင့်စက်ပေါ်တွင် တိုက်ရိုက် run လုပ်နိုင်သည်-

1. **Server process ကို စတင်ပါ**: MCP server application ကို run လုပ်ပါ
2. **Networking ကို configure လုပ်ပါ**: Server သည် မျှော်လင့်ထားသော port တွင် ရရှိနိုင်ကြောင်း သေချာပါစေ
3. **Clients များကို ချိတ်ဆက်ပါ**: `http://localhost:3000` ကဲ့သို့သော local connection URLs များကို အသုံးပြုပါ

```bash
# Example: Running a TypeScript MCP server locally
npm run start
# Server running at http://localhost:3000
```

## သင့်ရဲ့ ပထမဆုံး MCP Server ကို တည်ဆောက်ခြင်း

ကျွန်ုပ်တို့ [Core concepts](/01-CoreConcepts/README.md) ကို ယခင်သင်ခန်းစာတွင် ဖော်ပြခဲ့ပြီး အခုတော့ အဲ့ဒီအရာများကို အကောင်အထည်ဖော်ရန် အချိန်ရောက်ပါပြီ။

### Server တစ်ခု ဘာလုပ်နိုင်သလဲ

Code ရေးမစတင်မီ Server တစ်ခု ဘာလုပ်နိုင်သလဲကို သတိရပါစေ-

MCP server တစ်ခုသည် ဥပမာအားဖြင့်-

- Local files နှင့် databases များကို access လုပ်နိုင်သည်
- Remote APIs များကို ချိတ်ဆက်နိုင်သည်
- Computations များကို ဆောင်ရွက်နိုင်သည်
- အခြား tools နှင့် services များနှင့် ပေါင်းစည်းနိုင်သည်
- အပြန်အလှန် ဆက်သွယ်ရန် user interface ကို ပေးနိုင်သည်

ကောင်းပါပြီ၊ အခုတော့ ဘာလုပ်နိုင်မလဲ သိပြီးသားဖြစ်တဲ့အတွက် coding စတင်လိုက်ရအောင်။

## လေ့ကျင့်ခန်း: Server တစ်ခု ဖန်တီးခြင်း

Server တစ်ခု ဖန်တီးရန် အောက်ပါအဆင့်များကို လိုက်နာရမည်-

- MCP SDK ကို install လုပ်ပါ။
- Project တစ်ခုကို ဖန်တီးပြီး project structure ကို ပြင်ဆင်ပါ။
- Server code ကို ရေးပါ။
- Server ကို စမ်းသပ်ပါ။

### -1- Project ဖန်တီးခြင်း

#### TypeScript

```sh
# Create project directory and initialize npm project
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Create project dir
mkdir calculator-server
cd calculator-server
# Open the folder in Visual Studio Code - Skip this if you are using a different IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java အတွက် Spring Boot project တစ်ခုကို ဖန်တီးပါ-

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d javaVersion=21 \
  -d type=maven-project \
  -d groupId=com.example \
  -d artifactId=calculator-server \
  -d name=McpServer \
  -d packageName=com.microsoft.mcp.sample.server \
  -o calculator-server.zip
```

Zip file ကို extract လုပ်ပါ-

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# optional remove the unused test
rm -rf src/test/java
```

*pom.xml* ဖိုင်တွင် အောက်ပါ configuration အပြည့်အစုံကို ထည့်ပါ-

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Spring Boot parent for dependency management -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.0</version>
        <relativePath />
    </parent>

    <!-- Project coordinates -->
    <groupId>com.example</groupId>
    <artifactId>calculator-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>Calculator Server</name>
    <description>Basic calculator MCP service for beginners</description>

    <!-- Properties -->
    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
    </properties>

    <!-- Spring AI BOM for version management -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>1.0.0-SNAPSHOT</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!-- Dependencies -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-test</artifactId>
         <scope>test</scope>
      </dependency>
    </dependencies>

    <!-- Build configuration -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <release>21</release>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Repositories for Spring AI snapshots -->
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
        <repository>
            <id>spring-snapshots</id>
            <name>Spring Snapshots</name>
            <url>https://repo.spring.io/snapshot</url>
            <releases>
                <enabled>false</enabled>
            </releases>
        </repository>
    </repositories>
</project>
```

#### Rust

```sh
mkdir calculator-server
cd calculator-server
cargo init
```

### -2- Dependencies ထည့်သွင်းခြင်း

Project ကို ဖန်တီးပြီးသားဖြစ်တဲ့အတွက် dependencies များကို ထည့်သွင်းပါ-

#### TypeScript

```sh
# If not already installed, install TypeScript globally
npm install typescript -g

# Install the MCP SDK and Zod for schema validation
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Create a virtual env and install dependencies
python -m venv venv
venv\Scripts\activate
pip install "mcp[cli]"
```

#### Java

```bash
cd calculator-server
./mvnw clean install -DskipTests
```

#### Rust

```sh
cargo add rmcp --features server,transport-io
cargo add serde
cargo add tokio --features rt-multi-thread
```

### -3- Project files ဖန်တီးခြင်း

#### TypeScript

*package.json* ဖိုင်ကို ဖွင့်ပြီး server ကို build နှင့် run လုပ်နိုင်ရန် အောက်ပါ content ဖြင့် အစားထိုးပါ-

```json
{
  "name": "calculator-server",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "npm run build && node ./build/index.js",
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "A simple calculator server using Model Context Protocol",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.16.0",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@types/node": "^24.0.14",
    "typescript": "^5.8.3"
  }
}
```

*tsconfig.json* ဖိုင်ကို အောက်ပါ content ဖြင့် ဖန်တီးပါ-

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

Source code အတွက် directory တစ်ခု ဖန်တီးပါ-

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* ဖိုင်တစ်ခု ဖန်တီးပါ-

```sh
touch server.py
```

#### .NET

လိုအပ်သော NuGet packages များကို install လုပ်ပါ-

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot projects အတွက် project structure ကို အလိုအလျောက် ဖန်တီးထားသည်။

#### Rust

Rust အတွက် `cargo init` ကို run လုပ်သောအခါ *src/main.rs* ဖိုင်တစ်ခုကို အလိုအလျောက် ဖန်တီးထားသည်။ ဖိုင်ကို ဖွင့်ပြီး default code ကို ဖျက်ပါ။

### -4- Server code ဖန်တီးခြင်း

#### TypeScript

*index.ts* ဖိုင်တစ်ခု ဖန်တီးပြီး အောက်ပါ code ကို ထည့်ပါ-

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Create an MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Server တစ်ခု ရှိပြီးသားဖြစ်သော်လည်း အလုပ်မလုပ်သေးပါ၊ အဲ့ဒါကို ပြင်ဆင်လိုက်ရအောင်။

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")
```

#### .NET

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

// add features
```

#### Java

Java အတွက် core server components များကို ဖန်တီးပါ။ အရင်ဆုံး main application class ကို ပြင်ဆင်ပါ-

*src/main/java/com/microsoft/mcp/sample/server/McpServerApplication.java*:

```java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

Calculator service ကို ဖန်တီးပါ *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

```java
package com.microsoft.mcp.sample.server.service;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

/**
 * Service for basic calculator operations.
 * This service provides simple calculator functionality through MCP.
 */
@Service
public class CalculatorService {

    /**
     * Add two numbers
     * @param a The first number
     * @param b The second number
     * @return The sum of the two numbers
     */
    @Tool(description = "Add two numbers together")
    public String add(double a, double b) {
        double result = a + b;
        return formatResult(a, "+", b, result);
    }

    /**
     * Subtract one number from another
     * @param a The number to subtract from
     * @param b The number to subtract
     * @return The result of the subtraction
     */
    @Tool(description = "Subtract the second number from the first number")
    public String subtract(double a, double b) {
        double result = a - b;
        return formatResult(a, "-", b, result);
    }

    /**
     * Multiply two numbers
     * @param a The first number
     * @param b The second number
     * @return The product of the two numbers
     */
    @Tool(description = "Multiply two numbers together")
    public String multiply(double a, double b) {
        double result = a * b;
        return formatResult(a, "*", b, result);
    }

    /**
     * Divide one number by another
     * @param a The numerator
     * @param b The denominator
     * @return The result of the division
     */
    @Tool(description = "Divide the first number by the second number")
    public String divide(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a / b;
        return formatResult(a, "/", b, result);
    }

    /**
     * Calculate the power of a number
     * @param base The base number
     * @param exponent The exponent
     * @return The result of raising the base to the exponent
     */
    @Tool(description = "Calculate the power of a number (base raised to an exponent)")
    public String power(double base, double exponent) {
        double result = Math.pow(base, exponent);
        return formatResult(base, "^", exponent, result);
    }

    /**
     * Calculate the square root of a number
     * @param number The number to find the square root of
     * @return The square root of the number
     */
    @Tool(description = "Calculate the square root of a number")
    public String squareRoot(double number) {
        if (number < 0) {
            return "Error: Cannot calculate square root of a negative number";
        }
        double result = Math.sqrt(number);
        return String.format("√%.2f = %.2f", number, result);
    }

    /**
     * Calculate the modulus (remainder) of division
     * @param a The dividend
     * @param b The divisor
     * @return The remainder of the division
     */
    @Tool(description = "Calculate the remainder when one number is divided by another")
    public String modulus(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a % b;
        return formatResult(a, "%", b, result);
    }

    /**
     * Calculate the absolute value of a number
     * @param number The number to find the absolute value of
     * @return The absolute value of the number
     */
    @Tool(description = "Calculate the absolute value of a number")
    public String absolute(double number) {
        double result = Math.abs(number);
        return String.format("|%.2f| = %.2f", number, result);
    }

    /**
     * Get help about available calculator operations
     * @return Information about available operations
     */
    @Tool(description = "Get help about available calculator operations")
    public String help() {
        return "Basic Calculator MCP Service\n\n" +
               "Available operations:\n" +
               "1. add(a, b) - Adds two numbers\n" +
               "2. subtract(a, b) - Subtracts the second number from the first\n" +
               "3. multiply(a, b) - Multiplies two numbers\n" +
               "4. divide(a, b) - Divides the first number by the second\n" +
               "5. power(base, exponent) - Raises a number to a power\n" +
               "6. squareRoot(number) - Calculates the square root\n" + 
               "7. modulus(a, b) - Calculates the remainder of division\n" +
               "8. absolute(number) - Calculates the absolute value\n\n" +
               "Example usage: add(5, 3) will return 5 + 3 = 8";
    }

    /**
     * Format the result of a calculation
     */
    private String formatResult(double a, String operator, double b, double result) {
        return String.format("%.2f %s %.2f = %.2f", a, operator, b, result);
    }
}
```

**Production-ready service အတွက် optional components:**

Startup configuration ကို ဖန်တီးပါ *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

```java
package com.microsoft.mcp.sample.server.config;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class StartupConfig {
    
    @Bean
    public CommandLineRunner startupInfo() {
        return args -> {
            System.out.println("\n" + "=".repeat(60));
            System.out.println("Calculator MCP Server is starting...");
            System.out.println("SSE endpoint: http://localhost:8080/sse");
            System.out.println("Health check: http://localhost:8080/actuator/health");
            System.out.println("=".repeat(60) + "\n");
        };
    }
}
```

Health controller ကို ဖန်တီးပါ *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

```java
package com.microsoft.mcp.sample.server.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@RestController
public class HealthController {
    
    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "UP");
        response.put("timestamp", LocalDateTime.now().toString());
        response.put("service", "Calculator MCP Server");
        return ResponseEntity.ok(response);
    }
}
```

Exception handler ကို ဖန်တီးပါ *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

```java
package com.microsoft.mcp.sample.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErrorResponse> handleIllegalArgumentException(IllegalArgumentException ex) {
        ErrorResponse error = new ErrorResponse(
            "Invalid_Input", 
            "Invalid input parameter: " + ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }

    public static class ErrorResponse {
        private String code;
        private String message;

        public ErrorResponse(String code, String message) {
            this.code = code;
            this.message = message;
        }

        // Getters
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Custom banner ကို ဖန်တီးပါ *src/main/resources/banner.txt*:

```text
_____      _            _       _             
 / ____|    | |          | |     | |            
| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                
Calculator MCP Server v1.0
Spring Boot MCP Application
```

</details>

#### Rust

*src/main.rs* ဖိုင်၏ အပေါ်ပိုင်းတွင် အောက်ပါ code ကို ထည့်ပါ။ MCP server အတွက် လိုအပ်သော libraries နှင့် modules များကို import လုပ်ပါသည်။

```rust
use rmcp::{
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
    ServerHandler, ServiceExt,
};
use std::error::Error;
```

Calculator request ကို ကိုယ်စားပြုသော struct တစ်ခုကို ဖန်တီးပါ-

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Calculator server ကို ကိုယ်စားပြုသော struct တစ်ခုကို ဖန်တီးပါ။ Tool router ကို register လုပ်ရန် ဒီ struct ကို အသုံးပြုပါမည်။

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

အခုတော့ `Calculator` struct ကို implement လုပ်ပြီး server information ကို ပေးနိုင်ရန် server handler ကို implement လုပ်ပါမည်။

```rust
#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}
```

နောက်ဆုံးတွင် server ကို စတင်ရန် main function ကို implement လုပ်ရန် လိုအပ်သည်။ ဒီ function သည် `Calculator` struct ကို ဖန်တီးပြီး standard input/output မှတစ်ဆင့် serve လုပ်ပါမည်။

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Server သည် အခြေခံအချက်အလက်များကို ပေးနိုင်ရန် အဆင်သင့်ဖြစ်ပါပြီ။ အခုတော့ addition လုပ်ဆောင်ရန် tool တစ်ခုကို ထည့်သွင်းပါမည်။

### -5- Tool နှင့် Resource ထည့်သွင်းခြင်း

Tool နှင့် Resource ကို အောက်ပါ code ထည့်သွင်းခြင်းဖြင့် ထည့်ပါ-

#### TypeScript

```typescript
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

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
```

Tool သည် `a` နှင့် `b` parameters ကို ယူပြီး အောက်ပါ response ပုံစံဖြင့် function တစ်ခုကို run လုပ်ပါသည်-

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Resource သည် "greeting" string မှတစ်ဆင့် access လုပ်ပြီး `name` parameter ကို ယူပြီး tool နှင့် တူသော response ကို ထုတ်ပေးပါသည်-

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

အထက်ပါ code တွင်-

- `add` tool ကို သတ်မှတ်ထားပြီး `a` နှင့် `p` parameters (integer) ကို ယူပါသည်။
- `greeting` ဟုခေါ်သော resource ကို ဖန်တီးပြီး `name` parameter ကို ယူပါသည်။

#### .NET

Program.cs ဖိုင်တွင် အောက်ပါ code ကို ထည့်ပါ-

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Tools မ
`Command` အကွက်တွင် `python` ကို သတ်မှတ်ပြီး `Arguments` အဖြစ် `server.py` ကို သတ်မှတ်ပါ။ ဒါက script ကို မှန်ကန်စွာ run ဖို့ အရေးကြီးပါတယ်။

#### .NET

သင့် project directory ထဲမှာ ရှိနေကြောင်း သေချာပါ:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Calculator server ကို run လုပ်ထားကြောင်း သေချာပါ။
Inspector ကို run လုပ်ပါ:

```cmd
npx @modelcontextprotocol/inspector
```

Inspector web interface တွင်:

1. "SSE" ကို transport type အဖြစ် ရွေးပါ။
2. URL ကို `http://localhost:8080/sse` အဖြစ် သတ်မှတ်ပါ။
3. "Connect" ကို click လုပ်ပါ။

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.my.png)

**သင် server ကို ချိတ်ဆက်ပြီးပါပြီ**
**Java server စမ်းသပ်မှု အပိုင်းပြီးဆုံးပါပြီ**

နောက်အပိုင်းမှာ server နဲ့ အပြန်အလှန် ဆက်သွယ်မှုအကြောင်း ဖြစ်ပါတယ်။

သင့်အနေနဲ့ အောက်ပါ user interface ကို တွေ့ရပါမယ်:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.my.png)

1. Connect button ကို ရွေးပြီး server ကို ချိတ်ဆက်ပါ။
   Server ကို ချိတ်ဆက်ပြီးပါက အောက်ပါအတိုင်း တွေ့ရပါမယ်:

   ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.my.png)

1. "Tools" နဲ့ "listTools" ကို ရွေးပါ၊ "Add" ပေါ်လာပါမယ်၊ "Add" ကို ရွေးပြီး parameter values တွေကို ဖြည့်ပါ။

   သင့်အနေနဲ့ အောက်ပါအတိုင်း အဖြေကို တွေ့ရပါမယ်၊ "add" tool မှ ရလာသော ရလဒ်ဖြစ်ပါတယ်:

   ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.my.png)

အောင်မြင်ပါတယ်၊ သင့်အနေနဲ့ ပထမဆုံး server ကို ဖန်တီးပြီး run လုပ်နိုင်ခဲ့ပါပြီ!

#### Rust

MCP Inspector CLI နဲ့အတူ Rust server ကို run လုပ်ဖို့ အောက်ပါ command ကို အသုံးပြုပါ:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Official SDKs

MCP သည် အမျိုးမျိုးသော programming language များအတွက် တရားဝင် SDK များကို ပေးထားပါသည်:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft နှင့် ပူးပေါင်း၍ ထိန်းသိမ်းထားသည်
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI နှင့် ပူးပေါင်း၍ ထိန်းသိမ်းထားသည်
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - တရားဝင် TypeScript အကောင်အထည်
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - တရားဝင် Python အကောင်အထည်
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - တရားဝင် Kotlin အကောင်အထည်
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI နှင့် ပူးပေါင်း၍ ထိန်းသိမ်းထားသည်
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - တရားဝင် Rust အကောင်အထည်

## အဓိကအချက်များ

- MCP development environment ကို language-specific SDK များဖြင့် အလွယ်တကူ စတင်နိုင်သည်။
- MCP servers ဖန်တီးခြင်းသည် tool များကို ရှင်းလင်းသော schema များနှင့်အတူ ဖန်တီးပြီး register လုပ်ရန် လိုအပ်သည်။
- MCP implementation များကို ယုံကြည်စိတ်ချရစေရန် စမ်းသပ်ခြင်းနှင့် အမှားရှာဖွေခြင်းများ အရေးကြီးသည်။

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## လုပ်ငန်းတာဝန်

သင့်စိတ်ကြိုက် tool တစ်ခုဖြင့် ရိုးရှင်းသော MCP server တစ်ခု ဖန်တီးပါ:

1. သင်နှစ်သက်သော programming language (.NET, Java, Python, TypeScript, or Rust) ဖြင့် tool ကို implement လုပ်ပါ။
2. Input parameters နှင့် return values ကို သတ်မှတ်ပါ။
3. Server မှန်ကန်စွာ အလုပ်လုပ်ကြောင်း သေချာရန် inspector tool ကို run လုပ်ပါ။
4. အမျိုးမျိုးသော input များဖြင့် စမ်းသပ်ပါ။

## ဖြေရှင်းချက်

[Solution](./solution/README.md)

## အပိုဆောင်းအရင်းအမြစ်များ

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## နောက်တစ်ခု

နောက်တစ်ခု: [Getting Started with MCP Clients](../02-client/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။