# MCP தொடக்கம்

Model Context Protocol (MCP) உடன் உங்கள் முதல் படிகளை எமது வரவேற்கிறோம்! நீங்கள் MCP இல் புதியவராக இருந்தால் அல்லது உங்கள் புரிதலை ஆழமாக்க விரும்பினால், இந்த வழிகாட்டி உங்களுக்கு அடிப்படை அமைப்பு மற்றும் மேம்பாட்டு செயல்முறை வழிவகுக்கும். MCP எப்படி AI மாதிரிகள் மற்றும் செயலிகள் இடையே தடையில்லாத ஒருங்கிணைப்பை ஏற்படுத்துகிறது என்பதை நீங்கள் கண்டுபிடிப்பீர்கள், மற்றும் MCP இயங்கும் தீர்வுகளை உருவாக்கி சோதனை செய்ய உங்கள் சூழலை விரைவாக தயாரிப்பது எப்படி என்பதை கற்றுக்கொள்வீர்கள்.

> TLDR; நீங்கள் AI பயன்பாடுகளை உருவாக்குவீர்கள் என்றால், LLM (பெரிய மொழி மாதிரி)க்கு உபகரணங்கள் மற்றும் பிற வளங்களை சேர்க்கலாம் என்பதை அறிந்திருப்பீர்கள், இதனால் LLM அதிக அறிவுடையதாக மாறும். ஆனால் அந்த உபகரணங்கள் மற்றும் வளங்களை சர்வர் மீது வைத்தால், அந்த பயன்பாடு மற்றும் சர்வரின் திறன்கள் எந்தவொரு கிளையன்ட் கூட LLM உடன் அல்லது இல்லாமல் பயன்படுத்த முடியும்.

## ஒவ்வோற்றம்

இந்த பாடத்தில் MCP சூழல்கள் அமைக்கவும் முதல் MCP செயலிகளை உருவாக்கவும் தொடர்பான நடைமுறை வழிகாட்டல்களை வழங்குகிறது. தேவையான உபகரணங்கள் மற்றும் கட்டமைப்புகளை உருவாக்குவது, அடிப்படையிலான MCP சர்வர்களை கட்டமைப்பது, ஹோஸ்ட் செயலிகளை உருவாக்குவது மற்றும் உங்கள் செயல்பாடுகளை சோதிப்பது எப்படி என்பதை நீங்கள் கற்றுக்கொள்வீர்கள்.

Model Context Protocol (MCP) என்பது செயலிகள் LLM களுக்கு சூழலை வழங்கும் முறையை சிறப்புமிக்க ஒரு திறந்த நெறிமுறை ஆகும். MCP ஐ ஒரு AI செயலிகளுக்கான USB-C போர்ட் என்று கற்பனை செய்யுங்கள் — இது AI மாதிரிகளை பன்முக தரவூறுகள் மற்றும் உபகரணங்களுக்கு இணைக்க ஒரு ஒருங்கிணைந்த வழியை வழங்குகிறது.

## கற்றல் இலக்குகள்

இந்த பாடம் முடிவிற்கு, நீங்கள் செய்ய முடியும்:

- C#, Java, Python, TypeScript, மற்றும் Rust இல் MCP மேம்பாட்டு சூழல்கள் அமைப்பது
- தனிப்பயன் அம்சங்களுடன் (வளங்கள், தூண்டுதல்கள், மற்றும் உபகரணங்கள்) அடிப்படையான MCP சர்வர்கள் கட்டமைத்து வெளிமாற்றுவது
- MCP சர்வர்கள் இணைக்கக்கூடிய ஹோஸ்ட் செயலிகளை உருவாக்குவது
- MCP செயல்பாடுகளை சோதித்து பிழைகள் சரி செய்வது

## உங்கள் MCP சூழல் அமைத்தல்

