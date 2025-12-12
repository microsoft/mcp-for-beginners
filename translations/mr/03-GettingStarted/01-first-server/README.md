<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T05:48:43+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "mr"
}
-->
# MCP सह प्रारंभ करणे

मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) सह तुमच्या पहिल्या पावलांवर स्वागत आहे! तुम्ही MCP मध्ये नवीन असाल किंवा तुमचे ज्ञान अधिक सखोल करायचे असेल, हा मार्गदर्शक तुम्हाला आवश्यक सेटअप आणि विकास प्रक्रियेतून मार्गदर्शन करेल. तुम्हाला कसे MCP AI मॉडेल्स आणि अनुप्रयोगांमध्ये अखंड समाकलन सक्षम करते हे समजेल, आणि MCP-शक्तीने चालणाऱ्या सोल्यूशन्स तयार करण्यासाठी आणि चाचणी करण्यासाठी तुमचे वातावरण लवकर तयार कसे करायचे हे शिकाल.

> TLDR; जर तुम्ही AI अॅप्स तयार करत असाल, तर तुम्हाला माहित आहे की तुम्ही तुमच्या LLM (मोठ्या भाषा मॉडेल) मध्ये साधने आणि इतर संसाधने जोडू शकता, ज्यामुळे LLM अधिक ज्ञानवान होते. मात्र जर तुम्ही ती साधने आणि संसाधने सर्व्हरवर ठेवली, तर अॅप आणि सर्व्हर क्षमता कोणत्याही क्लायंटद्वारे LLM सह किंवा शिवाय वापरली जाऊ शकतात.

## आढावा

हा धडा MCP वातावरण सेटअप करण्याबाबत व्यावहारिक मार्गदर्शन आणि तुमचे पहिले MCP अनुप्रयोग तयार करण्याबाबत आहे. तुम्ही आवश्यक साधने आणि फ्रेमवर्क सेटअप कसे करायचे, मूलभूत MCP सर्व्हर कसे तयार करायचे, होस्ट अनुप्रयोग कसे तयार करायचे, आणि तुमच्या अंमलबजावणीची चाचणी कशी करायची हे शिकाल.

मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) हा एक खुला प्रोटोकॉल आहे जो अनुप्रयोग LLMs ला संदर्भ कसा पुरवतात याचे मानकीकरण करतो. MCP ला AI अनुप्रयोगांसाठी USB-C पोर्ट म्हणून विचार करा - तो AI मॉडेल्सना विविध डेटा स्रोत आणि साधनांशी जोडण्याचा मानकीकृत मार्ग पुरवतो.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- C#, Java, Python, TypeScript, आणि Rust मध्ये MCP साठी विकास वातावरण सेटअप करणे
- सानुकूल वैशिष्ट्यांसह (संसाधने, प्रॉम्प्ट्स, आणि साधने) मूलभूत MCP सर्व्हर तयार करणे आणि तैनात करणे
- MCP सर्व्हरशी कनेक्ट होणारे होस्ट अनुप्रयोग तयार करणे
- MCP अंमलबजावणीची चाचणी आणि डीबग करणे

## तुमचे MCP वातावरण सेट करणे

MCP सह काम सुरू करण्यापूर्वी, तुमचे विकास वातावरण तयार करणे आणि मूलभूत कार्यप्रवाह समजून घेणे महत्त्वाचे आहे. हा विभाग सुरळीत सुरुवात सुनिश्चित करण्यासाठी प्रारंभिक सेटअप पायऱ्यांमध्ये तुम्हाला मार्गदर्शन करेल.

### पूर्वअट

MCP विकासात उतरायच्या आधी, खात्री करा की तुमच्याकडे आहे:

- **विकास वातावरण**: तुमच्या निवडलेल्या भाषेसाठी (C#, Java, Python, TypeScript, किंवा Rust)
- **IDE/संपादक**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, किंवा कोणताही आधुनिक कोड संपादक
- **पॅकेज मॅनेजर्स**: NuGet, Maven/Gradle, pip, npm/yarn, किंवा Cargo
- **API कीज**: तुमच्या होस्ट अनुप्रयोगांमध्ये वापरण्यासाठी कोणत्याही AI सेवांसाठी

## मूलभूत MCP सर्व्हर रचना

एक MCP सर्व्हर सामान्यतः समाविष्ट करतो:

- **सर्व्हर कॉन्फिगरेशन**: पोर्ट, प्रमाणीकरण, आणि इतर सेटिंग्ज सेट करणे
- **संसाधने**: LLMs साठी उपलब्ध केलेला डेटा आणि संदर्भ
- **साधने**: मॉडेल्स वापरू शकणारी कार्यक्षमता
- **प्रॉम्प्ट्स**: मजकूर तयार करण्यासाठी किंवा रचनेसाठी टेम्पलेट्स

TypeScript मध्ये एक सोपा उदाहरण येथे आहे:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्व्हर तयार करा
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// एक अतिरिक्त साधन जोडा
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन संसाधन जोडा
server.resource(
  "file",
  // 'list' पॅरामीटर संसाधन कसे उपलब्ध फाइल्सची यादी करतो हे नियंत्रित करते. त्याला undefined सेट केल्यास या संसाधनासाठी यादी करणे अक्षम होते.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// एक फाइल संसाधन जोडा जे फाइलची सामग्री वाचते
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

// stdin वर संदेश प्राप्त करणे आणि stdout वर संदेश पाठवणे सुरू करा
const transport = new StdioServerTransport();
await server.connect(transport);
```

वरील कोडमध्ये आपण:

- MCP TypeScript SDK मधून आवश्यक वर्ग आयात केले.
- नवीन MCP सर्व्हर उदाहरण तयार आणि कॉन्फिगर केले.
- कस्टम टूल (`calculator`) एक हँडलर फंक्शनसह नोंदवले.
- येणाऱ्या MCP विनंत्यांसाठी सर्व्हर सुरू केले.

## चाचणी आणि डीबगिंग

तुमचा MCP सर्व्हर चाचणी करण्यापूर्वी, उपलब्ध साधने आणि डीबगिंगसाठी सर्वोत्तम पद्धती समजून घेणे महत्त्वाचे आहे. प्रभावी चाचणी तुमचा सर्व्हर अपेक्षेप्रमाणे वागत आहे याची खात्री करते आणि समस्या लवकर ओळखून सोडवण्यास मदत करते. पुढील विभागात तुमच्या MCP अंमलबजावणीची पडताळणी करण्यासाठी शिफारस केलेल्या पद्धती दिल्या आहेत.

MCP तुमच्या सर्व्हरची चाचणी आणि डीबग करण्यासाठी साधने पुरवते:

- **इन्स्पेक्टर टूल**, हा ग्राफिकल इंटरफेस तुम्हाला तुमच्या सर्व्हरशी कनेक्ट होण्याची आणि तुमची साधने, प्रॉम्प्ट्स आणि संसाधने चाचणी करण्याची परवानगी देतो.
- **curl**, तुम्ही curl सारख्या कमांड लाइन टूलचा वापर करून किंवा HTTP कमांड तयार आणि चालवू शकणाऱ्या इतर क्लायंट्सचा वापर करून तुमच्या सर्व्हरशी कनेक्ट होऊ शकता.

### MCP इन्स्पेक्टर वापरणे

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) हा एक दृश्य चाचणी साधन आहे जे तुम्हाला मदत करते:

1. **सर्व्हर क्षमता शोधा**: उपलब्ध संसाधने, साधने, आणि प्रॉम्प्ट्स आपोआप शोधा
2. **साधन कार्यान्वयन चाचणी करा**: वेगवेगळे पॅरामीटर्स वापरून रिअल-टाइम प्रतिसाद पहा
3. **सर्व्हर मेटाडेटा पहा**: सर्व्हर माहिती, स्कीमा, आणि कॉन्फिगरेशन तपासा

```bash
# ex TypeScript, MCP Inspector स्थापित करणे आणि चालविणे
npx @modelcontextprotocol/inspector node build/index.js
```

वरील कमांड्स चालवल्यानंतर, MCP Inspector तुमच्या ब्राउझरमध्ये स्थानिक वेब इंटरफेस सुरू करेल. तुम्हाला तुमच्या नोंदणीकृत MCP सर्व्हर्स, त्यांची उपलब्ध साधने, संसाधने, आणि प्रॉम्प्ट्स दर्शवणारा डॅशबोर्ड दिसेल. हा इंटरफेस तुम्हाला साधन कार्यान्वयन इंटरॅक्टिव्हली चाचणी करण्याची, सर्व्हर मेटाडेटा तपासण्याची, आणि रिअल-टाइम प्रतिसाद पाहण्याची परवानगी देतो, ज्यामुळे तुमच्या MCP सर्व्हर अंमलबजावणीची पडताळणी आणि डीबग करणे सोपे होते.

हे कसे दिसू शकते याचे स्क्रीनशॉट येथे आहे:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.mr.png)

## सामान्य सेटअप समस्या आणि उपाय

| समस्या | शक्य तो उपाय |
|-------|-------------------|
| कनेक्शन नाकारले गेले | तपासा की सर्व्हर चालू आहे आणि पोर्ट बरोबर आहे का |
| साधन कार्यान्वयन त्रुटी | पॅरामीटर वैधता आणि त्रुटी हाताळणी तपासा |
| प्रमाणीकरण अयशस्वी | API कीज आणि परवानग्या तपासा |
| स्कीमा वैधता त्रुटी | पॅरामीटर्स परिभाषित स्कीमाशी जुळतात का ते तपासा |
| सर्व्हर सुरू होत नाही | पोर्ट संघर्ष किंवा गहाळ अवलंबित्वे तपासा |
| CORS त्रुटी | क्रॉस-ओरिजिन विनंत्यांसाठी योग्य CORS हेडर्स कॉन्फिगर करा |
| प्रमाणीकरण समस्या | टोकन वैधता आणि परवानग्या तपासा |

## स्थानिक विकास

स्थानिक विकास आणि चाचणीसाठी, तुम्ही MCP सर्व्हर थेट तुमच्या मशीनवर चालवू शकता:

1. **सर्व्हर प्रक्रिया सुरू करा**: तुमचा MCP सर्व्हर अनुप्रयोग चालवा
2. **नेटवर्किंग कॉन्फिगर करा**: सर्व्हर अपेक्षित पोर्टवर प्रवेशयोग्य आहे याची खात्री करा
3. **क्लायंट्स कनेक्ट करा**: `http://localhost:3000` सारख्या स्थानिक कनेक्शन URL वापरा

```bash
# उदाहरण: TypeScript MCP सर्व्हर स्थानिकपणे चालविणे
npm run start
# सर्व्हर http://localhost:3000 येथे चालू आहे
```

## तुमचा पहिला MCP सर्व्हर तयार करणे

आम्ही आधीच्या धड्यात [कोर संकल्पना](/01-CoreConcepts/README.md) पाहिल्या आहेत, आता त्या ज्ञानाचा वापर करण्याची वेळ आली आहे.

### सर्व्हर काय करू शकतो

कोड लिहिण्यापूर्वी, चला आठवण करून घेऊया की सर्व्हर काय करू शकतो:

एक MCP सर्व्हर उदाहरणार्थ करू शकतो:

- स्थानिक फाइल्स आणि डेटाबेसमध्ये प्रवेश
- दूरस्थ API शी कनेक्ट होणे
- गणना करणे
- इतर साधने आणि सेवा समाकलित करणे
- संवादासाठी वापरकर्ता इंटरफेस पुरवणे

छान, आता आपल्याला काय करता येते ते माहित आहे, तर कोडिंग सुरू करूया.

## सराव: सर्व्हर तयार करणे

सर्व्हर तयार करण्यासाठी, तुम्हाला खालील पायऱ्या पाळाव्या लागतील:

- MCP SDK इन्स्टॉल करा.
- प्रोजेक्ट तयार करा आणि प्रोजेक्ट रचना सेट करा.
- सर्व्हर कोड लिहा.
- सर्व्हरची चाचणी करा.

### -1- प्रोजेक्ट तयार करा

#### TypeScript

```sh
# प्रकल्प निर्देशिका तयार करा आणि npm प्रकल्प प्रारंभ करा
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# प्रकल्प डिरेक्टरी तयार करा
mkdir calculator-server
cd calculator-server
# Visual Studio Code मध्ये फोल्डर उघडा - जर तुम्ही वेगळा IDE वापरत असाल तर हे वगळा
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java साठी, Spring Boot प्रोजेक्ट तयार करा:

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

झिप फाइल अनझिप करा:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ऐच्छिक वापरात नसलेला चाचणी काढा
rm -rf src/test/java
```

तुमच्या *pom.xml* फाईलमध्ये खालील पूर्ण कॉन्फिगरेशन जोडा:

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

### -2- अवलंबित्वे जोडा

आता तुमचा प्रोजेक्ट तयार झाला आहे, पुढे अवलंबित्वे जोडा:

#### TypeScript

```sh
# जर आधीच स्थापित नसेल, तर TypeScript जागतिक पातळीवर स्थापित करा
npm install typescript -g

# स्कीमा प्रमाणीकरणासाठी MCP SDK आणि Zod स्थापित करा
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# एक आभासी वातावरण तयार करा आणि अवलंबित्वे स्थापित करा
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

### -3- प्रोजेक्ट फाइल्स तयार करा

#### TypeScript

*package.json* फाईल उघडा आणि खालील सामग्रीने बदला जेणेकरून तुम्ही सर्व्हर तयार आणि चालवू शकता:

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

*tsconfig.json* तयार करा खालील सामग्रीसह:

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

तुमच्या स्रोत कोडसाठी एक डिरेक्टरी तयार करा:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* नावाची फाईल तयार करा

```sh
touch server.py
```

#### .NET

आवश्यक NuGet पॅकेजेस इन्स्टॉल करा:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot प्रोजेक्टसाठी, प्रोजेक्ट रचना आपोआप तयार होते.

#### Rust

Rust साठी, `cargo init` चालवल्यावर *src/main.rs* फाईल डिफॉल्टने तयार होते. ती फाईल उघडा आणि डिफॉल्ट कोड हटवा.

### -4- सर्व्हर कोड तयार करा

#### TypeScript

*index.ts* नावाची फाईल तयार करा आणि खालील कोड जोडा:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// एक MCP सर्व्हर तयार करा
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

आता तुमच्याकडे एक सर्व्हर आहे, पण तो फार काही करत नाही, ते दुरुस्त करूया.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# एक MCP सर्व्हर तयार करा
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

Java साठी, मुख्य सर्व्हर घटक तयार करा. प्रथम, मुख्य अनुप्रयोग वर्ग बदला:

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

कॅल्क्युलेटर सेवा तयार करा *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**उत्पादन-तयार सेवेसाठी ऐच्छिक घटक:**

स्टार्टअप कॉन्फिगरेशन तयार करा *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

हेल्थ कंट्रोलर तयार करा *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

अपवाद हँडलर तयार करा *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // गेटर्स
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

कस्टम बॅनर तयार करा *src/main/resources/banner.txt*:

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

*src/main.rs* फाईलच्या वर खालील कोड जोडा. हे तुमच्या MCP सर्व्हरसाठी आवश्यक लायब्ररी आणि मॉड्यूल्स आयात करते.

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

कॅल्क्युलेटर सर्व्हर एक सोपा असेल जो दोन संख्या एकत्र जोडू शकतो. कॅल्क्युलेटर विनंतीचे प्रतिनिधित्व करणारा struct तयार करूया.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

नंतर, कॅल्क्युलेटर सर्व्हरचे प्रतिनिधित्व करणारा struct तयार करा. हा struct टूल राउटर ठेवेल, जो साधने नोंदवण्यासाठी वापरला जातो.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

आता, `Calculator` struct ची अंमलबजावणी करूया जे सर्व्हरची नवीन उदाहरण तयार करेल आणि सर्व्हर माहिती पुरवण्यासाठी सर्व्हर हँडलर अंमलात आणेल.

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

शेवटी, मुख्य फंक्शन अंमलात आणा जे सर्व्हर सुरू करेल. हे फंक्शन `Calculator` struct ची उदाहरण तयार करेल आणि ते स्टँडर्ड इनपुट/आउटपुटवर सर्व्ह करेल.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

सर्व्हर आता स्वतःबद्दल मूलभूत माहिती पुरवण्यासाठी तयार आहे. पुढे, आपण बेरीज करण्यासाठी एक साधन जोडू.

### -5- साधन आणि संसाधन जोडणे

खालील कोड जोडून साधन आणि संसाधन जोडा:

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

तुमचे साधन `a` आणि `b` पॅरामीटर्स घेतो आणि खालील स्वरूपात प्रतिसाद तयार करतो:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

तुमचा संसाधन "greeting" स्ट्रिंगद्वारे प्रवेश केला जातो, `name` पॅरामीटर घेतो आणि साधनासारखा प्रतिसाद तयार करतो:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# एक बेरीज साधन जोडा
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन स्रोत जोडा
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

वरील कोडमध्ये आपण:

- `add` नावाचे साधन परिभाषित केले जे `a` आणि `b` पॅरामीटर्स (दोन्ही पूर्णांक) घेतो.
- `greeting` नावाचा संसाधन तयार केला जो `name` पॅरामीटर घेतो.

#### .NET

हे तुमच्या Program.cs फाईलमध्ये जोडा:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

साधने आधीच्या टप्प्यात तयार केली गेली आहेत.

#### Rust

`impl Calculator` ब्लॉकमध्ये नवीन साधन जोडा:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- अंतिम कोड

सर्व्हर सुरू होण्यासाठी आवश्यक शेवटचा कोड जोडा:

#### TypeScript

```typescript
// stdin वरून संदेश प्राप्त करणे सुरू करा आणि stdout वर संदेश पाठवा
const transport = new StdioServerTransport();
await server.connect(transport);
```

पूर्ण कोड येथे आहे:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्व्हर तयार करा
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// एक बेरीज साधन जोडा
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन संसाधन जोडा
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

// stdin वरून संदेश प्राप्त करणे आणि stdout वर संदेश पाठवणे सुरू करा
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# एक MCP सर्व्हर तयार करा
mcp = FastMCP("Demo")


# एक बेरीज साधन जोडा
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन संसाधन जोडा
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# मुख्य अंमलबजावणी ब्लॉक - सर्व्हर चालवण्यासाठी हे आवश्यक आहे
if __name__ == "__main__":
    mcp.run()
```

#### .NET

खालील सामग्रीसह Program.cs फाईल तयार करा:

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

तुमचा पूर्ण मुख्य अनुप्रयोग वर्ग असा दिसायला हवा:

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

Rust सर्व्हरसाठी अंतिम कोड असा दिसायला हवा:

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

### -7- सर्व्हरची चाचणी करा

खालील कमांडने सर्व्हर सुरू करा:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector वापरण्यासाठी, `mcp dev server.py` वापरा जे आपोआप Inspector सुरू करते आणि आवश्यक प्रॉक्सी सत्र टोकन पुरवते. `mcp run server.py` वापरत असल्यास, तुम्हाला मॅन्युअली Inspector सुरू करावा लागेल आणि कनेक्शन कॉन्फिगर करावे लागेल.

#### .NET

तुम्ही तुमच्या प्रोजेक्ट डिरेक्टरीमध्ये आहात याची खात्री करा:

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

सर्व्हर फॉरमॅट आणि चालवण्यासाठी खालील कमांड्स चालवा:

```sh
cargo fmt
cargo run
```

### -8- इन्स्पेक्टर वापरून चालवा

इन्स्पेक्टर हा एक उत्कृष्ट साधन आहे जो तुमचा सर्व्हर सुरू करू शकतो आणि तुम्हाला त्याच्याशी संवाद साधण्याची परवानगी देतो जेणेकरून तुम्ही तपासू शकता की तो योग्यरित्या कार्य करतो का. चला ते सुरू करूया:

> [!NOTE]
> "command" फील्डमध्ये ते वेगळे दिसू शकते कारण त्यात तुमच्या विशिष्ट रनटाइमसाठी सर्व्हर चालवण्याचा आदेश असतो.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

किंवा ते तुमच्या *package.json* मध्ये अशा प्रकारे जोडा: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` आणि नंतर `npm run inspector` चालवा

#### Python

Python Node.js टूल inspector ला रॅप करते. तुम्ही खालीलप्रम
`Command` फील्डमध्ये `python` आणि `Arguments` मध्ये `server.py` सेट करणे सुनिश्चित करा. यामुळे स्क्रिप्ट योग्यरित्या चालेल.

#### .NET

आपण आपल्या प्रोजेक्ट डायरेक्टरीमध्ये आहात याची खात्री करा:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

आपला कॅल्क्युलेटर सर्व्हर चालू आहे याची खात्री करा
नंतर इन्स्पेक्टर चालवा:

```cmd
npx @modelcontextprotocol/inspector
```

इन्स्पेक्टर वेब इंटरफेसमध्ये:

1. ट्रान्सपोर्ट प्रकार म्हणून "SSE" निवडा
2. URL सेट करा: `http://localhost:8080/sse`
3. "Connect" क्लिक करा

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.mr.png)

**आपण आता सर्व्हरशी जोडलेले आहात**
**Java सर्व्हर चाचणी विभाग आता पूर्ण झाला आहे**

पुढील विभाग सर्व्हरशी संवाद साधण्याबद्दल आहे.

आपण खालील वापरकर्ता इंटरफेस पाहू शकता:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.mr.png)

