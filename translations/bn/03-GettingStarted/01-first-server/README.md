# MCP দিয়ে শুরু করা

> [!NOTE]
> এই পাঠের জাভা HTTP উদাহরণটি পুরানো HTTP+SSE পরিবহন ব্যবহার করে এবং
> MCP `2025-11-25` এর সাথে সামঞ্জস্যপূর্ণ SDK লক্ষ্য করে। নতুন রিমোট সার্ভারের জন্য,
> `2026-07-28` স্ট্রিমেবল HTTP পরিবহন ব্যবহার করুন এবং আপনার SDK এ সমর্থন যাচাই করুন।

মডেল কনটেক্সট প্রোটোকল (MCP) এর সাথে আপনার প্রথম পদক্ষেপে স্বাগতম! আপনি যদি MCP এ নতুন হন বা আপনার বোঝাপড়া গভীর করতে চান, এই গাইডটি মৌলিক সেটআপ এবং উন্নয়ন প্রক্রিয়ার মাধ্যমে আপনাকে নিয়ে যাবে। আপনি দেখতে পাবেন কিভাবে MCP এআই মডেল এবং অ্যাপ্লিকেশনের মধ্যে নির্বিঘ্ন ইন্টিগ্রেশন সক্ষম করে এবং শিখবেন কীভাবে দ্রুত আপনার পরিবেশ প্রস্তুত করবেন MCP-চালিত সমাধান তৈরি এবং পরীক্ষা করার জন্য।

> সংক্ষেপে; আপনি যদি AI অ্যাপ তৈরি করেন, আপনি জানেন যে আপনি আপনার LLM (large language model)-এ টুল এবং অন্যান্য সংস্থান যোগ করতে পারেন, যাতে LLM আরও জ্ঞানসম্পন্ন হয়। তবে যদি আপনি সেই টুল এবং সংস্থানগুলি সার্ভারে রাখেন, তাহলে অ্যাপ এবং সার্ভার ক্ষমতা যেকোন ক্লায়েন্ট দ্বারা ব্যবহার করা যেতে পারে LLM সহ/বিনা।

## সংক্ষিপ্ত বিবরণ

এই পাঠে MCP পরিবেশ চালু করার এবং আপনার প্রথম MCP অ্যাপ্লিকেশন তৈরি করার ব্যবহারিক নির্দেশনা দেওয়া হয়েছে। আপনি শিখবেন প্রয়োজনীয় টুল ও ফ্রেমওয়ার্ক সেটআপ করা, মৌলিক MCP সার্ভার তৈরি করা, হোস্ট অ্যাপ্লিকেশন তৈরি করা এবং আপনার বাস্তবায়ন পরীক্ষা করা।

মডেল কনটেক্সট প্রোটোকল (MCP) একটি উন্মুক্ত প্রোটোকল যা অ্যাপ্লিকেশনগুলি কীভাবে LLM-এ প্রসঙ্গ সরবরাহ করে তা মানকরণ করে। MCP কে ভাবুন AI অ্যাপ্লিকেশনগুলির জন্য একটি USB-C পোর্টের মতো - এটি একটি মানানসই উপায় প্রদান করে AI মডেলগুলিকে বিভিন্ন ডেটা উৎস এবং টুলের সাথে সংযোগের জন্য।

## শেখার উদ্দেশ্য

এই পাঠ শেষে, আপনি পারবেন:

- C#, Java, Python, TypeScript, এবং Rust এ MCP উন্নয়ন পরিবেশ গড়ে তোলা
- কাস্টম বৈশিষ্ট্য (সংস্থান, প্রম্পট, এবং টুল) সহ মৌলিক MCP সার্ভার তৈরি ও প্রয়োগ করা
- MCP সার্ভারগুলোর সাথে সংযুক্ত হোস্ট অ্যাপ্লিকেশন তৈরি করা
- MCP বাস্তবায়ন পরীক্ষা ও ডিবাগ করা

## আপনার MCP পরিবেশ সেটআপ করা

MCP নিয়ে কাজ শুরু করার আগে, আপনার উন্নয়ন পরিবেশ প্রস্তুত করা এবং মৌলিক কার্যপ্রবাহ বোঝা গুরুত্বপূর্ণ। এই অংশ আপনাকে প্রাথমিক সেটআপ ধাপগুলো দিয়ে গাইড করবে, MCP দিয়ে সুষ্ঠু শুরু নিশ্চিত করার জন্য।

