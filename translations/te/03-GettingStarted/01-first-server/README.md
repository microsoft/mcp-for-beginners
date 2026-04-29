# MCP తో ప్రారంభించడం

Model Context Protocol (MCP) తో మీ మొదటి అడుగులకు స్వాగతం! మీరు MCP లో కొత్తవారు అయితే గానీ లేదా మీ అర్థనాన్ని గాఢం చేసుకోవాలనుకుంటున్నట్లయితే, ఈ గైడ్ మీకు అవసరమైన సెటప్ మరియు అభివృద్ధి ప్రక్రియలో మీకు మార్గనిర్దేశం చేస్తుంది. మీరు కలిగి ఉంటారు ఎలా MCP AI మోడల్స్ మరియు అప్లికేషన్ల మధ్య సులభమైన ఇంటిగ్రేషన్ ను సత్వరంగా సాధించడానికి సహాయం చేస్తుందో తెలుసుకుని, MCP ఆధారిత పరిష్కారాలను నిర్మించడం మరియు పరీక్షించడం కోసం మీ పరిసరాలను ఎలా సిద్దం చేసుకోవాలో నేర్చుకుంటారు.

> TLDR; మీరు AI యాప్స్ తయారు చేస్తే, మీరు మీ LLM (విస్తృత భాషా మోడల్)కి మరింత విజ్ఞానం కోసం సాధనాలు మరియు ఇతర వనరులను జోడించగలమని తెలుసుకుంటారు. అయితే, మీరు ఆ సాధనాలు మరియు వనరులను సర్వర్ పై ఉంచినప్పుడు, యాప్లికేషన్ మరియు సర్వర్ సామర్థ్యాలను ఏ LLM ఉన్న/లేని క్లయింట్ ద్వారా ఉపయోగించొచ్చు.

## అవలోకనం

ఈ పాఠం MCP పరిసరాలను సెట్ చేయడం మరియు మీ మొదటి MCP యాప్‌లను తయారుచేయడంపై ప్రాక్టికల్ గైడెన్స్ అందిస్తుంది. మీరు అవసరమైన సాధనాలు మరియు ఫ్రేమ్‌వర్క్‌లను సెటప్ చేయడం, ప్రాథమిక MCP సర్వర్లను నిర్మించడం, హోస్ట్ యాప్లికేషన్లను సృష్టించడం, మరియు మీ అమలు చేసిన ఫంక్షన్లను పరీక్షించడాన్ని నేర్చుకుంటారు.

Model Context Protocol (MCP) అనేది అప్లికేషన్లు ఎలా LLMలకు సందర్భం అందిస్తాయో సాందర్భీకరణ చేసే ఓపెన్ ప్రోటోకాల్. MCPని AI అప్లికేషన్లకు USB-C పోర్ట్ లాగా అనుకోండి – ఇది AI మోడల్స్ ను వివిధ డేటా వనరులు మరియు సాధనాలతో అనుసంధానం చేసేందుకు ఒక సాందర్భీకృత మార్గాన్ని అందిస్తుంది.

## నేర్చుకునేందునుకి లక్ష్యాలు

ఈ పాఠం చివరికి, మీరు చేయగలుగుతారు:

- C#, Java, Python, TypeScript, మరియు Rustలో MCP కోసం అభివృద్ధి పరిసరాలను సెట్ చేయడం
- కస్టమ్ ఫీచర్లతో (వనరులు, ప్రాంప్ట్‌లు, సాధనాలు) ప్రాథమిక MCP సర్వర్లను నిర్మించి డిప్లాయ్ చేయడం
- MCP సర్వర్లకు కనెక్ట్ అయ్యే హోస్ట్ యాప్లికేషన్లను సృష్టించడం
- MCP అమలును పరీక్షించి డీబగ్ చేయడం

## మీ MCP పరిసరం సెట్ చేయడం

