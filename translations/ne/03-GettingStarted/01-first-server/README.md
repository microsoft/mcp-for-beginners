<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T05:54:17+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "ne"
}
-->
# MCP सँग सुरु गर्दै

Model Context Protocol (MCP) सँग तपाईंको पहिलो कदमहरूमा स्वागत छ! तपाईं MCP मा नयाँ हुनुहुन्छ वा आफ्नो बुझाइलाई गहिरो बनाउन खोज्दै हुनुहुन्छ भने, यो मार्गदर्शकले तपाईंलाई आवश्यक सेटअप र विकास प्रक्रियामा लैजानेछ। तपाईंले पत्ता लगाउनुहुनेछ कि कसरी MCP ले AI मोडेलहरू र अनुप्रयोगहरू बीच सहज एकीकरण सक्षम पार्छ, र कसरी छिटो आफ्नो वातावरण तयार पारेर MCP-संचालित समाधानहरू निर्माण र परीक्षण गर्ने।

> TLDR; यदि तपाईं AI अनुप्रयोगहरू बनाउनुहुन्छ भने, तपाईंलाई थाहा छ कि तपाईंले आफ्नो LLM (ठूलो भाषा मोडेल) मा उपकरणहरू र अन्य स्रोतहरू थप्न सक्नुहुन्छ, जसले LLM लाई अझ ज्ञानवान बनाउँछ। तर यदि तपाईं ती उपकरणहरू र स्रोतहरू सर्भरमा राख्नुहुन्छ भने, अनुप्रयोग र सर्भर क्षमताहरू कुनै पनि क्लाइन्टले LLM सहित वा बिना प्रयोग गर्न सक्छ।

## अवलोकन

यस पाठले MCP वातावरणहरू सेटअप गर्ने र तपाईंका पहिलो MCP अनुप्रयोगहरू निर्माण गर्ने व्यावहारिक मार्गदर्शन प्रदान गर्दछ। तपाईंले आवश्यक उपकरणहरू र फ्रेमवर्कहरू कसरी सेटअप गर्ने, आधारभूत MCP सर्भरहरू कसरी बनाउने, होस्ट अनुप्रयोगहरू कसरी सिर्जना गर्ने, र तपाईंका कार्यान्वयनहरू कसरी परीक्षण गर्ने सिक्नुहुनेछ।

Model Context Protocol (MCP) एक खुला प्रोटोकल हो जसले अनुप्रयोगहरूले LLMs लाई सन्दर्भ कसरी प्रदान गर्ने भन्ने कुरा मानकीकृत गर्दछ। MCP लाई AI अनुप्रयोगहरूको लागि USB-C पोर्ट जस्तै सोच्नुहोस् - यसले AI मोडेलहरूलाई विभिन्न डेटा स्रोतहरू र उपकरणहरूसँग जडान गर्ने मानकीकृत तरिका प्रदान गर्दछ।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- C#, Java, Python, TypeScript, र Rust मा MCP को लागि विकास वातावरण सेटअप गर्न
- कस्टम सुविधाहरू (स्रोतहरू, प्रॉम्प्टहरू, र उपकरणहरू) सहित आधारभूत MCP सर्भरहरू निर्माण र तैनाथ गर्न
- MCP सर्भरहरूसँग जडान गर्ने होस्ट अनुप्रयोगहरू सिर्जना गर्न
- MCP कार्यान्वयनहरू परीक्षण र डिबग गर्न

## तपाईंको MCP वातावरण सेटअप गर्दै

MCP सँग काम गर्न सुरु गर्नु अघि, तपाईंको विकास वातावरण तयार पार्नु र आधारभूत कार्यप्रवाह बुझ्नु महत्त्वपूर्ण छ। यस खण्डले तपाईंलाई सुरुवाती सेटअप चरणहरूमा मार्गदर्शन गर्नेछ ताकि MCP सँग सहज सुरुवात सुनिश्चित होस्।

### पूर्वआवश्यकताहरू

MCP विकासमा डुब्नु अघि, सुनिश्चित गर्नुहोस् कि तपाईंले:

- **विकास वातावरण**: तपाईंले रोजेको भाषा (C#, Java, Python, TypeScript, वा Rust) को लागि
- **IDE/संपादक**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, वा कुनै आधुनिक कोड संपादक
- **प्याकेज प्रबन्धकहरू**: NuGet, Maven/Gradle, pip, npm/yarn, वा Cargo
- **API कुञ्जीहरू**: तपाईंले होस्ट अनुप्रयोगहरूमा प्रयोग गर्ने कुनै पनि AI सेवाहरूका लागि

## आधारभूत MCP सर्भर संरचना

एक MCP सर्भर सामान्यतया समावेश गर्दछ:

- **सर्भर कन्फिगरेसन**: पोर्ट, प्रमाणीकरण, र अन्य सेटिङहरू सेटअप गर्ने
- **स्रोतहरू**: LLMs लाई उपलब्ध गराइने डेटा र सन्दर्भ
- **उपकरणहरू**: मोडेलहरूले कल गर्न सक्ने कार्यक्षमता
- **प्रॉम्प्टहरू**: पाठ सिर्जना वा संरचना गर्नका लागि टेम्प्लेटहरू

यहाँ TypeScript मा एक सरल उदाहरण छ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्भर सिर्जना गर्नुहोस्
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// एक थप उपकरण थप्नुहोस्
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन स्रोत थप्नुहोस्
server.resource(
  "file",
  // 'list' प्यारामिटरले स्रोतले उपलब्ध फाइलहरू कसरी सूचीबद्ध गर्छ नियन्त्रण गर्छ। यसलाई undefined मा सेट गर्दा यस स्रोतको लागि सूचीबद्धता अक्षम हुन्छ।
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// फाइल सामग्री पढ्ने फाइल स्रोत थप्नुहोस्
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

// stdin मा सन्देशहरू प्राप्त गर्न र stdout मा सन्देशहरू पठाउन सुरु गर्नुहोस्
const transport = new StdioServerTransport();
await server.connect(transport);
```

अघिल्लो कोडमा हामीले:

- MCP TypeScript SDK बाट आवश्यक कक्षाहरू आयात गरेका छौं।
- नयाँ MCP सर्भर उदाहरण सिर्जना र कन्फिगर गरेका छौं।
- कस्टम उपकरण (`calculator`) लाई ह्यान्डलर फंक्शनसहित दर्ता गरेका छौं।
- MCP अनुरोधहरू सुन्न सर्भर सुरु गरेका छौं।

## परीक्षण र डिबगिङ

तपाईंको MCP सर्भर परीक्षण गर्न सुरु गर्नु अघि, उपलब्ध उपकरणहरू र डिबगिङका लागि उत्तम अभ्यासहरू बुझ्नु महत्त्वपूर्ण छ। प्रभावकारी परीक्षणले तपाईंको सर्भर अपेक्षित रूपमा व्यवहार गर्छ भन्ने सुनिश्चित गर्दछ र छिटो समस्याहरू पहिचान र समाधान गर्न मद्दत गर्दछ। तलको खण्डले तपाईंको MCP कार्यान्वयनलाई मान्य पार्न सिफारिस गरिएका दृष्टिकोणहरू वर्णन गर्दछ।

MCP ले तपाईंलाई सर्भरहरू परीक्षण र डिबग गर्न मद्दत गर्ने उपकरणहरू प्रदान गर्दछ:

- **Inspector उपकरण**, यो ग्राफिकल इन्टरफेसले तपाईंलाई सर्भरसँग जडान गर्न र तपाईंका उपकरणहरू, प्रॉम्प्टहरू र स्रोतहरू परीक्षण गर्न अनुमति दिन्छ।
- **curl**, तपाईं कमाण्ड लाइन उपकरण जस्तै curl वा अन्य क्लाइन्टहरू प्रयोग गरेर पनि सर्भरसँग जडान गर्न सक्नुहुन्छ जसले HTTP आदेशहरू सिर्जना र चलाउन सक्छ।

### MCP Inspector प्रयोग गर्दै

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) एक दृश्य परीक्षण उपकरण हो जसले तपाईंलाई मद्दत गर्दछ:

1. **सर्भर क्षमताहरू पत्ता लगाउने**: उपलब्ध स्रोतहरू, उपकरणहरू, र प्रॉम्प्टहरू स्वचालित रूपमा पत्ता लगाउने
2. **उपकरण कार्यान्वयन परीक्षण गर्ने**: विभिन्न प्यारामिटरहरू प्रयास गर्ने र वास्तविक समयमा प्रतिक्रिया हेर्ने
3. **सर्भर मेटाडाटा हेर्ने**: सर्भर जानकारी, स्किमाहरू, र कन्फिगरेसनहरू जाँच गर्ने

```bash
# उदाहरण TypeScript, MCP निरीक्षक स्थापना र चलाउने
npx @modelcontextprotocol/inspector node build/index.js
```

तपाईं माथिका आदेशहरू चलाउँदा, MCP Inspector ले तपाईंको ब्राउजरमा स्थानीय वेब इन्टरफेस सुरु गर्नेछ। तपाईंले दर्ता गरिएका MCP सर्भरहरू, तिनीहरूको उपलब्ध उपकरणहरू, स्रोतहरू, र प्रॉम्प्टहरू देखाउने ड्यासबोर्ड देख्न सक्नुहुन्छ। इन्टरफेसले तपाईंलाई अन्तरक्रियात्मक रूपमा उपकरण कार्यान्वयन परीक्षण गर्न, सर्भर मेटाडाटा निरीक्षण गर्न, र वास्तविक समय प्रतिक्रियाहरू हेर्न अनुमति दिन्छ, जसले तपाईंका MCP सर्भर कार्यान्वयनहरू मान्य र डिबग गर्न सजिलो बनाउँछ।

यहाँ यसको स्क्रिनशट छ:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ne.png)

## सामान्य सेटअप समस्याहरू र समाधानहरू

| समस्या | सम्भावित समाधान |
|-------|-------------------|
| जडान अस्वीकृत | सर्भर चलिरहेको छ कि छैन र पोर्ट सही छ कि छैन जाँच गर्नुहोस् |
| उपकरण कार्यान्वयन त्रुटिहरू | प्यारामिटर मान्यकरण र त्रुटि ह्यान्डलिङ समीक्षा गर्नुहोस् |
| प्रमाणीकरण असफलता | API कुञ्जीहरू र अनुमति जाँच गर्नुहोस् |
| स्किमा मान्यकरण त्रुटिहरू | प्यारामिटरहरू परिभाषित स्किमासँग मेल खान्छन् कि छैनन् सुनिश्चित गर्नुहोस् |
| सर्भर सुरु नहुनु | पोर्ट द्वन्द्व वा हराइरहेका निर्भरता जाँच गर्नुहोस् |
| CORS त्रुटिहरू | क्रस-ओरिजिन अनुरोधहरूको लागि उचित CORS हेडरहरू कन्फिगर गर्नुहोस् |
| प्रमाणीकरण समस्या | टोकन वैधता र अनुमति जाँच गर्नुहोस् |

## स्थानीय विकास

स्थानीय विकास र परीक्षणका लागि, तपाईंले MCP सर्भरहरू सिधै आफ्नो मेसिनमा चलाउन सक्नुहुन्छ:

1. **सर्भर प्रक्रिया सुरु गर्नुहोस्**: तपाईंको MCP सर्भर अनुप्रयोग चलाउनुहोस्
2. **नेटवर्किङ कन्फिगर गर्नुहोस्**: सर्भर अपेक्षित पोर्टमा पहुँचयोग्य छ कि छैन सुनिश्चित गर्नुहोस्
3. **क्लाइन्टहरू जडान गर्नुहोस्**: `http://localhost:3000` जस्ता स्थानीय जडान URL हरू प्रयोग गर्नुहोस्

```bash
# उदाहरण: स्थानीय रूपमा TypeScript MCP सर्भर चलाउँदै
npm run start
# सर्भर http://localhost:3000 मा चलिरहेको छ
```

## तपाईंको पहिलो MCP सर्भर निर्माण गर्दै

हामीले अघिल्लो पाठमा [मूल अवधारणाहरू](/01-CoreConcepts/README.md) कभर गरिसकेका छौं, अब त्यो ज्ञानलाई कार्यान्वयन गर्ने समय आएको छ।

### सर्भरले के गर्न सक्छ

कोड लेख्न सुरु गर्नु अघि, हामीलाई सम्झनुहोस् सर्भरले के गर्न सक्छ:

एक MCP सर्भरले उदाहरणका लागि:

- स्थानीय फाइलहरू र डेटाबेसहरू पहुँच गर्न सक्छ
- रिमोट API हरूसँग जडान गर्न सक्छ
- गणना गर्न सक्छ
- अन्य उपकरणहरू र सेवाहरू सँग एकीकरण गर्न सक्छ
- अन्तरक्रियाको लागि प्रयोगकर्ता इन्टरफेस प्रदान गर्न सक्छ

शानदार, अब हामीलाई थाहा छ के गर्न सक्छ, कोड लेख्न सुरु गरौं।

## अभ्यास: सर्भर सिर्जना गर्दै

सर्भर सिर्जना गर्न, तपाईंले यी चरणहरू पालना गर्नुपर्छ:

- MCP SDK स्थापना गर्नुहोस्।
- परियोजना सिर्जना गर्नुहोस् र परियोजना संरचना सेटअप गर्नुहोस्।
- सर्भर कोड लेख्नुहोस्।
- सर्भर परीक्षण गर्नुहोस्।

### -1- परियोजना सिर्जना गर्नुहोस्

#### TypeScript

```sh
# परियोजना निर्देशिका सिर्जना गर्नुहोस् र npm परियोजना आरम्भ गर्नुहोस्
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# परियोजना निर्देशिका सिर्जना गर्नुहोस्
mkdir calculator-server
cd calculator-server
# फोल्डरलाई Visual Studio Code मा खोल्नुहोस् - यदि तपाईंले फरक IDE प्रयोग गर्दै हुनुहुन्छ भने यो छोड्नुहोस्
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java का लागि, Spring Boot परियोजना सिर्जना गर्नुहोस्:

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

जिप फाइल निकाल्नुहोस्:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# वैकल्पिक रूपमा प्रयोग नगरिएको परीक्षण हटाउनुहोस्
rm -rf src/test/java
```

तपाईंको *pom.xml* फाइलमा निम्न पूर्ण कन्फिगरेसन थप्नुहोस्:

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

### -2- निर्भरता थप्नुहोस्

अब तपाईंले परियोजना सिर्जना गर्नुभयो, अब निर्भरता थपौं:

#### TypeScript

```sh
# यदि पहिले नै स्थापना गरिएको छैन भने, TypeScript लाई विश्वव्यापी रूपमा स्थापना गर्नुहोस्
npm install typescript -g

# MCP SDK र Zod लाई स्कीमा प्रमाणीकरणको लागि स्थापना गर्नुहोस्
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# भर्चुअल वातावरण सिर्जना गर्नुहोस् र निर्भरताहरू स्थापना गर्नुहोस्
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

### -3- परियोजना फाइलहरू सिर्जना गर्नुहोस्

#### TypeScript

*package.json* फाइल खोल्नुहोस् र निम्न सामग्रीले प्रतिस्थापन गर्नुहोस् ताकि तपाईं सर्भर निर्माण र चलाउन सक्नुहुनेछ:

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

*tsconfig.json* सिर्जना गर्नुहोस् निम्न सामग्रीसहित:

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

तपाईंको स्रोत कोडको लागि डिरेक्टरी सिर्जना गर्नुहोस्:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* फाइल सिर्जना गर्नुहोस्

```sh
touch server.py
```

#### .NET

आवश्यक NuGet प्याकेजहरू स्थापना गर्नुहोस्:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot परियोजनाहरूको लागि, परियोजना संरचना स्वचालित रूपमा सिर्जना हुन्छ।

#### Rust

Rust का लागि, `cargo init` चलाउँदा *src/main.rs* फाइल डिफल्ट रूपमा सिर्जना हुन्छ। फाइल खोल्नुहोस् र डिफल्ट कोड मेटाउनुहोस्।

### -4- सर्भर कोड सिर्जना गर्नुहोस्

#### TypeScript

*index.ts* फाइल सिर्जना गर्नुहोस् र निम्न कोड थप्नुहोस्:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// एक MCP सर्भर सिर्जना गर्नुहोस्
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

अब तपाईंको सर्भर छ, तर यो धेरै गर्दैन, त्यसलाई सुधारौं।

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# एक MCP सर्भर सिर्जना गर्नुहोस्
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

Java का लागि, मुख्य सर्भर कम्पोनेन्टहरू सिर्जना गर्नुहोस्। पहिले, मुख्य अनुप्रयोग कक्षा संशोधन गर्नुहोस्:

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

क्याल्कुलेटर सेवा सिर्जना गर्नुहोस् *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**उत्पादन-तयार सेवाका लागि वैकल्पिक कम्पोनेन्टहरू:**

स्टार्टअप कन्फिगरेसन सिर्जना गर्नुहोस् *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

हेल्थ कन्ट्रोलर सिर्जना गर्नुहोस् *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

अपवाद ह्यान्डलर सिर्जना गर्नुहोस् *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // गेटरहरू
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

कस्टम ब्यानर सिर्जना गर्नुहोस् *src/main/resources/banner.txt*:

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

*src/main.rs* फाइलको शीर्षमा निम्न कोड थप्नुहोस्। यसले तपाईंको MCP सर्भरका लागि आवश्यक पुस्तकालयहरू र मोड्युलहरू आयात गर्दछ।

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

क्याल्कुलेटर सर्भर एक सरल सर्भर हुनेछ जसले दुई संख्याहरू जोड्न सक्छ। क्याल्कुलेटर अनुरोध प्रतिनिधित्व गर्न एक struct सिर्जना गरौं।

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

अर्को, क्याल्कुलेटर सर्भर प्रतिनिधित्व गर्न struct सिर्जना गर्नुहोस्। यस struct मा उपकरण राउटर हुनेछ, जुन उपकरणहरू दर्ता गर्न प्रयोग हुन्छ।

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

अब, हामी `Calculator` struct लाई नयाँ सर्भर उदाहरण सिर्जना गर्न र सर्भर ह्यान्डलर कार्यान्वयन गर्न सक्छौं जसले सर्भर जानकारी प्रदान गर्दछ।

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

अन्तमा, मुख्य फंक्शन कार्यान्वयन गर्न आवश्यक छ जसले सर्भर सुरु गर्दछ। यसले `Calculator` struct को उदाहरण सिर्जना गर्नेछ र मानक इनपुट/आउटपुट मार्फत सेवा दिनेछ।

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

सर्भर अब आफैंको आधारभूत जानकारी प्रदान गर्न सेटअप गरिएको छ। अब, हामी थप गर्ने उपकरण थप्नेछौं।

### -5- उपकरण र स्रोत थप्दै

तलको कोड थपेर उपकरण र स्रोत थप्नुहोस्:

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

तपाईंको उपकरणले प्यारामिटरहरू `a` र `b` लिन्छ र यस्तो प्रतिक्रिया उत्पादन गर्ने फंक्शन चलाउँछ:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

तपाईंको स्रोत "greeting" स्ट्रिङमार्फत पहुँचयोग्य छ र प्यारामिटर `name` लिन्छ र उपकरण जस्तै प्रतिक्रिया उत्पादन गर्छ:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# एउटा थप उपकरण थप्नुहोस्
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन स्रोत थप्नुहोस्
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

अघिल्लो कोडमा हामीले:

- `add` नामक उपकरण परिभाषित गरेका छौं जसले प्यारामिटरहरू `a` र `b` लिन्छ, दुवै पूर्णांक।
- `greeting` नामक स्रोत सिर्जना गरेका छौं जसले प्यारामिटर `name` लिन्छ।

#### .NET

यसलाई तपाईंको Program.cs फाइलमा थप्नुहोस्:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

उपकरणहरू पहिले नै अघिल्लो चरणमा सिर्जना गरिएका छन्।

#### Rust

`impl Calculator` ब्लक भित्र नयाँ उपकरण थप्नुहोस्:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- अन्तिम कोड

सर्भर सुरु गर्न आवश्यक अन्तिम कोड थपौं:

#### TypeScript

```typescript
// stdin मा सन्देशहरू प्राप्त गर्न सुरु गर्नुहोस् र stdout मा सन्देशहरू पठाउनुहोस्
const transport = new StdioServerTransport();
await server.connect(transport);
```

पूरा कोड यहाँ छ:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्भर सिर्जना गर्नुहोस्
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// एक थप उपकरण थप्नुहोस्
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन स्रोत थप्नुहोस्
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

// stdin मा सन्देशहरू प्राप्त गर्न र stdout मा सन्देशहरू पठाउन सुरु गर्नुहोस्
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# एक MCP सर्भर सिर्जना गर्नुहोस्
mcp = FastMCP("Demo")


# एक थप उपकरण थप्नुहोस्
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन स्रोत थप्नुहोस्
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# मुख्य कार्यान्वयन ब्लक - सर्भर चलाउन यो आवश्यक छ
if __name__ == "__main__":
    mcp.run()
```

#### .NET

तलको सामग्रीसहित Program.cs फाइल सिर्जना गर्नुहोस्:

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

तपाईंको पूर्ण मुख्य अनुप्रयोग कक्षा यसरी देखिनु पर्छ:

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

Rust सर्भरको अन्तिम कोड यसरी देखिनु पर्छ:

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

### -7- सर्भर परीक्षण गर्नुहोस्

तलको आदेश प्रयोग गरेर सर्भर सुरु गर्नुहोस्:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector प्रयोग गर्न, `mcp dev server.py` प्रयोग गर्नुहोस् जसले स्वचालित रूपमा Inspector सुरु गर्छ र आवश्यक प्रोक्सी सत्र टोकन प्रदान गर्छ। यदि `mcp run server.py` प्रयोग गर्दै हुनुहुन्छ भने, तपाईंले म्यानुअली Inspector सुरु गर्न र जडान कन्फिगर गर्नुपर्नेछ।

#### .NET

पक्का गर्नुहोस् कि तपाईं आफ्नो परियोजना डिरेक्टरीमा हुनुहुन्छ:

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

सर्भर फर्म्याट र चलाउन तलका आदेशहरू चलाउनुहोस्:

```sh
cargo fmt
cargo run
```

### -8- Inspector प्रयोग गरेर चलाउनुहोस्

Inspector एक उत्कृष्ट उपकरण हो जसले तपाईंको सर्भर सुरु गर्न सक्छ र तपाईंलाई यससँग अन्तरक्रिया गर्न दिन्छ ताकि तपाईं परीक्षण गर्न सक्नुहुन्छ कि यो काम गर्छ कि गर्दैन। सुरु गरौं:

> [!NOTE]
> "command" फिल्डमा फरक देखिन सक्छ किनकि यसमा तपाईंको विशिष्ट रनटाइमसँग सर्भर चलाउने आदेश हुन्छ।

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

वा यसलाई तपाईंको *package.json* मा यसरी थप्नुहोस्: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` र त्यसपछि `npm run inspector` चलाउनुहोस्।

#### Python

Python ले Node.js उपकरण inspector लाई र्याप गर्दछ। यसलाई यसरी कल गर्न सकिन्छ:

```sh
mcp dev server.py
```

तर, यसले उपकरणमा उपलब्ध सबै विधिहरू कार्यान्वयन गर्दैन त्यसैले तपाईंलाई सिधै Node.js उपकरण चलाउन सिफारिस गरिन्छ:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

यदि तपाईं स्क्रिप्टहरू चलाउन आदेश र आर्गुमेन्टहरू कन्फिगर गर्न अनुमति दिने उपकरण वा IDE प्रयोग गर्दै हुनुहुन्छ,
पक्का गर्नुहोस् कि `Command` फिल्डमा `python` सेट गरिएको छ र `Arguments` मा `server.py` छ। यसले स्क्रिप्ट सही रूपमा चल्ने सुनिश्चित गर्दछ।

#### .NET

पक्का गर्नुहोस् कि तपाईं आफ्नो प्रोजेक्ट डाइरेक्टरीमा हुनुहुन्छ:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

पक्का गर्नुहोस् कि तपाईंको क्याल्कुलेटर सर्भर चलिरहेको छ
फेरि इन्स्पेक्टर चलाउनुहोस्:

```cmd
npx @modelcontextprotocol/inspector
```

इन्स्पेक्टर वेब इन्टरफेसमा:

1. ट्रान्सपोर्ट प्रकारको रूपमा "SSE" चयन गर्नुहोस्
2. URL सेट गर्नुहोस्: `http://localhost:8080/sse`
3. "Connect" मा क्लिक गर्नुहोस्

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.ne.png)

**तपाईं अब सर्भरसँग जडान हुनुहुन्छ**
**Java सर्भर परीक्षण खण्ड अब पूरा भयो**

अर्को खण्ड सर्भरसँग अन्तरक्रिया गर्ने बारेमा हो।

तपाईंले निम्न प्रयोगकर्ता इन्टरफेस देख्नु पर्नेछ:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ne.png)

