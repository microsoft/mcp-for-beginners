# MCP দিয়ে শুরু করা

Model Context Protocol (MCP) এর সাথে আপনার প্রথম পদক্ষেপে স্বাগতম! আপনি MCP-তে নতুন হোন বা আপনার জ্ঞান বাড়াতে চান, এই গাইডটি আপনাকে অনিবার্য সেটআপ এবং উন্নয়ন প্রক্রিয়ার মাধ্যমে নিয়ে যাবে। আপনি জানবেন কিভাবে MCP AI মডেল এবং অ্যাপ্লিকেশনগুলোর মধ্যে নির্বিঘ্ন সংযোগ সক্ষম করে, এবং দ্রুত আপনার পরিবেশ প্রস্তুত করে MCP-ভিত্তিক সমাধান তৈরি ও পরীক্ষা করতে শিখবেন।

> সংক্ষেপে; আপনি যদি AI অ্যাপ তৈরি করেন, তাহলে জানেন যে আপনি আপনার LLM (বড় ভাষা মডেল)-এ টুল এবং অন্যান্য সম্পদ যুক্ত করতে পারেন, যাতে LLM আরও জ্ঞানী হয়। তবে যদি আপনি সেই টুল এবং সম্পদ সার্ভারে রাখেন, তাহলে অ্যাপ এবং সার্ভারের সক্ষমতা যেকোন ক্লায়েন্ট দ্বারা LLM সহ বা ছাড়াই ব্যবহার করা যায়।

## ওভারভিউ

এই পাঠটি MCP পরিবেশ সেটআপ এবং আপনার প্রথম MCP অ্যাপ্লিকেশন তৈরি করার জন্য ব্যবহারিক নির্দেশনা দেয়। আপনি জানবেন প্রয়োজনীয় টুল এবং ফ্রেমওয়ার্ক কিভাবে সেটআপ করবেন, বেসিক MCP সার্ভার তৈরি করবেন, হোস্ট অ্যাপ্লিকেশন তৈরি করবেন এবং আপনার ইমপ্লিমেন্টেশনগুলি পরীক্ষা করবেন।

Model Context Protocol (MCP) একটি ওপেন প্রোটোকল যা অ্যাপ্লিকেশনগুলো কিভাবে LLM কে প্রসঙ্গ সরবরাহ করে তা মানক করে। MCP কে ভাবুন AI অ্যাপ্লিকেশনের জন্য USB-C পোর্টের মতো — এটি AI মডেলগুলোকে বিভিন্ন ডেটা উত্স ও টুলগুলোর সাথে সংযুক্ত করার একটি মানক পদ্ধতি প্রদান করে।

## শেখার উদ্দেশ্য

এই পাঠের শেষে আপনি সক্ষম হবেন:

- C#, Java, Python, TypeScript, এবং Rust-এ MCP ডেভেলপমেন্ট পরিবেশ সেটআপ করা
- কাস্টম বৈশিষ্ট্য (সম্পদ, প্রম্পট, এবং টুল) সহ বেসিক MCP সার্ভার তৈরি ও ডিপ্লয় করা
- MCP সার্ভারের সাথে সংযুক্ত হোস্ট অ্যাপ্লিকেশন তৈরি করা
- MCP ইমপ্লিমেন্টেশন পরীক্ষা ও ডিবাগ করা

## আপনার MCP পরিবেশ সেটআপ করা

MCP নিয়ে কাজ শুরু করার আগে, এটি গুরুত্বপূর্ণ যে আপনি আপনার ডেভেলপমেন্ট পরিবেশ প্রস্তুত করুন এবং মৌলিক ওয়ার্কফ্লো বুঝে নিন। এই বিভাগটি আপনাকে প্রাথমিক সেটআপ ধাপগুলোতে গাইড করবে যাতে MCP দিয়ে মসৃণ শুরু নিশ্চিত হয়।

### প্রাক-প্রয়োজনীয়তা

MCP ডেভেলপমেন্টে ডুব দেওয়ার আগে নিশ্চিত করুন আপনার কাছে আছে:

- **ডেভেলপমেন্ট পরিবেশ**: আপনার নির্বাচিত ভাষার জন্য (C#, Java, Python, TypeScript, বা Rust)
- **IDE/এডিটর**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, বা যে কোনো আধুনিক কোড এডিটর
- **প্যাকেজ ম্যানেজার**: NuGet, Maven/Gradle, pip, npm/yarn, বা Cargo
- **API কী**: যে কোনো AI সেবা ব্যবহারের জন্য আপনার হোস্ট অ্যাপ্লিকেশনে

## বেসিক MCP সার্ভার স্ট্রাকচার

একটি MCP সার্ভারে সাধারণত থাকে:

- **সার্ভার কনফিগারেশন**: পোর্ট, অথেনটিকেশন, এবং অন্যান্য সেটিংস কনফিগারেশন
- **সম্পদসমূহ**: LLM-এর জন্য উপলব্ধ ডেটা ও প্রসঙ্গ
- **টুলস**: যা মডেলগুলো কল করতে পারে এমন কার্যকারিতা
- **প্রম্পটস**: টেক্সট তৈরি বা গঠন করার টেমপ্লেট

এখানে TypeScript-এ একটি সরল উদাহরণ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// একটি MCP সার্ভার তৈরি করুন
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// একটি যোগ করার টুল যুক্ত করুন
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// একটি গতিশীল স্বাগত রিসোর্স যোগ করুন
server.resource(
  "file",
  // 'list' প্যারামিটার রিসোর্সটি কীভাবে উপলব্ধ ফাইলগুলি তালিকাভুক্ত করে তা নিয়ন্ত্রণ করে। এটিকে undefined এ সেট করলে এই রিসোর্সের জন্য তালিকা বন্ধ হয়ে যায়।
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

// stdin এ মেসেজ গ্রহণ করা এবং stdout এ মেসেজ প্রেরণ শুরু করুন
const transport = new StdioServerTransport();
await server.connect(transport);
```

উপরের কোডে আমরা:

- MCP TypeScript SDK থেকে প্রয়োজনীয় ক্লাসগুলো ইমপোর্ট করেছি।
- একটি নতুন MCP সার্ভার ইনস্ট্যান্স তৈরি ও কনফিগার করেছি।
- একটি কাস্টম টুল (`calculator`) একটি হ্যান্ডলার ফাংশনের মাধ্যমে রেজিস্টার করেছি।
- সার্ভারটি শুরু করেছি যেটি আসন্ন MCP অনুরোধ শুনবে।

## পরীক্ষা এবং ডিবাগিং

আপনার MCP সার্ভার পরীক্ষা করার আগে উপলব্ধ টুল এবং ডিবাগিংয়ের সেরা চর্চাগুলো বোঝা গুরুত্বপূর্ণ। কার্যকরী পরীক্ষা নিশ্চিত করে সার্ভার প্রত্যাশিতভাবে কাজ করছে এবং দ্রুত সমস্যা সনাক্ত ও সমাধান করতে সাহায্য করে। নিম্নলিখিত অংশটি আপনার MCP ইমপ্লিমেন্টেশন যাচাই করার জন্য সুপারিশকৃত পদ্ধতিগুলো বর্ণনা করে।

MCP আপনাকে পরীক্ষা এবং ডিবাগের জন্য টুল দেয়:

- **Inspector টুল**: একটি গ্রাফিকাল ইন্টারফেস যা আপনাকে আপনার সার্ভারে সংযোগ করতে এবং আপনার টুল, প্রম্পট এবং সম্পদ পরীক্ষা করতে দেয়।
- **curl**: আপনি কমান্ড লাইন টুল curl অথবা অন্য ক্লায়েন্ট ব্যবহার করেও সার্ভারে HTTP কমান্ড তৈরি ও চালাতে পারেন।

### MCP Inspector ব্যবহার

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) একটি ভিজ্যুয়াল টেস্টিং টুল যা আপনাকে সাহায্য করে:

1. **সার্ভারের ক্ষমতা আবিষ্কার করা**: উপলব্ধ সম্পদ, টুল এবং প্রম্পট স্বয়ংক্রিয়ভাবে সনাক্ত করুন
2. **টুল এক্সিকিউশন পরীক্ষা**: বিভিন্ন প্যারামিটার ব্যবহার করে রিয়েল-টাইমে প্রতিক্রিয়া দেখুন
3. **সার্ভার মেটাডেটা দেখা**: সার্ভারের তথ্য, স্কিমা এবং কনফিগারেশন পরীক্ষা করুন

```bash
# ট্যাক্সটাইপ স্ক্রিপ্ট, MCP ইনস্পেক্টর ইনস্টল ও চালানো
npx @modelcontextprotocol/inspector node build/index.js
```

এই কমান্ডগুলো চালালে, MCP Inspector আপনার ব্রাউজারে একটি লোকাল ওয়েব ইন্টারফেস চালু করবে। আপনি একটি ড্যাশবোর্ড দেখতে পাবেন যেখানে রেজিস্টারকৃত MCP সার্ভারগুলো, তাদের উপলব্ধ টুল, সম্পদ এবং প্রম্পট প্রদর্শিত হবে। ইন্টারফেসটি আপনাকে ইন্টারেক্টিভভাবে টুল এক্সিকিউশন পরীক্ষা, সার্ভার মেটাডেটা নিরীক্ষণ এবং রিয়েল-টাইম প্রতিক্রিয়া দেখতে দেয়, যা MCP সার্ভার ইমপ্লিমেন্টেশন যাচাই ও ডিবাগ আরও সহজ করে তোলে।

এখানে একটি স্ক্রিনশট কী দেখতে পারে:

![MCP Inspector server connection](../../../../translated_images/bn/connected.73d1e042c24075d3.webp)

## সাধারণ সেটআপ সমস্যা ও সমাধান

| সমস্যা | সম্ভাব্য সমাধান |
|-------|-------------------|
| সংযোগ প্রত্যাখ্যাত | সার্ভার চলছে কিনা এবং পোর্ট সঠিক কিনা পরীক্ষা করুন |
| টুল এক্সিকিউশন ত্রুটি | প্যারামিটার যাচাই এবং ত্রুটির হ্যান্ডলিং পর্যালোচনা করুন |
| অথেনটিকেশন ব্যর্থতা | API কী এবং অনুমতি যাচাই করুন |
| স্কিমা যাচাই ত্রুটি | প্যারামিটার সঠিক স্কিমার সাথে মিলছে কিনা নিশ্চিত করুন |
| সার্ভার শুরু হয় না | পোর্ট সংঘর্ষ বা অনুপস্থিত ডিপেনডেন্সি পরীক্ষা করুন |
| CORS ত্রুটি | ক্রস-অরিজিন অনুরোধের জন্য সঠিক CORS হেডার কনফিগার করুন |
| অথেনটিকেশন সমস্যা | টোকেন বৈধতা ও অনুমতি যাচাই করুন |

## স্থানীয় ডেভেলপমেন্ট

স্থানীয় ডেভেলপমেন্ট এবং পরীক্ষার জন্য, আপনি সরাসরি আপনার মেশিনে MCP সার্ভার চালাতে পারেন:

1. **সার্ভার প্রসেস শুরু করুন**: আপনার MCP সার্ভার অ্যাপ্লিকেশন চালান
2. **নেটওয়ার্কিং কনফিগার করুন**: নিশ্চিত করুন সার্ভারে প্রত্যাশিত পোর্টে প্রবেশযোগ্যতা আছে
3. **ক্লায়েন্ট সংযোগ করুন**: স্থানীয় সংযোগ URL যেমন `http://localhost:3000` ব্যবহার করুন

```bash
# উদাহরণ: টাইপস্ক্রিপ্ট MCP সার্ভার স্থানীয়ভাবে চলানো
npm run start
# সার্ভার চলছে http://localhost:3000 এ
```

## আপনার প্রথম MCP সার্ভার তৈরি করা

আমরা পূর্বের একটি পাঠে [মৌলিক ধারণাগুলো](../../01-CoreConcepts/README.md) আলোচনা করেছি, এখন সেই জ্ঞান কাজে লাগানোর সময়।

### সার্ভার কি করতে পারে

কোড লেখা শুরু করার আগে, আসুন মনে করি সার্ভার কি করতে পারে:

একটি MCP সার্ভার উদাহরণস্বরূপ পারে:

- স্থানীয় ফাইল এবং ডাটাবেস অ্যাক্সেস করা
- রিমোট API-তে সংযোগ করা
- হিসাব-নিকাশ সম্পাদন করা
- অন্যান্য টুল ও সেবার সাথে ইন্টিগ্রেট করা
- ব্যবহারকারীদের জন্য ইন্টারঅ্যাকশন ইন্টারফেস প্রদান করা

চমৎকার, এখন আমরা জানি সার্ভার কি করতে পারে, চল শুরু করি কোডিং।

## অনুশীলন: একটি সার্ভার তৈরি

সার্ভার তৈরি করতে, আপনাকে নিচের ধাপগুলো অনুসরণ করতে হবে:

- MCP SDK ইনস্টল করুন।
- একটি প্রজেক্ট তৈরি করুন এবং প্রজেক্ট স্ট্রাকচার সেটআপ করুন।
- সার্ভারের কোড লিখুন।
- সার্ভার পরীক্ষা করুন।

### -1- প্রজেক্ট তৈরি

#### TypeScript

```sh
# প্রজেক্ট ডিরেক্টরি তৈরি করুন এবং npm প্রজেক্ট আরম্ভ করুন
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# প্রকল্প ডিরেক্টরি তৈরি করুন
mkdir calculator-server
cd calculator-server
# ভিজ্যুয়াল স্টুডিও কোডে ফোল্ডারটি খুলুন - আপনি যদি অন্য কোনো আইডিই ব্যবহার করেন তবে এটি এড়িয়ে যান
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java-র জন্য, একটি Spring Boot প্রজেক্ট তৈরি করুন:

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

জিপ ফাইল উত্তোলন করুন:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ঐচ্ছিকভাবে অনাবশ্যক টেস্ট মুছুন
rm -rf src/test/java
```

আপনার *pom.xml* ফাইলে নিম্নলিখিত পূর্ণ কনফিগারেশন যোগ করুন:

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

এখন আপনার প্রজেক্ট তৈরি হয়ে গেছে, ডিপেনডেন্সি যোগ করা যাক:

#### TypeScript

```sh
# যদি ইতিমধ্যেই ইনস্টল করা না থাকে, তাহলে TypeScript গ্লোবালি ইনস্টল করুন
npm install typescript -g

# MCP SDK এবং স্কিমা ভ্যালিডেশনের জন্য Zod ইনস্টল করুন
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# একটি ভার্চুয়াল পরিবেশ তৈরি করুন এবং নির্ভরশীলতা ইনস্টল করুন
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

### -3- প্রজেক্ট ফাইল তৈরি

#### TypeScript

*package.json* ফাইলটি খুলে নিচের বিষয়বস্তুর দ্বারা প্রতিস্থাপন করুন যাতে সার্ভার তৈরি এবং চালানো যায়:

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

*tsconfig.json* তৈরি করুন নিম্নলিখিত বিষয়বস্তুর সঙ্গে:

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

*server.py* নামক ফাইল তৈরি করুন

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

Java Spring Boot প্রজেক্টের ক্ষেত্রে, প্রজেক্ট স্ট্রাকচার স্বয়ংক্রিয়ভাবে তৈরি হয়।

#### Rust

Rust-এ, `cargo init` চালানোর সময় ডিফল্টরূপে *src/main.rs* ফাইল তৈরি হয়। ফাইলটি খুলে ডিফল্ট কোড মুছে ফেলুন।

### -4- সার্ভারের কোড তৈরি

#### TypeScript

*index.ts* নামে একটি ফাইল তৈরি করুন এবং নিচের কোড যোগ করুন:

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

এখন আপনার কাছে একটি সার্ভার আছে, তবে এটি তেমন কিছু করে না, চল ঠিক করি।

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

Java-র জন্য, মূল সার্ভার কম্পোনেন্ট তৈরি করুন। প্রথমে মেইন অ্যাপ্লিকেশন ক্লাস সংশোধন করুন:

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

**প্রডাকশন-রেডি সার্ভিসের জন্য ঐচ্ছিক উপাদান:**

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

হেলথ কন্ট্রোলার তৈরি করুন *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

এক্সসেপশন হ্যান্ডলার তৈরি করুন *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

কাস্টম ব্যানার তৈরি করুন *src/main/resources/banner.txt*:

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

নিম্নলিখিত কোডটি *src/main.rs* ফাইলের শীর্ষে যোগ করুন। এটি MCP সার্ভারের জন্য প্রয়োজনীয় লাইব্রেরি এবং মডিউলগুলো ইমপোর্ট করে।

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

ক্যালকুলেটর সার্ভার হবে একটি সহজ সার্ভার যা দুইটি সংখ্যা যোগ করতে পারে। প্রথমে একটি struct তৈরি করি যা ক্যালকুলেটর রিকোয়েস্ট প্রতিনিধিত্ব করবে।

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

পরবর্তীতে, একটি struct তৈরি করুন যেটি ক্যালকুলেটর সার্ভার প্রতিনিধিত্ব করবে। এই struct টুল রাউটার ধারণ করবে, যা টুল রেজিস্টার করার জন্য ব্যবহৃত হয়।

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

এবার, `Calculator` struct ইমপ্লিমেন্ট করুন যাতে সার্ভারের একটি নতুন ইনস্ট্যান্স তৈরি হয় এবং সার্ভার হ্যান্ডলার ইমপ্লিমেন্ট করে সার্ভার তথ্য প্রদান করে।

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

অবশেষে, প্রধান ফাংশন ইমপ্লিমেন্ট করুন সার্ভার চালু করার জন্য। এই ফাংশন `Calculator` struct-এর একটি ইনস্ট্যান্স তৈরি করবে এবং এটিকে স্ট্যান্ডার্ড ইনপুট/আউটপুটে সার্ভ করবে।

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

এখন সার্ভার নিজ সম্পর্কে বেসিক তথ্য প্রদান করতে প্রস্তুত। পরবর্তীতে যোগ করার জন্য একটি টুল থাকবে যা যোগফল করবে।

### -5- একটি টুল এবং একটি রিসোর্স যোগ করা

নিম্নলিখিত কোড যোগ করে একটি টুল এবং একটি রিসোর্স যুক্ত করুন:

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

আপনার টুল `a` এবং `b` প্যারামিটার নেয় এবং নিচের ফর্মে একটি ফাংশন চালায় যা রেসপন্স তৈরি করে:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

আপনার রিসোর্স একটি স্ট্রিং "greeting" এর মাধ্যমে অ্যাক্সেস করা হয়, প্যারামিটার `name` নেয় এবং টুলের মতো একটি অনুরূপ রেসপন্স তৈরি করে:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# একটি যোগ করার টুল যোগ করুন
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# একটি গতিশীল শুভেচ্ছা সম্পদ যোগ করুন
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

উপরের কোডে আমরা:

- একটি `add` টুল সংজ্ঞায়িত করেছি যা `a` এবং `b` প্যারামিটার নেয়, উভয়ই ইন্টিজার।
- একটি `greeting` নামক রিসোর্স তৈরি করেছি যা `name` প্যারামিটার নেয়।

#### .NET

এই কোডটি আপনার Program.cs ফাইলে যোগ করুন:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

টুলগুলো ইতিমধ্যে পূর্বের ধাপে তৈরি করা হয়েছে।

#### Rust

`impl Calculator` ব্লকের ভিতরে নতুন একটি টুল যোগ করুন:

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

সার্ভার শুরু করার জন্য আমরা শেষ কোড যোগ করি:

#### TypeScript

```typescript
// stdin এ মেসেজ গ্রহণ শুরু করুন এবং stdout এ মেসেজ পাঠানো শুরু করুন
const transport = new StdioServerTransport();
await server.connect(transport);
```

সর্বশেষ পূর্ণ কোড এখানে:

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

// একটি যোগ(tool) যোগ করুন
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// একটি গতিশীল অভ্যর্থনা রিসোর্স যোগ করুন
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

// stdin এ মেসেজ গ্রহণ এবং stdout এ মেসেজ প্রেরণ শুরু করুন
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# একটি MCP সার্ভার তৈরি করুন
mcp = FastMCP("Demo")


# একটি যোগ করার টুল যোগ করুন
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# একটি গতিশীল শুভেচ্ছা রিসোর্স যোগ করুন
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# প্রধান কার্যনির্বাহী ব্লক - সার্ভার চালানোর জন্য এটি প্রয়োজনীয়
if __name__ == "__main__":
    mcp.run()
```

#### .NET

পরবর্তী বিষয়বস্তু সহ একটি Program.cs ফাইল তৈরি করুন:

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

আপনার সম্পূর্ণ মেইন অ্যাপ্লিকেশন ক্লাস এইরকম হওয়া উচিত:

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

Rust সার্ভারের চূড়ান্ত কোড এইরকম হওয়া উচিত:

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

নিম্নলিখিত কমান্ড দিয়ে সার্ভার শুরু করুন:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector ব্যবহার করার জন্য, `mcp dev server.py` চালান যা স্বয়ংক্রিয়ভাবে Inspector চালু করে এবং প্রয়োজনীয় প্রোক্সি সেশন টোকেন সরবরাহ করে। `mcp run server.py` ব্যবহার করলে আপনাকে ম্যানুয়ালি Inspector চালু করে সংযোগ কনফিগার করতে হবে।

#### .NET

নিশ্চিত করুন আপনি আপনার প্রজেক্ট ডিরেক্টরিতে আছেন:

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

সার্ভার ফরম্যাট এবং রান করতে নিম্নলিখিত কমান্ড চালান:

```sh
cargo fmt
cargo run
```

### -8- Inspector ব্যবহার করে রান করা

Inspector হল একটি চমৎকার টুল যা আপনার সার্ভার চালু করবে এবং আপনাকে এটি ইন্টারঅ্যাক্টিভভাবে পরীক্ষা করার সুযোগ দেবে। চল এটি চালু করি:

> [!NOTE]
> "command" ক্ষেত্রটি আপনার নির্দিষ্ট রuntime অনুযায়ী সার্ভার চালানোর কমান্ডটি ধারণ করার কারণে ভিন্ন দেখাতে পারে।

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

অথবা আপনার *package.json* এ এভাবে যোগ করুন: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` এবং তারপর চালান `npm run inspector`

#### Python

Python Node.js টুল ইনস্পেক্টরকে র‍্যাপ করে। এটি নিম্নরূপ কল করা সম্ভব:

```sh
mcp dev server.py
```

তবে, এটি টুলের সব মেথড ইমপ্লিমেন্ট করে না তাই সরাসরি Node.js টুল চালানোর পরামর্শ দেওয়া হয়:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

যদি আপনি এমন কোনো টুল বা IDE ব্যবহার করেন যা স্ক্রিপ্ট চালানোর জন্য কমান্ড এবং আর্গুমেন্ট কনফিগার করতে দেয়,
make sure to set `python` in the `Command` field and `server.py` as `Arguments`. This ensures the script runs correctly.

#### .NET

Make sure you're in your project directory:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Ensure you calculator server is running
The run the inspector:

```cmd
npx @modelcontextprotocol/inspector
```

In the inspector web interface:

1. Select "SSE" as the transport type
2. Set the URL to: `http://localhost:8080/sse`
3. Click "Connect"

![Connect](../../../../translated_images/bn/tool.163d33e3ee307e20.webp)

**You're now connected to the server**
**The Java server testing section is completed now**

The next section it's about interacting with the server.

You should see the following user interface:

![Connect](../../../../translated_images/bn/connect.141db0b2bd05f096.webp)

1. Connect to the server by selecting the Connect button
  Once you connect to the server, you should now see the following:

  ![Connected](../../../../translated_images/bn/connected.73d1e042c24075d3.webp)

1. Select "Tools" and "listTools", you should see "Add" show up, select "Add" and fill in the parameter values.

  You should see the following response, i.e a result from "add" tool:

  ![Result of running add](../../../../translated_images/bn/ran-tool.a5a6ee878c1369ec.webp)

Congrats, you've managed to create and run your first server!

#### Rust

To run the Rust server with the MCP Inspector CLI, use the following command:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Official SDKs

MCP provides official SDKs for multiple languages:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Maintained in collaboration with Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Maintained in collaboration with Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - The official TypeScript implementation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - The official Python implementation
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - The official Kotlin implementation
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Maintained in collaboration with Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - The official Rust implementation

## Key Takeaways

- Setting up an MCP development environment is straightforward with language-specific SDKs
- Building MCP servers involves creating and registering tools with clear schemas
- Testing and debugging are essential for reliable MCP implementations

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Assignment

Create a simple MCP server with a tool of your choice:

1. Implement the tool in your preferred language (.NET, Java, Python, TypeScript, or Rust).
2. Define input parameters and return values.
3. Run the inspector tool to ensure the server works as intended.
4. Test the implementation with various inputs.

## Solution

[Solution](./solution/README.md)

## Additional Resources

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## What's next

Next: [Getting Started with MCP Clients](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকারোক্তি**:
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। যদিও আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অমিমাংসিততা থাকতে পারে। মূল নথিটি তার স্বাভাবিক ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ প্রয়োজন। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->