1. Connect बटण निवडून सर्व्हरशी कनेक्ट व्हा
  एकदा आपण सर्व्हरशी कनेक्ट केल्यावर, आपल्याला खालील दिसेल:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.mr.png)

1. "Tools" आणि "listTools" निवडा, आपल्याला "Add" दिसेल, "Add" निवडा आणि पॅरामीटर मूल्ये भरा.

  आपल्याला खालील प्रतिसाद दिसेल, म्हणजे "add" टूलचा परिणाम:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.mr.png)

अभिनंदन, आपण आपला पहिला सर्व्हर तयार करून चालविला आहे!

#### Rust

MCP Inspector CLI सह Rust सर्व्हर चालवण्यासाठी खालील कमांड वापरा:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### अधिकृत SDKs

MCP अनेक भाषांसाठी अधिकृत SDKs प्रदान करते:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft सह सहयोगाने देखभाल केली जाते
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI सह सहयोगाने देखभाल केली जाते
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - अधिकृत TypeScript अंमलबजावणी
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - अधिकृत Python अंमलबजावणी
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - अधिकृत Kotlin अंमलबजावणी
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI सह सहयोगाने देखभाल केली जाते
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - अधिकृत Rust अंमलबजावणी

## मुख्य मुद्दे

- भाषा-विशिष्ट SDKs सह MCP विकास वातावरण सेट करणे सोपे आहे
- MCP सर्व्हर तयार करणे म्हणजे स्पष्ट स्कीमासह टूल्स तयार करणे आणि नोंदणी करणे
- विश्वसनीय MCP अंमलबजावणीसाठी चाचणी आणि डीबगिंग आवश्यक आहे

## नमुने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## असाइनमेंट

आपल्या पसंतीच्या टूलसह एक सोपा MCP सर्व्हर तयार करा:

1. आपल्या पसंतीच्या भाषेत टूल अंमलात आणा (.NET, Java, Python, TypeScript, किंवा Rust).
2. इनपुट पॅरामीटर्स आणि परतावा मूल्ये परिभाषित करा.
3. सर्व्हर योग्यरित्या कार्य करत असल्याची खात्री करण्यासाठी इन्स्पेक्टर टूल चालवा.
4. विविध इनपुटसह अंमलबजावणीची चाचणी करा.

## सोल्यूशन

[Solution](./solution/README.md)

## अतिरिक्त संसाधने

- [Azure वर Model Context Protocol वापरून एजंट तयार करा](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps सह Remote MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## पुढे काय

पुढे: [MCP Clients सह सुरुवात](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->