1. Connect बटन चयन गरेर सर्भरसँग जडान गर्नुहोस्
  एक पटक तपाईं सर्भरसँग जडान भएपछि, तपाईंले अब निम्न देख्नु पर्नेछ:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ne.png)

1. "Tools" र "listTools" चयन गर्नुहोस्, तपाईंले "Add" देख्नु पर्नेछ, "Add" चयन गर्नुहोस् र प्यारामिटर मानहरू भर्नुहोस्।

  तपाईंले निम्न प्रतिक्रिया देख्नु पर्नेछ, अर्थात् "add" उपकरणबाट परिणाम:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.ne.png)

बधाई छ, तपाईंले आफ्नो पहिलो सर्भर सिर्जना र चलाउन सफल हुनुभयो!

#### Rust

MCP Inspector CLI सँग Rust सर्भर चलाउन, तलको कमाण्ड प्रयोग गर्नुहोस्:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### आधिकारिक SDK हरू

MCP ले विभिन्न भाषाहरूका लागि आधिकारिक SDK हरू प्रदान गर्दछ:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft सँग सहकार्यमा मर्मत गरिएको
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI सँग सहकार्यमा मर्मत गरिएको
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - आधिकारिक TypeScript कार्यान्वयन
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - आधिकारिक Python कार्यान्वयन
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - आधिकारिक Kotlin कार्यान्वयन
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI सँग सहकार्यमा मर्मत गरिएको
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - आधिकारिक Rust कार्यान्वयन