### পূর্বপ্রয়োজনীয়তা

MCP উন্নয়নে প্রবেশের আগে নিশ্চিত করুন আপনার কাছে আছে:

- **উন্নয়ন পরিবেশ**: আপনার পছন্দসই ভাষার জন্য (C#, Java, Python, TypeScript, অথবা Rust)
- **আইডিই/এডিটর**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm বা যেকোন আধুনিক কোড এডিটর
- **প্যাকেজ ম্যানেজার**: NuGet, Maven/Gradle, pip, npm/yarn, অথবা Cargo
- **এপিআই কী**: যেকোন AI সার্ভিসের জন্য যা আপনি আপনার হোস্ট অ্যাপ্লিকেশনগুলোতে ব্যবহার করতে চান

## মৌলিক MCP সার্ভার স্ট্রাকচার

সাধারণত একটি MCP সার্ভারে থাকে:

- **সার্ভার কনফিগারেশন**: পোর্ট, প্রমাণীকরণ এবং অন্যান্য সেটিংস সেটআপ করা
- **সংস্থান**: LLM গুলোর জন্য ডেটা এবং প্রসঙ্গ প্রদান করা
- **টুলস**: কার্যকারিতা যা মডেলগুলি কল করতে পারে
- **প্রম্পট**: লেখার জন্য টেমপ্লেট বা গঠন

এখানে TypeScript এ একটি সরল উদাহরণ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// একটি MCP সার্ভার তৈরি করুন
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// একটি অ্যাডিশন টুল যোগ করুন
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// একটি ডায়নামিক শুভেচ্ছা সম্পদ যোগ করুন
server.resource(
  "file",
  // 'list' প্যারামিটারটি কিভাবে রিসোর্স উপলভ্য ফাইলগুলো তালিকাভুক্ত করবে তা নিয়ন্ত্রণ করে। এটি undefined এ সেট করলে এই রিসোর্সের জন্য তালিকাভুক্তি নিষ্ক্রিয় হবে।
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// একটি ফাইল রিসোর্স যোগ করুন যা ফাইলের বিষয়বস্তু পড়ে
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

// stdin থেকে মেসেজ গ্রহণ করা শুরু করুন এবং stdout এ মেসেজ পাঠানো শুরু করুন
const transport = new StdioServerTransport();
await server.connect(transport);
```

উপরের কোডে আমরা:

- MCP TypeScript SDK থেকে প্রয়োজনীয় ক্লাস আমদানি করেছি।
- একটি নতুন MCP সার্ভার ইনস্ট্যান্স তৈরি ও কনফিগার করেছি।
- একটি কাস্টম টুল (`calculator`) নিবন্ধিত করেছি একটি হ্যান্ডলার ফাংশন সহ।
- আসন্ন MCP অনুরোধের জন্য সার্ভার শুরু করেছি।

## পরীক্ষা ও ডিবাগিং

আপনার MCP সার্ভারের পরীক্ষা শুরু করার আগে, উপলব্ধ টুলস এবং ডিবাগিংয়ের সেরা অনুশীলনগুলি বোঝা গুরুত্বপূর্ণ। কার্যকর পরীক্ষা নিশ্চিত করে আপনার সার্ভারের প্রত্যাশিত আচরণ এবং দ্রুত সমস্যা সনাক্ত এবং সমাধান করতে সাহায্য করে। নিম্নলিখিত অংশ আপনার MCP বাস্তবায়ন যাচাই করার সুপারিশকৃত পদ্ধতিগুলো বর্ণনা করে।

MCP সরঞ্জাম সরবরাহ করে যা আপনার সার্ভার পরীক্ষা ও ডিবাগে সহায়তা করে:

- **ইন্সপেক্টর টুল**, এই গ্রাফিক্যাল ইন্টারফেস আপনাকে সার্ভারে যুক্ত হয়ে আপনার টুল, প্রম্পট এবং সংস্থান পরীক্ষা করার সুযোগ দেয়।
- **curl**, আপনি কمان্ড লাইন টুল curl বা অন্যান্য ক্লায়েন্ট ব্যবহার করেও সার্ভারে সংযোগ করতে পারেন যারা HTTP কমান্ড তৈরি ও চালাতে পারে।

### MCP ইন্সপেক্টর ব্যবহার করা

[MCP ইন্সপেক্টর](https://github.com/modelcontextprotocol/inspector) একটি ভিজ্যুয়াল টেস্টিং টুল যা আপনাকে সাহায্য করে:

1. **সার্ভার ক্ষমতা আবিষ্কার করা**: স্বয়ংক্রিয়ভাবে উপলব্ধ সংস্থান, টুল এবং প্রম্পট সনাক্ত করা
2. **টুল এক্সিকিউশন পরীক্ষা করা**: বিভিন্ন প্যারামিটার চেষ্টা করা এবং রিয়েল-টাইম প্রতিক্রিয়া দেখা
3. **সার্ভার মেটাডাটা দেখা**: সার্ভারের তথ্য, স্কিমা এবং কনফিগারেশন পরীক্ষা করা

```bash
# উদাহরণ TypeScript, MCP ইনস্পেক্টর ইনস্টল এবং চালানো
npx @modelcontextprotocol/inspector node build/index.js
```

উপরের কমান্ডগুলো চালালে, MCP ইন্সপেক্টর আপনার ব্রাউজারে একটি লোকাল ওয়েব ইন্টারফেস চালু করবে। আপনি একটি ড্যাশবোর্ড দেখতে পাবেন যা আপনার নিবন্ধিত MCP সার্ভার, তাদের উপলব্ধ টুল, সংস্থান এবং প্রম্পট প্রদর্শন করবে। ইন্টারফেস ইন্টারেক্টিভলি টুল এক্সিকিউশন পরীক্ষা, সার্ভার মেটাডাটা পরিদর্শন, এবং রিয়েল-টাইম প্রতিক্রিয়া দেখা সহজ করে, যা MCP সার্ভার বাস্তবায়নগুলি যাচাই ও ডিবাগ করা সহজ করে তোলে।

এরকম একটি স্ক্রিনশট এখানে দেওয়া হলো:

![MCP Inspector server connection](../../../../translated_images/bn/connected.73d1e042c24075d3.webp)

## সাধারণ সেটআপ সমস্যা ও সমাধান

| সমস্যা | সম্ভাব্য সমাধান |
|-------|-------------------|
| সংযোগ প্রত্যাখ্যাত | সার্ভার চলছে কি না এবং পোর্ট সঠিক কি না পরীক্ষা করুন |
| টুল পরিচালনা ত্রুটি | প্যারামিটার যাচাই এবং ত্রুটি পরিচালনা রিভিউ করুন |
| প্রমাণীকরণ ব্যর্থতা | API কী এবং অনুমতি সঠিক কিনা যাচাই করুন |
| স্কিমা যাচাই ত্রুটি | প্যারামিটার সংজ্ঞায়িত স্কিমা মেনে চলছে কি না নিশ্চিত করুন |
| সার্ভার শুরু হয় না | পোর্ট সংঘাত বা অনুপস্থিত নির্ভরশীলতা যাচাই করুন |
| CORS ত্রুটি | ক্রস-অরিজিন অনুরোধের জন্য সঠিক CORS হেডার কনফিগার করুন |
| প্রমাণীকরণ সমস্যা | টোকেন বৈধতা ও অনুমতি যাচাই করুন |

## লোকাল উন্নয়ন

লোকাল উন্নয়ন এবং পরীক্ষার জন্য, আপনি সরাসরি আপনার মেশিনে MCP সার্ভার চালাতে পারেন:

1. **সার্ভার প্রসেস শুরু করুন**: আপনার MCP সার্ভার অ্যাপ্লিকেশন চালান
2. **নেটওয়ার্কিং কনফিগার করুন**: সার্ভার প্রত্যাশিত পোর্টে অ্যাক্সেসযোগ্য কিনা নিশ্চিত করুন
3. **ক্লায়েন্ট সংযোগ করুন**: লোকাল সংযোগ URL ব্যবহার করুন যেমন `http://localhost:3000`

```bash
# উদাহরণ: লোকালিতে একটি টাইপস্ক্রিপ্ট MCP সার্ভার চালানো
npm run start
# সার্ভার চলছে http://localhost:3000 এ
```

## আপনার প্রথম MCP সার্ভার তৈরি করা

আমরা পূর্বেকার পাঠে [মূল ধারণা](../../01-CoreConcepts/README.md) আলোচনা করেছি, এখন সেই জ্ঞান কাজে লাগানোর সময়।

### একটি সার্ভার কী করতে পারে

কোড লেখা শুরু করার আগে, আসুন মনে করিয়ে দিই একটি সার্ভার কী করতে পারে:

একটি MCP সার্ভার উদাহরণস্বরূপ করতে পারে:

- স্থানীয় ফাইল এবং ডাটাবেস অ্যাক্সেস করা
- দূরবর্তী API গুলোর সাথে সংযোগ করা
- গণনা/হিসাব করা
- অন্যান্য টুল ও সার্ভিসের সাথে ইন্টিগ্রেট করা
- ইন্টারঅ্যাকশনের জন্য একটি ব্যবহারকারী ইন্টারফেস প্রদান করা

চমৎকার, এখন যেহেতু আমরা জানি এটি কী করতে পারে, চলুন কোডিং শুরু করি।

## অনুশীলন: একটি সার্ভার তৈরি করা

একটি সার্ভার তৈরি করতে, আপনাকে নিম্নলিখিত ধাপগুলো অনুসরণ করতে হবে:

- MCP SDK ইনস্টল করুন।
- একটি প্রোজেক্ট তৈরি করে প্রোজেক্ট কাঠামো সেটআপ করুন।
- সার্ভার কোড লিখুন।
- সার্ভার পরীক্ষা করুন।

### -1- প্রোজেক্ট তৈরি

#### TypeScript

```sh
# প্রকল্প ডিরেক্টরি তৈরি করুন এবং npm প্রকল্প শুরু করুন
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# প্রজেক্ট ডিরেক্টরি তৈরি করুন
mkdir calculator-server
cd calculator-server
# ভিজ্যুয়াল স্টুডিও কোডে ফোল্ডারটি খুলুন - আপনি যদি অন্য কোনও আইডিই ব্যবহার করেন তবে এটি উপেক্ষা করুন
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

জাভার জন্য, একটি Spring Boot প্রোজেক্ট তৈরি করুন:

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

জিপ ফাইল আনজিপ করুন:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ঐচ্ছিকভাবে ব্যবহার না হওয়া টেস্ট মুছে ফেলুন
rm -rf src/test/java
```

আপনার *pom.xml* ফাইলে নিম্নোক্ত সম্পূর্ণ কনফিগারেশন যোগ করুন:

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

### -2- ডিপেনডেন্সি যোগ করা

এখন যখন আপনার প্রোজেক্ট তৈরি হয়েছে, পরবর্তী ধাপে ডিপেনডেন্সি যোগ করুন:

#### TypeScript

```sh
# যদি ইতিমধ্যে ইনস্টল না করা থাকে, TypeScript গ্লোবালি ইনস্টল করুন
npm install typescript -g

# MCP SDK এবং Zod ইনস্টল করুন স্কিমা ভ্যালিডেশনের জন্য
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# একটি ভার্চুয়াল এনভ তৈরি করুন এবং নির্ভরশীলতাগুলি ইনস্টল করুন
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

### -3- প্রোজেক্ট ফাইল তৈরি

#### TypeScript

*package.json* ফাইল খুলুন এবং নিম্নলিখিত কন্টেন্ট দিয়ে প্রতিস্থাপন করুন যাতে সার্ভার তৈরি ও চালানো যায়:

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

একটি *tsconfig.json* তৈরি করুন নিম্নরূপ:

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

আপনার সোর্স কোডের জন্য একটি ডিরেক্টরি তৈরি করুন:

```sh
mkdir src
touch src/index.ts
```

#### Python

একটি *server.py* ফাইল তৈরি করুন

```sh
touch server.py
```

#### .NET

প্রয়োজনীয় NuGet প্যাকেজ ইনস্টল করুন:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot প্রোজেক্টের জন্য, প্রোজেক্ট স্ট্রাকচার স্বয়ংক্রিয়ভাবে তৈরি হয়।

#### Rust

Rust এর জন্য, *src/main.rs* ফাইল ডিফল্টভাবে `cargo init` কমান্ড দেয়ার সময় তৈরি হয়। ফাইলটি খুলে ডিফল্ট কোড মুছে ফেলুন।

### -4- সার্ভার কোড তৈরি করা

#### TypeScript

একটি *index.ts* ফাইল তৈরি করুন এবং নিম্নলিখিত কোড যোগ করুন:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// একটি MCP সার্ভার তৈরি করুন
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

এখন আপনার একটি সার্ভার আছে, কিন্তু এটি বেশি কিছু করে না, চলুন ঠিক করি।

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# একটি MCP সার্ভার তৈরি করুন
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

জাভার জন্য, মুল সার্ভার উপাদান তৈরি করুন। প্রথমে প্রধান অ্যাপ্লিকেশন ক্লাসটি পরিবর্তন করুন:

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

ক্যালকুলেটর সার্ভিস তৈরি করুন *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**প্রোডাকশন-রেডি সার্ভিসের জন্য ঐচ্ছিক উপাদান:**

স্টার্টআপ কনফিগারেশন তৈরি করুন *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

একটি হেলথ কন্ট্রোলার তৈরি করুন *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

একটি এক্সসেপশন হ্যান্ডলার তৈরি করুন *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // গেটারস্
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

একটি কাস্টম ব্যানার তৈরি করুন *src/main/resources/banner.txt*:

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

*src/main.rs* ফাইলের শীর্ষে নিম্নলিখিত কোড যোগ করুন। এটি আপনার MCP সার্ভারের জন্য প্রয়োজনীয় লাইব্রেরি এবং মডিউল ইম্পোর্ট করে।

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

ক্যালকুলেটর সার্ভারটি একটি সহজ সার্ভার হবে যা দুটি সংখ্যা যোগ করতে পারবে। চলুন একটি স্ট্রাক্ট তৈরি করি যা ক্যালকুলেটর অনুরোধ প্রতিনিধিত্ব করবে।

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

পরবর্তীতে, একটি স্ট্রাক্ট তৈরি করুন যা ক্যালকুলেটর সার্ভার প্রতিনিধিত্ব করবে। এই স্ট্রাক্টে থাকবে টুল রাউটার, যা টুল নিবন্ধন করতে ব্যবহৃত হয়।

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

এখন, আমরা `Calculator` স্ট্রাক্ট বাস্তবায়ন করতে পারি যা সার্ভারের একটি নতুন ইনস্ট্যান্স তৈরি করে এবং সার্ভার হ্যান্ডলার বাস্তবায়ন করে সার্ভারের তথ্য প্রদান করে।

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

অবশেষে, সার্ভার শুরু করার জন্য প্রধান ফাংশনটি বাস্তবায়ন করা দরকার। এই ফাংশনটি `Calculator` স্ট্রাক্টের একটি ইনস্ট্যান্স তৈরি করবে এবং এটি স্ট্যান্ডার্ড ইনপুট/আউটপুট এর মাধ্যমে পরিবেশন করবে।

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

সার্ভার এখন নিজেকে সম্পর্কে মৌলিক তথ্য সরবরাহের জন্য প্রস্তুত। পরবর্তীতে, আমরা একটি টুল যোগ করব যা যোগফল করবে।

### -5- একটি টুল এবং একটি সংস্থান যোগ করা

নিম্নলিখিত কোড যোগ করে একটি টুল এবং একটি সংস্থান যোগ করুন:

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

আপনার টুলের প্যারামিটারসমূহ `a` এবং `b` থাকে এবং এটি একটি ফাংশন চালায় যা নিম্নরূপ একটি প্রতিক্রিয়া তৈরি করে:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

আপনার সংস্থান `"greeting"` স্ট্রিং-এর মাধ্যমে অ্যাক্সেস করা হয়, এটি `name` প্যারামিটার নেয় এবং টুলের মতো একটি প্রতিক্রিয়া তৈরি করে:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# একটি যোগফল সরঞ্জাম যোগ করুন
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# একটি গতিশীল অভ্যর্থনা সম্পদ যোগ করুন
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

পূর্ববর্তী কোডে আমরা:

- `add` নামে একটি টুল সংজ্ঞায়িত করেছি যা `a` এবং `b` প্যারামিটার নেয়, উভয়ই পূর্ণসংখ্যা।
- `greeting` নামে একটি সংস্থান তৈরি করেছি যা `name` প্যারামিটার নেয়।

#### .NET

আপনার Program.cs ফাইলে এটি যোগ করুন:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

টুলগুলো পূর্ববর্তী ধাপে ইতিমধ্যে তৈরি করা হয়েছে।

#### Rust

`impl Calculator` ব্লকের ভিতরে একটি নতুন টুল যোগ করুন:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- চূড়ান্ত কোড

চলুন শেষ কোড যোগ করি যাতে সার্ভার শুরু হতে পারে:

#### TypeScript

```typescript
// stdin এ মেসেজ গ্রহণ শুরু এবং stdout এ মেসেজ পাঠানো শুরু করুন
const transport = new StdioServerTransport();
await server.connect(transport);
```

এখানে সম্পূর্ণ কোড:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// একটি MCP সার্ভার তৈরি করুন
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// একটি যোগ করার সরঞ্জাম যোগ করুন
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// একটি গতিশীল অভিবাদন সম্পদ যোগ করুন
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

// stdin এ বার্তা গ্রহণ শুরু করুন এবং stdout এ বার্তা প্রেরণ করুন
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# একটি MCP সার্ভার তৈরি করুন
mcp = FastMCP("Demo")


# একটি যোগফল টুল যোগ করুন
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# একটি গতিশীল অভিবাদন সম্পদ যোগ করুন
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# প্রধান কার্যকরী ব্লক - এটি সার্ভার চালানোর জন্য প্রয়োজন হয়
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Program.cs ফাইলটি নিম্নলিখিত কন্টেন্টের সাথে তৈরি করুন:

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

আপনার সম্পূর্ণ প্রধান অ্যাপ্লিকেশন ক্লাসটি এরকম দেখাবে:

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

Rust সার্ভারের শেষ কোডটি এরকম হওয়া উচিত:

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

### -7- সার্ভার পরীক্ষা করা

নীচের কমান্ড দিয়ে সার্ভার চালু করুন:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP ইন্সপেক্টর ব্যবহার করতে, `mcp dev server.py` ব্যবহার করুন যা স্বয়ংক্রিয়ভাবে ইন্সপেক্টর চালু করে এবং প্রয়োজনীয় প্রক্সি সেশন টোকেন প্রদান করে। `mcp run server.py` ব্যবহার করলে, আপনাকে ম্যানুয়ালি ইন্সপেক্টর চালু করে সংযোগ কনফিগার করতে হবে।

#### .NET

নিশ্চিত করুন আপনি আপনার প্রোজেক্ট ডিরেক্টরিতে আছেন:

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

সার্ভার ফরম্যাট ও চালানোর জন্য নিম্নলিখিত কমান্ড গুলো চালান:

```sh
cargo fmt
cargo run
```

### -8- ইন্সপেক্টর ব্যবহার করে চালনা

ইন্সপেক্টর একটি অসাধারণ টুল যা আপনার সার্ভার চালু করতে পারে এবং আপনার সাথে ইন্টারঅ্যাক্ট করতে দেয় যাতে আপনি পরীক্ষা করতে পারেন এটি কাজ করছে কি না। চলুন শুরু করি:

> [!NOTE]
> "command" ফিল্ডে এটি বিভিন্ন দেখতে পারে কারণ এতে আপনার নির্দিষ্ট রানটাইম/সহ সার্ভার চালানোর কমান্ড থাকে।

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

অথবা এটিকে আপনার *package.json* এ এইভাবে যোগ করুন: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` এবং এরপর চালান `npm run inspector`

#### Python

Python একটি Node.js টুল inspector র‍্যাপ করে। নিম্নরূপ এটি কল করা সম্ভব:

```sh
mcp dev server.py
```


যাই হোক না কেন, এটি টুলে উপলব্ধ সমস্ত পদ্ধতি বাস্তবায়ন করে না, তাই নিচের মতো সরাসরি Node.js টুল চালানোর পরামর্শ দেওয়া হয়:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

আপনি যদি এমন কোনও টুল বা IDE ব্যবহার করেন যা স্ক্রিপ্ট চালানোর জন্য কমান্ড এবং আর্গুমেন্ট কনফিগার করতে দেয়,
নিশ্চিত করুন `Command` ক্ষেত্রের মধ্যে `python` এবং `Arguments` হিসেবে `server.py` সেট করা হয়েছে। এতে স্ক্রিপ্ট সঠিকভাবে চলবে।

#### .NET

নিশ্চিত করুন আপনি আপনার প্রকল্প ডিরেক্টরিতে আছেন:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

নিশ্চিত করুন আপনার ক্যালকুলেটর সার্ভার চলছে
এরপর ইনস্পেক্টর চালান:

```cmd
npx @modelcontextprotocol/inspector
```

ইনস্পেক্টরের ওয়েব ইন্টারফেসে:

1. ট্রান্সপোর্ট টাইপ হিসেবে "SSE" নির্বাচন করুন
2. URL সেট করুন: `http://localhost:8080/sse`
3. "Connect" ক্লিক করুন

![Connect](../../../../translated_images/bn/tool.163d33e3ee307e20.webp)

**আপনি এখন সার্ভারের সাথে সংযুক্ত হয়েছেন**
**Java সার্ভার টেস্টিং অংশ সম্পন্ন হয়েছে**

পরবর্তী অংশ হলো সার্ভারের সাথে ইন্টারঅ্যাক্ট করা।

আপনি নিচের ইউজার ইন্টারফেস দেখতে পাবেন:

![Connect](../../../../translated_images/bn/connect.141db0b2bd05f096.webp)

1. Connect বোতামটি নির্বাচন করে সার্ভারের সাথে সংযুক্ত হন
  সার্ভারের সাথে সংযুক্ত হলে আপনি নিচেরটি দেখতে পাবেন:

  ![Connected](../../../../translated_images/bn/connected.73d1e042c24075d3.webp)

1. "Tools" থেকে "listTools" নির্বাচন করুন, "Add" প্রদর্শিত হওয়া উচিত, "Add" নির্বাচন করুন এবং প্যারামিটার মান পূরণ করুন।

  আপনি নিচের প্রতিক্রিয়া দেখতে পাবেন, অর্থাৎ "add" টুল থেকে ফলাফল:

  ![Result of running add](../../../../translated_images/bn/ran-tool.a5a6ee878c1369ec.webp)

অভিনন্দন, আপনি সফলভাবে আপনার প্রথম সার্ভার তৈরি ও চালাতে পেরেছেন!

#### Rust

MCP ইনস্পেক্টর CLI দিয়ে Rust সার্ভার চালানোর জন্য নিম্নলিখিত কমান্ড ব্যবহার করুন:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### সরকারী SDKs

MCP বিভিন্ন ভাষার জন্য সরকারী SDK প্রদান করে:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - মাইক্রোসফটের সহযোগিতায় রক্ষণাবেক্ষণ করা হচ্ছে
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI এর সহযোগিতায় রক্ষণাবেক্ষণ
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - সরকারী TypeScript বাস্তবায়ন
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - সরকারী Python বাস্তবায়ন
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - সরকারী Kotlin বাস্তবায়ন
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI এর সহযোগিতায় রক্ষণাবেক্ষণ
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - সরকারী Rust বাস্তবায়ন

## প্রধান বিষয়াবলী

- MCP ডেভেলপমেন্ট পরিবেশ সেটআপ করা ভাষাভিত্তিক SDK গুলোর সাহায্যে সহজ
- MCP সার্ভার তৈরি মানে স্পষ্ট স্কিমা সহ টুল তৈরি ও রেজিস্টার করা
- সফল MCP বাস্তবায়নের জন্য টেস্টিং এবং ডিবাগিং গুরুত্বপূর্ণ

## নমুনা

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## অ্যাসাইনমেন্ট

আপনার পছন্দের একটি টুল নিয়ে একটি সহজ MCP সার্ভার তৈরি করুন:

1. আপনার পছন্দের ভাষায় ( .NET, Java, Python, TypeScript, অথবা Rust) টুলটি বাস্তবায়ন করুন।
2. ইনপুট প্যারামিটার ও রিটার্ন মান নির্ধারণ করুন।
3. সার্ভার সঠিকভাবে কাজ করছে কিনা নিশ্চিত করতে ইনস্পেক্টর টুল চালান।
4. বিভিন্ন ইনপুট দিয়ে বাস্তবায়নটি পরীক্ষা করুন।

## সমাধান

[Solution](./solution/README.md)

## অতিরিক্ত সংস্থান

- [Azure এ Model Context Protocol ব্যবহার করে এজেন্ট তৈরি করা](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps (Node.js/TypeScript/JavaScript) সহ Remote MCP](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## পরবর্তী

পরবর্তী: [MCP ক্লায়েন্ট শুরু করা](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->