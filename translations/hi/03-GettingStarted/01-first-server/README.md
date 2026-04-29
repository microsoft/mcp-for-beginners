# MCP के साथ शुरुआत करना

Model Context Protocol (MCP) के साथ आपके पहले कदमों में आपका स्वागत है! चाहे आप MCP में नए हों या अपनी समझ को गहरा करना चाहते हों, यह गाइड आपको आवश्यक सेटअप और विकास प्रक्रिया के माध्यम से मार्गदर्शन करेगा। आप जानेंगे कि MCP कैसे AI मॉडल और अनुप्रयोगों के बीच सहज एकीकरण सक्षम करता है, और कैसे जल्दी से अपना वातावरण तैयार किया जाए ताकि MCP-संचालित समाधानों का निर्माण और परीक्षण किया जा सके।

> TLDR; यदि आप AI ऐप्स बनाते हैं, तो आप जानते हैं कि आप अपने LLM (बड़े भाषा मॉडल) में उपकरण और अन्य संसाधन जोड़ सकते हैं, ताकि LLM अधिक जानकार हो सके। हालांकि, यदि आप उन उपकरणों और संसाधनों को किसी सर्वर पर रखते हैं, तो ऐप और सर्वर की क्षमताएं किसी भी क्लाइंट द्वारा LLM के साथ/बिना उपयोग की जा सकती हैं।

## अवलोकन

यह पाठ MCP वातावरण सेटअप करने और अपने पहले MCP अनुप्रयोग बनाने के व्यावहारिक मार्गदर्शन प्रदान करता है। आप आवश्यक उपकरण और फ्रेमवर्क सेटअप करना, मूल MCP सर्वर बनाना, होस्ट अनुप्रयोग बनाना, और अपने कार्यान्वयन का परीक्षण करना सीखेंगे।

Model Context Protocol (MCP) एक खुला प्रोटोकॉल है जो यह मानकीकृत करता है कि अनुप्रयोग कैसे LLMs को संदर्भ प्रदान करते हैं। MCP को AI अनुप्रयोगों के लिए USB-C पोर्ट की तरह सोचें - यह AI मॉडल को विभिन्न डेटा स्रोतों और उपकरणों से जोड़ने का एक मानकीकृत तरीका प्रदान करता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- C#, Java, Python, TypeScript, और Rust में MCP के लिए विकास वातावरण सेटअप करना
- कस्टम फीचर्स (संसाधन, प्रॉम्प्ट, और उपकरण) के साथ बुनियादी MCP सर्वर बनाना और डिप्लॉय करना
- MCP सर्वरों से कनेक्ट होने वाले होस्ट अनुप्रयोग बनाना
- MCP कार्यान्वयन का परीक्षण और डिबग करना

## अपना MCP वातावरण सेटअप करना

MCP के साथ काम शुरू करने से पहले, अपने विकास वातावरण को तैयार करना और बुनियादी कार्यप्रवाह को समझना महत्वपूर्ण है। यह भाग आपको प्रारंभिक सेटअप चरणों में मार्गदर्शन करेगा ताकि MCP के साथ एक सुचारू शुरुआत सुनिश्चित हो सके।

### पूर्वापेक्षाएँ

MCP विकास में डुबकी लगाने से पहले, सुनिश्चित करें कि आपके पास है:

- **विकास वातावरण**: आपकी चुनी हुई भाषा (C#, Java, Python, TypeScript, या Rust) के लिए
- **IDE/संपादक**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, या कोई आधुनिक कोड संपादक
- **पैकेज प्रबंधक**: NuGet, Maven/Gradle, pip, npm/yarn, या Cargo
- **API कुंजी**: जिन AI सेवाओं का आप अपने होस्ट अनुप्रयोगों में उपयोग करने की योजना बना रहे हैं उनके लिए

## बुनियादी MCP सर्वर संरचना

एक MCP सर्वर सामान्यतः शामिल करता है:

- **सर्वर कॉन्फ़िगरेशन**: पोर्ट, प्रमाणीकरण, और अन्य सेटिंग्स सेटअप करना
- **संसाधन**: LLMs के लिए उपलब्ध डेटा और संदर्भ
- **उपकरण**: वे कार्यक्षमताएं जिन्हें मॉडल कॉल कर सकते हैं
- **प्रॉम्प्ट**: टेक्स्ट बनाने या संरचित करने के लिए टेम्प्लेट

यहाँ TypeScript में एक सरल उदाहरण है:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्वर बनाएँ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// एक अतिरिक्त उपकरण जोड़ें
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन संसाधन जोड़ें
server.resource(
  "file",
  // 'list' पैरामीटर नियंत्रित करता है कि संसाधन उपलब्ध फ़ाइलों को कैसे सूचीबद्ध करता है। इसे undefined पर सेट करने से इस संसाधन के लिए सूचीबद्ध करना अक्षम हो जाता है।
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// एक फ़ाइल संसाधन जोड़ें जो फ़ाइल की सामग्री पढ़ता है
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

// stdin पर संदेश प्राप्त करना और stdout पर संदेश भेजना शुरू करें
const transport = new StdioServerTransport();
await server.connect(transport);
```

पिछले कोड में हमने:

- MCP TypeScript SDK से आवश्यक क्लासेज आयात किए।
- एक नया MCP सर्वर इंस्टेंस बनाया और कॉन्फ़िगर किया।
- एक कस्टम टूल (`calculator`) को एक हैंडलर फंक्शन के साथ पंजीकृत किया।
- आने वाले MCP अनुरोधों को सुनने के लिए सर्वर शुरू किया।

## परीक्षण और डिबगिंग

अपने MCP सर्वर का परीक्षण शुरू करने से पहले, उपलब्ध उपकरणों और डिबगिंग के लिए सर्वोत्तम प्रथाओं को समझना महत्वपूर्ण है। प्रभावी परीक्षण सुनिश्चित करता है कि आपका सर्वर अपेक्षित व्यवहार करता है और आपको जल्दी से समस्याओं की पहचान और समाधान करने में मदद करता है। निम्नलिखित अनुभाग आपके MCP कार्यान्वयन को सत्यापित करने के लिए अनुशंसित दृष्टिकोण प्रस्तुत करता है।

MCP आपको अपने सर्वर का परीक्षण और डिबग करने में मदद करने के लिए उपकरण प्रदान करता है:

- **Inspector टूल**, यह ग्राफिकल इंटरफ़ेस आपको अपने सर्वर से कनेक्ट करने और अपने टूल, प्रॉम्प्ट और संसाधनों का परीक्षण करने की अनुमति देता है।
- **curl**, आप अपने सर्वर से कनेक्ट करने के लिए कमांड लाइन टूल जैसे curl या अन्य क्लाइंट का भी उपयोग कर सकते हैं जो HTTP कमांड बना और चला सकते हैं।

### MCP Inspector का उपयोग

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) एक विज़ुअल परीक्षण उपकरण है जो आपकी मदद करता है:

1. **सर्वर क्षमताओं की खोज करें**: उपलब्ध संसाधन, उपकरण, और प्रॉम्प्ट स्वचालित रूप से पहचानें
2. **टूल निष्पादन का परीक्षण करें**: विभिन्न पैरामीटर आज़माएं और प्रतिक्रियाएं वास्तविक समय में देखें
3. **सर्वर मेटाडेटा देखें**: सर्वर सूचना, स्कीमा, और विन्यासों की जांच करें

```bash
# उदाहरण के लिए TypeScript, MCP इंस्पेक्टर इंस्टॉल करना और चलाना
npx @modelcontextprotocol/inspector node build/index.js
```

जब आप ऊपर के कमांड चलाते हैं, तो MCP Inspector आपके ब्राउज़र में एक स्थानीय वेब इंटरफ़ेस लॉन्च करेगा। आपको एक डैशबोर्ड देखने को मिलेगा जो आपके पंजीकृत MCP सर्वरों, उनके उपलब्ध टूल, संसाधनों, और प्रॉम्प्ट को दर्शाता है। यह इंटरफ़ेस आपको इंटरैक्टिव रूप से टूल निष्पादन का परीक्षण करने, सर्वर मेटाडेटा का निरीक्षण करने, और वास्तविक समय प्रतिक्रियाएं देखने में सक्षम बनाता है, जिससे आपके MCP सर्वर कार्यान्वयन को मान्य और डिबग करना आसान हो जाता है।

यहाँ इसका एक स्क्रीनशॉट है:

![MCP Inspector server connection](../../../../translated_images/hi/connected.73d1e042c24075d3.webp)

## सामान्य सेटअप समस्याएँ और समाधान

| समस्या | संभावित समाधान |
|-------|-------------------|
| कनेक्शन अस्वीकृत | जांचें कि सर्वर चल रहा है और पोर्ट सही है |
| टूल निष्पादन त्रुटियाँ | पैरामीटर सत्यापन और त्रुटि हैंडलिंग की समीक्षा करें |
| प्रमाणीकरण असफलताएँ | API कुंजियों और अनुमतियों की पुष्टि करें |
| स्कीमा सत्यापन त्रुटियाँ | सुनिश्चित करें कि पैरामीटर परिभाषित स्कीमा से मेल खाते हैं |
| सर्वर शुरू नहीं हो रहा | पोर्ट संघर्ष या गुमDependencies की जाँच करें |
| CORS त्रुटियाँ | क्रॉस-ओरिजिन अनुरोधों के लिए उचित CORS हेडर कॉन्फ़िगर करें |
| प्रमाणीकरण समस्याएँ | टोकन की वैधता और अनुमतियों की पुष्टि करें |

## स्थानीय विकास

स्थानीय विकास और परीक्षण के लिए, आप अपने मशीन पर सीधे MCP सर्वर चला सकते हैं:

1. **सर्वर प्रक्रिया शुरू करें**: अपना MCP सर्वर अनुप्रयोग चलाएँ
2. **नेटवर्किंग कॉन्फ़िगर करें**: सुनिश्चित करें कि सर्वर अपेक्षित पोर्ट पर पहुँच योग्य है
3. **क्लाइंट से कनेक्ट करें**: स्थानीय कनेक्शन URL जैसे `http://localhost:3000` का उपयोग करें

```bash
# उदाहरण: लोकल पर एक टाइपस्क्रिप्ट MCP सर्वर चलाना
npm run start
# सर्वर http://localhost:3000 पर चल रहा है
```

## अपना पहला MCP सर्वर बनाना

हमने पिछले पाठ में [मूल अवधारणाएँ](../../01-CoreConcepts/README.md) कवर की हैं, अब समय है उस ज्ञान को काम में लाने का।

### एक सर्वर क्या कर सकता है

कोड लिखना शुरू करने से पहले, आइए याद दिलाएं कि एक सर्वर क्या कर सकता है:

एक MCP सर्वर उदाहरण के लिए कर सकता है:

- स्थानीय फाइलों और डेटाबेस तक पहुँच
- दूरस्थ APIs से कनेक्ट होना
- गणनाएं करना
- अन्य उपकरणों और सेवाओं के साथ एकीकरण
- बातचीत के लिए उपयोगकर्ता इंटरफ़ेस प्रदान करना

बहुत बढ़िया, अब जब हमें पता है कि हम इसके लिए क्या कर सकते हैं, तो कोडिंग शुरू करते हैं।

## अभ्यास: सर्वर बनाना

सर्वर बनाने के लिए, आपको ये चरण पालन करने होंगे:

- MCP SDK इंस्टॉल करें।
- एक प्रोजेक्ट बनाएं और प्रोजेक्ट संरचना सेटअप करें।
- सर्वर कोड लिखें।
- सर्वर का परीक्षण करें।

### -1- प्रोजेक्ट बनाएं

#### TypeScript

```sh
# परियोजना निर्देशिका बनाएँ और npm परियोजना प्रारंभ करें
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# प्रोजेक्ट डिरेक्टरी बनाएं
mkdir calculator-server
cd calculator-server
# फोल्डर को विजुअल स्टूडियो कोड में खोलें - यदि आप किसी अन्य IDE का उपयोग कर रहे हैं तो इसे छोड़ दें
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java के लिए, एक Spring Boot प्रोजेक्ट बनाएं:

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

ज़िप फ़ाइल निकालें:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# वैकल्पिक रूप से अप्रयुक्त परीक्षण हटाएं
rm -rf src/test/java
```

अपने *pom.xml* फ़ाइल में निम्नलिखित पूरी कॉन्फ़िगरेशन जोड़ें:

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

### -2- निर्भरताएँ जोड़ें

अब जब आपका प्रोजेक्ट बन चुका है, तो अगला कदम निर्भरताएँ जोड़ना है:

#### TypeScript

```sh
# यदि पहले से इंस्टॉल नहीं है, तो TypeScript को वैश्विक रूप से इंस्टॉल करें
npm install typescript -g

# स्कीमा मान्यता के लिए MCP SDK और Zod इंस्टॉल करें
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# एक वर्चुअल एनवायरनमेंट बनाएं और निर्भरताएँ इंस्टॉल करें
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

### -3- प्रोजेक्ट फाइलें बनाएं

#### TypeScript

*package.json* फ़ाइल खोलें और सर्वर को बिल्ड और चलाने के लिए निम्नलिखित सामग्री से बदलें:

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

*tsconfig.json* बनाएं जिसमें निम्नलिखित कंटेंट हो:

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

अपने स्रोत कोड के लिए एक डायरेक्टरी बनाएं:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* फ़ाइल बनाएं

```sh
touch server.py
```

#### .NET

आवश्यक NuGet पैकेज इंस्टॉल करें:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot प्रोजेक्ट्स के लिए, प्रोजेक्ट संरचना स्वचालित रूप से बन जाती है।

#### Rust

Rust के लिए, `cargo init` चलाने पर *src/main.rs* फ़ाइल डिफ़ॉल्ट रूप से बन जाती है। फ़ाइल खोलें और डिफ़ॉल्ट कोड हटा दें।

### -4- सर्वर कोड बनाएं

#### TypeScript

*index.ts* नामक फ़ाइल बनाएं और निम्नलिखित कोड जोड़ें:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// एक MCP सर्वर बनाएं
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

अब आपका एक सर्वर है, लेकिन यह ज्यादा कुछ नहीं करता, आइए इसे ठीक करें।

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# एक MCP सर्वर बनाएं
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

Java के लिए, मुख्य सर्वर घटक बनाएं। पहले, मुख्य एप्लिकेशन क्लास को संशोधित करें:

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

कैलकुलेटर सेवा बनाएं *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**उत्पादन-तैयार सेवा के लिए वैकल्पिक घटक:**

स्टार्टअप कॉन्फ़िगरेशन बनाएं *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

हेल्थ कंट्रोलर बनाएं *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

एक अपवाद हैंडलर बनाएं *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

एक कस्टम बैनर बनाएं *src/main/resources/banner.txt*:

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

*src/main.rs* फ़ाइल के शीर्ष पर निम्नलिखित कोड जोड़ें। यह आपके MCP सर्वर के लिए आवश्यक लाइब्रेरी और मॉड्यूल आयात करता है।

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

कैलकुलेटर सर्वर एक सरल होगा जो दो संख्याओं को जोड़ सकता है। चलिए, कैलकुलेटर अनुरोध को प्रतिनिधित्व करने के लिए एक struct बनाते हैं।

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

अगला, कैलकुलेटर सर्वर का प्रतिनिधित्व करने के लिए एक struct बनाएं। यह struct टूल राउटर रखेगा, जिसका उपयोग टूल पंजीकृत करने के लिए किया जाता है।

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

अब, हम `Calculator` struct को लागू कर सकते हैं ताकि सर्वर का एक नया उदाहरण बनाया जा सके और सर्वर हैंडलर को लागू किया जा सके जिससे सर्वर जानकारी प्रदान हो।

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

अंत में, मुख्य फ़ंक्शन को लागू करना होगा जिससे सर्वर शुरू हो सके। यह फ़ंक्शन `Calculator` struct का उदाहरण बनाएगा और इसे मानक इनपुट/आउटपुट के माध्यम से सर्व करेगा।

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

अब सर्वर अपने बारे में बुनियादी जानकारी प्रदान करने के लिए सेट हो गया है। अगला, हम जोड़ करने के लिए एक टूल जोड़ेंगे।

### -5- एक टूल और एक संसाधन जोड़ना

निम्नलिखित कोड जोड़ कर एक टूल और एक संसाधन जोड़ें:

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

आपका टूल पैरामीटर्स `a` और `b` लेता है और एक प्रतिक्रिया उत्पन्न करता है इस रूप में:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

आपके संसाधन को "greeting" स्ट्रिंग के माध्यम से एक्सेस किया जाता है और यह एक पैरामीटर `name` लेता है तथा टूल के समान प्रतिक्रिया उत्पन्न करता है:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# एक जोड़ उपकरण जोड़ें
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन संसाधन जोड़ें
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

पिछले कोड में हमने:

- एक टूल `add` परिभाषित किया जो कि पैरामीटर्स `a` और `b` लेता है, दोनों पूर्णांक।
- एक `greeting` नाम का संसाधन बनाया जो पैरामीटर `name` लेता है।

#### .NET

इसे अपनी Program.cs फ़ाइल में जोड़ें:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

उपकरण पहले ही पिछले चरण में बनाए जा चुके हैं।

#### Rust

`impl Calculator` ब्लॉक के अंदर एक नया टूल जोड़ें:

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

चलो वह अंतिम कोड जोड़ते हैं जिसकी जरूरत है ताकि सर्वर शुरू हो सके:

#### TypeScript

```typescript
// stdin पर संदेश प्राप्त करना शुरू करें और stdout पर संदेश भेजना शुरू करें
const transport = new StdioServerTransport();
await server.connect(transport);
```

यहाँ पूरा कोड है:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्वर बनाएं
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// एक अतिरिक्त टूल जोड़ें
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन संसाधन जोड़ें
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

// stdin पर संदेश प्राप्त करना शुरू करें और stdout पर संदेश भेजें
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# एक MCP सर्वर बनाएं
mcp = FastMCP("Demo")


# एक जोड़ टूल जोड़ें
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन संसाधन जोड़ें
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# मुख्य निष्पादन ब्लॉक - सर्वर चलाने के लिए यह आवश्यक है
if __name__ == "__main__":
    mcp.run()
```

#### .NET

एक Program.cs फ़ाइल बनाएं निम्नलिखित सामग्री के साथ:

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

आपकी पूरी मुख्य एप्लिकेशन क्लास इस प्रकार दिखनी चाहिए:

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

Rust सर्वर के लिए अंतिम कोड इस तरह दिखना चाहिए:

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

### -7- सर्वर का परीक्षण करें

सर्वर को निम्नलिखित कमांड के साथ शुरू करें:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector का उपयोग करने के लिए, `mcp dev server.py` का उपयोग करें जो स्वचालित रूप से Inspector लॉन्च करता है और आवश्यक प्रॉक्सी सेशन टोकन प्रदान करता है। यदि आप `mcp run server.py` का उपयोग करते हैं, तो आपको मैन्युअली Inspector शुरू करना होगा और कनेक्शन कॉन्फ़िगर करना होगा।

#### .NET

सुनिश्चित करें कि आप अपने प्रोजेक्ट डायरेक्टरी में हैं:

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

सर्वर को फॉर्मेट और रन करने के लिए निम्नलिखित कमांड चलाएं:

```sh
cargo fmt
cargo run
```

### -8- Inspector का उपयोग कर चलाएं

Inspector एक उत्कृष्ट उपकरण है जो आपका सर्वर स्टार्ट करता है और आपको इसके साथ इंटरैक्ट करने देता है ताकि आप टेस्ट कर सकें कि यह काम करता है। चलिए इसे शुरू करते हैं:

> [!NOTE]
> यह "command" फ़ील्ड में अलग दिख सकता है क्योंकि इसमें आपके विशेष रनटाइम के साथ सर्वर चलाने के लिए कमांड होता है।

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

या इसे अपनी *package.json* में ऐसे जोड़ें: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` और फिर `npm run inspector` चलाएं

#### Python

Python, Node.js के एक टूल inspector को रैप करता है। आप इसे इस तरह कॉल कर सकते हैं:

```sh
mcp dev server.py
```

हालांकि, यह उस टूल के सभी मेथड्स को नहीं लागू करता है, इसलिए आपको सीधे Node.js टूल चलाने की सलाह दी जाती है जैसे नीचे:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

यदि आप ऐसा टूल या IDE उपयोग कर रहे हैं जो स्क्रिप्ट चलाने के लिए कमांड और आर्गुमेंट्स कॉन्फ़िगर करने की अनुमति देता है,
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

![Connect](../../../../translated_images/hi/tool.163d33e3ee307e20.webp)

**You're now connected to the server**
**The Java server testing section is completed now**

The next section it's about interacting with the server.

You should see the following user interface:

![Connect](../../../../translated_images/hi/connect.141db0b2bd05f096.webp)

1. Connect to the server by selecting the Connect button
  Once you connect to the server, you should now see the following:

  ![Connected](../../../../translated_images/hi/connected.73d1e042c24075d3.webp)

1. Select "Tools" and "listTools", you should see "Add" show up, select "Add" and fill in the parameter values.

  You should see the following response, i.e a result from "add" tool:

  ![Result of running add](../../../../translated_images/hi/ran-tool.a5a6ee878c1369ec.webp)

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
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। जबकि हम सटीकतापूर्वक अनुवाद के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->