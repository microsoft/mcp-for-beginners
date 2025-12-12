<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T05:01:11+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "ur"
}
-->
# MCP کے ساتھ شروعات

ماڈل کانٹیکسٹ پروٹوکول (MCP) کے ساتھ اپنے پہلے قدموں میں خوش آمدید! چاہے آپ MCP میں نئے ہوں یا اپنی سمجھ کو گہرا کرنا چاہتے ہوں، یہ رہنما آپ کو ضروری سیٹ اپ اور ترقیاتی عمل سے گزاریگا۔ آپ جانیں گے کہ MCP کس طرح AI ماڈلز اور ایپلیکیشنز کے درمیان بغیر رکاوٹ انضمام کو ممکن بناتا ہے، اور سیکھیں گے کہ MCP سے چلنے والے حل بنانے اور ٹیسٹ کرنے کے لیے اپنا ماحول کیسے جلدی تیار کیا جائے۔

> خلاصہ؛ اگر آپ AI ایپس بناتے ہیں، تو آپ جانتے ہیں کہ آپ اپنے LLM (بڑے زبان ماڈل) میں ٹولز اور دیگر وسائل شامل کر سکتے ہیں تاکہ LLM زیادہ معلوماتی بن جائے۔ تاہم اگر آپ وہ ٹولز اور وسائل سرور پر رکھتے ہیں، تو ایپ اور سرور کی صلاحیتیں کسی بھی کلائنٹ کے ذریعے LLM کے ساتھ یا بغیر استعمال کی جا سکتی ہیں۔

## جائزہ

یہ سبق MCP ماحولیات کو سیٹ اپ کرنے اور اپنی پہلی MCP ایپلیکیشنز بنانے کے بارے میں عملی رہنمائی فراہم کرتا ہے۔ آپ سیکھیں گے کہ ضروری ٹولز اور فریم ورکس کیسے سیٹ اپ کریں، بنیادی MCP سرورز بنائیں، ہوسٹ ایپلیکیشنز تخلیق کریں، اور اپنی امپلیمنٹیشنز کو ٹیسٹ کریں۔

ماڈل کانٹیکسٹ پروٹوکول (MCP) ایک کھلا پروٹوکول ہے جو اس بات کو معیاری بناتا ہے کہ ایپلیکیشنز LLMs کو کانٹیکسٹ کیسے فراہم کرتی ہیں۔ MCP کو AI ایپلیکیشنز کے لیے USB-C پورٹ سمجھیں — یہ AI ماڈلز کو مختلف ڈیٹا ذرائع اور ٹولز سے منسلک کرنے کا ایک معیاری طریقہ فراہم کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ قابل ہوں گے:

- C#, Java, Python, TypeScript، اور Rust میں MCP کے لیے ترقیاتی ماحول سیٹ اپ کرنا
- کسٹم خصوصیات (وسائل، پرامپٹس، اور ٹولز) کے ساتھ بنیادی MCP سرورز بنانا اور تعینات کرنا
- MCP سرورز سے جڑنے والی ہوسٹ ایپلیکیشنز تخلیق کرنا
- MCP امپلیمنٹیشنز کو ٹیسٹ اور ڈیبگ کرنا

## اپنے MCP ماحول کی تیاری

MCP کے ساتھ کام شروع کرنے سے پہلے، اپنے ترقیاتی ماحول کو تیار کرنا اور بنیادی ورک فلو کو سمجھنا ضروری ہے۔ یہ سیکشن آپ کو ابتدائی سیٹ اپ کے مراحل سے گزاریگا تاکہ MCP کے ساتھ آسان آغاز یقینی بنایا جا سکے۔

### ضروریات

MCP کی ترقی میں غوطہ لگانے سے پہلے، یقینی بنائیں کہ آپ کے پاس ہے:

- **ترقیاتی ماحول**: اپنی منتخب زبان (C#, Java, Python, TypeScript، یا Rust) کے لیے
- **IDE/ایڈیٹر**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm، یا کوئی جدید کوڈ ایڈیٹر
- **پیکیج مینیجرز**: NuGet, Maven/Gradle, pip, npm/yarn، یا Cargo
- **API کیز**: کسی بھی AI سروسز کے لیے جو آپ اپنی ہوسٹ ایپلیکیشنز میں استعمال کرنے کا ارادہ رکھتے ہیں

## بنیادی MCP سرور کا ڈھانچہ

ایک MCP سرور عام طور پر شامل ہوتا ہے:

- **سرور کنفیگریشن**: پورٹ، توثیق، اور دیگر ترتیبات کا سیٹ اپ
- **وسائل**: LLMs کو دستیاب ڈیٹا اور کانٹیکسٹ
- **ٹولز**: وہ فعالیت جو ماڈلز کال کر سکتے ہیں
- **پرامپٹس**: متن بنانے یا ترتیب دینے کے لیے ٹیمپلیٹس

یہاں TypeScript میں ایک سادہ مثال ہے:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ایک MCP سرور بنائیں
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ایک اضافی ٹول شامل کریں
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ایک متحرک خوش آمدید وسیلہ شامل کریں
server.resource(
  "file",
  // 'list' پیرامیٹر کنٹرول کرتا ہے کہ وسیلہ دستیاب فائلوں کو کیسے فہرست بناتا ہے۔ اسے undefined پر سیٹ کرنے سے اس وسیلہ کے لیے فہرست سازی غیر فعال ہو جاتی ہے۔
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// ایک فائل وسیلہ شامل کریں جو فائل کے مواد کو پڑھتا ہے
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

// stdin پر پیغامات وصول کرنا اور stdout پر پیغامات بھیجنا شروع کریں
const transport = new StdioServerTransport();
await server.connect(transport);
```

پچھلے کوڈ میں ہم نے:

- MCP TypeScript SDK سے ضروری کلاسز امپورٹ کیں۔
- ایک نیا MCP سرور انسٹینس بنایا اور کنفیگر کیا۔
- ایک کسٹم ٹول (`calculator`) کو ہینڈلر فنکشن کے ساتھ رجسٹر کیا۔
- سرور کو شروع کیا تاکہ آنے والی MCP درخواستوں کو سن سکے۔

## ٹیسٹنگ اور ڈیبگنگ

اپنے MCP سرور کی ٹیسٹنگ شروع کرنے سے پہلے، دستیاب ٹولز اور ڈیبگنگ کے بہترین طریقوں کو سمجھنا ضروری ہے۔ مؤثر ٹیسٹنگ یقینی بناتی ہے کہ آپ کا سرور متوقع طریقے سے کام کرے اور آپ کو مسائل کو جلدی شناخت اور حل کرنے میں مدد دیتی ہے۔ اگلا سیکشن آپ کی MCP امپلیمنٹیشن کی تصدیق کے لیے تجویز کردہ طریقے بیان کرتا ہے۔

MCP آپ کے سرورز کو ٹیسٹ اور ڈیبگ کرنے میں مدد کے لیے ٹولز فراہم کرتا ہے:

- **انسپکٹر ٹول**، یہ گرافیکل انٹرفیس آپ کو اپنے سرور سے جڑنے اور اپنے ٹولز، پرامپٹس، اور وسائل کو ٹیسٹ کرنے کی اجازت دیتا ہے۔
- **curl**، آپ کمانڈ لائن ٹول curl یا دیگر کلائنٹس کا استعمال کرتے ہوئے بھی اپنے سرور سے جڑ سکتے ہیں جو HTTP کمانڈز بنا اور چلا سکتے ہیں۔

### MCP انسپکٹر کا استعمال

[MCP انسپکٹر](https://github.com/modelcontextprotocol/inspector) ایک بصری ٹیسٹنگ ٹول ہے جو آپ کی مدد کرتا ہے:

1. **سرور کی صلاحیتوں کا پتہ لگائیں**: دستیاب وسائل، ٹولز، اور پرامپٹس کو خودکار طریقے سے دریافت کریں
2. **ٹول کے نفاذ کا ٹیسٹ کریں**: مختلف پیرامیٹرز آزمائیں اور حقیقی وقت میں جوابات دیکھیں
3. **سرور میٹا ڈیٹا دیکھیں**: سرور کی معلومات، اسکیمہ، اور کنفیگریشنز کا معائنہ کریں

```bash
# مثال ٹائپ اسکرپٹ، MCP انسپکٹر کی تنصیب اور چلانا
npx @modelcontextprotocol/inspector node build/index.js
```

جب آپ اوپر دیے گئے کمانڈز چلائیں گے، MCP انسپکٹر آپ کے براؤزر میں ایک مقامی ویب انٹرفیس لانچ کرے گا۔ آپ کو ایک ڈیش بورڈ نظر آئے گا جو آپ کے رجسٹرڈ MCP سرورز، ان کے دستیاب ٹولز، وسائل، اور پرامپٹس دکھائے گا۔ یہ انٹرفیس آپ کو ٹول کے نفاذ کو انٹرایکٹو طریقے سے ٹیسٹ کرنے، سرور میٹا ڈیٹا کا معائنہ کرنے، اور حقیقی وقت میں جوابات دیکھنے کی اجازت دیتا ہے، جس سے آپ کے MCP سرور امپلیمنٹیشنز کی تصدیق اور ڈیبگنگ آسان ہو جاتی ہے۔

یہاں ایک اسکرین شاٹ ہے کہ یہ کیسا دکھ سکتا ہے:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ur.png)

## عام سیٹ اپ مسائل اور حل

| مسئلہ | ممکنہ حل |
|-------|-------------------|
| کنکشن مسترد ہو گیا | چیک کریں کہ سرور چل رہا ہے اور پورٹ درست ہے |
| ٹول کے نفاذ میں غلطیاں | پیرامیٹر کی تصدیق اور ایرر ہینڈلنگ کا جائزہ لیں |
| توثیق کی ناکامیاں | API کیز اور اجازتوں کی تصدیق کریں |
| اسکیمہ کی تصدیق کی غلطیاں | یقینی بنائیں کہ پیرامیٹرز متعین اسکیمہ سے میل کھاتے ہیں |
| سرور شروع نہیں ہو رہا | پورٹ کے تصادم یا گمشدہ انحصار کی جانچ کریں |
| CORS کی غلطیاں | کراس اوریجن درخواستوں کے لیے مناسب CORS ہیڈرز ترتیب دیں |
| توثیق کے مسائل | ٹوکن کی درستگی اور اجازتوں کی تصدیق کریں |

## مقامی ترقی

مقامی ترقی اور ٹیسٹنگ کے لیے، آپ اپنے کمپیوٹر پر براہ راست MCP سرورز چلا سکتے ہیں:

1. **سرور کا عمل شروع کریں**: اپنی MCP سرور ایپلیکیشن چلائیں
2. **نیٹ ورکنگ ترتیب دیں**: یقینی بنائیں کہ سرور متوقع پورٹ پر قابل رسائی ہے
3. **کلائنٹس سے جڑیں**: مقامی کنکشن URLs جیسے `http://localhost:3000` استعمال کریں

```bash
# مثال: لوکل طور پر ایک ٹائپ اسکرپٹ MCP سرور چلانا
npm run start
# سرور http://localhost:3000 پر چل رہا ہے
```

## اپنی پہلی MCP سرور کی تعمیر

ہم نے پچھلے سبق میں [بنیادی تصورات](/01-CoreConcepts/README.md) کا احاطہ کیا، اب وقت ہے کہ اس علم کو عملی جامہ پہنائیں۔

### سرور کیا کر سکتا ہے

کوڈ لکھنا شروع کرنے سے پہلے، آئیے یاد دہانی کر لیں کہ سرور کیا کر سکتا ہے:

ایک MCP سرور مثال کے طور پر کر سکتا ہے:

- مقامی فائلز اور ڈیٹا بیسز تک رسائی حاصل کرنا
- ریموٹ APIs سے جڑنا
- حساب کتاب کرنا
- دیگر ٹولز اور سروسز کے ساتھ انضمام کرنا
- تعامل کے لیے یوزر انٹرفیس فراہم کرنا

زبردست، اب جب کہ ہم جانتے ہیں کہ ہم اس کے لیے کیا کر سکتے ہیں، آئیے کوڈنگ شروع کریں۔

## مشق: سرور بنانا

سرور بنانے کے لیے، آپ کو یہ مراحل پورے کرنے ہوں گے:

- MCP SDK انسٹال کریں۔
- ایک پروجیکٹ بنائیں اور پروجیکٹ کا ڈھانچہ سیٹ اپ کریں۔
- سرور کا کوڈ لکھیں۔
- سرور کو ٹیسٹ کریں۔

### -1- پروجیکٹ بنائیں

#### TypeScript

```sh
# پروجیکٹ ڈائریکٹری بنائیں اور npm پروجیکٹ کو شروع کریں
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# پروجیکٹ ڈائریکٹری بنائیں
mkdir calculator-server
cd calculator-server
# فولڈر کو Visual Studio Code میں کھولیں - اگر آپ کوئی مختلف IDE استعمال کر رہے ہیں تو اسے چھوڑ دیں
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

زپ فائل کو نکالیں:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# غیر ضروری ٹیسٹ کو اختیاری طور پر ہٹائیں
rm -rf src/test/java
```

اپنی *pom.xml* فائل میں درج ذیل مکمل کنفیگریشن شامل کریں:

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

### -2- انحصار شامل کریں

اب جب کہ آپ کا پروجیکٹ بن چکا ہے، اگلا قدم انحصار شامل کرنا ہے:

#### TypeScript

```sh
# اگر پہلے سے انسٹال نہیں ہے، تو TypeScript کو عالمی سطح پر انسٹال کریں
npm install typescript -g

# MCP SDK اور Zod کو اسکیمہ کی تصدیق کے لیے انسٹال کریں
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# ایک ورچوئل ماحول بنائیں اور انحصارات انسٹال کریں
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

### -3- پروجیکٹ فائلیں بنائیں

#### TypeScript

*package.json* فائل کھولیں اور مندرجہ ذیل مواد سے تبدیل کریں تاکہ آپ سرور کو بنا اور چلا سکیں:

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

ایک *tsconfig.json* بنائیں جس میں درج ذیل مواد ہو:

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

Java Spring Boot پروجیکٹس کے لیے، پروجیکٹ کا ڈھانچہ خود بخود بن جاتا ہے۔

#### Rust

Rust کے لیے، `cargo init` چلانے پر *src/main.rs* فائل خود بخود بن جاتی ہے۔ فائل کھولیں اور ڈیفالٹ کوڈ حذف کریں۔

### -4- سرور کا کوڈ بنائیں

#### TypeScript

*index.ts* فائل بنائیں اور درج ذیل کوڈ شامل کریں:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// ایک MCP سرور بنائیں
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

# ایک MCP سرور بنائیں
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

Java کے لیے، بنیادی سرور اجزاء بنائیں۔ سب سے پہلے، مین ایپلیکیشن کلاس میں ترمیم کریں:

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

**پیداواری معیار کی سروس کے لیے اختیاری اجزاء:**

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

        // گیٹرز
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

مندرجہ ذیل کوڈ *src/main.rs* فائل کے اوپر شامل کریں۔ یہ آپ کے MCP سرور کے لیے ضروری لائبریریاں اور ماڈیولز امپورٹ کرتا ہے۔

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

کیلکولیٹر سرور ایک سادہ سرور ہوگا جو دو نمبروں کو جمع کر سکتا ہے۔ آئیے ایک struct بنائیں جو کیلکولیٹر کی درخواست کی نمائندگی کرے۔

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

اگلا، ایک struct بنائیں جو کیلکولیٹر سرور کی نمائندگی کرے۔ یہ struct ٹول روٹر رکھے گا، جو ٹولز کو رجسٹر کرنے کے لیے استعمال ہوتا ہے۔

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

اب، ہم `Calculator` struct کو امپلیمنٹ کر سکتے ہیں تاکہ سرور کا نیا انسٹینس بنایا جا سکے اور سرور ہینڈلر کو امپلیمنٹ کیا جا سکے تاکہ سرور کی معلومات فراہم کی جا سکیں۔

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

آخر میں، ہمیں مین فنکشن کو امپلیمنٹ کرنا ہوگا تاکہ سرور شروع ہو سکے۔ یہ فنکشن `Calculator` struct کا انسٹینس بنائے گا اور اسے اسٹینڈرڈ ان پٹ/آؤٹ پٹ پر سرو کرے گا۔

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

سرور اب اپنے بارے میں بنیادی معلومات فراہم کرنے کے لیے تیار ہے۔ اگلا، ہم ایک ٹول شامل کریں گے جو جمع کرنے کا کام کرے گا۔

### -5- ٹول اور ریسورس شامل کرنا

مندرجہ ذیل کوڈ شامل کرکے ایک ٹول اور ایک ریسورس شامل کریں:

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

آپ کا ٹول پیرامیٹرز `a` اور `b` لیتا ہے اور ایک فنکشن چلتا ہے جو درج ذیل فارم میں جواب پیدا کرتا ہے:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

آپ کا ریسورس "greeting" سٹرنگ کے ذریعے حاصل کیا جاتا ہے، یہ پیرامیٹر `name` لیتا ہے اور ٹول کی طرح ایک جواب پیدا کرتا ہے:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ایک جمع کرنے کا آلہ شامل کریں
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ایک متحرک خوش آمدید وسیلہ شامل کریں
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

پچھلے کوڈ میں ہم نے:

- ایک ٹول `add` تعریف کیا جو پیرامیٹرز `a` اور `b` لیتا ہے، دونوں انٹیجرز۔
- ایک ریسورس `greeting` بنایا جو پیرامیٹر `name` لیتا ہے۔

#### .NET

اسے اپنی Program.cs فائل میں شامل کریں:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

ٹولز پہلے ہی پچھلے مرحلے میں بن چکے ہیں۔

#### Rust

`impl Calculator` بلاک کے اندر نیا ٹول شامل کریں:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- آخری کوڈ

آئیے وہ آخری کوڈ شامل کریں جس سے سرور شروع ہو سکے:

#### TypeScript

```typescript
// اسٹڈ ان پر پیغامات وصول کرنا شروع کریں اور اسٹڈ آؤٹ پر پیغامات بھیجنا شروع کریں
const transport = new StdioServerTransport();
await server.connect(transport);
```

یہاں مکمل کوڈ ہے:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ایک MCP سرور بنائیں
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// ایک جمع کرنے کا آلہ شامل کریں
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ایک متحرک خوش آمدیدی وسیلہ شامل کریں
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

// stdin پر پیغامات وصول کرنا شروع کریں اور stdout پر پیغامات بھیجنا شروع کریں
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# سرور.py
from mcp.server.fastmcp import FastMCP

# ایک MCP سرور بنائیں
mcp = FastMCP("Demo")


# ایک جمع کرنے کا آلہ شامل کریں
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ایک متحرک خوش آمدید وسیلہ شامل کریں
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# مرکزی عمل درآمد بلاک - سرور چلانے کے لیے یہ ضروری ہے
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Program.cs فائل بنائیں جس میں درج ذیل مواد ہو:

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

آپ کی مکمل مین ایپلیکیشن کلاس کچھ یوں نظر آنی چاہیے:

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

Rust سرور کے لیے آخری کوڈ کچھ یوں ہونا چاہیے:

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

### -7- سرور کا ٹیسٹ کریں

سرور کو درج ذیل کمانڈ سے شروع کریں:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP انسپکٹر استعمال کرنے کے لیے، `mcp dev server.py` استعمال کریں جو خود بخود انسپکٹر کو لانچ کرتا ہے اور مطلوبہ پراکسی سیشن ٹوکن فراہم کرتا ہے۔ اگر `mcp run server.py` استعمال کر رہے ہیں، تو آپ کو دستی طور پر انسپکٹر شروع کرنا ہوگا اور کنکشن ترتیب دینا ہوگا۔

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

انسپکٹر ایک زبردست ٹول ہے جو آپ کے سرور کو شروع کر سکتا ہے اور آپ کو اس کے ساتھ تعامل کرنے دیتا ہے تاکہ آپ ٹیسٹ کر سکیں کہ یہ کام کر رہا ہے۔ آئیے اسے شروع کریں:

> [!NOTE]
> "کمانڈ" فیلڈ میں یہ مختلف نظر آ سکتا ہے کیونکہ اس میں آپ کے مخصوص رن ٹائم کے ساتھ سرور چلانے کا کمانڈ شامل ہوتا ہے۔

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

یا اسے اپنی *package.json* میں اس طرح شامل کریں: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` اور پھر `npm run inspector` چلائیں۔

#### Python

Python ایک Node.js ٹول انسپکٹر کو لپیٹتا ہے۔ اس ٹول کو اس طرح کال کرنا ممکن ہے:

```sh
mcp dev server.py
```

تاہم، یہ ٹول کے تمام دستیاب طریقے نافذ نہیں کرتا، اس لیے آپ کو مشورہ دیا جاتا ہے کہ نیچے دیے گئے طریقے سے Node.js ٹول کو براہ راست چلائیں:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

اگر آپ کوئی ایسا ٹول یا IDE استعمال کر رہے ہیں جو اسکرپٹس چلانے کے لیے کمانڈز اور دلائل ترتیب دینے کی اجازت دیتا ہے،
یقینی بنائیں کہ `Command` فیلڈ میں `python` سیٹ کیا گیا ہے اور `Arguments` میں `server.py`۔ اس سے اسکرپٹ صحیح طریقے سے چلتا ہے۔

#### .NET

یقینی بنائیں کہ آپ اپنے پروجیکٹ ڈائریکٹری میں ہیں:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### جاوا

یقینی بنائیں کہ آپ کا کیلکولیٹر سرور چل رہا ہے
پھر انسپکٹر چلائیں:

```cmd
npx @modelcontextprotocol/inspector
```

انسپکٹر ویب انٹرفیس میں:

1. "SSE" کو ٹرانسپورٹ ٹائپ کے طور پر منتخب کریں
2. URL کو سیٹ کریں: `http://localhost:8080/sse`
3. "Connect" پر کلک کریں

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.ur.png)

**آپ اب سرور سے جُڑ چکے ہیں**
**جاوا سرور ٹیسٹنگ سیکشن مکمل ہو چکا ہے**

اگلا سیکشن سرور کے ساتھ تعامل کے بارے میں ہے۔

آپ کو درج ذیل یوزر انٹرفیس نظر آنا چاہیے:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ur.png)

