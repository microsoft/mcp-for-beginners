<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "726b74589522653d930c7395c9e1fab8",
  "translation_date": "2025-10-20T16:54:29+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "ur"
}
-->
# ایم سی پی کے ساتھ شروعات

ماڈل کانٹیکسٹ پروٹوکول (MCP) کے ساتھ اپنے پہلے قدموں میں خوش آمدید! چاہے آپ ایم سی پی کے لیے نئے ہوں یا اپنی سمجھ کو گہرا کرنا چاہتے ہوں، یہ گائیڈ آپ کو ضروری سیٹ اپ اور ترقیاتی عمل کے ذریعے لے جائے گا۔ آپ دریافت کریں گے کہ ایم سی پی کس طرح AI ماڈلز اور ایپلیکیشنز کے درمیان آسان انضمام کو ممکن بناتا ہے، اور سیکھیں گے کہ ایم سی پی سے چلنے والے حلوں کی تعمیر اور جانچ کے لیے اپنے ماحول کو جلدی سے کیسے تیار کریں۔

> مختصر خلاصہ: اگر آپ AI ایپس بناتے ہیں، تو آپ جانتے ہیں کہ آپ اپنے LLM (بڑے زبان ماڈل) میں ٹولز اور دیگر وسائل شامل کر سکتے ہیں تاکہ LLM کو زیادہ معلوماتی بنایا جا سکے۔ تاہم، اگر آپ ان ٹولز اور وسائل کو سرور پر رکھیں، تو ایپ اور سرور کی صلاحیتیں کسی بھی کلائنٹ کے ذریعہ LLM کے ساتھ یا بغیر استعمال کی جا سکتی ہیں۔

## جائزہ

یہ سبق ایم سی پی ماحول کو ترتیب دینے اور اپنے پہلے ایم سی پی ایپلیکیشنز بنانے کے بارے میں عملی رہنمائی فراہم کرتا ہے۔ آپ ضروری ٹولز اور فریم ورک کو ترتیب دینے، بنیادی ایم سی پی سرورز بنانے، میزبان ایپلیکیشنز تخلیق کرنے، اور اپنی عمل درآمد کی جانچ کرنے کا طریقہ سیکھیں گے۔

ماڈل کانٹیکسٹ پروٹوکول (MCP) ایک کھلا پروٹوکول ہے جو ایپلیکیشنز کو LLMs کے لیے کانٹیکسٹ فراہم کرنے کا معیار بناتا ہے۔ ایم سی پی کو AI ایپلیکیشنز کے لیے USB-C پورٹ کی طرح سمجھیں - یہ AI ماڈلز کو مختلف ڈیٹا ذرائع اور ٹولز سے جڑنے کا معیاری طریقہ فراہم کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ یہ کرنے کے قابل ہوں گے:

- C#, Java, Python, TypeScript، اور Rust میں ایم سی پی کے لیے ترقیاتی ماحول ترتیب دینا
- حسب ضرورت خصوصیات (وسائل، پرامپٹس، اور ٹولز) کے ساتھ بنیادی ایم سی پی سرورز بنانا اور تعینات کرنا
- ایم سی پی سرورز سے جڑنے والی میزبان ایپلیکیشنز تخلیق کرنا
- ایم سی پی عمل درآمد کی جانچ اور ڈیبگ کرنا

## اپنا ایم سی پی ماحول ترتیب دینا

ایم سی پی کے ساتھ کام شروع کرنے سے پہلے، اپنے ترقیاتی ماحول کو تیار کرنا اور بنیادی ورک فلو کو سمجھنا ضروری ہے۔ یہ سیکشن آپ کو ایم سی پی کے ساتھ ہموار آغاز کے لیے ابتدائی سیٹ اپ کے مراحل کے ذریعے رہنمائی کرے گا۔

### ضروریات

ایم سی پی ترقی میں جانے سے پہلے، یقینی بنائیں کہ آپ کے پاس یہ ہیں:

- **ترقیاتی ماحول**: آپ کی منتخب کردہ زبان کے لیے (C#, Java, Python, TypeScript، یا Rust)
- **IDE/ایڈیٹر**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm، یا کوئی جدید کوڈ ایڈیٹر
- **پیکیج مینیجرز**: NuGet, Maven/Gradle, pip, npm/yarn، یا Cargo
- **API کیز**: کسی بھی AI سروسز کے لیے جو آپ اپنے میزبان ایپلیکیشنز میں استعمال کرنے کا ارادہ رکھتے ہیں

## بنیادی ایم سی پی سرور کی ساخت

ایک ایم سی پی سرور عام طور پر شامل ہوتا ہے:

- **سرور کنفیگریشن**: پورٹ، تصدیق، اور دیگر ترتیبات کی سیٹ اپ
- **وسائل**: ڈیٹا اور کانٹیکسٹ جو LLMs کو دستیاب ہوتا ہے
- **ٹولز**: وہ فعالیت جو ماڈلز استعمال کر سکتے ہیں
- **پرامپٹس**: متن کو جنریٹ یا ساخت دینے کے لیے ٹیمپلیٹس

یہاں TypeScript میں ایک سادہ مثال ہے:

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

پچھلے کوڈ میں ہم نے:

- ایم سی پی TypeScript SDK سے ضروری کلاسز درآمد کیں۔
- ایک نیا ایم سی پی سرور انسٹینس بنایا اور کنفیگر کیا۔
- ایک کسٹم ٹول (`calculator`) کو ہینڈلر فنکشن کے ساتھ رجسٹر کیا۔
- سرور کو آنے والی ایم سی پی درخواستوں کے لیے سننے کے لیے شروع کیا۔

## جانچ اور ڈیبگنگ

اپنے ایم سی پی سرور کی جانچ شروع کرنے سے پہلے، دستیاب ٹولز اور ڈیبگنگ کے بہترین طریقوں کو سمجھنا ضروری ہے۔ مؤثر جانچ یہ یقینی بناتی ہے کہ آپ کا سرور توقع کے مطابق کام کرتا ہے اور آپ کو مسائل کی جلد شناخت اور حل کرنے میں مدد دیتا ہے۔ درج ذیل سیکشن ایم سی پی عمل درآمد کی توثیق کے لیے تجویز کردہ طریقے بیان کرتا ہے۔

ایم سی پی سرورز کی جانچ اور ڈیبگ کرنے میں مدد کے لیے ٹولز فراہم کرتا ہے:

- **انسپکٹر ٹول**، یہ گرافیکل انٹرفیس آپ کو اپنے سرور سے جڑنے اور اپنے ٹولز، پرامپٹس، اور وسائل کی جانچ کرنے کی اجازت دیتا ہے۔
- **curl**، آپ کمانڈ لائن ٹول جیسے curl یا دیگر کلائنٹس کا استعمال کر کے اپنے سرور سے جڑ سکتے ہیں جو HTTP کمانڈز بنا اور چلا سکتے ہیں۔

### ایم سی پی انسپکٹر کا استعمال

[MCP انسپکٹر](https://github.com/modelcontextprotocol/inspector) ایک بصری جانچ کا ٹول ہے جو آپ کو مدد دیتا ہے:

1. **سرور کی صلاحیتوں کو دریافت کریں**: دستیاب وسائل، ٹولز، اور پرامپٹس کو خودکار طور پر شناخت کریں
2. **ٹول کے عمل کی جانچ کریں**: مختلف پیرامیٹرز آزمائیں اور حقیقی وقت میں جوابات دیکھیں
3. **سرور میٹا ڈیٹا دیکھیں**: سرور کی معلومات، اسکیمے، اور کنفیگریشنز کا جائزہ لیں

```bash
# ex TypeScript, installing and running MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

جب آپ اوپر دیے گئے کمانڈز چلائیں گے، ایم سی پی انسپکٹر آپ کے براؤزر میں ایک مقامی ویب انٹرفیس لانچ کرے گا۔ آپ ایک ڈیش بورڈ دیکھنے کی توقع کر سکتے ہیں جو آپ کے رجسٹرڈ ایم سی پی سرورز، ان کے دستیاب ٹولز، وسائل، اور پرامپٹس کو دکھاتا ہے۔ انٹرفیس آپ کو انٹرایکٹو طور پر ٹول کے عمل کی جانچ کرنے، سرور میٹا ڈیٹا کا جائزہ لینے، اور حقیقی وقت کے جوابات دیکھنے کی اجازت دیتا ہے، جس سے آپ کے ایم سی پی سرور عمل درآمد کی توثیق اور ڈیبگ کرنا آسان ہو جاتا ہے۔

یہاں ایک اسکرین شاٹ ہے کہ یہ کیسا دکھائی دے سکتا ہے:

![MCP انسپکٹر سرور کنکشن](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ur.png)

## عام سیٹ اپ کے مسائل اور حل

| مسئلہ | ممکنہ حل |
|-------|----------|
| کنکشن مسترد | چیک کریں کہ سرور چل رہا ہے اور پورٹ درست ہے |
| ٹول کے عمل کی غلطیاں | پیرامیٹر کی توثیق اور غلطی کے ہینڈلنگ کا جائزہ لیں |
| تصدیق کی ناکامی | API کیز اور اجازتوں کی تصدیق کریں |
| اسکیمہ کی توثیق کی غلطیاں | یقینی بنائیں کہ پیرامیٹرز متعین اسکیمہ سے میل کھاتے ہیں |
| سرور شروع نہیں ہو رہا | پورٹ کے تنازعات یا گمشدہ ڈیپینڈنسیز چیک کریں |
| CORS کی غلطیاں | کراس اوریجن درخواستوں کے لیے مناسب CORS ہیڈرز کنفیگر کریں |
| تصدیق کے مسائل | ٹوکن کی درستگی اور اجازتوں کی تصدیق کریں |

## مقامی ترقی

مقامی ترقی اور جانچ کے لیے، آپ ایم سی پی سرورز کو براہ راست اپنی مشین پر چلا سکتے ہیں:

1. **سرور پروسیس شروع کریں**: اپنی ایم سی پی سرور ایپلیکیشن چلائیں
2. **نیٹ ورکنگ کنفیگر کریں**: یقینی بنائیں کہ سرور متوقع پورٹ پر قابل رسائی ہے
3. **کلائنٹس کو جڑیں**: مقامی کنکشن URLs جیسے `http://localhost:3000` استعمال کریں

```bash
# Example: Running a TypeScript MCP server locally
npm run start
# Server running at http://localhost:3000
```

## اپنا پہلا ایم سی پی سرور بنانا

ہم نے [بنیادی تصورات](/01-CoreConcepts/README.md) کو پچھلے سبق میں کور کیا ہے، اب وقت ہے کہ اس علم کو عملی جامہ پہنائیں۔

### سرور کیا کر سکتا ہے

کوڈ لکھنے سے پہلے، آئیے یاد کریں کہ ایک سرور کیا کر سکتا ہے:

ایک ایم سی پی سرور، مثال کے طور پر:

- مقامی فائلوں اور ڈیٹا بیسز تک رسائی حاصل کر سکتا ہے
- ریموٹ APIs سے جڑ سکتا ہے
- حسابات انجام دے سکتا ہے
- دیگر ٹولز اور سروسز کے ساتھ انضمام کر سکتا ہے
- تعامل کے لیے یوزر انٹرفیس فراہم کر سکتا ہے

زبردست، اب جب کہ ہم جانتے ہیں کہ ہم اس کے لیے کیا کر سکتے ہیں، آئیے کوڈنگ شروع کریں۔

## مشق: سرور بنانا

سرور بنانے کے لیے، آپ کو درج ذیل مراحل پر عمل کرنا ہوگا:

- ایم سی پی SDK انسٹال کریں۔
- ایک پروجیکٹ بنائیں اور پروجیکٹ کی ساخت ترتیب دیں۔
- سرور کوڈ لکھیں۔
- سرور کی جانچ کریں۔

### -1- پروجیکٹ بنائیں

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

Java کے لیے، ایک Spring Boot پروجیکٹ بنائیں:

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

زپ فائل نکالیں:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# optional remove the unused test
rm -rf src/test/java
```

اپنے *pom.xml* فائل میں درج ذیل مکمل کنفیگریشن شامل کریں:

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

### -2- ڈیپینڈنسیز شامل کریں

اب جب کہ آپ نے اپنا پروجیکٹ بنا لیا ہے، آئیے اگلے مرحلے میں ڈیپینڈنسیز شامل کریں:

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

### -3- پروجیکٹ فائلز بنائیں

#### TypeScript

*package.json* فائل کھولیں اور درج ذیل مواد کے ساتھ تبدیل کریں تاکہ آپ سرور کو بنا اور چلا سکیں:

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

*tsconfig.json* بنائیں درج ذیل مواد کے ساتھ:

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

اپنے سورس کوڈ کے لیے ایک ڈائریکٹری بنائیں:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* فائل بنائیں

```sh
touch server.py
```

#### .NET

ضروری NuGet پیکجز انسٹال کریں:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot پروجیکٹس کے لیے، پروجیکٹ کی ساخت خود بخود بن جاتی ہے۔

#### Rust

Rust کے لیے، *src/main.rs* فائل ڈیفالٹ طور پر بنائی جاتی ہے جب آپ `cargo init` چلاتے ہیں۔ فائل کھولیں اور ڈیفالٹ کوڈ کو حذف کریں۔

### -4- سرور کوڈ بنائیں

#### TypeScript

*index.ts* فائل بنائیں اور درج ذیل کوڈ شامل کریں:

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

اب آپ کے پاس ایک سرور ہے، لیکن یہ زیادہ کچھ نہیں کرتا، آئیے اسے ٹھیک کریں۔

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

Java کے لیے، بنیادی سرور کے اجزاء بنائیں۔ پہلے، مین ایپلیکیشن کلاس میں ترمیم کریں:

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

کیلکولیٹر سروس بنائیں *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**پروڈکشن کے لیے تیار سروس کے اختیاری اجزاء:**

اسٹارٹ اپ کنفیگریشن بنائیں *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

ہیلتھ کنٹرولر بنائیں *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

ایکسپشن ہینڈلر بنائیں *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

کسٹم بینر بنائیں *src/main/resources/banner.txt*:

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

*src/main.rs* فائل کے اوپر درج ذیل کوڈ شامل کریں۔ یہ آپ کے ایم سی پی سرور کے لیے ضروری لائبریریاں اور ماڈیولز درآمد کرتا ہے۔

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

کیلکولیٹر سرور ایک سادہ سرور ہوگا جو دو نمبروں کو جمع کر سکتا ہے۔ آئیے کیلکولیٹر درخواست کی نمائندگی کرنے کے لیے ایک اسٹرکچر بنائیں۔

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

اگلا، کیلکولیٹر سرور کی نمائندگی کرنے کے لیے ایک اسٹرکچر بنائیں۔ یہ اسٹرکچر ٹول روٹر کو رکھے گا، جو ٹولز کو رجسٹر کرنے کے لیے استعمال ہوتا ہے۔

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

اب، ہم `Calculator` اسٹرکچر کو نافذ کر سکتے ہیں تاکہ سرور کی ایک نئی مثال بنائی جا سکے اور سرور ہینڈلر کو نافذ کیا جا سکے تاکہ سرور کی معلومات فراہم کی جا سکیں۔

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

آخر میں، ہمیں سرور شروع کرنے کے لیے مین فنکشن کو نافذ کرنے کی ضرورت ہے۔ یہ فنکشن `Calculator` اسٹرکچر کی ایک مثال بنائے گا اور اسے معیاری ان پٹ/آؤٹ پٹ پر فراہم کرے گا۔

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

سرور اب اپنی بنیادی معلومات فراہم کرنے کے لیے تیار ہے۔ اگلے مرحلے میں، ہم ایک ٹول شامل کریں گے جو جمع کرنے کا کام انجام دے سکے۔

### -5- ٹول اور وسائل شامل کرنا

ٹول اور وسائل شامل کرنے کے لیے درج ذیل کوڈ شامل کریں:

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

آپ کا ٹول پیرامیٹرز `a` اور `b` لیتا ہے اور ایک فنکشن چلاتا ہے جو درج ذیل شکل میں جواب دیتا ہے:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

آپ کے وسائل کو ایک سٹرنگ "greeting" کے ذریعے رسائی حاصل کی جاتی ہے اور یہ ایک پیرامیٹر `name` لیتا ہے اور ٹول کے جواب کی طرح ایک جواب دیتا ہے:

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

پچھلے کوڈ میں ہم نے:

- ایک ٹول `add` کی تعریف کی جو دو عددی پیرامیٹرز `a` اور `p` لیتا ہے۔
- ایک وسائل `greeting` تخلیق کیا جو پیرامیٹر `name` لیتا ہے۔

#### .NET

اپنی Program.cs فائل میں یہ شامل کریں:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

ٹولز پہلے ہی پچھلے مرحلے میں بنائے جا چکے ہیں۔

#### Rust

`impl Calculator` بلاک کے اندر ایک نیا ٹول شامل کریں:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- حتمی کوڈ

آخری کوڈ شامل کریں تاکہ سرور شروع ہو سکے:

#### TypeScript

```typescript
// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

یہاں مکمل کوڈ ہے:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Add an addition tool
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


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

# Main execution block - this is required to run the server
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Program.cs فائل درج ذیل مواد کے ساتھ بنائیں:

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

آپ کی مکمل مین ایپلیکیشن کلاس اس طرح نظر آنی چاہیے:

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

Rust سرور کے لیے حتمی کوڈ اس طرح نظر آنا چاہیے:

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

### -7- سرور کی جانچ کریں

سرور کو درج ذیل کمانڈ کے ساتھ شروع کریں:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> ایم سی پی انسپکٹر استعمال کرنے کے لیے، `mcp dev server.py` استعمال کریں جو خود بخود انسپکٹر لانچ کرتا ہے اور مطلوبہ پراکسی سیشن ٹوکن فراہم کرتا ہے۔ اگر آپ `mcp run server.py` استعمال کر رہے ہیں، تو آپ کو دستی طور پر انسپکٹر شروع کرنا ہوگا اور کنکشن کو کنفیگر کرنا ہوگا۔

#### .NET

یقینی بنائیں کہ آپ اپنے پروجیکٹ ڈائریکٹری میں ہیں:

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

سرور کو فارمیٹ اور چلانے کے لیے درج ذیل کمانڈز چلائیں:

```sh
cargo fmt
cargo run
```

### -8- انسپکٹر کے ذریعے چلائیں

انسپکٹر ایک بہترین ٹول ہے جو آپ کے سرور کو شروع کر سکتا ہے اور آپ کو اس کے ساتھ تعامل کرنے دیتا ہے تاکہ آپ جانچ سکیں کہ یہ کام کرتا ہے۔ آئیے اسے شروع کریں:

> [!NOTE]
> یہ "کمانڈ" فیلڈ میں مختلف نظر آ سکتا ہے کیونکہ اس میں آپ کے مخصوص رن ٹائم کے ساتھ سرور چلانے کے لیے کمانڈ شامل ہے۔

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

یا اسے اپنے *package.json* میں اس طرح شامل کریں: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` اور پھر `npm run inspector` چلائیں۔

Python ایک Node.js ٹول کو لپیٹتا ہے جسے انسپکٹر کہا جاتا ہے۔ اس ٹول کو اس طرح کال کرنا ممکن ہے:

```sh
mcp dev server.py
```

تاہم، یہ ٹول پر دستیاب تمام طریقے نافذ نہیں کرتا، اس لیے آپ کو نیچے دیے گئے طریقے سے براہ راست Node.js ٹول چلانے کی سفارش کی جاتی ہے:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

اگر آپ
یقینی بنائیں کہ `Command` فیلڈ میں `python` سیٹ کریں اور `Arguments` میں `server.py` رکھیں۔ یہ اس بات کو یقینی بناتا ہے کہ اسکرپٹ صحیح طریقے سے چلتا ہے۔

#### .NET

یقینی بنائیں کہ آپ اپنے پروجیکٹ ڈائریکٹری میں ہیں:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### جاوا

یقینی بنائیں کہ آپ کا کیلکولیٹر سرور چل رہا ہے۔
پھر انسپکٹر چلائیں:

```cmd
npx @modelcontextprotocol/inspector
```

انسپکٹر ویب انٹرفیس میں:

1. "SSE" کو ٹرانسپورٹ ٹائپ کے طور پر منتخب کریں۔
2. URL کو سیٹ کریں: `http://localhost:8080/sse`
3. "Connect" پر کلک کریں۔

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.ur.png)

**آپ اب سرور سے جڑ چکے ہیں**
**جاوا سرور ٹیسٹنگ سیکشن مکمل ہو چکا ہے**

اگلا سیکشن سرور کے ساتھ تعامل کے بارے میں ہے۔

آپ کو درج ذیل یوزر انٹرفیس نظر آنا چاہیے:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ur.png)