MCP இல் பணியாற்ற தொடங்குவதற்கு முன், உங்கள் மேம்பாட்டு சூழலை தயார் செய்து அடிப்படையான வேலைப்பாட்டை புரிந்துகொள்ளுவது முக்கியம். இந்த பிரிவு MCP உடன் மெல்லிசைவான தொடக்கத்தை உறுதிப்படுத்த ஆரம்ப அமைப்பு படிகளை வழிகாட்டும்.

### முன் தேவைகள்

MCP மேம்பாட்டில் இறங்குவதற்கு முன், பின்வற்றவை உறுதிப்படுத்திக் கொள்ளுங்கள்:

- **மேம்பாட்டு சூழல்**: உங்கள் தேர்ந்த மொழி (C#, Java, Python, TypeScript, அல்லது Rust)
- **IDE/எடிட்டர்**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, அல்லது எந்தவொரு நவீன குறியீட்டு எடிட்டரும்
- **பேக்கேஜ் மேலாளர்கள்**: NuGet, Maven/Gradle, pip, npm/yarn, அல்லது Cargo
- **API விசைகள்**: உங்கள் ஹோஸ்ட் செயலிகளில் பயன்படுத்த உள்ள AI சேவைகளுக்கு

## அடிப்படைக் MCP சர்வர் அமைப்பு

ஒரு MCP சர்வர் பொதுவாக பின்வரும் பகுதிகளை கொண்டிருக்கும்:

- **சர்வர் கட்டமைப்பு**: போர்ட் அமைப்பு, அடையாளம் நிரூபிப்பு மற்றும் பிற அமைப்புகள்
- **வளங்கள்**: LLM களுக்கு கிடைக்கப்படும் தரவு மற்றும் சூழல்
- **உபகரணங்கள்**: மாதிரிகள் கூப்பிடக்கூடிய செயல்திறன்
- **தூண்டுதல்கள்**: உரையை உருவாக்க அல்லது கட்டமைக்க வடிவங்கள்

Typescript இல் எளிமைப்படுத்திய உதாரணம்:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ஒரு MCP சேவையகத்தை உருவாக்கவும்
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ஒரு கூட்டல் கருவியை சேர்க்கவும்
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ஒரு இயங்கக்கூடிய வரவேற்பு வளத்தை சேர்க்கவும்
server.resource(
  "file",
  // 'list' அளவுரு வளம் எவ்வாறு கிடைக்கக்கூடிய கோப்புகளை பட்டியலிடும் என்பதை கட்டுப்படுத்துகிறது. அதனை வரையறுக்காதது என்ற நிலைக்கு அமைத்தால் இந்த வளத்துக்கான பட்டியலிடல் இயக்கு முடிவடைகிறது.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// கோப்பு உள்ளடக்கங்களை படிக்கும் ஒரு கோப்பு வளத்தை சேர்க்கவும்
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

// stdinஇல் செய்திகளை பெற ஆரம்பித்து stdoutஇல் செய்திகளை அனுப்ப தொடங்கவும்
const transport = new StdioServerTransport();
await server.connect(transport);
```

புதிய குறியீட்டில் நாங்கள்:

- MCP TypeScript SDK இலிருந்து தேவையான வகுப்புகளை இறக்குமதி செய்தோம்.
- புதிய MCP சர்வர் இலக்கணத்தை உருவாக்கி அமைத்தோம்.
- தனிப்பயன் உபகரணம் (`calculator`) கைகூட்டு செயலியை பதிவு செய்தோம்.
- வரவிருக்கும் MCP கோரிக்கைகளை கேட்க சர்வரை துவங்கினோம்.

## சோதனை மற்றும் பிழைதிருத்தல்

உங்கள் MCP சர்வரை சோதனை செய்யத் தொடங்குவதற்கு முன், கிடைக்கும் உபகரணங்கள் மற்றும் சிறந்த பிழைதிருத்த நடைமுறைகளை புரிந்து கொள்வது முக்கியம். பயனுள்ள சோதனை உங்கள் சர்வர் எதிர்பார்த்தபடி செயல்படுவதை உறுதி செய்யும், மேலும் பிரச்சனைகளை விரைவாக கண்டுபிடித்து சரிசெய்ய உதவும். பின்வரும் பகுதிகள் உங்கள் MCP செயல்பாடுகளை சரிபார்க்க பரிந்துரைக்கப்படும் முறைகளைக் குறிக்கின்றன.

MCP உங்களுக்கு சர்வர்கள் சோதனை மற்றும் பிழைதிருத்த உதவிப் கருவிகளை வழங்குகிறது:

- **இன்ஸ்பெக்டர் கருவி**, இந்த காட்சி இடைமுகம் உங்கள் சர்வருடன் இணைந்து உங்கள் உபகரணங்கள், தூண்டுதல்கள் மற்றும் வளங்களை சோதிக்க அனுமதிக்கும்.
- **curl**, நீங்கள் curl அல்லது பிற HTTP கட்டளைகள் உருவாக்கி இயக்கும் CLI கருவிகளைக் கொண்டு உங்கள் சர்வருடன் இணைக்கலாம்.

### MCP இன்ஸ்பெக்டர் பயன்படுத்தல்

[MCP இன்ஸ்பெக்டர்](https://github.com/modelcontextprotocol/inspector) என்பது ஒரு காட்சி சோதனை கருவி, இது உங்கள் உதவிக்கு:

1. **சர்வர் திறன்களை கண்டறிதல்**: கிடைக்கும் வளங்கள், உபகரணங்கள் மற்றும் தூண்டுதல்களை தானாக கண்டறிதல்
2. **உபகரண செயல்பாட்டை சோதனை செய்தல்**: வித்தியாசமான அளவுருக்கள் கொண்டு முயற்சி செய்து நேரடி பதில்களை பார்வையிடுதல்
3. **சர்வர் மெட்டாடேட்டா பார்வை**: சர்வர் தகவல், நிகழ்த்தலைக் குறித்த வேலைத்திட்டங்கள் மற்றும் கட்டமைப்புகளை ஆய்வு செய்தல்

```bash
# உதாரணமாக TypeScript, MCP இன்ஸ்பெக்டரை நிறுவுவதும் இயக்குவதும்
npx @modelcontextprotocol/inspector node build/index.js
```

மேலே உள்ள கட்டளைகளை இயக்கும் போது MCP இன்ஸ்பெக்டர் உலாவியில் உள்ள ஒரு உள்ளூர் வலை இடைமுகத்தை துவக்கும். உங்கள் பதிவுசெய்த MCP சர்வர்கள், அவற்றின் கிடைக்கும் உபகரணங்கள், வளங்கள் மற்றும் தூண்டுதல்கள் ஒரு டாஷ்போர்டில் காட்சியிடப்படும். இந்த இடைமுகம் உபகரண செயல்பாட்டை தொடர்புகொள்ளவும், சர்வர் மெட்டாடேட்டாவை ஆய்வு செய்யவும், நேரடி பதில்களை பார்வையிடவும் அனுமதிக்கிறது, இது உங்கள் MCP சர்வர் செயல்பாடுகளை சரிபார்க்கவும் பிழைதிருத்தவும் எளிதாக்கும்.

இதோ அதன் தோற்றம்:

![MCP Inspector server connection](../../../../translated_images/ta/connected.73d1e042c24075d3.webp)

## பொதுவான அமைப்பு பிரச்சனைகள் மற்றும் தீர்வுகள்

| பிரச்சனை | சாத்தியமான தீர்வு |
|----------|------------------|
| இணைப்பு நிராகரிக்கப்பட்டது | சர்வர் இயங்குகிறதா, போர்ட் சரியானதா என சரிபார்க்கவும் |
| உபகரண செயல்பாடு பிழைகள் | அளவுரு சரிபார்ப்பு மற்றும் பிழை கையாளல் பரிசீலனை செய்யவும் |
| அடையாளம் நிரூபிப்பு தோல்விகள் | API விசைகள் மற்றும் அனுமதிகளை உறுதிப்படுத்தவும் |
| நிகழ்த்தல் சரித்திர பிழைகள் | அளவுருக்கள் வரையறுக்கப்பட்ட நிகழ்த்தலிற்கு பொருந்துகிறதா என சரிபார்க்கவும் |
| சர்வர் துவங்கவில்லை | போர்ட் மோதல்கள் அல்லது தகுதிகள் இல்லாமை சோதிக்கவும் |
| CORS பிழைகள் | திறப்பு தோற்றங்கள் கோரிக்கைகளுக்கு சரியான CORS தலைப்புகளை அமைக்கவும் |
| அடையாளம் நிரூபிப்பு பிரச்சனைகள் | டோக்கன் செல்லுபடியாக உள்ளதா மற்றும் அனுமதிகள் சரிபார்க்கவும் |

## உள்ளூர் மேம்பாடு

உள்நாட்டுக் மேம்பாட்டுக்கும் சோதனைக்கும், நீங்கள் உங்கள் கணியலில் நேரடியாக MCP சர்வர்களை இயக்கலாம்:

1. **சர்வர் செயலியை துவங்கு**: உங்கள் MCP சர்வர் செயலியை இயக்கவும்
2. **பணியாளர் அமைத்தல்**: சர்வர் எதிர்பார்க்கும் போர்டில் அணுகக் கூடியதா என உறுதிப்படுத்தவும்
3. **கிளையன்ட் இணைத்தல்**: `http://localhost:3000` போன்ற உள்ளூர் இணைப்பு URL களை பயன்படுத்தவும்

```bash
# எடுத்துக்காட்டு: TypeScript MCP சேவையகம் உள்ளூரில் இயக்கப்படுகிறது
npm run start
# சேவையகம் http://localhost:3000 இல் இயக்கப்படுகிறது
```

## உங்கள் முதல் MCP சர்வர் உருவாக்கல்

நாம் [முக்கிய கருத்துக்கள்](../../01-CoreConcepts/README.md) பற்றிய பாடத்தில் அவற்றைப் புரிந்துகொண்டுள்ளோம், இப்போது அந்த அறிவை நடைமுறைப்படுத்தும் நேரம்.

### சர்வர் செய்யக்கூடியவை

குறியீடு எழுதத் தொடங்கும் முன், சர்வர் என்ன செய்ய முடியும் என்பதை மட்டும் நினைவுபடுத்திக்கொள்ளலாம்:

ஒரு MCP சர்வர் உதாரணமாக:

- உள்ளூர் கோப்புகள் மற்றும் தரவுத்தளங்களை அணுக முடியும்
- தொலைநிலை API களை இணைக்க முடியும்
- கணக்கீடுகள் செய்ய முடியும்
- பிற உபகரணங்கள் மற்றும் சேவைகளுடன் ஒருங்கிணைக்க முடியும்
- தொடர்புக்கான பயனர் இடைமுகம் வழங்க முடியும்

சரி, இவற்றை நமக்கு சர்வர் செய்ய இயலும் என்று அறிந்துவிட்டோம், எழுதத் தொடங்குவோம்.

## பயிற்சி: சர்வர் உருவாக்குதல்

சர்வர் உருவாக்க, கீழ்காணும் படிமுறைகளை பின்பற்ற வேண்டும்:

- MCP SDK ஐ நிறுவவும்.
- ஒரு திட்டத்தை உருவாக்கி திட்ட அமைப்பை செய்யவும்.
- சர்வர் குறியீட்டை எழுதவும்.
- சர்வரை சோதனை செய்யவும்.

### -1- திட்டத்தை உருவாக்குதல்

#### TypeScript

```sh
# திட்ட அடைவைக் கொண்டு உருவாக்கி npm திட்டத்தைத் துவங்கவும்
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# திட்ட அடைவை உருவாக்கவும்
mkdir calculator-server
cd calculator-server
# இந்த கோப்புறையை Visual Studio Code இல் திறக்கவும் - நீங்கள் வேறு IDE ஐ பயன்படுத்தினால் இவ்வதைத் தவிர்க்கவும்
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java க்காக, ஒரு Spring Boot திட்டத்தை உருவாக்கவும்:

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

பிட் கோப்பை வெளியீடு செய்யவும்:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# விருப்பமாக பயன்படுத்தப்படாத சோதனையை நீக்கு
rm -rf src/test/java
```

*pom.xml* கோப்பில் கீழ்க்காணும் முழுமையான கட்டமைப்பை சேர்க்கவும்:

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

### -2- அனுசரணைகள் சேர்த்தல்

திறக்கப்பட்ட திட்டத்திற்கு இப்போது அனுசரணைகளை சேர்க்கலாம்:

#### TypeScript

```sh
# ஏற்கனவே நிறுவப்பட்டிருந்தால் மட்டும் இல்லையெனில், TypeScript ஐ உலகளாவியமாக நிறுவுக
npm install typescript -g

# MCP SDK மற்றும் Zod ஐ ஸ்கீமா சரிபார்ப்பிற்கு நிறுவுக
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# ஒரு காட்சிப்பட_env உருவாக்கி சார்புகளை நிறுவுக
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

### -3- திட்ட கோப்புகள் உருவாக்கல்

#### TypeScript

*package.json* கோப்பை திறந்து உள்ளடக்கத்தை பின்வரும் போல மாற்றவும், சர்வரை கட்டி இயக்க தேவையானவை உள்ளன:

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

*tsconfig.json* கொடுக்கப்பட்ட உள்ளடக்கத்துடன் உருவாக்கவும்:

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

உங்கள் மூலக் குறியீடு கோப்புகளுக்கான அடைப்பகம் உருவாக்கவும்:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* என்ற கோப்பை உருவாக்கவும்

```sh
touch server.py
```

#### .NET

தேவையான NuGet பேக்கேஜ்களை நிறுவவும்:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot திட்டங்கள் தானாகவே திட்ட அமைப்பு உருவாக்கும்.

#### Rust

Rust இல் `cargo init` இயக்கும் போது *src/main.rs* கோப்பு இயல்பாக உருவாகும். அதை திறந்து உள்ளடக்கத்தை நீக்கவும்.

### -4- சர்வர் குறியீட்டை உருவாக்குதல்

#### TypeScript

*index.ts* கோப்பை உருவாக்கி கீழ்காணும் குறியீட்டை சேர்க்கவும்:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// ஒரு MCP சேவையை உருவாக்குக
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

இப்போது ஒரு சர்வர் உள்ளது, ஆனால் அது அதிகமில்லை, அதைச் சரிசெய்வோம்.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ஒரு MCP சேவையகத்தை உருவாக்குக
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

Java க்கான அத்தியாய சர்வர் கூறுகளை உருவாக்கவும். முதலில், முதன்மை செயலி வகுப்பை மாற்றவும்:

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

கல்குலேட்டர் சேவையை உருவாக்கவும் *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**உற்பத்தி தயாரான சேவைக்கான விருப்ப கூறுகள்:**

துவக்கம் அமைப்பை உருவாக்கவும் *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

ஒரு சுகாதார கட்டுப்படுத்தியை உருவாக்கவும் *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

ஒரு தவறு கையாளுமுறை உருவாக்கவும் *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // பெறிகள்
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

தனித்துவமான பாணரை உருவாக்கவும் *src/main/resources/banner.txt*:

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

*src/main.rs* கோப்பின் மேலே கீழ்கண்ட குறியீட்டை சேர்க்கவும். இது MCP சர்வருக்கான தேவையான நூலகங்கள் மற்றும் தொகுதிகளை இறக்குமதி செய்கிறது.

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

கல்குலேட்டர் சர்வர் எளிமையான ஒன்று ஆகும், இரு எண்கள் கூட்டச் செய்யும். கல்குலேட்டர் கோரிக்கையை பிரதிநிதித்துவப்படுத்த struct ஒன்றை உருவாக்குவோம்.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

பின்னர், கல்குலேட்டர் சர்வரை பிரதிநிதித்துவப்படுத்த struct ஒன்றை உருவாக்குங்கள். இந்த struct உபகரண ரவுடரை வைத்திருக்கும், இது உபகரணங்களை பதிவு செய்வதற்காக பயன்படும்.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

இப்போது, சர்வரின் தகவலை வழங்க சர்வர் ஹேண்ட்லரை செயல்படுத்தும் `Calculator` struct ஐ உருவாக்க முடியும்.

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

கடைசியில், சர்வரை துவக்கும் மெயின் செயல்பாட்டை செயல்படுத்த வேண்டும். இந்த செயல்பாடு `Calculator` struct ஐ உருவாக்கி அதனை நிலை உள்ளீடு/வெளியீட்டில் வழங்கும்.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

சர்வர் இப்போது தன்னுடைய அடிப்படைக் தகவல்களை வழங்கத் தயாராக உள்ளது. அடுத்து, கூட்டல் செய்யும் உபகரணத்தை சேர்ப்போம்.

### -5- உபகரணமும் வளமும் சேர்த்தல்

தொடர்ந்து கீழ்காணும் குறியீட்டை சேர்க்க உபகரணமும் வளமும் உருவாக்கவும்:

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

உங்கள் உபகரணத்தின் அளவுருக்கள் `a` மற்றும் `b` ஆகும், மற்றும் இது பின்வரும் வடிவில் பதில்களை உருவாக்கும்:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

உங்கள் வளம் "greeting" என்ற சமன்வயத்தை கொண்டு அணுகப்படுகிறது, இது `name` என்ற அளவுருவை ஏற்று உபகரணத்தினைப் போல பதிலை உருவாக்கும்:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ஒரு கூட்டுதல் கருவியை சேர்
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ஒரு இயக்கத்தைக் கூற்றும் வரவேற்பு வளத்தைச் சேர்
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

மேலே உள்ள குறியீட்டில் நாம்:

- `add` என்பது `a` மற்றும் `b` என்ற முழு எண்களான அளவுருக்களைக் கொண்ட உபகரணமாக வரையறுத்தோம்.
- `greeting` என்ற வளத்தை உருவாக்கி அதில் `name` என்ற அளவுரு உண்டு.

#### .NET

உங்கள் Program.cs கோப்பில் இதை சேர்க்கவும்:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

மேற்கண்ட படியில் உபகரணங்கள் ஏற்கனவே உருவாக்கப்பட்டுள்ளன.

#### Rust

`impl Calculator` தொகுதியின் உள்ளே புதிய உபகரணத்தை சேர்க்கவும்:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- இறுதி குறியீடு

சர்வர் துவங்க வேண்டிய கடைசி குறியீட்டை சேர்ப்போம்:

#### TypeScript

```typescript
// stdin-ல் செய்திகளை பெற ஆரம்பித்து stdout-ல் செய்திகளை அனுப்பவும்
const transport = new StdioServerTransport();
await server.connect(transport);
```

முழு குறியீடு இங்கே:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ஒரு MCP சர்வரை உருவாக்கவும்
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// ஒரு சேர்க்கை கருவியைச் சேர்க்கவும்
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ஒரு மாற்றும் வாழ்த்து வளத்தைச் சேர்க்கவும்
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

// stdin இல் இருந்து செய்திகள் பெறத் தொடங்கி stdout இல் செய்திகள் அனுப்புதல் தொடங்கும்
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ஒரு MCP சர்வரை உருவாக்கவும்
mcp = FastMCP("Demo")


# ஒரு கூட்டல் கருவியைச் சேர்க்கவும்
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ஒரு மெய்நிகர் வாழ்த்துக்களை வழங்கும் வளத்தைச் சேர்க்கவும்
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# முக்கிய செயல்பாடுக் குழு - சர்வரை இயக்க இது அவசியமாகும்
if __name__ == "__main__":
    mcp.run()
```

#### .NET

கீழ்காணும் உள்ளடக்கத்துடன் Program.cs கோப்பை உருவாக்கவும்:

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

உங்கள் முழுமையான முதன்மை செயலி வகுப்பு இதுபோல இருக்கும்:

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

Rust சர்வருக்கான இறுதி குறியீடு இதுபோல இருக்கும்:

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

### -7- சர்வரை சோதனை செய்தல்

கீழ்காணும் கட்டளையுடன் சர்வரை துவங்கவும்:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP இன்ஸ்பெக்டரை பயன்படுத்த, `mcp dev server.py` ஐ பயன்படுத்தவும், இது இன்ஸ்பெக்டரை தானாக துவக்கி தேவையான பிராக்சி அமர்வு டோக்கனை வழங்கும். `mcp run server.py` ஐ பயன்படுத்துகின்றால், நீங்கள் இன்ஸ்பெக்டரை கைமுறையில் துவக்கி இணைப்பு அமைக்க வேண்டும்.

#### .NET

திட்ட அடைவில் இருப்பதை உறுதி செய்க:

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

திருத்தி இயக்க கீழ்காணும் கட்டளைகளை இயக்கவும்:

```sh
cargo fmt
cargo run
```

### -8- இன்ஸ்பெக்டர் மூலம் இயக்குதல்

இன்ஸ்பெக்டர் ஒரு சிறந்த கருவி, இது உங்கள் சர்வரை துவக்கி அதனுடன் தொடர்பு கொண்டு சோதிக்க அனுமதிக்கும். அதை துவங்குவோம்:

> [!NOTE]
> "command" புலத்தில் இருக்கும் கட்டளை உங்கள் runtime இல் சர்வரை இயக்கும் கட்டளையாக இருக்கும் மற்றும் பொதுவாக வேறுபடலாம்.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

அல்லது, உங்கள் *package.json* கோப்பில் இதுபோல் சேர்க்கவும்: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` பிறகு `npm run inspector` ஐ இயக்கவும்

#### Python

Python ஒரு Node.js கருவியான இன்ஸ்பெக்டரை சுற்றி இருக்கிறது. அதை இப்படி அழைக்க முடியும்:

```sh
mcp dev server.py
```

ஆனால், அது கருவியில் உள்ள அனைத்து முறைகளையும் செயல்படுத்தவில்லை என்பதனால், Node.js கருவியை நேரடியாக இயக்க பரிந்துரைக்கப்படுகிறது:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

எனவே, நீங்கள் கட்டளைகள் மற்றும் அளவுருக்களை அமைக்க அனுமதிக்கும் கருவி அல்லது IDE ஐ பயன்படுத்தினால்,
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

![Connect](../../../../translated_images/ta/tool.163d33e3ee307e20.webp)

**You're now connected to the server**
**The Java server testing section is completed now**

The next section it's about interacting with the server.

You should see the following user interface:

![Connect](../../../../translated_images/ta/connect.141db0b2bd05f096.webp)

1. Connect to the server by selecting the Connect button
  Once you connect to the server, you should now see the following:

  ![Connected](../../../../translated_images/ta/connected.73d1e042c24075d3.webp)

1. Select "Tools" and "listTools", you should see "Add" show up, select "Add" and fill in the parameter values.

  You should see the following response, i.e a result from "add" tool:

  ![Result of running add](../../../../translated_images/ta/ran-tool.a5a6ee878c1369ec.webp)

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
**பிரதி பொறுப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற க مصنوعி நுண்ணறிவு மொழிபெயர்ப்புச் சேவையால் மொழிபெயர்க்கப்பட்டுள்ளது. நாம் துல்லியத்திற்காக முயற்சி செய்கிறோம் என்றாலும், தானியங்கி மொழிபெயர்ப்புகளில் தவறுகள் அல்லது தவறான பகுதிகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனிக்கவும். அசல் ஆவணம் அதன் தாய்மொழியில் அல்லாத அதிர்ஷ்டமான ஆதாரமாகக் கருதப்பட வேண்டும். முக்கிய தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பினை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பைப் பயன்படுத்தியதால் ஏற்பட்ட எந்தப் புரிதல் தவறுகள் அல்லது தவறான விளக்கங்களுக்குமான பொறுப்பே நாம் ஏற்கவில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->