1. کنیکٹ بٹن کو منتخب کر کے سرور سے جُڑیں
  جب آپ سرور سے جُڑ جائیں گے، تو آپ کو درج ذیل نظر آئے گا:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ur.png)

1. "Tools" اور "listTools" کو منتخب کریں، آپ کو "Add" نظر آئے گا، "Add" کو منتخب کریں اور پیرامیٹر ویلیوز بھریں۔

  آپ کو درج ذیل جواب نظر آئے گا، یعنی "add" ٹول کا نتیجہ:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.ur.png)

مبارک ہو، آپ نے اپنا پہلا سرور بنانے اور چلانے میں کامیابی حاصل کی ہے!

#### رسٹ

MCP انسپکٹر CLI کے ساتھ رسٹ سرور چلانے کے لیے، درج ذیل کمانڈ استعمال کریں:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### سرکاری SDKs

MCP متعدد زبانوں کے لیے سرکاری SDKs فراہم کرتا ہے:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - مائیکروسافٹ کے تعاون سے مینٹین کیا گیا
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI کے تعاون سے مینٹین کیا گیا
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - سرکاری TypeScript امپلیمنٹیشن
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - سرکاری Python امپلیمنٹیشن
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - سرکاری Kotlin امپلیمنٹیشن
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI کے تعاون سے مینٹین کیا گیا
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - سرکاری Rust امپلیمنٹیشن

