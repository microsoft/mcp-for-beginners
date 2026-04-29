# MCP सह प्रारंभ करणे

मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) सह तुमच्या पहिल्या पावलांसाठी आपले स्वागत आहे! तुम्ही MCP मध्ये नवीन असाल किंवा तुमचे ज्ञान अधिक सखोल करायचे असले तरी, हा मार्गदर्शक तुम्हाला आवश्यक सेटअप आणि विकास प्रक्रिया मार्गदर्शन करेल. तुम्ही कसे MCP एआय मॉडेल आणि अनुप्रयोगांमधील निर्बाध एकत्रीकरण सक्षम करते ते शोधाल आणि कसे त्वरेने तुमचे पर्यावरण तयार करून MCP-आधारित उपाय तयार आणि चाचणी करू शकता हे शिकाल.

> TLDR; जर तुम्ही AI अनुप्रयोग तयार करत असाल, तर तुम्हाला माहिती आहे की तुम्ही तुमच्या LLM (मोठे भाषा मॉडेल) मध्ये उपकरणे आणि इतर संसाधने जोडू शकता, ज्यामुळे LLM अधिक माहितीपूर्ण बनते. मात्र, जर तुम्ही ती उपकरणे आणि संसाधने एका सर्व्हरवर ठेवली तर अनुप्रयोग आणि सर्व्हर क्षमता कोणत्याही ग्राहकाद्वारे LLM सह/शिवाय वापरता येऊ शकतात.

## आढावा

हा धडा MCP पर्यावरण सेटअप आणि तुमचे पहिले MCP अनुप्रयोग तयार करण्याबाबत व्यावहारिक मार्गदर्शन प्रदान करतो. तुम्ही आवश्यक उपकरणे आणि फ्रेमवर्क सेटअप कसे करायचे, मूलभूत MCP सर्व्हर तयार कसे करायचे, होस्ट अनुप्रयोग तयार कसे करायचे आणि तुमच्या अंमलबजावण्या कसे तपासायचे हे शिकाल.

मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) हा एक मुक्त प्रोटोकॉल आहे जो अनुप्रयोगांना LLMs कडे संदर्भ प्रदान करण्याच्या पद्धतीचे मानकीकरण करतो. MCP हा AI अनुप्रयोगांसाठी USB-C पोर्टसारखा आहे - तो AI मॉडेलना वेगवेगळ्या डेटा स्रोत आणि उपकरणांशी जोडण्याचा मानकीकृत मार्ग पुरवतो.

## शिकण्याच्या उद्दिष्टे

या धड्यास शेवटी, तुम्ही सक्षम असाल:

- C#, Java, Python, TypeScript, आणि Rust मध्ये MCP विकास पर्यावरण सेटअप करणे
- सानुकूल वैशिष्ट्यांसह (संसाधने, प्रॉम्प्ट्स, आणि उपकरणे) मूलभूत MCP सर्व्हर तयार करणे आणि तैनात करणे
- MCP सर्व्हरशी जोडलेले होस्ट अनुप्रयोग तयार करणे
- MCP अंमलबजावण्या तपासणे आणि डीबग करणे

## तुमचे MCP पर्यावरण सेट करणे

MCP सह काम करण्यापूर्वी, तुमचे विकास पर्यावरण तयार करणे आणि मूलभूत कार्यप्रवाह समजून घेणे महत्त्वाचे आहे. हा विभाग सुरळीत सुरुवातीसाठी प्रारंभिक सेटअप पावले मार्गदर्शित करेल.

### पूर्वअट

MCP विकासात प्रवेश करण्यापूर्वी, खात्री करा की:

- **विकास पर्यावरण**: तुमच्या निवडलेल्या भाषेसाठी (C#, Java, Python, TypeScript, किंवा Rust)
- **IDE/एडिटर**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, किंवा कोणताही आधुनिक कोड संपादक
- **पॅकेज मॅनेजर्स**: NuGet, Maven/Gradle, pip, npm/yarn, किंवा Cargo
- **API कीज**: तुमच्या होस्ट अनुप्रयोगांमध्ये वापरायच्या कोणत्याही AI सेवांसाठी

## मूलभूत MCP सर्व्हर रचना

एक MCP सर्व्हर सामान्यतः यांचा समावेश करतो:

- **सर्व्हर कॉन्फिगरेशन**: पोर्ट, प्रमाणीकरण, आणि इतर सेटिंग्ज सेट करणे
- **संसाधने**: LLM कडे दिला जाणारा डेटा आणि संदर्भ
- **उपकरणे**: मॉडेल्स वापरू शकतील अशा कार्यक्षमता
- **प्रॉम्प्ट्स**: मजकूर तयार करण्यासाठी किंवा रचण्याच्या साचा

येथे TypeScript मध्ये एक साधे उदाहरण आहे:

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

// एक डायनामिक अभिवादन स्रोत जोडा
server.resource(
  "file",
  // 'list' पॅरामीटर स्रोताने उपलब्ध फाइल्स कशा यादी करायच्या हे नियंत्रित करतो. त्याला undefined सेट केल्यास या स्रोतासाठी यादी प्रक्रिया अक्षम होते.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// एक फाइल स्रोत जोडा जो फाइलची सामग्री वाचतो
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

// stdin वरून संदेश स्वीकारायला आणि stdout वर संदेश पाठवायला प्रारंभ करा
const transport = new StdioServerTransport();
await server.connect(transport);
```

वरिल कोडमध्ये आपण:

- MCP TypeScript SDK मधील आवश्यक वर्ग आयात केले.
- नवीन MCP सर्व्हर उदाहरण तयार आणि कॉन्फिगर केले.
- सानुकूल उपकरण (`calculator`) नोंदवले ज्याचा एक हॅन्डलर फंक्शन आहे.
- सर्व्हर सुरू केला जेणेकरून येणाऱ्या MCP विनंत्यांसाठी तो ऐकू शकेल.

## चाचणी आणि डीबगिंग

तुमचा MCP सर्व्हर तपासण्यापूर्वी, उपलब्ध उपकरणे आणि डीबगिंगसाठी सर्वोत्तम पद्धती समजून घेणे आवश्यक आहे. प्रभावी चाचणी सुनिश्चित करते की तुमचा सर्व्हर अपेक्षेनुसार चालतो आणि समस्या लवकर ओळखून निराकरण करण्यात मदत करते. खालील विभाग आपल्या MCP अंमलबजावणीसाठी शिफारस केलेल्या दृष्टिकोनांचे रेखाटन करतो.

MCP तुम्हाला तुमचे सर्व्हर तपासण्यासाठी आणि डीबग करण्यासाठी उपकरणे प्रदान करतो:

- **इन्स्पेक्टर उपकरण**, हा ग्राफिकल इंटरफेस तुमच्या सर्व्हरशी जोडण्यासाठी आणि तुमची उपकरणे, प्रॉम्प्ट आणि संसाधने तपासण्यासाठी वापरला जातो.
- **curl**, तुम्ही तसेच curl सारखे कमांड लाइन साधन किंवा इतर क्लायंट्स वापरून तुमच्या सर्व्हरशी कनेक्ट करू शकता जे HTTP कमांड तयार आणि चालवू शकतात.

### MCP इन्स्पेक्टर वापरून

[MCP इन्स्पेक्टर](https://github.com/modelcontextprotocol/inspector) एक व्हिज्युअल चाचणी साधन आहे जे तुम्हाला मदत करते:

1. **सर्व्हर क्षमता शोधा**: उपलब्ध संसाधने, उपकरणे, आणि प्रॉम्प्ट स्वयंचलितपणे शोधा
2. **उपकरण कार्यान्वयन तपासणी**: विविध पॅरामीटर्स वापरून पाहा आणि रिअल-टाइम प्रतिसाद पहा
3. **सर्व्हर मेटाडेटा पहा**: सर्व्हर माहिती, स्कीमा, आणि कॉन्फिगरेशन तपासा

```bash
# ex TypeScript, MCP Inspector स्थापित करणे आणि चालवणे
npx @modelcontextprotocol/inspector node build/index.js
```

वरील कमांड्स चालवल्यानंतर, MCP इन्स्पेक्टर तुमच्या ब्राउझरमध्ये स्थानिक वेब इंटरफेस सुरू करेल. तुम्हाला तुमच्या नोंदलेल्या MCP सर्व्हरचा डॅशबोर्ड दिसेल, त्यांच्या उपलब्ध उपकरणे, संसाधने आणि प्रॉम्प्टसह. इंटरफेस इंटरेक्टिव्ह टूल एक्झिक्युशन तपासण्यासाठी, सर्व्हर मेटाडेटा तपासण्यासाठी, आणि रिअल-टाइम प्रतिसाद पाहण्यासाठी मदत करते, ज्यामुळे तुमच्या MCP सर्व्हर अंमलबजावण्या ची पडताळणी आणि डीबगिंग सुलभ होते.

हे कसे दिसू शकते याचे एक स्क्रीनशॉट येथे आहे:

![MCP Inspector server connection](../../../../translated_images/mr/connected.73d1e042c24075d3.webp)

## सामान्य सेटअप समस्या आणि उपाय

| समस्या | शक्य उपाय |
|-------|-------------------|
| कनेक्शन नाकारले गेलं | सर्व्हर चालू आहे का आणि पोर्ट बरोबर आहे का तपासा |
| उपकरण कार्यान्वयन त्रुटी | पॅरामीटर पडताळणी आणि त्रुटी हाताळणी पुनरावलोकन करा |
| प्रमाणीकरण अयशस्वी | API कीज आणि परवानग्या तपासा |
| स्कीमा पडताळणी त्रुटी | पॅरामीटर्स परिभाषित स्कीमाशी जुळतात याची खात्री करा |
| सर्व्हर सुरू होत नाही | पोर्ट संघर्ष किंवा आवश्यक अवलंबनांची तपासणी करा |
| CORS त्रुटी | क्रॉस-ओरिजिन विनंत्यांसाठी योग्य CORS हेडर्स कॉन्फिगर करा |
| प्रमाणीकरण समस्या | टोकन वैधता आणि परवानग्या तपासा |

## स्थानिक विकास

स्थानिक विकास आणि चाचणीसाठी, तुम्ही तुमच्या मशीनवर थेट MCP सर्व्हर चालवू शकता:

1. **सर्व्हर प्रक्रिया सुरू करा**: तुमचा MCP सर्व्हर अनुप्रयोग चालवा
2. **नेटवर्किंग कॉन्फिगर करा**: सर्व्हर अपेक्षित पोर्टवर प्रवेशयोग्य आहे याची खात्री करा
3. **क्लायंट कनेक्ट करा**: `http://localhost:3000` सारखे स्थानिक कनेक्शन URLs वापरा

```bash
# उदाहरण: स्थानिकपणे TypeScript MCP सर्व्हर चालवत आहे
npm run start
# सर्व्हर http://localhost:3000 वर चालू आहे
```

## तुमचा पहिला MCP सर्व्हर तयार करणे

आम्ही मागील धड्यात [कोर संकल्पना](../../01-CoreConcepts/README.md) समजल्या आहेत, आता त्या ज्ञानाचा वापर करूया.

### सर्व्हर काय काय करू शकतो

कोड लिहिण्यापूर्वी, सर्व्हर काय करू शकतो याची आठवण करून घेऊया:

MCP सर्व्हर उदाहरणार्थ करू शकतो:

- स्थानिक फायली आणि डेटाबेस प्रवेश करणे
- रिमोट API शी कनेक्ट करणे
- गणनाकिय कार्ये करणे
- इतर उपकरणे आणि सेवा एकत्रित करणे
- संवादासाठी वापरकर्ता इंटरफेस उपलब्ध करणे

चांगले, आता आम्हाला काय करू शकतो हे माहीत आहे, तर कोडिंग सुरू करूया.

## सराव: सर्व्हर तयार करणे

सर्व्हर तयार करण्यासाठी, पुढील पावले पाळा:

- MCP SDK इन्स्टॉल करा.
- एक प्रोजेक्ट तयार करा आणि प्रोजेक्ट रचना सेट करा.
- सर्व्हर कोड लिहा.
- सर्व्हरची चाचणी करा.

### -1- प्रोजेक्ट तयार करा

#### TypeScript

```sh
# प्रोजेक्ट डिरेक्टरी तयार करा आणि npm प्रोजेक्ट सुरू करा
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# प्रोजेक्ट डिरेक्टरी तयार करा
mkdir calculator-server
cd calculator-server
# फोल्डर Visual Studio Code मध्ये उघडा - जर आपण वेगळे IDE वापरत असाल तर हे वगळा
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

झिप फाईल एक्स्ट्रॅक्ट करा:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ऐच्छिक वापरलेले नसलेले चाचणी काढून टाका
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

### -2- अवलंबन जोडा

आता तुम्ही प्रोजेक्ट तयार केले आहे, तर पुढे अवलंबने जोडा:

#### TypeScript

```sh
# जर आधीपासून स्थापित नसेल तर, TypeScript जागतिक पातळीवर स्थापित करा
npm install typescript -g

# MCP SDK आणि स्कीमा पडताळणीसाठी Zod स्थापित करा
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# आभासी पर्यावरण तयार करा आणि अवलंबन स्थापित करा
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

### -3- प्रोजेक्ट फायली तयार करा

#### TypeScript

*package.json* फाईल उघडा आणि खालील सामग्रीने बदला जेणेकरून सर्व्हर बांधणी आणि चालवता येईल:

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

*tsconfig.json* फाईल तयार करा खालील सामग्रीसह:

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

Java Spring Boot प्रोजेक्टसाठी, प्रोजेक्ट रचना स्वयंचलितपणे तयार केली जाते.

#### Rust

Rust साठी, `cargo init` चालविल्यावर *src/main.rs* फाईल डीफॉल्टने तयार होते. ती उघडा आणि डीफॉल्ट कोड हटवा.

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

आता तुमच्याकडे सर्व्हर आहे, पण ते फार काम करत नाही, त्याला सुधारूया.

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

Java साठी, कोर सर्व्हर घटक तयार करा. प्रथम, मुख्य अनुप्रयोग वर्ग सुधारित करा:

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

**प्रोडक्शन-तयार सेवेकरिता पर्यायी घटक:**

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

एखादा अपवाद हँडलर तयार करा *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

सानुकूल बॅनर तयार करा *src/main/resources/banner.txt*:

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

*src/main.rs* फाईलच्या वर खालील कोड जोडा. यामुळे एमसीपी सर्व्हरसाठी आवश्यक ग्रंथालय आणि मॉड्यूल आयात होतात.

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

कॅल्क्युलेटर सर्व्हर एक सोपा असा असेल जो दोन संख्या जमा करू शकेल. कॅल्क्युलेटर विनंतीचे प्रतिनिधित्व करण्यासाठी एक स्ट्रक्चर तयार करूया.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

यानंतर, कॅल्क्युलेटर सर्व्हरचे प्रतिनिधित्व करणारा एक स्ट्रक्चर तयार करा. या स्ट्रक्चरमध्ये टूल राउटर असेल, जे उपकरणे नोंदवण्यासाठी वापरले जाते.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

आता, नवीन सर्व्हर इन्स्टन्स तयार करण्यासाठी आणि सर्व्हर माहिती पुरवण्यासाठी `Calculator` स्ट्रक्चरला इम्प्लिमेंट करू शकतो.

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

शेवटी, मुख्य फंक्शन इम्प्लिमेंट करा जे सर्व्हर सुरु करेल. हे फंक्शन `Calculator` चे उदाहरण तयार करेल आणि स्टँडर्ड इनपुट/आउटपुट वर सर्व्ह करेल.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

सर्व्हर आता त्याबद्दल मूलभूत माहिती प्रदान करण्यासाठी तयार आहे. पुढे, आपण बेरीज करण्यासाठी एक उपकरण जोडू.

### -5- उपकरण आणि संसाधन जोडा

खालील कोड जोडून एक उपकरण आणि एक संसाधन जोडा:

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

तुमचे उपकरण `a` आणि `b` पॅरामीटर्स घेतो आणि खालील स्वरूपात उत्तर तयार करणारी फंक्शन चालवतो:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

तुमचे संसाधन "greeting" नावाच्या स्ट्रिंगद्वारे प्रवेशयोग्य आहे, ते `name` पॅरामीटर घेतो आणि उपकरणासारखेच प्रतिसाद तयार करते:

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


# एक डायनामिक अभिवादन स्रोत जोडा
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

वरिल कोडमध्ये आपण:

- `add` नावाचे एक उपकरण परिभाषित केले ज्यात `a` आणि `b` नामक पूर्णांक पॅरामीटर्स असतात.
- `greeting` नावाचे एक संसाधन तयार केले जे `name` पॅरामीटर घेतो.

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

उपकरणे आधीच्या टप्प्यात तयार केली गेली आहेत.

#### Rust

`impl Calculator` ब्लॉकच्या आत नवीन उपकरण जोडा:

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

सर्व्हर सुरु करण्यासाठी आवश्यक शेवटचा कोड जोडूया:

#### TypeScript

```typescript
// stdin वरून संदेश प्राप्त करणे सुरू करा आणि stdout वर संदेश पाठवा
const transport = new StdioServerTransport();
await server.connect(transport);
```

पूर्ण कोड:

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

// एक डायनॅमिक अभिवादन संसाधन जोडा
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

// stdin वर संदेश स्वीकारणे आणि stdout वर संदेश पाठवणे सुरू करा
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


# एक गतिशील अभिवादन स्त्रोत जोडा
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# मुख्य अंमलबजावणी ब्लॉक - सर्व्हर चालविण्यासाठी हे आवश्यक आहे
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

तुमचा पूर्ण मुख्य अनुप्रयोग वर्ग असा दिसेल:

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

Rust सर्व्हरसाठी अंतिम कोड असे दिसेल:

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

> MCP इन्स्पेक्टर वापरण्यासाठी `mcp dev server.py` वापरा, ज्यामुळे इन्स्पेक्टर स्वयंचलितपणे सुरू होतो आणि आवश्यक प्रॉक्सी सत्र टोकन प्रदान करते. जर `mcp run server.py` वापरले तर तुम्हाला इन्स्पेक्टर मॅन्युअली सुरू करावा लागेल आणि कनेक्शन कॉन्फिगर करावे लागेल.

#### .NET

तुम्ही तुमच्या प्रोजेक्ट डिरेक्टरीत असल्याची खात्री करा:

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

सर्व्हर फॉरमॅट आणि चालवण्यासाठी खालील कमांड चालवा:

```sh
cargo fmt
cargo run
```

### -8- इन्स्पेक्टर वापरून चालवा

इन्स्पेक्टर एक उत्तम साधन आहे जे तुमचा सर्व्हर सुरू करू शकतो आणि तुम्हाला त्याच्याशी संवाद साधण्याची परवानगी देतो त्यामुळे तुम्ही तपासू शकता की तो कसा कार्य करतो. चला तो सुरू करूया:

> [!NOTE]
> "command" फील्डमध्ये तो वेगळा दिसू शकतो कारण त्यात तुमच्या विशिष्ट रनटाइमसाठी सर्व्हर चालवण्याचा कमांड असतो.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

किंवा तुमच्या *package.json* मध्ये अशा प्रकारे जोडा: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` आणि नंतर `npm run inspector` चालवा

#### Python

Python मध्ये Node.js टूल इन्स्पेक्टरला रॅप केले आहे. अशा पद्धतीने ते कॉल करणे शक्य आहे:

```sh
mcp dev server.py
```

तथापि, ते टूलवरील सर्व मेथड्स अंमलात नाहीत, त्यामुळे तुम्हाला Node.js टूल थेट खालीलप्रमाणे चालवण्याची शिफारस केली जाते:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

जर तुम्ही एखाद्या साधन किंवा IDE वापरत असाल ज्यात स्क्रिप्ट चालवण्यासाठी कमांड आणि आर्ग्युमेंट्स कॉन्फिगर करता येतात,
कृपया `Command` क्षेत्रात `python` सेट करा आणि `Arguments` मध्ये `server.py` सेट करा. हे सुनिश्चित करते की स्क्रिप्ट योग्यरित्या चालेल.

#### .NET

आपण आपल्या प्रकल्प निर्देशिकेत आहात याची खात्री करा:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

आपला कॅल्क्युलेटर सर्व्हर चालू असल्याची खात्री करा
नंतर इन्स्पेक्टर चालवा:

```cmd
npx @modelcontextprotocol/inspector
```

इन्स्पेक्टर वेब इंटरफेसमध्ये:

1. ट्रान्सपोर्ट प्रकार म्हणून "SSE" निवडा
2. URL सेट करा: `http://localhost:8080/sse`
3. "Connect" वर क्लिक करा

![Connect](../../../../translated_images/mr/tool.163d33e3ee307e20.webp)

**आपण आता सर्व्हरशी जोडलेले आहात**
**जावा सर्व्हर तपासणी विभाग आता पूर्ण झाला आहे**

पुढील विभाग सर्व्हरसह संवाद साधण्याबद्दल आहे.

आपण पुढील वापरकर्ता इंटरफेस पाहू शकता:

![Connect](../../../../translated_images/mr/connect.141db0b2bd05f096.webp)

1. कनेक्ट बटण निवडून सर्व्हरशी कनेक्ट व्हा
  एकदा आपण सर्व्हरशी कनेक्ट केल्यावर, आपल्याला आता पुढील दिसावे:

  ![Connected](../../../../translated_images/mr/connected.73d1e042c24075d3.webp)

1. "Tools" आणि "listTools" निवडा, "Add" दिसेल, त्यानंतर "Add" निवडा आणि पॅरामीटर मूल्ये भरा.

  आपल्याला खालील प्रतिसाद दिसेल, म्हणजे "add" टूलचा परिणाम:

  ![Result of running add](../../../../translated_images/mr/ran-tool.a5a6ee878c1369ec.webp)

अभिनंदन, आपण आपला पहिला सर्व्हर तयार करून यशस्वीरित्या चालविला आहे!

#### Rust

MCP Inspector CLI सह Rust सर्व्हर चालवण्यासाठी खालील आदेश वापरा:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### अधिकृत SDKs

MCP विविध भाषांसाठी अधिकृत SDKs प्रदान करते:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft सह सांभाळलेले
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI सह सांभाळलेले
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - अधिकृत TypeScript अंमलबजावणी
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - अधिकृत Python अंमलबजावणी
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - अधिकृत Kotlin अंमलबजावणी
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI सह सांभाळलेले
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - अधिकृत Rust अंमलबजावणी

## मुख्य मुद्दे

- MCP विकास वातावरण लॅंग्वेज-सहानुकूल SDKs सह सोपे आहे
- MCP सर्व्हर तयार करणे म्हणजे स्पष्ट schemas सह टूल तयार करणे आणि नोंदणी करणे
- विश्वसनीय MCP अंमलबजावणीसाठी चाचणी आणि डिबगिंग आवश्यक आहे

## नमुने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## कार्य

आपल्या पसंतीच्या टूलसह सोपा MCP सर्व्हर तयार करा:

1. आपल्या पसंतीच्या भाषेत टूल अंमलात आणा (.NET, Java, Python, TypeScript, किंवा Rust).
2. इनपुट पॅरामिटर्स आणि रिटर्न मूल्ये परिभाषित करा.
3. सर्व्हर योग्यरित्या कार्यान्वित आहे यासाठी इन्स्पेक्टर टूल चालवा.
4. विविध इनपुटसह अंमलबजावणीची चाचणी करा.

## समाधान

[Solution](./solution/README.md)

## अतिरिक्त साधने

- [Azure वर Model Context Protocol वापरून एजंट तयार करा](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps सह Remote MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## पुढे काय

पुढे: [MCP Clients सह प्रारंभ करणे](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवेचा वापर करून अनुवादित करण्यात आला आहे [Co-op Translator](https://github.com/Azure/co-op-translator). आम्ही अचूकतेसाठी प्रयत्न करतो, तरीही कृत्रिम अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात याची कृपया जाणीव ठेवा. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीकरिता, व्यावसायिक मानवी भाषांतर शिफारसीय आहे. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुतीस किंवा चुकीच्या अर्थ लावण्यांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->