## मुख्य बुँदाहरू

- MCP विकास वातावरण सेटअप भाषा-विशिष्ट SDK हरूको साथ सरल छ
- MCP सर्भरहरू निर्माण गर्दा स्पष्ट स्किमासहित उपकरणहरू सिर्जना र दर्ता गर्नुपर्छ
- परीक्षण र डिबगिङ विश्वसनीय MCP कार्यान्वयनका लागि आवश्यक छ

## नमूनाहरू

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## कार्य

आफ्नो रोजाइको उपकरणसहित सरल MCP सर्भर सिर्जना गर्नुहोस्:

1. आफ्नो मनपर्ने भाषामा उपकरण कार्यान्वयन गर्नुहोस् (.NET, Java, Python, TypeScript, वा Rust)।
2. इनपुट प्यारामिटरहरू र रिटर्न मानहरू परिभाषित गर्नुहोस्।
3. सर्भर ठीकसँग काम गर्छ कि भनी सुनिश्चित गर्न इन्स्पेक्टर उपकरण चलाउनुहोस्।
4. विभिन्न इनपुटहरूसँग कार्यान्वयन परीक्षण गर्नुहोस्।

## समाधान

[Solution](./solution/README.md)

## थप स्रोतहरू

- [Azure मा Model Context Protocol प्रयोग गरेर एजेन्टहरू निर्माण गर्नुहोस्](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps सँग रिमोट MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## के छ अर्को

अर्को: [MCP क्लाइन्टहरूसँग सुरु गर्दै](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->