MCPతో పని ప్రారంభించే ముందు, మీ అభివృద్ధి పరిసరాన్ని సిద్ధం చేసుకోవడం మరియు ప్రాథమిక వర్క్‌ఫ్లోను అర్థం చేసుకోవడం ముఖ్యం. ఈ విభాగం మీరు సాఫీగా MCPతో ప్రారంభించాలని ప్రారంభ సెట్ అప్ దశలను గైడ్ చేస్తుంది.

### ప్రీ-రిక్విజిట్లు

MCP అభివృద్ధిలో దిగడమునకు ముందు, దయచేసి ఇవి కలిగినట్టు చూసుకోండి:

- **అభివృద్ధి పరిసరం**: మీరు ఎంచుకున్న భాష (C#, Java, Python, TypeScript, లేదా Rust) కొరకు
- **IDE/ఎడిటర్**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, లేదా ఏ ఆధునిక కోడ్ ఎడిటర్
- **ప్యాకేజీ మేనేజర్లు**: NuGet, Maven/Gradle, pip, npm/yarn, లేదా Cargo
- **API కీలు**: మీ హోస్ట్ అప్లికేషన్లలో ఉపయోగించబోయే ఏదైనా AI సేవల కొరకు

## ప్రాథమిక MCP సర్వర్ నిర్మాణం

MCP సర్వర్ సాధారణంగా కలిగి ఉంటుంది:

- **సర్వర్ కాన్ఫిగరేషన్**: పోర్ట్, ఆథెంటికేషన్, మరియు ఇతర సెట్టింగ్స్ సెట్ చేయడం
- **వనరులు**: LLMలకు అందుబాటులో ఉన్న డేటా మరియు సందర్భం
- **సాధనాలు**: మోడల్స్ కాల్ చేయగల ఫంక్షనాలిటీ
- **ప్రాంప్ట్‌లు**: పాఠ్యాన్ని నిర్మించడాని కోసం టెంప్లేట్లు

ఇది TypeScript లో ఒక సులభీకృత ఉదాహరణ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP సర్వర్‌ని సృష్టించండి
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ఒక అదనపు టూల్‌ను జోడించండి
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// డైనమిక్ శుభాకాంక్షల వనరును జోడించండి
server.resource(
  "file",
  // 'list' పారామీటర్ వనరు అందుబాటులో ఉన్న ఫైళ్లను ఎలా జాబితా చేస్తుందో నియంత్రిస్తుంది. దాన్ని నిర్వచించని స్థాయికి సెట్ చేయడం వల్ల ఈ వనరుకు జాబితా చేయడం నిలిపివేయబడుతుంది.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// ఫైల్ విషయాలను చదివే ఫైల్ వనరును జోడించండి
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

// stdin పై సందేశాలు స్వీకరించడం మరియు stdout పై సందేశాలు పంపించడం ప్రారంభించండి
const transport = new StdioServerTransport();
await server.connect(transport);
```

గత కోడులో మనం:

- MCP TypeScript SDK నుండి అవసరమైన తరగతులను దిగుమతిచేశాం.
- ఒక కొత్త MCP సర్వర్ ఇన్స్టాన్స్ ని సృష్టించి కాన్ఫిగర్ చేసాము.
- ఒక కస్టమ్ సాధనాన్ని (`calculator`) హ్యాండ్లర్ ఫంక్షన్ తో రిజిస్టర్ చేశాం.
- MCP అభ్యర్థనలను వినడానికి సర్వర్‌ను ప్రారంభించాము.

## పరీక్షించడం మరియు డీబగ్గింగ్

మీ MCP సర్వర్ ని పరీక్షించడానికి ముందు, అందుబాటులో ఉన్న సాధనాల గురించి మరియు డీబగ్గింగ్ మంచి పద్ధతులను అర్థం చేసుకోవడం ముఖ్యం. సమర్థవంతమైన పరీక్ష వివరాలను మన సర్వర్ ఎలా స్పందిస్తున్నదో తెలుసుకొని సమస్యలను త్వరగా గుర్తించి పరిష్కరించడంలో సహాయపడుతుంది. క్రింది విభాగంలో MCP అమలును ధృవీకరించడం కోసం శ్రేష్ట మార్గాలు వివరించబడ్డాయి.

MCP మీ సర్వర్లను పరీక్షించడంలో మరియు డీబగ్ చేయడంలో సహాయపడే సాధనాలను అందిస్తుంది:

- **Inspector tool**, ఈ గ్రాఫికల్ ఇంటర్‌ఫేస్ మీ సర్వర్‌కు కనెక్ట్ అయినట్లుగా మీ సాధనాలు, ప్రాంప్ట్‌లు, వనరులను పరీక్షించవచ్చు.
- **curl**, మీరు curl లేదా ఇతర కమాండ్ లైన్ టూల్‌ల సహాయంతో కూడా మీ సర్వర్‌కి కనెక్ట్ కావచ్చు, HTTP కమాండ్లును సృష్టించి ఉపయోగించగలుగుతారు.

### MCP Inspector ఉపయోగించడం

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ఒక విజువల్ పరీక్షా సాధనము, ఇది మీకు సహాయపడుతుంది:

1. **సర్వర్ సామర్థ్యాలను కనుగొనండి**: అందుబాటులో ఉన్న వనరులు, సాధనాలు, మరియు ప్రాంప్ట్‌లను ఆటోమేటిక్‌గా గుర్తించడం
2. **సాధన అమలుపై పరీక్షించండి**: వివిధ పరిమితులను ప్రయత్నించండి మరియు ప్రత్యక్ష సమాధానాలు చూడండి
3. **సర్వర్ మెటాడేటాను వీక్షించండి**: సర్వర్ సమాచారం, స్కీమాలు మరియు కాన్ఫిగరేషన్‌లను పరిశీలించండి

```bash
# ఉదాహరణ TypeScript, MCP ఇన్స్పెక్టర్ సంస్థాపించడం మరియు నడపడం
npx @modelcontextprotocol/inspector node build/index.js
```

మీరు పై కమాండ్లను నడిపినప్పుడు MCP Inspector బ్రౌజర్ లో స్థానిక వెబ్ ఇంటర్‌ఫేస్ ను ప్రారంభిస్తుంది. మీరు నమోదు చేసిన MCP సర్వర్లు, అందుబాటులో ఉన్న సాధనాలు, వనరులు, మరియు ప్రాంప్ట్‌ల డాష్బోర్డ్ను చూడచ్చు. ఈ ఇంటర్‌ఫేస్ ద్వారా మీరు ఇంటరాక్టివ్‌ గ సాధన అమలుపై పరీక్షించవచ్చు, సర్వర్ మెటాడేటాను పరిశీలించవచ్చు, ప్రత్యక్ష సమాధానాలను చూస్తూ మీ MCP సర్వర్ అమలును సులభంగా ధృవీకరించవచ్చు మరియు డీబగ్ చేయవచ్చు.

ఇది ఇలా కనిపించొచ్చు:

![MCP Inspector server connection](../../../../translated_images/te/connected.73d1e042c24075d3.webp)

## సాధారణ సెటప్ సమస్యలు మరియు పరిష్కారాలు

| సమస్య | సాధ్యమైన పరిష్కారం |
|-------|-------------------|
| కనెక్షన్ తిరస్కరించడం | సర్వర్ నడుస్తుందో లేదో, పోర్ట్ సరైనదో తనిఖీ చేయండి |
| సాధన అమలులో లోపాలు | పరిమితుల ధృవీకరణ మరియు లోపాల నిర్వహణను పునః సమీక్షించండి |
| గుర్తింపు విఫలమవడం | API కీలు మరియు అనుమతులను ధృవీకరించండి |
| స్కీమా ధృవీకరణ లోపాలు | పరామితులు నిర్వచించబడిన స్కీమాకు సరిపోతున్నాయా వెరిఫై చేయండి |
| సర్వర్ ప్రారంభం కాకపోవడం | పోర్ట్ ఘర్షణలు లేదా తప్పు ఆధారాలను తనిఖీ చేయండి |
| CORS లోపాలు | క్రాస్-ఒరిజిన్ అభ్యర్థనల కొరకు సరైన CORS హెడ్డర్లను కాన్ఫిగర్ చేయండి |
| గుర్తింపు సమస్యలు | టోకెన్ చెలామణీగా ఉందో, అనుమతులు సరైనవో తనిఖీ చేయండి |

## లోకల్ అభివృద్ధి

లోకల్ అభివృద్ధి మరియు పరీక్షలకు, మీరు MCP సర్వర్లను ప్రత్యక్షంగా మీ మెషీన్లో నడిపించవచ్చు:

1. **సర్వర్ ప్రాసెస్ ప్రారంభించండి**: మీ MCP సర్వర్ అప్లికేషన్ నడపండి
2. **నెట్‌వర్కింగ్ కాన్ఫిగర్ చేయండి**: సర్వర్ సముచిత పోర్ట్ లో యాక్సెసిబుల్ కాబోతుందని చూసుకోండి
3. **క్లయింట్లను కనెక్ట్ చేయండి**: `http://localhost:3000` వంటి లోకల్ కనెక్షన్ URLలను ఉపయోగించండి

```bash
# ఉదాహరణ: TypeScript MCP సర్వర్‌ను లోకల్‌గా నడపడం
npm run start
# సర్వర్ http://localhost:3000 వద్ద నడుస్తోంది
```

## మీ మొదటి MCP సర్వర్ నిర్మించడం

మునుపటి పాఠంలో మనం [కోర్ భావనలు](../../01-CoreConcepts/README.md) చర్చించాం, ఇప్పుడు ఆ జ్ఞానాన్ని ఉపయోగించాలి.

### సర్వర్ చేయగల కొన్ని పనులు

కోడు రాయడం ప్రారంభించే ముందు, ఒక సర్వర్ చేయగల పనుల్ని మనం గుర్తుంచుకుందాం:

MCP సర్వర్ ఉదాహరణకు:

- లోకల్ ఫైళ్లను మరియు డేటాబేస్‌లను యాక్సెస్ చేయడం
- రిమోట్ APIs కు కనెక్ట్ కావడం
- గణనలు నిర్వహించడం
- ఇతర సాధనాలు మరియు సేవలతో ఇంటిగ్రేట్ కావడం
- యూజర్ ఇంటర్‌ఫేస్ కోసం ప్రావైడ్ చేయడం

చాలా బాగుంది, ఇప్పుడు మనం ఏం చేయగలామో తెలిసింది, కోడింగ్ ప్రారంభిద్దాం.

## వ్యాయామం: సర్వర్ సృష్టించడం

సర్వర్ సృష్టించడానికి, ఈ దశలను పాటించాలి:

- MCP SDK ని ఇన్‌స్టాల్ చేయండి.
- ఒక ప్రాజెక్టును సృష్టించి ప్రాజెక్ట్ నిర్మాణాన్ని సెట్ చేయండి.
- సర్వర్ కోడును రాయండి.
- సర్వర్‌ను పరీక్షించండి.

### -1- ప్రాజెక్ట్ సృష్టించండి

#### TypeScript

```sh
# ప్రాజెక్ట్ డైరెక్టరీని సృష్టించండి మరియు npm ప్రాజెక్టును ప్రారంభించండి
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# ప్రాజెక్ట్ ఫోల్డర్‌ను సృష్టించండి
mkdir calculator-server
cd calculator-server
# Visual Studio Codeలో ఫోల్డర్‌ను తెరవండి - మీరు వేరే IDE ఉపయోగిస్తుంటే దీన్ని వదిలించండి
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java కోసం, Spring Boot ప్రాజెక్ట్ సృష్టించండి:

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

జిప్ ఫైల్ ను ఎక్స్‌ట్రాక్ట్ చేయండి:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ఐచ్ఛికంగా ఉపయోగించని పరీక్షను తొలగించండి
rm -rf src/test/java
```

*pom.xml* ఫైల్‌కు క్రింది పూర్తి కాన్ఫిగరేషన్ జోడించండి:

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

### -2- డిపెండెన్సీలను జోడించండి

మీరు ప్రాజెక్ట్ సృష్టించాక, డిపెండెన్సీలను జోడిద్దాం:

#### TypeScript

```sh
# ఇప్పటికే ఇన్‌స్టాల్ చేయకపోతే, TypeScript ను గ్లోబలీ ఇన్‌స్టాల్ చేయండి
npm install typescript -g

# స్కీమా ధృవీకరణ కోసం MCP SDK మరియు Zod ను ఇన్‌స్టాల్ చేయండి
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# ఒక వర్చువల్-env సృష్టించి డిపెండెన్సీలను ఇన్స్టాల్ చేయండి
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

### -3- ప్రాజెక్ట్ ఫైళ్లు సృష్టించండి

#### TypeScript

*package.json* ఫైల్ ఓపెన్ చేసి, సర్వర్‌ను నిర్మించడానికి మరియు నడిపించడానికి క్రింది కంటెంటుతో మార్చండి:

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

*tsconfig.json*ని క్రింది కంటెంటుతో సృష్టించండి:

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

మీ సోర్స్ కోడ్ కోసం ఒక డైరెక్టరీ సృష్టించండి:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* ఫైల్ సృష్టించండి

```sh
touch server.py
```

#### .NET

అవసరమైన NuGet ప్యాకేజీలు ఇన్స్టాల్ చేయండి:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot ప్రాజెక్టుల కోసం, ప్రాజెక్ట్ నిర్మాణం స్వయంచాలకంగా సృష్టించబడుతుంది.

#### Rust

Rust కోసం, `cargo init` నడిపితే *src/main.rs* ఫైల్ డిఫాల్ట్‌గా సృష్టించబడుతుంది. ఫైల్ ఓపెన్ చేసి డిఫాల్ట్ కోడ్ ని తొలగించండి.

### -4- సర్వర్ కోడ్ సృష్టించండి

#### TypeScript

*index.ts* అనే ఫైల్ సృష్టించి క్రింది కోడ్ జతచేయండి:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// ఒక MCP సర్వర్ సృష్టించండి
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

ఇప్పుడు ఒక సర్వర్ వుంది కానీ ఎక్కువ పని చేయడం లేదు, దీన్ని ఫిక్స్ చేద్దాం.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ఒక MCP సర్వర్ సృష్టించండి
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

Java కోసం, కోర్ సర్వర్ కంపోనెంట్లను సృష్టించండి. ముందు, ప్రధాన అప్లికేషన్ క్లాస్ను మార్చండి:

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

క్యాలిక్యులేటర్ సర్వీస్ సృష్టించండి: *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**ఉత్పత్తి-సిద్ధమైన సర్వీస్‌కి ఐచ్ఛిక భాగాలు:**

స్టార్ట్‌అప్ కాన్ఫిగరేషన్ సృష్టించండి: *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

హెల్త్ కంట్రోలర్ సృష్టించండి: *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

ఎక్సెప్షన్ హ్యాండ్లర్ సృష్టించండి: *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // గెట్‌లు
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

కస్టమ్ బ్యానర్ సృష్టించండి: *src/main/resources/banner.txt*:

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

*src/main.rs* ఫైల్ సమాచారం కోసం క్రింది కోడ్ జతచేయండి. ఇది MCP సర్వర్ కోసం అవసరమైన లైబ్రరీలు మరియు మాడ్యూల్స్ ని దిగుమతిస్తుంది.

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

క్యాలిక్యులేటర్ సర్వర్ ఒక సులభమైనది, ఇది రెండు అంకెలను కలిపే పని చేస్తుంది. క్యాలిక్యులేటర్ అభ్యర్థనను ప్రతినిధించేందుకు ఒక నిర్మాణాన్ని (struct) సృష్టిద్దాం.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

తర్వాత, క్యాలిక్యులేటర్ సర్వర్ ని ప్రతినిధించేందుకు ఒక struct సృష్టించండి. ఈ struct సాధన రౌటర్ ని కలిగి ఉంటుంది, ఇది సాధనాలను రిజిస్టర్ చేయడానికి ఉపయోగపడుతుంది.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

ఇప్పుడు, `Calculator` structని అమలు చేయండి. సర్వర్ యొక్క కొత్త ఇన్స్టాన్స్ సృష్టించడానికి మరియు సర్వర్ హ్యాండ్లర్ ని అమలు చేయడానికి ఇది ఉపయోగపడుతుంది.

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

చివరగా, సర్వర్ మొదలుపెట్టడానికి మైన్ ఫంక్షన్ ని అమలు చేయాలి. ఈ ఫంక్షన్ `Calculator` struct యొక్క ఇన్స్టాన్స్ సృష్టించి స్టాండర్డ్ ఇన్పుట్/ఆట్పుట్ ద్వారా సేవ్ చేస్తుంది.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

సర్వర్ ప్రస్తుతం తన గురించి ప్రాథమిక సమాచారాన్ని అందించడానికి సిద్దంగా ఉంది. తరువాత నేను జోడించబోతున్న సాధన ఒక యాడిషన్ చేయడానికి.

### -5- సాధన మరియు వనరు జోడించడం

క్రింది కోడ్ జతచేసి సాధన మరియు వనరును జోడించండి:

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

మీ సాధనం `a` మరియు `b` పరామితులు తీసుకుని క్రింది రూపంలో స్పందనను ఉత్పత్తి చేస్తుంది:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

మీ వనరు "greeting" అనే స్ట్రింగ్ ద్వారా యాక్సెస్ అవుతుంది, ఇది `name` పరామితిని తీసుకుని సాధన విధంగా సమాధానం ఉత్పత్తి చేస్తుంది:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ఒక జతచేయు సాధనం జోడించండి
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ఒక డైనమిక్ గ్రీటింగ్ వనరును జోడించండి
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

గత కోడులో మేము:

- `add` అనే సాధనను నిర్వచించాము, ఇది `a` మరియు `b` అనే పూర్తి సంఖ్యల పరామితులు తీసుకుంటుంది.
- `greeting` అనే వనరును సృష్టించాము, ఇది `name` అనే పరామితిని తీసుకుంటుంది.

#### .NET

ఇది మీ Program.cs ఫైల్ లో జోడించండి:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

పూర్వదశలో సాధనాలను ఇప్పటికే సృష్టించారు.

#### Rust

`impl Calculator` బ్లాక్ లో కొత్త సాధన జోడించండి:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- తుది కోడ్

సర్వర్ మొదలుపెట్టటానికి అవసరమైన చివరి కోడ్ ని జోడిద్దాం:

#### TypeScript

```typescript
// stdin లో సందేశాలు అందుకోవడం మొదలు పెట్టండి మరియు stdout లో సందేశాలు పంపండి
const transport = new StdioServerTransport();
await server.connect(transport);
```

పూర్తి కోడ్ ఇది:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ఒక MCP సర్వర్‌ని సృష్టించండి
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// ఒక అదనపు టూల్‌ని జోడించండి
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ఒక డైనమిక్ అభివాద వనరును జోడించండి
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

// stdin లో మెసేజ్‌లు స్వీకరించడం ప్రారంభించి stdout లో మెసేజ్‌లు పంపడం ప్రారంభించండి
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ఒక MCP సర్వర్ సృష్టించండి
mcp = FastMCP("Demo")


# ఒక యుక్తి సాధనాన్ని జోడించండి
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ఒక డైనమిక్ స్వాగత వనరును జోడించండి
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# ప్రధాన అమలు బ్లాక్ - ఇది సర్వర్ నడిపించడానికి అవసరం
if __name__ == "__main__":
    mcp.run()
```

#### .NET

క్రింది కంటెంటుతో Program.cs ఫైల్ను సృష్టించండి:

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

మీ పూర్తి ప్రధాన అప్లికేషన్ క్లాస్ ఈ విధంగా ఉండాలి:

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

Rust సర్వర్ యొక్క తుది కోడ్ ఇలా ఉంటుంది:

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

### -7- సర్వర్ పరీక్షించండి

క్రింద చూపిన కమాండ్లతో సర్వర్‌ను ప్రారంభించండి:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector ఉపయోగించడానికి, `mcp dev server.py` ఉపయోగించండి, ఇది ఆటోమేటిక్‌గా Inspector ను ప్రారంభించి అవసరమైన ప్రోక్సీ సెషన్ టోకెన్ ఇస్తుంది. `mcp run server.py` వాడితే, మీరు చేతితో Inspector ప్రారంభించి కనెక్షన్ సెట్ చేసుకోవాలి.

#### .NET

మీరు ప్రాజెక్ట్ డైరెక్టరీలో ఉన్నారని నిర్ధారించుకోండి:

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

సర్వర్ ఫార్మాట్ చేసి నడిపేందుకు క్రింది కమాండ్లను నడుపండి:

```sh
cargo fmt
cargo run
```

### -8- Inspector ఉపయోగించి నడపడం

Inspector ఒక అద్భుతమైన సాధన, ఇది మీ సర్వర్ ను ప్రారంభించి, మీరు దీన్ని ట్రై చేయడానికి అనుమతిస్తుంది. దీన్ని ప్రారంభిద్దాం:

> [!NOTE]
> ఇది "కమాండ్" ఫీల్డ్ లో వేరుగా కనిపించవచ్చు, ఎందుకంటే ఇది మీ ప్రత్యేక రన్‌టైమ్ కోసం సర్వర్ నడిపే కమాండ్ ను కలిగి ఉంటుంది.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

లేదా మీ *package.json*కి `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ఇలా జోడించి `npm run inspector` ని నడపండి

#### Python

Python Node.js టూల్ అయిన inspector ని రాపింగ్ చేస్తుంది. ఈ టూల్ ని ఇలా కాల్ చేయవచ్చు:

```sh
mcp dev server.py
```

అయితే, ఇది టూల్ అందించే అన్ని విధానాలను అమలు చేయదు కనుక, బదులుగా Node.js టూల్ ని నేరుగా కింద రెండు విధాలా నడపటం సలహా:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

మీరు స్క్రిప్ట్‌లు నడిపే కమాండ్లు మరియు ఆర్గ్యుమెంట్స్ కాన్ఫిగర్ చేయగల టూల్ లేదా IDE ఉపయోగిస్తే,
`Command` ఫీల్డులో `python` ని మరియు `Arguments`గా `server.py` ను సెట్ చేయాలని నిర్థారించుకోండి. దీని ద్వారా స్క్రిప్ట్ సరిగ్గా నడుస్తుంది.

#### .NET

మీ ప్రాజెక్ట్ డైరెక్టరీలో ఉన్నారని నిర్ధారించుకోండి:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

మీ calculator సర్వర్ నడుస్తోందని నిర్ధారించుకోండి
తర్వాత ఇన్స్పెక్టర్‌ని నడపండి:

```cmd
npx @modelcontextprotocol/inspector
```

ఇన్స్పెక్టర్ వెబ్ ఇంటర్‌ఫేస్‌లో:

1. ట్రాన్స్పోర్ట్ టైప్‌గా "SSE" ని ఎంచుకోండి
2. URL ని ఈవిధంగా సెట్ చేయండి: `http://localhost:8080/sse`
3. "Connect" పై క్లిక్ చేయండి

![Connect](../../../../translated_images/te/tool.163d33e3ee307e20.webp)

**మీరు ఇప్పుడు సర్వర్‌కు కనెక్ట్ అయ్యారు**
**Java సర్వర్ టెస్టింగ్ సెక్షన్ ఇప్పుడు పూర్తయింది**

తర్వాతి సెక్షన్ సర్వర్‌తో ఇంటరాక్ట్ చేయడం గురించి.

మీరు క్రింది యూజర్ ఇంటర్‌ఫేస్‌ను చూడాలి:

![Connect](../../../../translated_images/te/connect.141db0b2bd05f096.webp)

1. Connect బటన్ ఎంచుకుని సర్వర్‌కు కనెక్ట్ అవ్వండి
  సర్వర్‌కి కనెక్ట్ అయిన వెంటనే, మీరు క్రింది దాన్ని చూడగలరు:

  ![Connected](../../../../translated_images/te/connected.73d1e042c24075d3.webp)

1. "Tools" మరియు "listTools" ఎంచుకోండి, "Add" కనిపిస్తుంది, "Add" ఎంచుకుని పారామీటర్ విలువలను నింపండి.

  మీరు క్రింది ప్రతిస్పందనను చూడగలరు, అంటే "add" టూల్ నుండి ఫలితం:

  ![Result of running add](../../../../translated_images/te/ran-tool.a5a6ee878c1369ec.webp)

అభినందనలు, మీరు మీ తొలి సర్వర్‌ను సృష్టించి నడపగలిగారు!

#### Rust

MCP Inspector CLI తో Rust సర్వర్ నడపడానికి, క్రింది కమాండ్ ఉపయోగించండి:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### అధికారిక SDKలు

MCP అనేక భాషలకి అధికారిక SDKలను అందిస్తుంది:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft తో కలిసి నిర్వహించబడుతోంది
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI తో కలిసి నిర్వహించబడుతోంది
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - అధికారిక TypeScript అమలు
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - అధికారిక Python అమలు
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - అధికారిక Kotlin అమలు
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI తో కలిసి నిర్వహించబడుతోంది
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - అధికారిక Rust అమలు

## ముఖ్యమైన సంగతులు

- MCP అభివృద్ధి పరిసరాన్ని భాషాపరమైన SDKలతో సులభంగా ఏర్పాటు చేయవచ్చు
- MCP సర్వర్ల నిర్మాణంలో స్పష్టమైన స్కీమాలతో టూల్స్ సృష్టించడం మరియు నమోదు చేయడం ఉంటుంది
- పరీక్షించడం మరియు డీబగింగ్ MCP అమలులో విశ్వసనీయత కోసం అవసరం

## నమూనాలు

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## ఆదేశం

మీ ఇష్టమైన టూల్‌తో సింపుల్ MCP సర్వర్ సృష్టించండి:

1. మీ అభిరుచైన భాషలో టూల్ అమలు చేయండి (.NET, Java, Python, TypeScript, లేదా Rust).
2. ఇన్పుట్ పారామీటర్లను మరియు రిటర్న్ విలువలను నిర్వచించండి.
3. సర్వర్ సరిగ్గా పనిచేస్తున్నదని నిర్ధారించడానికి ఇన్స్పెక్టర్ టూల్ నడపండి.
4. వివిధ ఇన్పుట్‌లతో అమలును పరీక్షించండి.

## పరిష్కారం

[Solution](./solution/README.md)

## అదనపు వనరులు

- [Azureలో Model Context Protocol ఉపయోగించి ఏజెంట్లు నిర్మించడం](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Appsతో రిమోట్ MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP ఏజెంట్](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## తర్వాత ఏమి

తర్వాత: [MCP క్లయింట్లతో ప్రారంభం](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:
ఈ డాక్యుమెంట్ [Co-op Translator](https://github.com/Azure/co-op-translator) అనే AI అనువాద సేవను ఉపయోగించి అనువదించబడింది. మేము సరైనత కోసం ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉన్నట్లు ఉండకూడదని దయచేసి గమనించండి. స్వదేశీ భాషలో ఉన్న అసలు డాక్యుమెంట్ అధికారిక మూలంగా పరిగణించాలి. కీలక సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదం అవసరం. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల ఏవైనా అపార్థాలు లేదా తప్పైన అర్థాలు ఉత్పన్నమైతే వాటికి మేము బాధ్యులం కాదని తెలియజేస్తున్నాము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->