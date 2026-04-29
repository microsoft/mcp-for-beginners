# เริ่มต้นใช้งาน MCP

ยินดีต้อนรับสู่ก้าวแรกของคุณกับ Model Context Protocol (MCP)! ไม่ว่าคุณจะเป็นมือใหม่กับ MCP หรือกำลังมองหาวิธีเพิ่มพูนความเข้าใจ คู่มือนี้จะพาคุณผ่านขั้นตอนการตั้งค่าและการพัฒนาที่สำคัญ คุณจะได้เรียนรู้ว่า MCP ช่วยให้การเชื่อมต่อระหว่างโมเดล AI และแอปพลิเคชันเป็นไปอย่างราบรื่นได้อย่างไร และจะเตรียมสภาพแวดล้อมเพื่อสร้างและทดสอบโซลูชันที่ใช้ MCP ได้อย่างรวดเร็วอย่างไร

> TLDR; ถ้าคุณสร้างแอป AI คุณรู้ว่าคุณสามารถเพิ่มเครื่องมือและทรัพยากรอื่น ๆ ให้กับ LLM (โมเดลภาษาขนาดใหญ่) เพื่อทำให้ LLM มีความรู้มากขึ้น อย่างไรก็ตามหากคุณวางเครื่องมือและทรัพยากรเหล่านั้นบนเซิร์ฟเวอร์ ความสามารถของแอปและเซิร์ฟเวอร์นั้นสามารถถูกใช้ได้โดยลูกค้าใดก็ได้ ไม่ว่าจะมี LLM หรือไม่ก็ตาม

## ภาพรวม

บทเรียนนี้ให้คำแนะนำเชิงปฏิบัติในการตั้งค่าสภาพแวดล้อม MCP และการสร้างแอป MCP แรกของคุณ คุณจะได้เรียนรู้วิธีการตั้งค่าเครื่องมือและกรอบงานที่จำเป็น สร้างเซิร์ฟเวอร์ MCP พื้นฐาน สร้างแอปโฮสต์ และทดสอบการใช้งานของคุณ

Model Context Protocol (MCP) คือโปรโตคอลเปิดที่เป็นมาตรฐานวิธีที่แอปพลิเคชันให้บริบทกับ LLM ลองนึกถึง MCP เหมือนพอร์ต USB-C สำหรับแอป AI — มันให้วิธีมาตรฐานในการเชื่อมต่อโมเดล AI กับแหล่งข้อมูลและเครื่องมือต่าง ๆ

## เป้าหมายการเรียนรู้

ภายในสิ้นสุดบทเรียนนี้ คุณจะสามารถ:

- ตั้งค่าสภาพแวดล้อมการพัฒนา MCP ในภาษา C#, Java, Python, TypeScript และ Rust
- สร้างและปรับใช้เซิร์ฟเวอร์ MCP พื้นฐานพร้อมฟีเจอร์ที่กำหนดเอง (ทรัพยากร, prompts, และเครื่องมือ)
- สร้างแอปโฮสต์ที่เชื่อมต่อกับเซิร์ฟเวอร์ MCP
- ทดสอบและดีบักงานที่พัฒนาโดย MCP

## การตั้งค่าสภาพแวดล้อม MCP ของคุณ

ก่อนเริ่มใช้งาน MCP สิ่งสำคัญคือการเตรียมสภาพแวดล้อมการพัฒนาและเข้าใจขั้นตอนการทำงานพื้นฐาน ส่วนนี้จะนำทางคุณผ่านขั้นตอนการตั้งค่าเบื้องต้นเพื่อให้เริ่มต้นใช้งาน MCP ได้อย่างราบรื่น

### สิ่งที่ต้องมีล่วงหน้า

ก่อนเริ่มพัฒนา MCP ให้แน่ใจว่าคุณมี:

- **สภาพแวดล้อมการพัฒนา**: ตามภาษาที่เลือกใช้ (C#, Java, Python, TypeScript หรือ Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm หรือโปรแกรมแก้ไขโค้ดสมัยใหม่ใด ๆ
- **ตัวจัดการแพ็กเกจ**: NuGet, Maven/Gradle, pip, npm/yarn หรือ Cargo
- ** API Keys**: สำหรับบริการ AI ที่คุณวางแผนจะใช้ในแอปโฮสต์ของคุณ

## โครงสร้างเซิร์ฟเวอร์ MCP พื้นฐาน

เซิร์ฟเวอร์ MCP ทั่วไปจะประกอบด้วย:

- **การตั้งค่าเซิร์ฟเวอร์**: ตั้งค่าพอร์ต, การยืนยันตัวตน, และการตั้งค่าอื่นๆ
- **ทรัพยากร**: ข้อมูลและบริบทที่ให้กับ LLM
- **เครื่องมือ**: ฟังก์ชันที่โมเดลสามารถเรียกใช้
- **Prompts**: แม่แบบสำหรับสร้างหรือจัดโครงสร้างข้อความ

นี่คือตัวอย่างอย่างง่ายใน TypeScript:

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

// เพิ่มทรัพยากรคำทักทายแบบไดนามิก
server.resource(
  "file",
  // พารามิเตอร์ 'list' ควบคุมวิธีที่ทรัพยากรแสดงรายการไฟล์ที่มีอยู่ การตั้งค่าเป็น undefined จะปิดการแสดงรายการสำหรับทรัพยากรนี้
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// เพิ่มทรัพยากรไฟล์ที่อ่านเนื้อหาไฟล์
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

// เริ่มรับข้อความจาก stdin และส่งข้อความบน stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

ในโค้ดข้างต้น เราได้:

- นำเข้าคลาสที่จำเป็นจาก MCP TypeScript SDK
- สร้างและตั้งค่าอินสแตนซ์เซิร์ฟเวอร์ MCP ใหม่
- ลงทะเบียนเครื่องมือแบบกำหนดเอง (`calculator`) พร้อมฟังก์ชันตัวจัดการ
- เริ่มเซิร์ฟเวอร์ให้รอฟังคำร้องขอ MCP ที่เข้ามา

## การทดสอบและดีบัก

ก่อนเริ่มทดสอบเซิร์ฟเวอร์ MCP ของคุณ สิ่งสำคัญคือการเข้าใจเครื่องมือที่มีอยู่และแนวทางที่ดีที่สุดสำหรับการดีบัก การทดสอบอย่างมีประสิทธิภาพช่วยให้เซิร์ฟเวอร์ของคุณทำงานตามที่คาดหวังและช่วยให้คุณระบุและแก้ปัญหาได้รวดเร็ว ส่วนต่อไปนี้ชี้แนะวิธีที่แนะนำสำหรับการตรวจสอบการใช้งาน MCP ของคุณ

MCP มีเครื่องมือเพื่อช่วยทดสอบและดีบักเซิร์ฟเวอร์ของคุณ:

- **เครื่องมือตรวจสอบ (Inspector tool)**, อินเทอร์เฟซกราฟิกนี้ช่วยให้คุณเชื่อมต่อกับเซิร์ฟเวอร์และทดสอบเครื่องมือ, prompts และทรัพยากรของคุณได้
- **curl**, คุณยังสามารถเชื่อมต่อเซิร์ฟเวอร์โดยใช้เครื่องมือบรรทัดคำสั่ง เช่น curl หรือไคลเอนต์ตัวอื่นที่สามารถสร้างและรันคำสั่ง HTTP ได้

### การใช้ MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) คือเครื่องมือทดสอบด้วยภาพที่ช่วยให้คุณ:

1. **ค้นหาความสามารถของเซิร์ฟเวอร์**: ตรวจจับอัตโนมัติทรัพยากร, เครื่องมือ, และ prompts ที่มี
2. **ทดสอบการทำงานของเครื่องมือ**: ลองพารามิเตอร์ต่างๆ และดูผลตอบสนองแบบเรียลไทม์
3. **ดูข้อมูลเมตาของเซิร์ฟเวอร์**: ตรวจสอบข้อมูลเซิร์ฟเวอร์, สคีมา, และการตั้งค่า

```bash
# ตัวอย่าง TypeScript การติดตั้งและใช้งาน MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

เมื่อคุณรันคำสั่งข้างต้น MCP Inspector จะเปิดอินเทอร์เฟซเว็บท้องถิ่นในเบราว์เซอร์ของคุณ คุณจะเห็นแดชบอร์ดแสดงเซิร์ฟเวอร์ MCP ที่ลงทะเบียนไว้ เครื่องมือ ทรัพยากร และ prompts ที่มี อินเทอร์เฟซช่วยให้คุณทดสอบการทำงานของเครื่องมือ ได้แบบโต้ตอบ ตรวจสอบข้อมูลเมต้า และดูการตอบสนองแบบเรียลไทม์ ทำให้ง่ายต่อการตรวจสอบและดีบักการใช้งานเซิร์ฟเวอร์ MCP ของคุณ

นี่คือภาพหน้าจอว่าหน้าตาอาจเป็นอย่างไร:

![MCP Inspector server connection](../../../../translated_images/th/connected.73d1e042c24075d3.webp)

## ปัญหาการตั้งค่าที่พบบ่อยและวิธีแก้ไข

| ปัญหา | วิธีแก้ไขที่เป็นไปได้ |
|-------|-----------------------|
| การเชื่อมต่อล้มเหลว | ตรวจสอบว่าเซิร์ฟเวอร์กำลังทำงานและพอร์ตถูกต้อง |
| ข้อผิดพลาดในการเรียกใช้เครื่องมือ | ทบทวนการตรวจสอบพารามิเตอร์และการจัดการข้อผิดพลาด |
| การยืนยันตัวตนล้มเหลว | ตรวจสอบ API keys และสิทธิ์การใช้งาน |
| ข้อผิดพลาดการตรวจสอบสคีมา | ตรวจสอบว่าพารามิเตอร์ตรงกับสคีมาที่กำหนดไว้ |
| เซิร์ฟเวอร์ไม่เริ่มทำงาน | ตรวจสอบปัญหาการชนกันของพอร์ตหรือการขาดส่วนประกอบที่จำเป็น |
| ข้อผิดพลาด CORS | ตั้งค่าหัวข้อ CORS ให้เหมาะสมสำหรับคำขอข้ามแหล่งที่มา |
| ปัญหาการยืนยันตัวตน | ตรวจสอบความถูกต้องและสิทธิ์ของโทเค็น |

## การพัฒนาท้องถิ่น

สำหรับการพัฒนาและทดสอบท้องถิ่น คุณสามารถรันเซิร์ฟเวอร์ MCP ได้โดยตรงบนเครื่องของคุณ:

1. **เริ่มกระบวนการเซิร์ฟเวอร์**: รันแอปเซิร์ฟเวอร์ MCP ของคุณ
2. **ตั้งค่าเครือข่าย**: ตรวจสอบให้แน่ใจว่าเซิร์ฟเวอร์เข้าถึงได้บนพอร์ตที่คาดหวัง
3. **เชื่อมต่อไคลเอนท์**: ใช้ URL การเชื่อมต่อท้องถิ่นเช่น `http://localhost:3000`

```bash
# ตัวอย่าง: การรันเซิร์ฟเวอร์ MCP ด้วย TypeScript ในเครื่องท้องถิ่น
npm run start
# เซิร์ฟเวอร์กำลังทำงานที่ http://localhost:3000
```

## การสร้างเซิร์ฟเวอร์ MCP แรกของคุณ

เราได้พูดถึง [แนวคิดหลัก](../../01-CoreConcepts/README.md) ในบทเรียนก่อนหน้านี้แล้ว ตอนนี้ถึงเวลานำความรู้นั้นมาปฏิบัติ

### เซิร์ฟเวอร์สามารถทำอะไรได้บ้าง

ก่อนเริ่มเขียนโค้ด ขอทบทวนกันว่าคุณจะทำอะไรกับเซิร์ฟเวอร์ได้บ้าง:

เซิร์ฟเวอร์ MCP สามารถทำได้เช่น:

- เข้าถึงไฟล์และฐานข้อมูลภายในเครื่อง
- เชื่อมต่อกับ API ระยะไกล
- ทำการคำนวณ
- รวมเข้ากับเครื่องมือและบริการอื่น ๆ
- ให้ส่วนต่อประสานผู้ใช้สำหรับการโต้ตอบ

เยี่ยมเลย ตอนนี้เรารู้ว่าเซิร์ฟเวอร์ทำอะไรได้บ้าง เรามาเริ่มเขียนโค้ดกันเลย

## แบบฝึกหัด: การสร้างเซิร์ฟเวอร์

ในการสร้างเซิร์ฟเวอร์ คุณต้องทำตามขั้นตอนดังนี้:

- ติดตั้ง MCP SDK
- สร้างโปรเจกต์และตั้งค่าโครงสร้างโปรเจกต์
- เขียนโค้ดเซิร์ฟเวอร์
- ทดสอบเซิร์ฟเวอร์

### -1- สร้างโปรเจกต์

#### TypeScript

```sh
# สร้างไดเรกทอรีโปรเจกต์และเริ่มต้นโปรเจกต์ npm
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# สร้างไดเรกทอรีโครงการ
mkdir calculator-server
cd calculator-server
# เปิดโฟลเดอร์ใน Visual Studio Code - ข้ามขั้นตอนนี้หากคุณใช้ IDE อื่น
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

สำหรับ Java ให้สร้างโปรเจกต์ Spring Boot:

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

แตกไฟล์ zip:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ไม่จำเป็นต้องลบการทดสอบที่ไม่ได้ใช้
rm -rf src/test/java
```

เพิ่มการตั้งค่าครบถ้วนนี้ลงในไฟล์ *pom.xml* ของคุณ:

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

### -2- เพิ่ม Dependencies

ตอนนี้คุณสร้างโปรเจกต์เสร็จแล้ว ต่อไปเราจะเพิ่ม dependencies:

#### TypeScript

```sh
# หากยังไม่ได้ติดตั้ง ให้ติดตั้ง TypeScript แบบทั่วโลก
npm install typescript -g

# ติดตั้ง MCP SDK และ Zod สำหรับการตรวจสอบสคีมา
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# สร้างสภาพแวดล้อมเสมือนและติดตั้ง dependencies
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

### -3- สร้างไฟล์โปรเจกต์

#### TypeScript

เปิดไฟล์ *package.json* แล้วแทนที่เนื้อหาด้วยข้อความต่อไปนี้เพื่อให้แน่ใจว่าสามารถสร้างและรันเซิร์ฟเวอร์ได้:

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

สร้าง *tsconfig.json* ด้วยเนื้อหาต่อไปนี้:

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

สร้างไดเรกทอรีสำหรับโค้ดต้นฉบับของคุณ:

```sh
mkdir src
touch src/index.ts
```

#### Python

สร้างไฟล์ *server.py*

```sh
touch server.py
```

#### .NET

ติดตั้งแพ็กเกจ NuGet ที่จำเป็น:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

สำหรับโปรเจกต์ Java Spring Boot โครงสร้างโปรเจกต์จะถูกสร้างขึ้นอัตโนมัติ

#### Rust

สำหรับ Rust ไฟล์ *src/main.rs* จะถูกสร้างโดยอัตโนมัติเมื่อคุณรันคำสั่ง `cargo init` เปิดไฟล์และลบโค้ดมาตรฐานออก

### -4- เขียนโค้ดเซิร์ฟเวอร์

#### TypeScript

สร้างไฟล์ *index.ts* และเพิ่มโค้ดต่อไปนี้:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// สร้างเซิร์ฟเวอร์ MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

ตอนนี้คุณมีเซิร์ฟเวอร์แล้ว แต่ยังทำอะไรไม่มาก มาแก้ไขกัน

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# สร้างเซิร์ฟเวอร์ MCP
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

สำหรับ Java ให้สร้างส่วนประกอบหลักของเซิร์ฟเวอร์ ก่อนอื่นแก้ไขคลาสแอปพลิเคชันหลัก:

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

สร้างเซอร์วิสเครื่องคิดเลข *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**ส่วนประกอบเสริมสำหรับเซอร์วิสที่พร้อมใช้งานในผลิตจริง:**

สร้างการตั้งค่าเริ่มต้น *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

สร้างคอนโทรลเลอร์สำหรับสุขภาพ *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

สร้างตัวจัดการข้อยกเว้น *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // ตัวดึงข้อมูล
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

สร้างแบนเนอร์แบบกำหนดเอง *src/main/resources/banner.txt*:

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

เพิ่มโค้ดต่อไปนี้ที่ส่วนบนของไฟล์ *src/main.rs* ซึ่งนำเข้าไลบรารีและโมดูลที่จำเป็นสำหรับเซิร์ฟเวอร์ MCP ของคุณ

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

เซิร์ฟเวอร์เครื่องคิดเลขจะเป็นเซิร์ฟเวอร์ง่ายๆ ที่สามารถบวกเลขสองตัวเข้าด้วยกัน ให้เราสร้าง struct เพื่อแทนคำขอเครื่องคิดเลข

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

จากนั้นสร้าง struct เพื่อแทนเซิร์ฟเวอร์เครื่องคิดเลข struct นี้จะเก็บ router ของเครื่องมือซึ่งใช้สำหรับลงทะเบียนเครื่องมือ

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

ตอนนี้ เราสามารถใช้งาน `Calculator` struct เพื่อสร้างอินสแตนซ์ของเซิร์ฟเวอร์และเขียนตัวจัดการเซิร์ฟเวอร์เพื่อให้ข้อมูลเซิร์ฟเวอร์

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

สุดท้าย เราต้องเขียนฟังก์ชันหลักเพื่อเริ่มเซิร์ฟเวอร์ ฟังก์ชันนี้จะสร้างอินสแตนซ์ `Calculator` และให้บริการผ่าน standard input/output

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

เซิร์ฟเวอร์ถูกตั้งค่าเพื่อให้ข้อมูลพื้นฐานเกี่ยวกับตัวเองแล้ว ต่อไปเราจะเพิ่มเครื่องมือสำหรับการบวก

### -5- เพิ่มเครื่องมือและทรัพยากร

เพิ่มเครื่องมือและทรัพยากรด้วยการเพิ่มโค้ดต่อไปนี้:

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

เครื่องมือของคุณจะรับพารามิเตอร์ `a` และ `b` และรันฟังก์ชันที่สร้างคำตอบในรูปแบบ:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

ทรัพยากรของคุณเข้าถึงได้ผ่านสตริง "greeting" และรับพารามิเตอร์ `name` แล้วสร้างคำตอบในลักษณะคล้ายกับเครื่องมือ:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# เพิ่มเครื่องมือการบวก
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# เพิ่มแหล่งทรัพยากรคำทักทายแบบไดนามิก
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

ในโค้ดข้างต้นเราได้:

- กำหนดเครื่องมือ `add` ที่รับพารามิเตอร์ `a` และ `b` ซึ่งเป็นจำนวนเต็ม
- สร้างทรัพยากรชื่อ `greeting` ที่รับพารามิเตอร์ `name`

#### .NET

เพิ่มโค้ดนี้ลงในไฟล์ Program.cs ของคุณ:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

เครื่องมือถูกสร้างไว้แล้วในขั้นตอนก่อนหน้า

#### Rust

เพิ่มเครื่องมือใหม่ภายในบล็อก `impl Calculator`:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- โค้ดสุดท้าย

เพิ่มโค้ดส่วนสุดท้ายที่จำเป็นเพื่อให้เซิร์ฟเวอร์สามารถเริ่มทำงานได้:

#### TypeScript

```typescript
// เริ่มรับข้อความจาก stdin และส่งข้อความไปยัง stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

นี่คือโค้ดทั้งหมด:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// สร้างเซิร์ฟเวอร์ MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// เพิ่มเครื่องมือบวก
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// เพิ่มทรัพยากรคำทักทายแบบไดนามิก
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

// เริ่มรับข้อความจาก stdin และส่งข้อความบน stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

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

# บล็อกการทำงานหลัก - จำเป็นต้องใช้เพื่อรันเซิร์ฟเวอร์
if __name__ == "__main__":
    mcp.run()
```

#### .NET

สร้างไฟล์ Program.cs ด้วยเนื้อหาดังต่อไปนี้:

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

#### Java

คลาสแอปพลิเคชันหลักฉบับสมบูรณ์ของคุณควรมีลักษณะดังนี้:

```java
// McpServerApplication.java
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

#### Rust

โค้ดสุดท้ายสำหรับเซิร์ฟเวอร์ Rust ควรมีลักษณะดังนี้:

```rust
use rmcp::{
    ServerHandler, ServiceExt,
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
};
use std::error::Error;

#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}

#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}

#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
    
    #[tool(description = "Adds a and b")]
    async fn add(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a + b).to_string()
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

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

### -7- ทดสอบเซิร์ฟเวอร์

เริ่มเซิร์ฟเวอร์ด้วยคำสั่งต่อไปนี้:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> เพื่อใช้ MCP Inspector ให้ใช้คำสั่ง `mcp dev server.py` ซึ่งจะเปิด Inspector อัตโนมัติและให้โทเค็น proxy session ที่จำเป็น หากใช้ `mcp run server.py` คุณจะต้องเปิด Inspector ด้วยตนเองและตั้งค่าการเชื่อมต่อ

#### .NET

ตรวจสอบให้แน่ใจว่าคุณอยู่ในไดเรกทอรีโปรเจกต์:

```sh
cd McpCalculatorServer
dotnet run
```

#### Java

```bash
./mvnw clean install -DskipTests
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### Rust

รันคำสั่งต่อไปนี้เพื่อจัดรูปแบบและรันเซิร์ฟเวอร์:

```sh
cargo fmt
cargo run
```

### -8- รันด้วย inspector

Inspector เป็นเครื่องมือที่ยอดเยี่ยมสำหรับเริ่มเซิร์ฟเวอร์ของคุณและช่วยให้คุณโต้ตอบกับมันเพื่อทดสอบว่าใช้งานได้ ให้เราเริ่มใช้งานกัน:

> [!NOTE]
> อาจดูแตกต่างในช่อง "command" เพราะมันแสดงคำสั่งสำหรับรันเซิร์ฟเวอร์กับ runtime เฉพาะของคุณ

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

หรือนำไปเพิ่มใน *package.json* ของคุณแบบนี้: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` แล้วรัน `npm run inspector`

#### Python

Python ห่อหุ้มเครื่องมือ Node.js ที่ชื่อ inspector มันสามารถเรียกใช้เครื่องมือดังกล่าวได้แบบนี้:

```sh
mcp dev server.py
```

แต่เครื่องมือ Python ไม่ได้รองรับทุกฟังก์ชันของเครื่องมือดังกล่าว ดังนั้นจึงแนะนำให้รันเครื่องมือ Node.js โดยตรงดังนี้:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

หากคุณใช้เครื่องมือหรือ IDE ที่อนุญาตให้ตั้งค่าคำสั่งและอาร์กิวเมนต์สำหรับรันสคริปต์,
ตรวจสอบให้แน่ใจว่าได้ตั้งค่า `python` ในฟิลด์ `Command` และตั้งค่า `server.py` เป็น `Arguments` ซึ่งจะช่วยให้สคริปต์ทำงานได้อย่างถูกต้อง

#### .NET

ตรวจสอบให้แน่ใจว่าคุณอยู่ในไดเรกทอรีโครงการของคุณ:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

ตรวจสอบให้แน่ใจว่าเซิร์ฟเวอร์เครื่องคิดเลขของคุณกำลังทำงาน
จากนั้นรันตัวตรวจสอบ:

```cmd
npx @modelcontextprotocol/inspector
```

ในอินเทอร์เฟซเว็บของตัวตรวจสอบ:

1. เลือก "SSE" เป็นประเภทการขนส่ง
2. ตั้งค่า URL เป็น: `http://localhost:8080/sse`
3. คลิก "Connect"

![Connect](../../../../translated_images/th/tool.163d33e3ee307e20.webp)

**ตอนนี้คุณเชื่อมต่อกับเซิร์ฟเวอร์แล้ว**
**ส่วนการทดสอบเซิร์ฟเวอร์ Java เสร็จสมบูรณ์แล้ว**

ส่วนถัดไปเกี่ยวกับการโต้ตอบกับเซิร์ฟเวอร์

คุณควรเห็นอินเทอร์เฟซผู้ใช้ดังต่อไปนี้:

![Connect](../../../../translated_images/th/connect.141db0b2bd05f096.webp)

1. เชื่อมต่อกับเซิร์ฟเวอร์โดยเลือกปุ่ม Connect
  เมื่อต่อเซิร์ฟเวอร์สำเร็จ คุณจะเห็นสิ่งต่อไปนี้:

  ![Connected](../../../../translated_images/th/connected.73d1e042c24075d3.webp)

1. เลือก "Tools" และ "listTools" คุณควรเห็นปุ่ม "Add" ปรากฏขึ้น เลือก "Add" และกรอกค่าพารามิเตอร์

  คุณควรเห็นการตอบกลับดังนี้ คือผลลัพธ์จากเครื่องมือ "add":

  ![Result of running add](../../../../translated_images/th/ran-tool.a5a6ee878c1369ec.webp)

ยินดีด้วย คุณได้สร้างและรันเซิร์ฟเวอร์แรกของคุณสำเร็จแล้ว!

#### Rust

เพื่อรันเซิร์ฟเวอร์ Rust ด้วย MCP Inspector CLI ให้ใช้คำสั่งดังต่อไปนี้:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### SDK อย่างเป็นทางการ

MCP มี SDK อย่างเป็นทางการสำหรับหลายภาษา:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - ดูแลโดยร่วมกับ Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - ดูแลโดยร่วมกับ Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - การติดตั้ง TypeScript อย่างเป็นทางการ
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - การติดตั้ง Python อย่างเป็นทางการ
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - การติดตั้ง Kotlin อย่างเป็นทางการ
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - ดูแลโดยร่วมกับ Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - การติดตั้ง Rust อย่างเป็นทางการ

## ประเด็นสำคัญ

- การตั้งค่าสภาพแวดล้อมการพัฒนา MCP ทำได้ง่ายดายด้วย SDK เฉพาะภาษา
- การสร้างเซิร์ฟเวอร์ MCP เกี่ยวข้องกับการสร้างและลงทะเบียนเครื่องมือที่มีสคีมาอย่างชัดเจน
- การทดสอบและดีบักมีความสำคัญสำหรับการใช้งาน MCP ที่น่าเชื่อถือ

## ตัวอย่าง

- [เครื่องคิดเลข Java](../samples/java/calculator/README.md)
- [เครื่องคิดเลข .Net](../../../../03-GettingStarted/samples/csharp)
- [เครื่องคิดเลข JavaScript](../samples/javascript/README.md)
- [เครื่องคิดเลข TypeScript](../samples/typescript/README.md)
- [เครื่องคิดเลข Python](../../../../03-GettingStarted/samples/python)
- [เครื่องคิดเลข Rust](../../../../03-GettingStarted/samples/rust)

## งานมอบหมาย

สร้างเซิร์ฟเวอร์ MCP ง่ายๆ ด้วยเครื่องมือที่คุณเลือก:

1. พัฒนาเครื่องมือในภาษาที่คุณชอบ (.NET, Java, Python, TypeScript หรือ Rust)
2. กำหนดพารามิเตอร์อินพุตและค่าที่คืนกลับ
3. รันเครื่องมือตรวจสอบเพื่อให้แน่ใจว่าเซิร์ฟเวอร์ทำงานตามที่ตั้งใจ
4. ทดสอบการใช้งานด้วยอินพุตที่หลากหลาย

## แนวทางแก้ไข

[แนวทางแก้ไข](./solution/README.md)

## แหล่งข้อมูลเพิ่มเติม

- [สร้างเอเจนต์ด้วย Model Context Protocol บน Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP ระยะไกลกับ Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [เอเจนต์ .NET OpenAI MCP](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## ถัดไป

ถัดไป: [เริ่มต้นกับ MCP Clients](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้การแปลโดยผู้เชี่ยวชาญด้านภาษามนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใดๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->