1. "Connect" بٹن منتخب کر کے سرور سے جڑیں۔
   جب آپ سرور سے جڑ جائیں گے، تو آپ کو درج ذیل نظر آنا چاہیے:

   ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ur.png)

1. "Tools" اور "listTools" کو منتخب کریں، آپ کو "Add" نظر آئے گا، "Add" کو منتخب کریں اور پیرامیٹر ویلیوز کو بھریں۔

   آپ کو درج ذیل جواب نظر آئے گا، یعنی "add" ٹول کا نتیجہ:

   ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.ur.png)

مبارک ہو، آپ نے اپنا پہلا سرور بنانے اور چلانے میں کامیابی حاصل کر لی ہے!

#### رسٹ

MCP انسپکٹر CLI کے ساتھ رسٹ سرور چلانے کے لیے، درج ذیل کمانڈ استعمال کریں:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### آفیشل SDKs

MCP مختلف زبانوں کے لیے آفیشل SDKs فراہم کرتا ہے:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - مائیکروسافٹ کے تعاون سے برقرار رکھا گیا
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - اسپرنگ AI کے تعاون سے برقرار رکھا گیا
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - آفیشل ٹائپ اسکرپٹ امپلیمنٹیشن
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - آفیشل پائتھون امپلیمنٹیشن
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - آفیشل کوٹلن امپلیمنٹیشن
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - لوپ ورک AI کے تعاون سے برقرار رکھا گیا
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - آفیشل رسٹ امپلیمنٹیشن