## اہم نکات

- MCP ڈیولپمنٹ ماحول کی سیٹنگ زبان مخصوص SDKs کے ساتھ آسان ہے
- MCP سرورز بنانے میں واضح اسکیموں کے ساتھ ٹولز بنانا اور رجسٹر کرنا شامل ہے
- قابل اعتماد MCP امپلیمنٹیشن کے لیے ٹیسٹنگ اور ڈیبگنگ ضروری ہے

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [TypeScript کیلکولیٹر](../samples/typescript/README.md)
- [Python کیلکولیٹر](../../../../03-GettingStarted/samples/python)
- [رسٹ کیلکولیٹر](../../../../03-GettingStarted/samples/rust)

## اسائنمنٹ

اپنی پسند کے ٹول کے ساتھ ایک سادہ MCP سرور بنائیں:

1. اپنی پسندیدہ زبان میں ٹول کو امپلیمنٹ کریں (.NET, جاوا, Python, TypeScript, یا رسٹ)۔
2. ان پٹ پیرامیٹرز اور ریٹرن ویلیوز کی تعریف کریں۔
3. انسپکٹر ٹول چلائیں تاکہ سرور صحیح کام کر رہا ہو۔
4. مختلف ان پٹس کے ساتھ امپلیمنٹیشن کو ٹیسٹ کریں۔

## حل

[حل](./solution/README.md)

## اضافی وسائل

- [Azure پر Model Context Protocol کے ذریعے ایجنٹس بنائیں](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps کے ساتھ ریموٹ MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP ایجنٹ](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## اگلا کیا ہے

اگلا: [MCP کلائنٹس کے ساتھ شروعات](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->