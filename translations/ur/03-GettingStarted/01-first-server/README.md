# MCP کے ساتھ شروعات

خوش آمدید آپ کے پہلے قدموں پر ماڈل کانٹیکسٹ پروٹوکول (MCP) کے ساتھ! چاہے آپ MCP میں نئے ہوں یا اپنی سمجھ کو گہرا کرنا چاہتے ہوں، یہ رہنما آپ کو ضروری سیٹ اپ اور ترقیاتی عمل کے ذریعے لے جائے گا۔ آپ یہ دریافت کریں گے کہ MCP کیسے AI ماڈلز اور ایپلیکیشنز کے درمیان بے رکاوٹ انضمام کو ممکن بناتا ہے، اور سیکھیں گے کہ اپنے ماحول کو MCP سے چلنے والے حل بنانے اور ٹیسٹ کرنے کے لئے تیزی سے کیسے تیار کریں۔

> خلاصہ؛ اگر آپ AI ایپس بناتے ہیں، تو آپ جانتے ہیں کہ آپ اپنے LLM (بڑے زبان کے ماڈل) میں ٹولز اور دیگر وسائل شامل کر سکتے ہیں تاکہ LLM زیادہ معلوماتی بن جائے۔ تاہم اگر آپ یہ ٹولز اور وسائل سرور پر رکھتے ہیں، تو ایپ اور سرور کی صلاحیتیں کسی بھی کلائنٹ کے ذریعہ LLM کے ساتھ یا بغیر استعمال کی جا سکتی ہیں۔

## جائزہ

یہ سبق MCP ماحولیات کو ترتیب دینے اور اپنے پہلے MCP ایپلیکیشنز بنانے کے لئے عملی رہنمائی فراہم کرتا ہے۔ آپ سیکھیں گے کہ ضروری ٹولز اور فریم ورکس کس طرح ترتیب دیں، بنیادی MCP سرورز تخلیق کریں، ہوسٹ ایپلیکیشنز بنائیں، اور اپنی تنصیبات کی جانچ کریں۔

ماڈل کانٹیکسٹ پروٹوکول (MCP) ایک کھلا پروٹوکول ہے جو اس بات کو معیاری بناتا ہے کہ ایپلیکیشنز LLMs کو کانٹیکسٹ کیسے فراہم کرتی ہیں۔ MCP کو AI ایپلیکیشنز کے لئے USB-C پورٹ سمجھیں - یہ AI ماڈلز کو مختلف ڈیٹا ذرائع اور ٹولز سے منسلک کرنے کا ایک معیاری طریقہ فراہم کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام پر، آپ قابل ہوں گے:

- C#، جاوا، پائتھون، ٹائپ اسکرپٹ، اور رسٹ میں MCP کے لئے ترقیاتی ماحول ترتیب دینا
- حسب ضرورت فیچرز (وسائل، پرامپٹس، اور ٹولز) کے ساتھ بنیادی MCP سرورز بنانا اور تعینات کرنا
- MCP سرورز سے رابطہ کرنے والی ہوسٹ ایپلیکیشنز بنانا
- MCP تنصیبات کی جانچ اور ڈیبگنگ کرنا

## اپنے MCP ماحول کی ترتیب

MCP کے ساتھ کام شروع کرنے سے پہلے، اپنے ترقیاتی ماحول کو تیار کرنا اور بنیادی ورک فلو کو سمجھنا ضروری ہے۔ یہ سیکشن ابتدائی ترتیب کے اقدامات کے ذریعے آپ کی رہنمائی کرے گا تاکہ MCP کے ساتھ ایک ہموار آغاز یقینی بنایا جا سکے۔

### پیشگی شرائط

MCP کی ترقی میں کودنے سے پہلے، یقینی بنائیں کہ آپ کے پاس موجود ہیں:

- **ترقیاتی ماحول**: آپ کی منتخب زبان کے لئے (C#، جاوا، پائتھون، ٹائپ اسکرپٹ، یا رسٹ)
- **IDE/ایڈیٹر**: Visual Studio، Visual Studio Code، IntelliJ، Eclipse، PyCharm، یا کوئی جدید کوڈ ایڈیٹر
- **پیکیج مینیجرز**: NuGet، Maven/Gradle، pip، npm/yarn، یا Cargo
- **API کیز**: کسی بھی AI سروسز کے لئے جو آپ اپنی ہوسٹ ایپلیکیشنز میں استعمال کرنے کا ارادہ رکھتے ہیں

## بنیادی MCP سرور کی ساخت

ایک MCP سرور عام طور پر شامل ہوتا ہے:

- **سرور کی ترتیب**: پورٹ، توثیق، اور دیگر سیٹنگز کا سیٹ اپ
- **وسائل**: ڈیٹا اور کانٹیکسٹ جو LLMs کو دستیاب ہوتا ہے
- **ٹولز**: وہ فنکشنلٹی جو ماڈلز کال کر سکتے ہیں
- **پرامپٹس**: ٹیکسٹ بنانے یا ترتیب دینے کے ٹیمپلیٹس

یہاں ٹائپ اسکرپٹ میں ایک آسان مثال ہے:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ایک MCP سرور بنائیں
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ایک اضافی آلہ شامل کریں
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ایک متحرک خوش آمدید وسیلہ شامل کریں
server.resource(
  "file",
  // 'list' پیرامیٹر کنٹرول کرتا ہے کہ وسیلہ دستیاب فائلوں کو کیسے فہرست کرتا ہے۔ اسے undefined پر سیٹ کرنا اس وسیلہ کے لیے فہرست سازی کو غیر فعال کر دیتا ہے۔
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

// stdin پر پیغامات وصول کرنا شروع کریں اور stdout پر پیغامات بھیجنا شروع کریں
const transport = new StdioServerTransport();
await server.connect(transport);
```

پچھلے کوڈ میں ہم نے:

- MCP ٹائپ اسکرپٹ SDK سے ضروری کلاسز کو درآمد کیا۔
- ایک نیا MCP سرور انسٹانس تخلیق اور ترتیب دیا۔
- ایک کسٹم ٹول (`calculator`) کو ہینڈلر فنکشن کے ساتھ رجسٹر کیا۔
- سرور کو MCP درخواستوں کے ان پٹ کے لئے سننے کے لئے شروع کیا۔

## ٹیسٹنگ اور ڈیبگنگ

اپنے MCP سرور کی جانچ شروع کرنے سے پہلے، دستیاب ٹولز اور ڈیبگنگ کی بہترین مشقوں کو سمجھنا ضروری ہے۔ مؤثر جانچ آپ کے سرور کے متوقع رویے کو یقینی بناتی ہے اور مسائل کو جلد از جلد پہچان کر حل کرنے میں مدد دیتی ہے۔ درج ذیل سیکشن آپ کی MCP تنصیب کی توثیق کے لئے تجویز کردہ طریقے بیان کرتا ہے۔

MCP آپ کے سرورز کی ٹیسٹنگ اور ڈیبگنگ میں مدد کے لئے ٹولز فراہم کرتا ہے:

- **انسپیکٹر ٹول**، یہ گرافیکل انٹرفیس آپ کو اپنے سرور سے کنیکٹ ہونے اور اپنے ٹولز، پرامپٹس، اور وسائل کی جانچ کرنے کی اجازت دیتا ہے۔
- **curl**، آپ اپنے سرور سے curl یا دیگر کلائنٹس جیسے کمانڈ لائن ٹول کے ذریعے بھی رابطہ کر سکتے ہیں جو HTTP کمانڈز بنا اور چلا سکتے ہیں۔

### MCP انسپیکٹر کا استعمال

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ایک بصری ٹیسٹنگ ٹول ہے جو آپ کی مدد کرتا ہے:

1. **سرور صلاحیتوں کی دریافت**: دستیاب وسائل، ٹولز، اور پرامپٹس خودکار طریقے سے معلوم کریں
2. **ٹول کی جانچ**: مختلف پیرا میٹرز آزمائیں اور حقیقی وقت میں جوابات دیکھیں
3. **سرور میٹا ڈیٹا دیکھیں**: سرور کی معلومات، اسکیموں، اور کنفیگریشنز کا معائنہ کریں

```bash
# جیسے TypeScript، MCP انسپکٹر انسٹال کرنا اور چلانا
npx @modelcontextprotocol/inspector node build/index.js
```

جب آپ اوپر دیے گئے کمانڈز چلائیں گے، MCP Inspector آپ کے براؤزر میں ایک لوکل ویب انٹرفیس شروع کرے گا۔ آپ کو اپنے رجسٹرڈ MCP سرورز، ان کے دستیاب ٹولز، وسائل، اور پرامپٹس دکھانے والا ڈیش بورڈ نظر آئے گا۔ یہ انٹرفیس آپ کو انٹریکٹو طریقے سے ٹولز کی جانچ کرنے، سرور میٹا ڈیٹا کی تفتیش کرنے، اور حقیقی وقت کے جوابات دیکھنے دیتا ہے، جو MCP سرور کی تنصیبات کی توثیق اور ڈیبگنگ کو آسان بناتا ہے۔

یہاں ایک اسکرین شاٹ ہے کہ یہ کیسا دکھ سکتا ہے:

![MCP Inspector server connection](../../../../translated_images/ur/connected.73d1e042c24075d3.webp)

## عام ترتیبی مسائل اور حل

| مسئلہ | ممکنہ حل |
|-------|-----------|
| کنکشن مسترد ہو گیا | چیک کریں کہ سرور چل رہا ہے اور پورٹ درست ہے |
| ٹول کی عملدرآمد میں غلطیاں | پیرامیٹر کی تصدیق اور غلطی کی ہینڈلنگ دیکھیں |
| توثیق کی ناکامیاں | API کیز اور اجازتیں چیک کریں |
| اسکیمہ کی جانچ میں غلطیاں | یقینی بنائیں کہ پیرامیٹرز تعین شدہ اسکیمہ سے میل کھاتے ہیں |
| سرور شروع نہیں ہو رہا | پورٹ کی ٹکراؤ یا گم شدہ انحصاریوں کو دیکھیں |
| CORS کی غلطیاں | کراس اوریجن درخواستوں کے لئے مناسب CORS ہیڈرز ترتیب دیں |
| توثیق کے مسائل | ٹوکن کی درستگی اور اجازتیں چیک کریں |

## مقامی ترقی

مقامی ترقی اور جانچ کے لئے، آپ اپنے کمپیوٹر پر براہ راست MCP سرور چلا سکتے ہیں:

1. **سرور عمل شروع کریں**: اپنا MCP سرور ایپلیکیشن چلائیں
2. **نیٹ ورکنگ ترتیب دیں**: یقینی بنائیں کہ سرور متوقع پورٹ پر دستیاب ہو
3. **کلائنٹس کنیکٹ کریں**: `http://localhost:3000` جیسے مقامی رابطہ URLs استعمال کریں

```bash
# مثال: ایک ٹائپ اسکرپٹ MCP سرور مقامی طور پر چلانا
npm run start
# سرور http://localhost:3000 پر چل رہا ہے
```

## اپنا پہلا MCP سرور بنانا

ہم نے ایک پچھلے سبق میں [بنیادی تصورات](../../01-CoreConcepts/README.md) کا احاطہ کیا، اب وقت ہے کہ اس علم کو عمل میں لائیں۔

### سرور کیا کچھ کر سکتا ہے

کوڈ لکھنے سے پہلے، آئیے یاد کریں کہ ایک سرور کیا کچھ کر سکتا ہے:

ایک MCP سرور مثلاً کر سکتا ہے:

- مقامی فائلوں اور ڈیٹا بیسز تک رسائی
- ریموٹ APIs سے رابطہ
- حساب کتاب انجام دینا
- دیگر ٹولز اور سروسز کے ساتھ انضمام
- تعامل کے لئے یوزر انٹرفیس فراہم کرنا

زبردست، اب جب ہم جانتے ہیں کہ ہم کیا کر سکتے ہیں، تو کوڈنگ شروع کرتے ہیں۔

## مشق: سرور بنانا

سرور بنانے کے لئے، آپ کو درج ذیل مراحل پر عمل کرنا ہوگا:

- MCP SDK انسٹال کریں۔
- ایک پروجیکٹ بنائیں اور پروجیکٹ کی ساخت ترتیب دیں۔
- سرور کا کوڈ لکھیں۔
- سرور کی جانچ کریں۔

### -1- پروجیکٹ بنائیں

#### TypeScript

```sh
# پراجیکٹ ڈائریکٹری بنائیں اور این پی ایم پراجیکٹ شروع کریں
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# پراجیکٹ ڈائریکٹری بنائیں
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

جاوا کے لیے، ایک اسپرنگ بوٹ پروجیکٹ بنائیں:

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
# غیر استعمال شدہ ٹیسٹ کو اختیاری طور پر ہٹائیں
rm -rf src/test/java
```

اپنی *pom.xml* فائل میں مکمل کنفیگریشن شامل کریں:

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

### -2- انحصاریات شامل کریں

اب جب آپ کا پروجیکٹ بن چکا ہے، اگلے مرحلے میں انحصاریات شامل کریں:

#### TypeScript

```sh
# اگر پہلے سے انسٹال نہیں ہے تو، TypeScript کو عالمی طور پر انسٹال کریں
npm install typescript -g

# سکیمہ کی توثیق کے لیے MCP SDK اور Zod انسٹال کریں
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# ایک ورچوئل اینوائرنمنٹ بنائیں اور انحصارات انسٹال کریں
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

*package.json* فائل کھولیں اور درج ذیل مواد سے تبدیل کریں تاکہ آپ سرور بنا اور چلا سکیں:

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

*tsconfig.json* بنائیں جس میں درج ذیل مواد ہو:

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

*server.py* فائل بنائیں:

```sh
touch server.py
```

#### .NET

ضروری NuGet پیکیجز انسٹال کریں:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

جاوا اسپرنگ بوٹ پروجیکٹس میں، پروجیکٹ کی ساخت خود بخود بن جاتی ہے۔

#### Rust

رسٹ کے لئے `cargo init` چلانے پر ڈیفالٹ کے طور پر *src/main.rs* فائل بن جاتی ہے۔ فائل کھولیں اور ڈیفالٹ کوڈ کو حذف کریں۔

### -4- سرور کوڈ بنائیں

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

اب آپ کے پاس ایک سرور ہے، لیکن یہ زیادہ کام نہیں کرتا، آئیے اسے بہتر بنائیں۔

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

جاوا کے لیے، بنیادی سرور کمپونینٹس بنائیں۔ پہلے، مین ایپلیکیشن کلاس کو ترمیم کریں:

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

**پروڈکشن کے لئے اختیاری کمپونینٹس:**

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

ایک استثناء ہینڈلر بنائیں *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // حاصل کنندہ
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

مندرجہ ذیل کوڈ *src/main.rs* فائل کے اوپر شامل کریں۔ یہ آپ کے MCP سرور کے لیے ضروری لائبریریاں اور ماڈیولز درآمد کرتا ہے۔

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

کیلکولیٹر سرور ایک سادہ سرور ہوگا جو دو نمبرز کو جمع کر سکتا ہے۔ آئیے ایک struct بنائیں جو کیلکولیٹر درخواست کی نمائندگی کرے۔

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

اگلا، ایک struct بنائیں جو کیلکولیٹر سرور کی نمائندگی کرے گا۔ یہ struct ٹول روٹر رکھے گا، جو ٹولز رجسٹر کرنے کے لیے استعمال ہوتا ہے۔

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

اب، ہم `Calculator` struct کو نافذ کریں گے تاکہ سرور کا نیا انسٹانس بنائیں اور سرور ہینڈلر کو نافذ کریں جو سرور کی معلومات فراہم کرے۔

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

آخر میں، ہمیں مین فنکشن نافذ کرنے کی ضرورت ہے تاکہ سرور شروع ہو سکے۔ یہ فنکشن `Calculator` struct کا ایک انسٹانس بنائے گا اور اسے اسٹینڈرڈ ان پٹ/آؤٹ پٹ پر سرور کرے گا۔

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

سرور اب خود کے بارے میں بنیادی معلومات فراہم کرنے کے لئے ترتیب دیا گیا ہے۔ اگلا، ہم ایک ٹول شامل کریں گے جو جمع کا عمل انجام دے۔

### -5- ایک ٹول اور وسیلہ شامل کرنا

مندرجہ ذیل کوڈ شامل کرکے ایک ٹول اور وسیلہ شامل کریں:

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

آپ کا ٹول `a` اور `b` پیرامیٹر لیتا ہے اور ایک فنکشن چلاتا ہے جو درج ذیل فارم میں جواب تیار کرتا ہے:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

آپ کا وسیلہ "greeting" سٹرنگ کے ذریعہ قابل رسائی ہے اور ایک پیرامیٹر `name` لیتا ہے اور ٹول کی طرح ایک جواب تیار کرتا ہے:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ایک اضافی آلہ شامل کریں
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ایک متحرک خوش آمدیدی ذریعہ شامل کریں
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

پچھلے کوڈ میں ہم نے:

- `add` نامی ٹول تعریف کی جس میں `a` اور `b` پیرامیٹرز شامل ہیں، دونوں انٹیجرز ہیں۔
- `greeting` نامی ایک وسیلہ تخلیق کیا جو `name` پیرامیٹر لیتا ہے۔

#### .NET

یہ اپنی Program.cs فائل میں شامل کریں:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

ٹولز پہلے مرحلے میں بن چکے ہیں۔

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
// stdin پر پیغامات وصول کرنا شروع کریں اور stdout پر پیغامات بھیجیں
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

// ایک متحرک خوش آمدید وسیلہ شامل کریں
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

// stdin پر پیغامات وصول کرنا اور stdout پر پیغامات بھیجنا شروع کریں
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

# مرکزی عملدرآمد بلاک - سرور چلانے کے لیے یہ ضروری ہے
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

رسٹ سرور کا آخری کوڈ اس طرح ہوگا:

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

ایسا کمانڈ چلائیں تاکہ سرور شروع ہو:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector استعمال کرنے کے لیے `mcp dev server.py` استعمال کریں جو خود بخود Inspector کو لانچ کرتا ہے اور ضروری پراکسی سیشن ٹوکن فراہم کرتا ہے۔ اگر `mcp run server.py` استعمال کرتے ہیں، تو آپ کو دستی طور پر Inspector شروع کرنا اور کنکشن ترتیب دینا ہوگا۔

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

سرور کو فارمیٹ اور چلانے کے لئے درج ذیل کمانڈز چلائیں:

```sh
cargo fmt
cargo run
```

### -8- انسپیکٹر کے ذریعے چلائیں

انسپیکٹر ایک زبردست ٹول ہے جو آپ کا سرور شروع کرتا ہے اور آپ کو اس کے ساتھ تعامل کرنے دیتا ہے تاکہ آپ جانچ سکیں کہ یہ کام کر رہا ہے۔ آئیے اسے شروع کریں:

> [!NOTE]
> "کمانڈ" فیلڈ میں یہ مختلف لگ سکتا ہے کیونکہ اس میں آپ کے مخصوص رن ٹائم کے ساتھ سرور چلانے کا کمانڈ شامل ہوتا ہے۔

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

یا اسے اپنے *package.json* میں اس طرح شامل کریں: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` اور پھر `npm run inspector` چلائیں۔

#### Python

پائتھون ایک Node.js ٹول انسپیکٹر کو لپیٹتا ہے۔ اس ٹول کو یوں کال کرنا ممکن ہے:

```sh
mcp dev server.py
```

تاہم، یہ تمام دستیاب طریقے نافذ نہیں کرتا، اس لیے آپ کو Node.js ٹول کو براہ راست چلانے کا مشورہ دیا جاتا ہے جیسا کہ نیچے ہے:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

اگر آپ کوئی ایسا ٹول یا IDE استعمال کر رہے ہیں جو سکرپٹس چلانے کے لئے کمانڈز اور ارگیومنٹس کو ترتیب دینے کی اجازت دیتا ہے،
یقینی بنائیں کہ `Command` فیلڈ میں `python` سیٹ ہو اور `Arguments` میں `server.py` ہو۔ اس سے اسکرپٹ صحیح طریقے سے چلتا ہے۔

#### .NET

یقینی بنائیں کہ آپ اپنے پروجیکٹ کے ڈائریکٹری میں ہیں:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### جاوا

یقینی بنائیں کہ آپ کا کیلکولیٹر سرور چل رہا ہے
اس کے بعد انسپیکٹر چلائیں:

```cmd
npx @modelcontextprotocol/inspector
```

انسپیکٹر ویب انٹرفیس میں:

1. "SSE" کو ٹرانسپورٹ قسم کے طور پر منتخب کریں
2. URL کو سیٹ کریں: `http://localhost:8080/sse`
3. "Connect" پر کلک کریں

![Connect](../../../../translated_images/ur/tool.163d33e3ee307e20.webp)

**اب آپ سرور سے منسلک ہیں**
**جاوا سرور ٹیسٹنگ کا سیکشن مکمل ہوچکا ہے**

اگلا سیکشن سرور کے ساتھ تعامل کے بارے میں ہے۔

آپ کو درج ذیل یوزر انٹرفیس نظر آنا چاہیے:

![Connect](../../../../translated_images/ur/connect.141db0b2bd05f096.webp)

1. سرور سے جڑنے کے لیے Connect بٹن منتخب کریں
  جب آپ سرور سے جڑ جائیں گے، آپ کو درج ذیل دکھائی دے گا:

  ![Connected](../../../../translated_images/ur/connected.73d1e042c24075d3.webp)

1. "Tools" اور "listTools" منتخب کریں، آپ کو "Add" ظاہر ہونا چاہیے، "Add" منتخب کریں اور پیرامیٹر ویلیوز بھریں۔

  آپ کو مندرجہ ذیل جواب نظر آئے گا، یعنی "add" ٹول سے نتیجہ:

  ![Result of running add](../../../../translated_images/ur/ran-tool.a5a6ee878c1369ec.webp)

مبارک ہو، آپ نے اپنا پہلا سرور بنانے اور چلانے میں کامیابی حاصل کر لی ہے!

#### رسٹ

MCP انسپیکٹر CLI کے ساتھ رسٹ سرور چلانے کے لیے درج ذیل کمانڈ استعمال کریں:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### سرکاری SDKs

MCP متعدد زبانوں کے لیے سرکاری SDKs فراہم کرتا ہے:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - مائیکروسافٹ کے تعاون سے مینٹینڈ
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI کے تعاون سے مینٹینڈ
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - سرکاری ٹائپ اسکرپٹ امپلیمینٹیشن
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - سرکاری پائتھن امپلیمینٹیشن
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - سرکاری کوٹلن امپلیمینٹیشن
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI کے تعاون سے مینٹینڈ
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - سرکاری رسٹ امپلیمینٹیشن

## اہم نکات

- MCP ڈیولپمنٹ ماحول کی ترتیب زبان مخصوص SDKs کے ساتھ آسان ہے
- MCP سرور بنانے کے لیے ٹولز بنانا اور واضح سکیموں کے ساتھ رجسٹر کرنا ضروری ہے
- قابل اعتماد MCP امپلیمینٹیشنز کے لیے ٹیسٹنگ اور ڈیبگنگ ضروری ہے

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھن کیلکولیٹر](../../../../03-GettingStarted/samples/python)
- [رسٹ کیلکولیٹر](../../../../03-GettingStarted/samples/rust)

## اسائنمنٹ

اپنی پسند کا ایک سادہ MCP سرور بنائیں:

1. منتخب زبان (.NET، جاوا، پائتھن، ٹائپ اسکرپٹ، یا رسٹ) میں ٹول امپلیمینٹ کریں۔
2. ان پٹ پیرامیٹرز اور ریٹرن ویلیوز کی تعریف کریں۔
3. انسپیکٹر ٹول چلائیں تاکہ سرور صحیح کام کرے۔
4. مختلف ان پٹس کے ساتھ امپلیمینٹیشن کا جائزہ لیں۔

## حل

[حل](./solution/README.md)

## اضافی وسائل

- [Azure پر Model Context Protocol کے ذریعے ایجنٹس بنائیں](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP ایجنٹ](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## اگلا کیا ہے

اگلا: [MCP کلائنٹس کے ساتھ شروع کرنا](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہِ کرم آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا غیر یقینی ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط ترجمانی کی ذمہ داری ہم پر عائد نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->