## اہم نکات

- MCP ڈیولپمنٹ ماحول کو سیٹ اپ کرنا زبان کے مخصوص SDKs کے ساتھ آسان ہے۔
- MCP سرورز بنانا واضح اسکیموں کے ساتھ ٹولز بنانے اور رجسٹر کرنے پر مشتمل ہے۔
- قابل اعتماد MCP امپلیمنٹیشنز کے لیے ٹیسٹنگ اور ڈیبگنگ ضروری ہیں۔

## نمونے

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## اسائنمنٹ

اپنی پسند کے ٹول کے ساتھ ایک سادہ MCP سرور بنائیں:

1. اپنے پسندیدہ زبان (.NET، Java، Python، TypeScript، یا Rust) میں ٹول کو نافذ کریں۔
2. ان پٹ پیرامیٹرز اور ریٹرن ویلیوز کی وضاحت کریں۔
3. انسپکٹر ٹول چلائیں تاکہ یہ یقینی بنایا جا سکے کہ سرور صحیح کام کر رہا ہے۔
4. مختلف ان پٹس کے ساتھ امپلیمنٹیشن کو ٹیسٹ کریں۔

## حل

[Solution](./solution/README.md)

## اضافی وسائل

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## آگے کیا ہے

اگلا: [Getting Started with MCP Clients](../02-client/README.md)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